# JMP Batch-1 Pre-Extraction Readiness Check (v1)

**Date:** 2026-06-02
**Purpose:** Verify, against the actual filesystem, that every Batch-1 paper is
ready to extract with `JMP_T1_exhaustive_extraction_prompt_v2.md`. No papers
summarized, no external searches, no bib edits, no PDFs moved, no MD extractions
generated.

---

## 1. Readiness verdict

**Batch 1 is READY WITH WARNINGS.**

All 12 Batch-1 papers have (1) a PDF in `Literature/`, (2) a matching, non-empty
MD extraction in `Literature/md_extractions/`, and (3) a usable bibkey in
`JMP_literature_tiers_expanded_v1.csv` assigned the T1 prompt. **Zero blocking
issues.** The warnings are metadata-only (missing DOIs, an author-name
correction, a date ambiguity, non-ASCII filenames) and do **not** block
extraction, because the extractor reads the PDF + MD, not the bib.

---

## 2. Files inspected

Read:
- `JMP_literature/00_admin/JMP_first_extraction_batch_v1.md`
- `JMP_literature/00_admin/JMP_literature_tiers_expanded_v1.csv`
- `JMP_literature/06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md` (15,033 B — present)
- `JMP_literature/06_prompts/JMP_T2_focused_extraction_prompt_v2.md` (6,247 B — present)
- `JMP_literature/00_admin/JMP_missing_pdf_acquisition_queue_v1.csv`
- `JMP_literature/00_admin/JMP_bibtex_repair_queue_v1.md`

Inspected (filesystem ground truth):
- `Literature/` — **72 PDFs**
- `Literature/md_extractions/` — **72 `.md` extractions** (+ 1 stray `.html` temp, see §8)

Matching method: substring match of distinctive title/author/year tokens against
the real filenames (shell globbing is unreliable here due to spaces, commas,
brackets, and non-ASCII characters in filenames). MD non-emptiness verified by
byte size.

---

## 3. Batch-1 papers checked

| # | bibkey | author_year | tier |
|---|---|---|---|
| 1 | dagsvikLaborSupplyChoice2016 | Dagsvik & Jia 2016 | T1A |
| 2 | dagsvikTHEORETICALPRACTICALARGUMENTS2014 | Dagsvik et al. 2014 | T1A |
| 3 | aabergeEvaluatingAlternativeRepresentations2009 | Aaberge et al. 2009 | T1A |
| 4 | capeauEstimatingSimulatingRandom2015 | Capéau et al. 2015 | T1A |
| 5 | cappauGettingTiredWork2015 | Capéau & Decoster 2015/2016 | T1A |
| 6 | dagsvikCompensatingVariationHicksian2005 | Dagsvik & Karlström 2005 | T1A |
| 7 | bargainWelfareLaborSupply2013 | Bargain et al. 2013 | T1A |
| 8 | bhattacharyaNonparametricWelfareAnalysis2015 | Bhattacharya 2015 | T1A |
| 9 | shorrocksDecompositionProceduresDistributional2013 | Shorrocks 2013 | T1A |
| 10 | audolyPractitionersNoteShapleyOwenShorrocks2025 | Audoly et al. 2025 | T1A |
| 11 | jacquetHowMuchDoes2026 | Jacquet et al. 2026 (JJT) | T1A |
| 12 | vansoestStructuralModelsFamily1995 | Van Soest 1995 | T1B |

All 12 are present in `JMP_literature_tiers_expanded_v1.csv` and carry
`extraction_prompt = T1`. **12/12 mapped.**

---

## 4. PDF availability

**12 / 12 present in `Literature/`.**

