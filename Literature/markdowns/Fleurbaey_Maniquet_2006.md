---
title: "Fair Income Tax"
authors: [Marc Fleurbaey, François Maniquet]
year: 2006
outlet: "Review of Economic Studies, 73(1), 55--83"
country_or_context: "General (theoretical, with US TANF illustration)"
population: "Heterogeneous agents differing in skills and preferences over consumption-leisure"
data_period: "N/A (theoretical)"
shelf: "fair taxation / equivalent wage / social preferences / optimal taxation / fairness axioms"
tags: [fair-taxation, equivalent-wage, equivalent-income, Transfer-Principle, Laisser-Faire, Hansson-Independence, Separability, maximin, optimal-tax, fairness, social-preferences, hardworking-poor, low-skilled, Pigou-Dalton, incentive-compatibility, Fleurbaey, Maniquet]
priority: "critical"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Maniquet, F. (2006). Fair Income Tax. *Review of Economic Studies*, 73(1), 55--83.

# One-sentence contribution

Derives the optimal income tax from fairness axioms (a restricted Pigou-Dalton Transfer Principle and a Laisser-Faire principle for equal-skill economies) rather than from a utilitarian social welfare function, showing that these axioms uniquely select the "equivalent wage" $W_i(z_i)$ as the measure of individual well-being and the maximin over $W_i$ as the social objective, and that the optimal tax maximises the net income of the hardworking poor (lowest-skilled, full-time workers).

# Why this paper matters

This is the foundational paper connecting the Fleurbaey-Maniquet fair allocation theory to the Mirrlees optimal taxation problem. It shows that the choice of social welfare function need not be arbitrary: specific fairness axioms uniquely determine both (i) the interpersonal welfare measure (equivalent wage $W_i$) and (ii) the aggregation rule (maximin/leximin). This resolves the "weighting problem" in optimal taxation -- how to aggregate utilities of agents with heterogeneous preferences -- without imposing a utilitarian framework. The paper's criterion for comparing tax schedules (minimise the maximum average tax rate over low incomes) is remarkably simple and policy-relevant.

# Core research question

How should an income tax be designed when agents differ in both earning abilities (skills) and consumption-leisure preferences, if the objective is derived from fairness principles rather than utilitarian social welfare?

# Economic setting and context

Standard Mirrlees optimal taxation framework: agents choose labour supply $\ell_i \in [0,1]$ to maximise preferences $R_i$ over bundles $z_i = (\ell_i, c_i)$ subject to the budget set $B(\tau, w_i) = \{(\ell, c) \mid c \leq w_i \ell - \tau(w_i \ell)\}$. Heterogeneity is two-dimensional: skills $w_i$ (productivity) and preferences $R_i$ (ordinal, over consumption-labour bundles). The government observes only earnings $y_i = w_i \ell_i$, not skills or preferences separately, so redistribution must be via a tax function $\tau(y)$ satisfying incentive compatibility.

# Model / theoretical framework

**Two goods:** labour $\ell_i \in [0,1]$ and consumption $c_i \geq 0$. Agent $i$'s bundle: $z_i = (\ell_i, c_i)$. Earnings: $y_i = w_i \ell_i$. Constant returns to scale (marginal product = $w_i$).

**Four fairness axioms on social preferences $R$ (complete ordering over allocations):**

1. **Transfer Principle** (restricted Pigou-Dalton): Among agents with *identical preferences* and *identical labour*, Pigou-Dalton transfers in consumption are socially desirable. (Restricts the standard PD principle to avoid conflicts with preference heterogeneity.)

2. **Laisser-Faire**: When all agents have the *same skill* $w$, the laisser-faire allocation (each agent optimises freely on $c \leq w\ell$) is socially optimal. (Respects free choice when the opportunity set is equal.)

3. **Weak Pareto**: If all agents strictly prefer $z_i$ to $z_i'$, then $z$ is socially better.

