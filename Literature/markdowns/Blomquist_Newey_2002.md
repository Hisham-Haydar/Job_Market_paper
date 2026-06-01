---
title: "Nonparametric Estimation with Nonlinear Budget Sets"
authors: [Soren Blomquist, Whitney Newey]
year: 2002
outlet: "Econometrica, 70(6), 2455--2480"
country_or_context: "Sweden"
population: "Married/cohabiting men aged 20--60"
data_period: "1973, 1980, 1990 (Swedish Level of Living survey)"
shelf: "nonparametric estimation / labour supply / nonlinear budget sets / series estimation / tax reform"
tags: [nonparametric, labour-supply, nonlinear-budget-sets, series-estimation, piecewise-linear, tax-reform, wage-elasticity, income-elasticity, specification-test, Hausman-model, Blomquist, Newey, Sweden, continuous-hours]
priority: "low-medium"
read_status: "extracted"
---

# Full citation

Blomquist, S., & Newey, W. (2002). Nonparametric estimation with nonlinear budget sets. *Econometrica*, 70(6), 2455--2480.

# One-sentence contribution

Develops a nonparametric series estimator for labour supply with piecewise-linear budget constraints that avoids parametric distributional assumptions, exploiting the additive structure implied by utility maximisation with convex preferences to overcome the curse of dimensionality, and finds that the standard parametric (Hausman) model substantially overestimates wage elasticities and tax reform effects for Swedish men.

# Why this paper matters

This paper provides a methodological alternative to both the Hausman (1985) parametric approach and the Van Soest (1995) discrete-choice approach for estimating labour supply with nonlinear budget sets. The key finding -- that parametric assumptions (normality of heterogeneity and measurement error) substantially bias wage elasticities upward -- is directly relevant for any structural labour supply analysis, including the discrete-choice and RURO models used in my literature. The paper demonstrates that functional form matters greatly for estimated elasticities and policy predictions.

# Core research question

Can labour supply with nonlinear (piecewise-linear) budget sets be estimated nonparametrically, and how do the resulting elasticity estimates and tax reform predictions compare with standard parametric (MLE/Hausman) estimates?

# Economic setting and context

Swedish male labour supply under three different tax systems (1973, 1980, 1990), spanning a major tax reform that substantially reduced marginal tax rates during the 1980s. Budget sets are piecewise linear with multiple kink points due to progressive taxation, housing allowances, and social security contributions. The number of budget segments varies across individuals (typically 5--10 segments).

# Model / theoretical framework

**Labour supply as conditional expectation:**
$$E[h_i | x_i] = \tilde{h}(x_i)$$
where $h_i$ = hours, $x_i$ = budget set description (intercepts, slopes, and kink points of all segments).

**Structural labour supply:** $h_i = h(x_i, v_i) + \varepsilon_i$ where $v_i$ = unobserved preference heterogeneity, $\varepsilon_i$ = measurement error. The parametric approach (Hausman) assumes $v, \varepsilon \sim N(0, \sigma^2)$.

**Key theoretical result (Theorem 2.1):** Under utility maximisation with convex preferences, the conditional expectation decomposes additively:
$$\tilde{h}(x) = \tilde{\pi}(y_J, w_J) + \sum_{j=1}^{J-1}[\mu(y_j, w_j, \ell_j) - \mu(y_{j+1}, w_{j+1}, \ell_j)]$$
where $\tilde{\pi}(y, w)$ = expected hours on a linear budget set with intercept $y$ and slope $w$, and $\mu(y, w, \ell)$ = a three-dimensional correction for each kink point $\ell_j$.

The $\tilde{\pi}(y, w)$ term is a two-dimensional function (the "basic" labour supply function), and the correction term has a difference form that is uniform over the number of budget segments. This additive structure reduces the effective dimensionality from $3J - 1$ to 3, overcoming the curse of dimensionality.

