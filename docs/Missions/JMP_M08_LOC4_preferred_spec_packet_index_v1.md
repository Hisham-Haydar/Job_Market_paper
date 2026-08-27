# JMP-M08 — LOC4 PREFERRED-SPECIFICATION PACKET INDEX v1

**Object.** The index for the LOC4 preferred-specification packet: every
evidence object → the file and section that satisfies it, plus the sealed
artifact and hash behind it.

**Status.** Index only. It asserts no finding, selects no specification,
authorises nothing, and is uncommitted.

---

## 0. SOURCE STATUS — THE 16 ENUMERATED ITEMS ARE NOW ON DISK

**v1 as first written recorded that the deputy's enumerated evidence items 1–16
could not be located on disk, and declined to invent a numbering.** That gap is
now closed. The rulings document was extended by GOV-AC-2 and re-hashed for this
revision:

| | sha256 | ends at |
|---|---|---|
| at packet v1 | `2510542bb8b67726263f50bd59c830370bb38841f2545236149f1eadf94dbc75` | R-140 |
| **now** | **`8d4edafbe406f0b7e8154e2619b3ce49c1c1e793e7ba161c513f73450f56972d`** | **R-155** |

The enumeration is in
`::JMP::docs/Missions/JMP_M08_goal1_rulings_document_v4.md`, section
*"Appended 2026-08-27 — R-141 … R-155"*, item **(3) Deputy Ruling — Complete
LOC4 Preferred-Specification Packet First** — the option-(c) ruling — under the
heading `INDEPENDENT REVIEW`, following the instruction *"Attach or make
available:"*. §1 below re-keys the index to it, with each of the sixteen items
**QUOTED verbatim**.

The commissioned review named in that ruling has returned and is on disk:

| item | value |
|---|---|
| path | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_preferred_spec_review_v1.md` |
| **verified on disk** | **yes** |
| **sha256** | **`86d43fe08880a22749440827fb5d985f109f1575c4de65bde2da1ce44239de3c`** |
| bytes | `16237` |
| verdict token returned | **`LOC4_PREFERRED_PENDING_TIER2_BOUNDARY_ANALYSIS`** — one of the four the ruling permits |

Nothing in the evidence changed when the numbering became available; only the
keying did, exactly as v1 §0 anticipated.

---

## 1. THE DEPUTY'S 16 ENUMERATED ITEMS → FILE / SECTION

Ruling text QUOTED verbatim, item by item, from the option-(c) ruling's
`Attach or make available:` list. The ruling adds one exclusion, QUOTED:
*"No raw household-level or microdata file."* — satisfied throughout: every
artifact below is aggregate-only, and the persistence contract of record is
*"NO row-level data, NO household identifier, NO draw-level quantity."*

| # | deputy's item (QUOTED) | satisfied by | sealed artifact / hash |
|---|---|---|---|
| **1** | "frozen LOC4 design v4" | `::JMP::docs/Missions/JMP_M08_LOC4_robustness_design_v4.md` — used and re-hashed at every attempt's Stage-A gate | sha256 `8cf5280c55fc64b8b9cf35674ed921218609f8d043a190d5c1da38d9388b1a2c` |
| **2** | "final LOC4 estimation/inference memo" | `FR_P2a_m08_loc4_stage1_estimation_memo_v1.md` (whole); binding table §1, four-leg §2, inference conventions §3, curvature §5, gates §6, log Z §7, W-4 §8 | **S1** bundle `0dac858179dae8bae08a15755099e0b245cda7cf6881f7c7b0fa3970c7c6d688` |
| **3** | "LOC4 parameter/inference table" | memo 1 §3.1 (wage + δ), §3.2 (occupation access), **§3.3 full 50-coordinate table** | `loc4_parameter_table.csv` `b9d37f844c613959a6e78ffdd4c0b1c910ca304b6c2f66c2bee7ee05dbd2a752`; `loc4_standard_errors.csv` `5259f3c3007356b43961b0e4883a4b0f0ad8658f9e9de9ba2d56744e4093ba9f` |
| **4** | "G-L4-8 diagnostics" | memo 1 **§5** (tier boundaries §5, block table §5.1, joint curvature §5.2) | `loc4_extended_block_battery.csv` `adf9e823ab5734d1129b7bfdc328b81ab7cf4c740beb91a82f2dca642e53ab8f`; `loc4_curvature_diagnostics.json` `d2d3aed25d69f341d5221cee1ea03e8c47245fc161e3deda80f2d754087fa98b` |
| **5** | "Stage-2 materiality report" | `FR_P2a_m08_loc4_stage2_materiality_report_v1.md` (whole); verdict §6 | **S2** `0bb9558470b03e4f966b4159053168d3a374e9d52d378fbbb52203ccc55be21b` |
| **6** | "direct CRN difference tables" | memo 2 **§4.4** (the full 66-row Δ / `E_Δ` / threshold table); estimator §4.1, denominators §4.2, thresholds §4.3, C-16 §4.5 | **S2** `step3_differences.rows` |
| **7** | "six-scenario LOC4 S-10 report" | `FR_P2a_m08_loc4_s10_battery_report_v1.md` (whole); Tier-2 verdict §5, family-(ii) stability §6 | **S10** `a8e3724e8b1e00ad32a39bb42bd00e7448dec08f0592f3aeda2773bcf00b42ed` |
| **8** | "frozen scenario vectors and hashes" | memo 3 **§2** (six θ hashes and moved values); perturbation table §1.1 | `s1` `937a39c9…`, `s2` `33326cca…`, `s3` `343057b9…`, `s4` `bc2cb9dc…`, `s5` `8c116d35…`, `s6` `c5a0d064…` (full hashes in memo 3 §2) |
| **9** | "baseline M08 acceptance" | `FR_P2a_m08_u6_16x_limited_precision_review_v1.md`; the acceptance label and permitted claim set are QUOTED in memo 6 §1 from R-138 §9 | rulings v4 `8d4edafb…`; closure label `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` |
| **10** | "baseline limited-MC results" | memo 2 §3 (the bitwise reproduction, 726/726) and §5.2 (`baseline_level_gate_of_record`: T16 and `E_T` per headline); memo 6 §1 table | **u6ffn16** `1a6f586605e05da6b2057a85af7116ffb6b6fd536992ae60be2c4514b96c3a9d` |
| **11** | "baseline S-10 report" | memo 4 §(e.1)–(e.2) (the U10 / corrected-baseline S-10 coordinate rows and their binding arms); memo 3 §1.1 records that the baseline arm's own S-10 was **not** reused and **no numeral carried across** | **E4v2** `e4_manifest.json :: step3_s10`, `step3_s10_vs_e4v1`; `e4_s10_coordinates.csv` |
| **12** | "baseline and LOC4 aggregate functional maps" | memo 2 §4.4 carries both arms' T16 values for all 66 functionals side by side (`T16 BASE`, `T16 LOC4`); memo 3 §4.3–4.4 carry them per scenario | **S2** `step2_baseline_reproduction_crosscheck.per_functional` (66 functionals × 11 sub-bases); **S2** `arms.*.decomposition_T16` |
| **13** | "baseline and LOC4 W-4 diagnostics" | memo 1 §8 (LOC4 W-4 table and the membership change); memo 4 **§(e)** (all three records side by side: certified Phase-5, corrected baseline, LOC4) | **S1** `loc4_inference_diagnostics.json` `e6fee8b6…`; **E4v2** `e4_manifest.json :: step3_w4`, `step3_w4_vs_e4v1` |
| **14** | "exact nesting/model-comparison table" | `FR_P2a_m08_loc4_model_comparison_v1.md` §(a) nesting, §(b) common sample/objective, §(c) LR/df/p, §(d) AIC/BIC — summary table at **§(d.4)** | **S1** `nesting_proof`; `negll_certified_vector_loc4_builder_at_delta_zero = 18499.489277699933` bitwise |
| **15** | "parity/HK path closure" | **`FR_P2a_m08_parity_path_closure_v1.md`** (MNL, `docs/France_case/P2a/`); the per-run disposition actually used is at memo 2 §1.2 and memo 3 header | sha256 `68814c4f74d34e205e8a75179bcf75583e76ad2a68f014d71a9429b3de482d0d` |
| **16** | "specification-limits disclosure draft" | `FR_P2a_m08_loc4_specification_limits_disclosure_v1.md` (whole); consolidated ten-point list at **§10** | sha256 reported in the DET-AC-2 return |

**The review itself** — the object the sixteen items are attached *to* —
is `FR_P2a_m08_loc4_preferred_spec_review_v1.md`, sha256
`86d43fe08880a22749440827fb5d985f109f1575c4de65bde2da1ce44239de3c`
(verified on disk, 16,237 bytes), returning
`LOC4_PREFERRED_PENDING_TIER2_BOUNDARY_ANALYSIS`.

### 1.1 The ruling's nine adjudication topics → where the evidence sits

QUOTED verbatim from the same ruling (*"The review must adjudicate:"*):

| deputy's adjudication topic (QUOTED) | evidence at |
|---|---|
| "strict nesting and common objective" | memo 4 §(a), §(b) |
| "LR/AIC/BIC" | memo 4 §(c), §(d) |
| "convergence/rank/curvature" | memo 1 §2 (four-leg), §5 (G-L4-8 + joint curvature) |
| "economic validity of the LOC4 asymmetry repair" | memo 2 §8 (coherence finding **C-5**); memo 1 §1.2 (the extension is live) |
| "stability of the LOC4 materiality result" | memo 3 §6 (family-(ii) stability across all six scenarios) |
| "scope of the beta_w_pexp2 Tier-2 trigger" | memo 3 §5.5 and §3.2 (only `s5`/`s6` move any normalisation limb, and only `wage_limb_mu`); memo 5 §2 |
| "W4 normative-reference sensitivity" | memo 3 §7; memo 4 §(f) |
| "preferred specification" | memo 6 §2 (Disposition A) and §3 (Disposition B) — **PROPOSED**, not selected |
| "manuscript claim boundaries" | memo 5 §10; memo 6 §4 |

The ruling's constraint on the reviewer is QUOTED here for completeness:
*"The reviewer must not design a Tier-2 estimator or rewrite text."*

### 1.2 The deputy's own "COMPLETE THE DETERMINISTIC PACKET" list → where produced

QUOTED verbatim from the option-(c) ruling (*"Produce and verify:"*):

| deputy's item (QUOTED) | produced at |
|---|---|
| "exact nesting map" | memo 4 §(a) |
| "common sample and common objective" | memo 4 §(b) |
| "LR statistic, df and p-value" | memo 4 §(c) |
| "AIC and BIC, with the sample-size convention explicit" | memo 4 §(d) — both `N = 1,555` clusters and `N = 157,055` rows |
| "beta_w_pexp2 W-4 disclosure" | memo 4 §(e) |
| "W4/W6 normative-sensitivity disclosure" | memo 4 §(f) |
| "parity/HK path-only closure" | `FR_P2a_m08_parity_path_closure_v1.md` |
| "proposed manuscript claim set" | memo 6 |

The ruling's constraint on this packet is QUOTED here: *"No new estimation,
pinning or curvature re-specification."* — satisfied: `re_estimation = false`,
`euromod_executed = false`, `new_pricing = false`, `new_draw_produced = false`,
`commit = false` in every attempt, and the DET-AC-2 packet itself ran no code
against the model at all.

---

## 1A. THE PACKET — THE WRITTEN FILES

The seven DET-AC-1 files, plus the two standing documents they depend on.

| # | file | repository | what it satisfies | deputy item(s) |
|---|---|---|---|---|
| 1 | `docs/France_case/P2a/FR_P2a_m08_loc4_stage1_estimation_memo_v1.md` | MNL | the Stage-1 estimation record | 2, 3, 4, 13 |
| 2 | `docs/France_case/P2a/FR_P2a_m08_loc4_stage2_materiality_report_v1.md` | MNL | the Branch-B materiality record | 5, 6, 10, 12 |
| 3 | `docs/France_case/P2a/FR_P2a_m08_loc4_s10_battery_report_v1.md` | MNL | the six-scenario S-10 record | 7, 8, 12 |
| 4 | `docs/France_case/P2a/FR_P2a_m08_loc4_model_comparison_v1.md` | MNL | the deterministic comparison (nesting, common sample/objective, LR/df/p, AIC/BIC, the `beta_w_pexp2` W-4 disclosure, the W4/W6 normative-sensitivity disclosure) | 11, 13, 14 |
| 5 | `docs/France_case/P2a/FR_P2a_m08_loc4_specification_limits_disclosure_v1.md` | MNL | the limits draft the independent review reads | 16 |
| 6 | `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | Job_Market_paper | the proposed claim set under each disposition; carries the deputy's interpretation of record verbatim at §2.3 | 9 (in part) |
| 7 | `docs/Missions/JMP_M08_LOC4_preferred_spec_packet_index_v1.md` | Job_Market_paper | this index | — |
| — | `docs/France_case/P2a/FR_P2a_m08_parity_path_closure_v1.md` | MNL | parity / HK-01 path-only closure; sha256 `68814c4f74d34e205e8a75179bcf75583e76ad2a68f014d71a9429b3de482d0d` | 15 |
| — | `docs/France_case/P2a/FR_P2a_m08_loc4_preferred_spec_review_v1.md` | MNL | **the independent review itself** — the object items 1–16 are attached to; sha256 `86d43fe08880a22749440827fb5d985f109f1575c4de65bde2da1ce44239de3c`, 16,237 bytes, verdict `LOC4_PREFERRED_PENDING_TIER2_BOUNDARY_ANALYSIS` | — |
| — | `::JMP::docs/Missions/JMP_M08_LOC4_robustness_design_v4.md` | Job_Market_paper | the frozen design; sha256 `8cf5280c55fc64b8b9cf35674ed921218609f8d043a190d5c1da38d9388b1a2c` | 1 |

