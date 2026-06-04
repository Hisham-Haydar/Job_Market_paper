---
title: "Labour Supply and Taxation with Restricted Choices"
authors: [Magali Beffy, Richard Blundell, Antoine Bozio, Guy Laroque, Maxime Tô]
year: 2019
outlet: "Journal of Econometrics, 211(1), 16--46"
country_or_context: "United Kingdom"
population: "Women with children (single or married mothers), ages working-age"
data_period: "1997--2002"
shelf: "structural labour supply / restricted choices / offer distribution / identification"
tags: [restricted-choices, two-offer-model, offer-distribution, consideration-set, identification, discrete-choice, fixed-costs, nonlinear-budget, hours-restrictions, demand-side, UK, FES, IFS-Taxben]
priority: "high"
read_status: "extracted"
---

# Full citation

Beffy, M., Blundell, R., Bozio, A., Laroque, G., & Tô, M. (2019). Labour Supply and Taxation with Restricted Choices. *Journal of Econometrics*, 211(1), 16--46.

# One-sentence contribution

Develops a structural model of labour supply in which individuals choose from a restricted set of hours offers (a "two-offer" model) rather than the full set of possible hours, proves formal identification results for both preferences and the offer distribution, and shows empirically that ~8% of UK working mothers are observed at hours that reject the standard unrestricted choice model, with hours restrictions significantly reducing employment and shifting hours downward.

# Why this paper matters

Standard discrete-choice labour supply models assume individuals can freely choose any hours level, but observed hours distributions -- with sharp peaks at part-time and full-time -- suggest demand-side restrictions. This paper provides the first rigorous econometric framework for identifying both preferences and the distribution of hours offers from observed choices, using non-linearities in the budget constraint as an exclusion restriction. It bridges the gap between the RURO approach (which models opportunities via a continuous density) and the standard van Soest approach (which ignores restrictions), offering a middle ground with formal identification guarantees.

# Core research question

Can preferences and the distribution of hours offers be separately identified when individuals face restricted choice sets? What are the implications of ignoring hours restrictions for estimates of preferences, elasticities, and employment predictions?

# Economic setting and context

UK 1997--2002: a period of major welfare reform including the introduction of the Working Families' Tax Credit (WFTC), replacing Family Credit. The nonlinear tax-benefit system creates complex budget constraints with flat regions, kinks, and non-convexities (Income Support, Family Credit, rent rebates, local tax rebates). Women with children face particularly complex incentives due to means-tested benefits. The Family Expenditure Survey (FES) provides detailed consumption, hours, and earnings data, with tax-benefit simulation via IFS-Taxben.

# Model / theoretical framework

**Standard model (Section 2.1):** Life-cycle model where woman maximizes $E_t \int_t^T u_t(c_\tau, h_\tau) d\tau$ subject to intertemporal budget constraint with nonlinear tax function $R(w, h)$ and fixed costs of work $b$. At each date, she chooses hours from a set $\mathcal{H}$.

**Rejections of the unrestricted model (Section 2.2):** Define $S(w, h) = \sup_{x \leq h} R(w, x)$ as the maximal income achievable at most $h$ hours. The "dominated set" $H^W = \{$hours ranges where $S$ is constant on some interval$\}$ consists of hours that should never be chosen by a rational agent. In the data, 2.6% of working women choose hours in $H^W$ -- a nonparametric rejection of unrestricted choice.

**Two-offer model (Section 2.3):** Each individual faces exactly two randomly drawn hours offers from a distribution $g = (g_1, \ldots, g_I)$ over $I$ discrete hours categories. She picks the offer (or non-participation) yielding highest utility. The observed distribution of hours choices $\ell_i$ satisfies:

$$\ell_i(Z, \beta) = g_i^2 + 2g_i \sum_{j \neq i} g_j p_i(\{i, j\}, Z, \beta)$$

where $p_i(\{i, j\}, Z, \beta)$ is the probability of choosing $i$ when both $i$ and $j$ are available. The first term corresponds to receiving two identical offers (no real choice); the second to genuine choice between two distinct offers.

**$n$-offer generalization:** As $n \to \infty$, the model converges to the standard unrestricted choice model.

# Key objects

- **Offer distribution $g = (g_1, \ldots, g_I)$:** Probability of being offered each hours category. Modelled as a mixture of two truncated normals with means $m_1 \approx 15$ (part-time) and $m_2 \approx 38$ (full-time), variances $\sigma_1, \sigma_2$, and mixture probability $p_1$ that can depend on education, location, year.
- **Dominated set $H^W$:** Hours ranges that are strictly dominated by lower hours with equal or higher income. Provides a nonparametric test of unrestricted choice.
- **Choice probabilities $p_i(\{i,j\}, Z, \beta)$:** Probability of choosing hours $i$ when the choice set is $\{i, j\}$, determined by preferences $\beta$ and the budget constraint.
- **Fixed costs of work $b$:** Cost (in consumption units) of employment; depends on demographics (London, number of children, cohabitation).

