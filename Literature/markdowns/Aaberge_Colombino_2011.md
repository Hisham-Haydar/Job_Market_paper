---
title: "Empirical Optimal Income Taxation"
authors: [Rolf Aaberge, Ugo Colombino]
year: 2011
outlet: "ChilD Working Paper n. 16/2011"
country_or_context: "Norway"
population: "Married/cohabiting couples, single females, single males; ages 20--62"
data_period: "1994 (with out-of-sample validation on 2001)"
shelf: "structural labour supply / optimal taxation / welfare evaluation"
tags: [RURO, discrete-choice, optimal-taxation, piecewise-linear, common-welfare, rank-dependent-SWF, microsimulation, Norway, out-of-sample, Bonferroni, Gini]
priority: "high"
read_status: "extracted"
---

# Full citation

Aaberge, R., & Colombino, U. (2011). Empirical Optimal Income Taxation. *ChilD Working Paper* n. 16/2011.

# One-sentence contribution

Combines a 78-parameter structural RURO labour supply model estimated on Norwegian 1994 data with numerical optimization over a 9-parameter piecewise-linear tax function to compute empirically optimal income taxes under four rank-dependent social welfare criteria, finding monotonically increasing marginal tax rates with lower rates on low/average incomes than the 1994 system and a binding upper constraint (75%) on the top rate.

# Why this paper matters

This is an intermediate version between Aaberge & Colombino (2006, Discussion Paper 475) and the published Aaberge & Colombino (2013, Scandinavian Journal of Economics). Relative to the 2006 version, it: (i) expands the tax instrument from 6 to 9 parameters (adding a lump-sum transfer $T$ and a third kink point), (ii) constrains the top MTR $\tau_4 \leq 0.75$, (iii) drops the Equality of Opportunity (EOp) criteria and focuses exclusively on Equality of Outcome (EO), and (iv) adds an out-of-sample prediction exercise (1994$\to$2001) validating the structural model. The paper demonstrates the full pipeline from structural estimation to optimal policy design and provides the most detailed exposition of the common welfare function $V(y, h)$ used for interpersonal comparability.

# Core research question

What is the empirically optimal piecewise-linear income tax schedule in Norway, given a structurally estimated labour supply model that accounts for heterogeneous preferences and opportunity constraints, under rank-dependent social welfare functions with varying degrees of inequality aversion?

# Economic setting and context

Norway 1994: progressive individual income tax with top MTR ~49.5%, high female participation (~75%), flexible part-time labour market, moderate inequality (Gini ~0.25 disposable income). The 1992 tax reform had recently flattened the rate structure relative to the 1980s.

# Model / theoretical framework

**Positive model:** The RURO (Random Utility Random Opportunity) job-choice model of Dagsvik (1994), estimated as a 78-parameter structural model following Aaberge, Colombino & Strøm (1999) and Aaberge & Colombino (2006). Households choose from a latent set of jobs characterized by hours $h$, wages $w$, and non-pecuniary attributes, subject to opportunity densities $p(h, w)$ that vary by demographics and region.

**Normative framework:** Four rank-dependent social welfare functions $W_k$ indexed by inequality aversion $k \in \{1, 2, 3, \infty\}$:
$$W_k = \int_0^1 p_k(t) F^{-1}(t) \, dt$$
where $F^{-1}(t)$ is the quantile function of the welfare distribution and $p_k(t)$ are weight functions: $k=1$ (Bonferroni, most egalitarian), $k=2$ (Gini), $k=\infty$ (utilitarian, no inequality aversion). The welfare distribution is computed using a **common welfare function** $V(y, h)$ for interpersonal comparability.

**Policy instrument:** A 9-parameter piecewise-linear tax function:
$$\text{Tax}(Y) = \max\{0, \tau_1(Y - E)\} + \tau_2 \max\{0, Y - Z_1\} + \tau_3 \max\{0, Y - Z_2\} + \tau_4 \max\{0, Y - Z_3\} - T$$
with exemption $E$, four marginal rates $\tau_1 \leq \tau_2 \leq \tau_3 \leq \tau_4 \leq 0.75$, three kink points $Z_1 < Z_2 < Z_3$, and lump-sum transfer $T$ (can be negative, i.e., a lump-sum tax).

