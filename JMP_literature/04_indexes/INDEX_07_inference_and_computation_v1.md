# INDEX 07 - Inference and Computation v1

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
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit].
  **Do not overclaim:** The accepted T1A/T1B literature does not supply the exact
  JMP bootstrap implementation.

## Standard Errors

- **Claim:** Opportunity parameters are expected to be more precisely estimated
  than preference parameters in the certified baseline, which affects component
  uncertainty.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Beffy et al. 2019 [derived-by-analogy identification trade-off between
  dominated regions and preferences].
  **Do not overclaim:** This is expected/diagnostic until decomposition CIs are
  computed.

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
