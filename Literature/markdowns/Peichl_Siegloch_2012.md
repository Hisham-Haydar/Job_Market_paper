---
title: "Accounting for Labor Demand Effects in Structural Labor Supply Models"
authors: [Andreas Peichl, Sebastian Siegloch]
year: 2012
outlet: "Labour Economics, 19(1), 129--138"
country_or_context: "Germany"
population: "Single men, single women, couples (working-age population)"
data_period: "2009 (SOEP wave 2010, tax system January 2009; LIAB 1996--2007 for demand)"
shelf: "labour demand / supply-demand link / structural labour supply / workfare / policy simulation"
tags: [labour-demand, labour-supply, demand-supply-link, discrete-choice, translog, workfare, policy-reform, demand-elasticities, skill-groups, iteration, Germany, SOEP, LIAB, fiscal-effects]
priority: "medium"
read_status: "extracted"
---

# Full citation

Peichl, A., & Siegloch, S. (2012). Accounting for Labor Demand Effects in Structural Labor Supply Models. *Labour Economics*, 19(1), 129--138.

# One-sentence contribution

Proposes and implements an iterative demand-supply link for structural discrete-choice labour supply models: after estimating separate labour supply and labour demand models on German microdata, the paper iterates wage and employment adjustments until partial equilibrium is reached, showing that labour demand offsets about 25% of the pure labour supply effect of a workfare reform.

# Why this paper matters

Standard structural labour supply models implicitly assume perfectly elastic labour demand (i.e., any increase in labour supply translates one-for-one into employment). This paper shows that demand restrictions matter quantitatively: for a workfare reform in Germany, demand effects reduce the employment gain from 1.5 million to 1.1 million FTE jobs. The approach is parsimonious (stays at the micro level, uses microdata for both sides), avoids the aggregation problems of CGE models, and is general enough to be combined with any discrete-choice labour supply model.

# Core research question

How can labour demand effects be incorporated into structural labour supply models at the micro level, and how large are these demand-side adjustments for a realistic policy reform (workfare)?

# Economic setting and context

Germany, 2009 tax-benefit system. The workfare reform requires every employable individual receiving government benefits to work full-time (40 hours/week) in a community job in exchange for transfers. This is a pure labour supply shift -- demand does not change -- making it ideal for illustrating the demand-supply iteration. Labour demand is estimated from linked employer-employee data (LIAB) covering German establishments 1996--2007.

# Model / theoretical framework

**Labour supply (Section 3):** Standard van Soest (1995) discrete-choice model. Translog utility for couple household $i$:
$$U_{ij} = \alpha_{C_i} \ln C_{ij} + \alpha_{h_{f,i}} \ln h_{ij}^f + \alpha_{h_{f2}} (\ln h_{ij}^f)^2 + \alpha_{h_{m,i}} \ln h_{ij}^m + \alpha_{h_{m2}} (\ln h_{ij}^m)^2 + \alpha_{CC} (\ln C_{ij})^2 + \alpha_{Ch} \ln C_{ij} \ln h_{ij}^f + \alpha_{Ch_m} \ln C_{ij} \ln h_{ij}^m + \alpha_{h_fh_m} \ln h_{ij}^f \ln h_{ij}^m + \beta_f D_{ij}^f + \beta_m D_{ij}^m$$

Seven hours categories per individual (0, 10, 20, 30, 40, 50, 60). $J = 49$ for couples. McFadden conditional logit with extreme-value error terms.

**Labour demand (Section 4):** Translog cost function for firm output $Y$:
$$\ln C(w_i, Y) = \alpha_0 + \sum_i \alpha_i \ln w_i + 0.5 \sum_i \sum_j \alpha_{ij} \ln w_i \ln w_j + \beta_Y \ln Y + 0.5 \beta_{YY} (\ln Y)^2 + \sum_i \beta_{iY} \ln w_i \ln Y + \delta_i t + \ldots$$

with symmetry, homogeneity, and adding-up restrictions. Three skill types: high-skilled, medium-skilled, low-skilled. Cost shares:
$$S_i = \alpha_i + \sum_j \alpha_{ij} \ln w_j + \beta_{iY} \ln Y + \delta_{it} t$$

Own-wage demand elasticity: $\bar{\eta}_{ii}^{\Pi} = \frac{\alpha_{ii} - \hat{S}_i + \hat{S}_i^2}{\hat{S}_i}$

