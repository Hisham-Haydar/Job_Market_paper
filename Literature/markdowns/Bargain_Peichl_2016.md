---
title: "Own-Wage Labor Supply Elasticities: Variation across Time and Estimation Methods"
authors: [Olivier Bargain, Andreas Peichl]
year: 2016
outlet: "IZA Journal of Labor Economics, 5:10"
country_or_context: "Western Europe and USA (meta-analysis)"
population: "Married women, single mothers, married men, childless singles"
data_period: "1967--2005 (surveyed studies)"
shelf: "labour supply elasticities / meta-analysis / survey"
tags: [elasticities, wage-elasticity, participation-elasticity, meta-analysis, time-trend, Hausman-model, discrete-choice, married-women, single-mothers, men, Europe, USA, survey]
priority: "medium"
read_status: "extracted"
---

# Full citation

Bargain, O., & Peichl, A. (2016). Own-Wage Labor Supply Elasticities: Variation across Time and Estimation Methods. *IZA Journal of Labor Economics*, 5:10.

# One-sentence contribution

Provides a comprehensive meta-analysis of 282 elasticity estimates from 92 studies across Western Europe and the USA, documenting a dramatic decline in married women's wage elasticities since the 1980s (from ~1.0 to ~0.2) driven primarily by time trends (rising female labour force attachment) rather than by differences in estimation methods (Hausman vs. discrete-choice).

# Why this paper matters

The huge variation in published labour supply elasticities has been a major source of confusion in optimal tax analysis. This paper disentangles two competing explanations for the variation -- changes over time (reflecting genuine preference/participation shifts) vs. estimation method artefacts (Hausman overestimation). The finding that time trends dominate has direct implications for calibrating optimal tax models: analysts should use elasticities from data collected close to the policy period, not rely on "canonical" estimates from older studies.

# Core research question

What are the relative contributions of (i) the time period of observation and (ii) the estimation method (Hausman continuous models vs. discrete-choice models vs. natural experiments) to the large variation in published labour supply elasticity estimates?

# Economic setting and context

The paper surveys studies spanning ~40 years (1967--2005 data periods) across 15+ Western European countries and the USA. The period covers the massive increase in female labour force participation (1970s--2000s), major tax-benefit reforms (EITC expansions, European welfare reforms), and the shift in estimation technology from Hausman continuous models to discrete-choice structural models.

# Model / theoretical framework

The paper is a **survey and meta-analysis**, not a new estimation. It reviews three main estimation approaches:

1. **Hausman continuous model (C):** Estimates a continuous labour supply function $h(w, y)$ via local linearization of the piecewise-linear budget constraint. Identification from cross-sectional wage/income variation. Subject to endogeneity bias, requires global Slutsky consistency, and handles non-convexities poorly.

2. **Discrete-choice model (D):** Random utility maximization over a finite set of hours alternatives (van Soest 1995). Identification from non-linearities in tax-benefit schedules. Handles non-convexities, fixed costs of work, and extensive margin naturally. Fewer behavioural restrictions needed.

3. **Natural experiments / reduced form:** DiD, RD, or IV designs exploiting policy reforms (e.g., EITC expansions). Credible identification but limited to specific populations affected by reforms; often report benefit/tax-rate elasticities rather than wage elasticities, making comparison difficult.

**Elasticity definitions:**
- Uncompensated (Marshallian) wage elasticity: $\epsilon^u = \frac{dh}{dw} \frac{w}{h}$
- Income elasticity: $\epsilon^Y = \frac{dh}{dy} \frac{y}{h}$
- Compensated (Hicksian): $\epsilon^c = \epsilon^u - \frac{wh}{y} \epsilon^Y$

# Key objects

