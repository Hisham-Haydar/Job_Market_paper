GOAL 1 — BAND-EDGE CROSS-SPECIFICATION CORRECTION: DEPUTY ADJUDICATION

VERDICT: ACCEPT.

Circulation remains BLOCKED until the corrected S11 predictive evaluation
and fit moments are regenerated, propagated, and audited.

The important conceptual correction is:

17.5 / 28.5 / 36.5 are not globally stale or erroneous.
They are native to the S8/R240/S12 construction.

18.5 / 29.5 / 37.5 are the relevant S10/S11 structural-band edges.

The error is that S11/S10 estimates were evaluated on S12 priced nodes while
retaining the S12-native structural-band indicators.

Treat this as a CROSS-SPECIFICATION EVALUATION ERROR.

==================================================

1. PRESERVE HISTORICAL ARTIFACTS
   ==================================================

Do NOT overwrite or mutate the original S12 panels or their native band
indicators.

Create an explicit S11-evaluation view/copy of the same priced S12 nodes.

In that evaluation view:

* keep identical household/node geometry;
* keep hours;
* keep occupations;
* keep wages;
* keep priced consumption;
* keep proposal q and all proposal-density columns;
* keep all non-band covariates unchanged;

but RECOMPUTE the structural hours-band indicator columns using the exact
S10/S11 definitions used in estimation.

Record both:

native_panel_band_definition = S12/S8
evaluation_model_band_definition = S11/S10

No historical source should be rewritten to pretend that S12 originally used
the S11 edges.

==================================================
2. RE-RUN S11 PREDICTIVE EVALUATION, NOT JUST LABELS
====================================================

Re-evaluate S11 probabilities on the corrected S11-evaluation view.

This is a full predictive reevaluation because the band indicators enter
log g and therefore affect choice probabilities.

Regenerate ALL dependent POSFIT v3 objects:

* participation probabilities;
* participation hard predictions;
* extensive-margin confusion matrices;
* hours-state probabilities;
* modal hours-state predictions;
* hours-bin confusion matrices;
* probability assigned to the observed state/bin;
* Brier scores;
* log scores;
* calibration;
* model-simulated benchmark;
* numerical-adequacy diagnostics;
* node-convergence curves;
* all four group verdict inputs.

Do not reuse old probabilities and merely relabel their bins.

Groups:

* single men;
* single women;
* coupled men;
* coupled women.

==================================================
3. NUMERICAL-ADEQUACY GATE
==========================

Reapply the existing pre-registered gate mechanically.

Coupled men previously sat at approximately 0.240 against a 0.25 threshold.

Do NOT preserve the previous classification if the corrected evaluation
crosses the threshold.

Return for each group:

old diagnostic;
corrected diagnostic;
threshold;
old status;
corrected status;
change/no-change.

Any change in group status must propagate to:

* story report;
* paper;
* deck;
* notebook;
* gallery;
* rehearsal wording.

No post-hoc threshold change.

==================================================
4. POPULATION-FIT HOURS MOMENTS
===============================

Separately recompute the S11 population-fit hours moments using the
authoritative S10/S11 structural-band definitions.

Preserve the distinction between:

A. structural opportunity-shifter bands used by S11; and
B. descriptive/reporting hours categories where those are defined
independently.

Do not silently redefine a descriptive reporting bin merely because a
structural coefficient band has different boundaries.

For the structural-band fit table, use the S11/S10 bands exactly.

The old claim of a large “near-full-time band underprediction” is RETIRED.

Do not carry forward:

* the old single-men -9.48pp statement;
* the old coupled-women -7.21pp statement;
* the paper's “9.5 percentage points” sentence;
* corresponding stale gallery/notebook numbers.

Current preliminary audit suggests the corrected structural FT-band gaps are
much smaller and that a remaining mismatch is concentrated at the 37-hour
mass point, which lies outside the S11 FT structural band.

