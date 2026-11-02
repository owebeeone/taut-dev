# CoordinatedMinorRelease Partial Boundary — STATE-AXIS REVIEW

**Review object:** Partial-publication receipt at root `19deeb49cb5dd84a2079af9a4c19e28723109f92`.

**Baseline:** Accepted release sources and prior independent-TypeScript review; immutable documents read with `git show`, supplemented by retained execution receipts.

**Date:** 2026-11-03

**Axis:** State — durable publication status, recovery legality, preservation and source association. Independent, adversarial, read-only, by the original State reviewer. No current peer report was accessed. Filed verbatim by the lane owner.

**Verdict: GO** — publish the root partial-boundary receipt. No blocking finding was established. This does not accept completion of the remaining release train.

---

## 0. Evidence base

Verified the immutable tuple at start and end:

| Component | Commit |
|---|---|
| Root | `19deeb49cb5dd84a2079af9a4c19e28723109f92` |
| Taut | `9260da45f486ed5a57aa399788c2936f2c044619` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| Rust shape | `506b60ef059208c9dd7a1d85fa6df4deb8824577` |
| TypeScript shape | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Read the committed PublicationBoundary, Status, BoundaryReceipt, both NpmConsumer receipts, Preservation inventory, managed lock and integrity marker. Inspected the ordinary public consumer’s manifest, lock, generator bindings, OFF/ON programs, command log, results and controlling verification script.

Also inspected npm publication output, foundation failure output, workspace snapshot and immutable upstream crates.io documentation/server sources.

Independently rehashed all **35 restored artifacts and five protected files** against both the original before-inventory and committed preservation receipt: **zero differences**. The preservation stash remains readable; enum-case ancestry is retained. Unrelated member heads match their original checkpoint.

No tests, builds, writes, retries, credential changes or publication actions were performed.

## Problem, requirement provenance, and scope

The original authorization covers the coordinated release. Subsequent steering permits coherent independent publication while foundation-dependent releases remain held.

The deliverable here is an accurate durable receipt for that partial state. No runtime, workflow or package changes are introduced. Recording the hold does not authorize replacing credentials or relaxing publication requirements.

## 2. Invariant analysis

**Published and held states are distinguished.** npm publication run `41537841200` completed successfully; its retained output records the 0.11.0 upload and signed provenance. The ordinary registry install subsequently succeeded, followed by OFF/ON compilation and execution covering codecs, immutable descriptors, validation behavior and shared foundation ownership.

The consumer pins npm 0.11.0, records registry integrity, and runs without source-runtime paths, `PYTHONPATH` or `NODE_PATH`. Generation alone uses the disclosed qualified Taut source/tag. The receipt correctly avoids claiming a public PyPI compiler.

**Rust authentication is described accurately.** Existing Rust shape uses OIDC; the new foundation attempt used the environment’s API-token route and failed 403. Neither failure nor secret presence establishes expiry or scope.

At the inspected upstream commit, [official documentation](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/svelte/src/routes/docs/trusted-publishing/%2Bpage.svelte#L65-L68) requires an API token for initial publication. The [configuration handler](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/src/controllers/trustpub/github_configs/create.rs#L48-L55) loads an existing crate, while [token exchange](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/src/controllers/trustpub/tokens/exchange/mod.rs) scopes authorization to configured crate IDs. This supports the recorded distinction between existing `taut-shape` trust and absent foundation eligibility.

**Recovery remains legal.** The receipt preserves the exact failed run, SHA and version; proposes the existing reconciliation-aware rerun after the required credential action; and claims no replacement or retry already occurred. Taut’s public tag is distinguished from its held GitHub Release and registry publication.

**Preservation and workspace state agree.** GWZ records all nine members and retains Taut’s expected dirty warning for the 35 restored untracked artifacts. Tracked cleanliness is not confused with removal of user artifacts. Earlier failed npm attempts remain separately attributed.

## 3. Risks and next action

Publish this receipt as a **partial boundary**. Keep Taut/Python/Rust registry progression held until foundation is verified.

Credential enablement, foundation recovery, remaining registry locks/public consumers and final train completion remain outstanding. Registry absence is timestamped receipt evidence, not a permanent assertion.
