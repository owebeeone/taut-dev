# Coordinated minor release — merged remediation 1

The original Code+Surface and State reports are filed verbatim. Both are
NO-GO; no public tag, GitHub Release or registry publication has occurred.
Their independent convergence is the execution-ledger cardinality defect.
This is one merged correction of bounded readiness behavior; canonical runtime
and generated API implementations remain unchanged.

| Finding | Disposition | Required closure |
|---|---|---|
| Code P2-1: xdist registration | Use explicit entry-point name `xdist`; gate establishes plugin isolation and clears inherited pytest options | Real isolated xdist probe with autoload enabled and disabled, ledger loaded and one execution |
| Code P2-2 / State P2-1: erased/missing phases | Record every phase event and worker; require exactly one passed setup/call/teardown per required ID | Real-hook serialized duplicate, call-only, missing teardown, repeated phase, failed-then-passed probes; real `--dist=each` rejection; full final Windows/WSL ledger |
| State P2-2: ambiguous publication recovery | Reconcile public API checksum, downloaded crate payload and exact VCS SHA against locally packaged reviewed source; only HTTP404 means absent | Controlled absent/upload, lost-response/rerun, matching existing, mismatching existing and network/lookup-error cases; actual workflow retains immutable SHA/tag guards and scoped secret |
| Owner smoke failure | Generate wheel then source at the same output path; retain wheel bytes in a verified sibling snapshot and compare all files/receipts byte for byte | Actual full wheel smoke gate; no manifest omission or semantic normalization |
| Owner WSL source-inventory boundary | Windows-created Gearu `.git` indirection is not a Linux Git path. Pass the native Git-collected exact inventory to POSIX and independently hash every named candidate file there | Real POSIX complement from same candidate, exact hash/ID union, no reliance on Linux interpreting a Windows gitdir |
| Owner host path and cleanup probes | Pass forward-slash paths through `wsl --exec`; run the small POSIX complement before the native partition. Confine cleanup to the created temporary root and retain extended Windows path spelling for namespace-adversity fixtures | Real path conversion and POSIX run; actual trailing-dot cleanup probe passed; all candidate failure receipts copied before cleanup |

The same two originators must verify their original counterexamples and the
changed-range/source association at the new committed tuple. Foundation
preflight and publication remain pending; Rust lock completion remains blocked
on actual foundation publication. No reviewer is added. Earlier candidate
results remain attributed to source17d3820 and are not final-source evidence.
Its actual native run completed 2552 passed, zero failed/skipped; all16 parity
variants and package build passed. The aggregate failed before POSIX execution
at Windows-backslash `wslpath` conversion; the independently inspected smoke
snapshots differ only in 18 path-bound ownership receipts. Original logs,
JUnit, raw-source inventories and hashes are preserved under
`coordinated-release-2026-11-03/failed-source-17d3820`.
