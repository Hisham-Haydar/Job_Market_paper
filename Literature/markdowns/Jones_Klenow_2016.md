---
title: "Beyond GDP? Welfare across Countries and Time"
authors: [Charles I. Jones, Peter J. Klenow]
year: 2016
outlet: "American Economic Review, 106(9), 2426--2457"
country_or_context: "Cross-country (13 countries micro, 152 countries macro)"
population: "General population"
data_period: "1980s--2007 (household surveys vary by country)"
shelf: "welfare measurement / beyond GDP / consumption equivalent / inequality / leisure / mortality"
tags: [welfare-measurement, beyond-GDP, consumption-equivalent, inequality, leisure, mortality, life-expectancy, cross-country, expected-utility, veil-of-ignorance, equivalent-variation, decomposition, AER]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Jones, C. I., & Klenow, P. J. (2016). Beyond GDP? Welfare across Countries and Time. *American Economic Review*, 106(9), 2426--2457.

# One-sentence contribution

Proposes a consumption-equivalent welfare measure that incorporates consumption, leisure, inequality, and mortality into a single expected-utility framework, and shows that Western Europe is much closer to US welfare than income suggests (due to longer life, more leisure, and lower inequality), while developing countries are further behind than income alone indicates.

# Why this paper matters

This paper operationalises the "beyond GDP" agenda using standard expected-utility theory. Unlike the Fleurbaey equivalent-income approach (which uses individual preferences), Jones and Klenow use a common set of preferences (a fictitious "Rawls" behind a veil of ignorance) to compare welfare across countries. The key innovation is to compute a single consumption-equivalent scalar $\lambda_i$ that incorporates multiple non-income dimensions of well-being, making it directly comparable to GDP per capita. The paper demonstrates that non-income dimensions can change country rankings substantially.

# Core research question

By what factor $\lambda_i$ must we adjust US consumption to make a person behind a veil of ignorance indifferent between living in the US and country $i$, incorporating differences in consumption, leisure, inequality, and mortality?

# Economic setting and context

Cross-country comparison for 13 countries using detailed household surveys (micro data) and 152 countries using publicly available macro data (Penn World Tables, WHO mortality data, UNU-WIDER inequality data). Time period spans 1980s to mid-2000s.

# Model / theoretical framework

**Expected lifetime utility (eq. 1):**

$$U = E \sum_{a=1}^{100} \beta^a u(C_a, \ell_a) S(a)$$

where $C_a$ = annual consumption at age $a$, $\ell_a$ = leisure, $S(a)$ = survival probability to age $a$, $\beta$ = discount factor.

**Consumption-equivalent welfare $\lambda_i$ (eqs. 2--3):** $\lambda_i$ solves:

$$U_{us}(\lambda_i) = U_i(1)$$

where $U_i(\lambda)$ is expected utility in country $i$ with consumption scaled by $\lambda$ at each age.

**Benchmark flow utility (eq. 4):**

$$u(C, \ell) = \bar{u} + \log C + v(\ell)$$

where $v(\ell) = -\frac{\theta\epsilon}{1+\epsilon}(1-\ell)^{\frac{1+\epsilon}{\epsilon}}$ captures disutility of work, with $\epsilon$ = Frisch elasticity.

**Simplified decomposition (eq. 7, log case with $\beta=1$, $g=0$):**

$$\log \lambda_i^{simple} = \underbrace{\frac{e_i - e_{us}}{e_{us}}\left(\bar{u} + \log c_i + v(\ell_i) - \tfrac{1}{2}\sigma_i^2\right)}_{\text{Life expectancy}} + \underbrace{\log c_i - \log c_{us}}_{\text{Consumption}} + \underbrace{v(\ell_i) - v(\ell_{us})}_{\text{Leisure}} + \underbrace{-\tfrac{1}{2}(\sigma_i^2 - \sigma_{us}^2)}_{\text{Inequality}}$$

where $e_i = \sum_a S_i(a)$ is life expectancy, $c_i$ is mean consumption, $\sigma_i^2$ is variance of log consumption.

**Micro-data welfare (eq. 9, using individual-level data):**

$$U_i = \sum_{a=1}^{100} \beta^a S_a^i \sum_{j=1}^{N_a^i} \bar{\omega}_{ja}^i u(c_{ja}^i e^{ga}, \ell_{ja}^i)$$

**Full decomposition (eq. 19):** With micro data and additively separable log utility:

