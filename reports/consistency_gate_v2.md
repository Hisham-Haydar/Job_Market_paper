# Consistency gate v2

**Overall: FAIL.** Instrument: `reports/run_consistency_gate.py`, implementing `reports/consistency_gate_spec_v1.md`. `reports/consistency_gate_v1.md` is retained unchanged.

Run over the current build of H and the current saved execution of N.

## Verdict matrix

| # | gate item | paper v2 | story HTML | deck content v2.2 | research-lab notebook (markdown) |
|---|---|---|---|---|---|
| 1 | Notation — canonical symbols (spec §1) | **PASS** | **PASS** | **PASS** | **PASS** |
| 2 | The W1 statement (spec §2) | **PASS** | **PASS** | **PASS** | **PASS** |
| 3 | negLL labels (spec §3) | **PASS** | **PASS** | **N/A** | **FAIL** |
| 4 | Coverage: RQMC bands and CR1 intervals (spec §4) | **PASS** | **PASS** | **PASS** | **PASS** |
| 5 | Nested endowments/needs semantics (spec §5) | **PASS** | **PASS** | **PASS** | **N/A** |
| 6 | Reference labels (spec §6) | **PASS** | **PASS** | **PASS** | **PASS** |
| 7 | Couples beta_ll (spec §7) | **PASS** | **PASS** | **PASS** | **PASS** |
| 8 | The RUM block (spec §8) | **PASS** | **PASS** | **PASS** | **N/A** |
| 9 | Geographic and sex results (spec §9) | **PASS** | **PASS** | **PASS** | **FAIL** |
| 10 | Forbidden terms and permitted sites (spec §10) | **PASS** | **PASS** | **PASS** | **PASS** |
| 11 | Boundary-active coordinates: the age-bound line (spec §11) | **PASS** | **PASS** | **N/A** | **N/A** |
| 12 | Consumption curvature: maintained, not tested (spec §12) | **PASS** | **PASS** | **N/A** | **FAIL** |
| 13 | The couples coefficient table (spec §13) | **PASS** | **PASS** | **N/A** | **N/A** |
| 14 | Children: the male term and child age (spec §14) | **PASS** | **PASS** | **N/A** | **N/A** |
| 15 | Execution profiles and backend parity (spec §15) | **N/A** | **PASS** | **N/A** | **FAIL** |
| 16 | Retired welfare-decomposition lineage: no read by path (DECOMP-PRESEMINAR-1) | **FAIL** | **FAIL** | **PASS** | **FAIL** |

7 of 64 (item, artifact) cells FAIL.

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

- PARA-3 at cell 21/blk 2
- PARA-3 at cell 27/blk 5

### 3. negLL labels (spec §3)

**deck content v2.2 — N/A**

- artifact reports neither negLL value

**research-lab notebook (markdown) — FAIL**

- L1: canonical label `singles final model negLL 18022.764617170084` absent

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

**research-lab notebook (markdown) — FAIL**

- GEO-1: 87.6 %% of the access channel absent
- GEO-1: 13.05 %% of baseline inequality absent

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

**research-lab notebook (markdown) — FAIL**

- TC-1: the curvature is not stated as maintained common
- TC-1: `not tested sex-specifically` is not stated
- TC-1: the scale-numeraire reason is missing
- TC-1: the parsimony reason is missing
- TC-3: not named as a candidate money-metric sensitivity

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

**research-lab notebook (markdown) — FAIL**

- BP: profile server_jax_cpu is not listed
- BP: profile laptop_jax_cpu is not listed
- BP: profile laptop_torch_cuda is not listed
- BP: the parity clearance is not named (PKG-04B / 1eed2756)
- BP-1: the exact negLL is not printed with the parity claim
- BP-1: the parity list omits gradient
- BP-1: the parity list omits hessian
- BP-1: the parity list omits covariance/CR1
- BP-1: the parity list omits standard errors
- BP-1: the parity list omits active-bound set
- BP-1: the parity list omits pinned
- BP-2: the CUDA device caveat is missing
- BP-4: the default-unchanged statement is missing
- BP-4: runtime is not disclaimed

### 16. Retired welfare-decomposition lineage: no read by path (DECOMP-PRESEMINAR-1)

**paper v2 — FAIL**

- retired-lineage path reference(s): gn_step2_nested_v1, headline_decomposition_v1
- registry J (numbers_of_record_v1.json) itself carries retired-lineage source paths in its provenance fields: headline_decomposition_v1, ss8_step1_states_v1

**story HTML — FAIL**

- retired-lineage path reference(s): headline_decomposition_v1, ss8_step1_states_v1

**research-lab notebook (markdown) — FAIL**

- retired-lineage path reference(s): *headline_shares family, s12_*_attributions family

## Inputs

| id | path |
|---|---|
| J | `C:\Users\hisham\Repo\Job_Market_paper\reports\numbers_of_record_v1.json` |
| P | `C:\Users\hisham\Repo\Job_Market_paper\manuscript\JMP_working_paper_for_seminar_v2.md` |
| H | `C:\Users\hisham\Repo\Job_Market_paper\reports\JMP_research_story_report_v1.html` |
| D | `C:\Users\hisham\Repo\Job_Market_paper\manuscript\JMP_seminar_deck_content_v2.md` |
| N | `C:\Users\hisham\Repo\MNL\experiments\JMP_SEMINAR_SPRINT\JMP_research_lab.ipynb` |
