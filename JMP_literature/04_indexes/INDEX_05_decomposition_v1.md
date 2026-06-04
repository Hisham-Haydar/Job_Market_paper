# INDEX 05 - Decomposition v1

## Shorrocks / Shapley Decomposition

- **Claim:** The decomposition should be Shapley-Shorrocks because it is
  exhaustive and order-independent.
  **Sources:** Shorrocks 2013 [explicit]; Audoly et al. 2025 [explicit
  practitioner recipe]; Sastre & Trannoy 2002 [explicit methodological issues];
  JMP welfare spec v5 [explicit].
  **Do not overclaim:** These sources justify the allocation rule, not the
  economic channel partition.

- **Claim:** Shorrocks 1982 is the foundation and warning: unaxiomatized
  decompositions can be arbitrary; structural-channel decomposition needs
  axiomatic discipline.
  **Sources:** Shorrocks 1982 [explicit]; Shorrocks 2013 [background extension];
  Audoly et al. 2025 [background operationalization].
  **Do not overclaim:** The 1982 covariance rule is for additive income sources
  and does not transport directly to access/ability/preference channels.

## Source Decomposition

- **Claim:** The JMP decomposes inequality in the constructed welfare vector
  `Omega^k`, not observed income.
  **Sources:** JMP welfare spec v5 [explicit]; JMP project state v1 [explicit];
  Shorrocks 2013 [background general decomposition framework]; Audoly et al.
  2025 [explicit arbitrary sample transformation support].
  **Do not overclaim:** Shorrocks 2013 supplies the decomposition method; the
  welfare vector is the JMP's object.

- **Claim:** The sources are structural blocks, not additive money components:
  access, ability, and preference are neutralized/equalized and the welfare
  distribution is recomputed.
  **Sources:** JMP welfare spec v5 [explicit]; JMP project state v1 [explicit];
  Shorrocks 1982 [derived-by-analogy from eliminated contribution]; Shorrocks
  2013 [background Shapley averaging].
  **Do not overclaim:** Do not cite Shorrocks 1982 as if it directly decomposes
  structural models.

## Path / Order Dependence

- **Claim:** Order dependence is the reason for Shapley averaging: each channel's
  marginal contribution depends on what has already been equalized.
  **Sources:** Shorrocks 2013 [explicit]; Audoly et al. 2025 [explicit];
  Sastre & Trannoy 2002 [explicit practical issues]; JMP welfare spec v5
  [explicit 3! orderings].
  **Do not overclaim:** Order-independence of the rule does not make the channel
  partition causal or data-free.

- **Claim:** Interactions among channels should be split symmetrically rather
  than loaded onto one source.
  **Sources:** Shorrocks 1982 [explicit warning via pure/eliminated
  interpretations]; Shorrocks 2013 [explicit Shapley framework]; Audoly et al.
  2025 [explicit].
  **Do not overclaim:** Symmetric interaction allocation is a decomposition
  convention with axiomatic backing, not evidence that channels are independent.

## Exact Decomposition

- **Claim:** The implementation gate is exactness: Shapley components must sum
  exactly to total inequality `I(Omega^k)` for each measure.
  **Sources:** JMP welfare spec v5 [explicit]; Shorrocks 2013 [explicit
  exhaustiveness]; Audoly et al. 2025 [explicit]; Sastre & Trannoy 2002
  [background].
  **Do not overclaim:** Exact summation is a numerical/accounting gate, not a
  proof that the structural model is true.

## Access / Ability / Preference Equalization

- **Claim:** Access equalization changes hours, market, region/year, and
  occupation offer availability while holding ability and preferences fixed.
  **Sources:** JMP welfare spec v5 [explicit]; JMP project state v1 [explicit];
  Capeau & Decoster 2016 [background two-way opportunity equalization]; Beffy et
  al. 2019 [background restricted-hours counterfactual].
  **Do not overclaim:** Published RURO counterfactuals are not the JMP's
  three-way Shapley decomposition.

- **Claim:** Ability equalization neutralizes wage-technology differences and is
  reported as the contested addition to the access-only lower bound.
  **Sources:** JMP welfare spec v5 [explicit]; Fleurbaey & Maniquet 2018 JEL
  [derived-by-analogy responsibility-for-skill axis]; Dagsvik & Jia 2016
  [explicit wage/ability object]; Capeau & Decoster 2016 [explicit wage-offer
  density].
  **Do not overclaim:** The literature supports the pieces; the exact
  access-only/access-plus-ability bracket is the JMP design.

- **Claim:** Preference equalization changes the preference yardstick and must be
  handled carefully for couples because pinned/degenerate male-leisure
  parameters compress the couples preference component.
  **Sources:** JMP welfare spec v5 [explicit]; JMP project state v1 [explicit];
  Jacquet et al. 2026 [background reference-preference comparator]; Aaberge &
  Colombino 2013 [background common-utility comparator].
  **Do not overclaim:** Preference equalization is not the same as the primary
  preference-respecting welfare metric.

## Warnings Against Causal Interpretation

- **Claim:** The decomposition is conditional on a model and a normative channel
  cut; it is not a causal estimate of labor-market mechanisms.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Shorrocks 1982 [background warning about behavioral feedback omitted by pure
  factor decompositions]; Audoly et al. 2025 [background channel-blind method].
  **Do not overclaim:** Do not write "access causes X percent" without the
  model-conditional qualifier.

- **Claim:** The decomposition does not identify channels by itself; structural
  identification comes from the latent-jobs/RURO model and synthetic recovery.
  **Sources:** Dagsvik & Jia 2016 [explicit preference/opportunity
  identification]; Beffy et al. 2019 [explicit identification and Monte Carlo
  recovery]; JMP project state v1 [explicit synthetic-recovery gate]; Shorrocks
  2013 [background decomposition rule only].
  **Do not overclaim:** Shapley solves allocation/order dependence, not
  structural identification.
