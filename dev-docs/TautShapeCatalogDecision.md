# Taut Shape Catalogue Decision

Status: consolidated decision — Steps 0.2 and 0.3 implemented locally

Date: 2026-08-22

Decision scope: Step 0.1 of `TautShapeImplementationPlan.md`

Supersedes: competing catalogue lists as sources of canonical meaning; it does
not supersede their detailed per-shape behavioral contracts

Independent inputs:

- `TautShapeCatalogProposal-F5.md`
- `TautShapeCatalogProposal-56.md`

The proposals remain unchanged as evidence and dissent. This document is the
single decision record to be consumed by Steps 0.2 and 0.3.

Phase 7 amendment (2026-08-22): the previously reserved `text_crdt` row is now
active as `text_crdt.profile/v1` over `crdt.oracle/v1`. Identity, vector resume,
equivocation, bootstrap, text payload, and convergence rules are ratified in
`taut-shape/dev-docs/TautShapeCrdtDecision.md`; all three portable engines, the
live 3x3 matrix, and Glial's collaborative consumer pass. Earlier statements in
this record describing CRDT as unbound or text_crdt as inactive are retained as
historical decision context and superseded by this amendment.

## 1. Decision summary

Taut retains a concise, closed, named `shape="..."` authoring surface for the
current implementation cycle. A shape name resolves through one canonical
registry to one of three semantic classes:

1. **Interaction kind** — determines invocation/cardinality but owns no
   taut-shape state machine.
2. **Engine shape** — owns a distinct payload-agnostic delivery contract,
   corpus, and portable state-machine family.
3. **Profile** — a stable public name for fixed policy on an engine core; it owns
   profile-specific conformance rows but must not fork the core implementation.

The canonical engine shapes are:

```text
value, atom, log, stream, swmr, crdt
```

The canonical profiles are:

```text
snapshot_delta -> swmr core with expiry/out-of-band recovery
text_crdt      -> crdt core with text identity/merge semantics
```

`unary` remains the canonical delivered-once interaction kind and retains its
current spelling as a Taut shape row with no engine core.

`message`, `exchange`, and `window` are not Taut delivery engines:

- `message` has no ratified portable semantics and is rejected as a shape;
- `exchange` remains Glade's directed, correlated service/routing interaction;
- `window` is an application projection/view concept whose base delivery must be
  an actual shape such as `log` or `swmr`.

Unknown, unimplemented, and unsupported shapes fail closed. No declaration may
silently run through `value`, `log`, or another available engine.

The normalized interaction/delivery/view decomposition proposed by agent 56 is
adopted as the semantic analysis model and as future-design input, but it does
not replace Taut's public IR now. A public IR-v2 split is deferred until a real
consumer needs one-way, generic duplex, or composable view declarations and the
trigger conditions in §14 are met.

## 2. How the independent proposals were used

Both proposals independently selected a validated profile model and agreed on
the substantive engine boundaries:

- six engine families (`value`, `atom`, `log`, `stream`, `swmr`, `crdt`);
- `snapshot_delta` sharing the SWMR core;
- `text_crdt` sharing the CRDT replication core;
- `unary` owning no stateful delivery engine;
- `exchange` being an interaction/routing mechanism rather than retained state;
- `window` being too ambiguous to implement as a delivery engine;
- exact fail-closed dispatch and per-adapter capabilities; and
- a strict distinction between declaration, corpus, reference implementation,
  portable engine, and live integration.

The material disagreement was representation and migration timing:

