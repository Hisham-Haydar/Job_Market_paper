---

title: "Equality of opportunity: A progress report"
authors: ["John E. Roemer"]
year: 2002
outlet: "Social Choice and Welfare"
country_or_context: "General normative framework with empirical illustrations for the United States and 10–11 OECD countries"
population: "Abstract populations partitioned into types; empirical illustrations use young men in the United States and young men in several OECD countries"
data_period: "US education-finance illustration uses young men aged 16 in the late 1960s; cross-country fiscal illustration uses panel data for 10–11 OECD countries [exact years not stated in this article]"
shelf: "equality_of_opportunity_theory_and_policy"
tags: ["equality of opportunity", "circumstances and effort", "responsibility", "non-welfarist", "educational finance", "tax and transfer", "types", "quantile effort", "Roemer"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Roemer, John E. 2002. “Equality of opportunity: A progress report.” *Social Choice and Welfare* 19(2): 455–471. 

# One-sentence contribution

The paper formalizes equality of opportunity as equalization of outcomes across circumstance-defined types at fixed effort ranks, develops a non-welfarist policy objective based on that idea, and illustrates it with applications to US educational finance and cross-country tax-transfer systems. 

# Why this paper matters

This paper matters because it is one of the clearest statements of Roemer’s responsibility-sensitive equality-of-opportunity program in a form directly usable for policy analysis. It does not stop at philosophical distinction between circumstances and effort; it proposes an operational social objective and shows how it can be computed from data under explicit assumptions. 

For your project, it is especially important because it sharply separates ethically compensable disadvantage from responsibility-sensitive variation. That is not yet your (W(z,R,A;y)) framework, but it is one of the most important references for the general logic of “compensate circumstances, respect effort.” It is also directly useful because it is explicitly non-welfarist: equal-opportunity policy depends on how outcomes are distributed across types and effort ranks, not only on final outcome levels. 

# Core research question

How should equality of opportunity be formalized when society wants both to compensate for arbitrary circumstances and to hold individuals responsible for effort, and what policy recommendations follow when that principle is applied to education finance and tax-transfer systems? 

# Economic setting and context

The paper is a progress report rather than a single applied study. It begins from a broad normative question—what equal opportunity means—and then presents two empirical illustrations. The first concerns educational finance in the United States and equal opportunities for wage-earning capacity among young men. The second concerns how well tax-and-transfer systems in a set of OECD countries equalize opportunities for income acquisition across family-background types. 

The motivating ethical picture is the “level the playing field” metaphor. Roemer explicitly says that equal-opportunity policy should neutralize disadvantages due to circumstances and then allow outcome differences due to effort. He contrasts this with both older “equality of opportunity sets” approaches and with equality-of-outcome ethics. This framing appears in the introduction on pages 455–457. 

# Model / theoretical framework

The model is a normative policy framework. Outcomes are represented by a function (u(C,e,\varphi)), where (C) denotes circumstances, (e) effort, and (\varphi) policy; (u) need not be welfare in the economist’s narrow sense and may instead be income, life expectancy, or wage-earning capacity. Individuals are partitioned into finitely many types according to circumstances, and for any policy there is a type-specific effort distribution (F^t). Pages 457–458 define this setup. 

The distinctive move is the treatment of effort. Roemer argues that absolute effort is not the correct morally relevant comparison across types, because the distribution of effort itself is partly a characteristic of type. He therefore defines comparable effort by rank: two individuals in different types are treated as having exerted the same morally relevant effort if they occupy the same quantile of their type-specific effort distribution. Pages 458–459 are the key discussion. 

Let (v^t(\pi,\varphi)) denote the outcome of a type-(t) individual at effort quantile (\pi) under policy (\varphi). Equal opportunity then means equalizing outcomes across types at fixed (\pi), subject to the impossibility of doing so simultaneously for all (\pi). Roemer’s usual compromise is to maximize the integral of the lower envelope across effort quantiles:
[
\varphi^{EOp} = \arg\max_{\varphi}\int_0^1 \min_t v^t(\pi,\varphi), d\pi .
]
This is equation (2.2), and Figure 1 on page 460 illustrates it geometrically. 

The framework is explicitly normative and non-welfarist. Roemer emphasizes that unlike utilitarianism or Rawlsian maximin in their standard forms, equal opportunity cannot be computed from the set of outcome levels alone; it requires knowing how outcomes are distributed by type and effort rank. Pages 460–461 make this point explicitly. 

# Key objects

The key objects are circumstances, effort, policy, type, and the opportunity equalisandum (u(C,e,\varphi)). Circumstances are the factors for which individuals are not to be held responsible; effort consists of the factors for which they are to be held responsible; policy is the planner’s instrument. This is the core conceptual triad of the paper. 

A second key object is the type-specific effort distribution (F^t) and the associated effort-quantile index (\pi). Roemer’s crucial normative choice is to compare individuals across types by their effort ranks, not by their absolute effort levels. 

A third key object is the indirect outcome function (v^t(\pi,\varphi)), and the associated equal-opportunity objective obtained by integrating the minimum across types over (\pi). Figure 1 on page 460 and Figure 2 on page 463 provide the visual interpretation: choose the policy that maximizes the area under the lower envelope across type-specific outcome profiles or cumulative distributions. 

In the empirical applications, the main policy objects are per-pupil educational expenditures by type in the US case and affine tax-transfer systems (y=(1-a)x+c) in the OECD fiscal case. Tables 1–4 are the relevant policy summaries. 

# Data

The paper itself is partly theoretical and partly a survey of empirical work. In the US education-finance application, the data source is the National Longitudinal Study of Young Men. Roemer states that it contains parental education, school-district expenditure per capita at age 16, and wages at age 30; the sample concerns young men who were 16 in the late 1960s. This is on page 464. 

In the fiscal application, the paper refers to panel datasets for eleven countries: the United States, Britain, France, the Netherlands, Belgium, Germany, Spain, Italy, Denmark, Norway, and Sweden. The article does not state the exact panel years in the summary text. It uses prefisc and postfisc income distributions by parental-education types, and later augments circumstances with IQ for four countries using secondary data. Pages 466–469 summarize these datasets and constructions. 

# Identification logic

This is not a causal-identification paper in the reduced-form sense. The core logic is normative and structural. Roemer begins from an ethical decomposition of determinants into circumstances and effort, then imposes the rank-based comparability of effort, and then defines policy to maximize a type-sensitive equal-opportunity objective. 

There is, however, a concrete operational simplification. Roemer shows that if three assumptions hold—effort is identified with rank in the type distribution, effort is the residual determinant of outcomes once type and policy are fixed, and more effort raises outcomes ceteris paribus—then one can compute the equal-opportunity policy from the distribution of outcomes by type without directly observing effort. This is the main analytical content of Section 3, culminating in equation (3.2). 

A very important limitation is that assumption (2)—effort as the residual determinant once type and policy are fixed—is explicitly described by Roemer as “conservative” in a political sense, because it attributes to effort much that may in fact belong to unmodeled circumstances such as talent, sex, or race. Pages 462–463 state this with unusual candor. This is one of the most important methodological cautions in the paper. 

# Estimation / empirical strategy

The empirical strategy differs across the two applications. In the education-finance application, Roemer and Betts estimate type-specific outcome functions (v^t(\pi,x)), where the outcome is log wage at age 30 and the policy variable is per-pupil schooling expenditure. The type definition is based first on parental education only, and then on parental education crossed with race. The policy space is a vector of educational expenditures by type constrained by a fixed mean budget. Pages 464–466 and Tables 1–2 summarize the setup and results. 

In the fiscal application, the authors estimate the mapping from prefisc to postfisc income using an affine tax-transfer schedule (y=(1-a)x+c), where (a) is a marginal tax rate and (c) a transfer. They then define the feasible policy set as revenue-neutral affine tax systems and choose the one that maximizes the equal-opportunity objective. The observed system is compared to the optimal equal-opportunity system through a measure (v) of how much equality of opportunity the observed policy achieves. Pages 467–469 and Table 3 describe this. 

# Treatment of preferences

Preferences enter the paper mainly through the ethical distinction between responsibility and circumstance, and through the recognition that beliefs and preferences within a type are partly shaped by circumstances. This is exactly why absolute effort is rejected as the correct comparison across types and rank-based effort is adopted instead. Pages 458–459 are essential here. 

The paper therefore does not treat preferences as primitive objects to be respected unconditionally. Nor does it aggregate utilities in a utilitarian way. Instead, it asks which parts of outcome heterogeneity are morally attributable to circumstance and which to responsible effort. This is a distinctive responsibility-sensitive treatment, not a standard welfare-economics treatment. 

# Treatment of opportunities / constraints

This is a central strength of the paper, but one must be precise. The paper does not model feasible job sets, latent offers, or RURO-type opportunity distributions. It does not have an explicit (A_i)-object. Instead, opportunities are represented through circumstance-defined types and through the type-specific distributions of effort and outcomes under policy. 

Thus, the paper treats opportunity inequality indirectly rather than as literal feasible-set heterogeneity. Family background, race, and IQ are treated as circumstances generating unequal opportunity. The equal-opportunity objective then compensates across these circumstance types at fixed effort ranks. This is very useful for your project conceptually, but it is not a structural opportunity-set model. [reasonable inference for my project] supported by 

The paper clearly helps distinguish effort-responsibility from circumstance disadvantage. It does not distinguish preference heterogeneity from opportunity heterogeneity in the same way as a jobs-and-wellbeing or latent-jobs model would. It is therefore much closer to normative decomposition into “circumstances versus effort” than to empirical decomposition into “preferences versus feasible job sets.” 

# Welfare / normative object

The paper is explicitly normative and non-welfarist. Roemer states that utilitarianism and Rawlsianism, as formulated in the paper, are welfarist because they depend only on the set of outcome levels, whereas equal opportunity is non-welfarist because it depends on the distribution of outcomes by type and effort rank. Pages 460–461 make this explicit. 

The welfare or evaluative object is not utility in the conventional sense. It is the equal-opportunity objective that integrates, across effort ranks, the minimum outcome attained by any type at that rank. This is a responsibility-sensitive objective: it is egalitarian with respect to outcome differences due to type or circumstance, and permissive with respect to outcome differences due to effort. The discussion just after Figure 1 on page 460 states this clearly. 

This is directly useful for thinking about responsibility versus compensation. It is not, however, a measure of compensation for actual feasible job sets, reference opportunity sets, or opportunity menus. Nor is it a decomposition of welfare into preferences and opportunities in your specific sense. It is a circumstance-effort framework. 

# Main findings

The first main finding is conceptual. Roemer argues that equal opportunity should be understood as compensating for circumstances while holding people responsible for effort, and that morally relevant effort should be measured by rank within the type-specific effort distribution rather than by absolute effort. This is the central theoretical claim of Sections 1–3. 

The second main finding is methodological: under the paper’s three assumptions in Section 3, one can compute the equal-opportunity policy from outcome distributions by type, without direct observation of effort. Figure 2 on page 463 illustrates the objective geometrically as the area to the left of the lower envelope of type-specific distribution functions. 

The third main finding comes from the US educational-finance application. Table 1 on page 464 shows that with a common budget of $2,500 per pupil in 1989 dollars, the equal-opportunity allocation would have assigned roughly $5,360 to the most disadvantaged parental-education type and only $1,110 to the most advantaged type, with average wages 2.6 percent higher than under equal per-pupil spending. The text immediately below Table 1 states that this is about a five-to-one spending ratio. 

The fourth main finding is that a purely SES-based equal-opportunity policy would do very little to reduce racial inequality in US wages. Roemer reports that blacks were 38.1 percent of the lowest wage quintile in the actual data and would still have been 35.3 percent under the SES-only equal-opportunity education policy. Pages 465–466 and Table 2 then show that once race is explicitly included in the type definition, the recommended compensatory pattern becomes much stronger. 

The fifth main finding comes from the OECD fiscal comparison. Table 3 on page 469 reports that, relative to the paper’s equal-opportunity objective, Denmark, Norway, Sweden, the Netherlands, and Germany “overtax,” Belgium is essentially at the optimum, and the worst performers are Italy, the United States, and Britain. A striking result is that for Norway, Denmark, Sweden, and Germany the optimal equal-opportunity marginal tax rate is zero in the affine system considered, because prefisc inequality across parental-education types is already small enough that further taxation is not worthwhile under the maintained structure. 

The sixth main finding is that adding IQ as an additional circumstance changes some, but not all, country conclusions. Table 4 on page 470 shows that the Netherlands no longer overtaxes once IQ is included, whereas Denmark and Sweden still do, implying that these countries more than compensate even for disadvantage associated with low parental education and below-average intelligence under the paper’s specification. 

# Main limitations

The first major limitation is the definition of effort. Roemer explicitly acknowledges that effort is treated as the residual determinant of outcomes once type and policy are fixed, and that this necessarily misattributes some unmodeled circumstances to effort. This is not a minor technical issue; it is the paper’s own stated conservative bias. 

A second limitation is the narrow treatment of circumstances in the applications. In practice, the paper uses parental education, race, and IQ in relatively coarse categories. Roemer himself notes that if one refined these categories further, the amount of measured equal-opportunity inequality might increase and the policy recommendations could become even more compensatory. Pages 469–471 make this explicit. 

A third limitation for your project is that opportunities are not modeled as actual feasible sets. The framework is ethically rich, but structurally thin on the opportunity side. It has no explicit job menu, no wage-offer distribution, and no person-specific opportunity correspondence. [reasonable inference for my project] supported by 

A fourth limitation is that the empirical applications are simplified. The fiscal comparison restricts policy to one-dimensional affine tax systems, and Roemer explicitly notes that if one optimized over a richer policy space, no country might achieve full equality of opportunity. Page 469 states this clearly. 

# Relevance for my JMP

## possible use for framing

This paper is extremely useful for framing. It gives one of the clearest formulations of the responsibility-sensitive intuition that outcome inequality should be decomposed into an ethically compensable part due to circumstances and a responsibility-sensitive part due to effort. That is directly relevant to the normative positioning of your JMP. 

## possible use for model design

It is useful for model design mainly on the normative layer. It shows how a policy objective can be constructed once one partitions determinants into circumstances and effort. It is not useful as a direct structural model of jobs, offers, or labour supply. [reasonable inference for my project] supported by 

## possible use for identification

Its main use here is conceptual discipline. The paper forces the researcher to declare what is being treated as circumstance and what as effort, and it makes clear that residualization is ethically loaded. That is an important lesson if your project ever operationalizes responsibility-sensitive empirical exercises. [reasonable inference for my project] supported by 

## possible use for welfare measurement

It is highly useful. The equal-opportunity objective is an explicit non-welfarist welfare criterion, sitting between utilitarianism and Rawlsianism. It is especially valuable because it is not outcome-blind to responsibility: it is egalitarian across types at fixed effort rank, but not across differential effort. 

## possible use for decomposition

This is one of the paper’s strongest contributions. It provides a normative decomposition between circumstances and effort, even if the empirical implementation is imperfect. It does not give your preferred preferences-versus-opportunities decomposition, but it is one of the core references for a responsibility-sensitive decomposition of inequality. 

## possible use for comparative application

It is useful comparatively. The cross-country fiscal application is explicitly comparative and gives a way to compare how much different tax-transfer systems equalize opportunity as defined by circumstance types. This is not your eventual comparison object, but it is a meaningful precedent. 

# Research questions this paper inspires

How should Roemer’s circumstance-effort decomposition be reformulated when individuals face heterogeneous feasible job sets (A_i) rather than only type-specific outcome distributions?

Can one combine Roemer’s rank-based notion of responsible effort with a latent-jobs labour-supply model so that equal-opportunity policy is sensitive both to effort and to actual opportunity sets?

How much of measured “effort” in Roemer-style applications disappears once one models unobserved opportunity constraints explicitly rather than treating them as residuals?

Can one define a jobs-and-wellbeing analogue of Roemer’s (v^t(\pi,\varphi)) in which type depends on circumstances and (A_i), while effort is ranked within type-specific feasible environments?

Would a responsibility-sensitive tax or transfer criterion change materially if the relevant disadvantage were opportunity deprivation rather than parental background alone?

# Challenge to this paper

The strongest challenge is that the paper operationalizes responsibility by rank within type-specific residual outcome distributions, but it does not model whether observed low outcomes arise from effort, taste, luck, or lack of feasible opportunities once the chosen circumstance variables are conditioned on. This means the framework is normatively attractive but empirically fragile when applied to labour-market environments with rich opportunity heterogeneity. For your project, that fragility matters greatly. [reasonable inference for my project] supported by 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] Roemer’s framework distinguishes outcomes, circumstances, effort, and policy. Its central ethical claim is that policy should equalize outcomes across types at fixed effort ranks, where types are defined by circumstances and effort is measured by quantile within the type-specific effort distribution. 

