# Taut 0.11.1 Corrective Source — CODE+SURFACE-AXIS REVIEW

**Review object:** Taut `0258b49e92c8b4ccd95027b4b10ad0b2f3992c52`, controlled by `dev-docs/TautV0111CorrectiveRelease-DRAFT.md` at root `1fc9e8101a7cf68b0ec8847e52a8126315fc0720`.

**Baseline:** Immutable Taut `9260da45f486ed5a57aa399788c2936f2c044619`. Sources were read through named Git objects and the complete five-file diff.

**Date:** 2026-11-03  
**Axis:** Same-originator Code + Surface. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on its report. Filed verbatim by the lane owner.

**Verdict: GO** — no blocking source findings. This accepts the correction for full candidate qualification. It does not certify completion of that qualification, publication CI or registry consumers.

---

## 0. Evidence base

The exact tuple matched at the beginning and end:

| Component | Commit |
|---|---|
| Root | `1fc9e8101a7cf68b0ec8847e52a8126315fc0720` |
| Taut | `0258b49e92c8b4ccd95027b4b10ad0b2f3992c52` |
| Rust shape | `7f2a60747901fcf15362ab3c9a8af65c20faad68` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| TypeScript shape | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Read changed RELEASE.md, Gearu configuration and workflow cold, then the controlling DRAFT, complete diff, shared path helper and actual Go/Java canonical-path callers.

Inspected the failed publication diagnostics, obstruction probe, two committed regressions, standalone recursive-pair probe, Cbor/compiler probe logs, Gearu plan, Rust package binding and unchanged foundation manifest/provenance.

The DRAFT records two native focused passes and an actual Python 3.12.3 obstruction-probe pass; their implementations were inspected. No tests or builds were independently executed here.

Git blob comparisons confirmed:

- `cbor.hpp` is identical across public `v0.10.1`, `9260da4…` and this correction.
- Foundation manifest/provenance and inspected Rust canonical runtime files are unchanged from `9260da4…`.

## Problem, requirement provenance, and scope

Original human release authority includes necessary readiness corrections. Subsequent explicit steering authorizes compiler `0.11.1` while retaining foundation and compatible shape coordinates `0.11.0`.

The observed package defect is concrete: older POSIX pathlib raises `NotADirectoryError` when `_is_alias` examines a child beneath a regular file. This escapes the intended preflight rejection. Failed CI also exposes unavailable TypeScript tooling, Go harness configuration and a particular C++ compiler/library incompatibility.

The five-file correction addresses those failures locally. It changes no canonical runtime, wire format, generated ABI, protected authoring file or unrelated member. No new architectural remedy or unauthorized prerequisite was established.

## 2. Invariant analysis

**Obstruction safety remains intact.** `_is_alias` additionally catches only `NotADirectoryError`; permission and other I/O failures are not broadly suppressed. Go/Java still inspect every lexical parent before physical normalization and reject the regular-file obstruction with `ValueError`, before writes. The regressions exercise those actual callers and preserve the handwritten file/tree.

**Compiler evidence supports bounded qualification.** The non-Taut recursive-pair example reproduces the same incomplete-pair diagnostic with Clang 21/libstdc++15. The evidence supports a pairing incompatibility; it does not by itself establish a compiler bug or universal source conformance.

The actual unchanged header passes the recorded libstdc++13 pairings. The isolated GCC13/lib15 recursive-pair success is correctly distinguished from the failed whole-header GCC13/lib15 experiment.

**Coverage is retained.** Ubuntu 24.04, installed GNU13 tools and the explicit Clang18/libstdc++13 wrapper provide qualified routes without editing or deselecting C++ tests. Some helpers prefer `c++` before `clang++`; this review does not claim every invocation selects the wrapper. Actual matrix execution remains required.

The workflow exposes the frozen sibling TypeScript compiler and requires its version command. `CGO_ENABLED=0` selects the existing pure-Go route without changing Go runtime code.

**Independent foundation versioning is coherent.** Removing only Gearu’s Rust version adapter prevents an unnecessary foundation `0.11.1`. Canonical synchronization, Cargo tests/package checks and exact checks remain. Foundation stays `0.11.0`; generated Rust package bindings retain the same owner/contracts. Python shape’s `>=0.11.0,<0.12` range admits compiler `0.11.1`.

## Surface

RELEASE.md explains the corrective compiler coordinate, retained public tag, independent foundation identity and CI prerequisites. It prohibits tag replacement and gratuitous foundation reupload. Existing migration limits remain honest; this patch adds no runtime ownership interface.

## 3. Risks and next action

Run the complete configured Gearu candidate for this exact source: strict Windows/WSL union, all-sixteen parity, package build and raw-byte smoke. Then require terminal success across Python 3.10–3.13 publication CI and fresh public registry consumers.

Earlier qualification remains attributed to its original source. Final restoration/rehashing of the exact35 artifacts and protected five, followed by final workspace receipts, remains required.