| Question | F5 | 56 | Consolidated decision |
| --- | --- | --- | --- |
| Public declaration | Keep `shape` as sole discriminator | Split into interaction + delivery + view in IR v2 | Keep `shape` now; preserve the decomposition as normalized metadata and future design. |
| `message` | Reject pending a real one-way need | Normalize to `one_way` | Reject now; one-way is an explicit IR-v2 trigger. |
| `exchange` | Keep Glade-only | Normalize to generic `duplex` | Keep Glade-only now; generic duplex is an explicit IR-v2 trigger. |
| `window` | Reject/defer | Add a composable view axis | Reject as a shape; use explicit producer projection over a base shape now; view axis deferred. |
| Migration | Additive registry and validation work | Taut model/DSL/compat/generator migration | Take the additive path so engine implementation is not blocked by an IR redesign. |

This is a staged synthesis, not a vote for one document. It adopts F5's current
authoring/migration boundary and 56's stronger semantic descriptors, capability
model, maturity distinctions, and falsification tests.

## 3. Normative vocabulary

### 3.1 Interaction kind

An interaction kind determines the invocation contract generated for a method.
It owns no retained delivery state, cursor, merge, or conformance engine.

`unary` is the only ratified Taut interaction kind in this decision: one request,
one whole response, delivered once.

Potential `one_way` and `duplex` interaction kinds are reserved design concepts,
not current registry rows. They require explicit method-model and generator work;
they must not be smuggled in as `message` or `exchange` delivery shapes.

### 3.2 Engine shape

An engine shape owns behavior that cannot be reduced to a fixed construction
policy on another engine without changing message vocabulary, states, ordering,
position, lifecycle, recovery, or merge invariants.

Every portable engine shape must eventually own:

- a Taut companion schema and generated IR;
- normative semantic decisions;
- authored positive and negative scenarios;
- a deterministic committed oracle corpus;
- Rust, TypeScript, and Python implementations;
- complete same-language corpus gates;
- all required live cross-language matrix rows; and
- an explicit adapter/consumer capability gate.

### 3.3 Engine core

An engine core is implementation vocabulary: the shared state machine behind one
engine shape and any fixed profiles. Core names are not application-manifest
escape hatches and do not permit arbitrary combinations.

Two public names may share a core only when profile-specific corpus rows prove
their different outcomes. Sharing helper code or a mailbox frame does not by
itself make two shapes one core.

### 3.4 Profile

A profile is a stable public name resolving to one engine core plus fixed policy.
A profile may set only knobs declared by that core. It owns conformance rows for
every outcome changed by the fixed policy.

If a proposed profile adds, removes, or re-types a message, state, position kind,
or lifecycle transition, it is a new engine shape rather than a profile.

### 3.5 View/projection

A view is application/domain computation over a source. It owns selection,
aggregation, range, time model, late-event behavior, and materialization. Its
base delivery shape owns transport, replay/position, retention mechanics, and
recovery.

No generic view axis is added to Taut in this decision. A current application
implements a view as a producer exposing an ordinary `atom`, `log`, or `swmr`
method, with separate control methods for steering when required.

### 3.6 Adapter capability

An adapter capability is an exact supported tuple such as:

```text
(public shape/profile, contract version, operations, corpus version)
```

It belongs to a language package or consumer adapter, not to the semantic shape
registry. Registry recognition never implies that every runtime can execute the
shape.

## 4. Canonical catalogue

