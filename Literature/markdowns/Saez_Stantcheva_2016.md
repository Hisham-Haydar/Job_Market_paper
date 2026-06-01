---
title: "Generalized Social Marginal Welfare Weights for Optimal Tax Theory"
authors: [Emmanuel Saez, Stefanie Stantcheva]
year: 2016
outlet: "American Economic Review, 106(1), 24--45"
country_or_context: "Theoretical (US calibration for equality of opportunity illustration)"
population: "General (Mirrlees economy)"
data_period: "N/A (theoretical; US 2008 income distribution and Chetty et al. 2014 mobility data for Table 2)"
shelf: "optimal taxation / social welfare weights / fairness / equality of opportunity / poverty / libertarianism / sufficient statistics"
tags: [optimal-taxation, generalized-welfare-weights, social-marginal-welfare, fairness, equality-of-opportunity, libertarianism, poverty-alleviation, freeloaders, horizontal-equity, tagging, Saez-formula, sufficient-statistics, Roemer, Fleurbaey-Maniquet, survey-experiment]
priority: "high"
read_status: "extracted"
---

# Full citation

Saez, E., & Stantcheva, S. (2016). Generalized Social Marginal Welfare Weights for Optimal Tax Theory. *American Economic Review*, 106(1), 24--45.

# One-sentence contribution

Proposes replacing the standard welfarist social welfare function with "generalized social marginal welfare weights" $g_i = g(c_i, z_i; x_i^s, x_i^b)$ that can depend on characteristics beyond individual utility -- including counterfactual behaviour, family background, and horizontal equity concerns -- showing that optimal tax formulas retain the standard Saez (2001) form but with these richer weights, and demonstrating how equality of opportunity (Roemer), libertarianism, poverty alleviation, and the fair income tax (Fleurbaey-Maniquet) all map into specific weight specifications.

# Why this paper matters

This paper bridges the gap between the sufficient statistics approach to optimal taxation (Saez 2001, 2002; Piketty and Saez 2013a) and the normative theories of fairness (Roemer 1998; Fleurbaey and Maniquet 2011). By showing that any set of justice principles can be translated into generalized welfare weights that plug directly into the standard optimal tax formula, the paper makes fairness-based optimal taxation operationally tractable. It also resolves several discrepancies between standard utilitarian theory and actual tax practice (Table 1): nondegenerate optimal taxes with fixed incomes, the freeloader problem, limited use of tagging, and poverty alleviation objectives.

# Core research question

Can optimal tax theory accommodate fairness principles beyond standard welfarism -- including equality of opportunity, libertarianism, horizontal equity, and poverty alleviation -- while retaining the tractability of the sufficient statistics approach?

# Economic setting and context

Standard Mirrlees income taxation model with quasilinear preferences (no income effects). Individual $i$ has utility $u_i = u(c_i - v(z_i; x_i^u, x_i^b))$ where $c_i = z_i - T(z_i)$, $z_i$ is earnings, $x_i^u$ are characteristics entering utility only, and $x_i^b$ enter both utility and social weights. Productivity $w_i \equiv z_i/l_i$ and cost of effort $\theta_i$ are the two key sources of individual heterogeneity.

# Model / theoretical framework

**Generalized social marginal welfare weight (Definition 1):**

$$g_i = g(c_i, z_i; x_i^s, x_i^b)$$

where $x_i^s$ are characteristics affecting the social weight only (not utility) and $x_i^b$ affect both. Three characteristic sets are distinguished (Figure 1 Venn diagram):
- $x^u$: enter utility only (not fair to compensate for)
- $x^s$: enter social weight only (social criteria, not in utility)
- $x^b$: enter both utility and social weight (fair to compensate for)

**Tax reform desirability (Definition 3):** A budget-neutral reform $\Delta T(z)$ is desirable iff $\int_i g_i \Delta T(z_i) \, di < 0$.

**Local optimal tax (Proposition 1):** $T(z)$ is locally optimal iff for any budget-neutral reform $\Delta T(z)$: $\int_i g_i \Delta T(z_i) \, di = 0$.

**Optimal marginal tax rate (Proposition 2):**

$$T'(z) = \frac{1 - \bar{G}(z)}{1 - \bar{G}(z) + \alpha(z) \cdot e(z)}$$

