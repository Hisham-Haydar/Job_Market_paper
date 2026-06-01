---

title: "Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare"
authors: ["Bart Capéau", "Liebrecht De Sadeleer", "Sebastiaan Maes", "André Decoster"]
year: 2021
outlet: "CESifo Working Paper No. 9071"
country_or_context: "Methodological; empirical illustration on Germany"
population: "General discrete-choice framework with unrestricted preference heterogeneity; empirical illustration on single females in Germany"
data_period: "2018 for the empirical illustration"
shelf: "discrete_choice_welfare_measurement"
tags: ["discrete choice", "nonparametric welfare analysis", "money metric utility", "compensating variation", "equivalent variation", "social welfare", "heterogeneous preferences", "reference opportunity sets"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Capéau, Bart, Liebrecht De Sadeleer, Sebastiaan Maes, and André Decoster. 2021. “Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare.” CESifo Working Paper No. 9071. 

# One-sentence contribution

The paper develops a nonparametric framework for measuring individual and social welfare in discrete-choice models with unrestricted unobserved preference heterogeneity, showing how welfare levels, welfare differences, and social welfare can be recovered from choice probabilities and, when needed, transition probabilities. 

# Why this paper matters

This paper matters because it directly addresses one of the central methodological problems in welfare analysis under discrete choice: once preferences are heterogeneous and partly unobserved, welfare measures are themselves stochastic objects from the econometrician’s point of view. The paper shows that one can still recover their distributions nonparametrically, without imposing the strong parametric restrictions that are common in applied work. 

For your project, its importance is especially high on the welfare-measurement side. It is one of the rare papers that connects discrete choice, heterogeneous preferences, money-metric welfare, joint distributions of welfare levels and welfare gains/losses, and social welfare aggregation, while explicitly drawing on Fleurbaey’s broader framework of nested opportunity set welfare measures. 

At the same time, its relevance for your opportunity-set agenda is specific rather than global. It is very useful for **reference opportunity sets as evaluative devices**, but it does **not** model heterogeneous actual feasible job sets in the RURO sense. That distinction has to be kept explicit. 

# Core research question

How can one conduct individual and social welfare analysis in discrete-choice random-utility models while allowing for unrestricted unobserved preference heterogeneity and avoiding strong parametric assumptions, and how can such welfare objects be identified from cross-sectional or panel data? 

# Economic setting and context

The paper is fundamentally methodological. Its main contribution is not tied to one country or one dataset, but to a general discrete-choice random-utility setting with a finite common choice set and a numeraire. The empirical illustration uses German SOEP 2018 data and studies single females choosing among non-work, part-time work, and full-time work under the German tax-benefit system and a counterfactual basic-income flat tax reform. 

The substantive policy context of the illustration is a reform replacing the current nonlinear progressive German income tax schedule with a revenue-neutral flat tax combined with a basic-income-type treatment of social assistance relative to earned income. The application is therefore public-economics oriented, but the theoretical framework is much broader. 

# Model / theoretical framework

The model class is a discrete-choice random-utility model with unrestricted unobserved preference heterogeneity. Each preference type (\omega) has utility (U_c^\omega(y-p_c)) over a finite common choice set (C) and a numeraire, where (y) is exogenous income and (p_c) is the price of alternative (c). The paper assumes continuity and strict monotonicity in the numeraire, negligible probability of ties, exogeneity of budget sets, and a standard random-utility representation of observed choice. 

The core normative framework is built from Fleurbaey-style nested opportunity set (NOS) measures. The paper adapts these measures from a continuous setting to discrete choice. A welfare measure is defined by associating the individual’s indifference set with the largest member of a common family of nested opportunity sets that the individual still weakly prefers no more than her actual situation. In the discrete setting, this produces a welfare measure (W^\omega(y-p_k,k)) that depends on the chosen option and the underlying preference type. 

This framework is both positive and normative. It is positive because it starts from a DC-RUM and links welfare identification to observable choice probabilities and transition probabilities. It is normative because the object of interest is not merely behavior but welfare levels, welfare changes, and social welfare, defined using an evaluative family of reference opportunity sets. 

What the agent chooses is one alternative from a finite common choice set (C). The actual feasible set is therefore common and discrete in the baseline theory. Opportunities are modeled explicitly only in the **evaluative** sense of common nested reference opportunity sets (B_\lambda), not as heterogeneous actual job sets faced by different individuals. This is a crucial distinction for your project. 

# Key objects

The main preference object is the type-specific utility function (U_c^\omega(y-p_c)). The main behavioral objects are the Marshallian choice probabilities
[
P_i(p,y)=\Pr_\omega!\left[U_i^\omega(y-p_i)\ge \max_{c\neq i}{U_c^\omega(y-p_c)}\right]
]
and the transition probabilities
[
P_{i,j}(p,p',y)=\Pr_\omega!\left[i=J^\omega(p,y),, j=J^\omega(p',y)\right].
]
These are the empirical inputs from which welfare distributions are identified. 

