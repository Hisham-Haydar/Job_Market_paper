# JMP BibTeX Audit — v1
**File audited:** `JMP_lit_collection/JMP_lit_collection.bib`
**Date:** 2026-06-02
**Total entries found:** 87 (including stubs)
**Audit scope:** duplicates, missing fields, irrelevance flags, essential-but-no-PDF flags

---

## 1. Duplicate or Near-Duplicate Entries

### 1.1 Full duplicate — DELETE one entry

| Issue | Entry keys | Details |
|---|---|---|
| EXACT DUPLICATE | `fleurbaeyGDPQuestMeasure2009` and `GDPQuestMeasure` | `GDPQuestMeasure` is a bare `@online` stub (no author, no year, no title fields) pointing to the same Fleurbaey 2009 JEL paper. The stub adds nothing and will confuse citation software. **Action: delete `GDPQuestMeasure` from bib.** |

### 1.2 Near-duplicate PDF paths — same paper, multiple file references

These entries have duplicate `file = {}` fields referencing more than one PDF path for the same paper. This indicates the paper was imported twice into Zotero and the bib was exported without deduplication. The BibTeX entries themselves are not duplicated, but the internal Zotero attachment is. No immediate action needed in the bib file, but note that `files/` paths may be stale if Zotero is not the source of truth.

| Entry key | Duplicate file paths |
|---|---|
| `aabergeEvaluatingAlternativeRepresentations2009` | `files/1086/` and `files/1174/` |
| `bloemenJobSearchHours2008` | `files/1177/` and `files/719/` |
| `blomquistNonparametricEstimationNonlinear2002` | `files/1101/` and `files/1296/` |
| `brunoriInequalityOpportunityIncome2013` | `files/1349/` and `files/1351/` |
| `dagsvikSectoralLabourSupply2006` | `files/1052/` and `files/367/` |
| `hufeMeasuringUnfairInequality2022` | `files/1126/` and `files/1383/` |

### 1.3 Author name inconsistency — same paper, different spelling

| Entry key | Problem |
|---|---|
| `cappauGettingTiredWork2015` | Author listed as "Cappau, Bart" and "Decoster, Andrr" — both are corrupted OCR/encoding artifacts. Should be "Capéau, Bart" and "Decoster, André". The corresponding MD extraction and PDF filename correctly use "Capéau". **Action: correct author field in bib.** The date is 2015 in bib but the filename convention elsewhere uses 2016 (the SSRN working paper year differs from the conference version). |

---

## 2. Missing Years

No entries with entirely missing `date` fields were found. All entries include a `date` value.

---

## 3. Missing Titles

| Entry key | Problem |
|---|---|
| `GDPQuestMeasure` | No `title` field in the stub entry (beyond the URL page title). |
| `WelfareLossCaused` | No proper `title` field — only a ProQuest URL link title in the entry. |
| `Chapter34Welfare2002` | Title present but `author` field is missing entirely — this is a handbook chapter. Author should be Moffitt, Robert A. (Handbook of Public Economics Vol. 4, Ch. 34). **[verify]** |

---

## 4. Missing DOIs / URLs

The following entries lack a `doi` field and have only a URL (JSTOR, IDEAS, or similar) or no identifier at all. For journal articles this is a metadata gap; for working papers a URL is often the only persistent identifier.

### 4.1 Journal articles missing DOI (JSTOR/other URL only)

