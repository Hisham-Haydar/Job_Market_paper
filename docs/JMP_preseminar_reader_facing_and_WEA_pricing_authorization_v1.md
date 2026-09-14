GOAL 1 — PI OVERRIDE: AUTHORISE WEA PRICING + READER-FACING REPORT

This ruling supersedes the previous instruction not to launch WEA pricing
before the seminar.

The PI explicitly authorises the additional pricing required to compute the
ex-ante opportunity-prospect welfare measure correctly.

Do not continue treating the pricing decision as blocked.

==================================================
A. ABSTRACT — MAGNITUDE APPROVED
================================

Restore the preliminary decomposition magnitude to the abstract.

Use:

“In a preliminary restricted structural decomposition of the attained-bundle
money metric, equalising systematic utility heterogeneity, coarse geographic
and temporal access, and systematic wage opportunities—while holding
household resources, needs and composition fixed—reduces the Gini by
1.8–9.9% relative to its baseline level across household types and reporting
scales. Within this restricted exercise, the earning-opportunity channel is
larger than the coarse access channel throughout. These figures do not
estimate the total share of well-being inequality caused by unequal job
opportunities.”

Keep the full numerical table in the main results and the technical detail
in the appendix.

The decomposition is PRELIMINARY, not hidden.

==================================================
B. WEA PRICING IS NOW AUTHORISED
================================

The WEA readiness audit established that the current S10 panel is not
adequate for the J/H welfare integral and that additional pricing is
indispensable.

Proceed.

Do NOT immediately price an arbitrary fixed 354k design.

First exploit the fact that H requires no consumption and therefore allows
free pre-validation.

Construct the defensive-hours augmentation described in
JMP_WEA_reconstruction_and_estimand_comparison_v1.md.

Use the same:

* accepted household samples;
* S10/S11 structural model;
* cross-fit employment/quadrant law;
* occupation law;
* wage proposal law;
* existing EUROMOD pricing path.

Augment working alternatives with a defensive hours proposal covering
[5,70], as designed in the readiness memo.

Also include the 260 missing couple NN/home states.

PRE-PRICING DESIGN RULE:

Test increasing defensive sample sizes on TWO fixed independent seed streams.

Select the SMALLEST design that passes, in every one of the eight P/A/B
coalitions and in both samples:

1. median absolute log error of estimated H <= 0.01;
2. at least 95% of households have absolute log H error <= 0.05;
3. no material systematic undercoverage remains in the low-hours region;
4. the result is stable across the two seed streams.

If N_def=100 passes, use it.
If it fails, increase N_def until the fixed gate passes.

Do not inspect WEA inequality or Shapley results while choosing N_def.

Once a design passes, price it immediately through the existing accepted
S4-IID / EUROMOD route.

This pricing is authorised without another Deputy permission request.

After pricing, compute W_EA_flat using the already-ruled H-F primary
reference, with H-D and household exclusion only as sensitivities.

No EUR1 floor.
No C_obs substitution.
No silent sample deletion.

Then apply the existing WEA post-pricing checks:

* J/H integrand ESS;
* top-weight diagnostics;
* second-seed stability;
* wage-tail check;
* constant-consumption identity;
* singleton-state identity;
* intensity-scale cancellation;
* flat-reference inversion identity;
* exact Shapley adding-up;
* independent implementation verification.

Report whatever numbers emerge.
There is NO target opportunity share.

==================================================
C. DO NOT HOLD THE DISCUSSANT REPORT HOSTAGE TO WEA
===================================================

The discussant report proceeds using the verified Mapping-F welfare results
and the preliminary restricted DECOMP-2 results.

If clean WEA results pass verification before the report is frozen, add them
as a clearly distinct ex-ante welfare perspective.

If they do not pass by the circulation freeze, state only that the ex-ante
opportunity-prospect extension is under numerical validation.

Do NOT restore historical W1-EA percentages merely because the clean
calculation is unfinished.

Earlier report versions may be used for PRESENTATION STYLE and simpler
narrative, not as numerical authority for superseded W1-EA results.

==================================================
D. REMOVE “MACHINE LANGUAGE” FROM THE DISCUSSANT REPORT
=======================================================

The current v7 remains too close to an internal audit document.

Rewrite the MAIN TEXT and ABSTRACT for an economics discussant.

Internal implementation labels must disappear from reader-facing prose,
except where absolutely needed in a technical appendix.

