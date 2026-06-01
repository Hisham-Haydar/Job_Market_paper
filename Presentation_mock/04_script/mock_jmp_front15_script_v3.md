## Slide 1

**Final title**
**Main question: how much welfare inequality is really opportunity inequality?**

**Final bullet points**

* Main question: how much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than heterogeneous preferences, once labor supply is modeled as choice among latent jobs?
* The paper’s object is decomposition, not country ranking.
* Belgium is the baseline application; broader EUROMOD country coverage is extension only.
* The paper combines structural labor supply, welfare measurement, and inequality decomposition in one design.

**Speaker script**
Let me start with the question exactly as the paper is framed. I ask how much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than heterogeneous preferences, once labor supply is modeled as choice among latent jobs. That wording matters, because the paper is not primarily about hours elasticities, and it is not a welfare-ranking exercise across countries. The object is the decomposition of welfare inequality once jobs are treated as constrained opportunities rather than as freely chosen points on a common budget set. Empirically, I take Belgium as the baseline application and focus on prime-age childless single women. Conceptually, the contribution is to combine three layers that are often kept separate: a structural labor-supply model with latent opportunities, an opportunity-sensitive money-metric welfare object, and a decomposition that attributes welfare inequality to opportunities and preferences. The headline result is that unequal opportunities explain a substantial share of welfare inequality. So the core message is not that preferences do not matter. It is that a meaningful part of what standard models might read as taste heterogeneity is better understood as unequal access to jobs, and that this matters for welfare measurement.  

**Note on which visual to insert**
Insert a compact three-step title visual on the right: **latent jobs and opportunities → opportunity-sensitive welfare → decomposition of welfare inequality**.

---

## Slide 2

**Final title**
**Subquestion 1: do standard models overstate preference heterogeneity?**

**Final bullet points**

* The same observed bundle can be a chosen optimum for one person and a constrained second-best for another.
* If the model ignores constrained opportunities, it risks absorbing opportunity differences into tastes.
* That distorts both behavioral interpretation and welfare interpretation.
* The paper tests this against a common-choice-set benchmark.

**Speaker script**
The first subquestion is an identification problem with direct welfare consequences. Suppose two women are observed at the same hours-income bundle. In a standard common-choice-set model, it is natural to interpret that bundle as revealing similar preferences, up to noise. But once job opportunities are constrained and heterogeneous, the same observed bundle can have very different meanings. For one woman, it may be her preferred package from a relatively rich feasible set. For another, it may be a constrained second-best because better packages are simply not available to her. If the model does not represent that difference explicitly, it will tend to absorb opportunity gaps into leisure tastes. That is costly in two ways. First, it distorts the behavioral interpretation of heterogeneity, because part of what looks like taste variation is really variation in access to jobs. Second, it distorts the welfare interpretation, because the same outcome is being evaluated as if it emerged from the same choice environment. So the first question of the paper is whether standard models without explicit opportunity constraints systematically misread opportunity differences as preferences. Later in the talk I show that the benchmark without explicit opportunities fits worse and compresses the observed region-by-education gradients in employment. But the key point at the outset is conceptual: omitted opportunities do not disappear; they reappear as tastes.  

**Note on which visual to insert**
Insert a two-person schematic: same observed hours-income point in the center, but one person has a rich feasible job set and the other a truncated feasible set.

---

## Slide 3

**Final title**
**Three subquestions, one contribution**

**Final bullet points**

* Subquestion 1: to what extent do standard models misread opportunities as tastes?
* Subquestion 2: how should money-metric welfare be computed when feasible job sets differ?
* Subquestion 3: under a responsibility-sensitive view, how much welfare inequality is opportunity-driven?
* Contribution: one empirical pipeline that answers all three questions consistently.

