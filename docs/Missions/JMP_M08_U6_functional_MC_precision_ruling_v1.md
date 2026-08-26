DEPUTY RULING — U6 FUNCTIONAL MONTE CARLO PRECISION

Choose option (a), with the following binding amendment.

1. VALIDITY VERSUS PRECISION

Retain as hard validity gates:

- opportunity-kernel normalisation;
- exact q^W density and -log q^W correction;
- defensive-mixture bound conformance;
- finite weights and tail diagnostic;
- all eight coalition samplers evaluable;
- per-coalition persistent direct-vs-IS median <= 0.5 nats;
- inversion, reference, operator, disclosure and Shapley-accounting
  gates.

Reclassify:

- the 0.05-nat household adjacent-step V_i drift;
- the raw ESS-30 V6/V22 status;

as mandatory diagnostics and functional-precision triggers rather
than standalone promotion gates.

The remaining {A,P} V22 flag must remain visible.

2. CANDIDATE BASIS

Use 4x as the sole paper-facing candidate basis.

Keep 1x and 2x as diagnostics.
Authorize no additional EUROMOD for this decision.

3. BLOCK DESIGN

Verify that the 400 stochastic q^W nodes per household form four
disjoint, valid 1x-equivalent random blocks. The deterministic chosen
and non-employment nodes may be shared.

If four valid blocks cannot be established from the frozen design,
halt and return.

For every paper-facing functional T compute:

- full 4x value T4;
- all six two-block estimates T2_ab;
- four leave-one-block-out three-block estimates T3_-b.

Define:

T2_bar = mean over the six T2_ab

T3_bar = mean over the four T3_-b

SE_MC(T4)
= sqrt[(3/4) * sum_b (T3_-b - T3_bar)^2]

E_T = max(
    abs(T4 - T2_bar),
    1.96 * SE_MC(T4)
)

4. FROZEN PRECISION THRESHOLDS

For each W1-W6 mean and median define:

S_k = max(
    abs(mean_Wk),
    abs(median_Wk),
    IQR_Wk,
    1 euro
)

Require:

E_T / S_k <= 0.0025

For every welfare Gini or other headline inequality index require:

E_T <= 0.00125

For access, opportunity, preference and residual shares require:

E_T <= 0.005

For headline decomposition signs and ordering:

- sign must agree between 4x and every 3x leave-one-block-out estimate;
- ordering must agree between 4x and every 3x estimate;
- no sign claim where the 95% MC interval includes zero.

For later RUM-RURO comparisons:

- rank-correlation E_T <= 0.01;
- decile-movement or threshold-crossing share E_T <= 0.005.

Subgroup summaries carry MC_STABLE / MC_UNSTABLE diagnostics but are
not separate population-level promotion gates.

5. PROMOTION

Promote 4x only if:

- every hard validity gate remains passed;
- all W1-W6 mean/median/Gini functionals pass;
- the primary W2 decomposition passes;
- the secondary W5 decomposition passes;
- Shapley and fixed-background accounting pass;
- no paper-facing functional is silently omitted;
- the independent U6 review accepts.

If any primary functional fails, halt and return. Do not self-authorize
QMC, control variates, more ordinary draws, or a gate relaxation.

6. RUM BENCHMARK

Proceed immediately with the common-opportunity RUM estimation and
inference in parallel.

Use the corrected marginal/MIS proposal convention, the same sample,
job support and priced budgets, and the frozen RUM estimand.

No EUROMOD and no q^W are required.

7. LOC4=-2 TO LOC4=4 AUDIT

Before occupation-access interpretation, produce one bounded
aggregate audit establishing:

- exact code path and rule;
- source meaning of -2 and 4;
- chosen-row incidence;
- affected-household count;
- identity of the seven rows across accepted production, corrected
  marginal/MIS and qW 1x/2x/4x bases;
- consistent pre-likelihood and pre-welfare application;
- absence of any path retaining -2 while another uses 4.

Do not remap, drop or reprice.

If deterministic, documented and identical across all paths, retain
and disclose in data cleaning and the specification-limits block.
Otherwise halt and return.

8. HOUSEKEEPING

No further JMP-HK-01 movement or deletion during the U6 functional
review.

In the next return record the subjects and changed-path summaries for:

MNL 9b2fe82
Job_Market_paper 5efc37a

and confirm no pinned path, accepted attempt, ruling-protected
artifact, manifest member or live review target moved or disappeared.

Proceed autonomously through the functional calculation and the
already planned independent GPT-5.6 Thinking U6 review.

Return only if:

- four valid random blocks cannot be formed;
- a primary functional fails;
- the loc4 audit finds inconsistent treatment;
- the RUM estimand fails;
- a Tier-2 S-10 trigger fires;
- a package change is required;
- disclosure fails;
- or LOC4 sequencing conflicts.