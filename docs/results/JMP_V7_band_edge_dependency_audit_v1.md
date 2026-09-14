# V7 band-edge dependency audit

Date: 14 September 2026  
Scope: S11 predictive evaluation, population-fit reporting, RUM-A/B inputs, and DECOMP-2  
Ruling implemented: `JMP_S11_S12_band_edge_crossspec_correction_v1.md`

## Adjudication

The defect was cross-specification evaluation, not a globally erroneous set of cutoffs. The original S12/S8 panels correctly retain their native structural indicators at 17.5/28.5/36.5 hours. The corrected S11 evaluation view keeps the same priced nodes and all non-band columns but rebuilds the structural indicators at the S11/S10 edges, 18.5/29.5/37.5 hours. The view audit reports zero old-rule mismatches on the original panels, zero new-rule mismatches on the rebuilt panels, and bit-identical non-band columns.

Classification: **A** means generated from the correct definition for its specification and unaffected, or regenerated from the corrected S11 view. **B** means the result depended on S12-native indicators while evaluating S11 and therefore required regeneration.

| Surface or input | Before correction | Dependency class | V7 disposition | Authoritative evidence |
|---|---|---:|---|---|
| Original single-adult S12 priced panel | Native S12/S8 indicators | A | Preserved byte-for-byte; not rewritten | `MNL_posfit/outputs/band_fix_1/evaluation_view_provenance_audit_v1.json` |
| Original couple S12 priced panel | Native S12/S8 indicators | A | Preserved byte-for-byte; not rewritten | same audit |
| S11 single-adult evaluation view | S11 evaluated with S12-native indicators | B | Rebuilt at 18.5/29.5/37.5; all non-band columns identical | same audit |
| S11 couple evaluation view | S11 evaluated with S12-native indicators | B | Rebuilt at 18.5/29.5/37.5; all non-band columns identical | same audit |
| POSFIT v3 probabilities and hard predictions | Read the incorrect S11 evaluation inputs | B | Superseded by POSFIT v3b | `MNL_posfit/outputs/band_fix_1/POSFIT_v3_vs_v3b_side_by_side.md` |
| POSFIT v3 confusion, scores, calibration, simulation bands and group-rule inputs | Descended from the incorrect probabilities | B | All regenerated in `positive_fit_diagnostics_v3b` | v3b `run_provenance.json`, `artifact_hashes_v3b.csv` |
| POSFIT node-convergence v1 | Descended from the incorrect probabilities | B | Superseded by node-convergence v3b | `MNL_posfit/outputs/posfit_node_convergence_v3b/run_provenance.json` |
| S11 population-fit structural-band moments | Used the wrong structural indicators | B | Regenerated; FT uses [37.5,40.5] | `bandfix2_recompute/new_results_v1.json` |
| Independently defined descriptive hours categories | Reporting categories, not S11 regressors | A | Preserved, including the separate [36.5,37.5) 37-hour cell | `bandfix2_recompute/new_results_v1.json` |
| RUM-A estimation input | Reference-width code used 26.5 instead of 29.5 | B, disclosed limitation | Same-theta likelihood check differs only by an alternative-invariant log-density constant; estimates, standard errors and criterion are unaffected, while absolute opportunity-mass metadata are stale | `band_fix_3_rum_edge_scope_v1.json` |
| RUM-B estimation input | Does not read the affected reference-width rows | A | Estimates, standard errors and criterion unaffected; criterion-B reporting moments regenerated | same audit and `bandfix2_recompute/new_results_v1.json` |
| S10 criterion-A estimation frames | Carry their own S10 structural flags | A | Hashes unchanged | `BAND_FIX_3_verification_audit_v1.md` |
| DECOMP-2 coalition inputs | Read SHA-pinned S10 frames and their flags | A | No rerun; inputs, coalition Ginis and Shapley assets unchanged | same verification audit |
| v6 fit tables/figures and reader wording | Contained descendants of B results | B | Retired; v7 surfaces point to v3b/Band-Fix-2 only | V7 G7/G8 release gates |
| W1_F and DECOMP-2 reported numerical results | Do not reconstruct S11 indicators from S12 constants | A | Retained, with the separately required wording and scope corrections | prior ruling plus DECOMP verification audit |

## Result

No current main result remains in class B. Historical S12 artifacts remain historically correct, the superseded S11-on-S12 evaluation is retained only as an audit comparator, and every current predictive/population-fit descendant has been regenerated. DECOMP-2 passes the independent no-dependency check and was not rerun.

## RUM-A/B limitation carried into V7

RUM-A's estimation input used a 26.5-hour reference width where the S11 definition implies 29.5. At the same parameter vector this changes `log_gbar` by the global constant -0.0508559 and changes the conditional negative log likelihood by approximately 9.1e-13. The constant cancels from the conditional likelihood, so the stored estimate, standard errors and maximized criterion are unaffected. RUM-B does not read those rows. The stale absolute RUM-A opportunity-mass metadata and the fact that the downstream search was not exhaustive remain disclosed limitations; the RUM-A/B criterion-B population-fit moments shown in V7 are corrected.
