---
title: "Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification"
authors: [John K. Dagsvik, Zhiyang Jia]
year: 2016
outlet: "Journal of Applied Econometrics, 31(3), 487--506"
country_or_context: "Norway"
population: "Married/cohabiting couples"
data_period: "1997 (Norwegian Labor Survey)"
shelf: "RURO model / identification / latent jobs / unobserved heterogeneity / labour supply"
tags: [latent-jobs, RURO, identification, nonparametric, opportunity-measure, opportunity-density, wage-heterogeneity, hours-restrictions, Poisson, multiplicative-utility, Box-Cox, labour-supply, couples, Norway, policy-simulation]
priority: "high"
read_status: "extracted"
---

# Full citation

Dagsvik, J. K., & Jia, Z. (2016). Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification. *Journal of Applied Econometrics*, 31(3), 487--506.

# One-sentence contribution

Provides a formal identification analysis of the latent job choice model of labour supply, showing that the model is in general not nonparametrically identified -- $v(C,h)$ is identified only up to a multiplicative function of hours, and $g_1(h)$ and $\delta(h)$ are not separately identified -- but that under Box-Cox utility and additional functional form assumptions, full identification is achieved; compares two models of wage heterogeneity (across jobs vs. across individuals) on Norwegian couples data, finding that the individual-specific wage model fits better.

# Why this paper matters

The latent job choice (RURO) framework is increasingly used for labour supply analysis, but its identification properties had not been formally analysed. This paper fills that gap, showing precisely what is and is not identified from cross-sectional data on hours, wages, and non-labour income. The key negative result -- that preferences $v(C,h)$ and the opportunity measure $\theta g_1(h) g_2(w|h)$ cannot be separately nonparametrically identified -- is fundamental for understanding the limitations of RURO models and for interpreting the decomposition results in papers like Capéau et al. (2016). The positive results show that under specific (but standard) parametric assumptions, identification is restored.

# Core research question

Under what conditions is the latent job choice model nonparametrically or parametrically identified from cross-sectional data on hours of work, wages, non-labour income, and individual characteristics? And how does the specification of wage heterogeneity (across jobs vs. across individuals) affect model fit and identification?

# Economic setting and context

Norway 1997. High female part-time work (>35% of married women work 20--30 hours/week, ~40% full-time). Norwegian working environment legislation supports voluntary part-time. Public health sector is a major employer of part-time women. The institutional setting motivates the RURO model: part-time positions may be the only positions offered by some employers, so hours are restricted by the demand side.

# Model / theoretical framework

**Utility:** $U(C, h, z) = v(C, h) \varepsilon(z)$ (Assumption 1)
where $v(\cdot)$ is a positive deterministic function, $\varepsilon(z)$ are i.i.d. random taste shifters for each job $z$, $C$ is disposable income, $h$ is hours. Multiplicative separability is crucial for tractability and the IIA property.

**Budget constraint:** $C = f(hw, I)$ where $f(\cdot)$ is the net-of-tax function, $w$ is wage, $I$ is non-labour income.

**Random opportunities (Assumption 2):** Job offers arrive as an inhomogeneous Poisson process:
- Non-market opportunities: intensity $\varepsilon^{-2}$
- Market opportunities: intensity $\theta \varepsilon^{-2}$, where $\theta > 0$ is the relative job availability parameter
- Available jobs are distributed on $D \times (0, \infty)$ according to joint density $g_1(h) g_2(w|h)$

**Choice probability (Theorem 1):** For $h > 0$:
$$\varphi(h, w | I) = \frac{v(f(hw, I), h) \theta g_1(h) g_2(w|h)}{v(f(0, I), 0) + \theta \sum_{r \in D} \int_0^\infty v(f(ry, I), r) g_1(r) g_2(y|r) \, dy}$$

Non-participation:
$$\varphi(0, 0 | I) = \frac{v(f(0, I), 0)}{v(f(0, I), 0) + \theta \sum_{r \in D} \int_0^\infty v(f(ry, I), r) g_1(r) g_2(y|r) \, dy}$$

**Two models of wage heterogeneity:**
- **Model 1 (Aaberge et al. 1995, 1999):** $\eta = \psi(\cdot) = 0$. All observationally identical individuals face the same wage offer distribution. Wage variation across jobs ($\xi(z)$) represents job-specific variation.
- **Model 2:** $\xi(z) = 0$. Each individual faces a single offered wage determined by individual characteristics plus a person-specific random effect $\eta$. Wage variation is inter-individual, not inter-job.

