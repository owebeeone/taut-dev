# Taut 0.9 Release Train

Status: release candidate; packages and tags are not yet published

Date: 2026-08-25

## Version rule

Taut protocol and shape artifacts in a coordinated release share the same
major and minor version. Patch versions may advance independently when a fix is
isolated to one artifact.

For this train, every release coordinate is therefore `0.9.*`.

## Initial coordinates

| Repository | Artifact | Initial coordinate |
| --- | --- | --- |
| `taut` | PyPI `taut-proto` | `0.9.0` |
| `taut-shape` | contract/corpus Git tag | `v0.9.0` |
| `taut-shape-rs` | crates.io `taut-shape` | `0.9.0` |
| `taut-shape-ts` | npm `@owebeeone/taut-shape` | `0.9.0` |
| `taut-shape-py` | PyPI `taut-shape` | `0.9.0` |

The Python shape package requires `taut-proto>=0.9.0,<0.10`. A later patch may,
for example, pair `taut-proto 0.9.1` with unchanged `taut-shape 0.9.0` packages.

## Consumer boundary

Glial, Gryth, and Datascad are consumers of the train, not release artifacts in
the initial package publication. Their current development pins are replaced
only after the corresponding `0.9.*` artifacts exist in registries. If one of
those repositories is subsequently published as part of this coordinated Taut
train, its release coordinate must also remain in `0.9.*`.

Grip and other independent dependencies retain their own version lines.

## Publication order

1. Tag and publish `taut-proto 0.9.0`.
2. Tag the contract repository at `v0.9.0`.
3. Publish the Rust, TypeScript, and Python shape packages at `0.9.0`.
4. Replace consumer path/workspace/content pins with published `0.9.*` ranges or
   immutable release coordinates.
5. Run the strict release compatibility gate and consumer CI before declaring
   the train released.
