---
title: "Help the Low Skilled or Let the Hardworking Thrive? A Study of Fairness in Optimal Income Taxation"
authors: [Marc Fleurbaey, Francois Maniquet]
year: 2007
outlet: "Journal of Public Economic Theory, 9(3), 467--500"
country_or_context: "Theoretical"
population: "General (Mirrlees economy with heterogeneous preferences and skills)"
data_period: "N/A (theoretical)"
shelf: "optimal taxation / fairness / egalitarian-equivalent / equivalent-budget / compensation / laissez-faire / zero marginal rate"
tags: [optimal-taxation, fairness, egalitarian-equivalent, equivalent-budget, compensation, laissez-faire, implicit-transfer, implicit-budget, money-metric-utility, maximin, zero-marginal-rate, hardworking-poor, Mirrlees, second-best, incentive-compatibility]
priority: "high"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Maniquet, F. (2007). Help the Low Skilled or Let the Hardworking Thrive? A Study of Fairness in Optimal Income Taxation. *Journal of Public Economic Theory*, 9(3), 467--500.

# One-sentence contribution

Derives optimal income tax properties from two conflicting fairness principles -- compensation for unequal skills (Help Low Skilled) and respect for individual effort (Let Hardworking Thrive) -- showing that despite their first-best incompatibility, both yield second-best taxes with a zero marginal rate on incomes below the minimum wage and maximal subsidy to the lowest earners, under a No Identification assumption on the joint distribution of skills and preferences.

# Why this paper matters

This is the key paper connecting the two fairness axioms (compensation and laissez-faire) to specific features of the optimal tax schedule. It shows that the ethical dilemma "should we help the low skilled or let the hardworking thrive?" is partially resolved in the second-best context: both principles converge toward tax exemption for low incomes and maximal transfers to lowest earners. The paper introduces the implicit transfer $IT(z, \tilde{w}, R)$ and implicit budget $IB(z, w, R)$ as the welfare measures underlying the egalitarian-equivalent (EE) and equivalent-budget (EB) social preferences, providing the operational building blocks for the welfare analysis in Bargain et al. (2013) and the 2018 JEL survey.

# Core research question

What features of the optimal income tax follow from fairness principles that incorporate either the goal of helping the low skilled (compensation for unequal wages) or rewarding the hardworking (respect for individual effort), when agents have heterogeneous preferences and skills and incentive constraints bind?

# Economic setting and context

Standard Mirrlees income tax model. Agents choose bundle $z_i = (\ell_i, c_i) \in X = [0,1] \times \mathbb{R}_+$ where $\ell_i$ is labour and $c_i$ is consumption. Agent $i$ has skill $w_i$ (wage rate) and ordinal preferences $R_i$ over $X$. In second-best, only earnings $y_i = w_i \ell_i$ are observed, so redistribution is via a tax function $\tau(y)$ with disposable income $y - \tau(y)$ nondecreasing.

# Model / theoretical framework

**Two fairness principles:**

**Help Low Skilled (HLS -- compensation):** *It is a social improvement to change an allocation by modifying the bundles of two agents $i$ and $j$ who have identical preferences $R$, from $z_i, z_j$ to $z_i', z_j'$, so that $z_i' P z_j' P z_j P z_i$ (reducing the indifference curve gap).*

**Let Hardworking Thrive (LHT -- laissez-faire/natural reward):** *It is a social improvement to change an allocation obtainable via lump-sum transfers by modifying the lump-sum transfers of two agents $i$ and $j$ who have the same skill, from $t_i, t_j$ to $t_i', t_j'$, so that $t_i > t_j > t_j' > t_i'$ (equalising transfers).*

These two principles are **mutually incompatible** (Figure 4): an agent with low indifference curves may have a high implicit budget, so HLS and LHT can give contradictory instructions.

**Key welfare objects:**

**Implicit transfer** $IT(z, w, R_i)$: the minimal transfer $t$ such that there exists $x \in B^f(t, w)$ with $x R_i z$. This is the money-metric utility at reference wage $w$. In the $(y, c)$ space, $IT(z_i, \tilde{w}, R_i)$ is constructed by finding the budget line of slope $\tilde{w}/w_i$ tangent to the agent's indifference curve.

