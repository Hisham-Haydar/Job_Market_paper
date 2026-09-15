# JMP — V12 to V13 figures release, v1

No estimation, pricing, welfare or decomposition was rerun. Every figure is
drawn by `reports/research_story_build/make_v13_figures.py` directly from the
records below; no stored image is reused. Every number printed on a figure is
listed, with its source pointer and printed text, in
`reports/v13_figure_values.json` (48 values) and registered as `fig13_*`. The
V12 registry values are unchanged. The four new PNGs are 256-colour palette
images; the matched-household figure is byte-identical to V11.

## 1. Figures and captions

| Figure | Place | Sources |
|---|---|---|
| `fig_v13_architecture.png` | Section 4, before G | none (no numbers) |
| `fig_v13_att_decomposition.png` | Section 5, attained-bundle decomposition | `MNL_decomp/outputs/welfare/preseminar_pab_v1/shapley_PAB_{singles,couples}.csv` (`gini_point_contribution`), `coalition_values_{singles,couples}.csv` (`I_S_gini`, coalition EMPTY) |
| `fig_v13_ea_decomposition.png` | Section 5, ex-ante well-being and decomposition | `MNL_wea/docs/wea_sprint_1/stage4/stage4_certification_and_results_v1.json` (`results.*.*.phi`, `gini_EMPTY`) |
| `fig_v13_central_result.png` | Section 5, "The central result", above the comparison table | same record: `comparison_W1F.*.*.W1F_phi` and `W1F_gini_EMPTY` (attained bundle); `results.*.*.phi` and `gini_EMPTY` (ex ante); each bar = contribution / own baseline Gini × 100 |

The attained-bundle CSV contributions and baselines equal the certified
comparison record to 1e-12; the generator stops if they do not.

**Architecture.** "How the decomposition is built. Three channels can be
equalised: systematic preferences; local labour-market access (local
unemployment exposure, region, urban or rural location and year); and
systematic earning opportunities. Household resources, needs and composition
are held fixed in every coalition. Each counterfactual household is evaluated
under both welfare perspectives, inequality is measured with the
household-weighted Gini, and the Shapley rule averages each channel's marginal
contribution over all orders." The diagram shows the fixed input as a hatched,
dashed box and the two perspectives as branches from the same counterfactual
household.

**Attained-bundle decomposition.** "Attained-bundle welfare: exact Shapley
contribution of each channel to the change in the Gini, in Gini points, for raw
and equivalised reporting, with each baseline Gini stated in the panel. Access
is local labour-market access (local unemployment exposure, region, urban or
rural location and year). Preliminary. Household resources, needs and
composition are held fixed. The preference contribution changes sign with
equivalisation in both samples, so no directional claim is made about it."

The figure itself carries:
- the "PRELIMINARY" line;
- the held-fixed statement;
- the sign-change annotation in each panel;
- the baseline Gini for both scales in each panel title.

**Ex-ante decomposition.** Same design. The figure says the calculation passed
its numerical checks and that resources, needs and composition are held fixed,
and it annotates the couples' preference sign change. It is not labelled
"preliminary", because the ex-ante computation is certified and the report
never calls it preliminary; labelling it so would contradict the certification
record. This is a deliberate deviation from the instruction's wording for the
"certified ex-ante equivalents".

**Central result.** "The central result. Access and earning-opportunity
contributions, each as a percentage of its own perspective's baseline Gini,
under attained-bundle welfare (ATT) and ex-ante welfare (EA). Access is local
labour-market access (local unemployment exposure, region, urban or rural
location and year). For single-adult households earning opportunities are
larger under ATT and access is larger under EA, on both scales; couples show no
such reversal. Household resources, needs and composition are held fixed;
neither perspective is designated primary." Four panels (sample × scale); panel
titles state "REVERSAL" for singles and "No reversal" for couples, derived from
the record's orderings rather than typed.

## 2. Source-record fix (MNL_decomp, commit `389374c7`, local)

`preseminar_pab_record_v1.json` now reads:
- `factor_labels.A`: "local labour-market access (local unemployment exposure, region, urban/rural, year)";
- `A_definition_note`: now says household-level access heterogeneity "runs through local unemployment exposure, geography and year";
- `A_label_erratum`: a new key recording the correction and the evidence, namely `samples.*.gate0.coalition_invariance.*.substituted_covariates`, which lists `gsur` in every coalition containing A.

The same label omission existed in the label columns of
`shapley_PAB_*.csv`, `coalition_values_*.csv` and
`anchor_attainment_shares_v1.csv`; those are corrected too. The generator
labels in `run_preseminar_pab_decomposition_v1.py` are also corrected, so a
rerun cannot reintroduce the omission.

`scripts/welfare/fix_preseminar_pab_access_label_v1.py` performs the correction
by exact string replacement. It verified that:
- every non-label CSV field is unchanged;
- the other 1,606 JSON leaves are unchanged.

No hash of these files is pinned by any active build or gate; historical
release records list their earlier hashes.

**Not pushed.** The `welfare/preseminar-pab` branch has never been published: it
is 157 commits beyond `origin/main` and has no remote counterpart. Pushing it
would publish all of that unpublished history. That is a separate decision for
the PI, so the fix is committed locally only.

## 3. Counts (rendered text; bibliography excluded)

| Surface | Version | Body words | Appendix words | Body figures | Appendix figures | Body tables | Appendix tables | Size |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Report | V12 | 12,817 | 3,009 | 10 | 2 | 17 | 3 | 5.20 MB |
| Report | **V13** | **13,161** | **3,009** | **14** | **2** | **17** | **3** | **5.60 MB** |
| Gallery | V12 | 7,072 | 8,519 | 12 | 5 | 16 | 38 | 4.65 MB |
| Gallery | **V13** | **7,367** | **8,519** | **16** | **5** | **16** | **38** | **5.06 MB** |

The report appendix is 0.23 of the body. No section title is shared between
body and appendix.

## 4. Gates (`reports/v13_release_gate_summary.md`, all PASS)

- Figures regenerated from the certified records; report and gallery built.
- **New figure-caption gate** (`check_v13_figure_captions.py`), across the report (32 captions and alt texts) and gallery (43):
  - a caption naming the access channel must name local unemployment exposure;
  - no outdated access definition may appear;
  - no old decomposition image may be embedded.
  - Its negative control inserts a figure captioned with the outdated definition and fails as required. Run against V11 it fails on the three embedded old images; V12 passes.
- Banned-term audit, Stage A status and section-title uniqueness, each with its negative control failing as required.
- 54 reader and structure checks, including figure placement and no old images.
- 37 number-to-source checks. The new ones:
  - re-derive every printed figure value independently from the CSVs and the JSON;
  - confirm the printed text and registry keys;
  - confirm the singles-reversal / couples-no-reversal verdicts;
  - confirm palette encoding and no reuse of an old image hash;
  - confirm the matched figure is byte-identical to V11.
- Offline render, cross-surface synchronisation, R11 deck and V11 notebook regressions, compilation, V9–V12 byte-preservation.

## 5. Hashes

- `JMP_research_story_report_v13.html` — `77b0b8c2a78c2e17bea250c50f8a61565e47e116654993725f7e5e00e83b60b5`
- `JMP_results_gallery_v13.html` — `f417acaeb07f6cb492a2a410275f651f277888a1ff1a899344cdc7501f69683d`
- Figures: architecture `cbd6075a…`, attained-bundle `9a95e5c7…`, ex-ante `3145036e…`, central `eedc699b…`; full list in `reports/v13_surface_manifest.json`.
