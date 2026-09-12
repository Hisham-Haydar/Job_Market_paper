# deck_status_r6.md — the 17 September seminar deck, R6 content (v2: equivalised-primary)

| Field | Value |
|---|---|
| Deck | `beamer/JMP_seminar_deck_r6.tex` → `beamer/build/JMP_seminar_deck_r6.pdf` |
| Rehearsal | `beamer/JMP_seminar_deck_r6_rehearsal.tex` (notes on second screen) |
| Branch | `docs/seminar-r6-v2`, cut from `main` (`071c5d2`). **Not merged.** |
| Authority | `docs/normative/JMP_W1_fork_ruling_v1.md` Appendix A (R6); `docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` §5; `docs/JMP_seminar_architecture_freeze_2026-09-17_v1.md` (the seminar freeze, commit `6d441b1`); the Deputy/PI brief implementing items A-G of that freeze (this revision). |
| Build | `cd beamer && python build_deck_r6.py all` (equivalent to `make r6`) |
| Log | `beamer/build/JMP_seminar_deck_r6_build_log.txt` |
| Result | Deck: 0 overfull, 0 underfull. Rehearsal: 32 pages, 0 overfull, 0 underfull. **Gates: 15/15 PASS** (10 inherited R6 gates + 5 new gates added for this revision). |
| Build commit | HEAD of `docs/seminar-r6-v2` after the commit that carries this file (see `git log -1` on this branch). Branch cut point: `071c5d2`. |

This revision supersedes the v1 status doc that was written at commit `cafe0ba`
on the sibling branch `docs/seminar-r6`. That file already existed in this
branch's tree (it is an ancestor commit, `cafe0ba`, reachable from `071c5d2`);
it is **not** missing, contrary to the initial assumption in this task's
brief — but its content described the pre-revision (unequivalised-primary)
deck and is stale. This file replaces it in place at the same path.

## What changed in this revision (items A-G of the Deputy/PI brief)

- **(A) No singles/couples equivalised-level side-by-side.** Every
  equivalised number is shown once per sample, on its own frame; no frame,
  table or sentence anywhere in the deck places a singles equivalised number
  next to a couples equivalised number. New gate `G-NOSIDEBYSIDE` fails the
  build if any frame's LaTeX source carries both a singles-equivalised and a
  couples-equivalised macro, if any pdftotext-extracted paragraph contains
  both samples' equivalised Gini values, or if the withdrawn "near equality"
  / "nearly equal" wording reappears anywhere. The withdrawn claim does not
  appear in this deck's source or rendered text (confirmed by ID scan, see
  below); it was already absent before this revision.
- **(B) Equivalised results are now primary.** §6 is retitled "Equivalised
  $\Wone$-F distribution (primary)" and its two frames (singles, couples)
  report `C^{eq}` and `\Wone_F{}^{eq}` weighted mean/median/Gini. The old
  unequivalised frames are demoted to appendix backup slides B1 (singles) and
  B2 (couples), explicitly labelled "verification backup", pushing the old
  B1/B2/B3 checks/gate/authority slides to B3/B4/B5. New gate `G-EQPRIMARY`
  checks the ordering (equivalised section before `\appendix`) and the demoted
  slide count; `G-UNITS` now checks both the 2 equivalised (units: EUR/month,
  household-equivalised, modified-OECD) and 2 unequivalised backup frames
  (units: household EUR/month, unequivalised) for their respective unit/weight
  caveats.
- **(C) Child-shifter wording.** The verbatim sentence from the brief is
  reproduced exactly in the Q&A note of the "Four operators" frame (§7), and
  the shifter is never called a preference or taste parameter. New gate
  `G-CHILDSHIFTER` checks the exact wording (whitespace-normalised, so a line
  wrap in the .tex source cannot silently break the check) and greps for any
  "child ... is/as a preference/taste parameter" mislabelling.
- **(D) P label.** The decomposition table's $P$ row now reads "its
  systematic utility heterogeneity (tastes + reduced-form time constraints)
  by the common reference"; the frame's caveat adds "Final decomposition
  semantics are work in progress." No magnitude or share is attached to
  $P$/$A$/$B$/$D$ anywhere (unchanged from R6; reconfirmed by new gate
  `G-PLABEL` and the existing `G-NOSHARE`/`G-NUMBERS`).
- **(E) Architecture preserved.** The chain opportunity environment → choice/
  attained bundle → literal Mapping-F $\Wone$ → inequality is unchanged
  (§§2-6). The staying-home-equivalent coincidence is still phrased as a
  domain coincidence, not a theorem (§5, second frame — unchanged). No
  sentence states that opportunities do not affect well-being (checked by ID
  scan; none was present before or after this revision). The one-page
  `docs/normative/JMP_counterfactual_attainment_architecture_for_seminar_v1.md`
  named in the freeze doc does **not exist** anywhere in git history and was
  **not created**: per this task's brief, the architecture is fully specified
  by the freeze doc plus this brief, so the deck cites the freeze doc and
  this status file instead of that missing note. The freeze doc's suggested
  Q&A paragraph (its §3) is not reproduced verbatim anywhere in this deck —
  no existing frame already carried that exact wording, so there was nothing
  to "keep unchanged"; existing frame-specific Q&A notes were left as they
  were.
