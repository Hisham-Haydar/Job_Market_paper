# FINAL-GATE-1 synchronized claim-to-evidence report

**Verdict: PASS**

The gate parsed signed values from the six reader-rendered surfaces. It used PDF text, rendered HTML, executed notebook output plus reader-visible notebook Markdown, and rehearsal Markdown; it did not inspect the paper/deck TeX or notebook code as evidence.

## COMMIT-RV accepted reconciliation

- Goal 1 accepts the result-numeral count change from **6,167** to **6,152**: removing the reader-visible internal labels removed **19** label digits, while rebuilt-PDF text extraction contributed a net **+4** occurrences. The resulting arithmetic is 6,167 - 19 + 4 = 6,152. All 6,152 current occurrences resolve and there are zero mismatches; no scientific number, claim or result was changed.
- The separate repository-wide lineage sweep reports **10** failures. They are pre-existing, disclosed debt in untouched historical, live-legacy, untracked or orphaned files outside the reader-voice edit scope. COMMIT-RV authorizes the reader-voice commit without treating those failures as new drift and without weakening or deleting the lineage gate.
- Untouched lineage-debt paths: `reports/JMP_v5_review_and_modular_revision_plan_v1.md`; `reports/consistency_gate_v1.md`; `reports/model_extraction_v1.md`; `reports/novelty-audit-structural-well-being-inequality.md`; `reports/numbers_of_record_v1.json`; `reports/numbers_of_record_v3.json`; `reports/numbers_of_record_v4.json`; `reports/JMP_reference_profiles_v1.md`; `reports/figure_modules/v5_labour_market_opportunity_composition/build_figure.py`; `reports/figure_modules/v5_labour_market_opportunity_composition/evidence.md`.

## Six canonical surfaces

| surface | exact path | SHA-256 |
|---|---|---|
| deck | `C:\Users\hisham\Repo\Job_Market_paper\beamer\build\JMP_seminar_deck_r6.pdf` | `0d09fe7b68e5a881a697b0ac116e7f5e58323730a1a2d964e45a3540d9068b41` |
| story | `C:\Users\hisham\Repo\Job_Market_paper\reports\JMP_research_story_report_v5.html` | `8897459ce8d1638227e65d4c0680a3d95dfa68a623d44b5a33b0e8be27b289c1` |
| paper | `C:\Users\hisham\Repo\Job_Market_paper\manuscript\JMP_working_paper_for_seminar_v5.pdf` | `a8953b923fc64fc2bee033a8f680d91edfc7b99ee7ddeabc2de2a132288fcb34` |
| gallery | `C:\Users\hisham\Repo\Job_Market_paper\reports\JMP_results_gallery_current.html` | `7a0d8e7840c5bccb271f4c1e16974238ee1e19f50585d5b5093ab996bb3dfb5e` |
| notebook | `C:\Users\hisham\Repo\MNL\experiments\JMP_SEMINAR_SPRINT\JMP_canonical_AtoZ.ipynb` | `ce102ad5098e5f5479b306cdf516d8cc7473cceebc33714758a1fe5aace90632` |
| rehearsal | `C:\Users\hisham\Repo\Job_Market_paper\reports\rehearsal_pack_v1.md` | `246a3943bee92a82e5f6fe3fe3007490cb2b0dce2441d7d8e3a5eb18d1e9ce3c` |

## Retired-welfare content signatures

**PASS: zero retired-welfare content-signature hits across all six rendered surfaces.**

## Critical semantic, unit and sign checks

| surface | check | status | detail |
|---|---|---|---|
| deck | DECOMP headline | PASS | expected 1.8-9.9% |
| deck | variance headline | PASS | expected 100-127% when variance split is claimed |
| deck | DECOMP denominator | PASS | surface states baseline-Gini denominator |
| paper | DECOMP headline | PASS | expected 1.8-9.9% |
| paper | variance headline | PASS | expected 100-127% when variance split is claimed |
| paper | DECOMP denominator | PASS | surface states baseline-Gini denominator |
| story | DECOMP headline | PASS | expected 1.8-9.9% |
| story | variance headline | PASS | expected 100-127% when variance split is claimed |
| story | DECOMP denominator | PASS | surface states baseline-Gini denominator |
| gallery | DECOMP headline | PASS | expected 1.8-9.9% |
| gallery | variance headline | PASS | expected 100-127% when variance split is claimed |
| gallery | DECOMP denominator | PASS | surface states baseline-Gini denominator |
| notebook | DECOMP headline | PASS | expected 1.8-9.9% |
| notebook | variance headline | PASS | expected 100-127% when variance split is claimed |
| notebook | DECOMP denominator | PASS | surface states baseline-Gini denominator |
| rehearsal | DECOMP headline | PASS | expected 1.8-9.9% |
| rehearsal | variance headline | PASS | expected 100-127% when variance split is claimed |
| rehearsal | DECOMP denominator | PASS | surface states baseline-Gini denominator |
| deck | fit observed couples_female | PASS | coupled women: rendered=[89.8, 89.8]; source=89.802242% |
| deck | fit observed couples_male | PASS | coupled men: rendered=[92.3, 92.3]; source=92.298113% |
| deck | fit observed singles_female | PASS | single women: rendered=[85.5, 85.5]; source=85.484621% |
| deck | fit observed singles_male | PASS | single men: withheld (QUADRATURE-LIMITED) |
| story | fit observed couples_female | PASS | coupled women: rendered=[89.8, 89.8]; source=89.802242% |
| story | fit observed couples_male | PASS | coupled men: rendered=[92.3, 92.3]; source=92.298113% |
| story | fit observed singles_female | PASS | single women: rendered=[85.5, 85.5, 86.4]; source=85.484621% |
| story | fit observed singles_male | PASS | single men: withheld (QUADRATURE-LIMITED) |
| paper | fit observed couples_female | PASS | coupled women: rendered=[89.8]; source=89.802242% |
| paper | fit observed couples_male | PASS | coupled men: rendered=[92.3]; source=92.298113% |
| paper | fit observed singles_female | PASS | single women: rendered=[85.5]; source=85.484621% |
| paper | fit observed singles_male | PASS | single men: withheld (QUADRATURE-LIMITED) |
| rehearsal | fit observed couples_female | PASS | coupled women: rendered=[89.8]; source=89.802242% |
| rehearsal | fit observed couples_male | PASS | coupled men: rendered=[92.3]; source=92.298113% |
| rehearsal | fit observed singles_female | PASS | single women: rendered=[85.5]; source=85.484621% |
| rehearsal | fit observed singles_male | PASS | single men: withheld (QUADRATURE-LIMITED) |
| gate-self-test | signed parser negative control | PASS | injected -0.006888789 against source +0.006888789; resolver returned FAIL_SIGN |

## Resolved four-group positive-fit adjudication

All values are weighted and use the all-household scope. Accuracy and bands are proportions.

| group | G2 gate (ratio) | observed accuracy | simulated 95% band | prediction-conditioned verdict | model-simulated benchmark verdict | supported statement |
|---|---:|---:|---:|---|---|---|
| couples_female | ADEQUATE (0.018527) | 0.898022 | [0.886911, 0.916157] | MECHANICAL_STOCHASTIC_CONDITIONING | MISSPECIFICATION_EVIDENCE | report observed accuracy with its band and explicit composite verdicts |
| couples_male | ADEQUATE (0.239759) | 0.922981 | [0.892070, 0.921041] | MECHANICAL_STOCHASTIC_CONDITIONING | MISSPECIFICATION_EVIDENCE | report observed accuracy with its band and explicit composite verdicts |
| singles_female | ADEQUATE (0.150017) | 0.854846 | [0.808002, 0.865551] | INCONCLUSIVE_QUADRATURE_LIMITED | INCONCLUSIVE_QUADRATURE_LIMITED | report observed accuracy with its band and explicit composite verdicts |
| singles_male | QUADRATURE-LIMITED (0.299817) | 0.871213 | [0.763152, 0.842038] | MECHANICAL_STOCHASTIC_CONDITIONING | MISSPECIFICATION_EVIDENCE | withhold extensive accuracy; other composite rules are distinct |

## DECOMP-2 headline table

Signed convention: `Delta I = I_EMPTY - I_PAB`; a positive value is a reduction in inequality. Weighting is `dwt`.

| population | reporting scale | baseline Gini | PAB Gini | signed Delta I | % baseline | P contribution (share) | A contribution (share) | B contribution (share) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| singles | unequivalised | 0.233685512 | 0.226796723 | +0.006888789 | 2.948% | +0.001237388 (+18.0%) | +0.001614712 (+23.4%) | +0.004036689 (+58.6%) |
| singles | equivalised | 0.245091719 | 0.240641411 | +0.004450309 | 1.816% | -0.000307519 (-6.9%) | +0.001315187 (+29.6%) | +0.003442641 (+77.4%) |
| couples | unequivalised | 0.203541230 | 0.183401206 | +0.020140025 | 9.895% | +0.006427900 (+31.9%) | +0.000925912 (+4.6%) | +0.012786213 (+63.5%) |
| couples | equivalised | 0.197118749 | 0.192108878 | +0.005009871 | 2.542% | -0.001933949 (-38.6%) | +0.000732727 (+14.6%) | +0.006211092 (+124.0%) |

## Mismatches found and corrected

The pre-correction strings below used `g2_adequacy.csv::node_bootstrap_mean` while labelling the number as observed accuracy. The corrected value is `hard_classification_metrics.csv::extensive_accuracy`; the G2 mean remains only a numerical-adequacy diagnostic.

| surface occurrence | quantity | pre-correction | corrected/source-rounded |
|---|---|---:|---:|
| deck figure + B4 table | coupled men observed extensive accuracy | 92.2% | 92.3% |
| deck figure + B4 table | single women observed extensive accuracy | 85.7% | 85.5% |
| story-report figure | coupled men observed extensive accuracy | 92.2% | 92.3% |
| story-report figure | single women observed extensive accuracy | 85.7% | 85.5% |
| working-paper figure | coupled men observed extensive accuracy | 92.2% | 92.3% |
| working-paper figure | single women observed extensive accuracy | 85.7% | 85.5% |
| rehearsal script | coupled men observed extensive accuracy | 92.2% | 92.3% |
| rehearsal script | single women observed extensive accuracy | 85.7% | 85.5% |

No remaining sign, magnitude, unit/weighting, or source-resolution mismatch was found.

### Unsupported result numerals removed during correction

These reader-visible values had no source in the ruling's accepted-source list. They were removed rather than silently rebound to a numerically similar value elsewhere in the catalog.

| affected surface(s) | former claim | unsupported rendered value(s) | disposition |
|---|---|---|---|
| story report | consumption-normalizer table | 1,938.238719; 4,247.875047; 1,774.518218; 3,821.448012; 1,911.108058; 3,821.448012 EUR/month | exact table removed; qualitative invariance statement retained |
| story report; working paper | non-positive simulated-consumption floor counts | 22,597; 59,821 node-evaluations | counts removed; floor scope retained |
| story report; technical gallery | sub-ten-hour support-mass explanation | 4.15%; 0.00019%; expected count 0.249 | values removed; positive-mass/zero-realized-draw limitation retained |
| story report; working paper | predecessor-frame counts | 1,555; 2,275 households | counts removed; screening history and current S11 samples retained |
| story report; working paper | superseded single-adult curvature estimate | 0.168 | value removed; specification history retained |

## Cross-surface consistency (every resolved quantity on two or more surfaces)

