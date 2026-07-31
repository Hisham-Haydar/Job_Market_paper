# JMP-M05 Task Plan v1 — Household-Clustered Inference (Design Stage)

**Mission ID:** JMP-M05 — Household-Clustered Inference
**Stage:** Design-only task planning (no statistical design, no implementation)
**Workstream:** Claude Project 1 — JMP paper and empirical design
**Date:** 2026-07-30
**Target repository path:** `docs/missions/JMP_M05_task_plan_v1.md`
**Commit status:** NOT COMMITTED — awaiting manager review

---

## 1. Plan verdict

**READY WITH SOURCE GAPS**

The mission is well-posed, internally consistent, and can proceed to the design
memo. The governance set supplied is sufficient to fix the mission
interpretation, the derivation programme, the decision structure, and the gate
architecture. It is **not** sufficient to close the design memo, because six
classes of repository fact required by the pre-registered gates were not
supplied and cannot be inferred without inventing paths or semantics:

| Gap | Required for |
| --- | --- |
| G-A: exact parameter-map / free-vector ordering source | active-bound indexing, regional indexing, all reporting |
| G-B: exact JAX likelihood module and the additive composition of the household log-likelihood term | score derivation, cluster contract |
| G-C: bounds configuration (which bound is active, bound values) | active-bound treatment, KKT sign check |
| G-D: weighting status of the accepted objective (survey weights in/out; sum vs mean) | sample scaling, meat construction, finite-sample correction |
| G-E: cluster-identifier source and its alignment with loader group order | cluster-count gate, row alignment |
| G-F: exact Phase-4 bundle filenames (only `hessian_free.npy` is named in evidence) | immutable bread provenance |

The design memo may be **drafted** on the derivational and decision-analytic
axes immediately (Tasks S-1 to S-9 below are source-independent in structure),
but it may not be **finalized or submitted** until G-A to G-F are closed by
verified repository evidence. Every unresolved path in this plan is marked
`UNKNOWN`; none has been invented.

One further item requires a manager ruling before the memo is submitted, not
because the sources conflict substantively but because two different revisions
are both described as canonical starting points: see V-1 in §4.

---

## 2. Mission interpretation

### 2.1 What this mission is

JMP-M05 design stage produces **one** artifact: a statistical contract
specifying how uncertainty will be computed, corrected, tested, reported, and
stored for the already-accepted France 2016 singles P2a region-live estimate.
It is a **contract-writing mission**, not a statistical-computation mission. The
accepted point estimate, the accepted Hessian, and the accepted bundles are
treated as immutable inputs.

### 2.2 What this mission unlocks

Per the charter §2 and the roadmap §2, no parameter standard error, no
regional-block significance statement, no later welfare uncertainty, and no
decomposition uncertainty is admissible in the manuscript until this contract
exists and is certified. The mission is therefore on the critical path to
JMP-M06 (synthetic recovery) only in the sense of ordering; it does **not**
substitute for it (D-009, Phase-4 acceptance §16).

### 2.3 Economic reading of the mission

The paper's headline claim (canonical state §2, D-011) is a decomposition of
money-metric well-being inequality into an **opportunity-environment**
component and a **preference** component. Inference matters asymmetrically
across the parameter vector:

- the ten regional/access parameters (`beta_E_gsur`, `beta_E_drgn2..8`,
  `beta_E_drgur`, `beta_E_drgmd`) carry the empirical content of the claim that
  the opportunity environment is heterogeneous. If the joint restriction "no
  regional heterogeneity in the opportunity index" cannot be rejected, the
  headline decomposition's opportunity component rests on the wage/ability and
  occupation channels alone, and the paper's framing must change. This is the
  single most consequential inferential statement in the mission.
- the preference block carries the content of the absorption claim (JMP-M07),
  but only comparatively, against the comparison model. Phase-5 precision on
  preference parameters is necessary bookkeeping, not the test.
- two preference parameters (`beta_l_age2_sm`, `beta_l_age2_sf`) are at active
  bounds. Symmetric Wald inference on them is not available at any tolerance.
  The design must say so in a form that survives into the manuscript.

### 2.4 Interpretive limits fixed by governance

- This is real-data **local** uncertainty at a point estimate. It is not
  identification certification (Phase-4 acceptance §14) and not structural
  recovery (D-009).
- Preferences are not responsibility (D-012). Nothing in the inference layer may
  introduce responsibility language.
- The pooled 47-parameter specification remains the formal certified baseline
  (canonical state §4). P2a inference results do not promote P2a.
- Any statement about occupation-specific wage densities, continuous regional
  labour-market conditions, couples, or pooled years is out of scope
  (X-001 to X-004, canonical state §13).

### 2.5 Non-scope restrictions carried forward verbatim in effect

The design memo must not, and this plan does not: implement code; compute scores
or covariances; run inference; invoke optimizer, gradient, or Hessian; run
synthetic recovery; run welfare, decomposition, EUROMOD, or notebooks; alter the
accepted estimate or artifacts; redesign the RURO specification; broaden into
couples, pooled years, or alternative countries (charter §6). One consequence is
operational and must be stated explicitly in the memo: **the bread may not be
recomputed.** It must be loaded from the accepted Phase-4 bundle under hash
verification, because recomputation would constitute invoking the Hessian.

---

## 3. Authoritative inputs

### 3.1 Supplied and used (verified content in hand)

