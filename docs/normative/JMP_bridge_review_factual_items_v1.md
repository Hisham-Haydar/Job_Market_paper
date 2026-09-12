# JMP_bridge_review_factual_items_v1.md — SRC-3: factual items raised by BRIDGE-REVIEW-1

| Field | Value |
|---|---|
| Mission | SRC-3 — resolve factual items raised by `JMP_W1_stochastic_ability_set_bridge_review_v1.md` (BRIDGE-REVIEW-1) |
| Status | READ-ONLY frame/source audit. **Not a welfare computation.** No welfare number, no counterfactual, no decomposition, no household-level output written. |
| Scope note | Item 1 required computing aggregate statistics over the accepted S10 criterion-A engine-ready frames (parquet). This is arithmetic on frame columns (`hours`, `working`, `in_choice_domain`), reported as aggregates only — it is not a welfare object. |
| Output file | `Job_Market_paper/docs/normative/JMP_bridge_review_factual_items_v1.md` |

---

## 1. Masking incidence at the floor

**Frames used** (the accepted S10 criterion-A engine-ready frames, R=100 draws + chosen + non-employment row ⇒ 101 rows/household for both groups):

- `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/singles_engine_ready_criterion_a_v1.parquet` — 155,540 rows, 1,540 households (703 male, 837 female; `household_class == "single"` throughout).
- `MNL/outputs/corr/s10_criterion_a_iid_r100_v1/couples_engine_ready_criterion_a_v1.parquet` — 224,523 rows, 2,223 households.

**Definitions used.** A "market alternative" = a row with `working == 1` (singles) / `working_male == 1` or `working_female == 1` (couples, computed separately per spouse). "In choice_domain" = `in_choice_domain == True`. For each household, `h_min` = the minimum of `hours` (singles) / `hours_male`, `hours_female` (couples, per spouse) over that household's rows satisfying **both** conditions. "Masked market alternatives" per household = count of rows with `working(_male/_female) == 1` **and** `in_choice_domain == False`.

### Singles

| Group | n hh | h_min: min | p5 | p25 | median | p75 | p95 | max | share h_min > 5h |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Male | 703 | 7.00 | 15.06 | 17.45 | 19.13 | 20.82 | 23.14 | 27.06 | **1.0000** |
| Female | 837 | 6.00 | 14.55 | 17.40 | 19.33 | 20.96 | 23.27 | 26.09 | **1.0000** |

Masked market alternatives per household: male mean 0.0541, median 0, max 33 (out of ≤100 market draws); female mean 0.0000, median 0, max 0. Every household in both groups has at least one in-domain market alternative (no household has an undefined `h_min`).

### Couples (computed per spouse)

| Spouse | n hh | h_min: min | p5 | p25 | median | p75 | p95 | max | share h_min > 5h |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Male | 2,223 | 9.00 | 21.44 | 23.94 | 25.54 | 27.15 | 29.47 | 31.68 | **1.0000** |
| Female | 2,223 | 5.00 | 13.41 | 16.01 | 17.72 | 19.49 | 21.96 | 25.54 | **0.99955** (1 household exactly at 5.0) |

Masked market alternatives per household: male-spouse mean 0.0009, median 0, max 2; female-spouse mean 0.0018, median 0, max 1; combined (either spouse masked) mean 0.0027, median 0, max 3. No couple household has zero in-domain market alternatives for either spouse.

**Caveat (mandatory).** These frames are R=100 **numerical draws** per household (`hours` are draws from the Uniform[5,70] proposal, not an enumeration of the structural support), so `h_min` here is the **minimum of the sampled hours actually drawn for that household**, not the infimum of the structural support of $g_i$. Every group's `h_min` distribution sits well above 5h essentially because 100 draws from a continuous Uniform[5,70] proposal land near the left edge only rarely (expected minimum of 100 iid Uniform[5,70] draws is $5+65/101\approx5.64$h, consistent with the medians of 17–26h seen once market draws are further conditioned on `in_choice_domain`). **This measures masking incidence in the executed frames — how often a market draw is present but excluded by `in_choice_domain`, and how far the closest surviving market draw sits from 5h in this particular random sample — not the structural support of $g_i$, which is a separate (continuous, unmasked-by-construction on `[5,17.5]`) object addressed in item 3.** Masking itself (rows with `working==1` and `in_choice_domain==False`) is rare — well under 1% of market draws per household in every group/spouse cut above — and is concentrated in a small number of households (max 33 for singles-male, ≤3 for couples), not systematic across the sample.

