# JMP BibTeX Repair Queue (v1)

**Date:** 2026-06-02
**Target file:** `JMP_lit_collection/JMP_lit_collection.bib` (87 entries incl. stubs)
**Source audits:** `00_admin/JMP_existing_bibtex_audit_v1.md`,
`00_admin/JMP_pdf_inventory_v1.csv`, `00_admin/JMP_literature_rebuild_decision_log_v1.md`.

**Discipline:** Nothing here has been applied to the bib. No metadata is
invented; every uncertain field is marked `[verify]`. Apply in the order below
(deletes/fixes first, additions next, DOI/URL repairs last as a separate batch).

---

## A. Deletions

| # | Action | Entry key | Reason |
|---|---|---|---|
| A1 | **DELETE** | `GDPQuestMeasure` | Bare `@online` stub (no author/year/title) duplicating `fleurbaeyGDPQuestMeasure2009` (Fleurbaey 2009, JEL, "Beyond GDP: The Quest for a Measure of Social Welfare"). Confuses citation software. Keep `fleurbaeyGDPQuestMeasure2009`. |

---

## B. Author / name corrections

| # | Action | Entry key | Fix |
|---|---|---|---|
| B1 | **FIX author** | `cappauGettingTiredWork2015` | Author OCR-corrupted as "Cappau, Bart" and "Decoster, Andrr". Correct to **Capéau, Bart and Decoster, André**. (PDF + MD already use "Capéau".) |
| B2 | **VERIFY date** | `cappauGettingTiredWork2015` | bib `date = 2015` but PDF filename uses 2016. SSRN working-paper year (2015) vs conference/version year (2016). `[verify]` which to keep; record both in a `note`. |
| B3 | **VERIFY author spelling** | `vandegaerMeasurementInequalityOpportunity2020` | Inventory flags "Van de gaer" (lowercase 'd'). `[verify]` the exact `author = {Van de gaer, Dirk and Ramos, Xavier}` form against the bib. |

---

## C. Missing-metadata / stub repairs (author, title)

| # | Action | Entry key | Fix |
|---|---|---|---|
| C1 | **REPLACE stub** | `WelfareLossCaused` | Bare ProQuest stub, no author/title/year. Replace with a full entry for **Calo-Blanco, Aitor and García-Pérez, Á. (2014), "On the Welfare Loss Caused by Inequality of Opportunity", Journal of Economic Inequality** `[verify all fields: exact authors, volume, issue, pages, DOI]`. Suggested key `caloBlancoGarciaPerez2014` (matches the expanded-tiers row; DEFER tier). |
| C2 | **ADD author** | `Chapter34Welfare2002` | `author` field missing. Likely **Moffitt, Robert A.**, "Welfare Programs and Labor Supply", Handbook of Public Economics Vol. 4, Ch. 34 (2002), DOI 10.1016/S1573-4420(02)80013-1. `[verify author = Moffitt]`. |

---

## D. Missing-entry additions (PDF and/or MD exist, no bib entry)

