# JMP-M05 Deputy Programme Acceptance v1

**Mission:** JMP-M05 — Household-Clustered Inference, design stage  
**Decision-maker:** ChatGPT JMP Deputy Programme Director  
**Date:** 2026-07-31  
**Verdict:** ACCEPTED SUBJECT TO ONE MECHANICAL v4 CLOSURE

## 1. Strategic verdict

The JMP-M05 design stage is substantively complete.

The verified source contract, design v3, independent methods review, targeted
recheck, micro-recheck, mission ledger v3, and Goal 1 manager acceptance packet
support acceptance of the Phase-5 inference design.

No model, estimand, baseline, or likelihood-specification change is required.
The micro-recheck residual is procedural and numerical-annotation-only. It does
not reopen the methods design and does not count as a third substantive
remediation cycle.

## 2. Accepted dependencies

Numerical application anchor:

`982c52217031158c4a2368709d4a6b211ebcde76`

Phase-4 execution ancestor:

`fee60723ed27d6979976a3dc85b09cde3096e011`

Nested dclaborsupply HEAD and MNL gitlink:

`27756a06ea189339aa82915ed2124628afed20eb`

Accepted Phase-3 bundle:

`2cf237648743f59bd742b12feceaea67c5fd377b26faf4fb6fad6f452f86864b`

Accepted Phase-4 bundle:

`5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`

The source audit established that the accepted MNL checkpoint is a descendant
of the Phase-4 execution revision and that the accepted bundles rehash exactly.

## 3. Frozen decisions D-1 through D-8

### D-1 — Finite-sample correction

Freeze the two-factor HC1/CR1-style regression-analogue convention:

\[
N=G=1555,\qquad K=35,\qquad
c=\frac{G}{G-1}\frac{N-1}{N-K}
 =\frac{1555}{1520}
 =1.0230263157894737.
\]

This is a pre-registered convention for the nonlinear sandwich, not an exact
unbiasedness theorem. The uncorrected CR0 object must remain available in the
diagnostics or derivable from the stored meat and bread.

### D-2 — Active-bound treatment

Freeze the conditional 35-dimensional restricted pseudo-true QMLE covariance:

- `beta_l_age2_sm` and `beta_l_age2_sf` are treated as active upper-bound
  equality restrictions;
- bread is the inverse of the name-selected `H_II`, not a Schur complement;
- meat uses the corresponding 35 score columns;
- the two active-bound coordinates receive literal `NA` for symmetric standard
  errors, z-statistics, p-values, and Wald intervals;
- T-22 is sample numerical KKT evidence, not proof of population strict
  activity;
- reported inference is conditional on the active set;
- no robust-covariance Loewner ordering is claimed.

Freeze the two-tier downstream trigger:

1. material loading requires disclosure and consideration of sensitivity;
2. boundary-aware or resampling inference is required only for inference on the
   bound coordinate, an unconditional active-set claim, or a functional for
   which strict activity is not defensible.

### D-3 — Score artifact contract

Freeze:

- authoritative score artifact: float64 C-contiguous `.npy`, shape `1555×37`;
- canonical row-index and column-index artifacts;
- committed summary/fingerprint artifacts;
- non-authoritative `%.17g` CSV rendering;
- mandatory SHA-256, size, shape, dtype, layout, row fingerprint, column
  fingerprint, disclosure class, and retention responsibility;
- T-23 custody/completeness gate.

Operational route pending explicit licence clearance: **restricted custody**.
The household-level `.npy` and row-level rendering must not be committed or
pushed to a public/shared Git repository. They must be durably retained in an
access-controlled immutable store. Non-disclosive summaries, metadata, and
fingerprints may be committed.

This is a conservative project-governance determination, not a legal opinion.
A later documented licence clearance may supersede the route without changing
the statistical design.

### D-4 — Fixed-pin reporting

Freeze:

- status `pinned`;
- literal `NA` in the five inferential fields;
- no pin described as a normalisation;
- distinguish the two verified structural-inapplicability mechanisms;
- include the mandatory reporting footnote.

