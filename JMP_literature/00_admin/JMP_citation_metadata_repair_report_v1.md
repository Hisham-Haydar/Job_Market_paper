# JMP Citation Metadata Repair Report — v1

**Date:** 2026-06-04
**Scope:** Narrow citation metadata repairs authorized before drafting the
literature-review skeleton. No summaries produced. No summaries edited. No
external searches run. No indexes updated beyond the authorized INDEX 01 v2.

---

## 1. Repair verdict

**PASSED WITH WARNINGS.**

The two missing bib entries (`bloemenCollectiveHousehold2010` and
`cameronMillerClusterRobust2015`) have been added to the base `.bib` file.
INDEX 01 v2 has been written reflecting all five DR03 accepted additions and
their citation warnings.

One warning persists that is **not resolved** in this session:
- **Bloemen 2000 PDF content mismatch** — the bib entry
  `bloemenModelLabourSupply2000` correctly records the published journal article
  (*Labour Economics* 7(3):297–312, 2000). The PDF in `Literature/` is however
  the 1992 CentER Discussion Paper No. 9239 (confirmed below). The bib
  `file=` attachment in Zotero storage (`files/715/`) also refers to this DP.
  The journal article PDF has not been acquired. The `[DP version; journal pages
  TBC]` flag propagates into all citing indexes and the writing bank §16 until
  this is resolved.

Löffler 2014 version note is resolved: the bib already has
`lofflerStructuralLaborSupply2014` (SOEPpapers 675, Econstor URL) and the
published version `loefflerSensitivityStructuralLabor2018`. Both are available.
No repair needed; note recorded below.

---

## 2. Files inspected

| File | Purpose |
|---|---|
| `JMP_DR03_index_update_report_v1.md` | Authorised repairs and open warnings |
| `JMP_DR03_added_summaries_QC_report_v1.md` | Acceptance status and metadata repair queue |
| `JMP_DR03_added_summaries_repair_queue_v1.csv` | 5 repairs (R01–R05) |
| `JMP_bibtex_repair_queue_v1.md` | Pre-existing repair queue (not applied in this session) |
| `INDEX_01_master_bibliography_v1.md` | 23 official T1A/T1B entries + 1 supplementary |
| `JMP_lit_collection/JMP_lit_collection.bib` | 87-entry base BibTeX file |
| `T1B/Bloemen_2010_collective_household.md` | §0 metadata confirmed |
| `T2/Cameron_Miller_2015_cluster_robust.md` | §0 metadata confirmed |
| `T1A/Bloemen_2000_job_offer_restrictions.md` | §0 metadata confirmed (DP vs journal) |
| `T2/Loffler_et_al_2014_wage_exogeneity.md` | §0 metadata confirmed (SOEPpapers) |

---

## 3. BibTeX entries added

### 3.1 `bloemenCollectiveHousehold2010`

**Status before:** MISSING — no entry in `JMP_lit_collection.bib`.

**Entry added:**
```bibtex
@article{bloemenCollectiveHousehold2010,
  title = {An {{Empirical Model}} of {{Collective Household Labour Supply}}
           with {{Non-Participation}}},
  author = {Bloemen, Hans G.},
  date = {2010},
  journaltitle = {The Economic Journal},
  volume = {120},
  number = {543},
  pages = {183--214},
  doi = {10.1111/j.1468-0297.2009.02292.x},
  url = {https://doi.org/10.1111/j.1468-0297.2009.02292.x},
  langid = {english},
  note = {T1B: contrastive background source. ...},
  file = {Literature/Bloemen_2010_An Empirical Model of Collective Household
          Labour Supply with Non-Participation.pdf}
}
```

**Metadata source:** Confirmed against the Bloemen 2010 summary §0 Metadata,
which records Economic Journal 120(543):183–214 and DOI
`10.1111/j.1468-0297.2009.02292.x`. The PDF in `Literature/` (ASCII-hyphen
filename, 689 KB) was confirmed correct in the acquisition close-out report.

**DOI status:** Recorded from the summary; plausible for an Economic Journal
2010 paper but not independently verified via publisher website in this session
(no external search run). Flagged in the bib entry `note` field; acceptable for
drafting. Verify before final submission.

