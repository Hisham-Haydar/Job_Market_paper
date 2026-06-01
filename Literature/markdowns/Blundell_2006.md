---
title: "Earned income tax credit policies: Impact and optimality -- The Adam Smith Lecture, 2005"
authors: [Richard Blundell]
year: 2006
outlet: "Labour Economics, 13(4), 423--443"
country_or_context: "United Kingdom and United States"
population: "Lone parents (single mothers), primarily with children"
data_period: "1978--2003 (UK Family Resources Survey, Labour Force Survey)"
shelf: "earned income tax credit / WFTC / EITC / optimal taxation / structural labour supply / discrete choice / welfare reform / policy evaluation"
tags: [EITC, WFTC, earned-income-tax-credit, in-work-benefits, optimal-taxation, structural-labour-supply, discrete-choice, difference-in-differences, lone-parents, participation, extensive-margin, intensive-margin, welfare-weights, Saez, UK, US, Blundell, policy-evaluation]
priority: "medium"
read_status: "extracted"
---

# Full citation

Blundell, R. (2006). Earned income tax credit policies: Impact and optimality -- The Adam Smith Lecture, 2005. *Labour Economics*, 13(4), 423--443.

# One-sentence contribution

Evaluates the impact and optimality of the UK Working Families Tax Credit (WFTC) reform using both a structural discrete-choice labour supply model and difference-in-differences, resolving the puzzle of why the UK WFTC had smaller labour supply effects than the US EITC despite being more generous, and showing that the WFTC design is close to optimal for lone parents with pre-school children under mild inequality aversion.

# Why this paper matters

This paper demonstrates the full pipeline from structural labour supply estimation to optimal tax design for in-work benefit policies. It validates structural models by comparing their predictions to quasi-experimental (DiD) estimates, shows how interactions between the tax credit and other benefits (Housing Benefit, Income Support) dampen incentive effects, and uses the structural model to compute optimal tax schedules. The resolution of the UK-US puzzle is instructive: similar elasticities in both countries, but the UK's means-testing against net (not gross) income and simultaneous increases in out-of-work benefits explain the smaller UK impact.

# Core research question

What is the impact of the UK WFTC on labour supply of lone parents, and is the WFTC design close to an optimal earned income tax credit given reasonable social welfare weights?

# Economic setting and context

UK welfare reform in 1999: Working Families Tax Credit replaced Family Credit with higher generosity, lower withdrawal rate (55% vs 70%), and a childcare credit. Compared with the US EITC (phased in at 34-40%, withdrawn at ~16-21%). The UK system is means-tested on net family income (interacting with Housing Benefit and Income Support), while the US EITC is based on gross individual earnings. Simultaneously, the UK increased Income Support (out-of-work benefits) and Child Benefit, dampening the work incentive from WFTC.

# Model / theoretical framework

**Structural model:** Mixed multinomial discrete choice over hours: $h \in \{0, 1-15, 16-22, 23-29, 30-36, 37+\}$. Utility is a quadratic polynomial in net income and hours, with demographic-specific preference heterogeneity. Additive Type-I extreme value errors for each hours alternative.

Key model features:
- Non-convex budget constraint from tax-benefit interactions computed exactly for each individual
- Fixed costs of work (participation costs)
- Childcare costs (linear in hours per child, varying with age)
- Take-up / stigma costs for programme participation
- Unobserved heterogeneity: 6 discrete mass points (support points) for random preferences

**Elasticity estimates:** Average extensive elasticity = 0.81 (s.e. 0.13), average intensive elasticity = 0.31 (s.e. 0.09).

**Optimality analysis:** Social welfare function $\Gamma(U|\theta) = \frac{1}{\theta}\{(\exp U)\theta - 1\}$. $\theta < 0$ favours equality; $\theta = 0$ is utilitarian. Government chooses 4 marginal tax rates over 5 earnings regions to maximise social welfare subject to budget constraint. Marginal tax rates restricted to $[-100\%, 100\%]$ with non-decreasing budget constraint.

# Key objects

- **WFTC (Working Families Tax Credit):** UK in-work benefit from 1999, replacing Family Credit. Requires 16+ hours work, means-tested on net family income, withdrawn at 55%.
- **EITC (Earned Income Tax Credit):** US in-work benefit. Phase-in at 34-40%, plateau, withdrawal at 16-21%. Based on gross earnings.
- **Benefit interactions:** WFTC income counts as income for Housing Benefit and Council Tax Benefit calculation, reducing the net gain from WFTC by ~50% for many claimants (Fig. 5).
- **The UK-US puzzle:** UK WFTC is ~2x more generous than US EITC, yet UK labour supply impact (~3.5-4 ppt participation increase for lone parents) is similar to or smaller than US EITC impact. Resolution: (1) simultaneous increase in Income Support dampened incentives; (2) WFTC interacts with housing/council tax benefits reducing net gain; (3) elasticities are actually similar in both countries.

# Data