The main welfare object is the discrete NOS measure
[
W^\omega(y-p_k,k)=\max_\lambda\left{\lambda ;|; U_k^\omega(y-p_k)\ge \max_c U_c^\omega(y-\tilde p_c(\lambda))\right},
]
where (\tilde p(\lambda)) is the virtual price vector associated with the common family of nested opportunity sets. 

The paper then treats money metric utility (MMU), compensating variation (CV), equivalent variation (EV), equivalent income, and wage metrics as particular cases or close relatives within this structure. It also defines social welfare as an additively separable function of the welfare distribution. 

# Data

The theory is not tied to one dataset, but the empirical illustration uses the 2018 German SOEP. The estimation sample consists of single females available to the labour market, under age 60, after trimming outliers in wages and asset income and dropping missing-hours observations. The final subsample contains 1,922 single females. Appendix C.1 gives the sample description. 

Observed labour supply is discretized into three alternatives: non-working, part-time, and full-time. Disposable incomes for these alternatives are computed using a tax-benefit calculator. Missing wages for nonworkers are imputed using a Heckman-type selection model. The policy experiment compares the baseline German system with a counterfactual flat-tax-plus-basic-income reform. 

# Identification logic

The identification strategy is the paper’s central methodological contribution. It does **not** identify primitive deterministic preferences and the distribution of unobserved heterogeneity separately. Instead, it identifies the distributions of welfare objects directly as functionals of choice and transition probabilities. This is an important conceptual choice: the paper identifies the welfare statistics of interest without fully recovering the underlying structural primitives. 

The fundamental insight is that the event “welfare exceeds a threshold” can be rewritten as an event about optimal choice under a counterfactual virtual price vector associated with the welfare metric. This turns welfare-distribution questions into choice-probability evaluations at actual and virtual prices. That is the key lemma underlying the whole framework. 

For welfare **levels**, cross-sectional data with sufficient relative price variation are enough because the relevant distributions can be expressed through ordinary choice probabilities. For welfare **levels jointly with welfare differences**, panel data identify the relevant transition probabilities; when only cross-sections are available, the paper derives set-identification using Boole-Fréchet inequalities and stochastic revealed-preference restrictions. This is a major practical contribution. 

The crucial assumptions are strong and explicit: the budget set must be exogenous; the utility function must be continuous and strictly increasing in the numeraire; ties between alternatives must have probability zero; and preference types must be unchanged by the price change when transition probabilities are used for welfare-difference analysis. The paper is therefore nonparametric in preferences, but not assumption-free. 

# Estimation / empirical strategy

At the theoretical level, implementation requires nonparametric estimation of choice probabilities and, when needed, transition probabilities. The paper emphasizes that standard nonparametric regression tools can be used because choice probabilities are conditional expectation objects. It also discusses shape restrictions implied by utility maximization, such as own-price monotonicity and cross-price effects on choice probabilities. 

In the German illustration, the authors use a semiparametric sieve-type approximation rather than a fully unrestricted estimator, mainly to handle dimensionality. They estimate flexible binary logits for part-time and full-time choices, using cubic polynomials in disposable income for all three alternatives and a linear demographic index. Shape restrictions are imposed by a penalty function. Appendix C.2 details the implementation. 

Social welfare is then computed by integrating the identified welfare distribution against an inequality-averse transformation, including Atkinson-type examples. Welfare gains and losses conditional on baseline welfare are obtained by numerically approximating the joint distribution of welfare levels and welfare changes. 

# Treatment of preferences

Preferences are treated with unusual generality. The paper allows unrestricted, unobserved preference heterogeneity across individuals, encoded in the preference type (\omega). This is one of its main virtues. In contrast to much applied welfare work, it does not impose a specific additive-logit or other narrow parametric structure on tastes in order to derive welfare distributions. 

At the same time, the paper is still squarely preference-based in the welfare-economics sense. Welfare measures are built from indifference comparisons relative to reference opportunity sets. The authors explicitly argue that NOS measures are ethically attractive because they compare individuals in a way that respects their preferences while avoiding cruder comparisons based only on income or subjective satisfaction. 

