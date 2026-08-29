<!-- GOVERNANCE DOCUMENT — CURRENT-STATE SURFACE -->

# JMP Current-State Dashboard v1

**Programme:** Goal 1 — Empirical JMP
**Last updated:** 2026-08-29, at Goal-1 R-183 / R-184.1.
**Standing:** Established by the PI STANDING DIRECTION — PRACTICAL RESEARCH
MODE (recorded verbatim at Goal-1 R-168): *"Maintain one current-state
dashboard rather than multiple overlapping status memos."*

**This file is THE status surface from R-168 forward.** Superseded status
memos are no longer created. Existing status memos remain valid as immutable
history of the moment they recorded; they are not the current state. Update
this file in place; do not fork a v2 for a status change.

This dashboard is a pointer surface, not an authority. Where it and a ratified
document differ, the ratified document governs.

---

## 1. Programme status labels — all current

| Label | Object it qualifies | Set at |
|---|---|---|
| **`S8_PREFERRED_SINGLES_POSITIVE_SPECIFICATION`** | S8 = S0 + S3 (LOC4/S0 plus the explicit 35-hour opportunity peak), the preferred **singles positive** specification | **R-183** (`_PENDING_BOUNDED_REVIEW` set R-182, discharged by `S8_ACCEPTED`) |
| **`S0_ACCEPTED_NESTED_REFERENCE_BENCHMARK`** | S0, the nested reference benchmark | **R-182** |
| **`ACCESS_ABILITY_ORDER_UNRESOLVED_UNDER_S8`** | the A/B ordering under S8 — **unresolved, not reversed** | **R-182** |
| **`NO_CROSS_MEASURE_QUANTITATIVE_ROBUSTNESS_CLAIM`** | W4/W6 against W1 — normative sensitivities only | **R-182** |
| **`NUTS2_EXTERNAL_OPPORTUNITY_IDENTIFICATION_AID`** + **`NOT_A_CAUSAL_INSTRUMENT`** | the BMO regional design | **R-182 §5** |
| **`CORSE_RETAINED_AS_OWN_NUTS2_CELL`** | Corse's 3 households and their own 2015 BMO NUTS-2 tension value | **R-182 §5(b)** |
| `LOC4_PREFERRED_STRUCTURAL_SPECIFICATION` | the preferred structural specification | R-157 |
| `BASELINE_ACCEPTED_NESTED_REFERENCE_SPECIFICATION` | the corrected common-dispersion model | R-157 |
| `T2A_PROFILE_ACCEPTED_WITH_COMPONENT_SIGN_QUALIFICATION` | T2-A `beta_w_pexp2` profile | R-161 |
| `LOC4_PROFILE_ACCEPTED` | the profile evidence | R-161 |
| `W1_MEAN_PROFILE_STABLE` | W1 mean over the profile region | R-161 |
| `A_GREATER_THAN_B_GREATER_THAN_P_PROFILE_STABLE` | component ordering | R-161 |
| `PHI_B_SIGN_UNRESOLVED_95_PROFILE` | `sgn(phi_B)` inside the 95% profile-LR region | R-161, re-affirmed **R-175** |
| **`LOC4_PREFERRED_MC_BANDED_LEVELS`** | the JMP-M08T2 closing verdict | **R-175** |
| **`MC_BANDED_LEVELS`** | the LOC4 W1 magnitudes | **R-175** |
| **`MC_BANDED_NORMALIZED_DIAGNOSTIC`** | `r_phi_P` and `r_R_bg` | **R-175** |
| `MC_BAND_ONLY_NONSMOOTH` | the W1 median | R-161, re-affirmed **R-175** |
| `T2B_RQMC_IMPLEMENTATION_ACCEPTED_PREPRICING` | the T2-B RQMC implementation and its pre-pricing gate | R-168 |
| `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` | the closed M08 prototype | R-138 §9 |
| `PROVISIONAL_NOT_PROMOTED_MC_PRECISION` | the 16x welfare functionals (baseline arm) | R-138 |
| `PARITY_AXIS_DISPOSITION_RETIRED_SUPERSEDED_BY_RENAME_AWARE_ALIAS_CLOSURE` | the old Stage-2 parity record | R-157 §9 |

