# JMP-M08 Singles Welfare Execution Contract v2 (DRAFT — UNCOMMITTED)

**Supersession.** This document **supersedes
`docs/Missions/JMP_M08_singles_welfare_execution_contract_v1.md`**. **v1 remains
on disk, unchanged, as immutable history.** v2 is the contract of record for
Stage A. The only substantive change from v1 is the incorporation of the Deputy
Programme Director's binding ruling

> `Job_Market_paper docs/Missions/JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md`
> sha256 `0d40802c8585b04d3743c4818faa7c4fbbdfecd7fb252bcfe81c395de1f85749`
> (Deputy Programme Director, 2026-08-07, Binding)

— hereafter **"the decomposition-architecture ruling"** — applied per its §4
items 1–10, together with the consequential consistency and housekeeping pass
those amendments force. **No welfare computation, no code change, no data
change, no MNL write, and no commit accompany this document.** Stage A still
owns the freeze.

**Status:** DRAFT produced by M08 Stage 0 → Stage-A preparation (Claude Code,
documentation-only). Not reviewed by Stage A (independent contract/economics
review, Opus). Not frozen. **Do not execute against this draft.**

**Revision lineage (all documentation-only):** finalised under Goal-1 **R-59**
(four full digests; on-disk resolution of the §3.2 register) → **U4 deputy
ruling** incorporated as §6.3–§6.7 → **R-64** carry-forwards recorded as §2.1 →
**R-70.2** digest byte-fix → **R-71 / R-72** ratification of the U12 and R9
design memos, transcribed at §5A → **this v2**, under the
decomposition-architecture ruling.

**What v2 changes, in one paragraph.** `W3` is removed as the primary
source-decomposition anchor and retained as a **validation-only** measure (first
welfare-engine validation; laissez-faire/full-responsibility endpoint in the
welfare-family comparison; reference-recovery and inversion diagnostic). The
**primary source decomposition is `W2`**; the **secondary is `W5`**. The
grand-coalition-zero requirement is withdrawn and replaced by **exact residual
accounting** with a named fixed-background residual `R_bg^k = I^k({A,B,P})`, five
revised validation gates, and headline shares including the S-10 opportunity
share `s_opp`. The three-channel `{A,B,P}` game is retained and **no fourth
channel is authorized**. Two items that v1 recorded as UNRESOLVED and
execution-blocking — **R8** (`W^3` own-set degeneracy) and **S6** (`c_ij`
grand-coalition residual) — are **RESOLVED-BY-DEPUTY-RULING**. Access, ability
and preference **operator definitions at §5A are otherwise unchanged**
(ruling §4.10).