**Wage equation (general, eq. 4):** $\log W(z) = \alpha + \psi(H(z)) + \eta + \xi(z)$

**Extended model (eq. 3a,b):** With random effect $\eta$:
$$\varphi(h, w | I) = E_\eta\left[\frac{v(f(hw, I), h) \theta(\eta) g_1(h) g_2(w|h;\eta)}{v(f(0, I), 0) + \theta(\eta) \sum_{r \in D} \int_0^\infty v(f(ry, I), r) g_1(r) g_2(y|r;\eta) \, dy}\right]$$

# Key objects

- **$v(C, h)$:** Deterministic/systematic utility -- the identified target of the identification analysis.
- **$\theta$:** Relative job availability -- ratio of market to non-market opportunities. Can depend on individual characteristics; $\theta < 1$ means fewer attractive market than non-market opportunities.
- **$g_1(h)$:** Probability that a job has offered hours $h$ -- the hours offer distribution.
- **$g_2(w|h)$:** Conditional wage offer density given hours $h$.
- **$\theta g_1(h) g_2(w|h)$:** The "opportunity measure" -- the joint density of available $(h,w)$ jobs.
- **$\delta(h)$:** An unknown multiplicative function of hours that cannot be separated from $v(C,h)$ nonparametrically.
- **$r(I)$:** A function of non-labour income related to the marginal utility of consumption at $h=0$; identified from data.

# Data

Norwegian Labor Survey 1997. Sample: married/cohabiting couples with both partners aged 25--64, not self-employed, not students. 2,515 households total (2,254 both working, 256 only husband, 5 only wife).

**Key statistics (Table I):**
- Men: mean age 45, education 12.6 years, experience 25.5 years, wage rate NOK 153.82/hour, hours 38.43/week
- Women: mean age 42.8, education 12.1 years, experience 23.7 years, wage rate NOK 120.12/hour, hours 30.45/week
- Non-labour income: NOK 6,320 (both working)

Eight feasible annual hours: 0, 208, 624, 1040, 1456, 1950, 2340, 2600.

# Identification logic

**Fundamental equation (eq. 7):** From Theorem 1, for positive $h$:
$$\frac{\varphi(h, w | I)}{\varphi(0, 0 | I)} = \frac{v(f(hw, I), h) \theta g_1(h) g_2(w|h)}{v(f(0, I), 0)}$$

The LHS is observable. The RHS contains both preferences ($v$) and opportunities ($\theta g_1 g_2$). The identification challenge: can $v$ and $\theta g_1 g_2$ be separately recovered?

**Theorem 2 (negative result):** Under Assumptions 1--3 only, $v(C,h)$ can be expressed as $v(C,h) = \zeta(C)^{r} \lambda^*(C,h) \delta(h)$ for $h > 0$, where $\zeta(C)$ and $\lambda^*(C,h)$ are identified but $r$ is an unknown constant and $\delta(h)$ is an unknown function of $h$. So $v(C,h)$ is identified only up to a multiplicative function of hours.

**Key insight:** Non-labour income $I$ enters only through consumption $C = f(hw, I)$, generating variation in $C$ while holding $h$ and $w$ fixed. This variation identifies the "shape" of $v$ in $C$ at each $h$, but the "level" across different $h$ values is not pinned down.

**Theorem 3:** Under additional independence of wages and hours (Assumption 4), the distribution of offered hours $g_1(h)$ is identified, but $\delta(h)$ is still not identified. For policy simulations that only change taxes/wages (not the opportunity distribution), separate identification of $\delta(h)$ and $g_1(h)$ is not necessary.

**Theorem 4 (positive result):** Under Box-Cox utility (eq. 8, Assumption 6) plus a regularity condition (Assumption 5: marginal net of tax rate constant in a neighbourhood), the model is fully identified.

**Theorem 5:** Extends identification to the case with unobserved individual heterogeneity $\eta$ in the wage offer distribution (Model 2). Under Assumptions 1--4, 7--8, $v(C,h)$ is identified up to a multiplicative constant and the wage distribution conditional on $\eta$ is identified.

