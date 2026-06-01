---

title: "The Quantity and Quality of Life and the Evolution of World Inequality"
authors: ["Gary S. Becker", "Tomas J. Philipson", "Rodrigo R. Soares"]
year: 2005
outlet: "American Economic Review"
country_or_context: "Cross-country / global"
population: "96 countries covering more than 82% of the world population in the main analysis; 49 countries in the age-cause mortality decomposition"
data_period: "1960-2000 main analysis; 1965-1995 for age-cause decomposition"
shelf: "welfare_measurement_health_inequality"
tags: ["full income", "welfare measurement", "longevity", "world inequality", "cross-country comparison", "health valuation", "life expectancy", "decomposition"]
priority: "medium-high"
read_status: "extracted"
------------------------

# Full citation

Becker, Gary S., Tomas J. Philipson, and Rodrigo R. Soares. 2005. “The Quantity and Quality of Life and the Evolution of World Inequality.” *American Economic Review* 95(1): 277-291. 

# One-sentence contribution

The paper constructs a “full income” measure that adds the monetary value of longevity gains to income growth and shows that, once health improvements are incorporated, cross-country welfare inequality fell substantially between 1960 and 2000 even though income inequality alone did not show the same pattern. 

# Why this paper matters

This paper matters because it is a clear and influential example of welfare measurement that does **not** rely on income alone. For your broader project, its value lies in showing how a non-income dimension can be monetized and inserted into a welfare comparison framework in a disciplined way. It is therefore useful for thinking about the architecture of a well-being measure, even though it is not a labour-supply paper and does not model job opportunity sets. 

It is also relevant because it explicitly distinguishes between ordinary GDP growth and “full income” growth, and it performs a decomposition exercise on the health side. However, the decomposition is into age groups and causes of death, not into preferences, opportunities, or responsibility-sensitive components. So its relevance to your JMP is real but indirect. 

# Core research question

How does the evolution of cross-country inequality change once welfare is measured by combining income per capita with the monetary value of gains in longevity rather than by income alone? Relatedly, which age groups and causes of death account for the observed reduction in life expectancy inequality? 

# Economic setting and context

The paper studies welfare inequality across countries in the postwar period. The main empirical comparison uses 96 countries, covering more than 82 percent of the world population, and tracks income per capita and life expectancy from 1960 to 2000. A second exercise uses WHO mortality data for 49 countries to decompose life expectancy changes by age group and broad cause-of-death category between 1965 and 1995. Table 1 reports the contrasting evolution of income and life expectancy inequality; Tables 2 and 3 report the valuation of longevity gains and the implied changes in “full income” inequality. 

The paper is cross-country and macro-comparative in orientation. It is not about labour supply, taxes, or household decision-making. Its empirical object is the welfare of a hypothetical representative life-cycle individual for each country-year, built from country-level income and survival schedules. 

# Model / theoretical framework

The model class is a calibrated lifetime welfare-accounting framework. The key theoretical object is an indirect utility function (V(Y,S)), where (Y) is lifetime income and (S) is the survival function. The individual chooses a consumption path to maximize discounted expected utility
[
V(Y,S)=\max \int_0^\infty e^{-\rho t}S(t)u(c(t))dt
]
subject to a lifetime budget constraint
[
Y=\int_0^\infty e^{-rt}S(t)y(t)dt=\int_0^\infty e^{-rt}S(t)c(t)dt.
]
The budget setup assumes full annuity insurance or, equivalently, complete contingent claims markets. 

