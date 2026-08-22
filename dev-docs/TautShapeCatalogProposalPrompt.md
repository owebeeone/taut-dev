# Taut Shape Catalogue — Independent Findings and Proposal Prompt

Status: analysis commission for `TautShapeImplementationPlan.md` Step 0.1
Purpose: produce multiple independent, decision-ready shape-catalogue proposals
that can be compared and consolidated later

## Invocation and output naming

The launch message will assign you an agent name. Treat that value as
`<AGENT_NAME>` throughout this prompt.

Write your complete findings and proposal to the adjacent file:

```text
/Users/owebeeone/limbo/taut-dev/dev-docs/TautShapeCatalogProposal-<AGENT_NAME>.md
```

The output must be beside this prompt, not inside a member repository. Preserve
the supplied spelling when it is filesystem-safe (`A-Z`, `a-z`, `0-9`, `.`, `_`,
or `-`). If the supplied name contains other characters, replace each run of
unsafe characters with `-` in the filename and record both the assigned name and
normalized filename suffix in the document header.

If no agent name was supplied, stop and request one. Do not invent a designator.
If the target output already exists, do not overwrite it; report the collision.

## Independence rules

Several models will perform this commission separately. Independence is part of
the method.

- Do not read any file matching
  `dev-docs/TautShapeCatalogProposal-*.md`, even if one already exists.
- Do not ask another agent or sub-agent to analyze any part of the task.
- Do not modify code, schemas, corpora, plans, or existing documentation. Your
  only filesystem write is your assigned proposal document.
- Do not perform git mutations. Read-only inspection and status commands are
  allowed; use the installed `gwz` when inspecting workspace-wide state.
- Work from the current local files, including relevant uncommitted files. Record
  the observed revision and dirty-state summary so later consolidation knows
  which snapshot you analyzed.
- Existing plans and comments are evidence of intent, not ratified truth. In
  particular, do not merely restate the working classification in
  `TautShapeImplementationPlan.md`.
- Cite local evidence as `path:line`. Separate observed fact, inference, and
  recommendation. Mark anything you could not verify as `UNVERIFIED`.
- External research is optional and should only clarify established terminology
  or prior art. Local requirements remain authoritative; cite any external source
  used and state what it changed in your reasoning.

## Commission

Perform Step 0.1 of `TautShapeImplementationPlan.md` at proposal depth:

> Determine what a Taut "shape" should mean, identify semantic overlap and
> category errors in the current catalogues, compare credible normalized
> catalogues, and recommend one canonical model with an explicit compatibility
> and migration strategy.

The goal is not to preserve every current name as an independent engine. Nor is
the goal to minimize the number of names at any cost. The goal is a small,
coherent model that:

- makes illegal or contradictory method declarations difficult to express;
- gives code generators enough information to select the right API and runtime;
- lets runtime engines share mechanisms without hiding meaningful semantic
  differences;
- is understandable to a schema author without reading implementation code;
- admits future shapes without turning the registry into arbitrary strings;
- supports Rust, TypeScript, and Python consistently; and
- has a feasible migration path for Taut, taut-shape, Glade/Glial, Datascad, and
  Gryth.

You must make a recommendation. A report that only lists questions or says that
all alternatives are equivalent is incomplete.

## Why this analysis is needed

There are currently several overlapping catalogues and layers:

1. Taut's registry names `unary`, `atom`, `log`, `stream`, `swmr`,
   `snapshot_delta`, and `crdt`. It describes each as a point across payload,
   history, initiation, writers, events, and delivery axes, while also saying
   shape is the sole method discriminator.
2. taut-shape currently has contract artifacts for `log`, `value`, `atom`, and
   `swmr` at different maturity levels.
3. Glade's declaration enum names `value`, `log`, `message`, `stream`,
   `exchange`, and `window`.
4. Planning material additionally discusses `text_crdt`.
5. Glade separately declares retention (`latest`, `from_cursor`, `ttl`), which
   may overlap with shape names that already imply retention/history.
6. Current Glial code implements `value` and a subset of `log`, but dispatches
   non-`log` declarations through `value`; declaration vocabulary therefore
   exceeds real engine semantics.

These names may mix different dimensions:

- method interaction/cardinality (`unary`, `message`, `exchange`);
- delivery timing and initiation (`pull`, `push`, bidirectional);
- retention/history (`latest`, append-only, none, bounded window);
- reader state (`cursor`, version, reset epoch, replay/repair);
- writer cardinality and authority (single, source, multi-writer);
- merge/convergence (`value` LWW, CRDT ops);
- payload granularity (whole state, whole records, deltas, operations); and
- public product profiles (`window`, `snapshot_delta`, `text_crdt`).

