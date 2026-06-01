---
title: "The Quantity and Quality of Life and the Evolution of World Inequality"
authors: [Gary S. Becker, Tomas J. Philipson, Rodrigo R. Soares]
year: 2005
outlet: "American Economic Review, 95(1), 277--291"
country_or_context: "Cross-country / global (96 countries)"
population: "Hypothetical life-cycle individuals for each country-year"
data_period: "1960--2000 (main); 1965--1995 (cause-of-death decomposition)"
shelf: "welfare measurement / health / longevity / world inequality / beyond GDP"
tags: [full-income, longevity, welfare-measurement, world-inequality, health-valuation, convergence, cross-country-comparison, cause-of-death-decomposition, Becker, Philipson, Soares]
priority: "low-medium"
read_status: "extracted"
---

# Full citation

Becker, G. S., Philipson, T. J., & Soares, R. R. (2005). The quantity and quality of life and the evolution of world inequality. *American Economic Review*, 95(1), 277--291.

# One-sentence contribution

Constructs a "full income" measure incorporating the monetary value of longevity gains alongside income growth, showing that cross-country welfare inequality fell substantially between 1960 and 2000 once health improvements are included, even though income inequality alone showed no such convergence.

# Why this paper matters

This paper is a clean example of welfare measurement beyond income, demonstrating how a non-income dimension (longevity) can be monetised using a utility-theoretic framework and incorporated into cross-country inequality comparisons. For my JMP, it provides a conceptual template: just as Becker et al. convert survival improvements into income-equivalent welfare units, my framework converts opportunity-set differences into equivalent income units via the RURO model.

# Core research question

How does the evolution of cross-country inequality change once welfare is measured by "full income" (income + monetised longevity gains) rather than by income alone?

# Economic setting and context

Cross-country comparison using 96 countries (82%+ of world population), 1960--2000. Representative-agent (hypothetical life-cycle individual) framework. Not about labour supply, taxes, or household decisions.

# Model / theoretical framework

**Lifetime welfare accounting:**
$$V(Y, S) = \max \int_0^\infty e^{-\rho t} S(t) u(c(t)) \, dt$$
subject to $Y = \int_0^\infty e^{-r t} S(t) c(t) \, dt$ (full annuity insurance).

