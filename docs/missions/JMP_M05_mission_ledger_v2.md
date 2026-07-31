# JMP-M05 Mission Ledger v2

**Mission:** JMP-M05 — Household-Clustered Inference
**Goal manager:** Goal 1 Manager — Empirical JMP (persistent chat, operating under `JMP_Goal1_manager_operating_contract_v1.md`)
**Supersedes:** `JMP_M05_mission_ledger_v1.md` (retained, committed at `1d31d10a…`, historical)
**Ledger updated:** 2026-07-31
**Target repository path:** `docs/missions/JMP_M05_mission_ledger_v2.md`
**Ledger status:** Operational file. Not canonical state. Not a decision log.

---

## 1. Stage tracker

| Stage | Status | Evidence / gate |
| --- | --- | --- |
| M-0 — Management checkpoint commit | **CLOSED** 2026-07-30 | `Job_Market_paper` commit `1d31d10a355a5c154bdb84ac419f89fff46c12fa` (parent `30fbe2da…`); ten files, additions only; accepted by Goal 1 Manager |
| A — Source verification | **CLOSED** 2026-07-31 | Audit verdict `SOURCE CONTRACT COMPLETE WITH NONBLOCKING GAPS`; task-manager verdict `REPORT COMPLETE WITH NONBLOCKING GAPS` (15/15 contract headings); Goal 1 Manager acceptance ruling R-1 |
| A′ — Stage-A closure documentation checkpoint | OPEN | Commit of completeness memo + ledger v2 + deferred commit-prompt in `Job_Market_paper` (card M05-AC-3) |
| B — Design memo | NEXT (blocked on A′) | Separate Opus author chat; design prompt v1 + binding addendum (ERR-1, ERR-2, findings F-1–F-5) |
| C — Independent methods review | PENDING | Separate reviewer; provisional routing Codex 5.6, max thinking |
| D — Narrow remediation | PENDING (0 of 2 used) | — |
| E — Final Goal 1 decision | PENDING | `JMP_M05_goal_manager_acceptance_v1.md` |

---

## 2. Stage-A outcome

Verification inventory: **V-1 through V-12 all CLOSED.** Source gaps **G-A through G-F all CLOSED.** No charter §13 halt and no HM-* halt fired. HM-KKT explicitly does not fire (recorded upper bounds consistent with negative negLL gradients; multipliers 0.8446 and 1.4682).

Permanent nonblocking UNKNOWNs (under V-11; never recorded in any accepted artifact; unrecoverable by static inspection; re-execution prohibited):

1. JAX / jaxlib version at Phase-3/4 execution time;
2. platform string, thread and XLA flag settings at execution time;
3. SciPy version at Phase-3 execution time.

Handoff requirement carried to the Phase-5 implementation charter: the implementation must log interpreter, JAX/jaxlib, platform, and thread/XLA facts into its manifest going forward.

---

## 3. Binding verified inputs for Stage B (ratified by ruling R-2)

Facts are binding; the decisions they bear on remain the design author's and the managers'.

