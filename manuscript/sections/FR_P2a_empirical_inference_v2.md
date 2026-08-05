# Estimation Results and Inference

*Note on reporting.* Estimates, standard errors and confidence-interval
endpoints are reported to three decimal places. Wald statistics are reported to
two decimal places, and *p*-values to three significant figures, or to two
significant figures in scientific notation where the value is below 0.001;
full-precision values for the hypothesis-test battery are given in Appendix A.
Parameter names appear in code form so that each row of Table 2 maps one-to-one
onto the released parameter table. Paragraphs headed **Interpretation** are the
authors' reading of the estimates rather than a restatement of them.

---

## 5.1 Estimation sample and inference framework

The estimates reported in this section come from the France 2016 single-adult
(P2a) region-live specification. The estimation sample contributes **1,555
household observations**, and inference is computed by clustering the
likelihood contributions at the household level, giving 1,555 clusters.

Inference uses a sandwich covariance estimator. The bread is the accepted
Hessian of the constrained quasi-maximum-likelihood objective at the accepted
optimum; the meat is built from the streamed per-household score aggregate. The
score aggregate was validated against the independently computed Phase-4
gradient, with a maximum absolute deviation of `1.4566126083082054e-13`. A
finite-sample
correction scalar of `1555/1520` is applied, which follows the
`[G/(G−1)] × [(N−1)/(N−K)] = G/(G−K)` convention with `G = 1555` clusters,
`N = 1555` observations and `K = 35` estimated interior coordinates. The
correction therefore inflates every standard error by the common factor
`√c`, slightly above one percent; it is a reporting convention of the HC1/CR1
family and no conclusion in this section turns on it. Both the model-based and
the robust covariance matrices are reported throughout, and no per-household
score is retained at row level in the released artifacts.

The parameter vector has 47 coordinates. Ten are pinned by construction and are
not estimated in this sample; of the 37 free coordinates, two sit at an active
upper bound, so the covariance object that supports symmetric inference is
**conditional and 35-dimensional**. All reported standard errors, confidence
intervals and Wald statistics are therefore conditional on the observed active
set. The two active-bound coordinates, and the ten pinned coordinates, carry
literal `NA` in every inferential field rather than a number; §5.4 explains why.
Restrictions for the hypothesis tests below are selected by parameter name, not
by position in the parameter vector.

**Interpretation.** The P2a sample is constructed as a single-adult sample, so
each household contributes one likelihood term; this is a design feature of the
sample documented in the sample section, not a property established by the
inference artifacts used here. Conditional on it, clustering at the household
level is not correcting for within-cluster dependence, and the robust standard
errors should be read as **misspecification-robust** rather than
dependence-robust.

---

## 5.2 Does the regional access channel belong in the model?

The opportunity environment in this model has several channels. Job packages
differ in the hours they carry, in the occupation they belong to, and in the
regional labour market in which they are located; each channel has its own block
of access parameters. This subsection tests **one** of those channels — the
regional, urbanisation and GSUR access block. It is not a test of the opportunity
mechanism as a whole: the hours-access block (`beta_E`, `beta_h_pt1`,
`beta_h_pt2`, `beta_h_ft`, `beta_h_lh`) and the occupation-access block are not
part of any null tested here, and their estimates are reported separately in
§5.3.

Four nulls are tested, all as Wald restrictions on named coordinates and all
reported under both variance estimators.

**Table 1. Regional access hypothesis battery, France 2016 P2a.**

| Null | Restricted coordinates | df | *W* (model) | *p* (model) | *W* (robust) | *p* (robust) | Verdict |
|---|---|---:|---:|---:|---:|---:|---|
| H0-A | `beta_E_gsur`, `beta_E_drgn2`–`beta_E_drgn8`, `beta_E_drgur`, `beta_E_drgmd` | 10 | 36.25 | 7.6e-05 | 37.45 | 4.7e-05 | Reject |
| H0-B | `beta_E_drgn2`–`beta_E_drgn8` (NUTS-1 dummies) | 7 | 5.87 | 0.555 | 5.54 | 0.594 | Fail to reject |
| H0-C | `beta_E_drgur`, `beta_E_drgmd` (urbanisation) | 2 | 0.34 | 0.844 | 0.33 | 0.847 | Fail to reject |
| H0-G | `beta_E_gsur` | 1 | 27.48 | 1.6e-07 | 29.21 | 6.5e-08 | Reject |

