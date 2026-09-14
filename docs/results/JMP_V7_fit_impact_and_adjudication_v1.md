# V7 corrected fit impact and adjudication

Date: 14 September 2026  
Corrected diagnostic bundle: POSFIT v3b, commit `cd7247cf9c627b35b6b5b017be214823b77bbd13`  
Population moments: Band-Fix-2 `new_results_v1.json`

No estimate was refit and no state was repriced. POSFIT probabilities were fully re-evaluated after rebuilding the S11 structural indicators on the already-priced S12 nodes.

## Compact impact table

| Item | Superseded | Corrected | Classification |
|---|---:|---:|---|
| Single men, weighted extensive accuracy | 87.12% | 86.41%; **WITHHELD**, adequacy ratio 0.3607 | MODIFIED |
| Single women, weighted extensive accuracy | 85.48% | 85.68%; 95% simulation band [80.02,85.86], ratio 0.0961 | MODIFIED |
| Coupled men, weighted extensive accuracy | 92.30% | 92.20%; **WITHHELD**, ratio 0.3527 | MODIFIED |
| Coupled women, weighted extensive accuracy | 89.80% | 89.80%; band [88.12,91.23], ratio 0.0491 | MODIFIED |
| Coupled-men numerical adequacy | 0.2398, ADEQUATE | 0.3527, QUADRATURE-LIMITED | MODIFIED |
| Single men, weighted intensive accuracy | 64.85% | 65.05% | MODIFIED |
| Single women, weighted intensive accuracy | 57.20% | 56.63% | MODIFIED |
| Coupled men, weighted intensive accuracy | 62.73% | 62.80% | MODIFIED |
| Coupled women, weighted intensive accuracy | 61.00% | 60.98% | UNCHANGED substantively |
| Singles population-moment MAE | 0.01287 over 34 moments | 0.01400 over 36 moments | MODIFIED; rises slightly |
| Couples population-moment MAE | 0.01357 over 28 moments | 0.01185 over 30 moments | MODIFIED |
| Single-men structural FT gap | -9.48 pp | +4.29 pp | MODIFIED; old headline retired |
| Single-women structural FT gap | old definition | -2.74 pp | MODIFIED |
| Coupled-men structural FT gap | old definition | +0.54 pp | MODIFIED |
| Coupled-women structural FT gap | -7.21 pp | +0.70 pp | MODIFIED; old headline retired |
| 37-hour observed-minus-predicted gap | not isolated | +5.19, +3.81, +4.41, +6.51 pp for single men, single women, coupled men, coupled women | NEW diagnostic |
| “near-full-time underprediction” claim | live | **WITHDRAWN** | WITHDRAWN |
| Three-group excess-predictability claim | live | **WITHDRAWN** | WITHDRAWN |

The full old-versus-corrected score, Brier, log-score, calibration, confusion-matrix and hours-state bridge is `MNL_posfit/outputs/band_fix_1/posfit_v3_vs_v3b_all_quantities_long.csv`; its readable companion is `POSFIT_v3_vs_v3b_side_by_side.md`. Those files, not this compact presentation table, are the exhaustive impact record.

## Four-group corrected weighted adjudication

| Group | Conditioning verdict (D) | Excess-dispersion verdict (E) | Extensive accuracy display |
|---|---|---|---|
| Coupled men | MECHANICAL_STOCHASTIC_CONDITIONING | MISSPECIFICATION_EVIDENCE | WITHHELD: quadrature-limited |
| Coupled women | MECHANICAL_STOCHASTIC_CONDITIONING | MISSPECIFICATION_EVIDENCE | 89.80%, reportable |
| Single men | MECHANICAL_STOCHASTIC_CONDITIONING | INCONCLUSIVE_QUADRATURE_LIMITED | WITHHELD: quadrature-limited |
| Single women | MECHANICAL_STOCHASTIC_CONDITIONING | INCONCLUSIVE_QUADRATURE_LIMITED | 85.68%, reportable |

Numerical adequacy of an individual displayed statistic and the composite D/E adjudication are distinct gates. The threshold remains 0.25 and was not changed.

## Reader-facing finding

The remaining common mismatch is **underprediction of the observed 37-hour mass point**, by 3.8–6.5 percentage points across the four groups. The point lies outside the S11 structural FT band [37.5,40.5]. The correction is not described as improved fit: singles MAE rises slightly.
