# Taut Shape Engine Adapter Contract

Status: Steps 2.1 and 2.2 implemented locally for `log` and `value` in Rust,
TypeScript, and Python.

Date: 2026-08-22

Authority: this document defines the shared shell/adapter boundary used by the
taut-shape conformance tools. Shape semantics remain authoritative in each
shape contract and oracle.

## Purpose

The conformance shell MUST be reusable across shapes without importing a log
cursor, log lifecycle state, or another shape-specific message type. A shape
adapter owns all translation between its wire messages and its state machine.
The shared runtime owns only ordered dispatch and effect collection.

## Minimal contract

Each language expresses the same generic contract using its natural type
system. An adapter MUST provide:

1. `shape`: the exact canonical shape name.
2. `decode_input(frame)`: validate direction and decode one inbound frame into
   the adapter's private input type.
3. `dispatch(input)`: apply one decoded input to the shape-local state machine
   and return ordered private outputs.
4. `encode_output(output)`: turn one private output into an outbound frame and
   annotate any timer or teardown effect.
5. `finish()`: perform end-of-input teardown and return ordered final outputs;
   the `log.v0` implementation currently returns none.

The shared runtime MUST call these operations in the order above for each
frame. It MUST NOT inspect message tags, cursors, payloads, lifecycle states, or
shape-specific output variants.

An encoded emission contains:

- the original private output, for shape-specific transcripts where required;
- exactly one encoded outbound frame;
- zero or one shape-neutral timer action (`set(token, delay_ms)` or
  `cancel(token)`); and
- zero or one shape-neutral teardown request carrying an opaque reason.

Timer and teardown annotations do not replace the conformance wire frame. The
current CLI MUST continue to emit the same `set_timer`, `cancel_timer`, and
`producer_stop` frames byte-for-byte. A future in-process host MAY consume the
annotations to operate its scheduler and ownership layer.

## Registry and diagnostics

Runtime support MUST be exact and fail closed. The implemented registry
contains `log` and `value`; catalogue membership does not imply an implemented
engine adapter.

The boundary uses typed diagnostics with stable codes:

| Code | Meaning |
| --- | --- |
| `TAUT_SHAPE_UNSUPPORTED_SHAPE` | No adapter is registered for the requested shape. |
| `TAUT_SHAPE_UNKNOWN_TAG` | A complete frame contains a tag absent from the selected shape's tag map. |
| `TAUT_SHAPE_MALFORMED_MESSAGE` | The body cannot be decoded as the message selected by its tag. |
| `TAUT_SHAPE_DIRECTION_VIOLATION` | A known output-only message arrived on the engine input channel. |
| `TAUT_SHAPE_ADAPTER_FAILURE` | An adapter invariant failed outside the preceding categories. |

Unknown shape selection MUST fail before an engine is constructed or input is
read. Unknown tags and direction violations MUST fail before engine dispatch,
so rejected input cannot mutate shape state.

## Language mapping

| Language | Generic shell | `log` adapter | `value` adapter |
| --- | --- | --- | --- |
| Rust | `taut-shape-tool/src/runtime.rs` (`EngineAdapter`, `EngineRuntime`) | `node.rs::LogAdapter` | `value_tool.rs::ValueAdapter` |
| TypeScript | `src/runtime.ts` (`EngineAdapter`, `EngineRuntime`) | `src/log/adapter.ts` | `src/value/adapter.ts` |
| Python | `taut_shape/tool/runtime.py` (`EngineAdapter`, `EngineRuntime`) | `taut_shape/tool/log_adapter.py` | `taut_shape/tool/value_adapter.py` |

Associated/generic types keep the contract independent of `LogInput`,
`LogOutput`, `LogCursor`, and `LogState`. Implementations MAY retain
shape-specific routing context inside the adapter; for `log`, this is the
per-stream `log_id` echo map.

## Compatibility gate

Steps 2.1 and 2.2 remain complete only while:

- all existing log oracle and CLI tests remain green;
- the 36 live log matrix rows remain transcript-compatible;
- each language proves an unknown shape is a typed diagnostic;
- each language proves an unknown tag is a typed diagnostic; and
- a contract test uses non-log placeholder input/output types, demonstrating
  that the shared runtime has no log cursor or lifecycle dependency.

## CLI selection (Step 2.2)

The Rust, TypeScript, and Python `node` and `client` modes accept
`--shape <name>`. Selection defaults to `log` for backward compatibility and
is resolved against the exact runtime registry before an engine is constructed,
input is read, or a client session writes its first frame. Every CLI advertises
the same implemented names (`log`, `value`) and rejects all other names with
exit status 2 and `TAUT_SHAPE_UNSUPPORTED_SHAPE`.

The selected adapter owns its message-tag map. Adding a catalogue name to a
declaration or document does not make it selectable; a working adapter must be
registered in every language first.