Do not freeze the exact 37-hour magnitude until the corrected run is complete.

If it survives, describe it precisely as:

“underprediction of the observed 37-hour mass point”

and NOT as:
“underprediction of the structural full-time band.”

==================================================
5. IMPACT TABLE
===============

Produce one compact old-versus-corrected impact table covering at minimum:

* participation accuracy by group;
* extensive balanced accuracy / adequacy statistic;
* hours-state accuracy by group;
* key structural-band observed-minus-predicted gaps;
* observed-state log score;
* Brier score;
* numerical-adequacy status;
* any headline calibration result.

Classify every prior substantive fit claim:

UNCHANGED
MODIFIED
WITHDRAWN

This table becomes the authoritative provenance bridge.

==================================================
6. DECOMP-2
===========

Do NOT rerun DECOMP-2 because of the band-edge issue unless an independent
dependency trace contradicts the current audit.

Its current implementation uses the SHA-pinned S10 criterion-A frames and
their own structural flags rather than reconstructing these bands from the
S12 constants.

Perform only a cheap lineage/no-change verification:

* input frame hashes unchanged;
* band flags read from S10 frames;
* no dependency on the S12-native edge constants;
* coalition Ginis/Shapley assets therefore unchanged.

Return PASS/FAIL.

If FAIL, stop and escalate immediately.
Do not silently regenerate the decomposition.

==================================================
7. SURFACE REGENERATION
=======================

After corrected POSFIT and hours-fit outputs pass internal checks, rebuild:

* JMP_research_story_report_v7.html;
* editable story-report source;
* JMP_results_gallery_current.html;
* canonical A-to-Z notebook;
* seminar deck slides 8–9 and any other affected slide;
* rehearsal pack;
* affected working-paper fit text/tables/figures.

Do not circulate v6.

The v7 report must simultaneously implement the prior Deputy ruling:

* W1_F wording corrected;
* DECOMP-2 restored to main results as a preliminary restricted exercise;
* abstract states qualitative decomposition result without making 1.8–9.9%
  the headline;
* W_EA_flat remains numerically BLOCKED;
* no historical W1-EA percentage appears as current evidence;
* short-hours finite-panel limitation disclosed.

==================================================
8. FINAL STALE-ASSET SCAN
=========================

Search all current seminar-facing outputs for:

17.5
28.5
36.5
18.5
29.5
37.5
9.48
7.21
9.5 percentage
0.0129
0.0136

Every occurrence must be classified as:

A. historically/native correct;
B. corrected current S11 result;
C. stale and removed.

Also search for old rendered figures by filename/hash, not text alone.

No seminar-facing current artifact may silently retain a superseded POSFIT
figure.

==================================================
9. CIRCULATION UNBLOCK GATE
===========================

Circulation is unblocked only if all are true:

G1 corrected S11 evaluation uses the S11/S10 band indicators;
G2 POSFIT v3 dependent outputs regenerated;
G3 population-fit moments regenerated;
G4 group adequacy adjudication re-run mechanically;
G5 old near-FT claims removed/replaced;
G6 DECOMP-2 no-dependency verification passes;
G7 all seminar-facing surfaces rebuilt;
G8 stale-asset scan passes;
G9 v7 wording satisfies the prior W1_F / DECOMP-2 / WEA ruling.

==================================================
RETURN TO DEPUTY
================

Return one package with:

1. corrected POSFIT v3 memo;
2. old-vs-corrected impact table;
3. four-group final adequacy adjudication;
4. corrected structural-band fit table;
5. 37-hour diagnostic if it survives;
6. DECOMP-2 no-dependency verification;
7. stale-asset scan;
8. v7 HTML + source + hashes;
9. updated deck/notebook/gallery/rehearsal identifiers;
10. tool/model/effort/dependency/status ledger.

No re-estimation.
No repricing.
No WEA computation.
No threshold changes.
No rewriting of historical S8/S12 artifacts.
