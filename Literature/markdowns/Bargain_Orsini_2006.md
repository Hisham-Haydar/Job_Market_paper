---
title: "In-work policies in Europe: Killing two birds with one stone?"
authors: [Olivier Bargain, Kristian Orsini]
year: 2006
outlet: "Labour Economics, 13(6), 667--697"
country_or_context: "France, Germany, Finland"
population: "Women in couples and single women, aged 25--64"
data_period: "1998 (France: 1994 HBS inflated to 1998; Germany: GSOEP 1998; Finland: IDS 1998)"
shelf: "in-work benefits / structural labour supply / microsimulation / cross-country / policy design"
tags: [in-work-benefits, WTC, WFTC, EITC, low-wage-subsidy, structural-labour-supply, discrete-choice, microsimulation, EUROMOD, cross-country, France, Germany, Finland, poverty, social-inclusion, policy-simulation, Van-Soest]
priority: "medium"
read_status: "extracted"
---

# Full citation

Bargain, O., & Orsini, K. (2006). In-work policies in Europe: Killing two birds with one stone? *Labour Economics*, 13(6), 667--697.

# One-sentence contribution

Compares the labour supply, poverty, and social inclusion effects of two hypothetical in-work benefit reforms -- a family-based Working Tax Credit (WTC, modelled on the British WFTC) and an individual Low-Wage Subsidy (LWS) -- simulated for France, Germany, and Finland using structural discrete-choice models and the EUROMOD microsimulator, finding that the individual LWS dominates on employment while the family-based WTC achieves a "double dividend" of poverty reduction and social inclusion only for lone mothers in Germany.

# Why this paper matters

This is one of the first comprehensive cross-country comparisons of in-work benefit design using a unified structural labour supply framework. It demonstrates how "framework conditions" -- the existing tax-benefit system, wage distribution, and participation rates -- drive cross-country differences in reform effects. The paper illustrates the standard Van Soest discrete-choice methodology applied to policy simulation, making it a useful reference for how structural models are used for ex-ante policy evaluation in the European context.

# Core research question

Can in-work transfers simultaneously increase employment (social inclusion) and reduce poverty ("killing two birds with one stone"), and how does the design choice between family-based (WTC) and individual-based (LWS) transfers interact with country-specific framework conditions?

# Economic setting and context

France, Germany, and Finland, circa 1998. All three countries have generous social assistance with near-100% implicit taper rates at low earnings, creating inactivity traps. None has implemented EITC/WFTC-style in-work benefits on a comparable scale. The paper simulates hypothetical reforms calibrated to the same real budgetary cost (after behavioural responses) across countries: WTC costs ~0.4% of GDP; LWS costs ~0.5% of GDP.

Key country differences: (1) France has individual income taxation but joint family assessment for benefits, higher female participation elasticity, more lone mothers on welfare; (2) Germany has joint income taxation (income splitting), lower female participation, higher childcare costs, larger social assistance; (3) Finland has individual taxation, flat-rate local tax, high female participation, compressed wage distribution.

# Model / theoretical framework

**Discrete-choice labour supply (Section 4.2):** Standard Van Soest (1995) conditional logit. Female chooses from $J = 3$ hours categories: non-participation ($H_1 = 0$), part-time ($H_2 = 20$), full-time ($H_3 = 39$ hours/week). Male labour supply fixed.

**Utility (eq. 2):**

$$U_{ij} = \alpha_{cc}(C_{ij} - F_{ij})^2 + \alpha_{hh}(H_j)^2 + \alpha_{ch}(C_{ij} - F_{ij})H_j + \alpha_{ci}(C_{ij} - F_{ij}) + \alpha_{hi}H_j$$

where $C_{ij}$ = disposable income (from EUROMOD), $F_{ij}$ = fixed costs of work, $H_j$ = hours. Taste-shifters interact with demographics: $\alpha_{ci} = \alpha_c^0 + \alpha_c' Z_i$ and $\alpha_{hi} = \alpha_h^0 + \alpha_h' Z_i$ where $Z_i$ includes age, children, education, region.

**Choice probability (eq. 1):**

$$P_{ik} = \frac{\exp U(H_k, C_{ik}, Z_i)}{\sum_{j=1}^{J} \exp U(H_j, C_{ij}, Z_i)}$$

