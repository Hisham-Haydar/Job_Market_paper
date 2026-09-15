# JMP — V11 to V12 structural release, v1

Structural edit only: no estimation, pricing, welfare or decomposition was
rerun. `numbers_of_record_v12.json` equals `numbers_of_record_v11.json` on
every key. V9, V10 and V11 are byte-preserved; the matched-household figure and
record are byte-identical to the V11 manifest.

## 1. Counts (rendered text; bibliography excluded)

| Surface | Version | Body words | Appendix words | Body figures | Appendix figures | Body tables | Appendix tables | Size |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Report | V11 | 10,579 | 21,640 | 9 | 19 | 11 | 25 | 10.07 MB |
| Report | **V12** | **12,817** | **3,009** | **10** | **2** | **17** | **3** | **5.20 MB** |
| Gallery | V11 | 6,068 | 11,232 | 11 | 9 | 13 | 46 | 5.90 MB |
| Gallery | **V12** | **7,072** | **8,519** | **12** | **5** | **16** | **38** | **4.65 MB** |

Report appendix / body = 0.23. The gallery appendix is 915 words of prose; the
rest is the cells of 38 predictive-fit diagnostic tables (confusion matrices,
calibration, simulated benchmarks), which a reader consults only when checking
implementation.

## 2. Deletion and promotion log (report)

Rule applied: if the body covers it, the appendix copy is deleted; if the
appendix copy carries analysis the body lacks, that analysis is moved up and
the appendix copy deleted. Nothing is kept twice.

| Appendix section in V11 | Decision | Reason |
|---|---|---|
| Technical record: Introduction (1,932 words, theory figure) | Deleted | Section 1 covers the argument; the copy carried own-set/Haydar–Maniquet framing and the superseded ex-ante status (kept once in the historical statements). |
| Technical record: Data (heading only) | Deleted | Empty wrapper. |
| The estimation samples | Deleted (body kept) | Identical text and table in Section 2. |
| What the households look like | Deleted (body kept) | Identical in Section 2. |
| Observed raw labour-force status (appears twice: inside the data copy and as an implementation record) | **Promoted** to Section 2, both appendix copies deleted | It is a descriptive result. The body version is rewritten without join code names; the table is unchanged. |
| The household budget | Deleted (body kept) | Identical in Section 2. The accounting-identity sentence stays in the appendix estimation record. |
| Technical record: A latent-jobs model (heading only) | Deleted | Empty wrapper. |
| Preferences | Deleted (body kept) | Equation A covers it with reason, meaning and use; the leisure-scaling exercise stays in the appendix as a diagnostic. |
| Opportunities | Deleted (body kept) | Equation C covers it; the copy also carried an obsolete matched-pair disclaimer. |
| Identification, in words | Deleted (body kept) | Near-identical to the body section. |
| Estimation | Deleted | Duplicated the implementation record. The body keeps "Estimation, in words"; the appendix keeps the likelihood and optimiser detail once. |
| Money-metric well-being record (W1_F construction, reference and pay, worked illustration, interpersonal comparison) | Deleted | Section 3 covers ATT, the staying-home coincidence and interpersonal comparison; the copy used superseded labels. |
| The distinct ex-ante opportunity-prospect metric | Deleted; quotation kept once in the historical statements | Superseded status. |
| Behavioural estimates | Deleted (body kept) | Identical tables and figures in Section 5. |
| Fit (band figure, convergence figure, adequacy ratios) | Split | Band figure: already in body. Integration-convergence figure and adequacy ratios: kept in appendix as numerical-precision diagnostics. |
| The full margin-by-margin comparison | **Promoted** to Section 5 | Both fit tables, benchmark table, fuller benchmark paragraph and group-specific verdict are results. |
| Implementation record: population-fit moments (V11) | Deleted | Superseded by the promotion. |
| Within-sample equivalised results | **Merged** into Section 5 | Same table as the body's attained-bundle well-being table; its one extra point (not a welfare-loss index, what the gap reflects) moved up. |
| Preliminary restricted structural decomposition (1,619 words, 3 figures, 3 tables) and its duplicate "Coalition values and signed allocation" in Appendix D | **Promoted** coalition tables, variance statement and robustness to Section 5; prose, the architecture figure and both decomposition figures deleted | The prose duplicated Section 5. The three figures embed internal labels and the outdated access definition (region, urban/rural, year) inside the image, so moving them up would have put that defect in the body. Their values are all in the body tables. |
| Two open econometric questions | Deleted (body kept) | Section 6 "Maintained econometric assumptions" covers both. |
| Limitations | **Merged** into Section 6 | Time-endowment sensitivity paragraph and figure promoted. The men's extensive-accuracy paragraph and the adjudication labels duplicated body text and were dropped. No second limitations section. |
| What is not established | **Merged** into Section 6 | Causal scope and short hours were already covered. The benchmark input defect is promoted in plain language. The superseded ex-ante status goes to the historical statements. |
| Technical record: Conclusion | Deleted | V7-era conclusion with superseded framing; the body's results and limits replace it. |
| Appendix A. Estimated parameter vectors | Kept | Parameter code names and full coordinate tables; restriction list kept here once. |
| Appendix B. Inequality indices and allocation rule | Deleted | Equation H covers the Shapley rule. |
| Appendix C. Data, software and replication | Kept, shortened | Provenance and replication; the superseded "own-set" wording removed. |
| Appendix D preamble | Split | The status sentence goes to the historical statements. The wage-location boundary (0.10 vs 0.37 log points) is **promoted** to Section 6. |
| Counterfactual operators and simulation rule | Rewritten as a short implementation record | Game and operator definitions duplicated Section 4. The simulation device (weighted-mean substitution, Gumbel-max under common random numbers, 1,000 replications, second seed, closure) stays. The operator table, whose access row was wrong, is deleted. |
| Equivalization and the preliminary decomposition; Interpretation of the restricted results | Deleted | Sections 3 (F), 5 and 6 cover both. |
| Research notebook; Scientific history | Deleted | Project history, not implementation. |
| Technical presentation-preparation questions 1–26 | Deleted; Q26 kept once as a historical statement | Every other answer restates body content. |
| Implementation record: estimation / matched-household method / certified ex-ante calculation | Kept | Implementation only. |

