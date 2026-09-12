# docs/normative/INDEX.md — Job_Market_paper normative and record documents

> **STANDING NOTE — hashes after SANITISE-1.** After SANITISE-1 (`98e9f828`, merged to `main` at `dbfb20da`), the current SHA-256 of several documents deliberately **DIFFERS** from the hashes cited in rulings, acceptance memos and the CLEAN-B registry. Those citations resolve to the **historical commits named in each citing document** (for example `8a4df81`, `ce0ee3f`, `e278bcd`, `838127e0`). This is expected and is **not drift**. Live documents use the labels H-S1 / H-C1 / H-S2; the label-to-identifier mapping exists only in the restricted store, outside Git. History was not rewritten.

**Status vocabulary.** CURRENT — the version to read. SUPERSEDED-BY-<path> — replaced by the named file. PINNED — cited by path or hash in the CLEAN-B registry (`JMP_repo_inventory_v1.md` section 2): never move, rename, delete or edit. QUARANTINED — a copy is held in `EUROMOD-STORAGE/restricted/cleanup_quarantine_2026-09-12/`. UNKNOWN — not assessed; no status is implied. **This INDEX is the only place supersession is recorded.** Documents are not edited to carry status; the family table in the CLEAN-B inventory (section 3) is a dated snapshot and does not govern.

Commit = latest commit touching the path on `main` (Job_Market_paper) or on the named MNL branch. MNL rows are listed for family completeness; MNL was not modified by CLEAN-C1.

## Fork (W1 reference-domain fork, FORK-1)

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `docs/normative/JMP_W1_reference_domain_fork_v1.md` | CURRENT + PINNED | `8dcc476` | Theory/source audit of the W1 reference domain: full feasible set (F) versus market-job reference (M); REC-1 citation-closed. |
| 2 | `docs/normative/scripts/fork_derived_numerals_v1.py` | CURRENT + PINNED | `8dcc476` | REC-1 script reproducing every [derived here] numeral of the fork note. |
| 3 | `docs/normative/fork_derived_numerals_v1.csv` | CURRENT + PINNED | `8dcc476` | REC-1 pass/fail table (158 of 158 numerals reproduced). |
| 4 | `docs/normative/JMP_W1_fork_ruling_v1.md` | CURRENT + PINNED | `8dcc476` | Goal 1 implementation record of the Deputy FORK-1 ruling R1-R6; Appendix A (Deputy text) controls. |
| 5 | `docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` | CURRENT + PINNED | `358a2e8` | Deputy gate ruling: BASELINE-F-1 authorised in principle, locked until MEASURE-MAP-1R acceptance; C_obs treatment. |

## Measure map (MEASURE-MAP-1R / GATE-1)

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `docs/normative/JMP_measure_map_v1.md` | CURRENT + PINNED | `98e9f82` | MEASURE-MAP-1R audit mapping stored W1-W6 objects to the theory measures; sanitised at `98e9f82`; the gate cites both this commit and the historical `8a4df81`. |
| 2 | `docs/normative/JMP_measure_map_acceptance_v1.md` | CURRENT + PINNED | `98e9f82` | Goal 1 acceptance of MEASURE-MAP-1R and the BASELINE-F-1 unlock conditions; sanitised at `98e9f82`. |
| 3 | `docs/normative/baseline_f1_term_check_v1.md` | CURRENT + PINNED | `d58f93b` | GATE-1 step 2 term-by-term hard gate over the 99 S11 parameters: PASS. |
| 4 | `MNL: gate/measure_map_accepted.json` | CURRENT + PINNED | MNL `e57d3e25` (branch `welfare/baseline-f1`; not on MNL `main`) | Machine gate read by the BASELINE-F-1 validator; regenerated against `98e9f828` with the historical commit and hashes kept in a provenance field; validator PASS. |
| 5 | `MNL_posfit: gate/measure_map_accepted.json` | SUPERSEDED-BY-MNL:gate/measure_map_accepted.json@e57d3e25 | MNL `d729cf89` (branch `diagnostics/posfit-v2`) | Stale copy of the pre-SANITISE gate carried on the POSFIT branch; not regenerated. |

