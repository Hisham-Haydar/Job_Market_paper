LOCAL-STATE RULE

Do not reset, checkout, stash, clean, or otherwise alter any repository.
The listed commit hashes are reference anchors, not instructions to roll back.
Record the actual local branch, HEAD, ahead/behind status, and working-tree status.
If the local repository is newer than the reference commit, audit the actual current
local state and report the divergence explicitly.

ROLE

Act as a read-only cross-repository auditor for an economics Job Market Paper.

REPOSITORIES AND FIXED REVISIONS

1. dclaborsupply-monorepo
   repository: Hisham-Haydar/dclaborsupply-monorepo
   branch: main
   expected commit: 6bcbc922cd048906cc91c4f93a3ffc4237791b69

2. MNL
   repository: Hisham-Haydar/MNL
   branch: main
   expected commit: 0daab084a591df59da1807c41bf05fc664e2dca6

3. Job_Market_paper
   repository: Hisham-Haydar/Job_Market_paper
   branch: main
   expected commit: c7a8cad98cd375b061c4ea2ba0e1752ef5728ee4

PURPOSE

Prepare a canonical current-state handoff to the main JMP prompting and project manager.

The project has three repositories with overlapping and potentially stale documentation. Determine the actual current state from repository contents, committed artifacts, git history and locally available outputs.

Do not run estimation.
Do not run EUROMOD.
Do not modify code, data, specifications, notebooks, results or existing documentation.
Do not authorize welfare, promotion or replacement of any baseline.

CENTRAL PROJECT BOUNDARY

This is the empirical structural JMP on latent jobs, money-metric welfare and access/ability/preference decomposition.

It is distinct from the separate Haydar–Maniquet pure theory paper.

OBJECTS TO RECONCILE

A. Certified pooled baseline:
- 47-param pooled specification joint_pooled_v1_bll0_tlmpin;
- France 2015–2017;
- JAX;
- synthetic recovery;
- singles 101 alternatives;
- couples 901 alternatives;
- certified negLL approximately 238504.636097.

B. Historical MNL branches:
- continuous RURO;
- job-choice RURO;
- corrected pooled P3a;
- NC couples pilot;
- legacy GAMSPy/CONOPT paths.

C. Current FR 2016 singles P2a work:
- fr_data_walkthrough.ipynb;
- fr_singles_pipeline_v1.ipynb;
- P2a B-pool draws;
- W1 occupation-conditioned proposal;
- region-dead result approximately 19071.6562;
- region-live repaired result approximately 19053.4655.

D. Welfare and writing:
- JMP_project_state_v1.md;
- JMP_welfare_spec_v5.md;
- current literature indexes;
- literature-review skeleton;
- any welfare scaffold or implementation files.

QUESTIONS TO ANSWER

1. Verify all three repositories are at the expected commits.
2. Assign one authoritative role to each repository:
   - research/writing;
   - certified provenance and legacy pipeline;
   - reusable package/application layer.
3. Identify all documentation that is materially stale or contradictory.
4. Determine the formal active JMP baseline.
5. Determine the status of the FR 2016 singles P2a track:
   - exploratory;
   - diagnostic;
   - production candidate;
   - accepted robustness result;
   - or replacement candidate.
6. Determine whether the region-live repair exists only in
   fr_data_walkthrough.ipynb or also in reusable code.
7. Determine whether fr_singles_pipeline_v1.ipynb still reproduces only the
   region-dead 19071.6562 result.
8. Locate any committed or local artifacts for the region-live result:
   - engine-ready parquet metadata;
   - theta CSV;
   - estimation JSON;
   - optimizer status;
   - gradient;
   - Hessian/eigenvalues;
   - bound diagnostics;
   - cluster-robust SE;
   - post-estimation report;
   - provenance record;
   - cold-reload regression anchor.
9. Inspect the active P2a YAML/spec and determine whether:
   - structural wage_spec is standard vw;
   - loc_empirical is used structurally;
   - vw_occupation is used structurally;
   - occupation conditioning belongs only to the proposal;
   - the active path is compatible with the validated JAX engine.