- **(F) Out-of-scope tokens.** `beamer/verify_deck_r6.py`'s existing
  24-entry `RETIRED_TOKENS` map is unchanged and untouched; six new entries
  (`W_EA`, `finite-offer welfare`, `finite-market-set welfare`,
  `OEC characterisation`, `OEC-CHAR`, `SCALE-SENS-1`) are added to the same
  map via `RETIRED_TOKENS.update(...)`, and checked both by the existing
  `G-RETIRE` gate (merged map) and by a new, separately itemised `G-NOBAN`
  gate for this revision's own audit trail. `figP07` and the `4.29`/`×4.29`
  ratio were already in the original 24 and needed no addition.
- **(G) This file.** Regenerated fresh per this section, at the same path as
  the earlier `deck_status_r6.md`.

## Running order and the source of every number

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
| 6 | **Baseline W¹-F, equivalised, single adults (PRIMARY)** | `docs/results/JMP_BASELINE_F1_equivalised_reporting_v1.md`, commit `4c4e07e`, over the verified construction `MNL/outputs/welfare/baseline_f1_v1/baseline_f1_full_sample_report_v1.md`, commit `6048c9f`, verified `b5550af`. Machine-readable source read directly by `make_deck_numbers_r6.py`: `MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json`. `C_eq`/`W_F_eq` weighted mean/median/Gini (Gini to 6 d.p.: **0.263292 → 0.249807**) |
| 6 | **Baseline W¹-F, equivalised, couples (PRIMARY)** | same memo/commits; `MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json`. Gini **0.226805 → 0.197403** |
| 7 | Four operators | — (operators only; no magnitude; $P$ label text is hand-authored per the Deputy/PI ruling, not a computed numeral) |
| 7 | The open problem: observed vs counterfactual bundle | — |
| 8 | Where the decomposition stands | — |
| 8 | What I would like from you today | — |
| B1 | **Baseline W¹-F, unequivalised, single adults (backup)** | `MNL/outputs/welfare/baseline_f1_v1/baseline_f1_full_sample_report_v1.md`, commit `6048c9f`, verified `b5550af`. N, weighted mean, median, Gini, worker/non-worker counts |
| B2 | **Baseline W¹-F, unequivalised, couples (backup)** | same file and commits; couples row |
| B3 | Baseline W¹-F pre-registered checks | `baseline_f1_full_sample_aggregates_v1.json` → `checks.*` (C1, C2, C5) |
| B4 | The G2 quadrature-adequacy gate | `g2_adequacy.csv` + `run_provenance.json` (bootstrap replicates, nodes, simulated vectors) |
| B5 | Authority for what is and is not on these slides | — |

Units, on every welfare slide: primary (§6) **EUR/month, household-equivalised
(modified-OECD scale)**, survey weight `dwt`, scale flagged PROVISIONAL
pending economics review; backup (B1/B2) **household EUR/month,
unequivalised**, survey weight `dwt`. No pooled figure anywhere; the source
carries no pooled row and no singles/couples level comparison is drawn.

## What was retired (R2, unchanged from the v1 status doc)

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

**Retired/out-of-scope in this revision (item F, seminar freeze)**

- **W_EA** as a current-paper result (October research option only)
- **finite-offer welfare** / finite-market-set welfare architecture (October only)
- **OEC characterisation** (OEC-CHAR-1 mission, on HOLD until October)
- **SCALE-SENS-1** (not a seminar deliverable)
- the withdrawn **"near equality"** claim between singles and couples
  equivalised welfare (never present in this deck; the claim itself is
  permanently withdrawn and a verifier gate now guards its non-recurrence)

The v4.1 deck itself is not deleted and not rebuilt: it is the historical
artifact R2 preserves, and `make v41` refuses to build it without an explicit
command.

## What replaced it

§6, equivalised primary distribution (this revision) plus §8, *Where the
quantitative welfare decomposition stands*: **Settled** (measure, reference
domain, measure-correspondence audit, the equivalised and unequivalised
descriptive baselines) / **In design (R5)** (counterfactual attainment
operator; the choice between the realised-bundle and g-computation estimands)
/ **Open** (support audit, node coverage at the hours margin; ratification of
the modified-OECD equivalence scale) / **Withdrawn** (every previously
reported welfare share; the singles/couples equivalised "near equality"
claim). No P/A/B/D share appears anywhere in the deck.

## Open items

- The modified-OECD equivalence scale used in §6 is flagged
  `PROVISIONAL_PENDING_ECONOMICS_REVIEW` for both samples in its own source
  memo (`docs/results/JMP_BASELINE_F1_equivalised_reporting_v1.md`).
  Ratification is an open Deputy/PI item; `make_deck_numbers_r6.py` refuses to
  emit the equivalised numbers if either sample's status ever drifts from
  that exact string, so the deck cannot silently go stale on this point.