**Speaker script**
The best way to read the paper is as one integrated pipeline built around three linked subquestions. The first is the identification question I just described: to what extent do standard labor-supply models without explicit opportunity constraints overstate preference heterogeneity by absorbing opportunity differences into tastes? The second is a welfare-measurement question: once feasible job sets differ across individuals, how should money-metric welfare actually be computed? The third is the decomposition question: if opportunities are not fully the individual’s responsibility, how much of welfare inequality should be attributed to unequal opportunities, and how much remains attributable to preferences? The contribution of the paper is that it answers these three questions inside a single design rather than treating them as separate exercises. First, I estimate a structural model with latent job opportunities and heterogeneous preferences. Second, I compute an opportunity-sensitive money-metric welfare level conditional on the estimated feasible set. Third, I decompose welfare inequality into opportunity and preference components using counterfactual equalizations and an order-independent Shapley-Shorrocks rule. That is the paper’s value added. It is not one more structural labor-supply model and not one more welfare-ranking exercise. It is a unified empirical framework for identifying, measuring, and decomposing welfare inequality in a world of jobs.  

**Note on which visual to insert**
Insert three numbered boxes labeled **Subquestion 1**, **Subquestion 2**, and **Subquestion 3**, all feeding into a final box labeled **Completed JMP contribution**.

---

## Slide 4

**Final title**
**Baseline empirical design: Belgium as the clean first application**

**Final bullet points**

* Baseline setting: Belgian EU-SILC matched to EUROMOD baseline tax-benefit rules.
* Sample: 3,284 childless single women aged 25–54.
* Labor supply is modeled over 16 job packages: non-employment plus 5 hours bins × 3 wage terciles.
* Opportunity heterogeneity varies by region × education; preference heterogeneity uses age, age², and two latent taste types.

**Speaker script**
The baseline application is intentionally narrow. I use Belgian EU-SILC matched to EUROMOD baseline tax-benefit rules, and I restrict attention to prime-age childless single women aged 25 to 54. The final estimation sample contains 3,284 women. This design choice is deliberate. It strips out joint household choice, childcare-related tax-benefit interactions, and self-employment measurement problems, so the first paper can stay focused on the core empirical object: whether unequal job opportunities explain a meaningful share of welfare inequality once preferences and opportunities are separated. Labor supply is represented over 16 alternatives: non-employment plus five weekly-hours bins crossed with three wage terciles. On the opportunity side, heterogeneity is allowed to vary with region and education. On the preference side, heterogeneity is disciplined through age, age squared, and two latent taste types. That is a narrow but defensible first-pass design. It is narrow enough to keep identification transparent, but rich enough to let unequal opportunities show up in economically meaningful ways. The broader EUROMOD portability of the framework matters, but only as extension. The baseline paper stands or falls on whether this Belgium design already delivers a credible and informative decomposition.   

**Note on which visual to insert**
Insert a Belgium map on the left and, on the right, a compact design table listing data source, sample, 16 alternatives, opportunity shifters, preference shifters, and welfare object.

---

## Slide 5

**Final title**
**Model logic and identification in a world of latent jobs**

**Final bullet points**

* Each woman chooses one package from 16 alternatives: non-employment plus five hours bins crossed with three wage terciles.
* Utility depends on disposable income, leisure, age, age squared, and two latent taste types.
* Opportunity heterogeneity enters through region × education differences in job availability.
* The main identification challenge is separating leisure tastes from opportunity probabilities.

**Speaker script**
The structural logic is straightforward. Each woman chooses one package from a finite set of 16 alternatives: non-employment, or one of fifteen employment packages formed by crossing five hours bins with three wage terciles. Utility depends on disposable income and leisure, with observed heterogeneity through age and age squared and unobserved heterogeneity through two latent taste types. That is the preference block. The opportunity block is separate. It governs the distribution of feasible job packages as a function of region and education. This separation is the core structural move of the paper. The model does not say that everyone faces the same menu and simply ranks it differently. It says that individuals differ both in the way they value packages and in the opportunities they actually face. The main identification challenge is then obvious: a model can fit observed choices either by moving leisure tastes or by moving opportunity probabilities. That is exactly why the first version stays parsimonious. I do not start with rich random coefficients or a highly detailed job taxonomy. I keep the opportunity mechanism disciplined and the taste heterogeneity controlled, so that the decomposition does not look like an artifact of excessive flexibility. In the full deck I then show that this opportunity-sensitive specification outperforms a common-choice-set benchmark, which is the empirical reason to take the opportunity block seriously.  

