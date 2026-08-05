# Appendix A. Inference for the France 2016 P2a Specification

**Mission:** JMP-M07, Stage B (economics drafting)
**Target repository path:** `manuscript/appendices/FR_P2a_inference_appendix_note_v1.md`
**Companion:** `manuscript/sections/FR_P2a_empirical_inference_v1.md`
**Authoritative numerical inputs:** `docs/results/FR_P2a_phase5_inference_results_memo_v1.md`;
`docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv`
**Numerical estimation:** Not performed. **New model execution:** Not performed.

> **Drafting note (remove before circulation).** This appendix records the
> construction of the reported standard errors, the treatment of constrained and
> non-estimated coordinates, the full-precision test statistics, and the
> pre-registered diagnostics that the welfare stage inherits. Every figure below
> is a verbatim rendering of an accepted Phase-5 artifact. Nothing in this
> appendix is recomputed from microdata.

---

## A.1 Scope

This appendix supports the estimation and inference section. It does three
things: it documents how the reported covariance objects were built and why the
reported dimension is 35 rather than 47; it reproduces the regional access
hypothesis battery at full precision; and it states the two pre-registered
commitments — the near-boundary sensitivity design and the wage-density
robustness axis — that constrain the interpretation of the welfare and
decomposition results reported later in the paper.

It does not report any welfare, decomposition, or LOC4 result, none of which
existed at the time of writing.

---

## A.2 Evidence base

All figures in the inference section and in this appendix derive from one
accepted estimation-and-inference attempt.

| Item | Value |
|---|---|
| Accepted attempt | `20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE` |
| Phase-5 bundle (SHA-256) | `d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232` |
| Estimation-engine evidence commit | `905348c53b31049db854c16016fa064517c19892` |
| Estimation-engine closeout HEAD | `520441a653f04196bf1e92e3658a478b4feb3718` |
| Paper repository checkpoint | `1e54bcd7fe6eb5d202db97c204a655d385181442` |
| Nested estimation package | `27756a06ea189339aa82915ed2124628afed20eb` |
| Accepted Hessian bread (SHA-256) | `e9ca080ecc7e40e43881b9422af0095f23ad2bfef3e84648d2031a33eb9e4061` |
| Parameter reporting map (SHA-256) | `89a0465cc55f4bc05898559120591e4c28db15a18992bd2b33ba6538ce7b8481` |

All nineteen members of the attempt manifest were inspected in the Stage-A
extraction. The set of recorded gating failures is empty, and every diagnostic
carrying gating status passed. Exactly one diagnostic did not pass: `W-4`,
which carries warning status and is the near-boundary interval check discussed
in A.6.

---

## A.3 The covariance estimator

Standard errors are computed from a sandwich estimator of the covariance of the
constrained quasi-maximum-likelihood estimator, evaluated at the accepted
optimum.

**Bread.** The accepted Hessian of the objective, whose hash is recorded in
A.2 and which was verified at the manifest-binding stage. Its rank is **37**,
matching the count of free coordinates in the parameter vector.

**Meat.** Built from the streamed per-household score aggregate over **1,555
household contributions**. The aggregate was validated against the
independently computed Phase-4 analytic gradient, with a maximum absolute
deviation of `1.4566126083082054e-13` — a machine-precision agreement, which is
what makes the meat and the bread demonstrably the same objective's derivatives
rather than two separately assembled objects. The meat has numerical rank 35.
No per-household score is persisted at row level in the released artifacts: the
released member set is allow-listed, contains no row-level score member, and
leaves no unclassified files.

**Finite-sample correction.** A scalar `c = 1.0230263157894737` is applied,
recorded in telescoped form as `1555/1520` and following
`c = [G/(G−1)] × [(N−1)/(N−K)] = G/(G−K)` with `G = 1555` clusters,
`N = 1555` observations and `K = 35` estimated interior coordinates. Applied to
variances, this scales every standard error by the common factor `√c`, an
inflation slightly above one percent. This is a convention of the HC1/CR1
family. It is uniform across coordinates, it cannot change the ordering of any
test statistic, and at this magnitude it does not move any verdict in Table 1
of the main section. It is reported for reproducibility, not because anything
turns on it.

**Both covariance objects are released.** The model-based covariance (the
inverse-Hessian object) and the robust sandwich covariance are both produced as
released members, in matrix and array form, and both satisfy the required
definiteness checks. The main section reports standard errors under both.

