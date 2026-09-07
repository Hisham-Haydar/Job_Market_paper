# Consistency gate v2

**Overall: PASS.** Instrument: `reports/run_consistency_gate.py`, implementing `reports/consistency_gate_spec_v1.md`. `reports/consistency_gate_v1.md` is retained unchanged.

Run over a freshly rebuilt H (`reports/research_story_build/build.py`), a freshly re-executed N (14 code cells, execution counts 1-14, zero error outputs), and the deck content file the three rebuilt PDFs were compiled from.

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

0 of 40 (item, artifact) cells FAIL.

## Evidence

### 1. Notation — canonical symbols (spec §1)

All four artifacts PASS with no exceptions recorded.

### 2. The W1 statement (spec §2)

**paper v2 — PASS**

- canonical sentence at 781-785

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

## Inputs

| id | path |
|---|---|
| J | `C:\Users\hisham\Repo\Job_Market_paper\reports\numbers_of_record_v1.json` |
| P | `C:\Users\hisham\Repo\Job_Market_paper\manuscript\JMP_working_paper_for_seminar_v2.md` |
| H | `C:\Users\hisham\Repo\Job_Market_paper\reports\JMP_research_story_report_v1.html` |
| D | `C:\Users\hisham\Repo\Job_Market_paper\manuscript\JMP_seminar_deck_content_v2.md` |
| N | `C:\Users\hisham\Repo\MNL\experiments\JMP_SEMINAR_SPRINT\JMP_research_lab.ipynb` |