*Source: `phase5_regional_tests.csv`, all rows. Full-precision values are in
Appendix A, Table A.2.*

**Claim 1 — the regional access block is jointly relevant.** H0-A restricts all
ten coordinates of the regional/urbanisation/GSUR access block to zero and is
rejected: robust Wald `37.45` on 10 degrees of freedom, robust *p*-value
`4.7e-05`. This is a confirmatory test of a named ten-parameter block that was
specified before estimation. It establishes that regional job-access
heterogeneity belongs in the model; it does not establish anything about the
hours-access or occupation-access blocks.

**Claim 2 — the rejection is concentrated in the GSUR dimension.** Within the
same block, the joint restriction on the seven NUTS-1 region dummies is not
rejected (H0-B, robust *p* = `0.594`), and the joint restriction on the two
urbanisation indicators is likewise not rejected (H0-C, robust *p* = `0.847`),
while the restriction on the single GSUR coordinate is rejected on its own
(H0-G, robust Wald `29.21`, robust *p* = `6.5e-08`). The point estimate is `beta_E_gsur = -1.105` with robust 95%
interval `[-1.51, -0.70]`. The paper's statement of this result is deliberately
bounded:

> At the resolution and specification studied, measured access heterogeneity is
> concentrated in one GSUR dimension rather than diffuse across broad NUTS-1
> geography or the two urbanisation indicators.

No substantive label is attached to `gsur` beyond the design-column identity
recorded in the parameter map; the coordinate is reported as the GSUR access
dimension and nothing further is asserted about what it measures.

**Claim 3 — the verdicts do not depend on the variance estimator.** For all four
nulls the model-based and robust statistics fall on the same side of
conventional thresholds, so no rejection or non-rejection in Table 1 is an
artifact of the covariance choice. This is stability of the test verdicts. It is
not evidence that the model is correctly specified, and it should not be read
that way.

**Interpretation.** Two points bound how much weight this battery can carry.
First, the ten restrictions in H0-A are exactly the seven NUTS-1 dummies, the
two urbanisation indicators and the single GSUR coordinate, so the three
sub-block tests exhaust the joint test's restriction set. Second, the bounded
statement above describes the pattern of the three marginal test outcomes and
nothing more: a failure to reject H0-B or H0-C is not evidence that the
coordinates in question are zero, and the battery is silent about regional
dimensions that are not among the tested coordinates. All statements here are
statements about an estimated structural model; none is a causal claim about the
effect of location on employment, and none supports a policy conclusion.

---

## 5.3 Parameter estimates

Table 2 reports all 47 coordinates in the original parameter order, grouped into
five economic panels. Rows are **not** ranked by statistical significance.
Interior coordinates carry a model-based standard error, a robust standard
error, and a robust 95% interval computed as
`estimate ± 1.959963984540054 × robust standard error`. Active-bound and pinned
coordinates carry literal `NA` in all four inferential fields.

**Table 2. Parameter estimates, France 2016 P2a region-live, 47 coordinates.**

### Panel 1 — Preferences