**`file=` path:** Points to the ASCII-safe copy in `Literature/` (the copy
created to work around the pdftotext U+2010 filename issue). The original
U+2010-filename PDF also exists in `Literature/`; both are identical (689 KB).

---

### 3.2 `cameronMillerClusterRobust2015`

**Status before:** MISSING — no entry in `JMP_lit_collection.bib`.

**Entry added:**
```bibtex
@article{cameronMillerClusterRobust2015,
  title = {A {{Practitioner}}'s {{Guide}} to {{Cluster-Robust Inference}}},
  author = {Cameron, A. Colin and Miller, Douglas L.},
  date = {2015},
  journaltitle = {Journal of Human Resources},
  volume = {50},
  number = {2},
  pages = {317--372},
  url = {https://www.jstor.org/stable/24735989},
  langid = {english},
  note = {T2: inference infrastructure only. ...},
  file = {Literature/Cameron_Miller_2015_A Practitioner's Guide to
          Cluster-Robust Inference.pdf}
}
```

**Metadata source:** Confirmed against the Cameron-Miller 2015 summary §0
Metadata, which records JHR 50(2):317–372 and JSTOR URL
`https://www.jstor.org/stable/24735989`. The acquisition close-out confirmed
the PDF content is the correct paper (JHR 50-2, 2015; authors Cameron and
Miller; cluster-robust inference).

**DOI status:** The canonical JHR DOI for this paper is not confirmed in a local
source. The JSTOR stable URL is included as the URL field; a DOI field can be
added after confirmation (repair R05 in the repair queue). The URL is sufficient
for drafting.

---

## 4. BibTeX entries not added

The following repairs from the pre-existing `JMP_bibtex_repair_queue_v1.md`
were **not applied** in this session. They are not authorized in this narrow
citation repair gate. They remain in the queue for a separate full BibTeX repair
pass.

| Repair | Key | Reason not applied here |
|---|---|---|
| A1 Delete stub | `GDPQuestMeasure` | Out of scope |
| B1–B3 Author/name fixes | `cappauGettingTiredWork2015` et al. | Out of scope |
| C1–C2 Stub repairs | `WelfareLossCaused`, `Chapter34Welfare2002` | Out of scope |
| D1–D15 Missing additions | Various | Out of scope |
| E1 Roemer disambiguation | `roemerEqualityOpportunityTheory2016` | Out of scope |
| F PDF duplicate hygiene | Various | Out of scope |
| G DOI/URL batch | Various | Out of scope |

---

## 5. Bloemen 2000 version status

**Status: WARNING PERSISTS — DP version in Literature/; journal-article bib
entry exists; PDF mismatch unresolved.**

### What was found

| Item | Status |
|---|---|
| **Bib entry `bloemenModelLabourSupply2000`** | **EXISTS** and is correct: *Labour Economics* 7(3):297–312 (2000), publisher Elsevier, URL pointing to Ideas/RepEC record. |
| **Bib `file=` attachment** | Points to Zotero-internal path `files/715/Bloemen_2000_A model of labour supply with job offer restrictions.pdf`. This file is managed by Zotero and has not been inspected directly. |
| **`Literature/Bloemen_2000_A model of labour supply with job offer restrictions.pdf`** | Present; 8.25 MB. The summary explicitly identifies this as the 1992 CentER Discussion Paper No. 9239 (October 1992). The 1992 DP is substantially longer than a typical journal article (explaining the 8.25 MB size vs the Bloemen 2008 PDF at ~1 MB for a comparable 43-page JoLE article). |
| **`md_extractions/Bloemen_2000_...md`** | Produced from the DP PDF. Summary page references refer to DP internal pagination. |
| **Journal article PDF (*Labour Economics* 7(3):297–312)** | **NOT present** in `Literature/` and not available locally. |

### Implication

The bib entry `bloemenModelLabourSupply2000` has correct **citation metadata**
(journal, volume, number, pages, publisher). This is the entry that will appear
in the LaTeX bibliography when `\cite{bloemenModelLabourSupply2000}` is used.
The formatted reference will correctly read:

> Bloemen, H. G. (2000). A model of labour supply with job offer restrictions.
> *Labour Economics*, 7(3), 297–312.