- The counterfactual attainment estimand (R5) remains in design; no execution
  before the seminar per the freeze doc.
- `docs/normative/JMP_counterfactual_attainment_architecture_for_seminar_v1.md`
  does not exist and was not created (see item E above).
- POSFIT close-out (male-group quadrature adequacy) is unresolved; both male
  groups remain withheld on the fit slide.
- Final P/A/B/D decomposition semantics (in particular the interpretation of
  $P$) remain work in progress, as now stated explicitly on the operators
  slide.

## Gates

`beamer/verify_deck_r6.py`, run by every build.

| Gate | What it enforces |
|---|---|
| G-RETIRE | none of the retired W1-EA tokens (24 original + 6 new out-of-scope tokens, merged into one map) appears in the source or the rendered text |
| G-NOSHARE | no Shapley/Owen/share language in the rendered deck |
| G-CAPTION | the calibration caption appears verbatim |
| G-UNITS | 2 equivalised (primary) + 2 unequivalised (backup) baseline slides each state units, weight and scale status |
| G-SOURCE | the baseline slides cite `6048c9f`, `b5550af`, and the E3-EQ memo `4c4e07e` |
| G-NUMBERS | no hand-typed quantitative numeral; every one comes from `deck_numbers_r6.tex` |
| G-G2 | only G2-**ADEQUATE** fit statistics reach a slide |
| G-QA | all 8 welfare-section slides carry a Q&A note citing a ruling ID |
| G-NOCONF | no confusion-matrix headline statistic |
| G-POOLED | no pooled welfare figure |
| **G-NOSIDEBYSIDE** *(new)* | no frame or rendered paragraph mixes singles- and couples-equivalised levels; the withdrawn "near equality" claim never reappears |
| **G-EQPRIMARY** *(new)* | equivalised distribution is section 6, before `\appendix`; exactly 2 unequivalised slides are demoted to the backup appendix |
| **G-CHILDSHIFTER** *(new)* | the child-shifter sentence is present verbatim (whitespace-normalised); the shifter is never called a preference/taste parameter |
| **G-PLABEL** *(new)* | the $P$ label reads "systematic utility heterogeneity (tastes + reduced-form time constraints)" verbatim, with a "work in progress" caveat, and no P/A/B/D magnitude appears anywhere |
| **G-NOBAN** *(new)* | the six seminar-freeze out-of-scope tokens (W_EA, finite-offer welfare, finite-market-set welfare, OEC characterisation, OEC-CHAR, SCALE-SENS-1) are individually itemised and absent |

Result of the last run (recorded in `beamer/build/JMP_seminar_deck_r6_build_log.txt`): **15/15 PASS**.

## ID scan (post-build)

Every forbidden token — the original 24 plus the 6 new item-F tokens plus 3
"near equality" phrasings — was grepped (case-insensitive) against
`JMP_seminar_deck_r6.tex`, `build/JMP_seminar_deck_r6_text.txt` and
`build/JMP_seminar_deck_r6_rehearsal_text.txt`. **Zero hits in all three
files.** No retirement is mentioned inside the deck itself; every retirement
is documented only in this status file, per the R6 convention already in
place before this revision.

## Decisions taken, and why

1. **New driver, not an edit of the v4.1 deck.** Unchanged from the v1
   status doc: R2 preserves W1-EA artifacts unedited, so `JMP_seminar_deck_r6.tex`
   remains a separate driver.
2. **Equivalised numbers are read from the same machine-readable JSONs the
   E3-EQ memo itself reports from**, not retyped from the memo's markdown
   table: `make_deck_numbers_r6.py` now reads
   `MNL/outputs/welfare/baseline_f1_equivalised_v1/{singles,couples}
   _equivalised_reporting_v1.json` directly and reproduces the memo's Gini
   values to 6 decimal places (`0.263292`, `0.249807`, `0.226805`,
   `0.197403`), so the deck cannot drift from its source file.
3. **Singles and couples equivalised results stay on separate frames**,
   continuing the existing pattern already used for the unequivalised
   baseline in R6 — this was the simplest way to satisfy item A
   structurally, rather than relying only on a verifier gate to catch a
   violation after the fact.
4. **Backup slide numbering shifts (B1/B2/B3 → B3/B4/B5)** because two new
   backup slides (the demoted unequivalised singles/couples tables) were
   inserted at the front of the appendix, ahead of the pre-registered checks,
   G2 gate and authority slides.
5. **No architecture note was written.** The freeze doc's
   `JMP_counterfactual_attainment_architecture_for_seminar_v1.md` was
   confirmed absent from every branch and commit in git history; per this
   task's own brief, the freeze doc plus this status file are treated as
   sufficient specification of the architecture for this seminar, so no new
   document was authored.
