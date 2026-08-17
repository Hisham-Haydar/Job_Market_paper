# JMP-M08 Singles Welfare Execution Contract v1 (DRAFT — UNCOMMITTED)

**Status:** DRAFT produced by M08 Stage 0 (Claude Code, documentation-only). Not
reviewed by Stage A (independent contract/economics review, Opus). Not frozen.
**Do not execute against this draft.** No welfare computation has been performed
to produce it.
**Revision:** finalised under Goal-1 ruling **R-59** (documentation-only pass;
no code change, no data change, no welfare computation). R-59 supplied four full
digests and directed on-disk resolution of the remaining §3.2 register. Every
§3.2 item now carries an explicit status — **RESOLVED**, **PROPOSED-PENDING-
RATIFICATION**, or **ESCALATED** — in §3.2/§3.2a, and §8 has been reduced to the
questions that survive. Nothing in this revision is FROZEN; Stage A still owns
the freeze.
**Amendment (2026-08-06, documentation-only):** incorporates the Deputy
Programme Director's **U4 subgroup reporting ruling**
(`docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md`, sha256
`41061f7ce681f56528cd3576dda707691e3440bac7c35bb6ca4947dde0af9bcb` — restated
2026-08-06 under Goal-1 **R-70.2**, which replaced that path's content with the
faithful deputy byte-copy; the digest cited before the byte-fix was
`b7c0ac18557c13984b685f32f64355c8708fdfd020c1880ae9efd40edce12181`) as §6.3–§6.7,
and the certified Stage-B parity result as §2.1. U4 moves from **ESCALATED** to
**RESOLVED-BY-DEPUTY-RULING**. The narrow Codex T4/T7 re-verification landed
during this pass with **overall REJECT** on report v2's evidence packet (T4
cured, gate numbers independently confirmed, T7 documentary cure incomplete) —
recorded at §2.1(iii); **the Stage-A freeze cannot issue until that is closed.**
No code change, no data change, no welfare computation, no commit. Stage A still
owns the freeze.
**Produced against:** MNL `520441a653f04196bf1e92e3658a478b4feb3718` (clean);
`dclaborsupply-monorepo` `27756a06ea189339aa82915ed2124628afed20eb` (clean);
`Job_Market_paper` `7d29a1f4d03e7be5402b1ed1890242c5f390d6eb` (M07 closeout
commit; 4 files remain deliberately untracked, listed in the Stage-0 report).
**Governing documents (per charter §2, in order):**
`JMP_M07_deputy_closeout_and_identity_ruling_v1.md` →
`JMP_M08_welfare_input_handoff_v1.md` →
`JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md` →
`JMP_LOC4_pathB_ruling_v1.md` → accepted P2a manifests → `JMP_welfare_spec_v5.md`
(only version on disk; `JMP_welfare_spec_latest.md` named in the charter does not
exist as a file — v5 is the highest-numbered spec and is treated as "latest") →
`RURO_welfare_scaffold_design_contract_v2.md`.

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
3. **The narrow Codex re-verification of T4/T7 has since landed, and its overall
   verdict is REJECT.** It was pending when this amendment was drafted; it
   completed during the same documentation pass and is recorded here as it
   actually stands, not as anticipated. Source:
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

   **Consequence — binding.** The Stage-A freeze **does not issue on the current
   report v2**. What is required is narrow and documentary: withdraw or
   evidence-fence the two untraceable claims in report v2 §§3–4 (a report v3, or
   an erratum), then re-verify. **No re-run of the gate is required** — R4 has
   already certified the attempt's numbers independently. The correction cycle for
   this rejection is Stage-B/C business and is **not** performed by this
   amendment. The freeze record, not this subsection, carries the final status.

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
| D3 | Build order | Step 1: validate `W3` end-to-end alone. Step 2: `W5` (access face) + `W2` (2nd Full-Responsibility check) + `W4`/`W6` (Full-Compensation endpoints). Step 3: decide headline empirically; committed focal pair if spread immaterial = `W3` + `W5` | Scaffold contract §5; `JMP_welfare_spec_v5.md` §6 |
| D4 | Active measure set | `["W3","W5","W2","W4","W6","W1"]` (config example matches charter §4.2 build-order narrative exactly) | Scaffold contract §4 |
| D5 | Access/ability/preference parameter membership (47-param baseline) | **Preference (20):** `beta_l0_{sm,sf,f}`, `beta_l_age{,2}_{sm,sf,m,f}`, `beta_l_nkids_{sf,f}`, `theta_l_{sm,sf,f}`, `theta_c_singles`; fixed `theta_l_m=-0.8`, `beta_ll=0`, `beta_c=1`. **Ability (6):** `beta_w_educL`, `beta_w_educH`, `beta_w_pexp`, `beta_w_pexp2`, `sigma`; `beta_w0` common anchor. **Access (23):** `beta_E`, `beta_h_pt1`, `beta_h_pt2`, `beta_h_ft`, `beta_h_lh`; `beta_E_gsur`, `beta_E_drgn2..8`, `beta_E_drgur`, `beta_E_drgmd`, `beta_E_y2015`, `beta_E_y2017`; `beta_occ_{2,3,4}_{m,f}` | `JMP_welfare_spec_v5.md` §2 (table); counts cross-checked against `RURO_welfare_gate_report_W3_v1.md` line "preference 20 / ability 6 / access 23 names" — MATCH |
| D6 | Access-purity rule (channel routing principle) | Education → wage return only → **ability**; never access. Age → experience → ability; age-in-leisure → preference; **never access**. Gender → offers (`beta_occ_*_m/_f`) → access; tastes (`beta_l0_f`, `beta_l_nkids_sf` etc.) → preference. A parameter's normative role follows the channel it acts through, not the observable driving it. Reporting the `[access-only, access+ability]` bracket is mandatory | `docs/France_case/_shared/governance/JMP_ability_opportunity_cut_v1.md` §0–§3 (MNL) — this is the document Step 3 calls "the access-purity rules"; title of its own §2.1 is literally "the access-purity rule binds" |
| D7 | Equalisation operators (qualitative) | **Access:** set access blocks to a common offer environment; hold ability+preference at actual; recompute. **Ability:** neutralise wage-technology's dependence on own education/experience/residual productivity (`beta_w0` stays anchor); hold access+preference; recompute. **Preference:** assign a common reference preference (horizontal reference `R^h` named as "the natural choice," not yet a hard freeze — see U15); revalue feasible sets; recompute | `JMP_welfare_spec_v5.md` §2; scaffold contract §3.2/§7; ability/opportunity-cut memo §5 |
| D8 | Inequality index | Gini, mandatory/primary (`active_indices: ["gini"]`). Sensitivity-only secondary indices: CV², Theil-L, Atkinson(ε=1), Atkinson(ε=2) | Scaffold contract §4 |
| D9 | Engine-parity tolerance (Gate 0) | Smoke `1.0e-8`; production `1.0e-6` (max abs Δ negLL vs estimator negLL) — achieved machine-exact (0.0/0.0/1.1e-13) in the Stage-One production run | `RURO_welfare_gate_report_W3_v1.md` Gate 0 table + "Tolerances" line; `scripts/welfare/configs/welfare_stage1_w3.yaml` |
| D10 | Reprice-parity tolerance | `1.0e-6` euros absolute (`stage2.parity_grid.parity_tol`) — **note (see U-source-mismatch below): this lives in Stage-Two config, not literally inside `RURO_welfare_scaffold_design_contract_v2.md`**, which the charter names as "the frozen scaffold contract" for §6 Stage A thresholds | `scripts/welfare/configs/welfare_stage1_w3.yaml` |
| D11 | Inversion-convergence tolerance (Gate 2) | Residual `1e-6`; bracket width `1e-9`; reference recovers zero exactly (`Φ_i(0)=0` to solver tolerance, `≈−2.91e-10`); monotonicity required; converged for all 12,445 households in the Stage-One production run | `RURO_welfare_gate_report_W3_v1.md` §"Commands run" tolerances line + Gate 2 table |
| D12 | Reference-coverage gate (Gate 4) definition | All required `c_ij` for the reference packages of `Ā/J/o` must be finite and positive before any reference is evaluated; no wholesale EUROMOD rerun; no silent interpolation; missing packages **block**, not approximate. For `W3` (own set, no `Ā/J/o` needed) this passed in Stage One (0 non-positive across all 3 groups) | Scaffold contract §6.1(iii); `RURO_welfare_gate_report_W3_v1.md` Gate 4 |
| D13 | Household-unit integrity gate (Gate 3) | One `Ω_i` per couple from joint utility/joint budget; no per-capita split; type-conditional references; passed in Stage One for all 3 groups | Scaffold contract §6.3; gate report Gate 3 |
| D14 | Welfare code paths (scaffold + application) | MNL: `scripts/welfare/welfare_core.py`, `welfare_vdir.py`, `run_stage1_w3.py`, `run_stage2_parity.py`, `configs/welfare_stage1_w3.yaml`, `configs/welfare_p2a_singles2016.yaml`. Nested (read-only reuse): `dclaborsupply/welfare/{__init__.py,protocol.py}`, `dclaborsupply_app/welfare/{__init__.py,core.py,measures.py,vdir.py}` | Stage-0 inventory (§2 of accompanying report), hashes recorded there |
| D15 | S-10 four scenarios (formula) | `Δ_j = min{0.5·se_rob_j, 0.5·(θ̂_j − lb_j)}`; `θ^sens_j = θ̂_j − Δ_j`. Four scenarios: (1) baseline; (2) `beta_l0_sm` at sensitivity value; (3) `beta_w_pexp2` at sensitivity value; (4) both jointly. No search beyond these four points | `JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md` §3–4 |
| D16 | S-10 material-loading trigger | ≥1% change in mean/median welfare; ≥0.005 absolute Gini change; ≥2pp opportunity-share change; sign/ordering change in a headline decomposition component; qualitative-conclusion change | S-10 spec §6 |
| D17 | Vigilance treatment, `beta_l0_sf` | Monitored alongside the two flagged coordinates in every welfare/decomposition output; robust CI lower endpoint `0.05467` sits adjacent to the male counterpart's recorded `0.05`-class bound; its own bound is **not** in accepted artifacts; nothing asserted in paper text absent an accepted bound record; not perturbed, not itself a Tier-1 scenario coordinate | Handoff §2 item 5; charter §6 (final bullet) |
| D18 | Disclosure policy | No household-level welfare or microdata artifact in the public `Job_Market_paper` repository (charter acceptance gate #13); restricted numerical artifacts, manifest, and acceptance pointer live in MNL under an approved P2a welfare production namespace (charter §8 "MNL") | Charter §8, §9.13 |
| D19 | Shapley decomposition scope | Three-way {access, ability, preference}; 3!=6 orderings; primary anchor `W3`, second check `W2`; `W1`/`W5` reported as corroborating interpretation only, **never** a numerical reconciliation identity | Charter §4.3; `JMP_welfare_spec_v5.md` §1.4/§6 (D2); scaffold contract §9 |
| D20 | LOC4 sequencing (Path B) | Baseline welfare proceeds on the certified common-dispersion model now; LOC4 four-density robustness is mandatory **before final quantitative decomposition claims**, not before the first prototype | `JMP_LOC4_pathB_ruling_v1.md` (the version the charter cites by exact filename); handoff §2 item 3; charter §5.5 |

**D2 in full (the measure table):**

| Measure | Reference / construction | Ind y | Ind A | Normative reading |
|---|---|---|---|---|
| `W1` | preferred job in own set `A`, pay ignored | + | − | compensate pay; responsible for the set |
| `W2` | best-paid equivalent in own set `A` | − | − | Full Responsibility (own everything) |
| `W3` | laissez-faire in own set `A`, with pay | − | − | Full Responsibility (laissez-faire) |
| `W4` | staying-home equivalent (non-employment `o`, `y(o)=0`) | + | + | Full Compensation |
| `W5` | uniform subsidy to reference set `Ā` | − | + | compensate the set; responsible for pay |
| `W6` | best job in whole economy `J` | + | + | Full Compensation (+ Weak Responsibility) |

### 3.2 UNDEFINED items — register with R-59 status

Status vocabulary: **RESOLVED** = value extracted from a committed on-disk source
and recorded verbatim in §3.2a; **PROPOSED-PENDING-RATIFICATION** = no operative
value exists on disk, a value is proposed with a one-line rationale and is *not*
frozen; **ESCALATED** = cannot be resolved from the repositories, goes to the
Goal 1 Manager as a §8 question.

| # | Object | What exists | What is missing | Blocking? | **R-59 status** |
|---|---|---|---|---|---|
| U1 | Full artifact hashes | Truncated hashes only: theta bytes `c024b893…f0580d`, Phase-5 bundle `d08947ce…`, reporting map `89a0465c…`, extraction memo `b800d0e3…`, model anchor `982c5221…` | Full untruncated hex digests | **Yes** — charter §3 states explicitly a truncated hash "is not sufficient for execution"; Stage A must resolve and record full identifiers | **RESOLVED** — all five full digests in §3.2a(U1); each independently recomputed/matched against a committed artifact |
| U2 | Non-employment option `o` (needed for `W4`) | Config key name only: `o_nonemployment_key: "..."` (literal ellipsis placeholder in the scaffold contract) | The actual alternative key in the P2a singles choice set that represents "staying home" | **Yes** — `W4` cannot be built without it | **RESOLVED** — with a schema correction: **no alternative *key* exists**; `o` is resolved by predicate, §3.2a(U2) |
| U3 | "up1 manifest note" | Nothing located | Exhaustive search (filename + content grep across MNL, Job_Market_paper, `dclaborsupply-monorepo`, plus `git log --all --grep`) found **no** file, commit message, or in-document reference matching "up1" in any welfare-adjacent context | **Yes/clarify** — cannot rule out this is a typo or a not-yet-created artifact; flagged as a direct question to the Goal 1 Manager rather than guessed | **ESCALATED** — R-59 gave no direction on U3; unchanged |
| U4 | Subgroup list "already pre-registered" | Both the charter (§6) and the S-10 spec (§5, §7) refer to pre-registered subgroup summaries as if they exist | No subgroup list was found anywhere in MNL or `Job_Market_paper` docs (the only "subgroup" hits are the charter/S-10 references themselves, unrelated inference-manuscript uses, and two unrelated archived docs) | **No longer blocking** — the list now exists | **RESOLVED-BY-DEPUTY-RULING** — supplied by `docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md` (Deputy Programme Director, 2026-08-05), incorporated at §6.3–§6.7; §3.2a(U4) records the resolution and its supporting sources |
| U5 | ESS threshold (frozen value) | Contract schema: `ess_threshold: "declared"` (placeholder). Stage-One **operational** run used `30` | A value frozen *in* the contract/handoff for M08, vs. reuse of the Stage-One operator choice | **Yes, narrow** — 30 is a strong candidate (used in the only production run to date) but is not yet adopted as M08's frozen number | **RESOLVED** — adopt `ess_threshold = 30`, §3.2a(U5) |
| U6 | Draw-growth stability tolerance | Contract schema: `tolerance: "declared"` (placeholder); `draw_multipliers: [1,2,4]` | 2×/4× draw-multiplier datasets **still do not exist on disk** (confirmed: only the coarser 20×20 grid and the production 901-alt set exist); Gate 1(i) was BLOCKED in Stage One and remains blocked now; no tolerance number was ever set because the check never ran | **Yes** — this gate cannot pass without new data; M08 must either build the 2×/4× datasets or carry the BLOCKED status forward under a pre-registered escalation rule | **ESCALATED** — a data-creation decision, not a documentation gap; R-59 gave no direction; unchanged |
| U7 | Direct-vs-IS (`V_i^dir`) agreement tolerance | Contract text: "require agreement within tolerance" (prose, no number) | Numeric tolerance; the cross-check itself was never run (redraw machinery not implemented in Stage One) | **Yes** — same blocker as U6; the escalation trigger ("persistent disagreement on the flagged subset") cannot fire without both the machinery and the tolerance | **PROPOSED-PENDING-RATIFICATION** — a Stage-One code constant exists (`0.5` nats on high-ESS `\|delta_common\|`) but was never ratified for M08; §3.2a(U7) |
| U8 | Shapley-exhaustiveness numeric tolerance | "Components must sum **exactly** to `I(Ω^k)`" (qualitative) | An explicit numeric epsilon for "exactly" (floating-point tolerance) | **Yes, narrow** — needed for Stage F's gate to be checkable in code | **PROPOSED-PENDING-RATIFICATION** — no Shapley constant exists anywhere in `scripts/welfare/`; §3.2a(U8) |
| U9 | MNL production output namespace | Existing precedents on disk: `outputs/welfare/fastlane/`, `outputs/welfare/stage1_w3/`, `outputs/welfare/fastlane_anchors_v{1,2,3}/`; separately, project memory records a P2a-singles-specific precedent path (`outputs/welfare/p2a_singles2016/`) used for a related but distinct welfare pipeline | Charter §8 explicitly forbids inventing a path in prose before repository inspection; no M08-specific namespace has been selected | **Yes** — required output location for restricted artifacts/manifest | **RESOLVED** — `outputs/p2a_singles2016/region_live_v1/welfare_m08_v1/` under the `attempts/` transaction pattern, §3.2a(U9) |
| U10 | S-10 resolved numeric values | Formula (D15) is exact | `theta_hat_j`, `se_rob_j`, `lb_j`, `Δ_j`, `θ^sens_j` for `beta_l0_sm` and `beta_w_pexp2` are **not computed in this draft** — the S-10 spec itself requires they be resolved "before execution," and this Stage-0 pass performed no welfare/parameter computation per its own charter. The now-committed `FR_P2a_phase5_parameter_reporting_map_v1.csv` (Job_Market_paper) is the correct accepted source for Stage A to pull them from | **Yes** — pre-execution requirement, explicitly out of scope for Stage 0 | **MECHANICAL-AT-FREEZE** — the source artifact is digest-bound under U1, so Stage A pulls the numbers against a verified file and substitutes them into D15; arithmetic, not an open decision (§8.3 item 1) |
| U11 | Reference ability set `Ā` (needed for `W5`) | A default is named (`type_conditional_median_opportunity`) with one listed sensitivity (`maximal_opportunity`) | A single ratified primary choice for M08 (currently framed as a config option, not a freeze) | **Yes, narrow** | **RESOLVED** — R-59 ratifies `type_conditional_median_opportunity`; verbatim source in §3.2a(U11) |
| U12 | Common reference offer environment (access-equalisation operand) | Qualitative description only ("population-average offer density, or a reference cell") | A specific frozen choice | Nonblocking for Stage 0/`W3` build; **blocking before Stage F** (decomposition) | **RESOLVED-BY-RULING (R-71)** — superseded 2026-08-06: the design memo `JMP_M08_access_equalisation_operand_design_v1.md` (D1–D10, V1–V13) is ratified by R-71 and transcribed at **§5A**. The prior "no on-disk candidate / ESCALATED" status is history. *Two items remain open and are not U12: R8 and S6, at §7.3.* |
| U13 | Reference preference `R` for preference-equalisation | Horizontal reference `R^h` named as "the natural choice" | A hard freeze (currently a recommendation, not a ratified decision) | Nonblocking for Stage 0/`W3`; **blocking before Stage F** | **RESOLVED** — R-59 ratifies the named default `R_h`; verbatim source in §3.2a(U13) |
| U14 | Pinned-preference held-vs-swapped switch | Config flag exists; default recorded is `held` | Explicit Stage-A ratification of `held` for M08 (the flag "must exist and be honoured," default stated but not yet confirmed as M08's choice) | **Yes, narrow** — affects the couples opportunity-share (informational only for M08, which is singles-only, but the switch is shared machinery) | **RESOLVED** — R-59 ratifies `held`; verbatim source in §3.2a(U14) |
| U15 | Two non-identical LOC4 rulings | `docs/design_notes/JMP_LOC4_pathB_ruling_v1.md` (cited by charter §2 item 4; 5-item materiality rule) vs. `docs/Missions/JMP_LOC4_pathB_robustness_ruling_v1.md` (**not** cited by the charter; different, more elaborate materiality rule; names a distinct mission "JMP-M08R") — both currently uncommitted/untracked in `Job_Market_paper` | Which ruling governs LOC4/M08R materiality is inconsistent across the two documents | Nonblocking for M08 itself (both agree on Path-B sequencing); **flag for the Goal 1 Manager** before LOC4/M08R starts | **ESCALATED** — R-59's byte-identity check **FAILS**: the two files differ in name, size, and digest, and **neither is committed**; §3.2a(U15) |

### 3.2a R-59 resolutions — values, sources, and exact status

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

#### U7 — `V_i^dir` cross-check tolerance · **PROPOSED-PENDING-RATIFICATION**

`RURO_welfare_stage2_vdir_crosscheck_v2.md` contains **no** direct-vs-IS agreement
tolerance — its only numeric tolerance is the reprice-parity `1e-6` (D10). A
Stage-One **code** constant does exist and is recorded here verbatim:

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

**PROPOSED:** `|V_i^dir − V_i^IS| ≤ 0.5` nats, evaluated on the like-for-like
common basis and applied only to **high-ESS** households (ESS ≥ 30 per U5).
*Rationale:* it is the only operative agreement threshold in the Stage-One code,
it is already the gate the singles `V_i^dir` smoke enforces, and restricting it
to high-ESS households mirrors that code exactly — but it was written for a
utility-only anchor gate and has never been ratified as M08's cross-check
tolerance, so it is **not FROZEN**.

#### U8 — Shapley-exhaustiveness epsilon · **PROPOSED-PENDING-RATIFICATION**

Search of `MNL scripts/welfare/` (`*.py`, `*.yaml`) for `shapley` returns **zero
matches**: no Stage-One implementation, and therefore no constant, exists.
**PROPOSED:** `|Σ_k φ_k − I(Ω)| ≤ 1e-9 · max(1, |I(Ω)|)`. *Rationale:* `1e-9` is
the tightest tolerance already in the Stage-One tolerance line (the inversion
bracket width, D11), and relativising it keeps the gate meaningful for Gini-scale
and euro-scale indices alike. **Not FROZEN** — no code, no precedent, no ruling.

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
`maximal_opportunity` retained as the listed sensitivity only.

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
| Bytes | 5,168 (was 5,164 — the 4-byte difference is two U+201C/U+201D quotation glyphs at ruling §2, restored from the deputy's faithful byte-copy) |
| Decision-maker / date | Deputy Programme Director, 2026-08-05 |
| Status in this contract | Incorporated at **§6.3** (dimensions, statistics, disclosure — verbatim), **§6.4** (label/weighting sources), **§6.5** (implementation path), **§6.6** (output files) |
| Tracking | Untracked; rides the Stage-A freeze commit |

The ruling's own §5 requires exactly this incorporation before Stage-D welfare
execution, and its §6 states that it *"closes U4."* U4 is therefore no longer a
§8.1 escalation. The dimensions it pre-registers are **sex**, **education
(`educ3`)**, and **broad region (`drgn1`)**; it explicitly **excludes** age bands
and occupation from the mandatory list, with reasons quoted at §6.3.

A second copy of the same ruling exists at
`docs/design_notes/JMP_M08_U4_subgroup_reporting_ruling_v1.md` (untracked,
5,168 bytes, sha256
`41061f7ce681f56528cd3576dda707691e3440bac7c35bb6ca4947dde0af9bcb`).
The two differ **only** in that the `docs/design_notes/` copy renders one pair of
quotation marks in §2 (Age) as U+201C/U+201D typographic quotes where the
`docs/Missions/` copy uses ASCII `"`. No substantive text differs. The
`docs/Missions/` copy is the one this contract cites and the one the Goal 1
Manager placed under the ruling's §5 instruction; Stage A should direct whether
the `docs/design_notes/` duplicate is removed or retained as history.

**Prior status, retained as history.** R-59(g)'s targeted re-search of exactly
the four named sources returned **ABSENT** — every hit was a *reference to* a
pre-registered list; none was a list:

| Source | `grep -i subgroup` result |
|---|---|
| `Job_Market_paper docs/Missions/JMP_M08_singles_welfare_decomposition_mission_charter_v1.md` | 4 hits, all referential — L111 *"No post-hoc factor definitions, reference sets, subgroup lists, or thresholds."*; L134 *"exact subgroup list already pre-registered;"*; L264 *"pre-registered subgroup summaries;"*; L294 *"…decomposition, subgroup, convergence, and invariance outputs."* |
| `MNL docs/jmp_methodology/RURO_welfare_gate_report_W3_v1.md` | **0 hits** |
| `MNL docs/jmp_methodology/RURO_welfare_scaffold_design_contract_v2.md` | **0 hits** |
| `Job_Market_paper docs/design_notes/JMP_M07_S10_tier1_welfare_sensitivity_specification_v1.md` | 1 hit, referential — L86 *"subgroup summaries already pre-registered for the baseline;"* |

The list does not exist on disk. It must be supplied or authored-and-ratified
before Stage E/G, since both consume it (§8 Q2).

#### U15 — LOC4 ruling byte-identity · **FAILS → ESCALATED**

R-59(f) asked whether `docs/design_notes/JMP_LOC4_pathB_ruling_v1.md` is
byte-identical to "the committed `docs/missions/` copy". Two findings:

| File (`Job_Market_paper`) | Bytes | SHA-256 | Tracked by git? |
|---|---|---|---|
| `docs/design_notes/JMP_LOC4_pathB_ruling_v1.md` | 4,261 | `4e7b95d9ecf730a3f820f18f2a9fb207a317775f32165486e6794b92eee8b4bb` | **No** (`??` untracked) |
| `docs/Missions/JMP_LOC4_pathB_robustness_ruling_v1.md` | 3,402 | `b2ddee467702425bcd9bf233e4eca92c8c155784c1c4f68fb6d6e01174282238` | **No** (`??` untracked) |

1. **Not byte-identical** — different filenames, sizes, and digests.
2. **Neither is committed.** `git ls-files docs/design_notes/ docs/Missions/ | grep -i loc4`
   returns nothing, so the premise "the committed `docs/missions/` copy" has no
   referent. There is no `docs/missions/JMP_LOC4_pathB_ruling_v1.md` at all —
   only the differently-named `…_robustness_ruling_v1.md`.

U15 therefore stands as originally recorded, now with hashes. D20 continues to
cite the charter-named file (`JMP_LOC4_pathB_ruling_v1.md`) as governing, since
the charter names it by exact filename; the other document remains uncited.

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

---

## 4. The single authorized welfare execution (Stage D–G)

Authorized **only** after Sections 1–2 close (parity passes) and Stage A
(independent review) freezes this contract with all of §3.2's blocking items
resolved.

1. **Stage D — integration certification:** reproduce estimator/welfare
   engine parity at accepted `θ̂` (D9); compute household ESS diagnostics
   (threshold per U5, resolved); run the pre-registered redraw cross-check on
   the flagged set (blocked on U6/U7 until resolved); run draw-growth
   stability (blocked on U6); apply the frozen escalation rule; verify
   inversion convergence (D11) and invariances; record a restricted-artifact
   manifest at the namespace resolved under U9.
2. **Stage E — baseline family:** compute `W1..W6` in build order D3/D4 (the
   charter §4.2 set, per §6.4); report per D-items 5–13 diagnostics; emit the
   §3.1 subgroup tables required by §6.3.2 (six measures × {sex, education});
   no stochastic-dominance exercise.
3. **Stage F — decomposition:** per §5 below; emit the §3.2 subgroup tables for
   the primary `W3` baseline (§6.3.2), noting that **no subgroup-level Shapley
   decomposition is required or permitted** in M08.
4. **Stage G — S-10 Tier-1:** exactly the four scenarios of D15, with the
   resolved numeric values of U10; report per D16; emit the §3.3 per-scenario
   subgroup tables (§6.3.2); monitor `beta_l0_sf` per D17 without perturbing it.

Subgroup reporting at Stages E–G is governed throughout by §6.3–§6.7 (dimensions,
statistics, `dwt` weighting, `SUPPRESSED_LT30` disclosure, output files). Any node
pricing performed at Stage D uses **target-only D-BEN Option B geometry**; joint
batching is not licensed (§2.1(iv)).

**No welfare computation, code change, or numerical execution has occurred
under this draft.** Everything in this section is a specification of what
Stage D–G will do once authorized, not a record of anything done.

---

## 5. Decomposition (Shapley–Shorrocks, per charter §4.3 / §7 Stage F)

1. Evaluate the eight coalitions of the three-channel {access, ability,
   preference} Shapley game for the primary `W3` decomposition (D19).
2. Compute exact Shapley contributions for each channel using the operators
   of D7, with the resolved operands of U11–U14.
3. Verify exhaustiveness to the tolerance of U8 (must be resolved first).
4. Report access-only and access-plus-ability shares as a bracket (D6), never
   a single point.
5. Repeat for `W2` as the pre-registered second check.
6. Report `W1`/`W5` only as corroborating interpretation — never a numerical
   reconciliation identity (D19).
7. Every result is model-conditional and non-causal; the preference-related
   component is never labelled "responsibility" (charter §4.3).

The operators, operands, coalition structure, Shapley weights, and validation
checks referred to in items 1–4 are transcribed in full at **§5A**, which
supersedes the placeholder cross-references to "the operators of D7, with the
resolved operands of U11–U14" wherever the two differ.

---

## 5A. Decomposition operators — verbatim transcription under Goal-1 R-71 / R-72

**Status.** Transcribed 2026-08-06 (documentation-only; no computation, no
welfare number, no commit) under Goal-1 rulings **R-71** and **R-72**, which
ratify the two design memos below. The memos are the binding source; this
section is a verbatim transcription so that the execution requirements are
readable without leaving this file, exactly as §6.3 does for the U4 ruling.
**Where transcription and source could ever diverge, the memos govern.**

| Register item | Document | sha256 |
|---|---|---|
| **U12** — access-equalisation operand (`g_ref`) | `docs/Missions/JMP_M08_access_equalisation_operand_design_v1.md` | `41372e8e193bf5e9a82f2b1dca184545f4c1c1bd875d281031cdf589f2f3a872` |
| **R9** — ability operator (`B`) and preference operator (`P`) | `docs/Missions/JMP_M08_ability_preference_operators_design_v1.md` | `868e7388ab4a1d64f48933064f204c91f2532a577b49a042941f82012270b419` |

**Nothing in this section is FROZEN.** Stage A owns the freeze, and §5A.11
records two items that, on the Step-0 charter reading recorded at §7.3, remain
**UNRESOLVED** and block execution.

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
paragraph are to U12's own sections, transcribed here at §5A.2 and §5A.5.
"V8" is superseded by V20a/b/c — see §5A.8.)*

**Ratified by R-71** as an amendment to `RURO_welfare_scaffold_design_contract_v2.md`
§7 (name-list → cell routing).

### 5A.2 The access operator `A` / operand `g_ref` (U12 §3, verbatim)

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

### 5A.3 The ability operator `B` (R9 §2, verbatim)

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

### 5A.4 The frozen joint occupation object `Π` and its four conditionals (R9 §2.5, verbatim)

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

### 5A.5 GSUR × educ slot table and the mirror guards

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

### 5A.6 The preference operator `P` (R9 §3, verbatim)

> ### 3.1 What is heterogeneous in `u_i`, and the necessary distinction
>
> `u_i(c_ij, ℓ_ij; θ^pref)` carries **two** sources of cross-household heterogeneity in the singles P2a application, and the operator must treat them differently:
>
> **(a) Covariate arguments** — the taste shifters entering the leisure term: `age_norm`, `age_norm2`, the education-in-leisure dummy (`beta_l_educH_*`), and the children term (`beta_l_nkids_sf`). These are substituted by dwt-weighted references, exactly as `A` and `B` substitute theirs. **The operator substitutes covariate arguments; it never re-estimates a coefficient** (charter §5.3, §10).
>
> **(b) Group-specific coefficient blocks** — singles male and singles female carry separate preference blocks (`beta_c_sm/sf`, `theta_c_*`, `beta_l0_sm/sf`, `theta_l_sm/sf`, `beta_l_age_*`, `beta_l_age2_sm/sf`, `beta_l_nkids_sf`). This is **gender-in-tastes**, which the bookkeeping assigns to preference and declares non-compensable. Non-compensable means *the paper does not compensate it*; it does **not** mean the preference channel excludes it. If `P` leaves the group-specific blocks standing, gender-in-tastes survives all three operators, the grand coalition is not degenerate, and exhaustiveness fails (charter §9.8; V8's precondition).
>
> `P` therefore has two steps: a **covariate-substitution step** (a) and a **group-block selection step** (b). Step (b) is a *selection among accepted coordinates of `θ̂`* — not an estimation, not a re-fit, and not a modification of any accepted value. It is nonetheless the single most consequential unratified choice in this memo (§7, item S2).
>
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

| # | `S` | Operator composition | Role |
|---|---|---|---|
| 1 | `∅` | identity | baseline `I(Ω^k)`; the total being decomposed |
| 2 | `{A}` | `g_ref` access cells; own educ/pexp; own tastes | access-only marginal base |
| 3 | `{B}` | `ē, p̄ₑₓₚ, p̄ₑₓₚ²`; `p̃(loc4\|dgn)`; own access; own tastes | ability-only marginal base |
| 4 | `{P}` | reference taste covariates + reference group block; own `g` | preference-only marginal base |
| 5 | `{A,B}` | full opportunity equalisation; `p̄̄(loc4)`; own tastes | **headline opportunity coalition** (charter §4.3) |
| 6 | `{A,P}` | access + preference; own wage technology arguments | ability-residual coalition |
| 7 | `{B,P}` | ability + preference; own access | access-residual coalition |
| 8 | `{A,B,P}` | grand coalition | degeneracy target; V8/V20 precondition |

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

**Commutation (R9 §4.3), verbatim:**

> **Claim.** For any `S`, `I(S)` is independent of the order in which the operators in `S` are applied.
>
> **Justification.** Under D1 each operator substitutes values into a set of argument slots of a fixed evaluated function; the slot sets assigned to the three channels are pairwise disjoint. Substituting into disjoint slots of a function evaluation is order-independent — it is not composition of maps on a shared state, it is assembling one argument tuple. Two cells are *shared* across channels, and both are handled so that commutation survives:
>
> - **GSUR×educ** (§2.6): a product of two slots, one per channel; each operator writes only its own slot.
> - **The occupation table** (§2.5): both operators select a conditional of one frozen joint `Π`, indexed by which conditioning coordinates remain at own; the selection is path-independent by construction.
>
> There is one asymmetry worth naming: `P`'s step (b) substitutes a *coefficient block*, not an argument. It still commutes with `A` and `B`, because `θ^pref` occupies no cell either operator touches (`A` and `B` act only inside `log g`). Asserted by **V19**.

### 5A.8 Validation checks V1–V23, with R-71 / R-72 tolerances

Assertions and failure actions are transcribed **verbatim** from U12 §7 (V1–V13)
and R9 §7 (V14–V23). The **Tolerance / status** column records the R-71 and
R-72 dispositions.

| # | Check | Assertion (verbatim) | Tolerance / status | On failure (verbatim) |
|---|---|---|---|---|
| **V1** | Fixed point / idempotence | For a household (or synthetic test row set) whose access-assigned arguments equal `x̄^acc`, the access operator returns `V_i` and every `Ω_i^k` unchanged to ≤1e-12. | **`1e-12`** (R-71 R7) | Gate the run. |
| **V2** | Reference coalition-invariance | Each measure's reference construction (own-set baseline for `W^3`, `Ā`, `J`, `o`) and the `c_ij` matrix are hash-identical across all eight coalitions. | **exact** (hash-identical) | Gate. Prevents the reference co-moving with the channel and cancelling the effect. |
| **V3** | π-invariance | The `prior` column is hash-identical across all eight coalitions. | **exact** (hash-identical) | Gate (contract §3.1). |
| **V4** | No new package | Alternative support, row count, and `c_ij` hash unchanged under every coalition ⇒ the reference-coverage / EUROMOD gate (contract §6.1(iii), W3 Gate 4) is not re-triggered, and `abar_j_o_required` is unchanged. | **exact** (hash-identical) | Gate; a failure means the operand has silently become a set-substitution. |
| **V5** | Density integrity | `p̄(loc4 \| educ3)` sums to 1 within each education cell; counterfactual `log g` finite on every row; count of non-finite = 0. | as stated in the assertion | Gate. |
| **V6** | Counterfactual ESS | Re-run the contract §6.1(ii) ESS diagnostic (`ESS_i`, max normalised weight) under **every non-baseline coalition**. The counterfactual changes the IS *target* while the proposal is unchanged, so baseline ESS does not transfer. Baseline singles ESS is already weak (W3 gate report: median 20.3 / 18.8; 1,918/2,243 and 2,493/2,764 below the threshold of 30). | ESS threshold **30** (ratified); **materiality/escalation number PROPOSED-AT-STAGE-A** | Apply the frozen escalation rule to the counterfactual, not only the baseline. If the flagged set widens materially and `V_i^dir` remains blocked, **halt** (charter §11). |
| **V7** | No double counting with the wage/occupation technology | (a) the 47 coordinates form an exact partition over preference/ability/access cells — no coordinate in two channels, none omitted; (b) the per-row `log g^W` contribution is **bitwise identical** between baseline and access-equalised runs, confirming `δ_occ`, `μ_i`, `σ` are untouched by the access operator. | (a) exact partition; (b) **bitwise** | Gate. Membership is frozen and unchanged after results (charter §9.10). |
| **V8** | Grand-coalition degeneracy | With access+ability+preference all equalised, `I(Ω^k)` ≤ the frozen tolerance. | **SUPERSEDED by V20a/b/c** (R-72, adopting R9 item S4). V8's single-tolerance form is not executed. | Record the residual and **halt**; do not renormalise silently. Exhaustiveness (charter §9.8) is the acceptance gate. |
| **V9** | Sex-pooling audit | Under access equalisation, the between-sex difference in mean counterfactual access index is exactly zero. | exact (as stated) | Report; a non-zero value means a sex-conditioned cell was missed. |
| **V10** | Directional sanity (reported, not gated) | Households whose own access index is below the reference in every access cell weakly gain. | not gated | Report. Not a theorem once occupation composition interacts with own wage technology; gating it would be an invented identity. |
| **V11** | Determinism | Bit-for-bit reproducible on re-run given identical inputs (mirrors contract §5 Step 1(d)). | **exact** (bit-for-bit) | Gate. |
| **V12** | Block-count reconciliation | The W3 gate report records `welfare.blocks` as preference 20 / ability 6 / access 23 = **49 names** against a **47**-coordinate certified vector. Stage A must reconcile the arithmetic against the frozen spec YAML and the accepted θ̂ (handoff §1) and **halt** if the declared membership is not an exact partition. That report was also produced on the pooled couples-inclusive build at working-tree HEAD `7cac2e3`; per charter §2 its membership counts are indicative for P2a singles and are not imported as validated. | exact partition | *(halt, per the assertion)* |
| **V13** | Occupation-term separability | Stage A must bind each factor of §1.1 to the exact engine term (`log_h`, `log_w`, `log_market`, and wherever the occupation contribution is assembled) and **halt** if the occupation contribution is not separable from the market index in the accepted production path — the access operator is not implementable without that separation. | binding check | *(halt, per the assertion)* |
| **V14** | Operator commutation / mixture path-independence | For every coalition, applying the constituent operators in both (all) orders yields bitwise-identical resolved objects; the `{A,B}` occupation object equals the frozen `p̄̄(loc4)`; the GSUR×educ term matches the §2.6 table cell-for-cell. | **exact** (bitwise) | Gate. A failure means the D1 slot disjointness is violated somewhere. |
| **V15** | Ability V7-analogue (mirror guard) | Under `B`, the following are bitwise invariant per row: the `dgn` conditioning of the occupation availability weights, the region/GSUR level cells of `g^E`, `g^H`, `π`, and `c_ij`. | **exact** (bitwise) | Gate. This is the operational form of §2.7. |
| **V16** | Preference V7-analogue | Under `P`, `log g` is bitwise invariant per row in **all** factors, and `c_ij` and `π` are bitwise invariant. | **exact** (bitwise) | Gate. |
| **V17** | Ability fixed point | A household (or synthetic row set) at `(ē, p̄ₑₓₚ, p̄ₑₓₚ²)` and in the reference education cell sees `V_i` and every `Ω_i^k` unchanged to ≤ `1e-12` (mirror of V1's ratified tolerance). | **`1e-12`** | Gate. |
| **V18** | Preference fixed point | A household at the reference taste covariates **and** in the reference group block sees `V_i` and every `Ω_i^k` unchanged to ≤ `1e-12`. Requires that the reference group block be an actual accepted block — which is why P2 fails. | **`1e-12`** | Gate. |
| **V19** | No re-estimation, mechanically asserted | The 47-coordinate `θ̂` is bitwise identical in every coalition, with the sole exception of the declared step-(b) substitution; the substitution map is hash-recorded and is a pure selection among accepted coordinates. | **exact** (bitwise) | Gate (charter §5.3, §10). |
| **V20a** | Analytic degeneracy | resolved equalised `u` block, taste covariates, and every `g` factor hash-identical across households under `{A,B,P}` | **`1e-9`** | gate |
| **V20b** | Numerical degeneracy | residual `I(Ω^k)` within a declared simulation tolerance derived from the counterfactual ESS, not `1e-9` | **PROPOSED-AT-STAGE-A** (declared simulation tolerance; explicitly **not** `1e-9`) | gate at the declared tolerance |
| **V20c** | Enumeration | every remaining source of cross-household variation enumerated and assigned or escalated | constructive, no computation | **halt to deputy** if `c_ij` heterogeneity is unassigned |
| **V21** | Level-of-aggregation gap | Report `C_A + C_B`, `C_O^(2)`, and their difference. Diagnostic, **not** a gate. | diagnostic (not a gate) | Report; interpret as aggregation level, never as an error. |
| **V22** | Counterfactual ESS for the mirrors | Extend the ratified U12 V6 (threshold 30) to the `{B}`, `{P}`, `{A,B}`, `{A,P}`, `{B,P}`, `{A,B,P}` coalitions: the IS target changes under each while the proposal does not. The Stage-D `V_i^dir` cross-check at the frozen 0.5-nat tolerance (R-71) applies to the flagged subsets **of each coalition**, not only the baseline. | ESS threshold **30**; `V_i^dir` tolerance **0.5 nats** (R-71); **per-coalition materiality/escalation number PROPOSED-AT-STAGE-A** | Apply the frozen escalation rule per coalition; halt if the flagged set widens beyond the Stage-A materiality number. |
| **V23** | Reference-group pre-registration | The `θ̄^pref` group selection and its mirror sensitivity are recorded, with timestamp and hash, **before** any coalition value is computed. | gate | Gate (charter §5.7, §6; §5.3 of this memo). |

**V20 as a whole (R9 §7, verbatim):**

> **V20** | **Degeneracy, split three ways** | **a)** resolved equalised `u` block, taste covariates, and every `g` factor hash-identical across households under `{A,B,P}` (tolerance `1e-9`); **b)** residual `I(Ω^k)` within a declared simulation tolerance derived from the counterfactual ESS, not `1e-9`; **c)** every remaining source of cross-household variation enumerated and assigned or escalated. | a) gate; b) gate at the declared tolerance; c) **halt to deputy** if `c_ij` heterogeneity is unassigned. Supersedes V8's single-tolerance form (item S4).

