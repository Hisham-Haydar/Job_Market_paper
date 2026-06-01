---
title: "Putting Structure on the RD Design: Social Transfers and Youth Inactivity in France"
authors: [Olivier Bargain, Karina Doorley]
year: 2013
outlet: "IZA Discussion Paper No. 7508"
country_or_context: "France"
population: "Childless single individuals aged 20--30"
data_period: "1999 (French Census), 1997--2001 (LFS), 2004--2011 (Census for validation)"
shelf: "structural labour supply / RD design / welfare programs / youth unemployment / methodology"
tags: [structural-labour-supply, regression-discontinuity, RD, RMI, RSA, social-assistance, participation, youth, France, discrete-choice, validation, counterfactual, in-work-benefits, methodology]
priority: "medium"
read_status: "extracted"
---

# Full citation

Bargain, O., & Doorley, K. (2013). Putting Structure on the RD Design: Social Transfers and Youth Inactivity in France. *IZA Discussion Paper* No. 7508.

# One-sentence contribution

Combines a regression discontinuity design with a structural discrete-choice participation model to study the disincentive effects of French social assistance (RMI) on youth employment, using the age-25 eligibility cutoff for identification, and validates the structural model by comparing its predictions for the 2009 RSA reform against actual post-reform RD estimates.

# Why this paper matters

This paper demonstrates how to bridge the credibility gap between structural and reduced-form approaches. The RD design provides clean local identification of the RMI's employment effect at the age-25 threshold, but cannot extrapolate or simulate counterfactual policies. The structural participation model, identified on the same discontinuity plus an exclusion restriction, enables extrapolation to ages away from the cutoff and to counterfactual policies (RSA reform, extending benefits to under-25s). The paper validates the structural model by showing that its predictions for the 2009 RSA reform match actual post-reform RD estimates -- a rare and valuable test of structural model credibility.

# Core research question

What is the effect of the French RMI social assistance program on youth employment, and can a structural participation model identified on the age-25 eligibility discontinuity make credible counterfactual predictions for alternative policies?

# Economic setting and context

