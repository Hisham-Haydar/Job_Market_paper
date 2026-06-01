---

title: "Fairness and well-being measurement"
authors: ["Marc Fleurbaey", "François Maniquet"]
year: 2017
outlet: "Mathematical Social Sciences"
country_or_context: "Theoretical / axiomatic welfare economics"
population: "Agents consuming divisible goods under heterogeneous preferences"
data_period: "[not applicable]"
shelf: "axiomatic_wellbeing_measurement_fairness"
tags: ["well-being measurement", "fairness", "axiomatic welfare economics", "ray utility", "money-metric utility", "egalitarian equivalence", "equal income Walrasian", "heterogeneous preferences"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Fleurbaey, Marc, and François Maniquet. 2017. “Fairness and well-being measurement.” *Mathematical Social Sciences* 90: 119–126. 

# One-sentence contribution

The paper axiomatizes individual well-being measures under heterogeneous preferences and shows that two dual families emerge from fairness-based requirements: one centered on “worst preferences” and containing ray-utility type measures, and one centered on “best preferences” and containing money-metric type measures. 

# Why this paper matters

This paper matters because it isolates the **individual well-being measurement** problem from the separate question of social aggregation. That is analytically important. Much of the fair-allocation literature jointly determines both individual well-being and its aggregation, often leading to maximin-type social criteria. Here the authors ask a prior question: given heterogeneous preferences, how should one compare two individuals’ well-being on the basis of the bundles they consume? 

For your project, this is highly relevant. It does not provide a jobs-and-opportunities model, but it gives a sharp axiomatic foundation for two central benchmark families—ray utility and money-metric utility—and explicitly links them to fairness. This is close to the problem you face when asking what kind of (W)-measure can compare individuals with different preferences without collapsing everything into raw income or subjective utility. 

# Core research question

When agents have heterogeneous, continuous, convex, monotonic preferences over divisible goods, what fairness-based axioms can justify an interpersonal well-being measure defined from bundles of resources and preferences, and which families of measures survive those axioms? 

# Economic setting and context

The paper is fully theoretical. The context is welfare economics and fair allocation, especially the long-standing problem of how to compare individual well-being when agents do not share identical or quasi-linear preferences. The authors explicitly motivate the paper by noting that once one allows income effects and heterogeneous reactions to policy, it is no longer obvious how well-being should be measured. 

The paper positions itself relative to two literatures. First, the consumer-surplus / utility-calibration literature, especially Samuelson’s money-metric and ray-utility concepts. Second, the fair-allocation literature, especially egalitarian-equivalent and equal-income Walrasian ideas. The article’s contribution is to axiomatize the individual-measurement part separately from the social-aggregation part. 

# Model / theoretical framework

The model class is an axiomatic well-being measurement model on a standard divisible-goods consumption space. The consumption set is
[
X=\mathbb{R}_+^K,
]
and agents have continuous, convex, monotonic preferences (R) over (X). A well-being measure is a function
[
W:X\times \mathcal{R}\to \mathbb{R},
]
where (W(x,R)) is the well-being level of an agent consuming bundle (x) and having preferences (R). 

The framework is normative. It assumes that economic justice is about fair allocation of resources and then asks how individual well-being should be measured consistently with that idea. The paper does not study policy behavior, labor supply, or empirical identification. It studies axioms on interpersonal comparison. 

The agent “chooses” nothing inside the model. The paper starts from a realized bundle (x) and the agent’s preferences (R), and asks how this pair should be mapped into a cardinal well-being number. The feasible set is the whole nonnegative orthant (X), not an individual-specific opportunity set. Opportunities are therefore not modeled explicitly as menus or sets varying across persons. 

The central basic axiom is **Nested Contour**: if the upper contour set of one agent at her bundle does not intersect the lower contour set of another at hers, then the first must be assigned higher well-being. This is shown in Figure 1 and formalized in Section 2. The authors then study two stronger, dual axioms—**Supremum Nested Contour** and **Infimum Nested Contour**—which generate the two main families of well-being measures. Figures 2–5 on pages 122–123 visually illustrate these dual constructions. 

# Key objects

The main objects are the consumption bundle (x), the preference relation (R), and the well-being measure (W(x,R)). The lower, upper, and indifference contour sets (L(x,R)), (U(x,R)), and (I(x,R)) are central because the fairness axioms are stated in terms of geometric relations among these sets. 

A second key object is the notion of **worst preferences** (R^w). These are preferences such that, at any common bundle, the corresponding well-being is never above that of any other preferences. Under the strengthened axiom Supremum Nested Contour, well-being at ((x,R)) is represented by the maximal well-being along the lower contour of ((x,R)) evaluated with respect to (R^w). This family contains ray-utility type measures. 

A third key object is **best preferences** (R^b). These are preferences such that, at any common bundle, the corresponding well-being is never below that of any other preferences. Under Infimum Nested Contour, well-being at ((x,R)) is represented by the minimal well-being along the upper contour of ((x,R)) evaluated with respect to (R^b). This family contains money-metric type measures. 

The paper also introduces the lattice structure of the space of indifference curves, which makes the duality between the two families transparent. Section 5 is central here. 

# Data

[not applicable]. The paper is entirely theoretical and contains no dataset, no econometric model, and no empirical estimation. 

# Identification logic

This is not an econometric identification paper. The relevant logic is axiomatic characterization. The question is not how to recover primitive parameters from observed choices, but how fairness requirements restrict the admissible forms of an interpersonal well-being measure (W(x,R)). 

The basic discipline comes from Nested Contour, which the paper treats as a weak but essential consistency condition if one wants well-being comparisons to be based on resource bundles while still respecting preferences. Stronger discipline comes from either Supremum Nested Contour or Infimum Nested Contour, each of which implies comparability across all preferences through a reference class of worst or best preferences. 

Thus, the paper “identifies” two families of measures by fairness axioms. It does not identify a unique measure unless one further fixes the reference preferences, such as Leontief preferences for the ray-utility family or linear preferences for the money-metric family. 

# Estimation / empirical strategy

[not applicable]. The method is theorem-proof analysis. The paper proves equivalence results between axioms and families of well-being measures, then interprets the resulting families in relation to known concepts such as ray utility and money-metric utility. 

# Treatment of preferences

Preferences are central and explicitly heterogeneous. This is the entire point of the paper. The well-being measure must respect each agent’s own preferences in the sense that if (xRx'), then (W(x,R)\ge W(x',R)), with strict inequality under strict preference. This is the analogue of an individual-level Pareto consistency requirement. 

