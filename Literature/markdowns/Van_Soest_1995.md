---
title: "Structural Models of Family Labor Supply: A Discrete Choice Approach"
authors: [Arthur van Soest]
year: 1995
outlet: "Journal of Human Resources, 30(1), 63--88"
country_or_context: "Netherlands"
population: "Married/cohabiting couples, both partners aged 16--65, male working"
data_period: "1987 (SEP, Socio-Economic Panel)"
shelf: "structural labour supply / discrete choice / hours restrictions / tax-benefit modelling"
tags: [discrete-choice, labour-supply, translog, conditional-logit, hours-restrictions, random-preferences, simulated-ML, Netherlands, SEP, tax-reform, elasticities, policy-simulation, wage-prediction]
priority: "high"
read_status: "extracted"
---

# Full citation

Van Soest, A. (1995). Structural Models of Family Labor Supply: A Discrete Choice Approach. *Journal of Human Resources*, 30(1), 63--88.

# One-sentence contribution

Introduces the discrete-choice approach to structural labour supply modelling -- discretising the hours continuum into a finite set of alternatives and estimating preferences via conditional logit on a translog direct utility function -- and shows that incorporating hours restrictions (via alternative-specific constants) dramatically improves fit and reduces wage elasticities, while random preferences add little.

# Why this paper matters

This is the foundational paper for the discrete-choice labour supply literature. Before this paper, structural labour supply models either used continuous hours (Hausman 1985) with well-known econometric difficulties (non-convex budget sets, multiple tangencies) or simplified the tax system. Van Soest showed that discretising the choice set sidesteps these problems entirely: any tax-benefit system, however complex, can be handled by simply computing net income at each discrete point. The approach became the workhorse methodology for ex-ante policy evaluation across Europe (used by virtually all subsequent papers in this literature: Bargain et al. 2013, Aaberge-Colombino, Löffler et al. 2014, etc.).

# Core research question

Can a discrete-choice framework for family labour supply tractably incorporate complex tax-benefit systems, hours restrictions, and preference heterogeneity, and what are the implications for estimated elasticities and policy evaluation?

# Economic setting and context

Netherlands, 1987. The Dutch tax system features individual taxation (since 1984), social security contributions, means-tested housing subsidies, and child benefits. Female labour force participation is low by international standards (~35% of married women work), with strong clustering at part-time hours (15--25 hours/week). The policy question is whether switching to joint taxation or changing tax rates would affect female participation.

# Model / theoretical framework

**Basic model (Section III, Model I):** Household utility is a translog function of after-tax income $y$, male leisure $l_m$, and female leisure $l_f$:

$$U(v) = v' A v + b' v$$

where $v = (\ln y, \ln l_m, \ln l_f)'$, $A$ is a $3 \times 3$ symmetric matrix of quadratic/interaction parameters $\{a_{kl}\}$, and $b = (b_1, b_2, b_3)'$ is a vector of linear parameters. Taste variation enters through $b_k = \sum_r \beta_{kr} x_r$ where $x_r$ are demographic characteristics (age, children, education).

Choice set: each partner chooses from $m_{ind}$ discrete hours levels (0, 5, 10, ..., 60 for women; 0, 38, ..., 60 for men). Total alternatives: $J = m_{ind}^2$ for the couple. Net household income $y_j$ at each combination computed via full tax-benefit microsimulation.

**Conditional logit:** Adding iid extreme-value errors $\epsilon_j$ to utility, the probability of choosing alternative $j$:

$$P(j) = \frac{\exp(U_j)}{\sum_{k=1}^{J} \exp(U_k)}$$

**Model II -- Hours restrictions:** Adds alternative-specific constants $\gamma_{sk}$ to utility for hours level $k$ and partner $s$:

$$U_j = U(v_j) + \gamma_{mh_m} + \gamma_{fh_f}$$

These capture hours restrictions (unavailability of certain hours levels) and fixed costs of working. Identified relative to full-time. Expected to be negative (fewer jobs available at non-standard hours).

