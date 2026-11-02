# Partial Publication Boundary — CODE+SURFACE CLOSURE REVIEW

**Review object:** Root receipt `19deeb49cb5dd84a2079af9a4c19e28723109f92`.

**Date:** 2026-11-03  
**Axis:** Same-originator Code + Surface; independent, adversarial, read-only. No current peer report was inspected.

**Verdict: GO** — the root receipt accurately records partial publication. No blocking finding was established. This verdict does not declare the full release train complete.

## 0. Evidence base

The immutable tuple matched at the beginning and end:

| Component | Commit |
|---|---|
| Root | `19deeb49cb5dd84a2079af9a4c19e28723109f92` |
| Taut | `9260da45f486ed5a57aa399788c2936f2c044619` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| Rust shape | `506b60ef059208c9dd7a1d85fa6df4deb8824577` |
| TypeScript shape | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Inspected the committed PublicationBoundary, Status, BoundaryReceipt, both NpmConsumer receipts and Preservation receipt; managed lock changes; npm publication logs; ordinary consumer source, bindings, lockfile and command results; consumer/restoration verification scripts; and immutable upstream crates.io documentation/server sources.

No source, workflow or runtime changes were introduced or performed during this review.

## Problem, requirement provenance, and scope

The human-authorized release and subsequent independent-publication steering permit recording TypeScript completion while holding foundation-dependent publication.

The receipt distinguishes published npm runtime, public Taut source tag, held PyPI/crates packages and outstanding bootstrap authorization. It does not convert a partial result into full-train acceptance.

## 2. Invariant analysis

**npm publication is supported by multiple evidence types.** Run `41537841200` is recorded as successful; its publication log records 235 files, the stated shasum, signed provenance and accepted `@owebeeone/taut-shape@0.11.0`.

The fresh ordinary consumer uses the public registry without `--full-metadata`. Its exact-version lock integrity agrees with the receipt. Compilation and execution pass validation OFF/ON, codec use, immutable descriptors, six shape exports and shared foundation ownership. Runtime execution clears source-path overrides.

**Compiler provenance is honest.** Generation uses qualified Taut source `9260da4…`; the receipt explicitly states that PyPI publication remains held. This proves the public npm runtime, not a released PyPI compiler.

**First-crate bootstrap is supported by current immutable sources.** The official documentation requires prior publication and an API token for the initial upload. The server configuration handler loads an existing crate, while OIDC exchange issues tokens scoped to configured crate IDs. Existing `taut-shape` trust therefore does not authorize creating `taut-foundation`. [Official prerequisites](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/svelte/src/routes/docs/trusted-publishing/%2Bpage.svelte#L65-L68), [configuration handler](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/src/controllers/trustpub/github_configs/create.rs#L48-L55), [token scoping](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/src/controllers/trustpub/tokens/exchange/mod.rs#L138-L218).

The recorded 403 establishes failure of the attempted credential route; it establishes neither expiry nor particular token scope. The receipt preserves that distinction and claims no replacement or retry.

**Preservation records agree.** All 35 restored-artifact hashes and five protected-file hashes exactly match the before inventory. The inspected restoration script verifies these bytes, exact untracked membership, retained stash and ancestry before issuing PASS. Managed lock changes preserve the expected untracked-artifact warning and update only released member revisions.

## Surface

The documents clearly disclose partial completion, ordinary npm installation success, generation-only source provenance and the remaining bootstrap action. They retain earlier failed consumer attempts without relabelling them as success. No secret value appears in the reviewed receipts.

## 3. Risks and next action

Publish the root partial-boundary receipt. Keep dependent registry publication held pending an authorized successful foundation bootstrap, followed by registry locks, package workflows and clean consumers. Preserve the recorded immutable tags and retained artifact stash.
