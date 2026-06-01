---

title: "Beyond GDP: Using Equivalent Incomes to Measure Well-Being in Europe"
authors: ["Koen Decancq", "Erik Schokkaert"]
year: 2016
outlet: "Social Indicators Research"
country_or_context: "Europe"
population: "Individuals in 18 European countries covered by the European Social Survey"
data_period: "2008 and 2010"
shelf: "equivalent_income_beyond_gdp_europe"
tags: ["equivalent income", "well-being measurement", "Europe", "beyond GDP", "inequality aversion", "subjective well-being", "preferences", "multidimensional welfare"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Decancq, Koen, and Erik Schokkaert. 2016. “Beyond GDP: Using Equivalent Incomes to Measure Well-Being in Europe.” *Social Indicators Research* 126: 21–55. Published online 14 February 2015. 

# One-sentence contribution

The paper proposes a multidimensional, preference-respecting measure of individual well-being based on equivalent incomes, implements it for European countries using ESS data for 2008 and 2010, and shows that incorporating non-income dimensions and inequality aversion can substantially alter country rankings and growth assessments relative to income alone. 

# Why this paper matters

This paper matters because it provides a concrete empirical implementation of a normative welfare metric that goes beyond GDP while still yielding a single aggregate indicator. It is not merely a dashboard paper. Its core claim is that a synthetic measure is both possible and desirable once one accepts a clear set of underlying principles about individual well-being, cumulative deprivation, respect for preferences, and inequality aversion. 

For your project, the paper is especially important on the welfare-measurement side. It gives a tractable way to construct an interpersonal well-being metric that respects heterogeneous preferences and is distribution-sensitive. It is much weaker on opportunities as feasible sets, but very strong on the (z)- and (R)-side of the problem. 

# Core research question

How can one measure social progress in Europe in a way that goes beyond GDP, respects heterogeneity in individual views about the good life, accounts for cumulative deprivation and inequality, and remains empirically implementable with available survey data? 

# Economic setting and context

The paper is located in the “beyond GDP” literature and is explicitly framed against approaches that either focus only on income growth or rely on dashboards without coherent aggregation. It also situates itself relative to the capability approach, the social-indicator literature, subjective well-being research, the HDI, and OECD and EU initiatives following the Stiglitz–Sen–Fitoussi report. This positioning is set out in the introduction on pages 21–24. 

Empirically, the context is Europe during and immediately after the onset of the financial crisis. The implementation uses European Social Survey waves for 2008 and 2010, allowing the authors to compare both levels and changes in well-being across countries during a turbulent period. Pages 24–25 and 38–39 explain this choice. 

# Model / theoretical framework

The framework is normative and measurement-oriented rather than behavioral in the labor-supply sense. The authors formulate five principles for a richer measure of well-being: focus on individual well-being rather than GDP, account for cumulative deprivation, respect individuals’ own ideas about the good life, avoid reducing well-being to subjective happiness alone, and incorporate inequality aversion in the social aggregation step. These principles are laid out in Section 2, especially pages 24–31. 

The central well-being concept is the equivalent income. Individual well-being is measured as the hypothetical income that, combined with the best possible values of all non-income dimensions, would leave the individual indifferent relative to her actual situation. This is defined graphically and formally in Section 3, pages 33–36. 

The framework is explicitly synthetic. The authors reject the idea that one should remain with a multidimensional dashboard only. They argue that cumulative deprivation requires first constructing an individual well-being index row-by-row and only then aggregating across individuals. Table 2 and the hypothetical example in Table 3 are central here. 

Opportunities or feasible sets are not modeled explicitly. The framework contains no job menus, no latent opportunities, no rationing structure, and no (A_i)-type feasible-set object. It is therefore a multidimensional welfare-measurement framework, not a positive model of constrained choice. 

# Key objects

The first key object is the individual well-being index (W_i(x_{i1},x_{i2},\ldots,x_{ik})), constructed over multiple life dimensions and then aggregated into social welfare. Table 2 on page 26 is the clearest compact representation of this structure. 

The second key object is the equivalent income (y_i^*), defined as the hypothetical income that, when combined with the best feasible values of all non-income dimensions, yields the same level of well-being as the person’s actual situation. The paper’s formal definition appears on pages 33–35, and the intuition is illustrated in Figures 2 and 3. 

The third key object is the social welfare function
[
SW = M(1-I_q),
]
where (M) is average individual well-being and (I_q) is an inequality index parameterized by an inequality-aversion parameter (q). This is equation (1) on page 30. The inequality index is drawn from the S-Gini family, shown in equation (2) on page 30. 

A fourth key object is the satisfaction equation used to recover preference trade-offs:
[
S_i=\alpha+\lambda + p'(z_i)\ln y_i + (b+c'z_i)'f(x_i)+d'z_i+\varepsilon_i.
]
This is equation (3) on page 36. It is the bridge between observed life-satisfaction responses and the estimation of dimension-specific marginal rates of substitution. 

