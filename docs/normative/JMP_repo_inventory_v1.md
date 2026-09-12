# JMP_repo_inventory_v1.md — CLEAN-B repository inventory (Job_Market_paper, MNL, MNL_posfit)

| Field | Value |
|---|---|
| Mission | CLEAN-B — INVENTORY. READ-ONLY. |
| Generated | 2026-09-12 22:28 local, Claude Code (Opus 5). Mechanical tables computed live from git and file bytes; classification columns are judgments and labelled as such. |
| HEADs | Job_Market_paper `0ff8f748a4791226648344ddca972f2629eed9c6` (docs/w1-reference-domain-fork); MNL `76e2087291640deb0bf1d5a868e3d6756805aa49` (welfare/baseline-f1); MNL_posfit `96b6c883848017f67951ae0d5e2bd7adf2c06cea` (diagnostics/posfit-v2) |
| Writes | This file only. No merge, move, deletion, tag or branch change. |
| Preceding cards | CLEAN-A (tags `pre-cleanup/*/2026-09-12`; `wip/pre-cleanup-*` snapshots); CLEAN-A-VERIFY (41-file quarantine at `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/cleanup_quarantine_2026-09-12/`). |
| Status | INVENTORY. Section 8 recommendations are not authorisations. |

## 1. Branch topology

### MNL

| Branch | HEAD | Upstream | Last commit | Merge-base with main | Ahead | Behind | FF of main to branch? | Subject |
|---|---|---|---|---|---:|---:|---|---|
| `corr/estimator-and-support` | `aa36e816e4` | — | 2026-09-10 | `3162b0858c` | 23 | 0 | **YES** | Repair reader-facing welfare explanations and regenerate outputs |
| `diag/dben-program-attribution` | `e546e38585` | origin/diag/dben-program-attribution | 2026-06-16 | `e546e38585` | 0 | 163 | not needed (main contains it) | diag(D-BEN): program-level attribution of F3 joint-batch benefit wobble |
| `diagnostics/posfit-v2` | `96b6c88384` | — | 2026-09-12 | `3162b0858c` | 30 | 0 | **YES** | diagnostics: classify S12 zero-mass support gaps |
| `feat/ps1-semi-flexible-couples-adapter` | `432929e7c5` | — | 2026-09-03 | `69c8653f4a` | 6 | 70 | **NO — diverged** | feat(sprint): R-233 seminar sprint - scaffold, GPU research bundle, rulings re-pins |
| `handoff/final-rich-contract-v1` | `7783831291` | origin/handoff/final-rich-contract-v1 | 2026-09-07 | `5b0e3d29e2` | 1 | 94 | **NO — diverged** | docs(handoff): export frozen final rich engine contract v1 (bytes of 618b3f3) |
| `main` | `3162b0858c` | origin/main | 2026-09-08 | `3162b0858c` | 0 | 0 | (is main) | feat(sprint): preference figures - indifference curves, marginal utilities, MRS, normalization sensi |
| `welfare/baseline-f1` | `76e2087291` | — | 2026-09-12 | `3162b0858c` | 29 | 0 | **YES** | E3-EQ: equivalised BASELINE-F-1 reporting code and aggregates |
| `wip/pre-cleanup-welfare/baseline-f1` | `5a26cf47a6` | — | 2026-09-12 | `3162b0858c` | 30 | 0 | **YES** | WIP snapshot before cleanup; classification pending |
| `wip/pre-cleanup-worktree-jmp-m08-loc4-stage1` | `960b37bb49` | — | 2026-09-12 | `5b0e3d29e2` | 1 | 94 | **NO — diverged** | WIP snapshot before cleanup; classification pending |
| `worktree-agent-ae939588345df9c31` | `5b0e3d29e2` | — | 2026-08-07 | `5b0e3d29e2` | 0 | 94 | not needed (main contains it) | feat(m08): certify P2a reprice-parity gate - code, evidence, reports v1-v4, reviews, E2 closure |
| `worktree-jmp-m08-loc4-stage1` | `5b0e3d29e2` | — | 2026-08-07 | `5b0e3d29e2` | 0 | 94 | not needed (main contains it) | feat(m08): certify P2a reprice-parity gate - code, evidence, reports v1-v4, reviews, E2 closure |

`main` is 94 ahead / 0 behind `origin/main`.

### Job_Market_paper

| Branch | HEAD | Upstream | Last commit | Merge-base with main | Ahead | Behind | FF of main to branch? | Subject |
|---|---|---|---|---|---:|---:|---|---|
| `docs/seminar-r6` | `4c4e07e398` | — | 2026-09-12 | `425c4c735c` | 2 | 0 | **YES** | E3-EQ: BASELINE-F-1 equivalised reporting memo and verification |
| `docs/w1-reference-domain-fork` | `0ff8f748a4` | — | 2026-09-12 | `425c4c735c` | 3 | 0 | **YES** | docs(dashboard): record Deputy Goal 1 ruling — bridge verdict D accepted, G-WELFARE-1 commissioned |
| `main` | `425c4c735c` | origin/main | 2026-09-11 | `425c4c735c` | 0 | 0 | (is main) | docs(dashboard): MEASURE-MAP-1R ACCEPTED, BASELINE-F-1 UNLOCKED |
| `wip/pre-cleanup-docs/w1-reference-domain-fork` | `6d441b188c` | — | 2026-09-12 | `425c4c735c` | 4 | 0 | **YES** | WIP snapshot before cleanup; classification pending |

`main` is 34 ahead / 0 behind `origin/main`.

### Diverged pairs and unique content

**MNL: `diagnostics/posfit-v2` vs `welfare/baseline-f1`** — merge-base `d729cf895e`; paths changed 119 vs 10; **overlapping paths: 0**.

- only in `diagnostics/posfit-v2` (4): `96b6c883` diagnostics: classify S12 zero-mass support gaps; `a2e80a82` diagnostics: add POSFIT support coverage v2b; `ec02b1db` feat(diagnostics): complete amended POSFIT v2 package; `0255bb98` chore(diagnostics): record POSFIT v2 convergence halt
- only in `welfare/baseline-f1` (3): `76e20872` E3-EQ: equivalised BASELINE-F-1 reporting code and aggregates; `b5550af5` Verify BASELINE-F1 independently; `6048c9f7` Record BASELINE-F1 full-sample aggregates

**Job_Market_paper: `docs/seminar-r6` vs `docs/w1-reference-domain-fork`** — merge-base `425c4c735c`; paths changed 23 vs 7; **overlapping paths: 0**.

- only in `docs/seminar-r6` (2): `4c4e07e` E3-EQ: BASELINE-F-1 equivalised reporting memo and verification; `cafe0ba` docs(seminar): rebuild the deck on R6 content; retire the W1-EA block
- only in `docs/w1-reference-domain-fork` (3): `0ff8f74` docs(dashboard): record Deputy Goal 1 ruling — bridge verdict D accepted, G-WELFARE-1 commissioned; `e278bcd` docs(normative): bridge review + factual items + direct-g welfare ruling; `ce0ee3f` docs(normative): commit W1 stochastic ability set bridge memo (SRC-1)

**MNL: `feat/ps1-semi-flexible-couples-adapter` vs `main`** — merge-base `69c8653f4a`; paths changed 131 vs 1082; **overlapping paths: 80**: `experiments/JMP_PS1/decision_note.md`, `experiments/JMP_PS1/model_comparison.csv`, `experiments/JMP_PS1/runs/ps1w3_wage_pref/.gitignore`, `experiments/JMP_PS1/runs/ps1w3_wage_pref/_run_cells.sh`, `experiments/JMP_PS1/runs/ps1w3_wage_pref/_s3/cell_s0.5_r0.5_01.json`, `experiments/JMP_PS1/runs/ps1w3_wage_pref/_s3/cell_s0.5_r0.5_02.json`, `experiments/JMP_PS1/runs/ps1w3_wage_pref/_s3/cell_s0.5_r0.5_03.json`, `experiments/JMP_PS1/runs/ps1w3_wage_pref/_s3/cell_s0.5_r0.5_04.json`.

- only in `feat/ps1-semi-flexible-couples-adapter` (6): `432929e7` feat(sprint): R-233 seminar sprint - scaffold, GPU research bundle, rulings re-pins; `861f3e18` chore(ps1): record the r6 adapter commit id in the validation JSON; `b9fb98cb` feat(ps1): PKG-03A r6 adapter RE-TEST - 19/19 gates on all three real tests; `ddd4981a` feat(ps1): S9 selection - corrected S8 formally retained; W3 NOT_IDENTIFIED; `f569f060` feat(ps1): W3 feasibility gates (NOT_IDENTIFIED) - wage-residual/preference dependence; `8419dd4c` feat(ps1): PKG-03 semi-flexible couples adapter test - all three real tests pass
- only in `main` (70): `3162b085` feat(sprint): preference figures - indifference curves, marginal utilities, MRS, normalization sensitivity; `bbcc6e04` feat(sprint): final-sample descriptives for singles and couples; relabelled figures; `6a9b1446` docs(sprint): backend profile support, the parity record, and a runtime benchmark cell; `65593f1a` docs(sprint): research lab notebook consistent with gate spec v1; `9cfe67ae` chore(mnl): ignore notebook_dev_v3 staging dir after reference audit; `aa52856d` chore(mnl): .gitignore for the storage layer; param_child audit; figN01 band fix; `a4293a01` feat(sprint): nested endowments/needs (ADMITTED), research lab notebook, close-out; `d8217424` docs(jmp): consistency fixes (gate v1); `c8bb836f` docs(jmp): rebase the deck-side claim checks onto the live content; archive deck content v1; `cb0eb73c` feat(sprint): R-263 the end-to-end chain, ordered so a failure is safe; … +60 more

**MNL: `handoff/final-rich-contract-v1` vs `main`** — merge-base `5b0e3d29e2`; paths changed 1 vs 1698; **overlapping paths: 1**: `docs/handoffs/JMP_final_rich_engine_terms_contract_v1.yaml`.

- only in `handoff/final-rich-contract-v1` (1): `77838312` docs(handoff): export frozen final rich engine contract v1 (bytes of 618b3f3)
- only in `main` (94): `3162b085` feat(sprint): preference figures - indifference curves, marginal utilities, MRS, normalization sensitivity; `bbcc6e04` feat(sprint): final-sample descriptives for singles and couples; relabelled figures; `6a9b1446` docs(sprint): backend profile support, the parity record, and a runtime benchmark cell; `65593f1a` docs(sprint): research lab notebook consistent with gate spec v1; `9cfe67ae` chore(mnl): ignore notebook_dev_v3 staging dir after reference audit; `aa52856d` chore(mnl): .gitignore for the storage layer; param_child audit; figN01 band fix; `a4293a01` feat(sprint): nested endowments/needs (ADMITTED), research lab notebook, close-out; `d8217424` docs(jmp): consistency fixes (gate v1); `c8bb836f` docs(jmp): rebase the deck-side claim checks onto the live content; archive deck content v1; `cb0eb73c` feat(sprint): R-263 the end-to-end chain, ordered so a failure is safe; … +84 more

**MNL: `wip/pre-cleanup-worktree-jmp-m08-loc4-stage1` vs `main`** — merge-base `5b0e3d29e2`; paths changed 4 vs 1698; **overlapping paths: 2**: `scripts/loc4/loc4_spec_extension.py`, `scripts/loc4/loc4_stage1_lib.py`.

- only in `wip/pre-cleanup-worktree-jmp-m08-loc4-stage1` (1): `960b37bb` WIP snapshot before cleanup; classification pending
- only in `main` (94): `3162b085` feat(sprint): preference figures - indifference curves, marginal utilities, MRS, normalization sensitivity; `bbcc6e04` feat(sprint): final-sample descriptives for singles and couples; relabelled figures; `6a9b1446` docs(sprint): backend profile support, the parity record, and a runtime benchmark cell; `65593f1a` docs(sprint): research lab notebook consistent with gate spec v1; `9cfe67ae` chore(mnl): ignore notebook_dev_v3 staging dir after reference audit; `aa52856d` chore(mnl): .gitignore for the storage layer; param_child audit; figN01 band fix; `a4293a01` feat(sprint): nested endowments/needs (ADMITTED), research lab notebook, close-out; `d8217424` docs(jmp): consistency fixes (gate v1); `c8bb836f` docs(jmp): rebase the deck-side claim checks onto the live content; archive deck content v1; `cb0eb73c` feat(sprint): R-263 the end-to-end chain, ordered so a failure is safe; … +84 more

Notes (judgment): `corr/estimator-and-support` is an ancestor of both `welfare/baseline-f1` and `diagnostics/posfit-v2`, which diverge at `d729cf89` (GATE-1 gate): POSFIT v2 package vs full-sample aggregates + verification + E3-EQ code; no shared path. `docs/seminar-r6` (R6 deck, E3-EQ memos) and `docs/w1-reference-domain-fork` (bridge memo, review, SRC-3, direct-g ruling, dashboard) fork from `425c4c7` on disjoint paths. `handoff/final-rich-contract-v1`: `git cherry` marks its commit patch-equivalent to one on `main`, whose YAML has since changed. `feat/ps1-semi-flexible-couples-adapter`: 6 non-equivalent commits; 58 of its changed files differ from `main`, 73 are identical — stale. `diag/dben-program-attribution` and both `worktree-*` branches are contained in `main`. `wip/pre-cleanup-*` are CLEAN-A snapshots.

### Cited commits — reachability

| Commit | Repo | Reachable from | On main? |
|---|---|---|---|
| `8a4df81a7a` | Job_Market_paper | `docs/seminar-r6`, `docs/w1-reference-domain-fork`, `main`, `wip/pre-cleanup-docs/w1-reference-domain-fork` | yes |
| `d58f93b11a` | Job_Market_paper | `docs/seminar-r6`, `docs/w1-reference-domain-fork`, `main`, `wip/pre-cleanup-docs/w1-reference-domain-fork` | yes |
| `8dcc476b60` | Job_Market_paper | `docs/seminar-r6`, `docs/w1-reference-domain-fork`, `main`, `wip/pre-cleanup-docs/w1-reference-domain-fork` | yes |
| `acf33c645f` | Job_Market_paper | `docs/seminar-r6`, `docs/w1-reference-domain-fork`, `main`, `wip/pre-cleanup-docs/w1-reference-domain-fork` | yes |
| `f6346232ef` | Job_Market_paper | `docs/seminar-r6`, `docs/w1-reference-domain-fork`, `main`, `wip/pre-cleanup-docs/w1-reference-domain-fork` | yes |
| `834055e8da` | Job_Market_paper | `docs/seminar-r6`, `docs/w1-reference-domain-fork`, `main`, `wip/pre-cleanup-docs/w1-reference-domain-fork` | yes |
| `cafe0ba019` | Job_Market_paper | `docs/seminar-r6` | **no** |
| `ce0ee3f76f` | Job_Market_paper | `docs/w1-reference-domain-fork`, `wip/pre-cleanup-docs/w1-reference-domain-fork` | **no** |
| `e278bcd5f7` | Job_Market_paper | `docs/w1-reference-domain-fork`, `wip/pre-cleanup-docs/w1-reference-domain-fork` | **no** |
| `838127e05c` | MNL | `diagnostics/posfit-v2`, `welfare/baseline-f1`, `wip/pre-cleanup-welfare/baseline-f1` | **no** |
| `6864468029` | MNL | `diagnostics/posfit-v2`, `welfare/baseline-f1`, `wip/pre-cleanup-welfare/baseline-f1` | **no** |
| `d729cf895e` | MNL | `diagnostics/posfit-v2`, `welfare/baseline-f1`, `wip/pre-cleanup-welfare/baseline-f1` | **no** |
| `6048c9f740` | MNL | `welfare/baseline-f1`, `wip/pre-cleanup-welfare/baseline-f1` | **no** |
| `b5550af594` | MNL | `welfare/baseline-f1`, `wip/pre-cleanup-welfare/baseline-f1` | **no** |
| `aa36e816e4` | MNL | `corr/estimator-and-support`, `diagnostics/posfit-v2`, `welfare/baseline-f1`, `wip/pre-cleanup-welfare/baseline-f1` | **no** |
| `1cf57ddc87` | MNL | `corr/estimator-and-support`, `diagnostics/posfit-v2`, `welfare/baseline-f1`, `wip/pre-cleanup-welfare/baseline-f1` | **no** |
| `0255bb986d` | MNL | `diagnostics/posfit-v2` | **no** |
| `a2e80a8264` | MNL | `diagnostics/posfit-v2` | **no** |
| `55bb0d0ea7` | MNL/dclaborsupply-monorepo | `main` | yes |

## 2. Hash-cited registry (critical)

Scope: 67 citing documents — `MNL/gate/measure_map_accepted.json` (identical in `MNL_posfit/gate/`), every file under `Job_Market_paper/docs/normative/` (this file excluded), every `*_ruling(s)_*.md`, every `*accept*`/`*verif*` memo in Job_Market_paper and MNL. 230 SHA-256 citations extracted; each paired with the path (same line, else up to 3 lines above) that its hash matches, else the nearest preceding path. Current hashes recomputed from bytes (including `EUROMOD-STORAGE`); for mismatches every historical version of the path on all refs was hashed.

**Every row in section 2 is PINNED — the cited file (or cited bytes / cited commit) may never be moved or deleted.**

Summary: MATCH 137; NO PATH CITED 49; NOT FOUND 21; PATH UNRESOLVED, bytes found 14; MISMATCH (historical version) 4; MISMATCH (unexplained) 3; MISMATCH (bytes elsewhere) 2.

### 2a. SHA-256 citations

