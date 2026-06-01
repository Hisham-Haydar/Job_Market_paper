---
title: "A fair solution to the compensation problem"
authors: [Giacomo Valletta]
year: 2009
outlet: "Social Choice and Welfare, 32, 455--478"
country_or_context: "Theoretical fair division / social ordering under non-transferable talents"
population: "Finite population of agents differing in non-transferable talents and preferences"
data_period: "Not applicable"
shelf: "fair division / compensation / responsibility / social orderings / non-transferable talents"
tags: [compensation-problem, social-ordering, second-best-fairness, non-transferable-talents, E-maximin, conditional-equality, incentive-compatibility, responsibility-sensitive-fairness, aversion-to-lack-of-talent, Valletta]
priority: "high"
read_status: "extracted"
---

# Full citation

Valletta, G. (2009). A fair solution to the compensation problem. *Social Choice and Welfare*, 32, 455--478.

# One-sentence contribution

Replaces allocation rules by social orderings in a one-dimensional compensation problem with non-transferable talents, proving that fairness, efficiency, and robustness axioms uniquely characterise an $E^{\wedge}$-maximin ordering based on the viewpoint of agents most averse to low talent, with strong implications for incentive-compatible compensation policy.

# Why this paper matters

This paper tackles the normative tension between compensation and responsibility in a framework where individuals differ in both a non-transferable trait and preferences -- exactly the type of problem that arises when distinguishing opportunities from preferences in my JMP. Its key methodological innovation is the move from allocation rules to social orderings, which allows policy guidance even under informational/incentive constraints. This is directly relevant for building a social evaluation criterion over allocations in a jobs-and-wellbeing framework.

# Core research question

How should society rank allocations of a divisible resource among agents who differ in non-transferable talents and preferences, if one wants to compensate for talents (not responsible) while treating preference differences as individual responsibility, possibly under incentive constraints?

# Model / theoretical framework

**Axiomatic fair-division model.** Economy $e = (t_N, R_N, M)$: $N$ = finite set of agents, $t_i \in T$ = non-transferable talent, $R_i$ = preference ordering over $(m, t) \in \mathbb{R}_+ \times T$, $M$ = total divisible resource. Allocations: $m_N \in \mathbb{R}_+^N$.

**Key innovations:**
- Preferences defined over extended bundles $(m, t)$, enabling cross-talent comparisons.
- Social ordering function $R(e)$ ranks all allocations (feasible and infeasible).
- "Aversion to lack of talent" ordering $R \succeq_A R'$: single-crossing comparison of how much agents dislike low talent.

**Central welfare representation $E^{\wedge}(m_i, t_i, R_i)$:** Money that would make agent $i$ accept the best talent $t^H$; if no such amount exists, the hypothetical talent distance that would make zero transfer acceptable.

**Impossibility results (Lemmas 1--2):** No social ordering satisfies both Equal Preferences Transfer and Equal Talent Transfer; Strong Pareto is incompatible with both Equal Preferences Permutation and Equal Talent Permutation simultaneously.

**Main characterisation (Theorem 1):** Strong Pareto + Nested Preferences Transfer + Equal Preferences Permutation + Equal Talent Transfer to the Unhappy + Minimal Equal Talent Transfer + Separation $\Rightarrow$ $E^{\wedge}$-maximin social ordering.

**Incentive compatibility (Theorem 2):** Under single-crossing and richness assumptions, the optimal incentive-compatible allocation equalises welfare from the perspective of agents with highest aversion to lack of talent. Yields a conditional-equality rule using the most talent-averse preferences as reference.

# Key objects

- $E^{\wedge}(m_i, t_i, R_i)$: welfare representation; money equivalent of accepting best talent, or talent distance from best if no money suffices.
- $E^{\wedge}$-maximin social ordering: maximin over vector $(E^{\wedge}(m_i, t_i, R_i))_{i \in N}$.
- Aversion to lack of talent ordering $\succeq_A$: determines the reference perspective for second-best policy.
- Stepped compensation schedule (Figure 4): normative support for threshold-type disability compensation systems.

# Data

Not applicable. Purely theoretical.

# Identification logic

Axiomatic characterisation. The combination of fairness, efficiency, and robustness axioms pins down the social ordering uniquely. The impossibility results (Lemmas 1--2) motivate weakening from full compensation-plus-responsibility to the specific combination of axioms in Theorem 1.

# Treatment of preferences

Preferences are heterogeneous and normatively central. The paper explicitly assumes responsibility for preferences while treating talents as compensable. The final characterisation gives a special role to agents with the highest aversion to lack of talent: the social evaluation takes their viewpoint as the reference. This is a deep substantive result -- when society organises compensation, it should adopt the perspective of those least willing to accept low talent.

# Treatment of opportunities / constraints

No modelling of opportunities as feasible job sets, menus, or latent offers. No $A_i$ object. The only constrained object is the one-dimensional aggregate resource. However, the model does treat non-transferable talent as an exogenous heterogeneity requiring compensation, which is conceptually analogous to non-transferable opportunity-set restrictions. The paper's treatment of incentive constraints (unobservable preferences) is relevant for second-best institutional design.

# Welfare / normative object

Social ordering over allocations of compensation resources, constructed from the $E^{\wedge}$ welfare representation and maximin aggregation. Not a money-metric utility or equivalent income, but a fairness-derived welfare representation that shares the compensatory logic with equivalent income. Explicitly about compensation vs responsibility.

