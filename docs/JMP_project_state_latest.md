# Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition

## Project State Document

**Author:** Hisham Haydar (LISER)
**Document class:** comprehensive project state and methodological record
**Date:** 2 June 2026
**Purpose:** A self-contained account of what the project is, what has been built and estimated, where the work currently stands, the precise nature of the welfare analysis, and the sequenced next steps. It is written so that a reader with no prior exposure to the project — a co-author, a supervisor, a referee, or the author returning after an interval — can reconstruct the full state of the work from this document alone.

---

## 1. Overview and research question

### 1.1 The question

The paper studies how unequal *job opportunities*, as distinct from heterogeneous *preferences*, shape the measurement and decomposition of money-metric well-being inequality, in a structural labour-supply model in which labour supply is modelled as choice among latent jobs. The central research question is:

> How much of observed inequality in money-metric well-being is attributable to unequal job opportunities rather than to heterogeneous preferences, once labour supply is modelled as choice among latent jobs?

Operationally, "job opportunities" resolve into two channels, so the decomposition is **three-way — access, ability, and preference** (wage technology = *ability*; market/job/hours/region/occupation availability = *access*; the earlier two-way "opportunity vs preference" phrasing is a shorthand for this finer cut, developed in §2.2, §3.3 and §6.1).

The motivating intuition is that standard labour-supply models, by representing behaviour as a choice over a fixed and common hours grid subject only to a tax-benefit budget, fold all systematic between-household differences in behaviour into *preferences*. If, in reality, households face *different feasible sets of jobs* — different distributions of available wages, hours packages, occupations, and participation possibilities — then a model that does not represent those differences will attribute opportunity-driven variation to taste-driven variation. The paper's premise is that a structural model with an explicit, estimated *opportunity density* over latent jobs can separate these two sources, and that the separation matters normatively: under the responsibility-sensitive view that individuals are not fully accountable for the jobs available to them, opportunity-driven inequality is compensation-relevant in a way that preference-driven inequality may not be.

### 1.2 Supporting sub-questions

1. To what extent do standard labour-supply models that do not model constrained opportunities overstate preference heterogeneity by absorbing opportunity differences into tastes?
2. How should money-metric well-being be computed when individuals face different feasible job sets?
3. Under the view that opportunities are not fully the individual's responsibility, how much well-being inequality is attributable to unequal opportunities, and how much remains attributable to preferences?
4. How sensitive is the decomposition to alternative money-metric well-being measures and to alternative definitions of the opportunity/responsibility boundary?

### 1.3 What the paper is not

The contribution is the *consistent treatment of opportunities* across three layers — structural estimation, money-metric welfare measurement, and inequality decomposition. It is **not** a country-ranking or "beyond-GDP" ranking exercise; cross-country and cross-year comparison is a possible later extension, not the object. It is also distinct from a separate, purely axiomatic theory paper (co-authored with François Maniquet) on jobs and well-being: the present paper is an empirical, empirically grounded paper that *imports* normative readings from that theory as cited primitives but does not reproduce or centre itself on the axiomatic derivations. The boundary is maintained deliberately and is discussed again in §6.3, because the welfare design draws on the theory paper's classification of measures.

### 1.4 Empirical setting

The empirical baseline is **France**, using French EU-SILC microdata processed through **EUROMOD** (input and output variables, system years 2015–2017). The estimation pools three cross-sections (2015, 2016, 2017); the working prototype is anchored on this pooled French sample. The sample comprises three estimation groups processed separately under type-conditional structure: single males, single females, and couples. At the production resolution the groups contain **2,243 single-male households, 2,764 single-female households, and 7,438 couple households** (12,445 households in total), the couples being the joint-decision unit described in §4. Extensions to other years (e.g. France 2021), other countries (e.g. Germany), and richer opportunity data are envisaged but explicitly deferred behind a credible baseline result.

---

## 2. Type of welfare analysis

This section answers, in detail, the question "what kind of welfare analysis are we doing?", because the answer determines every subsequent design choice.

### 2.1 Money-metric, preference-respecting, equivalent-income welfare

The welfare object is a **money-metric, preference-respecting equivalent income** in the tradition of King (1983) and, in its responsibility-sensitive form, Fleurbaey (2006, 2008) and Fleurbaey–Maniquet. For each household, welfare is the hypothetical income (or income-equivalent subsidy) that, evaluated under the household's *own* preferences, would equate the household's attained situation to a measure-specific *reference* situation. Two features distinguish this from naive income comparison. First, it respects preference heterogeneity: two households with the same consumption and leisure but different tastes are not assumed equally well off; each is evaluated against its own indifference map. Second, the *choice of reference* encodes a normative position on which dimensions of advantage are compensation-relevant and which are the individual's own responsibility.

