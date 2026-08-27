# JMP-M08 — LOC4: PROPOSED MANUSCRIPT CLAIM SET UNDER EACH DISPOSITION (v1)

**STATUS: PROPOSAL. NOTHING MANUSCRIPT-FACING CHANGES NOW.**

This document sets out, for each of the two dispositions the deputy may take,
the claim set that *would* be permitted. It changes no manuscript text, selects
no specification, withdraws no closure, and rebinds nothing. Every claim below
is marked **PROPOSED**.

**Pipeline state, TRANSCRIBED verbatim** from the sealed Stage-2 record
(`…loc4s2b…/loc4_stage2_comparison_v1.json ::
step5_branch_verdict.pipeline_consequence`, sha256
`0bb9558470b03e4f966b4159053168d3a374e9d52d378fbbb52203ccc55be21b`):

> **NOTHING REBINDS PENDING DISPOSITION. The pipeline is HELD, not switched.
> theta-hat_margqh-v2 remains the parameter source of record; the M08 prototype
> closure is NOT withdrawn; the preferred-specification decision is the deputy's
> and the manager selects neither arm on its own authority.**

**Evidence base.** The five MNL-side memos in this packet:
`FR_P2a_m08_loc4_stage1_estimation_memo_v1.md`,
`FR_P2a_m08_loc4_stage2_materiality_report_v1.md`,
`FR_P2a_m08_loc4_s10_battery_report_v1.md`,
`FR_P2a_m08_loc4_model_comparison_v1.md`,
`FR_P2a_m08_loc4_specification_limits_disclosure_v1.md`.
Every numeral quoted here is TRANSCRIBED from a sealed artifact via one of those
memos, or COMPUTED there under a stated formula.

---

## 0. SOURCE STATUS — GAP CLOSED AT DET-AC-2

**v1 as first written recorded two source gaps.** Both are now closed. The
rulings document was extended by GOV-AC-2 and re-hashed for this revision:

| item | v1 status | status now |
|---|---|---|
| the deputy's **interpretation of record** for the LOC4 finding | not on disk; §2.3 carried a marked empty slot | **ON DISK.** QUOTED verbatim at §2.3 from `JMP_M08_goal1_rulings_document_v4.md`, section *"Appended 2026-08-27 — R-141 … R-155"*, **(2) Deputy Interim Ruling — LOC4 Branch B Confirmed** |
| the deputy's **enumerated evidence items 1–16** | not on disk | **ON DISK.** In the same appended section, **(3) Deputy Ruling — Complete LOC4 Preferred-Specification Packet First** (the option-(c) ruling), under `INDEPENDENT REVIEW / Attach or make available:`. Re-keyed in `JMP_M08_LOC4_preferred_spec_packet_index_v1.md` §1 |

**Rulings-document hash, re-verified on disk for this revision:**

| | sha256 | ends at |
|---|---|---|
| at packet v1 | `2510542bb8b67726263f50bd59c830370bb38841f2545236149f1eadf94dbc75` | R-140 |
| **now** | **`8d4edafbe406f0b7e8154e2619b3ce49c1c1e793e7ba161c513f73450f56972d`** | **R-155** |

Nothing was reconstructed, paraphrased or inferred at any point. The §2.3 slot
was left empty in v1 and is now filled from the deputy's own words.

**The independent review has also returned** and is on disk:
`MNL/docs/France_case/P2a/FR_P2a_m08_loc4_preferred_spec_review_v1.md`, sha256
`86d43fe08880a22749440827fb5d985f109f1575c4de65bde2da1ce44239de3c`, 16,237
bytes. Its verdict token is **`LOC4_PREFERRED_PENDING_TIER2_BOUNDARY_ANALYSIS`**
— one of the four the option-(c) ruling permits. That bears directly on which
disposition below is live; see §3.0.

---

## 1. THE CURRENT PERMITTED CLAIM SET (the status quo, for reference)

