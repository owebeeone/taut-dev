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

Required credential action: replace `CARGO_REGISTRY_TOKEN` in repository
`owebeeone/taut-shape-rs`, environment `crates-io`, with a valid token authorized
for the initial foundation publication. Never put the value in a receipt/chat.
Then safely retry the same immutable inputs with:

`gh run rerun 41536859807 --repo owebeeone/taut-shape-rs --failed`

The coordinating task explicitly permits independent coherent releases. The
same Code+Surface and State originators both GO independent TypeScript79d3899
localv0.11.0 (only package-version delta;315pass/zero fail/skip, typecheck and
pack passed). It has no runtime dependency on held PyPI/crates artifacts.
Proceeding through its Gearu/workflow publication; result still pending.
