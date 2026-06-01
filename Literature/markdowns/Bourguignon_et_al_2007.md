---
title: "Inequality of Opportunity in Brazil"
authors: [François Bourguignon, Francisco H. G. Ferreira, Marta Menéndez]
year: 2007
outlet: "Review of Income and Wealth, 53(4)"
country_or_context: "Urban Brazil"
population: "Active urban males aged 26--60 with positive earnings"
data_period: "1996 cross-section (PNAD 1996), seven 5-year birth cohorts"
shelf: "inequality of opportunity / decomposition / circumstances vs effort / Brazil"
tags: [inequality-of-opportunity, Roemer, Brazil, earnings-inequality, circumstances-effort, decomposition, Theil-index, parental-background, direct-indirect-effects, partial-identification, Bourguignon, Ferreira, Menendez]
priority: "medium"
read_status: "extracted"
---

# Full citation

Bourguignon, F., Ferreira, F. H. G., & Menéndez, M. (2007). Inequality of opportunity in Brazil. *Review of Income and Wealth*, 53(4).

# One-sentence contribution

Proposes an empirical measure of the share of earnings inequality attributable to observed circumstances (family background, race, region of birth), finding that these account for 10--37% of the Theil index of male earnings inequality in urban Brazil, with roughly 60% of the effect operating directly on wages rather than indirectly through schooling and labour-market status.

# Why this paper matters

This is one of the clearest empirical implementations of Roemer's circumstance/effort distinction applied to earnings inequality. For my JMP, it provides (i) a template for how normative decomposition can be taken to the data, and (ii) a benchmark for what circumstance-based methods can and cannot capture -- specifically, they cannot separate preferences from opportunities as structural objects.

# Core research question

How much of observed male earnings inequality in urban Brazil can be attributed to unequal opportunities (exogenous circumstances) versus "effort," and how much of the circumstance effect operates directly on earnings versus indirectly through observed effort proxies?

# Model / theoretical framework

