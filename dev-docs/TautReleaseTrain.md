# Taut 0.9 Release Train

Status: package publication complete; required consumer and contract finalization in progress

Date: 2026-08-25

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
| `taut-shape-rs` | crates.io `taut-shape` | `0.9.0` |
| `taut-shape-ts` | npm `@owebeeone/taut-shape` | `0.9.1` |
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
6. Run the strict release compatibility gate and consumer CI.
7. Tag the contract repository at `v0.9.0` and declare the train released.

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
