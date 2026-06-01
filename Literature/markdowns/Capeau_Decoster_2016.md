---
title: "Getting tired of work, or re-tiring in absence of decent job opportunities? Some insights from an estimated Random Utility/Random Opportunity model on Belgian data"
authors: [Bart Capéau, André Decoster]
year: 2016
outlet: "EUROMOD Working Paper, No. EM4/16, ISER, University of Essex"
country_or_context: "Belgium"
population: "Working-age adults (16--64), singles and couples, employees and unemployed (excluding self-employed, early retired, disabled, students)"
data_period: "EU-SILC 2007 Belgium, EUROMOD version F5.5"
shelf: "RURO / discrete choice / labour supply / ageing / preferences vs opportunities / job offers / extensive margin"
tags: [RURO, random-utility, random-opportunity, discrete-choice, labour-supply, job-offers, opportunity-density, Poisson-process, Frechet, ageing, preferences, opportunities, extensive-margin, intensive-margin, Belgium, EU-SILC, EUROMOD, Box-Cox, wage-offer-distribution, hours-distribution, counterfactual, Capeau, Decoster]
priority: "very high"
read_status: "extracted"
---

# Full citation

Capéau, B. and Decoster, A. (2016). Getting tired of work, or re-tiring in absence of decent job opportunities? Some insights from an estimated Random Utility/Random Opportunity model on Belgian data. *EUROMOD Working Paper*, No. EM4/16, ISER, University of Essex.

# One-sentence contribution

Estimates a full RURO (Random Utility/Random Opportunity) model on Belgian data, separately identifying age effects on preferences (increasing taste for leisure with age) and opportunities (declining job offer intensity after age 30), and uses counterfactual simulations to show that declining opportunities are at least as important as changing preferences in explaining the lower labour market participation of older workers, with opportunities operating primarily through the extensive margin and preferences through both margins.

# Why this paper matters

This is the most directly relevant paper for my JMP's theoretical framework. It provides a complete, self-contained exposition of the RURO model and estimates it on European data, explicitly decomposing observed labour market behaviour into preference and opportunity components. The paper demonstrates that the distinction between $R$ (preferences) and $A$ (opportunities/feasible set) in $W(z, R, A; y)$ is not just theoretically important but empirically identifiable and quantitatively consequential. The counterfactual exercises (equalising opportunities vs. equalising preferences) are exactly the kind of analysis my JMP aims to conduct with the welfare dimension added.

# Core research question

To what extent is the lower labour market participation of older workers (aged 50--64 vs. 30--49) due to changing preferences (increasing taste for leisure) versus declining opportunities (fewer or less attractive job offers suitable for their capacities)?

# Economic setting and context

Belgium in 2007: participation rate drops sharply with age (e.g., females in couples: 85% for ages 30--49, 54% for ages 50--64; single males: 85% to 62%). Average hours conditional on working also decline by 6--10 hours/week. The paper investigates whether this is voluntary (preferences) or involuntary (opportunities). Belgium has relatively high unemployment, especially for low-educated and older workers (type-specific unemployment rates range from 2% to 34%).

# Model / theoretical framework

**Full RURO model (Sections 2.1--2.3):**

The choice set $\mathcal{Z} = \mathcal{I} \cup \mathcal{J}$ consists of non-market alternatives ($\mathcal{I}$) and job offers ($\mathcal{J}$), with $\mathcal{I} \cap \mathcal{J} = \emptyset$. A job offer $j \in \mathcal{J}$ specifies hours $h$, wage $w$, and non-pecuniary attributes $\mathbf{s}$.

**Utility:** Total utility from choosing alternative $z$ is multiplicatively separable:
$$U(C(z), H(z), s(z); \mathbf{x}_v) := V(C(z), T - H(z); \mathbf{x}_v) \cdot \varepsilon(s(z))$$
where $V$ is systematic utility (over consumption and leisure), $\varepsilon(s(z))$ captures unobserved non-pecuniary attributes, $C(z) = f(w, h; \mathbf{x}_f)$ is disposable income via tax-benefit system.

The systematic utility in hours-wage space:
$$\Psi(w, h; \mathbf{x}_v, \mathbf{x}_f) := V(f(w, h; \mathbf{x}_f), T - h; \mathbf{x}_v)$$

