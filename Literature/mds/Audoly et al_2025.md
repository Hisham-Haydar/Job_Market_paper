---

title: "A Practitioner’s Note on the Shapley-Owen-Shorrocks Decomposition"
authors: ["Richard Audoly", "Rory McGee", "Sergio Ocampo", "Gonzalo Paz-Pardo"]
year: 2025
outlet: "Federal Reserve Bank of New York Staff Reports, No. 1163"
country_or_context: "General methodological note; no single-country empirical setting"
population: "[not applicable; methodological paper]"
data_period: "[not applicable]"
shelf: "decomposition_methods_structural_models"
tags: ["Shapley decomposition", "Owen value", "Shorrocks decomposition", "methodology", "structural models", "nonlinear decomposition", "R-squared decomposition", "welfare decomposition"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Audoly, Richard, Rory McGee, Sergio Ocampo, and Gonzalo Paz-Pardo. 2025. “A Practitioner’s Note on the Shapley-Owen-Shorrocks Decomposition.” *Federal Reserve Bank of New York Staff Reports* No. 1163, August 2025. 

# One-sentence contribution

The paper provides a compact practitioner-oriented exposition of the Shapley-Owen-Shorrocks decomposition, emphasizing its usefulness for additive, order-invariant decomposition of nonlinear outcomes in structural economic models. 

# Why this paper matters

This paper matters because it is a methodological bridge between the abstract Shapley-value literature and the practical needs of economists working with nonlinear counterfactuals, rich structural models, and grouped factors. Its main value is not theoretical novelty in the narrow sense, but transparent implementation and interpretation. 

For your project, the paper is especially useful for decomposition. It is directly relevant if you later want to decompose an aggregate welfare or inequality object generated from a (W(z,R,A;y))-type framework into components attributable to preferences, opportunities, pay schedules, taxes, prices, or grouped model blocks. That is an inference for your project; the paper itself does not study (W(z,R,A;y)). 

# Core research question

How can one decompose a nonlinear aggregate outcome into contributions of inputs or groups of inputs in a way that is additive, symmetric with respect to elimination order, and interpretable for practical empirical and structural work? 

# Economic setting and context

This is a methodological note, not a substantive paper on labor markets, welfare policy, or a specific country. The context is the frequent need in economics to decompose nonlinear objects—such as counterfactual outcomes, inequality statistics, (R^2), or structural model outputs—into contributions of multiple interacting inputs. 

The authors explicitly motivate the note by the prevalence of nonlinear aggregation in structural models of economic decision-making and by what they see as underuse of the decomposition in economics despite its practical value. Pages 1–3 are especially clear on this motivation. 

# Model / theoretical framework

The model class is a general decomposition framework for arbitrary functions
[
Y=f(X_1,X_2,\dots,X_n),
]
where the goal is to assign to each input (X_j) a contribution (C_j) to the overall outcome. The problem arises because when (f) is nonlinear, the contribution of (X_j) depends on the order in which other inputs are “zeroed out” or removed. The Shapley-Owen-Shorrocks approach resolves this by averaging marginal contributions over all possible elimination orders. Pages 4–5 define this formally. 

The framework is neither a behavioral model nor a welfare theory. It is a methodological accounting tool. It can be applied to regression outputs, counterfactuals from structural models, inequality measures, or welfare calculations, but it does not itself specify agents, choice sets, utilities, or feasible opportunities. 

The paper also discusses grouped factors. Following Owen’s extension of Shapley to unions of players, the decomposition can attribute outcomes not only to single inputs but also to groups of inputs that move jointly, such as prices, policy functions, or initial conditions. This is particularly relevant for structural counterfactuals. 

# Key objects

The key objects are the outcome function (f(X_1,\dots,X_n)), the individual contributions (C_j), the collection of sub-models that exclude a given input, and the Shapley-Owen-Shorrocks contribution formula:
[
C_j
===

\sum_{k=0}^{n-1}
\frac{(n-k-1)!k!}{n!}
\left(
\sum_{s\subseteq S_k\setminus{X_j}:|s|=k}
[f(s\cup{X_j})-f(s)]
\right).
]
This is the central formula of the note, on pages 4–5. 

A second key object is the reference or null model. The decomposition is additive relative to the value of the model when all factors are at their null values. In the nonlinear toy example, this null model is (f(\emptyset_1,\emptyset_2,\emptyset_3)); in the (R^2) example it is (R^2(\emptyset)=0). Pages 8–10 explain this clearly. 

The paper also provides an implementation object in the form of Matlab code on page 14, which is useful practically because it maps the theoretical decomposition into a simple algorithm over a binary matrix of included inputs and a vector of function values over all sub-models. 

# Data

The paper contains no original microdata or substantive empirical application. It is a methodological note illustrated with toy examples and references to existing applications in the literature. 

# Identification logic

There is no econometric identification strategy in the usual sense. The method is deterministic once the analyst has specified three things: the outcome function (f), the set or grouping of inputs to be treated as players, and the reference/null values used when inputs are removed. The decomposition then mechanically assigns contributions by averaging marginal effects across orders. 

The important implication is that substantive interpretation depends entirely on model design upstream of the decomposition. If the outcome function or the null values are poorly chosen, the decomposition remains exact but may not be economically meaningful. This is a reasonable inference from the paper’s framework rather than a separately proved theorem in the note. 

# Estimation / empirical strategy

There is no estimation. The strategy is expository. The authors first define the decomposition and its properties, then work through a linear example, a nonlinear interaction example, and an (R^2) decomposition example, before closing with discussion of applications and a Matlab implementation. Pages 6–11 are the main worked-out examples; page 14 contains the code. 

# Treatment of preferences

Preferences are not modeled. They can enter only indirectly if an analyst chooses a function (f) that depends on preferences or preference-related parameters. The note itself does not define utility, preference heterogeneity, or labor-supply tastes. 

For your purposes, this means the paper is not useful for estimating or interpreting preferences directly. Its usefulness begins only after a model has already delivered an outcome that depends on preference objects. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly. It has no concept of feasible job sets, latent offers, hours restrictions, or demand-side labor-market constraints. It is not a job-choice paper. 

Its relevance to opportunities is therefore purely methodological. If a separate model has already represented opportunities—for example through feasible sets (A), latent opportunity densities, or circumstance-type partitions—then this decomposition can be used to quantify their contribution to an aggregate outcome. That is a reasonable inference for your project, not something the paper itself implements. 

# Welfare / normative object

The paper does not propose a welfare criterion, a well-being measure, or a fairness principle. It is a decomposition note. However, the authors explicitly mention welfare decompositions from counterfactual exercises as a promising application, including cases where changes in aggregate levels and distributions of consumption and leisure are separated. Page 11 is especially relevant here. 

So the paper is not itself normative, but it is highly useful for normative work once a welfare object has already been defined elsewhere. In your terms, it can support decomposition of a welfare or inequality statistic, but not the prior justification of that statistic. 

It does not address responsibility for opportunities, compensation for opportunities, or reference opportunity sets directly. Any such interpretation would have to come from the substantive model being decomposed. 

# Main findings

The main methodological finding is that the Shapley-Owen-Shorrocks decomposition is the unique decomposition satisfying four desirable properties: exact decomposition under addition, symmetry with respect to factor order, zero contribution for null-effect factors, and linearity of the attribution operator in the outcome function. These properties are stated on pages 4–5. 

The linear example shows that in the special case of a linear model, the decomposition coincides with the intuitive additive decomposition because the marginal effect of each input is invariant to elimination order. Pages 6–7 provide this benchmark. 

The nonlinear interaction example is especially useful. For
[
Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3X_2,
]
the decomposition allocates the interaction term symmetrically across the interacting variables, yielding
[
C_2=\beta_2X_2+\frac{1}{2}\beta_3X_2X_3,\qquad
C_3=\frac{1}{2}\beta_3X_2X_3.
]
This is the clearest practical illustration of why order averaging matters in nonlinear settings. Pages 7–9 develop this result. 

The (R^2) example is also important. It shows that the decomposition of (R^2) differs from partial (R^2) because the Shapley-Owen-Shorrocks approach preserves exact additivity and symmetry, whereas partial (R^2) does not generally do so. Pages 9–10 make this contrast explicitly. 

Finally, the paper’s closing discussion argues that the method is particularly useful in rich structural models and welfare counterfactuals, and that grouped-factor versions can control computational cost when there are many inputs. Page 11 summarizes this perspective. 

# Main limitations

The first limitation is that the paper is purely methodological. It does not tell the reader how to define economically meaningful factors, how to choose null values, or how to interpret grouped decompositions ethically. Those are substantive modeling decisions left to the user. 

A second limitation is computational. The number of sub-models grows exponentially with the number of inputs, (2^n), so exact implementation can become costly. The authors note that judicious grouping of factors can mitigate this. This is discussed on page 11 and made concrete by the Matlab implementation on page 14. 

A third limitation for your project is that the paper provides no direct guidance on decomposing objects like (W(z,R,A;y)). It can be used once such an object or an aggregate statistic derived from it exists, but it does not help define the welfare measure itself or justify the ethical meaning of decomposed components. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing the decomposition component of your JMP. It gives you a clean methodological language for saying that nonlinear outcomes generated by structural models require order-invariant decomposition if one wants additive and interpretable contributions. 

## possible use for model design

Indirectly useful. It suggests that if you want later decomposition, you should design your model so that the objects to be decomposed—preferences, opportunities, pay schedules, taxes, prices, demographics, or grouped parameter blocks—are clearly separable computationally. That is a reasonable inference for your project. 

## possible use for identification

Limited directly. The paper offers no causal or econometric identification guidance. Its contribution is downstream of identification: once an outcome has been computed, it tells you how to attribute it across interacting factors. 

## possible use for welfare measurement

Indirect but important. It is not a welfare-measurement paper, but it is highly relevant once you have an aggregate welfare or inequality object that you want to decompose without arbitrary order effects. 

## possible use for decomposition

This is its strongest use for your JMP. It is essentially a manual for performing exact nonlinear decomposition, including grouped decompositions, in structural contexts. 

## possible use for comparative application

Potentially very useful. If your project later compares countries, cohorts, or policy regimes, the same decomposition could be applied to cross-context differences in a common structural outcome or welfare statistic. That is a reasonable inference rather than an explicit application in the note. 

# Research questions this paper inspires

Can inequality in an aggregate welfare statistic built from (W(z,R,A;y)) be decomposed additively into the contributions of (R), (A), (y), and their grouped subcomponents using the Shapley-Owen-Shorrocks method?

What is the economically defensible null model when “removing” opportunity sets (A) in a jobs-and-wellbeing decomposition: universal access, reference access, or no access?

Should grouped decomposition in a structural labor model treat tax policy, pay schedules, and opportunity sets as separate players, or should some be grouped jointly because they move together empirically?

How sensitive are welfare decompositions to alternative factor groupings when a structural model has many interacting primitives?

Can one combine the lower-bound logic of opportunity measurement papers with Shapley-Owen-Shorrocks decomposition so that only observed opportunity components are decomposed explicitly?

# Challenge to this paper

The main challenge is that the method is formally attractive but substantively agnostic. It guarantees additive and symmetric attribution once the model and the factors are chosen, but the hard economic question often lies precisely in how those factors should be defined and what “removing” one of them means. For projects like yours, this is not a fatal weakness, but it means the decomposition can only be as convincing as the substantive model underneath it. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper provides a general decomposition method for arbitrary nonlinear functions and explicitly argues that it is especially well suited to rich structural models and welfare decompositions. It also allows grouped factors to move together, which is useful when model components are naturally bundled. 

[reasonable inference for my project] This is directly relevant if your framework eventually generates an aggregate outcome—such as inequality in (W(z,R,A;y)), average welfare differences across policies, or welfare gaps across groups—and you want to attribute it to preferences (R), feasible opportunities (A), pay schedules (y), and other components without arbitrary ordering. 

[unclear from paper] The paper does not indicate how (z), (R), (A), or (y) should be operationalized as players, nor how the null model should be chosen for a jobs-and-wellbeing application. It also does not address the ethical interpretation of those decomposed contributions. 

[reasonable inference for my project] In your taxonomy, the paper is closest to decomposition of inequality or welfare and to methodological support for grouped counterfactual accounting. It is not close to independence of (A), independence of (y), laissez-faire evaluation, or reference opportunity sets as substantive axioms. Its role would be downstream and methodological. 

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

The paper is not substantively about opportunities versus preferences. It does not define either concept. But it is highly relevant once a separate model has successfully distinguished them, because it gives a principled way to decompose an aggregate statistic across those factors in nonlinear settings. 

For your purposes, this means the paper is not an answer to the opportunities-versus-preferences problem, but a tool for quantifying their relative contribution once the problem has been solved at the modeling stage. That is its correct place in your corpus. 

# Useful quotations / formulas

The master setup is
[
Y=f(X_1,X_2,\dots,X_n),
]
with the aim of decomposing the value of (f) into contributions of the inputs. This is the paper’s core starting point. 

The contribution formula is
[
C_j
===

\sum_{k=0}^{n-1}
\frac{(n-k-1)!k!}{n!}
\left(
\sum_{s\subseteq S_k\setminus{X_j}:|s|=k}
[f(s\cup{X_j})-f(s)]
\right).
]
This is the central practical formula on pages 4–5. 

The (R^2) example is especially useful because it shows that Shapley-Owen-Shorrocks decomposition is not the same as partial (R^2), precisely because it preserves exact additivity and symmetry. Pages 9–10 make this distinction clearly. 

# Suggested tags

Shapley-Owen-Shorrocks, nonlinear-decomposition, grouped-decomposition, structural-model-accounting, welfare-decomposition, R-squared-decomposition, methodology

# My quick takeaway

This is a very useful decomposition-methods paper for your corpus. Its main value is not to define welfare or opportunities, but to provide a clean, interpretable, and additive decomposition method once a nonlinear structural or welfare object has already been built. For your project, it is especially relevant as a downstream tool for decomposing aggregate outcomes across preferences, opportunities, pay schedules, and grouped counterfactual components.
