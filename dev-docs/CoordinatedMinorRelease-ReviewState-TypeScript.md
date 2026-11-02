# TypeScript 0.11 Independent Publication — STATE-AXIS REVIEW

**Review object:** `@owebeeone/taut-shape` at `79d3899b91af843b2295d089c82f6547ef97fde8`, local tag `v0.11.0`; independent publication boundary only.

**Baseline:** Previously reviewed TypeScript `1aaeab65e4564a462044d2f5d824cd2f375aae97`. Sources read through immutable Git objects and their exact diff.

**Date:** 2026-11-03

**Axis:** State — dependency coherence, immutable release identity, publication sequencing and recovery. Independent, adversarial, read-only, by the original State reviewer. No current peer report was accessed. Filed verbatim by the lane owner.

**Verdict: GO** — no blocking finding for independent TypeScript publication. This does not declare publication successful or the coordinated train complete.

---

## 0. Evidence base

Verified these immutable objects at start and end:

| Component | Commit |
|---|---|
| Root | `06e8a10b53630e9c90c8038be0b7a23429168980` |
| TypeScript | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Taut | `9260da45f486ed5a57aa399788c2936f2c044619` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| Rust shape | `506b60ef059208c9dd7a1d85fa6df4deb8824577` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

The TypeScript tag resolves to the stated release commit.

Inspected the complete version diff; package metadata, exports, Gearu configuration, publication workflow, foundation build/provenance, generated foundation imports, README ownership instructions and repository release rules.

`shape-ts-candidate.log` records **315 passed, zero failed/cancelled/skipped**, frozen installation, typecheck, package creation, post-version exact checks, fast-forward application and local tag creation.

The foundation publication failure log records **403 Forbidden: authentication failed**. Registry absence and successful preflight were supplied as owner-verified execution evidence; this reviewer did not query remote services.

No tests, builds, source writes, Git mutations or publication actions were performed.

## Problem, requirement provenance, and scope

The original human authorization covers all four releases. The supplied task steering explicitly permits independently releasable reviewed packages while holding foundation-dependent publication.

Foundation authentication is a demonstrated blocker for its dependent release path. It is not a TypeScript runtime prerequisite: this package has no runtime dependency declaration on PyPI, crates.io or another npm foundation package.

The authorized action remains Gearu-managed publication through the repository workflow. No credential migration, alternate publishing infrastructure or unrelated implementation change is necessary.

## 1. Changed-range and closure analysis

The entire TypeScript delta changes only `package.json` version `0.10.0` to `0.11.0`. Foundation sources, generated APIs, dependency lock and release workflow remain reviewed content.

Prior State findings remain closed within their accepted scope. No new architectural root cause or finding was established.

## 2. Invariant analysis

The npm package includes `dist`, `foundation` and `foundation-src`. Its build verifies recorded canonical-source hashes and constructs the foundation locally, without fetching Taut or the Rust crate. Generated library modules bind to that included foundation.

ESM facades delegate to the actual CJS owner, preserving the reviewed nominal ownership arrangement. Publishing TypeScript therefore introduces no unresolved dependency on the held foundation release.

Gearu’s local version/tag identity agrees with package metadata. Independent publication changes neither the failed foundation result nor the hold on Taut/Python/Rust registry progression.

## 3. Risks and next action

Proceed through the ordinary Gearu push/GitHub Release path for this exact TypeScript commit/tag, then require successful npm workflow completion and a clean public-registry runtime consumer exercising the reviewed ownership behavior.

Retain immutable tags and reconcile any partial publication against the actual registry artifact. Keep foundation-dependent publication held until foundation is verified; record TypeScript’s outcome separately from full-train completion.
