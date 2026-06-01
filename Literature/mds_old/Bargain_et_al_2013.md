---

title: "Welfare, labor supply and heterogeneous preferences: evidence for Europe and the US"
authors: ["Olivier Bargain", "André Decoster", "Mathias Dolls", "Dirk Neumann", "Andreas Peichl", "Sebastian Siegloch"]
year: 2013
outlet: "Social Choice and Welfare"
country_or_context: "11 European countries and the United States"
population: "Married-couple households, with female labor supply modeled; women aged 18–59; husbands working at least 30 hours per week"
data_period: "EU countries: 1998 or 2001 depending on country; US: 2005 income year using 2006 IPUMS-CPS"
shelf: "welfare_labor_supply_crosscountry"
tags: ["welfare", "labor supply", "discrete choice", "heterogeneous preferences", "cross-country comparison", "equivalent income", "microsimulation", "tax-benefit systems", "married women", "normative economics"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bargain, Olivier, André Decoster, Mathias Dolls, Dirk Neumann, Andreas Peichl, and Sebastian Siegloch. 2013. “Welfare, labor supply and heterogeneous preferences: evidence for Europe and the US.” *Social Choice and Welfare* 41: 789–817. DOI: 10.1007/s00355-012-0707-x. 

# One-sentence contribution

The paper combines harmonized cross-country structural discrete-choice labor supply estimation with preference-sensitive welfare metrics to show that international welfare rankings change materially once heterogeneous consumption-leisure preferences are respected.

# Why this paper matters

This paper matters because it links positive structural labor supply estimation to explicitly normative welfare comparison, rather than treating welfare as income alone or imposing identical preferences for interpersonal comparability. It is particularly important for work that wants to go beyond GDP, compare well-being across countries, and keep preference heterogeneity visible rather than normalizing it away.

For your potential JMP, it is highly relevant because it gives a concrete template for using estimated labor supply preferences in welfare comparisons while also making clear where the main unresolved issue lies: the paper treats preference heterogeneity seriously, but does not model opportunity sets or demand-side job constraints as first-class objects. That makes it a strong benchmark and, simultaneously, a clear point of departure.

# Core research question

How do international welfare rankings change when one compares households using welfare metrics that fully retain heterogeneity in consumption-leisure preferences, rather than relying on income alone or on a representative/reference preference ordering?

# Economic setting and context

The setting is a cross-country comparison of well-being across 11 European countries and the United States, motivated by the “beyond GDP” agenda and by debates in fair allocation and social choice about how to compare welfare when preferences differ. The paper works in a consumption-leisure environment and evaluates married-couple households, focusing on female labor supply because married women exhibit substantial variation in hours and are viewed by the authors as less affected by demand-side restrictions than other groups.

Institutionally, the paper embeds household choices in country-specific tax-benefit systems. Net household income at each discrete hours point is generated using EUROMOD for European countries and TAXSIM for the US, so the policy environment enters through nonlinear household budget sets rather than through a reduced-form policy indicator. 

# Model / theoretical framework

The model is a static structural labor supply model with discrete hours choices, combined with an explicitly normative welfare-ranking framework derived from the social-choice / fair-allocation literature. The positive side estimates consumption-leisure preferences; the normative side maps estimated indifference curves into alternative welfare metrics. The framework is therefore both positive and normative, but it stops short of a social welfare function and focuses on interpersonal orderings of individual situations.

The household chooses among a finite set of female hours alternatives. Male labor supply is fixed. The feasible set is the set of discrete hours categories together with the corresponding net incomes implied by wages, non-labor income, demographics, and the country’s tax-benefit schedule. The paper does not model explicit job opportunity sets, hours rationing, latent jobs, or employer-side availability. In that sense, feasibility is budget-feasibility over a discretized hours menu, not an explicit opportunity-set model in the RURO sense.

On the welfare side, the paper studies three metrics built from indifference curves and hypothetical linearized budget sets: the “wage” metric, the “rent + reference wage” metric, and the “rent” metric. These metrics differ only in their ethical treatment of heterogeneous tastes for work versus leisure. 

# Key objects

The central preference object is the household utility function over net consumption and female leisure, with deterministic utility specified in Box-Cox form and an additive extreme-value error at each hours alternative. Country-specific preference parameters and household-level taste shifters generate heterogeneity.

The main behavioral objects are discrete female hours choices, predicted female wages, household net income at each hours point, and marginal rates of substitution between consumption and hours worked. The authors emphasize MRS as the key summary of cross-country taste heterogeneity, not labor supply elasticities.

The main normative objects are the three welfare metrics:
[
\nu_i^W(u,0)=\min_{\tilde w_i}{\tilde w_i \mid v_i(\tilde w_i,0)\ge u},
]
[
\nu_i^{RW}(u,w^r)=e_i(u,w^r)=\min_{\mu_i}{c_i-w^r h_i \mid u_i(c_i,h_i)\ge u},
]
[
\nu_i^R(u,0)=c_i(u,0)=\min_{c_i}{c_i \mid u_i(c_i,0)\ge u}.
]
These are, respectively, the wage metric, the rent-plus-reference-wage metric, and the rent metric. 

# Data

The paper uses 12 representative microdatasets: 11 European country datasets linked to national tax-benefit simulations for 1998 or 2001, and the 2006 IPUMS-CPS for the US containing information for 2005. The sample is restricted to married couples. Women are aged 18–59 and must be available for the labor market; women who are disabled, retired, or in education are excluded. Husbands must work at least 30 hours per week, and households with extreme capital income are excluded. The full sample contains 42,975 households.

The core variables are household net income, non-labor income, female hours, female wages, and socio-demographics. Taste shifters include spouses’ ages, female education, young children, and region. Net income is computed at seven discrete female hours categories from 0 to 60 hours in 10-hour steps. Income and wages are expressed in 2001 PPP-USD for comparability.

# Identification logic

Identification is mainly structural and parametric. Preference parameters are identified from observed female hours choices combined with the nonlinearities of country-specific tax-benefit systems, predicted wages, non-labor income, and demographic taste shifters. The key source of variation is how different households face different effective net-income schedules across discrete hours points because of taxes, transfers, and household characteristics. 

This is not an explicit quasi-experimental identification design. The paper relies on the maintained utility specification, the discrete-choice structure, selection-corrected wage prediction, and the assumption that observed choices reveal the relevant consumption-leisure trade-off once the tax-benefit schedule is properly simulated. The paper is explicit that direct parametrization of utility is what allows them to recover indifference curves and then construct welfare orderings.

Relative to your agenda, the important point is that identification is of preferences conditional on the model’s feasible menu; it is not identification of opportunity sets, job offers, or rationing mechanisms. That distinction is central if one wants to separate preferences from opportunities.

# Estimation / empirical strategy

The empirical strategy is to estimate country-specific structural discrete-choice labor supply models by maximum likelihood under i.i.d. Type-I extreme-value errors. Utility at each discrete hours alternative is (V_{ij}=u_i(c_{ij},T-h_{ij})+\varepsilon_{ij}), with deterministic utility given by a Box-Cox function in consumption and leisure.

After estimation, the authors compute expected optimal utility using repeated draws from the extreme-value distribution, recover indifference curves from the deterministic component, and then derive welfare metrics analytically for the rent metric and numerically for the other two metrics using tangency conditions along the indifference curve. They then compare households internationally through percentile ranks rather than by aggregating with a social welfare function.

They also conduct decomposition exercises: first by examining MRS differences across countries, then by counterfactual decompositions that separate the contribution of estimated preference parameters from socio-demographic composition to cross-country reranking. Robustness checks vary the utility specification, the computation of welfare metrics, and the reference household used in the decomposition analysis.

# Treatment of preferences

Preferences are modeled explicitly and heterogeneously. The paper allows both cross-country heterogeneity and within-country heterogeneity. Cross-country heterogeneity enters because the utility parameters are estimated separately by country. Within-country heterogeneity enters through taste shifters in the leisure coefficient, including age, education, children, and region.

This is not a random-coefficients continuous mixture model in the modern sense; it is a structural discrete-choice model with observed heterogeneity and additive random utility shocks. The random term captures unobserved determinants of the hours choice, including unobserved taste variation across alternatives, but the normatively relevant indifference curves are derived from the deterministic utility component. 

Normatively, the paper is expressly about whether welfare analysis should retain heterogeneous preferences instead of replacing them with a reference household. That makes preference heterogeneity the main conceptual object of the paper, not a robustness feature.

# Treatment of opportunities / constraints

This is the crucial weakness from the perspective of your research agenda.

The paper does **not** model opportunities explicitly. It does **not** estimate job opportunity sets, latent jobs, job offer distributions, or country-specific hours availability in the RURO / latent-jobs sense. The household is assumed to choose from a fixed discrete set of hours alternatives, with feasibility determined through the budget set generated by taxes, transfers, wages, and non-labor income. Demand-side restrictions and fixed costs of work are omitted in the baseline specification.

The authors are unusually clear about this limitation. In the conclusion they note that fixed costs of work and demand-side constraints may rationalize non-participation or restricted choices, and they explicitly say that, in the present context, a demanding requirement would have been to determine country-specific choice opportunities. They also cite the literature on quantity constraints and involuntary unemployment as relevant omitted factors. 

So the paper treats constraints implicitly through the tax-benefit budget schedule and the discrete hours menu, but not through explicit opportunity sets. For your purposes, that means the paper may still conflate genuine work preferences with constrained labor-market opportunities, even though it is much more careful than most welfare-comparison papers about heterogeneity in tastes. 

# Welfare / normative object

The welfare object is an individual welfare ranking based on equivalent-income-type metrics in the consumption-leisure space, adapted from Fleurbaey’s fair-allocation framework. The three welfare metrics are the rent metric, the rent-plus-reference-wage metric, and the wage metric. Each retains individuals’ own indifference curves but differs in the ethical reference used for interpersonal comparison. 

The paper is therefore not purely positive. It is positive in the estimation of labor supply preferences and normative in the construction of welfare rankings. It is not an explicit social-welfare-function paper: the authors emphasize that they study pure orderings of individual well-being and intentionally avoid a social aggregator. They note that moving to SWF-based aggregation is a further step and that their concerns about preference heterogeneity should precede it.

# Main findings

First, once preferences are assumed identical through a reference household, changing the welfare metric does little beyond the standard income-versus-leisure adjustment; the strong reranking appears only when heterogeneous preferences are fully retained. 

Second, with full preference heterogeneity, international welfare rankings depend strongly on the metric. Countries with relatively high female working hours, such as the US and Nordic countries, rank relatively higher under metrics that favor higher willingness-to-work, while countries with relatively low female working hours, such as Ireland, Austria, Germany, the Netherlands, and the UK, rank relatively higher under metrics more favorable to lower willingness-to-work.

Third, reranking is quantitatively large. The paper reports changes of at least 15 percentile points for 7 of 12 countries when moving from the rent metric to the wage metric. Ireland is the most striking case, moving from 46.5 under the rent metric to 73.9 under the wage metric in average percentile rank; Finland moves in the opposite direction from 34.3 to 13.9. 

Fourth, the estimated MRS differ markedly across countries. Ireland, Germany, Austria, and the Netherlands display relatively high MRS, whereas Nordic countries, Portugal, Belgium, and the US display relatively low MRS. The authors interpret MRS, not elasticities, as the relevant summary of heterogeneous consumption-leisure tastes. 

Fifth, the decomposition exercises indicate that cross-country reranking across metrics is driven primarily by estimated country-specific preferences rather than by demographic composition alone. Demographics matter, especially children, but they do not explain most of the ranking reversals.

Sixth, the core conclusions are robust to alternative utility specifications, alternative ways of computing expected welfare metrics, and alternative reference-household choices in the decomposition exercises. 

# Main limitations

The main limitation, relative to your interests, is the absence of explicit opportunity modeling. The paper does not model latent jobs, job-offer distributions, hours rationing, or country-specific choice sets. As a result, what is estimated as preference heterogeneity may partly reflect restricted opportunities or demand-side labor-market conditions. 

A second limitation is that the analysis is built on a simple unitary married-couple model with fixed male labor supply. This is a tractable empirical design, but it excludes intra-household bargaining, joint labor supply responses, and other household-structure complexities. 

A third limitation is the narrow welfare space. The comparison goes beyond income by adding leisure, but it still leaves out in-kind public services, non-cash benefits, health, job quality, and other non-market dimensions. The authors explicitly note that public services are not incorporated because of data limitations. 

A fourth limitation is that the cross-country comparison is performed on a relatively selected group: married women in relatively rich countries plus Portugal and the US. External validity to the full population, singles, men, or poorer-country comparisons is therefore limited.

A fifth limitation is interpretive rather than technical: the paper provides interpersonal rankings, not a full social evaluation. That is deliberate, but it means the paper stops before the aggregation problem and before any explicit social-choice rule over countries or populations.

# Relevance for my JMP

## possible use for framing

This paper is useful for framing a project that sits at the intersection of labor supply, welfare comparison, and heterogeneous preferences. It gives you a clean language for saying that income-based comparisons are incomplete and that welfare comparisons can be normatively sensitive even before aggregation, once heterogeneity in tastes is respected.

## possible use for model design

It provides a benchmark structural design: discrete female-hours choice, nonlinear tax-benefit budgets, estimated indifference curves, and post-estimation welfare metrics. If you want to build a richer model, this is a natural baseline against which to compare a RURO / latent-opportunity extension. 

## possible use for identification

It is a strong illustration of how tax-benefit nonlinearities can identify consumption-leisure preferences in a comparable cross-country framework. For your work, the lesson is twofold: this is a credible starting point for identifying preferences, but it also shows exactly where identification of opportunities is missing.

## possible use for welfare measurement

The paper is especially useful if you want welfare measures that respect heterogeneous preferences without collapsing everything into a representative-agent metric. It also helps clarify that the ethical choice is embedded in the reference used for interpersonal comparison, not only in any eventual SWF.

## possible use for cross-country comparison

Methodologically, it is one of the clearest examples of harmonized cross-country structural estimation feeding into welfare comparison. For a JMP on cross-country welfare comparison, it gives you a ready-made benchmark result: much of the reranking is attributed to estimated taste heterogeneity, but because opportunities are not explicitly modeled, a future paper could ask how much of that reranking survives after modeling constrained choice sets.

# Research questions this paper inspires

How much of the cross-country reranking attributed here to heterogeneous consumption-leisure preferences would remain if households faced explicitly estimated latent job opportunity sets rather than a common discrete hours menu? 

Can one construct preference-respecting welfare metrics in a RURO framework where the feasible set is an estimated distribution of offered jobs over earnings, hours, and job characteristics rather than an abstract hours grid?

When fixed costs, demand-side constraints, and hours rationing are modeled explicitly, do cross-country differences in estimated MRS still dominate demographic composition in explaining welfare reranking?

Can cross-country welfare comparison be extended from the consumption-leisure space to a richer opportunity-sensitive space that includes job characteristics or public-service access while preserving interpersonal comparability?

Does the normative ranking implied by alternative equivalent-income metrics remain stable once the opportunity side is allowed to differ systematically across institutional environments?

# Challenge to this paper

The strongest simplification is that the paper interprets heterogeneous observed labor-supply behavior through heterogeneous preferences while leaving opportunity heterogeneity largely outside the model. Once demand-side constraints, hours rationing, fixed costs, and country-specific job availability are omitted, estimated “work preferences” can absorb part of what is really a difference in feasible opportunities. A future paper could challenge exactly this step by embedding welfare comparison in an explicit opportunity-set or latent-jobs framework. 

# Relation to Bargain et al. (2013)

This is the benchmark paper itself. For your corpus, it should be treated as a core reference because it operationalizes cross-country welfare comparison using structural labor supply estimation while preserving heterogeneous preferences. Its distinctive contribution is not merely empirical cross-country comparison; it is the combination of harmonized estimation and explicit normative comparison across alternative welfare metrics. Relative to later opportunity-sensitive agendas, its main value is that it shows how far one can go with preference heterogeneity alone, and where that strategy starts to run into conceptual limits.

# Relation to opportunities vs preferences

This paper helps separate preferences from income and leisure bundles more carefully than standard representative-agent welfare comparisons do, but it does **not** cleanly separate preferences from opportunities. The structural model isolates preferences conditional on tax-benefit schedules and a common discrete hours menu, yet it does not model latent job availability, quantity constraints, or country-specific opportunity sets. So relative to your agenda, the paper is best read as a strong preference-sensitive benchmark that still risks conflating tastes with constrained choice opportunities.

# Useful quotations / formulas

The core empirical random-utility specification is
[
V_{ij}=u_i(c_{ij},T-h_{ij})+\varepsilon_{ij}.
]
The deterministic utility is Box-Cox:
[
u_i(c_{ij},T-h_{ij})=\beta_c\frac{c_{ij}^{\alpha_c}-1}{\alpha_c}+\beta_{li}\frac{(T-h_{ij})^{\alpha_l}-1}{\alpha_l}.
]
Household heterogeneity in leisure taste enters through
[
\beta_{li}=\beta_{l0}+\beta_{lz}z_i.
]
These are the central positive-model objects behind the welfare analysis.

A very short statement capturing the paper’s main conclusion is that differences in rankings across welfare metrics are “mainly due to heterogeneous work preferences across countries—rather than demographic composition.” 

# Suggested tags

#labor_supply #discrete_choice #heterogeneous_preferences #welfaremetric #crosscountry #equivalent_income #microsimulation #taxbenefit #choice_set #normative

# My quick takeaway

If you only remember one thing from this paper for your JMP, remember this: it shows that cross-country welfare rankings can reverse once heterogeneous preferences are respected, but because opportunities are not explicitly modeled, it leaves open the decisive next question for your agenda—how much of what looks like preference heterogeneity is actually opportunity heterogeneity.