**Clustering, correctly described.** The P2a sample contains one
labour-market-relevant adult per household, so each household contributes
exactly one likelihood term and each cluster has size one. Clustering at the
household level therefore cannot and does not correct for within-cluster
dependence. What the sandwich delivers here is **robustness to misspecification
of the likelihood** — the divergence between the outer product of scores and
the negative Hessian — and it should be described that way rather than as a
dependence correction. *(Interpretation; the underlying construction is as
recorded in the accepted artifacts.)*

---

## A.4 Dimension of the reported inference

The parameter vector has 47 coordinates, resolving as follows.

| Class | Count | Inferential treatment |
|---|---:|---|
| Interior, freely estimated | 35 | Model-based SE, robust SE, robust 95% interval |
| Free but at an active upper bound | 2 | Literal `NA` in all inferential fields |
| Pinned (not estimated in this sample) | 10 | Literal `NA` in all inferential fields |
| **Total** | **47** | |

The 37 free coordinates match the rank of the bread; the 35 interior
coordinates match the dimension and numerical rank of the reported covariance.
Reported inference is therefore **conditional on the observed active set**. The
two active-bound coordinates are `beta_l_age2_sm` and `beta_l_age2_sf`, both at
their upper bound.

The rationale for excluding active-bound coordinates is given in the main
section: at an active constraint the Karush-Kuhn-Tucker multiplier is non-zero,
the score does not vanish in the constrained direction, and the estimator's
sampling distribution is censored at the constraint rather than symmetric, so a
Wald standard error would describe a distribution the estimator does not have.
The pinned coordinates are excluded for a different reason — eight couples
leisure parameters are not referenced by the singles objective, and two
survey-year dummies correspond to covariates that are identically zero in a
2016-only sample — but the reporting consequence is the same.

Two limits on what this implies. First, conditional inference does not
incorporate uncertainty about **which** coordinates are active; the paper makes
no unconditional active-set claim. Second, the `NA` entries are a statement
about the absence of a defined symmetric interval, not a statement that the
coordinates are unimportant: `beta_l_age2_sm` and `beta_l_age2_sf` enter the
leisure specification and therefore enter the money-metric welfare object like
any other preference coordinate.

---

## A.5 Regional access battery at full precision

Restrictions are selected by parameter name rather than by position in the
parameter vector. The restriction set of H0-A is, verbatim:
`beta_E_gsur; beta_E_drgn2; beta_E_drgn3; beta_E_drgn4; beta_E_drgn5;
beta_E_drgn6; beta_E_drgn7; beta_E_drgn8; beta_E_drgur; beta_E_drgmd`.

**Table A.2. Wald tests on the regional access block, full precision.**

| Null | df | *W* (model) | *p* (model) | *W* (robust) | *p* (robust) | Same side of 0.05 |
|---|---:|---|---|---|---|---|
| H0-A | 10 | 36.254933058284301 | 7.6092403707792337e-05 | 37.446975959270233 | 4.7351579328540456e-05 | yes (reject) |
| H0-B | 7 | 5.8727461336166895 | 0.55468440309732081 | 5.5406502206474828 | 0.59428532005685808 | yes (fail to reject) |
| H0-C | 2 | 0.34026532887756678 | 0.84355289970082881 | 0.33158415259614427 | 0.84722237348924945 | yes (fail to reject) |
| H0-G | 1 | 27.483391678525457 | 1.5844935333993574e-07 | 29.208167292116848 | 6.5e-08 | yes (reject) |

*Source: `phase5_regional_tests.csv`, all rows and columns, as reproduced in the
Stage-A extraction memo §2. Note on the H0-G robust *p*-value: the extraction
memo renders it at two slightly different final digits in its two locations
(`6.500461827702641e-08` in the claim text and `6.500461827702638e-08` in the
table). This appendix reports the charter's rendering `6.5e-08` and refers a
correction of the extraction memo to the Goal 1 Manager (see item A-4 of the
Stage-B cover note). The discrepancy is in the sixteenth significant figure and
affects no reported verdict.*

Robust 95% intervals reported anywhere in the paper use
`z₀.₉₇₅ = 1.959963984540054`, taken verbatim from the accepted diagnostics, and
are computed as `estimate ± z₀.₉₇₅ × robust standard error` for interior
coordinates only.

---

## A.6 The `W-4` near-boundary diagnostic

`W-4` is a pre-registered, non-gating check on whether a robust symmetric
interval reaches the boundary of the admissible parameter region. It flagged two
coordinates.

**Table A.3. Coordinates flagged by `W-4`.**

| Parameter | Robust CI low | Robust CI high | Lower bound | Upper bound |
|---|---|---|---|---|
| `beta_l0_sm` | −0.12309900960568587 | 9.683896877332586 | 0.05 | 50.0 |
| `beta_w_pexp2` | −0.1014429187847586 | 0.07539182354674019 | −0.1 | 0.1 |

