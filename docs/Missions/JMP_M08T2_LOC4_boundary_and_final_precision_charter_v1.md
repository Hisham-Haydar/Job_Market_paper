# MISSION JMP-M08T2 — LOC4 beta_w_pexp2 Boundary Analysis and Preferred-Arm Final Numerical Precision

**Status:** CHARTER-BINDING (deputy-ruled; no Goal-1 freeze needed - the ruling IS the freeze)
**Source:** M08T2 deputy ruling, ss3-8 + s12 (verbatim transcription; constants are not paraphrased)
**Two-stage structure:** T2-A (profile likelihood over beta_w_pexp2) followed by T2-B (randomized QMC final numerical precision instrument for the preferred LOC4 arm)

## 4. STAGE T2-A — PROFILE LIKELIHOOD

Profile beta_w_pexp2 over its full legal interval.

Freeze the initial grid:

{-0.10, -0.09, ..., 0.09, 0.10}
plus the exact unrestricted LOC4 estimate.

At every point:

fix beta_w_pexp2;

re-optimize every other free LOC4 coordinate;

retain all accepted pins, bounds, sample, proposal correction and
objective;

use two deterministic starts:
unrestricted LOC4 MLE projected onto the fixed value, and the
nearest converged profile solution;

add a third deterministic perturbation start at either bound or
wherever the two starts differ by more than 1e-8 in negLL;

record convergence, KKT, active set, gradients and objective.

No EUROMOD and no new alternatives.

Define:

LR_p(b) = 2 * [Q_profile(b) - Q_LOC4_MLE]

Report conventional support regions:

LR_p <= 2.7055434541
LR_p <= 3.8414588207

with an explicit boundary/active-set caveat.

Adaptively bisect only intervals containing:

either LR cutoff;

a 1% W1-mean crossing;

a sign change;

an ordering change;

a LOC4 materiality-classification change.

Stop at beta-width <= 0.0025.

At every converged point evaluate on the same priced 16x basis:

W1 mean and Gini;

phi_A, phi_B, phi_P, R_bg, phi_A+phi_B;

s_opp;

signs and ordering;

LOC4-minus-baseline differences;

W4 mean as normative-reference disclosure.

Use identical qW, normalisation, references, operators, CRN and
prices.

Report the profile-conditioned functional envelope over the
conventional LR<=3.8414588207 region.

Do not call this full welfare uncertainty.

Return if:

the profile is disconnected;

relevant constrained optimisations fail;

the unrestricted optimum moves to a bound;

LOC4 fit/materiality ceases inside the profile region;

W1 Gini or opportunity materiality disappears;

A>B>P fails anywhere;

a sign changes;

an estimand, support, qW or normalisation inconsistency appears.

A W1-mean envelope wider than 1% does not reject LOC4. It requires
boundary-conditioned reporting.

## 5. FINAL PRECISION INSTRUMENT

The prior pre-LOC4 ceiling is lifted only for the preferred LOC4 arm.

Authorize randomized QMC as the sole new final numerical instrument.

Do not reopen or retune U6-CV1.
Do not authorize another ordinary ladder.
Do not authorize per-functional estimator selection.

Use eight independent Owen-scrambled Sobol replicates, 256 stochastic
proposal nodes per household per replicate, with seeds:

2026082701
2026082702
2026082703
2026082704
2026082705
2026082706
2026082707
2026082708

Freeze before pricing:

Sobol dimension;

uniform-coordinate mapping;

inverse-CDF rules;

mixture, hours, occupation and wage construction;

atom/chosen treatment;

support and duplicate rules;

exact qW density;

target-only pricing geometry;

package/SciPy versions.

Implement in MNL only. No dclaborsupply source change.

Commission one bounded GPT-5.6 Codex read-only review before pricing.

Require:

deterministic reproduction by seed;

distinct scrambles;

exact marginal/moment/category checks;

finite exact qW for every row;

defensive-bound conformance;

normalisation identities;

unchanged chosen/non-employment conventions;

identical priced nodes across baseline, LOC4, S-10 and profile
evaluations.

Authorize EUROMOD only after Codex ACCEPT.

Cost guard:
7 hours projected maximum.

If exceeded, return before pricing.

## 6. RQMC ESTIMATOR

For household i and scramble r calculate J_ir.

Use:

Jbar_i = mean_r(J_ir)

before log and money-metric inversion.

Calculate eight leave-one-scramble-out functional estimates.

Use the delete-one-scramble jackknife and:

t_0.975,7 = 2.364624251

for the MC band.

Do not average already-transformed welfare values as the primary
estimator.

Primary final gates:

W1 mean relative MC error <= 0.0025;

W1 Gini MC error <= 0.00125;

every W1 component-level MC error <= 0.00125;

normalized-contribution precision under the accepted scale-
consistent rule;

signs and A>B>P stable across all leave-one-scramble estimates;

precise LOC4-minus-baseline differences;

precise S-10 differences;

exact Shapley and R_bg accounting;

valid support and inequality-index domains.

Median remains:

MC_BAND_ONLY_NONSMOOTH

W4/W6 remain secondary. If their decomposition precision fails, do
not claim cross-measure quantitative robustness; this does not by
itself overturn LOC4's preferred structural status.

If primary W1 QMC gates fail:

authorize no further instrument;

retain LOC4 as preferred if T2-A passed;

retain banded magnitudes;

return for final manuscript-claim narrowing.

## 7. INDEPENDENT REVIEW

After T2-A and T2-B, commission:

JMP-M08T2 — Independent Boundary and Precision Review

Tool:
ChatGPT Thinking

Model:
GPT-5.6 Thinking

Reasoning:
High

Writes:
None

The reviewer audits:

profile construction and nuisance reoptimization;

LR support-region caveat;

functional profile envelope;

continued LOC4 fit/materiality/ordering;

QMC target identity;

scramble independence and MC estimator;

support and disclosure;

final claim boundaries.

Permitted verdicts:

LOC4_PREFERRED_FULL_NUMERICAL_FREEZE
LOC4_PREFERRED_PROFILE_BANDED_LEVELS
LOC4_PREFERRED_MC_BANDED_LEVELS
PREFERRED_SPECIFICATION_UNRESOLVED
REJECT_EVIDENCE_CHAIN

## 8. REQUIRED PERMANENT OUTPUTS

Retain only:

JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md

FR_P2a_m08_loc4_beta_w_pexp2_profile_results_v1.md

FR_P2a_m08_loc4_rqmc_final_precision_results_v1.md

FR_P2a_m08_loc4_tier2_independent_review_v1.md

JMP_M08_LOC4_preferred_spec_acceptance_v1.md

JMP_M08_LOC4_manuscript_claim_set_v2.md

Code, configs, tests, manifests and restricted numerical artifacts
remain in MNL.

Routine prompts and progress notes remain disposable chat.

## 2. RETURN

Return to the deputy if:

a T2-A halt fires;

QMC design cannot reproduce exact qW;

projected pricing exceeds 7 hours;

Codex rejects after the one permitted correction;

primary W1 QMC gates fail;

final review returns unresolved/reject;

a package change is required;

disclosure fails.

Otherwise, close JMP-M08T2 autonomously and return the final
preferred-specification acceptance packet.

Record this ruling in the consolidated rulings document.
Create no separate deputy-ruling memo.
