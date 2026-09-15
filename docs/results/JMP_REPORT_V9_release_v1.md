# JMP report V9-WEA release record

Status: **PASS**

Report HTML SHA-256: `f921f25afe9fb2a1a0c3dcdbf75ec2e25cec7ef420a1a880d87a1b09f98cd365`

## Reader-facing release

- Exact title: *Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition*.
- The main text restores the utility model, opportunity density, estimation criterion, maintained separation assumptions, both welfare derivations, and the structural operators.
- The attained-bundle perspective values the realised job; the ex-ante perspective values the whole job prospect. Neither is designated primary.
- Earning opportunities dominate attained-bundle accounting. For single-adult households, access is about three times earnings in ex-ante accounting.
- Ex-ante access plus earnings is 7.9-21.3% of its own baseline Gini. For couples, equivalisation moves the share from 21.3% to 7.9% and turns the preference contribution negative; no directional preference claim is made.
- Earlier figures near 90% covered all non-preference circumstances, including household resources and composition, and are not comparable with the current restricted results.
- The implementation, certification and provenance record remains within the single collapsed appendix. V8 was not overwritten.
- The welfare branch was published as a focused snapshot because an unrelated oversized blob in its local ancestral history cannot pass GitHub's file-size limit; the certified result and notebook contents are unchanged apart from line-ending normalization in the published snapshot.

## Verification records

- Banned-term rendered-text scan: `reports/v9_banned_term_audit.md`
- Banned-term negative control: `reports/v9_banned_term_negative_control.md`
- Number-to-source checks: `reports/v9_number_to_source_results.md`
- Reader/economics checks: `reports/v9_reader_gate_results.md`
- Complete release suite: `reports/v9_release_gate_summary.md`

## Tool and dependency ledger

| Work item | Tool or dependency | Status |
|---|---|---|
| Narrative and equations | Python section source and Pandoc/MathJax rendering | Complete |
| Certified ex-ante evidence | Stage-4 result record and memo | Read-only propagation; all declared checks passed |
| Decks | LaTeX build plus rendered-text verification | Main and rehearsal PDFs built without box warnings |
| Notebook | Executed canonical notebook with source-linked comparison table | No error outputs; synchronized |
| Visual inspection | Offline browser and PDF rendering | Report, gallery and comparison slide inspected |
| Validation | Language, negative control, number lineage, rendering, synchronization and V8 regression | All PASS |

## Surfaces and SHA-256