**Desired hours as an alternative:** If desired hours data are available, preferences can be identified directly since "job choice constraints are irrelevant" (footnote 4, citing Bloemen 2008). Then opportunities can be backed out from observed behaviour.

# Estimation / empirical strategy

**Three-stage estimation:**
1. Reduced-form participation probability
2. Heckman-corrected wage equations (separate for Model 1 and Model 2)
3. Maximum likelihood of the structural labour supply model with predicted wages

**Functional forms:**
- Box-Cox utility (eq. 8): $\log v(C,h) = \gamma_1(C^\alpha - 1)/\alpha + \gamma_2((1-h/M)^\beta - 1)/\beta + \gamma_3(C^\alpha - 1)((1-h/M)^\beta - 1)/\alpha\beta$
- $\theta_F$ and $\theta_M$ linear in years of schooling $S$
- Hours offer density $g_{1k}(h)$: uniform except for peaks at part-time (1040h = 20h/week) and full-time (1950h = 37.5h/week)
- Model 1: $\xi(z) \sim N(0, \sigma_\xi^2)$ across jobs; Model 2: $\eta \sim N(0, \sigma_\eta^2)$ across individuals

**Model comparison:** Pseudo-$R^2$ (McFadden's $\rho^2$): Model 1 = 0.49, Model 2 = 0.50. Andrew's chi-square test (6 cells): Model 1 = 57.6 (rejects at 5%), Model 2 = 10.4 (passes). Model 2 is the maintained model.

# Treatment of preferences

Preferences modelled via Box-Cox utility with consumption-leisure interaction. Key findings:
- $\log v(C,h)$ is strictly increasing and concave in consumption and leisure for both models
- Marginal utility of leisure for women decreases until age ~35 then increases
- Children significantly affect women's leisure preference, not men's
- Women take more responsibility for children within the household
- The model provides a "theoretical rationale" for hours dummies in standard discrete-choice models (van Soest 1995): what appear as preference peaks at part-time and full-time hours are actually demand-side constraints captured by the opportunity measure

# Treatment of opportunities / constraints

This is the paper's distinguishing feature:
- **$\theta$:** For both genders, estimated to be less than 1, meaning "the number of interesting and available jobs is smaller than the number of interesting non-market opportunities"
- **$\theta_F$:** Depends positively on schooling for women (more education = more job offers)
- **$\theta_M$:** Not significant for men (very few non-participants)
- **$g_1(h)$:** Full-time peak "substantially higher" for men than women; part-time peak higher for women. Gender-specific hours offer distributions reflect institutional differences.
- **Simulation (Section 4.3, Figure 3):** Removing the part-time peak and replacing with full-time jobs: significant shift from part-time to full-time for women, men barely affected. Demonstrates the RURO model's ability to simulate demand-side reforms that standard models cannot.

# Welfare / normative object

No welfare analysis. The paper focuses on identification and positive analysis (elasticities, model fit, policy simulation).

# Main findings

**Identification (Section 3):**
1. Without parametric restrictions, $v(C,h)$ is identified only up to a multiplicative function of $h$ (Theorem 2)
2. The opportunity measure is nonparametrically unidentified (but $g_1(h)$ is identified under wage-hours independence, Theorem 3)
3. Separate identification of $\delta(h)$ and $g_1(h)$ is unnecessary for simulating tax/wage changes
4. Box-Cox utility + regularity conditions restore full identification (Theorem 4)
5. With unobserved individual wage heterogeneity, identification extends under additional exclusion restrictions (Theorem 5)

**Empirical (Section 4):**
6. Model 2 (individual-specific wages) fits better than Model 1 (job-specific wages): passes Andrew's test, Model 1 does not
7. Gross wage elasticities (Table II, Model 2):
   - Women's participation w.r.t. own wage: 0.33; cross (husband's): −0.17
   - Men's participation w.r.t. own wage: 0.01; cross (wife's): −0.007
   - Women's unconditional hours w.r.t. own wage: 0.62; men's: −0.02
8. Labour supply curves are highly nonlinear -- elasticities decrease with wage level (Figure 2)
9. Removing part-time peak from women's opportunity distribution: significant shift from part-time to full-time (Figure 3), demonstrating demand-side simulation

# Main limitations