Cross-wage elasticity: $\bar{\eta}_{ij}^{\Pi} = \frac{\alpha_{ij} + \hat{S}_i \hat{S}_j}{\hat{S}_i}$

Estimated via Seemingly Unrelated Regressions (SUR) with iterated FGLS.

**Demand-supply iteration (Section 5):**
1. Compute change in net income from reform
2. Simulate labour supply effect (hours change $\Delta E$)
3. Use demand elasticity to compute wage adjustment: $\Delta w = f(\Delta E, \eta)$
4. Re-simulate labour supply given new wage
5. Repeat steps 3--4 until relative change in hours < 0.1%

Iteration converges to partial labour market equilibrium where supply equals demand at each skill level.

# Key objects

- **Labour demand elasticities (Table 1):**
  - High-skilled own-wage: $-0.56$
  - Medium-skilled own-wage: $-0.37$
  - Low-skilled own-wage: $-1.05$
  - Key cross-wage: medium-skilled workers are substitutes for both high and low-skilled
- **LS/LD offset ratio (Table 2):** The percentage by which demand effects reduce the pure labour supply effect. Overall: $-25.31\%$. Ranges from $-3.81\%$ (high-skilled) to $-31.05\%$ (medium-skilled).
- **Convergence (Table 3):** Iteration converges in 3--9 steps depending on household type and skill group. Higher demand elasticity (in absolute terms) → faster convergence.

# Data

**Labour supply:** German SOEP, wave 2010 (incomes from 2009). ~25,000 individuals in ~12,000 households. Five demographic subgroups. Tax-benefit system modelled via IZA¥MOD microsimulation.

**Labour demand:** Linked Employer-Employee Dataset (LIAB) from IAB Nuremberg. Links IAB Establishment Panel (representative sample of ~4,073 establishments, stratified, 1996--2007) with administrative employee data from the German employment register. 13,451 establishment-year observations. Covers private sector (public excluded as hours are inflexible). Three skill groups based on qualification: high (university/polytechnic), medium (vocational training or *Abitur*), low (no completed vocational training or *Abitur*).

# Identification logic

**Supply side:** Standard discrete-choice identification from variation in hours, wages, non-labour income, and tax-benefit nonlinearities.

**Demand side:** SUR estimation of cost share equations using variation in wages across skill types, output, time, and industry dummies. Identification from cross-sectional and time-series wage variation across establishments and skill groups. Demand elasticities assumed constant along the demand curve (local approximation).

**Iteration:** The iteration assumes perfectly competitive labour markets, constant demand elasticities, and that the labour supply model correctly captures behavioural responses. Convergence is not theoretically guaranteed but achieved in practice.

# Estimation / empirical strategy

1. **Wage equations:** Predicted wages for all individuals (employed and non-employed) using standard Mincer approach.
2. **Labour supply model:** Conditional logit on SOEP, estimated separately by household type.
3. **Demand model:** SUR on LIAB cost share equations with industry dummies. Iterated FGLS until convergence.
4. **Policy simulation:** Workfare reform → compute pure supply effect → iterate with demand adjustments → partial equilibrium.
5. **Robustness:** Low/high elasticity scenarios (±20% wage elasticities); alternative reform scenarios; alternative utility specifications; alternative discretisations.

# Treatment of preferences

Standard translog utility with observed heterogeneity (age, children, region) and fixed costs of working. No unobserved preference heterogeneity (no random coefficients). The paper notes that the qualitative results are robust to the choice of utility specification and the number of discrete hours categories.

# Treatment of opportunities / constraints

The paper's central contribution is incorporating demand-side constraints. However, opportunities are modelled only through the aggregate demand function (wage-employment relationship by skill group), not through individual-level opportunity sets. There is no RURO-style opportunity density -- the demand side operates at the skill-group level, adjusting wages uniformly for all workers within a skill group. This is a much coarser representation of demand than the RURO model's individual-specific opportunity sets.

# Welfare / normative object

No welfare analysis per se. The paper computes fiscal effects (Table 4): the workfare reform increases the government budget by €15.7 billion after accounting for demand adjustments (vs. €31.7 billion from pure supply effects). The demand adjustment reduces the fiscal gain by approximately 50% (through lower tax revenue on reduced wages).

# Main findings