The M08 prototype closed under `M08_BASELINE_PROTOTYPE_LIMITED_MC_PRECISION`,
which is the §9 fallback branch of the deputy ruling **R-138**
(`JMP_M08_goal1_rulings_document_v4.md`, "U6-CV1 and Limited-Precision
Fallback"). TRANSCRIBED verbatim from §9:

> Permitted quantitative headlines:
>
> - W1 mean with MC band;
> - W1 Gini with MC band;
> - phi_A with MC band;
> - phi_B with MC band.
>
> Permitted qualitative claims:
>
> - stable component signs;
> - stable ordering B > A > P;
> - opportunity-related variation is non-negligible;
> - S-10 does not alter the qualitative conclusion.
>
> Report all other decomposition magnitudes and s_opp as estimate +/- E_T, not
> as exact headline shares.
>
> Do not claim quantitative robustness across W4/W6 if neither passes.
>
> Limited-precision acceptance closes the M08 prototype only. Final quantitative
> magnitudes remain blocked until LOC4 and a final precision decision on the
> preferred specification.

LOC4 has now run. The final precision decision has not been taken. That last
paragraph is the hinge on which both dispositions below turn.

For reference, the four permitted headlines at their baseline T16 values, with
the closure record's own `E_T` (TRANSCRIBED via the Stage-2 memo's
`baseline_level_gate_of_record` rows and the u6ffn16 record, sha256
`1a6f586605e05da6b2057a85af7116ffb6b6fd536992ae60be2c4514b96c3a9d`):

| headline | T16 | `E_T` | level gate |
|---|---|---|---|
| `W1_mean` | `1396.133144516662` | `3.02142` | pass (ratio `0.866`) |
| `W1_gini` | `0.17395548089149374` | `0.000869933` | pass (ratio `0.696`) |
| `φ_A` | `0.006175877698704207` | — | — |
| `φ_B` | `0.011434648541721012` | — | — |

*(`W1_median` T16 `1340.43`, `E_T = 11.5733`, ratio `3.316` — **FAIL**, already
removed from the promotion gate by R-138 §2. `W1_s_opp` T16 `0.101236`,
`E_T = 0.0094323`, ratio `1.886` — **FAIL** on the level gate.)*

---

## 2. DISPOSITION A — BASELINE PREFERRED, LOC4 REPORTED AS MATERIAL ROBUSTNESS

*"The corrected baseline `θ-v2` remains the specification of record; the LOC4
result is reported as a material robustness finding."*

### 2.1 PROPOSED: the permitted headline set is UNCHANGED

The four R-138 §9 quantitative headlines stand exactly as they are — same
values, same MC bands, same measure roles (primary W1; secondary W4/W6;
validation-only W3; signed-diagnostic-only W5; W2 excluded from paper-facing).
**PROPOSED: no numeral in the headline set changes under Disposition A.**

The reason is structural rather than merely conservative. **S2** verified that
the baseline arm, re-run through the *installed LOC4 code path*, reproduces the
sealed `u6ffn16` record **bitwise**: 66 functionals, 11 sub-bases, **726 / 726
values bitwise equal**, `max_abs_deviation_over_every_value = 0.0`. Nothing
about the baseline arm's numbers is disturbed by the existence of the LOC4 arm.

### 2.2 PROPOSED: Q-2 is RE-SCOPED, not withdrawn

The pre-registered qualitative claim `Q-2` is *"stable ordering B > A > P"*.
**S2** records its verdict as **`CHANGED`**: the ordering holds on the baseline
arm on T16 and all four T12_-b, and fails on the LOC4 arm on all five.

**PROPOSED wording change — the minimum that makes the claim true:**

> ~~stable ordering B > A > P~~
> **stable ordering B > A > P *on the baseline specification***

**PROPOSED accompanying sentence**, to be placed wherever the ordering is used:

> The ordering is stable across the Monte-Carlo replicate family on the baseline
> specification, and it does not survive the LOC4 occupation-wage-location
> extension, where the ordering is A > B > P on T16 and on every leave-one-
> superblock-out replicate.