Item **9** ("baseline M08 acceptance") is satisfied by
`FR_P2a_m08_u6_16x_limited_precision_review_v1.md` together with R-138 §9 as
QUOTED in memo 6 §1; it predates this packet and is not re-issued here.

---

## 2. DESIGN-v4 §4.4 RETURN PACKET → SATISFYING SECTION

Design v4 §4.4 (the Branch-B return packet) enumerates seven items. The sealed
Stage-2 record carries them under `step5_branch_verdict.return_packet_s4_4`.
Each is indexed here to the memo section that reproduces it.

| §4.4 item | sealed location | satisfied by |
|---|---|---|
| LOC4 convergence class and four-leg verdict | **S2** `return_packet_s4_4.loc4_convergence_class_and_four_leg`; **S1** `convergence_records.json` | memo 1 §2 (all ten polished points, leg by leg); memo 2 §9 |
| parameter table `47 + K` with CR1 SEs | **S1** `loc4_parameter_table.csv`, `loc4_standard_errors.csv` | memo 1 §3 (wage + δ + occupation blocks) and §3.3 (full 50-coordinate table) |
| W-4 flagged membership | **S1** `loc4_inference_diagnostics.json :: W4` | memo 1 §8; full three-record history in memo 4 §(e) |
| per-criterion Δ, `E_Δ` and classification | **S2** `step4_materiality` | memo 2 §5.2 (M-1…M-4) and §4.4 (the full 66-row table) |
| full M-5 indicator table | **S2** `step4_materiality.M5` | memo 2 §5.3 |
| CRN regime with the box-hash comparison | **S2** `return_packet_s4_4.crn_regime_with_the_box_hash_comparison` | memo 2 §2.1; memo 1 §6 (G-L4-2) |
| G-L4-8 evidence | **S1** `loc4_curvature_diagnostics.json`, `loc4_extended_block_battery.csv` | memo 1 §5 |
| coherence findings that fired | **S2** `return_packet_s4_4.coherence_findings_that_fired` | memo 2 §8 |

