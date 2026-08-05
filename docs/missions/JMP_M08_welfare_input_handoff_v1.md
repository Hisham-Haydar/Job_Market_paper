# JMP-M08 Welfare Input Handoff v1 (FROZEN)

**From:** Goal 1 Manager — Empirical JMP (closing JMP-M07)  **Date:** 2026-08-05
**Status:** Frozen input contract for the welfare mission. Changes require a deputy-approved revision register.
**Target repository path:** `docs/missions/JMP_M08_welfare_input_handoff_v1.md`

## 1. Accepted inputs (the only permissible parameter and inference sources)

| Object | Anchor |
| --- | --- |
| Parameter vector θ̂ (47 = 35 interior + 10 pins + 2 active upper bounds) | accepted Phase-3 artifacts at MNL `520441a6…`; theta bytes `c024b893…f0580d` |
| Inference objects (V_model, V35 robust, c = 1555/1520, CR0-recoverable) | accepted Phase-5 attempt `20260803T133122Z_…`, bundle `d08947ce…` |
| Reporting artifacts | extraction memo `b800d0e3…`; reporting map `89a0465c…` |
| Manuscript inference backbone | `FR_P2a_empirical_inference_v2.md`, `FR_P2a_inference_appendix_note_v2.md` (accepted M07) |
| Model/spec | certified 47-parameter pooled spec at numerical anchor `982c5221…`; package gitlink `27756a06…` (frozen) |

No welfare computation may source any number from management memos (per R-57/A-5); the strategic assessment is context, never data.

## 2. Binding obligations carried into the welfare mission

1. **S-10 Tier-1 four-scenario sensitivity (mandatory, exact):** implement `JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md` verbatim — the accepted baseline vector plus the specified scenario vectors for the two W-4 coordinates (`beta_l0_sm`, `beta_w_pexp2`); no re-estimation; the perturbations Δⱼ and sensitivity vectors θ^sens_j are recorded by the welfare mission **before** execution; all headline welfare/inequality outputs reported under all four scenarios with the convergence/invariance diagnostics.
2. **Tier-2 trigger (pre-registered):** boundary-aware or resampling inference becomes mandatory if a direct inferential claim is made about a flagged coordinate, if any welfare or decomposition functional loads materially on one, or if an unconditional active-set claim is made. Material loading is assessed and documented in the welfare mission's first gate.
3. **LOC4 (Path-B ruling, binding):** baseline welfare proceeds on the certified model; the four-density LOC4 variant (mean-and/or-dispersion formulation per the ruling, no double counting) is **mandatory before final quantitative decomposition claims** — pre-registered as the first robustness axis, not a prerequisite for the first prototype.
4. **W-4 visibility:** the two flagged coordinates remain visible in every welfare and decomposition output and caveat block.
5. **Vigilance item (R-57/A-9):** `beta_l0_sf`'s robust CI lower endpoint (`0.05467`) sits adjacent to the recorded `0.05`-class bound of its male counterpart; its own bound is not carried in accepted artifacts. The welfare mission's material-loading assessment monitors `beta_l0_sf` alongside the two flagged coordinates; nothing is asserted in paper text absent an accepted bound record.
6. **Scope:** singles P2a only (A-2 ratified resolution); no couples, pooled years, EUROMOD reruns, or estimation of any kind; the normative framework (W¹–W⁶ family) remains the separate theory paper's — the welfare mission implements the JMP's money-metric decomposition per its own charter, to be issued by the deputy.

## 3. Open strategic item traveling with this handoff

The manuscript-identity inconsistency (acceptance memo §3) is with the deputy; the welfare mission may proceed on singles scope regardless of the framing decision.