**Estimation:** Series (sieve) least squares. Two types of approximating functions:
1. Power series in $(y_J, w_J)$ for the basic labour supply term $\tilde{\pi}$.
2. Differenced power series in $(y, w, \ell)$ for the correction terms $\mu$.

Cross-validation selects the number of terms $K$. Gaussian-centered variant uses a parametric first step (MLE or IV) to centre the approximation, improving precision.

**Asymptotic theory:** Consistency and asymptotic normality are proved with convergence rates that are uniform in the number of budget segments $J$ (Theorems 4.1--4.4).

# Key objects

- **$\tilde{\pi}(y, w)$:** Conditional expectation of hours on a linear budget set. Contains information about average preferences.
- **$\mu(y, w, \ell)$:** Correction function for kink points. Analogous to the Heckman (1979) selection correction but for budget set nonlinearity rather than sample selection.
- **Wage elasticity $\hat{E}_w$:** Nonparametric: 0.03--0.11 (Table I, II). Parametric MLE: 0.123. The nonparametric estimates are 1/2 to 1/4 of the MLE estimate.
- **Tax reform effect $\hat{M}$:** Predicted percentage change in hours from the 1980→1990 Swedish tax reform. Nonparametric: 0.025--0.035 (Table I, II). Parametric MLE: 0.055. The nonparametric estimate is about 50--60% of the MLE estimate.

# Data

Swedish "Level of Living" survey, three waves: 1974 (for 1973 incomes), 1981 (1980), 1991 (1990). Married/cohabiting men aged 20--60, excluding farmers, pensioners, students, self-employed, and those with >5 weeks sick leave. Sample: 777 (1973), 864 (1980), 680 (1990), pooled = 2,321. Tax and social security data merged from fiscal authorities and National Social Insurance Board. Budget constraints computed from detailed tax rules for each year.

# Identification logic

Identified from cross-sectional variation in budget set characteristics: different wages, non-labour incomes, and housing allowances generate different budget set shapes across individuals. The major Swedish tax reform (1980→1990) provides additional variation, as the same individuals face dramatically different tax schedules. The key assumption: unobserved preference heterogeneity $v$ is independent of the budget set, and preferences are convex. Endogeneity tests (using region, age, number of children as instruments for wages) find no significant evidence of endogeneity.

# Estimation / empirical strategy

1. **Parametric (MLE):** Linear labour supply $\pi(y, w, v) = c + \beta y + \alpha w + v$, with $v \sim N(0, \sigma_v^2)$ and $\varepsilon \sim N(0, \sigma_\varepsilon^2)$. Result: $\hat{E}_w = 0.123$ (s.e. 0.0137), $\hat{E}_y = -0.022$ (s.e. 0.0037), $\hat{M} = 0.0546$ (s.e. 0.0212).

2. **Nonparametric (power series):** Raw power series approximation with cross-validation for $K$. Results in Table I: $\hat{E}_w$ ranges from 0.0295 to 0.108, $\hat{M}$ ranges from 0.0252 to 0.0380 depending on specification.

3. **Nonparametric (Gaussian-centered):** Uses parametric MLE or IV estimates to centre the series approximation. Results in Table II: $\hat{E}_w$ ranges from 0.0675 to 0.108, $\hat{M}$ ranges from 0.0244 to 0.0348.

4. **Specification tests:** Hausman tests comparing MLE vs two-step LS ($|T| = 3.28$) and MLE vs IV ($|T| = 4.64$) both reject the parametric specification at conventional levels. The source of misspecification: the distribution of $v + \varepsilon$ is non-normal (peaked, heavier tails than Gaussian -- Fig. 1).

# Treatment of preferences

Preferences are assumed convex and monotonic, which drives the additive decomposition (Theorem 2.1). Within this, preferences are left nonparametric -- the conditional expectation $\tilde{h}(x)$ is estimated without imposing a functional form on the utility function or the distribution of heterogeneity. The paper shows that the normality assumption in the standard Hausman model leads to substantial overestimation of wage elasticities: the true distribution of unobserved heterogeneity is non-normal (Fig. 1).

