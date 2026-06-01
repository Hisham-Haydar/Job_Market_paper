---
title: "The Labour Market Impact of the Working Families' Tax Credit"
authors: [Richard Blundell, Alan Duncan, Julian McCrae, Costas Meghir]
year: 2000
outlet: "Fiscal Studies, 21(1), 75--104"
country_or_context: "United Kingdom"
population: "Families with children: lone parents and married/cohabiting couples"
data_period: "1994--96 (Family Resources Survey)"
shelf: "in-work benefits / structural labour supply / microsimulation / WFTC / UK / childcare"
tags: [WFTC, family-credit, in-work-benefits, structural-labour-supply, discrete-choice, microsimulation, TAXBEN, UK, lone-parents, married-women, childcare, participation, secondary-earner, policy-simulation]
priority: "medium"
read_status: "extracted"
---

# Full citation

Blundell, R., Duncan, A., McCrae, J., & Meghir, C. (2000). The Labour Market Impact of the Working Families' Tax Credit. *Fiscal Studies*, 21(1), 75--104.

# One-sentence contribution

Simulates the labour supply effects of replacing the UK's Family Credit with the more generous Working Families' Tax Credit (WFTC) using a discrete-choice structural model with fixed costs of work, childcare costs, and unobserved heterogeneity, finding that lone mothers' participation rises by 2.2 percentage points (~34,000) but married women with employed partners reduce participation by 0.57 ppt (~20,000), yielding a net increase of ~30,000 participants.

# Why this paper matters

This is the seminal UK application of discrete-choice labour supply modelling to in-work benefit reform evaluation. It established the IFS modelling approach (TAXBEN microsimulation + structural discrete-choice) that became the standard for UK policy analysis and influenced the broader European literature. The paper's central finding -- that family-based in-work benefits simultaneously encourage lone parents into work but discourage married women -- became a stylised fact of the in-work benefits literature and motivated the design of individual-based alternatives (like the LWS in Bargain & Orsini 2006).

# Core research question

What is the impact of replacing the UK's Family Credit with the more generous WFTC on hours of work and labour force participation among lone parents and married couples with children?

# Economic setting and context

UK, 1998--99. The WFTC replaced Family Credit (FC) with four key changes: (1) credit for children under 11 increased from £12.35 to £14.85/week, (2) income threshold raised from £79 to £90/week, (3) taper rate reduced from 70% to 55%, (4) childcare credit of 70% of actual costs up to £150/week. WFTC requires at least 16 hours of work per week; 30-hour premium for full-time. Total cost ~£5 billion/year (£1.5 billion more than FC).

Lone parent participation: 40%. Married women in couples: 57%. Married men: 82%. Hours distribution shows spikes at 16 hours (FC eligibility cutoff) for lone parents.

# Model / theoretical framework

**Discrete-choice labour supply (Section V.4):** Each household member chooses from discrete hours points $\{0, 10, 20, 30, 40\}$. Net income at each point computed via TAXBEN microsimulation model.

**Utility specification:** Preferences over household net income and hours, with:
- Fixed costs of working (estimated, vary by demographics)
- Childcare costs (imputed from observed patterns by hours of work, number/age of children, and type of care)
- Unobserved heterogeneity in preferences

**Estimation:** Maximum likelihood on the discrete-choice model. For couples, both male and female labour supply are jointly modelled, though joint responses to WFTC are found to be negligible.

**Simulation:** For each individual, compute choice probabilities at each hours point under FC and WFTC using TAXBEN. Transition matrices built by drawing 100 times from the distribution of unobserved heterogeneity.

# Key objects

- **TAXBEN:** IFS tax and benefit microsimulation model computing household net income at each hours point under full UK tax-benefit rules
- **Budget constraint shifts (Figures 3--7):** Illustrative changes in the relationship between hours and disposable income for lone parents, married men, and married women under FC vs. WFTC
- **Transition matrices (Tables 7--10):** Simulated movements between non-work, part-time, and full-time under the reform
- **Childcare credit:** 70% of actual childcare costs up to £150/week -- the paper carefully models childcare use patterns and their interaction with the WFTC

# Data

Family Resources Survey (FRS), 1994--95 and 1995--96 pooled. ~50,000 UK households per year. After selection (exclude self-employed, students, retired, <17 or >64): 1,807 lone parents, 4,694 couples with children. Childcare expenditure data from FRS for working mothers; imputed for non-workers.

Wages: observed for workers; predicted from selectivity-corrected wage equations for non-workers.

# Identification logic

Standard discrete-choice identification: cross-sectional variation in wages, non-labour income, household composition, and the nonlinear tax-benefit schedule (via TAXBEN). The WFTC reform provides a counterfactual policy change, but the model is estimated on pre-reform data -- the reform is simulated, not evaluated ex post. No quasi-experimental variation or instruments.