**Model III -- Wage prediction errors:** Wages are predicted for all individuals (including non-workers) via Mincer equations. The prediction error $\xi$ enters net income, creating a random utility component. Estimated via simulated maximum likelihood:

$$P(j) = \frac{1}{R} \sum_{r=1}^{R} \frac{\exp(U_j(\xi^r))}{\sum_k \exp(U_k(\xi^r))}$$

with $R = 5$ or $R = 10$ draws. Consistency as $R \to \infty$ (Lerman and Manski 1981).

**Model IV -- Random preferences:** Adds random coefficients $\zeta_2, \zeta_3$ (normal) to the linear leisure terms $b_2, b_3$:

$$b_s = \sum_r \beta_{sr} x_r + \zeta_s, \quad \zeta_s \sim N(0, \sigma_{\zeta_s}^2)$$

Estimated via simulated ML jointly with wage errors.

# Key objects

- **Translog utility parameters** $\{a_{kl}, \beta_{kr}\}$: determine substitution patterns between income and leisure for each partner
- **Hours restriction parameters $\gamma_{sk}$**: alternative-specific constants capturing demand-side constraints on available hours levels
- **Wage elasticities of labour supply** (Table 4): uncompensated own-wage elasticities for males and females, at mean and median
- **Policy simulation effects** (Table 5): predicted changes in hours and participation from tax reforms

# Data

Dutch Socio-Economic Panel (SEP), 1987 wave. Sample: 2,859 couples where both partners are aged 16--65, male works at least one hour, neither self-employed, not in education, not receiving disability benefits. Female participation rate: ~35%. Male hours strongly peaked at 38--40/week; female hours dispersed with peaks at 0, 20, and 38.

Wage equations estimated on workers only (no Heckman correction in the main specification). Male wage equation: $R^2 = 0.39$; female: $R^2 = 0.31$. Predicted log wages used for non-workers and in the structural model.

Tax-benefit system modelled in full detail: income tax (three brackets, individual basis), social security contributions, housing subsidies, child benefits.

# Identification logic

Identification comes from: (1) variation in gross wages across individuals (from human capital differences), (2) variation in non-labour income, (3) nonlinearities in the tax-benefit system (bracket changes, phase-outs, means-testing) creating exogenous variation in effective marginal tax rates at different hours levels, (4) demographic variation in household composition affecting both preferences and budget constraints. The discrete-choice framework requires only that utility can be computed at each hours point -- it does not require smoothness or convexity of the budget set.

# Estimation / empirical strategy

1. **Wage equations:** OLS on log hourly wages for workers. Covariates: age, age$^2$, education dummies, sector dummies. Predicted wages for all individuals.
2. **Tax-benefit simulation:** Compute net household income $y_j$ at each discrete hours combination using the full 1987 Dutch tax-benefit rules.
3. **Structural model:** Maximum likelihood (Models I, II) or simulated ML (Models III, IV) on the conditional logit.
4. **Elasticities:** Compute uncompensated wage elasticities by raising gross wage by 1%, recomputing net incomes at all hours points, and comparing predicted hours distributions.
5. **Policy simulations:** Separate taxation vs. joint taxation, proportional tax changes.

# Treatment of preferences

Translog direct utility with observed heterogeneity (age, children, education) in linear terms. Model IV adds unobserved heterogeneity via normal random coefficients on leisure terms, but the estimated standard deviations are small and barely affect results. No fixed costs of working modelled explicitly (captured by hours restriction constants instead). Preferences are assumed identical across partners conditional on observables (no correlated random effects across spouses).

The paper's key finding on preferences: the functional form (translog) and demographic heterogeneity are sufficient; random preference heterogeneity (Model IV) adds little because the hours restriction parameters $\gamma_{sk}$ already absorb much of the unexplained variation in hours choices.

# Treatment of opportunities / constraints