**Note on which visual to insert**
Insert the 16-package matrix, with a side bracket labeling the **preference block** and another labeling the **opportunity block**.

---

## Slide 6

**Final title**
**Subquestion 2: how should welfare be computed when feasible job sets differ?**

**Final bullet points**

* Welfare is equivalent monthly disposable income at a non-employment/full-leisure reference state.
* Welfare is computed from expected utility conditional on the estimated feasible set.
* The baseline inequality object is the Gini of individual welfare levels.
* Decomposition uses a two-factor Shapley-Shorrocks rule: opportunities versus preferences.

**Speaker script**
The second subquestion is about welfare measurement rather than estimation. Once feasible job sets differ across individuals, welfare cannot be computed as if everyone faced a universal menu. So I do not use observed disposable income as the welfare object, and I do not use the raw estimated utility index either. Instead, I compute opportunity-sensitive money-metric welfare as equivalent monthly disposable income at a common non-employment, full-leisure reference state. Operationally, I take expected utility under the estimated feasible set and convert it into the cash amount at that reference point that would make the individual indifferent. That gives a welfare level that is comparable across individuals while still respecting the fact that their opportunity sets differ. Once I have those welfare levels, the baseline inequality object is the Gini coefficient of individual welfare. I then ask how that Gini changes under counterfactual equalizations. One counterfactual equalizes opportunities. Another neutralizes preferences. A final counterfactual does both. The decomposition itself uses a two-factor Shapley-Shorrocks rule, so the contribution assigned to opportunities and the contribution assigned to preferences are not driven by an arbitrary sequence of elimination. That is the key link between subquestion 2 and subquestion 3: once welfare is defined correctly, decomposition becomes well posed.  

**Note on which visual to insert**
Insert a flow chart: **estimated model → expected utility under feasible set → equivalent monthly disposable income at reference state → welfare Gini → Shapley decomposition**.

---

## Slide 7

**Final title**
**Subquestion 3: how much welfare inequality is opportunity-driven?**

**Final bullet points**

* Disposable-income Gini: **0.164**; opportunity-sensitive welfare Gini: **0.186**.
* Opportunity equalization lowers the welfare Gini to **0.151**.
* Preference equalization lowers the welfare Gini to **0.140**; equalizing both lowers it to **0.097**.
* Opportunity heterogeneity explains **0.039** Gini points: **43.8%** of the explained component and **21.0%** of baseline welfare inequality.

**Speaker script**
Now the main result. In the Belgium baseline, disposable-income inequality and welfare inequality are not the same object. The disposable-income Gini is 0.164, while the opportunity-sensitive welfare Gini is 0.186. So once unequal feasible job sets are brought into the welfare measure, measured inequality rises. I then ask what happens under counterfactual equalizations. If I equalize opportunities, the welfare Gini falls from 0.186 to 0.151. If I equalize preferences, it falls to 0.140. If I equalize both, it falls to 0.097. Using the two-factor Shapley-Shorrocks decomposition, opportunity heterogeneity accounts for 0.039 Gini points. That is 43.8 percent of the explained component of welfare inequality, and 21.0 percent of baseline welfare inequality. Preference heterogeneity accounts for 0.050 Gini points, or 56.2 percent of the explained component. This is exactly the balance I want the audience to take away. Opportunities matter a great deal, but they do not swamp preferences. That makes the result structural rather than rhetorical. At the same time, the opportunity component is far too large to be treated as background friction. By the end of this slide, the main question and the three subquestions have one integrated answer: once jobs are modeled as constrained opportunities, welfare should be measured conditional on those constraints, and unequal opportunities emerge as a quantitatively important source of welfare inequality.  

**Note on which visual to insert**
Insert the main stacked-bar decomposition figure based on the baseline welfare Gini of **0.186**, with an inset table showing: baseline **0.186**, opportunity equalized **0.151**, preference equalized **0.140**, both equalized **0.097**.