| Document | Status | Used for |
| --- | --- | --- |
| `JMP_canonical_state_v1.md` | supplied | structure counts, accepted states, authorizations, stale-context list |
| `JMP_decision_log_v1.md` | supplied | D-004 to D-012, X-001 to X-005 |
| `JMP_M05_phase5_inference_mission_charter_v1.md` | supplied | scope, frozen decisions, gates, artifacts |
| `JMP_program_governance_v1.md` | supplied | source hierarchy, mission stages, commit policy |
| `JMP_roadmap_v1.md` | supplied | mission sequence, downstream dependencies |
| `JMP_mission_template_v1.md` | supplied | required controls for the follow-on implementation charter |
| `FR_P2a_region_live_phase3_manager_acceptance_v1.md` | supplied | negLL, bundle hash, pin list, G-15/G-16 bound gates, gradient gate |
| `FR_P2a_region_live_phase4_manager_acceptance_v1.md` | supplied | Hessian construction, regional order, Schur protocol, limits |
| `FR_P2a_region_live_phase4_execution_report_v2.md` | supplied | execution revision, bundle contents |
| `phase4_diagnostics.json` | supplied | free gradient, eigenspectrum, regional free positions, design SVD, solve-vs-pinv precedent |

### 3.2 Required and NOT supplied (must be verified in repository)

| Required input | Path | Status |
| --- | --- | --- |
| Parameter map / `PARAM_NAMES` ordering for the 47-vector and the 37-free projection | UNKNOWN | required, G-A |
| P2a certified specification file (spec hash anchor `492bcfa9…` per Phase-3 acceptance §10) | UNKNOWN | required, G-A |
| JAX negative-log-likelihood module in nested `dclaborsupply` at gitlink `27756a06ea189339aa82915ed2124628afed20eb` | UNKNOWN | required, G-B |
| Production likelihood loader that produced `regional_design_source: production_likelihood_loader_arrays` | UNKNOWN | required, G-B, G-E |
| Optimization bounds block for the 37-free vector | UNKNOWN | required, G-C |
| `theta_estimated.csv` | `outputs/p2a_singles2016/region_live_v1/phase3_estimation_v1/complete/theta_estimated.csv` (named in Phase-3 acceptance §2; directory verified by memo, file existence to be confirmed) | locatable |
| `optimizer_diagnostics.json`, `estimation_results.json`, `phase3_manifest.json`, `phase3_console.log` | same directory as above | locatable |
| Phase-4 `complete/` bundle, eight files | `outputs/p2a_singles2016/region_live_v1/phase4_curvature_v1/complete/` (directory named in execution report; only `hessian_free.npy` named by filename) | partially locatable, G-F |
| Household identifier array in loader order | UNKNOWN | required, G-E |
| Survey-weight variable and its use in the objective | UNKNOWN | required, G-D |
| Governance files as committed | `docs/governance/…` as asserted by the charter | to confirm |

### 3.3 Non-authoritative background explicitly demoted

Prior workstream material on active-bound treatment exists in the project's
historical record — notably an NC-pilot `beta_l0_m` specification review that
enumerated four options (keep bounded and free; fix at bound; relax bound;
respecify the block) and an estimator design contract that mandated float64 JAX
with a projected-gradient/KKT bound-hit diagnostic. Under canonical state §13
and governance §5 this is **reasoning precedent only**. It concerns a different,
superseded state (couples, NC pilot, 35-parameter vector, `beta_l0_m` at a lower
bound) and carries no evidentiary weight for P2a. It may be cited in the design
memo as prior reasoning about the *class* of problem; it may not be cited as
evidence about `beta_l_age2_sm` or `beta_l_age2_sf`.

---

## 4. Source-verification tasks

These are strictly factual retrieval tasks. None involves a statistical
judgement. Each returns either a verified value or `UNKNOWN`. No statistical
task in §5 may be closed while its listed prerequisite is `UNKNOWN`.

**V-1 — Revision reconciliation.** The charter §3 records MNL HEAD
`982c52217031158c4a2368709d4a6b211ebcde76` as the canonical starting state. The
Phase-4 execution report and manager acceptance record the *execution* revision
as MNL HEAD `fee60723ed27d6979976a3dc85b09cde3096e011`, with the acceptance
instructing that the acceptance memo, execution report, and bundle be committed
as one subsequent checkpoint. The two are therefore reconcilable by
construction: `fee60723` is the execution revision, `982c5221` is the
post-acceptance checkpoint. The nested gitlink `27756a06…` is identical in both.
**Task:** confirm by `git log` that `982c5221` is a descendant of `fee60723`
and that the only intervening changes are the acceptance memo, the execution
report, and the bundle. **Outcome required:** both revisions recorded
separately in the design memo, labelled *execution revision* and *canonical
checkpoint revision*. This is **not** a canonical-file conflict and does not
fire the charter §13 halt, provided the descendancy check passes. If it fails,
halt HM-REV (§15).

**V-2 — Parameter map and ordering.** Retrieve the authoritative ordered name
list for the 47-parameter vector and the 37-free projection. Record the source
file path and its committed hash. **This is the single highest-priority
verification task**, because active-bound indexing, regional indexing, the
interior-35 index map, and every reporting table depend on it.

**V-3 — Active-bound identity and direction.** From the bounds configuration and
`theta_estimated.csv`, record for `beta_l_age2_sm` and `beta_l_age2_sf`: the
bound value, whether the active bound is upper or lower, and the sign of the
free-gradient component. Cross-check against the published `gradient_free`
array: exactly two entries exceed `1e-3` in absolute value —
`-0.8445544161794221` at 0-based position 2 and `-1.4682021491125388` at 0-based
position 6 — while the recorded maximum over the 35 non-bound free parameters is
`1.0992597206183063e-4`, which equals the entry at 0-based position 33. The
inference that free positions 2 and 6 are the two bound parameters is therefore
strongly supported but **remains provisional until confirmed by name**. Also
verify KKT consistency: for a minimized negLL, a negative gradient component
implies the objective would fall as the parameter rises, which is consistent
with an **upper** active bound and a non-negative multiplier. If the recorded
bound direction contradicts the gradient sign, halt HM-KKT (§15).