| Entry key | Journal | Available URL |
|---|---|---|
| `bloemenJobSearchHours2008` | Journal of Labor Economics | IDEAS URL only |
| `bloemenModelLabourSupply2000` | Labour Economics | IDEAS URL only |
| `blomquistNonparametricEstimationNonlinear2002` | Econometrica | JSTOR URL only |
| `brunoriUpwardDownwardBias2019` | Social Choice and Welfare | JSTOR URL only |
| `chettySufficientStatisticsWelfare2009` | Annual Review of Economics | JSTOR URL only |
| `choneNegativeMarginalTax2010` | American Economic Review | JSTOR URL only |
| `dagsvikCompensatingVariationHicksian2005` | Review of Economic Studies | JSTOR URL only |
| `fleurbaeyExAnteEx2013` | Economica | JSTOR URL only |
| `fleurbaeyFairIncomeTax2006` | Review of Economic Studies | JSTOR URL only |
| `immervollWelfareReformEuropean2007` | Economic Journal | JSTOR URL only |
| `masValuingAlternativeWork2017` | American Economic Review | JSTOR URL only |
| `palominoChannelsInequalityOpportunity2019` | Social Indicators Research | JSTOR URL only |
| `roemerEqualityOpportunityProgress2002` | Social Choice and Welfare | JSTOR URL only |
| `saezGeneralizedSocialMarginal2016` | American Economic Review | JSTOR URL only |
| `saezOptimalIncomeTransfer2002` | Quarterly Journal of Economics | JSTOR URL only |
| `vandegaerMeasurementInequalityOpportunity2020` | Social Choice and Welfare | JSTOR URL only |

### 4.2 Preprints and working papers — URL present (no DOI expected)

| Entry key | Source |
|---|---|
| `audolyPractitionersNoteShapleyOwenShorrocks2025` | SSRN — has DOI |
| `bargainPuttingStructureRD2013` | IZA via JSTOR |
| `brunoriOpportunitySensitivePovertyMeasurement2013` | IZA via JSTOR |
| `jacquetHowMuchDoes2026` | SSRN — URL only, no DOI field |
| `lofflerStructuralLaborSupply2014` | SOEPpapers via Econstor |

### 4.3 Stub entries — no usable identifier

| Entry key | Problem |
|---|---|
| `GDPQuestMeasure` | JSTOR URL only; no DOI, no author, no year |
| `WelfareLossCaused` | ProQuest URL only; no DOI, no author, no year, no title |

---

## 5. Entries That Look Irrelevant for the JMP

The following entries are in the bib but appear weakly connected to the JMP's core question (latent-jobs welfare decomposition in France). They may be background references accumulated during the literature search phase.

| Entry key | Concern |
|---|---|
| `anandMeasuringWelfareLatent2011` | Capabilities approach with GLLAMM for Argentina; not connected to labor supply, RURO, or decomposition methodology. |
| `duroFactorDecompositionCrosscountry1998` | Factor decomposition of Theil index for 120 countries; cross-country income decomposition, no welfare or opportunity angle. |
| `osbergIndexEconomicWell2002` | OECD well-being index 1980–1999; very broad; background at best. |
| `GDPQuestMeasure` | Duplicate stub — should be deleted (see Section 1.1). |
| `WelfareLossCaused` | Bare ProQuest stub; needs full entry if the paper (Calo-Blanco & García-Pérez 2014) is to be retained. |
| `rothShapleyValueEssays1988` | Shapley value essays book (1988); useful as background but unlikely to be cited directly; no PDF in `Literature/`. |

---

## 6. Entries That Look Essential but Lack PDFs in `Literature/`