UK Family Resources Survey (FRS), ~30,000 families/year, cross-section, Spring 1996 -- Spring 2003 (dropping Summer 1999 -- Spring 2000 transition period). UK Labour Force Survey (LFS), ~60,000 families/quarter. DiD analysis: 74,959 (FRS) and 233,208 (LFS) observations. Treatment: single mothers; control: childless single women.

# Identification logic

**DiD:** Treatment = lone parents (eligible for WFTC); control = childless single women (not eligible). Three assumptions: (i) separability, (ii) common trends, (iii) time-invariant group heterogeneity. Matching on age, education, region, ethnicity. DiD estimate: 3.57 ppt (FRS, s.e. 0.81), 3.81 ppt (LFS, s.e. 0.33).

**Structural model:** Identified from variation in budget constraints across individuals (wage variation, location-specific housing costs, tax-benefit schedule kinks, childcare costs). The DiD validates the structural model: the simulated DiD from the structural model is not significantly different from the actual DiD (p-value = 0.42).

# Estimation / empirical strategy

1. **DiD:** Employment rate changes for lone parents vs childless single women, pre- vs post-WFTC, with matching covariates.

2. **Structural discrete choice:** Maximum simulated likelihood. Mixed multinomial logit over discrete hours. Integrates over unobserved heterogeneity (6 mass points) and childcare cost distribution.

3. **Optimal tax computation:** Grid search over 4 marginal tax rates (in 5 earnings regions), maximising social welfare with $\theta = -0.2$ (mild inequality aversion), conditional on government budget = actual expenditure on each demographic group.

# Treatment of preferences

Preferences are a quadratic function of consumption and hours: $U(c, h) = \alpha_c c + \alpha_h h + \alpha_{cc} c^2 + \alpha_{hh} h^2 + \alpha_{ch} ch + \text{fixed costs}$, with coefficients varying by demographic group and unobserved heterogeneity mass points. 99.0% of lone parents have positive marginal utility of net income. Preferences are heterogeneous across demographic and ethnic groups and across unobserved types.

# Treatment of opportunities / constraints

The paper does not model demand-side constraints or job availability. Hours are chosen from a discrete set, but this reflects modelling convenience for non-convex budget constraints, not demand-side rationing. There is no discussion of involuntary unemployment or hours constraints beyond the minimum 16-hour work condition for WFTC eligibility. Take-up and stigma costs are modelled as fixed costs that reduce the effective benefit of programme participation.

# Welfare / normative object

Social welfare function $\Gamma(U|\theta)$ applied to individual utilities. The implied welfare weights $\frac{\partial \Gamma}{\partial U}$ decline monotonically with income (Fig. 9b). With $\theta = -0.2$, the welfare weights at the top of the income distribution are about 0.2 relative to the bottom (=1.4). The analysis asks whether the existing WFTC schedule is close to the schedule that maximises this social welfare function subject to the government budget constraint.

# Main findings

1. **DiD impact:** WFTC increased lone parent employment by 3.5--4 ppt (Table 3). Robust across FRS and LFS data.

2. **Structural model validates DiD:** Simulated DiD from structural model = 3.86 ppt (s.e. 0.84), not significantly different from actual DiD (p = 0.42). This validates the structural model.

3. **WFTC expansion alone:** 5.95 ppt employment increase (Table 4a). But combined with all reforms (Income Support increases, child benefit increases): only 3.86 ppt (Table 4b). The difference confirms that the IS increases dampened WFTC incentive effects.

4. **Resolution of UK-US puzzle:** Similar elasticities in both countries; the smaller UK impact is due to (i) interaction with housing benefits reducing net gain from WFTC, (ii) simultaneous IS increases, (iii) UK means-testing on net income vs US on gross income.

5. **Optimal tax schedule resembles WFTC:** For lone parents with pre-school children (age 0-4), the optimal schedule with $\theta = -0.2$ closely resembles the actual WFTC schedule (Fig. 10). The WFTC is approximately optimal for this group.

6. **Suboptimality for older children:** The WFTC is not generous enough for lone parents with older children (11-18): the optimal schedule shows steeper phase-in and higher transfers for this group (Fig. 9a).

7. **Welfare weights are reasonable:** The implied welfare weights ($\theta = -0.2$) decline monotonically with income and are comparable to those in Immervoll et al. (2004). Robust to varying $\theta$ from 0 to $-0.2$ (conclusions about optimal design remain).

# Main limitations

- Focus on lone parents only; couples excluded despite being a major target group.
- No demand-side modelling: assumes free choice of hours, ignoring labour market constraints.
- Static model: no dynamic effects (human capital accumulation, job search, career progression).
- Representative agent approach to UK-US comparison, though individual-level for UK analysis.
- The optimal tax computation uses a standard utilitarian-type SWF with an inequality aversion parameter, not a fairness-based criterion (equivalent income, conditional equality).
- Take-up behaviour modelled as a cost but not structurally estimated.

# Relevance for my JMP

## possible use for the structural model validation approach
The paper's strategy of validating structural model predictions against DiD estimates is a useful template for my work. If my RURO model generates predictions that can be validated against quasi-experimental evidence, this strengthens the credibility of the welfare analysis.