### D-5 — Regional/access protocol

Freeze:

- H0-A: ten-degree-of-freedom confirmatory omnibus;
- H0-B: seven NUTS-1 intercept shifts;
- H0-C: two urbanisation shifts;
- H0-G: one `gsur` coefficient;
- name-keyed `E_R`/`A` restriction algebra;
- separate model-based and robust Wald statistics and p-values;
- H0-A carries the confirmatory block claim.

These tests concern the regional/urbanisation/GSUR access block, not the whole
opportunity mechanism and not the final welfare decomposition.

### D-6 — Gates and tolerances

Freeze T-1 through T-23 and the warning tier after the authorized v4 correction.

For T-7 use:

\[
\gamma_G=\frac{G u}{1-G u},\qquad
\kappa_{BE}=K\gamma_G,\qquad
\kappa_{BE,\mathrm{certified}}=6.0424\times10^{-12},
\]

with `K=35`, `G=1555`, and `u=2^-53`.

The certified constant is upward-rounded and remains approximately 16.55 times
tighter than the `1e-10` rank convention.

### D-7 — Canonical row order

Freeze `idhh`-ascending stable argsort.

This is equal to the verified loader order for the accepted sample and is
required for deterministic hashes.

### D-8 — K/covariance linkage

Freeze the linkage:

- the accepted conditional covariance uses `K=35`;
- any later strategic decision to use an unrestricted 37-dimensional
  covariance must change `K` to 37 in the same approved design revision.

No such change is currently authorized.

## 4. Ratified task-plan supersessions

Ratify:

1. S-10 is replaced by the two-tier downstream boundary trigger in D-2. This
   governs JMP-M08/JMP-M09 and the condition for revisiting X-005.
2. Unsupported claims that the chosen correction is necessarily conservative
   or universally expected by referees are removed.
3. T-7's earlier generic relative tolerance is superseded by the quantified
   backward-error certification.
4. The average-negLL/`ln(101)` diagnostic is not an objective-bound argument and
   must not appear in paper-facing interpretation.
5. The regional block is not the complete opportunity mechanism.

## 5. Micro-recheck disposition

Ratify R-15a: the six front-matter changes between design v2 and v3 are
version-identity metadata required by the v3 instruction. They do not constitute
a design change.

Authorize one E0 closure producing design v4:

1. replace the inaccurate relative-change annotation `1.8e-5` with
   approximately `1.85e-6` (exact ratio approximately
   `1.8516646205e-6`);
2. replace the inconsistent no-weakening wording with exactly:

   `T-7 is minimally loosened only to implement the valid upward-rounded certification, while remaining 16.55× tighter than the rank convention.`

3. admit the six version-only front-matter lines;
4. make no other substantive or numerical change.

The independent reviewer must create a new micro-recheck v2 rather than editing
the historical v1. Its verdict must be `MICRO-RECHECK PASS`.

## 6. Documentation checkpoints

After v4 and micro-recheck v2 pass, authorize:

1. one MNL documentation-only commit containing the complete Phase-5
   source/design/review evidence set;
2. one `Job_Market_paper` documentation-only commit containing the mission
   instruments, ledger v3, PI disclosure determination, Goal 1 acceptance, and
   this deputy acceptance.

The numerical application anchor remains `982c522...`; the resulting MNL HEAD is
a later documentation checkpoint and must be recorded separately.

## 7. Next mission

Authorize creation and execution of the design-to-dry-run mission:

`JMP-M05B — Phase-5 Inference Implementation and Certification`

Delegated scope:

- implementation;
- non-numerical and fixture tests;
- independent code review;
- narrow remediation;
- exact-state commit;
- one full real-data dry run;
- dry-run artifact audit.

Not authorized:

- production `complete/` execution;
- accepted inference claims;
- welfare, decomposition, synthetic recovery, EUROMOD, notebooks, couples, or
  pooled years;
- upstream package changes without a separate PKG mission.

Return to the deputy programme director only after a review-approved committed
implementation and successful audited dry run, or on an E2 halt.
