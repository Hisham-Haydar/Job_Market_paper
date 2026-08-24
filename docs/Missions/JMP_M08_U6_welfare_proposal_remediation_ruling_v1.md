# JMP-M08 U6 Ruling — Welfare Proposal Remediation v1

**Programme:** Goal 1 — Empirical JMP  
**Decision-maker:** Deputy Programme Director  
**Date:** 2026-08-18  
**Status:** Binding  
**Mission disposition:** M08 remains open; Stage-D execution remains halted  
**Authorized remediation:** Proposal-axis repair only  
**Re-estimation:** Prohibited  
**Gate relaxation or re-anchoring:** Prohibited

## 1. Decision

Authorize a bounded M08 welfare-integration remediation on the **proposal axis**.

The current estimation proposal \(q\) remains accepted for estimation and for the
historical 1x/2x/4x diagnostic record. It is not accepted as the production
proposal for welfare-level integration or the coalition counterfactuals.

The remediation constructs a welfare-specific defensive-mixture proposal
\(q^{W}\), together with a valid sampler from every coalition-specific estimated
opportunity density \(\widehat g_i^S\).

No parameter, utility function, opportunity-density parameter, tax-benefit
mapping, coalition operator, welfare measure, inequality index, or materiality
threshold is changed.

## 2. Basis

The pre-registered R-89 rule required promotion only if the smallest
\(m\in\{2,4\}\) satisfied:

1. adjacent-step group-median \(V_i^{IS}\) drift into \(m\) no greater than
   0.05 nats;
2. the full frozen battery, including V6/V22, passed on the \(m\)-basis;
3. no persistent direct-versus-IS disagreement.

The returned evidence establishes:

- the 1x V6/V22 failure was an ESS artifact and closes at 2x/4x;
- raw inclusive-value drift remains above 0.05 nats at both promotion points;
- convergence is slower than the nominal \(1/\sqrt m\) benchmark;
- ESS grows sub-linearly;
- the baseline direct cross-check persistently disagrees with IS;
- seven coalition cross-checks are not evaluable because no sampler from
  \(\widehat g_i^S\) exists.

This is a failure of the welfare integration instrument, not evidence against
the accepted structural estimate.

### 2.1 Consequence for the welfare specification

For the France 2016 P2a M08 application, the prior statement that the existing
estimation proposal is empirically “well-conditioned” for welfare integration is
superseded by the Stage-D evidence.

The following remain valid:

- proposal-corrected importance sampling is a consistent integration framework
  under adequate moment/support conditions;
- the mandatory proposal correction remains part of the welfare estimator;
- the accepted estimation likelihood and its proposal are unchanged.

The following no longer controls M08:

- the empirical claim that the existing \(q\) provides adequate welfare-level
  integration for the baseline and equalised coalition targets.

M08 therefore retains importance sampling as the primary integration method but
uses the repaired \(q^W\). The existing welfare specification is not rewritten
during remediation; this ruling and the amended execution contract govern until
the next accepted welfare-specification revision.

## 3. Rejected alternatives

### 3.1 No functional-only gate re-anchoring

Do not replace the frozen inclusive-value and direct-agreement gates with a
post hoc requirement that only final money-metric or Shapley functionals be
stable.

The observed direct-versus-IS disagreement is approximately one nat in the
baseline flagged subset and is not shown to be a household-common additive
error. The error may vary by household, coalition, and reference inversion.
Stable aggregate functionals under such an instrument could be accidental and
would not certify the underlying welfare calculation.

Functional-level drift may be reported as an **additional diagnostic after**
the repaired proposal passes the frozen raw-level gates. It cannot substitute
for them in M08.

### 3.2 No further draw-size escalation under the old proposal

Do not build 8x, 16x, or 32x extensions under the old \(q\). The observed
heavy-tail signature and direct disagreement make that route computationally
inefficient and scientifically inferior.

### 3.3 No M08 pause at this stage

M08 remains active because a bounded proposal repair is technically and
scientifically feasible. If the single authorized repair fails, M08 pauses and
returns to the deputy; no second proposal redesign is self-authorized.

## 4. Required welfare-proposal architecture

Before any new EUROMOD pricing, freeze one exact design in:

`Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md`

The design must satisfy all of the following.