This is the correct published reference. **The bib entry itself does not need to
be changed.**

The **warning** is about the **PDF content** used to produce the MD extraction
and summary: the summary page numbers and direct quotes refer to the 1992 DP,
not to the journal article. This must be flagged in the draft:
- Do not use summary page numbers in manuscript footnotes.
- Treat direct quotes from the summary as `[DP version; verify against journal]`.
- The journal article reference itself is correct and may be used in citations.

### Action required to clear

Acquire *Labour Economics* 7(3):297–312 (2000) PDF from Elsevier/ScienceDirect
(DOI pending — see repair R04 in `JMP_DR03_added_summaries_repair_queue_v1.csv`
row R04, which covers Bloemen 2008 DOI; and repair R01 which covers the DP
version issue). Replace the `Literature/` PDF and re-run the MD extraction. Then
update §0 Metadata and §14 Direct quotes in the summary.

---

## 6. Löffler et al. version status

**Status: RESOLVED — both working-paper and published versions are in the bib.**

### What was found

| Item | Status |
|---|---|
| **`lofflerStructuralLaborSupply2014`** | EXISTS in bib: `@report`, type = Working Paper, number = 675 (SOEPpapers), institution = SSRN / Econstor URL `https://econstor.eu/...`. The summary §0 records `hdl.handle.net/10419/99953` (same Econstor handle, same paper). |
| **`loefflerSensitivityStructuralLabor2018`** | EXISTS in bib: published SSRN journal version, date = 2018. The acquisition queue referenced "IZA DP 8281". The entry with key `lofflerStructuralLaborSupply2014` has `number = 675` matching SOEPpapers 675; IZA DP 8281 and SOEPpapers 675 are both circulation channels for the same working paper. |
| **PDF in `Literature/`** | `Löffler et al_2014_Structural labor supply models and wage exogeneity.pdf` (604 KB) is present. |

### Conclusion

Both the 2014 working-paper version and the 2018 published version are
in the bib. The IZA DP 8281 number is an alternate working-paper handle for
the same paper. The summary may cite `lofflerStructuralLaborSupply2014` for the
working-paper version or `loefflerSensitivityStructuralLabor2018` for the
published version; they are interchangeable for the same substantive claim. The
outlet discrepancy noted in INDEX 06 v2 and the repair queue (R03) is a
cosmetic record-keeping note, not a blocking issue. No further action needed.

---

## 7. Master bibliography update

INDEX 01 v2 has been created incorporating all DR03 accepted additions. See
`JMP_literature/04_indexes/INDEX_01_master_bibliography_v2.md`.

The v2 file adds:
- Five new rows for the DR03 accepted additions (T1A: Bloemen 2000, Bloemen
  2008; T1B: Bloemen 2010; T2: Cameron-Miller 2015, Löffler 2014)
- An updated T2/other section for the two new T2 sources
- Citation warnings propagated from the QC report and this repair report

---

## 8. Remaining citation warnings

After this session, the following citation warnings remain active.

| Warning | Source | Priority | Blocks |
|---|---|---|---|
| **[DP version; journal pages TBC]** — PDF in Literature/ is 1992 CentER DP; summary page refs and quotes are DP-pagination. Bib entry itself is correct. Do not use page numbers in manuscript. | Bloemen 2000 | MEDIUM | Final manuscript page citations only; does not block drafting |
| **DOI missing** — `bloemenModelLabourSupply2000` bib has no `doi=` field, only an Ideas/RepEC URL. The journal DOI (Elsevier/ScienceDirect) should be added. | Bloemen 2000 | LOW | No |
| **DOI missing** — `bloemenJobSearchHours2008` has no `doi=` field (only Ideas/RepEC URL). DOI `10.1086/522069` flagged `[verify]` in summary. | Bloemen 2008 | LOW | No |
| **DOI not confirmed** — `bloemenCollectiveHousehold2010` bib records DOI `10.1111/j.1468-0297.2009.02292.x` from the summary; not independently verified. | Bloemen 2010 | LOW | No |
| **DOI missing** — `cameronMillerClusterRobust2015` has JSTOR URL only; canonical JHR DOI not yet added. | Cameron-Miller 2015 | LOW | No |
| **Bibkey in summary ≠ canonical** — Summary §0 records informal keys; canonical keys now in bib. No edit to summaries required for drafting. | All five DR03 summaries | LOW | No |
| **Pre-existing BibTeX repair queue** — `JMP_bibtex_repair_queue_v1.md` items A1–G remain unapplied. | Multiple entries | BACKGROUND | No |