# Treatment of opportunities / constraints

The paper assumes individuals freely choose hours on their piecewise-linear budget constraint (wage-taker assumption). There is no demand-side modelling or job availability constraint. The condition $\Pr(h = 0 | x) = 0$ (no non-participation) is required for the main theorem; the paper notes that "such is the case for our application" (Swedish men, where very few are unemployed). For populations with significant non-participation (e.g., women), the method would need extension.

# Welfare / normative object

No welfare analysis. The paper focuses on prediction (tax reform effects) and specification testing, not on normative evaluation.

# Main findings

1. **Parametric model is misspecified:** Hausman tests reject the standard MLE specification at conventional levels. The source: non-normal distribution of heterogeneity (Fig. 1 shows a peaked, heavy-tailed distribution vs the Gaussian).

2. **Wage elasticity is much lower nonparametrically:** Nonparametric $\hat{E}_w \approx 0.03$--$0.11$ vs parametric $\hat{E}_w = 0.123$. The best-fitting specifications (highest cross-validation) give $\hat{E}_w \approx 0.08$--$0.11$, about 60--90% of MLE.

3. **Tax reform effect is substantially lower:** Nonparametric $\hat{M} \approx 0.025$--$0.035$ (2.5--3.5% increase in hours from 1980→1990 reform) vs parametric $\hat{M} = 0.055$ (5.5%). The nonparametric estimate is about 50--60% of MLE.

4. **Nonconvexities matter little:** Tests for the importance of budget set nonconvexities (from housing allowances) are not significant. The convex approximation introduces little bias.

5. **No evidence of wage endogeneity:** Tests using region, age, and children as instruments do not reject exogeneity of the budget set.

6. **Gaussian-centered estimator preferred:** Smaller bias, higher precision, more accurate standard errors than raw power series.

# Main limitations

- Requires $\Pr(h = 0 | x) = 0$: not applicable to populations with significant non-participation.
- Continuous hours model: not directly comparable to discrete-choice models (Van Soest 1995).
- Estimates the conditional mean (first moment) only: does not identify the utility function, preference distribution, or individual-level responses.
- Limited to within-sample prediction: cannot predict effects of tax reforms that generate budget sets outside the observed range.
- Swedish men only: results may not generalise to women or other populations.

# Relevance for my JMP

## possible use for methodological context on functional form sensitivity
The paper demonstrates that parametric assumptions in labour supply estimation (normality, linear labour supply) substantially affect elasticity estimates and policy predictions. This is directly relevant to Löffler et al. (2018)'s finding that modelling assumptions matter, and motivates the discrete-choice approach (which avoids continuous-hours assumptions) used in my RURO framework. The nonparametric approach is a robustness benchmark.

## possible use for the wage elasticity finding
The nonparametric wage elasticity for Swedish men (~0.08--0.11) is lower than the MLE estimate (0.123), confirming that standard parametric models may overestimate responsiveness. This aligns with the sensitivity analysis in Löffler et al. (2018) and motivates careful specification choices in my structural model.

# Research questions this paper inspires

1. Can the nonparametric approach be extended to the RURO setting, where the "budget set" is replaced by an "opportunity set" that depends on job availability? The additive decomposition (Theorem 2.1) relies on the piecewise-linear structure of the budget constraint and convex preferences. In the RURO model, the feasible set is not piecewise-linear but a random set of (hours, wage) points, which may require a different decomposition.

# Challenge to this paper

