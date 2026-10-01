# Generated bounds in glade: all languages or none

Status: deferred (owner, 2026-10-01). A note, not a plan.

## The feature

taut v0.10.0's `max_encoded_len` option (D27; `taut/dev-docs/TautCheckedDecode.md` CD-B4) bounds a
message's encoded length. A schema declares it at file level or on one message; a message's value
overrides the file's; with no declaration there is no bound. Every generated language emits it:

- constants, at file level and per message (Rust: `MAX_ENCODED_LEN: Option<usize>`, beside
  `MAX_DEPTH`);
- a typed decode per message (Rust: `X::decode(bytes)`), which calls the runtime's
  `try_decode_with(bytes, MAX_DEPTH, MAX_ENCODED_LEN)`. That checks `bytes.len()` against the bound
  first and refuses with `TooLarge` before it parses anything.

The plain `try_decode(bytes)` ignores any declared bound.

## What was tried, and what stays

glade's node step (CD-G3 item 3) declared `max_encoded_len = 16 MiB - 1` at file level in glade's
schema, and derived glade-wire's frame limit from it: `MAX_FRAME_BYTES = 1 + MAX_ENCODED_LEN`, the tag
byte plus the largest message. It was Rust only.

glade no longer uses it. Two reasons:
- **It changes taut.** glade's schema lives in taut (`ir/glade.taut.py`, exported to
  `corpus/glade.ir.json`), so declaring the bound is a taut commit. The owner keeps taut unchanged
  unless a change is critical, and this one is not.
- **It did no work.** glade decodes frames with the plain `try_decode` and `from_cbor`, never the
  typed `decode`. The check that protects glade is each carrier's: `frame_len` against
  `MAX_FRAME_BYTES`, on a frame's claimed length, before it allocates.

glade-wire's `MAX_FRAME_BYTES` is therefore the literal `16 << 20` again, with unchanged behaviour.

glade_build's header, which names the taut tag the generated files came from (CD-G1), went with it in
glade. It is also a taut change: the script is `src/taut/corpus/glade_build.py`.

**Where it stands.** The taut commit, `3c6d07e` (the bound and the header), was published with a
workspace push on 2026-10-01 before it could be dropped. The owner kept it rather than pull back a
public commit ("easier to release a patch than pull it back"). So taut's `main` declares the bound in
glade's schema and writes the header, ahead of the v0.10.0 packages, and a patch release will ship it.
A local tag, `archive/glade-schema-bound`, also marks it. glade's frame limit stays its own constant.

## The rule for doing it later

**If it is done for Rust, it is done for all languages, in one change.** Every glade carrier and
client takes its size limit from the schema's generated bound:
- **Rust:** glade-wire, for the node's websocket and peer stream and for client-rs's websocket.
- **TypeScript:** client-ts. A browser WebSocket hands over whole messages, so there is no claimed
  length to check. The generated typed `decode` and its `TooLarge` refusal would be client-ts's bound.
- **Any later client,** in whatever language.

Each gets a test that its limit is the tag byte plus the generated bound, and all targets are
regenerated from the same schema.

**Preconditions:**
- **client-ts on taut 0.10.** It must first re-vendor taut's TS runtime (CD-G3 item 4), which has the
  typed decode.
- **A taut change, or none.** While glade's schema lives in taut, declaring the bound is a taut
  change. So do it when glade's schema moves out of taut into glade, or in a taut release that has
  other reasons to be cut.
