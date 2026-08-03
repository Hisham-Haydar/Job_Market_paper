# JMP-M05B E2 Escalation — Code Review REJECT v1

**Mission:** JMP-M05B — Phase-5 Inference Implementation and Certification
**From:** Goal 1 Manager — Empirical JMP  **To:** ChatGPT Deputy Programme Director
**Date:** 2026-08-01
**Halt trigger:** charter §15 — independent code review verdict REJECT (12 required fixes)
**Target repository path:** `docs/missions/JMP_M05B_E2_escalation_code_review_reject_v1.md`

## 1. State at halt

Stages I-1/I-2 delivered a Phase-5 implementation (separate runner + config + 53-test deterministic suite + report), uncommitted, at MNL HEAD `983a2ecf…` with the nested package untouched at `27756a06…` and both accepted bundles rehashing exactly. Stage I-3 (Codex 5.6, maximum reasoning, read-only) returned **REJECT** in `docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v1.md`. Per charter §15 the Goal 1 Manager stopped: remediation was not commissioned, nothing was committed, the working set is preserved unedited, and the dry run remains blocked — the review parser is fail-closed and this REJECT cannot authorize execution.

## 2. What the review confirms sound

The central statistics are substantially correct as implemented: jacfwd per-household scores with the T-1/T-4 identity at frozen tolerances; hash-checked bread loaded and symmetrised, name-reduced to `H_II`; 35-column meat; `c = 1555/1520` with CR0 recoverable; certified T-7 constant; covariance algebra, `E_R` selectors, H0-A/B/C/G, upper-bound and literal-`NA` reporting all conform to design v4. Likelihood reuse is by import only — no duplicated loader or likelihood mathematics. Goal-1 rulings A-3 and A-4 verified correct; A-1 substantively correct (manifest must add chunk size); A-2 correct as architecture but not closed in implementation (unregistered `_t12` duplicate).

## 3. Why REJECT is warranted

Two critical custody defects: (i) a public ungated `reproduce` mode computes the full 1,555×37 restricted score matrix and writes it to any caller-selected path with no review, revision, cleanliness, transaction, or custody gate — an authorization and disclosure bypass of the PI determination; (ii) restricted-path confinement enumerates two Git roots instead of resolving actual Git ancestry, so a destination inside the sibling `Job_Market_paper` worktree would pass. Additionally high: an all-pass dry run is structurally forced to STOPPED (gate register summarized before four gates attach); the binding `phase5_parameter_map_v1.csv` is not authenticated or used at projections (design §§7, 21); T-13 compares cached pre-run bundle hashes rather than rehashing after evaluation; external restricted writes are non-transactional. Plus medium/low items including an ineffective lazy-import optimizer guard, a tautological pin-gradient falsification, stale environment capture, and three lifecycle-invalid tests that cannot stay green through the mandated review→commit→dry-run sequence.

## 4. Classification of the twelve fixes

- **Code-only, design-conformant (no design reopening):** fixes 1–7, 9–11 — every one enforces something design v4, the charter, or deputy D-3 already requires. None alters a formula, gate constant, frozen decision, or the statistical contract.
- **Infrastructure + code:** fix 8 — a durable, access-controlled, immutable restricted store must be **provisioned by the PI** (ACL-restricted directory or IT-managed store) and then bound by code with external staging and atomic publication. Requires a PI action outside any coding tool.
- **Test-suite corrections:** fix 12 — integration coverage for fixes 1–11 plus removal of two tautological and three lifecycle-invalid assertions.
- **Explicitly out of scope:** stale committed Phase-4 `test_42` (predates this mission) — reviewer and manager concur it is separate housekeeping; deputy authorization requested to schedule it.

## 5. Assessment and recommendation

The design stands; the failure is implementation-stage engineering concentrated in custody, authorization, and lifecycle — found by the independent layer working as intended. The reviewer's own §11 judges the defects repairable in **one bounded remediation** followed by an independent **Phase-5 review v2 bound to the remediated state**.

**Requested deputy decisions:**
1. Authorize one bounded remediation cycle implementing exactly the twelve required fixes (no scope beyond them), executed by the original implementer, from the preserved uncommitted state.
2. Authorize independent code review v2 (Codex, read-only) bound to the remediated exact state; commit gate (charter §10) and the single dry run (§11) remain conditional on APPROVE.
3. Direct the PI store-provisioning action for fix 8 (in parallel; blocking only the custody-binding portion).
4. Authorize the separate `test_42` housekeeping change (may be batched with the eventual I-5 commit as a distinct commit, or deferred).
5. Confirm the REJECT consumed no charter §9 remediation budget (the two narrow cycles attach to APPROVE AFTER FIXES); alternatively, rule how the budget applies to the authorized bounded remediation.

## 6. Repository state

MNL `983a2ecf…`, working set: modified `.gitignore` + five untracked Phase-5 files + the review file (untracked). `Job_Market_paper` `7195fc50…`, clean. Nested `27756a06…`, clean, never touched. No `complete/` exists; no household-level score bytes exist anywhere (no full scoring has ever run); both bundles verified.