| Current name | Decision | Canonical class | Normative meaning | Engine core | Declaration state and compatibility action | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| `unary` | Keep | Interaction kind | One request and one whole response, delivered once; no taut-shape engine or retained delivery state. | — | Public Taut default; existing spelling and behavior remain. | `taut` |
| `value` | Add to canonical Taut catalogue | Engine shape | Attributed multi-writer LWW whole-value register: dedup by `(origin, seq)`, winner by `(lamport, origin, seq)` (with `seq` resolving same-origin clock reuse), equivocation rejected, materialized reads. | `value` | Already public in Glade and contract-backed in taut-shape; Step 0.2 must resolve portable read/watch operation binding before generators claim subscription support. | `taut-shape`; Glade/Glial adapter |
| `atom` | Keep | Engine shape | Single-writer latest-value mailbox with versioned overwrite, late-reader refresh, held reads/timers, and terminal lifecycle; no back-history. | `atom` | Existing Taut name; uncommitted contract must pass Phase 1 review before release. | `taut-shape` |
| `log` | Keep | Engine shape | Single-origin retained ordered records with scalar cursor resume, bounded replay window, client-decided expiry, batching, held reads/timers, and terminal lifecycle. | `log` | Existing Taut and Glade name; only currently portable engine family. | `taut-shape` |
| `message` | Reject/reserve | Unsupported interaction spelling | No ratified semantics. A possible fire-and-forget method is an interaction kind, not a retained delivery engine. | — | Preserve Glade numeric value for decoding; reject new declarations and never emit it. Revisit only through the IR-v2 trigger. | `glade-decl`; future `taut` interaction design |
| `stream` | Keep | Engine shape | Disposable ordered live delivery with no cursor/replay and an explicit slow-consumer overflow policy. | `stream` | Existing Taut/Glade name; declarable for schema work but runtime adapters reject it until contract and capability exist. | `taut-shape` |
| `exchange` | Keep outside Taut catalogue | Glade interaction/service mechanism | Directed correlation-matched request/response routed to an attached provider; never folded, replicated, or cached as a shape. | — | Preserve Glade routing and numeric value; reject it in fold/delivery dispatch. Taut methods carried by an exchange remain unary for now. | `glade` |
| `window` | Reject/reserve as shape | View/projection concept | A range/time/key projection materialized by an application over an explicit base delivery shape. | — | Preserve Glade numeric value for decoding; reject new shape declarations. No automatic migration without known base, bounds, and recovery. | Application/view layer; future Taut view design |
| `swmr` | Keep | Engine shape | One wire-bound writer, snapshot plus bounded deltas, scalar sequence within a reset epoch, and typed in-band reset/repair. | `swmr` | Existing Taut name; draft `v1` must gain durable reset semantics before release or Datascad re-pin. | `taut-shape` |
| `snapshot_delta` | Keep and reclassify | Profile | SWMR core with expiry/out-of-band refresh when retained reconstruction is impossible, rather than SWMR's in-band reset/repair. | `swmr` | Existing Taut name; no second store/engine. The profile policy must be represented before the SWMR engine core is frozen. | `taut-shape` |
| `crdt` | Keep | Engine shape/family | Multi-writer attributed replica operations with per-origin identity, causal/vector resume, anti-entropy, deterministic convergence, and equivocation handling. | `crdt` | Existing Taut name remains contract-level until identity, compaction, corpus, and portable engines exist. | `taut-shape`, extracting reusable Glade precedent |
| `text_crdt` | Reserve | Profile | CRDT core with stable text item/position identity, text operations, compaction rules, and an adversarial text convergence corpus. | `crdt` | Canonical reserved name, not yet an active/declarable Taut row; add only with its schema and corpus. | `taut-shape` |
| `windowed` | Reject as catalogue term | Legacy retention spelling | An incomplete bounded-retention intent, not a shape. | Base shape | Do not emit or silently normalize. Existing use needs an owner-approved replacement with an explicit base and bound/policy. | Glade declaration/application config |

The catalogue deliberately distinguishes a **canonical reserved name** from an
**active compiler row**. New names such as `text_crdt` are not registered merely
to reserve vocabulary: registration waits until their semantics and slots are
concrete enough for validation.

## 5. Normative engine boundaries

### 5.1 `value`

The engine owns the attributed op set, exact-op idempotence, equivocation
rejection, LWW winner selection, and immediate materialized reads. It does not
own Glade share/key routing or application payload meaning.

`value` and `atom` remain distinct. Value is multi-writer and merge-bearing;
Atom is single-writer, sequential, lifecycle-bearing latest state. Sharing a UI
affordance called "current value" does not make their wire or state semantics
substitutable.