1. **Labour demand elasticities (Table 1):** Own-wage elasticities: $-0.56$ (high), $-0.37$ (medium), $-1.05$ (low). All negative and finite, confirming that labour demand is not perfectly elastic. Low-skilled demand is most elastic. Medium-skilled workers are substitutes for both high and low-skilled.

2. **Demand offsets supply by 25% (Table 2):** The pure labour supply effect of workfare is +1,491,000 FTE. Demand restrictions reduce this by 377,400 FTE (25.3%). The offset is largest for medium-skilled ($-31.1\%$) and women in couples ($-30.1\%$), smallest for high-skilled ($-3.8\%$).

3. **Convergence (Table 3):** The iteration converges in 3--9 steps. Higher absolute demand elasticity → faster convergence (smaller wage adjustments needed per employment change). Wage and hours adjustments alternate in sign, consistent with the graphical intuition (Fig. 1).

4. **Fiscal effects (Table 4):** After demand adjustments, the budget gain from workfare shrinks from €31.7B to €15.7B. The reform remains fiscally positive even after demand effects.

5. **Sensitivity (Table 5):** Demand offset ranges from 15% to 35% depending on the elasticity scenario and reform type. Higher demand elasticity (in absolute terms) → smaller offset (demand adjusts via smaller wage changes). The qualitative finding is robust across all scenarios.

6. **Robustness:** Results are robust to: alternative utility functions (quadratic, Box-Cox), different numbers of discrete hours categories, inclusion of capital as quasi-fixed input, alternative reform scenarios.

# Main limitations

- Assumes perfectly competitive labour markets (price-taking firms, market-clearing wages)
- Demand elasticities assumed constant (valid only for small changes)
- Only three skill groups (no finer demand disaggregation by occupation, industry, etc.)
- No general equilibrium: ignores output, consumption, and price feedback effects
- Static: no dynamic adjustment, no intertemporal labour supply responses
- Public sector excluded from demand model
- Demand adjustments are at the skill-group level, not individual-specific
- No uncertainty about demand elasticity estimates in the iteration

# Relevance for my JMP

## possible use for framing
The paper demonstrates that ignoring labour demand biases employment predictions by ~25%. This is relevant for the $W(z, R, A; y)$ framework: the $A$-component (feasible job set) depends on demand-side factors. A policy reform that shifts labour supply also changes $A$ through wage adjustments, which standard supply-only models miss.

## possible use for model design
The paper's iterative approach could be adapted for the RURO framework. In RURO, demand-side effects could be incorporated by letting the opportunity density $g(h, w)$ respond to labour supply changes: if supply of low-skilled workers increases, the opportunity density shifts toward lower wages, changing the feasible set $A$. This would be a micro-founded version of the paper's macro-level iteration.

## possible use for welfare implications
The paper shows that demand effects reduce the fiscal gain of workfare by ~50%. For welfare analysis, this means that $W(z, R, A; y)$ should account for demand-induced changes in $A$ (fewer/worse job opportunities when supply expands) and $y$ (lower wages), not just the direct policy change in $y$ (tax schedule).

## possible use for limitations discussion
The paper's limitation -- demand adjustments at the skill-group level only -- is exactly what the RURO framework addresses by modelling individual-specific opportunity sets. The paper's approach treats all medium-skilled workers as facing the same wage adjustment, while in reality, demand effects may vary by occupation, sector, region, and hours.

# Research questions this paper inspires

1. Can the demand-supply iteration be embedded in a RURO model where the opportunity density $g(h, w)$ adjusts endogenously to labour supply changes? This would give individual-level demand effects rather than skill-group averages.

2. How does the 25% demand offset vary across countries and institutional settings? In highly regulated labour markets (minimum wages, collective bargaining), the offset may be larger because wages are stickier.

3. What are the welfare implications of demand-side effects? If demand effects reduce wages for low-skilled workers, the welfare loss may be disproportionately borne by the poor -- even if aggregate employment increases.

4. Can the demand model be disaggregated by hours (part-time vs. full-time demand) to interact with the hours dimension of the opportunity density?

# Challenge to this paper

The paper's demand model is estimated at the establishment level using three skill groups, then applied to individual-level labour supply adjustments. This creates an aggregation inconsistency: the demand elasticity for "medium-skilled workers" is a weighted average across all establishments, but individual workers face establishment-specific demand. A medium-skilled nurse in a hospital faces different demand than a medium-skilled factory worker, yet both receive the same wage adjustment in the iteration. The RURO framework's individual-specific opportunity density would handle this heterogeneity naturally, though at the cost of requiring much more detailed demand-side data.