For `beta_l0_sm` the interval extends well below a lower bound of `0.05`; for
`beta_w_pexp2` the interval's lower endpoint sits marginally below the lower
bound of `−0.1`. Both point estimates remain strictly interior.

The accepted routing treats this as Tier 1 of the project's boundary-inference
escalation ladder. Concretely, the warning is non-gating; it does not invalidate
the accepted estimate; it does not reopen the estimation phase; it does not
require boundary-aware inference at this stage; and it must remain visible in
this appendix and in the welfare and decomposition work. It is not elevated into
a headline result. Tier 2 — boundary-aware or resampling inference — becomes
mandatory only if a direct inferential claim is made about a flagged coordinate,
if the welfare or decomposition functional loads materially on it, or if the
paper makes an unconditional active-set claim. None of these has occurred in the
inference section.

---

## A.7 Pre-registered welfare sensitivity design (S-10 Tier 1)

The welfare and decomposition stage inherits a fixed diagnostic, pre-registered
before any welfare number is computed and reproduced here so that it can be
audited against what is eventually reported.

**Perturbation rule.** For each flagged coordinate *j* with accepted estimate
`θ̂ⱼ`, robust standard error `se^rob_j` and relevant lower bound `lb_j`:

  `Δⱼ = min{ 0.5 · se^rob_j , 0.5 · (θ̂ⱼ − lb_j) }`,  `θ^sens_j = θ̂ⱼ − Δⱼ`.

The perturbation moves the coordinate toward the flagged boundary while
remaining strictly inside the admissible region and no more than one-half robust
standard error from the accepted estimate. The exact numerical values of the
estimate, robust standard error, bound, distance to bound, selected perturbation
and resulting sensitivity value are recorded before execution; no rounding may
move a value onto or outside a bound.

**Scenarios.** Exactly four, with no search over additional points: (1) the
accepted baseline vector; (2) `beta_l0_sm` at its sensitivity value; (3)
`beta_w_pexp2` at its sensitivity value; (4) both coordinates moved jointly.
Every non-flagged parameter, the opportunity and access parameters, the job draws
and canonical seeds, the tax-benefit mapping, the sample, the welfare
normalisation, the inequality index and the decomposition rule are held fixed. No
parameter is re-estimated.

**Reported per scenario.** Mean money-metric welfare; median money-metric
welfare; the welfare Gini; the headline inequality index if different; the
opportunity-attributable inequality component; the preference-related component;
the opportunity share of total measured welfare inequality; the subgroup
summaries already pre-registered for the baseline; and numerical convergence and
invariance diagnostics. All changes are reported continuously, including those
below the thresholds. The preference-related component is not labelled as
responsibility.

**Material-loading thresholds.** A flagged coordinate is materially
welfare-relevant if its individual or joint scenario produces any one of: a
change of at least 1 percent in mean or median money-metric welfare; an absolute
change of at least 0.005 in the welfare Gini; a change of at least 2 percentage
points in the opportunity-attributable share; a sign or ordering change in a
headline decomposition component; or a change in the paper's qualitative
conclusion about the importance of opportunity heterogeneity.

**Escalation.** If no threshold is breached, the accepted baseline is retained,
the sensitivity is reported in this appendix, and the main welfare conclusions
are described as locally stable. If any threshold is breached, final paper-facing
welfare claims are halted pending a bounded design for boundary-aware or
resampling inference for the affected functional, or an admissible
profile/sensitivity analysis targeted to that coordinate. Re-estimation of the
whole model is not an automatic consequence.

**Interpretation limits.** This diagnostic does not establish coverage for
parameter uncertainty, does not replace confidence intervals for welfare
functionals, does not prove global robustness, does not assign normative
responsibility to preferences, and does not change the accepted estimator. It
answers one question: whether the headline welfare and opportunity-decomposition
conclusions are locally sensitive to the two empirically flagged coordinates.

---

## A.8 Pre-registered wage-density robustness (LOC4)

The paper-facing baseline is the certified specification reported in the main
section: one log-wage density with a common dispersion parameter, shifted in
location by education, potential experience and occupation. The LOC4
four-density variant, in which the existing occupation grouping carries its own
wage densities, is pre-registered as the **first mandatory wage-density
robustness axis**. It has not been estimated and no LOC4 result appears in this
paper.

