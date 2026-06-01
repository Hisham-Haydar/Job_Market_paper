---
title: "\"Making Work Pay\" in a Rationed Labor Market"
authors: [Olivier Bargain, Marco Caliendo, Peter Haan, Kristian Orsini]
year: 2010
outlet: "Journal of Population Economics, 23(1), 323--351"
country_or_context: "Germany"
population: "Singles and couples, ages 20--65"
data_period: "2002 (GSOEP 2003 wave)"
shelf: "structural labour supply / rationing / making work pay / double-hurdle"
tags: [discrete-choice, double-hurdle, rationing, involuntary-unemployment, mini-job, employment-bonus, making-work-pay, Germany, microsimulation, elasticities, demand-side-constraints]
priority: "medium"
read_status: "extracted"
---

# Full citation

Bargain, O., Caliendo, M., Haan, P., & Orsini, K. (2010). "Making Work Pay" in a Rationed Labor Market. *Journal of Population Economics*, 23(1), 323--351.

# One-sentence contribution

Introduces a double-hurdle discrete choice labour supply model that explicitly accounts for involuntary unemployment in Germany, shows that ignoring rationing leads to a triple bias in elasticity estimates and overstates employment effects of "making work pay" reforms by up to 60%, and finds that transfers conditioned on low wages (Employment Bonus) dominate transfers conditioned on low earnings (mini-job reform) in both employment effects and cost efficiency.

# Why this paper matters

Most structural labour supply models used for tax reform evaluation assume all non-employment is voluntary, which leads to biased elasticity estimates and overstated policy predictions in countries with significant involuntary unemployment. This paper provides one of the clearest demonstrations of the quantitative importance of accounting for demand-side rationing in a discrete choice framework. The "triple bias" characterization — (1) misspecification, (2) erroneous freedom of choice, (3) overstatement of taste for leisure — provides a systematic taxonomy of the errors from ignoring rationing. The paper also contributes to the policy debate on optimal design of in-work transfers (individual vs. family-based, wage-conditioned vs. earnings-conditioned).

# Core research question

How large are the biases in labour supply elasticities and policy predictions when involuntary unemployment is ignored? And how do two "making work pay" reforms — the German mini-job reform (conditioned on low earnings) and a hypothetical Employment Bonus (conditioned on low wages, inspired by Belgium) — compare in employment effects and cost efficiency when rationing is properly accounted for?

# Economic setting and context

Germany 2002: high involuntary unemployment (~6% of individuals in couples, ~10% of singles by ILO definition), progressive joint income taxation for married couples, complex social security contribution (SSC) system with mini-job exemptions. Strong regional variation in labour market conditions (East vs. West Germany). The 2003 mini-job reform expanded earnings exemptions from SSC from 325 to 400 Euro/month and abolished the 15-hour restriction.

# Model / theoretical framework

**1. Unconstrained model (standard DC):** Van Soest (1995) style discrete choice model with 6 hours points per worker (0, [0,12], ]12,20], ]20,34], ]34,40], >40). For couples with both spouses flexible: 36 alternatives. Utility $V_{ij} = U(Lf_{ij}, Lm_{ij}, C_{ij}, Z_i) + \epsilon_{ij}$ with quadratic specification following Blundell et al. (2000). Part-time dummies to capture job availability / disutility of part-time.

**2. Constrained model (double-hurdle):** Combines the DC model with a probit rationing equation:
$$I_i^* = \beta X_i + \eta_i$$
where $X_i$ includes regional labour market indicators (5 clusters of labour office districts), education, age, and past employment history. Three states: voluntary inactivity, involuntary unemployment, employment.

**Likelihood contributions:**
- Voluntarily inactive: $P_{i0}^{VOL} = \frac{\exp U(L_{i0}, C_{i0}, Z_i)}{\sum_j \exp U(L_{ij}, C_{ij}, Z_i)}$
- Involuntarily unemployed at desired hours $k$: $P_{ik}^{INVOL} = \frac{\exp U(L_{ik}, C_{ik}, Z_i)}{\sum_j \exp U(L_{ij}, C_{ij}, Z_i)} \cdot \Phi(\beta X_i)$
- Employed at hours $k$: $P_{ik}^{EMP} = \frac{\exp U(L_{ik}, C_{ik}, Z_i)}{\sum_j \exp U(L_{ij}, C_{ij}, Z_i)} \cdot [1 - \Phi(\beta X_i)]$

**Key assumption:** The rationing probability and the utility error terms are independent (estimated separately). This rules out discouragement effects but is standard in the double-hurdle literature.

**Framework:** Positive (behavioural prediction of employment effects).

# Key objects