| quantity/source locator | per-surface rendered values | status |
|---|---|---|
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:equivalised.C_eq.dwt_weighted_gini | deck: 0.226805; notebook: 0.226805; rehearsal: 0.226805; story: 0.2268, 0.2268 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:equivalised.C_eq.dwt_weighted_mean | notebook: 2245.109852; story: 2,245 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:equivalised.W_F_eq.dwt_weighted_gini | deck: 0.197403; notebook: 0.197403; rehearsal: 0.197403; story: 0.1974, 0.1974 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:equivalised.W_F_eq.dwt_weighted_mean | deck: 1 311; notebook: 1310.614979; rehearsal: 1,311; story: 1,311 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:equivalised.W_F_eq.dwt_weighted_median | deck: 1 237; notebook: 1237.352468; rehearsal: 1,237; story: 1,237 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:n_households | notebook: 2223, 2223; rehearsal: 2,223, 2,223, 2,223 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:unequivalised.W_F_obs.dwt_weighted_gini | notebook: 0.210354; rehearsal: 0.210 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:unequivalised.W_F_obs.dwt_weighted_mean | deck: 2 496; notebook: 2495.800866; rehearsal: 2,496 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:unequivalised.W_F_obs.dwt_weighted_median | deck: 2 356; notebook: 2356.493006; rehearsal: 2,356 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:worker_ratio.n_nonworkers_excluded | rehearsal: 50; story: 50 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json:worker_ratio.n_workers | rehearsal: 2,173; story: 2,173 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:equivalised.C_eq.dwt_weighted_gini | deck: 0.263292; notebook: 0.263292; story: 0.2633, 0.2633 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:equivalised.C_eq.dwt_weighted_mean | deck: 1 766; notebook: 1766.486493; rehearsal: 1,766; story: 1,766 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:equivalised.C_eq.dwt_weighted_median | deck: 1 588; notebook: 1588.290880; rehearsal: 1,588; story: 1,588 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:equivalised.C_eq.n | notebook: 1540, 1540; story: 1,540 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:equivalised.W_F_eq.dwt_weighted_gini | deck: 0.249807; notebook: 0.249807; story: 0.2498, 0.2498 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:equivalised.W_F_eq.dwt_weighted_mean | deck: 1 302; notebook: 1302.071576; rehearsal: 1,302; story: 1,302 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:equivalised.W_F_eq.dwt_weighted_median | deck: 1 165; notebook: 1165.140857; rehearsal: 1,165; story: 1,165 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:n_households | notebook: 1540; rehearsal: 1,540, 1,540, 1,540; story: 1,540, 1,540 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:unequivalised.W_F_obs.dwt_weighted_mean | notebook: 1434.811650; rehearsal: 1,435 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:unequivalised.W_F_obs.dwt_weighted_median | deck: 1 320; notebook: 1319.977952; rehearsal: 1,320 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:worker_ratio.n_nonworkers_excluded | rehearsal: 204; story: 204 | PASS |
| BASELINE:MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json:worker_ratio.n_workers | rehearsal: 1,336; story: 1,336 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/anchor_attainment_shares_v1.csv:row=14:share_attaining_the_observed_anchor_node | paper: 4, 4; story: 3.9 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/anchor_attainment_shares_v1.csv:row=6:mc_min | gallery: 1.8, 1.8; story: 1.8, 1.8 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/anchor_attainment_shares_v1.csv:row=7:share_attaining_the_observed_anchor_node | rehearsal: 3, 3; story: 3, 3, 3 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/anchor_attainment_shares_v1.csv:row=8:mc_min | gallery: 1.8; rehearsal: 1.8, 1.8; story: 1.8, 1.8, 1.8, 1.8 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/anchor_excluded_arm_v1.json:couples.equivalised.delta_I_relative_move | gallery: +9.3%, +9.3%; paper: 9.3; story: 9.3 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=10:I_S_gini | gallery: 0.1971; notebook: 0.197119; story: 0.1971 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=10:mc_max | gallery: 0.2075; story: 0.2075 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=10:mc_min | gallery: 0.1871; story: 0.1871 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=11:I_S_gini | gallery: 0.1969; notebook: 0.196910; story: 0.1969 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=11:change_from_actual | gallery: -0.0002; notebook: -0.000209; story: -0.0002 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=11:mc_max | gallery: 0.2069; story: 0.2069 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=11:mc_min | gallery: 0.1873; story: 0.1873 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=11:mc_range | deck: 1.96, 1.96; gallery: 2 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=12:I_S_gini | gallery: 0.1963; notebook: 0.196289; story: 0.1963 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=12:change_from_actual | gallery: -0.0008; notebook: -0.000829; story: -0.0008, -0.0008 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=12:mc_max | gallery: 0.2055; story: 0.2055 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=12:mc_min | gallery: 0.1869; story: 0.1869 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=13:I_S_gini | gallery: 0.1887; notebook: 0.188705; story: 0.1887 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=13:change_from_actual | gallery: -0.0084; notebook: -0.008413; story: -0.0084 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=13:mc_max | gallery: 0.1998; story: 0.1998 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=13:mc_min | gallery: 0.1789; story: 0.1789 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=14:I_S_gini | gallery: 0.1961; story: 0.1961, 20, 20 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=14:change_from_actual | gallery: -0.0010; story: -0.0010 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=14:mc_max | gallery: 0.2049; story: 0.2049 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=14:mc_min | gallery: 0.1861; story: 0.1861 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=15:I_S_gini | gallery: 0.1927; story: 0.1927 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=15:change_from_actual | gallery: -0.0044; story: -0.0044 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=15:mc_max | gallery: 0.2039; story: 0.2039 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=15:mc_min | gallery: 0.1829; story: 0.1829 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=16:I_S_gini | gallery: 0.1880; story: 0.1880 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=16:change_from_actual | gallery: -0.0091; story: -0.0091 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=16:mc_max | gallery: 0.1985; story: 0.1985 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=16:mc_min | gallery: 0.1775; story: 0.1775 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=17:I_S_gini | gallery: 0.1921; notebook: 0.192109; story: 0.1921 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=17:change_from_actual | gallery: -0.0050; notebook: -0.005010; story: -0.0050 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=2:I_S_gini | gallery: 0.2035; notebook: 0.203541; story: 0.2035 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=2:mc_max | gallery: 0.2144; story: 0.2144 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=2:mc_min | gallery: 0.1936; story: 0.1936 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=3:I_S_gini | gallery: 0.1956; notebook: 0.195631; story: 0.1956 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=3:change_from_actual | gallery: -0.0079; notebook: -0.007910; story: -0.0079 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=3:mc_max | gallery: 0.2059; story: 0.2059 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=3:mc_min | gallery: 0.1858; story: 0.1858 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=4:I_S_gini | gallery: 0.2025; notebook: 0.202539; story: 0.2025 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=4:change_from_actual | gallery: -0.0010; notebook: -0.001002; story: -0.0010 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=4:mc_max | gallery: 0.2140; story: 0.2140 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=4:mc_min | gallery: 0.1938; story: 0.1938 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=5:I_S_gini | gallery: 0.1892; notebook: 0.189193; rehearsal: 19; story: 0.1892 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=5:change_from_actual | gallery: -0.0143; notebook: -0.014348; story: -0.0143 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=5:mc_max | gallery: 0.2018; story: 0.2018 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=5:mc_min | gallery: 0.1803; rehearsal: 18, 18; story: 0.1803 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=6:I_S_gini | gallery: 0.1946; story: 0.1946 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=6:change_from_actual | gallery: -0.0089; story: -0.0089 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=6:mc_max | gallery: 0.2046; story: 0.2046 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=6:mc_min | gallery: 0.1844; story: 0.1844 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=6:mc_range | paper: 2, 2; rehearsal: 2, 2, 2, 2 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=7:I_S_gini | gallery: 0.1842; story: 0.1842 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=7:change_from_actual | gallery: -0.0193; story: -0.0193 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=7:mc_max | gallery: 0.1962; story: 0.1962 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=7:mc_min | gallery: 0.1742; story: 0.1742 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=8:I_S_gini | gallery: 0.1883; story: 0.1883 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=8:change_from_actual | gallery: -0.0152; story: -0.0152 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=8:mc_max | gallery: 0.2000; story: 0.2000 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=8:mc_min | gallery: 0.1796; story: 0.1796 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=9:I_S_gini | gallery: 0.1834; notebook: 0.183401; story: 0.1834 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=9:change_from_actual | gallery: -0.0201; notebook: -0.020140; story: -0.0201 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_couples.csv:row=9:mc_min | deck: 17; rehearsal: 17 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=10:I_S_gini | gallery: 0.2451; notebook: 0.245092; story: 0.2451 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=10:mc_max | gallery: 0.2663; story: 0.2663 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=10:mc_min | gallery: 0.2284; story: 0.2284 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=11:I_S_gini | gallery: 0.2456; notebook: 0.245591; story: 0.2456 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=11:change_from_actual | gallery: 0.0005; notebook: 0.000500; story: +0.0005 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=11:mc_max | gallery: 0.2647; story: 0.2647, 26.5 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=12:I_S_gini | gallery: 0.2436; notebook: 0.243647; story: 0.2436 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=12:change_from_actual | gallery: -0.0014; notebook: -0.001445; story: -0.0014 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=12:mc_max | gallery: 0.2631; story: 0.2631 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=12:mc_min | gallery: 0.2264, 0.2264; story: 0.2264, 0.2264 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=13:I_S_gini | gallery: 0.2419; notebook: 0.241891; story: 0.2419 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=13:change_from_actual | gallery: -0.0032; notebook: -0.003201; story: -0.0032 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=13:mc_max | gallery: 0.2592; story: 0.2592 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=14:I_S_gini | gallery: 0.2443; story: 0.2443 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=14:mc_max | gallery: 0.2624; story: 0.2624 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=14:mc_min | gallery: 0.2304, 0.2304; story: 0.2304, 0.2304 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=15:I_S_gini | gallery: 0.2418; story: 0.2418 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=15:change_from_actual | gallery: -0.0033; story: -0.0033 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=15:mc_max | gallery: 0.2594; story: 0.2594 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=15:mc_min | gallery: 0.2263; story: 0.2263 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=16:I_S_gini | gallery: 0.2405; story: 0.2405 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=16:change_from_actual | gallery: -0.0046; story: -0.0046 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=16:mc_max | gallery: 0.2582; story: 0.2582 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=16:mc_min | gallery: 0.2245; story: 0.2245 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=17:I_S_gini | gallery: 0.2406; notebook: 0.240641; story: 0.2406 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=17:change_from_actual | gallery: -0.0045; notebook: -0.004450; story: -0.0045 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=2:I_S_gini | gallery: 0.2337, 23.4%; notebook: 0.233686; paper: 23.4%; story: 0.2337 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=2:mc_max | gallery: 0.2509; story: 0.2509 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=2:mc_min | gallery: 0.2203; story: 0.2203 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=3:I_S_gini | gallery: 0.2326; notebook: 0.232621; story: 0.2326 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=3:change_from_actual | gallery: -0.0011; notebook: -0.001065; story: -0.0011 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=3:mc_max | gallery: 0.2491; story: 0.2491 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=3:mc_min | gallery: 0.2180; story: 0.2180 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=4:I_S_gini | gallery: 0.2319; notebook: 0.231912; story: 0.2319 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=4:change_from_actual | gallery: -0.0018; notebook: -0.001773; story: -0.0018 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=4:mc_max | gallery: 0.2480; story: 0.2480 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=4:mc_min | gallery: 0.2178; story: 0.2178 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=5:I_S_gini | gallery: 0.2298; notebook: 0.229813; story: 0.2298 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=5:change_from_actual | gallery: -0.0039; notebook: -0.003872; story: -0.0039 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=5:mc_max | gallery: 0.2452; story: 0.2452 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=5:mc_min | gallery: 0.2148; story: 0.2148 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=6:I_S_gini | gallery: 0.2310; story: 0.2310 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=6:change_from_actual | gallery: -0.0027; story: -0.0027 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=6:mc_max | gallery: 0.2478; story: 0.2478 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=6:mc_min | gallery: 0.2177; story: 0.2177 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=7:change_from_actual | gallery: -0.0054; story: -0.0054 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=7:mc_max | gallery: 0.2437; story: 0.2437 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=7:mc_min | gallery: 0.2138; story: 0.2138 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=8:I_S_gini | gallery: 0.2282, 0.2282; story: 0.2282, 0.2282 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=8:change_from_actual | gallery: -0.0055; story: -0.0055 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=8:mc_max | gallery: 0.2411; story: 0.2411 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=8:mc_min | gallery: 0.2135; story: 0.2135 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=9:I_S_gini | gallery: 0.2268; notebook: 0.226797; story: 0.2268 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/coalition_values_singles.csv:row=9:change_from_actual | gallery: -0.0069; notebook: -0.006889; story: -0.0069 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/log_variance_split_v1.csv:row=2:share_var_log_C | gallery: 126.8%, 127%; notebook: 127%; paper: 127%; rehearsal: 127%; story: 127%, 127%, 127% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/log_variance_split_v1.csv:row=2:var_log_W1F | gallery: 0.1905; rehearsal: 19, 19 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/log_variance_split_v1.csv:row=4:share_var_log_C | gallery: 100.4%, 100; paper: 100; rehearsal: 100; story: 100, 100, 100 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=10:gini_point_contribution | gallery: 0.0007; paper: +0.0007; story: +0.0007 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=10:second_seed_gini_point | gallery: 0.0008; paper: +0.0008; story: +0.0008 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=10:share_of_delta_I | gallery: 14.6%; paper: 14.6%; story: 14.6% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=11:gini_point_contribution | gallery: 0.0062; story: +0.0062 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=11:second_seed_gini_point | gallery: 0.0061; story: +0.0061 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=11:share_of_delta_I | gallery: 124.0%, 124.0%; story: 124.0% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=13:second_seed_gini_point | gallery: 0.0050, 0.0050; story: +0.0050, +0.0050 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=14:gini_point_contribution | gallery: 0.1921; rehearsal: 19 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=14:mc_max_gini_point | gallery: 0.2033; story: 0.2033 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=14:mc_min_gini_point | gallery: 0.1821; story: 0.1821 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=2:gini_point_contribution | gallery: 0.0064; story: +0.0064 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=2:second_seed_gini_point | gallery: 0.0065; story: +0.0065 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=3:second_seed_gini_point | gallery: 0.0009, 0.0009; story: +0.0009, +0.0009 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=3:second_seed_share_of_delta_I | gallery: 4.6%; story: 4.6% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=3:share_of_delta_I | gallery: 4.6%; paper: 4.6% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=4:gini_point_contribution | gallery: 0.0128; story: +0.0128 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=4:second_seed_gini_point | gallery: 0.0127; story: +0.0127 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=4:share_of_delta_I | gallery: 63.5%; story: 63.5% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=6:second_seed_gini_point | gallery: 0.0201, 0.0201, 2; paper: 2; rehearsal: 2, 2, 2; story: +0.0201, +0.0201, 2 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=7:mc_max_gini_point | gallery: 0.1944, 19.4%; story: 0.1944 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=7:mc_min_gini_point | gallery: 0.1731; story: 0.1731 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_couples.csv:row=9:second_seed_gini_point | gallery: -0.0019, -0.0019; story: -0.0019, -0.0019 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=10:gini_point_contribution | gallery: 0.0013; paper: +0.0013; story: +0.0013 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=10:second_seed_gini_point | gallery: 0.0014; paper: +0.0014; story: +0.0014 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=10:share_of_delta_I | gallery: 29.6%, 29.6%; paper: 29.6%; story: 29.6% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=11:gini_point_contribution | gallery: 0.0034; story: +0.0034 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=11:second_seed_gini_point | gallery: 0.0038; story: +0.0038 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=11:share_of_delta_I | gallery: 77.4%; story: 77.4% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=13:second_seed_gini_point | gallery: 0.0049, 0.0049, 0.0049, 0.0049, 0.0049, 0.0049; story: +0.0049 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=14:mc_max_gini_point | gallery: 0.2580; story: 0.2580 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=14:mc_min_gini_point | gallery: 0.2248; story: 0.2248 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=2:gini_point_contribution | gallery: 0.0012; story: +0.0012 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=2:second_seed_gini_point | gallery: 0.0011; story: +0.0011 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=3:gini_point_contribution | gallery: 0.0016; story: +0.0016 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=3:second_seed_gini_point | gallery: 0.0017; paper: +0.0017; story: +0.0017 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=4:gini_point_contribution | gallery: 0.0040; story: +0.0040 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=4:second_seed_gini_point | gallery: 0.0042; story: +0.0042 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=4:share_of_delta_I | gallery: 58.6%, 58.6%; story: 58.6% | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=6:gini_point_contribution | gallery: 0.0069; story: +0.0069 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=6:second_seed_gini_point | gallery: 0.0071; story: +0.0071 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=7:mc_max_gini_point | gallery: 0.2431; story: 0.2431 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=7:mc_min_gini_point | gallery: 0.2127; story: 0.2127 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=9:gini_point_contribution | gallery: -0.0003; story: -0.0003 | PASS |
| DECOMP:MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_singles.csv:row=9:second_seed_gini_point | gallery: -0.0004; story: -0.0004 | PASS |
| DECOMP:couples:unequivalised:delta_I_share_baseline | deck: 9.9%; gallery: 9.9%, 9.9%, 9.9%; notebook: 9.9%; paper: 9.9%, 9.9%, 9.9%, 9.9%; rehearsal: 9.9%, 9.9%, 9.9%; story: 9.9%, 9.9%, 9.9%, 9.9%, 9.9%, 9.9%, 9.9%, 9.9%, 9.9% | PASS |
| DECOMP:singles:equivalised:delta_I_share_baseline | deck: 1.8; notebook: 1.8; paper: 1.8, 1.8, 1.8, 1.8; rehearsal: 1.8; story: 1.8, 1.8, 1.8 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/observed_participation.csv:row=2:observed_participation_weighted | gallery: 0.9231, 0.9231, 0.9231, 0.9231, 0.9231, 0.9231, 0.9231, 0.9231; notebook: 0.9231, 0.9231, 0.9231, 0.9231, 0.9231, 0.9231, 0.9231, 0.9231 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/observed_participation.csv:row=3:observed_participation_weighted | gallery: 0.8984, 0.8984, 0.8984, 0.8984, 0.8984, 0.8984, 0.8984, 0.8984; notebook: 0.8984, 0.8984, 0.8984, 0.8984, 0.8984, 0.8984, 0.8984, 0.8984 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/observed_participation.csv:row=4:observed_participation_weighted | gallery: 0.8805, 0.8805, 0.8805, 0.8805, 0.8805, 0.8805, 0.8805, 0.8805; notebook: 0.8805, 0.8805, 0.8805, 0.8805, 0.8805, 0.8805, 0.8805, 0.8805 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/observed_participation.csv:row=5:observed_participation_weighted | gallery: 0.8642, 0.8642, 0.8642, 0.8642, 0.8642, 0.8642, 0.8642, 0.8642; notebook: 0.8642, 0.8642, 0.8642, 0.8642, 0.8642, 0.8642, 0.8642, 0.8642 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/primary_power_of_two_convergence.csv:row=11:predicted_participation_weighted | gallery: 0.8999; notebook: 0.8999; story: 90, 90 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/primary_power_of_two_convergence.csv:row=12:predicted_participation_weighted | gallery: 0.9015; notebook: 0.9015 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/primary_power_of_two_convergence.csv:row=13:node_count | deck: 2 048, 2 048; gallery: 2048, 2048, 2048, 2048; notebook: 2048, 2048, 2048, 2048; rehearsal: 2,048, 2,048 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/primary_power_of_two_convergence.csv:row=13:predicted_participation_weighted | gallery: 0.9023, 0.9023, 0.9023, 0.9023; notebook: 0.9023, 0.9023, 0.9023, 0.9023 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/primary_power_of_two_convergence.csv:row=14:predicted_participation_weighted | gallery: 0.7586; notebook: 0.7586 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/primary_power_of_two_convergence.csv:row=19:predicted_participation_weighted | gallery: 0.7705, 0.7705, 0.7705, 0.7705; notebook: 0.7705, 0.7705, 0.7705, 0.7705 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/primary_power_of_two_convergence.csv:row=25:predicted_participation_weighted | gallery: 0.8304, 0.8304, 0.8304, 0.8304; notebook: 0.8304, 0.8304, 0.8304, 0.8304 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/primary_power_of_two_convergence.csv:row=7:predicted_participation_weighted | gallery: 0.9058, 0.9058, 0.9058, 0.9058; notebook: 0.9058, 0.9058, 0.9058, 0.9058 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=10:mean | gallery: 0.8925; notebook: 0.8925 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=10:median | gallery: 0.9034; notebook: 0.9034 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=10:node_count | gallery: 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50; notebook: 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=10:p90 | gallery: 0.9311; notebook: 0.9311 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=11:mean | gallery: 0.8941; notebook: 0.8941 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=11:median | gallery: 0.8940; notebook: 0.8940 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=11:node_count | gallery: 100, 100, 100, 100; notebook: 100, 100, 100, 100 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=11:p10 | gallery: 0.8632; notebook: 0.8632 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=11:p90 | gallery: 0.9207; notebook: 0.9207 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=12:mean | gallery: 0.8981; notebook: 0.8981 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=12:node_count | gallery: 200, 200, 200, 200; notebook: 200, 200, 200, 200 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=12:p10 | gallery: 0.8709; notebook: 0.8709 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=12:p90 | gallery: 0.9204; notebook: 0.9204 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=13:node_count | gallery: 400, 400, 400, 400; notebook: 400, 400, 400, 400 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=13:p10 | gallery: 0.8847; notebook: 0.8847 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=13:p90 | gallery: 0.9162; notebook: 0.9162 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=14:mean | gallery: 0.9002; notebook: 0.9002 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=14:median | gallery: 0.8994; notebook: 0.8994 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=14:node_count | gallery: 800, 800, 800, 800; notebook: 800, 800, 800, 800 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=14:p10 | gallery: 0.8883; notebook: 0.8883 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=14:p90 | gallery: 0.9120; notebook: 0.9120 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=15:mean | gallery: 0.9014; notebook: 0.9014 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=15:median | gallery: 0.9003, 0.9003; notebook: 0.9003, 0.9003 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=15:node_count | gallery: 1200, 1200, 1200, 1200; notebook: 1200, 1200, 1200, 1200 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=15:p10 | gallery: 0.8958; notebook: 0.8958 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=15:p90 | gallery: 0.9091; notebook: 0.9091 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=16:mean | gallery: 0.9028; notebook: 0.9028 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=16:median | gallery: 0.9027; notebook: 0.9027 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=16:node_count | gallery: 1600, 1600, 1600, 1600; notebook: 1600, 1600, 1600, 1600 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=16:p10 | gallery: 0.8992; notebook: 0.8992 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=16:p90 | gallery: 0.9066; notebook: 0.9066 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=18:p10 | gallery: 0.7240; notebook: 0.7240 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=18:p90 | gallery: 0.8236; notebook: 0.8236 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=19:mean | gallery: 0.7776; notebook: 0.7776 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=19:median | gallery: 0.7779; notebook: 0.7779 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=19:p10 | gallery: 0.7334; notebook: 0.7334 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=19:p90 | gallery: 0.8210; notebook: 0.8210 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=20:mean | gallery: 0.7665, 0.7665; notebook: 0.7665, 0.7665 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=20:median | gallery: 0.7701, 0.7701, 0.7701; notebook: 0.7701, 0.7701, 0.7701 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=20:p10 | gallery: 0.7315; notebook: 0.7315 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=20:p90 | gallery: 0.7961; notebook: 0.7961 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=21:mean | gallery: 0.7725; notebook: 0.7725 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=21:median | gallery: 0.7734; notebook: 0.7734 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=21:p10 | gallery: 0.7504; notebook: 0.7504 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=21:p90 | gallery: 0.7952; notebook: 0.7952 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=22:p10 | gallery: 0.7532; notebook: 0.7532 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=22:p90 | gallery: 0.7856; notebook: 0.7856 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=23:mean | gallery: 0.7704; notebook: 0.7704 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=23:median | gallery: 0.7707, 0.7707; notebook: 0.7707, 0.7707 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=23:p10 | gallery: 0.7615; notebook: 0.7615 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=23:p90 | gallery: 0.7794; notebook: 0.7794 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=24:mean | gallery: 0.7700; notebook: 0.7700 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=24:p10 | gallery: 0.7654; notebook: 0.7654 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=24:p90 | gallery: 0.7738; notebook: 0.7738 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=26:mean | gallery: 0.8364; notebook: 0.8364 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=26:median | gallery: 0.8475; notebook: 0.8475 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=26:p10 | gallery: 0.7818; notebook: 0.7818 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=26:p90 | gallery: 0.8849; notebook: 0.8849 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=27:mean | gallery: 0.8332; notebook: 0.8332 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=27:median | gallery: 0.8376; notebook: 0.8376 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=27:p10 | gallery: 0.7898; notebook: 0.7898 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=27:p90 | gallery: 0.8760; notebook: 0.8760 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=28:mean | gallery: 0.8283; notebook: 0.8283 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=28:p10 | gallery: 0.7922; notebook: 0.7922 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=28:p90 | gallery: 0.8579; notebook: 0.8579 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=29:mean | gallery: 0.8320; notebook: 0.8320 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=29:median | gallery: 0.8313; notebook: 0.8313 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=29:p10 | gallery: 0.8199; notebook: 0.8199 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=29:p90 | gallery: 0.8468; notebook: 0.8468 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=2:mean | gallery: 0.9039; notebook: 0.9039 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=2:p10 | gallery: 0.8533; notebook: 0.8533 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=2:p90 | gallery: 0.9455; notebook: 0.9455 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=30:mean | gallery: 0.8323; notebook: 0.8323 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=30:median | gallery: 0.8310; notebook: 0.8310 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=30:p10 | gallery: 0.8198; notebook: 0.8198 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=30:p90 | gallery: 0.8451; notebook: 0.8451 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=31:mean | gallery: 0.8308, 0.8308; notebook: 0.8308, 0.8308 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=31:median | gallery: 0.8309; notebook: 0.8309 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=31:p10 | gallery: 0.8220; notebook: 0.8220 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=31:p90 | gallery: 0.8387; notebook: 0.8387 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=32:mean | gallery: 0.8295; notebook: 0.8295 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=32:median | gallery: 0.8302, 0.8302; notebook: 0.8302, 0.8302 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=32:p10 | gallery: 0.8241; notebook: 0.8241 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=32:p90 | gallery: 0.8343; notebook: 0.8343 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=3:mean | gallery: 0.9026; notebook: 0.9026 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=3:p10 | gallery: 0.8618; notebook: 0.8618 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=3:p90 | gallery: 0.9428; notebook: 0.9428 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=4:mean | gallery: 0.9037; notebook: 0.9037 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=4:median | gallery: 0.8996; notebook: 0.8996 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=4:p10 | gallery: 0.8787; notebook: 0.8787 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=4:p90 | gallery: 0.9367; notebook: 0.9367 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=5:mean | gallery: 0.9084; notebook: 0.9084 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=5:median | gallery: 0.9074; notebook: 0.9074 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=5:p10 | gallery: 0.8887; notebook: 0.8887 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=5:p90 | gallery: 0.9250; notebook: 0.9250 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=6:mean | gallery: 0.9071; notebook: 0.9071 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=6:median | gallery: 0.9077; notebook: 0.9077 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=6:p10 | gallery: 0.8951; notebook: 0.8951 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=6:p90 | gallery: 0.9191; notebook: 0.9191 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=7:mean | gallery: 0.9070; notebook: 0.9070 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=7:median | gallery: 0.9069; notebook: 0.9069 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=7:p10 | gallery: 0.9010, 0.9010; notebook: 0.9010, 0.9010 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=7:p90 | gallery: 0.9149; notebook: 0.9149 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=8:mean | gallery: 0.9060; notebook: 0.9060 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=8:median | gallery: 0.9057; notebook: 0.9057 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=8:p10 | gallery: 0.9025; notebook: 0.9025 | PASS |
| NODE:MNL_posfit/outputs/posfit_node_convergence_v1/secondary_deputy_list_convergence.csv:row=8:p90 | gallery: 0.9095, 0.9095; notebook: 0.9095, 0.9095 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/convergence.csv:row=12:abs_mean_share_change_unweighted | gallery: 0.0824; notebook: 0.0824 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/convergence.csv:row=12:max_abs_dP_household | paper: 2; story: 2 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/convergence.csv:row=19:abs_mean_share_change_weighted | gallery: 0.5914, 0.5914; notebook: 0.5914, 0.5914 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/convergence.csv:row=29:abs_mean_share_change_unweighted | gallery: 0.2499, 0.2499; notebook: 0.2499, 0.2499 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/deciles.csv:row=11:decile | paper: 10, 1,000, 1,000, 1,000, 1,000, 1,000; rehearsal: 10; story: 1,000, 1,000 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/deciles.csv:row=16:decile | gallery: 500; notebook: 500, 500; paper: 500; rehearsal: 500; story: 500, 500 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/deciles.csv:row=19:decile | notebook: 8; rehearsal: 8 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/deciles.csv:row=53:mean_observed_hours | gallery: 40; notebook: 40 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/ess_summary.csv:row=10:n_households_with_mass | notebook: 2223; paper: 2,223; story: 2,223, 2,223 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=105:g2_threshold_0_25_sampling_sd | paper: 0.1669; story: 0.1669 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=117:adequacy_ratio_mcse_to_sampling_sd | deck: 0.15; rehearsal: 0.15 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=123:monte_carlo_se | gallery: 0.0148; notebook: 0.0148 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=124:monte_carlo_se | gallery: 0.0148; notebook: 0.0148 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=125:adequacy_ratio_mcse_to_sampling_sd | paper: 0.25; rehearsal: 0.25; story: 0.25, 0.25, 0.250 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=128:monte_carlo_se | gallery: 0.0007; notebook: 0.0007 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=129:monte_carlo_se | gallery: 0.0022; notebook: 0.0022 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=169:monte_carlo_se | gallery: 0.0149; notebook: 0.0149 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=170:monte_carlo_se | gallery: 0.0149; notebook: 0.0149 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=174:monte_carlo_se | gallery: 0.0025; notebook: 0.0025; rehearsal: 0.25 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=175:monte_carlo_se | gallery: 0.0062; notebook: 0.0062 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=25:adequacy_ratio_mcse_to_sampling_sd | deck: 0.02; rehearsal: 0.02 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=25:node_bootstrap_mean | deck: 89.8%; gallery: 0.8980; notebook: 0.8980; rehearsal: 89.8% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=31:monte_carlo_se | gallery: 0.0122; notebook: 0.0122 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=32:monte_carlo_se | gallery: 0.0122; notebook: 0.0122 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=36:monte_carlo_se | gallery: 0.0011; notebook: 0.0011 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=37:monte_carlo_se | gallery: 0.0032; notebook: 0.0032 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=71:adequacy_ratio_mcse_to_sampling_sd | deck: 0.24; rehearsal: 0.24, 0.2398, 0.239759; story: 0.240 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=72:simulated_sd | gallery: 0.2177; notebook: 0.2177 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=85:node_bootstrap_mean | gallery: 1.064e+05; notebook: 1.064e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=90:monte_carlo_se | gallery: 0.0156; notebook: 0.0156 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=91:monte_carlo_se | gallery: 0.0156; notebook: 0.0156 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=92:monte_carlo_se | gallery: 0.0016; notebook: 0.0016 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv:row=93:monte_carlo_se | gallery: 0.0044; notebook: 0.0044 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=3:extensive_accuracy | deck: 92.3%; notebook: 0.922981; story: 92.3%, 92.3% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=3:extensive_balanced_accuracy | gallery: 0.5053; notebook: 0.5053 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=5:extensive_accuracy | notebook: 0.898022; story: 89.8%, 89.8% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=5:extensive_balanced_accuracy | gallery: 0.4998, 0.4998; notebook: 0.4998, 0.4998 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=7:extensive_balanced_accuracy | gallery: 0.6689; notebook: 0.6689 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=7:intensive_balanced_accuracy | gallery: 0.2496; notebook: 0.2496 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=7:intensive_sensitivity_macro | gallery: 0.2496; notebook: 0.2496 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=9:extensive_accuracy | notebook: 0.854846; story: 85.5%, 85.5% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=9:extensive_balanced_accuracy | gallery: 0.5373; notebook: 0.5373 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=9:intensive_balanced_accuracy | gallery: 0.2648; notebook: 0.2648 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=9:intensive_sensitivity_macro | gallery: 0.2648; notebook: 0.2648 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/hard_classification_metrics.csv:row=9:intensive_specificity_macro | gallery: 0.7489; notebook: 0.7489 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_extended.csv:row=3:bin_1_median_predicted_hours | gallery: 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5; notebook: 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_extended.csv:row=5:bin_1_mean_predicted_hours | gallery: 33.5, 33.5, 33.5, 33.5, 33.5, 33.5, 33.5, 33.5; notebook: 33.5, 33.5, 33.5, 33.5, 33.5, 33.5, 33.5, 33.5 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_extended.csv:row=5:bin_2_observed_mean_hours | gallery: 27; notebook: 27 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_extended.csv:row=9:bin_2_mean_signed_error | gallery: 7; notebook: 7 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=14:mean_predicted_hours | gallery: 33.4608; notebook: 33.4608 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=14:mean_signed_error | gallery: 21.0564, 21.0564; notebook: 21.0564, 21.0564 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=14:median_predicted_hours | gallery: 34.6203; notebook: 34.6203 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=14:share_above | gallery: 93.18%; notebook: 93.18% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=14:share_below | gallery: 6.82%; notebook: 6.82% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=14:weighted_n | gallery: 1.406e+05; notebook: 1.406e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=15:mean_absolute_error | gallery: 6.0557; notebook: 6.0557 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=15:mean_predicted_hours | gallery: 32.9238; notebook: 32.9238 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=15:mean_signed_error | gallery: 5.6392; notebook: 5.6392 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=15:median_predicted_hours | gallery: 30.7300; notebook: 30.7300 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=15:n | gallery: 459; notebook: 459 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=15:share_above | gallery: 96.54%; notebook: 96.54% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=15:share_below | gallery: 3.46%; notebook: 3.46% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=15:weighted_n | gallery: 9.849e+05; notebook: 9.849e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=16:mean_absolute_error | gallery: 4.4620; notebook: 4.4620 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=16:mean_predicted_hours | gallery: 33.0463; notebook: 33.0463 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=16:mean_signed_error | gallery: -3.8765; notebook: -3.8765 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=16:median_predicted_hours | gallery: 30.7244; notebook: 30.7244 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=16:n | gallery: 1,214; notebook: 1,214 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=16:share_below | gallery: 2.94%; notebook: 2.94% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=16:share_inside | gallery: 97.06%; notebook: 97.06% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=16:weighted_n | gallery: 2.851e+06; notebook: 2.851e+06 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=17:mean_absolute_error | gallery: 15.5878; notebook: 15.5878 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=17:mean_predicted_hours | gallery: 32.5896; notebook: 32.5896 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=17:mean_signed_error | gallery: -15.5878; notebook: -15.5878 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=17:median_predicted_hours | gallery: 30.5168; notebook: 30.5168 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=17:n | gallery: 288; notebook: 288 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=17:share_below | gallery: 100.00%, 100.00%; notebook: 100.00%, 100.00% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=17:weighted_n | gallery: 6.968e+05; notebook: 6.968e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=22:mean_predicted_hours | gallery: 35.9323; notebook: 35.9323 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=22:mean_signed_error | gallery: 25.0277, 25.0277; notebook: 25.0277, 25.0277 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=22:median_predicted_hours | gallery: 37.7227; notebook: 37.7227 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=22:share_above | gallery: 27.26%; notebook: 27.26% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=22:share_below | gallery: 72.74%; notebook: 72.74% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=22:weighted_n | gallery: 39,506.4; notebook: 39,506.4 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=23:mean_absolute_error | gallery: 11.0864; notebook: 11.0864 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=23:mean_predicted_hours | gallery: 36.6733; notebook: 36.6733 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=23:mean_signed_error | gallery: 11.0835; notebook: 11.0835 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=23:median_predicted_hours | gallery: 37.3324; notebook: 37.3324 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=23:share_above | gallery: 62.19%; notebook: 62.19% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=23:share_below | gallery: 37.81%; notebook: 37.81% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=23:weighted_n | gallery: 1.163e+05; notebook: 1.163e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=24:mean_absolute_error | gallery: 2.3280; notebook: 2.3280 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=24:mean_predicted_hours | gallery: 37.1372; notebook: 37.1372 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=24:mean_signed_error | gallery: -0.1973; notebook: -0.1973 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=24:median_predicted_hours | gallery: 37.3594; notebook: 37.3594 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=24:n | gallery: 403; notebook: 403 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=24:share_below | gallery: 20.67%; notebook: 20.67% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=24:share_inside | gallery: 79.33%; notebook: 79.33% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=24:weighted_n | gallery: 1.229e+06; notebook: 1.229e+06 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=25:mean_absolute_error | gallery: 10.8510; notebook: 10.8510 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=25:mean_predicted_hours | gallery: 37.0833; notebook: 37.0833 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=25:mean_signed_error | gallery: -10.8510; notebook: -10.8510 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=25:median_predicted_hours | gallery: 37.3452; notebook: 37.3452 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=25:n | gallery: 157; notebook: 157 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=25:share_below | gallery: 99.68%; notebook: 99.68% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=25:share_inside | gallery: 0.32%; notebook: 0.32% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=25:weighted_n | gallery: 5.040e+05; notebook: 5.040e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=30:mean_predicted_hours | gallery: 31.2876; notebook: 31.2876 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=30:mean_signed_error | gallery: 16.9615, 16.9615; notebook: 16.9615, 16.9615 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=30:median_predicted_hours | gallery: 30.7401; notebook: 30.7401 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=30:share_above | gallery: 55, 55.01%; notebook: 55, 55.01% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=30:share_below | gallery: 34.19%; notebook: 34.19% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=30:share_inside | gallery: 10.80%; notebook: 10.80% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=30:weighted_n | gallery: 67,334.5; notebook: 67,334.5 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=31:mean_absolute_error | gallery: 6.7946; notebook: 6.7946 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=31:mean_predicted_hours | gallery: 33.0698; notebook: 33.0698 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=31:mean_signed_error | gallery: 6.5838; notebook: 6.5838 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=31:median_predicted_hours | gallery: 33.6725; notebook: 33.6725 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=31:n | gallery: 136; notebook: 136 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=31:share_above | gallery: 83.54%; notebook: 83.54% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=31:share_below | gallery: 16.46%; notebook: 16.46% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=31:weighted_n | gallery: 3.574e+05; notebook: 3.574e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=32:mean_absolute_error | gallery: 3.5768; notebook: 3.5768 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=32:mean_predicted_hours | gallery: 33.6103; notebook: 33.6103 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=32:mean_signed_error | gallery: -3.2783; notebook: -3.2783 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=32:median_predicted_hours | gallery: 34.3195; notebook: 34.3195 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=32:n | gallery: 425; notebook: 425 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=32:share_below | gallery: 15.50%; notebook: 15.50% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=32:share_inside | gallery: 84.50%; notebook: 84.50% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=32:weighted_n | gallery: 1.219e+06; notebook: 1.219e+06 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=33:mean_absolute_error | gallery: 13.9670; notebook: 13.9670 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=33:mean_predicted_hours | gallery: 33.8403; notebook: 33.8403 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=33:mean_signed_error | gallery: -13.9670; notebook: -13.9670 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=33:median_predicted_hours | gallery: 34.3653; notebook: 34.3653 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=33:n | gallery: 141; notebook: 141 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=33:weighted_n | gallery: 3.958e+05; notebook: 3.958e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=6:mean_predicted_hours | gallery: 37.6165; notebook: 37.6165 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=6:mean_signed_error | gallery: 26.2186, 26.2186; notebook: 26.2186, 26.2186 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=6:median_predicted_hours | gallery: 40.5326; notebook: 40.5326 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=6:share_above | gallery: 100.00%; notebook: 100.00% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=6:weighted_n | gallery: 6,744.2; notebook: 6,744.2 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=7:mean_predicted_hours | gallery: 37.9243; notebook: 37.9243 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=7:mean_signed_error | gallery: 10.3700, 10.3700; notebook: 10.3700, 10.3700 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=7:median_predicted_hours | gallery: 39.2908; notebook: 39.2908 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=7:n | gallery: 88; notebook: 88 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=7:share_above | gallery: 98.90%; notebook: 98.90% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=7:share_below | gallery: 1.10%; notebook: 1.10% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=7:weighted_n | gallery: 1.864e+05; notebook: 1.864e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=8:mean_absolute_error | gallery: 3.4795; notebook: 3.4795 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=8:mean_predicted_hours | gallery: 37.4055; notebook: 37.4055 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=8:mean_signed_error | gallery: 0.1202; notebook: 0.1202 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=8:median_predicted_hours | gallery: 35.2430; notebook: 35.2430 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=8:n | gallery: 1,293; notebook: 1,293 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=8:share_below | gallery: 4.27%; notebook: 4.27% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=8:share_inside | gallery: 95.73%; notebook: 95.73% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=8:weighted_n | gallery: 3.011e+06; notebook: 3.011e+06 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=9:mean_absolute_error | gallery: 12.1219; notebook: 12.1219 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=9:mean_predicted_hours | gallery: 37.8462; notebook: 37.8462 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=9:mean_signed_error | gallery: -12.1053; notebook: -12.1053 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=9:median_predicted_hours | gallery: 39.4984; notebook: 39.4984 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=9:n | gallery: 672; notebook: 672 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=9:share_below | gallery: 99.95%; notebook: 99.95% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=9:share_inside | gallery: 0.05%; notebook: 0.05% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/intensive_margin_extended.csv:row=9:weighted_n | gallery: 1.597e+06; notebook: 1.597e+06 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/joint_and_intensive_extended_benchmark_bands.csv:row=109:observed | rehearsal: 100; story: 100 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/joint_and_intensive_extended_benchmark_bands.csv:row=299:simulated_sd | gallery: 0.0894; notebook: 0.0894 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/joint_and_intensive_extended_benchmark_bands.csv:row=381:simulated_p025 | deck: 2 245; rehearsal: 2,245 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/joint_and_intensive_extended_benchmark_bands.csv:row=7:simulated_p975 | gallery: 0.6298; notebook: 0.6298 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/joint_and_intensive_extended_benchmark_bands.csv:row=85:simulated_mean | gallery: 0.0004, 0.0004, 0.0004; notebook: 0.0004, 0.0004, 0.0004 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/joint_and_intensive_extended_benchmark_bands.csv:row=91:simulated_p025 | gallery: 0.0915; notebook: 0.0915 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1014:simulated_mean | gallery: 0.0068; notebook: 0.0068 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1028:simulated_p025 | gallery: 0.7514; notebook: 0.7514 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1054:observed | gallery: 0.4031; notebook: 0.4031 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1056:observed | gallery: 0.0482; notebook: 0.0482 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1059:simulated_p975 | gallery: 0.7680; notebook: 0.7680 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1067:simulated_mean | gallery: 0.0002, 0.0002; notebook: 0.0002, 0.0002 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1067:simulated_p975 | gallery: 0.0010; notebook: 0.0010 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1071:simulated_mean | gallery: 0.0003; notebook: 0.0003 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1071:simulated_p975 | gallery: 0.1001, 0.0010; notebook: 0.1001, 0.0010 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1080:simulated_mean | gallery: 0.1368, 0.1368; notebook: 0.1368, 0.1368 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1156:simulated_mean | deck: 1.96; rehearsal: 1.96 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1172:observed | gallery: 0.0056; notebook: 0.0056 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=1191:simulated_mean | gallery: 0.0775; notebook: 0.0775 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=127:simulated_mean | gallery: 0.2500, 0.2500, 0.2500, 0.2500; notebook: 0.2500, 0.2500, 0.2500, 0.2500 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=128:simulated_mean | gallery: 0.7500, 0.7500, 0.7500, 0.7500, 0.7500; notebook: 0.7500, 0.7500, 0.7500, 0.7500, 0.7500 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=129:simulated_mean | gallery: 0.2500, 0.2500, 0.2500, 0.2500; notebook: 0.2500, 0.2500, 0.2500, 0.2500 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=152:simulated_mean | gallery: 0.9015; notebook: 0.9015 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=152:simulated_p025 | gallery: 0.8869; notebook: 0.8869; story: 88.7, 88.7 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=152:simulated_p975 | gallery: 0.9162; notebook: 0.9162 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=153:observed | gallery: 0.9996, 0.9996; notebook: 0.9996, 0.9996 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=154:simulated_mean | gallery: 0.0023; notebook: 0.0023 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=157:observed | gallery: 0.1016; notebook: 0.1016 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=157:simulated_mean | gallery: 0.0983; notebook: 0.0983 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=157:simulated_p025 | gallery: 0.0837; notebook: 0.0837 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=157:simulated_p975 | gallery: 0.1131; notebook: 0.1131 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=158:simulated_p975 | gallery: 0.0004; notebook: 0.0004 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=159:observed | gallery: 0.8980; notebook: 0.8980 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=159:simulated_mean | gallery: 0.9013; notebook: 0.9013 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=159:simulated_p025 | gallery: 0.8865; notebook: 0.8865 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=159:simulated_p975 | gallery: 0.9159; notebook: 0.9159 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=162:observed | gallery: 0.0301; notebook: 0.0301 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=162:simulated_mean | gallery: 0.1227; notebook: 0.1227 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=162:simulated_p025 | gallery: 0.1052; notebook: 0.1052 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=162:simulated_p975 | gallery: 0.1401; notebook: 0.1401 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=166:observed | gallery: 0.2108; notebook: 0.2108 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=166:simulated_mean | gallery: 0.2121; notebook: 0.2121 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=166:simulated_p975 | gallery: 0.2329; notebook: 0.2329 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=170:observed | gallery: 0.6100; notebook: 0.6100 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=170:simulated_mean | gallery: 0.5201; notebook: 0.5201 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=170:simulated_p025 | gallery: 0.4924; notebook: 0.4924 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=170:simulated_p975 | gallery: 0.5466; notebook: 0.5466 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=174:observed | gallery: 0.1491; notebook: 0.1491 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=174:simulated_mean | gallery: 0.1451; notebook: 0.1451 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=174:simulated_p025 | gallery: 0.1257; notebook: 0.1257 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=174:simulated_p975 | gallery: 0.1644; notebook: 0.1644 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=176:observed | gallery: 0.6100; notebook: 0.6100 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=176:simulated_mean | gallery: 0.5201; notebook: 0.5201 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=176:simulated_p025 | gallery: 0.4924; notebook: 0.4924 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=176:simulated_p975 | gallery: 0.5466; notebook: 0.5466 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=180:observed | gallery: 0.0969; notebook: 0.0969 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=180:simulated_mean | gallery: 0.0789; notebook: 0.0789 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=180:simulated_p975 | gallery: 0.0892; notebook: 0.0892 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=181:simulated_mean | gallery: -0.2592; notebook: -0.2592 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=181:simulated_p025 | gallery: -0.2851; notebook: -0.2851 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=181:simulated_p975 | gallery: -0.2344; notebook: -0.2344 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=182:simulated_mean | gallery: -1.3095; notebook: -1.3095 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=182:simulated_p025 | gallery: -1.3407; notebook: -1.3407 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=182:simulated_p975 | gallery: -1.2782; notebook: -1.2782 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=183:simulated_mean | gallery: -1.4080; notebook: -1.4080 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=183:simulated_p025 | gallery: -1.4403; notebook: -1.4403 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=183:simulated_p975 | gallery: -1.3721; notebook: -1.3721 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=184:simulated_mean | gallery: 0.0985; notebook: 0.0985 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=184:simulated_p975 | gallery: 0.1171; notebook: 0.1171 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=185:observed | gallery: 37.8448; notebook: 37.8448 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=185:simulated_mean | gallery: 0.0203; notebook: 0.0203 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=185:simulated_p025 | gallery: -6.1775; notebook: -6.1775 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=185:simulated_p975 | gallery: 6.1289; notebook: 6.1289 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=186:observed | gallery: -0.0611; notebook: -0.0611 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=186:simulated_p025 | gallery: 0.8194; notebook: 0.8194 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=186:simulated_p975 | gallery: 1.1842; notebook: 1.1842 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=187:observed | gallery: 21.0564; notebook: 21.0564 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=187:simulated_mean | gallery: 19.6424; notebook: 19.6424 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=187:simulated_p025 | gallery: 19.0599; notebook: 19.0599 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=187:simulated_p975 | gallery: 20.3415; notebook: 20.3415 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=188:observed | gallery: 5.6392; notebook: 5.6392 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=188:simulated_mean | gallery: 5.9405; notebook: 5.9405 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=188:simulated_p025 | gallery: 5.3899; notebook: 5.3899 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=188:simulated_p975 | gallery: 6.5145; notebook: 6.5145 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=189:observed | gallery: -3.8765; notebook: -3.8765 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=189:simulated_mean | gallery: -3.0445; notebook: -3.0445 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=189:simulated_p025 | gallery: -3.2904; notebook: -3.2904 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=189:simulated_p975 | gallery: -2.8148; notebook: -2.8148 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=190:observed | gallery: -15.5878; notebook: -15.5878 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=190:simulated_mean | gallery: -14.4241; notebook: -14.4241 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=190:simulated_p025 | gallery: -15.3844; notebook: -15.3844 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=190:simulated_p975 | gallery: -13.5493; notebook: -13.5493 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=191:observed | gallery: -0.0218; notebook: -0.0218 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=191:simulated_mean | gallery: 0.0813; notebook: 0.0813 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=191:simulated_p025 | gallery: 0.0668; notebook: 0.0668 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=191:simulated_p975 | gallery: 0.0956; notebook: 0.0956 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=192:observed | gallery: 2.293e+05; notebook: 2.293e+05 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=192:simulated_mean | gallery: 15.2837; notebook: 15.2837 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=192:simulated_p025 | gallery: 3.4965; notebook: 3.4965 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=192:simulated_p975 | gallery: 46.2097; notebook: 46.2097 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=193:observed | gallery: 191.3088; notebook: 191.3088 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=193:simulated_mean | gallery: 16.4153; notebook: 16.4153 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=193:simulated_p025 | gallery: 5.6108; notebook: 5.6108 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=193:simulated_p975 | gallery: 39.2360; notebook: 39.2360 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=194:observed | gallery: 12.0173; notebook: 12.0173 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=194:simulated_mean | gallery: 15.9576; notebook: 15.9576 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=194:simulated_p025 | gallery: 5.0865; notebook: 5.0865 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=194:simulated_p975 | gallery: 32.3463; notebook: 32.3463 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=195:observed | gallery: 185.6973; notebook: 185.6973 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=195:simulated_mean | gallery: 16.0165; notebook: 16.0165; story: 16 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=195:simulated_p025 | gallery: 4.9749; notebook: 4.9749 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=195:simulated_p975 | gallery: 31.9529; notebook: 31.9529 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=196:observed | gallery: 133.9741; notebook: 133.9741 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=196:simulated_mean | gallery: 16.6563; notebook: 16.6563 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=196:simulated_p025 | gallery: 5.7733; notebook: 5.7733 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=196:simulated_p975 | gallery: 33.5574; notebook: 33.5574 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=197:observed | gallery: 317.1879; notebook: 317.1879 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=197:simulated_mean | gallery: 14.4687; notebook: 14.4687 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=197:simulated_p025 | gallery: 4.4456; notebook: 4.4456 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=197:simulated_p975 | gallery: 29.7085; notebook: 29.7085 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=216:simulated_mean | gallery: 0.1822; notebook: 0.1822 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=21:simulated_mean | gallery: 0.0002; notebook: 0.0002 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=225:simulated_p975 | gallery: 0.1901; notebook: 0.1901 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=252:observed | gallery: 0.8712; notebook: 0.8712 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=252:simulated_mean | gallery: 0.8039; notebook: 0.8039 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=252:simulated_p025 | gallery: 0.7632; notebook: 0.7632 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=252:simulated_p975 | gallery: 0.8420; notebook: 0.8420 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=253:simulated_mean | gallery: 0.9526; notebook: 0.9526 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=253:simulated_p025 | gallery: 0.9347, 0.9347; notebook: 0.9347, 0.9347 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=253:simulated_p975 | gallery: 0.9685; notebook: 0.9685 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=254:simulated_mean | gallery: 0.3033; notebook: 0.3033 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=254:simulated_p025 | deck: 0.238; gallery: 0.2383; notebook: 0.2383 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=254:simulated_p975 | gallery: 0.3668; notebook: 0.3668 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=255:simulated_mean | gallery: 0.6279; notebook: 0.6279 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=255:simulated_p025 | gallery: 0.5875; notebook: 0.5875 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=255:simulated_p975 | gallery: 0.6643; notebook: 0.6643 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=256:simulated_mean | gallery: 0.0690; notebook: 0.0690 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=256:simulated_p025 | gallery: 0.0547; notebook: 0.0547 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=256:simulated_p975 | gallery: 0.0815; notebook: 0.0815 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=257:observed | gallery: 0.0713; notebook: 0.0713 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=257:simulated_mean | gallery: 0.1595; notebook: 0.1595 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=257:simulated_p025 | gallery: 0.1263; notebook: 0.1263 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=257:simulated_p975 | gallery: 0.1966; notebook: 0.1966 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=258:observed | gallery: 0.0575; notebook: 0.0575 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=258:simulated_mean | gallery: 0.0366; notebook: 0.0366 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=258:simulated_p975 | gallery: 0.0510; notebook: 0.0510; story: 5 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=259:observed | gallery: 0.8230; notebook: 0.8230 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=259:simulated_mean | gallery: 0.7349; notebook: 0.7349 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=259:simulated_p025 | gallery: 0.6978; notebook: 0.6978 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=260:simulated_mean | gallery: 0.0026; notebook: 0.0026 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=260:simulated_p975 | gallery: 0.0069; notebook: 0.0069 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=262:observed | gallery: 0.0209; notebook: 0.0209 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=262:simulated_mean | gallery: 0.0701; notebook: 0.0701 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=263:simulated_mean | gallery: 5.869e-06; notebook: 5.869e-06 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=264:observed | gallery: 0.0013; notebook: 0.0013 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=264:simulated_mean | gallery: 0.0026; notebook: 0.0026 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=266:observed | gallery: 0.0603; notebook: 0.0603; paper: 6; rehearsal: 6 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=266:simulated_p025 | gallery: 0.1439; notebook: 0.1439 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=266:simulated_p975 | gallery: 0.2238; notebook: 0.2238 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=268:observed | gallery: 0.0030; notebook: 0.0030 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=268:simulated_mean | gallery: 0.0020; notebook: 0.0020 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=270:observed | gallery: 0.6476; notebook: 0.6476 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=270:simulated_mean | gallery: 0.4617; notebook: 0.4617 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=270:simulated_p025 | gallery: 0.4107; notebook: 0.4107; story: 41 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=272:simulated_mean | gallery: 0.0019; notebook: 0.0019 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=274:observed | gallery: 0.2660; notebook: 0.2660 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=274:simulated_mean | gallery: 0.2760; notebook: 0.2760 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=274:simulated_p025 | gallery: 0.2204; notebook: 0.2204 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=274:simulated_p975 | gallery: 0.3261; notebook: 0.3261 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=275:simulated_mean | gallery: 0.0005; notebook: 0.0005 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=275:simulated_p975 | gallery: 0.0010; notebook: 0.0010 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=276:observed | gallery: 0.6485; notebook: 0.6485 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=276:simulated_mean | gallery: 0.4648; notebook: 0.4648 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=276:simulated_p025 | gallery: 0.4132; notebook: 0.4132 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=276:simulated_p975 | gallery: 0.5200; notebook: 0.5200 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=277:simulated_mean | gallery: 0.2583; notebook: 0.2583 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=277:simulated_p025 | gallery: 0.2473; notebook: 0.2473 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=277:simulated_p975 | gallery: 0.2739; notebook: 0.2739 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=278:simulated_mean | gallery: 0.7517; notebook: 0.7517 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=278:simulated_p025 | gallery: 0.7491; notebook: 0.7491 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=278:simulated_p975 | gallery: 0.7539; notebook: 0.7539 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=279:simulated_mean | gallery: 0.2583; notebook: 0.2583 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=279:simulated_p025 | gallery: 0.2473; notebook: 0.2473 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=279:simulated_p975 | gallery: 0.2739; notebook: 0.2739 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=27:simulated_mean | gallery: 0.2502; notebook: 0.2502 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=280:observed | gallery: 0.1086; notebook: 0.1086 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=280:simulated_p975 | gallery: 0.1571; notebook: 0.1571 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=281:simulated_mean | gallery: -0.4190; notebook: -0.4190 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=281:simulated_p025 | gallery: -0.4705; notebook: -0.4705 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=281:simulated_p975 | gallery: -0.3731; notebook: -0.3731 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=282:simulated_mean | gallery: -1.3389; notebook: -1.3389 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=282:simulated_p025 | gallery: -1.3929; notebook: -1.3929 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=282:simulated_p975 | gallery: -1.2863; notebook: -1.2863 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=283:simulated_mean | gallery: -1.4701; notebook: -1.4701 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=283:simulated_p025 | gallery: -1.5135; notebook: -1.5135 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=283:simulated_p975 | gallery: -1.4248; notebook: -1.4248 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=284:simulated_mean | gallery: 0.1312; notebook: 0.1312 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=284:simulated_p025 | gallery: 0.0930; notebook: 0.0930 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=284:simulated_p975 | gallery: 0.1691; notebook: 0.1691 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=285:observed | gallery: 28.8141; notebook: 28.8141 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=285:simulated_mean | gallery: 0.8180; notebook: 0.8180 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=285:simulated_p025 | gallery: -22.9376; notebook: -22.9376 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=285:simulated_p975 | gallery: 24.8362; notebook: 24.8362 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=286:observed | gallery: 0.2717; notebook: 0.2717 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=286:simulated_mean | gallery: 0.9778; notebook: 0.9778 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=286:simulated_p975 | gallery: 1.6135; notebook: 1.6135 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=287:observed | gallery: 25.0277; notebook: 25.0277 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=287:simulated_mean | gallery: 24.0107; notebook: 24.0107 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=287:simulated_p025 | gallery: 22.4508; notebook: 22.4508 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=287:simulated_p975 | gallery: 25.5803; notebook: 25.5803 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=288:observed | gallery: 11.0835; notebook: 11.0835 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=288:simulated_mean | gallery: 9.8041; notebook: 9.8041 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=288:simulated_p025 | gallery: 8.6062; notebook: 8.6062 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=288:simulated_p975 | gallery: 11.0055; notebook: 11.0055 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=289:observed | gallery: -0.1973; notebook: -0.1973 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=289:simulated_mean | gallery: 0.2748; notebook: 0.2748 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=289:simulated_p025 | gallery: -0.1155; notebook: -0.1155 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=289:simulated_p975 | gallery: 0.6723; notebook: 0.6723 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=28:simulated_mean | gallery: 0.7501, 0.7501; notebook: 0.7501, 0.7501 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=290:observed | gallery: -10.8510; notebook: -10.8510 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=290:simulated_mean | gallery: -13.2307; notebook: -13.2307 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=290:simulated_p025 | gallery: -14.6355; notebook: -14.6355 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=290:simulated_p975 | gallery: -11.7881; notebook: -11.7881 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=291:observed | gallery: 0.0327; notebook: 0.0327 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=291:simulated_mean | gallery: 0.0401; notebook: 0.0401 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=291:simulated_p025 | gallery: 0.0188; notebook: 0.0188 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=292:observed | gallery: 338.7629; notebook: 338.7629 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=292:simulated_mean | gallery: 20.2994; notebook: 20.2994 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=292:simulated_p025 | gallery: 4.5202; notebook: 4.5202 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=292:simulated_p975 | gallery: 40.2418; notebook: 40.2418 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=293:observed | gallery: 51.0006; notebook: 51.0006 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=293:simulated_mean | gallery: 15.7593; notebook: 15.7593 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=293:simulated_p025 | gallery: 4.7329; notebook: 4.7329 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=293:simulated_p975 | gallery: 48.5944; notebook: 48.5944 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=294:observed | gallery: 52.0860; notebook: 52.0860 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=294:simulated_mean | gallery: 16.6393; notebook: 16.6393 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=294:simulated_p025 | gallery: 4.8052; notebook: 4.8052 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=294:simulated_p975 | gallery: 40.6189; notebook: 40.6189 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=295:observed | gallery: 162.1065; notebook: 162.1065 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=295:simulated_mean | gallery: 16.8086; notebook: 16.8086 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=295:simulated_p025 | gallery: 5.4363; notebook: 5.4363 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=295:simulated_p975 | gallery: 34.2931; notebook: 34.2931 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=296:observed | gallery: 17.0014; notebook: 17.0014 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=296:simulated_mean | gallery: 17.6090; notebook: 17.6090 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=296:simulated_p025 | gallery: 5.4512; notebook: 5.4512 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=296:simulated_p975 | gallery: 36.9199; notebook: 36.9199 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=297:observed | gallery: 191.9255; notebook: 191.9255 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=297:simulated_mean | gallery: 15.3481; notebook: 15.3481 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=297:simulated_p025 | gallery: 5.1933; notebook: 5.1933 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=297:simulated_p975 | gallery: 31.7483; notebook: 31.7483 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=29:simulated_mean | gallery: 0.2502; notebook: 0.2502 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=309:simulated_p975 | gallery: 0.8411; notebook: 0.8411 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=318:simulated_sd | gallery: 0.0035; notebook: 0.0035 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=323:simulated_sd | gallery: 0.1219; notebook: 0.1219 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=352:observed | gallery: 0.8548; notebook: 0.8548; rehearsal: 85.5% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=352:simulated_mean | gallery: 0.8373; notebook: 0.8373 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=352:simulated_p025 | gallery: 0.8080; notebook: 0.8080; story: 80.8, 80.8 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=352:simulated_p975 | gallery: 0.8656; notebook: 0.8656; story: 86.6, 86.6 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=353:observed | gallery: 0.9733; notebook: 0.9733 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=353:simulated_mean | gallery: 0.9822; notebook: 0.9822 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=353:simulated_p025 | gallery: 0.9737; notebook: 0.9737 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=353:simulated_p975 | gallery: 0.9904; notebook: 0.9904 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=354:observed | gallery: 0.1014; notebook: 0.1014 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=354:simulated_mean | gallery: 0.1301; notebook: 0.1301 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=354:simulated_p025 | gallery: 0.0885; notebook: 0.0885 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=354:simulated_p975 | gallery: 0.1733; notebook: 0.1733 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=355:simulated_mean | gallery: 0.5562; notebook: 0.5562 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=355:simulated_p025 | gallery: 0.5315; notebook: 0.5315 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=355:simulated_p975 | gallery: 0.5813; notebook: 0.5813 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=356:observed | gallery: 0.0138; notebook: 0.0138 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=356:simulated_mean | gallery: 0.0220; notebook: 0.0220 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=356:simulated_p025 | gallery: 0.0148; notebook: 0.0148 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=357:observed | gallery: 0.1221; notebook: 0.1221 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=357:simulated_mean | gallery: 0.1479; notebook: 0.1479 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=357:simulated_p975 | gallery: 0.1770; notebook: 0.1770 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=358:observed | gallery: 0.0231; notebook: 0.0231 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=358:simulated_mean | gallery: 0.0148; notebook: 0.0148 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=359:simulated_mean | gallery: 0.8152; notebook: 0.8152 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=359:simulated_p025 | gallery: 0.7862; notebook: 0.7862 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=359:simulated_p975 | gallery: 0.8412; notebook: 0.8412 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=360:observed | gallery: 0.0036; notebook: 0.0036 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=360:simulated_mean | gallery: 0.0136; notebook: 0.0136; story: 0.0136 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=360:simulated_p025 | gallery: 0.0067; notebook: 0.0067 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=360:simulated_p975 | gallery: 0.0217; notebook: 0.0217 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=361:simulated_mean | gallery: 0.0034; notebook: 0.0034 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=362:observed | gallery: 0.0294; notebook: 0.0294 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=362:simulated_mean | gallery: 0.1156; notebook: 0.1156 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=362:simulated_p975 | gallery: 0.1478; notebook: 0.1478 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=364:observed | gallery: 0.0108; notebook: 0.0108 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=364:simulated_mean | gallery: 0.0116; notebook: 0.0116 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=364:simulated_p025 | gallery: 0.0053; notebook: 0.0053 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=365:simulated_mean | gallery: 0.0040; notebook: 0.0040 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=365:simulated_p975 | gallery: 0.0094; notebook: 0.0094 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=366:observed | gallery: 0.1645; notebook: 0.1645 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=366:simulated_mean | gallery: 0.2236; notebook: 0.2236 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=366:simulated_p025 | gallery: 0.1849; notebook: 0.1849 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=366:simulated_p975 | gallery: 0.2673; notebook: 0.2673 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=368:observed | gallery: 0.0217; notebook: 0.0217 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=368:simulated_mean | gallery: 0.0093; notebook: 0.0093 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=368:simulated_p975 | gallery: 0.0158; notebook: 0.0158 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=369:observed | gallery: 0.0076; notebook: 0.0076 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=369:simulated_mean | gallery: 0.0036; notebook: 0.0036 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=369:simulated_p975 | gallery: 0.0097; notebook: 0.0097 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=370:observed | gallery: 0.5684; notebook: 0.5684 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=370:simulated_mean | gallery: 0.4241; notebook: 0.4241 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=370:simulated_p025 | gallery: 0.3793; notebook: 0.3793 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=370:simulated_p975 | gallery: 0.4651; notebook: 0.4651 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=372:observed | gallery: 0.0018; notebook: 0.0018 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=372:simulated_mean | gallery: 0.0039; notebook: 0.0039 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=372:simulated_p975 | gallery: 0.0095; notebook: 0.0095 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=373:simulated_mean | gallery: 0.0017; notebook: 0.0017 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=373:simulated_p975 | gallery: 0.0062; notebook: 0.0062 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=374:observed | gallery: 0.1923; notebook: 0.1923 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=374:simulated_mean | gallery: 0.1855; notebook: 0.1855 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=374:simulated_p025 | gallery: 0.1555; notebook: 0.1555 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=376:observed | gallery: 0.5720; notebook: 0.5720 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=376:simulated_mean | gallery: 0.4417; notebook: 0.4417 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=376:simulated_p025 | gallery: 0.3944; notebook: 0.3944 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=376:simulated_p975 | gallery: 0.4841; notebook: 0.4841 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=377:simulated_mean | gallery: 0.2724; notebook: 0.2724 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=377:simulated_p025 | gallery: 0.2564; notebook: 0.2564 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=377:simulated_p975 | gallery: 0.2906; notebook: 0.2906 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=378:simulated_mean | gallery: 0.7569; notebook: 0.7569 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=378:simulated_p975 | gallery: 0.7624; notebook: 0.7624 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=379:simulated_mean | gallery: 0.2724; notebook: 0.2724 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=379:simulated_p025 | gallery: 0.2564; notebook: 0.2564 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=379:simulated_p975 | gallery: 0.2906; notebook: 0.2906 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=380:observed | gallery: 0.1013; notebook: 0.1013 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=380:simulated_mean | gallery: 0.1193; notebook: 0.1193 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=380:simulated_p025 | gallery: 0.1040; notebook: 0.1040 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=381:simulated_mean | gallery: -0.3769; notebook: -0.3769 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=381:simulated_p025 | gallery: -0.4245; notebook: -0.4245 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=381:simulated_p975 | gallery: -0.3361; notebook: -0.3361 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=382:simulated_mean | gallery: -1.4195; notebook: -1.4195 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=382:simulated_p025 | gallery: -1.4657; notebook: -1.4657 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=382:simulated_p975 | gallery: -1.3823; notebook: -1.3823 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=383:simulated_mean | gallery: -1.5216; notebook: -1.5216 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=383:simulated_p025 | gallery: -1.5532; notebook: -1.5532 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=383:simulated_p975 | gallery: -1.4908; notebook: -1.4908 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=384:simulated_mean | gallery: 0.1021; notebook: 0.1021 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=384:simulated_p025 | gallery: 0.0674; notebook: 0.0674 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=384:simulated_p975 | gallery: 0.1317; notebook: 0.1317 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=385:observed | gallery: 16.3323; notebook: 16.3323 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=385:simulated_mean | gallery: -0.1885; notebook: -0.1885 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=385:simulated_p025 | gallery: -13.6268; notebook: -13.6268 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=385:simulated_p975 | gallery: 12.6048; notebook: 12.6048 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=386:observed | gallery: 0.6005; notebook: 0.6005 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=386:simulated_mean | gallery: 1.0055; notebook: 1.0055 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=386:simulated_p975 | gallery: 1.3927; notebook: 1.3927 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=387:observed | gallery: 16.9615; notebook: 16.9615 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=387:simulated_mean | gallery: 20.1700; notebook: 20.1700 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=387:simulated_p025 | gallery: 19.1356; notebook: 19.1356 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=387:simulated_p975 | gallery: 21.3484; notebook: 21.3484 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=388:observed | gallery: 6.5838; notebook: 6.5838 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=388:simulated_mean | gallery: 6.3718; notebook: 6.3718 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=388:simulated_p025 | gallery: 5.4754; notebook: 5.4754 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=388:simulated_p975 | gallery: 7.2210; notebook: 7.2210 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=389:observed | gallery: -3.2783; notebook: -3.2783 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=389:simulated_mean | gallery: -3.0558; notebook: -3.0558 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=389:simulated_p025 | gallery: -3.4426; notebook: -3.4426 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=389:simulated_p975 | gallery: -2.6788; notebook: -2.6788 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=390:observed | gallery: -13.9670; notebook: -13.9670 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=390:simulated_mean | gallery: -14.9508; notebook: -14.9508 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=390:simulated_p025 | gallery: -16.4337; notebook: -16.4337 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=390:simulated_p975 | gallery: -13.6020; notebook: -13.6020 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=391:observed | gallery: 0.0748; notebook: 0.0748 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=391:simulated_mean | gallery: 0.0568; notebook: 0.0568 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=391:simulated_p025 | gallery: 0.0334; notebook: 0.0334 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=392:observed | gallery: 15.9241; notebook: 15.9241 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=392:simulated_mean | gallery: 15.6587; notebook: 15.6587 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=392:simulated_p025 | gallery: 3.7257; notebook: 3.7257 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=392:simulated_p975 | gallery: 34.5707; notebook: 34.5707 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=393:observed | gallery: 62.6536; notebook: 62.6536 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=393:simulated_mean | gallery: 15.0846; notebook: 15.0846 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=393:simulated_p025 | gallery: 5.0601; notebook: 5.0601 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=393:simulated_p975 | gallery: 33.9910; notebook: 33.9910 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=394:observed | gallery: 23.1534; notebook: 23.1534 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=394:simulated_mean | gallery: 14.8844; notebook: 14.8844 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=394:simulated_p025 | gallery: 4.5884; notebook: 4.5884 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=394:simulated_p975 | gallery: 32.2474; notebook: 32.2474 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=395:observed | gallery: 99.7384; notebook: 99.7384 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=395:simulated_mean | gallery: 14.7295; notebook: 14.7295 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=395:simulated_p025 | gallery: 5.1442; notebook: 5.1442 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=395:simulated_p975 | gallery: 31.1769; notebook: 31.1769 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=396:observed | gallery: 11.0857; notebook: 11.0857 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=396:simulated_mean | gallery: 14.6076; notebook: 14.6076 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=396:simulated_p025 | gallery: 5.2139; notebook: 5.2139 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=396:simulated_p975 | gallery: 29.9169; notebook: 29.9169 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=397:observed | gallery: 85.6001; notebook: 85.6001 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=397:simulated_mean | gallery: 13.3917; notebook: 13.3917 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=397:simulated_p025 | gallery: 4.1389; notebook: 4.1389 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=397:simulated_p975 | gallery: 27.0132; notebook: 27.0132 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=425:simulated_mean | gallery: 0.0008; notebook: 0.0008 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=454:observed | gallery: 0.0117; notebook: 0.0117 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=457:observed | gallery: 0.0760; notebook: 0.0760 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=471:simulated_sd | gallery: 0.0289; notebook: 0.0289 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=478:simulated_mean | gallery: 0.7504; notebook: 0.7504 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=504:simulated_p975 | gallery: 0.5155; notebook: 0.5155 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=505:simulated_mean | gallery: 0.5011; notebook: 0.5011 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=506:simulated_mean | gallery: 0.0241; notebook: 0.0241 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=52:observed | gallery: 0.9230; notebook: 0.9230; rehearsal: 92.3% | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=52:simulated_mean | gallery: 0.9063; notebook: 0.9063 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=52:simulated_p025 | gallery: 0.8921; notebook: 0.8921; story: 89.2, 89.2 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=52:simulated_p975 | gallery: 0.9210; notebook: 0.9210; story: 92.1, 92.1 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=536:simulated_mean | gallery: 0.9996; notebook: 0.9996 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=53:observed | gallery: 0.9989; notebook: 0.9989 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=53:simulated_mean | gallery: 0.9990; notebook: 0.9990 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=53:simulated_p025 | gallery: 0.9982; notebook: 0.9982 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=53:simulated_p975 | gallery: 0.9997; notebook: 0.9997 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=54:simulated_mean | gallery: 0.0108; notebook: 0.0108 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=54:simulated_p025 | gallery: 0.0038; notebook: 0.0038 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=54:simulated_p975 | gallery: 0.0183; notebook: 0.0183 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=553:simulated_sd | gallery: 0.0220; notebook: 0.0220 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=554:simulated_p975 | gallery: 0.0046; notebook: 0.0046 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=555:simulated_mean | gallery: 0.5010; notebook: 0.5010 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=555:simulated_p975 | gallery: 0.5023; notebook: 0.5023 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=556:simulated_mean | gallery: 0.0002; notebook: 0.0002 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=55:simulated_mean | gallery: 0.5049; notebook: 0.5049 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=55:simulated_p975 | gallery: 0.5090; notebook: 0.5090 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=56:simulated_mean | gallery: 0.0010; notebook: 0.0010 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=56:simulated_p975 | gallery: 0.0017; notebook: 0.0017 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=57:simulated_mean | gallery: 0.0928; notebook: 0.0928 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=57:simulated_p025 | gallery: 0.0782; notebook: 0.0782 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=57:simulated_p975 | gallery: 0.1070; notebook: 0.1070 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=58:observed | gallery: 0.0011; notebook: 0.0011 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=58:simulated_mean | gallery: 0.0009; notebook: 0.0009 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=58:simulated_p975 | gallery: 0.0016; notebook: 0.0016 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=59:observed | gallery: 0.9221; notebook: 0.9221 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=59:simulated_mean | gallery: 0.9053; notebook: 0.9053 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=59:simulated_p025 | gallery: 0.8911; notebook: 0.8911 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=59:simulated_p975 | gallery: 0.9198; notebook: 0.9198 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=62:observed | gallery: 0.0014; notebook: 0.0014 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=62:simulated_mean | gallery: 0.0781; notebook: 0.0781 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=62:simulated_p025 | gallery: 0.0646; notebook: 0.0646 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=62:simulated_p975 | gallery: 0.0926; notebook: 0.0926 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=630:observed | gallery: 0.1187; notebook: 0.1187 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=653:simulated_mean | paper: 95, 95; rehearsal: 95%; story: 95, 95, 95, 95 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=66:observed | gallery: 0.0388; notebook: 0.0388 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=66:simulated_mean | gallery: 0.1089; notebook: 0.1089 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=66:simulated_p975 | gallery: 0.1272; notebook: 0.1272 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=670:simulated_mean | notebook: 47; rehearsal: 47; story: 47 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=67:simulated_mean | gallery: 4.795e-06; notebook: 4.795e-06 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=6:simulated_p025 | gallery: 0.0009; notebook: 0.0009 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=6:simulated_sd | gallery: 0.0618; notebook: 0.0618 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=70:observed | gallery: 0.6271; notebook: 0.6271 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=70:simulated_mean | gallery: 0.5608; notebook: 0.5608 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=70:simulated_p025 | gallery: 0.5332; notebook: 0.5332 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=71:simulated_mean | gallery: 6.585e-05, 0.0066; notebook: 6.585e-05, 0.0066 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=745:simulated_mean | gallery: 1,000, 1,000, 1,000; paper: 10; story: 10, 1,000, 1,000, 1,000, 1,000 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=74:observed | gallery: 0.3325; notebook: 0.3325 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=74:simulated_mean | gallery: 0.2520; notebook: 0.2520 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=74:simulated_p025 | gallery: 0.2273; notebook: 0.2273 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=74:simulated_p975 | gallery: 0.2759; notebook: 0.2759 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=75:simulated_mean | gallery: 0.0001; notebook: 0.0001 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=75:simulated_sd | gallery: 0.0085; notebook: 0.0085 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=768:simulated_sd | gallery: 0.0442; notebook: 0.0442 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=76:observed | gallery: 0.6273; notebook: 0.6273 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=76:simulated_mean | gallery: 0.5609; notebook: 0.5609 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=76:simulated_p025 | gallery: 0.5333; notebook: 0.5333 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=806:simulated_mean | gallery: 0.3332; notebook: 0.3332 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=80:simulated_mean | gallery: 0.0731; notebook: 0.0731 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=80:simulated_p025 | gallery: 0.0646; notebook: 0.0646 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=81:simulated_mean | gallery: -0.2399; notebook: -0.2399 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=81:simulated_p025 | gallery: -0.2669; notebook: -0.2669 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=81:simulated_p975 | gallery: -0.2164; notebook: -0.2164 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=825:simulated_mean | gallery: 0.0002, 0.0002; notebook: 0.0002, 0.0002 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=827:simulated_mean | gallery: 0.2501, 0.2501; notebook: 0.2501, 0.2501 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=829:simulated_mean | gallery: 0.2501, 0.2501; notebook: 0.2501, 0.2501 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=82:simulated_mean | gallery: -1.2078; notebook: -1.2078 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=82:simulated_p025 | gallery: -1.2465; notebook: -1.2465 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=82:simulated_p975 | gallery: -1.1717; notebook: -1.1717 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=83:simulated_mean | gallery: -1.3178; notebook: -1.3178 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=83:simulated_p025 | gallery: -1.3555; notebook: -1.3555 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=83:simulated_p975 | gallery: -1.2785; notebook: -1.2785 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=84:simulated_mean | gallery: 0.1100; notebook: 0.1100 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=84:simulated_p025 | gallery: 0.0885; notebook: 0.0885 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=84:simulated_p975 | gallery: 0.1318; notebook: 0.1318 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=85:observed | gallery: 40.4346; notebook: 40.4346 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=85:simulated_mean | gallery: 0.0368; notebook: 0.0368; paper: 0.0368 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=85:simulated_p025 | gallery: -7.7919; notebook: -7.7919 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=85:simulated_p975 | gallery: 7.6146; notebook: 7.6146 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=86:observed | gallery: 0.0173; notebook: 0.0173 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=86:simulated_mean | gallery: 0.9990; notebook: 0.9990 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=86:simulated_p025 | gallery: 0.8115; notebook: 0.8115 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=86:simulated_p975 | gallery: 1.2024; notebook: 1.2024 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=878:simulated_p025 | gallery: 0.7499; notebook: 0.7499 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=878:simulated_sd | gallery: 0.0079; notebook: 0.0079 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=87:observed | gallery: 26.2186; notebook: 26.2186 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=87:simulated_mean | gallery: 23.8216; notebook: 23.8216 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=87:simulated_p025 | gallery: 22.9875; notebook: 22.9875 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=87:simulated_p975 | gallery: 24.5773; notebook: 24.5773 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=88:observed | gallery: 10.3700; notebook: 10.3700 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=88:simulated_mean | gallery: 10.0165; notebook: 10.0165 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=88:simulated_p025 | gallery: 9.2478; notebook: 9.2478 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=89:observed | gallery: 0.1202; notebook: 0.1202 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=89:simulated_mean | gallery: 0.8161; notebook: 0.8161 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=89:simulated_p025 | gallery: 0.5820; notebook: 0.5820 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=89:simulated_p975 | gallery: 1.0679; notebook: 1.0679 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=908:simulated_mean | gallery: 0.0002, 0.0002; notebook: 0.0002, 0.0002 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=90:observed | gallery: -12.1053; notebook: -12.1053 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=90:simulated_mean | gallery: -13.5258; notebook: -13.5258 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=90:simulated_p025 | gallery: -14.3219; notebook: -14.3219 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=90:simulated_p975 | gallery: -12.7247; notebook: -12.7247 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=91:observed | gallery: 0.0023; notebook: 0.0023 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=91:simulated_mean | gallery: 0.0933; notebook: 0.0933 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=91:simulated_p025 | gallery: 0.0777; notebook: 0.0777 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=91:simulated_p975 | gallery: 0.1064; notebook: 0.1064 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=92:simulated_mean | gallery: 14.0734; notebook: 14.0734 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=92:simulated_p025 | gallery: 3.7676; notebook: 3.7676 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=92:simulated_p975 | gallery: 42.1498; notebook: 42.1498 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=930:simulated_mean | gallery: 0.0766; notebook: 0.0766 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=93:observed | gallery: 171.0562; notebook: 171.0562 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=93:simulated_mean | gallery: 15.9497; notebook: 15.9497 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=93:simulated_p025 | gallery: 5.2910; notebook: 5.2910 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=93:simulated_p975 | gallery: 38.6941; notebook: 38.6941 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=948:simulated_p025 | gallery: 0.0696; notebook: 0.0696 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=94:observed | gallery: 102.5397; notebook: 102.5397 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=94:simulated_mean | gallery: 15.8014; notebook: 15.8014 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=94:simulated_p025 | gallery: 5.1972; notebook: 5.1972; paper: 5.2 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=94:simulated_p975 | gallery: 32.5667; notebook: 32.5667 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=953:simulated_mean | gallery: 0.9998; notebook: 0.9998 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=958:simulated_mean | gallery: 0.0181; notebook: 0.0181 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=95:observed | gallery: 151.8711; notebook: 151.8711 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=95:simulated_mean | gallery: 16.2198; notebook: 16.2198 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=95:simulated_p025 | gallery: 5.1072; notebook: 5.1072 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=95:simulated_p975 | gallery: 33.3899; notebook: 33.3899 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=96:observed | gallery: 250.8451; notebook: 250.8451 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=96:simulated_mean | gallery: 16.3403; notebook: 16.3403 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=96:simulated_p025 | gallery: 5.2365; notebook: 5.2365 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=96:simulated_p975 | gallery: 34.2078; notebook: 34.2078 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=97:observed | gallery: 416.9722; notebook: 416.9722 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=97:simulated_mean | gallery: 14.8150; notebook: 14.8150 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=97:simulated_p025 | gallery: 4.3498; notebook: 4.3498 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=97:simulated_p975 | gallery: 29.9596; notebook: 29.9596 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/model_simulated_bands.csv:row=984:simulated_p025 | gallery: 0.0771; notebook: 0.0771; paper: 0.0771; story: 0.0771 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/participation_reliability.csv:row=16:probability_decile | gallery: 500; notebook: 500; story: 500 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/participation_reliability.csv:row=32:mean_predicted_p_work | gallery: 70, 70, 70, 70; notebook: 70, 70, 70, 70 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/pit.csv:row=42:count_or_normalized_weight | notebook: 41; rehearsal: 41 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/reliability.csv:row=173:mean_predicted_probability | gallery: 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5; notebook: 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/reliability.csv:row=266:mean_predicted_probability | gallery: 4; notebook: 4 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/reliability.csv:row=318:mean_predicted_probability | gallery: 10.9568; notebook: 10.9568 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/run_provenance.json:objectives.couples | notebook: 10283.034369; story: 10283.034 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/run_provenance.json:objectives.singles | notebook: 6253.463074; story: 6253.463, 6253.463 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/s12_unsupported_cases_all_and_supported_only.csv:row=4:s12c_classified_unrepresented_finite_panel_region | gallery: 5; story: 5 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=3:log_score_skill | gallery: -0.2301; notebook: -0.2301 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=3:multinomial_log_score | gallery: -1.2342; notebook: -1.2342 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=3:multinomial_log_score_null | gallery: -1.0041; notebook: -1.0041 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=3:participation_log_score | gallery: -0.3756; notebook: -0.3756 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=5:log_score_skill | gallery: -0.2742; notebook: -0.2742 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=5:multinomial_log_score | gallery: -1.5181; notebook: -1.5181 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=5:multinomial_log_score_null | gallery: -1.2439; notebook: -1.2439 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=5:participation_log_score | gallery: -0.5205; notebook: -0.5205 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=7:log_score_skill | gallery: -0.1036; notebook: -0.1036 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=7:multinomial_log_score | gallery: -1.2486; notebook: -1.2486 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=7:multinomial_log_score_null | gallery: -1.1450; notebook: -1.1450 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=7:participation_log_score | gallery: -0.3691; notebook: -0.3691 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=9:log_score_skill | gallery: -0.0045; notebook: -0.0045 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=9:multinomial_log_score | gallery: -1.3037; notebook: -1.3037 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=9:multinomial_log_score_null | gallery: -1.2992; notebook: -1.2992 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores.csv:row=9:participation_log_score | gallery: -0.3348; notebook: -0.3348 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=10:observed | gallery: 0.0766; notebook: 0.0766 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=10:simulated_mean | gallery: 0.0731; notebook: 0.0731 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=10:simulated_p025 | gallery: 0.0646; notebook: 0.0646 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=10:simulated_p975 | gallery: 0.0824; notebook: 0.0824 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=11:observed | gallery: -0.3756; notebook: -0.3756 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=11:simulated_mean | gallery: -0.2399; notebook: -0.2399 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=11:simulated_p025 | gallery: -0.2669; notebook: -0.2669 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=11:simulated_p975 | gallery: -0.2164; notebook: -0.2164 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=12:observed | gallery: -1.2342; notebook: -1.2342 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=12:simulated_mean | gallery: -1.2078; notebook: -1.2078 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=12:simulated_p025 | gallery: -1.2465; notebook: -1.2465 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=12:simulated_p975 | gallery: -1.1717; notebook: -1.1717 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=13:observed | gallery: -0.2301; notebook: -0.2301 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=13:simulated_mean | gallery: 0.1100; notebook: 0.1100 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=13:simulated_p025 | gallery: 0.0885; notebook: 0.0885 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=13:simulated_p975 | gallery: 0.1318; notebook: 0.1318 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=26:observed | gallery: 0.0969; notebook: 0.0969 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=26:simulated_mean | gallery: 0.0789; notebook: 0.0789 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=26:simulated_p025 | gallery: 0.0696; notebook: 0.0696 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=26:simulated_p975 | gallery: 0.0892; notebook: 0.0892 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=27:observed | gallery: -0.5205; notebook: -0.5205 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=27:simulated_mean | gallery: -0.2592; notebook: -0.2592 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=27:simulated_p025 | gallery: -0.2851; notebook: -0.2851 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=27:simulated_p975 | gallery: -0.2344; notebook: -0.2344 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=28:observed | gallery: -1.5181; notebook: -1.5181 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=28:simulated_mean | gallery: -1.3095; notebook: -1.3095 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=28:simulated_p025 | gallery: -1.3407; notebook: -1.3407 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=28:simulated_p975 | gallery: -1.2782; notebook: -1.2782 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=29:observed | gallery: -0.2742; notebook: -0.2742 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=29:simulated_mean | gallery: 0.0985; notebook: 0.0985 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=29:simulated_p025 | gallery: 0.0771; notebook: 0.0771 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=29:simulated_p975 | gallery: 0.1171; notebook: 0.1171 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=42:observed | gallery: 0.1086; notebook: 0.1086 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=42:simulated_mean | gallery: 0.1368; notebook: 0.1368 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=42:simulated_p025 | gallery: 0.1187; notebook: 0.1187 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=42:simulated_p975 | gallery: 0.1571; notebook: 0.1571 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=43:observed | gallery: -0.3691; notebook: -0.3691 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=43:simulated_mean | gallery: -0.4190; notebook: -0.4190 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=43:simulated_p025 | gallery: -0.4705; notebook: -0.4705 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=43:simulated_p975 | gallery: -0.3731; notebook: -0.3731 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=44:observed | gallery: -1.2486; notebook: -1.2486 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=44:simulated_mean | gallery: -1.3389; notebook: -1.3389 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=44:simulated_p025 | gallery: -1.3929; notebook: -1.3929 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=44:simulated_p975 | gallery: -1.2863; notebook: -1.2863 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=45:observed | gallery: -0.1036; notebook: -0.1036 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=45:simulated_mean | gallery: 0.1312; notebook: 0.1312 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=45:simulated_p025 | gallery: 0.0930; notebook: 0.0930 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=45:simulated_p975 | gallery: 0.1691; notebook: 0.1691 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=58:observed | gallery: 0.1013; notebook: 0.1013 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=58:simulated_mean | gallery: 0.1193; notebook: 0.1193 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=58:simulated_p025 | gallery: 0.1040; notebook: 0.1040 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=58:simulated_p975 | gallery: 0.1368; notebook: 0.1368 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=59:observed | gallery: -0.3348; notebook: -0.3348 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=59:simulated_mean | gallery: -0.3769; notebook: -0.3769 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=59:simulated_p025 | gallery: -0.4245; notebook: -0.4245 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=59:simulated_p975 | gallery: -0.3361; notebook: -0.3361 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=60:observed | gallery: -1.3037; notebook: -1.3037 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=60:simulated_mean | gallery: -1.4195; notebook: -1.4195 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=60:simulated_p025 | gallery: -1.4657; notebook: -1.4657 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=60:simulated_p975 | gallery: -1.3823; notebook: -1.3823 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=61:observed | gallery: -0.0045; notebook: -0.0045 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=61:simulated_mean | gallery: 0.1021; notebook: 0.1021 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=61:simulated_p025 | gallery: 0.0674; notebook: 0.0674 | PASS |
| POSFIT:MNL_posfit/outputs/positive_fit_diagnostics_v3/scores_with_mcse.csv:row=61:simulated_p975 | gallery: 0.1317; notebook: 0.1317 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=10:estimate | gallery: -1.6863; notebook: -1.6863; paper: -1.68631; story: -1.6863, -1.68631 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=10:se_robust_CR1 | gallery: 0.2458; notebook: 0.2458; paper: 0.245846; story: 0.2458, 25, 0.245846, 25, 25 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=10:upper_bound | paper: 0.95; rehearsal: 95%; story: 0.95, 0.95, 0.95, 0.95 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=10:z_robust | paper: -6.859; story: -6.859 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=11:estimate | gallery: -2.1233; notebook: -2.1233; paper: -2.12326; story: -2.1233, -2.12326 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=11:se_robust_CR1 | gallery: 0.3195; notebook: 0.3195; paper: 0.319457; story: 0.3195, 0.319457 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=11:z_robust | paper: -6.646; story: -6.646 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=12:estimate | gallery: -2.8148; notebook: -2.8148; paper: -2.81476; story: -2.8148, -2.81476 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=12:se_robust_CR1 | gallery: 0.3021; notebook: 0.3021; paper: 0.302078; story: 0.3021, 0.302078, 0.3 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=12:z_robust | paper: -9.318; story: -9.318 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=13:estimate | gallery: -1.1094; notebook: -1.1094; paper: -1.10936; story: -1.1094, -1.10936 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=13:lower_bound | paper: -10; story: -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=13:se_robust_CR1 | gallery: 0.3791; notebook: 0.3791; paper: 0.379086; story: 0.3791, 0.379086 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=13:z_robust | paper: -2.926; story: -2.926 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=14:estimate | gallery: -0.5173; notebook: -0.5173; paper: -0.517276; story: -0.5173, -0.517276 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=14:se_robust_CR1 | gallery: 0.1629; notebook: 0.1629; paper: 0.162932; story: 0.1629, 0.162932 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=14:z_robust | paper: -3.175; story: -3.175 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=15:estimate | gallery: 0.0835; notebook: 0.0835; paper: 0.0835202; story: 8, 8, 0.0835, 0.0835202 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=15:se_robust_CR1 | gallery: 0.2378; notebook: 0.2378; paper: 0.237788; story: 0.2378, 0.237788 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=15:z_robust | paper: 0.351; story: 0.351 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=16:estimate | gallery: 1.1586; notebook: 1.1586; paper: 1.15858; story: 1.1586, 1.15858 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=16:se_robust_CR1 | gallery: 0.1214; notebook: 0.1214; paper: 0.121438; story: 0.1214, 0.121438 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=16:z_robust | paper: 9.541; story: 9.541 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=17:estimate | gallery: 2.2888; notebook: 2.2888; paper: 2.2888; story: 2.2888, 2.2888 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=17:se_robust_CR1 | gallery: 0.0821; notebook: 0.0821; paper: 0.0821348; story: 0.0821, 0.0821348 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=17:z_robust | paper: 27.866; story: 27.866 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=18:estimate | gallery: 2.0284; notebook: 2.0284; paper: 2.02835; story: 2.0284, 2.02835 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=18:se_robust_CR1 | gallery: 0.0682; notebook: 0.0682; paper: 0.0682392; story: 0.0682, 0.0682392 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=18:z_robust | paper: 29.724; story: 29.724 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=19:estimate | gallery: 2.3801; notebook: 2.3801; paper: 2.38012; story: 2.3801, 2.38012 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=19:se_robust_CR1 | gallery: 0.0866; notebook: 0.0866; paper: 0.0865569; story: 0.0866, 0.0865569 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=19:z_robust | paper: 27.498; story: 27.498 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=20:estimate | gallery: 1.6825; notebook: 1.6825; paper: 1.68251; story: 1.6825, 1.68251 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=20:se_robust_CR1 | gallery: 0.0798; notebook: 0.0798; paper: 0.0798241; story: 0.0798, 0.0798241 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=20:z_robust | paper: 21.078; story: 21.078 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=21:estimate | gallery: 0.6977; notebook: 0.6977; paper: 0.69767; story: 0.6977, 0.69767 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=21:se_robust_CR1 | gallery: 0.1335; paper: 0.133487; story: 0.133487 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=21:z_robust | paper: 5.226; story: 5.226 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=22:estimate | gallery: -0.3109; notebook: -0.3109; paper: -0.310873; story: -0.3109, -0.310873 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=22:se_robust_CR1 | gallery: 0.1615; notebook: 0.1615; paper: 0.161533; story: 0.1615, 0.161533 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=22:z_robust | paper: -1.925; story: -1.925 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=23:estimate | gallery: -1.1924; notebook: -1.1924; paper: -1.19243; story: -1.1924, -1.19243 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=23:se_robust_CR1 | gallery: 0.1557; notebook: 0.1557; paper: 0.155667; story: 0.1557, 0.155667 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=23:z_robust | paper: -7.660; story: -7.660 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=24:estimate | gallery: -0.1546; notebook: -0.1546; paper: -0.154617; story: -0.1546, -0.154617 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=24:se_robust_CR1 | gallery: 0.2442; notebook: 0.2442; paper: 0.24423; story: 0.2442, 0.24423 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=24:z_robust | paper: -0.633; story: -0.633 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=25:estimate | gallery: 0.0873; notebook: 0.0873; paper: 0.0872501; story: 0.0873, 0.0872501 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=25:se_robust_CR1 | gallery: 0.2808; notebook: 0.2808; paper: 0.280833; story: 0.2808, 0.280833 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=25:z_robust | paper: 0.311; story: 0.311 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=26:estimate | gallery: 0.0150; notebook: 0.0150; paper: 0.0150136; story: 0.0150, 0.0150136 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=26:se_robust_CR1 | gallery: 0.3068; notebook: 0.3068; paper: 0.306753; story: 0.3068, 0.306753 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=26:z_robust | paper: 0.049; story: 0.049 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=27:estimate | gallery: -0.1455; notebook: -0.1455; paper: -0.145472; story: -0.1455, -15, -15, -15, -15, -15, -15, -0.145472, -15, -15, -15, -15, -15, -15 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=27:se_robust_CR1 | gallery: 0.2555; notebook: 0.2555; paper: 0.255453; story: 0.2555, 0.255453 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=27:z_robust | paper: -0.569; story: -0.569 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=28:estimate | gallery: -0.2844; notebook: -0.2844; paper: -0.284391; story: -0.2844, -0.284391 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=28:se_robust_CR1 | gallery: 0.2748; notebook: 0.2748; paper: 0.274814; story: 0.2748, 0.274814 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=28:z_robust | paper: -1.035; story: -1.035 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=29:estimate | gallery: -0.1396; notebook: -0.1396; paper: -0.139569; story: -0.1396, -0.139569 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=29:se_robust_CR1 | gallery: 0.2651; notebook: 0.2651; paper: 0.265133; story: 0.2651, 0.265133 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=29:z_robust | paper: -0.526; story: -0.526 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=2:estimate | gallery: 3.9814; notebook: 3.9814; paper: 3.98136; story: 3.9814, 3.98136 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=2:se_robust_CR1 | gallery: 0.7466; notebook: 0.7466; paper: 0.746569; story: 0.7466, 0.746569 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=2:upper_bound | paper: 50; story: 50, 50, 50, 50, 50, 50 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=2:z_robust | paper: 5.333; story: 5.333 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=30:estimate | gallery: -0.1659; notebook: -0.1659; paper: -0.165927; story: -0.1659, -0.165927 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=30:se_robust_CR1 | gallery: 0.2660; notebook: 0.2660; paper: 0.26603; story: 0.2660, 0.26603 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=30:z_robust | paper: -0.624; story: -0.624 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=31:estimate | gallery: -0.1823; notebook: -0.1823; paper: -0.182322; story: -0.1823, -0.182322 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=31:se_robust_CR1 | gallery: 0.1657; notebook: 0.1657; paper: 0.165665; story: 0.1657, 0.165665 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=31:z_robust | paper: -1.101; story: -1.101 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=32:estimate | gallery: -0.4174; notebook: -0.4174; paper: -0.417356; story: -0.4174, -0.417356 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=32:se_robust_CR1 | gallery: 0.1861; notebook: 0.1861; paper: 0.1861; story: 0.1861, 0.1861 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=32:z_robust | paper: -2.243; story: -2.243 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=33:estimate | gallery: -1.5097; notebook: -1.5097; paper: -1.50975; story: -1.5097, -1.50975 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=33:se_robust_CR1 | gallery: 0.0967; notebook: 0.0967; paper: 0.0967347; story: 0.0967, 0.0967347 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=33:z_robust | paper: -15.607; story: -15.607 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=34:estimate | gallery: -2.2532; notebook: -2.2532; paper: -2.25319; story: -2.2532, -2.25319 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=34:se_robust_CR1 | gallery: 0.1244; notebook: 0.1244; paper: 0.124405; story: 0.1244, 0.124405 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=34:z_robust | paper: -18.112; story: -18.112 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=35:estimate | gallery: 0.1594; notebook: 0.1594; paper: 0.159368; story: 0.1594, 0.159368 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=35:se_robust_CR1 | gallery: 0.0618; notebook: 0.0618; paper: 0.061796; story: 0.0618, 0.061796 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=35:z_robust | paper: 2.579; story: 2.579 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=36:estimate | gallery: 0.2074; notebook: 0.2074; paper: 0.207379; story: 0.2074, 0.207379 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=36:se_robust_CR1 | gallery: 0.0891; notebook: 0.0891; paper: 0.0891054; story: 0.0891, 0.0891054 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=36:z_robust | paper: 2.327; story: 2.327 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=37:estimate | gallery: -0.1804; notebook: -0.1804; paper: -0.180381; story: -0.1804, -0.180381 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=37:se_robust_CR1 | gallery: 0.0923; notebook: 0.0923; paper: 0.0923137; story: 0.0923, 0.0923137 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=37:z_robust | paper: -1.954; story: -1.954 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=38:estimate | gallery: 0.8159; notebook: 0.8159; paper: 0.81589; story: 0.8159, 0.81589 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=38:se_robust_CR1 | gallery: 0.0799; notebook: 8, 8, 0.0799; paper: 0.079925; story: 0.0799, 0.079925 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=38:z_robust | paper: 10.208; story: 10.208 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=39:estimate | gallery: 2.0480; notebook: 2.0480; paper: 2.048; story: 2.0480, 2.048 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=39:se_robust_CR1 | paper: 0.0335421; story: 0.0335421 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=39:z_robust | paper: 61.058; story: 61.058 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=3:estimate | gallery: -0.0080; notebook: -0.0080; paper: -0.00799228; story: -0.0080, -0.00799228 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=3:lower_bound | paper: -5; story: -5, -5, -5, -5, -5, -5, -5, -5, -5, -5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=3:se_robust_CR1 | notebook: 0.0287; paper: 0.0287174; story: 0.0287, 0.0287174 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=3:z_robust | paper: -0.278; story: -0.278 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=40:estimate | gallery: -0.0433; notebook: -0.0433; paper: -0.0433046; story: -0.0433, -4, -4, -4, -0.0433046, -4, -4, -4 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=40:se_robust_CR1 | gallery: 0.0217; notebook: 0.0217; paper: 0.0216643; story: 0.0217, 0.0216643 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=40:z_robust | paper: -1.999; story: -1.999 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=41:estimate | gallery: 0.1817; notebook: 0.1817; paper: 0.181652; story: 0.1817, 0.181652 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=41:se_robust_CR1 | gallery: 0.0197; notebook: 0.0197; paper: 0.0197059; story: 0.0197, 0.0197059 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=41:z_robust | paper: 9.218; story: 9.218 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=42:estimate | gallery: 0.5643; notebook: 0.5643; paper: 0.56435; story: 0.5643, 0.56435 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=42:se_robust_CR1 | gallery: 0.0546; notebook: 0.0546; paper: 0.0545928; story: 0.0546, 0.05, 0.05, 0.05, 0.05, 0.0545928, 0.05 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=42:z_robust | paper: 10.337; story: 10.337 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=43:estimate | gallery: -0.1598; notebook: -0.1598; paper: -0.15983; story: -0.1598, -0.15983 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=43:se_robust_CR1 | gallery: 0.0243; paper: 0.0242888; story: 0.0242888 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=43:z_robust | paper: -6.580; story: -6.580 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=44:estimate | gallery: 0.3631; paper: 0.363075; story: 0.363075 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=44:se_robust_CR1 | gallery: 0.0072; paper: 0.0072235; story: 0.0072235 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=44:z_robust | paper: 50.263; story: 50.263 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=45:estimate | gallery: -0.0740; notebook: -0.0740; paper: -0.0740, -0.0740322; story: -0.0740, -0.0740322 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=45:se_robust_CR1 | gallery: 0.0231; notebook: 0.0231; paper: 0.0231318; story: 0.0231, 0.0231318 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=45:z_robust | paper: -3.200; story: -3.200 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=46:estimate | gallery: 0.0394; notebook: 0.0394; paper: 0.0393566; story: 0.0394, 0.0393566 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=46:se_robust_CR1 | paper: 0.0228, 0.0228; story: 0.0228 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=46:z_robust | paper: 1.726; story: 1.726 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=47:estimate | gallery: 0.2146; notebook: 0.2146; paper: 0.2146, 0.214559; story: 21.5, 0.2146, 0.214559 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=47:se_robust_CR1 | gallery: 0.0223; notebook: 0.0223; paper: 0.0223344; story: 0.0223, 0.0223344 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=47:z_robust | paper: 9.607; story: 9.607 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=48:estimate | gallery: 2.1017; notebook: 2.1017, 2.1017; paper: 2.1017, 2.10172; story: 2.1017, 2.1017, 2.1017, 2.10172, 2.1017, 2.1017 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=48:se_robust_CR1 | gallery: 0.2939; notebook: 0.2939, 0.2939; paper: 0.2939, 0.293879; story: 0.2939, 0.2939, 0.2939, 0.293879, 0.2939 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=48:z_robust | paper: 7.152; story: 7.152 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=4:estimate | gallery: 0.0065; notebook: 0.0065; paper: 0.00648336; story: 0.0065, 0.00648336 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=4:se_robust_CR1 | gallery: 0.0030; paper: 0.00297388; story: 0.00297388 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=4:z_robust | paper: 2.180; story: 2.180 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=5:estimate | gallery: -0.9761; notebook: -0.9761; paper: -0.976109; story: -0.9761, -0.976109 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=5:se_robust_CR1 | gallery: 0.1357; notebook: 0.1357; paper: 0.135663; story: 0.1357, 0.135663 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=5:z_robust | paper: -7.195; story: -7.195 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=6:estimate | gallery: 13.10; notebook: 13.1029; paper: 13.1029; story: 13.1029, 13.1029 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=6:se_robust_CR1 | gallery: 4.7760; notebook: 4.7760; paper: 4.77604; story: 4.7760, 5, 5, 5, 5, 5, 5, 4.77604, 5, 5, 5, 5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=6:z_robust | paper: 2.743; story: 2.743 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=7:estimate | gallery: -0.1228; notebook: -0.1228; paper: -0.122813; story: -0.1228, -0.122813 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=7:se_robust_CR1 | gallery: 0.1260; notebook: 0.1260; paper: 0.126048; story: 0.1260, 0.126048 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=7:z_robust | paper: -0.974; story: -0.974 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=8:estimate | gallery: 0.0073; notebook: 0.0073; paper: 0.00730709; story: 0.0073, 0.00730709 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=8:se_robust_CR1 | gallery: 0.0103; notebook: 0.0103; paper: 0.0102503; story: 0.0103, 0.0102503 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=8:z_robust | paper: 0.713; story: 0.713 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=9:estimate | gallery: -0.3055; notebook: -0.3055; paper: -0.305471; story: -0.3055, -0.305471, -0.3 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=9:se_robust_CR1 | gallery: 1.1472; notebook: 1.1472; paper: 1.14719; story: 1.1472, 1.14719 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv:row=9:z_robust | paper: -0.266; story: -0.266 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=12:observed | notebook: 7, 7; story: 7, 7 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=20:predicted | notebook: 0.1335; story: 0.1335 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=22:observed | notebook: 0.0243; story: 0.0243 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=24:observed | notebook: 6, 6; rehearsal: 6; story: 6, 6 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=25:observed | notebook: 3, 3, 3, 3; story: 3, 3, 3, 3 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=26:predicted | notebook: 4, 4, 4; story: 4, 4, 4 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=29:observed | notebook: 5, 5; story: 5, 5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=31:absolute_error | notebook: 0.3631; story: 0.3631 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=40:absolute_error | gallery: 0.0228; notebook: 0.0228; story: 0.0228 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=45:observed | notebook: 0.3274; story: 0.3274 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=49:predicted | notebook: 4; story: 4 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=54:predicted | gallery: 0.0335; notebook: 0.0335; story: 0.0335 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=5:predicted | notebook: 2, 2, 2, 2; story: 2, 2, 2, 2 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=65:predicted | notebook: 0.0894; story: 0.0894 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv:row=95:absolute_error | notebook: 0.0372; story: 0.0372 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=10:estimate | gallery: -0.9274; notebook: -0.9274; paper: -0.927353; story: -0.9274, -0.927353 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=10:se_robust_CR1 | gallery: 0.2161; notebook: 0.2161; paper: 0.216128; story: 0.2161, 0.216128 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=10:z_robust | paper: -4.291; story: -4.291 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=12:estimate | paper: 1e-06; story: 1e-06 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=20:estimate | gallery: -3.1735; notebook: -3.1735; paper: -3.17353; story: -3.1735, -3.17353 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=20:se_robust_CR1 | gallery: 0.4053; notebook: 0.4053; paper: 0.405337; story: 0.4053, 0.405337 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=20:z_robust | paper: -7.829; story: -7.829 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=21:estimate | gallery: 0.0298; paper: 0.0297672; story: 0.0298, 0.0297672, 3 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=21:se_robust_CR1 | gallery: 0.1972; notebook: 0.1972; paper: 0.197247; story: 0.1972, 0.197247 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=21:z_robust | paper: 0.151; story: 0.151 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=22:estimate | gallery: 0.7080; notebook: 0.7080; paper: 0.707971; story: 0.7080, 0.707971 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=22:se_robust_CR1 | gallery: 0.1928; notebook: 0.1928; paper: 0.192788; story: 0.1928, 0.192788 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=22:z_robust | paper: 3.672; story: 3.672 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=23:estimate | gallery: 1.9387; notebook: 1.9387; paper: 1.93873; story: 1.9387, 1.93873 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=23:se_robust_CR1 | gallery: 0.0997; notebook: 0.0997; paper: 0.0996968; story: 0.0997, 10, 10, 0.0996968, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0.1, 0.1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0.1 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=23:z_robust | paper: 19.446; story: 19.446 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=24:estimate | gallery: -0.0834; notebook: -0.0834; paper: -0.0833752; story: -0.0834, -8, -8, -0.0833752, -8, -8 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=24:se_robust_CR1 | gallery: 0.1772; notebook: 0.1772; paper: 0.177201; story: 0.1772, 0.177201 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=24:z_robust | paper: -0.471; story: -0.471 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=25:se_robust_CR1 | gallery: 0.2356; notebook: 0.2356; paper: 0.235591; story: 0.2356, 0.235591 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=25:z_robust | paper: -6.122; story: -6.122 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=26:estimate | gallery: -0.3780; notebook: -0.3780; paper: -0.377963; story: -0.3780, -0.377963 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=26:se_robust_CR1 | gallery: 0.3292; notebook: 0.3292; paper: 0.32925; story: 0.3292, 0.32925 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=26:z_robust | paper: -1.148; story: -1.148 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=27:estimate | gallery: -0.1117; notebook: -0.1117; paper: -0.111713; story: -0.1117, -0.111713, -0.1 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=27:se_robust_CR1 | gallery: 0.3891; notebook: 0.3891; paper: 0.38912; story: 0.3891, 0.38912 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=27:z_robust | paper: -0.287; story: -0.287 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=28:estimate | gallery: -0.8218; notebook: -0.8218; paper: -0.821813; story: -0.8218, -0.821813 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=28:se_robust_CR1 | gallery: 0.3810; notebook: 0.3810; paper: 0.380963; story: 0.3810, 0.380963 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=28:z_robust | paper: -2.157; story: -2.157 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=29:estimate | gallery: -0.5162; notebook: -0.5162; paper: -0.516158; story: -0.5162, -0.516158 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=29:se_robust_CR1 | gallery: 0.3274; paper: 0.327362; story: 0.327362 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=29:z_robust | paper: -1.577; story: -1.577 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=2:estimate | gallery: 8.5199; notebook: 8.5199; paper: 8.51993; story: 8.5199, 8.51993 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=2:se_robust_CR1 | gallery: 3.5480; notebook: 3.5480; paper: 3.54798; story: 3.5480, 3.54798 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=2:z_robust | paper: 2.401; story: 2.401 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=30:estimate | gallery: -0.7222; notebook: -0.7222; paper: -0.722159; story: -0.7222, -0.722159 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=30:se_robust_CR1 | gallery: 0.3528; notebook: 0.3528; paper: 0.35278; story: 0.3528, 0.35278 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=30:z_robust | paper: -2.047; story: -2.047 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=31:estimate | gallery: -0.5374; notebook: -0.5374; paper: -0.537369; story: -0.5374, -0.537369 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=31:se_robust_CR1 | gallery: 0.3503; notebook: 0.3503; paper: 0.350308; story: 0.3503, 0.350308 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=31:z_robust | paper: -1.534; story: -1.534 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=32:estimate | gallery: -0.4512; notebook: -0.4512; paper: -0.45119; story: -0.4512, -0.45119 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=32:se_robust_CR1 | gallery: 0.3401; notebook: 0.3401; paper: 0.340074; story: 0.3401, 0.340074 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=32:z_robust | paper: -1.327; story: -1.327 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=35:estimate | notebook: -0.0288; story: -0.0288, -0.0287689 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=35:se_robust_CR1 | gallery: 0.2209; notebook: 0.2209; paper: 0.220916; story: 0.2209, 0.220916 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=35:z_robust | paper: -0.130; story: -0.130 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=36:estimate | notebook: 0.0641; story: 0.0641, 0.064133 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=36:se_robust_CR1 | gallery: 0.2614; notebook: 0.2614; paper: 0.261352; story: 0.2614, 0.261352 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=37:estimate | gallery: -1.3737; paper: -1.37371; story: -1.37371 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=37:se_robust_CR1 | gallery: 0.1581; paper: 0.158147; story: 0.158147 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=37:z_robust | paper: -8.686; story: -8.686 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=38:estimate | gallery: -2.1096; paper: -2.10963; story: -2.10963 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=38:se_robust_CR1 | gallery: 0.2022; paper: 0.202248; story: 0.202248, 20, 20, 20, 20 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=38:z_robust | paper: -10.431; story: -10.431 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=39:estimate | gallery: -0.3259; paper: -0.325897; story: -0.325897 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=39:se_robust_CR1 | gallery: 0.1213; paper: 0.121341; story: 0.121341 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=39:z_robust | paper: -2.686; story: -2.686 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=3:estimate | gallery: 1.4820; notebook: 1.4820; paper: 1.48195; story: 1.4820, 1.48195 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=3:se_robust_CR1 | gallery: 1.0236; notebook: 1.0236; paper: 1.02361; story: 1.0236, 1.02361 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=3:z_robust | paper: 1.448; story: 1.448 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=40:estimate | gallery: 0.1135; notebook: 0.1135; paper: 0.113492; story: 0.1135, 0.113492 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=40:se_robust_CR1 | gallery: 0.1374; notebook: 0.1374; paper: 0.137399; story: 0.1374, 0.137399 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=40:z_robust | paper: 0.826; story: 0.826 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=41:estimate | gallery: -0.4060; notebook: -0.4060; paper: -0.406009; story: -0.4060, -0.406009 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=41:se_robust_CR1 | gallery: 0.1440; notebook: 0.1440; paper: 0.144045; story: 0.1440, 0.144045 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=41:z_robust | paper: -2.819; story: -2.819 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=42:estimate | gallery: 0.5632; notebook: 0.5632; paper: 0.563216; story: 0.5632, 0.563216 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=42:se_robust_CR1 | gallery: 0.1225; notebook: 0.1225; paper: 0.122467; story: 0.1225, 0.122467 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=42:z_robust | paper: 4.599; story: 4.599 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=43:estimate | gallery: 2.0138; notebook: 2.0138; paper: 2.01382; story: 2, 2.0138, 2.01382 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=43:se_robust_CR1 | gallery: 0.0561; notebook: 0.0561; paper: 0.0560922; story: 0.0561, 0.0560922 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=43:z_robust | paper: 35.902; story: 35.902 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=44:estimate | notebook: 0.0566; story: 0.0566, 0.0566261 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=44:se_robust_CR1 | gallery: 0.0372; paper: 0.0372485; story: 0.0372485 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=44:z_robust | paper: 1.520; story: 1.520 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=45:estimate | notebook: 0.1491; story: 0.1491, 15, 15, 15, 15, 15, 15, 0.149054, 15, 15, 15, 15, 15, 15 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=45:se_robust_CR1 | gallery: 0.0308; notebook: 0.0308; paper: 0.0308408; story: 0.0308, 0.0308408 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=45:z_robust | paper: 4.833; story: 4.833 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=46:estimate | gallery: 0.2408; notebook: 0.2408; paper: 0.24077; story: 0.2408, 0.24077 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=46:se_robust_CR1 | gallery: 0.0862; notebook: 0.0862; paper: 0.0862223; story: 0.0862, 0.0862223 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=46:z_robust | paper: 2.792; story: 2.792 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=47:estimate | gallery: -0.0282; notebook: -0.0282; paper: -0.0281739; story: -0.0282, -0.0281739 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=47:se_robust_CR1 | gallery: 0.0390; notebook: 0.0390; paper: 0.0389905; story: 0.0390, 0.0389905 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=47:z_robust | paper: -0.723; story: -0.723 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=48:estimate | deck: 0.382; gallery: 0.3815; notebook: 0.3815; paper: 0.381505; story: 0.3815, 0.381505 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=48:se_model | notebook: 0.0072; story: 0.0072 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=48:se_robust_CR1 | gallery: 0.0133; notebook: 0.0133; paper: 0.0132752; story: 0.0133, 0.0132752 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=48:z_robust | deck: 28.7; paper: 28.738; rehearsal: 28.7; story: 28.738 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=49:estimate | gallery: -0.0347; notebook: -0.0347; paper: -0.0347, -0.0347155; story: -0.0347, -0.0347155 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=49:se_robust_CR1 | gallery: 0.0399; notebook: 0.0399; paper: 0.0399, 0.039899; story: 0.0399, 0.039899, 4, 4, 4, 4, 4, 4 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=49:z_robust | paper: -0.870; story: -0.870 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=4:estimate | gallery: 0.7783; notebook: 0.7783; paper: 0.778284; story: 0.7783, 0.778284 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=4:se_robust_CR1 | gallery: 0.7732; notebook: 0.7732; paper: 0.773158; story: 0.7732, 0.773158 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=4:z_robust | paper: 1.007; story: 1.007 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=50:estimate | gallery: 0.0622; notebook: 0.0622; paper: 0.0622, 0.0622139; story: 0.0622, 0.0622139 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=50:se_robust_CR1 | gallery: 0.0383; notebook: 0.0383; paper: 0.0383, 0.0382749; story: 0.0383, 0.0382749 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=50:z_robust | paper: 1.625; story: 1.625 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=51:estimate | gallery: 0.2785; paper: 0.278494; story: 0.2785, 0.278494 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=51:se_robust_CR1 | gallery: 0.0368; notebook: 0.0368; paper: 0.0367705; story: 0.0368, 0.0367705 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=51:z_robust | paper: 7.574; story: 7.574 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=52:estimate | gallery: 2.0656; notebook: 2.0656; paper: 2.06556; story: 2.0656, 2.06556 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=52:se_robust_CR1 | gallery: 0.0894; paper: 0.0894479; story: 0.0894479 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=52:z_robust | paper: 23.092; story: 23.092 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=53:estimate | gallery: 2.0387; notebook: 2.0387, 2.0387; paper: 2.0387, 2.03873; story: 2.0387, 2.0387, 2.0387, 2.03873, 2.0387, 2.0387 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=53:se_robust_CR1 | gallery: 0.2917; notebook: 0.2917, 0.2917; paper: 0.2917, 0.291729; story: 0.2917, 0.2917, 0.2917, 0.291729, 0.2917 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=53:z_robust | paper: 6.988; story: 6.988 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=5:estimate | gallery: -1.6263; notebook: -1.6263; paper: -1.62627; story: -1.6263, -1.62627 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=5:se_robust_CR1 | gallery: 0.3301; notebook: 0.3301; paper: 0.330058; story: 0.3301, 0.330058 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=5:z_robust | paper: -4.927; story: -4.927 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=6:estimate | gallery: 5.8683; notebook: 5.8683; paper: 5.86829; story: 5.8683, 5.86829 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=6:se_robust_CR1 | gallery: 2.1346; notebook: 2.1346; paper: 2.13459; story: 2.1346, 2.13459 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=6:z_robust | paper: 2.749; story: 2.749 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=7:estimate | gallery: 0.0678; notebook: 0.0678; paper: 0.0677662; story: 0.0678, 0.0677662 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=7:se_robust_CR1 | gallery: 0.4792; notebook: 0.4792; paper: 0.479217; story: 0.4792, 0.479217 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=9:estimate | gallery: 0.1666; notebook: 0.1666; paper: 0.166636; story: 0.1666, 0.166636 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=9:se_robust_CR1 | gallery: 0.4422; notebook: 0.4422; paper: 0.442236; story: 0.4422, 0.442236 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv:row=9:z_robust | paper: 0.377; story: 0.377 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.COUPLES.curvature.symmetry.threshold | notebook: 0.0030; story: 0.0030 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.COUPLES.n_households | paper: 2,223; rehearsal: 2,223 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.COUPLES.negll | deck: 10283.034; paper: 10283.034 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.employment_index.terms[0].estimate | gallery: -1.4422; notebook: -1.4422; paper: -1.44224; story: -1.4422 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.employment_index.terms[10].estimate | gallery: -0.0288; paper: -0.0287689 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.employment_index.terms[11].estimate | gallery: 0.0641; paper: 0.064133 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.hours.bands_applied[0].lo | notebook: 17.5; story: 17.5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.hours.bands_applied[1].hi | notebook: 30.5; story: 30.5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.hours.bands_applied[1].lo | notebook: 28.5; story: 28.5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.hours.bands_applied[2].hi | notebook: 36.5, 36.5; story: 36.5, 36.5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.hours.bands_applied[2].lo | notebook: 33.5; story: 33.5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.hours.bands_applied[3].hi | notebook: 40.5; story: 40.5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.canonical_gbar.hours.bands_applied[4].lo | notebook: 44.5; story: 44.5 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.common_measure.wage_reference_terms[0].estimate | gallery: 0.0566; paper: 0.0566261 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.common_measure.wage_reference_terms[1].estimate | gallery: 0.1491; paper: 0.149054 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-A.parameter_table[2].se_model | notebook: 0.2785; paper: 0.2785 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.RUM-B.parameter_table[0].estimate | notebook: 6; rehearsal: 6, 6 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.SINGLES.n_free | deck: 41; paper: 41; rehearsal: 41 | PASS |
| S11:MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json:results.SINGLES.negll | deck: 6253.463; paper: 6253.463 | PASS |
| S11:couples:criterion_improvement_vs_s10 | paper: 15.659; story: 15.659 | PASS |
| S11:singles:criterion_improvement_vs_s10 | paper: 23.753; story: 23.753 | PASS |
| S11:singles:one_nat_consumption_factor | notebook: 2, 2; story: 2, 1.633 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=10:lambda_key | gallery: 20, 20.000, 20, 20.000, 20.000, 20.000, 20.000; notebook: 20, 20.000, 20, 20.000, 20.000, 20.000, 20.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=10:objective_after_refit | gallery: 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369; notebook: 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=10:theta_l_estimate | gallery: -0.976110; notebook: -0.976110 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=11:lambda_key | gallery: 20, 20.000, 20; notebook: 20, 20.000, 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=11:objective_after_refit | gallery: 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369; notebook: 10,283.034369, 10,283.034369, 10,283.034369, 10,283.034369 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=11:theta_l_estimate | gallery: -1.686306, -1.686306, -1.686306; notebook: -1.686306, -1.686306, -1.686306 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=12:lambda_key | gallery: 40, 40.000, 40, 40.000, 40.000, 40.000, 40.000; notebook: 40, 40.000, 40, 40.000, 40.000, 40.000, 40.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=13:lambda_key | gallery: 40, 40.000, 40; notebook: 40, 40.000, 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=14:lambda_value | gallery: 45.624, 45.624, 45.624, 45.624, 45.624; notebook: 45.624, 45.624, 45.624, 45.624, 45.624 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=14:objective_after_refit | gallery: 10,283.034369, 10,283.034369; notebook: 10,283.034369, 10,283.034369 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=14:theta_l_estimate | gallery: -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109; notebook: -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109, -0.976109 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=15:lambda_value | gallery: 45.624; notebook: 45.624 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=15:objective_after_refit | gallery: 10,283.034369, 10,283.034369; notebook: 10,283.034369, 10,283.034369 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=15:theta_l_estimate | gallery: -1.686306; notebook: -1.686306 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=16:lambda_value | gallery: 43.000, 43.000, 43.000, 43.000, 43.000; notebook: 43.000, 43.000, 43.000, 43.000, 43.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=16:objective_after_refit | gallery: 10,283.034369, 10,283.034369; notebook: 10,283.034369, 10,283.034369 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=16:theta_l_estimate | gallery: -0.976109; notebook: -0.976109 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=17:lambda_value | gallery: 43.000; notebook: 43.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=17:objective_after_refit | gallery: 10,283.034369, 10,283.034369; notebook: 10,283.034369, 10,283.034369 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=17:theta_l_estimate | gallery: -1.686307, -1.686307, -1.686307, -1.686307; notebook: -1.686307, -1.686307, -1.686307, -1.686307 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=18:analytic_value | gallery: 2.759821; notebook: 2.759821 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=18:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=18:refit_value | gallery: 2.759819; notebook: 2.759819 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=18:rel_dev_from_analytic | gallery: 6.980e-07; notebook: 6.980e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=19:analytic_value | gallery: 0.480042; notebook: 0.480042 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=19:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=19:refit_value | gallery: 0.480043; notebook: 0.480043 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=19:rel_dev_from_analytic | gallery: 1.938e-06; notebook: 1.938e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=20:analytic_value | gallery: 0.252106; notebook: 0.252106 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=20:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=20:refit_value | gallery: 0.252107; notebook: 0.252107 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=20:rel_dev_from_analytic | gallery: 3.873e-06; notebook: 3.873e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=21:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=21:refit_value | gallery: -1.626266; notebook: -1.626266 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=21:rel_dev_from_analytic | gallery: 4.726e-07; notebook: 4.726e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=22:analytic_value | gallery: 3.085678; notebook: 3.085678 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=22:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=22:refit_value | gallery: 3.085675; notebook: 3.085675 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=22:rel_dev_from_analytic | gallery: 9.344e-07; notebook: 9.344e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=23:analytic_value | gallery: 0.035633, 0.035633; notebook: 0.035633, 0.035633 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=23:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=23:rel_dev_from_analytic | gallery: 1.406e-05; notebook: 1.406e-05 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=24:analytic_value | gallery: 0.525822; notebook: 0.525822 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=24:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=24:refit_value | gallery: 0.525823; notebook: 0.525823 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=24:rel_dev_from_analytic | gallery: 8.615e-07; notebook: 8.615e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=25:analytic_value | gallery: 0.087621; notebook: 0.087621 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=25:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=25:refit_value | gallery: 0.087620; notebook: 0.087620 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=25:rel_dev_from_analytic | gallery: 3.721e-06; notebook: 3.721e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=26:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=26:refit_value | gallery: -0.927352; notebook: -0.927352 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=26:rel_dev_from_analytic | gallery: 1.340e-06; notebook: 1.340e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=27:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=27:refit_value | gallery: 0.893976, 0.893976; notebook: 0.893976, 0.893976 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=27:rel_dev_from_analytic | gallery: 5.307e-11; notebook: 5.307e-11 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=28:analytic_value | gallery: 0.155498, 0.155498; notebook: 0.155498, 0.155498 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=28:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=28:rel_dev_from_analytic | gallery: 3.851e-11; notebook: 3.851e-11 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=29:analytic_value | gallery: 0.081664, 0.081664; notebook: 0.081664, 0.081664 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=29:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=29:rel_dev_from_analytic | gallery: 3.650e-12; notebook: 3.650e-12 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=2:lambda_key | gallery: 20, 20.000; notebook: 20, 20.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=2:objective_after_refit | gallery: 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074; notebook: 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=2:theta_l_estimate | gallery: -1.626266; notebook: -1.626266 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=2:wall_seconds | rehearsal: 80; story: 80, 80, 80, 80 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=30:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=30:rel_dev_from_analytic | gallery: 2.332e-11; notebook: 2.332e-11 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=31:analytic_value | gallery: 1.622517, 1.622517; notebook: 1.622517, 1.622517 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=31:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=31:rel_dev_from_analytic | gallery: 3.338e-10; notebook: 3.338e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=32:analytic_value | gallery: 0.018737, 0.018737; notebook: 0.018737, 0.018737 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=32:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=32:rel_dev_from_analytic | gallery: 9.748e-12; notebook: 9.748e-12 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=33:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=33:refit_value | gallery: 0.276489, 0.276489; notebook: 0.276489, 0.276489 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=33:rel_dev_from_analytic | gallery: 3.413e-10; notebook: 3.413e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=34:analytic_value | gallery: 0.046073, 0.046073; notebook: 0.046073, 0.046073 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=34:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=34:rel_dev_from_analytic | gallery: 4.300e-10; notebook: 4.300e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=35:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=35:rel_dev_from_analytic | gallery: 2.655e-10; notebook: 2.655e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=36:analytic_value | gallery: 0.721802, 0.721802; notebook: 0.721802, 0.721802 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=36:rel_dev_from_analytic | gallery: 3.817e-07; notebook: 3.817e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=37:analytic_value | gallery: 0.125550; notebook: 0.125550 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=37:refit_value | gallery: 0.125551; notebook: 0.125551 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=37:rel_dev_from_analytic | gallery: 5.234e-06; notebook: 5.234e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=38:refit_value | gallery: 0.065936, 0.065936; notebook: 0.065936, 0.065936 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=38:rel_dev_from_analytic | gallery: 9.493e-06; notebook: 9.493e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=39:analytic_value | gallery: -1.626267; notebook: -1.626267 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=39:refit_value | gallery: -1.626266; notebook: -1.626266 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=39:rel_dev_from_analytic | gallery: 5.426e-07; notebook: 5.426e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=3:lambda_key | gallery: 20, 20.000; notebook: 20, 20.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=3:objective_after_refit | gallery: 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074; notebook: 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=3:theta_l_estimate | gallery: -0.927352; notebook: -0.927352 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=40:analytic_value | gallery: 1.436184; notebook: 1.436184 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=40:refit_value | gallery: 1.436185; notebook: 1.436185 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=40:rel_dev_from_analytic | gallery: 3.841e-07; notebook: 3.841e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=41:analytic_value | gallery: 0.016585, 0.016585; notebook: 0.016585, 0.016585 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=41:rel_dev_from_analytic | gallery: 1.024e-05; notebook: 1.024e-05 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=42:analytic_value | gallery: 0.244736, 0.244736; notebook: 0.244736, 0.244736 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=42:rel_dev_from_analytic | gallery: 5.966e-07; notebook: 5.966e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=43:analytic_value | gallery: 0.040782; notebook: 0.040782 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=43:refit_value | gallery: 0.040781; notebook: 0.040781 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=43:rel_dev_from_analytic | gallery: 1.789e-05; notebook: 1.789e-05 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=44:refit_value | gallery: -0.927353, -0.927353, -0.927353, -0.927353, -0.927353; notebook: -0.927353, -0.927353, -0.927353, -0.927353, -0.927353 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=44:rel_dev_from_analytic | gallery: 4.239e-07; notebook: 4.239e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=45:analytic_value | gallery: 0.794781, 0.794781; notebook: 0.794781, 0.794781 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=45:rel_dev_from_analytic | gallery: 2.112e-10; notebook: 2.112e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=46:analytic_value | gallery: 0.138244, 0.138244; notebook: 0.138244, 0.138244 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=46:rel_dev_from_analytic | gallery: 1.600e-10; notebook: 1.600e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=47:refit_value | gallery: 0.072602, 0.072602; notebook: 0.072602, 0.072602 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=47:rel_dev_from_analytic | gallery: 3.841e-11; notebook: 3.841e-11 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=48:refit_value | gallery: -1.626267, -1.626267, -1.626267, -1.626267, -1.626267; notebook: -1.626267, -1.626267, -1.626267, -1.626267, -1.626267 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=48:rel_dev_from_analytic | gallery: 8.828e-11; notebook: 8.828e-11 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=49:analytic_value | gallery: 1.517269, 1.517269; notebook: 1.517269, 1.517269 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=49:rel_dev_from_analytic | gallery: 1.194e-09; notebook: 1.194e-09 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=4:lambda_key | gallery: 40, 40.000; notebook: 40, 40.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=50:refit_value | gallery: 0.017521, 0.017521; notebook: 0.017521, 0.017521 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=50:rel_dev_from_analytic | gallery: 2.265e-11; notebook: 2.265e-11 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=51:refit_value | gallery: 0.258554, 0.258554; notebook: 0.258554, 0.258554 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=51:rel_dev_from_analytic | gallery: 1.221e-09; notebook: 1.221e-09 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=52:refit_value | gallery: 0.043084, 0.043084; notebook: 0.043084, 0.043084 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=52:rel_dev_from_analytic | gallery: 1.506e-09; notebook: 1.506e-09 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=53:refit_value | gallery: -0.927353, -0.927353; notebook: -0.927353, -0.927353 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=53:rel_dev_from_analytic | gallery: 9.025e-10; notebook: 9.025e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=54:analytic_value | gallery: 2.023920, 2.023920, 2.023920; notebook: 2.023920, 2.023920, 2.023920 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=54:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=54:rel_dev_from_analytic | gallery: 3.281e-07; notebook: 3.281e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=55:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=55:refit_value | gallery: -0.004063, -0.004063; notebook: -0.004063, -0.004063 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=55:rel_dev_from_analytic | gallery: 1.754e-06; notebook: 1.754e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=56:analytic_value | gallery: 0.003296, 0.003296; notebook: 0.003296, 0.003296 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=56:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=56:rel_dev_from_analytic | gallery: 6.280e-07; notebook: 6.280e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=57:refit_value | gallery: -0.976110; notebook: -0.976110 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=57:rel_dev_from_analytic | gallery: 8.399e-07; notebook: 8.399e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=58:analytic_value | gallery: 4.071334, 4.071334; notebook: 4.071334, 4.071334 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=58:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=58:refit_value | gallery: 4.071329; notebook: 4.071329 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=58:rel_dev_from_analytic | gallery: 1.293e-06; notebook: 1.293e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=59:analytic_value | gallery: -0.038161, -0.038161; notebook: -0.038161, -0.038161 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=59:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=59:rel_dev_from_analytic | gallery: 5.449e-07; notebook: 5.449e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=5:lambda_key | gallery: 40, 40.000; notebook: 40, 40.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=60:analytic_value | gallery: 0.002270, 0.002270; notebook: 0.002270, 0.002270 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=60:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=60:rel_dev_from_analytic | gallery: 4.502e-06; notebook: 4.502e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=61:analytic_value | gallery: -0.094916, -0.094916; notebook: -0.094916, -0.094916 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=61:lambda_key | gallery: 20; notebook: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=61:rel_dev_from_analytic | gallery: 6.668e-06; notebook: 6.668e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=62:analytic_value | gallery: -1.686307, -1.686307, -1.686307, -1.686307, -1.686307, -1.686307, -1.686307, -1.686307; notebook: -1.686307, -1.686307, -1.686307, -1.686307, -1.686307, -1.686307, -1.686307, -1.686307 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=62:refit_value | gallery: -1.686306; notebook: -1.686306 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=62:rel_dev_from_analytic | gallery: 7.811e-07; notebook: 7.811e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=63:analytic_value | gallery: 1.028857, 1.028857, 1.028857; notebook: 1.028857, 1.028857, 1.028857 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=63:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=63:rel_dev_from_analytic | gallery: 7.841e-10; notebook: 7.841e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=64:analytic_value | gallery: -0.002065, -0.002065; notebook: -0.002065, -0.002065 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=64:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=64:rel_dev_from_analytic | gallery: 8.057e-08; notebook: 8.057e-08 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=65:analytic_value | gallery: 0.001675, 0.001675; notebook: 0.001675, 0.001675 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=65:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=65:rel_dev_from_analytic | gallery: 4.867e-08; notebook: 4.867e-08 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=66:rel_dev_from_analytic | gallery: 5.439e-10; notebook: 5.439e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=67:analytic_value | gallery: 1.265050, 1.265050, 1.265050; notebook: 1.265050, 1.265050, 1.265050 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=67:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=67:rel_dev_from_analytic | gallery: 9.429e-10; notebook: 9.429e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=68:analytic_value | gallery: -0.011857, -0.011857; notebook: -0.011857, -0.011857 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=68:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=68:rel_dev_from_analytic | gallery: 1.083e-09; notebook: 1.083e-09 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=69:analytic_value | gallery: 0.000705, 0.000705; notebook: 0.000705, 0.000705 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=69:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=69:rel_dev_from_analytic | gallery: 3.169e-08; notebook: 3.169e-08 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=6:lambda_value | gallery: 45.624; notebook: 45.624 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=6:objective_pre_refit_transformed_at_record | gallery: 6,253.463074, 6,253.463074; notebook: 6,253.463074, 6,253.463074 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=6:theta_l_estimate | gallery: -1.626266; notebook: -1.626266 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=70:lambda_key | gallery: 40; notebook: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=70:refit_value | gallery: -0.029492, -0.029492; notebook: -0.029492, -0.029492 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=70:rel_dev_from_analytic | gallery: 2.480e-10; notebook: 2.480e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=71:rel_dev_from_analytic | gallery: 3.980e-10; notebook: 3.980e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=72:analytic_value | gallery: 0.904879, 0.904879, 0.904879; notebook: 0.904879, 0.904879, 0.904879 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=72:rel_dev_from_analytic | gallery: 8.689e-08; notebook: 8.689e-08 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=73:refit_value | gallery: -0.001816, -0.001816; notebook: -0.001816, -0.001816 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=73:rel_dev_from_analytic | gallery: 4.452e-06; notebook: 4.452e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=74:refit_value | gallery: 0.001474, 0.001474; notebook: 0.001474, 0.001474 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=74:rel_dev_from_analytic | gallery: 4.918e-08; notebook: 4.918e-08 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=75:refit_value | gallery: -0.976109, -0.976109, -0.976109, -0.976109, -0.976109; notebook: -0.976109, -0.976109, -0.976109, -0.976109, -0.976109 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=75:rel_dev_from_analytic | gallery: 1.991e-07; notebook: 1.991e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=76:analytic_value | gallery: 1.013374, 1.013374; notebook: 1.013374, 1.013374 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=76:refit_value | gallery: 1.013373; notebook: 1.013373 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=76:rel_dev_from_analytic | gallery: 9.338e-07; notebook: 9.338e-07 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=77:refit_value | gallery: -0.009498, -0.009498; notebook: -0.009498, -0.009498 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=77:rel_dev_from_analytic | gallery: 1.258e-06; notebook: 1.258e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=78:analytic_value | gallery: 0.000565, 0.000565; notebook: 0.000565, 0.000565 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=78:rel_dev_from_analytic | gallery: 1.243e-05; notebook: 1.243e-05 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=79:analytic_value | gallery: -0.023625; notebook: -0.023625 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=79:refit_value | gallery: -0.023624; notebook: -0.023624 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=79:rel_dev_from_analytic | gallery: 2.864e-05; notebook: 2.864e-05 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=7:lambda_value | gallery: 45.624; notebook: 45.624 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=7:objective_pre_refit_transformed_at_record | gallery: 6,253.463074, 6,253.463074; notebook: 6,253.463074, 6,253.463074 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=7:theta_l_estimate | gallery: -0.927353, -0.927353; notebook: -0.927353, -0.927353 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=80:analytic_value | gallery: -1.686307; notebook: -1.686307 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=80:refit_value | gallery: -1.686306; notebook: -1.686306 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=80:rel_dev_from_analytic | gallery: 1.062e-06; notebook: 1.062e-06 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=81:refit_value | gallery: 0.958732, 0.958732, 0.958732; notebook: 0.958732, 0.958732, 0.958732 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=81:rel_dev_from_analytic | gallery: 7.117e-10; notebook: 7.117e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=82:refit_value | gallery: -0.001925, -0.001925; notebook: -0.001925, -0.001925 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=82:rel_dev_from_analytic | gallery: 6.873e-08; notebook: 6.873e-08 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=83:analytic_value | gallery: 0.001561, 0.001561; notebook: 0.001561, 0.001561 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=83:rel_dev_from_analytic | gallery: 6.795e-08; notebook: 6.795e-08 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=84:refit_value | gallery: -0.976109, -0.976109; notebook: -0.976109, -0.976109 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=84:rel_dev_from_analytic | gallery: 4.708e-10; notebook: 4.708e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=85:refit_value | gallery: 1.119807, 1.119807, 1.119807; notebook: 1.119807, 1.119807, 1.119807 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=85:rel_dev_from_analytic | gallery: 8.480e-10; notebook: 8.480e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=86:refit_value | gallery: -0.010496, -0.010496; notebook: -0.010496, -0.010496 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=86:rel_dev_from_analytic | gallery: 8.849e-10; notebook: 8.849e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=87:analytic_value | gallery: 0.000624, 0.000624; notebook: 0.000624, 0.000624 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=87:rel_dev_from_analytic | gallery: 2.667e-08; notebook: 2.667e-08 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=88:refit_value | gallery: -0.026106, -0.026106; notebook: -0.026106, -0.026106 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=88:rel_dev_from_analytic | gallery: 2.540e-10; notebook: 2.540e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=89:analytic_value | gallery: -1.686307, -1.686307; notebook: -1.686307, -1.686307 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=89:rel_dev_from_analytic | gallery: 3.404e-10; notebook: 3.404e-10 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=8:lambda_value | gallery: 43.000; notebook: 43.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=8:objective_after_refit | gallery: 6,253.463074, 6,253.463074; notebook: 6,253.463074, 6,253.463074 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=8:theta_l_estimate | gallery: -1.626267, -1.626267; notebook: -1.626267, -1.626267 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=9:lambda_value | gallery: 43.000; notebook: 43.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=9:objective_after_refit | gallery: 6,253.463074, 6,253.463074; notebook: 6,253.463074, 6,253.463074 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionA_run_table_v1.csv:row=9:theta_l_estimate | gallery: -0.927353; notebook: -0.927353 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=10:T | gallery: 75; notebook: 75; story: 75, 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=10:estimate | gallery: 0.066345; notebook: 0.066345 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=10:estimate_at_T80_baseline | gallery: 0.067766, 0.067766; notebook: 0.067766, 0.067766 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=11:T | gallery: 75; notebook: 75; rehearsal: 75, 75; story: 75, 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=11:estimate | gallery: 0.681137; notebook: 0.681137 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=12:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=12:estimate | gallery: 0.118354; notebook: 0.118354 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=12:estimate_at_T80_baseline | gallery: 0.166636, 0.166636; notebook: 0.166636, 0.166636 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=13:T | paper: 90; story: 90, 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=14:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=14:estimate | gallery: 14.378742; notebook: 14.378742 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=14:estimate_at_T80_baseline | gallery: 8.519929, 8.519929; notebook: 8.519929, 8.519929 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=15:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=15:estimate | gallery: 2.091836; notebook: 2.091836 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=15:estimate_at_T80_baseline | gallery: 1.481952, 1.481952; notebook: 1.481952, 1.481952 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=16:T | gallery: 90; notebook: 90; rehearsal: 90, 90, 90; story: 90, 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=16:estimate_at_T80_baseline | gallery: 0.778284, 0.778284; notebook: 0.778284, 0.778284 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=18:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=18:estimate | gallery: 9.957457; notebook: 9.957457 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=18:estimate_at_T80_baseline | gallery: 5.868292, 5.868292; notebook: 5.868292, 5.868292 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=19:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=19:estimate | gallery: -0.011930; notebook: -0.011930 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=20:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=21:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=21:estimate | gallery: 0.053156; notebook: 0.053156 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=22:T | paper: 80, 80; rehearsal: 80.0 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=25:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=25:estimate | gallery: 2.260373; notebook: 2.260373 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=25:estimate_at_T80_baseline | gallery: 3.981360, 3.981360, 3.981360; notebook: 3.981360, 3.981360, 3.981360 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=26:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=26:estimate | gallery: -0.002914; notebook: -0.002914 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=26:estimate_at_T80_baseline | gallery: -0.007992, -0.007992; notebook: -0.007992, -0.007992 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=27:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=27:estimate | gallery: 0.003705; notebook: 0.003705 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=27:estimate_at_T80_baseline | gallery: 0.006483, 0.006483; notebook: 0.006483, 0.006483 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=29:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=29:estimate | gallery: 7.938300; notebook: 7.938300 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=29:estimate_at_T80_baseline | gallery: 13.102854, 13.102854, 13.102854; notebook: 13.102854, 13.102854, 13.102854 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=30:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=30:estimate | gallery: -0.074166; notebook: -0.074166 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=30:estimate_at_T80_baseline | gallery: -0.122813, -0.122813; notebook: -0.122813, -0.122813 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=31:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=31:estimate | gallery: 0.005651; notebook: 0.005651 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=31:estimate_at_T80_baseline | gallery: 0.007307, 0.007307; notebook: 0.007307, 0.007307 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=32:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=32:estimate | gallery: -0.099584; notebook: -0.099584 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=32:estimate_at_T80_baseline | gallery: -0.305471, -0.305471; notebook: -0.305471, -0.305471 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=34:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=34:estimate | gallery: 7.191531; notebook: 7.191531 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=35:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=35:estimate | gallery: -0.019444; notebook: -0.019444 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=36:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=36:estimate | gallery: 0.011500; notebook: 0.011500 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=38:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=38:estimate | gallery: 22.130177; notebook: 22.130177 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=39:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=39:estimate | gallery: -0.207124; notebook: -0.207124 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=40:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=40:estimate | gallery: 0.009375; notebook: 0.009375 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=41:T | gallery: 90; notebook: 90 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=41:estimate | gallery: -0.676017; notebook: -0.676017 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=5:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=5:estimate | gallery: 5.253148; notebook: 5.253148 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=6:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=6:estimate | gallery: 0.993437; notebook: 0.993437 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=7:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=7:estimate | gallery: 0.480310; notebook: 0.480310 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=9:T | gallery: 75; notebook: 75 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionB_run_table_v1.csv:row=9:estimate | gallery: 3.664756; notebook: 3.664756 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=10:beta_l0 | gallery: 0.794781; notebook: 0.794781 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=10:lambda_l | gallery: 43.000, 43.000, 43.000, 43.000; notebook: 43.000, 43.000, 43.000, 43.000; story: 43.0 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=10:theta_l | gallery: -1.626267, -1.626267, -1.626267, -1.626267, -1.626267, -1.626267, -1.626267; notebook: -1.626267, -1.626267, -1.626267, -1.626267, -1.626267, -1.626267, -1.626267 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=11:beta_l0 | gallery: 5.868292; notebook: 5.868292 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=11:lambda_l | gallery: 10.000, 10.000, 10.000, 10.000; notebook: 10.000, 10.000, 10.000, 10.000; story: 10, 1,000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=12:beta_l0 | gallery: 3.085678; notebook: 3.085678 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=12:lambda_l | gallery: 20.000, 20.000; notebook: 20.000, 20.000; story: 20 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=13:beta_l0 | gallery: 3.085675; notebook: 3.085675 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=13:lambda_l | gallery: 20.000, 20.000; notebook: 20.000, 20.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=13:mrs | gallery: 27.826780; notebook: 27.826780 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=13:negll | gallery: 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074; notebook: 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074, 6,253.463074 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=13:theta_l | gallery: -0.927352; notebook: -0.927352 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=14:beta_l0 | gallery: 1.622517; notebook: 1.622517 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=14:lambda_l | gallery: 40.000, 40.000; notebook: 40.000, 40.000; story: 40 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=15:beta_l0 | gallery: 1.622517; notebook: 1.622517 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=15:lambda_l | gallery: 40.000, 40.000; notebook: 40.000, 40.000 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=16:beta_l0 | gallery: 1.436184; notebook: 1.436184 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=16:lambda_l | gallery: 45.624, 45.624; notebook: 45.624, 45.624; story: 45.623591 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=17:beta_l0 | gallery: 1.436185; notebook: 1.436185 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=17:du_dl | gallery: 0.032327, 0.032327, 0.032327, 0.032327, 0.032327, 0.032327, 0.032327, 0.032327, 0.032327; notebook: 0.032327, 0.032327, 0.032327, 0.032327, 0.032327, 0.032327, 0.032327, 0.032327, 0.032327 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=17:lambda_l | gallery: 45.624, 45.624; notebook: 45.624, 45.624 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=17:mrs | gallery: 27.826791; notebook: 27.826791 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=17:theta_l | gallery: -0.927353, -0.927353, -0.927353, -0.927353, -0.927353, -0.927353, -0.927353, -0.927353; notebook: -0.927353, -0.927353, -0.927353, -0.927353, -0.927353, -0.927353, -0.927353, -0.927353 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=18:beta_l0 | gallery: 1.517269; notebook: 1.517269 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=19:beta_l0 | gallery: 1.517269; notebook: 1.517269 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=19:mrs | gallery: 27.826781, 27.826781, 27.826781, 27.826781, 27.826781, 27.826781, 27.826781; notebook: 27.826781, 27.826781, 27.826781, 27.826781, 27.826781, 27.826781, 27.826781 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=22:beta_l0 | gallery: 2.023920; notebook: 2.023920 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=22:du_dl | gallery: 0.024599, 0.024599, 0.024599, 0.024599, 0.024599, 0.024599, 0.024599, 0.024599, 0.024599; notebook: 0.024599, 0.024599, 0.024599, 0.024599, 0.024599, 0.024599, 0.024599, 0.024599, 0.024599 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=22:mrs | gallery: 45.109507; notebook: 45.109507 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=22:theta_l | gallery: -0.976110; notebook: -0.976110 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=24:beta_l0 | gallery: 1.028857; notebook: 1.028857 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=26:beta_l0 | gallery: 0.904879; notebook: 0.904879 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=26:mrs | gallery: 45.109539; notebook: 45.109539 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=27:mrs | gallery: 45.109518, 45.109518, 45.109518, 45.109518, 45.109518; notebook: 45.109518, 45.109518, 45.109518, 45.109518, 45.109518 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=28:beta_l0 | gallery: 0.958732; notebook: 0.958732 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=28:mrs | gallery: 45.109518, 45.109518; notebook: 45.109518, 45.109518 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=2:beta_l0 | gallery: 8.519929; notebook: 8.519929 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=30:du_dl | gallery: 0.023614, 0.023614, 0.023614, 0.023614, 0.023614; notebook: 0.023614, 0.023614, 0.023614, 0.023614, 0.023614 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=31:beta_l0 | gallery: 4.071329; notebook: 4.071329 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=31:mrs | gallery: 43.302215; notebook: 43.302215 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=33:beta_l0 | gallery: 1.265050; notebook: 1.265050 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=33:mrs | gallery: 43.302216, 43.302216, 43.302216, 43.302216, 43.302216, 43.302216, 43.302216; notebook: 43.302216, 43.302216, 43.302216, 43.302216, 43.302216, 43.302216, 43.302216 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=35:beta_l0 | gallery: 1.013373; notebook: 1.013373 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=35:mrs | gallery: 43.302224; notebook: 43.302224 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=37:beta_l0 | gallery: 1.119807; notebook: 1.119807 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=37:du_dl | gallery: 0.023614, 0.023614, 0.023614, 0.023614; notebook: 0.023614, 0.023614, 0.023614, 0.023614 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=3:beta_l0 | gallery: 2.759821; notebook: 2.759821 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=4:beta_l0 | gallery: 2.759819; notebook: 2.759819 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=4:mrs | gallery: 16.594712; notebook: 16.594712 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=4:theta_l | gallery: -1.626266, -1.626266; notebook: -1.626266, -1.626266 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=6:beta_l0 | gallery: 0.893976, 0.893976; notebook: 0.893976, 0.893976 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=6:mrs | gallery: 16.594717, 16.594717; notebook: 16.594717, 16.594717 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=7:beta_l0 | gallery: 0.721802; notebook: 0.721802 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=8:beta_l0 | gallery: 0.721802; notebook: 0.721802 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=8:du_dl | gallery: 0.019125, 0.019125, 0.019125, 0.019125, 0.019125, 0.019125, 0.019125, 0.019125, 0.019125; notebook: 0.019125, 0.019125, 0.019125, 0.019125, 0.019125, 0.019125, 0.019125, 0.019125, 0.019125 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=8:mrs | gallery: 16.594706; notebook: 16.594706 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=9:beta_l0 | gallery: 0.794781; notebook: 0.794781 | PASS |
| WS4:MNL@5a8e6bba:experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/outputs/ws4_sectionC_derived_objects_v1.csv:row=9:mrs | gallery: 16.594717, 16.594717, 16.594717, 16.594717, 16.594717; notebook: 16.594717, 16.594717, 16.594717, 16.594717, 16.594717 | PASS |