Under the hypothetical life-cycle individual (HLCI) assumption (constant annual income = country's per capita income), simplifies to:
$$V(y, S) = u(y) A(S) \quad \text{where} \quad A(S) = \int_0^\infty e^{-rt} S(t) \, dt$$

**Monetary value of longevity gains:** Income compensation $W(S, S')$ solving:
$$V(Y' + W(S, S'), S) = V(Y', S')$$

**"Full income" growth:** Income growth rate augmented by the annual equivalent of longevity gains $w(S, S')$.

Calibration: $\varepsilon = 0.346$ (elasticity of utility from Becker et al.'s earlier work), $\gamma = 1.250$ (value of statistical life anchor), $r = 0.03$.

# Key objects

- **Full income growth:** Average 2.8%/year globally, of which ~1/4 from health.
- **Poorest 50% (1960):** 4.1%/year full income growth, 1.7 ppt from health.
- **Richest 50% (1960):** 2.6%/year full income growth, 0.4 ppt from health.
- **Convergence:** Cross-country inequality in full income fell substantially; income inequality alone did not.

# Data

Penn World Tables 6.1 (GDP per capita), World Bank WDI (life expectancy at birth), WHO Mortality Database (cause-specific mortality for 49 countries).

# Identification logic

Calibration-and-accounting, not causal identification. Cross-country variation in income and survival combined with calibrated utility model.

# Estimation / empirical strategy

1. Calibrate lifetime utility framework to convert survival improvements into yearly income equivalents.
2. Compute inequality statistics for income, life expectancy, and full income.
3. Decompose life expectancy changes by age group (0--19, 20--49, 50+) and 13 cause-of-death categories using counterfactual survival functions (49 countries, 1965--1995).

# Treatment of preferences

Homogeneous and calibrated. Common instantaneous utility function $u(c)$ with parameters from the value-of-life literature. No heterogeneous preferences across individuals or countries.

# Treatment of opportunities / constraints

No modelling of opportunities in the labour market sense. No feasible job sets, latent offers, hours restrictions, or demand-side constraints. The only "constraint" is the lifetime budget with full annuity insurance.

# Welfare / normative object

"Full income": income per year plus monetary equivalent of longevity gains. A welfare-accounting object, not a fairness-based criterion. No discussion of responsibility, compensation, or reference opportunity sets.

# Main findings

1. **Income inequality shows little convergence** (1960--2000), but **life expectancy inequality falls substantially**.

2. **Full income inequality is lower and falling:** Poorest countries gained most from health improvements. Health contributes disproportionately to welfare growth in poor countries.

3. **Health-driven convergence concentrated pre-1990:** After 1990, AIDS in Africa partially reverses convergence.

4. **Cause-of-death decomposition:** Reductions in infectious diseases, respiratory/digestive diseases, and perinatal conditions (especially mortality before age 20) drive convergence. Mortality declines after age 50 from nervous-system and circulatory diseases contributed to increased inequality (concentrated in rich countries).

# Main limitations

- Representative-agent (HLCI) construction: abstracts from within-country inequality and the joint distribution of income and mortality.
- Common calibrated utility function: no preference heterogeneity.
- No opportunity sets, no feasible job menus, no labour supply modelling.
- Decomposition by cause/age only, not by preferences, opportunities, or responsibility.

# Relevance for my JMP

## possible use as a welfare measurement template
The paper demonstrates how a non-income dimension can be monetised and inserted into a welfare measure using a utility-theoretic framework. My JMP does the analogous exercise for job opportunities: converting differences in the opportunity set $A_i$ into equivalent income units via the structural labour supply model.

## possible use for the beyond-GDP argument
The finding that welfare convergence is hidden when only income is measured motivates the broader case for multidimensional welfare measurement. In my framework, the opportunity dimension may similarly change conclusions about who is worst-off relative to income-only measures.

# Research questions this paper inspires

1. Can a job-opportunity-sensitive well-being measure be constructed analogously to "full income," where the value of expanded feasible job sets is expressed in income-equivalent units?

2. How sensitive are welfare-convergence conclusions to the choice of common utility function when the additional dimension is opportunity rather than health?

# Challenge to this paper

The welfare metric abstracts from heterogeneous preferences and within-country inequality, using a common calibrated utility function applied to representative agents. This makes cross-country comparison tractable but misses the individual-level variation that drives both the equivalent income approach (Bargain et al. 2013) and the RURO framework. In my framework, welfare depends on individual-level preferences $R_i$, individual-level opportunity sets $A_i$, and the full within-country distribution -- objects that the representative-agent approach cannot capture.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper constructs a welfare measure that depends on income and a non-income dimension (survival), and converts the non-income dimension into income-equivalent units. It belongs to the family of "beyond income" welfare measurement papers.

[Reasonable inference for my project] The closest conceptual link is architectural: defining a welfare object that depends on more than current income and using utility theory to price additional dimensions. In my framework, the additional dimension is the opportunity set $A_i$ rather than the survival schedule $S$.

[Unclear from paper] No mapping into $W(z, R, A; y)$. The paper does not model $R$ heterogeneously, has no feasible set $A$, and does not analyse a pay schedule $y$.

# Relation to Bargain et al. (2013)

Not directly related. Both measure welfare beyond income, but Bargain et al. use individual-level structural estimation with heterogeneous preferences and equivalent income, while Becker et al. use calibrated representative-agent utility with homogeneous preferences and "full income."

# Relation to opportunities vs preferences

Orthogonal to this distinction. Preferences are common and calibrated; opportunities are not modelled as feasible sets. Welfare differences arise from country-level income paths and survival schedules, not from job opportunities or preference heterogeneity.

# Useful quotations / formulas

**Core valuation equation:**
$$V(Y' + W(S, S'), S) = V(Y', S')$$

**Simplified welfare under HLCI:**
$$V(y, S) = u(y) A(S), \quad A(S) = \int_0^\infty e^{-rt} S(t) \, dt$$

**Key empirical result (Table 2):** For poorest 50% of countries (1960), yearly full-income growth = 4.1%, with 1.7 ppt from health; for richest 50%, 2.6%, with 0.4 ppt from health.

# Suggested tags

full-income, longevity, welfare-measurement, world-inequality, health-valuation, convergence, cross-country-comparison, cause-of-death-decomposition, Becker, Philipson, Soares, representative-agent, calibration

# My quick takeaway

A clean example of welfare measurement beyond income, showing that longevity gains substantially reduce cross-country inequality relative to income-only measures. For my JMP, the conceptual template is relevant: just as this paper monetises survival improvements, my framework monetises opportunity-set differences via equivalent income. The limitations are equally clear: no preference heterogeneity, no individual-level analysis, no opportunity sets in the labour market sense.