| # | Action | Proposed key | Paper | Evidence | Verify |
|---|---|---|---|---|---|
| D1 | **ADD** | `aabergeLaborSupply1995` | Aaberge, Dagsvik & Strøm (1995), "Labor Supply Responses and Welfare Effects of Tax Reforms", Scandinavian Journal of Economics | PDF + MD in `Literature/`; no bib entry (decision log Decision 2). Original RURO paper. | volume, issue, pages, DOI |
| D2 | **ADD / VERIFY** | `aabergeColombinoStructural2018` | Aaberge & Colombino (2018), "Structural Labour Supply Models and Microsimulation", International Journal of Microsimulation 11(1):162-197 | PDF + MD in `Literature/`; bib entry not found in scan (decision log Decision 8). Welfare spec §4 anchor. | vol/issue/pages exact; DOI |
| D3 | **ADD / VERIFY** | `aaberge1999LabourSupplyItaly` | Aaberge et al. (1999), "Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints", Journal of Applied Econometrics `[verify venue]` | PDF in `Literature/` (PDF-inventory id 3); bib key not confirmed. Welfare spec §4 names "Aaberge-Colombino-Strøm 1999". | venue, vol/pages, DOI, exact author list |
| D4 | **LOCATE or ADD** | `bargainPeichl2016OwnWage` | Bargain & Peichl (2016), "Own-Wage Labor Supply Elasticities: Variation Across Time and Estimation Methods", IZA Journal of Labor Economics `[verify]` | PDF + MD in `Literature/`; bib not confirmed. Elasticity benchmark (T3). | key exists?; full fields |
| D5 | **LOCATE or ADD** | `jonesKlenow2016` | Jones & Klenow (2016), "Beyond GDP? Welfare across Countries and Time", American Economic Review `[verify]` | PDF + MD in `Literature/`; bib not confirmed. Motivation (T3, boundary). | key exists?; full fields |
| D6 | **LOCATE or ADD** | `fleurbaeyHelpLowSkilled2007` | Fleurbaey (2007), "Help the Low Skilled or Let the Hardworking Thrive? A Study of Fairness in Optimal Income Taxation", Journal of Public Economic Theory `[verify]` | PDF + MD in `Literature/` (J Public Economic Theory filename); bib not confirmed. Normative primitive (T3). | key exists?; full fields |
| D7 | **IDENTIFY then ADD** | `chapter_10` | Book chapter 10 — source unknown from filename | PDF + MD in `Literature/`; no identifiable bib. | read MD to identify handbook/source, then full entry |
| D8 | **IDENTIFY then ADD** | `chapter_11` | Book chapter 11 — source unknown from filename | PDF + MD in `Literature/`; no identifiable bib. | read MD to identify handbook/source, then full entry |
| D9 | **IDENTIFY then ADD** | `fleurbaeyManiquet2017` | Fleurbaey & Maniquet (2017) — title unknown | PDF + MD (`Fleurbaey_maniquet_2017.pdf`); no confirmed bib. **May belong to the theory stream — keep boundary.** | identify exact paper/venue/key |
| D10 | **IDENTIFY then ADD** | `fleurbaeyManiquet2019` | Fleurbaey & Maniquet (2019) — title unknown | PDF + MD (`Fleurbaey_maniquet_2019.pdf`); no confirmed bib. **Theory-boundary check.** | identify exact paper/venue/key |
| D11 | **IDENTIFY; possible DUP** | `fleurbaeyManiquet2018` (file) | `Fleurbaey_maniquet_2018.pdf` may duplicate `fleurbaeyOptimalIncomeTaxation2018` (JEL) | PDF + MD; decision log Decision 7. | confirm whether same paper → if so, do NOT add a second entry; note PDF dup |
| D12 | **IDENTIFY then ADD** | `fleurbaey1995` | Fleurbaey (1995) — title unknown | PDF + MD (`Fleurbaey_1995.pdf`); no confirmed bib. | identify exact paper/venue/key |
| D13 | **IDENTIFY then ADD** | `maniquet2008` | Maniquet (2008) — title unknown | PDF + MD (`Maniquet2008.pdf`); no confirmed bib. **Theory-boundary check.** | identify exact paper/venue/key |
| D14 | **IDENTIFY then ADD** | `valetta2010` | Valletta `[verify spelling]` (2010) — title unknown | PDF + MD (`Valetta_2010.pdf`); no confirmed bib. | identify; correct Valetta→Valletta if confirmed |
| D15 | **IDENTIFY then ADD** | `equalOpportunityOrEqualSocialOutcome` | "Equal Opportunity or Equal Social Outcome…" — title truncated | PDF + MD; no confirmed bib. | identify full title/author/year |

> **Note on D7-D15:** these are *identify-first* items. Per the no-invention
> rule, do not author bib entries from filenames alone — read the existing MD
> extraction to confirm identity, then add. Several (D9, D10, D13) may belong to
> the **separate Haydar-Maniquet theory paper** stream, not the empirical JMP
> library; resolve the boundary before citing.

---

## E. Roemer file disambiguation

