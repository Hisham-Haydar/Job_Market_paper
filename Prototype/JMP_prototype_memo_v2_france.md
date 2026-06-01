### 1. Preferred empirical setting

The baseline prototype should be written as a **France 2016** structural labor-supply application using **SRCV / EUROMOD-input microdata**, estimated in a RURO / latent-jobs framework on the **couples sample**. This is now the correct empirical anchor. France is the primary estimation setting in the current pipeline; 2021 can appear later as a robustness year, and Germany should remain only a diagnostic benchmark rather than part of the JMP’s headline design.   

### 2. Unit of analysis

The unit of analysis should be the **household/couple**, not the single individual. The implemented France sample is household-based, and the current couples model is a joint unitary job-choice model in which household disposable income and both spouses’ leisure enter the utility function. For that reason, the first decomposition should be conducted over **household welfare levels**, even though opportunities are modeled at the spouse-specific job-offer level inside the structural system.  

### 3. Sample restrictions

Use the currently implemented France couples filter: opposite-sex couples; head and partner both aged 16–65; both out of full-time education; replacement income no greater than 100 euros per month; unemployed individuals excluded under the current eligibility rule (`les != 5`); self-employment excluded; households with additional labour-market-eligible non-head, non-partner members dropped; and abnormal employee hours or wages filtered out. For writing purposes, this current rule should be treated as the baseline even though earlier France code versions were not fully consistent on unemployment treatment.  

### 4. Why this sample is the right first prototype

This is the right first prototype not because it is the simplest imaginable sample, but because it is the **most aligned with the real France implementation**. The France pipeline is already built around this household/couples structure, with approximately 4,253 couples documented before final filtering, and it is much more credible to write from the actual implemented sample than to keep relying on the obsolete Belgium/single-woman fallback. It is also safer than making singles the new baseline, because the current France singles estimations are precisely where the most visible pathological estimates have already appeared.   

### 5. Minimal job-package definition

The minimal job-package definition should be the **basic `job` representation** already embedded in the France hierarchy: each spouse’s market alternative is a **wage-vigintile × 4-hour-interval** package, plus the non-work option `j_0`. At the household level, an alternative is therefore a **joint bundle of head and partner job packages**. This is narrow enough for a first decomposition table while remaining faithful to the actual implementation. Occupation- and industry-augmented identifiers (`jobloc`, `joblind`, `jobtot`) should be postponed to robustness work, while the sampled-alternative engine should remain as currently coded rather than being replaced by an artificial 16-cell fixed grid.   

### 6. Circumstances used for opportunity heterogeneity

For the first prototype, the opportunity counterfactual should use **spouse-specific region × education cells** as the circumstance partition. This is the cleanest way to keep the decomposition economically interpretable and consistent with the project’s within-country opportunity logic. Richer variables such as experience, sector, or the `gsur` component may remain inside the opportunity density where already useful for estimation, but they should not define the headline decomposition groups in the first table. The XGBoost ability-set construction should not be the baseline opportunity object for writing purposes, because its current performance is weak and it conflates ability with local availability.   

### 7. Preference heterogeneity structure

The baseline preference structure should follow the **implemented Box-Cox couples utility**, not the older prototype’s latent-type simplification. Concretely, use a common consumption term, spouse-specific leisure terms, and a leisure–leisure interaction term, with only **parsimonious observed heterogeneity** in leisure tastes through already prepared demographic shifters in the spouse-specific (X) vectors. Do **not** introduce latent taste classes in the first France writing prototype. That would add another layer of instability at exactly the stage where the France RURO system still needs normalization and convergence discipline.   

### 8. Welfare object

The welfare object should be a **household-level AEI-style money-metric measure** implied by the implemented couples utility and its non-work normalization. Operationally, the first prototype should evaluate each couple relative to a **joint non-work reference state**, using the AEI logic already designated as the primary welfare measure in the current programme. Measure 2 with reference preferences should be kept as a robustness exercise, not as the headline object. This keeps the JMP empirical and structural while remaining distinct from the separate theory paper. At the same time, the memo should remain honest that the exact non-work reference implementation is not yet fully closed in the France pipeline.   

### 9. Inequality index

The baseline inequality index should be the **Gini coefficient of household AEI**. This is the cleanest first-pass index because it is easy to communicate, already fits the older prototype logic, and is fully compatible with the order-independent decomposition plan. Atkinson or alternative welfare-inequality indices can be added only after the France baseline table exists.  

### 10. Decomposition rule

The first prototype should use a **two-factor Shapley-Shorrocks decomposition** of the household-welfare Gini. The two factors are: first, **opportunity heterogeneity**, implemented by equalizing spouse-specific opportunity distributions across region × education cells; second, **preference heterogeneity**, implemented by replacing household-specific taste shifters with a pooled reference specification. Any interaction between the two should be absorbed by the order-independent Shapley allocation rather than reported as a separate headline component in the first table. That is the most disciplined and feasible decomposition rule for the France prototype at this stage.   

### 11. First table

Table 1 should be a **France 2016 couples prototype table** with the following core columns: baseline household welfare Gini; welfare Gini after opportunity equalization; welfare Gini after preference neutralization; welfare Gini after both equalizations; Shapley share attributed to opportunities; and Shapley share attributed to preferences. That table is enough to make the decomposition contribution visible without pretending that the France estimation layer is already fully mature.  

### 12. First figure

Figure 1 should be a **single stacked bar** showing the Shapley decomposition of baseline household welfare inequality into an **opportunity component** and a **preference component** for the France 2016 couples sample. Do not use multiple figures in the main text yet. Sensitivity to alternative circumstance definitions, alternative welfare measures, or richer job-package definitions should go later, once the baseline France result exists.  

### 13. Main empirical risk

The main empirical risk is not generic “identification” in the abstract; it is the current **France-specific instability of the estimated structural system**. Three issues matter most. First, the France RURO runs still show normalization and convergence problems, including pathological coefficients and large gradient norms. Second, the pipeline is not yet fully internally consistent on sample definition and wage construction, especially regarding unemployment treatment and the mismatch between the `yem > 100` and `yem > 500` thresholds. Third, the opportunity and welfare layers are not fully locked: the role of `gsur` remains open, the XGBoost ability-set route is weak, and the AEI reference non-work implementation still needs tightening. Unless those issues are stabilized, the decomposition could look mechanical rather than substantive.   

### 14. What I need to code first

First, freeze the **France 2016 couples estimation sample** with one definitive labour-market eligibility rule and one definitive household filter. Second, lock the **France data-year / EUROMOD system-year pairing** for the prototype so the writing and code refer to the same empirical object. Third, freeze the baseline **basic `job` representation** and the sampled-alternative settings, keeping the richer job hierarchy out of the first decomposition pass. Fourth, rerun the **couples RURO estimation** under the chosen normalization and keep gradient diagnostics explicit before treating any coefficients as usable. Fifth, implement the **household AEI calculation** under the joint non-work reference state. Sixth, code the **region × education opportunity equalization** and the **reference-preference neutralization**. Seventh, compute the **household AEI Gini** and the **two-factor Shapley decomposition**, then produce one table and one figure. Only after that should you add richer opportunity groupings, `jobloc`/`jobtot`, or alternative welfare measures.    

Save this as `JMP_prototype_memo_FR_v2.md` and treat it as a prototype memo.
