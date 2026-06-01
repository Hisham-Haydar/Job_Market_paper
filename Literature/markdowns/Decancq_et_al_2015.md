---
title: "Happiness, Equivalent Incomes and Respect for Individual Preferences"
authors: [Koen Decancq, Marc Fleurbaey, Erik Schokkaert]
year: 2015
outlet: "Economica, 82(s1), 1082--1106"
country_or_context: "Russia"
population: "Russian adults (RLMS-HSE panel)"
data_period: "1995--2003 (7 waves)"
shelf: "equivalent income / subjective well-being / preference heterogeneity / multidimensional welfare / axiomatic"
tags: [equivalent-income, subjective-well-being, happiness, preferences, axiomatic, multidimensional, health, unemployment, housing, Russia, RLMS, ordered-logit, fixed-effects, Decancq, Fleurbaey, Schokkaert, personal-preference-principle, same-preference-principle, weak-dominance]
priority: "high"
read_status: "extracted"
---

# Full citation

Decancq, K., Fleurbaey, M., & Schokkaert, E. (2015). Happiness, equivalent incomes and respect for individual preferences. *Economica*, 82(s1), 1082--1106.

# One-sentence contribution

Develops an axiomatic comparison of welfare measures -- hedonic, subjective well-being, equivalent income, and objective -- showing that only equivalent income simultaneously satisfies the personal-preference principle, same-preference principle, and weak dominance principle, and demonstrates empirically using Russian panel data that equivalent income rankings differ substantially from both expenditure rankings and life satisfaction rankings, with health being the key differentiating dimension.

# Why this paper matters

This paper provides the strongest axiomatic case for equivalent income as a welfare measure by showing that it uniquely satisfies three normatively appealing properties that competing measures violate. The empirical application demonstrates that the choice of welfare measure is not merely theoretical: it changes who is identified as worst-off, with implications for targeting social policy. The finding that least satisfied individuals are not the most deprived in equivalent income terms -- they are younger, better educated, and healthier but have higher aspirations -- directly challenges the use of subjective well-being as a social welfare criterion.

# Core research question

Which welfare measures respect individual preferences, and how do equivalent income rankings compare empirically with expenditure, subjective well-being, and objective welfare rankings?

# Economic setting and context

Russian households during the transition period (1995--2003), a setting with large variation in income, health, housing quality, unemployment, and wage arrears. The RLMS-HSE panel provides repeated observations on the same individuals, enabling fixed-effects estimation of preference parameters.

# Model / theoretical framework

**Three axioms for well-being measurement:**

1. **Personal-preference principle:** For any individual $i$ with preferences $R_i$, if $(y, q) P_i (y', q')$ then $W_i(y, q) > W_i(y', q')$. The well-being ordering respects the individual's own preferences for intrapersonal comparisons.

2. **Same-preference principle:** For two individuals $i, j$ with identical preferences $R_i = R_j$, if $(y_i, q_i) P_i (y_j, q_j)$ then $W_i > W_j$, regardless of any scaling factors $s_i, s_j$ that may differ between them. Interpersonal comparisons between individuals with the same preferences should respect those preferences.

3. **Weak dominance principle:** At the optimal non-income quality of life $q^*(y; R_i)$ chosen by $i$ when free to choose, higher income implies higher well-being.

**Key impossibility result:** The (strong) dominance principle -- stating that $(y_i \geq y_j, q_i \geq q_j)$ with at least one strict inequality implies $W_i > W_j$ -- is incompatible with the personal-preference principle. This motivates the weak dominance principle, which restricts dominance to comparisons at optimal non-income bundles.

**Table 1 -- Axiomatic scorecard:**

| Measure | Personal-preference | Same-preference | Weak dominance | Dominance |
|---------|-------------------|-----------------|----------------|-----------|
| Hedonic (e.g., capabilities) | No | No | No | Yes |
| Subjective well-being | Yes | No | No | No |
| Equivalent income | Yes | Yes | Yes | No |
| Objective (e.g., income) | No | No | No | Yes |

SWB fails same-preference because two individuals with identical preferences but different scaling factors (aspirations) may report different satisfaction levels, leading to different welfare rankings even though both would agree on which situation is better. Equivalent income uniquely satisfies all three applicable axioms.

**Equivalent income definition (eq. 1):**
$(y_i, q_i) \, I_i \, (y_i^*, q^*(y_i^*; R_i))$

The equivalent income $y_i^*$ is the income that, combined with the optimal non-income conditions the individual would freely choose at that income level, yields the same utility as the actual situation $(y_i, q_i)$.

