# Taut 0.9 Release Train

Status: released

Date: 2026-08-26

## Version rule

Taut protocol and shape artifacts in a coordinated release share the same
major and minor version. Patch versions may advance independently when a fix is
isolated to one artifact.

For this train, every release coordinate is therefore `0.9.*`.

## Initial coordinates

| Repository | Artifact | Initial coordinate |
| --- | --- | --- |
| `taut` | PyPI `taut-proto` | `0.9.1` |
| `taut-shape` | contract/corpus Git tag | `v0.9.0` |
| `taut-shape-rs` | crates.io `taut-shape` | `0.9.1` |
| `taut-shape-ts` | npm `@owebeeone/taut-shape` | `0.9.2` |
| `taut-shape-py` | PyPI `taut-shape` | `0.9.1` |

The Python shape package requires `taut-proto>=0.9.1,<0.10`. Its patch advanced
to 0.9.1 after the 0.9.0 GitHub workflow found that the wheel depended on schema
files in a sibling contract checkout. No 0.9.0 Python artifact reached PyPI.
The corrected wheel bundles those canonical schemas; Rust and TypeScript remain
in the `0.9.*` train. TypeScript advanced to 0.9.1 after its 0.9.0 bootstrap
package was found to export raw `.ts` files that Node refuses to load from
`node_modules`; 0.9.1 instead ships compiled JavaScript and declarations.

## Consumer boundary

Glial, Gryth, and Datascad are consumers of the train, not release artifacts in
the initial package publication. Their current development pins are replaced
only after the corresponding `0.9.*` artifacts exist in registries. If one of
those repositories is subsequently published as part of this coordinated Taut
train, its release coordinate must also remain in `0.9.*`.

Grip and other independent dependencies retain their own version lines.

## Publication order

1. Tag and publish `taut-proto 0.9.1`. (Complete.)
2. Publish Rust `taut-shape 0.9.0`. (Complete.)
3. Publish Python `taut-shape 0.9.1`. (Complete.)
4. Publish TypeScript `@owebeeone/taut-shape 0.9.1`. (Complete.)
5. Replace the required Glial consumer path pin with `^0.9.1`. (Complete.)
   Optional prototype consumers retain their documented development pins.
6. Run the strict release compatibility gate and consumer CI. (Complete.)
7. Tag the contract repository at `v0.9.0` and declare the train released.
   (Complete.)

`taut-proto` tag `v0.9.0` was withdrawn before PyPI publication after its
release workflow exposed a Python 3.11 dataclass compatibility issue. The tag
is retained immutably for auditability; `v0.9.1` contains the fix.

The same immutable-tag rule applies to Python `taut-shape` v0.9.0: its release
workflow failed before registry publication, so v0.9.1 carries the standalone
wheel correction.

TypeScript `v0.9.0` is also retained immutably. Its bootstrap artifact reached
npm before the raw-TypeScript consumer-install defect was found; v0.9.1 carries
the compiled-package correction and the release workflow now tests the packed
tarball through a clean consumer installation.

Rust `v0.9.1` and TypeScript `v0.9.2` are corrective release-workflow patches.
Their tag-triggered runs use the standalone workflows that check out the
contract corpus before testing. The earlier failed tag runs remain historical;
their immutable tags are not moved.

## Release tooling (2026-09-30)

Every repository in the train now releases with [gearu](https://github.com/owebeeone/gearu):
taut (`taut-proto`), taut-shape-py, taut-shape-rs, taut-shape-ts and the contract, taut-shape. Each
keeps a `gearu.toml`, whose checks are the ones its CI runs before it publishes, and a `RELEASE.md`.
- `gearu release X.Y.Z --push --github-release` runs the repository's checks on a candidate and tags
  it. It pushes the branch and the tag together, and creates the GitHub Release that starts the
  registry workflow.
- `scripts/release.py tag-shapes`, `tag-package` and `finalize` still run this train's
  cross-repository checks: versions against the compatibility manifest, every input synced and
  clean, and each package's gates. They then call gearu for each repository instead of tagging it
  themselves.
- Each shape package's checks read the contract corpus from the `taut-shape` checkout beside it, as
  CI does, so shape releases run from this workspace.
- The contract publishes nothing. Its `pyproject.toml` exists for gearu, with the tag as its
  version, which the manifest's `contract_version` must equal. Its gearu check is the release gate,
  `release/check_compatibility.py --release`, which reads the release inputs from this workspace.
