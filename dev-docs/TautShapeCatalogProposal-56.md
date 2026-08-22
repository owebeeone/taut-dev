# Taut Shape Catalogue Proposal — 56

## 1. Analysis snapshot

This proposal is the independent catalogue review assigned to agent **56**. The assigned output suffix is `56`; the collision check found `dev-docs/TautShapeCatalogProposal-56.md` absent before writing. No other `TautShapeCatalogProposal-*.md` was read. All statements below use one of three labels:

- **Observed** — directly represented by code, executable corpus, tests, or a live consumer.
- **Inferred** — the best explanation of observed code, but not yet a frozen contract.
- **Proposed** — the recommendation in this document.

The analysis was made against the following checkout snapshot. Dirtiness matters because the Atom and SWMR work is materially ahead of the committed `taut-shape` revision.

| Checkout/member | Revision | State relevant to this review |
|---|---:|---|
| `taut-dev` root | `51bf25351e6e` | Dirty only through the untracked prompt and implementation-plan inputs at snapshot time |
| `taut` | `f00841966663` | Clean |
| `taut-shape` | `389c867010a7` | Dirty: 8 tracked edits plus untracked Atom/SWMR schemas, corpora, scripts, and review notes |
| `taut-shape-rs` | `7e5045739148` | Dirty: 6 tracked Log/API edits |
| `taut-shape-ts` | `b1152457ac03` | Dirty: 4 tracked Log edits |
| `taut-shape-py` | `7e7d5a7fc276` | Dirty: 7 tracked Log/package edits |
| `glade-wz` root | `82e09c7635f8` | One unrelated workspace/member change; relevant members below were clean |
| `glade-decl` | `ccdae14a544d` | Clean |
| `glade` | `61617d57b237` | Clean |
| `glial` | `b3ee6658b76c` | Clean |
| `glade-gwz` | `e53c87dddb8f` | Clean |
| `glade-chat` | `9238d21f6a36` | Clean |
| `grazel` | `cbb19baa4746` | Clean |
| `gryth-dev` root | `49987a453ad7f003ea93598e674c003d19878979` | Clean |

The evidence hierarchy used here is: executable cross-language corpus and live end-to-end use first; implemented single-language engine second; checked-in schema/validator third; plan or prose last. The working implementation plan explicitly calls its catalogue an intent, not a ratified contract, and warns against freezing profiles before their semantics exist (`dev-docs/TautShapeImplementationPlan.md:53-90,586-588`).

## 2. Executive recommendation

Adopt **Candidate C: a validated composite/profile model**.

The canonical declaration has two independent top-level concepts:

1. `interaction`: `request_response`, `one_way`, `subscription`, or `duplex`.
2. `delivery`: absent for stateless interactions, or a named, versioned profile: `value`, `atom`, `log`, `stream`, `swmr`, `snapshot_delta`, `crdt`, or `text_crdt`.

Named profiles expand into a closed semantic descriptor covering writer cardinality, payload unit, ordering, retention, reader position, overflow, lifecycle, recovery, merge, and identity. Authors get concise, familiar names; validators and engines get explicit dimensions. Profile parameters are allowed only where the profile contract says they are allowed. There is no arbitrary mix-and-match escape hatch in the portable IR.

The existing names should be classified as follows:

- `unary`, `message`, and `exchange` are **interaction compatibility spellings**, not delivery engines.
- `value`, `atom`, `log`, `stream`, `swmr`, and `crdt` are **canonical delivery profiles with distinct engine contracts**.
- `snapshot_delta` is a **named compatibility profile over the SWMR snapshot/delta core**, differing in recovery: expiry/out-of-band refresh rather than an in-band `reset` event.
- `text_crdt` is a **specialized profile over the CRDT envelope/core**, because text identity and editing operations are not just a field-level merge option.
- `window` is a **view/projection decorator**, not a delivery shape. The live `windowed` token is a retention spelling that also must be normalized, not another shape.

This model should replace Taut’s current “shape is the sole discriminator” rule. Today the registry appears rich, but the model and generated clients consume only the binary `once` versus `stream` distinction (`taut/src/taut/ir/model.py:81-115`; `taut/src/taut/gen/scaffold.py:102-119,179-199,259-272,409-415`). A larger flat list would therefore preserve the wrong abstraction and leave invalid combinations undetectable.

The immediate execution rule is fail closed: until a profile has a schema, versioned corpus, reference engine, and adapter conformance result, it may be declared for schema-generation experiments but must not silently route through another engine. Glial’s current `shape === "log" ? log : value` behavior is the concrete anti-pattern to remove (`../glade-wz/glial/src/instance.ts:71-79,155-199`; `../glade-wz/glade/client-rs/src/session.rs:15-23`).

## 3. Evidence and current catalogues

### Taut’s authoritative catalogue

**Observed.** `taut/src/taut/ir/shapes.py` calls itself the sole discriminator and publishes seven names: `unary`, `atom`, `log`, `stream`, `swmr`, `snapshot_delta`, and `crdt`. Its records already mix payload, retention, initiation, writers, events, and delivery (`taut/src/taut/ir/shapes.py:1-18,27-56`). `value`, `message`, `exchange`, `window`, and `text_crdt` are absent.

Validation checks that a name exists and that output slots match the registry; it does not reject contradictory retention, interaction, writer, merge, or recovery combinations because those dimensions are not represented in the IR (`taut/src/taut/ir/validate.py:93-128`). Compatibility treats any shape-name change as breaking (`taut/src/taut/ir/compat.py:123-145`). The four client generators choose only between `call` and `subscribe`, so neither fire-and-forget nor duplex exchange has a generated API (`taut/src/taut/gen/scaffold.py:102-119,179-199,259-272,409-415`).

Taut’s own IR demonstrates the intended richer surface: GripLab declares Atom presence, Log chat, SWMR file state, ephemeral Stream terminal output, and CRDT sync (`taut/ir/griplab.taut.py:84-118,142-150`); Razel declares a latest-state Atom (`taut/ir/razel.taut.py:96-110`). These are schema declarations, not evidence that corresponding portable engines exist.

### `taut-shape` contract and implementation reality

**Observed.** The architecture document explicitly says Taut currently reduces shape to `is_streaming` and leaves delivery mechanics unspecified (`taut-shape/dev-docs/TautShapeArchitecture.md:23-39`). The current contract work has four concrete IR families: Log, Value, Atom, and SWMR. Regeneration enumerates exactly those four (`taut-shape/ir/regen.py:37-43`). Their maturity is not equal:

| Profile | Schema/IR | Corpus gate | Reference/runtime engine | Cross-language evidence |
|---|---|---|---|---|
| `log` | Present | 25-script oracle | Rust, TypeScript, Python engines | Real 3×3 writer/reader matrix; all three public packages expose Log only (`taut-shape/dev-docs/TautShapeOracle.md:113-185,425-471`) |
| `value` | Present | 11 vectors | Handwritten Glial TypeScript fold/session path | Glial local/in-process tests; no `taut-shape-*` engine (`taut-shape/dev-docs/TautShapeOracle.md:187-217`; `taut-shape/dev-docs/TautShapeGladeConsolidation.md:20-70,133-177`) |
| `atom` | Present in the dirty working tree | 28-script v1 corpus | Generator/reference semantics only | No per-language engine (`taut-shape/corpus/README.md:41-72`) |
| `swmr` | Present in the dirty working tree | 32-script v1 corpus | Generator/reference semantics only | No per-language engine (`taut-shape/corpus/README.md:74-117`) |
| `stream` | Roadmap design | None | None | None; overflow policy remains open (`taut-shape/dev-docs/TautShapeRoadmap.md:101-157,488-553`) |
| `snapshot_delta` | Taut registry and plan only | None | Intended SWMR-core profile | None |
| `crdt` | Taut schema sketch | No delivery corpus | Partial field-level reference model | No portable delivery engine (`taut/dev-docs/TautCrdt.md:12-23,37-70`) |
| `text_crdt` | Consolidation plan only | None | None | None (`taut-shape/dev-docs/TautShapeGladeConsolidation.md:179-189`) |