This is precisely the architecture of the equivalent-income labour-supply literature, of which Bargain, Decoster, Dolls, Neumann, Peichl and Siegloch (2013, *Social Choice and Welfare*) is the canonical empirical statement. That paper estimates discrete-choice labour-supply models on harmonised EUROMOD microdata, retrieves preference heterogeneity, and computes a *family* of money-metric welfare measures — a "rent" metric (consumption at zero hours), a "rent + reference wage" metric (virtual non-labour income at a reference wage), and a "wage" metric (the wage equivalent at zero virtual non-labour income) — finding that cross-individual welfare rankings shift materially with the normative treatment of preference heterogeneity. The present paper's welfare layer is the same construction: a single estimated preference, a menu of references spanning a compensation–responsibility spectrum, and the spread across the menu as an object of interest.

### 2.2 The novel layer: opportunity-sensitivity

What distinguishes this paper from the Bargain et al. tradition is the addition of an explicit, estimated **opportunity density** over latent jobs, and the consequent ability to decompose welfare inequality into an opportunity component, an ability component, and a preference component. Bargain et al. and the broader equivalent-income literature have preference heterogeneity and a tax-benefit budget but treat the choice set as a fixed common hours grid; they do not model a household-specific feasible-job distribution. The latent-jobs / Random Utility Random Opportunity (RURO) framework — Aaberge, Colombino and Strøm (1999), Dagsvik (1994), Aaberge and Colombino (2018) — supplies exactly the missing object: a probabilistic representation of the jobs a household can access. Notably, Bargain et al. (2013) themselves flag the determination of country-specific choice opportunities and demand-side constraints on the choice set as a needed extension left for future research. The opportunity layer of the present paper is the implementation of that flagged extension, and the opportunity/preference decomposition is its empirical payoff.

### 2.3 The ex-ante stance

The welfare object is computed **ex ante**, that is, as the expected-maximum (inclusive-value) utility over the household's feasible opportunity set, rather than ex post as the utility of the single realised job. This choice is dispositive for an opportunity paper and is discussed formally in §5.1. The ex-ante object reflects the welfare of the feasible set a household faces; the ex-post object, conditioning on the realised job, structurally cannot carry the access channel that the paper exists to measure. The ex-post certainty-equivalent is retained only as a diagnostic cross-check.

### 2.4 The welfare unit

The unit of welfare is the **household**, with one welfare object per household, computed from joint utility over a joint budget. Couples are treated as a single decision-making unit (a "unitary" household in the Bargain et al. sense) and are never decomposed into two individual well-beings at the welfare stage. This is not equivalisation in the OECD sense — there is no division of income by a demographic equivalence scale — but a genuine joint money-metric. Intra-household distribution is a separate identification problem (it would require a collective model identifying individual preferences from a joint utility) and is deliberately out of scope; it is named as a boundary, not silently assumed away.

---

## 3. The structural model

### 3.1 The RURO / latent-jobs factorisation

The choice probability factorises as

$$
P(\text{job } j \mid \text{household } i) \;\propto\; \exp\big(v_{\text{type}}(j;\,\theta^{\text{pref}})\big)\cdot g(j;\,x_i,\theta^{\text{opp}}),
$$

where $v_{\text{type}}$ is the type-specific deterministic utility (preferences, group-specific) and $g$ is the opportunity density (a market primitive governing which jobs are available, shared in structure across groups — one economy). Operationally, on a sampled set of alternatives drawn from a proposal distribution $\pi$, the engine forms a per-alternative value

$$
V_{ij} \;=\; u_{ij} + \log h_{ij} + \log w_{ij} + \log\text{market}_{ij} - \log\pi(j;x_i),
$$

where $u$ is the deterministic utility, the $\log h$, $\log w$, $\log\text{market}$ terms are the opportunity-density components (hours, wage, and market/participation availability), and $-\log\pi$ is the mandatory **sampling-of-alternatives correction** (the proposal/prior correction). The household inclusive value is the log-sum $\text{lse}_i = \log\sum_{j} \exp(V_{ij})$. This same construction is reused, unmodified, in the welfare layer (§5).

### 3.2 Preferences (the utility block)

The deterministic utility is a **Box–Cox** specification in consumption and leisure, with leisure preferences shifted by demographic taste-shifters (age, presence of children) and gender. Box–Cox is the standard choice in this normative literature precisely because monotonicity and concavity conditions are checkable and tangency-based welfare metrics are well-defined on it. Consumption $c$ is locked to EUROMOD's standardised disposable income (the real, deflated `ils_dispy_real`). The preference block of the estimated parameter vector contains 20 parameters, comprising the leisure-preference baselines and demographic shifters for single males, single females, and the two couple legs, the consumption curvature for singles, and two pinned parameters (below).

### 3.3 Opportunities (the opportunity block)

The opportunity density $g$ governs which jobs are available and is the structural locus of the paper's novelty. It is organised into channels:

- a **wage** (ability) sub-block, with returns to education and experience (the Mincer-type wage technology) and a dispersion parameter $\sigma$ — 6 parameters;
- an **access** sub-block governing participation/employment availability and hours availability, with regional (region, GSUR/urbanisation), temporal (year), and occupation shifters — 23 parameters, comprising the employment and hours-availability parameters, the regional and urbanisation interactions, the year interactions, and six gender-specific occupation-availability parameters.

The distinction between the wage (ability) sub-block and the access sub-block is the operationalisation of the ability/opportunity cut discussed in §6.1.

### 3.4 The occupation channel — a precise statement

Occupation enters the **opportunity** layer only, never the utility layer, through six estimated gender-specific occupation-availability parameters in the access sub-block. It is represented by a four-category task variable (`loc4`) derived from EUROMOD's occupation field. This asymmetry — occupation in opportunity, not in utility or in the structural wage return — is a deliberate design choice. A terminological discipline is maintained throughout: `loc4` (occupation, derived from the ISCO-type field) is *never* referred to as sector or industry; the industry variable (`lindi`, NACE) is a distinct object reserved for a later robustness extension and is not in the baseline. Note that the *proposal* distribution's wage channel does carry an occupation-dependent mean (a calibrated occupation shifter), but this is a property of the importance-sampling instrument, not of the estimated structural wage return; the structural return is to education and experience only. Whether occupation should additionally enter the structural wage return is a named, deferred robustness specification (§6.2).

### 3.5 The certified baseline estimate

The certified baseline is the **47-parameter pooled specification** `joint_pooled_v1_bll0_tlmpin`, estimated jointly on the pooled French 2015–2017 sample, with couples at 901 alternatives (a $30\times30$ joint partner-marginal grid plus the chosen alternative) and singles at 101 alternatives. The estimation backend is JAX; an earlier GAMS/CONOPT path was abandoned after the JAX likelihood was validated to machine precision and found to be both far faster and the means of detecting a real engine bug in a Box–Cox derivative term. The parameter count of 47 arises from 49 structural parameters (29 shared opportunity + 20 group-specific preference) minus 2 data-justified pins:

- `beta_ll = 0`: the couples leisure-interaction term, weakly identified, is pinned to zero;
- `theta_l_m = -0.8`: the couples-male leisure curvature, unidentified on these data because the couples-male baseline leisure preference is effectively absent, is pinned to the curvature value that is stable across all other groups.

A further normalisation fixes the consumption scale (`beta_c = 1`), and the couples consumption curvature is set to zero. Both pins are implemented through a generic `fixed_params` YAML mechanism rather than hard-coded, preserving specification-agnosticism.

### 3.6 Identification, certification, and the standard of evidence

The baseline is **certified by a synthetic-recovery gate**, not merely by in-sample fit. The estimate is interior, the Hessian is positive definite on both synthetic and real data (synthetic minimum eigenvalues +1.706 / +1.532; real-data +0.459 / +0.408), two independent starting values agree, and — critically — the data-generating-process recovery test at the production resolution recovers the known synthetic parameters. The standard of evidence is deliberately higher than a positive-definite real-data fit, for a reason established by a closed investigation described next.

### 3.7 The gender-split investigation (closed; a methodological lesson on record)

A richer specification relaxing two opportunity parameters (`beta_E`, `beta_h_pt2`) to gender-specific values was entertained. A likelihood-ratio test *rejected* pooling (LR statistics 65.7 and 206.6, the latter with apparently opposite-signed male and female estimates), and the relaxed model fit better in-sample with a positive-definite real-data Hessian. Nonetheless, the synthetic-recovery gate returned **not certified**: three of four gender-split parameters failed to recover on synthetic data, exhibiting confident-but-wrong estimates (a tight-standard-error bias) that both the real-data fit and the LR test masked. A cheap non-identification diagnostic localised the failure: `beta_E` is a partial ridge (its gender contrast modestly identified, its level flat), while `beta_h_pt2` is an independent mislocation for which no reparameterisation helps — the "opposite signs" finding being an in-sample artefact, not an identified structure. The governing lesson, which now disciplines every prospective specification, is that **likelihood-ratio rejection of pooling does not establish recoverability of the split**: a specification is adopted only if it recovers on synthetic data, regardless of in-sample improvement. Consequently the 47-parameter shared specification remains the certified baseline, and the gender split is demoted to a robustness question to be revisited only if the decomposition proves sensitive to it.

### 3.8 Inference and standard-error structure

Inference is by **cluster-robust bootstrap** on the household identifier `idorighh` (the repeated-cross-section cluster key; roughly 20% of households appear in two of the three waves, none in all three). Asymptotic standard errors are not used for headline claims, because three parameters sit at their bounds (the couples-male leisure baseline at its floor, and two single-female leisure-age curvatures at their ceilings), where asymptotic standard errors are invalid. A reportable feature of the certified estimate, with direct consequences for the decomposition, is a **standard-error asymmetry**: the shared opportunity block is tightly estimated (21 of 29 parameters significant under clustered standard errors), while the singles-leisure preference block is wide (9 of 18 significant). The opportunity component — the paper's headline channel — is therefore precisely estimated, whereas the preference component carries wide uncertainty. This is identification with imprecision, not non-identification. A related fact, `beta_l0_m` at its floor, means the couples-male baseline leisure preference is effectively absent; this is a reportable economic finding and has a specific downstream consequence for the decomposition (§6.1).