The paper then defines the monetary value of an infra-marginal change in longevity as the income increment (W(S,S')) that makes the individual indifferent between the old survival schedule with compensation and the new survival schedule without compensation:
[
V(Y' + W(S,S'), S)=V(Y',S').
]
At the annual level, this becomes (w(S,S')), and “full-income” growth is the income growth rate augmented by this health valuation. 

The framework is positive with welfare-accounting content. It is not a structural behavioural model of labour supply or job choice, and it is not an explicit normative theory of fairness or compensation. The feasible set is not a job set and opportunities are not modeled as choice sets. Instead, the framework evaluates welfare consequences of country-level changes in income and survival. 

# Key objects

The central objects are the indirect utility function (V(Y,S)), the instantaneous utility function (u(c)), the annuity value of survival (A(S)=\int_0^\infty e^{-rt}S(t)dt), the yearly value of longevity gains (w(S,S')), the lifetime value (W(S,S')), and the “full income” growth rate (g). The paper also defines the hypothetical life-cycle individual (HLCI), who receives the country’s per capita income in every year of life and faces the country’s cross-sectional survival function throughout life. 

For the decomposition exercise, the key additional objects are counterfactual survival functions that isolate changes in mortality by age group and cause of death, the implied counterfactual life expectancy levels, and the decomposition of the regression-to-the-mean coefficient in life expectancy into age-cause-specific contributions. Equations (7) and (8) are central here. 

# Data

The main income data come from Penn World Tables 6.1, using GDP per capita adjusted for terms of trade. The main health data come from the World Bank’s *World Development Indicators*, using life expectancy at birth. The main sample contains 96 countries and covers 1960, 1990, and 2000 for the inequality comparisons. Table 1 reports dispersion statistics for income per capita and life expectancy; Table 2 reports the monetary value of longevity gains by region and for poorer versus richer countries; Table 3 reports inequality measures for “full income.” 

For the cause-of-death decomposition, the paper uses the World Health Organization Mortality Database. Because data availability is more limited, this exercise is restricted to 49 countries and relies on ten-year averages centered around 1965 and 1995. The authors classify causes of death into 13 broad groups and use three age groups: 0-19, 20-49, and 50+. Tables 4 and 5 report the resulting decompositions. 

# Identification logic

This is not an identification paper in the econometric causal sense. The paper is a calibration-and-accounting exercise. The variation used comes from observed cross-country changes in income per capita, life expectancy, and mortality by cause and age, combined with a calibrated lifetime utility model that assigns monetary values to survival gains. 

The crucial assumptions are strong and explicit: full annuity insurance or complete contingent claims markets, the HLCI representation, a common instantaneous utility function, and parameter calibration using values from the “value of life” and intertemporal-substitution literatures. The paper calibrates (u(c)) using parameters such as (e=0.346), (\gamma=1.250), and (r=0.03), with the calibration anchored partly in U.S. data. Thus, the empirical conclusions depend materially on the maintained functional form and parameterization. 

Identification is therefore mainly parametric and conceptual rather than econometrically quasi-experimental. The decomposition by cause and age is an accounting decomposition of mortality changes, not a causal decomposition of treatment effects. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The empirical strategy has two layers. First, the paper calibrates a lifetime utility framework that can convert survival improvements into yearly income equivalents. Under the HLCI assumptions, optimal consumption equals constant annual income, which yields the simpler representation (V(y,S)=u(y)A(S)). The yearly value of longevity gains (w(S,S')) and full-income growth (g) then follow from closed-form expressions based on the chosen utility specification. 

Second, the paper computes inequality statistics and convergence regressions using GDP per capita, life expectancy, and the constructed “full income” series. It then performs a separate decomposition of life expectancy changes by age and cause of death using WHO mortality data and counterfactual survival functions. The main comparative statistics are population-weighted and abstract from within-country inequality. 

# Treatment of preferences

Preferences are treated in a highly aggregated and homogeneous way. The paper does not estimate heterogeneous preferences across individuals or countries. Instead, it posits a common lifetime utility structure and calibrates the instantaneous utility function (u(c)) using parameters drawn from the value-of-life and consumption literatures. 

The authors do emphasize that their method differs from measures such as the UNDP’s because the relative value assigned to nonmaterial aspects is meant to be disciplined by preferences revealed by market behavior rather than by arbitrary institutional weights. But operationally, the model still uses a common calibrated utility specification rather than heterogeneous estimated preference structures. 

So, for your purposes, the paper is useful as an example of a welfare measure built from a common evaluative metric, not as a paper on preference heterogeneity. It does not help distinguish welfare inequality due to different (R) across agents. 

# Treatment of opportunities / constraints

This section is crucial for your project, and here the paper is clearly limited. It does **not** model opportunities explicitly in the sense of feasible job sets, latent opportunity distributions, hours restrictions, or demand-side labour-market constraints. There is no analogue of a job opportunity set (A), no labour-supply choice problem, and no observed or latent set of available alternatives. 

The only “constraint” in the formal model is the lifetime budget constraint under complete annuity insurance, together with the survival schedule. That is not an opportunity-set treatment in your sense. It is a lifetime resource-and-survival environment, not a set of feasible jobs or bundles generated by market opportunities. 

Accordingly, the paper does **not** help distinguish preference heterogeneity from opportunity heterogeneity. It distinguishes neither. It instead compares welfare across country-level hypothetical life-cycle individuals using common preferences and observed country-level income and mortality profiles. 

# Welfare / normative object

The welfare object is “full income”: income per year plus the annual monetary equivalent of longevity gains. Formally, the key normative-comparative object is the income compensation that equates utility across survival schedules. This object is then used to compare welfare growth and welfare inequality across countries. 

The paper is best described as positive with welfare-accounting applications. It is not purely positive, because it clearly evaluates welfare and inequality using a specific utility-based metric. But it is not explicitly normative in the social-choice or fairness-axiom sense either. It does not discuss responsibility for opportunities, compensation for exogenous disadvantage, or reference opportunity sets. 

On decomposition, the paper is relevant but only in a specific way. It decomposes changes in life expectancy inequality by cause of death and age group. It does **not** decompose welfare inequality into preferences, opportunities, effort, responsibility, or compensation-sensitive components. 

# Main findings

The central empirical result is that, while cross-country income inequality shows little decline up to the 1990s, cross-country life expectancy inequality falls substantially over the period. Once longevity gains are monetized and included in “full income,” countries become significantly more equal between 1960 and 2000. Table 1 shows the divergent patterns in income and life expectancy inequality, and Table 3 shows that inequality in full income is lower than inequality in income alone. 

The paper estimates an average yearly growth in full income of 2.8 percent for the world as a whole, of which about one quarter comes from health. For the poorest 50 percent of countries in 1960, the average yearly growth in full income is 4.1 percent, with 1.7 percentage points due to health; for the richest 50 percent, it is 2.6 percent, with only 0.4 percentage points due to health. These magnitudes are reported in the abstract and Table 2. 

The decomposition results indicate that reductions in mortality from infectious diseases, respiratory and digestive diseases, congenital and perinatal conditions, and ill-defined conditions account for most of the reduction in life expectancy inequality, especially through mortality declines before age 20 and, to a lesser extent, between ages 20 and 50. By contrast, mortality declines after age 50 from nervous-system and circulatory diseases contributed to increased inequality because they were concentrated more in richer countries. Tables 4 and 5 are the key evidence here. 

The paper also emphasizes that the convergence in health inequality is concentrated before 1990; after that, AIDS in Africa increases life expectancy inequality somewhat. This is already visible in the descriptive discussion around Table 1 and reappears in the conclusions. 

# Main limitations

The main limitation is the representative-HLCI construction. The welfare comparison is based on a hypothetical life-cycle individual who receives the country’s average income in each year and faces the country’s average survival curve. This abstracts from within-country heterogeneity, within-country inequality, and the joint distribution of income and mortality. For your purposes, that means it is very far from an individual-level (W(z,R,A;y)) framework. 

A second limitation is the strong calibration structure. The valuation of longevity gains depends on a common utility function and on parameters partly calibrated using U.S. evidence. This is analytically transparent, but it is not identified from the cross-country data in a structural microeconometric sense. 

A third limitation is the treatment of opportunities. The paper has no explicit feasible set, no distinction between realized bundle and opportunity set, and no account of labour-market or institutional opportunity heterogeneity. Therefore it cannot be integrated directly into a responsibility-versus-compensation analysis of opportunities. 

A fourth limitation is decomposition scope. The paper does provide a useful decomposition of health improvements by age and cause, but not a decomposition of welfare inequality into opportunities, preferences, circumstances, effort, or policy design. Thus its decomposition relevance to your project is narrow. 

A fifth limitation is data coverage in the cause-specific mortality exercise. The WHO-based decomposition uses only 49 countries and includes just one sub-Saharan African country, so the age-cause decomposition is not well suited to capturing the later AIDS-driven African experience. The authors state this explicitly. 

# Relevance for my JMP

## possible use for framing

This paper is useful for framing the general idea that welfare measurement should not collapse entirely to observed income. It gives a clean example of how an additional non-income dimension can be monetized and incorporated into a single welfare index. That is helpful when motivating why a well-being measure (W) may need to depend on more than realized money income alone. 

## possible use for model design

Its relevance for model design is limited but not zero. The useful lesson is architectural: define a welfare metric carefully, specify its evaluative inputs, and make explicit the assumptions needed to convert non-income dimensions into comparable welfare units. But it does not provide a model of job choice, feasible job sets, labour supply, or latent opportunities. 

## possible use for identification

The paper is mainly useful as a cautionary example of calibration-based welfare measurement rather than as a source of causal identification. It can help you think about what assumptions are required when one maps empirical observables into a welfare metric, but it does not help identify preferences versus opportunities in your sense. [reasonable inference for my project] supported by 

## possible use for welfare measurement

This is the strongest relevance margin. The paper offers a fully explicit welfare object, clarifies the distinction between ordinary income growth and welfare growth, and shows how to price a non-income dimension using a utility-theoretic framework. Even though the application is health rather than labour-market opportunities, the logic is relevant to the construction of well-being measures. 

## possible use for decomposition

Useful only in a restricted sense. The paper shows how to decompose an aggregate welfare-related change into interpretable components, here age groups and causes of death. That may inspire decomposition design. But it does not provide the decomposition you need between preferences, opportunities, and pay schedules. 

## possible use for comparative application

This is an explicitly comparative cross-country application, so it is relevant if part of your long-run agenda includes comparing welfare across countries or regions under a common evaluative metric. Its comparative strength is exactly there. But the comparative object is country-level welfare accounting, not individual-level opportunity-sensitive well-being. 

# Research questions this paper inspires

Can a job-opportunity-sensitive well-being measure be constructed analogously to “full income,” where the value of expanded feasible job sets is expressed in a common welfare-equivalent monetary metric?

What assumptions are needed to compare well-being across individuals or countries when the relevant non-income dimension is opportunity rather than longevity?

How would a decomposition of welfare inequality into realized bundle effects and feasible-set effects differ conceptually from Becker et al.’s decomposition of life expectancy gains by cause and age?

Can one define a reference-based welfare metric for job opportunities in the same spirit that this paper defines a common valuation of survival gains?

How sensitive are welfare-convergence conclusions to the choice of common evaluative utility function when the additional dimension is opportunity rather than health?

# Challenge to this paper

The core challenge is that the welfare metric is highly stylized and homogeneous. The paper prices longevity gains using a common calibrated utility function applied to hypothetical life-cycle individuals, thereby abstracting from heterogeneous preferences, within-country inequality, and the possibility that survival and income are jointly distributed in systematically unequal ways. This makes the exercise elegant and tractable, but it also makes the welfare object less compelling for projects that need individual-level heterogeneity and explicit opportunity structures. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper studies a welfare measure that depends on realized income and survival schedules, and it evaluates welfare changes by converting longevity gains into income-equivalent units. It therefore belongs to the broad family of welfare-measurement papers rather than to labour-supply or opportunity-set papers. 

[reasonable inference for my project] The closest conceptual link to your framework is methodological: the paper shows that one can define a welfare object (W) that depends on more than current income and can be used for comparative inequality analysis. In that abstract sense, it supports the idea that a well-being measure may legitimately depend on additional arguments beyond realized consumption. supported by 

[unclear from paper] There is no explicit mapping into (W(z,R,A;y)). The paper does not define (z) as a realized bundle in your sense, does not model (R) heterogeneously, has no feasible job set (A), and does not analyze a pay schedule (y) as a job-dependent object. Any such mapping would be external to the paper. 

[reasonable inference for my project] If forced into a loose analogy, the paper is closest to the general question of how to construct a common well-being metric. It is not close to independence of (A), responsibility for opportunities, reference opportunity sets, or laissez-faire evaluation of realized choices. It is somewhat closer to decomposition of inequality, but only because it decomposes health-related welfare changes by cause and age, not because it separates opportunities from preferences. supported by 

# Relation to Bargain et al. (2013)

[not central].

# Relation to opportunities vs preferences

This paper is largely orthogonal to the opportunities-versus-preferences distinction that matters for your JMP. Preferences are effectively treated as common and calibrated, while opportunities are not modeled as feasible sets at all. The welfare differences arise from differences in country-level income paths and survival schedules, not from different job opportunities or different estimated tastes over work-leisure bundles. 

Its usefulness here is therefore mostly negative but clarifying: it is a good example of a welfare paper that is informative about measurement yet not informative about the opportunity/preference distinction you care about. That distinction would have to be added externally. [reasonable inference for my project] supported by 

# Useful quotations / formulas

The central valuation equation is
[
V(Y' + W(S,S'), S)=V(Y',S'),
]
which defines the income compensation for moving from one survival schedule to another. This is the core welfare-pricing object of the paper. 

Under the hypothetical life-cycle individual setup, the indirect utility simplifies to
[
V(y,S)=u(y)A(S),
]
where
[
A(S)=\int_0^\infty e^{-rt}S(t),dt.
]
This simplification is what makes the empirical cross-country exercise operational. 

The paper’s summary empirical message is captured well by Table 2: for the poorest 50 percent of countries in 1960, yearly full-income growth is estimated at 4.1 percent, versus 2.6 percent for the richest 50 percent, with health accounting for a much larger share of gains among poorer countries. 

# Suggested tags

full-income, longevity, welfare-measurement, world-inequality, health-valuation, convergence, cross-country-comparison, cause-of-death-decomposition

# My quick takeaway

This is not a paper on labour supply, latent jobs, feasible job sets, or responsibility-sensitive opportunity evaluation. But it is still useful for your corpus because it is a disciplined example of welfare-measure construction beyond income alone. Its strongest contribution for your purposes is conceptual: it shows how a non-income dimension can be assigned an explicit welfare-equivalent monetary value and then used in inequality comparisons. Its weakest point for your JMP is equally clear: it has no real treatment of (A), no heterogeneous (R), and no decomposition into opportunities versus preferences.