The paper assumes agents choose freely on their budget constraint (no demand-side constraints). For Swedish men in the 1970s--1990s with near-full employment, this may be reasonable. But for populations facing unemployment risk, hours restrictions, or job rationing, the conditional expectation $E[h|x]$ conflates preference heterogeneity with opportunity constraints. The RURO framework separates these: $h$ depends on both preferences and the opportunity set, and $E[h|x]$ would need to be conditioned on the opportunity density $g(h,w)$ as well as the budget set $x$.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The budget set $x_i$ maps to the pay schedule $y$ in my framework: the piecewise-linear budget constraint determines disposable income at each hours level. The paper's $\tilde{\pi}(y, w)$ is the average labour supply function on a linear budget, which would be an input to my framework's labour supply component.

[Reasonable inference for my project] The finding that non-normality of heterogeneity drives the difference between parametric and nonparametric estimates supports using flexible heterogeneity specifications (discrete mass points, random coefficients) in my structural model, rather than imposing Gaussian distributions.

[Unclear from paper] Whether the nonparametric approach can recover individual-level welfare objects (equivalent incomes) or only population averages. Since it estimates the conditional expectation only, it may not provide the individual-level preference information needed for my welfare analysis.

# Relation to Bargain et al. (2013)

Methodological contrast. Bargain et al. (2013) use discrete-choice models (Van Soest 1995 type) which impose functional form on utility but allow flexible budget constraints. Blomquist & Newey offer a nonparametric alternative that avoids utility function specification but requires continuous hours and no non-participation. The discrete-choice approach is more practical for welfare analysis (it identifies the utility function, enabling equivalent income computation), while the nonparametric approach is useful as a specification test for parametric models.

# Relation to opportunities vs preferences

The paper is about preferences (conditional on the budget set). Opportunities are not modelled: agents are assumed to freely choose hours on their budget constraint. The paper's key assumption -- that unobserved heterogeneity $v$ is independent of the budget set -- rules out the possibility that agents with limited job opportunities have different budget sets from those with rich opportunities. In the RURO framework, the budget set and the opportunity set are distinct objects, and the paper's approach would need to account for both.

# Useful quotations / formulas

**On the additive decomposition (Theorem 2.1, eq. 2.5, p. 2458):**
$$\tilde{h}(x) = \tilde{\pi}(y_J, w_J) + \sum_{j=1}^{J-1}[\mu(y_j, w_j, \ell_j) - \mu(y_{j+1}, w_{j+1}, \ell_j)]$$

**On the curse of dimensionality (p. 2456):**
"We show that utility maximization with convex preferences and budget sets imposes many restrictions that help to reduce the curse of dimensionality."

**On specification testing (p. 2471):**
"The value of $|T|$ is significant at conventional levels, providing evidence of misspecification."

**On the source of misspecification (p. 2474):**
"This suggests that within the utility maximization model the differences between the MLE and nonparametric estimates may result from $v$ and/or $\varepsilon$ being nonnormal."

**Key elasticity comparison (p. 2470, 2472-2473):**
MLE: $\hat{E}_w = 0.123$ (s.e. 0.0137), $\hat{M} = 0.0546$ (s.e. 0.0212).
Nonparametric (best): $\hat{E}_w \approx 0.08$--$0.11$, $\hat{M} \approx 0.025$--$0.035$.

# Suggested tags

nonparametric, labour-supply, nonlinear-budget-sets, series-estimation, piecewise-linear, tax-reform, wage-elasticity, income-elasticity, specification-test, Hausman-model, curse-of-dimensionality, Blomquist, Newey, Sweden, continuous-hours, convex-preferences

# My quick takeaway

A technically important paper showing that standard parametric labour supply models (Hausman/MLE) overestimate wage elasticities and tax reform effects due to normality assumptions about heterogeneity. The nonparametric approach finds wage elasticities 50--90% of MLE and tax reform effects about 60% of MLE for Swedish men. For my JMP, this motivates flexible heterogeneity specifications in structural models and serves as a caution against over-reliance on distributional assumptions. The main limitation: the approach requires continuous hours and no non-participation, making it less applicable to populations with significant extensive-margin responses.
