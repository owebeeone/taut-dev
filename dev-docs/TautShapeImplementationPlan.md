# Taut Shape Implementation and Integration Plan

Status: complete locally — Phases 0–8 implemented; packages unreleased
Date: 2026-08-22
Scope: the `taut-dev` workspace plus its Glade/Glial, Datascad, and Gryth
integration seams

## 1. Outcome

Deliver the complete, agreed Taut delivery-shape set as payload-agnostic,
corpus-conformant engines in Rust, TypeScript, and Python, with live cross-language
interop and at least one explicit consumer gate for every shape.

Completion means:

- there is one canonical shape catalogue and every public declaration maps to it
  explicitly;
- every engine shape has a Taut IR schema, authored scenarios, a committed oracle
  corpus, generated bindings, Rust/TypeScript/Python engines, and a 3x3 live
  node/client matrix;
- profile shapes reuse a named core engine rather than duplicating it;
- unsupported shapes fail closed instead of silently using another shape;
- Glade/Glial, Datascad, and Gryth consume shapes through declared adapters and
  act as integration acceptance gates; and
- each milestone can ship independently without waiting for the entire catalogue.

This plan supersedes the implementation ordering in
`taut-shape/dev-docs/TautShapeRoadmap.md` where the current workspace or active
consumer evidence has moved on. It does not replace that document's detailed
per-shape semantics.

## 2. Current baseline

As of 2026-08-22:

| Area | State |
| --- | --- |
| `log` | Rust, TypeScript, and Python engines exist; corpus gates and the 3x3 matrix pass. |
| `value` | Rust, TypeScript, and Python engines pass the 13-vector corpus and the live 3x3 matrix; Glial's explicit local adapter passes the same taut-shape-owned corpus. |
| `atom` | Rust, TypeScript, and Python engines pass all 28 `v1` vectors and a five-scenario 3x3 live matrix; Glial consumes it for a single-writer provider-status surface. |
| `swmr` | Rust, TypeScript, and Python pass all 33 `v1` vectors and five live scenarios across the 3x3 matrix. |
| `stream` | Rust, TypeScript, and Python pass all 28 `v1` vectors and five live scenarios across the 3x3 matrix; overflow drops slow readers explicitly and reconnect is a live-only late join. |
| `snapshot_delta` | Fixed expiry profile over SWMR; four profile vectors and three 3x3 live scenarios pass without a second store/resolver. |
| `crdt` | Rust, TypeScript, and Python pass 15 mailbox vectors, five N-replica convergence scenarios, and four live scenarios across the 3x3 matrix. |
| `text_crdt` | Fixed specialization over the CRDT core; five convergence/profile scenarios and four live 3x3 scenarios pass. |
| Glade/Glial | Real `value` and `log` use plus canonical TypeScript-engine adapters for provider-status `atom` and live-metrics `stream` surfaces. Fold/mount dispatch remains exactly value/log; atom/stream have separate single-writer service boundaries. All 25 log vectors are classified at the owning seam (6 assembly, 19 portable-node lifecycle). Exchange remains a dedicated service path. |
| Datascad | Keeps its exact contract pin, passes all 15 existing adapter checks, and runs one real SQLite query-result generation-reset path through `taut-shape-py` SWMR. |
| Gryth | The existing `WORKSPACE_NAME` Grip consumer is now served by a Glial `value` provider in the GWZ-managed workspace; the original grip/type remains unchanged and its seam test covers write round-trip. Other surfaces remain incremental future cutovers. |

The workspace repositories were fetched and were each 0 ahead / 0 behind
`origin/main` when this plan was authored. No upstream merge is a prerequisite.
The immediate work is review and completion of the local uncommitted changes.

## 3. Shape catalogue working model

Phase 0 must ratify this model before additional public APIs are added.

### 3.1 Engine shapes

These have distinct state, cursor, lifecycle, or convergence semantics and earn
their own contracts and conformance suites:

| Shape | Semantic core |
| --- | --- |
| `value` | Attributed multi-writer LWW whole-value register with deduplication and equivocation rejection. |
| `atom` | Single retained latest value with versioned reads, holds, timers, and terminal lifecycle. |
| `log` | Retained ordered records with cursor reads, batching, holds, eviction, and terminal lifecycle. |
| `stream` | Disposable ordered delivery with an explicit slow-consumer/overflow policy. |
| `swmr` | Single-writer snapshot plus retained deltas, reset epochs, resume repair, and lifecycle. |
| `crdt` | Multi-writer replicated operations with deterministic convergence. |

