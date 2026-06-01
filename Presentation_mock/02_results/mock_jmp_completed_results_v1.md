Below is a synthetic completed-results pack calibrated to the fixed Belgium / prime-age childless single women / 16-job-package / region × education / opportunity-sensitive welfare design in your concept and prototype notes, and formatted to read like a finished RURO structural labor-supply paper in the style of the Belgian RURO application and the Aaberge–Colombino results sections. All numerical entries are synthetic mock estimates, but they are internally coherent and presentation-ready.     

## 1. TABLE 1 — Sample and institutional setup

**Panel A. Sample**

| Item                             |                                                         Value |
| -------------------------------- | ------------------------------------------------------------: |
| Data source                      | Belgian EU-SILC matched to EUROMOD baseline tax-benefit rules |
| Unit of analysis                 |                              Prime-age childless single women |
| Age range                        |                                                         25–54 |
| Final estimation sample          |                                             3,284 individuals |
| Mean age                         |                                                          39.7 |
| Region shares                    |                Flanders 56.8%; Wallonia 30.9%; Brussels 12.3% |
| Education shares                 |                           Low 25.9%; Medium 42.5%; High 31.6% |
| Observed employment rate         |                                                         77.6% |
| Mean weekly hours, employed      |                                                          34.9 |
| Mean gross hourly wage, employed |                                                         €15.8 |
| Mean monthly disposable income   |                                                        €1,694 |

**Panel B. Institutional / modelling setup**

| Item                       | Value                                                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Labour-supply alternatives | 16 packages                                                                                                                                  |
| Package definition         | Non-employment + 5 hours bins × 3 wage terciles                                                                                              |
| Hours bins                 | 1–15, 16–24, 25–34, 35–44, 45+                                                                                                               |
| Opportunity heterogeneity  | Region × education                                                                                                                           |
| Preference heterogeneity   | 2 latent taste types + age and age² shifters                                                                                                 |
| Welfare object             | Opportunity-sensitive money-metric welfare, expressed as equivalent monthly disposable income at the non-employment / full-leisure reference |
| Baseline inequality index  | Gini of welfare                                                                                                                              |
| Decomposition rule         | Two-factor Shapley-Shorrocks decomposition                                                                                                   |
| Decomposition factors      | Opportunity heterogeneity; preference heterogeneity                                                                                          |
| Baseline comparison object | Belgian status quo tax-benefit system                                                                                                        |

## 2. TABLE 2 — Estimated preference parameters

Table 2 reports the simulated maximum-likelihood estimates for the preference block. The specification uses log disposable income, log leisure, age shifters on the leisure coefficient, a work fixed cost, and a two-type latent class structure.

| Parameter                           |  Estimate |  S.E. |
| ----------------------------------- | --------: | ----: |
| Log disposable income               |  2.946*** | 0.188 |
| Log leisure, Type 1                 |  1.428*** | 0.116 |
| Type 2 shift in leisure coefficient |  0.612*** | 0.141 |
| Age/10 × log leisure                |  0.084*** | 0.029 |
| (Age/10)² × log leisure             | -0.010*** | 0.003 |
| Work fixed cost                     | -1.324*** | 0.182 |
| Latent Type 2 logit intercept       | -0.447*** | 0.118 |
| Implied Type 2 population share     |  0.390*** | 0.028 |

**Notes.** Type 2 is the more leisure-oriented class. The implied leisure coefficient is 1.43 for Type 1 and 2.04 for Type 2. The age pattern is concave: the marginal value of leisure rises with age within the prime-age window, but at a decreasing rate. Standard errors in parentheses. *** (p<0.01), ** (p<0.05), * (p<0.10).

## 3. TABLE 3 — Estimated opportunity / job availability mechanism

Table 3 reports the opportunity block. Panel A gives the log total job-offer intensity relative to the reference cell of medium-educated women in Flanders. Panel B gives the composition of offered jobs by hours and wage package, conditional on market access.

**Panel A. Log total job-offer intensity ( \ln q_i )**

| Parameter                 |  Estimate |  S.E. |
| ------------------------- | --------: | ----: |
| Wallonia                  |  -0.150** | 0.061 |
| Brussels                  | -0.192*** | 0.071 |
| Low education             |  -0.108** | 0.051 |
| High education            |   0.151** | 0.062 |
| Wallonia × Low education  |   -0.109* | 0.060 |
| Wallonia × High education |     0.011 | 0.071 |
| Brussels × Low education  |   -0.126* | 0.071 |
| Brussels × High education |     0.031 | 0.079 |

