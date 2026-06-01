---
title: "Fairness and well-being measurement"
authors: [Marc Fleurbaey, Francois Maniquet]
year: 2017
outlet: "Mathematical Social Sciences, 90, 119--126"
country_or_context: "Theoretical (abstract consumption model)"
population: "N/A (abstract social choice model)"
data_period: "N/A (theoretical)"
shelf: "well-being measurement / money-metric utility / ray utility / fairness / axiomatic / indifference curves"
tags: [well-being-measurement, money-metric-utility, ray-utility, fairness, axiomatic, indifference-curves, nested-contour, worst-preferences, best-preferences, Leontief, linear-preferences, Fleurbaey, Maniquet, egalitarian-equivalence, equal-income-Walrasian]
priority: "medium-high"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Maniquet, F. (2017). Fairness and well-being measurement. *Mathematical Social Sciences*, 90, 119--126.

# One-sentence contribution

Axiomatically derives two families of well-being measures from fairness principles: strengthening a basic "Nested Contour" axiom in one direction yields the ray utility (measuring well-being by the amount along a reference ray that leaves the agent indifferent), while strengthening it in another direction yields the money-metric utility (measuring well-being by the expenditure at reference prices that leaves the agent indifferent).

# Why this paper matters

This paper provides the deepest axiomatic foundation for the two most common individual well-being measures used in fair allocation and welfare economics: ray utility and money-metric utility. It shows that these are not arbitrary constructions but are uniquely justified by strengthening a basic fairness axiom (Nested Contour) in two natural but incompatible directions. The paper disentangles measuring individual well-being from aggregating it, focusing exclusively on the former. It connects the well-being measurement literature to the fair allocation literature by showing that ray utility corresponds to egalitarian equivalence allocations and money-metric utility corresponds to equal-income Walrasian allocations.

# Core research question

What well-being measures $W(x, R)$ -- assigning a real-valued well-being level to an agent consuming bundle $x$ with preferences $R$ -- are consistent with fairness principles, specifically the requirement that well-being comparisons respect agents' preferences and depend on the bundles of resources they consume?

# Economic setting and context

Abstract model with $K$ divisible goods, consumption set $X = \mathbb{R}^K_+$. Agents have continuous, convex, and monotonic preferences $R \in \mathcal{R}$ over bundles. No specific institutional setting, no taxes, no labour supply -- purely a framework for measuring individual well-being from bundles and preferences.

# Model / theoretical framework

**Well-being measure:** A function $W: X \times \mathcal{R} \to \mathbb{R}$ that is continuous in $x$ and respects preferences:
- $x R x' \Rightarrow W(x, R) \geq W(x', R)$
- $x P x' \Rightarrow W(x, R) > W(x', R)$

**Notation:** $L(x, R)$, $U(x, R)$, $I(x, R)$ denote the lower, upper, and indifference contour sets of $R$ at $x$.

**Key axioms (progressive strengthening):**

1. **Axiom 1 -- Nested Contour:** If $U(x, R) \cap L(x', R') = \emptyset$, then $W(x, R) > W(x', R')$. (If agent $R'$'s upper contour at $x'$ does not intersect agent $R$'s lower contour at $x$, then $R$ at $x$ is better off.)

2. **Axiom 2 -- Unchanged Indifference Independence:** If $I(x, R) = I(x, R')$, then $W(x, R) = W(x, R')$. (Equivalent to Nested Contour by Lemma 1.)

3. **Axiom 3 -- Supremum Nested Contour:** If the lower contour set $L(x, R)$ lies in the interior of the union of lower contour sets of a countable set $\mathcal{X}$, then $W(x, R) < \sup_{(x',R') \in \mathcal{X}} W(x', R')$.

4. **Axiom 4 -- Worst Preferences:** There exist $R^w \in \mathcal{R}^w$ such that for all $x \in X, R \in \mathcal{R}$, $W(x, R^w) \leq W(x, R)$. (Some preferences are universally worst -- their well-being is always lowest regardless of bundle.)

5. **Axiom 5 -- Infimum Nested Contour:** If $U(x, R)$ lies in the interior of the convex hull of the union of upper contour sets of a countable set $\mathcal{X}$, then $W(x, R) > \inf_{(x',R') \in \mathcal{X}} W(x', R')$.