**V-4 — Likelihood composition.** Identify every additive term in the
per-household log-likelihood contribution: the discrete-choice term over the 101
alternatives, and any continuous-density terms (log-wage density, hours-offer
density, occupation-opportunity term, market/region term, prior normalization).
This is not an academic question. The accepted negLL of `19053.46553160093`
over 1,555 households is `12.25` nats per household, far above the
uniform-choice benchmark `ln(101) = 4.615`. A fitted choice-only likelihood
cannot exceed the uniform benchmark. The excess is therefore attributable to
continuous-density terms, weighting, or a term count above 1,555 — and the
design memo cannot define the household score without knowing which.
**Deliverable:** an explicit enumeration of terms with their sign and scaling.

**V-5 — Term count and cluster contract.** Determine the number of additive
log-likelihood terms and whether it equals 1,555. This determines whether
household clustering is **binding** (more than one independent score
contribution per household, so clustering corrects genuine within-household
dependence) or **degenerate** (exactly one score contribution per household, in
which case the household-clustered sandwich is algebraically identical to the
outer-product-of-gradients misspecification-robust sandwich). For a single-year
singles sample, the degenerate case is the natural expectation, and if it holds
the design memo must say so plainly: the 101 alternatives per household are a
row-level implementation concern, not a source of statistical dependence, and
the sandwich is *misspecification-robust*, not *dependence-robust*. The label
used in the manuscript follows from this finding, as does the point at which
clustering begins to bind (couples, X-001; pooled years, X-002).

**V-6 — Weighting and scaling.** Determine whether EU-SILC survey weights enter
the accepted objective; if so, the variable, the normalization, and whether the
objective is a sum or a mean over households. The frozen score identity
`Σ_g s_g = −∇negLL` (charter §8) is consistent only with a matched scaling
convention; the memo must state which convention holds rather than assume the
sum form.

**V-7 — Cluster identifier alignment.** Locate the array supplying `idhh` in the
loader's group order, confirm 1,555 unique values with no missing entries, and
confirm that row *g* of any score matrix corresponds to the same household as
group *g* of the likelihood loader. Record the mechanism that guarantees this
alignment (index array, group-boundary array, or sort key).

**V-8 — Regional covariate definitions.** Confirm the canonical order
`gsur, reg2..reg8, drgur, drgmd` mapped to `beta_E_gsur, beta_E_drgn2..8,
beta_E_drgur, beta_E_drgmd`, at free positions 15–24 (0-based, per
`phase4_diagnostics.json`). Retrieve the definition of each covariate,
specifically: what `gsur` measures, which region is the omitted reference
category, and whether `drgur`/`drgmd` are urbanisation-degree indicators.
Without the omitted-category identity, the joint null in §9 cannot be written
correctly.

**V-9 — Pin classification.** For each of the ten pins — `beta_l0_m`,
`beta_l_age_m`, `beta_l_age2_m`, `beta_l0_f`, `beta_l_age_f`, `beta_l_age2_f`,
`beta_l_nkids_f`, `theta_l_f`, `beta_E_y2015`, `beta_E_y2017` — record the pin
value and classify the reason: structurally inapplicable to a 2016 singles
sample (the couples-side `_m`/`_f` leisure block and the 2015/2017 year effects
appear to fall here), identifying normalization, or numerical convention. The
reporting rule in §8 is category-dependent.

**V-10 — Phase-4 bundle inventory and bread provenance.** Enumerate the eight
files by exact filename, record each hash against the manifest, and confirm the
bundle SHA-256 recomputes to `5484886985aecd28e511719e42f45b85ad0e1755d1f951dbd13a79281d9665f3`
with the manifest excluded from its own hash map. Identify which file is the
authoritative bread source (CSV and `.npy` both exist) and whether they are
bit-identical after load.

**V-11 — Numerical environment.** Confirm that `jax_enable_x64` is set before
any array creation in the accepted pipeline and record the JAX/jaxlib versions,
platform, and thread settings. Float64 is a precondition for the `1e-8` score
identity tolerance; a float32 path cannot meet it.

**V-12 — Governance path confirmation.** Confirm the six governance and mission
files exist at the paths asserted by the charter, or record the actual paths.

---

## 5. Statistical design tasks

Each task states the object to be produced and the verification prerequisite.
These are the derivation and decision tasks the design memo must discharge. None
is executed here.

**S-1 — Notation and index maps.** Define the 47-vector θ, the selection matrix
J (47×37) that maps free coordinates into the full vector with pins constant,
the free vector θ_F = J′θ, the active set A ⊂ {1,…,37} with |A| = 2, and the
interior set I with |I| = 35. Produce the name-keyed index map
47 → 37 → 35 and record where the regional block sits in each. Arithmetically,
removing 0-based free positions 2 and 6 maps regional free positions 15–24 to
interior positions 13–22, but the memo must obtain this **by name**, never by
arithmetic. *Prereq: V-2, V-3.*

**S-2 — Household log-likelihood contribution.** Write ℓ_g(θ_F) as the explicit
sum of its verified components, with the scaling and weighting convention
stated. *Prereq: V-4, V-6.*

**S-3 — Household score.** Define s_g = ∂ℓ_g/∂θ_F ∈ ℝ³⁷ as the gradient of the
**log-likelihood** contribution, not of the negative log-likelihood, and state
that the artifact stores this object. Derive the identity
Σ_g s_g = ∇ℓ = −∇negLL and fix the sign convention once, at this point in the
memo, for the whole document. Show the chain rule through the pin-fixed
reparameterization explicitly, so that no reader can mistake the 37-vector for a
47-vector projection with zeros. *Prereq: S-2.*

**S-4 — Cluster contract.** State the cluster as household `idhh`, the count as
exactly 1,555, and the mapping from likelihood terms to clusters. State whether
clustering is binding or degenerate and, if degenerate, state the algebraic
equivalence to the OPG sandwich and the consequent naming convention for the
manuscript. *Prereq: V-5, V-7.*

