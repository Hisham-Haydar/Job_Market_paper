# Beamer v4.1 — build and content review

Authority: [the supplied content v2.1](../manuscript/JMP_seminar_deck_content_v2.md), updated 2026-09-07 with the corrected slide 12 speech. 25 running-order frames; B1 in three blocks, then B2–B6. 5b has four builds, 9b has two, and geography/sex on 19 has two. The 25-minute order is unchanged.

Verifier: **PASS — 56/56 checks.** All three logs have zero errors, zero overfull boxes and zero underfull boxes. PDF headlines match the content document; supplied captions and prose are present; running speaker notes match both the source and the rehearsal PDF. The text-layer gate finds zero forbidden labels in every built PDF and every active slide figure.

| Build | Pages | PDF | Text export |
|---|---:|---|---|
| Full | 38 | [Open](build/JMP_seminar_deck_v1.pdf) | [Text](build/JMP_seminar_deck_v1_text.txt) |
| 25-minute | 23 | [Open](build/JMP_seminar_deck_v1_25min.pdf) | [Text](build/JMP_seminar_deck_v1_25min_text.txt) |
| Rehearsal | 38 | [Open](build/JMP_seminar_deck_v1_rehearsal.pdf) | [Text](build/JMP_seminar_deck_v1_rehearsal_text.txt) |

## Per-slide table

Counts are measured from the PDF text layer: headline, prose, table/equation text, chart labels and numeric tokens; navigation fractions and speaker notes are excluded. A whitespace-delimited token counts when it contains a letter or digit. Slides with builds report the largest count across their builds. These are **all on-slide words**, not the former body-prose-only count.

| Slide | Headline | Element | Builds | On-slide words |
|---|---|---|---:|---:|
| 1 | Unequal Job Opportunities and the Measurement of Welfare Inequality | text | 1 | 22 |
| 2 | Two questions. | text | 1 | 34 |
| 3 | Three literatures, one gap. | three literature columns | 1 | 83 |
| 4 | A job is a package; welfare is compared on the set of reachable jobs. | theory diagram | 1 | 82 |
| 5 | Empirically the set is an estimated distribution and the pay is an offer density. | theory diagram | 1 | 44 |
| 5b | For one household: its estimated employment mass, hours weights, occupation shares and wage-offer density | household_a_employment / household_a_hours / household_a_occupation / household_a_wages | 4 | 53 |
| 6 | Preferences and an opportunity density, in one likelihood. | equations | 1 | 53 |
| 7 | Each household: its observed job plus 100 drawn alternatives, all priced through the tax-benefit system. | equations | 1 | 43 |
| 8 | France 2016: 1,555 single-adult households; one in four employed at exactly 35 hours. | observed_hours | 1 | 36 |
| 9 | The model reproduces the hours distribution, employment and occupation shares. | hours | 1 | 70 |
| 9b | Estimated indifference curves and the price of an hour, by age and sex | indifference_curves / compensation_by_age | 2 | 52 |
| 10 | What the data pin down, and what remains conditional. | text | 1 | 43 |
| 11 | An independent source puts the 35-hour concentration at 37%; the sample at 34%; the model at 35%. | external | 1 | 49 |
| 12 | Equivalent income at a common reference pay, under four preference–environment states. | equations + table | 1 | 83 |
| 13 | A two-player Shapley game: preferences against the complete non-preference environment. | equations + table | 1 | 93 |
| 13b | The distribution of equivalent income under the four states | welfare_distributions | 1 | 42 |
| 14 | The non-preference environment accounts for 94% of measured welfare inequality; preferences for 6%. | headline_references | 1 | 50 |
| 15 | Household endowments and needs 58%, earning opportunities 21%, job access 15%; job opportunities together 36%. | environment | 1 | 54 |
| 16 | Unequal job opportunities account for about a third of measured welfare inequality; omitting them re-attributes almost nothing to preferences. | text | 1 | 55 |
| 17 | The benchmark fits the marginals as well, is 129 log-points worse, and recovers availability as taste. | benchmark | 1 | 55 |
| 18 | The preference share is the sensitive margin; the environment's internal structure is stable. | table | 1 | 50 |
| 19 | Within job access, nearly all of the household-varying contribution is geographic; job access matters twice as much for men. | regional_profiles / subgroup | 2 | 56 |
| 20 | Couples reproduce the same environment ordering; their preference share is not robustly identified. | couples | 1 | 65 |
| 21 | Each limit names the evidence that would lift it. | table | 1 | 40 |
| 22 | Conclusion | text | 1 | 54 |
| B1a | B1 — The estimated coefficients: preferences | coefficients_1 | 1 | 22 |
| B1b | B1 — The estimated coefficients: job access | coefficients_2 | 1 | 37 |
| B1c | B1 — The estimated coefficients: earning opportunities | coefficients_3 | 1 | 21 |
| B2 | B2 — Exhaustiveness is a tested property | table | 1 | 23 |
| B3 | B3 — The scale moves with the channel that equalises needs | table | 1 | 49 |
| B4 | B4 — the desired-hours counterpart test | table | 1 | 41 |
| B5 | B5 — Where the welfare family comes from | equations | 1 | 53 |
| B6 | B6 — The RUM benchmark details | table | 1 | 35 |

