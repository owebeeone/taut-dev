> Historical partial boundary: this document records an earlier state.
> All five packages are now public; see CoordinatedMinorRelease-Completion.md.

# Coordinated release publication boundary

The release is partially published. TypeScript0.11.0 is public; Taut's immutable
tag is public but its GitHub Release is held. Python shape and Rust shape remain
prepared, without0.11.0 release tags. Neither their registries nor taut-foundation
contain0.11.0. The full train is not complete.

## Existing trust and first publication

Checked against crates.io upstream mainc2cca915732c4d7abb27a8094c58217d429f6cb7
on2026-11-03 Sydney time, rather than relying on the July2025 announcement:

- [Current official documentation source, prerequisites lines65-68](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/svelte/src/routes/docs/trusted-publishing/%2Bpage.svelte#L65-L68) explicitly requires an already published crate and an API token for the initial publication.
- [Configuration creation, lines48-55](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/src/controllers/trustpub/github_configs/create.rs#L48-L55) loads an existing crate before creating its publisher. There is no pending-new-crate path in this handler.
- [OIDC exchange](https://github.com/rust-lang/crates.io/blob/c2cca915732c4d7abb27a8094c58217d429f6cb7/src/controllers/trustpub/tokens/exchange/mod.rs) filters configured repository, workflow and environment, then scopes its temporary token to those existing crate IDs. Reusing release.yml cannot extend taut-shape's authorization to a new crate name.

The public [taut-shape0.10.0 registry record](https://crates.io/api/v1/crates/taut-shape/0.10.0)
contains GitHub trusted-publishing provenance for repository
owebeeone/taut-shape-rs, source502671593f453f4b2e5915fe90e4c34b863e9b50,
[successful run36682081483](https://github.com/owebeeone/taut-shape-rs/actions/runs/36682081483).
Its existing release.yml uses rust-lang/crates-io-auth-action@v1,
id-token:write and environment crates-io. The user's statement that Rust shape
already uses trusted publishing is confirmed. The new foundation.yml used the
existing environment secret instead; it did not try OIDC. That route failed403
in [run41536859807](https://github.com/owebeeone/taut-shape-rs/actions/runs/41536859807).
The failure does not establish that the secret is expired, missing, or has any
particular scope. No further upload was attempted after the correction.

The smallest available one-time action is to put an API token authorized to
create taut-foundation into CARGO_REGISTRY_TOKEN for repository
owebeeone/taut-shape-rs, environment crates-io. Keep its value out of chat and
receipts. After the user confirms that action, retry the existing failed job
with the same source9260da45f486ed5a57aa399788c2936f2c044619/version0.11.0:
`gh run rerun 41536859807 --repo owebeeone/taut-shape-rs --failed`.
The helper first checks public registry state and verifies an existing exact
package instead of re-uploading. Once the initial crate exists, a separate
crate-side trusted publisher may be configured for future foundation releases;
no such change has been made or claimed here.

## Independent TypeScript publication

Source/release79d3899b91af843b2295d089c82f6547ef97fde8, immutablev0.11.0,
[GitHub Release](https://github.com/owebeeone/taut-shape-ts/releases/tag/v0.11.0),
[successful publication41537841200](https://github.com/owebeeone/taut-shape-ts/actions/runs/41537841200).
The two original reviewers approved this independent release. It has no runtime
dependency on the held PyPI/crates releases. npm accepted235 files, shasum
e0e12d536e4abaa4b91f489d059e1ed92ee30f8b, with signed GitHub provenance.

Public registry consumer evidence is retained under
D:/projects/limbo/coordinated-release-2026-11-03/npm-public-consumer-full-metadata/.
Its fresh official npm install of exactly0.11.0 passed both generated validation
modes, codec execution, immutable descriptors, six shape exports and the shared
foundation owner. Installed integrity equals public registry metadata. It uses
no source runtime or PYTHONPATH/NODE_PATH at execution. The generation-only
compiler input is the qualified public Taut tag9260da4 source; this is disclosed
because its PyPI release is still held. Earlier ordinary-install ETARGET logs
are retained, not overwritten or relabelled as successful.

Abbreviated npm metadata then caught up. A second fresh ordinary npm install
(`--prefer-online`, without `--full-metadata`) and the same OFF/ON consumer
checks passed in npm-public-consumer-standard/. The earlier transient failures
remain in npm-public-consumer/ and npm-public-consumer-verified/. Both successful
consumer RESULTS.json receipts are filed alongside this document. Public npm
runtime0.11.0 availability and behavior are therefore verified through the
ordinary installation path as well.

The exact35 preserved artifacts were restored with stash apply and every hash
matched the before inventory. All five protected authoring files also match;
the enum.case commit remains an ancestor. Stash23d45758f2a73de865dacc2ebc68e6dc9ef22ed6
is retained. Taut's expected35 untracked files remain uncommitted. All tracked
member trees are clean; unrelated member heads remain at the initial checkpoint.
GWZ capture updates only the two released member revisions in its managed lock
and integrity marker. The resulting root receipt is for this partial boundary.

No registry success is inferred solely from a tag, GitHub Release or green
workflow. Python/crates consumers remain pending until their actual packages
are public. User artifacts and final workspace receipts are recorded separately.
