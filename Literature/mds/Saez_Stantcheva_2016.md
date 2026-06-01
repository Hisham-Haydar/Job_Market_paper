---

title: "Generalized Social Marginal Welfare Weights for Optimal Tax Theory"
authors: ["Emmanuel Saez", "Stefanie Stantcheva"]
year: 2016
outlet: "American Economic Review"
country_or_context: "General optimal tax theory with illustrative U.S. calibrations"
population: "Continuum of taxpayers in stylized income-tax models; one illustration uses U.S. intergenerational mobility data"
data_period: "Theoretical paper; illustrations use U.S. 2008 tax return data and intergenerational mobility estimates for U.S. individuals born in 1980–1981"
shelf: "optimal_taxation_normative_welfare_weights"
tags: ["optimal taxation", "social marginal welfare weights", "normative public economics", "fairness", "equality of opportunity", "poverty alleviation", "horizontal equity", "tagging"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Saez, Emmanuel, and Stefanie Stantcheva. 2016. “Generalized Social Marginal Welfare Weights for Optimal Tax Theory.” *American Economic Review* 106(1): 24–45. 

# One-sentence contribution

The paper reformulates optimal tax theory around generalized social marginal welfare weights that aggregate money-metric gains and losses from tax reforms, thereby preserving the tractability of standard optimal-tax formulas while allowing fairness criteria that are not reducible to individual utility. 

# Why this paper matters

This paper matters because it offers a clean separation between positive behavior and normative evaluation. Individuals still maximize standard utility functions, but the planner’s evaluation of reforms is conducted through generalized social marginal welfare weights rather than through a primitive social welfare function over utilities. That is a major conceptual move for any project that wants to avoid collapsing fairness judgments into utility comparisons. 

For your project, the paper is especially valuable because it shows how one can let normative evaluation depend on objects that need not coincide with the arguments of utility. In your language, this is highly relevant whenever one wants the welfare evaluator to depend on features of opportunities or deservingness that are not simply encoded in preferences (R). It is not a labor-supply estimation paper and not a feasible-set paper, but it is one of the strongest papers for building a welfare-evaluation layer on top of a positive model. 

# Core research question

Can optimal tax theory be reformulated so that tax reforms are evaluated using socially chosen fairness weights rather than a primitive welfarist social objective, while retaining standard optimal-tax formulas and accommodating alternative justice principles such as libertarianism, equality of opportunity, poverty alleviation, and horizontal equity? 

# Economic setting and context

The paper is a normative public-economics paper in optimal tax theory. Its central object is the design and evaluation of tax reforms, not the estimation of labor supply or the empirical incidence of actual tax systems. The authors position the paper as a way to reconcile gaps between standard welfarist optimal-tax theory and actual tax-policy reasoning, especially where public debate appeals to fairness concepts that are not easily represented as utility aggregation.

The setting is mostly theoretical, but the paper includes illustrative applications. In the equality-of-opportunity example, it uses U.S. intergenerational mobility statistics from Chetty et al. and 2008 U.S. tax-return data to construct social weights and implied optimal marginal tax rates across the income distribution. The paper also reports an online survey in the appendix to elicit social preferences, though the main article remains primarily theoretical.

# Model / theoretical framework

The model class is an optimal-tax framework with standard individual utility maximization and a generalized reform-evaluation criterion. Individuals derive utility from consumption and disutility from earnings:
[
u_i = u(c_i - v(z_i; x_i^u, x_i^b)),
]
with the government setting an income tax (T(z)) and individuals choosing earnings (z_i). The main analytical environment uses quasilinear utility to rule out income effects on earnings and simplify formulas. 

The novelty is normative rather than behavioral. Instead of postulating a social welfare function to maximize, the planner assigns each individual a generalized social marginal welfare weight (g_i), interpreted as the social value of giving that individual one additional dollar of consumption. Small budget-neutral tax reforms are then judged desirable if the weighted sum of money-metric gains is positive. A locally optimal tax system is one around which no small budget-neutral reform is desirable.

The framework is therefore explicitly normative, but it nests the standard welfarist first-order approach as a special case. If the generalized weights equal standard marginal social welfare weights, the resulting formulas coincide with standard optimal-tax formulas. At the same time, the generalized approach allows the weights to depend on characteristics that do not enter utility, and to ignore some characteristics that do enter utility, depending on what society considers fair to compensate.

# Key objects

The central objects are the generalized social marginal welfare weights (g_i), the average social welfare weights by income level (\bar g(z)), and the average weight above income level (G(z)). Definition 1 specifies individual weights as
[
g_i = g(c_i, z_i, x_i^s, x_i^b),
]
where some characteristics affect only social evaluation, some affect only utility, and some may affect both. The diagram on page 6 visually distinguishes these three sets of characteristics, which is one of the paper’s most useful conceptual devices. 

The main policy object is the nonlinear income-tax schedule (T(z)), and the key analytical objects for tax formulas are the local Pareto parameter (\alpha(z)), the earnings elasticity (e(z)), and the income-distribution functions (H(z)) and (h(z)). Proposition 2 gives the optimal marginal tax formula:
[
T'(z)=\frac{1-\bar g(z)}{1-\bar g(z)+\alpha(z)e(z)}.
]
This is formally the standard Saez formula with generalized weights substituted for standard welfare weights. 

# Data

This is not a data-driven estimation paper. Its empirical content consists of illustrations. The most substantive illustration is the equality-of-opportunity application, which uses U.S. intergenerational mobility estimates from Chetty et al. for individuals born in 1980–1981 and combines them with the 2008 U.S. income distribution to compute implied social weights and illustrative optimal marginal tax rates at various percentiles. Table 2 on page 19 reports these values. 

There is also an online survey, referenced in the paper, designed to elicit social preferences over tax burdens and deservingness. The article notes its existence, but the main text does not develop it as a central empirical exercise. 

# Identification logic

There is no econometric identification strategy in the usual sense. The paper is not trying to identify behavioral primitives causally from quasi-experimental variation. Instead, it proceeds analytically: choose a set of generalized social marginal welfare weights, combine them with behavioral elasticities and the income distribution, and derive first-order tax formulas and reform-evaluation criteria.

In the illustrative equality-of-opportunity calibration, the key assumptions concern how family background maps into social weights, how representation among top earners is measured, and what earnings elasticity is used. The authors assume a constant elasticity (e=0.5) for the U.S. illustration and use empirical mobility statistics to construct (G(z)). This is calibration, not causal identification. 

# Estimation / empirical strategy

There is no estimation of a structural labor-supply model in the paper itself. The strategy is to derive a tax-reform framework and then apply it to a sequence of theoretical and calibrated examples: fixed incomes, freeloaders, tagging and horizontal equity, equality of opportunity, and poverty alleviation. Table 1 on page 11 summarizes how the generalized-weights approach differs from actual practice and from the standard welfarist criterion across these cases. 

The equality-of-opportunity section then calibrates implied social weights using intergenerational mobility data and computes optimal marginal tax rates by percentile. Table 2 shows that under the equality-of-opportunity weights the implied top rates are lower and less progressive than under a standard utilitarian log-utility calibration. 

# Treatment of preferences

The treatment of preferences is one of the paper’s most important contributions. Individual preferences remain standard and are not modified to encode fairness directly. Individuals still maximize their own utility. The authors are explicit that they keep individual preferences intact and move fairness considerations into the social weights instead. 

This means the paper separates positive preferences from normative judgment more sharply than standard welfarism. Social welfare weights may depend on characteristics that do not enter utility, and may omit characteristics that do enter utility if society does not regard compensation for them as fair. That is precisely the type of separation your project often needs when distinguishing what people prefer from what society should compensate or hold them responsible for.

# Treatment of opportunities / constraints

The paper does not model opportunities as feasible job sets, latent offers, or demand-side labor-market constraints. There is no (A)-type opportunity set in the sense of a set of attainable jobs or bundles. The only constraints explicitly modeled are those of the tax schedule and the individual earnings problem. 

However, the paper is relevant for opportunities in a broader normative sense. In the equality-of-opportunity example, family background affects the social weights even though it need not affect utility directly and is not directly taxable. The weights are concentrated on those from disadvantaged backgrounds conditional on earnings, because they are viewed as having more merit. That is not an explicit feasible-set treatment of opportunities, but it is an explicit normative treatment of background circumstances.

The paper therefore helps much more with normative evaluation of circumstances and deservingness than with modeling actual opportunity sets. It can help distinguish what society wants to compensate from what individuals happen to prefer, but it does not itself distinguish preference heterogeneity from feasible-set heterogeneity in a structural sense.

# Welfare / normative object

The welfare object is not a global social welfare function but a local tax-reform criterion based on generalized social marginal welfare weights. A reform is desirable if the weighted sum of individual money-metric gains is positive; a tax system is locally optimal if no small budget-neutral reform is desirable. This is fundamentally a local, first-order normative theory.

The paper is explicitly designed to incorporate alternative justice principles. The authors show how weights can operationalize libertarian concerns, equality of opportunity, poverty alleviation, and horizontal equity. They also show that if the generalized weights are nonnegative, the framework respects the Pareto principle locally. This is crucial: the paper aims to enlarge the ethical content of optimal tax theory without abandoning local Pareto efficiency.

For your project, this is directly relevant to responsibility and compensation, though not specifically to opportunity sets. The paper provides a normative aggregator over reform gains and losses that can be made sensitive to morally relevant background or fairness criteria, without requiring those criteria to be embedded in utility itself.

# Main findings

The first main result is formal: optimal tax formulas keep exactly the same form as in standard welfarist optimal tax theory once standard marginal welfare weights are replaced by generalized ones. Proposition 2 gives the nonlinear tax formula, and Proposition 3 gives the linear-tax analogue. This is the central technical achievement of the paper. 

The second main result is conceptual: generalized weights can rationalize several fairness ideas that standard welfarism handles poorly. The summary table on page 11 states that the generalized-weight approach can produce nondegenerate optimal taxes with fixed incomes if weights depend on taxes paid, can account for freeloaders if weights depend on counterfactual work behavior, can justify limited tagging via horizontal-equity concerns, and can incorporate poverty alleviation while maintaining Pareto efficiency. 

The third main result concerns the equality-of-opportunity illustration. Using U.S. mobility data, the paper finds that the representation of individuals from disadvantaged backgrounds remains substantial even at the very top: Table 2 on page 19 reports (G(z)=0.340) at the 99th percentile and (0.330) at the 99.9th percentile. With (a=1.5) and (e=0.5), this implies an asymptotic top rate of about 47 percent under equality of opportunity, versus about 57 percent under the utilitarian benchmark. The optimal schedule is U-shaped and roughly flat within the top 1 percent. 

A fourth result concerns poverty. The paper argues that direct poverty-gap minimization can yield Pareto-dominated outcomes, such as negative bottom rates when the poorest work, whereas the generalized-weights approach can pursue poverty alleviation with weights concentrated on the poor while maintaining Pareto efficiency. Figure 2 on page 20 illustrates the contrast between direct poverty-gap minimization and the generalized-weights approach. 

# Main limitations

The first limitation is that the framework is local. The paper is explicit that it evaluates only small reforms around a tax system and cannot, in general, systematically rank multiple local optima. This is a real limitation relative to a full social welfare function that gives a global ordering over allocations. 

A second limitation is that the generalized weights are primitives. The paper deliberately takes society’s preferences as given and does not analyze how the weights arise politically or ethically beyond illustrative justice principles. That makes the framework flexible, but also underdetermined unless one has an external source for the weights. 

A third limitation for your purposes is that the paper does not model feasible opportunity sets. The equality-of-opportunity example uses family background and representation among earners, not actual job opportunities or attainable bundle sets. Thus, it is not directly usable for a (W(z,R,A;y)) framework in which (A) is a set-valued opportunity object.

A fourth limitation is that the positive side of the model is stylized. The main results are derived in simple tax models, often with quasilinear utility and in some sections without income effects. The equality-of-opportunity section is an illustration, not an estimated structural model.

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing. It gives you a rigorous way to say that welfare evaluation need not be identical to preference aggregation. If your JMP needs to distinguish positive behavior from normative evaluation, this paper is a powerful citation anchor.

## possible use for model design

It is not directly a labor-supply model-design paper. But it is useful if your design strategy is to estimate a positive model first and then place a fairness-sensitive normative layer on top of it. In that respect, it complements rather than replaces structural labor-supply or RURO modeling. 

## possible use for identification

Its value here is limited. The paper does not help identify preferences or opportunities causally. What it does provide is a disciplined way to translate externally chosen fairness principles into implementable weights once the positive environment is specified.

## possible use for welfare measurement

This is one of its strongest uses for your JMP. The paper offers an operational welfare-evaluation device that can depend on background, taxes paid, counterfactual behavior, or poverty status without forcing those considerations into utility. That is directly relevant if your project needs a welfare object richer than individual utility alone.

## possible use for decomposition

Indirectly useful. The paper does not provide a Shapley-type decomposition of inequality or welfare, but it does decompose normative concern across ethically distinct dimensions by choosing which characteristics enter the weights. That could be combined later with a formal decomposition method. [reasonable inference for my project] supported by

## possible use for comparative application

Potentially useful if your project later compares settings with different notions of deservingness or mobility. The equality-of-opportunity example shows how weights can be calibrated from mobility data, so cross-country differences in mobility could, in principle, imply different optimal tax schedules under the same fairness principle. [reasonable inference for my project] supported by 

# Research questions this paper inspires

Can a generalized social marginal welfare weight be defined over (W(z,R,A;y)) rather than over disposable income alone, so that optimal policy reflects both realized well-being and ethically relevant opportunity differences?

How should social weights depend on feasible job sets (A) when those sets are estimated rather than observed, and when society wants to compensate some opportunity deficits but not others?

Can one combine a RURO-style positive model of opportunities with Saez–Stantcheva-style generalized weights to obtain optimal tax or transfer formulas that remain operational?

What empirical objects would be needed to calibrate social weights that depend on opportunity disadvantage rather than only on family background or income rank?

When fairness concerns involve horizontal equity or responsibility for acquired traits, can generalized weights be made compatible with your axiomatic constraints on well-being measurement?

# Challenge to this paper

The main challenge is that the framework gains ethical flexibility by moving the hard normative work into the choice of weights, but it does not itself tell us how those weights should be chosen. In difficult cases, that may simply relocate the central problem rather than solve it. For a project like yours, this is both the paper’s strength and its weakness: it cleanly separates evaluation from utility, but the evaluator’s criterion remains externally imposed.

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper separates individual utility from social evaluation. Social weights can depend on characteristics that do not enter utility, and they can ignore utility-relevant characteristics that society does not want to compensate. This is directly explicit in the framework and in the diagram on page 6. 

[reasonable inference for my project] That feature makes the paper very relevant if your framework eventually has a positive layer in which choices depend on (R), (A), and (y), and a normative layer in which well-being or policy evaluation should depend on only some of those objects, or on additional ethically relevant characteristics. In other words, it offers a template for separating behavioral primitives from fairness weights.

[unclear from paper] The paper does not define an individual well-being measure (W(z,R,A;y)). It does not analyze feasible job sets (A), nor does it study whether welfare should satisfy independence of (A), independence of (y), or any axioms of the kind you are working with. Those issues are outside its scope.

[reasonable inference for my project] In your taxonomy, the paper is closest to responsibility for opportunities, compensation for opportunities, reference-sensitive evaluation, and a general rejection of naive utility aggregation. It is not close to laissez-faire evaluation. It is also not naturally an “independence of (A)” paper; if anything, its spirit is that socially relevant characteristics may matter normatively even when they are not utility arguments or tax bases.

# Relation to Bargain et al. (2013)

This paper is relevant to the broader welfare-and-labor-supply literature associated with structural tax-benefit analysis, but in a different role. Bargain-style work is typically about measuring welfare or reform incidence in empirically estimated tax-benefit environments with heterogeneous preferences. Saez and Stantcheva contribute the normative aggregation layer: how to evaluate money-metric gains and losses when society’s fairness concerns are not reducible to utility. [reasonable inference for my project] supported by

So the relation is complementary rather than direct. If Bargain-type models tell you how reforms change utilities or incomes, Saez–Stantcheva tell you how one might normatively weight those changes without committing to pure welfarism. That is highly relevant for a project trying to integrate structural modeling with richer fairness concepts. [reasonable inference for my project] supported by 

# Relation to opportunities vs preferences

The paper is highly relevant to this distinction at the normative level. It allows social evaluation to depend on background or deservingness variables even when those variables are not arguments of utility, and it allows some utility-relevant factors to be ignored if society does not regard them as compensation-worthy.

But it is not a structural model of opportunities versus preferences. It does not estimate separate preference and opportunity components, and it does not model feasible opportunity sets. Its contribution is instead to provide a language for saying that what matters normatively need not coincide with what matters behaviorally. That is a major conceptual bridge for your project, even if the paper stops short of your full (W(z,R,A;y)) architecture.

# Useful quotations / formulas

The central optimal marginal tax formula is
[
T'(z)=\frac{1-\bar g(z)}{1-\bar g(z)+\alpha(z)e(z)}.
]
This is the key operational result because it preserves the standard formula while replacing standard welfare weights with generalized ones. 

Definition 1 is also central:
[
g_i=g(c_i,z_i,x_i^s,x_i^b).
]
It matters because it makes explicit that some characteristics affect only social weights, some affect only utility, and some may affect both. 

Table 1 on page 11 is useful conceptually. It summarizes that the generalized-weight approach can handle fixed-income taxation, freeloaders, tagging, and poverty alleviation in ways the standard welfare criterion cannot or handles poorly. 

# Suggested tags

generalized-welfare-weights, optimal-taxation, fairness, nonwelfarism, equality-of-opportunity, poverty-alleviation, horizontal-equity, tagging, local-optimal-tax-theory

# My quick takeaway

This is a high-priority normative paper for your corpus. It does not solve the positive modeling problem of opportunities, feasible job sets, or heterogeneous preferences. What it does very well is solve a different problem: how to evaluate reforms when fairness judgments are richer than utility aggregation. For your project, its strongest use is as a conceptual and operational bridge between a positive structural model and a non-naive welfare criterion.
