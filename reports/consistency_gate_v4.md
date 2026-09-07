# Consistency gate v4

**Overall: PASS.** Instrument: `reports/run_consistency_gate.py`, implementing `reports/consistency_gate_spec_v1.md`. `reports/consistency_gate_v1.md` is retained unchanged.

Run over story report v2: H rebuilt from the reader-facing rewrite of sections 3, 6, 7, 13-14 and the new glossary section 24; N at its last execution; the deck content the three PDFs were compiled from.

## Verdict matrix

| # | gate item | paper v2 | story HTML | deck content v2.2 | research-lab notebook (markdown) |
|---|---|---|---|---|---|
| 1 | Notation — canonical symbols (spec §1) | **PASS** | **PASS** | **PASS** | **PASS** |
| 2 | The W1 statement (spec §2) | **PASS** | **PASS** | **PASS** | **PASS** |
| 3 | negLL labels (spec §3) | **PASS** | **PASS** | **N/A** | **PASS** |
| 4 | Coverage: RQMC bands and CR1 intervals (spec §4) | **PASS** | **PASS** | **PASS** | **PASS** |
| 5 | Nested endowments/needs semantics (spec §5) | **PASS** | **PASS** | **PASS** | **N/A** |
| 6 | Reference labels (spec §6) | **PASS** | **PASS** | **PASS** | **PASS** |
| 7 | Couples beta_ll (spec §7) | **PASS** | **PASS** | **PASS** | **PASS** |
| 8 | The RUM block (spec §8) | **PASS** | **PASS** | **PASS** | **N/A** |
| 9 | Geographic and sex results (spec §9) | **PASS** | **PASS** | **PASS** | **PASS** |
| 10 | Forbidden terms and permitted sites (spec §10) | **PASS** | **PASS** | **PASS** | **PASS** |
| 11 | Boundary-active coordinates: the age-bound line (spec §11) | **PASS** | **PASS** | **N/A** | **N/A** |
| 12 | Consumption curvature: maintained, not tested (spec §12) | **PASS** | **PASS** | **N/A** | **N/A** |
| 13 | The couples coefficient table (spec §13) | **PASS** | **PASS** | **N/A** | **N/A** |
| 14 | Children: the male term and child age (spec §14) | **PASS** | **PASS** | **N/A** | **N/A** |
| 15 | Execution profiles and backend parity (spec §15) | **N/A** | **PASS** | **N/A** | **PASS** |

0 of 60 (item, artifact) cells FAIL.

## Evidence

### 1. Notation — canonical symbols (spec §1)

All four artifacts PASS with no exceptions recorded.

### 2. The W1 statement (spec §2)

**paper v2 — PASS**

- canonical sentence at 788-792

**story HTML — PASS**

- PARA-3 at s13

**deck content v2.2 — PASS**

- PARA-1 at 20-21
- PARA-2 at 44-45

**research-lab notebook (markdown) — PASS**

- PARA-3 at cell 17/blk 2
- PARA-3 at cell 23/blk 4

### 3. negLL labels (spec §3)

**deck content v2.2 — N/A**

- artifact reports neither negLL value

### 4. Coverage: RQMC bands and CR1 intervals (spec §4)

All four artifacts PASS with no exceptions recorded.

### 5. Nested endowments/needs semantics (spec §5)

**research-lab notebook (markdown) — N/A**

- artifact does not report the nested split

### 6. Reference labels (spec §6)

All four artifacts PASS with no exceptions recorded.

### 7. Couples beta_ll (spec §7)

All four artifacts PASS with no exceptions recorded.

### 8. The RUM block (spec §8)

**research-lab notebook (markdown) — N/A**

- artifact does not report the RUM comparison

### 9. Geographic and sex results (spec §9)

All four artifacts PASS with no exceptions recorded.

### 10. Forbidden terms and permitted sites (spec §10)

All four artifacts PASS with no exceptions recorded.

### 11. Boundary-active coordinates: the age-bound line (spec §11)

**deck content v2.2 — N/A**

- artifact does not introduce the boundary-active coordinates

**research-lab notebook (markdown) — N/A**

- artifact does not introduce the boundary-active coordinates

### 12. Consumption curvature: maintained, not tested (spec §12)

**deck content v2.2 — N/A**

- artifact does not report the consumption curvature

**research-lab notebook (markdown) — N/A**

- artifact does not report the consumption curvature

### 13. The couples coefficient table (spec §13)

**deck content v2.2 — N/A**

- artifact does not carry the couples coefficient table

**research-lab notebook (markdown) — N/A**

- artifact does not carry the couples coefficient table

### 14. Children: the male term and child age (spec §14)

**deck content v2.2 — N/A**

- artifact does not report the male child term

**research-lab notebook (markdown) — N/A**

- artifact does not report the male child term

### 15. Execution profiles and backend parity (spec §15)

**paper v2 — N/A**

- artifact does not carry the profile table, and no obsolete backend claim remains

**deck content v2.2 — N/A**

- artifact does not carry the profile table, and no obsolete backend claim remains

## Inputs

| id | path |
|---|---|
| J | `C:\Users\hisham\Repo\Job_Market_paper\reports\numbers_of_record_v1.json` |
| P | `C:\Users\hisham\Repo\Job_Market_paper\manuscript\JMP_working_paper_for_seminar_v2.md` |
| H | `C:\Users\hisham\Repo\Job_Market_paper\reports\JMP_research_story_report_v1.html` |
| D | `C:\Users\hisham\Repo\Job_Market_paper\manuscript\JMP_seminar_deck_content_v2.md` |
| N | `C:\Users\hisham\Repo\MNL\experiments\JMP_SEMINAR_SPRINT\JMP_research_lab.ipynb` |