**Panel B. Composition of offered job packages**
Reference categories: 1–15 hours; low-wage tercile.

| Parameter           |  Estimate |  S.E. |
| ------------------- | --------: | ----: |
| 16–24 hours         |  0.214*** | 0.053 |
| 25–34 hours         |  0.548*** | 0.061 |
| 35–44 hours         |  1.012*** | 0.069 |
| 45+ hours           |  0.392*** | 0.079 |
| Middle wage tercile |   0.094** | 0.041 |
| Top wage tercile    | -0.181*** | 0.051 |

**Panel C. Implied relative total offer intensity by region × education**
Reference cell: Flanders / Medium education = 1.00

|                  | Flanders | Wallonia | Brussels |
| ---------------- | -------: | -------: | -------: |
| Low education    |     0.90 |     0.69 |     0.65 |
| Medium education |     1.00 |     0.86 |     0.83 |
| High education   |     1.16 |     1.01 |     0.99 |

**Interpretation.** The opportunity mechanism delivers three finished-paper style results: standard-hours jobs are much more prevalent than fringe-hours jobs; top-wage packages are relatively scarcer on average; and total market access is sharply stratified by region × education, with the lowest offer intensity in low-education cells outside Flanders.

## 4. TABLE 4 — Model fit / observed vs predicted behavior

The full opportunity-sensitive model fits materially better than a common-choice-set benchmark and reproduces both the overall participation margin and the systematic region × education gradients in employment.

**Panel A. Goodness of fit**

| Statistic                                     |    Value |
| --------------------------------------------- | -------: |
| Log-likelihood                                | -4,786.2 |
| McFadden pseudo-(R^2)                         |    0.271 |
| Exact 1-of-16 package hit rate                |    39.2% |
| Employment classification hit rate            |    82.4% |
| Hours-bin hit rate, conditional on employment |    64.8% |
| Common-choice-set benchmark pseudo-(R^2)      |    0.214 |
| Common-choice-set benchmark exact hit rate    |    33.8% |

**Panel B. Employment rate by region × education, observed vs predicted**

|                             | Observed | Predicted |
| --------------------------- | -------: | --------: |
| Flanders / Low education    |    72.4% |     73.0% |
| Flanders / Medium education |    79.3% |     78.9% |
| Flanders / High education   |    86.5% |     85.9% |
| Wallonia / Low education    |    64.0% |     64.8% |
| Wallonia / Medium education |    73.6% |     74.0% |
| Wallonia / High education   |    83.8% |     83.0% |
| Brussels / Low education    |    62.4% |     63.5% |
| Brussels / Medium education |    71.2% |     72.0% |
| Brussels / High education   |    82.4% |     81.7% |

**Interpretation.** The main fit gain comes from recovering the strong cross-cell heterogeneity in market attachment. The benchmark without explicit opportunity heterogeneity compresses these gradients too much; the full model does not.

## 5. TABLE 5 — Welfare inequality and decomposition results

Table 5 reports the paper’s central result: welfare inequality exceeds disposable-income inequality once constrained opportunities are built into the welfare object, and the decomposition assigns a substantial but not dominant role to opportunities.

**Panel A. Welfare distribution summary**

| Statistic                          |  Value |
| ---------------------------------- | -----: |
| Mean monthly welfare               | €1,718 |
| Median monthly welfare             | €1,681 |
| 10th percentile                    | €1,079 |
| 90th percentile                    | €2,452 |
| Disposable-income Gini             |  0.164 |
| Opportunity-sensitive welfare Gini |  0.186 |

**Panel B. Counterfactual inequality and Shapley decomposition**

| Scenario / Component  | Welfare Gini | Reduction vs. baseline |
| --------------------- | -----------: | ---------------------: |
| Baseline              |        0.186 |                      — |
| Opportunity equalized |        0.151 |                 -0.035 |
| Preference equalized  |        0.140 |                 -0.046 |
| Both equalized        |        0.097 |                 -0.089 |

| Shapley component                                  | Absolute contribution | Share of explained reduction | Share of baseline Gini |
| -------------------------------------------------- | --------------------: | ---------------------------: | ---------------------: |
| Opportunity heterogeneity                          |                 0.039 |                        43.8% |                  21.0% |
| Preference heterogeneity                           |                 0.050 |                        56.2% |                  26.9% |
| Residual/common component after both equalizations |                 0.097 |                            — |                  52.2% |

**Interpretation.** The central mature-paper message is clear: opportunities explain a quantitatively important share of welfare inequality, but preferences still explain slightly more. That is exactly the balance needed for the paper’s contribution to look structural rather than rhetorical.

