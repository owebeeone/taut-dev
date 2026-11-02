# CoordinatedMinorRelease — STATE-AXIS REVIEW — REMEDIATION 1

**Review object:** Coordinated 0.11 release readiness, merged remediation 1, controlled by `dev-docs/CoordinatedMinorRelease-DRAFT.md` and `dev-docs/CoordinatedMinorRelease-RemPlan-1.md` at root `4c8bcdca1cfb49d0f5d9bc3aaf7fd51db9a76a2f`. Publication remains pending.

**Baseline:** Prior reviewed root `5f9c4953781282a3578aa7a132e3968fbcd4ac63`, Taut `17d3820f6d2375664623e9020dbb40f86beaa49d`, Rust shape `e63ec55123977f6174211cdc7dfc80ad9fac513d`; other members unchanged. The original published baselines remain those recorded in the prior reports. Sources were inspected through immutable `git show <SHA>:<path>` and named-range diffs.

**Date:** 2026-11-03

**Axis:** State — release transitions, interruption/recovery, filesystem isolation, source association and fail-closed execution evidence. Independent, adversarial, read-only. The prior reports are legitimate merged-round input; no current-round peer report was inspected. Filed verbatim by the lane owner.

**Verdict: NO-GO** — the two original State defects are corrected and their focused regressions pass, but one newly demonstrated P2 execution blocker remains. I pre-commit to GO on a revision resolving P2-3 as specified, subject to the required final-source execution evidence. No new architectural root cause was established.

---

## Prior-finding closure

| Prior finding | Disposition | Original counterexample verification |
|---|---|---|
| State P2-1: execution multiplicity and incomplete phases erased | **Corrected; focused closure verified.** Full platform-union qualification remains blocked by P2-3. | The collector now appends phase events and worker identity. The validator requires exactly three events, ordered setup/call/teardown, all passed, from one worker. Duplicate complete executions, repeated calls, omitted setup/teardown and failed-then-passed sequences are rejected. The real two-worker `--dist=each` probe serializes its ledger and demonstrates rejection. |
| State P2-2: successful foundation upload cannot be reconciled after interruption | **Closed at readiness-source level.** Actual registry execution remains pending. | The new publisher first queries the exact version. Only HTTP 404 permits upload. An existing version must match registry checksum, complete package payload and the clean reviewed VCS SHA. The controlled lost-response test records one accepted upload, then reconciles the rerun without uploading again. Mismatches and lookup/network failures reject. |
| Merged Code P2-1: xdist duplicate plugin registration | **Changed range verified; no State objection.** | Explicit loading uses the entry-point name `xdist`. The gate establishes plugin isolation, removes inherited pytest options/plugins and selects `loadfile`. Real autoload-enabled and autoload-disabled probes both execute successfully. Closure of the Code finding remains its originator’s responsibility. |
| Merged Code P2-2 | Same implementation root as State P2-1. | Covered by the event-cardinality checks above; no reliance on the current Code reviewer’s verdict. |

The focused Taut log reports **29 passed**. The publication-recovery log reports **six tests passed**. I inspected the corresponding committed test implementations; these are owner-run results, not tests executed by this reviewer.

## Changed-range analysis

The complete Taut range from `17d3820` to `092f0b4` changes six files: publication-test dependencies, Gearu migration notes, the Rust sibling pin, release checks, the execution ledger and its regressions. Canonical runtime and generated API implementations are unchanged.

The complete Rust shape range from `e63ec55` to `506b60e` changes the foundation workflow and recovery documentation, and adds the publisher plus controlled tests. Root changes file both original reports and the merged plan, and update managed member-lock/integrity records. Python shape, TypeScript shape and the reference contract retain their prior immutable commits.

The additional corrections are bounded and connected to observed readiness failures:

- Same-location smoke generation preserves and compares every output byte, including ownership receipts. No manifest exclusion or semantic normalization was introduced.
- WSL invocation now uses `--exec` and forward-slash paths. Its source inventory comes from native Git, while POSIX independently reads and hashes each named candidate file. This avoids asking Linux Git to interpret a Windows worktree gitdir.
- Cleanup resolves and confines the target to the created release temporary directory, then uses Windows extended-path spelling for the namespace-adversity fixtures.
- Foundation reconciliation preserves immutable source/tag guards, pins Cargo’s toolchain and checks payload identity before recording success.
- Publication CI declares xdist for the new real subprocess probes. Minor release notes identify runtime ownership, regeneration and compatibility consequences.