The public package surfaces corroborate that distinction: Rust re-exports only Log, TypeScript exports only Log types and `LogNode`, and Python exports only `LogNode`/`StopWhen` (`taut-shape-rs/crates/taut-shape/src/lib.rs:53-67`; `taut-shape-ts/src/index.ts:1-20`; `taut-shape-py/src/taut_shape/__init__.py:1-13`). Calling Atom or SWMR “implemented” would confuse a strong schema/corpus gate with a shipped engine.

### Glade and Glial’s catalogue

**Observed.** `glade-decl` defines six names: `value`, `log`, `message`, `stream`, `exchange`, and `window`, plus an independent retention enum `latest`, `from_cursor`, and `ttl` (`../glade-wz/glade-decl/ir/glade_decl.taut.py:47-51,70-102`). The declaration corpus exercises all six names, including semantically suspicious combinations such as `message + from_cursor`, `window + latest`, and `exchange + latest`; that proves encoding compatibility, not delivery behavior (`../glade-wz/glade-decl/corpus/build.py:77-111`).

Only Value and a subset of Log are folded in Glial. The local Value fold conforms to the 11-vector LWW corpus, while Log covers only immediate append/read behavior (`../glade-wz/glial/test/oracle.test.ts:1-9,65-138`; `../glade-wz/glial/dev-docs/DecisionLog.md:8-25`). Both Glial and the Glade TypeScript/Rust sessions send every non-Log name through Value behavior, so `message`, `stream`, `exchange`, and `window` do not have honest generic runtime semantics (`../glade-wz/glial/src/instance.ts:71-79,155-199`; `../glade-wz/glade/client-ts/src/session.ts:61-65`; `../glade-wz/glade/client-rs/src/session.rs:15-23`).

Glade Exchange is nevertheless real—but at a different layer. The node routes a directed request to a declared provider and returns a correlated response; it is never folded or cached (`../glade-wz/glade/node/src/exchange.rs:1-14,60-84`). `glade-gwz` is a live supplier and has end-to-end integration tests using that exchange, while long operation output is a separate Log surface (`../glade-wz/glade-gwz/src/supplier.rs:76-113,175`; `../glade-wz/glade-gwz/tests/integration.rs:167-173`). This is strong evidence that Exchange is an interaction, not a state shape.

The live Grazel app uses only `value` and `log` bindings and declares `gwz.ops` as a service, not as a binding shape. It also introduces `windowed` as a retention token for `term.log` (`../glade-wz/glade/apps/grazel-app.glade:19-39`). Separately, the demo manifest assigns `from_cursor` even to Value surfaces (`../glade-wz/glade/demo/src/manifest.ts:22-47`). These live declarations show why retention must be profile-validated instead of independently enumerable.

### Datascad, Gryth, and other consumers

**Observed.** Datascad’s RL harness is a fixture adapter for Atom and SWMR only. It pins five schema/corpus files and explicitly does not provide a runtime engine (`../datascad/rl/harness/TAUT_ADAPTER.md:1-17`). Its mapping and tests are valuable consumers of field identity, reset, and sequence semantics, but its `TAUT_PIN.json` points at a base commit plus uncommitted file content, so it is not evidence of a released portable contract (`../datascad/rl/harness/TAUT_PIN.json:2-10,12-44`). It explicitly skips Log and Window (`../datascad/rl/harness/TAUT_ADAPTER.md:223-252`).

Gryth is earlier still. Its current UI depends on Grip packages, not Glade/Glial/`taut-shape`; `WorkspaceNameTap` is a local `AtomValueTap` initialized to `mock-workspace` (`../gryth-dev/gryth-ui/package.json:13-25`; `../gryth-dev/gryth-ui/src/taps.ts:1-23`). Grip’s `AtomValueTap` is a local reactive container with get/set/update and notifications; remote echo control belongs to a future binder, not the tap (`../glial-dev/grip-core/src/core/atom_tap.ts:44-71,97-170`). The Gryth proposal correctly describes Glade attachment as not yet present and its surfaces as mock atoms (`../gryth-dev/dev-docs/GrythDemoProposal.md:184-196`). Therefore Grip “Atom” must not be counted as a Taut Atom engine.

Other live evidence is narrow but useful: `glade-chat` serves Value/Log shares, and `glade-gwz` serves Exchange plus Log output. No additional implemented delivery-shape name was found. `windowed` is the only additional catalogue-like spelling found in a loaded app declaration, and it is a retention policy, not a shape.

## 4. Semantic decomposition

The following tables describe the **current best-supported meaning**, not the recommendation. `O` means observed, `I` inferred from names/plans, and `—` means the current catalogue does not define the axis. “Core” distinguishes an actual portable engine from a schema, adapter, or live mechanism.

### Interaction, initiation, cardinality, and payload

| Current name | Interaction | Initiation | Producer cardinality | Consumer cardinality | Payload unit |
|---|---|---|---|---|---|
| `unary` | O request/response | O caller pull | O one callee per call | O many independent callers | O one response value |
| `value` | O immediate read plus write op; Glial also invalidates subscribers | O pull read / push write | O many attributed writers | O many replicas/readers | O whole value and LWW set op |
| `atom` | O read/subscribe latest state | O pull or push | O single source intent | O many stream readers | O whole replacement value |
| `log` | O cursor read/subscription plus append | O pull or push | I one source role; Glade fold accepts many origins | O many readers | O record/batch |
| `message` | I one-way notification | I sender push | — | — | I one message |
| `stream` | I live subscription | I source push | I one source | I many subscribers | I event/chunk |
| `exchange` | O directed correlated request/response in Glade | O requester push | O one attached provider per route | O many requesters | O request and response frames |
| `window` | I view/projection, not an interaction | I base-source dependent | I base-source dependent | I base-source dependent | I materialized window or window update |
| `swmr` | O state subscription | O producer push / reader pull | O exactly one bound writer | O many readers | O snapshot, delta, or reset |
| `snapshot_delta` | I state subscription | I producer push | I single writer | I many readers | O registry says snapshot/delta; reset omitted by profile intent |
| `crdt` | O/I duplex replica sync | O/I peer push and pull | O/I many writers/replicas | O/I many peers | O ops plus state/sync |
| `text_crdt` | I duplex collaborative editing | I peer push and pull | I many writers | I many peers | I stable-position text ops and sync |
| `windowed` | O retention token on a Log binding, not an interaction | I base Log behavior | I base-dependent | I base-dependent | I records inside a retention bound |

### Ordering, history, reader position, pressure, and lifecycle

