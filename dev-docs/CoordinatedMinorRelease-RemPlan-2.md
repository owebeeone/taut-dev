# Coordinated minor release — merged remediation 2

Both same-originator R1 reports close their original findings and identify the
same new bounded host-capture defect (Code P2-3 / State P2-3), explicitly not a
new architectural root cause. R1 source092f0b4 remains an overall failed
candidate: all16 parity variants, package build and 132-file strict smoke
passed, but POSIX capture exited3 before any case execution. It created no tag.

The one source correction is explicit `--capture=sys` for the POSIX partition.
It preserves all four case IDs and assertions, native/independent file hashing,
complete phase/worker event accounting and no-skip/error rules. The source-only
probe at the same DrvFS TMPDIR passed four cases with exactly three passing
phases each; it is supporting host evidence, not final candidate qualification.

Closure requires a fresh committed source and actual Gearu candidate passing
the complete native/WSL union, all16 mandatory parity variants, complete package
checks and raw-byte smoke. The SAME Code+Surface and State originators must
verify that exact source/candidate tuple and their original P2-3 counterexample.
No additional reviewer or unrelated source/coverage change is authorized by
this plan. Original R0/R1 results retain their immutable-source attribution.
