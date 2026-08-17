# JMP-M08 Stage-A Freeze Record (v1)

**Programme:** Goal 1 — Empirical JMP
**Document class:** Manager governance record — deputy-transcribed. Records a
ratification issued by the Goal 1 Manager; creates no new authority beyond
that ratification and amends no contract text in place.
**Created:** 2026-08-17, during the JMP-M08 Stage-A freeze commit pass
(documentation-only: no computation, no welfare number, no MNL write, no
code change).
**Purpose:** to record, verbatim, the Goal-1 ratification that discharges the
sole remaining freeze condition at
`JMP_M08_singles_welfare_execution_contract_v5.md` §8.4 condition 3, and to
declare the resulting frozen state of the Stage-A execution contract.

---

## (a) The R-87 ratifications — verbatim, as supplied by the Goal 1 Manager

> V6/V22 materiality = min{0.05, 0.5*(1-f_baseline)} per coalition on the
> flagged fraction, disjunctive halt with the frozen 0.5-nat V_i^dir
> cross-check; U6 = median adjacent-step drift <= 0.05 nats per group
> (1x->2x, 2x->4x), max/p95 reported not gated, Branch A/B failure actions
> per contract s5A.8.3; welfare_stage1_w3.yaml:32 tolerance VOID (dead,
> dimensionally wrong, must not be read by any Stage-D config); S-10 spec
> digest acbf1637...19db adopted as its binding pin; U3
> CLOSED-BY-RULING R-64.5; s6.2 deliverable-name staleness cosmetic and
> non-gating.

**Cross-reference, for auditability (transcription only — not part of the
ratification text above):**

- **V6/V22 materiality and the disjunctive halt** ratify, without
  modification, the implementer's Stage-A proposal at contract §5A.8.3.2 —
  `Δf_material = min{0.05, ½·(1 − f_∅)}`, evaluated per coalition on
  `Δf_S = f_S − f_∅`, with the halt firing on either `Δf_S ≥ Δf_material`
  for any coalition, or persistent `V_i^dir`/`V_i^IS` disagreement beyond the
  frozen 0.5-nat tolerance (I-4; U7; R-60/R-71/R-78).
- **U6** ratifies, without modification, the implementer's Stage-A proposal
  at contract §5A.8.3.3 — the gate statistic is the median of
  `d_i^(m→2m) = |V_i^IS(2m·draws) − V_i^IS(m·draws)|` per household, per
  group, per adjacent multiplier step (`1→2`, `2→4`), tolerance `0.05` nats;
  the maximum and p95 are reported but not gated; Branch A (datasets built:
  fail ⇒ halt and escalate) and Branch B (datasets not built: Gate 1(i)
  carried forward BLOCKED, disclosed, every welfare number reported
  draw-growth-unverified) apply exactly as stated at §5A.8.3.3.
- **`welfare_stage1_w3.yaml:32`** — `MNL scripts/welfare/configs/
  welfare_stage1_w3.yaml`, the `tolerance: 1.0e-6` key inside the
  `per_household_stability` block (lines 29–32). Contract §5A.8.3.3 records
  it as dead code (`run_stage1_w3.py`/`run_stage2_vdir.py` read
  `draw_multipliers` only, never `tolerance`) and dimensionally wrong (a
  euro-valued reprice-parity tolerance, not a nats-valued draw-growth
  tolerance). This ratification voids it outright rather than routing it
  into the Stage-D disposition contract §5A.8.3.3 left conditional on
  ratification.
- **The S-10 spec digest** — `acbf163740b8ae97ed59bf2734fc029f1fb42b1d7e88bf7f05a46d78675b19db`,
  recomputed on disk for this pass against
  `docs/design_notes/JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md`
  (142 lines; relocated to `docs/Missions/` by Step 2 of this same pass) —
  **exact match**. Adopted as the file's binding pin, closing the gap U10.2
  recorded (the spec was not digest-bound at U1).