### 3.9 Build facts material to the welfare layer

Several build-stage facts bear directly on the welfare work and are recorded for completeness. Consumption equals EUROMOD's standardised disposable income, deflated to a **2016-real** basis at the build stage (so consumption and wages share one price basis, with no double-deflation, verified). The 901-alternative couples grid and the 101-alternative singles grids are the production resolution; the draws constituting these grids *are* the importance-sampling proposal sample, each alternative carrying its own log-prior, so no separate McFadden correction is required. The proposal distribution is **partly individualised** (established by a dedicated audit, §5.3): its wage and occupation channels condition on household characteristics, while its hours and employment channels are common across households.

---

## 4. The household unit, in detail

Because the welfare unit is consequential and frequently misunderstood, it is stated explicitly. For a single-person household the unit is the individual. For a couple the unit is the household: a single welfare object computed from the couple's joint utility (defined over household consumption and both partners' leisure) over a joint budget (household disposable income at the joint labour-supply alternative). There is exactly one welfare object per couple; couples are never split into two individual objects, and no per-capita division is applied. This is verified as an integrity gate in the welfare implementation (§5.5). Within-couple gender enters only later, through the attribution rules of the decomposition, where the question of whose access is being equalised becomes live. The welfare model identifies a *household* preference, not two separable individual preferences; manufacturing individual well-beings would require an intra-household allocation rule the model does not contain. Intra-household distribution is therefore deferred as a distinct extension, not treated.

---

## 5. The welfare layer: design and implementation status

### 5.1 The welfare object and the family of measures

The frozen welfare-object design (the memo `JMP_welfare_spec_v5.md`, superseding four earlier versions) settles the welfare object as an **ex-ante, household-level, money-metric, preference-respecting equivalent income**, computed as a *family* of six measures $W^1,\dots,W^6$ that share a common computational core and differ only in the reference against which attained utility is converted to money.

The common core is the ex-ante inclusive value

$$
V_i \;=\; \log \sum_{j\in\mathcal C_i}\exp\!\big(v_i(c_j,\ell_j) + \log g(j;x_i) - \log\pi(j)\big),
$$

evaluated at the certified $\hat\theta$, with the mandatory $-\log\pi$ correction; the expectation over the extreme-value shocks is taken analytically (the log-sum is the closed-form expected maximum), so the welfare layer requires no shock draws and no simulated argmax. Each $W^k$ is then an equivalent-income object: the income or subsidy that equates $V_i$ to a measure-specific reference, evaluated under the household's own preferences, computed by a one-dimensional bracketing root-solve of the own-utility map (never by a closed-form shortcut that would bypass the household's preferences).

The six references span the compensation–responsibility spectrum, classified by their Independence-of-pay (Ind-$y$) and Independence-of-opportunity-set (Ind-$A$) properties:

| Measure | Reference / construction | Ind $y$ | Ind $A$ | Normative reading |
|---|---|---|---|---|
| $W^1$ | preferred job in own set, pay ignored | + | − | compensate pay; responsible for the set |
| $W^2$ | best-paid equivalent in own set | − | − | Full Responsibility |
| $W^3$ | laissez-faire in own set with pay | − | − | Full Responsibility (laissez-faire) |
| $W^4$ | staying-home equivalent (non-employment option) | + | + | Full Compensation |
| $W^5$ | uniform subsidy to reference ability set $\bar A$ | − | + | compensate the set; responsible for pay |
| $W^6$ | best job in the whole economy $\mathcal J$ | + | + | Full Compensation (+ Weak Responsibility) |

The endpoints are $W^2/W^3$ (Full Responsibility) and $W^4/W^6$ (Full Compensation); $W^1$ and $W^5$ are the two one-sided duals, which read the access/ability cut directly off the measure menu ($W^1$ compensates pay and holds the set responsible; $W^5$ compensates the set and holds pay responsible). A structurally important fact is that *all six measures read attained utility $V_i$*, so unequal access lowers welfare under every measure through attainment; the Ind-$y$/Ind-$A$ properties bite only in the *direct* evaluation channel, which is why a later decomposition is measure-dependent and must be anchored.

The ex-ante stance is the baseline because the ex-post chosen-alternative certainty-equivalent conditions on the realised job $j^*$ and therefore cannot carry the access channel; it is retained as a proposal-correction-free diagnostic cross-check only. De Palma–Kilani equivalent/compensating-variation objects are retained as secondary measures for comparability with the Aaberge–Colombino and related literatures; these too are analytic in the shocks.

