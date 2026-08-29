# JMP-M08 — LOC4: THE MANUSCRIPT CLAIM SET (v2)

**STATUS: OPERATIVE.** This is the charter's permanent output 6
(`JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` §8), written at
Goal-1 **R-175** on the verdict `LOC4_PREFERRED_MC_BANDED_LEVELS`.

v2 is v1 (`JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md`, sha256
`c9051c9df6ff3a0f901aaaeec44de76f93effddd3e68a9c7eecb31d132aea5e4`) revised
per the eleven strikes and additions required by the independent Tier-2 review's
H10 (`MNL/docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md`,
sha256 `06d2c0fc9cfd62ff1eb220e62cc34f660a739e0d594f079e47ed7307bab4b396`).
**v1 is superseded for manuscript purposes** and survives only as immutable
history of the moment it recorded. Where v1 and v2 differ, v2 governs.

The governing acceptance is
`JMP_M08_LOC4_preferred_spec_acceptance_v1.md`. Section numbers below carry the
H10 item they discharge.

---

## 0. What v2 changes, item by item

| H10 item | Change | §here |
|---|---|---|
| 1 | Strike the Disposition-B pending logic | §1 |
| 2 | Replace the old T16 values with the RQMC record | §2 |
| 3 | Strike "stable component signs" and every collective-sign formulation | §3 |
| 4 | Add the deputy's exact `phi_B` sentence | §3.2 |
| 5 | Label `r_phi_P` and `r_R_bg` `MC_BANDED_NORMALIZED_DIAGNOSTIC` | §4 |
| 6 | Retain `A > B > P` as the LOC4/profile/RQMC ordering only | §5 |
| 7 | Retain the W4/W6 prohibition; median stays `MC_BAND_ONLY_NONSMOOTH` | §6 |
| 8 | Never combine the RQMC band with the profile envelope | §7 |
| 9 | Demote the one-coordinate S-10 sensitivity to a diagnostic | §8 |
| 10 | No broad `Q-4` or collective robustness restoration | §9 |
| 11 | Preserve the benchmark-versus-final-JMP-specification distinction | §10 |

---

## 1. The pending-status logic is STRUCK (H10 item 1)

v1 §3.0–§3.1 stated that the deputy had not yet ruled, that LOC4 remained merely
`LOC4_MATERIAL_TIER2_TRIGGER_PREFERRED_SPEC_PENDING`, and that **no** LOC4
quantitative magnitude could be manuscript-facing until a final-precision ruling
disposed of the Tier-2 trigger. All of that is **superseded**. It is struck, not
merely re-worded.

The deputy has disposed of T2-B and accepted LOC4 as the current benchmark at
**`MC_BANDED_LEVELS`**. The two operative status labels are:

* **`LOC4_PREFERRED_STRUCTURAL_SPECIFICATION`** — the specification;
* **`MC_BANDED_LEVELS`** — its magnitudes.

**This does not imply `FULL_NUMERICAL_FREEZE`**, which the review expressly
declined to find. Magnitudes are manuscript-facing **banded**, and only banded.

