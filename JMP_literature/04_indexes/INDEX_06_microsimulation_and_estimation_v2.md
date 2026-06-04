# INDEX 06 - Microsimulation and Estimation v2

> **Version note:** v2 adds entries from four DR03 accepted summaries: Bloemen
> 2000, Bloemen 2008 (RURO Estimation and Wage-Offer Modelling), Bloemen 2010
> (Couples/Singles), and Löffler et al. 2014 (Wage-Offer Modelling). All v1
> content is carried forward unchanged. v1 file is preserved.
>
> **Citation warning — Bloemen 2000:** The PDF in `Literature/` is the 1992
> CentER Discussion Paper No. 9239 (Tilburg). All page references and quotes
> from the Bloemen 2000 summary refer to the DP text. Flag as `[DP version;
> journal pages TBC]` until the *Labour Economics* 7(3):297–312 (2000) journal
> article is confirmed.
>
> **Bloemen 2010 role:** Bloemen 2010 is a contrastive background source, not a
> JMP model component. It is the canonical collective-household model with non-
> participation; it is cited to bound the JMP's unitary simplification, not to
> import any bargaining or sharing-rule mechanism.
>
> **Löffler et al. 2014 outlet note:** The summary records SOEPpapers No. 675;
> the acquisition queue references IZA DP 8281. Both are the same working paper.
> The 2018 published version (`loefflerSensitivityStructuralLabor2018`) is also
> in the corpus at T3 and may be cited interchangeably for the same caution.

---

## Structural Labor Supply

- **Claim:** The JMP sits in the discrete-choice structural labor-supply
  tradition and extends it with explicit opportunities.
  **Sources:** Van Soest 1995 [explicit benchmark]; Bargain et al. 2013
  [explicit welfare/labor-supply comparator]; Dagsvik & Jia 2016 [explicit
  latent-jobs model]; Aaberge & Colombino 2018 [background synthesis].
  **Do not overclaim:** Structural labor-supply heritage does not imply that
  standard fixed-grid models contain opportunity densities.

- **Claim:** Couples are modeled as joint/unitary decision units in the relevant
  tradition, matching the JMP household welfare unit.
  **Sources:** Van Soest 1995 [explicit]; Capeau & Decoster 2016 [explicit];
  Aaberge & Colombino 2013 [explicit]; Jacquet et al. 2026 [explicit]; JMP
  project state v1 [explicit].
  **Do not overclaim:** These sources do not solve intra-household distribution;
  the JMP also leaves collective welfare out of scope.

## RURO Estimation

- **Claim:** RURO estimation separates a preference block from an opportunity
  density and fits labor supply as choice among latent jobs.
  **Sources:** Dagsvik & Jia 2016 [explicit]; Capeau et al. 2015/2016 RURO
  [explicit]; Capeau & Decoster 2016 [explicit]; Aaberge & Colombino 2013
  [explicit]; Aaberge & Colombino 2018 [background].
  **Do not overclaim:** Most RURO sources have a two-way preference/opportunity
  split; the JMP's access/ability/preference cut is finer.

- **Claim:** Preference/opportunity separation in cross-section is defended by
  functional form, exclusion/budget variation, and recovery/validation evidence.
  **Sources:** Dagsvik & Jia 2016 [explicit identification]; Beffy et al. 2019
  [explicit budget-constraint identification and Monte Carlo recovery]; Capeau &
  Decoster 2016 [explicit exclusion-restriction precedent]; JMP project state v1
  [explicit synthetic-recovery gate].
  **Do not overclaim:** Identification is parametric/model-conditional; do not
  present it as nonparametric or instrument-free causal identification.