| # | bibkey | PDF filename (actual) |
|---|---|---|
| 1 | dagsvikLaborSupplyChoice2016 | `Dagsvik and Jia - 2016 - Labor Supply as a Choice Among Latent Jobs Unobserved Heterogeneity and Identification LABOR SUPPL.pdf` |
| 2 | dagsvikTHEORETICALPRACTICALARGUMENTS2014 | `Dagsvik et al. - 2014 - THEORETICAL AND PRACTICAL ARGUMENTS FOR MODELING LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS.pdf` |
| 3 | aabergeEvaluatingAlternativeRepresentations2009 | `Aaberge et al_2009_Evaluating Alternative Representations of the Choice Sets in Models of Labor.pdf` |
| 4 | capeauEstimatingSimulatingRandom2015 | `Capéau et al. - 2015 - Estimating and Simulating with a Random Utility Random Opportunity Model of Job ChoicePresentation a.pdf` |
| 5 | cappauGettingTiredWork2015 | `Capéau_Decoster_2016_Getting tired of work, or re-tiring in absence of decent job opportunities.pdf` |
| 6 | dagsvikCompensatingVariationHicksian2005 | `Dagsvik_Karlström_2005_Compensating Variation and Hicksian Choice Probabilities in Random Utility.pdf` |
| 7 | bargainWelfareLaborSupply2013 | `Bargain et al_2013_Welfare, labor supply and heterogeneous preferences.pdf` |
| 8 | bhattacharyaNonparametricWelfareAnalysis2015 | `Bhattacharya_2015_Nonparametric Welfare Analysis for Discrete Choice.pdf` |
| 9 | shorrocksDecompositionProceduresDistributional2013 | `Shorrocks_2013_Decomposition procedures for distributional analysis.pdf` |
| 10 | audolyPractitionersNoteShapleyOwenShorrocks2025 | `Audoly et al_2025_A Practitioner's Note on the Shapley-Owen-Shorrocks Decomposition.pdf` |
| 11 | jacquetHowMuchDoes2026 | `Jacquet et al_2026_How Much Does Responsibility Matter in Fairness Measurement.pdf` |
| 12 | vansoestStructuralModelsFamily1995 | `Van Soest - 1995 - Structural Models of Family Labor Supply A Discrete Choice Approach.pdf` |

Note on #5: the PDF filename is dated **2016** while the bibkey/CSV is **2015**
(SSRN working-paper year vs version year). Same paper — see §6 / §8.

---

## 5. MD extraction availability

**12 / 12 present in `Literature/md_extractions/`, all non-empty.** Each MD
filename is the exact stem of its PDF (legacy pipeline convention), so the match
is unambiguous.

| # | bibkey | MD size (bytes) |
|---|---|---|
| 1 | dagsvikLaborSupplyChoice2016 | 66,309 |
| 2 | dagsvikTHEORETICALPRACTICALARGUMENTS2014 | 66,526 |
| 3 | aabergeEvaluatingAlternativeRepresentations2009 | 65,591 |
| 4 | capeauEstimatingSimulatingRandom2015 | 108,234 |
| 5 | cappauGettingTiredWork2015 | 160,170 |
| 6 | dagsvikCompensatingVariationHicksian2005 | 45,291 |
| 7 | bargainWelfareLaborSupply2013 | 91,633 |
| 8 | bhattacharyaNonparametricWelfareAnalysis2015 | 84,282 |
| 9 | shorrocksDecompositionProceduresDistributional2013 | 68,801 |
| 10 | audolyPractitionersNoteShapleyOwenShorrocks2025 | 28,415 |
| 11 | jacquetHowMuchDoes2026 | 96,327 |
| 12 | vansoestStructuralModelsFamily1995 | 63,582 |

Smallest (Audoly, 28 KB) is still a full extraction; none are stubs. **No MD
extraction is missing**, so §9 is empty by design.

---

## 6. BibTeX / metadata availability

All 12 bibkeys resolve in `JMP_literature_tiers_expanded_v1.csv`. Extraction is
not gated on the bib (the extractor reads PDF + MD; the bibkey is only the label),
so none of the items below blocks Batch 1.

| # | bibkey | bibtex_status | metadata_needs_verification |
|---|---|---|---|
| 1 | dagsvikLaborSupplyChoice2016 | clean | no |
| 2 | dagsvikTHEORETICALPRACTICALARGUMENTS2014 | clean | no |
| 3 | aabergeEvaluatingAlternativeRepresentations2009 | clean | no (note: bib has duplicate `file=` paths — §8) |
| 4 | capeauEstimatingSimulatingRandom2015 | title-typo | verify "ChoicePresentation" title typo is intentional |
| 5 | cappauGettingTiredWork2015 | author-corrupted | verify 2015 vs 2016 date; author "Cappau/Andrr" → "Capéau/André" |
| 6 | dagsvikCompensatingVariationHicksian2005 | clean-no-DOI | verify DOI (JSTOR URL only) |
| 7 | bargainWelfareLaborSupply2013 | clean | no |
| 8 | bhattacharyaNonparametricWelfareAnalysis2015 | clean-no-DOI | verify DOI (Econometrica) |
| 9 | shorrocksDecompositionProceduresDistributional2013 | clean | no |
| 10 | audolyPractitionersNoteShapleyOwenShorrocks2025 | clean | no |
| 11 | jacquetHowMuchDoes2026 | clean-no-DOI | verify DOI / SSRN status |
| 12 | vansoestStructuralModelsFamily1995 | clean | no |