**One-line verdict (item 1):** masking of market alternatives by `in_choice_domain` is present but rare (mean ≪1 masked market draw/household in every cut) and not the reason `h_min` sits above 5h in these frames — that gap is sampling discreteness from R=100 continuous draws, not floor exclusion; only one household (a couple, female spouse) has a surviving in-domain market draw exactly at the 5h floor, and none has a surviving draw below it.

---

## 2. Wage support: `DEFAULT_W_MAX` vs. `[2, 590]`

Two distinct objects, both in EUR/hour, governing two distinct roles:

- **`continuous.py:38–41`** (`MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/alternatives/continuous.py`):
  ```
  DEFAULT_H_MIN = 5.0
  DEFAULT_H_MAX = 70.0
  DEFAULT_W_MIN = 2.0
  DEFAULT_W_MAX = 170.0
  ```
  These bound the **Uniform[2, 170] EUR/hour proposal** (`q`) used by `generate_draws_long` to actually draw the wage values that populate each household's sampled alternatives (`log_q_wage = -log(w_max - w_min)`, a Uniform log-density). **This governs the executed draws** — every wage value that appears as an alternative in the S10/S11 frames is drawn from `[2, 170]`.

- **`[2.0, 590.0]`**, set in `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s10_criterion_a_iid_r100/s10_estimation_lib_v1.py:80,97`:
  ```python
  spec.wage_support_lower, spec.wage_support_upper = 2.0, 590.0
  ```
  consumed by `_structural_wage_support(spec)` in both `engine_jax.py:123–128` and `engine_numpy.py:50–55`, and used inside `_jlog_wage_density`/the wage-density truncation terms to renormalise the **structural log-normal wage-opportunity density** (`g`'s wage component) on `[2, 590]`. **This governs the structural density** used to score wage values in the likelihood (`log_w` in the `V = u + log_h + log_w + log_market − log_prior` index), not what values are drawn.

**Reconciliation.** The two intervals answer different questions and are not in conflict as code, but they are **not consistent with each other**: the estimated log-normal `g`-density is normalised as though wages could be observed up to 590 EUR/hour, while the sampled alternatives that are actually scored against that density never exceed 170 EUR/hour (the executed draws are a strict subset of the structural density's declared support). This is exactly the reconciliation the bridge memo and review both flag as open (memo §7 row 12, §4.3; review R3, R10-4, correction P3) — immaterial to the degeneracy result at the hours floor (item 1/3 concern hours, not wages), but a genuine cross-document inconsistency in the wage dimension that has not been closed in source.

---

## 3. F35: which of the three sources holds

**Three sources, read directly.**

1. **SRC-1's pooled-ancestor spec** (`estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`, the common ancestor both S11 group specs declare — **not itself the spec that ran S11**), `hours_opportunity:` block:
   ```yaml
   - variable: "working_lh"
     coefficient: "beta_h_lh"   # long-hours [44.5,70]; F35 remains reference
   ```
   Five hours coefficients (`beta_E, beta_h_pt1, beta_h_pt2, beta_h_ft, beta_h_lh`); F35 `[33.5,36.5]` has no coefficient, folded into the residual/reference region.

2. **The note's residual-width arithmetic** (`W1_latent_set_identification_note_v1.md:294–298, 366`): residual reference width **26.5h**. Checking the arithmetic: total support `[5,70]` = 65h; band widths pt1=4, pt2=2, f35=3, ft=4, lh=25.5 → sum 38.5h → residual = 65 − 38.5 = **26.5h**. This subtraction already removes the f35 band's 3h from the residual — i.e. the note's own number is internally consistent only if F35 is **not** the reference band (if it were, the residual would be 26.5+3=29.5h). This is indirect evidence, not a direct spec read.

3. **Direct read of the two files that actually produced the S11 estimates** (per SRC-2's provenance finding, confirmed here):
   - **Singles**, `MNL/experiments/JMP_SEMINAR_SPRINT/export/gpu_research_bundle_v1/spec/estimation_spec_S8_corrected_floor5_v1.yaml`, `parameter_order:` (51 coordinates total):
     ```
     - beta_E                  # 18
     - beta_h_pt1              # 19
     - beta_h_pt2              # 20
     - beta_h_ft                # 21
     - beta_h_lh                # 22
     ...
     - beta_h_f35              # 50
     ```
     `beta_h_f35` is a live coordinate (appended at the end of the parameter order, alongside three further `delta_occ_2/3/4` additions not present in the ancestor's partition at all).
   - **Couples**, `MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml`:
     ```yaml
     gender_split:
     - beta_E
     - beta_h_pt1
     - beta_h_pt2
     - beta_h_f35
     - beta_h_ft
     - beta_h_lh
     ```
     `beta_h_f35` is listed among the gender-split hours coefficients, with `beta_h_f35_m`/`beta_h_f35_f` initial values `2.579482184820325` each.
   - **Certified fitted values**, `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md`:
     ```
     | beta_h_f35   | 2.06556193 | 0.08944789 | [-10, 10] | no | no | -1.105   |
     | beta_h_f35_m | 2.28879659 | 0.08213478 | [-10, 10] | no | no | -0.37449 |
     | beta_h_f35_f | 2.02835055 | 0.06823924 | [-10, 10] | no | no | -0.74557 |
     ```
     ("no" in the "fixed" column = not fixed, i.e. genuinely estimated, with a standard error, in every one of singles/couples-male/couples-female.)

**Which holds.** The pooled ancestor's "F35 remains reference" comment describes a spec that **is not the spec of record** — it is the superseded common ancestor. Both files that actually produced the certified S11 estimates carry `beta_h_f35` as a live, estimated, non-fixed coefficient with a reported standard error. **F35 carries its own coefficient in the S11 specs of record; it is not the reference band.** The note's 26.5h residual-width arithmetic is the one of the three that is consistent with this direct read; the ancestor spec's comment is stale.

**Resulting shared-opportunity parameter count.** With F35 included, the hours-opportunity block has **six** coefficients, not five:
```
Hours (6):      beta_E, beta_h_pt1, beta_h_pt2, beta_h_f35, beta_h_ft, beta_h_lh
Market (12):    beta_E_gsur, beta_E_drgn2..8 (7), beta_E_drgur, beta_E_drgmd, beta_E_y2015, beta_E_y2017
Occupation (6): beta_occ_{2,3,4}_m, beta_occ_{2,3,4}_f
Wage (6):       beta_w0, beta_w_educL, beta_w_educH, beta_w_pexp, beta_w_pexp2, sigma
```
Total shared-opportunity parameters = 6 + 12 + 6 + 6 = **30**, not the memo's 29. (The singles spec of record also carries three further `delta_occ_2/3/4` coordinates not part of this shared-opportunity/preference partition at all — noted here for completeness, not scored into either count, since neither the memo nor the review's partition names them.)

---

## 4. Check households: sex flag of 1504300 and 1550400

Both looked up directly in the singles engine-ready frame (`in couples`: False for both — neither is a couple household):

| idhh | dgn | female | household_class |
|---:|---:|---:|---|
| 1504300 | 1 | 0 | single |
| 1550400 | 1 | 0 | single |

Coding check across the full singles frame confirms `dgn == 1 ⇔ female == 0` throughout (84,537 rows at `dgn=0/female=1`; 71,003 rows at `dgn=1/female=0`; no exceptions). **Both 1504300 and 1550400 are single men.** This satisfies the review's stated condition for F6 consistency (R9): "the two singles are consistent only if both are men."

---

## 5. Theory domain: is $\mathcal J$ finite?

`Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex`, the "Results" section's standing-assumptions statement (lines 374–377), quoted verbatim:

```
Throughout this section the standing domain assumptions are in force: every
$R\in\mathcal R$ is continuous and monotonic in consumption, and $\mathcal J$
(hence every $A\in\mathcal A$) is finite. Representation, Job Duplication
Invariance, and Job Neutrality are maintained as structural axioms.
```

(A comment immediately above the section, lines 358–362, states the same thing as a maintained convention: `mathcal J is finite, hence every A in mathcal A is finite`.) **Confirmed: the theory's Results section, under which `thm:w1` is proved, assumes $\mathcal J$ finite.**

---

## Summary of resolutions

| # | Item | Resolution |
|---|---|---|
| 1 | Masking incidence at the floor | Masking of market draws by `in_choice_domain` is rare (≪1 masked draw/household on average, max 33/2223/etc.) and does not explain why `h_min` sits above 5h in the frames — that is sampling discreteness of R=100 continuous draws. Only one household (couple, female spouse) has an in-domain draw exactly at the 5h floor. |
| 2 | Wage support | `[2,170]` (continuous.py `DEFAULT_W_MAX=170.0`) governs the executed draws; `[2,590]` (`s10_estimation_lib_v1.py`, consumed by `_structural_wage_support`) governs the structural log-normal density. The two are inconsistent with each other and unreconciled in source. |
| 3 | F35 | The S11 specs of record (not the pooled ancestor) carry `beta_h_f35` as a genuinely estimated, non-fixed coefficient (singles and both couples genders). F35 is not the reference band. Shared-opportunity parameter count = 30, not 29. |
| 4 | Check households | 1504300 and 1550400 are both single men (`dgn=1`, `female=0`). |
| 5 | Theory domain | `jobs_and_wellbeing.tex:374–377` states $\mathcal J$ (hence every $A$) is finite as a standing assumption of the Results section. |