This is the paper's most important methodological contribution. **Hours restrictions** are modelled via alternative-specific constants $\gamma_{sk}$ that are negative for non-standard hours (part-time, overtime), capturing the fact that fewer jobs are available at these hours. The $\gamma_{sk}$ parameters act as reduced-form proxies for demand-side constraints -- they shift utility of non-standard hours downward, mimicking the effect of limited job availability.

However, opportunities are not modelled structurally: there is no explicit job offer distribution, no opportunity density $g(h,w)$, and no distinction between voluntary and involuntary hours choices. The $\gamma_{sk}$ are estimated as free parameters and could reflect either demand constraints or fixed costs of working. The paper acknowledges this ambiguity.

This is a fundamental limitation that the RURO framework (Dagsvik, Aaberge-Colombino) addresses by modelling the opportunity set explicitly.

# Welfare / normative object

No welfare analysis. The paper focuses on positive predictions: elasticities and policy simulations of hours and participation changes. No equivalent variation, compensating variation, or social welfare function is computed.

# Main findings

1. **Model I (basic) fits poorly (Table 3):** Overpredicts female part-time (15--25 hours), underpredicts both non-participation and full-time. The smooth translog utility cannot generate the observed clustering at 0 and 38 hours.

2. **Model II (hours restrictions) fits well:** Adding $\gamma_{sk}$ parameters dramatically improves fit. The estimated $\gamma_{sk}$ are large and negative for non-standard hours: $\gamma_{f,10} = -1.18$, $\gamma_{f,15} = -0.67$, $\gamma_{f,20} = -0.40$, $\gamma_{f,38} = 0$ (reference). This means part-time hours carry a "utility penalty" that proxies for their limited availability.

3. **Hours restrictions reduce elasticities substantially (Table 4):**
   - Female own-wage elasticity: Model I median = 1.027; Model II median = 0.524; Model III median = 0.472
   - Male own-wage elasticity: approximately 0.08 across all models (insensitive to specification)
   - The reduction in female elasticity from hours restrictions is intuitive: if part-time jobs are scarce, a wage increase cannot pull many women into part-time work.

4. **Wage prediction errors matter, random preferences do not (Models III, IV):** Incorporating wage prediction uncertainty via simulated ML (Model III) slightly changes elasticities. Random preference heterogeneity (Model IV) has negligible effects -- the estimated standard deviations of $\zeta_2, \zeta_3$ are small.

5. **Policy simulations (Table 5):**
   - 10% male wage increase → male hours +0.11% (near zero)
   - 10% female wage increase → female hours +0.40% (moderate)
   - Switch from individual to joint taxation → female hours $-4.2\%$, male hours $+0.7\%$

6. **Computational tractability:** The discrete-choice approach handles the full Dutch tax-benefit system without difficulty. No need for piecewise-linear approximations, convexification, or multiple-tangency algorithms.

# Main limitations

- Hours restrictions modelled as reduced-form constants, not structurally (no job offer distribution)
- No distinction between voluntary non-participation and involuntary unemployment
- Conditional logit implies IIA across hours alternatives (no nested or mixed logit in main models)
- Wage endogeneity not addressed (no joint estimation of wages and preferences -- see Löffler et al. 2014)
- No Heckman correction for wage selectivity in the main specification
- Static model: no dynamics, no job search, no intertemporal considerations
- Homogeneous hours restrictions $\gamma_{sk}$: same for all individuals within a gender (no heterogeneity by education, region, sector)
- Netherlands 1987 only; external validity unclear

# Relevance for my JMP

## possible use for framing
This is the foundational paper for the entire discrete-choice labour supply literature. Any JMP using this methodology must cite and discuss Van Soest (1995). The paper establishes the baseline approach against which the RURO framework can be contrasted: Van Soest uses reduced-form hours restrictions ($\gamma_{sk}$) while RURO models the opportunity set structurally via $g(h,w)$.