**Gallery.** Removed from the appendix:
- the counterfactual-decomposition record: its prose duplicated the body, and its three figures carry the same baked-in labels;
- the robustness, scope, short-hours, benchmark-defect and wage-elasticity boxes, which duplicate report Sections 5–6;
- the time-endowment block, which is now in the body through Section 6.

Promoted: the variance-accounting table, into the decomposition panel, with its stale `W1_F` column label replaced.

Kept in the appendix:
- the predictive-fit matrices and calibration;
- integration convergence;
- the leisure-normalisation exercise;
- the superseded ex-ante status box as a labelled historical statement.

## 3. Defect fixes

**(a) Access cell.** The attained-bundle Shapley table's four access rows now read "Local unemployment exposure, region, urban or rural location, and year".

Before editing, I checked this against the executed decomposition record, not only the V11 text. `MNL_decomp/outputs/welfare/preseminar_pab_v1/preseminar_pab_record_v1.json` lists `gsur` (local unemployment exposure) among the substituted covariates of every coalition containing A, for both samples. That record's own `factor_labels` and `A_definition_note` still say "region, urban/rural, year", so the label there is inconsistent with its execution. It is not edited here; it is flagged for the owner of that record.

The inherited operator table, which listed group unemployment as *retained*, was also wrong. It is deleted.

**(b) Stage A misses carried forward.** The historical-statements section opens with the superseded label, then quotes:
- the paragraph formerly printed under "Numerically blocked opportunity-prospect metric" (heading named after the label);
- the Q26 answer;
- the "A separately defined ex-ante metric is being reconstructed" sentence.

The Stage A status gate finds 7 stale occurrences in the report and 3 in the gallery, 0 unlabelled.

## 4. File size

The report fell from 10.07 MB to 5.20 MB through deletion of duplicated figures alone. The remainder is:

| Component | Size |
|---|---:|
| 12 embedded PNG figures | 2.93 MB |
| Embedded MathJax script | 2.11 MB |
| Text and markup | 0.16 MB |

- **Reducing resolution does not help.** Downscaling these line-art figures to 1,800 px (twice the display column) makes them **larger**, 4.58 MB, because resampling adds antialiasing noise that PNG compresses poorly. It would also risk legibility of small-text panels.
- **Lossless re-encoding does not help:** 3.12 MB.
- **A 256-colour palette at full resolution** cuts the figures to 1.10 MB, saving 1.8 MB. The mean channel difference is 0.02 on 0–255, and a side-by-side inspection of the data panel shows no visible change in text, ticks or lines.
- **Not applied in V12.** Any re-encoding would change figure bytes, including the matched-household figure that must stay exactly as built.
- **Recommended for a later pass:** palette-encode every figure except the illustration (≈1.7 MB saving), and optionally load a lighter MathJax build (≈1–2 MB).

## 5. Gates (`reports/v12_release_gate_summary.md`, all PASS)

- Report and gallery builds.
- Rendered-text banned-term audit, negative control fires.
- Stage A status check, negative control fires.
- **New** body/appendix section-title uniqueness check. Titles are normalised to strip "Technical record:", "Implementation record:", "Appendix X." and ", in words". Report and gallery share no title. The negative control injects "Behavioural estimates" into the report appendix and fails as required. Run against V11, the gate reports six shared titles: behavioural estimates, estimation, identification, the estimation samples, the household budget, what the households look like.
- 50 reader, structure and economic-derivation checks.
- 30 number-to-source checks.
- Offline render and cross-surface synchronisation.
- R11 deck and V11 notebook verification (unchanged).
- Compilation and V9–V11 byte-preservation.

## 6. Hashes

- `JMP_research_story_report_v12.html` — `0db4290ad8b63febd8a61580381a7b29165f4c030808e368c2cb2e4227b7a92f`
- `JMP_results_gallery_v12.html` — `11c9e9ab4b553d0a893a11c1f19c8865b458af7524f82086c11a7999d8c48cc4`
- Full list: `reports/v12_surface_manifest.json`.
