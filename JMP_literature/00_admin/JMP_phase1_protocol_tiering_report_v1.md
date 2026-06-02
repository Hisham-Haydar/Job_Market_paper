# JMP Literature Rebuild — Phase 1 Protocol & Tiering Report (v1)

**Date:** 2026-06-02
**Phase:** 1 — Protocol alignment + disciplined tiering + first extraction batch
**Inputs read (Phase 0 + project state):**
`00_admin/JMP_existing_corpus_inventory_v1.csv`,
`00_admin/JMP_existing_bibtex_audit_v1.md`,
`00_admin/JMP_pdf_inventory_v1.csv`,
`00_admin/JMP_literature_rebuild_decision_log_v1.md`,
`summary_T1.md`, `summary_T2.md`, `tiers.csv`,
`JMP_project_state_v1.md`, `JMP_welfare_spec_v5.md`,
`JMP_lit_collection/JMP_lit_collection.bib`,
`JMP_literature/JMP_literature_rebuild_plan_v3_update.md`.

**Outputs produced this phase:**
1. `00_admin/JMP_phase1_protocol_tiering_report_v1.md` (this file)
2. `00_admin/JMP_literature_tiers_expanded_v1.csv`
3. `00_admin/JMP_missing_pdf_acquisition_queue_v1.csv`
4. `00_admin/JMP_bibtex_repair_queue_v1.md`
5. `06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md`
6. `06_prompts/JMP_T2_focused_extraction_prompt_v2.md`
7. `00_admin/JMP_first_extraction_batch_v1.md`

**Scope discipline:** This phase did **not** summarize papers, did **not**
run external searches, and did **not** open PDFs to verify metadata. All
metadata uncertainties are carried forward as `[verify]` / `metadata_needs_verification`
rather than guessed. No Phase 0 work was repeated.

---

## 0. The single most important correction this phase makes

`summary_T1.md` and `summary_T2.md` both anchor on an **outdated two-factor**
decomposition:

> "a two-factor Shapley-Shorrocks decomposition of the household welfare Gini
> into an opportunity-driven component and a preference-driven component."

The current authoritative design — `JMP_welfare_spec_v5.md` (carried forward
from v3) and `JMP_project_state_v1.md` §6.1 — is **three-way**:

> **access / ability / preference**, attributed by Shapley-Shorrocks
> equalisation, where
> - **preference** = the utility block $v$ (Box-Cox tastes over consumption,
>   leisure, children-time): 20 params;
> - **ability** = the wage-technology sub-block of the opportunity density $g$
>   (returns to own education and experience, residual productivity $\sigma$):
>   6 params; this is the *Independence-of-$y$* / pay dimension;
> - **access** = the rest of $g$ (employment/hours availability, region,
>   urbanisation, year, and gender-specific occupation offers): 23 params; this
>   is the *Independence-of-$A$* / set dimension.

"Opportunity" survives only as the **union of access + ability** (the
upper-bound opportunity share), with **access alone** as the lower bound. The
v2 extraction prompts must therefore force a *three-way* mapping, never a
two-way one. The revised T1/T2 prompts (outputs 5-6) implement this.

A second, equally binding correction: the welfare object is no longer a single
measure but the **characterised family $W^1,\dots,W^6$** spanning a
compensation-responsibility spectrum (welfare spec §1.3). Extraction must locate
every source on the $W$-family map (which references / Ind-$y$ / Ind-$A$
properties it speaks to), not merely ask "does it compute a money-metric."

A third: the **"random opportunities" framing is removed** (welfare spec
V3-5). Opportunities are **deterministic** feasible sets, as in the companion
theory paper. This re-grounds how RURO/RURO-adjacent sources (Capéau-Decoster-Dekkers
2015 in particular) are read — the "RO" in RURO is retained as estimation
machinery, not as a claim that opportunities are random.

---

## 1. How the two tier sources were reconciled

There are two pre-existing, **disagreeing** tier signals:

| Source | Granularity | Basis |
|---|---|---|
| `tiers.csv` | T1 / T2 / T3, 84 keys | local hand-tiering already begun (15 T1, 25 T2, 44 T3) |
| inventory `preliminary_tier` | Tier 1 / Tier 2 / Tier 3 / not_central, 87 rows | drawn from the deep-research reports + gap check |