$$\log \frac{\lambda_i}{\tilde{y}_i} = \sum_a \Delta s_a^i u_a^i \quad \text{(life expectancy)} + \log \frac{\bar{c}_i / y_i}{\bar{c}_{us}/y_{us}} \quad \text{(C/Y share)} + v(\bar{\ell}_i) - v(\bar{\ell}_{us}) \quad \text{(leisure)} + \text{cons. ineq.} + \text{leis. ineq.}$$

**Alternative utility (eq. 21, CRRA with non-separable leisure):**

$$u(C,\ell) = \bar{u} + \frac{(C+\underline{c})^{1-\gamma}}{1-\gamma}\left(1 + (\gamma-1)\frac{\theta\epsilon}{1+\epsilon}(1-\ell)^{\frac{1+\epsilon}{\epsilon}}\right)^\gamma - \frac{1}{1-\gamma}$$

# Key objects

- **$\lambda_i$:** Consumption-equivalent welfare -- proportion of US consumption needed to equate expected utility between the US and country $i$
- **Flow utility intercept $\bar{u}$:** Calibrated so the value of remaining life at age 40 equals \$6 million (2007 prices). $\bar{u} = 5.00$.
- **$\theta$:** Weight on leisure disutility, calibrated from the labor-leisure FOC: $\theta = 14.2$
- **$\epsilon$:** Frisch elasticity of labor supply = 1.0 (benchmark)
- **Decomposition components:** Life expectancy, consumption level, consumption share (C/Y), leisure, consumption inequality, leisure inequality

# Data

**Micro data:** Household surveys from 13 countries (US Consumer Expenditure Survey, French BDF, UK FES, Italian SHIW, etc. -- see Table 1). Variables: consumption (nondurables + services), hours worked, age. Merged with WHO mortality data by age.

**Macro data:** Penn World Tables 8.0 (consumption, income, hours for 52 countries), UNU-WIDER World Income Inequality Database (Gini coefficients for 68 developing + 49 rich countries), World Bank HNPStats (life expectancy for 152 countries).

**Calibration:** $\beta = 0.99$, $g = 0.02$, $\epsilon = 1.0$, $\bar{u} = 5.00$, $\theta = 14.2$. US benchmark: all measures normalised to 100.

# Identification logic

Not a causal identification strategy. The welfare measure is a calibrated accounting exercise: given observed data on consumption, leisure, inequality, and mortality, and given a specified utility function, what is the consumption-equivalent welfare? The main identification question is: how sensitive are the results to the utility specification? Robustness checks (Table 4) show the qualitative findings are stable across a wide range of parameter values.

# Estimation / empirical strategy

1. Collect micro data on consumption and hours by age for each country-year
2. Collect mortality data (survival probabilities by age) from WHO
3. Specify utility function and calibrate parameters ($\bar{u}, \theta, \epsilon, \beta, g$)
4. Compute expected lifetime utility $U_i$ for each country
5. Solve for $\lambda_i$ such that $U_{us}(\lambda_i) = U_i(1)$
6. Decompose $\log \lambda_i$ into life expectancy, consumption, leisure, and inequality components

# Treatment of preferences

**Common preferences.** All countries are evaluated using the same utility function (that of a fictitious "Rawls" behind a veil of ignorance). This is explicitly not the Fleurbaey equivalent-income approach, which respects individual preferences. The paper acknowledges this as a limitation: "We evaluate the allocations both within and across countries according to one set of preferences" (p. 2429). The common-preference assumption means that cross-country differences in leisure choices are treated as welfare-relevant (more leisure = higher welfare), even if the higher leisure in France reflects higher taxes rather than preferences.

The approach is closer to the conditional equality solution in Fleurbaey (1995) -- using benchmark preferences $\tilde{R}$ -- than to the egalitarian-equivalent solution (which uses individual preferences).

# Treatment of opportunities / constraints

Opportunities are not modelled. The welfare measure is based on outcomes (consumption, leisure, mortality), not on the opportunity sets available to individuals. There is no distinction between voluntary and involuntary non-participation, no job availability, no RURO-type opportunity density. The measure cannot distinguish between a country where people work fewer hours because they prefer leisure and one where fewer jobs are available.

# Welfare / normative object

Consumption-equivalent welfare $\lambda_i$: the proportion of US consumption that would make a person behind a veil of ignorance indifferent between the US and country $i$. This is an equivalent-variation measure. The paper also computes the compensating variation $\lambda_i^{cv}$ (Section I.D), which can differ substantially for poor countries because it weights life expectancy differences by a country's own flow utility rather than by US flow utility.

Social welfare is utilitarian (equal weights) behind the veil of ignorance. Risk aversion (inequality aversion) comes from the concavity of the utility function.

