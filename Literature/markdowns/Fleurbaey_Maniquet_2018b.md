---
title: "Inequality-averse well-being measurement"
authors: [Marc Fleurbaey, Francois Maniquet]
year: 2018
outlet: "International Journal of Economic Theory, 14(1), 35--50"
country_or_context: "Theoretical (abstract consumption model)"
population: "N/A (abstract social choice model)"
data_period: "N/A (theoretical)"
shelf: "well-being measurement / money-metric utility / ray utility / inequality aversion / fairness / axiomatic"
tags: [well-being-measurement, money-metric-utility, ray-utility, inequality-aversion, diminishing-priority, nested-contour, concave-transformation, fairness, axiomatic, Fleurbaey, Maniquet, transfer-principle, Leontief, linear-preferences]
priority: "medium"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Maniquet, F. (2018). Inequality-averse well-being measurement. *International Journal of Economic Theory*, 14(1), 35--50.

# One-sentence contribution

Introduces inequality-aversion (transfer/priority) axioms into the axiomatic framework for well-being measurement and shows that: (1) combining "diminishing priority" with infimum nested contour uniquely selects strictly concave transformations of the money-metric utility; (2) combining "weak diminishing priority" with supremum nested contour uniquely selects strictly concave transformations of the ray utility; but (3) the full "nested priority" axiom is incompatible with nested contour altogether.

# Why this paper matters

This paper extends Fleurbaey and Maniquet (2017a) by adding inequality-aversion properties to the well-being measurement framework. The key contribution: it shows that requiring well-being measures to exhibit diminishing marginal value (so that egalitarian social welfare functions would prioritise the worse-off) pins down not just the general family of measures (ray utility or money-metric) but also requires them to be strictly concave transformations of the base measure. This bridges the gap between individual well-being measurement and social welfare aggregation by embedding inequality aversion directly into the well-being measure itself, rather than only in the aggregation rule.

# Core research question

Can individual well-being measures be constructed to satisfy both fairness principles (comparing indifference sets) and inequality-aversion properties (diminishing marginal well-being from additional resources), and if so, what specific measures result?

# Economic setting and context

Same abstract model as Fleurbaey and Maniquet (2017a): $K$ divisible goods, consumption set $X = \mathbb{R}^K_+$, continuous convex monotonic preferences $R \in \mathcal{R}$. No institutional context, no labour supply.

# Model / theoretical framework

**Building blocks from Fleurbaey and Maniquet (2017a):**

- **Supremum Nested Contour (Axiom 1):** If $L(x, R) \subset \text{interior}[L(x', R') \cup L(x'', R'')]$, then $W(x, R) < \max\{W(x', R'), W(x'', R'')\}$.
- **Infimum Nested Contour (Axiom 2):** If $U(x, R) \subset \text{interior}[CH(U(x', R') \cup U(x'', R''))]$, then $W(x, R) > \min\{W(x', R'), W(x'', R'')\}$.
- **Lemma 1 (from 2017a):** Supremum Nested Contour $\iff$ $\exists R^w \in \mathcal{R}^w$ (worst preferences) such that $W(x, R) = \max_{x' \in L(x,R)} W(x', R^w)$.
- **Lemma 2 (from 2017a):** Infimum Nested Contour $\iff$ $\exists R^b \in \mathcal{R}^b$ (best preferences) such that $W(x, R) = \min_{x' \in U(x,R)} W(x', R^b)$.

**New inequality-aversion axioms:**