**S-5 — Model-based covariance.** Define the bread from the accepted 37×37 negLL
Hessian H, loaded not recomputed, symmetrized as in Phase 4. Define the
model-based covariance for the interior parameters and — this is the substantive
choice, not a formatting one — decide between the **conditional** object
(H_II)⁻¹, which treats the two active-bound coordinates as fixed constants, and
the **marginal** object [H⁻¹]_II, which allows them to vary. §7 argues the
choice. *Prereq: S-1, V-10.*

**S-6 — Robust sandwich.** Define the meat Ω = Σ_g s_{g,I} s_{g,I}′ over
interior coordinates, the sandwich V = c · B⁻¹ Ω B⁻¹ with B the chosen bread and
c the correction scalar, and specify that every inverse-like operation is a
Cholesky or LU solve, never an explicit inverse, following the Phase-4 precedent
in which solve-versus-pinv agreement reached `8.53e-14`. *Prereq: S-3, S-5.*

**S-7 — Correction scalar.** Analysed in §6.

**S-8 — Regional inference protocol.** Analysed in §9.

**S-9 — Reporting contract.** Specify the exact columns of the parameter table:
name, block, estimate, model SE, robust SE, robust/model ratio, z, p, status
flag ∈ {interior, active-bound, pinned}. Specify the permitted-claims and
prohibited-claims list, mirroring the Phase-3 and Phase-4 acceptance style.
Specify that reported precision is local at the accepted estimate and carries no
identification or recovery claim. *Prereq: S-5, S-6, §6–§10.*

**S-10 — Downstream declaration.** State, without executing anything, how the
Phase-5 covariance object will be consumed by JMP-M08 and JMP-M09: delta-method
propagation requires the 35×35 interior covariance; the two active-bound
coordinates enter as fixed, which understates decomposition uncertainty; the ten
pins likewise. Pre-register that if any pinned or bound coordinate enters the
welfare or opportunity index materially, a resampling-based uncertainty
treatment becomes a requirement of a later mission rather than an optional
robustness item (X-005 currently defers the decomposition bootstrap). *Prereq:
V-9, §7, §8.*

---

## 6. Finite-sample correction analysis

### 6.1 The decision

Recommend exactly one baseline from: CR0 (no correction); cluster-only
G/(G−1); or a justified two-factor correction of the form
c = [G/(G−1)] · [(N−1)/(N−K)].

### 6.2 What the design memo must establish

1. **The magnitudes, so that the decision is made with its stakes visible.**
   With G = 1,555: G/(G−1) = 1.000643, i.e. a standard-error inflation of
   0.03%. With N = 1,555 and K = 35, the degrees-of-freedom factor
   (N−1)/(N−K) = 1554/1520 = 1.02237, i.e. 1.11% on standard errors. The
   combined two-factor c = 1.02303 gives 1.15%. No parameter's significance
   verdict can plausibly turn on this choice. The decision is therefore about
   **convention and defensibility**, not about results — and the memo should say
   so rather than implying a substantive stake.
2. **Whether N and G are the same object.** If V-5 returns the degenerate case,
   N = G = 1,555 and the two factors are not two independent corrections: they
   are a cluster factor and a parameter-count factor on the same count. The memo
   must write c in terms of verified quantities and not import a formula whose
   N refers to household×alternative rows. A correction built on N = 157,055
   rows would be indefensible and must be explicitly excluded.
3. **What K counts.** Candidates: 35 (interior free), 37 (all free), 47 (all).
   The defensible choice is the number of coordinates over which the reported
   covariance is defined, which is 35 under the §7 recommendation. The memo must
   state this and note that using 37 changes the factor to 1.02372, a difference
   of 0.07% on standard errors.
4. **The reference distribution.** With G = 1,555 the small-cluster problem does
   not arise; the usual rule-of-thumb threshold is one to two orders of
   magnitude below this count. The memo should fix normal critical values and
   record that t(G−1) would give 1.9613 against 1.9600 at the 5% two-sided
   level, a 0.07% difference, so that no reader supposes the choice was
   overlooked. Wild-cluster-bootstrap machinery is not warranted and should be
   explicitly declined with this reasoning, not silently omitted.
5. **The weighting interaction.** If V-6 returns weighted estimation, the memo
   must state how weights enter the meat and whether the cluster count remains
   the correct G in the correction, since the correction counts clusters and not
   weighted mass.

### 6.3 Working presumption to be confirmed or rejected

The memo should adopt **one** baseline and defend it, not present a menu. The
working presumption is the two-factor correction with K = 35, on the grounds
that it is the convention a labour-economics referee expects, it is
conservative, and its cost is 1.15% on standard errors. The falsification
criterion is pre-registered: if V-5 or V-6 shows that N and G are not the same
count or that weighting makes the row-count interpretation of N ambiguous, the
memo must fall back to the cluster-only factor with the ambiguity documented,
rather than choose a factor whose inputs it cannot define.

---

## 7. Active-bound inference analysis

### 7.1 The problem

`beta_l_age2_sm` and `beta_l_age2_sf` sit at active bounds with free-gradient
components of magnitude 0.845 and 1.468 — three to four orders of magnitude
above the 35-parameter maximum of 1.10e-4. The constraints are strictly, not
marginally, active. Standard maximum-likelihood asymptotics do not deliver an
asymptotically normal, symmetric distribution for a parameter on the boundary of
the admissible set; the limiting object is a projection of a normal onto the
feasible cone. Inverting the full 37×37 Hessian and reporting two symmetric
standard errors alongside 35 others would be exactly the naive treatment the
charter §10 gate prohibits.

### 7.2 What the design memo must establish