- **Triple bias from ignoring rationing:** (1) *Specification bias*: the unconstrained model is misspecified since individual characteristics must implicitly account for demand-side constraints; (2) *Participation bias*: rationed workers are assumed to voluntarily choose inactivity, so transitions to participation are overstated after a wage shock; (3) *Preference bias* (Ham 1982): ignoring unemployment leads to overstating the taste for leisure, which understates elasticities. Biases (1)+(2) dominate (3), so overall elasticities are biased upward.
- **Rationing probability:** Probit model with regional clusters, education, age, and employment history as predictors. Cluster I (East Germany) has 12.4% female / 11.7% male involuntary unemployment; Cluster V (best West German regions) has 3.1% / 2.4%.
- **Employment Bonus:** Hypothetical reform inspired by Belgium — SSC rebate conditioned on full-time equivalent wage rate (up to 1,210 Euro/month), phased out at 17.8% taper rate above this threshold. Targets low-wage workers regardless of hours.
- **Mini-job reform:** Actual 2003 reform — SSC exemption expanded to 400 Euro/month earnings with sliding-scale phase-out to 800 Euro. Targets low-earnings workers regardless of wage rate.

# Data

2003 wave of the German Socio-Economic Panel (GSOEP), fiscal year 2002. Sample: 1,022 single women, 783 single men, 3,822 couples (both flexible), 970 couples (female flexible), 562 couples (male flexible). ILO definition of involuntary unemployment: actively searched in last 4 weeks AND ready to take up a job within 2 weeks. Tax-benefit calculations using STSM microsimulation model.

# Identification logic

The rationing probability is identified from regional demand-side variation (5 labour office district clusters based on Blien et al. 2004) and individual characteristics correlated with job-finding probability (education, past employment history). The key identifying assumption is that, conditional on observables, the rationing risk is independent of the utility error terms — i.e., who gets rationed is not systematically related to unobserved taste for leisure. This is the standard double-hurdle assumption (Blundell et al. 1987).

# Estimation / empirical strategy

1. Estimate the rationing probit and the discrete choice utility model jointly (though with independent error terms).
2. Compute elasticities from both constrained and unconstrained models.
3. Simulate employment effects of the mini-job reform and Employment Bonus under both models.
4. For the constrained model, account for the fact that new labour market entrants face a rationing probability: their expected hours are weighted by $(1 - \Phi(\beta X_i))$.
5. Bootstrap confidence intervals from 100 draws of utility parameters.

# Treatment of preferences

Preferences modeled via quadratic utility in leisure and consumption, with taste-shifters for age, children, region (East Germany), and nationality. Part-time dummies capture specific (dis)utility from part-time work arrangements. The constrained model produces "more precise" preference estimates: some taste-shifters that appear significant in the unconstrained model (e.g., East Germany dummy for male leisure) lose significance when rationing is accounted for, revealing they were proxying for demand-side constraints rather than preferences.

# Treatment of opportunities / constraints

**This is the paper's central contribution.** The standard DC model assumes all individuals can freely choose among all hours alternatives — the opportunity set is fixed and identical for everyone. The double-hurdle model introduces a **rationing probability** $\Phi(\beta X_i)$ that varies across individuals based on demand-side characteristics (region, education, employment history).

Key differences from the RURO approach:
- The rationing probability is a **reduced-form** probit, not a structural opportunity density $p(w,h)$
- Rationing is **binary** (employed or not) — there is no variation in the density of different hours/wage combinations
- The opportunity set structure (which types of jobs are available) is captured only through part-time dummies, not through a structural density
- The rationing probability is **not endogenous** to the tax reform — it is held fixed under counterfactual policies

Despite these simplifications, the model captures the essential feature: not all desired jobs are available, and ignoring this leads to biased predictions.

# Welfare / normative object

The paper is **purely positive** — no welfare evaluation is performed. The focus is entirely on predicting employment effects (participation, hours) and computing elasticities. No social welfare functions, equivalent income, or distributional analysis.

# Main findings

**Elasticities (Table 8):**

| Group | Unconstrained participation | Constrained participation | Unconstrained hours | Constrained hours |
|-------|---------------------------|--------------------------|--------------------|--------------------|
| Women in couples (both flex.) | 0.150 | 0.122 | 0.351 | 0.316 |
| Men in couples (both flex.) | 0.079 | 0.050 | 0.115 | 0.091 |
| Single women | 0.197 | 0.069 | 0.267 | 0.104 |
| Single men | 0.226 | 0.083 | 0.300 | 0.152 |

- Unconstrained elasticities are systematically higher than constrained ones
- The bias is largest for groups with high rationing (single men: 0.226 vs. 0.083 participation; single women: 0.197 vs. 0.069)
- For married women (lowest rationing, highest voluntary non-participation), the bias is smallest