| # | Citing document | Line | Cited path (as written) | Cited SHA-256 | Resolved to | Exists | Current hash vs cited | Pin |
|---:|---|---:|---|---|---|---|---|---|
| 1 | `MNL/gate/measure_map_accepted.json` | 7 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | `6568ec53936c48fdafe4376714b6d2eaa8d37f30db040da25014773023534cc9` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | MATCH | PINNED |
| 2 | `MNL/gate/measure_map_accepted.json` | 11 | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | `45c45247246b9516945e4c196c60c0194f39f5dd0587d0de6e10524b5904bab3` | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | yes | MATCH | PINNED |
| 3 | `MNL/gate/measure_map_accepted.json` | 16 | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | `d3f41334273483ca2eac804f35014c12944cea4a428ab4c507056d0a6cda109b` | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | yes | MATCH | PINNED |
| 4 | `MNL/gate/measure_map_accepted.json` | 20 | _(none; context: "singles": ")_ | `641ceb0ed47b38111c4bac25deb9dd0d1f5942b931a694cd4cc1cec13d429128` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | PINNED |
| 5 | `MNL/gate/measure_map_accepted.json` | 21 | _(none; context: "couples": ")_ | `50b8289e97ceef16d767ce5799d9f0a712100c4db051444be630b1a56b34345d` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | PINNED |
| 6 | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 18 | `MNL/docs/corr/baseline_f1_provenance_v1.md` | `4bbce0f744677b6e1aa487f66eff3083b04597d628aa856148b6ef1cf36f04a6` | `MNL/docs/corr/baseline_f1_provenance_v1.md` | yes | MATCH | PINNED |
| 7 | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 47 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | `6568ec53936c48fdafe4376714b6d2eaa8d37f30db040da25014773023534cc9` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | MATCH | PINNED |
| 8 | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 55 | `experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | `cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 9 | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 57 | `…/s11_couples_parameter_table_v1.csv` | `fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 10 | `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 33 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | `a715fcd11c77bf589c71907fbaa1d7df00202c5819ddfc5b43fe018b8c307814` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | yes | MATCH | PINNED |
| 11 | `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 44 | `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml` | `dfc13329b0d6097b817a3191b1bdc8da052b3777162ccfc054e1258c62c5f7ab` | `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml` | yes | MATCH | PINNED |
| 12 | `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 45 | `MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml` | `c4a673e78c9ae29c6a95b49cf83d5afe2067d707dd9c327a883a64a475afe708` | `MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml` | yes | MATCH | PINNED |
| 13 | `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 48 | `estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` | `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | yes | MATCH | PINNED |
| 14 | `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 398 | `Job_Market_paper\1stfolder\J of Applied Econometrics - 2015 - Dagsvik - Labor Supply as a Choice Among Latent Jobs  Unobserved Heterogeneity and.pdf` | `1da644f96f2cc5c27e2a62028319035ffaea3e85a9be6a23ad0dff448fc18ee4` | `Job_Market_paper/1stfolder/J of Applied Econometrics - 2015 - Dagsvik - Labor Supply as a Choice Among Latent Jobs  Unobserved Heterogeneity and.pdf` | yes | MATCH | PINNED |
| 15 | `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 400 | `Job_Market_paper\JMP_lit_collection\files\41\Dagsvik and Jia - 2016 - Labor Supply as a Choice Among Latent Jobs Unobserved Heterogeneity and Identification LABOR SUPPL.pdf` | `9cbb7a56928b89d8b005d1f106d9fd673da5e17d26f673da90e3586a76f60995` | `Job_Market_paper/JMP_lit_collection/files/41/Dagsvik and Jia - 2016 - Labor Supply as a Choice Among Latent Jobs Unobserved Heterogeneity and Identification LABOR SUPPL.pdf` | yes | MATCH | PINNED |
| 16 | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 14 | `MNL/docs/corr/baseline_f1_provenance_v1.md` | `ab6e544f58e6921f4d79dc3cc183226a84755e14e192567e0922d24f3b91f938` | `MNL/docs/corr/baseline_f1_provenance_v1.md` | yes | MISMATCH — file changed since; cited hash = version at `838127e05c` | PINNED |
| 17 | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 95 | `JMP_measure_map_v1.md` | `641ceb0ed47b38111c4bac25deb9dd0d1f5942b931a694cd4cc1cec13d429128` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | MISMATCH at cited path; identical bytes at `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | PINNED |
| 18 | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 96 | _(none; context: - couples)_ | `50b8289e97ceef16d767ce5799d9f0a712100c4db051444be630b1a56b34345d` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | PINNED |
| 19 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 25 | `MNL/scripts/welfare/m08_welfare_measures.py` | `ccb8a2c9ddece225522201d8b667e69530c8c23c90d3f192c6a2523a19c21335` | `MNL/scripts/welfare/m08_welfare_measures.py` | yes | MATCH | PINNED |
| 20 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 26 | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | `d8687d3cfb71ce00f81613286e784c71c0e643721987bebf0d57226afe2a02d1` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | MATCH | PINNED |
| 21 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 270 | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/measure_map_1r/20260911/household_checks_v1.json` | `5556ee82fa1ad90f67eb60bae2373c912ad172194d24122f7162073446bd8578` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/measure_map_1r/20260911/household_checks_v1.json` | yes | MATCH | PINNED |
| 22 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 282 | `MNL/scripts/welfare/m08_welfare_measures.py` | `ccb8a2c9ddece225522201d8b667e69530c8c23c90d3f192c6a2523a19c21335` | `MNL/scripts/welfare/m08_welfare_measures.py` | yes | MATCH | PINNED |
| 23 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 283 | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | `d8687d3cfb71ce00f81613286e784c71c0e643721987bebf0d57226afe2a02d1` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | MATCH | PINNED |
| 24 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 284 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | `cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 25 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 285 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | `fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 26 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 286 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_theta_hat_v1.npy` | `8ed736215222265dc2a194df2d77fc92df0707baa21339eb51723b01f49926c9` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_theta_hat_v1.npy` | yes | MATCH | PINNED |
| 27 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 287 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_theta_hat_v1.npy` | `0838f36373eda7b391de671f8fdf14a957b23db37221d8753dbfd1c1581c3570` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_theta_hat_v1.npy` | yes | MATCH | PINNED |
| 28 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 288 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | `a715fcd11c77bf589c71907fbaa1d7df00202c5819ddfc5b43fe018b8c307814` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | yes | MATCH | PINNED |
| 29 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 289 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | `c4aee66a2adf8b08f1314913b52ee3c2218a7f5c0cd1b9c42f1ec82e4a21cc8c` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 30 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 290 | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | `641ceb0ed47b38111c4bac25deb9dd0d1f5942b931a694cd4cc1cec13d429128` | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | yes | MATCH | PINNED |
| 31 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 291 | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | `50b8289e97ceef16d767ce5799d9f0a712100c4db051444be630b1a56b34345d` | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | yes | MATCH | PINNED |
| 32 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 292 | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/engine_metadata_criterion_a_v1.json` | `709cc8cc604db66484a3eb9e4c52a8123cefc83517294d26bc2cc88169e352d7` | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/engine_metadata_criterion_a_v1.json` | yes | MATCH | PINNED |
| 33 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 293 | `MNL/outputs/welfare/fastlane/singles_measures_F4A_v1.parquet` | `ddfbd867871b69ddcb708862503826c56e7b122e062012f72e1c066272c5782f` | `MNL/outputs/welfare/fastlane/singles_measures_F4A_v1.parquet` | yes | MATCH | PINNED |
| 34 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 294 | `MNL/outputs/welfare/fastlane/singles_measures_F4C_v1.parquet` | `dd163e2ec87b43ca97a5613bd0983fd6de720889d7e34ed0f048b9d71e827a4b` | `MNL/outputs/welfare/fastlane/singles_measures_F4C_v1.parquet` | yes | MATCH | PINNED |
| 35 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 295 | `MNL/outputs/welfare/fastlane/F4C_manifest_v1.json` | `5bd2a37c071a4a3b1adce14540d004a22ccdb0807cfdb2d87366305aaee9de85` | `MNL/outputs/welfare/fastlane/F4C_manifest_v1.json` | yes | MATCH | PINNED |
| 36 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 296 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_principal_welfare_distributions_v1.parquet` | `8205b55dbb65278a40b196111deb0a9c6c3b96c7a9932f7c65d69d64e3814447` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_principal_welfare_distributions_v1.parquet` | yes | MATCH | PINNED |
| 37 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 297 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_w4_premise_audit_v1.json` | `3f65e92655363e3522548a19d76afedd946a730afcd6f725efe44d383cc1e142` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_w4_premise_audit_v1.json` | yes | MATCH | PINNED |
| 38 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 298 | `MNL/docs/corr/welfare_identity_check_v1.md` | `159cad6686e9622d4ef23212322858674b291fa5244c152eb31719d12a9b968d` | `MNL/docs/corr/welfare_identity_check_v1.md` | yes | MATCH | PINNED |
| 39 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 299 | `MNL/docs/corr/welfare_identity_check_v1.json` | `ec2414449f0f105e4e3b2313f64fc6ce5170031b1cf00359c3404ba07326fbb7` | `MNL/docs/corr/welfare_identity_check_v1.json` | yes | MATCH | PINNED |
| 40 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 300 | `MNL/scripts/bpool/specs/theta_hat_realdata_901_v1.csv` | `c72e92b16170a7dd2dc8ec0b76dc3f522a1fc6d6182a5eba8f8cad34cef76269` | `MNL/scripts/bpool/specs/theta_hat_realdata_901_v1.csv` | yes | MATCH | PINNED |
| 41 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 301 | `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md` | `1ffa1500907ada28835dda8f7ac089562dba79c343eb5af51d668283c9ed0479` | `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md` | yes | MISMATCH — file changed since; cited hash = version at `003b29a0b5` | PINNED |
| 42 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 302 | `MNL/scripts/welfare/configs/theta_hat_p2a_singles2016_v1.csv` | `0684ee52a3c290749c0e9c30c272db1956990a84a6f4a77f328305e91f0d417c` | `MNL/scripts/welfare/configs/theta_hat_p2a_singles2016_v1.csv` | yes | MATCH | PINNED |
| 43 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 303 | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260825T164802Z_500708_1759e2e09f0941609ea183ae51ea8f20_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json` | `1a6f586605e05da6b2057a85af7116ffb6b6fd536992ae60be2c4514b96c3a9d` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260825T164802Z_500708_1759e2e09f0941609ea183ae51ea8f20_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json` | yes | MATCH | PINNED |
| 44 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 304 | `C:/Users/hisham/MNL/EUROMOD-STORAGE/outputs/welfare/p2a_singles2016/singles_measures_p2a_v1.parquet` | `63d66877a2f832dcc13c6067133137079bffd433e13eee644ce7c3e584014512` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/outputs/welfare/p2a_singles2016/singles_measures_p2a_v1.parquet` | yes | MATCH | PINNED |
| 45 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 37 | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | `4002220a4c127404ff1169d7453354dc0aa7f1d250ba38d9bbc820b9fee8a2e4` | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | yes | MATCH | PINNED |
| 46 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 37 | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2.md` | `c2dd032363e70de24fe31a2d3fff082c3e56aaa2ed44fbfe1dd3787619e8ba71` | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2.md` | yes | MATCH | PINNED |
| 47 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 39 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | `8b02ff93b94a72327caa8d16476a3bf5c6176894162e0758f03562ee6329e226` | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | yes | MATCH | PINNED |
| 48 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 40 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | `00df1d8d5a5e42bf0186515311389f87370cbd06457251943286e3c91990474d` | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | yes | MATCH | PINNED |
| 49 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 40 | `docs/normative/scripts/fork_derived_numerals_v1.py` | `994c3dfaad7cbafd2f76871ac05629e0ee60947b5a00085f944a0bebe11d8e9c` | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | yes | MATCH | PINNED |
| 50 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 40 | `docs/normative/fork_derived_numerals_v1.csv` | `2677356a555ec3eb65623227e3d26363925c2d11add1112c8db925213f77bf8e` | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | yes | MATCH | PINNED |
| 51 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 41 | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | `7f5d26857d8a96174a9924848f65a02611944273d7775fdc52dc82364a818c05` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | MATCH | PINNED |
| 52 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 42 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | `6568ec53936c48fdafe4376714b6d2eaa8d37f30db040da25014773023534cc9` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | MATCH | PINNED |
| 53 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 42 | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | `45c45247246b9516945e4c196c60c0194f39f5dd0587d0de6e10524b5904bab3` | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | yes | MATCH | PINNED |
| 54 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 43 | `MNL/docs/corr/baseline_f1_verification_v1.md` | `da7badf639f3d502d47b301558453d76501c9c44033ece3f17bde350bfd5e55f` | `MNL/docs/corr/baseline_f1_verification_v1.md` | yes | MATCH | PINNED |
| 55 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 43 | `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | `54dfd886e41d0a89c1056cbea5fa51e0a1294d3ca0813f938802bdc3dbd9ee0e` | `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | yes | MATCH | PINNED |
| 56 | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 17 | `docs/normative/JMP_W1_reference_domain_fork_v1.md` | `260eb0d6dc4497cb920f4e0838c8fb3921b065d7e3df947e18ab687c49081d35` | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | yes | MISMATCH — file changed since; cited hash = version at `f6346232ef` | PINNED |
| 57 | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 23 | `jobs_and_wellbeing.tex` | `d8687d3cfb71ce00f81613286e784c71c0e643721987bebf0d57226afe2a02d1` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | MATCH | PINNED |
| 58 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 16 | `docs/normative/scripts/fork_derived_numerals_v1.py` | `994c3dfaad7cbafd2f76871ac05629e0ee60947b5a00085f944a0bebe11d8e9c` | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | yes | MATCH | PINNED |
| 59 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 18 | `docs/normative/fork_derived_numerals_v1.csv` | `2677356a555ec3eb65623227e3d26363925c2d11add1112c8db925213f77bf8e` | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | yes | MATCH | PINNED |
| 60 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 944 | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | `d8687d3cfb71ce00f81613286e784c71c0e643721987bebf0d57226afe2a02d1` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | MATCH | PINNED |
| 61 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 945 | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.agent.md` | `4940775b8b57ab5ec4278795d2fe7361de8119e2019f45fa3bbf8fce138f4c2a` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.agent.md` | yes | MATCH | PINNED |
| 62 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 946 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | `8b02ff93b94a72327caa8d16476a3bf5c6176894162e0758f03562ee6329e226` | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | yes | MATCH | PINNED |
| 63 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 947 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | `cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 64 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 948 | `…/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | `fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 65 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 949 | `…/runs/preference_figures_final/pff_step1_reference_v1.json` | `594a941ebacad8e4b4462e464732199d836b8ca65c43a0679368e0c03375d41a` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/preference_figures_final/pff_step1_reference_v1.json` | yes | MATCH | PINNED |
| 66 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 950 | `…/runs/figE1_matched_households/e1_matched_households_v1.json` | `4dbb3e6abf918689a8027ed093ece2aeaf884d64fd2f25c9282cf3396a5c3454` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/figE1_matched_households/e1_matched_households_v1.json` | yes | MATCH | PINNED |
| 67 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 951 | `Job_Market_paper/Literature/markdowns/Dagsvik_Jia_2016.md` | `29cf5975c22e40b4224408c48f7cf1f11c6f1d8412e2aff665bc4645ce9a804d` | `Job_Market_paper/Literature/markdowns/Dagsvik_Jia_2016.md` | yes | MATCH | PINNED |
| 68 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 952 | `Job_Market_paper/beamer/reference/Theory_talk/slides/spoken_script_click_cues.tex` | `f07a475eeb1004d2c6cdbc3376289945f359eec424e9abf26141df44e9029236` | `Job_Market_paper/beamer/reference/Theory_talk/slides/spoken_script_click_cues.tex` | yes | MATCH | PINNED |
| 69 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 953 | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | `994c3dfaad7cbafd2f76871ac05629e0ee60947b5a00085f944a0bebe11d8e9c` | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | yes | MATCH | PINNED |
| 70 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 954 | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | `2677356a555ec3eb65623227e3d26363925c2d11add1112c8db925213f77bf8e` | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | yes | MATCH | PINNED |
| 71 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 958 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | `c4aee66a2adf8b08f1314913b52ee3c2218a7f5c0cd1b9c42f1ec82e4a21cc8c` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 72 | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 42 | `s11_singles_parameter_table_v1.csv` | `cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 73 | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 44 | `s11_couples_parameter_table_v1.csv` | `fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | yes | MATCH | PINNED |
| 74 | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 46 | `pff_step1_reference_v1.json` | `594a941ebacad8e4b4462e464732199d836b8ca65c43a0679368e0c03375d41a` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/preference_figures_final/pff_step1_reference_v1.json` | yes | MATCH | PINNED |
| 75 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 788 | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | `681420523f1efb76389c624e437549ee8971184672327d483296862708845983` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | yes | MATCH | PINNED |
| 76 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 789 | `…/likelihood/wage_density.py` | `083b5cf5deeae485a270c60fd2b7d6188bf6a72c65aedf9f12d56aa11972a0eb` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/wage_density.py` | yes | MATCH | PINNED |
| 77 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 790 | `MNL/scripts/welfare/m08_welfare_measures.py` | `ccb8a2c9ddece225522201d8b667e69530c8c23c90d3f192c6a2523a19c21335` | `MNL/scripts/welfare/m08_welfare_measures.py` | yes | MATCH | PINNED |
| 78 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 791 | `MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` | `MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | yes | MATCH | PINNED |
| 79 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 792 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json` | `5fdc88502493ce540b088880eecf049bc268392ff3e8790ffe78a16aa6ddc884` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json` | yes | MATCH | PINNED |
| 80 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 793 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_w4_premise_audit_v1.json` | `3f65e92655363e3522548a19d76afedd946a730afcd6f725efe44d383cc1e142` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_w4_premise_audit_v1.json` | yes | MATCH | PINNED |
| 81 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 794 | `…/runs/s12_welfare_record/run_s12_welfare_record_v1.py` | `5ed7a47120e03f0629ce336e06b4bd1376ddd22f86988ce5d9caa2d33958e743` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/run_s12_welfare_record_v1.py` | yes | MATCH | PINNED |
| 82 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 23 | `JMP_HK_01_inventory_and_disposition_register_v3.csv` | `30d0999e56e29a6ef513359b0a708512f1780d4b63f76cc22d5aba23a16f2937` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v3.csv` | yes | MATCH | PINNED |
| 83 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 24 | `JMP_HK_01_inventory_and_disposition_register_v4.csv` | `4cb3bda72d26f5b723756a85b31ab617361e18f6e467b7cf00855073c9a61126` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v4.csv` | yes | MATCH | PINNED |
| 84 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 25 | `JMP_HK_01_inventory_and_disposition_register_v5.csv` | `ed8a186ac7520bb319ff513a3edc8ceb1f721164a33271474c881ddcba8451b8` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v5.csv` | yes | MATCH | PINNED |
| 85 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 26 | `JMP_HK_01_inventory_and_disposition_register_v6.csv` | `cc2f1725615831d7231532f6f39356583c8f6271e54601a8d11343baa6963ce0` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v6.csv` | yes | MATCH | PINNED |
| 86 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 27 | `JMP_HK_01_inventory_and_disposition_register_v7.csv` | `7b710381cf8c41bdbadd7b230a4b8b40274ca696024f1875305a2c8fb5a4734e` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v7.csv` | yes | MATCH | PINNED |
| 87 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 30 | `JMP_HK_01_inventory_and_disposition_register_v7.csv` | `cc2f1725615831d7231532f6f39356583c8f6271e54601a8d11343baa6963ce0` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v7.csv` | yes | MISMATCH at cited path; identical bytes at `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v6.csv` | PINNED |
| 88 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 48 | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md` | `c7a66c97dd7c6ad29d63cf916bada6b343a2a28004ecff1b6bcce538e586888f` | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md` | yes | MATCH | PINNED |
| 89 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 60 | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v2.md` | `699479f3c5b8b323e58b804c1cfe5eb114eb209432315ce2cedc66a5f944a9ad` | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v2.md` | yes | MATCH | PINNED |
| 90 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 89 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v4.md` | `0c1d17d8345d7ce5ff932cac1fc3ea3a8684168620e96f450401b5248d137590` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v4.md` | yes | MATCH | PINNED |
| 91 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 90 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v5.md` | `ff313833cf6c1bb2f616e3bde05046702b7fe0c5ce8dc165cf8e7ada37bf9376` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v5.md` | yes | MATCH | PINNED |
| 92 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 91 | `docs/jmp_methodology/RURO_welfare_stage2_vdir_crosscheck_v1.md` | `354301fc0e17e2e1b6a54aaf8013576b657d0fa801a6644270ded5437a68943d` | `MNL/docs/jmp_methodology/RURO_welfare_stage2_vdir_crosscheck_v1.md` | yes | MATCH | PINNED |
| 93 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 106 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v2.md` | `24e694055d56dbf639404a365bccce4c1f6cfb3a9de31524f030664d0202ef02` | `MNL/archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v2.md` | yes | MATCH | PINNED |
| 94 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 107 | `docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v3.md` | `a7b530d484899885632d1d2366c6df336e2e7bbdf9fed418636b8e62fe9bef1e` | `MNL/archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase4_remediation_report_v3.md` | yes | MATCH | PINNED |
| 95 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 108 | `docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v4.md` | `3a785d4fb09776c1654a49a83e607a41526fca92dc16d898765d004275454ce2` | `MNL/archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_region_live_phase5_code_review_v4.md` | yes | MATCH | PINNED |
| 96 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 109 | `docs/France_case/P2a/FR_P2a_streaming_incrementA_review_v2.md` | `f61f72e93f714dd5fce4813820d58e564a4d2902b0328eede787388027b54133` | `MNL/archive/HK01/2026-08-25_ratified_v1/docs/France_case/P2a/FR_P2a_streaming_incrementA_review_v2.md` | yes | MATCH | PINNED |
| 97 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 160 | `JMP_HK_01_phase2_archive_manifest_v1.csv` | `a634e509c1ba0296335ad0a2bcc76d3450dea39c16a8ab5fe94ecad4e65227c1` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_phase2_archive_manifest_v1.csv` | yes | MATCH | PINNED |
| 98 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 194 | `market.html` | `7bce41c298b86000e880578233a9adf85d73ec9816571ef14a86df6766942c6b` | — | no | NOT FOUND (not found) | PINNED |
| 99 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 215 | _(none; context: Working tree (restored)  1,483,064)_ | `7bce41c298b86000e880578233a9adf85d73ec9816571ef14a86df6766942c6b` | — | no | NO PATH CITED — unresolved | PINNED |
| 100 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 216 | _(none; context: Index blob d7678fa9  1,465,090)_ | `847c7151f603ca09477d0fc7fa43efabe0877a5e80c6fd1cb422b57cb8e66fb1` | — | no | NO PATH CITED — unresolved | PINNED |
| 101 | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 286 | `JMP_HK_01_v5_movable_rows_codex_review_v1.md` | `c1e92cf3671917be3cbe5fb3abd305091f0a4632e475226b9ba3dd644ce4b6f0` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_v5_movable_rows_codex_review_v1.md` | yes | MATCH | PINNED |
| 102 | `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | 39 | _(none; context: - Pre-edit sha256:)_ | `47c92480aa3ec010bbbd6be73a7698fbef834616c6c1355aeba9c1dd8d733dd1` | — | no | NO PATH CITED — unresolved | PINNED |
| 103 | `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | 40 | _(none; context: - Post-edit sha256:)_ | `62fda1ca28a39b641ea788c93d88932a9ae0c0ea62fa7b040ae18ad7ce565e9f` | — | no | NO PATH CITED — unresolved | PINNED |
| 104 | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 26 | `docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | `d4de2055ca5db8c6e3d3ea4c945b027ee0a80c0764ba4dc2c99d7d8154968d80` | `Job_Market_paper/docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | yes | MATCH | PINNED |
| 105 | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 27 | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_rqmc_final_precision_results_v1.md` | `a456113473cebad748915ad1448134d891023951d05fb1be96ab1f6c914d90f7` | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_rqmc_final_precision_results_v1.md` | yes | MATCH | PINNED |
| 106 | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 28 | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_beta_w_pexp2_profile_results_v1.md` | `99b5df2e163c9a0b11ab9f8c77dcbb769797a130174a96f3e51a8b4047aa7fce` | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_beta_w_pexp2_profile_results_v1.md` | yes | MATCH | PINNED |
| 107 | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 29 | `MNL/docs/France_case/P2a/FR_P2a_m08_rqmc_preflight_codex_review_v1.md` | `5244968fdf7ac6d5fa2c985b67e273d21259454730d1f99661905153a1849916` | `MNL/docs/France_case/P2a/FR_P2a_m08_rqmc_preflight_codex_review_v1.md` | yes | MATCH | PINNED |
| 108 | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 30 | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | `06d2c0fc9cfd62ff1eb220e62cc34f660a739e0d594f079e47ed7307bab4b396` | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | yes | MATCH | PINNED |
| 109 | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 31 | `docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | `aa938e7b3f56236f42a553dc34b48e8fca52b36b1720ef37c451c73604d854f9` | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | yes | MATCH | PINNED |
| 110 | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 90 | _(none; context: )_ | `b1879fcf2c210d337a4f4d3bfff93d06a6e044f8da1326f6ca3a5ab168d76f00` | — | no | NO PATH CITED — unresolved | PINNED |
| 111 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v2.md` | 131 | _(none; context: )_ | `e663802712b2e004711beb327432a43e64501a47d82fcd7d6a2589c3e689ae2d` | — | no | NO PATH CITED — unresolved | PINNED |
| 112 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v3.md` | 131 | _(none; context: )_ | `e663802712b2e004711beb327432a43e64501a47d82fcd7d6a2589c3e689ae2d` | — | no | NO PATH CITED — unresolved | PINNED |
| 113 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v3.md` | 180 | _(none; context: )_ | `670de8adf5f23e6714195bacdb13258f1014d7d79f8aeb4f42717dd4e986e157` | — | no | NO PATH CITED — unresolved | PINNED |
| 114 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 131 | _(none; context: )_ | `e663802712b2e004711beb327432a43e64501a47d82fcd7d6a2589c3e689ae2d` | — | no | NO PATH CITED — unresolved | PINNED |
| 115 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 180 | _(none; context: )_ | `670de8adf5f23e6714195bacdb13258f1014d7d79f8aeb4f42717dd4e986e157` | — | no | NO PATH CITED — unresolved | PINNED |
| 116 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 302 | _(none; context: )_ | `094200a86aa23207d55266c52c36d617d6b16ca2171b637870b46474b199551b` | — | no | NO PATH CITED — unresolved | PINNED |
| 117 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1054 | _(none; context: )_ | `30d0999e56e29a6ef513359b0a708512f1780d4b63f76cc22d5aba23a16f2937` | — | no | PATH UNRESOLVED (no path cited); hash matches `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v3.csv` | PINNED |
| 118 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1055 | _(none; context: sha256:)_ | `4cb3bda72d26f5b723756a85b31ab617361e18f6e467b7cf00855073c9a61126` | — | no | PATH UNRESOLVED (no path cited); hash matches `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v4.csv` | PINNED |
| 119 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3153 | `docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | `06d2c0fc9cfd62ff1eb220e62cc34f660a739e0d594f079e47ed7307bab4b396` | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | yes | MATCH | PINNED |
| 120 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3442 | _(none; context: theta_hat sha256)_ | `913dd559a769d410f26f505d32d258fb45c4e2f4a430ec95cfca333d7d8bdce1` | — | no | NO PATH CITED — unresolved | PINNED |
| 121 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3858 | `experiments/JMP_PS1/runs/ps1r1_bmo/r1bmo_secure_env_bundle_v1.zip` | `65ff967bb1b077bebaec78db9c82abe1180e706891fd112cc085af57b72894d5` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/r1bmo_secure_env_bundle_v1.zip` | yes | MATCH | PINNED |
| 122 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 7190 | `Literature/Decoster_Haan_2015_Empirical welfare analysis with preference heterogeneity [2013 VfS working paper].pdf` | `1c1e765313d83393a45b09142389501d42447cb32274778b19d7b84b402e53f2` | `Job_Market_paper/Literature/Decoster_Haan_2015_Empirical welfare analysis with preference heterogeneity [2013 VfS working paper].pdf` | yes | MATCH | PINNED |
| 123 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 7846 | _(none; context: )_ | `e4b2f16e0d638f9586156f00e03b0498bb01a29fef32f6146135e26beb7ec5e7` | — | no | NO PATH CITED — unresolved | PINNED |
| 124 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 7847 | _(none; context: 18453.4750133318, LOC4 theta sha256)_ | `10d4aaeda3b7e5f0d6e480dc9a0b8de9c889d5b8c28eb135a47a7d3091bf8ef5` | — | no | NO PATH CITED — unresolved | PINNED |
| 125 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 170 | _(none; context: )_ | `41061f7ce681f56528cd3576dda707691e3440bac7c35bb6ca4947dde0af9bcb` | — | no | NO PATH CITED — unresolved | PINNED |
| 126 | `Job_Market_paper/docs/missions/JMP_M05C_deputy_phase5_acceptance_v1.md` | 54 | _(none; context: )_ | `d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232` | — | no | NO PATH CITED — unresolved | PINNED |
| 127 | `Job_Market_paper/docs/missions/JMP_M05C_deputy_phase5_acceptance_v1.md` | 58 | _(none; context: )_ | `7f71a532ff66a1e882f4a085ca78e14a9788e6c98cff8c04957b9df4c3ff4a80` | — | no | NO PATH CITED — unresolved | PINNED |
| 128 | `Job_Market_paper/docs/missions/JMP_M05C_deputy_phase5_acceptance_v1.md` | 62 | _(none; context: )_ | `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b` | — | no | NO PATH CITED — unresolved | PINNED |
| 129 | `Job_Market_paper/docs/missions/JMP_M05C_deputy_phase5_acceptance_v1.md` | 66 | _(none; context: )_ | `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3` | — | no | NO PATH CITED — unresolved | PINNED |
| 130 | `Job_Market_paper/docs/missions/JMP_M05_deputy_programme_acceptance_v1.md` | 37 | _(none; context: )_ | `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b` | — | no | NO PATH CITED — unresolved | PINNED |
| 131 | `Job_Market_paper/docs/missions/JMP_M05_deputy_programme_acceptance_v1.md` | 41 | _(none; context: )_ | `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3` | — | no | NO PATH CITED — unresolved | PINNED |
| 132 | `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 78 | _(none; context: )_ | `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b` | — | no | NO PATH CITED — unresolved | PINNED |
| 133 | `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 82 | _(none; context: )_ | `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3` | — | no | NO PATH CITED — unresolved | PINNED |
| 134 | `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 17 | _(none; context: tenated in master input order  128250  128250  Exactly equal)_ | `aa6ee29c8c0b331ef9ea299240a28b7736fc87b6205493d4184cab32d17a08a6` | — | no | NO PATH CITED — unresolved | PINNED |
| 135 | `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 18 | _(none; context: nes replaced by section bytes  131850  131850  Exactly equal)_ | `bc647257f5519a5fec13b7c9194cb623f183663418377fd6f2ed9d2926a2adc2` | — | no | NO PATH CITED — unresolved | PINNED |
| 136 | `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 37 | _(none; context: assert hashlib.sha256(body).hexdigest() == ")_ | `aa6ee29c8c0b331ef9ea299240a28b7736fc87b6205493d4184cab32d17a08a6` | — | no | NO PATH CITED — unresolved | PINNED |
| 137 | `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 39 | _(none; context: assert hashlib.sha256(expanded).hexdigest() == ")_ | `bc647257f5519a5fec13b7c9194cb623f183663418377fd6f2ed9d2926a2adc2` | — | no | NO PATH CITED — unresolved | PINNED |
| 138 | `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 71 | _(none; context: t also matches byte for byte across all three PDFs; SHA-256:)_ | `9209c9a513c118033c9de136756095f7c0b38a9d1d10cb457dd8fc56814a9111` | — | no | NO PATH CITED — unresolved | PINNED |
| 139 | `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 89 | `FR_P2a_m08_parity_gate_report_v2.md:423-428` | `bde41a0718093855ec310e1725633df5532d50c44def056a2b041389823d82c7` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 140 | `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 89 | `FR_P2a_m08_parity_gate_report_v2.md:423-428` | `d79d05ae326276506bc950449af737da35042cac4d16e733963c1ae1b9856547` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 141 | `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 89 | `FR_P2a_m08_parity_gate_report_v2.md:423-428` | `441b416d164827eab6b0822b2f6dfbda9d3de639aac61ddbdc0f144ac3181046` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 142 | `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 89 | `FR_P2a_m08_parity_gate_report_v2.md:423-428` | `1eea3cc7583811170426c12e2a44058d9145dac52eceb202c7f10ecda31423d8` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 143 | `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 89 | `FR_P2a_m08_parity_gate_report_v2.md:423-428` | `69571a671492ec37151ca322003a4c551c6b218996949ea47e11b74a1a0b6467` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 144 | `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 89 | `FR_P2a_m08_parity_gate_report_v2.md:423-428` | `029d5ee618576c9a91cc2374500e3d632912c52d637a1b4268c1db4796979e81` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 145 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 69 | _(none; context: original_sha256 =)_ | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | PINNED |
| 146 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 70 | _(none; context: tampered_sha256 =)_ | `0fff7e7d28587402c98ea21dd28242e4db2104c191c7e1c10084d19c5b8e3751` | — | no | NO PATH CITED — unresolved | PINNED |
| 147 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 86 | _(none; context: ; source says 201 alts/HH  201 draws, 1,555 HH, 312,555 rows)_ | `b245ec092b44be107d4bc5f96d2e0e767b749f716a29c9300af63bcbc214e132` | — | no | NO PATH CITED — unresolved | PINNED |
| 148 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 86 | _(none; context: ec092b44be107d4bc5f96d2e0e767b749f716a29c9300af63bcbc214e132)_ | `535d6d74d21e584ce5d673bbd1fa295782dd01d17fccd214ba385f9a73b8a76f` | — | no | NO PATH CITED — unresolved | PINNED |
| 149 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 87 | _(none; context: ; source says 401 alts/HH  401 draws, 1,555 HH, 623,555 rows)_ | `064679d5998735a8f5052efd0072f4d2db3cf4165b4e0c37d2436eee6d76e44a` | — | no | NO PATH CITED — unresolved | PINNED |
| 150 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 87 | _(none; context: 79d5998735a8f5052efd0072f4d2db3cf4165b4e0c37d2436eee6d76e44a)_ | `be9c614205a882b7999d58a3247f3f20d17ec8c1b4b17d56596cb2308279adbd` | — | no | NO PATH CITED — unresolved | PINNED |
| 151 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 97 | _(none; context: - 2x history:)_ | `6f9eea2dec117240817a648a238191c44a594a91950016519d19f442b99060f0` | — | no | NO PATH CITED — unresolved | PINNED |
| 152 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 98 | _(none; context: - 4x history:)_ | `1a23e933cfd35d99daec738a77d84a63becc11dc3c98dfd208f6cb13321cdf53` | — | no | NO PATH CITED — unresolved | PINNED |
| 153 | `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 144 | _(none; context: both canonical_sha256 =)_ | `e4fe69d617f4de3086c8475d30579b35128e41645221223a78b229f5ef476ccb` | — | no | NO PATH CITED — unresolved | PINNED |
| 154 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 30 | `scripts/m08e/m08e_pins.py` | `4222dda6486d219ac6053177d2fcf2db073de27f325dce4dcb272a0f070f6113` | `MNL/scripts/m08e/m08e_pins.py` | yes | MISMATCH — no matching historical version | PINNED |
| 155 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 31 | `docs/France_case/P2a/FR_P2a_m08e_E3_reestimation_note_v2.md` | `970eda4c0d3dcc140b1608159c64fff420eb8395964e2e3b34f500c1a660a5f5` | `MNL/docs/France_case/P2a/FR_P2a_m08e_E3_reestimation_note_v2.md` | yes | MATCH | PINNED |
| 156 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 122 | `m08e_e3_reestimate_v2.py` | `4c0a5344c820308d79d79d6098cade7442db6fcbf6cb44e4414182b7c3ee75c4` | `MNL/scripts/m08e/m08e_e3_reestimate_v2.py` | yes | MATCH | PINNED |
| 157 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 123 | `m08e_e4_curvature_inference_v2.py` | `c315aabbea9ed0d9a218ff720c7b6567eaaa2d703a36658835126318fa06efaa` | `MNL/scripts/m08e/m08e_e4_curvature_inference_v2.py` | yes | MATCH | PINNED |
| 158 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 141 | `e4_manifest.json:617-620` | `cd0bb6ee5a0cbe130e65cdb211d9eb6d38ede1143e7b2431583013fd9a708d0c` | — | no | NOT FOUND (ambiguous: 6 candidates) | PINNED |
| 159 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 142 | `e4_manifest.json:627-630` | `763bfe2955e35608a726d5a67da3fde3df9ce86ca09fe63e0b7db6b61ad2ab30` | — | no | NOT FOUND (ambiguous: 6 candidates) | PINNED |
| 160 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 143 | `e4_manifest.json:672-675` | `8b92a6f053ac8b3551e2283264efb7231da2b67d21e453b4c33709020f0e0d55` | — | no | NOT FOUND (ambiguous: 6 candidates) | PINNED |
| 161 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 144 | `e4_manifest.json:687-690` | `a4fc240045b1836852f2868060991939d6fe6b017c00dc8650164d3dba3dfc22` | — | no | NOT FOUND (ambiguous: 6 candidates) | PINNED |
| 162 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 160 | _(none; context: spec_yaml=)_ | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | PINNED |
| 163 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 162 | _(none; context: mod_phase5_runner=)_ | `054139c699321b6ca07e04a51e17d0cf4454fd3a75b3d5bcbf39b709cab4f72f` | — | no | NO PATH CITED — unresolved | PINNED |
| 164 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 169 | `r1_probe_evidence.json=b49518e4eb61765e7c8c0d2f97c67f6957fc52a096a87c72642d69b1813010d5` | `b49518e4eb61765e7c8c0d2f97c67f6957fc52a096a87c72642d69b1813010d5` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/e2_closure_r1_v1/attempts/20260823T152543Z_180012_69c59793f2284da6ae0daa2a42682fef_r1probes_R1_PROBES_PASS/r1_probe_evidence.json` | yes | MATCH | PINNED |
| 165 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 171 | `r1_probe_evidence.json=b49518e4eb61765e7c8c0d2f97c67f6957fc52a096a87c72642d69b1813010d5` | `30bcdc2dd7fac7b5b956f2aff94b0bf577447f38f0551ef6c4b838391ec5da19` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 166 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 212 | `e3_manifest.json:195-201` | `5e03b3a8a4d77b723d9616b7adda6caa1b5a6b6355bee3740f4b6daa4821a263` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/e3_estimation_v2/attempts/20260819T214600Z_672360_410223ff1ccd4d12b85d48b36d60fb1e_margqh_v2_phase3equiv_tightened_E3_CONVERGED_SINGLE_OPTIMUM/e3_manifest.json` | yes | MATCH | PINNED |
| 167 | `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 220 | _(none; context: )_ | `ffbc759ffb9199d288b1d8e3c221a9a3589fa8abed0096e85ab6573ace861303` | — | no | NO PATH CITED — unresolved | PINNED |
| 168 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 38 | `region_live_v1/inputs/fr_p2a_draws_geometry__singles.parquet` | `5bcf0e5409ef74c57f6de24efdfd24d0075132dc3138ddb57a22740b916cf235` | `MNL/outputs/p2a_singles2016/region_live_v1/inputs/fr_p2a_draws_geometry__singles.parquet` | yes | MATCH | PINNED |
| 169 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 39 | `region_live_v1/fr_p2a_singles2016_regionlive__singles.parquet` | `8bf083ce3be17f8c74af894bc3748718cbb0a991eb9a411db7188e806d1e9f0d` | `MNL/outputs/p2a_singles2016/region_live_v1/fr_p2a_singles2016_regionlive__singles.parquet` | yes | MATCH | PINNED |
| 170 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 40 | `estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` | `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | yes | MATCH | PINNED |
| 171 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 41 | `estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | `5f3722dc2092cda0af47cec39cb2cbbb7050dd153df1edf9dd9de8a231d76c9b` | — | no | NOT FOUND (ambiguous: 4 candidates) | PINNED |
| 172 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 42 | `run_p2a_regionlive_rebuild.py` | `be11294bf6e0456a37afc713d0e1bd843f574e2dfd136d60968b6519594c4475` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 173 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 43 | `p2a_regionlive_rebuild_v1.yaml` | `68d152e70cb73b6616a8b16a63edfb90298945c65fa15dd8580399033059d8fe` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 174 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 33 | `FR_P2a_region_live_phase3_code_review_v6.md` | `9c78d4e0a194e0b20904c6b9ec8f875525e1a6217d4d4f7a7192635b672ab341` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_code_review_v6.md` | yes | MATCH | PINNED |
| 175 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 42 | _(none; context: )_ | `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b` | — | no | NO PATH CITED — unresolved | PINNED |
| 176 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_manager_acceptance_v1.md` | 24 | _(none; context: SHA-256)_ | `cd0bb6ee5a0cbe130e65cdb211d9eb6d38ede1143e7b2431583013fd9a708d0c` | — | no | NO PATH CITED — unresolved | PINNED |
| 177 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_manager_acceptance_v1.md` | 32 | _(none; context: ()_ | `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b` | — | no | NO PATH CITED — unresolved | PINNED |
| 178 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_manager_acceptance_v1.md` | 44 | _(none; context: )_ | `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3` | — | no | NO PATH CITED — unresolved | PINNED |
| 179 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 56 | `scripts/p2a/run_p2a_phase5_inference.py` | `d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232` | `MNL/scripts/p2a/run_p2a_phase5_inference.py` | yes | MISMATCH — no matching historical version | PINNED |
| 180 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 68 | `meat_free37.csv` | `548be0a6c122ef636931e53f7818296929fab2ee6060b2a2eba8781ccc49b02c` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/meat_free37.csv` | yes | MATCH | PINNED |
| 181 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 69 | `meat_free37.npy` | `4bac680485d6e651165666c80ee1929ae4a6efc4f41c7d4a35d9b981426b4d94` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/meat_free37.npy` | yes | MATCH | PINNED |
| 182 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 70 | `meat_interior35.csv` | `b2a1f2144745a55423695523c3d2e8f2837a0bb9d65756f6a222ed562af3cfed` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/meat_interior35.csv` | yes | MATCH | PINNED |
| 183 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 71 | `meat_interior35.npy` | `3551b319ead355619577e58725e1071ae400c6964ef9510c2a029a81753e0e89` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/meat_interior35.npy` | yes | MATCH | PINNED |
| 184 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 72 | `meat_interior35.npy` | `7111aa441f38ad2b9648fa920cda414c7b155f546ddacda27a45681ddc4e31b9` | — | no | NOT FOUND (ambiguous: 8 candidates) | PINNED |
| 185 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 73 | `phase5_correlation_model.csv` | `d9d0d2eb4616693297021bb2b17aba1dbb49e752f057302dc02da2a0d0bd461a` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_correlation_model.csv` | yes | MATCH | PINNED |
| 186 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 74 | `phase5_correlation_robust.csv` | `b0c857c8a9432031996f8d2ee5fb51943e649cfc52417dcfd44e3bbcaa7af652` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_correlation_robust.csv` | yes | MATCH | PINNED |
| 187 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 75 | `phase5_covariance_model.csv` | `2e72678a6b7392f53794add0d20ff089bf2f0c5c8819f8327877c97a81e2ed73` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_covariance_model.csv` | yes | MATCH | PINNED |
| 188 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 76 | `phase5_covariance_model.npy` | `04952ba16eb1032a315000f2fd5593de7faa37f8bd571a01c1c8181e0c185632` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_covariance_model.npy` | yes | MATCH | PINNED |
| 189 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 77 | `phase5_covariance_robust.csv` | `c43710b4f5452ba10e569f44bab4b2853c4b21c9c09bbbf3510f153cbe3b094c` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_covariance_robust.csv` | yes | MATCH | PINNED |
| 190 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 78 | `phase5_covariance_robust.npy` | `0b4e2a509b718ad67d337784df7c38cb4e1edcec9514b78a1f73edf3aff6a80b` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_covariance_robust.npy` | yes | MATCH | PINNED |
| 191 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 79 | `phase5_diagnostics.json` | `943d8532dc0c4825b435b65fefa677d8ecca6018c924e9663e9024a34c60c34f` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_diagnostics.json` | yes | MATCH | PINNED |
| 192 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 81 | `phase5_parameter_table.csv` | `6727692a8614c8a8cf01c0d5d98a75bc737d026e6c297c73b6f4826172deebb2` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_parameter_table.csv` | yes | MATCH | PINNED |
| 193 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 82 | `phase5_regional_covariance.csv` | `3cba5b4389073d41022cc9e3a43afc6a3a826f2e139ec18a09d554e795db4111` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_regional_covariance.csv` | yes | MATCH | PINNED |
| 194 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 83 | `phase5_regional_tests.csv` | `47dae8014ec2c536cb3cf79e27a61f50af4871f3c0303d3be1737fb9f735b584` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_regional_tests.csv` | yes | MATCH | PINNED |
| 195 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 84 | `phase5_standard_errors.csv` | `da92759879c7e451a5b1ff488a48e13ec7e6dd98b793ebf7caa9313b420f3fbb` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_standard_errors.csv` | yes | MATCH | PINNED |
| 196 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 85 | `score_aggregate_summary.json` | `b3533fa4d52ee504d89b8b0d3d7e6e7fc217815aa91cd2388b43d9130108cf08` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/score_aggregate_summary.json` | yes | MATCH | PINNED |
| 197 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 86 | `score_sum_free37.csv` | `b76ff964ec40561a625f660657258c5effe97ce12bd47c6bda618f952f48cc19` | `MNL/outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/score_sum_free37.csv` | yes | MATCH | PINNED |
| 198 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 90 | _(none; context: - Phase-3 bundle:)_ | `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b` | — | no | NO PATH CITED — unresolved | PINNED |
| 199 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 91 | _(none; context: - Phase-4 bundle:)_ | `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3` | — | no | NO PATH CITED — unresolved | PINNED |
| 200 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 92 | _(none; context: - Accepted theta-byte hash:)_ | `c024b89386c502003f9d4abb927b048dfab42c0bafe48d9a69d9fcb330f0580d` | — | no | NO PATH CITED — unresolved | PINNED |
| 201 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 93 | _(none; context: - Bread (Phase-4 Hessian) hash:)_ | `e9ca080ecc7e40e43881b9422af0095f23ad2bfef3e84648d2031a33eb9e4061` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/attempts/20260729T121430Z_322592_6a8a24821914433f9f4303f2a6459025_curvature_STOPPED/hessian_free.npy` | PINNED |
| 202 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 112 | _(none; context: )_ | `7f71a532ff66a1e882f4a085ca78e14a9788e6c98cff8c04957b9df4c3ff4a80` | — | no | NO PATH CITED — unresolved | PINNED |
| 203 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 130 | `phase5_manifest.json.accepted_binding` | `08be1cf6a7be0ff64a6417aef8e979003f5fa4f48f826b4d202ffd50c1f161d9` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 204 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 131 | `phase5_manifest.json.accepted_binding` | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` | — | no | PATH UNRESOLVED (ambiguous: 2 candidates); hash matches `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | PINNED |
| 205 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 133 | _(none; context: )_ | `7f71a532ff66a1e882f4a085ca78e14a9788e6c98cff8c04957b9df4c3ff4a80` | — | no | NO PATH CITED — unresolved | PINNED |
| 206 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 137 | `scripts/p2a/run_p2a_phase5_inference.py` | `d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232` | `MNL/scripts/p2a/run_p2a_phase5_inference.py` | yes | MISMATCH — no matching historical version | PINNED |
| 207 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 185 | `scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` | `MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | yes | MATCH | PINNED |
| 208 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 464 | `dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | `49bf6b7048f0065f248bf49dc750797ca9d9809c2aade29bd8808baeea2ceeed` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | yes | MISMATCH — file changed since; cited hash = version at `99a727c189` | PINNED |
| 209 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 807 | `hessian_eigenvalues.csv` | `f29a1a1b31cbfe73e9359c6e38f175cd55e744744d0835a006511afe10476611` | `MNL/outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/attempts/20260729T121430Z_322592_6a8a24821914433f9f4303f2a6459025_curvature_STOPPED/hessian_eigenvalues.csv` | yes | MATCH | PINNED |
| 210 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 808 | `hessian_free.csv` | `8985b619858ce8b6c5f4bbb2700bfbb7c22333c17538cc1eb8dc5b09b58f470e` | `MNL/outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/attempts/20260729T121430Z_322592_6a8a24821914433f9f4303f2a6459025_curvature_STOPPED/hessian_free.csv` | yes | MATCH | PINNED |
| 211 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 809 | `hessian_free.npy` | `e9ca080ecc7e40e43881b9422af0095f23ad2bfef3e84648d2031a33eb9e4061` | `MNL/outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/attempts/20260729T121430Z_322592_6a8a24821914433f9f4303f2a6459025_curvature_STOPPED/hessian_free.npy` | yes | MATCH | PINNED |
| 212 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 810 | `hessian_free.npy` | `581a307e92534277534c04fedf150044b651e5ef65beffde7e29e5f7983c887d` | — | no | NOT FOUND (ambiguous: 4 candidates) | PINNED |
| 213 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 811 | `phase4_diagnostics.json` | `5facb3ab9a6aa326e688eede781da8178b6033569c5891eb7bd0b8197ba3a1f3` | `MNL/outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/complete/phase4_diagnostics.json` | yes | MATCH | PINNED |
| 214 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 812 | `regional_hessian_subblock.csv` | `2dc64925319773235d6ceb30c49aa4cf59a44781af4c592eb0bd017f9511b909` | `MNL/outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/attempts/20260729T121430Z_322592_6a8a24821914433f9f4303f2a6459025_curvature_STOPPED/regional_hessian_subblock.csv` | yes | MATCH | PINNED |
| 215 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 813 | `regional_schur_complement.csv` | `c00127bbb650d7edf46934e1e6189d5e88dd470ca616df4312b808c57705614d` | `MNL/outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/attempts/20260729T121430Z_322592_6a8a24821914433f9f4303f2a6459025_curvature_STOPPED/regional_schur_complement.csv` | yes | MATCH | PINNED |
| 216 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 825 | _(none; context: )_ | `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3` | — | no | NO PATH CITED — unresolved | PINNED |
| 217 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 943 | `estimation_results.json → results.joint.theta` | `c024b89386c502003f9d4abb927b048dfab42c0bafe48d9a69d9fcb330f0580d` | — | no | NOT FOUND (not found) | PINNED |
| 218 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 953 | _(none; context: )_ | `2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b` | — | no | NO PATH CITED — unresolved | PINNED |
| 219 | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 957 | `phase4_manifest.json → accepted_phase3_bundle_sha256` | `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3` | — | no | NOT FOUND (not found) | PINNED |
| 220 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 32 | _(none; context: S11 singles parameter table)_ | `cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | PINNED |
| 221 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 33 | _(none; context: S11 couples parameter table)_ | `fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | PINNED |
| 222 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 34 | _(none; context: S10 singles frame)_ | `641ceb0ed47b38111c4bac25deb9dd0d1f5942b931a694cd4cc1cec13d429128` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | PINNED |
| 223 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 35 | _(none; context: S10 couples frame)_ | `50b8289e97ceef16d767ce5799d9f0a712100c4db051444be630b1a56b34345d` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | PINNED |
| 224 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 36 | _(none; context: S10 engine metadata)_ | `709cc8cc604db66484a3eb9e4c52a8123cefc83517294d26bc2cc88169e352d7` | — | no | PATH UNRESOLVED (no path cited); hash matches `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/engine_metadata_criterion_a_v1.json` | PINNED |
| 225 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 49 | `baseline_f1.py` | `d103c947a5d735619c4b619c0d9c06c06be1c38f56706c5c3fe8c6d8e50bb4dc` | — | no | NOT FOUND (ambiguous: 2 candidates) | PINNED |
| 226 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 69 | `engine_jax.py` | `681420523f1efb76389c624e437549ee8971184672327d483296862708845983` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | yes | MATCH | PINNED |
| 227 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 86 | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/baseline_f1_prep_v1/baseline_f1_households_v1.jsonl` | `d4dd47a3b8d97e698cf3e87b22f602215d2c56195a8d8ce3a8a1c4b5db5faa20` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/baseline_f1_prep_v1/baseline_f1_households_v1.jsonl` | yes | MATCH | PINNED |
| 228 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 170 | `baseline_f1_verification_households_v1.jsonl` | `a412750b155d510daeb22b2e05e39b121f9a9c1da3d66a6a0523173e8fe2d1d9` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/baseline_f1_prep_v1/baseline_f1_verification_households_v1.jsonl` | yes | MATCH | PINNED |
| 229 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 171 | `baseline_f1_verification_oracle_v1.jsonl` | `c41439169c5386db88d0372c35d1ffcaa022de39d5d9af9d981b8dfc5a1ff150` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/baseline_f1_prep_v1/baseline_f1_verification_oracle_v1.jsonl` | yes | MATCH | PINNED |
| 230 | `MNL/docs/corr/baseline_f1_verification_v1.md` | 172 | `baseline_f1_verification_summary_v1.json` | `81d7371a127628cfe75f5c65007fc86db0ca35d36fdede9795cd0c39a638e51e` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/baseline_f1_prep_v1/baseline_f1_verification_summary_v1.json` | yes | MATCH | PINNED |

### 2b. Path citations without a hash

930 distinct (document, path) citations; 615 resolve to an existing file; 315 do not (not found / ambiguous basename / glob). PINNED by the card's rule; existence only.

| Citing document | Line | Cited path | Resolved to | Exists | Pin |
|---|---:|---|---|---|---|
| `Job_Market_paper/JMP_literature/00_admin/JMP_DR03_verification_log_v1.md` | 5 | `JMP_DR03_assimilation_decision_v1.md` | `Job_Market_paper/JMP_literature/00_admin/JMP_DR03_assimilation_decision_v1.md` | yes | PINNED |
| `Job_Market_paper/JMP_literature/00_admin/JMP_DR03_verification_log_v1.md` | 5 | `JMP_DR03_tier_update_v1.csv` | `Job_Market_paper/JMP_literature/00_admin/JMP_DR03_tier_update_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 35 | `W1_latent_set_identification_note_v1.md` | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 36 | `JMP_W1_reference_domain_fork_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 64 | `jobs_and_wellbeing.tex` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 64 | `jobs_and_wellbeing.md` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.md` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 66 | `JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 67 | `JMP_measure_map_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 68 | `baseline_f1_verification_v1.md` | `MNL/docs/corr/baseline_f1_verification_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 175 | `JMP_W1_stochastic_ability_set_bridge_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 191 | `JMP_W1_stochastic_ability_set_bridge_review_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 203 | `JMP_BASELINE_F1_equivalised_reporting_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 203 | `JMP_BASELINE_F1_equivalised_reporting_verification_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | 215 | `JMP_positive_fit_diagnostics_memo_v2_S12.md` | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2_S12.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 5 | `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` | `Job_Market_paper/docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 47 | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md` | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 59 | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v2.md` | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 64 | `Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md` | `MNL/Results/P3a/pooled_P3a/JMP_pooled_P3a_estimation_report_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 66 | `JMP_pooled_P3a_estimation_report_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 131 | `FR_P2a_region_live_phase4_remediation_report_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 132 | `FR_P2a_region_live_phase4_remediation_report_v3.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 133 | `FR_P2a_region_live_phase5_code_review_v4.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 133 | `Job_Market_paper/docs/prompts/JMP_M05B_closed_form_code_review_v4_prompt_v1.md` | `Job_Market_paper/docs/prompts/JMP_M05B_closed_form_code_review_v4_prompt_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 134 | `FR_P2a_streaming_incrementA_review_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 134 | `Job_Market_paper/docs/prompts/JMP_M05C_incrementA_review_v2_prompt_v1.md` | `Job_Market_paper/docs/prompts/JMP_M05C_incrementA_review_v2_prompt_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 159 | `JMP_HK_01_phase2_archive_manifest_v1.csv` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_phase2_archive_manifest_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 192 | `market.html` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 268 | `RURO_welfare_stage2_vdir_crosscheck_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 285 | `JMP_HK_01_v5_movable_rows_codex_review_v1.md` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_v5_movable_rows_codex_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 338 | `m08e_pins.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 338 | `m08_u6_pins_v2.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 353 | `JMP_cross_repo_artifact_manifest_v1.md` | `Job_Market_paper/docs/JMP_cross_repo_artifact_manifest_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 354 | `RURO_ACTIVE_RESULTS_REGISTRY.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 356 | `JMP_HK_01_phase2_supersession_map_v1.csv` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_phase2_supersession_map_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | 360 | `notebooks/france/fr_singles_results_discussion_v1.ipynb` | `MNL/notebooks/france/fr_singles_results_discussion_v1.ipynb` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` | 108 | `JMP_HK_01_inventory_and_disposition_register_v1.csv` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` | 109 | `JMP_HK_01_inventory_summary_v1.md` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_summary_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` | 110 | `JMP_HK_01_reference_protection_map_v1.csv` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_reference_protection_map_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_acceptance_rider_v1.md` | 19 | `JMP_literature_positioning_memo_v2.md` | `Job_Market_paper/docs/JMP_literature_positioning_memo_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_acceptance_rider_v1.md` | 23 | `docs/JMP_literature_positioning_memo_v3.md` | `Job_Market_paper/docs/JMP_literature_positioning_memo_v3.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_acceptance_rider_v1.md` | 24 | `docs/missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | 7 | `docs/Missions/JMP_M07I_positioning_memo_acceptance_rider_v1.md` | `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_acceptance_rider_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | 11 | `docs/JMP_literature_positioning_memo_v3.md` | `Job_Market_paper/docs/JMP_literature_positioning_memo_v3.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | 11 | `JMP_literature_positioning_memo_v2.md` | `Job_Market_paper/docs/JMP_literature_positioning_memo_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | 5 | `FR_P2a_m08e_codex_reverification_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | 13 | `C:/Users/hisham/Repo/MNL/outputs/p2a_singles2016/region_live_margqh_v1/e3_estimation_v2/attempts/20260819T214600Z_672360_410223ff1ccd4d12b85d48b36d60fb1e_margqh_v2_phase3equiv_tightened_E3_CONVERGED_SINGLE_OPTIMUM/e3_manifest.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/e3_estimation_v2/attempts/20260819T214600Z_672360_410223ff1ccd4d12b85d48b36d60fb1e_margqh_v2_phase3equiv_tightened_E3_CONVERGED_SINGLE_OPTIMUM/e3_manifest.json` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | 16 | `C:/Users/hisham/Repo/MNL/outputs/p2a_singles2016/region_live_margqh_v1/e4_curvature_inference_v2/attempts/20260819T214723Z_763848_8304bf6f33d94beba38b05a498049d01_margqh_v2_p4p5equiv_E4_PASS/e4_manifest.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/e4_curvature_inference_v2/attempts/20260819T214723Z_763848_8304bf6f33d94beba38b05a498049d01_margqh_v2_p4p5equiv_E4_PASS/e4_manifest.json` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | 19 | `FR_P2a_m08e_E3_reestimation_note_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | 20 | `FR_P2a_m08e_E4_curvature_inference_note_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | 65 | `MNL/notebooks/france/fr_singles_pipeline_v3_working.ipynb` | `MNL/notebooks/france/fr_singles_pipeline_v3_working.ipynb` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | 68 | `MNL/notebooks/france/fr_singles_results_preview_v1.ipynb` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | 71 | `dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v2.ipynb` | `dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v2.ipynb` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_E2_parity_report_v3_documentary_correction_ruling_v1.md` | 16 | `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3.md` | `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_E2_parity_report_v3_documentary_correction_ruling_v1.md` | 94 | `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3_change_log.md` | `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3_change_log.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_E2_parity_report_v3_documentary_correction_ruling_v1.md` | 141 | `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v3_acceptance.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_LOC4_design_rereview_v4_accept_v1.md` | 5 | `JMP_M08_LOC4_robustness_design_v4.md` | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_robustness_design_v4.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 4 | `JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 265 | `JMP_M08_LOC4_manuscript_claim_set_v2.md` | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_manuscript_claim_set_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | 267 | `JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md` | 110 | `docs/missions/JMP_M08_singles_welfare_execution_contract_v1.md` | `Job_Market_paper/docs/missions/JMP_M08_singles_welfare_execution_contract_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_ruling_v1.md` | 108 | `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_ruling_v1.md` | 340 | `MNL/docs/France_case/P2a/FR_P2a_m08_welfare_proposal_validation_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_ruling_v1.md` | 341 | `MNL/docs/France_case/P2a/FR_P2a_m08_welfare_proposal_codex_review_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_remediation_ruling_v1.md` | 342 | `Job_Market_paper/docs/Missions/JMP_M08_U6_welfare_proposal_acceptance_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | 22 | `Literature_collection.md` | `Job_Market_paper/Literature/Literature_collection.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | 57 | `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4.md` | `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | 81 | `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_change_log.md` | `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_change_log.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v1.md` | 5 | `JMP_M08_goal1_rulings_register_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v1.md` | 116 | `docs/Missions/JMP_M08_stageA_contract_review_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_stageA_contract_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v2.md` | 5 | `JMP_M08_goal1_rulings_register_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v2.md` | 116 | `docs/Missions/JMP_M08_stageA_contract_review_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_stageA_contract_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v3.md` | 5 | `JMP_M08_goal1_rulings_register_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v3.md` | 116 | `docs/Missions/JMP_M08_stageA_contract_review_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_stageA_contract_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v3.md` | 193 | `welfare_stage1_w3.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5 | `JMP_M08_goal1_rulings_register_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 116 | `docs/Missions/JMP_M08_stageA_contract_review_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_stageA_contract_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 193 | `welfare_stage1_w3.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 955 | `JMP_HK_01_inventory_and_disposition_register_v4.csv` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v4.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1093 | `control_variate_design_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1848 | `JMP_HK_01_inventory_and_disposition_register_v6.csv` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v6.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1855 | `FR_P2a_region_live_phase4_remediation_report_v4.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1856 | `FR_P2a_region_live_phase4_remediation_report_v5.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1857 | `RURO_welfare_stage2_vdir_crosscheck_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1952 | `docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 1993 | `JMP_HK_01_inventory_and_disposition_register_v7.csv` | `Job_Market_paper/docs/Missions/HK01/JMP_HK_01_inventory_and_disposition_register_v7.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2000 | `JMP_pooled_P3a_estimation_report_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2165 | `FR_P2a_m08_parity_path_closure_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2181 | `JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2193 | `JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2314 | `FR_P2a_m08_loc4_beta_w_pexp2_profile_results_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2315 | `FR_P2a_m08_loc4_rqmc_final_precision_results_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2316 | `FR_P2a_m08_loc4_tier2_independent_review_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2317 | `JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2318 | `JMP_M08_LOC4_manuscript_claim_set_v2.md` | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_manuscript_claim_set_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2638 | `scripts/loc4/run_loc4_stage2_comparison.py` | `MNL/scripts/loc4/run_loc4_stage2_comparison.py` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2639 | `notebooks/france/fr_singles_results_discussion_v1.ipynb` | `MNL/notebooks/france/fr_singles_results_discussion_v1.ipynb` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2656 | `rqmc_gates_r3fix.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 2679 | `docs/Missions/JMP_current_state_dashboard_v1.md` | `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3031 | `docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3032 | `docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3033 | `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_v2.md` | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_manuscript_claim_set_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3365 | `scripts/ps1/run_ps1_item4_fit_suite.py` | `MNL/scripts/ps1/run_ps1_item4_fit_suite.py` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3366 | `post_estimation_comparison.html` | — (ambiguous: 3 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3436 | `scripts/ps1/run_ps1_s8_acceptance.py` | `MNL/scripts/ps1/run_ps1_s8_acceptance.py` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3527 | `experiments/JMP_PS1/decision_note.md` | `MNL/experiments/JMP_PS1/decision_note.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3623 | `decision_note.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3688 | `specification_matrix.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3689 | `model_comparison.csv` | — (ambiguous: 4 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3857 | `experiments/JMP_PS1/runs/ps1r1_bmo/r1bmo_secure_env_bundle_v1.zip` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/r1bmo_secure_env_bundle_v1.zip` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3869 | `Design/JMP_paper_outline_v1.md` | `Job_Market_paper/Design/JMP_paper_outline_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3887 | `inventory.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3888 | `silc_db040_test.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3888 | `lfs_hours_table.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 3888 | `RUNBOOK.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 4393 | `experiments/JMP_PS1/welfare_decomposition_comparison.csv` | `MNL/experiments/JMP_PS1/welfare_decomposition_comparison.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 4394 | `experiments/JMP_PS1/post_estimation_comparison.html` | `MNL/experiments/JMP_PS1/post_estimation_comparison.html` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 4967 | `DRD_FR_2016_a3_export.txt` | — (ambiguous: 5 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5114 | `m08_normalisation.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5267 | `experiments/JMP_PS1/model_comparison.csv` | `MNL/experiments/JMP_PS1/model_comparison.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5938 | `scripts/ps1/run_ps1_laneB_step0_docaudit.py` | `MNL/scripts/ps1/run_ps1_laneB_step0_docaudit.py` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5939 | `run_ps1_laneB_step0_wage_audit.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5939 | `run_ps1_laneB_step1_channel_probe.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5949 | `Data/documentation/DRD_FR_2016_a3_export.txt` | `MNL/Data/documentation/DRD_FR_2016_a3_export.txt` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5956 | `EUROMOD-STORAGE/Data/FR/drd/DRD_FR_2018_a2_export.txt` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/FR/drd/DRD_FR_2018_a2_export.txt` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5958 | `Data/documentation/euromod_fr_2015_2017_input_variables.csv` | `MNL/Data/documentation/euromod_fr_2015_2017_input_variables.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 5988 | `dclaborsupply/likelihood/engine_numpy.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 6240 | `experiments/JMP_PS1/sample_expansion_audit.csv` | `MNL/experiments/JMP_PS1/sample_expansion_audit.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 6241 | `experiments/JMP_PS1/sample_expansion_design.yaml` | `MNL/experiments/JMP_PS1/sample_expansion_design.yaml` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 7189 | `Literature/Decoster_Haan_2015_Empirical welfare analysis with preference heterogeneity [2013 VfS working paper].pdf` | `Job_Market_paper/Literature/Decoster_Haan_2015_Empirical welfare analysis with preference heterogeneity [2013 VfS working paper].pdf` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 7336 | `scripts/welfare/m08_p2a_parity.py` | `MNL/scripts/welfare/m08_p2a_parity.py` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 7356 | `Literature_collection.md` | `Job_Market_paper/Literature/Literature_collection.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 7357 | `JMP_literature_review_skeleton_v1.md` | `Job_Market_paper/JMP_literature_review_skeleton_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 7745 | `sample_expansion_design.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8035 | `experiments/JMP_SEMINAR_SPRINT/{run_registry.csv` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8036 | `decision_log.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8036 | `JMP_GPU_lab.ipynb` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8360 | `experiments/JMP_SEMINAR_SPRINT/run_registry.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/run_registry.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8361 | `experiments/JMP_SEMINAR_SPRINT/model_comparison.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/model_comparison.csv` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8362 | `experiments/JMP_SEMINAR_SPRINT/decision_log.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/decision_log.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8366 | `experiments/JMP_SEMINAR_SPRINT/JMP_GPU_lab.ipynb` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8748 | `JMP_working_paper_for_seminar_v1.md` | `Job_Market_paper/manuscript/JMP_working_paper_for_seminar_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8758 | `JMP_seminar_deck_content_v1.md` | `Job_Market_paper/manuscript/JMP_seminar_deck_content_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8861 | `MNL/experiments/JMP_PS1/decision_note.md` | `MNL/experiments/JMP_PS1/decision_note.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 8862 | `JMP/docs/Missions/JMP_current_state_dashboard_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 9256 | `run_registry.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | 9596 | `headline_decomposition_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 11 | `JMP_M08_singles_welfare_execution_contract_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_singles_welfare_execution_contract_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 31 | `*.md` | — (glob pattern) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 33 | `docs/governance/JMP_decision_log_v1.md` | `Job_Market_paper/docs/governance/JMP_decision_log_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 44 | `MNL docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 67 | `…_v2.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 67 | `…_v3.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 80 | `JMP_M07I_identity_alignment_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 106 | `JMP_M07I_positioning_memo_rider_acceptance_v1.md` | `Job_Market_paper/docs/Missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 187 | `RURO_welfare_scaffold_design_contract_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | 199 | `JMP_M08_ability_preference_operators_design_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_ability_preference_operators_design_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_opportunity_normalisation_and_notebook_restart_ruling_v1.md` | 9 | `fr_singles_pipeline_v2.ipynb` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_opportunity_normalisation_and_notebook_restart_ruling_v1.md` | 257 | `JMP_welfare_spec_v6.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_opportunity_normalisation_and_notebook_restart_ruling_v1.md` | 267 | `dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v2.ipynb` | `dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v2.ipynb` | yes | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_opportunity_normalisation_and_notebook_restart_ruling_v1.md` | 282 | `JMP_M08_goal_manager_acceptance_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_opportunity_normalisation_and_notebook_restart_ruling_v1.md` | 292 | `MNL/notebooks/france/fr_singles_pipeline_v3.ipynb` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_proposal_density_convention_and_corrected_baseline_ruling_v1.md` | 113 | `Job_Market_paper/docs/Missions/JMP_M08E_proposal_correction_estimand_audit_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_proposal_density_convention_and_corrected_baseline_ruling_v1.md` | 307 | `fr_singles_pipeline_v2.ipynb` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/Missions/JMP_M08_proposal_density_convention_and_corrected_baseline_ruling_v1.md` | 314 | `MNL/notebooks/france/fr_singles_pipeline_v3.ipynb` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05C_goal_manager_dryrun_acceptance_v1.md` | 5 | `docs/missions/JMP_M05C_goal_manager_dryrun_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M05C_goal_manager_dryrun_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_deputy_programme_acceptance_v1.md` | 89 | `.npy` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | 6 | `docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | 26 | `hessian_free.npy` | — (ambiguous: 4 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | 54 | `phase5_scores_free.npy` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | 58 | `.npy` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | 82 | `JMP_M05_mission_ledger_v3.md` | `Job_Market_paper/docs/missions/JMP_M05_mission_ledger_v3.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | 82 | `phase5_parameter_map_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | 82 | `phase5_source_inventory_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | 82 | `JMP_M05_source_verification_completeness_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 11 | `FR_P2a_region_live_phase5_source_verification_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 11 | `phase5_parameter_map_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 11 | `phase5_source_inventory_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 52 | `theta_estimated.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 58 | `run_p2a_regionlive_rebuild.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 58 | `engine_jax.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 75 | `hessian_free.csv` | — (ambiguous: 4 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 75 | `hessian_free.npy` | — (ambiguous: 4 candidates) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 75 | `.npy` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 110 | `JMP_M05_stageA_correction_memo_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_stageA_correction_memo_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_source_verification_completeness_v1.md` | 110 | `JMP_M05_inference_design_prompt_v1.md` | `Job_Market_paper/docs/prompts/JMP_M05_inference_design_prompt_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md` | 4 | `JMP_M05_task_plan_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 12 | `docs/design_notes/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 13 | `JMP_M07I_manuscript_identity_alignment_charter_v1.md` | `Job_Market_paper/docs/missions/JMP_M07I_manuscript_identity_alignment_charter_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 14 | `docs/JMP_project_state_identity_addendum_v2.md` | `Job_Market_paper/docs/JMP_project_state_identity_addendum_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 15 | `docs/JMP_core_packet_v3.md` | `Job_Market_paper/docs/JMP_core_packet_v3.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 15 | `manuscript/JMP_abstract_clean_v3.md` | `Job_Market_paper/manuscript/JMP_abstract_clean_v3.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 15 | `manuscript/JMP_extended_abstract_clean_v3.md` | `Job_Market_paper/manuscript/JMP_extended_abstract_clean_v3.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 15 | `manuscript/JMP_intro_skeleton_v3.md` | `Job_Market_paper/manuscript/JMP_intro_skeleton_v3.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 16 | `manuscript/sections/FR_P2a_empirical_inference_v2.md` | `Job_Market_paper/manuscript/sections/FR_P2a_empirical_inference_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 23 | `JMP_M07I_stageB_independent_consistency_review_v1.md` | `Job_Market_paper/docs/missions/JMP_M07I_stageB_independent_consistency_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 23 | `FR_P2a_empirical_inference_v2.md` | `Job_Market_paper/manuscript/sections/FR_P2a_empirical_inference_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 24 | `JMP_project_state_latest.md` | `Job_Market_paper/docs/JMP_project_state_latest.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 36 | `JMP_literature_positioning_memo_v2.md` | `Job_Market_paper/docs/JMP_literature_positioning_memo_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 44 | `JMP_core_packet_v1.md` | `Job_Market_paper/Design/JMP_core_packet_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 44 | `v2.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 44 | `JMP_abstract_clean_v1.md` | `Job_Market_paper/Design/JMP_abstract_clean_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 44 | `JMP_extended_abstract_clean_v1.md` | `Job_Market_paper/Design/JMP_extended_abstract_clean_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 44 | `JMP_intro_skeleton_v1.md` | `Job_Market_paper/Design/JMP_intro_skeleton_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | 44 | `docs/JMP_project_state_identity_addendum_v1.md` | `Job_Market_paper/docs/JMP_project_state_identity_addendum_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | 17 | `manuscript/sections/FR_P2a_empirical_inference_v2.md` | `Job_Market_paper/manuscript/sections/FR_P2a_empirical_inference_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | 18 | `manuscript/appendices/FR_P2a_inference_appendix_note_v2.md` | `Job_Market_paper/manuscript/appendices/FR_P2a_inference_appendix_note_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | 22 | `docs/results/FR_P2a_phase5_inference_results_memo_v1.md` | `Job_Market_paper/docs/results/FR_P2a_phase5_inference_results_memo_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | 23 | `docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv` | `Job_Market_paper/docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | 24 | `docs/missions/JMP_M07_stageC_independent_economics_review_v1.md` | `Job_Market_paper/docs/missions/JMP_M07_stageC_independent_economics_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | 25 | `docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | 26 | `docs/missions/JMP_M08_welfare_input_handoff_v1.md` | `Job_Market_paper/docs/missions/JMP_M08_welfare_input_handoff_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | 27 | `docs/missions/JMP_M07_stageB_author_cover_note_v1.md` | `Job_Market_paper/docs/missions/JMP_M07_stageB_author_cover_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | 5 | `docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | 9 | `FR_P2a_empirical_inference_v2.md` | `Job_Market_paper/manuscript/sections/FR_P2a_empirical_inference_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | 9 | `FR_P2a_inference_appendix_note_v2.md` | `Job_Market_paper/manuscript/appendices/FR_P2a_inference_appendix_note_v2.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | 9 | `JMP_M07_stageB_author_cover_note_v1.md` | `Job_Market_paper/docs/missions/JMP_M07_stageB_author_cover_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | 21 | `JMP_M08_welfare_input_handoff_v1.md` | `Job_Market_paper/docs/missions/JMP_M08_welfare_input_handoff_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | 1 | `JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | 10 | `JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | 119 | `JMP_counterfactual_attainment_design_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 1 | `JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 9 | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 14 | `docs/normative/JMP_W1_reference_domain_fork_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 19 | `W1_latent_set_identification_note_v1.md` | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 67 | `discussion2.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 80 | `r240_step3_parameter_table_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 93 | `JMP_measure_map_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 114 | `m08_welfare_measures.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 123 | `s12_w4_premise_audit_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 127 | `JMP_counterfactual_attainment_design_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 166 | `docs/normative/JMP_measure_map_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | 245 | `JMP_W1_reference_domain_fork_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 15 | `docs/normative/scripts/fork_derived_numerals_v1.py` | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 17 | `docs/normative/fork_derived_numerals_v1.csv` | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 27 | `experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 38 | `docs/normative/W1_latent_set_identification_note_v1.md` | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 51 | `fork_derived_numerals_v1.csv` | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 55 | `Theory_other_project/jobs_and_wellbeing.tex` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 56 | `jobs_and_wellbeing.agent.md` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.agent.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 95 | `The_draft_theorypaper.tex` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 191 | `pff_step1_reference_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 337 | `agent.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 404 | `discussion2.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 433 | `beamer/reference/Theory_talk/slides/spoken_script_click_cues.tex` | `Job_Market_paper/beamer/reference/Theory_talk/slides/spoken_script_click_cues.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 455 | `Literature/markdowns/Dagsvik_Jia_2016.md` | `Job_Market_paper/Literature/markdowns/Dagsvik_Jia_2016.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 775 | `s11_couples_parameter_table_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 937 | `JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 955 | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | 957 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 1 | `JMP_W1_stochastic_ability_set_bridge_review_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 6 | `JMP_W1_stochastic_ability_set_bridge_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 14 | `JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 14 | `JMP_BRIDGE1_amendment_v1.md` | `Job_Market_paper/docs/JMP_BRIDGE1_amendment_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 15 | `Jobs_and_wellbeing.tex` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 15 | `jobs_and_wellbeing_agent.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 15 | `jobs_and_wellbeing.md` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 17 | `W1_latent_set_identification_note_v1.md` | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 18 | `JMP_W1_reference_domain_fork_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 18 | `JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 19 | `JMP_bridge_source_extract_v1.md` | `Job_Market_paper/docs/JMP_bridge_source_extract_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 19 | `JMP_bridge_source_extract_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 20 | `JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 20 | `JMP_measure_map_acceptance_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 20 | `baseline_f1_verification_v1.md` | `MNL/docs/corr/baseline_f1_verification_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | 21 | `JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 1 | `JMP_W1_stochastic_ability_set_bridge_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 7 | `JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 7 | `JMP_BRIDGE1_amendment_v1.md` | `Job_Market_paper/docs/JMP_BRIDGE1_amendment_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 10 | `JMP_W1_stochastic_ability_set_bridge_v*.md` | — (glob pattern) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 11 | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 17 | `jobs_and_wellbeing.tex` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 17 | `jobs_and_wellbeing_agent.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 17 | `.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 18 | `JMP_bridge_source_extract_v1.md` | `Job_Market_paper/docs/JMP_bridge_source_extract_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 19 | `JMP_bridge_source_extract_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 20 | `W1_latent_set_identification_note_v1.md` | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 21 | `JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 21 | `JMP_measure_map_acceptance_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 21 | `baseline_f1_verification_v1.md` | `MNL/docs/corr/baseline_f1_verification_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 23 | `JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 42 | `continuous.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 206 | `alternatives/continuous.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 561 | `engine_jax.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 590 | `estimation_spec_S8_corrected_floor5_v1.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 590 | `estimation_spec_couples_clean_r240_v1.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | 652 | `JMP_W1_stochastic_ability_set_bridge_review_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 1 | `JMP_bridge_review_factual_items_v1.md` | `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 5 | `JMP_W1_stochastic_ability_set_bridge_review_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 8 | `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 16 | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 17 | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 49 | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/alternatives/continuous.py` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/alternatives/continuous.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 72 | `estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | — (ambiguous: 4 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 82 | `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml` | `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 93 | `MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml` | `MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 104 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 140 | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 158 | `continuous.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | 158 | `s10_estimation_lib_v1.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 5 | `JMP_bridge_source_extract_v1.md` | `Job_Market_paper/docs/JMP_bridge_source_extract_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 13 | `estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | — (ambiguous: 4 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 14 | `estimation_spec_S8_corrected_floor5_v1.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 15 | `estimation_spec_couples_clean_r240_v1.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 32 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 34 | `MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | `MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 39 | `s11_welfare_specs_of_record_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 39 | `run_s11_welfare_specs_of_record_v1.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 97 | `RURO_couples_leisure_profile_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 144 | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 296 | `engine_jax.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 302 | `continuous.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 314 | `MNL/dclaborsupply-monorepo/.../alternatives/continuous.py` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 351 | `requirements.txt` | `MNL/requirements.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 354 | `MNL_posfit/scripts/diagnostics/build_positive_fit_diagnostics_v2b.py` | `MNL_posfit/scripts/diagnostics/build_positive_fit_diagnostics_v2b.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 355 | `build_positive_fit_diagnostics_v2.py` | `MNL_posfit/scripts/diagnostics/build_positive_fit_diagnostics_v2.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 359 | `outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 378 | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 397 | `Job_Market_paper/1stfolder/J of Applied Econometrics - 2015 - Dagsvik - Labor Supply as a Choice Among Latent Jobs  Unobserved Heterogeneity and.pdf` | `Job_Market_paper/1stfolder/J of Applied Econometrics - 2015 - Dagsvik - Labor Supply as a Choice Among Latent Jobs  Unobserved Heterogeneity and.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | 399 | `Job_Market_paper/JMP_lit_collection/files/41/Dagsvik and Jia - 2016 - Labor Supply as a Choice Among Latent Jobs Unobserved Heterogeneity and Identification LABOR SUPPL.pdf` | `Job_Market_paper/JMP_lit_collection/files/41/Dagsvik and Jia - 2016 - Labor Supply as a Choice Among Latent Jobs Unobserved Heterogeneity and Identification LABOR SUPPL.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_direct_g_welfare_ruling_v1.md` | 63 | `JMP_RURO_direct_opportunity_welfare_design_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_direct_g_welfare_ruling_v1.md` | 131 | `Literature_collection.md` | `Job_Market_paper/Literature/Literature_collection.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 1 | `JMP_measure_map_acceptance_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 9 | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 13 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 15 | `MNL/docs/corr/baseline_f1_prep2_report_v1.md` | `MNL/docs/corr/baseline_f1_prep2_report_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 17 | `JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 17 | `JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 89 | `gate/measure_map_accepted.json` | `MNL/gate/measure_map_accepted.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 89 | `MNL/scripts/welfare/run_baseline_f1_full_sample.py` | `MNL/scripts/welfare/run_baseline_f1_full_sample.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 92 | `JMP_measure_map_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | 105 | `JMP_counterfactual_attainment_design_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 4 | `JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 59 | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 61 | `MNL/scripts/welfare/m08_welfare_measures.py` | `MNL/scripts/welfare/m08_welfare_measures.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 75 | `MNL/scripts/welfare/run_m08_u6e_functionals.py` | `MNL/scripts/welfare/run_m08_u6e_functionals.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 81 | `MNL/scripts/welfare/m08_normalisation_tests.py` | `MNL/scripts/welfare/m08_normalisation_tests.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 85 | `MNL/scripts/welfare/run_m08_welfare_decomposition.py` | `MNL/scripts/welfare/run_m08_welfare_decomposition.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 89 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/run_s12_welfare_record_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/run_s12_welfare_record_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 100 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_principal_welfare_distributions_v1.parquet` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_principal_welfare_distributions_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 100 | `s12_welfare_record_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 100 | `s12_w4_premise_audit_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 103 | `MNL/scripts/welfare/fastlane/run_f4a_singles_measure_core.py` | `MNL/scripts/welfare/fastlane/run_f4a_singles_measure_core.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 105 | `MNL/scripts/welfare/fastlane/run_f4c_final_singles_measures.py` | `MNL/scripts/welfare/fastlane/run_f4c_final_singles_measures.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 105 | `run_f5_singles_measure_family.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 108 | `MNL/scripts/welfare/run_m08_u6f_functionals16.py` | `MNL/scripts/welfare/run_m08_u6f_functionals16.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 110 | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260825T164802Z_500708_1759e2e09f0941609ea183ae51ea8f20_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260825T164802Z_500708_1759e2e09f0941609ea183ae51ea8f20_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 124 | `s12_W3_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 126 | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 126 | `JMP_M08_singles_welfare_execution_contract_v5.md` | `Job_Market_paper/docs/Missions/JMP_M08_singles_welfare_execution_contract_v5.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 129 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/run_s12_w4_premise_audit_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/run_s12_w4_premise_audit_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 132 | `MNL/scripts/welfare/run_p2a_singles_welfare.py` | `MNL/scripts/welfare/run_p2a_singles_welfare.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 133 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/cw_states_lib_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/cw_states_lib_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 140 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 140 | `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md` | `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 144 | `s11_singles_parameter_table_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 145 | `s11_couples_parameter_table_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 146 | `couples_clean_baseline/r240_step3_parameter_table_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 147 | `scripts/bpool/specs/theta_hat_realdata_901_v1.csv` | `MNL/scripts/bpool/specs/theta_hat_realdata_901_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 148 | `scripts/welfare/configs/theta_hat_p2a_singles2016_v1.csv` | `MNL/scripts/welfare/configs/theta_hat_p2a_singles2016_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 153 | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 154 | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 156 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s4_corrected_frame/build_s4_corrected_frame_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s4_corrected_frame/build_s4_corrected_frame_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 156 | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/data/loader.py` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/data/loader.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 156 | `.../likelihood/engine_numpy.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 205 | `C:/Users/hisham/MNL/EUROMOD-STORAGE/new_data/fr_p3a_bpool_engine_ready_staged_threeB1__singles.parquet` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/new_data/fr_p3a_bpool_engine_ready_staged_threeB1__singles.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 223 | `welfare_identity_check_v1.md` | `MNL/docs/corr/welfare_identity_check_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 225 | `MNL/docs/corr/welfare_identity_check_v1.md` | `MNL/docs/corr/welfare_identity_check_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 246 | `cw_engine_ready_v1.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 249 | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/cw_engine_ready_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_couples_welfare/cw_engine_ready_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 249 | `MNL/scripts/bpool/harmonise_bpool_engine_ready.py` | `MNL/scripts/bpool/harmonise_bpool_engine_ready.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 268 | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/measure_map_1r/20260911/household_checks_v1.json` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/measure_map_1r/20260911/household_checks_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 311 | `experiments/JMP_SEMINAR_SPRINT/figures/captions/figD06_occupation_isco_and_model.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/captions/figD06_occupation_isco_and_model.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 312 | `experiments/JMP_SEMINAR_SPRINT/figures/captions/figD07_observed_wages_annualised.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/captions/figD07_observed_wages_annualised.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 313 | `experiments/JMP_SEMINAR_SPRINT/figures/captions/figD09_resource_components.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/captions/figD09_resource_components.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 314 | `experiments/JMP_SEMINAR_SPRINT/figures/figD06_occupation_isco_and_model.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD06_occupation_isco_and_model.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 315 | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 316 | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_paper.pdf` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_paper.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 317 | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_paper.png` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_paper.png` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 318 | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_slide.pdf` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_slide.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 319 | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_slide.png` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_slide.png` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 320 | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 321 | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_paper.pdf` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_paper.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 322 | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_paper.png` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_paper.png` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 323 | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_slide.pdf` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_slide.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 324 | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_slide.png` | `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_slide.png` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 325 | `experiments/JMP_SEMINAR_SPRINT/runs/couples_reprice_target_only/cpl_b_reprice_batched_switch_record_v1.json` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_reprice_target_only/cpl_b_reprice_batched_switch_record_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 326 | `experiments/JMP_SEMINAR_SPRINT/runs/couples_reprice_target_only/run_couples_reprice_batched_switch_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_reprice_target_only/run_couples_reprice_batched_switch_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 327 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_common_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_common_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 328 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_descriptives_continuous_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_descriptives_continuous_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 329 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_funnel_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_funnel_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 330 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_occupation_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_occupation_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 331 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_resource_components_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_resource_components_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 332 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_step1_funnel_v1.json` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_step1_funnel_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 333 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_step2_descriptives_v1.json` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_step2_descriptives_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 334 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/make_fd_figures_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/make_fd_figures_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 335 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/run_fd_step1_funnel_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/run_fd_step1_funnel_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 336 | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/run_fd_step2_descriptives_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/run_fd_step2_descriptives_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 337 | `experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/ne_step1_gate_v1.json` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/ne_step1_gate_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 338 | `experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 339 | `experiments/JMP_SEMINAR_SPRINT/tables/fd_descriptives_continuous_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/fd_descriptives_continuous_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 340 | `experiments/JMP_SEMINAR_SPRINT/tables/fd_descriptives_continuous_v1.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/fd_descriptives_continuous_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 341 | `experiments/JMP_SEMINAR_SPRINT/tables/fd_occupation_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/fd_occupation_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 342 | `experiments/JMP_SEMINAR_SPRINT/tables/fd_occupation_v1.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/fd_occupation_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 343 | `experiments/JMP_SEMINAR_SPRINT/tables/fd_resource_components_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/fd_resource_components_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 344 | `experiments/JMP_SEMINAR_SPRINT/tables/fd_resource_components_v1.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/fd_resource_components_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 345 | `experiments/JMP_SEMINAR_SPRINT/tables/fd_sample_funnel_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/fd_sample_funnel_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 346 | `experiments/JMP_SEMINAR_SPRINT/tables/fd_sample_funnel_v1.md` | `MNL/experiments/JMP_SEMINAR_SPRINT/tables/fd_sample_funnel_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 347 | `july2014.pdf` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 348 | `docs/corr/fr2016_drd_field_dictionary_v1.csv` | `MNL/docs/corr/fr2016_drd_field_dictionary_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 349 | `docs/corr/fr2016_source_audit_evidence_v1.json` | `MNL/docs/corr/fr2016_source_audit_evidence_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 350 | `docs/corr/fr2016_source_to_estimation_sample_audit_v1.md` | `MNL/docs/corr/fr2016_source_to_estimation_sample_audit_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 351 | `docs/corr/run_s12_consumption_floor_audit_v1.py` | `MNL/docs/corr/run_s12_consumption_floor_audit_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 352 | `docs/corr/s12_consumption_floor_audit_v1.csv` | `MNL/docs/corr/s12_consumption_floor_audit_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 353 | `docs/corr/s12_consumption_floor_audit_v1.json` | `MNL/docs/corr/s12_consumption_floor_audit_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 354 | `docs/corr/s12_consumption_floor_audit_v1.md` | `MNL/docs/corr/s12_consumption_floor_audit_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 355 | `docs/corr/target_integrability_checks_v1.json` | `MNL/docs/corr/target_integrability_checks_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 356 | `docs/corr/target_model_and_integrability_v1.md` | `MNL/docs/corr/target_model_and_integrability_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 357 | `docs/corr/welfare_finite_sum_examples_v1.csv` | `MNL/docs/corr/welfare_finite_sum_examples_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 358 | `docs/corr/welfare_finite_sum_examples_v1.md` | `MNL/docs/corr/welfare_finite_sum_examples_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 359 | `docs/corr/welfare_identity_check_v1.json` | `MNL/docs/corr/welfare_identity_check_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 360 | `docs/corr/welfare_identity_check_v1.md` | `MNL/docs/corr/welfare_identity_check_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 361 | `docs/corr/welfare_integrator_chosen_row_v1.md` | `MNL/docs/corr/welfare_integrator_chosen_row_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 362 | `Copy.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 363 | `docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1.md` | `MNL/docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 364 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/README.md` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/README.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 365 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_frame.json` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_frame.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 366 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_frame.py` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_frame.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 367 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_halton.json` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_halton.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 368 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_halton.py` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_halton.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 369 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/run_decomp.py` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/run_decomp.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 370 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/run_toy.py` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/run_toy.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 371 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/ss34_decomp_results.json` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/ss34_decomp_results.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 372 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/ss34_toy_results.json` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/ss34_toy_results.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 373 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/tables.py` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/tables.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 374 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/toy_sampler.py` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/toy_sampler.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 375 | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/toy_world.py` | `MNL/docs/jmp_methodology/evidence/ss34_criterion_audit_v1/toy_world.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 376 | `experiments/JMP_PS1/education_counts_raw.csv` | `MNL/experiments/JMP_PS1/education_counts_raw.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 377 | `experiments/JMP_PS1/runs/ps1_channelD/_baseline_full_snapshot.parquet` | `MNL/experiments/JMP_PS1/runs/ps1_channelD/_baseline_full_snapshot.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 378 | `experiments/JMP_PS1/runs/ps1_channelD/channelD_reference_profile_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1_channelD/channelD_reference_profile_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 379 | `experiments/JMP_PS1/runs/ps1_channelD/cs_common_correction_frame_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1_channelD/cs_common_correction_frame_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 380 | `experiments/JMP_PS1/runs/ps1_channelD/cs_common_nodes_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1_channelD/cs_common_nodes_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 381 | `experiments/JMP_PS1/runs/ps1_channelD/cs_common_priced_rows_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1_channelD/cs_common_priced_rows_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 382 | `experiments/JMP_PS1/runs/ps1_channelD/cs_common_slotmap_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1_channelD/cs_common_slotmap_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 383 | `experiments/JMP_PS1/runs/ps1_laneA_fourcell/operator_accounting_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1_laneA_fourcell/operator_accounting_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 384 | `experiments/JMP_PS1/runs/ps1c_fit_suite/calibration_curves.csv` | `MNL/experiments/JMP_PS1/runs/ps1c_fit_suite/calibration_curves.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 385 | `experiments/JMP_PS1/runs/ps1c_fit_suite/category_shares.csv` | `MNL/experiments/JMP_PS1/runs/ps1c_fit_suite/category_shares.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 386 | `experiments/JMP_PS1/runs/ps1c_fit_suite/chosen_prob_deciles.csv` | `MNL/experiments/JMP_PS1/runs/ps1c_fit_suite/chosen_prob_deciles.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 387 | `experiments/JMP_PS1/runs/ps1c_fit_suite/chosen_rank_deciles.csv` | `MNL/experiments/JMP_PS1/runs/ps1c_fit_suite/chosen_rank_deciles.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 388 | `experiments/JMP_PS1/runs/ps1c_fit_suite/confusion_long.csv` | `MNL/experiments/JMP_PS1/runs/ps1c_fit_suite/confusion_long.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 389 | `experiments/JMP_PS1/runs/ps1c_fit_suite/cube_top_misallocation.csv` | `MNL/experiments/JMP_PS1/runs/ps1c_fit_suite/cube_top_misallocation.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 390 | `experiments/JMP_PS1/runs/ps1c_fit_suite/post_estimation_comparison.html` | `MNL/experiments/JMP_PS1/runs/ps1c_fit_suite/post_estimation_comparison.html` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 391 | `experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_engine_ready_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_engine_ready_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 392 | `experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_frame_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_frame_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 393 | `experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_frame_v2.parquet` | `MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_frame_v2.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 394 | `experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_priced_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_priced_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 395 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/BUNDLE_MANIFEST_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/BUNDLE_MANIFEST_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 396 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/README_FIRST.md` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/README_FIRST.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 397 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/secure_env_protocol_v1.md` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/secure_env_protocol_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 398 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/verify_manifest.py` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/verify_manifest.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 399 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_array_inventory_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_array_inventory_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 400 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_bounds_pins_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_bounds_pins_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 401 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_columns_documentation_v1.md` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_columns_documentation_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 402 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_record_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_record_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 403 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_starts_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_starts_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 404 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_terms_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_terms_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 405 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_theta_of_record_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_theta_of_record_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 406 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/02_estimator/mnl_s8_numpy.py` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/02_estimator/mnl_s8_numpy.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 407 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/02_estimator/selftest_s8_negll.py` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/02_estimator/selftest_s8_negll.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 408 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/bmo_mapping_disclosures_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/bmo_mapping_disclosures_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 409 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/fap2009_to_loc4_T_v2.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/fap2009_to_loc4_T_v2.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 410 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/tension_z_matrix_22x4_v2_full.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/tension_z_matrix_22x4_v2_full.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 411 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/tension_z_matrix_22x4_v2_hc090.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/tension_z_matrix_22x4_v2_hc090.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 412 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/v2_audit_and_rebuild_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/v2_audit_and_rebuild_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 413 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/v2_fap_audit_and_map_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/v2_fap_audit_and_map_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 414 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/04_join/join_db040f_v1.py` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/04_join/join_db040f_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 415 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/education_inventory_v1.py` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/education_inventory_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 416 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/export_pack_v1.py` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/export_pack_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 417 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/lfs_desired_hours_v1.py` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/lfs_desired_hours_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 418 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/run_r1_estimations_v1.py` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/run_r1_estimations_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 420 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/join_diagnostics_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/join_diagnostics_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 421 | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/selftest_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/selftest_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 423 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/DARES_FAP2009_intro_et_table_de_correspondance.pdf` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/DARES_FAP2009_intro_et_table_de_correspondance.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 424 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/Matrice_PCS2020_ISCO08.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/Matrice_PCS2020_ISCO08.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 425 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/Matrice_PCS2020_ISCO08.xlsx` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/Matrice_PCS2020_ISCO08.xlsx` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 426 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/ResMetBE16.xlsx` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/ResMetBE16.xlsx` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 428 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/donnees_consolidees_2015.zip` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/donnees_consolidees_2015.zip` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 429 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/donnees_consolidees_2016.zip` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/donnees_consolidees_2016.zip` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 430 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/matrice_P2003_P2020.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/matrice_P2003_P2020.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 431 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/matrice_P2020_P2003.csv` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/matrice_P2020_P2003.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 432 | `experiments/JMP_PS1/runs/ps1r1_bmo/source/table_passage_PCS2003_PCS2020.xlsx` | `MNL/experiments/JMP_PS1/runs/ps1r1_bmo/source/table_passage_PCS2003_PCS2020.xlsx` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 433 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_HRS_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_HRS_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 434 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_OCC_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_OCC_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 435 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_OCCxHRS_v1.parquet` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_OCCxHRS_v1.parquet` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 436 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_hrs_parameter_table_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_hrs_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 437 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_occ_parameter_table_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_occ_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 438 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_occxhrs_parameter_table_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_occxhrs_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 439 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_frozen_parameter_table_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_frozen_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 440 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_proposal_fits_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_proposal_fits_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 441 | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_redraw_v1.json` | `MNL/experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_redraw_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 442 | `experiments/JMP_PS1/runs/ps1s16b_gw_structural/ps1s16b_b_h_parameter_table_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1s16b_gw_structural/ps1s16b_b_h_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 443 | `experiments/JMP_PS1/runs/ps1s16b_gw_structural/ps1s16b_b_nl_parameter_table_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1s16b_gw_structural/ps1s16b_b_nl_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 444 | `experiments/JMP_PS1/runs/ps1s8a_acceptance/ps1s8a_hours_grid_v1.csv` | `MNL/experiments/JMP_PS1/runs/ps1s8a_acceptance/ps1s8a_hours_grid_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 445 | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 446 | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.pdf` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 447 | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.png` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.png` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 448 | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization_caption.txt` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization_caption.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 449 | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/render_s11_normalization_figure_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/render_s11_normalization_figure_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 450 | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/run_s11_normalization_figure_v1.py` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/run_s11_normalization_figure_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 452 | `experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s2_hours_5_10_coverage_audit_v1.json` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s2_hours_5_10_coverage_audit_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 453 | `no_gsur_setup/requirements.txt` | `MNL/no_gsur_setup/requirements.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 454 | `no_gsur_setup/setup.ps1` | `MNL/no_gsur_setup/setup.ps1` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 455 | `outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__geometry_meta.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__geometry_meta.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 456 | `outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__mnlmeta.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__mnlmeta.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 457 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_hours_grid_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_hours_grid_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 458 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_manifest_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_manifest_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 459 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_parameter_table_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 460 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_spec_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_spec_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 461 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_hours_grid_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_hours_grid_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 462 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_manifest_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_manifest_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 463 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_parameter_table_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 464 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_spec_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_spec_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 465 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_hours_grid_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_hours_grid_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 466 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_manifest_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_manifest_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 467 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_parameter_table_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 468 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_spec_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_spec_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 469 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_hours_grid_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_hours_grid_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 470 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_manifest_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_manifest_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 471 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_parameter_table_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 472 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_spec_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_spec_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 473 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_hours_grid_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_hours_grid_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 474 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_manifest_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_manifest_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 475 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_parameter_table_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 476 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_spec_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_spec_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 477 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_hours_grid_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_hours_grid_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 478 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_manifest_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_manifest_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 479 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_parameter_table_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 480 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_spec_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_spec_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 481 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/ps1_battery_part1_manifest_20260829T132034Z.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/ps1_battery_part1_manifest_20260829T132034Z.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 482 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/ps1_model_comparison_part1_20260829T132034Z.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/ps1_model_comparison_part1_20260829T132034Z.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 483 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_derivation_note_v1.md` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_derivation_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 484 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_manifest_v1.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_manifest_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 485 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_result_block_v1.md` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_result_block_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 486 | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_verification_table_v1.csv` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_verification_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 487 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T202801Z_262600_80d94f8b9c994b4890d52d4a2ab735df_u6r_smoke/RESTRICTED_DO_NOT_PUBLISH.txt` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T202801Z_262600_80d94f8b9c994b4890d52d4a2ab735df_u6r_smoke/RESTRICTED_DO_NOT_PUBLISH.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 488 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T202850Z_133812_15108f9f85704ddc81c6729efb88e98b_u6resume2/RESTRICTED_DO_NOT_PUBLISH.txt` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T202850Z_133812_15108f9f85704ddc81c6729efb88e98b_u6resume2/RESTRICTED_DO_NOT_PUBLISH.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 489 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T203836Z_194344_736992b537f341aeb18d124f5716f41c_u6resume3/RESTRICTED_DO_NOT_PUBLISH.txt` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T203836Z_194344_736992b537f341aeb18d124f5716f41c_u6resume3/RESTRICTED_DO_NOT_PUBLISH.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 490 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T213827Z_671796_47f3785e9c8946b48fd41cc09b9f48ed_u6resume4/RESTRICTED_DO_NOT_PUBLISH.txt` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T213827Z_671796_47f3785e9c8946b48fd41cc09b9f48ed_u6resume4/RESTRICTED_DO_NOT_PUBLISH.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 491 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074210Z_535880_837a2a554a744991b320ffc7ffaf9129_normsmoke/RESTRICTED_DO_NOT_PUBLISH.txt` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074210Z_535880_837a2a554a744991b320ffc7ffaf9129_normsmoke/RESTRICTED_DO_NOT_PUBLISH.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 492 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074322Z_686888_47fdba224d9e40f0a61b12e63acd05b8_normsmoke2/RESTRICTED_DO_NOT_PUBLISH.txt` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074322Z_686888_47fdba224d9e40f0a61b12e63acd05b8_normsmoke2/RESTRICTED_DO_NOT_PUBLISH.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 493 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074423Z_472652_4f7193670e4542ae8229155aa77e8132_m08normfull/RESTRICTED_DO_NOT_PUBLISH.txt` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074423Z_472652_4f7193670e4542ae8229155aa77e8132_m08normfull/RESTRICTED_DO_NOT_PUBLISH.txt` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 494 | `scripts/corr/build_fr2016_source_audit_v1.py` | `MNL/scripts/corr/build_fr2016_source_audit_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 495 | `scripts/corr/check_target_integrability_v1.py` | `MNL/scripts/corr/check_target_integrability_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 496 | `scripts/corr/check_welfare_finite_sum_examples_v1.py` | `MNL/scripts/corr/check_welfare_finite_sum_examples_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 497 | `scripts/corr/check_welfare_identity_v1.py` | `MNL/scripts/corr/check_welfare_identity_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 498 | `scripts/ps1/append_s16_model_comparison.py` | `MNL/scripts/ps1/append_s16_model_comparison.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 499 | `scripts/ps1/ps1_s16_bands.py` | `MNL/scripts/ps1/ps1_s16_bands.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 500 | `scripts/ps1/run_ps1_s16a_diag.py` | `MNL/scripts/ps1/run_ps1_s16a_diag.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 501 | `scripts/ps1/run_ps1_s16a_price.py` | `MNL/scripts/ps1/run_ps1_s16a_price.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 502 | `scripts/ps1/run_ps1_s16a_qw_proposal.py` | `MNL/scripts/ps1/run_ps1_s16a_qw_proposal.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 503 | `scripts/ps1/run_ps1_s16b_gw_structural.py` | `MNL/scripts/ps1/run_ps1_s16b_gw_structural.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 506 | `market.html` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 507 | `beamer/build/verification_v4.json` | `Job_Market_paper/beamer/build/verification_v4.json` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 510 | `manuscript/tables/v5/v5_benchmark.csv` | `Job_Market_paper/manuscript/tables/v5/v5_benchmark.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 511 | `manuscript/tables/v5/v5_coefficients_preferences.csv` | `Job_Market_paper/manuscript/tables/v5/v5_coefficients_preferences.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 512 | `manuscript/tables/v5/v5_full_coefficients_singles.csv` | `Job_Market_paper/manuscript/tables/v5/v5_full_coefficients_singles.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 513 | `reports/JMP_research_story_report_v2.html` | `Job_Market_paper/reports/JMP_research_story_report_v2.html` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 514 | `Literature/JMP_core_bibliography.bib` | `Job_Market_paper/Literature/JMP_core_bibliography.bib` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 515 | `Literature/core_papers/aaberge_colombino_2018.md` | `Job_Market_paper/Literature/core_papers/aaberge_colombino_2018.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 516 | `Literature/core_papers/aaberge_colombino_strom_1999.md` | `Job_Market_paper/Literature/core_papers/aaberge_colombino_strom_1999.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 517 | `Literature/core_papers/aaberge_dagsvik_strom_1995.md` | `Job_Market_paper/Literature/core_papers/aaberge_dagsvik_strom_1995.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 518 | `Literature/core_papers/audoly_et_al_2025.md` | `Job_Market_paper/Literature/core_papers/audoly_et_al_2025.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 519 | `Literature/core_papers/bargain_et_al_2013.md` | `Job_Market_paper/Literature/core_papers/bargain_et_al_2013.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 520 | `Literature/core_papers/bargain_et_al_2014.md` | `Job_Market_paper/Literature/core_papers/bargain_et_al_2014.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 521 | `Literature/core_papers/capeau_decoster_dekkers_2015.md` | `Job_Market_paper/Literature/core_papers/capeau_decoster_dekkers_2015.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 522 | `Literature/core_papers/dagsvik_jia_2016.md` | `Job_Market_paper/Literature/core_papers/dagsvik_jia_2016.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 523 | `Literature/core_papers/dagsvik_strom_2006.md` | `Job_Market_paper/Literature/core_papers/dagsvik_strom_2006.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 524 | `Literature/core_papers/decoster_haan_2015.md` | `Job_Market_paper/Literature/core_papers/decoster_haan_2015.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 525 | `Literature/core_papers/fleurbaey_maniquet_2006.md` | `Job_Market_paper/Literature/core_papers/fleurbaey_maniquet_2006.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 526 | `Literature/core_papers/fleurbaey_maniquet_2018_jel.md` | `Job_Market_paper/Literature/core_papers/fleurbaey_maniquet_2018_jel.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 527 | `Literature/core_papers/haydar_maniquet_2026_wip.md` | `Job_Market_paper/Literature/core_papers/haydar_maniquet_2026_wip.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 528 | `Literature/core_papers/jacquet_jia_thoresen_2026.md` | `Job_Market_paper/Literature/core_papers/jacquet_jia_thoresen_2026.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 529 | `Literature/core_papers/jia_thoresen.md` | `Job_Market_paper/Literature/core_papers/jia_thoresen.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 530 | `Literature/core_papers/sastre_trannoy_2002.md` | `Job_Market_paper/Literature/core_papers/sastre_trannoy_2002.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 531 | `Literature/core_papers/shorrocks_1982.md` | `Job_Market_paper/Literature/core_papers/shorrocks_1982.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 532 | `Literature/core_papers/shorrocks_2013.md` | `Job_Market_paper/Literature/core_papers/shorrocks_2013.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 533 | `Literature/corpus_index.md` | `Job_Market_paper/Literature/corpus_index.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 534 | `Theory_other_project/jobs_and_wellbeing.agent.md` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.agent.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 535 | `Theory_other_project/jobs_and_wellbeing.tex` | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 536 | `docs/JMP_W1_theory_to_implementation_bridge_v1.md` | `Job_Market_paper/docs/JMP_W1_theory_to_implementation_bridge_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 537 | `docs/Missions/JMP_welfare_walkthrough_mission_v1.md` | `Job_Market_paper/docs/Missions/JMP_welfare_walkthrough_mission_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 538 | `docs/normative/JMP_W1_fork_ruling_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 539 | `docs/normative/W1_latent_set_identification_note_v1.md` | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 540 | `reports/JMP_reference_profiles_v1.csv` | `Job_Market_paper/reports/JMP_reference_profiles_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 541 | `reports/JMP_reference_profiles_v1.md` | `Job_Market_paper/reports/JMP_reference_profiles_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 542 | `reports/JMP_reference_profiles_v1.tex` | `Job_Market_paper/reports/JMP_reference_profiles_v1.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 543 | `reports/JMP_v5_review_and_modular_revision_plan_v1.md` | `Job_Market_paper/reports/JMP_v5_review_and_modular_revision_plan_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 544 | `reports/figure_modules/v5_labour_market_opportunity_composition/build_figure.py` | `Job_Market_paper/reports/figure_modules/v5_labour_market_opportunity_composition/build_figure.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 545 | `reports/figure_modules/v5_labour_market_opportunity_composition/evidence.md` | `Job_Market_paper/reports/figure_modules/v5_labour_market_opportunity_composition/evidence.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 546 | `reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.csv` | `Job_Market_paper/reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 547 | `reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.pdf` | `Job_Market_paper/reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 548 | `reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.png` | `Job_Market_paper/reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.png` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 549 | `reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.tex` | `Job_Market_paper/reports/figure_modules/v5_labour_market_opportunity_composition/v5_labour_market_opportunity_composition.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 550 | `reports/leisure_curvature_vs_normalizer.pdf` | `Job_Market_paper/reports/leisure_curvature_vs_normalizer.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 551 | `reports/leisure_intercept_vs_normalizer.pdf` | `Job_Market_paper/reports/leisure_intercept_vs_normalizer.pdf` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 554 | `docs/normative/fork_derived_numerals_v1.csv` | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | 554 | `docs/normative/scripts/fork_derived_numerals_v1.py` | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 5 | `JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 7 | `JMP_bridge_source_extract_v1.md` | `Job_Market_paper/docs/JMP_bridge_source_extract_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 35 | `JMP_BASELINE_F1_equivalised_reporting_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 38 | `JMP_counterfactual_attainment_design_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 38 | `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md` | `Job_Market_paper/docs/Missions/JMP_current_state_dashboard_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 45 | `welfare_core.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 45 | `baseline_f1.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 45 | `run_baseline_f1_full_sample.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 45 | `baseline_f1_provenance_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 45 | `baseline_f1_verification_v1.md` | `MNL/docs/corr/baseline_f1_verification_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 50 | `..._verification_v1.md` | — (not found) | no | PINNED |
| `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | 52 | `JMP_W1_stochastic_ability_set_bridge_v*.md` | — (glob pattern) | no | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 27 | `docs/JMP_W1_theory_to_implementation_bridge_v1.md` | `Job_Market_paper/docs/JMP_W1_theory_to_implementation_bridge_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 98 | `canonical_notation_v5.md` | `Job_Market_paper/reports/canonical_notation_v5.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 103 | `m08_welfare_measures.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 104 | `welfare_m08_decomposition_v1.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 109 | `engine_jax.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 112 | `estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | — (ambiguous: 4 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 136 | `s12_w4_premise_audit_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 165 | `s11_welfare_specs_of_record_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 440 | `04_welfare_and_decomposition.tex` | `Job_Market_paper/manuscript/sections/04_welfare_and_decomposition.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 440 | `run_s12_welfare_record_v1.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 795 | `Job_Market_paper/reports/canonical_notation_v5.md` | `Job_Market_paper/reports/canonical_notation_v5.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 796 | `Job_Market_paper/manuscript/sections/04_welfare_and_decomposition.tex` | `Job_Market_paper/manuscript/sections/04_welfare_and_decomposition.tex` | yes | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 797 | `Job_Market_paper/Literature/core_papers/haydar_maniquet_2026_wip.md` | `Job_Market_paper/Literature/core_papers/haydar_maniquet_2026_wip.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | 835 | `JMP_literature/03_summaries/T1A/Bloemen_2000_job_offer_restrictions.md` | `Job_Market_paper/JMP_literature/03_summaries/T1A/Bloemen_2000_job_offer_restrictions.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 1 | `baseline_f1_term_check_v1.md` | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 16 | `MNL/docs/corr/baseline_f1_provenance_v1.md` | `MNL/docs/corr/baseline_f1_provenance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 23 | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | yes | PINNED |
| `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 45 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 54 | `experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | 56 | `…/s11_couples_parameter_table_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 1 | `JMP_W1_reference_domain_fork_v1.md` | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 11 | `docs/normative/fork_derived_numerals_v1.csv` | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 23 | `.../figE1_matched_households/e1_matched_households_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 41 | `s11_singles_parameter_table_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 43 | `s11_couples_parameter_table_v1.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 45 | `pff_step1_reference_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | 48 | `fork_derived_numerals_v1.csv` | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v1.md` | 10 | `JMP_M05_task_plan_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v1.md` | 22 | `JMP_M05_task_plan_manager_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v1.md` | 75 | `docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v1.md` | 76 | `docs/France_case/P2a/phase5_parameter_map_v1.csv` | `MNL/docs/France_case/P2a/phase5_parameter_map_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v1.md` | 77 | `docs/France_case/P2a/phase5_source_inventory_v1.json` | `MNL/docs/France_case/P2a/phase5_source_inventory_v1.json` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 13 | `JMP_M05_task_plan_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 38 | `docs/governance/JMP_program_governance_v1.md` | `Job_Market_paper/docs/governance/JMP_program_governance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 39 | `docs/governance/JMP_management_hierarchy_and_delegation_v1.md` | `Job_Market_paper/docs/governance/JMP_management_hierarchy_and_delegation_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 40 | `docs/governance/JMP_canonical_state_v1.md` | `Job_Market_paper/docs/governance/JMP_canonical_state_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 41 | `docs/governance/JMP_decision_log_v1.md` | `Job_Market_paper/docs/governance/JMP_decision_log_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 42 | `docs/missions/JMP_M05_phase5_inference_mission_charter_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_phase5_inference_mission_charter_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 43 | `docs/missions/JMP_M05_task_plan_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 44 | `docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 45 | `docs/missions/JMP_M05_mission_ledger_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_mission_ledger_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 184 | `docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 185 | `docs/France_case/P2a/phase5_parameter_map_v1.csv` | `MNL/docs/France_case/P2a/phase5_parameter_map_v1.csv` | yes | PINNED |
| `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | 186 | `docs/France_case/P2a/phase5_source_inventory_v1.json` | `MNL/docs/France_case/P2a/phase5_source_inventory_v1.json` | yes | PINNED |
| `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 9 | `SECTION_MAP.md` | `Job_Market_paper/manuscript/SECTION_MAP.md` | yes | PINNED |
| `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 9 | `sections/README.md` | `Job_Market_paper/manuscript/sections/README.md` | yes | PINNED |
| `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 28 | `JMP_working_paper_for_seminar_v5.tex` | `Job_Market_paper/manuscript/JMP_working_paper_for_seminar_v5.tex` | yes | PINNED |
| `Job_Market_paper/manuscript/SECTION_SPLIT_VERIFICATION.md` | 40 | `.git/v5-section-split-verification/original.tex` | `Job_Market_paper/.git/v5-section-split-verification/original.tex` | yes | PINNED |
| `MNL/docs/France_case/NC_pilot/execution_logs/JMP_NC_pilot_scaled_JAX_estimator_acceptance_memo_v1.md` | 214 | `docs/France_case/NC_pilot/design/JMP_NC_pilot_beta_l0_m_specification_review_v1.md` | `MNL/docs/France_case/NC_pilot/design/JMP_NC_pilot_beta_l0_m_specification_review_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 4 | `docs/France_case/P2a/FR_P2a_m08_codex_production_path_review_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_m08_codex_production_path_review_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 12 | `FR_P2a_*.md` | — (glob pattern) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 12 | `gate_manifest.json` | — (ambiguous: 8 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 12 | `chunk_priced_*.json` | — (glob pattern) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 25 | `FR_P2a_m08_codex_production_path_review_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 29 | `scripts/welfare/m08_p2a_parity.py` | `MNL/scripts/welfare/m08_p2a_parity.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 32 | `scripts/welfare/run_m08_p2a_parity_gate.py` | `MNL/scripts/welfare/run_m08_p2a_parity_gate.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 35 | `chunk_priced_00000.json` | — (ambiguous: 6 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 76 | `FR_P2a_m08_parity_gate_report_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 88 | `priced_00000.parquet` | — (ambiguous: 4 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 88 | `docs/jmp_methodology/RURO_welfare_F6PRICEB0_geometry_audit_v1.md` | `MNL/docs/jmp_methodology/RURO_welfare_F6PRICEB0_geometry_audit_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 88 | `docs/France_case/P2a/FR_P2a_m08_parity_diagnosis_memo_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_m08_parity_diagnosis_memo_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 88 | `fr_singles_pricing_p2a/priced_*.parquet` | — (glob pattern) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 90 | `dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v2.ipynb` | `MNL/dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v2.ipynb` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 99 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260805T175932Z_733948_1ce508a6e0504acb94c901ef3751a011_parity_PARITY_PASS_SMOKE/chunk_priced_00000.json` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260805T175932Z_733948_1ce508a6e0504acb94c901ef3751a011_parity_PARITY_PASS_SMOKE/chunk_priced_00000.json` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md` | 99 | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260805T180301Z_638408_ca402c3a3d9a412ea0d76914c07697f7_parity_PARITY_PASS_FULL/chunk_priced_00000.json` | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260805T180301Z_638408_ca402c3a3d9a412ea0d76914c07697f7_parity_PARITY_PASS_FULL/chunk_priced_00000.json` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 7 | `Job_Market_paper/docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 30 | `FR_P2a_m08_parity_gate_report_v4.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 41 | `FR_P2a_m08_parity_gate_report_v4_change_log.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 52 | `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4.md` | `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 62 | `FR_P2a_m08_parity_gate_report_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 63 | `FR_P2a_m08_parity_gate_report_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 64 | `FR_P2a_m08_parity_gate_report_v3.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 65 | `FR_P2a_m08_parity_gate_report_v3_change_log.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 67 | `FR_P2a_m08_codex_production_path_review_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 68 | `FR_P2a_m08_codex_reverification_T4_T7_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 69 | `FR_P2a_m08_parity_diagnosis_memo_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 85 | `gate_manifest.json` | — (ambiguous: 8 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 85 | `chunk_priced_*.json` | — (glob pattern) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 85 | `reconstruction_log.txt` | — (ambiguous: 8 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 155 | `JMP_M08_E2_parity_report_v3_documentary_correction_ruling_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_E2_parity_report_v3_documentary_correction_ruling_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_acceptance.md` | 161 | `JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 5 | `FR_P2a_m08_u6c_qw_stack_review_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 34 | `scripts/welfare/run_m08_u6_resume_v2.py` | `MNL/scripts/welfare/run_m08_u6_resume_v2.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 45 | `scripts/welfare/run_m08_welfare_decomposition.py` | `MNL/scripts/welfare/run_m08_welfare_decomposition.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 47 | `scripts/welfare/m08_u6_pins_v2.py` | `MNL/scripts/welfare/m08_u6_pins_v2.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 51 | `scripts/welfare/m08_u6_basis.py` | `MNL/scripts/welfare/m08_u6_basis.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 57 | `.../20260823T213827Z_671796_47f3785e9c8946b48fd41cc09b9f48ed_u6resume4_U6_RESUME_V2_DONE/u6_resume_margqh_v2.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 77 | `u6resume4/u6_resume_margqh_v2.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 90 | `C:/Users/hisham/MNL/EUROMOD-STORAGE/new_data/fr_p2a_singles2016_welfare_u6_2x__mnlmeta.json` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/new_data/fr_p2a_singles2016_welfare_u6_2x__mnlmeta.json` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 101 | `u6resume3/u6_resume_margqh_v2.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 118 | `scripts/welfare/m08_n7_reproducibility_probe_v1.py` | `MNL/scripts/welfare/m08_n7_reproducibility_probe_v1.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08_u6c_reverification_v1.md` | 128 | `scripts/welfare/m08_ghat_samplers.py` | `MNL/scripts/welfare/m08_ghat_samplers.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 11 | `docs/France_case/P2a/FR_P2a_m08e_codex_review_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_review_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 21 | `m08e_pins.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 22 | `m08e_successor_v2_build.py` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 22 | `m08e_e3_reestimate_v2.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 23 | `m08e_e4_curvature_inference_v2.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 26 | `e3_manifest.json` | — (ambiguous: 10 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 27 | `e4_manifest.json` | — (ambiguous: 6 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 76 | `FR_P2a_m08e_E4_curvature_inference_note_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 99 | `FR_P2a_m08e_E3_reestimation_note_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 160 | `e4_inference_diagnostics.json` | — (ambiguous: 6 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_codex_reverification_v1.md` | 173 | `scripts/p2a/run_p2a_phase5_inference.py` | `MNL/scripts/p2a/run_p2a_phase5_inference.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 14 | `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | `Job_Market_paper/docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 46 | `scripts/m08e/m08e_pins.py` | `MNL/scripts/m08e/m08e_pins.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 86 | `outputs/p2a_singles2016/region_live_margqh_v1/e2_closure_r1_v1/attempts/20260823T152543Z_180012_69c59793f2284da6ae0daa2a42682fef_r1probes_R1_PROBES_PASS/r1_probe_evidence.json` | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/e2_closure_r1_v1/attempts/20260823T152543Z_180012_69c59793f2284da6ae0daa2a42682fef_r1probes_R1_PROBES_PASS/r1_probe_evidence.json` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 100 | `r1_probe_evidence.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 107 | `scripts/m08e/m08e_e3_reestimate_v2.py` | `MNL/scripts/m08e/m08e_e3_reestimate_v2.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 108 | `scripts/m08e/m08e_e4_curvature_inference_v2.py` | `MNL/scripts/m08e/m08e_e4_curvature_inference_v2.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 111 | `m08e_pins.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 128 | `m08e_e3_reestimate_v2.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 129 | `m08e_e4_curvature_inference_v2.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 172 | `r1_probes_manifest.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 179 | `docs/France_case/P2a/FR_P2a_m08e_E3_reestimation_note_v2.md` | `MNL/docs/France_case/P2a/FR_P2a_m08e_E3_reestimation_note_v2.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 188 | `FR_P2a_m08e_E3_reestimation_note_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 203 | `e4_manifest.json` | — (ambiguous: 6 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 210 | `e3_manifest.json` | — (ambiguous: 10 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_m08e_final_verification_R1_R5_v1.md` | 221 | `docs/France_case/P2a/FR_P2a_m08e_E4_curvature_inference_note_v2.md` | `MNL/docs/France_case/P2a/FR_P2a_m08e_E4_curvature_inference_note_v2.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 4 | `FR_P2a_region_live_dry_run_report_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 5 | `FR_P2a_region_live_manager_decisions_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 6 | `FR_P2a_region_live_production_rebuild_plan_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 30 | `pre_estimation_reload_verification.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 50 | `propagate_regionlive.py` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase12_manager_acceptance_v1.md` | 104 | `scripts/p2a/run_p2a_regionlive_rebuild.py` | `MNL/scripts/p2a/run_p2a_regionlive_rebuild.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 5 | `FR_P2a_region_live_phase3_estimation_report_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 21 | `theta_estimated.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 21 | `optimizer_diagnostics.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 22 | `estimation_results.json` | — (ambiguous: 170 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 22 | `phase3_manifest.json` | — (ambiguous: 142 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 32 | `FR_P2a_region_live_phase3_code_review_v6.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 135 | `fr_singles_pipeline_v1.ipynb` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase3_manager_acceptance_v1.md` | 135 | `fr_singles_pipeline_v2.ipynb` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_manager_acceptance_v1.md` | 5 | `FR_P2a_region_live_phase4_execution_report_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 4 | `JMP_M05C_deputy_phase5_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M05C_deputy_phase5_acceptance_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 5 | `JMP_M05C_goal_manager_dryrun_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M05C_goal_manager_dryrun_acceptance_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 53 | `scripts/p2a/run_p2a_phase5_inference.py` | `MNL/scripts/p2a/run_p2a_phase5_inference.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 63 | `phase5_manifest.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 97 | `phase5_diagnostics.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 205 | `phase5_regional_covariance.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_result_acceptance_v1.md` | 205 | `phase5_regional_tests.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 4 | `JMP_M05_task_plan_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 44 | `hessian_free.npy` | — (ambiguous: 4 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 45 | `hessian_free.csv` | — (ambiguous: 4 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 82 | `docs/Missions/JMP_M05_task_manager_operating_prompt_v1.md` | `Job_Market_paper/docs/Missions/JMP_M05_task_manager_operating_prompt_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 83 | `docs/prompts/JMP_M05_management_checkpoint_commit_prompt_v1.md` | `Job_Market_paper/docs/prompts/JMP_M05_management_checkpoint_commit_prompt_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 84 | `docs/prompts/JMP_M05_source_verification_prompt_v1.md` | `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 87 | `JMP_M05_stageA_correction_memo_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_stageA_correction_memo_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 113 | `docs/governance/JMP_program_governance_v1.md` | `Job_Market_paper/docs/governance/JMP_program_governance_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 114 | `docs/governance/JMP_management_hierarchy_and_delegation_v1.md` | `Job_Market_paper/docs/governance/JMP_management_hierarchy_and_delegation_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 115 | `docs/governance/JMP_canonical_state_v1.md` | `Job_Market_paper/docs/governance/JMP_canonical_state_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 116 | `docs/governance/JMP_decision_log_v1.md` | `Job_Market_paper/docs/governance/JMP_decision_log_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 117 | `docs/governance/JMP_roadmap_v1.md` | `Job_Market_paper/docs/governance/JMP_roadmap_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 118 | `docs/governance/JMP_mission_template_v1.md` | `Job_Market_paper/docs/governance/JMP_mission_template_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 119 | `docs/governance/JMP_Goal1_manager_operating_contract_v1.md` | `Job_Market_paper/docs/governance/JMP_Goal1_manager_operating_contract_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 120 | `docs/governance/JMP_governance_creation_report_v1.md` | `Job_Market_paper/docs/governance/JMP_governance_creation_report_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 121 | `docs/missions/JMP_M05_phase5_inference_mission_charter_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_phase5_inference_mission_charter_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 122 | `docs/missions/JMP_M05_task_plan_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 123 | `docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 124 | `docs/missions/JMP_M05_mission_ledger_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_mission_ledger_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 125 | `docs/missions/JMP_M05_design_stage_delegation_packet_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_design_stage_delegation_packet_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 126 | `docs/missions/JMP_M05_stageA_correction_memo_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_stageA_correction_memo_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 127 | `docs/missions/JMP_M05_task_manager_operating_prompt_v2.md` | `Job_Market_paper/docs/missions/JMP_M05_task_manager_operating_prompt_v2.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 128 | `docs/prompts/JMP_M05_source_verification_prompt_v2.md` | `Job_Market_paper/docs/prompts/JMP_M05_source_verification_prompt_v2.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 129 | `docs/prompts/JMP_M05_task_plan_prompt_v1.md` | `Job_Market_paper/docs/prompts/JMP_M05_task_plan_prompt_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 130 | `docs/prompts/JMP_M05_inference_design_prompt_v1.md` | `Job_Market_paper/docs/prompts/JMP_M05_inference_design_prompt_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 131 | `docs/prompts/JMP_M05_methods_review_prompt_v1.md` | `Job_Market_paper/docs/prompts/JMP_M05_methods_review_prompt_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 134 | `JMP_M05_task_manager_operating_prompt_v1.md` | `Job_Market_paper/docs/missions/JMP_M05_task_manager_operating_prompt_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 155 | `docs/France_case/P2a/FR_P2a_region_live_phase4_execution_report_v2.md` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_execution_report_v2.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 156 | `docs/France_case/P2a/FR_P2a_region_live_phase4_manager_acceptance_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_manager_acceptance_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 157 | `outputs/…/phase4_curvature_v1/complete/hessian_eigenvalues.csv` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 158 | `outputs/…/phase4_curvature_v1/complete/hessian_free.csv` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 159 | `outputs/…/phase4_curvature_v1/complete/hessian_free.npy` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 161 | `outputs/…/phase4_curvature_v1/complete/phase4_diagnostics.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 162 | `outputs/…/phase4_curvature_v1/complete/phase4_manifest.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 163 | `outputs/…/phase4_curvature_v1/complete/regional_hessian_subblock.csv` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 164 | `outputs/…/phase4_curvature_v1/complete/regional_schur_complement.csv` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 184 | `scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | `MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 233 | `phase4_diagnostics.json` | — (ambiguous: 4 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 235 | `theta_estimated.csv` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 265 | `docs/France_case/P2a/phase5_parameter_map_v1.csv` | `MNL/docs/France_case/P2a/phase5_parameter_map_v1.csv` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 352 | `scripts/p2a/configs/p2a_regionlive_rebuild_v1.yaml` | `MNL/scripts/p2a/configs/p2a_regionlive_rebuild_v1.yaml` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 354 | `theta_p2a_singles_2016_v1.csv` | `MNL/theta_p2a_singles_2016_v1.csv` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 360 | `engine_jax.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 463 | `dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 617 | `dclaborsupply/se/cluster_robust.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 619 | `MNL/scripts/enhanced/cluster_robust_se.py` | `MNL/scripts/enhanced/cluster_robust_se.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 704 | `phase4_manifest.json` | — (ambiguous: 112 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 724 | `EUROMOD-STORAGE/Data/external/FR_gsur_ruro_v2_stageA_y2015.parquet` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/external/FR_gsur_ruro_v2_stageA_y2015.parquet` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 782 | `hessian_eigenvalues.csv` | — (ambiguous: 4 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 788 | `regional_hessian_subblock.csv` | — (ambiguous: 10 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 789 | `regional_schur_complement.csv` | — (ambiguous: 10 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 797 | `FR_P2a_region_live_phase4_execution_report_v2.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 832 | `.npy` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 905 | `se/numerical.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 906 | `solvers/jax_optimize.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 954 | `phase3_manifest.json` | — (ambiguous: 142 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 966 | `scripts/bpool/specs/theta_hat_realdata_901_v1.csv` | `MNL/scripts/bpool/specs/theta_hat_realdata_901_v1.csv` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 968 | `outputs/…/fr_p2a_singles2016_regionlive__singles.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 969 | `outputs/…/fr_p2a_singles2016_regionlive__mnlmeta.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 970 | `outputs/…/inputs/fr_p2a_draws_geometry__singles.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 971 | `outputs/…/inputs/fr_p2a_draws_geometry__meta.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 972 | `outputs/…/rebuild_manifest.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 973 | `outputs/…/dry_run_report.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 974 | `outputs/…/pre_estimation_reload_verification.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 975 | `scripts/p2a/run_p2a_regionlive_rebuild.py` | `MNL/scripts/p2a/run_p2a_regionlive_rebuild.py` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 977 | `docs/France_case/P2a/FR_P2a_region_live_phase4_code_review_v7.md` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase4_code_review_v7.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 981 | `spec/parser.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 981 | `likelihood/_numpy_primitives.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 1068 | `docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 1080 | `docs/France_case/P2a/phase5_source_inventory_v1.json` | `MNL/docs/France_case/P2a/phase5_source_inventory_v1.json` | yes | PINNED |
| `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_source_verification_v1.md` | 1096 | `docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v1.md` | `MNL/docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v1.md` | yes | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 15 | `Z:/hisham/EUROMOD-STORAGE/Data/processed/fr/2016/fr_2016_RURO_mnl_GSURv2__singles.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 16 | `Z:/hisham/EUROMOD-STORAGE/Data/processed/fr/2016/fr_2016_RURO_mnl_GSURv2__couples.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 17 | `Z:/hisham/EUROMOD-STORAGE/Data/processed/fr/2016/fr_2016_RURO_mnl_GSURv2__mnlmeta.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 21 | `fr_2016_RURO_mnl_GSURv2__mnlmeta.json` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/2016/fr_2016_RURO_mnl_GSURv2__mnlmeta.json` | yes | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 23 | `fr_2016_RURO_mnl__mnlmeta.json` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/2016/fr_2016_RURO_mnl__mnlmeta.json` | yes | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 33 | `Data/processed/fr/pooled/fr_p3a_gsurv2_harmonised__stage_m1_meta.json` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/pooled/fr_p3a_gsurv2_harmonised__stage_m1_meta.json` | yes | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 36 | `fr_2016_RURO_mnl_GSURv2_y2015__singles/couples.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 43 | `Data/processed/fr/pooled/fr_p3a_provisional_v1fallback_harmonised__stage_m1_meta.json` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/pooled/fr_p3a_provisional_v1fallback_harmonised__stage_m1_meta.json` | yes | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 48 | `fr_p3a_gsurv2_harmonised.parquet` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/pooled/fr_p3a_gsurv2_harmonised.parquet` | yes | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 50 | `fr_2016_RURO_mnl_GSURv2__{singles,couples}.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 57 | `scripts/pilot/specs/estimation_spec_nc_pilot_couples_2016.yaml` | `MNL/scripts/pilot/specs/estimation_spec_nc_pilot_couples_2016.yaml` | yes | PINNED |
| `MNL/docs/France_case/P3a/consolidated/RURO_pilot_gsurv2_verification_v1.md` | 116 | `Data/pilot/nc_2016_couples/fr_pilot_nc_2016_couples_product__mnlmeta.json` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/pilot/nc_2016_couples/fr_pilot_nc_2016_couples_product__mnlmeta.json` | yes | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 10 | `hours_mixture_d1.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 10 | `occ_draw_empirical.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 11 | `build_bpool_singles.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 11 | `build_bpool_couples.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 11 | `run_bpool_draws.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 81 | `fr_p3a_gsurv2_estimation_ready__singles.parquet` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/pooled/fr_p3a_gsurv2_estimation_ready__singles.parquet` | yes | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 82 | `fr_p3a_gsurv2_estimation_ready__couples.parquet` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/pooled/fr_p3a_gsurv2_estimation_ready__couples.parquet` | yes | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 115 | `fr_p3a_gsurv2_harmonised__stage_m1_meta.json` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/pooled/fr_p3a_gsurv2_harmonised__stage_m1_meta.json` | yes | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 127 | `fr_p3a_gsurv2_estimation_ready__*.parquet` | — (glob pattern) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 137 | `stage_m1_meta.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 148 | `RURO_pilot_gsurv2_verification_v1.md` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 160 | `scripts/bpool/hours_mixture_d1.py` | `MNL/scripts/bpool/hours_mixture_d1.py` | yes | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 198 | `pilot_mincer_coefficients_v1.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 251 | `fr_p3a_bpool_d1w1__singles.parquet` | — (ambiguous: 3 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 252 | `fr_p3a_bpool_d1w1__couples.parquet` | — (ambiguous: 3 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 257 | `build_bpool_precompute.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 261 | `RURO_recovery_test_design_v1.md` | — (not found) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 331 | `enh_RURO_prep_mnl_basic.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 332 | `gamspy_estimation_vectorized.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 333 | `estimation_spec_nc_pilot_couples_2016.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 543 | `scripts/bpool/specs/estimation_spec_bpool_p3a_v1.yaml` | `MNL/scripts/bpool/specs/estimation_spec_bpool_p3a_v1.yaml` | yes | PINNED |
| `MNL/docs/France_case/P3a/execution_logs/Bpool/RURO_Bpool_draws_verification_v1.md` | 563 | `estimation_spec_ruro_occ_P3a_pooled.yaml` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 9 | `enh_job_universe.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 40 | `enh_job_draws.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 54 | `run_job_ruro_pipeline.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 68 | `scripts/Job_model/enh_job_universe.py` | `MNL/scripts/Job_model/enh_job_universe.py` | yes | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 69 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/singles_RURO_ready.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 70 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/couples_RURO_ready.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 80 | `scripts/Job_model/enh_job_draws.py` | `MNL/scripts/Job_model/enh_job_draws.py` | yes | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 83 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/job_model_test/job_universe_2016.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 84 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/job_model_test/job_universe_2016__meta.json` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 89 | `enh_RURO_euromod.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 90 | `scripts/enhanced/enh_RURO_euromod.py` | `MNL/scripts/enhanced/enh_RURO_euromod.py` | yes | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 91 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/singles_RURO_ready_jobdraws.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 92 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/couples_RURO_ready_jobdraws.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 93 | `U:/EUROMOD-STORAGE/Data/raw/FR_2016_c2.txt` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 136 | `job_universe_YYYY__gmm_diagnostics.csv` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 145 | `scripts/Job_model/run_job_ruro_pipeline.py` | `MNL/scripts/Job_model/run_job_ruro_pipeline.py` | yes | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 169 | `test_singles_small.parquet` | — (not found) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 198 | `singles_RURO_ready_jobdraws.parquet` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/2016/singles_RURO_ready_jobdraws.parquet` | yes | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 235 | `job_universe_2016.parquet` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 248 | `job_universe_2016__meta.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 328 | `combined_draws_em.parquet` | — (ambiguous: 37 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 348 | `*_jobdraws.parquet` | — (glob pattern) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 356 | `*_jobdraws__drawsmeta.json` | — (glob pattern) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 399 | `enh_RURO_draws.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 401 | `*_RURO_ready.parquet` | — (glob pattern) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 412 | `README_job_model.md` | — (ambiguous: 4 candidates) | no | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 413 | `scripts/Job_model/sanity_checks_job.py` | `MNL/scripts/Job_model/sanity_checks_job.py` | yes | PINNED |
| `MNL/docs/France_case/job_model/ACCEPTANCE_TESTS.md` | 414 | `.claude/plans/melodic-doodling-orbit.md` | — (not found) | no | PINNED |
| `MNL/docs/archive/2026-05-25_docs_supersession/merged_sources/gsur_external_acquisition/RURO_GSUR_external_acquisition_verification_claude_v1.md` | 1 | `docs/France_case/consolidated/RURO_GSUR_external_acquisition_consolidated_v1.md` | — (not found) | no | PINNED |
| `MNL/docs/archive/2026-05-25_docs_supersession/merged_sources/gsur_external_acquisition/RURO_GSUR_external_acquisition_verification_claude_v1.md` | 1 | `docs/France_case/cleanup/MOVE_MANIFEST_2026-05-25.md` | `MNL/docs/France_case/cleanup/MOVE_MANIFEST_2026-05-25.md` | yes | PINNED |
| `MNL/docs/archive/2026-05-25_docs_supersession/merged_sources/gsur_external_acquisition/RURO_GSUR_external_acquisition_verification_claude_v1.md` | 15 | `NUTS2013-NUTS2016.xlsx` | — (ambiguous: 3 candidates) | no | PINNED |
| `MNL/docs/archive/2026-05-25_docs_supersession/merged_sources/gsur_external_acquisition/RURO_GSUR_external_acquisition_verification_claude_v1.md` | 28 | `Y10_CR_FR_Final.pdf` | — (not found) | no | PINNED |
| `MNL/docs/corr/baseline_f1_verification_v1.md` | 14 | `MNL/scripts/welfare/baseline_f1.py` | `MNL/scripts/welfare/baseline_f1.py` | yes | PINNED |
| `MNL/docs/corr/baseline_f1_verification_v1.md` | 47 | `baseline_f1.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/corr/baseline_f1_verification_v1.md` | 67 | `engine_jax.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/docs/corr/baseline_f1_verification_v1.md` | 84 | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/baseline_f1_prep_v1/baseline_f1_households_v1.jsonl` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/restricted/baseline_f1_prep_v1/baseline_f1_households_v1.jsonl` | yes | PINNED |
| `MNL/gate/measure_map_accepted.json` | 5 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | yes | PINNED |
| `MNL/gate/measure_map_accepted.json` | 9 | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | yes | PINNED |
| `MNL/gate/measure_map_accepted.json` | 14 | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | yes | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 9 | `enh_job_universe.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 40 | `enh_job_draws.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 54 | `run_job_ruro_pipeline.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 68 | `scripts/Job_model/enh_job_universe.py` | `MNL/scripts/Job_model/enh_job_universe.py` | yes | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 69 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/singles_RURO_ready.parquet` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 70 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/couples_RURO_ready.parquet` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 80 | `scripts/Job_model/enh_job_draws.py` | `MNL/scripts/Job_model/enh_job_draws.py` | yes | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 83 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/job_model_test/job_universe_2016.parquet` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 84 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/job_model_test/job_universe_2016__meta.json` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 89 | `enh_RURO_euromod.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 90 | `scripts/enhanced/enh_RURO_euromod.py` | `MNL/scripts/enhanced/enh_RURO_euromod.py` | yes | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 91 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/singles_RURO_ready_jobdraws.parquet` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 92 | `U:/EUROMOD-STORAGE/Data/processed/fr/2016/couples_RURO_ready_jobdraws.parquet` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 93 | `U:/EUROMOD-STORAGE/Data/raw/FR_2016_c2.txt` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 136 | `job_universe_YYYY__gmm_diagnostics.csv` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 145 | `scripts/Job_model/run_job_ruro_pipeline.py` | `MNL/scripts/Job_model/run_job_ruro_pipeline.py` | yes | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 169 | `test_singles_small.parquet` | — (not found) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 198 | `singles_RURO_ready_jobdraws.parquet` | `C:/Users/hisham/MNL/EUROMOD-STORAGE/Data/processed/fr/2016/singles_RURO_ready_jobdraws.parquet` | yes | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 235 | `job_universe_2016.parquet` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 248 | `job_universe_2016__meta.json` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 328 | `combined_draws_em.parquet` | — (ambiguous: 37 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 348 | `*_jobdraws.parquet` | — (glob pattern) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 356 | `*_jobdraws__drawsmeta.json` | — (glob pattern) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 399 | `enh_RURO_draws.py` | — (ambiguous: 2 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 401 | `*_RURO_ready.parquet` | — (glob pattern) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 412 | `README_job_model.md` | — (ambiguous: 4 candidates) | no | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 413 | `scripts/Job_model/sanity_checks_job.py` | `MNL/scripts/Job_model/sanity_checks_job.py` | yes | PINNED |
| `MNL/scripts/Job_model/ACCEPTANCE_TESTS.md` | 414 | `.claude/plans/melodic-doodling-orbit.md` | — (not found) | no | PINNED |

## 3. Document families

Scope: every `.md` under `Job_Market_paper/docs/` in the working tree (tracked and untracked), plus family members on other branches or in MNL / MNL_posfit, marked by location. Status comes from the document's own header or version note, or from an explicit superseding statement in another document; otherwise UNKNOWN. `+ PINNED` = cited by path or hash in section 2 (either as a resolved path or as the cited path). `[T]` tracked on the checked-out branch, `[U]` untracked, `[B:docs/seminar-r6]` exists only on that branch.

### Fork (W1 reference-domain fork, FORK-1)

| Order | Document | Location | Status |
|---:|---|---|---|
| 1 | `Job_Market_paper/docs/normative/JMP_W1_reference_domain_fork_v1.md` | [T] | CURRENT (REC-1 r3 citation-closed; the fork ruling cites earlier bytes `260eb0d6` = version at `f6346232`) + PINNED |
| 2 | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | [T] | CURRENT (REC-1 script; not .md, listed with its family) + PINNED |
| 3 | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | [T] | CURRENT (record; Deputy Appendix A controls) + PINNED |
| 4 | `Job_Market_paper/docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | [T] | CURRENT (binding execution-gate ruling) + PINNED |

### Measure map (MEASURE-MAP-1R / GATE-1)

| Order | Document | Location | Status |
|---:|---|---|---|
| 1 | `Job_Market_paper/docs/normative/JMP_measure_map_v1.md` | [T] | CURRENT (audit return; accepted) + PINNED |
| 2 | `Job_Market_paper/docs/normative/JMP_measure_map_acceptance_v1.md` | [T] | CURRENT (acceptance record) + PINNED |
| 3 | `Job_Market_paper/docs/normative/baseline_f1_term_check_v1.md` | [T] | CURRENT (GATE-1 step 2, PASS) + PINNED |
| 4 | `MNL/gate/measure_map_accepted.json` | [T] | CURRENT (machine gate; not .md, listed for completeness) + PINNED |

### Bridge (theory to implementation; market-set BRIDGE-1)

| Order | Document | Location | Status |
|---:|---|---|---|
| 1 | `Job_Market_paper/docs/JMP_W1_theory_to_implementation_bridge_v1.md` | [U] | SUPERSEDED-BY-docs/normative/W1_latent_set_identification_note_v1.md (partial: "superseded on two points", note lines 27-32) + PINNED |
| 2 | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | [T] | CURRENT + PINNED |
| 3 | `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | [U] | UNKNOWN (named controlling by the bridge memos; no superseding document found, but later Deputy documents exist) + PINNED |
| 4 | `Job_Market_paper/docs/JMP_BRIDGE1_amendment_v1.md` | [U] | UNKNOWN (declared controlling by bridge v1/v3; no superseding document found) + PINNED |
| 5 | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | [T] | SUPERSEDED-BY-docs/JMP_W1_stochastic_ability_set_bridge_v3.md (v3 version note) + PINNED |
| 6 | `Job_Market_paper/docs/JMP_W1_stochastic_ability_set_bridge_v1.md` | [U] | SUPERSEDED-BY-docs/JMP_W1_stochastic_ability_set_bridge_v3.md; byte-identical duplicate of the normative copy |
| 7 | `Job_Market_paper/docs/JMP_W1_stochastic_ability_set_bridge_v2.md` | absent | **MISSING** — v3 says "v2 (partial pass, SRC-3 items 9-11 only) [is] preserved unedited", but no v2 exists in any branch, tag, working tree or the CLEAN-A quarantine |
| 8 | `Job_Market_paper/docs/JMP_W1_stochastic_ability_set_bridge_v3.md` | [U] | CURRENT per its own version note (complete BRIDGE-1-AMEND-2 pass). **Committed nowhere**; protected only by the CLEAN-A quarantine copy (SHA-256 `458786d29fad...`) |
| 9 | `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | [T] | CURRENT (review of v1; header supersedes its own first same-day issue) + PINNED |
| 10 | `Job_Market_paper/docs/normative/JMP_direct_g_welfare_ruling_v1.md` | [T] | CURRENT (accepts bridge verdict D) + PINNED |

### POSFIT (positive-fit diagnostics)

| Order | Document | Location | Status |
|---:|---|---|---|
| 1 | `MNL/JMP_positive_fit_diagnostics_memo_v1.md` | [U] | SUPERSEDED-BY-MNL_posfit/JMP_positive_fit_diagnostics_memo_v2.md (v2 = bounded POSFIT-1R revision); untracked in the MNL main checkout |
| 2 | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2.md` | [T] | SUPERSEDED-BY-MNL_posfit/JMP_positive_fit_diagnostics_memo_v2_S12.md (preserved historical base per the S12 alias) + PINNED |
| 3 | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | [T] | UNKNOWN (preserved addendum folded into the S12 alias; neither current nor explicitly superseded) + PINNED |
| 4 | `MNL_posfit/JMP_positive_fit_diagnostics_memo_v2_S12.md` | [T] | CURRENT (binding-name alias; fit verdicts OPEN pending Deputy review) + PINNED |

### BASELINE-F-1

| Order | Document | Location | Status |
|---:|---|---|---|
| 1 | `MNL/docs/corr/baseline_f1_provenance_v1.md` | [T] | SUPERSEDED-BY-MNL/docs/corr/baseline_f1_prep2_report_v1.md (own header: PREP-1 halt resolved by PREP-2); acceptance record cites its bytes at `838127e0` + PINNED |
| 2 | `MNL/docs/corr/baseline_f1_prep2_report_v1.md` | [T] | CURRENT (implementation report) + PINNED |
| 3 | `MNL/docs/corr/baseline_f1_verification_v1.md` | [T] | CURRENT (VERIFIED) + PINNED |

### E3-EQ (equivalised BASELINE-F-1 reporting)

| Order | Document | Location | Status |
|---:|---|---|---|
| 1 | `Job_Market_paper/docs/results/JMP_BASELINE_F1_equivalised_reporting_v1.md` | [B:docs/seminar-r6] | CURRENT (only on `docs/seminar-r6`) |
| 2 | `Job_Market_paper/docs/results/JMP_BASELINE_F1_equivalised_reporting_verification_v1.md` | [B:docs/seminar-r6] | CURRENT (only on `docs/seminar-r6`) |

### SRC (mechanical source extracts and audits)

| Order | Document | Location | Status |
|---:|---|---|---|
| 1 | `Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | [T] | CURRENT as a dated 2026-09-12 snapshot (SRC-1); its HEAD table is now stale + PINNED |
| 2 | `Job_Market_paper/docs/JMP_step0_status_v1.md` | [U] | as above; byte-identical duplicate of the normative copy |
| 3 | `Job_Market_paper/docs/JMP_bridge_source_extract_v1.md` | [U] | SUPERSEDED-BY-docs/normative/JMP_bridge_source_extract_v2.md (v2 header) + PINNED |
| 4 | `Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | [T] | CURRENT (SRC-2) + PINNED |
| 5 | `Job_Market_paper/docs/JMP_bridge_source_extract_v2.md` | [U] | CURRENT; byte-identical duplicate of the normative copy |
| 6 | `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` | [T] | CURRENT (SRC-3) + PINNED |
| 7 | `Job_Market_paper/docs/JMP_frame_draw_law_audit_v1.md` | [U] | UNKNOWN (SRC-4 v1; no acceptance or superseding record found); byte-identical to untracked `MNL/docs/corr/JMP_frame_draw_law_audit_v1.md` |

### Deck / seminar

| Order | Document | Location | Status |
|---:|---|---|---|
| 1 | `Job_Market_paper/docs/seminar/deck_status_r6.md` | [B:docs/seminar-r6] | CURRENT (only on `docs/seminar-r6`; states "Not merged") |
| 2 | `Job_Market_paper/docs/JMP_seminar_architecture_freeze_2026-09-17_v1.md` | [U] | CURRENT through 2026-09-17 by its own terms (Deputy freeze) |

### Other `.md` under Job_Market_paper/docs/ (outside the eight families) — 157 files

Not assigned to a family by this card; status not assessed, therefore **UNKNOWN** (plus PINNED where section 2 cites them).

| Document | Location | Status |
|---|---|---|
| `docs/JMP_core_packet_v2.md` | [T] | UNKNOWN |
| `docs/JMP_core_packet_v3.md` | [T] | UNKNOWN + PINNED |
| `docs/JMP_cross_repo_artifact_manifest_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/JMP_cross_repo_documentation_repair_report_v1.md` | [T] | UNKNOWN |
| `docs/JMP_cross_repo_documentation_staleness_audit_v1.md` | [T] | UNKNOWN |
| `docs/JMP_cross_repo_manager_handoff_v1.md` | [T] | UNKNOWN |
| `docs/JMP_literature_positioning_memo_v2.md` | [T] | UNKNOWN + PINNED |
| `docs/JMP_literature_positioning_memo_v3.md` | [T] | UNKNOWN + PINNED |
| `docs/JMP_open_decisions_cross_repo_v1.md` | [T] | UNKNOWN |
| `docs/JMP_project_state_identity_addendum_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/JMP_project_state_identity_addendum_v2.md` | [T] | UNKNOWN + PINNED |
| `docs/JMP_project_state_latest.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/HK01/JMP_HK_01_delta_summary_v1.md` | [T] | UNKNOWN |
| `docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/HK01/JMP_HK_01_inventory_summary_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/HK01/JMP_HK_01_phase1_codex_rereview_v1.md` | [T] | UNKNOWN |
| `docs/Missions/HK01/JMP_HK_01_phase1_codex_rereview_v2.md` | [T] | UNKNOWN |
| `docs/Missions/HK01/JMP_HK_01_phase1_codex_review_v1.md` | [T] | UNKNOWN |
| `docs/Missions/HK01/JMP_HK_01_v2_correction_note_v1.md` | [T] | UNKNOWN |
| `docs/Missions/HK01/JMP_HK_01_v3_correction_note_v1.md` | [T] | UNKNOWN |
| `docs/Missions/HK01/JMP_HK_01_v5_movable_rows_codex_review_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M07I_manuscript_claim_rider_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M07I_positioning_memo_acceptance_rider_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_E2_parity_report_v3_documentary_correction_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_LOC4_design_rereview_v3_reject_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_LOC4_design_rereview_v4_accept_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_LOC4_design_review_v2_reject_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_v2.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_LOC4_preferred_spec_packet_index_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_LOC4_robustness_design_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_LOC4_robustness_design_v2.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_LOC4_robustness_design_v3.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_LOC4_robustness_design_v4.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_RUM_benchmark_estimand_design_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_U6_CV1_control_variate_design_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_U6_functional_MC_precision_ruling_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_U6_welfare_proposal_remediation_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_ability_preference_operators_design_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_access_equalisation_operand_design_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_goal1_rulings_document_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_goal1_rulings_document_v2.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_goal1_rulings_document_v3.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_measure_definition_binding_memo_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_opportunity_normalisation_and_notebook_restart_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_proposal_density_convention_and_corrected_baseline_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v2.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v3.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v4.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v5.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_stageA_contract_review_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_M08_stageA_freeze_record_v1.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_M08_welfare_input_handoff_v2.md` | [T] | UNKNOWN |
| `docs/Missions/JMP_current_state_dashboard_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/Missions/JMP_welfare_walkthrough_mission_v1.md` | [U] | UNKNOWN + PINNED |
| `docs/design_notes/JMP_M05C_W4_routing_memo_v1.md` | [T] | UNKNOWN |
| `docs/governance/JMP_Goal1_manager_operating_contract_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/governance/JMP_canonical_state_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/governance/JMP_certification_proportionality_rule_v1.md` | [T] | UNKNOWN |
| `docs/governance/JMP_decision_log_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/governance/JMP_governance_creation_report_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/governance/JMP_management_hierarchy_and_delegation_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/governance/JMP_mission_template_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/governance/JMP_program_governance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/governance/JMP_roadmap_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/handoffs/CONTRACT_INDEX.md` | [T] | UNKNOWN |
| `docs/missions/JMP_LOC4_pathB_ruling_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05B_E2_deputy_decision_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05B_E2_deputy_decision_v2.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05B_E2_escalation_code_review_reject_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05B_E2_escalation_final_review_reject_v2.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05B_mission_ledger_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05B_pause_and_M05C_redesign_decision_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05B_phase5_implementation_mission_charter_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_E2_incrementA_review_reject_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_E2_incrementB_second_reject_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_deputy_phase5_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05C_goal_manager_dryrun_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05C_incrementA_E2_deputy_decision_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_incrementB_proportionality_decision_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_minimal_streaming_implementation_mission_charter_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_mission_ledger_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_mission_ledger_v2.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_mission_ledger_v3.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_mission_ledger_v4.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05C_mission_ledger_v5.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05_PI_disclosure_determination_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05_deputy_programme_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_design_stage_delegation_packet_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_mission_ledger_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_mission_ledger_v2.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M05_mission_ledger_v3.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_phase5_inference_mission_charter_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_source_verification_completeness_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_stageA_correction_memo_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_task_manager_operating_prompt_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_task_manager_operating_prompt_v2.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M05_task_plan_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M07I_manuscript_identity_alignment_charter_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M07I_stageB_independent_consistency_review_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M07_inference_results_integration_mission_charter_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M07_stageB_author_cover_note_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M07_stageC_independent_economics_review_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_M08_singles_welfare_decomposition_mission_charter_v1.md` | [T] | UNKNOWN |
| `docs/missions/JMP_M08_welfare_input_handoff_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/missions/JMP_goal1_phase5_strategic_assessment_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_E2_goal_manager_resume_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_E2_goal_manager_resume_prompt_v2.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_architectural_closure_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_archive_and_test42_salvage_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_bounded_remediation_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_closed_form_code_review_v4_prompt_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/prompts/JMP_M05B_code_review_v2_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_goal_manager_delegation_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_restricted_store_provisioning_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05B_test42_housekeeping_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05C_closeout_and_evidence_commit_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05C_goal_manager_closeout_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05C_goal_manager_delegation_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05C_goal_manager_resume_after_incrementA_reject_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05C_goal_manager_resume_incrementB_proportionality_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05C_incrementA_bounded_refix_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05C_incrementA_review_v2_prompt_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/prompts/JMP_M05C_incrementB_focused_closure_review_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05C_incrementB_three_fix_closure_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05D_goal_manager_delegation_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05_inference_design_prompt_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/prompts/JMP_M05_management_checkpoint_commit_prompt_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/prompts/JMP_M05_methods_review_prompt_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/prompts/JMP_M05_source_verification_prompt_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/prompts/JMP_M05_source_verification_prompt_v2.md` | [T] | UNKNOWN + PINNED |
| `docs/prompts/JMP_M05_stageB_author_addendum_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05_stageC_reviewer_addendum_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05_stageD_cycle1_instruction_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M05_task_plan_prompt_v1.md` | [T] | UNKNOWN + PINNED |
| `docs/prompts/JMP_M05_v4_closure_and_documentation_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M07_goal_manager_delegation_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_M08_goal_manager_delegation_prompt_v1.md` | [T] | UNKNOWN |
| `docs/prompts/JMP_cross_repo_state_audit_prompt_v1.md` | [T] | UNKNOWN |
| `docs/results/FR_P2a_phase5_inference_results_memo_v1.md` | [T] | UNKNOWN + PINNED |

## 4. Misplaced files (listed, not moved)

| File | Belongs in | Basis | Caution |
|---|---|---|---|
| `Job_Market_paper/docs/JMP_W1_stochastic_ability_set_bridge_v3.md` | `docs/normative/` | Own header: Intended path `Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v3.md` | Untracked live deliverable; commit before any move |
| `Job_Market_paper/docs/JMP_bridge_source_extract_v1.md` | `docs/normative/` | By card: SRC-1 output, companion of `JMP_step0_status_v1.md`, whose copy sits in normative; its successor v2 is in normative | Superseded |
| `Job_Market_paper/docs/JMP_frame_draw_law_audit_v1.md` | `docs/normative/` | By card family: SRC-4, sibling of SRC-3 (`docs/normative/JMP_bridge_review_factual_items_v1.md`) | Second copy at `MNL/docs/corr/`; neither committed |
| `Job_Market_paper/docs/JMP_BRIDGE1_amendment_v1.md` | `docs/normative/` (ambiguous) | Deputy amendment declared controlling; the controlling rulings of this family live in normative | No intended path in header |
| `Job_Market_paper/docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | `docs/normative/` or `docs/Missions/` (ambiguous) | Header: "Save as: a versioned JMP design/mission note"; function: controlling ruling | Cited by filename in bridge v1/v3, review and the E3-EQ memo |
| `Job_Market_paper/docs/JMP_seminar_architecture_freeze_2026-09-17_v1.md` | `docs/normative/` (ambiguous) | Deputy decision document | No intended path in header |
| `Job_Market_paper/docs/JMP_W1_stochastic_ability_set_bridge_v1.md` | none (redundant copy) | Byte-identical to committed `docs/normative/` copy (`ce0ee3f`) | See section 5 before removal |
| `Job_Market_paper/docs/JMP_bridge_source_extract_v2.md` | none (redundant copy) | Byte-identical to committed `docs/normative/` copy | See section 5 |
| `Job_Market_paper/docs/JMP_step0_status_v1.md` | none (redundant copy) | Byte-identical to committed `docs/normative/` copy | See section 5 |
| `Job_Market_paper/docs/results/JMP_BASELINE_F1_equivalised_reporting_v1.md and ..._verification_v1.md` | `docs/results/` (correct path) | Present only on `docs/seminar-r6`; the verification memo cites `Job_Market_paper/docs/results/...` | Missing from the checked-out fork branch until seminar-r6 is merged |
| `MNL/JMP_positive_fit_diagnostics_memo_v1.md` | with the POSFIT family (MNL root on `diagnostics/posfit-v2`) | Superseded POSFIT memo sitting untracked in the MNL root of the baseline-f1 checkout | Untracked |

Not misplaced: `docs/JMP_W1_theory_to_implementation_bridge_v1.md` is cited at exactly that path by `docs/normative/W1_latent_set_identification_note_v1.md` (line 27); moving it breaks the citation.

## 5. Duplicates (identical bytes at two or more paths)

Scope: every file under `Job_Market_paper/docs/` and `MNL/docs/`, plus repo-root `.md` files of Job_Market_paper, MNL and MNL_posfit (tracked and untracked; empty files and `__pycache__` skipped). The same repo-relative path in both MNL worktrees is one repository file, not a duplicate. **11 duplicate groups.** "Full-path refs" counts documents in scope (other than the copies) whose text contains that copy's repo-relative path; "filename mentions" counts documents containing the bare filename (cannot distinguish copies).

| SHA-256 (prefix) | Copies | Tracked | Full-path refs | Filename mentions |
|---|---|---|---|---|
| `4444548306f6` | `Job_Market_paper/docs/JMP_W1_stochastic_ability_set_bridge_v1.md`<br>`Job_Market_paper/docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | U / T | 0 / 0 | 3 / 3 |
| `81cdd1aee6e9` | `Job_Market_paper/docs/JMP_bridge_source_extract_v2.md`<br>`Job_Market_paper/docs/normative/JMP_bridge_source_extract_v2.md` | U / T | 0 / 0 | 4 / 4 |
| `8db40f10c180` | `Job_Market_paper/docs/JMP_frame_draw_law_audit_v1.md`<br>`MNL/docs/corr/JMP_frame_draw_law_audit_v1.md` | U / U | 0 / 0 | 0 / 0 |
| `c567f44317f1` | `Job_Market_paper/docs/JMP_project_state_latest.md`<br>`Job_Market_paper/JMP_project_state_v1.md` | T / T | 7 / 24 | 14 / 24 |
| `fd23084bb618` | `Job_Market_paper/docs/JMP_step0_status_v1.md`<br>`Job_Market_paper/docs/normative/JMP_step0_status_v1.md` | U / T | 0 / 0 | 1 / 1 |
| `ec16eba7472e` | `Job_Market_paper/docs/governance/JMP_certification_proportionality_rule_v1.md`<br>`MNL/docs/France_case/P2a/JMP_certification_proportionality_rule_v1.md` | T / T | 7 / 7 | 12 / 12 |
| `7ecbab78de26` | `Job_Market_paper/docs/handoffs/JMP_final_rich_engine_terms_contract_v1.yaml`<br>`MNL/docs/handoffs/JMP_final_rich_engine_terms_contract_v1.yaml` | T / T | 1 / 1 | 1 / 1 |
| `fe5274f77ca4` | `Job_Market_paper/docs/missions/JMP_M05C_incrementB_proportionality_decision_v1.md`<br>`MNL/docs/France_case/P2a/JMP_M05C_incrementB_proportionality_decision_v1.md` | T / T | 1 / 8 | 13 / 13 |
| `3425ab19b463` | `Job_Market_paper/docs/missions/JMP_M05C_minimal_streaming_implementation_mission_charter_v1.md`<br>`MNL/docs/France_case/P2a/JMP_M05C_minimal_streaming_implementation_mission_charter_v1.md` | T / T | 2 / 10 | 17 / 17 |
| `d7335e60fc21` | `MNL/docs/archive/inventories/external_storage_2026-05-12/external_storage_full_file_inventory_2026-05-12.csv`<br>`MNL/docs/archive/inventories/external_storage_2026-05-12/external_storage_reports_results_inventory_2026-05-12.csv` | T / T | 7 / 7 | 12 / 12 |
| `95b659c476c1` | `MNL/docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1 - Copy.md`<br>`MNL/docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1.md` | U / U | 2 / 2 | 2 / 4 |

Reading (judgment): for the three bridge/SRC pairs in Job_Market_paper, the tracked `docs/normative/` copy is the one cited by path in the normative record; the untracked `docs/` copies are working drops. The `MNL/docs/corr/JMP_frame_draw_law_audit_v1.md` / `Job_Market_paper/docs/JMP_frame_draw_law_audit_v1.md` pair is uncommitted on both sides.

## 6. Stale infrastructure

Registered MNL worktrees: `C:/Users/hisham/Repo/MNL`, `C:/Users/hisham/Repo/MNL/.claude/worktrees/agent-ae939588345df9c31`, `C:/Users/hisham/Repo/MNL/.claude/worktrees/jmp-m08-loc4-stage1`, `C:/Users/hisham/Repo/MNL_posfit`. Registered-but-missing (prunable): **none** — every registered path exists. Job_Market_paper has no linked worktrees.

| Item | What it is | Live dependency? | Evidence |
|---|---|---|---|
| `MNL/.claude/worktrees/jmp-m08-loc4-stage1` (~412 MB) | Claude agent worktree from M08 LOC4 Stage 1; branch `worktree-jmp-m08-loc4-stage1` @ `5b0e3d29` (contained in `main`). Holds 4 **untracked** files in `scripts/loc4/` (`loc4_stage1_lib.py`, `loc4_spec_extension.py`, `run_loc4_stage1_estimation.py`, `_loc4_stage1_report.json`), snapshotted in `wip/pre-cleanup-worktree-jmp-m08-loc4-stage1` (`960b37bb`). | **YES — LIVE.** | Committed MNL files reference this path at HEAD: `docs/France_case/P2a/FR_P2a_m08_loc4_beta_w_pexp2_profile_results_v1.md`, `docs/France_case/P2a/FR_P2a_m08_loc4_stage1_estimation_memo_v1.md`, `experiments/JMP_PS1/runs/ps1h_couples_p1/phase3_estimate.py`, `experiments/JMP_PS1/runs/ps1r1_bmo/step0c_missing_location_probe_v1.py`, `scripts/loc4/run_loc4_t2a_profile.py`, `scripts/ps1/run_ps1_battery_part1.py`, `scripts/ps1/run_ps1_item2_invariance.py`. The scripts import the Stage-1 library from it; removing the worktree breaks them. |
| `MNL/.claude/worktrees/agent-ae939588345df9c31` (~411 MB) | Claude agent worktree; branch `worktree-agent-ae939588345df9c31` @ `5b0e3d29` (contained in `main`); clean, no unique commits. | **No dependency found.** | 0 references to its path or branch in MNL or Job_Market_paper at HEAD. `.claude/` is ignored by MNL `.gitignore` (line 25). Its nested `dclaborsupply-monorepo` directory is empty. |
| `MNL_posfit/dclaborsupply-monorepo` (empty) | Gitlink (mode 160000) at `55bb0d0e` with **no `.gitmodules` entry**, so it was never initialised (`git submodule` fails with "no submodule mapping"). | **Not on this directory.** | POSFIT builders set `SOURCE_MNL` to the main `MNL` checkout when the criterion-A frames are absent from MNL_posfit (they are) and use `MNL/dclaborsupply-monorepo` as `EVALUATOR` with `EXPECTED_EVALUATOR = 55bb0d0e` (`MNL_posfit/scripts/diagnostics/build_positive_fit_diagnostics_v2.py` lines 31-33, 51). POSFIT therefore depends on the **main MNL working tree and its populated engine checkout**. |
| `MNL/dclaborsupply-monorepo` (populated, clean, HEAD `55bb0d0e`) | The engine checkout actually used by MNL; gitlink without `.gitmodules`. | **YES — LIVE.** | Cited by path in `JMP_measure_map_v1.md`, `W1_latent_set_identification_note_v1.md`, `JMP_bridge_source_extract_v2.md`, `JMP_step0_status_v1.md`, `baseline_f1_term_check_v1.md`, `JMP_bridge_review_factual_items_v1.md`; hash-pinned files inside it (section 2). |
| `C:/Users/hisham/Repo/dclaborsupply-monorepo` (standalone, HEAD `94c25f24`) | A second, newer engine checkout outside MNL. | Not on the pinned MNL path. | Recorded as "standalone checkout" in `JMP_step0_status_v1.md`; a relative `dclaborsupply-monorepo/...` path in `FR_P2a_region_live_phase5_source_verification_v1.md` can resolve to either checkout (section 2 flags the mismatch). |

## 7. MNL dirty classification

`git status --porcelain=v1` at MNL HEAD `76e2087291` (branch `welfare/baseline-f1`) shows **110 entries** with untracked directories collapsed (109 pre-existing plus `cleanup/` from CLEAN-A; the card's "~103" was an estimate), expanding to **222 files** with `-uall`. Files are classified individually by the rules in the Reason column (judgment). All files except the 51 CLEAN-A exclusions and the CLEAN-A state file are captured in `wip/pre-cleanup-welfare/baseline-f1` (`5a26cf47`); the exclusions not already in history are in the CLEAN-A quarantine.

| Group | Files | Entries wholly in group |
|---|---:|---:|
| (a) generated — reproducible from committed code at HEAD | 11 | 10 |
| (a′) generated — generator uncommitted or modified; reproducible only once group (b) is committed | 110 | 52 |
| (b) source, scripts or authored documents not yet committed | 34 | 23 |
| (c) editor/OS/build noise — belongs in .gitignore | 2 | 2 |
| (d) restricted or oversized — must never be committed | 51 | 16 |
| (e) unclassifiable — needs a decision | 14 | 5 |
| entries spanning several groups | — | 2: `docs/jmp_methodology/evidence/` ((a′)/(b)), `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/` ((a′)/(b)) |

### (a) generated — reproducible from committed code at HEAD — 11 files

| Status | Path | Reason |
|---|---|---|
| `??` | `experiments/JMP_PS1/runs/ps1_laneA_fourcell/operator_accounting_v1.json` | generated; generator committed and unmodified at HEAD |
| `??` | `experiments/JMP_PS1/runs/ps1c_fit_suite/calibration_curves.csv` | generated; generator committed and unmodified at HEAD |
| `??` | `experiments/JMP_PS1/runs/ps1c_fit_suite/category_shares.csv` | generated; generator committed and unmodified at HEAD |
| `??` | `experiments/JMP_PS1/runs/ps1c_fit_suite/chosen_prob_deciles.csv` | generated; generator committed and unmodified at HEAD |
| `??` | `experiments/JMP_PS1/runs/ps1c_fit_suite/chosen_rank_deciles.csv` | generated; generator committed and unmodified at HEAD |
| `??` | `experiments/JMP_PS1/runs/ps1c_fit_suite/confusion_long.csv` | generated; generator committed and unmodified at HEAD |
| `??` | `experiments/JMP_PS1/runs/ps1c_fit_suite/cube_top_misallocation.csv` | generated; generator committed and unmodified at HEAD |
| `??` | `experiments/JMP_PS1/runs/ps1c_fit_suite/post_estimation_comparison.html` | generated; generator committed and unmodified at HEAD |
| `??` | `experiments/JMP_PS1/runs/ps1s8a_acceptance/ps1s8a_hours_grid_v1.csv` | generated; generator committed and unmodified at HEAD |
| `??` | `outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__geometry_meta.json` | generated; generator committed and unmodified at HEAD |
| `??` | `outputs/p2a_singles2016/region_live_margqh_floor5_v1/fr_p2a_singles2016_regionlive_margqh_floor5_v1__mnlmeta.json` | generated; generator committed and unmodified at HEAD |

### (a′) generated — generator uncommitted or modified; reproducible only once group (b) is committed — 110 files

| Status | Path | Reason |
|---|---|---|
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/captions/figD06_occupation_isco_and_model.md` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/captions/figD07_observed_wages_annualised.md` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/captions/figD09_resource_components.md` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD06_occupation_isco_and_model.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_paper.pdf` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_paper.png` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_slide.pdf` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD07_observed_wages_annualised_slide.png` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_paper.pdf` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_paper.png` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_slide.pdf` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/figures/figD09_resource_components_slide.png` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/couples_reprice_target_only/cpl_b_reprice_batched_switch_record_v1.json` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_descriptives_continuous_v1.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_funnel_v1.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_occupation_v1.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_resource_components_v1.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_step1_funnel_v1.json` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_step2_descriptives_v1.json` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/ne_step1_gate_v1.json` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/tables/fd_descriptives_continuous_v1.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/tables/fd_descriptives_continuous_v1.md` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/tables/fd_occupation_v1.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/tables/fd_occupation_v1.md` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/tables/fd_resource_components_v1.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/tables/fd_resource_components_v1.md` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/tables/fd_sample_funnel_v1.csv` | generated; generator committed but carries uncommitted modifications (group b) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/tables/fd_sample_funnel_v1.md` | generated; generator committed but carries uncommitted modifications (group b) |
| `??` | `docs/corr/fr2016_drd_field_dictionary_v1.csv` | generated; generator untracked (group b) |
| `??` | `docs/corr/fr2016_source_audit_evidence_v1.json` | generated; generator untracked (group b) |
| `??` | `docs/corr/s12_consumption_floor_audit_v1.csv` | generated; generator untracked (group b) |
| `??` | `docs/corr/s12_consumption_floor_audit_v1.json` | generated; generator untracked (group b) |
| `??` | `docs/corr/s12_consumption_floor_audit_v1.md` | generated; generator untracked (group b) |
| `??` | `docs/corr/target_integrability_checks_v1.json` | generated; generator untracked (group b) |
| `??` | `docs/corr/welfare_identity_check_v1.json` | generated; generator untracked (group b) |
| `??` | `docs/corr/welfare_identity_check_v1.md` | generated; generator untracked (group b) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_frame.json` | generated; generator untracked (group b) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_halton.json` | generated; generator untracked (group b) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/ss34_decomp_results.json` | generated; generator untracked (group b) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/ss34_toy_results.json` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_hrs_parameter_table_v1.csv` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_occ_parameter_table_v1.csv` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_arm_occxhrs_parameter_table_v1.csv` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_frozen_parameter_table_v1.csv` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_proposal_fits_v1.json` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/ps1s16a_redraw_v1.json` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_PS1/runs/ps1s16b_gw_structural/ps1s16b_b_h_parameter_table_v1.csv` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_PS1/runs/ps1s16b_gw_structural/ps1s16b_b_nl_parameter_table_v1.csv` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.csv` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.pdf` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization.png` | generated; generator untracked (group b) |
| `??` | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/outputs/figS11_leisure_normalization_caption.txt` | generated; generator untracked (group b) |
| `??` | `notebooks/france/JMP_positive_fit_diagnostics_v1.ipynb` | generated; generator untracked (group b) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_hours_grid_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_manifest_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_parameter_table_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S1/ps1_s1_spec_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_hours_grid_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_manifest_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_parameter_table_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S2/ps1_s2_spec_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_hours_grid_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_manifest_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_parameter_table_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S3/ps1_s3_spec_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_hours_grid_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_manifest_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_parameter_table_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S4/ps1_s4_spec_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_hours_grid_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_manifest_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_parameter_table_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S6/ps1_s6_spec_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_hours_grid_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_manifest_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_parameter_table_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/20260829T132034Z_S7/ps1_s7_spec_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/ps1_battery_part1_manifest_20260829T132034Z.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_battery_part1_v1/ps1_model_comparison_part1_20260829T132034Z.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_derivation_note_v1.md` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_manifest_v1.json` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_result_block_v1.md` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/p2a_singles2016/region_live_margqh_v1/ps1_item2_invariance_v1/ps1_item2_verification_table_v1.csv` | generated by committed scripts that import the untracked LOC4 Stage-1 files in `.claude/worktrees/jmp-m08-loc4-stage1` (section 6) |
| `??` | `outputs/positive_fit_diagnostics_v1/coding_audit.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/extensive_margin_confusion.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/extensive_margin_metrics.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/01_les_distributions_counts_shares.pdf` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/01_les_distributions_counts_shares.png` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/02_extensive_margin_confusion.pdf` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/02_extensive_margin_confusion.png` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/03_intensive_margin_confusion.pdf` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/03_intensive_margin_confusion.png` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/04_hours_calibration_regression_to_mean.pdf` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/04_hours_calibration_regression_to_mean.png` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/05_participation_by_parameter_draw.pdf` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/figures/05_participation_by_parameter_draw.png` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/file_dependencies.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/hours_calibration.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/intensive_margin_class_metrics.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/intensive_margin_confusion.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/intensive_margin_summary_metrics.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/les_distribution.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/manifest.json` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/participation_parameter_draw_summary.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/participation_parameter_draws.csv` | generated; generator untracked (group b) |
| `??` | `outputs/positive_fit_diagnostics_v1/regression_to_mean_screen.csv` | generated; generator untracked (group b) |
| `??` | `reports/JMP_positive_fit_diagnostics_v1.html` | generated; generator untracked (group b) |
| `??` | `JMP_positive_fit_diagnostics_memo_v1.md` | generated by `scripts/diagnostics/build_positive_fit_diagnostics_v1.py` (untracked, group b); superseded by POSFIT v2 (section 3) |

### (b) source, scripts or authored documents not yet committed — 34 files

| Status | Path | Reason |
|---|---|---|
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/couples_reprice_target_only/run_couples_reprice_batched_switch_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/fd_common_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/make_fd_figures_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/run_fd_step1_funnel_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/final_descriptives/run_fd_step2_descriptives_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `·M` | `experiments/JMP_SEMINAR_SPRINT/runs/nested_endowments/run_ne_step1_gate_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `docs/corr/JMP_frame_draw_law_audit_v1.md` | authored document not committed |
| `??` | `docs/corr/fr2016_source_to_estimation_sample_audit_v1.md` | authored document not committed |
| `??` | `docs/corr/run_s12_consumption_floor_audit_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `docs/corr/target_model_and_integrability_v1.md` | authored document not committed |
| `??` | `docs/corr/welfare_integrator_chosen_row_v1.md` | authored document not committed |
| `??` | `docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1.md` | authored document not committed |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/README.md` | authored document not committed |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_frame.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/audit_halton.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/run_decomp.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/run_toy.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/tables.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/toy_sampler.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `docs/jmp_methodology/evidence/ss34_criterion_audit_v1/toy_world.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/render_s11_normalization_figure_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `experiments/JMP_SEMINAR_SPRINT/runs/s11_normalization_figure/run_s11_normalization_figure_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `no_gsur_setup/requirements.txt` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `no_gsur_setup/setup.ps1` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/corr/build_fr2016_source_audit_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/corr/check_target_integrability_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/corr/check_welfare_identity_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/diagnostics/build_positive_fit_diagnostics_v1.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/ps1/append_s16_model_comparison.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/ps1/ps1_s16_bands.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/ps1/run_ps1_s16a_diag.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/ps1/run_ps1_s16a_price.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/ps1/run_ps1_s16a_qw_proposal.py` | source or script not committed (new file, or committed file with uncommitted modifications) |
| `??` | `scripts/ps1/run_ps1_s16b_gw_structural.py` | source or script not committed (new file, or committed file with uncommitted modifications) |

### (c) editor/OS/build noise — belongs in .gitignore — 2 files

| Status | Path | Reason |
|---|---|---|
| `??` | `docs/jmp_methodology/JMP_sampled_alternatives_criterion_audit_v1 - Copy.md` | editor copy, byte-identical to the original |
| `??` | `experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/_s2_hours_audit.err` | stderr log (JAX warning) |

### (d) restricted or oversized — must never be committed — 51 files

| Status | Path | Reason |
|---|---|---|
| `??` | `docs/corr/welfare_finite_sum_examples_v1.csv` | contains criterion-A idhh values (ID-disclosure scan) |
| `??` | `docs/corr/welfare_finite_sum_examples_v1.md` | contains criterion-A idhh values (ID-disclosure scan) |
| `??` | `experiments/JMP_PS1/runs/ps1_channelD/_baseline_full_snapshot.parquet` | household-ID columns (idhh, idperson); these bytes are already in MNL history before `620a1ea3` |
| `??` | `experiments/JMP_PS1/runs/ps1_channelD/channelD_reference_profile_v1.parquet` | household-ID columns (idhh, idperson); these bytes are already in MNL history before `620a1ea3` |
| `??` | `experiments/JMP_PS1/runs/ps1_channelD/cs_common_correction_frame_v1.parquet` | household-ID columns (idhh, idperson); these bytes are already in MNL history before `620a1ea3` |
| `??` | `experiments/JMP_PS1/runs/ps1_channelD/cs_common_nodes_v1.parquet` | household-ID columns (idhh, idperson); these bytes are already in MNL history before `620a1ea3` |
| `??` | `experiments/JMP_PS1/runs/ps1_channelD/cs_common_priced_rows_v1.parquet` | household-ID columns (idhh, idperson); these bytes are already in MNL history before `620a1ea3` |
| `??` | `experiments/JMP_PS1/runs/ps1_channelD/cs_common_slotmap_v1.parquet` | household-ID columns (idhh, idperson); these bytes are already in MNL history before `620a1ea3` |
| `??` | `experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_engine_ready_v1.parquet` | household-ID columns; `ps1h_couples_engine_ready_v1.parquet` is also 53.9 MB |
| `??` | `experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_frame_v1.parquet` | household-ID columns; `ps1h_couples_engine_ready_v1.parquet` is also 53.9 MB |
| `??` | `experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_frame_v2.parquet` | household-ID columns; `ps1h_couples_engine_ready_v1.parquet` is also 53.9 MB |
| `??` | `experiments/JMP_PS1/runs/ps1h_couples_p1/ps1h_couples_priced_v1.parquet` | household-ID columns; `ps1h_couples_engine_ready_v1.parquet` is also 53.9 MB |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/BUNDLE_MANIFEST_v1.json` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/README_FIRST.md` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/secure_env_protocol_v1.md` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/00_manifest/verify_manifest.py` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_array_inventory_v1.csv` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_bounds_pins_v1.json` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_columns_documentation_v1.md` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_record_v1.json` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_starts_v1.csv` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_terms_v1.json` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/01_inputs/s8_theta_of_record_v1.csv` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/02_estimator/mnl_s8_numpy.py` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/02_estimator/selftest_s8_negll.py` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/bmo_mapping_disclosures_v1.json` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/fap2009_to_loc4_T_v2.csv` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/tension_z_matrix_22x4_v2_full.csv` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/tension_z_matrix_22x4_v2_hc090.csv` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/v2_audit_and_rebuild_v1.json` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/03_bmo/v2_fap_audit_and_map_v1.csv` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/04_join/join_db040f_v1.py` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/education_inventory_v1.py` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/export_pack_v1.py` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/lfs_desired_hours_v1.py` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/05_run/run_r1_estimations_v1.py` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/.keep` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/join_diagnostics_v1.json` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/06_out/selftest_v1.json` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/07_export/.keep` | secure-environment bundle (restricted); NOT matched by .gitignore |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_HRS_v1.parquet` | household-ID columns |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_OCC_v1.parquet` | household-ID columns |
| `??` | `experiments/JMP_PS1/runs/ps1s16a_qw_proposal/geometry/ps1s16a_geometry_ARM_OCCxHRS_v1.parquet` | household-ID columns |
| `??` | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T202801Z_262600_80d94f8b9c994b4890d52d4a2ab735df_u6r_smoke/RESTRICTED_DO_NOT_PUBLISH.txt` | restricted path |
| `??` | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T202850Z_133812_15108f9f85704ddc81c6729efb88e98b_u6resume2/RESTRICTED_DO_NOT_PUBLISH.txt` | restricted path |
| `??` | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T203836Z_194344_736992b537f341aeb18d124f5716f41c_u6resume3/RESTRICTED_DO_NOT_PUBLISH.txt` | restricted path |
| `??` | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/margqh_v2_20260823T213827Z_671796_47f3785e9c8946b48fd41cc09b9f48ed_u6resume4/RESTRICTED_DO_NOT_PUBLISH.txt` | restricted path |
| `??` | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074210Z_535880_837a2a554a744991b320ffc7ffaf9129_normsmoke/RESTRICTED_DO_NOT_PUBLISH.txt` | restricted path |
| `??` | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074322Z_686888_47fdba224d9e40f0a61b12e63acd05b8_normsmoke2/RESTRICTED_DO_NOT_PUBLISH.txt` | restricted path |
| `??` | `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/restricted/normalisation_v1_20260818T074423Z_472652_4f7193670e4542ae8229155aa77e8132_m08normfull/RESTRICTED_DO_NOT_PUBLISH.txt` | restricted path |
| `??` | `scripts/corr/check_welfare_finite_sum_examples_v1.py` | contains criterion-A idhh values (ID-disclosure scan) |

### (e) unclassifiable — needs a decision — 14 files

| Status | Path | Reason |
|---|---|---|
| `??` | `Data/documentation/DOCSILC065 operation 2015 VERSION july2014.pdf` | third-party EU-SILC documentation PDF (2.1 MB); vendoring decision needed |
| `??` | `cleanup/CLEAN_A_state_MNL_2026-09-12.txt` | CLEAN-A state record; disposition (commit as record or keep outside the tree) needs a decision |
| `??` | `experiments/JMP_PS1/education_counts_raw.csv` | household counts including cells below 30; no generator found; disclosure status undetermined |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/DARES_FAP2009_intro_et_table_de_correspondance.pdf` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/Matrice_PCS2020_ISCO08.csv` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/Matrice_PCS2020_ISCO08.xlsx` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/ResMetBE16.xlsx` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/ResmetBE15.xls` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/donnees_consolidees_2015.zip` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/donnees_consolidees_2016.zip` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/matrice_P2003_P2020.csv` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/matrice_P2020_P2003.csv` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_PS1/runs/ps1r1_bmo/source/table_passage_PCS2003_PCS2020.xlsx` | third-party public source data (DARES/INSEE/BMO; 17 MB incl. zips); licence/vendoring decision needed |
| `??` | `experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s2_hours_5_10_coverage_audit_v1.json` | no generator found in committed or untracked code |

## 8. Recommended merge order (recommendation only — not authorised)

Governing constraint from sections 1-2: every cited commit must stay reachable with its SHA. **Only fast-forwards or true merge commits are acceptable. No rebase, squash, or cherry-pick-then-delete of any branch that carries a cited commit.** Before and after each step, re-run the section 2 registry and confirm the MATCH count does not fall.

| Step | Repo | Action | Risk | Reason |
|---:|---|---|---|---|
| 0 | both | Commit nothing from the dirty trees until groups (d) and (e) are ruled on. First add `experiments/JMP_PS1/runs/ps1r1_bmo/secure_env_bundle_v1/` and the group (c) patterns to MNL `.gitignore`. | Low | `secure_env_bundle_v1/` is not ignored; a broad `git add` would commit it. |
| 1 | Job_Market_paper | Fast-forward `main` to `docs/w1-reference-domain-fork` (3 commits). | **Low** | Pure fast-forward; carries pinned `ce0ee3f`, `e278bcd` and the Deputy Goal 1 dashboard record. |
| 2 | Job_Market_paper | Merge `docs/seminar-r6` into `main` with a merge commit. | **Low-moderate** | No path overlap with step 1. `cafe0ba0`, cited by `JMP_step0_status_v1.md`, is reachable only from this branch, so rebasing or deleting it would orphan the citation. Brings the E3-EQ memos into `docs/results/`. |
| 3 | MNL | Fast-forward `main` to `corr/estimator-and-support` (23 commits). | **Low** | Pure fast-forward; includes the engine gitlink move `27756a06` to `55bb0d0e` already in use. |
| 4 | MNL | Fast-forward `main` to `welfare/baseline-f1` (6 further commits). | **Low** | Pure fast-forward after step 3; carries pinned `838127e0`, `68644680`, `d729cf89`, `6048c9f7`, `b5550af5`. |
| 5 | MNL | Merge `diagnostics/posfit-v2` into `main` with a merge commit. | **Moderate** | Diverged 4/3 from baseline-f1 at `d729cf89` with no overlapping path, but `0255bb98` and `a2e80a82` (cited) are reachable only from this branch, POSFIT provenance records branch names and HEADs, and the fit verdicts are still OPEN. Merging archives the work; it does not accept it. |
| 6 | MNL | Commit the four LOC4 Stage-1 files (from `wip/pre-cleanup-worktree-jmp-m08-loc4-stage1`) at a proper tracked path and re-point the five scripts, **before** any removal of `.claude/worktrees/jmp-m08-loc4-stage1`. | **Moderate** | Live dependency (section 6); changes committed code, so it needs a parity re-run. |
| 7 | both | Push `main` (MNL 94, Job_Market_paper 34 commits ahead of origin before these steps). | Low mechanically; outward-facing | Needs explicit authorisation. ID-bearing parquets are already in MNL history before `620a1ea3` and five Job_Market_paper normative documents cite household IDs; **the pending Deputy ID ruling should precede any push that spreads that history further.** |
| — | MNL | `handoff/final-rich-contract-v1`: do not merge. | **UNSAFE** | Its patch is already on `main`, and `main` has since changed the same YAML; a merge replays an add against a modified file (add/add conflict, risk of reverting the newer contract). Keep as the published handoff ref. |
| — | MNL | `feat/ps1-semi-flexible-couples-adapter`: do not merge. | **UNSAFE** | 6 unique commits against 70 on `main` since the merge-base; 58 of its files differ from `main`, whose R-233 content landed by another route. A merge risks silently reverting newer sprint files. Needs per-file review or retirement. |
| — | both | `wip/pre-cleanup-*`: never merge wholesale. | **UNSAFE** | Recovery snapshots that mix groups (a)-(e), including LaTeX `.aux`/`.log` build files in Job_Market_paper. |
| — | MNL | `diag/dben-program-attribution`, `worktree-agent-ae939588345df9c31`, `worktree-jmp-m08-loc4-stage1` | None | Already contained in `main`; nothing to merge. |

## Appendix — method limits

- Section 2 pairs a hash with a path heuristically in prose; rows marked NOT FOUND, NO PATH CITED or ambiguous were not guessed, and remain PINNED.
- Section 2b lists only citations with a file extension; directory citations are not listed.
- Section 3 statuses come only from document headers and explicit superseding statements; the dashboard was not used to override a document's own header.
- Section 7 separates (a) from (a′) by searching committed and untracked code for each output's filename; generators that build names dynamically may be misattributed between the two.
- This file is itself untracked in Job_Market_paper until committed.
