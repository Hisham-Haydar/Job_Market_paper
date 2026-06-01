---

title: "Happiness, Equivalent Incomes and Respect for Individual Preferences"
authors: ["Koen Decancq", "Marc Fleurbaey", "Erik Schokkaert"]
year: 2015
outlet: "Economica"
country_or_context: "Theoretical welfare-comparison framework with an empirical illustration for Russia"
population: "Individuals in the Russia Longitudinal Monitoring Survey (RLMS-HSE); unbalanced panel of 12,016 individuals"
data_period: "1995–2003"
shelf: "welfare_measurement_equivalent_income_preferences"
tags: ["equivalent income", "subjective wellbeing", "preferences", "interpersonal comparisons", "welfare measurement", "Russia", "RLMS-HSE", "life satisfaction", "individual sovereignty"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Decancq, Koen, Marc Fleurbaey, and Erik Schokkaert. 2015. “Happiness, Equivalent Incomes and Respect for Individual Preferences.” *Economica* 82: 1082–1106. 

# One-sentence contribution

The paper argues that subjective wellbeing scores cannot by themselves ground interpersonal comparisons of wellbeing because they may violate respect for common preferences, and it proposes instead an equivalent-income metric that uses SWB data only to recover ordinal preferences, with an empirical illustration on Russian panel data. 

# Why this paper matters

This paper matters because it is one of the cleanest statements of a distinction that is central for your project: SWB can be useful for recovering preference information, but it should not automatically be treated as a cardinal interpersonal welfare metric. The paper therefore separates the informational role of reported satisfaction from the normative role of a wellbeing index. 

It is especially relevant because it proposes an individual wellbeing metric—equivalent income—that is explicitly preference-respecting and interpersonally comparable. That makes it much closer to your (W(z,R,A;y))-type concerns than standard happiness economics, even though the paper does not model opportunities as feasible job sets. 

# Core research question

How should one make interpersonal comparisons of wellbeing when individuals have heterogeneous preferences, and can subjective wellbeing surveys be used in a way that respects individual preferences without collapsing wellbeing into raw satisfaction scores? 

# Economic setting and context

The paper sits in welfare economics and social choice rather than labor supply or microsimulation per se. Its point of departure is the growing use of happiness and life-satisfaction data in economics, both for valuing non-market goods and for broader welfare comparisons. The authors explicitly question the move from “SWB as information” to “SWB as metric.” 

The empirical illustration uses Russian panel data from the RLMS-HSE over 1995–2003, a period of substantial economic turbulence. This matters because the data contain large within-person changes in living conditions, allowing the authors to estimate satisfaction equations with individual fixed effects and to study how alternative wellbeing metrics rank individuals. 

# Model / theoretical framework

The model class is an axiomatic interpersonal-comparison framework combined with an empirical satisfaction-based preference-recovery exercise. Individual situations are described by a vector of life dimensions (\ell_i) or, more specifically, by ((y_i,q_i)), where (y_i) is income/expenditures and (q_i) is a vector of non-income quality-of-life dimensions. Individuals have preference orderings (R_i) over these life dimensions and satisfaction functions (S_i) representing those orderings. 

The framework is explicitly normative. The authors formulate principles for interpersonal wellbeing comparisons. The personal-preference principle requires intrapersonal comparisons to respect individual preferences. The same-preference principle requires interpersonal comparisons with common preferences also to respect those preferences. The weak dominance principle then yields an equivalent-income representation when combined with the personal-preference principle. Pages 5–9 are the theoretical core. 

What the agent “chooses” is not modeled behaviorally in the usual labor-supply sense. This is not a positive choice model. Instead, the theory assumes individuals have informed preferences over aspects of life and asks how wellbeing should be measured. The feasible set is not modeled explicitly. The framework is normative first, empirical second. 

# Key objects

The central objects are the preference ordering (R_i), the satisfaction function (S_i(\ell_i)), the scaling factors (s_i) that affect how individuals translate life situations into reported SWB, and the equivalent income (y_i^*). The critical conceptual move is to distinguish preferences from scaling factors. This is what allows the authors to say that satisfaction scores may respect ordinal preferences within a person while still failing as interpersonal welfare metrics. 

The core wellbeing object is equivalent income, defined as the income level that, when combined with the best attainable non-income situation (q^*(y^*,R)), makes the individual indifferent to the actual bundle ((y,q)). The defining equation is
[
(y,q), I, (y^*, q^*(y^*,R)).
]
This is equation (1) in the paper and the central formal object for your purposes. 

A second key object is the empirical equivalent-income formula derived from the estimated satisfaction equation:
[
y^*_{it}
========

y_{it}\exp!\left(
\frac{(\vartheta+\Gamma Z_{it})'}{\beta+\Lambda Z_{it}}
(q_{it}-q_i^*)
\right),
]
reported as equation (5). This is the operational bridge from SWB data to a preference-respecting wellbeing measure. 

# Data

The empirical illustration uses the RLMS-HSE, an unbalanced Russian panel covering 1995, 1996, 1998, 2000, 2001, 2002, and 2003. After cleaning inconsistent information, the sample contains 12,016 individuals. The satisfaction regressions use 40,120 observations. 

The life-satisfaction variable is the standard “satisfaction with life in general at the present time” question on a five-point scale. The main non-income dimensions used in the benchmark equivalent-income measure are self-assessed health, housing quality, unemployment, and wage arrears, combined with equivalized expenditures. Table A1 reports descriptive statistics, and the benchmark choice of dimensions is discussed on pages 12–15. 

# Identification logic

Identification is not causal in the reduced-form treatment-effect sense. The theoretical identification comes from axioms: combining the personal-preference principle with the weak dominance principle yields equivalent income as the interpersonal-comparison metric. The empirical identification comes from the consistency assumption that SWB answers represent ordinal preferences, up to scaling and noise. 

Empirically, the key identifying variation comes from panel changes in expenditures and quality-of-life dimensions, together with interaction terms that allow preference heterogeneity across observable groups. Individual fixed effects and time dummies absorb persistent personality differences and common macro shocks. The authors are explicit that this identification remains limited: some variables may affect both preferences and scaling, fixed characteristics are difficult to handle with fixed effects, and only subgroup-average rather than fully individual preferences are recovered. Pages 10–12 are explicit about these limits. 

So the paper is transparent that it is identifying a workable preference-based welfare metric, not a deep structural preference model free of all confounds. [explicit in paper] 

# Estimation / empirical strategy

The empirical strategy has two stages. First, the authors estimate a satisfaction equation using ordered logit methods with individual fixed effects, following Ferrer-i-Carbonell and Frijters’ Chamberlain-style approach, simplified as in Jones and Schurer. The specification includes log expenditures, health, housing, unemployment, wage arrears, occupational status, education, marital status, reference-group variables, age, and interactions. Table A2 reports the estimates. 

Second, they use the estimated coefficients to recover group-specific marginal rates of substitution between income and non-income dimensions, determine the preferred reference values (q_i^*), and compute equivalent incomes for each observation using equation (5). They then compare the ranking implied by equivalent income with rankings based on expenditures, a simple objective index, and raw subjective satisfaction. Tables 2–5 are the core comparison tables. 

# Treatment of preferences

Preferences are the centerpiece of the paper. The authors explicitly reject a narrow revealed-preference interpretation and instead work with “informed judgments” over life dimensions. They emphasize that wellbeing measurement should respect these preferences, not merely reported feelings. Pages 1–4 and 6–8 are particularly clear on this point. 

The paper’s main normative claim is that SWB scores respect a weak version of individual sovereignty in intrapersonal comparisons but fail a stronger version needed for interpersonal comparisons, because scaling factors such as adaptation, shifting aspirations, and reference-group effects may differ across persons. This is why the same-preference principle is not satisfied by raw SWB scores. 

Empirically, preference heterogeneity is modeled through interaction terms in the satisfaction equation. For example, younger individuals value health less and expenditures more; males value health less and unemployment more negatively; higher-educated individuals react more negatively to unemployment and wage arrears; rural individuals value housing more. Figure 1 and Table A2 are important here. 

# Treatment of opportunities / constraints

This section is where the paper is relatively weak for your opportunity-set agenda. The model does not include explicit feasible sets, job opportunities, latent offers, or rationing. There is no analogue of an observed or latent (A_i) in the RURO sense. 

Non-income dimensions such as health, housing, unemployment, and wage arrears are treated as aspects of life that enter wellbeing, not as feasible-set primitives. The paper therefore helps think about multidimensional wellbeing and preference heterogeneity, but not about the distinction between preferences and feasible opportunities in a labor-market structure. [reasonable inference for my project] supported by 

Unemployment appears as a quality-of-life dimension in the empirical application, not as a model of constrained opportunities. This is an important difference from the Bargain–Caliendo–Haan–Orsini rationing paper or from RURO-type work. 

# Welfare / normative object

The paper is explicitly normative. Its welfare object is individual wellbeing measured by equivalent income, not subjective satisfaction and not income alone. This metric is justified by axioms intended to respect individual preferences in both intra- and interpersonal comparisons. 

This is directly relevant to your project’s interest in reference-based welfare measurement and the normative handling of heterogeneous preferences. The paper is especially important because it provides a preference-respecting interpersonal metric without assuming away heterogeneity in tastes. 

The paper is not about responsibility versus compensation for opportunities in the Fleurbaey–Maniquet unequal-skills sense, and it is not a decomposition paper into preferences, opportunities, and pay schedules. But it is central for the normative question of how to compare wellbeing across people when preferences differ. 

# Main findings

The first main finding is theoretical: subjective wellbeing scores can conflict with individuals’ own judgments in interpersonal comparisons because different scaling factors may lead equally satisfied people to rank life situations differently when they share the same preferences. The same-preference principle therefore rules out using raw SWB as the interpersonal wellbeing metric. Pages 5–8 are central here. 

The second main finding is constructive: the combination of the personal-preference principle and the weak dominance principle yields equivalent income as the relevant interpersonal-comparison metric. This is the paper’s core theoretical contribution. 

The third main finding is empirical: equivalent incomes are only moderately correlated with expenditures and weakly correlated with SWB. For the year 2000, the rank correlation between equivalent income and expenditures is 0.48, between equivalent income and the objective measure 0.64, and between equivalent income and subjective satisfaction only 0.25. Tables 2–4 report these comparisons. 

The fourth main finding is distributive: different metrics identify different groups as worst off. Table 5 shows that the least satisfied Russians are younger, better educated, more likely male, less likely minority, and have higher expenditures, better health, and better housing than the individuals identified as worst off by equivalent income. Conversely, the lowest-equivalent-income group is much poorer in objective living conditions. This is one of the most important substantive results. 

The fifth main finding is that equivalent-income rankings are relatively stable to the incremental inclusion of additional life dimensions, but they differ sharply from both the expenditures ranking and the raw-satisfaction ranking. Table 5 shows especially large turnover when moving from expenditures-only to equivalent income with health included, and again when moving from equivalent income to raw satisfaction. 

# Main limitations

A first limitation is that the empirical implementation identifies only subgroup-average preferences, not fully individual preferences. The authors are explicit about this. That matters if fine-grained heterogeneity is central. 

A second limitation is the potential confounding of preferences and scaling. Variables such as education may affect both aspirations/scaling and genuine preferences, and the paper cannot cleanly separate the two with the available data. The authors say this directly. 

A third limitation, relative to your project, is the absence of explicit opportunity sets. Equivalent income here is defined over income and non-income functionings, not over realized bundles and feasible job menus. That makes it a powerful welfare-measurement paper, but not yet an opportunity-sensitive one. [reasonable inference for my project] supported by 

A fourth limitation is that the set of relevant life dimensions is partly judgment-based. The authors acknowledge that different choices about what belongs in (\ell_i) or in the scaling factors can affect results, even if some qualitative conclusions appear robust. 

# Relevance for my JMP

## possible use for framing

This is one of the best framing papers for the claim that wellbeing measurement should not rely mechanically on either income or subjective satisfaction. It gives a rigorous preference-respecting alternative.

## possible use for model design

It is useful mainly for the welfare-measurement layer of your model design. It suggests how an individual wellbeing index can be built from preferences over multiple dimensions without assuming homogeneous tastes.

## possible use for identification

It is useful as a template for recovering ordinal preference information from SWB data while refusing to treat SWB itself as the final welfare metric. That distinction is highly valuable methodologically.

## possible use for welfare measurement

This is the paper’s strongest contribution. It is directly relevant if you want a wellbeing metric that respects heterogeneous preferences and remains interpersonally comparable.

## possible use for decomposition

It is moderately useful. It does not provide an (R/A/y) decomposition, but it does show how rankings change when one moves from raw income or raw SWB to a preference-based equivalent-income measure.

## possible use for comparative application

Moderate directly, since the empirical illustration is Russia-only. Strong indirectly, because the theoretical framework is portable to other countries and datasets.

# Research questions this paper inspires

1. Can equivalent income be extended from a ((y,q)) framework to a jobs-and-wellbeing measure (W(z,R,A;y)) where feasible job sets (A) enter directly?

2. How much of the gap between raw SWB rankings and equivalent-income rankings in labor-market data is driven by opportunity constraints rather than by preference heterogeneity?

3. Can one combine RURO-style estimation of feasible job opportunities with Decancq–Fleurbaey–Schokkaert-style preference-respecting equivalent wellbeing?

4. What is the correct reference analogue of (q^*(y,R)) when non-income dimensions include job characteristics that are not universally attainable?

5. How robust are preference-based wellbeing rankings when the distinction between true life dimensions and scaling factors is itself ambiguous?

# Challenge to this paper

The strongest challenge is that the paper solves the interpersonal-comparison problem for heterogeneous preferences much more convincingly than it solves the empirical problem of separating preferences from scaling and omitted dimensions. The theory is sharp; the empirical implementation is necessarily partial. For your project, that means it is a strong normative benchmark but not a fully identified empirical welfare technology. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper proposes a preference-respecting interpersonal wellbeing metric based on equivalent income and argues that raw subjective satisfaction is normatively insufficient for interpersonal comparisons. It is directly concerned with how wellbeing should depend on individual preferences and observed life dimensions. 

[reasonable inference for my project] In your notation, the paper is closest to the (z)- and (R)-parts of the problem. The realized bundle (z) would correspond here to the observed income and non-income life dimensions ((y,q)). Preferences (R) are central. The pay schedule (y) is present only as income or expenditures, not as a job-specific wage schedule. The feasible set (A) is essentially absent as an explicit object. 

[unclear from paper] The paper does not define wellbeing as (W(z,R,A;y)), does not analyze actual versus reference opportunity sets, and does not study independence of (A), IIJ, IPIJ, or responsibility for opportunities. Those issues are outside its scope. 

[reasonable inference for my project] In your taxonomy, the paper is very close to the preference-respecting welfare-measurement side of the project and to reference-based evaluation. It is not close to independence of (A), not because it rejects it, but because (A) is not modeled. It is therefore a strong benchmark for the (R)-side of your framework and a weak one for the opportunity-set side. 

# Relation to Bargain et al. (2013)

This paper is closely related in spirit to Bargain et al. (2013), but it is more explicit and philosophically sharper about why heterogeneous preferences matter normatively. Bargain et al. studies alternative welfare metrics in the consumption-leisure space under heterogeneous preferences. Decancq et al. provides a broader and more foundational argument for equivalent-income style comparison, using SWB only as a source of ordinal preference information and explicitly rejecting raw SWB as the interpersonal welfare metric. It is therefore highly relevant as a conceptual complement and, in some ways, a deeper normative foundation for that literature.

# Relation to opportunities vs preferences

This paper is much stronger on preferences than on opportunities. It is one of the best papers in your corpus for showing how interpersonal wellbeing comparisons should be adjusted when preferences differ across persons. 

But it does not model opportunities as feasible sets, job offers, or labor-market constraints. So it should not be read as a full solution to the opportunities-versus-preferences problem. It is best read as a high-level benchmark for the “preferences” side that would need to be combined with a richer (A)-sensitive framework for your JMP. 

# Useful quotations / formulas

The central defining equation for equivalent income is
[
(y,q), I, (y^*, q^*(y^*,R)).
]
This is equation (1) and the core welfare object of the paper. 

The key empirical formula is
[
y^*_{it}
========

y_{it}\exp!\left(
\frac{(\vartheta+\Gamma Z_{it})'}{\beta+\Lambda Z_{it}}
(q_{it}-q_i^*)
\right),
]
equation (5), which operationalizes equivalent income using estimated preference parameters from the satisfaction equation. 

Table 5 is especially important. It shows that the least satisfied individuals are not the same as those with the lowest equivalent incomes, and that the SWB-identified worst off are in several respects objectively better situated than the equivalent-income-identified worst off. 

# Suggested tags

equivalent-income, subjective-wellbeing, interpersonal-comparisons, heterogeneous-preferences, individual-sovereignty, welfare-measurement, Russia, RLMS-HSE, happiness-economics, Decancq-Fleurbaey-Schokkaert

# My quick takeaway

This is a core paper for the welfare-measurement side of your project. Its main value is not labor-supply modeling or opportunity-set analysis, but a rigorous argument that raw satisfaction should not be used directly as interpersonal wellbeing, together with a workable preference-respecting alternative. For your JMP, it is especially valuable as a benchmark for how to treat heterogeneous (R) seriously while keeping the welfare metric interpersonally comparable.
