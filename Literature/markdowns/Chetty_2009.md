---
title: "Sufficient Statistics for Welfare Analysis: A Bridge Between Structural and Reduced-Form Methods"
authors: [Raj Chetty]
year: 2009
outlet: "Annual Review of Economics, 1, 451--487"
country_or_context: "Theoretical survey with US applications"
population: "N/A (general framework)"
data_period: "N/A"
shelf: "welfare analysis / sufficient statistics / optimal taxation / social insurance / methodology"
tags: [sufficient-statistics, welfare-analysis, deadweight-loss, Harberger, envelope-theorem, elasticity, taxable-income, optimal-tax, social-insurance, behavioral, structural, reduced-form, methodology, survey]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Chetty, R. (2009). Sufficient Statistics for Welfare Analysis: A Bridge Between Structural and Reduced-Form Methods. *Annual Review of Economics*, 1, 451--487.

# One-sentence contribution

Develops a general framework showing how envelope conditions from optimization can be used to derive welfare formulas that depend on a small set of high-level elasticities (sufficient statistics) rather than deep structural primitives, bridging the structural and reduced-form approaches to policy evaluation, and illustrates with applications to income taxation (Feldstein 1999, Saez 2001), social insurance (Baily 1978, Chetty 2008), and behavioral models.

# Why this paper matters

The paper reconciles two competing paradigms in applied economics: (1) structural models that estimate all primitives but face identification challenges, and (2) reduced-form program evaluation that achieves credible identification but cannot directly address welfare. The sufficient-statistic approach shows that welfare formulas can often be expressed in terms of a few estimable elasticities, providing the counterfactual welfare predictions of structural models with the transparent identification of reduced-form methods. This is directly relevant for labour supply welfare analysis: the question is whether one needs a full structural model (like RURO) or whether sufficient statistics (like the elasticity of taxable income) suffice for welfare evaluation.

# Core research question

How can welfare consequences of government policies be expressed as functions of reduced-form elasticities rather than structural primitives, and what are the advantages and limitations of this approach relative to full structural estimation?

# Economic setting and context

Theoretical survey with illustrative applications to US tax policy, unemployment insurance, and behavioral economics. The framework is general and applies to any setting where agents optimize subject to constraints affected by a policy instrument.

# Model / theoretical framework

**General framework (Section 3):** Agent maximises utility subject to $M$ constraints:

$$\max_x U(x) \text{ s.t. } G_1(x, t, T) = 0, \ldots, G_M(x, t, T) = 0$$

where $t$ is the tax rate and $T$ is the transfer. Social welfare:

$$W(t) = \max_x U(x) + \sum_{m=1}^M \lambda_m G_m(x, t, T)$$

**Six-step rubric for deriving sufficient-statistic formulas:**
1. Specify the structure of the model (utility, constraints)
2. Express $dW/dt$ in terms of multipliers using envelope conditions (eq. 14)
3. Substitute multipliers by marginal utilities using FOCs (eq. 15)
4. Recover marginal utilities from observed choices
5. Empirical implementation
6. Model evaluation

**Key result (eq. 15):** Under Assumption 1 (tax and transfer enter constraints interchangeably):

$$\frac{dW}{dt} = k_T \frac{dT}{dt} u'(x_J(t)) - k_t u'(x_1(t))$$

Welfare change reduces to recovering a pair of marginal utilities.

**Harberger formula (eq. 4):** With quasilinear utility and no pre-existing distortions:

$$\frac{dW}{dt} = t \frac{dx_1(t)}{dt}$$

The effect on equilibrium quantity is a sufficient statistic for the marginal excess burden.

**Discrete choice extension (eqs. 8--11):** With heterogeneous agents and discrete choice (multinomial logit), welfare is:

$$W = \sum_i \log\left(\sum_j \exp(v_{ij})\right) + p \cdot P - c(P)$$

The aggregate demand response $dP_1/dt$ remains the sufficient statistic (eq. 11), even though individual demand functions are discontinuous.

**Feldstein (1999) -- Taxable income (eq. 21):**

$$\frac{dW(t)}{dt} = t \frac{dTI(t)}{dt}$$

The elasticity of taxable income is a sufficient statistic for the deadweight cost of income taxation, aggregating responses across all margins (hours, effort, evasion, avoidance).

**Saez (2001) -- Optimal tax rate (eq. 24):**

$$\frac{\tau^*}{1 - \tau^*} = \frac{1 - \bar{g}}{a\varepsilon}$$

where $\varepsilon$ = taxable income elasticity, $a$ = Pareto parameter, $\bar{g}$ = social marginal welfare weight. Three sufficient statistics determine the optimal top rate.

**Optimal nonlinear tax (eq. 25):**

