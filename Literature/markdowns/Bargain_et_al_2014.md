---
title: "Comparing Inequality Aversion across Countries when Labor Supply Responses Differ"
authors: [Olivier Bargain, Mathias Dolls, Dirk Neumann, Andreas Peichl, Sebastian Siegloch]
year: 2014
outlet: "International Tax and Public Finance, 21(5), 845--873"
country_or_context: "18 countries: 14 EU-15 (excl. Luxembourg) + Estonia, Hungary, Poland + US"
population: "Childless single men and single women, ages 18--64"
data_period: "1998, 2001, or 2005 (country-specific)"
shelf: "optimal taxation / revealed social preferences / inequality aversion / cross-country"
tags: [inequality-aversion, revealed-social-preferences, optimal-tax-inversion, Saez-model, marginal-social-welfare-weights, extensive-margin, elasticities, EUROMOD, TAXSIM, cross-country, discrete-choice, labour-supply]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Bargain, O., Dolls, M., Neumann, D., Peichl, A., & Siegloch, S. (2014). Comparing Inequality Aversion across Countries when Labor Supply Responses Differ. *International Tax and Public Finance*, 21(5), 845--873.

# One-sentence contribution

Inverts Saez's (2002) discrete optimal income tax model using harmonized labour supply elasticities estimated on the same data to recover the social inequality aversion parameter $\gamma$ implicit in the tax-benefit systems of 18 Western countries, finding three distinct clusters: utilitarian (Southern/Eastern Europe, US, $\gamma < 1$), intermediate (Continental Europe, $\gamma \approx 1$), and Rawlsian (Nordic, Belgium, $\gamma > 1$) -- with the ranking changing significantly when country-specific vs. uniform elasticities are used.

# Why this paper matters

Most cross-country comparisons of redistributive preferences assume uniform labour supply elasticities, confounding differences in behavioural responses with differences in social preferences. By estimating both elasticities and social preferences from the same data using a harmonized approach, this paper isolates genuine cross-country differences in inequality aversion from differences in efficiency constraints. The key finding -- that accounting for country-specific elasticities changes the ranking of revealed inequality aversion -- highlights the importance of jointly estimating behavioural and normative parameters.

# Core research question

To what extent does social inequality aversion differ across countries when controlling for actual (rather than assumed uniform) differences in labour supply responses at both extensive and intensive margins?

# Economic setting and context

18 Western countries (~1998--2005): EU-14, Estonia, Hungary, Poland, US. Single childless individuals (men and women). Tax-benefit systems simulated via EUROMOD (EU) and TAXSIM v9 (US). Population partitioned into $I + 1 = 6$ income groups (non-workers + 5 income quintiles among workers). The paper exploits cross-country variation in both tax-benefit generosity and labour supply responsiveness.

# Model / theoretical framework

**Saez (2002) discrete optimal tax model:**

Population divided into $I + 1$ groups: group 0 (non-workers) and groups $i = 1, \ldots, I$ (workers ranked by increasing market income $Y_i$). Disposable income $C_i = Y_i - T_i$. The optimal tax formula balances equity (welfare weights $g_i$) against efficiency (elasticities $\eta_i, \zeta_i$):

$$\frac{T_i - T_{i-1}}{C_i - C_{i-1}} = \frac{1}{\zeta_i h_i} \sum_{j=i}^{I} h_j \left[1 - g_j - \eta_j \frac{T_j - T_0}{C_j - C_0}\right] \quad \text{for } i = 1, \ldots, I$$

where $\zeta_i$ = intensive margin elasticity, $\eta_i$ = extensive margin elasticity, $h_i$ = population share, $g_i$ = marginal social welfare weight.

**Inversion procedure:** Given observed tax levels $T_i$, estimated elasticities $\eta_i, \zeta_i$, and population shares $h_i$, the formula is inverted to recover the welfare weights $g_i$ (normalized: $\sum h_i g_i = 1$). These are then summarized by a single inequality aversion parameter $\gamma$ via:

$$g_i = \frac{1}{(p \cdot C_i)^\gamma} \quad \text{for all } i = 0, \ldots, I$$

where $p$ = marginal value of public funds, $\gamma = 0$ is utilitarian, $\gamma \to \infty$ is Rawlsian (maximin).

**Framework:** Positive (revealed preference for redistribution), not normative design.

# Key objects

- **$\gamma$ (inequality aversion parameter):** Single scalar summarizing redistributive preferences implicit in each country's tax-benefit system. Ranges from $\gamma \approx 0.25$ (Greece, US) to $\gamma > 3$ (Denmark, Belgium).
- **$g_i$ (marginal social welfare weights):** Social value of transferring one euro to group $i$, expressed in public funds. Necessary condition: $g_i > 0$ for all $i$ (Paretian).
- **$\zeta_i$ (intensive margin elasticity):** Response of hours/income to changes in the income gap between adjacent groups.
- **$\eta_i$ (extensive margin elasticity):** Participation response to changes in the income gap between working and not working.
- **$g_0$ (weight on non-workers):** Typically very large ($g_0 = 1.2$--$7.3$), reflecting generosity of social transfers.

# Data

Harmonized micro-data for 18 countries: EU-SILC, ECHP, GSOEP, SHIW, SOEP, FES, CPS, etc. Tax-benefit rules via EUROMOD (EU) and TAXSIM v9 (US). Single childless individuals aged 18--64, excluding pensioners, students, farmers, self-employed. Sample sizes range from 106 (Portugal) to 7,053 (US). All incomes in euros/week.

# Identification logic

The key identifying assumption is that **observed tax-benefit systems are optimal** -- i.e., they represent the outcome of a social planner maximizing a social welfare function subject to the efficiency constraints given by actual labour supply responses. Under this assumption, the inversion of the optimal tax formula uniquely recovers the welfare weights $g_i$ and hence $\gamma$. The assumption is acknowledged as strong but maintained as a benchmark (following Bourguignon and Spadaro 2012).

# Estimation / empirical strategy

1. **Tax-benefit simulation:** For each country, compute gross income $Y_i$, disposable income $C_i$, effective marginal tax rates (EMTRs), and effective participation tax rates (EPTRs) for each income group using EUROMOD/TAXSIM.
2. **Labour supply estimation:** Country-specific discrete-choice models (quadratic utility, 7 hours categories, conditional logit with fixed costs of work $f_{kj}$) estimated separately for each country.
3. **Elasticity computation:** Simulate individual-level responses to 1% uniform income changes, aggregate to income-group-level Saez elasticities $\eta_i, \zeta_i$.
4. **Inversion:** Plug $T_i, C_i, h_i, \eta_i, \zeta_i$ into the optimal tax formula to recover $g_i$.
5. **$\gamma$ estimation:** Regress $\log g_i$ on $\log C_i$ (with controls) to recover $\gamma$.

# Treatment of preferences

Individual consumption-leisure preferences modelled via quadratic utility:
$$V_{kj}(c_{kj}, h_{kj}) = \alpha_{ck} c_{kj} + \alpha_{cc} c_{kj}^2 + \alpha_{hk} h_{kj} + \alpha_{hh} h_{kj}^2 + \alpha_{ch} c_{kj} h_{kj} - f_{kj}$$

with taste-shifters on $\alpha_{ck}$ and $\alpha_{hk}$ (gender, age polynomial, region) and fixed costs of work $f_{kj}$ (zero for non-participation, positive for $j > 0$). EV-I random term $\epsilon_{ij}$.

Social preferences are the object of interest: the welfare weights $g_i$ and inequality aversion $\gamma$ represent the planner's (society's) redistributive tastes, not individual preferences. The paper explicitly separates individual preferences (labour supply) from social preferences (redistribution).

# Treatment of opportunities / constraints

No explicit modelling of demand-side constraints. Fixed costs of work $f_{kj}$ partially capture entry barriers. The paper notes that the extensive margin dominates -- responses are "systematically larger at the extensive margin" (p. 847) -- and that this is particularly important for low-income groups, where participation barriers (including demand-side constraints) are most relevant. However, the model does not distinguish between voluntary non-participation and involuntary unemployment.

