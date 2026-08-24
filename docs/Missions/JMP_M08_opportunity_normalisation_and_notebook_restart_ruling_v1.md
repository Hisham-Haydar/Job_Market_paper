# JMP-M08 Deputy Ruling — Opportunity Normalisation and Notebook Restart v1

**Programme:** Goal 1 — Empirical JMP  
**Decision-maker:** Deputy Programme Director  
**Date:** 2026-08-18  
**Status:** Binding  
**M08 disposition:** Remains open; numerical welfare execution remains halted  
**Estimation disposition:** Accepted estimate and inference remain unchanged  
**Notebook disposition:** `fr_singles_pipeline_v2.ipynb` remains frozen

## 1. Decision

Adopt the manager-recommended normalisation remedy.

For every household \(i\), coalition \(S\), S-10 scenario \(r\), and
measure/reference opportunity object used by M08, interpret the implemented
positive opportunity kernel \(\widetilde g_{i}^{S,r}\) as an **unnormalised
kernel**, not as the welfare-layer probability density.

Define the welfare-layer opportunity probability measure by

\[
Z_i^{S,r}
=
\int_{\mathcal J_i}
\widetilde g_i^{S,r}(j)\,d\mu(j),
\qquad
\widehat g_i^{S,r}(j)
=
\frac{\widetilde g_i^{S,r}(j)}{Z_i^{S,r}},
\]

where \(\mu\) is the exact mixed base measure of the accepted model: the
non-employment atom together with the accepted discrete/continuous employed-job
support.

The welfare attained-utility core uses

\[
\log \widehat g_i^{S,r}(j)
=
\log \widetilde g_i^{S,r}(j)-\log Z_i^{S,r}.
\]

This normalisation is mandatory for:

- the baseline opportunity object;
- all eight access/ability/preference coalitions;
- both active decomposition measures;
- all six welfare-family measures wherever an opportunity object enters;
- all four S-10 scenarios;
- every attained and reference-side evaluation;
- the direct-redraw validation estimator.

## 2. Economic and econometric classification

This is a **welfare-layer fidelity correction and scale convention**, not a
re-estimation and not a change to the identified choice model.

For a fixed household and coalition, \(-\log Z_i^{S,r}\) is common to all
alternatives. It therefore cancels from conditional choice probabilities and
does not change:

- the accepted likelihood;
- the accepted parameter vector;
- the accepted Hessian or covariance;
- fitted choice probabilities;
- the access/ability/preference slot assignments;
- the relative odds of work versus non-work or of one job package versus
  another.

It does change welfare levels, necessarily, because the unnormalised kernel
adds an unidentified household- and coalition-specific constant to the
inclusive value.

The implemented object must therefore be described precisely:

- \(\widetilde g\): positive opportunity kernel / unnormalised opportunity
  measure;
- \(\widehat g\): normalised opportunity probability density or mass-density
  used in welfare integration.

Do not continue calling \(\widetilde g\) itself a probability density.

## 3. Domain and calculation of the normalising constant

### 3.1 Analytic support, not sampled-node support

Compute \(Z_i^{S,r}\) over the model's analytic latent-job support.

Do **not** define \(Z_i^{S,r}\) as a sum over the sampled 101/201/401 proposal
nodes. A draw-dependent normalisation would make welfare levels depend on the
proposal realisation and draw count.

Use the audited closed-form factor integrals, including:

- the non-employment atom;
- the employment/participation factor;
- interval widths in the hours factor;
- the full discrete occupation support;
- the normalised wage density;
- every coalition-specific argument substitution.

Persist the component masses and the total \(Z_i^{S,r}\) so the construction is
auditable.

### 3.2 Operator order

For each coalition:

1. apply the frozen access, ability, and preference argument substitutions to
   the accepted kernel;
2. form the complete coalition kernel \(\widetilde g_i^{S,r}\);
3. compute \(Z_i^{S,r}\);
4. normalise once;
5. evaluate welfare.

Normalisation is not a fourth decomposition channel and receives no Shapley
contribution.

## 4. Required normalisation validation

Before resuming proposal remediation or EUROMOD pricing, the application path
must pass all of the following.

### N1 — positivity and finiteness

For every relevant household, coalition, scenario, and reference object:

\[
0 < Z_i^{S,r} < \infty.
\]

No non-finite kernel value or normalising constant is permitted.

### N2 — unit mass

Analytic integration of \(\widehat g_i^{S,r}\) equals one to absolute tolerance
\(10^{-12}\).

### N3 — independent integration check

An independent numerical/quadrature reconstruction agrees with the analytic
\(Z_i^{S,r}\) to absolute or relative tolerance \(10^{-10}\).

### N4 — conditional-likelihood invariance

Choice probabilities and the accepted conditional log-likelihood computed with
\(\widetilde g\) and with \(\widehat g\) agree to \(10^{-12}\), apart from the
analytically cancelling household-common constant.

### N5 — scale invariance

Multiplying any household-coalition kernel by an arbitrary positive scalar
changes neither \(\widehat g\) nor the resulting welfare attained utility,
within \(10^{-12}\).

This is the direct test that the unidentified kernel scale has been removed.

### N6 — proposal-estimator identity

The primary estimator uses the exact term

\[
\log \widetilde g_i^{S,r}(j)
-
\log Z_i^{S,r}
-
\log q_i^W(j).
\]

No code path may mix:

- unnormalised \(\widetilde g\) with a sampler from \(\widehat g\);
- the old proposal correction with draws from \(q^W\);
- baseline \(Z_i\) with a counterfactual coalition kernel.

### N7 — direct-sampler identity

Every coalition direct sampler draws from the exact
\(\widehat g_i^{S,r}\) that appears in the corresponding IS integrand.

Analytic moments/category probabilities and simulated frequencies must agree
under the already frozen sampler-validation rules.

### N8 — reference consistency

Attained and reference-side evaluations use the same normalisation convention.
No measure may compare a normalised attained object with an unnormalised
reference object, or vice versa.

### N9 — coalition commutation

After coalition operators are applied and the resulting kernel is normalised,
all permitted operator orders produce the same \(\widehat g_i^{S,r}\) within
the frozen commutation tolerance.

## 5. Consequences for the prior integration evidence

The old direct-versus-IS discrepancy is not interpreted as proposal-tail
evidence because the two estimators targeted different quantities.

Preserve it as diagnostic history, with the corrected interpretation:

- the level gap was generated primarily by the omitted \(-\log Z_i^S\);
- it does not certify or reject the old proposal after the estimands are aligned.

The old-proposal draw-growth evidence remains relevant. The manager reports that
even after removing the normalising-constant level shift, the 2x and 4x
adjacent-step drifts remain above the frozen 0.05-nat gate. Therefore the
variance problem remains live.

Before new pricing:

1. recompute the complete existing 1x/2x/4x battery against the normalised
   target, using the already priced bases;
2. record the corrected direct-versus-IS comparison wherever an exact
   \(\widehat g\) sampler is already evaluable;
3. unless the old proposal unexpectedly passes every unchanged promotion gate,
   resume the frozen \(q^W\) defensive-mixture remediation.

No gate is relaxed and no old-\(q\) basis beyond 4x is authorised.

## 6. Resumption of the welfare-proposal remediation

The previously authorised proposal-axis remediation remains binding, amended
only as follows:

- \(q^W\) targets the normalised coalition objects \(\widehat g_i^{S,r}\);
- every proposal density is evaluated relative to the same base measure used in
  \(Z_i^{S,r}\);
- all coalition direct samplers draw from \(\widehat g_i^{S,r}\);
- normalisation tests N1–N9 precede proposal tests and EUROMOD pricing;
- \(\theta\), coalition operators, references, pricing path, S-10 rules, and
  LOC4 sequencing remain unchanged.

No `dclaborsupply` package-source change is authorised. Implement the
normalisation and welfare proposal in the MNL France-application layer. Escalate
if a generic package modification is genuinely unavoidable.

## 7. Contract and specification treatment

Amend the frozen M08 execution contract before execution. The amendment must
include:

- the kernel-versus-density distinction;
- the exact \(Z_i^{S,r}\) formula and component masses;
- tests N1–N9;
- the corrected IS and direct estimands;
- the amended \(q^W\) target;
- the status of the old 1x/2x/4x evidence.

Do not rewrite the full welfare specification during remediation. This ruling
and the amended M08 contract govern the application.

After M08 acceptance, consolidate the correction into
`JMP_welfare_spec_v6.md`, superseding the application-specific claims in v5
that the old proposal was well-conditioned and that the implemented
\(\widetilde g\) could be used directly as a density.

## 8. Notebook restart ruling

### 8.1 The current notebook

Do not edit or rerun production flags in:

`dclaborsupply-monorepo/notebooks/fr_singles_pipeline_v2.ipynb`

It remains frozen because:

- it is part of the accepted P2a construction and parity lineage;
- it embeds the old unnormalised welfare interpretation;
- it is France-application material located in the package repository;
- using it as the remediation workbench would duplicate the production code and
  weaken the evidence boundary.

### 8.2 Exact restart milestone

Notebook work resumes **immediately after M08 is accepted**, identified by the
creation of:

`JMP_M08_goal_manager_acceptance_v1.md`

Do not restart merely after this normalisation ruling, after the normalisation
unit tests, or after the \(q^W\) design. The notebook should document an
accepted end-to-end path, not serve as the debugging environment for that path.

### 8.3 Successor notebook

At M08 closeout create:

`MNL/notebooks/france/fr_singles_pipeline_v3.ipynb`

The v3 notebook is a thin orchestration and exposition layer. It must:

- call accepted production scripts rather than reimplement them;
- load accepted manifests and aggregate reporting maps;
- show P2a sample construction;
- show accepted estimation and inference;
- show the normalised opportunity construction and proposal diagnostics;
- show the six-measure welfare family;
- show the accepted W2/W5 decomposition and fixed-background residual;
- show S-10 sensitivity;
- generate the main paper tables and figures;
- keep all expensive run flags false by default;
- write only to an isolated notebook-development namespace.

LOC4 may proceed in parallel. After LOC4 acceptance, add its comparison to v3.
Create a v4 only if LOC4 changes the preferred specification materially.

## 9. Return conditions

Return to the deputy if:

- an exact analytic \(Z_i^{S,r}\) cannot be defined;
- normalisation changes conditional choice probabilities or the accepted
  likelihood;
- N1–N9 fail;
- a coalition direct sampler cannot target the exact normalised object;
- a package-source change is required;
- the repaired proposal fails both 2x and 4x;
- persistent direct-versus-IS disagreement remains after estimands are aligned;
- accepted structural or normative operators would need to change;
- disclosure cannot be controlled.

No welfare headline, decomposition result, or notebook update is authorised
before these conditions are cleared and M08 is accepted.
