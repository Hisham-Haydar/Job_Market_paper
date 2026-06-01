---
title: "Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US"
authors: [Olivier Bargain, Andre Decoster, Mathias Dolls, Dirk Neumann, Andreas Peichl, Sebastian Siegloch]
year: 2013
outlet: "Social Choice and Welfare, 41(4), 789--817"
country_or_context: "12 countries: AT, BE, DK, FI, FR, DE, IE, NL, PT, SW, UK, US"
population: "Married/cohabiting women"
data_period: "~2001 (country-specific, harmonized)"
shelf: "welfare measurement / preference heterogeneity / interpersonal comparison"
tags: [welfare-metrics, Fleurbaey, preference-heterogeneity, money-metric, equivalent-income, compensation, liberal-reward, MRS, cross-country, discrete-choice, Box-Cox, EUROMOD, TAXSIM, beyond-GDP]
priority: "high"
read_status: "extracted"
---

# Full citation

Bargain, O., Decoster, A., Dolls, M., Neumann, D., Peichl, A., & Siegloch, S. (2013). Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US. *Social Choice and Welfare*, 41(4), 789--817.

# One-sentence contribution

Implements three Fleurbaey-inspired welfare metrics -- "wage", "rent + reference wage", and "rent" -- that differ in how they treat heterogeneous consumption-leisure preferences, and shows empirically that cross-country welfare rankings of 12 European countries and the US change dramatically depending on which metric is used, with the differences driven primarily by country-specific preference parameters rather than demographic composition.

# Why this paper matters

Standard income-based cross-country welfare comparisons ignore leisure and treat all individuals as having identical preferences. This paper operationalizes the Fleurbaey (2006, 2008) framework of responsibility-sensitive welfare measurement using structurally estimated labour supply models, demonstrating that the normative choice of how much responsibility to assign for work preferences has large quantitative consequences for international rankings. It bridges the gap between theoretical welfare economics and applied microsimulation by showing that preference heterogeneity is not a second-order concern but a first-order determinant of welfare rankings.

# Core research question

How do cross-country welfare rankings change when we move beyond income to include leisure, and when we use welfare metrics that treat heterogeneous consumption-leisure preferences differently -- specifically, metrics ranging from full compensation for preference differences ("rent") to full responsibility for preferences ("wage")?

# Economic setting and context

Twelve countries (~2001 data): Austria, Belgium, Denmark, Finland, France, Germany, Ireland, Netherlands, Portugal, Sweden, UK, US. Married women's labour supply is modeled; male hours treated as fixed. Tax-benefit systems simulated via EUROMOD (European countries) and TAXSIM (US). Countries span a wide range of female labour force participation rates and tax-benefit generosity.

# Model / theoretical framework

**Welfare metrics from Fleurbaey (2006, 2008):**

All three metrics are based on indifference curves in $(c, h)$ space and satisfy the compensation principle (individuals with identical preferences who face different budget constraints are ranked by their actual utility). They differ in how they handle preference heterogeneity:

1. **"Wage" metric** $v_i^W$: The minimum wage $\tilde{w}_i$ at which individual $i$, with zero non-labour income, would reach utility level $u$. Formally:
$$v_i^W(u, \mu^r = 0) = \min[\tilde{w}_i \mid v_i(\tilde{w}_i, \mu^r = 0) \geq u]$$
This metric assigns **maximal responsibility** for preferences: a work-averse person needs a higher wage equivalent to reach the same utility, so is ranked lower. Favours the industrious.

2. **"Rent + reference wage" metric** $v_i^{RW}$: The expenditure function at a reference wage $w^r$:
$$v_i^{RW}(u, w^r) = e_i(u, w^r) = \min[c_i - w^r h_i \mid u_i(c_i, h_i) \geq u]$$
Intermediate between "rent" and "wage". The reference wage $w^r$ is set at selected percentiles (p25, p50, p75) of the pooled wage distribution. As $w^r \to 0$, this converges to "rent"; as $w^r \to \infty$, it converges to "wage".

