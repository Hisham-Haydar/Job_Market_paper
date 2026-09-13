Below is the final continuation for **slides 8–14 only**, written to follow naturally from a front-loaded 15-minute core. The logic stays faithful to `mock_jmp_slide_outline_v5.md`, and all quantitative claims are kept consistent with `mock_jmp_completed_results_v1.md`.  

---

## Slide 8

**Final title**
**The Belgium baseline: data, sample, and institutional environment**

**Final bullet points**

* Baseline application: Belgian EU-SILC matched to EUROMOD baseline tax-benefit rules.
* Final estimation sample: **3,284** prime-age childless single women aged **25–54**.
* Observed employment rate: **77.6%**; mean employed weekly hours: **34.9**; mean gross hourly wage: **€15.8**.
* Region shares: **56.8% Flanders, 30.9% Wallonia, 12.3% Brussels**; education shares: **25.9% low, 42.5% medium, 31.6% high**.

**Speaker script**
Let me now open the black box behind the core result. Everything I showed in the first 15 minutes comes from a deliberately narrow Belgium baseline. The data are Belgian EU-SILC matched to EUROMOD baseline tax-benefit rules, and the final estimation sample contains 3,284 childless single women aged 25 to 54. This is a very purposeful design. It gives me a sample that is economically meaningful, but still strips out the main sources of avoidable complexity in a first paper: joint household choice, childcare-related tax-benefit interactions, and self-employment measurement issues. The sample is also not marginal in labor-market terms. Observed employment is 77.6 percent, mean employed weekly hours are 34.9, mean gross hourly wage is 15.8 euros, and mean monthly disposable income is 1,694 euros. Region and education composition matter because they are exactly where the opportunity mechanism is allowed to vary: 56.8 percent of the sample is in Flanders, 30.9 percent in Wallonia, and 12.3 percent in Brussels; education is split across low, medium, and high groups in proportions of 25.9, 42.5, and 31.6 percent. This slide connects back most directly to **subquestion 1**, because it shows the observed heterogeneity the opportunity block has to explain, and to **subquestion 3**, because those same region-by-education cells are later the basis for the decomposition. 

**Note on which visual to insert**
Insert a two-panel slide: on the left, a compact sample-statistics table using the numbers above; on the right, a Belgium map or simple region-by-education layout emphasizing that the opportunity mechanism varies across these cells.

---

## Slide 9

**Final title**
**The 16 job packages and what the model is actually estimating**

**Final bullet points**

* Labor supply alternatives: **16 packages**.
* Package definition: **non-employment + 5 hours bins × 3 wage terciles**.
* Hours bins: **1–15, 16–24, 25–34, 35–44, 45+**.
* The model separately estimates the **preference block** and the **opportunity block** over this package space.

**Speaker script**
This slide makes the latent-jobs language concrete. The model is not estimating an abstract notion of constrained choice in the air; it is estimating choice over 16 explicit labor-supply alternatives. Those are non-employment plus five weekly-hours bins crossed with three wage terciles. The hours bins are 1 to 15, 16 to 24, 25 to 34, 35 to 44, and 45-plus. This is the narrowest defensible package structure for a first pass. It is rich enough to reflect the two margins that matter most for both labor supply and welfare — working time and earning power — but still compact enough that the source of identification remains transparent. This slide connects especially to **subquestion 1**, because it shows what the benchmark common-choice-set model is abstracting from, and to **subquestion 2**, because welfare is later computed over this exact package space. The separation is important: the preference block ranks accessible packages, while the opportunity block governs access to them. That distinction is the backbone of the entire paper. Once we define the choice set in this way, equalizing opportunities is no longer a vague idea. It means equalizing access to a well-defined distribution of labor-market packages, rather than just shifting an abstract taste parameter.  

**Note on which visual to insert**
Insert a clear 4-by-4 style package grid: one cell for non-employment and 15 cells for the hours-bin by wage-tercile combinations. Label the grid so the audience sees immediately what counts as a package.

---

## Slide 10

**Final title**
**Preference estimates: heterogeneity is real, but disciplined**

**Final bullet points**

* Log disposable income enters positively: coefficient **2.946**.
* Two latent taste types: leisure coefficient **1.428** for Type 1; Type 2 adds **0.612**, implying **2.04**.
* Implied Type 2 population share: **39.0%**.
* Work fixed cost is sizable: **-1.324**; the marginal value of leisure rises with age, but concavely.

