# JMP First Extraction Batch (v1)

**Date:** 2026-06-02
**Prompt to use:** `06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md` for all
core papers; use `06_prompts/JMP_T2_focused_extraction_prompt_v2.md` only for the
EUROMOD infrastructure paper (Sutherland & Figari, in the "next 8").
**Tier source:** `00_admin/JMP_literature_tiers_expanded_v1.csv`.
**Selection rule:** Batch 1 (first 12) draws from the **unblocked T1A** papers
(PDF already in `Literature/`, legacy MD extraction present) plus the one
T1B foil model (Van Soest) read alongside the latent-jobs core. The two T1A
**decomposition foundations** with no portable PDF (Shorrocks 1982, Sastre &
Trannoy 2002) are pushed to Batch 2 — acquisition-lag is harmless because the
decomposition (Exercise B) is itself deferred behind a validated welfare layer
(project_state §6.2). **No paper in Batch 1 is blocked by a missing PDF.**

> Ordering logic, from the welfare spec / project state: the welfare layer is
> built on the **model + identification + welfare-core** papers, so those come
> first; the nearest competitor (JJT) is read early to lock the positioning; the
> decomposition-method papers cluster in Batch 2 because Exercise B is deferred.

**Status legend:** `pdf` = PDF in `Literature/`? · `md` = legacy MD extraction in
`Literature/md_extractions/` (re-verify with `ls` before running) · `blocks?` =
does a missing PDF block extraction now?

---

## Batch 1 — summarize NOW (12 papers, T1 v2 prompt)

| # | bibkey | author_year | tier | pdf | md | blocks? | reason (why first) |
|---|---|---|---|---|---|---|---|
| 1 | dagsvikLaborSupplyChoice2016 | Dagsvik & Jia 2016 | T1A | yes | yes | no | Core **identification** benchmark for the RURO/latent-jobs model; couples joint choice — the structural foundation everything else rests on. |
| 2 | dagsvikTHEORETICALPRACTICALARGUMENTS2014 | Dagsvik et al. 2014 | T1A | yes | yes | no | The latent-jobs **manifesto** (vs Van Soest/Hausman); grounds the modelling choice and the opportunity-density interpretation. |
| 3 | aabergeEvaluatingAlternativeRepresentations2009 | Aaberge et al. 2009 | T1A | yes | yes | no | **Choice-set construction** (fixed grid vs sampled alternatives); directly informs the 901/101-alternative resolution. |
| 4 | capeauEstimatingSimulatingRandom2015 | Capéau et al. 2015 | T1A | yes | yes | no | The explicit **RURO estimation recipe** closest to the JMP engine (opportunity density with education effects). Read as deterministic feasible sets (drop the "random" framing). |
| 5 | cappauGettingTiredWork2015 | Capéau & Decoster 2015/2016 | T1A | yes | yes | no | The **closest published prototype** to the JMP headline: a RURO preference-vs-opportunity welfare decomposition. Extract what to extend from two-way to three-way. |
| 6 | dagsvikCompensatingVariationHicksian2005 | Dagsvik & Karlström 2005 | T1A | yes | yes | no | **Welfare apparatus**: Hicksian CV / de Palma–Kilani machinery, analytic in shocks; supplies the secondary EV/CV (D3) forms. |
| 7 | bargainWelfareLaborSupply2013 | Bargain et al. 2013 | T1A | yes | yes | no | The **canonical empirical equivalent-income family** (rent / rent+wage / wage) the JMP welfare layer mirrors; its fixed-grid limitation is the JMP entry point. |
| 8 | bhattacharyaNonparametricWelfareAnalysis2015 | Bhattacharya 2015 | T1A | yes | yes | no | Benchmark **nonparametric discrete-choice welfare** (EV/CV from choice probabilities); also the anchor for the deferred stochastic-dominance extension. |
| 9 | shorrocksDecompositionProceduresDistributional2013 | Shorrocks 2013 | T1A | yes | yes | no | The **Shapley-value decomposition framework** (order-independence, exhaustiveness) — the rule behind the three-way split. (PDF in `Literature/`; its 1982 basis is in Batch 2.) |
| 10 | audolyPractitionersNoteShapleyOwenShorrocks2025 | Audoly et al. 2025 | T1A | yes | yes | no | The most **operational** Shapley-Owen-Shorrocks recipe for a structural model — the implementation bridge for Exercise B. |
| 11 | jacquetHowMuchDoes2026 | Jacquet et al. 2026 (JJT) | T1A | yes | yes | no | The **nearest competitor**; lock the positioning early (JJT vary the *preference* axis at two points; the JMP varies the *opportunity* axis across six measures — near-orthogonal). High overclaim risk — read carefully. |
| 12 | vansoestStructuralModelsFamily1995 | Van Soest 1995 | T1B | yes | yes | no | The **fixed-grid discrete-choice foil** the latent-jobs approach departs from; read alongside #1–#2 to sharpen the contrast (opportunity density = exactly what it lacks). |