This means the paper is highly relevant for welfare measurement under heterogeneous preferences. It is much less about explaining where preferences come from or separating preference heterogeneity from opportunity heterogeneity in the labour-market sense. 

# Treatment of opportunities / constraints

This section is crucial for your project, and the paper requires careful reading here. The paper does **not** model heterogeneous actual feasible job sets, latent job arrivals, or labour-demand-side constraints. The actual choice set is a finite common set (C), shared across individuals in the core theory. Prices and exogenous income define the budget environment, but the paper is not a RURO or latent-jobs paper. 

However, the paper does make opportunities central in a different sense: welfare is measured through **nested opportunity sets** used as common evaluative benchmarks. These are not empirical opportunity sets (A_i) faced by different persons; they are reference opportunity sets (B_\lambda) used to cardinalize preferences and compare well-being across heterogeneous individuals. This is directly relevant to your interest in reference opportunity sets, but it should not be confused with opportunity heterogeneity in the actual labor-market environment. 

Accordingly, the paper helps distinguish **preference heterogeneity** very strongly, but it does **not** distinguish empirical opportunity heterogeneity from preference heterogeneity in the way RURO papers do. The main “constraints” are the finite choice set, prices, exogenous income, and the researcher-chosen family of reference opportunity sets. 

# Welfare / normative object

The paper is explicitly normative and econometric at once. Its main normative object is the class of discrete nested opportunity set welfare measures, with money metric utility as the leading special case. Welfare differences are then defined through changes in these measures, and social welfare is constructed by aggregating the resulting welfare distribution with a concave social aggregator. 

This is therefore not a paper that merely appends compensating variation to a structural demand model. It studies **levels** of welfare, **differences** in welfare, the **joint distribution** of levels and differences, and **social welfare**. That is a much richer normative program than most applied discrete-choice welfare papers. 

The paper is also directly relevant for decomposition in one important sense: it derives the joint distribution of baseline welfare and welfare gains/losses, allowing one to ask whether winners from a reform were initially well-off or badly off. This is not a decomposition into opportunities and preferences, but it is a meaningful welfare-incidence decomposition. 

On the other hand, the paper is not about responsibility for opportunities, compensation for unequal feasible sets, or axioms governing actual versus reference opportunity sets. It operates at the level of welfare measurement under preference heterogeneity, not fairness decomposition by sources of disadvantage. 

# Main findings

The main theoretical finding is that for the broad class of discrete nested-opportunity-set welfare measures, marginal, conditional, and joint welfare distributions can be expressed as functionals of observed choice probabilities and, for welfare differences, transition probabilities. This includes MMU, CV, EV, equivalent income, wage metrics, and social welfare. 

A second major finding is that these welfare objects can be identified nonparametrically from observational data. Welfare levels are point-identified from cross-sectional data with sufficient price variation. Joint distributions of welfare levels and welfare differences are point-identified from panel data, and when only cross-sections are available, the paper derives informative bounds using Boole-Fréchet inequalities and stochastic revealed preference restrictions. 

In the German illustration, the authors find that around 25% of single females have a welfare distribution that degenerates to a step function, so their welfare level can be determined exactly despite unobserved heterogeneity. This occurs especially for low-wage individuals choosing full-time work and high-wage individuals choosing non-work. The figures around page 30 and the discussion immediately following are central here. 

Aggregating by choice and wage quartile, the paper finds that among high-wage women, those choosing full-time work tend to dominate those choosing part-time, who in turn dominate non-workers in first-order welfare terms. For low-wage women, the pattern reverses: low-wage full-timers tend to be worse off because their preferences are less aligned with their poor earnings opportunities. Figure 5 on page 31 summarizes this. 

At a more aggregated level, the welfare distribution of the highest wage quartile tends to first-order dominate the distributions of the lower quartiles, whereas the lower three quartiles are more intermingled. The paper interprets this as evidence that wages matter, but unobserved preferences still play a major role. Figure 6 on page 32 is the key visual result. 

For the reform experiment, the overall reform welfare distribution first-order dominates the baseline welfare distribution. This implies unanimous improvement for the entire class of additively separable, inequality-averse social welfare functions considered. Figure 7 on page 33 and Table 4 in Appendix C.5 support this conclusion. 

Yet the reform is not Pareto-improving. Around 15% of single females lose, and these losers are disproportionately concentrated among the initially well-off. Large gains are more prevalent among the initially poor; among the bottom two-thirds of the baseline welfare distribution, almost 98% gain. Figure 8 on page 34 and Table 1 on page 34 provide the core evidence. 