# Estimation / empirical strategy

1. Wage equations with selectivity correction on FRS data
2. TAXBEN computes net income at each discrete hours point for each household
3. Childcare costs imputed from observed patterns (Tables A.1, A.2): hours of childcare vary linearly with hours of work; price distribution varies by care type and demographics
4. ML estimation of discrete-choice model with fixed costs and unobserved heterogeneity (detailed in Blundell, Duncan, McCrae & Meghir 1999)
5. Simulation: recompute net incomes under WFTC rules, predict new choice probabilities, build transition matrices
6. Sensitivity analysis across 5 scenarios (Table 11): full/50%/zero childcare credit take-up, increased childcare prices, entry wages for non-workers

# Treatment of preferences

Discrete-choice utility over net income and hours with fixed costs of working and unobserved heterogeneity. Demographics enter through taste-shifters. The paper does not report the structural utility parameters (these are in Blundell et al. 1999). Childcare costs enter as a reduction in net income (increasing the effective cost of working), not as a separate preference parameter.

# Treatment of opportunities / constraints

Not explicitly modelled. All non-employment is treated as voluntary (supply-side model). The paper notes the 16-hour minimum for WFTC eligibility as a policy constraint but does not model demand-side constraints on hours availability. The spike at 16 hours in the hours distribution for lone parents (Figure 2) is attributed to the FC eligibility rule, not to demand-side hours restrictions.

# Welfare / normative object

No welfare analysis. The paper evaluates the reform exclusively on positive criteria: participation changes, hours changes, transition patterns, and programme costs. No equivalent income, compensating variation, or social welfare function.

# Main findings

1. **Lone parents: participation rises by +2.2 ppt (Table 7).** ~34,000 lone mothers move from non-work to part-time or full-time employment. The effect is driven by the higher net income at 16+ hours under WFTC. A small offsetting movement from full-time to part-time (0.5%) reflects the income effect.

2. **Married women with employed partners: participation falls by $-0.57$ ppt (Table 8).** ~20,000 married women leave employment. The mechanism: WFTC increases household income when the husband works (through higher credit), reducing the wife's incentive to work. This is the "secondary earner disincentive" -- the defining problem of family-based in-work benefits.

3. **Married women with unemployed partners: participation rises by +1.32 ppt (Table 9).** ~11,000 women move into work, driven by the increased generosity of basic WFTC relative to FC.

