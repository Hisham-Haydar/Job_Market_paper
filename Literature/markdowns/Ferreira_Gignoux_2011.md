---
title: "The Measurement of Inequality of Opportunity: Theory and an Application to Latin America"
authors: [Francisco H. G. Ferreira, Jérémie Gignoux]
year: 2011
outlet: "Review of Income and Wealth, 57(4), 622--657"
country_or_context: "Six Latin American countries: Brazil, Colombia, Ecuador, Guatemala, Panama, Peru"
population: "Household heads and spouses aged 30--49 with positive income/consumption"
data_period: "Brazil 1996; Colombia 2003; Ecuador 2006; Guatemala 2000; Panama 2003; Peru 2001"
shelf: "inequality of opportunity / measurement / lower bound / Latin America / decomposition"
tags: [inequality-of-opportunity, lower-bound, Roemer, van-de-Gaer, between-group-inequality, Latin-America, opportunity-deprivation, mean-log-deviation, path-independent-decomposition, circumstances, Ferreira, Gignoux]
priority: "medium"
read_status: "extracted"
---

# Full citation

Ferreira, F. H. G., & Gignoux, J. (2011). The measurement of inequality of opportunity: Theory and an application to Latin America. *Review of Income and Wealth*, 57(4), 622--657.

# One-sentence contribution

Formalises a scalar measure of inequality of opportunity as between-type inequality (types defined by predetermined circumstances), proves it is a lower bound on true opportunity inequality, ties it uniquely to the mean logarithmic deviation under path-independent decomposability, and applies it to six Latin American countries.

# Why this paper matters

This paper provides the clearest theoretical bridge between the philosophical equality-of-opportunity literature and a tractable empirical measurement framework. For my JMP, it is valuable as a measurement and decomposition template while simultaneously highlighting the gap that a structural approach fills: the paper's "opportunities" are circumstance-based types, not explicit feasible sets.

# Core research question

How should inequality of opportunity be measured in theory and in practice, and what do lower-bound estimates look like across six Latin American countries when opportunities are defined by predetermined circumstances?

# Model / theoretical framework