# Welfare / normative object

The paper recovers **revealed social preferences** from observed tax-benefit systems, not individual welfare. The normative object is the social welfare function $W = \sum_i h_i u(g_i)$ with $g_i = 1/(p \cdot C_i)^\gamma$, where $\gamma$ summarizes society's inequality aversion. This is a welfarist framework (SWF as weighted sum of utilities), not a Fleurbaey-style responsibility-sensitive framework.

The paper explicitly notes (footnote 10) that alternative characterizations could use non-welfarist objectives (Kanbur and Tuomala 2006) or preference-respecting metrics (Fleurbaey 2008), but stays within the standard optimal tax framework.

# Main findings

**Labour supply elasticities (Tables 4--5, Figures 1--2):**
- Extensive margin dominates intensive margin in all countries (mean extensive elasticity 0.24 vs. intensive 0.13)
- Extensive margin elasticities largest for lowest income groups (group 1: 0.26 mean) and decrease with income
- International differences relatively small: mean participation elasticity ranges from 0.04 (Portugal, Poland) to 0.59 (Italy), with most countries in 0.06--0.35 range
- Ireland has highest elasticities overall (0.36 intensive, 0.38--0.57 extensive)
- Income effects near zero ($<0.01$ in absolute value) for most countries

**Marginal social welfare weights (Table 1):**
- $g_0$ (non-workers) very large in all countries: 1.2 (Greece) to 7.3 (Austria)
- $g_1$ (working poor) varies substantially: 0.0 (Belgium, Germany, Sweden) to 1.6 (Italy)
- For upper income groups ($g_3$--$g_5$), weights are positive but below 1 in almost all countries -- Paretian condition generally satisfied
- Nordic and Continental countries show steepest decline in $g_i$ with income

**Revealed inequality aversion $\gamma$ (Figure 3):**
- **Three country clusters:**
  1. **Low $\gamma$ (utilitarian):** Southern/Eastern Europe + US ($\gamma \approx 0.25$): Greece, US, Portugal, Italy, Spain, Eastern Europe
  2. **Intermediate $\gamma$:** Continental Europe ($\gamma \approx 1$): France, Ireland, Finland, UK, Austria, Germany
  3. **High $\gamma$ (Rawlsian):** Nordic + Belgium ($\gamma > 1$): Netherlands, Sweden, Denmark, Belgium ($\gamma \approx 1.5$--$3$)

- **Uniform vs. country-specific elasticities changes rankings:** With uniform (mean) elasticities, France appears less Rawlsian because its very low elasticities are overestimated (overstating efficiency costs). Ireland appears more Rawlsian because its high elasticities are underestimated.

**Sensitivity analyses (Figure 4):**
- Zero extensive margin responses: inequality aversion decreases mechanically (fewer efficiency costs to rationalize), but the three-group ranking is broadly preserved. Belgium, Sweden, Denmark, Netherlands still show highest $\gamma$.
- Alternative income group definitions: robust (middle panel of Figure 4)
- Alternative number of income groups ($I + 1 = 11$): very similar results (right panel)

**Key mechanism:** Countries with generous social assistance (high $g_0$) combined with large extensive margin responses *must* have very high $\gamma$ to rationalize their policy -- the efficiency costs of non-participation are large, so the social value of redistribution must be correspondingly large. This is why Continental European countries with traditional social assistance programs show Rawlsian preferences.

# Main limitations

- Optimality assumption is strong -- actual tax-benefit systems result from political processes, not a benevolent planner
- Only singles; no couples, no children -- limits scope for cross-household redistribution analysis
- No demand-side constraints or involuntary unemployment -- participation responses may confound supply and demand
- Income effects assumed zero (a maintained restriction, not tested)
- Single $\gamma$ parameter may mask heterogeneity in social preferences across the income distribution (e.g., "charitable conservatism" vs. "poverty radicalism" à la Kanbur and Tuomala 2011)
- Confidence intervals on $\gamma$ are wide for some countries -- pairwise differences often not statistically significant
- Only direct taxes and transfers considered; in-kind benefits and public services excluded

