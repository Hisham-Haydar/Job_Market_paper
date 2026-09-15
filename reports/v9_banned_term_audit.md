# V9 rendered-text banned-term audit

Overall: **PASS**

The checker reads the rendered HTML, excludes exactly the explicit marker range, strips script/style elements, base64/data URLs, image tags and all remaining tags, decodes HTML entities, and scans the resulting visible text.

## Explicit appendix boundary

- Begin: `<!-- V9_PROVENANCE_APPENDIX_BEGIN -->`
- End: `<!-- V9_PROVENANCE_APPENDIX_END -->`
- Exclusion: exactly and only the inclusive range between those markers.

## Negative control

- Injected `S11` rendered HTML immediately before the explicit appendix begin marker.
- Expected audit result: **FAIL**.
- Observed audit result: **FAIL** (1 hit).
- Temporary injected file removed: **TRUE**; original SHA-256 unchanged: **TRUE**.

## Rendered-text scan

| Surface | Begin markers | End markers | Hits outside appendix | Status |
|---|---:|---:|---:|---:|
| `reports/JMP_research_story_report_v9.html` | 1 | 1 | 0 | **PASS** |
| `reports/JMP_results_gallery_v9.html` | 1 | 1 | 0 | **PASS** |

## Term counts outside the appendix

| Banned term | Report | Gallery | Status |
|---|---:|---:|---:|
| `S10` | 0 | 0 | **PASS** |
| `S11` | 0 | 0 | **PASS** |
| `S12` | 0 | 0 | **PASS** |
| `POSFIT` | 0 | 0 | **PASS** |
| `v3b` | 0 | 0 | **PASS** |
| `DECOMP-2` | 0 | 0 | **PASS** |
| `criterion-A` | 0 | 0 | **PASS** |
| `Gate 0` | 0 | 0 | **PASS** |
| `anchor` | 0 | 0 | **PASS** |
| `node` | 0 | 0 | **PASS** |
| `proposal panel` | 0 | 0 | **PASS** |
| `exact-H` | 0 | 0 | **PASS** |
| `H-F` | 0 | 0 | **PASS** |
| `H-D` | 0 | 0 | **PASS** |
| `H-X` | 0 | 0 | **PASS** |
| `NN state` | 0 | 0 | **PASS** |
| `NN pricing state` | 0 | 0 | **PASS** |
| `SHA` | 0 | 0 | **PASS** |
| `hash` | 0 | 0 | **PASS** |
| `dwt` | 0 | 0 | **PASS** |
| `worktree` | 0 | 0 | **PASS** |
| `registry` | 0 | 0 | **PASS** |
| `G1-G9` | 0 | 0 | **PASS** |
| `adjudication` | 0 | 0 | **PASS** |
| `gate` | 0 | 0 | **PASS** |
| `mission` | 0 | 0 | **PASS** |
| `ruling` | 0 | 0 | **PASS** |
| `Mapping-F` | 0 | 0 | **PASS** |
| `MECHANICAL_STOCHASTIC_CONDITIONING` | 0 | 0 | **PASS** |

## Required before/after replacements

| Before | After |
|---|---|
| `Mapping-F attained-bundle money metric` | attained-bundle money metric |
| `Corrected POSFIT-v3b predictive evidence` | the corrected predictive-fit diagnostics |
| `the corrected S11 evaluation` | the corrected evaluation |
| `S12-native full employment-hours width` | the full employment-hours range represented in the predictive integration sample |
| `H-F domain` | the ex-ante reference keeps the full opportunity environment fixed while equalising consumption across jobs |
| `exact-H pre-validation` | additional counterfactual tax-benefit evaluations are required before the ex-ante measure can be reported reliably |
| `dwt-weighted` | household-weighted |
| `the estimation panel's anchor node` | the household's own observed job, which the simulation always includes |
| `MECHANICAL_STOCHASTIC_CONDITIONING` | the pattern is a mechanical consequence of conditioning on realised outcomes under stochastic choice |
| `V7 status note` | deleted from the report; the status statement uses the required ongoing-validation wording and names no version |