- **282 elasticity estimates** from 92 studies: 156 for couples, 70 for singles, 56 income elasticities
- **Wage elasticity distributions by demographic group (Figure 1):**
  - Married women: mean 0.43, wide dispersion (0 to >1.5)
  - Men (married + single): mean 0.12, tight distribution (0 to 0.3)
  - Childless single women: mean 0.23, moderate dispersion
  - Single mothers: mean 0.59, very wide dispersion
- **Time-elasticity correlation (Figure 3):** Strong negative correlation between data year and elasticity estimate (~$-0.55$ for married women)

# Data

The paper itself collects no new data. It surveys published and working papers from 1981--2016 covering Western Europe (Austria, Belgium, Denmark, Finland, France, Germany, Ireland, Italy, Netherlands, Norway, Spain, Sweden, Switzerland, UK) and the USA. Tables 1--3 catalogue every study with: country, authors, data source, data year, model type, specification, tax-benefit treatment, and reported elasticities.

# Identification logic

Not applicable (survey/meta-analysis). For the meta-regression (Tables 4--5), the "identification" is from cross-study variation in data year, model type, and specification features. The paper acknowledges this is not causal identification (footnote 16: "like all meta-regressions, our analysis is not identifying causal effects").

# Estimation / empirical strategy

**Survey (Section 3):** Systematic cataloguing of 282 elasticity estimates across 92 studies, organized by demographic group (couples, singles) and country.

**Meta-regression (Section 4, Tables 4--5):** Regresses reported elasticity values on:
- Year of data collection (linear time trend)
- Discrete model dummy (D vs. C/H)
- Desired hours dummy
- Joint decision dummy
- Fixed costs dummy
- US dummy
- Constant

Key finding from meta-regression on married women (Table 4): Year coefficient $= -0.013^{***}$ (each additional year reduces elasticity by 0.013, or 0.31 over 24 years). Discrete model dummy is insignificant when year is included ($0.013$, s.e. $0.079$).

# Treatment of preferences

Preferences are not directly modelled in this paper. However, the declining elasticity trend is interpreted as reflecting genuine preference changes: "a more stable attachment of women to the labor market is responsible for modest participation responses to financial incentives in the recent period" (p. 2). This is consistent with a shift in women's consumption-leisure preferences toward higher labour supply. The paper also notes that childcare policies and domestic technology changes may play a role.

# Treatment of opportunities / constraints

The paper notes but does not model demand-side constraints. Key observation: "non-participation corresponds more often to demand-side constraints (rather than to voluntary choice) in [childless singles'] case" (p. 18), which explains why elasticity estimates for this group are imprecise. The paper also observes that "models estimated on observed work duration do underestimate potential labor supply responses" when demand-side constraints on hours exist (p. 23--24), citing this as a reason why desired-hours models produce higher elasticities.

# Welfare / normative object

No welfare analysis. The paper discusses implications for optimal tax design: "Diamond and Saez (2011) use an elasticity of 0.25 to derive an optimal top marginal tax rate of 72.7%. However, an elasticity of 0.6 reduces the optimal top marginal tax rate to 52.6%" (p. 24). The key normative implication is that the "right" elasticity for policy simulation depends critically on the data period and demographic group.

# Main findings

**Stylized facts from the survey:**
1. Married women have the largest and most dispersed elasticities (mean 0.43)
2. Men's elasticities are small, positive, and consistent across studies (mean 0.12); negative values found in older studies are not confirmed
3. Single mothers show high but declining elasticities, with the largest responses at the extensive margin
4. Childless singles are under-studied despite being a growing demographic
5. Income elasticities are generally small and often insignificant ($|\epsilon^Y| < 0.1$)

**Time trend (Figures 3--4, Tables 4--5):**
- Strong negative correlation between data year and elasticity ($r \approx -0.55$ for married women)
- Meta-regression: each year reduces married women's wage elasticity by $0.013$, totalling $0.31$ over 24 years ($p < 0.01$)
- Trend is similar for EU and US (Figure 3, right panel)
- Decline is steeper for participation elasticities than for hour elasticities
- Period dummies confirm: 1967--1984 elasticities are $0.497$ higher than 1996--2004 ($p < 0.001$); 1985--1995 are $0.145$ higher ($p = 0.053$)