6. **Axiom 6 -- Best Preferences:** There exist $R^b \in \mathcal{R}^b$ such that for all $x \in X, R \in \mathcal{R}$, $W(x, R^b) \geq W(x, R)$. (Some preferences are universally best.)

**Two families of well-being measures:**

**Family 1 -- Ray Utility $W^\ell$:**
$$W^\ell(x, R) = w \iff x \, I \, w\ell$$
where $\ell \in \mathbb{R}^K_+$ is a fixed reference ray. Well-being is measured by the scalar $w$ such that the bundle $w\ell$ on the ray is indifferent to $x$. Linked to Samuelson (1977), Pazner (1979), Deaton (1979).

**Family 2 -- Money-Metric Utility $W^p$:**
$$W^p(x, R) = w \iff x \, I \, \max(R, \{x' \in X \mid px' \leq w\})$$
where $p \in \mathbb{R}^K_+$ is a fixed reference price vector. Well-being is the minimum expenditure at prices $p$ to reach the same satisfaction as $x$. Linked to Samuelson (1974), Samuelson and Swamy (1974).

# Key objects

- **Nested Contour (Axiom 1):** The basic fairness requirement -- reconciles no-envy with respect for individual preferences. Equivalent to Unchanged Indifference Independence (Lemma 1).
- **Worst Preferences $R^w$:** Leontief preferences $x R^\ell x' \iff \min_k \frac{x_k}{\ell_k} \geq \min_k \frac{x'_k}{\ell_k}$. An agent unable to substitute between goods -- well-being determined by the most deprived dimension.
- **Best Preferences $R^b$:** Linear preferences $x R^p x' \iff \sum p_k x_k \geq \sum p_k x'_k$. An agent with maximal ability to substitute between goods -- all goods equally valuable at the margin (up to prices).
- **Lattice structure of indifference curves ($\mathcal{I}$):** The space of indifference curves forms a lattice with $\leq$ and $\ll$ orderings. Supremum Nested Contour and Infimum Nested Contour are dual, corresponding to chains in this lattice (Theorem 3).

# Data

No data. Purely theoretical.

# Identification logic

Not applicable (axiomatic theory).

# Estimation / empirical strategy

Not applicable.

# Treatment of preferences

Preferences are the central object. They are ordinal, heterogeneous, continuous, convex, and monotonic. The key insight: well-being measurement requires interpersonal comparisons, but the paper constructs these from ordinal preferences alone, without cardinal utility. The two families differ in which preferences serve as the reference:
- Ray utility uses **worst preferences** (Leontief) as the reference -- well-being is anchored at the inability to substitute.
- Money-metric utility uses **best preferences** (linear) as the reference -- well-being is anchored at the maximal ability to substitute.

The paper explicitly does not address preference heterogeneity arising from needs or abilities -- only heterogeneity in tastes over goods.

# Treatment of opportunities / constraints

No explicit treatment of opportunities or constraints. The consumption set is $\mathbb{R}^K_+$ for all agents. The paper focuses on measuring well-being at a given bundle, not on how agents arrived at that bundle. Budget sets appear only in the definition of money-metric utility (as the budget set at reference prices $p$).

# Welfare / normative object

Individual well-being measures $W(x, R)$, not social welfare functions. The paper explicitly separates measurement from aggregation. However, the conclusion notes that when combined with egalitarian (maximin) aggregation:
- Ray utility + maximin $\to$ egalitarian equivalence allocation rule (Pazner and Schmeidler 1978)
- Money-metric utility + maximin $\to$ equal-income Walrasian allocation rule (Kolm 1968, Varian 1974)

# Main findings

1. **Lemma 1:** Nested Contour $\iff$ Unchanged Indifference Independence. Well-being depends only on the indifference curve, not on the specific preferences generating it.

2. **Theorem 1 (Ray Utility):** A well-being measure $W$ satisfies Supremum Nested Contour if and only if it satisfies Nested Contour and Worst Preferences. Moreover:
$$W(x, R) = \max_{x' \in L(x, R)} W(x', R^w)$$
Well-being is measured by the worst-preferences value of the highest bundle on the lower contour set. Once $R^w$ is Leontief with ray $\ell$, this yields the ray utility $W^\ell$.

