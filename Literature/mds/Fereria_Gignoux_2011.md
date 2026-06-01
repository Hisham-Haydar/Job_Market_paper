---

title: "The Measurement of Inequality of Opportunity: Theory and an Application to Latin America"
authors: ["Francisco H. G. Ferreira", "Jérémie Gignoux"]
year: 2011
outlet: "Review of Income and Wealth"
country_or_context: "Brazil, Colombia, Ecuador, Guatemala, Panama, and Peru"
population: "Household heads and spouses aged 30–49 with positive income/consumption and observed circumstances; labor-earnings results also reported for occupied individuals"
data_period: "Brazil 1996; Colombia 2003; Ecuador 2006; Guatemala 2000; Panama 2003; Peru 2001"
shelf: "inequality_of_opportunity_measurement"
tags: ["inequality of opportunity", "Roemer", "van de Gaer", "between-group inequality", "Latin America", "circumstances", "lower bound", "decomposition"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Ferreira, Francisco H. G., and Jérémie Gignoux. 2011. “The Measurement of Inequality of Opportunity: Theory and an Application to Latin America.” *Review of Income and Wealth* 57(4): 622–657. 

# One-sentence contribution

The paper formalizes a simple scalar measure of inequality of opportunity as between-type inequality when types are defined by predetermined circumstances, shows that it is a lower-bound estimate of true inequality of opportunity, and applies it to six Latin American countries. 

# Why this paper matters

This paper matters because it is one of the clearest bridges between the philosophical and social-choice literature on responsibility versus compensation and an empirically tractable decomposition method. It does not merely apply Roemerian language; it asks what exactly should be measured, proves why the resulting measure is a lower bound, and compares parametric and non-parametric estimators. 

For your project, it is especially important on the decomposition side. It gives a disciplined way to map a normative distinction—circumstances versus effort—into a scalar measure of inequality attributable to morally irrelevant background factors. It is not a job-choice or feasible-set paper, but it is highly relevant for thinking about how a fairness-oriented decomposition can be done once the underlying objects have been chosen. 

# Core research question

How should inequality of opportunity be measured in theory and in practice, and what do lower-bound estimates of that inequality look like across six Latin American countries when opportunities are defined by predetermined circumstances such as family background, ethnicity, birthplace, and gender? 

# Economic setting and context

The paper is situated at the intersection of normative economics, inequality measurement, and empirical development economics. Its applied setting is Latin America, using household surveys from Brazil, Colombia, Ecuador, Guatemala, Panama, and Peru. The advantage variables are household per capita income and, where available, household per capita consumption; labor earnings are also used for a supplementary exercise involving gender. 

The normative context is the opportunity-egalitarian tradition associated with Dworkin, Arneson, Cohen, Sen, Roemer, and van de Gaer. The paper starts from the idea that inequalities due to predetermined circumstances are ethically objectionable, whereas inequalities due to effort may be less objectionable, and then asks how this distinction can be measured with real survey data. 

# Model / theoretical framework

The model class is a measurement framework for inequality of opportunity, not a behavioral labor-supply or structural choice model. Individuals are characterized by an advantage variable (y), a vector of predetermined circumstances (C), and an effort variable (e). The population is partitioned into Roemerian “types,” where people share the same circumstances. Equality of opportunity is related to the idea that the distribution of advantage should not depend on type. 

The paper then weakens the empirical identification criterion for equality of opportunity from equality of conditional distributions across types to equality of conditional means across types. This move connects Roemer’s framework to van de Gaer’s ex-ante approach and leads to a scalar measure based on the inequality of a smoothed distribution in which each individual’s advantage is replaced by the mean advantage of their type. 

The framework is explicitly normative in motivation and measurement-oriented in implementation. There is no agent who chooses from a feasible set, no budget set, and no explicit positive model of preferences or labor supply. The paper is about how to measure unfair inequality, not how choices are generated. 

# Key objects

The key objects are the advantage variable (y), the circumstance vector (C), the effort variable (e), the partition of the population into types (P={T_1,\dots,T_K}), the smoothed distribution ({\mu_i^k}), and the standardized distribution ({\nu_i^k}). These are defined in Section 2. 

The paper defines two central indices. The first is the inequality of opportunity level,
[
\theta_a = I({\mu_i^k}),
]
and the second is the inequality of opportunity ratio,
[
\theta_r = \frac{I({\mu_i^k})}{I(y)}.
]
With path-independent decomposability added to the axioms for the inequality measure (I(\cdot)), both indices are uniquely tied to the mean logarithmic deviation (E_0). This yields the specific measures in equations (5′) and (6′). 

A further important object is the “opportunity-deprivation profile,” which ranks types by mean advantage and identifies the worst-off types in each society. This is introduced in Section 6 and used to summarize which combinations of circumstances characterize opportunity deprivation. 

# Data

The paper uses six nationally representative household surveys: Brazil PNAD 1996, Colombia ECV 2003, Ecuador ECV 2006, Guatemala ENCOVI 2000, Panama ENV 2003, and Peru ENAHO 2001. The main analysis is conducted on household heads and spouses aged 30–49 with positive income or consumption and observed circumstances. Sample sizes with complete information range from about 4,556 in Panama to 70,521 in Brazil, as reported in Tables 1 and 5. 

Advantage is measured as household per capita income and, where available, household per capita consumption expenditure. Circumstances include parental education, father’s occupation, ethnicity or race, region of birth or birth area, and gender, although gender is excluded from the household-level decomposition because household headship is viewed as choice-related. For labor-earnings decompositions, gender is included. Tables 2, 3, and 4 describe the variables and their distributions. 

# Identification logic

There is no causal identification strategy in the quasi-experimental sense. The paper’s object is measurement, not causal effect estimation. The main identification issue is conceptual and statistical: given a set of observed circumstance variables, how much between-type inequality can be attributed to opportunities, and how should this be interpreted when some circumstances are unobserved? 

The paper’s central identification claim is that the proposed indices are lower-bound estimators of true inequality of opportunity. The logic is that any omitted circumstance variable would refine the partition of the population into types, and this can weakly increase between-type inequality in the smoothed distribution. Proposition and corollary in Section 3 establish this result for the non-parametric case, and the same logic is argued for the parametric case. 

Thus, the paper does not identify the full contribution of all morally irrelevant factors. It identifies the contribution of the observed circumstance set as a lower bound on the true opportunity component. This lower-bound interpretation is one of the main theoretical contributions of the paper. 

# Estimation / empirical strategy

The paper implements both non-parametric and parametric estimators. The non-parametric estimator computes between-type inequality directly from the smoothed distribution once the population is partitioned by observed circumstances. This is straightforward but becomes imprecise when the number of types is large and cell sizes are small. 

The parametric estimator instead estimates a reduced-form regression of log advantage on circumstances and uses predicted values to generate a parametric smoothed distribution and a parametrically standardized distribution. Equations (8) through (11′) define these objects. This approach reduces data requirements and is especially helpful when the partition into types is fine but samples are moderate. 

The paper reports both approaches throughout the application and emphasizes that they usually produce similar results. That agreement is used as evidence of robustness, though the authors prefer the parametric lower-bound estimates when samples are smaller and cell sparsity is more severe. Table 6 is central for these results. 

# Treatment of preferences

Preferences are not modeled. There is no utility function, no heterogeneity in tastes, and no behavioral model from which effort is derived. Effort appears as a conceptual category inherited from the normative literature, but the empirical implementation does not require observing or estimating preferences directly. 

This is an important limitation for your project. The paper can distinguish outcome inequality attributable to observed circumstances from residual outcome inequality, but it cannot separate opportunities from preferences. Any preference heterogeneity is effectively absorbed into the ethically acceptable or residual component, unless it is correlated with observed circumstances in a way that shows up through between-type means. 

# Treatment of opportunities / constraints

The paper treats opportunities explicitly, but in the opportunity-egalitarian sense of predetermined circumstances rather than in the feasible-set sense of actual menus of jobs or bundles. Circumstances include family background, ethnicity, birthplace, and gender. These define types, and opportunity inequality is identified with inequality across those types. 

There is no explicit modeling of feasible job sets, hours restrictions, job offers, demand-side constraints, or latent opportunity sets. The paper therefore does not model opportunities as (A)-type feasible sets. It also does not assume a universal choice set because it is not a choice model at all. Rather, it proxies opportunities by morally irrelevant traits that condition the opportunities available to a person. 

The paper is therefore highly useful for one meaning of “opportunities”—background-determined life chances—but not for your more specific notion of feasible job or ability sets. It helps distinguish opportunity heterogeneity from residual inequality, but not opportunity heterogeneity from preference heterogeneity, and not actual opportunity sets from reference opportunity sets. 

# Welfare / normative object

The normative object is inequality of opportunity, not utility or well-being directly. The paper asks how much inequality in a valuable outcome—household income, household consumption, or labor earnings—can be attributed to predetermined circumstances. It is therefore a normative measurement paper rather than a behavioral welfare paper. 

This is directly relevant to responsibility versus compensation. The paper explicitly adopts the view that outcome differences due to circumstances should be compensated, whereas differences due to effort may be ethically acceptable. That is precisely the language of opportunity egalitarianism with which your project overlaps. 

The paper is also useful for thinking about policy targeting through its “opportunity-deprivation profile,” which identifies the worst-off types in each society. This is especially relevant to compensation-oriented policy design, even though the paper itself does not solve an optimal policy problem. 

# Main findings

The main empirical finding is that lower-bound estimates of the inequality of opportunity ratio are large in all six Latin American countries. For household per capita income, the parametric IOR ranges from 0.23 in Colombia to 0.34 in Guatemala. For household consumption, the parametric IOR ranges from 0.25 in Colombia to 0.51 in Guatemala. These are reported in Table 6 on pages 22–23. 

A second important result is that the non-parametric and parametric estimates are generally close, and their differences are never statistically significant. This supports the robustness of the lower-bound estimates, while still favoring the parametric approach in smaller samples where many types have sparse cell counts. Table 5 and Table 6 are central here. 

The circumstance-specific partial shares suggest that family background is the most important set of observed circumstances. Mother’s education and father’s education generally account for larger partial opportunity shares than ethnicity or birthplace; father’s occupation also matters where observed. Table 9 is the key source. 

The opportunity-deprivation profiles show that the worst-off types are heavily concentrated among ethnic minorities and socially disadvantaged family-background groups. Table 11 reports that the opportunity-deprived are entirely composed of ethnic or racial minorities in three of the six countries, and that in all six countries they are overwhelmingly drawn from low parental education and disadvantaged occupational backgrounds. 

# Main limitations

The first limitation is that the indices are only lower bounds. This is a virtue relative to overclaiming, but it also means the paper does not recover the true level of inequality of opportunity, only a floor implied by the observed set of circumstances. 

A second limitation is conceptual for your purposes: opportunities are defined through types determined by background variables, not by feasible sets of jobs or actual opportunity menus. This is far from your (A)-type opportunity set. The paper therefore cannot answer questions about independence of infeasible jobs, latent offers, or reference opportunity sets. 

A third limitation is that preferences and responsibility-relevant effort are not structurally modeled. The ethically acceptable component is residual relative to observed circumstances, but it is not cleanly identified as “effort” in any behavioral sense. This matters if one wants a sharper fairness interpretation. 

A fourth limitation is that the measure is sensitive to the observed circumstance set and to how categories are discretized. The authors themselves note that international comparability sometimes requires relatively coarse coding, which may compress the measured opportunity component. Tables 3–5 make this operational issue clear. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing any argument that the ethically important part of inequality is the part due to predetermined circumstances. It provides a clean empirical counterpart to a compensation-oriented fairness claim. 

## possible use for model design

It is not useful for structural labor-supply model design directly. But it is useful as a template for how to turn a normative distinction into a measurable object once a set of opportunity-defining variables has been specified. For your project, it suggests how a decomposition layer could sit on top of a richer well-being model. 

## possible use for identification

It is useful because it is explicit about lower-bound identification. Rather than pretending to identify the full opportunity effect, the paper shows how to interpret observed-circumstance decompositions conservatively. That is a discipline worth importing into your own decomposition work. 

## possible use for welfare measurement

Directly limited, because the advantage measure remains income or consumption, not well-being. Indirectly important, because it shows how a fairness-motivated measure can be axiomatically linked to a unique inequality index and then implemented empirically. 

## possible use for decomposition

This is one of the paper’s strongest uses for your JMP. It gives you a theoretically grounded and empirically feasible between-type decomposition framework, and it clarifies why the resulting measure should be interpreted as a lower bound when some circumstances are unobserved. 

## possible use for comparative application

Very useful. The paper is explicitly comparative across six countries and develops opportunity-deprivation profiles that can be compared across societies. This is relevant if your project later acquires a cross-country or cross-region dimension. 

# Research questions this paper inspires

Can a lower-bound inequality-of-opportunity measure be constructed when opportunities are represented by estimated feasible job sets rather than by observed background types?

How would the between-type opportunity share change if the advantage variable were not income or consumption but a well-being index (W(z,R,A;y))?

Can one derive a similar lower-bound result when types are defined jointly by family background and estimated job opportunity sets?

What axioms would be needed to replace the mean-log-deviation-based opportunity measure with one defined over a richer well-being object while preserving path-independent decomposition?

How sensitive are opportunity-deprivation profiles to the choice of type partition when the opportunity concept is expanded from background types to labor-market feasibility types?

# Challenge to this paper

The key challenge is that the measure’s ethical interpretation depends on a sharp partition between “circumstances” and everything else, but the empirical implementation has no structural account of effort, preferences, or choice. As a result, the residual is treated as ethically distinct without demonstrating that it is genuinely responsibility-sensitive. That may be acceptable for lower-bound measurement, but it is less satisfying for a fully worked-out fairness theory. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper defines opportunity inequality through between-type inequality when types are formed exclusively by predetermined circumstance variables. It does not model individual well-being as a function (W(z,R,A;y)), and it does not define opportunities as feasible job sets or ability sets. 

[reasonable inference for my project] The paper is useful if your framework eventually aggregates well-being or advantage across individuals and then seeks a lower-bound decomposition of inequality attributable to background-type differences. In that case, its smoothed-distribution logic and lower-bound interpretation could carry over. 

[unclear from paper] It is unclear how its type-based notion of opportunity would map into your (A), because (A) in your work is a feasible-set object, whereas types here are circumstance classes. It is also unclear how (R) could be incorporated, since preferences are absent, and how (y) would enter except through the observed advantage variable. 

[reasonable inference for my project] In your taxonomy, the paper is closest to responsibility for opportunities, compensation for opportunities, and decomposition of inequality. It is not close to independence of (A), independence of (y), reference opportunity sets, or laissez-faire evaluation. It is a measurement paper for circumstance-based opportunities, not a theory of feasible opportunities. 

# Relation to Bargain et al. (2013)

[not central]

# Relation to opportunities vs preferences

This paper is strongly about opportunities versus responsibility, but only weakly about opportunities versus preferences. Opportunities are formalized through circumstances; preferences do not appear. The ethically admissible remainder is not identified as preference heterogeneity, but as whatever is left once between-type opportunity inequality has been netted out. 

For your purposes, that means the paper is highly relevant for the opportunity side of the distinction, but not sufficient for a framework that needs to separate opportunities from preferences rigorously. It would need to be complemented by a model in which preferences are explicit and not merely absorbed into the residual. 

# Useful quotations / formulas

The core indices are:
[
\theta_a = I({\mu_i^k}), \qquad
\theta_r = \frac{I({\mu_i^k})}{I(y)}.
]
These define the inequality of opportunity level and inequality of opportunity ratio. 

With path-independent decomposability, the paper pins these down to:
[
\theta_a = E_0({\mu_i^k}), \qquad
\theta_r = \frac{E_0({\mu_i^k})}{E_0(y)}.
]
This is one of the paper’s most useful theoretical contributions. 

The lower-bound argument is central: any unobserved circumstance variable would refine the partition of the population into types and weakly increase between-type inequality in the smoothed distribution. This is the proposition in Section 3. 

# Suggested tags

inequality-of-opportunity, lower-bound-measurement, Roemer, van-de-Gaer, Latin-America, between-group-inequality, opportunity-deprivation-profile, circumstances

# My quick takeaway

This is one of the most useful papers in your corpus for the measurement side of fairness and decomposition. Its main contribution is not to model labor-supply behavior or actual opportunity sets, but to provide a theoretically disciplined lower-bound measure of inequality due to predetermined circumstances and to show how it can be implemented robustly across countries. For your project, it is especially valuable as a decomposition and measurement template. It is less useful for modeling (A) as a job-feasibility set or for handling heterogeneous preferences, which remain outside its framework.
