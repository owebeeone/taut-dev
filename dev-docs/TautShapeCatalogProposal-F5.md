# Taut Shape Catalogue Proposal — F5

Assigned agent name: `F5` (filesystem-safe as supplied; filename suffix `F5`).
Commission: `TautShapeCatalogProposalPrompt.md`, executing Step 0.1 of
`TautShapeImplementationPlan.md` at proposal depth, independently.

Note on citable IDs: findings in §5 are numbered `F5-F01…` (agent prefix + `F`
+ two digits). These are distinct from the pre-existing review IDs of the form
`F5-02`/`56-F2` quoted inside `taut-shape/dev-docs/AtomSwmrNotes.md` and
`corpus/README.md`, which come from an earlier, unrelated code review
(`TautShapeCode-ReviewF5.md`). Any consolidation tooling should match on the
`F5-Fnn` pattern for this document.

## 1. Analysis snapshot

Observed 2026-08-22, local working trees (no fetch, no mutation performed).
Paths in citations are relative to `/Users/owebeeone/limbo/` unless they start
with a member name used unambiguously in context.

| Checkout | Revision | Dirty state relevant to this analysis |
| --- | --- | --- |
| `taut-dev` (gwz workspace root) | `51bf253` | 1 untracked (this prompt's sibling docs). |
| `taut-dev/taut` | `f008419` | clean |
| `taut-dev/glade` | `61617d5` | clean |
| `taut-dev/taut-shape` | `389c867` | 23 dirty entries: **the entire atom/swmr contract is uncommitted** (`ir/shape_atom.taut.py`, `ir/shape_swmr.taut.py`, generated IR, `corpus/atom.v1.json` 28 vectors, `corpus/swmr.v1.json` 32 vectors, scripts, `dev-docs/AtomSwmrNotes.md`, review docs), plus modified `ir/shape_value.taut.py`, `corpus/value_gen.py`, `corpus/README.md`, `dev-docs/TautShapeOracle.md`, `matrix/driver.py`, READMEs. |
| `taut-dev/taut-shape-rs` | `7e50457` | 6 dirty (log engine/session/window + lib) |
| `taut-dev/taut-shape-ts` | `b115245` | 4 dirty (log engine files) |
| `taut-dev/taut-shape-py` | `7e7d5a7` | 7 dirty (log engine files) |
| `glade-wz` (workspace root) | `82e09c7` | glade-discover docs only; members relevant here clean |
| `glade-wz/glade` | `61617d5` (same as taut-dev's copy) | clean |
| `glade-wz/glial` | `b3ee665` (2026-07-18 — newest Glial anywhere) | clean |
| `glade-wz/glade-decl` | `ccdae14` | clean |
| `datascad` | branch `main`, **no commits yet** | everything working-tree only; `rl/` untracked |
| `gryth-dev` | `49987a4` | clean; symlinks into frozen `glial-dev` |

`glade-wz` is confirmed the current Glade/Glial integration evidence: its
`glade` member equals taut-dev's (`61617d5`) and its `glial` member
(`b3ee665`, 2026-07-18) is the newest relevant checkout found. The datascad
pin (`datascad/rl/harness/TAUT_PIN.json:7-9`) states it pins taut-shape base
commit `389c867` **plus** the uncommitted atom/swmr working-tree content by
sha256 — consistent with the dirty state observed above.

## 2. Executive recommendation

Adopt a **validated composite/profile model** (Candidate C):

- **One canonical registry** (Taut's `SHAPES` in
  `taut-dev/taut/src/taut/ir/shapes.py`) listing every public shape name, each
  classified as an **engine shape** (owns a taut-shape contract + corpus +
  per-language engines), a **profile** (a named, fixed-parameter configuration
  of an engine core), or an **interaction kind** (no delivery engine).
- **Six engine shapes**: `atom`, `log`, `stream`, `swmr`, `value`, `crdt`.
  `value` is **added to the Taut registry** (it is live everywhere else and is
  the one flagship shape a Taut method cannot currently declare).
- **Two profiles**: `snapshot_delta` = profile of the `swmr` core with
  `reset_policy=expire`; `text_crdt` = profile of the `crdt` core with a text
  payload/merge binding and its own convergence oracle.
- **One interaction kind**: `unary` (delivered once; the codegen "call" arm).
  It stays in the registry so shape remains the sole method discriminator
  (D22) — its classification, not its mechanics, changes.
- **Not Taut shapes**: `exchange` remains Glade's directed frame/routing
  surface kind (live, correct, but transport-layer); `message` and `window`
  are **rejected/unsupported** — semantics are defined nowhere, no live
  declaration uses either, and both must fail closed at declaration time.
- **Retention, writer cardinality, and merge stay intrinsic to the shape**,
  exposed as registry capability metadata; Glade's separate `RetentionPolicy`
  gets a per-shape legality table instead of free composition.

Migration is small and mostly additive: one registry edit + regen in Taut, a
fail-closed dispatch registry in Glial (already Step 0.3), declaration-time
validation in glade-decl/appdecl (wire enum values retained, so no wire or
corpus version bump), no taut-shape wire change, no Datascad re-pin, no
package major bump.

## 3. Evidence and current catalogues

### 3.1 The four "shape" carriers (they are not one catalogue)

1. **Taut method registry** — `taut-dev/taut/src/taut/ir/shapes.py:27-56`
   names `unary, atom, log, stream, swmr, snapshot_delta, crdt`, each a point
   in axes (payload/history/initiation/writers) plus `events` (out-slots) and
   `delivery` (`once`|`stream`). Shape is the **sole method discriminator**
   (`shapes.py:2-3`, `model.py:81-94`); validation rejects unknown shapes and
   out-slot mismatches (`validate.py:106-126`); `out` must be non-empty for
   every method (`validate.py:111-115`). The registry is exported wholesale
   into every generated `.ir.json` (`export.py:45`). A method's shape change
   is a **breaking** schema change (`compat.py:128-131`). The only codegen
   consequence today is call-vs-subscribe (`gen/scaffold.py:413,457,487`);
   the architecture doc states this plainly: "`shape` drives no codegen …
   left unspecified and hand-rolled per consumer"
   (`taut-dev/taut-shape/dev-docs/TautShapeArchitecture.md:35-39`).
2. **taut-shape contracts** — `taut-dev/taut-shape/ir/` holds `shape_log`,
   `shape_value`, `shape_atom`, `shape_swmr` (`ir/` listing; the latter two
   uncommitted). Corpora: `log.v0.json` (25 vectors per
   `glade-wz/glial/dev-docs/DecisionLog.md:9-10`), `value.v0.json` (11),
   `atom.v1.json` (28), `swmr.v1.json` (32), plus the re-homed `fold.v0.json`
   (12) (`taut-dev/taut-shape/corpus/README.md:21-142`). Note the set
   mismatch with carrier 1: `value` has a contract but no registry row;
   `stream`, `snapshot_delta`, `crdt` have registry rows but no contract.
3. **Glade wire `Op.shape`** — `taut-dev/taut/ir/glade.taut.py:58-60` defines
   `Enum("Shape", value=0, log=1, stream=2)`: a per-op **fold selector**
   ("fold: shape (selects the taut fold)", `glade.taut.py:85`), three values
   only. `exchange` is not here — it is a **frame pair**
   (`ExchangeReq`/`ExchangeRes`, `glade.taut.py:150-160`), and terminal-style
   liveness is the `Channel*` frames ("ephemeral, never replicated",
   `glade.taut.py:162-163`).
4. **Glade declaration enum** — `glade-wz/glade-decl/ir/glade_decl.taut.py:50-51`:
   `Enum("Shape", value=0, log=1, message=2, stream=3, exchange=4, window=5)`,
   mirrored by the node's `.glade` parser
   (`glade-wz/glade/node/src/appdecl.rs:40`) and the hand-written TS type
   (`glade-wz/glade-decl-ts/src/api.ts:3`). Alongside it, an independent
   `RetentionPolicy` enum (`latest, from_cursor, ttl`,
   `glade_decl.taut.py:72-73`) rides `BindingDecl.retention`
   (`glade_decl.taut.py:95-102`).

### 3.2 What is actually live, per consumer (declaration vs test vs fixture vs runtime)

- **Taut schema declarations** (authoritative IR, not runtime): GripLab
  declares `atom`/`log`/`swmr`/`stream`/`crdt` methods
  (`taut-dev/taut/ir/griplab.taut.py:87,92,97,104,149`); razel declares one
  `atom` method (`taut-dev/taut/ir/razel.taut.py:109-110`). GripLab's CRDT is
  explicitly contract-only ("the live GripLab slice does not serve it",
  `taut-dev/taut/dev-docs/TautCrdt.md:55-57`).
- **taut-shape engines (corpus-conformant code)**: `log` only, in all three
  languages (`taut-dev/taut-shape-rs/crates/taut-shape/src/lib.rs:1-4`,
  `taut-shape-ts/README.md:1-9`, `taut-shape-py/README.md:1-13`), with a live
  3×3 interop matrix for log (`taut-dev/taut-shape/matrix/driver.py:1-25`).
  `value`/`atom`/`swmr` have corpora + Python reference engines embedded in
  generators only (`corpus/README.md:62-67,109-112`).
- **Glade/Glial runtime (end-to-end)**: Glial's `value` fold passes **all 11**
  value vectors; its `log` fold passes the **6 immediate** log vectors, scope
  recorded as GAP-1 (`glade-wz/glial/test/oracle.test.ts:65-77,83-90`;
  `glial/dev-docs/DecisionLog.md:8-26`). Dispatch is `log` vs everything-else:
  `this.isLog = decl.shape === "log"` (`glial/src/instance.ts:76`), same in
  the grip adapter (`glial/src/grip/index.ts:142`), the TS client
  (`glade/client-ts/src/session.ts:64`), and the Rust client, whose comment is
  candid: "anything not `log` folds as a value"
  (`glade/client-rs/src/session.rs:14-23`).
- **Live Glade declarations**: every committed `.glade` binding in glade-wz is
  `log` (11) or `value` (4) (swept across all `*.glade`); `exchange` is live
  as a **service/directed surface** (`grazel/apps/grazel-app.glade:39`
  `service grazel gwz.ops`; provider routing in
  `glade/node/src/exchange.rs:62-79`; supplier seam split "EXCHANGE surfaces →
  serveExchange … VALUE/LOG/WINDOW surfaces → serveShare",
  `glial/src/supplier/index.ts:13-26`). `message` and `window` appear **only**
  as enum members and as codec-coverage vectors in glade-decl's own corpus
  (`glade-wz/glade-decl/corpus/build.py:103-111` — including a
  `shape="message"` + `policy="from_cursor"` combination no validator
  questions). One live retention word is outside the enum entirely:
  `binding term.log log share commons windowed`
  (`grazel/apps/grazel-app.glade:25`); the parser stores retention as a free
  string (`glade/node/src/appdecl.rs:128`).
- **Datascad (fixture/contract pin, not runtime)**: hash-pins the uncommitted
  atom/swmr contract (`datascad/rl/harness/TAUT_PIN.json:3-34`) and validates
  fixtures against it; `window` (P9 case 05) and `log` (P8 query d) are
  explicitly asserted-and-skipped (`datascad/rl/harness/TAUT_ADAPTER.md:3-8,
  241-252`). Post-PH0-D20 its snapshot numbering is identical to taut-shape's
  (`TAUT_ADAPTER.md:191-221`).
- **Gryth (mock-only)**: all surfaces are grip-core mock atoms; "No glade
  binding in gryth-ui" (`gryth-dev/dev-docs/GrythDemoProposal.md:186-187`);
  the binder it would reuse dispatches per shape as log-vs-value
  (`GrythDemoProposal.md:111-117`). `AtomValueTap` is a UI-local state
  container (`glade-wz/grip-core/src/core/atom_tap.ts:57`) — not Taut's
  `atom`.
- **Additional consumers found by search** (beyond the prompt's list):
  gwz-py's hand-rolled log reader `wait_events`
  (`gwz-dev/gwz-py/src/gwz/bridge.py`, named as prior art in
  `TautShapeArchitecture.md:41-47`); razel's vendoring generator explicitly
  excludes taut-shape (`razel-dev/tools/crates_gen/generator.py:34-36`);
  glade-chat declares `log`/`value` surfaces
  (`glade-wz/glade-chat/src/manifest.ts:64-70`). No consumer of
  `message`/`window`/`text_crdt` exists anywhere searched.

### 3.3 Inference drawn from §3.1–3.2 (marked as such)

The system does not have one shape catalogue with drift; it has **two genuine
catalogues and two projections**. The Taut registry and the taut-shape
contracts are both *delivery* catalogues (mismatched sets); the Glade wire
enum is a *fold* projection (3 values); the Glade declaration enum is a
*surface-kind* vocabulary that mixes delivery shapes with a transport pattern
(`exchange`) and two undefined words (`message`, `window`). Any decision that
treats these as one flat namespace will mis-classify something.

## 4. Semantic decomposition

Values are from cited evidence; *(inf)* marks inference; `unknown` means no
authoritative definition exists. "Frame" below = the shared mailbox engine
frame (held reads, timers-as-messages, `stream_id` addressing, seal/close
lifecycle, `ProducerStop`, diagnostics) established by `shape_log`
(`taut-dev/taut-shape/ir/shape_log.taut.py:100-176`) and reused by
atom/swmr (`shape_atom.taut.py:12-21`, `shape_swmr.taut.py:82-85`).

### 4.1 `unary`

| Axis | Value |
| --- | --- |
| Interaction | One request / one response (`shapes.py:28-31`, `delivery="once"`) |
| Initiation | Pull (registry); engine-inert — there is no engine |
| Producer cardinality | The service handler (writers="single", registry) |
| Consumer cardinality | The caller; N/A beyond that |
| Payload unit | Whole response (sole slot `value`) |
| Ordering | N/A (single response) |
| Retention/history | None |
| Reader position | None |
| Slow consumer | N/A |
| Lifecycle | Call lifetime only |
| Recovery | Re-call *(inf)* |
| Merge | None |
| Identity/addressing | Method + transport correlation (adapter-owned) |
| Existing engine core | **None — interaction kind.** The "degenerate delivered-once member" (`shapes.py:2-3`); codegen emits a call (`scaffold.py:413`) |
| Actual consumers | Every default-shape method (`dsl.py:191` default `shape="unary"`); e.g. `presence.get`, `chat.post` (`griplab.taut.py:89-95`) |

### 4.2 `value`

| Axis | Value |
| --- | --- |
| Interaction | Write ops in; immediate read probes out (v0: no held reads, no timers — `shape_value.taut.py:30-32`) |
| Initiation | Pull reads at the engine; push refresh at Glial's event layer (`glial/src/instance.ts:167-173`) |
| Producer cardinality | **Many attributed writers** (`ValueSet{origin,seq,lamport,prev?}`, `shape_value.taut.py:101-106`) |
| Consumer cardinality | Many independent readers (`two_reads_two_streams`, `TautShapeOracle.md:216-217`) |
| Payload unit | Whole state (winning payload) |
| Ordering | Total order by `(lamport, origin)` winner selection (`shape_value.taut.py:5-8`) |
| Retention/history | The accepted **op-set** is retained (reconstructible); materialized read is latest-winner |
| Reader position | None (immediate probe; no cursor) |
| Slow consumer | N/A in v0 (no subscription at contract level) |
| Lifecycle | None in v0 (`shape_value.taut.py:31-32`) |
| Recovery | Re-probe; op-set re-fold; equivocation never mutates state |
| Merge | **LWW register with dedup by `(origin,seq)` and equivocation rejection** (`shape_value.taut.py:24-29`) |
| Identity/addressing | `value_id` + `stream_id`; op identity `(origin, seq)` |
| Existing engine core | Own contract + corpus; Glial local fold conformant to all 11 vectors (`oracle.test.ts:65-77`); no rs/ts/py engines yet (`TautShapeGladeConsolidation.md:139-147`) |
| Actual consumers | End-to-end in Glade/Glial (`ws.tree`, `chat.groups` bindings; `instance.ts:161-165`); **absent from the Taut registry** (`shapes.py:27-56` has no `value`) |

### 4.3 `atom`

| Axis | Value |
| --- | --- |
| Interaction | Subscription-style reads with holds/timers + probe mode (`shape_atom.taut.py:130-141`) |
| Initiation | Registry says `pull|push` (`shapes.py:32-35`); contract is cursor-style pull with held reads — push is the adapter's framing *(inf)* |
| Producer cardinality | Single, node-local; **no wire enforcement** (no `writer_id`; contrast swmr) |
| Consumer cardinality | Many streams, each `stream_id`-addressed (`shape_atom.taut.py:23-28`) |
| Payload unit | Whole state (`AtomValue{version, payload}`) |
| Ordering | Total scalar `version` change counter (`shape_atom.taut.py:96-102`) |
| Retention/history | **Latest only**; no floor, no expiry, terminal still readable (`shape_atom.taut.py:32-39`) |
| Reader position | Scalar `version`; absent = 0; beyond-current clamped (`shape_atom.taut.py:77-81`) |
| Slow consumer | None needed — late reader gets latest (`subscriber_join_mid_stream`, `TautShapeOracle.md:269-270`) |
| Lifecycle | Full frame lifecycle: seal/close/failed, holds, timers, `ProducerStop` (`shape_atom.taut.py:113-147`) |
| Recovery | Latest refresh (re-read) |
| Merge | None — overwrite (`replacement_overwrites`, `TautShapeOracle.md:264-265`) |
| Identity/addressing | `atom_id` + `stream_id` (`AtomSwmrNotes.md:24-33`) |
| Existing engine core | Own contract + 28-vector corpus v1 (uncommitted); reference engine in generator only |
| Actual consumers | Declarations: `presence.subscribe` (`griplab.taut.py:87`), `build.subscribe` (`razel.taut.py:109`); fixture pin: Datascad (`TAUT_ADAPTER.md:29-37`); no runtime engine consumer yet |

### 4.4 `log`

| Axis | Value |
| --- | --- |
| Interaction | Cursor-in/cursor-out reads; holds/timers/probe (`shape_log.taut.py:112-133`) |
| Initiation | Registry `pull|push`; engine is pull/held-read; push is adapter framing *(inf)* |
| Producer cardinality | `writers="source"` (registry); node-local unaddressed producer in v0 (`shape_log.taut.py:100-110`) |
| Consumer cardinality | Many disposable streams; position lives in the client-held cursor (D3, `shape_log.taut.py:21-25`) |
| Payload unit | Whole records (`LogRecord{seq, payload}` opaque) |
| Ordering | Total scalar `seq` (single-origin: "the cursor is a scalar, not a vector", `TautShapeArchitecture.md:102-103`) |
| Retention/history | Append-only within a **bounded window**; consumer-driven `Evict`; floor (`shape_log.taut.py:139-142`) |
| Reader position | Scalar cursor; absent = START(0); below floor ⇒ `expired` with earliest resumable cursor — **client-decided** recovery (`shape_log.taut.py:62-63,144-149`) |
| Slow consumer | Catch-up by cursor + `max_records`/`max_bytes` batching (D10) |
| Lifecycle | Full frame lifecycle (seal→eof, close→closed/failed, `ProducerStop`) |
| Recovery | Replay from cursor; expiry is a state, never an error (D9) |
| Merge | None at the delivery contract. (Glade's *replicated* log converges by fold `(lamport, origin, seq)` — a different layer; see F5-F14) |
| Identity/addressing | `log_id` + `stream_id` |
| Existing engine core | The reference engine family: rs/ts/py engines + 3×3 matrix green (`TautShapeImplementationPlan.md:38`) |
| Actual consumers | End-to-end: Glial log assembly (6-vector immediate subset, GAP-1); declarations `chat.subscribe` (`griplab.taut.py:92`), 11 `.glade` bindings; prior art gwz-py `wait_events` |

### 4.5 `message`

| Axis | Value |
| --- | --- |
| Interaction | `unknown` — plausibly one-way fire-and-forget *(inf)*; defined nowhere |
| Initiation … Merge | `unknown` on every axis: no schema, no fold, no frames, no doc defines it |
| Identity/addressing | `unknown` |
| Existing engine core | **None.** Exists only as decl enum member (`glade_decl.taut.py:51`), parser word (`appdecl.rs:40`), and a codec-coverage corpus vector (`glade-decl/corpus/build.py:109-111`) |
| Actual consumers | **None** (no live declaration found; Glial would silently fold it as `value` — `instance.ts:76`) |

A precise missing decision, not an invented semantic: Taut cannot even express
a no-response method today (`out` must be non-empty, `validate.py:111-115`),
so `message` has no honest mapping target (see F5-F16).

### 4.6 `stream`

| Axis | Value |
| --- | --- |
| Interaction | Subscription; live-only (`TautShapeRoadmap.md:101-116`) |
| Initiation | Registry `push` (`shapes.py:40-43`); in the mailbox model a subscribe is a permanently-held read (`TautShapeRoadmap.md:137-141`) |
| Producer cardinality | `source` (registry); node-local *(inf)* |
| Consumer cardinality | Many live subscribers |
| Payload unit | `whole-or-delta` events, not stored (`StreamEmit` sketch, `TautShapeRoadmap.md:122-127`) |
| Ordering | Emission order; **no `seq`** ("history none means no position to name", roadmap table) |
| Retention/history | **None** — no backfill, no resume; a disconnect loses the gap by contract (`TautShapeRoadmap.md:114-116`) |
| Reader position | None |
| Slow consumer | **The defining open policy**: drop / coalesce / bounded buffer (D24, `TautShapeRoadmap.md:519-523`) |
| Lifecycle | Frame minus eof/expired (`TautShapeRoadmap.md:127-133`) |
| Recovery | None (that is the contract) |
| Merge | None |
| Identity/addressing | `stream_id` (subscriber) |
| Existing engine core | **None** — roadmap design only; plan Phase 5 |
| Actual consumers | Declaration only: `session.output.subscribe` (`griplab.taut.py:104`); Glade models the need as `Channel*` frames (`glade.taut.py:162-174`); wire enum member exists (`glade.taut.py:60`); Glial would mis-fold it as `value` today |

### 4.7 `exchange`

| Axis | Value |
| --- | --- |
| Interaction | **Directed duplex request/response**, correlation-matched 1:1 (`ExchangeReq{corr}`/`ExchangeRes{corr}`, `glade.taut.py:150-160`) |
| Initiation | Client pull toward the authority; never fan-out (`exchange.rs:1-14`) |
| Producer cardinality | Exactly one authority provider per `(share, glade_id)` (`attach_provider`, `exchange.rs:82-90`) |
| Consumer cardinality | Any requester with routing |
| Payload unit | Whole request/response, opaque |
| Ordering | Per-correlation only |
| Retention/history | **None — never replicated, never folded, never cached** (`exchange.rs:10-12`) |
| Reader position | None |
| Slow consumer | Timeouts answered as data (`exchange.rs:39-45`) |
| Lifecycle | Request lifetime; provider attach/detach |
| Recovery | Re-request *(inf)* |
| Merge | None |
| Identity/addressing | `(share, glade_id)` routing + `corr`; claim-holding authority |
| Existing engine core | **None in taut-shape** — it is Glade frame vocabulary + routing (transport/session layer) |
| Actual consumers | **Live end-to-end in Glade**: `service grazel gwz.ops` (`grazel-app.glade:39`), supplier `serveExchange` (`glial/src/supplier/index.ts:15-19`), typed manifest test (`glial/test/manifest.test.ts:25`) |

### 4.8 `window`

| Axis | Value |
| --- | --- |
| All delivery axes | `unknown` as a shape. The word denotes at least four different things in-tree: (a) decl enum member with no semantics (`glade_decl.taut.py:51`); (b) an out-of-enum **retention word** in a live binding (`grazel-app.glade:25` `windowed`); (c) reader **window-steering** on an swmr-shaped surface (`file.window.update` role=`ctl` + `FileSnapshot.window_start/end`, `griplab.taut.py:39-45,99-100`); (d) the log engine's internal **store window** (`taut-shape-rs/.../log/window.rs:1-6`) |
| Existing engine core | None. Consolidation P3 sketches a "windowed projection over a log" contract (`TautShapeGladeConsolidation.md:179-183`); plan §3.2 keeps it provisionally a projection/retention profile (`TautShapeImplementationPlan.md:77-79`) |
| Actual consumers | None. Datascad P9 case 05 declares mapping `window` and is asserted-and-skipped (`TAUT_ADAPTER.md:241-252`) |

### 4.9 `swmr`

| Axis | Value |
| --- | --- |
| Interaction | Cursor reads with holds/timers/probe (`SwmrReadRequest`, `shape_swmr.taut.py:232-236`) |
| Initiation | Registry `push` (`shapes.py:44-47`); contract is cursor-in/cursor-out pull — direct evidence the registry initiation axis is not engine-real (F5-F10) |
| Producer cardinality | **Exactly one bound writer, wire-enforced**: first content input binds `writer_id`; later different writer rejected `writer_conflict` (`shape_swmr.taut.py:29-37`; `AtomSwmrNotes.md:179-199`) |
| Consumer cardinality | Many disposable streams (D3 kept universal — no steering built; `AtomSwmrNotes.md:293-310`) |
| Payload unit | Snapshot (whole state at seq) + deltas (`SwmrSnapshot`, `SwmrDelta`, `shape_swmr.taut.py:156-164`) |
| Ordering | Total scalar delivery seq; snapshot re-base consumes **no** seq slot (PH0-D20, `shape_swmr.taut.py:42-50`) |
| Retention/history | Reconstructible: snapshot + bounded delta window (`max_deltas` hard backpressure — reject, never silent-evict; `AtomSwmrNotes.md:201-222`) |
| Reader position | Scalar cursor; **absent ≠ {seq:0}** (deliberate D8 divergence, `AtomSwmrNotes.md:126-149`); `next_cursor` optional (present iff a snapshot exists) |
| Slow consumer | Falls behind the base ⇒ typed reset with fresh snapshot in the same response |
| Lifecycle | Full frame lifecycle + producer `SwmrReset` (reason normalized to `producer_requested`, opaque `detail`; `shape_swmr.taut.py:191-208`) |
| Recovery | **Engine-repaired in-band**: `state=reset` + fresh snapshot+tail (vs log's client-decided `expired`; `shape_swmr.taut.py:66-73`) |
| Merge | None (single writer) |
| Identity/addressing | `swmr_id` + `stream_id` + `writer_id` |
| Existing engine core | Contract + 32-vector corpus v1 (uncommitted); reference engine in generator; plan says reset-epoch correctness is **not ready to freeze** (`TautShapeImplementationPlan.md:41,180-199`) |
| Actual consumers | Declaration `file.subscribe` (`griplab.taut.py:97-98`, binding only `{snapshot, delta}` — not `reset`); fixture pin Datascad (numbering now identical, `TAUT_ADAPTER.md:191-221`); no runtime |

### 4.10 `snapshot_delta`

| Axis | Value |
| --- | --- |
| All axes | As `swmr` except: no in-band reset — below-base becomes client-decided expiry (`TautShapeRoadmap.md:271-277`); registry row differs only by dropping the `reset` event (`shapes.py:48-51`) |
| Existing engine core | **None**; plan §3.2 mandates it "must not fork a second snapshot/delta store" (`TautShapeImplementationPlan.md:73-75`); D28 recommends one engine + `reset_policy` knob, explicitly deferred (`AtomSwmrNotes.md:312-326`) |
| Actual consumers | None (registered "contract surface, unused by GripLab", `shapes.py:20-22`) |

### 4.11 `crdt`

| Axis | Value |
| --- | --- |
| Interaction | Bidirectional: clients write ops; engine fans out (`initiation="push-bidi"`, `shapes.py:52-55`; `TautShapeRoadmap.md:355-371`) |
| Initiation | Push-bidi (the only bidi registry entry) |
| Producer cardinality | **Many attributed writers with merge** (`writers="multi-merge"`) |
| Consumer cardinality | Replicated peers (each also a writer) |
| Payload unit | Operations (`Op{origin,seq,prev,lamport,refs,payload}`, `glade.taut.py:87-97`) |
| Ordering | Causal/partial: lamport + refs; fold gives deterministic total order |
| Retention/history | Reconstructible op log + version vector (`CrdtState`, `TautCrdt.md:37-41`) |
| Reader position | **Vector**: per-origin heads (`StreamHeads`/`missing_for`; `TautShapeRoadmap.md:388-396`) |
| Slow consumer | Anti-entropy gap-ship on resume |
| Lifecycle | Session attach/resume; equivocation is the new failure mode (forked `(origin,seq)`; `glade/client-ts/src/fold.ts:20-33`) |
| Recovery | Peer sync (heads exchange, ship gaps) |
| Merge | Deterministic convergence: fold family (lww/log) proven cross-language (`fold.v0.json`, `corpus/README.md:119-142`); field-merge vocabulary `lww|counter` (`TautCrdt.md:10-23`) |
| Identity/addressing | `(stream_id, origin)` question open (D26, `TautShapeRoadmap.md:536-541`) |
| Existing engine core | **The mechanism exists inside Glade** (store/session/folds/chain, oracle-backed) but as substrate, not a taut-shape contract; Taut registry row is wire/contract-only (`shapes.py:20-23`) |
| Actual consumers | Declaration `board.sync` binds `{op}` only — the `sync` slot is unbound (`griplab.taut.py:149-150`); Glade's whole replication layer is the de-facto runtime |

### 4.12 `text_crdt`

| Axis | Value |
| --- | --- |
| All axes | As `crdt`, with a text payload/merge binding: ops with stable position identity, text-specific convergence oracle (`TautShapeGladeConsolidation.md:185-190`); "specialization layered over the common convergence engine" (`TautShapeImplementationPlan.md:75-77`); `EngineNotBound` if declared without an engine (`TautCrdt.md:20-23`) |
| Existing engine core | None anywhere (name appears only in planning + a decl-surface comment, `glade_decl.taut.py:48-49`) |
| Actual consumers | None |

## 5. Overlap findings

Format: `ID | names/layers | relationship | evidence | consequence | proposal implication`.

**F5-F01** | all names / four carriers | name collision & category error (system-level) | §3.1: `shapes.py:27-56` vs `taut-shape/ir/` vs `glade.taut.py:60` vs `glade_decl.taut.py:50-51` have four non-identical name sets | any "one flat list" decision mis-classifies at least one carrier; consolidation keeps failing | the canonical registry must classify names (engine / profile / interaction kind / non-Taut), not merely list them.

**F5-F02** | `value` vs Taut registry | distinct + missing | `value` absent from `shapes.py:27-56`; live end-to-end in Glial (`oracle.test.ts:65-77`); contract exists (`shape_value.taut.py`) | a Taut method literally cannot declare the system's most-exercised shape; `validate.py:107` would reject `shape="value"` | add `value` as a canonical engine shape row (additive).

**F5-F03** | `unary` / `message` / `exchange` | same category (interaction kinds), different layers; `message` = undefined | `unary`: `delivery="once"` + call codegen (`shapes.py:28-31`, `scaffold.py:413`); `exchange`: frames + authority routing, "never replicated" (`glade.taut.py:150-160`, `exchange.rs:1-14`); `message`: no semantics anywhere (§4.5) | treating these as delivery engines would manufacture state machines nothing needs | `unary` stays a registry interaction kind; `exchange` stays Glade surface vocabulary (not a Taut shape); `message` rejected/unsupported.

**F5-F04** | `value` / `atom` | distinct engines sharing a read affordance | multi-writer attributed LWW + equivocation (`shape_value.taut.py:24-29`) vs single-writer versioned mailbox with lifecycle (`shape_atom.taut.py:23-39`); wire vocabularies share almost nothing | merging them would either lose attribution/merge or burden the simple mailbox with fold identity | keep both canonical; plan's acceptance criterion (`TautShapeImplementationPlan.md:132-134`) is confirmed, not just inherited.

**F5-F05** | `value` / `crdt` | shares the op/merge substrate; distinct delivery contract (specialization by materialization) | value's fold is glade's lww fold (`shape_value.taut.py:5-8`); crdt delivers ops + sync with vector resume (`shapes.py:52-55`, roadmap §4.2) | value *is* an LWW-register CRDT; the delivery difference (engine-materialized whole vs op feed) is what earns two names | classify `value` as engine shape now; record the option to re-core it as a materialized profile of the crdt engine at Phase 7 without renaming (see §15).

**F5-F06** | `log` / `stream` / `message` | log vs stream: distinct engines on the retention/resume axis sharing the mailbox frame; message: unrelated (F5-F03) | stream deletes cursor/window/eof and surfaces the overflow policy the window hid (`TautShapeRoadmap.md:118-157`) | one knobbed engine would let a "cursor on retention=none" contradiction exist | two engine shapes; overflow is a `stream` profile knob (D24), not a new shape.

**F5-F07** | `window` vs everything | name collision / category error (4 senses); no shape semantics | §4.8 evidence: enum member, out-of-enum retention word, swmr ctl steering, internal store window | any engine built now would be built from a pun, not a spec; Datascad already skips it | reject/unsupported; revisit via the s-window trace as a **profile** over log/swmr per plan §3.2; fix the `windowed` retention word (F5-F11).

**F5-F08** | `atom` / `swmr` | distinct engines; shared frame; NOT degenerate-of-each-other | atom keeps D8 (absent=0, next always present, clamp; `shape_atom.taut.py:77-81,158-167`); swmr deliberately diverges (absent≠0, optional next, typed reset; `AtomSwmrNotes.md:126-177`); atom is the roadmap's degenerate **log**, not swmr (`TautShapeRoadmap.md:93-97`) | folding atom into swmr imports reset/optional-cursor complexity into the shape whose value is simplicity | both canonical engines; unify only documentation of the shared frame.

**F5-F09** | `log` / `swmr` / `snapshot_delta` | swmr distinct from log (recovery contract); snapshot_delta = policy profile of swmr | engine-repaired in-band reset vs client-decided expired (`shape_swmr.taut.py:66-73`); rebase-at-base + writer binding are new store-core semantics (roadmap §3.3); registry's separate `snapshot_delta` row differs only by the `reset` event — but `reset` is not a bindable payload slot in practice (griplab binds `{snapshot, delta}` only, `griplab.taut.py:97-98`; the contract models reset as a *state* + reason + detail, `shape_swmr.taut.py:114-115,272`) | the registry's slot-set distinction between swmr and snapshot_delta is illusory; a second engine would fork the store (plan §3.2 forbids it) | `snapshot_delta` = canonical **profile** (`core=swmr`, `reset_policy=expire`), per D28's recommendation, decided now.

**F5-F10** | registry axes vs contracts | category error inside the registry: `initiation` (and partly `payload`) are adapter-level, not engine-level | swmr registry says `push` (`shapes.py:44-47`) but the contract is cursor-in reads (`shape_swmr.taut.py:232-236`); roadmap: the push/pull inversion is "cosmetic" in a mailbox (`TautShapeRoadmap.md:137-141`) | generators or validators keying on `initiation` would encode a fiction | keep the axes as documentation metadata; the normative discriminators are writer model, position kind, retention/recovery class, payload granularity, lifecycle (§4 evidence).

**F5-F11** | shape vs Glade `RetentionPolicy` | orthogonal axis with un-validated overlap ⇒ expressible contradictions | `RetentionPolicy{latest, from_cursor, ttl}` (`glade_decl.taut.py:72-73`); nothing validates shape×retention (decl corpus happily encodes `message`+`from_cursor`, `build.py:109-111`); parser takes retention as any string — live `windowed` (`appdecl.rs:128`, `grazel-app.glade:25`) | `value`+`from_cursor` or `log`+`latest` are declarable today and mean nothing; a fourth retention vocabulary (`windowed`) already leaked in | add a per-shape retention legality table enforced at declaration (manifest build + appdecl + glade-decl validation); reject unknown retention words.

**F5-F12** | declared vocabulary vs engines (Glial/clients) | category error at dispatch: everything non-`log` executes as `value` | `instance.ts:76`; `grip/index.ts:142`; `session.ts:64`; `client-rs/session.rs:14-23` ("anything not log folds as a value") | a declared `stream`/`message`/`window`/`exchange` surface silently gets LWW semantics | Step 0.3's fail-closed adapter registry is a prerequisite of any catalogue outcome; register exactly `{value, log}` today.

**F5-F13** | `crdt` / `text_crdt` | strict specialization (payload/merge profile) | unanimous: `TautShapeImplementationPlan.md:75-77`, `TautShapeGladeConsolidation.md:185-190`, `TautCrdt.md:20-23` (engine slot, `EngineNotBound`) | a separate delivery shape would fork identity/transport/dedup/bootstrap (explicitly forbidden, plan §7.4) | `text_crdt` = canonical **profile** (`core=crdt`, payload profile `text`), name reserved now, engine at Phase 7.

**F5-F14** | `log` (taut-shape) / `log` (glade) | one public name, two mechanisms at two layers (shares a read contract, not an engine) | taut-shape log is single-origin scalar-cursor (`TautShapeArchitecture.md:102-103`); glade's log surface is a multi-origin op-fold (`fold_log` by `(lamport,origin,seq)`, `fold.ts:1-8`) assembled by Glial into the log read contract's immediate subset (GAP-1) | "log" claims about resume/cursor semantics are layer-dependent; conflation would re-derive the fall-through bug in new places | the decision record must name the layering: replication (Glade op layer / future `crdt` core) **below**, delivery contract (`log`) **above**; Glial's assembly is a consumer-side implementation gated by corpus subset (graduating in plan Phase 3/8).

**F5-F15** | `atom` (Taut) / `AtomValueTap` (grip-core); `window` (shape word) / `log/window.rs` (store) | name collision across unrelated layers | `atom_tap.ts:57` is a UI state container; `log/window.rs:1-6` is the store window; plan already warns "`AtomValueTap` is not the Taut `atom` shape" (`TautShapeImplementationPlan.md:47`) | Gryth cutovers could wire the wrong "atom" | no rename (public grip API); one glossary paragraph in the decision record.

**F5-F16** | `message` vs Taut method model | unrepresentable interaction | every method must bind non-empty `out` (`validate.py:111-115`) | fire-and-forget has no legal Taut declaration today; use-case 2 can only be an acked unary | record as an explicit open decision (add a one-way interaction kind **only** when a real consumer appears); do not pre-bake `message`.

**F5-F17** | `atom` writers axis vs wire | registry claim without enforcement (asymmetric with swmr) | registry `writers="single"` for atom (`shapes.py:32-35`); atom wire has no `writer_id` (whole schema, `shape_atom.taut.py`); swmr added it precisely because otherwise "the wire vocabulary has no way to detect a second writer" (`AtomSwmrNotes.md:179-199`) | atom's single-writer promise is convention-only; adding `writer_id` later is additive (optional field) but changes corpus vectors | decide before atom `v1` freeze: add writer binding now (symmetry) or record it as adapter-enforced (see §15).

**F5-F18** | `crdt.sync` slot vs declarations | registry slot that is engine protocol, not app payload | `events={op, sync}` (`shapes.py:52-55`) but `board.sync` binds `{op}` only (`griplab.taut.py:149-150`); roadmap: sync carries heads/anti-entropy metadata (`TautShapeRoadmap.md:398-404`) | schema authors are offered a slot they can't meaningfully type | narrow `crdt.events` to `{op}` at Phase 7 definition time (or keep `sync` with a fixed engine-owned type); validation already tolerates subset binding, so this is documentation-plus-registry cleanup.

## 6. Use-case tests of the current model

What the **current** system does for each commissioned case (declaration
evidence level marked):

1. **Unary request/response** — works: default `shape="unary"` methods
   (`presence.get`, `griplab.taut.py:89-90`). Declared + generated.
2. **Fire-and-forget** — not expressible: `out` mandatory
   (`validate.py:111-115`); GripLab models commands as acked unary
   (`chat.post` → `ChatMessage`, `griplab.taut.py:94-95`). Gap.
3. **Single-writer status/presence, late subscriber gets latest** — `atom`:
   declared (`presence.subscribe`, `build.subscribe`), corpus pins
   `subscriber_join_mid_stream` (`TautShapeOracle.md:269-270`); no language
   engine yet.
4. **Attributed multi-writer LWW whole value** — `value`: live end-to-end in
   Glial (`ws.tree`, `chat.groups`; all 11 vectors) — but **undeclarable as a
   Taut method** (F5-F02).
5. **Durable chat with cursor replay** — `log`: declared
   (`chat.subscribe`), engines + matrix green; Glial's runtime covers the
   immediate subset only (GAP-1) with glade replication underneath (F5-F14).
6. **Ephemeral terminal, lossy slow consumer** — `stream`: declared
   (`session.output.subscribe`) but engine-less; Glade serves the need via
   `Channel*` frames; a *declared* `stream` surface would today mis-execute
   as `value` in Glial (F5-F12). Gap.
7. **Datascad query results** — `swmr`: contract + corpus fit (typed reset +
   opaque `detail` carries generation; numbering aligned post-PH0-D20,
   `TAUT_ADAPTER.md:191-221`); fixture-adapter level only; reset-epoch
   durability still open (plan 1.1).
8. **Bounded/time-windowed materialized view** — nothing real: `window` is
   four puns (F5-F07); Datascad's window case is skipped. Gap.
9. **Multi-writer replicated state, generic CRDT ops** — `crdt`: registry +
   wire types + reference folds exist; contract-only (GripLab does not serve
   it); Glade's substrate is the working precedent.
10. **Collaborative text** — `text_crdt`: planning-only. Gap.
11. **Generic bidirectional exchange** — Glade `exchange`: live end-to-end
    (grazel gwz.ops); correctly **not** stored/replicated state; not a Taut
    shape.

Score of the current model: 5 of 11 cases have at least contract-level
support with a coherent name; 3 are engine-less declarations that would
silently mis-execute (6, and any premature 8/9 use); 2 are unexpressible
(2, 8); 1 lives in a different layer and keeps being miscounted as a shape
(11).

## 7. Candidate A — compatibility-first flat catalogue

**Model.** Keep one flat `shape="<name>"` everywhere. All twelve names remain
declarable words somewhere; a mapping table (prose + registry docstring)
records which are aliases/profiles: `snapshot_delta` documented as
swmr-profile, `text_crdt` as crdt-profile, `message`/`exchange`/`window`
documented as "interaction/frame patterns — do not implement engines".
Glial's dispatch is still fixed (Step 0.3 is unconditional), but the
declaration surfaces keep accepting every current word.

**Public declaration surface (example).**

```python
method("file.subscribe", role="out", shape="swmr",
       out={"snapshot": Ref("FileSnapshot"), "delta": Ref("FileDelta")})
# glade manifest (unchanged): { id: "app:notes", shape: "value", share, retention? }
```

**Canonical names + one-sentence definitions.** As §4's rows, unchanged; the
table is documentation, not data.

**Aliases/profiles/deprecated/rejected.** `snapshot_delta`, `text_crdt`
documented profiles; nothing formally rejected — `message`/`window` stay
declarable but documented-as-undefined.

**Engine cores and reuse.** Same six cores as Candidate C, but only by
convention; the registry carries no `core` field.

**Codegen selection.** Unchanged: `is_streaming` picks call vs subscribe
(`model.py:102-103`); everything else stays hand-rolled per consumer.

**Retention/writer/merge/lifecycle.** Stay implicit in each shape's docs;
Glade `RetentionPolicy` remains freely composable (F5-F11 unfixed).

**Illegal combinations.** Prevented only where Step 0.3 lands (Glial
dispatch); declarations of `message`/`window`, contradictory retention, and
`shape="value"` methods (still impossible in Taut) remain as today.

**Changes required.** Taut: none (or docstring). taut-shape: none.
Glade/Glial: Step 0.3 only. Datascad: none. Gryth: none.

**Compatibility/migration cost.** Near zero.

**Strongest argument against.** It leaves every found defect in place:
`value` stays undeclarable in Taut (F5-F02), the four-carrier mismatch stays
unnamed (F5-F01), `message`/`window` stay declarable ambient hazards
(F5-F07), retention contradictions stay expressible (F5-F11), and the
registry keeps a row (`snapshot_delta`) whose slot-distinction is illusory
(F5-F09). It is a documentation patch presented as a decision.

## 8. Candidate B — minimal orthogonal engine catalogue

**Model.** `shape` names **only irreducible delivery state machines**:
`{atom, log, stream, swmr, value, crdt}`. Everything else moves to explicit
axes:

- interaction: a separate method field `kind ∈ {call, oneway}` replaces
  `unary` (and would host `message`);
- policy: declaration-level parameters `reset_policy ∈ {in_band, expire}`
  (subsumes `snapshot_delta`), `overflow ∈ {drop, coalesce, buffer(n)}`,
  `payload_profile ∈ {opaque, text}` (subsumes `text_crdt`);
- retention: Glade `RetentionPolicy` merged into those parameters;
- `exchange` stays Glade-only; `window` deleted.

**Public declaration surface (example).**

```python
method("query.subscribe", role="out", shape="swmr",
       params=..., out={"snapshot": Ref("QSnap"), "delta": Ref("QDelta")},
       policy={"reset_policy": "expire"})          # ex-snapshot_delta
method("doc.sync", role="out", shape="crdt",
       out={"op": Ref("TextOp")}, policy={"payload_profile": "text"})
method("audit.note", kind="oneway", params=[("note", STR)])  # ex-message
```

**Canonical names.** Six engine shapes, normatively defined as in §4; no
profile names in the public surface — profiles are parameter values.

**Aliases/deprecated/rejected.** `unary`, `snapshot_delta`, `text_crdt`
become **parsing aliases** (accepted on input, canonicalized to
shape+parameters, never emitted); `message` becomes `kind="oneway"`;
`exchange` non-Taut; `window` rejected.

**Engine cores/reuse.** Identical cores; policy knobs formally attach to the
core (D24/D28 become schema-level).

**Codegen.** `kind` picks call/oneway; `shape` picks subscription machinery;
policy parameters flow into generated adapters.

**Illegal states.** Needs a validation matrix for shape×policy — the axes
reintroduce expressible nonsense (`overflow` on `log`, `reset_policy` on
`atom`) that the flat name previously made unrepresentable.

**Changes required.** Taut: reintroduce a `kind` axis on `MethodDef` and
policy parameters — reversing the ratified D22 design whose stated point is
that "`kind`/`output`/`events` are derived views … the old unary-with-a-shape
illegal state is unrepresentable" (`model.py:91-94`, `shapes.py:2-8`); compat:
every existing method's serialized form changes; a shape change is already
"breaking" per `compat.py:128-131`. taut-shape: contracts unchanged.
Glade: decl enum shrinks (wire-value churn or heavy aliasing). Datascad:
pinned names survive only via aliases. Gryth: unaffected.

**Compatibility/migration cost.** High: schema-surface change in Taut,
alias plumbing in every generator/validator, decl-surface churn in Glade —
for semantics Candidate C achieves with registry rows.

**Strongest argument against.** It un-decides D22. The codebase's one
structural invariant — shape is the sole discriminator, other views derived —
is load-bearing in the model, validator, DSL, and compat checker; Candidate B
trades a proven illegal-state-prevention mechanism (closed names) for an
open parameter space that then needs its own validation matrix to close
again. Maximum orthogonality, negative net safety.

## 9. Candidate C — validated composite/profile model

**Model.** Keep flat public names and the D22 invariant. Make the registry
itself two-level: every public name is a row; every row names its **engine
core** and its **fixed profile parameters**; interaction kinds carry
`core=None`. Orthogonal dimensions (writers, position kind,
retention/recovery class, payload granularity, lifecycle) become **capability
metadata** on the row — machine-readable, exported into every `.ir.json`
(free via `export.py:45`), consumed by validators, Glial's dispatch registry,
and the Phase-2 CLI `--shape` maps. Schema authors never compose axes; they
pick a validated name.

**Public declaration surface.** Unchanged for authors:

```python
method("file.subscribe", role="out", shape="swmr", out={...})
method("query.subscribe", role="out", shape="snapshot_delta", out={...})
```

**Registry sketch** (the shape of the change, not final code):

```python
SHAPES = {
  # interaction kinds (no delivery engine)
  "unary": {..., "delivery": "once", "core": None, "class": "interaction"},
  # engine shapes
  "value": {..., "core": "value", "class": "engine",
            "writers": "multi-merge", "position": "none",
            "recovery": "refold", "granularity": "whole-state"},
  "atom":  {..., "core": "atom",  "class": "engine", ...},
  "log":   {..., "core": "log",   "class": "engine", ...},
  "stream":{..., "core": "stream","class": "engine", ...},   # engine pending (Phase 5)
  "swmr":  {..., "core": "swmr",  "class": "engine", ...},
  "crdt":  {..., "core": "crdt",  "class": "engine", ...},   # engine pending (Phase 7)
  # profiles (share a core; fixed parameters; own conformance rows)
  "snapshot_delta": {..., "core": "swmr", "class": "profile",
                     "profile": {"reset_policy": "expire"}},
  "text_crdt":      {..., "core": "crdt", "class": "profile",
                     "profile": {"payload": "text"}},
}
```

**Canonical names + definitions.** §11's table.

**Aliases/profiles/deprecated/rejected.** Profiles: `snapshot_delta`,
`text_crdt` (stable public words, shared cores, conformance rows of their
own — plan rule 6, `TautShapeImplementationPlan.md:103-104`). Rejected as
Taut shapes: `message`, `window` (fail closed at declaration), `exchange`
(classified as Glade surface vocabulary; a Taut method that rides an
exchange is `unary`). No deprecated names in this round.

**Engine cores and reuse boundaries.** Six cores. The shared **frame**
(mailbox, `stream_id`, holds, timers, lifecycle, `ProducerStop`,
diagnostics) is a documented convention, not code (`TautShapeRoadmap.md:
590-630`: frame generalizes verbatim; store cores are per-shape). A profile
may set only knobs its core declares (`stop_when`, `max_deltas`,
`reset_policy`, `overflow`, payload profile); anything touching states or
message sets is a new engine by definition (§13).

**Codegen selection.** `delivery` picks call vs subscribe (today's
`is_streaming`); `core` + capability metadata select the engine API and
tag-maps for the Phase 2 shape-aware CLI/adapters; profiles resolve to their
core's engine with fixed construction knobs.

**Retention/writer/merge/lifecycle.** Intrinsic to the shape row
(capability metadata); Glade `RetentionPolicy` validated against the shape
(legality table, §12.3).

**Illegal combinations prevented by:** closed name set (unknown ⇒
`validate.py:107` error, unchanged); non-Taut words rejected at Glade
declaration build (manifest/appdecl/glade-decl validation); shape×retention
legality table; Glial fail-closed dispatch (Step 0.3); profile knobs limited
to the core's declared set.

**Changes required.** Taut: one registry edit (+`value` row, +metadata keys)
plus IR regen. taut-shape: docs only (contracts untouched). Glade: decl
validation + Glial dispatch registry. Datascad: none now. Gryth: none now.
Detail in §14.

**Compatibility/migration cost.** Low; almost entirely additive (§14 names
the two behavioral edges: rejected declarations that were previously
silently mis-folded, and the `windowed` retention word).

**Strongest argument against.** The registry becomes the single point of
truth for classification, and its `class`/`core` fields are only as honest
as review keeps them — a future "just add a row" shortcut could smuggle in a
ninth near-duplicate engine; also, keeping `snapshot_delta` and `text_crdt`
as public words costs two names whose distinct value is still unproven by
any consumer (both currently consumer-less).

## 10. Comparative scorecard

1 (poor) – 5 (strong). Justifications compressed; §7–§9 carry the detail.

| Criterion | A (flat/compat) | B (orthogonal axes) | C (validated profiles) |
| --- | --- | --- | --- |
| Semantic orthogonality | 2 — mixture stays implicit | 5 — axes explicit | 4 — axes explicit as metadata, names stay composite |
| Schema-author comprehensibility | 3 — familiar but 4 unexplained words | 2 — every declaration is shape+policy algebra | 4 — pick a name; one-line normative meaning |
| Illegal-state prevention | 2 — only Step 0.3 | 3 — closes some, opens shape×policy space | 4 — closed names + validated knobs + decl validation |
| Engine reuse w/o semantic leakage | 3 — convention only | 4 — knobs formalized | 5 — named cores + profile rows (plan rule 6) |
| Code-generation determinism | 3 — call/subscribe only | 4 — richer, but two discriminators | 5 — one discriminator + machine-readable core/caps |
| Rust/TS/Python burden | 4 — nothing new | 2 — alias + policy plumbing ×3 languages | 4 — engines unchanged; registry data only |
| Current consumer fit | 4 — nothing moves | 2 — breaks D22, decl-surface churn | 5 — every live consumer keeps its words |
| Backward compat / migration risk | 5 — none | 1–2 — Taut method surface changes (breaking per `compat.py:130-131`) | 4 — additive registry; two contained behavioral edges |
| Future extensibility | 2 — more prose per new name | 4 — new payload/policy values cheap | 4 — new profile = row + knob + vectors |
| Testability / conformance clarity | 3 — corpora per shape, mapping informal | 4 — per-core corpora + policy vectors | 5 — per-core corpora + per-profile conformance rows |
| **Total** | **31** | **31–32** | **44** |

A and B tie numerically for opposite reasons (A safe-but-empty, B
clean-but-destructive). C dominates on the criteria Phase 0 exists to serve.

## 11. Recommended canonical catalogue

Columns: `current name | proposed status | canonical name/category |
normative meaning | public declaration? | engine core |
compatibility/migration action | owner`.

| current name | proposed status | canonical name/category | normative meaning (one sentence) | public declaration? | engine core | compatibility/migration action | owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `unary` | interaction kind | `unary` | One request, one whole response, delivered once; no delivery engine exists or may be implied. | Yes (Taut method; the default) | — | None; registry row gains `class="interaction"`, `core=None`. | taut |
| `value` | canonical engine shape | `value` | Attributed multi-writer last-writer-wins whole-value register: op-set deduped by `(origin,seq)`, winner `max(lamport,origin)`, equivocation rejected, reads engine-materialized. | Yes (Taut + Glade) | `value` | **Add to Taut registry** (additive); Glade enum value 0 unchanged; document its CRDT-register nature. | taut-shape (contract), glial/glade (runtime) |
| `atom` | canonical engine shape | `atom` | Single-writer latest-value mailbox: versioned overwrite, held reads, timers, terminal lifecycle, no back-history. | Yes (Taut) | `atom` | None to the name; commit contract after plan Phase 1; decide writer-binding question (§15) before `v1` freeze. | taut-shape |
| `log` | canonical engine shape | `log` | Single-origin retained ordered records with scalar cursor resume, bounded consumer-driven retention, client-decided expiry, full lifecycle. | Yes (Taut + Glade) | `log` | None; decision record names the log-above/replication-below layering (F5-F14). | taut-shape |
| `message` | rejected/unsupported | — | No semantics defined anywhere; fire-and-forget is currently unrepresentable in Taut (`out` mandatory). | No (reject at declaration) | — | Glade enum wire value 2 **reserved** (accepted on decode, rejected on declare, never emitted); revisit only with a real one-way consumer. | glade-decl (rejection), taut (future interaction kind, if ever) |
| `stream` | canonical engine shape (contract pending) | `stream` | Disposable ordered live delivery: no history, no cursor, explicit slow-consumer overflow policy, lifecycle minus eof/expired. | Yes (Taut + Glade) | `stream` (Phase 5) | Name stays declarable in schemas; **fail closed at runtime** until the engine exists (Step 0.3); freeze D24 before IR (plan 5.1). | taut-shape |
| `exchange` | interaction kind (Glade surface kind) | `exchange` (Glade-only) | Directed correlation-matched request/response routed to the claim-holding authority; never replicated, folded, or cached. | Yes in Glade only (binding/service records); **not a Taut method shape** | — (frame routing) | Keep Glade enum value 4 + `service` records; taut-shape excludes it; Taut methods riding an exchange are `unary`. | glade |
| `window` | rejected/unsupported | — | Currently four unrelated meanings (enum word, rogue retention word, swmr reader-steering, store internals); no delivery semantics exist. | No (reject at declaration) | — | Glade enum wire value 5 reserved; fix `grazel-app.glade`'s `windowed` retention word; revisit via s-window as a **profile** over `log`/`swmr` only if independent wire/lifecycle semantics are demonstrated (plan §3.2). | glade-decl now; taut-shape later if ratified |
| `swmr` | canonical engine shape | `swmr` | Single-writer snapshot-plus-delta store with wire-enforced writer binding, bounded delta retention as hard backpressure, and typed engine-repaired in-band reset. | Yes (Taut) | `swmr` | None to the name; reset-epoch durability (plan 1.1) before freeze/re-pin. | taut-shape |
| `snapshot_delta` | canonical profile | `snapshot_delta` = profile of `swmr` | The swmr engine with `reset_policy=expire`: below-base resolves client-decided (expired-like) instead of engine-repaired; no producer in-band reset. | Yes (Taut) | `swmr` | Registry row re-typed `class="profile"`, `core="swmr"` (resolves D28 as recommended); never build a second store; profile conformance rows at Phase 6.2. | taut-shape |
| `crdt` | canonical engine shape | `crdt` | Multi-writer replicated operation delivery: per-origin identity and chains, causal metadata, vector-heads resume, anti-entropy sync, deterministic convergent fold, equivocation rejection. | Yes (Taut) | `crdt` (Phase 7; extracted from Glade) | Registry row kept; narrow/define the `sync` slot at Phase 7.1 (F5-F18); identity model D26 decided there. | taut-shape (extracting glade) |
| `text_crdt` | canonical profile | `text_crdt` = profile of `crdt` | The crdt engine with a text payload/merge binding (stable position identity) and a text-specific convergence oracle. | Yes (reserved name; declarable when Phase 7.4 lands) | `crdt` | Add registry row as `class="profile"`, `core="crdt"` now (name reservation); no engine before Phase 7. | taut-shape |

Non-catalogue glossary entries the decision record should carry (F5-F15):
Glade wire `Op.shape` (a 3-value fold selector, not the catalogue);
grip-core `AtomValueTap` (UI state container); the log engine's internal
"window" (store core).

## 12. Proposed declaration model and examples

### 12.1 The declaration rule

Authors declare `shape="<name>"` from the catalogue — nothing else changes at
the method surface. `out` binds the shape's slots exactly as today
(`validate.py:110-126`). Profiles are declared by their own name; the
generator resolves `core` + fixed knobs from the registry.

### 12.2 The eleven use cases as pseudo-IR

```python
# 1. Ordinary unary request/response (default shape)
method("config.get", role="out", out=Ref("Config"))

# 2. Fire-and-forget command — RESOLVED AS ACKED UNARY (one-way is
#    unrepresentable today; see §15 open decisions before inventing it)
method("audit.note", role="in", params=[("note", STR)], out=Ref("Ack"))

# 3. Single-writer provider status; late subscribers receive latest
method("provider.status.subscribe", role="out", shape="atom",
       out=Ref("ProviderStatus"))                     # razel.taut.py:109 precedent

# 4. Glade's attributed multi-writer LWW whole-value surface  (NEW in Taut)
method("workspace.meta.subscribe", role="out", shape="value",
       out=Ref("WorkspaceMeta"))
# glade: { id: "ws.meta", shape: "value", retention: {policy: "latest"} }

# 5. Durable chat/history with cursor replay
method("chat.subscribe", role="out", shape="log", out=Ref("ChatMessage"))
# glade: { id: "chat.msgs", shape: "log", retention: {policy: "from_cursor"} }

# 6. Ephemeral terminal output; slow consumer may lose data
method("term.output.subscribe", role="out", shape="stream",
       params=[("session_id", STR)], out=Ref("TerminalChunk"))
# engine profile knob at construction (D24): overflow = drop | coalesce | buffer(n)

# 7. Datascad query results (snapshot+deltas, generation reset, retained resume)
method("query.subscribe", role="out", shape="swmr",
       params=[("query_id", STR)],
       out={"snapshot": Ref("QuerySnapshot"), "delta": Ref("QueryDelta")})
# generation & revision context ride SwmrReset.detail / payloads, opaque
# (shape_swmr.taut.py:14-19); nothing relational enters the shape layer.

# 8. Bounded/time-windowed materialized view — NOT a shape: the producer
#    materializes the projection; the reader steers via a ctl method
method("view.subscribe", role="out", shape="swmr",
       out={"snapshot": Ref("ViewSnapshot"), "delta": Ref("ViewDelta")})
method("view.window.update", role="ctl",
       params=[("start", INT), ("end", INT)], out=BOOL)   # griplab.taut.py:99 precedent

# 9. Multi-writer replicated state with generic CRDT operations
method("board.sync", role="out", shape="crdt", out={"op": Ref("CrdtOp")})

# 10. Collaborative text with offline edits and convergence
method("doc.sync", role="out", shape="text_crdt", out={"op": Ref("TextOp")})
# registry resolves core=crdt + payload profile "text"

# 11. Generic bidirectional exchange (request/response lifetimes ≠ stored state)
# NOT a Taut delivery shape. Glade declaration:
#   service grazel gwz.ops                      (grazel-app.glade:39)
#   or SurfaceSpec { id: "gwz.ops", shape: "exchange", share }
# Methods carried over it are unary:
method("gwz.run", role="in", params=[("argv", List(STR))], out=Ref("RunResult"))
```

Common declarations stay concise: cases 1–5 and 9 are one line each; nothing
gained a mandatory new field.

### 12.3 Contradiction validation (the flat name keeps working)

- **Unknown shape** ⇒ existing `validate.py:107` error (unchanged).
- **Slot mismatch** ⇒ existing `validate.py:116-126` (unchanged).
- **Glade declaration**: manifest build (`defineManifest`), `.glade` parsing
  (`appdecl.rs`), and glade-decl validation reject `message`/`window`, and
  enforce the retention legality table:

| shape | legal `RetentionPolicy` | note |
| --- | --- | --- |
| `value` | `latest` | op-set retention is the fold's concern, not declarable |
| `log` | `from_cursor`, `ttl` | `latest` on a log is a contradiction (implies no replay) |
| `stream` | *(needs additive enum member `none`; until then `ttl`)* | decide at Phase 5 with D24 |
| `exchange` | field inert (nothing stored) | validation skips; document |
| others (`atom`/`swmr`/`snapshot_delta`/`crdt`/`text_crdt`) | not currently Glade-declarable surface kinds | reject until a Glade binding for them is ratified |

  Unknown retention words (today's `windowed`) are rejected; the one live
  occurrence in `grazel-app.glade:25` is fixed to `from_cursor` (its surface
  is a log; the "windowed" intent returns as a profile when s-window is
  ratified — F5-F07).
- **Runtime**: Glial's dispatch registry (Step 0.3) registers exactly
  `{value, log}`; any other declared shape raises a typed
  unsupported-shape error at manifest/session construction, with one
  negative test per enum word (plan 0.3 acceptance).

## 13. Engine, adapter, and application boundaries

For each canonical engine core — what the engine owns / what the
transport-session adapter owns / what the consumer-application owns / what a
profile may configure without becoming a new engine:

- **`value`** — engine: op-set, dedup, winner selection, equivocation
  rejection, materialized reads. Adapter: routing (`value_id`), transport,
  response addressing; Glade owns `share/glade_id/key` routing
  (`shape_value.taut.py:94-100`). Application: payload meaning; MV conflict
  surfacing when ratified (additive, `shape_value.taut.py:33-36`).
  Profile knobs: none in v0.
- **`atom`** — engine: version counter, single slot, holds/timers, terminal
  lifecycle, clamp rule. Adapter: `EndStream` on disconnect, real clocks,
  framing. Application: **generation/compatibility semantics** — a
  generation bump is an ordinary replace; the consumer ends and re-requests
  (`AtomSwmrNotes.md:58-70`). Profile knobs: `stop_when` (D6).
- **`log`** — engine: window, cursor resolution, expiry-as-state, batching
  bounds, holds/timers, lifecycle, watermarks. Adapter: transport
  backpressure per client, disconnect cleanup. Application: retention policy
  decisions via `Evict`; payload decode per method `out=`. Profile knobs:
  `stop_when`; retention bounds.
- **`stream`** (to be frozen at Phase 5) — engine: live fan-out, overflow
  policy execution, lifecycle minus eof. Adapter: subscription transport.
  Application: tolerance of loss. Profile knobs: `overflow` (D24) — the
  policy is a knob precisely so one corpus covers all profiles
  (`TautShapeRoadmap.md:519-523`).
- **`swmr`** — engine: writer binding, snapshot/delta store, rebase rule
  (PH0-D20), typed reset resolution, `max_deltas` backpressure, holds/timers,
  lifecycle. Adapter: disconnect cleanup; routing. Application: everything
  relational — generation numbers, revisions, row semantics ride opaque
  `payload`/`detail` (`shape_swmr.taut.py:14-19`); reader steering
  (window.update) is an application ctl method, not engine protocol.
  Profile knobs: `stop_when`, `max_deltas`, and `reset_policy`
  (`in_band` = swmr, `expire` = snapshot_delta).
- **`crdt`** (to be frozen at Phase 7) — engine: op identity, per-origin
  chains, dedup/equivocation, heads/anti-entropy, deterministic fold
  dispatch, fan-out. Adapter: session auth, QoS, chunking — explicitly the
  Glade superstructure that stays behind (`TautShapeRoadmap.md:428-433`).
  Application: payload CRDT semantics (merge engines pluggable,
  `TautCrdt.md:59-70`). Profile knobs: payload profile (`text` ⇒
  `text_crdt`) with its own oracle.

Rule of thumb the decision record should state verbatim: **a profile may set
declared construction knobs; the moment a change adds, removes, or re-types a
message or a state, it is a new engine and needs its own contract row.**

## 14. Migration plan and impact on Steps 0.2/0.3

Smallest-risk sequence (each step independently shippable):

1. **Taut registry/DSL/codegen (Step 0.2 core).** Add the `value` row; add
   `class`/`core`/`profile` metadata keys to every row; docstring becomes the
   canonical catalogue table (§11). Additive: no existing method changes, so
   no breaking diffs under `compat.py`; regenerate exported IR (the `shapes`
   block in every `.ir.json` changes via `export.py:45` — run
   `taut-shape/ir/regen.py` and Glade-side corpus `--check` gates in the same
   change). DSL and validator need **no change** (closed-set check already
   generic). Codegen change: none required now; the metadata is consumed by
   Phase 2's `--shape` CLI maps when they land.
2. **taut-shape contracts and package APIs.** No wire change. Docs:
   architecture/roadmap sections that list the catalogue defer to the
   decision record (Step 0.2 acceptance: "no competing list described as
   canonical"). `snapshot_delta` is recorded as the swmr profile (D28
   resolved); language packages unaffected (log-only today).
3. **Glade declaration enum and retention field.** Keep all six wire values
   (decl corpus `decl.v0.json` byte-stable ⇒ **no corpus version bump, no
   wire tag change**). Add declaration-time validation: reject
   `message`/`window`; enforce the retention legality table (§12.3); trim
   `appdecl.rs` `SHAPES` to `{value, log, stream, exchange}` and validate
   retention words against the enum (+ fix `grazel-app.glade:25`
   `windowed`→`from-cursor` in both byte-identical copies). glade-decl minor
   version bump; no major.
4. **Glial fail-closed dispatch (Step 0.3, unchanged in scope).** Replace
   `isLog` with an explicit adapter registry `{value: ValueRegister-adapter,
   log: LogBuffer-adapter}`; typed unsupported-shape error at
   manifest/session construction; one negative test per declared-but-
   unsupported name (`message`, `stream`, `exchange`, `window`). The TS/Rust
   *clients'* `fold()` dispatch (`session.ts:64`, `client-rs/session.rs:18`)
   gets the same fail-closed treatment or a documented "callers must pass
   only value|log" contract — recommend the former, it is ~5 lines each.
5. **Datascad.** Nothing now: the catalogue changes neither pinned file
   bytes nor names (`atom`/`swmr` keep their meanings). The deliberate
   re-pin stays gated on plan Phase 1 (reset-epoch fix), per plan 1.5.
6. **Gryth.** Nothing now: no Glial dependency exists yet. When providers
   land (plan 8.2), they declare from the canonical set; the decision
   record's glossary paragraph (F5-F15) prevents the AtomValueTap/atom
   confusion.

**Aliases accepted-on-input but never emitted:** the Glade enum's
`message`/`window` wire values (decodable forever, undeclarable); the
`windowed` retention word (reject in new registrations; the one live file is
fixed). `snapshot_delta` is **not** an alias — it stays a first-class
declarable profile name.

**Version/wire impact summary:** no wire tag changes; no corpus version
bumps (`log.v0`, `value.v0`, `atom.v1`, `swmr.v1`, `fold.v0`, `decl.v0` all
byte-stable); no public package major bumps; Taut and glade-decl minor
releases; regenerated `.ir.json` files (metadata block only).

**Impact on Step 0.2:** this document *is* the input; 0.2 reduces to the
registry edit + doc reconciliation above.
**Impact on Step 0.3:** unchanged in scope, now with the exact dispatch
table, the negative-test name list, and the two extra client-side dispatch
sites named (Rust/TS session `fold`).

## 15. Risks, falsification, and open decisions

**Three strongest facts/requirements that would overturn this
recommendation:**

1. **A ratified one-way (no-response) method need.** Today `out` is
   mandatory (`validate.py:111-115`) and `message` is rejected here partly
   *because* it is unrepresentable. A real fire-and-forget consumer (e.g.
   telemetry ping over a Gryth provider) would force either a new
   interaction kind (registry row with `delivery="once", out` optional —
   a validator change, weakening D22's "out always bound" simplicity) or a
   degenerate ack. If that lands, `message` must be re-classified rather
   than left rejected.
2. **s-window demonstrating independent wire/lifecycle semantics.** If the
   windowed-projection trace (consolidation P3,
   `TautShapeGladeConsolidation.md:179-183`) shows priority-first-paint or
   window identity interacting with delivery ordering in ways `log`/`swmr`
   profiles cannot express, `window` graduates from rejected to engine shape
   — exactly the escape hatch plan §3.2 reserves. The rejection here is of
   the current four-way pun, not of the future contract.
3. **The Phase 7 crdt engine subsuming `value` cheaply.** If the extracted
   crdt core plus an lww payload profile plus an engine-materialized read
   mode reproduces `value.v0.json` byte-for-byte, keeping a separate `value`
   core becomes waste; `value` should then be re-cored as a crdt profile.
   The public name and corpus survive either way, which is why this is
   contained rather than fatal — but if it happens *before* Phase 3 builds
   three value engines, the build order should flip.

**Decisions that can be deferred without foreclosing the model:** stream
overflow policy details (D24 — knob shape is fixed, values at Phase 5.1);
crdt identity model (D26) and convergence-oracle format (D27) — Phase 7.1;
`text_crdt` payload details — Phase 7.4; MV surfacing for `value` (additive
field, `shape_value.taut.py:33-36`); re-coring `value` onto crdt (above);
adding a `none` member to `RetentionPolicy` (additive enum growth).

**Decisions that must be made before atom/SWMR `v1` is frozen:**

1. SWMR reset-epoch durability (plan 1.1 — already mandated; the current
   draft's sequence-only reset detection is the named defect).
2. **Atom writer binding (F5-F17):** either add `writer_id` to `AtomReplace`
   (wire + corpus change — cheap only while `v1` is uncommitted) or record
   in the contract that atom's `writers="single"` is adapter-enforced.
   Recommendation: record adapter-enforced for v1 (razel/presence producers
   are node-local; swmr needed enforcement because Datascad's requirement
   named it), and note the additive path.
3. Whether `snapshot_delta`'s profile knob (`reset_policy`) is a
   construction knob of `SwmrNode` v1 or a v2 addition — deciding it now
   costs a field name; deferring risks the profile forking the engine later
   (D28's warning).

**Terms whose current semantics are too incomplete to classify safely:**
`message` (nothing defines it — hence rejected rather than mapped);
`window` as a *delivery* concept (rejected pending s-window); the `sync`
slot of `crdt` (engine metadata vs bindable payload — Phase 7.1, F5-F18).

## 16. Decision-ready summary

**Model (one paragraph).** One canonical registry (Taut `SHAPES`) classifies
every public name as engine shape, profile, or interaction kind, with the
engine core and capability metadata machine-readable in the row; schema
authors keep declaring a single flat `shape="<name>"`; profiles are stable
public names resolving to a shared core plus fixed knobs; everything not in
the catalogue fails closed at declaration and dispatch.

**Canonical engines:** `value`, `atom`, `log`, `stream` (Phase 5), `swmr`,
`crdt` (Phase 7).
**Canonical profiles:** `snapshot_delta` (= swmr, `reset_policy=expire`),
`text_crdt` (= crdt, text payload).
**Interaction kinds:** `unary` (Taut); `exchange` (Glade surface vocabulary,
not a Taut shape).
**Rejected/unsupported (fail closed, wire values reserved):** `message`,
`window`.
**Aliases:** none created; `windowed` retention word rejected and the one
live use fixed.

**First three migration actions:** (1) add `value` + classification metadata
to `taut/src/taut/ir/shapes.py` and regenerate IR; (2) land Glial's explicit
`{value, log}` adapter registry with typed unsupported-shape errors and
negative tests (Step 0.3), including the TS/Rust client `fold()` sites;
(3) add declaration-time validation to glade-decl/appdecl (reject
`message`/`window`, enforce the shape×retention legality table, fix
`grazel-app.glade`'s `windowed`).

**Most important unresolved decision:** whether atom gains wire-level writer
binding (`writer_id`) before its uncommitted `v1` corpus freezes — the last
cheap moment to decide it (F5-F17).
