---

title: "How Much Does Responsibility Matter in Fairness Measurement?"
authors: ["Laurence Jacquet", "Zhiyang Jia", "Thor O. Thoresen"]
year: 2026
outlet: "CESifo Working Paper No. 12418"
country_or_context: "Norway"
population: "Married couples in Norway; empirical labor-supply model estimated on Norwegian household microdata"
data_period: "Main estimation data from 2015; reform application compares the 2013 and 2019 tax systems"
shelf: "fairness_responsibility_welfare_measurement_tax_reform"
tags: ["fairness", "responsibility", "money metric utility", "compensating variation", "conditional equality", "job choice model", "structural labor supply", "tax reform", "Norway"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Jacquet, Laurence, Zhiyang Jia, and Thor O. Thoresen. 2026. “How Much Does Responsibility Matter in Fairness Measurement?” CESifo Working Paper No. 12418. 

# One-sentence contribution

The paper proposes a new empirical way to measure how much responsibility-related heterogeneity matters for welfare assessment of tax reforms by comparing standard compensating variation (CV) with a fairness-adjusted “circumstance-CV” (CVcirc), estimated through a structural job-choice labor-supply model that separates preferences from circumstances. 

# Why this paper matters

This paper matters because it does not merely discuss fairness abstractly. It operationalizes a liberal-egalitarian distinction inside an empirical structural model: inequalities due to preferences are treated differently from inequalities due to circumstances. That is unusually close to the kind of bridge you are interested in between normative fairness measurement and structural labor-supply estimation. 

It is especially important because it keeps together three layers that are often separated in the literature: a structural labor-supply model, money-metric welfare measurement, and a fairness correction based on responsibility. It is therefore much more directly relevant to your project than a generic “beyond GDP” or purely axiomatic paper. 

# Core research question

How can one empirically measure the importance of responsibility-related characteristics in welfare assessment of tax reforms, and how much does that matter in practice when evaluating a concrete income-tax reform? More specifically, do welfare effects computed under a standard money-metric criterion differ substantially from welfare effects computed under a fairness-sensitive criterion that neutralizes preference heterogeneity? 

# Economic setting and context

The empirical application is a Norwegian income-tax reform: the gradual 2013–2019 introduction of the “bracket tax,” which expanded the number of brackets in labor-income taxation while generally reducing marginal tax rates. Figure 3 in the paper shows clearly that the 2019 schedule has more brackets than the 2013 schedule and that rates are generally lower, though the first bracket begins taxing at a lower income level. 

The paper is motivated by a liberal-egalitarian concern: redistribution is more socially accepted when inequality is perceived as resulting from choices or preferences rather than from circumstances. The authors’ contribution is to translate that normative intuition into an empirical welfare-measurement exercise in the context of tax reform. 

# Model / theoretical framework

The model class is a structural discrete-choice labor-supply model of the “job choice” type, following Dagsvik and Jia. Households are unitary married couples who choose jointly over female and male hours. Utility depends on disposable income, the spouses’ hours, and job-specific nonpecuniary components. The econometric model allows for latent job opportunities, so the household does not simply choose hours off a common deterministic menu. 

The paper’s crucial theoretical move is that the job-choice model mirrors the preferences/circumstances distinction. Preferences enter through the labor-leisure trade-off in the deterministic and stochastic utility components. Circumstances enter through the latent set of job opportunities, represented by the number of available jobs at different hours combinations. The authors are explicit that this is why the model is especially suitable for a fairness analysis centered on the responsibility/circumstances dyad. 

The agent chooses a job, not just an hours point. In the two-earner household setting, the household chooses among combinations of female and male job alternatives. Latent sets (B(h)) contain jobs and non-market opportunities that offer given hours. The resulting indirect utility contains both a preference term and a term involving (\log Q(h)), where (Q(h)) is the number of available jobs with hours (h). This is one of the paper’s most important modeling features. 

The framework is positive and normative at once. It is positive because it estimates a structural labor-supply/job-choice model. It is normative because welfare changes are then evaluated with money-metric tools—CV, CVcirc, and a CE-based welfare change—under alternative views on how much preference heterogeneity should count. 

# Key objects

The main positive object is the utility function
[
U(C,h_F,h_M,z)=u(C,h_F,h_M)+\varepsilon(z),
]
where (C) is household consumption, (h_F) and (h_M) are female and male hours, and (z) indexes jobs and non-market opportunities. The corresponding indirect utility includes opportunity terms (\log Q_F(h_F)+\log Q_M(h_M)). 

The main welfare object is standard compensating variation, CV: the money amount that restores the household’s original utility after the tax reform. The central fairness-adjusted innovation is CVcirc: a compensating variation computed under the assumption that households differ only in circumstances, because preference heterogeneity is neutralized through common reference preference parameters and a common error component. 

A third key object is the conditional-equality-based welfare change, (\Delta CE), constructed by comparing welfare levels before and after the reform under the CE criterion. To obtain CE, the paper computes an equivalent linear budget line for each household, then evaluates the maximum utility reachable under reference preferences. Equations (3.2) and (3.3), together with the diagrams in Appendix A, are central here. 

# Data

The empirical implementation uses Norwegian microdata for 2015, based on a merge of the Labour Force Survey and the Income and Wealth Statistics of Households. The estimation focuses on married couples. Couples with substantial self-employment income are excluded, along with observations with implausibly high hours or wages outside a specified interval. The final estimation sample contains 1,594 couples. Table C1 gives summary statistics and Table C2 reports estimation results. 

Observed information includes hours of work, wage income, non-labor income, demographic characteristics, and education. Disposable income under actual and counterfactual tax rules is computed using the Norwegian LOTTE microsimulation system. This allows the authors to evaluate welfare effects under the 2013 and 2019 tax schedules consistently within the structural labor-supply model. 

# Identification logic

Identification is structural rather than quasi-experimental. The paper estimates a discrete-choice labor-supply/job-choice model by maximum likelihood within a conditional logit framework. The identification of preference heterogeneity relies on taste-modifying variables, especially age and number of children, while job-opportunity heterogeneity enters through the opportunity terms in the indirect utility. 

A central identifying feature is that the job-choice model contains both a utility component and an opportunity component. This permits a conceptually clean split between the preference side and the circumstance side that the authors need for CV versus CVcirc. The paper emphasizes that conventional discrete-choice labor-supply models do not handle this distinction as naturally, because they lack an explicit latent-opportunity structure. 

The welfare measures themselves are then identified through simulation. For CV and CVcirc, the authors follow McFadden’s simulation approach, drawing random utility terms and numerically solving for the income compensation that equates pre- and post-reform maximum utility. For CE, they construct equivalent linear budget sets and compare pre- and post-reform CE levels. Thus, identification of the welfare effects is model-based and simulation-based throughout. 

# Estimation / empirical strategy

The labor-supply side is estimated as a structural job-choice model for couples. Households choose among 56 combinations of male and female job or non-market alternatives. The deterministic utility specification is Box-Cox in disposable income and leisure, with age and children affecting the taste for leisure. Table C2 shows that the female leisure-preference shifters are especially important empirically. 

The paper then computes CV by solving, for each simulation draw, the income amount that equates the maximum indirect utility under the pre-reform tax schedule with the maximum indirect utility under the post-reform schedule. Appendix D explains the simulation procedure in detail. This is standard CV, fully respecting heterogeneity in both preferences and circumstances. 

To compute CVcirc, the authors modify the model so that households differ only in circumstances. In practice, they set the taste-modifying variables—age, gender, number of children—to common median values and impose a common random error term. Thus, heterogeneity in preferences is neutralized, while heterogeneity in wages, non-labor income, and job opportunities remains. Equation (D.2) is the formal definition. 

To compute (\Delta CE), the authors first calculate each household’s equivalent linear budget line before and after the reform, then evaluate the maximum reference-utility level reachable on that equivalent set. Welfare change is the difference between the post- and pre-reform CE levels. Appendix A.3 and the associated figure make this construction explicit. 

# Treatment of preferences

Preferences are central and explicitly heterogeneous. The paper treats the labor-leisure trade-off as the main source of preference heterogeneity, with age and the presence of children shifting leisure tastes. Table C2 shows that for women, age and the number of children significantly affect the taste for leisure, while the corresponding male effects are much weaker. 

This is not just a standard heterogeneous-preferences exercise. The whole point of CVcirc is to ask what welfare measurement looks like when heterogeneity in those preferences is suppressed. In other words, the paper does not merely estimate preferences; it asks whether differences in preferences should count when welfare changes from tax reform are measured. That is the paper’s central normative contribution. 

The empirical results imply that preference heterogeneity matters little for most of the Norwegian household income distribution, but does matter at the top. The mechanism runs largely through women’s stronger preference for leisure in high-income households. When preferences are neutralized under CVcirc, those women display higher labor supply and thus somewhat larger welfare gains from the reform. 

# Treatment of opportunities / constraints

This section is especially important for your project, because the paper is stronger than most fairness-measurement papers on the opportunity side. It does not model opportunities merely as a metaphor or as reference sets. It uses the job-choice model, in which households face latent sets of jobs and non-market opportunities. The number of jobs with given hours, (Q(h)), enters utility through (\log Q(h)), so opportunity heterogeneity is part of the positive model. 

The paper is explicit that this feature allows the model to reflect the circumstances/preferences dyad. Preferences are represented by the labor-leisure utility trade-off. Circumstances are represented by latent job opportunities. This is a stronger opportunity treatment than in the conventional van Soest-style discrete-choice labor-supply model, which the authors explicitly contrast with the job-choice approach. 

However, the empirical fairness correction implemented in the paper neutralizes preferences, not opportunities. That is, CVcirc fixes reference preferences while leaving opportunity heterogeneity in place. Appendix D.2 does propose a further, alternative measure (CV^{pref}) that would instead neutralize circumstances by imposing reference wages and opportunity measures, but the paper leaves that for future research. This is a very important limit from your perspective. 

So the paper helps distinguish both preference heterogeneity and opportunity heterogeneity positively, but only uses the first distinction normatively in the main empirical exercise. It is therefore a substantial step toward your project, though not the full destination. 

# Welfare / normative object

The welfare object is money-metric utility under alternative fairness interpretations. Standard CV fully respects household-specific preferences. CVcirc asks what the welfare effect of the reform would be if households differed only in circumstances. (\Delta CE) provides a second fairness-sensitive welfare-change criterion based on conditional equality rather than on compensating variation. 

This is not a paper about social welfare aggregation in the strong sense. It does not build a full social objective function over households. Instead, it focuses on how individual welfare changes from tax reform should be measured when one wants to distinguish responsibility-related heterogeneity from circumstance-related heterogeneity. 

The normative inspiration is explicitly liberal egalitarian. The paper states that fairness requires correcting inequalities due to circumstances while respecting those that arise from responsibility. The empirical question is then whether welfare measurement really changes when one implements that idea. 

# Main findings

The first main finding is that, on average, the Norwegian bracket-tax reform generates welfare gains under all three methods. Table 1 reports average welfare effects of about NOK 18,384 under CV and NOK 18,677 under CVcirc, with (\Delta CE) also positive on average. The spread of welfare effects is slightly smaller under CVcirc than under CV. 

The second main finding is that the distribution of welfare gains under CV and CVcirc is very similar across most of the household disposable-income distribution. Figure 4, Panel (A), shows almost identical profiles from the bottom through decile 9. Both measures rise gradually up to decile 9 and then drop in decile 10. 

The third and headline finding is that meaningful divergence between CV and CVcirc appears only at the very top of the household income distribution. In decile 10, CVcirc implies larger welfare gains than standard CV. The authors interpret this as evidence that responsibility matters mainly at the top, at least for this reform in Norway. 

The fourth finding is mechanistic and comes from the bottom panels of Figure 4. Panel (C) shows that males’ hours change little under preference neutralization except in the top decile, while Panel (D) shows that females’ hours increase more broadly under CVcirc. The divergence in welfare measurement is therefore driven mainly by women’s labor-supply responses. 

The fifth finding is that rankings of households by reform welfare gain are highly stable across CV and CVcirc. Table 2 shows that roughly 71% to 93% of households remain in the same welfare-gain quintile when switching from CV to CVcirc. This again suggests limited aggregate importance of responsibility adjustments for this particular reform. 

The sixth finding is that the CE-based welfare change closely tracks CVcirc. Figure 5 shows that the welfare profiles under (\Delta CE) and CVcirc are remarkably similar across the income distribution, with only slight divergence at the top. This is important because it indicates that the new CVcirc method is broadly aligned with an established fairness criterion from the social-choice literature. 

# Main limitations

The first main limitation is that the paper is a working-paper application to one country and one reform. The authors themselves note that the conclusion—that responsibility matters mainly at the top—may not generalize to other reforms or other countries. 

A second limitation is that the fairness adjustment is implemented by fixing reference preferences through median taste-modifying variables and a common error term. This is operationally convenient, but the choice of reference values is ultimately normative and partly ad hoc. The paper acknowledges this general issue by stressing the role of reference preferences in both CVcirc and CE. 

A third limitation is that the paper neutralizes preferences in the main empirical exercise, not circumstances. Although the model is rich enough to represent opportunity heterogeneity, the alternative fairness measure that would impose reference wages and reference opportunity measures, (CV^{pref}), is left for future research. From your perspective, this is the paper’s main incompleteness. 

A fourth limitation is the unitary-household assumption. Couples are assumed to make harmonized labor-supply choices, which may be restrictive if intra-household bargaining matters for labor supply and welfare measurement. 

A fifth limitation is that the welfare analysis remains at the level of individual/household money-metric welfare changes. The paper does not provide a decomposition of welfare inequality into preferences, circumstances, job opportunities, and pay schedules beyond the particular CV versus CVcirc comparison. 

# Relevance for my JMP

## possible use for framing

This paper is extremely useful for framing because it shows that fairness measurement under tax reform can be made empirical rather than merely axiomatic. It gives you a concrete example of how to ask whether responsibility-sensitive corrections materially change welfare evaluation. 

## possible use for model design

It is highly useful for model design. The key lesson is that a structural job-choice model can serve as the empirical backbone of a fairness-sensitive welfare analysis, because it separates preferences from opportunities more naturally than a conventional discrete-choice labor-supply model. 

## possible use for identification

High relevance. The paper shows one credible route to identifying a responsibility-sensitive welfare metric from microdata: estimate a model that separates preference shifters from opportunity measures, then perform counterfactual welfare calculations under alternative reference assignments. 

## possible use for welfare measurement

This is the strongest relevance margin. The paper is directly about how to construct and compare welfare metrics that either fully respect preferences or neutralize them for fairness reasons. That is almost exactly the kind of problem your project faces, though in a different notation and with a tax-reform application. 

## possible use for decomposition

Moderate to high relevance. The paper does not give a full (R)-(A)-(y) decomposition, but it does provide a concrete welfare comparison that isolates the role of preference heterogeneity. It is therefore a partial decomposition device, and one that could potentially be extended toward your broader framework. 

## possible use for comparative application

High relevance. The methodology is portable to other tax reforms and countries, provided a structural job-choice model and tax-benefit microsimulation are available. The paper itself explicitly says CVcirc could be used for other reforms and in future policy design. 

# Research questions this paper inspires

Can one construct an analogue of CVcirc that neutralizes opportunity heterogeneity rather than preference heterogeneity, and then compare the two in a unified fairness decomposition?

Can the appendix’s proposed (CV^{pref}) measure be fully implemented empirically, so that the relative importance of preferences and opportunities can be compared directly in tax-reform welfare analysis?

How would the results change if the welfare metric were built on actual feasible job sets (A_i) rather than on latent opportunity densities (Q(h))?

Can one embed CV, CVcirc, and CE-type welfare changes into a single (W(z,R,A;y)) framework and derive axiomatic conditions under which they coincide or diverge?

Does responsibility matter more in welfare measurement for reforms that strongly affect labor supply at the bottom or middle of the distribution than for a bracket-tax reform like the Norwegian one studied here?

# Challenge to this paper

The strongest challenge is that the paper claims to assess how much responsibility matters, but in the main empirical implementation it only neutralizes one side of the fairness dyad: preference heterogeneity. Since the model is actually rich enough to represent opportunity heterogeneity, the absence of a full empirical implementation of the opportunity-neutralizing counterpart leaves the fairness analysis incomplete. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper uses a structural job-choice model in which households have heterogeneous preferences over leisure and labor and face latent job opportunities that arise from circumstances. It then computes welfare changes under different fairness-sensitive reference assignments. 

[reasonable inference for my project] The mapping into your notation is unusually natural. The realized bundle (z) corresponds to the chosen job-hours-consumption outcome; (R) corresponds to the household’s labor-leisure preferences; (A) corresponds to the latent opportunity structure (B(h)) or its summary through (Q(h)); and (y) corresponds to the wage/tax schedule entering disposable income through the tax-benefit function. supported by 

[explicit in paper] The paper is explicitly about responsibility versus circumstances in welfare measurement, and the empirical implementation focuses on reference preferences. It is therefore very close to the fairness-measurement problem, though not framed with your axioms. 

[unclear from paper] The paper does not formulate axioms such as Full Compensation, Independence of (A), IIJ, IPIJ, Responsibility for Equal Pay, or Compensation for Reference Preferences in your exact terminology. It also does not characterize a general (W(z,R,A;y)) measure axiomatically. 

[reasonable inference for my project] Relative to your framework, this is one of the closest empirical bridge papers in the corpus. It does not yet deliver the full jobs-and-wellbeing theory, but it shows concretely how fairness-sensitive welfare changes can be computed from a structural model in which both preferences and opportunities are present. supported by 

# Relation to Bargain et al. (2013)

This paper is closely related to the Bargain-type tradition of structural labor-supply welfare analysis, but it departs from it in a decisive way. Instead of stopping at standard money-metric welfare measurement under heterogeneous preferences, it asks whether one should neutralize preference heterogeneity for fairness reasons and compares the resulting welfare distributions. In that sense, it extends the labor-supply welfare literature toward a responsibility-sensitive direction. 

# Relation to opportunities vs preferences

This paper is directly about the opportunities-versus-preferences distinction, but asymmetrically. On the modeling side, it treats both: preferences are in the labor-leisure utility component, and opportunities are in the latent job-opportunity structure. On the welfare-measurement side, however, the main empirical comparison neutralizes preferences rather than opportunities. 

So the paper is highly relevant to your core distinction. It shows that one can build an empirical welfare analysis where both preferences and circumstances are present in the positive model. It also shows that, for one particular reform, neutralizing preferences matters only at the top of the income distribution. What remains open is the symmetric question of how much opportunity heterogeneity matters when it is the component neutralized. 

# Useful quotations / formulas

The paper’s central idea is already in the abstract: it proposes a new method “that measures the importance of preferences in the distribution of welfare in the context of tax reforms” by comparing standard CV to a new (CV^{circ}). That is the cleanest summary of the contribution. 

A central formal definition is
[
CV^{circ}:
\quad
\max u_{\text{pre}}(\cdot;\bar R)=\max u_{\text{post}}(\cdot + CV^{circ};\bar R),
]
implemented in the paper by setting taste-modifying variables at sample median and imposing a common error term. Equation (4.13) and Appendix D.2 are the relevant formal references. 

The *chart in Figure 4 on page 18* is especially important. Panel (A) shows that CV and CVcirc are almost identical through decile 9 and diverge only in decile 10. Panels (C) and (D) show that the divergence is driven mainly by female labor-supply adjustments under reference preferences. 

The *chart in Figure 5 on page 21* is also highly informative. It shows that the distribution of welfare effects under (\Delta CE) closely tracks the distribution under CVcirc, which strengthens the paper’s claim that its new measure is aligned with an established fairness criterion. 

# Suggested tags

responsibility-sensitive-welfare, compensating-variation, circumstance-CV, conditional-equality, job-choice-model, structural-labor-supply, fairness-measurement, Norway, tax-reform, latent-opportunities

# My quick takeaway

This is one of the most relevant empirical papers in your corpus. It does not solve the full axiomatic jobs-and-wellbeing problem, but it provides a concrete empirical bridge between structural labor-supply modeling and fairness-sensitive welfare measurement. Its most important substantive result is that, for the Norwegian bracket-tax reform, neutralizing preference heterogeneity changes the welfare distribution only at the very top. Its most important methodological value for your project is that it shows how a model containing both preferences and latent opportunities can be used to compute alternative welfare metrics that reflect different views of fairness.
