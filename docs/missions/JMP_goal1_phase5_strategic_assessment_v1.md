# JMP Goal-1 Strategic Assessment — Accepted Phase-5 Inference Results

**From:** Goal 1 Manager — Empirical JMP  **To:** ChatGPT Deputy Programme Director (roadmap proposal)
**Date:** 2026-08-04  **Evidence:** canonical attempt `20260803T133122Z_…` at MNL `520441a6…`, bundle `d08947ce…`
**Target repository path:** `docs/missions/JMP_goal1_phase5_strategic_assessment_v1.md`

## 1. The economic headline

With certified household-clustered inference (1,555 clusters, conditional-35 sandwich, c = 1555/1520), the paper's opportunity-environment mechanism is **statistically established and structurally sharp**:

- **H0-A (confirmatory, 10 df): W_robust = 37.45, p_robust = 4.7e-05 — rejected.** Regional job-access differences belong in the model.
- **The rejection is carried entirely by `gsur`** (H0-G: W_robust = 29.21, p_robust = 6.5e-08; β = −1.105, robust 95% CI [−1.51, −0.70]). The seven NUTS-1 dummies are jointly null (p_robust = 0.594) and the two urbanisation terms add nothing (p_robust = 0.847). Access inequality is one dominant, precisely measured dimension — not diffuse geography.
- Model-based and robust p-values agree on every verdict (all four tests same side of every conventional threshold), so no conclusion hinges on the variance estimator.

**Consequences.** (i) The previously deferred external-regional-covariates decision resolves itself: the parsimonious access set (`E`, `gsur`, occupation structure) is statistically sufficient at NUTS-1 resolution; enrichment is optional robustness (a later mission), not a prerequisite. (ii) The opportunity block for the welfare decomposition is ready: hours structure (β_E z = −8.0; ft/pt/lh all |z| > 5) and occupation access (five of six coefficients significant, e.g. occ_4_f = 0.854, z = 8.6) are precise.

## 2. The precision picture for the welfare stage

Wage-density parameters are strong (β_w0 z = 38; educH z = 12.5; σ = 0.4135 with z = 27). Three robust/model ratios stand out (σ 1.83, θ_c 1.67, β_l0_sf 1.54) — classic misspecification sensitivity in the curvature-relevant parameters; W-1 passes at full sample ([0.72, 1.83] inside [0.2, 5]), confirming the earlier subset flag was scale artifact. The known soft spot is preference-side leisure curvature: both age² terms at their upper bounds (multipliers 0.84, 1.47), and W-4 flags `beta_l0_sm` (robust CI [−0.12, 9.68] vs lb 0.05) and `beta_w_pexp2` (CI lower −0.1014 vs lb −0.1, a hairline breach). Consumption curvature θ_c = 0.093 (SE_rob 0.077) is imprecise. **Money-metric welfare loads on exactly these preference parameters**, so the S-10 Tier-1 treatment (disclosure + pre-registered sensitivity of welfare results to the boundary-region coordinates) is not optional caution — it is the empirically indicated design for the welfare mission. Technical hygiene is clean throughout: T-19 stationarity 3.4e-05 vs 0.05; W-5 centring correction 7.8e-12; correction-scalar SE inflation 1.14% (convention-scale, as ruled).

## 3. Recommended next missions (deputy decision)

1. **M07 — Inference results integration and write-up (charter now; no blockers).** The empirical section's inference story is complete: methods paragraph (clustered misspecification-robust sandwich, conditional-35, NA-reporting for bounds/pins), the 47-row table, the H0 battery with the gsur concentration result, W-4/S-10 Tier-1 disclosure text. Pure economics and writing on accepted artifacts; also produces the sensitivity-point specification (e.g. welfare recomputed at CI-interior values of `beta_l0_sm`, `beta_w_pexp2`) that the welfare mission consumes.
2. **The LOC4 decision (Path A vs B) — decide alongside M07, before the welfare run.** New evidence for the call: occupation mean-shifts are large and precise (educH 0.345; occupation coefficients up to 0.85) while σ is common across occupations by construction. If V_i^dir is sensitive to occupation-specific dispersion (not just means), Path A (resolve four LOC4 densities first) is safer; if means dominate the welfare functional, Path B (proceed, LOC4 as robustness) is defensible and faster. Goal-1 lean: a bounded Path-B-with-sensitivity — proceed on the certified baseline, with the LOC4 four-density variant pre-registered as the first robustness axis — but this is a design-authority call for the deputy.
3. **M06 (industry `lindi`) and external regional covariates: defer** — both are enrichment, now demonstrably not prerequisites.

## 4. Standing state

All repositories clean at `520441a6…` (MNL) / `1e54bcd7…` (JMP) / `27756a06…` (nested); mission M05C closed; two duplicate-file deletions queued for the next gated JMP-repo task; debt D3–D10 nonblocking; no Phase-5 reopening.
