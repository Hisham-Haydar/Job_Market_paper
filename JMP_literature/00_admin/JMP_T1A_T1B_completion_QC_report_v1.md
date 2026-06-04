# JMP T1A/T1B Completion QC Report (v1)

**Date:** 2026-06-04
**Updated after local repair pass:** 2026-06-04
**Scope:** Individual `.md` files in `JMP_literature/03_summaries/T1A/` and
`JMP_literature/03_summaries/T1B/`, checked against the 13 official T1A and
10 official T1B bibkeys in `JMP_literature_tiers_expanded_v1.csv`.

No new summaries were generated. No external searches were run. No BibTeX
entries were edited. This pass only corrected stale QC metadata and canonical
filenames, and archived one non-canonical combined file.

---

## 1. QC verdict

**COMPLETE WITH MINOR REPAIRS.**

All 23 official T1A/T1B slots are covered by individual summary files:
13/13 T1A and 10/10 T1B. The previous blocker for
`fleurbaeyOptimalIncomeTaxation2018` is resolved: the JEL survey summary is
present as `T1B/Fleurbaey_Maniquet_2018_JEL_optimal_income_taxation.md`.

The IJET Fleurbaey-Maniquet paper is retained as a supplementary normative
primitive under the explicit filename
`T1B/Fleurbaey_Maniquet_2018_IJET_inequality_averse.md`; it does not occupy an
official T1B slot. The non-canonical combined files `all_summaries_T1A.md` and
`all_summaries_T1B.md` have been archived and must not be indexed.

The remaining repairs are citation/metadata hygiene only. They do not block
reading or indexing.

---

## 2. Files inspected

**T1A official summaries (13 files):**

| Filename | Official bibkey |
|---|---|
| `Aaberge_et_al_2009.md` | `aabergeEvaluatingAlternativeRepresentations2009` |
| `Audoly_et_al_2025.md` | `audolyPractitionersNoteShapleyOwenShorrocks2025` |
| `Bargain_et_al_2013.md` | `bargainWelfareLaborSupply2013` |
| `Bhattacharya_2015.md` | `bhattacharyaNonparametricWelfareAnalysis2015` |
| `Capeau_Decoster_2016.md` | `cappauGettingTiredWork2015` |
| `Capeau_et_al_2015_RURO.md` | `capeauEstimatingSimulatingRandom2015` |
| `Dagsvik_Jia_2016_latent_jobs.md` | `dagsvikLaborSupplyChoice2016` |
| `Dagsvik_Karlstrom_2005.md` | `dagsvikCompensatingVariationHicksian2005` |
| `Dagsvik_et_al_2014_latent_jobs_arguments.md` | `dagsvikTHEORETICALPRACTICALARGUMENTS2014` |
| `Jacquet_Jia_Thoresen_2026.md` | `jacquetHowMuchDoes2026` |
| `Sastre_Trannoy_2002.md` | `sastreShapleyInequalityDecomposition2002` |
| `Shorrocks_1982.md` | `shorrocksInequalityDecompositionFactor1982` |
| `Shorrocks_2013.md` | `shorrocksDecompositionProceduresDistributional2013` |

**T1B official summaries (10 files):**

| Filename | Official bibkey |
|---|---|
| `Aaberge_Colombino_2013.md` | `aabergeUsingMicroeconometricModel2013` |
| `Aaberge_Colombino_2018.md` | `aabergeColombinoStructural2018` |
| `Aaberge_Dagsvik_Strom_1995.md` | `aabergeLaborSupply1995` |
| `Beffy_et_al_2019.md` | `beffyLabourSupplyTaxation2019` |
| `Bhattacharya_2018.md` | `bhattacharyaEmpiricalWelfareAnalysis2018` |
| `Capeau_et_al_2021.md` | `capeauNonparametricWelfareAnalysis2021` |
| `Decancq_et_al_2015.md` | `decancqHappinessEquivalentIncomes2015` |
| `Fleurbaey_Maniquet_2018_JEL_optimal_income_taxation.md` | `fleurbaeyOptimalIncomeTaxation2018` |
| `Sutherland_Figari_2013.md` | `sutherlandEUROMODEuropeanUnion2013` |
| `van_Soest_1995.md` | `vansoestStructuralModelsFamily1995` |

**Supplementary retained file:**

| Filename | Status |
|---|---|
| `Fleurbaey_Maniquet_2018_IJET_inequality_averse.md` | Supplementary accepted normative primitive; not an official T1B slot |

**Archived non-canonical file:**

| Filename | Status |
|---|---|
| `archive/all_summaries_T1A_COMBINED_NONCANONICAL.md` | Archived; exclude from indexing |
| `archive/all_summaries_T1B_COMBINED_NONCANONICAL.md` | Archived; exclude from indexing |