**Speaker script**
After defining the package space, the next step is to ask whether the preference block looks economically sensible. It does. Utility loads positively on log disposable income, with an estimated coefficient of 2.946. Leisure also matters strongly, and the model recovers two latent taste types. Type 1 has a leisure coefficient of 1.428, while Type 2 adds 0.612 on top of that, implying an overall coefficient of roughly 2.04. The implied share of the more leisure-oriented type is 39 percent. The work fixed cost is also economically meaningful, at minus 1.324. Finally, the age terms imply that the marginal value of leisure rises with age within the prime-age window, but at a decreasing rate. This is where I want to be careful in how I defend the paper. The message is not that preferences are unimportant. In fact, the decomposition already showed that preferences account for slightly more of the explained component than opportunities do. The point is narrower and stronger: once a separate opportunity mechanism is allowed for, the preference block no longer needs to do all the work. This slide therefore connects mainly to **subquestion 1**. It shows that preference heterogeneity remains real and interpretable, but it is disciplined enough that it is not simply standing in for omitted constraints. That is exactly the balance a mature structural paper should deliver. 

**Note on which visual to insert**
Insert a compact coefficient table or coefficient plot for the preference block only, with a small annotation translating the Type 2 shift into the implied total leisure coefficient and noting the 39.0 percent latent-class share.

---

## Slide 11

**Final title**
**Opportunity estimates: unequal access to jobs is economically structured**

**Final bullet points**

* Relative to medium-educated women in Flanders, total offer intensity is lower in **Wallonia (-0.150)** and **Brussels (-0.192)**.
* Low education lowers total offer intensity **(-0.108)**; high education raises it **(+0.151)**.
* Implied relative total offer intensity ranges from **0.65** to **1.16** across region × education cells.
* Standard-hours packages are much more prevalent than fringe-hours jobs; top-wage packages are relatively scarcer.

**Speaker script**
This is the most distinctive structural object in the paper. The opportunity block is not a nuisance term in the likelihood; it is where the model locates unequal access to jobs. Relative to the reference cell of medium-educated women in Flanders, total offer intensity is lower in Wallonia by 0.150 and lower in Brussels by 0.192. Low education reduces offer intensity by 0.108, while high education raises it by 0.151. When those effects are translated into implied relative total offer intensity, the range across region-by-education cells is economically meaningful: from 0.65 for low-educated women in Brussels up to 1.16 for highly educated women in Flanders. The opportunity mechanism also has structure along the composition margin. Standard-hours packages are much more prevalent than fringe-hours jobs, and top-wage packages are relatively scarcer on average. This slide connects directly to **subquestion 1**, because it shows the source of heterogeneity that a common-choice-set model would tend to push into tastes. It also connects to **subquestion 3**, because these same gradients are exactly what is being compensated in the opportunity equalization exercise. So the point is not just that opportunities differ. It is that they differ in a patterned, economically interpretable way that maps directly into the later welfare decomposition. 

**Note on which visual to insert**
Insert a heatmap of implied relative offer intensity by region × education cell, using the 0.65 to 1.16 range, plus a small secondary bar chart showing the relative composition of hours and wage packages.

---

## Slide 12

**Final title**
**Subquestion 1 revisited: what the common-choice-set benchmark misses**

**Final bullet points**

* Full opportunity-sensitive model pseudo-R²: **0.271** versus **0.214** in the common-choice-set benchmark.
* Exact 1-of-16 package hit rate: **39.2%** versus **33.8%**.
* Employment classification hit rate: **82.4%**.
* The main gain is recovering the strong region × education gradients in employment.

**Speaker script**
I can now return explicitly to the first subquestion: to what extent do models that ignore constrained opportunities overstate preference-based explanations? The completed-results pack does not give me a parameter-by-parameter comparison of taste dispersion across the two models, so I do not claim that directly. But what it does show is the next-best and, in many ways, more persuasive piece of evidence: the opportunity-sensitive model fits the data materially better exactly where the omitted-opportunity problem should bite. The pseudo-R² rises from 0.214 in the common-choice-set benchmark to 0.271 in the full model. The exact 1-of-16 package hit rate rises from 33.8 percent to 39.2 percent. Employment classification accuracy reaches 82.4 percent. Most importantly, the full model recovers the strong region-by-education gradients in market attachment that the benchmark compresses too much. That last point is critical. If the benchmark systematically flattens the gradients that are visibly present in the data, then it must be explaining those differences elsewhere, and the obvious place is the preference block. So this slide sharpens the answer to **subquestion 1**: I do not claim that omitted opportunities disappear. I claim that when the model cannot represent them explicitly, it reallocates them to tastes. The fit evidence is exactly consistent with that interpretation. 

