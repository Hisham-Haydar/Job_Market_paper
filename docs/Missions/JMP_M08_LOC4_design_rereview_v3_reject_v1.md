# Narrow Re-Review — JMP-M08 LOC4 Design v3

Scope is restricted exactly as requested: the six corrections mandated in my v2 review plus the two A1 disclosure corrections. Nothing previously accepted is reopened. I reviewed v3 against the relevant recorded numerical machinery where necessary. 

**OVERALL VERDICT: REJECT — NARROW CORRECTIVE RETURN.**

Five of the six mandated corrections are substantively cured. The remaining defect is concentrated in M-5: v3 correctly repairs the arm-to-arm sign/order logic and tie convention, but then adds the six `T8_ab` bases to the unanimity gate without authority from the recorded sign/order instrument. That unsupported extension is propagated through §4. There is also one sentence in the second A1 disclosure that should be corrected because it confuses the target estimand with the CRN coupling.

This rejection does **not** reopen or reject R-a, direct CRN differencing, the arm-precision rider, Path-B reconciliation, or the estimation architecture.

| Item                                            | Verdict                        | Ruling                                                                              |
| ----------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------- |
| 1. M-5 arm-to-arm sign/order + tie convention   | **NOT CURED, narrowly**        | Arm-to-arm construction and tie convention are cured; accepted-replicate set is not |
| 2. M-5 propagation through §4                   | **NOT CURED, derivative only** | Logic propagates correctly, but propagates the unsupported `T8` requirement         |
| 3. Transcribed `E_Δ` estimator                  | **CURED**                      | Exact accepted functional and scaling are now specified                             |
| 4. Corrected C-8 `n/(n+1)` statement            | **CURED**                      | Numerator cancellation and surviving normalization factor correctly distinguished   |
| 5. G-L4-8 curvature/rank + blocking consequence | **CURED**                      | Identification diagnostic is now genuinely gating                                   |
| 6. Exact frozen `δ_occ` bound                   | **CURED**                      | Formula and slack are completely deterministic pre-estimation                       |
| A1 disclosure 1: CRN covariance wording         | **CURED**                      | Universal overstatement removed                                                     |
| A1 disclosure 2: partial-CRN regime             | **NOT CURED, wording only**    | Diagnostic treatment is right; statement about the estimand is too strong           |

## 1. M-5 arm-to-arm sign/order and ties — NOT CURED, narrowly

The principal v2 defect **is fixed**.

The new indicators

$$
S_{c,b}
=
1\left\{
\operatorname{sgn}(\phi^{L4}_{c,b})
\neq
\operatorname{sgn}(\phi^{0}_{c,b})
\right\},
$$

and

$$
O_{cd,b}
=
1\left\{
\operatorname{sgn}
(\phi^{L4}_{c,b}-\phi^{L4}_{d,b})
\neq
\operatorname{sgn}
(\phi^{0}_{c,b}-\phi^{0}_{d,b})
\right\}
$$

now test exactly the correct economic event: whether the **component's own sign or ordering changes between baseline and LOC4**, rather than the sign or ordering of \(\Delta\). That directly cures my main v2 objection. 

The tie convention is also adequately frozen. `sgn(0)=0`; exact zero is a separate state; exact pairwise equality is an ordering tie; moves into or out of zero/tie count as changes; no epsilon is introduced. That satisfies the requested deterministic convention.

The residual defect is §3.5.4.

v3 declares that M-5's accepted replicates comprise

* four `T12_-b`; **and**
* six `T8_ab`.

But the recorded `threshold_set_of_record` states expressly that the sign/order requirement is:

> signs and ordering identical between `T16` and **every `T12` LOO**. 

The actual 16x evaluation record is equally explicit. It has eleven numerical sub-bases because the precision estimator requires `T16`, six `T8_ab`, and four `T12_-b`; nevertheless its sign/order gate reports **“zero sign disagreements with any `T12` LOO; zero ordering failures.”** The six T8 bases enter

$$
|T16-\bar T8|
$$

inside \(E_T\); they are not part of the recorded sign/order unanimity test. 

That distinction matters.

v3 itself says T8 is being added because:

> “there is no principled ground on which to exclude” it.

That is a **new construction**, not a transcription from the accepted machinery. Worse, v3 correctly recognizes in C-15 that the T8 bases are substantially noisier and that their inclusion is likely to generate `INDETERMINATE_MC`. Thus the added rule can change the mission verdict and cause a deputy return.

