---
title: "Well-being measurement with non-classical goods"
authors: [Marc Fleurbaey, Francois Maniquet]
year: 2019
outlet: "Economic Theory, 68, 765--786"
country_or_context: "Theoretical (abstract consumption model)"
population: "N/A (abstract social choice model)"
data_period: "N/A (theoretical)"
shelf: "well-being measurement / money-metric utility / ray utility / non-classical goods / satiation / ordinal goods / fairness / axiomatic"
tags: [well-being-measurement, money-metric-utility, ray-utility, non-classical-goods, ordinal-goods, satiation, monotone-consumption-path, fairness, axiomatic, Fleurbaey, Maniquet, nested-contour, labour-supply, health, leisure]
priority: "medium"
read_status: "extracted"
---

# Full citation

Fleurbaey, M., & Maniquet, F. (2019). Well-being measurement with non-classical goods. *Economic Theory*, 68, 765--786.

# One-sentence contribution

Extends the axiomatic well-being measurement framework of Fleurbaey and Maniquet (2017, 2018) to settings where goods may be ordinal (non-cardinal quantities), subject to satiation (not always desirable), or both, showing that the two basic axioms (Supremum and Infimum Nested Contour) remain compatible and jointly characterise "monotone consumption path" well-being measures, while in the satiation model a new family based on the "preferred attribute" emerges.

# Why this paper matters

This is the most directly relevant of the three Fleurbaey-Maniquet well-being measurement papers for labour supply applications, because it explicitly addresses goods that are not always desirable (hours of work / leisure have natural satiation points) and goods that are ordinal (job quality, health). The paper shows that the classical results -- ray utility and money-metric utility -- rely on assumptions (cardinality, monotonicity) that fail for labour supply. When these assumptions are relaxed, new well-being measures emerge, and the paper characterises them. This directly bears on the choice of well-being measure in labour-consumption models.

# Core research question

Do the axiomatic results characterising ray utility and money-metric utility (from Fleurbaey and Maniquet 2017, 2018) generalise to settings where goods are ordinal (quantities not cardinally comparable) or subject to satiation (not always desirable)? If not, what alternative well-being measures are justified?

# Economic setting and context

Three models of increasing generality:

1. **Classical model** (Section 2): $K$ divisible goods, $X = \mathbb{R}^K_+$, preferences continuous, convex, monotonic. Same as Fleurbaey and Maniquet (2017, 2018). Two families: ray utility ($W^\ell$) and money-metric utility ($W^p$).

2. **Ordinal desirable goods** (Section 3): Goods are desirable (monotonic preferences) but purely ordinal -- quantity differences are not meaningful, convex combinations of quantities are not meaningful. Example: housing quality, car quality. Consumption set $X = \mathbb{R}^K_+$, preference domain $\mathcal{R}^{od}$ (all monotonic continuous preferences). The two axioms become compatible and characterise a single family.

3. **Satiation model** (Section 4): Goods take values in a compact set $A \subset \mathbb{R}^{K-1}_+$ (attributes: hours, health, location), plus one classical good $m \in \mathbb{R}_+$ (income/money) that is always desirable. Preferences $\mathcal{R}^s$ are continuous, monotonic in $m$, but not necessarily monotonic in attributes. No attribute can be infinitely preferred over another.

4. **General case** (Section 5): Combines classical goods with non-classical goods. Consumption set $X \times A$. Four families of well-being measures from combining the two dimensions.

# Model / theoretical framework

**Two basic axioms (same as 2017):**

**Axiom 1 -- Supremum Nested Contour:** If $L(x, R) \subset \text{interior}[L(x', R') \cup L(x'', R'')]$, then $W(x, R) < \max\{W(x', R'), W(x'', R'')\}$.

**Axiom 2 -- Infimum Nested Contour:** If $U(x, R) \subset \text{interior}[CH(U(x', R') \cup U(x'', R''))]$, then $W(x, R) > \min\{W(x', R'), W(x'', R'')\}$.

In the classical model, these are incompatible (they characterise different families). But when goods are ordinal, they become compatible.

**Key new concept -- Monotone Consumption Path:**
$P \subset \mathbb{R}^K_+$ is a monotone consumption path if:
- $0^K \in P$
- For all $x, x' \in P$: either $x \ll x'$ or $x' \ll x$ or $x = x'$
- $P$ is homeomorphic to $\mathbb{R}_+$
- For all $r \in \mathbb{R}^K_+$, there exists $x \in P$ such that $r \ll x$