- **U3 CLOSED-BY-RULING R-64.5** — resolves the standing tension between
  R-64's and R-70's recitals ("U3 closed") and R-78's and contract §8.4.0b's
  more recent status ("U3 stays ESCALATED-NO-REFERENT" / "documentary;
  neither gates a number"). This ratification is the written R-64.5 text;
  U3 is now CLOSED and carries no further open action.
- **s6.2 deliverable-name staleness** — contract v5 §6.2 item 1 still names
  the deliverable as `JMP_M08_singles_welfare_execution_contract_v2.md
  (this file, once frozen)`, unchanged since v2. With the contract now at
  v5, that filename is stale. Ratified as cosmetic and non-gating: the
  deliverable is the frozen contract of record, whatever its version
  number, and no correction cycle is required on this account.

---

## (b) Declaration — the frozen Stage-A execution contract

**`JMP_M08_singles_welfare_execution_contract_v5.md`**
(sha256 `c7b0338f71af2fb31c4ce20e99691713e53a8e4bd1e31d01c493432799f15005`)
**+ this record together constitute the FROZEN Stage-A execution contract.**

Contract §8.4 enumerated exactly three freeze conditions. Conditions 1
(v4-ACCEPT) and 2 (Stage-A economics review) were already DISCHARGED at v5
(§8.4.0, §8.4.0a). Condition 3 — Goal-1 ratification of the V6/V22
materiality number and the U6 draw-growth decision, proposed without
ratification at §5A.8.3 — is discharged by ratification (a) above.

**The §8.4 execution block is DISCHARGED.** All three conditions are now
met. **Stage-D welfare execution is authorized under the frozen contract.**
No further Stage-A instrument is required to begin Stage-D work; Stage-D
execution remains bound by every other frozen value, gate, and disclosure
rule the contract already carries unchanged (ESS 30, 0.5 nats, `ε_Shapley`,
the D15 formula, the U4 subgroup dimensions, `dwt = db090`, the halt
conditions, etc.).

---

## (c) Freeze inventory

- **Parity axis:** FROZEN at MNL HEAD
  `5b0e3d29e28126e1b3ee0340a243c09755da0b3b` (verified as this repository's
  current HEAD for this pass; R-77, R-79).
- **Report of record:** MNL `docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4.md`
  + its acceptance note `FR_P2a_m08_parity_gate_report_v4_acceptance.md`
  (contract §8.4.0).
- **Stage-A review:** CLOSED — all items confirmed (R-86.1; contract
  §8.4.0a). Review memo of record:
  `docs/Missions/JMP_M08_stageA_contract_review_v1.md`
  (sha256 `4733876f3a6e8ca499e93c732bea3e847939bf4907c676c974bb184fde838f11`).
- **Measure bindings:** per contract §3.1c — the six W1–W6 definition
  extractions, the fidelity map, the U13 `R^h` citation binding, O-1 Option A
  (R-85, PI decision), O-3 (R-86), O-8, O-9, and the O-2/O-4/O-5/O-6/O-7
  PI-owned theory-source items, all as transcribed at §3.1c.1–§3.1c.9.
- **U10:** RESOLVED (contract §3.2a(U10); the six S-10 §3 quantities per
  coordinate and the four scenario vectors, each cited to file + line).
- **Every remaining PROPOSED item is now FROZEN or VOID:** V6/V22
  materiality — FROZEN (ratification (a) above). U6 draw-growth tolerance —
  FROZEN (ratification (a) above). `welfare_stage1_w3.yaml:32`
  `tolerance` key — VOID (ratification (a) above). S-10 spec digest binding
  — FROZEN (ratification (a) above). U3 — CLOSED (ratification (a) above).
  s6.2 deliverable-name staleness — disposed of as cosmetic/non-gating
  (ratification (a) above). No item within the Goal-1 rulings register or
  the contract's own tracking tables remains in a PROPOSED,
  PROPOSED-PENDING-GOAL1-RATIFICATION, or ESCALATED state after this record.

---

**Statement:** no welfare number, decomposition number, parameter value, or
re-estimation is produced or implied by this record. No computation was
performed to produce it. This record accompanies a documentation-only
commit; no MNL file is written or modified.