| Parameter | Source block | Economic label | Status | Estimate | SE (model) | SE (robust) | Robust 95% CI |
|---|---|---|---|---:|---:|---:|---|
| `beta_l0_sm` | singles male leisure | Leisure utility — intercept | interior | 4.780 | 1.782 | 2.502 | [−0.123, 9.684] |
| `beta_l_age_sm` | singles male leisure | Leisure utility — age slope | interior | 0.360 | 1.131 | 1.132 | [−1.860, 2.579] |
| `beta_l_age2_sm` | singles male leisure | Leisure utility — age-squared slope | active bound (upper) | 1.000 | NA | NA | NA |
| `theta_l_sm` | singles male leisure | Leisure — Box-Cox curvature | interior | −2.341 | 0.352 | 0.254 | [−2.838, −1.844] |
| `beta_l0_sf` | singles female leisure | Leisure utility — intercept | interior | 7.812 | 2.570 | 3.958 | [0.055, 15.569] |
| `beta_l_age_sf` | singles female leisure | Leisure utility — age slope | interior | −0.837 | 1.305 | 1.084 | [−2.961, 1.287] |
| `beta_l_age2_sf` | singles female leisure | Leisure utility — age-squared slope | active bound (upper) | 1.000 | NA | NA | NA |
| `beta_l_nkids_sf` | singles female leisure | Leisure utility — number-of-children slope | interior | 1.877 | 1.589 | 1.489 | [−1.040, 4.795] |
| `theta_l_sf` | singles female leisure | Leisure — Box-Cox curvature | interior | −1.985 | 0.274 | 0.301 | [−2.575, −1.394] |
| `theta_c_singles` | singles consumption | Consumption — Box-Cox curvature | interior | 0.093 | 0.046 | 0.077 | [−0.057, 0.244] |
| `beta_l0_m` | couples male leisure | Leisure utility — intercept | pinned | 0.000001 | NA | NA | NA |
| `beta_l_age_m` | couples male leisure | Leisure utility — age slope | pinned | −0.067 | NA | NA | NA |
| `beta_l_age2_m` | couples male leisure | Leisure utility — age-squared slope | pinned | 0.088 | NA | NA | NA |
| `beta_l0_f` | couples female leisure | Leisure utility — intercept | pinned | 10.052 | NA | NA | NA |
| `beta_l_age_f` | couples female leisure | Leisure utility — age slope | pinned | −1.780 | NA | NA | NA |
| `beta_l_age2_f` | couples female leisure | Leisure utility — age-squared slope | pinned | 1.000 | NA | NA | NA |
| `beta_l_nkids_f` | couples female leisure | Leisure utility — number-of-children slope | pinned | 0.586 | NA | NA | NA |
| `theta_l_f` | couples female leisure | Leisure — Box-Cox curvature | pinned | −2.132 | NA | NA | NA |

*The eight couples leisure coordinates are pinned because they are structurally
inapplicable in this sample: they are not referenced by the singles objective.
They are retained in the table for completeness of the 47-coordinate vector and
carry no inferential content here.*

### Panel 2 — Employment and hours access

*Source block: `opportunity_hours` for all rows.*

| Parameter | Economic label | Status | Estimate | SE (model) | SE (robust) | Robust 95% CI |
|---|---|---|---:|---:|---:|---|
| `beta_E` | Hours-access level shifter | interior | −2.897 | 0.366 | 0.362 | [−3.606, −2.189] |
| `beta_h_pt1` | Part-time (band 1) hours-access shifter | interior | −1.277 | 0.163 | 0.167 | [−1.605, −0.949] |
| `beta_h_pt2` | Part-time (band 2) hours-access shifter | interior | −0.981 | 0.179 | 0.186 | [−1.346, −0.616] |
| `beta_h_ft` | Full-time hours-access shifter | interior | 0.887 | 0.067 | 0.075 | [0.740, 1.034] |
| `beta_h_lh` | Long-hours hours-access shifter | interior | −1.453 | 0.115 | 0.141 | [−1.728, −1.177] |

### Panel 3 — Regional access

| Parameter | Source block | Economic label | Status | Estimate | SE (model) | SE (robust) | Robust 95% CI |
|---|---|---|---|---:|---:|---:|---|
| `beta_E_gsur` | regional access | Regional access, GSUR dimension (design column `gsur`) | interior | −1.105 | 0.211 | 0.204 | [−1.505, −0.704] |
| `beta_E_drgn2` | regional access | NUTS-1 region dummy 2 (design column `reg2`) | interior | −0.205 | 0.311 | 0.311 | [−0.815, 0.405] |
| `beta_E_drgn3` | regional access | NUTS-1 region dummy 3 (design column `reg3`) | interior | −0.089 | 0.369 | 0.363 | [−0.800, 0.623] |
| `beta_E_drgn4` | regional access | NUTS-1 region dummy 4 (design column `reg4`) | interior | −0.690 | 0.345 | 0.360 | [−1.395, 0.015] |
| `beta_E_drgn5` | regional access | NUTS-1 region dummy 5 (design column `reg5`) | interior | −0.265 | 0.309 | 0.317 | [−0.887, 0.356] |
| `beta_E_drgn6` | regional access | NUTS-1 region dummy 6 (design column `reg6`) | interior | −0.522 | 0.327 | 0.332 | [−1.173, 0.129] |
| `beta_E_drgn7` | regional access | NUTS-1 region dummy 7 (design column `reg7`) | interior | −0.388 | 0.335 | 0.336 | [−1.046, 0.271] |
| `beta_E_drgn8` | regional access | NUTS-1 region dummy 8 (design column `reg8`) | interior | −0.309 | 0.323 | 0.329 | [−0.953, 0.336] |
| `beta_E_y2015` | market year | Survey-year 2015 dummy | pinned | −0.255 | NA | NA | NA |
| `beta_E_y2017` | market year | Survey-year 2017 dummy | pinned | −0.069 | NA | NA | NA |
| `beta_E_drgur` | regional access | Urbanisation indicator, rural (design column `drgur`) | interior | −0.010 | 0.201 | 0.208 | [−0.418, 0.398] |
| `beta_E_drgmd` | regional access | Urbanisation indicator, medium density (design column `drgmd`) | interior | 0.109 | 0.238 | 0.243 | [−0.368, 0.585] |

