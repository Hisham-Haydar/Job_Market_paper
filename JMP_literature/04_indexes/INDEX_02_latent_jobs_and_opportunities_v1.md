# INDEX 02 - Latent Jobs and Opportunities v1

## Latent Jobs

- **Claim:** The empirical unit is a latent job package, not a point on a common
  hours grid. Labor supply is modeled as choice among feasible wage-hours job
  packages, with non-work as an alternative.
  **Sources:** Dagsvik & Jia 2016 [explicit]; Dagsvik et al. 2014 [background];
  Capeau & Decoster 2016 [explicit]; Aaberge & Colombino 2013 [explicit];
  Aaberge & Colombino 2018 [background].
  **Do not overclaim:** These sources justify the latent-jobs architecture; they
  do not by themselves justify the JMP's W^1-W^6 welfare family or three-way
  decomposition.

- **Claim:** The latent-jobs approach is the model-class departure from standard
  fixed-grid labor-supply models.
  **Sources:** Van Soest 1995 [explicit fixed-grid benchmark]; Dagsvik et al.
  2014 [background/motivation]; Aaberge et al. 2009 [explicit comparison of
  choice-set representations]; Aaberge & Colombino 2013 [explicit].
  **Do not overclaim:** Van Soest is the foil, not an opportunity-density source.

## Random Opportunities

- **Claim:** The RURO literature often derives choice probabilities from a random
  opportunity process, but the JMP uses the resulting opportunity density as a
  deterministic estimated feasible-set object for welfare/decomposition.
  **Sources:** Dagsvik & Jia 2016 [explicit random/Poisson lineage]; Capeau &
  Decoster 2016 [explicit random-opportunity lineage]; Beffy et al. 2019
  [explicit random-offer restricted choice]; Jacquet et al. 2026 [explicitly
  compatible with deterministic opportunity-size parameters].
  **Do not overclaim:** Do not describe the JMP welfare object as depending on
  realised random opportunity draws; the summaries repeatedly require a
  deterministic-opportunities mapping.

## Constrained Choice Sets

- **Claim:** Constrained choice sets matter empirically because omitted
  restrictions can be absorbed into estimated preferences and elasticities.
  **Sources:** Bargain et al. 2013 [explicit omission/motivation]; Van Soest
  1995 [explicit availability-constraint effect on elasticities]; Beffy et al.
  2019 [explicit restricted-choice identification and elasticity changes];
  Capeau & Decoster 2016 [explicit opportunity-vs-preference counterfactual].
  **Do not overclaim:** These are not all welfare-decomposition sources; some
  speak only to behavior or identification.

- **Claim:** A common hours grid is useful as a benchmark but cannot carry the
  JMP's household-specific access channel.
  **Sources:** Van Soest 1995 [explicit fixed-grid MNL]; Bargain et al. 2013
  [explicit fixed common grid welfare comparator]; Aaberge et al. 2009 [explicit
  choice-set representation comparison].
  **Do not overclaim:** A fixed grid is not "wrong" generically; it is
  insufficient for a paper whose object is unequal feasible job sets.

## Opportunity Density

- **Claim:** The opportunity density is the structural object that separates the
  feasible-job side from preferences.
  **Sources:** Dagsvik & Jia 2016 [explicit factorization and identification];
  Capeau et al. 2015/2016 RURO [explicit estimation recipe]; Capeau & Decoster
  2016 [explicit `q*g1*g2` factorization]; Aaberge & Colombino 2013 [explicit
  density `p(h,w,s)`]; Beffy et al. 2019 [explicit hours-offer density].
  **Do not overclaim:** Beffy identifies hours offers, not a full wage/occupation
  opportunity density.

- **Claim:** The JMP's access / ability / preference vocabulary refines, rather
  than simply repeats, the older opportunity/preference split.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Dagsvik & Jia 2016 [explicit two-way source mapped by analogy]; Capeau &
  Decoster 2016 [explicit two-way source mapped by analogy].
  **Do not overclaim:** The three-way cut is the JMP's operational/normative
  partition; most sources do not contain it as such.

## Proposal Correction