Open operation boundary: `value.v0` defines immediate reads, while Glial provides
change propagation through its session/binder. Portable Value watch semantics
require new corpus vectors; until then adapters may expose local invalidation but
must not claim it as portable `value` contract behavior.

### 5.2 `atom`

The engine owns version progression, overwrite/coalescing, latest-value refresh,
held reads, timer messages, terminal behavior, and stream teardown. It owns no
multi-writer merge and retains no historical values.

The single-writer invariant is normative. Whether v1 enforces writer identity in
the wire engine or requires the adapter to enforce it remains a blocking contract
decision in §13.

### 5.3 `log`

The engine owns a scalar record sequence, bounded replay window, cursor
resolution, batching bounds, client-decided expiry below the floor, held reads,
timers, lifecycle, and watermarks. The consumer owns payload meaning and chooses
safe retention/eviction policy within the contract.

The taut-shape Log contract is a single-origin delivery engine. Glade's
multi-origin replicated op fold is a lower substrate/assembly layer. Glial may
materialize that fold as a Log consumer, but doing so does not silently change
the portable Log cursor into a multi-origin vector. A future interleaved-log
profile requires its own corpus-visible identity and ordering decision.

### 5.4 `stream`

The engine owns live fan-out, ordering within a live session, explicit overflow
behavior, loss signaling if any, and terminal/disconnect behavior. It owns no
replay cursor or retained history.

Drop, coalesce, and bounded-buffer policies may be core construction profiles,
but Phase 5 must decide their exact observable states and loss markers before
the Stream schema is authored. There is no implicit universal default.

### 5.5 `swmr` and `snapshot_delta`

The SWMR core owns writer binding, reset epoch, scalar delivery sequence within
the epoch, snapshot re-base, bounded delta retention, cursor resolution,
held reads/timers, lifecycle, and recovery outcomes. Application generation,
revision, relational, and row semantics remain opaque payload/reset detail.

The two public behaviors are:

| Profile | Unrecoverable old cursor | Producer reset | Shared core |
| --- | --- | --- | --- |
| `swmr` | Typed reset with in-band fresh snapshot/deltas and reset detail | Allowed; increments reset epoch | Yes |
| `snapshot_delta` | Expiry/out-of-band refresh contract | Not exposed as the profile's application event | Yes |

Profile-specific vectors must reject the other profile's recovery outcome. A
second snapshot/delta store is prohibited.

### 5.6 `crdt` and `text_crdt`

The CRDT core owns replica/op identity, per-origin chains, deduplication,
equivocation handling, causal/vector position, anti-entropy, bootstrap, and
convergence-safe compaction protocol. A merge/payload specialization owns its
operation semantics and convergence oracle.

`text_crdt` shares the replica shell but must define stable text identity,
editing operations, state/update exchange, and text-specific compaction. Calling
an arbitrary merge plugin "text" is insufficient.

The `crdt.sync` output-slot question remains open: engine-owned heads/sync frames
must not appear as an application-bindable slot unless the schema author can
meaningfully type and consume it.

## 6. Canonical registry model

Taut's canonical registry remains the authoring discriminator and gains explicit
classification and normalized semantics. The exact implementation type is a
Step 0.2 concern, but every row must be equivalent to:

```python
ShapeSpec(
    name="snapshot_delta",
    shape_class="profile",          # interaction | engine | profile
    core="swmr",                    # None for unary
    fixed_profile={"recovery": "expire"},
    delivery="stream",              # once | stream
    events={"snapshot", "delta"},
    payload="delta",
    writers="single",
    ordering="scalar_epoch_seq",
    retention="snapshot_bounded_deltas",
    position="epoch_cursor",
    recovery="expire",
    merge="sequential_single_writer",
    lifecycle="mailbox_terminal",
)
```

Requirements:

- schema authors select a closed named row; they do not compose arbitrary axes;
- profiles resolve to a core and fixed policy in one canonical place;
- all exported IR contains enough normalized metadata for validators and tools to
  compare semantics without re-parsing prose;