**PROPOSED: `Q-1` and `Q-3` are NOT re-scoped.** Both are recorded `UNCHANGED`
in **S2** — component signs (`sgn φ_A = +1`, `sgn φ_B = +1`, `sgn φ_P = −1`) and
non-negligible opportunity variation (`φ_A + φ_B > 0`, `s_opp > 0`) hold on
*both* arms on T16 and every T12_-b. These two claims are strengthened, not
weakened, by the robustness exercise, and **PROPOSED** that the manuscript may
say so.

**PROPOSED: `Q-4` remains open.** *"S-10 does not alter the qualitative
conclusion"* is recorded in **S2** as `NOT_EVALUABLE_SEVERED`, TRANSCRIBED:
*"design v4 §2.4 forbids an autonomous S-10 re-derivation and Stage 1 returned a
CHANGED W-4 flagged membership. The claim is severable and is carried to the
deputy UNCHANGED; it is not asserted, not refuted, and not used in the M-6
verdict."* The subsequently authorised S-10 battery bears on it — family (ii) is
stable across all six scenarios — but that battery returned `S10_TIER2_TRIGGER`
and took no autonomous action. **PROPOSED: `Q-4` is neither asserted nor
withdrawn pending the deputy's disposition.**

### 2.3 PROPOSED: the LOC4 finding is reported with the deputy's interpretation of record

The LOC4 finding, as it would be reported:

| object | baseline T16 | LOC4 T16 | Δ | E_Δ | m | classification |
|---|---|---|---|---|---|---|
| `W1_mean` | `1396.133144516662` | `1342.1310202506527` | `-54.00212426600933` | `1.3897660684459012` | `0.01` rel. | `LOC4_MATERIAL` |
| `W1_gini` | `0.17395548089149374` | `0.1503603209922411` | `-0.02359515989925265` | `0.0007246778049694155` | `0.005` abs. | `LOC4_MATERIAL` |
| `W1_s_opp` | `0.10123582281037721` | `0.023836960352717894` | `-0.07739886245765931` | `0.004166009264228679` | `0.02` abs. | `LOC4_MATERIAL` |
| `W1_median` | `1340.4310587595537` | `1246.8241821981856` | `-93.60687656136815` | `19.141281905819792` | `0.01` rel. | **`UNCERTIFIED_NO_VERDICT`** |

plus M-5 aggregate `MATERIAL` (the `O_AB` ordering indicator, unanimous across
T16 and all four T12_-b) and M-6 `CHANGED` (Q-2). Overall: **LOC4 MATERIAL
overall**, Branch B.

**THE DEPUTY'S INTERPRETATION OF RECORD.** QUOTED verbatim from
`::JMP::docs/Missions/JMP_M08_goal1_rulings_document_v4.md` (sha256
`8d4edafbe406f0b7e8154e2619b3ce49c1c1e793e7ba161c513f73450f56972d`), section
*"Appended 2026-08-27 — R-141 … R-155"*, **(2) Deputy Interim Ruling — LOC4
Branch B Confirmed**, under the instruction *"Interpret this narrowly:"* —

> "Allowing occupation-specific wage-location shifts materially changes the
> structural attribution of welfare inequality. The estimated ability
> contribution falls much more sharply than the access contribution, reversing
> their ordering and substantially reducing the overall normalized opportunity
> contribution."

**PROPOSED: this paragraph is reported verbatim wherever the LOC4 finding is
reported, and is not paraphrased.**

The same ruling attaches an explicit prohibition to it, QUOTED verbatim:

> Do not say that LOC4 causally transfers or absorbs a fixed quantity of
> opportunity content. Both phi_A and phi_B fall; this is a model-conditional
> reallocation and welfare-distribution change.

That both components fall is confirmed by the sealed record (TRANSCRIBED,
**S2**, T16): `φ_A` `0.006175877698704207` → `0.0029168164479072647`;
`φ_B` `0.011434648541721012` → `0.0006673165622067221`. The ordering reverses
because `φ_B` falls further, not because content moves from one to the other.

