# INDEX 07 - Inference and Computation v2

> **Version note:** v2 adds Cameron & Miller 2015 to the Bootstrap and
> Standard Errors sections, and adds a Train 2009 methods reference to the
> Simulated Likelihood section. All other sections are unchanged from v1.
> v1 file is preserved.
>
> **Cameron & Miller 2015 role:** This is a methods survey on cluster-robust
> inference. It supports the JMP's inference layer only — the cluster-robust
> bootstrap on `idorighh` (≈9,657 clusters). It does not speak to structural
> labor supply, opportunity density, welfare objects, or any element of the
> access/ability/preference decomposition. Do not cite it for anything beyond
> inference and standard errors.

---

## Simulated Likelihood

- **Claim:** Sampled or simulated alternatives are established in the RURO
  tradition, but implementation details differ across papers.
  **Sources:** Aaberge et al. 2009 [explicit sampled estimator]; Capeau &
  Decoster 2016 [explicit sampled alternatives and correction]; Aaberge &
  Colombino 2013 [background simulation with observed job plus draws]; Beffy et
  al. 2019 [contrast: combinatorial two-offer likelihood].
  **Do not overclaim:** Not every source uses the JMP's sampled-MNL likelihood or
  `-log pi` correction.

- **Claim:** Synthetic recovery is the JMP's standard for accepting a structural
  specification, not merely an in-sample fit criterion.
  **Sources:** JMP project state v1 [explicit]; Aaberge et al. 2009 [background
  true-model/re-estimate/compare template]; Beffy et al. 2019 [explicit Monte
  Carlo recovery].
  **Do not overclaim:** Aaberge et al. 2009 and Beffy et al. 2019 support the
  validation logic, but the certified 47-parameter result is the JMP's own.

> *Methods reference:* Train (2009), *Discrete Choice Methods with Simulation*
> (MIT Press, 2nd ed.; freely downloadable from author website), is the standard
> reference for quasi-random integration (Halton sequences, MLHS) and simulated
> maximum likelihood in discrete-choice models. Cite for simulation-method
> language only; not a welfare or decomposition source.

## Sampled Alternatives

- **Claim:** The correction for sampled alternatives is separate from the
  structural opportunity terms and must be carried at the alternative level.
  **Sources:** Aaberge et al. 2009 [explicit]; Capeau & Decoster 2016 [explicit];
  JMP project state v1 [explicit].
  **Do not overclaim:** Dagsvik & Jia 2016 enumerates hours alternatives and has
  no proposal correction.

- **Claim:** Effective sample size and redraw stability are under-covered in the
  accepted literature and are therefore a JMP-specific validation frontier.
  **Sources:** JMP project state v1 [explicit ESS/redraw frontier]; Aaberge &
  Colombino 2013 [weak/background absence of ESS check]; Jacquet et al. 2026
  [weak/background absence of importance-sampling guidance].
  **Do not overclaim:** The under-coverage is not evidence that the problem is
  unimportant; it is a reason the JMP gate matters.

## Bootstrap

- **Claim:** Headline uncertainty should use cluster-robust bootstrap, especially
  because bound/pinned parameters invalidate simple asymptotic SEs for headline
  welfare/decomposition claims.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Cameron & Miller 2015 [explicit: cluster-robust variance estimator (CRVE
  sandwich) and pairs/wild cluster bootstrap for data with within-cluster error
  correlation; authoritative practitioner anchor for clustered-data inference;
  *Journal of Human Resources* 50(2):317–372].
  **Do not overclaim:** Cameron & Miller 2015 covers the general econometric
  justification for cluster-robust inference; the JMP's specific bootstrap
  implementation for a structural RURO model with bound parameters remains the
  JMP's own design choice and is not pre-approved by C&M. Cameron & Miller is
  not a structural labor-supply or welfare paper; do not cite it for opportunity
  density, W^1–W^6, or decomposition content.

## Standard Errors

