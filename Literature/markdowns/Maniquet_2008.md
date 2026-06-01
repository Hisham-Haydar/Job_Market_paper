---
title: "Social orderings for the assignment of indivisible objects"
authors: [Francois Maniquet]
year: 2008
outlet: "Journal of Economic Theory, 143(1), 199--215"
country_or_context: "Theoretical (indivisible goods assignment)"
population: "N/A (abstract social choice model)"
data_period: "N/A (theoretical)"
shelf: "social choice / money-metric utility / leximin / fairness / axiomatic"
tags: [social-ordering, money-metric-utility, money-equivalent, leximin, maximin, indivisible-objects, fairness, Transfer-Principle, Anonymity, Consistency, Independence, axiomatic, Maniquet]
priority: "low-medium"
read_status: "extracted"
---

# Full citation

Maniquet, F. (2008). Social orderings for the assignment of indivisible objects. *Journal of Economic Theory*, 143(1), 199--215.

# One-sentence contribution

Proves that in the assignment problem of indivisible objects with money, the only social ordering function satisfying Strong Pareto, Independence of Preferences over Infeasible Bundles, Consistency, the Transfer Principle among Equals, and Anonymity among Equals is the leximin applied to money equivalents (the amount of money that would leave each agent indifferent between their assigned bundle and receiving only money).

# Why this paper matters

This paper provides a clean axiomatic foundation for using money-metric utility (money equivalents) as the basis for social evaluation, in a setting simpler than labour-consumption models. The key insight -- that efficiency, independence, and consistency axioms force us to use money equivalents, and then fairness axioms select the leximin aggregation -- parallels the equivalent-income approach in Fleurbaey & Maniquet's optimal taxation work. It demonstrates that the leximin-over-money-metric-utility result is not specific to labour supply models but holds in a broader class of economic problems.

# Core research question

In the assignment of indivisible objects with monetary transfers, what social ordering function satisfies efficiency (Pareto), implementability (independence of preferences over infeasible bundles), consistency (invariance to population changes), and fairness (transfer principle and anonymity)?

# Economic setting and context

Abstract model. Infinite set $\mathcal{A}$ of objects, infinite set $\mathcal{N}$ of agents. An economy $E = (N, A, R)$ has finite agents $N$, finite available objects $A \subset \mathcal{A}$, and preferences $R = (R_i)_{i \in N}$ over object-money bundles $(a, m) \in \mathcal{A}^* \times \mathbb{R}$ where $\mathcal{A}^* = \mathcal{A} \cup \{v\}$ ($v$ = null object). Preferences are continuous, strictly monotone in money, and all objects are desirable with finite values. Feasibility: no two agents share an object, $\sum m_i \leq 0$.

# Model / theoretical framework

**Money utility (money equivalent):** $u(R_i, z_i) = m$ where $z_i I_i (v, m)$ -- the amount of money that makes agent $i$ indifferent between receiving only money $m$ (no object) and their actual bundle $z_i = (a_i, m_i)$.

**Five axioms:**
1. **Strong Pareto:** If all weakly prefer $z$ to $z'$ and at least one strictly prefers, then $z$ is socially strictly preferred.
2. **Independence of Preferences over Infeasible Bundles:** Changes in preferences over bundles containing unavailable objects do not affect social ordering.
3. **Consistency:** Removing agents who receive the same bundle in both allocations does not change the social ranking.
4. **Transfer Principle among Equals:** For agents with identical preferences, a money transfer from richer to poorer (preserving ranking) is a strict social improvement.
5. **Anonymity among Equals:** Permuting bundles between same-preference agents does not change social evaluation.

**Definition -- Money Equivalent Leximin $\mathbf{R}^L$:** For allocations $z, z'$, find money equivalents $m^*, m^{*\prime}$ such that $z_i I_i(v, m_i^*)$ and $z_i' I_i(v, m_i^{*\prime})$. Then $z \mathbf{R}^L z' \Leftrightarrow m^* \geq_{\text{lex}} m^{*\prime}$.

# Key objects