**Opportunity structure (inhomogeneous Poisson process):**

Job offers arrive according to an inhomogeneous spatial Poisson process with intensity:
$$g_2(t; \mathbf{x}_{g_2}) \cdot g_1(r|t; \mathbf{x}_{g_1}) \cdot \lambda^1(v; \mathbf{x}_q)$$
where $g_2(h; \mathbf{x}_{g_2})$ = density of hours regimes offered, $g_1(w|h; \mathbf{x}_{g_1})$ = conditional wage density, $\lambda^1(v; \mathbf{x}_q) = \pi_1(\mathbf{x}_q)/v^2$ = intensity of job offers yielding utility multiplier $v$.

Key parameter: $\pi_1(\mathbf{x}_q) \in (0, 1)$ measures the proportion of an individual's capacities that are useful on the job market. Normalisation: $\pi_0(\mathbf{x}_q) + \pi_1(\mathbf{x}_q) \equiv 1$, where $\pi_0$ measures the share useful for non-market alternatives.

Non-market alternatives similarly follow an inhomogeneous Poisson process with intensity $\lambda^0(\epsilon; \mathbf{x}_q) = \pi_0(\mathbf{x}_q)/\epsilon^2$.

**Relative job offer intensity:**
$$q(\mathbf{x}_q) := \frac{\pi_1(\mathbf{x}_q)}{\pi_0(\mathbf{x}_q)}$$
This is the key demand-side parameter: how many job offers an individual receives relative to non-market opportunities, as a function of personal characteristics.

**Distributional results:**
- $U_0$ (utility from best non-market alternative) $\sim$ Fréchet with scale $\sigma_0 = \pi_0 \Psi(0, 0; \mathbf{x}_v, \mathbf{x}_f)$ (eq. 10)
- $U_{\mathcal{B}}$ (utility from best job offer in set $\mathcal{B}$) $\sim$ Fréchet with scale $\sigma_{\mathcal{B}} = \pi_1 \int g_2(t) \int g_1(r|t) \Psi(r, t; \mathbf{x}_v, \mathbf{x}_f) \, dr \, dt$ (eq. 13--14)

**Likelihood (eq. 19):** Probability of choosing job $(w, h)$:
$$\varphi(w, h) = \frac{\Psi(w, h; \mathbf{x}_v, \mathbf{x}_f) \cdot q(\mathbf{x}_q) \cdot g_1(w; \mathbf{x}_{g_1}) \cdot g_2(h; \mathbf{x}_{g_2})}{\Psi(0, 0; \mathbf{x}_v, \mathbf{x}_f) + q(\mathbf{x}_q) \int_{\mathcal{W}} \int_{\mathcal{H}} \Psi(s, t; \mathbf{x}_v, \mathbf{x}_f) g_1(s; \mathbf{x}_{g_1}) g_2(t; \mathbf{x}_{g_2}) \, dt \, ds}$$