Moreover, the assumption that demand elasticities are constant along the demand curve is problematic for the workfare reform, which involves very large labour supply shifts (1.5 million FTE). For shifts of this magnitude, the constant-elasticity approximation may break down, and the true demand offset could be larger than 25%.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper shows that ignoring demand effects leads to biased employment predictions. In the $W(z, R, A; y)$ framework, demand effects change both $A$ (the feasible job set shifts as wages adjust) and $y$ (the wage schedule changes), affecting welfare through both channels.

[Reasonable inference for my project] The paper's approach operates at the macro (skill-group) level, while the RURO framework operates at the micro (individual) level. Combining them would require the opportunity density $g(h, w)$ to respond to aggregate demand conditions -- a structural extension that would make welfare analysis fully consistent with labour market equilibrium.

[Unclear from paper] How demand effects interact with the preference-opportunity decomposition in $W(z, R, A; y)$. When demand effects reduce wages, is this a change in $A$ (fewer high-wage jobs available) or a change in $y$ (the pay schedule shifts)? The distinction matters for welfare: an $A$ change affects feasibility, while a $y$ change affects the budget constraint.

The paper is closest to: **incorporating demand-side constraints into structural labour supply models** and **demonstrating the quantitative importance of demand effects for policy evaluation**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute welfare metrics from a pure supply-side model. Peichl and Siegloch (2012) show that demand effects can offset supply effects by 25%. This suggests that welfare calculations ignoring demand may overstate the welfare gains from labour supply-expanding reforms (workfare, EITC) because they miss the wage depression from increased supply. The demand-adjusted welfare effect would be smaller and potentially more regressive (low-skilled workers bearing the wage reduction).

# Relation to opportunities vs preferences

The paper contributes to the opportunities side of the framework: demand restrictions limit the job opportunities available to workers. However, the demand effects are modelled at the aggregate level (skill-group wages) rather than at the individual level (opportunity densities). In the RURO framework, demand effects would be captured by changes in the opportunity density $g(h, w)$: when labour supply increases, the density shifts toward lower wages (or fewer available jobs), directly affecting the $A$-component of $W(z, R, A; y)$. The paper's approach is a first step toward this but operates at a much coarser level.

# Useful quotations / formulas

**On the bias from ignoring demand (Abstract):**
"We find that demand effects offset about 25% of the positive labor supply effect of the policy reform."

**On the iteration (p. 133):**
"1. The change in net income due to the tax reform is calculated. 2. The labor supply effect is simulated, given the new net income. 3. The gross wage adjusts according to the supply effect and the labor demand function. 4. The labor supply effect is re-simulated given the new wage. 5. If the relative change in working hours is greater than 0.1%, repeat steps 3 and 4."

**Demand elasticities (Table 1):** High-skilled: $-0.56$; Medium-skilled: $-0.37$; Low-skilled: $-1.05$.

**On labour demand as stabiliser (p. 136):**
"labor demand works as a stabilizer to employment shifts [...] In all cases, demand adjustments soften this effect, so that the resulting employment effect is less negative than the initial labor supply reaction."

**On fiscal implications (p. 135):**
"the workfare reform [...] increases by 31.7 billion euros [...] The countervailing demand effect, of course, reduces this positive budget effect to 27.7 billion euros"

# Suggested tags

labour-demand, labour-supply, demand-supply-link, discrete-choice, translog, cost-function, SUR, workfare, policy-reform, demand-elasticities, skill-groups, iteration, partial-equilibrium, Germany, SOEP, LIAB, linked-employer-employee, fiscal-effects, wage-adjustment, employment

# My quick takeaway

This paper provides a clean, parsimonious method for incorporating labour demand into structural labour supply models. The key quantitative result -- demand offsets 25% of supply effects -- is important for policy evaluation and welfare analysis. For my JMP, the paper motivates extending the RURO framework to allow the opportunity density $g(h,w)$ to respond to aggregate labour market conditions. The paper's limitation (demand at skill-group level only) is exactly what the RURO approach, with its individual-level opportunity sets, is designed to overcome. The welfare implication is that $W(z, R, A; y)$ should account for demand-induced changes in both $A$ and $y$, not just the direct policy change.