# Main limitations

The first limitation is that the framework is built for **discrete choice with a common finite choice set**. This is powerful and clean, but it is not a model of heterogeneous actual opportunity sets, latent jobs, or labour-market rationing. For your (W(z,R,A;y)) agenda, the paper is therefore strongest on (W) and (R), but weak on empirical (A). 

A second limitation is the exogeneity requirement on prices and income. The paper acknowledges that endogeneity is a serious issue and suggests control-function approaches for some cases, but the core identification results rely on budget-set exogeneity. This is a substantial empirical restriction. 

A third limitation is scope. The strongest results concern price changes. The paper itself notes that extending the analysis to changes in other attributes of alternatives, or to the introduction/removal of alternatives, is a future research direction and likely leads to set-identification rather than point-identification. 

A fourth limitation is that the normative content still depends on the researcher’s choice of welfare metric and, for MMU, on the choice of reference prices. The authors explicitly note that empirical welfare estimates may be sensitive to that choice. This is not a flaw unique to the paper, but it is important. 

A fifth limitation is that the empirical illustration, while useful, is not fully nonparametric in implementation. It uses a semiparametric sieve-style estimator with penalty-based shape restrictions. So the paper’s identification results are more general than the particular empirical implementation. 

Finally, for your decomposition interests, the paper does not separate welfare inequality into preferences, opportunities, and pay schedules. It instead studies the distribution of welfare and reform-induced welfare changes. That is valuable, but different from your decomposition target. 

# Relevance for my JMP

## possible use for framing

This paper is extremely useful for framing a welfare-measurement component of your JMP. It provides a rigorous language for saying that welfare under heterogeneous preferences should be represented by distributions, not just point estimates, and that one can study who gains from reforms relative to who was initially well-off. 

## possible use for model design

It is useful if your empirical design retains a discrete-choice structure and you want a welfare analysis that does not inherit the full rigidity of parametric logit-style assumptions. It is less useful for model design on the opportunity-set side, because it does not estimate heterogeneous feasible job sets. 

## possible use for identification

Very high relevance. The paper shows how welfare distributions can be identified from choice probabilities and transition probabilities rather than from fully recovered preference primitives. It also gives a practical strategy for bounding transition-based welfare objects when only cross-sectional data are available. 

## possible use for welfare measurement

This is the strongest relevance margin. The paper is directly about welfare levels, welfare changes, and social welfare under heterogeneous preferences in discrete choice. It is one of the closest papers in your corpus to the measurement side of your project. 

## possible use for decomposition

It does not provide the (R)-(A)-(y) decomposition you ultimately want. But it does provide a powerful decomposition-style tool: the joint distribution of baseline welfare and welfare gains/losses, which lets you ask whether reform winners were initially advantaged or disadvantaged. That can be useful in a later stage of your project. 

## possible use for comparative application

The theory is portable across policy environments as long as comparable discrete-choice data and sufficient price variation are available. It is therefore suitable for comparative tax-benefit or labor-supply welfare applications, though not immediately for cross-country comparisons of heterogeneous actual opportunity sets. 

# Research questions this paper inspires

Can one construct a welfare measure (W(z,R,A;y)) that combines Capéau et al.’s nonparametric identification of welfare distributions with a separately estimated heterogeneous feasible set (A_i)?

What changes when the evaluative reference opportunity sets used in NOS measures are replaced by ethically relevant reference **job** sets rather than generic discrete alternatives?

Can the joint distribution of baseline welfare and welfare gains/losses be extended to decompose gains by differences in realized pay schedules (y), preferences (R), and feasible job sets (A)?

How sensitive are welfare rankings and reform-incidence conclusions to the choice of reference prices or to the choice of NOS metric?

Can RURO-style models of latent job opportunities be combined with nonparametric NOS-based welfare analysis so that welfare is not only preference-sensitive but also explicitly opportunity-sensitive?

# Challenge to this paper

The strongest challenge is that the paper’s elegant welfare identification rests on a common discrete choice set and on researcher-chosen reference opportunity sets. That makes it highly valuable for welfare analysis under heterogeneous preferences, but less convincing for projects where unequal **actual** opportunities are the central normative object. In other words, the paper solves an important part of the welfare-measurement problem, but not the problem of normatively evaluating heterogeneous feasible sets themselves. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper constructs individual welfare measures for discrete choice under heterogeneous preferences and shows how their distributions can be recovered from observed choice probabilities. Its main objects are the chosen alternative, the budget environment, and common reference opportunity sets used for welfare measurement. 