### 3.2 Profiles and specializations

- `snapshot_delta` is a public profile of the SWMR engine with a named reset and
  retention policy. It must not fork a second snapshot/delta store.
- `text_crdt` is a CRDT specialization with text operations and a text-specific
  oracle layered over the common convergence engine.
- `window` is provisionally a projection/retention profile over `log`, `stream`,
  or `swmr`. It becomes an engine shape only if Phase 0 identifies independent
  wire and lifecycle semantics.

### 3.3 Interaction and transport names

- `unary` remains a Taut method cardinality unless a missing delivery state
  machine is demonstrated.
- Glade's `message` and `exchange` remain interaction/frame patterns rather than
  stateful shape engines unless Phase 0 proves otherwise.

This classification preserves the useful public words while avoiding nine
near-duplicate engines. The canonical registry must record both engine shapes
and any supported aliases/profiles so code generation and consumers do not infer
the mapping independently.

## 4. Delivery rules

1. `taut-shape` owns the payload-agnostic wire contracts and oracle corpora.
2. Each language package owns its engine implementation and generated bindings.
3. The oracle is mandatory; implementation identity is not. A consumer may keep
   a local engine only if it passes the same complete applicable corpus.
4. New behavior is corpus-first: authored scenario, generated expected transcript,
   then language implementations.
5. All dispatch is explicit and fail-closed. No `else => value`, `else => log`, or
   similar compatibility fallback is permitted.
6. A shared engine core may serve multiple named profiles, but each public profile
   has explicit capability metadata and conformance rows.
7. Every step below targets fewer than 500 changed lines where practical. Generated
   outputs and committed corpus data are excluded from that aspirational budget.
8. A shared contract or harness change lands before independent language work that
   depends on it. Rust, TypeScript, Python, and consumer adapters can then proceed
   in parallel.

## 5. Phased plan

### Phase 0 — Canonical catalogue and fail-closed capability model

Milestone: one reviewed vocabulary maps Taut, taut-shape, and Glade names to
engine shapes, profiles, or non-shape interaction patterns.

Progress (2026-08-22): Steps 0.1–0.3 are implemented locally. Taut now exports
validated normalized `ShapeSpec` rows (including `value` and the
`snapshot_delta -> swmr` profile); Glial and both Glade clients dispatch
`value`/`log` exactly and reject all other fold shapes before mutation; Glade
keeps Exchange on its dedicated service path. The declaration/retention
inventory is in `glade/dev-docs/GladeShapeDispatch.md`. Changes remain
uncommitted.

#### Step 0.1 — Ratify the catalogue

Write a short decision record alongside this plan that resolves `value`, `unary`,
`message`, `exchange`, `window`, `snapshot_delta`, and `text_crdt`. Record for each
name its owner, semantics, engine/profile classification, and compatibility name.

Commission independent proposals with
[`TautShapeCatalogProposalPrompt.md`](TautShapeCatalogProposalPrompt.md), then
compare and consolidate them into the decision record without allowing proposal
authors to read one another's work first.

Consolidated decision record:
[`TautShapeCatalogDecision.md`](TautShapeCatalogDecision.md), derived from the
independent F5 and 56 proposals while retaining both as evidence.

Acceptance:

- every name in `taut/src/taut/ir/shapes.py`, `taut-shape/ir/shape_*.taut.py`, and
  the Glade declaration enum appears exactly once in the mapping;
- `value` and `atom` remain distinct unless their different writer and lifecycle
  semantics are deliberately redesigned; and
- unresolved names are marked unsupported, not silently mapped.

#### Step 0.2 — Reconcile registries and architecture docs

Update the canonical Taut registry and taut-shape architecture/roadmap documents
to reflect the decision. Add machine-readable profile/alias metadata only if a
current generator or runtime consumes it; avoid speculative framework work.

Acceptance:

- one source is named canonical;
- schema regeneration and existing Taut tests pass; and
- documentation contains no competing list described as canonical.

#### Step 0.3 — Make Glade/Glial dispatch explicit

