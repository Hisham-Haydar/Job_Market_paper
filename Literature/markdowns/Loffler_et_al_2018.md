---
title: "The Sensitivity of Structural Labor Supply Estimations to Modeling Assumptions"
authors: [Max Löffler, Andreas Peichl, Sebastian Siegloch]
year: 2018
outlet: "ifo Working Paper No. 259"
country_or_context: "Germany (main), United States (robustness)"
population: "Working-age adults (17--65), five demographic subgroups: single men, single women, couples (male flexible, female flexible, both flexible)"
data_period: "2008 SOEP (German Socio-Economic Panel), 2007 tax system; robustness: 2007 IPUMS-CPS (US)"
shelf: "structural labour supply / discrete choice / sensitivity analysis / wage imputation / elasticities / meta-analysis"
tags: [structural-labour-supply, discrete-choice, sensitivity-analysis, wage-imputation, prediction-error, elasticity, extensive-margin, intensive-margin, meta-analysis, translog, quadratic, Box-Cox, fixed-costs, hours-restrictions, unobserved-heterogeneity, SOEP, Germany, Loffler, Peichl, Siegloch]
priority: "high"
read_status: "extracted"
---

# Full citation

Löffler, M., Peichl, A. and Siegloch, S. (2018). The Sensitivity of Structural Labor Supply Estimations to Modeling Assumptions. *ifo Working Paper*, No. 259, ifo Institute, Munich.

# One-sentence contribution

Estimates 3,456 different structural discrete-choice labour supply models on the same German data (and replicates on US data), finding that elasticity estimates are robust to utility function specification, preference heterogeneity, and hours restrictions, but are highly sensitive to the treatment of wages -- specifically whether predicted wages are used for non-workers only or the full sample, and whether the wage prediction error is integrated out, with elasticities ranging from 0.2 to 0.65 depending on these choices.

# Why this paper matters

This paper is the first systematic "controlled meta-analysis" of structural discrete-choice labour supply models, isolating the marginal impact of each modelling assumption on estimated elasticities while holding everything else constant. The key finding -- that the wage imputation procedure matters far more than the utility function specification -- is a critical warning for the entire structural labour supply literature, including the RURO-type models used in my JMP. It directly affects the reliability of welfare analyses that depend on estimated preferences (e.g., Bargain et al. 2013).

# Core research question

How sensitive are estimated labour supply elasticities from structural discrete-choice models to the many modelling assumptions researchers make, and which assumptions matter most?

# Economic setting and context

The paper addresses the long-standing puzzle of why labour supply elasticity estimates vary so much across studies, even for the same country and time period. While differences across countries or between micro and macro estimates have been attributed to frictions and adjustment costs, within-country variation in micro estimates from structural models remains unexplained. The paper systematically varies modelling choices to identify which ones drive elasticity estimates.

# Model / theoretical framework

**General discrete-choice model:** Individual $n$ chooses job type $j \in J_n$ to maximise:
$$\max_{j \in J_n} U(C_{nj}, L_j, \epsilon_{nj}) = \max_{j \in J_n} \varphi(C_{nj}, L_j | \mathbf{x}_{nj}, \boldsymbol{\beta}_n, \gamma_j) + \epsilon_{nj}$$
where $C_{nj}$ = consumption, $L_j = T - h_j$ = leisure, $\epsilon_{nj} \sim$ Type I extreme value (iid). Consumption $C_{nj} = f[w_{nj} h_j, I_n | \mathbf{x}_{nj}]$ via tax-benefit system $f[\cdot]$.

**Choice probability (with opportunity density):**
$$P(U_{ni} > U_{nj}, \forall j \neq i) = \frac{\exp(v[C_{ni}, L_i | \mathbf{x}_{ni}, \boldsymbol{\beta}_n]) \cdot g(i | \mathbf{x}_{ni}, \gamma_i)}{\sum_{s \in J_n} \exp(v[C_{ns}, L_s | \mathbf{x}_{ns}, \boldsymbol{\beta}_n]) \cdot g(s | \mathbf{x}_{ns}, \gamma_s)}$$
where $v(\cdot)$ = systematic utility and $g(\cdot)$ = frequency/availability of job type $j$ (captures fixed costs, hours restrictions).

