DEPUTY -> GOAL 1 — FINAL-DIAGNOSTIC-SURFACE-1

This is a bounded correction to the existing seminar package.

No new welfare design.
No new decomposition design.
No broad specification search before the seminar.

==================================================

1. RAW LES 3/5/7 — MUST FIX
   ==================================================

The current canonical notebook reports zero unemployed coupled men and
zero unemployed coupled women.

This is NOT accepted as evidence.

The prior coding audit established that couples-frame les_m/les_f are derived
3/7 participation states and therefore erase raw LES=5.

Rebuild the LES diagnostic by joining the FINAL accepted household samples
back to the untouched person-level source LES.

Independently reverify:

```
dgn = 1 -> male
dgn = 0 -> female
```

and source labels:

```
LES 3 = employee
LES 5 = unemployed
LES 7 = inactive / out of labour market.
```

Produce for:

* single men;
* single women;
* men in couples;
* women in couples.

Figure A:
weighted 100% composition, LES 3 / 5 / 7.

Figure B:
conditional on nonwork only, LES 5 versus LES 7.

Return weighted shares AND unweighted counts.

Add both to:

* canonical notebook;
* JMP_results_gallery_current.html;
* concise Figure A or B to JMP_research_story_report_v5.html.

Do not state that the structural model distinguishes LES 5 from LES 7.
It currently maps both into the nonmarket/nonwork alternative.

==================================================
2. CONFUSION MATRICES — SURFACE THE ACTUAL COUNTS
=================================================

The canonical notebook already contains current predictive heatmaps.

Make the underlying matrices explicit for all four groups.

A. extensive margin:
observed work/nonwork rows × hard predicted work/nonwork columns.

B. joint hours-state:
observed state rows × modal predicted state columns, using:

NONWORK + the authoritative current hours bands.

Every cell must contain:

* raw person count;
  and provide a companion weighted matrix/table.

C. conditional intensive margin:
workers only, observed hours bin × predicted hours bin.

For every observed bin report:
N, weighted N, mean/median prediction, mean signed error, MAE,
share predicted below / inside / above the observed band.

Pair hard classification with:

* probability assigned to observed state;
* Brier/log scores;
* calibration;
* model-simulated benchmark.

Resolve the existing final POSFIT group-verdict conflict before writing a
headline claim.

==================================================
3. 50 -> 2048 NODE CONVERGENCE — MUST BE VISIBLE
================================================

These are NOT Bayesian posterior draws.

Use the technically correct label:

predictive/integration-node convergence.

For N:

50, 100, 200, 400, 800, 1200, 1600, 2048

show predicted participation for:

* single men;
* single women;
* couple men;
* couple women;

with observed participation as a horizontal reference.

If prefixes are not a valid nested integration design, use repeated
fixed-seed subsets and show a numerical envelope.

Do not call that envelope a confidence interval.

This figure was authorised previously but is not visible in the current
canonical reader notebook reviewed by Deputy.

Add it to:

* canonical notebook;
* technical gallery;
* story report only if concise enough; otherwise technical backup.

==================================================
4. LEISURE NORMALISATION / T SENSITIVITY — SURFACE IT
=====================================================

The seminar package states:

* lambda_l is a pure units normalisation;
* changing T is substantive;
* T=80 is a maintained convention to which the model is not indifferent.

Expose the actual evidence in the canonical notebook and technical gallery.

For lambda_l show:

* tested values;
* beta_l/theta_l transformation or re-estimates;
* objective/probability equivalence;
* physical marginal utility or consumption/leisure MRS at a common reference.

For T show:

* T=75, 80, 90;
* estimated leisure parameters;
* criterion/fit changes;
* active-bound status;
* comparable MUL/MRS object.

Do NOT use T=60 while the job-hours support reaches 70.

If the lambda exercise was analytical reparameterisation rather than
independent re-estimation, label it exactly as such. Do not imply an
independent estimation exercise that did not occur.

==================================================
5. CURRENT TASTE-SHIFTER DESCRIPTION
====================================

Correct any statement that the current model uses age alone.

Current systematic leisure heterogeneity includes:

all four groups:

* intercept;
* age;
* age squared;
* group-specific leisure curvature;

women:

* number-of-children leisure shifter.

Sex/household type is represented through separate parameter blocks.

Use seminar wording:

“The baseline deliberately keeps systematic preference heterogeneity
parsimonious: age profiles for all four adult groups and a child-related
shifter for women. The child term is interpreted as a reduced-form
behavioural/time-constraint shifter, not as pure taste.”

No new preference specification before the seminar.

==================================================
6. POST-SEMINAR QUEUE
=====================

Record, do not execute now:

PREF-SHIFTER-BATTERY-1

P0 current baseline.

P1 replace total-child shifter with economically meaningful child-age bands,
subject to support.

P2 allow child-age effects for men as well as women.

P3 evaluate only a small number of additional taste shifters after checking
identification/exclusion implications.

Do NOT mechanically enter education or the same rich covariate set into both
P and B/A. Education already shifts wage opportunities and unrestricted
duplication across preference/opportunity equations can weaken the structural
separation the JMP is trying to identify.

Compare future specifications on:
LL/AIC/BIC, curvature/rank, calibration and individual fit, opportunity
parameters, W1_F inequality, and DECOMP-2 contributions.

==================================================
RETURN
======

Return to Deputy:

1. corrected raw-LES table and figures;
2. verified dgn mapping and exact raw LES source lineage;
3. four extensive matrices;
4. four joint hours-state matrices;
5. intensive matrices;
6. current POSFIT final group adjudication;
7. 50->2048 node-convergence figure/table;
8. lambda/T sensitivity evidence;
9. updated canonical notebook;
10. updated technical gallery;
11. updated story report sections.

No new estimation except already-authorised T sensitivity work.
No preference-shifter model search before seminar.