| Surface | Path | SHA-256 |
|---|---|---|
| report HTML | `Job_Market_paper/reports/JMP_research_story_report_v9.html` | `f921f25afe9fb2a1a0c3dcdbf75ec2e25cec7ef420a1a880d87a1b09f98cd365` |
| editable resolved Markdown | `Job_Market_paper/reports/research_story_build/story_v9.generated.md` | `4c1da8804b0a8a8bc3e284c43b06971c883598e04faf64f74e07e984b8a16ecb` |
| editable section source | `Job_Market_paper/reports/research_story_build/v9_sections.py` | `f261951391cc1a33321fc80c93258b89266ef66ca120494a76adfd6cb635157f` |
| numerical input adapter | `Job_Market_paper/reports/research_story_build/v9_render_inputs.py` | `494109dc6f2ea2845032197d337b8565fa421488c5ed7950479e3567bd648a61` |
| report builder | `Job_Market_paper/reports/research_story_build/build_v9.py` | `c8f24d7df70175b500256a702c9ae028a1bc4e0f7b704447c4b382cf2809936a` |
| V9 numerical registry | `Job_Market_paper/reports/numbers_of_record_v9.json` | `ddd7f4f9c44747438532de1808bf7390e3615547832b8810a070ddd7f765851c` |
| reader-facing gallery | `Job_Market_paper/reports/JMP_results_gallery_v9.html` | `c54f28b8284582bc95bff4fee6d02bf90cd0bdfca894f37be3ed7b65c4b21948` |
| gallery builder | `Job_Market_paper/reports/results_gallery_build/build_v9.py` | `6e55ad8d0ad156515f861b27f6ef5ca5c1eed049b7601883428eb9739588783a` |
| deck source | `Job_Market_paper/beamer/JMP_seminar_deck_r9.tex` | `7625ddb9b707af8180d512ff1a519f1f03de9c742337f8c4d85865ff46922fa4` |
| rehearsal deck source | `Job_Market_paper/beamer/JMP_seminar_deck_r9_rehearsal.tex` | `9a5fdfbc43b46bd9df383caf6c6cb0b2046bd1ac6c3ced02acf7940d46d48159` |
| deck numerical macros | `Job_Market_paper/beamer/deck_numbers_r9.tex` | `732e7e8cbca2b74026eeaf9efe89fee8c05a375738fc9b13fcaba39c228d4b96` |
| deck macro generator | `Job_Market_paper/beamer/make_deck_numbers_r9.py` | `658f85dc996470f747dcd83c3b5f2004c9ba10a0eadcb64ebc23c6f3fb138c8e` |
| deck preparation script | `Job_Market_paper/beamer/prepare_deck_v9.py` | `c0e6650c0b712765f8659b1e7b1d3dfc3414e99f771b146106892ed651f06964` |
| deck builder | `Job_Market_paper/beamer/build_deck_r9.py` | `b28ded49268f034ee948627b532425a90370c663db21c2f7854174f360064b84` |
| deck verifier | `Job_Market_paper/beamer/verify_deck_r9.py` | `c96fa0222a5bdf13eb23524fcfda9c78ecda4c8b3419e9df8553dd7485e50b8b` |
| presentation PDF | `Job_Market_paper/beamer/build/JMP_seminar_deck_r9.pdf` | `8e9cf03198c5097f4d209b6f60de211ae93d2d9ab614f0e6cf220f09cb08970d` |
| rehearsal PDF | `Job_Market_paper/beamer/build/JMP_seminar_deck_r9_rehearsal.pdf` | `8f8a8483674ea854024baf6becb97b1727988aaf7ac7dee15849cd6d87d79ff7` |
| presentation rendered text | `Job_Market_paper/beamer/build/JMP_seminar_deck_r9_text.txt` | `f9f00e251b5a19955f21792fc16e6c7a134d07cff53c9754fac8966f1531329e` |
| rehearsal rendered text | `Job_Market_paper/beamer/build/JMP_seminar_deck_r9_rehearsal_text.txt` | `4edb5f77ebe09029d05801ff38e0db878ae3b6fcc338606ac33de192d3638d38` |
| rehearsal script | `Job_Market_paper/reports/rehearsal_pack_v9.md` | `1fa168634fa874031ba09ba2fffc1a4b655d7c856602edbe2f811d3fa3c21147` |
| rehearsal-script builder | `Job_Market_paper/beamer/build_rehearsal_script_v9.py` | `c3ac6371195886aa717741886f83faa57c01a9391b8bb26e440c55f7dbf98bf8` |
| executed canonical notebook | `MNL_wea/experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb` | `439e8f3d3c1309f92316136af22fd3803a731e27d90239d1143e7d5660024f63` |
| notebook updater | `MNL_wea/experiments/JMP_SEMINAR_SPRINT/refresh_canonical_notebook_v9.py` | `c6229a850a7bf15888f86360dc1bb84a6f6770da7397c81bfb8d53604b54629d` |
| notebook verifier | `MNL_wea/experiments/JMP_SEMINAR_SPRINT/verify_canonical_notebook_v9.py` | `2ce6c287c7df6aff0a049f7e43a5ad9c02252358d8bf377eb40dc3e38251716b` |
| reader and economics checker | `Job_Market_paper/reports/check_v9_reader_gates.py` | `b54555667347aa5dad166f09c7b945431bd44d6708e7560206e1b86ad76208b1` |
| rendered-language checker | `Job_Market_paper/reports/check_v9_rendered_language.py` | `4eb22b6551ca608f8e77465e76717434c63bc09133bc4e61ebba8f846eafc7dc` |
| number-to-source checker | `Job_Market_paper/reports/check_v9_numbers_against_source.py` | `e1f890958b60577b9cd258b17004875fe6fb1c487955fbe6868c6c4f9d6045a5` |
| cross-surface checker | `Job_Market_paper/reports/check_v9_synced_surfaces.py` | `5c6ab964d4a217a8d1f640a2c998d7d9605569c57018ab2541734381fa35b5cd` |
| offline render checker | `Job_Market_paper/reports/research_story_build/check_v9_render.py` | `7962ab3606daee85b8e8f4f556d10d44e962c3f5c9c772dd7d0341757b3356bb` |
| release-suite runner | `Job_Market_paper/reports/run_v9_release_gates.py` | `c36fd0155c7a594d8f508472bf6b5a56131cbac3e99b7d12f48d809aded5419a` |
| release-manifest writer | `Job_Market_paper/reports/write_v9_release_manifest.py` | `72c289eeb049047c90313f9f2b66a619aed70925fcd944b477b8cad361af5e4f` |
| banned-term audit | `Job_Market_paper/reports/v9_banned_term_audit.md` | `1a1cb48047d832eabd346c7a4bbbad790bcfced16f11d45499966ce80832a6bc` |
| banned-term negative control | `Job_Market_paper/reports/v9_banned_term_negative_control.md` | `d9bf38e69adda271381bd1f2c8252bd4afb52684df399bde00523adb209baf21` |
| number-to-source results | `Job_Market_paper/reports/v9_number_to_source_results.md` | `ff8e1ca92a2527ec3e4f31acb8cb01d85498b02c937ede2dbdfb93b0ebe48f5e` |
| reader gate results | `Job_Market_paper/reports/v9_reader_gate_results.md` | `d27bc3339205c64987f05b64c928e7630f9562aa8f6b094c1657a27da086b10c` |
| render gate results | `Job_Market_paper/reports/v9_render_gate.json` | `4909d5661336c341706a8c9754e3d1fb46ae7e6e31e3494267ce955f22bd28a7` |
| complete gate summary | `Job_Market_paper/reports/v9_release_gate_summary.md` | `29e7ba8b0a044a58663bdfb9cd48781919e432bfbbde624843cb1ef396dafcca` |

## Numerical evidence

| Source | Path | SHA-256 |
|---|---|---|
| certified ex-ante result record | `MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json` | `5923e62d16cf11f22b2b92608a0f20ceac3fcfcaeb5d44afc8a9c8f8bd021898` |
| certified ex-ante result memo | `MNL_wea/docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md` | `c3a52b1b48732faff62f11d07aafcaa79a88e287fed72e6727d00425b47d5e86` |
| attained-bundle decomposition record | `MNL_decomp/outputs/welfare/preseminar_pab_v1/preseminar_pab_record_v1.json` | `bcbe4b6fc742daa39535d5c3eb03bda0641055a9f5e851b4f53f62fa3e612011` |
| corrected prediction ranges | `MNL_posfit/outputs/positive_fit_diagnostics_v3b/model_simulated_bands.csv` | `cbc827e76357503265a315bf1945f53eee51c76f41ac4843634abd7bdd7f418e` |