## Substantive wording changes

- Rebound extensive-margin labels to observed weighted accuracy; G2 bootstrap means are now described only as numerical-integration diagnostics.
- Replaced all current POSFIT-v2b surface labels with the accepted POSFIT-v3 vintage and removed the unresolved bootstrap-replication count from the deck/rehearsal.
- Added the observed fit percentages and simulated bands to the story/paper figure caption, making the bitmap labels text-auditable.
- Replaced stale ‘fit verdicts open’ wording with the explicit group adjudications.
- Removed current-surface descriptions of superseded welfare/decomposition constructions; the current provenance now states eight P/A/B coalitions per scale and the actual DECOMP-2 Monte Carlo/second-seed evidence.
- Rephrased the empirical-domain welfare coincidence without reproducing the retired W4/W1 comparison.
- Removed exact normalizer, simulated-consumption-floor and sub-ten-hour support counts that did not resolve to an accepted source package; their qualitative limitations remain stated.
- Removed predecessor-frame counts from the scientific-history paragraph while retaining the current S11 sample sizes and screening description.
- Narrowed notebook output labels from generic access to coarse geographic/temporal access and pointed the notebook to POSFIT v3 and the DECOMP-2 repository outputs.
- Updated the report’s notebook description to the canonical A-to-Z reader/results notebook and retained the explicit raw-job-set/pricing limitation.