**Superseded at R-175:** `RQMC_FINAL_PRECISION_PENDING` (set R-157 / R-161) —
the pass has run and is disposed of. The evaluation runner's mechanical
`PHI_B_POSITIVE_PROFILE_STABLE` output is superseded by
`PHI_B_SIGN_UNRESOLVED_95_PROFILE`.

**Withdrawn from the S8 claim set at R-182:**
`A_GREATER_THAN_B_GREATER_THAN_P_PROFILE_STABLE`. It stands **on the LOC4/S0 arm**
where it was set; it must **not** be carried into any S8 or successor claim.
Under S8 the A/B leg is unresolved, so the collective ordering disappears.
`PHI_B_SIGN_UNRESOLVED_95_PROFILE` is **untouched** — S8 carries an RQMC
numerical-integration band only, no profile envelope, and its positive numerical
`phi_B` level cannot be promoted into a sign statement.

**Primary claim region.** The conventional 95% profile-LR support region, with
the active-set/boundary caveat (R-161). The 90% region is a supplementary
sensitivity only.

**Pricing standing.** Eight-scramble RQMC pricing **has run** (R-175):
2,549,225 nodes in 5.2123 h of EUROMOD time against the 7 h guard; sealed
priced panel `b1879fcf2c210d337a4f4d3bfff93d06a6e044f8da1326f6ca3a5ab168d76f00`.
Both statistical t-bands remain deleted from the R3 pass path and are diagnostic
only. **No further numerical instrument is authorized on this benchmark.**

**Frozen at R-175, banded.** The eight manuscript-facing LOC4 quantities —
W1 mean `1339.0426 ± 2.1105`, W1 Gini `0.15114755 ± 0.0010869`,
`phi_A 0.00291492 ± 0.00039130`, `phi_B 0.00070562 ± 0.00065901`,
`phi_P −0.35279421 ± 0.00078335`, `R_bg 0.50032122 ± 0.00072355`,
`phi_A+phi_B 0.00362054 ± 0.00067681`, `s_opp 0.02395367 ± 0.0043248`. These are
numerical-integration bands, **never** confidence intervals.

**Still not claimable.** Cross-measure W4/W6 quantitative robustness; a
precision-certified `r_phi_P` or `r_R_bg`; any collective component-sign
statement; any combination of the RQMC band with the profile envelope; any
causal transfer/absorption language (R-157 claim-set conditions). The claim
boundaries of record are `JMP_M08_LOC4_manuscript_claim_set_v2.md`.

---

## 2. Missions — open and closed

| Mission | State | Closing / governing document |
|---|---|---|
| JMP-M05 — household-clustered inference, design | CLOSED | `JMP_M05_deputy_programme_acceptance_v1.md` |
| JMP-M05B — phase-5 implementation | CLOSED (paused, superseded by M05C) | `JMP_M05B_pause_and_M05C_redesign_decision_v1.md` |
| JMP-M05C — minimal streaming inference | CLOSED | `JMP_M05C_deputy_phase5_acceptance_v1.md` |
| JMP-M07 — inference/results integration | CLOSED | `JMP_M07_deputy_closeout_and_identity_ruling_v1.md` |
| JMP-M07I — manuscript identity alignment | CLOSED | `JMP_M07I_identity_alignment_acceptance_v1.md`, rider `JMP_M07I_manuscript_claim_rider_v1.md` |
| JMP-M08 — singles welfare decomposition | CLOSED as prototype under `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` | `JMP_M08_singles_welfare_decomposition_mission_charter_v1.md`; rulings R-129/R-131/R-138 |
| JMP-M08E — estimand correction / E2 closure | CLOSED | `JMP_M08E_E2_closure_notebook_and_RUM_ruling_v1.md` |
| JMP-HK-01 — housekeeping / archive | CLOSED | `HK01/` register set; MNL `192ef57`, JMP `9e15e56` |
| JMP-M08T2 — LOC4 boundary analysis and final numerical precision | **CLOSED at R-175**, verdict `LOC4_PREFERRED_MC_BANDED_LEVELS` | acceptance `JMP_M08_LOC4_preferred_spec_acceptance_v1.md`; claim set `JMP_M08_LOC4_manuscript_claim_set_v2.md`; charter `JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` |
| **JMP_PS1 — positive-specification sprint (S1..S8)** | **ESTIMATION PHASE CLOSED at R-183** — S8 accepted, verdict `S8_ACCEPTED`; the sprint continues only as the BMO exploratory leg | `Design/JMP_post_meeting_research_agenda_v1.md` §3–4, §12; MNL `experiments/JMP_PS1/decision_note.md` §11 |
| **JMP couples — joint household specification** | **ACTIVE** (opened R-182 §7, runs in parallel; inherits the accepted S8 architecture) | ruling R-182 §7; no charter (§9 four-file cap) |
| **`R1_BMO_NUTS2_OCCUPATION_TENSION`** — regional exploratory | **ACTIVE** (authorized R-182 §6, after S8 acceptance; does not block couples) | ruling R-182 §5–6; MNL `experiments/JMP_PS1/decision_note.md` §10, §11.5 |

