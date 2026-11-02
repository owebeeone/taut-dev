# Coordinated 0.11 Minor Release — CODE+SURFACE-AXIS REVIEW

**Review object:** Committed readiness source controlled by `dev-docs/CoordinatedMinorRelease-DRAFT.md` at root `5f9c4953781282a3578aa7a132e3968fbcd4ac63`, reviewed on 2026-11-03.

| Repository | Reviewed immutable commit |
|---|---|
| `taut-dev` | `5f9c4953781282a3578aa7a132e3968fbcd4ac63` |
| `taut` | `17d3820f6d2375664623e9020dbb40f86beaa49d` |
| `taut-shape-py` | `d33a069198c5540bfdd5b92b6ff22615d8113fa1` |
| `taut-shape-rs` | `e63ec55123977f6174211cdc7dfc80ad9fac513d` |
| `taut-shape-ts` | `1aaeab65e4564a462044d2f5d824cd2f375aae97` |
| Reference-only `taut-shape` | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

**Baseline:** Root `05b921181f73ca1e6a83709b1a237d87308211da`; Taut `bd93122c66c917f9144db57b048e34831e92c244`; Python shape `c08c2a1b5197f761c5b0b835c588da512130ceda`; Rust shape `8e92b89ed3a4f218a5a4e018fbfee6301fcc14b4`; TypeScript shape unchanged. Sources were read using `git show <named-SHA>:<path>` and immutable-range diffs, never moving `HEAD`.

**Date:** 2026-11-03  
**Axis:** Aggregate Code + Surface: architecture, public interfaces, packaging, compatibility, strict coverage and release execution routes. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on it. Filed verbatim by the lane owner.

**Verdict: NO-GO** — two P2 findings block. I pre-commit to GO on a revision that resolves **P2-1** and **P2-2** as specified, provided the revised tuple introduces no additional substantive changes.

---

## 0. Evidence base

The six named commit objects were resolved successfully at the beginning and again at the end. Every result matched the specified immutable tuple. No source files, Git state, registries or workflows were modified.

The public surface was read cold before the DRAFT and implementation:

- All four release repositories’ `README.md`, `RELEASE.md` and package metadata.
- Taut’s existing CLI documentation in its README.
- The new `rust/taut-foundation/README.md` in full.
- The Rust shape foundation/dependency instructions and linked Rust composition example.

Subsequent inspection covered:

- Root `AGENTS.md`, `AGENTS_GWZ.md`, the controlling DRAFT, root lock and integrity-marker diff.
- All four actual repository `AGENTS.md` and `gearu.toml` files.
- All publication workflows, including the complete new Rust foundation bootstrap workflow.
- Every changed file in the aggregate diff.
- Taut `scripts/release_checks.py` in full, particularly lines 156–241 and evidence retention in `main`.
- `scripts/release_test_ledger.py` in full; `prepare_release_workspace.py` and `release-inputs.json` in full.
- `src/tests/test_release_checks.py`, the changed platform markers, Go formatting fixes, archived-document assertion and Rust composition fixture.
- Rust foundation manifest, wrapper, provenance inventory, canonical source derivation script and runtime module references.
- Canonical/package source comparisons for `cbor.rs`, `descriptors.rs`, `ext.rs` and `validation.rs`: each pair’s complete Git-rendered contents matched.
- Rust shape’s manifest and current lock, including the explicitly pending registry transition.
- Existing parity implementation, including target selection, missing-run rejection, summary generation and `--require-all` handling.
- Read-only scratch receipts: preservation manifest, stash identity, preservation script, candidate launcher, candidate log, collection ledger, parity log and parity coverage JSON.
- Installed pytest and pluggy source showing explicit plugin loading before automatic entry-point discovery and rejection of duplicate plugin registration.

Observed scratch evidence:

- Collection recorded **2,564 tests**.
- Exactly four cases had the POSIX assignment.
- Exactly eight cases were marked duplicate parity wrappers.
- The actual parity log showed all **16 variants GREEN**, each accounting for 88 rows. Compiled targets’ three type-satisfied rows were distinguished from failures.
- The candidate’s tests were still running at the last inspection. No complete strict-test success is claimed here.
- No tests or builds were independently executed: the command allowlist authorized inspection only. Finding reproductions below are deterministic source traces and specified regression cases.

## Problem, requirement provenance, and scope

The requested outcome is a coordinated minor release of Taut and the three implemented shape libraries, through Gearu and repository publication workflows, followed by clean public-registry consumption and final workspace receipts.