Two consequences follow for v1's text. v1 §3.2's condition column ("Tier-2
disposed; the level's own `E_T` established on the LOC4 arm — *not currently on
disk*") is discharged: the LOC4 arm's own bands are now on disk, in the RQMC
record of §2. v1 §3.2's prerequisite ("an MC-precision battery on the LOC4 arm
is a prerequisite") is satisfied by the eight-scramble RQMC pass.

---

## 2. The final quantitative record (H10 item 2)

**The old T16 LOC4 values in v1 §2.3 and §3.2 are struck as final quantitative
values.** They remain valid as the historical 16x record and as the Stage-2
materiality evidence that produced the Branch-B finding; they are no longer the
paper's numbers.

**The final numerical record is the RQMC record.** These eight quantities, and
only these, are the manuscript-facing LOC4 magnitudes:

| quantity | value | RQMC numerical band |
|---|---|---|
| W1 mean | `1339.0426` | `± 2.1105` |
| W1 Gini | `0.15114755` | `± 0.0010869` |
| `phi_A` | `0.00291492` | `± 0.00039130` |
| `phi_B` | `0.00070562` | `± 0.00065901` |
| `phi_P` | `−0.35279421` | `± 0.00078335` |
| `R_bg` | `0.50032122` | `± 0.00072355` |
| `phi_A + phi_B` | `0.00362054` | `± 0.00067681` |
| `s_opp` | `0.02395367` | `± 0.0043248` |

**These are numerical-integration bands. They are NEVER to be called confidence
intervals**, and no sampling-uncertainty language may attach to them. All seven
W1 **level** gates pass with these bands; the two failures are in §4.

Every value must travel with its band. A bare point estimate of any of the eight
is not a licensed claim.

---

## 3. Sign claims (H10 items 3 and 4)

### 3.1 The collective formulation is STRUCK

**"Stable component signs" is struck as a manuscript claim** — including in v1
§1's transcribed R-138 §9 list where it appears as `Q-1`, and in v1 §3.2's live
Disposition-B table where it is proposed. It is **not** replaced by another
collective-sign formulation: not "all component signs stable", not "the signs of
the decomposition are stable", not any equivalent.

Individual sign diagnostics may still be reported as part of the numerical gate
record. What is prohibited is the manuscript-facing collective assertion.

### 3.2 What may be said, individually

* **`phi_A` is positive.** Its 95% profile envelope `[0.0028051, 0.0029298]` is
  strictly positive. Licensed.
* **`phi_P` is negative.** Its 95% profile envelope `[−0.3534812, −0.3519888]`
  is strictly negative. Licensed.
* **`phi_B` carries the ruled qualification below, and nothing else.**

**The deputy's exact sentence. This wording is used VERBATIM wherever `phi_B` is
discussed; the older R-161 formulation carried in the RQMC memo is NOT the final
ruled wording and is not to be substituted for it:**

> “The ability contribution is small. It is positive over the conventional 90%
> profile region, but its sign is not resolved over the wider conventional 95%
> region once numerical precision and profile resolution are taken into
> account.”

The claim set carries the status token **`PHI_B_SIGN_UNRESOLVED_95_PROFILE`**.

**Prohibited about `phi_B`:** that it is statistically insignificant; that it has
no effect; that it is null or zero; that its sign is settled either way over the
95% region. The unresolved sign is a joint consequence of numerical precision
and profile grid resolution, not a significance statement.

---

## 4. The two normalized ratios (H10 item 5)

`r_phi_P` and `r_R_bg` are labelled **`MC_BANDED_NORMALIZED_DIAGNOSTIC`**.

| row | `r_T` | `E_r/S_r` | frozen threshold | verdict |
|---|---|---|---|---|
| `r_phi_P` | `−2.3341048` | `8.6804e−03` | `0.005` | FAIL — diagnostic only |
| `r_R_bg` | `3.3101511` | `7.2901e−03` | `0.005` | FAIL — diagnostic only |

Rules:

* they may be shown **only** as estimates with their RQMC numerical bands;
* they are **never** presented as precision-certified point contributions;
* the frozen `0.005` gate is **not** to be relaxed, recalibrated or re-derived;
* neither is a share — both lie outside `[0,1]`, both carry the record's
  `SIGNED NORMALIZED CONTRIBUTION RELATIVE TO BASELINE WELFARE INEQUALITY`
  label, and the no-pie-chart prohibition stands.

The failures are **denominator-dominated**: the W1 Gini relative numerical error
`0.0010869/0.15114755 ≃ 0.00719` alone accounts for approximately 83% of the
`r_phi_P` ratio band and approximately 99% of the `r_R_bg` band. This is an
explanation of the failure, not a reason to reclassify it.

**Conversely, the normalized quantities that passed remain certifiable**,
including the primary **`s_opp`** (`E_r/S_r = 4.3248e−03` against `0.005`),
`r_phi_A` and `r_phi_B`.

---

## 5. The ordering (H10 item 6)

**`phi_A > phi_B > phi_P` is retained — as the LOC4/profile/RQMC ordering, and
only as that.**

It survives every leave-one-scramble estimate and every one of the 20 evaluated
points inside the 95% profile region, in every scramble set. It is compatible
with the unresolved `phi_B` sign because `phi_P` remains far more negative.

Wording rules:

* state it as a property **of the LOC4 specification**, evaluated under the
  profile and the RQMC instrument — never as a property of the data;
* the pre-registered claim `Q-2` was the specific ordering `B > A > P`. Under
  LOC4 that claim is **false**. It is recorded as a specification-driven
  reversal. `A > B > P` is **not** substituted into the old "stable ordering"
  sentence, and the "stable ordering" wording is not carried across;
* the ordering statement is not a component-sign statement and must not be used
  to imply one (§3.1).

---

## 6. W4, W6 and the median (H10 item 7)

* **No cross-measure quantitative robustness claim.** W4 and W6 fail
  decomposition precision. No statement that the W1 decomposition is
  quantitatively robust across W4/W6 is licensed, in any form.
* **W4 may remain a normative-reference disclosure** where the manuscript
  requires one — but never as evidence of cross-measure quantitative
  robustness.
* **The W1 median stays `MC_BAND_ONLY_NONSMOOTH`**: `1244.077 ± 5.609`,
  reported as a banded non-smooth diagnostic, carrying no pass/fail
  classification. **It must not become a precision-certified headline.**

---

## 7. Numerical and profile uncertainty are never combined (H10 item 8)

Three distinct objects, reported separately, always:

| object | what it addresses |
|---|---|
| the RQMC band `± E_T` | numerical-integration uncertainty **only** |
| the 95% `beta_w_pexp2` profile envelope | `beta_w_pexp2`-conditional uncertainty **only** |
| sampling uncertainty of `theta_L4` | **not estimated here** |

**Neither the band nor the envelope is sampling uncertainty.** Their union, sum,
or any other combination must not be presented as a statistical confidence
interval. The conventional profile-LR support regions and the RQMC numerical
band are not the same object and are not to be shown as one.

The active-set / boundary caveat travels with every profile envelope: two
nuisance coordinates (`beta_l_age2_sf`, `beta_l_age2_sm`) are bound-active
throughout, `beta_w_pexp2` itself is pinned along the profile, and the grid
reaches its legal box boundaries.

---

## 8. The one-coordinate S-10 sensitivity is a diagnostic, not the profile conclusion (H10 item 9)

**v1 §3.3's standing-disclosure wording — "The preferred specification's welfare
level is sensitive to a single near-boundary wage coordinate" — does not survive
as the final profile conclusion.** That sentence describes the earlier
one-coordinate S-10 perturbation, which displaced `beta_w_pexp2` by half its
robust standard error **holding every other parameter fixed**.

**The final profile result is the nuisance-reoptimized one.** With the other 39
free coordinates re-optimized at each of the 30 constrained points, the W1-mean
envelope over the 95% region is `[1338.3178, 1339.9855]` around `1339.0426` — a
width of **0.1245%**, far below the charter's 1% reporting threshold.

So: the S-10 fact may be stated as a **specific sensitivity diagnostic**, with
its holding-others-fixed condition explicit. It may **not** be presented as the
profile answer, and it may not be carried as a standing qualification on every
LOC4 magnitude in place of the profile result.

---

## 9. No broad robustness restoration (H10 item 10)

**`Q-4` — "S-10 does not alter the qualitative conclusion" — is not restored**,
and no equivalent generic statement is licensed merely because the RQMC
difference gates pass.

What **is** certified: the **reported S-10 differences** (all five
S-10-minus-LOC4 scenarios pass on the full headline set), and the specified
**ordering and materiality** results. Those may be stated as what they are.

What is **not** certified: any generic claim that S-10 does not alter the
qualitative conclusion, or any collective robustness statement built from the
passing difference gates.

---

## 10. The status distinction: benchmark, not automatically the final JMP specification (H10 item 11)

The accepted M08T2 result is the final numerical record for the **current LOC4
benchmark**. It is **not** automatically the final JMP structural specification.

The authorized positive-specification sprint (JMP_PS1, opened at Goal-1 R-172)
may select an S8 successor; if it does, the paper's structural specification
changes while this numerical acceptance stands unaltered as the record of the
benchmark it certifies. That boundary is conceptually separate from the
numerical acceptance reached here, and the manuscript states it rather than
eliding it.

---

## 11. Carried forward from v1 §4, unchanged

These bind the manuscript and are not modified by v2:

1. **Disclosure 7 and the prohibited-claims list**: `δ_occ` is not a causal
   occupational wage premium; no baseline-versus-LOC4 coefficient change is a
   statistically significant difference.
2. **The median is uncertified in both arms**, level and difference, W1 and W4
   and W6 (and see §6 for its RQMC banding on the LOC4 arm).
3. **The 22 uncertified differences carry no interpretation.**
4. **W4/W6 quantitative robustness is claimable by neither arm** (§6).
5. **No subgroup welfare quantity** may be reported on either arm.
6. **LR / AIC / BIC are conventional references at a boundary-adjacent optimum
   in both arms** (`beta_l_age2_sm` and `beta_l_age2_sf` upper-bound-active on
   both sides), not a specification decision:
   `LR = 92.86956706583442` on `df = 3`, `p` (χ²₃) `= 5.297971492402584e-20`;
   ΔAIC `-86.86956706583442`; ΔBIC `-70.82187459199486` under `N = 1,555`
   clusters or `-56.976513041467115` under `N = 157,055` rows.
7. **C-16** stands as a named, uncorrected defect of the precision machinery in
   both arms.
8. **The exact nesting fact may be stated**, being algebraic rather than
   asymptotic: the LOC4 likelihood restricted to `δ = 0` reproduces the
   certified objective `18499.489277699933` **bitwise**, and the δ-gradient
   there is `(129.31441848714294, 51.479426015565224, -278.8939056307008)` —
   non-zero, so the baseline is not a stationary point of the extension.
9. **C-7**: Δ is the effect of the specification change **as a whole**, not the
   partial effect of the `delta_occ` term — both arms are evaluated at their own
   full re-estimated vectors; CRN pairs the randomness, not the parameters.
10. **The baseline closure is not withdrawn.** The M08 prototype closure stands;
    the corrected baseline remains the accepted nested reference specification.

---

## 12. The two T2-A reporting corrections, binding on the manuscript

Recorded at Goal-1 R-175 from the review's H1; both are count/transcription
corrections that leave the numerical record and the envelopes intact:

1. the convergence reading is **29 constrained profile optimizations plus the
   accepted unrestricted optimum**, not "30 points converge SINGLE-OPTIMUM";
2. the in-region count is **20 of 30**, not 30.

Any manuscript sentence that repeats either count uses the corrected figure.

---

*v2 is operative. v1 is superseded for manuscript purposes and retained as
history.*