### 5.2 Why a family rather than a single measure

The decision to compute and compare the whole family, rather than to select one measure and treat the others as robustness, is deliberate and is the paper's headline architecture: because the paper concerns *responsibility disagreement*, computing the family and exhibiting how the inequality picture moves along the compensation–responsibility spectrum is the empirical answer to sub-question 4. The architecture is configuration-driven — adding or removing a measure is a configuration change, not a code change — and the family-as-headline claim is treated as an empirical bet on the across-measure spread, to be confirmed only once that spread is observed. A build-order gate (§5.6) governs the sequence in which measures are validated and computed, precisely so that the headline is not asserted before the spread is seen. The precedent of Bargain et al. (2013), whose move from a "rent" to a "wage" criterion produced rerankings of at least 15 percentage points for 7 of 12 countries, gives reason to expect a material spread, though this remains to be established on the present within-France data.

### 5.3 The integration scheme and the proposal-individualisation audit

A central methodological question is how the inclusive-value integral is *evaluated*. Two estimators are defined:

- $\widehat V_i^{\text{IS}}$: **importance sampling over the existing estimation draws**, reweighted by the household-specific per-row prior $-\log\pi(j;x_i)$. This is the **primary** scheme.
- $\widehat V_i^{\text{dir}}$: a **redraw** estimator that draws integration nodes from the estimated individual opportunity density $\hat g(\cdot;x_i)$ directly (with the shocks still integrated analytically), retained as a **validation cross-check**.

The choice of $\widehat V_i^{\text{IS}}$ as primary rests on a dedicated read-only audit of the proposal distribution (`welfare_proposal_individualisation_check.md`). The audit established that the proposal $\pi$ is **partly individualised**: the wage channel draws from a household-specific mean ($\mu_i = X_i b + \delta_{\text{occ}}[\text{loc4}_i]$) and the occupation channel conditions on the gender$\times$education stratum, so $\log\pi$ varies across households for the same $(w,h)$ node; the hours channel (a fixed five-mode mixture) and the employment channel (a flat participation split) are common across households; the structural market block (region, urbanisation, year) resides in the utility-side density $g$, not in $\pi$. Because the two *individualised* channels (wage, occupation) are precisely the high-dispersion channels of the integrand, the importance-sampling divergence between $\hat g_i$ and $\pi$ is small on the dimensions that would otherwise dominate its variance, and the importance-sampling estimator is consistent (never in doubt) and additionally well-conditioned. The redraw estimator is therefore demoted from a co-primary to a cross-check, escalated to primary only on households flagged by an effective-sample-size gate (§5.6). The residual exposure is confined to the two common channels (hours, employment), which is exactly the exposure the effective-sample-size diagnostic is built to detect.

### 5.4 The implementation contract

The welfare implementation is governed by a frozen code-design contract (`RURO_welfare_scaffold_design_contract_v2.md`, superseding v1), which translates the v5 welfare-object memo into binding module boundaries, a configuration schema, a build order, and validation gates. The contract is explicit that the welfare path must reuse the *same* utility and opportunity-density construction as the estimator (one machine, not a re-implementation), so that $V_i$ at $\hat\theta$ is consistent by construction with the likelihood that produced $\hat\theta$. It draws the welfare-versus-decomposition scope boundary (the welfare layer is Exercise A; the source decomposition is Exercise B, deferred to its own contract); it requires every specification-identifying value to be read from configuration (zero hard-coded country/year constants, the agnosticism test); and it specifies the decomposition-readiness interfaces the welfare outputs must expose without implementing the decomposition.

### 5.5 Stage One: the W^3 welfare core, built and validated

Stage One built the welfare machine and validated it on $W^3$ (the Full-Responsibility laissez-faire measure), chosen as the first case because it pre-absorbs nothing and therefore stresses the core, the inversion, and the inequality machinery without measure-side compensation masking a defect. The results, on the full production sample (12,445 households, 901-alternative couples):

- **Engine parity (the "one machine" guarantee made falsifiable).** The welfare core's implied likelihood at $\hat\theta$ reproduces the estimator's own negative log-likelihood to **machine precision** ($\max|\Delta| = 0$ for all three groups on production data; $1.1\times10^{-13}$ on the smoke sample). This establishes that $\widehat V_i^{\text{IS}}$ *is* the estimator's household inclusive value, not an approximation of it.
- **Inversion sanity.** For every household the $W^3$ reference recovers zero welfare exactly, the inversion is monotone, and the bracketing solve converges (zero non-convergences across all 12,445 households).
- **Household-unit integrity.** Exactly one welfare object per couple from joint utility and joint budget; no per-capita split; type-conditional references for the three groups.
- **Reference coverage.** $W^3$'s laissez-faire reference lies in the household's own set, so the required consumption values are already present; no EUROMOD evaluation of out-of-set reference packages is required for $W^3$ (this exposure arises only for $W^5$/$W^6$, §5.7).