**Two simulated reforms:**
- **WTC (Working Tax Credit):** Family-based, modelled on 2001 British WFTC. $\text{WTC} = B - \max(0; (z - \theta)t)$ with $B$ = maximum amount, $\theta$ = disregard, $t$ = 55% taper rate on net household income $z$. Requires at least 16 hours/week; 30-hour premium.
- **LWS (Low-Wage Subsidy):** Individual-based, proportional to individual earnings. $\text{LWS} = Ay$ if $w \leq W$; tapers to zero at $1.4W$ where $W$ = reference wage (10th percentile). Not conditional on family income.

Both calibrated to equal real cost after labour supply responses. $A = 12\%$ (Finland), 20.5% (France), 13% (Germany).

# Key objects

- **EMTR (Effective Marginal Tax Rate):** Implicit marginal tax rate on earnings, including benefit withdrawal. 4--6% of households face EMTR > 70% in all three countries.
- **Financial gain from working:** Change in disposable income from switching from non-participation to part-time or full-time work.
- **Elasticities (Table 4):** Own-wage elasticities of female labour supply (hours and participation).
- **Transition matrices (Table 5):** Simulated movements between non-participation, part-time, and full-time work under each reform.

# Data

- **France:** 1994 Household Budget Survey (*Enquête Budget des Ménages*), 11,220 households, inflated to 1998 prices.
- **Germany:** 1998 GSOEP wave, 7,677 households.
- **Finland:** 1998 Income Distribution Survey, 9,345 households.

Selected samples: households with head aged 25--64, not self-employed, not disabled, not retired, not in education. Labour supply estimated for women in couples (~2,095 France, 1,265 Germany, 1,632 Finland) and single women (~664, 453, 416).

Tax-benefit simulation via EUROMOD (EU-15 integrated microsimulation model, 1998 policy year).

# Identification logic

Standard discrete-choice identification from cross-sectional variation in wages and demographics, combined with nonlinearities in the tax-benefit system (via EUROMOD). No quasi-experimental variation or instruments. The paper acknowledges that demand-side constraints, rationing, and life-cycle effects are not modelled.

# Estimation / empirical strategy

1. Wage equations estimated with Heckman correction on LFS/survey data for each country.
2. Disposable income computed via EUROMOD at each discrete hours point for each household.
3. Conditional logit ML estimation of utility parameters separately for women in couples and single women, for each country.
4. Calibration of stochastic error terms to match observed hours distribution exactly.
5. Simulation of reforms: recompute disposable income under WTC/LWS rules, predict new hours choice using estimated model.
6. Bootstrapped 90% confidence intervals from 200 draws of parameter estimates.

# Treatment of preferences

Quadratic utility in consumption and hours with demographic taste-shifters. Fixed costs of work (significant for married women in France and Germany; not for Finland). The paper explicitly notes that estimated "preferences" likely confound true consumption-leisure preferences with demand-side constraints: "fixed costs of work and educational dummies might capture part of [hours rationing]" (p. 680). The paper refrains from welfare analysis because of this concern: "We also refrain from using the model for welfare analysis due to previous arguments on the lack of robustness of the model interpretation" (p. 680).

# Treatment of opportunities / constraints

Not modelled. The paper treats all non-employment as voluntary, acknowledging this is problematic: "the treatment of unemployed workers as opposed to individuals receiving social assistance... Most often, in the absence of modeling of the demand-side, the former are treated as other inactive workers, which amounts to arguing that they voluntarily remain unemployed" (p. 676). Job seekers/unemployed are excluded from the sample. This confounding of voluntary and involuntary non-participation is the standard limitation that the RURO framework addresses.

# Welfare / normative object

No welfare analysis. The paper evaluates reforms on two criteria: (1) **poverty reduction** (headcount ratio at 40%, 50%, 60% of median equivalised income), and (2) **social inclusion** (number of transitions from non-participation to work). These are positive outcomes, not welfare metrics. The authors explicitly note that "the equity-efficiency trade-off that is central to the design of in-work programs should be addressed using a social welfare function" and call for "a proper definition of the money metric equivalent" (p. 692) -- pointing directly to the Bargain et al. (2013) approach.

# Main findings