Probability of non-participation (eq. 19'):
$$\varphi(0, 0) = \frac{\Psi(0, 0; \mathbf{x}_v, \mathbf{x}_f)}{\Psi(0, 0; \mathbf{x}_v, \mathbf{x}_f) + q(\mathbf{x}_q) \int \int \Psi(s, t) g_1(s) g_2(t) \, dt \, ds}$$

**Comparison with standard discrete choice (eq. 20):** In the standard Van Soest (1995) model with fixed wage:
$$\varphi(w, h_l) = \frac{\Psi(w, h_l)}{\Psi(0, 0) + \sum_{k=1}^{K} \Psi(w, h_k)}$$
The RURO model differs: (i) utilities are weighted by opportunity density $q \cdot g_1 \cdot g_2$; (ii) wages are endogenous (part of the job offer); (iii) the denominator sums over all $(w, h)$ pairs, not just hours for a given wage.

**Functional forms (Section 3.3):**
- Systematic utility: Box-Cox type with exponents $\alpha_c < 1$ (consumption) and $\alpha_h < 1$ (leisure)
- Wage offer distribution $g_1$: lognormal with parameters depending on education and potential experience
- Hours distribution $g_2$: piecewise uniform with peaks around half-time (18.5--20.5), three-quarter-time (29.5--30.5), and full-time (37.5--40.5)
- Relative job intensity $q$: log-linear in covariates $\mathbf{x}_q$ (age, education, region, unemployment rate, gender)

# Key objects

- **$\pi_1(\mathbf{x}_q)$:** Proportion of individual's capacities demanded on the labour market -- the key demand-side parameter
- **$q(\mathbf{x}_q) = \pi_1/\pi_0$:** Relative intensity of job offers vs. non-market opportunities
- **$g_1(w; \mathbf{x}_{g_1})$:** Wage offer distribution -- lognormal, estimated simultaneously with preferences
- **$g_2(h; \mathbf{x}_{g_2})$:** Distribution of offered hours regimes -- piecewise uniform with peaks
- **$\Psi(w, h; \mathbf{x}_v, \mathbf{x}_f)$:** Systematic utility in hours-wage space
- **MRS$_{c,h}$:** Marginal rate of substitution between consumption and labour time (eq. 34--35)

# Data

Belgian EU-SILC 2007 data: 6,348 households, 15,493 individuals. Estimation sample: 1,457 couple households, 571 single females, 449 single males. Ages 16--64, excluding self-employed, early retired, disabled, sick, students. EUROMOD (version F5.5) used for tax-benefit simulation. External data: type-specific unemployment rates by age $\times$ sex $\times$ education from Eurostat (Table 2), used as exclusion restriction for identifying $q$ from preferences.

# Identification logic

**Key identification argument (Section 3.2, eqs. 21--23):**

Within an observationally equivalent group:

1. Ratio of densities at same wage, different hours identifies $\Psi(w, h) \cdot g_2(h)$:
$$\frac{\varphi(w, h_1)}{\varphi(w, h_2)} = \frac{\Psi(w, h_1) \cdot g_2(h_1)}{\Psi(w, h_2) \cdot g_2(h_2)}$$

2. Ratio at same hours, different wages identifies $g_1(w)$ (since $\Psi \cdot g_2$ cancels):
$$\frac{\varphi(w_1, h)}{\varphi(w_2, h)} = \frac{\Psi(w_1, h) \cdot g_1(w_1)}{\Psi(w_2, h) \cdot g_1(w_2)}$$

3. Ratio of workers to non-workers identifies $q$ (the relative job offer intensity):
$$\frac{\varphi(w, h)}{\varphi(0, 0)} = \frac{\Psi(w, h) \cdot q \cdot g_1(w) \cdot g_2(h)}{\Psi(0, 0)}$$

The unemployment rate serves as an exclusion restriction: it enters $q$ (opportunity) but not $V$ (preferences).

$\Psi$ and $g_2$ are not separately non-parametrically identified; functional form assumptions are needed. The wage density $g_1$ is non-parametrically identified (up to $\Psi$, which is identified from the functional form).

# Estimation / empirical strategy

Maximum simulated likelihood with importance sampling. Choice sets sampled from prior distribution $\mathbb{P}(w, h; \mathbf{x}_{\mathbb{P}})$ using lognormal wages and uniform hours on $[H_{\min}, H_{\max}]$, with non-market alternatives proportional to observed non-participation rate $\pi_0^{\text{obs}}$. Correction terms for sampling bias included (eqs. 27, 29, 31). Couples estimated as unitary model (both partners' job processes independent). Log likelihood = $-8427$ for couples. Estimation for singles and couples jointly via shared wage equation parameters.

# Treatment of preferences

Preferences enter through $V(c, T - h; \mathbf{x}_v)$ with Box-Cox functional form. Age affects preferences through taste shifters $\boldsymbol{\beta}_h' \mathbf{x}_v$ (quadratic in $\ln(\text{age})$), so the marginal rate of substitution between consumption and leisure changes with age. For single males: MRS increases monotonically with age (steeper indifference curves = stronger preference for leisure). For single females: U-shaped, with minimum preference for leisure at age 37. For males in couples: minimum at age 36. For females in couples: monotonically increasing. Education also affects preferences: higher education generally reduces leisure preference for females.

Key finding: age effects on preferences are estimated jointly with age effects on opportunities, so the two channels are disentangled. This is impossible in standard discrete-choice models where all age effects are absorbed into preferences.

# Treatment of opportunities / constraints

Opportunities are explicitly modelled through the Poisson process structure:
1. **Relative intensity $q(\mathbf{x}_q)$:** Depends on age (quadratic in $\ln(\text{age})$), region (Brussels, Flanders, Wallonia), education, gender, type-specific unemployment rate. Key result: $\pi_1$ has inverted-U shape peaking around age 30, then declining sharply. At age 60, $\pi_1$ is approximately 10--15% (vs. 60--80% at age 30). Regional variation: Brussels lowest, Flanders highest.
2. **Wage offer distribution $g_1(w; \mathbf{x}_{g_1})$:** Lognormal, depends on potential experience and education. Higher education shifts distribution right. Mean wages: low-educated males 8.58--10.33 EUR/hr, high-educated 13.08--15.74 EUR/hr (Table 5).
3. **Hours distribution $g_2(h; \mathbf{x}_{g_2})$:** Piecewise uniform with peaks. For males: full-time (37.5--40.5) and over-time (40.5--70) dominate (~65%). For females: more part-time offers (~26% in half-time + three-quarter-time peaks) (Table 6).

The paper explicitly notes (p. 50) a conceptual difficulty: in this static model, increasing $q$ (more jobs) simultaneously reduces non-market opportunities ($\pi_0 = 1 - \pi_1$), so "increasing job offer intensity is not a blessing for all" -- especially for elderly who prefer leisure activities.

# Welfare / normative object

No formal welfare analysis is conducted. The paper uses utility comparisons (Figures 13--15) to assess whether individuals are better off in the "equalised opportunities" counterfactual. The finding that some individuals lose utility when given more job offers (because they lose non-market opportunities) highlights a conceptual limitation of the RURO model's normalisation ($\pi_0 + \pi_1 = 1$). No equivalent-income or social welfare function is computed.

# Main findings

1. **Job offer intensity declines sharply with age (Figure 6, Table 7):** $\pi_1$ peaks around age 30 (70--80% for Flanders reference) then drops to 10--15% by age 60. The decline is steeper for females. Regional variation is substantial: Brussels residents face much lower job intensity than Flanders residents at all ages.

2. **Preferences for leisure increase with age, but pattern varies by group:** For single males and females in couples, preference for leisure increases monotonically with age. For single females and males in couples, it is U-shaped (minimum around age 36--37). Education effects: higher education reduces leisure preference for females.

3. **Equalising Opportunities counterfactual (EO, Table 9):** Giving all individuals the job offer intensity of a 30-year-old raises overall participation by **6.9 ppt** (from 82.0% to 88.9%). The effect is largest for single females (+11.6 ppt) and smallest for males in couples (+3.1 ppt). The effect is concentrated on the **extensive margin** (participation); conditional hours barely change (decrease of 0.3 hours/week on average).

4. **Equalising Preferences counterfactual (EP, Table 9):** Giving all individuals the preferences of their group-specific age with minimum leisure intensity raises participation by **2.6 ppt** (from 82.0% to 84.6%). This is substantially smaller than the EO effect. Unlike EO, EP affects both margins: conditional hours increase by 1.9 hours/week.

5. **Opportunities dominate the extensive margin; preferences affect both margins:** The key decomposition result. Declining opportunities with age explain most of the participation drop (EO raises participation more than EP in all groups). But changing preferences explain most of the intensive-margin decline (hours conditional on working increase more under EP than EO).

6. **Wage elasticities (Table 8):** Total wage elasticities from shifting the wage offer distribution by 10%: females in couples 0.50, single females 0.48, males in couples 0.31, single males 0.29. Cross-effects for couples: shifting female wages reduces male participation by 0.11, and vice versa ($-0.22$). These are larger than standard micro estimates because they include extensive-margin responses and reflect shifts of the wage offer distribution, not a change in a fixed individual wage.

7. **Utility effects of equalising opportunities (Figures 13--15):** Surprisingly, some individuals lose utility in the EO counterfactual despite facing more job offers. This is because more jobs = fewer non-market opportunities ($\pi_0 + \pi_1 = 1$), which harms those who prefer leisure.

# Main limitations

- Working paper (not published in a journal as of 2016)
- Static model: does not capture dynamic retirement incentives (social security wealth accrual)
- Unitary household model for couples: assumes identical preferences and joint utility maximisation
- $\pi_0 + \pi_1 = 1$ normalisation creates a zero-sum between market and non-market opportunities, which is problematic (authors acknowledge this on p. 50)
- Hours distribution $g_2$ is not non-parametrically identified separately from $\Psi$ (acknowledged on p. 18)
- Small sample sizes (449 single males, 571 single females) lead to imprecise estimates for some preference parameters
- Unemployment rate as exclusion restriction for identifying $q$ may be endogenous (reflects both demand and supply)
- No welfare analysis beyond utility comparisons

# Relevance for my JMP

## core reference for the RURO framework
This paper provides the most complete self-contained exposition of the RURO model that I use. The decomposition into $V(\cdot)$ (preferences), $q(\mathbf{x}_q)$ (opportunity intensity), $g_1$ (wage distribution), and $g_2$ (hours distribution) maps directly onto my framework's $W(z, R, A; y)$ where $R$ corresponds to $V$, $A$ corresponds to $(q, g_1, g_2)$, and $y$ is captured by $f(\cdot)$ (the tax-benefit system).

## core reference for the preferences-vs-opportunities decomposition
The EO and EP counterfactuals are exactly the type of analysis my JMP aims to conduct, but with the welfare dimension (equivalent income) added. The finding that opportunities dominate the extensive margin and preferences affect both margins is a key empirical fact that my welfare analysis should account for.

## key methodological reference
The identification argument (Section 3.2), the estimation procedure (importance sampling with correction terms), and the simulation method are directly applicable to my work. The exclusion restriction (unemployment rate enters $q$ but not $V$) is a strategy I may need to adapt or improve.

## the normalisation problem is directly relevant
The $\pi_0 + \pi_1 = 1$ constraint means that increasing job offers mechanically reduces non-market opportunities. This is the RURO model's Achilles' heel: it cannot distinguish between "more jobs available" and "fewer leisure options available." My JMP should address this by either relaxing the normalisation or carefully interpreting the counterfactuals.

# Research questions this paper inspires

1. How do the EO and EP counterfactuals affect equivalent income (money-metric welfare) rather than utility? The paper only reports utility comparisons. Using Fleurbaey-Maniquet equivalent income would provide interpersonally comparable welfare measures and allow social welfare evaluation.

2. The paper finds that some individuals lose utility from more job offers (Figures 13--15). In the equivalent-income framework, would these individuals also have lower equivalent income? If so, the maximin social welfare function would prioritise them, potentially reversing the policy recommendation.

3. Can the RURO model be extended to allow $\pi_0$ and $\pi_1$ to vary independently (relaxing $\pi_0 + \pi_1 = 1$)? This would require additional identification restrictions but would eliminate the zero-sum between market and non-market opportunities.

4. The paper uses type-specific unemployment rate as an exclusion restriction. Can vacancy data or regional labour demand indicators provide sharper instruments for identifying $q$ from preferences?

# Challenge to this paper

The $\pi_0 + \pi_1 = 1$ normalisation creates a fundamental identification problem: any increase in job offer intensity mechanically reduces non-market opportunities. This means the "equalising opportunities" counterfactual (giving everyone the $\pi_1$ of a 30-year-old) simultaneously removes non-market options from elderly individuals who may genuinely value them. The paper acknowledges this (p. 50) but does not resolve it. For welfare analysis, this is problematic: equivalent income should reflect the value of the individual's *actual* opportunity set, not a counterfactual set that simultaneously expands one dimension and contracts another. My JMP's framework $W(z, R, A; y)$ should define $A$ more carefully to avoid this confound -- perhaps by modelling job offers and non-market options as independent processes with separate intensities.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The RURO model's decomposition $U = V(c, \ell; \mathbf{x}_v) \cdot \varepsilon(s)$ with opportunity density $q \cdot g_1 \cdot g_2$ is the structural foundation for my framework's $W(z, R, A; y)$. The systematic utility $V$ corresponds to preferences $R$, the opportunity structure $(q, g_1, g_2)$ corresponds to the feasible set $A$, and the tax-benefit function $f$ corresponds to the pay schedule $y$.

[Reasonable inference for my project] The paper's finding that opportunities operate primarily through the extensive margin while preferences affect both margins suggests that the welfare effect of opportunity constraints (the $A$ dimension) is primarily about whether people can participate at all, not about the hours they work conditional on participation. This has implications for equivalent-income calculation: the reference wage $\tilde{w}$ should be chosen to capture participation constraints.

[Unclear from paper] Whether the RURO model's opportunity structure is rich enough to capture the key welfare-relevant variation in $A$. The paper models $g_1$ and $g_2$ as common distributions (varying only by education, experience, sex), while $q$ varies by age, region, etc. My JMP may need richer individual-level variation in the opportunity density.

# Relation to Bargain et al. (2013)

Direct methodological comparison. Bargain et al. (2013) use standard discrete-choice models (Van Soest 1995 type) that assume all individuals face the same choice set (hours categories at a fixed wage). Capéau and Decoster estimate a RURO model where the choice set varies across individuals through $q(\mathbf{x}_q)$. The RURO model attributes some of what the standard model ascribes to preferences to differences in opportunities. This means the equivalent-income welfare measures in Bargain et al. may be biased by not accounting for demand-side constraints.

# Relation to opportunities vs preferences

This paper is *the* key reference for the preferences-vs-opportunities distinction. The entire analysis is built around this decomposition. The RURO model structurally separates the preference component $V(c, \ell; \mathbf{x}_v)$ from the opportunity component $(q, g_1, g_2)$, allowing counterfactual experiments that vary one while holding the other constant. The key empirical finding -- that opportunities matter at least as much as preferences for explaining age-related participation declines, and operate through different margins -- validates the theoretical motivation for separating $R$ and $A$ in the welfare framework.

# Useful quotations / formulas

**On why standard models are insufficient (p. 3):**
"In standard random utility models also wages are exogenously fixed individual characteristics, reflecting a person's productive capacities. For several reasons, this is unattractive. Productive capacities can in many cases not be determined appropriately, when considered separately from the specific job in which these capacities are exhibited."

**On what the RURO model adds (p. 4):**
"It is exactly these type of frictions in the choice process which are taken into consideration by RURO models, as an additional factor, next to preferences, to understand choice behaviour."

**On the key counterfactual result (p. 47--48):**
"It seems as if 'equalising' differences in opportunities with respect to age, has in the first place an impact on the extensive margin, and much less so on the intensive margin of the number of hours worked."

**On the normalisation problem (p. 50):**
"It might be considered an unattractive property of the model that increasing the intensity of job offers is, by definition, mirrored by lowering the degree of availability of non-market opportunities... Indeed, why would I loose the opportunities to do what I liked most, when more jobs were offered to me?"

**On the standard model comparison (p. 16, eq. 20):**
"The difference with (19)-(19') is twofold. Firstly, in the RURO model utilities are weighted with the intensity with which alternatives are rendered available to an individual. Next, the wage is part of the job offer."

# Suggested tags

RURO, random-utility, random-opportunity, discrete-choice, job-choice, labour-supply, Poisson-process, Frechet-distribution, job-offers, opportunity-density, wage-offer-distribution, hours-distribution, ageing, elderly, preferences-vs-opportunities, extensive-margin, intensive-margin, Belgium, EU-SILC, EUROMOD, Box-Cox, counterfactual, identification, importance-sampling, Capeau, Decoster, Aaberge, Colombino, Dagsvik

# My quick takeaway

The most directly relevant paper for my JMP: a complete RURO model estimated on Belgian data, decomposing observed labour market behaviour into preferences (taste for leisure) and opportunities (job offer intensity). Key finding: declining opportunities with age are at least as important as increasing leisure preference for explaining lower participation of the elderly, with opportunities operating through the extensive margin and preferences through both margins. For my welfare analysis, this paper provides (a) the structural model I build on, (b) the identification strategy I need to adapt, (c) the key empirical finding that demand-side constraints matter, and (d) a warning about the $\pi_0 + \pi_1 = 1$ normalisation that can confound welfare comparisons. The paper lacks the welfare analysis (equivalent income) that my JMP adds.