The contract governing that exercise is fixed in advance. It uses the existing
LOC4 grouping definition; it changes only the pre-registered wage-density
component; it preserves the sample, the utility specification, the access index,
the tax-benefit mapping, the welfare metric, the inequality index and the
decomposition rule; it documents whether mean and/or dispersion changes are
introduced; it guards against double counting between occupation-access
coefficients and wage-density shifts; and it compares the same headline welfare
and decomposition outputs. Sex-specific occupation densities, industry
enrichment, external regional covariates and alternative grouping searches are
excluded from it.

The variant counts as materially different if any one of the following occurs:
the opportunity-attributable inequality share changes by at least 2 percentage
points; the welfare Gini changes by at least 0.005; mean or median money-metric
welfare changes by at least 1 percent; the sign or ordering of a headline
decomposition component changes; or the paper's qualitative conclusion about the
importance of opportunity heterogeneity changes. If none occurs, the certified
baseline is retained as the preferred specification and LOC4 is reported as
robustness. If any occurs, the preferred specification is reconsidered before
final paper-facing quantitative claims.

Sequencing is therefore: baseline welfare and decomposition prototype on the
certified specification; then the LOC4 four-density robustness; only then a
freeze of the preferred quantitative welfare results. Industry enrichment and
external regional covariates remain deferred under the same governing ruling.

---

## A.9 What this appendix does not establish

Four limits, stated explicitly because each is a plausible misreading.

1. **The regional battery tests one access channel.** H0-A restricts the named
   ten-coordinate regional/urbanisation/GSUR block. The hours-access block and
   the occupation-access block are not part of any null tested, so nothing in
   Table 1 or Table A.2 is a test of the opportunity mechanism as a whole.
2. **Agreement between variance estimators is not evidence of correct
   specification.** The four verdicts coincide under the model-based and robust
   covariances. That is stability of the verdicts. Specification testing beyond
   the reported battery is not attempted here.
3. **Statistical rejection is not causal identification.** All statements are
   statements about an estimated structural model. None is a claim about the
   causal effect of location, occupation or hours on employment outcomes, and
   none supports a policy conclusion.
4. **No normative interpretation is carried in this appendix.** The
   opportunity-attributable and preference-related components are labelled as
   such. The paper's responsibility-sensitive framework is developed elsewhere
   and is not invoked here.

---

## A.10 Items not carried by the Stage-A extraction

The following are outside the scope of the accepted-result extraction and are
therefore **not** stated anywhere in the inference section or this appendix.
They are listed so that a reader does not mistake their absence for a claim, and
so that the drafting of the data and specification sections can supply them from
their own sources.

- Sample-construction filters for the P2a estimation sample beyond the household
  count of 1,555.
- The identity of the omitted or reference category in the hours-access,
  occupation-access, regional and education specifications.
- Any substantive labelling of the `gsur` design column beyond its identity as a
  design column.
- The bounds of interior coordinates other than the two recorded for the `W-4`
  flagged coordinates, and the numerical values of the Karush-Kuhn-Tucker
  multipliers at the two active bounds.
- Per-coordinate *z*-statistics, *p*-values and robust-to-model standard-error
  ratios. These exist in the source parameter table but are not carried into the
  parameter reporting map, so precision is expressed in this paper through robust
  confidence intervals only.
- The numerical values of the S-10 perturbations `Δⱼ` and sensitivity values
  `θ^sens_j`, which are recorded by the welfare mission before its execution and
  are not computed here.

---

## A.11 Rendering conventions

- Estimates, standard errors and confidence-interval endpoints in the main
  section's Table 2 are rendered to three decimal places, rounded
  half-away-from-zero, from the full-precision entries of the parameter
  reporting map. The reporting map is authoritative. One consequence worth
  recording: `beta_occ_4_f` has full-precision estimate `0.85450203950514481`
  and therefore renders as `0.855` at three decimals, whereas earlier
  management-facing summaries quote the truncated `0.854`.
- The pinned coordinate `beta_l0_m` has full-precision value
  `9.9999999999999995e-07`; it is rendered as `0.000001` rather than as `0.000`,
  to avoid presenting a pinned non-zero value as an exact zero.
- Headline figures that the mission charter and the extraction memo themselves
  quote at coarser precision — `beta_E_gsur = -1.105`, its robust interval
  `[-1.51, -0.70]`, robust Wald `37.45` and `29.21`, robust *p*-values `4.7e-05`
  and `6.5e-08` — are reproduced verbatim in the prose of the main section at
  that precision.
- Economic labels are reproduced from the parameter reporting map with the
  double-hyphen separator typeset as an em dash and, in the panel tables, with
  the sample and block prefix carried by the panel or column heading rather than
  repeated in every row.