**Estimation method (Tables 4--5):**
- Discrete model dummy is **insignificant** when year is included
- The apparent "Hausman overestimation" is explained by the fact that Hausman studies were conducted primarily on older data (1970s--1980s) when elasticities were genuinely higher
- Within the common support period (post-1985), both methods produce similar estimates

**Modelling features (Tables 4--5):**
- Desired hours: significant positive effect ($+0.185^{**}$) -- models using desired hours report higher elasticities, reflecting demand-side constraints on observed hours
- Joint decision, fixed costs, US dummy: insignificant

# Main limitations

- Meta-regression is not causal -- omitted study-level characteristics (sample selection, wage measure, etc.) may confound
- Limited common support between methods: few discrete-choice estimates before 1985, few Hausman estimates after 2000
- Cannot separate genuine preference changes from institutional changes (childcare, labour market regulations)
- Does not cover dynamic/lifecycle models or taxable income elasticities
- Survey may not be fully exhaustive -- some studies do not report comparable elasticities

# Relevance for my JMP

## possible use for framing
The paper's central finding -- that elasticities are not structural constants but vary systematically over time -- supports the $W(z, R, A; y)$ framework's treatment of preferences ($R$) as context-dependent. If "elasticities" capture both preference responses and opportunity-set effects, then changes in $A$ (childcare availability, labour market institutions) could explain part of the declining trend without requiring changes in underlying preferences $R$.

## possible use for model design
The finding that demand-side constraints inflate desired-hours elasticities relative to observed-hours elasticities (Table 4, desired hours coefficient) motivates the RURO approach: in a model with explicit opportunity densities, the "elasticity" would decompose into a preference component (response along indifference curves) and an opportunity component (shifts in available jobs), avoiding the conflation documented in this survey.

## possible use for identification
The survey provides benchmark elasticity values by country, demographic group, and time period that can be compared against RURO-based estimates. If RURO-based estimates differ systematically from standard discrete-choice estimates (because they separate preferences from opportunities), this would be informative about the role of $A$ in driving measured elasticities.

## possible use for comparative application
The finding that cross-country elasticity differences are small (confirmed by Bargain et al. 2014) but time-period differences are large suggests that for cross-country welfare comparisons, the time period of data is more important than the country. This has implications for the $W(z, R, A; y)$ framework's cross-country application.

# Research questions this paper inspires

1. How much of the declining elasticity trend is due to changes in preferences ($R$) vs. changes in opportunities ($A$)? A RURO model estimated on data from multiple time periods could decompose the trend into preference shifts and opportunity-density shifts.

2. The paper finds that desired-hours models yield higher elasticities than observed-hours models. In the RURO framework, this difference should be captured by the opportunity density $p(h,w)$. Can the RURO model reconcile the two types of estimates?

3. If elasticities are not structural constants, how should optimal tax models be calibrated? Should they use current-period estimates (which may change) or structural preference parameters (which require more assumptions)?

# Challenge to this paper

The paper's conclusion that "estimation method does not matter" (time trend dominates) is based on the limited common support between methods: few discrete-choice estimates exist before 1985, and few Hausman estimates after 2000. Within this narrow window, both methods may produce similar estimates because the data period effect swamps method differences. But the more fundamental concern is that neither method addresses demand-side constraints or opportunity heterogeneity: both Hausman and discrete-choice models treat labour supply as purely preference-driven. If the declining elasticity trend partly reflects changes in opportunity structures (more stable employment, less rationing) rather than preference changes, then both methods are equally biased -- they just happen to produce similar biased estimates for recent periods.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper notes that "a labor supply elasticity per se is not a deep structural parameter and depends on many factors including the country (wage distribution, institutions, labor market characteristics), the demographic group under investigating, and the time period" (p. 25--26). This supports treating $R$ and $A$ as separate primitives in $W(z, R, A; y)$ rather than relying on reduced-form elasticities.