Replace the current `log` versus everything-else dispatch with an exhaustive
shape adapter registry. Initially register only actually supported shapes.
Return a typed unsupported-shape error during manifest/session construction.

Acceptance:

- `value` and `log` behavior remains green;
- `message`, `stream`, `exchange`, and `window` cannot execute as `value`; and
- one negative test exists for every declared-but-unsupported name.

Parallelism: Steps 0.2 and 0.3 may proceed in parallel after Step 0.1.

### Phase 1 — Stabilize and land the current atom/SWMR contract work

Milestone: the uncommitted atom/SWMR `v1` artifacts are correctness-reviewed,
fully reproducible, and safe for language implementations and Datascad to pin.

Progress (2026-08-22): completed locally and re-pinned in Datascad; see the
clean post-remediation report at
`taut-shape/dev-docs/TautShapePhase1Review.md`. The changes remain uncommitted.

#### Step 1.1 — Make SWMR resets durable

Replace sequence-only reset detection with an explicit node-managed reset epoch
in the cursor/protocol. A producer reset increments the epoch; compaction snapshot
pushes do not. Retain the most recent reset reason and opaque detail so a reader
presenting an old epoch receives `state=reset` plus the fresh repair payload even
when the reset occurred between polls.

An absent cursor still means a new reader and does not receive a historical reset.
Because `swmr.v1` is uncommitted and unreleased, correct `v1` in place rather than
publishing a knowingly broken `v2` transition.

Acceptance:

- an old cursor cannot be accepted as current after a reset, even if sequence
  numbers overlap;
- a caught-up reader remains caught up across compaction that does not reset;
- reset reason and opaque detail reach the read response; and
- restart/epoch initialization behavior is documented.

#### Step 1.2 — Add reset regression vectors

Add authored scenarios for reset-between-polls, reset detail propagation, stale
epoch with overlapping sequence, absent cursor after reset, held read across reset,
and compaction without reset. Regenerate `swmr.v1.json` from the reference engine.

Acceptance:

- each regression fails against the current draft behavior for the intended
  reason before the fix and passes afterward;
- corpus generation is deterministic; and
- IR regeneration and corpus `--check` gates are clean.

#### Step 1.3 — Close the remaining implementation-quality findings

Remove creation-order quadratic held-reader release behavior in TypeScript and
Python, and make the matrix terminate an already-started child and close its pipes
when its peer executable is missing or startup fails.

Acceptance:

- held-reader release is linear or `O(H log H)` for `H` held streams;
- tests cover non-creation release order and a large held-reader set;
- the missing-peer matrix test leaves no live process; and
- existing log behavior remains corpus-compatible.

#### Step 1.4 — Run the complete review gate

Run IR regeneration checks, every corpus generator in check mode, Rust tests and
`no_std` build, TypeScript tests and typecheck, Python tests and targeted strict
typecheck, and both normal and isolated-Python 3x3 matrix runs. Produce a fresh
post-remediation review report; prior reports remain historical evidence.

Acceptance:

- no open correctness finding remains;
- any repository-wide pre-existing lint/typecheck limitation is separated from
  changed-file gates; and
- the atom/SWMR files are ready to commit as one coherent contract milestone.

#### Step 1.5 — Re-pin Datascad deliberately

After the contract is stable, update Datascad's exact hashes and adapter mapping,
then run all adapter/self-tests. Do not re-pin before reset semantics and response
detail are final.

Acceptance:

- the pin names every consumed artifact;
- pin drift detection still fails on an intentional mismatch; and
- all Datascad adapter/self-tests pass against the new contract.

Parallelism: Step 1.3 can run alongside Steps 1.1–1.2. Steps 1.4 and 1.5 are
ordered final gates.

### Phase 2 — Shared multi-shape runtime and matrix seam

Milestone: adding a shape no longer requires copying log-specific CLI, framing,
or matrix control flow.