3. **"Rent" metric** $v_i^R$: The consumption level needed at zero hours to reach utility $u$:
$$v_i^R(u, h^r = 0) = c_i(u, 0) = \min[c_i \mid u_i(c_i, 0) \geq u]$$
This metric assigns **minimal responsibility** for preferences: it compensates for work aversion. Favours the work-averse.

**Labour supply model:** Discrete-choice (van Soest 1995 style) with 7 hours categories (0, 5, 10, 20, 30, 40, 50 hours/week). Box-Cox utility:
$$u_i(c, T - h) = \beta_c \frac{c^{\alpha_c} - 1}{\alpha_c} + \beta_{li} \frac{(T - h)^{\alpha_l} - 1}{\alpha_l}$$
with $\beta_{li} = \beta_{l0} + \beta_{lz} z_i$ (taste-shifters for demographics: age, education, children) and EV-I random term.

**Framework:** Normative (interpersonal welfare comparison), not social evaluation (no SWF aggregation).

# Key objects

- **MRS (marginal rate of substitution):** Ratio of marginal utility of leisure to marginal utility of consumption, $MRS = \frac{\beta_{li}(T-h)^{\alpha_l - 1}}{\beta_c c^{\alpha_c - 1}}$. Evaluated at a common bundle $(\bar{c}, \bar{h})$ for cross-country comparability. Ranges from 3.7 PPP-USD/h (Portugal) to 17.6 (Ireland) across countries (Table 2).
- **Rank correlation between metrics:** Spearman correlation between "rent" and "wage" rankings. Drops from 1.00 (identical preferences) to 0.59 (full heterogeneity, Table 5 last row).
- **Average percentile position:** Mean position of a country's households in the pooled 12-country distribution under each metric (Table 3).

# Data

Harmonized household micro-data for 12 countries: EU-SILC, ECHP, GSOEP, IPUMS CPS, etc. Tax-benefit rules simulated via EUROMOD v.D16 and TAXSIM v.9. Wages in 2001 PPP-USD. Married women with working-age partners; wage imputation for non-workers via Heckman selection model.

# Identification logic

Preference parameters ($\alpha_c, \alpha_l, \beta_c, \beta_{l0}, \beta_{lz}$) are identified from observed labour supply choices under known budget constraints (tax-benefit schedules). Country-specific estimation allows preferences to vary across countries. Welfare metrics are computed from estimated indifference curves -- no additional identification assumptions beyond the labour supply model.

# Estimation / empirical strategy

1. Estimate country-specific discrete-choice labour supply models (Box-Cox utility, 7 hours categories, conditional logit).
2. Compute welfare metrics for each household using estimated indifference curves and EV-I taste draws (expected value over draws).
3. Pool all households across 12 countries into a single distribution; compute each household's percentile position under each metric.
4. Compare country-level average percentile positions and rankings across metrics.
5. Decomposition (Section 5.3): Isolate sources of ranking differences by counterfactually varying (a) only demographic composition, (b) only country-specific preference parameters, holding the other fixed.

# Treatment of preferences

Preferences are the paper's central focus. They are **heterogeneous** along two dimensions:
- **Observed heterogeneity:** Taste-shifters $z_i$ (age, education, number/age of children) enter through $\beta_{li}$
- **Country-specific parameters:** $\alpha_c, \alpha_l, \beta_c, \beta_{l0}$ estimated separately for each country, allowing systematic cross-country taste differences

The paper does **not** take a stand on which metric is "correct" but shows that the normative choice matters quantitatively. The three metrics embody different positions on the compensation-vs-responsibility spectrum.

# Treatment of opportunities / constraints

