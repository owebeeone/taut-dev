# CoordinatedMinorRelease — STATE-AXIS REVIEW

**Review object:** Coordinated 0.11 release readiness aggregate; controlling `dev-docs/CoordinatedMinorRelease-DRAFT.md` at root `5f9c4953781282a3578aa7a132e3968fbcd4ac63`. Status: drafted readiness source, publication pending. Reviewed 2026-11-03.

**Baseline:** root `05b921181f73ca1e6a83709b1a237d87308211da`; Taut `bd93122c66c917f9144db57b048e34831e92c244`; Python shape `c08c2a1b5197f761c5b0b835c588da512130ceda`; Rust shape `8e92b89ed3a4f218a5a4e018fbfee6301fcc14b4`; TypeScript unchanged. Source was read with `git show <exact-SHA>:<path>` and immutable baseline-to-source diffs.

**Date:** 2026-11-03

**Axis:** State — durable release transitions, interruption/recovery, filesystem isolation, source association and fail-closed evidence. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — two P2 findings block. I pre-commit to GO on a revision that resolves P2-1 and P2-2 as specified, with the stated regression evidence. That acceptance would cover readiness source only; final version, lockfile, execution and publication gates remain separate requirements.

---

## 0. Evidence base

The following immutable objects resolved to their named commit IDs at both the start and end of review:

| Repository | Reviewed commit |
|---|---|
| `taut-dev` | `5f9c4953781282a3578aa7a132e3968fbcd4ac63` |
| `taut` | `17d3820f6d2375664623e9020dbb40f86beaa49d` |
| `taut-shape-py` | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| `taut-shape-rs` | `e63ec55123977f6174211cdc7dfc80ad9fac513d` |
| `taut-shape-ts` | `1aaeab65e4564a462044d2f5d824cd2f375aae97` |
| Read-only `taut-shape` contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Read:

- The canonical State prompt in `D:/projects/limbo/coordinated-release-2026-11-03/review-state-prompt.txt`, in full.
- Workspace `AGENTS.md`, `AGENTS_GWZ.md`, and the review-loop skill; all four release repositories’ actual `AGENTS.md`, `RELEASE.md`, `gearu.toml` and publication workflows.
- The controlling DRAFT in full and the aggregate diff statistics for all changed repositories.
- Taut’s `scripts/release_checks.py` in full, particularly lines 156–173, 176–226 and 229–241; `scripts/release_test_ledger.py` in full, particularly lines 18–31 and 34–51; `scripts/prepare_release_workspace.py`, `release-inputs.json`, and release-check regression tests.
- All changed Taut test hunks, including POSIX assignments, Go newline fixes, archived-document lookup and the actual Rust shape/foundation composition fixture.
- Foundation manifest, README, provenance inventory, synchronization script and library entry point. Compared all four foundation runtime files with their named canonical Git-object source texts; all four comparisons were equal. Inspected their module/include directives for sibling-file dependencies.
- Rust shape’s workspace and crate manifests, existing lockfile, bootstrap workflow in full, and ordinary release workflow in full. Foundation workflow references below use its exact numbered lines.
- Python shape’s package dependency metadata and publication matrix; TypeScript’s package release checks and workflow.
- Parity governance, reporting and `--require-all` dispatch, together with the wrapper-accounting regression test requiring eight wrappers.
- Root GWZ lock and integrity-marker diffs.
- Supplemental scratch evidence: `preserve.py`, `preserved-before.json`, `preserved-stash.json`, candidate launcher and candidate log. Inspected preservation stash `23d45758f2a73de865dacc2ebc68e6dc9ef22ed6` and its untracked-files parent; that parent contains exactly 35 files, including the wheel.
- Taut history at the reviewed commit, confirming the enum-case change `5b5280e` remains in its ancestry.

No builds, installs, tests, registry actions, workflow actions, source edits or Git mutations were performed. Counterexamples below are source-derived execution sequences, not claims that a release was attempted by this reviewer.

The observed candidate log showed successful sibling materialization, foundation packaging, parity and wheel-build stages, with tests/smoke still pending in the read snapshot. It did not establish a complete strict candidate pass. Raw cross-host execution receipts were not yet available in the inspected evidence directory. This report therefore does not certify their eventual contents.

## Problem, requirement provenance, and scope

The requested outcome is an actual coordinated minor release of Taut and the three completed shape libraries, including their package registries. The canonical prompt records the lane owner’s direct verification of the human instruction, “Okay, then go ahead and do a minor bump on and release these new revisions,” following an explanation naming all four repositories, Gearu releases and PyPI/crates/npm publication. I rely on that supplied authority; I did not independently retrieve the voice message.

Repository rules require Gearu preparation, immutable tags and workflow-owned registry publication. They prohibit direct local registry publishing and tag reuse. The qualified Windows/WSL split is authorized only with complete exact-ID/raw-source accounting, no required-case skip or omission, and actual all-sixteen parity execution.

The observed prerequisites are concrete:

- The existing foundation manifest explicitly had `publish = false`; Rust shape used a local sibling `[patch.crates-io]`. That route supports local composition but cannot supply the requested standalone registry dependency. Publishing the already-existing canonical foundation, then removing the local patch, addresses the registry-consumer requirement without creating a second runtime implementation.
- Gearu’s isolated Taut candidate needs the actual sibling composition inputs. Exact committed clones provide these without relying on mutable sibling working trees.
- The suite contains actual Windows-only namespace/junction cases and POSIX shell/symlink cases. Assigning four POSIX cases to WSL preserves those cases; silently skipping either platform’s cases would not satisfy the authorized gate.
- The document-path and LF-writing changes are localized corrections to observed readiness failures.

The editable components are the four release repositories and their necessary readiness/release infrastructure, plus root release records and GWZ receipts through the managed route. The contract repository is reference-only. Unfinished language libraries, unrelated members, protected authoring files and the excluded artifacts are outside implementation scope.

Foundation token scope, initial preflight, actual publication, Rust registry-lock refresh and clean public consumers are explicitly pending execution gates. Their absence alone is not a defect in a package presented as readiness preparation. The two findings instead concern concrete behavior of the newly introduced strict evidence and bootstrap recovery paths.

The unchanged Rust/TypeScript manual-dispatch workflows also have an optional pre-existing weakness: their `tag` input supplies the version check without explicitly selecting that tag for checkout. Ordinary release events and reruns of the original event do not depend on that optional route. This review does not turn that external shortcoming into additional mandatory release work; a separate follow-up should bind dispatch checkout to its named immutable tag.

## 1. Findings

### [P2-1] The strict test ledger erases execution multiplicity before checking “exactly once”

**Location:** Taut `scripts/release_test_ledger.py:18–31`; `scripts/release_checks.py:156–173`, with native execution at lines 191–195.

**Violated invariant:** Every required case must execute exactly once on its assigned host, and the machine-readable evidence must reject duplicate or incomplete execution rather than reduce it to an apparently valid result.

**Counterexample:** The plugin stores selection by node ID and stores phase outcome by `(nodeid, phase)`:

```python
selected.setdefault(name, {})
phases.setdefault(report.nodeid, {})[report.when] = report.outcome
```

A second complete execution of the same test overwrites the first execution’s setup, call and teardown. The resulting ledger is identical to one execution. `verify_test_coverage()` checks sets of IDs and the remaining values, so it accepts that ledger.

A concrete xdist route is a native run with two or more workers and inherited `PYTEST_ADDOPTS=--dist=each`. `source_env()` preserves this environment variable, and the command specifies the worker count without fixing the distribution mode. Every worker can execute each selected test; all executions can pass; the JSON still records one apparent execution per ID. JUnit is examined for skips, not multiplicity.

The same validator also accepts a phase mapping containing only `{"call": "passed"}` because it does not require the phase-key set to equal `{"setup", "call", "teardown"}`.

**Impact:** The new evidence protocol cannot establish the exact-once/full-phase assertion on which authorization of the platform split depends. Its duplicate rejection currently detects duplication between run records, after within-run duplication has already been discarded.

**Required correction:** Preserve execution events or explicit per-node/per-phase counts, including worker identity where appropriate. Reject repeated execution phases and require exactly one passed setup, call and teardown for every required ID. Pin or sanitize incompatible xdist options as useful defense, while keeping the evidence validator independently strict.

**Closure/regression test:** Feed two complete passed executions of one node ID through the real ledger hooks and verify rejection after serialization and loading. Also reject a call-only record, missing teardown, and repeated setup/call/teardown events. Run a small qualified xdist probe using `--dist=each` with at least two workers and demonstrate that it cannot produce accepted exact-once coverage. Retain the existing missing/extra/skip/failure/wrong-host/wrong-source cases.

### [P2-2] Foundation publication has no recovery transition after an acknowledged-or-unacknowledged successful upload

**Location:** Rust shape `.github/workflows/foundation.yml:57–71`, particularly the unconditional publication command at line 71; release recovery requirements in Taut/Rust shape `RELEASE.md` and the controlling DRAFT.

**Violated invariant:** An interruption after the irreversible registry write must have a legal recovery path that verifies the already-published immutable artifact and reaches completion without republishing or moving its version/tag.

**Counterexample:**

1. The exact source, version and immutable tag pass the workflow guards.
2. `cargo publish` uploads `taut-foundation 0.11.0`, and crates.io accepts it.
3. The runner loses its response, is interrupted, or is cancelled before the workflow records successful completion.
4. Rerun the same reviewed workflow with the same SHA, version and tag.
5. The final step always invokes `cargo publish` again. The immutable version already exists, so that publication fails instead of reconciling the successful registry write.

The concurrency group prevents overlapping runs, but it does not resolve this sequential partial-publication state. The workflow has no “present and matches this reviewed artifact” branch.