**Simulated log-likelihood (mixed logit):**
$$\ln(SL) = \sum_{n=1}^{N} \ln \left( \frac{1}{R} \sum_{r=1}^{R} \frac{\exp(v_{ni}[\cdot | \hat{w}_{ni}^{(r)}, \boldsymbol{\beta}_n^{(r)}]) \cdot g(i | \gamma_i^{(r)})}{\sum_{j \in J_n} \exp(v_{nj}[\cdot | \hat{w}_{nj}^{(r)}, \boldsymbol{\beta}_n^{(r)}]) \cdot g(j | \gamma_j^{(r)})} \right)$$
integrating over distributions of $(\boldsymbol{\beta}_n, \gamma)$ and $\hat{w}_{nj}$.

**Three broad categories of modelling assumptions tested:**

1. **Utility function specification:**
   - Functional form: translog (reference), quadratic, Box-Cox
   - Observed heterogeneity: none, in $\beta_C$ only, in $\beta_L$ only, in both
   - Unobserved heterogeneity: none, random $\beta_C$, random $\beta_L$, random both, random both with correlation
   - Welfare stigma: yes/no

2. **Choice set and constraints:**
   - Hours restrictions: none, part-time restrictions, fixed costs
   - Choice set: 7 categories (0, 10, 20, 30, 40, 50, 60 hours/week)

3. **Wage treatment:**
   - Imputation sample: non-workers only vs. full sample
   - Wage prediction error: ignored, 1 random draw, integrated out (5 or 10 Halton draws)
   - Selection correction: yes/no (Heckman)

**Exogeneity assumptions (eq. 5):**
$$E[\boldsymbol{\beta}_n w_{nj} | \mathbf{x}_{nj}] = 0, \quad E[\gamma_j w_{nj} | \mathbf{x}_{nj}] = 0$$
Preferences and labour market conditions are assumed independent of wages conditional on observables.

# Key objects

- **Own-wage elasticity:** simulated response to a 10% increase in hourly wage rates, decomposed into extensive margin (participation) and intensive margin (hours conditional on participation)
- **AIC (Akaike Information Criterion):** statistical fit measure; lower = better
- **Meta-regression coefficients (Table 4):** standardised marginal effects of each modelling assumption on AIC and on extensive/intensive/total elasticities
- **3,456 model specifications:** full factorial combination of all modelling choices

# Data

**Germany (main):** 2008 wave of SOEP (German Socio-Economic Panel), ~24,000 individuals in ~11,000 households. Tax system of 2007 simulated via IZA$\Psi$MOD (v3.0.0). Sample: ages 17--65, excluding self-employed, civil servants, military, retirees, students, disability beneficiaries. Five subgroups: 779 single males, 1,065 single females, 688 couples (male flexible), 1,042 couples (female flexible), 3,099 couples (both flexible).

**US (robustness):** March 2007 IPUMS-CPS, with NBER's TAXSIM for tax simulation.

# Identification logic

Not causal identification of a treatment effect. The paper exploits controlled variation across model specifications on the same data. By estimating 3,456 models on identical data and regressing the resulting elasticities on modelling-choice dummies, the paper isolates the marginal contribution of each modelling assumption to the estimated elasticity (a "controlled meta-analysis"). The identification of labour supply elasticities within each model relies on the standard discrete-choice assumptions: variation in wages $w_{nj}$, non-labour income $I_n$, and the nonlinear tax-benefit function $f(\cdot)$.

# Estimation / empirical strategy

Maximum simulated likelihood (MSL) using Halton sequences for the integration over random coefficients and wage prediction errors. Tax-benefit system approximated by a flexible second-degree polynomial mapping gross earnings to disposable income ($R^2 > 0.99$ for most groups, 0.97 for single women). Elasticities computed by simulating individual responses to a 10% wage increase and aggregating. Meta-regression: OLS of standardised outcomes (AIC, elasticities) on dummies for each modelling choice, with labour supply type fixed effects, $R^2 \approx 0.85$--$0.88$.