## possible use for the importance of benefit interactions
The finding that WFTC's impact was halved by interactions with Housing Benefit and Income Support highlights the importance of modelling the full tax-benefit system in welfare analysis. My RURO framework should account for these interactions when computing equivalent incomes, as they affect both budget constraints and opportunity sets.

## possible use for the extensive margin focus
The paper shows that labour supply responses to EITC/WFTC are primarily extensive-margin (participation), with limited intensive-margin (hours) response. This supports the focus on participation decisions in my RURO framework, where the extensive margin is naturally captured by the job arrival process and opportunity density.

# Research questions this paper inspires

1. How would the optimality analysis change if the social welfare function were based on equivalent incomes (as in Fleurbaey & Maniquet) rather than transformed utilities? The WFTC might look less optimal if fairness criteria prioritise the worst-off in terms of equivalent income rather than in terms of utility.

2. How would demand-side constraints (hours restrictions, job availability) change the optimal EITC design? If some lone parents cannot access 16+ hour jobs (the WFTC minimum), the WFTC may be suboptimal because it excludes constrained workers.

# Challenge to this paper

The paper assumes free choice of hours from a discrete set, treating the 16-hour minimum in WFTC as a feature of the tax schedule, not as a potential mismatch with available jobs. In the RURO framework, some lone parents may face an opportunity set where 16+ hour jobs are scarce or unavailable, making the WFTC inaccessible regardless of their preferences. The paper's finding that the WFTC is "approximately optimal" is conditional on the assumption that all lone parents can freely choose 16+ hours. Under demand-side constraints, the optimal policy might involve lower hour thresholds or alternative instruments targeting the extensive margin without an hours condition.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper uses a structural discrete-choice labour supply model that is a close precursor to the models in my framework. The budget constraint computation, preference specification, and simulation methodology are directly relevant.

[Reasonable inference for my project] The paper's finding that benefit interactions reduce the effective incentive from in-work benefits by ~50% implies that the opportunity value of a job (in my RURO framework) depends not just on the wage but on the full tax-benefit schedule. The opportunity density $g(h, w)$ should be evaluated at net income, not gross income.

[Unclear from paper] Whether the DiD validation approach can be extended to validate RURO models, where the demand side (job availability) is also modelled. The DiD identifies the average treatment effect of the policy change, but it does not separate supply-side from demand-side channels.

# Relation to Bargain et al. (2013)

Direct connection. Bargain et al. (2013) build on the same structural discrete-choice labour supply methodology (citing Blundell et al. 2000, Blundell and MaCurdy 2000, Van Soest 1995) but add the equivalent income welfare criterion. Blundell (2006) uses standard utilitarian SWF with transformed utilities; Bargain et al. use equivalent income with maximin. The structural models are similar, but the welfare evaluation differs.

# Relation to opportunities vs preferences

The paper is about preferences and incentives, not opportunities. Labour market attachment is treated as a choice variable responding to financial incentives (the tax-benefit schedule), not as constrained by job availability. The 16-hour minimum for WFTC eligibility is treated as a policy design feature, not as a potential barrier for workers facing demand-side hours restrictions. The hours distribution (Fig. 6a) shows a spike at 16 hours for single mothers, consistent with bunching at the WFTC threshold, but the paper does not ask whether this spike reflects constrained or unconstrained choice.

# Useful quotations / formulas

**On the UK-US puzzle (p. 437):**
"The small effects of the reform are due to interaction of WFTC with other taxes/benefits and the rise in family allowances (all reforms) which are given without a work condition, rather than 'small' response elasticities."

**On structural model validation (p. 437):**
"Note that the simulated diff-in-diff parameter from the structural evaluation model is precise and does not differ significantly from the diff-in-diff estimate."

**On optimality (p. 439):**
"Remarkably the optimal tax function and the WFTC constraint show a degree of similarity. Suggesting that the WFTC policy for social welfare weights with $\theta = -0.2$ may well be an optimal design."

**On the iron triangle (p. 424):**
"The aim of such policies is to break the 'iron triangle' of welfare policy - that is the three, often conflicting, goals: raising the living standards of those on low incomes; encouraging work and economic self-sufficiency; and keeping government costs low."

**Elasticities (p. 436):**
"With an average extensive elasticity of .81 (.13) and an intensive elasticity of .31 (.09)."

# Suggested tags

EITC, WFTC, earned-income-tax-credit, in-work-benefits, optimal-taxation, structural-labour-supply, discrete-choice, difference-in-differences, lone-parents, participation, extensive-margin, intensive-margin, welfare-weights, Saez, UK, US, Blundell, policy-evaluation, benefit-interactions

# My quick takeaway

A comprehensive Adam Smith Lecture demonstrating the full structural labour supply pipeline: from estimation to DiD validation to optimal tax design. The key findings for my JMP: (1) extensive margin elasticities dominate, supporting RURO's focus on participation; (2) benefit interactions can halve the incentive effects of in-work benefits, making the full tax-benefit schedule essential for welfare analysis; (3) the WFTC is approximately optimal under mild inequality aversion for lone parents with young children. The paper uses standard utilitarian SWF, not equivalent income/fairness criteria, which is a key difference from my approach.