The ruling's own provisional-evidence list, QUOTED verbatim, is the numeric
frame the interpretation sits on:

> The Stage-2 LOC4 materiality findings are accepted as provisional decision
> evidence because their direct CRN difference-precision gates pass:
>
> - W1 mean: -54.00 EUR, -3.87%;
> - W1 Gini: -0.0236;
> - normalized opportunity contribution:
>   0.1012 -> 0.0238, Delta = -0.0774;
> - stable ordering reversal:
>   baseline B > A > P;
>   LOC4 A > B > P.

Each figure reconciles with the sealed record at full precision (TRANSCRIBED,
**S2**): `-54.00212426600933` EUR; `-0.02359515989925265`;
`0.10123582281037721` → `0.023836960352717894`, Δ `-0.07739886245765931`.
The `-3.87%` is the M-1 tested ratio `-0.03867978099230983`.

Two further status labels are fixed by the ruling and QUOTED here because they
constrain every sentence in this document:

> Corrected baseline:
> ACCEPTED_REFERENCE_BASELINE_NOT_FINAL_PREFERRED
>
> LOC4:
> LOC4_MATERIAL_TIER2_TRIGGER_PREFERRED_SPEC_PENDING

and the notebook/label instruction, QUOTED verbatim:

> Do not label LOC4 preferred or restore the baseline ordering as robust.

**PROPOSED framing constraint, independent of that text.** Whatever the
interpretation of record says, the report of the LOC4 finding must observe
Disclosure 7: `δ_occ` is not a causal occupational wage premium, and no
baseline-versus-LOC4 coefficient change is a statistically significant
difference. And it must observe coherence finding **C-7**, TRANSCRIBED:
*"Delta is the effect of the SPECIFICATION CHANGE AS A WHOLE, not the partial
effect of the delta_occ term: both arms are evaluated at their own full
re-estimated vectors. CRN pairs the RANDOMNESS, not the PARAMETERS."*

### 2.4 PROPOSED: the specification-limits disclosure ships with the paper

`FR_P2a_m08_loc4_specification_limits_disclosure_v1.md` is **PROPOSED** as a
standing disclosure under Disposition A, in whatever venue the manuscript uses
for methodological limits. Its ten-point list at §10 is the operative content.
The four points that bind hardest under Disposition A:

1. the ordering and the `s_opp` magnitude are **specification-sensitive**;
2. the median is **uncertified in both arms**;
3. the 22 uncertified differences carry **no interpretation**;
4. **W4/W6 quantitative robustness is claimable by neither arm** — the
   comparator triggers on a different scenario set and, at `s6`, with the
   opposite sign on the mean.

### 2.5 PROPOSED: what may NOT be said under Disposition A

* Not: "the decomposition ordering is a property of the data." **PROPOSED**
  instead: "of the baseline specification."
* Not: "`s_opp ≈ 0.10`" as a specification-free magnitude. The LOC4 value is
  `0.023836960352717894`.
* Not: "the results are robust to allowing occupation-specific wage location."
  They are **not** — that is the whole finding.
* Not: any claim that the LOC4 arm is *wrong*. It is a single-optimum fit with
  clean curvature that nests the baseline bitwise; its objective is better by
  `46.43478353291721` in negLL. It is a live alternative, not a diagnostic
  failure.

---

## 3. DISPOSITION B — LOC4 PREFERRED, PENDING A TIER-2 / FINAL-PRECISION RULING

*"The LOC4 specification becomes the specification of record."*

### 3.0 The independent review returned in this direction — but the deputy has not ruled

The option-(c) ruling required the reviewer to *"return exactly one"* of four
tokens. The review on disk
(`MNL/docs/France_case/P2a/FR_P2a_m08_loc4_preferred_spec_review_v1.md`, sha256
`86d43fe08880a22749440827fb5d985f109f1575c4de65bde2da1ce44239de3c`) returned
**`LOC4_PREFERRED_PENDING_TIER2_BOUNDARY_ANALYSIS`**, and states, QUOTED:

> The clean distinction is: **specification preference can be LOC4 now; final
> level magnitudes remain conditional.**

**This does not by itself make Disposition B operative.** The same ruling fixes
the standing status as `LOC4_MATERIAL_TIER2_TRIGGER_PREFERRED_SPEC_PENDING` and
states, QUOTED: *"Until that packet is accepted: baseline remains the reference
benchmark; LOC4 remains a material candidate; neither is final preferred; no
preferred quantitative magnitude is frozen."* The reviewer's token is one of the
sixteen evidence inputs to the deputy's decision, not the decision. Disposition
B remains **PROPOSED**, exactly as Disposition A does.

Note also that the review's token is *conditional in the same place* §3.1
identifies: on the Tier-2 boundary analysis. The two are consistent.

### 3.1 The gating fact: nothing can be claimed until Tier-2 is disposed of

The S-10 battery returned **`S10_TIER2_TRIGGER`**, on
`scenarios_with_a_trigger = ["s5_beta_w_pexp2_alone", "s6_all_four_jointly"]`,
with `scenarios_indeterminate_mc = []`. Consequence of record, TRANSCRIBED
verbatim:

> ruling §8: a LOC4 Tier-2 trigger BLOCKS the preferred-arm quantitative freeze
> but does NOT automatically require whole-model re-estimation. Ruling §8 also
> directs a RETURN on an INDETERMINATE_MC classification. Either way this battery
> takes no autonomous action: nothing rebinds, nothing is re-run to break a tie,
> and the disposition is the deputy's.

**PROPOSED: under Disposition B, *no* LOC4 quantitative magnitude is
manuscript-facing until a final-precision ruling disposes of the Tier-2
trigger.** That is not a drafting preference; it is what "blocks the
preferred-arm quantitative freeze" means.

### 3.2 PROPOSED: what could be claimed ONLY AFTER a final-precision ruling

Conditional on such a ruling, and only then:

| PROPOSED claim | supporting numeral | condition |
|---|---|---|
| LOC4 `W1_mean` with MC band | `1342.1310202506527` | Tier-2 disposed; the level's own `E_T` established on the LOC4 arm (**not currently on disk** — the closure record's `E_T` values are the *baseline* arm's) |
| LOC4 `W1_gini` with MC band | `0.1503603209922411` | idem |
| LOC4 `φ_A`, `φ_B` with MC bands | `0.0029168164479072647`, `0.0006673165622067221` | idem |
| stable component signs | `Q-1` = `UNCHANGED` on both arms | available now |
| opportunity-related variation is non-negligible | `Q-3` = `UNCHANGED`; `φ_A + φ_B = 0.0035841330101139867`, `s_opp = 0.023836960352717894` at T16, both > 0 on every replicate | available now |
| ordering **A > B > P** on the LOC4 specification | `φ_A − φ_B` = `0.0022494998857005427` at T16, positive on all five replicates and on all six S-10 scenarios | available now, **if** stated as a property of the LOC4 specification |

**PROPOSED: `Q-2` cannot simply be re-pointed at the LOC4 arm.** The
pre-registered claim is the specific ordering `B > A > P`. Under Disposition B
that claim is **false**, and the honest move is to record it as a
specification-driven reversal, not to substitute `A > B > P` into the same
sentence and carry the "stable ordering" wording across.

**PROPOSED: an MC-precision battery on the LOC4 arm is a prerequisite.** The
`E_T` figures in the closure record are the baseline arm's. Every `E_Δ` in this
packet is a *difference* band, not an arm's own band — the estimator's own
prohibition, TRANSCRIBED: *"E_Delta is NEVER formed from the arms' own bands."*
So no LOC4 level currently has a certified MC band on disk.

