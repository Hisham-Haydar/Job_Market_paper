---

title: "Compensating Variation and Hicksian Choice Probabilities in Random Utility Models that are Nonlinear in Income"
authors: ["John K. Dagsvik", "Anders Karlström"]
year: 2005
outlet: "The Review of Economic Studies"
country_or_context: "General methodological discrete-choice framework; no country-specific application"
population: "[not an empirical paper]"
data_period: "[not applicable]"
shelf: "discrete_choice_welfare_methods"
tags: ["random utility", "compensating variation", "equivalent variation", "Hicksian demand", "discrete choice", "nonlinear income", "welfare measurement", "GEV", "multinomial logit", "theory"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Dagsvik, John K., and Anders Karlström. 2005. “Compensating Variation and Hicksian Choice Probabilities in Random Utility Models that are Nonlinear in Income.” *The Review of Economic Studies* 72(1): 57–76. 

# One-sentence contribution

The paper derives exact Hicksian choice probabilities and exact distributions of the random expenditure function, compensating variation, and equivalent variation for discrete random utility models with utility nonlinear in income. 

# Why this paper matters

This paper matters because it fills a genuine gap in discrete-choice welfare analysis: when utility is nonlinear in income, the familiar linear-income log-sum welfare shortcut is unavailable, and the paper shows how to recover exact welfare objects anyway. It therefore provides a rigorous money-metric welfare layer for random utility models rather than relying on approximations or simulation-only workarounds. 

For your potential JMP, the paper is especially relevant on the welfare-measurement side, not on the opportunity-set side. If you estimate a discrete-choice labor supply or RURO-style model and then want exact money-metric welfare objects under policy or price changes, this paper is one of the key methodological references. 

# Core research question

How can one define and compute Hicksian demand, the expenditure function, compensating variation, and equivalent variation in discrete random utility models when utility is nonlinear in income? 

# Economic setting and context

The paper is not tied to a specific country, dataset, or policy episode. Its setting is a general discrete-choice framework in which an agent chooses among a finite set of alternatives, each with attributes and possibly prices, and the researcher wants to evaluate welfare effects of price or policy changes. 

The motivating context is the welfare analysis of discrete choices under nonlinear income effects. The authors position the paper against earlier work where analytic formulas for the distribution of compensating variation were not available in the nonlinear-income case, so researchers relied on approximations or Monte Carlo simulation. 

# Model / theoretical framework

The model class is a general random utility model for discrete choice. For alternative (j), utility is
[
U_j = v_j(w_j,y) + \varepsilon_j,
]
where (y) is income, (w_j) is a vector of attributes including price, (v_j(\cdot)) is deterministic and may be nonlinear in income, and (\varepsilon_j) is the random utility component. The feasible choice set is a finite set (B\subseteq S). 

The paper defines the indirect utility
[
V_B(w,y)=\max_{k\in B}\big(v_k(w_k,y)+\varepsilon_k\big),
]
and then defines the random expenditure function (Y_B(w,u)) as the income required to attain utility level (u). Hicksian choice probabilities are defined as the probability of choosing alternative (j) when utility is held fixed at (u), namely
[
P_B^h(j,w,u)=P!\left(J_B(w,Y_B(w,u))=j\right).
]
The framework is normative only in the individual money-metric sense; it is not a social-welfare or fairness framework. 

# Key objects

The main objects are the random indirect utility (V_B(w,y)), the random expenditure function (Y_B(w,u)), Hicksian choice probabilities (P_B^h(j,w,u)), compensating variation, equivalent variation, and the joint distribution of expenditure with the initial and post-policy choices. These are the core welfare-theoretic objects of the paper. 

A second important object is the joint distribution (F_B) of the utility shocks. The paper derives general results first for arbitrary continuous (F_B), then specializes them to the multivariate extreme value class and further to the i.i.d. extreme value case, where the formulas become especially simple. 

# Data

There are no data. This is a pure theory paper. It contains no empirical estimation, no sample description, and no country-specific application. The examples are analytical illustrations of special cases such as nested logit and multinomial logit. 

# Identification logic

This is not an identification paper in the econometric sense. The paper assumes a random utility model is given and derives welfare objects implied by that model. The main assumptions are continuity of the deterministic utility components, strict monotonicity in income, and a continuous joint distribution for the utility shocks. 

In the baseline setup, the random terms are assumed not to change when prices or policy attributes change. The paper explicitly notes that this is natural if the shocks represent tastes, but more restrictive if they also capture unmeasured attributes altered by policy. The authors discuss this assumption rather than empirically test it. 

# Estimation / empirical strategy

There is no estimation. The paper’s method is analytical derivation. It first derives the cdf of the expenditure function and Hicksian choice probabilities in the general random utility case, then derives the corresponding objects conditional on utility being fixed at the initial level after a price or policy change, and finally specializes the formulas to the GEV and i.i.d. extreme value cases. 

The practical value of the paper is that it replaces approximation-heavy welfare analysis with exact formulas. In the GEV case the formulas simplify substantially, and in some cases no numerical integration is needed for the joint density results. 

# Treatment of preferences

Preferences enter through the deterministic utility components (v_j(w_j,y)), which are allowed to be nonlinear in income. This is the paper’s decisive generalization beyond the standard linear-income case. 

The paper also discusses an extension with random coefficients, writing (v_j(w_j,y;\beta)) with (\beta) random. In that case, the main results continue to hold conditionally on (\beta), and unconditional objects are obtained by integrating over the distribution of (\beta). This broadens the framework but does not turn the paper into a preference-heterogeneity normative analysis. 

# Treatment of opportunities / constraints

This section is not central in the way it is in RURO or latent-jobs papers.

The paper takes the feasible choice set (B) as given and studies welfare objects conditional on that choice model. It does not model job offer processes, opportunity sets, hours restrictions, rationing, or latent jobs as structural objects. 

It can accommodate changes in the available set of alternatives, and the paper explicitly discusses how to treat the entry or removal of an alternative by using very unfavorable utility/price values. But this is not an opportunity model; it is a welfare-calculus paper built on a pre-specified discrete-choice structure. 

# Welfare / normative object

The welfare object is money-metric and Hicksian. The paper defines the random expenditure function, derives Hicksian choice probabilities, and then uses these objects to derive the distributions of compensating variation and equivalent variation. This is the exact normative content of the paper. 

The paper is explicitly about welfare measurement, but at the individual level. It does not define a social welfare function or interpersonal comparability criterion. Its contribution is to make individual money-metric welfare analysis exact and tractable in nonlinear-income random utility models. 

# Main findings

First, the paper shows that the random expenditure function has a simple distributional characterization. If (Y_B(w,u)) is the expenditure required to reach utility level (u), then
[
P(Y_B(w,u)<y)=1-F_B\big(u-v_1(w_1,y),\dots,u-v_m(w_m,y)\big).
]
This is one of the paper’s central results. 

Second, Hicksian choice probabilities can be written as a one-dimensional integral involving the joint density of the utility shocks and the derivative of the deterministic utility of the chosen alternative with respect to income. This gives an exact analogue of compensated demand in a random utility discrete-choice framework. 

Third, the paper derives exact formulas for the distribution of expenditure and choices after a price or policy change, conditional on utility being fixed at the initial level. This immediately yields exact formulas for the distributions of compensating variation and equivalent variation. 

Fourth, the paper derives a probabilistic or aggregate version of Shephard’s Lemma: under the price-user-cost structure (v_j(w_j,y)=\psi_j(y-w_{1j},w_{2j})), the derivative of expected expenditure with respect to the price of alternative (j) equals the Hicksian choice probability for (j). This is one of the most elegant results in the paper. 

Fifth, in the multivariate extreme value case, and especially in the i.i.d. extreme value case, the formulas simplify substantially. For multinomial logit-type models, the distribution of the expenditure function becomes especially tractable, and the paper shows how known linear-income expressions fit into this broader nonlinear-income framework. 

# Main limitations

A first limitation, relative to your interests, is that the paper is not about labor supply, opportunity sets, or constrained job choice. It is a welfare-methods paper for discrete choice more generally. 

A second limitation is that the framework is purely individual and money-metric. It does not address interpersonal comparability, heterogeneous preferences as a normative problem, or fairness-sensitive welfare metrics. 

A third limitation is that the paper takes the behavioral model as given. If the underlying random utility model already conflates preferences and opportunities, the welfare objects derived here will inherit that conflation. 

A fourth limitation is the maintained assumption that the policy change does not alter the random utility shocks in the main framework. The paper discusses why this may be restrictive when shocks include unmeasured attributes affected by policy. 

# Relevance for my JMP

## possible use for framing

This paper is useful if your JMP has a welfare-measurement layer built on a discrete-choice model. It gives you a rigorous reason to say that exact Hicksian welfare objects are available even when utility is nonlinear in income, so one need not rely on linear-income log-sum shortcuts. 

## possible use for model design

If you estimate a structural labor supply or RURO model and want compensating variation or equivalent variation, this paper can supply the welfare-calculus layer. It is especially useful if your model does not have linear utility in income. 

## possible use for identification

It has limited direct use for identification. Its role is downstream rather than upstream: once the behavioral model is specified and estimated, this paper tells you how to compute exact Hicksian welfare objects from it. 

## possible use for welfare measurement

This is the paper’s strongest use for your project. It provides an exact money-metric welfare apparatus for discrete-choice models, including distributions of compensating variation and joint distributions with initial and post-policy choices. 

## possible use for cross-country comparison

Indirectly useful. If you estimate comparable discrete-choice models across countries, this paper provides a common welfare-calculus framework for deriving country-specific EV/CV objects. But it does not itself solve the cross-country comparability problem. 

# Research questions this paper inspires

How different are welfare rankings of tax-benefit reforms when one computes exact nonlinear-income compensating variation rather than using linear-income or log-sum approximations?

Can this Hicksian welfare machinery be combined with a RURO labor supply model in which the underlying choice objects are jobs rather than hours bundles?

How sensitive are money-metric welfare conclusions to whether the underlying discrete-choice model treats opportunities explicitly or absorbs them into preferences?

Can one move from the individual Hicksian welfare objects derived here to an interpersonal welfare measure that remains credible under heterogeneous preferences? 

# Challenge to this paper

The strongest omission, from your perspective, is that the paper assumes the behavioral model is already correctly specified. It gives an elegant welfare calculus for discrete choice, but it does not ask whether the underlying choice model confounds tastes, constraints, and opportunities. A future paper could challenge this by combining Dagsvik–Karlström-style exact Hicksian welfare with an opportunity-sensitive behavioral model such as RURO. 

# Relation to Bargain et al. (2013)

The relation is methodological rather than substantive. Bargain et al. (2013) is a structural labor supply and welfare-comparison paper, whereas Dagsvik and Karlström derive exact Hicksian welfare objects for generic discrete-choice models with nonlinear income. So this 2005 paper is not a direct competitor to Bargain et al.; it is better read as a welfare-calculus tool that could sit underneath later applied welfare analyses. Relative to Bargain et al. (2013), it is stronger on exact money-metric discrete-choice welfare formulas and weaker on heterogeneous preferences, labor supply behavior, and cross-country normative interpretation. 

# Relation to opportunities vs preferences

This paper does not itself help separate preferences from opportunities. It assumes a discrete-choice random utility model and then derives welfare objects from that model. So if the underlying model already conflates opportunities with tastes, the derived compensating variation will inherit that structure. For your agenda, the paper is therefore valuable as a welfare-calculus layer, but not as a solution to the preferences-versus-opportunities problem. 

# Useful quotations / formulas

The cdf of the expenditure function is
[
P(Y_B(w,u)<y)=1-F_B\big(u-v_1(w_1,y),u-v_2(w_2,y),\ldots,u-v_m(w_m,y)\big).
]
This is the central result linking the expenditure function directly to the joint distribution of the utility shocks. 

Hicksian choice probabilities are defined as
[
P_B^h(j,w,u)=P!\left(J_B(w,Y_B(w,u))=j\right),
]
and are shown to equal
[
P_B^h(j,w,u)=\int_0^\infty F_j^B\big(u-v_1(w_1,y),\ldots,u-v_m(w_m,y)\big),v_j(w_j,dy),
]
which is the paper’s exact compensated-demand formula in the general case. 

Compensating variation is defined by
[
cv=y^1-Y_B!\left(w,V_B(w^0,y^0)\right),
]
so once the distribution of the expenditure function is known, the distribution of compensating variation follows immediately. 

Under the price-user-cost structure, the paper derives an aggregate Shephard’s Lemma:
[
\frac{\partial E,Y_B(w,u)}{\partial w_{1j}} = P_B^h(j,w,u).
]
This is one of the most useful summary formulas in the paper. 

# Suggested tags

#compensating_variation #equivalent_variation #Hicksian_demand #random_utility #discrete_choice #nonlinear_income #welfare_measurement #GEV #multinomial_logit #theory

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That discrete-choice models with utility nonlinear in income still admit exact Hicksian welfare analysis—so once the behavioral model is in place, compensating variation and equivalent variation can be derived rigorously rather than approximated.
