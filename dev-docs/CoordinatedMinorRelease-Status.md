# Coordinated minor release status

Status: **accepted at Taut9260da45f486ed5a57aa399788c2936f2c044619 after
CoordinatedMinorRelease-ReviewCode-2.md and ReviewState-2.md reported GO; this
accepts readiness and local Taut0.11.0 preparation only**.

Qualified sourcec426a9acc40406e41d82649e84960472510445a9; final release commit
differs only by Gearu's foundation version change0.10.0->0.11.0. All984 raw Git
blobs match the qualified raw tree. Required2564 cases passed (2560native,
4POSIX), zero skips/failures/omissions, eight accounted parity wrappers; actual
all16 variants each88rows GREEN; package and132-file smoke checks passed.

Publication order is reviewed Rust-shape workflow506b60e reachable on main,
Gearu push of Taut9260da4/v0.11.0 without GitHub Release, foundation preflight
and initial0.11.0 workflow publication with exact same SHA/tag, verified public
crate, then Taut GitHub Release/PyPI and dependent shape releases0.11.0.

Foundation credential presence is known; new-crate scope remains unproven until
actual upload. Public registry publication, Rust checksum/lock completion,
supported-Python workflows, clean index consumers, exact35 artifact restoration
and final GWZ/remote receipts remain outstanding. No full-train completion is claimed.

## Current publication boundary

Taut9260da4/v0.11.0 was atomically pushed through Gearu without a GitHub Release.
The reviewed Rust506b60e and Python d33a069 preparation commits are public main.
Foundation preflight41536648490 succeeded. Upload41536859807 failed with
crates.io403 authentication failed; all five0.11.0 registry versions remain
absent at that check. Native and WSL standard Cargo credentials/config/env
contain no alternate credential. Taut/Python/Rust registry publication is held.

The 403 proves failure of that credential route only; its cause and the secret's
scope/expiry are unknown. No token replacement or retry has been performed.
The existing `taut-shape` publisher is verified by crates.io's 0.10.0
`trustpub_data` and successful run36682081483. It uses `release.yml`, OIDC,
and environment `crates-io`. That crate-specific trust cannot create the absent
`taut-foundation` crate. Current official documentation and server source still
require an API token for an initial publication; see the immutable references in
CoordinatedMinorRelease-PublicationBoundary.md. Changing foundation.yml to OIDC
alone cannot supply this missing crate-side eligibility.

The coordinating task explicitly permits independent coherent releases. The
same Code+Surface and State originators both GO independent TypeScript79d3899
localv0.11.0 (only package-version delta;315pass/zero fail/skip, typecheck and
pack passed). It has no runtime dependency on held PyPI/crates artifacts.
Gearu pushed79d3899/v0.11.0 and created its GitHub Release. Run41537841200
terminated SUCCESS and npm accepted the upload. The public npm0.11.0 package
installed in a fresh consumer with validation OFF/ON, codecs, immutable
descriptors, and shared ownership passing. The successful install used npm's
supported `--full-metadata` option while abbreviated registry metadata lagged.
A second fresh ordinary npm install and both consumer modes subsequently passed.
Generation used the
qualified public Taut tag's development source because its PyPI release is held.
This proves the public npm runtime, not a public PyPI compiler release.

All35 preserved untracked artifacts have now been restored and matched to
their before hashes; all five protected files match, enum.case remains an
ancestor, and the reversible stash is retained. Taut has zero tracked changes
and exactly those35 untracked files. Other members are clean. GWZ capture
records the actual release commits and preserves its dirty-state warning for
those user artifacts. Final workspace publication is a partial-release receipt,
not acceptance of the remaining unpublished packages.
