---

title: "Compensating Variation and Hicksian Choice Probabilities in Random Utility Models That Are Nonlinear in Income"
authors: ["John K. Dagsvik", "Anders Karlström"]
year: 2005
outlet: "The Review of Economic Studies"
country_or_context: "General methodological framework for discrete choice"
population: "Consumers choosing among discrete alternatives"
data_period: ""
shelf: "welfare_methods_random_utility"
tags: ["compensating variation", "equivalent variation", "Hicksian demand", "random utility", "discrete choice", "nonlinear income effects", "welfare measurement", "GEV", "mixed logit"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Dagsvik, John K., and Anders Karlström. 2005. “Compensating Variation and Hicksian Choice Probabilities in Random Utility Models That Are Nonlinear in Income.” *The Review of Economic Studies* 72(1): 57–76. 

# One-sentence contribution

The paper derives exact analytical formulas for Hicksian choice probabilities, the distribution of the random expenditure function, and the distribution of compensating variation and equivalent variation in discrete-choice random-utility models with nonlinear income effects.

# Why this paper matters

This paper matters because it addresses a central welfare-measurement problem in discrete choice: once utility is nonlinear in income, the usual log-sum shortcut no longer applies, and welfare effects become substantially harder to characterize. The paper’s main achievement is to recover exact Hicksian welfare objects in this setting rather than relying on approximations or Monte Carlo methods alone.

For your project, this is an important methodological paper on the welfare side. It does not model opportunity sets in the labor-market sense, but it is directly relevant if one wants to move from a random-utility labor-supply or job-choice model to exact money-metric welfare measures such as compensating variation. In that respect it is especially useful as a bridge between discrete-choice behavioural models and welfare measurement. [reasonable inference for my project] supported by

# Core research question

How can one define and compute Hicksian demand, Hicksian choice probabilities, and compensating variation in random-utility discrete-choice models when utilities are nonlinear in income, so that standard log-sum and quasilinear shortcuts are unavailable?

# Economic setting and context

The paper is methodological and not tied to a single country, market, or dataset. It studies a generic consumer choosing among discrete alternatives, each characterized by attributes including price, under a random-utility model. Welfare effects are evaluated under changes in prices or other attributes associated with the alternatives.

The authors are explicit that the target is compensating variation and related Hicksian welfare objects in discrete choice, including the distribution of expenditure conditional on the initial utility level and the joint distribution of expenditure, initial choice, and post-policy choice. This is a welfare-analysis paper rather than an empirical application paper.

# Model / theoretical framework

The model class is a random-utility discrete-choice model. A consumer faces a feasible set (B) of discrete alternatives and the utility of alternative (j) is
[
U_j = v_j(w_j,y)+\varepsilon_j,
]
where (y) is income, (w_j) is a vector of attributes including price, (v_j(\cdot)) is deterministic and increasing in income, and (\varepsilon_j) is a random term. The paper initially assumes that the joint distribution of the random terms does not depend on the structural utility terms.

The agent chooses among discrete alternatives. The feasible set is therefore the menu of available alternatives (B), not a continuous budget set or latent job set. The paper is positive in its behavioural setup and welfare-analytic in its target objects. It is not an explicitly normative theory of justice or fairness. 

The key dual object is the random expenditure function (Y_B(w,u)), defined as the minimum expenditure needed to attain utility level (u) under attributes (w). The paper shows that this can be represented as the minimum over alternative-specific expenditure requirements (Y_k(w_k,u-\varepsilon_k)). This formulation is then used to derive Hicksian choice probabilities and the distribution of compensating variation under attribute or price changes. 

The paper later extends the framework to allow the structural part of utility to depend on random coefficients, so that the deterministic component becomes (v_j(w_j,y;\beta)) with (\beta) random. It also provides simplifications for the multivariate extreme-value class and for the i.i.d. extreme-value case.

# Key objects

The main economic objects are the indirect utility
[
V_B(w,y)=\max_{k\in B}{v_k(w_k,y)+\varepsilon_k},
]
the random expenditure function (Y_B(w,u)), the Hicksian choice probabilities (P_B^h(j,w,u)), and the welfare measures compensating variation and equivalent variation. 

A particularly important object is the expenditure function conditional on the initial utility level, (Y_B(w,V_B(w^0,y^0))). This is central because compensating variation is defined as the difference between post-policy income and the expenditure needed to attain initial utility under the new regime. The paper derives both its distribution and its moments. 

The paper also derives joint distributions involving the initial choice and the post-change compensated choice. This is useful because welfare analysis can then be conditioned on transition patterns across alternatives, not only on aggregate welfare distributions. 

# Data

There is no empirical dataset in the paper. The analysis is theoretical and formula-based, with illustrative examples such as nested logit, introduction of a new alternative, and removal of an alternative. These are examples of model environments, not empirical applications to observed microdata.

# Identification logic

The paper is not primarily an identification paper in the nonparametric sense. Its logic is conditional and analytical: given knowledge of the utility specification and the joint distribution of the random utility components, derive exact formulas for Hicksian welfare objects. This is different from later work, such as Bhattacharya’s, which asks whether welfare can be identified from choice probabilities alone without parametric knowledge of heterogeneity. [reasonable inference for my project] supported by

The paper is explicit that Hicksian choice probabilities can be computed readily provided the cumulative distribution (F_B(\cdot)) is known. In the GEV and i.i.d. extreme-value cases, the formulas simplify substantially and become especially tractable. Thus the paper’s “identification” is largely from assumed model structure and known heterogeneity distributions, not from minimal observable implications alone.

The extension to random coefficients remains within this same spirit. The paper allows (v_j(w_j,y;\beta)) with random (\beta), but still assumes enough structure to integrate out (\beta) and obtain the relevant welfare distributions. Again, the approach is exact within the model, not nonparametric from demand data alone. 

# Estimation / empirical strategy

The paper is theoretical and does not estimate a model. Its “empirical strategy” is instead methodological guidance: once a random-utility model is estimated and the relevant distribution (F_B) is known, the formulas in the paper can be used to compute Hicksian choice probabilities, the distribution of expenditure, and the distribution of compensating variation exactly.

A major practical message is that the formulas become especially simple in the GEV class and even more so under i.i.d. extreme-value errors. In those cases, the paper gives closed-form or near-closed-form expressions for the relevant welfare objects and for mean compensating variation. 

The paper also argues that, relative to simulation-based approaches, these analytical formulas are preferable when available. In the conclusion, the authors state that when the model belongs to the GEV class, the formulas simplify and this method is to be preferred to using simulations. 

# Treatment of preferences

Preferences are modeled through the deterministic utility components (v_j(w_j,y)), which may be nonlinear in income and may differ across alternatives. This is crucial because nonlinear income effects are precisely what make Hicksian welfare measurement nontrivial in discrete choice.

The paper does not study preference heterogeneity in an unrestricted way. It works within a fully specified random-utility framework where the distribution of the random components is known or sufficiently structured. In the extension with random coefficients, heterogeneity enters through a random parameter vector (\beta), again under maintained distributional assumptions. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly in the labor-market or feasible-job-set sense. The feasible set is simply the menu (B) of discrete alternatives under consideration. There is no latent job-offer process, no opportunity density, and no distinction between preference heterogeneity and opportunity heterogeneity of the kind central to your project. 

Constraints therefore enter only through the menu of alternatives and the income-price structure. The paper is about exact welfare measurement conditional on a given discrete-choice environment, not about how that environment is generated or whether it is equally available across agents.

That said, the paper does explicitly allow the choice set to change across policy regimes, for example when an alternative is removed or a new one appears. It shows how the formulas can be adapted to such cases by treating the unavailable alternative as having an effectively prohibitive price or utility level. This is a menu-change result, but it is still not an opportunity-set theory in your sense. 

# Welfare / normative object

The welfare object is Hicksian money-metric welfare, especially compensating variation and equivalent variation. The paper is explicit that the goal is to derive the distribution of these objects in discrete-choice random-utility models with nonlinear income effects.

The paper is positive with welfare applications rather than explicitly normative in the fairness sense. It does not specify a social welfare function, does not discuss interpersonal comparability, and does not address responsibility for opportunities or compensation for unequal feasible sets. Its welfare analysis is standard money-metric welfare analysis at the individual level.

Still, for your project it is important because it shows how exact welfare measurement can be layered onto a discrete-choice model once the behavioural structure is specified. In other words, it is valuable not for choosing the ethical welfare criterion, but for computing one important class of welfare measures exactly. [reasonable inference for my project] supported by

# Main findings

The first main result is that the random expenditure function in a discrete-choice random-utility model can be represented as the minimum of alternative-specific expenditure requirements, and its distribution can be written explicitly. Theorem 1 establishes existence, uniqueness, continuity, monotonicity, and the distribution formula for (Y_B(w,u)). 

The second main result is the definition and derivation of Hicksian choice probabilities. Theorem 2 provides an exact formula for the probability of choosing alternative (j) conditional on attaining a fixed utility level (u). The paper emphasizes that these probabilities can be computed with only a one-dimensional integral once the cumulative distribution (F_B) is known.

The third main result is an aggregate discrete-choice version of Shephard’s Lemma. Corollary 1 shows that the derivative of expected expenditure with respect to the price of alternative (j) equals the Hicksian choice probability for (j). The paper explicitly interprets this as a probabilistic or aggregate version of Shephard’s Lemma.

The fourth main result is the derivation of the distribution of expenditure and compensating variation under price or attribute changes conditional on maintaining the initial utility level. Theorems 3 and 4 derive the distribution of (Y_B(w,V_B(w^0,y^0))) and the joint distribution with initial and post-change choices. This yields exact expressions for compensated transition probabilities. 

The fifth main result is that the formulas simplify substantially in the GEV and especially i.i.d. extreme-value cases, yielding tractable expressions for mean compensating variation and related objects.

# Main limitations

The main limitation for your purposes is that the framework is fully model-dependent. The welfare objects are exact conditional on knowledge of (F_B) and of the utility structure, but the paper does not establish that these objects are recoverable from choice probabilities alone under weak assumptions. This makes it less robust than later nonparametric approaches. [reasonable inference for my project] supported by

A second limitation is that the paper is silent on opportunities in the labor-market sense. The feasible set (B) is simply the choice menu, and no attempt is made to model unequal access to alternatives as a separate source of welfare inequality. This limits its direct value for a (W(z,R,A;y)) framework where (A) is central. 

A third limitation is that the paper is not a decomposition paper. It does not separate welfare differences into components due to prices, preferences, opportunities, or policy schedules beyond the Hicksian money-metric calculation itself.

A fourth limitation is that the paper remains at the individual welfare-measurement level. It does not address social aggregation, interpersonal comparisons, or fairness criteria. For your project, this means it is a technical welfare paper, not a social-choice or justice paper.

# Relevance for my JMP

## possible use for framing

This paper is useful for framing the welfare-measurement side of your project. It shows that once one has a discrete-choice behavioural model, exact Hicksian welfare measures can in principle be derived even with nonlinear income effects. That is helpful if you want to distinguish clearly between behavioural modelling and welfare computation.

## possible use for model design

It is useful for model design insofar as it shows what kinds of welfare objects become available once a random-utility model is specified. In particular, if your job-choice or labor-supply model is discrete and nonlinear in income, this paper gives one route to exact money-metric welfare analysis. [reasonable inference for my project] supported by

## possible use for identification

Its direct use for identification is limited because it does not solve the weak-identification problem. Instead, it clarifies what one can compute once the model and heterogeneity distribution are sufficiently specified. In that sense it is more a post-identification welfare paper than an identification paper. [reasonable inference for my project] supported by

## possible use for welfare measurement

This is the paper’s strongest contribution for your JMP. It is a very strong reference for exact Hicksian welfare measurement in random-utility discrete choice when income effects matter. It is especially relevant if later parts of your project need compensating variation or equivalent variation from discrete-choice models.

## possible use for decomposition

Direct use is weak. The paper does not decompose welfare into opportunities, preferences, or pay-schedule components. At most, it gives a way to compute one welfare object exactly after the underlying discrete-choice environment is specified.

## possible use for comparative application

Indirectly, it could be used comparatively across countries or reforms if one had comparable random-utility models. But the paper itself is not comparative and provides no country application. 

# Research questions this paper inspires

Can the exact Hicksian welfare formulas in this paper be embedded inside a latent-job labor-supply model so that welfare effects of changes in job availability, not just prices, can be computed?

What is the relationship between Dagsvik–Karlström exact money-metric welfare and a broader well-being measure (W(z,R,A;y)) when (A) is an explicit opportunity set?

Can one derive exact or approximate compensating-variation formulas when the choice set itself is generated by a latent opportunity process rather than treated as exogenous?

How sensitive are policy conclusions from structural labor-supply models to using exact Dagsvik–Karlström-style Hicksian welfare rather than simpler log-sum or quasilinear approximations?

Can compensated transition probabilities be used to decompose welfare effects of reforms into “same-choice” and “choice-switching” margins in job-choice settings?

# Challenge to this paper

The sharpest challenge is that the paper gives exact formulas conditional on a strong parametric or distributional model, but it does not tell us whether those welfare distributions are identified from observed behaviour under weaker assumptions. Later work shows that this distinction is substantive, not merely technical. So the paper is powerful as a model-internal welfare tool, but less persuasive as a general empirical welfare method when the heterogeneity structure is uncertain. [reasonable inference for my project] supported by

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper develops exact Hicksian welfare measurement for random-utility discrete-choice models, with compensating variation and expenditure-based welfare objects at the center. Its main ingredients are the utility specification (U_j=v_j(w_j,y)+\varepsilon_j), the indirect utility (V_B), and the expenditure function (Y_B). 

[reasonable inference for my project] A rough mapping to your notation is that the realized chosen alternative is part of (z), the deterministic-plus-random utility representation corresponds loosely to (R), and the price/attribute environment can be thought of as part of (y)-type institutional structure. But there is no explicit analogue of (A) as a feasible job or ability set beyond the exogenously given choice menu (B). supported by 

[explicit in paper] The paper does not define a well-being measure (W(z,R,A;y)), does not discuss axioms such as independence of (A) or (y), and does not analyze responsibility for opportunities, reference opportunity sets, or laissez-faire evaluation. Those questions are outside its scope.

[reasonable inference for my project] In your taxonomy, the paper is closest to a technical welfare-measurement building block rather than to any substantive axiom. It is potentially useful downstream, once a behavioural model and an ethical interpretation have already been chosen, but it does not itself settle either the opportunity-set question or the normative choice of well-being measure. supported by

[unclear from paper] Whether its exact Hicksian formulas can be adapted cleanly to a latent-job model with endogenous or stochastic opportunity sets is not addressed. 

# Relation to Bargain et al. (2013)

This paper is relevant to the Bargain-type literature mainly as a technical welfare foundation. Bargain-style work uses structural labor-supply models to compare welfare across heterogeneous households, whereas Dagsvik and Karlström provide exact Hicksian welfare formulas for discrete-choice random-utility models with nonlinear income effects. The connection is therefore methodological: this paper offers exact money-metric welfare tools that could, in principle, be used within richer labour-supply settings. [reasonable inference for my project]

# Relation to opportunities vs preferences

The paper is strong on welfare measurement and weak on opportunities. It treats preferences through a structured random-utility model and derives exact welfare consequences of policy changes. But it does not separately model opportunity heterogeneity or unequal feasible sets. 

Its relevance for your opportunities-versus-preferences agenda is therefore indirect. It shows how to compute welfare exactly once the discrete-choice environment is specified, but it does not help decide whether observed differences arise from preferences or opportunities, or how those differences should be treated normatively.

# Useful quotations / formulas

A central formula is the random expenditure function:
[
Y_B(w,u)=\min_{k\in B}Y_k(w_k,u-\varepsilon_k).
]
This representation is the basis for the rest of the paper’s welfare results. 

The distribution of the expenditure function is
[
P(Y_B(w,u)<y)=1-F_B(u-v_1(w_1,y),\ldots,u-v_m(w_m,y)).
]
This is one of the paper’s key analytical results. 

The definition of Hicksian choice probabilities is
[
P_B^h(j,w,u)=P(J_B(w,Y_B(w,u))=j),
]
and Theorem 2 provides an explicit formula for them.

The paper also derives an aggregate version of Shephard’s Lemma:
[
\frac{\partial E Y_B(w,u)}{\partial w_{1j}}=P_B^h(j,w,u),
]
under the stated differentiability conditions. 

# Suggested tags

random-utility-welfare, Hicksian-choice-probabilities, compensating-variation, equivalent-variation, nonlinear-income-effects, exact-welfare-formulas, discrete-choice, GEV, mixed-logit

# My quick takeaway

This is a technically important paper for the welfare side of your corpus. Its main value is not in modelling opportunities, but in showing that exact Hicksian welfare analysis is possible in discrete-choice random-utility models even when utility is nonlinear in income. For your JMP, it is best treated as a downstream welfare-computation reference: once you have a behavioural model of jobs or labour supply, this paper is the kind of tool you may need if you want exact money-metric welfare rather than simpler approximations. But it is not itself a paper about separating preferences from opportunities or about normative responsibility for unequal opportunity sets.