Opportunities enter only through the budget constraint (tax-benefit schedule) and wage rate. There is **no explicit modelling of job availability or rationing** -- the paper uses a standard van Soest discrete-choice model without job dummies, peaks dummies, or opportunity densities. The paper acknowledges this limitation: "demand-side constraints which restrict the choice set available to the individual (Dagsvik 1994; Aaberge et al. 1999; Dagsvik and Strom 2006) ... could also result in involuntary unemployment (Peichl and Siegloch 2012). Here, a specific and additionally demanding requirement in the present context would have been to determine country-specific choice opportunities" (p. 815).

# Welfare / normative object

The paper computes **individual-level welfare metrics** (not social welfare functions). The three metrics are all ordinal, satisfy the compensation principle, but differ in their treatment of the "liberal reward" principle. No aggregation into a SWF is performed -- the paper explicitly notes that aggregation requires additional choices (footnote 22 discusses leximin aggregation and the "indexing dilemma" from Fleurbaey 2007).

The paper is entirely about **interpersonal comparisons**, not **social evaluation**.

# Main findings

**Cross-country welfare rankings (Table 3):**
- Income rankings: US (63.3), IE (53.1), NL (47.6), UK (45.0), AT (43.6), DK (47.2), BE (49.2), DE (36.3), FR (34.4), SW (38.1), FI (29.7), PT (19.1)
- "Rent" rankings shift substantially: US drops from 63.3 to 62.4, IE rises from 53.1 to 55.5, FI drops from 29.7 to 24.1
- "Wage" rankings: US drops to 60.9, IE rises to 58.2, DK drops from 47.2 to 41.5
- For 7 of 12 countries, the difference between "rent" and "wage" average percentile exceeds 3 percentage points

**MRS heterogeneity (Table 2):**
- MRS at common bundle varies from 3.7 (PT) to 17.6 (IE) PPP-USD/hour
- Countries with high MRS (IE, US, DK) are "work-loving"; low MRS (PT, FI) are relatively "work-averse"
- This drives the metric-dependent rankings: "work-loving" countries gain under "wage", lose under "rent"

**Decomposition (Tables 5--6):**
- With identical preferences across countries, all metrics produce nearly identical rankings (rank correlation 0.98--1.00)
- Country-specific preference parameters are the **primary driver** of ranking differences (Table 6b reproduces Table 3 patterns closely)
- Demographic composition has **negligible effect** on ranking differences (Table 6a shows minimal variation across metrics)
- Children and country-specific preferences interact most strongly (rank correlation drops to 0.60 in Table 5)

**Income-poor analysis (Table 4):**
- For households in the bottom income quintile, the metric choice matters even more
- Portuguese poor are at ~10th percentile under all metrics; Irish poor rise from ~30th (income) to ~50th ("rent")
- Metric-dependent rankings for the poor sometimes reverse relative to the average

**Robustness (Section 5.4):**
- Box-Cox vs. quadratic utility: very similar MRS (Table 2)
- Alternative computation methods for metrics (averaging metric values vs. weighted by choice probabilities): orderings unaffected
- Alternative reference households (p10, p50, p90 of MRS): core results unchanged -- country-specific preferences dominate

# Main limitations

- No demand-side constraints or job availability modelling -- ignores involuntary unemployment and rationing
- Only married women; no singles, no male labour supply modelling
- No fixed costs of work -- paper acknowledges this could reduce apparent MRS differences (p. 814--815)
- No in-kind benefits or public services in welfare metrics
- No SWF aggregation -- interpersonal comparisons only, leaving the "indexing dilemma" unresolved
- Cross-country preference differences could partly reflect institutional constraints (e.g., childcare availability) rather than "true" preferences
- Static model; no lifecycle or dynamic considerations

# Relevance for my JMP

## possible use for framing
The paper provides the leading empirical demonstration that preference heterogeneity matters for welfare rankings -- exactly the motivation for including $R$ as a primitive in $W(z, R, A; y)$. The finding that rankings change by 15+ percentile points depending on the metric directly motivates the need for a framework that makes the treatment of $R$ explicit and transparent.

