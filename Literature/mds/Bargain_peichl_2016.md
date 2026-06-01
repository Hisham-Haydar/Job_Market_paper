---

title: "Own-wage labor supply elasticities: variation across time and estimation methods"
authors: ["Olivier Bargain", "Andreas Peichl"]
year: 2016
outlet: "IZA Journal of Labor Economics"
country_or_context: "Western Europe and the United States"
population: "Review/meta-analysis covering married women, married men, childless single women and men, and single mothers across many studies rather than one estimation sample"
data_period: "Surveyed evidence spans roughly 1967–2005 depending on country and study"
shelf: "labor_supply_elasticities_methodology_review"
tags: ["labor supply elasticities", "meta-analysis", "structural labor supply", "Hausman model", "discrete choice", "time trends", "Europe", "United States", "taxation", "policy simulation"]
priority: "very high"
read_status: "extracted"
------------------------

# Full citation

Bargain, Olivier, and Andreas Peichl. 2016. “Own-wage labor supply elasticities: variation across time and estimation methods.” *IZA Journal of Labor Economics* 5:10. 

# One-sentence contribution

The paper surveys static labor-supply elasticity estimates for Western Europe and the US and shows, through a meta-analysis, that the major source of variation across studies is the observation period—especially the long decline in elasticities since the 1980s—rather than the estimation method itself. 

# Why this paper matters

This paper matters because it addresses a practical bottleneck in structural labor-supply and public-finance work: researchers routinely need elasticity values for ex ante reform simulation or optimal-tax calibration, yet the literature contains very heterogeneous estimates. The paper’s main value is to organize that heterogeneity and to ask systematically whether it comes from real behavioral change over time or from methodological differences across studies. 

For your project, it is especially useful as a methodological benchmark on the (R)- and (y)-sides of the problem. It is not a paper about feasible job sets or opportunity-sensitive welfare, but it is highly relevant if you want to understand what structural labor-supply elasticities can and cannot tell you, and how cautious one should be when importing them into policy simulation or normative analysis. 

# Core research question

Why do own-wage labor-supply elasticities vary so much across studies, and in particular how much of that variation is due to changes over time versus differences in estimation methods? 

# Economic setting and context

The paper is a review and meta-analysis rather than a single-country application. Its empirical universe is the literature on static labor-supply models for Western Europe and the US, with particular attention to married women, single mothers, men, and childless singles. The context is tax-benefit policy analysis, where labor-supply elasticities are used to simulate reforms or calibrate optimal-tax models. 

The policy motivation is explicit from the first page: the size of labor-supply responses matters for ex ante evaluation of tax-benefit reforms and for optimal-tax calculations, yet there is “huge variation” in the literature and little agreement on which elasticity values are credible for policy use. The paper is therefore situated squarely in the intersection of labor-supply econometrics and public economics. 

# Model / theoretical framework

The paper does not present one new structural behavioral model. Instead, it reviews three broad empirical approaches to static labor-supply estimation. The first is the traditional continuous-hours/Hausman approach, relying on labor-supply functions derived from consumption-leisure preferences and local linearization or related treatments of budget sets. The second is the discrete-choice structural approach associated with van Soest-type models, where individuals choose among discrete hours alternatives under full tax-benefit simulation. The third is the natural-experiment or quasi-experimental approach, which uses policy reforms or discontinuities to estimate labor-supply responses without fully specifying a structural model. Section 2 is devoted to these methods. 

The agent’s choice problem, in the literature being reviewed, is a standard static labor-supply problem in the consumption-leisure space. The paper is explicit that its object is “steady-state elasticities,” that is, wage or income elasticities of participation or worked hours in static frameworks. The framework is therefore positive and behavioral, not an explicit welfare or fairness framework. 

Opportunities or feasible job sets are not modeled explicitly in the paper’s core framework. The review discusses hours choice, participation, taxes, benefits, and in some cases fixed costs, rationing, or unemployment risk in the underlying literature, but not a set-valued opportunity object (A). This is crucial for locating the paper relative to your project. 

# Key objects

The central objects are uncompensated own-wage elasticities, income elasticities, and their variation across demographic groups, countries, periods, and methods. The paper defines the uncompensated wage elasticity as
[
\varepsilon^u = \frac{dh}{dw}\frac{w}{h},
]
the income elasticity as
[
\varepsilon^Y = \frac{dh}{dy}\frac{y}{h},
]
and, using the Slutsky equation, the compensated wage elasticity as
[
\varepsilon^c = \varepsilon^u - \frac{wh}{y}\varepsilon^Y.
]
These formulas appear in Section 3 and are among the most useful formal statements in the paper. 

