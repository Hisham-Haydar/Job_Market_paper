# JMP-M07 Stage-B Author Cover Note v1

**Mission:** JMP-M07 — Phase-5 Inference Results Integration
**Stage:** B (economics drafting)
**Author role:** Stage-B economics author (Claude Project chat, Opus, thinking on, high effort)
**Status of this document:** Reconstructed from the Stage-B author's session record
under Goal-1 ruling R-56. It records the Stage-B return as it was made, before the
Stage-C review was received.

---

## 1. Stage-B verdict

**Delivered complete; submitted for independent economics review.**

Stage B does not certify its own output. The author's self-assessment at return
was: both required Stage-B deliverables were produced in full against charter
sections 3–8; every reported numeral was traced to an accepted artifact; no
blocking evidence gap was encountered; and nine specification ambiguities were
referred upward for Goal-1 ruling rather than resolved silently. The binding
verdict on the deliverables is Stage C's.

---

## 2. Authoritative inputs used

Numerical sources (the only two permitted, and the only two used):

1. `FR_P2a_phase5_inference_results_memo_v1.md` — the Stage-A accepted-result
   extraction memo.
2. `FR_P2a_phase5_parameter_reporting_map_v1.csv` — the 47-row parameter
   reporting map (SHA-256 `89a0465cc55f4bc05898559120591e4c28db15a18992bd2b33ba6538ce7b8481`).

Governing and framing documents (no numerals drawn from them):

3. `JMP_M07_inference_results_integration_mission_charter_v1.md`
4. `JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md`
5. `JMP_M05C_W4_routing_memo_v1.md`
6. `JMP_LOC4_pathB_ruling_v1.md`
7. `JMP_core_packet_v1.md`, `JMP_abstract_clean_v1.md`,
   `JMP_extended_abstract_clean_v1.md`, `JMP_intro_skeleton_v1.md`,
   `JMP_topic_lock_v1.md` — register and paper-identity consistency only.
8. `JMP_goal1_phase5_strategic_assessment_v1.md` — read, but deliberately **not**
   used as a numerical source (see item A-5 below).

---

## 3. Files created

| File | Words | Charter output |
|---|---:|---|
| `manuscript/sections/FR_P2a_empirical_inference_v1.md` | 4,066 | §8 output 3 |
| `manuscript/appendices/FR_P2a_inference_appendix_note_v1.md` | 2,824 | §8 output 4 |

No other file was created, and no existing file was modified. Charter outputs
1–2 were produced at Stage A; outputs 5–6 are Stage-D goal-manager outputs and
were not attempted.

---

## 4. Confirmations

- **No statistic was recomputed.** Every estimate, standard error, confidence
  interval, Wald statistic, p-value, count, hash and diagnostic value in the two
  deliverables was copied from the extraction memo or the parameter reporting
  map. The only transformations applied were declared display renderings
  (decimal rounding, significant-figure rendering, and typographic rendering of
  labels), each of which is documented in the appendix's rendering-conventions
  section.
- **No estimation, inference, welfare, decomposition, or LOC4 execution
  occurred.** No model was run, no covariance object was rebuilt, no test was
  re-derived, no microdata was accessed, and no repository was written to. The
  work was text authorship only.
- **No item recorded as unavailable was filled by inference.** Omitted and
  reference categories, per-coordinate z-statistics and p-values, the numerical
  KKT multipliers, the bounds of coordinates other than the two `W-4`
  coordinates, and the numerical S-10 perturbations were all left unstated and
  were listed explicitly as not carried.
- **No numbers were taken from the strategic assessment**, including the
  `1.14%` standard-error inflation figure, the per-parameter z-statistics, the
  robust-to-model standard-error ratios, and the KKT multiplier magnitudes.

---

## 5. Drafting and source discrepancies encountered

Five discrepancies or judgement points arose during drafting and were recorded
rather than absorbed.

**D-1 — H0-G robust p-value, dual source route (the "A-4" item).** The
extraction memo carries the H0-G robust p-value at two renderings differing in
the sixteenth significant figure: `6.500461827702641e-08` in the §2 claim text
and `6.500461827702638e-08` in the §2 table. The Stage-B author used the
charter's paper-facing rendering `6.5e-08` throughout, disclosed the divergence
in the appendix, and — at the time of return — asked whether the extraction memo
should be corrected. *Subsequent disposition, recorded here for completeness:*
Stage C adjudicated this under R-55c as a harmless dual source route rather than
an error. In the v2 deliverables the full-precision appendix table carries the
table-route value, the claim-route value is recorded as a source-route note, the
prose retains `6.5e-08`, and **no correction to any source artifact is
requested anywhere**.

**D-2 — Transcription error caught in draft.** The H0-G robust Wald statistic
was mis-transcribed as `29.208167292116638` in an intermediate draft of the
appendix and was corrected to the source value `29.208167292116848` before
return. No other transcription error was found on self-audit.