---

## 9. What was not done

- **The pre-existing BibTeX repair queue** (`JMP_bibtex_repair_queue_v1.md`
  items A1–G) was not applied. Not authorized in this session.
- **The journal article PDF for Bloemen 2000** (*Labour Economics* 7(3):297–312)
  was not acquired. Requires external access to Elsevier/ScienceDirect.
- **No summary files were edited.** The informal bibkeys in summary §0 sections
  were not updated; they remain at the informal names recorded at summary
  production time (`Bloemen2010`, `cameron_miller_2015_cluster_robust`, etc.).
  These can be updated as a low-priority cosmetic pass.
- **INDEX 02/06/07/08** were not re-touched. These remain at v2 as written in
  the prior session.
- **Tier CSV was not updated.** The physical `JMP_literature_tiers_expanded_v1.csv`
  still reflects the pre-DR03 state; Bloemen 2000/2008 are still listed as T3
  there.
- **§9 verification** for the four conditional sources was not run.

---

## 10. Whether literature-review skeleton may proceed

**Yes.**

All five DR03 accepted summaries are indexed in INDEX 01 v2, INDEX 02 v2,
INDEX 06 v2, INDEX 07 v2, and INDEX 08 v2. Both new bib entries are in the
`.bib` file, enabling `\cite{}` in LaTeX drafts.

The **Bloemen 2000** `[DP version; journal pages TBC]` warning must be carried
into the draft for any page reference or direct quote. The citation itself
(`\cite{bloemenModelLabourSupply2000}`) is correct and will produce the right
formatted reference.

The **four conditional sources** (Magnac-Robin, Dagsvik-Strøm-Locatelli,
Crede/Grammatikos, Sun-Leung) remain gated and may not appear in the draft.

---

## 11. Immediate next action

1. **Begin literature-review skeleton draft** — all indexes are now at v2, all
   bib entries are in place, INDEX 01 is at v2. Use INDEX 08 v2 §§1–16 as the
   paragraph skeleton template. Carry `[DP version; journal pages TBC]` for any
   Bloemen 2000 page reference.

2. **Apply tier CSV update** — promote Bloemen 2000/2008 from T3 to T1A; add
   Bloemen 2010 as T1B; add Cameron-Miller 2015 as T2; promote Löffler 2014
   from T3 to T2 in `JMP_literature_tiers_expanded_v1.csv`. Then update
   INDEX 00 (T1A/T1B status register).

3. **Acquire Bloemen 2000 journal PDF** (medium priority) — *Labour Economics*
   7(3):297–312 (2000) via Elsevier/ScienceDirect. Replace the Literature/
   PDF and re-extract. Update §0 and §14 of the summary. Clear the
   `[DP version; journal pages TBC]` flag in the indexes.

4. **Add DOIs** (low priority, separate batch) — confirm and add `doi=` fields
   for `bloemenModelLabourSupply2000`, `bloemenJobSearchHours2008`,
   `cameronMillerClusterRobust2015`. Verify `bloemenCollectiveHousehold2010`
   DOI. Part of the pre-existing G batch in the repair queue.

5. **Apply the remaining BibTeX repair queue** (`JMP_bibtex_repair_queue_v1.md`
   items A–G) as a separate full-bib repair session after the skeleton draft is
   underway.

6. **Run §9 verification** for the four conditional sources — manual lookup via
   publisher websites, DOI, Econlit, SSRN. Record outcomes in
   `JMP_DR03_verification_log_v1.md`.

---

**CITATION REPAIR STATUS: PASSED WITH WARNINGS**

Both authorized bib entries added. INDEX 01 v2 written. The Bloemen 2000
PDF/DP warning persists but does not block drafting; the bib citation is correct.
All DOI additions are low priority. Literature-review skeleton may proceed.