| Current name | Ordering | Retention/history | Reader position | Slow-consumer behavior | Lifecycle |
|---|---|---|---|---|---|
| `unary` | O none beyond one call | O none | O none | O not applicable | O completes once or errors |
| `value` | O winner total order `(lamport, origin)`; dedupe by `(origin, seq)` | O current materialization plus reconstructible op set | O no consumer cursor in Value contract | O no held-reader contract | O immediate reads; no stream lifecycle |
| `atom` | O generation plus monotonic version | O latest only | O version | O coalesces to latest replacement | O holds, timers, supersede, seal, close, fail |
| `log` | O scalar sequence in `taut-shape`; Glade interleaves `(lamport, origin, seq)` | O retained, possibly bounded record history | O scalar cursor | O batches, holds, or expires below floor | O sessions, timers, supersede, seal, close, fail |
| `message` | — | — | — | — | — |
| `stream` | I arrival order | O/I none | O/I none | O undecided: drop, coalesce, or buffer | I terminal behavior planned, not contracted |
| `exchange` | O correlation-local only | O none in exchange layer | O correlation/session, not replay cursor | O transport timeout/backpressure, not shape-defined | O one exchange completes or errors |
| `window` | I base ordering | I bounded projection | I base cursor plus window parameters | I recompute/coalesce likely | — |
| `swmr` | O generation plus scalar delta sequence | O latest snapshot plus bounded reconstructible deltas | O `(generation, seq)` or absent | O in-band reset when reader falls behind | O holds, timers, supersede, seal, close, fail |
| `snapshot_delta` | I generation plus scalar delta sequence | I latest snapshot plus bounded deltas | I `(generation, seq)` | I expiry when recovery is impossible | I SWMR-core lifecycle, not separately contracted |
| `crdt` | O/I per-origin sequence plus causal/version-vector relation | O/I reconstructible ops/state with convergence-safe compaction | O/I version vector | I sync missing state/ops; policy not frozen | — |
| `text_crdt` | I causal plus stable text-position rules | I reconstructible document/ops | I version vector/state vector | I state/update sync | — |
| `windowed` | I base Log ordering | O bounded retention intent, exact bound absent | I base Log cursor | I expires or truncates old records | I base Log lifecycle |

### Recovery, merge, identity, core, and consumers

| Current name | Recovery behavior | Merge semantics | Identity/addressing | Existing engine core | Actual consumers |
|---|---|---|---|---|---|
| `unary` | O caller/transport retry outside shape | O none | O service/method; call identity transport-owned | O no delivery core; generated call path | Taut IR, validators, generated clients |
| `value` | O replay/fold attributed ops or read materialized value | O multiwriter LWW | O value/surface id, origin, seq | O Glial TypeScript fold; no portable package engine | Glial/Glade demo, Grazel/Gryth plans, Value corpus |
| `atom` | O read latest; generation prevents stale reuse | O replacement, not attributed LWW | O atom/stream id, generation, version | O schema + oracle generator only | Taut GripLab/Razel declarations; Datascad fixtures |
| `log` | O replay from cursor; expiry below floor | O append; application fold optional | O log id, stream id, cursor | O portable Rust/TS/Python engines | 3×3 matrix, Glial subset, Glade chat/activity/output |
| `message` | — | — | O declaration has Glade surface address only | O none | Glade declaration corpus only |
| `stream` | O/I no replay | O none | I stream/session id | O none | Taut terminal declaration; Glade wire/declaration only |
| `exchange` | O retry is application/transport policy | O none | O share, glade id, provider route, correlation | O real Glade routing/service mechanism, not `taut-shape` | `glade-gwz`, Grazel and demo E2E paths |
| `window` | I refresh/recompute base view | I application projection | I base address plus window key/range | O none | Glade declaration corpus only; roadmap prose |
| `swmr` | O in-band reset with replacement snapshot | O sequential delta application by one writer | O stream, writer, generation, seq | O schema + oracle generator only | Datascad fixture adapter; Taut declaration |
| `snapshot_delta` | I expire/out-of-band refresh | I sequential delta application | I SWMR identity | O no independent core | Taut registry/plan only |
| `crdt` | O/I exchange missing ops or state | O field LWW/counter sketch; generic merge slot intended | O doc, actor/replica, per-origin seq/vector | O partial reference model; no delivery engine | Taut schema declaration only |
| `text_crdt` | I state-vector/update sync | I text-specific convergence | I document, replica, stable item ids | O none | Planned only |
| `windowed` | I cursor expiry then refresh | O no merge of its own | I base Log address | O no distinct core | Loaded Grazel app retention token |

Three conclusions follow from the decomposition:

1. Names that share storage words do not necessarily share behavior: Value and Atom are both “latest values,” yet attribution, writer count, ordering, held reads, lifecycle, and recovery differ.
2. Names that share transport direction do not necessarily share state: Exchange and CRDT both need bidirectional traffic, yet only CRDT owns convergence and replica recovery.
3. The engine boundary is narrower than the public profile boundary: SWMR and `snapshot_delta` can share a core, and CRDT and `text_crdt` can share an envelope/core, while retaining profile-level validation and generated types.

## 5. Overlap findings

| ID | Names/layers | Relationship | Evidence | Consequence | Proposal implication |
|---|---|---|---|---|---|
| `56-F01` | `unary` vs `message` | Different interactions: response-bearing call vs one-way send; neither is retained state | Taut generators expose call/subscribe only, while Glade has a declaration-only Message name (`taut/src/taut/gen/scaffold.py:102-119`; `../glade-wz/glade-decl/ir/glade_decl.taut.py:47-51`) | Treating either as an engine invents retention/lifecycle questions that do not apply | Move both to `interaction`; map legacy `unary` automatically and map `message` only when no response is declared |
| `56-F02` | `value` vs `atom` | Same broad “latest” intuition, different machines | Value is attributed multiwriter LWW with immediate reads; Atom is a single-source versioned mailbox with holds and terminal lifecycle (`taut-shape/ir/shape_value.taut.py:1-42`; `taut-shape/ir/shape_atom.taut.py:1-51,130-190`) | Substituting one changes conflict resolution and reader behavior | Keep distinct named profiles and cores; share only low-level storage/envelope utilities |
| `56-F03` | `atom` vs SWMR snapshot | A SWMR snapshot is not an Atom | SWMR adds writer identity, generation, delta sequence, retention floor, and reset (`taut-shape/ir/shape_swmr.taut.py:29-85,147-220`) | Calling a snapshot “latest state” loses the recovery proof | Atom remains whole-state replacement; SWMR remains reconstructible snapshot-plus-delta |
| `56-F04` | `log` vs `stream` | Both emit sequences; only Log promises replay/cursors | Stream roadmap says live-only and leaves overflow open (`taut-shape/dev-docs/TautShapeRoadmap.md:101-157`) | A fallback from Stream to Log silently changes resource use and late-subscriber behavior | Separate profiles; they may share a session shell, never a semantic fallback |
| `56-F05` | `log` vs `message` | Log is delivery/history; Message is interaction intent | Glade’s corpus can encode `message + from_cursor`, but no Message engine consumes it (`../glade-wz/glade-decl/corpus/build.py:77-111`) | Flat enums admit nonsensical combinations | `one_way` may target no delivery or an explicitly named delivery profile; retention comes from the profile |
| `56-F06` | `log` vs `window`/`windowed` | Window is a projection or retention bound over a base, not a base state machine | Consolidation calls Window a planned windowed projection; the live app uses `windowed` as Log retention (`taut-shape/dev-docs/TautShapeGladeConsolidation.md:179-189`; `../glade-wz/glade/apps/grazel-app.glade:19-25`) | A standalone Window cannot determine ordering, cursor, writer, or recovery semantics | Replace `shape=window` with `view.window(...)`; normalize `windowed` into bounded Log retention |
| `56-F07` | `swmr` vs `snapshot_delta` | Same core, recovery-policy profiles | The implementation plan proposes `snapshot_delta` as a profile; SWMR’s corpus specifies in-band reset (`dev-docs/TautShapeImplementationPlan.md:64-79`; `taut-shape/dev-docs/AtomSwmrNotes.md:126-177`) | Two independent engines would duplicate nearly all protocol and corpus work | One snapshot/delta core; keep both named profiles until callers migrate, with reset vs expiry validated |
| `56-F08` | `crdt` vs `text_crdt` | Text is a specialization, not a synonym | Generic sketch supports field LWW/counter, while text needs stable-position text operations (`taut/dev-docs/TautCrdt.md:12-23`; `taut-shape/dev-docs/TautShapeGladeConsolidation.md:179-189`) | Pretending generic fields cover text hides identity and convergence requirements | One CRDT envelope/core interface, separate versioned `text_crdt` profile and corpus |
| `56-F09` | `exchange` vs CRDT sync | Shared duplex transport, different semantics | Glade Exchange is directed/correlated and never folded; CRDT sync carries state/ops and merge (`../glade-wz/glade/node/src/exchange.rs:1-14`; `taut/ir/griplab.taut.py:120-150`) | Calling CRDT “exchange” loses convergence; calling Exchange “CRDT” invents state | `duplex` interaction is reusable; `delivery=None` for generic exchange, `delivery=crdt` for replica sync |
| `56-F10` | Glial non-Log fallback | Accidental implementation overlap, not semantics | Every non-Log declaration becomes Value in Glial and both clients (`../glade-wz/glial/src/instance.ts:71-79`; `../glade-wz/glade/client-ts/src/session.ts:61-65`) | Unsupported shapes appear to work while corrupting their contract | Exhaustive adapters must reject unsupported profiles before subscription or mutation |
| `56-F11` | Retention vs shape | Current catalogues allow contradictory pairs | Glade’s typed demo uses `from_cursor` on Value, and declaration defaults can produce `latest` on Log (`../glade-wz/glade/demo/src/manifest.ts:22-47`; `../glade-wz/glial/src/manifest.ts:41-75`) | Runtime behavior depends on undocumented adapter convention | Profiles own allowed retention families; validation rejects all other pairs |
| `56-F12` | Grip Atom vs Taut Atom | Naming collision across application and delivery layers | `AtomValueTap` is local state and explicitly delegates remote echo control to a binder (`../glial-dev/grip-core/src/core/atom_tap.ts:44-71,154-170`) | Counting it as an engine overstates implementation maturity and couples UI terminology to wire semantics | Application containers stay outside the catalogue; adapters explicitly bind a tap to a delivery profile |