## Bridge (theory to implementation; market-set BRIDGE-1)

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `docs/JMP_W1_theory_to_implementation_bridge_v1.md` | SUPERSEDED-BY-docs/normative/W1_latent_set_identification_note_v1.md (partial: on the two points named in that note, lines 27-32) + PINNED | not committed (untracked in the Job_Market_paper checkout) | Diagnostic of the old W1-EA object against the theoretical W1 (N4 conjecture). |
| 2 | `docs/normative/W1_latent_set_identification_note_v1.md` | CURRENT + PINNED | `8dcc476` | What the RURO model maintains versus identifies about the latent opportunity set, and what W1 can mean under it. |
| 3 | `docs/JMP_market_set_bridge_and_parallel_work_ruling_v1.md` | UNKNOWN + PINNED | not committed (untracked in the Job_Market_paper checkout) | Deputy instruction: build the market-only random-set Measure 1 bridge first; bounded E3-EQ and POSFIT continuation. |
| 4 | `docs/JMP_BRIDGE1_amendment_v1.md` | UNKNOWN + PINNED | not committed (untracked in the Job_Market_paper checkout) | Deputy amendment to BRIDGE-1: keep utility, taste shock and opportunity density separate. |
| 5 | `docs/normative/JMP_W1_stochastic_ability_set_bridge_v1.md` | SUPERSEDED-BY-docs/normative/JMP_W1_stochastic_ability_set_bridge_v3.md + PINNED | `98e9f82` | BRIDGE-1 author draft: market-only random-set Measure 1 construction, compatibility and verdict; sanitised at `98e9f82`. |
| 6 | `docs/JMP_W1_stochastic_ability_set_bridge_v2.md` | QUARANTINED (RECOVERED-QUARANTINED) + SUPERSEDED-BY-docs/normative/JMP_W1_stochastic_ability_set_bridge_v3.md | not committed (untracked in the checkout; sanitised copy in the quarantine) | Correction pass 1 (SRC-3 items 9-11), recovered from the Goal 1 chat. Known defect of the file as produced: its H1 title reads `..._v1.md`; not corrected. |
| 7 | `docs/normative/JMP_W1_stochastic_ability_set_bridge_v3.md` | CURRENT + QUARANTINED | `3997d98` | Complete BRIDGE-1-AMEND-2 pass (amendment items 1-11 and review corrections); sanitised bytes committed at the path its header names; an earlier copy is also quarantined. |
| 8 | `docs/normative/JMP_W1_stochastic_ability_set_bridge_review_v1.md` | CURRENT + PINNED | `98e9f82` | Independent conceptual review of bridge v1 (reissued the same day with full inputs); sanitised at `98e9f82`. |
| 9 | `docs/normative/JMP_direct_g_welfare_ruling_v1.md` | CURRENT + PINNED | `e278bcd` | Deputy ruling: bridge verdict D accepted; direct opportunity-density welfare question reopened. |

## SRC (mechanical source extracts and audits)

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `docs/normative/JMP_step0_status_v1.md` | CURRENT + PINNED | `ce0ee3f` | SRC-1 Step-0 status: repository HEADs, paths and hashes as read on 2026-09-12 (dated snapshot; HEADs now stale). |
| 2 | `docs/JMP_bridge_source_extract_v1.md` | SUPERSEDED-BY-docs/normative/JMP_bridge_source_extract_v2.md + PINNED | not committed (untracked in the Job_Market_paper checkout) | SRC-1 quoted source extract (theory measure, specs, engine) with line anchors and hashes. |
| 3 | `docs/normative/JMP_bridge_source_extract_v2.md` | CURRENT + PINNED | `ce0ee3f` | SRC-2: resolves spec provenance - the pooled spec is the ancestor, not the S11 spec of record. |
| 4 | `docs/normative/JMP_bridge_review_factual_items_v1.md` | CURRENT + PINNED | `98e9f82` | SRC-3: frame and source answers to the factual items raised by the bridge review; sanitised at `98e9f82`. |
| 5 | `docs/JMP_frame_draw_law_audit_v1.md` | UNKNOWN | not committed (untracked in the Job_Market_paper checkout) | SRC-4: draw-law provenance of the S10 frames and wage-support reconciliation (identical untracked copy in MNL `docs/corr/`). |

