Below is a fully revised extended abstract aligned with the **actual France RURO implementation**, correcting the Belgium mismatch, tightening the contribution logic, and keeping the empirical claims disciplined.

---

# **Opportunity Constraints as a Driver of Welfare Inequality: A Latent-Jobs Structural Decomposition Approach**

## **1. Motivation**

Structural labor-supply models are widely used to estimate preferences and evaluate policy. However, the standard framework assumes that individuals choose labor supply from a common budget set, typically represented as a continuous or discretized hours choice. In practice, individuals choose among jobs, and the set of feasible job opportunities differs across individuals. Once this is recognized, observed inequality in labor-market outcomes becomes normatively ambiguous: identical observed bundles may reflect unconstrained choice for some individuals and constrained second-best outcomes for others.

If opportunity heterogeneity is not modeled explicitly, structural models tend to absorb it into preference heterogeneity. This conflation affects both behavioral interpretation and welfare analysis. The project is motivated by the need to treat **opportunities as a first-class object** in empirical labor-supply modeling and to quantify their role in generating welfare inequality.

## **2. Main research question**

The paper asks: **how much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than to heterogeneous preferences**, once labor supply is modeled as discrete choice among latent job packages and welfare is evaluated conditional on constrained feasible sets.

Equivalently, the empirical question is whether standard structural labor-supply models overstate preference heterogeneity because unequal access to jobs is left implicit, and whether this matters quantitatively for welfare inequality.

## **3. Literature gap**

The project lies at the intersection of four literatures: constrained structural labor supply, latent jobs and restricted choices, empirical welfare analysis for discrete choice, and inequality-of-opportunity measurement. Each strand is well developed in isolation, but they have not been integrated into a single empirical pipeline.

Existing structural labor-supply studies incorporate constraints but typically treat welfare evaluation as the endpoint and the opportunity structure as background. Welfare-comparison papers emphasize heterogeneous preferences but do not model opportunity sets explicitly. Inequality-of-opportunity approaches focus on circumstance-based decompositions but lack a structural behavioral foundation.

The missing element is a **structural decomposition of welfare inequality** in which opportunities are estimated, carried into welfare measurement, and then attributed quantitatively.

## **4. Core mechanism: opportunities versus preferences**

The framework separates two objects. Preferences determine how individuals rank consumption–leisure bundles conditional on available jobs. The opportunity mechanism determines which job packages are feasible and how their distribution varies across observable circumstances.

If the opportunity mechanism is omitted, constrained outcomes are mechanically reinterpreted as preferences. This creates an identification problem and a normative distortion. The paper therefore models opportunities explicitly and treats them consistently across all stages.

The normative interpretation is limited but clear: unequal opportunities are treated as **compensation-relevant circumstances**, while preference heterogeneity is not allowed to absorb constraints by construction. This interpretation remains embedded in an empirical framework and does not rely on the separate axiomatic theory project.

## **5. France empirical setting**

The empirical application is a **France-based structural model** estimated on SRCV / EUROMOD-input microdata, with 2016 as the primary estimation year. The model is implemented on a **household/couples sample**, where both spouses’ labor supply decisions enter a joint utility function.

Labor supply is modeled as choice among **latent job packages**, defined by discrete wage–hours opportunities. Disposable income for each job package is computed using EUROMOD under the French tax-benefit system. Microsimulation is therefore used to map job packages into budget constraints, not to estimate behavior.

The empirical setting reflects an already implemented RURO pipeline, including sampled job alternatives, a structural likelihood, and a welfare layer under development. At the same time, estimation stability and normalization remain active issues, so the empirical claims are framed as disciplined measurement rather than finalized results. 

## **6. Empirical strategy**

The empirical strategy is a single-country structural application with three estimated components. First, preferences over consumption and leisure are estimated using a flexible utility specification at the household level. Second, an **opportunity mechanism** is estimated, capturing the distribution of feasible job packages across individuals as a function of observable circumstances such as region and education. Third, job packages are evaluated through EUROMOD to obtain disposable income.

Formally, individuals choose among sampled alternatives with utility depending on consumption and leisure, while the probability of each alternative reflects both utility and its availability. Estimation proceeds by maximum likelihood, jointly identifying preference parameters and opportunity parameters under standard RURO assumptions. 

The empirical output is not a full policy simulation, but a set of objects sufficient to support decomposition: estimated preferences, an estimated opportunity distribution, and a welfare mapping.

## **7. Welfare object**

The welfare object is a **money-metric measure defined conditional on constrained feasible sets**. In the baseline prototype, welfare is computed at the household level using an AEI-style measure relative to a joint non-work reference state.

This construction ensures that welfare comparisons respect both consumption and leisure, while remaining consistent with the estimated opportunity set. It also maintains a clear separation between behavioral utility and the welfare metric, avoiding the direct use of estimated utility as an interpersonal welfare measure.

## **8. Decomposition strategy**

Decomposition is the central object of the paper. The approach compares baseline welfare inequality with counterfactual distributions obtained by:

* equalizing the opportunity mechanism across circumstance groups,
* neutralizing preference heterogeneity,
* and applying both adjustments jointly.

An order-independent **Shapley-Shorrocks decomposition** is then used to attribute welfare inequality to opportunity heterogeneity and preference heterogeneity.

This is a stronger contribution than a welfare ranking. A ranking describes levels; a decomposition identifies **mechanisms**. The paper’s objective is therefore to quantify the role of opportunities as a driver of welfare inequality, not to produce a new ranking of individuals or countries.

## **9. Expected contribution**

The contribution is threefold.

First, it advances constrained structural labor-supply estimation by explicitly modeling job opportunities rather than treating all heterogeneity as preferences.

Second, it contributes to empirical welfare analysis by constructing a money-metric welfare object consistent with constrained opportunities.

Third, it contributes to inequality analysis by making decomposition, rather than ranking or reform incidence, the central empirical object.

The key novelty is the integration of these elements into a single empirical pipeline. Opportunities are estimated, carried into welfare evaluation, and then decomposed, rather than being treated as an auxiliary modeling feature.

## **10. Main risk and identification challenge**

The main challenge is identification. Preferences and opportunities are jointly determined in observed choices, and separating them requires structural assumptions. In the current France implementation, estimation stability and normalization remain nontrivial issues, and the opportunity mechanism is only partially disciplined.

There are also internal consistency challenges in sample construction and wage modeling, and the welfare layer requires further refinement. These issues do not invalidate the project, but they constrain the strength of empirical claims.

The strategy is therefore to keep the first version **parsimonious and transparent**, focusing on a minimal opportunity structure and a small number of decomposition exercises.

## **11. First empirical prototype**

The first empirical prototype is a **France 2016 couples application** using the implemented RURO pipeline. Job packages are represented by sampled discrete wage–hours opportunities, and opportunity heterogeneity varies across region × education groups.

The first output is a single decomposition table reporting:

* baseline welfare inequality,
* inequality under opportunity equalization,
* inequality under preference neutralization,
* and the corresponding Shapley decomposition shares.

A single figure presents the decomposition as a stacked contribution of opportunities and preferences.

The purpose of this prototype is not to deliver definitive quantitative results, but to establish whether the opportunity component of welfare inequality is **empirically meaningful and robust**. If that condition is met, the project’s direction is validated as a job market paper.

---
