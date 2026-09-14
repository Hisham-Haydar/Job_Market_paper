# JMP report V8 reader-facing release record

Status: **PASS**

Report HTML SHA-256: `fd644010e23caa895d517058d40d994accfc5886263682bcc23aec24be8cac13`

## Reader-facing changes

- The abstract is the authorised magnitude paragraph, including 1.8–9.9%.
- The main report follows the seven-part economic sequence from motivation through the ex-ante extension.
- The full numerical Shapley allocation remains in the main results with the restricted-exercise caveat.
- Corrected predictive evidence is retained: coupled men's extensive accuracy is WITHHELD, the 37-hour mass-point finding remains explicit, and short-hours coverage remains a limitation.
- The ex-ante section is the authorised single paragraph. No historical ex-ante percentage is reported.
- Detailed predecessor sections and the implementation record are preserved in one explicitly marked, collapsed provenance appendix; the predecessor abstract and status note are omitted, and V7 files were not overwritten.

## Release records

- Banned-term deletion/replacement audit: `reports/v8_banned_term_audit.md`
- Banned-term negative control: `reports/v8_banned_term_negative_control.md`
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
| report HTML | `Job_Market_paper/reports/JMP_research_story_report_v8.html` | `fd644010e23caa895d517058d40d994accfc5886263682bcc23aec24be8cac13` |
| editable resolved Markdown | `Job_Market_paper/reports/research_story_build/story_v8.generated.md` | `173160ca370c83caed30049d5819826a59e4e6ee58210461b62b1e902f09de1f` |
| editable section source | `Job_Market_paper/reports/research_story_build/v8_sections.py` | `4c9c24cbe66df91d4457923ed99d8d0fae292f68fd36731d1f14f26ba7d15b64` |
| numerical input adapter | `Job_Market_paper/reports/research_story_build/v8_render_inputs.py` | `fcb96234ce9479dd45e73a2210702578f3c89b8e51fa93d93ef90daf55c22495` |
| report builder | `Job_Market_paper/reports/research_story_build/build_v8.py` | `88a47da913fd1a1afff7cae6cf0ae2cef3f836a7e21e10c6c8b500ddd4af2311` |
| V8 numerical registry | `Job_Market_paper/reports/numbers_of_record_v8.json` | `e97ea73d6cf1327fdef3c0a309bcd46e0fa125951ff9d1f46b64a6e6ab645244` |
| reader-facing gallery | `Job_Market_paper/reports/JMP_results_gallery_v8.html` | `4e91b8252c210ef32c2d9ddb394fd7d0706815c8051ce0cbcd5299287856a54d` |
| gallery builder | `Job_Market_paper/reports/results_gallery_build/build_v8.py` | `b30a5b77bb39e23428245852b33df3aac061432f7b02cc277c9bfc55dd3271ec` |
| reader-language checker | `Job_Market_paper/reports/check_v8_reader_gates.py` | `3e39bbabf03eec5421b8029205610fa76a099fd63e34844a7c83b1e47d74ad34` |
| rendered-language checker | `Job_Market_paper/reports/check_v8_rendered_language.py` | `8b69afc3b548286b79d6457b53fb2ff029a3ac3c0b430920393dfa8491ff83c5` |
| number-to-source checker | `Job_Market_paper/reports/check_v8_numbers_against_source.py` | `e2cf22e176f618f105e1dcb1287ab1dd476b549b9bbc872d1d855b85c8b3fab0` |
| offline render checker | `Job_Market_paper/reports/research_story_build/check_v8_render.py` | `f9b8f9c5be9dca95905bc7153733edf5fd5e6beb7c603d11ea15a4499522b480` |
| release-suite runner | `Job_Market_paper/reports/run_v8_release_gates.py` | `bcbe0b2865d360b429564340cf6d10d48b549809441edd1cadf021407ef26456` |
| release-manifest writer | `Job_Market_paper/reports/write_v8_release_manifest.py` | `d1d59094dcafcd76ec1b3aa7b25a9e1a8abcc05b9017da62cc7fc42672e92d71` |
| banned-term audit | `Job_Market_paper/reports/v8_banned_term_audit.md` | `ec438b32ecc87bd9e98ec599f073b6f8e8177eabca661beee3af98f4cb87ed50` |
| banned-term negative control | `Job_Market_paper/reports/v8_banned_term_negative_control.md` | `3d7cd6bb09941d8b8a9ee40ca087f1d73743d2cbe4a6c0a08a0558e6745bf006` |
| section map | `Job_Market_paper/reports/v8_section_map.md` | `87a35e97f0c155f6cd1e8d68fb2186f63e7d8547e7f8ed595da9a8532db23f64` |
| number-to-source results | `Job_Market_paper/reports/v8_number_to_source_results.md` | `4249c6956b1ec9df6c702a0013791adf105743ede07dc71f086c531f7883b695` |
| reader gate results | `Job_Market_paper/reports/v8_reader_gate_results.md` | `a9cac5c944e1d89378dadda12a9ccdbf3ead38968581f385eb48ec2724cab1be` |
| render gate results | `Job_Market_paper/reports/v8_render_gate.json` | `faffae50758fed735b6c0fee3e0dcfb5d3f57ed92d11179a545b3499425f643e` |
| complete gate summary | `Job_Market_paper/reports/v8_release_gate_summary.md` | `1712bbd72405ffeacfcf8935ef610d585b06fcf8913373721540d709bdcacae1` |
| authorisation source | `Job_Market_paper/docs/JMP_preseminar_reader_facing_and_WEA_pricing_authorization_v1.md` | `d5fb98c82b0a3a1ab708831a278b1c8cb4d34527010916cd94c3f4511b7f33c0` |

## Numerical evidence

| Source | Path | SHA-256 |
|---|---|---|
| corrected prediction ranges | `MNL_posfit/outputs/positive_fit_diagnostics_v3b/model_simulated_bands.csv` | `cbc827e76357503265a315bf1945f53eee51c76f41ac4843634abd7bdd7f418e` |
| corrected numerical precision | `MNL_posfit/outputs/positive_fit_diagnostics_v3b/g2_adequacy.csv` | `304b7af652118d64df9f5862d3c1af42fe91dad642d768487d6bcaf03b7369af` |
| corrected population moments | `MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/bandfix2_recompute/new_results_v1.json` | `e75ff27c6e324e332231f29a60282b742ab6114bd1f4b6f60afea3fa98977d12` |
| decomposition record | `MNL_decomp/outputs/welfare/preseminar_pab_v1/preseminar_pab_record_v1.json` | `bcbe4b6fc742daa39535d5c3eb03bda0641055a9f5e851b4f53f62fa3e612011` |