1. **WTC reduces overall female employment in all three countries (Table 5).** The family-based WTC discourages secondary earners (married women) because the benefit is tapered on household income. Net employment effect: $-3.0\%$ (France), $-0.6\%$ (Germany), $-0.8\%$ (Finland) of the selected population.

2. **LWS increases overall female employment in all three countries (Table 5).** The individual-based subsidy has no household income test, so no secondary earner disincentive. Net employment: $+2.3\%$ (France), $+0.9\%$ (Germany), $+0.6\%$ (Finland).

3. **The negative WTC effect on married women is strongest in France** due to: (i) joint family assessment interacting with individual income taxation, (ii) wider income distribution → more households in the phase-out range, (iii) higher female labour supply elasticity.

4. **Poverty reduction is similar across reforms (Table 7).** Both WTC and LWS reduce the poverty rate (50% median line) by roughly 0.5--1.5 ppt. The WTC is better targeted (lower deciles) but the LWS reaches more households. Behavioural responses amplify poverty reduction for WTC in Germany (lone mothers move into work).

5. **The "double dividend" (employment + poverty reduction) is achievable only for specific groups.** In Germany, the WTC generates a double dividend for lone mothers (high poverty rate, high elasticity, well-targeted by the WTC). In France, the LWS is better on both counts.

6. **Cross-country differences in reform effects are driven by framework conditions** -- the existing tax-benefit system, wage distribution, and initial participation rates -- not by differences in preferences alone.

7. **Elasticities (Table 4):** Women in couples: France 0.59 (hours), 0.52 (participation); Germany 0.38, 0.32; Finland 0.14, 0.14. Single women: France 0.11, 0.06; Germany 0.14, 0.12; Finland 0.27, 0.26.

# Main limitations

- No demand-side modelling; all non-employment treated as voluntary
- No welfare analysis (the authors explicitly flag this as a limitation)
- Male labour supply fixed (male responses to WTC could be important)
- No general equilibrium effects (wage adjustments, labour demand)
- Static model (no dynamics, no human capital, no job search)
- Three-point hours discretisation is very coarse
- No unobserved preference heterogeneity (no random coefficients)
- Cross-country comparisons limited by differences in data quality and sample composition

# Relevance for my JMP

## possible use for cross-country policy design context
The paper provides a template for comparing in-work benefit designs across European countries using structural models + EUROMOD. For my JMP, the key insight is that framework conditions matter enormously: the same reform has very different effects in France vs. Germany vs. Finland. This motivates country-specific RURO estimation rather than importing elasticities across countries.

## possible use for the welfare analysis gap
The paper explicitly calls for welfare analysis using "a proper definition of the money metric equivalent" (p. 692). Bargain et al. (2013) answer this call, and my JMP extends it by incorporating the RURO opportunity decomposition. The Bargain-Orsini paper demonstrates what can be done without welfare metrics (positive predictions only) and motivates why welfare metrics are needed.

## possible use for the demand-side limitation
The paper acknowledges that treating all non-employment as voluntary is problematic (p. 676). The RURO framework's explicit modelling of the opportunity density $g(h,w)$ resolves this. If some women are involuntarily non-participating (no suitable job available), the predicted employment responses to in-work benefits would be smaller than the standard model predicts (you can't take a job that doesn't exist, regardless of financial incentives).

# Research questions this paper inspires

1. How would the WTC vs. LWS comparison change if the opportunity set were modelled explicitly (RURO framework)? If many non-participating women face involuntary constraints, the WTC's negative employment effect on married women might be smaller (they can't leave jobs that are already scarce), and the LWS's positive effect might be smaller (the subsidy increases incentives but can't create jobs).

2. The paper finds that cross-country differences are driven by framework conditions. Can the RURO framework decompose these framework conditions into preferences ($R$) and opportunities ($A$)? Are French women's higher elasticities driven by preferences or by differences in the opportunity density $g(h,w)$?

3. The paper evaluates reforms on poverty and social inclusion but not on welfare. Using the equivalent income metric from Bargain et al. (2013), would the WTC or LWS score higher on welfare? The answer depends on whether welfare is evaluated using individual preferences (egalitarian-equivalent) or benchmark preferences (conditional equality).

# Challenge to this paper