A consequence of validating on $W^3$ is that the resulting equivalent income is $\Omega_i \approx 0$ for every household, and hence the inequality of $\Omega^3$ is degenerate (Gini $= 0$). This is *correct by construction*: the laissez-faire equivalent income of a household evaluated against its own feasible set is identically zero, because no counterfactual reference is imposed; non-trivial $\Omega$ variation arises only once a decomposition imposes an equalised channel, which Stage One does not implement. The $W^3$ distribution and its inequality computed at this stage are therefore explicitly internal validation artefacts, not welfare findings.

### 5.6 The effective-sample-size finding (the binding empirical result so far)

The importance-sampling diagnostic computes, per household, the effective sample size $\text{ESS}_i = (\sum_s \omega_{is})^2 / \sum_s \omega_{is}^2$, where $\omega_{is} = \exp(V_{is} - \text{lse}_i)$ are the within-household model-implied probabilities — which, it should be emphasised, are *already* the predicted choice probabilities at $\hat\theta$, computed and validated for every household and every existing draw. The production ESS distribution returned a split verdict that is the single most consequential empirical result of the welfare work to date:

| Group | $N$ | ESS median | ESS min | ESS $p_{05}$ | $N(\text{ESS}<30)$ | share |
|---|---|---|---|---|---|---|
| single male | 2,243 | 20.3 | 1.73 | 6.5 | 1,918 | 85.5% |
| single female | 2,764 | 18.8 | 1.58 | 5.7 | 2,493 | 90.2% |
| couples | 7,438 | 63.2 | 1.79 | 16.4 | 1,285 | 17.3% |

The pattern is economically interpretable and consistent with the proposal audit. Couples, integrated against the rich $30\times30$ joint grid, are healthy (median ESS 63 of 901). Singles, on the 101-alternative marginal grids, are thin (median ESS $\approx 20$), with 85–90% of single households below the threshold of 30 and minima below 2 — meaning that for some single households the effective number of contributing draws is of order one, where the log of an importance-weighted sum carries finite-sample bias of exactly the kind that distorts a welfare distribution and the inequality measure built on it. The thinness traces to the audit's finding that the hours and employment proposal channels are common rather than individualised, leaving singles without the joint-grid dispersion that protects couples.

The consequence for the design is precise: the redraw cross-check $\widehat V_i^{\text{dir}}$, which had been reserved as a precaution, is **promoted from precaution to precondition** for the singles welfare distribution. Because 85–90% of singles fall below threshold, the cross-check is designed to run on the *full* singles samples (a blanket cross-check being cleaner than a near-total conditional one), while couples are cross-checked on the genuine sub-threshold flag of 1,285 households. A complementary existing-node subsample-stability probe corroborates the picture: median drift falls monotonically toward zero as the node count grows (the integral stabilises for the bulk), while the maximum drift persists at roughly 1.3–2.5 and does not collapse with the median — the persistent tail being the low-ESS households, exactly the set the redraw cross-check exists to vet.

### 5.7 The redraw cross-check and the EUROMOD-on-nodes boundary (current frontier)

Computing $\widehat V_i^{\text{dir}}$ requires the disposable income $c_{is}$ at each *redrawn* node $(w,h)$, which is an EUROMOD output. A first feasibility increment concluded that producing these consumptions required a wholesale rebuild of the EUROMOD inputs and was therefore blocked by the contract's prohibition on wholesale reruns. A re-audit overturned this conclusion on better evidence: the engine-ready parquet that the first increment inspected is a stripped, estimation-facing slice retaining about ten variables, but the **storage-level priced-long files** (`fr_p3a_bpool_priced__{year}__{mode}.parquet`) retain the **full EUROMOD input schema** (122–128 variables across the three years) and the stored disposable income for all six year×mode combinations. Redrawn-node input records can therefore be built by a **bounded template overwrite** — taking a household's existing input record, overwriting only the decider's choice variables, and preserving the non-decider roster — rather than a wholesale rebuild. The redraw machinery itself is built for both singles and couples (couples constructed jointly from per-partner covariates, mirroring the estimator's channel structure rather than stapling two singles draws).

A safeguard analogous to the Stage-One engine-parity gate was imposed before any redrawn node is priced: the template-overwrite EUROMOD path must first reproduce the build's *stored* consumption on *existing* nodes to machine tolerance. This **reprice-parity check currently fails**: on a 2016 singles smoke (100 rows), the median absolute difference is exactly 0 (the path is fundamentally correct for the large majority) but 8 of 100 rows exceed tolerance, with a maximum discrepancy of about 422 euros. A draw-identifier-stamping fix reduced the failures from 21/100 to 8/100, localising part of the cause to record-handling mechanics; a residual gap remains, attributable provisionally to chunk-runner preprocessing that the reprice path does not yet replicate. In strict conformity with the safeguard, **no redrawn node has been priced against this unvalidated path**: $\widehat V_i^{\text{dir}}$ remains uncomputed, the escalation set is empty (the trigger cannot fire without $\widehat V_i^{\text{dir}}$ values), and the draw-multiplier stability gate is deferred behind the same parity requirement. The reprice failure is *not yet diagnosed* as either a uniform preprocessing omission (shrinkable by replicating the missing step) or a structural household-type defect (which would mean the cross-check is unreliable for that type); this diagnosis is the immediate next task (§7).