## possible use for model design
The translog utility specification $U(v) = v'Av + b'v$ is the standard starting point for discrete-choice models. The RURO framework replaces the $\gamma_{sk}$ parameters with an explicit opportunity density, which has two advantages: (1) it allows individual-level variation in opportunities (by education, region, sector), and (2) it enables welfare decomposition into preferences vs. opportunities.

## possible use for identification
The paper shows that hours restrictions ($\gamma_{sk}$) are essential for fit but conflate demand constraints with fixed costs. This identification problem motivates the RURO approach: by modelling opportunities explicitly, one can distinguish between "few part-time jobs exist" (opportunity constraint) and "part-time work is costly" (preference/fixed cost). This distinction matters for welfare: an opportunity constraint reduces $A$ in $W(z,R,A;y)$, while a fixed cost affects $R$.

## possible use for limitations discussion
The paper's hours restrictions are homogeneous: all women face the same $\gamma_{sk}$. In the RURO framework, the opportunity density $g_i(h,w)$ varies by individual characteristics, allowing heterogeneous constraints. This is important for welfare analysis: two women may face the same preferences but different opportunity sets (e.g., rural vs. urban, low vs. high education), leading to different welfare levels through the $A$-channel.

# Research questions this paper inspires

1. Can the hours restriction parameters $\gamma_{sk}$ be decomposed into demand-side constraints (opportunity density) and fixed costs of working (preferences)? The RURO framework suggests yes, but the decomposition requires additional structure or data.

2. How sensitive are welfare conclusions (not just elasticities) to the treatment of hours restrictions? If $\gamma_{sk}$ reflects demand constraints, the welfare cost of limited part-time availability could be large -- but this cannot be computed without a structural opportunity model.

3. Does the IIA property of conditional logit matter for policy simulations? If a new hours category (e.g., 30-hour jobs) is introduced, IIA predicts proportional substitution from all existing categories, which may be unrealistic.

4. How do the results change with heterogeneous hours restrictions (by education, sector, region)? The RURO framework's individual-specific opportunity density addresses this, but Van Soest's approach could be partially extended by interacting $\gamma_{sk}$ with demographics.

# Challenge to this paper

The paper's central innovation -- hours restriction parameters $\gamma_{sk}$ -- is both its greatest strength and its fundamental limitation. The $\gamma_{sk}$ absorb all deviation between observed hours distributions and what smooth preferences would predict, but they are not interpretable: a large negative $\gamma_{f,10}$ could mean (a) few 10-hour jobs exist (demand constraint), (b) 10-hour work involves high fixed commuting/childcare costs (preference-side), or (c) measurement error in reported hours makes 10 hours rarely observed. Without distinguishing these channels, the model cannot answer welfare questions about hours constraints. If the government creates more part-time jobs (expanding $A$), does welfare increase? Van Soest's model cannot answer this because $\gamma_{sk}$ conflates $A$ and $R$.

Moreover, the $\gamma_{sk}$ are homogeneous across all individuals of the same gender. A university-educated woman in Amsterdam and a low-educated woman in a rural area face the same hours restriction parameters. This is implausible and masks substantial heterogeneity in opportunity sets that matters for both positive predictions and welfare analysis.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper models labour supply as a discrete choice among hours-income bundles $z_j = (h_j, y_j)$, where $y_j$ is determined by gross wages and the tax-benefit system $y(\cdot)$. Preferences $R$ are captured by translog utility with demographic heterogeneity. Hours restrictions $\gamma_{sk}$ are a reduced-form proxy for the feasible set $A$.

[Reasonable inference for my project] In the $W(z, R, A; y)$ framework, Van Soest's model captures $z$ (realized bundle), $R$ (preferences via translog utility), and $y$ (tax-benefit schedule), but treats $A$ only through the blunt instrument of $\gamma_{sk}$. The RURO framework enriches the $A$-component by replacing $\gamma_{sk}$ with an explicit opportunity density $g(h,w)$, enabling welfare decomposition into preference-driven and opportunity-driven components.