A central question is therefore whether a single flat `shape` name should encode
all of these, whether some axes should become explicit independent fields, or
whether a small set of validated composite profiles should remain the public
surface over orthogonal internal dimensions.

## Required evidence

Read the relevant material completely enough to understand its definitions and
actual use. At minimum inspect:

### Taut and workspace plan

- `/Users/owebeeone/limbo/taut-dev/dev-docs/TautShapeImplementationPlan.md`
- `/Users/owebeeone/limbo/taut-dev/taut/src/taut/ir/shapes.py`
- Taut DSL validation, code generation, and tests that consume `shape`, found by
  searching `/Users/owebeeone/limbo/taut-dev/taut`
- `/Users/owebeeone/limbo/taut-dev/taut/dev-docs/TautCrdt.md`
- any Taut documents directly referenced by the registry or shape-validation code

### taut-shape contracts and design history

- `/Users/owebeeone/limbo/taut-dev/taut-shape/dev-docs/TautShapeArchitecture.md`
- `/Users/owebeeone/limbo/taut-dev/taut-shape/dev-docs/TautShapeRoadmap.md`
- `/Users/owebeeone/limbo/taut-dev/taut-shape/dev-docs/TautShapeGladeConsolidation.md`
- `/Users/owebeeone/limbo/taut-dev/taut-shape/dev-docs/AtomSwmrNotes.md`
- `/Users/owebeeone/limbo/taut-dev/taut-shape/dev-docs/TautShapeOracle.md`
- every `/Users/owebeeone/limbo/taut-dev/taut-shape/ir/shape_*.taut.py`
- corpus README/generators where they clarify behavior rather than merely repeat
  schema vocabulary
- the public APIs and README files of `taut-shape-rs`, `taut-shape-ts`, and
  `taut-shape-py`

### Current integration evidence

Use `/Users/owebeeone/limbo/glade-wz` as the current Glade/Glial integration
evidence unless local revision history proves another checkout is newer. Inspect:

- `glade-decl/ir/glade_decl.taut.py`
- `glial/src/instance.ts`
- `glial/src/folds/value.ts` and `glial/src/folds/log.ts`
- `glial/test/oracle.test.ts`
- TypeScript and Rust client session shape dispatch
- manifests/examples that actually declare shapes

Also inspect:

- `/Users/owebeeone/limbo/datascad/rl/harness/TAUT_ADAPTER.md`
- `/Users/owebeeone/limbo/datascad/rl/harness/TAUT_PIN.json`
- `/Users/owebeeone/limbo/gryth-dev/dev-docs/GrythDemoProposal.md`
- `/Users/owebeeone/limbo/gryth-dev/gryth-ui/package.json`
- representative Gryth taps/providers needed to distinguish a Grip atom from a
  Taut delivery shape

Search rather than assume that these are the only consumers. Report any additional
live consumer you find. Distinguish a schema declaration, a corpus-only gate, a
fixture adapter, and an end-to-end runtime integration.

## Required semantic decomposition

Build a semantic table for every current or proposed name:

```text
unary, value, atom, log, message, stream, exchange, window,
swmr, snapshot_delta, crdt, text_crdt
```

Add any additional name found in authoritative code or a live consumer. For each
name, determine or explicitly mark unknown:

| Axis | Questions |
| --- | --- |
| Interaction | One request/one response, one-way, subscription, duplex exchange, or independent of transport interaction? |
| Initiation | Pull, push, either, or bidirectional? Is this engine semantics or adapter behavior? |
| Producer cardinality | Exactly one bound writer, one source, many attributed writers, or unspecified? |
| Consumer cardinality | One, many independent readers, replicated peers, or unspecified? |
| Payload unit | Whole response, whole state, record, delta, operation, snapshot, or opaque/independent? |
| Ordering | None, total scalar sequence, per-origin sequence, causal/partial order, or implementation-defined? |
| Retention/history | None, latest only, bounded replay, append-only durable, reconstructible, or policy-controlled? |
| Reader position | None, version, scalar cursor, vector cursor, reset epoch, or application state? |
| Slow consumer | Hold, buffer, batch, drop, coalesce, expire/reset, or undefined? |
| Lifecycle | Immediate, held reads, seal/drain, close/fail, disconnect, producer stop, or profile-specific? |
| Recovery | Replay, latest refresh, snapshot plus deltas, reset/repair, peer sync, or none? |
| Merge | None, overwrite, LWW, application fold, CRDT convergence, or orthogonal to delivery? |
| Identity/addressing | Operation, value/atom/log id, stream id, writer id, origin, replica, or transport session? |
| Existing engine core | Unique state machine, alias, profile of another core, composition, or unimplemented declaration? |
| Actual consumers | End-to-end, corpus-conformant local implementation, fixture/contract pin, planned only, or none? |

