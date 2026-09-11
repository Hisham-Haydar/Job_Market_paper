# JMP_W1_fork_ruling_v1.md — Goal 1 response to the Deputy ruling "FORK-1 and next welfare gates"

| Field | Value |
|---|---|
| Mission | JMP-W1-FORK close-out; Goal 1 implementation record for Deputy R1–R6 |
| Date | 2026-09-11 |
| Author | Goal 1 Manager (Claude project chat) |
| Status | RECORD. The Deputy text in Appendix A controls; §1 records how Goal 1 implements it and adds nothing that changes it. |
| Intended path | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` |

## 0. Authoritative inputs

1. Deputy ruling "DEPUTY RULING — FORK-1 AND NEXT WELFARE GATES" (R1–R6), carried verbatim in Appendix A.
2. `docs/normative/JMP_W1_reference_domain_fork_v1.md`. As reported by Claude Code, and to be verified on merge:
   - repository and branch: `Job_Market_paper`, `docs/w1-reference-domain-fork`;
   - commit `f6346232ef6696c623b053085991349f2bb5c462`;
   - file SHA-256 `260eb0d6dc4497cb920f4e0838c8fb3921b065d7e3df947e18ab687c49081d35`;
   - git blob `55dd6ee3a58b0a08229463b723da4deea0ce9218`.
3. `W1_latent_set_identification_note_v1.md`. The fork document cites it by hash, but it was **untracked** at the time of this record.
4. The MEASURE-MAP-1 return. It was delivered in chat only; no file was written. It recorded:
   - MNL HEAD `aa36e816e46568ff448810e5b89c28ea616a2476`;
   - `Job_Market_paper` HEAD `834055e8da5573ae237f40d38229e836b6717270`;
   - theory source `jobs_and_wellbeing.tex` SHA-256 `d8687d3cfb71ce00f81613286e784c71c0e643721987bebf0d57226afe2a02d1`.

## 1. Implementation of R1–R6

### R1 — Mapping F primary: ADOPTED

The operational object is

  W_i^1 = m_i(o; z_i), with u_i(m_i(o), o) = u_i(z_i),

which under log consumption is W_i^1 = C_i · exp{[L_i(j_i) − L_i(o)] / β_c}.

Goal 1 implementation notes. Each follows from R1 and none modifies it.

- **Utility only.** L_i is the estimated systematic non-consumption utility. Four objects do **not** enter W1-F: the opportunity density g, the numerical proposal q, the behavioural shocks ε, and the intensity κ.
- **Consumption argument.** C_i must be the consumption argument of the estimated utility at the observed state. Whether this is raw or equivalised, and whether it is EUROMOD-priced, is recorded as open item E2 (§3).
- **Home consumption does not enter.** At the observed bundle, the priced home consumption C_i(o) does not appear; W1-F uses only C_i^obs, L_i(j^obs), L_i(o) and β_c.
  - For nonworkers, W1-F = C_i^obs exactly. For workers, W1-F < C_i^obs.
  - Consequently, the 119 couples whose neither-work bundle lies outside the positive-consumption subdomain do **not** affect baseline W1-F. They can matter only for counterfactual choice sets (R5).
- **Required prose.** W1 = W4 is an empirical-domain coincidence under the current preference specification and universal behavioural availability of non-employment. It is not a theory claim.
- **Mapping M.** M is sensitivity only, at the dense-law endpoint, where it is Measure 6 on the market-job universe (identified given the 5-hour support endpoint). Finite-κ M goes to limitations. No κ enters the baseline.

### R2 — W1-EA retired from the baseline: ADOPTED

Historical name for any future reference: "ex-ante RURO inclusive-value welfare functional (historical; not Haydar–Maniquet W1)."

The following are historical artifacts, not current results:

- all stored W1-EA levels;
- all P/A/B/D shares computed on W1-EA;
- the singles/couples access-versus-earnings contrast;
- figP07;
- the power-mean paragraph, the worked example, and the Q&A answer built on W1-EA.

HFIX-1 is not authorised. Code, results and audits are preserved unedited.

### R3 — Close the FORK-1 record before citation: PARTIALLY CLOSED

| R3 item | Status | Note |
|---|---|---|
| 1 Couples max-L configuration | Closed on S11 parameters; **new open item P1** | Woman-only at 5h (the woman works 5h, the man is at home). The cause is curvature, not weights. Goal 1 reproduced the fork's increments to rounding (S11: 0.008753 / 0.002047, ratio 4.277). See P1 below. |
| 2 Deterministic script for derived numerals | **OPEN** | The numerals are labelled memo-grade, but **no script exists**. R3 requires one before citation. Carded as REC-1. |
| 3 Revision log (M → F) | Closed | Records that the flip followed the Goal 1 header item 7 and was not reached independently. |
| 4 Memory replaced, not appended | Closed | Reported: one index line; pending items tagged PENDING RULING. |
| 5 Co-author example caveat | Closed; retained | Primary source is `discussion2.md`, held by the PI. The caveat stands until an excerpt is placed in `docs/normative/`. |
| 6 No promotion of implemented W4/W6 | Standing | Pending MEASURE-MAP-1R. |

Housekeeping:

- The commit is on a branch, not `main`. Goal 1 recommends fast-forwarding `main` only after REC-1 passes.
- The cited `W1_latent_set_identification_note_v1.md` must be committed, since it is cited by hash.

**P1 — parameter provenance.** Two couples leisure-curvature tables are in circulation:

| Source | θ_ℓ (men) | θ_ℓ (women) |
|---|---|---|
| Fork document ("S11") | −0.976 | −1.686 |
| MEASURE-MAP-1 (`r240_step3_parameter_table_v1.csv`) | −1.0321 | −1.8669 |

Goal 1 recomputed both. Woman-only is the max-L market configuration under either:

- R240 increment ratio 5.52, against a block-minimum weight ratio of 3.16;
- S11 increment ratio 4.28, against a reference-couple weight ratio of 3.15.

The man-only corner threshold (4.28 versus 5.52) depends on which table is accepted. The stakes are limited to M-sensitivity; baseline F is unaffected. Which table is the accepted corrected baseline must be established from the acceptance record.

### R4 — MEASURE-MAP-1: RETURNED, NOT ACCEPTED; reissued as MEASURE-MAP-1R

Review findings on the returned audit:

- **MM-1 — wrong specification answered.** The return answers Goal 1's earlier card, not R4. It lacks R4's column set (opportunity density enters; depends directly on A; needed in revised JMP) and R4's five-class vocabulary. No `JMP_measure_map_v1.md` was written.
- **MM-2 — max versus log-sum-exp.** Measure 1 is z I max_R B, i.e. min over j ∈ A of m_i(j).
  - The executed W1 instead equates a log-sum-exp over nodes, carrying opportunity weights opp_j, to the attained value. The same holds for the reference sides of W5 and W6 (log-mean-exp).
  - A log-sum-exp with opportunity weights is an inclusive value. In it, ε is integrated out (not excluded) and the opportunity density enters.
  - The return's claims "ε does not enter" and "the log-sum-exp is structural, not smoothing" do not establish literal correspondence. That the object is structural for the RUM is precisely why it is not Measure 1.
  - The executed W1 is therefore not literal Measure 1 whatever attained value it is fed.
- **MM-3 — function versus executed artifact.** The return classes each measure by what the function would compute if fed u(z_obs), not by what the stored runs computed.
  - On W4 it conflicts with the fork closure. The closure reports that the executed W4's attained side is the ex-ante inclusive value less log(number of nodes).
  - Unresolved until the call sites are traced.
- **MM-4 — "stored literal baseline exists" is unsupported.**
  - The cited identity, W = λ_c[1 + θ_c(log J − log H)]^{1/θ_c}, is the production J/H form. It is not C^obs·exp{[L(j^obs) − L(o)]/β_c}.
  - Its "β_c = 1" qualifier conflicts with the identified-scale baseline (θ_c = 0, β_c estimated).
  - Working position: **no literal observed-bundle W1-F/W4 distribution exists** in any stored artifact.
- **MM-5 — couples derivation.**
  - The return reaches the label "woman-only" but inverts its meaning: it says the woman stays home.
  - It attributes the result to the level asymmetry in leisure weights. That asymmetry actually points toward man-only; curvature decides it.
  - Its endpoint slopes are arithmetically off. At its own parameters the correct values are 0.0582 (men) and 0.0324 (women), not 0.0625 and 0.0414.
  - It uses a different parameter table from the fork (P1).
- **MM-6 — 119 couples.**
  - The exposure it describes applies to the executed ex-ante objects, not to literal W1-F at the observed bundle (see R1 notes).
  - It also describes F as "o ∈ J", contrary to the fork verdict that o is a state, not a job.
- **MM-7 — invalid hash.** The recorded SHA-256 of `m08_welfare_measures.py` has 63 hex characters. The record is invalid.
- **MM-8 — W5/W6 departure.** The material departure is not the −log n normalisation. It is that a mean over nodes replaces a minimum.

Retained, subject to re-verification:

- the code locations and line ranges;
- W3 is degenerate (≡ 0) at baseline;
- the O-1 disposable-income-for-pay substitution in W2, W3 and W5 (reported as ratified under R-85; verify);
- the Ā construction in W5 is implementer-declared, not ratified;
- the provenance of the 119-couple count (`s12_w4_premise_audit_v1.json`).

### R5 — Counterfactual attainment design: QUEUED

`JMP_counterfactual_attainment_design_v1.md` is authored by Goal 1 after MEASURE-MAP-1R is accepted. Nothing is executed.

### R6 — Seminar: ADOPTED

Seminar content follows R6. Its conditional clause requires a literal observed-bundle W1-F/W4 distribution. Per MM-4, none exists, so verification alone cannot meet that condition. This is escalated as E1.

## 2. Standing holds

The following are held:

- all welfare and decomposition reruns;
- any finite κ;
- HFIX-1;
- the old W1-EA text, figures and Q&A;
- promotion of any executed W4/W6 number;
- counting sample couples in the man-only corner (requires sample data; not authorised).

## 3. Escalations to the Deputy

- **E1 — BASELINE-F-1 (authorisation requested).**
  - Scope: compute literal W1-F at the observed bundle for all singles and couples in the accepted estimation samples. Closed form; no simulation, no counterfactual, no decomposition.
  - Pre-registered checks:
    - (i) nonworkers W = C^obs exactly;
    - (ii) workers 0 < W/C^obs < 1;
    - (iii) no argument of the function carries g, q, ε or κ, enforced by a test;
    - (iv) two-household reproduction of the MEASURE-MAP-1R step-3 values;
    - (v) summary distribution and inequality indices reported as descriptive baseline only, with no decomposition.
  - Purpose: satisfy R6's conditional for the seminar.
- **E2 — the consumption argument C^obs.**
  - Goal 1 position: this is a consistency requirement, not a free normative choice. C^obs must be the consumption argument of the estimated utility at the observed labour state.
  - MEASURE-MAP-1R will report what that argument is (raw or equivalised; EUROMOD-priced). The Deputy confirms, or rules otherwise.

## 4. Next authorised actions

1. **REC-1** (Claude Code): FORK-1 citation closure.
   - Parameter provenance P1.
   - Deterministic numerals script (R3.2).
   - Commit this file and the identification note on the branch.
   - State-dashboard update.
2. **MEASURE-MAP-1R** (Claude Code): writes `docs/normative/JMP_measure_map_v1.md` to the R4 specification, with pre-registered acceptance criteria.
3. **Deputy**: E1 and E2.
4. After MEASURE-MAP-1R is accepted: Goal 1 drafts `JMP_counterfactual_attainment_design_v1.md` (R5).

---

## Appendix A — Deputy ruling (verbatim)

```
DEPUTY RULING — FORK-1 AND NEXT WELFARE GATES

