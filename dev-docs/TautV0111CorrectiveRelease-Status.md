# Taut0.11.1 corrective release status

Corrective source0258b49e92c8b4ccd95027b4b10ad0b2f3992c52 was accepted GO/GO
by the original reviewers at root1fc9e8101a7cf68b0ec8847e52a8126315fc0720.
Its complete unchanged Gearu candidate passed2566 required cases, all16x88
parity, package/build/smoke and984 immutable raw Git blob checks. Qualification.json
remains the original pre-push snapshot, not relabelled publication evidence.

Gearu pushed immutable v0.11.1 and created its GitHub Release. Workflow41561903710
terminated SUCCESS across3.10–3.13 tests/build/PyPI. Compiler0.11.1 is public;
compiler0.11.0 remains absent after its failed workflow, with its old tag retained.
Foundation0.11.0 still corresponds to9260da4; its canonical runtime is unchanged.

All five intended artifacts and publication workflows are now successful. Python
shape190-test Gearu qualification and publication41564573410 passed. Exact public
artifact verification and fresh generated public Python/Rust/npm consumers passed,
including validation OFF/ON and shared owner identity. See the consolidated
CoordinatedMinorRelease-Completion.md and final machine-readable receipts.

The two future3.15 CI-only commits are distinct from public artifact sources.
Actual local3.15.2 passed1052 Taut Python-facing and190 shape tests plus public
OFF/ON consumers. Hosted3.15 remains a next-release matrix entry. C++ qualification
includes coherent GNU selections and an explicit Clang18/libstdc++13 wrapper;
no claim is made that every helper selects that wrapper.

All35 preserved artifacts and5 author files match; enum.case remains an ancestor,
all3 stashes remain. The temporary bootstrap token is revoked and its environment
secret removed; never retrieve/reuse it. Final receipt review returned GO/GO and the accepted root was pushed with all9
remote dependencies verified. The consolidated final acceptance records completion.