- **Claim:** The job-offer-restriction tradition (Bloemen line) pre-dates and
  substantiates the latent-jobs framing: it models labor supply as choice among
  restricted (wage, hours) packages rather than over a common hours grid.
  **Sources:** Bloemen 2000 [explicit restricted-offer labor-supply model, static
  cross-section — DP version, journal pages TBC]; Bloemen 2008 [explicit job-
  search with wage-and-hours offers; hours availability as demand-side object;
  *JoLE* 26(1):137–179].
  **Do not overclaim:** The Bloemen line does not contain RURO's opportunity-
  density estimation, the JMP welfare object ($W^1$–$W^6$), or the
  proposal/sampling correction. The Bloemen 2000 identification warning — that
  individualising the offer-intensity collapses preference identification — is a
  historical precedent for why the JMP's synthetic-recovery gate is necessary;
  it does not impugn the JMP baseline, which was disciplined by that gate. Use
  these sources for the model-class motivation paragraph only; do not cite them
  in the estimation section as if they contained RURO's likelihood.

## EUROMOD / Tax-Benefit Simulation

- **Claim:** EUROMOD is the disposable-income engine that maps each job package
  to consumption, not the paper's contribution.
  **Sources:** Sutherland & Figari 2013 [explicit]; Bargain et al. 2013
  [explicit EUROMOD welfare comparator]; Capeau & Decoster 2016 [explicit
  EUROMOD budget map]; JMP project state v1 [explicit].
  **Do not overclaim:** Do not cite EUROMOD for welfare theory, opportunities,
  or decomposition.

- **Claim:** Microsimulation is supporting infrastructure that enables nonlinear
  tax-benefit budgets inside structural labor supply.
  **Sources:** Sutherland & Figari 2013 [explicit]; Bargain et al. 2013
  [explicit]; Aaberge & Colombino 2018 [background]; Aaberge & Colombino 2013
  [explicit optimal-tax/microsimulation context].
  **Do not overclaim:** Microsimulation does not identify access or ability by
  itself.

## Budget-Set Construction

- **Claim:** Nonlinear tax-benefit budget heterogeneity is useful both for
  realistic welfare computation and for preference/opportunity identification.
  **Sources:** Van Soest 1995 [explicit nonlinear-budget discrete choice];
  Bargain et al. 2013 [explicit EUROMOD budget welfare]; Beffy et al. 2019
  [explicit budget-constraint heterogeneity identification]; Capeau & Decoster
  2016 [explicit EUROMOD `c=f(w,h;x)`].
  **Do not overclaim:** Budget heterogeneity does not by itself identify the
  within-opportunity ability/access split.

## Couples / Singles

- **Claim:** The JMP should keep singles and couples separately reportable
  because preferences, opportunity precision, and welfare integration differ by
  group.
  **Sources:** JMP project state v1 [explicit]; JMP welfare spec v5 [explicit];
  Van Soest 1995 [background couples benchmark]; Capeau & Decoster 2016
  [background singles/couples samples]; Jacquet et al. 2026 [background couples
  comparator].
  **Do not overclaim:** Literature precedent for unitary couples is not evidence
  that within-couple welfare is identified.

- **Claim:** A collective household model with non-participation provides a
  structural contrast to the JMP's unitary assumption: if within-couple
  bargaining and a sharing rule govern the allocation of non-labour income, the
  unitary model absorbs that heterogeneity into a joint preference block. The
  identification of a collective model requires egoistic preferences, no public
  goods, and ideally panel data — all conditions the JMP does not impose or have.
  **Sources:** Bloemen 2010 [explicit collective-household non-participation model
  with Chiappori/Donni sharing rule estimated on Dutch panel couples,
  *Economic Journal* 120(543):183–214 (2010) — background contrast only].
  **Do not overclaim:** The JMP uses a unitary household design. Bloemen 2010 is
  not a JMP model component and does not identify within-couple welfare in the
  JMP. Cite only to bound the unitary simplification and justify deferring intra-
  household distribution to a later project; do not import any bargaining
  mechanism, sharing rule, or collective-welfare object. The Bloemen 2010
  decomposition is preferences vs sharing rule — a two-way intra-household split,
  not the JMP's three-way access/ability/preference Shapley–Shorrocks split. Do
  not conflate. The coherence condition |s_m s_f| < 1 is specific to two-decider
  collective participation; it does not apply to the JMP's unitary couple.