# Main findings

1. **Impossibility:** Full compensation and full responsibility cannot both be satisfied (Lemmas 1--2).
2. **Infinite inequality aversion emerges:** Nested Preferences Transfer + Equal Preferences Permutation + Separation imply absolute priority for the worse-off in $E^{\wedge}$ (Lemma 3).
3. **Unique characterisation:** Theorem 1 pins down $E^{\wedge}$-maximin as the unique social ordering satisfying the combined axioms.
4. **Second-best policy:** Under incentive compatibility, optimal compensation uses the most talent-averse preferences as reference and equalises welfare from that viewpoint (Theorem 2).
5. **Policy implication:** Threshold-type compensation (no transfer above a talent cutoff) can be normatively justified, supporting real-world disability compensation structures (Figure 4).

# Main limitations

- One-dimensional resource and scalar talent: unclear how much structure survives in multidimensional settings.
- No explicit opportunity sets, jobs, wages, or budget sets.
- Responsibility for preferences is assumed, not derived: the results are conditional on this contested normative cut.
- Richness and single-crossing assumptions for incentive compatibility are restrictive.
- No empirical application.

# Relevance for my JMP

## possible use for social ordering construction
Highly relevant. The paper shows how fairness axioms can generate a social ordering over allocations that respects compensation while handling responsibility and incentive constraints. If my framework needs not just an individual $W$-measure but also a social ranking of policies/allocations, this paper provides the normative architecture.

## possible use for the reference perspective
The result that the most talent-averse preferences determine the reference viewpoint is suggestive for choosing reference opportunity sets in my framework: analogously, "aversion to lack of opportunities" might determine the relevant reference for compensation.

## possible use for impossibility awareness
The impossibility results (compensation + responsibility cannot both be fully satisfied) apply to any richer framework that tries to distinguish compensable from responsible heterogeneity.

# Research questions this paper inspires

1. What is the analogue of $E^{\wedge}$-maximin when the non-transferable heterogeneity is a feasible job set $A_i$ rather than a scalar talent?

2. Can "aversion to lack of opportunities" be defined analogously to "aversion to lack of talent," and would it similarly determine the reference perspective for compensation?

3. How does the compensation/responsibility impossibility change when the compensated object is a multidimensional opportunity set?

# Challenge to this paper

The elegance of the characterisation rests on a scalar talent and one-dimensional transfer. The hard question for my JMP is whether the same axiomatic structure survives when disadvantage is a multidimensional opportunity set $A_i$ and the relevant "transfer" is not just money but tax-transfer policy affecting the entire opportunity distribution. The paper's greatest insight -- that reference perspectives emerge endogenously from axioms -- deserves extension to richer environments.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] Compensation among agents differing in non-transferable talent and preferences. Social ordering over monetary allocations based on fairness, efficiency, and robustness. No $W(z,R,A;y)$, no feasible set $A$, no pay schedule $y$.

[Reasonable inference for my project] Loose mapping: $z$ = money transfer + talent; $R$ = preferences over $(m,t)$; $A$ has no counterpart; $y$ has no counterpart. The strongest connection is through the second-best compensation logic and the endogenous emergence of a reference perspective.

[Unclear from paper] How to extend $E^{\wedge}$-maximin to settings with $A$-type feasible sets; whether independence of $A$ or $y$ axioms relate to the paper's framework.

# Relation to Bargain et al. (2013)

Not directly related.

# Relation to opportunities vs preferences

Not about opportunities vs preferences in the labour economics sense. Highly relevant to the nearby normative distinction: how to compensate exogenous heterogeneity while respecting preference differences treated as individual responsibility. The paper clarifies how social evaluation changes once one insists on a responsibility cut and on incentive compatibility. What is missing is reinterpretation of the non-transferable characteristic as a feasible opportunity set.

# Useful quotations / formulas

**Welfare representation:**
$$E^{\wedge}(m_i, t_i, R_i) = \begin{cases} \hat{m}_i & \text{if } \hat{m}_i \text{ exists} \\ \hat{t}_i - t^H & \text{otherwise} \end{cases}$$

**Key impossibility (Lemma 1):** No social ordering satisfies both Equal Preferences Transfer and Equal Talent Transfer.

**Characterisation (Theorem 1):** SP + NPT + EPP + ETTU + METT + Sep $\Rightarrow$ $E^{\wedge}$-maximin.

**Incentive compatibility (Theorem 2):** Optimal allocation under IC equalises $E^{\wedge}$ using the most talent-averse preferences as reference.

# Suggested tags

compensation-problem, social-ordering, second-best-fairness, non-transferable-talents, E-maximin, conditional-equality, incentive-compatibility, responsibility-sensitive-fairness, aversion-to-lack-of-talent, Valletta

# My quick takeaway

A strong normative paper showing how fairness axioms uniquely characterise an $E^{\wedge}$-maximin social ordering for compensation under non-transferable talent heterogeneity. For my JMP, its most valuable contributions are: (1) the methodological move from allocation rules to social orderings (enabling second-best policy), (2) the endogenous emergence of a reference perspective from axioms (the most talent-averse preferences), and (3) the clear impossibility results showing that full compensation and full responsibility are jointly unattainable. The extension to multidimensional opportunity sets is the natural next step.