- registry metadata is semantic and stable, not a record of which package happens
  to be installed;
- unknown names remain validation errors;
- adding a name requires a normative definition, slots, core classification, and
  compatibility analysis; and
- `register_shape` cannot make an arbitrary string executable without a matching
  adapter capability.

The following current fields need review rather than blind preservation:

- `initiation` is often adapter perspective, not engine behavior;
- `payload` is too coarse to distinguish whole state, record, snapshot, delta,
  operation, and opaque application payload;
- `writers="source"` does not settle Log's source versus Glade multi-origin
  layering; and
- `events` must distinguish application-bindable slots from engine protocol
  messages such as CRDT sync metadata.

## 7. Authoring surface

The current concise form remains canonical for this cycle:

```python
# Interaction kind; no delivery engine.
method("config.get", role="out", out=Ref("Config"))

# Engine shapes.
method("provider.status.subscribe", role="out", shape="atom",
       out=Ref("ProviderStatus"))
method("chat.subscribe", role="out", shape="log",
       out=Ref("ChatMessage"))
method("terminal.output.subscribe", role="out", shape="stream",
       out=Ref("TerminalChunk"))
method("query.subscribe", role="out", shape="swmr",
       out={"snapshot": Ref("QuerySnapshot"),
            "delta": Ref("QueryDelta")})
method("board.sync", role="out", shape="crdt",
       out={"op": Ref("BoardOp")})

# Shared-core profile.
method("cache.subscribe", role="out", shape="snapshot_delta",
       out={"snapshot": Ref("CacheSnapshot"),
            "delta": Ref("CacheDelta")})
```

Value becomes a canonical name, but Step 0.2 must bind its operation honestly:

```python
# Illustrative only until portable read/watch semantics are ratified.
method("workspace.title.read", role="out", shape="value",
       out=Ref("WorkspaceTitle"))
```

Collaborative text is not authorable until its profile contract exists:

```python
# Reserved future spelling; currently a validation error.
method("document.text.sync", role="out", shape="text_crdt",
       out={"op": Ref("TextOp")})
```

Fire-and-forget and generic duplex are intentionally not invented through shape
names:

```python
# Current portable form: explicit acknowledgement via unary.
method("audit.note", role="in", params=[("note", STR)], out=Ref("Ack"))

# Glade exchange remains a service/routing declaration whose carried Taut
# operations are unary. It is not shape="exchange" in Taut.
method("gwz.run", role="in", params=[("request", Ref("RunRequest"))],
       out=Ref("RunResponse"))
```

## 8. Shape, retention, and application policy

Shape semantics constrain retention; a separate retention declaration may tune
storage only within those constraints. It cannot redefine position or recovery.

| Shape/profile | Intrinsic semantic constraint | Permitted deployment tuning |
| --- | --- | --- |
| `value` | Materialized current winner; op history is substrate/convergence state, not a consumer cursor | Safe op compaction and persistence outside the portable read contract |
| `atom` | Latest value retained; no history | Lifetime/TTL only if expiry is surfaced without changing Atom semantics |
| `log` | Cursor-readable retained records with explicit floor/expiry | Record/byte/age bounds and eviction policy consistent with cursor expiry |
| `stream` | No replay history | Buffer bound only as part of the declared overflow policy |
| `swmr` | Current snapshot plus bounded reconstructible deltas | Positive delta bound and external persistence that preserves reset semantics |
| `snapshot_delta` | Same store core; expiry recovery | Delta bound and external refresh source |
| `crdt`/`text_crdt` | State/ops retained until convergence-safe compaction | Snapshot cadence and garbage collection proven safe by the profile |
| `unary`/Glade exchange | No shape retention | Transport timeout/retry outside delivery state |

Glade's current `RetentionPolicy` mixes delivery intent and substrate persistence.
Step 0.3 must inventory each live declaration and classify it as:

1. a compatible delivery tuning;
2. a lower-level substrate/store policy that should move out of the shape
   declaration; or
3. contradictory/ambiguous and requiring an owner decision.

In particular:

- `value + from_cursor` must not silently turn Value into Log; if it describes
  replicated op retention, it belongs to Glade's substrate configuration;
- `log + latest` contradicts replay semantics unless explicitly defined as a
  different profile;
- Stream and Exchange need no retained-shape policy;
- the free `windowed` token is invalid until it names an actual bound and
  recovery policy; and
- no migration may narrow data availability without an explicit before/after
  trace and owner approval.

## 9. Capability and maturity model

Semantic catalogue membership and implementation maturity are separate.
Capability manifests published by language packages and adapters use these
levels:

1. **declared** — normative definition and schema slots exist;
2. **corpus** — deterministic positive and negative vectors exist;
3. **reference** — one named reference engine passes the corpus;
4. **portable** — required language engines and live cross-language matrices pass;
5. **integrated** — a named consumer path passes an end-to-end adapter gate.

The levels are monotonic evidence labels, not fallback permissions. An adapter
advertises exact supported `(shape/profile, contract version, operations)` tuples
and rejects everything else before state mutation.

Current evidence at this decision date:

| Name | Highest honest evidence |
| --- | --- |
| `unary` | Generated/integrated Taut interaction; no engine applicable |
| `value` | Corpus + Glial reference/integration; not portable taut-shape packages |
| `atom` | Corpus draft/reference generator; no portable engine |
| `log` | Portable 3-language/3x3; partial Glial integration |
| `stream` | Declared/roadmap only |
| `swmr` | Corpus draft/reference generator + Datascad fixture integration; no portable engine |
| `snapshot_delta` | Declared profile intent only |
| `crdt` | Declared plus Glade mechanism/reference precedent; no portable delivery corpus |
| `text_crdt` | Reserved/planned only |

Datascad's exact contract pin remains fixture/contract evidence, not portable
runtime evidence. Gryth remains a planned consumer. Grip's `AtomValueTap` is an
application container and conveys no Taut Atom capability.

## 10. Fail-closed rules

All layers enforce explicit capability:

- Taut rejects unknown or not-yet-active shape names at schema validation.
- A generated/client package rejects a known shape/profile version it does not
  implement.
- Glade declaration loading rejects unsupported category combinations before a
  session or fold is constructed.
- Glial replaces `shape === "log" ? log : value` with an exhaustive adapter
  registry. Its initial supported delivery set is exactly the versions of
  `value` and `log` its tests prove.
- Rust and TypeScript Glade clients remove the same non-Log-to-Value fallback.
- Exchange continues through the dedicated Glade exchange path, never the fold
  registry.
- Capability negotiation may report unsupported; it may not reinterpret.

Every declared-but-unsupported legacy Glade name gets a negative test proving
failure before fold/store mutation.

## 11. Compatibility and versioning

This decision does not introduce Taut IR v2.

### Taut

- Existing `shape="..."` declarations remain source-compatible.
- `value` is an additive canonical catalogue name, but code generation support is
  gated on the operation decision in §13.
- Registry classification/semantic metadata is additive to exported IR. Step 0.2
  must ensure metadata-only changes do not masquerade as per-method behavioral
  changes in compatibility reporting.
- Existing `snapshot_delta` and `crdt` spellings remain recognized; capability
  checks prevent runtime claims beyond evidence.
- `text_crdt` is reserved in this decision but is not registered until its
  contract is concrete.

### taut-shape contracts

- No existing released Log or Value wire tag changes solely because of this
  catalogue decision.
- Atom/SWMR `v1` is uncommitted and unreleased; correctness fixes modify `v1` in
  place before its first freeze.
- Contract versions advance for observable changes to messages, states, ordering,
  position, lifecycle, recovery, merge, or identity—not for implementation-only
  refactors.