## Explicitly reported live retired-content consumer (not modified)

- Path: `C:\Users\hisham\Repo\MNL\experiments\JMP_SEMINAR_SPRINT\discussion_notebook_support.py`
- SHA-256: `dcd67843f1f860cb1d783ec1e4e597afdf3e3a347ae9e5caaf257cd7c90e55b4`
- Status: CONFIRMED — reads `REGISTER["discussion_tables"]` and renders I00/I01/I10/I11 under “Four principal welfare states”. This file is outside the six surfaces and was reported, not fixed.

## Coverage and machine artifacts

- Result-bearing numeric occurrences extracted: **6152**.
- Resolved to accepted sources: **6152**.
- Unresolved/mismatched: **0**.
- Data/method/definition tables explicitly excluded from the result-numeral population: **87**.
- Accepted source files/blobs hashed: **51**.
- Full occurrence-level number-to-source table: `C:\Users\hisham\Repo\Job_Market_paper\reports\JMP_final_claim_number_to_source_v1.csv`.
- Machine-readable report: `C:\Users\hisham\Repo\Job_Market_paper\reports\JMP_final_claim_evidence_gate_v1.json`.
- Plot axis ticks are presentation scales, not result claims. Data-labelled fit values in bitmap figures are duplicated in visible captions and checked semantically above.