Progress (2026-08-22): completed locally. The normative
boundary is in
[`TautShapeEngineAdapterContract.md`](TautShapeEngineAdapterContract.md). Rust,
TypeScript, and Python route the existing `log` node through a generic
decode/dispatch/encode/effect/finish shell. Their `node` and `client` modes now
select the exact adapter with `--shape <name>` (default `log`), advertise the
same implemented registry, and reject unsupported names before input or session
startup. Typed unknown-shape and unknown-tag diagnostics and non-log placeholder
contract tests exist in every language. The live matrix now separates
shape-neutral process transport/cleanup from registered shape commands,
scenarios, and canonicalization; a live non-log smoke fixture uses the same path.
All existing language suites and all 36 live log rows pass in normal and
isolated-Python modes, and partial-start/protocol-failure leak regressions pass.
Phase 3 is next.

#### Step 2.1 — Define the engine adapter contract

Define the smallest per-language adapter surface for input decoding, engine
dispatch, output encoding, timer actions, and teardown. Keep concrete state
machines shape-local; share only the shell.

Acceptance:

- `log` runs through the adapter without transcript changes;
- unknown shapes and unknown message tags fail with typed diagnostics; and
- the adapter does not impose log cursor or lifecycle types on other shapes.

#### Step 2.2 — Add explicit shape selection to each CLI

Add a consistent `--shape <name>` or equivalent subcommand in Rust, TypeScript,
and Python. Register message-tag maps per shape.

Progress (2026-08-22): implemented locally. All six `node`/`client` entry paths
accept exact `--shape` selection, default to `log`, and reject an unsupported
name with the shared typed diagnostic before reading or writing the data
channel. Explicit-`log` self-pair tests preserve existing framing.

Acceptance:

- all three CLIs expose the same supported shape names;
- framing remains byte-compatible for log; and
- unsupported shape selection exits deterministically before starting a session.

#### Step 2.3 — Generalize the live matrix

Separate process orchestration and transcript transport from shape scenarios and
canonicalization. Select node/client commands from the shared shape registry and
guarantee cleanup on every startup and protocol failure path.

Progress (2026-08-22): implemented locally. `matrix/harness.py` owns only child
lifecycles and crossed pipes; `matrix/shapes.py` defines the registration seam;
and `matrix/log_shape.py` owns log scenarios and canonicalization. The driver
builds both commands with explicit `--shape` selection from the registry. A
separate live `smoke` fixture proves a non-log shape can run through the same
code, and PID-based regressions prove cleanup after partial startup and a hung
peer.

Acceptance:

- existing 36 log rows remain green in normal and isolated-Python modes;
- a minimal second-shape smoke fixture can run without log-specific branches; and
- process-leak regression tests pass.

Parallelism: language CLI changes in Step 2.2 may proceed independently once Step
2.1 is fixed. Step 2.3 can start with the adapter contract and finish after the
three CLIs land.

### Phase 3 — Value vertical slice

Milestone: `value` is the first non-log shape with three engines, live interop,
and a real Glade/Glial consumer.

Progress (2026-08-22): completed locally. The canonical schema and all 13
`value.oracle/v0` vectors regenerate cleanly. Rust, TypeScript, and Python expose
independent attributed LWW engines with exact op deduplication and equivocation
diagnostics. Their CLIs register shape-specific tags and pass five authored live
scenarios across all 9 language pairings in normal and isolated-Python modes.
The TypeScript wire runtime was refreshed from canonical Taut so signed 64-bit
stamps survive end-to-end as `bigint`. Glial retains its explicit `ValueRegister`
adapter and passes the complete taut-shape-owned corpus plus its integration
suite. Changes remain uncommitted.

#### Step 3.1 — Implement the value engine in each language

Generate/import the value bindings and implement op-set deduplication, LWW winner
selection by `(lamport, origin, seq)`, equivocation rejection, and immediate
reads. `seq` is the deterministic final tie-break when one origin reuses a
Lamport value.
Rust, TypeScript, and Python are independent steps, each kept below the target
change budget.

Acceptance per language:

- all 13 value corpus vectors pass byte-for-byte;
- malformed and unknown tags fail closed; and
- repeated exact ops are idempotent while equivocation leaves state unchanged.

#### Step 3.2 — Add the value 3x3 matrix

Add value scenarios to the generic matrix and exercise every node/client pairing.

Acceptance:

- all 9 language pairings pass;
- normal and isolated-Python modes agree; and
- transcripts match the committed oracle.

#### Step 3.3 — Graduate Glial/Glade onto the contract seam

Either use the taut-shape TypeScript engine or keep Glial's local assembly and
prove it against the complete value corpus through an explicit adapter. Repoint
private oracle references to the taut-shape-owned corpus where possible.