where $\bar{G}(z)$ is the average generalised weight above $z$, $\alpha(z)$ is the local Pareto parameter, and $e(z)$ is the elasticity. This is identical to the standard Saez (2001) formula but with $\bar{G}(z)$ computed from generalised weights.

**Optimal linear tax (Proposition 3):**

$$\tau = \frac{1 - \bar{g}}{1 - \bar{g} + e}, \quad \bar{g} \equiv \frac{\int_i g_i \cdot z_i \, di}{\int_i g_i \, di \cdot \int_i z_i \, di}$$

**Implicit Pareto weights (Proposition 4):** For any nonnegative $g_i$ and local optimum $T(z)$, there exist Pareto weights $\omega_i = g_i / u_{c_i} \geq 0$ such that $T(z)$ satisfies the FOC of maximising $\int \omega_i u_i \, di$. But these weights are endogenous (evaluated at the optimum) and cannot be specified ex ante.

# Key objects

- **$g_i$:** Generalized social marginal welfare weight -- the value society places on giving \$1 to individual $i$
- **$\bar{G}(z)$:** Average relative weight for earners above $z$ (Definition 4): $\bar{G}(z) = \int_{\{i: z_i \geq z\}} g_i \, di / [\text{Prob}(z_i \geq z) \cdot \int_i g_i \, di]$
- **$\bar{g}(z)$:** Average weight at income level $z$: $\bar{G}(z)[1-H(z)] = \int_z^\infty \bar{g}(z') \, dH(z')$
- **$\tilde{g}(z-c)$:** Component depending on net taxes paid (libertarian component)
- **$\bar{g}_c$, $\bar{g}_{z-c}$:** Derivatives with respect to consumption and taxes paid
- **Simple generalized weights (Definition 5):** $g_i = g(c_i, z_i) = \tilde{g}(c_i, z_i - c_i)$ with two polar cases:
  - Utilitarian: $g_i = \tilde{g}(c_i)$, $\bar{g}_c \leq 0$, $\bar{g}_{z-c} = 0$
  - Libertarian: $g_i = \tilde{g}(z_i - c_i)$, $\bar{g}_c = 0$, $\bar{g}_{z-c} \geq 0$

# Data

No primary data for the theoretical framework. Calibrated illustration in Table 2 uses:
- US 2008 income tax return data (actual income distribution)
- Chetty et al. (2014) intergenerational mobility statistics: fraction of individuals with parents below median at each income percentile
- Elasticity $e = 0.5$ (constant)
- Pareto parameter $a = 1.5$ for top incomes

# Identification logic

Not an empirical paper. The framework takes generalised weights as primitives and derives optimal tax formulas. The paper notes that weights can be estimated from: (1) online surveys of social preferences (Appendix C), (2) the inverse optimum approach (inferring weights from actual tax systems), or (3) calibration from intergenerational mobility data (equality of opportunity case).

# Estimation / empirical strategy

1. **Online survey (Appendix C):** Subjects rank taxpayers by deservedness given income and tax information. Results confirm that social preferences depend on both disposable income and taxes paid, consistent with weights between utilitarian and libertarian.
2. **Equality of opportunity calibration (Table 2):** $\bar{G}(z)$ = fraction of individuals above $z$ from disadvantaged background (parents below median). Optimal marginal tax rates compared to utilitarian case.
3. **Poverty alleviation (Proposition 7):** Weights concentrated on individuals below poverty threshold $\bar{c}$.

# Treatment of preferences