[reasonable inference for my project] A natural translation into your notation is the following. The realized bundle (z) corresponds to the chosen alternative together with the associated numeraire level; (R) corresponds to the individual preference type (\omega); (y) corresponds to the income-price environment that determines the disposable numeraire attached to each alternative; and the paper’s analogue of (A) is **not** an individual actual feasible set but a common evaluative family of nested reference opportunity sets (B_\lambda). This means the mapping is only partial. supported by 

[explicit in paper] The paper is closest to **reference opportunity sets** and to welfare measurement under heterogeneous preferences. It is not a paper about latent job availability, actual heterogeneous feasible sets, or labour-demand constraints. 

[unclear from paper] The paper does not analyze whether welfare should satisfy independence of (A), independence of (y), responsibility for opportunities, responsibility for acquired ability, or laissez-faire evaluation. It does not formulate axioms of the kind used in your jobs_and_wellbeing project. 

[reasonable inference for my project] Relative to your framework, this paper is therefore most useful as a welfare-measurement module that could be embedded into a richer opportunity-sensitive model. It is much closer to reference-based evaluation and reform-incidence analysis than to a direct normative theory of heterogeneous actual job sets. supported by 

# Relation to Bargain et al. (2013)

This paper is methodologically related to the benchmark labour-supply welfare literature rather than tied to one particular empirical application. Relative to parametric structural studies of labour supply and welfare under heterogeneous preferences, its distinctive contribution is to recover welfare distributions nonparametrically from choice probabilities instead of imposing a tight parametric structure on preferences. It is also broader on the welfare-measurement side because it studies not only welfare changes such as CV or EV, but also welfare levels and the joint distribution of levels and changes. [reasonable inference for my project] supported by 

# Relation to opportunities vs preferences

This paper is much stronger on the **preferences** side than on the **opportunities** side as you define that distinction. It allows unrestricted, unobserved preference heterogeneity and then shows how welfare can still be compared across individuals in a disciplined way. 

Its notion of opportunity is evaluative and common: nested opportunity sets used as welfare benchmarks. It does not study actual heterogeneous opportunities faced by different individuals in the labour market. So it is highly relevant for reference-based welfare measurement, but only weakly relevant for separating actual opportunity heterogeneity from preference heterogeneity. 

That said, it may still be very useful for your project because it clarifies how one can compare welfare across heterogeneous preferences once one has chosen an ethically acceptable reference structure. The missing step, from your perspective, is to connect that reference structure to heterogeneous actual job sets (A_i). [reasonable inference for my project] supported by 

# Useful quotations / formulas

The key discrete NOS welfare measure is
[
W^\omega(y-p_k,k)=\max_\lambda\left{\lambda ;|; U_k^\omega(y-p_k)\ge \max_c U_c^\omega(y-\tilde p_c(\lambda))\right}.
]
This is the central bridge from welfare measurement to observable choice probabilities. 

The key choice-probability object is
[
P_i(p,y)=\Pr_\omega!\left[U_i^\omega(y-p_i)\ge \max_{c\neq i}{U_c^\omega(y-p_c)}\right].
]
The paper’s identification strategy works by rewriting welfare events as choice events at counterfactual virtual prices. 

For social welfare, the paper proposes an additively separable aggregate of the welfare distribution:
[
SWF=\int!!\int h(w),dF_W(w\mid p,y),dG(p,y).
]
This is important because it connects individual welfare measurement directly to social evaluation. 

Empirically, Figure 8 on page 34 is especially useful: it plots welfare gains and losses conditional on baseline welfare and shows that losses are concentrated much more among those initially better off. 

# Suggested tags

nonparametric-welfare-analysis, discrete-choice, nested-opportunity-sets, money-metric-utility, compensating-variation, equivalent-variation, social-welfare, heterogeneous-preferences, reform-incidence

# My quick takeaway

This is a core paper for the welfare-measurement side of your research corpus. It does not solve the empirical opportunity-set problem that is central to RURO or to your (W(z,R,A;y)) framework, because actual heterogeneous (A_i) are largely absent. But it makes a major contribution to something you also need: how to measure, compare, and aggregate welfare under heterogeneous preferences in discrete choice without relying on strong parametric assumptions. In your project, it is best seen as a powerful reference-opportunity-set and welfare-identification paper that could later be combined with a richer model of actual job opportunities.