Do not make the discussant read terms such as:

S10
S11
S12
POSFIT-v3b
DECOMP-2
criterion-A
Gate 0
anchor
node
proposal panel
exact-H
H-F
H-D
H-X
NN pricing state
SHA/hash
dwt
PROTECTED_ATTRS
worktree
result registry

Translate them into economic language.

Examples:

Instead of:
“the S11/S10 specification”

write:
“the preferred specification”.

Instead of:
“the S12 predictive panel”

write:
“the large predictive integration sample”.

Instead of:
“POSFIT-v3b”

write:
“the predictive-fit diagnostics”.

Instead of:
“DECOMP-2”

write:
“the preliminary structural decomposition”.

Instead of:
“H-F is the primary WEA domain”

write:
“the ex-ante reference keeps the full opportunity environment fixed while
equalising consumption across jobs.”

Instead of:
“260 couples lack a priced NN state and exact-H pre-validation is required”

write, if it needs to appear at all:
“additional counterfactual tax-benefit evaluations are required before the
ex-ante measure can be reported reliably.”

Most of that information should simply be moved to a technical appendix.

==================================================
E. WEA SECTION IN MAIN REPORT — SHORTEN DRASTICALLY
===================================================

Replace the current implementation-heavy WEA discussion in the main text
with approximately one paragraph:

“We are also developing a complementary ex-ante measure that values the
quality of the household’s entire job-opportunity prospect rather than only
the bundle eventually attained. It asks for the constant consumption level
that would make the household indifferent between its actual stochastic job
prospect and a reference prospect with the same opportunities but equal
consumption across jobs. Unlike the attained-bundle measure, this object is
directly sensitive to the estimated opportunity distribution. Its numerical
implementation requires additional counterfactual tax-benefit evaluations
to obtain adequate coverage of the hours distribution, so the corresponding
inequality decomposition is still preliminary and is not reported here.”

Put J/H formulas and domain conventions in the technical appendix only.

==================================================
F. KEEP THE PAPER'S ECONOMIC STORY VISIBLE
==========================================

The discussant should be able to understand the paper without knowing our
internal mission history.

The main sequence should be:

1. Why income inequality mixes preferences and opportunities.
2. How the latent-jobs model separates systematic preferences from job
   opportunities under maintained restrictions.
3. How attained bundles are converted into money-metric well-being.
4. How the preliminary counterfactual decomposition works economically.
5. What the current results say.
6. What remains preliminary.
7. Why an ex-ante opportunity-prospect extension is useful.

Technical provenance belongs in appendices and internal memos.

==================================================
G. ONGOING-WORK LANGUAGE
========================

It is acceptable and required to tell the discussant that some results are
preliminary.

Use language such as:

“These decomposition estimates are preliminary and subject to ongoing
numerical validation of the counterfactual integration.”

or:

“The quantitative decomposition should be read as a preliminary structural
accounting exercise; additional numerical robustness checks are in progress.”

Do NOT use informal phrases such as:
“we are still cleaning the results”.

==================================================
H. BAND-EDGE CORRECTION
=======================

Continue the already-authorised correction of S11 predictive evaluation on
the S12 priced nodes.

This requires no repricing:
recompute the S11 structural band indicators on the existing priced states,
reevaluate probabilities, and regenerate the affected fit diagnostics.

Do not delay WEA pre-validation or report rewriting while this runs.

DECOMP-2 remains unchanged unless its already-requested no-dependency check
fails.

==================================================
I. NEXT REPORT
==============

Do not overwrite v7.

Build:
JMP_research_story_report_v8.html

The purpose of v8 is not to add more audit material.
It is to REMOVE internal audit language and return to a readable economics
research narrative.

Also rebuild the results gallery so that captions and headings are
reader-facing. Internal labels may remain only in a collapsible provenance
appendix if useful.

RETURN:

1. v8 HTML + editable source;
2. revised abstract with 1.8–9.9%;
3. main-results decomposition section;
4. one-paragraph reader-facing ex-ante extension section;
5. machine-language deletion/replacement audit;
6. corrected predictive-fit outputs from the band-edge fix;
7. WEA pre-pricing exact-H design results;
8. selected defensive design and pricing-launch record if the gate passes;
9. ledger of tools/models/effort/dependencies/status.

No additional Deputy permission is needed to launch WEA pricing after the
pre-pricing gate passes.
