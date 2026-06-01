---

title: "Fair Income Tax"
authors: ["Marc Fleurbaey", "François Maniquet"]
year: 2006
outlet: "The Review of Economic Studies"
country_or_context: "General normative optimal-tax model; no single empirical country application, though the paper includes an illustrative U.S. reform figure"
population: "Agents with heterogeneous skills and heterogeneous preferences over consumption and leisure"
data_period: ""
shelf: "fairness_optimal_tax_axiomatic"
tags: ["optimal income tax", "fairness", "equivalent wage", "maximin", "heterogeneous preferences", "unequal skills", "incentive compatibility", "non-welfarist welfare economics", "working poor"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Fleurbaey, Marc, and François Maniquet. 2006. “Fair Income Tax.” *The Review of Economic Studies* 73(1): 55–83. 

# One-sentence contribution

The paper derives a non-welfarist criterion for optimal income taxation in a model with heterogeneous skills and heterogeneous consumption-leisure preferences, and shows that fair taxation should minimize the greatest average tax rate on low incomes, implying maximal subsidies for the hardworking poor.

# Why this paper matters

This paper matters because it is one of the clearest attempts to derive the objective of optimal taxation from explicit fairness principles rather than from an assumed utilitarian social welfare function. Instead of taking interpersonal utility comparisons as primitive, it starts from axioms and derives a measure of individual advantage, the “equivalent wage,” together with a maximin social ordering.

For your project, this paper is especially important on the normative side. It is not a structural labour-supply estimation paper and it does not model opportunity sets in the RURO or latent-jobs sense. But it is highly relevant for thinking about responsibility versus compensation, about how preferences should matter in redistribution, and about how one can build a welfare criterion in a setting with both heterogeneous preferences and heterogeneous skills.

# Core research question

In a model with unequal earning abilities and heterogeneous preferences over consumption and leisure, what social preferences and what optimal income-tax rule can be justified from efficiency and fairness principles under incentive-compatibility constraints?

# Economic setting and context

The setting is an abstract optimal-tax model. Agents differ in two dimensions: skill, which determines earning ability, and preferences over consumption and leisure, which determine labour-supply choices. Income inequality therefore reflects both unequal productivities and heterogeneous willingness to work. 

The paper is not an empirical country study. Its context is the classical Mirrlees-type income-tax problem with unobservable skills, but reformulated in a fairness-based framework. The paper does include an illustrative figure based on a U.S. lone-parent budget set under welfare reform, but this is only an application of the comparison criterion, not a structural empirical analysis. Figure 13 on page 19 is the relevant illustration.

# Model / theoretical framework

The model is a normative optimal income-tax framework with incentive compatibility. Each agent consumes a bundle (z_i=(\ell_i,c_i)), where (\ell_i) is labour and (c_i) is consumption. Agents have continuous, convex, monotonic preferences (R_i) over consumption and leisure, and productivity (w_i), so pre-tax earnings are (y_i=w_i \ell_i). 

The government observes only earnings, not skills. Redistribution is therefore implemented through an income tax function (\tau(y)), and agents freely choose labour time from the budget set induced by (c \le y-\tau(y)). The paper works in the standard second-best mechanism-design environment where allocations must satisfy incentive-compatibility or self-selection constraints. 

The framework is explicitly normative. The key analytical step is the derivation of social preferences from axioms: a qualified Pigou-Dalton transfer principle, a laissez-faire principle for equal-skill economies, Weak Pareto, Hansson Independence, and Separability. These axioms imply a maximin ordering over a particular individual measure, the equivalent wage.

# Key objects

The main individual normative object is the equivalent wage
[
W_i(z_i)=\max{w\in \mathbb{R}_+ \mid \forall \ell,\ z_i\ R_i\ (\ell,w\ell)},
]
that is, the hypothetical wage rate that would allow agent (i) to attain the same indifference curve if she could choose labour freely at that wage. Theorem 1 and Figure 4 make this object central. 

The main social object is the maximin ordering applied to equivalent wages: among allocations in the relevant domain, society gives absolute priority to the worst-off in terms of (W_i(z_i)). This is the normative core of the paper.

The key tax-policy object is the income tax function (\tau(y)) and, more specifically, the maximal average tax rate on low incomes,
[
\max_{0<y\le w_m} \frac{\tau(y)}{y},
]
where (w_m) is the minimum skill in the population. This becomes the operational criterion for comparing tax schedules.

# Data

There is no estimation dataset and no empirical identification exercise. The paper is theoretical. The only empirical-looking element is the illustrative U.S. budget-set figure on page 19, used to show how the tax-comparison criterion can be applied.

# Identification logic

This is not an econometric identification paper. There is no attempt to identify preferences or skills from data. The main “identification” logic is axiomatic: fairness and efficiency principles are used to determine the appropriate social ordering and the corresponding individual welfare metric.

The paper then studies taxation under incentive compatibility. Given the model primitives and the fairness axioms, the key theorems characterize when one tax schedule is socially preferred to another. The crucial maintained assumptions for the tax results include self-selection constraints and the Low-Skill Diversity assumption, which ensures that among low incomes there are low-skill agents with locally similar preferences. This assumption is what makes the envelope over low incomes socially informative. 

So identification here is ethical and analytical, not empirical. [explicit in paper]

# Estimation / empirical strategy

There is no estimation. The paper uses theorem-based analysis. Section 3 derives social preferences from axioms. Section 4 studies tax redistribution under incentive constraints and derives comparative and optimality results for tax schedules.

# Treatment of preferences

Preferences matter centrally. Agents differ in their ordinal preferences over consumption and leisure, and the paper takes that heterogeneity seriously rather than collapsing everyone into a common utility function. This is one reason the usual utilitarian approach becomes problematic in the paper’s setup.

At the same time, the paper refuses to build the social objective by directly summing heterogeneous utilities. Instead, fairness principles induce the equivalent-wage metric. This is a way of respecting heterogeneous preferences while still obtaining an interpersonal welfare ordering.

A particularly important normative feature is the laissez-faire axiom in equal-skill economies. It encodes the idea that when individuals face the same earning ability, income differences generated by different preferences and labour choices should be respected. This is the paper’s main responsibility-sensitive ingredient regarding preferences.

# Treatment of opportunities / constraints

This is not a paper about explicit opportunity sets. It does not model jobs, offer distributions, latent opportunities, or feasible set heterogeneity in your (A)-type sense. Agents differ by skill and preferences, and choose labour continuously under a common tax schedule. 

The relevant constraints are budget constraints and incentive-compatibility constraints arising from unobservable skill. The budget set in labour-consumption space is (c \le y-\tau(y)), and in earnings-consumption space the same income schedule applies to everyone. This is therefore a budget-set and mechanism-design framework, not an opportunity-set framework. 

The paper clearly distinguishes preference heterogeneity from skill heterogeneity, but it does not distinguish preference heterogeneity from opportunity heterogeneity. It is useful for thinking about responsibility versus compensation for skills and labour choices, but not for actual opportunity sets, reference opportunity sets, or latent job availability. [reasonable inference for my project] supported by

# Welfare / normative object

The paper is explicitly normative. Its welfare object is not utility, EV/CV, or equivalent income in the standard consumption-only sense. It is the equivalent wage (W_i(z_i)), derived from fairness axioms. Social preferences then rank allocations by the minimum equivalent wage in the relevant domain, giving absolute priority to the worst-off.

This is directly relevant for responsibility and compensation. The Transfer Principle applies only between agents with identical preferences and identical labour time, which means the paper does not endorse equalization across arbitrary preference-driven outcomes. The laissez-faire axiom further says that when all skills are equal, redistribution should be absent, because income differences then reflect choices from a common budget set.

The paper therefore is useful for thinking about compensation for unequal earning abilities and respect for preference-driven labour choices. It is not useful for compensation for unequal opportunity sets as such, because those are not modeled. It also does not provide a decomposition of inequality into preferences, opportunities, and skills, though it does sharply distinguish skill and preference sources conceptually.

# Main findings

The central result is Theorem 1: the stated fairness axioms imply that social preferences give absolute priority to the worst-off when individual situations are measured by equivalent wage. This is the paper’s foundational normative result.

The main tax-comparison result is Theorem 2: one tax schedule is socially preferred to another if it has a lower greatest average tax rate over low incomes (y\in[0,w_m]), where (w_m) is the minimum skill. This turns the abstract maximin-over-equivalent-wage criterion into an operational tax test. Pages 17–18 and Figure 12 are central here. 

The main optimal-tax result is Theorem 3: the optimal tax can be found by maximizing the net income of the hardworking poor, (w_m-\tau(w_m)), under constraints implying that average tax rates on lower incomes are no higher, that the subsidy at (w_m) is maximal in absolute value, and that (\tau(0)\le 0). In substantive terms, the hardworking poor should receive the greatest subsidy in the population. Figure 14 on page 20 illustrates the admissible shape restriction.

The paper also concludes that average marginal tax rates on low incomes should be non-positive, so the results favour in-work subsidies or negative tax rates on low earnings rather than purely out-of-work redistribution.

# Main limitations

The first limitation, from your project’s perspective, is that opportunities are absent as an independent object. The model concerns skills, preferences, and incentive-compatible taxation, but not feasible job sets or labour-demand constraints. This limits direct portability to a (W(z,R,A;y)) framework where (A) is central. 

A second limitation is that the fairness axioms are strong and ethically selective. In particular, the laissez-faire principle assumes that when skills are equal, income differences from different preferences should be fully respected. That is a coherent moral stance, but not the only one. The paper itself notes that alternative ethical principles generate different social orderings.

A third limitation is that the operational tax results depend on the Low-Skill Diversity assumption. For large populations it is plausible, but it is still a richness assumption linking the preference distribution of low-skill agents to the whole envelope over low incomes. 

A fourth limitation is that there is no empirical implementation. The results are sharp, but they are not tied to an estimation strategy that would let one recover the required objects from data in actual labour markets. [reasonable inference for my project] supported by

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing the normative side of your JMP. It gives a rigorous example of how fairness principles can determine the welfare criterion, rather than taking a utilitarian welfare function for granted.

## possible use for model design

Direct use for positive model design is limited, because the paper has no structural job-choice or RURO component. Indirectly, it is useful because it shows how, once a positive environment is specified, one can build a fairness-based evaluative layer on top of it. [reasonable inference for my project] supported by

## possible use for identification

There is no empirical identification strategy here. The paper is instead useful for identifying which normative objects you may want to target empirically: a fairness-induced money-metric object rather than raw utility levels. [reasonable inference for my project] supported by

## possible use for welfare measurement

This is the paper’s strongest use for your JMP. It provides a non-welfarist but still preference-sensitive measure of individual advantage, the equivalent wage, and a maximin social ordering over it. This is directly relevant to the design of well-being measures under heterogeneous preferences.

## possible use for decomposition

It does not provide a formal decomposition of welfare inequality into preferences, skills, and opportunities. But it is useful for clarifying one normative separation: skill differences may justify redistribution, whereas pure preference differences from a common opportunity situation may not. [reasonable inference for my project] supported by

## possible use for comparative application

Direct comparative application is limited because there is no empirical cross-country design. The tax-comparison criterion itself is simple enough to be used in comparative discussion of low-income tax schedules, but the paper does not implement this. [reasonable inference for my project] supported by

# Research questions this paper inspires

Can one construct an analogue of equivalent wage for a framework (W(z,R,A;y)) in which feasible opportunity sets (A) matter intrinsically rather than only skills and preferences?

How would the Fleurbaey–Maniquet tax criterion change if unequal job opportunities, not just unequal skills, were treated as the relevant source of unjust inequality?

Can a fairness axiom stronger than laissez-faire for equal-skill economies be defended when agents face identical wages but unequal opportunity sets or social constraints?

Is there an opportunity-sensitive variant of the working-poor result in which maximal subsidy should go not to the hardworking poor defined by skill alone, but to those with the worst feasible opportunity sets conditional on effort?

Can the equivalent-wage approach be embedded in a structural labour-supply model with latent jobs, so that the normative object is empirically linked to estimated preferences and opportunity distributions?

# Challenge to this paper

The strongest challenge is that the paper’s fairness logic is powerful only because it abstracts from opportunity sets and labour-demand frictions. Once one allows that some low earnings reflect constrained opportunities rather than chosen leisure at a given skill, the laissez-faire axiom for equal-skill economies may become normatively too strong, and the working-poor criterion may no longer be sufficient. That is not an internal flaw of the paper; it is a boundary of its model. [reasonable inference for my project] supported by

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper studies redistribution in a model with heterogeneous skills and heterogeneous preferences over consumption and leisure, under incentive compatibility, and derives a welfare ordering based on equivalent wage. It is therefore directly about how to evaluate people when preferences differ, but it is not about job opportunities as such.

[reasonable inference for my project] In your notation, the paper is closest to a framework where well-being depends on realized bundle (z), preferences (R), and a wage/earnings environment, but not on an explicit feasible-set object (A). The realized bundle is present, preferences are central, and the pay dimension matters through skill and tax schedule, but feasible job opportunities are absent as an independent argument.

[explicit in paper] The paper’s ethical core is not independence of (A) or independence of (y), because those axioms are not discussed. Its explicit normative commitments are a qualified transfer principle, a laissez-faire principle for equal-skill economies, Pareto, informational parsimony, and separability.

[reasonable inference for my project] In your taxonomy, this paper is closest to responsibility for preferences or labour-choice differences conditional on equal skill, and compensation for unequal skill. It is not a paper on reference opportunity sets, not a laissez-faire measure in your exact sense, and not a decomposition of opportunities versus preferences. It is nevertheless highly relevant because it shows how a fairness-based welfare metric can be derived rather than assumed.

[unclear from paper] How the equivalent-wage approach should be modified when agents have different feasible job sets (A_i), or when equal skills do not imply equal opportunities, is not addressed. 

# Relation to Bargain et al. (2013)

This paper is relevant to Bargain-type work at the normative level rather than the empirical-structural one. Both are concerned with welfare evaluation under heterogeneous preferences and labour-supply choice, but Fleurbaey and Maniquet derive the social criterion from fairness axioms, whereas Bargain-type work typically begins from estimated behavioural models and then imposes a welfare metric. For your purposes, *Fair Income Tax* is the ethical benchmark, not the structural benchmark. [reasonable inference for my project]

# Relation to opportunities vs preferences

The paper is strong on preferences and weak on opportunities. It takes heterogeneous preferences very seriously and asks when preference-based labour choices should be respected. That is precisely the role of the laissez-faire axiom in equal-skill economies.

But it does not model unequal opportunities. In effect, it treats the morally relevant heterogeneity as skills plus preferences, under a common tax schedule. That makes it very useful for responsibility-versus-compensation questions in a skill-preference world, but incomplete for your opportunities-versus-preferences agenda.

# Useful quotations / formulas

The paper’s central welfare measure is the equivalent wage:
[
W_i(z_i)=\max{w\in \mathbb{R}_+ \mid \forall \ell,\ z_i\ R_i\ (\ell,w\ell)}.
]
This is the key object induced by the fairness axioms. 

The main tax-comparison criterion is:
[
\max_{0<y\le w_m}\frac{\tau(y)}{y}.
]
The lower this greatest average tax rate on low incomes, the better the tax schedule.

Theorem 3 implies that the optimal tax can be found by maximizing the net income of the hardworking poor,
[
w_m-\tau(w_m),
]
under shape constraints ensuring that lower incomes do not face a higher average tax rate than the hardworking poor and that subsidies are not lower below (w_m). Figure 14 on page 20 is the clearest visual summary. 

# Suggested tags

fair-income-tax, equivalent-wage, maximin, non-welfarist-optimal-tax, heterogeneous-preferences, unequal-skills, working-poor, responsibility-vs-compensation, fairness-axioms

# My quick takeaway

This is a core paper for the normative architecture of your JMP. It does not help with latent jobs or feasible job sets, but it is one of the strongest papers for deriving a welfare criterion in a labour-supply environment with heterogeneous preferences. Its main lesson is that once fairness axioms are taken seriously, one need not accept utilitarian social welfare as primitive: one can derive a specific interpersonal measure, equivalent wage, and then obtain sharp implications for tax design, especially the priority given to the hardworking poor. For your project, it is best used as a benchmark on how to derive the evaluative layer from principles, while recognizing that the (A)-dimension remains outside its model.