### 4.1 One coalition-robust proposal

Use one frozen welfare proposal \(q_i^W\) for:

- all eight \(A/B/P\) coalitions;
- both active decomposition measures;
- all four S-10 scenarios.

This preserves common random numbers and prevents proposal changes from
contaminating coalition or scenario differences.

A coalition-specific proposal may be used only for the independent
\(\widehat g_i^S\)-direct cross-check, not as the primary proposal.

### 4.2 Defensive-mixture form

The proposal must be a genuine defensive mixture:

\[
q_i^W(j)=(1-\lambda)q_i(j)+\lambda r_i(j),
\qquad 0<\lambda<1,
\]

or an algebraically equivalent multiple-importance-sampling construction.

Requirements:

- the accepted estimation proposal \(q_i\) retains strictly positive mixture
  mass;
- \(r_i\) gives materially broader coverage of the wage and other tail-relevant
  job-package dimensions;
- \(r_i\) covers the support needed by every frozen coalition target;
- the exact mixture density \(q_i^W(j)\) is evaluable for every sampled row;
- the welfare value uses the exact correction \(-\log q_i^W(j)\), never the old
  \(-\log q_i(j)\);
- mixture component labels, weights, normalizing constants, and seeds are
  persisted.

The design author must choose and justify one primary \(\lambda\), one exact
tail component, and one exact support convention before priced welfare outcomes
exist. No post-result tuning of \(\lambda\), scale, or component weights is
permitted.

### 4.3 Nested draw ladder

Construct one nested seeded ladder:

- 1x: 101 alternatives per household;
- 2x: 201 alternatives per household;
- 4x: 401 alternatives per household.

The 1x basis is a prefix/subset of 2x, and 2x is a prefix/subset of 4x.
Preserve the accepted chosen-alternative and non-employment support conventions.

Operational sequence:

1. generate and price through 2x;
2. evaluate the frozen promotion rule;
3. extend and price only the additional rows needed for 4x if 2x does not
   qualify.

Do not price a separate non-nested 1x, 2x, and 4x basis.

### 4.4 Coalition opportunity samplers

Implement a sampler for each normalized coalition opportunity object
\(\widehat g_i^S\), \(S\subseteq\{A,B,P\}\).

The sampler must:

- use the same frozen factorization and channel operators as the accepted
  contract;
- alter no accepted coefficient;
- respect the accepted access/ability/preference slot routing;
- sample no object from the fixed proposal \(q\) while labelling it a
  \(\widehat g_i^S\) draw;
- persist the coalition, household, component, seed, and probability/density
  information needed to reproduce each draw;
- pass normalization and moment/category-frequency tests against the analytic
  coalition object before EUROMOD pricing.

The direct estimator remains a validation estimator. It does not replace the
primary proposal-corrected estimator.

### 4.5 Application location

Implement this remediation in the France application layer in MNL.

Do not modify `dclaborsupply` package source during this mission. Reuse its
accepted evaluators where possible. If a generic package change is unavoidable,
halt and return as a package-change escalation.

## 5. Frozen validation and promotion rules

No numerical gate is relaxed.

For the repaired \(q^W\), apply the existing smallest-qualifying-basis rule:

1. U6 adjacent-step group-median drift into \(m\leq0.05\) nats;
2. full frozen battery including V6/V22 passes on that basis;
3. no persistent direct-versus-IS disagreement;
4. all existing finiteness, inversion, reference, operator, disclosure, and
   invariance gates pass.

Direct cross-check:

- evaluate every coalition on its frozen flagged subset;
- disagreement for a household:
  \(|V_i^{dir,S}-V_i^{IS,S}|>0.5\) nats;
- persistent disagreement:
  subset median above 0.5 nats;
- choose redraw count by the existing pilot rule
  \(MC\text{-}SE(V_i^{dir,S})\leq0.05\) nats.

All eight coalitions must be evaluable before promotion. If projected direct
pricing exceeds six hours, return a costed execution plan to the Goal 1 Manager;
do not truncate the certification set or redefine the gate.

Functional-level stability may be computed in parallel as a non-gating
diagnostic.

## 6. Bounded work stages

### Stage U6-A — proposal design and freeze