## Household identifier sanitisation

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `docs/normative/JMP_household_identifier_sanitisation_decision_v1.md` | CURRENT | `98e9f82` | SANITISE-1 decision: live documents use labels H-S1/H-C1/H-S2; mapping only in the restricted store; history deliberately not rewritten. |

## BASELINE-F-1 (documents live in MNL)

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `MNL: docs/corr/baseline_f1_provenance_v1.md` | SUPERSEDED-BY-MNL:docs/corr/baseline_f1_prep2_report_v1.md + PINNED | MNL `68644680` (`welfare/baseline-f1`) | Independent provenance and the PREP-1 halt on utility entanglement (historical; the acceptance record cites its bytes at `838127e0`). |
| 2 | `MNL: docs/corr/baseline_f1_prep2_report_v1.md` | CURRENT | MNL `68644680` (`welfare/baseline-f1`) | PREP-2 implementation of the gated BASELINE-F-1 utility with engine and m08 oracles: PASS. |
| 3 | `MNL: docs/corr/baseline_f1_verification_v1.md` | CURRENT + PINNED | MNL `b5550af5` (`welfare/baseline-f1`) | Independent reconstruction reproducing every restricted household value: VERIFIED. |

## POSFIT (documents live in MNL)

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `MNL: JMP_positive_fit_diagnostics_memo_v1.md` | SUPERSEDED-BY-MNL_posfit:JMP_positive_fit_diagnostics_memo_v2.md | MNL `80608229` (`corr/estimator-and-support`; committed by another session) | Positive-fit diagnostics v1 on S8 singles / R240 couples. |
| 2 | `MNL_posfit: JMP_positive_fit_diagnostics_memo_v2.md` | SUPERSEDED-BY-MNL_posfit:JMP_positive_fit_diagnostics_memo_v2_S12.md | MNL `a2e80a82` (`diagnostics/posfit-v2`) | Bounded POSFIT-1R revision on the S11 models of record with pre-registered decision rules. |
| 3 | `MNL_posfit: JMP_positive_fit_diagnostics_memo_v2b_addendum.md` | UNKNOWN + PINNED | MNL `a2e80a82` (`diagnostics/posfit-v2`) | POSFIT-1R-B support-coverage addendum (2,048-node support, G1-G4 gates). |
| 4 | `MNL_posfit: JMP_positive_fit_diagnostics_memo_v2_S12.md` | CURRENT | MNL `96b6c883` (`diagnostics/posfit-v2`) | S12 binding-name alias preserving v2 and the addendum; zero-mass classification; fit verdicts OPEN pending Deputy review. |

## Deck / seminar

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `docs/seminar/deck_status_r6.md` | CURRENT | `cafe0ba` | Status of the 17 September R6 seminar deck: sources, build route and authority. |
| 2 | `docs/JMP_seminar_architecture_freeze_2026-09-17_v1.md` | CURRENT | not committed (untracked in the Job_Market_paper checkout) | Deputy freeze of welfare-architecture expansion until the seminar (OEC / finite-offer work on hold). |

## Repository housekeeping records