- Cross-sectional data only -- cannot exploit panel variation
- Measurement error in hours ("division bias" from weekly hours × weeks, no overtime data)
- Independence of wages and hours (Assumption 4) may not hold -- wage-hours correlation could be important
- No welfare analysis despite having separate preference and opportunity estimates
- Joint model for couples but does not allow for intra-household bargaining
- Small sample of non-working men (5 observations of "only wife working")
- Sector-specific preferences and restrictions not modelled

# Relevance for my JMP

## possible use for framing
The paper provides the definitive statement of the identification problem in RURO models: $v(C,h)$ and $g_1(h)$ are not separately nonparametrically identified. This is the fundamental challenge for the $W(z,R,A;y)$ framework: if $R$ (preferences) and $A$ (opportunities) cannot be separately identified, then welfare decompositions into $R$ and $A$ components are only valid under the parametric assumptions imposed.

## possible use for model design
The two-model comparison (Model 1 vs. Model 2) directly informs my modelling choices. Model 2 (individual-specific wages, $\xi(z)=0$) fits better and has cleaner identification. The three-stage estimation procedure is a practical template. The Box-Cox utility specification (eq. 8) is the standard choice for RURO applications.

## possible use for identification
Theorems 2--5 are the identification results I need to cite and build upon. The key constructive insight: for simulating tax/wage changes, separate identification of $\delta(h)$ and $g_1(h)$ is unnecessary. But for welfare analysis (comparing utility levels), the unidentified $\delta(h)$ matters -- it affects the level of $v(C,h)$ at different hours, which matters for welfare comparisons across individuals choosing different hours.

## possible use for policy simulation
The hours-distribution reform simulation (Section 4.3, Figure 3) demonstrates that RURO models can simulate demand-side reforms that standard models cannot: removing the part-time peak from the opportunity distribution and replacing with full-time. This is exactly the kind of $A$-channel simulation my JMP should perform.

# Research questions this paper inspires

1. The non-identification of $\delta(h)$ means that welfare comparisons across individuals at different hours levels are not nonparametrically identified. Can Bhattacharya's (2015) or Capéau et al.'s (2021) nonparametric welfare results be applied to the RURO setting despite this limitation?

2. The paper shows Model 2 (individual-specific wages) fits better than Model 1 (job-specific wages). In a welfare framework, these models have different implications: Model 1 implies wage variation is an attribute of the opportunity set $A$, while Model 2 makes it a characteristic of the individual. Which interpretation is correct for welfare analysis?

3. Can the identification problem be resolved using desired hours data (as suggested in footnote 4, citing Bloemen 2008)? If desired hours identify preferences, then $g_1(h)$ can be backed out from observed behaviour, restoring separate identification.

4. The simulation of removing the part-time peak (Figure 3) assumes $\theta_F$ is unchanged. But if part-time jobs are replaced by full-time jobs, might total job availability change? An equilibrium extension would be needed.

# Challenge to this paper

The paper's central identification result -- that $v(C,h)$ and $g_1(h)$ are not separately nonparametrically identified -- means that the entire preference-opportunity decomposition in RURO models rests on parametric assumptions (Box-Cox utility, specific hours density parameterisation). The paper candidly acknowledges this but does not assess how sensitive the decomposition is to alternative parametric specifications. The finding that Model 2 fits better than Model 1 is based on a specific chi-square test over 6 cells -- a relatively coarse evaluation. Moreover, the paper's approach to measurement error in hours (three-stage estimation to remove "division bias") addresses the correlation between observed wage and hours but does not eliminate the underlying measurement error, which the authors acknowledge "may still be a problem in the last-stage maximum likelihood estimation" (p. 496).

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The model separates utility $v(C,h)$ (preferences $R$) from the opportunity measure $\theta g_1(h) g_2(w|h)$ (opportunity set $A$). The identification analysis shows precisely what can and cannot be recovered about each component.

[Reasonable inference for my project] The non-identification of $\delta(h)$ means that welfare comparisons using $v(C,h)$ across different hours levels are not robust to the parametric specification. For the $W(z,R,A;y)$ framework, this implies that money-metric welfare measures that compare utility at different $(C,h)$ points are identified only under the maintained parametric form. This is a fundamental caveat for welfare analysis using RURO models.

[Unclear from paper] Whether the non-identification of $\delta(h)$ affects welfare measures that are defined in terms of choice probabilities (Bhattacharya 2015, Capéau et al. 2021) rather than in terms of the structural utility function. If welfare can be computed from choice probabilities alone (as those papers show for standard DC-RUMs), then the non-identification of $v(C,h)$ may be irrelevant -- but the RURO model's choice probabilities depend on both $v$ and the opportunity measure, so the connection is not straightforward.