**Framework:** Both positive (behavioural prediction) and normative (social welfare maximization).

# Key objects

- **Common welfare function** $V(y, h)$: used for interpersonal comparability across households with different preferences. Estimated parameters: $\gamma_1 = -0.649$, $\gamma_2 = 3.026$, $\gamma_3 = -12.262$, $\gamma_4 = 0.045$.
$$V(y, h) = \gamma_2 \frac{y^{\gamma_1} - 1}{\gamma_1} + \gamma_4 \frac{L^{\gamma_3} - 1}{\gamma_3}, \quad L = 1 - h/8760$$
- **Rank-dependent SWF** $W_k$: nests Bonferroni ($k=1$), Gini ($k=2$), and utilitarian ($k=\infty$) as special cases.
- **Opportunity density** $p(h, w) = p^0 \cdot g_1(h) \cdot g_2(w|h)$: with peaks at part-time and full-time hours.
- **Lump-sum transfer** $T$: a new policy parameter not in the 2006 version; optimal values are negative (lump-sum tax), ranging from $-2{,}800$ to $-11{,}900$ NOK.

# Data

Norwegian 1994 data from Statistics Norway: 1,842 married/cohabiting couples, 309 single females, 312 single males, ages 20--62. Administrative tax records merged with survey data. Same data as Aaberge & Colombino (2006). For the out-of-sample validation, 2001 data with updated demographics and tax rules are used.

# Identification logic

Identification follows the standard RURO approach (Aaberge et al. 1999; Aaberge & Colombino 2006):
- **Utility parameters:** Identified from non-linearities in the tax-benefit function across income levels and household types.
- **Opportunity density parameters:** Identified from the hours distribution (peaks at part-time/full-time), wage distributions, and participation rates.
- **Common welfare function $V(y, h)$:** Estimated separately — parameters $\gamma_1, \ldots, \gamma_4$ are fitted to match a reference preference ordering used for interpersonal comparability. The estimation method is not detailed in this paper but follows the approach described in Aaberge & Colombino (2008).

# Estimation / empirical strategy

1. **Structural estimation:** 78-parameter RURO model estimated by maximum likelihood on 1994 Norwegian data (estimates taken from Aaberge & Colombino 2006).
2. **Common welfare function:** Estimated separately with parameters $\gamma_1 = -0.649$, $\gamma_2 = 3.026$, $\gamma_3 = -12.262$, $\gamma_4 = 0.045$.
3. **Optimal tax computation:** For each SWF $W_k$, maximize $W_k$ over the 9 tax parameters $(E, \tau_1, \ldots, \tau_4, Z_1, Z_2, Z_3, T)$ subject to revenue neutrality (total tax revenue $\geq$ 1994 actual revenue) and $\tau_4 \leq 0.75$.
4. **Simulation:** For each candidate tax schedule, simulate labour supply responses for all households using the estimated RURO model, compute the welfare distribution using $V(y, h)$, and evaluate $W_k$.
5. **Out-of-sample validation:** Apply the model estimated on 1994 data to predict the 2001 income distribution under 2001 demographics and tax rules; compare predicted and actual 2001 distributions.

# Treatment of preferences

Preferences are modeled via Box-Cox utility functions with taste-shifters for age, education, children, and household composition. The functional form is:
$$v(C, h) = \alpha_C \frac{C^{\beta_C} - 1}{\beta_C} + \alpha_L \frac{L^{\beta_L} - 1}{\beta_L}$$
with $\alpha_C, \alpha_L$ depending on demographics. Preferences are heterogeneous through observed demographics and random taste components $\varepsilon$ (Type I extreme value).

For normative evaluation, individual preferences are **replaced** by the common welfare function $V(y, h)$ — this is a key design choice that ensures interpersonal comparability at the cost of ignoring individual preference heterogeneity in welfare assessment.

# Treatment of opportunities / constraints

The opportunity set is modeled through the opportunity density $p(h, w) = p^0 \cdot g_1(h) \cdot g_2(w|h)$, identical to the 2006 version:
- $p^0$: ratio of market to non-market opportunities (logistic in education, region)
- $g_1(h)$: hours density with peaks at part-time (910--1066 annual hours) and full-time (1898--2106 annual hours)
- $g_2(w|h)$: log-normal wage distribution conditional on hours