### 5.8 Validation-gate summary

| Gate | Object | Status |
|---|---|---|
| Engine parity (one machine) | $\widehat V_i^{\text{IS}} = \text{estimator lse}$ | **PASS** (machine-exact, all groups) |
| Inversion sanity ($W^3$) | reference recovers zero; monotone; converges | **PASS** (all 12,445 households) |
| Household-unit integrity | one object per couple; joint; no split | **PASS** |
| Reference coverage ($W^3$) | own-set consumption present | **PASS** (no $\bar A/\mathcal J/o$ exposure for $W^3$) |
| ESS diagnostic | per-household effective sample size | **COMPUTED**; singles thin, couples healthy |
| Draw-growth stability | $\widehat V_i^{\text{IS}}$ stable as draws grow | **DEFERRED** (feasible via template overwrite; behind parity) |
| Redraw cross-check ($\widehat V_i^{\text{dir}}$) | $\lvert \widehat V_i^{\text{dir}}-\widehat V_i^{\text{IS}}\rvert$ on flagged set | **BLOCKED** on reprice parity |
| EUROMOD-on-nodes feasibility | bounded template overwrite | **FEASIBLE**; **reprice parity FAILS** |

---

## 6. The decomposition (Exercise B): design status

### 6.1 The ability/opportunity/preference cut

The decomposition attributes welfare inequality to three channels, by equalising a channel to a reference environment, recomputing the welfare distribution through the same core, and measuring the inequality fall, with components combined in a Shapley–Shorrocks, order-independent manner that exhausts total inequality. The channel membership — the cut — is an *identifying normative assumption*, not an empirical finding, and the decomposition number is conditional on it. The settled allocation is: education and experience (the wage-technology parameters) are **ability**; age is **preference**; gender is **circumstance** on the offer side (access/compensation-relevant) but **preference** through leisure; region, urbanisation, and year are **access**; occupation enters **access** through the gendered offer parameters. The configuration encodes this as 20 preference, 6 ability, and 23 access parameters.

A specific consequence of the certified estimate must be carried into the decomposition. Because the couples-male baseline leisure preference is at its floor and two couples preference parameters are pinned, the couples *preference* component is mechanically compressed, which — if not handled — would inflate the couples *opportunity* share relative to singles for a non-structural reason. The welfare outputs are therefore required to keep singles and couples opportunity shares separable (never pre-pooled into a single opportunity-share headline), and the decomposition must specify whether pinned preference parameters are held or swapped for the reference preference under preference-equalisation, since that choice sizes the couples preference component. These are interface requirements already exposed by the welfare layer; the decomposition itself is not yet implemented.

### 6.2 Status and dependence

The decomposition is **deferred**, by design, behind a validated welfare layer; it requires its own prose-first design memo (`JMP_decomposition_spec_v1.md`) before implementation, and that memo is best written against an *observed* welfare spread rather than an anticipated one. The welfare-versus-decomposition boundary is held as a structural guard because the measure stance (Exercise A) and the decomposition channel (Exercise B) are the same normative cut operationalised two ways and must not be double-interpreted. An elegant internal check is available but is explicitly *not* a numerical gate: the $W^1$/$W^5$ duals read the access/ability cut off the measure menu, and should tell a story consistent with the decomposition's access/ability components, but because the measures are different money metrics with different references there is no theorem equating their inequality gap to any single measure's components; the dual is corroborating interpretation, not a reconciliation identity.

### 6.3 Deferred robustness specifications

Two estimation-side robustness specifications are named, deferred, and subordinated to the baseline, each gated on synthetic recovery before adoption (the discipline of §3.7): (i) an occupation-interacted *structural* wage return, distinguishing a calibrated proposal shifter from a prospective estimated structural return; (ii) the ability/access re-allocation, with education-as-access as the focal alternative cut and the decomposition's sensitivity to it as the quantity of interest. The industry variable (`lindi`, NACE) is reserved as a further extension. The gender split (§3.7) is a third robustness axis, to be revisited only if the decomposition proves sensitive to it.

---

## 7. Where we stand, and the next steps

### 7.1 Current position, in one paragraph