The following entries appear essential for the JMP based on deep-research report classifications, but have no corresponding PDF in the `Literature/` folder (only in Zotero's internal `files/` paths, which may not be portable).

| Entry key | Author–Year | Priority | Why essential |
|---|---|---|---|
| `bosmansFailureCompensateFailure2025` | Bosmans et al. 2025 | Tier 1 | Compensation vs reward decomposition of IOp — directly addresses JMP decomposition |
| `bosmansMeasurementInequalityOpportunity2021` | Bosmans & Öztürk 2021 | Tier 2 | Normative IOp measurement axiomatics |
| `checchiInequalityOpportunityItaly2010` | Checchi & Peragine 2010 | Tier 1 | Closest empirical EOp template for JMP application |
| `hufeMeasuringUnfairInequality2022` | Hufe et al. 2022 | Tier 1 | Unfair vs fair inequality decomposition; Review of Economic Studies |
| `mahlerEqualityOpportunityFour2019` | Mahler & Ramos 2019 | Tier 1 | EOp in welfare dimensions beyond income |
| `peichlAccountingSpouseWhen2016` | Peichl & Ungerer 2016 | Tier 1 | Household-level EOp — relevant for couples model |
| `sastreShapleyInequalityDecomposition2002` | Sastre & Trannoy 2002 | Tier 1 | Shapley decomposition foundations |
| `shorrocksInequalityDecompositionFactor1982` | Shorrocks 1982 | Tier 1 | Factor decomposition foundations (Econometrica) |
| `vandegaerMeasurementInequalityOpportunity2020` | Van de gaer & Ramos 2020 | Tier 1 | Counterfactual EOp measurement |
| `almasMeasuringUnfairInequality2011` | Almås et al. 2011 | Tier 2 | Responsibility-sensitive measurement |
| `brunoriUpwardDownwardBias2019` | Brunori et al. 2019 | Tier 2 | IOp measurement bias |
| `chantreuilInequalityDecompositionValues2013` | Chantreuil & Trannoy 2013 | Tier 2 | Decomposition axioms |
| `fleurbaeyExAnteEx2013` | Fleurbaey & Peragine 2013 | Tier 2 | Ex ante vs ex post EOp |
| `kabatekIncomeTaxationLabour2014` | Kabátek et al. 2014 | Tier 2 | France couples baseline — directly relevant for empirical setting |
| `palominoChannelsInequalityOpportunity2019` | Palomino et al. 2019 | Tier 2 | Channels of IOp in Europe |
| `tidotakengDecompositionsInequalityMeasures2023` | Tido Takeng et al. 2023 | Tier 2 | Shapley-Owen grouped decomposition |
| `brunoriOpportunitySensitivePovertyMeasurement2013` | Brunori et al. 2013b | Tier 3 | Opportunity-sensitive poverty (background) |

**Note:** "No PDF in Literature/" means no file matching the paper was found in the top-level `Literature/` folder. These papers may exist in Zotero's internal `files/` directory tree (referenced via bib `file =` fields) but were not exported/copied to the portable `Literature/` folder used by the markdown extraction pipeline.

---

## 7. Papers Cited in Deep Research Reports but Absent from BibTeX

These papers appear in `JMP_gap_check_v1.md` or `LIT_deep-research-report.md` as important additions but have **no BibTeX entry** in `JMP_lit_collection.bib`.

| Author–Year | Title | Source | Priority | Status |
|---|---|---|---|---|
| Aaberge, Dagsvik & Strøm 1995 | Labor Supply Responses and Welfare Effects of Tax Reforms | Scandinavian Journal of Economics | Tier 1 | Has PDF in Literature/; **no bib entry** |
| Chapter 10 / Chapter 11 | [verify title and source] | [verify] | Tier 2 | Has PDF and MD extraction; **no named bib entry** |

---

## 8. Summary Statistics

| Category | Count |
|---|---|
| Total bib entries audited | 87 |
| Full duplicates to delete | 1 (`GDPQuestMeasure`) |
| Near-duplicate PDF paths (same entry) | 6 |
| Author name errors | 1 (`cappauGettingTiredWork2015`) |
| Missing DOI (journal articles) | 16 |
| Entries likely irrelevant for JMP | 5–6 |
| Essential entries missing PDF in Literature/ | 17 |
| Papers with PDF in Literature/ but no bib entry | 2+ |
| Bare stub entries needing full replacement | 2 (`GDPQuestMeasure`, `WelfareLossCaused`) |
| Missing author field | 1 (`Chapter34Welfare2002`) |

---

## 9. Recommended Immediate Actions

1. **Delete** `GDPQuestMeasure` stub entry.
2. **Replace** `WelfareLossCaused` stub with a full entry for Calo-Blanco & García-Pérez 2014.
3. **Add** a bib entry for Aaberge, Dagsvik & Strøm 1995 (PDF already in `Literature/`).
4. **Add** bib entries for `chapter_10` and `chapter_11` once source is verified.
5. **Fix** author/date in `cappauGettingTiredWork2015`.
6. **Add** missing DOIs where available (16 journal articles).
7. **Copy** PDFs for the 17 essential-but-no-PDF entries into `Literature/` to enable markdown extraction.
