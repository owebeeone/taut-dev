# Taut 0.11.1 corrective release status

Status: **source accepted at Taut0258b49e92c8b4ccd95027b4b10ad0b2f3992c52,
root1fc9e8101a7cf68b0ec8847e52a8126315fc0720, after both original reviewers
reported GO in TautV0111CorrectiveRelease-ReviewCode.md and ReviewState.md**.
This accepts the five-file corrective source only. Full exact candidate
qualification, hosted publication and final public consumers remain required.

The configured Gearu0.11.1 qualification PASSED on unchanged source. All2574
cases were collected:2562 native plus4 POSIX required cases passed with exact
phase/cardinality coverage and zero skips/failures/omissions; eight duplicate
parity wrappers are accounted by the actual16 variants,88 rows each. Package,
132-file raw-byte smoke and exact checks passed. All984 raw committed blobs
match the qualified candidate, tree1773963420ab5be7aab1323865f09066ae2e65d84a0fe96a6caef1049cd211ca.
Native tests took641.08s. Evidence is retained in gate-evidence/taut-release-checks-j9c7b2kd.
No old qualification is relabelled to this source. Existing v0.11.0 remains
immutable and its PyPI workflow failed; no compiler0.11.0 package was uploaded.

Gearu atomically pushed0258b49/v0.11.1 and created its GitHub Release. The
supported-Python publication workflow41561903710 is now running. Both GitHub
Release notes explicitly distinguish the held0.11.0 PyPI version and corrective
0.11.1; no tag or existing artifact was replaced. Public PyPI is still a
required completion gate, not inferred from that release or a queued workflow.

Public foundation0.11.0 and Rust shape0.11.0 archives have exact source/payload
verification. A fresh registry-only Rust consumer passed OFF/ON CBOR execution
and nominal descriptor/validation owner identity. Generated semantic consumers
using the eventual public compiler0.11.1 are still a separate final gate.
TypeScript0.11.0 remains published and verified; no republish is needed.

C++ qualification includes coherent GNU routes as selected by existing tests,
plus the explicit Clang18/libstdc++13 wrapper. Some helpers prefer c++ before
clang++; final CI receipts must report actual tool selection accurately, not
claim every invocation uses that wrapper. No C++ source or test was changed.

Python shape source d33a069 remains accepted, and its0.11.0 release waits for
public compiler0.11.1. Its dependency range admits that compiler patch.
The original temporary token is revoked, its GitHub secret removed, and it
must never be accessed/reused. No remaining publication requires it.
