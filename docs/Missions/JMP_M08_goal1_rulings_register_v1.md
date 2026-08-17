# JMP Goal-1 Rulings Register — R-59 … R-72

**Programme:** Goal 1 — Empirical JMP
**Document class:** **Manager governance record. NOT deputy text.** Nothing in
this file rules on anything; it records rulings issued elsewhere and states
where each one's text can be found. It creates no authority and amends no
contract.
**Created:** 2026-08-06, during the JMP-M08 Stage-A preparation pass
(documentation-only: no computation, no welfare number, no MNL write, no commit).
**Purpose:** so that **every ruling citation in
`JMP_M08_singles_welfare_execution_contract_v1.md` resolves on disk** — or is
recorded, explicitly, as not resolving.

---

## 0. How to read the "Primary text" column — and the headline finding

**Headline finding: of the fourteen rulings R-59 … R-72, none exists as a
standalone document in any repository.** Every one is known only through
citation or recital in a document it authorised. Four (R-62, R-65, R-66, R-68,
R-69 — five) are not cited anywhere at all.

| Value | Meaning |
|---|---|
| **RECITED** | No ruling document exists; the substance is recorded in a document the ruling authorised, in enough detail to act on. Cite the reciting document, not the ruling. |
| **CITED-ONLY** | The ruling id appears on disk, but no text records what it decided beyond the citing sentence. |
| **NOT-ON-DISK** | The ruling id appears nowhere in `Job_Market_paper`, `MNL`, or `dclaborsupply-monorepo`; it is known only from the live Goal-1 Manager instruction. |
| **NO-TRACE** | The id appears nowhere at all, in any form. Existence not established. |

**Search performed (2026-08-06):** regex `R-(5[5-9]|6[0-9]|7[0-2])(\.[0-9])?`
over all `*.md` in `Job_Market_paper` (repo-wide) and over `MNL/docs`;
directory listings of `docs/Missions/`, `docs/design_notes/`, `docs/prompts/`,
`docs/governance/`. `docs/governance/JMP_decision_log_v1.md` uses a **different
numbering series** (`R-001…R-006`, `X-001…X-006`) and is **not** the source of
the `R-59…R-72` series.

---

## 1. Register

### R-59

- **Date:** not stated on disk. Bounded **≤ 2026-08-05** (cited by
  `MNL docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v1.md`, 2026-08-05).
- **Substance:** Documentation-only pass over the M08 execution contract — no
  code change, no data change, no welfare computation. Supplied four full
  digests and directed on-disk resolution of the remaining §3.2 register, each
  item to carry an explicit status (RESOLVED / PROPOSED-PENDING-RATIFICATION /
  ESCALATED). Sub-items are lettered (a)–(g) in the contract.
- **Resolved / frozen:** closed register items **U1, U2, U5, U9, U11, U13,
  U14**. U11 → `type_conditional_median_opportunity`; U13 → `R_h`; U14 →
  `held`. Gave **no** direction on U3, U6, U12, U15. (f)'s byte-identity check
  on the two LOC4 rulings **failed**.
- **Primary text:** **RECITED** — contract front matter and §3.2 / §3.2a.
- **Transcribed at:** contract front matter; §3.2 (status column); §3.2a
  (values, sources, exact status); §8.0.

### R-60

- **Date:** not stated on disk. Bounded **≤ 2026-08-05**.
- **Substance:** Route 6 → Route 1 (parity production-path routing decision).
- **Resolved / frozen:** the parity gate's execution route. No M08 register
  item.
- **Primary text:** **CITED-ONLY** — no text records the ruling's reasoning or
  scope.
- **Transcribed at:** `MNL docs/France_case/P2a/FR_P2a_m08_parity_gate_report_v1.md`
  (lines 4, 46, 347), `…_v2.md` (line 4), `…_v3.md` (line 4); contract §8.0.

### R-61

- **Date:** not stated on disk. Bounded **≤ 2026-08-05** (mtime of the reciting
  acceptance memo).
- **Substance:** Verification-reference reclassification. A byte-match failure
  against an ASCII-hyphen reference string supplied inline in a checkpoint
  prompt was reclassified as a **verification-reference defect, not a document
  defect** — the binding source renders the sentence with U+2013 EN DASH, so
  the ASCII reference string was void.
- **Resolved / frozen:** the M07I Step-0 en-dash flag. No file was edited; the
  M07I correction cycle remained unspent.
- **Primary text:** **RECITED** — `JMP_M07I_identity_alignment_acceptance_v1.md`
  §7 records the substance in full.