France, 1999. The RMI (*Revenue Minimum d'Insertion*) is a last-resort social assistance benefit available to individuals aged 25+ (or under 25 with a dependent child). It provides approximately EUR 540/month to a workless single individual, with a 100% taper rate on earnings (effectively confiscatory marginal taxation). Childless singles under 25 are not eligible, creating a sharp discontinuity in financial incentives at age 25. Youth unemployment is very high in France (~25% for under-25s), especially among high school (HS) dropouts. In 2009, the RMI was replaced by the RSA (*Revenue de Solidarité Active*), which reduces the taper rate from 100% to 38%, adding an in-work benefit component.

# Model / theoretical framework

**RD design (Section 4.1):** Sharp RD exploiting the age-25 eligibility cutoff:

$$Y_i^* = \alpha_i + \gamma_i \delta(A_i) + \beta_i \cdot I(A_i \geq 25) + \varepsilon_i$$

where $Y_i$ = employment, $A_i$ = age in years/quarters, $\delta(A_i)$ = smooth function of age, $\beta_i$ = treatment effect. Local continuity (Condition 1): $E[Y_1|A]$ and $E[Y_0|A]$ are continuous at $A = 25$.

**Structural participation model (Section 4.2):** Discrete choice between non-participation ($j=0$) and full-time work ($j=1$):

$$U_{ij} = U_i(H_j, C(w_i H_j; A_i)) - F_i \cdot 1(H_j > 0) + \epsilon_{ij}$$

where $C(wH; A)$ = disposable income after taxes and benefits (including RMI if $A \geq 25$), $F_i$ = fixed cost of working, $\epsilon_{ij}$ iid EV-I.

**Flexible specification (eq. 3):**

$$U_{ij} = a_{ij} + g_{ij} \delta(A_i) + b_{ij} C(w_i H_j; A_i) + c_{ij} C(w_i H_j; A_i)^2 + \epsilon_{ij}$$

with choice-specific intercepts $a_{ij}$ and smooth age functions $g_{ij}$.

**Exclusion restriction (Condition 2):** Marginal utility of consumption $b_{ij}$ does not vary with age. Age affects utility only through: (i) the additive separable term $a_i + g_i \delta(A_i)$ (preferences/search costs), and (ii) financial incentives $C(\cdot; A_i)$ (through the RMI eligibility rule).

**Participation equation (eq. 4):**

$$Y_i^* = a_i + g_i \delta(A_i) + b_{1i} C(\tilde{w}_i H_1; A_i) - b_{0i} C(0; A_i) + \epsilon_i$$

The structural model translates the RD discontinuity from a reduced-form to an income-effect specification: the treatment effect operates through the distance between disposable income when working ($C(\tilde{w}_i H_1; A_i)$) and when not working ($C(0; A_i)$).

**Unobserved heterogeneity:** Random coefficient $b_{1i} = b_{1i}^0 + b_{1i}^1 Z_i + b_{1i}^2 u_i$ where $u_i \sim N(0, \sigma_u^2)$. Total error is a mixture of normal and EV-I. Estimated by simulated ML with Halton draws ($r = 10$).

# Key objects

- **$\beta$:** RD treatment effect -- employment drop at age 25 due to RMI eligibility
- **$b_{1i}$:** Marginal utility of income when working -- the structural parameter that converts the financial incentive change into a participation response
- **$C(wH; A) - C(0; A)$:** Financial gain from working -- the "participation tax rate" that the RMI raises to near 100%
- **Employment elasticity of social assistance:** $\frac{dY/Y}{dR/R} \approx -0.05$ (from the RD)

# Data

**1999 French Census:** 1/4 sample of French population (~14.5 million). Provides age (in days), employment status, education, gender. No income data. Selected sample: 202,093 childless singles aged 20--30.

**French Labour Force Survey (LFS):** 1/300 sample, 1990--2002. Provides wages, earnings, hours. Used for wage estimation. Pooled 1997--2001: ~10,000 observations.

**EUROMOD tax-benefit microsimulator:** Computes disposable income $C(E; A)$ under the full French tax-benefit rules for each individual at each labour supply choice.

**Census 2004--2011:** Used for external validity checks (RSA reform validation).

# Identification logic

**RD identification:** The age-25 cutoff creates a sharp discontinuity in eligibility for the RMI. Under continuity of potential outcomes at the threshold, the employment drop at 25 identifies the causal effect of RMI eligibility on employment.

**Structural identification:** The structural model is identified by: (1) the same age-25 discontinuity (exogenous variation in financial incentives $C(\cdot; A)$), and (2) the exclusion restriction that marginal utility of consumption $b_{ij}$ does not vary with age (Condition 2). This means age affects participation only through financial incentives and through an additively separable age-preference function -- not through how much people value income. This exclusion restriction allows the structural model to extrapolate away from the cutoff and to predict the effects of counterfactual policies.

**Validation:** The model is validated by comparing its prediction for the 2009 RSA reform (RMI→RSA: taper rate 100%→38%) with actual post-reform RD estimates from Census 2010--2011 data.

# Estimation / empirical strategy

1. **Wage estimation:** Heckman-corrected wage equations on LFS data, using the RMI discontinuity at 25 for the selection equation instrument. Alternatively: wage matching (draw wage from same age-education-gender cell in LFS).
2. **Tax-benefit simulation:** Compute $C(wH; A)$ and $C(0; A)$ for each Census individual using EUROMOD.
3. **RD estimation:** Logit/probit/LPM with smooth polynomial in age + treatment indicator.
4. **Structural estimation:** Simulated ML of participation model (eq. 4) with random coefficients.
5. **Validation:** Cross-validation on holdout sample; out-of-sample prediction of RSA reform effect vs. actual post-reform RD.

# Treatment of preferences

Preferences captured by choice-specific intercepts ($a_i$, $g_i \delta(A_i)$) and marginal utility of income ($b_{1i}$). The intercepts mix preference for leisure, fixed costs of working, and search costs -- these components are not separately identified (p. 15, footnote 13). Heterogeneity in $b_{1i}$ by gender, education (HS dropout dummy), and unobserved random component $u_i$. The exclusion restriction means preferences for income are age-invariant, while preferences for work/leisure vary smoothly with age.

# Treatment of opportunities / constraints

Not explicitly modelled. Non-employment is rationalised as arising from: (i) low financial gains from work (low $\nu_i$ or high $C(0;A_i)$), (ii) high preference for leisure (low $u_i$), (iii) classic unemployment (productivity below minimum wage), or (iv) frictional/cyclical unemployment ($a_i + g_i \delta(A_i)$ captures this). The paper acknowledges that $a_i + g_i \delta(A_i)$ is "a non-identified combination of supply-side factors (work disutility or work costs) and demand-side factors (job search costs)" (p. 15). This is exactly the confounding of preferences and opportunities that the RURO framework addresses.

# Welfare / normative object

No welfare analysis. The paper focuses entirely on positive predictions: employment effects of RMI, RSA, and counterfactual policies. No equivalent income, compensating variation, or social welfare function computed.

# Main findings

1. **RMI reduces employment by 3.6--5.8 ppt for HS dropouts at the age-25 cutoff (Tables 2--3).** The effect is concentrated among the low-educated: for the full sample, the drop is only 1.5--1.6 ppt. Stronger effects for men than women.

2. **The structural model replicates the RD estimates closely (Table 2):** Model predicts $-1.5$ ppt (all) and $-3.9$ ppt (HS dropouts) vs. RD estimates of $-1.6$ and $-3.9$ respectively.

3. **Internal validity: the model fits employment rates at all ages (Figures 3--4),** not just at the cutoff. Actual employment rates fall within the model's 95% confidence intervals at virtually all age levels.

4. **External validity: the model correctly predicts the RSA reform effect (Table 5).** The model (estimated on 1999 data) predicts that replacing RMI with RSA should reduce the disincentive effect by ~3 ppt. Actual post-reform RD estimates (Census 2010--2011) confirm this: the employment discontinuity at age 25 shrinks from $-2.6$/$-3.6$ ppt under RMI to near zero under RSA, a difference of 2.8--3.4 ppt.

5. **Counterfactual simulations:**
   - Abolishing the RMI: +5 ppt employment for HS dropouts aged 25--30 (Figure 6)
   - Extending RMI to under-25s: $-5$ ppt employment for HS dropouts under 25 (Figure 7)
   - Extending RSA to under-25s: near-zero employment effect (Figure 8), because the in-work component offsets the disincentive

6. **Policy implication:** The RSA's in-work benefit component alleviates the inactivity trap. Extending social assistance to youth is feasible without significant disincentive effects if in-work incentives are maintained.

# Main limitations

- Participation margin only (binary: work full-time or not). No hours choice.
- No demand-side modelling (no labour demand constraints, no RURO-type opportunities)
- $a_i + g_i \delta(A_i)$ confounds preferences, fixed costs, and search/demand constraints
- Static model: no dynamics, no job search, no human capital accumulation
- No welfare analysis
- Exclusion restriction (Condition 2: $b_{ij}$ age-invariant) is untestable
- Wage endogeneity not fully addressed (Heckman correction relies on the discontinuity instrument)
- External validity test has limited power (small post-RSA sample)

# Relevance for my JMP

## possible use for methodology
The paper demonstrates how quasi-experimental variation (RD) can strengthen the identification of structural labour supply models. For my JMP, if similar discontinuities exist in the Belgian/European tax-benefit system, they could be used to validate the RURO model. The paper's six-step approach -- (1) RD estimate, (2) structural model identified on the same variation, (3) internal validity check, (4) external validity check, (5) counterfactual simulations, (6) policy conclusions -- provides a template for validation.

## possible use for the structural vs. reduced-form debate
The paper illustrates the central trade-off: RD provides clean local identification but cannot extrapolate or simulate counterfactuals; the structural model can extrapolate but rests on assumptions. Combining them is the best of both worlds. For my JMP, the RURO model is structural and needs validation -- reduced-form evidence from policy reforms or discontinuities provides the validation.

## possible use for the participation margin
The paper focuses on the extensive margin (work vs. non-work) rather than hours choice. This is because the RMI discontinuity only affects the participation margin (the benefit goes to zero upon employment). For the RURO framework, the extensive margin is captured by the opportunity to choose non-participation, but the model also handles intensive-margin choices (hours). The finding that participation is the primary adjustment margin for young workers supports the importance of modelling the extensive margin correctly.

# Research questions this paper inspires

1. Can the Bargain-Doorley validation approach be applied to RURO models? If a RURO model is estimated on cross-sectional data, can its predictions for a policy reform be validated against actual post-reform outcomes? This would require finding a reform that changes the opportunity density $g(h,w)$ or the tax-benefit schedule $y(\cdot)$.

2. The paper notes that $a_i + g_i \delta(A_i)$ mixes supply and demand factors (p. 15). In the RURO framework, the opportunity density $g(h,w)$ captures demand-side constraints while $v(C, T-h)$ captures supply-side preferences. Can the RD approach be used to identify the opportunity density separately from preferences?

3. The paper finds that extending the RSA to under-25s has no significant disincentive effect because the in-work component offsets the out-of-work transfer. In terms of $W(z, R, A; y)$, the RSA changes $y$ (the tax-benefit schedule) in a way that increases financial incentives without reducing transfers. Does this policy also improve equivalent incomes? The paper cannot answer this because it does not compute welfare.

# Challenge to this paper

The paper convincingly validates the structural model at the participation margin, but the validation is necessarily local: it shows that the model correctly predicts the employment effect at the age-25 threshold for a specific policy change (RMI→RSA). It cannot validate the model's predictions for: (a) the hours margin (not modelled), (b) ages far from the threshold (the exclusion restriction is untestable at distant ages), or (c) policies that change the opportunity set rather than financial incentives. The confounding of preferences and demand-side constraints in $a_i + g_i \delta(A_i)$ means that the model cannot distinguish between policy effects that operate through incentives ($y$-channel) and those that operate through opportunities ($A$-channel).

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper models the participation decision as a function of financial incentives: $Y_i^* = f(C(wH; A) - C(0; A))$. In $W(z, R, A; y)$ terms, the paper captures $z$ (binary: work or not), part of $R$ (marginal utility of income), and $y$ (the tax-benefit schedule through $C(\cdot; A)$), but does not model $A$ (the opportunity set).

[Reasonable inference for my project] The paper's exclusion restriction -- marginal utility of income does not vary with age -- is essentially an assumption about $R$ (preferences are age-invariant in the income dimension). This is a weaker version of the RURO assumption that $v(C, T-h)$ is structurally separate from $g(h,w)$. The validation result (Table 5) supports the credibility of structural participation models identified on tax-benefit variation.

[Unclear from paper] Whether the RMI's disincentive effect operates entirely through financial incentives ($y$-channel) or also through effects on the opportunity set ($A$-channel). For example, RMI eligibility might reduce job search effort, which in the RURO framework would reduce the effective opportunity density $g(h,w)$. The paper's static model cannot distinguish these channels.

# Relation to Bargain et al. (2013)

This paper shares one author (Bargain) with Bargain et al. (2013) and uses a similar structural discrete-choice framework. However, this paper focuses on participation (binary choice) rather than hours (multiple alternatives), uses an RD identification strategy rather than cross-sectional tax-benefit variation, and does not compute welfare metrics. The paper provides methodological support for the structural approach used in Bargain et al. (2013) by demonstrating that structural participation models, when identified on quasi-experimental variation, can make credible counterfactual predictions.

# Relation to opportunities vs preferences

The paper explicitly acknowledges the confounding of opportunities and preferences: "we take $a_i + g_i \delta(A_i)$ as a non-identified combination of supply-side factors (work disutility or work costs) and demand-side factors (job search costs)" (p. 15). This is the central problem that the RURO framework addresses. The paper's approach is to leave this combination unidentified and focus on the income effect (through $b_{1i}$), which is identified by the RD. The RURO framework would decompose the non-participation into: (i) voluntary (preferences), (ii) involuntary (no suitable job available in $g(h,w)$), enabling a richer welfare analysis.

# Useful quotations / formulas

**On combining approaches (p. 1):**
"Natural experiments provide explicit and robust identifying assumptions for the estimation of treatment effects. Yet their use for policy design is often limited by the difficulty in extrapolating on the basis of reduced-form estimates of policy effects."

**Exclusion restriction (Condition 2, p. 11):**
"Marginal utility of consumption $b_{ij}$ does not vary with age."

**On the confounding of preferences and demand (footnote 13, p. 15):**
"See van Soest et al. (2002) for a similar interpretation of involuntary unemployment in a supply-side framework."

**On validation (p. 23--24):**
"The proximity with our model prediction -- even if it is only suggestive evidence -- about the external validity of the model and of the natural experiment underlying model identification."

**On extending RSA to youth (p. 27):**
"Our simulation gives support to the extension of welfare programs in France provided that in-work components are in place to 'make work pay'."

# Suggested tags

structural-labour-supply, regression-discontinuity, RD, validation, RMI, RSA, social-assistance, participation, youth-unemployment, France, discrete-choice, counterfactual-simulation, in-work-benefits, extensive-margin, Bargain, methodology

# My quick takeaway

An elegant methodological paper showing how to combine RD (clean local identification) with structural labour supply (counterfactual extrapolation). The key result for my JMP is the successful validation: the structural participation model, estimated on 1999 data, correctly predicts the employment effect of the 2009 RSA reform, as confirmed by post-reform RD estimates. This provides confidence that structural discrete-choice labour supply models (the same family as the RURO model) can make credible out-of-sample predictions. The paper's acknowledged limitation -- confounding of preferences and demand-side constraints in the intercept term -- is precisely what the RURO framework resolves by modelling opportunities explicitly.