- Profiles share a core but carry their own conformance identity.

### Glade/Glial

- Existing numeric declaration enum values remain decodable; do not renumber.
- `message` and `window` values are reserved/unsupported and are not emitted by
  new declarations.
- `exchange` remains supported through the dedicated service/router mechanism,
  not as a fold.
- Existing manifests are inventoried before fail-closed behavior is enabled; any
  reliance on accidental fallback is migrated explicitly.

### Consumers

- Datascad is re-pinned only after the Atom/SWMR contract review passes.
- Gryth has no current migration; future binders select an explicitly supported
  shape and keep delivery protocol out of UI taps.

## 12. Consequences for implementation Steps 0.2 and 0.3

### Step 0.2 — canonical registry and documentation

Step 0.2 must:

1. Replace free dictionaries with a validated `ShapeSpec`-equivalent model while
   preserving the existing authoring field.
2. Classify every active row as interaction, engine, or profile.
3. Add normalized `core`, position, recovery, merge, lifecycle, and profile
   metadata.
4. Add `value` only with an honest operation/delivery decision and matching
   validation fixtures.
5. Reclassify `snapshot_delta` as a fixed SWMR profile.
6. Keep `text_crdt` reserved but inactive.
7. Reconcile architecture/roadmap/catalogue lists so they point here.
8. Add positive and negative registry/slot/compatibility fixtures.
9. Define an extension rule requiring semantic metadata and capability identity;
   arbitrary registered strings never imply implementation.
10. Leave current call-versus-subscribe code generation unchanged except where a
    newly ratified active row has a proven mapping.

### Step 0.3 — Glade/Glial declaration and dispatch

Step 0.3 must:

1. Inventory every live declaration and its effective adapter/retention behavior.
2. Replace all non-Log-to-Value branches with exhaustive dispatch.
3. Preserve dedicated Exchange routing outside the fold registry.
4. Reject `message` and `window` as new shape declarations while reserving their
   decode values.
5. Reject runtime use of Stream and any other known-but-unsupported engine until
   a capability is registered.
6. Classify or relocate every retention field per §8; do not auto-normalize
   ambiguous `windowed` or Value cursor retention.
7. Gate Value against all applicable value vectors and Log against the complete
   subset its adapter claims.
8. Add negative tests proving rejection before state mutation in Glial and both
   Glade clients.

## 13. Blocking pre-freeze decisions

These questions do not reopen the catalogue, but they must be resolved at the
named contract boundary.

### Before Atom `v1`

1. **Writer enforcement:** add `writer_id` and engine binding, or normatively make
   single-writer enforcement an adapter obligation. The choice must be tested and
   documented; "single" cannot remain an unenforced implication.

### Before SWMR `v1`

1. **Durable reset epoch:** stale pre-reset cursors must be distinguishable even
   when sequence numbers overlap after reset.
2. **Reset detail:** reset reason and opaque consumer detail must reach the read
   response.
3. **Profile policy:** decide how the shared core selects SWMR in-band reset versus
   `snapshot_delta` expiry so a later profile cannot force a second engine.
4. **Epoch initialization/restart:** specify whether and how a cursor survives node
   restart or instance recreation.

### Before portable Value

1. **Operation surface:** distinguish `set`, immediate `read`, and optional
   `watch` behavior.
2. **Watch ownership:** either add portable change-delivery corpus vectors or keep
   invalidation explicitly adapter-local.
3. **Future re-coring:** test whether the eventual CRDT replica core can reproduce
   Value behavior without changing its public name or corpus. Do this before
   duplicating substantial engines, not after.

### Before portable CRDT

1. Replica/op identity, equivocation, compaction, bootstrap, and snapshot authority.
2. Whether `sync` is an application slot or fixed engine protocol.
3. Whether Glade's multi-origin Log fold is adapter composition, a CRDT
   materialization, or a distinct interleaved-log profile.

## 14. Deferred interaction/delivery/view IR split

