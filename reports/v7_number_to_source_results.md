# V7 number-to-source gate

Overall: **PASS**

Expected display values are computed from the accepted source artifacts listed below; no estimate is recomputed.

| Claim family | Source | Status |
|---|---|---:|
| primary population-fit MAEs | `Band-Fix-2 population moments::summaries` | **PASS** |
| benchmark population-fit MAEs | `Band-Fix-2 population moments::summaries` | **PASS** |
| single women reportable accuracy/band (headline units) | `POSFIT v3b simulation bands + numerical adequacy` | **PASS** |
| single women reportable accuracy/band (raw shares) | `POSFIT v3b simulation bands` | **PASS** |
| single women reportable accuracy headline | `POSFIT v3b simulation bands` | **PASS** |
| single women adequacy ratio | `POSFIT v3b numerical adequacy` | **PASS** |
| coupled women reportable accuracy/band (headline units) | `POSFIT v3b simulation bands + numerical adequacy` | **PASS** |
| coupled women reportable accuracy/band (raw shares) | `POSFIT v3b simulation bands` | **PASS** |
| coupled women reportable accuracy headline | `POSFIT v3b simulation bands` | **PASS** |
| coupled women adequacy ratio | `POSFIT v3b numerical adequacy` | **PASS** |
| single men withheld accuracy adequacy ratio | `POSFIT v3b numerical adequacy` | **PASS** |
| single men withheld accuracy status | `POSFIT v3b numerical adequacy` | **PASS** |
| coupled men withheld accuracy adequacy ratio | `POSFIT v3b numerical adequacy` | **PASS** |
| coupled men withheld accuracy status | `POSFIT v3b numerical adequacy` | **PASS** |
| four-group 37-hour observed-minus-predicted gaps | `Band-Fix-2 population moments::hours::h_36_5_37_5` | **PASS** |
| four-group 37-hour observed/predicted cells | `Band-Fix-2 population moments::hours::h_36_5_37_5` | **PASS** |
| corrected structural FT observed/predicted cells | `Band-Fix-2 population moments::hours::ft` | **PASS** |
| restricted DECOMP-2 Gini-change range | `V7 registry::d2_deltaI_pct_singles_eq/couples_uneq` | **PASS** |
| RUM-A input-width limitation | `RUM edge-scope audit::RUM-A` | **PASS** |

## Source hashes

- POSFIT v3b simulation bands: `cbc827e76357503265a315bf1945f53eee51c76f41ac4843634abd7bdd7f418e` — `MNL_posfit\outputs\positive_fit_diagnostics_v3b\model_simulated_bands.csv`
- POSFIT v3b numerical adequacy: `304b7af652118d64df9f5862d3c1af42fe91dad642d768487d6bcaf03b7369af` — `MNL_posfit\outputs\positive_fit_diagnostics_v3b\g2_adequacy.csv`
- Band-Fix-2 population moments: `e75ff27c6e324e332231f29a60282b742ab6114bd1f4b6f60afea3fa98977d12` — `MNL_posfit\experiments\JMP_SEMINAR_SPRINT\runs\bandfix2_recompute\new_results_v1.json`
- RUM edge-scope audit: `45702e34f0d99c45332bdc433928f105effb03d600b3f321d2d3e4e4064edda1` — `MNL_posfit\outputs\band_fix_1\band_fix_3_rum_edge_scope_v1.json`
- V7 registered decomposition values: `d0f22fb2e38ed3097203de12d34bbc3dc686f19b90a1a4ced43467461be40123` — `Job_Market_paper\reports\numbers_of_record_v7.json`
