#!/usr/bin/env python3
"""Coordinate the Taut protocol/shape release train through GWZ.

Each package repository releases with gearu, which runs the package's own
checks, tags it and creates the GitHub Release that triggers its registry
workflow. The protocol goes first, from its own checkout::

    cd taut && gearu release X.Y.Z --push --github-release

After that artifact is visible on PyPI, this driver checks the train across
repositories, releases each shape package through gearu, and finally releases
the contract through gearu after consumer pins are released. Patch digits may vary inside one
major/minor train::

    python scripts/release.py check v0.9.0
    python scripts/release.py tag-shapes v0.9.0 --push --github-releases
    python scripts/release.py tag-package python v0.9.1 --push --github-release
    python scripts/release.py finalize v0.9.0 --push --github-release

Release tags are immutable. A pre-existing tag is accepted only when it points
at the current release commit.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "taut-shape"
TAG_PATTERN = re.compile(r"v(\d+)\.(\d+)\.(\d+)")

REPOS = {
    "protocol": {
        "target": "mem_taut",
        "path": ROOT / "taut",
        "github": "owebeeone/taut",
    },
    "contract": {
        "target": "mem_taut_shape",
        "path": ROOT / "taut-shape",
        "github": "owebeeone/taut-shape",
    },
    "rust": {
        "target": "mem_taut_shape_rs",
        "path": ROOT / "taut-shape-rs",
        "github": "owebeeone/taut-shape-rs",
    },
    "typescript": {
        "target": "mem_taut_shape_ts",
        "path": ROOT / "taut-shape-ts",
        "github": "owebeeone/taut-shape-ts",
    },
    "python": {
        "target": "mem_taut_shape_py",
        "path": ROOT / "taut-shape-py",
        "github": "owebeeone/taut-shape-py",
    },
    "glial": {
        "target": "mem_glial",
        "path": ROOT / "glial",
        "github": "owebeeone/glial-runtime",
    },
}

SHAPES = ("rust", "typescript", "python")
RELEASE_INPUTS = ("protocol", "contract", *SHAPES, "glial")


def fail(message: str) -> None:
    print(f"release: error: {message}", file=sys.stderr)
    raise SystemExit(1)


def log(message: str) -> None:
    print(f"release: {message}")


def run(
    command: list[object],
    *,
    cwd: Path = ROOT,
    capture: bool = False,
    check: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    argv = [str(part) for part in command]
    log("$ " + " ".join(argv))
    result = subprocess.run(
        argv,
        cwd=cwd,
        capture_output=capture,
        text=True,
        env=env,
    )
    if check and result.returncode:
        if capture and result.stdout:
            print(result.stdout)
        if capture and result.stderr:
            print(result.stderr, file=sys.stderr)
        fail(f"command failed ({result.returncode}): {' '.join(argv)}")
    return result


def require_tools(*names: str) -> None:
    missing = [name for name in names if shutil.which(name) is None]
    if missing:
        fail("missing required tools: " + ", ".join(missing))


def parse_tag(tag: str) -> str:
    match = TAG_PATTERN.fullmatch(tag)
    if match is None:
        fail(f"tag must look like vX.Y.Z, got {tag!r}")
    return ".".join(match.groups())


def gwz_args(names: tuple[str, ...], *command: str) -> list[str]:
    args = ["gwz", "--root", str(ROOT)]
    for name in names:
        args.extend(("--target", str(REPOS[name]["target"])))
    args.extend(command)
    return args


def git(
    name: str,
    *args: str,
    capture: bool = True,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    return run(
        ["git", *args],
        cwd=Path(REPOS[name]["path"]),
        capture=capture,
        check=check,
    )


def manifest() -> dict:
    return json.loads((CONTRACT / "release" / "compatibility.v1.json").read_text())


def scm_fallback(repo: Path) -> str:
    text = (repo / "pyproject.toml").read_text()
    section = re.search(r"(?ms)^\[tool\.setuptools_scm\]\s*(.*?)(?=^\[|\Z)", text)
    match = re.search(
        r'^fallback_version\s*=\s*"([^"]+)"',
        section.group(1) if section else "",
        re.MULTILINE,
    )
    if match is None:
        fail(f"{repo}: missing tool.setuptools_scm.fallback_version")
    return match.group(1)


def cargo_manifest_version(path: Path, section_name: str) -> str:
    text = path.read_text()
    section = re.search(
        rf"(?ms)^\[{re.escape(section_name)}\]\s*(.*?)(?=^\[|\Z)",
        text,
    )
    match = re.search(
        r'^version\s*=\s*"([^"]+)"',
        section.group(1) if section else "",
        re.MULTILINE,
    )
    if match is None:
        fail(f"{path}: missing {section_name}.version")
    return match.group(1)


def cargo_package_versions() -> dict[str, str]:
    repo = Path(REPOS["rust"]["path"])
    return {
        "workspace": cargo_manifest_version(repo / "Cargo.toml", "workspace.package"),
        "crate": cargo_manifest_version(
            repo / "crates" / "taut-shape" / "Cargo.toml", "package"
        ),
        "tool": cargo_manifest_version(
            repo / "crates" / "taut-shape-tool" / "Cargo.toml", "package"
        ),
    }


def package_versions() -> dict[str, str]:
    return {
        "rust": cargo_package_versions()["crate"],
        "typescript": str(
            json.loads((Path(REPOS["typescript"]["path"]) / "package.json").read_text())[
                "version"
            ]
        ),
        "python": scm_fallback(Path(REPOS["python"]["path"])),
    }


def assert_versions() -> None:
    data = manifest()
    expected = package_versions()
    errors = [
        f"{name}: package version {actual} != compatibility manifest {data['packages'][name]['version']}"
        for name, actual in expected.items()
        if actual != str(data["packages"][name]["version"])
    ]

    protocol = data["release_train"]["protocol_package"]
    protocol_version = str(protocol["version"])
    protocol_fallback = scm_fallback(Path(REPOS["protocol"]["path"]))
    if protocol_fallback != protocol_version:
        errors.append(
            f"protocol: pyproject fallback {protocol_fallback} != manifest {protocol_version}"
        )

    rust_versions = cargo_package_versions()
    if len(set(rust_versions.values())) != 1:
        errors.append(
            "rust: workspace/crate/tool versions differ: "
            + ", ".join(f"{name} {version}" for name, version in rust_versions.items())
        )

    train = data["release_train"]
    train_pair = (int(train["major"]), int(train["minor"]))
    for label, version in {"protocol": protocol_version, **expected}.items():
        parts = tuple(int(part) for part in version.split(".")[:2])
        if parts != train_pair:
            errors.append(
                f"{label}: {version} is outside train {train_pair[0]}.{train_pair[1]}.*"
            )
    if errors:
        fail("version preflight failed:\n  " + "\n  ".join(errors))


def assert_package_tag(name: str, tag: str) -> None:
    requested = parse_tag(tag)
    actual = package_versions()[name]
    recorded = str(manifest()["packages"][name]["version"])
    if actual != requested or recorded != requested:
        fail(
            f"{name}: requested {requested}, package version {actual}, "
            f"compatibility manifest {recorded}"
        )


def fetch_and_assert_synced(names: tuple[str, ...]) -> None:
    run(gwz_args(names, "--sync", "fetch-only", "pull", "--head"))
    errors: list[str] = []
    for name in names:
        branch = git(name, "branch", "--show-current").stdout.strip()
        if branch != "main":
            errors.append(f"{name}: branch is {branch!r}, expected 'main'")
            continue
        remote_ref = git(
            name,
            "rev-parse",
            "--verify",
            "origin/main",
            capture=True,
        ).stdout.strip()
        if not remote_ref:
            errors.append(f"{name}: origin/main is missing")
            continue
        counts = git(name, "rev-list", "--left-right", "--count", "HEAD...origin/main")
        ahead, behind = counts.stdout.split()
        if (ahead, behind) != ("0", "0"):
            errors.append(f"{name}: main is ahead {ahead}, behind {behind} relative to origin/main")
    if errors:
        fail("synchronization preflight failed:\n  " + "\n  ".join(errors))


def assert_clean(names: tuple[str, ...]) -> None:
    result = run(gwz_args(names, "status", "--porcelain"), capture=True)
    if result.stdout.strip():
        fail("release input trees are dirty:\n" + result.stdout.rstrip())


def run_check(tag: str, *, tests: bool) -> None:
    parse_tag(tag)
    require_tools("git", "gwz", "python3")
    assert_versions()
    fetch_and_assert_synced(RELEASE_INPUTS)
    assert_clean(RELEASE_INPUTS)

    run(["python3", "release/check_compatibility.py"], cwd=CONTRACT)
    if not tests:
        log("skipping package and interoperability tests")
        return

    require_tools("cargo", "pnpm", "uv")
    run(
        [
            "cargo",
            "test",
            "--workspace",
            "--locked",
        ],
        cwd=Path(REPOS["rust"]["path"]),
    )
    run(
        ["cargo", "clippy", "--workspace", "--all-targets", "--locked", "--", "-D", "warnings"],
        cwd=Path(REPOS["rust"]["path"]),
    )
    run(
        ["cargo", "build", "-p", "taut-shape", "--no-default-features", "--locked"],
        cwd=Path(REPOS["rust"]["path"]),
    )
    run(
        ["cargo", "package", "-p", "taut-shape", "--locked"],
        cwd=Path(REPOS["rust"]["path"]),
    )

    run(["pnpm", "install", "--frozen-lockfile"], cwd=Path(REPOS["typescript"]["path"]))
    run(["pnpm", "typecheck"], cwd=Path(REPOS["typescript"]["path"]))
    run(["pnpm", "test"], cwd=Path(REPOS["typescript"]["path"]))
    with tempfile.TemporaryDirectory(prefix="taut-shape-ts-pack-") as pack_dir:
        run(["pnpm", "pack", "--pack-destination", pack_dir], cwd=Path(REPOS["typescript"]["path"]))

    python_env = os.environ.copy()
    python_env["PYTHONPATH"] = os.pathsep.join(
        (str(Path(REPOS["protocol"]["path"]) / "src"), str(Path(REPOS["python"]["path"]) / "src"))
    )
    run(
        ["uv", "run", "--no-project", "--with", "pytest", "python", "-m", "pytest", "-q"],
        cwd=Path(REPOS["python"]["path"]),
        env=python_env,
    )
    build_env = os.environ.copy()
    python_version = str(manifest()["packages"]["python"]["version"])
    build_env["SETUPTOOLS_SCM_PRETEND_VERSION_FOR_TAUT_SHAPE"] = python_version
    run(
        ["uv", "run", "--no-project", "--with", "build", "python", "-m", "build"],
        cwd=Path(REPOS["python"]["path"]),
        env=build_env,
    )

    matrix_env = os.environ.copy()
    matrix_env["PYTHONPATH"] = os.pathsep.join(
        (str(Path(REPOS["python"]["path"]) / "src"), str(Path(REPOS["protocol"]["path"]) / "src"))
    )
    run(
        ["uv", "run", "--no-project", "--with", "pytest", "python", "-m", "pytest", "-q", "matrix/driver.py", "matrix/test_harness.py", "release/test_compatibility.py"],
        cwd=CONTRACT,
        env=matrix_env,
    )
    log(f"shape release gates passed for the {parse_tag(tag).rsplit('.', 1)[0]}.* train")










def gearu_release(names: tuple[str, ...], tag: str, *, push: bool, github_release: bool) -> None:
    """Release each package with gearu, from its own checkout. gearu runs the package's checks on a
    candidate, tags it and, with `push`, pushes the branch and the tag together; with
    `github_release` it creates the GitHub Release that starts the package's registry workflow.
    Rerunning a version gearu has tagged resumes it rather than moving the tag."""
    require_tools("gearu")
    for name in names:
        command = ["gearu", "release", parse_tag(tag)]
        if push:
            command.append("--push")
        if github_release:
            command.append("--github-release")
        run(command, cwd=Path(REPOS[name]["path"]))


def tag_shapes(args: argparse.Namespace) -> None:
    shape_version = parse_tag(args.tag)
    if args.github_releases and not args.push:
        fail("--github-releases requires --push")
    if not args.skip_check:
        run_check(args.tag, tests=not args.skip_tests)
    else:
        assert_versions()
        fetch_and_assert_synced(RELEASE_INPUTS)
        assert_clean(RELEASE_INPUTS)
    versions = package_versions()
    mismatches = [name for name in SHAPES if versions[name] != shape_version]
    if mismatches:
        fail(
            f"tag-shapes requires one shared patch; {args.tag} does not match "
            + ", ".join(f"{name} {versions[name]}" for name in mismatches)
        )
    gearu_release(SHAPES, args.tag, push=args.push, github_release=args.github_releases)


def tag_package(args: argparse.Namespace) -> None:
    if args.github_release and not args.push:
        fail("--github-release requires --push")
    assert_package_tag(args.package, args.tag)
    if not args.skip_check:
        run_check(args.tag, tests=not args.skip_tests)
    else:
        fetch_and_assert_synced(RELEASE_INPUTS)
        assert_clean(RELEASE_INPUTS)
    gearu_release((args.package,), args.tag, push=args.push, github_release=args.github_release)


def finalize(args: argparse.Namespace) -> None:
    parse_tag(args.tag)
    if args.github_release and not args.push:
        fail("--github-release requires --push")
    fetch_and_assert_synced(RELEASE_INPUTS)
    assert_clean(RELEASE_INPUTS)
    run(["python3", "release/check_compatibility.py", "--release"], cwd=CONTRACT)
    gearu_release(("contract",), args.tag, push=args.push, github_release=args.github_release)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check", help="run release preflight and package gates")
    check_parser.add_argument("tag", help="shape release tag, e.g. v0.9.0")
    check_parser.add_argument("--skip-tests", action="store_true")

    tag_parser = subparsers.add_parser("tag-shapes", help="tag the three language packages")
    tag_parser.add_argument("tag", help="shape release tag, e.g. v0.9.0")
    tag_parser.add_argument("--push", action="store_true")
    tag_parser.add_argument("--github-releases", action="store_true")
    tag_parser.add_argument("--skip-check", action="store_true")
    tag_parser.add_argument("--skip-tests", action="store_true")

    package_parser = subparsers.add_parser(
        "tag-package", help="tag one language package at an independent patch"
    )
    package_parser.add_argument("package", choices=SHAPES)
    package_parser.add_argument("tag", help="package release tag, e.g. v0.9.1")
    package_parser.add_argument("--push", action="store_true")
    package_parser.add_argument("--github-release", action="store_true")
    package_parser.add_argument("--skip-check", action="store_true")
    package_parser.add_argument("--skip-tests", action="store_true")

    final_parser = subparsers.add_parser("finalize", help="strict-gate and tag the contract")
    final_parser.add_argument("tag", help="contract release tag, e.g. v0.9.0")
    final_parser.add_argument("--push", action="store_true")
    final_parser.add_argument("--github-release", action="store_true")

    args = parser.parse_args()
    if args.command == "check":
        run_check(args.tag, tests=not args.skip_tests)
    elif args.command == "tag-shapes":
        tag_shapes(args)
    elif args.command == "tag-package":
        tag_package(args)
    else:
        finalize(args)


if __name__ == "__main__":
    main()