# Data

The empirical implementation uses the European Social Survey for waves 4 and 5, corresponding to 2008 and 2010. The final sample includes about 52,000 observations pooled across 18 countries. Pages 38–39 discuss the data choice and its limitations. 

The life dimensions included are material living conditions, health, unemployment, social interactions, and personal safety. These are operationalized with ESS variables as summarized in Table 4 on page 38. The paper explicitly notes that not all dimensions in the European Statistical System list can be included, and that happiness is not used as a life dimension because of its high correlation with life satisfaction and the ambiguity this creates. 

Income is based on reported household-income deciles in the ESS and then converted, adjusted, and uprated so that the country averages correspond to OECD “real net national income” measures. The details are given in Appendix 1, pages 52–53. This means the income data are usable but relatively coarse, and the authors acknowledge this directly. 

# Identification logic

Identification is not causal in the quasi-experimental sense. The key empirical identification problem is how to recover the weights individuals attach to different dimensions of life. The authors do this through life-satisfaction regressions, interpreting the estimated trade-offs across dimensions as information about the respondents’ views on the good life. Pages 35–37 discuss this logic. 

The paper is explicit that subjective satisfaction is not itself the well-being metric. Instead, it is used as a source of information on indifference-curve shape. This is a central conceptual distinction. The same data source that would be normatively problematic if interpreted directly as welfare is here used instrumentally to estimate preferences. Pages 28–30 and 35–36 are especially clear on this point. 

Identification of preference heterogeneity is limited. The method can only capture broad group-specific differences, not fully individual-specific preference parameters, because the regressions interact life dimensions only with a small set of socio-demographic characteristics. The authors explicitly acknowledge this limitation on pages 36–37 and again in the conclusion on pages 50–51. 

Identification is weak with respect to opportunities. The framework does not identify feasible sets or opportunity heterogeneity separately from outcomes and preferences. [explicit in paper / reasonable inference for my project] 

# Estimation / empirical strategy

The empirical strategy has three stages. First, the authors specify the normative principles and derive equivalent income as the appropriate well-being concept. Second, they estimate an ordered-logit life-satisfaction equation pooling the ESS 2008 and 2010 data across countries. Third, they compute equivalent incomes using the estimated dimension weights and then aggregate them into social welfare with different degrees of inequality aversion. Pages 35–38 and Tables 6–12 contain the operational core. 

The Box–Cox transformations for each non-income dimension are estimated jointly to maximize fit. Equivalent incomes are then computed using equation (5) on page 36:
[
y_i^* = y_i \exp\left(\frac{b+c'z_i}{\lambda + p'z_i}\right)'(f(x_i)-f(\bar x)).
]
The reference values (\bar x) are chosen as the best attainable levels for each dimension: very good health, no unemployment, daily social meetings, and no feeling of unsafety. Pages 36–38 explain this operationalization. 

The paper then computes average equivalent incomes, inequality in equivalent incomes, and the social welfare aggregates for different values of the inequality-aversion parameter (q). Tables 7–12 report the country rankings and growth comparisons. 

# Treatment of preferences

Preferences are central. The whole approach is built on the normative claim that the weighting scheme used to construct individual well-being should respect individuals’ own ideas about what a good life is. This is Principle 3 on pages 27–29. The paper therefore rejects both a purely objective weighting scheme and the direct use of subjective satisfaction as a welfare metric. 

At the same time, the approach remains careful about adaptation and aspiration effects. The paper explicitly argues that subjective satisfaction cannot be used directly as a synthetic measure of well-being because of physical-condition neglect and adaptation. This is the reason for the distinction between using satisfaction to estimate trade-offs and using it to measure welfare. Pages 28–30 are the key discussion. 

Empirically, the paper finds meaningful heterogeneity in preferences. Women and the highly educated place a relatively larger weight on income; younger and highly educated respondents care somewhat less about health; women are less negatively affected by unemployment and report different trade-offs with safety. Table 6 on page 40 is central here. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly. There is no feasible-set object, no opportunity menu, no latent jobs, no rationing, and no distinction between desired and available outcomes. This should be stated clearly. The framework measures well-being from realized income and realized non-income dimensions, conditional on estimated preferences. 

