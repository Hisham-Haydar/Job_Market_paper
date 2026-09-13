# deck_status_r6.md — the 17 September seminar deck, R6 content (v2: equivalised-primary)

| Field | Value |
|---|---|
| Deck | `beamer/JMP_seminar_deck_r6.tex` → `beamer/build/JMP_seminar_deck_r6.pdf` |
| Rehearsal | `beamer/JMP_seminar_deck_r6_rehearsal.tex` (notes on second screen) |
| Branch | `docs/seminar-r6-v2`, cut from `main` (`071c5d2`). **Not merged.** |
| Authority | `docs/normative/JMP_W1_fork_ruling_v1.md` Appendix A (R6); `docs/normative/JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md` §5; `docs/JMP_seminar_architecture_freeze_2026-09-17_v1.md` (the seminar freeze, commit `6d441b1`); the Deputy/PI brief implementing items A-G of that freeze (this revision). |
| Build | `cd beamer && python build_deck_r6.py all` (equivalent to `make r6`) |
| Log | `beamer/build/JMP_seminar_deck_r6_build_log.txt` |
| Result | Deck: 0 overfull, 0 underfull. Rehearsal: 32 pages, 0 overfull, 0 underfull. **Gates: 16/16 PASS** (10 inherited R6 gates + 5 DECK-2 gates + `G-SCALE` added in DECK-3). |
| Build commit | DECK-3: HEAD of `docs/seminar-r6-v2` after the commit that carries this file (parent `50b7072`, the DECK-2 commit; see `git log -1`). Branch cut point: `071c5d2`. |
| Build hashes (DECK-3) | `build/JMP_seminar_deck_r6.pdf` sha256 `5061c21f64d4458049f06050dbc4f3632c9e670ac6fe2d03908c8276d8fad4d5`; `build/JMP_seminar_deck_r6_rehearsal.pdf` sha256 `205574604f8350f6d53c9476a1a5aacb103b2c3c2ede8620a4baad2c06e714f4`; `deck_numbers_r6.tex` sha256 `43290c107317390aa750d5114d77683841c56e79bac9e3a83f77e343f35459aa` (PDF bytes carry a build timestamp, so a rebuild changes the PDF hash but not the numbers file). |

## DECK-3 revision (scale ratified; POSFIT v2b)

### 1. Equivalence scale is ratified

Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING", section 1, verbatim:
*"Modified-OECD is ratified as the primary equivalence scale for current JMP
distributional reporting. The provisional economics-review status is
closed."*