4. **Men in couples: near-zero net effect (+0.07 ppt, Table 10).** Two offsetting flows: 0.4% move into work (mostly from single-earner households), 0.3% leave work (to take advantage of wife's WFTC eligibility).

5. **Net aggregate effect: ~30,000 additional participants.** This is modest given the £1.5 billion additional cost.

6. **Sensitivity analysis (Table 11):** Results are sensitive to childcare credit take-up assumptions. Without the childcare credit, lone parent participation increase drops from 2.2 to 1.3 ppt. Entry wages (lower for non-workers) increase participation response to 3.0 ppt. Increased childcare prices (+50%) offset part of the participation gain.

7. **Budget constraint analysis (Figures 3--7):** WFTC unambiguously increases the financial return to working 16+ hours for lone parents and single-earner couples. For secondary earners in two-earner couples, it can reduce the return to working (Figure 6) because the family loses WFTC eligibility as the wife's earnings push household income above the threshold.

# Main limitations

- Static supply-side model: no dynamics, no job search, no demand-side constraints
- No welfare analysis
- Pre-reform estimation only (no ex-post validation)
- Discrete hours grid {0, 10, 20, 30, 40} is coarse
- Childcare costs imputed, not directly observed for non-workers
- Full take-up assumption for baseline (actual take-up ~69% for FC)
- No general equilibrium or wage effects
- Structural model details not in this paper (in Blundell et al. 1999)

# Relevance for my JMP

## possible use for the secondary earner problem
The paper documents the fundamental trade-off in family-based in-work benefits: they help lone parents but hurt secondary earners. This is relevant for my JMP because: (1) the welfare impact depends on whether the married women who leave work do so voluntarily (preference-driven, no welfare loss) or are discouraged (welfare loss), and (2) the RURO framework could distinguish these cases through the opportunity density.

## possible use for the UK policy context
This paper is the reference for how the IFS structural labour supply modelling approach works in practice. The TAXBEN + discrete-choice pipeline is the UK analogue of EUROMOD + Van Soest used in continental European studies. Bargain & Orsini (2006) explicitly compare their continental European results with Blundell et al.'s UK findings.

## possible use for childcare modelling
The paper's careful treatment of childcare costs (Tables A.1, A.2) -- imputed from observed patterns, varying by hours, number/age of children, and care type -- is methodologically relevant. Childcare costs effectively reduce the net return to working, similar to how fixed costs operate in the Van Soest framework or how the opportunity density's shape reflects demand-side constraints in the RURO framework.

# Research questions this paper inspires

1. The paper finds that married women with employed partners reduce their labour supply under WFTC. In the RURO framework, would these women's equivalent incomes increase (because household income rises even though they work less) or decrease (because they lose the "rent from working")? The answer depends on whether the women value the additional leisure.

2. Would demand-side constraints moderate the secondary earner disincentive? If some married women are involuntarily non-participating (no jobs available), the WFTC's income effect cannot pull them out of work because they are already not working. The pure supply-side model may overstate the negative participation effect.

# Challenge to this paper

The paper's finding that WFTC reduces married women's participation is driven by the assumption that all current workers are voluntary participants who could reduce their labour supply in response to higher household income. If some married women work because they must (binding budget constraint, no opportunity to reduce hours), the income effect would be smaller. More fundamentally, the paper cannot assess whether the net effect of WFTC on social welfare is positive or negative: the 34,000 lone mothers who enter work may gain more in welfare than the 20,000 married women who leave lose. Without a welfare metric (equivalent income), the reform's overall desirability remains unevaluated.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper models the $y \to z$ mapping: how changing the tax-benefit schedule (FC → WFTC) changes labour supply bundles. $R$ (preferences) is captured by the structural utility; $y$ (tax-benefit) is modelled via TAXBEN; $z$ (realised bundle) is the predicted hours-income choice; $A$ (opportunities) is not modelled.

[Reasonable inference for my project] The secondary earner disincentive is a key example of how $y$-changes (tax-benefit reform) affect different agents differently depending on their position: lone parents (for whom WFTC relaxes the budget constraint) vs. married women (for whom WFTC raises the reservation wage). In $W(z, R, A; y)$ terms, the reform changes $y$ but the welfare effect depends on $R$ (how much the agent values leisure vs. income) and $A$ (whether alternatives are available).

[Unclear from paper] The welfare implications. The paper provides no welfare analysis, making it impossible to assess whether the 30,000 net additional participants represents a net welfare gain or loss. The RURO equivalent-income framework would answer this by computing individual-level welfare changes.

# Relation to Bargain et al. (2013)

This paper is a methodological precursor. It uses the same discrete-choice + microsimulation pipeline but stops at positive analysis. Bargain et al. (2013) add the welfare dimension. The secondary earner disincentive documented here motivates the welfare analysis in Bargain et al.: is the married woman who stops working under WFTC better or worse off? The equivalent-income metric can answer this; the positive model cannot.

# Relation to opportunities vs preferences

The paper does not distinguish opportunities from preferences. The 16-hour spike in lone parents' hours distribution is attributed to the FC eligibility rule (a policy constraint on the $y$-schedule), not to demand-side hours restrictions. The RURO framework would model this spike through the interaction of the opportunity density $g(h,w)$ (which may have limited availability at 10--15 hours) and the policy constraint (16-hour minimum for WFTC).

# Useful quotations / formulas

**On the secondary earner effect (p. 87):**
"For the illustrative example shown here, any woman working more than 10 hours will have an increased incentive to reduce her labour supply or move out of work altogether."

**On the net effect (p. 100--101):**
"The participation rate for single mothers increases by around 2.2 percentage points... the participation rate for married women with employed partners decreases by 0.57 percentage points... a small increase in overall participation of around 30,000 individuals."

**On the structural approach (p. 92):**
"Since our study involves the simulation of a tax reform that has yet to be implemented, rather than an evaluation of a tax reform already in operation, we require a structural model for household labour supply."

# Suggested tags

WFTC, family-credit, in-work-benefits, UK, structural-labour-supply, discrete-choice, TAXBEN, microsimulation, lone-parents, married-women, secondary-earner, childcare, participation, policy-simulation, IFS, Blundell

# My quick takeaway

The definitive UK study of WFTC's labour supply effects. The finding that family-based in-work benefits simultaneously help lone parents (+2.2 ppt) and hurt secondary earners ($-0.57$ ppt) became a stylised fact motivating the design of individual-based alternatives. For my JMP, the paper illustrates the standard methodology (discrete-choice + microsimulation) and its key limitation: it evaluates reforms on participation and hours but not on welfare. The question "Is WFTC welfare-improving?" requires equivalent-income analysis (Bargain et al. 2013) and ideally the $R$-$A$ decomposition from the RURO framework to distinguish between voluntary and involuntary labour supply responses.
