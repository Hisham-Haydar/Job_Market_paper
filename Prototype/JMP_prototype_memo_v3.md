Save this as a working memo: `JMP_prototype_memo_v3_scope.md`.

## 1. Preferred empirical setting

The baseline remains **France 2016 couples**, estimated on **SRCV / EUROMOD-input microdata** in a **RURO / latent-jobs** framework. This is a deliberate scope choice, not a default inherited from an older memo. It remains the strongest first prototype because it is the only scope for which the documented sample, utility specification, welfare object, and decomposition design already line up cleanly for a first empirical result. **France 2021 couples** is the first extension, **France singles** come only after that as separate models, and **Germany** remains a later replication benchmark rather than part of the baseline.  

## 2. Unit of analysis

The unit of analysis is the **household/couple**. The behavioral model is a joint couples model in which household disposable income and both spouses’ leisure enter utility, so the first decomposition must be conducted over **household welfare levels**, even though opportunities are represented through spouse-specific job packages inside the structural system.  

## 3. Sample restrictions

Use the currently implemented France couples filter as the baseline sample: **opposite-sex couples**; head and partner both aged **16–65**; both outside full-time education; **self-employment excluded**; households with additional labour-market-eligible non-head, non-partner members dropped; abnormal employee hours or wages filtered out; and the current labour-market eligibility rule kept fixed for the baseline run. The point of the first prototype is not to perfect every margin of sample design, but to freeze one coherent France 2016 couples sample and run the first decomposition on it.  

## 4. Why this is the right first prototype

This is the right first prototype because it is the **shortest path to a stable decomposition result** while still being fully aligned with the real France implementation. The broader assets you already have—2021, singles, Germany, and a near-working RURO pipeline—are real, but they do not improve the next 2–4 weeks if they are moved into the baseline. The current memos are explicit that the France singles side is where visible pathologies have appeared, while 2021 is already a natural next robustness step and Germany is still framed as auxiliary. So the first task is not maximum empirical breadth; it is one credible France 2016 couples decomposition result that locks the paper’s core empirical identity.  

## 5. Minimal job-package definition

The minimal job-package definition is the **basic `job` representation** already implemented in the France pipeline. For each spouse, the non-work option is combined with market alternatives defined as **wage vigintile × 4-hour interval** job packages, sampled from the latent opportunity distribution. At the household level, the relevant alternative is therefore a **joint bundle of head and partner job packages**. Richer job hierarchies such as `jobloc`, `joblind`, and `jobtot` are explicitly postponed until after the first baseline decomposition table exists.  

## 6. Circumstances used for opportunity heterogeneity

The baseline circumstance partition is **spouse-specific region × education**. This is narrow enough to keep the decomposition interpretable and feasible, while still matching the within-country opportunity logic of the paper. Richer variables may remain inside the opportunity density where useful for estimation, but they should not define the headline decomposition groups in version 1. In particular, the ability-set route and richer availability constructions are postponed because they are not yet stable enough to serve as the baseline opportunity object.  

## 7. Preference heterogeneity structure

The baseline preference structure is the **implemented Box-Cox couples utility**. It includes a common consumption term, spouse-specific leisure terms, and a leisure–leisure interaction term, with only **parsimonious observed heterogeneity** through the already prepared demographic shifters. The first prototype should **not** introduce latent taste classes or other richer preference heterogeneity structures. That would add complexity at exactly the point where the France couples system still needs stabilization and clean diagnostics.  

## 8. Welfare object

The welfare object is **household AEI-style money-metric welfare** evaluated relative to a **joint non-work reference state**. This is the right baseline because it is already the leading welfare object in the current France design and because it keeps the paper empirical and structural rather than pushing it toward the separate theory paper on axiomatic well-being measurement. The alternative reference-preference welfare measure remains a robustness exercise for later versions, not the headline object of the first prototype.   

## 9. Inequality index

The baseline inequality index is the **Gini coefficient of household AEI**. This is the cleanest first-pass inequality object because it is easy to interpret, already embedded in the current France prototype logic, and fully compatible with the planned order-independent decomposition. Alternative welfare-inequality indices can be added only after the France 2016 couples baseline is in hand.  

## 10. Decomposition rule

The baseline decomposition is a **two-factor Shapley-Shorrocks decomposition** of the **household welfare Gini**. The two factors are: **opportunity heterogeneity**, implemented by equalizing spouse-specific opportunity distributions across region × education cells; and **preference heterogeneity**, implemented by replacing household-specific taste shifters with a pooled reference specification. Any interaction between the two is absorbed by the Shapley allocation rather than treated as a separate headline component. This keeps decomposition central and prevents the paper from drifting into a simple welfare-ranking exercise.  

## 11. First table

**Table 1** should be the **France 2016 couples prototype decomposition table**. Its core entries should be: baseline household welfare Gini; household welfare Gini after opportunity equalization; household welfare Gini after preference neutralization; household welfare Gini after both equalizations; Shapley share attributed to opportunity heterogeneity; and Shapley share attributed to preference heterogeneity. This is the first non-negotiable empirical object because it makes the paper’s contribution visible in one place.  

## 12. First figure

**Figure 1** should be a **single stacked bar** showing the Shapley decomposition of the **France 2016 household welfare Gini** into an **opportunity component** and a **preference component**. No richer visual program is needed in the first pass. Sensitivity figures for alternative circumstance definitions, richer job-package definitions, or alternative welfare measures should be postponed until after the baseline France result exists.  

## 13. Main empirical risk

The main empirical risk is the current **France-specific instability of the structural system**, not a generic abstract identification problem. The key risks are: normalization and convergence problems in the France RURO estimation; unresolved internal consistency issues in sample construction and wage treatment; and a welfare/opportunity layer that is implemented but not yet fully locked. If those issues are not stabilized, the first decomposition may look mechanical rather than substantive. This is precisely why the baseline must remain narrow and why wider scope should be treated as staged extensions rather than immediate baseline enlargement.   

## 14. What I need to code first

First, freeze the **France 2016 couples estimation sample** under one definitive household filter and one definitive labour-market eligibility rule. Second, lock the **France data-year / EUROMOD system-year pairing** so that the code and the writing refer to the same empirical object. Third, freeze the **basic `job` representation** and the sampled-alternative settings, keeping richer job hierarchies out of the first pass. Fourth, rerun the **couples RURO estimation** under the chosen normalization and keep the convergence diagnostics explicit. Fifth, implement the **household AEI calculation** under the joint non-work reference state. Sixth, code the **region × education opportunity equalization** and the **reference-preference neutralization**. Seventh, compute the **household AEI Gini** and the **two-factor Shapley decomposition**, and produce the one baseline table and one baseline figure. Only after that result exists should the scope widen, in this order: **France 2021 couples**, then **France singles as separate extensions**, then **Germany replication**.   