**Axiom 4 -- Nested Priority:** For all $x, x' \in X$, $R, R' \in \mathcal{R}$, $\lambda \in (0,1)$, if $x' \gg x$ and $L(x + \lambda(x'-x), R) \cap U(x', R') = \emptyset$, then:
$$W(x + \lambda(x'-x), R) - W(x, R) > W(x' + \lambda(x'-x), R') - W(x', R').$$
(Transferring a fraction of resources to a poorer agent increases their well-being more than it would increase the well-being of a richer agent.)

**Axiom 5 -- Diminishing Priority:** Same as Nested Priority but restricted to cases where the indifference curves of the poorer agent are upward translations (by $\Delta$) of the richer agent's indifference curves:
$$y = x + \lambda\Delta, \quad U(x', R') = U(x, R) + \Delta, \quad U(y', R') = U(y, R) + \Delta, \quad L(y, R) \cap U(x', R') = \emptyset$$
$$\Rightarrow W(y, R) - W(x, R) > W(y', R') - W(x', R').$$

**Axiom 6 -- Weak Diminishing Priority:** Same as Diminishing Priority but restricted to one specific direction $\Delta \in \mathbb{R}^L_{++}$ (rather than all directions).

**Key results:**

**Lemma 3 (Impossibility):** No well-being measure satisfies both Nested Priority and Nested Contour. The conflict arises because Nested Contour requires well-being to depend on indifference surfaces, while Nested Priority requires it to respond to bundle differences -- and these two requirements clash when indifference curves can be arbitrarily close while bundles are far apart.

**Theorem 1 (Money-Metric with Concavity):** $W$ satisfies Infimum Nested Contour and Diminishing Priority $\iff$ $\exists p \in \text{interior}[S^{K-1}]$ and a strictly concave $g: \mathbb{R}_+ \to \mathbb{R}_+$ such that $W = g \circ W^p$.

**Lemma 4 (Second Impossibility):** No well-being measure satisfies Supremum Nested Contour and Diminishing Priority. (The full diminishing priority is incompatible with the ray-utility family.)

**Theorem 2 (Ray Utility with Concavity):** $W$ satisfies Supremum Nested Contour and Weak Diminishing Priority $\iff$ $\exists \ell \in \text{interior}[X]$ and a strictly concave $g: \mathbb{R}_+ \to \mathbb{R}_+$ such that $W = g \circ W^\ell$.

# Key objects

- **Money-metric utility $W^p(x, R) = w \iff x \, I \, \max(R, \{x' \in X \mid px' \leq w\})$:** Expenditure at reference prices $p$ to reach satisfaction at $x$.
- **Ray utility $W^\ell(x, R) = w \iff x \, I \, w\ell$:** Amount along reference ray $\ell$ that is indifferent to $x$.
- **Strictly concave transformation $g$:** Ensures diminishing marginal well-being. Not pinned down by the axioms beyond strict concavity.
- **Nested Priority vs Diminishing Priority:** Full nested priority is too strong (impossibility); diminishing priority is the viable weakening that pins down concave money-metric. Weak diminishing priority (one direction only) is needed for the ray utility family.

# Data

No data. Purely theoretical.

# Identification logic

Not applicable (axiomatic theory).

# Estimation / empirical strategy

Not applicable.

# Treatment of preferences

Same as Fleurbaey and Maniquet (2017a): ordinal, heterogeneous, continuous, convex, monotonic. The paper shows that the choice between worst preferences (Leontief) and best preferences (linear) as the reference determines which family of well-being measures is obtained. The inequality-aversion axioms operate within each family, requiring a concave transformation.

# Treatment of opportunities / constraints

No treatment. The consumption set $X = \mathbb{R}^K_+$ is common to all agents. Well-being is measured at given bundles, with no modelling of how bundles are chosen or constrained.

# Welfare / normative object

Individual well-being measures $W(x, R)$ with built-in inequality aversion (concavity). The paper does not aggregate, but notes that if social welfare is the sum of individual well-being measures, then the concavity of $W$ automatically induces inequality aversion at the social level.

# Main findings

1. **Lemma 3 (Impossibility):** No well-being measure satisfies Nested Priority and Nested Contour simultaneously. This is because indifference-curve-based comparisons (Nested Contour) and bundle-based comparisons (Nested Priority) can conflict when indifference curves are close but bundles are far apart.

2. **Theorem 1 (Money-Metric + Concavity):** Infimum Nested Contour + Diminishing Priority $\iff$ $W = g \circ W^p$ for some reference prices $p$ and strictly concave $g$. The best preferences must be linear ($R^b = R^p$), and the transformation must be strictly concave.

3. **Lemma 4 (Second Impossibility):** Supremum Nested Contour + Diminishing Priority is impossible. The full diminishing priority is too strong for the ray utility family.

4. **Theorem 2 (Ray Utility + Concavity):** Supremum Nested Contour + Weak Diminishing Priority $\iff$ $W = g \circ W^\ell$ for some reference ray $\ell$ and strictly concave $g$. The worst preferences must be Leontief ($R^w = R^\Delta$), and weak diminishing priority can only hold in one direction $\Delta$.

5. **Asymmetry:** Diminishing priority is compatible with infimum nested contour (money-metric) but not with supremum nested contour (ray utility). Only the weaker version (weak diminishing priority, one direction) works with ray utility. This is an asymmetry favouring the money-metric family when inequality aversion is desired.

# Main limitations

- Same abstract setting as Fleurbaey and Maniquet (2017a): no labour supply, no institutional constraints, no heterogeneous opportunity sets.
- The concave transformation $g$ is not pinned down beyond strict concavity -- any strictly concave $g$ works. This leaves substantial degrees of freedom.
- The asymmetry between the two families (money-metric allows full diminishing priority; ray utility only allows weak diminishing priority) is a finding, but the paper does not clearly evaluate the normative implications.
- The conclusion acknowledges that extending to settings with bounded dimensions (leisure, health) where preferences may not be monotonic is future work.

# Relevance for my JMP

## possible use for justifying concavity in equivalent income
The paper shows that combining the money-metric utility family (which underlies equivalent income) with a natural inequality-aversion axiom (diminishing priority) requires using a strictly concave transformation of the money-metric utility. In my RURO welfare analysis, if I use equivalent income with a maximin/leximin aggregator, I am implicitly using the most concave transformation possible ($g(w) = w$ with leximin is the limit of $g_\alpha(w) = w^{1-\alpha}/(1-\alpha)$ as $\alpha \to \infty$). This paper provides the axiomatic foundation for why concavity in equivalent income is normatively justified.

## possible use for the asymmetry between money-metric and ray utility
The finding that money-metric utility is more naturally compatible with inequality aversion (full diminishing priority) than ray utility (only weak diminishing priority) provides an additional argument for choosing money-metric utility / equivalent income over ray utility as the welfare measure in my framework.

# Research questions this paper inspires

1. In the labour-consumption model, what does "diminishing priority" mean concretely? It requires that transferring resources from a richer to a poorer agent (in the indifference-curve sense) produces a larger well-being gain for the poorer agent. In the RURO setting, "resources" might include not just income but also job opportunities. Does diminishing priority extend naturally to transfers of opportunities?

# Challenge to this paper

The paper's axioms are formulated in terms of bundles and indifference curves, not in terms of budget sets or opportunity sets. In my RURO framework, two agents may consume the same bundle and have the same indifference curve at that bundle, but face vastly different opportunity sets. The paper's inequality-aversion axioms (Nested Priority, Diminishing Priority) compare agents based on their bundles and preferences only. An agent who is constrained to a poor bundle by a limited opportunity set and an agent who freely chose a poor bundle from a rich opportunity set would be treated identically by these axioms. A richer notion of inequality aversion would incorporate opportunity set differences.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The money-metric utility $W^p(x, R)$ is the direct analogue of equivalent income $m_i(\tilde{w}, z_i)$ in my framework. The paper shows that adding inequality aversion requires using $g \circ W^p$ where $g$ is strictly concave, which corresponds to applying a concave transformation to equivalent incomes before aggregation.

[Reasonable inference for my project] The leximin aggregation used in Fleurbaey & Maniquet's optimal taxation work is the limiting case of applying $g_\alpha(w) = w^{1-\alpha}/(1-\alpha)$ with $\alpha \to \infty$. This paper provides an intermediate foundation: it justifies strict concavity but does not single out the leximin. The full leximin characterisation requires additional axioms (as in Maniquet 2008).

[Unclear from paper] Whether the axioms extend to settings with heterogeneous opportunity sets and how inequality aversion should be modified to account for opportunity differences.

# Relation to Bargain et al. (2013)

Indirect. Bargain et al. (2013) use equivalent income with maximin aggregation. This paper shows that the well-being measure itself (before aggregation) should be a concave transformation of money-metric utility if one wants inequality aversion built into the measurement. Bargain et al. effectively use the identity transformation ($g(w) = w$) with maximin aggregation, which achieves extreme inequality aversion through the aggregator rather than through the measure. The paper suggests an alternative: moderate concavity in the measure combined with a less extreme aggregator (e.g., sum of concave-transformed equivalent incomes).

# Relation to opportunities vs preferences

The paper is about preferences only. Inequality aversion is defined over bundles and indifference curves, not over opportunity sets. The key axioms require that a richer agent (in terms of bundles) benefits less from additional resources than a poorer agent, holding preferences fixed. This is purely a consumption-space notion of inequality aversion that does not capture inequality in opportunities.

# Useful quotations / formulas

**On the impossibility (p. 40):**
"No well-being measure satisfies nested priority and nested contour." (Lemma 3)

**On the tension between bundles and indifference curves (p. 40):**
"This incompatibility comes from the conflict between insisting on indifference surfaces, as required by nested contour, and insisting on bundles, as required by nested priority."

**Money-metric characterisation (Theorem 1, p. 43):**
"A well-being measure $W$ satisfies infimum nested contour and diminishing priority if and only if there exist a vector $p \in \text{interior}[S^{K-1}]$ and a strictly concave function $g: \mathbb{R}_+ \to \mathbb{R}_+$ such that $W = g \circ W^p$."

**Ray utility characterisation (Theorem 2, p. 44-45):**
"A well-being measure $W$ satisfies supremum nested contour and weak diminishing priority if and only if there exist a bundle $\ell \in \text{interior}[X]$ and a strictly concave function $g: \mathbb{R}_+ \to \mathbb{R}_+$ such that $W = g \circ W^\ell$."

**On future extensions (p. 49-50):**
"Another direction of research that is worth considering is to explore more concrete and specific settings, for which the model of divisible commodities is not adapted. For instance, if health or leisure is a dimension, one dimension in the space is bounded and preferences for leisure may not be monotonic."

# Suggested tags

well-being-measurement, money-metric-utility, ray-utility, inequality-aversion, diminishing-priority, nested-contour, concave-transformation, fairness, axiomatic, Fleurbaey, Maniquet, transfer-principle, Leontief, linear-preferences, impossibility

# My quick takeaway

A companion to Fleurbaey & Maniquet (2017a) that adds inequality-aversion axioms to well-being measurement. The key results: (1) combining fairness with full diminishing priority uniquely selects concave transformations of money-metric utility; (2) ray utility can only accommodate a weaker version (one-directional). This provides an additional argument for choosing money-metric utility (equivalent income) as the welfare measure in my JMP, and justifies applying concave transformations to equivalent incomes before aggregation. The paper remains in an abstract setting without labour supply or opportunity constraints.
