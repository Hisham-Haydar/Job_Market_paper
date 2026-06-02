# JMP Literature Library Rebuild — Decision Log v1
**Date:** 2026-06-02
**Phase:** 0 — Inventory and audit of existing corpus
**Purpose:** Record what the existing corpus contains, what is missing, what needs to be fixed, and what decisions drive the rebuild structure going forward.

---

## Context

This document records the decisions and findings from Phase 0 of the JMP literature library rebuild. The existing corpus is centered in `JMP_lit_collection/JMP_lit_collection.bib` (87 entries), `Literature/` (73 PDFs), `Literature/md_extractions/` (72 markdown extractions), and four deep research / gap-check reports in `Deep_reports/`. The goal of the rebuild is to create a clean, well-organized, actionable literature library under `JMP_literature/` that supports the JMP's six research "shelves" and enables the empirical prototype.

---

## Decision 1: Rebuild location and naming

**Decision:** New library lives under `JMP_literature/` with subdirectory `00_admin/` for management files.

**Rationale:** Keeps the new structured library separate from the legacy `Literature/` pipeline without overwriting existing extractions. The `Literature/` folder and its scripts (`improve_md_extractions.py`, `build_full_literaterature.py`, `make_shelves.py`) remain untouched and functional. The rebuild adds structure on top, not a replacement.

**Implication:** All Phase 0 output files go to `JMP_literature/00_admin/`. Future phases will add per-shelf subdirectories under `JMP_literature/`.

---

## Decision 2: What counts as "in the corpus" for inventory purposes

**Decision:** A paper is counted as "in the corpus" if it has at least one of: (a) a BibTeX entry, (b) a PDF in `Literature/`, (c) a markdown extraction in `Literature/md_extractions/`. Papers appearing only in deep research reports as *recommendations* are tracked as "missing" rather than "in corpus."

**Rationale:** The three artifacts (bib, PDF, extraction) correspond to distinct stages of the pipeline. A paper can be cited without a PDF (bib-only), have a PDF without an extraction (PDF-only), or be mentioned in a report without either. Tracking this three-way coverage is the main utility of the Phase 0 inventory.