The FORK-1 central result is accepted subject to the verification/record items
below.

======================================================================
R1 — PRIMARY W1 REFERENCE DOMAIN
======================================================================

APPROVED: Mapping F is the primary empirical implementation of
Haydar–Maniquet W1 for the current JMP.

Use:

    W_i^1(z_i,R_i,A_i)
      = m_i(o; z_i)

on the current empirical domain, with

    u_i(m_i(o),o) = u_i(z_i).

For the current log-consumption specification this is

    W_i^1
      = C_i * exp{ [L_i(j_i) - L_i(o)] / beta_c }.

State explicitly that, under the CURRENT empirical preference specification
and universal behavioural availability of non-employment, W1 coincides with
the staying-home equivalent W4.

This is an EMPIRICAL-DOMAIN coincidence.
Do NOT claim W1 = W4 in the Haydar–Maniquet theory generally.

Mapping M is not primary.

At the dense-law endpoint, M has no household-specific direct access content
and becomes the whole-market/universal-market reference object.

Finite-kappa M requires an additional unidentified intensity/set-size object
and is deferred to limitations/future work.

Do not introduce a finite kappa into the baseline JMP.


======================================================================
R2 — OLD W1-EA
======================================================================

RETIRE W1-EA FROM THE JMP BASELINE.