Unemployment appears as a realized life dimension, not as evidence of opportunity shortage or demand-side constraint. Safety, health, and social interactions are also treated as achieved outcomes or experienced states, not as indicators of opportunity sets. Therefore the paper is very useful for multidimensional welfare measurement, but not for the treatment of opportunities in your stronger (A)-sense. 

The paper helps distinguish preference heterogeneity from simple income-only welfare measurement, but it does not help distinguish preference heterogeneity from opportunity heterogeneity. [reasonable inference for my project] supported by 

# Welfare / normative object

The paper is explicitly normative. Its welfare object is individual well-being measured by equivalent income and social welfare measured by an inequality-sensitive aggregation of these equivalent incomes. This is not a reduced-form happiness index and not a dashboard only. 

The paper is directly relevant for preference-respecting welfare measurement and for inequality aversion. It is less directly relevant for responsibility versus compensation in the Fleurbaey–Maniquet sense, because it does not distinguish ethically between preference-driven and opportunity-driven inequalities. Nor does it use reference opportunity sets. 

It does not provide a decomposition of inequality into opportunities, preferences, and pay schedules. It does provide a decomposition of social welfare into average equivalent income and inequality, and it shows how country rankings change once non-income dimensions and inequality aversion are introduced. 

# Main findings

The first main finding is that adding non-income dimensions to the measurement of well-being changes country rankings substantially relative to rankings based on monetary income alone. In 2008, for instance, Germany and the Netherlands perform worse in equivalent-income rankings than in income rankings, while Denmark performs better. Table 7 on pages 42–43 is the main source. 

The second main finding is that health has the largest marginal effect on equivalent incomes among the included non-income dimensions, followed by social interactions and safety, while unemployment has a smaller average impact because it affects only a subpopulation. Table 8 on pages 44–45 is central. 

The third main finding is that inequality in well-being is much higher than inequality in income, because the non-income disadvantages tend to cumulate rather than offset one another. This is exactly the cumulative-deprivation phenomenon emphasized in the paper’s theoretical setup. Table 9 on pages 46–47 shows this clearly. 

The fourth main finding is that once both multidimensionality and inequality aversion are introduced, the financial crisis looks much worse for some countries, especially Greece and Spain. Greece’s social-welfare growth between 2008 and 2010 becomes dramatically more negative when a bottom-sensitive inequality-averse social welfare function is used. Table 12 on page 49 is the key result. 

The fifth main finding is that Scandinavian countries and Switzerland perform very well in the overall social-welfare ranking, whereas Eastern European countries, Russia, and—by growth performance during the crisis—Greece and Spain perform substantially worse. Tables 10 and 11 on pages 47–48 summarize these rankings. 

# Main limitations

A first limitation is the data. Income is measured rather crudely in the ESS, and the authors must apply an uprating procedure to make it comparable to macro income data. They are explicit that the ESS is not an ideal income dataset. Pages 38–39 and Appendix 1 make this clear. 

A second limitation is that the satisfaction-regression method captures only group-level preference heterogeneity, not individual-specific preferences. The conclusion explicitly stresses this. 

A third limitation is that some variables, especially self-assessed health, may be overweighted because subjective variables are more strongly correlated with life satisfaction than purely objective variables. The authors explicitly note this concern in the conclusion on page 50. 

A fourth limitation, relative to your project, is the absence of explicit opportunity modeling. Equivalent incomes are built from realized outcomes and preferences, not from realized bundles plus feasible sets and pay schedules. So the framework is powerful for multidimensional wellbeing measurement but not for justice with respect to opportunities. [reasonable inference for my project] supported by 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing the claim that a serious welfare metric must go beyond income yet remain aggregative and distribution-sensitive. It is an excellent bridge between “beyond GDP” discussions and a more rigorous welfare-theoretic approach.

## possible use for model design

It is useful for the welfare-measurement layer of the project. It gives a concrete way to turn multiple realized dimensions into a scalar individual well-being measure while respecting heterogeneous preferences.

## possible use for identification

It is useful mainly as a method for recovering preference trade-offs from satisfaction data. It is not useful for identifying opportunity sets or disentangling opportunities from preferences.

## possible use for welfare measurement

This is the strongest use. The paper is directly about the construction of a preference-respecting, inequality-sensitive measure of well-being and social progress.

## possible use for decomposition

It is only moderately useful. It decomposes social welfare into average equivalent income and inequality, but it does not provide your desired decomposition into (R), (A), and (y).

## possible use for comparative application

It is highly useful comparatively. The European cross-country application is one of the paper’s major strengths, and it provides a template for international welfare comparisons that go far beyond income.

# Research questions this paper inspires

Can equivalent income be extended from a ((y,x)) framework to a jobs-and-wellbeing measure (W(z,R,A;y)) where opportunity sets (A) enter directly rather than being omitted?