- **Money equivalent $u(R_i, z_i)$:** The amount of money making agent $i$ indifferent between $(v, m)$ and their actual bundle -- analogous to money-metric utility in labour-consumption models
- **Money Equivalent Property:** Social orderings depend only on money equivalents (intermediate result, Lemma 1)
- **Money Utility Welfarism:** Social ordering is welfarist in money utility (Lemma 2: equivalent to Money Equivalent Property)
- **Maximin Money Equivalent Property:** If the minimum money equivalent rises, social welfare improves (Lemma 4)

# Data

No data. Purely theoretical.

# Identification logic

Not applicable (axiomatic social choice theory).

# Estimation / empirical strategy

Not applicable.

# Treatment of preferences

Preferences are ordinal, heterogeneous, continuous, and strictly monotone in money. The paper explicitly requires only ordinal information -- no cardinal utility or interpersonal utility comparisons. The key innovation: the money equivalent $u(R_i, z_i)$ provides interpersonal comparability despite using only ordinal preferences, because it anchors comparison at the common "null object + money" consumption set.

# Treatment of opportunities / constraints

The feasible set varies across economies (different available objects, different agents). The Independence axiom ensures that preferences over infeasible bundles are irrelevant. No labour supply, no demand-side constraints -- this is a pure assignment model.

# Welfare / normative object

The leximin applied to money equivalents: $\mathbf{R}^L$. This is the unique social ordering function satisfying all five axioms (Theorem 1). In first-best contexts, it selects allocations equalising money equivalents. In second-best contexts (with incentive or feasibility constraints), it applies the leximin to the constrained set.

# Main findings

1. **Lemma 1:** Pareto Indifference + Independence of Preferences over Infeasible Bundles + Consistency → Money Equivalent Property. The social ordering depends only on money equivalents. This is the foundational result: efficiency, implementability, and consistency force us to evaluate allocations using money equivalents.

2. **Lemma 2:** Money Equivalent Property ↔ Money Utility Welfarism. The social ordering is welfarist with money utility as the individual welfare measure.

3. **Lemma 3:** The Money Equivalent Leximin $\mathbf{R}^L$ satisfies all five axioms (existence/possibility result).

4. **Lemma 4:** Strong Pareto + Money Equivalent Property + Transfer Principle among Equals → Maximin Money Equivalent Property. Fairness forces maximin aggregation.

5. **Lemma 5:** Money Equivalent Property + Maximin + Consistency + Anonymity among Equals → Leximin. The maximin is strengthened to leximin.

6. **Theorem 1 (main result):** $\mathbf{R}$ satisfies Strong Pareto, Independence, Consistency, Transfer Principle among Equals, and Anonymity among Equals **if and only if** $\mathbf{R} = \mathbf{R}^L$ (Money Equivalent Leximin).

7. **Independence of axioms (p. 213):** Each axiom is necessary. Dropping Independence allows any welfarist function. Dropping Consistency allows $v$-utility or $w$-utility leximin. Dropping Strong Pareto allows variance-minimising functions. Dropping Transfer Principle allows sum-maximising. Dropping Anonymity allows tie-breaking by agent identity.

# Main limitations

- The setting (indivisible objects with money) is distant from labour supply and income taxation
- The key structural feature enabling the result -- that the "null object + money" consumption set is always feasible and common to all agents -- may not have a clean analogue in all economic settings
- The preference richness assumption is essential: with quasi-linear preferences, any concave utilitarian SWF would satisfy the axioms, and the leximin would not be uniquely selected
- No application to policy evaluation or empirical analysis

# Relevance for my JMP

## possible use for the axiomatic foundation of money-metric utility
The paper provides a clean demonstration that money equivalents (money-metric utility) are not an arbitrary welfare measure but are uniquely selected by basic efficiency, independence, and consistency axioms. This strengthens the theoretical case for using equivalent income in my RURO welfare analysis. The key insight: the money equivalent is the only welfare index that satisfies implementability (independence of preferences over infeasible bundles) while remaining welfarist.

## possible use for the leximin result
The paper shows that combining the money-metric welfarist framework with Pigou-Dalton transfer fairness axioms uniquely selects the leximin aggregation (not just any concave SWF). This is relevant because Bargain et al. (2013) and Fleurbaey & Maniquet (2006, 2007) all use maximin/leximin over equivalent income. The paper shows this is not an arbitrary choice but is axiomatically forced.

