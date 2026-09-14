# JMP report V7 release record

Date: 14 September 2026  
Status: **PASS — G1–G9 and number-to-source gate**  
Accepted corrected POSFIT commit: `cd7247cf9c627b35b6b5b017be214823b77bbd13`

Canonical-notebook surface commit: `e45e36482e5f3f872494d953f4a26a23b88a7f04`

## Claim disposition

- Men's extensive accuracy is withheld for both singles and couples because the corrected statistic is quadrature-limited.
- The corrected weighted four-group adjudication is D = mechanical stochastic conditioning for all groups; E = misspecification evidence for both couple groups and inconclusive/quadrature-limited for both single groups.
- The three-group excess-predictability claim is withdrawn.
- The retired near-full-time headline is replaced by **underprediction of the observed 37-hour mass point**. Singles MAE rises slightly, so the correction is not presented as improved fit.
- DECOMP-2 is restored to the main results as a preliminary restricted P/A/B exercise; its abstract statement is qualitative and its quantitative main-text statement carries the exact scope caveat.
- Current W1_F language refers to equivalent consumption at the universally available non-employment reference. W_EA_flat is definition-only and blocked; no historical W1-EA percentage is live.
- The short-hours limitation and RUM-A/B estimation-input band defect are disclosed.

## Exact W1_F/WEA language change

Retired from current W1_F: “equivalent flat consumption level” and descriptions in which current W1_F integrates over an opportunity distribution.

Current W1_F: “The empirical Mapping-F implementation evaluates the attained bundle against the universally available non-employment reference. Under the current specification, estimated opportunity density therefore affects this money metric through attained outcomes rather than through a direct opportunity-prospect term.”

W_EA_flat is separately defined under the H-F primary domain, remains numerically blocked by support/pricing requirements including 260 couples without a priced NN state, and has no reported number.

## Build and dependency ledger

| Item | Tool/dependency | Effort/status |
|---|---|---|
| Corrected predictive evidence | POSFIT v3b and node-convergence v3b at the accepted commit | Read-only propagation; no re-estimation, no repricing |
| Population fit | Band-Fix-2 `new_results_v1.json` | Read-only propagation; descriptive 37-hour cell kept separate from structural FT |
| Report/gallery | Python builders, Pandoc HTML renderer | Rebuilt and verified |
| Notebook | Python/Jupyter nbconvert using the MNL project environment | All non-empty code cells executed; zero error outputs |
| Deck | Python figure/number builders and MiKTeX Beamer | Projected and rehearsal PDFs rebuilt; zero overfull/underfull boxes |
| Paper | V7 Python source adapter and MiKTeX/pdfLaTeX/BibTeX | 35-page PDF rebuilt; no fatal or undefined-reference errors |
| DECOMP-2 | SHA-pinned S10 criterion-A frames and accepted DECOMP assets | No-dependency audit PASS; not rerun |
| Agent | Codex | Release engineering and evidence audit; runtime model identifier is not embedded in the build artifacts |

## Surfaces and SHA-256