**Mini-job reform (Table 10):**
- Unconstrained model: 56,000 new participants; net hours effect $-4,000$ FTE (negative intensive margin)
- Constrained model: 43,000 new participants (36,000 net of rationing); net hours effect $-11,000$ FTE
- ~16% of new entrants face rationing
- The reform mainly affects secondary earners in couples; effects on singles are negligible

**Employment Bonus (Table 11):**
- Unconstrained model: 295,000 new participants; net hours +339,000 FTE
- Constrained model: 159,000 new participants; net hours +211,000 FTE
- **The unconstrained model overstates the employment effect by about 60%**
- Effects are larger because the Bonus targets full-time work and low wages (not low earnings)
- Cost per new entrant: 19,000 Euro (Bonus) vs. 44,000 Euro (mini-job) — Bonus is more cost-efficient

**Key mechanism:** The Employment Bonus generates larger responses among singles and primary earners (groups with high rationing), so the bias from ignoring rationing is proportionally larger. The mini-job reform mainly affects secondary earners (low rationing), so the bias is smaller.

# Main limitations

- The rationing probability is a reduced-form probit — no structural model of labour demand.
- Rationing is binary (employed/not) and does not capture heterogeneous job availability by hours or occupation.
- The rationing probability is held fixed under policy changes — no equilibrium feedback.
- The independence assumption between rationing and utility errors rules out discouragement effects.
- No welfare evaluation — only employment effects are assessed.
- The Employment Bonus is hypothetical (not implemented in Germany), so there is no ex-post validation.
- Partial equilibrium: wage rates are fixed under the reforms.

# Relevance for my JMP

## possible use for framing
The paper demonstrates that ignoring demand-side constraints ($A$ in my framework) leads to systematically biased predictions. The triple bias taxonomy provides a clear motivation for explicitly modelling the opportunity set $A$ in both positive and normative analysis.

## possible use for model design
The double-hurdle approach is a simpler alternative to RURO for incorporating rationing. For my framework, the RURO approach is superior because it provides a structural representation of the opportunity density $p(w,h)$ that can be used both for positive predictions and for the welfare criterion $W(z,R,A;y)$. However, the double-hurdle results provide a useful benchmark for comparison.

## possible use for identification
The paper's identification of rationing from regional labour market clusters and individual employment history illustrates how demand-side information can be used to separate voluntary from involuntary non-participation — the empirical counterpart of distinguishing $R$-driven from $A$-driven non-employment.

## possible use for decomposition
The triple bias decomposition (specification, participation, preference) provides a taxonomy of the errors from ignoring $A$. In my framework, these correspond to: (1) misattributing $A$-effects to $R$; (2) treating $A$-constrained individuals as if they freely chose non-work; (3) overestimating the leisure preference component of $R$.

## possible use for comparative application
Germany provides a high-unemployment context where rationing matters substantially. Comparing with Norway (low unemployment, flexible hours) and Italy (high unemployment but also rigid hours) would illustrate how the importance of modeling $A$ varies across institutional settings.

# Research questions this paper inspires

1. How would the welfare evaluation of the mini-job reform vs. Employment Bonus differ if a $W(z,R,A;y)$ criterion were used? The paper only evaluates employment effects, but the welfare implications depend on whether non-employment is due to $A$ (circumstance) or $R$ (choice).

2. Would using a RURO model instead of a double-hurdle model change the ranking of the two reforms? The RURO captures richer heterogeneity in job availability (not just employed/not) and might produce different predictions for hours responses.

3. The paper finds that the bias from ignoring rationing is small for secondary earners but large for primary earners and singles. Does this imply that the welfare consequences of rationing are also larger for these groups?

# Challenge to this paper

The double-hurdle model treats rationing as a binary, reduced-form probability that is independent of preferences and fixed under policy changes. This has two important implications. First, it cannot capture how reforms might change the opportunity set itself — for example, the mini-job reform might create new types of jobs (splitting full-time positions into mini-jobs) that change the density of available opportunities. Second, the independence assumption between rationing and taste for leisure rules out discouragement effects, where individuals in high-unemployment regions may reduce their job search intensity (a taste-for-leisure response to poor opportunities). A structural model of the opportunity set (like RURO) would address both limitations by endogenizing the opportunity density.

# Relation to my jobs_and_wellbeing framework