The revised full candidate actually reached the new WSL command, but that command failed before executing its POSIX partition. This is the new bounded blocker P2-3. It is a host-execution compatibility defect, **not a new architectural root cause**: the inventory, ledger, publication ownership and release mutation boundaries need no redesign on the evidence inspected.

## 0. Evidence base

These immutable objects resolved to their stated commits at both the beginning and end:

| Repository | Reviewed commit |
|---|---|
| `taut-dev` | `4c8bcdca1cfb49d0f5d9bc3aaf7fd51db9a76a2f` |
| `taut` | `092f0b4871f33a93fe452ca25eab092e544516ea` |
| `taut-shape-rs` | `506b60ef059208c9dd7a1d85fa6df4deb8824577` |
| `taut-shape-py` | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| `taut-shape-ts` | `1aaeab65e4564a462044d2f5d824cd2f375aae97` |
| Reference-only `taut-shape` | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Read in this round:

- Committed merged remediation plan, both verbatim prior reports, and controlling DRAFT.
- Complete immutable Taut and Rust shape correction diffs, including all new publisher and regression-test code.
- Numbered revised release launcher around lines 186–233; revised foundation workflow in full; numbered publisher in full.
- Root lock/integrity changes and foundation-related ignore rules.
- `D:/projects/limbo/coordinated-release-2026-11-03/remediation-focused-final.log`: **29 passed**.
- `D:/projects/limbo/coordinated-release-2026-11-03/publication-recovery-tests.log`: **six passed**.
- Original failure receipts under `failed-source-17d3820`, including tests log, aggregate Gearu log, smoke log, parity coverage, inventory and collection source/hash identifiers.
- Revised candidate log and retained receipts under `gate-evidence/taut-release-checks-80cvnou2`: collection/source inventory identifiers, POSIX ledger, POSIX JUnit, tests log, parity log, build log and smoke log.

Original source `17d3820` produced **2,552 native passes**, sixteen complete parity variants and a successful package build, but its aggregate failed at WSL path conversion before POSIX execution; its cleanup also failed. Those results are explicitly historical and do not qualify `092f0b4`.

For source `092f0b4`, the retained collection and POSIX ledgers both identify:

- HEAD: `092f0b4871f33a93fe452ca25eab092e544516ea`
- Raw tracked-file tree hash: `a852a963e6d9c6e2d5aad2aac8220d75a33ab6678a63e808f3304500ac0a9304`

The revised collection reports **2,572 tests**. Its POSIX record has exit status **3**, empty selected/executed sets, and JUnit **zero tests**. The revised parity log records sixteen GREEN variants and clean mandatory governance. Build distributions passed checks. Smoke reports exact generation equality across **132 files**. The revised aggregate nevertheless failed.

No builds, tests, installs, workflow actions, publication actions, Git mutations or file writes were performed by this reviewer.

## Problem, requirement provenance, and scope

The authority and requested outcome remain unchanged: the human authorized a coordinated minor release of Taut and the three implemented shape libraries through Gearu, GitHub Releases and their registries. The original canonical prompt records the lane owner’s direct verification of that instruction and its preceding explanation.

Repository rules require immutable tags and workflow-owned registry publication. The authorized Windows/WSL qualification requires every required case to run without skips, failures or omissions, with exact-ID/raw-source evidence and actual sixteen-variant parity.

The foundation dependency remains necessary for registry publication: the supported development route relied on a sibling patch to an unpublished crate. The correction does not create another runtime implementation.

The merged changes address observed failures and reported findings within the authorized release infrastructure. No changes to protected authoring files, canonical runtime implementations, unfinished language libraries or unrelated members appear in the correction range. The prior exact35 stash and protected-file preservation requirements remain in force.

Preflight, token scope, initial foundation publication, Rust registry-lock completion and public consumers remain separate execution gates. Their pending status alone does not defeat readiness-source review. P2-3 is different: the inspected required command has now actually failed in the selected qualification environment and cannot yet produce the required union.

## 1. Findings

### [P2-3] The mandatory POSIX invocation fails before collecting or executing its assigned cases

**Location:** Taut `scripts/release_checks.py:213–221`, particularly line 216 assigning the mounted Windows work directory as `TMPDIR`, together with default pytest capture at line 217.

**Violated invariant:** The qualified POSIX complement must execute every assigned case and produce successful exact-source execution evidence. The documented gate must provide a working invocation for the selected Windows/WSL environment.

**Observed reproduction:**