*The two survey-year dummies are pinned because the corresponding covariates are
identically zero in the 2016-only estimation sample. They belong to the same
opportunity/access equation as the regional coordinates and are reported in this
panel for that reason.*

### Panel 4 — Occupation access

*Source block: `opportunity_occupation` for all rows.*

| Parameter | Economic label | Status | Estimate | SE (model) | SE (robust) | Robust 95% CI |
|---|---|---|---:|---:|---:|---|
| `beta_occ_2_m` | Male, occupation group 2 shifter | interior | −1.303 | 0.147 | 0.158 | [−1.613, −0.993] |
| `beta_occ_3_m` | Male, occupation group 3 shifter | interior | −1.886 | 0.189 | 0.199 | [−2.276, −1.496] |
| `beta_occ_4_m` | Male, occupation group 4 shifter | interior | 0.253 | 0.090 | 0.095 | [0.067, 0.440] |
| `beta_occ_2_f` | Female, occupation group 2 shifter | interior | −0.076 | 0.117 | 0.123 | [−0.317, 0.166] |
| `beta_occ_3_f` | Female, occupation group 3 shifter | interior | −0.461 | 0.129 | 0.135 | [−0.725, −0.197] |
| `beta_occ_4_f` | Female, occupation group 4 shifter | interior | 0.855 | 0.096 | 0.099 | [0.660, 1.049] |

### Panel 5 — Wage density

*Source block: `wage_density` for all rows.*

| Parameter | Economic label | Status | Estimate | SE (model) | SE (robust) | Robust 95% CI |
|---|---|---|---:|---:|---:|---|
| `beta_w0` | Location intercept | interior | 2.140 | 0.043 | 0.056 | [2.031, 2.249] |
| `beta_w_educL` | Location, low-education shifter | interior | 0.029 | 0.037 | 0.042 | [−0.054, 0.112] |
| `beta_w_educH` | Location, high-education shifter | interior | 0.345 | 0.026 | 0.028 | [0.291, 0.399] |
| `beta_w_pexp` | Location, potential-experience slope | interior | 0.238 | 0.083 | 0.101 | [0.041, 0.436] |
| `beta_w_pexp2` | Location, potential-experience-squared slope | interior | −0.013 | 0.039 | 0.045 | [−0.101, 0.075] |
| `sigma` | Common dispersion (log-normal σ) | interior | 0.413 | 0.008 | 0.015 | [0.383, 0.443] |

*Source for Table 2: `FR_P2a_phase5_parameter_reporting_map_v1.csv`
(SHA-256 `89a0465c…`), itself copied verbatim from `phase5_parameter_table.csv`.
Panel assignment and economic labels follow the reporting map.*

**Interpretation.** Taking the robust intervals at face value, the coordinates
whose intervals exclude zero are: all five hours-access coefficients;
`beta_E_gsur` alone among the ten regional and urbanisation coefficients; five
of the six occupation-access coefficients, all but `beta_occ_2_f`; `beta_w0`,
`beta_w_educH`, `beta_w_pexp` and `sigma` in the wage-density block, but not
`beta_w_educL` or `beta_w_pexp2`; and, on the preference side, `theta_l_sm`,
`theta_l_sf` and `beta_l0_sf`, but not the two age slopes, `beta_l_nkids_sf`,
`beta_l0_sm` or `theta_c_singles`. Two further leisure coordinates sit at a
bound and carry no interval at all.

