# MISSION JMP-M08 — France 2016 Singles Welfare Integration and Baseline Decomposition Prototype

**Programme:** Goal 1 — Empirical JMP  
**Manager:** Goal 1 Manager — Empirical JMP  
**Mission type:** Welfare integration, money-metric measurement, structural inequality decomposition  
**Status:** Authorized  
**Primary empirical scope:** France 2016 single-adult households, P2a region-live  
**Sample:** 1,555 households  
**Estimation:** Frozen; no re-estimation authorized  
**Final quantitative freeze:** Not authorized until LOC4 closes

## 1. Mission objective

Produce the first accepted, paper-usable baseline prototype that carries the same latent-job opportunity structure through:

1. ex-ante attained utility;
2. money-metric welfare;
3. inequality measurement;
4. an order-independent access/ability/preference decomposition.

The mission must validate the welfare integration for the 101-alternative singles grids before promoting any welfare number. It then computes the configured welfare-measure family and a baseline Shapley–Shorrocks decomposition under the certified P2a model, followed by the exact pre-registered S-10 Tier-1 sensitivity.

## 2. Governing hierarchy

The following control M08, in this order:

1. `JMP_M07_deputy_closeout_and_identity_ruling_v1.md`;
2. `JMP_M08_welfare_input_handoff_v1.md`;
3. `JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md`;
4. `JMP_LOC4_pathB_ruling_v1.md`;
5. accepted P2a estimation/inference artifacts and manifests;
6. `JMP_welfare_spec_latest.md`;
7. `RURO_welfare_scaffold_design_contract_v2.md` and accepted welfare-validation artifacts, where they exist.

Where the older welfare memo or project-state document assumes pooled years or couples, M08 rebinds the existing generic welfare machinery to the accepted France 2016 P2a singles application. It does not import couples-specific empirical claims, reference rules, or validation status without revalidation.

Management memos are context, not numerical data sources.

## 3. Frozen accepted inputs

Use only the exact full hashes resolved from the accepted manifests and handoff:

- P2a accepted 47-coordinate parameter vector:
  - 35 interior;
  - 2 active upper bounds;
  - 10 pins;
- accepted Phase-3 parameter bytes and bundle;
- accepted Phase-4 Hessian/bread;
- accepted Phase-5 conditional robust covariance and reporting artifacts;
- accepted P2a engine-ready alternatives and per-row proposal correction;
- accepted model/specification and package gitlink;
- accepted M07 inference backbone.

A truncated hash in a memo is not sufficient for execution. Stage A must resolve and record the exact full identifiers.

## 4. Binding economic objects

### 4.1 Attained utility

For household \(i\),

\[
V_i =
\log\sum_{j\in\mathcal C_i}
\exp\left[
u_i(c_{ij},\ell_{ij};\theta^{pref})
+\log g(j;x_i,\theta^{opp})
-\log\pi(j;x_i)
\right].
\]

The mandatory proposal correction remains at the alternative level. The welfare path must reuse the accepted estimator's utility and opportunity-density construction rather than reimplementing a parallel formula.

### 4.2 Welfare family

Exercise A computes the configured money-metric family \(W^1,\ldots,W^6\), subject to the frozen build order and reference-coverage gates.

- Primary build/validation anchor: \(W^3\).
- Full-Responsibility check: \(W^2\).
- One-sided access/ability duals: \(W^5\) and \(W^1\).
- Full-Compensation endpoints: \(W^4\) and \(W^6\).

The JMP imports the measures and their normative readings as cited primitives. It does not reproduce the companion theory paper's proofs or claim its axiomatic results as JMP contributions.

### 4.3 Decomposition

Exercise B uses Shapley–Shorrocks to allocate inequality in the money-metric welfare vector to:

- **access:** employment/hours availability, regional/urbanisation/GSUR environment, occupation availability, and other accepted non-wage offer terms;
- **ability:** accepted wage technology and productivity distribution, including education/experience returns and wage dispersion;
- **preference:** accepted tastes over consumption, leisure, and job packages.

