# deck_status_r6.md — the 17 September seminar deck, R6 content

| Field | Value |
|---|---|
| Deck | `beamer/JMP_seminar_deck_r6.tex` → `beamer/build/JMP_seminar_deck_r6.pdf` |
| Rehearsal | `beamer/JMP_seminar_deck_r6_rehearsal.tex` (notes on second screen) |
| Branch | `docs/seminar-r6`, cut from `main` (425c4c7). **Not merged.** |
| Authority | `docs/normative/JMP_W1_fork_ruling_v1.md` Appendix A (R6); `docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` §5 |
| Build | `cd beamer && make r6` (wraps `build_deck_r6.py all`) |
| Log | `beamer/build/JMP_seminar_deck_r6_build_log.txt` |
| Result | 30 PDF pages; 21 frames + 6 metropolis section pages + title. **0 overfull, 0 underfull.** Gates: **10/10 PASS.** |

## Running order and the source of every number

R6's own order, one section per R6 bullet. "Source" is where each numeral on
the slide comes from; slides with no numeral say `—`.

| § | Slide | Source of every number on it |
|---|---|---|
| 1 | Two people with the same tastes… | — |
| 1 | The contribution is a structural opportunity set… | — |
| 2 | France, EU-SILC priced through EUROMOD | S11 frames via `baseline_f1_full_sample_aggregates_v1.json` (`samples.*.unweighted_n`); node count from `positive_fit_diagnostics_v2/run_provenance.json` |
| 2 | A job is a package (TikZ) | — (the 35-hour week is a statutory fact, not an estimate) |
| 2 | Preferences and the opportunity density in one likelihood | — |
| 3 | S11 model of record: free parameters | `s11_{singles,couples}_parameter_table_v1.csv` (non-pinned row counts); objectives and evaluator commit from `run_provenance.json` |
| 3 | Extensive-margin accuracy | `g2_adequacy.csv`, weighted, `extensive_accuracy`, **ADEQUATE rows only** |
| 3 | Calibration conditioned on prediction | figure from `deciles.csv` (weighted); caption verbatim: *quadrature-limited; support audit pending* |
| 4 | The access kernel is estimated | `s11_singles_parameter_table_v1.csv`, access block, ±1.96×CR1 |
| 4 | The earning-opportunity kernel | `s11_singles_parameter_table_v1.csv`, wage block; σ̂ and its z |
| 5 | Haydar–Maniquet W¹ | — |
| 5 | W¹ coincides with the staying-home equivalent | — |
| 6 | **Baseline W¹-F, single adults** | `MNL/outputs/welfare/baseline_f1_v1/baseline_f1_full_sample_report_v1.md`, commit `6048c9f`, verified `b5550af`. N, weighted mean, median, Gini, worker/non-worker counts |
| 6 | **Baseline W¹-F, couples** | same file and commits; couples row |
| 7 | Four operators | — (operators only; no magnitude) |
| 7 | The open problem: observed vs counterfactual bundle | — |
| 8 | Where the decomposition stands | — |
| 8 | What I would like from you today | — |
| B1 | Baseline W¹-F pre-registered checks | `baseline_f1_full_sample_aggregates_v1.json` → `checks.*` (C1, C2, C5) |
| B2 | The G2 quadrature-adequacy gate | `g2_adequacy.csv` + `run_provenance.json` (bootstrap replicates, nodes, simulated vectors) |
| B3 | Authority for what is and is not on these slides | — |

Units on both welfare slides, on the slide: **household EUR/month,
unequivalised, survey weight `dwt`**. No pooled figure; the source carries no
pooled row.

## What was retired (R2)

Every item below was built on W1-EA — the ex-ante RURO inclusive-value welfare
functional, which MEASURE-MAP-1R established is a **different object** from
Haydar–Maniquet Measure 1. R2 preserves the code, results and audits unedited
and forbids presenting them as current W1 results. None is repaired here.

**From the v4.1 deck (`beamer/JMP_seminar_deck_v1.tex`), running slides**

- 12 — the welfare measure as an ex-ante equivalent income at a common reference pay
- 13 — the two-player Shapley game and its I-table
- 13b — the distribution of equivalent income under four states (`welfare_distributions_slide.pdf`)
- 14 — the environment / preference headline split
- 15 — the nested environment split (`environment_slide.pdf`)
- 15b — the nested endowments-and-needs slide (`nested_needs_slide.pdf`)
- 16 — "about a third of measured welfare inequality"
- 17 — the RUM benchmark welfare destinations (`benchmark_slide.pdf`)
- 18 — the preference-share sensitivity table
- 19 — geography and sex subgroup shares (`regional_profiles_slide.pdf`, `subgroup_slide.pdf`)
- 20 — couples reproduce the singles ordering (`couples_slide.pdf`)
- B2, B3, B5 — exhaustiveness, the scale-vs-channel table, the welfare-family derivation

**Magnitudes, wherever they appeared**