# Treatment of preferences

Preferences are modelled through the systematic utility function $v(C, L)$, which can take translog, quadratic, or Box-Cox form. Preference heterogeneity enters through: (a) observed characteristics (age, children, region, etc.) interacted with consumption and/or leisure coefficients; (b) unobserved heterogeneity via random coefficients (normal distribution) on consumption and/or leisure. The key finding is that these preference-side modelling choices have only minor effects on estimated elasticities. The functional form, the degree of observed heterogeneity, and the inclusion of unobserved heterogeneity produce elasticity differences that are small and often statistically insignificant.

# Treatment of opportunities / constraints

The opportunity set is modelled through: (a) the choice set (7 hours categories including non-participation); (b) the $g(j)$ function capturing availability of job types, operationalised as fixed costs of working or part-time hours restrictions. Fixed costs and hours restrictions improve fit (lower AIC) and tend to increase extensive-margin elasticities, but the effects on total elasticities are modest. The paper notes that Aaberge et al. (1995) provide a micro foundation for $g(j)$ through latent job offers that differ in availability, wages, and non-monetary attributes -- but this RURO approach is not tested in the meta-analysis.

# Welfare / normative object

No welfare analysis is conducted. The paper focuses entirely on the positive question of how modelling assumptions affect estimated elasticities and goodness of fit. However, the findings have direct welfare implications: since estimated elasticities feed into optimal tax formulas (e.g., Diamond and Saez 2011), the sensitivity of elasticities to wage treatment means that welfare conclusions from structural models are also sensitive.

# Main findings

1. **Utility function specification does not matter much (Table 4):** Switching from translog to quadratic increases extensive elasticity by 0.12 SD but has no significant effect on total elasticity. Box-Cox increases intensive elasticity by 0.08 SD. These are small effects.

2. **Observed preference heterogeneity has small effects:** Including heterogeneity in both $\beta_C$ and $\beta_L$ has no significant effect on total elasticity. Some small increases in extensive elasticity from consumption-side heterogeneity.

3. **Unobserved heterogeneity does not matter:** Random coefficients (any specification) produce no statistically significant changes in total elasticity. Adding correlation between random coefficients slightly reduces total elasticity by 0.10 SD.

4. **Fixed costs and hours restrictions improve fit but modestly affect elasticities:** Part-time restrictions increase extensive elasticity by 0.38 SD and total by 0.15 SD. Fixed costs increase extensive by 0.48 SD and total by 0.24 SD. These are the largest effects among non-wage modelling choices.

5. **Wage imputation is the critical modelling choice (Table 4, largest effects):**
   - *Full sample, no error correction:* increases total elasticity by **2.24 SD** relative to reference (non-workers only imputation). This is the dominant finding.
   - *Full sample, error integrated out:* increases total elasticity by **1.41 SD**.
   - *Full sample, 1 random draw:* no significant effect (random draw approximately cancels out the full-sample effect).
   - *Non-workers, error integrated out:* no significant effect on total elasticity.
   - Average own-wage elasticity ranges from **0.23** (observed wages for workers, predicted for non-workers) to **0.46** (predicted wages for all, no error correction) to **0.65** (predicted for all, ignoring prediction error) vs. **0.35** (predicted for all, error integrated out).

6. **Welfare stigma improves fit but does not affect elasticities:** Including stigma from welfare participation substantially improves AIC (0.97 SD) but has no significant effect on any elasticity measure.

7. **Results replicated on US data (Table A.1):** Qualitatively identical findings using CPS data and TAXSIM. Wage treatment remains the dominant factor.

8. **Policy implication (p. 3):** An elasticity of 0.25 (from one wage procedure) implies an optimal top marginal tax rate of 72.7% (Diamond and Saez 2011 formula), while an elasticity of 0.65 (from another wage procedure) implies 50.6%. The wage imputation choice can shift optimal tax rates by over 20 percentage points.

# Main limitations