### 3.3 PROPOSED: `beta_w_pexp2` sensitivity as a STANDING disclosure

Under Disposition B this stops being a return trigger and becomes a permanent
qualification on the preferred arm. **PROPOSED** disclosure text, all numerals
TRANSCRIBED:

> The preferred specification's welfare level is sensitive to a single
> near-boundary wage coordinate. `beta_w_pexp2` is W-4-flagged on the LOC4 arm
> (interval `[-0.10013548464127309, 0.06075817812945216]` against bounds
> `[-0.1, 0.1]`); it was **not** flagged on the corrected baseline and **was**
> flagged in the certified Phase-5 record. Displacing it by half its robust
> standard error, holding everything else at the estimate, moves the W1 mean by
> `-0.02040522831486493` in relative terms — more than twice the `0.01` Tier-2
> materiality threshold — while the same displacement applied to each of the
> three flagged leisure coordinates moves it by at most `0.007088706132609513`.
> Of thirteen normalisation limbs, the three leisure scenarios move none; the two
> scenarios containing `beta_w_pexp2` move exactly one, the wage location `μ`.

**PROPOSED: this disclosure travels with every LOC4 magnitude, not once in an
appendix.**

### 3.4 PROPOSED: what may NOT be said under Disposition B

* Not: any LOC4 quantitative magnitude, before the Tier-2 disposition.
* Not: "stable ordering B > A > P" — under Disposition B this is false.
* Not: "S-10 does not alter the qualitative conclusion" (`Q-4`): the S-10
  battery **triggered Tier-2** on the LOC4 arm. Family (ii) is stable, which
  bears on the *comparison*; the *level* is what triggered.
* Not: W4/W6 quantitative robustness — the same §5 disclosure binds under B as
  under A.
* Not: the median, in any form.
* Not: that the baseline is withdrawn. **S2**: *"the M08 prototype closure is NOT
  withdrawn."*

---

## 4. WHAT IS COMMON TO BOTH DISPOSITIONS

Regardless of which way the deputy rules, **PROPOSED** as binding on the
manuscript:

1. **Disclosure 7 and the prohibited-claims list**, unchanged: `δ_occ` is not a
   causal occupational wage premium; no baseline-versus-LOC4 coefficient change
   is a statistically significant difference.
2. **The median is uncertified in both arms**, level and difference, W1 and W4
   and W6.
3. **The 22 uncertified differences carry no interpretation.**
4. **W4/W6 quantitative robustness is claimable by neither arm.**
5. **No subgroup welfare quantity** may be reported on either arm.
6. **LR / AIC / BIC are conventional references at a boundary-adjacent optimum
   in both arms** (`beta_l_age2_sm` and `beta_l_age2_sf` upper-bound-active on
   both sides), not a specification decision. The figures, for the record:
   `LR = 92.86956706583442` on `df = 3`, `p` (χ²₃) `= 5.297971492402584e-20`;
   ΔAIC `-86.86956706583442`; ΔBIC `-70.82187459199486` under `N = 1,555`
   clusters or `-56.976513041467115` under `N = 157,055` rows.
7. **C-16** stands as a named, uncorrected defect of the precision machinery in
   both arms.
8. **The exact nesting fact may be stated in either disposition**, because it is
   algebraic rather than asymptotic: the LOC4 likelihood restricted to `δ = 0`
   reproduces the certified objective `18499.489277699933` **bitwise**, and the
   δ-gradient there is `(129.31441848714294, 51.479426015565224,
   -278.8939056307008)` — non-zero, so the baseline is not a stationary point of
   the extension.

---

## 5. WHAT THIS DOCUMENT DOES NOT DO

No manuscript text is edited. No specification is selected. No claim is added,
removed or re-worded anywhere outside this file. No closure is withdrawn. No
estimation, pricing, EUROMOD run or commit was performed in producing it. The
deputy's interpretation-of-record slot at §2.3 is **empty and marked**, because
its source is not on disk.

---

*PROPOSED throughout. Uncommitted.*