10. Determine whether GSUR, drgn1 and urbanisation are populated in:
    - source data;
    - engine-ready output;
    - core loader arrays;
    - likelihood index.
11. Determine whether the region-live improvement reflects:
    - a corrected data-wiring bug;
    - a specification change;
    - or both.
12. Determine whether region and urbanisation parameters are jointly identified:
    rank, smallest eigenvalues, condition number and flat-direction loadings.
13. Determine whether the region-live model should be:
    - frozen and fully diagnosed;
    - rebuilt through production code first;
    - rejected;
    - or retained only as an exploratory diagnostic.
14. Identify local output artifacts excluded from git that the manager must receive.
15. Identify stale root files in Job_Market_paper and MNL that could mislead Claude/RAG.
16. Identify accidental repository corruption or malformed documentation, including
    the altered line in MNL/files_structure_detailed.md.
17. State exactly one immediate next gate.

CREATE

1. Job_Market_paper/docs/JMP_cross_repo_manager_handoff_v1.md
2. Job_Market_paper/docs/JMP_cross_repo_artifact_manifest_v1.md
3. Job_Market_paper/docs/JMP_cross_repo_documentation_staleness_audit_v1.md
4. Job_Market_paper/docs/JMP_open_decisions_cross_repo_v1.md
5. dclaborsupply-monorepo/docs/validation/FR_P2a_region_live_promotion_readiness_v1.md

JMP_cross_repo_manager_handoff_v1.md headings:

1. Repository identities
2. Repository role allocation
3. Current JMP research question
4. Current contribution
5. Formal active baseline
6. Current pooled-estimation status
7. Current singles-P2a status
8. Current couples status
9. Current welfare status
10. Current literature and writing status
11. Accepted results
12. Provisional results
13. Diagnostic-only results
14. Superseded or invalid results
15. Cross-repository contradictions
16. Current blocker
17. Recommended next gate
18. Files the manager must inspect

JMP_cross_repo_artifact_manifest_v1.md must list for every important artifact:

- repository;
- path;
- track;
- producing code;
- upstream data;
- status: canonical / accepted / provisional / diagnostic / superseded / invalid;
- headline statistic;
- safe for warm start: yes/no;
- safe for inference: yes/no;
- safe for writing: yes/no;
- safe for welfare: yes/no;
- caveats.

JMP_cross_repo_documentation_staleness_audit_v1.md must identify:

- stale research question language;
- obsolete two-factor opportunity/preference language;
- documents incorrectly saying the model is not estimated;
- obsolete baselines;
- stale active-results registries;
- misleading Claude instructions;
- accidental file corruption;
- exact proposed replacement or archival action.

JMP_open_decisions_cross_repo_v1.md must separate:

- central now;
- useful later;
- deferred extensions;
- directions not worth pursuing now.

FR_P2a_region_live_promotion_readiness_v1.md headings:

1. Audit verdict
2. Source notebook evidence
3. Production-pipeline evidence
4. Data and wiring changes
5. Specification compatibility
6. JAX support status
7. Likelihood comparison
8. Convergence status
9. Gradient status
10. Hessian/rank status
11. Bound status
12. Cluster-robust inference status
13. Post-estimation status
14. Reproducibility status
15. Missing artifacts
16. Promotion decision
17. Required next action

FINAL VERDICTS

For the cross-repository handoff:
- COHERENT
- COHERENT WITH DOCUMENTATION REPAIRS
- NOT YET COHERENT

For P2a region-live:
- READY FOR STRICT ESTIMATION VERDICT
- READY AFTER PRODUCTION REBUILD
- DIAGNOSTIC ONLY
- REJECT

RULES

- File and artifact evidence overrides prose claims.
- A notebook cell is not a production pipeline.
- An improved likelihood is not sufficient for promotion.
- A positive-definite real-data Hessian is not sufficient without recovery or
  a clearly narrower diagnostic interpretation.
- Distinguish proposal occupation conditioning from structural occupation-wage modelling.
- Do not declare welfare readiness.
- Do not change the active baseline.
- Do not run any computational pipeline.
- Report missing local-only artifacts explicitly.