### JMP-M08T2 — closed

| Stage | State |
|---|---|
| T2-A — `beta_w_pexp2` profile over its full legal interval | ACCEPTED (R-161), with `PHI_B_SIGN_UNRESOLVED_95_PROFILE` |
| T2-B — randomized QMC, part 1: node construction and gates G1..G9 | ACCEPTED PRE-PRICING (R-168) |
| T2-B — part 2: eight-scramble pricing | **RUN** — 2,549,225 nodes, 5.2123 h EUROMOD |
| Final RQMC precision / final-precision functional stage | **ACCEPTED BANDED (R-175)** — all seven W1 level gates PASS; the `normalized_contributions` family failed on 2 of 6 rows and is disposed of as `MC_BANDED_NORMALIZED_DIAGNOSTIC` |
| Charter §8 independent Tier-2 review (permanent output 4) | RETURNED — `LOC4_PREFERRED_MC_BANDED_LEVELS`; MNL `docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` |

**Two T2-A reporting corrections stand (R-175, review H1):** the convergence
reading is **29 constrained optimizations + 1 accepted unrestricted optimum**,
not 30; and the in-region count is **20 of 30**, not 30. Neither contaminates
the numerical record.

**Sprint boundary.** The M08T2 result is the final numerical record for the
**current LOC4 benchmark**. It is not automatically the final JMP structural
specification if JMP_PS1 selects an S8 successor.

### JMP_PS1 — estimation phase closed at R-183

Exploratory tier (R-172): no mission charter and no independent review for
S1..S7; a spec earns one bounded review only once it clears the agenda §3.2
candidate bar; full welfare and acceptance are reserved for S0 and the selected
S8. Battery part 1 accepted at R-174 with the **F-BOX** and **F-ACTIVE**
findings. PS1-C (fit suite), PS1-E (S0/S8 welfare) and PS1-F (official-data
audit) accepted at **R-179 / R-180 / R-181**. The deputy S8 ruling was adopted at
**R-182**; the lean S8 acceptance run (S8A) returned **NO PROFILE TRIGGER** and
its commissioned bounded independent review returned **`S8_ACCEPTED`** at
**R-183**, closing S8 autonomously under the ruling's §2/§9 branch.

| PS1 leg | State |
|---|---|
| S1..S7 | disposed of by R-182 §8 — S1 invariance-only, S2 not included, S4 rejected, S5 split rejected, S6 **equivocal, not admitted** (parked), S7 rejected |
| S8 = S0 + S3 | **ACCEPTED** — the preferred singles positive specification |
| S8 acceptance run (S8A) | negLL `18022.456443792806`; ΔAIC `−859.1961`; SINGLE-OPTIMUM over 10 polished points (spread `7.64e-10`); exact nesting to 0 ulp with Δ-gradient `−307.387`; PD full-rank clean Hessians (41-free and 39-interior); **W-4 set EMPTY**; **13/13** primary welfare rows pass on a bitwise-identical θ with no re-pricing |
| Bounded independent review | RETURNED — A1–A7 all ACCEPT; verdict **`S8_ACCEPTED`**; four refinements binding as claim language (R-184.1) |