The primary source decomposition is anchored on \(W^3\). \(W^2\) is the pre-registered second check. The \(W^1/W^5\) dual is corroborating interpretation, not a numerical reconciliation identity.

Report:

- access-only opportunity content;
- access-plus-ability opportunity content;
- preference-related content.

Do not label the preference-related component as responsibility. Do not describe any component as causal.

## 5. Strategic scope rulings

1. **Singles only.** No couples, pooled-year, or other-country welfare result.
2. **2016 P2a production path only.** The older full year×mode parity requirement is deferred.
3. **No re-estimation.** Counterfactual equalisation and S-10 alter welfare inputs/functions only.
4. **Point-estimate prototype.** M08 does not freeze final quantitative magnitudes and does not substitute asymptotic delta-method inference for the later bootstrap.
5. **LOC4 after M08.** The certified common-dispersion wage specification is the M08 baseline. LOC4 remains mandatory before final quantitative claims.
6. **No package-source modification by default.** A required generic `dclaborsupply` change is an escalation, not an implicit M08 edit.
7. **No post-hoc factor definitions, reference sets, subgroup lists, or thresholds.** Stage A freezes them before any result is computed.

## 6. Mandatory pre-execution contract — Stage A

Before numerical welfare execution, create:

`docs/missions/JMP_M08_singles_welfare_execution_contract_v1.md`

It must record:

- exact repository revisions and full artifact hashes;
- exact P2a sample and alternative geometry;
- exact welfare code paths/modules to be reused;
- exact active measure set and build order;
- exact definitions of every measure-specific reference:
  - non-employment option \(o\);
  - reference set \(\bar A\);
  - universal job set \(\mathcal J\);
- exact access, ability, and preference parameter membership;
- exact equalisation/reference operator for each channel;
- exact inequality index:
  - welfare Gini as required;
  - any second headline index, if already pre-registered;
- exact subgroup list already pre-registered;
- exact welfare-integration thresholds from the frozen scaffold contract:
  - engine parity;
  - reprice parity;
  - effective sample size;
  - direct-versus-importance-sampling agreement;
  - draw-growth stability;
  - inversion convergence;
  - reference coverage;
  - Shapley exhaustiveness;
- exact persistence/disclosure policy for household-level welfare vectors;
- exact production output namespace selected from existing MNL conventions;
- exact S-10 numerical perturbations and four scenario vectors, recorded before execution;
- the vigilance treatment for `beta_l0_sf`.

If an exact threshold, reference rule, operator, or required contract is absent or internally inconsistent, halt before execution and return a bounded design conflict. Do not invent it.

## 7. Work stages

### Stage 0 — M07 closeout and M08 state inventory

**Tool:** Claude Code  
**Model:** Sonnet  
**Thinking:** On  
**Effort:** Medium  
**Repositories:**
- `Job_Market_paper`: write only M07 closeout and authorized M08 governance outputs;
- `MNL`: read-only;
- `dclaborsupply-monorepo`: read-only.

Tasks:

1. commit the accepted M07 packet in one documentation-only checkpoint after hash verification;
2. inventory all existing welfare code, contracts, tests, validation artifacts, and unresolved blockers;
3. identify which prior objects are pooled/couples-specific and which are reusable for P2a singles;
4. produce the Stage-A execution contract draft.

No welfare computation.

### Stage A — independent contract/economics review

**Tool:** separate Claude Project chat  
**Model:** Opus  
**Thinking:** On  
**Effort:** High  
**Writes:** none

Review the execution contract for:

- consistency with the frozen handoff;
- exact access/ability/preference cut;
- measure/decomposition non-double-counting;
- singles rebasing;
- reference-set validity;
- S-10 and LOC4 obligations;
- absence of theory-paper leakage.

The Goal 1 Manager resolves routine issues and freezes the contract.

### Stage B — reprice-parity diagnosis and bounded correction

