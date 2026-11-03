# Final Release Receipt and Future Python 3.15 CI — CODE+SURFACE-AXIS REVIEW

**Review object:** Root `2b39a54a24a1b9e6c9d337b2a564d5a9c722c3e6`, its completion/evidence records, and the two future Python CI additions.

**Baseline:** Published Taut `0258b49e92c8b4ccd95027b4b10ad0b2f3992c52` and Python shape `d33a069198c5540bfdd5b92b6ff22615d8113fa1`. Sources were inspected through immutable Git objects and complete diffs.

**Date:** 2026-11-03  
**Axis:** Same-originator Code + Surface. Independent, adversarial, read-only. The other axis runs in parallel; nothing here relies on its report. Filed verbatim by the lane owner.

**Verdict: GO** — no blocking findings. The completion receipt and two future-CI commits are acceptable. Final dual acceptance and checked GWZ remote publication remain the owner’s next gate.

---

## 0. Evidence base

All ten named root/member HEADs matched the canonical tuple at the beginning and end. Principal reviewed heads:

| Component | Commit |
|---|---|
| Root | `2b39a54a24a1b9e6c9d337b2a564d5a9c722c3e6` |
| Future Taut CI | `fcfbe0cfface9241c2b68542973936a166a0c8bc` |
| Future Python shape CI | `0488516aa1a5db94da44fdb10f12a7ec5bfd5940` |
| Rust shape | `7f2a60747901fcf15362ab3c9a8af65c20faad68` |
| TypeScript shape | `79d3899b91af843b2295d089c82f6547ef97fde8` |
| Reference contract | `89916c4d017123d7c16f094eb2fba6ece98facc0` |

The four unrelated member heads also matched FinalSourceProof.json.

Read Completion/Status and changed workflows cold, then Final-DRAFT, FinalEvidence, FinalSourceProof, PublicArtifacts, PublicConsumers, FinalRegistries, Python315, availability evidence and both JUnit files. Inspected verification scripts and supporting consumer, qualification and failed/retry logs.

Independent read-only `gh run view` checks confirmed terminal **completed/success** for:

- Compiler `41561903710`, source `0258b49…`.
- Python shape `41564573410`, source `d33a069…`.
- Rust shape `41558306131`, source `7f2a607…`.
- TypeScript shape `41537841200`, source `79d3899…`.
- Foundation `41536859807`, reviewed publisher `506b60e…`, successful second attempt.

No tests, builds, writes, publication actions or credential retrieval were performed.

## Problem, requirement provenance, and scope

The original human instruction authorized the coordinated release and its publication, consumer and preservation checks. Later steering authorized compiler `0.11.1` while retaining runtime coordinates `0.11.0`. The latest human follow-up explicitly requested future Python 3.15 coverage.

The implementation follows that bounded request: each Python workflow changes exactly one matrix line, adding one `3.15` entry. Existing `3.10–3.13`, integration commands and failure behavior remain unchanged. No `3.14`, runtime modification, new package version or replacement tag is introduced.

The release and preservation evidence addresses the requested completion outcome. No unsupported prerequisite, unauthorized expansion or new architectural root cause was established.

## 2. Invariant analysis

**Published sources remain immutable.** Tag checks distinguish compiler `v0.11.1` at `0258b49…`, historical compiler/foundation source `v0.11.0` at `9260da4…`, and shape `0.11.0` sources from future CI-only HEADs. Compiler `0.11.0` remains intentionally absent from PyPI.

**Qualification is accurately attributed.** Compiler `0.11.1` records 2,566 required passes, including 2,562 native and four POSIX cases, eight separately accounted wrappers, sixteen parity variants and the complete build/smoke checks. Ordinary hosted platform skips are not represented as strict qualification.

**Artifact checks are substantive.** Verification compares downloaded PyPI wheels/sdists with registry hashes and workflow artifacts, npm SHA1/SHA512 and source identity, and Rust VCS identities plus complete archive payloads. Foundation’s independently repacked compressed bytes remain explicitly unequal; its twelve payload entries match. Rust shape’s 31-entry payload and compressed checksum match.

**Public consumers use public packages.** Fresh Python/Rust/npm consumers use public compiler `0.11.1` and runtime owners `0.11.0`. Inspected checks cover OFF/ON generation, execution, descriptors, codec behavior and shared ownership. Rust metadata rejects path/git runtime substitution; npm checks CJS/ESM owner identity.

**Python 3.15 claims remain bounded.** JUnit contains exactly **1,052** selected Taut cases and **190** shape cases, with zero failures/errors/skips. Public-package OFF/ON execution also passed. The initial capture-storage failure remains separately recorded; the dedicated-temporary-directory retry supplies the passing evidence. These are local checks, not completed future hosted jobs.

Official sources confirm stable 3.15.2 and suitable Actions assets. [Python release](https://www.python.org/downloads/release/python-3152/), [pinned Actions manifest](https://raw.githubusercontent.com/actions/python-versions/160ca1e232997f36def6bb6e857f628222bef58a/versions-manifest.json).

**Preservation remains explicit.** The inspected proof verifies all original 35+5 hashes, ancestry and retained stashes. Current Taut status contains exactly the expected 35 untracked artifacts and no tracked changes. Unrelated/reference heads remain unchanged.

## Surface

Completion and Status distinguish public release success, historical failures, future CI heads and pending root publication. They disclose actual compiler selection, independent foundation versioning, consumer isolation and archive-comparison limits without implying unrun hosted 3.15 success.

## 3. Risks and next action

File both reports verbatim, merge final acceptance, then push the two ordinary CI commits and managed GWZ root using the required checked-remote proof. Retain the accurate untracked-artifact warning and historical evidence. No further release, implementation review or credential action is required by this object.