$$\frac{T'(z)}{1 - T'(z)} = \frac{1}{\varepsilon(z) z h(z)} \int_z^\infty (1 - g(z')) h(z') dz'$$

**Baily (1978) / Chetty (2006a) -- Social insurance (eq. 27):**

$$M_W(b) = \frac{u'(c_l) - u'(c_h)}{u'(c_h)} - \frac{\varepsilon_{1-e,b}}{e}$$

Two sufficient statistics: (1) gap in marginal utilities between good and bad states, (2) moral hazard elasticity.

**Chetty (2008) -- Liquidity vs. moral hazard (eq. 33):**

$$M_W(b) = \frac{-\partial e / \partial A}{\partial e / \partial A - \partial e / \partial b} - \frac{\varepsilon_{1-e,b}}{e}$$

The ratio of the liquidity effect to the substitution effect on effort recovers the marginal utility gap without assuming a specific utility function.

**Behavioral models -- Tax salience (eq. 36):**

$$\frac{dW}{dt} = t\theta \frac{dx}{dt}$$

where $\theta = (dx/dt)/(dx/dp)$ is the degree of underreaction to the tax relative to prices. Both price and tax elasticities are sufficient statistics.

# Key objects

- **Sufficient statistic $\beta$:** A high-level parameter (typically an elasticity) that, together with the policy instrument $t$, determines $dW/dt$. Multiple structural primitives $\omega$ map to the same $\beta$.
- **Envelope condition:** Behavioral responses $dx/dt$ have no first-order effect on private welfare because agents are optimising. This eliminates the need to identify the full demand system.
- **Elasticity of taxable income $dTI/dt$:** Sufficient statistic for the deadweight cost of income taxation.
- **Moral hazard elasticity $\varepsilon_{1-e,b}$:** The elasticity of the probability of being in the bad state with respect to the benefit level -- measures the fiscal externality of insurance.
- **$\theta$:** Degree of underreaction to taxes relative to prices in behavioral models.

# Data

No original data. Reviews applications using US tax data (Feldstein 1995), UI benefit data (Gruber 1997, Chetty 2008), and sales tax experiments (Chetty et al. 2009).

# Identification logic

The key insight is that welfare formulas derived from envelope conditions require identification of fewer parameters than the full structural model. For example:
- Harberger: only $dx_1/dt$ needed, not the full demand and supply systems
- Feldstein: only $dTI/dt$ needed, not separate hours, effort, and evasion elasticities
- Baily: only the marginal utility gap and moral hazard elasticity, not the full dynamic search model

Identification of sufficient statistics can use reduced-form methods (quasi-experiments, RD, IV) under weaker assumptions than structural estimation.

# Estimation / empirical strategy

Not applicable (methodological survey). Discusses empirical strategies for each application.

# Treatment of preferences

Preferences are general: the framework does not require specific functional forms for utility. The envelope condition eliminates behavioral responses from $dW/dt$, so the welfare formula does not depend on the curvature or shape of utility -- only on marginal utilities at the optimum, which can be backed out from FOCs. For behavioral models (Section 6), the approach relaxes the assumption of full optimisation but requires that agents optimise correctly in one dimension (Assumption 2: correct choices when prices are fully salient).

# Treatment of opportunities / constraints

Opportunities enter through the constraints $G_m(x, t, T) = 0$. The framework handles budget constraints, hours restrictions, insurance constraints, and borrowing constraints. However, opportunities are not modelled as heterogeneous across individuals in the way the RURO framework does -- the sufficient-statistic approach aggregates across heterogeneous agents to work with aggregate elasticities.

# Welfare / normative object

The welfare object is $dW/dt$: the marginal welfare gain from changing the policy instrument $t$ with accompanying transfer $T(t)$. This is a money-metric welfare measure (equivalent to the change in equivalent or compensating variation when utility is quasilinear). The paper focuses on efficiency (total surplus) rather than distributional welfare, except in the Saez (2001) application where social-welfare weights $\bar{g}$ enter.

# Main findings

1. **The sufficient-statistic approach bridges structural and reduced-form methods:** Welfare formulas can be expressed as functions of estimable elasticities, combining the welfare predictions of structural models with the credible identification of program evaluation.

2. **Envelope conditions are the key tool:** Because agents optimise, behavioral responses have no first-order welfare effects. This eliminates the need to identify the full demand system and reduces the welfare formula to a function of marginal utilities and fiscal externalities.

3. **Three applications demonstrate generality:**
   - **Taxation:** Elasticity of taxable income is sufficient for deadweight loss (Feldstein); three parameters (elasticity, Pareto parameter, welfare weight) determine optimal tax rates (Saez)
   - **Social insurance:** Gap in marginal utilities + moral hazard elasticity are sufficient (Baily/Chetty); can be recovered from liquidity vs. substitution effects (Chetty 2008) or reservation wages (Shimer & Werning 2007)
   - **Behavioral models:** Price and tax elasticities together are sufficient even when agents misoptimise (Chetty et al. 2009)

4. **Structural and sufficient-statistic approaches are complements:** Structural models provide guidance for out-of-sample extrapolation and for choosing which elasticities to estimate. Sufficient-statistic formulas identify the specific parameters that matter, reducing the dimensionality of the estimation problem.

5. **Model evaluation is important but under-implemented:** Sufficient-statistic formulas still rest on modelling assumptions (e.g., optimisation, no pre-existing distortions). Testing these assumptions (step 6 of the rubric) is often neglected.

# Main limitations

- Requires quasilinear utility or specific normalisation for welfare to be a money metric
- Local approximation: formulas give marginal ($dW/dt$), not global ($\Delta W$), welfare effects
- Pre-existing distortions require additional terms (Goulder & Williams 2003)
- Cannot address distributional questions without social-welfare weights
- Sufficient statistics may vary with the policy instrument $t$, requiring estimation as a function of $t$
- The approach is silent on which individuals gain or lose -- only aggregate welfare
- For large reforms, the linear approximation may be inaccurate

# Relevance for my JMP

## possible use for framing
The paper frames the fundamental methodological choice: does one need a full structural model (RURO) to evaluate welfare, or do sufficient statistics (elasticities of taxable income, labour supply) suffice? For my JMP, the answer depends on the welfare question: if the question is about the efficiency cost of taxation, sufficient statistics may suffice; if the question is about the distribution of welfare across individuals with different opportunities ($A$), a structural model is needed.

## possible use for positioning the structural approach
The paper's framework shows that structural estimation is most valuable when: (1) multiple policy questions need to be answered (the structural model provides all elasticities at once), (2) out-of-sample prediction is required, (3) heterogeneity matters for welfare (distributional analysis). All three conditions apply to my JMP: the RURO framework answers multiple policy questions (different tax reforms), makes out-of-sample predictions (counterfactual tax schedules), and provides heterogeneous welfare effects (across individuals with different $R$ and $A$).

## possible use for welfare formula comparison
The paper's welfare formulas (Harberger, Feldstein, Saez) provide benchmarks against which the RURO welfare calculations can be compared. If the RURO model is well-specified, the welfare effects from microsimulation should be consistent with the sufficient-statistic formulas. Discrepancies would signal model misspecification.

## possible use for the envelope theorem argument
The paper's key insight -- that behavioral responses have no first-order welfare effect due to the envelope condition -- applies to the RURO framework as well. When computing equivalent income changes from a tax reform, the change in hours/job choice has no first-order effect on utility (the individual was optimising at the margin). This simplifies welfare calculations.

# Research questions this paper inspires

1. Is there a sufficient-statistic formula for the welfare effect of changing the opportunity set $A$ (e.g., creating more part-time jobs)? The standard formulas assume that the choice set is fixed and only prices/taxes change. Expanding the choice set is not a price change but a change in the constraint.

2. Can the sufficient-statistic approach be extended to account for demand-side effects (Peichl & Siegloch 2012)? The Harberger formula assumes competitive markets with endogenous price adjustment. With labour demand constraints, the sufficient statistic may need to include both the supply elasticity and the demand elasticity.

3. The paper shows that $dW/dt = t \cdot dTI/dt$ for the efficiency cost of income taxation. In the RURO framework, does the welfare effect of a tax reform depend only on the change in taxable income, or does the change in opportunity utilisation (which jobs people take) contribute independently to welfare?

# Challenge to this paper

The sufficient-statistic approach is powerful for efficiency analysis but fundamentally limited for the kind of welfare analysis my JMP pursues. The approach measures aggregate welfare effects ($dW/dt$) but cannot decompose welfare changes across individuals with different preferences ($R$) and opportunities ($A$). The Saez (2001) formula introduces distributional weights $\bar{g}$, but these are exogenous (chosen by the planner) rather than derived from the structural model. The RURO framework can derive endogenous welfare weights by computing individual-level equivalent incomes and then applying maximin/leximin, which is a fundamentally different approach.

Moreover, the envelope-condition argument assumes that agents are optimising. If workers face rationed choice sets (as in the RURO model, where the available jobs are a random draw from $g(h,w)$), the worker is optimising over the available set but not over the full set -- the envelope condition applies to the available set but not to the welfare effect of changing the available set. This means that changes in $A$ (opportunity) have first-order welfare effects that cannot be captured by elasticities alone.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides welfare formulas based on envelope conditions and elasticities. In the $W(z, R, A; y)$ framework, these formulas capture the welfare effect of changing $y$ (the tax schedule) but not $A$ (the opportunity set) or $R$ (preferences).

[Reasonable inference for my project] The sufficient-statistic approach and the structural RURO approach are complements for my JMP. The sufficient-statistic formulas provide a check: do the RURO-based welfare calculations give results consistent with $dW/dt = t \cdot dTI/dt$? If yes, the structural model passes a basic validity test. If not, either the model or the sufficient-statistic formula is misspecified (e.g., due to hours restrictions, demand effects, or behavioral frictions).

[Unclear from paper] Whether there exists a sufficient-statistic formula for the welfare effect of opportunity changes (changes in $A$). The standard formulas assume fixed choice sets with varying prices/taxes. Opportunity changes (more part-time jobs, new sectors, reduced discrimination) are fundamentally different from price changes because they expand the constraint set rather than shifting the budget constraint.

The paper is closest to: **the methodological foundation for welfare analysis** and **the bridge between reduced-form elasticities and structural welfare evaluation**.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) take the full structural approach: they estimate all preference parameters and simulate welfare effects for each individual. The Chetty (2009) sufficient-statistic approach would instead use aggregate elasticities (e.g., elasticity of hours or participation with respect to the tax rate) to compute aggregate welfare effects. The structural approach in Bargain et al. is more informative because it provides individual-level welfare decompositions (preferences vs. opportunities), but it is also more vulnerable to misspecification. The sufficient-statistic approach provides a robustness check.

# Relation to opportunities vs preferences

The paper does not distinguish between opportunities and preferences. The envelope condition treats preferences as generating optimal choices, and welfare is computed from the marginal utility of the optimal choice. The opportunity set is implicit in the constraints $G_m$, but changes in the opportunity set are not analysed. This is a fundamental gap relative to the RURO framework, where the opportunity density $g(h,w)$ is a central object and changes in $g(h,w)$ have first-order welfare effects.

# Useful quotations / formulas

**Central concept (p. 452, Figure 1 caption):**
"The sufficient-statistic approach [...] leaves $\omega$ unidentified and instead identifies a smaller set of high-level parameters ($\beta$) using program-evaluation methods. [...] The $\beta$ vector is sufficient for welfare analysis in that any vector $\omega$ consistent with $\beta$ implies the same value of $\frac{dW}{dt}$."

**Harberger formula (eq. 4):**
$$\frac{dW(t)}{dt} = t \frac{dx_1(t)}{dt}$$

**Feldstein formula (eq. 21):**
$$\frac{dW(t)}{dt} = t \frac{dTI(t)}{dt}$$

**Saez optimal top rate (eq. 24):**
$$\frac{\tau^*}{1 - \tau^*} = \frac{1 - \bar{g}}{a\varepsilon}$$

**Baily formula (eq. 27):**
$$M_W(b) = \frac{u'(c_l) - u'(c_h)}{u'(c_h)} - \frac{\varepsilon_{1-e,b}}{e}$$

**On the bridge (p. 452):**
"The central concept of the sufficient-statistic approach is to derive formulas for the welfare consequences of policies that are functions of high-level elasticities rather than deep primitives."

**On complements (p. 455--456):**
"The structural and sufficient-statistic methods can be combined to address the shortcomings of each strategy. [...] A structural model can be calibrated to match the sufficient statistics that matter for local welfare analysis to improve its empirical credibility."

# Suggested tags

sufficient-statistics, welfare-analysis, Harberger, envelope-theorem, deadweight-loss, elasticity-of-taxable-income, optimal-taxation, Saez, Feldstein, social-insurance, Baily, moral-hazard, liquidity, behavioral, tax-salience, structural-vs-reduced-form, methodology, public-economics, survey

# My quick takeaway

This paper provides the methodological counterpoint to the full structural approach (RURO, Van Soest) used in my JMP. The key question it raises: does one need the full RURO machinery to evaluate welfare, or do sufficient statistics (elasticities) suffice? The answer depends on the welfare question. For aggregate efficiency (deadweight loss from taxation), sufficient statistics work well. For distributional welfare analysis decomposed into preferences ($R$) and opportunities ($A$), the structural approach is necessary -- because the $R$-$A$ decomposition requires identifying individual preference parameters and individual opportunity sets, which cannot be reduced to aggregate elasticities. The paper's framework does, however, provide a valuable consistency check: the RURO welfare calculations should be broadly consistent with the sufficient-statistic formulas. If the microsimulation says a tax reform has very different welfare effects from what $dW/dt = t \cdot dTI/dt$ implies, something is wrong. The paper's six-step rubric is also useful for structuring the welfare analysis in my JMP.