## 6. Use-case tests of current model

| Required use case | Best current declaration/path | Current verdict |
|---|---|---|
| 1. Unary request/response | Taut method with default `shape="unary"` | **Works**, but only because Unary conflates interaction with shape; it needs no delivery engine |
| 2. Fire-and-forget notification | Glade `shape="message"` or a Taut unary returning an acknowledgement | **Fails portably**: Message has no behavior and generated Taut clients have no send-only API |
| 3. Single-writer status/latest value | Taut `shape="atom"` | **Expressible, not executable portably**: schema and 28-vector oracle exist, language engines do not |
| 4. Glade attributed multiwriter LWW value | Glade `shape="value"`, Glial `ValueRegister` | **Works in the Glade/Glial TypeScript path**, but Value is absent from Taut’s registry and retention combinations are unchecked |
| 5. Durable chat/history with cursor resume | `shape="log"`, `from_cursor` | **Works best**: this is the only cross-language engine/matrix-backed profile; Glial covers a smaller immediate subset |
| 6. Ephemeral terminal output with loss/drop semantics | Taut `shape="stream"` | **Fails contractually**: no engine/corpus and drop/coalesce/buffer is unresolved |
| 7. Datascad-style single-writer snapshot plus delta | Taut `shape="swmr"`; Datascad fixture pin | **Schema/corpus works**, but Datascad is read-only fixture integration and no portable runtime engine exists |
| 8. Bounded time-window materialized view | Glade `shape="window"` or Log with `windowed` retention | **Ambiguous**: one spelling suggests a shape, the live spelling suggests retention, and neither specifies projection recovery |
| 9. Generic multiwriter CRDT state | Taut `shape="crdt"` | **Schema sketch only**: merge fields exist, but delivery identity, lifecycle, corpus, compaction, and engines are incomplete |
| 10. Collaborative text editing | Planned `text_crdt` | **Not currently expressible in authoritative IR** and has no corpus or engine |
| 11. Generic bidirectional request/response exchange | Glade service/Exchange mechanism | **Works in Glade**, but it is outside the shape fold and Taut cannot generate the duplex API |

The current model therefore passes only Unary, Glade Value, Log, and Glade Exchange in their specific stacks. It partially represents Atom and SWMR, and it fails to give portable, fail-closed meaning to Message, Stream, Window, CRDT, and Text CRDT.

## 7. Candidate A — compatibility-first flat catalogue

Candidate A keeps one public `shape` field and expands it to the union of all current names:

```text
unary | value | atom | log | message | stream | exchange |
window | swmr | snapshot_delta | crdt | text_crdt
```

Each registry row would gain implementation metadata—output slots, default retention, engine package, corpus version, and supported interactions—without changing the authoring concept. `windowed` would remain a retention spelling. Adapters would still switch on one name, but would be required to fail closed for unimplemented rows.

This is credible because it is the smallest change to Taut’s current sole-discriminator design, preserves every declaration spelling, and fits `compat.py`’s existing assumption that shape-name changes are breaking. It also gives Step 0.2 an obvious deliverable: generate one union registry and publish one table.

Its weakness is structural. The list contains three interactions (`unary`, `message`, `exchange`), at least six delivery profiles, one projection (`window`), and two specializations/profiles (`snapshot_delta`, `text_crdt`). The registry can document category differences, but the type system still says they are peers. It cannot naturally express a one-way append, a duplex CRDT sync, or a subscription over a windowed SWMR view without either composite names or hidden conventions. Every future orthogonal feature creates another cross-product name.

Candidate A is acceptable only as a short-lived compatibility facade. It is not an adequate canonical model.

## 8. Candidate B — minimal orthogonal engine catalogue

Candidate B removes all public shape names and exposes only primitive engine cores plus independent axes:

```text
engine = none | lww_register | latest_mailbox | cursor_feed |
         live_feed | snapshot_delta | replica_ops

interaction = request_response | one_way | subscription | duplex
writers = one | attributed_many
retention = none | latest | cursor_bounded | snapshot_plus_deltas | reconstructible
ordering = none | scalar | total_lww | per_origin_causal
recovery = retry | latest | replay | reset | expire | state_sync
merge = none | replace | lww | sequential_delta | plugin
```

Every declaration states or receives defaults for all relevant axes. `atom`, for example, becomes `latest_mailbox + one writer + latest retention + scalar version + replace + latest recovery`; `swmr` becomes `snapshot_delta + one writer + snapshot_plus_deltas + scalar sequence + reset`.

This is the most semantically orthogonal candidate. It makes engine reuse obvious, can express new combinations without new names, and lets code generation derive APIs from `interaction` rather than from a misleading state name. It is also the easiest internal representation to compare, validate, and serialize.

Its weakness is public combinatorial freedom. Many combinations are meaningless or have no corpus: multiwriter Atom, cursor-retained Stream, LWW Log, or reset-recovery Value. Preventing those combinations recreates named profiles as a validator rule set. Without profiles, application manifests become verbose and cross-language packages must agree on many more enum values at once. Candidate B is therefore the right **normalized internal descriptor**, but the wrong direct authoring surface for the current maturity of the ecosystem.

## 9. Candidate C — validated composite/profile model

Candidate C combines B’s normalized internal descriptor with stable named profiles:

```text
Endpoint = Interaction × (DeliveryProfile | none) × optional View

Interaction = request_response | one_way | subscription | duplex
DeliveryProfile = value@1 | atom@1 | log@1 | stream@1 |
                  swmr@1 | snapshot_delta@1 | crdt@1 | text_crdt@1
View = none | window(parameters)
```

Every profile expands into the same orthogonal descriptor used by Candidate B, but authors may override only explicitly parameterized policy fields. For example, Log may accept a bounded retention policy and batch limit; Stream must choose an overflow policy; SWMR may choose the delta bound; the writer cardinality and recovery family remain immutable.

The registry contains three records rather than one flat enum:

1. An interaction registry that determines generated method shape and transport obligations.
2. A delivery-profile registry that determines engine/core, event slots, state semantics, allowed policies, and corpus gate.
3. A view registry whose input and output compatibility is validated against the base delivery profile.

Candidate C preserves application vocabulary while preventing category errors. It admits engine sharing without pretending profile semantics are identical: SWMR and `snapshot_delta` share the snapshot/delta core; CRDT and `text_crdt` share the replica envelope/core; Log and Stream may share mailbox/session infrastructure but not replay behavior. A canonical normalizer makes all defaults explicit in serialized IR, so language generators never need to reimplement defaults.

This candidate also supports staged maturity. A registry row has a status—`declared`, `corpus`, `reference`, `portable`—and an adapter declares the statuses/profiles it accepts. Status is not semantics and does not weaken validation: unsupported profiles are rejected rather than routed elsewhere.

## 10. Comparative scorecard

Scores are 1 (poor) through 5 (strong), equally weighted. “Compatibility” includes source spelling and practical migration, not preservation of accidental runtime fallback.

| Criterion | A: flat | B: orthogonal | C: profiles | Rationale for leading score |
|---|---:|---:|---:|---|
| Semantic orthogonality | 2 | 5 | 5 | B/C separate interaction, delivery, view, and policy |
| Backward compatibility | 5 | 2 | 4 | A preserves spellings; C provides deterministic legacy normalization |
| Runtime implementability | 3 | 4 | 5 | C maps each profile to a bounded core plus conformance gate |
| Fail-closed validation | 3 | 4 | 5 | C validates a closed profile expansion and adapter capability |
| Codegen/API clarity | 2 | 5 | 5 | B/C generate call/send/subscribe/duplex from interaction |
| Corpus/oracle strategy | 3 | 4 | 5 | C versions behavior by profile and separately tests shared cores |
| Cross-language tractability | 4 | 3 | 4 | A is small but ambiguous; C limits combinations while exposing normalized IR |
| Application ergonomics | 5 | 2 | 4 | A is concise; C stays concise with explicit interaction |
| Migration risk | 5 | 2 | 4 | C can dual-read legacy and canonical forms without silent fallback |
| Extension quality | 2 | 5 | 5 | B/C add axes/profiles without an uncontrolled cross-product |
| **Total / 50** | **34** | **36** | **46** | **Candidate C wins** |

Candidate B’s two-point lead over A is not decisive by itself; the important result is why C dominates both. It preserves the useful names from A while making B’s decomposition normative and machine-readable.

## 11. Recommended canonical catalogue

The canonical registry is the following. “Retain” means retain as a canonical profile name, not necessarily as a top-level `shape` field. All profile versions below start at `@1`; they advance independently when behavior, not just encoding, changes.

| Current name | Current category | Canonical disposition | Canonical mapping | Engine/core | Migration rule |
|---|---|---|---|---|---|
| `unary` | Interaction disguised as shape | Compatibility alias | `interaction=request_response`, `delivery=None` | None | Auto-normalize; canonical emitters stop writing `shape="unary"` |
| `value` | Delivery profile | **Retain `value@1`** | Attributed multiwriter whole-value LWW; immediate read/write semantics | `lww_register` | Glade declarations map directly; add to Taut delivery registry |
| `atom` | Delivery profile | **Retain `atom@1`** | Single-writer latest mailbox, generation/version, held reads and lifecycle | `latest_mailbox` | Existing Taut declarations map directly after interaction is made explicit |
| `log` | Delivery profile | **Retain `log@1`** | Cursor-retained ordered records with replay and lifecycle | `cursor_feed` | Existing declarations map directly; retention must normalize and validate |
| `message` | Interaction disguised as shape | Compatibility alias, then deprecate | `interaction=one_way`, normally `delivery=None` | None unless an explicit delivery profile is also declared | Auto-map only if there is no response slot; otherwise reject for human choice |
| `stream` | Delivery profile | **Retain `stream@1`** | Live-only events, no cursor/replay; explicit overflow | `live_feed` | Existing declarations require an explicit overflow policy before runtime use |
| `exchange` | Interaction/service mechanism | Compatibility alias | `interaction=duplex` with correlated request/response, `delivery=None` | Transport/router mechanism | Glade services map directly; binding declarations using Exchange are rejected/migrated manually |
| `window` | View/projection | Remove from delivery catalogue | `view=window(range/time/key...)` over an explicit base delivery | Application/view adapter | No automatic migration because current declarations do not identify the base or projection semantics |
| `swmr` | Delivery profile | **Retain `swmr@1`** | Single writer, snapshot + bounded deltas, in-band reset recovery | `snapshot_delta` | Existing Taut/Datascad schemas map directly once committed and versioned |
| `snapshot_delta` | Delivery profile alias over shared core | **Retain named `snapshot_delta@1` profile** | Same core and ordering as SWMR, but unrecoverable cursors expire for out-of-band refresh | `snapshot_delta` | Preserve for compatibility; recommend `swmr` for new in-band repair consumers |
| `crdt` | Delivery profile/family | **Retain `crdt@1`** | Multiwriter replica ops/state sync with explicit merge plugin and vector position | `replica_ops` | Existing sketch remains `declared` until identity, compaction, corpus, and engine gate are complete |
| `text_crdt` | Specialized delivery profile | **Retain `text_crdt@1`** | CRDT replica envelope with stable text identity and text update/state-vector contract | `replica_ops` plus text merge plugin | Add only with its own schema and convergence corpus; never silently map to generic field CRDT |
| `windowed` | Live retention spelling, not shape | Normalize and deprecate spelling | `retention=bounded(...)` on `log@1` | Base Log core | Migration must supply the missing bound from app policy; fail if it cannot be recovered |

The resulting canonical public catalogues are therefore:

```text
Interactions: request_response, one_way, subscription, duplex
Delivery profiles: value, atom, log, stream, swmr, snapshot_delta, crdt, text_crdt
Views: window
```

The normalized internal cores are `none`, `lww_register`, `latest_mailbox`, `cursor_feed`, `live_feed`, `snapshot_delta`, and `replica_ops`. Core names are implementation vocabulary and should not leak into ordinary application manifests.

## 12. Proposed declaration model and examples

### Canonical form

The following is semantic pseudo-IR; exact Python/JSON syntax belongs to Step 0.2. Canonical serialized IR always contains explicit `interaction`, `delivery`, and `operation` values even when the authoring DSL uses a convenience default.

```python
endpoint(
    "qualified.name",
    interaction=interaction("request_response"),
    delivery=None,                         # or delivery("log", operation="read", ...)
    view=None,                             # or window(...)
    params=[...],
    out={...},
)
```

The normalized `delivery` record is generated centrally, not independently by each language:

```text
profile + profile_version + operation
producer_cardinality + consumer_cardinality
payload_unit + event_slots + ordering
retention + reader_position + overflow
lifecycle + recovery + merge + identity
engine_core + corpus_gate
```

Defaults and constraints are deliberately narrow:

- Authoring default: omitted `interaction` means `request_response`; canonical IR emits it explicitly.
- Authoring default: omitted `delivery` means `None`. A `subscription` without a delivery profile is invalid; use `stream` for live-only events.
- `value@1`: attributed-many writers, LWW merge, immediate read, and latest materialization are fixed. Portable operations are `read` and `set`; a watch/invalidation operation needs an additional corpus before it becomes portable.
- `atom@1`: one bound writer, whole replacement, latest retention, generation/version position, and latest recovery are fixed. Operations are `read`, `replace`, and `watch`.
- `log@1`: record payload, scalar cursor, replay, and lifecycle are fixed. Operations are `append` and `read`; retention bounds are deployment parameters and may not change cursor semantics.
- `stream@1`: no replay or reader position is fixed. `overflow` is required—there is no cross-application default—and a lossy policy must specify whether a loss marker is emitted.
- `swmr@1`: one bound writer, snapshot/delta ordering, and in-band reset are fixed. A positive delta bound is required.
- `snapshot_delta@1`: shares SWMR core fields, but unrecoverable position produces expiry/out-of-band refresh instead of a reset event.
- `crdt@1`: attributed-many replicas and vector position are fixed; merge plugin, identity codec, and convergence-safe compaction policy are required.
- `text_crdt@1`: supplies a text-specific merge/identity profile; implementations must name a corpus-compatible codec, not merely claim “CRDT.”
- `window(...)` always names its base endpoint/profile, range semantics, materialization owner, and refresh/recovery behavior. It cannot stand alone.

The profile registry also enumerates permitted operation/interaction pairs. For example, `atom.watch + subscription`, `log.append + one_way`, and `crdt.sync + duplex` are valid; `atom.watch + request_response`, `stream.read + request_response`, and `value.set + subscription` are not. This is how the composite model stays closed rather than becoming Candidate B’s arbitrary cross-product.

### Eleven required declarations

1. **Unary request/response**

```python
endpoint("catalog.lookup",
    interaction=interaction("request_response"),
    delivery=None,
    params=[("key", STR)], out={"item": Item})
```

Generated API: `call/lookup(key) -> Item`; no shape engine, retention, cursor, or merge state is created.

2. **Fire-and-forget notification**

```python
endpoint("audit.notify",
    interaction=interaction("one_way"),
    delivery=None,
    params=[("event", AuditEvent)], out=None)
```

Generated API: `send/notify(event) -> void`. Transport acknowledgement, if any, is not exposed as an application response.

3. **Single-writer status/latest value**

```python
endpoint("provider.status.watch",
    interaction=interaction("subscription"),
    delivery=delivery("atom", version=1, operation="watch"),
    out={"value": ProviderStatus})
```

The paired producer uses the same address with `operation="replace"` and `interaction="one_way"`. Late readers receive the latest whole value; intermediate replacements may coalesce.

4. **Glade-style attributed multiwriter LWW value**

```python
endpoint("workspace.title.set",
    interaction=interaction("one_way"),
    delivery=delivery("value", version=1, operation="set"),
    params=[("value", STR), ("origin", Origin), ("seq", INT)])

endpoint("workspace.title.read",
    interaction=interaction("request_response"),
    delivery=delivery("value", version=1, operation="read"),
    out={"value": STR, "winner": LwwStamp})
```

The address binds both operations to one `lww_register`; `(lamport, origin)` selects the winner and `(origin, seq)` provides operation identity/deduplication. This is not Atom.

5. **Durable chat/history with cursor resume**

```python
endpoint("chat.messages.read",
    interaction=interaction("subscription"),
    delivery=delivery("log", version=1, operation="read",
                      retention=cursor_history(max_age="30d")),
    params=[("cursor", LogCursor)], out={"record": ChatMessage})
```

The paired append endpoint uses `operation="append"`. A cursor below the retained floor receives the profile’s explicit expiry result, never Value fallback.

6. **Ephemeral terminal output with loss/drop semantics**

```python
endpoint("terminal.output",
    interaction=interaction("subscription"),
    delivery=delivery("stream", version=1, operation="read",
                      overflow=drop_oldest(emit_loss_marker=True)),
    params=[("session_id", STR)], out={"chunk": BYTES, "loss": LossMarker})
```

There is no replay cursor. A slow consumer may lose chunks, and the declaration makes that visible rather than inheriting an undocumented global policy.

7. **Datascad-style single-writer snapshot plus delta**

```python
endpoint("dataset.state",
    interaction=interaction("subscription"),
    delivery=delivery("swmr", version=1, operation="read",
                      writer="trainer-1", max_deltas=1024),
    out={"snapshot": DatasetSnapshot, "delta": DatasetDelta, "reset": Reset})
```

The position is `(generation, seq)`. A reader behind the floor is repaired in band with `reset + snapshot`, matching the Datascad fixture semantics.

8. **Bounded time-window materialized view**

```python
endpoint("metrics.last_five_minutes",
    interaction=interaction("subscription"),
    delivery=delivery("swmr", version=1, operation="read",
                      writer="metrics-materializer", max_deltas=600),
    view=window(kind="event_time", range="5m", slide="1s",
                materialized_by="provider", late_events="recompute"),
    out={"snapshot": MetricWindow, "delta": MetricWindowDelta, "reset": Reset})
```

Window defines application projection; SWMR defines transport, position, retention, and repair. A raw bounded event history would instead be `log@1` plus bounded retention, not `shape="window"`.

9. **Generic multiwriter CRDT state**

```python
endpoint("board.sync",
    interaction=interaction("duplex"),
    delivery=delivery("crdt", version=1, operation="sync",
                      merge="board_fields@1", identity="actor_seq@1",
                      compaction="version_vector_safe@1"),
    out={"op": CrdtOp, "state": CrdtState, "version": VersionVector})
```

Generated peers expose local apply, remote merge, and state/op sync. The merge plugin is part of the contract and corpus key, not an application comment.

10. **Collaborative text editing**

```python
endpoint("document.text.sync",
    interaction=interaction("duplex"),
    delivery=delivery("text_crdt", version=1, operation="sync",
                      codec="stable_text_ops@1",
                      compaction="state_vector_safe@1"),
    out={"update": TextUpdate, "state_vector": TextStateVector})
```

The Text profile fixes stable item/position identity and convergence vectors. It may use the generic replica shell but requires its own adversarial convergence corpus.

11. **Generic bidirectional request/response exchange**

```python
endpoint("gwz.ops",
    interaction=interaction("duplex", correlation="request_response",
                            routing="directed_provider"),
    delivery=None,
    params=[("request", GwzRequest)], out={"response": GwzResponse})
```

Generated API: a duplex channel or correlated `exchange()` helper. It owns no fold, replay, merge, or retained state; streaming job output remains a separate Log/Stream endpoint.

### Code-generation consequence

| Interaction | Generated client floor | Delivery contribution |
|---|---|---|
| `request_response` | `call()` / typed future | Optional profile-specific read/control types |
| `one_way` | `send()` / no application result | Optional write/op validation |
| `subscription` | typed async iterator/stream plus cancel | Cursor, event union, terminal, recovery, and overflow types from profile |
| `duplex` | typed channel or correlated exchange helper | Replica op/state types when a CRDT profile is present |

The old `streams()` boolean may remain as a derived compatibility query, but no generator is allowed to use it as the sole API decision.

## 13. Engine, adapter, and application boundaries

### Taut owns declaration meaning

Taut owns interaction/profile/view registries, canonical default expansion, validation, compatibility reports, output-slot derivation, and language-neutral generated API shape. Unknown profile versions, invalid operation/interaction pairs, unsupported overrides, and adapter capability gaps are validation errors. Raw registry mutation (`register_shape`) should become a versioned extension API that must supply a descriptor, oracle identity, and capability key; an arbitrary name plus dictionary is insufficient (`taut/src/taut/ir/shapes.py:67-84`).