All metadata items above are already tracked in `JMP_bibtex_repair_queue_v1.md`
(B1/B2 for #5, G.1 for the missing DOIs, F for the duplicate `file=` paths).

---

## 7. Blocking issues

**None.** All 12 papers have PDF + non-empty MD + a usable bibkey + the T1
prompt. There is nothing that prevents extraction of any Batch-1 paper.

---

## 8. Non-blocking warnings

1. **Non-ASCII filenames (`é`, `ö`, `ø`).** #4, #5 (`Capéau`), #6 (`Karlström`)
   contain real UTF-8 accented characters. The legacy pipeline already produced
   their MD extractions from these exact files, so the encoding is proven to work
   for extraction; only flag if a downstream tool that cannot handle UTF-8 paths
   is introduced.
2. **#5 date mismatch (2015 vs 2016).** Bibkey/CSV say 2015; PDF + MD filenames
   say 2016. Same paper. Resolve in the bib (repair queue B2) before *citing*;
   does not affect extraction.
3. **#5 author corruption in bib** ("Cappau, Bart" / "Decoster, Andrr"). Fix to
   "Capéau, Bart and Decoster, André" (repair queue B1). The PDF/MD use the
   correct spelling.
4. **#4 title-typo in bib** ("…Job ChoicePresentation a…") — a Zotero file-title
   artefact, consistent across PDF/MD filename. Cosmetic; verify before citing.
5. **Missing DOIs** for #6, #8, #11 (repair queue G.1). Citation-metadata gap
   only.
6. **#3 duplicate `file=` paths** in the bib (files/1086 and files/1174) —
   Zotero double-import artefact (repair queue F). The portable PDF in
   `Literature/` is present and singular; no extraction impact.
7. **Stray temp file** `Literature/md_extractions/__bbox_tmp_Bargain et al_2010_…Making work pay….html`
   — a leftover from a previous extraction run for a **non-Batch-1** paper
   (Bargain et al. 2010). Harmless; can be deleted during housekeeping. Not an MD
   extraction and not in Batch 1.

---

## 9. Commands needed if any MD extraction is missing

**No MD extraction is missing — no command required for Batch 1.**

For reference, if a future paper's MD extraction were absent, the regeneration
command (per `CLAUDE.md` / the legacy pipeline, run from the repo root) is:

```
python Literature/improve_md_extractions.py
```

This rebuilds Markdown from the source PDFs in `Literature/` into
`Literature/md_extractions/` (requires MiKTeX `pdftotext` at the hardcoded path
in the script). To then refresh the concatenated index:

```
python Literature/build_full_literaterature.py
```

Neither needs to be run for Batch 1.

---

## 10. Whether first 3 extractions may proceed

**Yes.** The first three papers each have a present PDF, a present non-empty MD
extraction, a clean bibkey, and the T1 prompt assigned, with **no** metadata
warning at all on any of them:

- dagsvikLaborSupplyChoice2016 — clean
- dagsvikTHEORETICALPRACTICALARGUMENTS2014 — clean
- aabergeEvaluatingAlternativeRepresentations2009 — clean

They may be extracted immediately using
`06_prompts/JMP_T1_exhaustive_extraction_prompt_v2.md`.

---

## 11. Recommended first 3 papers

Same as Batch-1 order #1–#3 (the model + identification + choice-set foundation
the welfare layer is built on, and the three cleanest-metadata papers):

1. **dagsvikLaborSupplyChoice2016** — Dagsvik & Jia 2016 (RURO identification; couples joint choice).
2. **dagsvikTHEORETICALPRACTICALARGUMENTS2014** — Dagsvik et al. 2014 (latent-jobs manifesto; modelling-choice justification).
3. **aabergeEvaluatingAlternativeRepresentations2009** — Aaberge et al. 2009 (choice-set construction; the 901/101-alternative resolution).

Extract each with the **T1 v2** prompt; apply the three-way
access/ability/preference vocabulary and the proposal/prior-correction extraction
points throughout.

---

## 12. Immediate next action

1. Begin extraction of the recommended first 3 (§11) with the T1 v2 prompt.
2. In parallel (does not block extraction): apply repair-queue items B1/B2 to fix
   `cappauGettingTiredWork2015` author/date before that paper (#5) is **cited**.
3. Optional housekeeping: delete the stray
   `__bbox_tmp_…Making work pay….html` temp file from `md_extractions/`.
4. After the first 3, continue through Batch-1 #4–#12, then begin Batch 2
   acquisition (Shorrocks 1982, Sastre & Trannoy 2002 — acquisition queue
   ranks 1–2).

---

## Final statement

**Batch 1 extraction is READY WITH WARNINGS** — 12/12 papers have PDF + non-empty
MD extraction + usable bibkey + T1 prompt; there are **no blocking issues**, and
the only warnings are non-blocking citation-metadata items already tracked in the
BibTeX repair queue. The first 3 extractions may proceed now.