1. **A covariance object for the 35 interior parameters, and a justification for
   the conditional-versus-marginal choice.** The two candidates are genuinely
   different objects. (H_II)⁻¹ is the inverse of the interior block of the
   Hessian: the curvature of the profile objective with the bound coordinates
   held at their bounds. [H⁻¹]_II is the interior block of the inverse: the
   marginal covariance allowing the bound coordinates to vary. The second is the
   inappropriate object here, because the bound coordinates *cannot* vary in the
   direction the likelihood wants, and treating them as free inflates the
   interior covariance by attributing to the interior parameters a sampling
   variability that the constraint has removed. The memo should therefore adopt
   the **conditional** object, treating the active set as a set of equality
   restrictions, and must state the condition under which this is asymptotically
   valid: that the constraints are strictly active in the population, so the
   active set is correctly identified with probability approaching one.
2. **An explicit statement that no symmetric Wald interval, z-statistic, or
   p-value is reported for the two bound parameters.** They are reported with
   their estimate, their bound value and direction, the gradient component, and
   a status flag. The memo must specify the flag text.
3. **An explicit statement of what inference for those two parameters *would*
   require.** One-sided or likelihood-ratio-based inference against the
   restricted model requires re-optimization, which the charter forbids in this
   mission. This is a candidate for a later, separately authorized mission and
   must be recorded as such, not left as an unexplained absence.
4. **The economic reading, and its consequence for the paper.** These are
   age-squared terms in the singles leisure block: the curvature of the
   leisure-preference profile in age. Their being at a corner means the estimated
   preference block absorbs age curvature at the constrained extreme. Because
   age-in-leisure is assigned to the preference channel under the project's
   normative bookkeeping, and because the headline decomposition separates
   opportunity from preferences (D-011), the memo must state the direction of the
   concern plainly: a preference block pinned at a corner cannot flexibly absorb
   variation, which bears on the interpretation of any absorption result in
   JMP-M07. This is a caveat to be carried into the manuscript, not a defect to
   be resolved here, and it must not be presented as evidence about the
   specification.
5. **The consequence for downstream uncertainty.** Fixing two coordinates
   understates the uncertainty of any welfare or decomposition functional that
   depends on them. Pre-register this as a known, directional limitation.

### 7.3 Working presumption to be confirmed or rejected

Conditional covariance on the 35 interior coordinates; no symmetric inference on
the two bound coordinates; explicit flags; boundary-aware treatment justified by
the strictly-active-constraint argument and by a narrowly targeted literature
check (§13, L-1). Falsification criterion: if V-3 shows either constraint is only
weakly active — a gradient component of the same order as the 1.10e-4 interior
maximum — the strict-activity argument fails, and the memo must instead treat the
coordinate as interior-but-near-boundary and report the limitation rather than
apply the equality-restriction argument. On the published gradient values this
falsification is very unlikely to trigger.

---

## 8. Fixed-pin reporting analysis

### 8.1 The decision

A representation for the ten pins that, per the charter §10 gate, cannot be
mistaken for estimated certainty.

### 8.2 What the design memo must establish

1. **Category-specific reporting.** The ten pins are not one kind of object.
   From the names, at least two categories appear present: coordinates
   structurally inapplicable to a 2016 singles sample (the couples-side `_m`/`_f`
   leisure coordinates and the `beta_E_y2015` / `beta_E_y2017` year effects), and
   coordinates that function as identifying or curvature normalizations
   (`theta_l_f` is the candidate). The memo must classify all ten from V-9 and
   assign a reporting convention per category. A structurally inapplicable
   coordinate and a normalization pin carry different messages to a referee.
2. **A prohibition, stated as such.** No pin receives a numeric standard error,
   no pin receives a zero standard error, and no pin receives a z-statistic or
   p-value. The table shows the pinned value and the status flag. The memo must
   fix the exact glyph or word used, so that implementation cannot improvise.
3. **Provenance.** Pin values are reported alongside the Phase-3 finding that all
   ten were bitwise unchanged from accepted values through the start vector to
   the final estimate. This is the evidence that pins are conventions rather than
   estimates.
4. **Whether any pin is decomposition-relevant.** If a pinned coordinate enters
   the welfare index or the opportunity index — the year effects enter the
   opportunity/access index by name — then decomposition results will be
   conditional on the pin. The memo declares this and hands the sensitivity
   question to JMP-M08/M09; it does not analyse it.

### 8.3 Working presumption

Pinned coordinates appear in the parameter table with value, category label, and
a non-numeric standard-error field, with a table footnote stating that pins are
imposed restrictions and not estimates. Exclusion from the table altogether is
rejected, because a 47-parameter specification that displays 37 rows invites the
reader to ask which ten are missing and why.

---

## 9. Regional-block inference analysis

### 9.1 Why this is the mission's substantive core

The ten regional/access coordinates are the empirical carrier of the headline
claim that the opportunity environment is heterogeneous. Phase 4 established
that this block is locally identified conditional on the other free
coordinates — Schur-complement rank 10 with minimum eigenvalue 2.2557 — but
identification is not significance. Phase 5 must deliver the significance
statement.

### 9.2 What the design memo must establish

1. **The correct null hypotheses, in economic terms.** At least three
   restrictions, each with its own selection matrix R and degrees of freedom:
   - H0-A: all ten coordinates zero, q = 10 — no opportunity-index heterogeneity
     of any modelled kind.
   - H0-B: the seven NUTS-1 region dummies jointly zero, q = 7 — no across-region
     differences in the opportunity index relative to the omitted reference
     region. **This is the restriction that maps most directly onto the paper's
     "common opportunity environment" counterfactual** and should be designated
     the primary regional test.
   - H0-C: the urbanisation pair (`drgur`, `drgmd`) jointly zero, q = 2.
   `gsur` requires V-8 before it can be assigned to a null; if it is not a
   regional-heterogeneity coordinate it must be excluded from H0-B and its role
   stated separately. The memo must not write a null over the ten coordinates
   without knowing what each measures.
