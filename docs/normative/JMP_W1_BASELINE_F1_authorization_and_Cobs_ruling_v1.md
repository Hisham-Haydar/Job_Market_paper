# JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md

**Programme:** JMP Goal 1 — Empirical JMP  
**Date:** 2026-09-11  
**Authority:** Deputy Programme Director ruling, subject to PI final authority  
**Status:** BINDING DESIGN / EXECUTION-GATE RULING

## 1. FORK-1 close-out status

`JMP_W1_fork_ruling_v1.md` is accepted as the Goal 1 implementation record of the Deputy's R1–R6 ruling. Appendix A remains controlling where any conflict exists.

R1 and R2 are adopted.

R3 remains partially open because the deterministic derived-numeral script (REC-1) is not yet closed. P1 concerning the two couples leisure-curvature tables is real but affects Mapping-M sensitivity only; it does not block the Mapping-F baseline.

MEASURE-MAP-1 is not accepted. MEASURE-MAP-1R remains the active scientific correspondence gate.

## 2. E1 — BASELINE-F-1

### Ruling

**AUTHORIZED IN PRINCIPLE, BUT FULL-SAMPLE EXECUTION REMAINS LOCKED UNTIL MEASURE-MAP-1R IS ACCEPTED.**

Reason: R4 explicitly requires the measure-correspondence audit to close before any new welfare execution. BASELINE-F-1 is a new welfare computation even though it is closed-form and contains no simulation.

Before MEASURE-MAP-1R acceptance, Goal 1 may prepare the implementation, tests, output schema, and the small deterministic checks already permitted by R4. It may not compute the full singles/couples distribution.

Upon MEASURE-MAP-1R acceptance, BASELINE-F-1 is automatically unlocked without another Deputy round-trip provided E2 below is resolved by the audit and no literal-correspondence conflict remains.

### Authorized object

For every household/individual in the accepted singles and couples estimation samples,

\[
W_{i,F}^{1,\mathrm{obs}}
=
C_i^{\mathrm{obs}}
\exp\!\left[
\frac{L_i(j_i^{\mathrm{obs}})-L_i(o)}
{\beta_c}
\right].
\]

This is literal Mapping-F Measure 1 at the observed attained bundle on the current empirical domain and coincides there with the staying-home equivalent Measure 4. This is not a general theoretical identity \(W^1=W^4\).

The baseline calculation uses only:

- \(C_i^{\mathrm{obs}}\);
- \(L_i(j_i^{\mathrm{obs}})\);
- \(L_i(o)\);
- \(\beta_c\).

It must have no dependence on:

- opportunity density \(g\);
- numerical proposal \(q\);
- behavioural shock \(\varepsilon\);
- latent-job intensity \(\kappa\);
- priced home consumption \(C_i(o)\).

The 119-couple neither-work pricing-floor issue does not enter this observed-bundle Mapping-F baseline.

### Pre-registered checks

1. For observed nonworkers \(j_i^{\mathrm{obs}}=o\),
   \[
   W_{i,F}^{1,\mathrm{obs}} = C_i^{\mathrm{obs}}.
   \]

2. For observed workers, verify the model-implied domain condition
   \[
   0 < W_{i,F}^{1,\mathrm{obs}}/C_i^{\mathrm{obs}} < 1.
   \]
   A violation is a scientific diagnostic to be explained; it must not be silently clipped or repaired.

3. Dependency test: the baseline function/API must accept no \(g,q,\varepsilon,\kappa\) input and must not read them indirectly.

4. Reproduce the deterministic household examples used by the accepted MEASURE-MAP-1R.

5. Verify the indifference identity implied by the accepted systematic utility:
   \[
   u_i(W_{i,F}^{1,\mathrm{obs}},o)
   =
   u_i(C_i^{\mathrm{obs}},j_i^{\mathrm{obs}}).
   \]

6. Report only descriptive baseline distribution/inequality outputs already authorized by the current reporting schema. No counterfactual, Shapley/Owen decomposition, P/A/B/D share, or causal interpretation is authorized.

### Data/output discipline

Household-level welfare values may be computed only in the existing restricted empirical environment. They must not be committed to Git. Paper-facing repository artifacts should contain aggregate/descriptive outputs only.

## 3. E2 — consumption argument

### Ruling

**CONFIRMED.**

For BASELINE-F-1, \(C_i^{\mathrm{obs}}\) is not a free normative reference choice. It must be the exact consumption/resource argument entering the accepted estimated systematic utility at household \(i\)'s observed labour state.

Therefore:

- if the estimated utility uses raw EUROMOD disposable household income as \(C\), use that object;
- if the estimated utility uses an equivalized or otherwise transformed consumption resource as its economic \(C\) argument, use that same object;
- do not substitute the neither-work priced amount;
- do not substitute a different post-estimation welfare income concept;
- do not switch between raw and equivalized units for presentation without separately documenting the transformation and its consequences.

The MEASURE-MAP-1R must identify the exact source column, preprocessing/equivalization rule, units, and utility call path. That empirical provenance closes E2 operationally.

If MEASURE-MAP-1R finds that the executed estimation utility and the proposed \(C_i^{\mathrm{obs}}\) source do not coincide, BASELINE-F-1 remains blocked and the discrepancy returns to the Deputy.

## 4. Sequencing

1. Continue REC-1 and P1 provenance closure in parallel.
2. Complete and independently accept MEASURE-MAP-1R.
3. On acceptance and E2 provenance closure, execute BASELINE-F-1.
4. Independently verify the baseline implementation and descriptive outputs.
5. Only after MEASURE-MAP-1R acceptance may Goal 1 begin R5, `JMP_counterfactual_attainment_design_v1.md`.
6. No counterfactual welfare or decomposition execution is authorized by this ruling.

## 5. Seminar status

If BASELINE-F-1 is executed and independently checked in time, its literal observed-bundle Mapping-F distribution may be shown under R6 as a descriptive baseline.

Old W1-EA welfare/decomposition magnitudes remain retired and must not be presented as Haydar–Maniquet Measure 1 results.
