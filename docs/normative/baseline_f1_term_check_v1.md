# baseline_f1_term_check_v1.md — GATE-1 step 2, term-by-term hard gate

**Mission:** GATE-1 — MEASURE-MAP-1R acceptance, step 2 (mechanical term-by-term
check). **Status: HARD GATE, PASS.** One row per estimated parameter in the S11
singles and couples tables (99 rows total, 52 + 47). No disagreement found.

**Rule (verbatim from the card).** PASS only if every UTILITY parameter is a
leisure term and every parameter in the utility block other than consumption is
UTILITY. The consumption term (`beta_c`, and singles' `theta_c_singles`) is the
one named exception to "every UTILITY parameter is a leisure term": it is a
UTILITY-block member that is not part of $L_i(j)$, by the card's own carve-out
("other than consumption").

## 0. Inputs and method

- **Classification source:** `MNL/docs/corr/baseline_f1_provenance_v1.md` §3
  ("Exhaustive parameter partition"), sha256 of the worktree copy inspected
  `4bbce0f744677b6e1aa487f66eff3083b04597d628aa856148b6ef1cf36f04a6`
  (this is a later state than the acceptance record's citation of commit
  `838127e0`/`ab6e544f…`, because commit `68644680` prepended a short status
  note to the same file; the classification table itself — §3, singles and
  couples — is unchanged between the two commits, verified by `git diff`).
- **Utility-block source:** `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py`,
  read directly, both factories:
  - singles `build_jax_singles_ll`, `index(theta)` at lines 292–340; the
    systematic-utility sub-block the card cites is lines 303–308 (`bc_c`
    through `u = beta_l_coeff * bc_l + beta_c * bc_c`), which sits inside the
    fuller `# ---- utility ----` block at 299–308. Opportunity terms (hours,
    wage, market/occupation) are computed separately at lines 310–337, outside
    both the card's window and the fuller utility block.
  - couples `build_jax_couples_ll`, `index(theta)` at lines 508–559; the
    systematic-utility sub-block the card cites is lines 519–530 (`bc_c`
    through `u = blc_m*bc_l_m + blc_f*bc_l_f + beta_c*bc_c + beta_ll*bc_l_m*bc_l_f`),
    inside the fuller block at 514–530. Opportunity terms are computed
    separately at lines 532–556.
  - **Note on `beta_ll`.** The couples utility line carries a cross-leisure
    interaction term `beta_ll * bc_l_m * bc_l_f` in the code. It is **not** an
    estimated coordinate: `beta_ll = P(interaction_name) if interaction_name
    else 0.0`, and the accepted couples specification declares no
    `interaction_name`, so `beta_ll` is always exactly `0.0` and contributes
    nothing. Confirmed: `beta_ll` does not appear as a row in either S11
    parameter table (`grep` returns no match, both files). There is therefore
    no parameter to classify for it, and its presence in the code is not a
    disagreement with any classification.
- **L-statement source:** `Job_Market_paper/docs/normative/JMP_measure_map_v1.md`
  (committed this GATE-1 pass, sha256
  `6568ec53936c48fdafe4376714b6d2eaa8d37f30db040da25014773023534cc9`), line 158
  ("Coefficients include the stored household age, squared-age, and applicable
  child shifters") and line 185 ("The current L has no wage or occupation
  term"). The card's paraphrase — "age, age², child shifters, theta_l" — matches
  this statement; `theta_l` is the Box-Cox curvature of the leisure term itself
  and is inseparable from "the leisure coefficients."
- **Parameter lists:** read directly from
  `experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv`
  (sha256 `cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab`,
  52 rows) and `…/s11_couples_parameter_table_v1.csv` (sha256
  `fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9`, 47 rows).
  These are the two hashes the accepted gate file also pins (§3 below).

Three columns are filled per row: (i) the provenance document's classification;
(ii) whether the parameter's coefficient is referenced inside the cited utility
sub-block (determined by reading the loop that builds `leis_shifters` /
`leis_m`/`leis_f` at lines 211–222 and 405–423, which bind exactly
`beta_l0{suffix}`, `beta_l_age{suffix}`, `beta_l_age2{suffix}`, the female-only
`beta_l_nkids{suffix}`, and `theta_l{suffix}`, against the corresponding
opportunity loops at 230–337 / 532–556 which bind every `beta_E*`, `beta_h_*`,
`beta_occ_*`, `beta_w_*`, `sigma`, `delta_occ_*`); (iii) whether that is
consistent with MEASURE-MAP-1R's stated composition of $L$.

## 1. Singles — 52 parameters

| Parameter | Pin | Provenance classification | In utility block (`engine_jax.py:303–308`)? | Consistent with "L = leisure terms only"? |
|---|---|---|---|---|
| `beta_l0_sm` | free | UTILITY | Yes | Yes — leisure intercept |
| `beta_l_age_sm` | free | UTILITY | Yes | Yes — age shifter |
| `beta_l_age2_sm` | free | UTILITY | Yes | Yes — age² shifter |
| `theta_l_sm` | free | UTILITY | Yes | Yes — leisure Box-Cox curvature |
| `beta_l0_sf` | free | UTILITY | Yes | Yes — leisure intercept |
| `beta_l_age_sf` | free | UTILITY | Yes | Yes — age shifter |
| `beta_l_age2_sf` | free | UTILITY | Yes | Yes — age² shifter |
| `beta_l_nkids_sf` | free | UTILITY | Yes | Yes — child shifter (female-only) |
| `theta_l_sf` | free | UTILITY | Yes | Yes — leisure Box-Cox curvature |
| `theta_c_singles` | pinned | UTILITY | Yes | **N/A — consumption term, the card's named exception** |
| `beta_l0_m` | pinned | UTILITY | Yes (pinned inactive couples-suffix coordinate, routed out for singles) | Yes — leisure intercept, on the coordinate it belongs to when active |
| `beta_l_age_m` | pinned | UTILITY | Yes (pinned inactive) | Yes — age shifter |
| `beta_l_age2_m` | pinned | UTILITY | Yes (pinned inactive) | Yes — age² shifter |
| `beta_l0_f` | pinned | UTILITY | Yes (pinned inactive) | Yes — leisure intercept |
| `beta_l_age_f` | pinned | UTILITY | Yes (pinned inactive) | Yes — age shifter |
| `beta_l_age2_f` | pinned | UTILITY | Yes (pinned inactive) | Yes — age² shifter |
| `beta_l_nkids_f` | pinned | UTILITY | Yes (pinned inactive) | Yes — child shifter |
| `theta_l_f` | pinned | UTILITY | Yes (pinned inactive) | Yes — leisure Box-Cox curvature |
| `beta_E` | free | OPPORTUNITY (g) | No — lines 310–314 | N/A — not in utility block |
| `beta_h_pt1` | free | OPPORTUNITY (g) | No — lines 310–314 | N/A |
| `beta_h_pt2` | free | OPPORTUNITY (g) | No — lines 310–314 | N/A |
| `beta_h_ft` | free | OPPORTUNITY (g) | No — lines 310–314 | N/A |
| `beta_h_lh` | free | OPPORTUNITY (g) | No — lines 310–314 | N/A |
| `beta_E_gsur` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgn2` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgn3` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgn4` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgn5` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgn6` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgn7` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgn8` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_y2015` | pinned | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_y2017` | pinned | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgur` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_E_drgmd` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_occ_2_m` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_occ_3_m` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_occ_4_m` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_occ_2_f` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_occ_3_f` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_occ_4_f` | free | OPPORTUNITY (g) | No — lines 328–337 | N/A |
| `beta_w0` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `beta_w_educL` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `beta_w_educH` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `beta_w_pexp` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `beta_w_pexp2` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `sigma` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `delta_occ_2` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `delta_occ_3` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `delta_occ_4` | free | OPPORTUNITY (g) | No — lines 316–326 | N/A |
| `beta_h_f35` | free | OPPORTUNITY (g) | No — lines 310–314 (F35 band extension) | N/A |
| `beta_c` | free | UTILITY | Yes | **N/A — consumption term, the card's named exception** |

**Singles disagreements: none.** 41 free + 11 pinned = 52 rows, matching S11's
recorded coordinate count.

## 2. Couples — 47 parameters

| Parameter | Pin | Provenance classification | In utility block (`engine_jax.py:519–530`)? | Consistent with "L = leisure terms only"? |
|---|---|---|---|---|
| `beta_l0_m` | free | UTILITY | Yes | Yes — leisure intercept |
| `beta_l_age_m` | free | UTILITY | Yes | Yes — age shifter |
| `beta_l_age2_m` | free | UTILITY | Yes | Yes — age² shifter |
| `theta_l_m` | free | UTILITY | Yes | Yes — leisure Box-Cox curvature |
| `beta_l0_f` | free | UTILITY | Yes | Yes — leisure intercept |
| `beta_l_age_f` | free | UTILITY | Yes | Yes — age shifter |
| `beta_l_age2_f` | free | UTILITY | Yes | Yes — age² shifter |
| `beta_l_nkids_f` | free | UTILITY | Yes | Yes — child shifter (female-only) |
| `theta_l_f` | free | UTILITY | Yes | Yes — leisure Box-Cox curvature |
| `beta_E_m` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_E_f` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_pt1_m` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_pt1_f` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_pt2_m` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_pt2_f` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_f35_m` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_f35_f` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_ft_m` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_ft_f` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_lh_m` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_h_lh_f` | free | OPPORTUNITY (g) | No — lines 532–535 | N/A |
| `beta_E_gsur` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgn2` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgn3` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgn4` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgn5` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgn6` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgn7` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgn8` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgur` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_E_drgmd` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_occ_2_m` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_occ_3_m` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_occ_4_m` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_occ_2_f` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_occ_3_f` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_occ_4_f` | free | OPPORTUNITY (g) | No — lines 549–556 | N/A |
| `beta_w0` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `beta_w_educL` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `beta_w_educH` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `beta_w_pexp` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `beta_w_pexp2` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `sigma` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `delta_occ_2` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `delta_occ_3` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `delta_occ_4` | free | OPPORTUNITY (g) | No — lines 540–547 | N/A |
| `beta_c` | free | UTILITY | Yes | **N/A — consumption term, the card's named exception** |

**Couples disagreements: none.** All 47 rows free (couples specification pins
`theta_c` to `0.0` structurally, in the spec YAML, not as a CSV coordinate —
so there is no couples `theta_c` row to classify; confirmed absent from the
CSV). 47 matches S11's recorded couples coordinate count.

## 3. Verdict

**PASS.** Across 99 rows (52 singles + 47 couples):

- Every parameter the provenance document classifies UTILITY is either a
  leisure term (intercept, age, age², the female-only child shifter, or the
  leisure Box-Cox curvature `theta_l`) or the named consumption exception
  (`beta_c`, `theta_c_singles`).
- Every parameter that is referenced inside the cited utility sub-block
  (`engine_jax.py:303–308` singles / `519–530` couples) is classified UTILITY;
  no OPPORTUNITY-classified parameter is referenced there.
- MEASURE-MAP-1R's stated composition of $L$ ("age, squared-age, and
  applicable child shifters"; "no wage or occupation term") matches exactly
  what the code and the provenance document independently show.
- The couples-only cross-leisure term `beta_ll` appears in the utility formula
  but is not an estimated coordinate (fixed at `0.0`, absent from the CSV), so
  it does not enter this check as a row and is not a disagreement.

No disagreement of any kind was found. GATE-1 proceeds to step 3.
