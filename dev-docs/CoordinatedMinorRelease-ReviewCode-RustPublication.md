# Rust 0.11 Publication Closure — CODE+SURFACE-AXIS REVIEW

**Review object:** Rust shape `7f2a60747901fcf15362ab3c9a8af65c20faad68`, local lightweight tag `v0.11.0`, with completion receipts at root `f2d2586af2cdd346e4933a0deb71a0460975e52f`.

**Baseline:** Accepted Rust shape `506b60ef059208c9dd7a1d85fa6df4deb8824577`. Sources were inspected through immutable `git show` and exact-range diffs.

**Date:** 2026-11-03  
**Axis:** Same-originator Code + Surface. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — no blocking findings. The exact Rust candidate may proceed through existing Gearu/OIDC publication. Full-train completion remains unclaimed.

---

## 0. Evidence base

The exact tuple matched at the beginning and end:

| Component | Commit |
|---|---|
| Root | `f2d2586af2cdd346e4933a0deb71a0460975e52f` |
| Rust shape | `7f2a60747901fcf15362ab3c9a8af65c20faad68` |
| Taut | `9260da45f486ed5a57aa399788c2936f2c044619` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| TypeScript shape | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Read the complete canonical prompt, Cargo manifests and RELEASE.md cold, controlling DRAFT/Completion, complete Rust delta, foundation workflow/independent receipts, verification helper, Gearu configuration, unchanged publication workflow and owner-reexport boundaries.

Inspected `shape-rs-candidate.log`: **108 tests passed**, zero failed/ignored; clippy denied warnings; no-default-features build passed; isolated packaging and post-commit exact packaging passed. The log records downloading and compiling registry `taut-foundation 0.11.0`, followed by Gearu’s release commit/tag.

No builds, tests, writes, publication or credential access were performed by this reviewer.

## Problem, requirement provenance, and scope

The original human minor-release authority covers these packages, necessary foundation publication, Gearu/workflow releases and consumers. Subsequent bootstrap authorization and credential removal/revocation are recorded; no credential was retrieved.

The previously deferred registry-lock step is now necessary and feasible: the canonical foundation is public and verified. Retaining its former local-path identity would not represent the requested registry dependency.

The correction is localized to that lock transition and Gearu versioning. No broader implementation or workflow remedy is introduced. Protected files, preserved artifacts, unrelated members and the reference contract remain outside this delta.

## 2. Invariant analysis

**Delta is mechanical.** Only four files differ from accepted `506b60e…`: three manifest versions and Cargo.lock. Workspace/library/tool versions become `0.11.0`; foundation becomes registry `0.11.0` with checksum:

`63ac99ac22bb0e5e9d645bf1f49cc4ff974d82c05219f72b83c9f03cb93375ef`

The unrelated `futures-core` version/checksum is unchanged.

**Registry identity closes correctly.** The lock checksum agrees with both filed foundation receipts. Workflow archive checksum matches the public registry archive. Independent verification establishes all **12 payload entries**, sizes and bytes plus clean Taut VCS identity. Its differently compressed local archive is explicitly recorded as unequal; the earlier compressed-byte assertion is not relabelled as success.

**One runtime owner remains.** There is no local foundation patch. Codec, descriptor and optional validation exports continue to re-export the registry foundation owner. No runtime source was copied or changed.

**Publication route remains appropriate.** Existing `taut-shape` OIDC configuration/workflow is unchanged. The release-event route checks tag/version agreement and publishes only `taut-shape`; the tool remains `publish=false`. The local tag resolves exactly to the reviewed candidate.

## Surface

Public dependency/features remain clear: registry foundation `0.11.0`, validation through `taut-foundation/validation`, and retained `no_std + alloc` support. Existing nominal-owner migration instructions remain applicable. This delta adds no API or lifecycle behavior.

## 3. Risks and next action

Push and publish this exact Rust commit/tag through existing Gearu/OIDC, then require terminal workflow success and clean public Rust consumers with validation OFF/ON and shared nominal identity.

Other PyPI workflows, public consumers, final artifact restoration and GWZ receipts remain completion gates. Completion.md correctly records the current reversible restash and pending restoration rather than claiming it finished.