**Empirical decomposition model** motivated by Roemer's equality-of-opportunity framework. Earnings function:
$$w_i = f(C_i, E(C_i, v_i), u_i)$$
where $C_i$ = circumstance variables (race, region of birth, parental education, father's occupation), $E_i$ = effort variables (own schooling, migration, labour-market status) that may themselves depend on circumstances, and $u_i$ = unobserved residual.

**Decomposition:** Overall opportunity share $\Theta_I = [I(F) - I(\Phi)] / I(F)$, where $I(F)$ = observed inequality and $I(\Phi)$ = inequality in counterfactual distribution with equalized circumstances. Direct-effect decomposition $\Theta_I^d = [I(F) - I(F^d)] / I(F)$ isolates the effect of circumstances on earnings conditional on observed efforts.

Not a structural choice model, not a labour-supply model, not a welfare model.

# Key objects

- Five observed circumstance variables: race, region of birth, mother's education, father's education, father's occupational status.
- Three observed "effort" variables: own schooling, migration dummy, labour-market status.
- Overall opportunity share: 10--37% of Theil across cohorts; central estimate ~23%.
- Direct effect: ~60% of total opportunity effect operates directly on wages, not through effort channels.
- Most important individual circumstance: parental education.

# Data

PNAD 1996 household survey (IBGE), urban areas. 28,474 occupied males aged 26--60. Seven 5-year birth cohorts (1936--40 through 1966--70). Dependent variable: real hourly earnings from all occupations.

# Identification logic

Not causal in the quasi-experimental sense. Partial identification via Monte Carlo bias simulation: randomly draws correlations between regressors and residuals, imposes positive semi-definiteness and sign restrictions, constructs 90% confidence intervals for unbiased coefficients. Results presented as intervals rather than point estimates. This bounded-inference approach is a major methodological strength.

# Estimation / empirical strategy

1. Log-linear earnings regressions: "full" equation (circumstances + efforts) and "reduced form" (circumstances only).
2. Counterfactual distribution simulation: equalize observed circumstances, compute inequality indices over counterfactual distributions.
3. Direct/indirect decomposition: compare full-equation counterfactual (direct effect only) with reduced-form counterfactual (total effect).
4. Robustness through bounded inference under omitted-variable bias.

# Treatment of preferences

Not modelled. No utility function, no heterogeneous tastes. "Effort" is not derived from choice theory; the authors place the term in quotation marks because effort proxies may also reflect luck or circumstance. The paper cannot separate circumstances from preferences.

# Treatment of opportunities / constraints

Opportunities defined as observed background circumstances (race, parental education, region of birth, father's occupation) that shape life chances -- NOT as explicit feasible job sets, latent offers, or demand-side constraints. No $A_i$ object. No modelling of hours restrictions, occupational menus, or personalised wage-offer distributions. This is the Roemer tradition's notion of opportunity, not the RURO tradition's.

# Welfare / normative object

Not a welfare measure. The object decomposed is current hourly earnings inequality (Theil index, secondarily Gini). Normative motivation is compensatory: inequalities due to circumstances beyond individual control are inequitable. No well-being measure combining bundles, preferences, feasible sets, and pay schedules.

# Main findings

1. Five observed circumstances account for 10--37% of Theil index across cohorts; simple average ~23%.
2. ~60% of the opportunity effect operates directly on wages conditional on observed effort, not through schooling/migration/labour-market-status channels.
3. Parental education is the most important individual circumstance variable.
4. Father's occupation second most important; race matters especially for younger cohorts.
5. Weak evidence that opportunity share declines for younger cohorts, but cohort vs time effects cannot be separated.

# Main limitations

- Opportunities measured through observed background variables, not actual feasible sets. Cannot tell how opportunity sets $A_i$ should be represented.
- Preferences absent: decomposition is between circumstances and a residual containing effort, luck, preference heterogeneity, and measurement error.
- Not point-identified causally; results are bounds under maintained assumptions.
- Outcome metric is current earnings among active men; excludes participation, household composition, non-labour income, broader well-being.

# Relevance for my JMP

## possible use for framing and decomposition logic
Very useful. Provides a concrete empirical example of Roemerian responsibility vs compensation decomposition. The direct/indirect architecture (how much of circumstance effect works through effort channels) is suggestive for richer decompositions in $W(z,R,A;y)$.

## possible use for positioning my structural approach
The paper's limitation -- that "opportunities" are only proxied by observable background characteristics rather than modelled as actual feasible sets -- is precisely the gap my RURO framework addresses.

## possible use for bounded inference
The Monte Carlo construction of admissible unbiased coefficient intervals is methodologically interesting for settings where clean instruments are unavailable.

# Research questions this paper inspires

1. How would the measured "opportunity share" of inequality change if opportunities were represented by estimated feasible job sets $A_i$ rather than by family-background circumstances?

2. Can a Roemer-style circumstance/effort distinction be integrated with a structural discrete-choice labour model to obtain both behavioural consistency and an ethically interpretable decomposition?

# Challenge to this paper

The ethical language is sharper than the empirical categories. Calling schooling, migration, and labour-market status "efforts" is analytically convenient but substantively questionable -- these are themselves shaped by social structure, institutions, and inherited constraints. The RURO framework can potentially capture demand-side constraints on job availability that this paper's circumstance partitions miss entirely: a worker with "good" circumstances but facing a depressed local labour market has worse opportunities than the decomposition recognises.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] Opportunities defined through exogenous circumstance variables; earnings function $w = f(C, E(C,v), u)$. No $W(z,R,A;y)$, no feasible set $A$, no preference object $R$, no pay schedule $y$.

[Reasonable inference for my project] Circumstances can be loosely interpreted as determinants of $A$ or $y$, but the paper does not formalise this mapping. My framework's explicit opportunity density $g(h,w)$ provides a richer representation.

[Unclear from paper] How to map circumstance variables into $A$-type feasible sets; whether the direct/indirect decomposition architecture translates to a $W(z,R,A;y)$ setting.

# Relation to Bargain et al. (2013)

Not directly related. Both concern inequality decomposition but from different angles: Bargain et al. use structural labour supply models and equivalent income; Bourguignon et al. use reduced-form circumstance partitions. The two approaches could complement each other.

# Relation to opportunities vs preferences

The paper is about circumstances vs effort, not about opportunities vs preferences in the structural labour economics sense. It does not model heterogeneous preferences and does not define opportunities as explicit individualised feasible sets. Its main lesson: empirical IOp work uses observed circumstances as proxies for unfair opportunity differences, which is informative but cruder than modelling opportunities as explicit sets $A_i$.

# Useful quotations / formulas

**Earnings function:**
$$w_i = f(C_i, E(C_i, v_i), u_i)$$

**Overall opportunity share:**
$$\Theta_I = \frac{I(F) - I(\Phi)}{I(F)}$$

**Direct-effect decomposition:**
$$\Theta_I^d = \frac{I(F) - I(F^d)}{I(F)}$$

**Key empirical result:** Five observed circumstances account for ~23% of Theil index; ~60% of effect is direct.

# Suggested tags

inequality-of-opportunity, Roemer, Brazil, earnings-inequality, circumstances-effort, parental-background, opportunity-decomposition, Theil-index, direct-indirect-effects, partial-identification, Bourguignon, Ferreira, Menendez

# My quick takeaway

A strong empirical implementation of Roemer's circumstance/effort decomposition applied to Brazilian earnings inequality. For my JMP, its main value is as a framing and decomposition template: it shows how normative language can be operationalised empirically while making the limitations of circumstance-based methods clear. My RURO framework advances this by modelling opportunities explicitly through $g(h,w)$, capturing demand-side constraints that circumstance partitions miss.