- **Tool:** separate Claude Project chat
- **Model:** Opus
- **Thinking:** On
- **Effort:** High
- **Repository writes:** only the design memo in `Job_Market_paper`
- **No EUROMOD execution**
- **No code change**

The design memo must specify:

- exact mixture formula;
- exact \(\lambda\);
- exact component distributions and support;
- exact common-random-number construction;
- exact nested ladder;
- exact \(\widehat g_i^S\) sampler;
- exact density/probability evaluation;
- exact tests;
- exact expected pricing volume and cost;
- exact output namespace;
- exact halt conditions.

The Goal 1 Manager may resolve mechanical implementation details but may not
change the frozen gates.

### Stage U6-B — implementation and deterministic tests

- **Tool:** Claude Code
- **Model:** Opus
- **Thinking:** On
- **Effort:** High
- **Repository:** MNL
- **Write authority:** application-specific proposal/sampler code, configs,
  tests, and restricted staging artifacts only

Before EUROMOD:

- test mixture normalization;
- test exact proposal-density evaluation;
- test support;
- test nested prefixes;
- test deterministic reproduction;
- test coalition sampler moments/category probabilities;
- test that old \(q\) and new \(q^W\) corrections cannot be confused;
- test that accepted \(\theta\), \(c_{ij}\) inputs, channel operators, and
  reference objects are unchanged.

### Stage U6-C — bounded independent code review

- **Tool:** GPT-5.6 Codex
- **Mode:** read-only
- **Reasoning:** High

Review only:

- mixture sampling and density identity;
- proposal correction;
- coalition sampler validity;
- common-random-number and nested-basis construction;
- unchanged accepted structural inputs;
- target-only pricing geometry;
- restricted-artifact persistence.

One narrow correction cycle is permitted. Do not reopen the structural model or
prior parity certification.

### Stage U6-D — nested pricing and validation

- **Tool:** Claude Code
- **Model:** Opus
- **Thinking:** On
- **Effort:** High

Execute the 2x basis first through the unchanged certified target-only pricing
path. Extend to 4x only if required by the frozen rule.

Run the full frozen validation battery and every coalition direct cross-check.

### Stage U6-E — independent numerical/economics review

- **Tool:** ChatGPT Thinking
- **Model:** GPT-5.6 Thinking
- **Reasoning:** High
- **Writes:** none

Audit:

- promotion-rule compliance;
- no gate relaxation;
- proposal correction;
- direct-versus-IS evidence;
- all-coalition evaluability;
- no model or normative change;
- whether the repaired basis is acceptable for M08 welfare execution.

One narrow reporting correction is permitted. No numerical rerun is permitted
unless the reviewer identifies a genuine evidence-binding defect.

## 7. Required permanent outputs

Apply documentation proportionality. Permanently retain only:

1. `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md`
2. `MNL/docs/France_case/P2a/FR_P2a_m08_welfare_proposal_validation_v1.md`
3. `MNL/docs/France_case/P2a/FR_P2a_m08_welfare_proposal_codex_review_v1.md`
4. `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_acceptance_v1.md`

Code, tests, configs, manifests, and restricted draw/pricing artifacts remain
in MNL. Routine action cards and progress notes remain disposable chat.

## 8. Failure and return conditions

Return to the deputy if:

- the design cannot define an exact \(q^W\) density;
- any coalition \(\widehat g_i^S\) sampler cannot be constructed;
- a generic package change is required;
- 2x and 4x both fail the unchanged promotion rule;
- any coalition has persistent direct-versus-IS disagreement;
- the repaired proposal requires infeasible pricing volume;
- accepted structural inputs or coalition operators would need to change;
- household-level disclosure cannot be controlled.

No second proposal redesign, gate re-anchoring, old-\(q\) draw escalation, or
welfare headline is authorized after such a failure.

## 9. Status of existing evidence

Preserve the old-\(q\) 1x/2x/4x datasets and validation records as the
diagnostic basis for this ruling.

They demonstrate that:

- the 1x V6/V22 failure was basis-ESS sensitive;
- enlarging the old basis improved ESS but did not stabilize level integration;
- the persistent baseline direct disagreement remains unresolved;
- the old proposal is not promoted for welfare-level production.

These artifacts are not headline welfare results and must not appear in the
paper as economic findings.
