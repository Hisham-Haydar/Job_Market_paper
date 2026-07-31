# JMP-M05 Stage-D Cycle-1 Remediation Instruction v1 — Binding

**Status:** Binding instruction to the Stage-B design author for remediation cycle 1 of 2. Paste into the original Stage-B author chat together with the attached review file.
**Issued by:** Goal 1 Manager — Empirical JMP, 2026-07-31, rulings R-11–R-12.
**Authoritative fix source:** `FR_P2a_region_live_phase5_inference_methods_review_v1.md` (Stage-C independent review; verdict APPROVE AFTER FIXES; attached).
**Target repository path:** `docs/prompts/JMP_M05_stageD_cycle1_instruction_v1.md` (Job_Market_paper; untracked until the next documentation checkpoint).

## 1. Mandate

Implement the seven required fixes in review §17, exactly as written there, informed by the defect table in review §16 and the section-level reasoning in review §§4–15 — in particular §9 for the revised downstream trigger (Fix 1) and §10 ¶4 for the schema reconciliation (Fix 4). All seven are ratified by the Goal 1 Manager without modification. No fix may be skipped, reinterpreted, or partially applied.

## 2. Hard boundaries

- The recommended baselines D-1 through D-8 are unchanged in substance: same estimand, same conditional-35 object, same correction scalar `c = 1555/1520`, same artifact choice and fallback trigger, same row order, same gate register structure. The fixes change justification, precision of claims, dimensional explicitness, schema completeness, tolerance tightness, language discipline, and fallback custody — not the recommendations.
- No gate may be weakened. Fix 5 tightens T-7/T-9 and sharpens T-4 and W-4; T-19 stays gating, T-22 stays a numerical-KKT gate (and is no longer described as proof of population strict activity — Fix 1).
- No change to the accepted specification, estimate, pins, bounds, or any Phase-3/Phase-4 artifact reference. No code, no computation, no commit.
- Binding corrections C-1–C-5, the Stage-B author addendum (ERR-1, ERR-2, F-1–F-5), and all charter-frozen decisions remain fully in force.
- Do not resolve the disclosure determination (review Fix 7 explicitly leaves the licence question to the principal investigator); implement the durable restricted-custody requirements unconditionally so the design is complete under either outcome.

## 3. Versioning and structure (ruling R-12)

- Produce a complete new file named exactly `FR_P2a_region_live_phase5_inference_design_v2.md`. Do not edit v1 in place; v1 is retained as the object the review cites.
- Keep exactly the 23 headings of the design-prompt CREATE block, in order. Add the revision register as subsection **§1.1 Revision register (v1 → v2)** inside heading 1: a table mapping each fix F1–F7 to the exact sections and subsections changed, one row per fix, plus one row for any strictly-entailed consequential edit (e.g., §20 claims-register lines affected by Fix 1 or Fix 6). No change outside the rows of that register is permitted.
- Update §22 statuses to the post-review state: D-2 becomes "recommended; ruled defensible by Stage-C review (§9, §18), freeze subject to targeted recheck of fixes"; the [C-4] open item is restated as "discharged by Stage-C review, pending targeted recheck"; the disclosure determination remains open with the principal investigator; D-7 ratification request stands. Re-derive the final verdict honestly from that state — do not declare the recheck passed.

## 4. Fix-specific reminders (the review text governs; these are pointers, not substitutes)

- **F1:** Loewner claim restricted to model-based inverse-information objects; delete the robust-SE extension and every known-direction downstream-uncertainty claim; replace with the conditionality statement from review §9; recast T-22 as sample numerical KKT evidence; adopt review §9's two-tier downstream trigger (material loading ⇒ disclose conditioning and consider sensitivity; boundary-aware/resampling inference required only for inference on the bound coordinates, unconditional active-set claims, or functionals where population strict activity is not defensible).
- **F2:** `K = 35` defined as the local dimension/rank of the restricted estimating problem under strict activity; `c` presented as a pre-registered HC1/CR1-style regression-analogue convention; remove "exactly-satisfied" score-equation reliance and the referee-expectation claim; the scalar itself is unchanged.
- **F3:** every Wald object dimensionally explicit — define the 10×35 selector `E_R`, `V_RR = E_R V_I E_R'`, each restriction with its `q`, name-keyed rows for H0-A/B/C/G, the solve, and separate `p_model` / `p_robust` fields.
- **F4:** add `bound_value`, `bound_side`, `grad_negll`, `multiplier` to the 47-row table or define a dedicated authoritative bound-diagnostics bundle member; remove or define the stray `flag` column against §17.3's exact schema; the five inferential fields stay literal `NA` for active-bound and pinned rows.
- **F5:** T-4 as the signed max-norm identity; T-7/T-9 PSD allowance at machine-precision/backward-error level or no looser than the `1e-10` rank convention unless quantitatively justified; W-4 defined on the robust 95% interval with equality-to-bound explicitly triggering the warning.
- **F6:** couples/pooled degeneracy statements made conditional on their future primitive contribution structure; H0-B described as testing the common NUTS-1 intercept component; sweep the entire memo for equivalent unconditional or full-opportunity wording, including §19 and §20.
- **F7:** fallback requires durable, access-controlled, immutable restricted custody of the authoritative `.npy` with custody/locator identifier, SHA-256, size, shape, row/column fingerprints, `disclosure_class`, and retention responsibility recorded in the manifest; summaries plus a hash are insufficient.

## 5. Return contract

Return to the Goal 1 Manager chat only: the v2 file, plus a cover note listing (a) the verdict, (b) the §1.1 revision register verbatim, (c) confirmation that no baseline changed and no gate weakened, (d) any fix whose implementation surfaced a conflict with a frozen decision — in which case stop on that fix and report rather than improvise. The user saves v2 to `MNL/docs/France_case/P2a/`, uncommitted, alongside the retained v1.