---

## 3. T1A completeness

**13/13 official T1A slots are covered.** Every official T1A paper has a
non-empty individual summary in `JMP_literature/03_summaries/T1A/`.

No T1B, T2, or T3 paper is being used as a T1A substitute. The archived combined
file is not part of the canonical T1A corpus.

---

## 4. T1B completeness

**10/10 official T1B slots are covered.** Every official T1B paper has a
non-empty individual summary in `JMP_literature/03_summaries/T1B/`.

The previous Fleurbaey-Maniquet ambiguity is fixed:

| Paper | Canonical file | Status |
|---|---|---|
| Fleurbaey & Maniquet 2018, JEL, "Optimal Income Taxation Theory and Principles of Fairness" | `Fleurbaey_Maniquet_2018_JEL_optimal_income_taxation.md` | Official T1B slot accepted |
| Fleurbaey & Maniquet 2018, IJET, "Inequality-averse well-being measurement" | `Fleurbaey_Maniquet_2018_IJET_inequality_averse.md` | Supplementary accepted file; not counted as official T1B |

---

## 5. Filing correctness

**T1A is clean.** The T1A folder contains the 13 official individual summaries
only. The non-canonical `all_summaries_T1A.md` file has been moved to
`JMP_literature/03_summaries/archive/all_summaries_T1A_COMBINED_NONCANONICAL.md`.

**T1B is clean.** The T1B folder contains the 10 official T1B summaries plus one
explicitly named supplementary IJET Fleurbaey-Maniquet summary. The
non-canonical `all_summaries_T1B.md` file has been moved to
`JMP_literature/03_summaries/archive/all_summaries_T1B_COMBINED_NONCANONICAL.md`.
No T2/T3 files are misfiled as T1A. `Sutherland_Figari_2013.md` remains in T1B
because it is an official T1B infrastructure citation, but it correctly uses the
T2 focused prompt.

No non-canonical combined file is being used for acceptance or indexing.

---

## 6. Prompt compliance

All official T1A summaries use the full T1 exhaustive structure.

Nine official T1B summaries use the full T1 exhaustive structure. The exception
is `Sutherland_Figari_2013.md`, which correctly uses the T2 focused structure
because it is EUROMOD infrastructure rather than core theory or estimation.

The supplementary IJET Fleurbaey-Maniquet summary also uses the full T1
structure. The JEL Fleurbaey-Maniquet summary uses the full T1 structure and
includes the required boundary warning that the JEL survey is a cited primitive,
not the companion Haydar-Maniquet theory paper and not the source of the
project's W^1-W^6 family.

---

## 7. Metadata warnings

Known non-blocking metadata warnings are recorded in
`JMP_T1A_T1B_remaining_repair_queue_v1.csv`.

| File or group | Warning | Blocks indexing? |
|---|---|---|
| `Aaberge_Colombino_2018.md` | Missing BibTeX entry before citation | No |
| `Aaberge_Dagsvik_Strom_1995.md` | Missing BibTeX entry before citation | No |
| `Capeau_Decoster_2016.md` | Bib author corruption and year/version ambiguity | No |
| `Capeau_et_al_2015_RURO.md` | Project bibkey year 2015 vs journal outlet year 2016 | No |
| `Beffy_et_al_2019.md` | In-press pagination vs published pagination | No |
| `Bhattacharya_2015.md` | DOI should be verified before citation | No |
| `Dagsvik_Karlstrom_2005.md` | JSTOR URL/no DOI in source | No |
| `Shorrocks_1982.md` | DOI/JSTOR metadata should be verified | No |
| `Sastre_Trannoy_2002.md` | DOI not confirmed; filename-origin note is informational | No |
| `Jacquet_Jia_Thoresen_2026.md` | SSRN/DOI status should be verified | No |
| `Sutherland_Figari_2013.md` | WP vs journal-version citation choice should be settled | No |
| All accepted summaries | Some metadata sections use ad-hoc BibTeX keys rather than canonical keys | No |

---

## 8. Overclaim risks

Required overclaim warnings are present where relevant:

| Risk area | Current status |
|---|---|
| W^1-W^6 overclaim | Summaries distinguish the JMP's W^1-W^6 family from source-specific notation. Fleurbaey-Maniquet JEL and IJET both state that they do not contain the JMP's W^1-W^6 classification. |
| Three-way vocabulary | Summaries use access / ability / preference vocabulary and flag when a source only supports a narrower or older two-way framing. |
| Occupation vs industry/sector | RURO and opportunity summaries keep occupation/ISCO separate from industry/sector/NACE. |
| Theory-paper boundary | Fleurbaey-Maniquet JEL and IJET are treated as cited primitives, not as the companion Haydar-Maniquet theory paper and not as the empirical JMP. |
| Access overclaims | Theory papers with no opportunity mechanism explicitly say they do not identify or model access. |
| Sutherland & Figari | Treated as EUROMOD infrastructure/input only, not core theory, not a welfare object, and not a decomposition source. |

