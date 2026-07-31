# Prompt — JMP-M05 Source Verification v2

**Tool:** Claude Code  
**Preferred model:** Opus  
**Fallback model:** Sonnet  
**Thinking:** On  
**Effort:** High  
**Mode:** Source-audit; existing files read-only; three report files may be created  
**Mission:** JMP-M05 Stage A

ROLE

Close the factual source gaps identified by `JMP_M05_task_plan_v1.md`.

This is a repository source audit, not a statistical-design task.

You may inspect all three repositories and Git history. You may create exactly
the three report files listed under CREATE. You may not modify any existing
source, configuration, test, data, accepted artifact, governance, mission, or
prompt file. Do not commit.

WORKSPACE

Use a workspace with access to all three working trees:

- `Job_Market_paper`
- `MNL`
- `MNL/dclaborsupply-monorepo`

Prefer the common parent workspace containing `Job_Market_paper` and `MNL`.
If the repositories are not siblings or any tree is inaccessible, stop and
report the actual paths required. Do not guess.

READ FIRST

From `Job_Market_paper`:

- `docs/governance/JMP_program_governance_v1.md`
- `docs/governance/JMP_management_hierarchy_and_delegation_v1.md`
- `docs/governance/JMP_canonical_state_v1.md`
- `docs/governance/JMP_decision_log_v1.md`
- `docs/missions/JMP_M05_phase5_inference_mission_charter_v1.md`
- `docs/missions/JMP_M05_task_plan_v1.md`
- `docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md`
- `docs/missions/JMP_M05_mission_ledger_v1.md`

From MNL:

- Phase-3 manager acceptance;
- Phase-4 execution report and manager acceptance;
- accepted Phase-3 and Phase-4 manifests and artifacts;
- production runner, config, specification, parameter map, accepted theta,
  likelihood, loader, bounds, and score-related sources.

From nested `dclaborsupply`:

- the exact loader, likelihood, utility/opportunity, parameter-map, grouping,
  and JAX-configuration sources used by the accepted MNL checkpoint.

Verify exact paths rather than assuming filenames.

BINDING REVISIONS

Expected MNL accepted checkpoint:

`982c52217031158c4a2368709d4a6b211ebcde76`

Expected Phase-4 execution revision:

`fee60723ed27d6979976a3dc85b09cde3096e011`

Expected nested dclaborsupply HEAD and MNL gitlink:

`27756a06ea189339aa82915ed2124628afed20eb`

Expected Phase-3 bundle:

`2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b`

Expected Phase-4 bundle:

`5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`

PROHIBITED OPERATIONS

Do not:

- modify any existing file;
- run an optimizer;
- evaluate a new gradient or Hessian;
- compute covariance matrices, standard errors, tests, welfare, or decomposition;
- run EUROMOD;
- run notebooks;
- regenerate data or draws;
- alter theta, pins, artifacts, or specifications;
- commit, amend, reset, rebase, clean, or delete.

Static imports and lightweight metadata/hash checks are permitted only when
they cannot trigger prohibited numerical work.

VERIFY REPOSITORY PROVENANCE

Record:

1. current `Job_Market_paper` HEAD;
2. governance checkpoint commit SHA;
3. exact committed governance/mission/prompt file list relevant to JMP-M05;
4. `Job_Market_paper` pre-audit worktree status;
5. MNL HEAD;
6. nested dclaborsupply HEAD;
7. MNL gitlink;
8. pre-audit status of MNL and nested repository;
9. whether `982c5221...` is a descendant of `fee60723...`;
10. intervening commits and their changed-file summaries.

REQUIRED FACTUAL OUTPUTS

### Parameter contract

1. Exact ordered 47-parameter vector.
2. Exact ordered 37-free vector.
3. Exact ordered 35-interior vector after removing the two active-bound
   parameters by verified name.
4. Name, value, role, and source for all ten pins.
5. Bounds, directions, accepted values, and KKT-sign evidence for:
   - `beta_l_age2_sm`;
   - `beta_l_age2_sf`.

### Likelihood and score contract

6. Exact production negLL function and complete call route.
7. Exact additive likelihood composition, term by term and with signs.
8. Whether the production objective is a sum, mean, weighted sum, or another
   scaling.
9. Whether survey, frequency, or other weights enter, and exactly where.
10. Primitive likelihood-contribution count.
11. Exact relationship among:
    - alternative rows;
    - household choice blocks;
    - person/decision-maker records;
    - `idhh`;
    - the 1,555 accepted clusters.
12. Whether one household is one primitive score contribution in the accepted
    singles application.
13. Whether household-cluster covariance is algebraically identical to a
    household-level OPG sandwich in this application.

### Regional/access contract

14. Exact names and free-vector positions of:
    - `beta_E_gsur`;
    - `beta_E_drgn2` through `beta_E_drgn8`;
    - `beta_E_drgur`;
    - `beta_E_drgmd`.
15. Exact loader covariates and omitted/reference categories.
16. State explicitly that this is the regional/urbanisation/GSUR access block,
    not the complete opportunity mechanism.

### Phase-4 bread and numerical environment

17. Exact Phase-4 complete-bundle filenames.
18. Recompute the bundle hash.
19. Identify the authoritative Hessian artifact.
20. Verify CSV/NPY numerical equality after loading.
21. Record dtype, JAX x64 initialization point, JAX version, NumPy version,
    Python version, and platform facts relevant to score reproduction.
22. Confirm accepted theta, pins, manifests, and result artifacts are unchanged.

INTERPRETIVE RESTRICTIONS

- Do not infer likelihood composition from average negLL.
- Do not treat `ln(101)` as a proven objective bound without source proof.
- Do not describe the ten regional/access parameters as all opportunity
  heterogeneity.
- Do not make a finite-sample-correction choice.
- Do not choose an active-bound inference method.
- Do not make methodological recommendations.
- Mark unsupported facts `UNKNOWN`.

CREATE EXACTLY

In the MNL repository:

1. `docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md`
2. `docs/France_case/P2a/phase5_parameter_map_v1.csv`
3. `docs/France_case/P2a/phase5_source_inventory_v1.json`

Do not create or modify any other file.

The report must use exactly these headings:

1. Verification verdict
2. Scope
3. Repository provenance
4. Governance provenance
5. Revision descendancy
6. Parameter ordering
7. Free and interior maps
8. Active bounds and KKT evidence
9. Fixed pins
10. Likelihood call route
11. Likelihood composition
12. Objective scaling and weighting
13. Primitive contribution and cluster contract
14. Household-ID alignment
15. Regional/access mapping
16. Phase-4 bread provenance
17. Numerical environment
18. Accepted-artifact integrity
19. Remaining unknowns
20. Design-blocking gaps
21. Files created
22. Immediate next action

FINAL VERDICT

Use exactly one:

- SOURCE CONTRACT COMPLETE
- SOURCE CONTRACT COMPLETE WITH NONBLOCKING GAPS
- DESIGN BLOCKED BY SOURCE GAPS

POST-AUDIT STATUS

Report:

- all three repository statuses;
- exact three created files;
- confirmation that no pre-existing file changed;
- confirmation that no commit occurred.

Stop.
