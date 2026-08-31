# JMP paper outline v1 — "Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition"

**Status legend:** ✅ accepted record · 🟡 provisional (sprint, PROVISIONAL label) · ⏳ pending (enclave / future mission) · ⛔ prohibited claim

### 1. Introduction (≈ 4 pages)
- The question: how much money-metric well-being inequality is attributable to unequal job opportunities, and how much opportunity-related inequality is misclassified as preference heterogeneity when opportunities are omitted.
- Why a latent-jobs (RURO) framework: jobs are packages (hours, wage, occupation); the opportunity set is an *estimated density*, not a menu; the 35-hour institution as the motivating fact.
- Contribution in three steps (estimate opportunities; carry them into a common-reference welfare measure; decompose) — one pipeline, consistent treatment.
- **Headline architecture (deputy-ruled):** the exhaustive two-player Shapley — *preferences vs the complete non-preference environment* (100%) — with access / wage-ability / endowments as the **nested** layer. ⏳ *The two-player number itself is not yet computed* (agenda item 6: after the specification is final); the paper's current certified magnitudes live in the nested layer.
- What we find, stated within the boundaries: opportunity contribution positive and non-negligible on every accepted specification; its magnitude is **specification-sensitive** (the LOC4 finding) but **robust to the 35-hour repair** at achieved precision; the access/ability *ordering* is not resolved. ⛔ no "10% share" as a data property; ⛔ no ordering claim.