- **Transcribed at:** `JMP_M07I_identity_alignment_acceptance_v1.md` §7 (and
  its input list, line 17); contract §8.0 (as one of the four rulings found on
  disk).

### R-62

- **Date:** —
- **Substance:** **No trace.**
- **Resolved / frozen:** —
- **Primary text:** **NO-TRACE** — the id appears in no document in any
  repository.
- **Transcribed at:** nowhere. *If R-62 exists, the Goal 1 Manager must supply
  it; nothing in the contract depends on it.*

### R-63.3

- **Date:** not stated on disk. Bounded **≤ 2026-08-06**.
- **Substance:** Carries the **deferred project-state placement** — the v3
  positioning memo and its acceptance ride the next documentation checkpoint
  together rather than being placed immediately.
- **Resolved / frozen:** placement/sequencing of the M07I positioning-memo
  documents. No M08 register item.
- **Primary text:** **CITED-ONLY.** Note that the parent **R-63** is itself
  never cited — only the `.3` sub-item is.
- **Transcribed at:** `JMP_M07I_positioning_memo_rider_acceptance_v1.md`
  (closing paragraph); contract §8.0.

### R-64

- **Date:** **2026-08-06** (the contract records the carry-forwards as
  "Incorporated 2026-08-06 under the Goal-1 R-64 carry-forwards").
- **Substance:** Certified Stage-B parity status carry-forwards, incorporated
  as contract §2.1.
- **Resolved / frozen:** the §2.1 certified-parity carry-forwards, including
  the target-only D-BEN Option B geometry and the non-licensing of joint
  batching (§2.1(iv)).
- **Primary text:** **NOT-ON-DISK.** The contract states plainly: *"**No R-64
  document exists in any repository**; the R-64 carry-forwards are recorded at
  §2.1 on the strength of the Goal-1 Manager's instruction, and Stage A should
  expect a written R-64 to accompany the freeze."* **Still outstanding.**
- **Transcribed at:** contract §2.1 (six citations); §8.0; §8.3 / closing
  status (as a freeze precondition).

### R-65

- **Date:** — **Substance:** **No trace.** **Primary text:** **NO-TRACE.**
  **Transcribed at:** nowhere.

### R-66

- **Date:** — **Substance:** **No trace.** **Primary text:** **NO-TRACE.**
  **Transcribed at:** nowhere.

### R-67