**Numbers marked PROPOSED-AT-STAGE-A** — i.e. not frozen by R-71/R-72 and to
be fixed at the Stage-A freeze: the **V6** counterfactual-ESS materiality and
escalation number; the **V20b** declared simulation tolerance; the **V22**
per-coalition materiality number.

### 5A.9 R-72 ratifications

#### 5A.9.1 Reference preference block (R9 item S2) — resolved

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

#### 5A.9.2 Index-mean convention (R9 item S1) — ratified

Baseline is the **index-mean**; each has a **single sensitivity**:

| Argument | Baseline (ratified) | Single sensitivity |
|---|---|---|
| experience | `(E[pexp], E[pexp²])` | profile-at-mean-worker `(E[pexp], (E[pexp])²)` |
| education (ability) | dwt **share vector** | share-weighted **probability** |
| age-in-leisure (preference) | `āge` and `āge²` as separate dwt means | *(mirrors the experience sensitivity)* |
| region (access, R-71 R4) | share-weighted **index** | share-weighted **probability** |

Named-level references (including the omitted category `educM`) and
median-region remain **rejected**.

#### 5A.9.3 Opportunity content (R9 item S5) — ratified

Opportunity content is **defined** as `C_A + C_B` from the primary
three-channel game. The two-channel value `C_O^(2)` and the gap are reported
as the **V21** diagnostic. R9 §4.5, verbatim:

> Charter §4.3 makes the headline cut opportunity-vs-preference with access-vs-ability nested inside; charter §7 Stage F instructs evaluating the eight coalitions of the **three-channel** game and reporting "access-only and access-plus-ability shares". Under the three-channel game, `C_A + C_B + C_P = I` exactly, so `C_A + C_B` is a coherent exhaustive definition of opportunity content. But it is **not** equal to the opportunity value of the two-channel game `{opportunity = A∪B, preference}`:
>
> ```
> C_O^(2)  =  ½[ I(∅) − I({A,B}) ] + ½[ I({P}) − I({A,B,P}) ]     ≠     C_A + C_B   in general
> ```
>
> The two differ in how the three-way `A–B–P` interaction is allocated. Proposed disposition (item **S5**): adopt the charter's three-channel game as primary, **define** opportunity content ≡ `C_A + C_B`, and report `C_O^(2)` and the gap `|C_A + C_B − C_O^(2)|` as a pre-registered diagnostic (**V21**), described as a level-of-aggregation gap and not as an error. Pre-registering the definition before results exist is required by charter §5.7.

The gap is reported as a **level of aggregation**, never as an error.

#### 5A.9.4 Expected-positive Tier-2 posture (R9 item S8) — ratified

Boundary-aware / resampling inference is scheduled as the **anticipated path**
for the ability and preference components, not treated as an exception. R9
§5.4, verbatim:

> - The **ability** component loads on `beta_w_pexp2` **by construction** — the flagged coordinate is a coefficient of the ability operator's own reference index.
> - The **preference** component loads on `beta_l0_sm` by construction if the male block is the reference, and through coalition values in any case.
>
> Handoff §2.2 makes boundary-aware or resampling inference mandatory if "any welfare or decomposition functional loads materially on one" of the flagged coordinates. The first-gate material-loading assessment should therefore be **expected to return positive for at least one component**, and Tier-2 should be scheduled as the anticipated path rather than treated as an exception. Materiality remains a numerical question answered at the first gate, not asserted here. `beta_l0_sf` is monitored throughout with no bound asserted absent an accepted record (handoff §2.5). The two W-4 coordinates remain visible in every ability- and preference-component table and caveat block (handoff §2.4).

Materiality remains a **numerical** question answered at the first gate; the
posture does not assert it. A Tier-2 trigger that fires is still a charter §11
halt (§7.1).

#### 5A.9.5 Specification-limits caveat block (R9 item S9, with R-71 R10) — ratified

The three degeneracies are reported together as **one** manuscript
specification-limits block, stated rather than buried:

| Degeneracy | Channel | Consequence for the reported component |
|---|---|---|
| **Hours availability** `g^H` carries no household covariates (U12 §3.4) | access | operator action is the identity; the hours cell contributes exactly zero; the access component is a **lower bound** on offer-side inequality w.r.t. hours-availability heterogeneity |
| **`σ` common across households** (R9 §2.3) | ability | operator action is the identity; the ability component is **location-only**, containing no wage-dispersion content, and is a **lower bound** w.r.t. dispersion heterogeneity |
| **`held` pinned-preference switch** (R9 §3.3) | preference | `theta_l_m` and `beta_ll` are couples-side; the switch is **non-binding in M08** under singles-only scope — recorded for provenance, with a Stage-A verification-and-halt |