Individual preferences $u_i = u(c_i - v(z_i; x_i^u, x_i^b))$ are quasilinear and heterogeneous. Crucially, the paper separates characteristics entering utility ($x^u$, $x^b$) from characteristics entering social weights ($x^s$, $x^b$). This allows the social planner to:
- Ignore preference differences society considers individuals responsible for (e.g., leisure preferences enter $x^u$ only, not $x^s$)
- Account for characteristics affecting only social judgments (e.g., family background enters $x^s$, not $x^u$ if background doesn't affect tastes)

The paper explicitly acknowledges the connection to Fleurbaey-Maniquet: "the generalized welfare weights have the advantage of highlighting which differences society considers unfair (for example, due to intrinsic skill differences) and which it considers fair (for example, due to different preferences for work)" (p. 44).

# Treatment of opportunities / constraints

Not explicitly modelled. All agents face the same tax schedule $T(z)$ and choose effort optimally. No demand-side constraints, job rationing, or involuntary unemployment.

The paper's "freeloader" analysis (Section IIB) comes closest to the opportunity question: freeloaders are individuals with $\theta_i < 1$ (low cost of work) who choose not to work because transfers are available. The paper distinguishes "deserving poor" ($\theta > 1$, would not work even without transfers) from "freeloaders" ($\theta < 1 - \tau$, work only absent transfers). This maps to the voluntary/involuntary distinction but frames it entirely in terms of preferences ($\theta$) rather than opportunities.

# Welfare / normative object

No social welfare function to maximise. Instead, the paper defines "locally optimal" tax systems as those around which no budget-neutral reform is desirable (Definition 3). Welfare change from reform $\Delta T$: $-\int_i g_i \Delta T(z_i) \, di$. This is a first-order local approach -- it cannot rank globally distinct tax systems, only evaluate local reforms.

The key advantage: the weights $g_i$ directly embed normative judgments without requiring a cardinal utility function or interpersonal comparisons. Different justice theories map to different weight specifications:

- **Utilitarian:** $g_i = u'(c_i)$, decreasing in $c$
- **Libertarian:** $g_i = \tilde{g}(z_i - c_i)$, increasing in net taxes paid
- **Rawlsian:** $g_i = 1$ for the worst off, $g_i = 0$ for all others
- **Equality of opportunity:** $g_i = 1(c_i \leq \bar{c}(r_i))$, concentrated on those below average consumption at their merit rank
- **Poverty alleviation:** $g_i = g > 0$ if $c_i < \bar{c}$, $g_i = 0$ if $c_i \geq \bar{c}$
- **Fair income tax (Fleurbaey-Maniquet):** discussed in online Appendix B5

# Main findings

1. **Optimal tax formulas are identical in form to the standard approach (Proposition 2).** The only change is replacing standard welfare weights with generalised weights $\bar{G}(z)$. This makes the framework immediately operational: any specification of $g_i$ can be plugged into the Saez (2001) formula.

2. **Table 1 -- Resolving discrepancies between theory and practice:**
   - **Fixed incomes:** Standard welfarism → degenerate (full redistribution). Generalised weights depending on taxes paid → nondegenerate.
   - **Freeloaders:** Standard approach cannot distinguish deserving from undeserving nonworkers. Generalised weights can depend on counterfactual behaviour ($g_i = 0$ for freeloaders).
   - **Tagging:** Standard approach recommends maximal tagging. Horizontal equity concerns through generalised weights limit tagging to cases benefiting the discriminated group.
   - **Poverty:** Direct poverty minimisation violates Pareto. Weights concentrated on the poor maintain Pareto efficiency.

3. **Optimal tax with fixed incomes (Proposition 5):** $T'(z) = 1/(1 - \bar{g}_{z-c}/\bar{g}_c)$. Utilitarian: $T'(z) = 1$ (full confiscation). Libertarian: $T'(z) = 0$ (no taxation). Intermediate: $0 \leq T'(z) \leq 1$.

4. **Freeloaders (Section IIB):** With generalised weights setting $g_i = 0$ for freeloaders ($\theta_i < 1 - \tau$, would work absent transfers), the average weight on nonworkers $\bar{g}_0$ falls below the utilitarian benchmark. This lowers the optimal tax rate $\tau^*$ and the optimal transfer $-T_0$. Application 1: when $\bar{g}_0 < 1$, in-work benefits ($T'(0) < 0$) become optimal. Application 2: during recessions, the freeloader fraction falls (more nonworkers are genuinely constrained), justifying expanded benefits.

5. **Horizontal equity and tagging (Section IIC, Proposition 6):** Tagging (differentiated taxes by observable characteristics) is optimal only if it benefits the group discriminated against. When the discriminated group is at the revenue-maximising rate, horizontal inequities are acceptable only with a Rawlsian justification. This dramatically limits the scope for tagging relative to the utilitarian recommendation.

6. **Equality of opportunity (Section IIIA):** Weights concentrated on individuals from disadvantaged backgrounds: $g_i = 1(c_i \leq \bar{c}(r_i))$. $\bar{G}(z)$ = fraction from disadvantaged background above $z$. This converges to ~1/3 at the top (unlike the utilitarian case where $\bar{G}(z) \to 0$), producing a lower asymptotic top tax rate: 47% (equality of opportunity) vs 57% (utilitarian) with $a = 1.5$, $e = 0.5$ (Table 2).

7. **Poverty alleviation (Section IIIB, Proposition 7):** Weights $g_i = g$ if $c_i < \bar{c}$, $g_i = 0$ otherwise. Revenue-maximising rates above $\bar{z}$ (the pretax poverty threshold). Below $\bar{z}$: high rates falling continuously to meet the revenue-maximising rate at $\bar{z}$ (Figure 2, Panel B). This avoids the Pareto violation of direct poverty gap minimisation.

# Main limitations

- Local theory only: cannot compare globally distinct tax systems or rank multiple local optima
- Quasilinear preferences (no income effects) -- simplifies but limits generality
- The choice of weights is normative and not pinned down by the theory
- No demand-side constraints: all nonworkers are either "deserving poor" (high $\theta$) or "freeloaders" (low $\theta$), with no involuntary unemployment
- Static model
- Online survey evidence (Appendix C) is suggestive but not definitive about social preferences
- The connection to Fleurbaey-Maniquet fair income tax is relegated to the online appendix

# Relevance for my JMP

## possible use for the bridge between sufficient statistics and fairness
The paper's central contribution for my JMP is showing that any fairness principle can be operationalised through generalised weights $g_i$ in the Saez formula. This means the RURO-based welfare metric (equivalent income with opportunity decomposition) can in principle be translated into welfare weights and plugged into the optimal tax formula. The question is: what weights does the RURO decomposition imply?

## possible use for the freeloader/deserving poor distinction
The freeloader analysis (Section IIB) directly motivates the RURO framework. The paper distinguishes agents by $\theta_i$ (cost of work) and sets $g_i = 0$ for those who would work absent transfers. But it cannot distinguish agents who don't work because of high $\theta$ (preference-driven, "lazy") from those who don't work because no suitable job exists (demand-constrained, "unlucky"). The RURO opportunity density $g(h,w)$ provides this decomposition: high-$\theta$ non-participants with good opportunities are freeloaders; high-$\theta$ non-participants with poor opportunities are deserving poor.

## possible use for the business cycle application
Application 2 (recessions shift the composition of nonworkers toward the deserving poor) is directly relevant to the RURO framework's time-varying opportunity density. During recessions, $\theta$ (total opportunity mass) falls, increasing the fraction of involuntary non-participants and justifying higher transfers.

# Research questions this paper inspires

1. What generalized welfare weights does the RURO equivalent-income metric imply? If welfare is $W_i = m_i(\tilde{w}, z_i)$ and the social ordering is maximin, the implied weight is $g_i = 1$ for the worst-off agent and $g_i = 0$ for all others. But with the RURO decomposition, the worst-off identification depends on opportunity restrictions: agents with high skills but poor opportunities may be worse off than agents with low skills but abundant opportunities.

2. Can the RURO opportunity density be mapped into the $x^s$ characteristics (entering social weights but not utility)? If demand-side constraints ($\theta$, $g(h,w)$) are viewed as circumstances (not the agent's responsibility), they should enter $x^s$, making constrained agents more deserving of transfers.

3. The paper notes that Fleurbaey-Maniquet fair income tax theory is covered in online Appendix B5. What specific weights does this theory imply, and how do they compare to the equality-of-opportunity weights in Table 2?

# Challenge to this paper

The paper's framework treats the freeloader problem as a normative judgment embedded in the weights ($g_i = 0$ for freeloaders). But identifying freeloaders requires counterfactual information: would individual $i$ work absent transfers? This counterfactual is not observed and depends on both preferences ($\theta_i$) and opportunities (job availability). The paper assumes that $\theta_i$ is the only relevant parameter, ignoring the possibility that some nonworkers with $\theta_i < 1 - \tau$ (who would work if they could) face demand constraints that prevent employment. The RURO framework provides a structural model for this counterfactual decomposition, separating the preference-driven component of nonparticipation from the opportunity-driven component and producing empirically grounded weights rather than normatively assumed ones.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper provides a framework for translating normative principles into operational welfare weights $g_i$ that enter optimal tax formulas. $R$ (preferences) is captured by utility $u_i$; $z$ (realised bundle) is earnings-consumption $(z_i, c_i)$; $y$ (tax schedule) is $T(z)$. The weights $g_i$ embed the normative evaluation $W$ but without requiring a global SWF.

[Reasonable inference for my project] The generalised weights $g_i = g(c_i, z_i; x_i^s, x_i^b)$ can incorporate opportunity restrictions as $x_i^s$ characteristics. An agent facing poor opportunities (low $\theta$, unfavourable $g(h,w)$) would receive higher $g_i$ under a compensation principle that treats demand constraints as circumstances. This would change the optimal tax formula through $\bar{G}(z)$.

[Unclear from paper] Whether the local nature of the approach (only evaluating small reforms) is compatible with the global welfare ranking provided by the RURO equivalent-income metric. The Fleurbaey-Maniquet approach uses a global SWF (maximin over equivalent incomes) while Saez-Stantcheva use local weights. The two are compatible at the optimum (Proposition 4) but may diverge for reform evaluation away from the optimum.

# Relation to Bargain et al. (2013)

The paper provides the theoretical framework for connecting Bargain et al.'s welfare analysis (equivalent income) to optimal tax formulas. Bargain et al. compute welfare metrics for reform evaluation; Saez-Stantcheva show how these metrics can be translated into welfare weights that enter optimal tax formulas. The online Appendix B5 explicitly discusses the Fleurbaey-Maniquet fair income tax, which is the theoretical foundation for Bargain et al.'s welfare metric.

# Relation to opportunities vs preferences

The paper distinguishes characteristics entering utility ($x^u$) from those entering social weights ($x^s$), and characteristics for which compensation is fair ($x^b$) from those for which it is not. This directly maps to the preferences-vs-opportunities distinction: preferences are $x^u$ (not fair to compensate for), opportunities/constraints are $x^s$ or $x^b$ (fair to compensate for). The freeloader analysis applies this: the cost of effort $\theta_i$ is treated as a responsible characteristic (those with low $\theta$ who don't work are freeloaders). The RURO framework adds the opportunity density as an additional dimension of $x^b$ (circumstances to compensate for).

# Useful quotations / formulas

**On the generalised approach (p. 24):**
"Weights directly capture society's concerns for fairness without being necessarily tied to individual utilities."

**Optimal marginal tax rate (Proposition 2, p. 30):**
$$T'(z) = \frac{1 - \bar{G}(z)}{1 - \bar{G}(z) + \alpha(z) \cdot e(z)}$$

**On freeloaders (p. 34--35):**
"The presence of such 'freeloaders,' perceived to take undue advantage of a generous transfer system, is precisely why many oppose welfare."

**On business cycles (Application 2, p. 36):**
"Individuals are less likely to be responsible for their unemployment status in a recession than in an expansion, so that the composition of those out of work changes over the business cycle."

**On equality of opportunity (p. 44):**
"Equality of opportunity has wide normative appeal both among liberals and conservatives."

**On the link to Fleurbaey-Maniquet (footnote 37, p. 44):**
"See the treatment of the fair income tax theory in online Appendix B5."

# Suggested tags

optimal-taxation, generalized-welfare-weights, social-marginal-welfare, fairness, equality-of-opportunity, libertarianism, Rawlsian, poverty-alleviation, freeloaders, deserving-poor, horizontal-equity, tagging, Saez-formula, sufficient-statistics, Roemer, Fleurbaey-Maniquet, local-optimum, tax-reform, survey-experiment, business-cycle

# My quick takeaway

The paper that operationalises fairness for optimal tax theory. By replacing the standard SWF with generalised welfare weights $g_i$, any justice principle -- equality of opportunity, libertarianism, poverty alleviation, Fleurbaey-Maniquet fairness -- can be plugged into the Saez optimal tax formula. For my JMP, the key contributions are: (1) the freeloader/deserving-poor distinction maps to the RURO preference/opportunity decomposition, (2) the $x^s$/$x^b$/$x^u$ classification provides a formal framework for deciding which characteristics (including opportunity restrictions) should enter the welfare weights, and (3) the business cycle application shows that time-varying opportunity density directly affects optimal policy through changing the composition of nonworkers.
