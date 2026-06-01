---

title: "Decomposition procedures for distributional analysis: a unified framework based on the Shapley value"
authors: ["Anthony F. Shorrocks"]
year: 2013
outlet: "Journal of Economic Inequality"
country_or_context: "General methodological framework; no single-country empirical setting"
population: "[not applicable; methodological paper]"
data_period: "[not applicable]"
shelf: "decomposition_methods_distributional_analysis"
tags: ["decomposition", "Shapley value", "inequality", "poverty", "distributional analysis", "methodology", "welfare decomposition", "multivariate decomposition"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Shorrocks, Anthony F. 2013. “Decomposition procedures for distributional analysis: a unified framework based on the Shapley value.” *Journal of Economic Inequality* 11: 99–126. 

# One-sentence contribution

The paper provides a unified decomposition rule for poverty and inequality analysis by assigning to each factor its average marginal contribution across all possible elimination orders, yielding an exact additive decomposition formally equivalent to the Shapley value. 

# Why this paper matters

This paper matters primarily as a decomposition technology. It is not a structural labour-supply paper, not a RURO paper, and not a paper on well-being measures of the form (W(z,R,A;y)). Its value for your project is that it offers a rigorous, general way to allocate the contribution of interacting factors to an aggregate distributional statistic when conventional decompositions either fail, leave a residual term, or cannot handle multivariate structures. 

For your purposes, the most important point is that Shorrocks explicitly formulates decomposition as a general problem (I=f(X_1,\dots,X_m)), where (I) is an aggregate indicator and the (X_k) are contributory factors. That makes the paper potentially useful if, at a later stage, you define an inequality or welfare statistic built from objects related to preferences, opportunities, and pay schedules. This is an inference for your project, not something the paper itself does. 

# Core research question

How should one decompose an aggregate distributional indicator such as poverty or inequality into factor contributions in a way that is symmetric, exact, interpretable, and applicable to complex multivariate settings where standard procedures are inadequate? 

# Economic setting and context

The paper is a methodological contribution in distributional analysis rather than a substantive study of a particular labour market, country, policy reform, or household dataset. Its applications are analytical illustrations drawn from standard poverty and inequality decomposition problems, including growth versus redistribution, subgroup decompositions, inequality by income source, and hierarchical decompositions. 

The context is therefore the theory of measurement and attribution in inequality and poverty analysis. The paper is concerned with the shortcomings of conventional decomposition procedures: weak interpretation of factor contributions, restrictions on admissible indices, inability to handle multivariate or mixed decompositions, and the absence of a unified framework. 

# Model / theoretical framework

The model class is a general decomposition framework, not a behavioural model. Shorrocks starts from an aggregate indicator (I) that is completely determined by a set of contributory factors (X_k), written as (I=f(X_1,\dots,X_m)). He then defines (F(S)) as the value of the indicator when only the factors in subset (S) remain, with (F(\emptyset)=0). The decomposition problem is to assign contributions (C_k) to the factors so that they sum exactly to the observed aggregate. The proposed solution is the Shapley decomposition, which assigns to each factor its expected marginal contribution over all factor-elimination sequences. The general formulas are in Section 2, especially equations (2.1)–(2.9). 

There is no agent choosing from a feasible set, no explicit opportunity set, and no microeconomic decision problem. The paper does not model preferences, labour supply, jobs, wages, or tax-budget constraints except insofar as those may appear inside an analyst-chosen aggregate function (f). The framework is therefore methodological and descriptive-analytical rather than positive behavioural or explicitly normative in the social-choice sense. Some of the underlying poverty or inequality indices used in applications are normatively loaded, but the paper itself is about decomposition procedure rather than normative axioms of justice. 

# Key objects

The central objects are the aggregate indicator (I), the set of contributory factors (X_1,\dots,X_m), the subset-value function (F(S)), and the factor contributions (C_k). The key decomposition formula is the Shapley rule, where each factor’s contribution is the expectation of its marginal effect (kF(S)=F(S\cup{k})-F(S)) over all subsets (S) of the remaining factors. This appears in equations (2.8) and (2.9). 

A second important object is the hierarchical model (\langle K,A,F\rangle), where secondary factors are grouped into primary factors. This leads to the comparison between the direct Shapley decomposition and the two-stage Owen decomposition, and to propositions characterizing when aggregation consistency holds. 

The applications use standard distributional objects: poverty as (P(\mu,L)) with mean income and Lorenz curve, decomposable poverty indices, entropy inequality measures, the Gini coefficient, and inequality by source of income. These are not new welfare objects introduced by the paper, but illustrations of the general rule. 

# Data

The paper contains no original microdata, household survey, or country-specific estimation exercise. It is an analytical and methodological paper. The examples are formula-based applications to standard decomposition problems in poverty and inequality analysis. 

# Identification logic

There is no empirical identification strategy in the econometric sense. The paper does not identify causal effects from data, nor does it estimate behavioural parameters. The “identification” of contributions is entirely decomposition-theoretic: once the analyst specifies the aggregate indicator (I), the contributory factors (X_k), and the counterfactual rule that defines (F(S)) when factors are removed, the Shapley rule allocates contributions exactly and symmetrically. 

The crucial assumption is therefore not an exclusion restriction or exogenous variation, but the analyst’s definition of what it means to “eliminate” a factor. In this sense, the paper is powerful but conditional: the resulting contributions are only as meaningful as the underlying model (F) and the chosen factorization of the problem. This is a reasonable inference from the paper’s framework rather than a statement made in those words by the author. 

# Estimation / empirical strategy

There is no estimation. The strategy is axiomatic-formal and comparative. Shorrocks first defines desirable properties of a decomposition rule, then introduces the Shapley rule, and then shows through a sequence of applications that it either reproduces accepted practice or improves on it by removing residual terms and handling multivariate settings. Section 4 adds hierarchical structure and derives conditions under which Shapley and Owen decompositions coincide. 

# Treatment of preferences

Preferences are not modeled as an object of analysis. The paper does not distinguish tastes, utility functions, or preference heterogeneity as separate primitives. If preferences enter at all, they enter only indirectly through whatever aggregate poverty or inequality measure an outside analyst has chosen to decompose. 

This means the paper is not directly useful for estimating or interpreting heterogeneous preferences in labour-supply models. Its value for your work lies elsewhere: if you already have a model producing a welfare or inequality statistic that depends on preferences, then the Shapley method may help decompose that statistic. That connection is an inference for your project. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly. It has no concept analogous to a feasible job set (A), latent job offers, hours restrictions, or demand-side labour-market constraints. It also does not assume a universal choice set because it is not a choice model at all. 

Accordingly, the paper does not distinguish preference heterogeneity from opportunity heterogeneity on its own. It can only do so if the analyst has already built a framework in which these are defined as separate factors in an aggregate indicator. In that derivative sense, it can support decomposition of opportunities versus preferences, but only after the substantive modelling work has been done elsewhere. This is a reasonable inference for your project, not an explicit result of the paper. 

# Welfare / normative object

The paper does not propose an individual welfare measure and does not develop a theory of justice, compensation, or responsibility. Its immediate objects are aggregate poverty and inequality indicators and changes in those indicators. It is therefore best described as methodological and distributional, not as explicitly normative in the axiomatic social-choice sense you are working on. 

That said, some of the indicators to which the procedure is applied are normatively loaded, and the paper clearly recognizes that decomposition is often used to assess the importance of causal or explanatory factors in poverty and inequality. It is therefore positive with distributional applications rather than purely positive or purely normative. 

For your project, the main relevance is decomposition rather than welfare measurement proper. The paper does not address responsibility for opportunities, compensation for opportunities, or reference opportunity sets. It does, however, provide a generic way to decompose an inequality or welfare statistic once those concepts have already been operationalized in some other framework. This is an inference for your use, not something explicit in the paper. 

# Main findings

The main conceptual finding is that the Shapley value provides a unified decomposition rule that is symmetric, exact, and interpretable as an average marginal contribution across elimination paths. This solves the general decomposition problem posed in Section 2. 

In applications, the paper shows that the Shapley decomposition replicates conventional practice in several benchmark cases: decomposable poverty indices by subgroup, inequality decomposition by subgroup using the mean logarithmic deviation, and inequality decomposition by income source using the variance. In other settings, it improves on existing methods by eliminating residual or interaction terms, notably in the growth-versus-redistribution decomposition of poverty change and in Gini decomposition. These comparative claims are stated in the introduction and conclusion and illustrated in Sections 3, 5, and 6. 

A further important result is the extension to hierarchical and multivariate decompositions. Section 4 establishes conditions under which grouped factors can be treated consistently, when the Owen two-stage procedure is appropriate, and when the Shapley and Owen decompositions coincide. Proposition 4 is especially important: for decomposable poverty indices with (n) attributes, the contribution of a category equals ( \frac{1}{n}\nu_k^j P_k^j ). 

The paper also derives results for decomposition by income source. In particular, for the variance the Shapley decomposition reproduces the natural covariance-based decomposition, while for other inequality measures the interpretation depends on whether one decomposes income levels or differences in income levels. Proposition 5 further shows that an equally distributed income component receives a negative contribution under certain conditions when one decomposes income levels rather than differences. 

# Main limitations

The paper’s main limitation for your project is that it is a decomposition paper, not a model of labour supply, welfare, or opportunity sets. It does not tell you how to define preferences, feasible job sets, pay schedules, or realized bundles. It only tells you how to allocate the contribution of factors once an aggregate statistic and factor-removal counterfactuals have already been specified. 

A second limitation is that decomposition results are highly dependent on the analyst’s representation of the factors and on the definition of (F(S)). The Shapley rule is formally symmetric across factors, but the substantive meaning of the resulting contributions depends on what exactly counts as “removing” a factor. That is particularly important if one wants to decompose opportunities versus preferences, because those are not naturally observed factors in most applications. This is a reasonable inference from the framework. 

A third limitation is that the method is not itself causal identification. It can decompose an indicator with respect to model inputs, but it does not validate whether the factorization corresponds to causal mechanisms rather than accounting identities or modeling choices. 

Finally, with respect to your (W(z,R,A;y)) framework, the paper is only indirectly useful. It could be integrated consistently only after you have already defined an individual welfare measure, aggregated it into a distributive statistic, and specified the counterfactual meaning of changing (R), (A), or (y). The paper does not itself provide that architecture. 

# Relevance for my JMP

## possible use for framing

This paper is useful for framing the decomposition part of your JMP if you want to argue that inequality in well-being should be decomposed across conceptually distinct sources rather than reported as a single undifferentiated number. It gives a clean language for factor contributions in nonlinear and interacting systems. 

## possible use for model design

It is not useful for structural labour-supply model design directly. However, once you have a structural model generating well-being or welfare outcomes, the paper suggests how to define a decomposition layer on top of that model. In particular, it encourages a design where opportunities, preferences, and pay-related elements are encoded as explicit factors in an aggregate statistic. This is a reasonable inference for your project. 

## possible use for identification

The paper offers essentially no empirical identification guidance. Its contribution is decomposition conditional on a chosen model, not causal or econometric identification of the underlying factors. 

## possible use for welfare measurement

It is not a welfare-measurement paper in the sense of constructing or axiomatizing individual well-being. Its contribution here is secondary: if you already construct an aggregate welfare or inequality functional from your individual (W(z,R,A;y)), this paper gives a principled way to decompose that aggregate. 

## possible use for decomposition

This is the paper’s main use for your JMP. It provides exactly the type of general decomposition rule you may need if you later want to say how much welfare inequality is attributable to preferences, opportunities, pay schedules, taxes, or interactions among them. 

## possible use for comparative application

Potentially useful. If the same welfare or inequality statistic is computed across countries or policy regimes, the Shapley framework could be used to compare which factors account for differences across contexts. This is a reasonable inference rather than an explicit application in the paper. 

# Research questions this paper inspires

1. If individual well-being is measured by (W(z,R,A;y)), can aggregate inequality in (W) be decomposed into contributions from heterogeneity in (R), heterogeneity in (A), and heterogeneity in (y) using a Shapley-based procedure?

2. What is the most defensible counterfactual definition of “removing” opportunity heterogeneity when feasible job sets are latent, stochastic, or estimated rather than directly observed?

3. Does a Shapley decomposition of welfare inequality remain informative when preferences and opportunity sets interact strongly, or do the results become too dependent on modeling choices?

4. How should one group factors hierarchically in a jobs-and-well-being model so that primary contributions, such as “opportunities” and “preferences,” remain aggregation consistent with their subcomponents?

5. Can a Shapley decomposition be combined with an axiomatic theory of compensation and responsibility so that the decomposed contributions have both statistical and ethical interpretation?

# Challenge to this paper

The central challenge is that the Shapley rule is elegant formally but underdetermined substantively. The method is exact and symmetric once the model (F) is fixed, but in many real applications the difficult question is precisely how the factors should be defined and what it means to eliminate one factor while holding others in place. For projects like yours, where “opportunities” and “preferences” are deep conceptual objects rather than directly observed regressors, the decomposition can easily look precise while resting on contestable modeling choices. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper formulates decomposition at the level of an aggregate indicator (I=f(X_1,\dots,X_m)) and assigns factor contributions through the Shapley value. It does not define individual well-being as a function of realized bundle, preferences, feasible set, and pay schedule, and it does not discuss jobs, abilities, or opportunity sets in your sense. 

[reasonable inference for my project] The paper could become highly relevant once your framework has already produced an aggregate object to decompose, for example inequality in (W(z,R,A;y)) across individuals. In that setting, one could try to treat distributions or transformations of (R), (A), and (y) as contributory factors and then compute their Shapley contributions to the chosen aggregate statistic. 

[unclear from paper] The paper gives no guidance on how to define (R), (A), or (y) as removable factors in a way consistent with your axioms. It does not address whether welfare should satisfy independence of (A), independence of (y), responsibility for opportunities, responsibility for acquired ability, or any reference-opportunity-set principle. 

[reasonable inference for my project] In your taxonomy, this paper is closest to decomposition of inequality and to methodological support for comparative attribution. It is not close to laissez-faire evaluation, reference opportunity sets, or independence axioms. Its role would be downstream: after a well-being measure has been defined and justified, not before. 

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

The paper is not substantively about opportunities versus preferences. It does not define either concept, and it does not propose ethical rules for how to treat them. 

Its relevance is methodological. If a separate model already distinguishes opportunity factors from preference factors, then the Shapley rule offers a disciplined way to attribute portions of an aggregate inequality or poverty statistic to each side. But that distinction must come from elsewhere; the paper does not create it. This is a reasonable inference for your project. 

# Useful quotations / formulas

The general decomposition problem is posed as
[
I=f(X_1,X_2,\dots,X_m),
]
with the goal of assigning contributions (C_k) to the factors. This is the paper’s master formulation. 

The Shapley decomposition rule is
[
C_k^S(K,F)=\sum_{S\subseteq K\setminus{k}} \pi(|S|,|K\setminus{k}|),kF(S),
]
where (kF(S)=F(S\cup{k})-F(S)). This is the key formula in equations (2.8)–(2.9). 

A concise statement of the paper’s contribution is that the rule yields an exact additive decomposition and interprets each factor’s contribution as its expected marginal effect over all elimination paths. That is the conceptual core of the paper. 

# Suggested tags

shapley-decomposition, inequality-decomposition, poverty-decomposition, multivariate-decomposition, hierarchical-decomposition, Owen-value, distributional-analysis, methodology

# My quick takeaway

This is not a core labour-supply or opportunity-set paper, but it is a core decomposition paper. For your corpus, it belongs on the methodological shelf that supports later decomposition claims. Its main use is clear: if your JMP eventually defines a credible well-being or welfare statistic built from (z), (R), (A), and (y), this paper gives you one of the strongest available general procedures for attributing aggregate inequality or welfare differences across interacting factors. What it does not do is solve the hard conceptual problem of defining opportunities, preferences, or responsibility in the first place. 