---

## 3. THE FINE-GRAINED TOPIC INDEX → SATISFYING SECTION

§1 keys the packet to the deputy's sixteen items. This section is the
finer-grained index *underneath* them: it resolves individual evidence objects
to the memo section and the sealed numeral, one level below the deputy's
granularity. Nothing here supersedes §1; the two are consistent by construction.

### 3.1 Estimation

| topic | satisfied by | key sealed numeral |
|---|---|---|
| Stage-A binding table (19 keys, all matched) | memo 1 §1 | 19 / 19 `match: true` |
| bound specification and frame | memo 1 §1.1 | 1,555 hh × 101 alts = 157,055 rows; stem `4cc6a223…`; geometry `3a0408d6…` |
| four-leg verdict, all ten points | memo 1 §2.2–2.3 | `SINGLE-OPTIMUM`; spread `2.7212081477046013e-09` |
| leg-(c) convergence-class adjudication | memo 1 §2.3 | `NOT_APPLICABLE_SAME_CONVERGENCE_CLASS`; `max_interior_negll_minus_max_endpoint = -1.5643308870494366e-10` |
| θ_L4 vs θ-v2, wage block + δ_occ, robust SEs | memo 1 §3.1 | δ = (`-0.04134302463126545`, `0.05110026973872385`, `0.2910659382175672`), SE_rob (`0.04399615185873616`, `0.04023634711487535`, `0.04286334447100348`) |
| CR1 factor recomputed, not carried across | memo 1 §3 | `c` `1.0230263157894737` → `1.025049439683586`; K 35 → 38 |
| G-L4-8 tiers | memo 1 §5.1 | all four blocks **clean**, PD, rank 9/9, Cholesky true; `G-L4-8_blocks = false` |
| the G-L4 gate set (1–8) | memo 1 §6 | `blocking_not_passed = []` |
| the log Z movement | memo 1 §7 | Δ log Z mean `0.09408059279976157`, sd `0.07464679989066998`, vector sha256 `431bf81b…` |
| the W-4 membership change | memo 1 §8 | `newly_flagged = ["beta_w_pexp2"]` |

