# Coordinated 0.11 minor release

Status: readiness source drafted; public release blocked until the combined
Code+Surface and State review accepts the exact candidate and every named gate
passes. Human authorization explicitly covers Gearu commits/tags/GitHub
Releases, registry publication, necessary readiness fixes and foundation.

## Scope and release matrix

| Repository/package | Gearu plan | Dependency/publication order |
|---|---|---|
| Taut / PyPI `taut-proto` | 0.11.0, highest existing tag 0.10.1 | Prepare local candidate; push only after acceptance; publish PyPI after foundation |
| Taut / crates.io `taut-foundation` | initial 0.11.0; internal manifest was unpublished 0.10.0 | Taut Gearu Rust adapter sets version; existing Rust shape environment bootstraps canonical crate first |
| Python shape / PyPI `taut-shape` | 0.11.0 from 0.10.0 | After public `taut-proto` 0.11.0; pin `>=0.11.0,<0.12` |
| Rust shape / crates.io `taut-shape` | 0.11.0 from 0.10.0 | After public foundation 0.11.0; remove local patch and resolve real registry checksum |
| TypeScript shape / npm `@owebeeone/taut-shape` | 0.11.0 from 0.10.0 | Frozen declared dependencies; standalone package build and consumption |

Plans inspect remote tags directly. All five package versions remain pinned
explicitly during execution. Never overwrite a published version or tag.
The shared contract repository is a read-only test input, not another release.
Unfinished language libraries and unrelated workspace members are out of scope.

## Observed readiness defects and bounded remedies

The archived proto API design was still tested at its former active location;
the test now checks the actual archived document with every contract assertion
retained. Two Go formatting probes wrote platform-default CRLF on Windows;
they now write UTF-8 LF, retaining native gofmt checks. All three passed on
native Windows. The missing Windows Rust wasm32 standard library was installed
and its real Node-executed 32-bit length test passed.

The suite contains both Windows-only MSVC/junction/namespace cases and
POSIX-only fake-process/PATH/symlink cases. No single OS can execute their union
without skips. The qualified gate uses the existing nine-toolchain Windows
environment and Ubuntu WSL for the four explicitly marked POSIX cases. It
collects the exact required ID universe at the same raw candidate bytes,
records host assignments and all execution phases, and rejects failed,
skipped, duplicated, missing, extra or source-mismatched execution. The eight
existing parity wrappers are accounted for by the actual mandatory
`tautc parity --require-all` run: all 16 variants, all 88 rows each. No name
reservation regression test is deselected. No OS security policy is changed.

Gearu candidates need immutable sibling composition inputs that the former
configuration did not supply. `taut/release-inputs.json` pins all four to exact
commits; preparation clones those commits with LF checkout and frozen package
dependencies. Those sibling commits intentionally precede publication: Rust's
registry lock refresh is pending the first foundation publication. The Taut
composition tests use an explicitly patched source owner, and the final Rust
release gates must separately package and consume the real registry owner.

Foundation already derives its runtime from canonical source with a byte-hash
provenance inventory. Metadata, README, license, include closure and Gearu
checks make it a self-contained publishable crate without another runtime
implementation. Its version changes only through Gearu. The actual Rust
composition fixture reads that manifest version rather than hardcoding 0.10.

## Credential and bootstrap boundary

GitHub account authentication works. `taut-foundation` is absent on crates.io.
There are no local registry tokens. The existing Rust shape `crates-io`
environment contains `CARGO_REGISTRY_TOKEN`; only its metadata was inspected.
Its token scope is not yet proven. The new `foundation.yml` preflight checks
canonical packaging and secret presence without printing or exporting secrets.
After acceptance and a successful Gearu candidate, push its source commit/tag
without a GitHub Release. The workflow publishes only from the exact Taut SHA
and matching immutable tag. Any actual credential/scope failure blocks the
Python GitHub Release and the rest of the train. A local Cargo publish is
prohibited. Public foundation success precedes Taut's GitHub Release/PyPI.

## Acceptance and completion

Exactly two peer-blind reviewers cover the aggregate revision: Code+Surface
and State. They audit this authority/scope, migration notes, source and
candidate association, platform coverage, packaging, credential boundaries,
immutability and partial-publication recovery. Their reports are filed
verbatim. A single bounded patch merges any blocking findings; the same
originators verify closure. Mechanical registry-lock completion and Gearu's
version commit receive their same-axis final checks at the exact tuple.

Publication is complete only when all relevant workflows terminate successfully,
public registry versions are visible, clean index consumers outside source
checkouts compile/run generated codecs/descriptors and validation OFF/ON as
appropriate, nominal identity is proven across actual package boundaries, and
final GWZ workspace receipts/remote heads agree. Nine implementation languages
are accepted checkpoint content, not nine shape-library releases. Pre-1.0 ABI,
packaging and generated API changes receive honest minor migration notes.

## Preservation

The user's enum.case commit remains an ancestor, including metadata-like enum
names and all namespace regression cases. Five protected authoring files and
35 generated/wheel artifacts are excluded from release changes. The 35 are in
an exact-path reversible stash with before hashes and stash-object byte proof
under `D:/projects/limbo/coordinated-release-2026-11-03`; restore and rehash them
after release. Unrelated members and unfinished libraries remain untouched.
