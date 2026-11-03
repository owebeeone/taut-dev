# CoordinatedMinorRelease Final Receipt and Future CI — STATE-AXIS REVIEW

**Review object:** Final evidence and future Python 3.15 CI additions at root `2b39a54a24a1b9e6c9d337b2a564d5a9c722c3e6`, controlled by `dev-docs/CoordinatedMinorRelease-Final-DRAFT.md`.

**Baseline:** Published Taut `0258b49e92c8b4ccd95027b4b10ad0b2f3992c52` and Python shape `d33a069198c5540bfdd5b92b6ff22615d8113fa1`; accepted Rust/TypeScript sources unchanged. Sources were read through immutable Git objects and complete published-source-to-current diffs.

**Date:** 2026-11-03

**Axis:** State — publication transitions, source/artifact association, evidence durability and preservation. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — no blocking finding. Accept the final receipt and two future-CI commits at this tuple. Final GWZ acceptance/push and checked remote proof remain subsequent actions, not completed facts established here.

---

## 0. Evidence base

All named commit objects and actual HEADs matched at both start and end:

| Component | Reviewed commit |
|---|---|
| Root | `2b39a54a24a1b9e6c9d337b2a564d5a9c722c3e6` |
| Taut future CI | `fcfbe0cfface9241c2b68542973936a166a0c8bc` |
| Python shape future CI | `0488516aa1a5db94da44fdb10f12a7ec5bfd5940` |
| Rust shape | `7f2a60747901fcf15362ab3c9a8af65c20faad68` |
| TypeScript shape | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |
| glade | `491dda9645a3ef76b6c1632fbb6bddef926e40a7` |
| glade-decl-ts | `f1b7492f3a970a8af25415356c3fb62db40c4a15` |
| glial | `6a9a9e216629ccdd6b57aa0c66436d5fa7e0e654` |
| grip-core | `b9d7149a1c3748ad2b4490d9d70ca23ee121268f` |

Inspected the controlling DRAFT, Completion, Status, FinalEvidence, FinalSourceProof, PublicArtifacts, PublicConsumers, FinalRegistries, Python315, availability receipt and both committed JUnit reports. Read the artifact/consumer verification programs and corresponding retained logs.

Independent read-only checks established:

- All five GitHub publication runs are **completed/success** at their recorded sources: compiler `41561903710`, Python shape `41564573410`, foundation `41536859807` attempt 2, Rust shape `41558306131`, TypeScript shape `41537841200`.
- All **984 immutable compiler release blobs** match the actual qualified inventory: zero mismatches.
- Strict qualification records **2,562 native + four POSIX cases**, complete passing phase sequences, matching raw hashes, and sixteen parity variants accounting for 88 rows each.
- All seven linked evidence files match their committed byte lengths and SHA256 values.
- All **35 restored artifacts and five protected files** match the original before-hashes. The untracked path set equals exactly the original 35 paths.
- All nine member trees have zero tracked changes; all three preservation stashes remain retained; enum-case ancestry remains intact.
- Python 3.15 XML records **1,052 Taut and 190 shape passes**, with zero failures/errors/skips.

No builds, tests, writes, registry actions or credential access were performed.

## Problem, requirement provenance, and scope

The original human instruction authorizes the coordinated releases and final evidence. Subsequent steering authorizes compiler 0.11.1 with foundation/shape 0.11.0 retained. The latest follow-up explicitly requests Python 3.15 for future runs.

Each complete implementation diff changes only one workflow matrix line, adding 3.15 while retaining 3.10–3.13 and every integration command. There is no 3.14 addition, failure masking, runtime change, new package version or tag movement.

The final object accurately consolidates completed publication and consumer evidence. Root acceptance and remote proof remain later gates. No unsupported prerequisite or scope expansion was established.

## 2. Invariant analysis

**Published sources remain distinct from future HEADs.** Taut’s public 0.11.1 tag resolves to `0258b49`; Python shape’s 0.11.0 tag resolves to `d33a069`. Their future CI heads differ only by the matrix additions. Rust/TypeScript tags retain their accepted release commits. Taut’s historical 0.11.0 tag still names `9260da4`; its failed PyPI publication is not relabelled as success.

**Publication is supported by artifacts and execution.** The inspected verification code and receipts connect PyPI wheel/sdist digests to registry downloads and CI distributions; npm integrity/gitHead to its release; and both Rust archives to exact VCS identities and complete payloads. Foundation’s differing local compressed archive remains explicitly distinguished from its twelve equal payload entries. Rust shape’s 31 payload entries and archive checksum agree.

Fresh public consumers use compiler 0.11.1 and runtime owners 0.11.0. The harness clears source-path overrides, uses isolated installations, checks Rust registry identities and exercises OFF/ON behavior, codecs, descriptors and shared owners. npm CJS/ESM identity is explicitly checked.

**Python 3.15 claims are bounded correctly.** The pinned official Actions manifest independently confirms stable 3.15.2 assets for the relevant Linux versions. Local receipts identify the actual runtime and selected Taut test scope. The first temporary-capture attempt remains failed; the dedicated `/var/tmp` retry supplies the passing results. Neither local execution nor historical release CI is presented as completed hosted 3.15 qualification.

**Preservation and completion language remain honest.** Restored user files are verified, retained stashes remain available, and Taut’s expected untracked-file warning is preserved. Historical partial-boundary absence claims are identified as historical. Revoked credentials are neither required nor reused.

Prior State findings remain closed. No new architectural root cause was established.

## 3. Risks and next action

File both final reports, accept this exact tuple, push the two ordinary CI commits and complete the GWZ root push with checked proof for all nine remote dependencies.

Record that final remote result before declaring workspace completion. Hosted Python 3.15 execution remains future coverage on the next release; no additional release or registry upload is required for these CI changes.
