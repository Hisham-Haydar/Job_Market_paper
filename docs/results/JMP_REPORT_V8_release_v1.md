# JMP report V8 reader-facing release record

Status: **PASS**

Report HTML SHA-256: `059e073160de188c8f823936199eb609c46f3d7551a3467add94a7a9c57db1c4`

## Reader-facing changes

- The abstract is the authorised magnitude paragraph, including 1.8–9.9%.
- The main report follows the seven-part economic sequence from motivation through the ex-ante extension.
- The full numerical Shapley allocation remains in the main results with the restricted-exercise caveat.
- Corrected predictive evidence is retained: coupled men's extensive accuracy is WITHHELD, the 37-hour mass-point finding remains explicit, and short-hours coverage remains a limitation.
- The ex-ante section is the authorised single paragraph. No historical ex-ante percentage is reported.
- The complete V7 text and implementation record are preserved in one collapsed provenance appendix; V7 files were not overwritten.

## Release records

- Banned-term deletion/replacement audit: `reports/v8_banned_term_audit.md`
- V7-to-V8 section map: `reports/v8_section_map.md`
- Complete checks: `reports/v8_release_gate_summary.md`
- Number-to-source checks: `reports/v8_number_to_source_results.md`

## Tool, model, effort and dependency ledger

| Work item | Tool/model or dependency | Effort and status |
|---|---|---|
| Narrative rebuild | Codex; runtime model identifier is not embedded in repository artifacts | Seven main sections rewritten and reviewed; complete |
| HTML generation | Python, pypandoc/Pandoc, vendored MathJax | Report and gallery built offline; complete |
| Numerical evidence | Accepted V7 registry plus the corrected predictive-fit and decomposition artifacts listed below | Read-only propagation; no value changed |
| Visual inspection | Playwright with local Microsoft Edge | Report and gallery rendered offline at desktop width; complete |
| Validation | Reader-language, number-to-source, render, V7 regression and source-compilation checks | All PASS |
| External services | None | No network data or external model dependency used |

## Surfaces and SHA-256

| Surface | Path | SHA-256 |
|---|---|---|
| report HTML | `Job_Market_paper/reports/JMP_research_story_report_v8.html` | `059e073160de188c8f823936199eb609c46f3d7551a3467add94a7a9c57db1c4` |
| editable resolved Markdown | `Job_Market_paper/reports/research_story_build/story_v8.generated.md` | `e3a69a127b616ef30b2e843f4d0a456b6e1996982399191ab16fec9bd23ade50` |
| editable section source | `Job_Market_paper/reports/research_story_build/v8_sections.py` | `5fdd65549e645a5c8d63d3e3c6db1046759accc7c2f9f57f77fa00199993de47` |
| numerical input adapter | `Job_Market_paper/reports/research_story_build/v8_render_inputs.py` | `fcb96234ce9479dd45e73a2210702578f3c89b8e51fa93d93ef90daf55c22495` |
| report builder | `Job_Market_paper/reports/research_story_build/build_v8.py` | `e1e24fbfb846224ea32870afaffc5962fe8224e71cce382cd381e957be8f1899` |
| V8 numerical registry | `Job_Market_paper/reports/numbers_of_record_v8.json` | `e97ea73d6cf1327fdef3c0a309bcd46e0fa125951ff9d1f46b64a6e6ab645244` |
| reader-facing gallery | `Job_Market_paper/reports/JMP_results_gallery_v8.html` | `720688bf7aa1398950649804b04e4a7de84924fc529c80b51b77d99324d3de63` |
| gallery builder | `Job_Market_paper/reports/results_gallery_build/build_v8.py` | `1234415d354ecae58d3fff5c2915828cb21adc18c1c823833b7f18cd3c10a785` |
| reader-language checker | `Job_Market_paper/reports/check_v8_reader_gates.py` | `e2369434441d782811620ab0cec98133c0a57b1eee047f85c2f75127fafa4669` |
| number-to-source checker | `Job_Market_paper/reports/check_v8_numbers_against_source.py` | `142b527d2a5fa803142bba2c022e21a8d1c18bd9f20d7cdc51457c03ff0301ef` |
| offline render checker | `Job_Market_paper/reports/research_story_build/check_v8_render.py` | `f9b8f9c5be9dca95905bc7153733edf5fd5e6beb7c603d11ea15a4499522b480` |
| release-suite runner | `Job_Market_paper/reports/run_v8_release_gates.py` | `2c215ab90085a899da07418d52ad8f262788dd7156c7bc8af66e8796652c583b` |
| release-manifest writer | `Job_Market_paper/reports/write_v8_release_manifest.py` | `e0b24e53a11510869bb4bca88c618a58683824bc374fa3f62b5a8c7e1d022e0c` |
| banned-term audit | `Job_Market_paper/reports/v8_banned_term_audit.md` | `28f923f413748b83391f661aebe2605ff1fc7759351bfa2141d252cee660baeb` |
| section map | `Job_Market_paper/reports/v8_section_map.md` | `620a53e76430337128a706ef7d7a784a93e742b6dc7d78269ab121a331db398a` |
| number-to-source results | `Job_Market_paper/reports/v8_number_to_source_results.md` | `4249c6956b1ec9df6c702a0013791adf105743ede07dc71f086c531f7883b695` |
| reader gate results | `Job_Market_paper/reports/v8_reader_gate_results.md` | `d7c598f02d3cc59cad27574b3f8df6f9ab12c5d455f397dc7f9434d13d51f043` |
| render gate results | `Job_Market_paper/reports/v8_render_gate.json` | `db357ce6b0950e432f18be4d504d5853c5532bb0af4184f2f1301a77bd72d468` |
| complete gate summary | `Job_Market_paper/reports/v8_release_gate_summary.md` | `329a92d1b5b87b441557fafba8cecae8f1ef9b996671f389c4d7a18cba48e27a` |
| authorisation source | `Job_Market_paper/docs/JMP_preseminar_reader_facing_and_WEA_pricing_authorization_v1.md` | `d5fb98c82b0a3a1ab708831a278b1c8cb4d34527010916cd94c3f4511b7f33c0` |

## Numerical evidence

| Source | Path | SHA-256 |
|---|---|---|
| corrected prediction ranges | `MNL_posfit/outputs/positive_fit_diagnostics_v3b/model_simulated_bands.csv` | `cbc827e76357503265a315bf1945f53eee51c76f41ac4843634abd7bdd7f418e` |
| corrected numerical precision | `MNL_posfit/outputs/positive_fit_diagnostics_v3b/g2_adequacy.csv` | `304b7af652118d64df9f5862d3c1af42fe91dad642d768487d6bcaf03b7369af` |
| corrected population moments | `MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/bandfix2_recompute/new_results_v1.json` | `e75ff27c6e324e332231f29a60282b742ab6114bd1f4b6f60afea3fa98977d12` |
| decomposition record | `MNL_decomp/outputs/welfare/preseminar_pab_v1/preseminar_pab_record_v1.json` | `bcbe4b6fc742daa39535d5c3eb03bda0641055a9f5e851b4f53f62fa3e612011` |