### 5A.10 S-10 invariance statement (R9 §5, verbatim)

> The compact statement for the contract: *arguments are scenario-invariant and hash-asserted; equalised values are scenario-dependent by construction and reported.*

**Hash-asserted invariant across all four S-10 scenarios** (R9 §5.1, verbatim):

> `ē`, `p̄ₑₓₚ`, `p̄ₑₓₚ²`, `āge`, `āge²`, `ēduc_leisure`, `n̄kids`; the dwt joint `π_dwt(dgn, educ3)`; the derived occupation objects `p̄(loc4|educ3)`, `p̃(loc4|dgn)`, `p̄̄(loc4)`; the D1 cell routing; the coalition enumeration and Shapley weights; the substitution map of `P`'s step (b) (which coordinates are replaced by which, as a *map*, not as values); `π`; `c_ij`; the alternative support; every measure reference.
>
> All hash-asserted identical across the four scenarios, and recorded before execution.

**Legitimately varying, and not hash-asserted** (R9 §5.2, verbatim):

> `beta_w_pexp2` **is an ability-channel coefficient**. The ability operator's reference index — the equalised Mincer location `μ̄ = b·x̄ + δ_occ[loc4_j]` — is evaluated at the scenario's `θ`, so `μ̄` differs in scenarios 3 and 4. Likewise, if `P`'s reference group block is singles-male, the equalised `θ̄^pref` differs in scenarios 2 and 4 because `beta_l0_sm` is perturbed. Consequently the **equalised values**, every `I(S)`, and every Shapley component vary across scenarios. This is the sensitivity the exercise exists to measure; it must be reported in full, including sub-threshold continuous changes (charter §7 Stage G), and must **not** be suppressed by an invariance assertion.