Do not repair the old singles W1-EA now.

Preserve its code, results and audits as historical research artifacts, but:

- do not call it Haydar–Maniquet W1;
- do not use its welfare levels as current headline results;
- do not use its P/A/B/D shares as current decomposition results;
- do not use its singles/couples access-versus-earnings contrast as a current
  quantitative JMP finding.

If revisited later, it must be separately named as an ex-ante RURO /
inclusive-value welfare functional and its singles target must first be repaired.

No HFIX-1 work is authorised now.


======================================================================
R3 — CLOSE FORK-1 RECORD BEFORE CITATION
======================================================================

Before committing/citing JMP_W1_reference_domain_fork_v1.md:

1. resolve the couple max-L reference configuration term by term from the
   accepted parameter tables;

2. reproduce all derived numerals used in the memo with one small deterministic
   script and label them as derived calculations;

3. add the revision log showing that the first-pass M recommendation was replaced
   by F and why;

4. verify that any project/Claude memory entry saying "recommend M" was REPLACED,
   not left alongside the revised F ruling; pending findings must remain marked
   pending;

5. retain the caveat on the co-author example unless its primary source is placed
   in the repository;

6. do not promote any implemented W4/W6 numerical result until MEASURE-MAP-1
   verifies literal correspondence to the theory definition.