# Main findings

1. **GDP per capita and welfare are highly correlated (0.98 in logs) but deviations are economically important (Table 2, Figure 5).** Median deviation: 35%. Western Europe is closer to the US in welfare (85%) than in income (67%). Developing countries are further behind in welfare than income.

2. **France example (Table 2):** Income = 67% of US, but welfare = 92% of US. Life expectancy adds 15 log points, leisure adds 8, lower inequality adds ~20. Consumption share subtracts 15.

3. **Each component matters (Table 2):** Life expectancy is the most important non-income component, especially for developing countries. Leisure matters for Europe vs. US comparisons. Inequality matters for Latin America and sub-Saharan Africa.

4. **Welfare growth exceeds income growth by ~1 percentage point (Table 3, Key Point 4):** Average welfare growth = 3.1% vs. income growth = 2.1% (1980s to mid-2000s). Rising life expectancy accounts for the bulk of the difference.

5. **Sub-Saharan Africa's tragedy (Tables 7--9):** Botswana and South Africa have welfare below 5% of the US level, far below their income (17--25%), due to AIDS-driven mortality and extreme inequality.

6. **Robustness (Table 4):** Results are qualitatively robust to: no discounting/growth, CRRA preferences ($\gamma = 1.5, 2.0$), household equivalence scales, different Frisch elasticities (0.5, 2.0), different values of life (\$5--7 million), equivalent vs. compensating variation.

# Main limitations

- Common preferences across countries (not individual preferences)
- No morbidity, only mortality (life expectancy as a crude health proxy)
- No natural environment, crime, political freedom, social connections
- No distinction between voluntary and involuntary leisure/unemployment
- Static: no savings/investment dynamics (consumption share penalises high-investment countries like Norway, Singapore)
- Utility function assumed, not estimated from data
- No within-country heterogeneity in preferences
- No job quality, working conditions, or opportunity set differences

# Relevance for my JMP

## possible use for framing
The paper provides a benchmark "beyond GDP" welfare measure against which the RURO-based equivalent income measure can be compared. Both approaches incorporate leisure and consumption into welfare. The key differences: (1) Jones-Klenow use common preferences; my JMP uses individual preferences via RURO. (2) Jones-Klenow do not model opportunities; my JMP decomposes welfare into preferences ($R$) and opportunities ($A$). (3) Jones-Klenow cannot distinguish voluntary leisure from unemployment; RURO can through the opportunity density.

## possible use for motivating individual-level analysis
The paper's limitation -- common preferences -- motivates the RURO approach. The paper acknowledges: "Preferences over consumption and leisure must differ within countries [...] exploring the role of preference heterogeneity versus wedges in explaining the joint consumption and hours decisions across households across and within countries" is left for future research (p. 2455, footnote 19). My JMP addresses exactly this by estimating heterogeneous preferences $v(C, T-h; x_V)$ and heterogeneous opportunities $g(h,w)$.

## possible use for the leisure component
The paper's treatment of leisure is instructive: it uses a Frisch elasticity of 1.0 and calibrates $\theta$ from the FOC. In the RURO framework, leisure enters through the structural utility $v(C, T-h)$, and the opportunity density $g(h,w)$ determines which leisure-income bundles are available. The paper's finding that leisure adds 8 log points to French welfare relative to the US highlights the importance of the leisure channel, which is central to labour supply welfare analysis.

# Research questions this paper inspires

1. How much of the cross-country welfare difference attributed to "leisure" in Jones-Klenow reflects differences in opportunity sets (fewer jobs available in Europe) versus preferences (Europeans prefer more leisure)? The RURO framework could decompose the leisure component into voluntary and involuntary parts.

2. Can the Jones-Klenow framework be extended to use individual preferences estimated from structural labour supply models? Instead of common $\bar{u} + \log C + v(\ell)$ for all agents, use the RURO-estimated $v_i(C, T-h)$ for each individual. This would produce an individualistic equivalent income that Fleurbaey (2009) advocates.

3. The paper's inequality component uses within-country consumption variance. In the RURO framework, inequality arises from both preference heterogeneity and opportunity heterogeneity. How much of within-country inequality is due to differences in $A$ (opportunity sets) versus $R$ (preferences)?

# Challenge to this paper

The use of common preferences is the paper's fundamental limitation. By evaluating all countries with the same utility function, the welfare measure cannot distinguish between: (a) a country where people work less because they value leisure more (preference-driven), and (b) a country where people work less because fewer jobs are available (opportunity-constrained). In case (a), the higher leisure is welfare-improving (people are getting what they want). In case (b), it may not be (people are involuntarily unemployed). The common-preference approach treats both cases identically, attributing the same welfare gain to the same leisure level regardless of the reason.

