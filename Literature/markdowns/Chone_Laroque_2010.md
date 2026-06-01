---
title: "Negative Marginal Tax Rates and Heterogeneity"
authors: [Philippe Choné, Guy Laroque]
year: 2010
outlet: "American Economic Review, 100(5), 2532--2547"
country_or_context: "Theoretical (UK calibration for illustration)"
population: "General (Mirrlees economy with multidimensional heterogeneity)"
data_period: "N/A (theoretical; UK 2003 earnings data for simulation in Section IIIC)"
shelf: "optimal taxation / negative marginal rates / heterogeneity / opportunity costs / social weights / intensive margin"
tags: [optimal-taxation, negative-marginal-rates, heterogeneity, opportunity-cost, work-cost, social-weights, Mirrlees, intensive-margin, multidimensional, cardinal-utility, EITC, UK, calibration]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Choné, P., & Laroque, G. (2010). Negative Marginal Tax Rates and Heterogeneity. *American Economic Review*, 100(5), 2532--2547.

# One-sentence contribution

Shows that in the standard intensive-margin Mirrlees model, negative marginal tax rates can be optimal when agents differ in both productivity ($\theta^p$) and opportunity cost of work ($\theta^c$), and the distribution of opportunity costs conditional on income shifts in a way that gives low-income agents with high costs disproportionate social weight -- providing a complementary channel to Saez (2002)'s extensive-margin explanation for EITC-type subsidies.

# Why this paper matters

This paper overturns a widespread belief that negative marginal tax rates require the extensive margin (participation responses). It shows that within the classical intensive-margin framework, multidimensional heterogeneity (in both productivity and work costs) can produce negative marginal rates at the bottom of the income distribution. The key mechanism: when agents at the same low income level include both high-productivity/high-cost types (who deserve compensation) and low-productivity/low-cost types (who are relatively well off), the social weight profile can be non-monotone in income, producing negative rates. This directly motivates the RURO framework's separation of preferences from opportunities.

# Core research question

Under what conditions on the distribution of heterogeneous characteristics (productivity and opportunity cost of work) are negative marginal tax rates optimal in the standard intensive-margin Mirrlees model?

# Economic setting and context

Standard Mirrlees income tax model with separable utility. Agent of type $\theta = (\theta^c, \theta^p)$ has utility $u(c) + \tilde{v}(y, \theta)$ where $u$ is concave utility of consumption, $\tilde{v}$ is disutility of earning income $y$ (increasing in $y$, decreasing in productivity $\theta^p$, increasing in opportunity cost $\theta^c$). The government observes only income $y$ and sets $R(y) = y - T(y)$.

The key simplification: behaviour depends on a unidimensional parameter $\alpha = A(\theta)$ combining $\theta^p$ and $\theta^c$, so the tax schedule can be analysed in terms of $\alpha$. But social weights still depend on both dimensions, because the cardinal utility $K[U, \theta^c]$ can weight different $\theta^c$ types differently even at the same $\alpha$.

# Model / theoretical framework

**Utility:** $v(y, A(\theta)) = u(c) + v(y, \alpha)$ where $\alpha = A(\theta^p, \theta^c)$, $A$ increasing in $\theta^p$ and decreasing in $\theta^c$. Single-crossing condition: $v_{y\alpha} > 0$.

**Incentive compatibility (Lemma 1):** Allocation $y$ is IC iff $y$ is nondecreasing in $\alpha$. Indirect utility $U_R(\alpha)$ is differentiable a.e. with $U_R'(\alpha) = v_\alpha(y(\alpha), \alpha)$.

**Social objective (utilitarian):**

$$\mathcal{L} = \int_{\underline{\alpha}}^{\bar{\alpha}} \{\pi(\alpha) U_R(\alpha) + \lambda[y(\alpha) - R(y(\alpha))]\} \, dG(\alpha)$$

where $\pi(\alpha)$ are Pareto weights summing to 1.