| # | Action | Detail |
|---|---|---|
| E1 | **VERIFY** | `Roemer-EqualityOpportunityTheory-2016.pdf` is mapped to `roemerEqualityOpportunityTheory2016` (the Roemer & Trannoy JEL survey) in the inventory. Confirm the file is the **JEL survey**, not a separate Roemer monograph; if a monograph file also exists, give it a distinct key. |

---

## F. PDF-attachment hygiene (Zotero export artefacts — not citation-breaking)

Entries whose `file = {}` field references **two** PDF paths for the same paper
(double Zotero import). No citation impact, but the stale path should be pruned
and a single portable copy placed in `Literature/`.

| Entry key | Duplicate file paths |
|---|---|
| `aabergeEvaluatingAlternativeRepresentations2009` | files/1086, files/1174 |
| `bloemenJobSearchHours2008` | files/1177, files/719 |
| `blomquistNonparametricEstimationNonlinear2002` | files/1101, files/1296 |
| `brunoriInequalityOpportunityIncome2013` | files/1349, files/1351 |
| `dagsvikSectoralLabourSupply2006` | files/1052, files/367 |
| `hufeMeasuringUnfairInequality2022` | files/1126, files/1383 |

---

## G. DOI / URL repairs (separate batch — apply last)

### G.1 Journal articles missing a DOI (currently JSTOR/IDEAS URL only)

Add a `doi` field where one exists; keep the URL as fallback. **Do not invent
DOIs** — look each up before adding; mark `[verify]` until confirmed.

| Entry key | Journal |
|---|---|
| `bloemenJobSearchHours2008` | Journal of Labor Economics |
| `bloemenModelLabourSupply2000` | Labour Economics |
| `blomquistNonparametricEstimationNonlinear2002` | Econometrica |
| `brunoriUpwardDownwardBias2019` | Social Choice and Welfare |
| `chettySufficientStatisticsWelfare2009` | Annual Review of Economics |
| `choneNegativeMarginalTax2010` | American Economic Review |
| `dagsvikCompensatingVariationHicksian2005` | Review of Economic Studies |
| `fleurbaeyExAnteEx2013` | Economica |
| `fleurbaeyFairIncomeTax2006` | Review of Economic Studies |
| `immervollWelfareReformEuropean2007` | Economic Journal |
| `masValuingAlternativeWork2017` | American Economic Review |
| `palominoChannelsInequalityOpportunity2019` | Social Indicators Research |
| `roemerEqualityOpportunityProgress2002` | Social Choice and Welfare |
| `saezGeneralizedSocialMarginal2016` | American Economic Review |
| `saezOptimalIncomeTransfer2002` | Quarterly Journal of Economics |
| `vandegaerMeasurementInequalityOpportunity2020` | Social Choice and Welfare |
| `bhattacharyaNonparametricWelfareAnalysis2015` | Econometrica (verify DOI present) |

### G.2 Preprints / working papers — URL only (no DOI expected)

`audolyPractitionersNoteShapleyOwenShorrocks2025` (SSRN — has DOI, OK),
`jacquetHowMuchDoes2026` (SSRN — add DOI field if minted),
`bargainPuttingStructureRD2013` (IZA via JSTOR),
`brunoriOpportunitySensitivePovertyMeasurement2013` (IZA via JSTOR),
`lofflerStructuralLaborSupply2014` (SOEPpapers/Econstor). URL is acceptable;
no action required beyond confirming the URL resolves.

---

## H. Apply order (summary)

1. **A1** delete stub.
2. **B1-B3** name/date fixes.
3. **C1-C2** stub-replace + missing author.
4. **D1-D6** straightforward additions (identifiable papers).
5. **D7-D15, E1** identify-first additions (read MD; theory-boundary check).
6. **F** prune duplicate `file=` paths; copy one portable PDF to `Literature/`.
7. **G** DOI/URL batch (look up; never invent).

After applying, regenerate any derived artefacts and bump this queue to `_v2`
recording what was actually applied vs still `[verify]`.