**R-184.1 — binding claim language.** Recorded in full at MNL
`experiments/JMP_PS1/decision_note.md` §11.6. In short: S6 is *"equivocal, not
admitted"* (never "rejected"); S8 welfare **levels** are **conditional on the
inherited hours-normalizer convention** and are not convention-free final
magnitudes, with the MC-banded discipline continuing; `beta_h_f35` is an
*"institutionally motivated 35-hour opportunity peak"* of reduced-form
availability and **never** *"the effect of the 35-hour law"*; and `s_opp` is
*"robust to the S0→S8 change at the achieved RQMC precision"*, **not** statistical
invariance. Also hard: 13/13 numerical-precision passes do **not** validate
structural identification, and this review closes the **singles** positive
specification only. **CR1 convention, stated explicitly:** `K_interior = 39` is
PRIMARY (`c = 1.0257255936675462`); `K_free = 41` (`c = 1.0270805812417436`) is
the recorded alternative, inflating every robust SE by 0.066% and changing zero
significance verdicts. Both constants are in the acceptance manifest.

**T2-B R3 closure chain (settled).** Round-1 Codex review accepted R1, R2 and
R4–R9 and rejected R3 (R-164). One bounded correction cycle followed (R-165);
the round-2 re-review rejected R3 a second time on completeness and the matter
was returned to the deputy (R-166). The deputy E2 ruling authorized one final
exceptional bounded correction scoped to R3F-1..R3F-4 (R-167). The
commissioned fresh Codex read-only review returned R3F-1..R3F-4 all ACCEPT and
OVERALL ACCEPT (R-168), confirming mechanically that the generator is
unchanged, the node frames are byte-unchanged, the t-band remains absent and
there is no extra gate change.

---

## 3. Current priorities — verbatim from the PI standing direction

> CURRENT PRIORITIES
> 1. close T2-B and final RQMC;
> 2. run EXP_H35_PEAK_v1;
> 3. update the discussion notebook/report;
> 4. complete the paper outline and main tables;
> 5. only then decide which exploratory result enters the formal
>    accepted specification.

**Position on that list at R-183.** Item 1 is **DONE** (M08T2 closed at R-175).
Item 2 — `EXP_H35_PEAK_v1` — is **DONE**: it was the PS1 S3 leg, it was the
battery's only PROMOTE, and it is now the accepted S8's one added coordinate.
Item 3 is DONE for the R-175 pass; the notebook now owes an S8 pass. Item 5 —
"which exploratory result enters the formal accepted specification" — is
**ANSWERED for singles**: S8, at R-183. So the live order is:

> 1. **Couples** — data, joint proposal, ~100 joint household alternatives over
>    {neither works, man only, woman only, both work}, inheriting the accepted
>    S8 architecture (explicit 35-hour peak, LOC4 occupation-conditioned wage
>    location, selected preference specification). Begun in parallel now; does
>    not wait on manuscript rewriting;
> 2. **`R1_BMO_NUTS2_OCCUPATION_TENSION`** — the one exploratory regional
>    specification, one coefficient on `g^Occ` only, lagged 2015 BMO mapped
>    FAP → ISCO → `loc4` and standardized within `loc4`, formula frozen in the
>    decision note **before** results, no welfare unless later promoted. Does not
>    block couples;
> 3. update the discussion notebook/report to the S8 state;
> 4. complete the paper outline and main tables.

The full standing direction — including the exploratory-work licence, the
four-artifact retention limit per exploratory run, and the `EXP_H35_PEAK_v1`
specification — is recorded verbatim in the consolidated rulings document at
R-168, section *(2) PI Standing Direction — Practical Research Mode*.

