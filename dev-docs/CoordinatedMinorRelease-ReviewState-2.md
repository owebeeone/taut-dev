# CoordinatedMinorRelease — STATE-AXIS REVIEW — REMEDIATION 2

**Review object:** Readiness source and successful Taut local release preparation, controlled by `dev-docs/CoordinatedMinorRelease-DRAFT.md` and `CoordinatedMinorRelease-RemPlan-2.md` at root `6cb4ad603f4a0b0a96066a3f9a9490e15006f385`.

**Baseline:** R1 root `4c8bcdca1cfb49d0f5d9bc3aaf7fd51db9a76a2f`, Taut `092f0b4871f33a93fe452ca25eab092e544516ea`; other members unchanged. Inspection used immutable Git objects and exact-range diffs.

**Date:** 2026-11-03

**Axis:** State — release recovery, filesystem isolation, source association and fail-closed evidence. Independent, adversarial, read-only, by the original State reviewer. Prior reports were legitimate inputs; no current peer R2 report was accessed. Filed verbatim by the lane owner.

**Verdict: GO** — all three State findings are closed; no open P0–P2 findings. This accepts readiness and the verified Taut local preparation, not public publication or completion of the coordinated train.

---

## Prior-finding closure

| Finding | Disposition | Verified closure |
|---|---|---|
| P2-1: execution multiplicity/incomplete phases erased | **Closed** | Retained R1 event-cardinality correction and real duplicate-execution regressions. Final candidate records exactly one complete passing phase sequence per required case. |
| P2-2: ambiguous foundation upload lacks recovery | **Closed at readiness-source level** | Unchanged reviewed reconciliation verifies registry checksum, complete payload and clean VCS identity; six controlled tests cover interrupted upload, matching/mismatching versions and lookup failures. Actual publication remains pending. |
| P2-3: POSIX capture fails before execution | **Closed** | Actual isolated Gearu candidate uses `--capture=sys`; all four original POSIX cases pass with complete phases, matching independently computed source hashes and successful final native/WSL union. |

## Changed-range analysis and classification

The entire Taut correction `092f0b4..c426a9a` adds `--capture=sys` to the POSIX invocation and two explanatory lines in `RELEASE.md`. It changes no test IDs, assertions, runtime, schema, inventory or coverage requirements.

Gearu’s subsequent `c426a9a..9260da4` delta changes only foundation’s manifest version from `0.10.0` to `0.11.0`.

Root changes file the prior reports/remediation plan and update managed receipts. No new architectural root cause or unauthorized expansion was established.

## 0. Evidence base

Reviewed immutable tuple:

| Component | Commit |
|---|---|
| Root | `6cb4ad603f4a0b0a96066a3f9a9490e15006f385` |
| Taut readiness source | `c426a9acc40406e41d82649e84960472510445a9` |
| Taut local release | `9260da45f486ed5a57aa399788c2936f2c044619` |
| Rust shape | `506b60ef059208c9dd7a1d85fa6df4deb8824577` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| TypeScript shape | `1aaeab65e4564a462044d2f5d824cd2f375aae97` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

The source objects matched at start/end. The final release object and local `v0.11.0` tag were checked after creation; the tag resolves to `9260da45f486ed5a57aa399788c2936f2c044619`.

Read the committed RemPlan-2, both verbatim R1 reports, complete correction/version diffs, `qualified-candidate-proof.json`, `qualified-source-c426a9a-release-9260da4.log`, and final receipts under:

`D:/projects/limbo/coordinated-release-2026-11-03/gate-evidence/taut-release-checks-a_hs5j50`

Verified:

- 2,572 collected IDs; 2,560 native plus four POSIX cases; 2,564 required cases and eight separately accounted parity wrappers.
- Both execution ledgers exit zero. Every required case has exactly ordered setup/call/teardown, all passed, from one worker.
- Both JUnit reports contain zero failures, errors and skips.
- Collection/native/POSIX raw hash agrees: `a1a42eb6d26243924197f9649ae0353c7f28e8dbbfdbb371a1a098bd1e9d455c`.
- Independently read and SHA-256 compared **all 984 committed release blobs** against the qualified candidate inventory: **zero mismatches**.
- Sixteen parity variants each account for 88 rows with zero failures.
- Package checks and strict **132-file** wheel/source byte comparison pass.
- Post-version exact canonical-inventory, Cargo-package and metadata checks pass.

The first R2 attempt passed checks but failed commit creation for missing isolated author identity. Its receipts remain distinct. The subsequent supported retry completed Gearu preparation and created the local commit/tag.

No tests, builds, mutations or publication actions were performed by this reviewer.

## Problem, requirement provenance, and scope

The original verified human authorization remains the coordinated minor release through Gearu, GitHub Releases and registries. Repository rules require immutable tags and workflow-owned publication. The qualified platform split requires complete exact-ID/raw-source evidence without skips or omissions.

This correction addresses the demonstrated capture failure locally. It preserves the authorized foundation prerequisite, package ownership and coverage boundaries. Protected authoring files, exact35 preservation artifacts, reference contract, unfinished libraries and unrelated members are unchanged by the correction.

Pending bootstrap, registry locks and consumers are execution gates, not concealed completed outcomes.

## 2. Invariant analysis

The original POSIX failure is refuted by actual candidate execution, not substituted source-only probes. Lossless event accounting establishes complete execution cardinality. Independent POSIX hashing and the 984-blob comparison associate tested bytes with the final version commit despite the ledger’s pre-version HEAD label.

Publication reconciliation remains fail-closed on identity mismatch or registry errors. Canonical ownership, credential locality, confined cleanup and strict ownership-receipt comparison retain their reviewed behavior.

Historical R0/R1 results were not used as final-source qualification. Local preparation is not represented as publication.

## 3. Risks and next action

Proceed through the accepted bootstrap/publication boundary after the other axis accepts the same tuple. Foundation credential scope/preflight, actual publication, completed Rust registry locks, supported-Python workflows, clean public consumers, exact35 restoration and final GWZ/remote receipts remain required. Their final immutable tuples and evidence require the promised same-originator checks.
