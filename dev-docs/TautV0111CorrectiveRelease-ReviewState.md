# Taut 0.11.1 Corrective Source — STATE-AXIS REVIEW

**Review object:** Five-file corrective source `0258b49e92c8b4ccd95027b4b10ad0b2f3992c52`, controlled by `dev-docs/TautV0111CorrectiveRelease-DRAFT.md` at root `1fc9e8101a7cf68b0ec8847e52a8126315fc0720`. Full candidate qualification remains pending.

**Baseline:** Immutable Taut 0.11.0 source `9260da45f486ed5a57aa399788c2936f2c044619`. Inspection used exact Git objects and the complete baseline-to-correction diff.

**Date:** 2026-11-03

**Axis:** State — fail-closed path preflight, immutable versions, qualification boundaries and preservation. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: GO** — source acceptance only. No blocking finding or new architectural root cause was established. Release requires the unchanged source to pass all mandatory qualification and publication gates.

---

## 0. Evidence base

Verified the tuple at start and end:

| Component | Commit |
|---|---|
| Root | `1fc9e8101a7cf68b0ec8847e52a8126315fc0720` |
| Taut correction | `0258b49e92c8b4ccd95027b4b10ad0b2f3992c52` |
| Rust shape | `7f2a60747901fcf15362ab3c9a8af65c20faad68` |
| Python shape | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| TypeScript shape | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

Read the canonical prompt, controlling DRAFT, complete five-file diff, shared `_is_alias`, actual Go/Java canonical-parent walks, regression cases, publication tool selection, Gearu configuration and plan.

Inspected the original publication failure log and Python 3.12 job diagnostics; Python 3.12 obstruction probe; minimal C++ probes and retained compiler diagnostics. The DRAFT records two native regression passes and the actual Python 3.12.3 probe pass.

Confirmed `cbor.hpp` has no diff from public v0.10.1. Foundation manifest, canonical inventory and Rust package bindings are unchanged from 0.11.0. The existing Taut `v0.11.0` still resolves to `9260da4`. The current preservation stash contains the expected 35 files.

No tests, builds, writes, registry actions or credential access were performed.

## Problem, requirement provenance, and scope

The original release authority includes necessary readiness fixes. Subsequent explicit steering authorizes compiler 0.11.1 while retaining foundation and shape coordinates at 0.11.0.

The observed package defect is concrete: older POSIX pathlib raises ENOTDIR while checking a child beneath a regular-file obstruction, escaping the intended preflight `ValueError`. The correction addresses that error locally.

Missing TypeScript compiler discovery, Go’s cgo scan and the demonstrated C++ compiler/library incompatibility support bounded CI-environment corrections. No runtime rewrite or test deselection is necessary. The five changed files remain within authorized scope.

## 2. Invariant analysis

**Obstructed parents remain rejected before writes.** Catching `NotADirectoryError` classifies the inaccessible child as a non-alias; it does not authorize creation beneath it. Both actual canonical-path functions continue walking lexical parents, encounter the regular file and raise the obstructed-directory error before mutation or physical resolution.

The new regressions exercise that shared guard through Go and Java, asserting `ValueError`, unchanged handwritten bytes and no additional tree entries. Alias checks remain active; permission and other I/O exceptions are not newly swallowed.

**Toolchain selection does not weaken assertions.** The isolated recursive-pair program reproduces the same incomplete-type diagnostic without Taut. This supports a compiler/standard-library compatibility classification; it does not establish standards compliance or assign a compiler bug. The failed GCC13/libstdc++15 whole-header experiment remains explicitly failed, distinct from the isolated-pair result.

CI selects Ubuntu 24.04, installs Clang18/GCC13, supplies Clang’s explicit GCC13 directory, exposes the frozen sibling TypeScript compiler and sets pure-Go mode. Runtime sources and test selections remain unchanged. Actual hosted execution remains mandatory.

**Version identity remains coherent.** Removing only Gearu’s Rust version adapter prevents an unnecessary foundation 0.11.1 release. Canonical synchronization, Cargo test/package and exact checks remain configured. Foundation stays 0.11.0; generated Rust package bindings retain its owner. Python shape’s `>=0.11.0,<0.12` range admits compiler 0.11.1.

The failed 0.11.0 publication is not relabelled as success, and its tag is not replaced. Historical strict results are not qualification for this correction.

**Preservation is explicit.** Protected files and unrelated members are outside the diff. The DRAFT names the reversible stash and leaves final restoration/rehashing pending.

## 3. Risks and next action

Run the complete configured Gearu 0.11.1 candidate on this exact source, retaining source hashes, full native/WSL coverage, all-sixteen parity and strict package/smoke receipts.

Then require supported-Python CI, actual PyPI publication, Python-shape registry checks, fresh public consumers and final preservation/GWZ evidence before declaring completion. Do not republish foundation or move the 0.11.0 tag.