## possible use for model design
The three Fleurbaey metrics map onto specific axiom choices in the $W(z, R, A; y)$ framework:
- "Rent" $\leftrightarrow$ Full Compensation axiom (compensate for all preference differences)
- "Wage" $\leftrightarrow$ liberal reward / Full Responsibility axiom (individuals bear consequences of their preferences)
- The paper shows these are not just theoretically distinct but empirically consequential

## possible use for identification
The decomposition in Section 5.3 (Table 5) provides a template for separating the effect of $R$ from demographics in welfare rankings. The coefficient of variation in MRS and rank correlations across metrics are practical tools for quantifying how much "preference heterogeneity" matters.

## possible use for decomposition
The paper's finding that country-specific $\alpha, \beta$ parameters (not demographics) drive ranking differences suggests that in my framework, the $R$ component captures deep preference differences that cannot be proxied by observable characteristics alone. This supports modelling $R$ as a latent object estimated from choices.

## possible use for comparative application
The 12-country implementation provides benchmarks for welfare metric values and MRS distributions that I can compare against RURO-based estimates. The finding that ignoring leisure/preferences gives misleading rankings strengthens the case for my comprehensive $W(z, R, A; y)$ approach.

# Research questions this paper inspires

1. How would the welfare rankings change if the opportunity set $A$ were explicitly modelled (via RURO opportunity densities) rather than absorbed into the budget constraint? Would the metric-dependence of rankings increase or decrease?

2. Can the "rent + reference wage" metric be reinterpreted as a specific parameterization of $W(z, R, A; y)$ where $A$ is held constant and $R$ is treated with partial responsibility?

3. The paper finds that country-specific preference parameters drive ranking differences. But are these "preference" parameters partly capturing country-specific opportunity constraints (e.g., part-time availability, childcare)? How would a RURO decomposition of preferences vs. opportunities change this conclusion?

4. What happens when a SWF is applied to these metrics? Do the ranking reversals amplify or dampen under different degrees of inequality aversion?

# Challenge to this paper

The paper's central finding -- that preference heterogeneity drives welfare ranking differences -- is conditional on the assumption that estimated labour supply parameters reflect "true" preferences. But in a model without demand-side constraints (no rationing, no fixed costs, no job availability heterogeneity), preference parameters absorb the effects of opportunity constraints. A country where women work less due to lack of childcare or part-time jobs (an $A$ problem) will appear to have "higher leisure preference" (an $R$ problem). The paper explicitly acknowledges this (p. 814--815) but does not address it empirically. In the $W(z, R, A; y)$ framework, this conflation means the paper cannot distinguish between the compensation principle (compensating for constrained opportunities) and the liberal reward principle (respecting genuine preferences) because the underlying model does not separate $R$ from $A$. A RURO-based implementation with explicit opportunity densities would provide a cleaner test of whether the metric-dependence of rankings reflects genuine preference differences or opportunity-constraint differences.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The three metrics correspond directly to different axiom sets in the $W(z, R, A; y)$ framework. "Rent" satisfies compensation (analogous to the Full Compensation axiom), while "wage" satisfies liberal reward (analogous to Full Responsibility). The paper states: "under criteria that tend to evaluate agents with a relatively higher willingness-to-work to be better off compared to agents with a lower willingness-to-work, households from apparently 'work-loving countries' (as Denmark and the US) rank higher on average" (p. 814).

[Reasonable inference for my project] The paper's welfare metrics implicitly hold $A$ constant (no opportunity modelling) and vary only how $R$ is treated. In the $W(z, R, A; y)$ framework, this corresponds to fixing the $A$ component and exploring different normative treatments of $R$. My framework extends this by also making $A$ explicit, which the paper identifies as a key limitation: "demand-side constraints which restrict the choice set available to the individual... could also result in involuntary unemployment" (p. 815).

[Unclear from paper] Whether the "rent + reference wage" metric has a natural analogue in the $W(z, R, A; y)$ framework -- specifically, whether the reference wage $w^r$ can be mapped to the pay schedule $y$ in my framework. Also unclear: how the three metrics would behave under RURO-estimated preferences where $R$ and $A$ are separately identified.