Acceptance:

- Glial's value adapter is named explicitly in dispatch;
- its complete applicable corpus and integration suite pass; and
- deleting a private duplicate oracle loses no coverage.

Parallelism: the three language implementations can proceed in parallel. Glial
adapter work can begin once the TypeScript types and adapter contract are stable.

### Phase 4 — Atom vertical slice

Milestone: the latest-state mailbox works identically in all languages and has a
live single-writer consumer surface.

Progress (2026-08-22): completed locally. Rust, TypeScript, and Python pass all
28 `atom.oracle/v1` vectors, deterministic timer/teardown checks, and 2,000-held-
reader scaling tests. Five live scenarios pass all 45 atom language pairings,
covering replacement wake-up, scripted timer expiry, terminal drain, failed
close, and two readers. Glial's explicit `GlialAtomAdapter` uses the canonical
TypeScript engine for a provider-status surface; its declaration registry and
writer handle reject a second writer, and its integration test covers replace
plus reconnect from the last version. See
`taut-shape/dev-docs/TautShapePhase4Review.md`.

#### Step 4.1 — Implement Rust, TypeScript, and Python atom engines

Implement replace/version behavior, held reads, timers, supersession, terminal
states, stream teardown, and producer-stop behavior from the stabilized corpus.

Acceptance per language:

- every atom corpus vector passes;
- timer and teardown actions are deterministic Sans-I/O outputs; and
- large held-reader tests meet the chosen complexity bound.

#### Step 4.2 — Add atom live interop

Add atom scenarios and all 9 node/client pairings to the matrix, including held
read wake-up, timer expiry, terminal drain, and multi-reader cases.

#### Step 4.3 — Add one real atom consumer

Use an atom for a genuinely single-writer latest-state surface such as presence,
provider status, or an active-session snapshot. Do not relabel Glade's multi-writer
`value` register as atom.

Acceptance:

- the declaration rejects a second writer at the service boundary;
- a real Glial/Glade or Datascad path crosses the adapter; and
- the consumer has an integration test for replacement and reconnect/resume.

### Phase 5 — Stream vertical slice

Milestone: disposable ordered delivery has a frozen slow-consumer contract and
three interoperable engines.

Progress (2026-08-22): completed locally. The bounded-ring/drop policy is frozen
in `taut-shape/dev-docs/TautShapeStreamDecision.md`; the authored IR and all 28
`stream.oracle/v1` vectors regenerate cleanly. Rust, TypeScript, and Python
engines pass their complete corpus, construction-bound, and 2,000-held-reader
tests and expose the same CLI capability. Five scenarios pass all 45 stream
language-pair cells, including observable slow-reader loss and reconnect as a
late join. Glial's `LiveMetricsStream` uses the canonical TypeScript engine and
tests loss counting, no-replay reconnect, and the next live record. See
`taut-shape/dev-docs/TautShapePhase5Review.md`.

#### Step 5.1 — Freeze stream policy decisions

Decide whether slow consumers are dropped, coalesced, or buffered; define batch
bounds, resume semantics, late join, terminal behavior, and whether policy is a
construction knob or distinct profile. Record the decision before authoring IR.

#### Step 5.2 — Author stream IR and oracle

Create the schema, notes, authored scenarios, reference engine, generated IR, and
corpus. Include overflow, multi-reader, held-read, timer, and teardown vectors.

#### Step 5.3 — Implement and matrix all three languages

Implement Rust, TypeScript, and Python engines independently, then add all 9 live
pairings.

#### Step 5.4 — Integrate a live stream surface

Use terminal output, telemetry, or another disposable live feed. Gryth's terminal
proposal is a suitable acceptance consumer once its Glial provider is available.

Acceptance:

- slow-consumer behavior is observable and corpus-defined;
- memory remains bounded under the selected policy; and
- a consumer reconnect test demonstrates the documented loss/resume behavior.

### Phase 6 — SWMR and snapshot-delta vertical slice

Milestone: the stabilized snapshot/delta contract has three engines, one shared
profile core, live interop, and a Datascad runtime consumer.

