---

title: "International Comparisons of Living Standards by Equivalent Incomes"
authors: ["Marc Fleurbaey", "Guillaume Gaulier"]
year: 2009
outlet: "Scandinavian Journal of Economics"
country_or_context: "24 OECD countries"
population: "National populations of 24 OECD countries represented through country-level aggregates and a representative-agent/social-welfare construction"
data_period: "2004"
shelf: "international_equivalent_income_comparisons"
tags: ["equivalent income", "international comparisons", "living standards", "OECD", "GDP correction", "social welfare", "inequality", "leisure", "health", "household demography"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Fleurbaey, Marc, and Guillaume Gaulier. 2009. “International Comparisons of Living Standards by Equivalent Incomes.” *Scandinavian Journal of Economics* 111(3): 597–624. 

# One-sentence contribution

The paper proposes an international living-standards measure based on equivalent income that corrects GDP per capita for non-income dimensions and inequality, and shows for 24 OECD countries that the resulting ranking differs substantially from the GDP ranking. 

# Why this paper matters

This paper matters because it gives a concrete, welfare-theoretic alternative to GDP per capita for international comparisons. Instead of building an ad hoc composite index, it uses equivalent income, that is, the income that would make a population indifferent between its actual situation and a reference situation in non-income dimensions. This is directly relevant to any project that wants a scalar welfare metric with an explicit theoretical basis. 

For your project, the paper is especially important as a bridge between social-choice theory and applied welfare measurement. It does not model jobs or feasible sets, but it is one of the cleanest applications of equivalent-income reasoning to multidimensional welfare comparisons at an aggregate level. 

# Core research question

How can one compare living standards across countries in a way that starts from GDP per capita but corrects for non-income dimensions such as leisure, health, unemployment risk, household demography, and inequality using a theoretically grounded money-metric welfare concept? 

# Economic setting and context

The paper is an OECD-country comparison for 2004. Its motivation is dissatisfaction with GDP per capita as a welfare measure and skepticism toward alternative composite indicators such as the HDI when their aggregation weights lack a clear rational basis. The authors explicitly position equivalent income as an alternative that remains monetary and comparable while incorporating non-income dimensions. 

The exercise is macro-comparative rather than micro-econometric. Countries are compared using national-account and related aggregate data, not individual microdata. The paper is therefore about cross-country welfare comparison, not about household or worker-level estimation. 

# Model / theoretical framework

The framework is normative and measurement-oriented. Individuals are described by income (y_i) and a vector of non-income living conditions (z_i), with indirect utility (v^i(y_i,z_i)). Fixing a benchmark (z^*), the equivalent income (y_i^*) solves (v^i(y_i,z_i)=v^i(y_i^*,z^*)). This converts all differences in non-income dimensions into income equivalents and thereby makes cross-country comparison possible in a single monetary dimension. Section II introduces this object formally, and Figure 1 on page 4 illustrates it graphically. 

At the social level, welfare is obtained by applying an inequality-averse social welfare function to the vector of equivalent incomes. The paper uses a CES social welfare function over equivalent incomes, with a Kolm-Atkinson-type deduction for inequality. In practice, because of data limitations, the paper approximates this by computing average equivalent income with a representative-agent approach and then subtracting an inequality correction based on the ordinary income distribution. Equations (6)–(8) in Section II and the discussion on pages 8–10 are central. 

The framework is not positive in the labor-supply or discrete-choice sense. The agent does not choose among jobs or bundles in an observed behavioral model. Instead, the paper postulates expected utility over consumption and labor for a representative agent and uses willingness-to-pay logic to compute corrections for specific non-income dimensions. It is therefore explicitly normative, with pragmatic approximations for empirical implementation. 

# Key objects

The central object is equivalent income. For an individual or representative agent, it is the income that, under a reference vector of non-income conditions, yields the same welfare as the actual income-plus-conditions bundle. This is the paper’s main money-metric welfare object. 

A second key object is the inequality-averse social welfare function
[
W(y_1^*,\ldots,y_n^*)=
\left(\frac{1}{n}\sum_{i=1}^n (y_i^*)^{1-\nu}\right)^{1/(1-\nu)},
]
where (\nu) is the coefficient of inequality aversion. The authors then decompose social welfare into mean equivalent income times an inequality adjustment. This is equation (6) and the decomposition in equation (7). 

A third key object is the sequence of empirical corrections added to GDP per capita. The final indicator incorporates corrections for GNI rather than GDP, leisure, unemployment risk, healthy life expectancy, household size, and inequality. Figure 3 on page 19 and Tables 2–4 summarize these corrections and their contribution to country rankings. 

# Data

The empirical exercise uses 24 OECD countries for 2004. The underlying data are drawn from macro and administrative sources, especially World Bank, OECD, LIS, and related datasets. The Appendix lists GDP/GNI, hours of work, unemployment rates and durations, replacement rates, tax data, health-adjusted life expectancy, household size, and income-distribution information. 

The paper is transparent that it uses easily accessible aggregate data and a representative-agent approximation rather than individual-level survey data. It explicitly presents the work as a prototype and hopes future progress will come from richer cross-country surveys on consumption and preferences. The conclusion and Appendix are clear on this limitation. 

# Identification logic

There is no quasi-experimental identification. The paper is not trying to estimate causal effects. Its identification logic is welfare-theoretic and calibration-based. It starts from a utility representation, defines equivalent income by indifference to a benchmark (z^*), and then approximates willingness-to-pay corrections using observed country aggregates and parameter choices. 

Empirically, the main approximations are substantial. The average equivalent income is computed by applying representative-agent preferences to average conditions, and the social-welfare aggregate is then approximated further by combining mean equivalent income with an income-inequality correction based on the ordinary income distribution. The paper is explicit that these steps are driven by data constraints. Pages 8–10 and the conclusion state this clearly. 

Identification is therefore weak in the econometric sense but explicit in the measurement sense: results are driven by the chosen welfare function, the chosen benchmark (z^*), and the calibrated preference parameters. The paper’s contribution is not empirical identification of preferences from behavior, but coherent measurement conditional on a specified normative structure. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The empirical strategy is a sequence of calibrated corrections to GDP per capita. First, GDP is replaced by GNI to correct for international income flows. Then the authors compute equivalent-income-style corrections for leisure, unemployment risk, health, and household composition, and finally apply an inequality correction through the social welfare function. Figure 3 on page 19 visually shows the country positions after each cumulative correction. Tables 2–4 provide the final levels, rankings, and dollar-valued corrections. 

Leisure is corrected using a willingness-to-pay logic around a reference labor norm, with marginal valuation approximated by net wage rates. Unemployment risk is valued through an expected-utility premium reflecting transition risk, replacement rates, and a stigma adjustment. Health is captured through healthy life expectancy and converted into an income equivalent via the lifetime utility function. Household composition is corrected through a household-production/public-good model that yields an equivalence-scale adjustment. Section III explains these constructions in detail. 

The paper also performs sensitivity analysis. Table A1 varies parameters in ways favorable to Anglo-Saxon, Latin, and Nordic country patterns. This is important because it shows that while rankings are parameter-sensitive, some broad patterns are fairly robust. 

# Treatment of preferences

Preferences enter centrally, but only in a representative-agent, calibrated form. The utility function is separable in consumption and labor, and non-income corrections are valued by willingness-to-pay. The paper’s claim is that this is superior to composite indicators with arbitrary weights because the weights now come from a welfare-theoretic structure rather than from arbitrary index design. 

However, preferences are not estimated from individual microdata in this paper. They are imposed or calibrated, often borrowing parameter values from the literature. This means the treatment of preferences is theoretically explicit but empirically coarse. The paper itself acknowledges that better international surveys on consumption and preferences are needed for more accurate application. 

The paper is therefore much closer to normative money-metric welfare theory than to empirical heterogeneous-preferences estimation of the Bargain et al. type. [reasonable inference for my project] supported by 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly as feasible job sets, latent offers, or menus of attainable bundles. There is no object analogous to your (A_i). Countries differ in realized average conditions such as leisure, unemployment risk, health, and household demography, and these are valued directly through equivalent-income corrections. 

Unemployment appears as a risk and not as an explicit opportunity-set structure. Leisure appears as realized average labor time, not as a constrained or chosen bundle from a labor-market opportunity set. Household demography and health are also treated as dimensions of life, not as feasible-set primitives. So the paper is weak on the opportunities side in your sense, even though it is strong on multidimensional welfare measurement. 

It therefore helps much more with converting non-income realized conditions into money-metric welfare than with separating preferences from opportunities or modeling job access. [reasonable inference for my project] supported by 

# Welfare / normative object

The paper is explicitly normative. Its welfare object is equivalent income at the individual or representative-agent level and inequality-averse social welfare at the population level. The entire exercise is designed to compare living standards, not productivity or GDP performance. 

This is directly relevant to your project’s interest in money-metric welfare measures and reference-based evaluation. The benchmark (z^*) plays a crucial normative role, because the equivalent-income measure depends on the reference values of non-income dimensions. The authors defend this by appealing to social-choice theory and the fair-allocation literature rather than treating the benchmark as merely arbitrary. Section II, especially pages 4–7, is central here. 

The paper is not about responsibility versus compensation for opportunities, and it is not an axiomatic jobs-and-wellbeing paper. It is a population-level welfare-comparison paper using a theoretically grounded monetary metric. 

# Main findings

The main finding is that country rankings change materially once GDP is corrected for non-income dimensions and inequality. Table 1 on page 3 and Table 2 on page 20 show that the final indicator differs substantially from both GDP per capita and the HDI. For example, France and Japan perform much better under the equivalent-income approach than under GDP per capita, while Australia, Sweden, and especially the United States do worse relative to GDP-based impressions. 

A second major finding is that the size of the corrections is economically meaningful. The correction for GNI is small for many countries but large for Ireland and Luxembourg; leisure strongly benefits countries such as France, Norway, and the Netherlands; health favors Japan, France, Sweden, and Switzerland; and the household-size correction is quantitatively very large. Table 4 on pages 21–22 is the key source here. 

A third major finding is that inequality matters a great deal. Even with what the authors call a conservative inequality-aversion coefficient, the inequality correction is strong and is especially unfavorable to countries such as Ireland, the UK, the US, Australia, Portugal, and Italy, while more egalitarian countries such as Japan and Nordic countries improve. This is one of the most important substantive results of the paper. 

A fourth finding is that three broad welfare patterns emerge. The paper identifies an Anglo-Saxon pattern with high inequality, relatively high work time, and low unemployment cost; a Latin pattern with more leisure, higher unemployment cost, and favorable health; and a Nordic pattern with equality, low unemployment risk, and relatively low work time. Pages 22–23 discuss these clusters explicitly. 

# Main limitations

A first limitation is the representative-agent approximation. The paper cannot compute individual equivalent incomes from microdata and therefore approximates mean welfare and inequality using aggregates plus an ordinary income-distribution correction. This is a serious limitation for any analysis concerned with cumulative deprivation at the micro level. 

A second limitation is that preference parameters are calibrated rather than estimated from comparable international micro evidence. The paper explicitly says that better data on consumption and preferences are needed. 

A third limitation, relative to your project, is that opportunities are absent as explicit objects. Unemployment risk, leisure, and household composition are all treated as realized conditions or risk environments, not as feasible-set structures. So the framework cannot distinguish whether observed disadvantages stem from preferences, opportunities, or both. [reasonable inference for my project] supported by 

A fourth limitation is the sensitivity to benchmarks and parameter values. The authors address this by sensitivity analysis, but the paper remains conditional on normative and calibration choices. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a money-metric welfare approach that goes beyond GDP while retaining a scalar measure. It is especially useful if you want to justify why a single welfare index need not be ad hoc.

## possible use for model design

It is moderately useful for model design on the welfare side. It provides a template for defining equivalent income with reference non-income conditions and then aggregating it with inequality aversion.

## possible use for identification

Directly, it is not useful for empirical identification of preferences or opportunities. Indirectly, it is useful because it makes transparent where benchmark and parameter choices enter and therefore where stronger empirical work would be needed.

## possible use for welfare measurement

This is the strongest use. It is a core reference for international welfare comparison via equivalent income and inequality-sensitive aggregation.

## possible use for decomposition

It is moderately useful. It does not decompose welfare into (R), (A), and (y), but it does decompose the final living-standard measure into successive corrections for distinct non-income dimensions and inequality.

## possible use for comparative application

It is highly useful. This is one of the paper’s main strengths: a transparent, cross-country comparative implementation for OECD countries.

# Research questions this paper inspires

Can equivalent income for cross-country comparisons be rebuilt on a micro-founded (W(z,R,A;y)) framework in which opportunity sets (A) are explicit rather than absent?

How would the country rankings change if unemployment and leisure were evaluated through a structural labor-supply/job-opportunity model rather than representative-agent corrections?

Can one move from the paper’s aggregate corrections to individual-level equivalent incomes using cross-country microdata, thereby capturing cumulative deprivation directly?

What is the correct benchmark (z^*) when non-income conditions include labor-market opportunity sets rather than only realized average dimensions?

Can the fair-allocation defense of benchmark-based equivalent income be extended to a jobs-and-wellbeing setting with explicit feasible jobs and pay schedules?

# Challenge to this paper

The strongest challenge is that the paper is normatively elegant but empirically thin. It shows how equivalent income can discipline international welfare comparison, but it does so through representative-agent calibrations and realized-condition corrections rather than through direct identification of preferences and opportunities from microdata. For your project, this means it is a strong conceptual and comparative reference, but not a sufficient empirical foundation for a richer jobs-and-wellbeing model. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper measures living standards through equivalent incomes that reduce differences in non-income dimensions to income equivalents under a reference situation (z^*). It then aggregates these with an inequality-averse social welfare function. 

[reasonable inference for my project] In your notation, this paper is closest to a welfare measure built from realized conditions (z) and a normative money-metric transformation, with inequality-sensitive social aggregation on top. The pay schedule (y) is present only indirectly through national income and labor corrections. Preferences (R) matter through willingness-to-pay. The feasible set (A) is not modeled. 

[unclear from paper] The paper does not define an individual well-being measure (W(z,R,A;y)), does not distinguish actual versus reference opportunity sets, and does not analyze IIJ, IPIJ, independence of (A), or responsibility for opportunities. Those questions are outside its scope. 

[reasonable inference for my project] In your taxonomy, the paper is closest to reference-based money-metric evaluation and inequality-sensitive welfare comparison. It is not close to independence of (A), because (A) is largely absent. It is also not close to laissez-faire or explicit compensation-for-opportunities analysis. It is best treated as a benchmark for the money-metric welfare side of your project, not for the opportunity-set side. 

# Relation to Bargain et al. (2013)

This paper is related to Bargain et al. (2013) through the common commitment to preference-sensitive welfare measurement, but the level and method differ sharply. Bargain et al. estimates heterogeneous preferences from labor-supply microdata and studies individual welfare rankings in the consumption-leisure space. Fleurbaey and Gaulier instead work at the country level, use calibrated representative-agent corrections, and focus on international living standards rather than micro welfare rankings. So the present paper is more macro-comparative and more explicitly money-metric, while Bargain et al. is more micro-empirical and more behaviorally grounded. [reasonable inference for my project] supported by 

# Relation to opportunities vs preferences

This paper is much stronger on welfare measurement than on opportunities. It values realized conditions such as leisure, unemployment risk, health, and household demography through equivalent-income corrections, but it does not model the feasible opportunities generating those outcomes. 

So for your project it should be read as a benchmark in reference-based money-metric evaluation, not as a model that separates preferences from opportunities. It helps show how one can aggregate multiple dimensions into a scalar welfare index, but not how opportunity sets should enter that index. 

# Useful quotations / formulas

The defining equation for equivalent income is
[
v^i(y_i,z_i)=v^i(y_i^*,z^*).
]
This is the paper’s core welfare concept and appears in Section II. 

The social welfare function is
[
W(y_1^*,\ldots,y_n^*)=
\left(\frac{1}{n}\sum_{i=1}^n (y_i^*)^{1-\nu}\right)^{1/(1-\nu)},
]
equation (6). This is the central aggregation device. 

The decomposition
[
W(y_1^*,\ldots,y_n^*)=
\left(\frac{1}{n}\sum_{i=1}^n y_i^*\right)\left(1-I(y_1^*,\ldots,y_n^*)\right)
]
is also crucial because it makes clear how the mean and inequality corrections interact. This is equation (7). 

Figure 3 on page 19 and Tables 2–4 are the most useful empirical summaries: they show the cumulative corrections from GDP to the final indicator, the final country rankings, and the absolute dollar value of each correction. 

# Suggested tags

equivalent-income, international-comparisons, OECD, living-standards, GDP-beyond, inequality-aversion, representative-agent, leisure-correction, health-correction, Fleurbaey-Gaulier

# My quick takeaway

This is a core reference for the money-metric welfare side of your project. It shows that equivalent income can be used to build a theoretically disciplined alternative to GDP for international comparison, and that the resulting corrections are quantitatively important. Its main weakness for your JMP is that it does not model opportunity sets at all. Its main value is that it gives a clean, applied template for reference-based welfare comparison with inequality sensitivity.