The Fleurbaey (2009) equivalent-income approach resolves this by using individual preferences: agent $i$'s welfare is evaluated using $i$'s own preferences, not a common utility function. The RURO framework goes further by structurally separating the opportunity density $g(h,w)$ from preferences $v(C, T-h)$, enabling welfare decomposition into voluntary and involuntary components.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper computes a consumption-equivalent welfare measure that incorporates consumption ($C$), leisure ($\ell = T - h$), inequality, and mortality. In the $W(z, R, A; y)$ framework, the paper captures $z$ (realized bundle of $C$ and $\ell$) and a common $R$ (benchmark preferences), but does not model $A$ (opportunity set) or $y$ (tax-benefit schedule) structurally.

[Reasonable inference for my project] The Jones-Klenow measure is a special case of the Fleurbaey equivalent-income approach with: (1) common benchmark preferences $\tilde{R}$ instead of individual preferences, (2) no explicit opportunity set $A$, (3) consumption used as the numeraire instead of income. The RURO-based equivalent income in my JMP is more general: it uses individual preferences, models opportunities explicitly, and incorporates the tax-benefit schedule.

[Unclear from paper] How the results would change with heterogeneous preferences. The paper's footnote 19 flags this as an open question. If Europeans genuinely prefer more leisure (higher $v(\ell)$), the welfare gap between Europe and the US would be even smaller than the paper reports. If instead European leisure is partly involuntary (limited job opportunities), the gap could be larger.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) use individual preferences estimated from a structural labour supply model to compute equivalent incomes, while Jones-Klenow use common preferences applied to aggregate data. The Bargain et al. approach is more principled for within-country welfare analysis but cannot easily be applied cross-country. Jones-Klenow provide the cross-country comparison but sacrifice preference heterogeneity. My JMP bridges these: structural estimation of heterogeneous preferences and opportunities within a country, then equivalent-income computation that incorporates both $R$ and $A$ channels.

# Relation to opportunities vs preferences

The paper does not distinguish opportunities from preferences. Leisure differences across countries are attributed entirely to the welfare effect of leisure in the common utility function, without asking whether the leisure reflects choice or constraint. This is the central limitation for my JMP's purposes: the $R$-$A$ decomposition is the core contribution of the RURO approach, and Jones-Klenow's framework cannot accommodate it.

# Useful quotations / formulas

**Welfare measure (p. 2430, eq. 3):**
"By what factor, $\lambda_i$, must we adjust Rawls' consumption to make him indifferent between living his life as a random person in the United States and living in some other country $i$?"

**France result (p. 2427):**
"Rather than looking like 60 percent of the US value, as it does based solely on consumption, France ends up with consumption-equivalent welfare equal to 92 percent of that in the United States."

**Key Point 1 (p. 2439):**
"GDP per person is an excellent indicator of welfare across a broad range of countries: the two measures have a correlation of 0.98. Nevertheless, there are economically important differences..."

**Key Point 4 (p. 2443):**
"Welfare growth averages 3.1 percent between the 1980s and the mid-2000s, versus income growth of 2.1 percent... A boost from rising life expectancy of more than a percentage point shows up throughout the world."

**On preference heterogeneity (footnote 19, p. 2455):**
"A topic for future research would be exploring the role of preference heterogeneity versus wedges in explaining the joint consumption and hours decisions across households across and within countries."

# Suggested tags

welfare-measurement, beyond-GDP, consumption-equivalent, expected-utility, veil-of-ignorance, Rawls, cross-country, inequality, leisure, mortality, life-expectancy, decomposition, equivalent-variation, Frisch-elasticity, France-US, developing-countries, growth, AER

# My quick takeaway

An elegant implementation of the beyond-GDP agenda using standard expected-utility theory. The paper shows that non-income dimensions (life expectancy, leisure, inequality) cause economically significant deviations between welfare and GDP -- Western Europe rises from 67% to 85% of US welfare. For my JMP, the paper's key limitation is the use of common preferences: it cannot distinguish leisure that reflects individual choice from leisure that reflects limited job opportunities. The RURO framework resolves this by structurally separating preferences from opportunities and using individual preferences for welfare evaluation. The paper's finding that leisure adds significantly to European welfare motivates the importance of getting the leisure/opportunity decomposition right -- if the "extra leisure" in Europe is partly involuntary (constrained by opportunity density $g(h,w)$), the welfare interpretation changes fundamentally.
