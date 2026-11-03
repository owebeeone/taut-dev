# Taut 0.11.1 corrective release

Status: **settled corrective source0258b49e92c8b4ccd95027b4b10ad0b2f3992c52;
source acceptance and exact Gearu qualification pending**.

The original coordinated-release authorization includes necessary readiness
corrections. Subsequent explicit steering authorizes this minimal0.11.1 compiler
path, independently retaining the already published foundation and three shape
coordinates0.11.0. No new routine version approval is required.

## Observed failure and immutable version boundary

Taut's public v0.11.0 remains9260da45f486ed5a57aa399788c2936f2c044619. Its
publication41557714352 terminated FAILURE: all four Python3.10–3.13 test jobs
failed; build and PyPI jobs were skipped. No taut-proto0.11.0 was uploaded.
The complete original log is retained as taut-v0110-publication-failed.log under
D:/projects/limbo/coordinated-release-2026-11-03. Python3.12 specifically reports
170 failed,2306 passed,66 skipped,30 errors; those are the failed CI run's counts,
not the earlier strict qualification or a later corrected candidate's counts.

Actual package defect: _is_alias calls lstat on a child of a regular-file
obstruction. POSIX Python3.12 raises NotADirectoryError, escaping the promised
preflight ValueError. This was independently reproduced with unmodified source
on WSL Python3.12.3. The one-line correction treats ENOTDIR like a missing leaf;
the existing canonical-path parent walk then rejects the obstructing parent
before any mutation. Permission/other I/O errors remain unhandled failures.
Go and Java's original tests exposed it. Two new cross-platform regression cases
simulate the older pathlib behavior through the actual Go/Java canonical-path
call graph, assert ValueError and preserve the handwritten obstruction/tree.
Both pass natively; actual Python3.12.3 Go/Java probes pass after correction.

The old public tag and all registry artifacts are immutable. The fixed Python
package must be0.11.1. Foundation0.11.0 and Rust/TS shape0.11.0 are already public;
Python shape remains0.11.0 with its accepted dependency range>=0.11.0,<0.12.
Taut's existing0.11.0 GitHub Release is held/superseded for PyPI, not repointed.

## Compiler/environment classification

The CI TypeScript failures include absent tsc/None executables. The frozen
sibling already installs its declared compiler; its node_modules/.bin is now
placed on GITHUB_PATH, and tsc --version is required before testing.

The C++ first diagnostic is libstdc++15 type_traits:1459: incomplete
std::pair<long long,taut::Cbor> used in a type-trait expression, recursively
reached through vector destruction/default construction and pair's conditional
default-constructor traits. This is independently reproduced without Taut by:

```cpp
#include <vector>
#include <utility>
struct Node { std::vector<std::pair<int, Node>> values; };
int main() { Node value; return value.values.size(); }
```

Using Clang21.1.6, x86_64-linux-gnu syntax checking, authentic Ubuntu
libstdc++15.2.0-16ubuntu1 headers and the WSL glibc headers, that standalone case
fails with the same diagnostic. GCC13.3 accepts the standalone case with those
headers; this is diagnostic isolation, not qualification of a GCC13/lib15
whole toolchain (the full header also hits newer optional features unsupported
by GCC13). The unchanged actual Taut header passes Clang21.1.6/libstdc++13 and
GCC13.3/libstdc++13, plus the prior Clang21/MSVC and MSVC native gates. Its raw
cbor.hpp blob is unchanged even from public v0.10.1, as well as from v0.11.0.

This provides a concrete non-Taut compiler/standard-library compatibility
failure rather than a new generator/runtime defect. The release CI explicitly
selects Ubuntu24.04, Clang18 and libstdc++13 through --gcc-install-dir. It requires
the actual versions/tools and runs the same tests; no test is deselected or
relabeled. The original two reviewers must assess this qualification boundary.
The C++ runtime, ABI, aggregates, constructors and canonical bytes are unchanged.
Failed scratch-only header experiments did not enter the source patch.

The two Go harness errors are Go's cgo-enabled scan rejecting co-located
foundation.cpp in the multi-language resource directory. CI explicitly selects
CGO_ENABLED=0, matching the qualified pure-Go runtime route; no Go source is
changed. This is test-tool setup, not a copied/mutated published package.

## Independent foundation version

The Cargo manifest and every Rust canonical source/provenance file remain
identical to v0.11.0. Remove only the Gearu Rust version adapter that would
otherwise manufacture foundation0.11.1 for a Python-only patch. Keep all
canonical sync, standalone cargo test/package and exact-check gates.
Gearu plan0.11.1 explicitly reports no metadata changes and a tag-derived
Python version; foundation stays0.11.0. Generated package-mode Rust still binds
taut_foundation with the same descriptor/codec/validation contract and canonical
snapshot; final public consumers must use actual registry foundation/shape0.11.0
with the public taut-proto0.11.1 compiler, without local patches/source runtimes.
No foundation reupload or temporary-token reuse is permitted.

## Exact delta, review and remaining gates

Five Taut files differ from9260da4: python_runtime.py, its real-call-graph
regressions in test_python_runtime_distribution.py, publish.yml tool selection,
gearu.toml independent-version policy, and RELEASE.md explaining the tuple.
No other implementation, user file, unrelated member or published artifact changes.

The same two original reviewers perform bounded Code+Surface and State review
of this exact correction, reproduction evidence and public version boundary.
This is a focused source/policy correction, not another review of all accepted
nine-language implementations. GO accepts this source only; Gearu must then
qualify the exact0.11.1 candidate through its full configured gates before tag
publication. Preserve failed logs and source association. If source changes
after acceptance, return to the same originators for the changed range.

After qualification, Gearu creates/pushes immutable v0.11.1 and its GitHub Release.
Require all four supported-Python jobs and publication terminal-success, public
PyPI0.11.1, Python shape's actual installed-registry Gearu checks and0.11.0
workflow, fresh public Python/Rust/npm OFF/ON consumers and artifact checks,
then original-reviewer completion evidence and final GWZ remote receipts.

The exact35 artifacts are restashed in cad981df4cabc771c91c0530db0f2bcd90caa263
for the clean candidate, with unchanged hashes and earlier stashes retained.
Restore and rehash35 plus the protected five at the final boundary. enum.case
and unrelated/contract member heads remain preserved. No full-train completion
is claimed by this corrective source checkpoint.