- **Date:** **2026-08-06** (reciting memo's stated date).
- **Substance:** Disclosed execution route. Authorised the Goal 1 Manager to
  apply an independent reviewer's **verbatim** clause substitution as a
  manager-verified file edit, the manager's role limited to verifying the
  clause occurred exactly once and applying the given text — **no drafting
  judgement**.
- **Resolved / frozen:** the execution route for the M07I positioning-memo
  correction. No M08 register item.
- **Primary text:** **RECITED** — `JMP_M07I_positioning_memo_rider_acceptance_v1.md`
  §(correction) states the route and its limits.
- **Transcribed at:** `JMP_M07I_positioning_memo_rider_acceptance_v1.md`;
  contract §8.0.

### R-68

- **Date:** — **Substance:** **No trace.** **Primary text:** **NO-TRACE.**
  **Transcribed at:** nowhere.

### R-69

- **Date:** — **Substance:** **No trace.** **Primary text:** **NO-TRACE.**
  **Transcribed at:** nowhere.

### R-70 (and sub-item R-70.2)

- **Date:** **2026-08-06.**
- **Substance (R-70.2 only):** U4 byte-fix. The `docs/design_notes/` copy of
  the deputy's U4 subgroup-reporting ruling is the **faithful deputy byte-copy**
  (sha256 `41061f7c…`, U+201C/U+201D at ruling §2); its bytes must replace the
  content of the `docs/Missions/` copy, and the `docs/design_notes/` copy must
  then be deleted.
- **Resolved / frozen:** the duplicate-U4-copy question left open at contract
  §8.3 item 4. **Executed 2026-08-06:** Missions copy now
  `41061f7ce681f56528cd3576dda707691e3440bac7c35bb6ca4947dde0af9bcb`
  (was `b7c0ac18…`); design_notes copy deleted; both contract digest citations
  restated.
- **Primary text:** **NOT-ON-DISK.** Known only from the Goal-1 Manager's
  Stage-A preparation instruction of 2026-08-06. **R-70's other sub-items
  (R-70.1, R-70.3+) are unknown** — only `.2` was communicated.
- **Transcribed at:** contract front matter (digest restatement); §6.3
  (digest restatement + byte-fix note); §8.3 item 4 (closed).

### R-71

- **Date:** **2026-08-06** (bounded by the reciting memo, which is dated by
  mtime 2026-08-06).
- **Substance:** Ratifies the U12 access-equalisation operand design memo in
  full and commissions its R9 mirror. This is the ruling that converts the
  decomposition operators from proposals into contract text.
- **Resolved / frozen:** **D1–D10 ratified**, with D1 adopted as an amendment
  to `RURO_welfare_scaffold_design_contract_v2.md` §7 (name-list → cell
  routing) and the cell table transcribed verbatim; **R2** (sex-pooling) and
  **R3** (education routing) ratified; **R4** = share-weighted **index**
  baseline, share-weighted probability the single sensitivity, median-region
  **rejected**; **R5** = `ω_s` are within-`educ3` `dwt` population sex shares;
  **R6** = **all** operand population references `dwt`-weighted (`dwt = db090`),
  unweighted variant **not run in M08**; **R7** = V1–V13 ratified with the
  stated tolerances, `V_i^dir` **unblocked** and mandatory at Stage D on
  flagged subsets under the frozen **0.5-nat** tolerance; **R8** =
  **verify-then-escalate at Stage A** (not resolved — see §7.3(a) of the
  contract); **R10/R11** as proposed.
- **Primary text:** **RECITED** — the only record is the "Authoritative inputs"
  recital at `JMP_M08_ability_preference_operators_design_v1.md` item 1, which
  states the dispositions in the detail summarised above. **No ruling document
  exists.**
- **Transcribed at:** contract **§5A** (whole section); §3.2 (U12 row, now
  RESOLVED-BY-RULING); §8.0; §8.1 item 3.

### R-72

- **Date:** **2026-08-06.**
- **Substance:** Ratifies the R9 ability/preference operators memo's open
  items, closing the decomposition-operator design.
- **Resolved / frozen:** (i) **θ̄^pref = singles-female block**, with the
  **singles-male block as the single pre-registered mirror sensitivity**, both
  recorded under **V23** before any coalition value is computed (R9 item S2);
  (ii) **index-mean baseline + single sensitivity** for squared and dummy
  arguments (R9 item S1); (iii) **opportunity content ≡ `C_A + C_B`** from the
  three-channel game, with `C_O^(2)` and the gap reported as the **V21**
  diagnostic (R9 item S5); (iv) **expected-positive Tier-2 posture** —
  boundary-aware/resampling inference scheduled as the anticipated path, not an
  exception (R9 item S8); (v) the **specification-limits caveat block** —
  hours-access degeneracy, `σ` ability degeneracy, `held` preference
  degeneracy, reported together (R9 item S9 with R-71's R10). The **V8 →
  V20a/b/c split** (R9 item S4) is adopted with V20a at `1e-9` and V20b at a
  declared simulation tolerance. **S6 is NOT resolved** — see §7.3(b).
- **Primary text:** **NOT-ON-DISK.** Known only from the Goal-1 Manager's
  Stage-A preparation instruction of 2026-08-06.
- **Transcribed at:** contract **§5A.8** (tolerances), **§5A.9.1–§5A.9.5**
  (the five ratifications), §5A.10 (S-10 invariance statement).

---

## 2. What this register shows the Goal 1 Manager

1. **Nine of fourteen ids have no substantive text anywhere** — five NO-TRACE
   (R-62, R-65, R-66, R-68, R-69), two CITED-ONLY (R-60, R-63.3), two
   NOT-ON-DISK but acted upon (R-70.2, R-72). A tenth, **R-64**, is
   NOT-ON-DISK and is already a named freeze precondition.
2. **The three rulings the M08 decomposition rests on — R-71, R-72, and
   R-70.2 — have no primary text.** R-71 survives only as a recital inside the
   memo it ratified; R-72 and R-70.2 survive only in this pass's instruction
   and in the contract text they produced. If the Stage-A freeze is to be
   auditable, these three should be issued as documents.
3. **Numbering gaps are unexplained.** R-62, R-65, R-66, R-68 and R-69 may
   never have existed, may be non-Goal-1, or may be missing. This register
   does not guess.
4. Nothing here is a deputy instrument, and nothing here changes a contract.

---

**Statement:** no welfare number, no decomposition number, no parameter value,
and no re-estimation is produced or implied by this register. No computation was
performed to produce it. No commit has been made.