## Source and implementation notes

- **Slide 18 corrected:** the full 50–400 range and the 100–400 range now have separate macros. The source `MNL/experiments/JMP_SEMINAR_SPRINT/figures/figS6_02_coefficient_stability.csv` gives a maximum absolute deviation of 0.213142 for R ≥ 100, which rounds to 0.2; including R = 50 gives 0.562005, displayed as 0.56. Both are maximum absolute deviations relative to the R=100 estimate, scaled by its robust standard error.
- **Slide 13:** the direct environment equalization reduces baseline Gini by 76.937%, displayed as 77%; the distinct Shapley attribution rounds to 94%. Both displayed values are generated from frozen data.
- **Slide 5b:** employment mass comes from E1 household A. Hours and occupation factors divide the CSV’s unconditional densities/probabilities by that mass; the wage curve retains the original occupation mixture. The supplied speech is verbatim; its “log-normal” shorthand describes the conditional components, while the displayed marginal is their mixture.
- **Slide 9b:** one actual employed adult without children per sex is selected deterministically by proximity to age 40, 35 hours and sex-specific median consumption. The household’s own 101 priced packages are plotted without identifiers; varying wage offers mean they are not joined into a fictitious fixed-wage budget line. Box-Cox inversion follows reader’s-guide notebook cells 61/63, using the final sprint estimates. The observed job lies on the central indifference curve; inversion residuals are checked numerically.
- **Slide 9b, age build:** the two final-model analytic curves are read directly from figAB02. This panel uses its declared common reference bundle (35 weekly hours, EUR 1,870.5768 monthly consumption, no children); the individual budgets belong to the preceding build. No widened-bound arm is shown.
- **Slide 13b:** figW01’s CSV contains summary statistics rather than density ordinates. The original frozen household-state parquet supplies its weighted KDE; all four raw-state counts, means, standard deviations and Ginis are checked against the CSV. The fully common state is shown as a vertical rule, not a smoothed density. Grid and bandwidth match the original renderer.
- The decisive verbatim-content brief supersedes the older 12-word ceiling and 23-message running order. The verifier retains their purposes through exact authored-prose and exact-order gates. The content document gives no `Say:` text for slide 22; its note is deliberately empty.
- New empirical macros read existing sprint tables or the original tabular/JSON artefacts named by the manuscript provenance. No matching new summary table exists for several couples, benchmark and sensitivity quantities; those use their existing run artefacts, with paths recorded beside the definitions. Citation years and question enumerators come from the supplied content document and are marked as document metadata.
- The market-side integration half-band is rounded outward to one decimal percentage point to reproduce the authored ±1.0. Other displayed precisions follow the supplied text.
- The shared preamble is unchanged. The main file adjusts only title-box height, caption spacing, equation size and figure placement to fit the longer verbatim content. Running rehearsal notes use a larger font; long backup notes retain the original compact size.
- The theory drawing is reused on exactly slides 4 and 5. Visibility switches hide the original pay dots and ability braces on slide 5; the original drawing coordinates, agent palette, staging macros and preference segments are retained.
- B1 retains the existing three coefficient panels. B2 shows the four removed objects using the supplied channel labels; its prior exhaustiveness explanation is retained in notes. B3 and B5 retain their source material. B4 uses the supplied descriptive backup label. B6 typesets the existing benchmark quantities and preserves the previous benchmark notes. No new spoken script is authored for the backups.
- Font checks verify the recorded figure-kit sizes and the embedded figure PDF fonts (minimum 18 pt). The figures are vector PDFs and are scaled when placed on the Beamer page.

## Figure reuse

All twelve active v4 panels are reused. Seven v4.1 panels were added from frozen inputs. The three panels first introduced in v4 were:

| New panel | Source CSV |
|---|---|
| `observed_hours_slide.pdf` | `fig01_observed_hours_35h_peak.csv` |
| `headline_references_slide.pdf` | `figW02_headline_decomposition.csv` |
| `regional_profiles_slide.pdf` | `figG02_regional_access_environments.csv` |

v4.1 provenance and calculation checks: [input fingerprints](figures/slides/v41_source_manifest.json), [indifference checks](figures/slides/indifference_checks.json), [density checks](figures/slides/welfare_distribution_checks.json), [figure index](figures/slides/slide_figure_index.csv).

Five unused v3 panels are preserved in `figures/unused_v3/`. No paper figure or MNL source artefact was modified.

## Reproduce

```powershell
cd Job_Market_paper/beamer
python build_deck_v4.py all
```

The build regenerates number macros and the seven v4.1 panels, reuses existing v4 panels, runs latexmk on the three existing drivers, exports text with `pdftotext -layout`, verifies, and rewrites this report.

Machine-readable evidence: [verification](build/verification_v4.json), [slide table](build/slide_table_v4.json).

Content SHA-256: `7fc32780abdad8fc5a96741d38ad46c59efa7fd4d422ede6a21433b041572f25`.