# Data

UK Family Expenditure Survey (FES), 1997--2002. 10,575 women with children (single or married mothers). Tax-benefit rules simulated via IFS-Taxben, producing household-specific nonlinear budget constraints $R(w, h)$. Consumption measure consistent with life-cycle model (following Blundell and Walker 1986). Median hourly wage £5.85; median usual hours 26/week. ~37% not working.

# Identification logic

**Three sequential identification results:**

1. **Preferences given known offer distribution (Lemma 1):** If $g$ is known, then utilities $V_i$ are uniquely identified from observed choices $\ell_i$ via a system of $I$ equations with $I$ unknowns, where the Jacobian is a dominant diagonal matrix (Gale-Nikaido theorem).

2. **Offer distribution given known preferences (Lemma 2):** If choice probabilities $p_{ij}$ are known, then $g$ is uniquely recovered from $\ell_i$ via the same system with roles reversed.

3. **Joint identification (Section 3.3):** Both preferences $(\beta)$ and offer distribution $(\gamma)$ identified simultaneously when:
   - **Parametric:** $\dim[\beta : \gamma] \leq I - 1$ (enough parameters relative to hours categories)
   - **Semi-parametric:** Exclusion restrictions from budget constraint heterogeneity -- variables (like spouse income, other household income) that shift the budget constraint $R$ without affecting the offer distribution $g$
   - **Nonparametric:** Dominated regions of the budget constraint reveal the offer distribution directly, since choices in dominated regions must reflect the offers, not preferences

# Estimation / empirical strategy

1. **Utility specification (eq. 13):** $u(c, h) = \frac{c^{1-\gamma}}{1-\gamma} + \frac{(L-h)^{1-\phi}}{1-\phi} a$ with $L = 100$ (physiological upper bound), $\ln(a) = Z^a \beta^a + \sigma^a \varepsilon^a$, and fixed costs $b = Z^b \beta^b + \sigma^b \varepsilon^b$.
2. **Offer distribution:** Mixture of two truncated normals on [0, 66] with means $m_k$, variances $\sigma_k$, mixture weight $p_1(Z^o)$.
3. **Wage equation:** Log-linear with human capital covariates (eq. 17).
4. **Consumption equation:** Reduced form for log consumption (eq. 18), used in two-step control function approach to handle endogeneity.
5. **Likelihood:** Joint likelihood of employment status, hours, consumption, and wages, integrating over the offer distribution and unobserved heterogeneity. Three models estimated: (1) baseline, (2) correlated errors, (3) covariates in offer distribution.

# Treatment of preferences

Preferences specified via CRRA utility over consumption and leisure (eq. 13). Preference heterogeneity through observed covariates ($Z^a$: cohabiting, youngest child age, birth cohort) and unobserved taste shock $\varepsilon^a$ (normal). The key innovation: by separately modelling the offer distribution, estimated preferences are **purged of demand-side effects** that would otherwise contaminate preference parameters. Model 3 (with correlated errors and offer covariates) finds: mean Frisch elasticity = 0.30, mean Marshallian elasticity = 0.20 (Table 10) -- substantially lower than Model 2 (0.59/0.48) which ignores offer heterogeneity.

# Treatment of opportunities / constraints

**This is the paper's central contribution.** The offer distribution $g(h|Z^o)$ is an explicit model of demand-side hours restrictions. Key findings:

- **Bimodal offer distribution (Table 5):** Offers concentrate at part-time (~15 hours, $m_1$) and full-time (~38 hours, $m_2$), consistent with institutional hours norms.
- **Observable heterogeneity in offers (Model 3):** More educated women are more likely to receive full-time offers ($p_1$ lower for education levels 2 and 3). London residents face similar offer distributions. Year effects are weak.
- **Quantitative importance:** Unconstrained employment = 71%, constrained (two-offer) employment = 62.5%. Average unconstrained hours = 35.5, constrained = 26.2. Hours restrictions reduce both employment and hours substantially.
- **Who is constrained?** Women rejecting the unrestricted model (Table 9) are more often lone mothers, younger, lower-wage, with more children -- they belong to "significantly poorer households" and "work shorter hours."

# Welfare / normative object

No welfare analysis is conducted. The paper is purely positive (identification and estimation of preferences + offer distribution). However, the framework has direct welfare implications: if women are constrained to suboptimal hours, their realized utility is below their unconstrained optimum. The gap between constrained and unconstrained utility is a measure of the welfare cost of hours restrictions -- directly related to the $A$ component in $W(z, R, A; y)$.

# Main findings