- **Claim:** Opportunity parameters are expected to be more precisely estimated
  than preference parameters in the certified baseline, which affects component
  uncertainty.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Cameron & Miller 2015 [explicit: cluster-robust SE justification when
  idiosyncratic errors are correlated within household clusters; with ≈9,657
  `idorighh` clusters, the many-clusters regime holds and the CRVE and pairs
  cluster bootstrap are well-behaved; *Journal of Human Resources* 50(2):317–372];
  Beffy et al. 2019 [derived-by-analogy identification trade-off between
  dominated regions and preferences].
  **Do not overclaim:** This is expected/diagnostic until decomposition CIs are
  computed. Cameron & Miller 2015 speaks to the cluster-robust inference
  machinery, not to whether the structural opportunity/preference split is
  precisely estimated. "Two-way clustering" in Cameron & Miller refers to
  clustering over two error-covariance dimensions (e.g. state and year); it is
  not the JMP's three-channel (access/ability/preference) decomposition — the
  terms are unrelated. The few-clusters corrections in Cameron & Miller (wild
  bootstrap as a necessity, CR2/CR3, effective-number-of-clusters) are background
  for the JMP: with ≈9,657 clusters, the standard CRVE and pairs bootstrap are
  appropriate.

- **Claim:** Boundaries and pinned parameters require explicit reporting rather
  than silent asymptotic inference.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit].
  **Do not overclaim:** This is a baseline-specific constraint, not a general
  claim about all RURO estimates.

## Simulation Error

- **Claim:** Welfare integration error is a live issue because the inclusive
  value depends on sampled alternatives and low effective sample size can distort
  household welfare.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit].
  **Do not overclaim:** No welfare findings should be reported until the
  integration gates pass.

- **Claim:** Analytic integration over EV shocks is preferred in the welfare
  layer; simulation concern is about alternatives/nodes, not about drawing EV
  shocks.
  **Sources:** Dagsvik & Karlstrom 2005 [explicit analytic-in-shocks machinery];
  JMP welfare spec v5 [explicit]; Aaberge & Colombino 2013 [background contrast
  with simulated argmax].
  **Do not overclaim:** Dagsvik & Karlstrom do not solve the alternative-sampling
  ESS problem.

## JAX / CONOPT Relevance

- **Claim:** JAX is a project implementation choice validated against the
  likelihood engine; the literature supports the structural model, not JAX
  specifically.
  **Sources:** JMP project state v1 [explicit]; Capeau & Decoster 2016
  [background estimation program lineage, not JAX]; Aaberge et al. 2009
  [background estimation/simulation].
  **Do not overclaim:** Do not cite T1A/T1B papers as if they endorse JAX or the
  abandoned CONOPT path.

## Active Constraints And Boundary Issues

- **Claim:** Active bounds and unidentified/pinned preference parameters require
  explicit qualification in inference and decomposition interpretation.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Jacquet et al. 2026 [background candid non-identification/normalisation
  precedent].
  **Do not overclaim:** Jacquet et al.'s non-identification is a precedent for
  honesty, not evidence for the JMP's parameter pins.

## What Remains Under-Covered

- **Claim:** The literature gives weak coverage of the exact computational
  problem created by ex-ante money-metric welfare over sampled, heterogeneous
  opportunity sets.
  **Sources:** JMP project state v1 [explicit current frontier]; Dagsvik &
  Karlstrom 2005 [explicit welfare machinery but no opportunity density];
  Capeau & Decoster 2016 [explicit opportunity sampling but no money-metric
  welfare]; Aaberge & Colombino 2013 [background ex-post contrast].
  **Do not overclaim:** This is a gap statement for targeted follow-up, not a
  claim that the literature has no relevant building blocks.

- **Claim:** The literature gives weak direct support for occupation-as-access
  and the within-opportunity access/ability split.
  **Sources:** JMP project state v1 [explicit design]; Dagsvik & Jia 2016
  [explicit occupation absence]; Capeau & Decoster 2016 [explicit occupation
  absence]; Aaberge & Colombino 2013 [explicit conflation warning]; Beffy et al.
  2019 [explicit ability/occupation absence].
  **Do not overclaim:** Treat this as a Deep Research target or robustness
  priority, not as already settled by the accepted corpus.