**Crucial assumption for optimal tax:** Opportunity densities are held fixed when the tax schedule changes. Only preferences (through utility maximization) respond to tax changes; the supply side of the labour market does not adjust. This is a partial-equilibrium assumption.

# Welfare / normative object

The paper uses **Equality of Outcome (EO)** social welfare criteria only — unlike the 2006 version which also included Equality of Opportunity (EOp, Roemer). The normative object is:
$$W_k = \int_0^1 p_k(t) F^{-1}(t) \, dt$$
where $F^{-1}(t)$ is the quantile function of $V(y_i, h_i)$ across the population.

The common welfare function $V(y, h)$ plays the role of a **reference preference ordering** — it converts each household's $(y, h)$ bundle into a scalar welfare index that is comparable across households. This is analogous to using a reference preference $\bar{R}$ in the Fleurbaey-Maniquet framework, though the paper does not make this connection explicit.

The paper does **not** address the distinction between circumstance-driven and effort-driven inequality, nor does it implement any responsibility-sensitive welfare criterion.

# Main findings

**Optimal tax schedules (Table 5.1):**

| Parameter | Bonferroni ($W_1$) | Gini ($W_2$) | $W_3$ | Utilitarian ($W_\infty$) | 1994 actual |
|-----------|-------------------|--------------|--------|-------------------------|-------------|
| $E$ (NOK) | 19,200 | 22,600 | 35,100 | 77,200 | ~20,000 |
| $\tau_1$ | 0.06 | 0.10 | 0.14 | 0.23 | ~0.28 |
| $\tau_2$ | 0.26 | 0.27 | 0.28 | 0.30 | ~0.35 |
| $\tau_3$ | 0.37 | 0.37 | 0.38 | 0.39 | ~0.42 |
| $\tau_4$ | 0.75 | 0.75 | 0.75 | 0.75 | ~0.50 |
| $T$ (NOK) | $-11,900$ | $-8,900$ | $-5,900$ | $-2,800$ | 0 |

**Key patterns:**
- All optimal schedules have **monotonically increasing** MTRs — no U-shape.
- Bottom MTRs ($\tau_1$) are **much lower** than in 1994 (0.06--0.23 vs. ~0.28), encouraging participation.
- Top MTRs hit the constraint ($\tau_4 = 0.75$) for all SWFs — even the utilitarian.
- Lump-sum transfer $T$ is **negative** (a tax) for all SWFs — the optimal system taxes the first dollar and uses lower MTRs rather than giving a lump-sum grant.
- More egalitarian SWFs ($W_1$) produce lower bottom rates and larger lump-sum taxes.

**Behavioural responses (Table 5.3):**
- Participation increases 2--5 percentage points under all optimal schedules.
- Mean hours increase 5--10%.
- Mean disposable income increases 5--14%.
- Bottom decile hours increase dramatically: 50--76% for couples (Table 5.4).

**Out-of-sample prediction (Table 3.5):**
- The model estimated on 1994 data predicts the 2001 income distribution accurately.
- Predicted and actual decile shares are close, validating the structural approach for counterfactual analysis.

**Social welfare gains:**
- All optimal schedules produce higher $W_k$ than the 1994 system.
- The gains come primarily from increased participation and hours among low-income households — consistent with the high elasticities at the bottom of the income distribution found in earlier papers.

# Main limitations

- Top MTR constrained at 75% — the unconstrained optimum may be higher, and the constraint is not derived from economic theory.
- Only EO criteria — the paper drops the EOp analysis from the 2006 version, so no responsibility-sensitive evaluation is performed.
- Partial equilibrium: opportunity densities fixed under tax changes. Large behavioural responses (especially at the bottom) might shift labour demand and wages.
- Common welfare function $V(y, h)$ imposes a single preference ordering on all households — this is a strong assumption that ignores preference heterogeneity in welfare assessment.
- Revenue neutrality imposed at national level; regional redistribution effects not explored.
- Working paper — the published version (2013, SJE) may differ in some details.