- **Claim:** When alternatives are sampled, a per-alternative sampling correction
  is mandatory; in additive log form this is the `-log pi(j;x_i)` term.
  **Sources:** Aaberge et al. 2009 [explicit sampling-of-alternatives correction];
  Capeau & Decoster 2016 [explicit importance-sampling reweighting]; Capeau et
  al. 2015/2016 RURO [explicit, via summary]; JMP welfare spec v5 [explicit].
  **Do not overclaim:** Dagsvik & Jia 2016 and Beffy et al. 2019 do not use a
  McFadden-style proposal correction because their choice sets are enumerated or
  modeled differently.

- **Claim:** The proposal correction is distinct from structural opportunity
  density terms: the model keeps `log h`, `log w`, and market/access terms while
  subtracting the proposal log-density.
  **Sources:** Dagsvik & Jia 2016 [derived-by-analogy from enumerated structural
  `g`]; Capeau & Decoster 2016 [explicit sampling correction]; JMP project state
  v1 [explicit].
  **Do not overclaim:** Do not cite enumerated-grid papers as if they prove the
  sampled-estimator correction.

## Access Versus Ability

- **Claim:** Ability is the wage-technology sub-block: returns to education and
  experience plus residual productivity dispersion.
  **Sources:** Dagsvik & Jia 2016 [explicit wage technology and individual
  ability language]; Capeau & Decoster 2016 [explicit wage-offer density as
  wage technology]; JMP project state v1 [explicit]; JMP welfare spec v5
  [explicit].
  **Do not overclaim:** Beffy et al. 2019 treats wage as a worker attribute, not
  as a wage-offer density; use it only by analogy.

- **Claim:** Access is the non-wage feasible-set side: hours availability,
  market/participation availability, region/year environment, and occupation
  availability in the JMP baseline.
  **Sources:** Capeau & Decoster 2016 [explicit hours and offer-intensity access];
  Beffy et al. 2019 [explicit hours-offer access]; Dagsvik & Jia 2016 [explicit
  hours/market opportunity terms]; JMP project state v1 [explicit]; JMP welfare
  spec v5 [explicit].
  **Do not overclaim:** The occupation component is the JMP's addition; most
  RURO sources have no occupation channel.

## Occupation Availability

- **Claim:** Occupation belongs in the JMP opportunity/access layer, not in the
  utility block and not in the structural wage return.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit].
  **Do not overclaim:** No accepted T1A/T1B source directly estimates the JMP's
  `loc4` occupation-as-access object. Dagsvik & Jia 2016 and Capeau & Decoster
  2016 are explicit absences; Aaberge & Colombino 2013 has occupation/sector
  conflation and double-entry warnings.

- **Claim:** The terminology must separate occupation/ISCO-type availability
  from industry/sector/NACE robustness.
  **Sources:** JMP project state v1 [explicit]; QC report v1 [explicit];
  Aaberge & Colombino 2013 [weak caution because of occupation/sector
  conflation]; Dagsvik & Jia 2016 [weak caution because "sector" is informal].
  **Do not overclaim:** Do not cite a source with no occupation variable as
  affirmative support for occupation-as-access.

## Choice-Set Sampling

- **Claim:** Sampling alternatives can be used for estimation and welfare
  integration, but it creates a separate integration-quality problem.
  **Sources:** Aaberge et al. 2009 [explicit sampling estimator]; Capeau &
  Decoster 2016 [explicit sampled alternatives]; Aaberge & Colombino 2013
  [background simulation with observed job plus 199 draws]; JMP project state v1
  [explicit ESS and redraw-cross-check frontier].
  **Do not overclaim:** The literature gives sampling precedents, but the
  production ESS/redraw certification problem is the JMP's own current gate.

## Relationship To Fixed-Grid Labor Supply Models

- **Claim:** Fixed-grid MNL models are the structural labor-supply baseline, but
  they treat constrained opportunities through common grids or ad hoc
  availability constants rather than a household-specific density.
  **Sources:** Van Soest 1995 [explicit]; Bargain et al. 2013 [explicit welfare
  comparator using fixed common grid]; Aaberge et al. 2009 [explicit comparison];
  Dagsvik et al. 2014 [background critique].
  **Do not overclaim:** Fixed-grid sources remain important for budget-set and
  discrete-choice labor-supply heritage; they are not discarded, only bounded.
