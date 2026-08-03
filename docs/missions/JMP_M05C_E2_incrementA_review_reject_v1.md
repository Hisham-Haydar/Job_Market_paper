# JMP-M05C E2 Escalation — Increment A Review REJECT v1

**Mission:** JMP-M05C — Minimal Streaming Inference Implementation
**From:** Goal 1 Manager — Empirical JMP  **To:** ChatGPT Deputy Programme Director
**Date:** 2026-08-02
**Halt trigger:** charter §6 — Review A verdict REJECT (five required fixes; REJECT is an E2 halt; the per-increment budget of one narrow remediation attaches only to APPROVE AFTER FIXES)
**Target repository path:** `docs/missions/JMP_M05C_E2_incrementA_review_reject_v1.md`

## 1. State at halt

Implementation base `b5169293…` (addendum committed on the clean post-closeout base `ffd060f7…`). Increment A delivered the streaming score reducer with the reviewer confirming: genuine production loader/likelihood/reducer under test with source hashes matching the committed inventory; numerical conformance passing the design-frozen T-11/T-16 bars including the first-64 canonical check (margins 10⁴–10⁶); bitwise-consistent 35×35/37×37 meats with by-name authenticated selection; no smuggled runner/transaction/covariance surfaces; correct non-scope. Rulings R-32a/b/c were adjudicated and upheld under real reviewer probes (R-32a conditionally). Nothing committed beyond the addendum pre-step; no full-population run; no persistence on the successful path.

## 2. The five findings (all implementation/test/report/state level; none touches design, package, or architecture)

1. **NP-1 (blocking):** a failed reducer call leaves the transient `(batch, 37)` score array reachable through the exception object graph (`__traceback__` frames); the shipped no-persistence test checked messages and files only — a false-green against the addendum's failure-path requirement.
2. **DG-1 (blocking):** the reducer silently truncates non-integral batch IDs before hashing; a forged `.5` identifier digests as its truncated integer, contradicting the published `int64_le` contract. Its fix is also the condition the reviewer attached to freezing R-32a at Increment C.
3. **T16-1:** the shipped T-16 test uses 24 households where design v4 freezes the first 64; the reviewer's own first-64 run passes, so this is test/report conformance, not numerics.
4. **PR-1:** the PROOFS packet is not verbatim-reproducible (missing interpreter/activation command; two stale test counts; one proof requiring a reviewer-created file; edit-based red-bar demonstrations incompatible with a read-only reviewer).
5. **ST-1:** four unexpected test-29 attempt files violated the exact expected state. Root cause is a Goal-1 process error, owned: the authorized deletion was issued as a human pre-step outside any gated prompt and was not executed before the review launched — repeating a failure mode already codified against after M05B. Corrective rule below.

## 3. Assessment

This is the redesigned process working, not failing. Defect classes that took JMP-M05B four full-implementation review rounds to surface were caught at increment 1, at minimal scope, before any covariance or runner code exists, with a closed and well-specified fix list. The reviewer's REJECT is correct under the charter's letter — five fixes exceed one narrow remediation — while its own §10 prescribes precisely the remedy: complete the five fixes, restore exact state, submit a fresh independent Review A.

## 4. Requested deputy decisions

1. **Authorize one bounded Increment-A refix** implementing exactly the five required fixes from Review A §9, executed by the same fresh implementer session, followed by a **fresh independent Review A (v2)** by a fresh Codex session. No scope beyond the five; design v4, the addendum, and the package remain untouched.
2. **Adopt the corrective process rule mission-wide:** every state disposition (deletions, moves, reconciliations) is executed inside the gated task prompt as a verified step, never as a human pre-step; and every full-suite command in every M05C card carries the test-29 deselection explicitly.
3. **Optional standing amendment for Increments B/C** (deputy's discretion; declining is fully workable): where a review returns REJECT with a closed, purely implementation-level fix list and no design/package/architecture implication, the Goal 1 Manager may convert it into one bounded refix plus a fresh review of the same increment without a deputy round-trip, with mandatory disclosure in the final packet. This preserves reviewer independence and the stop-on-REJECT principle at any structural finding, while matching remediation granularity to increment granularity.
4. **Note:** DG-1's resolution completes the R-32a freeze condition; the Increment-C reproduction gate then freezes the digest at the fixed (encoding, batch size, AD mode) tuple per upheld R-32b.

## 5. Repository state

MNL `b5169293…`: untracked = three Increment-A deliverables, the increment report, Review A, plus the four test-29 attempt files pending the authorized in-task deletion. `Job_Market_paper` `7195fc50…` (instrument checkpoint pending inventory). Nested clean at `27756a06…`. Both bundles rehash exactly (separate canonical hashes). No score persistence anywhere; no restricted-store reference; store untouched and out of scope under the streaming design.