**Return to the deputy only for a scientific decision, not routine
documentation or execution mechanics.**

---

## 4. Pointers — authorities of record

| Document | Path | sha256 |
|---|---|---|
| Consolidated rulings document (R-59 … R-183) | `docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | `9ff2a1f0e7c4e3647c7205aab71866a6f10c1f42bbd7891f56ec884444bb92d4` |
| JMP-M08T2 mission charter | `docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | `d4de2055ca5db8c6e3d3ea4c945b027ee0a80c0764ba4dc2c99d7d8154968d80` |
| **M08T2 acceptance (charter output 5)** | `docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` | `7a042b75bc535c2e72cd85daebc0521c7a23e44b26013b9c90d09770f87ff8f6` |
| **LOC4 manuscript claim set v2 — OPERATIVE (charter output 6)** | `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_v2.md` | `5a60ffdf3d0beefc006ba284af30009e0a3c99cf41a6f07a4506d7a1917e9ba6` |
| **Independent Tier-2 review (charter output 4)** | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | `06d2c0fc9cfd62ff1eb220e62cc34f660a739e0d594f079e47ed7307bab4b396` |
| RQMC final-precision results memo | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_rqmc_final_precision_results_v1.md` | `a456113473cebad748915ad1448134d891023951d05fb1be96ab1f6c914d90f7` |
| LOC4 preferred-spec packet index | `docs/Missions/JMP_M08_LOC4_preferred_spec_packet_index_v1.md` | `8fa35535bf4662d4f417580964de109225f5fff661a430d5316e681ee2d58017` |
| LOC4 manuscript claim set v1 — SUPERSEDED, history only | `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | `c9051c9df6ff3a0f901aaaeec44de76f93effddd3e68a9c7eecb31d132aea5e4` |

Paths are relative to the `Job_Market_paper` repository root except where marked
`MNL/`. The rulings-doc hash above is the post-R-175 value; it is the value the
live sha gates pin.

### 4.1 The rulings-doc pin recursion

Every append to the rulings document changes its sha256 and therefore stales
the live gates that pin it by hash. Under R-162 the re-pin of each dependent
site lands in the **same commit** as the append that stales it — an append
carries its own re-pins. Under **R-162.2** the sweep covers **both**
repositories, not the MNL executable gates alone. The dependent sites are:

**MNL — live executable gates (3):**

- `scripts/loc4/run_loc4_stage2_comparison.py` — `M6_RULINGS_SHA`
- `notebooks/france/fr_singles_results_discussion_v1.ipynb` — the `bind_evidence`
  pin in the §4(a) Monte-Carlo cell (`instrument_authority`)
- `notebooks/france/fr_singles_results_discussion_v1.ipynb` — the `bind_evidence`
  pin in the §8 welfare cell (`measure_disposition`)

**JMP — documentary pin tables (2):**

- `docs/Missions/JMP_current_state_dashboard_v1.md` — this file's §4 pointer table
- `docs/Missions/JMP_M08_LOC4_preferred_spec_acceptance_v1.md` — the `[rulings]`
  row of its source table (M08T2 charter output 5). Advancing that row is a
  **pin advance only**; the acceptance's findings and verdict are immutable and
  are not edited.

Re-pinning is **path-only**: the hash is advanced, and each binding cell's
claim strings are re-asserted under its own read of the new file. If a claim
string no longer appears, the append has moved text the gate depends on and
the re-pin must not be completed.

### 4.2 Evidence and code (MNL repository)

