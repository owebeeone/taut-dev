# Independent TypeScript 0.11 Publication — CODE+SURFACE REVIEW

**Review object:** `taut-shape-ts` release commit `79d3899b91af843b2295d089c82f6547ef97fde8`, local lightweight tag `v0.11.0`.

**Baseline:** Previously reviewed `1aaeab65e4564a462044d2f5d824cd2f375aae97`.

**Date:** 2026-11-03  
**Axis:** Same-originator Code + Surface; independent, adversarial, read-only. No current peer report was inspected.

**Verdict: GO** — independent TypeScript publication is coherent. No blocking finding was established. This does not certify publication success or full-train completion.

## 0. Evidence base

The named tuple resolved correctly at the beginning and end:

| Component | Immutable commit |
|---|---|
| Root | `06e8a10b53630e9c90c8038be0b7a23429168980` |
| TypeScript | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Taut | `9260da45f486ed5a57aa399788c2936f2c044619` |
| Rust shape | `506b60ef059208c9dd7a1d85fa6df4deb8824577` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Inspected immutable diff, package metadata, README, RELEASE.md, Gearu configuration, publication workflow, foundation builder/provenance, foundation import closure and codec facades.

`shape-ts-candidate.log` records frozen installation, typecheck, **315 passed, zero failed/skipped**, packaging and post-commit exact checks. Its package inventory includes compiled foundation owners, ESM facades and declarations. The tag directly resolves to the release commit; it is lightweight.

The complete release diff changes only `package.json` version `0.10.0` → `0.11.0`. No runtime or ownership implementation changed. No new architectural root cause was established.

No tests, builds, writes or mutations were performed by this reviewer.

## Problem, requirement provenance, and scope

The original authority covers the four-package minor release. Subsequent explicit steering authorizes independently releasable reviewed packages to proceed while foundation-dependent publication remains held.

The foundation upload log confirms HTTP 403 authentication failure. That blocks the dependent route, but does not establish a TypeScript dependency.

Requiring successful crates.io publication before this npm package would impose an unsupported prerequisite: TypeScript embeds its canonical foundation and declares no runtime, peer or optional package dependencies on PyPI, crates.io or another npm owner.

## 2. Invariant analysis

The packaged foundation is self-contained. Its inspected imports remain within the included foundation closure; provenance hashes are checked during building. Default packaging compiles one CJS owner, with ESM facades referencing that owner. Shape codec facades reference the same packaged implementation.

Canonical vendoring is development tooling. Installing or running the built npm package does not require a sibling Taut checkout, Python compiler or Rust registry artifact.

The existing workflow tests and packs before npm publication and checks tag/package version agreement. No dependency incoherence follows from publishing TypeScript first.

## Surface

README entry points identify the lightweight foundation and optional validation engine, shared owner identity and explicit source-owner composition. Node requirements and normal package-manager installation/removal remain applicable. The version-only change introduces no new lifecycle or configuration surface.

## 3. Risks and next action

Proceed through Gearu’s existing release/push route and repository publication workflow for this exact TypeScript commit/tag. Require successful workflow completion and a clean public-registry consumer exercising codecs, descriptors, validation and shared owner identity.

Keep Taut/Python/Rust registry publication held until foundation verification succeeds. Preserve immutable tags and report independent TypeScript completion separately from the remaining train.