A second key object is the study-level dataset assembled for the survey and meta-analysis. The paper compares 282 elasticity estimates from 92 studies, including 156 wage elasticities for individuals in couples, 70 wage elasticities for single individuals and lone parents, and 56 income elasticities. This is the empirical basis for the review. 

A third key object is the meta-regression design. The elasticity value from each study is regressed on study characteristics such as observation year, estimation method, whether desired hours are used, whether joint decision-making in couples is modeled, whether fixed costs are included, and whether the estimate pertains to the US. Tables 4 and 5 summarize these meta-regressions. 

# Data

Because this is a review article, there is no single micro dataset. The paper instead constructs a database of elasticity estimates extracted from the literature. The evidence base covers both Western Europe and the US and spans a long period, roughly from the late 1960s to the mid-2000s depending on country and study. 

The survey tables are themselves a major empirical contribution. Tables 1–3 on pages 7–15 list country, authors, data source, demographic group, model type, specification, tax-benefit treatment, and reported wage and income elasticities. Table 1 covers European couples, Table 2 European singles, and Table 3 the US. 

# Identification logic

The paper is not a new identification study in the usual microeconometric sense. Rather, it reviews the identification logic of the underlying literature. The continuous/Hausman approach relies on cross-sectional variation in after-tax wages and virtual income, with endogeneity and measurement-error issues around wages and non-labor income. The discrete-choice approach relies mainly on nonlinearities, discontinuities, and non-convexities in tax-benefit schedules, together with demographic taste shifters and sometimes policy variation over time or across jurisdictions. The natural-experiment literature relies on reforms or discontinuities for reduced-form identification. Section 2 is explicit on all of this. 

The paper’s own meta-analysis is descriptive rather than causally identified in a strong sense. The authors explicitly state in the endnotes that, like all meta-regressions, their analysis is not identifying causal effects. This is an important caveat. It means their conclusions about time versus method should be interpreted as systematic patterns in the literature, not as definitive causal decomposition. 

For your project, the main identification lesson is methodological rather than substantive: elasticity estimates should not be imported mechanically from the literature without regard to demographic group, period, and model architecture. This is especially important if one wants to use them in policy simulation or in any downstream welfare or decomposition exercise. [reasonable inference for my project] supported by 

# Estimation / empirical strategy

The empirical strategy has two layers. First, the paper undertakes a structured survey of the literature, assembling and classifying estimates by demographic group, country, period, and method. Figures 1 and 2 on page 16 then visualize the distribution of wage elasticities by demographic group and by country. These figures already show the central stylized facts: married women and single mothers exhibit the largest elasticities, while men and childless singles show smaller and less dispersed estimates. 

Second, the paper runs simple meta-regressions at the study-estimate level. The outcome is the reported elasticity, and the explanatory variables include the data year, a dummy for discrete-choice estimation, whether desired rather than observed hours are used, whether a joint household decision model is estimated, whether fixed costs are included, and whether the estimate comes from the US. Tables 4 and 5 on pages 23 and 25 report these regressions for married women and for married women plus single mothers. 

The central meta-analytic result is that the coefficient on year is robustly negative, while the method dummy is generally insignificant once time is controlled for. The authors summarize this as evidence that time changes matter more than estimation methods in explaining the historical variation in labor-supply elasticity estimates. 

# Treatment of preferences

Preferences are treated as the deep behavioral object in the underlying labor-supply literature, but the paper is careful not to overstate what observed cross-study variation tells us about them. It explicitly notes earlier evidence, especially Bargain et al. (2014), showing that only a small share of international variation in elasticities is driven by genuine cross-country differences in work preferences. This is an important analytical stance: the paper resists the temptation to interpret every elasticity difference as a preference difference. 

At the same time, the paper accepts that time changes may reflect changes in preferences, especially changing female attachment to the labor market. In the discussion of the shrinking elasticity hypothesis, the authors mention possible explanations such as more stable labor-market participation of women, changes in childcare policies, social preferences, or domestic technology. These are proposed explanations, not identified results. 

The paper is therefore strong on the positive treatment of preferences as behavioral primitives, but it does not turn preferences into a welfare object. It is not about whether heterogeneous preferences should be respected or compensated. That puts it in a different category from Bargain et al. (2013). 

# Treatment of opportunities / constraints

This section is where the paper is least aligned with your core framework. The review is centered on static consumption-leisure labor-supply models and their estimated elasticities. Opportunities are not represented as feasible job sets, latent job distributions, or explicit labor-demand opportunity structures. There is no direct analogue of (A) in the paper’s main conceptual apparatus. 

That said, the review does acknowledge various empirical constraints that appear in the literature: fixed costs of work, part-time dummies, unemployment risk, welfare participation, childcare costs, and in some cases rationing. These appear as modeling devices in some of the studies surveyed, but not as a unified opportunity-set concept. The paper’s primary distinction is between intensive and extensive margins of labor-supply response, not between preferences and feasible opportunities. 