4. **Hansson Independence**: Social preferences depend only on individual indifference curves at the allocations being compared (not on the full preference ordering).

5. **Separability**: Unconcerned agents (same bundle in both allocations) don't affect the social ranking.

**Theorem 1 (the main result):** Social preferences satisfying all five axioms rank allocations by:

$$\min_i W_i(z_i) \quad \text{(maximin over equivalent wages)}$$

where the **equivalent wage** is:

$$W_i(z_i) = \max\{w \in \mathbb{R}_+ \mid \forall \ell, \ z_i \ R_i \ (\ell, w\ell)\}$$

This is the wage rate that, if offered without any tax, would make agent $i$ just indifferent with her current bundle $z_i$. Graphically (Figure 4): find the budget line through the origin with slope $W_i$ that is tangent to the indifference curve through $z_i$.

**Key properties of $W_i$:**
- It is a money-metric utility representation, but derived from axioms rather than imposed
- It uses individual preferences $R_i$ (not a common utility function)
- It does not require cardinal utility or interpersonal utility comparisons
- It represents the "implicit wage" needed to reach the same satisfaction without redistribution

# Key objects

- **Equivalent wage $W_i(z_i)$:** The hypothetical wage that would give agent $i$ the same utility as $z_i$ if she could choose freely on the budget $c \leq W_i \ell$. This is the paper's welfare metric.
- **Maximal average tax rate over low incomes:** $\max_{0 \leq y \leq w_m} \tau(y)/y$. Theorem 2 shows that the tax schedule with the *lower* maximal average tax rate is socially preferred.
- **Hardworking poor:** Agents with the lowest skill $w_m = \min_i w_i$ who choose the largest labour time. These agents have the lowest $W_i$ and therefore receive absolute social priority.
- **Low-Skill Diversity:** Technical assumption ensuring that for every earnings level below $w_m$, there exist low-skilled agents with diverse preferences willing to earn that amount.
- **Minimal tax:** A tax function such that the after-tax income schedule $y - \tau(y)$ coincides with the envelope curve of the population's indifference curves (no "slack" in the budget).

# Data

No empirical data. One illustrative application: Figure 13 compares the 1986 and 2000 US budget sets for lone parents with two children (income tax, social security, food stamps, TANF/AFDC), showing that the 2000 reform reduced the maximum average tax rate over low incomes, and is therefore socially preferred by the paper's criterion.

# Identification logic

Not applicable (pure theory). The axioms identify the social welfare function uniquely. The key insight: Transfer Principle + Hansson Independence yield infinite inequality aversion (maximin), and Laisser-Faire + Separability select the equivalent wage $W_i$ as the individual welfare measure.

# Estimation / empirical strategy

Not applicable (theoretical paper). The paper derives axiomatic results and characterises features of the optimal tax.

# Treatment of preferences

Preferences $R_i$ are ordinal over $(\ell, c)$ bundles. They are continuous, convex, and monotonic (more consumption preferred, less labour preferred). The paper is explicitly preference-respecting: the Laisser-Faire axiom says that when opportunities are equal, differences in outcomes due to different preferences are acceptable. Preferences are treated as a *legitimate* source of inequality -- unlike skills, which are a *illegitimate* source. This is the compensation-responsibility divide: skills should be compensated, preferences should be respected.

The paper does not require cardinal utility functions or interpersonal utility comparisons. The equivalent wage $W_i$ uses agent $i$'s *own* preferences to measure well-being, avoiding the arbitrary choice of a common utility function that plagues utilitarian optimal taxation.

# Treatment of opportunities / constraints

The opportunity set is the budget set $B(\tau, w_i) = \{(\ell, c) \mid c \leq w_i \ell - \tau(w_i \ell)\}$. Differences in opportunities arise from differences in skills $w_i$. The Laisser-Faire axiom says that when opportunities are equal ($w_i = w$ for all $i$), no redistribution is needed. When opportunities are unequal, the Transfer Principle calls for redistribution among agents with identical preferences.