**Rejection of unrestricted model:**
- 2.6% of working women observed at strictly dominated hours (nonparametric rejection)
- Additional 0.4% would earn more by not working (violation of participation rationality)
- Using estimated parameters (Model 3, $\phi$), 7.9% of working women fail the revealed preference inequality (parametric rejection, Figure 3)
- Rejected women are poorer, lower-wage, with more children (Table 9)

**Offer distribution (Table 5):**
- Part-time mode: $m_1 \approx 14$--$15$ hours, $\sigma_1 \approx 17$
- Full-time mode: $m_2 \approx 38$ hours, $\sigma_2 \approx 1.7$
- Mixture probability $p_1 \approx 0.83$--$0.89$ (most offers concentrate near part-time or full-time)

**Preference estimates (Table 4, Model 3):**
- $\phi$ (leisure curvature): 15.1 for young cohort, 7.3--14.4 for older cohort (high disutility of work)
- $\gamma$ (consumption curvature): 0.001 for young cohort, 0.003 for older (close to linear in consumption)
- Fixed cost of work: ~£36/week for reference lone mother; higher for London (+£33), more children (+£5--20)

**Elasticities (Table 10, Model 3):**
- Mean Frisch elasticity: 0.30 (vs. 0.58 ignoring offer restrictions in Model 1)
- Mean Marshallian elasticity: 0.20 (vs. 0.58 in Model 1)
- Accounting for restrictions roughly halves estimated elasticities

**Simulations (Table 11, Figures 6--7):**
- Unconstrained model predicts 71% employment; two-offer model predicts 62.5%
- Average hours: 35.5 (unconstrained) vs. 26.2 (constrained)
- 10% wage increase: intensive margin response 0.35 (unconstrained) vs. 0.16 (constrained); extensive margin similar (0.25 vs. 0.27)

# Main limitations

- Two-offer restriction is arbitrary -- why exactly two? The $n$-offer extension is mentioned but not implemented
- Offer distribution assumed independent of preferences (no sorting of workers to jobs by taste)
- Only women with children; male labour supply and childless women excluded
- Static model applied to a period with major policy changes (WFTC introduction)
- Offer distribution modelled parametrically (mixture of normals); nonparametric estimation not implemented empirically
- No welfare analysis despite the framework being well-suited for it

# Relevance for my JMP

## possible use for framing
The paper provides the strongest econometric justification for modelling demand-side restrictions in labour supply -- directly motivating the $A$ component in $W(z, R, A; y)$. The finding that 8% of working women are at hours inconsistent with free choice demonstrates that the feasible set $A$ is binding and economically important.

## possible use for model design
The two-offer model is an alternative to the RURO framework for modelling restricted choices. Key differences: RURO uses a continuous opportunity density $p(h, w)$ while Beffy et al. use a discrete offer distribution $g(h)$ with a finite number of offers. The RURO approach is more general (allows wage variation across offers) but requires stronger distributional assumptions. The identification results in Lemmas 1--2 could inform the identification strategy for the RURO model.

## possible use for identification
The paper's key identification insight -- that dominated regions of the budget constraint identify the offer distribution nonparametrically -- has no direct analogue in the RURO framework. This suggests that the nonlinear budget constraint provides identification content for $A$ that the RURO framework may not fully exploit.

## possible use for decomposition
The paper's comparison of constrained vs. unconstrained hours (Table 11) directly quantifies the effect of $A$ on outcomes. The gap between unconstrained (35.5 hours) and constrained (26.2 hours) average hours is a measure of how much opportunities restrict choices -- the empirical content of the $A$ component.

## possible use for comparative application
The UK-specific offer distribution (bimodal at ~15 and ~38 hours) can be compared against the Norwegian opportunity density in the RURO literature (bimodal at part-time and full-time peaks). Cross-country differences in offer distributions directly inform the $A$ component of $W(z, R, A; y)$.

# Research questions this paper inspires

1. Can the welfare cost of hours restrictions be computed within this framework? The gap between constrained and unconstrained utility for each woman provides an individual-level measure of the cost of restricted $A$ -- directly related to the $W(z, R, A; y)$ framework.

2. How does the two-offer model compare to the RURO model when estimated on the same data? If both produce similar offer distributions but different preference estimates, this would reveal which modelling assumptions are most consequential.

3. The paper finds that accounting for restrictions halves estimated elasticities (0.30 vs. 0.58 Frisch). How would this affect revealed inequality aversion in the Bargain et al. (2014) framework? Lower "true" elasticities imply higher $\gamma$.

4. Can the identification-via-dominated-regions approach be extended to identify the wage component of the offer distribution (not just hours), connecting to the full RURO opportunity density $p(h, w)$?

# Challenge to this paper