How would the country rankings change if one treated unemployment, safety, or health partly as opportunity outcomes rather than only as realized dimensions?

Can a richer version of equivalent income be estimated using labor-supply data or job-choice data rather than life-satisfaction regressions, thereby identifying more individual-specific preferences?

How can cumulative deprivation be decomposed into realized-outcome inequality versus opportunity-set inequality?

What is the correct social-welfare aggregation once equivalent incomes are constructed from a framework that distinguishes between preference-respecting private dimensions and socially compensable opportunity deficits?

# Challenge to this paper

The strongest challenge is that the paper’s normative architecture is stronger than its empirical identification of preferences. The equivalent-income idea is powerful, but the concrete implementation depends on life-satisfaction regressions, coarse income data, and group-level rather than individual-level preference heterogeneity. For your purposes, this means it is a strong welfare-measurement paper but not yet a complete empirical foundation for a richer jobs-and-wellbeing metric. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper proposes a scalar individual well-being measure based on equivalent income, built from realized income and non-income dimensions and corrected for preference heterogeneity. It then aggregates this into social welfare using an explicit inequality-aversion parameter. 

[reasonable inference for my project] In your notation, the paper is closest to a framework using realized bundles (z) and preferences (R), with (z) summarized by income plus several non-income dimensions. It uses an implicit money-metric transformation to produce a welfare index analogous to a (W(z,R,\cdot;\cdot)) object, but without explicit feasible-set or pay-schedule arguments. 

[unclear from paper] The paper does not define well-being as (W(z,R,A;y)), does not model feasible job sets (A), does not distinguish actual from reference opportunity sets, and does not discuss IIJ, IPIJ, independence of (A), or independence of (y). These issues are outside its scope. 

[reasonable inference for my project] In your taxonomy, the paper is close to preference-respecting welfare measurement and to reference-style money-metric evaluation. It is not close to responsibility for opportunities or to explicit opportunity-set analysis. It is therefore best treated as a strong benchmark for the (R)-side and realized-outcome side of your project, not for the (A)-side. 

# Relation to Bargain et al. (2013)

This paper is closely related in spirit to Bargain et al. (2013). Both are interested in how to construct interpersonal welfare comparisons that respect heterogeneous preferences and go beyond income. Bargain et al. operates in the consumption-leisure labor-supply space and compares alternative welfare metrics derived from estimated preferences; Decancq and Schokkaert operate in a broader multidimensional quality-of-life space and use equivalent income as the unifying metric. The present paper is therefore highly relevant as a broader, beyond-labor analogue to the preference-respecting welfare logic in Bargain et al. (2013). 

# Relation to opportunities vs preferences

This paper is much stronger on preferences than on opportunities. Its central contribution is to show how well-being measurement changes once one respects heterogeneous preferences over multiple life dimensions instead of imposing a common weighting scheme or relying on raw life satisfaction. 

But it does not model opportunities as feasible sets or constrained menus. So it should not be read as a solution to the opportunities-versus-preferences problem. Rather, it is a sophisticated welfare-measurement benchmark for the case where the main challenge is heterogeneity in (R), not heterogeneity in (A). 

# Useful quotations / formulas

The key social welfare formula is
[
SW = M(1-I_q),
]
equation (1) on page 30. This is the core aggregate object. 

The key inequality specification is the S-Gini family
[
I_q = 1-\sum_{i=1}^n \left[\left(\frac{n-i+1}{n}\right)^q-\left(\frac{n-i}{n}\right)^q\right]\frac{W_i}{M},
]
equation (2) on page 30. This is how the degree of inequality aversion is operationalized. 

The central operational formula for individual well-being is the equivalent-income expression
[
y_i^* = y_i \exp\left(\frac{b+c'z_i}{\lambda + p'z_i}\right)'(f(x_i)-f(\bar x)),
]
equation (5) on page 36. This is the main bridge from survey data to the welfare metric. 

# Suggested tags

equivalent-income, beyond-GDP, Europe, multidimensional-wellbeing, inequality-aversion, ESS, preference-respecting-welfare, cumulative-deprivation, Decancq-Schokkaert, social-welfare-measurement

# My quick takeaway

This is a core paper for the welfare-measurement side of your project. It shows that one can build a scalar, distributive, cross-country measure of well-being that respects heterogeneous preferences and goes beyond GDP, without collapsing into raw happiness or a purely objective index. Its main limitation for your JMP is that opportunities are absent as explicit feasible sets. Its main value is that it gives a rigorous empirical template for the (R)- and realized-(z)-side of any future (W(z,R,A;y)) framework.