**Implicit budget** $IB(z, w, R_i)$: the budget $B^f(t, w)$ where $t = IT(z, w, R_i)$. It is the budget with slope $w$ that is tangent to the agent's indifference curve at $z$.

**Two social preferences:**

**Definition 1 -- Egalitarian-Equivalent (EE):** Apply the maximin criterion to the vector $(IT(z_1, \tilde{w}, R_1), \ldots, IT(z_n, \tilde{w}, R_n))$ for some chosen reference skill $\tilde{w}$.
- Satisfies HLS fully
- Satisfies LHT only for agents with $w_i = \tilde{w}$
- Low $\tilde{w}$ favours work-averse agents; high $\tilde{w}$ favours hardworking agents (Figure 8)

**Definition 2 -- Equivalent-Budget (EB):** Apply the maximin criterion to $(\tilde{U}^{\max}(IB(z_1, w_1, R_1)), \ldots, \tilde{U}^{\max}(IB(z_n, w_n, R_n)))$ where $\tilde{U}$ represents some chosen reference preferences $\tilde{R}$.
- Satisfies LHT fully
- Satisfies HLS only for agents with $R_i = \tilde{R}$
- Choice of $\tilde{R}$ determines degree of redistribution: if $\tilde{R}$ has low willingness to work, less redistribution (Figure 11)

**No Identification Assumption:** For every agent $i$ and every $w < w_i$, there exists agent $j$ with $w_j = w$ and $R_j^*|_{[0,w] \times \mathbb{R}_+} = R_i^*|_{[0,w] \times \mathbb{R}_+}$. This means that within any income interval, agents with different skills but identical restricted preferences exist and cannot be distinguished by the tax authority.

# Key objects