**Produced against:**
- `Job_Market_paper` **`f6a113089e72af6633a57212cf12124b7d6fbba7`** (`f6a1130`,
  *"docs(jmp): commit M07I immutable history set; place deputy closeout ruling at
  canonical path"*) — **rebound in this revision from v1's
  `7d29a1f4d03e7be5402b1ed1890242c5f390d6eb`**. Twelve files remain deliberately
  untracked at this HEAD, including this contract, its v1 predecessor, and the
  decomposition-architecture ruling.
- MNL `520441a653f04196bf1e92e3658a478b4feb3718` — **no tracked modification**;
  13 untracked entries, all M08 parity/welfare artifacts listed in §2.1.
- `dclaborsupply-monorepo` `27756a06ea189339aa82915ed2124628afed20eb` — **pin
  carried forward from v1 and not re-verified in this pass**; the repository is
  not on this session's reachable path list. Stage A must re-verify the pin at
  freeze.

**Governing documents (per charter §2, in order), with the ruling inserted at
its own scope:**
`JMP_M08_final_E2_literature_and_decomposition_architecture_ruling_v1.md`
(**binding, and governing over every decomposition-architecture statement in this
contract**) →
`JMP_M07_deputy_closeout_and_identity_ruling_v1.md` →
`JMP_M08_welfare_input_handoff_v1.md` →
`JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md` →
`JMP_LOC4_pathB_ruling_v1.md` → accepted P2a manifests → `JMP_welfare_spec_v5.md`
(only version on disk; `JMP_welfare_spec_latest.md` named in the charter does not
exist as a file — v5 is the highest-numbered spec and is treated as "latest") →
`RURO_welfare_scaffold_design_contract_v2.md`.

**Ordering rule for this file.** Where a transcription in §5A and the
decomposition-architecture ruling could diverge, **the ruling governs**. Where a
transcription in §5A and its source design memo could diverge, the memo governs.
Where the U4 subgroup ruling and the decomposition-architecture ruling touch the
same reporting slot, the later decomposition-architecture ruling governs the
*measure*; the U4 ruling continues to govern the *dimensions, statistics and
disclosure*.

---

## 0. Reading order and the halt this draft imposes on itself

This draft is sequenced exactly as the charter's stages require. **Section 1
(parity diagnosis) must close — diagnosis memo accepted by the Goal 1
Manager — before Section 2 (parity correction) starts, and Section 2 must pass
its gate before Section 4 (execution) starts.** Sections are numbered in
execution order, not charter-section order.

---

## 1. Parity diagnosis — FIRST, no code change until accepted

### 1.1 What must be reproduced

Stage B's first action (charter §7 Stage B, step 1) is: *"reproduce the
documented P2a singles reprice-parity failure on accepted existing nodes."*
The documented failure is fully transcribed below (verbatim extraction from
Stage 0's inventory, §3 of the accompanying report). Stage B opens by rerunning
`scripts/welfare/run_stage2_parity.py` against the same 2016-singles smoke
(5 households, ≤20 rows each) and confirming the **same** 8/100-row failure
signature before touching any code.

### 1.2 The documented failure (verbatim, from `RURO_welfare_stage2_parity_v1.md`, MNL)

> Parity **FAILS on every production year×mode cell**, with a single,
> consistent **STRUCTURAL** root cause now identified: the divergence is
> **localised entirely to `ils_ben` (benefits) on benefit-recipient
> households**. Original income (`ils_origy`) and social contributions
> (`ils_sicdy`) reproduce to **machine zero**. **No reprice-path repair is
> justified** by the diagnosis... so **node pricing stays BLOCKED** and no
> production `V_i^dir` is computed.

2016-singles cell numbers (the cell M08 needs): 100 rows / 5 households, 8
rows exceed tolerance, `ils_dispy` max abs diff **422.35**, median **0.00**,
`ils_ben` max abs diff **422.35**, `ils_origy` max abs diff **0.00**. Parity
tolerance (`scripts/welfare/configs/welfare_stage1_w3.yaml`, `stage2.parity_grid.
parity_tol`): **1.0e-6** (euros, absolute). All 8 failing rows are benefit
recipients; the 92 passing rows have zero benefit divergence. Ruled out (each
explicitly tested, not assumed): ID collision, dropped household roster,
input-column feedback, EUROMOD non-determinism, and an omitted
build-faithful-path preprocessing step (the build-faithful path was tested and
is *worse*).

**Suspected cause, as stated by the report itself:** *"the stored `ils_ben`
encodes household/annual state (means-test bases, prior-period or uprated
benefit inputs) that the per-draw stamped row does not carry, and that the
build established at original pricing time in a way the bounded reprice cannot
reconstruct from the row alone."* A follow-up read-only inspection
(`RURO_welfare_stage2_benefit_state_recoverability_v1.md`, same date) tested
whether this state is recoverable through bounded joins/plumbing and found
**NOT FEASIBLE**: `ils_ben` is EUROMOD-simulated, node-dependent output that
does not reconstruct from stored standardized subtotals. Its verdict: exact
redrawn-node benefits require a **separately authorised per-node EUROMOD
pricing path with full parity gates** — not a reconstruction of stored state.

All six year×mode cells fail identically (2015/2016/2017 × singles/couples);
this is systematic, not a 2016-singles artifact. Every subsequent stage-2
increment on disk (chunk-writeback fix, full-rebuild validation, singles
`V_i^dir` gate) also STOPs/FAILs — the gap was never closed after 2026-06-03,
and the charter treats it as still open by making its reproduction Stage B's
first mandatory action.

### 1.3 Diagnosis-memo requirement

Stage B must characterize failing rows (household/node concentration, roster
signatures, income/benefit components, missing preprocessing) **before any
code change**, per charter §7 Stage B step 2, and produce a diagnosis memo the
Goal 1 Manager accepts before step 4 (the bounded correction). This draft
does not pre-judge whether the 2026-06-02/03 diagnosis is still current or
needs to be rerun in full — that determination is Stage B's first action.

**Gate:** no redrawn node and no paper-facing welfare number may be produced
until the exact frozen reprice-parity gate passes (charter §7 Stage B).

> **Currency note added under R-59 (documentation-only).** §1.2's closing
> sentence — *"the gap was never closed after 2026-06-03"* — was written from the
> 2026-06-02/03 evidence set and is **superseded**. Four later on-disk
> increments (Two-L, Two-M, Two-N of 2026-06-03; F3-R2A/B of 2026-06-13; D-BEN
> of 2026-06-16) refine the mechanism and partly refute the §1.2 suspected
> cause. The Stage-B reproduction and root cause are recorded in
> `MNL docs/France_case/P2a/FR_P2a_m08_parity_diagnosis_memo_v1.md`, which
> **governs over §1.2's currency assessment**. §1.2's *numbers* are unchanged
> and were reproduced exactly. Stage A should read the memo before freezing
> §1–§2.

---

## 2. Parity correction + bounded Codex production-path review

Only after the diagnosis memo is accepted:

1. classify the defect as uniform/mechanical-repairable or
   structural/type-specific (the 2026-06-02 diagnosis classified it
   **STRUCTURAL**; Stage B must re-confirm or supersede this with new
   evidence, not assume it);
2. apply **only** the smallest production-path correction the diagnosis
   supports — the 2026-06-02 report found no tested path change closes the
   gap (income side already faithful; build-faithful path is worse); if that
   still holds, the correction is **not a path fix** but one of the two
   design paths the benefit-state report named: (a) a separately authorised
   per-node EUROMOD pricing path with full parity gates, or (b) a design
   decision to price redrawn nodes with a benefit model whose state is
   reconstructible from the node;
3. rerun parity on every existing France 2016 P2a node the redraw path will
   touch;
4. produce a change/evidence packet;
5. **Stage C (Codex, read-only, high reasoning):** bounded review of only the
   changed production path, parity evidence, accepted-input binding, proposal
   correction, and artifact persistence. One bounded review — do not reopen
   general software architecture or prior Phase-5 certification.

**If the failure is structural or the repair requires a generic
`dclaborsupply` package change, halt and escalate** (charter §7 Stage B,
final line; charter §11).

### 2.1 Certified parity status (R-64 carry-forwards)

*Incorporated 2026-08-06 under the Goal-1 R-64 carry-forwards. This subsection
**replaces all earlier parity-status text** in this contract. Where §1.2's
transcribed 2026-06-02/03 failure numbers or §1.3's currency note read as a
statement of current status, they are superseded here and retained only as
history; §1.2's role is now purely the documented failure that Stage B was
required to reproduce.*

#### (i) The certified gate result

The Stage-B reprice-parity gate **PASSES**, certified on attempt

```
20260806T062050Z_339096_ffa19dbeb2a340babf918b3acdaa9f74_parity_PARITY_PASS_FULL
```

published under
`MNL outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/attempts/`.
Every figure below is a named field of that attempt's `gate_manifest.json`
(`aggregate` block unless stated):

| Result | Field | Value |
|---|---|---|
| Chunks run / on grid | `chunks_run`, `chunks_on_grid`, `is_full_run` | **8 / 8**, full run |
| Rows compared | `rows_compared`, `rows_compared_from_chunks` | **225,836** |
| Rows compared == stored rows (asserted) | `rows_compared_equals_stored_rows` | **true** |
| Gate column | `gate_column` | `ils_dispy` |
| Tolerance (frozen, D10) | `tol_eur` | **1.0e-6** EUR absolute |
| Gate max abs diff | `ils_dispy_max_abs_diff` | **0.0** |
| Rows above tolerance | `rows_above_tol` | **0** |
| Non-finite gate values, stored side | `gate_nonfinite_stored` | **0** |
| Non-finite gate values, repriced side | `gate_nonfinite_repriced` | **0** |
| All gate values finite, both sides | `all_gate_values_finite_both_sides` | **true** |
| Witness column (`bsa00_s`, RSA) max abs diff | `bsa00_s_max_abs_diff` | **0.0** |
| Non-finite witness values, stored / repriced | `bsa00_s_nonfinite_stored`, `bsa00_s_nonfinite_repriced` | **0 / 0** |
| Chunks failing | `chunks_failing` | **[]** (empty) |
| EUROMOD hard errors | `chunk_results[*].euromod_hard_errors` | **0** across all 8 chunks |
| Verdict | `verdict` | **PASS** |

All artifact pins verified before comparison: `artifact_binding.all_pins_match =
true`, with all 8 chunk pins matching individually, `expected_rows_total ==
observed_rows_total == 225836` and `expected_hh == observed_hh == 1555`.

**Consequence for the charter §7 Stage-B gate.** The gate in §1.3 — *"no redrawn
node and no paper-facing welfare number may be produced until the exact frozen
reprice-parity gate passes"* — is **satisfied for the FR-2016 singles P2a cell**
by this attempt. It is not satisfied for any other cell, and this contract
authorizes none.

#### (ii) The tightened certification standard (verbatim)

The standard is persisted in the manifest itself (`certification_standard`, at
both attempt level and on every chunk record) and reads, verbatim:

> PASS requires, on EVERY chunk: zero rows above the frozen tol_eur on every gate
> column AND zero non-finite values on BOTH the stored and the repriced side of
> every gate column AND zero EUROMOD hard errors. A non-finite value on either
> side is treated as an infinite absolute difference, never a masked NaN, so it
> both fails the chunk and appears in the failing-row capture. Witness-column
> non-finiteness is counted, captured and reported but does not gate.

Per-side finiteness accounting and the rows-compared assertion are persisted, not
merely asserted in prose: each chunk record carries a `finiteness` block with
`n_nonfinite_gate_stored`, `n_nonfinite_gate_repriced`,
`n_rows_nonfinite_gate_either_side`, the witness-side equivalents, and
`rows_compared_equals_stored_rows`.

#### (iii) Review lineage (stated honestly)

1. The initial Codex production-path review
   (`MNL docs/France_case/P2a/FR_P2a_m08_codex_production_path_review_v1.md`)
   returned **overall REJECT**: **T4** (comparison soundness) and **T7**
   (claim-to-evidence) REJECT; **T1, T2, T3, T5, T6 ACCEPT**. The T4 rejection was
   characterised by the review itself as *"an implementation defect that blocks
   scientific certification; not affirmative evidence of a scientific mismatch."*
2. A **rule-3 conversion** was applied: the harness comparator was fixed (it had
   failed *open* on non-finite values), the report was reissued as
   `FR_P2a_m08_parity_gate_report_v2.md`, and the gate was **re-run** to produce
   the certified attempt in (i). The v1 verdict was withdrawn as a certification;
   the numbers were unchanged but became certified rather than asserted.
3. **The narrow Codex re-verification of T4/T7 landed with overall verdict
   REJECT.** Source:
   `MNL docs/France_case/P2a/FR_P2a_m08_codex_reverification_T4_T7_v1.md`
   (untracked; produced against MNL `520441a…`, monorepo `27756a0…`; no EUROMOD
   execution; read-only).

   | Item | Verdict |
   |---|---|
   | R1 — T4 cure (either-side non-finiteness ⇒ `+inf`, fails and is captured; per-side accounting; row-count assertions) | **ACCEPT** |
   | R2 — T4 witness delta (witness non-finiteness evidence-additive only; `witness_nonfiniteness_gates` persisted `false`) | **ACCEPT** |
   | R3 — T7 cure | **REJECT** |
   | R4 — earned verdict (independent recomputation from the eight new chunk JSONs) | **ACCEPT** |

   T1, T2, T3, T5, T6 remain **ACCEPTED** and were not reopened.

   **What R4 confirms.** The re-verification independently recomputed the gate
   from the eight chunk JSONs and obtained *"225,836/225,836 rows, max gate
   difference 0.0, zero above tolerance, zero gate non-finites, zero hard errors,
   and 8/8 passing chunks"* — matching the persisted aggregate. Its words:
   *"The gate's certified verdict is earned under the tightened standard on the
   new attempt's own evidence."* **§2.1(i) therefore stands, independently
   confirmed**, and the T4 comparator defect is cured.

   **What R3 rejects, and its scope.** The rejection is against **report v2's
   evidence packet**, not against the gate. Report v2's packet-only §§3–4 retain
   two numerical claims that do not trace to the new attempt: an unpersisted
   projected-runtime claim, and a three-execution determinism claim
   (attempts 2, 3, 4 *"each returning `0.0`"*) whose `0.0` fields live in the two
   **prior** attempts' chunk JSONs — files produced by the very comparator whose
   missing finiteness evidence caused the original T4 rejection. The
   re-verification's own characterisation:

   > **REJECT the conversion as a complete T4/T7 certification packet.** T4 is cured, the witness delta is evidence-additive, and the new attempt earns its numerical `PASS`. The sole blocking category is the still-incomplete T7 numerical claim-to-evidence cure in report v2. This is a disclosure/evidence-integrity rejection only; it is not evidence of a finite scientific mismatch and does not reopen any accepted threat.

   **Consequence — binding.** The Stage-A freeze **does not issue on report v2**.
   What is required is narrow and documentary. **No re-run of the gate is
   required** — R4 has already certified the attempt's numbers independently. The
   correction cycle is Stage-B/C business and is **not** performed by this
   contract. The freeze record, not this subsection, carries the final status.

#### (iv) Joint batching remains unlicensed (binding)

**JOINT BATCHING REMAINS UNLICENSED.** Any Stage-D node pricing uses
**target-only D-BEN Option B geometry**: `hh_all = sorted(single idhh)`, chunks of 200 source
households, one `EuromodPricingRunner.price()` call per chunk,
`alt_key_cols=['draw']`, each alternative replicated as an isolated synthetic
household. This constraint is a proven result, not a default: batch-context
dependence was demonstrated via the FR RSA accumulators
(`i_bsa00_cumpers_nw` / `i_bsa00_cumpers_w`, both present in the certified
attempt's `accumulators_available`), which are computed over the whole batch and
therefore make a household's benefits depend on its batch companions. Pricing a
redrawn node jointly with other households would silently change `ils_ben`.
Any proposal to relax this requires a separate authorisation and its own parity
gate.

#### (v) The authorized E2 closure path — report v4 (added in v2)

The decomposition-architecture ruling **§2** closes the E2 axis and fixes the
remedy. Its §2.1 identifies the single valid residual finding: report v3 §0
retained a sentence whose clause after the quoted reviewer classification *"makes
a pairwise inference between the old and new attempts"*, which *"is outside the
new attempt's packet and conflicts with the report-wide rule that prior attempts
provide lineage only."*

Its §2.2 authorizes creating
`MNL docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4.md` (v3 remaining
immutable history), replacing that sentence with, verbatim:

> "The review classified its T4 rejection as an implementation defect that blocked scientific certification rather than affirmative evidence of a finite scientific mismatch."

with **no other report text changing** except title/version bookkeeping, a
one-paragraph v4 supersession declaration, and mechanical cross-reference repair;
plus a concise change log at
`MNL docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v4_change_log.md`.
Its §2.3 requires **one fresh GPT-5.6 Codex read-only review** limited to four
checks, and forbids any code review, gate rerun, EUROMOD execution, architecture
review, or new requirement. **On ACCEPT** v4 becomes the parity report of record,
one acceptance note is created, and the parity axis freezes. **On REJECT** the
matter returns to the deputy with no further self-authorized correction.

**On-disk status at this revision:** `…_parity_gate_report_v3.md` and
`…_parity_gate_report_v3_change_log.md` exist in MNL (untracked); **no v4 and no
v4 acceptance note exist**. This is why the v2 contract status carries
`v4-ACCEPT` as a freeze condition (§8.4). **This contract performs no part of
that cycle.**

---
## 3. Frozen-register block

This section is the STEP 3 unresolved-contract register, values verbatim,
reproduced in full so the execution contract is self-contained. See the
Stage-0 report for source citations in prose; sources are repeated inline
here per item.

### 3.1 DEFINED items

| # | Object | Value | Source |
|---|---|---|---|
| D1 | Attained utility `V_i` | `V_i = log Σ_{j∈C_i} exp(v_i(c_j,ℓ_j) + log g(j;x_opp,i) − log π(j))`; primary estimator `V_i^IS` (importance sampling over existing draws); `V_i^dir` (redraw) is validation cross-check only, escalated only on flagged subset | Charter §4.1; `JMP_welfare_spec_v5.md` §1.1; `RURO_welfare_scaffold_design_contract_v2.md` §3.1 |
| D2 | Measure family, references | `W1`..`W6` table (reference/construction, Ind-y, Ind-A, normative reading) — reproduced in full in §3.1a below | `JMP_welfare_spec_v5.md` §1.3; scaffold contract §3.2 (identical) |
| D3 | Build order | Step 1: validate `W3` end-to-end alone. Step 2: `W5` (access face) + `W2` (2nd Full-Responsibility check) + `W4`/`W6` (Full-Compensation endpoints). Step 3: decide headline empirically; committed focal pair if spread immaterial = `W3` + `W5`. **v2 note (decomposition-architecture ruling §3.1–§3.2):** the *build order* is unchanged — `W3` is still validated first — but `W3`'s step-1 role is now expressly **validation-only**, and the *decomposition* anchor named in D19 is `W2` (primary) with `W5` secondary. The "focal pair" language of Step 3 is a **welfare-family presentation** statement, not a decomposition-anchor statement, and is not read as one | Scaffold contract §5; `JMP_welfare_spec_v5.md` §6; **ruling §3.1–§3.2** |
| D4 | Active measure set | `["W3","W5","W2","W4","W6","W1"]` (config example matches charter §4.2 build-order narrative exactly) — a *sequencing* of the charter's six measures, unchanged by v2 | Scaffold contract §4 |
| D5 | Access/ability/preference parameter membership (47-param baseline) | **Preference (20):** `beta_l0_{sm,sf,f}`, `beta_l_age{,2}_{sm,sf,m,f}`, `beta_l_nkids_{sf,f}`, `theta_l_{sm,sf,f}`, `theta_c_singles`; fixed `theta_l_m=-0.8`, `beta_ll=0`, `beta_c=1`. **Ability (6):** `beta_w_educL`, `beta_w_educH`, `beta_w_pexp`, `beta_w_pexp2`, `sigma`; `beta_w0` common anchor. **Access (23):** `beta_E`, `beta_h_pt1`, `beta_h_pt2`, `beta_h_ft`, `beta_h_lh`; `beta_E_gsur`, `beta_E_drgn2..8`, `beta_E_drgur`, `beta_E_drgmd`, `beta_E_y2015`, `beta_E_y2017`; `beta_occ_{2,3,4}_{m,f}` | `JMP_welfare_spec_v5.md` §2 (table); counts cross-checked against `RURO_welfare_gate_report_W3_v1.md` line "preference 20 / ability 6 / access 23 names" — MATCH |
| D6 | Access-purity rule (channel routing principle) | Education → wage return only → **ability**; never access. Age → experience → ability; age-in-leisure → preference; **never access**. Gender → offers (`beta_occ_*_m/_f`) → access; tastes (`beta_l0_f`, `beta_l_nkids_sf` etc.) → preference. A parameter's normative role follows the channel it acts through, not the observable driving it. Reporting the `[access-only, access+ability]` bracket is mandatory | `docs/France_case/_shared/governance/JMP_ability_opportunity_cut_v1.md` §0–§3 (MNL) — this is the document Step 3 calls "the access-purity rules"; title of its own §2.1 is literally "the access-purity rule binds" |
| D7 | Equalisation operators (qualitative) | **Access:** set access blocks to a common offer environment; hold ability+preference at actual; recompute. **Ability:** neutralise wage-technology's dependence on own education/experience/residual productivity (`beta_w0` stays anchor); hold access+preference; recompute. **Preference:** assign a common reference preference (horizontal reference `R^h`, ratified at U13); revalue feasible sets; recompute. Operative definitions are §5A, **unchanged by v2** (ruling §4.10) | `JMP_welfare_spec_v5.md` §2; scaffold contract §3.2/§7; ability/opportunity-cut memo §5; §5A |
| D8 | Inequality index | Gini, mandatory/primary (`active_indices: ["gini"]`). Sensitivity-only secondary indices: CV², Theil-L, Atkinson(ε=1), Atkinson(ε=2) | Scaffold contract §4 |
| D9 | Engine-parity tolerance (Gate 0) | Smoke `1.0e-8`; production `1.0e-6` (max abs Δ negLL vs estimator negLL) — achieved machine-exact (0.0/0.0/1.1e-13) in the Stage-One production run | `RURO_welfare_gate_report_W3_v1.md` Gate 0 table + "Tolerances" line; `scripts/welfare/configs/welfare_stage1_w3.yaml` |
| D10 | Reprice-parity tolerance | `1.0e-6` euros absolute (`stage2.parity_grid.parity_tol`) — **note (see U-source-mismatch below): this lives in Stage-Two config, not literally inside `RURO_welfare_scaffold_design_contract_v2.md`**, which the charter names as "the frozen scaffold contract" for §6 Stage A thresholds | `scripts/welfare/configs/welfare_stage1_w3.yaml` |
| D11 | Inversion-convergence tolerance (Gate 2) | Residual `1e-6`; bracket width `1e-9`; reference recovers zero exactly (`Φ_i(0)=0` to solver tolerance, `≈−2.91e-10`); monotonicity required; converged for all 12,445 households in the Stage-One production run | `RURO_welfare_gate_report_W3_v1.md` §"Commands run" tolerances line + Gate 2 table |
| D12 | Reference-coverage gate (Gate 4) definition | All required `c_ij` for the reference packages of `Ā/J/o` must be finite and positive before any reference is evaluated; no wholesale EUROMOD rerun; no silent interpolation; missing packages **block**, not approximate. For `W3` (own set, no `Ā/J/o` needed) this passed in Stage One (0 non-positive across all 3 groups) | Scaffold contract §6.1(iii); `RURO_welfare_gate_report_W3_v1.md` Gate 4 |
| D13 | Household-unit integrity gate (Gate 3) | One `Ω_i` per couple from joint utility/joint budget; no per-capita split; type-conditional references; passed in Stage One for all 3 groups | Scaffold contract §6.3; gate report Gate 3 |
| D14 | Welfare code paths (scaffold + application) | MNL: `scripts/welfare/welfare_core.py`, `welfare_vdir.py`, `run_stage1_w3.py`, `run_stage2_parity.py`, `configs/welfare_stage1_w3.yaml`, `configs/welfare_p2a_singles2016.yaml`. Nested (read-only reuse): `dclaborsupply/welfare/{__init__.py,protocol.py}`, `dclaborsupply_app/welfare/{__init__.py,core.py,measures.py,vdir.py}` | Stage-0 inventory (§2 of accompanying report), hashes recorded there |
| D15 | S-10 four scenarios (formula) | `Δ_j = min{0.5·se_rob_j, 0.5·(θ̂_j − lb_j)}`; `θ^sens_j = θ̂_j − Δ_j`. Four scenarios: (1) baseline; (2) `beta_l0_sm` at sensitivity value; (3) `beta_w_pexp2` at sensitivity value; (4) both jointly. No search beyond these four points | `JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md` §3–4 |
| D16 | S-10 material-loading trigger | ≥1% change in mean/median welfare; ≥0.005 absolute Gini change; **≥2pp opportunity-share change**; sign/ordering change in a headline decomposition component; qualitative-conclusion change. **v2 binding note (ruling §3.6):** the pre-registered **2-percentage-point trigger applies to `s_opp = (φ_A^W2 + φ_B^W2) / I^W2(∅)`** as defined at §5.5. It is not applied to any other share, and no other share substitutes for it | S-10 spec §6; **ruling §3.6** |
| D17 | Vigilance treatment, `beta_l0_sf` | Monitored alongside the two flagged coordinates in every welfare/decomposition output; robust CI lower endpoint `0.05467` sits adjacent to the male counterpart's recorded `0.05`-class bound; its own bound is **not** in accepted artifacts; nothing asserted in paper text absent an accepted bound record; not perturbed, not itself a Tier-1 scenario coordinate | Handoff §2 item 5; charter §6 (final bullet) |
| D18 | Disclosure policy | No household-level welfare or microdata artifact in the public `Job_Market_paper` repository (charter acceptance gate #13); restricted numerical artifacts, manifest, and acceptance pointer live in MNL under an approved P2a welfare production namespace (charter §8 "MNL") | Charter §8, §9.13 |
| **D19** | **Shapley decomposition scope — AMENDED IN v2** | Three-way `{access, ability, preference}` game, `3! = 6` orderings, **no fourth channel**. **Primary source decomposition: `W2`** (the non-degenerate Full-Responsibility measure). **Secondary decomposition: `W5`** (the access-compensated dual, showing how attribution changes under a different normative reference). **Validation only: `W3`** (first welfare-engine validation measure; laissez-faire/full-responsibility endpoint in the welfare-family comparison; reference-recovery and inversion diagnostic). `W1`, `W4`, `W6` remain in the six-measure welfare-family results and **carry no M08 Shapley requirement**. All measure references are frozen across coalitions. **v1's D19 — "primary anchor `W3`, second check `W2`; `W1`/`W5` corroborating interpretation only" — is SUPERSEDED in full.** The surviving prohibition from v1's D19 stands: no measure is used as a numerical reconciliation identity against another | **Ruling §3.1, §3.2, §3.3, §4.1–§4.3, §4.9**; charter §4.3 (as amended by the ruling); `JMP_welfare_spec_v5.md` §1.4/§6 (D2); scaffold contract §9 |
| D20 | LOC4 sequencing (Path B) | Baseline welfare proceeds on the certified common-dispersion model now; LOC4 four-density robustness is mandatory **before final quantitative decomposition claims**, not before the first prototype | `JMP_LOC4_pathB_ruling_v1.md` (canonical, tracked at `docs/Missions/`, sha256 `4e7b95d9ecf730a3f820f18f2a9fb207a317775f32165486e6794b92eee8b4bb` — see §3.2a(U15)); handoff §2 item 3; charter §5.5 |
| **D21** | **Fixed-background residual `R_bg` — NEW IN v2** | For `k ∈ {W2, W5}`, `R_bg^k = I^k({A,B,P})`: the inequality remaining after all three modeled structural channels are equalised while the frozen background is retained. **It is not a Shapley contribution.** It is **never** labelled an identified endowment, needs, circumstance, unfairness, or causal component. It is reported in **levels and as a share** of baseline inequality. Its admissible sources are enumerated verbatim at §5.4. There is **no requirement that `R_bg^k = 0`**, and no component is renormalised to make shares sum to 100 percent with the residual excluded | **Ruling §3.4, §3.5(4), §3.5(5), §3.6, §3.7** |

*(D21 is appended after D20 rather than inserted, so that every pre-existing
D-number keeps its v1 referent. No D-item was renumbered.)*

**D2 in full (the measure table):**

| Measure | Reference / construction | Ind y | Ind A | Normative reading | M08 decomposition role (v2) |
|---|---|---|---|---|---|
| `W1` | preferred job in own set `A`, pay ignored | + | − | compensate pay; responsible for the set | family results; **no Shapley requirement** |
| `W2` | best-paid equivalent in own set `A` | − | − | Full Responsibility (own everything) | **PRIMARY source decomposition** |
| `W3` | laissez-faire in own set `A`, with pay | − | − | Full Responsibility (laissez-faire) | **VALIDATION ONLY** |
| `W4` | staying-home equivalent (non-employment `o`, `y(o)=0`) | + | + | Full Compensation | family results; **no Shapley requirement** |
| `W5` | uniform subsidy to reference set `Ā` | − | + | compensate the set; responsible for pay | **SECONDARY decomposition** |
| `W6` | best job in whole economy `J` | + | + | Full Compensation (+ Weak Responsibility) | family results; **no Shapley requirement** |

*(The first five columns are v1's D2 table, unchanged. The sixth column records
the ruling §3.2 role assignment and adds no measure, no reference, and no
construction.)*

### 3.2 UNDEFINED items — register with v2 status

Status vocabulary: **RESOLVED** = value extracted from a committed on-disk source
and recorded verbatim in §3.2a; **PROPOSED-PENDING-RATIFICATION** = no operative
value exists on disk, a value is proposed with a one-line rationale and is *not*
frozen; **ESCALATED** = cannot be resolved from the repositories, goes to the
Goal 1 Manager as a §8 question; **RESOLVED-BY-DEPUTY-RULING** = closed by a
binding deputy decision cited inline.

| # | Object | What exists | What is missing | Blocking? | **v2 status** |
|---|---|---|---|---|---|
| U1 | Full artifact hashes | Truncated hashes only: theta bytes `c024b893…f0580d`, Phase-5 bundle `d08947ce…`, reporting map `89a0465c…`, extraction memo `b800d0e3…`, model anchor `982c5221…` | Full untruncated hex digests | **Yes** — charter §3 states explicitly a truncated hash "is not sufficient for execution"; Stage A must resolve and record full identifiers | **RESOLVED** — all five full digests in §3.2a(U1); each independently recomputed/matched against a committed artifact |
| U2 | Non-employment option `o` (needed for `W4`) | Config key name only: `o_nonemployment_key: "..."` (literal ellipsis placeholder in the scaffold contract) | The actual alternative key in the P2a singles choice set that represents "staying home" | **Yes** — `W4` cannot be built without it | **RESOLVED** — with a schema correction: **no alternative *key* exists**; `o` is resolved by predicate, §3.2a(U2) |
| U3 | "up1 manifest note" | Nothing located | Exhaustive search (filename + content grep across MNL, Job_Market_paper, `dclaborsupply-monorepo`, plus `git log --all --grep`) found **no** file, commit message, or in-document reference matching "up1" in any welfare-adjacent context | **Clarify** — cannot rule out this is a typo or a not-yet-created artifact; flagged as a direct question rather than guessed | **ESCALATED — NO REFERENT.** Unchanged. **Not enumerated among the v2 freeze conditions** (§8.4); carried to Stage A as an open documentary question. This contract does **not** close it |
| U4 | Subgroup list "already pre-registered" | Both the charter (§6) and the S-10 spec (§5, §7) refer to pre-registered subgroup summaries as if they exist | No subgroup list was found anywhere in MNL or `Job_Market_paper` docs | **No longer blocking** — the list now exists | **RESOLVED-BY-DEPUTY-RULING** — supplied by `docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md` (Deputy Programme Director, 2026-08-05), incorporated at §6.3–§6.7; §3.2a(U4). **v2 rebinds its §3.2/§3.3 "primary" slot from `W3` to `W2`** (§6.3.4) |
| U5 | ESS threshold (frozen value) | Contract schema: `ess_threshold: "declared"` (placeholder). Stage-One **operational** run used `30` | A value frozen *in* the contract/handoff for M08 | **Yes, narrow** | **RESOLVED** — adopt `ess_threshold = 30`, §3.2a(U5) |
| U6 | Draw-growth stability tolerance | Contract schema: `tolerance: "declared"` (placeholder); `draw_multipliers: [1,2,4]` | 2×/4× draw-multiplier datasets **still do not exist on disk**; Gate 1(i) was BLOCKED in Stage One and remains blocked; no tolerance number was ever set because the check never ran | **Yes** — this gate cannot pass without new data | **ESCALATED** — a data-creation decision, not a documentation gap. **Enumerated in the v2 freeze conditions** (§8.4): build the datasets, or carry Gate 1(i) forward BLOCKED under a pre-registered escalation rule |
| U7 | Direct-vs-IS (`V_i^dir`) agreement tolerance | Contract text: "require agreement within tolerance" (prose); Stage-One code constant `0.5` nats on high-ESS `\|delta_common\|` | Ratification for M08 | **Yes** | **RESOLVED-BY-R-71 at `0.5` nats**, as transcribed at §5A.8 **V22** (*"`V_i^dir` tolerance **0.5 nats** (R-71)"*). §3.2a(U7) retains the extraction record. *Recording flag for Stage A:* v1 §8.2 still listed U7 as unratified, which contradicted its own V22 transcription; v2 resolves the contradiction **in favour of the V22 transcription**, and Stage A should confirm against the written R-71 |
| U8 | Shapley-exhaustiveness numeric tolerance | v1 proposal only; no constant anywhere in `scripts/welfare/` | An explicit numeric epsilon | **Yes, narrow** — needed for the §5.4 gates to be checkable in code | **RESOLVED — FROZEN AS `ε_Shapley`.** The decomposition-architecture ruling §3.5(2)–(3) writes the gates in terms of `ε_Shapley`; this contract fixes `ε_Shapley` **= the frozen U8 convention** `1e-9 · max(1, |I^k(∅)|)` (§3.2a(U8), §5.4). The **integration stability tolerance remains separate and governing** for each `I^k(S)` and is **not** replaced by `ε_Shapley` |
| U9 | MNL production output namespace | Existing precedents on disk | An M08-specific namespace | **Yes** | **RESOLVED** — `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/` under the `attempts/` transaction pattern, §3.2a(U9) |
| U10 | S-10 resolved numeric values | Formula (D15) is exact | `theta_hat_j`, `se_rob_j`, `lb_j`, `Δ_j`, `θ^sens_j` for `beta_l0_sm` and `beta_w_pexp2` | **Yes** — pre-execution requirement | **MECHANICAL-AT-FREEZE** — the source artifact is digest-bound under U1; Stage A pulls the numbers against a verified file and substitutes them into D15 (§8.3 item 1) |
| U11 | Reference ability set `Ā` (needed for `W5`) | A default is named (`type_conditional_median_opportunity`) with one listed sensitivity (`maximal_opportunity`) | A single ratified primary choice | **Yes, narrow** — **and now load-bearing for the secondary decomposition** (`W5`, D19) | **RESOLVED** — R-59 ratifies `type_conditional_median_opportunity`; verbatim source in §3.2a(U11) |
| U12 | Common reference offer environment (access-equalisation operand) | Qualitative description only | A specific frozen choice | Nonblocking for `W3` build; **blocking before Stage F** | **RESOLVED-BY-RULING (R-71)** — the design memo `JMP_M08_access_equalisation_operand_design_v1.md` (D1–D10, V1–V13) is ratified and transcribed at **§5A**, **unchanged by v2** (ruling §4.10) |
| U13 | Reference preference `R` for preference-equalisation | Horizontal reference `R^h` named as "the natural choice" | A hard freeze | Nonblocking for `W3`; **blocking before Stage F** | **RESOLVED** — R-59 ratifies the named default `R_h`; verbatim source in §3.2a(U13) |
| U14 | Pinned-preference held-vs-swapped switch | Config flag exists; default recorded is `held` | Explicit ratification of `held` | **Yes, narrow** | **RESOLVED** — R-59 ratifies `held`; verbatim source in §3.2a(U14) |
| U15 | Two non-identical LOC4 rulings | Two differently-named, uncommitted files at v1 | A single governing, committed LOC4 ruling | Nonblocking for M08 itself; flagged before LOC4/M08R | **RESOLVED — CLOSED IN v2.** The canonical file is now **tracked** at `docs/Missions/JMP_LOC4_pathB_ruling_v1.md`, sha256 `4e7b95d9ecf730a3f820f18f2a9fb207a317775f32165486e6794b92eee8b4bb`, and it is the file charter §2 names by exact filename. The differently-named `…_robustness_ruling_v1.md` is **no longer on disk**. §3.2a(U15) records the verification |

### 3.2a Resolutions — values, sources, and exact status

Every value below was read from a committed on-disk artifact at the revisions
named in the header. No value is inferred, and nothing here is FROZEN — Stage A
freezes.

#### U1 — full artifact digests · **RESOLVED**

| Artifact | Full SHA-256 (or commit) | Verification performed |
|---|---|---|
| Model/spec anchor (MNL commit) | `982c52217031158c4a2368709d4a6b211ebcde76` | `git cat-file -t` in MNL → `commit`; subject *"results(p2a): record accepted Phase-4 curvature diagnostics"*, 2026-07-30 |
| Phase-5 inference bundle | `d08947ce015f2b2a922c6d5591ebe600c53016922b3a1158d90f125cd2195232` | matches `"bundle_sha256"` at line 270 of the committed Phase-5 manifest (path below) |
| Phase-5 parameter reporting map | `89a0465cc55f4bc05898559120591e4c28db15a18992bd2b33ba6538ce7b8481` | recomputed `sha256(docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv)` in `Job_Market_paper` → exact match |
| Phase-5 inference results memo | `b800d0e3b54d19340e231bd14020173ffd51904fdeb2832cbaa551eb731284b9` | recomputed `sha256(docs/results/FR_P2a_phase5_inference_results_memo_v1.md)` in `Job_Market_paper` → exact match |
| **θ̂ bytes (extracted per R-59(a))** | `c024b89386c502003f9d4abb927b048dfab42c0bafe48d9a69d9fcb330f0580d` | **extracted from two committed manifests, agreeing exactly** (below) |

**θ̂-bytes source paths (MNL, committed):**

- `outputs/p2a_singles2016/region_live_v1/phase5_inference_v1/attempts/20260803T133122Z_14772_817e8deb503d408fa73b8b53d598c0db_dryrun_PHASE_5_DRY_RUN_COMPLETE/phase5_manifest.json`
  — line 14, key `"theta_bytes_sha256"`. The same file carries `"phase3_bundle_sha256": "2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b"`,
  `"phase4_bundle_sha256": "5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3"`, and the Phase-5 `bundle_sha256` above.
- `outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/complete/phase4_manifest.json`
  — line 576, key `"theta_hat_sha256"`, identical value.

*Recording note (not a blocker):* Phase-5 has **no** `complete/` directory on
disk; its accepted artifacts live under `attempts/…_dryrun_PHASE_5_DRY_RUN_COMPLETE/`.
Stage A should bind Phase-5 by that attempt path, not by a `complete/` path.

#### U2 — non-employment option `o` · **RESOLVED (with a schema correction)**

The scaffold contract's `o_nonemployment_key: "..."` presumes a named alternative
key. **The P2a singles choice set has no such key.** Alternatives are indexed by
`draw ∈ {0,…,100}` (101 per household), and non-employment is a *predicate over a
column*, not a key. The operative constant, verbatim from the committed P2a
welfare runner (`MNL scripts/welfare/run_p2a_singles_welfare.py`, lines 110–115):

```python
# home node = lowest-draw working==0 alternative (run_f4a…py:220-226)
is_home = (self.working_grid == 0)
self.home_count = is_home.sum(axis=1).astype(int)
self.home_idx = np.argmax(is_home, axis=1)
rows = np.arange(ng)
self.leisure_term_home = self.leisure_term_grid[rows, self.home_idx]
```

- **Operative definition of `o`:** the alternative with the **lowest draw index
  such that `working == 0`**, per household.
- **Column provenance:** `working` is a required column of the frozen P2a
  draw-geometry contract (`MNL scripts/p2a/configs/p2a_regionlive_rebuild_v1.yaml`,
  `frozen_inputs.draws_geometry.required_columns`) and is the `beta_E` shifter
  variable in the certified spec (`MNL scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`,
  `hours_opportunity.shifters[0].variable: "working"`).
- **Precedent:** identical resolution in `run_f4a_singles_measure_core.py:220-226`,
  the F4 line the P2a runner copy-adapts.

**Stage-A action:** replace `o_nonemployment_key` in the config schema with a
predicate field (e.g. `o_nonemployment_predicate: "working == 0"` plus a
tie-break rule `lowest_draw_index`), because the current key-shaped field cannot
be filled correctly for this data model.

#### U5 — ESS threshold · **RESOLVED: `ess_threshold = 30`**

Adopted per R-59(c), citing `MNL docs/jmp_methodology/RURO_welfare_gate_report_W3_v1.md`:

> `ESS_i = (Σ_s ω_is)² / Σ_s ω_is²`, with `ω_is = exp(V_is − lse_i)` the within-household
> normalised importance weights. Threshold `core.integration.ess_threshold = 30`.

(line 94–95; restated in the report's "Tolerances" line 251: *"ESS threshold 30"*).
Operational corroboration: `MNL scripts/welfare/configs/welfare_stage1_w3.yaml:33`
— `ess_threshold: 30.0`.

#### U7 — `V_i^dir` cross-check tolerance · **RESOLVED-BY-R-71 at `0.5` nats**

`RURO_welfare_stage2_vdir_crosscheck_v2.md` contains **no** direct-vs-IS agreement
tolerance — its only numeric tolerance is the reprice-parity `1e-6` (D10). The
Stage-One **code** constants from which the value was extracted are recorded here
verbatim:

```python
# scripts/welfare/fastlane/run_f3r2a_repair_diagnosis.py:608-610
# Utility-only B2 gate: |delta_common| <= 0.5 for each priced anchor
statuses = [
    "pass" if abs(v.get("delta_common", float("inf"))) <= 0.5 else "fail"
```

```python
# scripts/welfare/run_stage4c_singles_vdir_smoke.py:828-829, 841
high_ok = (has_high_ess and cmp["high_ess_delta_common_abs_max"] is not None
           and cmp["high_ess_delta_common_abs_max"] <= 0.5)
…  f"high-ESS like-for-like |delta| too large … > 0.5 nats"
```

**Operative value:** `|V_i^dir − V_i^IS| ≤ 0.5` nats, evaluated on the
like-for-like common basis and applied only to **high-ESS** households
(ESS ≥ 30 per U5). §5A.8 **V22** transcribes this as *"`V_i^dir` tolerance
**0.5 nats** (R-71)"* and extends its application from the baseline to **each
coalition's** flagged subset. Stage A confirms against the written R-71.

#### U8 — Shapley-exhaustiveness epsilon · **RESOLVED — FROZEN AS `ε_Shapley`**

Search of `MNL scripts/welfare/` (`*.py`, `*.yaml`) for `shapley` returns **zero
matches**: no Stage-One implementation exists, and no competing constant exists to
be overridden. The decomposition-architecture ruling §3.5(2)–(3) states the two
arithmetic gates in terms of `ε_Shapley` without fixing its value; this contract
fixes it as the frozen U8 convention:

```
ε_Shapley  =  1e-9 · max(1, |I^k(∅)|)          for each k ∈ {W2, W5}
```

*Rationale (unchanged from v1's proposal, now adopted):* `1e-9` is the tightest
tolerance already in the Stage-One tolerance line (the inversion bracket width,
D11), and relativising it keeps the gate meaningful for Gini-scale and euro-scale
indices alike. **Anchoring note:** the reference magnitude is `|I^k(∅)|` — the
*baseline* inequality of the measure being decomposed — because the ruling's two
identities are both written against `I^k(∅)`. This replaces v1's `|I(Ω)|`
phrasing, which had no per-measure referent once two measures are decomposed.

**Scope limit, binding.** `ε_Shapley` governs **only** the Shapley *arithmetic*
gates at §5.4(2) and §5.4(3). The ruling §3.5 closing sentence is binding and is
transcribed at §5.4: *"The separate numerical-integration stability tolerance
continues to govern the accuracy of each \(I^k(S)\); it is not replaced by the
Shapley arithmetic tolerance."* In this contract that separate machinery is the
Stage-D integration battery — the ESS diagnostics and frozen escalation rule
(U5, **V6**, **V22**), the `V_i^dir` cross-check at `0.5` nats (U7), and the
draw-growth stability gate (U6, currently BLOCKED). None of those is subsumed by
`ε_Shapley`, and passing `ε_Shapley` never substitutes for them.

#### U9 — MNL output namespace · **RESOLVED**

```text
outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/
├── attempts/<attempt_id>_<STATUS>/     # every run publishes here
└── complete/                           # promoted only on acceptance
```

Adopted per R-59(d). This nests M08 inside the accepted P2a region-live run
namespace (the same parent that holds `phase3_estimation_v1/`,
`phase4_curvature_v1/`, `phase5_inference_v1/`), rather than beside the older
`outputs/welfare/*` Stage-One precedents, so M08's artifacts inherit the P2a
lineage they are conditioned on. The `attempts/` transaction pattern is the one
already implemented for Phases 3–5 (`MNL scripts/p2a/run_p2a_phase5_inference.py`,
lines 415–506; `run_p2a_regionlive_rebuild.py`, lines 1746–1848): lock → staging
dir → atomic same-volume rename to `attempts/<attempt_id>_<STATUS>`; `complete/`
is **never** created or promoted by the runner itself. Restricted household-level
artifacts stay here (D18); nothing household-level goes to `Job_Market_paper`.

#### U11 / U13 / U14 — ratified defaults · **RESOLVED**

All three are ratified per R-59(e) at the values the scaffold contract already
names as defaults. Definitions quoted **verbatim** from
`MNL docs/jmp_methodology/RURO_welfare_scaffold_design_contract_v2.md`:

**U11 — reference ability set `Ā`** (lines 286–288):

```yaml
      Abar_reference:                                # W5 reference ability set
        primary: "type_conditional_median_opportunity"
        sensitivity: ["maximal_opportunity"]
```

Ratified: **`type_conditional_median_opportunity`** as M08's primary `Ā`;
`maximal_opportunity` retained as the listed sensitivity only. **v2 note:** `Ā`
is now load-bearing for the **secondary decomposition** (`W5`, D19), not only for
the welfare family; Stage A should treat its verification with the same weight as
the primary-measure references.

**U13 — reference preference `R`** (line 281, in the `reference_preference` block):

```yaml
      W5: "R_h"                                       # horizontal reference preference
```

Ratified: the named default **`R_h`** (the horizontal reference preference) for
preference-equalisation.

**U14 — pinned-preference switch** (line 318, and §7 lines 447–456):

```yaml
    preference_equalisation_pinned_switch: "held"     # "held" | "swapped" (JMP_welfare_spec_v5.md §3a) — see §7
```

> Under the deferred **preference-equalisation** channel the pinned params may be
> either **held at their pinned values** or **swapped for the reference preference**
> (`JMP_welfare_spec_v5.md` §3a). This choice sizes the couples preference component
> and therefore the couples opportunity share, so it MUST be a config flag
> (`decomposition_readiness.preference_equalisation_pinned_switch: held | swapped`),
> surfaced now even though equalisation is implemented later. The default recorded
> here is `held`; the contract requires the flag to exist and be honoured by the
> later module, not that either value be computed now.

Ratified: **`held`**. (Informational for M08, which is singles-only; the pinned
params `theta_l_m` and `beta_ll` are couples-side. The flag must still exist and
be honoured because the machinery is shared.)

#### U4 — pre-registered subgroup list · **RESOLVED-BY-DEPUTY-RULING**

**Resolution (2026-08-06).** The list is supplied by the Deputy Programme
Director's binding ruling:

| Field | Value |
|---|---|
| Path | `Job_Market_paper docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md` |
| SHA-256 | `41061f7ce681f56528cd3576dda707691e3440bac7c35bb6ca4947dde0af9bcb` (restated under Goal-1 **R-70.2**, 2026-08-06; pre-fix digest `b7c0ac18557c13984b685f32f64355c8708fdfd020c1880ae9efd40edce12181`) |
| Bytes | 5,168 |
| Decision-maker / date | Deputy Programme Director, 2026-08-05 |
| Status in this contract | Incorporated at **§6.3** (dimensions, statistics, disclosure — verbatim), **§6.4** (label/weighting sources), **§6.5** (implementation path), **§6.6**/**§6.7** (output files); **measure slot rebound `W3` → `W2` at §6.3.4** under the later decomposition-architecture ruling |
| Tracking | Untracked; rides the Stage-A freeze commit |

The ruling's own §5 requires exactly this incorporation before Stage-D welfare
execution, and its §6 states that it *"closes U4."* The dimensions it
pre-registers are **sex**, **education (`educ3`)**, and **broad region
(`drgn1`)**; it explicitly **excludes** age bands and occupation from the
mandatory list, with reasons quoted at §6.3. The `docs/design_notes/` duplicate
was deleted under R-70.2; one copy remains.

#### U15 — LOC4 ruling · **RESOLVED (closed in v2)**

v1 recorded U15 as ESCALATED on two findings: the two candidate files were not
byte-identical, and **neither was committed**, so the phrase "the committed
`docs/missions/` copy" had no referent. **Both findings are now spent.**
Verification performed for this revision, at `Job_Market_paper` HEAD `f6a1130`:

| Check | Result |
|---|---|
| `git ls-files \| grep -i loc4` | **`docs/missions/JMP_LOC4_pathB_ruling_v1.md`** — the canonical file is **tracked** |
| `sha256(docs/Missions/JMP_LOC4_pathB_ruling_v1.md)` | **`4e7b95d9ecf730a3f820f18f2a9fb207a317775f32165486e6794b92eee8b4bb`** — identical to the digest v1 recorded for the then-untracked `docs/design_notes/` copy, i.e. the canonical file's bytes are unchanged, only its tracking status and path changed |
| `find docs -iname "*loc4*"` | exactly **one** file — `docs/Missions/JMP_LOC4_pathB_ruling_v1.md` |
| `docs/Missions/JMP_LOC4_pathB_robustness_ruling_v1.md` (v1's competing document, sha256 `b2ddee46…`) | **not on disk** |
| `docs/design_notes/JMP_LOC4_pathB_ruling_v1.md` (v1's untracked copy) | **not on disk**; `docs/design_notes/` now holds two unrelated files |

**Disposition:** the governing LOC4 document is
`docs/Missions/JMP_LOC4_pathB_ruling_v1.md` — the file charter §2 item 4 names by
exact filename, now tracked at the canonical path, with the 5-item materiality
rule. There is no longer a competing document and no ambiguity to escalate. D20's
source column is updated to cite it with its digest. **U15 is closed; §8.1's U15
row is closed with it.**

---

### 3.3 Non-blocking / resolved-by-charter-wording items

- **Second headline inequality index:** charter/contract language is
  conditional ("if already pre-registered"); none is — this is simply not
  applicable, not a gap.
- **Reprice-parity tolerance authority mismatch:** the number itself is
  defined (D10) but sourced from Stage-Two config rather than literally from
  `RURO_welfare_scaffold_design_contract_v2.md` as the charter's phrasing
  implies. Noted for precision, not blocking — the value is unambiguous and
  single-sourced.
- **Charter §4.3's `W3` anchor sentence.** Charter §4.3 reads *"The primary
  source decomposition is anchored on \(W^3\). \(W^2\) is the pre-registered
  second check."* That sentence is **superseded by the decomposition-architecture
  ruling §3.1–§3.2 and §4.1–§4.3**, which the charter's own governance chain
  permits: the ruling is a binding deputy decision issued after the charter and
  expressly directs the amendment. This is recorded here so that a Stage-A reader
  comparing contract to charter finds the divergence declared rather than silent.

---
## 4. The single authorized welfare execution (Stage D–G)

Authorized **only** after Sections 1–2 close (parity passes and the E2 axis
closes per §2.1(v)) and Stage A (independent review) freezes this contract with
all of §3.2's blocking items resolved.

1. **Stage D — integration certification:** reproduce estimator/welfare
   engine parity at accepted `θ̂` (D9); compute household ESS diagnostics
   (threshold per U5, resolved); run the pre-registered redraw cross-check on
   the flagged set at the `0.5`-nat tolerance (U7); run draw-growth
   stability (blocked on U6); apply the frozen escalation rule; verify
   inversion convergence (D11) and invariances; record a restricted-artifact
   manifest at the namespace resolved under U9.
2. **Stage E — baseline family:** compute `W1..W6` in build order D3/D4 (the
   charter §4.2 set, per §6.4); report per D-items 5–13 diagnostics; emit the
   §3.1 subgroup tables required by §6.3.2 (six measures × {sex, education});
   no stochastic-dominance exercise. **`W3` is validated here and reported as
   the laissez-faire/full-responsibility endpoint of the family comparison**
   (D19); its validation role is unchanged and is not diminished by v2.
3. **Stage F — decomposition:** per §5 below. **Primary: `W2`. Secondary:
   `W5`. `W3` is not decomposed.** Emit the §3.2 subgroup tables for the
   **primary `W2`** baseline (§6.3.2 as rebound at §6.3.4), noting that **no
   subgroup-level Shapley decomposition is required or permitted** in M08.
   Report `R_bg^k` in levels and as a share for each decomposed measure (D21).
4. **Stage G — S-10 Tier-1:** exactly the four scenarios of D15, with the
   resolved numeric values of U10; report per D16, whose 2pp opportunity-share
   trigger reads on `s_opp` (§5.5); emit the §3.3 per-scenario subgroup tables
   for **`W2`** (§6.3.2/§6.3.4); monitor `beta_l0_sf` per D17 without
   perturbing it.

Subgroup reporting at Stages E–G is governed throughout by §6.3–§6.7 (dimensions,
statistics, `dwt` weighting, `SUPPRESSED_LT30` disclosure, output files). Any node
pricing performed at Stage D uses **target-only D-BEN Option B geometry**; joint
batching is not licensed (§2.1(iv)).

**No welfare computation, code change, or numerical execution has occurred
under this draft.** Everything in this section is a specification of what
Stage D–G will do once authorized, not a record of anything done.

---

## 5. Decomposition (Shapley–Shorrocks) — under the decomposition-architecture ruling

**This section replaces v1's §5 in full.** Its content is the
decomposition-architecture ruling §3, transcribed verbatim where the ruling
states a definition, an identity, a gate, a headline quantity, or an
interpretation. The operator definitions it invokes are at **§5A** and are
**unchanged** (ruling §4.10).

### 5.1 Measure roles (ruling §3.1–§3.2, verbatim)

**`W3` is validation-only.** Ruling §3.1, verbatim:

> ### 3.1 W3 is not a level-inequality decomposition target
>
> `W3` remains:
>
> - the first welfare-engine validation measure;
> - the laissez-faire/full-responsibility endpoint in the welfare-family comparison;
> - a reference-recovery and inversion diagnostic.
>
> It is not the primary source-decomposition measure.
>
> Reason: under the accepted own-set laissez-faire construction, baseline
> \(\Omega_i^3 \simeq 0\) for every household. Hence \(I(\Omega^3)\simeq0\) is correct by construction and contains no observed baseline inequality to allocate.
>
> Do not redefine `W3` and do not create a “common-reference W3.” That would silently replace a characterised welfare measure with a new object.

**Binding consequences for this contract, stated as prohibitions:**

- **No "common-reference `W3`" is created** by this contract, by any Stage-D–G
  runner, or by any config it authorizes. `W3`'s own-set laissez-faire reference
  construction is unchanged.
- **`W3` is not redefined.** Its D2 row, its Gate-0/2/4 validation role, and its
  place in the family comparison stand exactly as in v1.
- **`W3` is not decomposed.** No `I^{W3}(S)` is computed for any non-empty `S`,
  no `φ_q^{W3}` is reported, and no `R_bg^{W3}` exists.

**Primary and secondary measures.** Ruling §3.2, verbatim:

> ### 3.2 Primary and secondary decomposition measures
>
> For M08:
>
> - **Primary source decomposition:** `W2`, the non-degenerate Full-Responsibility measure.
> - **Secondary decomposition:** `W5`, the access-compensated dual, used to show how attribution changes under a different normative reference.
> - **Validation only:** `W3`.
> - `W1`, `W4`, and `W6` remain in the six-measure welfare-family results but do not require a Shapley decomposition in M08.
>
> This preserves the intended two-decomposition workload while removing the degenerate object.
>
> All measure references are frozen across coalitions. The decomposition therefore measures changes in attained welfare valued in the baseline measure's units; it does not allow the reference itself to move with the equalised channel.

### 5.2 The game: three channels, no fourth (ruling §3.3, verbatim)

> ### 3.3 The three-channel game is conditional, not a complete four-channel causal partition
>
> The M08 Shapley game remains:
>
> \[
> N=\{A,B,P\},
> \]
>
> where:
>
> - \(A\): access;
> - \(B\): ability/wage technology;
> - \(P\): preferences.
>
> The following remain fixed across coalitions:
>
> - the disposable-income matrix \(c_{ij}\);
> - tax-benefit rules and non-labour-income inputs;
> - alternative support;
> - proposal correction \(\pi\);
> - measure references;
> - all other objects not assigned to \(A,B,P\).
>
> Do not invent a fourth `endowment/needs` Shapley operator in M08. Merely naming a fourth channel without an executable counterfactual operator would not constitute a Shapley decomposition. A genuine fourth-channel design would require a separately authorized operator and probably targeted EUROMOD re-evaluation; it is outside M08.

**Recorded verbatim, as the ruling requires, and binding on every later reading
of this contract:** *"Merely naming a fourth channel without an executable
counterfactual operator would not constitute a Shapley decomposition."*
**No fourth-channel operator is authorized in M08.** R9 §4.4's endowment/needs
fourth-channel proposal remains an escalation *proposal only* and is **not
adopted**; v1's §7.3 escalation of it is now disposed of at §7.3 below.

**Fixed-across-coalitions confirmation (ruling §4.8).** `c_ij`, `π`, alternative
support, and all measure references are fixed across coalitions. The mechanical
assertions that enforce this are **§5A.8 V2 (reference coalition-invariance,
hash-identical), V3 (π-invariance, hash-identical), and V4 (no new package,
hash-identical)** — **all three are UNCHANGED from v1**, and v2 confirms them as
the operative form of ruling §3.3's fixed-object list. `π` is never touched by
any operator (§5A.0).

### 5.3 Exact residual accounting (ruling §3.4, verbatim)

> ### 3.4 Exact residual accounting
>
> For measure \(k\in\{W2,W5\}\), let \(I^k(S)\) be inequality when channels in \(S\subseteq N\) are equalised.
>
> Compute the standard three-channel Shapley contributions:
>
> \[
> \phi_q^k
> =
> \sum_{S\subseteq N\setminus\{q\}}
> \frac{|S|!\,(3-|S|-1)!}{3!}
> \left[I^k(S)-I^k(S\cup\{q\})\right],
> \qquad q\in\{A,B,P\}.
> \]
>
> Define the fixed-background residual:
>
> \[
> R_{\mathrm{bg}}^k=I^k(\{A,B,P\}).
> \]
>
> The exact identities required are:
>
> \[
> \phi_A^k+\phi_B^k+\phi_P^k
> =
> I^k(\varnothing)-R_{\mathrm{bg}}^k,
> \]
>
> and
>
> \[
> I^k(\varnothing)
> =
> \phi_A^k+\phi_B^k+\phi_P^k+R_{\mathrm{bg}}^k.
> \]
>
> This is the M08 exhaustiveness rule.
>
> `R_bg` is not a Shapley contribution and is not called an identified endowment, needs, circumstance, unfairness, or causal component. It is the inequality remaining after all three modeled structural channels are equalised while the frozen background is retained.

**Definition adopted into this contract (D21):**
`R_bg^k = I^k({A,B,P})` for `k ∈ {W2, W5}` — and for those two measures only. No
`R_bg` is defined or reported for `W1`, `W3`, `W4`, or `W6`, none of which is
decomposed in M08.

**Residual source list (ruling §3.4, verbatim — this is the enumeration the
§5.4(4) gate requires):**

> The residual may contain:
>
> - non-labour-income and demographic variation operating through \(c_{ij}\);
> - tax-benefit mapping heterogeneity not assigned to the three channels;
> - fixed reference/support heterogeneity;
> - any remaining model-fixed heterogeneity;
> - numerical integration noise, which must be separately bounded by the integration gates.
>
> The validation memo must enumerate these sources and separate substantive residual inequality from numerical Shapley arithmetic error.

The validation memo of §6.2 item 2
(`docs/results/FR_P2a_welfare_integration_validation_v1.md`) carries this
enumeration for each of `W2` and `W5`, and separates substantive residual
inequality from numerical Shapley arithmetic error.

### 5.4 The five validation gates (ruling §3.5, verbatim)

**The grand-coalition-zero requirement is withdrawn.** Ruling §3.5, verbatim:

> ### 3.5 Revised validation gates
>
> Replace the grand-coalition-zero requirement with:
>
> 1. **Operator completeness:** all assigned access, ability, and preference arguments are equalised as frozen.
> 2. **Shapley arithmetic:**
>    \[
>    \left|
>    \sum_q\phi_q^k-\left[I^k(\varnothing)-R_{\mathrm{bg}}^k\right]
>    \right|
>    \leq \varepsilon_{\mathrm{Shapley}}.
>    \]
> 3. **Total accounting:**
>    \[
>    \left|
>    I^k(\varnothing)-\left(\phi_A^k+\phi_B^k+\phi_P^k+R_{\mathrm{bg}}^k\right)
>    \right|
>    \leq \varepsilon_{\mathrm{Shapley}}.
>    \]
> 4. **Residual reporting:** `R_bg` is reported in levels and as a share of baseline inequality.
> 5. **No silent renormalisation:** components are not rescaled to force their shares to sum to 100 percent after excluding the residual.
>
> The separate numerical-integration stability tolerance continues to govern the accuracy of each \(I^k(S)\); it is not replaced by the Shapley arithmetic tolerance.

#### 5.4.1 What replaces V8 and V20a/b/c, item by item

The five gates above **replace** the v1 grand-coalition-degeneracy machinery.
The disposition of each superseded check is recorded here and mirrored in the
§5A.8 table, where each carries a **SUPERSEDED** marker and a pointer back to
this subsection.

| v1 check | v2 disposition | Where its content now lives |
|---|---|---|
| **V8** — grand-coalition degeneracy (`I(Ω^k)` ≤ frozen tolerance) | **SUPERSEDED — withdrawn, not re-toleranced.** No gate requires `I^k({A,B,P}) = 0` or `≈ 0` | replaced by gates §5.4(2)–(5); the quantity it tested is now **reported** as `R_bg^k`, not gated to zero |
| **V20a** — analytic degeneracy: resolved equalised `u` block, taste covariates and every `g` factor **hash-identical across households** under `{A,B,P}`, tolerance `1e-9` | **RETAINED — as the mechanical form of gate §5.4(1) operator completeness.** Its household-hash identity of the resolved equalised objects is exactly the executable test that "all assigned access, ability, and preference arguments are equalised as frozen". Tolerance `1e-9` unchanged; failure action unchanged (gate) | gate **§5.4(1)**; assertion transcribed at §5A.8 |
| **V20b** — numerical degeneracy: residual `I(Ω^k)` within a declared simulation tolerance | **SUPERSEDED — RETIRED.** It gated the residual toward zero, which the ruling withdraws. Its `PROPOSED-AT-STAGE-A` declared simulation tolerance is therefore **removed from the Stage-A number list** | nothing replaces it as a gate; integration accuracy of each `I^k(S)` stays with the separate integration machinery (V6, V22, U6, U7) |
| **V20c** — enumeration: every remaining source of cross-household variation enumerated and assigned or escalated; *halt to deputy* if `c_ij` heterogeneity is unassigned | **RETAINED as gate §5.4(4)'s required background-source enumeration**, with its halt trigger **spent**: `c_ij` heterogeneity is now *assigned* — to the fixed background, by the ruling §3.4 residual source list, which names it first. The enumeration duty survives; the escalation it was built to fire no longer has a trigger | gate **§5.4(4)**; source list transcribed verbatim at §5.3 |

**`ε_Shapley` is the frozen U8 convention** — `1e-9 · max(1, |I^k(∅)|)`, per
§3.2a(U8). It governs gates (2) and (3) **only**. The separate
numerical-integration stability tolerance remains governing for each `I^k(S)`, as
the ruling's closing sentence requires and §3.2a(U8)'s scope limit records.

**Gate (5), stated as an executable prohibition.** No reported share is rescaled
so that `φ_A^k`, `φ_B^k`, `φ_P^k` sum to 100 percent with `R_bg^k` excluded. Every
share in §5.5 is taken over `I^k(∅)`, the full baseline, and the four shares
(`φ_A`, `φ_B`, `φ_P`, `R_bg`) therefore sum to 1 up to `ε_Shapley` **by
construction, not by renormalisation**.

### 5.5 Headline quantities and the S-10 opportunity share (ruling §3.6, verbatim)

> ### 3.6 Headline quantities
>
> For the primary `W2` decomposition, report:
>
> \[
> C_{\mathrm{access}}=\phi_A^{W2},
> \]
>
> \[
> C_{\mathrm{opportunity}}=\phi_A^{W2}+\phi_B^{W2},
> \]
>
> \[
> C_{\mathrm{preference}}=\phi_P^{W2},
> \]
>
> \[
> R_{\mathrm{bg}}=R_{\mathrm{bg}}^{W2}.
> \]
>
> The opportunity share used by S-10 is:
>
> \[
> s_{\mathrm{opp}}
> =
> \frac{\phi_A^{W2}+\phi_B^{W2}}
>      {I^{W2}(\varnothing)}.
> \]
>
> Also report:
>
> - access-only share \(\phi_A^{W2}/I^{W2}(\varnothing)\);
> - preference-related share \(\phi_P^{W2}/I^{W2}(\varnothing)\);
> - fixed-background residual share \(R_{\mathrm{bg}}^{W2}/I^{W2}(\varnothing)\).
>
> All contributions are reported signed. Do not suppress a negative contribution and do not reinterpret it causally.
>
> The pre-registered S-10 2-percentage-point trigger applies to \(s_{\mathrm{opp}}\) as defined above.

**Binding reporting rules carried from the above:**

- **Signed contributions.** Every `φ_q^k` is reported with its sign. **A negative
  contribution is not suppressed, not floored at zero, not reported in absolute
  value, and not reinterpreted causally.**
- **No silent renormalisation** (gate §5.4(5)).
- **The 2pp trigger reads on `s_opp`** and on nothing else (D16).
- **The `[access-only, access+ability]` bracket of D6** is now stated in these
  terms: the bracket's endpoints are `φ_A^{W2}/I^{W2}(∅)` and `s_opp`. Reporting
  the bracket rather than a single point remains **mandatory**.
- **Secondary measure.** The same quantity set — `φ_A^{W5}`, `φ_A^{W5}+φ_B^{W5}`,
  `φ_P^{W5}`, `R_bg^{W5}`, and their four shares over `I^{W5}(∅)` — is reported
  for `W5` as the secondary decomposition, *"used to show how attribution changes
  under a different normative reference"* (ruling §3.2). `s_opp` itself, and with
  it the S-10 2pp trigger, is defined on `W2` only.

### 5.6 Execution steps (the operative replacement for v1 §5's numbered list)

1. Evaluate the eight coalitions of the three-channel `{A, B, P}` game
   (§5A.7's coalition table, unchanged) for the **primary `W2`** decomposition,
   yielding `I^{W2}(S)` for all `S ⊆ N`.
2. Compute the exact Shapley contributions `φ_A^{W2}`, `φ_B^{W2}`, `φ_P^{W2}`
   with the §5.3 weights, using the operators of §5A with the resolved operands
   of U11–U14.
3. Form `R_bg^{W2} = I^{W2}({A,B,P})` and verify the five gates of §5.4 at
   `ε_Shapley`.
4. Report the §5.5 headline quantities, all four shares over `I^{W2}(∅)`, signed,
   and the D6 `[access-only, access+ability]` bracket — never a single point.
5. **Repeat 1–4 for `W5` as the secondary decomposition**, reporting how the
   attribution changes under the access-compensated normative reference.
   *(This step replaces v1 §5 item 5, "Repeat for `W2` as the pre-registered
   second check", which is spent: `W2` is now primary.)*
6. `W1`, `W4`, and `W6` are reported in the welfare-family results (§6.3.2 §3.1
   tables) and are **not decomposed**; no M08 Shapley requirement attaches to
   them. *(This replaces v1 §5 item 6's "`W1`/`W5` corroborating interpretation
   only": `W5` is now a decomposed measure, and the corroboration framing no
   longer applies to it.)* The v1 prohibition survives in general form: **no
   measure is used as a numerical reconciliation identity against another.**
7. `W3` is **not** decomposed (§5.1).
8. Every result is model-conditional and non-causal; the preference-related
   component is never labelled "responsibility" (charter §4.3); and `R_bg` is
   never labelled endowment, needs, circumstance, unfairness, or causal (§5.7).

The operators, operands, coalition structure, Shapley weights, and validation
checks referred to in items 1–4 are transcribed in full at **§5A**, which
supersedes any placeholder cross-reference wherever the two differ — **except**
that where §5A and the decomposition-architecture ruling differ, **the ruling
governs** (§5.4.1 records every such point).

### 5.7 Interpretation and the manuscript-caveat plan (ruling §3.7, verbatim)

The paper-facing interpretation is fixed by the ruling and is transcribed here
verbatim as the **manuscript-caveat plan** entry for the decomposition:

> ### 3.7 Interpretation
>
> The paper-facing interpretation becomes:
>
> > The decomposition attributes the part of measured welfare inequality that changes when the model's access, ability, and preference channels are equalised. Inequality remaining after all three equalizations is reported separately as a fixed-background residual, principally reflecting household budget and other frozen heterogeneity outside the three structural labour-market channels.
>
> This preserves the main question while being explicit that the first M08 prototype is not a complete causal decomposition of every determinant of welfare.
>
> A fully specified four-channel decomposition with an endowment/needs operator may be considered only after M08 and LOC4, if the residual is quantitatively material and scientifically worth explaining.

**Labelling prohibition, binding on every manuscript, table, figure, caption, and
restricted artifact this contract authorizes.** `R_bg` is reported **in levels
and as a share**, and is **NEVER** labelled:

- an **endowment** component;
- a **needs** component;
- a **circumstance** component;
- an **unfairness** component;
- a **causal** component.

It is described as *"the inequality remaining after all three modeled structural
channels are equalised while the frozen background is retained"* (§5.3), with the
§5.3 source list attached. The caveat block that carries this into the manuscript
is **§5A.9.5**, which v2 extends with a fourth row for the fixed-background
residual.

---
## 5A. Decomposition operators — verbatim transcription under Goal-1 R-71 / R-72

**Status.** Transcribed 2026-08-06 (documentation-only) under Goal-1 rulings
**R-71** and **R-72**, which ratify the two design memos below. The memos are the
binding source; this section is a verbatim transcription so that the execution
requirements are readable without leaving this file, exactly as §6.3 does for the
U4 ruling. **Where transcription and source could ever diverge, the memos
govern.**

**v2 amendment scope — read this before reading the section.** Under the
decomposition-architecture ruling **§4.10** ("keep the access/ability/preference
operator definitions otherwise unchanged"), **the operator definitions in this
section are UNCHANGED**. v2 touches this section in exactly five places, each
marked inline with **`[v2]`**:

1. every statement that the grand coalition must be degenerate, or that
   exhaustiveness requires `I({A,B,P}) = 0`, is marked **SUPERSEDED** with a
   pointer to §5.3–§5.4 (**§5A.1**, **§5A.6**, **§5A.7**);
2. **V8** and **V20b** are marked SUPERSEDED/RETIRED; **V20a** and **V20c** are
   retained in their new roles under gates §5.4(1) and §5.4(4) (**§5A.8**);
3. the **V1 / V17 / V18** fixed-point assertions are re-anchored to the
   **`W2`/`W5` money-metrics** (**§5A.8**);
4. **V21**'s diagnostic definition is re-anchored to **`W2`** (**§5A.8**,
   **§5A.9.3**), and the opportunity-content definition becomes
   `φ_A^{W2} + φ_B^{W2}` with the S-10 share `s_opp`;
5. the caveat block gains a fourth row for the fixed-background residual
   (**§5A.9.5**), and **§5A.11**'s two open items are closed.

**Where §5A and the ruling differ, the ruling governs** — every such point is
enumerated at §5.4.1 and marked here.

| Register item | Document | sha256 |
|---|---|---|
| **U12** — access-equalisation operand (`g_ref`) | `docs/Missions/JMP_M08_access_equalisation_operand_design_v1.md` | `41372e8e193bf5e9a82f2b1dca184545f4c1c1bd875d281031cdf589f2f3a872` |
| **R9** — ability operator (`B`) and preference operator (`P`) | `docs/Missions/JMP_M08_ability_preference_operators_design_v1.md` | `868e7388ab4a1d64f48933064f204c91f2532a577b49a042941f82012270b419` |

**Nothing in this section is FROZEN.** Stage A owns the freeze.

### 5A.0 The shared core (R9 §1, verbatim)

> Under D1 (ratified), the decomposition unit is the **(factor × argument) cell**. An equalisation operator is therefore not a parameter-block swap but an **argument substitution into a fixed function evaluation**: it replaces the household-specific arguments occupying its assigned cells by frozen reference values, and evaluates the *accepted* functional form at the accepted `θ̂` (handoff §1; charter §5.3, §10). Nothing is re-estimated, and no coefficient is re-fitted.
>
> Both operators act inside the attained-utility core only, as `g_ref` does (U12 §1.1):
>
> ```
> V_i = log Σ_{j∈C_i} exp( u_i(c_ij, ℓ_ij; θ^pref) + log g(j; x_i, θ^opp) − log π(j; x_i) )
> log g = log g^E(·; x_i) + work_j · [ log g^Occ(loc4_j | x_i) + log g^H(h_j) + log g^W(w_j | loc4_j; x_i) ]
> ```
>
> Every measure's reference (own-set baseline for `W^3`, `Ā`, `J`, `o`) and the `c_ij` matrix stay frozen across all coalitions (U12 V2, ratified). `π` is never touched by any operator (U12 V3, ratified). No operator introduces a job package, so the reference-coverage / EUROMOD gate is never re-triggered (U12 V4, ratified; contract §6.1(iii)).

**`[v2]`** The reference-freezing statement above is the operator-level form of
ruling §3.3's fixed-object list and of ruling §3.2's closing sentence (*"it does
not allow the reference itself to move with the equalised channel"*). It is
**unchanged**. Note only that the measures actually decomposed in M08 are `W2`
and `W5`, so the operative frozen references are `W2`'s own-set best-paid
reference and `W5`'s `Ā` (U11) — `W3`'s own-set baseline remains frozen too, but
as a validation object, not a decomposition baseline (§5.1).

### 5A.1 D1 — the decomposition unit and cell table (U12 §2, verbatim)

> **Proposed resolution (D1).** The decomposition unit is the **(factor × argument) cell**, not the parameter block. Each cell of the opportunity density is assigned to exactly one channel:

| Cell | Channel | Ground |
|---|---|---|
| `g^E`: intercept, region dummies, GSUR level | **access** | regional/urbanisation environment is offer-side (charter §4.3 access) |
| `g^E`: education interactions (GSUR×educ and any `educ`-interacted hours/market term) | **ability** | access-purity: education routes exclusively through wage/ability |
| `g^Occ`: dependence on `dgn` | **access** | gender-in-offers is access/compensable |
| `g^Occ`: dependence on `educ3` | **ability** | access-purity |
| `g^H`: hours-band shifters | **access** (degenerate — see §3.4) | employment/hours availability (charter §4.3) |
| `g^W`: `μ_i` via `educ`, `pexp` | **ability** | accepted wage technology; education and experience-via-wages |
| `g^W`: `δ_occ[loc4_j]` occupation mean-shift | **ability** | wage technology, not availability (§5) |
| `g^W`: `σ` (dispersion) | **ability** | wage dispersion (charter §4.3 ability) |
| `u_i`: age-in-leisure, kids, `β_l0`, `θ_l`, `β_c`, `θ_c` | **preference** | tastes (charter §4.3); age-in-leisure per the age split |
| `π` | **none** | sampling artifact (§1.2(b)) |

> Consequences, stated plainly: the **ability** operator becomes "replace `educ` and `pexp` wherever they appear, in `g^W` *and* in the education-assigned cells of `g^E`/`g^Occ`, plus `σ`", and the **access** operator becomes "replace everything else on the offer side, at own education". Under the grand coalition every cell is replaced, every household faces the identical `g`, and the exhaustiveness precondition is testable (V8).

*(The cross-references "§3.4", "§5", "§1.2(b)" inside the quoted table and
paragraph are to U12's own sections, transcribed here at §5A.2 and §5A.5.)*

> **`[v2]` SUPERSEDED CLAUSE — pointer.** The quoted consequence paragraph's final
> clause — *"the exhaustiveness precondition is testable (V8)"* — is **superseded**
> by the decomposition-architecture ruling §3.5, transcribed at **§5.4**. There is
> no longer an "exhaustiveness precondition" in the sense of a required grand-
> coalition zero. What survives, and is unchanged, is the *operator* statement
> immediately preceding it: under `{A,B,P}` every assigned cell is replaced and
> every household faces the identical `g`. **That statement is now tested by gate
> §5.4(1) operator completeness, whose mechanical form is the retained V20a
> household-hash identity** (§5.4.1). Exhaustiveness itself is now the ruling's
> §3.4 identity, `φ_A^k+φ_B^k+φ_P^k = I^k(∅) − R_bg^k`.

**Ratified by R-71** as an amendment to `RURO_welfare_scaffold_design_contract_v2.md`
§7 (name-list → cell routing). **Cell routing is unchanged by v2.**

### 5A.2 The access operator `A` / operand `g_ref` (U12 §3, verbatim) — **UNCHANGED**

> ### 3.1 Construction principle: covariate-reference, not density-averaging
>
> Two constructions are available. **Covariate-reference:** evaluate the *accepted* parametric access factors at a frozen reference argument vector `x̄^acc`. **Distribution-reference:** replace the whole factor by an averaged probability object. The proposal adopts **covariate-reference wherever the accepted object is a parametric index, and distribution-reference only where the accepted object is itself a conditional probability table**.
>
> Reasons: (i) the counterfactual remains a member of the accepted family — it is the offer environment of a well-defined reference worker, and every number in it is `exp` of the accepted index at accepted `θ^opp`, requiring no new estimation (handoff §1; charter §5.3); (ii) it makes the fixed-point identity of V1 (§7) an *exact* check rather than a vacuous one; (iii) it permits the cell-level bookkeeping of §2, which a pooled mixture cannot (see §6.1).
>
> ### 3.2 Employment / market margin `g^E` — **access, pooled**
>
> Replace `x_i` in the access-assigned cells of `g^E` by:
>
> - **Region:** the population-share vector over `drgn1` for the P2a singles sample, substituted for the household's region indicator vector. This sets the region contribution to the **share-weighted mean of the linear index**, which is well defined, unique, and pinned by the data — as opposed to a chosen region, which is not (§6.3). Note explicitly: this is the mean of the index, not the mean of the implied employment probability; the share-weighted-probability variant is pre-registered as a sensitivity, not the baseline.
> - **GSUR:** the sample mean of the accepted `gsur` column over P2a singles.
> - **Education-interacted cells:** *not* replaced (they are ability cells, D1).
>
> Because `g^E` is the only factor present at the non-employment alternative, the operator moves the **employment-availability margin** — the relative weight of the non-employment row against the employed rows — for every household. This is correct: employment availability is named access in charter §4.3.
>
> ### 3.3 Occupation availability `g^Occ` — **access in the sex argument only**
>
> The accepted object is a conditional table `p(loc4 | dgn, educ3)`. For a table, "evaluating at a reference covariate" *is* selecting a different cell. The access-assigned argument is `dgn`; the ability-assigned argument is `educ3`. The operand is therefore the **sex-pooled, education-conditional** table
>
> ```
> p̄(loc4 | educ3)  =  Σ_{s ∈ {m,f}} ω_s(educ3) · p(loc4 | dgn = s, educ3)
> ```
>
> with `ω_s(educ3)` the frozen population sex shares within the education cell, computed once on the P2a singles sample and recorded before execution. Every household of a given `educ3` receives the same occupation-availability distribution regardless of sex; education-conditional structure is left standing for the ability operator to remove.
>
> This single substitution is the operational content of "gender-in-offers is compensable." It is also the cell that LOC4 will move (§8.2).
>
> ### 3.4 Hours availability `g^H` — **access, but empirically degenerate**
>
> The certified hours-band shifters carry no household covariates: `g^H(h_j)` is identical across households. The access operator's action on this cell is therefore the **identity**, and the hours cell contributes exactly zero to the access component.
>
> **This must be stated in the paper, not buried.** Under the certified specification, measured access heterogeneity is generated by region×GSUR employment availability and by sex-differentiated occupation availability — and by nothing else. The access component is a lower bound on offer-side inequality with respect to any hours-availability heterogeneity the specification does not carry. Any `educ`-interacted hours term found in the frozen YAML is an *ability* cell under D1, not an access cell; Stage A must enumerate the hours block against the frozen spec and record the finding.
>
> ### 3.5 Age — **absent by design**
>
> Age enters the certified model twice: as experience in the wage index (ability) and as age-in-leisure in `u_i` (preference). It enters **no access factor**. The operand therefore neither conditions on age nor equalises it. Adding age to the access conditioning set would import either experience (ability) or leisure taste (preference) into access, violating the age split in both directions. Stage A must verify against the frozen spec YAML that no age or experience term appears in any access-assigned cell, and **halt** if one does (charter §6, §11).
>
> ### 3.6 Summary of the conditioning decision

| Coordinate | In `g_ref`'s conditioning set? | Criterion | What the access component then measures |
|---|---|---|---|
| **Sex** | **No — pooled** | gender-in-offers compensable | includes between-sex offer inequality; excludes gender-in-tastes, which stays in `u_i` at own `θ^pref` |
| **Education** | **Yes — held at own** | access-purity: education is ability-only | *within-education* access inequality; education's offer-side content is charged to ability, where the bookkeeping puts it |
| **Region** | **No — pooled to the share-weighted index** | regional environment is named access | includes the full regional/GSUR employment-availability gradient |
| **Age / experience** | **N/A — absent from access** | age split | nothing; verified, not assumed |

> The **headline cut is insensitive to the education row.** Charter §4.3 makes the primary decomposition opportunity-environment vs preferences, with access-vs-ability nested inside. The opportunity operator equalises access *and* ability cells jointly, so wherever education's offer content is charged, it stays inside opportunity. The education decision is consequential only for the nested split — which is exactly the status charter §4.3 and the project role assign to it.

**R-71 dispositions binding on this operator:** R2 (sex-pooling) ratified;
R3 (education routing) ratified; **R4** = share-weighted **index** is the
baseline, share-weighted **probability** is the single sensitivity,
median-region **rejected**; **R5** = `ω_s(educ3)` are within-`educ3` `dwt`
population sex shares; **R6** = **all** operand population references are
`dwt`-weighted (`dwt = db090`), and the unweighted variant is **not run in M08**.

### 5A.3 The ability operator `B` (R9 §2, verbatim) — **UNCHANGED**

> ### 2.1 Assigned cells (from the ratified D1 table)

| Cell | Argument(s) `B` substitutes |
|---|---|
| `g^W`: Mincer location `μ_i = X_i b + δ_occ[loc4_j]` | `educ` dummies, `pexp`, `pexp²` |
| `g^W`: `σ` | none available — degenerate (§2.3) |
| `g^W`: `δ_occ[loc4_j]` | none — coefficients, not arguments (§2.4) |
| `g^E`: education-interacted cells (GSUR×educ, and any `educ`-interacted market/hours term) | `educ` argument slot only |
| `g^Occ`: the `educ3` conditioning argument | `educ3` |

> ### 2.2 Reference objects, precisely
>
> All references are **dwt-weighted** over the accepted P2a singles sample, `dwt = db090` (R6). All are frozen and recorded before execution (handoff §2.1). Exact column names are bound at Stage A against the frozen spec YAML and the accepted engine-ready parquet; the memo states the object, not a guessed column string (charter §6; contract §9).

| Reference object | Definition | Source |
|---|---|---|
| `ē` — education | the dwt-weighted **share vector** over the education dummies (`educL`, `educH`; `educM` omitted), substituted for the household's dummy vector | accepted education dummy columns on the engine-ready singles parquet; weights `db090` |
| `p̄ₑₓₚ` — experience level | dwt-weighted mean of `pexp` | accepted `pexp` column |
| `p̄ₑₓₚ²` — experience square | dwt-weighted mean of `pexp²` (**not** `(p̄ₑₓₚ)²`) | accepted `pexp2` column (or the accepted squared construction, bound at Stage A) |
| `p̃(loc4 \| dgn)` — education-pooled occupation availability | the `educ3`-marginal of the frozen joint table (§2.5) | accepted `p(loc4 \| dgn, educ3)` × dwt joint distribution of `(dgn, educ3)` |

> **Why `E[pexp²]` and not `(E[pexp])²`.** R4 ratified the **share-weighted index** as the baseline convention for the region cell: the reference is the population mean of the *linear index*, not the index at a synthetic mean worker. Substituting `E[pexp]` and `E[pexp²]` separately is the exact analogue — it makes the reference Mincer location equal the dwt-weighted mean of the accepted experience index. Substituting `(E[pexp])²` would evaluate the index at a mean worker and discard the second-moment content of the experience profile, i.e. it is the *probability/level* analogue that R4 designated a sensitivity rather than the baseline. Proposed accordingly: **baseline = index-mean `(E[pexp], E[pexp²])`; single sensitivity = profile-at-mean-worker `(E[pexp], (E[pexp])²)`**, mirroring R4's one-baseline-one-sensitivity pattern (ratification item **S1**).
>
> The same logic gives the education reference: the dwt **share vector** (index-mean) is baseline; the share-weighted-probability variant is the single sensitivity (mirror of R4). Setting education to a *named level* — including `educM`, the omitted category — is rejected (§6, A4), for the reason median-region was rejected.
>
> ### 2.3 `σ`: degenerate, and what that means for the ability component
>
> The certified specification carries **one common `σ`** across households (contract anchors; the wage block is `beta_w0, beta_w_educL, beta_w_educH, beta_w_pexp, beta_w_pexp2, sigma`, all common). There is therefore no household-specific dispersion argument to substitute, and `B`'s action on the `σ` cell is the **identity** — exactly the status of `g^H` in the access operator (U12 §3.4).
>
> **Implication, to be stated in the manuscript rather than buried.** In M08, the ability component contains **no wage-dispersion content whatsoever**. It is a *location*-only ability channel: it measures the money-metric inequality attributable to differences in the education- and experience-driven level of the wage offer distribution (and, via §2.4, the wage consequences of own occupation availability under own vs. reference location), and it is a **lower bound** on ability inequality with respect to any heterogeneity in wage-offer dispersion the certified specification does not carry. This is the direct analogue of the access component's hours-availability lower-bound caveat (U12 §3.4), and it belongs in the same caveat block.
>
> **LOC4 forward statement (handoff §2.3; charter §5.5, §10).** Under the four-density variant, dispersion may become occupation-specific (`σ_occ`). At that point the `σ` cell ceases to be degenerate and `σ_occ` becomes an **ability** coefficient attached to an **access**-assigned availability weight — the same structural configuration `δ_occ` already occupies (§2.4). The boundary restatement is pre-registered now so LOC4 cannot reopen the bookkeeping: occupation *availability* is access; occupation-specific wage *mean and dispersion* are ability; only one of mean and dispersion may carry a given occupation effect (Path-B ruling, no double counting).
>
> ### 2.4 `δ_occ`: untouched, and the single cell where `B` and `A` interact
>
> `δ_occ` is a vector of **common coefficients** indexed by the drawn `loc4_j` on each row. It is not a household argument, so as an argument-substitution matter the ability operator does not touch it: `B` neither replaces `δ_occ` nor re-evaluates the row's `loc4_j`.
>
> The economic consequence must be stated exactly, because it is the one place where the two opportunity operators interact:
>
> - Under **`B` alone**, the household still faces its **own** (sex- and education-conditional) occupation availability, but its wage location no longer depends on its own education or experience. The wage attached to each row still depends on `loc4_j` through `δ_occ`. So `B`'s effect includes the wage consequences of the household's *own* occupation-availability composition, evaluated at the reference Mincer location.
> - Under **`A` alone** (U12), the household faces the sex-pooled availability but keeps its own Mincer location, so `A`'s effect includes the wage consequences of *reweighted* availability at own location.
> - The residual — the interaction between availability weights and `δ_occ` — is exactly the term neither operator can claim alone. **Shapley symmetry is what allocates it**, splitting it evenly between the access and ability marginal contributions across orderings. This is the substantive reason order-independence is not a formality in this application, and it should be said in the paper: the access/ability split of the occupation channel's wage content is an artefact of the Shapley symmetry axiom, not an identified quantity.

> **`[v2]` Terminology guard.** The word "residual" in §2.4 above denotes the
> `A`–`B` **interaction term** that Shapley symmetry allocates. It is **not**
> `R_bg`, the fixed-background residual of §5.3/D21. The two are distinct objects
> and must not be conflated in code, tables, or prose.

### 5A.4 The frozen joint occupation object `Π` and its four conditionals (R9 §2.5, verbatim) — **UNCHANGED**

> `p(loc4 | dgn, educ3)` is a conditional table whose two conditioning arguments are assigned to different channels: `dgn` → access (U12 §3.3), `educ3` → ability (D1). The two operators must therefore act on the same object without colliding.
>
> **Proposed construction.** Freeze one joint object,
>
> ```
> Π(loc4, dgn, educ3) = π_dwt(dgn, educ3) · p̂(loc4 | dgn, educ3)
> ```
>
> with `π_dwt` the dwt-weighted population distribution of `(dgn, educ3)` on the P2a singles sample and `p̂` the accepted conditional table. Each operator then **selects the appropriate conditional of `Π`**, indexed by which conditioning coordinates remain at own value:

| Coalition state | Occupation object faced |
|---|---|
| neither `A` nor `B` | `p̂(loc4 \| dgn_i, educ3_i)` — accepted baseline |
| `A` only | `p̄(loc4 \| educ3_i)` — sex-pooled within education (U12 §3.3) |
| `B` only | `p̃(loc4 \| dgn_i)` — education-pooled within sex |
| `A` and `B` | `p̄̄(loc4)` — the dwt-weighted marginal |

> This formulation is **equivalent to** R5's ratified weights (`ω_s(educ3) = π_dwt(s | educ3)`) and makes composition **path-independent by construction**: applying `A` then `B` and `B` then `A` both yield `p̄̄(loc4)`, because both are conditionals of one joint object rather than sequentially re-weighted mixtures. Defining the pooling weights instead as free, step-specific mixtures would make the order matter and would break the commutation property §4.3 relies on. Checked by **V14**.
>
> The joint uses only accepted objects: the accepted conditional table and the accepted covariate distribution under `db090`. It is **not** the empirical joint of realised occupations, which is choice- and selection-contaminated (U12 §6.4).

### 5A.5 GSUR × educ slot table and the mirror guards — **UNCHANGED**

#### 5A.5.1 Interaction terms: shared cell, disjoint argument slots (R9 §2.6, verbatim)

> The GSUR×education cells of `g^E` are a product of an access-assigned argument (`gsur`) and an ability-assigned argument (`educ`). Under D1 the *cell* is shared but the *argument slots* are not:

| Coalition state | GSUR×educ term evaluated at |
|---|---|
| baseline | `gsur_i × educ_i` |
| `A` only | `ḡsur × educ_i` |
| `B` only | `gsur_i × ē` |
| `A` and `B` | `ḡsur × ē` |

> Each operator writes only its own slot. This is not double counting — each changes a different input — and it is why the operators commute (§4.3). Note that `ḡsur` here is the U12-ratified dwt-weighted GSUR mean, unchanged.

#### 5A.5.2 Access-side one-line rule (U12 §5, verbatim)

> **One-line rule for the frozen contract:** *access moves the measure over job packages; ability moves the wage map defined on job packages; neither may write into the other's factor.*

The operational statement this rule rests on, also from U12 §5, verbatim:

> **The operational statement of the boundary.** Under the access operator, the per-row wage term `log g^W(w_j | loc4_j; x_i)` is **not re-evaluated**. It is read from the accepted per-row construction unchanged. The access operator changes only which rows carry weight. This is checkable bitwise (V7) and is the sharpest available non-double-counting test.

#### 5A.5.3 Ability-side mirror guard (R9 §2.7, verbatim)

> > **The ability operator must not alter occupation-availability weights (the `dgn` argument of `g^Occ`) or any access-assigned cell.**
>
> Enforced bitwise by **V15**.

### 5A.6 The preference operator `P` (R9 §3, verbatim) — **UNCHANGED, one clause superseded**

> ### 3.1 What is heterogeneous in `u_i`, and the necessary distinction
>
> `u_i(c_ij, ℓ_ij; θ^pref)` carries **two** sources of cross-household heterogeneity in the singles P2a application, and the operator must treat them differently:
>
> **(a) Covariate arguments** — the taste shifters entering the leisure term: `age_norm`, `age_norm2`, the education-in-leisure dummy (`beta_l_educH_*`), and the children term (`beta_l_nkids_sf`). These are substituted by dwt-weighted references, exactly as `A` and `B` substitute theirs. **The operator substitutes covariate arguments; it never re-estimates a coefficient** (charter §5.3, §10).
>
> **(b) Group-specific coefficient blocks** — singles male and singles female carry separate preference blocks (`beta_c_sm/sf`, `theta_c_*`, `beta_l0_sm/sf`, `theta_l_sm/sf`, `beta_l_age_*`, `beta_l_age2_sm/sf`, `beta_l_nkids_sf`). This is **gender-in-tastes**, which the bookkeeping assigns to preference and declares non-compensable. Non-compensable means *the paper does not compensate it*; it does **not** mean the preference channel excludes it. If `P` leaves the group-specific blocks standing, gender-in-tastes survives all three operators, the grand coalition is not degenerate, and exhaustiveness fails (charter §9.8; V8's precondition).

> **`[v2]` SUPERSEDED CLAUSE — pointer.** The final sentence's consequence — *"the
> grand coalition is not degenerate, and exhaustiveness fails (charter §9.8; V8's
> precondition)"* — is **superseded** by the decomposition-architecture ruling
> §3.4–§3.5, transcribed at §5.3–§5.4. Under v2, a non-degenerate grand coalition
> is **not** an exhaustiveness failure: `I^k({A,B,P})` is *reported* as `R_bg^k`,
> and exhaustiveness is the ruling's §3.4 identity. **The design conclusion the
> clause was used to justify is unaffected and stands unchanged:** step (b) is
> retained, because gender-in-tastes is a preference-assigned source and the
> preference operator must equalise its own assigned arguments — which is now
> enforced by gate §5.4(1) operator completeness (retained V20a). Leaving the
> group blocks standing would leave a preference-assigned source unequalised and
> **fail gate §5.4(1)**, and would additionally mis-load `R_bg` with content that
> belongs to `P`. Charter §9.8's acceptance gate ("Shapley decomposition is
> exhaustive") is re-anchored onto the §5.4(2)–(3) identities for `W2` and `W5`.

> ### 3.2 Covariate references (step a)
>
> All dwt-weighted (`db090`), index-mean convention per R4, frozen and recorded before execution:

| Reference | Definition |
|---|---|
| `āge` | dwt-weighted mean of `age_norm` |
| `āge²` | dwt-weighted mean of `age_norm2` — **not** `(āge)²`, per the R4 index-mean convention (§2.2, S1) |
| `ēduc_leisure` | dwt-weighted share of the education-in-leisure dummy |
| `n̄kids` | dwt-weighted mean number of children |

> **Age-in-leisure is equalised here**, per the age split: age enters ability via experience-in-wages (`B`, §2.2) and preference via age-in-leisure (`P`), and each channel equalises its own occurrence. Age appears in no access cell (U12 §3.5, verified at Stage A).
>
> **Education appears in two channels, and this is not a violation of access-purity.** Access-purity governs the *opportunity side*: it forbids education from being counted as access, which is why D1 routes the education arguments of `g^E` and `g^Occ` to ability. Education-in-*leisure* is a taste shifter occupying a `u_i` cell, and D1 assigns `u_i` cells to preference. The structure is identical to the ratified age split — one variable, two cells, two channels, distinguished by the cell it occupies, never double counted because each occurrence is substituted exactly once by exactly one operator. The normative content is real and should be ratified explicitly (item **S3**): under this routing, education-correlated *taste* differences are preference-classified and therefore not compensated.
>
> ### 3.3 The pinned-preference switch: `held`, and non-binding in M08
>
> Contract §7 exposes `decomposition_readiness.preference_equalisation_pinned_switch: held | swapped`, default `held`; R-71 ratifies `held`. Under `held`, the pinned coordinates `theta_l_m` and `beta_ll` are **kept at their pinned values under preference equalisation** rather than swapped for the reference preference. So `held` *does* constrain the preference operand: it removes those two coordinates from step (b)'s substitution map.
>
> **But in M08 the constraint is vacuous.** `theta_l_m` is the couples-male leisure Box-Cox exponent and `beta_ll` is the household leisure interaction (`= 0`); both are couples-side objects among the 10 pins of the certified pooled 47-coordinate specification, and neither enters a singles row's `u_i`. Under charter §5.1 (singles only), `held` therefore has no numerical consequence in M08 — a degenerate switch, in the same category as `σ` (§2.3) and hours availability (U12 §3.4). Contract §7's warning that the switch "sizes the couples preference component and therefore the couples opportunity share" is a couples statement and is not imported (charter §2).
>
> Required disposition: the flag is asserted as `held` in the resolved config for provenance, its non-binding status in M08 is recorded in the validation memo, and **Stage A must verify that neither pinned coordinate enters any singles row's `u_i` and halt if one does** (charter §6, §11).
>
> ### 3.4 Two boundary-active preference coordinates
>
> The accepted vector carries two **active upper bounds at 1.0**: `beta_l_age2_sm` and `beta_l_age2_sf` — the age² leisure coefficients, excluded from the covariance object with literal `NA` (handoff §1; the recorded Phase-5 treatment). Two consequences:
>
> 1. Whichever group block is selected in step (b), the reference preference **contains a bound-active coefficient**. No inferential claim about the preference component may be routed through `beta_l_age2_*` without boundary-aware inference (handoff §2.2).
> 2. However, `P` equalises `age_norm2` in the same move. Once the age² argument is common across households, the bound-active coefficient multiplies a common value and contributes **nothing to cross-household variation** in the equalised state. So this particular exposure is largely neutralised on the coalition side — which is worth reporting, because it narrows the Tier-2 exposure of the preference component to `beta_l0_sm` (§5.3).

**R-72 disposition of the step-(b) reference block:** see §5A.9.1.

### 5A.7 Coalition table and exact Shapley weights (R9 §4.1–4.2, verbatim)

> ### 4.1 The eight coalitions
>
> Let `A` = access, `B` = ability, `P` = preference, and let `I(S)` be the inequality of the money-metric welfare vector `Ω^k` when the channels in `S` are equalised. Every coalition is a composition of the three operators applied to the *same* accepted core, with references frozen (U12 V2) and `π` and `c_ij` untouched.

| # | `S` | Operator composition | Role — **`[v2]` column amended for row 8 only** |
|---|---|---|---|
| 1 | `∅` | identity | baseline `I^k(∅)`; the total being decomposed |
| 2 | `{A}` | `g_ref` access cells; own educ/pexp; own tastes | access-only marginal base |
| 3 | `{B}` | `ē, p̄ₑₓₚ, p̄ₑₓₚ²`; `p̃(loc4\|dgn)`; own access; own tastes | ability-only marginal base |
| 4 | `{P}` | reference taste covariates + reference group block; own `g` | preference-only marginal base |
| 5 | `{A,B}` | full opportunity equalisation; `p̄̄(loc4)`; own tastes | **headline opportunity coalition** (charter §4.3) |
| 6 | `{A,P}` | access + preference; own wage technology arguments | ability-residual coalition |
| 7 | `{B,P}` | ability + preference; own access | access-residual coalition |
| 8 | `{A,B,P}` | grand coalition | **`[v2]`** **the fixed-background residual `R_bg^k = I^k({A,B,P})`** (D21, ruling §3.4). *v1's role text — "degeneracy target; V8/V20 precondition" — is **SUPERSEDED**: this coalition is **not** required to be zero, is **not** a degeneracy target, and is **reported**, in levels and as a share, under gate §5.4(4)* |

**`[v2]` The coalition enumeration, the operator compositions, and rows 1–7 are
UNCHANGED.** Only row 8's *role* changes, and only in what is done with the
number — not in how the coalition is constructed. The eight coalitions are
evaluated for **`W2`** (primary) and again for **`W5`** (secondary); `I^k(S)` is
read for `k ∈ {W2, W5}` (§5.6).

> ### 4.2 Exact Shapley weights
>
> For `n = 3` channels, the contribution of channel `k` is
>
> ```
> C_k = Σ_{S ⊆ N\{k}}  [ |S|! · (3 − |S| − 1)! / 3! ] · [ I(S) − I(S ∪ {k}) ]
> ```
>
> with weights, equivalently the average over the `3! = 6` elimination orderings:

| `\|S\|` | number of such `S` | weight per term |
|---|---|---|
| 0 | 1 | `2!/3! = 1/3` |
| 1 | 2 | `1!·1!/3! = 1/6` each |
| 2 | 1 | `2!/3! = 1/3` |

> Weights sum to 1 for each `k`. Telescoping across orderings gives `C_A + C_B + C_P = I(∅) − I({A,B,P})`, so **exhaustiveness holds if and only if `I({A,B,P}) = 0`** — the precondition of V8, and the reason §4.4 and §5.4 matter.

> **`[v2]` SUPERSEDED CLAUSE — pointer, and what survives.** The weights, the
> formula, and the telescoping identity `C_A + C_B + C_P = I(∅) − I({A,B,P})` are
> **correct and unchanged** — indeed that identity is exactly the ruling's §3.4
> first identity, `φ_A^k+φ_B^k+φ_P^k = I^k(∅) − R_bg^k`, once `R_bg^k` is named.
> What is **SUPERSEDED** is only the sentence that follows from it in R9's framing:
> *"exhaustiveness holds if and only if `I({A,B,P}) = 0`"*. Under the
> decomposition-architecture ruling §3.4–§3.5, transcribed at **§5.3–§5.4**,
> **exhaustiveness is the identity itself**, `I^k(∅) = φ_A^k+φ_B^k+φ_P^k+R_bg^k`,
> checked to `ε_Shapley` — *"This is the M08 exhaustiveness rule"* — and
> `I^k({A,B,P})` is **not required to be zero**. R9 §4.4 and §5.4's motivation is
> correspondingly disposed of: §4.4's `c_ij` grand-coalition residual is item S6,
> closed at §7.3(b).

**Commutation (R9 §4.3), verbatim — UNCHANGED:**

> **Claim.** For any `S`, `I(S)` is independent of the order in which the operators in `S` are applied.
>
> **Justification.** Under D1 each operator substitutes values into a set of argument slots of a fixed evaluated function; the slot sets assigned to the three channels are pairwise disjoint. Substituting into disjoint slots of a function evaluation is order-independent — it is not composition of maps on a shared state, it is assembling one argument tuple. Two cells are *shared* across channels, and both are handled so that commutation survives:
>
> - **GSUR×educ** (§2.6): a product of two slots, one per channel; each operator writes only its own slot.
> - **The occupation table** (§2.5): both operators select a conditional of one frozen joint `Π`, indexed by which conditioning coordinates remain at own; the selection is path-independent by construction.
>
> There is one asymmetry worth naming: `P`'s step (b) substitutes a *coefficient block*, not an argument. It still commutes with `A` and `B`, because `θ^pref` occupies no cell either operator touches (`A` and `B` act only inside `log g`). Asserted by **V19**.

---
### 5A.8 Validation checks V1–V23, with R-71 / R-72 tolerances and the v2 amendments

Assertions and failure actions are transcribed **verbatim** from U12 §7 (V1–V13)
and R9 §7 (V14–V23). The **Tolerance / status** column records the R-71 and
R-72 dispositions, **plus the v2 dispositions marked `[v2]`**.

**`[v2]` Summary of what changes in this table, and nothing else changes:**
**V1, V17, V18** are re-anchored to the `W2`/`W5` money-metrics; **V8** is
SUPERSEDED (withdrawn); **V20a** is RETAINED as the mechanical form of gate
§5.4(1); **V20b** is SUPERSEDED and RETIRED; **V20c** is RETAINED as gate
§5.4(4)'s background-source enumeration with its halt trigger spent; **V21** is
re-anchored onto `W2`. **V2, V3, V4** — the `c_ij` / `π` / support / reference
invariance gates that ruling §4.8 requires be preserved — are **CONFIRMED
UNCHANGED**. V5, V6, V7, V9–V16, V19, V22, V23 are unchanged.

| # | Check | Assertion (verbatim) | Tolerance / status | On failure (verbatim) |
|---|---|---|---|---|
| **V1** | Fixed point / idempotence | For a household (or synthetic test row set) whose access-assigned arguments equal `x̄^acc`, the access operator returns `V_i` and every `Ω_i^k` unchanged to ≤1e-12. | **`1e-12`** (R-71 R7). **`[v2]` RE-ANCHORED:** "every `Ω_i^k`" is evaluated on the **decomposed money-metrics `k ∈ {W2, W5}`**, which are the measures the fixed point must hold for. `Ω_i^{W3}` may additionally be checked as a validation object (§5.1) but is not the anchor | Gate the run. |
| **V2** | Reference coalition-invariance | Each measure's reference construction (own-set baseline for `W^3`, `Ā`, `J`, `o`) and the `c_ij` matrix are hash-identical across all eight coalitions. | **exact** (hash-identical). **`[v2]` UNCHANGED — confirmed** as the operative form of ruling §3.3's fixed-object list and ruling §3.2's "references frozen across coalitions" | Gate. Prevents the reference co-moving with the channel and cancelling the effect. |
| **V3** | π-invariance | The `prior` column is hash-identical across all eight coalitions. | **exact** (hash-identical). **`[v2]` UNCHANGED — confirmed** (ruling §3.3, `π` fixed) | Gate (contract §3.1). |
| **V4** | No new package | Alternative support, row count, and `c_ij` hash unchanged under every coalition ⇒ the reference-coverage / EUROMOD gate (contract §6.1(iii), W3 Gate 4) is not re-triggered, and `abar_j_o_required` is unchanged. | **exact** (hash-identical). **`[v2]` UNCHANGED — confirmed** (ruling §3.3, `c_ij` and alternative support fixed) | Gate; a failure means the operand has silently become a set-substitution. |
| **V5** | Density integrity | `p̄(loc4 \| educ3)` sums to 1 within each education cell; counterfactual `log g` finite on every row; count of non-finite = 0. | as stated in the assertion | Gate. |
| **V6** | Counterfactual ESS | Re-run the contract §6.1(ii) ESS diagnostic (`ESS_i`, max normalised weight) under **every non-baseline coalition**. The counterfactual changes the IS *target* while the proposal is unchanged, so baseline ESS does not transfer. Baseline singles ESS is already weak (W3 gate report: median 20.3 / 18.8; 1,918/2,243 and 2,493/2,764 below the threshold of 30). | ESS threshold **30** (ratified); **materiality/escalation number PROPOSED-AT-STAGE-A**. **`[v2]`** this is one of the two surviving Stage-A numbers (§8.4) and is part of the *separate integration machinery* the ruling §3.5 keeps governing over each `I^k(S)` | Apply the frozen escalation rule to the counterfactual, not only the baseline. If the flagged set widens materially and `V_i^dir` remains blocked, **halt** (charter §11). |
| **V7** | No double counting with the wage/occupation technology | (a) the 47 coordinates form an exact partition over preference/ability/access cells — no coordinate in two channels, none omitted; (b) the per-row `log g^W` contribution is **bitwise identical** between baseline and access-equalised runs, confirming `δ_occ`, `μ_i`, `σ` are untouched by the access operator. | (a) exact partition; (b) **bitwise** | Gate. Membership is frozen and unchanged after results (charter §9.10). |
| **V8** | Grand-coalition degeneracy | ~~With access+ability+preference all equalised, `I(Ω^k)` ≤ the frozen tolerance.~~ | **`[v2]` SUPERSEDED — WITHDRAWN.** Replaced by the five gates of **§5.4** (ruling §3.5), which *"Replace the grand-coalition-zero requirement"*. **No gate requires `I^k({A,B,P}) = 0` or `≈ 0`.** The quantity V8 tested is now **reported** as `R_bg^k` under gate §5.4(4). v1's already-recorded "SUPERSEDED by V20a/b/c" is itself superseded — see §5.4.1 | ~~Record the residual and halt; do not renormalise silently.~~ **`[v2]`** the surviving half of this action is now gate §5.4(5): **do not renormalise silently**. The residual is recorded, not halted on |
| **V9** | Sex-pooling audit | Under access equalisation, the between-sex difference in mean counterfactual access index is exactly zero. | exact (as stated) | Report; a non-zero value means a sex-conditioned cell was missed. |
| **V10** | Directional sanity (reported, not gated) | Households whose own access index is below the reference in every access cell weakly gain. | not gated | Report. Not a theorem once occupation composition interacts with own wage technology; gating it would be an invented identity. |
| **V11** | Determinism | Bit-for-bit reproducible on re-run given identical inputs (mirrors contract §5 Step 1(d)). | **exact** (bit-for-bit) | Gate. |
| **V12** | Block-count reconciliation | The W3 gate report records `welfare.blocks` as preference 20 / ability 6 / access 23 = **49 names** against a **47**-coordinate certified vector. Stage A must reconcile the arithmetic against the frozen spec YAML and the accepted θ̂ (handoff §1) and **halt** if the declared membership is not an exact partition. That report was also produced on the pooled couples-inclusive build at working-tree HEAD `7cac2e3`; per charter §2 its membership counts are indicative for P2a singles and are not imported as validated. | exact partition | *(halt, per the assertion)* |
| **V13** | Occupation-term separability | Stage A must bind each factor of §1.1 to the exact engine term (`log_h`, `log_w`, `log_market`, and wherever the occupation contribution is assembled) and **halt** if the occupation contribution is not separable from the market index in the accepted production path — the access operator is not implementable without that separation. | binding check | *(halt, per the assertion)* |
| **V14** | Operator commutation / mixture path-independence | For every coalition, applying the constituent operators in both (all) orders yields bitwise-identical resolved objects; the `{A,B}` occupation object equals the frozen `p̄̄(loc4)`; the GSUR×educ term matches the §2.6 table cell-for-cell. | **exact** (bitwise) | Gate. A failure means the D1 slot disjointness is violated somewhere. |
| **V15** | Ability V7-analogue (mirror guard) | Under `B`, the following are bitwise invariant per row: the `dgn` conditioning of the occupation availability weights, the region/GSUR level cells of `g^E`, `g^H`, `π`, and `c_ij`. | **exact** (bitwise) | Gate. This is the operational form of §2.7. |
| **V16** | Preference V7-analogue | Under `P`, `log g` is bitwise invariant per row in **all** factors, and `c_ij` and `π` are bitwise invariant. | **exact** (bitwise) | Gate. |
| **V17** | Ability fixed point | A household (or synthetic row set) at `(ē, p̄ₑₓₚ, p̄ₑₓₚ²)` and in the reference education cell sees `V_i` and every `Ω_i^k` unchanged to ≤ `1e-12` (mirror of V1's ratified tolerance). | **`1e-12`**. **`[v2]` RE-ANCHORED** to the `W2`/`W5` money-metrics, as V1 | Gate. |
| **V18** | Preference fixed point | A household at the reference taste covariates **and** in the reference group block sees `V_i` and every `Ω_i^k` unchanged to ≤ `1e-12`. Requires that the reference group block be an actual accepted block — which is why P2 fails. | **`1e-12`**. **`[v2]` RE-ANCHORED** to the `W2`/`W5` money-metrics, as V1 | Gate. |
| **V19** | No re-estimation, mechanically asserted | The 47-coordinate `θ̂` is bitwise identical in every coalition, with the sole exception of the declared step-(b) substitution; the substitution map is hash-recorded and is a pure selection among accepted coordinates. | **exact** (bitwise) | Gate (charter §5.3, §10). |
| **V20a** | **`[v2]` RETAINED — now the mechanical form of gate §5.4(1) operator completeness** | resolved equalised `u` block, taste covariates, and every `g` factor **hash-identical across households** under `{A,B,P}` | **`1e-9`** (unchanged). **`[v2]`** re-titled: this is no longer an "analytic degeneracy" check on inequality; it is the executable test that *"all assigned access, ability, and preference arguments are equalised as frozen"* (ruling §3.5(1)). The household-hash identity of the **resolved equalised objects** is retained exactly as written | gate (unchanged) |
| **V20b** | ~~Numerical degeneracy~~ | ~~residual `I(Ω^k)` within a declared simulation tolerance derived from the counterfactual ESS, not `1e-9`~~ | **`[v2]` SUPERSEDED — RETIRED.** It gated the residual toward zero, which ruling §3.5 withdraws. **Its PROPOSED-AT-STAGE-A declared simulation tolerance is removed from the Stage-A number list** (§8.4). Integration accuracy of each `I^k(S)` remains governed by the separate integration machinery (V6, V22, U6, U7) | *(no gate)* |
| **V20c** | **`[v2]` RETAINED — now gate §5.4(4)'s required background-source enumeration** | every remaining source of cross-household variation enumerated and assigned or escalated | constructive, no computation. **`[v2]`** the enumeration duty survives and is discharged against the **verbatim ruling §3.4 residual source list transcribed at §5.3**, reported with `R_bg^k` in levels and as a share | **`[v2]` halt trigger SPENT.** v1's *"halt to deputy if `c_ij` heterogeneity is unassigned"* no longer has a trigger: `c_ij` heterogeneity **is** assigned — to the fixed background, by ruling §3.4, which names *"non-labour-income and demographic variation operating through \(c_{ij}\)"* first in the residual source list. A source found that is **neither** an `{A,B,P}` cell **nor** on the §5.3 list is still escalated |
| **V21** | Level-of-aggregation gap | Report `C_A + C_B`, `C_O^(2)`, and their difference. Diagnostic, **not** a gate. | diagnostic (not a gate). **`[v2]` RE-ANCHORED ONTO `W2`:** the quantities are `φ_A^{W2} + φ_B^{W2}`, the two-channel `C_O^{(2),W2}`, and their difference. It is reported for the **primary measure**; reporting it for `W5` as well is permitted but not required | Report; interpret as aggregation level, never as an error. |
| **V22** | Counterfactual ESS for the mirrors | Extend the ratified U12 V6 (threshold 30) to the `{B}`, `{P}`, `{A,B}`, `{A,P}`, `{B,P}`, `{A,B,P}` coalitions: the IS target changes under each while the proposal does not. The Stage-D `V_i^dir` cross-check at the frozen 0.5-nat tolerance (R-71) applies to the flagged subsets **of each coalition**, not only the baseline. | ESS threshold **30**; `V_i^dir` tolerance **0.5 nats** (R-71, = U7); **per-coalition materiality/escalation number PROPOSED-AT-STAGE-A**. **`[v2]`** the second of the two surviving Stage-A numbers (§8.4); part of the separate integration machinery ruling §3.5 keeps governing | Apply the frozen escalation rule per coalition; halt if the flagged set widens beyond the Stage-A materiality number. |
| **V23** | Reference-group pre-registration | The `θ̄^pref` group selection and its mirror sensitivity are recorded, with timestamp and hash, **before** any coalition value is computed. | gate | Gate (charter §5.7, §6; §5.3 of this memo). |

**V20 as a whole (R9 §7, verbatim) — retained as history:**

> **V20** | **Degeneracy, split three ways** | **a)** resolved equalised `u` block, taste covariates, and every `g` factor hash-identical across households under `{A,B,P}` (tolerance `1e-9`); **b)** residual `I(Ω^k)` within a declared simulation tolerance derived from the counterfactual ESS, not `1e-9`; **c)** every remaining source of cross-household variation enumerated and assigned or escalated. | a) gate; b) gate at the declared tolerance; c) **halt to deputy** if `c_ij` heterogeneity is unassigned. Supersedes V8's single-tolerance form (item S4).

> **`[v2]` Disposition of the V20 block as written above.** Its framing —
> "degeneracy, split three ways" — is **superseded** by ruling §3.5. (a) survives
> as gate §5.4(1); (b) is retired; (c) survives as gate §5.4(4)'s enumeration with
> its halt trigger spent. The block is retained here verbatim so the v1 → v2
> transition is auditable, not because any part of its *degeneracy* framing is
> still operative. See **§5.4.1** for the item-by-item map.

**Numbers marked PROPOSED-AT-STAGE-A** — i.e. not frozen by R-71/R-72 and to be
fixed at the Stage-A freeze. **`[v2]` the list is now TWO, not three:** the
**V6** counterfactual-ESS materiality and escalation number, and the **V22**
per-coalition materiality number. **V20b's declared simulation tolerance is
removed — V20b is retired.**

### 5A.9 R-72 ratifications

#### 5A.9.1 Reference preference block (R9 item S2) — resolved · **UNCHANGED**

The `θ̄^pref` group-block selection of the preference operator's step (b) is
ratified as the **singles-female block**. The **singles-male block is the
single pre-registered mirror sensitivity**. Both are recorded under **V23**
(timestamp and hash) **before any coalition value is computed**, per R9 §5.3:

> 1. The reference-group choice is frozen at Stage A, before any coalition value is computed (charter §5.7, §6).
> 2. Both directions are reported (§7, item S2: baseline group + the mirror as the single sensitivity), so the exposure is visible either way.

The hazard this closes is R9 §5.3, verbatim:

> If the singles-**female** block is selected as `θ̄^pref`, then `θ̄^pref` is invariant to scenario 2's perturbation of `beta_l0_sm` (and `beta_l0_sf` is a vigilance coordinate, not perturbed — handoff §2.5). The reference-group choice therefore **changes the S-10 exposure of the preference component**, and a choice made after seeing scenario results could suppress the very sensitivity S-10 is designed to reveal.

Because the ratified reference block is the female one, the male mirror
sensitivity is the leg that carries the `beta_l0_sm` exposure directly; it is
therefore **mandatory**, not optional, and is reported alongside the baseline.
Coefficient averaging remains rejected (R9 §6, P2).

#### 5A.9.2 Index-mean convention (R9 item S1) — ratified · **UNCHANGED**

Baseline is the **index-mean**; each has a **single sensitivity**:

| Argument | Baseline (ratified) | Single sensitivity |
|---|---|---|
| experience | `(E[pexp], E[pexp²])` | profile-at-mean-worker `(E[pexp], (E[pexp])²)` |
| education (ability) | dwt **share vector** | share-weighted **probability** |
| age-in-leisure (preference) | `āge` and `āge²` as separate dwt means | *(mirrors the experience sensitivity)* |
| region (access, R-71 R4) | share-weighted **index** | share-weighted **probability** |

Named-level references (including the omitted category `educM`) and
median-region remain **rejected**.

#### 5A.9.3 Opportunity content (R9 item S5) — **`[v2]` RE-ANCHORED ONTO `W2`**

**`[v2]`** Opportunity content is **defined** as `φ_A^{W2} + φ_B^{W2}` from the
primary three-channel game on the **primary measure `W2`** — which is precisely
the ruling §3.6 headline quantity `C_opportunity`. The corresponding
**pre-registered share is `s_opp = (φ_A^{W2} + φ_B^{W2}) / I^{W2}(∅)`**, and it
is the quantity the S-10 2-percentage-point trigger reads on (D16, §5.5). The
two-channel value `C_O^{(2)}` and the gap remain the **V21** diagnostic,
computed on `W2`. R9 §4.5, verbatim (its `C_A + C_B` is `φ_A + φ_B`; its `I` is
`I^k(∅)`):

> Charter §4.3 makes the headline cut opportunity-vs-preference with access-vs-ability nested inside; charter §7 Stage F instructs evaluating the eight coalitions of the **three-channel** game and reporting "access-only and access-plus-ability shares". Under the three-channel game, `C_A + C_B + C_P = I` exactly, so `C_A + C_B` is a coherent exhaustive definition of opportunity content. But it is **not** equal to the opportunity value of the two-channel game `{opportunity = A∪B, preference}`:
>
> ```
> C_O^(2)  =  ½[ I(∅) − I({A,B}) ] + ½[ I({P}) − I({A,B,P}) ]     ≠     C_A + C_B   in general
> ```
>
> The two differ in how the three-way `A–B–P` interaction is allocated. Proposed disposition (item **S5**): adopt the charter's three-channel game as primary, **define** opportunity content ≡ `C_A + C_B`, and report `C_O^(2)` and the gap `|C_A + C_B − C_O^(2)|` as a pre-registered diagnostic (**V21**), described as a level-of-aggregation gap and not as an error. Pre-registering the definition before results exist is required by charter §5.7.

> **`[v2]` Reading correction inside the quoted passage.** The quoted sentence
> *"Under the three-channel game, `C_A + C_B + C_P = I` exactly"* holds under the
> v1 premise that the grand coalition is degenerate. Under **§5.3**, the exact
> statement is `φ_A^k + φ_B^k + φ_P^k = I^k(∅) − R_bg^k`. **This does not disturb
> item S5's disposition**: `φ_A^{W2} + φ_B^{W2}` remains a coherent, exactly
> computed definition of opportunity content, and `C_O^{(2)}`'s formula above —
> which already carries the `I({A,B,P})` term explicitly — is unchanged and
> correct as written. Only the claim that the three components exhaust `I^{W2}(∅)`
> without a residual is corrected: they exhaust `I^{W2}(∅) − R_bg^{W2}`. **The
> share denominators of §5.5 are the full `I^{W2}(∅)`**, so the four reported
> shares (`φ_A`, `φ_B`, `φ_P`, `R_bg`) sum to 1 and **no renormalisation is
> applied** (gate §5.4(5)).

The gap is reported as a **level of aggregation**, never as an error.

#### 5A.9.4 Expected-positive Tier-2 posture (R9 item S8) — ratified · **UNCHANGED**

Boundary-aware / resampling inference is scheduled as the **anticipated path**
for the ability and preference components, not treated as an exception. R9
§5.4, verbatim:

> - The **ability** component loads on `beta_w_pexp2` **by construction** — the flagged coordinate is a coefficient of the ability operator's own reference index.
> - The **preference** component loads on `beta_l0_sm` by construction if the male block is the reference, and through coalition values in any case.
>
> Handoff §2.2 makes boundary-aware or resampling inference mandatory if "any welfare or decomposition functional loads materially on one" of the flagged coordinates. The first-gate material-loading assessment should therefore be **expected to return positive for at least one component**, and Tier-2 should be scheduled as the anticipated path rather than treated as an exception. Materiality remains a numerical question answered at the first gate, not asserted here. `beta_l0_sf` is monitored throughout with no bound asserted absent an accepted record (handoff §2.5). The two W-4 coordinates remain visible in every ability- and preference-component table and caveat block (handoff §2.4).

Materiality remains a **numerical** question answered at the first gate; the
posture does not assert it. A Tier-2 trigger that fires is still a charter §11
halt (§7.1). **`[v2]`** The trigger is evaluated on the D16 list, whose
opportunity-share element reads on `s_opp` (§5.5).

#### 5A.9.5 Specification-limits caveat block (R9 item S9, with R-71 R10) — ratified, **`[v2]` extended by one row**

The degeneracies are reported together as **one** manuscript
specification-limits block, stated rather than buried. **`[v2]`** the block now
carries a fourth row, so that the fixed-background residual travels with the
other stated limits rather than in a separate note:

| Degeneracy / limit | Channel | Consequence for the reported component |
|---|---|---|
| **Hours availability** `g^H` carries no household covariates (U12 §3.4) | access | operator action is the identity; the hours cell contributes exactly zero; the access component is a **lower bound** on offer-side inequality w.r.t. hours-availability heterogeneity |
| **`σ` common across households** (R9 §2.3) | ability | operator action is the identity; the ability component is **location-only**, containing no wage-dispersion content, and is a **lower bound** w.r.t. dispersion heterogeneity |
| **`held` pinned-preference switch** (R9 §3.3) | preference | `theta_l_m` and `beta_ll` are couples-side; the switch is **non-binding in M08** under singles-only scope — recorded for provenance, with a Stage-A verification-and-halt |
| **`[v2]` Fixed-background residual `R_bg^k`** (ruling §3.4, §3.7; D21) | **none — outside `{A,B,P}`** | inequality remaining after all three modeled structural channels are equalised, with the frozen background retained. Reported **in levels and as a share**, **signed**, with the §5.3 source list. **Never** labelled endowment, needs, circumstance, unfairness, or causal. The three-channel game is **not** a complete causal decomposition of every determinant of welfare |

**`[v2]` The manuscript paragraph that carries this row is the ruling §3.7
interpretation, transcribed verbatim at §5.7.** It is reproduced in the
manuscript caveat block alongside the three rows above, not paraphrased.

### 5A.10 S-10 invariance statement (R9 §5, verbatim)

> The compact statement for the contract: *arguments are scenario-invariant and hash-asserted; equalised values are scenario-dependent by construction and reported.*

**Hash-asserted invariant across all four S-10 scenarios** (R9 §5.1, verbatim):

> `ē`, `p̄ₑₓₚ`, `p̄ₑₓₚ²`, `āge`, `āge²`, `ēduc_leisure`, `n̄kids`; the dwt joint `π_dwt(dgn, educ3)`; the derived occupation objects `p̄(loc4|educ3)`, `p̃(loc4|dgn)`, `p̄̄(loc4)`; the D1 cell routing; the coalition enumeration and Shapley weights; the substitution map of `P`'s step (b) (which coordinates are replaced by which, as a *map*, not as values); `π`; `c_ij`; the alternative support; every measure reference.
>
> All hash-asserted identical across the four scenarios, and recorded before execution.

**Legitimately varying, and not hash-asserted** (R9 §5.2, verbatim):

> `beta_w_pexp2` **is an ability-channel coefficient**. The ability operator's reference index — the equalised Mincer location `μ̄ = b·x̄ + δ_occ[loc4_j]` — is evaluated at the scenario's `θ`, so `μ̄` differs in scenarios 3 and 4. Likewise, if `P`'s reference group block is singles-male, the equalised `θ̄^pref` differs in scenarios 2 and 4 because `beta_l0_sm` is perturbed. Consequently the **equalised values**, every `I(S)`, and every Shapley component vary across scenarios. This is the sensitivity the exercise exists to measure; it must be reported in full, including sub-threshold continuous changes (charter §7 Stage G), and must **not** be suppressed by an invariance assertion.

> **`[v2]` Scope note, no change of substance.** "every `I(S)`, and every Shapley
> component" is read as `I^k(S)` and `φ_q^k` for **`k ∈ {W2, W5}`**, the two
> decomposed measures. **`R_bg^k` varies across scenarios on the same footing and
> is reported per scenario, in levels and as a share** — it is neither
> hash-asserted invariant nor suppressed. The S-10 scenario **subgroup** tables are
> emitted for **`W2`** (§4 Stage G; §6.3.4), and the 2pp trigger reads on `s_opp`
> (D16, §5.5).

The access operand additionally satisfies the stronger U12 §8.1 property — it
is **numerically identical** across all four scenarios, because no
access-assigned coefficient is perturbed — asserted by hash of the resolved
operand object in each of the four scenario runs.

### 5A.11 Items this section does NOT close — **`[v2]` BOTH NOW CLOSED**

v1 recorded two items here as **UNRESOLVED on charter text**, both candidate
charter §11 halts, with the note *"Execution is blocked until the deputy resolves
them."* **The deputy has resolved them.** Both are now
**RESOLVED-BY-DEPUTY-RULING**; the reasoning is at **§7.3**, which v2 rewrites.

| Item | v1 status | v2 status |
|---|---|---|
| **R8 / U12 §8.3** — the `W^3` own-set reference and baseline non-degeneracy | UNRESOLVED on charter text; blocking before Stage F | **RESOLVED-BY-DEPUTY-RULING** (ruling §3.1–§3.2): the degeneracy is *acknowledged as correct by construction* and disposed of by **removing `W3` from the decomposition role**, not by redefining `W3`. Primary is `W2`, which is non-degenerate. §7.3(a) |
| **S6 / R9 §4.4** — the `c_ij` grand-coalition residual | UNRESOLVED on charter text; **V20c** the surfacing mechanism, failure action *halt to deputy* | **RESOLVED-BY-DEPUTY-RULING** (ruling §3.3–§3.4): `c_ij` stays fixed across coalitions and its heterogeneity is **assigned to the fixed background**, named first in the §5.3 residual source list and reported as part of `R_bg^k`. No fourth operator. §7.3(b) |

**Execution of the decomposition is no longer blocked by R8 or S6.** The
remaining freeze conditions are at §8.4.

---
## 6. Outputs and disclosure rules

### 6.1 Disclosure split (aggregate-only vs restricted)

**Aggregate-only in `Job_Market_paper`.** No household-level welfare or
microdata artifact is placed in the public paper repository under any
circumstance this contract authorizes (D18; charter acceptance gate #13).
This mirrors the frozen handoff's general rule that no welfare number may be
sourced from a management memo (handoff §1, "the strategic assessment is
context, never data") extended by the charter to disclosure: paper-facing
artifacts are aggregates, tables, and figures only.

**Restricted artifacts live in MNL**, at the namespace resolved under U9, and
must include: application-specific code, tests, restricted numerical
artifacts, a manifest, and an acceptance pointer (charter §8 "MNL"). Every
paper-facing magnitude must map to an accepted aggregate artifact (charter
§9.15).

### 6.2 Required `Job_Market_paper` outputs

**Required `Job_Market_paper` outputs (charter §8), once authorized:**

1. `docs/Missions/JMP_M08_singles_welfare_execution_contract_v2.md` (**this
   file**, once frozen). **`[v2]`** v1 remains on disk as immutable history and is
   **not** a deliverable; the frozen contract of record is v2.
2. `docs/results/FR_P2a_welfare_integration_validation_v1.md` — **`[v2]`** this is
   the "validation memo" that ruling §3.4 charges with enumerating the residual
   sources and separating substantive residual inequality from numerical Shapley
   arithmetic error (§5.3), and with recording the non-binding status of the
   `held` switch (§5A.6 §3.3).
3. `docs/results/FR_P2a_welfare_family_results_v1.md`
4. `docs/results/FR_P2a_welfare_decomposition_results_v1.md` — **`[v2]`** carries
   the `W2` primary and `W5` secondary decompositions, the §5.5 headline
   quantities and four shares (signed), `R_bg^k` in levels and as a share, and the
   V21 diagnostic on `W2`.
5. `docs/results/FR_P2a_S10_welfare_sensitivity_v1.md`
6. `docs/results/FR_P2a_welfare_reporting_map_v1.csv`
7. `manuscript/sections/FR_P2a_welfare_decomposition_baseline_v1.md`
8. `manuscript/appendices/FR_P2a_welfare_appendix_v1.md`
9. `docs/missions/JMP_M08_independent_economics_review_v1.md`
10. `docs/missions/JMP_M08_goal_manager_acceptance_v1.md`
11. `docs/missions/JMP_M09_LOC4_welfare_robustness_handoff_v1.md`

**`[v2]` No new paper-facing file is created by the v2 amendment.** The
deliverable list is v1's, with item 1 rebound to this file and items 2 and 4
annotated with the duties the ruling attaches to them.

---

### 6.3 Pre-registered subgroup reporting (U4 deputy ruling, incorporated)

**Governing document, by exact cross-reference:**
`Job_Market_paper docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md`
(sha256 `41061f7ce681f56528cd3576dda707691e3440bac7c35bb6ca4947dde0af9bcb`;
Deputy Programme Director; 2026-08-05; binding amendment to this contract).
**Digest restated under Goal-1 R-70.2** (2026-08-06); the `docs/design_notes/`
duplicate has been deleted; the pre-fix digest was
`b7c0ac18557c13984b685f32f64355c8708fdfd020c1880ae9efd40edce12181`.
The ruling governs in full, **except** on the identity of the *primary
decomposition measure*, where the later decomposition-architecture ruling
governs — see **§6.3.4**. Its §1 (dimensions), §3 (statistics) and §4
(disclosure) are quoted **verbatim** below, as its §5 permits and this contract
prefers, so that the execution requirements are readable without leaving this
file. Where quotation and source could ever diverge, the ruling governs.

#### 6.3.1 Ruling §1 — Decision (verbatim)

> ## 1. Decision
>
> The following subgroup dimensions are now pre-registered for the France 2016 P2a singles welfare prototype:
>
> 1. **Sex**
>    - single male;
>    - single female.
>
> 2. **Education**
>    - the three categories of the accepted `educ3` coding;
>    - labels must be taken from the accepted data/specification documentation;
>    - no relabelling or regrouping is permitted after welfare results are observed.
>
> 3. **Broad region**
>    - all accepted NUTS-1 design categories represented by the `drgn1` reference category and `drgn2`–`drgn8`;
>    - paper-facing labels must come from accepted data documentation;
>    - absent accepted labels, report the design-category codes only.
>
> These are descriptive reporting cuts. They do not change the access/ability/preference factor definitions, the equalisation operators, or the Shapley game.

Ruling §2 additionally **excludes** age bands (no accepted categorical age-band
scheme exists; creating one now *"would misstate the model and originate an
unrecorded design choice"*) and occupation (*"occupation is an estimated access
channel and the first mandatory LOC4 robustness dimension"*), together with
children, marital-status variants, industry, external regional covariates, and
ad hoc intersectional cells. **This contract adds none of them.**

#### 6.3.2 Ruling §3 — Required subgroup statistics (verbatim)

> ## 3. Required subgroup statistics
>
> Use the same weighting convention as the headline welfare and inequality calculations. Also report the unweighted household count.
>
> ### 3.1 Baseline welfare-family reporting
>
> For each active welfare measure \(W^1,\ldots,W^6\), report by:
>
> - sex;
> - education.
>
> Required statistics:
>
> - unweighted household count;
> - weighted mean money-metric welfare;
> - weighted median money-metric welfare;
> - weighted welfare Gini.
>
> Region-by-measure tables for all six measures are not mandatory.
>
> ### 3.2 Primary decomposition measure
>
> For the primary \(W^3\) baseline, report by:
>
> - sex;
> - education;
> - broad region.
>
> Required statistics:
>
> - unweighted household count;
> - weighted mean;
> - weighted median;
> - weighted 10th percentile;
> - weighted 90th percentile;
> - weighted welfare Gini.
>
> No subgroup-level Shapley decomposition is required in M08. The decomposition remains a population-level structural attribution unless a later mission explicitly authorizes subgroup Shapley games.
>
> ### 3.3 S-10 four-scenario reporting
>
> For each of the four S-10 scenarios, report the §3.2 statistics for \(W^3\) by:
>
> - sex;
> - education;
> - broad region.
>
> The purpose is to detect whether local sensitivity is concentrated in a particular observed subgroup. The pre-registered population-level materiality thresholds remain the formal Tier-2 trigger. Subgroup movements are reported continuously and discussed as diagnostics; they do not create an additional unstated trigger.

#### 6.3.3 Ruling §4 — Cell and disclosure treatment (verbatim)

> ## 4. Cell and disclosure treatment
>
> - No regrouping may be chosen after welfare outputs are observed.
> - Report cell counts with every subgroup table.
> - A cell with fewer than 30 unweighted households is not shown in paper-facing tables. It remains in restricted validation output and is marked `SUPPRESSED_LT30`.
> - Suppressed cells are not merged post hoc.
> - This suppression rule is a reporting/disclosure rule, not a change in the structural sample or decomposition.

Note the collision of thresholds: the `SUPPRESSED_LT30` cut-off (30 **unweighted
households**) is numerically equal to, but conceptually unrelated to, the ESS
threshold of 30 (**effective draws per household**, U5/D-item ESS). They are
different objects and must not be conflated in code or in prose.

#### 6.3.4 **`[v2]` Rebinding the U4 ruling's "primary decomposition measure" slot from `W3` to `W2`**

**The quotations at §6.3.2 are left byte-faithful and are not edited.** The U4
ruling is immutable history and says what it says. What changes is the *referent*
of the measure slot its §3.2 and §3.3 name, and the change is directed by a later
binding deputy decision:

- the U4 ruling (2026-08-05) wrote `W^3` into its §3.2 heading *"Primary
  decomposition measure"* and into its §3.3 scenario tables, because at that date
  `W3` was the contract's primary decomposition anchor;
- the decomposition-architecture ruling (2026-08-07) **§3.2** makes **`W2`** the
  primary source decomposition and **`W3` validation-only**, and its **§4.1**
  directs: *"replace every statement that `W3` is the primary decomposition target
  with `W2`"*.

**Operative requirement, restated in this contract's own words (this is what
Stage D–G executes):**

| U4 clause | Slot as written (2026-08-05) | **Slot as bound in v2** |
|---|---|---|
| §3.1 — baseline welfare-family reporting | six measures `W^1…W^6` × {sex, education}; count, weighted mean, weighted median, weighted Gini | **UNCHANGED.** All six measures, including `W3`, are reported here — `W3`'s family role is untouched (§5.1) |
| §3.2 — "primary decomposition measure" | `W^3` × {sex, education, broad region}; count, weighted mean, median, p10, p90, Gini | **`W2`** × {sex, education, broad region}; **same six statistics, unchanged** |
| §3.3 — S-10 four-scenario reporting | the §3.2 statistic set for `W^3`, per scenario, by {sex, education, broad region} | the §3.2 statistic set for **`W2`**, per scenario, by the same three dimensions; **unchanged otherwise** |

**Nothing else in the U4 ruling moves.** The dimensions (sex, `educ3`, `drgn1`),
the exclusions (age bands, occupation, children, marital-status variants,
industry, external regional covariates, intersectional cells), the statistics,
the `dwt` weighting convention, the unweighted counts, the `SUPPRESSED_LT30`
disclosure rule, and the prohibition on post-hoc regrouping are **all
unchanged**. In particular the U4 §3.2 sentence *"No subgroup-level Shapley
decomposition is required in M08"* stands unchanged and now attaches to `W2`.

**`W5`, the secondary decomposition measure, gets no new subgroup table.** The U4
ruling pre-registers one primary-measure region cut, and v2 does not enlarge the
pre-registered set — enlarging it would originate an unrecorded design choice of
exactly the kind the U4 ruling §2 forbids. `W5` appears in the §3.1 family tables
(sex × education) like every other measure, and its decomposition is reported at
population level per §5.6 item 5.

### 6.4 Binding of §3.1's "active welfare measure" to the charter's frozen list

Ruling §3.1 requires reporting "for each active welfare measure \(W^1,\ldots,W^6\)".
The active set is **the charter's**, not a set this contract may choose. Charter
`JMP_M08_singles_welfare_decomposition_mission_charter_v1.md` **§4.2 "Welfare
family"**, verbatim:

> ### 4.2 Welfare family
>
> Exercise A computes the configured money-metric family \(W^1,\ldots,W^6\), subject to the frozen build order and reference-coverage gates.
>
> - Primary build/validation anchor: \(W^3\).
> - Full-Responsibility check: \(W^2\).
> - One-sided access/ability duals: \(W^5\) and \(W^1\).
> - Full-Compensation endpoints: \(W^4\) and \(W^6\).
>
> The JMP imports the measures and their normative readings as cited primitives. It does not reproduce the companion theory paper's proofs or claim its axiomatic results as JMP contributions.

**This contract implements exactly that set — all six of `W1`…`W6`, and no
expansion.** The build order is D3; the operative ordering `["W3", "W5", "W2",
"W4", "W6", "W1"]` (D4) is a *sequencing* of the same six measures, not a
different set. Subgroup reporting under §6.3.2/§3.1 therefore covers six
measures × {sex, education}.

**`[v2]` Reading of the charter §4.2 bullets after the ruling.** *"Primary
build/validation anchor: `W3`"* is a **build/validation** statement and is
**unchanged** — it is exactly the role ruling §3.1 preserves. *"Full-Responsibility
check: `W2`"* is unchanged as a description of `W2`'s normative content; `W2`'s
*decomposition* role is upgraded from second check to **primary** by ruling §3.2.
The charter §4.3 sentence that anchored the *source decomposition* on `W3` is the
one superseded (§3.3, third bullet).

*Recording note for Stage A (not a proposal to deviate).* The pre-existing P2a
singles config `MNL scripts/welfare/configs/welfare_p2a_singles2016.yaml` carries
`measures.active: ["W1", "W3", "W4", "W6"]` and `headline_measures: ["W1", "W4",
"W6"]`. That is the **earlier P3-1 pipeline's** four-measure set, not M08's. M08
executes the charter's six. Any M08 config must set the active set to all six or
declare the divergence to Stage A; it may not inherit the four-measure list
silently. **`[v2]` note:** that legacy list also omits **`W2`** and **`W5`** — the
two measures v2 decomposes — so inheriting it would silently disable the entire
M08 decomposition, not merely shorten the family table.

### 6.5 Resolved sources: `educ3`, region, and the headline weighting convention

The ruling's §5 requires this contract to identify the accepted source for
`educ3` labels, the accepted source for region labels, and the headline weighting
convention. Each is resolved below against a **tracked, committed** artifact,
with the operative text quoted. **`[v2]` This subsection is unchanged.**

#### 6.5.1 `educ3` — definition and category labels · **RESOLVED, LABELS ACCEPTED**

**Accepted source:** `MNL docs/estimation/RURO_GSUR_DATA_AND_MERGE_NOTE.md`
(tracked). §"What The Preparation Script Does", item 6, verbatim:

> 6. Maps education into both text and numeric forms:
>
> ```text
> ED0-2 -> educL -> educ3 = 0
> ED3_4 -> educM -> educ3 = 1
> ED5-8 -> educH -> educ3 = 2
> TOTAL -> educALL -> educ3 = -1
> ```

The same document's "Main RURO Lookup Columns" table defines the two columns
verbatim as:

> | `educ_code` | `educL`, `educM`, `educH`, or `educALL` |
> | `educ3` | numeric education group |

**Operative M08 coding — the three reporting categories:**

| `educ3` | `educ_code` | ISCED-11 source group | Paper-facing label |
|---|---|---|---|
| 0 | `educL` | `ED0-2` | Low (ISCED 0–2) |
| 1 | `educM` | `ED3_4` | Medium (ISCED 3–4) |
| 2 | `educH` | `ED5-8` | High (ISCED 5–8) |

`educ3 = -1` (`educALL`, the ISCED `TOTAL` row) is a **lookup-table aggregate,
not a household category**; it must never appear as a reporting cell. Stage D
must assert `educ3 ∈ {0, 1, 2}` over the P2a singles evaluation sample and halt
if any other value occurs.

The labels above are the accepted document's own `educL/educM/educH` and
`ED0-2 / ED3_4 / ED5-8` strings rendered for a paper table; no new substantive
category name is introduced. Per ruling §1, **no relabelling or regrouping after
welfare results are observed.**

#### 6.5.2 Broad region `drgn1` — definition ACCEPTED, labels **CODE-CATEGORIES-ONLY**

**Accepted definition source:**
`MNL docs/France_case/_shared/gsur/RURO_GSUR_local_O1_evidence_audit_v1.md`
(tracked), §2 "EUROMOD drgn1 definition in local documentation", which records
the DRD (`DRD_FR_2016_a3_export.txt`) derivation verbatim:

> The DRD (`DRD_FR_2016_a3_export.txt`) documents the derivation explicitly:
>
> ```
> drgn1 = 1 if drgn2 == 1
> drgn1 = 2 if drgn2 in {2,3,4,5,6,7}
> drgn1 = 3 if drgn2 == 8
> drgn1 = 4 if drgn2 in {9,10,11}
> drgn1 = 5 if drgn2 in {12,13,14}
> drgn1 = 6 if drgn2 in {15,16,17}
> drgn1 = 7 if drgn2 in {18,19}
> drgn1 = 8 if drgn2 in {20,21,22}
> drgn1 = 9 if drgn2 in {23,24,25,26}
> drgn1 = 10 if drgn2 == 27
> ```

and characterises the result:

> These are the **22 former metropolitan régions** (NUTS 2013) plus DOM. The coding is
> the pre-2016 NUTS-2 vintage. EUROMOD `drgn1` therefore groups these 22 old régions
> into 8 composite categories plus a DOM category (9) and a residual (10). The local
> data dictionary fully documents this chain; no external EUROMOD codebook is needed
> to establish it.

**Support in the M08 cell.** The same audit records categories 9 and 10 as
observing **0 households** (*"Categories 9 and 10 observe 0 households. Maximum
observed `drgn1` = 8."*). The P2a singles-2016 design categories and their
household counts are recorded in
`MNL docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v4.md`
(audit §15), verbatim:

> 2. **`reg2 … reg8`** — seven NUTS-1 region dummies built by the loader fallback `reg{k} = (drgn1 == k)`; the stem's stored `reg2..reg8` columns are identically-zero region-dead placeholders never read by the likelihood [audit §15]. Household counts `{1: 245, 2: 254, 3: 122, 4: 135, 5: 279, 6: 175, 7: 182, 8: 163}`. **Reference category: `drgn1 == 1`, 245 households** [audit §15].

So the ruling's "the `drgn1` reference category and `drgn2`–`drgn8`" resolves to
the **eight** design categories `drgn1 ∈ {1,…,8}` — category 1 the estimation
reference, categories 2–8 carried by parameters `beta_E_drgn2 … beta_E_drgn8`
(D5). All eight are reported; the reference category is not dropped from a
descriptive table.

**Labels: `CODE-CATEGORIES-ONLY`** (ruling §1, third bullet: *"absent accepted
labels, report the design-category codes only"*). Justification, stated plainly:

- Accepted documentation names the **NUTS-2 `drgn2`** régions (Île-de-France,
  Picardie, …) and the **derivation** of `drgn1` from them, but assigns **no
  name to any composite `drgn1` category**.
- Only `drgn1 = 1` (← `drgn2 = 1`, FR10 Île-de-France) and `drgn1 = 3`
  (← `drgn2 = 8`, FR30 Nord-Pas-de-Calais) are singletons that could be named
  from the accepted table. The other six are composites of 2–6 old régions with
  no accepted name. Naming them would be **inventing substantive labels**, which
  the ruling's §5 forbids.
- Labelling a subset and coding the rest would produce a table mixing named and
  numbered rows — worse than uniform codes.

**Therefore:** paper-facing region tables use `drgn1 = 1 … 8` as row labels, with
a footnote pointing to the DRD derivation above, until an accepted `drgn1` label
set is supplied and ratified. Stage A may supersede this by supplying one.

Do **not** use the GSUR preparation script's `DEFAULT_NUTS1_ORDER`
(`scripts/enhanced/enh_prepare_FR_gsur.py:101`) to name `drgn1` categories: that
is the **GSUR lookup's own** region ordering over Eurostat NUTS-1 letter codes,
overridable at the CLI (`--nuts1-codes`), and
`MNL docs/France_case/_shared/data_audits/RURO_FR2016_CONTINUOUS_DATA_BUILD_AUDIT_v1.md`
warns that *"the live `drgn1` coding and the GSUR lookup region coding are not yet"*
aligned and that *"EUROMOD `drgn1` uses the old 10-category French regional
coding"*. Naming EUROMOD `drgn1` from the GSUR order would mislabel regions.

#### 6.5.3 Headline weighting convention · **RESOLVED — NO HALT**

The ruling's §3 requires *"the same weighting convention as the headline welfare
and inequality calculations"*, and its §5 makes an absent convention a halt
condition. **A convention exists in accepted artifacts. The halt does not fire.**

**The convention: household survey weight `dwt`; unweighted counts reported
alongside.** Evidence, in descending authority:

1. **Governance memo** —
   `MNL docs/jmp_methodology/JMP_welfare_measurement_decisions_memo_v2.md`:1347:
   > survey-weighted Ginis: W1 = 0.173, W4 = 0.329, W6 = 0.337; across-measure bracket [0.173, 0.337],
2. **Ratification record** —
   `MNL docs/jmp_methodology/RURO_welfare_F5_primary_scope_ratification_v1.md` §2,
   whose headline table column is titled verbatim:
   > | Measure | Primary 2016 survey-weighted Gini |
3. **Accepted F5 report, naming the variable** —
   `MNL docs/jmp_methodology/RURO_welfare_singles_measure_family_F5_report_v1.md`:3:
   > Date: 2026-06-13 · spec_hash `492bcfa9c766bfcb` · theta_hash `1dd94e9cf1f35464` · weight `dwt` · cluster `idorighh` · unit monthly real-2016 EUR
4. **Committed config** — `MNL scripts/welfare/configs/welfare_p2a_singles2016.yaml`:34-35 (tracked):
   > ```yaml
   >   weighting:
   >     weight_col: "dwt"              # survey weight (run_f5_singles_measure_family.py Primary index)
   >     cluster_col: "idorighh"        # fr_p2a_singles2016__mnlmeta.json:38
   > ```
5. **Committed implementation** —
   `MNL scripts/welfare/fastlane/run_f5_singles_measure_family.py`:13 (tracked):
   > Primary index = survey-weighted Gini (weight = staged `dwt`).

**What `dwt` is.** The accepted EUROMOD reference
`MNL docs/France_case/_shared/euromod_reference/euromod_fr_2015_2017_input_output_reference.md`:68
(tracked) defines it verbatim in its variable table:

> | dwt        | personal     | DEMOGRAPHIC : Weight                                                                       | dwt = db090                                                                                                              | 0          |  7482 |

i.e. the EU-SILC `db090` household cross-sectional weight, carried on the person
record. It is **household-constant**: the accepted F5 report records
*"within-uid constant: True"* and *"dwt finite>0: True"*, and the M08 runner
takes one value per household via `drop_duplicates` on the household key
(`run_p2a_singles_welfare.py:303-308`).

**Load-bearing scope limit — the estimator is NOT `dwt`-weighted.** The searched
accepted estimation spec
`MNL scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`
contains **no survey weight**. Its only `weight` keys are unrelated objects:
`center_weights: "proposal"` (:185, importance-sampling proposal centering) and
`expression_constraints.default_weight: 1000.0` (:441, a soft-constraint penalty).
The scaffold contract's and W3 gate report's "weights" are likewise **importance
weights** `ω_is` (ESS, max-normalised weight — scaffold contract §392-393; gate
report :95), not survey weights. `dwt` appears nowhere in the estimation loader,
and the one place the codebase discusses it outside the welfare layer states the
position explicitly
(`MNL Results/_proposal_adequacy_diag_ruro_occ_M0.py`:599):

> Unweighted statistics throughout; EUROMOD household weight `dwt` is intentionally not applied (diagnostic, not population estimate).

**Therefore, the frozen convention for M08:** `theta_hat` is estimated
**unweighted**; every **population-facing welfare and inequality statistic** —
headline and subgroup alike — is weighted by `dwt`; **household counts are
reported unweighted** (ruling §3, and the `SUPPRESSED_LT30` rule of §4 counts
unweighted households). No new weighting scheme is proposed or introduced.

**`[v2]`** This convention also governs every `I^k(S)` entering the
decomposition, hence `φ_q^k`, `R_bg^k`, and `s_opp`: the inequality index is the
`dwt`-weighted Gini (D8), computed identically in every coalition. The operand
population references are separately `dwt`-weighted per R-71 R6 (§5A.2, §5A.3),
which is the same weight and the same convention.

### 6.6 Implementation path for weighted quantiles and weighted Gini

Implementation is Stage-D work; this section fixes **where it lives** and what
may be reused, so Stage A can freeze the location. **`[v2]` unchanged.**

**Module (new, to be created at Stage D):**
`MNL scripts/welfare/m08_subgroup_reporting.py`
— sits beside the existing `scripts/welfare/m08_p2a_parity.py`, matching the
`m08_*` naming already established for this mission. It owns subgroup assignment,
the weighted statistics, the `SUPPRESSED_LT30` marking, and table emission. No
existing welfare module is modified.

| Object | Status | Location / action |
|---|---|---|
| Weighted Gini | **EXISTS — reuse unchanged** | `MNL scripts/welfare/run_p2a_singles_welfare.py`:245 `w_gini(x, w)` (Lerman–Yitzhaki; itself ported from `run_f5_singles_measure_family.py`:121-131), exposed through `inequality_battery(x, w)` at :276 |
| Weighted mean | **EXISTS — reuse unchanged** | same module, :240 `w_mean(x, w)` |
| Weighted median / p10 / p90 | **DOES NOT EXIST in the welfare layer — must be added** | new `weighted_quantile(values, weights, qs)` in `m08_subgroup_reporting.py`, ported from the proven `MNL scripts/enhanced/RURO_post_estimation_styled.py`:6610 `_weighted_quantile` (finite-and-positive-weight mask → sort → cumulative-weight CDF → `np.interp`) |

**Explicit trap.** `MNL scripts/welfare/run_p2a_singles_welfare.py`:294
`_quantiles(x)` is **unweighted** (`np.quantile`, no weight argument) and
`MNL scripts/welfare/welfare_core.py`:581 `gini(x)` is **unweighted**. Neither
may be used for any statistic required by ruling §3 — both would silently
produce an unweighted number where a `dwt`-weighted one is required. Stage D must
route all subgroup statistics through the weighted functions above.
**`[v2]` The same trap applies to every `I^k(S)`:** the decomposition's inequality
index is the **weighted** Gini, and the unweighted `gini(x)` must not be reached
by any coalition evaluation.

**Required Stage-D assertions** (cheap, and they close the failure modes this
section creates): `dwt` finite and `> 0` on every reporting row; `dwt`
household-constant; subgroup cells partition the evaluation sample exactly (no
household dropped, none double-counted); `educ3 ∈ {0,1,2}` and `drgn1 ∈ {1..8}`;
the sum of subgroup unweighted counts equals the headline household count.

### 6.7 Output tables and files carrying the subgroup summaries

All subgroup artifacts are **restricted** and live in MNL under the U9 namespace
`outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/`, written under the same
`attempts/` transaction pattern the parity gate uses. Standing rule 6 applies:
**`Job_Market_paper` receives aggregate tables only** — no household-level
artifact, ever (D18; charter acceptance gate #13).

**Restricted (MNL), under `…/welfare_m08_v1/attempts/<attempt_id>/`:**

| File | Content | Ruling clause |
|---|---|---|
| `subgroup_family_by_sex_educ_v1.csv` | `W1`…`W6` × {sex, education}: unweighted count, weighted mean, weighted median, weighted Gini | U4 §3.1 — **`[v2]` unchanged** |
| **`subgroup_W2_primary_v1.csv`** | **`W2`** × {sex, education, broad region}: unweighted count, weighted mean, weighted median, weighted p10, weighted p90, weighted Gini | U4 §3.2 as rebound at §6.3.4. **`[v2]` renamed from `subgroup_W3_primary_v1.csv`; statistic set unchanged** |
| **`subgroup_W2_s10_scenarios_v1.csv`** | the U4 §3.2 statistic set for **`W2`** under each of the four S-10 scenarios (D15), long format with a `scenario` key | U4 §3.3 as rebound at §6.3.4. **`[v2]` renamed from `subgroup_W3_s10_scenarios_v1.csv`; statistic set unchanged** |
| `subgroup_manifest_v1.json` | attempt id, input digests, `weight_col: "dwt"`, category codings used, per-cell unweighted counts, the full list of cells marked `SUPPRESSED_LT30`, and the Stage-D assertion results of §6.6. **`[v2]`** also records the primary-measure binding (`primary_decomposition_measure: "W2"`, `secondary: "W5"`, `validation_only: "W3"`) so the rebinding is machine-checkable, not only prose | U4 §4 |

Every row of the three CSVs carries its unweighted cell count and a
`disclosure` column valued `OK` or `SUPPRESSED_LT30`. Restricted output retains
suppressed cells **with their values** (ruling §4: *"It remains in restricted
validation output and is marked `SUPPRESSED_LT30`"*).

**`[v2]` No new restricted file is added.** Two files are renamed to follow the
measure they now carry; the file count, the statistic sets, and the disclosure
treatment are unchanged. A Stage-D run must not emit both the `W3`- and
`W2`-named variants.

**Paper-facing (`Job_Market_paper`), aggregate only:** the subgroup tables are
carried inside the already-required §6.2 deliverables — the U4 §3.1 family tables
and the **`W2`** primary tables in `docs/results/FR_P2a_welfare_family_results_v1.md`
(with the region cut reproduced in
`docs/results/FR_P2a_welfare_decomposition_results_v1.md` where it accompanies the
**`W2`** decomposition), and the U4 §3.3 scenario tables in
`docs/results/FR_P2a_S10_welfare_sensitivity_v1.md`. Every subgroup magnitude is
registered in `docs/results/FR_P2a_welfare_reporting_map_v1.csv` with a pointer to
its restricted source row, per charter §9.15. **No new paper-facing file is
created by this amendment.** Cells marked `SUPPRESSED_LT30` are **absent** from
these tables — shown as a suppression marker with the cell count, never merged
into a neighbouring cell (ruling §4).

---
## 7. Halt conditions (verbatim)

### 7.1 From the mission charter §11

> Return to the deputy immediately if:
> - reprice parity is structural/type-specific and unresolved;
> - accepted P2a inputs cannot be bound;
> - a required reference set/operator is undefined;
> - a generic package change is required;
> - the welfare family cannot be implemented under the accepted theory/JMP
>   boundary;
> - an integration gate fails without a frozen escalation rule;
> - a Tier-2 S-10 trigger fires;
> - Shapley exhaustiveness fails;
> - household-level disclosure cannot be controlled;
> - LOC4 Path B would need reconsideration.

**`[v2]` Two of these halts are re-anchored by the decomposition-architecture
ruling, and neither is weakened:**

- ***"Shapley exhaustiveness fails"*** now means **failure of the ruling §3.4
  identities at gate §5.4(2) or §5.4(3)**, i.e.
  `|Σ_q φ_q^k − [I^k(∅) − R_bg^k]| > ε_Shapley` or
  `|I^k(∅) − (φ_A^k+φ_B^k+φ_P^k+R_bg^k)| > ε_Shapley`, for `k ∈ {W2, W5}`. It
  **no longer** means `I^k({A,B,P}) ≠ 0`; a non-zero grand-coalition value is a
  *reported* `R_bg^k`, not a halt (§5.4.1).
- ***"a required reference set/operator is undefined"*** stands unchanged as a
  halt, but the two items v1 escalated under it — R8 and S6 — are **resolved**
  (§7.3). It remains live for anything newly found undefined at Stage A, and it
  is the halt that would fire if a Stage-D enumeration under gate §5.4(4) found a
  source of cross-household variation that is **neither** an `{A,B,P}` cell
  **nor** on the §5.3 fixed-background list.

The deputy's own return rule (ruling §5) is additionally binding and is
reproduced verbatim at §8.5.

### 7.2 From the delegation's "Critical M08 discipline" block (`JMP_M08_goal_manager_delegation_prompt_v1.md`)

> - Diagnose the documented singles reprice-parity failure before changing
>   code.
> - No redrawn node or paper-facing welfare number before parity passes.
> - Use the exact frozen ESS/redraw/draw-growth thresholds; invent none.
> - Reuse the estimator's utility/opportunity machine and mandatory proposal
>   correction.
> - Freeze all measure references, channel memberships, equalisation
>   operators, subgroup lists, and S-10 vectors before execution.
> - No re-estimation, Phase-5 reopening, LOC4, `lindi`, external covariates,
>   couples, pooled years, broad literature search, or silent package change.
> - One bounded Codex production-path review after the parity correction; no
>   general software-review loop.
> - One independent economics review after results; one narrow correction
>   cycle maximum.
> - If a Tier-2 S-10 trigger, structural parity failure, undefined
>   reference/operator, generic package change, Shapley failure, or
>   disclosure risk occurs, halt and escalate.

Both blocks are reproduced in full and are jointly binding; neither
supersedes the other.

**`[v2]` Status of the "invent none" line.** v1 recorded that this draft failed
*"use the exact frozen ESS/redraw/draw-growth thresholds; invent none"* for **U6**
and **U7**. **U7 is closed** at `0.5` nats (§3.2a(U7)). **U6 remains open** — the
2×/4× draw-multiplier datasets do not exist, so no draw-growth tolerance can be
exercised — and that remains a documented halt condition ("a required reference
set/operator is undefined") until Stage A resolves it. `ε_Shapley` is **not** an
invented threshold in the sense this line prohibits: it is the frozen U8
convention adopted to make the ruling's own §3.5(2)–(3) gates checkable, recorded
with its rationale and its scope limit at §3.2a(U8).

### 7.2a **`[v2]` Literature prohibition (decomposition-architecture ruling §1)**

The ruling's §1 **closes the literature axis for the duration of M08 and LOC4**,
and its constraint is added here to the standing prohibitions. Ruling §1.1,
verbatim:

> The JMP literature rebuild is treated as complete for the current empirical-design stage.
>
> No new broad paper search, no repeat Zotero-library summarisation, and no new literature mission is authorized during M08 or LOC4.

Ruling §1.2, verbatim, on what remains permitted:

> Only a claim-triggered targeted action is permitted:
>
> - verify one citation or metadata item;
> - extract one paper needed for an exact manuscript claim;
> - update a working-paper status;
> - close one explicitly identified comparator gap.
>
> For the decomposition methods section, the existing corpus entries on Shorrocks (2013), Audoly et al. (2025), Bargain et al. (2013), Dagsvik and Karlström (2005), and Jacquet, Jia and Thoresen (2026) are sufficient for the current design stage.
>
> A Zotero-completeness audit may be performed during final manuscript citation closure, but it is not a current research task.

**Operative prohibition for M08.** No broad literature search, no repeat Zotero
summarisation, and no new literature mission may be opened under this contract.
The five named corpus entries are **sufficient** for the decomposition methods
section at this design stage; a claim-triggered targeted action is the **only**
permitted literature work, and each such action must be traceable to one exact
manuscript claim. This reinforces — and does not replace — the delegation block's
existing *"no broad literature search"* prohibition at §7.2.

### 7.3 **`[v2]` Disposition of the two decomposition-baseline items (R8/S6) — BOTH RESOLVED-BY-DEPUTY-RULING**

**This subsection replaces v1's §7.3 in full.** v1 recorded a Step-0 charter
verification that classified both items **UNRESOLVED on charter text**, in the
form charter §6 requires for a bounded design conflict, and declined to invent a
resolution. That was the correct posture, and the escalation it produced has now
been answered. **The deputy has ruled on both.** Both are therefore
**RESOLVED-BY-DEPUTY-RULING**, and **execution of the decomposition is no longer
blocked by either.**

The v1 finding is retained below as the **charter-text record** — it is what the
escalation rested on, and Stage A should be able to read the conflict and its
resolution together.

#### (a) `W^3` own-set degeneracy (R8 / U12 §8.3) — **RESOLVED-BY-DEPUTY-RULING**

**What v1 found on charter text (retained verbatim as the record):**

> **Classification: UNRESOLVED.** The charter names `W^3` as "primary
> build/validation anchor" (§4.2) and states that "the primary source
> decomposition is anchored on \(W^3\)" (§4.3), but **nowhere defines `W^3`'s
> reference structure**. It expressly imports the measures "as cited primitives"
> (§4.2) and delegates "exact definitions of every measure-specific reference"
> to Stage A (§6). There is therefore **no charter text** that defines the
> decomposition welfare object as a common-reference money metric, and none that
> establishes a non-degenerate baseline \(I(\Omega)\). The own-set `W^3` anchor
> consequently **stands** on the charter's own text, and with it the degeneracy
> recorded at U12 §8.3 — baseline inequality identically ≈ 0, so that a
> decomposition of the baseline vector is not a decomposition of inequality.

**How the deputy resolved it (ruling §3.1, §3.2, §4.1, §4.3).** The deputy
**accepts the degeneracy finding** and disposes of it by changing the
*decomposition target*, not the measure:

- the degeneracy is confirmed as correct by construction — *"under the accepted
  own-set laissez-faire construction, baseline \(\Omega_i^3 \simeq 0\) for every
  household. Hence \(I(\Omega^3)\simeq0\) is correct by construction and contains
  no observed baseline inequality to allocate"*;
- **`W3` is not redefined**, and *"do not create a 'common-reference W3.' That
  would silently replace a characterised welfare measure with a new object"*;
- **`W3` is retained as validation-only**, with all three of its v1 roles intact;
- **the primary source decomposition moves to `W2`**, *"the non-degenerate
  Full-Responsibility measure"*, with `W5` secondary.

**Why this closes the charter §6 conflict.** The conflict was that the charter
named a decomposition anchor whose baseline is degenerate while delegating the
reference definition. The deputy — the authority the charter §6 halt routes to —
has now named a **non-degenerate** primary measure and left the reference
definitions where they were. Nothing is invented by this contract; the resolution
is quoted from the ruling. **The charter §11 halt "a required reference set/
operator is undefined" does not fire on R8.**

**One residual duty, recorded not escalated.** The non-degeneracy of `I^{W2}(∅)`
is an empirical property that Stage D observes, not an axiom. If `I^{W2}(∅)` were
found degenerate in the data, the ruling's own §5 return rule makes it a deputy
matter — *"inability to construct non-degenerate `W2`"* is an enumerated return
trigger (§8.5). Stage D reports `I^{W2}(∅)` and `I^{W5}(∅)` before any Shapley
value is formed.

#### (b) `c_ij` grand-coalition residual (S6 / R9 §4.4) — **RESOLVED-BY-DEPUTY-RULING**

**What v1 found on charter text (retained verbatim as the record):**

> **Classification: UNRESOLVED.** The §4.3 channel definitions are exhaustive of
> the *offer side* (access), the *wage technology* (ability), and *tastes*
> (preference). **No channel is defined over the budget mapping** — the
> household's non-labour income and demographic characteristics that determine
> disposable income `c_ij` at each row. The nearest candidate phrase, access's
> "other accepted non-wage offer terms", is by its own wording an **offer-side**
> term and does not reach the budget side. Nor does the charter define
> exhaustiveness in a way that disposes of the residual: §7 Stage F.3 requires
> that exhaustiveness be *verified* "to the frozen numerical tolerance", §9.8
> makes it an acceptance gate ("W3 Shapley decomposition is exhaustive"), and
> §11 makes its failure a halt ("Shapley exhaustiveness fails"). Those are a
> test and a halt, **not** an assignment of the residual to a channel. On
> charter text alone the grand-coalition residual is therefore unhandled.

**How the deputy resolved it (ruling §3.3, §3.4, §3.5, §4.4, §4.6, §4.7, §4.9).**
The deputy **accepts that the three channels do not exhaust household welfare
heterogeneity** and disposes of the residual by *naming and reporting* it rather
than by assigning it to a channel or inventing one:

- `c_ij` and the tax-benefit rules and non-labour-income inputs are **fixed across
  coalitions** (ruling §3.3) — the position v1 already implemented via V2/V3/V4,
  confirmed unchanged at §5.2;
- the grand-coalition value is **named**: `R_bg^k = I^k({A,B,P})`, *"the inequality
  remaining after all three modeled structural channels are equalised while the
  frozen background is retained"*;
- *"non-labour-income and demographic variation operating through \(c_{ij}\)"* is
  the **first named admissible source** of that residual (§5.3) — so `c_ij`
  heterogeneity is now **assigned**, to the fixed background;
- the requirement that `I({A,B,P}) = 0` is **removed** (ruling §4.6), and the
  claim that the three channels exhaust all household welfare heterogeneity is
  **removed** (ruling §4.7);
- **no fourth-channel operator is authorized** (ruling §3.3, §4.9): R9 §4.4's
  endowment/needs proposal is **not adopted**, and the ruling records that
  *"merely naming a fourth channel without an executable counterfactual operator
  would not constitute a Shapley decomposition"*. A four-channel design *"may be
  considered only after M08 and LOC4, if the residual is quantitatively material
  and scientifically worth explaining"* (ruling §3.7).

**Why this closes the charter §6 conflict.** v1's finding was that the charter
provides *a test and a halt, not an assignment*. The deputy has now supplied the
assignment — to a **reported fixed background**, with an enumerated source list
and an explicit prohibition on interpreting it as endowment, needs, circumstance,
unfairness, or causal (§5.7). **V20c's "halt to deputy if `c_ij` heterogeneity is
unassigned" therefore has no trigger** (§5A.8). Charter §9.8's acceptance gate is
re-anchored onto the §5.4(2)–(3) identities for `W2` and `W5`.

#### Consequence for this contract

**Both items are RESOLVED. Execution of the decomposition is no longer blocked by
R8 or S6.** §5A.11 carries the cross-reference. What remains before execution is
the §8.4 freeze list — and Stage A's own review — not these two design conflicts.
**No resolution was invented here:** every disposition above is quoted from the
binding ruling.

---
## 8. Open items and contract status

R-59 closed U1, U2, U5, U9, U11, U13, U14. The **U4 deputy ruling** closes U4.
**R-71/R-72** close U12 (and U7 at `0.5` nats). **v2** closes **U8** (frozen
`ε_Shapley`), **U15** (canonical LOC4 file now tracked), **R8** and **S6**
(deputy ruling, §7.3). What remains is below.

### 8.0 Open-items status at this amendment

| Item | v1 status | **v2 status on disk** | Basis |
|---|---|---|---|
| U1, U2, U5, U9, U11, U13, U14 | RESOLVED | **RESOLVED** ✓ | §3.2a |
| U4 | RESOLVED-BY-DEPUTY-RULING | **RESOLVED-BY-DEPUTY-RULING** ✓, measure slot rebound to `W2` | §6.3.4 |
| U12 | CLOSED by R-71 | **CLOSED**, transcribed at §5A, **operators unchanged** ✓ | ruling §4.10 |
| U10 | mechanical-at-freeze | **mechanical-at-freeze** ✓ | §8.3 item 1 |
| **U7** | PROPOSED-PENDING-RATIFICATION | **RESOLVED-BY-R-71 at `0.5` nats** ✓ | §3.2a(U7); §5A.8 V22 |
| **U8** | PROPOSED-PENDING-RATIFICATION | **RESOLVED — `ε_Shapley` = `1e-9·max(1,\|I^k(∅)\|)`** ✓ | §3.2a(U8); ruling §3.5 |
| **U15** | ESCALATED | **RESOLVED — closed** ✓ | §3.2a(U15); canonical file tracked, sha `4e7b95d9…b4bb`; competing file gone |
| **R8** | UNRESOLVED on charter text; blocking | **RESOLVED-BY-DEPUTY-RULING** ✓ | §7.3(a); ruling §3.1–§3.2 |
| **S6** | UNRESOLVED on charter text; blocking | **RESOLVED-BY-DEPUTY-RULING** ✓ | §7.3(b); ruling §3.3–§3.4 |
| **U6** | ESCALATED | **still ESCALATED** — enumerated freeze condition | §8.1 item 2 |
| **U3** | ESCALATED | **still ESCALATED — no referent**; *not* enumerated among the v2 freeze conditions | §8.1 item 1 |
| **V20b tolerance** | PROPOSED-AT-STAGE-A | **REMOVED — V20b retired** | §5.4.1; §5A.8 |
| **V6 / V22 numbers** | PROPOSED-AT-STAGE-A | **still PROPOSED-AT-STAGE-A** — enumerated freeze condition | §5A.8; §8.4 |

**Ruling-citation note, carried forward unchanged.** Of the Goal-1 rulings
R-59…R-72, none exists as a standalone document; each is known through citation
or recital in a document it authorised (see
`docs/Missions/JMP_M08_goal1_rulings_register_v1.md`). **No R-64 document
exists**, and §2.1's carry-forwards rest on the Goal-1 Manager's instruction;
Stage A should still expect a written R-64. **The decomposition-architecture
ruling is different in kind: it exists as a document on disk**, at the path and
digest in the front matter, and is cited directly rather than through a recital.

### 8.1 ESCALATED — cannot be resolved from the repositories

1. **U3 — "the up1 manifest note."** Unchanged: no file, commit message, or
   in-document reference matching "up1" exists in any welfare-adjacent context
   across the three repositories. Please supply the exact path or confirm it does
   not exist. **Recorded honestly:** the v2 status line (§8.4), which the deputy
   set, does **not** enumerate U3 among the freeze conditions. **This contract
   does not close U3** and does not assert that it is non-blocking; it records
   that no artifact in the execution path has been shown to depend on it, and
   carries it to Stage A as an open documentary question.
2. **U6 — draw-growth stability (Gate 1(i)).** Unchanged and not a
   documentation gap: the 2×/4× draw-multiplier datasets do not exist on
   disk, so no tolerance can be exercised. Decide: build the datasets, or
   carry Gate 1(i) forward BLOCKED under a pre-registered escalation rule.
   **Enumerated in the v2 freeze conditions.**
3. ~~**U12 — the common reference offer environment.**~~ **CLOSED by R-71/R-72**,
   transcribed at §5A, **operators unchanged by v2** (ruling §4.10).
   ~~*Superseded by two different open items — R8 and S6.*~~ **`[v2]` those two
   are themselves now CLOSED** by the decomposition-architecture ruling (§7.3).
4. ~~**U15 — the two LOC4 rulings.**~~ **CLOSED in v2.** The canonical
   `docs/Missions/JMP_LOC4_pathB_ruling_v1.md` is **tracked** at HEAD `f6a1130`,
   sha256 `4e7b95d9ecf730a3f820f18f2a9fb207a317775f32165486e6794b92eee8b4bb`; it
   is the file charter §2 item 4 names by exact filename; the competing
   `…_robustness_ruling_v1.md` is no longer on disk, and neither is the
   `docs/design_notes/` duplicate. There is no ambiguity left to escalate and no
   question for the Goal 1 Manager. Verification table at §3.2a(U15); D20's
   source column updated.

### 8.2 PROPOSED-PENDING-RATIFICATION

**`[v2]` This category is now EMPTY.** Both of v1's entries are closed:

1. ~~**U7 — `V_i^dir` cross-check tolerance.**~~ **RESOLVED at `0.5` nats**
   (R-71, as transcribed at §5A.8 V22). §3.2a(U7) records the extraction and the
   v1 internal contradiction it resolves; Stage A confirms against the written
   R-71.
2. ~~**U8 — Shapley-exhaustiveness epsilon.**~~ **RESOLVED — frozen as
   `ε_Shapley` = `1e-9 · max(1, |I^k(∅)|)`** (§3.2a(U8)), adopted to make the
   ruling §3.5(2)–(3) gates checkable, with an explicit scope limit: it governs
   the Shapley arithmetic **only**, and the separate numerical-integration
   stability tolerance continues to govern each `I^k(S)`.
   **v1's standing caveat is spent:** v1 noted U8's `1e-9` was "partially
   superseded" by the V20a/V20b split. V20a keeps `1e-9` as a **hash-identity**
   tolerance under gate §5.4(1); **V20b is retired**; and `ε_Shapley` is a
   **separate, relativised** arithmetic tolerance. The three are now distinct and
   non-competing objects.

### 8.3 Recording notes (no decision required, but Stage A must not trip on them)

1. **U10 — S-10 resolved numeric values: mechanical at freeze.** `theta_hat_j`,
   `se_rob_j`, `lb_j`, `Δ_j`, `θ^sens_j` for `beta_l0_sm` and `beta_w_pexp2` are
   read off the digest-bound accepted source
   `docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv` (sha256 under
   §3.2a(U1)) and substituted into the D15 formula. Arithmetic against a verified
   file, not an open question.
2. **Phase-5 has no `complete/` directory.** Bind by
   `phase5_inference_v1/attempts/…_dryrun_PHASE_5_DRY_RUN_COMPLETE/` (§3.2a(U1)).
3. **`o_nonemployment_key` is the wrong schema shape.** `o` is a predicate
   (`working == 0`, lowest draw index). The config field needs replacing, not
   filling (§3.2a(U2)).
4. ~~**Duplicate U4 ruling copy.**~~ **CLOSED by R-70.2**; one copy remains.
5. **M08 config must not inherit the four-measure P2a list.** §6.4's recording
   note — and note that the legacy list omits both decomposed measures.
6. **`[v2]` Two restricted output files are renamed** (`subgroup_W3_primary_v1.csv`
   → `subgroup_W2_primary_v1.csv`; `subgroup_W3_s10_scenarios_v1.csv` →
   `subgroup_W2_s10_scenarios_v1.csv`). No Stage-D run may emit both variants
   (§6.7).
7. **`[v2]` The monorepo pin was not re-verified** in this pass (repository not on
   this session's reachable path list). Stage A re-verifies
   `27756a06ea189339aa82915ed2124628afed20eb` at freeze.

### 8.4 **`[v2]` Contract status**

```
FREEZE-READY-PENDING(v4-ACCEPT; Stage-A economics review; Goal-1 ratification of V6/V22 and U6 numbers - V20b retired)
```

The three enumerated freeze conditions, spelled out:

1. **v4-ACCEPT** — the E2 documentary closure. Report **v4** must be created per
   ruling §2.2, and must receive the single fresh read-only Codex **ACCEPT** of
   ruling §2.3. On ACCEPT, v4 becomes the parity report of record, an acceptance
   note is created, and the parity axis freezes. **On REJECT the matter returns to
   the deputy.** No gate re-run is authorized. On-disk status: v3 and its change
   log exist; **v4 does not** (§2.1(v)).
2. **Stage-A economics review** — the amended architecture must pass the existing
   independent Stage-A economics/contract review. Ruling §4 closing line:
   *"No welfare execution may begin until the amended contract passes the existing
   Stage-A economics review."*
3. **Goal-1 ratification of the V6/V22 and U6 numbers** — the **V6**
   counterfactual-ESS materiality/escalation number, the **V22** per-coalition
   materiality number (§5A.8), and the **U6** draw-growth decision (build the
   2×/4× datasets, or carry Gate 1(i) BLOCKED under a pre-registered escalation
   rule). **V20b is retired**, so its declared simulation tolerance is no longer
   among the numbers to be ratified.

**Not enumerated by the deputy, and therefore recorded rather than claimed
closed:** **U3** (§8.1 item 1), and the written **R-64** that §2.1's
carry-forwards would rest on (§8.0). Stage A should dispose of both explicitly at
freeze rather than inherit them silently.

**Until conditions 1–3 are met and Stage A freezes this contract, no numerical
welfare execution is authorized.** The Stage-A freeze record, not this
subsection, carries the final status.

### 8.5 **`[v2]` The deputy's return rule (ruling §5, verbatim)**

> The Goal 1 Manager may proceed without deputy contact after:
>
> - report v4 receives final Codex ACCEPT;
> - the execution contract incorporates this decomposition ruling;
> - the independent Stage-A contract review accepts the amended architecture;
> - all other pre-existing freeze items are resolved under manager authority or separately escalated where required.
>
> Return to the deputy only for:
>
> - a valid final E2 REJECT;
> - inability to construct non-degenerate `W2`;
> - a claim that the residual requires a fourth operator before M08 can answer the paper's question;
> - a generic-package change;
> - an integration-gate failure without a frozen rule;
> - a Tier-2 S-10 trigger;
> - or a conflict with LOC4.

**This document discharges the second bullet of the first list** — the execution
contract now incorporates the decomposition ruling. The first, third and fourth
bullets remain outstanding and are §8.4's conditions 1–3.

---

## 9. **`[v2]` Amendment record — v1 → v2**

Documentation-only. Nothing in this section changes an obligation; it exists so
Stage A can audit the transition without diffing 1,842 lines.

### 9.1 Deputy amendment map (ruling §4 item → contract section)

| Ruling §4 item | Requirement | Where applied in v2 |
|---|---|---|
| **1** | replace every statement that `W3` is the primary decomposition target with `W2` | **D19**; **§4** Stage F/G; **§5.1**, **§5.2**, **§5.5**, **§5.6**; **§5A.9.3**; **§6.3.4**; **§6.7**; **§3.3** (charter-divergence note). Full site enumeration at **§9.2** |
| **2** | replace the former `W2` second-check requirement with `W5` as the secondary decomposition | **D19**; **D2 table** (new role column); **§5.1**; **§5.5** final bullet; **§5.6** item 5; **§6.3.4** (`W5` gets no new subgroup table) |
| **3** | retain `W3` as validation-only | **D19**; **D3** note; **§5.1** (ruling §3.1 verbatim + three prohibitions: not redefined, no common-reference `W3`, not decomposed); **§4** Stage E; **§6.3.4** (`W3` stays in the §3.1 family tables) |
| **4** | replace V8/V20 grand-coalition degeneracy with the residual-accounting gates of §3.5 | **§5.4** (five gates verbatim); **§5.4.1** (item-by-item map); **§5A.8** (V8 SUPERSEDED; V20a RETAINED as gate §5.4(1); V20b RETIRED; V20c RETAINED as gate §5.4(4)); **§3.2a(U8)** (`ε_Shapley`) |
| **5** | define `R_bg` and the shares of §3.6 | **D21**; **§5.3** (§3.4 verbatim + source list); **§5.5** (§3.6 verbatim, `s_opp`, four shares, signed); **§5A.7** row 8 |
| **6** | remove any requirement that `I({A,B,P}) = 0` | **§5.4** (gates replace it); **§5A.1**, **§5A.6**, **§5A.7** (each occurrence marked SUPERSEDED with a pointer); **§5A.8** V8/V20b; **§7.1** (re-anchored "Shapley exhaustiveness fails") |
| **7** | remove any claim that the three channels exhaust all household welfare heterogeneity | **§5.2**; **§5.3**; **§5.7** (ruling §3.7 verbatim: *"not a complete causal decomposition of every determinant of welfare"*); **§5A.9.5** fourth row; **§7.3(b)** |
| **8** | preserve `c_ij`, `π`, support, and measure references unchanged across coalitions | **§5.2** (fixed-object list verbatim + confirmation that **V2/V3/V4 are UNCHANGED**); **§5A.0**; **§5A.8** V2/V3/V4 rows |
| **9** | record that no fourth-channel operator is authorized | **§5.2** (ruling §3.3 verbatim, including *"merely naming a fourth channel without an executable counterfactual operator would not constitute a Shapley decomposition"*); **§7.3(b)**; **§5.7** (four-channel design deferred past M08/LOC4) |
| **10** | keep the access/ability/preference operator definitions otherwise unchanged | **§5A** header (v2 amendment scope: five marked touches, no definitional change); **§5A.2**, **§5A.3**, **§5A.4**, **§5A.5** all marked **UNCHANGED**; **D7** |

### 9.1a Instruction map (twelve enumerated instructions → contract section)

| Instruction | Where applied |
|---|---|
| **(a)** `W3` validation-only; no "common-reference W3"; every primary-anchor statement replaced | §5.1; §9.2 enumeration |
| **(b)** `W2` primary, `W5` secondary; `W1`/`W4`/`W6` no Shapley requirement | D19; D2 role column; §5.1; §5.6 items 5–6 |
| **(c)** three-channel game retained; no fourth channel; verbatim "naming a channel without an executable operator" statement | §5.2 |
| **(d)** `R_bg^k` for `k ∈ {W2,W5}`; §3.4 identities and §3.5 gates verbatim; V8/V20a-b-c replaced and marked SUPERSEDED with pointers; `ε_Shapley` = frozen U8 convention; integration tolerance separate and governing; V20a retained as gate §5.4(1); V20c → gate §5.4(4) with §3.4 source list verbatim | D21; §5.3; §5.4; §5.4.1; §3.2a(U8); §5A.8 |
| **(e)** §3.6 headline quantities and `s_opp` verbatim; 2pp trigger on `s_opp`; signed, no suppression, no causal reinterpretation, no silent renormalisation | §5.5; D16; §5.4(5) |
| **(f)** `R_bg` in levels and as a share; never endowment/needs/circumstance/unfairness/causal; §3.7 into the manuscript-caveat plan | D21; §5.7; §5A.9.5 (fourth row) |
| **(g)** `c_ij`, `π`, support, measure references fixed; V2/V3/V4 confirmed unchanged; §5A operators otherwise unchanged; V1/V17/V18 re-anchored to `W2`/`W5` money-metrics | §5.2; §5A header; §5A.8 V1/V2/V3/V4/V17/V18 |
| **(h)** consequential consistency pass: W3-anchored statements, U4 §3.2/§3.3 "primary W3" → "primary W2", V21 onto `W2`, S-10 scenario reporting to `W2` | §9.2 enumeration; §6.3.4; §5A.8 V21; §5A.9.3; §5A.10; §4 Stage G |
| **(i)** front matter HEAD → `f6a1130`; close §8.1 U15; §7.3 both conflicts RESOLVED-BY-DEPUTY-RULING; literature constraint into the prohibitions | front matter; §3.2a(U15) + §8.1 item 4 + D20; §7.3; §7.2a |
| **(j)** status line | §8.4 |

### 9.2 Enumeration of every `W3` → `W2` replacement site

Every site is listed with its **v1 line number** and its **v2 location**. Sites
where `W3` **survives unchanged** are listed separately below, so the enumeration
is complete in both directions.

**Replaced (decomposition-anchored `W3` → `W2`):**

| # | v1 site | v1 text (abridged) | v2 location and disposition |
|---|---|---|---|
| 1 | v1 §3.1 **D19**, line 329 | *"primary anchor `W3`, second check `W2`; `W1`/`W5` … corroborating interpretation only"* | **D19** — rewritten: `W2` primary, `W5` secondary, `W3` validation-only, `W1`/`W4`/`W6` no Shapley requirement. v1's D19 marked SUPERSEDED in full |
| 2 | v1 §3.1 **D2 table**, line 338 | `W3` row, no role column | **D2 table** — role column added; `W3` = VALIDATION ONLY, `W2` = PRIMARY, `W5` = SECONDARY. Measure definitions untouched |
| 3 | v1 §4 item 3 (Stage F), line 639–640 | *"emit the §3.2 subgroup tables for the primary `W3` baseline"* | **§4 item 3** — *"for the primary `W2` baseline (§6.3.2 as rebound at §6.3.4)"*; adds the `R_bg^k` reporting duty |
| 4 | v1 §4 item 4 (Stage G), line 641–643 | §3.3 per-scenario subgroup tables (implicitly `W3`) | **§4 item 4** — per-scenario tables for **`W2`**; 2pp trigger reads on `s_opp` |
| 5 | v1 §5 item 1, line 659 | *"…eight coalitions … for the primary `W3` decomposition (D19)"* | **§5.6 item 1** — eight coalitions for the **primary `W2`** decomposition |
| 6 | v1 §5 item 3, line 662 | *"Verify exhaustiveness to the tolerance of U8 (must be resolved first)"* | **§5.6 item 3** + **§5.4** — five gates at `ε_Shapley`; U8 resolved |
| 7 | v1 §5 item 5, line 665 | *"Repeat for `W2` as the pre-registered second check"* | **§5.6 item 5** — *"Repeat 1–4 for `W5` as the secondary decomposition"*; v1 item 5 marked spent |
| 8 | v1 §5 item 6, line 666–667 | *"Report `W1`/`W5` only as corroborating interpretation"* | **§5.6 item 6** — `W1`/`W4`/`W6` in the family, not decomposed; `W5` is now decomposed, so the corroboration framing no longer applies to it. The no-reconciliation-identity prohibition survives in general form |
| 9 | v1 §5A.7 coalition table row 8, line 949 | role = *"degeneracy target; V8/V20 precondition"* | **§5A.7 row 8** — role = **`R_bg^k = I^k({A,B,P})`**, reported not gated to zero. Rows 1–7 and all operator compositions unchanged |
| 10 | v1 §5A.7 §4.2 closing, line 967 | *"exhaustiveness holds if and only if `I({A,B,P}) = 0`"* | **§5A.7** — SUPERSEDED block quote with pointer to §5.3–§5.4; the telescoping identity itself retained as correct |
| 11 | v1 §5A.1 D1 consequences, line 726 | *"the exhaustiveness precondition is testable (V8)"* | **§5A.1** — SUPERSEDED clause note; the operator statement survives, now tested by gate §5.4(1) |
| 12 | v1 §5A.6 §3.1(b), line 898 | *"the grand coalition is not degenerate, and exhaustiveness fails (charter §9.8; V8's precondition)"* | **§5A.6** — SUPERSEDED clause note; step (b) retained on gate-§5.4(1) grounds |
| 13 | v1 §5A.8 **V8**, line 995 | grand-coalition degeneracy gate | **§5A.8 V8** — SUPERSEDED/withdrawn; struck through with pointer to §5.4.1 |
| 14 | v1 §5A.8 **V20a**, line 1007 | analytic degeneracy, `1e-9` | **§5A.8 V20a** — RETAINED as the mechanical form of gate §5.4(1); tolerance and failure action unchanged |
| 15 | v1 §5A.8 **V20b**, line 1008 | numerical degeneracy, declared simulation tolerance | **§5A.8 V20b** — SUPERSEDED/RETIRED; its Stage-A number removed from §8.4 |
| 16 | v1 §5A.8 **V20c**, line 1009 | enumeration; halt if `c_ij` unassigned | **§5A.8 V20c** — RETAINED as gate §5.4(4)'s background-source enumeration; halt trigger spent (`c_ij` now assigned to the fixed background) |
| 17 | v1 §5A.8 **V20 block**, line 1016 | "Degeneracy, split three ways" | **§5A.8** — retained verbatim as history with a v2 disposition note |
| 18 | v1 §5A.8 **V1 / V17 / V18**, lines 988, 1004, 1005 | *"every `Ω_i^k` unchanged to ≤1e-12"*, measure-unspecific | **§5A.8** — RE-ANCHORED to the `W2`/`W5` money-metrics; tolerances unchanged |
| 19 | v1 §5A.8 **V21**, line 1010 | *"Report `C_A + C_B`, `C_O^(2)`, and their difference"* | **§5A.8 V21** — RE-ANCHORED onto `W2`: `φ_A^{W2} + φ_B^{W2}`, `C_O^{(2),W2}`, and their difference. Still a diagnostic, not a gate |
| 20 | v1 §5A.9.3, lines 1058–1072 | opportunity content ≡ `C_A + C_B`, measure-unspecific | **§5A.9.3** — RE-ANCHORED: `φ_A^{W2} + φ_B^{W2}`, share `s_opp`; reading correction inserted for the quoted *"`C_A + C_B + C_P = I` exactly"* |
| 21 | v1 §5A.10, lines 1110–1112 | *"every `I(S)`, and every Shapley component vary across scenarios"* | **§5A.10** — scope note: `k ∈ {W2, W5}`; `R_bg^k` reported per scenario; scenario subgroup tables emitted for `W2` |
| 22 | v1 §5A.11, lines 1119–1132 | R8 and S6 UNRESOLVED; *"Execution is blocked"* | **§5A.11** — both **CLOSED**; table of v1 → v2 status; pointer to §7.3 |
| 23 | v1 §6.3.2 quoted U4 §3.2, line 1244 | *"For the primary \(W^3\) baseline, report by…"* | **§6.3.2** quote left byte-faithful; **§6.3.4** rebinds the slot to **`W2`**, statistics unchanged |
| 24 | v1 §6.3.2 quoted U4 §3.3, line 1263 | *"…the §3.2 statistics for \(W^3\)…"* per scenario | **§6.3.2** quote left byte-faithful; **§6.3.4** rebinds to **`W2`** |
| 25 | v1 §6.7 file row, line 1541 | `subgroup_W3_primary_v1.csv` | **§6.7** — renamed **`subgroup_W2_primary_v1.csv`**; content unchanged |
| 26 | v1 §6.7 file row, line 1542 | `subgroup_W3_s10_scenarios_v1.csv` | **§6.7** — renamed **`subgroup_W2_s10_scenarios_v1.csv`**; content unchanged |
| 27 | v1 §6.7 paper-facing paragraph, lines 1551–1556 | *"the §3.2 `W3` tables"*, *"where it accompanies the `W3` decomposition"* | **§6.7** — both rebound to **`W2`** |
| 28 | v1 §7.3(a), lines 1658–1674 | R8 UNRESOLVED on charter text | **§7.3(a)** — **RESOLVED-BY-DEPUTY-RULING**; v1 finding retained verbatim as the record |
| 29 | v1 §7.3(b), lines 1676–1690 | S6 UNRESOLVED; charter §9.8 *"W3 Shapley decomposition is exhaustive"* | **§7.3(b)** — **RESOLVED-BY-DEPUTY-RULING**; §9.8's gate re-anchored onto the §5.4(2)–(3) identities for `W2`/`W5` |
| 30 | v1 §7.3 Consequence, lines 1692–1700 | *"Execution of the decomposition is BLOCKED pending deputy resolution"* | **§7.3 Consequence** — no longer blocked by R8/S6; R9 §4.4's fourth-channel proposal explicitly **not adopted** |
| 31 | v1 §8.0 table rows R8/S6, lines 1721–1722 | UNRESOLVED, blocking before Stage F | **§8.0** — both **RESOLVED-BY-DEPUTY-RULING** |
| 32 | v1 §8.1 item 3, lines 1752–1760 | U12 closed but *"superseded by two different open items — R8 and S6"* | **§8.1 item 3** — those two now closed |
| 33 | v1 §8 status + closing list, lines 1809–1841 | `FREEZE-READY-PENDING(deputy-E2; R8/S6; Stage-A-proposed numbers)` | **§8.4** — `FREEZE-READY-PENDING(v4-ACCEPT; Stage-A economics review; Goal-1 ratification of V6/V22 and U6 numbers - V20b retired)` |
| 34 | v1 §6.2 item 1, lines 1158–1159 | deliverable = contract **v1** | **§6.2 item 1** — deliverable = contract **v2**; v1 is immutable history, not a deliverable |
| 35 | v1 front matter, lines 28–31 | `Job_Market_paper` `7d29a1f4…` | front matter — rebound to **`f6a1130`** |
| 36 | v1 §7.1 halt list, line 1578 | *"Shapley exhaustiveness fails"* (grand-coalition reading) | **§7.1** — re-anchored to the §5.4(2)–(3) identity failures |
| 37 | v1 §3.1 **D16**, line 326 | *"≥2pp opportunity-share change"*, share undefined | **D16** — the 2pp trigger reads on **`s_opp`** as defined at §5.5 |
| 38 | v1 §3.1 **D3**, line 313 | build order; *"committed focal pair … = `W3` + `W5`"* | **D3** — build order unchanged; note added that `W3`'s step-1 role is validation-only and that the focal-pair language is a family-presentation statement, not a decomposition anchor |

**`W3` sites deliberately RETAINED unchanged** (validation, family, and
gate-report references — none is a decomposition anchor): v1 lines **313/314**
(D3/D4 build order and active set), **319/321/322** (D9/D11/D12 gate-report
citations), **338** (D2 measure definition), **364/365** (U12/U13 "nonblocking
for Stage 0/`W3`"), **431/579** (source-path citations), **707/989** (§5A.0 and
V2 *"own-set baseline for `W^3`"* reference-invariance), **991/999** (V4/V12 W3
gate-report citations), **1244** (U4 quote, byte-faithful), **1297/1626**
(charter §4.2 quote, byte-faithful), **1305/1312** (D4 sequencing and the
four-measure config trap), **1482** (weights discussion), **1641** (charter §4.3
quote, byte-faithful). Byte-faithful quotations of the charter and of the U4
ruling are **never edited**; where their referent moves, a rebinding note is
added beside the quote (§3.3, §6.3.4, §6.4).

### 9.3 Worktree effect of this pass

| File | Effect |
|---|---|
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v1.md` | **untouched** — byte-identical to its pre-pass state, retained as immutable history |
| `docs/Missions/JMP_M08_singles_welfare_execution_contract_v2.md` | **new** — this file |
| everything else, in all repositories | **unchanged** |

**No computation, no welfare number, no MNL write, no code change, no data
change, no commit.**