# Relevance for my JMP

## possible use for framing
The paper demonstrates that revealed social preferences ($\gamma$) are sensitive to the labour supply elasticities used -- directly motivating the need for a framework like $W(z, R, A; y)$ that jointly models preferences, opportunities, and welfare evaluation. If the normative conclusions depend on the behavioural model, getting the behavioural model right (including demand-side constraints) is a first-order concern.

## possible use for model design
The Saez inversion approach could be applied within the RURO framework: instead of using standard discrete-choice elasticities, one could compute RURO-based elasticities that separate preference responses from opportunity-density effects, potentially yielding different revealed inequality aversion.

## possible use for identification
The paper's elasticity estimates (Tables 4--5) provide country-specific benchmarks for extensive and intensive margin responses that can be compared against RURO-based estimates. The finding that income effects are near zero supports the no-income-effect assumption used in many optimal tax models.

## possible use for decomposition
The paper's finding that the ranking of $\gamma$ changes with elasticity specification implies that the decomposition of welfare into $R$, $A$, and $y$ components in my framework has direct implications for revealed social preferences: if part of what looks like "low elasticity" is actually demand-side rationing ($A$ effects), then the implied $\gamma$ changes.

## possible use for comparative application
The 18-country estimates of $\gamma$ provide a direct benchmark for cross-country inequality aversion that my framework can improve upon by separating preference-based elasticities from opportunity-based responses.

# Research questions this paper inspires

1. How would revealed inequality aversion $\gamma$ change if the inversion used RURO-based elasticities that decompose responses into preference changes (movements along indifference curves) vs. opportunity changes (shifts in the feasible set $A$)?

2. The paper finds that countries with generous social assistance must have high $\gamma$ to rationalize their policies. But if these countries also have high rationing rates (Bargain et al. 2010), the extensive margin elasticity is overstated, implying that $\gamma$ is also overstated. Would accounting for rationing compress the cross-country distribution of $\gamma$?

3. Can the Saez inversion be extended to a multi-dimensional framework where the planner has separate inequality aversion parameters for income and leisure/well-being, connecting to the Bargain et al. (2013) welfare metrics?

4. The paper assumes observed systems are optimal. What if we instead ask: "Given $\gamma$, what is the optimal system?" and compare with the Aaberge-Colombino computational optimal tax results?

# Challenge to this paper

The paper's central finding -- three clusters of inequality aversion -- depends critically on the assumption that observed tax-benefit systems are optimal. But if policymakers designed social assistance programs without accounting for extensive margin responses (as the paper itself suggests on p. 860: "it is possible that potential labor supply responsiveness was underestimated or ignored by policymakers when generous demogrant policies were designed"), then the "revealed" preferences are not actual social preferences but rather the preferences that would *rationalize* a possibly sub-optimal policy. The zero-elasticity sensitivity check (Figure 4, left panel) shows that revealed $\gamma$ drops substantially when participation responses are ignored -- the very scenario the paper argues was plausible historically. This means the high Rawlsian values for Continental Europe may reflect policy mistakes rather than genuinely high inequality aversion.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper recovers social preferences under a welfarist framework ($g_i = 1/(pC_i)^\gamma$) that does not incorporate leisure or preference heterogeneity. Footnote 10 acknowledges that "it could be interesting to replicate our analysis with non-welfarist objectives (e.g. Kanbur et al. 2006) or welfare measures that preserve individual heterogeneity (see Fleurbaey 2008)" (p. 851). This directly points to the $W(z, R, A; y)$ framework.

[Reasonable inference for my project] In the $W(z, R, A; y)$ framework, the social planner's inequality aversion would be defined over the well-being measure $W$ rather than over income $C$. Since $W$ incorporates leisure preferences ($R$) and opportunity constraints ($A$), the implied $\gamma$ could differ substantially from the income-based $\gamma$ recovered here. A planner who is utilitarian over $W$ might appear Rawlsian over income if $W$ is concave in income.

