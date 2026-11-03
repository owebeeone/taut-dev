# Coordinated minor release status

Status: **accepted at root2b39a54a24a1b9e6c9d337b2a564d5a9c722c3e6 and the exact
member tuple in FinalAcceptance.json after both original reviewers reported GO**.
This accepts completed release evidence and the two future Python3.15 CI additions.

All five packages are published and verified: compiler taut-proto0.11.1, Python/Rust/
TypeScript shape0.11.0 and Rust foundation0.11.0. All five workflows succeeded;
strict compiler qualification and fresh public OFF/ON consumers passed. Compiler
0.11.0 remains intentionally absent after its failed publication, with its source
tag retained for foundation0.11.0. No tag/artifact was replaced.

Future3.15 CI was added to both Python matrices while retaining3.10–3.13 and all
existing integration commands. Ordinary commits fcfbe0c (Taut) and0488516
(Python shape) are pushed. Actual local3.15.2 passed1052 Taut Python-facing and190
shape tests plus public OFF/ON generation/execution. Hosted3.15 runs on the next
release; published artifact sources remain distinct and immutable.

The accepted root was pushed with all9 remote dependencies verified. See
FinalRemoteProof.json, FutureCIPush.json and FinalAcceptance.json. The receipt-only
descendant keeps that exact member tuple; its final checked-push SHA is recorded
in the final chat response and scratch/final-root-push.json.

All35 preserved artifacts and5 author files match, enum.case remains an ancestor,
all3 stashes are retained and unrelated/reference heads are unchanged. Taut has
exactly35 untracked user artifacts and zero tracked changes; other members are clean.
The bootstrap credential is revoked, its environment secret removed, and it must
never be retrieved/reused. No release work remains pending.

Completion.md is the full record; both final reviewer reports are verbatim.
Historical partial-boundary documents and original qualification snapshots remain
attributed to their original states.
