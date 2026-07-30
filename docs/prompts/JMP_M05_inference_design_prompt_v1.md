# Prompt — JMP-M05 Phase-5 Inference Design v1

Run only after the programme manager accepts `JMP_M05_task_plan_v1.md`.

Use this in **Claude Project 1 — JMP paper and empirical design**.

**Model:** Opus  
**Thinking:** On  
**Mode:** Design only

---

ROLE

Design Phase 5 of the France 2016 singles P2a region-live certification
pipeline: household-clustered statistical inference at the accepted Phase-3
estimate.

This is a design task only.

AUTHORITATIVE ORDER

1. `JMP_canonical_state_v1.md`
2. `JMP_decision_log_v1.md`
3. `JMP_M05_phase5_inference_mission_charter_v1.md`
4. manager-accepted `JMP_M05_task_plan_v1.md`
5. committed manager-acceptance memos and repository evidence
6. project memory

Do not modify code.
Do not compute scores, covariance matrices, standard errors, confidence
intervals, or hypothesis tests.
Do not run Phase 5.
Do not run an optimizer, gradient, Hessian, post-estimation, welfare,
synthetic recovery, EUROMOD, or notebooks.
Do not commit.

BINDING ACCEPTED STATE

MNL checkpoint:

`982c52217031158c4a2368709d4a6b211ebcde76`

Nested dclaborsupply checkpoint and MNL gitlink:

`27756a06ea189339aa82915ed2124628afed20eb`

Accepted Phase-3 bundle SHA-256:

`2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b`

Accepted Phase-4 bundle SHA-256:

`5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`

Accepted estimate:

- France 2016 singles;
- 1,555 household clusters;
- 101 alternatives per household;
- 47 total parameters;
- 37 free parameters;
- 10 fixed pins;
- two free parameters at their accepted lower bounds:
  - `beta_l_age2_sm`
  - `beta_l_age2_sf`;
- negLL: `19053.46553160093`.

Accepted Phase-4 evidence:

- exact 37×37 Hessian of negLL;
- rank 37;
- strictly positive definite;
- minimum eigenvalue `0.1037326963880782`;
- condition number `405353.94719781954`, clean tier;
- regional design 1,555×10, rank 10;
- raw regional subblock positive definite;
- conditional regional Schur complement rank 10 and positive definite.

OBJECTIVE

Produce one implementable and statistically defensible Phase-5 design covering:

1. household-clustered score construction;
2. model-based covariance;
3. cluster-robust sandwich covariance;
4. finite-sample correction;
5. treatment of fixed pins;
6. treatment of the two active-bound parameters;
7. standard errors and tests for the ten regional/access parameters;
8. numerical validation and certification gates;
9. output artifacts and transaction requirements;
10. the boundary between Phase 5 and later synthetic recovery.

CENTRAL DESIGN REQUIREMENT

Recommend one baseline inference specification. Do not present several equally
weighted alternatives.

The baseline must use:

- cluster = household `idhh`;
- number of clusters G = 1,555;
- score contribution = derivative of each household's summed log-likelihood;
- free-vector dimension K = 37;
- bread derived from the accepted free-parameter negLL Hessian;
- meat = sum over household outer products of household log-likelihood scores;
- a sign convention consistent with negLL versus log-likelihood;
- a justified finite-sample correction;
- fixed pins excluded from estimated covariance;
- explicit nonstandard treatment of the two active-bound parameters.

REQUIRED CONTENT

A. Define household log-likelihood and negLL contributions and the ordered
37-free score vector.

Retain:

`sum household log-likelihood scores = - gradient of negLL`

and:

`np.allclose(sum_scores, -gradient, atol=1e-8, rtol=1e-8)`.

Explain an efficient score-construction route that does not build a
memory-unsafe full row-level Jacobian.

B. Require exactly 1,555 `idhh` clusters. All 101 alternatives for one household
must remain in one contribution. Reject row, person, region, year, or
alternative clustering.

C. Define model covariance from the accepted negLL Hessian and explain why no
additional sample scaling is applied. Require stable solves or Cholesky methods.

D. Define:

\[
B=H^{-1}, \qquad
M=\sum_g s_gs_g', \qquad
V_{CR0}=BMB.
\]

Make one recommendation among:

- CR0 as the certified baseline;
- cluster-only \(G/(G-1)\);
- a justified two-factor correction.

Do not mechanically import a regression correction with an incoherent N.

E. Treat the two active-bound parameters explicitly. Distinguish:

1. unrestricted 37-dimensional local covariance;
2. covariance conditional on treating the bound parameters as fixed;
3. one-sided or nonstandard boundary inference;
4. later bootstrap/simulation approaches.

Select the correct covariance object for the 35 interior parameters under the
chosen interpretation. Explain why a 35×35 Hessian inverse, a submatrix of the
full inverse, and a Schur-complement object are not generally identical.

F. Exclude the ten fixed pins from differentiation and covariance estimation.
Recommend NA rather than zero standard errors unless a stronger reason exists.

G. Define inference for:

- `beta_E_gsur`;
- `beta_E_drgn2` through `beta_E_drgn8`;
- `beta_E_drgur`;
- `beta_E_drgmd`.

Specify model and robust standard errors, covariance/correlation submatrices,
individual Wald diagnostics, and one ten-degree-of-freedom joint test. Do not
interpret coefficients causally.

H. Specify production gates for:

- score shape 1555×37;
- finite values;
- cluster count and completeness;
- aggregate score identity;
- fresh-process reproduction;
- parameter-order fingerprint;
- accepted Hessian fingerprint;
- meat symmetry and PSD;
- model covariance symmetry and PD;
- robust covariance symmetry and PSD;
- finite nonnegative diagonals;
- valid correlations;
- regional covariance rank;
- joint-Wald computability;
- unchanged input hashes;
- no optimizer call;
- bitwise unchanged theta and pins.

Use exact tolerances where justified and reuse certified tolerances when
possible.

I. Specify the immutable Phase-5 bundle. Decide whether the 1555×37 score matrix
is committed as CSV, committed as binary, or stored as a hashed binary artifact
with committed summaries.

J. Specify dry-run/real execution, review binding, accepted Phase-3 and Phase-4
dependencies, lock/staging/attempts/complete behavior, post-evaluation recheck,
and one-run rule. Keep this at research-grade reproducibility rather than
production-security maximalism.

K. State that Phase 5 does not contain or replace synthetic recovery. Welfare
and decomposition remain blocked until the recovery gate passes.

CREATE

`docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v1.md`

Use exactly these headings:

1. Design verdict
2. Scope
3. Accepted dependencies
4. Inferential target
5. Household score definition
6. Cluster definition
7. Parameter ordering and mapping
8. Model-based covariance
9. Cluster-robust covariance
10. Finite-sample correction
11. Active-bound parameters
12. Fixed pins
13. Regional-block inference
14. Score validation gates
15. Covariance validation gates
16. Numerical tolerances
17. Required output artifacts
18. Transaction and execution contract
19. Synthetic-recovery boundary
20. Interpretation limits
21. Implementation sequence
22. Decisions requiring manager approval
23. Immediate next action

FINAL VERDICT

Use exactly one:

- READY FOR MANAGER REVIEW
- READY WITH OPEN DECISIONS
- BLOCKED

Do not implement Phase 5.
Do not run inference.
Do not commit.