## 6. TABLE 6 — Sensitivity to responsibility for opportunities

Table 6 varies the normative definition of which opportunity differences are compensation-relevant. The baseline treats the full region × education opportunity gradient as non-responsibility-relevant. The two alternative rows impose stricter responsibility stances by compensating only one of the two dimensions.

| Compensable opportunity definition | Opportunity-equalized Gini | Both-equalized Gini | Shapley opportunity component | Opportunity share of explained reduction | Opportunity share of baseline Gini |
| ---------------------------------- | -------------------------: | ------------------: | ----------------------------: | ---------------------------------------: | ---------------------------------: |
| Region × education (baseline)      |                      0.151 |               0.097 |                         0.039 |                                    43.8% |                              21.0% |
| Education only                     |                      0.158 |               0.105 |                         0.031 |                                    38.9% |                              16.7% |
| Region only                        |                      0.164 |               0.110 |                         0.026 |                                    34.2% |                              14.0% |

**Interpretation.** Tightening responsibility for opportunities reduces the compensable opportunity share, as it should, but does not eliminate it. Even under the strictest stance here, unequal opportunities still account for about one-seventh of baseline welfare inequality.

## 7. FIGURE 1 — Distribution / fit figure

**Recommended figure.** Side-by-side bars for observed and predicted shares across labour-supply states.

| Labour-supply state | Observed share | Predicted share |
| ------------------- | -------------: | --------------: |
| Non-employment      |          22.4% |           22.1% |
| 1–15 hours          |           6.1% |            6.3% |
| 16–24 hours         |           8.5% |            8.6% |
| 25–34 hours         |          13.7% |           13.4% |
| 35–44 hours         |          38.6% |           38.4% |
| 45+ hours           |          10.7% |           11.2% |

**Caption.** The model closely reproduces the non-employment margin and the strong concentration of work in standard-hours packages, with only a mild overprediction at 45+ hours.

## 8. FIGURE 2 — Decomposition shares

**Recommended figure.** A stacked bar for the baseline welfare Gini, decomposed into the residual/common component and the two Shapley contributions.

| Segment                                            | Value |
| -------------------------------------------------- | ----: |
| Residual/common component after both equalizations | 0.097 |
| Opportunity component                              | 0.039 |
| Preference component                               | 0.050 |
| Baseline welfare Gini                              | 0.186 |

**Optional annotation for the slide.**

* Opportunity share of explained component: **43.8%**
* Preference share of explained component: **56.2%**

**Caption.** Roughly half of baseline welfare inequality remains after equalizing both opportunities and preferences; of the explainable component, opportunities account for just under forty-four percent.

## 9. FIGURE 3 — Responsibility sensitivity figure

**Recommended figure.** Three bars showing the compensable opportunity component under alternative responsibility stances.

| Opportunity stance            | Shapley opportunity component | Share of baseline Gini |
| ----------------------------- | ----------------------------: | ---------------------: |
| Compensate region × education |                         0.039 |                  21.0% |
| Compensate education only     |                         0.031 |                  16.7% |
| Compensate region only        |                         0.026 |                  14.0% |

**Caption.** The opportunity contribution declines as more of the opportunity gradient is treated as responsibility-relevant, but it remains economically significant throughout.

## 10. MAIN TAKEAWAYS

1. The structural model looks like a completed paper rather than a prototype: the preference block is well-behaved, the opportunity block is sharply identified in economically sensible directions, and the fit gains over a common-choice-set benchmark are material.

2. The opportunity mechanism is substantively meaningful. Standard-hours packages are much more available than fringe-hour packages, and total access to jobs is strongly stratified by region × education, with the weakest access in low-education cells outside Flanders.

3. Welfare inequality is larger than disposable-income inequality once the welfare object is made opportunity-sensitive. In these mock results, the welfare Gini is **0.186**, compared with an income Gini of **0.164**.

4. The decomposition delivers the paper’s core contribution. Opportunity heterogeneity accounts for **0.039** Gini points, or **43.8% of the explained component** of welfare inequality, while preference heterogeneity accounts for **0.050** Gini points. Opportunities matter a great deal, but they do not swamp preferences.

5. The result is normatively robust. When the responsibility stance is tightened, the compensable opportunity share falls from **21.0%** to between **14.0%** and **16.7%** of baseline welfare inequality, but it remains too large to dismiss. This supports the paper’s main hiring-committee message: **decomposition is more informative than ranking, and unequal opportunities materially shape welfare inequality in a latent-jobs labour-supply framework.**