[Unclear from paper] How to reconcile the welfarist SWF framework ($\gamma$ over utilities) with the Fleurbaey-style responsibility-sensitive metrics used in Bargain et al. (2013). The two approaches may give different answers about "how redistributive" a country is, because the former treats all preferences symmetrically while the latter distinguishes between legitimate and illegitimate preference differences.

The paper is closest to: **revealed social preferences** and **cross-country comparison of redistributive policy**.

# Relation to Bargain et al. (2013)

This paper complements Bargain et al. (2013) by addressing the aggregation step that the welfare metrics paper deliberately avoids. While Bargain et al. (2013) compute individual-level welfare metrics and compare rankings, this paper estimates the social welfare function that aggregates over individuals. The key tension: Bargain et al. (2013) uses preference-sensitive metrics (Fleurbaey) while this paper uses a standard utilitarian/Rawlsian SWF that ignores preference heterogeneity. Combining the two approaches -- Fleurbaey metrics + Saez inversion -- would yield a richer picture of revealed social preferences that accounts for both leisure and preference heterogeneity.

# Relation to opportunities vs preferences

The paper does not separately model opportunities vs. preferences. However, its central finding -- that elasticity specification matters for revealed $\gamma$ -- implicitly highlights the importance of this distinction. If part of the extensive margin response is an opportunity effect (rationing, as in Bargain et al. 2010) rather than a preference effect, then the "true" elasticity of preferences alone is smaller, and the implied $\gamma$ changes. This connects directly to the $W(z, R, A; y)$ framework's separation of $R$ (which determines preference-based elasticities) from $A$ (which determines opportunity-based responses).

# Useful quotations / formulas

**Saez optimal tax formula (eq. 1):**
$$\frac{T_i - T_{i-1}}{C_i - C_{i-1}} = \frac{1}{\zeta_i h_i} \sum_{j=i}^{I} h_j \left[1 - g_j - \eta_j \frac{T_j - T_0}{C_j - C_0}\right]$$

**Welfare weight parameterization (eq. 5):**
$$g_i = \frac{1}{(p \cdot C_i)^\gamma} \quad \text{for all } i = 0, \ldots, I$$

**On the importance of elasticities (p. 856):**
"labor supply elasticities are neither a single number nor a primitive feature of preferences [...and] one important source of confusion in the literature is the idea that one can estimate a labor supply elasticity in one context and import this elasticity into other contexts." (quoting Keane and Rogerson 2012)

**On the three clusters (p. 859):**
"For Continental Europe, Ireland and the UK, Ireland and Finland we find a $\gamma$ value around 1. Importantly, the large weight on group 0 (workless poor) drives the result of high inequality aversion for these countries, and is rationalized by the fact that the extensive margin dominates."

**On policy mistakes (p. 860):**
"it is possible that potential labor supply responsiveness was underestimated or ignored by policymakers when generous demogrant policies were designed and implemented"

# Suggested tags

inequality-aversion, revealed-social-preferences, optimal-tax-inversion, Saez-model, extensive-margin, intensive-margin, marginal-social-welfare-weights, EUROMOD, TAXSIM, cross-country, discrete-choice, labour-supply, redistribution, welfare-state

# My quick takeaway

This paper provides the aggregation step missing from Bargain et al. (2013): how redistributive is each country's tax-benefit system, as measured by a single inequality aversion parameter? The key takeaway for my JMP is that the revealed $\gamma$ is sensitive to the elasticity estimates used, and these elasticities confound preference responses with opportunity constraints. A RURO-based inversion that separates $R$-driven elasticities from $A$-driven responses could yield materially different conclusions about cross-country differences in social preferences. The three-cluster finding (utilitarian South/East, intermediate Continental, Rawlsian Nordic) provides a useful benchmark but may partly reflect differences in opportunity structures rather than genuine differences in redistributive preferences.
