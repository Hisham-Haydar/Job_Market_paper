# Prompt — JMP-M05 Read-Only Source Verification v1

**Tool:** Claude Code  
**Mode:** Read-only  
**Effort:** High  
**Mission:** JMP-M05 design prerequisites

ROLE

Close the factual source gaps identified by `JMP_M05_task_plan_v1.md`.

Do not make statistical-method decisions.
Do not modify source code, configuration, data, accepted artifacts, governance,
or tests.
Do not run gradients, Hessians, optimizers, inference, welfare, decomposition,
EUROMOD, or notebooks.
Do not commit.

READ

- `JMP_M05_task_plan_v1.md`
- `JMP_M05_task_plan_manager_acceptance_v1.md`
- canonical governance files;
- Phase-3 and Phase-4 manager-acceptance memos;
- accepted Phase-3 and Phase-4 manifests and artifacts;
- the exact MNL source at the accepted checkpoint;
- the exact nested dclaborsupply source at its accepted gitlink.

VERIFY REPOSITORY PROVENANCE

Record:

- current `Job_Market_paper` HEAD;
- governance commit SHA;
- committed governance-file list;
- `Job_Market_paper` worktree status;
- MNL HEAD;
- nested dclaborsupply HEAD;
- MNL gitlink;
- clean/dirty status of all three repositories.

REQUIRED FACTUAL OUTPUTS

1. Exact 47-parameter ordering.
2. Exact 37-free ordering.
3. Exact 35-interior ordering after identifying the two active bounds by name.
4. Pin names, values, and source.
5. Bounds, directions, values, and KKT-sign evidence for:
   - `beta_l_age2_sm`
   - `beta_l_age2_sf`.
6. Exact production negLL function and call route.
7. Exact additive likelihood composition and sign.
8. Whether the objective is a sum or mean.
9. Whether survey or frequency weights enter, and how.
10. Primitive likelihood-contribution count.
11. Exact household-group and `idhh` alignment.
12. Whether household clustering is algebraically identical to household OPG in
    this application.
13. Exact regional/access parameter and covariate mapping.
14. Exact Phase-4 bundle filenames and artifact hashes.
15. Authoritative Hessian artifact and CSV/NPY equality after load.
16. JAX x64 and environment facts relevant to score reproduction.
17. Confirmation that accepted artifacts and theta remain unchanged.

BINDING INTERPRETIVE RESTRICTIONS

- Do not infer continuous-density terms merely from average negLL.
- Do not describe the regional/access block as the whole opportunity mechanism.
- Do not claim clustering is non-degenerate or degenerate until the primitive
  contribution structure is verified.
- Mark unsupported statements UNKNOWN.

CREATE

1. `docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md`
2. `docs/France_case/P2a/phase5_parameter_map_v1.csv`
3. `docs/France_case/P2a/phase5_source_inventory_v1.json`

The report must use exactly these headings:

1. Verification verdict
2. Scope
3. Repository provenance
4. Governance provenance
5. Parameter ordering
6. Free and interior maps
7. Active bounds and KKT evidence
8. Fixed pins
9. Likelihood call route
10. Likelihood composition
11. Objective scaling and weighting
12. Primitive contribution and cluster contract
13. Household-ID alignment
14. Regional/access mapping
15. Phase-4 bread provenance
16. Numerical environment
17. Accepted-artifact integrity
18. Remaining unknowns
19. Design-blocking gaps
20. Immediate next action

FINAL VERDICT

Use one:

- SOURCE CONTRACT COMPLETE
- SOURCE CONTRACT COMPLETE WITH NONBLOCKING GAPS
- DESIGN BLOCKED BY SOURCE GAPS

Do not modify or commit anything.