The proper M-5 replicate set on the evidence currently in force is therefore:

$$
\boxed{\text{full basis }T16
\quad+\quad
\text{four }T12_{-b}\text{ leave-one-superblock-out replicates}.}
$$

The six `T8_ab` bases should remain in the \(E_\Delta\) construction where the accepted estimator uses them; they should **not** be imported into M-5 unless the deputy separately authorizes that strengthening.

So item 1 is **not cured only on this replicate-set point**. The arm-to-arm indicators and exact zero/tie convention themselves pass.

## 2. Propagation through §4 — NOT CURED, derivative only

The conceptual propagation is now correct.

§4.1 correctly separates M-5 from the magnitude rule

$$
|\widehat\Delta|\pm E_\Delta,
$$

and treats M-5 as a binary configuration test. Branch A requires no change, Branch B requires a stable change, and Branch C treats disagreement as indeterminate. That is the correct architecture. 

But §§3.7, 4.3, 4.4 and 4.5 all propagate the same unsupported requirement that M-5 agree across the six T8 bases as well as the four T12 bases.

Therefore item 2 is **not cured derivatively**, not because the branch logic is wrong.

The needed correction is purely mechanical: wherever M-5 currently refers to

> `T16 + four T12_-b + six T8_ab`

replace the M-5 replicate universe with

> `T16 + four T12_-b`.

Do **not** alter the `T8_ab` role in \(E_\Delta\).

## 3. Exact `E_Δ` estimator — CURED

This is now fully specified.

v3 defines, basis-by-basis,

$$
\Delta_{16},\qquad
\Delta_{12,-b},\qquad
\Delta_{8,ab},
$$

then uses

$$
\bar\Delta_{12}
=
\frac14\sum_{b=1}^4\Delta_{12,-b},
$$

$$
SE_{MC}(\Delta)
=
\sqrt{
\frac34
\sum_{b=1}^4
(\Delta_{12,-b}-\bar\Delta_{12})^2
},
$$

$$
\bar\Delta_8
=
\frac16\sum_{a<b}\Delta_{8,ab},
$$

and

$$
\boxed{
E_\Delta
=
\max
\left\{
|\Delta_{16}-\bar\Delta_8|,
\;
1.96\,SE_{MC}(\Delta)
\right\}.
}
$$

This matches the recorded arm-level construction:

$$
SE_{MC}(T16)
=
\sqrt{\frac34\sum_b(T12_{-b}-\bar T12)^2},
$$

$$
E_T
=
\max\{|T16-\bar T8|,\;1.96SE_{MC}\},
$$

with six T8 pair bases and four T12 LOO bases. 

This is exactly what my v2 review required: the existing accepted error functional is no longer referred to generically; it is executable without interpretive discretion.

**Item 3: CURED.**

## 4. C-8 and the `n/(n+1)` inheritance — CURED

The corrected statement now makes the required distinction.

At the raw-integral level,

$$
\widehat I^{L4}_{impl}
-
\widehat I^{0}_{impl}
=
\frac{1}{n+1}
\sum_{t=1}^n
(y^{L4}_t-y^0_t),
$$

provided the deterministic node-0 contribution is identical across arms. Thus the node-0 **numerator** cancels.

But relative to an \(n\)-node average,

$$
\widehat I^{L4}_{impl}
-
\widehat I^{0}_{impl}
=
\frac{n}{n+1}
\left[
\frac1n\sum_t(y^{L4}_t-y^0_t)
\right].
$$

The normalization defect therefore remains, with the correctly stated basis-specific factors

$$
\frac{1600}{1601},\qquad
\frac{1200}{1201},\qquad
\frac{800}{801}.
$$

The underlying Stage-A source confirms that node 0 is included in every averaged sub-basis and that the implemented estimator divides by \(n+1\), rather than \(n\). 

v3 also keeps the correct operational consequence: LOC4 inherits the estimator of record; it does not rescale or repair it; an upstream estimator repair requires LOC4 to be rerun.

**Item 4: CURED.**

## 5. G-L4-8 curvature/rank gate — CURED

This correction is now substantive rather than cosmetic.

G-L4-8 no longer asks merely for correlations between \(\delta_{occ}\) and \(\beta_{occ}\). It requires those diagnostics to be read jointly with actual local-identification evidence for the extended block:

$$
\lambda_{\min}(H_{\beta^{Occ},\delta}),
\qquad
\operatorname{rank}(H_{\beta^{Occ},\delta}),
\qquad
\kappa(H_{\beta^{Occ},\delta}),
$$

plus Cholesky success and bound status.

More importantly, failure is genuinely blocking. A near-singular block yields:

* no paper-facing LOC4 level;
* no paper-facing LOC4 difference;
* no materiality verdict;
* no discharge of the mandatory LOC4 robustness;
* return rather than an ad hoc pin/drop/reparameterization. 

That is exactly the consequence my v2 review required.

OL-12 does **not** make this correction defective. It transparently recognizes that the inherited numerical tier boundaries still have to be transcribed before execution rather than invented. That is proper fail-closed implementation.

**Item 5: CURED.**

## 6. Exact `δ_occ` bound — CURED

The discretion in v2 has been removed.

v3 freezes

$$
B
=
\left\lceil
\texttt{log\_range\_L}
\right\rceil
=
\left\lceil
3.9609003763945605
\right\rceil
=
4,
$$

so

$$
\delta_{occ,k}\in[-4,4],\qquad k=2,3,4.
$$

The slack is itself deterministic:

$$
4-3.9609003763945605.
$$

No run-time choice, “reasonable slack,” \(\sigma\)-dependent rule, or data-dependent tuning survives. The source record confirms the frozen `log_range_L = 3.9609003763945605`. 

For purposes of my mandated correction—which was to freeze an exact number or exact deterministic formula including the slack—this satisfies the requirement.

**Item 6: CURED.**

## A1 disclosure 1 — CURED

The wording now correctly says that adding standalone arm bands discards the CRN covariance information and **generally**, rather than universally, overstates uncertainty under the intended positively correlated paired design.

It also correctly says that the deputy prohibition on summing arm bands does not depend on proving the sign of that error in every possible realization. 

That resolves the overstatement I identified.

**A1 disclosure 1: CURED.**

## A1 disclosure 2 — NOT CURED, wording only

The **operational treatment** is right:

* a box move destroys full pairing on the defensive quarter;
* the run is labelled partial-CRN/diagnostic;
* it cannot be represented as the designed fully paired precision experiment;
* no autonomous materiality verdict is taken from it.

That is consistent with the requested disclosure.

One sentence, however, should not survive:

> “A partial-CRN run does not estimate the quantity the full-CRN design defines.”

That confuses the **estimand** with the **Monte-Carlo coupling**.

Loss of CRN pairing changes

$$
\operatorname{Cov}
(\widehat T_{L4},\widehat T_0)
$$

and therefore the variance/precision of their difference. It does not, by itself, change the target functional

$$
T_{L4}-T_0,
$$

provided the two arms remain valid, supported and estimand-comparable. What has ceased to be the same is the **fully paired precision experiment**, not necessarily the economic/statistical quantity being targeted.

The clean wording is:

> “A partial-CRN run may target the same LOC4-minus-baseline functional difference, but it does not implement the pre-registered fully paired precision experiment: the defensive quarter loses CRN covariance cancellation, so its resulting band is not the designed full-CRN difference band.”

The diagnostic/return consequence can remain exactly as v3 states.

**A1 disclosure 2: NOT CURED only for that estimand-versus-coupling sentence.**

# Final ruling

The substantive v2 repair is nearly complete. There is no remaining defect in the R-a scale convention, direct difference estimator, C-8 inheritance, extended-block identification gate, or frozen \(\delta_{occ}\) bound.

The remaining blocking correction is narrow but consequential:

1. **M-5 must use the recorded sign/order replicate family: `T16` plus the four `T12_-b` LOO bases, not the six T8 pair bases.** The record explicitly reserves T8 for the \(E_T\)/\(E_\Delta\) bias-style term while sign/order stability is checked against every T12 LOO.  
2. Propagate that deletion of T8 from M-5 through §§3.7 and 4.1–4.5/C-9/C-15/output discipline. **Do not remove T8 from the \(E_\Delta\) formula.**
3. In the partial-CRN disclosure, replace “does not estimate the quantity” with the narrower and correct statement that it does not implement the same **fully paired precision experiment**.

No other correction is required by this re-review.

**OVERALL: REJECT — narrowly.** Once those two textual/operational points are corrected, the six-mandate package would otherwise satisfy my v2 return.
