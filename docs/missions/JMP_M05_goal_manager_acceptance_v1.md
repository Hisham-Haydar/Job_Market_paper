# JMP-M05 Goal Manager Acceptance v1

**Mission:** JMP-M05 — Household-Clustered Inference (design stage)
**Author:** Goal 1 Manager — Empirical JMP
**Date:** 2026-07-31
**Target repository path:** `docs/missions/JMP_M05_goal_manager_acceptance_v1.md`

## 1. Goal-manager verdict

**READY WITH STRATEGIC OPEN DECISIONS.**

The design stage is complete: source contract verified and accepted; the inference design authored, independently reviewed (APPROVE AFTER FIXES), remediated through the full two-cycle budget, and rechecked. Zero substantive defects remain — the reviewer's final finding states "no substantive D-2 defect remains" and that no model, estimand, baseline, or additional methods review is required. Two procedural items and four strategic decisions remain open for the deputy programme director (§15); one determination remains with the principal investigator. The goal manager's pre-registered halt on MICRO-RECHECK FAIL fired and is honored: the final procedural disposition is submitted for deputy decision rather than executed under delegation.

## 2. Mission scope

Design only, and the boundary held throughout: across Stages A–E no optimizer, gradient, Hessian, covariance, test statistic, welfare, decomposition, EUROMOD, or notebook computation was run; no accepted artifact, theta, pin, bound, or specification was altered; no scope expansion into couples, pooled years, or other countries occurred. The only computations performed anywhere were the Stage-A audit's permitted static hash/metadata checks and design-time arithmetic on published constants.

## 3. Governance provenance

- `Job_Market_paper`: governance base `30fbe2da…` → M-0 management checkpoint `1d31d10a355a5c154bdb84ac419f89fff46c12fa` (ten files) → Stage-A′ closure `dfd65b271cce9f3fd854d6604c78dc769d4521a5` (completeness memo, ledger v2, deferred commit prompt). Worktree clean apart from an untracked-by-design register: two superseded v1 prompts plus the Stage-B/C/D instruments (`stageB_author_addendum_v1`, `stageC_reviewer_addendum_v1`, `stageD_cycle1_instruction_v1`) awaiting the next authorized checkpoint.
- `MNL`: HEAD unchanged at the canonical anchor `982c52217031158c4a2368709d4a6b211ebcde76`; untracked mission outputs only (three Stage-A audit files; design v1/v2/v3; review; recheck; micro-recheck). No MNL commit was made under delegation (ruling R-4): advancing MNL HEAD past the canonical anchor is reserved to the deputy.
- Nested `dclaborsupply` and gitlink unchanged at `27756a06…`. Phase-3/Phase-4 bundles rehash exactly.

## 4. Source-verification outcome