Taut does **not** define store internals, transport framing, application projection algorithms, or a CRDT vendor implementation.

### `taut-shape` owns delivery contracts

`taut-shape` owns each delivery profile’s exact messages, state transitions, identity rules, reference oracle, corpus, and engine-core protocol. It also owns shared session/mailbox primitives where reuse is behavior-preserving. The architecture already places delivery IR, runtime packages, and oracle at separate layers and keeps stores outside the core (`taut-shape/dev-docs/TautShapeArchitecture.md:60-85,183-225`). Candidate C formalizes that split.

A profile reaches these statuses in order:

1. `declared`: schema and semantic table exist.
2. `corpus`: deterministic positive and negative vectors exist.
3. `reference`: one reference engine passes the corpus.
4. `portable`: supported language engines pass same-language oracle tests and the required cross-language matrix.

Status is published metadata. It never authorizes a lower-status profile to borrow another profile’s engine.

### Adapters own translation, not semantics

Glade/Glial, Grip binders, Datascad harnesses, and transport libraries own address mapping, frame conversion, scheduling, persistence selection, and capability negotiation. An adapter publishes a closed set of `(profile, version, operation)` capabilities and rejects everything else before state mutation.

Glade retains HELLO/SUBSCRIBE/OPS/HEADS/EXCHANGE/CHANNEL, routing, sessions, store, and provider attachment. `taut-shape` retains fold/delivery behavior; this is already the intended consolidation boundary (`taut-shape/dev-docs/TautShapeGladeConsolidation.md:1-16`). Exchange stays a Glade interaction mechanism. Value and Log folds may be `taut-shape`-conformant without turning all Glade shapes into folds.

Glial must switch exhaustively on canonical delivery profile. Until more engines ship, its accepted set is `value@1` and the explicitly documented subset/full version of `log@1`; `message`, `stream`, `window`, `exchange`, Atom, SWMR, and CRDT are rejected. Provider Exchange continues through its dedicated path.

### Applications own domain projections and policy choices

Applications own payload codecs, domain merge plugins, window functions, loss tolerance, retention sizes/ages, authorization, UI containers, and provider selection. They must choose policy within a profile’s allowed parameter space. A Grip `AtomValueTap` may be bound to `value@1` or another suitable profile, but the local container name does not select wire semantics.

For Window specifically, the application/view provider owns event-time vs processing-time, range, slide, late-event treatment, aggregation, and materialization. The base delivery profile owns transport history and repair.

## 14. Migration plan and impact on Steps 0.2/0.3

This plan preserves the implementation plan’s evidence-first intent while changing Step 0.2 from “one larger shape enum” to “interaction + validated delivery profiles + views.” It should land before language packages or Glial add more shape switches; otherwise accidental compatibility becomes harder to remove.

### Phase 0 — ratify and inventory

1. Ratify the category split and the canonical table in Section 11.
2. Export every Taut and Glade declaration into an inventory containing old name, operation/role, response slots, retention, and actual adapter. Classify each as automatically normalizable, unsupported-but-honest, or human-decision-required.
3. Freeze no new runtime profile based only on prose. Atom/SWMR are corpus-gated but remain non-portable until engines exist; Stream/CRDT/Text remain earlier.

### Step 0.2 — Taut registry and documentation

Replace `SHAPES` as the sole discriminator with generated registries for `Interaction`, `DeliveryProfile`, and `View`. Keep a legacy parser that normalizes old `shape=` input into canonical fields, but have all serializers/code generators emit canonical v2 IR.

Required Step 0.2 outputs:

- A machine-readable profile descriptor containing every axis in Section 4, allowed operations/interactions, event slots, defaults, allowed policy parameters, core, maturity, and corpus version.
- An exhaustive legacy mapping table identical in substance to Section 11.
- Validator errors for unknown profile/version, invalid retention, invalid operation/interaction, missing required policy, and unsupported adapter capability.
- Compatibility reporting that distinguishes an interaction change, profile/version change, policy tightening, and view change instead of treating all as an opaque shape-name change.
- Generated client APIs for call, send, subscribe, and duplex; `streams()` becomes derived only.
- Golden IR fixtures for all eleven declarations in Section 12, including negative fixtures for every prohibited combination.

Taut impact: `ir/shapes.py`, `model.py`, DSL/JSON normalization, validator, compatibility analysis, documentation, and all four scaffold generators change together. Existing `shape="atom"`/`log`/`stream`/`swmr`/`snapshot_delta`/`crdt` sources remain readable through normalization. `value` becomes a first-class delivery profile. Legacy Unary remains the default authoring behavior for one compatibility cycle.

### Step 0.3 — Glade/Glial exhaustive integration

Glade declaration v1 remains readable, but its six-name Shape enum is normalized by category:

- `value` and `log` become delivery profiles.
- `message` becomes `one_way` only if its response/output contract is empty.
- `stream` becomes a delivery profile only with explicit overflow.
- `exchange` moves to the service/interaction declaration; an Exchange binding is rejected.
- `window` requires manual replacement with a base profile and View declaration.

Retention also needs one canonical vocabulary. Normalize `from_cursor` and `from-cursor` to `cursor_history`; migrate `windowed` to `bounded` only when the actual size/age bound is available; keep `latest`, `ttl`, and bounds only where the selected profile permits them. Value’s current `from_cursor` demo declarations must either document that the op log is an adapter transport concern while the delivery materialization remains latest, or move that transport policy out of the profile declaration. They must not silently redefine Value.

Glial’s `isLog ? LogBuffer : ValueRegister` branches become exhaustive profile dispatch. Unsupported profiles produce a typed error during manifest load/session bind. Tests must prove that each unsupported current enum name fails before any op is folded. The Value 11-vector corpus and the supported Log corpus remain hard gates; claiming full `log@1` requires all lifecycle/retention vectors, not just immediate append/read.

### `taut-shape` and language packages

Commit or deliberately discard the current dirty Atom/SWMR contract slice before versioning it; the catalogue must cite immutable schema and corpus hashes. Add one profile manifest generated from the same source Taut consumes. Implement shared core protocols only after profile behaviors are fixed.

Language packages should progress profile-by-profile:

1. Preserve and re-run the complete Log 3×3 matrix while current dirty Log changes are reconciled.
2. Add Value only if a portable engine is desired; otherwise advertise it as an adapter/reference implementation in Glial, not in all packages.
3. Implement Atom and SWMR reference engines against their corpora, then same-language tests, then cross-language matrices.
4. Do not add Stream, CRDT, or Text exports until their corpus gates exist.

Package capability metadata must say exactly which profile versions and operations are implemented. A package-wide version alone is not enough to infer behavior.

### Datascad pin

Do not rewrite Datascad’s current fixture pin in place while `taut-shape` is dirty. After Atom/SWMR schemas and corpora are committed, publish immutable profile/corpus versions and update `TAUT_PIN.json` in a dedicated Datascad change with regenerated hashes and the existing field/sequence/reset tests. Datascad remains classified as a fixture consumer until it uses a runtime engine; the pin must not be counted as Step 0.3 engine conformance.

### Gryth and Grip

No Gryth migration is needed for current runtime code because no Glade binder is attached. When the planned binding lands, each `ShareDecl` resolves explicitly to `value@1` or `log@1`; the local `AtomValueTap` remains an application container. The binder’s existing `shape !== "log"` whole-value fallback must become an exhaustive mapping, and future provider-matcher work remains orthogonal to delivery shape (`../gryth-dev/dev-docs/GrythDemoProposal.md:97-128,310-327`).