The canonical prompt records the original human authorization: voice message `01a19e23-1077-7e23-a22f-d40b70f84683` in chat `01a19bfc-e75f-70e1-b214-35ca98a679f1`, following an explanation naming all four repositories and registry destinations. The parent verified that authority directly. This review treats that recorded authorization as authority for the specified release and necessary readiness fixes.

The observed prerequisites are supported by the sources:

- The shape Rust package already depends on the foundation owner. The old development workspace supplied it through a local patch while the foundation manifest prohibited publication. That supported development route does not provide a registry dependency for a published shape crate.
- Publishing the existing canonical foundation is therefore a bounded prerequisite for the requested Rust registry release. It does not introduce another runtime implementation.
- The Python dependency range must move with the 0.11 train.
- Windows-specific filesystem cases and POSIX shell/symlink cases require qualified complementary hosts to obtain their union without skips.
- Immutable sibling inputs are necessary for composition tests in Gearu’s isolated candidate and publication CI.

Localized remedies were used: metadata and packaging for the existing foundation, removal of the development patch, dependency-range correction, immutable input preparation, four platform assignments, LF output for formatting probes and correction of an archived document path.

Source-only consumers remain a supported alternative for their own applications, but that alternative does not satisfy publication of the existing Rust shape package with a usable registry foundation dependency.

The authorized editable components are the four release repositories and their necessary release infrastructure, plus root readiness documentation and GWZ receipts. The contract repository is reference-only. The aggregate diff does not touch protected authoring files, unfinished language libraries or unrelated members.

The preservation receipts identify the exact 35 paths, their prior hashes and stash `23d45758f2a73de865dacc2ebc68e6dc9ef22ed6`; the preservation script checks stash-object bytes before recording success. I inspected these receipts and the script, but did not independently rehash the artifacts. The protected enum authoring commit remains visible in the reviewed Taut ancestry.

No unauthorized prerequisite or scope expansion was established. Foundation preflight, real publication, registry lock completion and final consumer runs remain execution gates; their pending state alone is not a defect in this readiness package.

## 1. Findings

### [P2-1] Explicit xdist loading conflicts with pytest’s default plugin discovery

**Location:** Taut `scripts/release_checks.py:191–195`, especially `'-p', 'xdist.plugin'`; `source_env()` at lines 79–85. Public strict-gate instructions are in `RELEASE.md:158–188`.

**Violated invariant:** The documented release command must work with its declared dependencies and documented environment requirements. Required plugins must load once under the normal defaults.

**Reproduction/state sequence:**

1. Use the declared pytest/pytest-xdist environment on Windows.
2. Configure the documented WSL Python requirement.
3. Leave `PYTEST_DISABLE_PLUGIN_AUTOLOAD` unset, pytest’s normal default.
4. Run the strict tests step.
5. Its explicit `-p xdist.plugin` imports and registers the module under `xdist.plugin`.
6. Pytest subsequently discovers pytest-xdist’s `xdist` entry point and attempts to register that same module under `xdist`.
7. Pluggy raises `ValueError: Plugin already registered under a different name`, before the native partition executes.

The inspected pytest source performs command-line plugin loading before entry-point autoloading; the inspected pluggy source rejects registering an existing module under another name.

The current scratch launcher sets `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`, masking this failure. The committed command neither establishes that setting nor documents it as a prerequisite.

**Impact:** The public release/readiness route fails before its required native execution under the ordinary environment. A successful specially configured scratch run does not establish that the committed interface works as documented.

**Required correction:** Load xdist by its entry-point name (`-p xdist`) so explicit loading and automatic discovery agree, or make plugin isolation an explicit, consistently enforced property of the gate itself. Preserve operation when automatic discovery is disabled.

**Closure/regression test:** Exercise the constructed pytest invocation in a small isolated pytest/xdist environment with autoload both enabled and disabled. Both must start successfully, expose `-n`, load the ledger and execute a trivial case once without duplicate-registration errors.

### [P2-2] The execution ledger cannot prove exactly one complete phase sequence

**Location:** Taut `scripts/release_test_ledger.py:18–31`; `scripts/release_checks.py:156–173`, especially line 167.

**Violated invariant:** Every required case must execute exactly once, with passing setup, call and teardown; omitted or repeated execution must fail qualification.

**Reproduction/state sequence:**

- Give `verify_test_coverage` a matching source hash, successful exit status, the correct selected case and this phase record:

  ```json
  {"case": {"call": "passed"}}
  ```

  It accepts the record. `phases.get('call')` is passing and the set of existing outcomes is `{"passed"}`, although setup and teardown evidence is absent.