## Wage-Offer Modelling

- **Claim:** Wage technology is central to the ability channel: education,
  experience, and residual dispersion shape available pay.
  **Sources:** Dagsvik & Jia 2016 [explicit wage/ability object]; Capeau &
  Decoster 2016 [explicit wage-offer density]; Aaberge & Colombino 2013
  [background wage-density opportunity]; JMP project state v1 [explicit].
  **Do not overclaim:** Beffy et al. 2019 has a wage equation but not a wage-offer
  opportunity density.

- **Claim:** The proposal distribution may individualize high-variance channels
  without changing the structural interpretation of the opportunity density.
  **Sources:** JMP welfare spec v5 [explicit proposal audit]; Dagsvik & Jia 2016
  [derived-by-analogy wage individualization]; Capeau & Decoster 2016 [explicit
  contrast: structural density rich, sampling prior mainly sex-specific].
  **Do not overclaim:** Proposal individualization is an integration design, not
  an extra structural channel.

- **Claim:** Wage-preference independence is a maintained assumption of RURO and
  related structural labor-supply models; it is testable and estimates are
  sensitive to it. Misspecified wage imputation or a violated wage-preference
  independence assumption can roughly double estimated labor-supply elasticities.
  **Sources:** Löffler et al. 2014 [explicit: meta-analysis of 3,456 discrete-
  choice structural labor-supply specs shows elasticities are robust to utility
  functional form and preference heterogeneity but highly sensitive to wage
  treatment and the wage-preference independence assumption; IZA DP 8281 /
  SOEPpapers 675]; JMP project state v1 [explicit: ability channel depends on
  separability of wage technology from preferences].
  **Do not overclaim:** Löffler et al. 2014 tests sensitivity in standard (non-
  RURO) discrete-choice labor-supply models; apply the caution by analogy to the
  JMP's ability channel. The paper is not a RURO/latent-jobs paper, not an
  opportunity-density paper, and not a welfare or decomposition paper. The ~0.2→
  ~0.6 elasticity result is for single females only (Germany/SOEP, 2007) and
  should not be generalized. The 2018 published version
  (`loefflerSensitivityStructuralLabor2018`) is also in the corpus at T3 and may
  be cited interchangeably for the same caution.

- **Claim:** Hours-and-wage offers are the structural objects behind the access
  channel; they are not merely computational artifacts. The hours-offer
  distribution is a demand-side object distinct from desired hours, concentrated
  at institutional standard hours (40h/week in the Dutch case), and empirically
  large relative to the desired-hours distribution.
  **Sources:** Bloemen 2000 [explicit hours-and-wage offer restrictions; joint
  offer density f(w,h); DP version, journal pages TBC]; Bloemen 2008 [explicit:
  hours-offer distribution concentrated at 40h (probability ≈0.55–0.57), far
  more concentrated than desired-hours distribution; access and preference
  separation needs external pin when only hours data available; *JoLE*
  26(1):137–179].
  **Do not overclaim:** Bloemen 2000/2008 model offers in a search-theoretic
  framework with Poisson arrivals; the JMP's access channel is an estimated
  static opportunity density, not an arrival-rate object. Do not cite Bloemen
  as evidence for the JMP's three-way access/ability/preference decomposition.
  Do not present the 40h concentration result as directly transportable to
  France 2015–2017.

## Policy Simulation

- **Claim:** RURO and discrete-choice labor-supply models are natural engines for
  tax-benefit policy simulation, but the JMP's first object is level inequality
  and opportunity decomposition, not reform evaluation.
  **Sources:** Aaberge & Colombino 2013 [explicit optimal-tax simulation];
  Aaberge, Dagsvik & Strom 1995 [background tax-reform/welfare lineage]; Bargain
  et al. 2013 [explicit welfare comparator]; Jacquet et al. 2026 [explicit
  tax-reform CV comparator]; JMP project state v1 [explicit paper boundary].
  **Do not overclaim:** Do not present the JMP as a country-ranking exercise or
  merely another tax-reform simulation.
