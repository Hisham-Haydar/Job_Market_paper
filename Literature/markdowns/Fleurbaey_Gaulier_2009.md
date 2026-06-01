---
title: "International Comparisons of Living Standards by Equivalent Incomes"
authors: [Marc Fleurbaey, Guillaume Gaulier]
year: 2009
outlet: "Scandinavian Journal of Economics, 111(3), 597--624"
country_or_context: "24 OECD countries"
population: "Representative agents for 24 OECD countries"
data_period: "2004 (cross-section)"
shelf: "equivalent income / beyond GDP / international comparisons / welfare measurement / applied"
tags: [equivalent-income, money-metric-utility, beyond-GDP, international-comparisons, OECD, leisure, unemployment, health, household-size, inequality, Kolm-Atkinson, WTP, willingness-to-pay, Fleurbaey, CES-social-welfare, representative-agent]
priority: "medium"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Gaulier, G. (2009). International comparisons of living standards by equivalent incomes. *Scandinavian Journal of Economics*, 111(3), 597--624.

# One-sentence contribution

Proposes and applies a method for comparing living standards across 24 OECD countries using equivalent incomes -- GDP per capita corrected for non-income dimensions (leisure, unemployment risk, health, household size, inequality) via willingness-to-pay calculations -- showing that the resulting ranking differs substantially from both GDP and HDI rankings.

# Why this paper matters

This is the first major empirical application of the equivalent income approach to international comparisons, bridging Fleurbaey's theoretical work on fairness and money-metric utility with practical policy evaluation. It demonstrates that the equivalent income framework is operational and yields substantively different conclusions from GDP per capita. The paper also addresses key methodological questions: how to approximate equivalent incomes with aggregate data, how to choose reference values for non-income dimensions, and how sensitive rankings are to parameter choices.

# Core research question

How do international comparisons of living standards change when GDP per capita is corrected for differences in leisure, unemployment risk, health, household composition, and income inequality, using the equivalent income methodology?

# Economic setting and context

Cross-country comparison of 24 OECD countries in 2004. Data from OECD, World Bank, and various national sources. The approach uses a representative agent framework due to data limitations -- individual-level equivalent incomes are not computed. Living conditions are described by income $y_i$ and a vector of non-income dimensions $z_i$ (leisure, unemployment risk, health, household size). Equivalent income is the income that, combined with a reference level $z^*$ for non-income dimensions, would yield the same utility as the actual situation $(y_i, z_i)$.

# Model / theoretical framework

**Equivalent income definition:**
For individual $i$ with income $y_i$ and non-income conditions $z_i$, the equivalent income $y_i^*$ solves:
$$v_i(y_i^*, z^*) = v_i(y_i, z_i)$$
where $v_i$ is the indirect utility function and $z^*$ is a common reference vector for non-income dimensions.

**Social welfare function (CES):**
$$W(y_1^*, \ldots, y_n^*) = \left[\frac{1}{n}\sum_{i=1}^n (y_i^*)^{1-\nu}\right]^{\frac{1}{1-\nu}}$$
where $\nu$ is the coefficient of inequality aversion. This can be decomposed as:
$$W = \left(\frac{1}{n}\sum y_i^*\right)(1 - I(y_1^*, \ldots, y_n^*))$$
where $I$ is the Kolm-Atkinson inequality index.

**Approximation via WTP:** Due to data limitations (no individual-level data), the paper approximates average equivalent income using willingness-to-pay (WTP) corrections:
$$\frac{1}{n}\sum y_i^* \approx \frac{1}{n}\sum y_i - \frac{1}{n}\sum \delta_i$$
where $\delta_i \approx \sum_k \gamma_{ik}(z_k^* - z_{ik})$ is individual $i$'s WTP for moving from actual $z_i$ to reference $z^*$, and $\gamma_{ik}$ is the marginal WTP for dimension $k$.

**Representative agent utility:**
$$E\sum_{t=0}^T \beta^t[u(c(t)) - a(\ell(t))]$$
with CRRA utility $v(y) = \frac{1}{1-\varepsilon}y^{1-\varepsilon} + u_0$ where $u_0 < 0$ ensures subsistence level.