The paper does not model demand-side constraints, job rationing, or unemployment. All non-participation is voluntary. However, the conclusion notes that "when unemployment takes the form of constrained part time jobs... this should also be tackled by considering it as a reduction of the agents' earning ability" (p. 74). This suggests that involuntary non-participation can be accommodated by setting $w_i = 0$ or $w_i < w_m$ for constrained agents.

# Welfare / normative object

**Individual welfare:** Equivalent wage $W_i(z_i) = \max\{w \geq 0 \mid \forall \ell, z_i R_i (\ell, w\ell)\}$.

**Social welfare:** $\min_i W_i(z_i)$ (maximin / leximin over equivalent wages).

This is an instance of the "egalitarian-equivalent" approach from fair allocation theory (Pazner and Schmeidler 1978; Fleurbaey and Maniquet 1996a). The reference bundle is full-time labour at wage $w$ -- the equivalent wage is defined relative to this reference.

# Main findings

1. **Theorem 1:** The five axioms (Transfer Principle, Laisser-Faire, Weak Pareto, Hansson Independence, Separability) uniquely select maximin over equivalent wages $W_i$ as the social ranking criterion.

2. **Theorem 2 (comparison criterion):** Under Low-Skill Diversity, tax schedule $\tau$ is socially preferred to $\tau'$ whenever its maximal average tax rate over low incomes ($[0, w_m]$) is lower:

$$\max_{0 \leq y \leq w_m} \frac{\tau(y)}{y} < \max_{0 \leq y \leq w_m} \frac{\tau'(y)}{y}$$

This is a simple, observable criterion requiring only knowledge of $w_m$ (approximated by the minimum wage).

3. **Theorem 3 (optimal tax features):** The optimal tax maximises the net income $w_m - \tau(w_m)$ of the hardworking poor, subject to:
   - $\tau(y)/y \leq \tau(w_m)/w_m$ for $y \in (0, w_m]$ (average tax rate bounded by that at $w_m$)
   - $\tau(y) \geq \tau(w_m)$ for all $y$ (tax never falls below the level at $w_m$)
   - $\tau(0) \leq 0$ (subsidy at zero earnings)

4. **Non-positive marginal tax rates on low incomes** are obtained for all distributions (not just special cases), unlike in utilitarian optimal taxation where negative marginal rates arise only with specific distributions.

5. **Priority to the hardworking poor over the idle:** The social objective focuses on the lowest-skilled agents who work full time, not on non-workers. This is because the equivalent wage $W_i$ is lowest for full-time low-skilled workers (they are "poor despite working hard").

6. **US TANF reform illustration (Figure 13):** The 1986-to-2000 reform reduced the maximum average tax rate over low incomes and is therefore an improvement by the paper's criterion.

# Main limitations

- Theoretical framework with no empirical implementation
- Assumes all agents participate voluntarily (no involuntary unemployment beyond the $w_m = 0$ corner)
- Single-dimensional tax instrument $\tau(y)$ -- cannot condition on hours or other observables
- Low-Skill Diversity assumption is restrictive (rules out "gaps" in the earnings distribution of low-skilled agents)
- Does not address multi-dimensional screening (the paper acknowledges this is intractable)
- Skills are exogenous (no human capital investment, no endogenous productivity)
- No dynamics, no savings, no life-cycle considerations

# Relevance for my JMP

## possible use as the normative foundation for equivalent income
This paper provides the axiomatic derivation of the equivalent wage/income metric that my JMP uses as the welfare measure. The equivalent wage $W_i(z_i)$ defined here is directly analogous to the equivalent income in Bargain et al. (2013) and Fleurbaey (2009). For my JMP, this paper establishes *why* equivalent income is the right welfare metric: it is uniquely selected by specific, transparent, and defensible fairness axioms. The alternative -- utilitarian SWF with arbitrary weights -- is shown to violate the Laisser-Faire axiom.

## possible use for the "hardworking poor" priority
The paper's finding that the optimal tax prioritises the hardworking poor (lowest-skilled, highest-labour agents) is directly relevant to evaluating in-work benefit reforms. In my JMP, the RURO framework separates voluntary from involuntary non-participation; this paper's framework suggests that among workers, priority goes to those with the lowest equivalent wage -- which will be the low-skilled, full-time workers. The RURO decomposition adds: among non-workers, those who are involuntarily non-participating (opportunity-constrained) should receive higher priority than those who voluntarily choose leisure.

## possible use for connecting fairness to optimal taxation
This paper bridges fair allocation theory (Fleurbaey 1995) and optimal taxation (Mirrlees 1971). My JMP occupies the same bridge: I use the equivalent income metric from fair allocation theory to evaluate tax-benefit reforms in a structural labour supply framework. Citing this paper positions my welfare analysis within the fairness-based optimal taxation literature rather than the utilitarian tradition.

# Research questions this paper inspires

1. The paper assumes all non-participation is voluntary. In the RURO framework, some agents face $\theta = 0$ (no job offers). How does the equivalent wage $W_i$ change when the agent cannot choose freely on the budget $c \leq w\ell$ because no job is available? Should the equivalent wage account for the *feasible* set (actual opportunities) or the *hypothetical* set (all hours available)?

2. The paper's criterion (minimise maximum average tax rate over low incomes) is remarkably simple. Does this criterion survive when demand-side constraints are introduced? If some low-skilled agents are rationed, the envelope curve of indifference curves changes, potentially altering the criterion.

3. The equivalent wage $W_i$ is defined as the wage that achieves the same utility without redistribution. But in the RURO framework, the "same utility" depends on the opportunity set -- an agent with $\theta = 0$ cannot achieve any positive utility from market work. How should $W_i$ be defined when opportunities are constrained?

# Challenge to this paper

The paper's central welfare metric -- the equivalent wage -- measures well-being relative to a hypothetical world where the agent faces budget $c \leq W_i \ell$ with no tax. But this reference world assumes perfect labour market access: the agent can choose any hours level freely. In markets with demand-side constraints (job rationing, hours restrictions), this reference is unrealistic. An agent with equivalent wage $W_i = 10$ may be worse off than an agent with $W_i = 8$ if the first agent faces no job offers while the second has full-time employment. The RURO framework's opportunity measure $\theta$ captures this distinction, but the equivalent wage as defined here does not.

More broadly, the Laisser-Faire axiom -- no redistribution when skills are equal -- presumes that equal skills imply equal opportunities. In a world with demand-side frictions, two agents with the same skill may face very different opportunity sets (e.g., one lives in a region with high unemployment). The axiom's normative appeal weakens when opportunity inequality has sources beyond skill inequality.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The equivalent wage $W_i(z_i)$ is the welfare measure in $W(z, R, A; y)$ when $A$ is unrestricted (all hours available) and $y$ is the laissez-faire schedule ($\tau = 0$). Specifically, $W_i = \max\{w \mid \forall \ell, z_i R_i (\ell, w\ell)\}$ uses only the realised bundle $z$ and preferences $R$ -- the opportunity set $A$ does not enter because the reference world assumes unconstrained choice.

[Reasonable inference for my project] To incorporate the opportunity set $A$ into the welfare metric, one would need to modify the reference: instead of "what wage would make you indifferent without any tax?", ask "what wage would make you indifferent given the *same opportunities*?" This modification would yield a welfare metric $W_i(z_i, R_i, A_i)$ that depends on the opportunity set, allowing the RURO framework to contribute to the normative analysis. Alternatively, the opportunity constraint could be treated as part of the "handicap" (like a skill reduction), as suggested in the paper's conclusion.

[Unclear from paper] Whether the axiomatic foundation survives the introduction of opportunity constraints. The Laisser-Faire axiom says "no redistribution when skills are equal", but what about "no redistribution when skills *and opportunities* are equal"? Extending the axioms to multi-dimensional handicaps (skills + opportunities) is an open question that connects to Fleurbaey's (2009) discussion of the three reference options for labour.

# Relation to Bargain et al. (2013)

Bargain et al. (2013) compute equivalent incomes using a structural discrete-choice model, implementing the welfare metric axiomatised in this paper. The equivalent wage $W_i$ here corresponds to the equivalent income $\tilde{y}_i$ in Bargain et al., with the difference that Bargain et al. use a specific parametric utility function rather than ordinal preferences. The maximin social welfare function is the same. This paper provides the normative justification for Bargain et al.'s welfare analysis; Bargain et al. provide the empirical implementation.

# Relation to opportunities vs preferences

The paper draws a sharp line: skills are a source of illegitimate inequality (to be compensated via taxation), preferences are a source of legitimate inequality (to be respected via the Laisser-Faire axiom). This is the compensation-responsibility framework from Fleurbaey (1995). The paper does not distinguish opportunities from skills -- both are treated as the "handicap" dimension. The RURO framework adds a third element: the opportunity set $A_i$ (demand-side constraints), which is arguably another source of illegitimate inequality (like skills, it is beyond the agent's control). Incorporating $A_i$ into the fairness framework would strengthen the case for redistribution toward opportunity-constrained agents.

# Useful quotations / formulas

**Definition of the equivalent wage (p. 62):**
"Concretely, $W_i(z_i)$ is the wage rate which would enable agent $i$ to reach the same satisfaction as in $z_i$, if she were allowed to choose her labour time freely, at this wage rate: 'What wage rate would give you the same satisfaction as your current situation?'"

**On why $W_i$ avoids the weighting problem (p. 56):**
"For any given individual, her equivalent wage, relative to a particular indifference curve, is the hypothetical wage rate which would enable her to reach this indifference curve if she could choose her labour time at this wage rate. This particular measure of well-being, which is induced by the fairness conditions, does not require any other information about individuals than ordinal non-comparable preferences."

**On the comparison criterion (p. 71):**
"The application of the criterion requires no information about the population characteristics, except the value of $w_m$, which, in practice, may be thought to coincide with the legal minimum wage."

**On the focus on the hardworking poor (p. 73):**
"This result does not say that every optimal tax must satisfy these constraints, but it says, quite relevantly for the social planner, that there is no problem, i.e. no welfare loss, in restricting attention to taxes satisfying those constraints, when looking for the optimal allocation."

**On unemployment as skill reduction (p. 74):**
"Since unemployment may be viewed as nullifying the agents' earning ability, this result should best be interpreted as suggesting that the focus of redistributive policies should shift from the hardworking poor to the low-income households when the extent of unemployment is large."

# Suggested tags

fair-taxation, equivalent-wage, equivalent-income, maximin, optimal-tax, fairness-axioms, Transfer-Principle, Laisser-Faire, Hansson-Independence, Separability, Pigou-Dalton, hardworking-poor, low-skilled, incentive-compatibility, Mirrlees, social-preferences, Fleurbaey, Maniquet, compensation-responsibility

# My quick takeaway

The axiomatic foundation for using equivalent income as the welfare metric in optimal taxation. The key result: five transparent fairness axioms uniquely select (i) the equivalent wage $W_i$ as the individual welfare measure and (ii) maximin as the aggregation rule. The practical implication: compare tax schedules by the maximum average tax rate over low incomes -- lower is better. For my JMP, this paper provides the normative justification for the equivalent income approach used in Bargain et al. (2013) and my RURO-based welfare analysis. The main gap: the equivalent wage assumes unconstrained labour market access, which the RURO framework relaxes. Incorporating demand-side opportunity constraints into the fairness framework remains an open question.