### 2. Framework (≈ 6 pages)
- 2.1 The model: household utility over consumption and leisure (Box-Cox); the opportunity density g = access margin × occupation weights × hours-band factor (incl. the F35 peak) × occupation-conditional log-normal wage location. Equations from notebook §4(a).
- 2.2 Estimation on sampled alternatives: the −log q correction; **q is computation, g is economics** (the reader's-guide language; a proposal may be richer than its target).
- 2.3 Welfare: the common-reference money metric W1; W4/W6 as normative sensitivities. ⛔ no cross-measure quantitative robustness claim.
- 2.4 Decomposition: Shapley-Shorrocks; the equalization counterfactuals; the nested access/ability split; R_bg as the residual (to be absorbed by the two-player headline).
- 2.5 Numerical layer (one page, honest): importance sampling with the defensive mixture; RQMC for final precision; **MC bands are numerical-integration precision, never sampling CIs**; the profile envelope as a separate object. ✅

### 3. Data and institutional setting (≈ 4 pages)
- France 2016, EU-SILC/SRCV via EUROMOD input; singles module (1,555 households) with the waterfall from 11,459 (Table 1.1 + 1.1a); couples module (2,275) 🟡.
- The 35-hour statutory week and the observed spike (Fig 2.2); the hours bands with the corrected labels; the occupation key (ISCO→loc4, Table 2.2); regional coverage (NUTS-2 finest; urbanisation coding: rural = reference — the verified coding).
- EUROMOD as deterministic pricing; take-up traits.

### 4. Singles: the estimated model (≈ 6 pages) ✅ S8 as the preferred positive specification
- 4.1 Specification path (one table): baseline → LOC4 (occupation-specific wage locations, LR 92.9/3 df, ΔBIC −70.8) → S8 (+ the 35-hour opportunity peak, ΔnegLL −430.6/1 df, W-4 empty). Nesting bitwise at each step.
- 4.2 The S8 estimates (the §4 table with z, robust SEs; the reader's-guide "why z not t" as a footnote); δ_occ as *location shifts, not causal premia*; the peak as an *institutionally motivated 35-hour opportunity peak* — ⛔ not "the effect of the 35-hour law".
- 4.3 Fit: hours grid S0 vs S8 (MAE .0338→.0083, Fig 10.1); Brier on all 14 spaces; the employment/occupation share fits; the sampled-alternatives caveat on hard accuracy.
- 4.4 Identification diagnostics: single-optimum, curvature tiers, the invariance checks (age centring exact; **the leisure-unit finding** — bound-activity is a normalization artifact, interior at λ=40), the S-10 battery and the profile (the Tier-2 story resolved to a 0.12% envelope). ✅
- 4.5 Regional access: gsur active; NUTS-1/urbanisation not rejected conditional on it (the E4 tests, with the collinearity caveat).

### 5. Welfare inequality and its decomposition (≈ 8 pages)
- 5.1 The LOC4 benchmark record ✅ (`LOC4_PREFERRED_MC_BANDED_LEVELS`): W1 mean 1339.04 ± 2.11, Gini 0.1511 ± 0.0011, φ_A/φ_B/φ_P with RQMC bands, s_opp 0.0240 ± 0.0043; r_φ_P and r_R_bg as `MC_BANDED_NORMALIZED_DIAGNOSTIC`; median banded only; three-way uncertainty reporting (RQMC estimate / RQMC band / 95% profile envelope, never combined).
- 5.2 The φ_B sign qualification — the deputy's sentence verbatim ("small … positive over the 90% region … not resolved over the 95% region once numerical precision and profile resolution are taken into account"). ✅
- 5.3 The specification-sensitivity result (the paper's second finding): baseline vs LOC4 — allowing occupation-specific wage locations materially changes the attribution (the deputy's interpretation of record verbatim; both φ_A and φ_B fall; "model-conditional reallocation", ⛔ no transfer/absorption language); s_opp 0.101 → 0.024 as the contrast pair evidencing non-robustness, never as a headline magnitude.
- 5.4 S8 welfare 🟡: levels move (+8% W1 mean, Gini −0.009), **s_opp robust to the S0→S8 change at achieved RQMC precision** (0.02395 → 0.02400); the A/B gap becomes unresolved (`ACCESS_ABILITY_ORDER_UNRESOLVED_UNDER_S8`); W4/W6 disagree — ⛔ no cross-measure claim; the welfare-levels convention caveat (inherited hours normalizer).
- 5.5 What survives every specification: signs of φ_A (+) and φ_P (−); non-negligible opportunity contribution; the ordering does not. ⛔ "stable component signs" as a collective claim.
- 5.6 ⏳ The two-player preferences-vs-environment percentage (the future headline number) — placeholder, computed only after specification finalization.

### 6. Couples: first estimates (≈ 4 pages) 🟡
- The joint-alternative design (four quadrants, ~100 joint alternatives, not a cross-product); consumption pricing at the household budget; couples take-up.
- C-P4 estimates; the peak transfers (F35 reproduced per spouse); hours/employment fit; the quadrant margin as the open specification gap; the pooled-occupation cost.
- The honest state: `C-P4_NOT_PROMOTABLE_GATE_FAIL` — β_l0_m identified but not reliably calibrated; the pooled occupation block failing on fit and recovery; the five named next steps. No couples welfare in this version.

### 7. External evidence on the opportunity channel (≈ 3 pages) ⏳
- The regional identification audit: geography ceiling (NUTS-2), the recommended BMO design, `NUTS2_EXTERNAL_OPPORTUNITY_IDENTIFICATION_AID / NOT_A_CAUSAL_INSTRUMENT`; the four-table crosswalk with its disclosures (coverage 0.584; 38% withdrawn for no defensible basis; HIGH_CONFIDENCE_090 retained 0.381).
- The result slot: pending the enclave run and the §6 interpretation gate. If unlinkable: the section states the recode limitation and omits the estimate.
- LFS desired-hours validation of the hours-opportunity structure (if obtained).

### 8. Limitations and the specification-limits disclosure (≈ 2 pages) — carried in full ✅
The ten-point list (no specification-independent ordering/s_opp magnitude/levels; median; the 22 uncertified differences; W4/W6; subgroups; LR/AIC/BIC as conventional references at a boundary-adjacent optimum; δ_occ not causal); the numerical caveats (C-16 normalization, fixed-panel direct-check offset); the sampled-alternatives estimator's properties; take-up thinness (couples).

### 9. Conclusion (≈ 2 pages)
What the pipeline delivers; what the specification comparison teaches about opportunity attribution; the roadmap (couples completion; the two-player headline; the policy-reform paper as a separate piece).

### Appendices
A. Estimation details and the four-leg convergence standard · B. The welfare-measure family and normalization · C. The numerical layer (IS, CRN, RQMC, jackknife bands, the Owen scramble) · D. The profile and S-10 batteries · E. Couples design and the synthetic gate · F. Crosswalk construction · G. Data construction and the sample funnel.

### Main tables and figures (the "one main table, one main figure" rule)
- **Table 1 (main):** decomposition under the preferred specification (S8 🟡 / LOC4 benchmark ✅ side by side) with RQMC bands and the profile envelope column — the specification comparison visible in the headline.
- **Figure 1 (main):** the hours-opportunity grid, observed vs S0 vs S8 (the 35-hour spike as the paper's motivating picture).
- Supporting: the specification-path table; the φ_B profile figure with both regions; the ordering-by-basis figure; the couples quadrant confusion; the BMO grid-correlation figure.

---
redline the outline; next turn I cut the commit card and the item-8 card.