**Impact:** The mandatory bootstrap can leave the train with a publicly occupied foundation version and a failed publication workflow that cannot recover through the prescribed same-input rerun. The DRAFT requires successful workflow completion and prohibits version/tag replacement. The safe response must not be to pretend the failed run completed or blindly treat any existing version as the reviewed artifact.

**Required correction:** Add an explicit reconciliation transition. Before uploading, distinguish an absent version from registry/network errors. For an existing version, verify its immutable package identity against the reviewed source/package and record successful reconciliation; reject a mismatch. If an upload exits ambiguously, a subsequent same-input run must perform the same verification. Document that recovery path. Registry existence alone is insufficient evidence of source identity.

**Closure/regression test:** Exercise the workflow’s publication/reconciliation logic against controlled registry responses: absent version uploads once; accepted upload followed by lost response recovers on rerun without another upload; matching existing artifact succeeds; mismatching existing artifact fails; registry lookup/network errors fail without being interpreted as absence. Retain exact SHA, version and tag guards, and keep the credential scoped to the publication operation.

## 2. Invariant analysis

**Canonical foundation ownership and closure held under inspection.** The four derived runtime source texts equal their canonical Git-object sources. The descriptor path is internal to the crate; no sibling checkout include was found. The manifest declares a standalone workspace, no dependencies and an explicit package include closure. README/license/provenance are included. This supports the selected publication route without another runtime implementation.

**Version ownership is explicit.** Foundation remains at its pre-release manifest version in the reviewed source, with Gearu configured to change it. The supplemental candidate log shows Gearu testing/package-verifying `0.11.0`. That does not substitute for checking the eventual exact version commit.

**Dependency sequencing is honest.** Python shape requires `taut-proto>=0.11.0,<0.12`. Rust shape requires foundation `0.11.0` and removes its sibling patch. Its current lockfile still names the old non-registry foundation; the DRAFT explicitly blocks lock completion on first publication and requires a later exact check. The locally patched composition fixture proves source-owner composition, not registry consumption, and the DRAFT says so.

**Candidate inputs are fixed.** Taut’s manifest pins the four exact sibling commits. Preparation creates detached clones, disables CRLF conversion for newly materialized inputs, verifies their HEAD and cleanliness, and installs TypeScript dependencies with the frozen lockfile. The inspected candidate log names those same revisions. No mutable sibling source is intentionally substituted for those pins.

**The platform union is substantially fail-closed, subject to P2-1.** Required IDs come from full collection; platform selection is explicit; nonzero subprocess status fails; native and POSIX skip reports fail; selected and reported ID sets must match their assigned partition; cross-host tracked-file hashes must agree. These checks reject ordinary missing cases, extra cases, wrong-source runs and failures. They do not preserve multiplicity or prove every required phase, which is the bounded defect reported above.

**Parity coverage is not replaced with wrapper success.** The actual command is `tautc parity --require-all`. The release step requires the nine base variants and seven forward-compatibility variants, each with 88 passed/type-satisfied rows and zero failures. The existing regression enumerates exactly eight duplicate wrappers. The observed parity stage passed, but final machine-readable parity evidence remains required.

**Bootstrap guards and credential locality held, subject to P2-2.** The workflow validates a full SHA and numeric version, checks out that SHA, verifies HEAD, canonical sources and manifest identity, and requires the matching tag before actual publication. Publication defaults to false. The secret is not printed or exported to files; it is supplied to the presence check and actual publication step. A missing credential fails. These properties do not prove new-crate token scope, which remains an actual preflight/publication gate.

**Preservation is explicit and recoverable in the recorded objects.** The preservation script checks the five protected hashes and all 35 artifact hashes before stashing, restricts the stash path list to exactly those 35 artifacts, and checks each stashed untracked blob against its expected digest before writing the stash receipt. The inspected stash’s third parent contains exactly 35 files. The readiness diff does not alter the five protected files, and enum-case history remains ancestral. This is evidence of the preservation route, not a claim that restoration and final rehash have already occurred.

**Completion is not invented.** The DRAFT labels readiness, preflight, lock completion, registry publication, clean consumers and final GWZ receipts separately. The root GWZ lock still captures an earlier Taut readiness commit; final managed capture is explicitly outstanding. Neither the current candidate log nor this review establishes publication completion.

## 3. Risks and next action

No P0 or P1 defect was established. The two P2 roots are bounded corrections to newly introduced evidence and recovery behavior.

Remaining execution risks are the bootstrap credential’s actual scope, complete strict test/parity receipts, publication CI across the declared Python matrix, registry-lock resolution, and public consumer behavior outside source checkouts. Shared-target build caches and local source-owner composition must not be substituted for clean registry consumers. Restoration must use the recorded exact artifact paths and verify all before hashes while retaining the stash until integrity is established.

The next action is one bounded remediation patch for P2-1 and P2-2, followed by this State reviewer’s focused verification of the original counterexamples at the revised immutable tuple. Keep public release progression blocked until both axes accept the applicable revision and the separately required execution gates pass.
