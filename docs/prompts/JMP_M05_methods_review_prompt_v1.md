# Prompt — JMP-M05 Independent Statistical-Methods Review v1

**Reviewer:** separate reasoning chat from the design author and task manager  
**Preferred model:** Opus or equivalent high-capability reasoning model  
**Mode:** Independent, read-only

ROLE

Independently review the final JMP-M05 Phase-5 inference design.

Do not edit the design memo.
Do not write code.
Do not compute empirical inference.
Do not run any repository operation.
Do not defer to the author's preferred answer merely because it is internally
consistent.

READ

- canonical governance files;
- JMP-M05 mission charter;
- task plan;
- task-plan manager acceptance;
- final source-verification report and evidence files;
- final Phase-5 inference-design memo;
- Phase-3 and Phase-4 manager-acceptance memos;
- accepted Phase-4 diagnostics.

REVIEW QUESTIONS

1. Is the household score defined from the exact verified likelihood
   contribution and scaling?
2. Is the score sign convention correct?
3. Is the score aggregation identity correct?
4. Is cluster-versus-OPG terminology accurate for the verified primitive
   contribution structure?
5. Is the proposed finite-sample correction defined with coherent G, N, and K?
6. Is the correction appropriate for an M-estimation sandwich rather than copied
   mechanically from linear regression?
7. Is the model-based bread correctly scaled and sourced from the accepted
   Hessian?
8. Is the robust meat constructed at the correct primitive/cluster level?
9. Is the treatment of the two active-bound parameters defensible?
10. Is the 35-dimensional covariance object the correct object for the stated
    conditional interpretation?
11. Are the limitations of conditioning on the active set explicit?
12. Are symmetric Wald claims correctly prohibited for the bound parameters?
13. Are pins reported as restrictions rather than estimates?
14. Are the ten regional/access parameters described as one opportunity channel,
    not the complete opportunity mechanism?
15. Are individual and joint Wald tests correctly formed and indexed?
16. Are PSD, rank, symmetry, score-identity, and fingerprint gates adequate?
17. Is the score artifact choice reproducible and proportionate?
18. Does the design remain separate from synthetic recovery and welfare
    decomposition?
19. Are any paper-facing claims stronger than the design supports?
20. Is the design implementable without reopening the accepted specification?

TARGETED CORRECTIONS TO CHECK

- The average-negLL diagnostic must not be treated as proof of density terms.
- Regional-block significance must not be equated with the full opportunity
  decomposition.
- Claims about when clustering becomes non-degenerate must be conditional.
- Boundary inference must not be treated as ordinary unconstrained Wald
  inference.

CREATE

`docs/France_case/P2a/FR_P2a_region_live_phase5_inference_methods_review_v1.md`

Use exactly these headings:

1. Review verdict
2. Scope
3. Sources reviewed
4. Likelihood and score definition
5. Cluster interpretation
6. Model-based covariance
7. Robust covariance
8. Finite-sample correction
9. Active-bound parameters
10. Fixed pins
11. Regional/access inference
12. Numerical gates
13. Artifact and transaction contract
14. Interpretation limits
15. Implementation feasibility
16. Residual defects
17. Required fixes
18. Whether manager acceptance may proceed
19. Immediate next action

FINAL VERDICT

Use one:

- APPROVE
- APPROVE AFTER FIXES
- REJECT

Do not modify any source file.
