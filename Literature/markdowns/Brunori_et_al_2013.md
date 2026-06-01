---
title: "Inequality of Opportunity, Income Inequality and Economic Mobility: Some International Comparisons"
authors: [Paolo Brunori, Francisco H. G. Ferreira, Vito Peragine]
year: 2013
outlet: "IZA Discussion Paper No. 7155"
country_or_context: "International comparison: 41 countries (IEO), 39 countries (HOI)"
population: "National household survey populations across rich and poor economies"
data_period: "Various survey years, approximately 1985--2010"
shelf: "inequality of opportunity / cross-country comparison / circumstances / fairness / intergenerational mobility"
tags: [inequality-of-opportunity, ex-ante-IOp, human-opportunity-index, cross-country, unfair-inequality, circumstances-effort, intergenerational-mobility, compensation, Brunori, Ferreira, Peragine, lower-bound, Kuznets-curve]
priority: "medium"
read_status: "extracted"
---

# Full citation

Brunori, P., Ferreira, F. H. G., & Peragine, V. (2013). Inequality of opportunity, income inequality and economic mobility: Some international comparisons. IZA Discussion Paper No. 7155.

# One-sentence contribution

Synthesises cross-country evidence on two families of ex-ante opportunity-sensitive measures -- an inequality of economic opportunity index (IEO) across 41 countries and the Human Opportunity Index (HOI) across 39 countries -- finding substantial international variation, an inverted-U "Kuznets curve" for opportunity inequality vs development, and strong positive associations between inequality of opportunity and intergenerational persistence.

# Why this paper matters

This paper provides the clearest empirical overview of the inequality-of-opportunity literature, showing how the compensation-vs-responsibility framework is operationalised across countries. For my JMP, it positions the broader normative motivation (inequalities due to circumstances are unfair) while highlighting the gap between the literature's coarse empirical implementation (type means, observed circumstances) and a richer structural approach that separates preferences, opportunity sets, and pay schedules.

# Core research question

Can one make meaningful international comparisons of inequality of opportunity using ex-ante measures, and what empirical associations emerge between opportunity inequality, overall inequality, development, and intergenerational mobility?

# Economic setting and context

International and synthetic. Assembles country-level evidence from eight studies for IEO and World Bank HOI applications for 39 African and Latin American countries. Countries span Europe, Latin America, Africa, North America, Asia, and the Middle East. Outcome variables differ across studies: post-tax earnings, gross income, household per capita income/consumption.

# Model / theoretical framework