But the paper goes beyond within-person consistency. It asks how to compare well-being **across** different preference relations. The answer is not to collapse all preferences into a common utility scale. Instead, it uses geometric relations between indifference sets and then selects either worst-preference or best-preference benchmarks. This is an elegant way to preserve respect for heterogeneous preferences while still obtaining interpersonal comparability. 

Substantively, the two benchmark families have intuitive interpretations. Worst preferences are associated with strong complementarity and difficulty in substituting across goods; Leontief preferences are the canonical example. Best preferences are associated with strong substitutability; linear preferences are the canonical example. The paper explicitly emphasizes this interpretation. 

# Treatment of opportunities / constraints

This is the crucial limit for your project. The paper does **not** model opportunities or constraints as feasible job sets, random offers, hours restrictions, or demand-side rationing. There is no person-specific set (A_i). All agents are evaluated over the common consumption space (X=\mathbb{R}_+^K). 

Accordingly, the paper does not distinguish preference heterogeneity from opportunity heterogeneity. It distinguishes preferences only. The heterogeneity problem it solves is the interpersonal comparison problem created by different indifference maps over a common resource space. 

That said, the paper is still useful for your project because it shows how one can define fairness-based interpersonal comparisons once a relevant object of comparison has been chosen. If, in a richer model, the realized bundle (z) and feasible set (A) were both ethically relevant, one might try to extend a similar geometric logic to those richer objects. That step, however, is not in the paper. [reasonable inference for my project] supported by 

# Welfare / normative object

The paper is explicitly normative. Its welfare object is an **individual well-being measure** grounded in fair resource allocation under heterogeneous preferences. It is not a social welfare function, a policy-incidence measure, or a happiness index. The paper is careful to isolate the individual-measurement problem from the aggregation problem. 