### Wire, corpus, and package version impact

- **Taut IR:** introduce schema version 2. Readers may accept v1 and normalize; canonical writers emit v2. Removing v1 input support is a later major compatibility event.
- **Glade declaration wire:** preserve existing numeric enum values; add a versioned canonical declaration message rather than renumbering Shape. Exchange frames remain unchanged. Unknown canonical profiles must be rejected during capability negotiation.
- **Profile schemas/corpora:** version per profile (`log@1`, `atom@1`, and so on). Any behavioral change to ordering, expiry/reset, lifecycle, merge, or identity requires a profile/corpus version change and new vectors.
- **Language packages:** an API-breaking move from generic call/subscribe or new event unions requires the appropriate package major bump; adding a gated profile without changing existing APIs may be minor. Capability manifests still govern interoperability.
- **Matrices:** matrix identity includes writer language/package version, reader language/package version, profile version, corpus version, and adapter version. “Package versions match” is not a substitute for that tuple.

## 15. Risks, falsification, and open decisions

### Principal risks and controls

| Risk | Why it matters | Control / falsification test |
|---|---|---|
| Profiles merely hide a new flat enum | The decomposition would be documentation-only | Serialize normalized descriptors and property-test that every profile axis is explicit and equal across languages |
| Shared cores leak semantics between profiles | SWMR/`snapshot_delta` or CRDT/Text could accidentally converge in name only | Run the same core against profile-specific negative vectors; an SWMR expired-cursor result without reset must fail, while the `snapshot_delta` profile expects it |
| Legacy normalization guesses wrong | `message`, `window`, and retention tokens are ambiguous | Inventory all declarations; permit auto-migration only where operation/output/base/bound are provable; otherwise emit a blocking diagnostic |
| Fail-closed changes reveal latent dependencies | Applications may currently rely on non-Log→Value fallback | Add telemetry/dry-run diagnostics first, then tests that every unsupported manifest fails before state mutation; migrate only identified users |
| Schema/corpus maturity is mistaken for engine maturity | Atom/SWMR could be advertised prematurely | Capability metadata derives from executable package conformance, never from file presence or Datascad pins |
| Explicit interactions expand generators substantially | Four client styles must remain consistent | Golden API tests for all four languages and all eleven Section 12 declarations |
| View remains underspecified | Window could re-enter the catalogue under another name | Require base endpoint, clock, range, slide, late-event policy, materializer, and recovery before a Window declaration validates |
| CRDT becomes a vendor escape hatch | “Plugin merge” without identity/corpus provides no interoperability | A CRDT profile cannot reach `corpus` status until deterministic identity, duplicate/equivocation handling, compaction, partition/rejoin, and convergence vectors exist |
| Retention vocabulary migration changes data availability | `latest`, `from_cursor`, `ttl`, and `windowed` currently mix engine and store policy | Generate before/after availability traces from each live Glade manifest and require an owner to approve any narrower result |
| Profile proliferation returns | Every application nuance could become a new profile | Add a profile only when an existing profile cannot express a semantic invariant and a distinct cross-language corpus is justified |

### Decisive falsification experiments

The recommendation should be rejected or revised if any of these experiments fails:

1. **Round-trip inventory:** every live Taut and Glade declaration must normalize to canonical IR and either round-trip behavior-preservingly or produce an explicit human-decision diagnostic. Silent lossy conversion falsifies the migration claim.
2. **Generator separation:** call, send, subscribe, and duplex declarations must generate observably different, type-correct APIs in Python, TypeScript, Rust, and Go without consulting legacy shape names. Failure falsifies interaction orthogonality.
3. **Fail-closed adapter:** feeding Glial each unsupported profile must fail before fold/store mutation. Any Value result from Atom, Stream, Exchange, Window, SWMR, or CRDT falsifies the adapter boundary.
4. **Shared-core profile separation:** one snapshot/delta core must pass both SWMR reset vectors and `snapshot_delta` expiry vectors through different profile configuration, with the wrong recovery event rejected. If the core requires two independent implementations, the proposed sharing is false; if profiles cannot distinguish outcomes, the profile split is false.
5. **Value/Atom non-substitutability:** replay adversarial multiwriter LWW operations and Atom lifecycle scripts through both profiles. If either profile accepts the other’s expected outputs, validation is too weak.
6. **Window composition:** implement the Section 12 time-window example over a base SWMR endpoint and a raw bounded Log alternative. If the view cannot declare deterministic recovery without becoming an engine itself, Window needs a stronger contract or a separate materialized-view engine.
7. **CRDT convergence:** at least three replicas with reorder, duplicates, partition/rejoin, compaction, and snapshot restore must converge byte-for-byte under the declared identity/merge codec. Until then CRDT remains `declared`, regardless of API completeness.

### Open decisions that must remain explicit

- **Stream overflow:** no universal default. Terminal output in this proposal chooses `drop_oldest + loss marker`; telemetry or video may choose differently. Corpus naming and terminal semantics still need ratification.
- **`snapshot_delta` compatibility lifetime:** this proposal retains it as an expiry-recovery profile. It may be deprecated after inventory proves no consumer needs it, but it must not be silently aliased to reset-bearing SWMR.
- **Value watch semantics:** current Value contract has immediate reads; Glial supplies change propagation through its session/binder. Decide whether watch becomes a portable Value operation with new corpus vectors or stays adapter-level invalidation.
- **Log producer cardinality:** `taut-shape` uses a source role while Glade’s fold orders many origins. Decide whether that is one multiwriter Log profile, a separate interleaved-log profile, or an adapter composition. Do not obscure it behind `writers="source"`.
- **CRDT identity and compaction:** actor authentication, equivocation, garbage collection, snapshot authority, and plugin ABI remain gates.
- **Window time model:** event time vs processing time, watermarking, late events, and refresh ownership must be fixed per view declaration.
- **Message delivery guarantees:** `one_way` states application response behavior, not at-most-once/at-least-once. If delivery acknowledgement/retry becomes portable, model it as interaction/transport policy rather than reviving Message as a shape.

## 16. Decision-ready summary

Approve the following decision package:

1. Replace one flat shape discriminator with `interaction + delivery profile + optional view` in canonical Taut IR v2.
2. Keep `value`, `atom`, `log`, `stream`, `swmr`, `snapshot_delta`, `crdt`, and `text_crdt` as concise, versioned delivery profiles backed by explicit normalized descriptors.
3. Reclassify `unary`, `message`, and `exchange` as interactions; reclassify `window` as a view and `windowed` as bounded-retention migration input.
4. Share cores only where corpus-visible behavior permits it: SWMR/`snapshot_delta` share snapshot-delta core; CRDT/Text share replica shell; Log/Stream may share infrastructure but not semantics.
5. Make Step 0.2 generate registries, canonical normalization, validation, compatibility analysis, and four API interaction forms from one source.
6. Make Step 0.3 remove Glial’s non-Log→Value fallback, validate Glade retention/profile pairs, and advertise exact adapter capabilities.
7. Treat Log as portable today; Value as a real Glial implementation; Atom/SWMR as strong schema/corpus gates without language engines; Datascad as fixture-only; Gryth as planned/mock; Stream/CRDT/Text as not yet engine-ready.
8. Gate every new profile/version with schema, negative and positive corpus, reference engine, same-language tests, and the required cross-language matrix. Unsupported means error, never fallback.

This preserves the names developers understand while making their actual invariants explicit enough for validators, engines, adapters, generated APIs, corpora, and live applications to agree.