The access operand additionally satisfies the stronger U12 §8.1 property — it
is **numerically identical** across all four scenarios, because no
access-assigned coefficient is perturbed — asserted by hash of the resolved
operand object in each of the four scenario runs.

### 5A.11 Items this section does NOT close

Two items remain open on the charter reading recorded at **§7.3**, and both are
candidate charter §11 halts. **Execution is blocked until the deputy resolves
them.**

1. **R8 / U12 §8.3 — the `W^3` own-set reference and baseline non-degeneracy.**
   R-71 disposed of R8 as *verify-then-escalate at Stage A*; the verification
   is recorded at §7.3(a) and returns **UNRESOLVED** on charter text.
2. **S6 / R9 §4.4 — the `c_ij` grand-coalition residual.** Recorded at
   §7.3(b) and returns **UNRESOLVED** on charter text. **V20c** is the
   mechanism that surfaces it; its failure action is *halt to deputy*.

Neither is resolved here, and no resolution is designed here.

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

1. `docs/missions/JMP_M08_singles_welfare_execution_contract_v1.md` (this
   file, once frozen)
2. `docs/results/FR_P2a_welfare_integration_validation_v1.md`
3. `docs/results/FR_P2a_welfare_family_results_v1.md`
4. `docs/results/FR_P2a_welfare_decomposition_results_v1.md`
5. `docs/results/FR_P2a_S10_welfare_sensitivity_v1.md`
6. `docs/results/FR_P2a_welfare_reporting_map_v1.csv`
7. `manuscript/sections/FR_P2a_welfare_decomposition_baseline_v1.md`
8. `manuscript/appendices/FR_P2a_welfare_appendix_v1.md`
9. `docs/missions/JMP_M08_independent_economics_review_v1.md`
10. `docs/missions/JMP_M08_goal_manager_acceptance_v1.md`
11. `docs/missions/JMP_M09_LOC4_welfare_robustness_handoff_v1.md`