1. Gearu prepares candidate source `092f0b4`.
2. Native collection succeeds with 2,572 IDs.
3. The release script invokes WSL Python with `TMPDIR=/mnt/d/.../taut-release-checks-80cvnou2`, default pytest capture, and the four-case POSIX selection.
4. Pytest reports “no tests ran” and exits through an internal capture failure.
5. `_pytest/capture.py`, in `snap()`, calls `self.tmpfile.truncate()` and raises `FileNotFoundError`.
6. The retained POSIX ledger records exit status 3, no selected cases and no phase events. JUnit records zero tests. The aggregate correctly rejects the subprocess failure.

This is preserved in `gate-evidence/taut-release-checks-80cvnou2/tests.log`, `posix-tests.json`, `pytest-posix.xml` and the aggregate candidate log. Unlike the earlier source’s path-conversion failure, the revised command reached pytest.

The failure occurs in temporary capture-file handling on the shared mounted path. An isolated probe is still needed to distinguish the exact filesystem/Python mechanism; that uncertainty does not change the demonstrated failure of the required invocation.

**Impact:** The final-source platform union is unqualified. The revised native partition is scheduled after POSIX and therefore was not reached by this candidate. Neither historical native passes nor current parity/build/smoke success supplies the missing execution evidence.

**Required correction:** Qualify temporary-file/capture behavior for the actual WSL Python and mount, then use a working invocation. A localized choice such as Linux-native temporary capture storage or a compatible pytest capture mode is sufficient if demonstrated; preserve all case selection, source hashing, ledgers and no-skip requirements.

**Closure/regression test:** Run the same WSL/Python invocation against a fresh candidate on the selected mount and demonstrate collection plus all four assigned POSIX cases with exactly one passed setup/call/teardown each. Confirm the independent raw-file hash matches native collection. Then complete the full corrected Gearu gate, including the native partition and exact union, without skips, failures or missing tools. Retain the failure receipt separately from the successful revision’s evidence.

## 2. Invariant analysis

**Execution cardinality now holds under the original attacks.** An event list preserves duplicate attempts rather than overwriting them. Exact length, phase ordering, outcome and worker checks reject the original duplicate and incomplete sequences. Clearing inherited options and selecting `loadfile` also prevents the originally identified environmental route to duplicate execution.

**Source association remains explicit.** The POSIX inventory fallback reuses the native file-name inventory and commit label, then independently computes the actual file hashes. It does not simply copy the native hash. The observed failed POSIX run and native collection have matching hashes; that proves byte association for those snapshots, not successful test execution.

**Failure remains fail-closed.** POSIX exit status 3 stops the train. The new subprocess exception handling records failure, and the retained receipts survived cleanup. No zero-test or partial run was promoted to success.

**Publication recovery now has a legal rerun path.** Only an exact metadata-endpoint 404 permits upload. Registry/network errors propagate. Existing versions require the public archive’s checksum to match registry metadata and every payload entry to equal the locally packaged reviewed payload. The local VCS record must name the exact clean source SHA. Non-files, duplicate entries and unexpected payload entries reject. Archives are read, not extracted into the filesystem.

**Interrupted receipt creation does not invent publication completion.** Reconciliation returns verified identity before writing its receipt; successful workflow artifact upload follows the publisher step. An interrupted publisher or artifact upload can rerun the same identity verification. It need not republish or move a tag.

**Secret and immutable-source boundaries remain intact.** Foundation defaults to preflight. Actual publication still requires the exact checked-out SHA, matching manifest identity/version and matching immutable tag. The registry secret remains scoped to its presence check or publisher step and is not included in receipts.

**Smoke equality is now measured at the same logical output location.** Renaming the wheel output to a sibling snapshot preserves its original path-bound receipt bytes. Source regeneration uses the original output location, and all files are compared. The inspected revised receipt reports 132 equal files.

**Preservation and scope remain unchanged by remediation.** Protected authoring files, exact35 artifacts and canonical runtime sources are outside the correction range. Root managed receipts now name the reviewed Taut and Rust shape commits. Restoration and final rehash remain required after release.

## 3. Risks and next action

No P0, P1 or new architectural root cause was established. Original State P2-1 and P2-2 are corrected; P2-3 is a bounded host-execution blocker discovered by the actual revised gate.

The next action is to correct and qualify the POSIX invocation, then provide the complete final-source Windows/WSL union for focused State re-verdict. Do not advance publication from the current failed aggregate.

The eventual Gearu version/tag tuple, actual bootstrap result, completed registry locks, supported-Python publication workflows, clean public registry consumers, exact35 restoration and final GWZ/remote receipts still require the promised same-originator checks.