- Deliver two complete passing setup/call/teardown report sequences for the same node ID to `pytest_runtest_logreport`. Every event in the second sequence overwrites the first because the ledger stores one value per `(nodeid, phase)`. The resulting ledger is indistinguishable from one execution and the verifier accepts it.

These are direct consequences of the collector and validator; no external failure or tool absence is required to demonstrate the acceptance.

**Impact:** The machine-readable evidence does not establish the exact-once, complete-phase condition used to justify the Windows/WSL split. The current checks reject missing case IDs and differing hosts, but cannot detect missing phase reports or repeated execution within a partition. The DRAFT and RELEASE claims are stronger than the implemented gate.

**Required correction:** Preserve report cardinality or a lossless event sequence, and require exactly one passing setup, one passing call and one passing teardown for each assigned case. Reject repeated phase reports and incomplete phase sets. Keep repeated worker collection notifications separate from execution counts.

**Closure/regression test:** Add negative cases for omitted setup, omitted teardown, repeated passing call, a repeated complete execution and a failed outcome followed by a passing outcome. Each must fail. A real xdist partition plus its POSIX complement must then produce a complete accepted ledger with one phase sequence per required case.

## 2. Invariant analysis

The following attacks did not establish additional defects:

- **Foundation source ownership and closure:** The four derived runtime files match their canonical counterparts. The crate wrapper exposes the actual codec-owned descriptors and optional validation module. The inspected module paths remain inside the packaged source closure.
- **Package independence:** The foundation include inventory contains source, manifest, README, license and provenance. No sibling include or runtime dependency was found.
- **Version ownership:** Gearu’s Rust adapter owns the foundation manifest version. The Rust composition fixture reads that manifest version instead of retaining a fixed 0.10 dependency.
- **Registry transition:** The Rust shape dependency moves to 0.11 and removes the local workspace patch. Its old lock is visibly unfinished, and the DRAFT explicitly blocks completion on initial foundation publication. This requires the promised final tuple check, rather than being concealed as completed work.
- **Python train alignment:** Python shape requires `taut-proto>=0.11.0,<0.12`, permitting independent compatible patch releases within the train.
- **Immutable composition inputs:** Taut pins four sibling commits; preparation checks commit identity and tracked cleanliness, creates LF checkouts and installs frozen TypeScript dependencies. Publication CI uses that same manifest.
- **Parity coverage:** The mandatory command retains `--require-all`; the inspected implementation rejects missing selected runners. The scratch receipt records the complete 16-variant, 88-row result.
- **Wrapper accounting:** The collection receipt identifies the eight existing parity wrappers separately. The actual parity run supplies their intended coverage.
- **Platform scope:** Four cases are assigned to POSIX. Windows filesystem and namespace cases remain in the native partition. The changed markers do not weaken their assertions.
- **Bootstrap credential locality:** The secret is injected only into the presence check and publication step. Source verification and tests run before credential exposure. No source-level credential disclosure was found.
- **Foundation release identity:** Publication requires a full source SHA, matching manifest identity/version and a matching immutable Taut tag.
- **Release ordering:** Documentation holds Taut’s GitHub Release/PyPI publication until foundation succeeds, then releases the dependent libraries. It prohibits local registry publication and tag reuse.

## Surface

The new foundation README identifies its purpose, default feature behavior, dependency coordinate and nominal-identity requirement. It explicitly distinguishes the compiler from the runtime owner and states that generation does not install dependencies. Its migration note does not promise compatibility with earlier local owners.

Rust shape’s changed README presents the registry route and explains sharing the same actual crate identity. Existing source composition examples remain usable as development examples, although their historical “unpublished” wording should not be used as the final public release receipt.

The new WSL variables have a stated purpose and distro default. The public strict-gate surface nevertheless has the undeclared plugin-environment dependency in **P2-1**, and its promised complete execution accounting is not enforced because of **P2-2**.

Installation and removal remain ordinary package-manager lifecycles; this change adds no custom installer or uninstall state. Actual public-index installation, generated codec/descriptor use and validation OFF/ON consumption remain mandatory post-publication evidence.

## 3. Risks and next action

Foundation credential presence does not establish new-crate publication scope. Bootstrap preflight and actual publication remain necessary. A failure after registry upload must be reconciled against the immutable published artifact before retrying; tag movement is not an acceptable recovery.

The full candidate run, supported-Python publication matrix, real registry lock refresh, clean registry consumers, preservation restoration and final GWZ/remote receipts were not complete at this review snapshot. They remain release completion conditions.

**Next action:** Apply one bounded correction for **P2-1** and **P2-2**, obtain this originator’s closure check at the revised immutable tuple, and rerun the full qualified gate before advancing publication.
