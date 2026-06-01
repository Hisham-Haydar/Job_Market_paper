---

title: "Social orderings for the assignment of indivisible objects"
authors: ["François Maniquet"]
year: 2008
outlet: "Journal of Economic Theory"
country_or_context: "General theoretical model of assignment of indivisible objects with money"
population: "Agents competing for indivisible objects, each consuming at most one object, with monetary compensations"
data_period: ""
shelf: "fairness_social_orderings_indivisible_objects"
tags: ["indivisible objects", "social ordering functions", "money utility", "leximin", "independence of infeasible bundles", "consistency", "fairness axioms", "assignment with money", "social choice", "egalitarian equivalence"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Maniquet, François. 2008. “Social orderings for the assignment of indivisible objects.” *Journal of Economic Theory* 143: 199–215. 

# One-sentence contribution

The paper characterizes the unique social ordering function for the assignment of indivisible objects with money that satisfies efficiency, independence of preferences over infeasible bundles, consistency, and equity axioms: the leximin ordering in money utility. 

# Why this paper matters

This paper matters because it is directly about how to rank feasible allocations when the planner cannot necessarily implement first-best assignments. Instead of studying allocation rules only, it studies complete social ordering functions, precisely to handle incentive constraints, status quo restrictions, and other feasibility limitations. That is a major methodological move. 

For your project, the paper is especially important because it isolates one axiom that is very close in spirit to your concern with infeasible opportunities: social rankings should be independent of changes in preferences over infeasible bundles. The paper does not speak in your (W(z,R,A;y)) notation, but it is one of the clearest formal results showing how a “feasibility-sensitive” informational restriction can drive the form of the social objective. 

# Core research question

Which social ordering functions for assignment problems with indivisible objects and money can simultaneously satisfy efficiency, consistency, an independence requirement with respect to infeasible bundles, and basic equity principles? 

# Economic setting and context

The setting is the assignment of desirable indivisible objects with monetary compensation. Each agent may consume at most one object, and some agents may receive no object but only money. The motivating examples on page 1 include apartments, concert seats, parking lots, and tasks on a board of directors. The introduction also gives a university housing example in which visitors may be assigned campus housing or compensated for not receiving one. 

The paper’s broader context is the contrast between allocation rules and social ordering functions. Maniquet argues that allocation rules are often insufficient when information and incentive constraints prevent the planner from reaching first-best alternatives. A complete social ordering allows the planner to maximize social desirability over whatever feasible set is actually reachable. This is the core conceptual motivation on pages 1–3. 

# Model / theoretical framework

The model is a normative social-choice framework for assignment with indivisible objects and money. An economy is (E=(N,A,R)), where (N) is a finite set of agents, (A) a finite set of indivisible objects, and (R=(R_i)_{i\in N}) a profile of preferences over object-money bundles on (A^* \times \mathbb{R}), where (A^*=A\cup{\nu}) and (\nu) is the null object. Agents can consume at most one object. Preferences are continuous, strictly monotone in money, all objects are desirable, and each object has finite money value for each agent. Section 2 defines the model formally. 

A feasible allocation assigns to each agent either one available object or the null object, plus a monetary transfer, with no real object assigned twice and with aggregate transfers summing to at most zero. Social ordering functions rank all feasible allocations for each economy. This is explicitly a complete ranking framework, not merely a selection rule. 

The framework is explicitly normative. It is not a positive model of choice behavior. It does not estimate preferences or explain how allocations arise in actual markets. Instead, it asks what social ranking of feasible allocations is justified by a set of axioms. 

The feasible set is central. The paper’s independence axiom requires that changes in preferences over bundles containing unavailable objects not affect the social ranking. This is the key informational restriction and is the reason the paper is unusually relevant for your project. 

# Key objects

The most important object is the social ordering function (R), which assigns to each economy a complete, reflexive, and transitive ranking of feasible allocations. This is the paper’s target object. 

The second key object is the money equivalent or money utility of a bundle. For any preference (R_i) and bundle (z_i), the money utility (u(R_i,z_i)) is the amount of money (m) such that the agent is indifferent between (z_i) and ((\nu,m)). This object emerges as the crucial sufficient representation once independence over infeasible bundles, consistency, and Pareto indifference are imposed. Pages 6–9 are central here. 

The third key object is the money-equivalent leximin ordering. It ranks feasible allocations by lexicographically comparing the ordered vector of agents’ money equivalents. Definition 1 on page 11 gives the formal definition. 

# Data

There is no empirical dataset. The paper is purely theoretical and axiomatic. The examples are illustrative only. 

# Identification logic

This is not an econometric identification paper. The relevant “identification” logic is axiomatic. The paper asks which social ordering functions are singled out by a given set of normative and informational requirements. 

The crucial analytical step is the intermediary characterization in Lemma 1 and Lemma 2: Pareto Indifference, Independence of Preferences over Infeasible Bundles, and Consistency imply the Money Equivalent Property, and this is equivalent to a form of money-utility welfarism. In other words, once those axioms are imposed, the social ranking can depend only on each agent’s money equivalent of the assigned bundle. This is the paper’s first major result. 

A second identification step comes from fairness. Strong Pareto, the Money Equivalent Property, and the Transfer Principle among Equals yield a maximin property in money equivalents (Lemma 4), while adding Anonymity among Equals and Consistency upgrades this to leximin (Lemma 5). Thus the final theorem is an axiomatic characterization, not a parametric or statistical identification result. 

# Estimation / empirical strategy

There is no estimation. The method is theorem-based axiomatic analysis. Section 3 derives the money-equivalent restriction from independence and consistency; Section 4 adds fairness axioms and proves the leximin characterization. 

# Treatment of preferences

Preferences are ordinal over object-money bundles and may vary freely across agents, subject to continuity, strict monotonicity in money, desirability of objects, and finite object values. The paper does not estimate preferences and does not impose quasi-linearity. In fact, the conclusion explicitly notes that if one restricted the domain to quasi-linear preferences, the maximin conclusion would fail and more general generalized utilitarian criteria would survive. This is an important point on pages 15–16. 

The paper treats preferences normatively but indirectly. They matter through money equivalents, not via raw utilities or direct interpersonal utility comparisons. This is one of the paper’s main conceptual moves: the social ordering ends up aggregating money utility rather than arbitrary utility representations. 

# Treatment of opportunities / constraints

This section is crucial for your project. The paper does not model opportunity sets in the labour-market sense, but it does treat feasibility in a highly explicit way. The feasible set consists of allocations using only available objects and balanced money transfers. The central independence axiom says that preferences over infeasible bundles must not affect social rankings. This is not just a side condition; it is a core organizing principle of the analysis. 

The paper is therefore unusually strong on the treatment of infeasibility. It distinguishes feasible from infeasible bundles sharply and insists that only preferences over feasible bundles should matter for social evaluation. This is conceptually close to your concern with feasible-set dependence, even though the domain is assignment with money rather than jobs, abilities, and earnings. [reasonable inference for my project] supported by 

At the same time, the paper does not distinguish preference heterogeneity from opportunity heterogeneity in your sense. The feasible set is common at the economy level, not person-specific in the way (A_i) would be in a jobs-and-wellbeing model, and the paper does not decompose disadvantage into preferences versus opportunities. It is therefore a paper about social ranking under feasibility, not about heterogeneous opportunity sets across persons. 

# Welfare / normative object

The paper is explicitly normative. Its object is a social ordering over feasible allocations. The final result is that the only such ordering satisfying the stated axioms is the money-equivalent leximin function. 

This is not a welfare measure of the (W(z,R,A;y)) form, but it is closely related to your project in spirit because it derives a social objective from axioms rather than assuming utilitarian aggregation. The paper also makes a strong anti-utilitarian point: in this domain, the axioms force the use of money utility and, with the fairness axioms added, force infinite aversion to money-utility inequality via leximin. 

The paper is useful for responsibility for opportunities only indirectly. It does not discuss responsibility, compensation, or reference opportunity sets explicitly. But it does show that the treatment of infeasible bundles can strongly constrain admissible social orderings. [reasonable inference for my project] supported by 

It does not provide a decomposition of inequality into opportunities and preferences. It is a characterization paper, not a decomposition paper. 

# Main findings

The first main finding is the intermediary characterization: Pareto Indifference, Independence of Preferences over Infeasible Bundles, and Consistency imply the Money Equivalent Property. Equivalently, they imply money-utility welfarism. This means the social ranking can depend only on agents’ money equivalents of their assigned bundles. Lemma 1 and Lemma 2 on pages 6–9 are the key result. 

The second main finding is that fairness selects leximin, not just any money-utility aggregation rule. Strong Pareto, the Money Equivalent Property, and the Transfer Principle among Equals imply a money-equivalent maximin property (Lemma 4, pages 11–12). Adding Anonymity among Equals and Consistency sharpens this into full money-equivalent leximin (Lemma 5, pages 13–14). 

The third and main result is Theorem 1 on page 14: a social ordering function satisfies Strong Pareto, Independence of Preferences over Infeasible Bundles, Consistency, the Transfer Principle among Equals, and Anonymity among Equals if and only if it is the money-equivalent leximin function. This is the core theorem of the paper. 

A further conceptual finding in the conclusion is that the result depends on domain richness. In particular, if preferences were restricted to be quasi-linear, the maximin conclusion would fail and generalized utilitarian social welfare functions would satisfy the axioms. This qualification is important for interpretation. 

# Main limitations

The first limitation for your project is that the model is not about individual-specific feasible job sets. Feasibility enters as the set of available allocations in an assignment problem, not as heterogeneous (A_i)-type opportunity sets. This limits direct portability to your jobs-and-wellbeing framework. 

A second limitation is that the paper is purely axiomatic and static. It does not provide an empirical strategy for recovering money equivalents or for implementing the social ordering in observed data. This is a theoretical contribution, not a positive or empirical one. 

A third limitation is that the result depends on strong domain richness. The paper itself notes that if preferences are restricted, for example to quasi-linear preferences, the characterization changes materially. So the leximin conclusion is not domain-free. 

A fourth limitation is that the fairness axioms operate on equals in preferences and object-money tradeoffs, not on explicit opportunity disadvantage. Thus while infeasibility matters, the paper does not directly address responsibility for unequal feasible sets across individuals. [reasonable inference for my project] supported by 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing because it shows that an explicit restriction on how infeasible bundles may matter can have powerful implications for the form of the welfare criterion. It supports the broader idea that feasibility should not be treated as an afterthought in welfare analysis. 

## possible use for model design

Direct use for positive model design is limited. There is no structural labour-supply or RURO component. Indirectly, it is useful because it suggests that once one defines a feasible-set-sensitive evaluative domain carefully, strong characterization results may follow. [reasonable inference for my project] supported by 

## possible use for identification

There is no empirical identification strategy, but there is a strong axiomatic identification of the admissible social ordering. For your project, this is useful as an example of how informational restrictions on preferences over infeasible bundles can be built directly into the normative framework. [reasonable inference for my project] supported by 

## possible use for welfare measurement

It is highly useful normatively, but not as a direct welfare measure for your context. It shows how to derive a social objective from fairness and feasibility axioms and how money-equivalent comparisons can replace arbitrary utility aggregation. 

## possible use for decomposition

Directly, very limited. The paper does not decompose welfare or inequality into preferences, opportunities, and other components. Indirectly, it suggests that some informational decompositions may be possible once one distinguishes feasible from infeasible preference information. [reasonable inference for my project] supported by 

## possible use for comparative application

Not central. The paper is not comparative across countries or groups. Its portability lies in the formal logic, not in an empirical comparative application. 

# Research questions this paper inspires

Can a version of Independence of Preferences over Infeasible Bundles be formulated for a jobs-and-wellbeing framework where individuals have person-specific feasible job sets (A_i)?

If such an axiom is imposed in a (W(z,R,A;y)) model, does it force well-being to depend only on preferences restricted to (F(A)), the feasible bundle set?

Is there an analogue of money-equivalent leximin when the relevant outside option is not the null object plus money, but a reference opportunity set or a common reference job menu?

How much of the Maniquet characterization survives if infeasible bundles are person-specific rather than economy-wide?

Can one derive a fairness-based social ordering over realized job allocations that is independent of preferences over infeasible jobs but still sensitive to unequal feasible sets?

# Challenge to this paper

The sharpest challenge, from your perspective, is that the paper uses infeasibility only as an informational restriction, not as a morally relevant source of disadvantage. It says that preferences over infeasible bundles should not matter for social ranking, but it does not ask whether the fact that some bundles are infeasible for some agents is itself a fairness issue requiring compensation. In your project, that second question is central. [reasonable inference for my project] supported by 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper is about social orderings over feasible allocations of indivisible objects with money, and its central axiom requires independence from preferences over infeasible bundles. It therefore directly engages with feasibility-sensitive information, albeit in a different domain from labour supply. 

[reasonable inference for my project] This is highly relevant to a framework (W(z,R,A;y)) because your model also needs to distinguish what preferences matter when some bundles or jobs are infeasible. In particular, Maniquet’s axiom is conceptually close to your concern that preferences over infeasible jobs should not contaminate welfare evaluation or identification. 

[explicit in paper] The paper does not define an individual well-being measure (W(z,R,A;y)), does not study labour supply, and does not introduce person-specific opportunity sets (A_i). The feasible set is defined at the economy-allocation level, not at the individual opportunity-set level. 

[reasonable inference for my project] In your taxonomy, the paper is closest to the theme of IPIJ-like restrictions, that is, constraints on the relevance of preferences over infeasible bundles. It is much less related to IIJ, independence of (y), laissez-faire evaluation, or reference opportunity sets. It is also not a decomposition paper. Its main value is as a formal precedent for feasibility-sensitive axiomatization. 

[unclear from paper] Whether the money-equivalent leximin logic can be extended from common-feasibility assignment problems to person-specific feasible job sets is not addressed. 

# Relation to Bargain et al. (2013)

[not central].

# Relation to opportunities vs preferences

This paper is not about opportunity heterogeneity in the empirical sense, but it is deeply about the normative role of feasibility. It says that only preferences over feasible bundles should matter, and that this informational discipline sharply restricts admissible social orderings. 

That makes it quite relevant to your opportunities-versus-preferences agenda at a formal level. It does not separate heterogeneous opportunities from heterogeneous preferences empirically, but it does show that once feasibility is treated seriously, preferences cannot be used indiscriminately in welfare judgments. For your project, that is a valuable conceptual precedent. 

# Useful quotations / formulas

The formal money utility object is
[
u(R_i,z_i)=m \iff z_i I_i (\nu,m),
]
introduced in Section 3. This is the key representation result because all admissible social orderings end up depending on this object only. 

Definition 1 gives the final characterization:
[
z,R^L(E),z' \iff m^* \text{ lex } m^{*'},
]
where (m^*_i) and (m_i^{*'}) are the money equivalents of each assigned bundle. This is the money-equivalent leximin ordering. 

Theorem 1 on page 14 is the main theorem: Strong Pareto, Independence of Preferences over Infeasible Bundles, Consistency, Transfer Principle among Equals, and Anonymity among Equals characterize the money-equivalent leximin function. 

# Suggested tags

indivisible-objects, social-ordering-functions, infeasible-bundles, money-equivalent, money-utility, leximin, consistency, transfer-principle, anonymity, feasibility-sensitive-welfare

# My quick takeaway

This is a very important paper for the axiomatic side of your project. It is not about jobs, labour supply, or heterogeneous feasible job sets, but it is one of the clearest formal results showing how a restriction on the relevance of preferences over infeasible bundles can determine the admissible social objective. The paper’s main lesson for your JMP is that feasibility-sensitive normative analysis can be both rigorous and sharply characterizing. Its closest value for you is as a formal building block for thinking about how preferences over infeasible jobs should, or should not, enter a jobs-and-wellbeing framework.