Progress (2026-08-22): completed locally. All three SWMR engines pass the
33-vector corpus and 45 live cells. `snapshot_delta.profile/v1` is a fixed
expiry/out-of-band-refresh projection over the same cores, with four portable
vectors and 27 live cells including reset between polls. Datascad's existing 15
checks remain green and its new SQLite runtime selftest crosses a generation
reset through the Python engine with byte-identical opaque detail. The full
matrix/harness is 246/246 and isolated mode is 243/243. See
`taut-shape/dev-docs/TautShapeSnapshotDeltaDecision.md` and
`taut-shape/dev-docs/TautShapePhase6Review.md`.

#### Step 6.1 — Implement Rust, TypeScript, and Python SWMR engines

Implement writer binding, reset epochs, snapshot compaction, retained deltas,
resume repair, held reads, timers, terminal behavior, and teardown.

Acceptance per language:

- every SWMR corpus vector passes;
- stale epochs always reset and repair in-band;
- compaction never resets a caught-up reader; and
- reset detail remains byte-identical end-to-end.

#### Step 6.2 — Define snapshot-delta as an SWMR profile

Specify its public name, construction defaults, allowed messages, and reset policy
without copying the store or resolver.

Acceptance:

- profile conformance runs through the SWMR core;
- profile-specific vectors cover every changed policy; and
- code coverage demonstrates the common resolver is shared.

#### Step 6.3 — Add SWMR/profile live matrices

Run all 9 SWMR pairings and the profile-specific rows, including a reader crossing
a reset between polls.

#### Step 6.4 — Move Datascad from fixture adapter to runtime adapter

Keep the contract pin, then connect one real query/result path to a selected
language engine. Carry query generation/revision context in the opaque reset
detail while the engine owns only reset epoch and delivery sequence.

Acceptance:

- the existing 14 adapter/self-tests stay green;
- an end-to-end test crosses generation reset and receives detail; and
- no Datascad relational/query semantics leak into taut-shape.

Parallelism: Phases 5 and 6 may proceed in parallel after Phase 2 and the atom
mailbox precedent, provided they do not make competing shared-shell changes.

### Phase 7 — CRDT and text specialization

Milestone: multi-writer convergence is an explicit delivery contract rather than
an implementation detail inside Glade.

Progress (2026-08-22): completed locally. `crdt.oracle/v1` defines immutable
`(origin, seq)` identities, normalized vector dependencies/resume, bounded
causal buffering, deterministic equivocation, bootstrap floor, and terminal
reads. All three engines pass 15 mailbox vectors, five N-replica convergence
scenarios, and 36 live CRDT cells. `text_crdt.profile/v1` shares the exact core,
passes five text convergence scenarios and 36 live cells, and Glial's
collaborative-text adapter passes offline concurrent edit, reconnect, idempotent
resync, and delete tests. See `taut-shape/dev-docs/TautShapeCrdtDecision.md` and
`taut-shape/dev-docs/TautShapePhase7Review.md`.

#### Step 7.1 — Define CRDT identity and envelope boundaries

Ratify `(stream_id, origin)` or its replacement, operation identity, causal
metadata, deduplication, equivocation, snapshot/bootstrap, and error behavior.
Reuse the Glade op envelope only where it is genuinely shape-level.

#### Step 7.2 — Build an N-replica convergence oracle

Author operation sets and delivery permutations and require identical final state
and diagnostics. Include duplicates, reordering, concurrent writers, reconnect,
and snapshot bootstrap. Keep payload CRDT logic pluggable.

#### Step 7.3 — Implement the common CRDT delivery engine

Implement Rust, TypeScript, and Python delivery cores and live multi-replica
matrix scenarios. Reuse Taut/Glade fold code as reference material, not as an
unreviewed second contract.

#### Step 7.4 — Add the text-CRDT specialization

Layer text operations and text-specific convergence vectors over the common core.
Do not fork identity, transport, deduplication, or bootstrap logic.

#### Step 7.5 — Integrate a collaborative Glade/Gryth surface

Use a deliberately collaborative document or editor surface. Existing `value`
and `log` consumers remain unchanged.

Acceptance:

- every replica order in the oracle converges;
- all language combinations agree on final state and diagnostics; and
- the consumer works offline/reconnect without a private convergence rule.

### Phase 8 — Consumer graduation, releases, and maintenance

Milestone: the shape family is independently releasable and consumer drift is
detected continuously.

