<!-- GOVERNANCE DOCUMENT — CURRENT-STATE SURFACE -->

# JMP Current-State Dashboard v1

**Programme:** Goal 1 — Empirical JMP
**Last updated:** 2026-08-28, at Goal-1 R-168.
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
| `LOC4_PREFERRED_STRUCTURAL_SPECIFICATION` | the preferred structural specification | R-157 |
| `BASELINE_ACCEPTED_NESTED_REFERENCE_SPECIFICATION` | the corrected common-dispersion model | R-157 |
| `T2A_PROFILE_ACCEPTED_WITH_COMPONENT_SIGN_QUALIFICATION` | T2-A `beta_w_pexp2` profile | R-161 |
| `LOC4_PROFILE_ACCEPTED` | the profile evidence | R-161 |
| `W1_MEAN_PROFILE_STABLE` | W1 mean over the profile region | R-161 |
| `A_GREATER_THAN_B_GREATER_THAN_P_PROFILE_STABLE` | component ordering | R-161 |
| `PHI_B_SIGN_UNRESOLVED_95_PROFILE` | `sgn(phi_B)` inside the 95% profile-LR region | R-161 |
| `RQMC_FINAL_PRECISION_PENDING` | final numerical precision | R-157 / R-161 |
| `T2B_RQMC_IMPLEMENTATION_ACCEPTED_PREPRICING` | the T2-B RQMC implementation and its pre-pricing gate | **R-168** |
| `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION` | the closed M08 prototype | R-138 §9 |
| `PROVISIONAL_NOT_PROMOTED_MC_PRECISION` | the 16x welfare functionals | R-138 |
| `PARITY_AXIS_DISPOSITION_RETIRED_SUPERSEDED_BY_RENAME_AWARE_ALIAS_CLOSURE` | the old Stage-2 parity record | R-157 §9 |

**Primary claim region.** The conventional 95% profile-LR support region, with
the active-set/boundary caveat (R-161). The 90% region is a supplementary
sensitivity only.

**Pricing standing.** Eight-scramble RQMC pricing is **authorized** at R-168
under the unchanged 5.02h projection and the 7h guard. It has **not been run**
as of this update. Both statistical t-bands remain deleted from the R3 pass
path and are diagnostic only.

**Not yet frozen.** Exact preferred-arm W1/W4/W6 levels; `s_opp` for the LOC4
arm. No quantitative-robustness claim and no causal transfer/absorption
language is licensed (R-157 claim-set conditions).

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
| **JMP-M08T2 — LOC4 boundary analysis and final numerical precision** | **OPEN** | `JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` |

### JMP-M08T2 — the one open mission

| Stage | State |
|---|---|
| T2-A — `beta_w_pexp2` profile over its full legal interval | ACCEPTED (R-161), with `PHI_B_SIGN_UNRESOLVED_95_PROFILE` |
| T2-B — randomized QMC, part 1: node construction and gates G1..G9 | **ACCEPTED PRE-PRICING (R-168)** |
| T2-B — part 2: eight-scramble pricing | AUTHORIZED, NOT RUN |
| Final RQMC precision / final-precision functional stage | PENDING |

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
| Consolidated rulings document (R-59 … R-168) | `docs/Missions/JMP_M08_goal1_rulings_document_v4.md` | `f29b97a0a4ccc02e1fa56ffdb3349d5b7ac1f49f9ac01b6424d220037264b5c5` |
| JMP-M08T2 mission charter | `docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | `d4de2055ca5db8c6e3d3ea4c945b027ee0a80c0764ba4dc2c99d7d8154968d80` |
| LOC4 preferred-spec packet index | `docs/Missions/JMP_M08_LOC4_preferred_spec_packet_index_v1.md` | `8fa35535bf4662d4f417580964de109225f5fff661a430d5316e681ee2d58017` |
| LOC4 manuscript claim set (operative LOC4 branch, ratified R-157) | `docs/Missions/JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` | `c9051c9df6ff3a0f901aaaeec44de76f93effddd3e68a9c7eecb31d132aea5e4` |

Paths are relative to the `Job_Market_paper` repository root. The rulings-doc
hash above is the post-R-168 value; it is the value the live sha gates pin.

### 4.1 The rulings-doc pin recursion

Every append to the rulings document changes its sha256 and therefore stales
the live gates that pin it by hash. Under R-162 the re-pin of each dependent
site lands in the **same commit** as the append that stales it — an append
carries its own re-pins. The dependent sites, all in the MNL repository, are:

- `scripts/loc4/run_loc4_stage2_comparison.py` — `M6_RULINGS_SHA`
- `notebooks/france/fr_singles_results_discussion_v1.ipynb` — the `bind_evidence`
  pin in the §4(a) Monte-Carlo cell (`instrument_authority`)
- `notebooks/france/fr_singles_results_discussion_v1.ipynb` — the `bind_evidence`
  pin in the §8 welfare cell (`measure_disposition`)

Re-pinning is **path-only**: the hash is advanced, and each binding cell's
claim strings are re-asserted under its own read of the new file. If a claim
string no longer appears, the append has moved text the gate depends on and
the re-pin must not be completed.

### 4.2 Evidence and code (MNL repository)

| Object | Path |
|---|---|
| T2-B RQMC modules, gates and tests | `scripts/rqmc/` |
| T2-B Codex review chain (rounds 1–3, incl. the R3-final ACCEPT) | `docs/France_case/P2a/FR_P2a_m08_rqmc_preflight_codex_review_v1.md` |
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

---

## 6. Next action

`EXP_H35_PEAK_v1` on the preferred LOC4 model, under the exploratory licence
of the PI standing direction — separate experiment directory, labelled
provisional, no package/gitlink change, no EUROMOD, welfare integration,
decomposition or independent review, and at most four permanently retained
artifacts. Eight-scramble RQMC pricing is independently authorized and may
proceed under the 7h guard.
