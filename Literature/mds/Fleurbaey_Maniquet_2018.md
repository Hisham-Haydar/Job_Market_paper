---

title: "Inequality-averse well-being measurement"
authors: ["Marc Fleurbaey", "François Maniquet"]
year: 2018
outlet: "International Journal of Economic Theory"
country_or_context: "Theoretical / axiomatic welfare economics"
population: "Agents consuming divisible goods under heterogeneous preferences"
data_period: "[not applicable]"
shelf: "axiomatic_wellbeing_measurement_inequality_aversion"
tags: ["well-being measurement", "inequality aversion", "fairness", "ray utility", "money-metric utility", "axiomatic welfare economics", "heterogeneous preferences", "transfer principles"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Fleurbaey, Marc, and François Maniquet. 2018. “Inequality-averse well-being measurement.” *International Journal of Economic Theory* 14(1): 35–50. 

# One-sentence contribution

The paper refines the broad fairness-based families of well-being measures developed in earlier work by adding inequality-aversion or transfer principles, and shows that these stronger principles select strictly concave transformations of either money-metric utility or ray utility. 

# Why this paper matters

This paper matters because it moves from **general families** of admissible well-being measures to **specific benchmark measures**. In Fleurbaey and Maniquet’s earlier framework, fairness axioms based on indifference-set comparisons identified two broad classes of measures; here the authors ask whether one can further discipline those classes by requiring a form of inequality aversion in well-being increments. Their answer is sharp: the additional principles select money-metric and ray-utility forms, up to strictly concave transformation. 

For your project, this is highly relevant on the welfare-measurement side. It does not introduce actual feasible job sets or labor-market opportunities, but it shows how fairness plus transfer principles can pin down specific measures once one accepts a resource-based informational basis with heterogeneous preferences. This is directly useful if you need to justify why a particular measure is normatively better grounded than an arbitrary reference-based index. 

# Core research question

Given a framework in which individual situations are described by commodity bundles and ordinal preferences, can one impose inequality-aversion principles strong enough to refine the two general fairness-compatible families of well-being measures and characterize specific measures such as ray utility and money-metric utility? 

# Economic setting and context

The paper is fully theoretical. Its context is welfare economics and fair allocation under heterogeneous preferences. The opening section explicitly states that the paper builds on Fleurbaey and Maniquet (2011, 2017a), where fairness principles made it possible to compare individuals in terms of bundles and preferences rather than interpersonally comparable utilities. The present paper asks how far this approach can be refined once one adds transfer-style inequality aversion. 

The paper is also positioned against two neighboring traditions. On one side is the Kaldor–Hicks–Scitovsky compensation literature, which uses bundles and ordinal preferences but for a different evaluative purpose. On the other side is Suzumura’s extended-sympathy approach, which allows richer interpersonal judgements than the authors’ parsimonious informational basis. The authors explicitly choose the more parsimonious framework. 

# Model / theoretical framework

The model class is an axiomatic well-being measurement model over divisible goods. There are (K) goods, the consumption set is
[
X=\mathbb{R}_+^K,
]
and preferences are continuous, convex, and monotonic. A well-being measure is a function
[
W:X\times \mathcal R \to \mathbb R,
]
where (W(x,R)) is the well-being of an agent consuming bundle (x) with preferences (R). The paper also imposes continuity of (W) in (x) and respect for preferences, so that preference orderings are preserved by the well-being measure within each individual. 

The framework is normative. It is explicitly about how to measure individual well-being so that it can later serve as an argument of social welfare functions, but the aggregation step is left outside the paper. This separation between individual well-being measurement and social aggregation is one of the paper’s central methodological choices. 

The key inherited structure from the earlier paper is the pair of fairness axioms called **supremum nested contour** and **infimum nested contour**. These axioms compare situations by the relative positions of lower and upper contour sets, and they generate two broad families of well-being measures. The current paper then adds new transfer principles: **nested priority**, **diminishing priority**, and **weak diminishing priority**. The diagrams on pages 39–44 are integral to the argument: Figures 1 and 2 restate the two basic families; Figures 3–5 explain why one transfer principle is too strong and how it must be weakened; Figures 6 and 7 illustrate money-metric and ray-utility forms; Figures 8–11 visualize the impossibility and characterization proofs. 

The agent does not choose from an explicit menu in the model. The object of evaluation is the realized commodity bundle (x) together with preferences (R). There is no explicit feasible-set object, no labor-market opportunity set, and no pay schedule. 

# Key objects

The core objects are the bundle (x), the preference relation (R), and the well-being measure (W(x,R)). Lower, upper, and indifference contours (L(x,R)), (U(x,R)), and (I(x,R)) remain the geometric basis of all interpersonal comparisons. 

A second key object is the pair of general families inherited from the earlier paper. Under **supremum nested contour**, well-being takes the form
[
W(x,R)=\max_{x'\in L(x,R)} W(x',R^w),
]
for some “worst preferences” (R^w). Under **infimum nested contour**, it takes the dual form
[
W(x,R)=\min_{x'\in U(x,R)} W(x',R^b),
]
for some “best preferences” (R^b). These are recalled in Lemmas 1 and 2. 

A third key object is the new transfer structure. **Nested priority** attempts to compare well-being increments directly from bundle transfers toward the worse-off. **Diminishing priority** weakens this by requiring the relevant indifference-set shifts to be exact upward translations. **Weak diminishing priority** weakens it further by restricting the transfer direction to one specific vector. These refinements drive all the new results. 

The two specific benchmark measures selected by the final theorems are money-metric utility
[
W_p(x,R)=w \iff x I \max{R \text{ on } {x'\in X\mid p\cdot x' \le w}},
]
and ray utility
[
W_\ell(x,R)=w \iff x I w\ell,
]
with each measure only identified up to strictly concave transformation. Figures 6 and 7 on pages 43–44 give the geometric illustrations. 

# Data

[not applicable]. The paper is entirely theoretical and contains no dataset, no empirical sample, and no estimation exercise. 

# Identification logic

This is not an econometric identification paper. The relevant logic is axiomatic selection of admissible well-being measures. The authors start from the two broad classes already justified in earlier work and then ask which additional transfer principles are compatible with them. 

The decisive insight is that some seemingly natural transfer requirements are too strong. Lemma 3 proves that no well-being measure can satisfy both **nested priority** and **nested contour**. The intuition, explained in the text around Figures 3 and 4, is that there is a conflict between comparing bundle increments and comparing indifference-set geometry. This impossibility is one of the paper’s main theoretical contributions because it shows that not every intuitive inequality-aversion principle is compatible with fairness-respecting well-being measurement. 

Once the transfer principle is weakened appropriately, the theory becomes selective. Combining **infimum nested contour** with **diminishing priority** yields money-metric utility up to a strictly concave transform; combining **supremum nested contour** with **weak diminishing priority** yields ray utility up to a strictly concave transform. So the paper “identifies” these specific measures by narrowing the admissible classes with inequality-aversion axioms. 

# Estimation / empirical strategy

[not applicable]. The method is theorem-proof analysis plus geometric construction. The paper uses diagrams heavily to explain both the impossibility result and the characterization results. The figures on pages 39–45 are not decorative; they are part of the argument structure. 

# Treatment of preferences

Preferences are heterogeneous and central. The informational basis of welfare judgement is explicitly limited to commodity bundles and ordinal, non-comparable preferences. The authors insist that fairness principles make interpersonal comparison possible without needing interpersonally comparable utilities. 

The well-being measure must respect preferences, meaning that within a given preference ordering, higher-ranked bundles must receive weakly higher well-being. Beyond this, the comparison across different preference orderings is mediated by fairness axioms on indifference sets and transfer principles, rather than by direct utility comparison. 

The two characterization results pin down special classes of reference preferences. Under the money-metric side, the relevant best preferences must be **linear**. Under the ray-utility side, the relevant worst preferences must be **Leontief**. This is a substantive refinement relative to the earlier paper, where broader families were still admissible. 

# Treatment of opportunities / constraints

This is a major limit for your project. The paper does not model opportunities or constraints as feasible job sets, restricted menus, wages, hours offers, or labor-demand-side rationing. There is no object analogous to your (A). The entire framework is built on realized bundles in a common commodity space. 

The only “constraint” concept in the paper is the geometry of indifference sets and translated bundle increments. So the paper is not about opportunity heterogeneity; it is about how to compare well-being across heterogeneous preferences while remaining resource-based and fairness-sensitive. 

That said, the paper is useful for your project because it shows how fairness plus transfer principles can discipline the form of a well-being measure. In a richer jobs-and-wellbeing setting, one might try to ask whether analogous transfer principles over opportunity sets or opportunity-adjusted bundles can similarly select specific measures. This is a reasonable extension, but it is not in the paper. [reasonable inference for my project] supported by 

# Welfare / normative object

The welfare object is an **individual well-being measure** intended to serve as an argument in social welfare functions. The paper does not aggregate well-being, but it explicitly frames its results as providing better-grounded individual arguments for later social evaluation. 

Normatively, the paper is about combining two values: respect for individual preferences and inequality aversion in the evaluation of resource improvements. The central question is which individual well-being measures can support an egalitarian transfer logic while still respecting preferences and the contour-based fairness principles introduced previously. 

This is therefore a directly fairness-based welfare-measurement paper. But it is not about responsibility, effort, or unequal opportunities in the equality-of-opportunity sense, and it is not about decomposing welfare inequality into source components. Its contribution lies at the level of selecting the individual metric, not decomposing or aggregating it. 

# Main findings

The first major finding is an impossibility result. **Nested priority**, the most direct multidimensional transfer principle, is incompatible with **nested contour**. Lemma 3 proves that no well-being measure can satisfy both. The text around Figures 3 and 4 explains that the conflict comes from trying to compare bundle differences while also insisting that only indifference sets matter. 

The second major finding is Theorem 1. A well-being measure satisfies **infimum nested contour** and **diminishing priority** if and only if there exist a reference price vector (p\in \operatorname{int}(S^{K-1})) and a strictly concave function (g:\mathbb{R}*+\to\mathbb{R}*+) such that
[
W=g\circ W_p.
]
So the only admissible measures in that branch are strictly concave transformations of money-metric utility. Figure 6 on page 43 illustrates the money-metric construction. 

The third major finding is another impossibility. **Diminishing priority** is too strong to be combined with **supremum nested contour**. Lemma 4 proves that no well-being measure satisfies both. Thus the ray-utility branch requires a weaker transfer principle than the money-metric branch. 

The fourth major finding is Theorem 2. A well-being measure satisfies **supremum nested contour** and **weak diminishing priority** if and only if there exist a reference bundle (\ell\in \operatorname{int}(X)) and a strictly concave function (g:\mathbb{R}*+\to\mathbb{R}*+) such that
[
W=g\circ W_\ell.
]
So the only admissible measures in that branch are strictly concave transformations of ray utility. Figure 7 on page 44 illustrates the ray-utility construction. 

The fifth major finding is comparative. The money-metric branch can be combined with a stronger inequality-aversion axiom than the ray-utility branch. The authors explicitly emphasize this asymmetry, and it is one of the most interesting normative conclusions of the paper. 

# Main limitations

The first limitation is the absence of explicit opportunity sets, needs, abilities, leisure bounds, or non-monotonic dimensions. The concluding section explicitly notes that the divisible-commodities model is not adapted to settings where one dimension is bounded, such as leisure or health, or where preferences are not monotonic in every good. 

A second limitation is that the paper still requires exogenously chosen references: a price vector (p) for money-metric utility or a reference bundle (\ell) for ray utility. The paper shows when those forms are justified, but not how the reference itself should always be selected. 

A third limitation is that the framework does not study social aggregation. The authors say explicitly that the well-being measures are intended as arguments of social welfare functions, but aggregation is outside the current analysis. So the paper solves only one layer of the welfare-economics problem. 

A fourth limitation, especially important for your project, is that the theory is silent on responsibility for opportunities, compensation for unequal feasible sets, and decomposition of disadvantage into preferences versus opportunities. The informational basis is too narrow for those questions. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing the claim that a well-being measure should not be chosen arbitrarily. It shows that once one combines fairness and inequality-aversion principles, one can sharply restrict the admissible measures. That is a strong argument against purely ad hoc use of money-metric or ray-type metrics. 

## possible use for model design

It is highly useful for the normative design of your (W)-measure. In particular, it suggests that if your model contains a resource-based realized bundle component, transfer principles may help select among candidate measures. The paper also warns that some natural transfer principles are incompatible with fairness-based contour principles, so the design space is more constrained than it first appears. 

## possible use for identification

Its relevance for identification is axiomatic, not empirical. It identifies admissible forms of (W) from fairness and inequality-aversion axioms. It does not identify them from data, but it does tell you what kind of measure may be theoretically defensible before you go to data. 

## possible use for welfare measurement

This is the strongest relevance margin. The paper is directly about selecting specific individual well-being measures. It is particularly useful if your project needs to explain why concave transformations of money-metric or ray utility are not arbitrary conveniences but the outcomes of explicit normative requirements. 

## possible use for decomposition

Directly limited. The paper does not decompose welfare into preferences, opportunities, and pay schedules. Indirectly, it is relevant because any such decomposition presupposes a choice of well-being metric, and this paper helps justify that metric. [reasonable inference for my project] supported by 

## possible use for comparative application

Direct comparative application is limited because the model is too abstract. But the results are potentially portable across policy settings whenever the relevant evaluation is resource-based and preferences are heterogeneous. 

# Research questions this paper inspires

Can an opportunity-sensitive well-being measure (W(z,R,A;y)) be selected by transfer principles analogous to diminishing priority, but defined over feasible sets or opportunity-adjusted bundles rather than over simple commodity bundles?

Why can stronger inequality aversion be combined with the money-metric branch but not with the ray-utility branch? Is there a deeper economic interpretation of this asymmetry once opportunities and labor-market structures are introduced?

Can one define a transfer principle for reference opportunity sets that plays the same role here as translated bundle transfers play for money-metric and ray-utility measures?

How should reference prices or reference bundles be selected when the goods include labor-market attributes such as hours, income, job security, and nonpecuniary amenities?

Can the impossibility behind nested priority be generalized to a jobs-and-wellbeing setting where the conflict is between bundle-based transfers and opportunity-set geometry?

# Challenge to this paper

The strongest challenge is that the paper’s elegance comes from a narrow domain. It delivers sharp characterization results because it works in a monotonic divisible-goods framework and treats only realized bundles and preferences. The moment one wants to incorporate bounded dimensions, non-monotonicity, actual opportunity sets, or labor-market institutions, the results no longer transfer directly. So the paper is powerful as a benchmark, but not yet as a complete theory for richer welfare problems. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper studies well-being measures of the form (W(x,R)), where (x) is the realized commodity bundle and (R) is the individual’s preference ordering. It is explicitly about refining such measures through inequality-aversion axioms. 

[reasonable inference for my project] This maps naturally onto the (z)- and (R)-components of your framework. The paper is therefore directly useful for the problem of how to measure well-being from a realized situation when preferences are heterogeneous. supported by 

[unclear from paper] There is no explicit analogue of the feasible job set (A), and no explicit analogue of the pay schedule (y) as a separate normative argument. The paper does not distinguish realized bundles from feasible sets or opportunity sets. 

[reasonable inference for my project] Relative to your taxonomy, the paper is closest to the normative selection of **reference-based individual well-being measures** under heterogeneous preferences. It is not a paper on independence of (A), responsibility for opportunities, or decomposition of inequality into opportunities and preferences. Its main contribution is to sharpen the (W(z,R,\cdot;\cdot)) side once (z) and (R) are taken as primitive. supported by 

# Relation to Bargain et al. (2013)

[not central].

# Relation to opportunities vs preferences

This paper is fundamentally on the **preferences-and-bundles** side, not on the **opportunities** side. It assumes the informational basis of welfare judgement consists of realized bundles and ordinal preferences. Opportunities as distinct feasible sets are absent. 

Its value for your opportunities-versus-preferences project is therefore indirect but important. It shows how much can be done normatively once one takes heterogeneous preferences seriously, and also how sharply transfer principles can discipline the metric. The missing step is to extend this logic to settings where unequal feasible opportunities, not just unequal realized bundles, matter normatively. [reasonable inference for my project] supported by 

# Useful quotations / formulas

The two central characterization formulas are:
[
W=g\circ W_p
]
under infimum nested contour and diminishing priority, and
[
W=g\circ W_\ell
]
under supremum nested contour and weak diminishing priority, where (g) is strictly concave. These are the paper’s sharpest results. 

The diagrams are genuinely useful here. Figure 5 on page 42 illustrates diminishing priority as a comparison of well-being gains under translated indifference-set shifts. Figure 6 on page 43 shows the money-metric construction. Figure 7 on page 44 shows the ray-utility construction. Figures 8–11 on pages 46–49 visually encode the impossibility and uniqueness arguments. 

# Suggested tags

inequality-averse-wellbeing, money-metric-utility, ray-utility, transfer-principles, diminishing-priority, nested-contour, axiomatic-fairness, heterogeneous-preferences

# My quick takeaway

This is a core paper for the welfare-measurement side of your project. It does not address actual opportunity sets, so it is not a direct solution to (W(z,R,A;y)). But it is extremely valuable because it shows how fairness plus inequality-aversion principles can refine broad admissible classes into very specific candidate measures—strictly concave transforms of money-metric utility or ray utility. For your JMP, it is one of the strongest sources for defending why a particular reference-based well-being metric might be normatively justified rather than chosen for convenience.