2. **The covariance sub-object and its indexing.** V_RR is the 10×10 block of the
   chosen 35×35 interior covariance, extracted by name. Both model-based and
   robust versions are required.
3. **The statistic and its reference distribution.** W = (Rθ)′(R V R′)⁻¹(Rθ),
   asymptotically χ²(q), computed by Cholesky solve rather than explicit
   inversion. Note for the record that the robust meat has rank at most
   G = 1,555, far above q, so no rank degeneracy arises. The memo should state
   whether the F-form W/q against F(q, G−q) is also reported; with G = 1,555 the
   difference is immaterial and reporting the χ² form alone is defensible if
   stated.
4. **A conditioning caveat, reported not gated.** The regional design's singular
   values decline smoothly from 30.40 to 11.27 and then fall to 7.72 and 1.68.
   The smallest is roughly a factor of five below the next. One linear
   combination of the regional covariates is therefore substantially less well
   supported than the others, which bears on whether individual regional
   coefficients are separately informative even though the block is jointly
   identified. The memo must require reporting the eigenspectrum of V_RR and
   identifying the weakest direction. This is a reporting requirement, not a
   gate: Phase 4 already passed rank and positive-definiteness on this design.
5. **Multiplicity.** Ten individual coefficients invite ten individual tests. The
   memo should fix the convention that the **joint** test carries the
   significance claim and the individual coefficients are reported without
   multiplicity adjustment as descriptive detail. This is cleaner than adjusting
   ten marginal tests and matches how the claim will be stated in the paper.
6. **Model-versus-robust divergence in this block specifically.** A large
   robust/model ratio concentrated in the regional block would be diagnostically
   interesting. The memo must require the ratio to be reported and must forbid
   interpreting it as evidence of anything: it is a warning-tier diagnostic, in
   the manner of the Phase-4 R-3 loading-share diagnostic which was explicitly
   warning-only and never gating.

---

## 10. Score-artifact decision analysis

### 10.1 The decision

One of: committed CSV; committed binary artifact; hashed binary artifact plus
committed summaries.

### 10.2 What the design memo must establish

1. **The object and its dimensions.** The primitive is the 1,555 × 37 free-score
   matrix; the interior 1,555 × 35 object is a by-name column selection, not a
   separate primitive. The memo must state which is stored and which is derived.
2. **Size, so the decision is not made in the abstract.** 1,555 × 37 float64 is
   57,535 values, roughly 0.44 MiB as raw binary and roughly 1.4 MB as CSV at 17
   significant digits. Both are trivially committable. The "artifact too large to
   commit" argument does not apply, and the memo should say so explicitly rather
   than leave the reader wondering why the option list included a hashed-binary
   fallback.
3. **Bit-exactness.** Float64 written at 17 significant digits round-trips
   exactly under IEEE-754, so a correctly written CSV is not lossy; but its hash
   is sensitive to line endings, locale, and formatting, whereas a `.npy` hash is
   not. This, not size, is the real axis of the decision.
4. **Precedent.** The accepted Phase-4 bundle contains **both** a Hessian CSV and
   an optional `hessian_free.npy`. Following the accepted convention is a strong
   argument, and consistency across phases is itself a reproducibility property.
5. **Required committed summaries in every case.** Shape; ordered column names;
   column sums with their deviation from −∇negLL; per-column min, max, mean, and
   L2 norm; the meat's eigenvalues; the artifact SHA-256; and the environment
   fingerprint from V-11.

### 10.3 Working presumption

Follow the Phase-4 dual-format precedent: CSV as the canonical committed
artifact at 17 significant digits, `.npy` committed alongside as the bit-exact
companion, both hashed in the manifest, plus the committed summary table. This
is one baseline, not a menu; the falsification criterion is a repository policy
against committing binary artifacts, in which case CSV alone is canonical and
the `.npy` is dropped.

---

## 11. Numerical-gate design

The memo must pre-register gates with exact tolerances **before** any
implementation mission begins. Gates are named in the project's established
convention and split into gating and warning tiers, following Phase 4's practice
of an explicitly non-gating diagnostic.

### 11.1 Gating

| Gate | Statement | Tolerance |
| --- | --- | --- |
| T-1 | Score identity: `np.allclose(Σ_g s_g, −∇negLL, atol=1e-8, rtol=1e-8)` | frozen by charter §8 |
| T-2 | Shape: score matrix is exactly (1555, 37); column order matches the parameter map by name | exact |
| T-3 | Cluster count: unique `idhh` = 1,555; no missing; row-to-group alignment verified | exact |
| T-4 | Free-gradient reproduction against the published Phase-4 `gradient_free` | ≤ 1e-12 (Phase 4 achieved 8.88e-16 against Phase 3) |
| T-5 | Bread provenance: Hessian loaded from the accepted bundle; bundle SHA-256 recomputes to `5484886985…`; θ̂ hash recomputes to `c024b893…` | exact |
| T-6 | Bread integrity on load: symmetry deviation ≤ 2.3588e-4; minimum eigenvalue > 0; rank 37 | Phase-4 recorded tolerances |
| T-7 | Meat validity: Ω symmetric; minimum eigenvalue ≥ −1e-8 × maximum eigenvalue; rank reported | as stated |
| T-8 | Solve stability: every inverse-like operation by factorization; maximum absolute deviation from a pseudo-inverse reference ≤ 1e-8 | Phase 4 achieved 8.53e-14 |
| T-9 | Positive variances: all 35 interior diagonal entries strictly positive and finite, for both model and robust covariances | exact |
| T-10 | Correction scalar recorded as an explicit number with its formula and the numerical values of G, N, and K | exact |
| T-11 | Chunking invariance: if scores are computed in chunks, the concatenated matrix equals the single-pass matrix, or at minimum T-1 holds on the concatenation | machine zero preferred; T-1 minimum |
| T-12 | Determinism: a rerun in the recorded environment reproduces the artifact hash | exact |
| T-13 | Immutability: post-run recheck confirms all authenticated inputs, the ten pins, and the accepted bundles unchanged | exact, following Phases 3–4 |
| T-14 | Regional tests: V_RR positive definite; W finite for all three nulls; both model and robust computed; degrees of freedom recorded as 10, 7, 2 | exact |
| T-15 | Float64: `jax_enable_x64` confirmed true | exact; failure halts |