**Note on which visual to insert**
Insert a two-panel figure: on the left, observed versus predicted employment by region × education cell; on the right, a compact benchmark comparison table with pseudo-R², exact package hit rate, and employment hit rate.

---

## Slide 13

**Final title**
**Subquestion 3 revisited: decomposition and responsibility sensitivity**

**Final bullet points**

* Baseline opportunity component: **0.039** Gini points, or **21.0%** of baseline welfare inequality.
* If only **education** is compensated, the opportunity component falls to **0.031**.
* If only **region** is compensated, it falls to **0.026**.
* Even under stricter responsibility stances, opportunities still explain about **14–17%** of baseline welfare inequality.

**Speaker script**
The natural concern with any opportunity-based decomposition is that it may look normatively loaded. So here I revisit the third subquestion under stricter responsibility interpretations. In the baseline, I treat the full region-by-education opportunity gradient as compensation-relevant. Under that stance, the opportunity component is 0.039 Gini points, which is 21.0 percent of baseline welfare inequality and 43.8 percent of the explained component. I then tighten the responsibility stance in two ways. If only education is treated as compensable, the opportunity component falls to 0.031. If only region is treated as compensable, it falls further to 0.026. Those are meaningful reductions, and they should occur if the decomposition is behaving properly. But what matters for the paper is that the opportunity contribution does not disappear. Even under the stricter interpretations here, unequal opportunities still explain between 14 and 17 percent of baseline welfare inequality. This slide therefore deepens the answer to **subquestion 3**. The conclusion is not that there is one uniquely correct moral stance. It is that across a range of reasonable responsibility-sensitive views, unequal opportunities remain too important to be ignored in welfare analysis. That strengthens the case that the baseline result is substantive rather than merely rhetorical. 

**Note on which visual to insert**
Insert a three-bar responsibility-sensitivity figure comparing the opportunity component under the baseline, education-only, and region-only compensation definitions, with the 0.039, 0.031, and 0.026 values labeled directly.

---

## Slide 14

**Final title**
**Conclusion: answers to the main question and the three subquestions**

**Final bullet points**

* Main question: a substantial part of welfare inequality in the Belgium baseline is attributable to unequal job opportunities.
* Subquestion 1: models without explicit constrained opportunities risk misreading opportunity gradients as tastes.
* Subquestion 2: welfare should be computed conditional on the feasible set, not on a universal menu.
* Subquestion 3: under reasonable responsibility-sensitive views, opportunities account for a large but not dominant share of welfare inequality.

**Speaker script**
Let me close by answering the paper’s questions directly. The main question was how much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than heterogeneous preferences once labor supply is modeled as choice among latent jobs. In the Belgium baseline, the answer is: a substantial amount. Welfare inequality is higher than disposable-income inequality once constrained opportunities are brought into the welfare object, and opportunity heterogeneity accounts for a large share of the explained component of welfare inequality. The first subquestion asked whether standard models risk overstating preference heterogeneity when they do not model constrained opportunities explicitly. The answer is yes in a structural sense: the benchmark without explicit opportunities fits worse and compresses the observed region-by-education gradients that the full model recovers. The second subquestion asked how welfare should be computed when feasible job sets differ. The answer is that it should be computed conditional on the feasible set, using an opportunity-sensitive money-metric welfare object rather than a universal-menu metric. The third subquestion asked how much welfare inequality is opportunity-driven once opportunities are treated as not fully the individual’s responsibility. The answer is that the opportunity component is large, robust, and economically meaningful, though not dominant over preferences. That is the completed-paper message I want the committee to remember. Belgium is the clean baseline application. Broader EUROMOD country coverage is the natural next step, but as extension and scalability — not as the identity of this paper.  

**Note on which visual to insert**
Insert a closing slide with four boxes: **Main question**, **Subquestion 1**, **Subquestion 2**, **Subquestion 3**, each containing a one-line answer, and a small final box underneath labeled **Broader agenda: scale-up beyond Belgium using the same pipeline**.