The central normative claim is that if economic justice concerns fair allocation of resources, then interpersonal well-being comparisons should depend on comparisons of the bundles consumed by agents while remaining consistent with their preferences. The paper then shows that this idea supports two dual families of measures, rather than a single unique formula. 

This is highly relevant for fairness, but not directly for responsibility for opportunities or for decomposition of inequality into sources. The paper does not discuss responsibility, circumstances, effort, or compensation in the modern equality-of-opportunity sense. It also does not produce a welfare decomposition. 

# Main findings

The first main result is that the weak fairness property Nested Contour is equivalent to **Unchanged Indifference Independence**, meaning that the well-being of an agent at a given bundle depends only on the indifference set at that bundle, not on the rest of the preference ordering. This is Lemma 1 and is foundational for the rest of the analysis. 

The second main result is Theorem 1. Supremum Nested Contour is equivalent to Nested Contour plus the existence of worst preferences. It implies that for all ((x,R)),
[
W(x,R)=\max_{x'\in L(x,R)} W(x',R^w).
]
If the worst preferences are Leontief, the resulting family is ordinally equivalent to ray utility. Figure 2 on page 122 and Figure 3 on page 122 visually illustrate this construction. 

The third main result is Theorem 2. Infimum Nested Contour is equivalent to Nested Contour plus the existence of best preferences. It implies that for all ((x,R)),
[
W(x,R)=\min_{x'\in U(x,R)} W(x',R^b).
]
If the best preferences are linear, the resulting family is ordinally equivalent to money-metric utility. Figure 4 on page 123 and Figure 5 on page 123 illustrate this dual case. 

The fourth main result is conceptual: the duality between the two families is explained by the lattice structure of the space of indifference curves. Section 5 explicitly restates the results in this language and argues that this duality helps explain why both ray-type and money-metric-type solutions repeatedly appear in the literature on well-being measurement and fair allocation. 

The fifth main result is interpretive. The paper links the first family to egalitarian-equivalent reasoning and the second to equal-income Walrasian reasoning. This connects individual measurement to two major solution families in fair-allocation theory. 

# Main limitations

The main limitation is the absence of opportunities or person-specific feasible sets. The paper’s welfare measure depends only on a realized bundle and preferences over a common consumption space. This is too narrow for a framework in which actual job opportunities or feasible menus matter normatively. 

A second limitation is the very abstract goods space. The paper is not designed for labor supply, wages, hours, taxes, or multidimensional job attributes. It is therefore a foundational measurement paper, not an applied labor-economics welfare paper. 

A third limitation is that the axioms do not pick a unique measure unless one specifies the reference preferences. The choice of Leontief versus linear versus other benchmark classes remains ethically open. So the paper narrows the admissible families, but does not close the problem fully. 

A fourth limitation is that the paper explicitly brackets heterogeneity in needs and abilities. The conclusion notes that this remains to be addressed. For your purposes, this is substantial because many opportunity and fairness questions precisely concern unequal needs, abilities, and feasible sets. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing the well-being measurement problem under heterogeneous preferences. It supports the claim that one cannot simply read off welfare from income or from a common utility function once preferences differ; one needs a fairness-based interpersonal metric. 

## possible use for model design

It is highly useful on the normative side of model design. In particular, it suggests that if you want an individual well-being measure in a richer jobs-and-wellbeing framework, you may need to choose between benchmark structures analogous to “worst” and “best” preference references, or something extending them. [reasonable inference for my project] supported by 

## possible use for identification

Its relevance for identification is axiomatic rather than empirical. The paper tells you which fairness principles characterize certain well-being measures. It does not tell you how to estimate them from data, but it does tell you what structure a defensible (W)-measure might need. 

## possible use for welfare measurement

This is the strongest relevance margin. The paper is directly about individual well-being measurement and its fairness foundations. It is especially important if your project needs to justify why one well-being metric, rather than another, should be used when preferences differ. 

## possible use for decomposition

Directly limited. The paper does not decompose welfare or inequality into preferences, opportunities, or pay schedules. Indirectly, it is useful because it isolates one foundational component of any future decomposition: the metric used to compare persons once heterogeneous preferences are acknowledged. [reasonable inference for my project] supported by 

## possible use for comparative application