- Every "PROVISIONAL, pending economics review" statement is removed from the
  deck: the `\wfunitseq` units caveat (both §6 equivalised slides), the
  singles and couples §6 Q&A notes, the B2 note (which gave "scale not yet
  ratified" as the no-pooling reason) and the B5 authority table (E3-EQ row).
  The units caveat now reads "Equivalence scale: the ratified modified-OECD
  scale (Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING", s1;
  `JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md`). Singles and
  couples equivalised levels are never compared." The no-level-comparison
  caveat is kept (and `G-NOSIDEBYSIDE` is unchanged).
- The memo `JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md` is filed at
  `docs/normative/JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md`
  (commit `307e1a6`), recovered from the Goal 1 chat, SHA-256
  `7cace61e4476148d05c894729f05ff38f79af803b9e637449ec76f9cb808014e` verified
  before use, corrected identifier scan run over it with zero hits.
- **Guard repointed** (`beamer/make_deck_numbers_r6.py`). The old guard refused
  to emit equivalised numbers unless both artifacts read
  `PROVISIONAL_PENDING_ECONOMICS_REVIEW`. It now holds the ruling as constants
  (`SCALE_RULING_ID`, verbatim `SCALE_RULING_QUOTE`, `SCALE_MEMO`) and refuses
  unless (i) the deck source cites the ruling and the memo
  (`check_scale_citation`, whitespace/escape-normalised), (ii) every artifact's
  `scale_name` is `modified_OECD`, and (iii) every artifact's `scale_status` is
  the pre-ruling provisional label or a ratified label (`RATIFIED`,
  `RATIFIED_PRIMARY`, or any `RATIFIED*`) (`check_scale_status`). The
  committed JSONs still carry the provisional label; that is accepted.
- **Controls** (scratch script, temp copies only, discarded; real files
  sha-checked unchanged afterwards): current provisional-labelled artifacts →
  EMITTED; artifacts relabelled `RATIFIED` → EMITTED; relabelled
  `RATIFIED_PRIMARY` → EMITTED; relabelled `DRAFT_UNREVIEWED` → REFUSED;
  `scale_name` changed to `square_root` → REFUSED; all three ruling citations
  removed from the deck → REFUSED; memo citation removed → REFUSED.
- **New verifier gate `G-SCALE`**: the `\wfunitseq` macro (used on both §6
  slides) cites the ruling and memo, the rendered deck text carries both, and
  no `provisional…` / `pending (an) economics review` wording appears in the
  non-comment source or the rendered text. Controls: committed deck → PASS;
  "PROVISIONAL, pending economics review" reinserted into a note → FAIL;
  ruling removed from the macro → FAIL.

### 2. POSFIT sourcing moved from v2 to v2b

Source is now `C:\Users\hisham\Repo\MNL_posfit\outputs\positive_fit_diagnostics_v2b\`,
MNL_posfit commit **`a2e80a8`** ("diagnostics: add POSFIT support coverage
v2b"); memo `JMP_positive_fit_diagnostics_memo_v2b_addendum.md`. The files the
deck reads (`g2_adequacy.csv`, `deciles.csv`, `run_provenance.json`,
`hard_classification_metrics.csv`, `support_record.csv`,
`support_record_v2.csv`) are byte-identical at `a2e80a8` and at the worktree
HEAD `de61d1a` (the later `96b6c88` S12-C commit adds files and touches
`disclosure_scan.json` only). The package has no README/manifest file; its
provenance is `run_provenance.json`, `objective_gate_pass.json`,
`support_file_dependencies.csv` and the addendum memo.

**What changed v2 → v2b.** v2 evaluated fit on the estimation panel's
household-specific IID draws (criterion-A R100: 100 continuous nodes per
household plus the exact h=0 atom; coupled men had no short-hours node). v2b
re-evaluates at the same fixed S11 θ̂ (objectives reproduce exactly, evaluator
`55bb0d0`) on the S12 common 8×256 Owen-scrambled Sobol panel, **2,048 nodes
per household**, hours on [5,70] with short-hours nodes for every group. ESS<30
flags fall from 2072/2072/507/670 (cm/cf/sm/sf) to **0 for every group**
(median ESS 639/639/983/835); unsupported observed bins fall to 0 for singles
and 4 (cm) / 5 (cf) for couples (classified by S12-C as unrepresented
finite-panel region).

**G2 criterion** (addendum §Scope; builder
`build_positive_fit_diagnostics_v2b.py` l.373-376): "G2 is
`MCSE <= 0.25 * C5 sampling SD`", i.e. `adequate = monte_carlo_se <=
0.25*simulated_sd`, label ADEQUATE else QUADRATURE-LIMITED. The deck applies
it to the weighted, all-household row (the R6 rule it already used).

| group | extensive_accuracy weighted (ratio → label) | unweighted (ratio → label) | v2 weighted label | on slide? |
|---|---|---|---|---|
| couples_female | 0.0185 → ADEQUATE (89.8%) | 0.0129 → ADEQUATE | ADEQUATE (0.168) | yes (unchanged) |
| couples_male | 0.2398 → **ADEQUATE** (92.2%) | 0.2503 → QUADRATURE-LIMITED | QUADRATURE-LIMITED (0.323) | **yes — newly included** |
| singles_female | 0.1500 → ADEQUATE (85.7%) | 0.2218 → ADEQUATE | ADEQUATE (0.243) | yes (unchanged) |
| singles_male | 0.2998 → QUADRATURE-LIMITED | 0.3621 → QUADRATURE-LIMITED | QUADRATURE-LIMITED (0.300) | no — still withheld: MCSE 0.00595 exceeds 0.25×SD 0.00496 on the 2,048-node support |

**Node counts.** v2 `run_provenance.json` `predictive_support.full_nodes` = 100;
v2b `run_provenance.json` `nodes` = 2048 (= `support_record.csv`
`nodes_per_household` for all four groups). These are different objects. The
data slide now states both, labelled: the **estimation frame's drawn
alternatives per household** (`\FrameDraws` = 100, from v2b
`support_record_v2.csv` `continuous_nodes_per_household`, source panel
`s10_criterion_a_iid_r100`, which is the panel S11 is estimated on) and the
**diagnostic panel's common quadrature nodes per household** (`\FitNodes` =
2,048, from v2b `run_provenance.json`). B4 uses `\FitNodes` with that label.
Under v2 the single `\FitNodes` macro (100) served both roles.

**Caption decision.** "quadrature-limited; support audit pending" is no
longer true: v2b *is* the support-coverage audit. Replaced by "support
coverage audited (POSFIT v2b); calibration statistics partly
quadrature-limited; fit verdicts open pending Deputy review". Basis: on v2b
the weighted calibration-slope statistic `mz_slope` is ADEQUATE for cf/cm/sm
and QUADRATURE-LIMITED for sf (0.2501), and the per-bin reliability χ², PIT χ²
and outcome-gap statistics are QUADRATURE-LIMITED for nearly every
group/bin; the S12 alias memo states "The binding fit verdicts remain OPEN
pending Deputy review." `G-CAPTION` now checks the new caption and the absence
of "support audit pending". The fit-slide headline ("the one fit statistic
that passes") is reworded, since on v2b other statistics also pass.

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
| 2 | France, EU-SILC priced through EUROMOD | S11 frames via `baseline_f1_full_sample_aggregates_v1.json` (`samples.*.unweighted_n`); **estimation-frame draws per household** `\FrameDraws`=100 from `positive_fit_diagnostics_v2b/support_record_v2.csv` (`continuous_nodes_per_household`, criterion-A R100 panel); **diagnostic-panel quadrature nodes per household** `\FitNodes`=2,048 from `positive_fit_diagnostics_v2b/run_provenance.json` (`nodes`) — MNL_posfit `a2e80a8` |
| 2 | A job is a package (TikZ) | — (the 35-hour week is a statutory fact, not an estimate) |
| 2 | Preferences and the opportunity density in one likelihood | — |
| 3 | S11 model of record: free parameters | `s11_{singles,couples}_parameter_table_v1.csv` (non-pinned row counts); objectives (`objectives.*`) and evaluator commit from `positive_fit_diagnostics_v2b/run_provenance.json` (MNL_posfit `a2e80a8`) |
| 3 | Extensive-margin accuracy, shown only where it passes the gate | `positive_fit_diagnostics_v2b/g2_adequacy.csv` (MNL_posfit `a2e80a8`), weighted, scope `all`, `extensive_accuracy`, **ADEQUATE rows only**: coupled women 89.8%, coupled men 92.2% (**new in v2b**), single women 85.7%; single men withheld. Counts 3/1 from the same file; `\PosfitCommit` |
| 3 | Calibration conditioned on prediction | figure from `positive_fit_diagnostics_v2b/deciles.csv` (weighted); caption verbatim: *support coverage audited (POSFIT v2b); calibration statistics partly quadrature-limited; fit verdicts open pending Deputy review* |
| 4 | The access kernel is estimated | `s11_singles_parameter_table_v1.csv`, access block, ±1.96×CR1 |
| 4 | The earning-opportunity kernel | `s11_singles_parameter_table_v1.csv`, wage block; σ̂ and its z |
| 5 | Haydar–Maniquet W¹ | — |
| 5 | W¹ coincides with the staying-home equivalent | — |
| 6 | **Baseline W¹-F, equivalised, single adults (PRIMARY)** | `docs/results/JMP_BASELINE_F1_equivalised_reporting_v1.md`, commit `4c4e07e`, over the verified construction `MNL/outputs/welfare/baseline_f1_v1/baseline_f1_full_sample_report_v1.md`, commit `6048c9f`, verified `b5550af`. Machine-readable source read directly by `make_deck_numbers_r6.py`: `MNL/outputs/welfare/baseline_f1_equivalised_v1/singles_equivalised_reporting_v1.json`. `C_eq`/`W_F_eq` weighted mean/median/Gini (Gini to 6 d.p.: **0.263292 → 0.249807**). Scale: ratified modified-OECD, Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING" s1, memo `JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md` (filed at `docs/normative/`, commit `307e1a6`) |
| 6 | **Baseline W¹-F, equivalised, couples (PRIMARY)** | same memo/commits; `MNL/outputs/welfare/baseline_f1_equivalised_v1/couples_equivalised_reporting_v1.json`. Gini **0.226805 → 0.197403**. Same ratified-scale citation |
| 7 | Four operators | — (operators only; no magnitude; $P$ label text is hand-authored per the Deputy/PI ruling, not a computed numeral) |
| 7 | The open problem: observed vs counterfactual bundle | — |
| 8 | Where the decomposition stands | — |
| 8 | What I would like from you today | — |
| B1 | **Baseline W¹-F, unequivalised, single adults (backup)** | `MNL/outputs/welfare/baseline_f1_v1/baseline_f1_full_sample_report_v1.md`, commit `6048c9f`, verified `b5550af`. N, weighted mean, median, Gini, worker/non-worker counts |
| B2 | **Baseline W¹-F, unequivalised, couples (backup)** | same file and commits; couples row |
| B3 | Baseline W¹-F pre-registered checks | `baseline_f1_full_sample_aggregates_v1.json` → `checks.*` (C1, C2, C5) |
| B4 | The G2 quadrature-adequacy gate | `positive_fit_diagnostics_v2b/g2_adequacy.csv` (three ADEQUATE rows incl. coupled men; single men withheld) + `positive_fit_diagnostics_v2b/run_provenance.json` (`node_bootstrap.replicates`=200, `nodes`=2,048 common quadrature nodes per household, `simulation.draws`=500) — MNL_posfit `a2e80a8` |
| B5 | Authority for what is and is not on these slides | — (E3-EQ row now also records the scale ratification, SCALE CLOSED s1) |

Units, on every welfare slide: primary (§6) **EUR/month, household-equivalised
(ratified modified-OECD scale, Deputy ruling "SCALE CLOSED; CHILD-SHIFTER
FRAMING" s1)**, survey weight `dwt`; backup (B1/B2) **household EUR/month,
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

**Retired in DECK-3**

- the **"PROVISIONAL, pending economics review" equivalence-scale label** and
  every variant (units caveat, §6 notes, B2 note, B5 row), and the generator
  guard that required the `PROVISIONAL_PENDING_ECONOMICS_REVIEW` string —
  superseded by the Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING" s1;
  `G-SCALE` guards non-recurrence
- **POSFIT v2 sourcing** (`MNL_posfit/outputs/positive_fit_diagnostics_v2/`,
  R100 support) for the fit slide, calibration figure, data slide, S11 table
  objectives and B4 — superseded by v2b (`a2e80a8`)
- the single **`\FitNodes` = 100** macro that conflated estimation draws with
  diagnostic nodes (now `\FrameDraws` = 100 and `\FitNodes` = 2,048)
- the calibration caption **"quadrature-limited; support audit pending"** and
  the §8 "Open: the support audit …" bullet (the audit is done in v2b)
- the fit-slide headline "the one fit statistic that passes the
  quadrature-adequacy gate" (false on v2b)

The v4.1 deck itself is not deleted and not rebuilt: it is the historical
artifact R2 preserves, and `make v41` refuses to build it without an explicit
command.

## What replaced it

§6, equivalised primary distribution (this revision) plus §8, *Where the
quantitative welfare decomposition stands*: **Settled** (measure, reference
domain, measure-correspondence audit, the equivalised and unequivalised
descriptive baselines) / **In design (R5)** (counterfactual attainment
operator; the choice between the realised-bundle and g-computation estimands)
/ **Open** (the binding positive-fit verdicts: support coverage audited in
POSFIT v2b, Deputy review pending — DECK-3 wording) / **Withdrawn** (every previously
reported welfare share; the singles/couples equivalised "near equality"
claim). No P/A/B/D share appears anywhere in the deck.

## Open items

- The committed equivalised JSONs in `MNL/outputs/welfare/baseline_f1_equivalised_v1/`
  still carry `scale_status = PROVISIONAL_PENDING_ECONOMICS_REVIEW` (they
  predate the ruling). The generator accepts that label or a `RATIFIED*`
  label; relabelling the artifacts is optional housekeeping in MNL.
- POSFIT: the binding fit verdicts remain open pending Deputy review (S12
  alias memo). Single men stay withheld on extensive accuracy under v2b;
  coupled men pass the weighted gate (0.2398) but not the unweighted one
  (0.2503) — the deck applies the weighted rule, disclosed in the fit-slide
  note.
- The counterfactual attainment estimand (R5) remains in design; no execution
  before the seminar per the freeze doc.
- `docs/normative/JMP_counterfactual_attainment_architecture_for_seminar_v1.md`
  does not exist and was not created (see item E above).
- Final P/A/B/D decomposition semantics (in particular the interpretation of
  $P$) remain work in progress, as now stated explicitly on the operators
  slide.

## Gates

`beamer/verify_deck_r6.py`, run by every build.

| Gate | What it enforces |
|---|---|
| G-RETIRE | none of the retired W1-EA tokens (24 original + 6 new out-of-scope tokens, merged into one map) appears in the source or the rendered text |
| G-NOSHARE | no Shapley/Owen/share language in the rendered deck |
| G-CAPTION | the calibration caption appears verbatim — DECK-3: the v2b caption, and "support audit pending" absent |
| G-UNITS | 2 equivalised (primary) + 2 unequivalised (backup) baseline slides each state units, weight and scale status |
| G-SOURCE | the baseline slides cite `6048c9f`, `b5550af`, and the E3-EQ memo `4c4e07e` |
| G-NUMBERS | no hand-typed quantitative numeral; every one comes from `deck_numbers_r6.tex` |
| G-G2 | only G2-**ADEQUATE** fit statistics reach a slide — DECK-3: reads v2b; every ADEQUATE group's extensive-accuracy macro is on a slide and no limited group's macro exists; every posfit source path is v2b |
| G-QA | all 8 welfare-section slides carry a Q&A note citing a ruling ID |
| G-NOCONF | no confusion-matrix headline statistic |
| G-POOLED | no pooled welfare figure |
| **G-NOSIDEBYSIDE** *(new)* | no frame or rendered paragraph mixes singles- and couples-equivalised levels; the withdrawn "near equality" claim never reappears |
| **G-EQPRIMARY** *(new)* | equivalised distribution is section 6, before `\appendix`; exactly 2 unequivalised slides are demoted to the backup appendix |
| **G-CHILDSHIFTER** *(new)* | the child-shifter sentence is present verbatim (whitespace-normalised); the shifter is never called a preference/taste parameter |
| **G-PLABEL** *(new)* | the $P$ label reads "systematic utility heterogeneity (tastes + reduced-form time constraints)" verbatim, with a "work in progress" caveat, and no P/A/B/D magnitude appears anywhere |
| **G-NOBAN** *(new)* | the six seminar-freeze out-of-scope tokens (W_EA, finite-offer welfare, finite-market-set welfare, OEC characterisation, OEC-CHAR, SCALE-SENS-1) are individually itemised and absent |
| **G-SCALE** *(DECK-3)* | the `\wfunitseq` caveat on both §6 slides cites Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING" and `JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md`; both render; no "provisional…" / "pending economics review" wording in the source or rendered deck |

Result of the last run (recorded in `beamer/build/JMP_seminar_deck_r6_build_log.txt`): **16/16 PASS**.

## ID scan (post-build)

DECK-3 scan: the 30 `RETIRED_TOKENS` entries (24 + 6), 3 "near equality"
phrasings, and 6 DECK-3 strings ("provisional", "pending economics review",
"PROVISIONAL pending economics review", "support audit pending",
`positive_fit_diagnostics_v2/` in plain and TeX-escaped form) — 39 in all —
were checked case-insensitively, whitespace-normalised, against the three
files below: **zero hits in all three.**

Earlier (DECK-2) scan: every forbidden token — the original 24 plus the 6 new item-F tokens plus 3
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
