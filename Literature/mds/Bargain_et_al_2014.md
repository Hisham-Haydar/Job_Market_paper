---

title: "Comparing inequality aversion across countries when labor supply responses differ"
authors: ["Olivier Bargain", "Mathias Dolls", "Dirk Neumann", "Andreas Peichl", "Sebastian Siegloch"]
year: 2014
outlet: "International Tax and Public Finance"
country_or_context: "17 European countries and the United States"
population: "Childless single individuals aged 18–64 who are potential salary workers"
data_period: "EU: 1998 and/or 2001 for EU-15, 2005 for Estonia/Hungary/Poland; US: CPS 2006 with incomes for 2005"
shelf: "revealed_social_inequality_aversion_optimal_taxation"
tags: ["optimal taxation", "revealed social preferences", "inequality aversion", "labor supply", "extensive margin", "intensive margin", "cross-country comparison", "tax-benefit systems", "Saez inversion", "childless singles"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Bargain, Olivier, Mathias Dolls, Dirk Neumann, Andreas Peichl, and Sebastian Siegloch. 2014. “Comparing inequality aversion across countries when labor supply responses differ.” *International Tax and Public Finance* 21: 845–873. 

# One-sentence contribution

The paper estimates country-specific labor supply elasticities for childless singles in 17 EU countries and the US, then inverts a discrete Saez optimal-tax model to recover the degree of social inequality aversion implicit in actual tax-benefit systems, showing that accounting for cross-country differences in labor supply responses changes the ranking of redistributive tastes across countries. 

# Why this paper matters

This paper matters because it tries to separate two things that are often conflated in comparative public economics: redistributive tastes of the social planner and behavioral responsiveness of workers. A country may redistribute more either because it is normatively more inequality-averse or because it faces different labor supply constraints. The paper’s core contribution is to estimate labor supply elasticities and social inequality aversion on the same data using a common method across countries. 

For your project, the paper is particularly useful on two fronts. First, it shows how one can move from a structural labor supply model to a normative parameter recovered from observed policy. Second, it sharply illustrates the distinction between individual consumption-leisure preferences and social preferences for redistribution. It is much less useful for opportunities or feasible job sets, but very useful for the preference and welfare-aggregation sides of your framework. 

# Core research question

To what extent do social inequality aversion parameters differ across countries once one controls for actual country differences in labor supply responses, rather than imposing common “plausible” elasticities from the literature? 

# Economic setting and context

The paper is a cross-country comparative study of redistribution and optimal-tax primitives in 17 European countries and the US. It focuses on direct taxes and transfers for childless single individuals and interprets observed tax-benefit systems through the lens of a discrete Mirrleesian/Saez-style optimal tax model. 

The context is explicitly normative public economics. The authors are interested in the equity-efficiency trade-off embodied in actual systems, not just in descriptive redistribution. They argue that standard cross-country comparisons of redistribution often ignore labor supply behavior and therefore fail to separate social redistributive tastes from behavioral constraints. 

# Model / theoretical framework

The model class combines two pieces. The first is a structural discrete-choice labor supply model for childless singles, estimated country by country. The second is the discrete optimal income tax model of Saez (2002), formulated over a small number of income groups with extensive- and intensive-margin elasticities. The empirical strategy is to estimate the former and invert the latter. 

Agents are childless single individuals who choose labor supply over discrete hours categories. Utility is specified over disposable income and hours worked, with fixed costs of work and observed/unobserved heterogeneity. On the normative side, the government is represented as a social planner choosing an optimal tax-benefit schedule, summarized by marginal social welfare weights (g_i) and a scalar inequality-aversion parameter (\gamma). 

The framework is both positive and normative. The labor supply model is positive and behavioral. The optimal-tax inversion is explicitly normative in the sense that it recovers the social inequality aversion consistent with observed systems under the assumption that these systems are optimal. 

Opportunities are not modeled explicitly as feasible sets. The model is standard discrete labor supply with fixed costs and tax-benefit constraints. There is no explicit (A_i), no latent job density, and no direct treatment of opportunity heterogeneity in the RURO sense. Fixed costs may absorb some labor-market constraints, but this is not the paper’s central object. 

# Key objects

The main positive objects are gross income (Y_i), disposable income (C_i), effective tax levels (T_i), extensive-margin elasticities (\eta_i), and intensive-margin elasticities (\zeta_i). These are defined over discrete income groups rather than continuously at the individual level. Equations (1)–(3) on pages 5–6 are central. 

The main normative objects are the marginal social welfare weights (g_i) assigned to each income group and the scalar social inequality-aversion parameter (\gamma), recovered through the parameterization
[
g_i=\frac{1}{(p\cdot C_i)^\gamma}.
]
This is the paper’s key summary measure of redistributive tastes. 

A second important object is the grouping of the population into six income states: group 0 for non-workers and five income groups among workers. The group structure is central because the inversion is conducted on this discretized population. Tables 2 and 3 report group sizes, gross and disposable incomes, EMTRs, and EPTRs. 

# Data

The paper uses harmonized household microdata for 17 EU countries and the US, linked to tax-benefit simulation tools. EU countries are analyzed with EUROMOD using policy years 1998 and/or 2001 for EU-15 countries and 2005 for Estonia, Hungary, and Poland. The US is analyzed with TAXSIM combined with IPUMS-CPS 2006 data referring to 2005 incomes. 

The sample is restricted to childless single individuals aged 18–64 who are potential salary workers. Pensioners, students, farmers, and the self-employed are excluded. Households with capital income above 25% of total gross income are also excluded. The paper emphasizes this narrow selection because the Saez model is formulated for singles and because aggregation across demographic types raises comparability problems. 

Descriptive information is reported in Appendix I, especially Tables 2 and 3 on pages 19–22. These tables show for each country the group-specific gross income, disposable income, effective marginal tax rates, effective participation tax rates, and group sizes used in the inversion. 

# Identification logic

Identification has two layers. The first layer is identification of labor supply behavior. The paper estimates country-specific structural labor supply models using variation in net incomes generated by detailed nonlinear tax-benefit simulation, plus variation in wages and demographic characteristics. The authors explicitly rely on the structural identification logic common in discrete labor supply models, with tax-benefit nonlinearities as a key parametric source of identification. 

The second layer is identification of social inequality aversion. This is obtained by inverting the Saez optimal tax formula using observed group-level incomes and simulated net tax schedules together with estimated extensive- and intensive-margin elasticities. The crucial assumption is that the observed tax-benefit system is optimal, or at least corresponds to a fixed point of the planner’s problem. Without that optimality assumption, the inversion would not be valid. This is a strong but explicit identifying assumption. 

The paper also assumes zero income effects in the theoretical optimal-tax model, and then checks empirically that income elasticities are very small for the selected sample. That empirical check is important because it helps align the estimated labor supply model with the theoretical inversion. Appendix II is central here. 

Identification is weak with respect to opportunities. The paper does not separately identify opportunity heterogeneity from preference heterogeneity. It identifies labor supply responses and then social weights conditional on that behavioral model. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The empirical strategy proceeds in two steps. First, the authors estimate a discrete-choice structural labor supply model separately for each country for childless single individuals. Utility is quadratic in disposable income and hours worked, with fixed costs of work and random heterogeneity. The model uses seven discrete hours choices from 0 to 60 hours per week. 

Second, they simulate labor supply responses to obtain the Saez extensive- and intensive-margin elasticities by income group, and then invert the optimal tax model to recover the marginal social welfare weights (g_i) and the scalar inequality-aversion parameter (\gamma). This inversion is the paper’s main methodological innovation in comparative use. 

The core visual summaries are strong. Figure 1 on page 11 shows the country-by-country extensive and intensive Saez elasticities for each income group, making clear that the extensive margin is generally larger. Figure 2 on page 12 compares international participation elasticities. Figure 3 on page 15 shows the revealed inequality-aversion parameter (\gamma) under alternative elasticity scenarios. Figure 4 on page 17 reports sensitivity checks. 

# Treatment of preferences

The paper clearly distinguishes individual consumption-leisure preferences from social redistributive preferences. Individual preferences are estimated through the structural labor supply model. Social preferences are then recovered from the tax-benefit system via the optimal-tax inversion. This separation is one of the paper’s strongest conceptual features. 

On the individual side, the paper finds relatively small but non-negligible differences in labor supply elasticities across countries. It also emphasizes that elasticities differ more by income group and margin than by country in a dramatic way: extensive responses are systematically larger than intensive responses, and responses are often strongest at the bottom of the earnings distribution. Figure 1 and Tables 4–5 are central here. 

On the normative side, the recovered (\gamma) captures social inequality aversion, not individual tastes. This distinction is directly useful for your project because it separates (R)-type individual preferences from a social-ordering or policy-design parameter. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly as feasible sets, job offer distributions, or latent opportunity structures. There is no direct equivalent of (A) in your framework. Instead, the behavioral side is standard structural labor supply with fixed costs and tax-benefit constraints. 

The only sense in which constraints enter beyond the budget set is through fixed costs of work and the institutional structure of tax-benefit schedules. The authors note that fixed costs can partly account for labor-market restrictions, but this remains implicit and secondary. The paper is therefore not useful for actual opportunity sets, reference opportunity sets, or decomposition into opportunity versus preference disadvantage. 

It does, however, matter for your agenda in one indirect way. Because social inequality aversion is inferred from observed tax-benefit systems after controlling for estimated labor supply responses, the paper shows how one can move from a behavioral model to a normative parameter without collapsing the latter into the former. That is relevant to your broader aim of separating positive and normative layers. [reasonable inference for my project] supported by 

# Welfare / normative object

The paper is explicitly normative. Its central normative object is the degree of social inequality aversion (\gamma) implicit in actual tax-benefit systems when these systems are treated as optimal. The recovered (\gamma) summarizes how Rawlsian versus utilitarian the planner’s redistributive preferences must be, given labor supply responses and the existing system. 

The paper therefore does not evaluate welfare at the individual level using EV, equivalent income, or fair-allocation metrics. It evaluates systems through implied social marginal welfare weights and a scalar inequality-aversion parameter inside a welfarist optimal-tax framework. This is a social-evaluation paper, not an individual well-being paper. 

It is directly relevant for social preferences and redistribution, but not for responsibility versus compensation in the Fleurbaey-Maniquet sense. It also does not provide a decomposition of inequality into opportunities, preferences, and pay schedules. The decomposition it offers is closer to: observed redistribution = social redistributive tastes plus behavioral elasticities under optimality. [reasonable inference for my project] supported by 

# Main findings

The first main finding is that labor supply responses differ less across countries than is often presumed, but these differences are still large enough to affect the ranking of revealed inequality aversion across countries. Figure 2 on page 12 emphasizes that mean participation elasticities mostly lie in a relatively narrow range, yet Figure 3 on page 15 shows meaningful reranking once country-specific elasticities are used instead of uniform ones. 

The second main finding is that extensive-margin responses are systematically larger than intensive-margin responses, and often larger for the lowest income groups. Figure 1 on page 11 and Tables 4–5 in Appendix II show this clearly. This matters normatively because it makes redistribution toward the workless poor more distortionary in countries with traditional social assistance systems, thereby implying higher revealed social inequality aversion if such systems are still optimal. 

The third main finding is substantive: revealed social inequality aversion clusters countries into broad groups. Southern Europe and the US appear closer to utilitarian preferences, Nordic countries and some Continental European countries appear closer to Rawlsian views, and an intermediate group includes parts of Continental Europe, the UK, Ireland, and Finland. Figure 3 on page 15 is the key summary. 

A further finding is that if one فرضes zero extensive-margin responses, revealed redistributive tastes become much less pronounced and more similar across countries. Figure 4 on page 17 shows that much of the strong Rawlsian appearance of some systems depends on taking the extensive margin seriously. 

# Main limitations

A first limitation is the strong optimality assumption. The inversion only works if the observed tax-benefit system is treated as an optimal response of the planner. Real systems may instead reflect political frictions, historical accidents, or partial reforms. The paper explicitly acknowledges that it remains agnostic about the political process and uses the social planner as a simplified proxy. 

A second limitation is the narrow population coverage. The analysis is restricted to childless single individuals, partly for tractability and comparability. This improves internal coherence but limits external representativeness for whole-country redistributive preferences. The authors argue that cross-country patterns for this group still reflect broader differences in redistribution, but the restriction remains real. 

A third limitation is the absence of opportunities as explicit objects. The model cannot tell whether low earnings or low participation reflect constrained opportunity sets, preferences, or both. From your perspective, that means the recovered (\gamma) is informative about social preferences over income groups, but not about justice with respect to opportunity sets. [reasonable inference for my project] supported by 

A fourth limitation is that only labor supply responses are included. Migration, tax evasion, human capital choices, and other margins are omitted. The conclusion explicitly notes these as important directions for future work. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing the difference between individual behavioral preferences and social redistributive preferences. It gives a concrete comparative implementation of that distinction.

## possible use for model design

It is moderately useful for model design if your empirical work remains within standard discrete labor supply and public-finance inversion. It is not useful for explicit opportunity-set modeling.

## possible use for identification

It is useful as an example of how to estimate behavioral elasticities and then use them consistently in a normative inversion on the same data. The methodological discipline is a major strength.

## possible use for welfare measurement

It is useful mainly at the social-evaluation level. It does not provide an individual welfare metric, but it does provide a way to recover a country-level redistributive parameter from observed policy.

## possible use for decomposition

It is limited for your decomposition agenda. It does not decompose welfare into (R), (A), and (y). It does, however, separate social inequality aversion from behavioral responsiveness, which is a different but still useful decomposition.

## possible use for comparative application

It is highly useful comparatively. The harmonized cross-country structure is exactly the paper’s main contribution, and it is a strong reference for any international comparative normative exercise.

# Research questions this paper inspires

Can a revealed social inequality-aversion parameter be recovered in a framework where individual well-being is (W(z,R,A;y)) rather than income-group utility under a Saez model?

How would the recovered (\gamma) change if labor supply elasticities were estimated in a RURO-type model with explicit opportunity heterogeneity rather than a standard discrete-hours model?

Can one jointly recover social preferences over redistribution and ethical attitudes toward opportunity disadvantage, rather than only social inequality aversion over income groups?

How sensitive are revealed redistributive tastes to omitted extensive margins beyond participation, such as job access, occupational mobility, or wage offer constraints?

Can the inversion logic used here be adapted to recover not only a scalar inequality-aversion parameter but also opportunity-sensitive social weights?

# Challenge to this paper

The strongest challenge is that the normative sophistication of the inversion is paired with a relatively thin behavioral concept of heterogeneity. The paper carefully distinguishes social preferences from labor supply responses, but it does not distinguish preferences from opportunities at the individual level. For your project, this means it is strong on social redistribution and weak on the structure of individual disadvantage. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper clearly separates social redistributive preferences from individual labor supply behavior. Individual preferences are estimated through the labor supply model, while the social planner’s inequality aversion is recovered from observed policy through the inverted optimal-tax formula. 

[reasonable inference for my project] In your notation, the paper is closest to work on the relation between (R) and social evaluation, but not on (A). The realized bundle (z) is effectively reduced here to income-group position and labor supply outcome. The pay schedule (y) enters through the tax-benefit mapping and group-specific gross-to-net income transformation. Preferences (R) are behaviorally present. Feasible opportunities (A) are largely absent as explicit objects. 

[unclear from paper] The paper does not define an individual well-being measure (W(z,R,A;y)), does not analyze axioms such as independence of (A) or independence of (y), and does not study compensation or responsibility for opportunities. It also does not distinguish actual from reference opportunity sets. 

[reasonable inference for my project] In your taxonomy, this paper is closest to social aggregation, redistribution, and the relation between behavioral heterogeneity and normative conclusions. It is not close to independence of (A), because (A) is not a central object. It is also not close to laissez-faire or to a reference-opportunity-set approach. It is best read as a social-preference paper rather than an individual well-being paper. 

# Relation to Bargain et al. (2013)

This paper is closely related to Bargain et al. (2013) in one important respect: both separate individual consumption-leisure preferences from a normative evaluation layer. But the normative object differs sharply. Bargain et al. (2013) studies individual welfare rankings under alternative metrics that respect heterogeneous preferences, whereas the present paper recovers a social inequality-aversion parameter implicit in actual tax-benefit systems. So the 2013 paper is about interpersonal welfare comparison; this 2014 paper is about tax-revealed social preferences.

# Relation to opportunities vs preferences

This paper is much more useful for preferences and redistribution than for opportunities. It distinguishes individual consumption-leisure preferences from social redistributive tastes, but it does not distinguish preferences from opportunities in the sense of job access or feasible-set heterogeneity. 

So for your project, it should be read as a benchmark on how to recover social normative parameters from observed tax policy once behavioral responses are controlled for. It is not a paper about opportunity-sensitive welfare measurement. 

# Useful quotations / formulas

The key optimal-tax formula is
[
\frac{T_i-T_{i-1}}{C_i-C_{i-1}}
===============================

\frac{1}{\zeta_i h_i}
\sum_{j=i}^{I} h_j
\left(
1-g_j-\eta_j\frac{T_j-T_0}{C_j-C_0}
\right),
]
for (i=1,\ldots,I). This is the core equation inverted to recover social welfare weights. 

The key parameterization of social inequality aversion is
[
g_i=\frac{1}{(p\cdot C_i)^\gamma}.
]
This is central because (\gamma) is the paper’s summary statistic for redistributive tastes. 

Figure 3 on page 15 is especially useful. It visually shows that once country-specific elasticities are used, the ranking of revealed inequality aversion changes relative to the standard uniform-elasticity approach, and that some pairwise country comparisons remain statistically incomplete. 

# Suggested tags

revealed-social-preferences, inequality-aversion, optimal-tax-inversion, Saez, structural-labor-supply, extensive-margin, cross-country, redistribution, tax-benefit-systems, Bargain-et-al-2014

# My quick takeaway

This is a high-priority paper for the social-preference side of your corpus. It does not help much with opportunity sets or individual well-being as (W(z,R,A;y)), but it is a strong methodological paper on how to recover a normative parameter from actual redistribution once behavioral responses are estimated consistently. For your JMP, its main value is as a benchmark on separating individual labor supply behavior from social redistributive preferences in a comparative setting.