Agent 56's normalized model is retained as the leading design candidate for a
future Taut IR version:

```text
Endpoint = Interaction x (DeliveryProfile | none) x optional View

Interaction = request_response | one_way | subscription | duplex
```

It is not implemented now because current live requirements are representable
without changing the Taut model and every language generator, while portable
delivery engines are still missing.

A dedicated IR design is triggered when any of the following becomes a committed
near-term requirement:

1. A real Taut method requires no application response and an acknowledged unary
   would be semantically wrong.
2. A generic correlated or full-duplex Taut API must be generated independently
   of Glade's existing Exchange router.
3. One delivery profile needs more than one invocation form that cannot be
   represented honestly by current method roles and paired methods.
4. A view must compose over multiple base delivery profiles with portable,
   validator-visible range/time/recovery semantics.
5. The flat registry would require cross-product names rather than one additional
   well-defined engine/profile row.

When triggered, the design must prove:

- lossless normalization of every live Taut and Glade declaration or an explicit
  human-decision diagnostic;
- observably different, type-correct call/send/subscribe/duplex APIs in every
  supported generator;
- closed valid interaction/profile combinations rather than arbitrary axis mixing;
- compatibility reporting for interaction, profile version, policy, and view
  changes; and
- a migration that does not delay already-ratified portable engine work.

Until then, `message`, `exchange`, and `window` must not be added to Taut's
delivery registry as shortcuts.

## 15. Alternatives not selected

### One unclassified flat union

Rejected. Keeping every historical word as a peer would preserve category errors,
undefined names, retention contradictions, and accidental runtime fallback. A
closed list without classification is documentation rather than a model.

### Fully orthogonal author-composed axes

Rejected. It permits nonsensical combinations such as multi-writer Atom,
cursor-retained Stream, reset-recovery Value, or LWW Log, then recreates named
profiles as a validation matrix. The normalized axes are useful internally, not
as unrestricted public composition.

### Immediate interaction + delivery + view IR v2

Deferred, not rejected. It is cleaner if one-way, generic duplex, and composable
views are current requirements, but today it would expand catalogue cleanup into
model, DSL, serialization, compatibility, and all-generator migration before the
missing shape engines are built.

### One engine for every public word

Rejected. `snapshot_delta`/SWMR and CRDT/Text require shared cores with
profile-specific conformance; `unary`/Exchange own no delivery state; Window is
application computation. Engine identity follows observable state-machine
semantics, not vocabulary count.

## 16. Decision checks and falsification

The decision remains valid only while these checks hold:

1. Value and Atom reject one another's adversarial corpus behavior.
2. One SWMR core can produce both in-band-reset and expiry-profile outcomes while
   profile-negative vectors reject the wrong result.
3. Glial rejects every unsupported name before fold/store mutation.
4. Registry normalization is identical across exported IR and all consumers.
5. Every live Glade declaration can be classified without silent semantic change;
   ambiguous cases block migration.
6. A view materialized over Log or SWMR can define recovery without modifying the
   base engine. If not, Window requires a new design review.
7. CRDT convergence survives reorder, duplicates, partition/rejoin, compaction,
   and snapshot restore before CRDT is called portable.
8. Capability claims derive from executable conformance, never from a registry
   row, schema file, fixture pin, or package version alone.

If a check fails, revise the affected engine/profile boundary; do not restore
silent fallback or unrestricted shape strings.

## 17. Step 0.1 completion statement

Step 0.1 is complete at the catalogue-decision level when this record is accepted
as canonical and its source proposals remain archived as independent evidence.
Implementation begins with:

1. the Atom/SWMR pre-freeze correctness decisions already required by Phase 1;
2. the Step 0.2 classified registry and documentation reconciliation; and
3. the Step 0.3 Glade/Glial inventory and fail-closed dispatch.

This decision does not authorize those code changes by itself. It defines the
semantic target they must implement.