| Surface | Path | SHA-256 |
|---|---|---|
| report HTML | `Job_Market_paper/reports/JMP_research_story_report_v7.html` | `c4b746ad334bef8ea84b117f7a27af415c56c5f81e963475bb6812eace483fd6` |
| editable report source | `Job_Market_paper/reports/research_story_build/story_v7.generated.md` | `e49a5804b62724ef16647d748d512ec4654a1945f671ce569fad418ba4bb1ccd` |
| report section source | `Job_Market_paper/reports/research_story_build/v7_sections.py` | `e108200789ada02fa1755b2b67ee298c31bcf7e0002c8ad06445e80deca679c1` |
| report data adapter | `Job_Market_paper/reports/research_story_build/v7_render_inputs.py` | `59110b8c3c7c138a201418135e66a41b83bf9b1c54a6db00b2feca54d075744c` |
| report build entry point | `Job_Market_paper/reports/research_story_build/build_v7.py` | `c0af339ff919cb7378e3ad37e35ba202174ac140f81d4d1c38868cf4d312a171` |
| V7 number registry | `Job_Market_paper/reports/numbers_of_record_v7.json` | `d0f22fb2e38ed3097203de12d34bbc3dc686f19b90a1a4ced43467461be40123` |
| gallery HTML | `Job_Market_paper/reports/JMP_results_gallery_current.html` | `091670a78398120ed9fdc4e4738c6c341237bb92c247c5b7faa339c37fdded34` |
| gallery builder | `Job_Market_paper/reports/results_gallery_build/build.py` | `f5eab3995f2939b6d3a5589c35ff0a029dd2d8c75c96a896b08834d9fd5a7b3d` |
| gallery verifier | `Job_Market_paper/reports/results_gallery_build/verify.py` | `17a930d66f374acce4bc4a639aee3510d95d86383ecbdbc4e1803d9a9f5bcca5` |
| canonical notebook | `MNL/experiments/JMP_SEMINAR_SPRINT/JMP_canonical_AtoZ.ipynb` | `ee3f551f071fcd2d011238b04ab9291d6ed37b88e1b0d4377c73c5a310b18ab8` |
| notebook support | `MNL/experiments/JMP_SEMINAR_SPRINT/jmp_walkthrough_support.py` | `f605e9048285a2c755feaa4f5d426b58b3c6116bc689c2050d5f5ddcec15868b` |
| notebook diagnostics renderer | `MNL/experiments/JMP_SEMINAR_SPRINT/final_diagnostics_surface_v1.py` | `6f5c25250d6262d5860d6527c831274a13cac3a67d8229fd5c3140f739aa41ec` |
| notebook V7 updater | `MNL/experiments/JMP_SEMINAR_SPRINT/refresh_canonical_notebook_v7.py` | `1d20537354fb5ca64598139ff42c885b93e2df4a7435833561156120a3e20609` |
| notebook execution provenance | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/research_walkthrough/provenance_v1.json` | `6cf115dad989118808f3ed2e3ae31f0e03b1a8fc8956acdcebb0177111b8d888` |
| deck source | `Job_Market_paper/beamer/JMP_seminar_deck_r7.tex` | `ac06377ce1c60cce4053d1ec81a366a2b2caa1caad356a90faae8a921f4f77d9` |
| deck PDF | `Job_Market_paper/beamer/build/JMP_seminar_deck_r7.pdf` | `4564fe51edb2ffa64f54bd31ae347e3ce887a7cd69ede1a4bbc8c519b827abef` |
| deck rehearsal PDF | `Job_Market_paper/beamer/build/JMP_seminar_deck_r7_rehearsal.pdf` | `4d3ef59e9b800835b6e637b69da191149edca35f437ece32fe2792215e62b001` |
| deck number source | `Job_Market_paper/beamer/deck_numbers_r7.tex` | `e10ee2bdf4976d93d379d25000c23706ca7734e834ae0521b857eeecd155679b` |
| deck slide-8 figure | `Job_Market_paper/beamer/figures/r7/fitext_r7_slide.pdf` | `d1beed9eb0822800980d86490fb6ba657d77a3605926d0e2ab2aacafc042865b` |
| deck slide-9 figure | `Job_Market_paper/beamer/figures/r7/hours37_r7_slide.pdf` | `adfd8113eeba9fe9cb8264b6dda26d3f1ac6483dea6e7b531291136f30f04deb` |
| deck source manifest | `Job_Market_paper/beamer/figures/r7/r7_source_manifest.json` | `63dc166567f7af2148710b03ef6f8133544b26df8d19c86aedd745d70e87f10e` |
| versioned rehearsal pack | `Job_Market_paper/reports/rehearsal_pack_v7.md` | `11033eaad3b7bf3ae413701962f7c8fdcbb11443621a7e2412541789956c4ab5` |
| current rehearsal pack | `Job_Market_paper/reports/rehearsal_pack_v1.md` | `11033eaad3b7bf3ae413701962f7c8fdcbb11443621a7e2412541789956c4ab5` |
| paper source | `Job_Market_paper/manuscript/JMP_working_paper_for_seminar_v7.tex` | `9f2f64682657752282b13949289258254beac8114601960f15dc33aa7e775c07` |
| paper bibliography | `Job_Market_paper/manuscript/JMP_working_paper_for_seminar_v7.bib` | `627ba801b2dfba823274a2839c21e2bb34b8502b8f169c5e7fd5ac65364de18e` |
| paper PDF | `Job_Market_paper/manuscript/JMP_working_paper_for_seminar_v7.pdf` | `8353bf277f69ae685c0d5b81054944b2eb3e06a5f642a1df8d8958058495da44` |
| modular paper fit section | `Job_Market_paper/manuscript/sections/05b_fit.tex` | `28d27d71f9815b4cd83e0a031f8bba0810c75d2cd4c69c2dabaa00abda7b7163` |
| paper singles fit table | `Job_Market_paper/manuscript/tables/v7/v7_fit_singles.csv` | `cc1e77cca7c0b6480a8bb52df3a6ffb25fab869bf1c484905c5597afec7596a6` |
| paper couples fit table | `Job_Market_paper/manuscript/tables/v7/v7_fit_couples.csv` | `085dfa020ddca869131dd2ddd41f2d0d69a2a91e888ef927954c4e9cfef1c454` |
| paper benchmark table | `Job_Market_paper/manuscript/tables/v7/v7_benchmark.csv` | `c5960091727ee3ce85e31c8bc40a5185ffc9faecdb9138c324e69a3db052453c` |
| paper corrected fit figure | `Job_Market_paper/manuscript/figures/v7/fit_by_margin_v7.png` | `81e2ef7e0b464b08c5e6e3121759ce3ce9a8249c217e95866631b5b8a1682605` |
| paper corrected accuracy figure | `Job_Market_paper/manuscript/figures/v7/fitext_band_v3b.png` | `7c9b4b2565da3ea5d85b234f8b0c8604c7a4b44b12f53e9e477684d7c4458e1d` |
| paper corrected convergence figure | `Job_Market_paper/manuscript/figures/v7/node_convergence_v3b.png` | `dad3d79e4da7c4393482ae3e063ff25074690d318e98d491d4e09ca9b356e70f` |
| band-edge dependency audit | `Job_Market_paper/docs/results/JMP_V7_band_edge_dependency_audit_v1.md` | `099e4b139c2c38a8337f56d4c691a94cdf7c716d13118a2f3a469ad81e593b93` |
| fit impact/adjudication memo | `Job_Market_paper/docs/results/JMP_V7_fit_impact_and_adjudication_v1.md` | `30cf7ce5515eec9316f4deeebfd22eae0383732b2761e747651c30feb2204d1b` |
| G1-G9 checker | `Job_Market_paper/reports/check_v7_ruling_gates.py` | `2c4d232bd712045130f59613d4d070d0d9881a9569518b3dfb44a4301f7c29a5` |
| number-to-source checker | `Job_Market_paper/reports/check_v7_numbers_against_source.py` | `f8c13a2164d439fef6de948017aca762a6a6f7d0beaed4431846c7ccda268a86` |
| complete gate summary | `Job_Market_paper/reports/v7_release_gate_summary.json` | `f5a3dc31d4b686be747b23002281b92e99f9d8eea9e6bcf30b7d861e6d241568` |

The revised abstract and main-results decomposition subsection are in the editable report source and V7 paper source listed above. The dependency classification is in `docs/results/JMP_V7_band_edge_dependency_audit_v1.md`; the complete gate table is in `reports/v7_release_gate_summary.md`.