**Corrections computed:**
1. **GNI vs GDP:** Replace GDP with GNI per capita (net international income flows).
2. **Leisure:** WTP for difference between actual hours $\ell$ and reference $\ell^*$ (median): $\delta_\ell \approx w(\ell^* - \ell)$ (pricing method using net wage).
3. **Unemployment:** Risk premium from unemployment probability $p$, exit probability $q$, replacement rate $\tau$, and stigma: $\delta_U \approx -\xi(\hat{\tau} - \tau)y - \frac{1}{2}\xi(1-\xi)\varepsilon(1-\tau)^2 y$.
4. **Health:** WTP for life expectancy difference via utility integral over different lifespan $T$ vs $T^*$.
5. **Household size:** Equivalence scale correction $y/h^\eta$ where $\eta = 0.5$ (OECD scale), with reference = single person.
6. **Inequality:** Kolm-Atkinson deduction with $\nu = 1.5$.

# Key objects

- **Equivalent income $y_i^*$:** Income at reference non-income conditions that yields same utility as actual situation.
- **Reference vector $z^*$:** Median values across the 24-country sample for leisure, health, household size; reference unemployment = 0.
- **WTP corrections $\delta_k$:** Monetary value of deviations from reference in each non-income dimension.
- **Inequality deduction:** $I(y_1^*, \ldots, y_n^*)$ using Kolm-Atkinson index with aversion $\nu = 1.5$.

# Data

OECD 2004 cross-section for 24 countries. GDP/GNI per capita (World Bank PPP USD), hours of work (OECD Labour Statistics), unemployment rates and duration (OECD), health-adjusted life expectancy (OECD Health Data 2005), household size (OECD, Euromonitor), income distribution (World Bank, Luxembourg Income Study). Parameters: discount factor $\rho = 0.03$, risk aversion $\varepsilon = 0.8$, utility elasticity from Becker et al. (2005) = 0.346, subsistence level ~1 USD/day, inequality aversion $\nu = 1.5$, household scale $\eta = 0.5$.

# Identification logic

Not structural identification in the econometric sense. The paper calibrates a representative agent model using external parameter estimates (from Becker et al. 2005, Murphy and Topel 2003, etc.) and computes corrections using marginal WTP formulas. The key identification assumption: marginal WTP (pricing method) is a valid approximation for the equivalent income corrections, which requires that the corrections are small relative to income.

# Estimation / empirical strategy

Calibration, not estimation. Parameters are borrowed from the literature. The corrections are computed using closed-form WTP formulas derived from the representative agent model. Sensitivity analysis varies key parameters (WTP for leisure, risk aversion, inequality aversion, household scale) across three alternative scenarios designed to favour Anglo-Saxon, Latin, and Nordic country groups respectively.

# Treatment of preferences

Preferences are assumed homogeneous across countries (same representative agent utility function). This is a major limitation acknowledged by the authors. The paper explicitly notes that "one needs survey data on income and on the additional dimensions of consumption [...] as well as on preferences (WTP)" (p. 620-621) for a more accurate implementation. Within the model, preferences are separable between consumption and labour, with CRRA consumption utility and additive labour disutility.

# Treatment of opportunities / constraints

No explicit treatment. The paper takes observed outcomes (hours, unemployment, health, income) as given and computes WTP corrections. There is no modelling of choice sets, job availability, or demand-side constraints. The unemployment correction treats unemployment as a risk (probability of falling into unemployment) rather than as a constraint on the choice set. The leisure correction uses the pricing method (marginal WTP = net wage), which is valid only when agents freely choose hours at their wage -- an assumption that fails under hours constraints or involuntary unemployment.

# Welfare / normative object

Social welfare = CES function of equivalent incomes with inequality aversion $\nu = 1.5$. This is a representative-agent approximation to individual-level equivalent income aggregation. The Kolm-Atkinson inequality deduction captures within-country inequality in ordinary incomes (not equivalent incomes, due to data limitations).

# Main findings

1. **Rankings differ substantially from GDP** (Table 1): Norway moves from rank 3 (GDP) to rank 1 (equivalent income). France moves from rank 12 to rank 6. Japan moves from rank 10 to rank 3. The US drops from rank 2 to rank 4. Ireland remains rank 2-3.