**Batch 1 acquisition status:** all 12 PDFs are in `Literature/`. Nothing blocks
this batch. Re-confirm the 12 MD extractions exist (`ls Literature/md_extractions/`)
before running; if any is missing, run `improve_md_extractions.py` on that PDF.

---

## Batch 2 — summarize NEXT (8 papers)

| # | bibkey | author_year | tier | pdf | md | blocks? | reason (why second) |
|---|---|---|---|---|---|---|---|
| 13 | shorrocksInequalityDecompositionFactor1982 | Shorrocks 1982 | T1A | **no** | no | **yes (acquire)** | Factor-decomposition **foundation** (Econometrica) the 2013 framework generalizes. PDF in Zotero `files/` only — **acquire to `Literature/` first** (acquisition queue rank 2). Lag is fine: Exercise B is deferred. |
| 14 | sastreShapleyInequalityDecomposition2002 | Sastre & Trannoy 2002 | T1A | **no** | no | **yes (acquire)** | Practical **Shapley implementation** issues (zero-contribution, elimination order). Acquire to `Literature/` first (acquisition queue rank 1). |
| 15 | beffyLabourSupplyTaxation2019 | Beffy et al. 2019 | T1B | yes | yes | no | **Restricted-choice** identification (preferences vs choice-set distribution from at-most-two-offers); directly on the separation problem. |
| 16 | aabergeUsingMicroeconometricModel2013 | Aaberge & Colombino 2013 | T1B | yes | yes | no | Published **RURO benchmark** (opportunity-measure parameterization); companion to #17. |
| 17 | aabergeColombinoStructural2018 | Aaberge & Colombino 2018 | T1B | yes | yes | no | RURO + microsimulation **tradition anchor** (welfare spec §4). **No bib entry — add it** (repair queue D2) before citing; extraction not blocked (PDF + MD present). |
| 18 | aabergeLaborSupply1995 | Aaberge, Dagsvik & Strøm 1995 | T1B | yes | yes | no | The **original RURO paper**; opportunity-set + welfare effects. **No bib entry — add it** (repair queue D1); extraction not blocked. |
| 19 | bhattacharyaEmpiricalWelfareAnalysis2018 | Bhattacharya 2018 | T1B | yes | yes | no | General nonparametric discrete-choice welfare; **companion to #8**, read together. |
| 20 | capeauNonparametricWelfareAnalysis2021 | Capéau et al. 2021 | T1B | yes | yes | no | **Fleurbaey-style** discrete-choice welfare (distribution of individual welfare); closest to the JMP welfare construction. |

**Batch 2 acquisition status:** 6 of 8 are unblocked (PDF + MD in `Literature/`).
Two (#13 Shorrocks 1982, #14 Sastre & Trannoy 2002) are **blocked until their
PDFs are copied from Zotero `files/` into `Literature/`** and extracted — handle
via the acquisition queue (ranks 1–2). Two unblocked papers (#17, #18) need a
**bib entry added** before they can be *cited*, but their **extraction is not
blocked**.

---

## Notes carried into both batches (from the v2 prompts)

- Use the **three-way access / ability / preference** vocabulary, not the old
  two-factor cut. For #5 (Capéau & Decoster) and #11 (JJT), explicitly record how
  their two-way / two-point designs map onto the three channels.
- Place every welfare paper (#6, #7, #8, #19, #20) on the **$W^1$–$W^6$** map.
- Force the **proposal/prior correction** extraction for every RURO/estimation
  paper (#1–#5, #15–#18).
- Keep **occupation (`loc4`, ISCO) ≠ industry/sector (`lindi`, NACE)**; flag any
  conflation (watch #4 and Dagsvik–Strøm-style "sectoral" language if it recurs).
- Maintain the **empirical-JMP vs theory-paper boundary**: #6, #7, #20 and the
  Fleurbaey/Decancq primitives are cited readings, not JMP-original theory.

## Deliberately NOT in the first 20

Decomposition-method T3 background (Chantreuil & Trannoy, Tido Takeng), the IOp
measurement papers (Ferreira & Gignoux, Bourguignon et al., Checchi & Peragine,
Van de gaer & Ramos, Mahler & Ramos), the fairness primitives beyond
Fleurbaey–Maniquet 2018 (#22 in tiers, not in first 20), and EUROMOD
(Sutherland & Figari, T1B but extract with the **T2** prompt as infrastructure)
are sequenced after the model + welfare core is summarized, consistent with the
build order in the protocol report §8.
