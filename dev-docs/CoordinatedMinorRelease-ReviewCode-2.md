# Coordinated 0.11 Minor Release — CODE+SURFACE-AXIS REVIEW R2

**Review object:** Final bounded correction at root `6cb4ad603f4a0b0a96066a3f9a9490e15006f385`, Taut source `c426a9acc40406e41d82649e84960472510445a9`, and Gearu’s resulting local release commit `9260da45f486ed5a57aa399788c2936f2c044619`, resolved by local tag `v0.11.0`.

**Baseline:** R1 root `4c8bcdca1cfb49d0f5d9bc3aaf7fd51db9a76a2f`, Taut `092f0b4871f33a93fe452ca25eab092e544516ea`; other members unchanged.

**Date:** 2026-11-03  
**Axis:** Code + Surface. Same-originator, independent, adversarial, read-only. Both prior R1 reports and the merged plan were legitimate inputs; no current peer R2 report was inspected. Filed verbatim by the lane owner.

**Verdict: GO** — no open Code+Surface P0, P1 or P2 findings. This accepts the qualified readiness source and exact local Taut release commit/tag. Public publication and registry-consumer completion remain separate gates.

---

## Prior-finding closure

| Finding | Disposition and evidence |
|---|---|
| Code P2-1: duplicate xdist registration | **Closed.** Entry-point loading and explicit isolation remain corrected; real autoload-enabled/disabled probes passed. |
| Code P2-2: incomplete/repeated phase evidence | **Closed.** Lossless events and strict phase/worker validation reject the original counterexamples. The complete candidate now passes the exact platform union. |
| Code P2-3: POSIX capture failure | **Closed.** Committed `--capture=sys` executes all four assigned cases successfully inside the actual Gearu candidate, with matching raw-source hashes and complete passing phases. |
| Prior State multiplicity/recovery findings | Corrections inspected in R1 remain unchanged. State closure remains its originator’s responsibility. |

## Changed-range analysis and classification

The complete Taut `092f0b4…` → `c426a9a…` diff adds `--capture=sys` to the POSIX command and two RELEASE.md lines documenting the qualified mode. No case selection, assertion, ledger, hashing, runtime, schema or generated API changes occur.

The independently inspected `c426a9a…` → `9260da4…` diff changes only `rust/taut-foundation/Cargo.toml` from version `0.10.0` to `0.11.0`.

Root changes file the prior reports, merged plan and managed source receipts. **No new architectural root cause was established.** The correction resolves the demonstrated host-capture boundary without weakening coverage.

## 0. Evidence base

Named objects were verified at the start and end; the final local release object and tag target were also inspected.

| Component | Immutable revision |
|---|---|
| Root | `6cb4ad603f4a0b0a96066a3f9a9490e15006f385` |
| Taut readiness source | `c426a9acc40406e41d82649e84960472510445a9` |
| Taut local release/tag target | `9260da45f486ed5a57aa399788c2936f2c044619` |
| Rust shape | `506b60ef059208c9dd7a1d85fa6df4deb8824577` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| TypeScript shape | `1aaeab65e4564a462044d2f5d824cd2f375aae97` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Read the committed RemPlan-2, both verbatim R1 reports, complete correction/version diffs, changed public instructions, `qualified-candidate-proof.json`, successful Gearu log and final receipts under:

`D:/projects/limbo/coordinated-release-2026-11-03/gate-evidence/taut-release-checks-a_hs5j50`

Observed:

- **2,572 collected:** 2,560 native + four POSIX required cases; eight separately accounted parity wrappers.
- **2,564 required cases passed**, with no skips or omissions.
- Exactly 2,560 native and four POSIX setup/call/teardown events per phase; every recorded outcome passed.
- Collection and both execution ledgers identify `c426a9a…`, exit status zero and identical raw tree hash:

  `a1a42eb6d26243924197f9649ae0353c7f28e8dbbfdbb371a1a098bd1e9d455c`

- All **16 mandatory parity variants GREEN**, each accounting for 88 rows.
- Package build/check and **132-file raw-byte smoke comparison passed**.
- Gearu’s post-version canonical inventory, Cargo package and metadata checks passed.
- The owner’s raw-source proof records all **984 committed release files** matching the qualified candidate and protected five unchanged.

The successful log ends with local `v0.11.0` targeting `9260da4…`. Earlier failed candidates and the author-identity interruption remain separately attributed; they are not substituted for this successful run.

This reviewer performed inspection only, with no writes, tests, builds or publication actions.

## Problem, requirement provenance, and scope

The original human authority remains the explicitly verified instruction to perform the coordinated minor release across Taut and the three implemented shape libraries, through Gearu and their registries.

The foundation remains a necessary registry prerequisite: the former supported development route supplied an unpublished owner through a sibling patch. The release correction publishes that existing canonical owner rather than creating another implementation.

The qualified split preserves the required Windows/POSIX union, exact source association and all-sixteen parity requirement. The observed successful candidate now supplies that evidence.

Protected authoring files, exact35 preserved artifacts, unfinished libraries, unrelated members and the reference contract remain outside implementation scope. No unauthorized expansion appears in this correction.

## 2. Invariant analysis

The original capture counterexample no longer occurs in the actual candidate. All four POSIX cases execute with complete evidence, followed by the native partition and accepted exact union.

Registration, execution-cardinality, canonical runtime ownership, immutable sibling inputs and publication-reconciliation corrections remain intact. The final release’s sole metadata change matches Gearu’s authorized version operation and the qualified raw-source proof.

## Surface

RELEASE.md now explicitly describes the qualified POSIX capture mode. Existing migration notes retain regeneration and nominal-owner requirements, explicit runtime selection, deferred virtual selection and honest pre-1.0 compatibility limits. Installation/removal remains the ordinary package-manager lifecycle.

## 3. Risks and next action

Proceed through the documented bootstrap preflight and workflow-owned publication sequence. Credential scope, actual registry publication, Rust registry-lock completion, supported-Python workflows, clean public consumers, preservation restoration and final GWZ/remote receipts still require execution and the promised same-originator final checks. No public publication completion is claimed here.