---

## 9. Remaining blockers

**None for reading or indexing.**

There is no missing official T1A/T1B summary and no official slot occupied by
the wrong paper. The remaining queue contains citation and metadata repairs only.

---

## 10. Accepted summaries

**Official accepted summaries:** 23.

**T1A accepted (13):**

| File | Bibkey |
|---|---|
| `Aaberge_et_al_2009.md` | `aabergeEvaluatingAlternativeRepresentations2009` |
| `Audoly_et_al_2025.md` | `audolyPractitionersNoteShapleyOwenShorrocks2025` |
| `Bargain_et_al_2013.md` | `bargainWelfareLaborSupply2013` |
| `Bhattacharya_2015.md` | `bhattacharyaNonparametricWelfareAnalysis2015` |
| `Capeau_Decoster_2016.md` | `cappauGettingTiredWork2015` |
| `Capeau_et_al_2015_RURO.md` | `capeauEstimatingSimulatingRandom2015` |
| `Dagsvik_Jia_2016_latent_jobs.md` | `dagsvikLaborSupplyChoice2016` |
| `Dagsvik_Karlstrom_2005.md` | `dagsvikCompensatingVariationHicksian2005` |
| `Dagsvik_et_al_2014_latent_jobs_arguments.md` | `dagsvikTHEORETICALPRACTICALARGUMENTS2014` |
| `Jacquet_Jia_Thoresen_2026.md` | `jacquetHowMuchDoes2026` |
| `Sastre_Trannoy_2002.md` | `sastreShapleyInequalityDecomposition2002` |
| `Shorrocks_1982.md` | `shorrocksInequalityDecompositionFactor1982` |
| `Shorrocks_2013.md` | `shorrocksDecompositionProceduresDistributional2013` |

**T1B accepted (10 official):**

| File | Bibkey |
|---|---|
| `Aaberge_Colombino_2013.md` | `aabergeUsingMicroeconometricModel2013` |
| `Aaberge_Colombino_2018.md` | `aabergeColombinoStructural2018` |
| `Aaberge_Dagsvik_Strom_1995.md` | `aabergeLaborSupply1995` |
| `Beffy_et_al_2019.md` | `beffyLabourSupplyTaxation2019` |
| `Bhattacharya_2018.md` | `bhattacharyaEmpiricalWelfareAnalysis2018` |
| `Capeau_et_al_2021.md` | `capeauNonparametricWelfareAnalysis2021` |
| `Decancq_et_al_2015.md` | `decancqHappinessEquivalentIncomes2015` |
| `Fleurbaey_Maniquet_2018_JEL_optimal_income_taxation.md` | `fleurbaeyOptimalIncomeTaxation2018` |
| `Sutherland_Figari_2013.md` | `sutherlandEUROMODEuropeanUnion2013` |
| `van_Soest_1995.md` | `vansoestStructuralModelsFamily1995` |

**Supplementary accepted (1):**

| File | Status |
|---|---|
| `Fleurbaey_Maniquet_2018_IJET_inequality_averse.md` | Supplementary normative primitive; optional for indexing depending on corpus policy |

---

## 11. Summaries needing repair

No accepted summary needs content repair before indexing.

Remaining repairs are metadata/citation hygiene only:

| Priority | Area | Action |
|---|---|---|
| Low | Missing BibTeX entries | Add entries for Aaberge-Colombino 2018 and Aaberge-Dagsvik-Strom 1995 before citing. |
| Low | BibTeX corruption/version metadata | Correct Capeau-Decoster author/year metadata before citing. |
| Low | DOI/version/pagination checks | Resolve DOI, pagination, and WP-vs-journal warnings before citation finalization. |
| Low | Summary metadata keys | Reconcile ad-hoc metadata keys with canonical `.bib` keys when applying the BibTeX repair queue. |

---

## 12. Whether indexing may proceed

**Yes.**

Indexing may proceed over the 23 official accepted T1A/T1B summaries. Exclude
the archived combined files:
`JMP_literature/03_summaries/archive/all_summaries_T1A_COMBINED_NONCANONICAL.md`
and
`JMP_literature/03_summaries/archive/all_summaries_T1B_COMBINED_NONCANONICAL.md`.

The supplementary IJET Fleurbaey-Maniquet summary is usable, but it should be
included only if the index design intentionally includes accepted supplementary
normative primitives outside the official 23 slots.

---

## 13. Immediate next action

Build the T1A/T1B index over the 23 official accepted summaries, excluding the
archive directory. Then apply the low-priority citation metadata queue before
using these summaries for final manuscript citations.