- Working paper (not yet peer-reviewed as of 2018)
- Only discrete-choice models; does not cover continuous (Hausman-type) models
- Does not vary the number of choice categories (fixed at 7) or the choice set definition, though the paper cites evidence this matters little
- Does not model the RURO/latent-jobs framework (Aaberge et al. 1995, Dagsvik et al. 2014) as one of the modelling variants, despite noting it as a micro foundation for $g(j)$
- Wage exogeneity assumption (eq. 5) is maintained throughout; Löffler et al. (2014) show this matters but it is not tested here
- The meta-regression treats all modelling choices as additive; interaction effects between choices are not explored
- German institutional context (2007 tax system) may not generalise

# Relevance for my JMP

## directly relevant for understanding sensitivity of RURO-type model estimates
My JMP uses a structural discrete-choice model (RURO variant) to estimate preferences and compute welfare (equivalent income). This paper shows that the estimated preferences -- and hence the welfare analysis -- are highly sensitive to how wages are treated. Since the RURO model involves wage imputation for latent jobs (not just for non-workers), the sensitivity is potentially even greater. This paper suggests I should conduct extensive sensitivity analysis on the wage treatment in my model and report how welfare conclusions change.

## directly relevant for the choice between model specifications
The paper provides evidence that utility function choice (translog vs. quadratic vs. Box-Cox) and heterogeneity modelling matter little for elasticities, while fixed costs/hours restrictions matter somewhat. This helps justify my modelling choices and identifies where to focus robustness checks.

## directly relevant for the wage-preference endogeneity concern
The paper notes (footnote 2, p. 3) that very few studies estimate preferences and wages simultaneously (Aaberge et al. 1995, van Soest et al. 2002, Blundell and Shephard 2012). The maintained exogeneity assumption $E[\boldsymbol{\beta}_n w_{nj} | \mathbf{x}_{nj}] = 0$ is a concern for RURO models where the opportunity density $g(h, w)$ explicitly allows wages to vary across jobs.

# Research questions this paper inspires

1. How sensitive are equivalent-income welfare measures (Bargain et al. 2013) to the wage imputation procedure? If elasticities shift from 0.2 to 0.65, the implied preferences and hence the equivalent incomes and welfare rankings may change substantially.

2. In the RURO model, wages are not imputed for a single job but for a distribution of latent job offers. Does the prediction error problem become larger or smaller when integrating over a job offer distribution rather than imputing a single wage? The RURO framework's explicit modelling of the wage distribution across latent jobs may actually help, as the prediction error is incorporated through the opportunity density $g(h, w)$.

3. The paper treats wage imputation as a "nuisance" problem. But in the RURO framework, the wage distribution is a substantive object -- it characterises the demand side. Can we design a wage imputation procedure that is consistent with the RURO model's structural interpretation of the wage distribution?

# Challenge to this paper

The paper treats all 3,456 model specifications as equally valid "plausible combinations of frequently made choices." But not all specifications are equally theoretically motivated. For instance, the RURO model of Aaberge et al. (1995) provides a structural interpretation of the $g(j)$ function that restricts the model in theory-consistent ways, while ad hoc fixed costs do not. Similarly, integrating out the wage prediction error is the theoretically correct procedure (van Soest 1995); ignoring it is simply an error. The paper's finding that "wage treatment matters most" may partly reflect that some wage treatments are incorrect (ignoring prediction errors) rather than that the treatment is inherently ambiguous. A more refined analysis would distinguish between "equally valid modelling choices" and "some choices are incorrect."

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper's general model (eq. 1--4) is a special case of the RURO framework: the choice probability in eq. (4) includes both systematic utility $v(C, L)$ and job availability $g(j)$, exactly as in the RURO model. The paper explicitly references Aaberge et al. (1995) as providing a micro foundation for this structure. The key difference: the paper treats $g(j)$ as hours restrictions or fixed costs, while the RURO model gives it a structural interpretation as the density of latent job offers.

[Reasonable inference for my project] The paper's finding that wage treatment matters most suggests that in my RURO model, the specification of the opportunity density $g(h, w)$ -- which determines how wages are distributed across latent jobs -- may be the most consequential modelling choice for welfare analysis. This is consistent with my JMP's emphasis on the demand side ($A$ in $W(z, R, A; y)$).