3. **Theorem 2 (Money-Metric Utility):** A well-being measure $W$ satisfies Infimum Nested Contour if and only if it satisfies Nested Contour and Best Preferences. Moreover:
$$W(x, R) = \min_{x' \in U(x, R)} W(x', R^b)$$
Well-being is measured by the best-preferences value of the lowest bundle on the upper contour set. Once $R^b$ is linear with prices $p$, this yields the money-metric utility $W^p$.

4. **Theorem 3 (Lattice Duality):** If $W$ satisfies Supremum Nested Contour, there exists a chain $C$ in $(\mathcal{I}, \leq)$ such that $W(J) = \max_{J' \in C, J \neq J'} W(J')$. The dual holds for Infimum Nested Contour with $\ll$ replacing $\leq$.

5. **Incompatibility:** Supremum Nested Contour and Infimum Nested Contour cannot both be satisfied simultaneously (they strengthen Nested Contour in incompatible directions). This explains why ray utility and money-metric utility are two distinct families of well-being measures.

6. **Connection to fair allocation:** The paper's two families correspond to the two prominent allocation rules in fair allocation theory: egalitarian equivalence (ray utility) and equal-income Walrasian (money-metric utility). The axiomatic justification for well-being measures provides a "dual justification" for these allocation rules.

# Main limitations

- The setting is abstract ($K$ divisible goods, $\mathbb{R}^K_+$ consumption set) with no labour supply, time allocation, or institutional constraints.
- The paper does not address heterogeneous needs or abilities -- only heterogeneous tastes over goods.
- The choice of the reference ray $\ell$ (for ray utility) or reference prices $p$ (for money-metric utility) is left unresolved. The axioms justify the functional form but not the specific reference parameters.
- No aggregation: the paper does not say which family is "better" for social welfare evaluation -- it only shows that each has an axiomatic foundation.
- The duality result (Theorem 3) is elegant but does not help choose between the two families.

# Relevance for my JMP

## possible use for the axiomatic foundation of money-metric utility
The paper provides the most rigorous axiomatic justification for money-metric utility as a well-being measure. In my RURO welfare analysis, I use equivalent income (a form of money-metric utility) to measure individual well-being. This paper shows that money-metric utility is uniquely justified by a specific strengthening of the basic fairness axiom (Infimum Nested Contour + Best Preferences). This is stronger than simply citing "it's what Fleurbaey and Maniquet use" -- it shows the measure is axiomatically forced.

## possible use for understanding the two competing families
The duality between ray utility (worst preferences / Leontief / egalitarian equivalence) and money-metric utility (best preferences / linear / equal-income Walrasian) clarifies the normative commitments implicit in the choice of well-being measure. In my framework, using equivalent income (money-metric) implicitly adopts the "best preferences" perspective -- well-being is anchored at the ability to substitute, not at the inability to do so. This has implications for how my welfare criterion treats agents with very different substitution possibilities (e.g., agents who can easily switch between hours levels vs. those who cannot).

# Research questions this paper inspires

1. In the labour-consumption model underlying my JMP, what are the "worst preferences" and "best preferences"? If leisure and consumption are the two goods, Leontief preferences imply no substitution between leisure and consumption (agents want a fixed ratio), while linear preferences imply perfect substitution. How does the choice between ray utility and money-metric utility affect the welfare ranking of agents who differ in their willingness to trade leisure for consumption?

2. The paper leaves the reference parameters ($\ell$ or $p$) unresolved. In the equivalent income framework, the reference wage $\tilde{w}$ plays the role of the reference price. Does the axiomatic framework help justify a particular choice of $\tilde{w}$?

# Challenge to this paper

The paper assumes a common consumption set $X = \mathbb{R}^K_+$ for all agents. In labour supply models, agents face heterogeneous budget sets (due to different wages, tax schedules, and -- in the RURO framework -- different opportunity sets $A_i$). The well-being measure $W(x, R)$ is defined at a given bundle $x$, abstracting from how $x$ was chosen. But when opportunity sets vary, two agents at the same bundle $x$ with the same preferences $R$ but different opportunity sets $A_i \neq A_j$ may have different well-being (because one could have chosen better alternatives). The paper's framework cannot capture this opportunity-sensitive notion of well-being, which is central to the RURO approach. The paper's Axiom 2 (Unchanged Indifference Independence) explicitly requires that well-being depend only on the indifference curve at $x$, not on preferences over infeasible bundles -- but in a world with heterogeneous opportunity sets, the "feasible" vs "infeasible" distinction varies across agents.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The money-metric utility $W^p(x, R)$ is the direct analogue of equivalent income $m_i(\tilde{w}, z_i)$ in my framework. The reference price vector $p$ corresponds to the reference wage $\tilde{w}$ (in a two-good leisure-consumption model, the price of leisure is the wage). The paper provides the axiomatic foundation for this construction.

[Reasonable inference for my project] The "best preferences" in my two-good model would be linear preferences over consumption and leisure -- agents who are indifferent between working and not working at any wage. These preferences represent the maximal ability to substitute between leisure and consumption. The money-metric utility measures well-being relative to these best preferences, which means it evaluates agents by what they could achieve if they were maximally flexible in their labour-leisure choices.

[Unclear from paper] Whether the axioms extend to settings with heterogeneous opportunity sets. The RURO model's key feature -- that agents face different feasible sets $A_i$ determined by the opportunity density $g(h, w)$ -- is outside the scope of this paper's framework. If well-being should also reflect opportunity set differences, a richer axiomatic framework is needed.

# Relation to Bargain et al. (2013)

Indirect connection. Bargain et al. (2013) use equivalent income (a money-metric utility measure) with maximin aggregation. This paper provides the axiomatic foundation for why money-metric utility is a defensible well-being measure, justifying the first step in Bargain et al.'s procedure. The paper also shows that combining money-metric utility with egalitarian aggregation corresponds to the equal-income Walrasian allocation rule, which is distinct from the egalitarian equivalence rule that Fleurbaey & Maniquet's optimal taxation results typically favour.

# Relation to opportunities vs preferences

The paper is exclusively about preferences -- it does not address opportunities. Well-being $W(x, R)$ depends on the bundle consumed and preferences, not on the opportunity set from which the bundle was chosen. The paper's Nested Contour axiom compares agents solely through the geometry of their indifference curves. This is a limitation from the RURO perspective: two agents with the same $(x, R)$ but vastly different opportunity sets would have the same measured well-being, even though one may have been severely constrained while the other chose freely from a rich menu.

# Useful quotations / formulas

**On the two families and their duality (p. 125):**
"One family is consistent with the idea that comparing well-being requires to determine worst preferences. [...] The other family is consistent with the idea that comparing well-being requires to determine best preferences."

**On worst preferences being Leontief (p. 122):**
"An agent with Leontief preferences is unable to substitute one good for another. When such an agent consumes bundle $x$, her well-being is entirely determined by $\min_{k \in K} \frac{x_k}{\ell_k}$, that is, the good in which this agent feels most deprived."

**On best preferences being linear (p. 123):**
"An agent with linear preferences has the highest ability to substitute one good for another. All goods are equally valuable, whatever the proportion in which they come, as soon as we weight them with the $p_k$ parameters."

**On the connection to fair allocation (p. 125):**
"The axiomatic justification we give to these two families [is] dual to each other. One family is consistent with the idea [of] worst preferences [...]. The other family is consistent with the idea [of] best preferences."

**Ray utility definition (p. 122):**
$$W^\ell(x, R) = w \iff x \, I \, w\ell$$

**Money-metric utility definition (p. 123):**
$$W^p(x, R) = w \iff x \, I \, \max(R, \{x' \in X \mid px' \leq w\})$$

# Suggested tags

well-being-measurement, money-metric-utility, ray-utility, fairness, axiomatic, indifference-curves, nested-contour, worst-preferences, best-preferences, Leontief, linear-preferences, egalitarian-equivalence, equal-income-Walrasian, Fleurbaey, Maniquet, Samuelson, Pazner, Deaton

# My quick takeaway

A foundational paper showing that two natural but incompatible strengthenings of a basic fairness axiom (Nested Contour) uniquely justify two families of well-being measures: ray utility (anchored at worst/Leontief preferences) and money-metric utility (anchored at best/linear preferences). For my JMP, this provides the deepest axiomatic foundation for using equivalent income as the welfare measure: it is the money-metric utility justified by the "best preferences" strengthening. The key limitation is that the framework does not accommodate heterogeneous opportunity sets, which is central to the RURO approach.