---

### 6.3 Pre-registered subgroup reporting (U4 deputy ruling, incorporated)

**Governing document, by exact cross-reference:**
`Job_Market_paper docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md`
(sha256 `41061f7ce681f56528cd3576dda707691e3440bac7c35bb6ca4947dde0af9bcb`;
Deputy Programme Director; 2026-08-05; binding amendment to this contract).
**Digest restated under Goal-1 R-70.2** (2026-08-06): the deputy's faithful
byte-copy — which differs from the earlier copy at this path only in two
quotation glyphs (U+201C/U+201D for ASCII `"` at ruling §2) — now occupies this
path, and the `docs/design_notes/` duplicate has been deleted. The pre-fix
digest was `b7c0ac18557c13984b685f32f64355c8708fdfd020c1880ae9efd40edce12181`.
No quoted text in §6.3.1–§6.7 changes as a result.
The ruling governs in full. Its §1 (dimensions), §3 (statistics) and §4
(disclosure) are additionally quoted **verbatim** below, as its §5 permits and
this contract prefers, so that the execution requirements are readable without
leaving this file. Where quotation and source could ever diverge, the ruling
governs.

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

*Recording note for Stage A (not a proposal to deviate).* The pre-existing P2a
singles config `MNL scripts/welfare/configs/welfare_p2a_singles2016.yaml` carries
`measures.active: ["W1", "W3", "W4", "W6"]` and `headline_measures: ["W1", "W4",
"W6"]`. That is the **earlier P3-1 pipeline's** four-measure set, not M08's. M08
executes the charter's six. Any M08 config must set the active set to all six or
declare the divergence to Stage A; it may not inherit the four-measure list
silently.

### 6.5 Resolved sources: `educ3`, region, and the headline weighting convention

The ruling's §5 requires this contract to identify the accepted source for
`educ3` labels, the accepted source for region labels, and the headline weighting
convention. Each is resolved below against a **tracked, committed** artifact,
with the operative text quoted.

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

### 6.6 Implementation path for weighted quantiles and weighted Gini

Implementation is Stage-D work; this section fixes **where it lives** and what
may be reused, so Stage A can freeze the location.

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
| `subgroup_family_by_sex_educ_v1.csv` | `W1`…`W6` × {sex, education}: unweighted count, weighted mean, weighted median, weighted Gini | §3.1 |
| `subgroup_W3_primary_v1.csv` | `W3` × {sex, education, broad region}: unweighted count, weighted mean, weighted median, weighted p10, weighted p90, weighted Gini | §3.2 |
| `subgroup_W3_s10_scenarios_v1.csv` | the §3.2 statistic set for `W3` under each of the four S-10 scenarios (D15), long format with a `scenario` key | §3.3 |
| `subgroup_manifest_v1.json` | attempt id, input digests, `weight_col: "dwt"`, category codings used, per-cell unweighted counts, the full list of cells marked `SUPPRESSED_LT30`, and the Stage-D assertion results of §6.6 | §4 |