Three observations follow. First, within the hours block the full-time
coefficient is positive while the two part-time coefficients and the long-hours
coefficient are negative; because the omitted reference category is not
documented in the artifacts used here (Appendix A.10), these remain
coefficient-sign statements rather than statements about relative availability,
and the same qualification applies to the education shifters in the wage-density
block. Second, the occupation-access coefficients are estimated separately by
sex and, while sharing a common sign pattern across the three groups, differ in
magnitude between men and women — most visibly in group 4, where the female
coefficient is several times the male one. Third, money-metric welfare is
constructed from the preference coordinates, several of which have wide robust
intervals; the specific diagnostic that the welfare stage inherits, however, is
routed by the `W-4` near-boundary check and applies to two named coordinates,
`beta_l0_sm` and `beta_w_pexp2`, as set out in §5.5.

---

## 5.4 Active bounds, pinned coordinates, and the `NA` convention

Two free coordinates — `beta_l_age2_sm` and `beta_l_age2_sf`, the age-squared
slopes in the singles male and singles female leisure terms — are at their
**upper** bound at the accepted optimum. They are excluded from ordinary
symmetric inference and reported with literal `NA` in every inferential field.

The reason is the structure of the constrained optimum rather than a numerical
difficulty. At an interior optimum the usual argument delivers an asymptotically
normal, two-sided approximation to the sampling distribution of the estimator,
and a Wald standard error with its symmetric interval is the natural summary.
Where a coordinate is at an active bound, that unconstrained symmetric normal
approximation is not licensed in the constrained direction, so ordinary
two-sided Wald inference is not reported for it, and the inference that is
reported is conditional on the observed active set. Reporting a literal `NA` —
rather than a number, a zero, or a blank — makes the reader's position explicit:
the point estimate is the constrained optimum, and no symmetric-interval
statement is being made about it.

The same convention applies for a different reason to the ten pinned
coordinates. Eight are couples leisure parameters that the singles objective does
not reference, and two are survey-year dummies whose covariates are identically
zero in a 2016-only sample. These coordinates are not estimated from this
sample's variation at all, so no standard error is defined for them either.

Two consequences follow for how everything else in this section should be read.
First, the covariance object is 35-dimensional and **conditional on the observed
active set**: the reported intervals and Wald statistics are valid given that
`beta_l_age2_sm` and `beta_l_age2_sf` are at their bound, and they do not
incorporate the uncertainty involved in which coordinates are active. The paper
makes no unconditional active-set claim anywhere. Second, the arithmetic of the
parameter vector is: 47 coordinates in total, 10 pinned, 37 free, of which 2 are
at an active bound and 35 are interior. The 35 interior coordinates are exactly
the dimension of the reported covariance, and the 37 free coordinates are the
rank of the Hessian bread.

---

## 5.5 Near-boundary intervals and the pre-registered welfare sensitivity

One pre-registered non-gating diagnostic did not pass. Two interior coordinates
have robust symmetric intervals that reach the relevant boundary of the
admissible parameter region: `beta_l0_sm`, the singles male leisure intercept
(robust interval `[-0.123, 9.684]` against a lower bound of `0.05`), and
`beta_w_pexp2`, the potential-experience-squared coefficient in the wage-density
location (robust interval `[-0.101, 0.075]` against a lower bound of `-0.1`).
The paper discloses this as follows.

> Robust symmetric intervals for `beta_l0_sm` and `beta_w_pexp2` approach the
> relevant parameter boundary. They are reported as local diagnostics and should
> not be interpreted as unrestricted evidence beyond the admissible parameter
> region. The welfare analysis therefore includes a pre-registered admissible
> local sensitivity for these coordinates.

This warning is not gating: it does not invalidate the accepted estimates, it
does not reopen estimation, and it is not elevated into a headline result. Every
gating diagnostic in the accepted Phase-5 run passed, and estimation was not
reopened.

