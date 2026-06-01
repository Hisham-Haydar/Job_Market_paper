---

title: "Beyond GDP? Welfare across Countries and Time"
authors: ["Charles I. Jones", "Peter J. Klenow"]
year: 2016
outlet: "American Economic Review"
country_or_context: "Cross-country and over-time welfare comparisons; detailed micro-data exercise for 13 countries and broader macro-data exercise for 152 countries"
population: "National populations; micro analysis uses household survey samples from 13 countries, macro analysis covers 152 countries"
data_period: "Main micro cross-country comparison uses survey years around the 2000s; growth comparisons span earlier decades to the mid-2000s; macro panel emphasizes 1980–2007"
shelf: "welfare_measurement_cross_country"
tags: ["welfare measurement", "consumption-equivalent welfare", "GDP", "cross-country comparison", "mortality", "leisure", "inequality", "expected utility", "macro welfare", "micro data"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Jones, Charles I., and Peter J. Klenow. 2016. “Beyond GDP? Welfare across Countries and Time.” *American Economic Review* 106(9): 2426–2457. 

# One-sentence contribution

The paper proposes a consumption-equivalent welfare measure that combines consumption, leisure, mortality, and inequality, and shows that while this measure is highly correlated with GDP per capita, welfare differences across countries and over time can diverge substantially from GDP comparisons, especially because of mortality, leisure, and inequality. 

# Why this paper matters

This paper matters because it gives a disciplined welfare statistic that goes beyond GDP while remaining squarely within standard expected-utility economics. Rather than adding ad hoc indicators, it prices differences in leisure, survival, and inequality in consumption-equivalent units, making the final object directly comparable across countries and over time. 

For your project, the paper is useful above all as a benchmark on welfare measurement. It does not speak to job opportunity sets or responsibility-sensitive fairness directly, but it is an important example of how an explicit welfare object can be constructed from observable outcomes rather than simply equating welfare with income. It is especially relevant for thinking about what a welfare statistic includes, and what it leaves out. 

# Core research question

Can one construct a simple, economically grounded summary statistic of a country’s welfare that improves on GDP per capita by incorporating consumption, leisure, mortality, and inequality, and how much does such a measure alter cross-country and time-series comparisons of living standards? 

# Economic setting and context

The paper is set in a broad comparative macroeconomic context. It compares standards of living across countries and over time, beginning with a detailed micro-data exercise for 13 countries and then extending the analysis to a macro-data exercise for 152 countries. Its motivating examples include the comparison of France and the United States and the broader contrast between Western Europe, emerging Asia, and poorer developing regions. 

The authors position the paper explicitly as a response to the shortcomings of GDP as a welfare measure. The opening pages state that GDP omits or treats imperfectly many important determinants of living standards, and the paper deliberately focuses on the subset—consumption, leisure, mortality, and inequality—that can be incorporated using standard expected-utility tools. 

# Model / theoretical framework

The model is an expected-lifetime-utility framework used to compute a consumption-equivalent welfare index. A fictitious individual, called “Rawls” by the authors, draws from the cross-sectional distributions of consumption and leisure and from age-specific mortality schedules in a given country. Expected lifetime utility is
[
U = E\sum_{a=1}^{100}\beta^a u(C_a,\ell_a)S(a),
]
where (C_a) is consumption, (\ell_a) is leisure plus home production, (S(a)) is survival to age (a), and the expectation integrates over uncertainty in consumption and leisure. Welfare is then defined as the consumption-equivalent factor (\lambda_i) satisfying (U_{us}(\lambda_i)=U_i(1)). 

The framework is positive with welfare applications. It is positive in the sense that it uses observed distributions of consumption, leisure, and mortality. It is welfare-oriented because the target object is a utility-based welfare statistic, not merely a descriptive index. It is not an axiomatic fairness framework: the paper explicitly evaluates all countries using a common preference specification rather than deriving the welfare criterion from fairness principles. 

The benchmark flow utility is additively separable in log consumption and leisure,
[
u(C,\ell)=\bar u+\log C+v(\ell),
]
with (v(\ell)) chosen to imply a constant Frisch elasticity of labor supply in the benchmark calibration. The paper also studies more general nonseparable CRRA/CFE preferences in robustness analysis. 

# Key objects

The central welfare object is the consumption-equivalent welfare index (\lambda_i), defined as the proportional adjustment to US consumption that makes expected utility in the United States equal to expected utility in country (i). This is the paper’s summary statistic of welfare. 

A second key object is the decomposition of welfare relative to GDP. In the micro-data formulation, log welfare relative to income is additively decomposed into contributions from life expectancy, the consumption share of GDP, leisure, consumption inequality, and leisure inequality. Equation (19) is the key decomposition. 

A third key object is the distinction between equivalent variation and compensating variation. The baseline uses equivalent variation and therefore values life-expectancy differences using a country’s own flow utility; the authors explicitly note that compensating variation would weight survival differences by US flow utility and produces larger welfare gaps for very poor countries. 

# Data

The paper uses two empirical layers. The first is a detailed micro-data exercise based on household surveys for 13 countries: the United States, Brazil, China, France, India, Indonesia, Italy, Malawi, Mexico, Russia, South Africa, Spain, and the United Kingdom. Table 1 lists the survey sources, years, and sample sizes. The micro datasets allow the authors to compute consumption inequality, hours worked, and age-specific household outcomes more consistently across countries. 

The second is a macro-data exercise for 152 countries. For this broader exercise, the paper uses Penn World Table 8.0 for income, consumption, employment, and population; the UNU-WIDER World Income Inequality Database for inequality; and the World Bank HNPStats data for life expectancy. This second layer is much coarser and relies on stronger assumptions, such as lognormal consumption and simpler mortality treatment. 

# Identification logic

The paper is not an identification paper in the structural or causal sense. It does not attempt to identify deep preference parameters from policy variation, nor does it isolate causal effects of institutions or reforms. Instead, it calibrates a welfare function and computes welfare differences directly from observed cross-country distributions of consumption, leisure, inequality, and mortality. 

The crucial assumptions are therefore model-based rather than design-based. These include: a common preference specification across countries, the treatment of individuals as drawing from cross-sectional country distributions over their lifetime, the chosen discounting and growth assumptions, the calibration of the utility weight on leisure and the intercept in flow utility, and the chosen value of life used to pin down the utility intercept. The paper is clear that many limitations remain, including the omission of morbidity, environmental quality, crime, and political freedom. 

If identification is understood more broadly as “what permits the welfare statistic to be computed,” then the answer is: observed country distributions plus a common expected-utility model. This is a calibrated welfare-accounting exercise, not a causal or structural identification exercise. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The empirical strategy is welfare accounting rather than estimation in the usual econometric sense. In the micro-data exercise, the authors compute expected utility directly from age-specific cross-sectional micro distributions of consumption and leisure, combined with mortality schedules, and then solve for the consumption-equivalent (\lambda_i). This is the preferred exercise because it avoids imposing strong distributional assumptions on consumption and leisure. 

They then construct a macro approximation for 152 countries using a simplified formula based on the illustrative model in equation (7). This macro version assumes lognormal consumption, compresses mortality into life expectancy, and omits leisure inequality because of data limitations. The authors validate the macro exercise by comparing it with the micro results for the countries where both are available; Table 5 reports that the two are extremely close, with a correlation of 0.999 in log welfare. 

# Treatment of preferences

Preferences are imposed rather than estimated. The paper explicitly assumes a common preference specification for all countries and uses a fictitious representative evaluator, “Rawls,” to rank country allocations. This means that the welfare comparisons do not reflect country-specific tastes or heterogeneous normative standards. 

This is a major modeling choice. It is useful for comparability, because it ensures that all countries are evaluated by the same welfare yardstick. But it also means that the paper does not ask whether preferences differ systematically across countries or whether welfare should be evaluated relative to country-specific preferences. The authors state this limitation explicitly. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly in the sense of feasible job sets, latent job offers, or opportunity correspondences. Leisure enters directly as a realized time-use outcome, and the paper treats hours worked and leisure as part of the outcome distribution rather than as the result of explicit constraints or opportunity sets. 

Similarly, the paper does not distinguish whether low consumption or low leisure reflects preferences, institutions, taxes, labor-demand conditions, household constraints, or job opportunities. All of these are folded into the observed outcomes used in the welfare calculation. This makes the paper strong on welfare measurement from realized outcomes, but weak on decomposing outcomes into preferences versus opportunities. 

The relevant constraints are therefore implicit and highly reduced-form. The paper observes country-level distributions of consumption, work, and survival, and evaluates them. It does not offer a model of how those allocations arise. [reasonable inference for my project] supported by 

# Welfare / normative object

The welfare object is a consumption-equivalent measure of expected lifetime utility. This is explicitly utility-based, not a composite index built from arbitrary weights. The paper is clear that it aims to improve on mashup indices such as the Human Development Index by grounding the aggregation in expected utility and consumption-equivalent analysis. 

The paper is therefore positive with welfare applications, not an axiomatic fairness paper. It does not derive the welfare criterion from social-choice axioms, does not discuss responsibility for preferences or opportunities, and does not construct a social welfare ordering over persons in the Fleurbaey–Maniquet sense. Its welfare notion is an aggregate expected-utility comparison across national distributions. 

For your project, this means the paper is very useful for understanding how a welfare statistic can differ sharply from GDP once mortality, leisure, and inequality are incorporated. But it is not useful for responsibility for opportunities, compensation for opportunity sets, or reference opportunity-set evaluation. Those issues are outside its scope. 

# Main findings

The first headline result is that welfare is highly correlated with GDP per person, but deviations are often substantial. The abstract states the high correlation and the main text reports that for the 13-country micro-data sample the median deviation is around 35 percent. In the micro comparison, France is the leading example: consumption is only 60 percent of the US level, but once life expectancy, leisure, and lower inequality are added, French welfare reaches about 92 percent of the US level. The discussion on pages 1–2 and Table 2 are central here. 

The second major result is that Western Europe is much closer to the United States in welfare than in income. In the micro exercise, France, Italy, Spain, and the UK all gain significantly relative to the United States because of longer lives, more leisure, and lower inequality. In the macro regional averages, Western Europe’s welfare is about 82 percent of the US level versus about 73 percent for income. Table 2 and Table 6 are the key locations. 

The third major result is that many developing countries are poorer than income suggests because of shorter lives, low consumption shares, and high inequality. The abstract and pages 2–3 emphasize that mortality is often the largest force. In the micro results, countries such as South Africa, Brazil, India, Indonesia, and Malawi all show welfare well below income. In the macro regional results, sub-Saharan Africa and Latin America are notably worse off in welfare terms than GDP alone implies. 

The fourth major result concerns growth. Welfare growth is typically higher than income growth because of rising life expectancy. In the abstract and on page 3, the authors report average welfare growth of 3.1 percent versus income growth of 2.1 percent over the relevant period. Table 3 for the micro exercise and Table 8 for the macro exercise show that rising life expectancy contributes about one percentage point to welfare growth in many regions, with sub-Saharan Africa as a major exception. 

The fifth major result is that some high-GDP economies look much less impressive in welfare once low consumption shares and low leisure are counted. The macro discussion around Singapore, Hong Kong, and South Korea is especially important. Table 7 shows Singapore with GDP per capita above the United States but welfare only about 57 percent of the US level because of low consumption share and low leisure, while Japan’s welfare growth looks much stronger than income growth because of rising life expectancy, rising consumption share, and rising leisure. 

# Main limitations

The paper’s first major limitation is that it imposes one common preference structure across countries. This is transparent and useful for comparability, but it suppresses the possibility that societies legitimately differ in preferences over consumption, leisure, or longevity. The authors explicitly acknowledge this limitation. 

A second limitation is omission. The paper does not include morbidity, environmental quality, public safety, political freedom, or other major determinants of well-being. The conclusion and introduction both acknowledge this. Hence the welfare measure is broader than GDP but still incomplete. 

A third limitation, especially relevant for your agenda, is that opportunities are absent as independent objects. The measure is built from realized outcomes, not from feasible sets. It therefore cannot separate whether low welfare reflects poor choices, bad opportunities, institutional failures, or preferences. [reasonable inference for my project] supported by 

A fourth limitation is that the macro extension requires strong approximations: lognormal consumption, simplified mortality treatment, and missing-data conventions. The paper argues that the macro exercise tracks the micro results surprisingly well, but the authors are explicit that the macro approach is cruder. Table 5 is the validation exercise. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing because it demonstrates, in a disciplined and widely legible way, that GDP is not itself a welfare measure. It can help justify why your project should distinguish realized earnings or consumption from a broader evaluative object. 

## possible use for model design

Its direct use for model design is limited, because it is not a structural labour-supply or job-choice paper. Indirectly, it is useful as a model of how to build a welfare statistic once one has decided which arguments matter—consumption, leisure, mortality, inequality—and how to put them into a common metric. [reasonable inference for my project] supported by 

## possible use for identification

It is not useful for causal identification of preferences or opportunities. Its value here is methodological discipline: define the welfare object first, then compute it from the best available observable distributions under transparent assumptions. [reasonable inference for my project] supported by 

## possible use for welfare measurement

This is the paper’s main contribution for your JMP. It provides a concrete example of a welfare statistic that is not reducible to income and yet remains economically interpretable. It is especially useful if you want to think about how to compare welfare across contexts using a single consumption-equivalent metric. 

## possible use for decomposition

It is useful for decomposition in a limited but real sense. The paper decomposes welfare differences into components due to life expectancy, the consumption share, leisure, and inequality. It does not decompose into preferences versus opportunities, but it does show how a welfare gap can be broken into interpretable parts. Equation (19), Table 2, and Table 6 are especially relevant. 

## possible use for comparative application

This is one of the strongest uses for your JMP. The paper is directly comparative across countries and over time, and it shows how country rankings can change once welfare rather than GDP is the object. It is therefore a benchmark for comparative welfare applications even if the substantive components you may want ultimately differ. 

# Research questions this paper inspires

1. Can a consumption-equivalent welfare statistic analogous to Jones–Klenow be constructed in a labour-market setting where well-being depends explicitly on realized bundle (z), preferences (R), feasible set (A), and pay schedule (y)?

2. How would Jones–Klenow-style welfare rankings change if leisure were decomposed into chosen leisure versus constrained nonemployment due to lack of job opportunities?

3. Can one extend the decomposition of welfare into consumption, leisure, mortality, and inequality by adding an opportunity-set component that captures unequal access to jobs?

4. Under what conditions does a welfare statistic based on realized outcomes substantially mis-rank countries or individuals relative to a measure that also values feasible opportunities?

5. Could a structural labour-supply or latent-job model generate a Jones–Klenow-style aggregate welfare index while keeping preferences and opportunities analytically distinct?

# Challenge to this paper

The strongest challenge is that the paper evaluates realized outcome distributions, not people’s feasible opportunities. This makes it powerful as a welfare-accounting exercise but limited as a fairness analysis. If two countries have the same distribution of realized consumption and leisure but radically different opportunity sets, social insurance environments, or constraints on choice, the Jones–Klenow measure would treat them as equivalent except insofar as those differences show up in realized outcomes. For an opportunity-sensitive welfare project, that is a substantive limitation. [reasonable inference for my project] supported by 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper defines welfare as a consumption-equivalent expected-utility object built from realized consumption, leisure, mortality, and inequality. It is explicitly about how to measure welfare across countries and over time, rather than about how labour-market outcomes are generated. 

[reasonable inference for my project] In your notation, it is closest to a framework in which the realized bundle (z) is central and a common welfare evaluator is imposed across persons or countries. It has no explicit role for (A) as a feasible job set, and it does not model (R) as heterogeneous across agents in the welfare evaluation; instead, a common preference structure is imposed. The pay-schedule component (y) is absent except indirectly through realized income and consumption. 

[explicit in paper] The paper is not about fairness axioms, responsibility, or compensation. It does not discuss whether lower leisure should be interpreted as a choice or a constraint, and it does not distinguish between actual and reference opportunities. 

[reasonable inference for my project] In your taxonomy, the paper is closest to none of the substantive axioms directly. It is not about independence of (A), independence of (y), laissez-faire evaluation, or reference opportunity sets. Its main relevance is methodological: it shows how a welfare object can be defined and decomposed once one decides what the relevant arguments are. 

[unclear from paper] Whether the Jones–Klenow welfare ranking could be reinterpreted as a special case of a broader (W(z,R,A;y)) measure is not addressed. 

# Relation to Bargain et al. (2013)

[not central].

# Relation to opportunities vs preferences

The paper is weak on opportunities and only indirectly about preferences. Preferences appear as a common imposed utility specification, not as heterogeneous objects to be respected or neutralized. Opportunities do not appear as separate objects at all. 

Its relevance for your opportunities-versus-preferences agenda is therefore mostly negative but still useful. It shows how much welfare analysis can be done from realized outcomes alone, and thereby clarifies what remains missing if one wants a welfare concept that is sensitive to feasible opportunities or to ethically differentiated treatment of preference heterogeneity. 

# Useful quotations / formulas

The foundational utility object is
[
U = E \sum_{a=1}^{100}\beta^a u(C_a,\ell_a)S(a),
]
and the country welfare statistic is the consumption-equivalent factor (\lambda_i) satisfying
[
U_{us}(\lambda_i)=U_i(1).
]
These are the core equations of the paper. 

The key simplified decomposition is equation (7), which writes log welfare relative to income as the sum of life expectancy, consumption, leisure, and inequality terms. The richer micro decomposition is equation (19), which further distinguishes consumption share, leisure, consumption inequality, and leisure inequality. 

Table 2 is especially important because it shows, for the 13-country micro sample, how France moves from 67.2 percent of US income to 91.8 percent of US welfare, while countries such as South Africa, India, Indonesia, and Malawi move sharply downward relative to income. Table 3 is the key growth table, and Table 5 is the crucial validation of the macro approximation against the micro exercise. 

# Suggested tags

beyond-gdp, consumption-equivalent-welfare, cross-country-welfare, mortality, leisure, inequality, welfare-decomposition, welfare-growth, macro-vs-micro, expected-utility

# My quick takeaway

This is a foundational welfare-measurement paper for your corpus. It is not a paper on opportunity sets, labour-supply structure, or fairness axioms. Its main value is to show, cleanly and persuasively, that a welfare object can differ systematically from GDP once mortality, leisure, and inequality are incorporated in a common expected-utility metric. For your JMP, it is best treated as a benchmark on how to construct and decompose an aggregate welfare measure from realized outcomes—while also serving as a reminder that outcome-based welfare is not yet opportunity-sensitive welfare.