### 11.2 Warning tier, never gating

| Diagnostic | Statement |
| --- | --- |
| W-1 | Robust-to-model standard-error ratio reported per parameter; flag any ratio outside [0.2, 5] |
| W-2 | Eigenspectrum of V_RR reported with the weakest direction identified |
| W-3 | Effective-rank summary of the meat relative to 35 |

The memo must state, as Phase 4 did for its loading-share diagnostic, that
warning-tier items are informational and never determine the verdict.

---

## 12. Package-interface implications

The design must be expressible in the generic `dclaborsupply` API contemplated
by PKG-M02, without encoding France, EU-SILC, EUROMOD, or P2a assumptions
(governance §6, charter §10). Constraints the memo must impose on itself:

1. Cluster identity is an **argument** — an integer array or group-boundary
   array — never a hard-coded `idhh` column name.
2. The interface must not assume that the cluster count equals the number of
   likelihood terms. The degenerate case appears to hold for P2a; couples and
   pooled panels will break it. An API that assumed equivalence would be wrong
   at the first extension.
3. The active set is an **input**, not something the library infers from France
   bounds; the count of active constraints is not fixed at two.
4. Pins are a generic boolean mask with a generic pin-value vector; the library
   carries no knowledge of which economic coordinates are pinned or why.
5. The finite-sample correction is selectable — an enumeration or a callable —
   with the chosen convention recorded in returned metadata rather than assumed
   by the caller.
6. Restriction testing takes a generic (R, r) pair; regional blocks are a caller
   concern.
7. No assumption of 101 alternatives, a single year, one household type, or 37
   free coordinates anywhere in a signature or a validation check.
8. Returned objects carry their own provenance: which bread, which meat, which
   correction, which active set, which parameter ordering.

The memo states these as interface requirements. It does not design the API;
that is PKG-M02.

---

## 13. Targeted literature verification

Narrow, question-specific checks only. Each is triggered **only** if the design
memo cannot close the point from first principles. No broad literature search is
authorized (roadmap §6).

**L-1 — Boundary-constrained maximum likelihood.** Precise question: under
strictly active inequality constraints with strictly positive multipliers, is the
interior subvector of the constrained estimator asymptotically normal with
covariance equal to the inverse of the constrained information matrix, so that
conditional inference on the interior block is valid while symmetric inference on
the boundary coordinates is not? Anchors: Chernoff (1954); Self and Liang (1987);
Geyer (1994); Andrews (1999, 2002). **Priority: high** — this proposition is load
bearing for §7.

**L-2 — Cluster-robust finite-sample corrections.** Precise question: what is the
standard two-factor convention, and what does its parameter count K include when
some coordinates are pinned and some are at bounds? Anchors: Cameron and Miller
(2015); Cameron, Gelbach and Miller (2008, 2011); MacKinnon and Webb on small
cluster counts. **Priority: medium** — the magnitude is 1.15%, so this is a
convention check, not a result check.

**L-3 — Degenerate clustering.** Precise question: confirm that when each cluster
contains exactly one score contribution, the cluster-robust sandwich is
algebraically the outer-product-of-gradients misspecification-robust sandwich, and
confirm the standard naming convention in that case. Anchor: White (1982) and the
Cameron–Miller treatment. **Priority: high if V-5 returns the degenerate case**,
because it determines the manuscript's terminology.

**L-4 — Reference distribution for cluster-robust Wald tests.** Precise question:
χ²(q) versus F(q, G−q) with large G. **Priority: low.**

**L-5 — Reporting convention in the RURO / discrete-choice labour-supply
literature.** Precise question: do the closest comparators report model-based
standard errors, robust standard errors, or bootstrap intervals, and is bootstrap
the expected standard for welfare simulations built on these models? This is a
referee-expectation question and also informs whether JMP-M09 must plan a
bootstrap rather than treat it as deferred (X-005). **Priority: medium.**

Deep Research is authorized only for items that remain unresolved after the
memo's own reasoning, one narrow question at a time, per charter §12.

---

## 14. Required design-memo structure

The design artifact is
`docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v1.md`
with exactly these headings:

1. Design verdict
2. Scope and non-scope
3. Canonical inputs and verified repository paths
4. Notation, parameter map, and index maps
5. Household log-likelihood decomposition
6. Household score definition and sign convention
7. Sample scaling and weighting
8. Cluster definition and cluster-count contract
9. Model-based covariance
10. Cluster-robust sandwich covariance
11. Finite-sample correction decision
12. Active-bound treatment decision
13. Fixed-pin reporting decision
14. Regional and access block inference protocol
15. Score-artifact format decision
16. Numerical gates and tolerances
17. Immutable output contract
18. Reporting templates and permitted claims
19. Package and API implications
20. Limitations and dependencies on later missions
21. Halt conditions
22. Implementation-mission handoff

Required properties of the memo:

- **One** recommended baseline per decision, with the rejected alternatives
  named and the rejection reason given. No menus of equally weighted options.
- Every recommendation states its own falsification criterion, pre-registered
  before implementation, consistent with the programme's pre-registration
  discipline.
- Every numerical claim traces to a supplied artifact or a verified repository
  path, or is marked `UNKNOWN`.
