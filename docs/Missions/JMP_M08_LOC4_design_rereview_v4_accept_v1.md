# MICRO RE-REVIEW — JMP-M08 LOC4 DESIGN v4

Scope is bounded strictly to the three residual corrections from my v3 re-review. Everything else is closed and is not re-opened.

I reviewed `JMP_M08_LOC4_robustness_design_v4.md` only for:

1. the M-5 replicate family;
2. propagation of that correction through the specified downstream locations;
3. replacement of the partial-CRN sentence with the exact requested wording. 

## 1. M-5 replicate family: T16 + four T12 only; T8 retained in \(E_\Delta\)

**VERDICT: CURED.**

v4 now defines the M-5 universe exactly as required:

$$
\{T16,\;T12_{-1},T12_{-2},T12_{-3},T12_{-4}\}.
$$

Section 3.5.4 explicitly states:

> “The M-5 replicate universe is the full basis `T16` plus the four leave-one-superblock-out replicates `T12_-b` … The six `T8_ab` bases are NOT part of M-5.”

This directly cures the residual defect from v3. The justification is also now correct: the choice is based on transcription of the recorded sign/order instrument—“signs and ordering identical between `T16` and every `T12` LOO”—rather than on a newly constructed strictness criterion. 

Equally important, v4 does **not** mistakenly remove T8 from the numerical difference-error estimator. Section 3.2.2 continues to define

$$
\bar\Delta_8
=
\frac16\sum_{a<b}\Delta_{T8,ab},
$$

and

$$
E_\Delta
=
\max
\left\{
|\Delta_{T16}-\bar\Delta_8|,
\;
1.96\,SE_{MC}(\Delta)
\right\}.
$$

v4 explicitly says that the six `T8_ab` bases retain “exactly this role” inside \(E_\Delta\), while being excluded from M-5. That separation is now correct.

**Item 1: CURED.**

---

## 2. Propagation through §3.7 / §4 / C-9 / C-15 / Output Discipline

**VERDICT: CURED.**

The deletion of T8 from M-5 has been propagated consistently through every location specified in my prior ruling.

### §3.5.5

The verdict rule now operates over the four T12 replicates only:

$$
I\text{ MATERIAL}
\iff
I_{T16}=1
\quad\text{and}\quad
I_b=1
\;\forall b\in\{T12_{-1},\ldots,T12_{-4}\},
$$

with the analogous universal-zero condition for IMMATERIAL and disagreement giving INDETERMINATE_MC. 

### §3.7

The M-5 reporting table is now explicitly

$$
\{S_A,S_B,O_{AB}\}
\times
\{T16,T12_{-1},T12_{-2},T12_{-3},T12_{-4}\}.
$$

No T8 basis remains in the M-5 reporting universe.

### §4.1

The decision rule now explicitly says M-5 is classified over `T16` and the four `T12_-b`. It also prohibits both adding `T8_ab` and dropping a `T12_-b`, which correctly freezes the recorded replicate family.

### §4.3 — IMMATERIAL

The branch now requires

> `S_A = S_B = O_AB = 0` in `T16` and in every one of the four `T12_-b`.

Correct.

### §4.4 — MATERIAL

The branch now requires that a full-basis sign/order change also be exhibited by **every one of the four T12 replicates**.

Correct.

### §4.5 — INDETERMINATE_MC

The branch now identifies disagreement among the four T12 replicates, or between them and T16, as the M-5 indeterminacy condition. T8 is no longer mentioned.

Correct.

### C-9

The interpretation of “immaterial” for \(\phi_A,\phi_B\) now says the arm-to-arm qualitative configuration must be identical in `T16` and all four T12 LOO replicates.

Correct.

### C-15

The coherence discussion has also been repaired. It now explicitly distinguishes:

* the M-5 family: `T16` + four `T12_-b`;
* the \(E_\Delta\) basis usage: six `T8_ab` remain in the bias-type term.

It correctly states that these are two separate instruments and should not be forced into an identical basis family merely for symmetry.

### Output Discipline

The closing control section correctly records both:

* T8 removed from M-5;
* T8 retained untouched inside \(E_\Delta\).

The final return condition likewise refers to M-5 over `T16` plus the four T12 replicates only.

I find no surviving T8-based M-5 requirement in the requested propagation locations.

**Item 2: CURED.**

---

## 3. Partial-CRN sentence

**VERDICT: CURED.**

The prior problematic sentence has been replaced with the exact wording I required:

> “A partial-CRN run may target the same LOC4-minus-baseline functional difference, but it does not implement the pre-registered fully paired precision experiment: the defensive quarter loses CRN covariance cancellation, so its resulting band is not the designed full-CRN difference band.”

That wording makes the correct distinction:

$$
\text{economic/statistical target}
\quad\neq\quad
\text{Monte-Carlo coupling used to estimate it}.
$$

A loss of full CRN pairing can change the variance and precision properties of the estimator without necessarily changing the target functional

$$
T_{LOC4}-T_{BASE}.
$$

The diagnostic/return consequence remains unchanged, which is also correct under the previously accepted design.

**Item 3: CURED.**

---

# Final ruling

| Residual correction                                                    | Verdict   |
| ---------------------------------------------------------------------- | --------- |
| M-5 = `T16` + four `T12_-b`; no T8 in M-5; T8 retained in \(E_\Delta\) | **CURED** |
| Propagation through §3.7 / §4 / C-9 / C-15 / Output Discipline         | **CURED** |
| Partial-CRN sentence replaced with exact requested wording             | **CURED** |

No residual defect remains within the scope of this micro re-review.

This ruling does **not** reopen any previously closed element of the design, including R-a, the direct-difference instrument, the arm-precision rider, the transcribed \(E_\Delta\) estimator, corrected C-8, G-L4-8, the frozen \(\delta_{occ}\) bound, Path-B reconciliation, or the estimation architecture.

**OVERALL VERDICT: ACCEPT.**

`JMP_M08_LOC4_robustness_design_v4.md` satisfies the three residual corrections and may proceed to freeze, subject only to the already-recorded blocking open items that are outside the scope of this review. 