| Order | Path | Status | Commit | Contents |
|---:|---|---|---|---|
| 1 | `docs/normative/JMP_repo_inventory_v1.md` | CURRENT | `beec2fe` | CLEAN-B read-only inventory generated before SANITISE-1: topology, hash-cited registry (pre-sanitisation hashes), families, duplicates, stale infrastructure, merge order. |
| 2 | `cleanup/CLEAN_A_state_Job_Market_paper_2026-09-12.txt` | CURRENT | `beec2fe` | CLEAN-A record: branch, HEAD and verbatim porcelain status before cleanup. |
| 3 | `docs/normative/INDEX.md` | CURRENT | this commit (tag `clean/job-market-paper/2026-09-12`) | This index. |
| 4 | `docs/results/INDEX.md` | CURRENT | this commit | Index of results documents. |

## UNKNOWN — docs/ files outside the families (157 files)

Listed as in the CLEAN-B inventory. **Status UNKNOWN: not assessed, nothing implied.** PINNED is added only where the CLEAN-B registry cites the file (a fact, not a status judgment).

| Path | Status | Commit |
|---|---|---|
| `docs/JMP_core_packet_v2.md` | UNKNOWN | `f6a1130` |
| `docs/JMP_core_packet_v3.md` | UNKNOWN + PINNED | `27f89e2` |
| `docs/JMP_cross_repo_artifact_manifest_v1.md` | UNKNOWN + PINNED | `81302c9` |
| `docs/JMP_cross_repo_documentation_repair_report_v1.md` | UNKNOWN | `5e1e487` |
| `docs/JMP_cross_repo_documentation_staleness_audit_v1.md` | UNKNOWN | `81302c9` |
| `docs/JMP_cross_repo_manager_handoff_v1.md` | UNKNOWN | `81302c9` |
| `docs/JMP_literature_positioning_memo_v2.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/JMP_literature_positioning_memo_v3.md` | UNKNOWN + PINNED | `92a163d` |
| `docs/JMP_open_decisions_cross_repo_v1.md` | UNKNOWN | `81302c9` |
| `docs/JMP_project_state_identity_addendum_v1.md` | UNKNOWN + PINNED | `f6a1130` |
| `docs/JMP_project_state_identity_addendum_v2.md` | UNKNOWN + PINNED | `27f89e2` |
| `docs/JMP_project_state_latest.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/HK01/JMP_HK_01_delta_summary_v1.md` | UNKNOWN | `1f458de` |
| `docs/Missions/HK01/JMP_HK_01_final_acceptance_v1.md` | UNKNOWN + PINNED | `9e15e56` |
| `docs/Missions/HK01/JMP_HK_01_inventory_summary_v1.md` | UNKNOWN + PINNED | `1f458de` |
| `docs/Missions/HK01/JMP_HK_01_phase1_codex_rereview_v1.md` | UNKNOWN | `1f458de` |
| `docs/Missions/HK01/JMP_HK_01_phase1_codex_rereview_v2.md` | UNKNOWN | `1f458de` |
| `docs/Missions/HK01/JMP_HK_01_phase1_codex_review_v1.md` | UNKNOWN | `1f458de` |
| `docs/Missions/HK01/JMP_HK_01_v2_correction_note_v1.md` | UNKNOWN | `1f458de` |
| `docs/Missions/HK01/JMP_HK_01_v3_correction_note_v1.md` | UNKNOWN | `1f458de` |
| `docs/Missions/HK01/JMP_HK_01_v5_movable_rows_codex_review_v1.md` | UNKNOWN + PINNED | `9e15e56` |
| `docs/Missions/JMP_HK_01_authorization_and_PKG01A_crossref_ruling_v1.md` | UNKNOWN + PINNED | `1f458de` |
| `docs/Missions/JMP_M07I_manuscript_claim_rider_v1.md` | UNKNOWN | `d0a45c7` |
| `docs/Missions/JMP_M07I_positioning_memo_acceptance_rider_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M07I_positioning_memo_rider_acceptance_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md` | UNKNOWN | `30d63f9` |
| `docs/Missions/JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` | UNKNOWN + PINNED | `5b8edca` |
| `docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | UNKNOWN + PINNED | `e726174` |
| `docs/Missions/JMP_M08_E2_parity_report_v3_documentary_correction_ruling_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_LOC4_design_rereview_v3_reject_v1.md` | UNKNOWN | `d0a45c7` |
| `docs/Missions/JMP_M08_LOC4_design_rereview_v4_accept_v1.md` | UNKNOWN + PINNED | `d0a45c7` |
| `docs/Missions/JMP_M08_LOC4_design_review_v2_reject_v1.md` | UNKNOWN | `d0a45c7` |
| `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | UNKNOWN + PINNED | `e726174` |
| `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_v2.md` | UNKNOWN + PINNED | `eca4e56` |
| `docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | UNKNOWN + PINNED | `4c8b1fd` |
| `docs/Missions/JMP_M08_LOC4_preferred_spec_packet_index_v1.md` | UNKNOWN | `e726174` |
| `docs/Missions/JMP_M08_LOC4_robustness_design_v1.md` | UNKNOWN | `e726174` |
| `docs/Missions/JMP_M08_LOC4_robustness_design_v2.md` | UNKNOWN | `e726174` |
| `docs/Missions/JMP_M08_LOC4_robustness_design_v3.md` | UNKNOWN | `e726174` |
| `docs/Missions/JMP_M08_LOC4_robustness_design_v4.md` | UNKNOWN + PINNED | `e726174` |
| `docs/Missions/JMP_M08_RUM_benchmark_estimand_design_v1.md` | UNKNOWN | `1f458de` |
| `docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_U6_CV1_control_variate_design_v1.md` | UNKNOWN | `1f458de` |
| `docs/Missions/JMP_M08_U6_functional_MC_precision_ruling_v1.md` | UNKNOWN | `1f458de` |
| `docs/Missions/JMP_M08_U6_welfare_proposal_remediation_design_v1.md` | UNKNOWN + PINNED | `5efc37a` |
| `docs/Missions/JMP_M08_U6_welfare_proposal_remediation_ruling_v1.md` | UNKNOWN + PINNED | `5efc37a` |
| `docs/Missions/JMP_M08_ability_preference_operators_design_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_access_equalisation_operand_design_v1.md` | UNKNOWN | `30d63f9` |
| `docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_goal1_rulings_document_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_goal1_rulings_document_v2.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_goal1_rulings_document_v3.md` | UNKNOWN + PINNED | `5b8edca` |
| `docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | UNKNOWN + PINNED | `4c8b1fd` |
| `docs/Missions/JMP_M08_goal1_rulings_register_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_measure_definition_binding_memo_v1.md` | UNKNOWN | `30d63f9` |
| `docs/Missions/JMP_M08_opportunity_normalisation_and_notebook_restart_ruling_v1.md` | UNKNOWN + PINNED | `5efc37a` |
| `docs/Missions/JMP_M08_proposal_density_convention_and_corrected_baseline_ruling_v1.md` | UNKNOWN + PINNED | `5b8edca` |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v2.md` | UNKNOWN | `30d63f9` |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v3.md` | UNKNOWN | `30d63f9` |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v4.md` | UNKNOWN | `30d63f9` |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v5.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_stageA_contract_review_v1.md` | UNKNOWN + PINNED | `30d63f9` |
| `docs/Missions/JMP_M08_stageA_freeze_record_v1.md` | UNKNOWN | `30d63f9` |
| `docs/Missions/JMP_M08_welfare_input_handoff_v2.md` | UNKNOWN | `5b8edca` |
| `docs/Missions/JMP_current_state_dashboard_v1.md` | UNKNOWN + PINNED | `0ff8f74` |
| `docs/Missions/JMP_welfare_walkthrough_mission_v1.md` | UNKNOWN + PINNED | not committed (untracked in the Job_Market_paper checkout) |
| `docs/design_notes/JMP_M05C_W4_routing_memo_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/governance/JMP_Goal1_manager_operating_contract_v1.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/governance/JMP_canonical_state_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/governance/JMP_certification_proportionality_rule_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/governance/JMP_decision_log_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/governance/JMP_governance_creation_report_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/governance/JMP_management_hierarchy_and_delegation_v1.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/governance/JMP_mission_template_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/governance/JMP_program_governance_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/governance/JMP_roadmap_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/handoffs/CONTRACT_INDEX.md` | UNKNOWN | `3a8cc6a` |
| `docs/missions/JMP_LOC4_pathB_ruling_v1.md` | UNKNOWN | `27f89e2` |
| `docs/missions/JMP_M05B_E2_deputy_decision_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05B_E2_deputy_decision_v2.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05B_E2_escalation_code_review_reject_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05B_E2_escalation_final_review_reject_v2.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05B_mission_ledger_v1.md` | UNKNOWN | `7195fc5` |
| `docs/missions/JMP_M05B_pause_and_M05C_redesign_decision_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05B_phase5_implementation_mission_charter_v1.md` | UNKNOWN | `7195fc5` |
| `docs/missions/JMP_M05C_E2_incrementA_review_reject_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_E2_incrementB_second_reject_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_deputy_phase5_acceptance_v1.md` | UNKNOWN + PINNED | `1e54bcd` |
| `docs/missions/JMP_M05C_goal_manager_dryrun_acceptance_v1.md` | UNKNOWN + PINNED | `1e54bcd` |
| `docs/missions/JMP_M05C_incrementA_E2_deputy_decision_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_incrementB_proportionality_decision_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_minimal_streaming_implementation_mission_charter_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_mission_ledger_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_mission_ledger_v2.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_mission_ledger_v3.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_mission_ledger_v4.md` | UNKNOWN | `1e54bcd` |
| `docs/missions/JMP_M05C_mission_ledger_v5.md` | UNKNOWN | `7d29a1f` |
| `docs/missions/JMP_M05_PI_disclosure_determination_v1.md` | UNKNOWN | `f7cac33` |
| `docs/missions/JMP_M05_deputy_programme_acceptance_v1.md` | UNKNOWN + PINNED | `f7cac33` |
| `docs/missions/JMP_M05_design_stage_delegation_packet_v1.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/missions/JMP_M05_goal_manager_acceptance_v1.md` | UNKNOWN + PINNED | `f7cac33` |
| `docs/missions/JMP_M05_mission_ledger_v1.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/missions/JMP_M05_mission_ledger_v2.md` | UNKNOWN | `dfd65b2` |
| `docs/missions/JMP_M05_mission_ledger_v3.md` | UNKNOWN + PINNED | `f7cac33` |
| `docs/missions/JMP_M05_phase5_inference_mission_charter_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/missions/JMP_M05_source_verification_completeness_v1.md` | UNKNOWN + PINNED | `dfd65b2` |
| `docs/missions/JMP_M05_stageA_correction_memo_v1.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/missions/JMP_M05_task_manager_operating_prompt_v1.md` | UNKNOWN + PINNED | `f7cac33` |
| `docs/missions/JMP_M05_task_manager_operating_prompt_v2.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/missions/JMP_M05_task_plan_manager_acceptance_v1.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/missions/JMP_M05_task_plan_v1.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/missions/JMP_M07I_identity_alignment_acceptance_v1.md` | UNKNOWN + PINNED | `27f89e2` |
| `docs/missions/JMP_M07I_manuscript_identity_alignment_charter_v1.md` | UNKNOWN + PINNED | `7d29a1f` |
| `docs/missions/JMP_M07I_stageB_independent_consistency_review_v1.md` | UNKNOWN + PINNED | `f6a1130` |
| `docs/missions/JMP_M07_deputy_closeout_and_identity_ruling_v1.md` | UNKNOWN + PINNED | `f6a1130` |
| `docs/missions/JMP_M07_goal_manager_acceptance_v1.md` | UNKNOWN + PINNED | `7d29a1f` |
| `docs/missions/JMP_M07_inference_results_integration_mission_charter_v1.md` | UNKNOWN | `7d29a1f` |
| `docs/missions/JMP_M07_stageB_author_cover_note_v1.md` | UNKNOWN + PINNED | `7d29a1f` |
| `docs/missions/JMP_M07_stageC_independent_economics_review_v1.md` | UNKNOWN + PINNED | `7d29a1f` |
| `docs/missions/JMP_M08_singles_welfare_decomposition_mission_charter_v1.md` | UNKNOWN | `7d29a1f` |
| `docs/missions/JMP_M08_welfare_input_handoff_v1.md` | UNKNOWN + PINNED | `7d29a1f` |
| `docs/missions/JMP_goal1_phase5_strategic_assessment_v1.md` | UNKNOWN | `7d29a1f` |
| `docs/prompts/JMP_M05B_E2_goal_manager_resume_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05B_E2_goal_manager_resume_prompt_v2.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05B_architectural_closure_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05B_archive_and_test42_salvage_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05B_bounded_remediation_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05B_closed_form_code_review_v4_prompt_v1.md` | UNKNOWN + PINNED | `1e54bcd` |
| `docs/prompts/JMP_M05B_code_review_v2_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05B_goal_manager_delegation_prompt_v1.md` | UNKNOWN | `7195fc5` |
| `docs/prompts/JMP_M05B_restricted_store_provisioning_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05B_test42_housekeeping_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05C_closeout_and_evidence_commit_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05C_goal_manager_closeout_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05C_goal_manager_delegation_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05C_goal_manager_resume_after_incrementA_reject_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05C_goal_manager_resume_incrementB_proportionality_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05C_incrementA_bounded_refix_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05C_incrementA_review_v2_prompt_v1.md` | UNKNOWN + PINNED | `1e54bcd` |
| `docs/prompts/JMP_M05C_incrementB_focused_closure_review_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05C_incrementB_three_fix_closure_prompt_v1.md` | UNKNOWN | `1e54bcd` |
| `docs/prompts/JMP_M05D_goal_manager_delegation_prompt_v1.md` | UNKNOWN | `7d29a1f` |
| `docs/prompts/JMP_M05_inference_design_prompt_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/prompts/JMP_M05_management_checkpoint_commit_prompt_v1.md` | UNKNOWN + PINNED | `dfd65b2` |
| `docs/prompts/JMP_M05_methods_review_prompt_v1.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/prompts/JMP_M05_source_verification_prompt_v1.md` | UNKNOWN + PINNED | `f7cac33` |
| `docs/prompts/JMP_M05_source_verification_prompt_v2.md` | UNKNOWN + PINNED | `1d31d10` |
| `docs/prompts/JMP_M05_stageB_author_addendum_v1.md` | UNKNOWN | `f7cac33` |
| `docs/prompts/JMP_M05_stageC_reviewer_addendum_v1.md` | UNKNOWN | `f7cac33` |
| `docs/prompts/JMP_M05_stageD_cycle1_instruction_v1.md` | UNKNOWN | `f7cac33` |
| `docs/prompts/JMP_M05_task_plan_prompt_v1.md` | UNKNOWN + PINNED | `30fbe2d` |
| `docs/prompts/JMP_M05_v4_closure_and_documentation_prompt_v1.md` | UNKNOWN | `f7cac33` |
| `docs/prompts/JMP_M07_goal_manager_delegation_prompt_v1.md` | UNKNOWN | `7d29a1f` |
| `docs/prompts/JMP_M08_goal_manager_delegation_prompt_v1.md` | UNKNOWN | `7d29a1f` |
| `docs/prompts/JMP_cross_repo_state_audit_prompt_v1.md` | UNKNOWN | `5f6b727` |
| `docs/results/FR_P2a_phase5_inference_results_memo_v1.md` | UNKNOWN + PINNED | `7d29a1f` |

