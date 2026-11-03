# Coordinated 0.11.0 release completion

Status: **publication in progress**. This continues the accepted DRAFT and
partial boundary at root feafa8168aa31407f019bf0c05fd8784f23aa31a. Historical
partial-boundary receipts remain historical evidence, not current absence claims.

## Bootstrap completed

The human supplied a temporary foundation bootstrap credential and expressly
authorized the authenticated local route and non-echoing stdin. No credential
literal was put in code, shell arguments, files, stdout or this receipt. The
temporary GitHub environment secret was removed after success. The human has
confirmed revocation of the temporary crates.io token. Do not retrieve/reuse it.
Rust shape's release.yml trusted-publisher-only/OIDC route remains unchanged.

Foundation workflow41536859807 attempt2 terminated SUCCESS at reviewed publisher
506b60ef059208c9dd7a1d85fa6df4deb8824577, immutable Taut source/tag
9260da45f486ed5a57aa399788c2936f2c044619/v0.11.0. Public registry checksum:
63ac99ac22bb0e5e9d645bf1f49cc4ff974d82c05219f72b83c9f03cb93375ef.
The workflow's uploaded archive exactly equals that registry checksum. Independent
local repack comparison verifies all12 entry names, sizes and payload bytes plus
clean VCS SHA. Local compressed archive bytes differ; their checksum is recorded
separately, not equated to the registry archive. See FoundationWorkflow.json and
FoundationIndependent.json. No duplicate upload or tag replacement occurred.

## Remaining release candidate

Taut's existing reviewed v0.11.0 tag now has a Gearu-created GitHub Release;
publication workflow41557714352 is running its Python3.10–3.13 matrix. Its source
has not changed and the earlier complete strict source qualification still
applies. No additional full native rebuild is required for unchanged source.

Rust dependency-lock preparation ca84a2238fa85bae7ed457ba788de6c647875aeb adds
only foundation0.11.0's registry source/checksum. Gearu then prepared immutable
local release7f2a60747901fcf15362ab3c9a8af65c20faad68/v0.11.0. From accepted
506b60e, the only changes are that dependency lock and the three package versions
and their own lock entries0.10.0->0.11.0. All108 tests passed, zero failed/ignored;
clippy with warnings denied, no_std build, isolated package verification, and
postcommit exact packaging passed against the actual registry foundation.
No local foundation patch or copied runtime is present.

The original Code+Surface and State reviewers receive focused same-originator
closure for this mechanical Rust lock/version delta before its public push.
No source implementation or workflow redesign is proposed.

Both original reviewers reported GO on the exact root f2d2586/Rust7f2a607
tuple in ReviewCode-RustPublication.md and ReviewState-RustPublication.md.
This accepts publishing this Rust candidate through Gearu/OIDC only; all
terminal workflows and public consumer completion gates remain required.

Python shape source remains accepted d33a069198c5540bfdd5b92b6ff22615d8113fa1.
After Taut is verified on PyPI, its configured Gearu checks must test installed
registry dependencies and build the0.11.0 candidate, then publish its existing
source via immutable tag/GitHub Release. TypeScript79d3899/v0.11.0 remains public;
do not republish it.

## Completion gates and preservation

Remaining gates: Rust focused acceptance and OIDC publication; terminal-success
Taut and Python shape PyPI workflows; actual public registry version checks;
fresh isolated Python/Rust/npm consumers using the public PyPI compiler and
registry runtime owners, validation OFF/ON, codecs, descriptors and shared
nominal identity; exact user/artifact integrity; final GWZ capture/commit/push
with all nine remote dependencies proven. No full-train completion is claimed
until these gates finish.

The same35 artifacts are precisely stashed again for Gearu's clean Taut check,
with unchanged before hashes and retained original stash23d45758f2a73de865dacc2ebc68e6dc9ef22ed6.
Current reversible stash54d964b91a674fd86aeb860cf4b43c53f1dd87d0 must be restored
and all35+five protected-file hashes rechecked at the final boundary. enum.case
and unrelated/contract members remain unchanged.