### 3.2 Materiality

| topic | satisfied by | key sealed numeral |
|---|---|---|
| validity battery, both arms | memo 2 §2 | alignment `0.0`; v13 split bitwise; N1–N9 8 PASS / 1 NOT_EVALUABLE; V6 & V22 pass, 0 flagged |
| bitwise baseline reproduction | memo 2 §3 | **726 / 726** values bitwise equal; `max_abs_deviation = 0.0` |
| the full 66-row difference / `E_Δ` / threshold table | memo 2 §4.4 | 43 pass / 23 fail precision |
| M-1…M-4 | memo 2 §5.2 | mean / Gini / `s_opp` `LOC4_MATERIAL`; median `UNCERTIFIED_NO_VERDICT` |
| M-5 | memo 2 §5.3 | `O_AB = 1` on T16 and all four T12_-b → aggregate `MATERIAL` |
| M-6 | memo 2 §5.4 | `Q-2` `CHANGED`; `Q-1`/`Q-3` `UNCHANGED`; `Q-4` `NOT_EVALUABLE_SEVERED` |
| the branch verdict | memo 2 §6 | Branch **B**; `LOC4 MATERIAL overall` |
| the Branch-C → Branch-B correction note | memo 2 §7 | superseded attempt `c21254f4…`; `SUPERSEDED_BY.txt` transcribed in full |
| C-16 | memo 2 §4.5 and §8 | named, NOT corrected |
| the coherence findings that fired | memo 2 §8 | C-5, C-7, C-9, C-15, C-16, C-1 |
| pipeline consequence | memo 2 §6.4 | *"NOTHING REBINDS PENDING DISPOSITION"* |

