Here are the answers, drawn entirely from your project knowledge files including the correction note.

---

**1. What is the current main JMP question?**

How much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than heterogeneous preferences, once labor supply is modeled as discrete choice over latent job packages and welfare is evaluated under constrained feasible sets? The central object is the decomposition of the household welfare distribution, not a ranking or a reform simulation.

**2. What is the current empirical baseline?**

France 2016, SRCV / EUROMOD-input cross-section, household couples sample, RURO estimation with sampled latent alternatives and EUROMOD-computed disposable income. The current best empirical specification is `estimation_spec_job_M2h_pruned`, which uses a job-choice architecture (wage vigintile × hours bin × ISCO/type) and shows the most stable Hessian diagnostics. France 2021 is available for later robustness.

**3. What is the sample-size wording to use carefully?**

The correction note is explicit: **do not describe 4,253 as the couples-only sample.** The correct breakdown from the France 2016 processed MNL files is approximately 1,676 singles and 2,577 couples, totaling 4,253 groups/households across both. If you are describing the couples baseline, use ~2,577, not 4,253. Using 4,253 as the couples count is a factual error.

**4. What is the difference between the long-run empirical output and the immediate technical next step?**

The **long-run JMP objective** is one stable baseline decomposition table and one baseline figure showing the Shapley-Shorrocks split of the household welfare Gini into opportunity and preference components. That is the signature result of the paper.

The **immediate technical next step** is something different and more preliminary: write a RURO model-specification contract from the literature and technical memos; audit the current code against that contract; patch only the mismatches that affect likelihood interpretation, prior correction, normalization, or the preference/opportunity separation; run simulation recovery and stability tests; and only then proceed to welfare computation and decomposition. Jumping from "pipeline runs" to "decomposition table" without this intermediate step would produce results that are not yet reliably interpretable.

**5. Why is it not yet enough to jump directly to welfare decomposition?**

Because the France RURO estimation is not yet fully stabilized. Specifically: the continuous RURO specifications have weak or indefinite Hessian diagnostics and do not yet support a strong identification claim; the job-choice M2h pruned model has better diagnostics but is still provisional; simulation recovery tests against known true parameters have not yet been run; stability across seeds, draw counts, and starting values is incomplete; and some prior/proposal correction code paths still need cleanup. Decomposing a welfare Gini that rests on an unstable or misspecified likelihood would not be credible or reportable. The identification gates must be passed first.

**6. What is the role of the Stijn-style opportunity-layer redesign?**

Stijn's model structures the choice index additively as `U + O_time + O_wage − log q`, with separate named layers for preference utility, hours opportunity, and wage opportunity. The current France job-choice model already has the right architecture conceptually, but the sector/occupation availability is embedded inside the job bundle (`q_job`) rather than exposed as a transparent, separately-estimated opportunity layer. The Stijn-style redesign would make the factorization explicit:

```
V = U + O_employment + O_sector/occupation + O_hours + O_wage − log q
```

This matters because the decomposition of welfare inequality into opportunity and preference components requires that the opportunity components be cleanly separated in the likelihood and in the prior correction. Until they are, the opportunity share in the decomposition is not unambiguously identified. The redesign is therefore not cosmetic — it is a prerequisite for making the decomposition interpretable.

**7. Why should ISCO/LOC be called occupation opportunity rather than true sector opportunity?**

Because ISCO codes classify **occupations** (what work people do), while NACE codes classify **industries or sectors** (what sector the employer belongs to). The project files note that the current final MNL files contain `isco1`, `loc`, `loc4`, and `type_id`, but **do not currently expose a NACE/sector variable**. Calling ISCO-based availability "sector opportunity" would be a mislabeling that confuses occupation access with industry-demand access. The correct terminology is **occupation opportunity**. True sector opportunity (in the industry/labor-demand sense) would require NACE or an equivalent industry code to be carried through the data pipeline from raw SRCV through draws, EUROMOD, and MNL construction — work that has not yet been done.

**8. What should Claude Code do next?**

Per the correction note and the technical memos, the correct Claude Code sequence is:

1. **Write a RURO model-specification contract** — a formal document defining the intended structure of the likelihood (preference utility, hours opportunity, wage opportunity, optional occupation opportunity, prior/proposal correction, normalization) derived from the Stijn reference files and the technical memos.
2. **Audit the current code against that contract** — check that `estimation_engine.py`, `gamspy_estimation_vectorized.py`, and `enh_RURO_prep_mnl_basic.py` implement each component as specified, and identify mismatches in prior correction, centering, or opportunity/preference separation.
3. **Patch only the mismatches** that affect likelihood interpretation — not a full rewrite.
4. **Run recovery and stability tests** — simulate data with known parameters and verify the estimator recovers them.
5. **Only then** proceed to welfare computation and the decomposition.

Claude Code should not start by implementing welfare or decomposition code. The model layer must be verified first.

---

**Memory corrected.**

The previous memory test was mostly right but had one factual error that the correction note explicitly flags: it described 4,253 as the couples-only sample count, when 4,253 is the combined singles + couples total. The correct couples count is ~2,577. Additionally, the previous answer described the "next empirical step" as producing the decomposition table, without adequately foregrounding the prior technical step of model-specification contracting, code auditing, and recovery testing. The correction note makes that sequencing explicit, and the Stijn comparison documents and identification audit files confirm it. Both points are now corrected in these answers.