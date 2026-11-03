# Coordinated minor release completion

Status: **accepted at root2b39a54a24a1b9e6c9d337b2a564d5a9c722c3e6 and its
exact nine-member tuple after ReviewCode-Final.md and ReviewState-Final.md both
reported GO; this accepts completed publication/evidence and the two future-CI
additions only**. All five artifacts and workflows succeeded, public consumers
passed, both ordinary CI commits are pushed, and the accepted root was pushed
with all9 remote dependencies proven. FinalAcceptance.json records the verdict
merge; FinalRemoteProof.json records that actual checked push. This receipt-only
descendant preserves the same member tuple and is published with another checked push.
This is the current execution record; PublicationBoundary.md describes an earlier
partial boundary only. Historical reviews and qualifications retain their original scope.

| Public artifact | Version | Immutable source | Successful workflow |
|---|---|---|---|
| PyPI `taut-proto` | 0.11.1 | `0258b49e92c8b4ccd95027b4b10ad0b2f3992c52` | [41561903710](https://github.com/owebeeone/taut/actions/runs/41561903710) |
| PyPI `taut-shape` | 0.11.0 | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` | [41564573410](https://github.com/owebeeone/taut-shape-py/actions/runs/41564573410) |
| crates.io `taut-foundation` | 0.11.0 | `9260da45f486ed5a57aa399788c2936f2c044619` | [41536859807 attempt2](https://github.com/owebeeone/taut-shape-rs/actions/runs/41536859807/attempts/2) |
| crates.io `taut-shape` | 0.11.0 | `7f2a60747901fcf15362ab3c9a8af65c20faad68` | [41558306131](https://github.com/owebeeone/taut-shape-rs/actions/runs/41558306131) |
| npm `@owebeeone/taut-shape` | 0.11.0 | `79d3899b91af843b2295d089c82f6547ef97fde8` | [41537841200](https://github.com/owebeeone/taut-shape-ts/actions/runs/41537841200) |

## Qualification and public consumers

Compiler 0.11.1's exact Gearu candidate passed all 2566 required cases
(2562 native plus4 POSIX), zero failures/skips/omissions, with2574 collected
including8 separately accounted parity wrappers. All16 actual parity variants
passed88 rows each. Package build,132-file smoke and984 raw Git blob checks
passed for immutable source0258b49 and qualified tree
1773963420ab5be7aab1323865f09066ae2e65d84a0fe96a6caef1049cd211ca.
Hosted3.10–3.13 CI passed; its platform/tool skips are distinct from the strict
union's zero-skips qualification. Some C++ helpers select c++ before clang++;
actual CI includes coherent GNU routes plus the explicit Clang18/libstdc++13 wrapper.

Python shape's Gearu candidate passed190 tests; Rust shape passed108 tests,
clippy with warnings denied, no_std and exact package checks; TypeScript passed315
tests, typecheck and packed checks. Their original qualification records remain.

PublicArtifacts.json verifies downloaded PyPI wheels/sdists against registry and
actual CI output SHA256, npm SHA1/SHA512 integrity and gitHead, and both Rust VCS
sources and every archive payload byte. Foundation's independent local repack
has different compressed bytes; all12 payload entries match. Its actual CI
archive equals the public checksum. Rust shape's31 payload entries and compressed
archive match. These are separate claims, not a relabelled failed comparison.

PublicConsumers.json records fresh isolated Python/Rust/npm consumers using the
public PyPI compiler0.11.1 and runtime owners0.11.0. Validation OFF/ON, CBOR and
sparse JSON, frozen descriptors, shared nominal owners and mutable snapshot repair
passed where applicable. Generated Rust compiled and ran without workspace patches;
generated TypeScript compiled strictly and ran in Node; npm CJS/ESM owner identity
passed. Fresh ordinary npm install succeeded after the earlier metadata lag.

## Immutable corrective history

Compiler0.11.0's supported-Python workflow41557714352 failed, so that PyPI version
was never uploaded and remains intentionally absent. Its v0.11.0 tag/source is
retained; it remains the published foundation0.11.0 source. Compiler0.11.1 corrects
the POSIX obstruction preflight and qualifies CI tools, with unchanged canonical
C++/Rust runtimes. No tag was moved and no existing package was republished.
GitHub release notes now state the final corrective publication outcome.

Foundation's first bootstrap attempt failed403; no cause was inferred. After
explicit human authorization the temporary token was supplied through non-echoing
stdin, used for the initial workflow, then its GitHub environment secret was
deleted. The human confirmed revocation. Do not retrieve/reuse it. Rust shape
used its existing OIDC publisher unchanged. Final environment-secret inventory is empty.

## Future Python3.15 CI only

The human follow-up was: “For future runs, we probably should add3.15.” The
implementation retains3.10,3.11,3.12,3.13 and every existing integration command,
adding only one3.15 matrix entry to each Python publication workflow. It adds no3.14
and no allow-failure rule. No public artifact was rebuilt or retagged for this change.

Future Taut HEAD is `fcfbe0cfface9241c2b68542973936a166a0c8bc`; future Python shape HEAD is
`0488516aa1a5db94da44fdb10f12a7ec5bfd5940`. These differ from their published sources by that
single YAML matrix line only. FinalSourceProof.json verifies the exact bytes,
all984 immutable compiler release blobs, all nine member heads and preservation.

[Python.org](https://www.python.org/downloads/release/python-3152/) and the
[pinned official Actions manifest](https://raw.githubusercontent.com/actions/python-versions/160ca1e232997f36def6bb6e857f628222bef58a/versions-manifest.json)
confirm stable3.15.2, including Linux24.04/26.04 x64 availability. The official
Linux24.04 asset SHA256a945ca657bf4efeac7483c0c82381448d3b651a8d0e49be421c71fd53085cd01
was verified before isolated use. Actual local3.15.2 checks passed1052 Python-facing
Taut tests and all190 Python shape tests, plus fresh public-package OFF/ON generation
and consumer execution. Python315.json and the two JUnit files record exact scope.
The initial local harness attempt failed before collection in temporary capture
storage; it is retained, not counted as a pass. The dedicated-/var/tmp retry passed.
The new hosted3.15 jobs have not run: these release workflows trigger on the next
published release, and current immutable release CI remains3.10–3.13.

## Preservation and final workspace gate

All35 original untracked generated/wheel artifacts match their before hashes;
all5 protected authoring files match; enum.case5b5280ec remains an ancestor.
All3 reversible stashes remain retained. Taut has zero tracked changes and exactly
those35 untracked files; other members are clean. The read-only contract and four
unrelated members retain their original heads. GWZ must preserve this accurate
dirty-state warning rather than claim the whole workspace has no untracked files.

The same original Code+Surface and State reviewers independently reported GO
with zero blocking findings. Both reports are filed verbatim. No new architectural
root or remediation round was needed for this final object. Both ordinary main
commits and the accepted GWZ root were pushed with --check-remotes; all9 committed
dependencies were read and proven remotely. The final receipt-only root push
uses the same proof mode; its exact root SHA/transport receipt is recorded in
the final chat response and scratch/final-root-push.json. There is no remaining
release, runtime correction, credential action or registry upload for this train.