P/A/B/D and Shapley/Owen shares in both vintages: 58%, 21%, 15%, 36%, 93.7%,
94%, 35.5%, 6.3%, 6.4%, 77%, 10%, 45.73, 12.45, 13.05, 19.58, 9.79, baseline
Gini 0.134; and the s12-corrected replacements, which are the same functional
and are therefore retired with it: access **49.16**, resources and needs
34.20, job-opportunity total 55.92, preferences 9.88, Gini 0.193596, couples
8.23 / 35.72 / 51.20.

**Named items**

- the **~49% access share** (s12-corrected W1-EA frame)
- the **singles/couples access-versus-earnings contrast**
- **figP07** (`manuscript/figures/v3/figP07_w1_power_mean_weighting.png`)
- the **power-mean** paragraph, worked example and Q&A answer
- the **×4.29** ratio

The last three were already absent from the v4.1 deck source; they are listed
because R2 names them, and the R6 verifier now fails the build if any of them
reappears. The v4.1 deck itself is not deleted and not rebuilt: it is the
historical artifact R2 preserves, and `make v41` refuses to build it without
an explicit command.

Slides 12–20 were already carrying a "SUPERSEDED — WELFARE BLOCK. Do not
present." banner in `manuscript/JMP_seminar_deck_content_v2.md`. The R6 deck
does not inherit the block or the banner; the replacement is §8, *Where the
quantitative welfare decomposition stands*.

## What replaced it

One slide, §8: **Settled** (measure, reference domain, measure-correspondence
audit, descriptive baseline) / **In design (R5)** (counterfactual attainment
operator; the choice between the realised-bundle and g-computation estimands)
/ **Open** (support audit, node coverage at the hours margin) / **Withdrawn**
(every previously reported welfare share). No P/A/B/D share appears anywhere
in the deck.

## Gates

`beamer/verify_deck_r6.py`, run by every build. The v4 gates are bound to the
retired content and do not apply to this deck.

| Gate | What it enforces |
|---|---|
| G-RETIRE | none of the 24 retired W1-EA tokens appears in the source or the rendered text |
| G-NOSHARE | no Shapley/Owen/share language in the rendered deck |
| G-CAPTION | the calibration caption appears verbatim |
| G-UNITS | both baseline slides state units, weight and unequivalised |
| G-SOURCE | the baseline slides cite `6048c9f` and `b5550af` |
| G-NUMBERS | no hand-typed quantitative numeral; every one comes from `deck_numbers_r6.tex` |
| G-G2 | only G2-**ADEQUATE** fit statistics reach a slide |
| G-QA | all 8 welfare slides carry a Q&A note citing a ruling ID |
| G-NOCONF | no confusion-matrix headline statistic |
| G-POOLED | no pooled welfare figure |

## Decisions taken, and why

1. **New driver, not an edit of the v4.1 deck.** R2 preserves W1-EA artifacts
   unedited. The v4.1 deck, its content file, its figure kit and its verifier
   are all bound to that record; rebasing them in place would have meant
   editing the artifact R2 protects. `JMP_seminar_deck_r6.tex` is a separate
   driver sharing only `jmp_beamer_preamble.tex`, which carries no number.
2. **No v4.1 figure is reused.** `figures/slides/v41_source_manifest.json`
   shows the kit is built on S8/R240 sources (`ab_parameter_table_S8_v1.csv`,
   `ss8_principal_state_distributions_v1.parquet`, the P2a floor5 parquet).
   R6 says S11 only, so all four R6 panels are regenerated from S11 and from
   `positive_fit_diagnostics_v2`.
3. **Two of four fit groups are withheld, not downgraded.** Weighted
   `extensive_accuracy` is ADEQUATE for coupled women (ratio 0.17) and single
   women (0.24); it is QUADRATURE-LIMITED for both male groups (0.32, 0.30).
   The generator refuses to emit them. B2 shows the labels so the audience
   sees what is missing and why.
4. **No C_obs comparison.** E3 is not authorised: `docs/normative/` contains
   no ruling file granting it, and the run recorded
   `C_obs_benchmark: NOT PRODUCED`. The generator raises if that ever changes
   without a ruling.
5. **No welfare distribution figure.** The BASELINE-F-1 ruling confines
   household-level values to the restricted environment. The repository holds
   aggregates only, so both baseline slides are tables.

## Two discrepancies against the build brief

1. **"Build with the existing Makefile."** No Makefile existed anywhere in
   this repository. The build was driven directly by `build_deck_v4.py` /
   `build_deck_v1.sh`. `beamer/Makefile` is new here and wraps the Python
   builders without changing how either deck is produced. `make` is not
   installed on this machine, so the recorded build was run as
   `python build_deck_r6.py all` — byte-for-byte what `make r6` invokes.
2. **`outputs/positive_fit_diagnostics_v2` path.** It is not under `MNL/`; it
   is in the sibling worktree `MNL_posfit/` (branch `diagnostics/posfit-v2`),
   which is where POSFIT-1R ran. The generators read it there and record the
   SHA-256 of every file they read in
   `beamer/build/r6_number_provenance.json`.