[reasonable inference for my project] This is strongly relevant to your framework because it provides a formal template for distinguishing ethically compensable heterogeneity from responsibility-sensitive heterogeneity. In your notation, it is most naturally related to the distinction between (R)-like and (A)-like sources of inequality, although Roemer himself does not formulate the model that way. 

[explicit in paper] The paper does not define well-being as (W(z,R,A;y)), does not model feasible job sets (A_i), and does not separate preferences from opportunities structurally. Its typology is built from circumstances such as parental education, race, and IQ, not from job menus or latent opportunities. 

[reasonable inference for my project] In your taxonomy, the paper is closest to responsibility-versus-compensation reasoning, not to independence of (A), independence of (y), or laissez-faire-type measures. It is also not about reference opportunity sets. Its real value is to supply the ethical logic that unequal outcomes should be decomposed before evaluation, even if the decomposition variables in your project will differ. 

[unclear from paper] It is unclear how Roemer’s effort-rank method should be modified when the relevant disadvantage is not only circumstance but also person-specific feasible job-set restriction. The paper does not address that problem. 

# Relation to Bargain et al. (2013)

The connection is indirect but relevant. Bargain-type work is closer to structural welfare analysis using labour-supply models with heterogeneous preferences, whereas Roemer provides a non-welfarist, responsibility-sensitive normative criterion. For your purposes, Roemer is not a substitute for structural labour-supply welfare comparisons; he is a normative benchmark for how to separate compensable from non-compensable inequality before one aggregates welfare. [reasonable inference for my project] 