| Object | Path |
|---|---|
| T2-B RQMC modules, gates and tests (incl. part-2 rebind / price / stage / evaluate) | `scripts/rqmc/` |
| T2-B Codex review chain (rounds 1–3, incl. the R3-final ACCEPT) | `docs/France_case/P2a/FR_P2a_m08_rqmc_preflight_codex_review_v1.md` |
| T2-B part-2 evaluation record (the numbers R-175 was taken on) | `outputs/p2a_singles2016/region_live_margqh_v1/rqmc_t2b_v1/attempts/20260828T150001Z_…_t2beval_T2B_EVALUATE_PRIMARY_GATE_FAIL/rqmc_t2b_part2_evaluate_v1.json` |
| JMP_PS1 sprint instrument and decision note | `scripts/ps1/`, `experiments/JMP_PS1/decision_note.md` |
| **JMP_PS1 four permanent files (the §9 cap)** | `experiments/JMP_PS1/{specification_matrix.yaml, model_comparison.csv, post_estimation_comparison.html, decision_note.md}` |
| **S8 acceptance run (S8A) — the R-183 evidence** | `experiments/JMP_PS1/runs/ps1s8a_acceptance/` |
| **PS1-C / PS1-E / PS1-F run dirs** | `experiments/JMP_PS1/runs/{ps1c_fit_suite, ps1e_welfare_s8, ps1f_audit}/` |
| LOC4 Stage-2 comparison runner (carries `M6_RULINGS_SHA`) | `scripts/loc4/run_loc4_stage2_comparison.py` |
| Parity-path closure record of operative record | `docs/France_case/P2a/FR_P2a_m08_parity_path_closure_v1.md` |
| Results/discussion working notebook | `notebooks/france/fr_singles_results_discussion_v1.ipynb` |

**Package gitlink of record:** `dclaborsupply-monorepo` at `27756a06`. No
package main/gitlink change is licensed by any current status, including the
exploratory licence.

---

## 5. Pre-commit battery

Reproduced before and after every gated commit; read-only, seconds. Run from
`scripts/welfare` with the MNL project venv.

1. Gate self-pin: `m08_u6_pins_v2.open_gate(...)` over the expected pin set
   plus the U6 pin set — **76 pins** (52 + 24).
2. Re-hash every pinned key via `base_path` / `verified_path`.
3. `parity_axis_evidence("5b0e3d29e28126e1b3ee0340a243c09755da0b3b")`.
4. Assert the `dclaborsupply-monorepo` gitlink is still `27756a06`.

**R-179.1 — the battery is run in FULL, always.** All four steps and all 76 pins,
before **and** after every gated commit. **No scoped subset is licensed** by any
status, exploratory tier included; a scoped run is not a battery run.

**Commit trap.** Committing a *modification* to a file that did not exist at the
frozen axis still reads as `A` in the `frozen..HEAD` tree diff, so it is safe.
Check with `git cat-file -e 5b0e3d29…:<path>` before any commit that touches a
file that might predate the axis.

---

## 6. Next action

**Couples, priority 1 — and `R1_BMO` in parallel.** Begin couple data, the joint
proposal and the joint-alternative implementation now (R-182 §7), inheriting the
accepted S8 architecture. Run `R1_BMO_NUTS2_OCCUPATION_TENSION` as the single
exploratory regional specification (R-182 §6), with its three R-182 §5
constraints binding **before** estimation: Corse retained as its own NUTS-2 cell
with its own constructed 2015 BMO value plus one leave-Corse-out diagnostic —
**halt before estimation rather than impute** if that value cannot be built; the
raw missing-location flag recovered so the IDF BMO value is **not** assigned to
households recoded to `drgn2 = 1`, with the regional comparison estimated on
genuine observed-NUTS2 households only (restricted-sample S8, and restricted-
sample S8 + BMO) and the excluded count/share plus the genuine IDF count
reported; BTS/DADS kept to external validation or later auxiliary moments, and
employment-zone data not used at all because the merge is unavailable.

**Documentation discipline (R-182 §9).** The four-file permanent cap stands:
update only `specification_matrix.yaml`, `model_comparison.csv`,
`post_estimation_comparison.html` and `decision_note.md`. No new charter, profile
memo, regional memo, ordering memo or governance chain. Exploratory runs keep at
most their four-artifact sets.

**Nothing is owed on JMP-M08T2.** It is closed at R-175; no further numerical
instrument is authorized on the LOC4 benchmark. **Nothing is owed to the deputy on
S8** — R-183 closed it autonomously. Return only if a later step rejects S8, a new
W-4/boundary issue appears, or RQMC reuse fails.