**D-3 — Rendering of `beta_occ_4_f`.** The full-precision estimate is
`0.85450203950514481`, which renders as `0.855` at three decimals under
round-half-away-from-zero. The strategic assessment quotes the truncated
`0.854`. The reporting map was treated as authoritative and the divergence was
documented.

**D-4 — Rendering of the pinned coordinate `beta_l0_m`.** The full-precision
value is `9.9999999999999995e-07`, which would render as `0.000` at three
decimals. It was rendered as `0.000001` so that a pinned non-zero value is not
displayed as an exact zero.

**D-5 — Sign-pattern correction in draft.** An intermediate draft described the
male and female occupation-access coefficients as differing in sign pattern.
Checked against the reporting map, they share the pattern (−, −, +) and differ
in magnitude; the sentence was corrected before return.

---

## 6. The ambiguity register as issued — truthful statement

The instruction to this reconstruction offered the alternative that "A-4's
numbering was an artifact and it was the sole flagged item." **That is not what
happened, and the author does not adopt it.** The Stage-B return carried a
register of **nine** items, numbered A-1 through A-9, of which the H0-G item was
the fourth. A-1 through A-3 were substantive items in their own right and are
stated here in full.

- **A-1 — Table schema width.** The Stage-B brief specified a "13-column
  reporting schema as the memo renders it." The delivered reporting map carries
  **12** columns, and charter §5 enumerates nine reporting items. The author
  rendered eight display columns, collapsing the two confidence-interval
  endpoints into a single bracketed column and moving bound-side and pin-reason
  into the status cell and panel footnotes. Ruling requested on whether a
  thirteenth column was intended.
- **A-2 — Sample unit conflict (material).** The charter, the governance state
  and every Phase-5 artifact are France 2016 **singles** P2a. The core packet,
  the clean abstract, the extended abstract and the intro skeleton all describe
  a **couples** baseline, and the core packet explicitly instructs that
  "singles prototype" language is obsolete. The author resolved in favour of the
  charter under the project's precedence rule and flagged that the abstract,
  extended abstract, core packet and intro skeleton are now inconsistent with
  the results section.
- **A-3 — Display precision not fixed.** The charter and memo quote headline
  figures at mixed precision. The author adopted three decimals in tables with
  memo/charter renderings reproduced in prose, and flagged D-3 as the visible
  consequence.
- **A-4 — H0-G sixteenth-digit divergence.** As set out in D-1.
- **A-5 — Non-extracted management figures.** The `1.14%` inflation figure,
  per-parameter z-statistics, robust/model ratios and KKT multiplier magnitudes
  appear only in the strategic assessment. Treated as not extracted; precision
  expressed through robust confidence intervals only. Ruling requested on
  whether the strategic assessment may be cited as a paper-facing numerical
  source.
- **A-6 — Table placement.** Charter §5 permits a "47-row paper table *or*
  table-ready source." The author placed the full table in the body and the
  technical apparatus in the appendix.
- **A-7 — Pinned rows in the body table.** Ten pinned coordinates carry no
  inference; charter §5 says "47-row," so all appear, with pin reasons.
  Confirmation requested.
- **A-8 — Zero-rendering of `beta_l0_m`.** As set out in D-4.
- **A-9 — Possible reviewer question, not resolved.** The reporting map shows
  `beta_l0_sf` with robust CI lower endpoint `0.05467`, adjacent to the value
  `0.05` recorded as the lower bound for `beta_l0_sm`. The accepted `W-4` gate
  flags only two coordinates; the author did not extend the flag list, and the
  bound for `beta_l0_sf` is not carried in the accepted artifacts. Ruling
  requested on whether an explanatory footnote is wanted.

---

## 7. Unresolved items passed to Stage C

All nine register items A-1 through A-9 were passed forward unresolved, together
with the five drafting discrepancies D-1 through D-5. Stage C adjudicated A-4
under R-55c and A-5 under R-55b, both upheld on the merits. A-1, A-2, A-3, A-6,
A-7, A-8 and A-9 remain matters for the Goal 1 Manager; **A-2 in particular is a
paper-identity question that reaches beyond M07**, since the abstract, extended
abstract, core packet and intro skeleton describe a couples baseline that the
accepted evidence does not support.

---

## 8. Immediate next action

At the time of this return: Stage C independent economics review of the two
deliverables, restricted to claim-to-evidence alignment, the GSUR-concentration
interpretation, the regional-channel-versus-whole-mechanism distinction,
conditional-active-set wording, `W-4` disclosure, and the absence of causal or
responsibility overclaims.

*Subsequent state:* Stage C returned PASS WITH REQUIRED CORRECTIONS with ten
written-claim corrections. Those ten have been applied under Goal-1 ruling R-56
in `FR_P2a_empirical_inference_v2.md` and
`FR_P2a_inference_appendix_note_v2.md`, which supersede the v1 files; the v1
files remain immutable history. The next authorised action is Stage-D goal-manager
acceptance, which also produces the M07 acceptance memo and the M08
welfare-input handoff.