`SOURCE CONTRACT COMPLETE WITH NONBLOCKING GAPS`, accepted (ruling R-1) after independent goal-manager spot-verification. All twelve inventory items closed; all six gaps closed; no halt fired. Three permanent nonblocking UNKNOWNs (JAX/jaxlib version, platform/threads/XLA flags, SciPy version at Phase-3/4 execution) were never recorded and are unrecoverable; the design mandates environment logging in every Phase-5 manifest going forward. Ratified verified inputs (R-2): the `ln(101)` benchmark is invalid and dropped; no pin is a normalisation (all ten structurally inapplicable; true normalisations live outside the 47-vector); `gsur` is a continuous rate covariate; `hessian_free.npy` is the sole authoritative bread; symmetrisation on load against threshold `2.3588019878151842e-4` is mandatory; `N = G = 1,555` verified; clustering degenerate; strict upper-bound activity for `beta_l_age2_sm`/`beta_l_age2_sf` (ERR-1: the design prompt's "lower bounds" text was wrong and formally superseded).

## 5. Likelihood and score contract

One additive term per household: `ℓ_g = V_{g,0} − logsumexp_j V_gj ≤ 0`, all density/market/prior structure inside the alternative-specific index; unweighted sum objective (`dwt` present, never read); therefore the frozen identity `Σ_g s_g = −∇negLL` holds with no correction factor — verified, not assumed. Score matrix 1,555×37 as the stored primitive via the existing `per_group=True` hook with `jax.jacfwd` (37 forward passes vs 1,555 reverse), cross-checked by the T-16 two-mode agreement gate on 64 households; T-1 identity gated at the frozen tolerance on all 37 columns before any column selection; T-4 compares against the recorded Phase-4 gradient, closing a three-phase chain of custody.

## 6. Cluster interpretation

Exactly 1,555 `idhh` clusters, one primitive term each: the household-cluster sandwich is algebraically identical to the household-level OPG sandwich **in this application only**. All couples/pooled-year statements are conditional on their future primitive contribution structure (C-3 enforced through review and recheck). Canonical row order: `idhh`-ascending stable argsort (D-7), coinciding with the verified loader order; ratification requested because every artifact hash depends on it.

## 7. Finite-sample correction

**D-1:** two-factor with verified `N = G = 1,555` and `K = 35`, telescoping exactly to `c = G/(G−K) = 1555/1520 = 1.0230263157894737` (+1.1448% on standard errors). `K` is defined as the local dimension/rank of the restricted estimating problem under strict activity; `c` is presented as a pre-registered HC1/CR1-style regression-analogue convention for this nonlinear sandwich, not an exact M-estimation unbiasedness result. Rejected with reasons: CR0; cluster-only; `K = 37`; any `N = 157,055` construction; CR2/CR3; wild cluster bootstrap. Linked constraint **D-8**: if D-2 ever moves to the unrestricted 37, `K` moves to 37 in the same edit.

## 8. Active-bound treatment

**D-2:** conditional 35×35 sandwich `V₃₅ = c · H_II⁻¹ M H_II⁻¹` with `beta_l_age2_sm` and `beta_l_age2_sf` treated as equality restrictions at their **upper** bound 1.0 and reported with literal `NA` and status `active-bound`; no symmetric Wald objects for them under any framing. The independent review ruled this defensible and consistent with the constrained-M-estimation literature (Geyer; Andrews), with bread `H_II`, 35-column meat, and validity conditional on population strict activity — supported by multipliers `0.8446`/`1.4682` versus interior gradient noise `1.10e-4` (T-22, correctly characterized as sample numerical KKT evidence, not population proof). The Loewner ordering is confined to model-based inverse-information objects; no robust-covariance ordering or known-direction downstream-uncertainty claim survives. Boundary-aware/resampling inference is deferred under a two-tier trigger (disclosure-and-sensitivity vs required), superseding task-plan S-10 — flagged in §15 because it changes what would obligate JMP-M08/M09 to revisit the X-005 bootstrap deferral. [C-4] is discharged subject only to §15 item 3.

## 9. Fixed-pin reporting

**D-4:** literal `NA` for all inferential fields; two source-verified structural-inapplicability categories; **no normalisation category** (it would be empty); a mandatory table footnote distinguishing the true normalisations (`beta_c`, couples `theta_c`, `theta_l_m`, removed `beta_ll`) that sit outside the 47-vector. Pins carry exactly zero gradient for structural reasons; `NA` prevents a zero standard error asserting infinite precision where there is no information.

## 10. Regional-block inference

**D-5:** one certified 10-degree-of-freedom omnibus joint test carries the claim (H0-A), with pre-registered secondary sub-nulls H0-B (seven NUTS-1 dummies, described as the common NUTS-1 intercept component), H0-C (two urbanisation dummies), H0-G (`gsur` alone, stated separately as a continuous rate). All Wald objects dimensionally explicit (`E_R ∈ ℝ^{10×35}`, `V_RR = E_R V_I E_R'`, name-keyed restriction rows, separate `p_model`/`p_robust`). Language discipline holds throughout: this block is one access channel, never the full opportunity mechanism, never the decomposition share (C-2/C-5).

## 11. Score-artifact decision

**D-3:** `phase5_scores_free.npy` authoritative (hash-stable against the two demonstrated text-artifact fragilities in this repository), plus committed summaries and a non-authoritative `%.17g` CSV rendering. The disclosure status of household-level derived arrays is `UNKNOWN` and is the **principal investigator's determination** against the actual EU-SILC/EUROMOD licence terms — outstanding at this writing. The design is complete under either outcome: unconditional `disclosure_class` and `retention_responsibility` manifest fields, a durable access-controlled immutable restricted-custody fallback with locator/hash/shape/fingerprint records, and gate T-23 enforcing the route-specific block. Interim safe-harbor (R-9) in force: no household-level derived artifact is committed or pushed anywhere pending the determination.

## 12. Numerical gates

Register T-1–T-23 plus warning tier, extending the accepted naming: provenance fingerprints binding to the `.npy` SHA `e9ca080e…` and both bundle hashes; symmetrise-on-load at the recorded threshold; frozen score-identity tolerance; T-19 restricted-stationarity displacement gate (≤ 0.05 × robust SE per coordinate); T-22 strict-activity gate (≥ 100× interior max); W-4 interior-near-bound warning on the robust interval with equality triggering; T-23 custody completeness. Nothing was weakened across remediation: T-4 gained an explicit sign; T-9 tightened to the `1e-10` rank convention; T-7 replaced a derivationally invalid constant with the valid Gram/Weyl backward-error bound `κ_BE = K·G·u/(1−G·u) = 6.042388811523458e-12`, certified upward-rounded at `6.0424e-12` — 16.55× tighter than the rank convention. One E0 annotation defect in the v3 register paragraph remains (§13, §15).

## 13. Independent-review outcome

Stage C (independent ChatGPT reasoning chat, non-project, literature-checked against Geyer 1994, Andrews 1999, White 1982, Cameron–Miller 2015): **APPROVE AFTER FIXES**, seven narrow fixes, no E2. Cycle 1 produced design v2 with a full revision register; targeted recheck: **RECHECK FAIL** with exactly one residual (T-7 constant inconsistent with its displayed derivation). Cycle 2 produced v3; micro-recheck: substantive repair **PASS** on both commissioned counts; overall **MICRO-RECHECK FAIL** on two procedural grounds only — (i) a register-annotation typo (relative change is `1.85e-6`, misstated as `1.8e-5`) plus a self-contradictory loosening sentence, with the reviewer prescribing the exact replacement text; (ii) six version-identity front-matter lines outside the commission's three permitted locations, for which the reviewer explicitly requested a manager ruling. The remediation budget is exhausted at 2 of 2; per the goal manager's pre-registered halt, the disposition goes to the deputy (§15 item 3) rather than being executed under delegation.

## 14. Residual limitations

All reported uncertainty is conditional on the two active-set restrictions and ten pins and excludes active-set and specification uncertainty, whose magnitude and direction are not identified here. Precision claims are local to the accepted estimate and carry no identification or recovery claim: synthetic recovery (JMP-M06) remains mandatory and is not substituted by anything in this mission. Three environment UNKNOWNs are permanent for Phases 3–4. The regional/access block is one opportunity channel. The bound coordinates' economic reading (age-curvature of singles leisure preference at a corner) is a manuscript caveat and an M07/M08 handoff, not a defect. The v1 execution-report "optional npy" understatement stands flagged for correction at the next MNL documentation pass.

## 15. Decisions recommended for deputy approval

1. **Freeze D-1 through D-8** as specified in design v3 §22 and §§7–12 above.
2. **Ratify the task-plan supersessions** established through review: S-10's two-tier demotion (consequential for JMP-M08/M09 and the X-005 deferral trigger); §6.2(1)/§6.3's conservatism and referee-expectation claims removed; §11.1's T-7 tolerance replaced by the quantified bound.
3. **Dispose the micro-recheck residuals:** (a) ratify the goal manager's R-15 admission of the six version-identity front-matter lines (entailed by the v3 instruction; C-d precedent; the commission-wording defect is the goal manager's); (b) authorize the prescribed E0 micro-edit — correct `1.8e-5` to `1.85e-6` and substitute the reviewer's sentence ("T-7 is minimally loosened only to implement the valid upward-rounded certification, while remaining 16.55× tighter than the rank convention") — as design v4, followed by the reviewer's one-line conversion to PASS per its own stated passage logic.
4. **Authorize two documentation commits:** (a) MNL — the nine mission evidence files under `docs/France_case/P2a/` (advances MNL HEAD past the canonical anchor; deputy authority); (b) `Job_Market_paper` — the Stage-B/C/D instruments, ledger v3, and this memo.
5. **Record the outstanding E3 item:** the principal investigator's one-line disclosure determination on household-level derived arrays (blocks only the final D-3 route selection; execution design is complete under either outcome).