- **F-1:** `ln(101)` is not an objective bound. `l_g = V_obs − logsumexp_j(V_gj) ≤ 0` with no `−ln(101)` floor; every index term is alternative-specific. The comparison is dropped, not restated; nothing may rest on average negLL.
- **F-2:** No pin is a normalisation. All ten are structurally inapplicable (eight unreferenced by the singles builder; two multiply an identically-zero 2016 covariate). True normalisations (`beta_c = 1.0`, couples `theta_c = 0.0`, `theta_l_m = −0.8`, removed `beta_ll`) sit outside the 47-vector and outside the pin-reporting convention.
- **F-3:** `gsur` is a continuous `(drgn1, educ3, sex)`-indexed rate (×10, `offer_only_vars`), not a region dummy. Reference categories verified: NUTS-1 region 1 (`drgn1 == 1`, 245 households); rural (`drgru`, 395 households). Constraint on use: the charter/design-prompt requirement of one ten-degree-of-freedom omnibus joint test stands; layering H0-A/B/C sub-structure (gsur / seven NUTS-1 dummies / two urbanisation dummies) around it is the author's design decision.
- **F-4:** `hessian_free.csv` is not bit-exact to `hessian_free.npy` (337/1,369 entries differ; ≤1.82e-12 abs, ≤4.65e-13 rel). Authoritative bread: `hessian_free.npy` (float64, 37×37, C-contiguous, per-file SHA `e9ca080e…`).
- **F-5:** The persisted Hessian is the raw unsymmetrised `H`; the `Hs` Phase 4 used downstream is not persisted. Phase 5 must load the `.npy` and symmetrise on load against the recorded threshold `2.3588019878151842e-4`.
- **Firmed conditionals:** `N = G = 1,555` verified (1,555 additive unweighted terms; `dwt` present but never read; 157,055 rows definitively not a candidate for N). Clustering verified **degenerate**: household-cluster sandwich ≡ household-level OPG sandwich in this application only; no claim extended to couples or pooled years (C-3 preserved).
- **Score construction fact:** the production builder already exposes `per_group=True` returning the (n_groups,) positive log-likelihood vector; `jax.jacrev` of it is the 1,555×37 score matrix. Sum convention verified, so `Σ_g s_g = −∇negLL` holds with no correction factor.
- **Active-bound facts:** `beta_l_age2_sm` (free 2), `beta_l_age2_sf` (free 6), both at **upper** bound 1.0, strictly active (μ = 0.8446, 1.4682 vs interior max |grad| = 1.0993e-4 at `beta_w_educH`, free 33); matches Phase-3 G-15/G-16 records; task plan §7.3 falsification criterion does not trigger.

Binding corrections C-1 to C-5 from `JMP_M05_task_plan_manager_acceptance_v1.md` remain in force for Stages B–E unchanged.

---

## 4. Errata register (resolved by Stage-B addendum; committed prompts not edited)

- **ERR-1 — Design-prompt bound direction.** `JMP_M05_inference_design_prompt_v1.md` (BINDING ACCEPTED STATE) states "two free parameters at their accepted lower bounds". Source-verified: **upper** bounds. Canonical state and charter state no direction — no canonical conflict, no halt. The Stage-B addendum substitutes the verified statement.
- **ERR-2 — Design-memo heading contract.** The design prompt requires 23 headings and verdicts `READY FOR MANAGER REVIEW / READY WITH OPEN DECISIONS / BLOCKED`; task plan §14 anticipated 22 headings and `READY FOR IMPLEMENTATION CHARTER / …`. Ruling: the deputy-issued prompt governs structure and verdict vocabulary; task plan §14 properties (one baseline per decision with named rejected alternatives, pre-registered falsification criteria, UNKNOWN discipline, permitted/prohibited claims, implementation-handoff content) apply as content requirements within that structure.
- **Documentation note (no action this mission):** `FR_P2a_region_live_phase4_execution_report_v2.md` describes `hessian_free.npy` as "optional"; the accepted runner makes it a required `PHASE4_ARTIFACTS` member. Understatement flagged for the Stage-E packet.

---

## 5. Goal 1 Manager rulings register

- **R-1 (2026-07-31):** Stage-A source contract ACCEPTED as delivered; Stage A closed. Task-manager completeness memo accepted (15/15 headings; permitted verdict; no-follow-up call ratified — the three UNKNOWNs are unrecoverable by static inspection).
- **R-2:** Findings F-1–F-5 and firmed conditionals ratified as binding verified inputs for Stage B (§3 above).
- **R-3:** Completeness memo filed verbatim (including its preamble independence caveat) at the contract filename `docs/missions/JMP_M05_source_verification_completeness_v1.md`; the produced title "…Completeness_Memo_v1" is not used as the filename.
- **R-4:** The three audit files remain **untracked in MNL**. Committing them would advance MNL HEAD past the canonical anchor `982c5221…`, which only the deputy programme director may move. MNL documentation commit deferred to the Stage-E return packet for deputy authorization.
- **R-5:** A docs-only Stage-A closure checkpoint commit in `Job_Market_paper` is authorized under the goal-manager delegation (operational mission files only; no governance file touched; pattern established by the deputy-ordered M-0 checkpoint). Executed via card M05-AC-3.
- **R-6:** The task manager's known limitation — no independent repository channel; git-state claims taken from the audit's self-report — is accepted as inherent to a chat-based reviewer and mitigated by the audit's per-file blob/cleanliness inventory in `phase5_source_inventory_v1.json`.