**Modified weights (eq. 2):** $\pi^*(\alpha) = \pi(\alpha) u'(R(y_R(\alpha)))$. These incorporate the marginal utility of consumption.

**Average weight above $\alpha$ (eq. 3):** $p^*(\alpha) = \frac{1}{1 - G^*(\alpha)} \int_\alpha^{\bar{\alpha}} \pi^*(x) \, dG^*(x) = E_{G^*}(\pi^*(x) \mid x \geq \alpha)$.

**First-order condition (Lemma 2, eq. 4):**

$$\lambda \frac{u'(R(y_R(\alpha)))}{v_{y\alpha}(y_R(\alpha), \alpha)} T'(y_R(\alpha)) = \frac{1 - G^*(\alpha)}{g^*(\alpha)}[\lambda - p^*(\alpha)]$$

**Key result:** The marginal tax rate has the same sign as $\lambda - p^*(\alpha)$. Negative marginal rates occur when the average social weight of agents with lower $\alpha$ is above $\lambda$ (the marginal cost of public funds).

**Aggregate weights (eq. 5):** $\pi(\alpha) = \int \tilde{\pi}(\alpha, \theta^c) \, dF(\theta^c | \alpha)$ where $\tilde{\pi}$ are the individual-type weights.

**Cardinal utility specification:** $K[U, \theta^c]$ maps utility level $U$ and opportunity cost $\theta^c$ to cardinal social value. Two key cases:
- $K_U$ increasing in $\theta^c$: high opportunity cost → high social weight (cost comes from handicap → compensation motive)
- $K_U$ decreasing in $\theta^c$: high opportunity cost → low social weight (cost reflects taste for leisure → no compensation)

# Key objects

- **$\theta^p$:** Productivity (ability) -- earning $y$ requires labour $y/\theta^p$
- **$\theta^c$:** Opportunity cost of work -- reflects either handicap or taste for leisure
- **$\alpha = A(\theta^p, \theta^c)$:** Unidimensional composite parameter driving behaviour
- **$\pi^*(\alpha)$:** Modified social weight for type $\alpha$ (incorporates marginal utility)
- **$p^*(\alpha)$:** Average modified weight for types above $\alpha$ (eq. 3)
- **$K[U, \theta^c]$:** Cardinal utility function used by the social planner; the derivative $K_U$ determines social weights
- **Cross-product formula (Proposition 3, eq. 7):**

$$\pi^*(\underline{\alpha}) - \lambda = \iint \{\nabla F \times \nabla \tilde{\pi}^*\}[1 - G^*(\alpha)] \, d\theta^c \, d\alpha$$

where $\nabla F \times \nabla \tilde{\pi}^*$ is the cross-product of the gradients of the conditional CDF and the individual weight function.

# Data

UK 2003 annual earnings and marginal tax rate data (from Brewer, Saez, and Shephard 2009, the Mirrlees Review). Isoelastic utility $U_R(\alpha) = \max_y R(y) - y^{1+1/e} / [(1+1/e)\alpha^{1/e}]$ with elasticity $e = 0.25$. Work opportunity cost $\theta^c$ normally distributed conditional on $\alpha$ with standard error $\sigma(\alpha)$ varying across income quartiles. Cardinal utility: $K[U, \theta^c] = -\exp[-(U - \theta^c)]$.

# Identification logic

Not an empirical identification paper. Analytical results derived from the structure of the optimal tax problem. The simulation uses UK data for the earnings distribution and makes assumptions about the conditional distribution of $\theta^c$ on $\alpha$.

# Estimation / empirical strategy

UK calibration (Section IIIC):
1. Earnings distribution from UK 2003 data, kernel-smoothed
2. $\alpha$ recovered from first-order condition: $\alpha = (y/R'(y))^e$
3. $\theta^c | \alpha$ assumed normal with mean zero and standard error $\sigma(\alpha) = 200k(1 - \alpha/11850) + 200(\alpha/11850)$ where $k$ varies from 0 to 1
4. $K[U, \theta^c] = -\exp[-(U - \theta^c)]$ so social weight $\propto \exp[-U_R(\alpha) + \theta^c]$: increasing in $\theta^c$
5. Results: negative marginal tax rates at the bottom emerge when $\sigma(0) \geq$ £100 (Figure 2)

# Treatment of preferences

Preferences are heterogeneous along two dimensions: productivity $\theta^p$ and opportunity cost $\theta^c$. Behaviour depends on the composite $\alpha = A(\theta^p, \theta^c)$ -- the government cannot distinguish high-productivity/high-cost agents from low-productivity/low-cost agents at the same income level.

The critical normative question is embedded in the cardinal utility $K[U, \theta^c]$: does a high opportunity cost $\theta^c$ deserve social compensation? If $K_U$ is increasing in $\theta^c$ (the cost reflects a handicap), yes -- and this can generate negative marginal rates. If $K_U$ is decreasing in $\theta^c$ (the cost reflects taste for leisure), no -- and rates remain nonnegative. The paper is explicit that this is a value judgment about whether "the cost is associated with poor living conditions (i.e., a handicap) or reflects a taste for leisure or opportunities outside the labor market (such as gardening at home or black market activities)" (p. 2532).

# Treatment of opportunities / constraints

**Not explicitly modelled.** All agents choose their income level optimally given the tax schedule. There is no involuntary unemployment, job rationing, or demand-side constraints. The "opportunity cost of work" $\theta^c$ is a preference/circumstance parameter, not a measure of job availability.

However, the paper's framework is highly suggestive of the RURO approach: $\theta^c$ captures the value of outside options (non-market activities), and the distribution of $\theta^c$ conditional on productivity determines the social weight profile. In the RURO framework, the opportunity density $g(h, w)$ plays a similar role: it determines the set of available alternatives and thus affects both behaviour and welfare.

# Welfare / normative object

Utilitarian: maximise $\iint K[U_R(\alpha), \theta^c] \, dF(\theta^c | \alpha) \, dG(\alpha)$ subject to the government budget constraint. The cardinal utility $K[U, \theta^c]$ embeds both the social evaluation of utility levels and the normative treatment of opportunity costs.

# Main findings

1. **Unidimensional case (Proposition 1):** When $\theta^c$ is constant (only productivity varies), the standard result holds: marginal tax rates are nonnegative everywhere if $K$ is concave in $U$. This reproduces Mirrlees (1971) and Seade (1977, 1982).

2. **Multidimensional case -- sufficient condition for nonnegative rates (Proposition 2):** If $K_U[U, \theta^c]$ is nondecreasing in $\theta^c$ and $\theta^c$ conditional on $\alpha$ is first-order stochastically decreasing in $\alpha$, then marginal rates are nonnegative. This requires both that the social weight increases with cost and that low-$\alpha$ agents have higher costs.

3. **Corollary 1:** If $\theta^c$ is independent of $\alpha$, marginal rates are nonnegative regardless of how $K$ depends on $\theta^c$.

4. **Negative marginal rates are optimal when (Section III):**
   - Low-productivity agents exhibit heterogeneous opportunity costs (some have high costs, some low)
   - The cardinal utility $K$ is increasing in $\theta^c$ (high-cost agents are better off socially, e.g., because cost reflects valuable outside activities)
   - As a result, the social weight $\pi^*(\underline{\alpha})$ is below $\lambda$, and the marginal tax rate at the bottom is negative

5. **Cross-product formula (Proposition 3, eq. 7):** The deviation of $\pi^*(\underline{\alpha})$ from $\lambda$ is determined by the cross-product $\nabla F \times \nabla \tilde{\pi}^*$. Two components: (i) the standard redistribution motive (typically positive, pushing toward nonnegative rates), and (ii) the heterogeneity interaction term (can be negative, pushing toward negative rates). Negative rates require the second term to dominate.

6. **UK calibration (Section IIIC, Figure 2):** With a standard error of $\theta^c$ as low as £100--£200 at the bottom of the income distribution, negative marginal tax rates emerge at low incomes. This is a small amount relative to median earnings (£16,500), suggesting that heterogeneity effects can be quantitatively important even with modest variation in opportunity costs.

# Main limitations

- The interpretation of $\theta^c$ is normatively loaded: whether high $\theta^c$ reflects a handicap (deserving compensation) or a taste for leisure (not deserving) determines the sign of marginal rates
- The unidimensional restriction $\alpha = A(\theta^p, \theta^c)$ is a strong assumption: in general, multidimensional screening problems are much harder
- No extensive margin (participation): all agents work. Saez (2002)'s extensive margin channel is absent
- The UK calibration is illustrative: the distribution of $\theta^c$ conditional on $\alpha$ is assumed, not estimated
- Static model with no demand-side constraints

# Relevance for my JMP

## possible use for the theoretical motivation of RURO
The paper provides a direct theoretical motivation for the RURO framework. The key insight is that agents at the same income level may have very different compositions of productivity and opportunity costs, and the optimal tax depends on this composition. In the RURO model, the opportunity density $g(h, w)$ captures the distribution of available jobs, which is analogous to the conditional distribution $F(\theta^c | \alpha)$ in Choné-Laroque. The paper shows that ignoring this heterogeneity (treating $\theta^c$ as constant) can lead to qualitatively wrong tax recommendations (nonnegative vs negative rates).

## possible use for the normative treatment of opportunity costs
The paper's central normative question -- whether $\theta^c$ reflects a handicap or a preference -- maps directly to the RURO compensation principle. If demand-side constraints (job scarcity) drive high $\theta^c$, the compensation principle implies $K_U$ increasing in $\theta^c$, favouring negative marginal rates. If leisure preferences drive high $\theta^c$, the laissez-faire principle implies no compensation, preserving nonnegative rates. The RURO framework, by separating the opportunity density from preferences, provides the empirical basis for this normative judgment.

## possible use for the quantitative importance of heterogeneity
The UK calibration shows that modest amounts of heterogeneity in opportunity costs (standard error of £100--£200 at the bottom) can flip the sign of optimal marginal rates. This suggests that the RURO opportunity density -- which captures much larger sources of heterogeneity (job availability, hours restrictions, wage distributions) -- could have substantial quantitative effects on optimal tax design.

# Research questions this paper inspires

1. In the RURO framework, the opportunity density $g(h, w)$ captures the distribution of available jobs. Can this be mapped to the conditional distribution $F(\theta^c | \alpha)$ in Choné-Laroque? If agents with restricted opportunities (low $\theta$, unfavourable $g(h)$) have higher effective $\theta^c$, the cross-product formula (Proposition 3) would predict negative marginal rates when opportunity restrictions are concentrated at low incomes.

2. The paper assumes $K_U$ increasing in $\theta^c$ to generate negative rates. What if $\theta^c$ is decomposed into a preference component (taste for leisure) and an opportunity component (demand constraints)? The fairness axioms from Fleurbaey-Maniquet would prescribe $K_U$ increasing in the opportunity component (compensation) but not in the preference component (laissez-faire). Does this decomposed $K$ still produce negative rates?

# Challenge to this paper

The paper treats $\theta^c$ as a single parameter capturing "opportunity cost of work" without decomposing it into its sources. From a fairness perspective, an agent with high $\theta^c$ due to a disability (handicap) and an agent with high $\theta^c$ due to enjoyment of gardening (preference) should be treated differently: the former deserves compensation, the latter does not. The paper acknowledges this (p. 2532) but cannot resolve it without additional structure. The RURO framework, by explicitly modelling the opportunity density $g(h, w)$ separate from preferences, provides this decomposition and enables the fairness-based selection of the appropriate $K[U, \theta^c]$ function.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper models $u(c) + v(y, \alpha)$ where $\alpha = A(\theta^p, \theta^c)$. In my framework, $R$ = preferences (captured by $v$), $A$ = opportunities (partially captured by $\theta^p$ and $\theta^c$), $z$ = realised bundle $(y, c)$, $y$ = tax schedule $T(\cdot)$. The cardinal utility $K[U, \theta^c]$ determines the welfare evaluation $W$.

[Reasonable inference for my project] The cross-product formula (eq. 7) shows that the optimal tax depends on the interaction between the distribution of characteristics ($\nabla F$) and the social weight function ($\nabla \tilde{\pi}^*$). In my framework, $F(\theta^c | \alpha)$ would be replaced by the joint distribution of preferences and opportunities conditional on income, and the social weight would be derived from the equivalent-income metric.

[Unclear from paper] How to map the RURO opportunity density into the $\theta^c$ parameter. The opportunity density $g(h, w)$ is a function, not a scalar; it cannot be reduced to a single $\theta^c$ without additional assumptions about how job availability maps to opportunity costs.

# Relation to Bargain et al. (2013)

Indirect connection. Both papers deal with the role of heterogeneity in welfare evaluation and optimal taxation. Bargain et al. use structural labour supply models to estimate preferences and compute welfare; Choné-Laroque show theoretically that ignoring heterogeneity in opportunity costs can change optimal tax qualitatively. The RURO extension of Bargain et al. could provide the empirical counterpart to Choné-Laroque's theoretical analysis.

# Relation to opportunities vs preferences

The paper's central contribution is showing that the composition of heterogeneity at each income level -- the mix of preferences ($\theta^c$ as taste for leisure) and circumstances ($\theta^c$ as handicap) -- determines the optimal tax. This is exactly the RURO framework's motivation: separating the opportunity density (demand-side constraints, job availability) from preferences (taste for leisure, disutility of effort) to obtain a welfare-relevant decomposition.

# Useful quotations / formulas

**On the normative interpretation of $\theta^c$ (p. 2532):**
"How social weights, or marginal utilities of income, vary with income determines the shape of the optimal tax scheme. Conditionally on income, utility, and more importantly its derivative with respect to income, may either decrease or increase with work opportunity costs. This may vary according to circumstances, depending on whether the cost is associated with poor living conditions (i.e., a handicap) or reflects a taste for leisure or opportunities outside the labor market."

**First-order condition (Lemma 2, eq. 4):**
$$\lambda \frac{u'(R(y_R(\alpha)))}{v_{y\alpha}(y_R(\alpha), \alpha)} T'(y_R(\alpha)) = \frac{1 - G^*(\alpha)}{g^*(\alpha)}[\lambda - p^*(\alpha)]$$

**Cross-product formula (Proposition 3, eq. 7):**
$$\pi^*(\underline{\alpha}) - \lambda = \iint \{\nabla F \times \nabla \tilde{\pi}^*\}[1 - G^*(\alpha)] \, d\theta^c \, d\alpha$$

**On the quantitative importance (p. 2543):**
"While the numbers chosen for the dispersion of the work opportunity costs look small (£200), they are magnified through the expectation of the exponential of the normal variable."

# Suggested tags

optimal-taxation, negative-marginal-rates, heterogeneity, multidimensional, opportunity-cost, work-cost, social-weights, cardinal-utility, Mirrlees, intensive-margin, cross-product, compensation, handicap, EITC, UK, calibration, Choné, Laroque

# My quick takeaway

Shows that negative marginal tax rates can be optimal even within the intensive-margin Mirrlees model, provided agents are heterogeneous in both productivity and opportunity costs and the cardinal utility specification treats high costs as socially valuable. For my JMP: (1) the paper provides a theoretical foundation for why the composition of heterogeneity at each income level matters for optimal taxation -- exactly the RURO decomposition into preferences and opportunities, (2) the normative question of whether $\theta^c$ reflects a handicap or a preference maps to the RURO compensation-vs-laissez-faire distinction, and (3) the UK calibration suggests that even small amounts of heterogeneity in opportunity costs can qualitatively change optimal tax schedules, motivating the empirical decomposition of the opportunity density.