Every row of the three CSVs carries its unweighted cell count and a
`disclosure` column valued `OK` or `SUPPRESSED_LT30`. Restricted output retains
suppressed cells **with their values** (ruling §4: *"It remains in restricted
validation output and is marked `SUPPRESSED_LT30`"*).

**Paper-facing (`Job_Market_paper`), aggregate only:** the subgroup tables are
carried inside the already-required §6.2 deliverables — the §3.1 family tables and
the §3.2 `W3` tables in `docs/results/FR_P2a_welfare_family_results_v1.md`
(with the region cut reproduced in
`docs/results/FR_P2a_welfare_decomposition_results_v1.md` where it accompanies the
`W3` decomposition), and the §3.3 scenario tables in
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
supersedes the other. Per §3.2 above, this draft currently fails "use the
exact frozen ESS/redraw/draw-growth thresholds; invent none" for the
draw-growth and direct-vs-IS thresholds specifically (U6/U7) — those
thresholds do not yet exist to be used, which is itself a documented halt
condition ("a required reference set/operator is undefined") until Stage A
resolves them.

### 7.3 Step-0 charter verification of the two decomposition-baseline items (R8/S6)

Performed 2026-08-06 under the R-71 **verify-then-escalate** disposition of R8,
extended to R9 item S6. **Method:** the mission charter
(`JMP_M08_singles_welfare_decomposition_mission_charter_v1.md`) §4.1–4.3, §6
and §7 were read as the *sole* evidence. Design-memo reasoning, scaffold
contract text, and management memos were **not** admitted as evidence for the
classification, and **no resolution is designed here** — this subsection
reports what the charter does and does not settle.

**The charter text bearing on the decomposition's baseline object, verbatim:**

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

> ### 4.3 Decomposition
>
> Exercise B uses Shapley–Shorrocks to allocate inequality in the money-metric welfare vector to:
>
> - **access:** employment/hours availability, regional/urbanisation/GSUR environment, occupation availability, and other accepted non-wage offer terms;
> - **ability:** accepted wage technology and productivity distribution, including education/experience returns and wage dispersion;
> - **preference:** accepted tastes over consumption, leisure, and job packages.
>
> The primary source decomposition is anchored on \(W^3\). \(W^2\) is the pre-registered second check. The \(W^1/W^5\) dual is corroborating interpretation, not a numerical reconciliation identity.

From §6 (Stage-A contract), the charter **delegates** rather than defines:

> - exact definitions of every measure-specific reference:
>   - non-employment option \(o\);
>   - reference set \(\bar A\);
>   - universal job set \(\mathcal J\);
> - exact access, ability, and preference parameter membership;
> - exact equalisation/reference operator for each channel;

> If an exact threshold, reference rule, operator, or required contract is absent or internally inconsistent, halt before execution and return a bounded design conflict. Do not invent it.

From §7 Stage F, the charter requires a **check**, not an assignment:

> 3. verify exhaustiveness to the frozen numerical tolerance;

#### (a) `W^3` own-set degeneracy — **UNRESOLVED**

**Classification: UNRESOLVED.** The charter names `W^3` as "primary
build/validation anchor" (§4.2) and states that "the primary source
decomposition is anchored on \(W^3\)" (§4.3), but **nowhere defines `W^3`'s
reference structure**. It expressly imports the measures "as cited primitives"
(§4.2) and delegates "exact definitions of every measure-specific reference"
to Stage A (§6). There is therefore **no charter text** that defines the
decomposition welfare object as a common-reference money metric, and none that
establishes a non-degenerate baseline \(I(\Omega)\). The own-set `W^3` anchor
consequently **stands** on the charter's own text, and with it the degeneracy
recorded at U12 §8.3 — baseline inequality identically ≈ 0, so that a
decomposition of the baseline vector is not a decomposition of inequality.
The charter's §6 halt clause ("if an exact … reference rule … is absent or
internally inconsistent, halt before execution and return a bounded design
conflict. Do not invent it.") is the governing instruction, and §11's "a
required reference set/operator is undefined" is the matching halt.

#### (b) `c_ij` grand-coalition residual — **UNRESOLVED**

**Classification: UNRESOLVED.** The §4.3 channel definitions are exhaustive of
the *offer side* (access), the *wage technology* (ability), and *tastes*
(preference). **No channel is defined over the budget mapping** — the
household's non-labour income and demographic characteristics that determine
disposable income `c_ij` at each row. The nearest candidate phrase, access's
"other accepted non-wage offer terms", is by its own wording an **offer-side**
term and does not reach the budget side. Nor does the charter define
exhaustiveness in a way that disposes of the residual: §7 Stage F.3 requires
that exhaustiveness be *verified* "to the frozen numerical tolerance", §9.8
makes it an acceptance gate ("W3 Shapley decomposition is exhaustive"), and
§11 makes its failure a halt ("Shapley exhaustiveness fails"). Those are a
test and a halt, **not** an assignment of the residual to a channel. On
charter text alone the grand-coalition residual is therefore unhandled.

#### Consequence for this contract

**Both items are UNRESOLVED. Execution of the decomposition is BLOCKED
pending deputy resolution.** This is recorded as a bounded design conflict, in
the form charter §6 requires; per the same clause and the R-71 verify-then-
escalate posture, **no resolution is invented here**. §5A.11 carries the
cross-reference, and R9 §4.4's endowment/needs fourth-channel proposal is
noted there as an *escalation proposal only* — it is not adopted by this
contract.

---

## 8. Blocking questions for the Goal 1 Manager (post-R-59)

R-59 closed U1, U2, U5, U9, U11, U13, U14. The **U4 deputy ruling** (2026-08-06,
§3.2a(U4), §6.3–§6.7) closes U4. What remains:

### 8.0 Open-items status at this amendment

The amendment instruction anticipated that the remaining open items would be
**exactly U6 and U12**, with U10 mechanical-at-freeze. **That target is not met
by the repository state**, and this contract records the actual position rather
than the anticipated one.

| Item | Anticipated | Actual on disk | Basis |
|---|---|---|---|
| U4 | resolved | **RESOLVED-BY-DEPUTY-RULING** ✓ | ruling placed and incorporated |
| U6 | open | **open (ESCALATED)** ✓ | §8.1 item 2 |
| U12 | open | **CLOSED by R-71** (2026-08-06) | §8.1 item 3; transcribed at §5A |
| **R8** *(new)* | — | **UNRESOLVED on charter text** | §7.3(a) — blocking before Stage F |
| **S6** *(new)* | — | **UNRESOLVED on charter text** | §7.3(b) — blocking before Stage F |
| U10 | mechanical-at-freeze | **mechanical-at-freeze** ✓ | §8.3 item 1 |
| **U3** | *(expected closed)* | **still ESCALATED** ✗ | §8.1 item 1 — no ruling found |
| **U15** | *(expected closed)* | **still ESCALATED** ✗ | §8.1 item 4 — no ruling found |
| **U7** | *(expected closed)* | **still PROPOSED-PENDING-RATIFICATION** ✗ | §8.2 item 1 |
| **U8** | *(expected closed)* | **still PROPOSED-PENDING-RATIFICATION** ✗ | §8.2 item 2 |

Search performed for a closing authority: `R-6[0-9]` and `U3|U7|U8|U15|up1`
across all of `Job_Market_paper docs/`. The only Goal-1 rulings on disk are
**R-60** (Route 6 → Route 1, cited by the MNL parity gate report v2), **R-61**,
**R-63.3**, and **R-67**, none of which addresses U3, U7, U8 or U15. **No R-64
document exists in any repository**; the R-64 carry-forwards are recorded at §2.1
on the strength of the Goal-1 Manager's instruction, and Stage A should expect a
written R-64 to accompany the freeze.

Four items therefore still require a Goal-1 ruling before the freeze can claim
"U6 and U12 only". They are **not** silently closed here: closing U7/U8 requires
ratifying a number, and closing U3/U15 requires information not in the
repositories.

### 8.1 ESCALATED — cannot be resolved from the repositories

1. **U3 — "the up1 manifest note."** Unchanged: no file, commit message, or
   in-document reference matching "up1" exists in any welfare-adjacent
   context across the three repositories. Please supply the exact path or
   confirm it does not exist.
2. **U6 — draw-growth stability (Gate 1(i)).** Unchanged and not a
   documentation gap: the 2×/4× draw-multiplier datasets do not exist on
   disk, so no tolerance can be exercised. Decide: build the datasets, or
   carry Gate 1(i) forward BLOCKED under a pre-registered escalation rule.
3. ~~**U12 — the common reference offer environment** (access-equalisation
   operand). No on-disk candidate; qualitative description only. Nonblocking
   for `W3`, **blocking before Stage F**.~~ **CLOSED 2026-08-06 by Goal-1
   R-71**, which ratifies the U12 design memo (D1–D10, V1–V13) and its R9
   mirror (B1–B6, P1'–P4', C1, V14–V23); R-72 ratifies the remaining
   dispositions. Both are transcribed at **§5A**. **Superseded by two
   different open items** — R8 (`W^3` own-set reference) and S6 (`c_ij`
   grand-coalition residual) — both classified **UNRESOLVED** on charter text
   at **§7.3**, and both blocking before Stage F.
4. **U15 — the two LOC4 rulings.** The R-59(f) byte-identity check **fails**,
   and additionally **neither file is committed** — so "the committed
   `docs/missions/` copy" has no referent, and no file named
   `docs/missions/JMP_LOC4_pathB_ruling_v1.md` exists at all (§3.2a(U15),
   with both digests). Please (a) confirm which document governs and (b)
   direct whether both should be committed, one superseded, or the two
   reconciled, before LOC4/M08R opens.

### 8.2 PROPOSED-PENDING-RATIFICATION — a value is on the table, not frozen

1. **U7 — `V_i^dir` cross-check tolerance.** Proposed `0.5` nats on
   `|V_i^dir − V_i^IS|` (like-for-like common basis, high-ESS households
   only), extracted from the Stage-One code constants quoted in §3.2a(U7).
   Ratify, replace, or scope it differently.
2. **U8 — Shapley-exhaustiveness epsilon.** Proposed
   `|Σ_k φ_k − I(Ω)| ≤ 1e-9 · max(1, |I(Ω)|)`. No constant exists anywhere in
   `scripts/welfare/`; the proposal is reasoned, not sourced (§3.2a(U8)).

### 8.3 Recording notes (no decision required, but Stage A must not trip on them)

1. **U10 — S-10 resolved numeric values: mechanical at freeze.** No decision is
   required. `theta_hat_j`, `se_rob_j`, `lb_j`, `Δ_j`, `θ^sens_j` for
   `beta_l0_sm` and `beta_w_pexp2` are read off the digest-bound accepted source
   `docs/results/FR_P2a_phase5_parameter_reporting_map_v1.csv` (sha256 under
   §3.2a(U1)) and substituted into the D15 formula. Stage A performs the
   substitution at freeze time; it is arithmetic against a verified file, not an
   open question.
2. **Phase-5 has no `complete/` directory.** Its accepted artifacts live under
   `phase5_inference_v1/attempts/…_dryrun_PHASE_5_DRY_RUN_COMPLETE/`. Bind by
   that path (§3.2a(U1)).
3. **`o_nonemployment_key` is the wrong schema shape.** The P2a choice set has
   no alternative keys; `o` is a predicate (`working == 0`, lowest draw index).
   The config field needs replacing, not filling (§3.2a(U2)).
4. ~~**Duplicate U4 ruling copy.** `docs/design_notes/` holds a second copy of the
   deputy ruling differing only in two quotation glyphs (§3.2a(U4)). Direct
   whether it is removed or retained as history.~~ **CLOSED 2026-08-06 by
   Goal-1 R-70.2:** the `docs/design_notes/` copy was the faithful deputy
   byte-copy (sha256 `41061f7c…`, U+201C/U+201D at ruling §2); its bytes now
   occupy `docs/Missions/JMP_M08_U4_subgroup_reporting_ruling_v1.md` and the
   `docs/design_notes/` copy has been **deleted**. One copy remains. Digest
   citations restated in the front matter and at §6.3.
5. **M08 config must not inherit the four-measure P2a list.** See §6.4's
   recording note: `welfare_p2a_singles2016.yaml` carries a four-measure active
   set belonging to the earlier P3-1 pipeline; M08 executes the charter's six.

Until §8.1 is resolved, §8.2 is ratified, and Stage A (independent review)
freezes this contract, **no numerical welfare execution is authorized.**

**Contract status at this amendment (2026-08-06, Stage-A preparation pass under
R-71/R-72):**

`FREEZE-READY-PENDING(deputy-E2; R8/S6; Stage-A-proposed numbers)`

The decomposition axis is now complete on its own terms: **U12 and its R9
mirror are closed by R-71/R-72 and transcribed verbatim at §5A**, and the U4
subgroup-reporting axis is closed and byte-corrected under R-70.2. What the
freeze still waits on:

1. **deputy-E2** — the E2 documentary closure. Parity gate report **v3** and
   its change log exist in MNL (`docs/France_case/P2a/`, both 2026-08-06);
   the one authorized narrow re-verification of the two residual R3 items
   (projected-runtime and three-execution determinism statements) has **no
   verdict recorded on disk**. Per the E2 ruling §1, the Stage-A freeze may
   issue only on an `ACCEPT`. No gate re-run is authorized.
2. **R8 / S6** — the two decomposition-baseline items, classified
   **UNRESOLVED on charter text** at §7.3. Both are charter §11 candidates
   ("a required reference set/operator is undefined"; "Shapley exhaustiveness
   fails"). **Execution of the decomposition is blocked pending deputy
   resolution.**
3. **Stage-A-proposed numbers** — the three tolerances marked
   PROPOSED-AT-STAGE-A at §5A.8 (V6 materiality/escalation, V20b declared
   simulation tolerance, V22 per-coalition materiality), plus the standing
   §8.1/§8.2 items: **U3, U6, U15** (escalated), **U7, U8** (proposed, not
   ratified), and a written **R-64** to stand behind §2.1's carry-forwards.

Also standing: **U8's** proposed `1e-9` exhaustiveness epsilon is now
partially superseded — §5A.8 records `1e-9` as the **V20a analytic** tolerance
only, while V20b's numerical tolerance is expressly **not** `1e-9`. Ratifying
U8 should be done against that split, not against V8's original single-tolerance
form.

The Stage-A freeze record carries the final status.