The structural model is estimated and certified: a 47-parameter pooled RURO labour-supply specification on pooled French 2015–2017 EUROMOD data, with preferences in a Box–Cox utility block and opportunities in an estimated density with wage (ability) and access sub-blocks, certified by synthetic recovery and not merely by in-sample fit. The welfare layer is designed (a frozen six-measure ex-ante money-metric family) and its computational core is built and validated to machine precision on the Full-Responsibility measure $W^3$; the predicted choice probabilities at $\hat\theta$ are computed and validated for every household. The binding open issue is that the importance-sampling welfare integral is thin for single-person households (median effective sample size near 20 of 101, 85–90% below threshold), which makes the redraw cross-check a precondition rather than a precaution for the singles welfare distribution; the redraw is feasible via a bounded EUROMOD template-overwrite, but its reprice path does not yet reproduce the build's stored consumption to tolerance (median exact, an 8% tail), and that parity must pass — and be diagnosed as uniform rather than structural — before any single welfare number is produced. No welfare finding has been produced; no decomposition has been implemented.

### 7.2 Immediate next step

Diagnose and close the EUROMOD reprice-parity gap. The first task is *diagnostic, not corrective*: characterise the failing rows before changing any reprice logic, determining whether they are a few households at many nodes or many households at scattered nodes, whether they share a covariate or roster signature (self-employment income, benefit components, dependants, year-specific schema fields), and hence whether the failure is **uniform** (a preprocessing step omitted for all rows, shrinkable by replicating it) or **structural** (a household type the overwrite mishandles). Only then replicate the specific missing preprocessing, and re-run parity across the *full* year×mode grid the production run will touch (2015/2016/2017 × singles/couples), not only the 2016 singles smoke cell, since schemas differ by year and the couples joint two-decider overwrite is untested for parity. Parity must pass to machine tolerance on every cell the production run will touch.

### 7.3 The fork the diagnosis determines

The diagnosis settles which of two futures the singles results inhabit. If the failure is **uniform** and parity passes on all cells, the reprice path is trustworthy and the next authorisation is the bounded production $\widehat V_i^{\text{dir}}$ run — full singles and flagged couples — which finally produces the $\lvert\widehat V_i^{\text{dir}}-\widehat V_i^{\text{IS}}\rvert$ distributions and the per-household escalation decision, clearing the singles welfare distribution for promotion from validation artefact to result. If the failure is **structural** and concentrated in a household type, that is a more consequential finding: it would mean the cross-check is itself unreliable for that type, and since the low-effective-sample-size singles are exactly where the cross-check is load-bearing, it would force a candid reconsideration of whether the singles welfare distribution can be certified under importance sampling alone, or whether the honest claim is couples-certified with singles carrying an explicit coverage caveat.

### 7.4 The sequence beyond the parity gate

Conditional on a validated reprice path and a separate production authorisation, the ordered remaining work is: (i) the bounded production $\widehat V_i^{\text{dir}}$ run and the draw-growth stability gate, clearing the two outstanding welfare-integration blockers; (ii) promotion of $W^3$ from validation artefact to result and extension of the family to $W^5$ and the endpoints, at which point the $\bar A/\mathcal J/o$ reference-coverage gate becomes live and the bounded EUROMOD evaluation of out-of-set reference packages — dormant for $W^3$ — must be confronted, and the across-measure welfare spread (the empirical bet on which the family-as-headline thesis turns) is observed for the first time; (iii) the decomposition design memo, written against the observed spread, followed by the decomposition implementation with its Shapley-exhaustiveness gate and per-component cluster-robust confidence intervals (anticipated tight for the opportunity component, wide for the preference component, per the standard-error asymmetry); (iv) the deferred robustness specifications, each gated on synthetic recovery. Throughout, the governing principles hold: one change, one gate, read the result, decide the next step; validation gates before any distribution is trusted; no module stacked on an unvalidated module; and every prospective specification gated on synthetic recovery rather than in-sample fit.

---

## 8. Methodological principles on record

For the benefit of a reader reconstructing the project's working method, the following principles have governed the work and explain the structure of the artefacts:

1. **Synthetic recovery is the standard of evidence**, above in-sample fit and above likelihood-ratio rejection of a simpler model. The gender-split episode is the demonstration: a better-fitting, LR-favoured, positive-definite specification was rejected because it did not recover on synthetic data.
2. **Falsifiable parity gates** are imposed at every layer boundary where a re-implementation could silently diverge from a validated reference — the welfare core against the estimator likelihood (passed, machine-exact), and the EUROMOD reprice path against the build's stored consumption (currently failing, correctly blocking).
3. **One increment, one gate, read, decide.** Each step produces a single artefact, validated by a single gate, reviewed before the next step is authorised. Feasibility of a path is never authorisation to run it at production scale.
4. **Specification-agnosticism.** Every country/year/specification-identifying value lives in configuration, not in source; the welfare and decomposition code is a measure machine pointed at a certified estimate and an engine-ready dataset, so the current French 2015–2017 baseline is an input, not a constant.
5. **Honest blocking over silent approximation.** Where an input or a path is unavailable, the affected objects are reported blocked with exact counts and never approximated, interpolated, or faked.

---

*End of document.*