# Research questions this paper inspires

1. Does the analogue of the "null object" in labour supply models -- the bundle $(0, -\tau(0))$ (not working, receiving the basic income) -- play a similar anchoring role for money-metric utility? If so, the money-metric utility in labour supply is anchored at the participation margin, which is where demand-side constraints (modelled by the RURO opportunity density) are most relevant.

# Challenge to this paper

The result depends on the assumption that it is always feasible to assign no object and only money to any agent. In labour supply models, the analogue would be that voluntary non-participation is always feasible. If some agents face participation constraints (must work to survive, or face sanctions for non-participation), the "null object" assumption fails, and the money equivalent may not be well-defined or may not capture welfare correctly. The RURO framework, where the opportunity density $g(h, w)$ can restrict options including the non-participation option, highlights this limitation.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The paper's money equivalent $u(R_i, z_i)$ is the analogue of the money-metric utility $m_i(\tilde{w}, z_i)$ in my framework, with the "null object" playing the role of the reference wage $\tilde{w}$. The leximin aggregation over money equivalents corresponds to the maximin social welfare function over equivalent incomes.

[Reasonable inference for my project] The Independence of Preferences over Infeasible Bundles axiom has a direct analogue for labour supply: preferences over job-hours-wage combinations that are not available in the agent's opportunity set $A_i$ should not affect the welfare ranking. This supports the RURO framework's explicit modelling of the opportunity set: only preferences over feasible jobs should matter.

[Unclear from paper] Whether the uniqueness result (leximin over money equivalents) extends to settings where the opportunity set varies across agents, as in the RURO model. If agent $i$'s feasible set depends on their opportunity density $g_i(h, w)$, the "common consumption set" that enables the money equivalent construction may shrink or vary across agents.

# Relation to Bargain et al. (2013)

Indirect connection. The paper provides the axiomatic foundation for why money-metric utility + leximin is the right welfare criterion. Bargain et al. (2013) implement this criterion empirically using equivalent incomes computed from structural labour supply models. This paper explains why that specific combination (money-metric + leximin) is uniquely selected by fairness axioms.

# Relation to opportunities vs preferences

The paper does not address the preferences-vs-opportunities distinction. All agents face the same set of available objects (though assignments differ). The key structural assumption -- that the "null object" is always available -- ensures that money equivalents are well-defined for all agents regardless of their assignment. In the RURO framework, the analogue would be that non-participation is always feasible, which may not hold for all agents.

# Useful quotations / formulas

**On why money equivalents are forced (p. 204):**
"That only money equivalents matters comes from the fact that, since it is always possible to assign the null object to an agent, the part of the consumption set where money equivalents are computed is always part of the set of feasible bundles."

**On the relationship to welfarism (p. 206--207):**
"In this specific model of indivisible good assignment, combining Pareto Indifference, Independence of Preferences over Infeasible Bundles and Consistency forces us to be welfarist and to use money utility as the proper indicator of individual welfare."

**On why preference richness matters (p. 213):**
"If, instead, we had restricted ourselves to quasi-linear preferences, for instance, the maximin property could not have been deduced. Indeed, any generalized utilitarian social welfare function $\sum f(u(R_i, z_i))$ with strictly increasing and concave $f$ would satisfy all our axioms."

# Suggested tags

social-ordering, money-metric-utility, money-equivalent, leximin, maximin, indivisible-objects, fairness, Transfer-Principle, Pigou-Dalton, Anonymity, Consistency, Independence, axiomatic, social-choice, welfarism, Maniquet

# My quick takeaway

A clean axiomatic result showing that efficiency + implementability + consistency + fairness uniquely select the leximin over money equivalents in an assignment model. For my JMP, this strengthens the case for using equivalent income (money-metric utility) with maximin/leximin aggregation as the welfare criterion: it is not an arbitrary choice but is axiomatically forced by basic desiderata. The paper is somewhat tangential to labour supply modelling but provides important theoretical foundations for the welfare analysis methodology.