# Relevance for my JMP

## possible use for framing
The paper demonstrates the full pipeline from structural estimation to optimal policy design, using a common welfare function for interpersonal comparability. This pipeline is directly relevant for my framework, where $W(z, R, A; y)$ replaces the common welfare function with a measure that explicitly separates preferences ($R$) from opportunities ($A$).

## possible use for model design
The 9-parameter piecewise-linear tax function is a tractable policy instrument for optimization. The same or similar parametrization could be used in my framework for computing optimal taxes under $W(z, R, A; y)$.

## possible use for identification
The out-of-sample validation exercise (1994$\to$2001) provides a template for validating structural models: estimate on one year, predict another year's distribution, and compare. This strengthens the credibility of counterfactual simulations.

## possible use for welfare measurement
The common welfare function $V(y, h)$ is conceptually parallel to the reference preference $\bar{R}$ in the Fleurbaey-Maniquet framework. In my framework, $\bar{R}$ serves the same role — converting bundles into interpersonally comparable welfare indices — but does so within a responsibility-sensitive framework that also accounts for the feasible set $A$.

## possible use for decomposition
The paper does not decompose welfare effects into opportunity-driven vs. preference-driven components. My framework could extend this by showing how optimal tax schedules differ when the social planner accounts for differences in $A$ (compensable) vs. $R$ (responsibility).

## possible use for comparative application
The paper provides the Norwegian benchmark (1994 tax system, RURO model estimates, optimal tax schedules) that my cross-country analysis can build upon. Comparing Norwegian optimal taxes under $W(z, R, A; y)$ with the EO-optimal taxes in this paper would isolate the effect of incorporating responsibility-sensitivity.

# Research questions this paper inspires

1. How would the optimal tax schedules change if the social planner used a responsibility-sensitive criterion like $W(z, R, A; y)$ instead of the common welfare function $V(y, h)$? Would bottom MTRs be even lower (to compensate for opportunity deficits) or higher (to hold individuals responsible for labour supply choices)?

2. The top MTR hits the 75% constraint for all SWFs — what would the unconstrained optimum be? Is this an artifact of the piecewise-linear parametrization or a robust finding?

3. The lump-sum transfer $T$ is negative under all optimal schedules — does this result survive when opportunity heterogeneity is explicitly accounted for in the welfare criterion?

4. How sensitive are the optimal tax results to the specification of the common welfare function $V(y, h)$? Would using a Fleurbaey-Maniquet reference preference $\bar{R}$ instead produce different optimal schedules?

# Challenge to this paper

The use of a common welfare function $V(y, h)$ for interpersonal comparability is a strong normative choice that the paper does not fully justify. By imposing a single preference ordering on all households, the paper implicitly assumes that preference heterogeneity is irrelevant for welfare evaluation — or equivalently, that all preference differences should be fully compensated. This is inconsistent with responsibility-sensitive approaches (Fleurbaey 2008) where individuals should bear the consequences of their preference choices. The optimal tax schedules might look quite different under a criterion that holds individuals responsible for their preferences while compensating them for differences in opportunities ($A$). Moreover, the common welfare function's parameters ($\gamma_1, \ldots, \gamma_4$) are estimated, introducing an additional layer of uncertainty that is not propagated through the optimal tax computation.

# Relation to my jobs_and_wellbeing framework

[Reasonable inference for my project] The common welfare function $V(y, h) = \gamma_2(y^{\gamma_1}-1)/\gamma_1 + \gamma_4(L^{\gamma_3}-1)/\gamma_3$ is the empirical counterpart of using a reference preference $\bar{R}$ in my framework. In my notation, the paper effectively computes $W(z, \bar{R}, A; y)$ where $\bar{R}$ is fixed at $V(\cdot)$ and $A$ enters only through the structural model (not through the welfare criterion). My framework would extend this by making the welfare measure explicitly sensitive to differences in $A$ across individuals — so that two individuals with the same $(y, h)$ but different feasible sets would receive different welfare assessments.

[Explicit in paper] The paper uses $V(y, h)$ as a "common preference" for welfare evaluation (Section 4). The rank-dependent SWF $W_k = \int p_k(t) F^{-1}(t) dt$ evaluates inequality over the distribution of $V(y_i, h_i)$. The paper states that $V$ is estimated to ensure "interpersonal comparability" of welfare levels.