## 16. Whether implementation mission should launch

**Recommend LAUNCH** of the Phase-5 implementation-and-certification mission immediately upon §15 items 1–3, with item 5 resolvable in parallel. The design's §21–§22 handoff content is complete: scope, frozen decisions, gates T-1–T-23, artifact and transaction contract, one-run rule, halts, and the mandatory environment-logging requirement. Independent code review (Codex) becomes applicable at that stage per the hierarchy's role table.

## 17. Final return packet

(1) `JMP_M05_mission_ledger_v3.md`; (2) Stage-A audit report + `phase5_parameter_map_v1.csv` + `phase5_source_inventory_v1.json`; (3) `JMP_M05_source_verification_completeness_v1.md`; (4) design v3 (v1, v2 retained on disk as review-cited evidence); (5) methods review + targeted recheck + micro-recheck; (6) this memo; (7) the D-1–D-8 decision table (ledger v3 §4); (8) repository revisions and status as in §3; (9) the Stage-B/C/D instruction instruments.

## 18. Immediate next action

Deliver the packet to the ChatGPT deputy programme director for the strategic-gate decision on §15; on acceptance, execute the authorized v4 micro-edit and reviewer conversion, run the two documentation commits, obtain the PI disclosure determination, and open the Phase-5 implementation mission charter.