[Unclear from paper] Whether the sensitivity to wage treatment translates into sensitivity of welfare measures (equivalent income, social welfare) or only of elasticities. It is possible that welfare rankings are more robust than elasticities, if the preference orderings are preserved even when the scale of responses changes.

# Relation to Bargain et al. (2013)

Direct methodological connection. Bargain et al. (2013) use structural discrete-choice models to estimate preferences and compute equivalent incomes. This paper shows that the estimated preferences are sensitive to wage treatment, raising questions about the robustness of Bargain et al.'s welfare analysis. Table 2 of this paper documents the wage imputation methods used in the key papers of the literature (including Bargain et al. 2014, which uses full sample imputation with a random draw -- a procedure that this paper shows cancels out the full-sample effect and approximates the observed-wage baseline).

# Relation to opportunities vs preferences

The paper's central finding is that the *interaction* between wages and preferences (through the wage imputation procedure) drives elasticity estimates, not the preference specification alone. This resonates with the RURO framework's point that wages are not just inputs to the budget constraint but characterise the opportunity set. When predicted wages compress the wage distribution (by using the same Mincer regression for all individuals), the model must attribute more of the observed hours variation to preference variation, inflating elasticities. The RURO model, by allowing the opportunity density $g(h, w)$ to have rich wage variation, may partly address this problem by absorbing some of the wage heterogeneity into the opportunity structure rather than into preferences.

# Useful quotations / formulas

**On the main finding (abstract):**
"Our controlled meta-analysis shows that results are very sensitive to the treatment of hourly wages in the estimation. For example, different (sensible) choices concerning the modeling of the underlying wage distribution and especially the imputation of (missing) wages lead to point estimates of elasticities between 0.2 and 0.65."

**On the magnitude of the wage effect (p. 3):**
"The choice between predicting wage rates for non-workers with missing wage information only or for the full sample -- both procedures are often used in the literature -- may double the estimated labor supply elasticities, raising the average own-wage elasticity in our meta-analysis from 0.23 to 0.46."

**On the policy implication (p. 3):**
"Diamond and Saez (2011) use an elasticity of 0.25 to derive an optimal top marginal tax rate of 72.7 percent. However, an elasticity of 0.65, as often found when using alternative wage imputation procedures, reduces the optimal tax rate to 50.6 percent."

**On fixed costs as job availability (p. 7):**
"Aaberge et al. (1995) provide a micro foundation that allows a structural interpretation of fixed costs and the utility connected to certain hours alternatives. In their model, households choose between (latent) job offers that differ not only regarding the working hours, but also in terms of availability, wages, and non-monetary attributes."

**On what does not matter (p. 17):**
"The empirical specification of the systematic utility function has an impact on the statistical fit, we find only little differences in the estimated elasticities."

# Suggested tags

structural-labour-supply, discrete-choice, sensitivity-analysis, controlled-meta-analysis, wage-imputation, prediction-error, elasticity, extensive-margin, intensive-margin, translog, quadratic, Box-Cox, fixed-costs, hours-restrictions, unobserved-heterogeneity, random-coefficients, SOEP, CPS, Germany, US, Loffler, Peichl, Siegloch, RURO-relevance

# My quick takeaway

A critical methodological paper showing that in structural discrete-choice labour supply models, the wage imputation procedure matters far more than utility function specification for estimated elasticities (range 0.2 to 0.65). The key driver is whether predicted wages replace observed wages for all workers or only for non-workers, and whether the prediction error is integrated out. For my JMP, this is a direct warning: the RURO model's welfare conclusions depend on estimated preferences, which in turn depend heavily on how wages are treated. The paper justifies focusing robustness analysis on the wage/opportunity side rather than the utility function side. It also indirectly supports the RURO model's approach: by explicitly modelling the wage distribution through the opportunity density $g(h, w)$, the RURO framework may reduce the sensitivity to ad hoc wage imputation choices.