[Reasonable inference for my project] The paper's rationing probability $\Phi(\beta X_i)$ is a reduced-form measure of the scarcity of the feasible set $A_i$. In my framework, $A_i$ is the structural object — the set of feasible job packages — and the RURO opportunity density $p(w,h)$ is its empirical counterpart. The paper shows that ignoring $A$ (treating all non-employment as voluntary) produces biased positive predictions; my framework extends this insight to normative evaluation, where ignoring $A$ produces biased welfare assessments. Specifically, if two individuals are both non-employed but one is rationed ($A$ is empty) and the other voluntarily chose non-work ($R$ prefers leisure), the $W(z,R,A;y)$ framework treats them differently — the first has a circumstance-driven disadvantage that should be compensated, while the second has a preference-driven outcome for which they bear responsibility.

[Explicit in paper] The paper explicitly models involuntary unemployment as demand-side rationing (Section 3.2, eq. 2). It uses ILO criteria (active search + ready to work) to classify unemployment as involuntary. It states: "ignoring involuntary unemployment, however, leads to biased elasticities and wrong predictions of the employment effects of a reform" (p. 325).

[Unclear from paper] How the rationing probability relates to the RURO parameter $g_0$ (ratio of market to non-market opportunities). The double-hurdle probit is a reduced form; $g_0$ is a structural parameter. The relationship between them is not discussed. Also unclear is whether the triple bias taxonomy would apply equally to RURO models, which structurally separate preferences from opportunities.

The paper is closest to: **empirical demonstration that opportunity constraints ($A$) matter for positive predictions** — a necessary precursor to showing they also matter for normative evaluation.

# Relation to Bargain et al. (2013)

This is an earlier paper by overlapping authors (Bargain). While Bargain et al. (2013) focus on welfare evaluation with heterogeneous preferences (no rationing), this paper focuses on positive prediction with rationing (no welfare evaluation). The two papers are complementary: Bargain et al. (2013) show that preferences matter for welfare; this paper shows that opportunities matter for employment predictions. My framework combines both insights: $W(z,R,A;y)$ requires both $R$ (heterogeneous preferences, as in Bargain et al. 2013) and $A$ (opportunity constraints, as in this paper) for welfare evaluation.

# Relation to opportunities vs preferences

The paper provides the clearest demonstration in this literature of the **confounding of preferences and opportunities** in standard discrete choice models. The "preference bias" (Ham 1982) shows that ignoring rationing leads to overstating the taste for leisure — because involuntary unemployment is misattributed to preference for non-work. The "specification bias" shows that demand-side variables (region, employment history) are absorbed into preference parameters, making them imprecise. The constrained model resolves both biases by explicitly separating the rationing probability (opportunity) from the utility function (preferences). This is directly relevant to the $R$ vs. $A$ decomposition in my framework: standard models that ignore $A$ produce contaminated estimates of $R$.

# Useful quotations / formulas

**Triple bias (p. 340):**
"Not considering involuntary unemployment in the *unconstrained* model leads to biased estimated elasticities for several reasons. We suggest a breakdown of these effects."

**On overstating policy effects (p. 348):**
"In the case of the Employment Bonus, the total employment effect is overstated by about 60%."

**On policy design (p. 347):**
"A transfer conditioned on low wages (e.g., the Employment Bonus) avoids negative effects at the intensive margin and generates larger participation effects than a reform targeted at low earnings (e.g., the mini-job reform)."

**Constrained choice probability (eq. 5--6):**
$$P_{ik}^{INVOL} = \frac{\exp U(L_{ik}, C_{ik}, Z_i)}{\sum_j \exp U(L_{ij}, C_{ij}, Z_i)} \cdot \Phi(\beta X_i)$$
$$P_{ik}^{EMP} = \frac{\exp U(L_{ik}, C_{ik}, Z_i)}{\sum_j \exp U(L_{ij}, C_{ij}, Z_i)} \cdot [1 - \Phi(\beta X_i)]$$

# Suggested tags

discrete-choice, double-hurdle, rationing, involuntary-unemployment, making-work-pay, mini-job, employment-bonus, Germany, GSOEP, elasticities, participation-bias, preference-bias, specification-bias, demand-side-constraints, microsimulation, van-Soest

# My quick takeaway

This paper provides essential evidence that demand-side rationing (the $A$ component) must be accounted for in labour supply models. The triple bias taxonomy is a clean way to motivate the RURO approach (which structurally models $A$) over the standard DC approach (which ignores it). The finding that ignoring rationing overstates the Employment Bonus effect by 60% is striking and directly relevant to my framework: if the positive model is biased by 60%, the welfare evaluation under $W(z,R,A;y)$ — which requires accurate counterfactual predictions — would also be severely biased. The paper is purely positive (no welfare analysis), so the normative implications are left for my framework to develop. The comparison between wage-conditioned and earnings-conditioned transfers is also relevant: wage-conditioned policies are closer to "first-best" taxation on productivity, which relates to the $y$ (pay schedule) component of my framework.