Progress (2026-08-22): completed locally. Glial classifies all 25 log vectors
and gates the six assembly-applicable rows. Gryth's workspace-name mock producer
was replaced by a Glial `value` tap without changing its Grip consumer. A
machine-readable compatibility manifest/checker plus contract, Glial, and Gryth
CI workflows gate every IR/corpus, all language packages, the full/isolated
matrices, and selected consumers. All artifacts remain explicitly development
or private; tag mode rejects dirty trees, development versions, and path/hash
pins before release. See `taut-shape/dev-docs/TautShapePhase8Review.md` and
`taut-shape/dev-docs/TautShapeReleaseCompatibility.md`.

#### Step 8.1 — Complete Glial's applicable log coverage

Map the full log corpus to the assembly seam or document precisely which node-only
lifecycle vectors do not apply. Add integration coverage for holds, timers,
terminal states, eviction, and producer stop wherever Glial owns those behaviors.

#### Step 8.2 — Introduce Gryth incrementally

Replace one mock-backed surface at a time through the Glial provider seam:

| Surface kind | Candidate shape |
| --- | --- |
| Shared whole-value metadata | `value` |
| Presence/provider status | `atom` |
| Chat or durable history | `log` |
| Terminal/live metrics | `stream` |
| Workspace tree/query/diff | `swmr` or `snapshot_delta` |
| Collaborative document | `crdt` / `text_crdt` |

Each cutover must preserve the existing Grip consumer contract so UI components
do not learn delivery protocol details.

#### Step 8.3 — Add release and drift gates

Run IR/corpus regeneration checks, per-language tests, all matrices, and selected
consumer suites in CI. Publish a compatibility table tying contract versions to
language package versions and consumer pins.

Acceptance:

- schema or corpus drift fails before consumer release;
- every released contract has matching language packages; and
- no consumer relies on uncommitted path/hash pins.

## 6. Dependency and parallel-work map

```text
Phase 0 catalogue
    |
    +--> Phase 1 atom/SWMR stabilization --> Datascad re-pin
    |
    +--> Phase 2 shared runtime/matrix seam
             |
             +--> Phase 3 value -----> Glial/Glade value
             |
             +--> Phase 4 atom ------> first latest-state consumer
                       |
                       +--> Phase 5 stream --------> live-feed consumer
                       |
                       +--> Phase 6 SWMR/profile --> Datascad runtime
             |
             +--> Phase 7 CRDT/text -------------> collaborative consumer

All completed slices --> Phase 8 release/drift gates and Gryth cutovers
```

Within each language milestone, Rust, TypeScript, and Python implementations are
independent after schema, generated IR, corpus, and adapter surface are fixed.
Consumer integration can proceed alongside the remaining language engines once
the consumer's language and the contract are stable, but the milestone does not
complete until all 3x3 rows pass.

## 7. Standard acceptance gate for every engine shape

Every shape milestone uses the same checklist:

1. Authored IR schema and generated IR are reproducible.
2. Semantic decisions and invariants are documented.
3. Authored scenario scripts cover success, boundary, lifecycle, and failure paths.
4. The committed corpus regenerates byte-for-byte.
5. Rust, TypeScript, and Python pass the complete corpus independently.
6. Generated bindings and public APIs pass build/typecheck gates.
7. All 9 live node/client language pairings pass.
8. Normal and isolated-Python matrix modes agree.
9. Startup, protocol error, timeout, and teardown paths leak no child process or
   held stream.
10. At least one consumer adapter passes an end-to-end test, or the milestone
    explicitly records why consumer integration belongs to a later profile.
11. Unsupported shapes and tags fail closed.
12. A post-implementation review has no open correctness finding.

## 8. Immediate next change sets

With Phases 0–6 complete locally, the next reviewable increments are:

1. **CRDT convergence contract:** define the common replica envelope before the
   text specialization.
2. **Release and consumer gates:** complete applicable Glial log lifecycle
   coverage, introduce Gryth surfaces incrementally, and automate drift checks.

Do not start independent `window`, `snapshot_delta`, or `text_crdt` engines before
the Phase 0 classification. The SWMR reset-between-polls and reset-detail defects
were resolved in Phase 1; do not change that stabilized contract during engine
implementation without an authored regression and regenerated corpus.