So the paper helps little with separating preference heterogeneity from opportunity heterogeneity in your (R) versus (A) sense. It is much more useful for understanding how the estimated sensitivity of observed labor supply to (y)-type financial incentives varies across studies. [reasonable inference for my project] supported by 

# Welfare / normative object

The paper is not an individual well-being paper and not an explicit social-welfare paper either. Its interest in normative public economics is indirect: labor-supply elasticities are needed inputs for optimal tax calculations and ex ante policy simulations. The clearest illustration is in the conclusion, where the paper notes that different elasticity assumptions can generate very different optimal top tax rates in Diamond–Saez-style calculations. 

Thus the normative object is not welfare itself, but a policy-analytic parameter. The paper is about how to choose plausible behavioral elasticities for policy use. It does not construct an individual welfare metric, does not discuss responsibility versus compensation, and does not study inequality decomposition. 

From your standpoint, this makes the paper relevant upstream rather than downstream. It helps discipline the behavioral inputs that later feed into welfare or optimal-tax analysis, but it does not tell you how to measure well-being when preferences and opportunities differ. 

# Main findings

The first major finding is a confirmation and refinement of the standard demographic ranking. Married women have the largest body of evidence and relatively large wage elasticities; single mothers also exhibit relatively large elasticities; men and childless singles generally show much smaller elasticities. Figures 1 and 2 on page 16 visually summarize this distribution across demographic groups and countries. 

The second major finding is the paper’s headline result: there is a strong downward trend in labor-supply elasticities over time, especially for married women and single mothers. Figure 3 on pages 19–20 shows a clear negative correlation between the observation period and the elasticity size. The paper explicitly extends the earlier US evidence of Heim (2007) and Blau and Kahn (2007) by showing a similar pattern for European estimates. 

The third major finding is that the estimation method itself explains little once time is accounted for. Figures 4 and Tables 4–5 show that although early Hausman-based studies often reported larger elasticities and recent discrete-choice studies often report smaller ones, this pattern is largely driven by the fact that the methods are used in different periods. In the meta-regressions, the year coefficient is negative and statistically important, while the dummy for discrete-choice models is generally insignificant once time is controlled for. 

A fourth finding, more technical but useful, is that using desired rather than observed hours tends to raise estimated elasticities, which the authors interpret as evidence that observed-hours models partly understate potential responses because they are contaminated by labor-demand or institutional constraints on hours. This result appears in the meta-regressions. 

# Main limitations

A first limitation is that the paper is a meta-review, not a harmonized re-estimation of all studies. Even though the survey is extensive, the underlying estimates differ in sample selection, elasticity definition, budget-constraint treatment, and institutional coverage. The authors themselves stress that one should not expect one “right” elasticity. 

A second limitation is that the meta-analysis is not causally identified. The paper explicitly notes that its meta-regressions do not identify causal effects. Hence the conclusion that time matters more than method is persuasive but still inferential rather than definitive. 

A third limitation, relative to your project, is the near absence of an opportunity-set perspective. The paper does not ask whether declining elasticities over time reflect changes in feasible job sets, labor-demand structures, or opportunity heterogeneity. Those mechanisms remain mostly implicit. 

A fourth limitation is that the paper focuses on steady-state static elasticities and deliberately leaves aside other margins such as taxable-income responses, migration, evasion, human capital investment, and macro elasticities. That is appropriate for its purpose, but it narrows the behavioral object being summarized. 

# Relevance for my JMP

## possible use for framing

This paper is highly useful for framing because it shows that elasticity choice is itself a substantive research decision. In any jobs-and-wellbeing or structural public-economics project, one cannot simply pick a “standard” wage elasticity without regard to demographic group and period.

## possible use for model design

It is moderately useful for model design. The review clarifies the strengths and weaknesses of the Hausman and discrete-choice traditions and supports the use of discrete-choice models for policy simulation. It does not help directly with RURO or explicit feasible-set design.

## possible use for identification

It is useful mainly as a map of identification strategies in the labor-supply literature. It compares structural cross-sectional identification, grouped estimators, reform-based variation, and natural experiments. That is valuable for positioning your own empirical strategy.

## possible use for welfare measurement

Directly, limited. The paper does not provide a welfare measure. Indirectly, strong: any welfare or policy analysis that uses labor-supply elasticities needs exactly the caution this paper recommends.

## possible use for decomposition

It is limited for your (R/A/y) decomposition agenda. It does not decompose inequality or welfare by opportunities, preferences, and pay schedules. It does, however, decompose variation in elasticity estimates across studies into time and method components.

## possible use for comparative application

