# JMP Summary Corpus Classification Audit (v1)

**Date:** 2026-06-04
**Scope:** All files currently in `JMP_literature/03_summaries/T1A/` (the only
populated subfolder). Classified against `JMP_literature_tiers_expanded_v1.csv`
(the authoritative final-tier source).

**Inputs read:**
- `JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv`
- `JMP_literature/00_admin/JMP_first_extraction_batch_v1.md`
- `JMP_literature/00_admin/JMP_batch1_pre_extraction_readiness_v1.md`
- `JMP_literature/06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md`
- `JMP_literature/06_prompts/JMP_T2_focused_extraction_prompt_v2.md`

**Directories inspected:**
- `JMP_literature/03_summaries/T1A/` — 15 `.md` files + 1 combined file
- `JMP_literature/03_summaries/T1B/` — does not exist yet
- `JMP_literature/03_summaries/T2/` — does not exist yet
- `JMP_literature/03_summaries/T3_background/` — does not exist yet

**No files moved, edited, or generated during this audit.**

---

## 1. Which existing summaries are true T1A?

Four individual files in `T1A/` correctly match an official T1A paper:

| Filename | Matched bibkey | Official tier | Notes |
|---|---|---|---|
| `Dagsvik_Jia_2016_latent_jobs.md` | dagsvikLaborSupplyChoice2016 | **T1A** | Correct folder. |
| `Dagsvik_et_al_2014_latent_jobs_arguments.md` | dagsvikTHEORETICALPRACTICALARGUMENTS2014 | **T1A** | Correct folder. |
| `Aaberge_et_al_2009.md` | aabergeEvaluatingAlternativeRepresentations2009 | **T1A** | Correct folder. |
| `Batcharaya_2015.md` | bhattacharyaNonparametricWelfareAnalysis2015 | **T1A** | Correct folder. Filename has a typo ("Batcharaya" for "Bhattacharya") — non-blocking, see §7. |
| `Dagsvik_Karlstrom_2005.md` | dagsvikCompensatingVariationHicksian2005 | **T1A** | Correct folder. |
| `Shorrocks_1982.md` | shorrocksInequalityDecompositionFactor1982 | **T1A** | Correct folder. |
| `Shorrocks_2013.md` | shorrocksDecompositionProceduresDistributional2013 | **T1A** | Correct folder. |
| `Jaque_jia_Thor.md` | jacquetHowMuchDoes2026 | **T1A** | Correct folder. Filename truncation ("Jaque_jia_Thor" for "Jacquet_Jia_Thoresen_2026") — see §7. |

**True T1A count: 8 of 15 individual files.**

Note: `bargainWelfareLaborSupply2013`, `capeauEstimatingSimulatingRandom2015`,
`cappauGettingTiredWork2015`, `audolyPractitionersNoteShapleyOwenShorrocks2025`,
and `sastreShapleyInequalityDecomposition2002` are official T1A papers with
**no individual summary file yet** (see §4).

---

## 2. Which existing summaries are T1B but currently stored in T1A?

Three files are in `T1A/` but the matched paper is officially **T1B**:

| Filename | Matched bibkey | Official tier | Evidence |
|---|---|---|---|
| `van_Soest_1995.md` | vansoestStructuralModelsFamily1995 | **T1B** | The file itself states "My assessment: T1B" and gives the correct destination as `T1B/van_Soest_1995.md`. Contains a file/source mismatch note (requested as Aaberge_Colombino_2013; PDF was van Soest 1995 — correctly summarised as van Soest). |
| `Beffy_et_al_2019_summary.md` | beffyLabourSupplyTaxation2019 | **T1B** | Official tier T1B per tiers CSV; currently mis-filed in T1A. |
| `Aaberge_Colombino_2013.md` | aabergeUsingMicroeconometricModel2013 | **T1B** | Official tier T1B per tiers CSV; currently mis-filed in T1A. Content confirmed as Aaberge & Colombino 2013. Contains critical notation warning (paper's $W_k$ is not the JMP $W^1$-$W^6$ family). |

**T1B-in-T1A count: 3 files to relocate.**

---

## 3. Which existing summaries are T2 or T3 but currently stored in T1A?

Four files are in `T1A/` but the matched paper is officially **T2** or **T3**:

| Filename | Matched bibkey | Official tier | Notes |
|---|---|---|---|
| `Aberge_colombino_2012.md` | aabergeAccountingFamilyBackground2012 | **T2** | Official tier T2. Filename typo: "Aberge" for "Aaberge" (single-A). |
| `Bourguignon_et_al_2007.md` | bourguignonINEQUALITYOPPORTUNITYBRAZIL2007 | **T2** | Official tier T2; also extracted under the T1 exhaustive prompt (over-depth for its tier). |
| `Ferreria_Gignoux2011.md` | ferreiraMEASUREMENTINEQUALITYOPPORTUNITY2011 | **T2** | Official tier T2; filename typo "Ferreria" for "Ferreira". Also over-depth (T1 prompt used). |
| `Aaberge_Colombino_2006.md` | aabergeDesigningOptimalTaxes2006 | **T3** | Official tier T3. Extraction note states the T2 prompt was used (not T1 exhaustive). Content is accurate but tier/folder is wrong. |

**Mis-tiered-in-T1A count: 4 files (3 T2, 1 T3) to relocate.**

---

## 4. Which official T1A papers are still missing summaries?

Five official T1A papers have **no individual summary file** in `03_summaries/`:

| bibkey | author_year | PDF in Literature/ | MD extraction | Blocker |
|---|---|---|---|---|
| bargainWelfareLaborSupply2013 | Bargain et al. 2013 | yes | yes | none — ready to extract |
| capeauEstimatingSimulatingRandom2015 | Capeau et al. 2015 | yes | yes | none — ready to extract |
| cappauGettingTiredWork2015 | Capeau & Decoster 2015/2016 | yes | yes | none — ready to extract (fix bib author before citing) |
| audolyPractitionersNoteShapleyOwenShorrocks2025 | Audoly et al. 2025 | yes | yes | none — ready to extract |
| sastreShapleyInequalityDecomposition2002 | Sastre & Trannoy 2002 | **no** | no | **blocked — acquire PDF first** (acquisition queue rank 1) |

**Missing T1A summaries: 5.** Four are immediately extractable (Batch 1 or Batch 2 unblocked). One (Sastre & Trannoy 2002) requires PDF acquisition first.

Note: `Shorrocks_1982.md` exists as an individual file (§1 above), so
`shorrocksInequalityDecompositionFactor1982` is **not** missing — despite the PDF
being absent from `Literature/` at the time of Phase 1 (the summary may have been
produced from the Zotero-path PDF or from the `all_summaries_T1.md` combined file).

---

## 5. Which official T1B papers are still missing summaries?

Seven of ten official T1B papers have **no individual summary file** in
`03_summaries/`:

| bibkey | author_year | PDF in Literature/ | MD extraction | Blocker |
|---|---|---|---|---|
| aabergeColombinoStructural2018 | Aaberge & Colombino 2018 | yes | yes | none (no bib entry — fix before citing, not before extracting) |
| aabergeLaborSupply1995 | Aaberge Dagsvik & Strom 1995 | yes | yes | none (no bib entry — same caveat) |
| bhattacharyaEmpiricalWelfareAnalysis2018 | Bhattacharya 2018 | yes | yes | none — ready |
| capeauNonparametricWelfareAnalysis2021 | Capeau et al. 2021 | yes | yes | none — ready |
| decancqHappinessEquivalentIncomes2015 | Decancq et al. 2015 | yes | yes | none — ready |
| fleurbaeyOptimalIncomeTaxation2018 | Fleurbaey & Maniquet 2018 | yes | yes | none — ready |
| sutherlandEUROMODEuropeanUnion2013 | Sutherland & Figari 2013 | yes | yes | none — use T2 prompt |

**Already summarised (T1B, wrongly in T1A/): 3** — van Soest 1995,
Beffy et al. 2019, Aaberge & Colombino 2013. These exist and just need relocation.

**Truly missing T1B summaries: 7.** All 7 unblocked; 2 need a bib entry added
before citing (but extraction is not blocked).

---

## 6. Which summaries appear only inside `all_summaries_T1.md` but not as individual canonical files?

`all_summaries_T1.md` (519 KB) contains 14 summaries. Cross-referencing with
the 15 individual files:

**All 14 papers in `all_summaries_T1.md` also have individual files.** There are
no papers that exist *only* in the combined file. The combined file is therefore
entirely redundant with the individual files and adds no unique content.

| Paper in all_summaries_T1.md | Individual file exists? |
|---|---|
| Aaberge & Colombino 2013 | yes (`Aaberge_Colombino_2013.md`) |
| Aaberge, Colombino & Wennemo 2009 | yes (`Aaberge_et_al_2009.md`) |
| Aaberge & Colombino 2012 | yes (`Aberge_colombino_2012.md`) |
| Bhattacharya 2015 | yes (`Batcharaya_2015.md`) |
| Beffy et al. 2019 | yes (`Beffy_et_al_2019_summary.md`) |
| Bourguignon et al. 2007 | yes (`Bourguignon_et_al_2007.md`) |
| Dagsvik et al. 2014 | yes (`Dagsvik_et_al_2014_latent_jobs_arguments.md`) |
| Dagsvik & Jia 2016 | yes (`Dagsvik_Jia_2016_latent_jobs.md`) |
| Dagsvik & Karlström 2005 | yes (`Dagsvik_Karlstrom_2005.md`) |
| Ferreira & Gignoux 2011 | yes (`Ferreria_Gignoux2011.md`) |
| Jacquet et al. 2026 | yes (`Jaque_jia_Thor.md`) |
| Shorrocks 1982 | yes (`Shorrocks_1982.md`) |
| Shorrocks 2013 | yes (`Shorrocks_2013.md`) |
| van Soest 1995 | yes (`van_Soest_1995.md`) |

**Conclusion: `all_summaries_T1.md` is 100% redundant** with the individual files.
No summary exists only inside it. See §8 for the non-canonical ruling.

---

## 7. Which summaries have filename typos or metadata issues?

| Filename | Issue | Correct filename | Severity |
|---|---|---|---|
| `Batcharaya_2015.md` | Typo: "Batcharaya" for "Bhattacharya" | `Bhattacharya_2015.md` | Non-blocking (content correct; rename during relocation) |
| `Aberge_colombino_2012.md` | Typo: "Aberge" for "Aaberge" (single-A); lowercase second word | `Aaberge_Colombino_2012.md` | Non-blocking (content correct; rename during relocation) |
| `Ferreria_Gignoux2011.md` | Typo: "Ferreria" for "Ferreira" | `Ferreira_Gignoux_2011.md` | Non-blocking (content correct; rename during relocation) |
| `Jaque_jia_Thor.md` | Truncation: "Jaque_jia_Thor" for "Jacquet_Jia_Thoresen_2026" | `Jacquet_Jia_Thoresen_2026.md` | Non-blocking (rename during relocation or in-place) |
| `Beffy_et_al_2019_summary.md` | Suffix "_summary" non-standard | `Beffy_et_al_2019.md` | Cosmetic; rename during relocation |
| `van_Soest_1995.md` | Was originally requested as `Aaberge_Colombino_2013.md` (file/source mismatch at creation time; self-reported in file); current filename is **correct** for the actual content | keep `van_Soest_1995.md` | Resolved — content matches filename; move to T1B/ |
| All individual files | Bib keys embedded in metadata sections use ad-hoc keys (e.g., `DagsvikKarlstrom2005`, `AabergeColombinoWennemo2009`, `shorrocks1982decomposition`, `vanSoest1995`) that do not match the canonical bibkeys in `JMP_lit_collection.bib`. | N/A | Non-blocking for reading; **must align before citing** |
| `Aaberge_Colombino_2006.md` | Produced with T2 prompt (self-reported in file); filed in T1A/ | Relocate to T3_background/ and flag for optional T1-depth rerun | The extraction depth is insufficient for a T1A paper — moot since tier is T3 |
| `Bourguignon_et_al_2007.md` | Produced with T1 exhaustive prompt; paper is T2. Over-depth, but content is usable | Relocate to T2/ — no rerun needed | Non-blocking |
| `Ferreria_Gignoux2011.md` | Produced with T1 exhaustive prompt; paper is T2. Over-depth, but content is usable | Relocate to T2/ — no rerun needed | Non-blocking |

---

## 8. Whether `all_summaries_T1.md` should be treated as non-canonical

**Yes. `all_summaries_T1.md` is non-canonical and should not be cited, linked, or
used as the source of truth for any individual paper.**

Reasons:
1. It is a convenience concatenation: every paper it contains has an individual
   canonical file (§6). It adds no unique content.
2. It contains encoding artefacts from the concatenation (`â€"` for `—`,
   BOM character at the top) that indicate it was produced by a byte-level join
   without UTF-8 normalisation.
3. It mixes papers of different official tiers (T1A, T1B, T2, T3) under a single
   `T1A/` path, compounding the mis-tiering problem.
4. The individual files are the source of truth: they are self-contained, named,
   and traceable to their PDF/MD source.

**Recommended action:** archive `all_summaries_T1.md` to a non-canonical location
(e.g., `JMP_literature/03_summaries/archive/all_summaries_T1_COMBINED_NONCANO.md`)
or delete it once the individual files are confirmed complete. Do **not** delete
before the individual files are verified.

---

## Summary statistics

| Category | Count |
|---|---|
| Individual summary files currently in T1A/ | 15 |
| of which: correctly T1A | 8 |
| of which: should be T1B (misplaced) | 3 |
| of which: should be T2 (misplaced) | 3 |
| of which: should be T3_background (misplaced) | 1 |
| Combined non-canonical file | 1 (`all_summaries_T1.md`) |
| Official T1A papers missing individual summaries | 5 (4 unblocked, 1 needs PDF acquisition) |
| Official T1B papers missing individual summaries | 7 (all unblocked) |
| Filename typos to correct during relocation | 5 |
| Bib-key mismatches in embedded metadata | all 15 (use [verify] until bib repair applied) |