---

## 6. Escalation and remediation log

| # | Date | Class | Description | Resolution |
| --- | --- | --- | --- | --- |
| 1 | 2026-07-30 | Management correction (deputy-issued) | Stage-A correction memo: Defects A–C in v1 prompts and commit scope | v2 prompts adopted; M-0 checkpoint ordered and executed; does **not** consume Stage-D remediation budget |
| 2 | 2026-07-30 | E0 | M-0 executor clarifications: untracked residue; `core.ignorecase` staging quirk; casing split avoided by staging under tracked lowercase `docs/missions/` | Resolved in-task; casing normalization of untracked worktree file queued to A′ housekeeping |
| 3 | 2026-07-31 | E0/E1 | ERR-1 and ERR-2 identified during Goal 1 review of Stage-A return | Resolved by ruling; Stage-B addendum mechanism; no halt |

Remediation cycles used (Stage D budget): **0 of 2**.

---

## 7. Artifact register

Committed at `1d31d10a…` (M-0): operating contract; hierarchy; delegation packet; ledger v1; correction memo; task-manager prompt v2; task plan; task-plan acceptance; methods-review prompt v1; source-verification prompt v2. (`JMP_M05_inference_design_prompt_v1.md` was already tracked from `30fbe2da…`.)

| Artifact | Location | Status |
| --- | --- | --- |
| `FR_P2a_region_live_phase5_source_verification_v1.md` | `MNL/docs/France_case/P2a/` | delivered; **untracked pending deputy (R-4)** |
| `phase5_parameter_map_v1.csv` | `MNL/docs/France_case/P2a/` | delivered; untracked pending deputy (R-4) |
| `phase5_source_inventory_v1.json` | `MNL/docs/France_case/P2a/` | delivered; untracked pending deputy (R-4) |
| `JMP_M05_source_verification_completeness_v1.md` | `docs/missions/` | to be saved verbatim (R-3); committed at A′ |
| `JMP_M05_mission_ledger_v2.md` | `docs/missions/` | this file; committed at A′ |
| `JMP_M05_management_checkpoint_commit_prompt_v1.md` | `docs/prompts/` | deferred-queue item; committed at A′ |
| `FR_P2a_region_live_phase5_inference_design_v1.md` | `docs/France_case/P2a/` (MNL) | expected from Stage B; **not committed before review** |
| `FR_P2a_region_live_phase5_inference_methods_review_v1.md` | `docs/France_case/P2a/` (MNL) | expected from Stage C |
| `JMP_M05_goal_manager_acceptance_v1.md` | `docs/missions/` | expected from Stage E |

Untracked-by-design residue in `Job_Market_paper` after A′: exactly the two superseded v1 prompts (`JMP_M05_source_verification_prompt_v1.md`, `JMP_M05_task_manager_operating_prompt_v1.md`).

---

## 8. Open design decisions (unchanged; close in Stages B–E)

1. Finite-sample correction — Stage-A facts narrow it (`N = G = 1,555` verified; two-factor `c = [G/(G−1)]·[(N−1)/(N−K)]` now has fully defined inputs) but do not close it.
2. Active-bound treatment — strict upper-bound activity verified; conditional-35 covariance remains a proposal under C-4.
3. Score-artifact format.
4. Fixed-pin reporting — F-2 removes the "normalisation" category; NA-representation choice remains open.
5. Regional-block covariance and joint-test protocol — F-3 constrains construct language; 10-df omnibus fixed by charter.
6. Exact numerical gates and tolerances — must now include symmetrise-on-load (F-5) and `.npy`-fingerprint (F-4) gates.

---

## 9. Next authorized action

Execute card **M05-AC-3**: save the completeness memo (R-3) and this ledger to their repository paths, then run the Stage-A closure documentation checkpoint commit in `Job_Market_paper` only. On its clean return, the Goal 1 Manager issues **M05-AC-4** commissioning the Stage-B design memo (separate Opus chat; design prompt v1 verbatim + binding addendum covering ERR-1, ERR-2, F-1–F-5, firmed conditionals, and C-1–C-5).