- **$IT(z_i, \tilde{w}, R_i)$:** Implicit transfer / money-metric utility at reference wage $\tilde{w}$ -- the EE welfare index
- **$IB(z_i, w_i, R_i)$:** Implicit budget -- the budget tangent to the agent's indifference curve at slope $w_i$ -- the EB welfare index (evaluated by $\tilde{U}^{\max}$)
- **$B^f(t, w) = \{(\ell, c) \in X \mid c \leq t + w\ell\}$:** First-best budget set with transfer $t$ and wage $w$
- **$B^s(\tau, w_i) = \{(\ell, c) \in X \mid c \leq w_i\ell - \tau(w_i\ell)\}$:** Second-best budget set
- **$R^c$:** Preferences of agents who only care about consumption ($c_i' \geq c_i \Leftrightarrow$ weakly preferred) -- highest willingness to work
- **$W = \{w \in \mathbb{R}_+ \mid \exists i, w_i = w\}$:** Set of wage rates in the population
- **$w_m, w_M$:** Minimum and maximum skills

# Data

No data. Purely theoretical.

# Identification logic

Not applicable. The paper derives analytical results from axioms, not from data. The No Identification assumption is a condition on the joint distribution of skills and preferences in the population, not an econometric identification strategy.

# Estimation / empirical strategy

Not applicable.

# Treatment of preferences

Preferences $R_i$ are ordinal, heterogeneous across agents, continuous, convex, and monotonic (more consumption is better, less labour is better for given consumption). The single-crossing property holds: any two indifference curves (from different agents) cross at most once in $(\ell, c)$ space (Figure 1).

The paper defines a willingness-to-work ordering: $R_i$ exhibits lower willingness to work than $R_i'$ if, whenever indifference curves cross, $R_i$ always prefers the lower-labour bundle.

The key normative distinction: preferences are the agent's responsibility (LHT says redistribution should not depend on preferences), while skills are not (HLS says agents with identical preferences but different skills should be compensated). This responsibility distinction is the ethical core of the paper.

# Treatment of opportunities / constraints

Opportunities are determined entirely by skill $w_i$ and the tax schedule $\tau$. No demand-side constraints, job rationing, or involuntary unemployment in the model.

However, the paper includes a remarkable passage about unemployment (p. 494): "one may also suggest that agents who are constrained in their labor time by an insufficient labor demand, such as the unemployed, may be treated as if their wage rate was zero above their current labor time. Unemployed agents are then equivalent to agents with a zero wage. As a consequence of our analysis, one might suggest that in times of high unemployment, it is reasonable to maximize the minimum income, whereas when unemployment is low it is advisable to seek low marginal rates of taxation for low incomes."

This is an important bridge to the RURO framework: the paper acknowledges demand-side constraints but handles them by recoding constrained agents as zero-wage, rather than modelling the opportunity set explicitly.

# Welfare / normative object

Maximin over either:
- $IT(z_i, \tilde{w}, R_i)$ for EE social preferences, or
- $\tilde{U}^{\max}(IB(z_i, w_i, R_i))$ for EB social preferences

Both are ordinal, use only individual noncomparable preferences (no cardinal utility, no interpersonal utility comparisons), and satisfy the weak Pareto principle. The EE preferences actually satisfy the strong Pareto principle via the leximin extension (Fleurbaey & Maniquet 2005).

# Main findings

1. **Incompatibility of HLS and LHT (Figure 4, p. 474):** The two fairness principles are mutually exclusive. An allocation satisfying HLS may violate LHT and vice versa. This reflects the fundamental ethical dilemma: help the low skilled or reward the hardworking.

2. **Two-by-two case (Section 4):**
   - **Proposition 1:** The incentive compatibility constraint from high-skill to low-skill agents is binding for all social preferences except $R_1$-EB (when reference preferences favour hard work).
   - **Proposition 2:** An IC allocation is optimal for $w_1$-EE if and only if it is optimal for $R_2$-EB. The two seemingly opposed social preferences converge in the second-best.
   - Taxation is never progressive among low-skilled agents: transfers to hardworking low-skilled agents are at least as large as transfers to less hardworking ones.

3. **Theorem 1 ($w_m = 0$):** If every preference class contains agents with zero skill, then the optimal tax for all EE preferences and for EB with $\tilde{R} = R^c$ maximizes the minimum income $-\tau(0)$ (the basic income). This is the basic income proposal.

4. **Theorem 2 (EE, $\tilde{w} \geq w_m > 0$, the central result):** Under the No Identification assumption, the optimal EE tax minimizes $\tau(w_m)$ subject to:

$$\tau(w_m) \leq \tau(y) \leq \tau(w_m) + y - w_m + (w_m - y)^+\left(\frac{\tilde{w}}{w_m}\right) \quad \forall y \geq 0.$$

   Key features:
   - Agents earning $w_m$ receive the greatest subsidy in absolute amount
   - The average marginal tax rate over $[0, w_m]$ is nonpositive
   - When $\tilde{w} = w_m$: the marginal rate is **exactly zero** over $[0, w_m]$ -- a lump-sum transfer to all low earners
   - The income function $y - \tau(y)$ is bounded between two lines in Figure 15

5. **Theorem 3 (EB):** Under the No Identification assumption, the optimal EB tax minimizes $\tau(w_m)$ subject to:

$$\tau(w_m) \leq \tau(y) \leq \min_{w \in W}\left[(y - w)^+ - \tilde{E}(w, \tilde{U}_0)\right] \quad \forall y \geq 0.$$

   Key features:
   - Zero marginal tax rate over $[0, w_m]$
   - The upper bound has **nondecreasing marginal rates** -- a progressive tax structure
   - The optimal tax approaches the progressive upper bound as the tax becomes efficient

6. **Convergence in the second-best (p. 493--494):** Despite first-best incompatibility, EE and EB social preferences lead to similar optimal tax features: maximal subsidy to lowest earners, zero marginal rate on low incomes. "It is as if the second-best context reduced the intensity of this value conflict, as compared to the first-best context."

# Main limitations

- Standard Mirrlees framework: no demand-side constraints, involuntary unemployment, or hours rationing (though the paper discusses unemployment briefly)
- No Identification assumption is strong: requires sufficiently diverse preferences at every skill level
- No empirical implementation: entirely theoretical results about qualitative tax features
- Cannot pin down the exact optimal tax schedule, only bounds and qualitative features
- Static model: no dynamics, savings, or human capital
- The choice of $\tilde{w}$ (for EE) or $\tilde{R}$ (for EB) remains normatively open

# Relevance for my JMP

## possible use for the theoretical foundation of EE welfare metric
This paper provides the clearest exposition of why $IT(z_i, \tilde{w}, R_i)$ -- the implicit transfer / money-metric utility -- is the right welfare index for egalitarian-equivalent social preferences. The index is constructed from ordinal preferences alone, requires no cardinal utility, and embodies the compensation principle. For my JMP, this justifies using equivalent income as the welfare metric in the RURO framework.

## possible use for the treatment of unemployment
The paper's suggestion (p. 494) that unemployed agents "may be treated as if their wage rate was zero above their current labor time" is a critical bridge to my RURO framework. This recoding is a crude approximation: it treats all involuntary non-participants as zero-skill agents, losing information about their actual productivity and the nature of their constraints. The RURO framework's explicit modelling of the opportunity density $g(h, w)$ provides a more nuanced treatment: an agent with high $w_i$ but restricted opportunities (low $\theta$ or unfavourable $g(h)$) is different from a genuinely zero-skill agent.

## possible use for the zero marginal rate result
The zero marginal rate on incomes below $w_m$ is a central policy implication. In the RURO framework, where some agents face involuntary unemployment (and thus effectively have $w_m = 0$), Theorem 1 applies and the optimal tax maximizes the basic income. This provides a fairness-based justification for generous minimum income support when labour demand constraints bind.

# Research questions this paper inspires

1. How does the No Identification assumption interact with demand-side constraints? If agents with skill $w$ face different opportunity sets $A_i$ (e.g., some live in areas with few jobs), the assumption that agents with $w_j = w$ and identical restricted preferences exist may fail. Would the optimal tax features (zero marginal rate on low incomes) survive?

2. The paper treats $w_m$ as exogenous (the minimum skill in the population). In the RURO framework, the effective minimum wage depends on the opportunity density: an agent with positive $w_i$ but no available jobs has an effective wage of zero. Should $w_m$ in the optimal tax formula be redefined as the minimum *effective* wage (accounting for job availability)?

3. The convergence of EE and EB in the second-best is driven by the No Identification assumption. If the planner had additional information about agents' opportunity sets (as in the RURO framework), would the two principles diverge again?

# Challenge to this paper

The paper's treatment of involuntary unemployment as equivalent to zero skill (p. 494) is analytically convenient but empirically problematic. An unemployed worker with high productivity who faces demand-side rationing is fundamentally different from a genuinely low-skilled worker: the former would work productively if given the opportunity, while the latter cannot. The RURO framework, by modelling the opportunity density $g(h, w)$ and the total opportunity mass $\theta$, can distinguish these cases. This distinction matters for the optimal tax: the zero marginal rate result below $w_m$ is designed to help agents whose low earnings reflect low skills, but it may not be the right policy for agents whose low earnings reflect restricted opportunities at higher skill levels.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The implicit transfer $IT(z_i, \tilde{w}, R_i)$ is the formal expression for the welfare metric $W$ in my framework when the opportunity set $A$ equals the budget set. $R$ = individual ordinal preferences; $z$ = realised bundle $(\ell_i, c_i)$; the tax schedule $y$ enters through $\tau(\cdot)$. The paper derives properties of the optimal $y$ (tax schedule) by maximising $\min_i W(z_i, R_i; y)$.

[Reasonable inference for my project] The paper's two fairness principles map to my framework's $R$-$A$ decomposition: HLS (compensation) says differences in $A$ (proxied by $w_i$) should be compensated; LHT (laissez-faire) says differences in $R$ (preferences) should not trigger redistribution. The RURO extension enriches $A$ beyond $w_i$ to include the opportunity density $g(h, w)$ and total mass $\theta$, so the compensation principle should apply to opportunity restrictions as well as skill differences.

[Unclear from paper] Whether the zero marginal rate result survives when $A$ includes demand-side constraints. If some agents with $w_i > w_m$ face restricted opportunity sets (cannot access jobs at their skill level), the envelope curve of indifference curves over $[0, w_m]$ may no longer coincide with the envelope for the $w_m$-skill subpopulation, potentially invalidating the No Identification-based reasoning.

# Relation to Bargain et al. (2013)

The implicit transfer $IT(z_i, \tilde{w}, R_i)$ defined here is the theoretical object that Bargain et al. (2013) compute empirically as the equivalent income. Bargain et al.'s contribution is to estimate preferences $R_i$ from observed labour supply choices (using structural discrete-choice models) and then compute $IT$ for policy evaluation. This paper provides the theoretical justification for why $IT$ is the right welfare metric (it satisfies HLS under EE social preferences) and what the optimal tax should look like (zero marginal rate on low incomes).

# Relation to opportunities vs preferences

The paper's fundamental ethical distinction -- preferences are the agent's responsibility, skills are not -- maps exactly to the RURO framework's separation of preferences ($R$) from opportunities ($A$). The paper models $A$ as determined solely by $w_i$ (the budget set at wage $w_i$), while the RURO framework enriches $A$ with the opportunity density $g(h, w)$ and total mass $\theta$. The key question the paper raises but does not answer: when opportunity restrictions ($A$) are not fully captured by $w_i$, should they be treated as circumstances (to be compensated, like skills) or as part of the agent's situation (like preferences)? The natural answer from the fairness literature is that demand-side constraints are circumstances (not the agent's responsibility), so they should be compensated -- extending HLS to cover opportunity restrictions.

# Useful quotations / formulas

**On the ethical dilemma (p. 467--468):**
"Is it fair to try to reduce income inequalities indiscriminately, when some are due to unequal earning abilities while others are simply due to different consumption-leisure preferences?"

**On the convergence result (p. 494):**
"It is as if the second-best context reduced the intensity of this value conflict, as compared to the first-best context."

**On unemployment (p. 494):**
"One may also suggest that agents who are constrained in their labor time by an insufficient labor demand, such as the unemployed, may be treated as if their wage rate was zero above their current labor time. Unemployed agents are then equivalent to agents with a zero wage."

**On the zero marginal rate (Theorem 2 interpretation, p. 489--490):**
"The average marginal tax rate over incomes belonging to the interval $[0, w_m]$ is nonpositive. And in the particular case when $\tilde{w} = w_m$... the marginal tax rate is exactly zero over $[0, w_m]$."

**On the implicit transfer as money-metric utility (p. 476):**
"This measure of individual well-being does not require any information about individuals' subjective utility, and depends only on ordinal noncomparable preferences about consumption and labor."

**On the role of reference parameters (p. 478):**
"EE preferences are neutral about preferences for agents with $w_i = \tilde{w}$, are biased toward the 'hardworking' for agents with $w_i < \tilde{w}$, and conversely for $w_i > \tilde{w}$."

# Suggested tags

optimal-taxation, fairness, egalitarian-equivalent, equivalent-budget, compensation, laissez-faire, natural-reward, implicit-transfer, implicit-budget, money-metric-utility, maximin, leximin, zero-marginal-rate, hardworking-poor, basic-income, Mirrlees, second-best, incentive-compatibility, No-Identification, Fleurbaey, Maniquet

# My quick takeaway

The companion to Fleurbaey & Maniquet (2006), providing the second-best optimal tax analysis. The central results -- zero marginal rate on low incomes and maximal subsidy to lowest earners -- follow from both EE and EB social preferences despite their first-best incompatibility. For my JMP, the paper provides: (1) the formal definition of the implicit transfer $IT(z_i, \tilde{w}, R_i)$ that Bargain et al. (2013) compute as equivalent income, (2) the remarkable passage suggesting that unemployed agents be treated as zero-wage workers (a crude approximation that the RURO framework can improve upon), and (3) the insight that the compensation principle should extend from skill differences to opportunity restrictions -- the core motivation for incorporating $g(h, w)$ into the welfare analysis.