Direct empirical comparative use is limited. The paper is too abstract to be a ready-made cross-country or policy-comparison framework. Its comparative value is theoretical: it helps compare alternative welfare metrics rather than real-world populations. 

# Research questions this paper inspires

Can the duality between worst-preference and best-preference well-being measures be extended from common resource bundles (x) to a richer framework (W(z,R,A;y)) with feasible sets and pay schedules?

What is the analogue of Nested Contour when the ethically relevant object is not only the realized bundle but also the feasible opportunity set (A)?

Can a jobs-and-wellbeing measure combine ray-type and money-metric-type logic, for example by using one benchmark on the realized-bundle side and another on the opportunity-set side?

How should heterogeneity in needs, abilities, and feasible opportunities alter the axioms that justify interpersonal well-being comparisons?

Can one derive a fairness-based welfare metric for labor supply in which wages, hours, and job characteristics are bundled while preferences remain heterogeneous?

# Challenge to this paper

The main challenge is that the paper solves a clean but narrow problem. It provides an elegant axiomatic theory of interpersonal well-being measurement across heterogeneous preferences, but only over a common divisible-goods space. The real difficulty in many modern applications, including yours, is not only preference heterogeneity but also heterogeneity in opportunities, needs, and feasible sets. On that broader problem, the paper is suggestive rather than sufficient. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper constructs a well-being measure (W(x,R)) from a realized bundle (x) and a preference relation (R), under the normative idea that fair allocation of resources should ground interpersonal comparisons. It explicitly studies families related to ray utility and money-metric utility. 

[reasonable inference for my project] A partial mapping into your framework is immediate: your (z) plays the role of the realized bundle, and (R) plays the same role here as in the paper. The paper therefore speaks directly to the (z)- and (R)-side of (W(z,R,A;y)). supported by 

[unclear from paper] There is no analogue of your feasible job set (A), and no analogue of your pay schedule (y) as a separate argument. The paper does not discuss actual opportunities, wages, job menus, or reference opportunity sets. 

[reasonable inference for my project] Relative to your taxonomy, the paper is closest to **reference-based well-being measurement under heterogeneous preferences**, not to responsibility for opportunities or independence of (A). It is especially useful if your draft needs a rigorous bridge between ray-type and money-metric-type candidate measures, but it will need major extension before it can handle actual opportunity sets or the axioms you are studying for jobs and well-being. supported by 

# Relation to Bargain et al. (2013)

[not central].

# Relation to opportunities vs preferences

This paper is entirely on the **preferences** side of that distinction. It tackles the interpersonal-comparison problem generated by heterogeneous preferences and asks how one can compare well-being without pretending preferences are identical. 

It does not tackle **opportunities** in the sense of unequal feasible sets. So it should not be read as a paper on opportunities versus preferences. Rather, it is a paper on how to construct a fairness-respecting welfare metric once preferences are heterogeneous and resources are the relevant ethical object. [reasonable inference for my project] supported by 

# Useful quotations / formulas

The paper’s two core representation formulas are:
[
W(x,R)=\max_{x'\in L(x,R)} W(x',R^w)
]
for the worst-preferences family, and
[
W(x,R)=\min_{x'\in U(x,R)} W(x',R^b)
]
for the best-preferences family. These are the sharpest summary of the duality proved in Theorems 1 and 2. 

Figure 3 on page 122 is especially useful: it visually shows the ray-utility logic, where well-being is measured by the bundle on a fixed ray that leaves the agent indifferent to her actual bundle. Figure 5 on page 123 does the same for the money-metric logic, using a fixed price vector and expenditure equivalence. 

# Suggested tags

axiomatic-wellbeing, fairness-based-measurement, ray-utility, money-metric-utility, worst-preferences, best-preferences, heterogeneous-preferences, fair-allocation-foundations

# My quick takeaway

This is a core theoretical paper for the welfare-measurement side of your project. It does not speak to actual opportunity sets, jobs, or wages, so it is not a direct solution to (W(z,R,A;y)). But it gives a very clean axiomatic explanation of why ray-type and money-metric-type well-being measures keep reappearing in fairness theory, and it provides a rigorous foundation for comparing people with heterogeneous preferences on the basis of the bundles they consume.