**Satisfaction equation with interactions:**
$$S_{it} = \alpha_i + \mu_t + (\beta + \Gamma Z_{it}) \ln(y_{it}) + (\theta + \Lambda Z_{it})' q_{it} + \delta' Z_{it} + d_{it}$$

where $Z_{it}$ = demographic characteristics (age, gender, education, minority status), $q_{it}$ = non-income dimensions, $\alpha_i$ = individual fixed effects.

**Marginal rate of substitution:**
$$MRS^{yq} = y_{it} \cdot \frac{\theta + \Lambda Z_{it}}{\beta + \Gamma Z_{it}}$$

**Equivalent income formula (eq. 5):**
$$y_{it}^* = y_{it} \cdot \exp\left[\frac{(\theta + \Lambda Z_{it})}{(\beta + \Gamma Z_{it})}' \cdot (q_{it} - q_i^*)\right]$$

where $q_i^*$ is the reference (optimal) level of non-income dimensions for individual $i$.

# Key objects

- **Personal-preference principle:** Intrapersonal welfare comparisons respect own preferences.
- **Same-preference principle:** Interpersonal comparisons between individuals with identical preferences respect those preferences, regardless of scaling factors.
- **Weak dominance principle:** At freely chosen non-income conditions, more income implies higher well-being.
- **Equivalent income $y_i^*$:** Income at reference non-income conditions yielding same utility as actual situation.
- **Reference values $q_i^*$:** Perfect health (=5), 90th percentile housing quality, no wage arrears; unemployment reference is group-specific (men prefer employment, women's preference varies).
- **Scaling factors $s_i$:** Individual-specific factors (aspirations, adaptation, personality) that affect satisfaction reports but not preferences over bundles. The key reason SWB fails same-preference.

# Data

Russian Longitudinal Monitoring Survey (RLMS-HSE), 1995--2003, 7 waves. 12,016 individuals. Five life dimensions: (1) expenditures per consumption unit (log), (2) self-assessed health (1--5 scale), (3) housing quality index, (4) unemployment status, (5) wage arrears. Satisfaction measured on a 5-point ordered scale. Demographics: age, gender, education, minority status.

# Identification logic

Preferences identified from within-individual variation in satisfaction responses over time (fixed effects), interacted with demographics to allow heterogeneous MRS across groups. The fixed effects absorb time-invariant unobserved heterogeneity (personality, reporting style). The Chamberlain-type approach (Jones-Schurer 2011 approximation) handles the incidental parameters problem in ordered logit with fixed effects. Key assumption: the satisfaction function captures preference orderings over $(y, q)$ bundles, and the interaction terms $\Gamma, \Lambda$ capture systematic preference heterogeneity across demographic groups.

# Estimation / empirical strategy

Ordered logit with Chamberlain-type fixed effects (Jones and Schurer 2011 approximation). Dependent variable: 5-point life satisfaction. Explanatory variables: log expenditures, health, housing quality, unemployment, wage arrears, all interacted with age, gender, education, minority status. Time dummies included. Standard errors clustered at individual level.

# Treatment of preferences

Preferences are heterogeneous across demographic groups through interaction terms ($\Gamma, \Lambda$). The MRS between income and each non-income dimension varies by age, gender, education, and minority status. Key heterogeneity findings: (1) young people have lower MRS for health (health less important relative to income when young); (2) men have higher MRS for unemployment (stronger preference for employment); (3) minorities have lower MRS for income (lower marginal utility of expenditure). Individual fixed effects capture time-invariant preference heterogeneity beyond demographics.

# Treatment of opportunities / constraints

No explicit treatment. The framework takes observed $(y_i, q_i)$ bundles as given and evaluates welfare at those bundles. There is no modelling of choice sets, labour market constraints, or demand-side restrictions. The reference non-income conditions $q_i^*$ are defined as the levels the individual would "freely choose" at income $y_i^*$, but the paper does not model what constrains actual choices. The unemployment dimension is treated as a life outcome affecting well-being, not as an opportunity constraint.

# Welfare / normative object

Equivalent income $y_i^*$ is the welfare measure. The paper argues for it on axiomatic grounds (satisfies personal-preference, same-preference, and weak dominance) and computes it empirically. No social welfare function is aggregated -- the focus is on identifying who is worst-off and how the composition of the worst-off group changes across welfare measures.

# Main findings

1. **Axiomatic superiority of equivalent income:** Only equivalent income satisfies all three axioms (personal-preference, same-preference, weak dominance). SWB fails same-preference; hedonic/objective measures fail personal-preference.

2. **Satisfaction estimation (Table A2):** Log expenditures coefficient = 0.314***, health = 0.432***, housing = 0.284***. Significant interactions: young $\times$ health negative, male $\times$ health negative, male $\times$ unemployed strongly negative ($-0.347$***), minority $\times$ expenditure $-0.253$***.

3. **Low correlation between welfare measures:** Spearman $\rho$(EI, expenditures) = 0.48, $\rho$(EI, objective index) = 0.64, $\rho$(EI, SWB) = 0.25. The welfare measures identify very different populations as worst-off.

4. **Health is the key differentiator:** Moving from expenditure-only ranking (Set I) to expenditure + health (Set II), over 50% of the bottom decile is reclassified. Adding further dimensions (housing, unemployment, wage arrears) produces smaller marginal changes. The portrait of the deprived depends critically on whether health is included.

5. **Least satisfied $\neq$ worst-off in EI:** The least satisfied individuals are younger, better educated, healthier, have larger expenditures, and are more likely female. They are not the most deprived but have higher aspirations (different scaling factors $s_i$). This empirically confirms the theoretical prediction that SWB conflates preferences with scaling factors.

6. **Equivalent income identifies a different worst-off group:** The EI-worst-off are older, less educated, in worse health, with lower expenditures -- a profile more consistent with intuitive notions of deprivation than the SWB-worst-off profile.

# Main limitations

- Russian transition economy may not be representative of stable developed economies.
- Satisfaction data as a proxy for preference orderings: the identifying assumption that $S_{it}$ captures ordinal preferences over $(y, q)$ may be violated if satisfaction is affected by factors beyond $(y, q)$ in ways not captured by fixed effects.
- Group-level preference heterogeneity only (via interactions): individual-level preference heterogeneity is absorbed by fixed effects but not used for individual-level MRS computation beyond demographics.
- The reference values $q_i^*$ are chosen by the researcher, not derived from the model. The "optimal" non-income conditions are assumed, not estimated.
- Only five life dimensions; many important dimensions (social connections, environment, autonomy) excluded.
- Ordered logit with fixed effects approximation may not fully resolve the incidental parameters problem.
- No demand-side modelling: unemployment treated as a welfare-affecting outcome, not as an opportunity constraint.

# Relevance for my JMP

## possible use for the axiomatic foundation of equivalent income
The three axioms (personal-preference, same-preference, weak dominance) and the impossibility of the dominance principle provide the normative justification for using equivalent income rather than SWB or objective measures in my welfare analysis. The finding that SWB fails same-preference -- because scaling factors (aspirations, adaptation) contaminate interpersonal comparisons -- is a key argument for equivalent income in my JMP.

## possible use for demonstrating that welfare measure choice affects who is worst-off
The empirical finding that the bottom decile changes composition by 50%+ when moving from expenditures to equivalent income (with health as the key differentiator) motivates the importance of getting the welfare measure right. In my RURO framework, the opportunity dimension (job availability) may play a similar role to health in reclassifying who is worst-off.

## possible use for preference heterogeneity methodology
The satisfaction-based approach to estimating heterogeneous MRS (through interaction terms and fixed effects) is a complement to the structural discrete-choice approach used in Bargain et al. (2013). My JMP could compare equivalent incomes computed from structural preferences (via labour supply models) with those computed from satisfaction data (via the Decancq et al. approach) as a robustness check.

# Research questions this paper inspires

1. How would the equivalent income rankings change if the unemployment dimension were modelled as an opportunity constraint (RURO) rather than a welfare-affecting outcome? In the RURO framework, involuntary unemployment reduces the opportunity set $A_i$, which affects equivalent income through the feasible job set rather than through a direct utility penalty.

2. Can the satisfaction-based MRS estimation be combined with structural labour supply models to produce more credible equivalent income estimates? The satisfaction approach identifies preferences from subjective reports; the structural approach identifies them from observed choices. The two should agree if the model is well-specified.

# Challenge to this paper

The paper treats unemployment as a non-income dimension affecting well-being ($q_{it}$ includes an unemployment indicator), but does not model it as an opportunity constraint. In the RURO framework, unemployment restricts the feasible set $A_i$ -- it is not merely a bad outcome but a reduction in the available choices. The equivalent income formula $y_{it}^* = y_{it} \cdot \exp[\ldots(q_{it} - q_i^*)]$ treats unemployment symmetrically with health and housing quality, as a dimension where the individual has a "preference" (MRS). But unemployment is not chosen; it reflects a binding demand-side constraint. The RURO approach would compute equivalent income by integrating over the restricted opportunity set, not by applying a utility penalty for the unemployment state.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The equivalent income $y_i^*$ corresponds to the well-being measure $W(z, R, A; y)$ in my framework, with the non-income dimensions $q_{it}$ capturing aspects of the realized bundle $z$. The personal-preference principle corresponds to respecting $R_i$ in welfare evaluation. The reference conditions $q_i^*$ correspond to the reference wage $\tilde{w}$ and reference opportunity set in my framework.

[Reasonable inference for my project] The paper's finding that preference heterogeneity (through MRS interactions) substantially affects who is worst-off supports using heterogeneous preferences in my RURO model rather than representative-agent assumptions. The demographic interactions ($\Gamma, \Lambda$) in the satisfaction equation are analogous to demographic shifters in the utility function of discrete-choice labour supply models.

[Unclear from paper] Whether the satisfaction-based MRS estimates are consistent with structural labour supply estimates for the same population. If the two approaches give different MRS between leisure and consumption, the equivalent income computation would differ, raising the question of which preference measure to trust for welfare evaluation.

# Relation to Bargain et al. (2013)

Both papers compute equivalent incomes incorporating non-income dimensions and preference heterogeneity. The key differences: (1) Bargain et al. estimate preferences from observed labour supply choices (revealed preference), while Decancq et al. estimate them from satisfaction reports (stated/experienced preference); (2) Bargain et al. focus on leisure/labour as the non-income dimension, while Decancq et al. include health, housing, unemployment, and wage arrears; (3) Bargain et al. use structural discrete-choice models, while Decancq et al. use ordered logit with fixed effects; (4) Bargain et al. aggregate using maximin (Rawlsian), while Decancq et al. focus on identifying the worst-off without specifying an aggregation rule.

# Relation to opportunities vs preferences

The paper is about preferences (and their measurement), not opportunities. The axiomatic framework assumes individuals have well-defined preferences $R_i$ over $(y, q)$ bundles and evaluates welfare at observed bundles. Opportunities do not enter: there is no modelling of what bundles are feasible. Unemployment is treated as a preference-affecting outcome, not as an opportunity constraint. The key distinction -- that SWB conflates preferences with scaling factors (aspirations) -- is about measurement of preferences, not about the role of opportunities in shaping outcomes.

# Useful quotations / formulas

**On the personal-preference principle (p. 1084):**
"The personal-preference principle requires the well-being ordering over own situations of a given individual to respect her own preferences."

**On same-preference vs personal-preference (p. 1085):**
"When two individuals have the same preferences but different scaling factors, the same-preference principle requires their well-being ordering to follow their common preferences."

**On SWB failure (p. 1086):**
"Subjective well-being [...] satisfies the personal-preference principle but violates the same-preference principle and the weak dominance principle."

**On who is worst-off (p. 1099):**
"The least satisfied in our sample tend to be younger, better educated, in better health, have higher expenditures and are more likely to be female. They are not the most deprived."

**Equivalent income formula (eq. 5, p. 1093):**
$$y_{it}^* = y_{it} \cdot \exp\left[\frac{(\theta + \Lambda Z_{it})}{(\beta + \Gamma Z_{it})}' \cdot (q_{it} - q_i^*)\right]$$

**On the impossibility of dominance + personal-preference (p. 1085):**
"It is impossible to satisfy the dominance principle and the personal-preference principle simultaneously."

# Suggested tags

equivalent-income, subjective-well-being, happiness, preferences, axiomatic, multidimensional, health, unemployment, housing, Russia, RLMS, ordered-logit, fixed-effects, Decancq, Fleurbaey, Schokkaert, personal-preference-principle, same-preference-principle, weak-dominance, scaling-factors, aspirations, MRS

# My quick takeaway

The definitive axiomatic case for equivalent income over SWB and objective measures: only equivalent income respects individual preferences for both intrapersonal and same-preference interpersonal comparisons while satisfying weak dominance. The empirical application to Russia shows that health is the key dimension that reclassifies who is worst-off (50%+ reclassification), and that least-satisfied individuals are not the most deprived -- they have higher aspirations (scaling factors). For my JMP, this provides the normative foundation for equivalent income and motivates extending the framework to include the opportunity dimension (job availability), which this paper does not address.