Then commit the fork note and return its commit/hash.


======================================================================
R4 — AUTHORISE MEASURE-MAP-1
======================================================================

Run one READ-ONLY measure correspondence audit before any new welfare execution.

MISSION: MEASURE-MAP-1

For every welfare object currently named W1-W6 in the JMP code/report, produce
a table with:

- theory definition from the authoritative Haydar–Maniquet manuscript;
- exact mathematical object implemented in code;
- whether it is:
    LITERAL MATCH
    NUMERICAL APPROXIMATION TO THE SAME OBJECT
    SMOOTHED ANALOGUE
    DIFFERENT OBJECT
    NOT IMPLEMENTED;
- code path/function;
- reference domain;
- whether epsilon enters;
- whether opportunity density enters;
- whether proposal density enters;
- whether the object depends directly on A;
- whether the object is needed in the revised JMP.

PRIORITY CHECKS:

A. F / literal W1:
   verify the closed-form formula at the observed bundle.

B. W4:
   establish whether there is a stored/computed literal staying-home equivalent
   matching

       u_i(W_i^4,o) = u_i(z_i)

   or whether the existing reported W4 used another integration/smoothing route.

C. W6:
   verify the fork's warning that the existing implementation is a log-sum-exp
   or other smoothing rather than literal Measure 6.