These were **not** treated as authoritative. Per the rebuild plan v3 directive
("Do not rigidly follow the current tiers.csv if the alignment audit recommends
changes") and the explicit instruction not to treat preliminary Tier 1 labels
as final Tier 1, both signals are recorded verbatim in the expanded CSV
(`current_tier_from_tiers_csv`, `preliminary_tier_from_inventory`) and a
**`final_recommended_tier`** was assigned by the rule in §2 below, anchored to
the welfare spec and project state rather than to either prior list.

The expanded CSV covers **98 entries** — the 87 inventory rows plus 11
PDF-or-MD-only items surfaced by the PDF inventory that have no confirmed bib
key (the year-only Fleurbaey/Maniquet files, `Jones_Klenow_2016`,
`Aaberge et al. 1995`, `Aaberge et al. 1999`, `Bargain_Peichl_2016`,
`chapter_10/11`, `Equal_Opportunity...`, `Valetta_2010`). Two bare stubs
(`GDPQuestMeasure`, `WelfareLossCaused`) are **not** carried as their own rows:
`GDPQuestMeasure` is folded into `fleurbaeyGDPQuestMeasure2009` (delete-the-stub),
and `WelfareLossCaused` is carried as `caloBlancoGarciaPerez2014` (DEFER, replace-the-stub).

---

## 2. The disciplined final-tier rule

Final tiers are assigned by **proximity to the JMP's load-bearing machinery**,
defined by the project state and welfare spec, not by general topical interest.

- **T1A — summarize immediately; core to identification / model / welfare /
  decomposition.** A paper is T1A only if it is *operationally* reused in one of
  the four load-bearing layers: the RURO/latent-jobs estimation and its
  identification; the inclusive-value money-metric welfare construction and the
  $W^1$-$W^6$ family; the Shapley-Shorrocks decomposition rule; or the single
  nearest competitor (JJT 2026). 13 papers.
- **T1B — summarize after T1A; important but not first batch.** Core-adjacent:
  the contrast model the JMP defines itself against (Van Soest), the second-tier
  identification and welfare papers, the cited normative primitives that anchor
  the spectrum framing, and EUROMOD as infrastructure. 10 papers.
- **T2 — selective summary.** Important context that is cited but not reused as
  machinery: IOp measurement, fairness primitives, welfare-method comparators,
  the France couples baseline, demand-side rationing. 19 papers.
- **T3 — background / citation only.** Bib entry sufficient; full extraction not
  required. 50 papers.
- **DEFER — later extension.** Not needed for the baseline; acquire/extract only
  if a named extension activates (stochastic dominance, poverty angle, Shapley
  game-theory footnote). 3 papers.
- **REJECT — not useful for this JMP.** Peripheral accumulations flagged in the
  bibtex audit §5. 3 papers.

**Counts:** T1A 13 · T1B 10 · T2 19 · T3 50 · DEFER 3 · REJECT 3 = **98**.

### 2.1 Notable disagreements resolved (why a tier moved)

**Promotions (tiers.csv or inventory under-tiered relative to the welfare spec):**

- `cappauGettingTiredWork2015` (Capéau & Decoster) — **T3 → T1A.** This is the
  *closest published prototype to the JMP headline*: a RURO preference-vs-opportunity
  welfare decomposition. tiers.csv badly under-tiered it at T3. It must be read first.
- `capeauEstimatingSimulatingRandom2015` (Capéau-Decoster-Dekkers) — **T2 → T1A.**
  The explicit RURO estimation recipe closest to the JMP engine.
- `bargainWelfareLaborSupply2013` — **T2 → T1A.** project_state §2.1 names this
  the "canonical empirical statement" the JMP welfare layer mirrors; its
  fixed-grid limitation is the JMP's stated entry point.
- `audolyPractitionersNoteShapleyOwenShorrocks2025` — **T2 → T1A.** Most directly
  operational decomposition recipe for a structural model.
- `peichlAccountingLaborDemand2012` — **tiers.csv T3 → T2** (and inventory
  Tier 1 → T2): relevant to the access channel via demand-side rationing.
- `decancqGDPUsingEquivalent2016`, `fleurbaeyGDPQuestMeasure2009` — **T3 → T2**:
  supply the equivalent-income principles, with a boundary caveat (not a
  beyond-GDP ranking goal).
- `aabergeColombinoStructural2018`, `aabergeLaborSupply1995`,
  `aaberge1999LabourSupplyItaly` — **surfaced / promoted** as RURO-tradition
  anchors the welfare spec §4 cites by name; all need bib entries.

**Demotions (preliminary Tier 1 that is not final Tier 1):**

- `ferreiraMEASUREMENTINEQUALITYOPPORTUNITY2011`,
  `bourguignonINEQUALITYOPPORTUNITYBRAZIL2007`,
  `checchiInequalityOpportunityItaly2010`,
  `mahlerEqualityOpportunityFour2019`,
  `vandegaerMeasurementInequalityOpportunity2020` — **Tier 1 → T2/T3.** These are
  reduced-form **IOp-on-outcomes** papers. The JMP decomposes **money-metric
  welfare** inequality from a structural model; IOp measurement is context, not
  the JMP object. Important but not load-bearing.
- `chettySufficientStatisticsWelfare2009` — **tiers.csv T1 → T3.** Introduction
  positioning only; the JMP is fully structural, not sufficient-statistics.
- `aabergeDesigningOptimalTaxes2006` — **tiers.csv T1 → T3.** Superseded by the
  published `aabergeUsingMicroeconometricModel2013`.
- `bloemenModelLabourSupply2000`, `bloemenJobSearchHours2008` — **inventory
  Tier 1 → T3.** Search-theoretic offer constraints are a *different paradigm*
  from the RURO offer density; useful context, not the model.
- `hufeMeasuringUnfairInequality2022` — **kept T2, NOT promoted to T1** despite
  rebuild_plan_v3's "may need T1." Rationale: the current welfare spec imports
  fairness as **cited primitives** and carries "zero theory load"; the fairness
  machinery is not reused, so T2 is correct.

**Rejections / defers** follow the bibtex audit §5 (Anand 2011, Osberg-Sharpe
2002, Duro-Esteban 1998 → REJECT; Roth 1988, Calo-Blanco 2014, Brunori 2013b →
DEFER).

---

## 3. Protocol-alignment verdict on the existing prompts

### 3.1 Is `summary_T1.md` sufficient as the canonical T1 prompt? **No.**

It is a strong, retrieval-oriented base (16 sections, correct emphasis on RURO,
welfare, Shapley, overclaim risk) but it is **insufficient and partly outdated**
for the current JMP. Specific gaps, each fixed in the v2 T1 prompt:

| Gap in `summary_T1.md` | Fix in T1 v2 |
|---|---|
| Two-factor opportunity/preference decomposition (outdated) | Three-way **access / ability / preference**, with the param-block membership and the access-only vs access+ability bounds |
| No $W^1$-$W^6$ family mapping | New section forcing placement on the compensation-responsibility spectrum (Ind-$y$ / Ind-$A$) |
| Inclusive value / money-metric inversion under-specified | Explicit section on the ex-ante log-sum, the inversion, and the **mandatory proposal/prior correction** $-\log\pi$ |
| Proposal correction / sampling-of-alternatives not forced | Dedicated extraction point |
| Couples joint choice not forced | Dedicated extraction point (joint utility, joint budget, one object per couple) |
| Occupation-conditioned wage draws not addressed | Dedicated point + the **ISCO/occupation ≠ NACE/industry** discipline |
| Inference / bootstrap / simulation error / numerical implementation absent | New section (cluster bootstrap, ESS/importance-sampling, JAX-pipeline lessons) |
| Theory-paper boundary not stated | New rule: import normative readings as **cited primitives**, never reproduce the companion Haydar-Maniquet characterisation |

The lean `summary_T1.md` is **retained** (rebuild_plan_v3 suggests keeping it as
`JMP_T1_lean_extraction_prompt_v1.md`); the v2 exhaustive prompt is the
**canonical** prompt for T1A/T1B core papers.

### 3.2 Is `summary_T2.md` sufficient as the canonical T2 prompt? **Almost.**

It is appropriately shorter and correctly scoped to supporting papers, but it
carries the **same outdated two-factor language** and lacks the $W$-family and
proposal-correction hooks. The v2 T2 prompt corrects the decomposition language,
keeps the non-contiguous section numbers aligned to the T1 template (for
indexing), and stays short.

### 3.3 Coverage check (rebuild_plan_v3 §3 questions), against welfare spec v5

| Required coverage | In summary_T1 as-is? | In T1 v2? |
|---|---|---|
| latent jobs / RURO | partial | yes |
| constrained opportunities / opportunity density | partial | yes |
| proposal correction | no | yes |
| wage ability | no (folded into "opportunity") | yes (own ability dimension) |
| access / market opportunity | no (two-factor only) | yes (access dimension) |
| occupation-conditioned wage draws | no | yes |
| couples joint choice | no | yes |
| inclusive value | partial | yes |
| money-metric welfare | yes | yes (expanded) |
| $W^1$-$W^6$ welfare family | no | yes |
| responsibility / EOp | yes | yes |
| Shapley access/ability/preference decomposition | no (two-way) | yes (three-way) |
| microsimulation / EUROMOD | partial | yes |
| inference, bootstrap, simulation error, numerics | no | yes |
| contribution mapping + overclaim warnings | yes | yes (expanded) |

---

## 4. Empirical-JMP vs theory-paper boundary (preserved throughout)

Per project_state §1.3 / §6.3 and welfare spec §1.3, there is a **separate**
purely axiomatic theory paper (Haydar-Maniquet, in progress) that *characterises*
$W^1$-$W^6$. The empirical JMP **imports** the measures and their normative
readings as **cited primitives** and re-derives nothing. Consequences enforced in
the prompts and tiers:

- Fleurbaey/Maniquet/Decancq/Roemer entries are tiered as **normative-interpretation**
  cited primitives, with `do_not_cite_for = JMP-original theory` and a
  BOUNDARY overclaim warning.
- The T1/T2 v2 prompts instruct the extractor never to attribute the
  companion paper's axioms/proofs to the JMP, and never to read the JMP as a
  theory contribution.
- The unidentified `Fleurbaey_maniquet_{2017,2018,2019}` / `Maniquet2008` /
  `Fleurbaey_1995` PDFs are tagged `[verify]` and **must be identified before
  citation**, precisely because some may belong to the theory stream.

---

## 5. Terminology discipline carried into every output

From project_state §3.4 and the welfare spec, enforced in prompts and flagged in
the tiers `overclaim_warning` field:

- **Occupation** = `loc4` (a four-category task variable derived from the
  ISCO-type field); it is an **access/opportunity** object, entering $g$ only,
  never utility and never the structural wage return.
- **Industry / sector** = `lindi` (NACE); a **reserved, deferred** robustness
  variable, not in the baseline.
- Sources that say "sectoral" (e.g. Dagsvik-Strøm 2006) must **not** be read as
  speaking to the JMP occupation channel; the prompt forces flagging any
  conflation.

---

## 6. PDF / extraction coverage summary (drives outputs 3 and 7)

From the inventory and PDF inventory:

- **71** of 98 entries have a portable PDF in `Literature/`; **27** do not
  (PDF only in Zotero `files/`, or no PDF at all).
- Most `Literature/` PDFs already have an MD extraction in
  `Literature/md_extractions/` (the legacy pipeline). The expanded CSV marks
  `md_extraction_status` conservatively: `yes` where the PDF is in `Literature/`
  and a legacy extraction is known to exist; `no_MD` / `has_MD` otherwise, with
  `[verify]` where uncertain. **These MD flags should be reconciled against an
  actual `ls md_extractions/` before the first extraction run** (a mechanical
  Phase-1 follow-up, not done here to avoid asserting unverified states).
- The acquisition queue (output 3) lists the 27 no-PDF entries by priority; the
  first extraction batch (output 7) is built **only from T1A/T1B entries whose
  PDF is already in `Literature/`**, so no acquisition blocks the first batch.

---

## 7. What Phase 1 deliberately did NOT do

- Did not open PDFs → all title/author/DOI uncertainties remain `[verify]`.
- Did not run `improve_md_extractions.py` / `build_full_literaterature.py`.
- Did not edit `JMP_lit_collection.bib` → repairs are queued (output 4), not applied.
- Did not run Deep Research (per rebuild_plan_v3: a targeted gap audit comes
  *after* the first inventory + first batch).
- Did not summarize any paper.

---

## 8. Recommended Phase 1 execution order

1. Apply the BibTeX repair queue (output 4) to `JMP_lit_collection.bib`.
2. Acquire the **T1A/T1B** PDFs in the acquisition queue (output 3) that are
   missing from `Literature/` — only Shorrocks 1982 and Sastre-Trannoy 2002
   among first-batch-relevant items.
3. Reconcile `md_extraction_status` against `ls Literature/md_extractions/`.
4. Run the **first extraction batch** (output 7): 12 now, 8 next, using the
   **T1 v2** prompt for core papers and **T2 v2** for EUROMOD/infrastructure.
5. Only then commission the targeted Deep Research gap audit.

All subsequent tier changes should edit `JMP_literature_tiers_expanded_v1.csv`
and bump it to `_v2`; this report is the rationale of record for v1.