2. **Leisure correction is large and positive for European countries:** France gains +2,386 USD (high leisure), while the US loses -2,515 USD (low leisure) and Japan loses -2,039 USD. (Table 4)

3. **Unemployment correction is non-negligible:** France loses -602 USD, Spain -497 USD, Greece -696 USD. Anglo-Saxon countries also lose (US -432 USD). (Table 4)

4. **Health correction is largest for Japan:** +19,155 USD. The US loses -2,306 USD. France gains +15,498 USD. (Table 4)

5. **Household size correction is very large:** Ireland +25,347 USD, Luxembourg +30,775 USD, reflecting large household sizes relative to the single-person reference. (Table 4)

6. **Inequality deduction is substantial:** US loses -12,318 USD (high inequality), while Nordic countries lose less (-4,837 to -6,181 USD). (Table 4)

7. **Three welfare patterns identified:**
   - **Anglo-Saxon** (US, UK, Canada, Australia, NZ): High inequality, high working time, low unemployment cost.
   - **Latin** (France, Italy, Spain): High unemployment cost, high leisure, high life expectancy.
   - **Nordic** (Norway, Sweden, Denmark, Iceland): Low inequality, low unemployment, moderate leisure.

8. **Sensitivity analysis** (Table A1): Rankings are sensitive to parameter choices, but some features are robust: the US always loses at least 7 points relative to GDP, Japan always gains at least 14 points, France always gains at least 9 points.

# Main limitations

- Representative agent approach: individual-level equivalent incomes are not computed.
- Homogeneous preferences across countries: all countries assumed to have the same utility function.
- The pricing method (marginal WTP) is only valid for small corrections; for large corrections (e.g., household size), it is an approximation.
- Within-country inequality is measured on ordinary incomes, not equivalent incomes.
- No structural modelling of labour supply, unemployment, or health production.
- The leisure correction assumes free choice of hours at the market wage, ignoring hours constraints and involuntary unemployment.
- Data from various sources with varying quality and comparability.

# Relevance for my JMP

## possible use as an empirical template for equivalent income computation
The paper provides a practical methodology for computing equivalent incomes at the aggregate level, including the WTP approximation, the choice of reference values, and the Kolm-Atkinson inequality deduction. While my JMP works at the individual level with structural labour supply models, this paper's approach to decomposing welfare into income and non-income corrections, and its sensitivity analysis framework, are useful templates.

## possible use for the leisure correction methodology
The leisure correction using the pricing method ($\delta_\ell \approx w(\ell^* - \ell)$) is the simplest version of the equivalent income correction for hours of work. My RURO framework provides a richer version that accounts for demand-side constraints (agents may not be able to freely choose hours). Comparing the simple pricing-method correction with the RURO-based correction would quantify the welfare cost of ignoring opportunity constraints.

## possible use for demonstrating the importance of non-income dimensions
The paper's finding that non-income corrections substantially change country rankings motivates the broader equivalent income approach. For my JMP, this shows that welfare evaluation based on income alone is inadequate -- the non-income dimensions (hours, job availability, working conditions) captured by the RURO opportunity density matter for welfare.

# Research questions this paper inspires

1. How would the leisure correction change if computed with a RURO model (accounting for involuntary unemployment and hours constraints) instead of the pricing method (assuming free choice at the market wage)? Countries with tight labour markets (low unemployment, flexible hours) would see little change, while countries with rationed labour markets would see larger corrections.

2. The paper uses a representative agent. How would individual-level equivalent income computation (as in Bargain et al. 2013) change the cross-country rankings, especially when within-country heterogeneity in preferences and opportunities is accounted for?

# Challenge to this paper