D. Old W1-EA:
   label it explicitly as a different ex-ante object; do not repair it.

No welfare rerun.
No decomposition rerun.
Small deterministic one-household checks are allowed.

RETURN:
JMP_measure_map_v1.md


======================================================================
R5 — AFTER MEASURE-MAP-1, DESIGN COUNTERFACTUAL ATTAINMENT
======================================================================

Do NOT execute this before MEASURE-MAP-1 returns.

Prepare:

    JMP_counterfactual_attainment_design_v1.md

The central problem is:

baseline W1-F is evaluated at the OBSERVED attained bundle,

but under a P/A/B/D counterfactual the attained bundle can change.

We therefore need one coherent structural operator

    coalition S
      -> counterfactual behavioural environment
      -> counterfactual attained bundle z_i^S
      -> literal W1-F(z_i^S)
      -> inequality I_S.

Compare at least TWO candidate estimands.

1. REALISED-BUNDLE / CONDITIONED-HETEROGENEITY ROUTE

Condition behavioural latent heterogeneity on the observed choice, preserve an
economically coherent common latent state across coalition counterfactuals,
re-select the counterfactual job, and compute literal W1-F.

Establish:
- whether the Dagsvik-Jia/max-stable construction supplies such a cross-world
  coupling;
- whether it requires unidentified kappa;
- whether the empty coalition reproduces the observed choice and therefore the
  observed baseline W1 exactly;
- whether epsilon is used only for BEHAVIOURAL CHOICE and remains excluded from
  the WELFARE RANKING.

2. EX-ANTE / G-COMPUTATION ROUTE

Integrate literal W1-F of the attained bundle over the model-implied
counterfactual choice distribution.

Establish:
- whether this is kappa-invariant;
- whether it yields E[W_i^S] or a distribution of W_i^S;
- whether baseline S=empty reproduces observed welfare or instead a predicted
  expected-attainment object.

For each candidate give:

- exact formula;
- identified inputs;
- treatment of behavioural epsilon;
- kappa dependence;
- baseline reproduction;
- computational burden;
- compatibility with P/A/B/D operators;
- compatibility with grouped Owen/Shapley decomposition.

Also distinguish explicitly between:

    I( E[W_i^S] )

and

    E[ I(W_1^S,...,W_N^S) ].

These are not equivalent.

Recommend ONE primary estimand for the JMP, but do not execute it.

No arbitrary modal-choice rule.
No arbitrary finite-job-count assumption.
No new welfare/decomposition computation before Deputy/PI acceptance.


======================================================================
R6 — SEMINAR
======================================================================

Until the revised F counterfactual pipeline is accepted and run:

DO NOT present old W1-EA welfare/decomposition magnitudes as the paper's W1
results.

The seminar may present:

- data and structural RURO model;
- positive-model estimates and fit;
- evidence for heterogeneous access/earning opportunities;
- Haydar–Maniquet W1 definition;
- the empirical-domain result W1 = staying-home equivalent under F;
- the structural P/A/B/D decomposition architecture;
- revised work-in-progress status of the quantitative welfare decomposition.

If MEASURE-MAP-1 verifies a literal observed-bundle W1-F/W4 distribution in
time, that baseline distribution may be shown.

Use quantitative P/A/B/D shares only if the revised F implementation has been
executed and independently checked before the seminar.

Save Goal 1's immediate response/ruling as:

JMP_W1_fork_ruling_v1.md

Then have it produce:

JMP_measure_map_v1.md
```