### 3.3 S-10

| topic | satisfied by | key sealed numeral |
|---|---|---|
| the perturbation table | memo 3 §1.1 | four coordinates, half-SE binding on all four |
| vector hashes | memo 3 §2 | six θ hashes, `s1` = `937a39c9…` |
| invariance assertions | memo 3 §3 | one 16x basis for seven arms; q^W correction vector `7c9cb21a…`; pooled weight `92a6431b…` |
| which normalisation limb moves | memo 3 §3.2 | `s2`/`s3`/`s4`: none; `s5`/`s6`: `wage_limb_mu` only |
| difference family (i), in full | memo 3 §4.3 | 66 × 6 rows |
| difference family (ii), in full | memo 3 §4.4 | 66 × 6 rows |
| the Tier-2 verdict | memo 3 §5 | `S10_TIER2_TRIGGER` on `{s5, s6}`; `scenarios_indeterminate_mc = []` |
| `beta_w_pexp2`-driven | memo 3 §5.5 | `s5` alone triggers; `s2`/`s3`/`s4` do not |
| family-(ii) stability | memo 3 §6 | `three_MATERIAL_headlines_stable_across_all_six = true`; `ordering_flip_stable_across_all_six = true` |
| the W4/W6 comparator disclosure | memo 3 §7 | W4 triggers on `{s3, s6}`; opposite sign on `s6`; W4/W6 Gini and `s_opp` uncertified |

### 3.4 Comparison

| topic | satisfied by | key sealed numeral |
|---|---|---|
| (a) the exact nesting map | memo 4 §(a) | `18499.489277699933` bitwise; δ-gradient non-zero |
| (b) common sample and common objective | memo 4 §(b) | identical stem/geometry/mnlmeta hashes; parser-object extension documented |
| (c) LR, df, p, boundary caveat | memo 4 §(c) | `LR = 92.86956706583442`, `df = 3`, `p = 5.297971492402584e-20` |
| (d) AIC and BIC, both `N` conventions | memo 4 §(d) | ΔAIC `-86.86956706583442`; ΔBIC `-70.82187459199486` / `-56.976513041467115` |
| (e) the `beta_w_pexp2` W-4 disclosure | memo 4 §(e) | flagged → unflagged → re-flagged across three records |
| (f) the W4/W6 normative-sensitivity disclosure | memo 4 §(f) | different scenario set; opposite sign on `s6`; Gini/`s_opp` uncertified |

### 3.5 Disclosure and manuscript

| topic | satisfied by |
|---|---|
| what neither specification can claim | memo 5 (whole), consolidated at §10 |
| ordering and `s_opp` specification-sensitivity | memo 5 §1 |
| the LOC4 level's `beta_w_pexp2` sensitivity | memo 5 §2 |
| the median uncertified in both arms | memo 5 §3 |
| the 22 uncertified differences | memo 5 §4 |
| subgroups `MC_UNSTABLE` | memo 5 §6 |
| W4/W6 quantitative robustness claimable by neither | memo 5 §5 |
| proposed claim set under Disposition A | memo 6 §2 |
| proposed claim set under Disposition B | memo 6 §3 |
| common to both dispositions | memo 6 §4 |

### 3.6 Parity closure

| topic | satisfied by | key numeral |
|---|---|---|
| the parity-axis / HK-01 collision and its permanent closure | **`FR_P2a_m08_parity_path_closure_v1.md`** (MNL, `docs/France_case/P2a/`), sha256 `68814c4f74d34e205e8a75179bcf75583e76ad2a68f014d71a9429b3de482d0d` | frozen axis `5b0e3d29e28126e1b3ee0340a243c09755da0b3b`; four R100 renames at `192ef57`; 76/76 pins re-verified at HEAD, undetached |
| the per-run disposition actually used by the two welfare attempts | memo 2 §1.2; memo 3 header | Goal-1 R-150.1: execution head `ced7176`, restore to `192ef57`; `gate_satisfied_not_waived = true`; `instruments_pins_thresholds_or_configs_modified = 0` |