**Tool:** Claude Code  
**Model:** Opus  
**Thinking:** On  
**Effort:** High  
**Write authority:**
- MNL France-application welfare code and tests only;
- no `dclaborsupply` package-source modification.

Required order:

1. reproduce the documented P2a singles reprice-parity failure on accepted existing nodes;
2. characterize failing rows before changing code:
   - household concentration;
   - node concentration;
   - roster/covariate signatures;
   - income and benefit components;
   - record identifiers and ordering;
   - missing preprocessing transformations;
3. classify the defect as:
   - uniform/mechanical and repairable; or
   - structural/type-specific;
4. apply only the smallest production-path correction supported by the diagnosis;
5. rerun parity on every existing France 2016 P2a node that the redraw path will touch;
6. produce a change/evidence packet.

**Gate:** no redrawn node and no paper-facing welfare number may be produced until the exact frozen reprice-parity gate passes.

If the failure is structural or the repair requires a generic package change, halt and escalate.

### Stage C — bounded independent production-path review

**Tool:** Codex / GPT-5.6 Codex  
**Mode:** read-only independent review  
**Reasoning:** High  
**Scope:** only the changed production path, parity evidence, accepted-input binding, proposal correction, and artifact persistence.

This is one bounded review. Do not reopen general software architecture or prior Phase-5 certification.

### Stage D — welfare-integration certification

**Tool:** Claude Code  
**Model:** Opus  
**Thinking:** On  
**Effort:** High

Execute only after Stages A–C pass:

1. reproduce estimator/welfare engine parity at accepted P2a \(\hat\theta\);
2. compute and record household ESS diagnostics;
3. run the pre-registered redraw-from-\(\hat g_i\) cross-check on the flagged set;
4. run the pre-registered draw-growth stability check;
5. apply the exact escalation rule from the frozen contract;
6. verify inversion convergence and numerical invariances;
7. record a restricted-artifact manifest.

If the singles integration gate fails, no welfare distribution is accepted.

### Stage E — baseline welfare family

Compute the configured \(W^1,\ldots,W^6\) family in the frozen build order.

For each measure report at least:

- household count and validity count;
- mean;
- median;
- welfare Gini;
- second headline inequality index, if pre-registered;
- selected quantiles;
- pre-registered subgroup summaries;
- inversion/reference-coverage diagnostics;
- measure-ranking or reranking summaries only if pre-registered.

No stochastic-dominance exercise unless separately authorized.

### Stage F — baseline three-way decomposition

Using the frozen operators:

1. evaluate the eight coalitions of the three-channel Shapley game for the primary \(W^3\) decomposition;
2. compute exact Shapley contributions for access, ability, and preference;
3. verify exhaustiveness to the frozen numerical tolerance;
4. report access-only and access-plus-ability shares;
5. repeat the pre-registered \(W^2\) second check;
6. report \(W^1/W^5\) only as corroborating interpretation.

Every result is model-conditional and non-causal.

### Stage G — exact S-10 Tier-1 sensitivity

Implement exactly four scenarios:

1. accepted baseline;
2. only `beta_l0_sm` perturbed;
3. only `beta_w_pexp2` perturbed;
4. both perturbed jointly.

Hold fixed everything required by the frozen S-10 specification.

For each scenario report the full required welfare, inequality, decomposition, subgroup, convergence, and invariance outputs. Report all continuous changes, including those below thresholds.

Monitor `beta_l0_sf` as a vigilance coordinate without perturbing it or asserting a bound absent accepted evidence.

If any Tier-2 trigger fires, halt final paper-facing interpretation and return to the deputy with a bounded escalation proposal. Do not automatically re-estimate.

### Stage H — economics/statistical review and acceptance

**Independent review tool:** ChatGPT Thinking  
**Model:** GPT-5.6 Thinking  
**Reasoning:** High  
**Writes:** none

Audit:

- claim-to-artifact traceability;
- money-metric interpretation;
- access/ability/preference membership;
- Shapley exactness;
- measure/decomposition non-double-counting;
- S-10 verdict;
- no responsibility or causal overclaim;
- LOC4 sequencing;
- disclosure discipline.

The Goal 1 Manager may authorize one narrow correction cycle, then issue acceptance.

## 8. Required outputs

### Job_Market_paper

1. `docs/missions/JMP_M08_singles_welfare_execution_contract_v1.md`
2. `docs/results/FR_P2a_welfare_integration_validation_v1.md`
3. `docs/results/FR_P2a_welfare_family_results_v1.md`
4. `docs/results/FR_P2a_welfare_decomposition_results_v1.md`
5. `docs/results/FR_P2a_S10_welfare_sensitivity_v1.md`
6. `docs/results/FR_P2a_welfare_reporting_map_v1.csv`
7. `manuscript/sections/FR_P2a_welfare_decomposition_baseline_v1.md`
8. `manuscript/appendices/FR_P2a_welfare_appendix_v1.md`
9. `docs/missions/JMP_M08_independent_economics_review_v1.md`
10. `docs/missions/JMP_M08_goal_manager_acceptance_v1.md`
11. `docs/missions/JMP_M09_LOC4_welfare_robustness_handoff_v1.md`

### MNL

Create the application-specific code, tests, restricted numerical artifacts, manifest, and acceptance pointer in an existing or manager-approved P2a welfare production namespace. Record the exact paths in the execution contract. Do not invent a public repository path in prose before repository inspection.

## 9. Acceptance gates

M08 passes only if:

1. accepted P2a hashes and revisions are bound exactly;
2. reprice parity passes on the complete P2a singles production path;
3. engine parity passes;
4. ESS/redraw/draw-growth gates pass or follow their exact pre-registered escalation rule;
5. every welfare inversion converges or every exception is pre-registered and resolved;
6. reference coverage passes for every active measure;
7. the full configured measure family is produced;
8. W3 Shapley decomposition is exhaustive;
9. W2 second check is produced;
10. access/ability/preference membership is frozen and unchanged after results;
11. S-10 four-scenario sensitivity is complete;
12. no Tier-2 trigger remains unresolved;
13. no household-level welfare or microdata artifact is placed in the public paper repository;
14. the independent economics review passes after at most one narrow correction cycle;
15. every paper-facing magnitude maps to an accepted aggregate artifact.

## 10. Prohibitions

Do not:

- re-estimate any parameter;
- rerun Phase-5 inference;
- use management memos as numerical sources;
- modify accepted M07 v2 text except through a later manuscript-integration mission;
- implement LOC4 inside M08;
- add `lindi`, external regional covariates, new occupation groups, sex-specific wage densities, or policy reforms;
- run pooled/couples welfare;
- conduct broad literature research;
- label preference as responsibility;
- present decomposition as causal;
- use provisional notebook outputs as accepted results;
- silently modify package source;
- generate final quantitative claims before LOC4.

## 11. Halt and escalation conditions

Return to the deputy immediately if:

- reprice parity is structural/type-specific and unresolved;
- accepted P2a inputs cannot be bound;
- a required reference set/operator is undefined;
- a generic package change is required;
- the welfare family cannot be implemented under the accepted theory/JMP boundary;
- an integration gate fails without a frozen escalation rule;
- a Tier-2 S-10 trigger fires;
- Shapley exhaustiveness fails;
- household-level disclosure cannot be controlled;
- LOC4 Path B would need reconsideration.

## 12. Return gate and next mission

Routine stages remain with the Goal 1 Manager.

Return only with:

- M08 acceptance memo;
- welfare-integration validation memo;
- family results memo;
- decomposition results memo;
- S-10 verdict;
- independent review verdict;
- manuscript baseline section;
- M09 LOC4 handoff;
- or an escalation listed in §11.

After M08 succeeds, the next mandatory mission is the LOC4 four-density welfare robustness. Final welfare uncertainty and paper-facing quantitative freeze follow only after the preferred specification is settled.