The paper is closest to: **identification theory for RURO models** and **structural foundations for preference-opportunity decomposition**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) use a standard discrete-choice model (van Soest 1995) where the "opportunity set" is the full budget set -- all hours are available. Dagsvik and Jia (2016) show that when hours are restricted (RURO), the identification problem fundamentally changes: preferences and opportunities cannot be separately recovered nonparametrically. This means that Bargain et al.'s welfare metrics, which treat all labour supply variation as preference-driven, may confound $R$ and $A$ effects. The RURO model's explicit opportunity measure provides a framework for disentangling them -- but only under parametric assumptions.

# Relation to opportunities vs preferences

This paper is the definitive statement on the separability of preferences and opportunities in RURO models. The answer: they are NOT separately nonparametrically identified. The product $v(C,h) \cdot g_1(h)$ is identified (through eq. 7 and Theorem 2), but the individual factors are not. Parametric assumptions (Box-Cox for $v$, piecewise uniform for $g_1$) are needed to separate them. This means that the $R$ vs. $A$ decomposition in $W(z,R,A;y)$ is inherently model-dependent in the RURO framework.

# Useful quotations / formulas

**Choice probability (eq. 2a):**
$$\varphi(h,w|I) = \frac{v(f(hw,I),h)\theta g_1(h)g_2(w|h)}{v(f(0,I),0) + \theta\sum_{r\in D}\int_0^\infty v(f(ry,I),r)g_1(r)g_2(y|r)\,dy}$$

**Fundamental identification equation (eq. 7):**
$$\frac{\varphi(h,w|I)}{\varphi(0,0|I)} = \frac{v(f(hw,I),h)\theta g_1(h)g_2(w|h)}{v(f(0,I),0)}$$

**Non-identification result (Theorem 2):**
"$v(C,h) = \zeta(C)^r \lambda^*(C,h)\delta(h)$ for $h > 0$, where $\zeta(C)$ and $\lambda^*(C,h)$ are identified but $r$ is an unknown constant and $\delta(h)$ an unknown function of $h$."

**On desired hours and identification (p. 492):**
"If available, information on desired hours of work could be used to identify preferences, since job choice constraints are irrelevant in this case."

**Box-Cox utility (eq. 8):**
$$\log v(C,h) = \gamma_1\frac{C^\alpha - 1}{\alpha} + \gamma_2\frac{(1-h/M)^\beta - 1}{\beta} + \gamma_3\frac{(C^\alpha-1)((1-h/M)^\beta-1)}{\alpha\beta}$$

**On theoretical rationale for hours dummies (p. 495):**
"An advantage with our framework is that it provides a theoretical rationale for introducing such dummies, in contrast to the conventional discrete-choice labor supply model."

**On model comparison (p. 498):**
"Model 2 fits the data better than Model 1 and we therefore select Model 2 as our maintained model."

**On $\theta$ (p. 497):**
"$\theta$ is estimated to be less than 1 ... this can be interpreted as indicating that the number of interesting and available jobs is smaller than the number of interesting non-market opportunities."

# Suggested tags

latent-jobs, RURO, identification, nonparametric-identification, opportunity-measure, opportunity-density, wage-heterogeneity, hours-restrictions, Poisson, multiplicative-utility, Box-Cox, labour-supply, couples, Norway, policy-simulation, hours-peaks, part-time, full-time, demand-side

# My quick takeaway

This is the key identification paper for RURO models. Its central result -- that $v(C,h)$ and $g_1(h)$ are not separately nonparametrically identified from cross-sectional data -- is the fundamental caveat for any welfare analysis using RURO models, including my JMP. The implication: the $R$ vs. $A$ decomposition in $W(z,R,A;y)$ is only as credible as the parametric assumptions used to achieve identification (Box-Cox for preferences, piecewise uniform for hours offers). The positive side: for tax/wage simulations, separate identification is unnecessary (changes operate through $C$ and therefore through the identified parts of $v$). But for welfare comparisons across individuals at different hours levels, the unidentified $\delta(h)$ matters. The empirical finding that Model 2 (individual-specific wages) dominates Model 1 (job-specific wages) is also important for my specification choices.