[Reasonable inference for my project] The declining elasticity trend may reflect changes in both $R$ (women's preferences shifting toward more work) and $A$ (more part-time opportunities, better childcare). The $W(z, R, A; y)$ framework can separate these channels: $R$-driven changes affect the welfare metric directly, while $A$-driven changes affect the feasible set without necessarily changing well-being if preferences are unchanged.

[Unclear from paper] Whether the time trend in elasticities would persist in a RURO model that separates preferences from opportunities. If the opportunity density $p(h,w)$ has changed over time (more jobs available, different hours distributions), then RURO-based preference parameters might be more stable than reduced-form elasticities.

The paper is closest to: **empirical benchmarks for labour supply responsiveness** and **motivation for separating preferences from opportunities in structural models**.

# Relation to Bargain et al. (2013)

The elasticity estimates surveyed here are the behavioural foundation for the welfare metrics computed in Bargain et al. (2013). If elasticities have declined over time, then welfare metric calculations based on older preference estimates may be biased. The paper's finding that discrete-choice models (which Bargain et al. 2013 uses) produce reliable estimates in the recent period is reassuring, but the fundamental limitation remains: neither this survey nor Bargain et al. (2013) separates preference-driven from opportunity-driven labour supply responses.

# Relation to opportunities vs preferences

The paper implicitly demonstrates the impossibility of separating preferences from opportunities using reduced-form elasticities alone. The declining trend could reflect either: (a) women's leisure preferences have genuinely shifted, or (b) opportunity structures have changed (more jobs available, less rationing, better childcare). Standard models -- both Hausman and discrete-choice -- cannot distinguish these. Only a model with explicit opportunity densities (RURO) can decompose the trend into preference and opportunity components.

# Useful quotations / formulas

**On the declining trend (p. 2):**
"We highlight the key role of time changes, documenting the incredible fall in labor supply elasticities since the 1980s not only for the USA but also in the EU."

**On method vs. time (p. 22):**
"The main conclusion is that estimation periods ('year') turn out to play a significant role. An additional year decreases wage elasticities of married women by around .013, which amounts to a decrease of .31 over a period of 24 years. [...] In contrast, the estimation method is itself broadly insignificant."

**On elasticities not being structural (p. 25--26):**
"it should be emphasized that there is not one 'right' elasticity. A labor supply elasticity per se is not a deep structural parameter and depends on many factors including the country (wage distribution, institutions, labor market characteristics), the demographic group under investigating, and the time period, among others."

**Uncompensated wage elasticity:**
$$\epsilon^u = \frac{dh}{dw} \frac{w}{h}$$

**Meta-regression key result (Table 4):**
Year coefficient: $-0.013^{***}$ (s.e. $0.005$); Discrete model dummy: $0.013$ (s.e. $0.079$, insignificant)

# Suggested tags

elasticities, wage-elasticity, participation-elasticity, income-elasticity, meta-analysis, time-trend, shrinking-elasticities, Hausman-model, discrete-choice, married-women, single-mothers, men, childless-singles, Europe, USA, survey, optimal-taxation

# My quick takeaway

This survey establishes that the "right" elasticity depends more on when the data were collected than on how they were estimated. The $\sim 0.013$/year decline in married women's elasticities since the 1970s is large enough to change optimal tax rates by 20+ percentage points. For my JMP, the key implication is that reduced-form elasticities conflate $R$ and $A$ effects: if the declining trend partly reflects expanded opportunities rather than changed preferences, then welfare evaluations based on these elasticities may misattribute opportunity improvements to preference shifts. The RURO framework's explicit separation of $R$ and $A$ can address this by estimating stable preference parameters while allowing the opportunity density to evolve over time.