[Unclear from paper] How the welfare effects of policy reforms depend on the treatment of opportunities. If $\gamma_{sk}$ partly reflects demand constraints, then a tax reform that increases labour supply may run into limited demand for certain hours levels -- an effect that Van Soest's model misses but that Peichl and Siegloch (2012) address through their demand-supply iteration.

The paper is closest to: **the foundational discrete-choice methodology for structural labour supply** and **the starting point from which RURO models depart by modelling opportunities explicitly**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) use a Van Soest-type discrete-choice model as the structural base for computing Fleurbaey welfare metrics. The hours restriction parameters $\gamma_{sk}$ in the structural model affect the estimated preference parameters, which in turn affect the welfare metrics. If $\gamma_{sk}$ conflates preferences and opportunities, then the preference estimates fed into the welfare metrics are biased, potentially distorting the welfare decomposition. The RURO framework would provide cleaner preference estimates (purged of opportunity effects) for the welfare calculation.

# Relation to opportunities vs preferences

This paper is the key reference for the **confounding of opportunities and preferences** in standard labour supply models. The $\gamma_{sk}$ parameters are the mechanism through which opportunities are implicitly captured, but they are not identified separately from preferences. The paper's hours restriction approach is the methodological foil against which the RURO framework's explicit opportunity modelling should be evaluated.

The comparison: Van Soest (1995) uses $\gamma_{sk}$ (homogeneous, reduced-form, not welfare-interpretable) while RURO uses $g(h,w)$ (heterogeneous, structural, welfare-decomposable). Both improve fit over the basic model, but only the RURO approach enables the $R$-$A$ decomposition needed for $W(z, R, A; y)$.

# Useful quotations / formulas

**Translog utility (eq. 1):**
$$U(v) = v' A v + b' v, \quad v = (\ln y, \ln l_m, \ln l_f)'$$

**Choice probability (eq. 6):**
$$P(j) = \frac{\exp(U_j)}{\sum_{k=1}^{J} \exp(U_k)}$$

**Hours restrictions (eq. 13--14):**
$$U_j = U(v_j) + \gamma_{m,h_m} + \gamma_{f,h_f}$$

**On hours restrictions (p. 75):**
"If the labor market is such that not every job of any number of hours is available [...] then the model described above does not correctly describe labor supply decisions. [...] A negative value of $\gamma_{sk}$ can be interpreted as an indicator of 'hours restrictions': it reduces the attractiveness of jobs with $h_s$ hours."

**On the importance of hours restrictions for elasticities (p. 82):**
"Adding hours restrictions to the model has a substantial effect on the elasticities [...] The female own-wage elasticities fall by about 50%."

**On random preferences (p. 83):**
"The random terms, with 10 draws, do not seem to add a lot to the model with hours restrictions."

**Simulated ML (eq. 10--12):**
$$P(j) \approx \frac{1}{R} \sum_{r=1}^{R} \frac{\exp(U_j(\xi^r))}{\sum_k \exp(U_k(\xi^r))}$$

# Suggested tags

discrete-choice, labour-supply, translog, conditional-logit, hours-restrictions, alternative-specific-constants, random-preferences, simulated-ML, Netherlands, SEP, tax-reform, wage-elasticity, policy-simulation, family-labour-supply, microsimulation

# My quick takeaway

This is the paper that launched the discrete-choice labour supply literature. Its key insight -- discretise the hours choice set and use conditional logit -- elegantly sidesteps the computational nightmares of continuous hours models with nonlinear taxes. The hours restriction parameters $\gamma_{sk}$ are essential for fit and reduce estimated elasticities by ~50%, but they conflate demand constraints with preference-side fixed costs. This conflation is the central motivation for the RURO framework: by modelling opportunities explicitly via $g(h,w)$, one can decompose the $\gamma_{sk}$ effect into opportunity constraints ($A$-channel) and preference effects ($R$-channel), enabling the welfare decomposition $W(z, R, A; y)$ that is the goal of my JMP. Van Soest (1995) is the methodological starting point; the RURO model is where it needs to go.