The paper is closest to: **normative treatment of preference heterogeneity $R$** and **empirical welfare measurement in $(c, h)$ space**.

# Relation to Bargain et al. (2013)

This *is* Bargain et al. (2013). Key connections to the broader Bargain corpus:
- **Bargain et al. (2010):** The rationing model provides the demand-side constraints that this paper lacks. Combining the two would allow welfare metrics that account for both preference heterogeneity ($R$) and opportunity constraints ($A$).
- **Bargain et al. (2014):** Extends this framework to inequality measurement with different degrees of inequality aversion, addressing the aggregation step this paper deliberately avoids.
- **Bargain & Peichl (2016):** The elasticity estimates from the discrete-choice models used here feed into the comparative elasticity analysis.

# Relation to opportunities vs preferences

The paper provides the strongest empirical evidence in this literature that **preferences matter for welfare rankings**, but it cannot distinguish preference effects from opportunity effects because the underlying model does not separately identify $R$ and $A$. This is the paper's central limitation from the perspective of the $W(z, R, A; y)$ framework. The decomposition (Table 5) shows that "country-specific preference parameters" drive 85%+ of the ranking variation, but these parameters may partly capture cross-country differences in opportunities (childcare, part-time availability, labour market institutions).

# Useful quotations / formulas

**On the normative stakes (p. 809):**
"households from apparently 'work-loving countries' (as Denmark and the US) are better off on average than households from apparently 'work-averse nations' (e.g., Austria and Ireland) under the 'rent' criterion."

**On metric interpretation (p. 809):**
"the reason is that with the 'rent' metric, the policy maker tends to evaluate an agent with a higher willingness-to-work to be better off compared to another agent with a lower willingness-to-work (assigning low responsibility for work aversion)."

**On the limitation of ignoring demand side (p. 815):**
"demand-side constraints which restrict the choice set available to the individual (Dagsvik 1994; Aaberge et al. 1999; Dagsvik and Strom 2006) ... could also result in involuntary unemployment (Peichl and Siegloch 2012). Here, a specific and additionally demanding requirement in the present context would have been to determine country-specific choice opportunities."

**Welfare metric formulas:**

"Wage" metric:
$$v_i^W(u, \mu^r = 0) = \min[\tilde{w}_i \mid v_i(\tilde{w}_i, \mu^r = 0) \geq u]$$

"Rent + reference wage" metric:
$$v_i^{RW}(u, w^r) = e_i(u, w^r) = \min[c_i - w^r h_i \mid u_i(c_i, h_i) \geq u]$$

"Rent" metric:
$$v_i^R(u, h^r = 0) = \min[c_i \mid u_i(c_i, 0) \geq u]$$

**Box-Cox utility:**
$$u_i(c, T - h) = \beta_c \frac{c^{\alpha_c} - 1}{\alpha_c} + \beta_{li} \frac{(T - h)^{\alpha_l} - 1}{\alpha_l}, \quad \beta_{li} = \beta_{l0} + \beta_{lz} z_i$$

# Suggested tags

welfare-metrics, Fleurbaey, preference-heterogeneity, money-metric, equivalent-income, compensation-principle, liberal-reward, MRS, cross-country, discrete-choice, Box-Cox, EUROMOD, TAXSIM, beyond-GDP, interpersonal-comparison, labour-supply

# My quick takeaway

This is the key empirical paper motivating the $R$ component of $W(z, R, A; y)$. It shows that how you treat preference heterogeneity changes welfare rankings by 15+ percentile points for most countries -- this is not a theoretical curiosity but a first-order empirical issue. The critical limitation for my JMP is that the paper cannot separate $R$ from $A$ because it uses a standard discrete-choice model without opportunity modelling. My RURO-based framework directly addresses this by separately identifying preferences and opportunities, which would allow a cleaner implementation of the Fleurbaey metrics where the normative treatment of $R$ is not contaminated by unmodelled opportunity constraints $A$.