- Section 1 uses exactly one of: `READY FOR IMPLEMENTATION CHARTER`,
  `READY WITH OPEN DECISIONS`, `BLOCKED`.
- Section 18 states the permitted and prohibited claims explicitly, in the style
  of the Phase-3 and Phase-4 acceptance memos.
- Section 22 supplies the content needed for the follow-on implementation
  charter under the sixteen headings of `JMP_mission_template_v1.md`, without
  writing that charter, which is the programme manager's artifact.

---

## 15. Halt conditions

The eight charter §13 halts apply unchanged: canonical-file conflict;
unverifiable score or likelihood source; ambiguous parameter ordering; cluster
count differing from 1,555; a design requiring a change to the accepted model;
an unjustifiable finite-sample correction; unresolved active-bound treatment;
expansion into implementation.

Plan-stage additions, each requiring a stop and a return to the programme
manager:

- **HM-REV** — V-1 descendancy check fails, so the canonical checkpoint revision
  and the execution revision cannot be reconciled.
- **HM-MAP** — the free-vector ordering cannot be established by name from a
  committed source.
- **HM-LL** — the additive composition of the household log-likelihood cannot be
  established, so the household score cannot be defined.
- **HM-WGT** — the weighting and scaling convention of the accepted objective
  cannot be established.
- **HM-CLUS** — the household identifier array cannot be aligned to loader group
  order with a documented mechanism.
- **HM-KKT** — the recorded bound direction is inconsistent with the sign of the
  published free-gradient component.
- **HM-X64** — float64 cannot be confirmed for the accepted pipeline.
- **HM-SCOPE** — any task in this plan begins to require executing code,
  computing a score, or evaluating a gradient or Hessian.

---

## 16. Deliverables

**This stage:**

- `docs/missions/JMP_M05_task_plan_v1.md` — this document. Not committed.

**Next stage, on manager acceptance of this plan:**

- `docs/France_case/P2a/FR_P2a_region_live_phase5_inference_design_v1.md` — the
  statistical design memo per §14, produced in Claude Project 1 with Opus and
  thinking on, per charter §12. Not committed before manager review.

**Not authorized in either stage:** code, scripts, notebooks, score matrices,
covariance matrices, standard errors, test statistics, result bundles, commits,
or any repository state change.

---

## 17. Recommended execution order

One sequence. Steps 1–3 close the source gaps; steps 4–10 are the memo's
substance; step 11 assembles.

1. **Source verification, first pass.** V-2, V-4, V-5, V-6, V-7 — the five items
   without which no score can be defined. Then V-3, V-8, V-9. Record each result
   or `UNKNOWN`.
2. **Source verification, provenance pass.** V-1, V-10, V-11, V-12.
3. **Gap triage.** If any of V-2, V-4, V-5, V-7 is `UNKNOWN`, fire the
   corresponding halt and return to the manager rather than proceeding on
   assumption. If only V-6, V-8, or V-9 is `UNKNOWN`, proceed and mark the
   dependent decisions as open, since these constrain reporting and null
   specification rather than the score definition itself.
4. **Derivations.** S-1, S-2, S-3 — notation, index maps, household
   contribution, score, sign convention, and the identity.
5. **Cluster contract.** S-4, including the binding-versus-degenerate finding and
   its terminological consequence.
6. **Covariance objects.** S-5, S-6 — bread from the accepted artifact, meat,
   sandwich, solve discipline.
7. **The three manager decisions, in dependency order.** §7 first, because the
   active-bound treatment determines which coordinates the covariance covers and
   therefore what K means; then §6, the finite-sample correction, which depends
   on K; then §10, the score-artifact format, which is independent of both.
8. **The two further decisions.** §8 pin reporting; §9 regional protocol.
9. **Literature checks.** L-1 and, if V-5 returned degeneracy, L-3. Then L-2 and
   L-5 only if still open. L-4 only if a reviewer raises it.
10. **Gates.** §11, with every tolerance stated as a number and every gate
    assigned to the gating or warning tier.
11. **Assembly.** Write the memo to the §14 structure; add §20 limitations
    including the S-10 downstream declaration; add §22 handoff content; set the
    §1 verdict; do not commit.

---

## 18. Immediate next action

Execute step 1 of §17: retrieve and record the parameter map, the JAX likelihood
composition, the likelihood-term count, the weighting convention, and the
cluster-identifier alignment from the MNL and nested `dclaborsupply` working
trees at the recorded revisions, reporting each as a verified value or `UNKNOWN`.
This is a read-only repository-inspection task for Claude Code, appropriate to
the CLI or extension; it computes nothing, evaluates no gradient or Hessian, and
changes no file.

Do not begin the design memo before that retrieval is reported, and do not commit
this plan before manager review.

---

### Output-discipline record

- **Mission ID:** JMP-M05, design-only stage.
- **Authoritative inputs:** the ten supplied governance, charter, acceptance, and
  diagnostic documents listed in §3.1, in the order fixed by governance §5.
  Project memory was treated as background only, and the historical NC-pilot
  bound-hit material was explicitly demoted to reasoning precedent in §3.3.
- **Decisions made in this plan:** mission interpretation; the task inventory and
  its split between source verification and statistical design; the derivation
  programme; the gate architecture with tolerances; the design-memo structure;
  the execution order; and one working presumption per manager decision, each
  with a pre-registered falsification criterion. No statistical decision is
  closed here.
- **Unresolved decisions:** the three manager decisions themselves; pin
  representation; the regional joint-test protocol; and the six source gaps G-A
  to G-F, plus the V-1 revision reconciliation.
- **Exact output filename:** `JMP_M05_task_plan_v1.md`, for
  `docs/missions/JMP_M05_task_plan_v1.md`.
- **Next authorised action:** §18 — read-only source verification, step 1 of §17.

**FINAL VERDICT: READY WITH SOURCE GAPS**