The paper's key finding -- that the family-based WTC reduces married women's employment -- is driven by the standard model's assumption that all non-participation is voluntary. If some married women are rationed (involuntarily non-participating), the WTC's income effect would operate differently: the additional household income from the WTC would not "pull women out of work" because they are already not working due to constraints. The model conflates the WTC's income effect on voluntary non-participants (who might reduce their labour supply because household income rises) with its effect on involuntary non-participants (who cannot respond to income changes because they are already constrained). The RURO framework, by separating preferences from opportunities, would provide a cleaner estimate of the behavioural response.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper models the labour supply response to changes in $y$ (the tax-benefit schedule) using a standard Van Soest discrete-choice framework. $z$ (realised bundle) is determined by the choice among three hours categories. $R$ (preferences) is captured by quadratic utility with demographic heterogeneity. $A$ (opportunity set) is not modelled.

[Reasonable inference for my project] The paper's explicit call for welfare analysis using "the money metric equivalent" (p. 692) directly motivates the Bargain et al. (2013) and Fleurbaey equivalent-income approaches. In the $W(z, R, A; y)$ framework, the paper analyses the $y \to z$ mapping (how tax-benefit reforms change labour supply) but not the $z \to W$ mapping (how labour supply changes affect welfare).

[Unclear from paper] Whether the cross-country differences in elasticities reflect differences in preferences ($R$) or opportunities ($A$). If French women face more job opportunities (more flexible labour market, more part-time jobs), their higher elasticity could reflect greater opportunity rather than stronger preferences for leisure.

# Relation to Bargain et al. (2013)

This paper is a direct precursor to Bargain et al. (2013). It uses the same methodology (structural discrete-choice + EUROMOD) but stops at positive analysis (employment, poverty). Bargain et al. (2013) add the welfare dimension by computing equivalent incomes and other fairness-based welfare metrics. The policy question is the same: how do tax-benefit reforms affect different groups? But Bargain et al. can answer: "are the affected groups better or worse off in welfare terms?" while Bargain-Orsini can only answer: "do the affected groups work more or less?"

# Relation to opportunities vs preferences

The paper treats all non-employment as driven by preferences (or financial incentives), with no explicit opportunity/constraint channel. It acknowledges this limitation but cannot address it. The finding that fixed costs and educational dummies are significant for married women (esp. in Germany) is consistent with demand-side constraints (childcare rationing, hours restrictions) being absorbed into the utility function -- exactly the confounding that the RURO framework resolves.

# Useful quotations / formulas

**On the welfare analysis gap (p. 692):**
"Ultimately, the equity-efficiency trade-off that is central to the design of in-work programs should be addressed using a social welfare function. Further work is required in this direction and in particular a proper definition of the money metric equivalent to be used in coherence with the utility function."

**On demand-side constraints (p. 676):**
"Most often, in the absence of modeling of the demand-side, [the unemployed] are treated as other inactive workers, which amounts to arguing that they voluntarily remain unemployed. This is an extreme hypothesis, especially in the context of continental European labor markets."

**On framework conditions (p. 692--693):**
"The difference in tax-benefit environments has explained much of the differences in the effect of reforms across countries, in particular the difference in the generosity of the social assistance systems."

**On cross-country elasticity differences (p. 693):**
"It would be interesting to disentangle further the explanatory factors when assessing the differences across countries, especially how much is due to different preferences versus different tax-benefit environments."

# Suggested tags

in-work-benefits, WTC, WFTC, EITC, low-wage-subsidy, making-work-pay, structural-labour-supply, discrete-choice, conditional-logit, EUROMOD, microsimulation, France, Germany, Finland, cross-country, poverty, social-inclusion, inactivity-trap, secondary-earner, policy-simulation, Bargain

# My quick takeaway

A clean cross-country comparison of in-work benefit designs using standard structural labour supply models and EUROMOD. The central finding -- individual-based subsidies dominate family-based tax credits on employment, while poverty effects are similar -- highlights the tension between targeting (families) and incentive clarity (individuals). For my JMP, the paper's most important contribution is its explicit acknowledgment that welfare analysis is missing and needed ("a proper definition of the money metric equivalent"), pointing directly to the Bargain et al. (2013) equivalent-income approach and my JMP's RURO-based welfare decomposition. The paper also illustrates the standard model's inability to distinguish voluntary from involuntary non-participation -- a gap the RURO framework fills.