Rays are special cases. The key difference from the classical case: when goods are ordinal, the path need not be a ray (because scaling quantities is not meaningful).

**Theorem 1 (Ordinal model -- one axiom):** $W$ satisfies Supremum Nested Contour and Infimum Nested Contour* if and only if there exists a monotone consumption path $P$ and a strictly increasing $w: P \to \mathbb{R}_+$ such that $W(x, R) = w(p)$ for $p \in P$ with $x \, I \, p$.

**Theorem 2 (Ordinal model -- both axioms):** $W$ satisfies both Supremum Nested Contour and Infimum Nested Contour* if and only if the same characterisation holds with a monotone consumption path.

**Satiation model -- new well-being measure:**

$W^{\tilde{a}}(x, R)$: Fix a reference attribute $\tilde{a} \in A$. Well-being $= w$ if $(m, a) \, I \, (w, \tilde{a})$. Measures well-being by the income needed at the reference attribute to be indifferent.

**Axiom 5 -- Equal Well-Being at Preferred Attribute:** If two agents consume at their preferred attribute ($a \in a_{\max}(x, R)$ and $a \in a_{\max}(x, R')$), they have the same well-being: $W((x, a), R) = W((x, a), R')$.

**Theorem 3 (Satiation model):** $W$ satisfies Supremum Nested Contour and Infimum Nested Contour* if and only if there exists a fixed $\tilde{a} \in A$ and a strictly increasing $f$ such that $W(x, R) = f(W^{\tilde{a}}(x, R))$.

**Theorem 4 (Preferred attribute):** $W$ satisfies Equal Well-Being at Preferred Attribute if and only if $W$ is ordinally equivalent to $W^{a_{\max}}$: $W^{a_{\max}}(x, R) = w \iff (x, a) \, I \, (w, a_{\max}(w\ell, R))$.

**General case (Section 5) -- four combined measures:**
1. $W^{\ell \tilde{a}}$: ray utility $\times$ fixed attribute
2. $W^{\ell a_{\max}}$: ray utility $\times$ preferred attribute
3. $W^{p \tilde{a}}$: money-metric $\times$ fixed attribute
4. $W^{p a_{\max}}$: money-metric $\times$ preferred attribute

# Key objects

- **Monotone consumption path $P$:** Generalisation of a ray to ordinal goods. The indifference curve's intersection with $P$ gives well-being.
- **Fixed reference attribute $\tilde{a}$:** Analogue of reference prices/ray for the non-classical dimension. Well-being measured at the reference attribute.
- **Preferred attribute $a_{\max}(m, R)$:** The attribute(s) that agent $R$ considers optimal when consuming income $m$. Well-being measured at the agent's own preferred attribute.
- **$W^{a_{\max}}$:** Well-being at preferred attribute. Does not require fixing a common reference attribute -- each agent is evaluated at their own optimal attribute.

# Data

No data. Purely theoretical.

# Identification logic

Not applicable (axiomatic theory).

# Estimation / empirical strategy

Not applicable.

# Treatment of preferences

Preferences are ordinal, heterogeneous, and the sole subjective information used. The paper explicitly notes: "no a priori information on subjective utility, welfare or happiness was considered relevant. Our approach is thus consistent with the view of justice as fairness" (p. 784). The key extension: preferences over non-classical goods may exhibit satiation (agents prefer intermediate levels of attributes like hours of work or health), which is directly relevant for labour supply.

# Treatment of opportunities / constraints

No treatment. The paper focuses on well-being at given bundles, not on how bundles are chosen or constrained. The conclusion explicitly notes that "whether goods are private or public, whether they are tradable or not, whether their consumption exhibits congestion or exclusion phenomena, is unrelated to the way well-being has to be measured. These aspects need to enter the description of the allocation problem as feasibility constraints and not as relevant variables at the stage of the definition of well-being" (p. 785).

# Welfare / normative object

Individual well-being measures $W(x, R)$. The paper shows that "the aggregation of well-being levels can be operated using any kind of aggregator, from the utilitarian one to the leximin one" (p. 785) -- the choice of aggregator is separate from the choice of well-being measure.

# Main findings

1. **Classical results recalled:** In the classical model (cardinal, monotonic), Supremum Nested Contour and Infimum Nested Contour are incompatible and characterise two separate families: ray utility (worst preferences = Leontief) and money-metric utility (best preferences = linear).

2. **Theorem 1 (Ordinal + one axiom):** With ordinal goods, Supremum Nested Contour and Infimum Nested Contour* (weakened) are each sufficient to characterise monotone consumption path well-being measures.

3. **Theorem 2 (Ordinal + both axioms):** With ordinal goods, the two axioms become compatible and jointly characterise the same family -- monotone consumption path measures. The incompatibility from the classical model vanishes because convex combinations of quantities are no longer meaningful.

4. **Theorem 3 (Satiation + fixed attribute):** With satiation, Supremum Nested Contour + Infimum Nested Contour* uniquely characterise (up to increasing transformation) the fixed-attribute well-being measure $W^{\tilde{a}}$: well-being = income needed at reference attribute $\tilde{a}$ to achieve current satisfaction.

5. **Theorem 4 (Satiation + preferred attribute):** Equal Well-Being at Preferred Attribute characterises $W^{a_{\max}}$: well-being = income needed at agent's own preferred attribute to achieve current satisfaction. This avoids choosing a reference attribute but depends on individual preferences in a different way.

6. **General case:** Four well-being measures from combining classical (ray or money-metric) with non-classical (fixed or preferred attribute) dimensions. All four can be combined with any aggregator.

7. **Compatibility result:** The key surprise -- when goods are ordinal or subject to satiation, the two axioms that are incompatible in the classical model become compatible, dramatically narrowing the family of well-being measures.

# Main limitations

- The satiation model's "one classical good + attributes" structure maps imperfectly onto labour supply models where both consumption and leisure are goods with specific properties.
- The preferred-attribute measure $W^{a_{\max}}$ depends on the agent's most-preferred attribute, which may be hard to observe or estimate.
- The paper does not address how opportunity constraints affect well-being.
- The fixed-attribute reference $\tilde{a}$ is left unresolved -- the axioms characterise the family but not the specific reference.
- Proofs are abstract and do not provide direct guidance for empirical implementation.

# Relevance for my JMP

## possible use for labour supply as a non-classical good
This paper directly addresses the theoretical issue that hours of work (or leisure) is a "non-classical good" -- agents have preferred hours levels, more hours is not always better, and the quantity may be ordinal or subject to satiation. The classical ray utility and money-metric utility results (from 2017, 2018) assume all goods are desirable and cardinal, which fails for labour supply. This paper shows what well-being measures remain justified when these assumptions are relaxed. In my two-good (consumption, leisure) model, consumption is classical but leisure is subject to satiation (agents have preferred leisure levels), making the satiation model (Section 4) directly applicable.

## possible use for the fixed vs preferred attribute distinction
The distinction between $W^{\tilde{a}}$ (fixed reference attribute) and $W^{a_{\max}}$ (preferred attribute) maps onto the choice of reference wage in equivalent income. Using a fixed reference wage $\tilde{w}$ corresponds to $W^{\tilde{a}}$. An alternative approach -- evaluating each agent at their own preferred hours level -- would correspond to $W^{a_{\max}}$. The paper shows both are axiomatically justified but by different axioms.

## possible use for combining classical and non-classical dimensions
The general case (Section 5) shows how to combine money-metric utility for classical goods (consumption) with the attribute-based measures for non-classical goods (hours/leisure). The four resulting measures provide a principled menu for my welfare analysis.

# Research questions this paper inspires

1. In my labour-consumption model, does leisure qualify as a "satiation good" (bounded, with preferred level) or as an "ordinal good" (quality of time use)? The answer determines which theorem applies and which well-being measures are justified.

2. The preferred-attribute measure $W^{a_{\max}}$ evaluates agents at their own preferred hours. In the RURO framework, the preferred hours may be infeasible due to limited job offers. How should $W^{a_{\max}}$ be interpreted when the agent cannot achieve their preferred attribute due to demand-side constraints?

3. The four combined measures (Section 5) provide a systematic menu. Which of the four best captures the RURO framework's concern with both preferences and opportunities?

# Challenge to this paper

The paper's key finding -- that Supremum Nested Contour and Infimum Nested Contour become compatible for non-classical goods -- is theoretically elegant but may be problematic for labour supply. In the labour-consumption model, consumption is classical (always desirable, cardinal) while leisure is non-classical (satiation). The general case (Section 5) combines the two but does so by treating each dimension independently. This assumes separability in the well-being measure between the classical and non-classical dimensions, which may conflict with the non-separability of preferences over consumption and leisure that is empirically well-documented and central to structural labour supply models.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] The satiation model with $x = (m, a)$ where $m$ = income/consumption and $a$ = attributes (potentially including hours) maps directly onto the labour-consumption framework. The well-being measure $W^{\tilde{a}}((m, a), R) = w$ where $(m, a) \, I \, (w, \tilde{a})$ is equivalent to equivalent income with reference hours $\tilde{a}$ (or equivalently, reference wage $\tilde{w}$).

[Reasonable inference for my project] The measure $W^{a_{\max}}$ -- evaluating agents at their own preferred hours -- would correspond to an equivalent income concept where each agent is evaluated at the hours level they would freely choose. In the RURO framework, this preferred hours level may differ from actual hours due to demand-side constraints, and the gap between actual and preferred hours is informative about the welfare cost of opportunity restrictions.

[Unclear from paper] How the axioms interact with heterogeneous opportunity sets. The paper defines well-being at given bundles, abstracting from how bundles are chosen. But in RURO, the same bundle may reflect free choice (from a rich opportunity set) or constrained choice (from a limited one), and welfare should arguably differ.

# Relation to Bargain et al. (2013)

Indirect. Bargain et al. use equivalent income, which corresponds to $W^{p\tilde{a}}$ (money-metric for consumption, fixed reference for hours/wage) in the general case of this paper. This paper provides the axiomatic foundation for that specific combination and shows it is one of four justified alternatives. It also shows that the "preferred attribute" alternative ($W^{pa_{\max}}$) -- evaluating at agents' own preferred hours -- is another option that Bargain et al. do not consider.

# Relation to opportunities vs preferences

The paper explicitly states that opportunity constraints are not part of well-being measurement: "These aspects need to enter the description of the allocation problem as feasibility constraints and not as relevant variables at the stage of the definition of well-being" (p. 785). This is a strong position that my RURO framework challenges: if two agents have identical bundles and preferences but vastly different opportunity sets, my framework would assign different well-being levels (reflecting the different values of the opportunity sets), while this paper would assign the same well-being.

# Useful quotations / formulas

**On non-classical goods (p. 766-767):**
"We relax these two assumptions here. In a first model, we assume that goods are ordinal [...]. In a second model, we assume that goods are not necessarily desirable, that is, more is not always better."

**On satiation examples (p. 775):**
"Typical examples are health, for which we may see perfect health as a natural upper bound, hours of work, theater tickets, etc."

**Monotone consumption path well-being (Theorem 2, p. 774):**
"A well-being measure $W$ satisfies Supremum Nested Contour and Infimum Nested Contour* if and only if there exists a monotone consumption path $P$ and a strictly increasing function $w: P \to \mathbb{R}_+$ such that for all $x \in \mathbb{R}^K_+$, all $R \in \mathcal{R}$, $W(x, R) = w(p)$ for $p \in P$ such that $x \, I \, p$."

**Fixed attribute well-being (Theorem 3, p. 775):**
"$W^{\tilde{a}}((x, a), R) = w$ if and only if $(m, a) \, I \, (w, \tilde{a})$."

**On separating measurement from aggregation (p. 785):**
"The aggregation of well-being levels can be operated using any kind of aggregator, from the utilitarian one to the leximin one. Any degree of inequality aversion is acceptable."

**On the relationship between feasibility and well-being (p. 785):**
"Whether goods are private or public, whether they are tradable or not, whether their consumption exhibits congestion or exclusion phenomena, is unrelated to the way well-being has to be measured."

# Suggested tags

well-being-measurement, money-metric-utility, ray-utility, non-classical-goods, ordinal-goods, satiation, monotone-consumption-path, fairness, axiomatic, Fleurbaey, Maniquet, nested-contour, labour-supply, health, leisure, preferred-attribute, fixed-attribute

# My quick takeaway

The most relevant of the three Fleurbaey-Maniquet well-being measurement papers for my JMP because it addresses non-classical goods (satiation, ordinality) -- exactly the features of hours of work/leisure. Key results: (1) when goods are ordinal or subject to satiation, the two competing axioms from the classical model become compatible, narrowing the field; (2) in the satiation model, a new "preferred attribute" well-being measure emerges alongside the fixed-attribute measure; (3) combining classical and non-classical dimensions yields four families. The paper provides axiomatics for the equivalent income measure in labour-consumption settings, but explicitly excludes opportunity constraints from well-being measurement -- a position my RURO framework challenges.