**Normative-measurement framework** from the equality-of-opportunity literature. Population partitioned into **types** (homogeneous in observed circumstances $C$) and **tranches** (same percentile of type-specific advantage distribution, under Roemer's identification assumption).

**Ex-ante approach:** Replace each individual's observed advantage with the type mean; compute inequality over the smoothed distribution. The between-type inequality is the ex-ante measure of unfair inequality.

**IEO measures:**
- $IEO\text{-}L$: Inequality level in the smoothed (type-mean) distribution.
- $IEO\text{-}R = IEO\text{-}L / \text{total inequality}$: Share of total inequality attributable to opportunity (lower bound).

**Human Opportunity Index:**
$$H_j = \bar{p}_j(1 - D_j)$$
where $\bar{p}_j$ = average service coverage, $D_j$ = dissimilarity index across types. Development index penalised for unequal opportunities.

**Lower-bound logic:** Observed circumstance variables are a strict subset of all true circumstances. Adding more circumstances can only increase the estimated opportunity-inequality component. All IEO measures are therefore lower bounds.

# Key objects

- **IEO-R:** Ranges from 0.02 (Norway) to 0.34 (Guatemala). Brazil ~0.32.
- **IEO-L:** Ranges from 0.003 (Norway) to 0.223 (Brazil).
- **HOI:** Ranges from ~10 (Niger) to ~92 (Chile).
- **Intergenerational elasticity:** Positively correlated with IEO-R ($\rho = 0.585$).
- **Intergenerational correlation of education:** Also positively correlated with IEO-R ($\rho = 0.597$).

# Data

Synthesised from eight studies for IEO (EU-SILC 2005, Latin American surveys, PSID, IHDS India, African surveys). HOI from World Bank applications. No single harmonised micro dataset.

# Identification logic

Not causal identification. Defines types by observed circumstances, computes type-level opportunity valuations, and measures inequality across those valuations. Lower-bound interpretation rests on circumstance incompleteness.

# Estimation / empirical strategy

1. Collects existing IEO estimates from eight studies for 41 countries.
2. Assembles HOI values for 39 countries.
3. Descriptive cross-country correlations with GNI per capita, total inequality, intergenerational persistence.
4. Notes comparability challenges (different outcome variables, circumstance vectors, estimation methods).

# Treatment of preferences

Not modelled. The equality-of-opportunity framework distinguishes effort from circumstances but does not separately identify preference heterogeneity. Between-type inequality is attributed to circumstances; within-type variation (which includes both preference heterogeneity and unobserved circumstances) is in the residual.

# Treatment of opportunities / constraints

"Opportunity" here refers to the normative equality-of-opportunity concept (type-level advantage prospects associated with observed circumstances), NOT to explicit feasible job sets, latent offers, or demand-side labour market constraints. There is no modelling of hours restrictions, occupational menus, or personalised wage-offer sets. The paper does not distinguish observed choices from a latent availability distribution of jobs.

# Welfare / normative object

Inequality indices (IEO-L, IEO-R, HOI), not a direct welfare function. The normative motivation is compensatory: inequalities due to circumstances beyond individual control are unfair and should be compensated. No explicit welfare measure combining realised bundles, preferences, and opportunity sets.

# Main findings

1. **Substantial cross-country variation in IEO-R:** Norway (0.02) to Guatemala (0.34). Nordic countries lowest; Latin America and Sub-Saharan Africa highest.

2. **Inverted-U relationship with development:** A "Kuznets curve" for opportunity inequality vs log GNI per capita. Significant linear and quadratic terms.

3. **Positive correlation with overall inequality:** $\rho = 0.523$ between IEO-R and total inequality.

4. **Negative association with intergenerational mobility:** Higher IEO-R correlates with higher intergenerational income elasticity ($\rho = 0.585$) and higher education persistence ($\rho = 0.597$).

5. **HOI highly correlated with HDI:** $\rho = 0.941$, suggesting most cross-country variation is driven by mean service coverage, not the inequality penalty.

6. **Different measures, different rankings:** HOI's dissimilarity index and IEO-R produce very different -- even negatively correlated -- country rankings in common samples. Different ex-ante measures capture different things.

# Main limitations

- Comparability: different studies use different outcome variables, circumstance vectors, survey years, estimation methods.
- IEO measures are only lower bounds (circumstance incompleteness).
- Does not model actual job opportunities, offer distributions, or labour market constraints.
- Does not separately identify preferences, opportunities, and pay schedules.
- Not a welfare measure; inequality indices only.

# Relevance for my JMP

## possible use for framing and positioning
The paper motivates why inequality should be decomposed into fair (effort/responsibility) and unfair (circumstance/opportunity) components, and shows how the literature operationalises this across countries. My JMP's structural approach -- modelling opportunity sets $A$ explicitly through RURO rather than proxying with observed circumstances -- can be positioned as advancing this literature.

## possible use for the lower-bound logic
The finding that IEO measures are lower bounds (because observed circumstances are incomplete) is directly relevant. My RURO framework, by modelling the full opportunity density $g(h,w)$, can potentially capture aspects of opportunity inequality that circumstance-based methods miss -- specifically, demand-side constraints on job availability that are not proxied by parental background or education.

## possible use for cross-country context
The empirical regularities (Nordic countries have low IEO, Latin America high) provide context for situating any future application of my framework.

# Research questions this paper inspires

1. How would country rankings change if opportunities were measured through explicit feasible job sets (RURO opportunity densities) rather than through observed circumstance partitions? Countries with similar circumstance-based IEO but different labour market structures might rank very differently.

2. Can the lower-bound logic be tightened by using structural labour supply models to estimate the "true" opportunity set, capturing demand-side constraints that circumstance partitions miss?

# Challenge to this paper

The operational definition of opportunity is narrow relative to the normative ambitions. By relying on type means and observed circumstance partitions, the paper captures only a lower-bound between-type component, leaving preference heterogeneity, unobserved circumstances, and actual feasible job sets in the residual. In the RURO framework, opportunity is the set of available jobs $A_i = \{(h, w) : \text{available to } i\}$, which depends on demand-side labour market conditions that circumstance partitions do not capture. A worker with "good" circumstances (educated parents, favourable region) but facing a depressed local labour market may have worse opportunities than the IEO framework recognises.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper measures inequality attributable to observed circumstances using ex-ante between-type methods. It is situated in the compensation-vs-responsibility tradition.

[Reasonable inference for my project] The type-level opportunity valuations can be seen as reduced-form empirical proxies for some aspects of $A$, but without modelling $A$ as an actual feasible set. My framework's explicit opportunity density $g(h,w)$ provides a richer representation.

[Unclear from paper] Whether welfare should satisfy independence of $A$, independence of $y$, or other axioms relevant to my theory. The paper does not discuss these.

# Relation to Bargain et al. (2013)

Not directly related. Both concern inequality decomposition but from different angles: Bargain et al. use structural labour supply models and equivalent income; Brunori et al. use reduced-form circumstance partitions. The two approaches could complement each other: Bargain et al.'s framework could be used to estimate individual-level opportunity sets, which could then be aggregated into IEO-type measures.

# Relation to opportunities vs preferences

The paper is about **circumstances vs effort**, not about **opportunities vs preferences** in the structural labour economics sense. It does not model heterogeneous preferences directly and does not define opportunities as explicit individualised feasible sets. Its main lesson: empirical IOp work uses observed circumstances as proxies for unfair opportunity differences, which is informative but much cruder than modelling opportunities as explicit sets $A_i$.

# Useful quotations / formulas

**Core normative principle (p. 3):**
"Inequalities due to circumstances beyond individual control are unfair, and should be compensated for, while inequalities due to factors for which people can be held responsible... may be considered acceptable."

**IEO-R definition:**
$$IEO\text{-}R = \frac{IEO\text{-}L}{\text{total inequality}}$$

**HOI definition:**
$$H_j = \bar{p}_j(1 - D_j)$$

**Lower-bound interpretation:**
The IEO measures based on observed circumstances are lower bounds because observed circumstances are a strict subset of all true circumstances.

# Suggested tags

inequality-of-opportunity, ex-ante-IOp, human-opportunity-index, cross-country, unfair-inequality, circumstances-effort, intergenerational-mobility, compensation, lower-bound, Kuznets-curve, Brunori, Ferreira, Peragine

# My quick takeaway

A useful benchmark paper mapping the empirical equality-of-opportunity literature across countries. For my JMP, it motivates the normative question (isolating unfair circumstance-driven inequality) while highlighting the limitations of reduced-form approaches: IEO measures are lower bounds that rely on coarse circumstance partitions and do not model actual opportunity sets. My RURO framework advances this by modelling opportunities explicitly through $g(h,w)$, potentially capturing demand-side constraints that circumstance partitions miss. The cross-country regularities (Nordic low, Latin America high, inverted-U with development) provide useful empirical context.