**Measurement framework** (not behavioural/structural). Population partitioned into Roemerian types $T_k$ (homogeneous in observed circumstances $C$). Advantage variable $y$. Equality of opportunity weakened from equality of conditional distributions to equality of conditional means (van de Gaer's ex-ante approach).

**Smoothed distribution:** Replace each individual's advantage with the type mean $\mu^k$. Between-type inequality in this smoothed distribution measures opportunity inequality.

**Core indices:**
$$\theta_a = I(\{\mu_i^k\}), \qquad \theta_r = \frac{I(\{\mu_i^k\})}{I(y)}$$

With path-independent decomposability, uniquely pinned to mean logarithmic deviation $E_0$:
$$\theta_a = E_0(\{\mu_i^k\}), \qquad \theta_r = \frac{E_0(\{\mu_i^k\})}{E_0(y)}$$

**Lower-bound logic:** Any unobserved circumstance would refine the type partition and weakly increase between-type inequality. All IEO measures based on observed circumstances are therefore lower bounds on true inequality of opportunity.

# Key objects

- **IOR (parametric):** Ranges from 0.23 (Colombia) to 0.34 (Guatemala) for household per capita income; 0.25 (Colombia) to 0.51 (Guatemala) for consumption.
- **Opportunity-deprivation profiles:** Identify worst-off types in each society. Worst-off are heavily concentrated among ethnic minorities and low-parental-education backgrounds.
- Circumstance variables: parental education, father's occupation, ethnicity/race, region/area of birth, gender (in labour-earnings specifications).

# Data

Six nationally representative household surveys: Brazil PNAD 1996, Colombia ECV 2003, Ecuador ECV 2006, Guatemala ENCOVI 2000, Panama ENV 2003, Peru ENAHO 2001. Sample sizes 4,556 (Panama) to 70,521 (Brazil). Advantage: household per capita income and consumption.

# Identification logic

No causal identification. Between-type decomposition under the maintained assumption that observed circumstances are exogenous. Lower-bound interpretation rests on circumstance incompleteness: adding more circumstances can only increase the measured opportunity component.

# Estimation / empirical strategy

1. **Non-parametric:** Compute between-type inequality directly from cell means. Imprecise when many types have sparse cells.
2. **Parametric:** Reduced-form regression of log advantage on circumstances; use predicted values as the smoothed distribution. Preferred when samples are smaller.
3. Both approaches produce similar results; agreement used as robustness evidence.

# Treatment of preferences

Not modelled. No utility function, no taste heterogeneity. Preference heterogeneity is absorbed into the ethically acceptable residual component.

# Treatment of opportunities / constraints

Opportunities defined through predetermined circumstance types, NOT through explicit feasible job sets, latent offers, or demand-side labour market constraints. No $A_i$ object. The paper does not distinguish observed choices from latent availability distributions. Highly useful for the "circumstances as life chances" notion of opportunity, but not for the structural labour economics notion.

# Welfare / normative object

Inequality indices ($\theta_a$, $\theta_r$), not a welfare function. Normative motivation: inequalities due to circumstances are unfair and should be compensated; inequalities due to effort may be acceptable. No explicit welfare measure combining bundles, preferences, and opportunity sets.

# Main findings

1. Lower-bound IOR is large in all six countries: 0.23--0.34 for income, 0.25--0.51 for consumption.
2. Non-parametric and parametric estimates are generally close and never statistically significantly different.
3. Family background (parental education, father's occupation) is the most important set of circumstances.
4. Opportunity-deprived types are heavily composed of ethnic minorities and low-parental-education backgrounds.
5. Path-independent decomposability uniquely ties the measure to the mean logarithmic deviation.

# Main limitations

- Only lower bounds; true inequality of opportunity is higher.
- Opportunities are circumstance-based types, not actual feasible sets of jobs or bundles.
- Preferences and effort are not structurally modelled; the residual is not cleanly identified as "responsibility."
- Sensitive to observed circumstance set and discretisation; international comparability requires coarse coding.

# Relevance for my JMP

## possible use for measurement template
Highly useful. Provides a theoretically grounded lower-bound decomposition framework with a unique axiomatic tie to $E_0$. Could be adapted if the advantage variable were replaced by equivalent income $W(z,R,A;y)$.

## possible use for positioning
The lower-bound logic motivates richer approaches: my RURO framework, by modelling the full opportunity density $g(h,w)$, can capture aspects of opportunity inequality that circumstance partitions miss -- specifically demand-side job-availability constraints.

## possible use for opportunity-deprivation profiles
The idea of ranking types by mean advantage to identify the worst-off is directly relevant for welfare-policy applications.

# Research questions this paper inspires

1. Can a lower-bound inequality-of-opportunity measure be constructed when opportunities are represented by estimated feasible job sets rather than by observed background types?

2. How would the between-type opportunity share change if the advantage variable were a well-being index $W(z,R,A;y)$ rather than income or consumption?

3. What axioms would be needed to replace the MLD-based opportunity measure with one defined over a richer well-being object while preserving path-independent decomposition?

# Challenge to this paper

The measure's ethical interpretation depends on a sharp partition between "circumstances" and everything else, but the empirical implementation has no structural account of effort, preferences, or choice. The residual is treated as ethically distinct without demonstrating that it is genuinely responsibility-sensitive. My RURO framework can address this by modelling opportunity sets $A_i$ explicitly, so that within-type variation is more meaningfully interpretable.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] Opportunity inequality defined through between-type inequality; no $W(z,R,A;y)$, no feasible-set $A$, no preference $R$, no pay schedule $y$.

[Reasonable inference for my project] The smoothed-distribution logic and lower-bound interpretation could carry over if applied to well-being rather than income. Opportunity-deprivation profiles could be redefined over $W$-type groupings.

[Unclear from paper] How the type-based notion of opportunity maps into $A$; how $R$ could be incorporated; whether path-independent decomposability extends to welfare measures.

# Relation to Bargain et al. (2013)

Not directly related. Both concern inequality decomposition but from different angles: Bargain et al. use structural labour supply and equivalent income; Ferreira & Gignoux use reduced-form circumstance partitions. The frameworks could complement each other: Bargain et al.'s approach could estimate individual-level opportunity sets, which could then be aggregated into IEO-type measures.

# Relation to opportunities vs preferences

Strongly about opportunities versus responsibility, but only weakly about opportunities versus preferences. Opportunities are formalised through circumstance types; preferences do not appear. The ethically admissible remainder is not identified as preference heterogeneity but as whatever is left after netting out between-type opportunity inequality.

# Useful quotations / formulas

**Core indices (eqs. 5'--6'):**
$$\theta_a = E_0(\{\mu_i^k\}), \qquad \theta_r = \frac{E_0(\{\mu_i^k\})}{E_0(y)}$$

**Lower-bound result (Section 3):** Any unobserved circumstance variable refines the type partition and weakly increases between-type inequality in the smoothed distribution.

**Key empirical result:** Parametric IOR ranges from 0.23 (Colombia) to 0.34 (Guatemala) for income.

# Suggested tags

inequality-of-opportunity, lower-bound-measurement, Roemer, van-de-Gaer, Latin-America, between-group-inequality, opportunity-deprivation-profile, mean-log-deviation, path-independent-decomposition, circumstances, Ferreira, Gignoux

# My quick takeaway

The most useful paper in this corpus for the theoretical foundations of inequality-of-opportunity measurement. Its main contributions -- the unique axiomatic tie to MLD, the lower-bound interpretation, and opportunity-deprivation profiles -- are directly usable as a decomposition and measurement template. Its limitation for my JMP is the same as the broader IOp literature: opportunities are defined through circumstance partitions rather than explicit feasible sets, and preferences are absent. My RURO framework fills both gaps.