---

## 4. THE SEALED ARTIFACTS BEHIND THE PACKET

| tag | path | hash |
|---|---|---|
| **S1** | `MNL/outputs/p2a_singles2016/region_live_margqh_v1/loc4_estimation_v1/attempts/20260826T125833Z_751624_055eb9daf2ed4f92bb66729e7f03a4b1_loc4_m3_deltaocc_stage1_LOC4_STAGE1_ESTIMATED_RETURN_W4_MEMBERSHIP_CHANGED/` | bundle `0dac858179dae8bae08a15755099e0b245cda7cf6881f7c7b0fa3970c7c6d688`; θ `937a39c9d67c8d07a1f996ed68dc55e049a6a564f1652d51f1b0d196cc747f13` |
| **S2** | `…/loc4_estimation_v1/attempts/20260826T135327Z_62296_949f4a1fd582437d88bfc52008d1ec81_loc4s2b_LOC4_STAGE2_BRANCH_B_MATERIAL_RETURN/loc4_stage2_comparison_v1.json` | `0bb9558470b03e4f966b4159053168d3a374e9d52d378fbbb52203ccc55be21b` |
| **S2-superseded** | `…/attempts/20260826T134525Z_761540_7f068f6a16e649dcb218fa25f3f8ae99_loc4s2_LOC4_STAGE2_BRANCH_C_INDETERMINATE_RETURN/loc4_stage2_comparison_v1.json` | `c21254f4cd06f3adf8f8d038913b9c060f74c87b8cc33ba68cb85348e43403d4` |
| **S10** | `MNL/outputs/p2a_singles2016/region_live_v1/loc4_estimation_v1/attempts/20260826T150805Z_148648_7309baf14b3f47c88ce271b3b1c41c66_loc4s10b_LOC4_S10_TIER2_TRIGGER_RETURN/loc4_s10_battery_v1.json` | `a8e3724e8b1e00ad32a39bb42bd00e7448dec08f0592f3aeda2773bcf00b42ed` |
| **u6ffn16** | `MNL/outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/20260825T164802Z_500708_1759e2e09f0941609ea183ae51ea8f20_u6ffn16_U6F_FUNCTIONALS16_DONE/u6f_functionals16_v1.json` | `1a6f586605e05da6b2057a85af7116ffb6b6fd536992ae60be2c4514b96c3a9d` |
| **E3v2** | `…/e3_estimation_v2/attempts/20260819T214600Z_672360_410223ff1ccd4d12b85d48b36d60fb1e_margqh_v2_phase3equiv_tightened_E3_CONVERGED_SINGLE_OPTIMUM/` | `theta_estimated_margqh_v2.csv` `fddb49984c03313f150bdfa6761efcab600b3cfd5e910d1d9e520b4d9fcd7c38`; `convergence_records.json` `9cf81c03e3e7e0ec58d87582f9454d5b076b53bccfe8d3154188878db926b50e`; θ bytes `2cf320c3aa4bd42424929f3092088abccf0a2240ba2eb1be0ad7fc068ba51971` |
| **E4v2** | `…/e4_curvature_inference_v2/attempts/20260819T214723Z_763848_8304bf6f33d94beba38b05a498049d01_margqh_v2_p4p5equiv_E4_PASS/` | `e4_manifest.json`, `e4_parameter_table.csv`, `e4_inference_diagnostics.json` |
| **design v4** | `Job_Market_paper/docs/Missions/JMP_M08_LOC4_robustness_design_v4.md` | `8cf5280c55fc64b8b9cf35674ed921218609f8d043a190d5c1da38d9388b1a2c` |
| **rulings v4** | `Job_Market_paper/docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | **now `8d4edafbe406f0b7e8154e2619b3ce49c1c1e793e7ba161c513f73450f56972d`** (through R-155, carrying the LOC4 interim ruling and the option-(c) ruling). Was `2510542bb8b67726263f50bd59c830370bb38841f2545236149f1eadf94dbc75` (through R-140) when **S2** pinned it as the M-6 claim-set source |
| **independent review** | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_preferred_spec_review_v1.md` | `86d43fe08880a22749440827fb5d985f109f1575c4de65bde2da1ce44239de3c` (16,237 bytes) |
| **corrected-baseline ruling** | `Job_Market_paper/docs/Missions/JMP_M08_proposal_density_convention_and_corrected_baseline_ruling_v1.md` | `6d9fa09fe999da9069c4cbeef367ffaeb4fb8faca0d7dfcf2c4ef4993daa2a4b` |
| **spec** | `MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` |
| **frozen basis** | `fr_p2a_singles2016_welfare_qw16_16x`, `alts = 1601`, `2489555` rows | box hash `67ef22b3742ccc04a25c377cec60e18478b6fd07e539c0340497a274c0ce2c52` |
| **package** | `dclaborsupply-monorepo` gitlink | `27756a06`; `package_modified = false` in every attempt |