What it does require is a pre-registered treatment at the welfare stage. Before
any welfare number is computed, the design fixes, for each flagged coordinate, a
single admissible perturbation equal to the smaller of one-half of its robust
standard error and one-half of its distance to the relevant bound, applied in the
direction of that bound. This keeps the perturbed value strictly inside the
admissible region and no more than half a robust standard error from the accepted
estimate; the exact numerical values of the estimate, robust standard error,
bound, distance to bound, perturbation and perturbed value are recorded before
execution, and no rounding is permitted to move a value onto or outside a bound.
Exactly four scenarios are computed — the accepted baseline vector,
`beta_l0_sm` perturbed alone, `beta_w_pexp2` perturbed alone, and both perturbed
jointly — with every other parameter, the access block, the job draws and seeds,
the tax-benefit mapping, the sample, the welfare normalisation, the inequality
index and the decomposition rule held fixed. No search over additional points is
performed, and no parameter is re-estimated. Each scenario reports mean and
median money-metric welfare, the welfare Gini, the chosen headline inequality
index where it differs from the Gini, the opportunity-attributable and
preference-related components of measured welfare inequality, the opportunity
share, the pre-registered subgroup summaries, and numerical convergence and
invariance diagnostics; the exhaustive list is given in Appendix A.7. All
changes are reported continuously, including changes below the materiality
thresholds. The thresholds
themselves, and the escalation rule that applies if any is breached, are stated
in Appendix A.

**Interpretation.** The economic content of this design is narrow and should be stated
narrowly. It answers one question — whether the headline welfare and
opportunity-decomposition conclusions are locally sensitive to the two flagged
coordinates — and it answers it by local perturbation of a fixed functional. It
does not establish coverage for parameter uncertainty, it does not substitute for
confidence intervals on welfare functionals, and it does not demonstrate global
robustness. The preference-related component of the decomposition is a
preference-related component and nothing more; no responsibility interpretation
is attached to it here or elsewhere in this section.

---

## 5.6 Wage-density specification and the sequencing of robustness

The estimates in Table 2 come from the certified baseline wage specification, in
which a **single log-wage density with a common dispersion parameter** is shifted
in location by education and potential experience. The occupation coefficients
reported in Panel 4 belong to the opportunity-access block and are not part of
the wage-density location.

A four-density variant, in which the LOC4 occupation grouping carries its own
wage densities, is pre-registered as the **first mandatory wage-density
robustness axis**. It has not been estimated, and no LOC4 result appears anywhere
in this paper. The sequencing that governs it is explicit: the baseline welfare
and decomposition prototype proceeds on the certified specification reported
here, and the LOC4 four-density robustness must be completed before the paper
freezes its preferred quantitative decomposition magnitudes. That robustness
exercise changes only the pre-registered wage-density component, holding the
sample, the utility specification, the access index, the tax-benefit mapping, the
welfare metric, the inequality index and the decomposition rule fixed, and it
must document explicitly whether mean and/or dispersion changes are introduced
so that occupation-access coefficients and wage-density shifts are not double
counted.

**Interpretation.** The open question is narrow and worth stating precisely for
the reader: whether allowing occupation-specific wage densities — with the mean
and/or dispersion changes this introduces documented explicitly, so that
occupation-access coefficients and wage-density shifts are not double counted —
changes the money-metric welfare functional materially. Nothing in the accepted
evidence suggests the certified baseline is invalid; the LOC4 axis is a
robustness requirement on the final magnitudes, not a defect in the estimates
reported above.

---

## Sources

- Methods items in §5.1, the score-identity deviation, the finite-sample
  correction, the 47/37/35 dimension counts and the `NA` convention:
  `score_aggregate_summary.json`, `phase5_manifest.json` and
  `phase5_diagnostics.json`.
- Table 1 and Claims 1–3: `phase5_regional_tests.csv`.
- Table 2: `phase5_parameter_table.csv`, as released in the parameter reporting
  map, from which the panel assignment and the economic labels are taken.
- §5.4 active-bound status: the status and bound-side fields of the parameter
  table.
- §5.5: the `W-4` diagnostic record and the pre-registered welfare sensitivity
  specification.
- §5.6: the pre-registered wage-density robustness ruling.

Full-precision test statistics, the construction of the covariance estimator,
and the items not carried by the accepted inference artifacts: Appendix A.
