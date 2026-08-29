# JMP-M08T2 — ACCEPTANCE OF THE LOC4 PREFERRED SPECIFICATION AND ITS FINAL NUMERICAL RECORD (v1)

**STATUS: ACCEPTED AND CLOSED.** This is the charter's permanent output 5
(`JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` §8). It closes
JMP-M08T2 at Goal-1 **R-175**.

| Status label | Object it qualifies |
|---|---|
| **`LOC4_PREFERRED_STRUCTURAL_SPECIFICATION`** | the preferred structural specification (set R-157, unchanged and now final for this benchmark) |
| **`MC_BANDED_LEVELS`** | its W1 magnitudes — levels reported with their RQMC numerical bands |

**Returned verdict of the independent Tier-2 review, its final line, VERBATIM:**

> `LOC4_PREFERRED_MC_BANDED_LEVELS`

---

## 0. Sources — everything below is transcribed, and cited

Every numeral in this document is TRANSCRIBED from one of the following, and
each is cited inline as `[memo §n]` or `[review Hn]`. Nothing is recomputed,
paraphrased or inferred here.

| Tag | Document | sha256 |
|---|---|---|
| `[charter]` | `docs/Missions/JMP_M08T2_LOC4_boundary_and_final_precision_charter_v1.md` | `d4de2055ca5db8c6e3d3ea4c945b027ee0a80c0764ba4dc2c99d7d8154968d80` |
| `[memo]` | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_rqmc_final_precision_results_v1.md` | `a456113473cebad748915ad1448134d891023951d05fb1be96ab1f6c914d90f7` |
| `[profile]` | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_beta_w_pexp2_profile_results_v1.md` | `99b5df2e163c9a0b11ab9f8c77dcbb769797a130174a96f3e51a8b4047aa7fce` |
| `[preflight]` | `MNL/docs/France_case/P2a/FR_P2a_m08_rqmc_preflight_codex_review_v1.md` | `5244968fdf7ac6d5fa2c985b67e273d21259454730d1f99661905153a1849916` |
| `[review]` | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_tier2_independent_review_v1.md` | `06d2c0fc9cfd62ff1eb220e62cc34f660a739e0d594f079e47ed7307bab4b396` |
| `[rulings]` | `docs/Missions/JMP_M08_goal1_rulings_document_v4.md` (R-59 … R-175) | `68da3f84e986486dd446c1fb0e144d13620140c5a565068beda3ba40ac0765bc` |

---

## 1. The mission arc

**The charter.** JMP-M08T2 was opened on the charter above, `d4de2055ca5db8c6…`,
re-verified at every stage boundary of the execution `[memo, header]`. §5 froze
the design, §6 fixed the estimator and the gates, §7 fixed the three-way
uncertainty report, §8 fixed the six permanent outputs and §2 fixed the eight
RETURN conditions.

**T2-A — the `beta_w_pexp2` profile — ACCEPTED with a sign qualification.**
The frozen grid is the 21 values from −0.10 to +0.10 in 0.01 increments, plus
the exact unrestricted LOC4 estimate, plus eight authorized adaptive bisection
points: **30 evaluated parameter vectors** `[review H1]`. At each constrained
point `beta_w_pexp2` is fixed and the other **39** free LOC4 coordinates are
reoptimized `[review H1]`. The unrestricted estimate is `−0.0196886533` and is
interior; the active nuisance-bound set is `{beta_l_age2_sf, beta_l_age2_sm}`
throughout; the LR profile is connected, with support regions
`[−0.079704, +0.040347]` (90%) and `[−0.091215, +0.051871]` (95%), from the
fixed cutoffs `2.7055434541` and `3.8414588207` interpolated between the final
`0.0025` brackets `[review H1, H2]`. T2-A was accepted at Goal-1 **R-161** under
`T2A_PROFILE_ACCEPTED_WITH_COMPONENT_SIGN_QUALIFICATION`, carrying
`PHI_B_SIGN_UNRESOLVED_95_PROFILE`.

**Two T2-A reporting corrections, recorded at R-175 and binding here.**
`[review H1]`

1. The convergence reading is **29 + 1**, not 30: the unrestricted MLE is one of
   the 30 evaluated vectors but is explicitly *"theta_L4 of record (not refit)"*,
   so "all 30 points converge SINGLE-OPTIMUM" reads as 29 constrained profile
   optimizations plus the accepted unrestricted optimum.
2. The in-region count is **20 of 30**, not 30: the T2-A memo §6 statement that
   "30 points fall in the [95%] region" is false. The RQMC record correctly
   identifies 20 of 30 evaluated points inside the 95% region. The envelope
   numerals correspond to the in-region points, so the envelopes are unaffected.

Neither correction contaminates the numerical record `[review H1]`, and T2-A's
acceptance is not reopened.

**T2-B part 1 — the three-round Codex preflight, including the E2 closure.**
Round 1 accepted R1, R2 and R4–R9 and rejected R3 (R-164). One bounded
correction cycle followed — the reference map reconstructed independently of the
generator, and **both statistical t-bands deleted from the R3 pass path rather
than recalibrated** (R-165). The round-2 re-review rejected R3 a second time on
completeness and the matter was returned to the deputy (R-166). The **deputy E2
ruling** authorized one final exceptional bounded correction scoped to
R3F-1..R3F-4, with generator, node frames, qW, seeds and all downstream geometry
frozen and hash-verified byte-identical across the patch (R-167). The
commissioned fresh read-only review returned R3F-1..R3F-4 **all ACCEPT and
OVERALL ACCEPT** (R-168), confirming the generator unchanged, all eight frames
byte-unchanged, the t-band absent and no extra gate change
`[preflight]`, `[review H6]`.

**T2-B part 2 — the eight-scramble pricing.** One EUROMOD run, as authorized.
**2,549,225** nodes priced in **18,764.4 s = 5.2123 h** of EUROMOD time against
the frozen **7 h** guard, which was evaluated at every one of the 136 calls and
was never approached `[memo §1.3]`. Sealed priced panel sha256
**`b1879fcf2c210d337a4f4d3bfff93d06a6e044f8da1326f6ca3a5ab168d76f00`**,
3,665,581 rows at grain `(source_idhh, slot, source_idperson)`, 0 non-finites in
either persisted column `[memo §1.3]`. The rebind verified **37/37** theta
vectors bitwise, the 30 profile vectors having been replayed and matched against
their stored T2-A hashes 30/30 `[memo §1.1]`, `[review H5]`.

**The estimator.** `Jbar_i = mean_r(J_ir)` **before** the log and the
money-metric inversion — checked numerically as well as algebraically, the two
routes disagreeing by at most `1.37e−14` (males) and `1.42e−14` (females)
`[memo §2]`, `[review H5]`. The band is the chartered delete-one-scramble
jackknife, `SE_jack = sqrt[(7/8)·Σ_r (T_(−r) − T_bar)²]` and
`E_T = 2.364624251 · SE_jack`, with **no** bias term folded in `[memo §2]`,
`[review H6]`.

---

## 2. The final numerical record — all seven W1 level gates PASS, with their bands

`[memo §4.1]`, confirmed `[review H7]`. Thresholds are the charter's, frozen.

| Gate (charter §6) | Value | RQMC band `± E_T` | Threshold | Verdict |
|---|---|---|---|---|
| W1 mean, relative MC error | `1339.042631` | `2.1105` | `E_T/S_k = 1.576e−03` ≤ `0.0025` | **PASS** |
| W1 Gini | `0.151147548` | `1.0869e−03` | `0.00125` | **PASS** |
| `phi_A` level | `0.002914922` | `3.9130e−04` | `0.00125` | **PASS** |
| `phi_B` level | `0.000705617` | `6.5901e−04` | `0.00125` | **PASS** |
| `phi_P` level | `−0.352794213` | `7.8335e−04` | `0.00125` | **PASS** |
| `R_bg` level | `0.500321222` | `7.2355e−04` | `0.00125` | **PASS** |
| `phi_A+phi_B` level | `0.003620539` | `6.7681e−04` | `0.00125` | **PASS** |

Also passing: LOC4-minus-baseline differences on the full headline set, all five
S-10 difference scenarios, the sign/ordering gate, Shapley and `R_bg`
accounting (worst statistic across 27 checks `5.551115123125783e−17`, machine
epsilon), and support/index domains — common support in every scramble set and
every measure, zero non-finite and zero non-positive households, and
`no_shift_or_floor_applied = true` throughout `[memo §4.4–§4.7]`,
`[review H7, H9]`.

**These bands are numerical-integration bands. They are not sampling confidence
intervals.** `[memo §7]`, `[review H10 item 2]`

---

## 3. The two normalized-ratio failures — `MC_BANDED_NORMALIZED_DIAGNOSTIC`

`ALL_PRIMARY_W1_GATES_PASS = false`. Exactly one gate family failed:
`normalized_contributions`, 2 of its 6 rows `[memo §4.2]`.

| row | `r_T` | `E_r/S_r` | Threshold | Verdict |
|---|---|---|---|---|
| `r_phi_A` | `0.0192853` | `2.5325e−03` | `0.005` | PASS |
| `r_phi_B` | `0.0046684` | `4.3395e−03` | `0.005` | PASS |
| **`r_phi_P`** | **`−2.3341048`** | **`8.6804e−03`** | `0.005` | **`E_r_OVER_S_r_EXCEEDS_THRESHOLD`** |
| **`r_R_bg`** | **`3.3101511`** | **`7.2901e−03`** | `0.005` | **`E_r_OVER_S_r_EXCEEDS_THRESHOLD`** |
| `r_phi_A+phi_B` | `0.0239537` | `4.3248e−03` | `0.005` | PASS |
| `s_opp` | `0.0239537` | `4.3248e−03` | `0.005` | PASS |

**The failures are genuine and are left as failures.** The threshold remains
`0.005`; the two rows are recorded as failures; no recalibration was made
`[review H7]`. They are **denominator-dominated**: the W1 Gini relative
numerical error is `0.0010869/0.15114755 ≃ 0.00719`, which alone accounts for
approximately **83%** of the observed `r_phi_P` ratio band and approximately
**99%** of the `r_R_bg` band `[review H7]`; the W1 Gini *level* itself passes
its own gate `[memo §4.2]`.

**Disposition, ruled:** `r_phi_P` and `r_R_bg` are labelled
**`MC_BANDED_NORMALIZED_DIAGNOSTIC`** — shown only as estimates with their RQMC
numerical bands, never as precision-certified point contributions
`[review H7, H10 item 5]`. The normalized quantities that passed — including the
primary `s_opp` — retain their certified status `[review H7]`.

There was no post-hoc relaxation. The earlier pre-pricing R3 history is a
different object: an initially data-dependent statistical R3 criterion was
rejected, and the correction **removed** that statistical t-band from the R3
pass path rather than changing the final welfare-ratio threshold `[review H7]`.

---

## 4. `phi_B` — `PHI_B_SIGN_UNRESOLVED_95_PROFILE`

The mechanical T2-A §6 test was met — the RQMC 95% envelope
`[+2.2054256e−05, +1.6266955e−03]` is strictly above zero, and the evaluation
runner emitted `PHI_B_POSITIVE_PROFILE_STABLE` as that test's output
`[memo §6]`. **That output is superseded and is not adopted**, on three verified
arithmetical grounds `[memo §6]`, `[review H8]`:

1. the envelope minimum `2.2054e−05` is **3.35%** of the instrument's own MLE
   band `6.5901e−04`;
2. the 16x and RQMC instruments differ by a small smooth offset near the right
   profile edge — at `b = +0.045`, 16x `−7.66e−06` against RQMC `+6.18e−05`; at
   `b = +0.050`, `−4.97e−05` against `+2.21e−05` — while **at the unrestricted
   MLE both instruments are positive**, which is not to be misstated;
3. the RQMC zero crossing is `b* ≈ 0.052867`, only `0.000996` above the
   interpolated 95% endpoint `0.051871` — below the frozen `0.0025` profile
   resolution.

**The ruled sentence, VERBATIM. This exact wording travels with every
manuscript use of `phi_B`:**

> “The ability contribution is small. It is positive over the conventional 90%
> profile region, but its sign is not resolved over the wider conventional 95%
> region once numerical precision and profile resolution are taken into
> account.”

`phi_B` must **not** be characterized as statistically insignificant, nor as
having no effect `[review H8]`. Positivity over the conventional 90% region
remains supported `[review H8]`; on that region `phi_B ∈ [+1.030e−04,
+1.451e−03]` `[memo §6]`.

`phi_A` and `phi_P` are different: their 95% envelopes exclude zero cleanly —
`phi_A ∈ [0.0028051, 0.0029298]` strictly positive, `phi_P ∈ [−0.3534812,
−0.3519888]` strictly negative — so their **individual** sign claims stand
`[memo §6]`, `[review H3]`.

**No collective sign formulation is licensed.** "Stable component signs", "all
component signs stable" or any equivalent collective claim is struck
`[review H9, H10 item 3]`.

---

## 5. Ordering, median, and the secondary measures

**Ordering `phi_A > phi_B > phi_P` — retained, as the LOC4/profile/RQMC
ordering.** It holds in the eight-scramble estimate and in every one of the
eight leave-one-scramble-out estimates `[memo §4.3]`, and at **every one of the
20 in-region profile points, in every scramble set** `[memo §5]`, `[review H4]`.
M-1…M-4 materiality against the baseline also holds at every in-region point,
and no profile point causes the W1 Gini difference or opportunity materiality to
disappear `[memo §5]`, `[review H4]`. This is compatible with the unresolved
`phi_B` sign because `phi_P` remains far more negative `[review H10 item 6]`;
it is **narrower** than a collective sign-stability statement `[review H4]`.

**The W1-mean profile envelope.** `[1338.3178, 1339.9855]` around the MLE
`1339.0426`, a width of `0.0012454` = **0.1245%** of the MLE value — far under
the charter's 1% disclosure trigger `[memo §5]`, `[review H3]`. The displayed
envelopes are envelopes over the **evaluated in-region grid points**, while the
LR endpoints are interpolated to `−0.091215` and `+0.051871`; immaterial for W1
mean, `phi_A` and `phi_P`, and directly material for `phi_B` `[review H3]`.

**The W1 median — `MC_BAND_ONLY_NONSMOOTH`.** `1244.077 ± 5.609`, a banded
non-smooth diagnostic carrying **no** pass/fail classification; none was
assigned `[memo §4.8]`, `[review H9]`. It must not become a precision-certified
headline `[review H10 item 7]`.

**W4 and W6 — no cross-measure quantitative robustness claim.** Both fail
decomposition precision (e.g. `W4_phi_P` difference `E_T = 1.477e−03`,
`W6_phi_P` `E_T = 1.741e−03`) `[memo §4.8]`. Per charter §6 this licenses **no**
statement that the W1 decomposition is quantitatively robust across W4/W6, and —
also per charter §6 — it does **not** by itself overturn LOC4's preferred
structural status `[memo §4.8]`, `[review H9, H10 item 7]`.

**The three-way separation.** The RQMC band, the 95% `beta_w_pexp2` profile
envelope and sampling uncertainty are three different objects. Neither the band
nor the envelope is sampling uncertainty, and they must never be merged into a
confidence interval `[memo §7]`, `[review H2, H10 item 8]`.

---

## 6. The final verdict, and what it does and does not settle

**Verdict.** `LOC4_PREFERRED_MC_BANDED_LEVELS` `[review, final line]`.

The review found no basis for `FULL_NUMERICAL_FREEZE` and no defect that makes
the preferred specification unresolved or invalidates the evidence chain. The
required claim-set corrections do **not** warrant
`PREFERRED_SPECIFICATION_UNRESOLVED`: they are exactly the manuscript narrowing
the charter contemplates after a primary normalized-contribution failure. The
two T2-A reporting-count defects and the historical R3 preflight corrections do
not undermine the final evidence chain `[review H10, closing]`.

**Statuses set here:**

* **`LOC4_PREFERRED_STRUCTURAL_SPECIFICATION`** — the specification;
* **`MC_BANDED_LEVELS`** — its magnitudes.

**The successor claim set is `JMP_M08_LOC4_manuscript_claim_set_v2.md`**
(charter permanent output 6), which carries the eleven H10 strikes and additions
exactly. `JMP_M08_LOC4_manuscript_claim_set_proposal_v1.md` is superseded for
manuscript purposes and remains valid only as immutable history of the moment it
recorded.

### 6.1 The sprint boundary — benchmark, not automatically the final JMP spec

This acceptance is the **final numerical record for the CURRENT LOC4
benchmark**. It is **not** automatically the final JMP structural specification.
The deputy's post-meeting sprint ruling (R-172) opened the authorized
positive-specification sprint JMP_PS1; if that sprint selects an S8 successor,
the structural specification of the paper changes while this numerical
acceptance stands unaltered as the record of the benchmark it certifies. The two
questions are conceptually separate, and the distinction is preserved
deliberately `[review H10 item 11]`.

JMP-M08T2 is **CLOSED**. No further numerical instrument is authorized on this
benchmark; none was run and none is proposed `[memo §9]`.
