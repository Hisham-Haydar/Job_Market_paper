# V11 number-to-source results

Overall: **PASS**

| Check | Source | Status |
|---|---|---:|
| all certification checks pass | `certified record overall block` | **PASS** |
| every V10 registry value unchanged in V11 | `numbers_of_record_v10.json vs v11 (no differences)` | **PASS** |
| new registry keys are only source-bound comparison and illustration keys | `att_couples_eq_opportunity_pct, att_couples_uneq_opportunity_pct, att_opportunity_max_pct, att_opportunity_min_pct, att_singles_eq_opportunity_pct, att_singles_uneq_opportunity_pct, mh_access_ratio, mh_admissible_pairs, mh_crossing_wage, mh_employment_share_a, mh_employment_share_b, mh_leisure_cut, mh_leisure_distance, mh_leisure_weight_a, mh_leisure_weight_b, mh_opportunity_distance, mh_opportunity_distance_median, mh_wage_gap` | **PASS** |
| every scalar placeholder resolves | `V11 registry` | **PASS** |
| singles unequivalised ex-ante result | `results.singles.unequivalised` | **PASS** |
| singles equivalised ex-ante result | `results.singles.equivalised` | **PASS** |
| couples unequivalised ex-ante result | `results.couples.unequivalised` | **PASS** |
| couples equivalised ex-ante result | `results.couples.equivalised` | **PASS** |
| attained comparison values from the certified record | `comparison_W1F block` | **PASS** |
| attained A+B range is the sourced minimum and maximum | `derived over four comparison_W1F shares` | **PASS** |
| ex-ante A+B range is the sourced minimum and maximum | `derived over four certified shares` | **PASS** |
| single-adult access about three times earnings | `singles phi.A/phi.B` | **PASS** |
| couples: no reversal, equivalisation and preference sign | `couples rows` | **PASS** |
| singles reversal: ATT earnings > access, EA access > earnings | `singles rows` | **PASS** |
| illustration mh_admissible_pairs equals its record | `Job_Market_paper/reports/v11_matched_households.json::selection_rule.admissible_pairs` | **PASS** |
| illustration mh_leisure_weight_a equals its record | `Job_Market_paper/reports/v11_matched_households.json::leisure_weight_A` | **PASS** |
| illustration mh_leisure_weight_b equals its record | `Job_Market_paper/reports/v11_matched_households.json::leisure_weight_B` | **PASS** |
| illustration mh_leisure_distance equals its record | `Job_Market_paper/reports/v11_matched_households.json::leisure_profile_distance` | **PASS** |
| illustration mh_leisure_cut equals its record | `Job_Market_paper/reports/v11_matched_households.json::leisure_profile_distance_p10_cut` | **PASS** |
| illustration mh_access_ratio equals its record | `Job_Market_paper/reports/v11_matched_households.json::access_mass_ratio_A_over_B` | **PASS** |
| illustration mh_employment_share_a equals its record | `Job_Market_paper/reports/v11_matched_households.json::opportunity_employment_share_A` | **PASS** |
| illustration mh_employment_share_b equals its record | `Job_Market_paper/reports/v11_matched_households.json::opportunity_employment_share_B` | **PASS** |
| illustration mh_wage_gap equals its record | `Job_Market_paper/reports/v11_matched_households.json::wage_location_gap_B_minus_A_logpoints` | **PASS** |
| illustration mh_crossing_wage equals its record | `Job_Market_paper/reports/v11_matched_households.json::A_more_offers_paying_at_least_w_up_to_eur_per_hour` | **PASS** |
| illustration mh_opportunity_distance equals its record | `Job_Market_paper/reports/v11_matched_households.json::opportunity_distance` | **PASS** |
| illustration mh_opportunity_distance_median equals its record | `Job_Market_paper/reports/v11_matched_households.json::opportunity_distance_admissible_median` | **PASS** |
| illustration numbers displayed as sourced | `v11_matched_households.json` | **PASS** |
| illustration dominance statements match the record | `v11_matched_households.json` | **PASS** |
| illustration record carries no identifier or record value | `none` | **PASS** |
| pricing count 351,024,407 matches the result memo and report appendix | `result memo table` | **PASS** |

## Source hashes

- certified ex-ante result record: `5923e62d16cf11f22b2b92608a0f20ceac3fcfcaeb5d44afc8a9c8f8bd021898` — `MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json`
- certified result memo: `c3a52b1b48732faff62f11d07aafcaa79a88e287fed72e6727d00425b47d5e86` — `MNL_wea/docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md`
- matched-household record: `3f4691f63fdda93123bf156770a8285f95ef91896dd122e480db14c5293c62ba` — `Job_Market_paper/reports/v11_matched_households.json`
- V10 registry: `9a95a9fb6685c8cae7533ad83744abce11f6fca84214ac6e300d06c77b62150f` — `Job_Market_paper/reports/numbers_of_record_v10.json`