**Known gaps found:**
- Aaberge, Dagsvik & Strøm 1995: has PDF and MD extraction, **no bib entry**
- chapter_10 / chapter_11: have PDFs and MD extractions, **no identifiable bib entries**
- 17 papers: have bib entries, **no PDF in `Literature/`** (PDFs may be in Zotero's internal `files/` tree)

---

## Decision 3: Six JMP buckets map to the six shelves

**Decision:** The `likely_JMP_bucket` field in the inventory CSV uses the same six-shelf vocabulary as `Literature/make_shelves.py` and `CLAUDE.md`, plus five additional operational categories needed for the inventory.

**Six canonical shelves (from CLAUDE.md):**
1. `latent_jobs_RURO_opportunity_sets`
2. `random_utility_welfare` (covers "welfare measurement for discrete choice")
3. `money_metric_equivalent_income` (covers "equivalent income / beyond-GDP")
4. `responsibility_equality_of_opportunity` (covers "responsibility/compensation/fairness")
5. `inequality_of_opportunity_decomposition` (covers "inequality of opportunity & decomposition")
6. `microsimulation_tax_benefit`

**Additional categories added for inventory purposes:**
- `structural_labor_supply` — papers primarily about structural LS methodology without the explicit opportunity-set / RURO framing
- `Shapley_decomposition_inequality` — decomposition methodology papers (cross-cutting shelves 5 and 6)
- `wage_offer_occupation_distribution` — wage offer distributions and job attributes (currently thin in corpus)
- `simulation_inference_bootstrap` — identification and simulation methodology
- `motivation_positioning` — papers used for introduction positioning (e.g., Chetty 2009)
- `not_central_or_background` — clearly peripheral entries

**Rationale:** The six-shelf system is authoritative for the final library structure. The additional categories are working labels for the transition period and will be collapsed into shelves during Phase 1.

---

## Decision 4: Tier system for prioritization

**Decision:** Three tiers are used in the inventory, derived primarily from `LIT_deep-research-report.md` and `JMP_gap_check_v1.md`:

- **Tier 1** — Core papers for the JMP's exact direction. Must be read closely, cited, and have a clean bib entry + PDF + extraction.
- **Tier 2** — Important extensions and supporting papers. Should have clean bib entry and PDF; extraction desirable.
- **Tier 3 (background)** — Background or context papers. Bib entry sufficient; full extraction not needed.
- **not_central_or_background** — Papers that appear to be peripheral, duplicated, or accumulated during early searches.

**Note:** Tier assignments in v1 are preliminary and drawn from the deep research reports. They should be confirmed against the actual paper contents during Phase 1.

---

## Decision 5: Papers to add to the corpus (from gap check)

From `JMP_gap_check_v1.md`, the following papers are confirmed as essential additions not currently in `Literature/` with a proper bib entry + PDF. They must be sourced, added to bib, and have extractions created.

### Tier 1 additions — must acquire

| Paper | Year | Journal | Gap-check label |
|---|---|---|---|
| Shorrocks 1982 — Inequality Decomposition by Factor Components | 1982 | Econometrica | decomposition foundation |
| Sastre & Trannoy 2002 — Shapley inequality decomposition by factor components | 2002 | Journal of Economics | Shapley implementation |
| Checchi & Peragine 2010 — Inequality of opportunity in Italy | 2010 | Journal of Economic Inequality | EOp decomposition |
| Van de gaer & Ramos 2020 — Measurement of inequality of opportunity based on counterfactuals | 2020 | Social Choice and Welfare | counterfactual EOp |
| Calo-Blanco & García-Pérez 2014 — On the welfare loss caused by inequality of opportunity | 2014 | Journal of Economic Inequality | welfare loss |
| Peichl & Ungerer 2016 — Accounting for the spouse when measuring inequality of opportunity | 2016 | Social Choice and Welfare | household EOp |
| Mahler & Ramos 2019 — Equality of Opportunity in Four Measures of Well-Being | 2019 | Review of Income and Wealth | well-being EOp |
| Hufe, Kanbur & Peichl 2022 — Measuring Unfair Inequality | 2022 | Review of Economic Studies | unfair inequality |
| Bosmans, Dormans & Öztürk 2025 — Failure to compensate or failure to reward? | 2025 | Journal of Economic Inequality | compensation/reward decomp |

**Status of above in current corpus:** All nine have BibTeX entries (added during recent bib updates) but only some have PDFs in `Literature/` and none have MD extractions. **Action for Phase 1:** Copy PDFs to `Literature/`, run `improve_md_extractions.py`, run `build_full_literaterature.py`.

### Tier 2 additions — acquire if possible

| Paper | Year | Journal | Gap-check label |
|---|---|---|---|
| Chantreuil & Trannoy 2013 — Inequality decomposition values | 2013 | Journal of Economic Inequality | decomposition axioms |
| Bosmans & Öztürk 2021 — Measurement of inequality of opportunity: A normative approach | 2021 | Journal of Economic Inequality | normative EOp |
| Fleurbaey & Peragine 2013 — Ex Ante Versus Ex Post Equality of Opportunity | 2013 | Economica | ex ante/ex post |
| Brunori et al. 2019 — Upward and downward bias | 2019 | Social Choice and Welfare | measurement bias |
| Palomino et al. 2019 — Channels of Inequality of Opportunity | 2019 | Social Indicators Research | channels decomp |
| Almås et al. 2011 — Measuring unfair (in)equality | 2011 | Journal of Public Economics | responsibility-sensitive meas. |

**Status:** BibTeX entries exist; PDFs are in Zotero `files/` but not in `Literature/`.

### Tier 3 / possible blind spots

| Paper | Year | Journal | Gap-check label |
|---|---|---|---|
| Brunori et al. 2013 — Opportunity-Sensitive Poverty Measurement | 2013 | IZA DP | opportunity-sensitive welfare |
| Tido Takeng et al. 2023 — Decompositions via Shapley-Owen value | 2023 | Theory and Decision | Owen grouped decomp |
| Kabátek et al. 2014 — France couples discrete choice | 2014 | Labour Economics | France couples baseline |

---

## Decision 6: BibTeX cleanup required before rebuild

The following changes must be made to `JMP_lit_collection.bib` before Phase 1 proceeds (from `JMP_existing_bibtex_audit_v1.md`):

1. **DELETE** `GDPQuestMeasure` stub entry (duplicate of `fleurbaeyGDPQuestMeasure2009`)
2. **REPLACE** `WelfareLossCaused` stub with full Calo-Blanco & García-Pérez 2014 entry
3. **ADD** Aaberge, Dagsvik & Strøm 1995 (PDF already in `Literature/`)
4. **ADD** entries for `chapter_10.pdf` and `chapter_11.pdf` once source is identified
5. **FIX** author/date in `cappauGettingTiredWork2015` (Capéau not Cappau; date 2016 vs 2015)
6. **ADD** DOIs for 16 journal articles with JSTOR-URL-only entries
7. **FIX** `Chapter34Welfare2002` — add missing `author` field

---

## Decision 7: Papers with ambiguous filenames — resolution needed

The following PDFs have filenames that do not carry enough information to confirm a bib match without opening the file. These are flagged [verify] in the PDF inventory.

| Filename | Issue | Action |
|---|---|---|
| `Fleurbaey_1995.pdf` | Year-only; multiple 1995 Fleurbaey papers possible | Read MD extraction to confirm |
| `Fleurbaey_maniquet_2017.pdf` | Title unknown; may duplicate bib entries | Read MD extraction; check for overlap with 2018 JEL paper |
| `Fleurbaey_maniquet_2018.pdf` | Possibly same as `fleurbaeyOptimalIncomeTaxation2018` | Confirm via MD extraction |
| `Fleurbaey_maniquet_2019.pdf` | Title unknown | Read MD extraction |
| `Maniquet2008.pdf` | Title unknown | Read MD extraction |
| `Valetta_2010.pdf` | Title unknown; possibly Valletta not Valetta | Read MD extraction; correct spelling if needed |
| `Equal_Opportunity_or_Equal_Social_Outcom.pdf` | Title truncated | Read MD extraction; identify paper |
| `chapter_10.pdf` / `chapter_11.pdf` | No author/title | Read MD extraction; identify handbook source |
| `Bargain_Peichl_2016_Own-wage labor supply elasticities.pdf` | Bib entry not confirmed | Locate bib entry or add one |
| `Jones_Klenow_2016_Beyond GDP.pdf` | Bib entry not confirmed in scan | Locate bib entry |
| `J Public Economic Theory - 2007 - FLEURBAEY - ...pdf` | Bib entry not confirmed | Locate bib entry |

---

## Decision 8: Aaberge & Colombino 2018 — structural microsimulation paper

**Issue:** `Aaberge_Colombino_2018_Structural labour supply models and microsimulation.pdf` has a PDF and MD extraction but no BibTeX entry was found in the bib scan.

**Rationale:** This paper (International Journal of Microsimulation 11(1): 162–197) is cited as a benchmark in `LIT_deep-research-report.md` (Tier 2). It is a natural companion to the 2013 Scandinavian Journal paper.

**Action:** Locate or add BibTeX entry. Likely key would be `aabergeColombinoStructural2018`.

---

## Phase 1 checklist (derived from Phase 0)

- [ ] Delete `GDPQuestMeasure` stub from bib
- [ ] Add full entry for Calo-Blanco & García-Pérez 2014 (replace `WelfareLossCaused` stub)
- [ ] Add Aaberge, Dagsvik & Strøm 1995 to bib
- [ ] Add Aaberge & Colombino 2018 to bib
- [ ] Identify and add chapter_10 / chapter_11 bib entries
- [ ] Fix `cappauGettingTiredWork2015` author and date fields
- [ ] Add DOIs for 16 journal articles
- [ ] Copy the 17 Tier 1/2 PDFs from Zotero `files/` into `Literature/` for extraction
- [ ] Run `improve_md_extractions.py` on newly added PDFs
- [ ] Run `build_full_literaterature.py` to regenerate `full_literaterature.md`
- [ ] Resolve the 11 ambiguous-filename PDFs by reading MD extractions
- [ ] Confirm or add bib entries for: Aaberge & Colombino 2018, Bargain & Peichl 2016, Jones & Klenow 2016, Fleurbaey 2007 JPET paper
- [ ] Create per-shelf subdirectories under `JMP_literature/` for Phase 1 organization
