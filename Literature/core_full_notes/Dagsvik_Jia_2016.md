---
title: "Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification"
authors: [John K. Dagsvik, Zhiyang Jia]
year: 2016
outlet: "Journal of Applied Econometrics, 31(3), 487–506"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Dagsvik, J. K., & Jia, Z. (2016). Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification. *Journal of Applied Econometrics*, 31(3), 487–506.

## One-sentence contribution
Provides the first formal nonparametric identification analysis of the latent-jobs (RURO) labour-supply model and shows that preferences and the opportunity measure cannot be separately recovered from cross-sectional choice data without parametric structure, while Box-Cox utility plus regularity conditions restore full identification.

## Core research question
Under what conditions are preferences $v(C,h)$ and the opportunity measure $\theta\, g_1(h)\, g_2(w\mid h)$ separately identified in a latent-jobs labour-supply model from cross-sectional data on hours, wages, and non-labour income, and does it matter empirically whether wage heterogeneity is modelled as variation across jobs or across individuals?

## Model / framework
A multiplicative random-utility random-opportunity model. Utility on a job is $U(C,h,z)=v(C,h)\varepsilon(z)$ with i.i.d. extreme-value taste shocks. Job offers arrive as an inhomogeneous Poisson process: market intensity $\theta$, hours density $g_1(h)$, conditional wage density $g_2(w\mid h)$. Choice probabilities have the standard RURO logit-style form (eq. 2a). Two competing wage-heterogeneity specifications are compared: Model 1 with job-specific wage shocks (Aaberge, Colombino & Strøm 1999 style) and Model 2 with individual-specific wage random effects.

## Data
Norwegian Labor Survey 1997. 2,515 married/cohabiting couples aged 25–64, neither self-employed nor in education. Eight feasible annual hours: 0, 208, 624, 1040, 1456, 1950, 2340, 2600.

## Identification logic
The fundamental equation is the ratio of working to non-working choice probabilities: $\varphi(h,w\mid I)/\varphi(0,0\mid I)\propto v(f(hw,I),h)\,\theta\,g_1(h)\,g_2(w\mid h)/v(f(0,I),0)$. Variation in non-labour income $I$ identifies the shape of $v$ in $C$ at each $h$ but not the level across $h$ values. Theorem 2 (negative): $v(C,h)$ is identified only up to an unknown multiplicative function $\delta(h)$, so $\delta(h)$ and $g_1(h)$ are not separately identified. Theorem 3: under wage-hours independence, $g_1(h)$ alone is identified. Theorem 4 (positive): Box-Cox utility plus a regularity condition on the marginal net-of-tax rate restores full identification. Theorem 5 extends identification when wages contain an unobserved individual random effect $\eta$.

## Treatment of preferences
Box-Cox utility in consumption and leisure with a consumption–leisure interaction (eq. 8). Demographic shifters (age, children) enter the leisure parameter. The estimated $\log v(C,h)$ is strictly increasing and concave in both arguments. The framework provides a theoretical rationale for hours dummies in conventional discrete-choice models: what looks like a preference peak at part-time/full-time is reinterpreted as a demand-side opportunity peak in $g_1(h)$.

## Treatment of opportunities / constraints
Opportunities enter as a separate measure $\theta\, g_1(h)\, g_2(w\mid h)$. $\theta$ is estimated below 1 for both genders (interesting market jobs are scarcer than interesting non-market opportunities); $\theta_F$ rises with women's schooling. $g_1(h)$ has a much higher full-time peak for men and a higher part-time peak for women. A counterfactual that removes the part-time peak and reallocates mass to full-time produces a large female shift from part-time to full-time, illustrating an $A$-channel simulation that conventional models cannot perform.

## Welfare / normative object
None. The paper is purely about identification and positive analysis (elasticities, model fit, demand-side simulation).

## Main findings
(i) Without parametric structure, $v(C,h)$ is only identified up to an unknown function of $h$. (ii) For tax/wage simulations the unidentified $\delta(h)$ does not matter. (iii) Model 2 (individual-specific wages) fits the Norwegian data better than Model 1 (job-specific wages). (iv) Female participation elasticity 0.33, male 0.01; female unconditional-hours elasticity 0.62, male –0.02; elasticities decline sharply with the wage level. (v) Removing the part-time hours peak shifts women toward full-time without much male response.

## Main limitations
Cross-sectional data only. Hours are subject to division-bias measurement error that the three-stage estimator does not fully eliminate. Wage–hours independence (Assumption 4) is imposed. No bargaining inside couples. Sector-specific opportunity heterogeneity is ignored. No welfare analysis is attempted, so the welfare implications of the identification result are only conjectural.

## Quick takeaway
The definitive identification reference for RURO models. The result that $v(C,h)$ and $g_1(h)$ are not separately nonparametrically identified means that any opportunity-vs-preference decomposition in this class of models inherits its credibility from its parametric assumptions. For tax/wage counterfactuals the non-identification is irrelevant; for welfare comparisons across individuals choosing different hours it matters directly.