---

## 5. OPEN GAPS — NONE IN THE PACKET

**v1 recorded one open gap:** `JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md`
§2.3 carried a marked, empty slot for the deputy's interpretation of record.
**That slot is now filled**, QUOTED verbatim from the appended interim ruling
(rulings v4, sha256
`8d4edafbe406f0b7e8154e2619b3ce49c1c1e793e7ba161c513f73450f56972d`). No
paraphrase was ever inserted, at any point.

**All sixteen deputy items are satisfied by an on-disk object** (§1). The
independent review is on disk and hashed. The packet has no open gap.

What remains open is **not** a packet gap but the deputy's own outstanding
decision. QUOTED verbatim from the option-(c) ruling:

> Until that packet is accepted:
>
> - baseline remains the reference benchmark;
> - LOC4 remains a material candidate;
> - neither is final preferred;
> - no preferred quantitative magnitude is frozen.

Standing status labels, QUOTED: corrected baseline
`ACCEPTED_REFERENCE_BASELINE_NOT_FINAL_PREFERRED`; LOC4
`LOC4_MATERIAL_TIER2_TRIGGER_PREFERRED_SPEC_PENDING`. Notebook label, QUOTED:
`LOC4_MATERIAL_TIER2_TRIGGER_PREFERRED_SPEC_PENDING`, with *"Do not label LOC4
preferred or restore the baseline ordering as robust."*

The five conditions the ruling sets for LOC4 to become preferred, QUOTED
verbatim, with the packet's evidence pointer against each — **status recorded,
not adjudicated**:

| # | condition (QUOTED) | evidence | on the record |
|---|---|---|---|
| 1 | "LOC4 S-10 produces no Tier-2 trigger and no S10_MATERIALITY_INDETERMINATE_MC" | memo 3 §5.5 | Tier-2 **DID** trigger on `{s5, s6}`; `scenarios_indeterminate_mc = []` |
| 2 | "the independent LOC4 review accepts" | review, sha256 `86d43fe0…` | returned `LOC4_PREFERRED_PENDING_TIER2_BOUNDARY_ANALYSIS` |
| 3 | "strict nesting/common-sample model comparison is verified" | memo 4 §(a), §(b) | verified — bitwise nesting; one artifact set |
| 4 | "all validity/support/normalisation gates remain passed" | memo 1 §6; memo 2 §2 | passed |
| 5 | "the LOC4-specific W-4 warning is locally stable" | memo 4 §(e); memo 3 §5 | `beta_w_pexp2` re-flagged; its perturbation is what triggers Tier-2 |

Condition 1 is not met on the current record and condition 5 is the reason. The
disposition is the deputy's.

---

*Index only. No finding, no selection, no authorisation. Uncommitted.*