Do not force a value into every cell. An `unknown` backed by a precise missing
decision is more useful than an invented semantic.

## Overlap questions that must be answered

Analyze at least these pairs/groups explicitly. Classify each relationship as
`same`, `alias`, `strict specialization`, `policy profile`, `shares an engine
core`, `orthogonal/composable`, `distinct`, or `name collision/category error`.
More than one label may apply at different layers.

1. **`unary` / `message` / `exchange`:** are these delivery state machines,
   transport interaction patterns, method cardinalities, or profiles combining
   those dimensions? Is `exchange` inherently a CRDT sync event, a generic RPC
   duplex channel, or a Glade frame operation that should not be a Taut shape?
2. **`value` / `atom`:** both expose a current whole value. Does multi-writer LWW
   folding versus single-writer versioned mailbox lifecycle justify distinct
   public shapes, distinct profiles over a common register abstraction, or a
   writer/merge axis plus a latest-retention axis?
3. **`value` / `crdt`:** is current `value` specifically an LWW-register CRDT?
   If so, should it be named as a CRDT specialization while retaining a convenient
   compatibility name?
4. **`log` / `stream` / `message`:** is the difference fundamentally retention,
   initiation, replay, or lifecycle? Could one ordered-delivery engine support
   retained and disposable policies without making semantics ambiguous?
5. **`log` / `window`:** is window a bounded log, a time/size aggregation, a
   materialized query view, or an underspecified product name? How does Glade's
   separate `RetentionPolicy` change the answer?
6. **`atom` / `swmr`:** is atom a degenerate SWMR with a snapshot and no deltas,
   or do its version/hold/terminal semantics make that abstraction harmful?
7. **`log` / `swmr` / `snapshot_delta`:** are deltas merely log records plus a
   baseline, or does in-band reset/repair create a distinct state machine? Does
   `snapshot_delta` differ from `swmr` at all once single-writer identity and reset
   policy are explicit?
8. **`swmr` / `window`:** is a windowed materialized result naturally an SWMR
   profile? Which semantics belong to the consumer rather than the delivery
   engine?
9. **`crdt` / `text_crdt`:** should text be a payload/merge specialization over a
   common replication envelope, or a separate delivery shape visible to Taut?
10. **Shape versus retention:** can a declaration combine a shape whose history
    implies `latest` or replay with a contradictory Glade retention policy? Where
    should such illegal combinations be rejected?
11. **Shape versus writer/merge:** should writer cardinality and merge strategy be
    encoded by the shape, separate axes, or validated profiles? What extensions
    would each choice permit or accidentally allow?
12. **Public name versus engine core:** which names deserve stable schema-author
    vocabulary even if two names share an implementation?

## Use-case tests

Test every candidate catalogue against these concrete cases. Show the declaration
or descriptor each proposal would expose; do not merely say that it supports the
case.

1. Ordinary unary request/response.
2. Fire-and-forget command or notification.
3. Single-writer provider status/presence with late subscribers receiving latest.
4. Glade's attributed multi-writer LWW whole-value surface.
5. Durable chat/history with cursor replay.
6. Ephemeral terminal output where a slow consumer may lose data or be dropped.
7. Datascad query results: single writer, snapshot plus deltas, generation reset,
   late join, retained resume, and opaque reset detail.
8. A bounded/time-windowed materialized view.
9. Multi-writer replicated state with generic CRDT operations.
10. Collaborative text with offline edits and convergence.
11. Generic bidirectional exchange where request and response lifetimes do not
    correspond to stored replicated state.

If a candidate needs application-specific semantics outside the shape engine,
identify exactly which layer owns them.

## Candidate proposals required

Develop at least three credible alternatives before recommending one. They must
include:

1. **Compatibility-first flat catalogue:** retain most public names, but define
   aliases/profiles and shared engine cores precisely.
2. **Minimal orthogonal engine catalogue:** expose only irreducible state machines
   as shapes and move interaction, retention, writer, or merge concepts to other
   axes where appropriate.
3. **Validated composite/profile model:** represent a shape as a named, validated
   composition of orthogonal internal dimensions while keeping stable convenient
   profile names for schema authors.

You may add a fourth alternative if it is genuinely distinct. Do not construct a
straw proposal merely to make the recommendation win.

For each alternative provide:

- the public declaration surface with a concrete example;
- the canonical names and normative one-sentence definitions;
- which names are aliases, profiles, deprecated compatibility terms, or rejected;
- the internal engine cores and reuse boundaries;
- how code generation chooses unary call, subscription, duplex, or other API;
- where retention, writer cardinality, merge strategy, and lifecycle live;
- how illegal combinations are prevented;
- changes required in Taut, taut-shape, Glade/Glial, Datascad, and Gryth;
- compatibility and migration cost; and
- the strongest argument against the alternative.

Score each alternative from 1 (poor) to 5 (strong), with concise justification,
against:

- semantic orthogonality;
- schema-author comprehensibility;
- illegal-state prevention;
- engine reuse without semantic leakage;
- code-generation determinism;
- Rust/TypeScript/Python implementation burden;
- current consumer fit;
- backward compatibility and migration risk;
- future extensibility; and
- testability/conformance clarity.

## Recommended proposal requirements

The recommendation must be concrete enough to drive Steps 0.2 and 0.3. Include:

### Canonical catalogue

A table with one row for every current name and these columns:

```text
current name | proposed status | canonical name/category | normative meaning |
public declaration? | engine core | compatibility/migration action | owner
```

`Proposed status` must be one of: `canonical engine shape`, `canonical profile`,
`orthogonal axis/value`, `interaction kind`, `compatibility alias`, `deprecated`,
or `rejected/unsupported`.

### Proposed declaration model

Show exact pseudo-IR for at least the eleven use cases above. If the recommendation
keeps a flat `shape="..."`, show how related axes and contradictory declarations
are validated. If it decomposes the field, show defaults and prove that common
declarations remain concise.

### Normative boundaries

For each canonical engine core state:

- what behavior the engine owns;
- what the transport/session adapter owns;
- what a consumer/application owns; and
- what a profile may configure without becoming a new engine.

### Migration sequence

Give a smallest-risk sequence for:

1. Taut registry/DSL/codegen;
2. taut-shape contracts and package APIs;
3. Glade declaration enum and retention field;
4. Glial fail-closed dispatch and existing `value`/`log` folds;
5. Datascad's atom/SWMR pin and adapter; and
6. future Gryth provider declarations.

Identify compatibility aliases that can be accepted on input but should not be
emitted by new generators. State whether any wire tag, corpus version, or public
package major version must change.

### Falsification and open decisions

State:

- the three strongest facts or future requirements that would overturn your
  recommendation;
- decisions that can be deferred without foreclosing the model;
- decisions that must be made before atom/SWMR `v1` is frozen; and
- any term whose current semantics are too incomplete to classify safely.

## Output document structure

Write `TautShapeCatalogProposal-<AGENT_NAME>.md` with exactly these top-level
sections so proposal consolidation can compare like with like:

1. `# Taut Shape Catalogue Proposal — <AGENT_NAME>`
2. `## 1. Analysis snapshot`
3. `## 2. Executive recommendation`
4. `## 3. Evidence and current catalogues`
5. `## 4. Semantic decomposition`
6. `## 5. Overlap findings`
7. `## 6. Use-case tests of the current model`
8. `## 7. Candidate A — compatibility-first flat catalogue`
9. `## 8. Candidate B — minimal orthogonal engine catalogue`
10. `## 9. Candidate C — validated composite/profile model`
11. `## 10. Comparative scorecard`
12. `## 11. Recommended canonical catalogue`
13. `## 12. Proposed declaration model and examples`
14. `## 13. Engine, adapter, and application boundaries`
15. `## 14. Migration plan and impact on Steps 0.2/0.3`
16. `## 15. Risks, falsification, and open decisions`
17. `## 16. Decision-ready summary`

Within `## 5. Overlap findings`, assign citable IDs using the filename-safe agent
suffix: `<AGENT_NAME>-F01`, `<AGENT_NAME>-F02`, and so on. Each finding must state:

```text
ID | names/layers | relationship | evidence | consequence | proposal implication
```

The final decision-ready summary must fit on one screen and contain:

- the recommended shape model in one paragraph;
- the canonical engine/profile names;
- names to alias, deprecate, or reject;
- the first three migration actions; and
- the most important unresolved decision.

## Completion check

Before finishing, verify that:

- every required name appears in both the semantic table and recommended-catalogue
  table;
- all twelve overlap questions are answered;
- all eleven use cases have concrete declarations under the recommendation;
- all three candidate families are credible and scored;
- claims about live use distinguish declarations, tests, fixture adapters, and
  end-to-end runtime paths;
- every factual claim has a local `path:line` citation;
- no other agent's proposal was read;
- no file other than your assigned output was changed; and
- your final chat response reports the recommendation in at most ten lines and
  links the written proposal path.
