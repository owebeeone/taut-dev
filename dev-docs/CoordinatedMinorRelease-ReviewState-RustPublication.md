# Rust 0.11 Publication Closure — STATE-AXIS REVIEW

**Review object:** Rust shape local release `7f2a60747901fcf15362ab3c9a8af65c20faad68`, tag `v0.11.0`, controlled by the DRAFT and Completion document at root `f2d2586af2cdd346e4933a0deb71a0460975e52f`.

**Baseline:** Accepted Rust `506b60ef059208c9dd7a1d85fa6df4deb8824577`. Sources inspected through immutable Git objects and the complete baseline-to-candidate diff.

**Date:** 2026-11-03

**Axis:** State — registry dependency identity, immutable publication, partial-success recovery and preservation boundaries. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — publish this exact Rust candidate through the existing Gearu/OIDC route. No blocking finding or new architectural root cause was established. Full-train completion remains unaccepted.

---

## 0. Evidence base

Verified the exact tuple at start and end:

| Component | Commit |
|---|---|
| Root | `f2d2586af2cdd346e4933a0deb71a0460975e52f` |
| Taut | `9260da45f486ed5a57aa399788c2936f2c044619` |
| Rust shape | `7f2a60747901fcf15362ab3c9a8af65c20faad68` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| TypeScript shape | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Rust tag `v0.11.0` resolves to the candidate commit.

Read the complete canonical prompt, committed Completion document and FoundationWorkflow/Independent receipts; complete Rust diff; manifests, lock, Gearu configuration, release instructions and existing OIDC workflow. Inspected `shape-rs-candidate.log`, the successful foundation receipt, independent verification script and receipt, and the current preservation stash’s 35-file inventory.

The Rust log records foundation 0.11.0 downloaded from the registry; **108 passed, zero failed/ignored**; warnings-denied clippy, no-default-features build, isolated packaging and postcommit exact packaging all successful. Gearu completed local commit/tag preparation.

No builds, tests, writes, registry actions or credential access were performed.

## Problem, requirement provenance, and scope

The original human authorization covers the coordinated minor releases and necessary foundation publication. The supplied subsequent authorization covers the completed temporary bootstrap. Its credential and chat are outside this review.

The remaining Rust blocker was concrete: the old lock represented foundation 0.10.0 without registry identity. Foundation 0.11.0 is now public, so resolving its actual registry checksum is necessary for the authorized registry-only package route.

The remedy is bounded. The complete diff changes only foundation’s lock version/source/checksum, the three configured package versions, and their own lock entries. `futures-core` is unchanged. No runtime, workflow, copied foundation or unrelated dependency change appears.

## 2. Invariant analysis

**Registry identity agrees.** The Rust lock pins foundation 0.11.0 to crates.io with checksum:

`63ac99ac22bb0e5e9d645bf1f49cc4ff974d82c05219f72b83c9f03cb93375ef`

That matches the filed workflow and independent public-foundation receipts. The workspace contains no local foundation patch.

**Payload and compression identities remain distinct.** The workflow archive checksum equals the public checksum. The independent local repack has different compressed bytes, explicitly recorded as unequal, while verification checks all twelve payload entries and the exact clean Taut VCS SHA. The earlier compression-equality assertion is not represented as passing.

**Publication remains workflow-owned.** Existing `release.yml` retains OIDC exchange, `id-token: write`, the `crates-io` environment and tag/version agreement. The removed bootstrap secret is not a prerequisite for this existing crate’s trusted-publisher route.

**Recovery does not require tag replacement.** Gearu supports retrying the same prepared version after push or release-creation interruption. Publication failure must be reconciled against actual registry state; workflow existence checks alone do not establish final artifact identity.

**Preservation status is honest.** Completion records the 35 artifacts as reversibly stashed again, names the retained stashes and requires final restoration/rehashing. It does not reuse the earlier restored-state receipt as current completion evidence.

Prior State closures remain unaffected.

## 3. Risks and next action

Push/publish this exact Rust commit/tag through Gearu and monitor the OIDC workflow.

Require terminal publication success, public registry identity and fresh Rust consumer evidence before declaring Rust delivery complete. Taut/Python workflows, public-compiler consumers, final artifact restoration and GWZ receipts remain separate completion gates.
