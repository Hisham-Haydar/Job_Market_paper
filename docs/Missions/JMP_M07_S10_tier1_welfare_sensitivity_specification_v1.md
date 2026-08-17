# JMP-M07 S-10 Tier-1 Welfare Sensitivity Specification v1

**Applies to:** first welfare/decomposition mission  
**Flagged coordinates:** `beta_l0_sm`, `beta_w_pexp2`  
**Status:** Pre-registered diagnostic  
**Re-estimation:** Prohibited

## 1. Purpose

Assess whether the first welfare and decomposition results materially load on
the two coordinates flagged by W-4.

This is a local functional sensitivity. It is not an alternative estimator and
does not replace the accepted conditional-35 inference.

## 2. Baseline

Use the accepted Phase-5 parameter vector and the certified baseline welfare
pipeline.

Hold fixed:

- every non-flagged parameter;
- opportunity/access parameters;
- job draws and canonical seeds;
- tax-benefit mapping;
- sample;
- welfare normalization;
- inequality index;
- decomposition rule.

## 3. Admissible one-coordinate perturbations

For each flagged coordinate `j` with accepted estimate `theta_hat_j`, robust
standard error `se_rob_j`, and relevant lower bound `lb_j`, define:

\[
\Delta_j =
\min\left\{
0.5\,se^{rob}_j,\;
0.5\,(\widehat{\theta}_j-lb_j)
\right\},
\]

\[
\theta^{sens}_j=\widehat{\theta}_j-\Delta_j.
\]

This moves the coordinate toward the flagged boundary while remaining strictly
inside the admissible region and no more than one-half robust standard error
from the estimate.

Before execution, record the exact numerical values of:

- estimate;
- robust standard error;
- bound;
- distance to bound;
- selected perturbation;
- sensitivity value.

No rounding may move the value onto or outside the bound.

## 4. Required scenarios

Compute exactly four scenarios:

1. baseline accepted vector;
2. `beta_l0_sm` moved to its sensitivity value;
3. `beta_w_pexp2` moved to its sensitivity value;
4. both coordinates moved jointly to their sensitivity values.

Do not search over additional points during Tier 1.

## 5. Required welfare outputs

For each scenario report:

- mean money-metric welfare;
- median money-metric welfare;
- welfare Gini;
- chosen headline inequality index, if different;
- opportunity-attributable inequality component;
- preference-related component;
- opportunity share of total measured welfare inequality;
- subgroup summaries already pre-registered for the baseline;
- numerical convergence and invariance diagnostics.

Do not label the preference-related component as responsibility.

## 6. Material-loading trigger

A flagged coordinate is materially welfare-relevant if its individual or joint
scenario causes any one of:

1. at least a 1 percent change in mean or median money-metric welfare;
2. at least a 0.005 absolute change in welfare Gini;
3. at least a 2 percentage-point change in the opportunity-attributable share;
4. a sign or ordering change in a headline decomposition component;
5. a change in the paper's qualitative conclusion about the importance of
   opportunity heterogeneity.

Report all changes continuously even when below the thresholds.

## 7. S-10 escalation

### Tier 1 passes

Tier 1 is sufficient when no material-loading trigger fires.

Then:

- retain the accepted baseline;
- report the sensitivity in the appendix;
- state that the main welfare conclusions are locally stable.

### Tier 2 fires

Tier 2 becomes mandatory when any material-loading trigger fires.

The Goal 1 Manager must halt final paper-facing welfare claims and return a
bounded design proposal for:

- boundary-aware or resampling inference for the affected functional; or
- an admissible profile/sensitivity analysis targeted to that coordinate.

Do not automatically re-estimate the whole model.

## 8. Interpretation limits

This diagnostic does not:

- establish parameter uncertainty coverage;
- replace confidence intervals for welfare functionals;
- prove global robustness;
- assign normative responsibility to preferences;
- change the accepted Phase-5 estimator.

It answers one question only:

> Are the headline welfare and opportunity-decomposition conclusions locally
> sensitive to the two empirically flagged coordinates?