It is very useful comparatively. One of the paper’s strengths is its cross-country overview of Europe and the US and its insistence that apparently huge cross-country differences are often overstated once one controls for period and method.

# Research questions this paper inspires

1. How much of the observed decline in labor-supply elasticities over time reflects changing preferences (R) versus changing feasible opportunities (A)?

2. Can one construct an opportunity-sensitive analogue of this review in which the primary object is not just (dh/dw) but the responsiveness of choices to changes in feasible job sets?

3. If elasticities are highly time-specific, how should structural policy models be updated when they are used several years after estimation?

4. Can discrete-choice models with explicit latent job opportunities generate a different time profile of elasticities than standard consumption-leisure models?

5. How should a jobs-and-wellbeing framework choose behavioral inputs when the literature contains many elasticities but no single “correct” one?

# Challenge to this paper

The strongest challenge is that the paper explains variation in estimated behavioral responses without fully opening the black box of why those responses changed over time. It documents that elasticities shrank and that method is not the primary culprit, but it does not provide a structural explanation distinguishing changes in work preferences, childcare institutions, demand-side opportunities, or other social and technological changes. For your project, that unresolved mechanism matters. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper is about labor-supply elasticities in static models and about how those elasticities vary across studies because of time period and estimation method. It is directly concerned with behavioral responsiveness to financial incentives, not with individual well-being as such. 

[reasonable inference for my project] In your notation, the paper is most closely related to the mapping from pay schedules (y) into observed choices (z), conditional on preferences (R). It tells you how sensitive labor-supply outcomes are to wage and tax-benefit variation, and how that sensitivity differs by group and period. This makes it relevant to the (R)-(y)-(z) relationship. 

[unclear from paper] The paper does not define a well-being measure (W(z,R,A;y)), does not formalize feasible sets (A), and does not study axioms such as independence of (A), independence of (y), IIJ, IPIJ, reference opportunity sets, or responsibility for opportunities. Those issues are not part of its formal scope. 

[reasonable inference for my project] In your taxonomy, the paper is not close to independence of (y); on the contrary, it is centrally about responsiveness to (y)-type financial incentives. It is also not close to independence of (A), but mainly because (A) is not modeled explicitly. It is best viewed as a methodological benchmark for the behavioral side of your framework, not as a paper on well-being or opportunity-sensitive justice. 

# Relation to Bargain et al. (2013)

This paper is complementary to Bargain et al. (2013), not a substitute for it. Bargain et al. (2013) is about how individual welfare rankings change when heterogeneous consumption-leisure preferences are respected under alternative welfare metrics. The 2016 review, by contrast, is about the size and variation of labor-supply elasticities and their use in policy simulation. In simple terms, the 2013 paper is on the welfare side of heterogeneous preferences, whereas the 2016 paper is on the behavioral-response side.

# Relation to opportunities vs preferences

This paper is much more useful for preferences than for opportunities. Its central concern is how measured labor-supply responses vary across demographic groups, periods, and methods, and how much of that variation can plausibly be attributed to changing work preferences or related behavioral factors. 

But it does not offer an opportunity-set framework. It says very little about whether low or declining responsiveness is due to worse or tighter opportunities rather than different preferences. So for your project it should be treated as essential for the (R)-side of behavioral modeling, but as weak on the (A)-side. 

# Useful quotations / formulas

The most useful formulas are the basic elasticity definitions in Section 3:
[
\varepsilon^u = \frac{dh}{dw}\frac{w}{h}, \qquad
\varepsilon^Y = \frac{dh}{dy}\frac{y}{h}, \qquad
\varepsilon^c = \varepsilon^u - \frac{wh}{y}\varepsilon^Y.
]
These are the paper’s foundational objects. 

Figure 3 on pages 19–20 is especially important. It visually shows the negative time trend in wage elasticities for married women and single mothers, with a particularly clear downward pattern from older to newer data years in both Europe and the US. 

Tables 4 and 5 on pages 23 and 25 are the most important tables. They show that the coefficient on year is negative and significant in the meta-regressions, whereas the discrete-choice-method dummy is generally not robustly significant once year is controlled for. 

# Suggested tags

labor-supply-elasticities, meta-analysis, static-labor-supply, Hausman, discrete-choice, time-trends, policy-simulation, Europe, USA, Bargain-Peichl

# My quick takeaway

This is a core methodological paper for the behavioral side of your corpus. It does not help much with opportunity sets or with well-being measurement, but it is extremely useful for understanding what labor-supply elasticities mean, why they differ across studies, and why recent period-specific estimates matter more than old “classic” values. For your JMP, its main contribution is disciplined caution: any use of elasticities in structural or normative policy work must be demographic-specific, period-specific, and sensitivity-tested.
