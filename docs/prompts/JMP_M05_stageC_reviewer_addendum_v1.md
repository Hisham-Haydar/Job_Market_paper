# JMP-M05 Stage-C Reviewer Addendum v1 — Binding

**Status:** Binding supplement to `docs/prompts/JMP_M05_methods_review_prompt_v1.md`. Paste immediately after the full committed prompt text. Where this addendum and the prompt conflict, this addendum governs; everywhere else the prompt governs unchanged.
**Issued by:** Goal 1 Manager — Empirical JMP, 2026-07-31, under `JMP_Goal1_manager_operating_contract_v1.md`; rulings R-7–R-10.
**Target repository path:** `docs/prompts/JMP_M05_stageC_reviewer_addendum_v1.md` (Job_Market_paper; untracked until the next documentation checkpoint).

## 1. Independence contract

You are the independent Stage-C reviewer. You had no part in authoring the design memo, the task plan, or the source audit. You are a fresh chat with no project memory. Do not defer to the author's internal consistency; your mandate is adversarial adequacy review. You do not edit the memo, do not compute empirical inference, do not run repository operations, and do not propose respecification of the accepted model — if you conclude the memo cannot stand without a model, estimand, or baseline change, say so under "Residual defects" and verdict REJECT or APPROVE AFTER FIXES; the escalation is the Goal 1 Manager's to run.

## 2. Errata notices (do not mark these against the memo)

- **ERR-1.** The committed design prompt's BINDING ACCEPTED STATE says the two active-bound parameters sit at "accepted lower bounds". That sentence was factually wrong and was formally superseded before authoring: source verification (audit §8) establishes both at their **upper** bound 1.0, strictly active, KKT-consistent. The memo's upper-bound treatment is correct and mandated; flagging a prompt/memo mismatch here would be an error.
- **ERR-2.** The memo's 23-heading structure and verdict vocabulary follow the committed design prompt's CREATE block by manager ruling; the task plan §14's 22-heading list was superseded on structure while its content properties (one baseline per decision, falsification criteria, UNKNOWN discipline, claims register, handoff content) remained binding. Judge the memo against the 23-heading contract.
- The Stage-B author operated under `JMP_M05_stageB_author_addendum_v1.md` (attached); treat it as part of the author's binding instructions when judging compliance.

## 3. Priority review targets (in addition to the prompt's twenty questions)

1. **D-2 / [C-4] — the priority target.** Rule explicitly on each element the acceptance memo C-4 reserved: active-bound direction and KKT consistency; whether conditioning on the active set is the intended estimand; the correctness of the conditional bread `H_II⁻¹` and the 35-column meat `S_Iᵀ S_I` for the restricted pseudo-true QMLE (memo §§8–9, §11); the stated limits of treating the active set as fixed (including the memo's own admission that the conditional object is weakly smaller than the marginal — Loewner argument, §11.2); and whether any alternative boundary-aware inference is required for paper claims or is adequately deferred with the named trigger. No symmetric Wald objects for the two bound coordinates may survive review.
2. **D-1 — K = 35 and the telescoping.** Assess whether "K counts the exactly-satisfied first-order conditions on the score sums" (§10.3) is a defensible degrees-of-freedom rationale for an M-estimation sandwich rather than a regression formula imported mechanically; verify `c = G/(G−K) = 1555/1520` and the D-8 linkage (K moves with the covariance object).
3. **Meat construction.** The uncentred-OPG decision (§9.2) with the published residual `1.0993e-4` as diagnostic W-5: adequate, or does the restricted-model setting warrant centring?
4. **T-19 / T-22 / W-4.** Are the strict-activity gate (multiplier ≥ 100× interior max), the restricted-stationarity displacement gate (≤ 0.05 × robust SE per coordinate), and the interior-near-bound warning adequate, correctly tiered, and computable as specified?
5. **D-7 row order.** `idhh`-ascending stable argsort as canonical (§6.3), given the audit's finding that loader order is mergesort-by-`idhh`: confirm the two coincide or that the memo's construction is unambiguous either way, since every artifact hash depends on it.
6. **D-3 and the fallback.** Is the `.npy`-authoritative choice with the pre-specified disclosure fallback (§17.1) proportionate and reproducible? Do not attempt to resolve the EU-SILC/EUROMOD licence question — that determination is the principal investigator's; assess only whether the fallback preserves certification integrity if it triggers.
7. **Score route.** jacfwd over jacrev for a 1,555×37 Jacobian with the T-16 two-mode agreement check on 64 households: correct cost reasoning, adequate cross-check, no memory-unsafe row-level Jacobian.
8. **Language discipline.** C-2/C-5 in §13 and §20 (regional/access block ≠ full opportunity mechanism ≠ decomposition share); C-3 conditional degeneracy language; D-4's two structural-inapplicability categories and the mandatory footnote distinguishing the true normalisations outside the 47-vector.

## 4. Authoritative inputs (attached set)

Canonical state; decision log; mission charter; task plan; task-plan acceptance (C-1–C-5); mission ledger v2 (ratified findings F-1–F-5, errata, rulings); Stage-A audit report + `phase5_parameter_map_v1.csv` + `phase5_source_inventory_v1.json`; source-verification completeness memo; Stage-B author addendum; the design memo under review. Every review claim about repository facts must cite the audit, not assumption.

## 5. Output handling

Produce exactly one downloadable markdown file named `FR_P2a_region_live_phase5_inference_methods_review_v1.md`, using exactly the 19 headings of the committed review prompt's CREATE block, closing with exactly one verdict: APPROVE / APPROVE AFTER FIXES / REJECT. If APPROVE AFTER FIXES, list each required fix as a numbered, narrow, self-contained item — the remediation budget is two cycles, so fixes must be mergeable in one pass. The user saves the file to `MNL/docs/France_case/P2a/`, uncommitted. Return the file plus a three-line cover note (verdict; number of required fixes; whether any finding is E2 — i.e., requires a model, estimand, or baseline change) to the Goal 1 Manager chat only. Not the deputy programme director.