[Unclear from paper] Whether the common welfare function satisfies any of the axioms in my framework (Full Compensation, Independence of $A$, Independence of $\mathbf{y}$, Full Responsibility, RAA). The paper does not discuss which normative properties $V$ satisfies or violates. Since $V$ does not condition on $A$, it likely violates Full Compensation (which requires compensating for differences in $A$). Since $V$ replaces individual $R$ with $\bar{R}$, it satisfies something close to Independence of $R$ but does so without the responsibility justification.

The paper is closest to: **Measure 5 (Reference Ability LF)** in my framework, in the sense that it uses a reference preference for interpersonal comparability, but without conditioning on the feasible set $A$.

# Relation to Bargain et al. (2013)

The paper shares the RURO modelling framework with Bargain et al. (2013), but differs in the normative approach. Bargain et al. use heterogeneous preferences for welfare evaluation (computing equivalent income with individual-specific utility functions), while this paper replaces all preferences with a common $V(y, h)$. This means that Aaberge & Colombino's welfare evaluation is "preference-free" in the sense of not depending on individual tastes, while Bargain et al.'s evaluation is "preference-respecting" but not responsibility-sensitive. The optimal tax results here — low bottom MTRs, high top MTRs — could differ substantially under Bargain et al.'s heterogeneous-preference welfare criterion, particularly if preference heterogeneity correlates with income.

# Relation to opportunities vs preferences

The paper cleanly separates the **positive model** (which incorporates both preference and opportunity heterogeneity through the RURO structure) from the **normative evaluation** (which uses only a common preference $V(y, h)$ and ignores both individual preferences and opportunity heterogeneity). This creates an asymmetry: the behavioural predictions depend on both $R$ and $A$, but the welfare evaluation depends on neither individual $R$ nor individual $A$. The paper thus represents the "pure EO" position in the normative spectrum — evaluate outcomes without regard to their sources. This contrasts with my framework, where both $R$ and $A$ explicitly enter the welfare measure, and with the EOp approach (included in the 2006 version but dropped here), where circumstances ($A$-like objects) matter for the normative criterion.

# Useful quotations / formulas

**Common welfare function:**
$$V(y, h) = \gamma_2 \frac{y^{\gamma_1} - 1}{\gamma_1} + \gamma_4 \frac{L^{\gamma_3} - 1}{\gamma_3}$$
with $\gamma_1 = -0.649$, $\gamma_2 = 3.026$, $\gamma_3 = -12.262$, $\gamma_4 = 0.045$.

**Rank-dependent SWF:**
$$W_k = \int_0^1 p_k(t) F^{-1}(t) \, dt$$

**Piecewise-linear tax (with lump-sum):**
$$\text{Tax}(Y) = \max\{0, \tau_1(Y - E)\} + \sum_{j=2}^{4} (\tau_j - \tau_{j-1}) \max\{0, Y - Z_{j-1}\} - T$$

# Suggested tags

RURO, optimal-taxation, piecewise-linear-tax, common-welfare-function, rank-dependent-SWF, Bonferroni, Gini, utilitarian, microsimulation, Norway, out-of-sample, structural-estimation, inequality-aversion, labour-supply

# My quick takeaway

This paper is the most detailed exposition of the Aaberge-Colombino optimal tax pipeline: structural RURO estimation $\to$ common welfare function $\to$ numerical optimization over piecewise-linear taxes $\to$ welfare evaluation under rank-dependent SWFs. The key results — low bottom MTRs, binding top MTR at 75%, negative lump-sum transfer, large participation increases at the bottom — are robust across SWFs with different inequality aversion. For my JMP, the main value is: (i) a template for the optimal tax computation that I can extend to $W(z, R, A; y)$, (ii) the common welfare function $V(y, h)$ as a benchmark to compare against my responsibility-sensitive measure, and (iii) the out-of-sample validation exercise as a credibility check for structural counterfactuals. The paper's limitation — dropping EOp and ignoring $A$ in the welfare criterion — is precisely the gap my framework fills.