The leisure correction uses the pricing method, which assumes that the net wage equals the marginal rate of substitution between leisure and consumption. This is valid only at an interior optimum with free choice of hours. For agents who are constrained (involuntarily unemployed, working more or fewer hours than desired), the marginal WTP for leisure differs from the net wage. The RURO framework, where the opportunity density $g(h, w)$ restricts the feasible set, would generate a different leisure correction that accounts for the gap between desired and actual hours. In countries with rigid labour markets (France, Spain), this gap is likely large, and the pricing method may substantially overstate or understate the leisure correction.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The equivalent income $y_i^*$ is defined as $v_i(y_i^*, z^*) = v_i(y_i, z_i)$, which corresponds to $m_i(\tilde{w}, z_i)$ in my framework with $z^*$ playing the role of the reference conditions (including reference wage $\tilde{w}$). The paper's WTP corrections correspond to the "distance" between actual and reference conditions measured in income units.

[Reasonable inference for my project] The paper's finding that leisure and unemployment corrections are large and vary substantially across countries suggests that the opportunity dimension (captured by my $A_i$ / $g(h,w)$) is quantitatively important for welfare comparisons. A RURO-based equivalent income that accounts for demand-side constraints in the labour market would provide a more accurate correction.

[Unclear from paper] How to extend the representative-agent framework to account for individual-level heterogeneity in both preferences and opportunity sets, as required by the RURO model.

# Relation to Bargain et al. (2013)

Direct precursor. Both papers compute equivalent incomes incorporating non-income dimensions. Bargain et al. (2013) advance the methodology by: (1) using individual-level data rather than representative agents, (2) estimating preferences from structural labour supply models rather than calibrating, (3) computing equivalent incomes at the individual level and aggregating, (4) focusing on within-country inequality rather than cross-country comparisons. This paper provides the cross-country perspective that complements Bargain et al.'s within-country analysis.

# Relation to opportunities vs preferences

The paper does not distinguish between preferences and opportunities. The leisure correction treats hours of work as a choice variable (pricing method using the wage), implicitly assuming that differences in hours across countries reflect preference differences rather than opportunity differences (labour market institutions, hours constraints, unemployment). From the RURO perspective, a country where agents work long hours because they lack access to part-time jobs is treated the same as a country where agents freely choose long hours. The equivalent income correction should differ in these two cases.

# Useful quotations / formulas

**On the equivalent income concept (p. 598):**
"We fix a reference level for this dimension and, for each country, compute the willingness to pay (WTP) of the population in order to obtain this reference level. Correcting current income by this amount, we obtain 'equivalent income'."

**On the advantage over composite indices (p. 620):**
"An approach of this kind is superior to composite social indicators, such as the HDI, because it is grounded in economic theory and in particular is meant to take account of the population preferences about the various dimensions of life."

**On the full-income critique (p. 604):**
"The full-income measure characteristically fails to satisfy this requirement. When two individuals have identical preferences but different wage rates, the one with the greater full income may well be on the lower indifference curve."

**On data needs (p. 620-621):**
"For an accurate application of this methodology, one needs survey data on income and on the additional dimensions of consumption [...] at the individual level, for all the countries studied. WTP data can be collected using contingent valuation questionnaires or indirect methods based on revealed preferences or on satisfaction surveys."

**Social welfare decomposition (eq. 7-8, p. 606):**
$$W(y_1^*, \ldots, y_n^*) = \left(\frac{1}{n}\sum y_i^*\right)(1 - I(y_1^*, \ldots, y_n^*))$$
$$W \approx \left(\frac{1}{n}\sum y_i\right)(1 - I(y_1, \ldots, y_n)) - \frac{1}{n}\sum \delta_i$$

# Suggested tags

equivalent-income, money-metric-utility, beyond-GDP, international-comparisons, OECD, leisure, unemployment, health, household-size, inequality, Kolm-Atkinson, WTP, willingness-to-pay, Fleurbaey, Gaulier, CES-social-welfare, representative-agent, pricing-method

# My quick takeaway

A pioneering empirical application of the equivalent income framework to cross-country welfare comparisons, showing that GDP rankings change substantially when corrected for leisure, unemployment, health, household size, and inequality. The paper demonstrates that the equivalent income approach is operational with aggregate data, but at the cost of using a representative agent and the pricing method for corrections. For my JMP, this motivates the RURO-based equivalent income approach: the leisure correction in this paper assumes free choice of hours, while my framework accounts for demand-side constraints. The paper's finding that corrections are large (10-30% of GDP) suggests that the opportunity dimension is quantitatively important.