# Relation to opportunities vs preferences

The paper is much stronger on circumstances versus effort than on opportunities versus preferences. It does not structurally model preferences and opportunities as separate objects. Instead, it normatively partitions determinants into arbitrary circumstances and responsible effort, with the latter measured by relative rank within type. 

Still, it is highly relevant to your opportunities-versus-preferences agenda because it shows how strongly welfare conclusions depend on that decomposition. It is best read as a normative precursor: it gives the ethical template, but not yet the positive labour-market structure needed to distinguish preferences from actual opportunity sets. 

# Useful quotations / formulas

The central formal object is
[
u(C,e,\varphi),
]
where (C) is circumstances, (e) effort, and (\varphi) policy. This is the “opportunity equalisandum” and may represent income, life expectancy, or wage-earning capacity rather than utility narrowly understood. Page 457 is the key location. 

The equal-opportunity policy is usually defined by
[
\varphi^{EOp}=\arg\max_{\varphi}\int_0^1 \min_t v^t(\pi,\varphi), d\pi,
]
equation (2.2) on page 459. This formula captures the compromise between type egalitarianism and effort responsibility. 

The computational shortcut is equation (3.2), which rewrites the problem using inverse outcome distributions by type:
[
\varphi^{EOp}=\arg\max_{\varphi}\int_0^1 G_t^{-1}(\pi), d\pi
]
for the lower envelope logic described around Figure 2 on page 463. The precise notation in the article is garbled in the extracted text, but the substantive point is clear in the surrounding discussion. 

The most policy-relevant tables are Table 1 and Table 2 for the US education application, Table 3 for the OECD fiscal comparison, and Table 4 for the sensitivity to adding IQ as a circumstance. Figure 1 on page 460 and Figure 2 on page 463 are the best visual summaries of the equal-opportunity objective, while Figure 3 on pages 467–468 shows the noncrossing prefisc income distributions for the US, Spain, and Denmark. 

# Suggested tags

Roemer-EOp, circumstances-vs-effort, responsibility-sensitive-equality, rank-based-effort, non-welfarist-policy, educational-finance, fiscal-equality-of-opportunity, type-based-compensation, parental-background, affirmative-action

# My quick takeaway

This is a core normative paper for your corpus. Its main contribution is not a structural model of jobs or labour supply, but a powerful and operationalized ethical framework: compensate for circumstances, respect effort, and compare effort by rank within type rather than by absolute level. For your JMP, it is especially valuable as the responsibility-sensitive benchmark against which more opportunity-explicit models can be judged. Its main weakness for your purposes is that it lacks an explicit (A)-object, so it cannot by itself tell you how to treat unequal feasible job sets.