The two-offer restriction, while tractable and yielding clean identification results, is fundamentally arbitrary. The paper acknowledges this ("the two-offer specification... is nevertheless restrictive") but does not estimate the number of offers from the data. If individuals actually face 5 or 10 offers, the two-offer model would overstate the degree of constraint and thus understate elasticities. Conversely, if some individuals face only one offer (take-it-or-leave-it), the model understates constraints. The RURO framework avoids this issue by treating the number of latent opportunities as a parameter of the opportunity density, but at the cost of stronger distributional assumptions. An ideal framework would estimate the effective number of offers as a function of worker characteristics, connecting to the RURO's opportunity scale parameter $g_0$.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper explicitly models hours restrictions as arising from "the hours offered by employers" (p. 2), which is the demand-side component of the feasible set $A$ in $W(z, R, A; y)$. The offer distribution $g(h)$ is an empirical counterpart of $A$ (restricted to the hours dimension).

[Reasonable inference for my project] The identification results (Lemmas 1--2) provide a formal basis for the claim that $R$ and $A$ can be separately identified in a structural model -- the key requirement for the $W(z, R, A; y)$ framework to be operational. The paper shows that nonlinearities in the budget constraint (which is determined by $y$, the tax-benefit schedule) provide the exclusion restrictions needed to separate $R$ from $A$.

[Unclear from paper] Whether the framework can be extended to incorporate wage heterogeneity across offers (moving from $g(h)$ to the full $p(h, w)$ of the RURO model). Also unclear: how the welfare cost of restricted choices would compare to the welfare cost measured by the equivalent income approach in Bargain et al. (2013).

The paper is closest to: **identification and estimation of the feasible set $A$** and **separation of preferences $R$ from opportunities $A$**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute welfare metrics assuming unrestricted choice -- individuals are evaluated as if they freely chose their hours. Beffy et al. (2019) show that ~8% of women are at hours inconsistent with free choice. If welfare metrics are computed at constrained (rather than freely chosen) hours, the welfare rankings could change: a woman forced into suboptimal hours by restricted offers would be evaluated as worse off under any preference-respecting metric. The combination of the two frameworks -- Fleurbaey metrics applied to a restricted-choice model -- would provide welfare measures that account for both preference heterogeneity ($R$) and opportunity constraints ($A$).

# Relation to opportunities vs preferences

The paper provides the clearest formal demonstration that opportunities and preferences are separately identifiable in a structural labour supply model. The identification rests on three sources of information: (1) the shape of the budget constraint (dominated regions identify $A$), (2) variation in budget constraints across individuals (exclusion restrictions separate $R$ from $A$), and (3) the parametric structure of preferences and offers. The finding that ignoring restrictions approximately doubles estimated elasticities shows that conflating $R$ and $A$ has large quantitative consequences for both positive (elasticities) and potentially normative (welfare evaluation) conclusions.

# Useful quotations / formulas

**On the rejection of unrestricted choice (p. 16):**
"about 2.6% of working women are observed working at hours that belong to the set of irrational choices... This is a nonparametric rejection."

**On the importance of restrictions (p. 22):**
"Accounting for restrictions on the choice set changes the estimated pattern of preference parameters. Individuals appear more responsive once restrictions are accounted for and the model simulations predict a higher level of employment were restrictions to be removed."

**Two-offer choice probability (eq. 2):**
$$\ell_{2i}(Z, \beta) = g_i^2 + 2g_i \sum_{j \neq i} g_j p_i(\{i, j\}, Z, \beta)$$

**Utility function (eq. 13):**
$$u(c, h) = \frac{c^{1-\gamma}}{1-\gamma} + \frac{(L - h)^{1-\phi}}{1-\phi} a$$

**Employment effect of restrictions (Table 11):**
Unconstrained: 71% employment, 35.5 mean hours. Two-offer: 62.5% employment, 26.2 mean hours.

# Suggested tags

restricted-choices, two-offer-model, offer-distribution, consideration-set, identification, Gale-Nikaido, dominated-regions, discrete-choice, fixed-costs, nonlinear-budget, hours-restrictions, demand-side, UK, FES, IFS-Taxben, labour-supply, Frisch-elasticity

# My quick takeaway

This paper is the econometric counterpart to the RURO framework's modelling of opportunities. While RURO uses continuous opportunity densities, Beffy et al. use a discrete offer distribution with formal identification proofs. The key empirical finding -- that ~8% of women are at dominated hours and that accounting for restrictions halves elasticities -- provides strong evidence that the feasible set $A$ is economically important and cannot be ignored in welfare evaluation. For my JMP, this paper provides: (1) formal identification arguments for separating $R$ from $A$, (2) empirical evidence on the magnitude of hours restrictions, and (3) a benchmark for comparing the RURO approach to alternative restricted-choice models. The main limitation relative to RURO is that the offer distribution is over hours only, not hours-wage pairs, and the number of offers is fixed rather than estimated.
