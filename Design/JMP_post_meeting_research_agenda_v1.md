# JMP Post-Meeting Research Agenda v1

**Working title:** *Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition*  
**Date:** 29 August 2026  
**Principal investigator:** Hisham Haydar  
**Supervisor:** François Maniquet  
**Status:** **WORKING MEMO — NOT A FROZEN SPECIFICATION, NOT A MISSION CHARTER, NOT A MANUSCRIPT RESULT**

---

## 0. Purpose of this memo

This memo consolidates the substantive questions raised in the meeting with François, the current empirical status of the France application, and the next research priorities for the Job Market Paper.

It is intended to perform four functions:

1. define the scientific work that remains before the JMP specification can be selected;
2. distinguish exploratory specification work from manuscript-grade certification;
3. preserve a coherent empirical and normative research strategy;
4. prevent the project from being displaced by excessive documentation, software review, or repeated certification of provisional experiments.

The memo should be updated only when a major scientific decision changes. Routine prompts, action cards, progress summaries, debugging notes, and exploratory results should not generate additional permanent governance documents.

---

# 1. Core JMP question and final empirical scope

## 1.1 Main research question

The final paper should answer:

> **How much of inequality in money-metric well-being among working-age households is attributable to heterogeneous preferences, and how much is attributable to the broad non-preference environment—especially unequal job access and wage opportunities—when labour supply is modelled as choice among latent jobs?**

The paper should then decompose the broad non-preference environment further into:

- **access:** employment, hours, occupation, and other job-availability channels;
- **ability / wage technology:** wage-offer location and dispersion, including education and experience returns;
- **endowments / needs / background:** heterogeneous budget components that are neither preferences nor job opportunities.

The decomposition is structural and model-conditional. It is not a causal decomposition and it is not automatically a moral decomposition into “responsibility” and “unfairness.”

## 1.2 Final empirical population

The intended final JMP should include:

1. **single-adult households;**
2. **couple households;**
3. a combined well-being inequality analysis across both household types.

The existing France 2016 singles application is the completed prototype and first empirical module. It establishes the estimation, inference, pricing, welfare, and decomposition architecture. It should not be treated as the final population of the paper.

## 1.3 Unit of welfare for the final paper

The baseline plan is:

- one joint household money-metric welfare value for couples;
- household-level structural choice and joint disposable income;
- household-weighted inequality as the baseline;
- person-weighted or equivalence-scale sensitivity as a robustness exercise.

A full collective or bargaining model is outside the immediate JMP baseline unless later evidence shows that the unitary household model is untenable.

---

# 2. Current empirical status

## 2.1 Current completed module

The current France 2016 singles module contains:

- 1,555 single-adult households;
- 101 alternatives per household;
- EUROMOD-priced disposable incomes;
- corrected marginal proposal-density treatment;
- a converged RURO estimate;
- clustered parameter inference;
- a common-opportunity RUM benchmark;
- post-estimation fit diagnostics;
- a money-metric welfare layer;
- a Shapley-style decomposition;
- the LOC4 occupation-conditioned wage specification;
- ongoing randomized-QMC final numerical-precision work.

## 2.2 Current preferred structural model

The current preferred structural specification is LOC4.

The original model already contained occupation availability:

\[
g_i^{Occ}(o),
\]

which determines how the probability of receiving a job varies across occupation categories.

The baseline wage density was common across occupations:

\[
\log w \mid X_i \sim N(X_i\beta,\sigma^2).
\]

LOC4 replaces this with four occupation-conditioned wage distributions:

\[
\log w \mid X_i,o=k
\sim
N(X_i\beta+\delta_k,\sigma^2),
\]

with one omitted occupation category and three estimated location shifts.

LOC4 therefore gives four occupation-conditioned wage distributions, but not four unrestricted wage equations. Education and experience returns and the wage dispersion remain common across occupations.

## 2.3 Current regional structure

At present, regional variables enter only the employment-access margin \(g^E\).

The existing regional variables are:

- group unemployment rate (GSUR);
- NUTS-1 indicators;
- urban and medium-density indicators, with rural omitted.

They affect the relative availability of employment versus non-employment. They do not currently enter:

- conditional hours opportunities \(g^H\);
- occupation availability \(g^{Occ}\);
- wage technology \(g^W\);
- preferences \(u\).

The current evidence indicates that GSUR is the active regional employment-access signal, while NUTS-1 and urbanisation indicators do not reject jointly conditional on GSUR. This does not establish that geography is irrelevant for wages, occupations, conditional hours, commuting, or cost of living; those channels have not yet been modelled.

## 2.4 Current welfare status

Household-level money-metric welfare and welfare inequality have been computed for the singles prototype. The current decomposition contains:

\[
I(W)=\phi_A+\phi_B+\phi_P+R_{\mathrm{bg}},
\]

where:

- \(\phi_A\): access contribution;
- \(\phi_B\): ability / wage-technology contribution;
- \(\phi_P\): preference contribution;
- \(R_{\mathrm{bg}}\): fixed-background/endowment/needs contribution.

Under LOC4, access is currently the largest component and the ordering

\[
\phi_A>\phi_B>\phi_P
\]

is profile-stable. The ability component is small and its sign is not resolved over the wider conventional 95% profile region. Final RQMC precision remains pending, so exact preferred-arm magnitudes are not yet final JMP results.

---

# 3. Operating principle: exploratory research versus certification

## 3.1 Exploratory work

An exploratory specification may proceed without a mission charter, deputy ruling, independent software review, or acceptance chain when it:

- preserves accepted artifacts;
- writes to a separate experiment directory;
- changes neither package `main` nor the MNL package pin;
- is labelled provisional;
- is not inserted into the manuscript as an accepted result.

Each exploratory specification should retain only:

1. one specification/configuration file;
2. one machine-readable run manifest;
3. one comparison row in a common model-comparison table;
4. one concise interpretation note, if needed.

## 3.2 Candidate specification

A specification becomes a candidate for the paper only if it:

- materially improves fit or resolves an economically important misspecification;
- has acceptable convergence and local identification;
- produces economically plausible implications;
- does not create an unresolved channel-identification problem.

At that point it receives one bounded review.

## 3.3 Manuscript-grade accepted specification

Full inference, welfare integration, independent review, and acceptance are required only for the selected positive specification and the principal robustness model.

The programme should not certify every discarded experiment.

---

# 4. Post-meeting singles specification sprint

The current LOC4 model is the benchmark, labelled \(S0\).

The specification sprint should be executed as one experiment family, not as twelve separate missions.

## 4.1 Invariance diagnostic: age normalization

### Current definition

\[
a_i=\frac{age_i-\overline{age}}{10}.
\]

### Proposed alternative

\[
a_i^{min}=\frac{age_i-\min(age)}{10}.
\]

These are related by a constant shift. With a quadratic age profile,

\[
b_0+b_1a_i+b_2a_i^2,
\]

the same economic function can be represented exactly under either centering convention by transforming the coefficients.

### Required test

1. analytically transform the existing coefficients;
2. verify unchanged objective, probabilities, marginal utilities, MRS values, and indifference curves;
3. then re-estimate with relaxed or removed quadratic-age bounds.

### Scientific issue

Changing the centering is a reparameterization. Relaxing the age-curvature bounds is the substantive specification change. The two operations must not be conflated.

### Candidate

- **S1:** minimum-age centering with exact coefficient transformation;
- **S2:** minimum-age centering plus relaxed age-curvature bounds.

---

## 4.2 Invariance diagnostic: leisure normalizer

The model uses:

\[
l_{ij}=80-h_{ij},
\]

and a scaled leisure argument \(l/\Lambda_l\).

Changing \(\Lambda_l\) should primarily change units. If the leisure-weight coefficients are transformed consistently, the objective, probabilities, MRS, and indifference curves should remain unchanged.

### Required test

Evaluate:

\[
\Lambda_l\in\{10,40,45\}
\]

with the exact coefficient transformation and verify:

- objective equality;
- probability equality;
- MRS equality;
- identical indifference curves.

If economic implications change, investigate:

- active coefficient bounds;
- incorrect coefficient transformation;
- absolute-utility normalization in welfare;
- coding inconsistency.

### Substantive distinction

Changing \(\Lambda_l\) is not the same as changing the total time endowment \(80\). A different time endowment changes actual leisure and therefore changes the economic model.

### Required post-estimation output

Report the compensating consumption required for one additional weekly work hour:

\[
MRS_{h,c}
=
\frac{\partial u/\partial l}{\partial u/\partial c},
\]

by:

- sex;
- age;
- children;
- consumption quantile.

This is more informative than comparing raw coefficient magnitudes.

---

## 4.3 Explicit 35-hour opportunity peak

The current structural reference category is the complement of the four explicit hours bands. It contains the statutory 35-hour interval and other uncovered hours intervals. Therefore, the 35-hour alternatives are in the choice set, but the 35-hour peak is not separately parameterized.

### Candidate specification

Add:

\[
\beta_{35}D_{35}(h)
\]

to the hours-opportunity density, where \(D_{35}\) is a pre-specified narrow statutory-hours interval.

Retain another background category as the normalization.

### Candidate

- **S3:** current LOC4 plus an explicit 35-hour opportunity peak.

### Required output

- observed versus predicted 35-hour share;
- full fine-hours distribution;
- objective improvement;
- change in hours-opportunity parameters;
- change in preference parameters;
- convergence and active bounds.

A true mixed discrete-continuous atom at exactly 35 hours is deferred unless the narrow-band specification remains inadequate.

---

## 4.4 Children in male preferences

The current specification allows children to shift female leisure preferences but not male leisure preferences.

### Candidate

Add:

\[
\beta_{l,nkids,sm}nkids_i
\]

for single men.

- **S4:** current LOC4 plus a male children leisure-preference shifter.

### Evaluation

- sample size and number of single fathers;
- coefficient precision;
- effect on male employment and hours fit;
- effect on female child-shifter stability;
- effect on preference/opportunity attribution.

For couples, children should eventually enter both spouses’ preference equations, potentially by child age group.

---

## 4.5 Richer education specification

The current three-category education grouping may be too coarse.

### Primary variables

Use highest-attained education:

- `deh`;
- `dehde`;
- possibly `dey` as a coarse trend or spline.

Do not use current-attendance variables `dec` and `decde` as the primary measure of adult skill.

### Required preliminary table

For every detailed education category, report:

- unweighted count;
- survey-weighted share;
- employment rate;
- observed wage distribution;
- occupation distribution;
- sex composition.

### Candidate grouping

A possible five-group structure is:

1. less than upper secondary;
2. upper secondary;
3. post-secondary non-tertiary;
4. short-cycle/Bachelor;
5. Master/Doctorate.

General and vocational upper-secondary distinctions should be considered if cells are sufficiently large.

### Candidate

- **S5:** richer highest-attained education basis in the wage block.

Education detail may subsequently enter occupation availability, but should not be added to multiple channels simultaneously before the wage specification is assessed.

---

## 4.6 Education in preferences

Education may affect tastes over consumption and leisure, but this creates a stronger identification problem if education also enters the wage-opportunity block.

### Candidate

Add one parsimonious education shifter to the leisure-preference index.

- **S7:** one education preference shifter, diagnostic only.

### Evaluation

- objective improvement;
- Hessian conditioning;
- correlation with education wage coefficients;
- stability of hours-opportunity coefficients;
- stability of decomposition;
- comparison with common-opportunity RUM.

Education in preferences should be retained only if it materially improves fit and does not destabilize the separation between tastes and wage opportunities.

---

## 4.7 Consumption curvature near logarithmic utility

The current consumption curvature is close to zero, implying a near-logarithmic utility shape.

This does not mean that consumption is unimportant. The consumption coefficient is the utility numeraire; the curvature parameter controls shape.

### Candidate

Estimate:

\[
\theta_c=0
\]

using exact log utility.

- **S6:** current LOC4 with exact-log consumption utility.

### Evaluation

- likelihood difference;
- profile likelihood around zero;
- parameter stability;
- fit stability;
- welfare and decomposition stability for the final candidate only.

A translog utility specification remains a later robustness, not the first response to a near-zero Box-Cox curvature estimate.

---

## 4.8 Combined candidate

- **S8:** combined singles candidate containing only changes that are individually supported.

S8 should not mechanically include every modification. The inclusion rule is:

- economic relevance;
- fit improvement;
- convergence;
- local identification;
- predictive improvement;
- channel interpretability;
- parsimony.

Full welfare analysis should be run for \(S0\) and \(S8\), not for every intermediate exploratory model.

---

# 5. Wage proposal and wage-opportunity design

## 5.1 Computational proposal \(q\)

The proposal distribution is a numerical device. With exact \(-\log q\) correction, it should affect efficiency rather than the population estimand.

Candidate proposal designs:

\[
q_W(w\mid o),
\]

\[
q_W(w\mid h),
\]

\[
q_W(w\mid o,h).
\]

Evaluate using:

- effective sample size;
- importance-weight tails;
- optimizer stability;
- seed stability;
- welfare-integration precision.

Proposal changes must not be interpreted as economic changes.

## 5.2 Structural wage density \(g^W\)

A structural extension may allow wage location to depend on occupation and hours:

\[
\mu_{ioh}=X_i\beta+\delta_o+\kappa_h.
\]

The preferred first test is additive occupation and hours shifts. A full occupation-by-hours interaction should be considered only if the additive structure is clearly rejected and the data support the additional parameters.

This work should follow selection of S8 because it may require new alternatives and EUROMOD pricing.

---

# 6. Regional and external-data identification agenda

## 6.1 First feasibility question: available geography

Before adding any external regional variable, establish the finest geography that can be validly merged to the household data:

- NUTS-1;
- NUTS-2;
- department/NUTS-3;
- employment zone;
- commune/employment basin;
- urbanisation category only.

The value of external regional data depends on the merge key. If the household data support only NUTS-1, fine local labour-market variables must be aggregated and will provide limited independent variation.

## 6.2 Candidate official sources to audit

The audit should be limited to:

1. France Travail BMO recruitment-needs data;
2. French Labour Force Survey / EU-LFS desired-hours and underemployment information;
3. INSEE employee wage and occupation data, including DADS/Base Tous Salariés where accessible;
4. INSEE employment-zone job density, employment concentration, sectoral structure, and commuting indicators.

For every source, record:

- years;
- geographic resolution;
- access conditions;
- merge key available in the JMP data;
- variable definitions;
- sample/cell sizes;
- candidate structural channel;
- simultaneity and sorting risks;
- possible use: covariate, offset, auxiliary moment, validation target, or instrument candidate.

## 6.3 Channel assignment

Every external variable must be assigned before estimation.

### Employment access

Possible variables:

- local job density;
- employment concentration;
- lagged vacancy/recruitment intensity;
- commuting accessibility.

These enter:

\[
g^E.
\]

### Occupation access

Possible variables:

- region-by-occupation recruitment demand;
- local occupation/sector shares;
- occupation-specific vacancy difficulty.

These enter:

\[
g^{Occ}.
\]

### Wage technology

Possible variables:

- region-by-occupation wage distributions;
- regional wage location;
- regional wage dispersion.

These enter:

\[
g^W.
\]

### Hours access

Possible variables:

- regional part-time/full-time distributions;
- underemployment and desired-hours moments;
- occupation-specific hours distributions.

These discipline:

\[
g^H.
\]

### Preferences

Regional variables should not enter preferences in the baseline regional extension. Doing so would weaken identification unless a clear exclusion strategy or external moment is available.

## 6.4 Identification strategy

External data should preferably discipline opportunity-side objects rather than merely add more covariates to the same choice likelihood.

Possible strategies include:

- fixed external offsets;
- penalized/joint estimation;
- simulated minimum distance;
- auxiliary moments;
- external validation.

A generic objective is:

\[
\widehat\theta
=
\arg\min_{\theta}
\left[
-\ell_{\mathrm{household}}(\theta)
+
\lambda
\left(m_{\mathrm{external}}-m_{\mathrm{model}}(\theta)\right)'
W
\left(m_{\mathrm{external}}-m_{\mathrm{model}}(\theta)\right)
\right].
\]

## 6.5 Priority order

1. desired-hours/underemployment moments to distinguish preferences from hours constraints;
2. regional occupation demand to discipline occupation access;
3. external occupation-region wage distributions to discipline wage technology;
4. job density and commuting variables to strengthen employment access.

If only broad NUTS-1 variation can be merged, the exercise should be described as a structural robustness analysis rather than strong external identification.

---

# 7. Unobserved heterogeneity

The current model includes:

- random-utility shocks;
- wage-offer dispersion;
- observed heterogeneity in preferences;
- observed heterogeneity in opportunities.

It does not yet estimate rich household-specific random preference coefficients or random opportunity intensities.

Possible later extensions include:

\[
\beta_{l,i}=X_i\beta_l+\sigma_l\eta_i,
\]

or a two-class latent preference model, and separately:

\[
\log g_i^E=X_i\gamma+\sigma_g\nu_i.
\]

Preference and opportunity heterogeneity should not be made random simultaneously in the first extension. From one cross-section, these mechanisms can generate similar choice patterns and may be weakly identified.

Priority:

1. finish the observable specification;
2. implement couples;
3. estimate one two-class preference model as a robustness;
4. estimate one separate opportunity-intensity random-effect diagnostic;
5. consider joint random heterogeneity only with additional identifying information.

---

# 8. Couples as a core JMP module

## 8.1 Choice-set design

Use approximately 100 **joint household alternatives**, not 100 alternatives per spouse followed by a Cartesian product.

For household \(i\), sample:

\[
(j_{mi}^{(s)},j_{fi}^{(s)}),
\qquad s=1,\ldots,100.
\]

The proposal must cover:

- neither spouse works;
- man works only;
- woman works only;
- both work.

The observed joint alternative must always be included.

## 8.2 Household model

The baseline couple utility is:

\[
u_i
\left(
c_i(j_m,j_f),
l_{mi}(j_m),
l_{fi}(j_f)
\right),
\]

with joint disposable income priced through EUROMOD.

The first couple model should be parsimonious:

- unitary household utility;
- spouse-specific leisure preferences;
- joint consumption;
- spouse-specific job opportunities;
- children in both preference equations;
- no bargaining heterogeneity in the baseline.

## 8.3 Couple outputs

- estimation and inference;
- household-level predictive fit;
- money-metric welfare;
- preference-versus-environment decomposition;
- nested access/ability/needs decomposition;
- comparison with singles;
- combined household-type inequality.

---

# 9. Headline welfare and decomposition architecture

## 9.1 Cross-sectional JMP decomposition

The final paper should produce an exhaustive two-way headline decomposition:

- preferences \(P\);
- complete non-preference environment \(O\).

Let:

- \(I_{00}\): actual inequality;
- \(I_{10}\): inequality after preference equalization;
- \(I_{01}\): inequality after environment equalization;
- \(I_{11}\): inequality after both are equalized.

The two-player Shapley contributions are:

\[
C_P
=
\frac{1}{2}
\left[
(I_{00}-I_{10})
+
(I_{01}-I_{11})
\right],
\]

\[
C_O
=
\frac{1}{2}
\left[
(I_{00}-I_{01})
+
(I_{10}-I_{11})
\right].
\]

If the grand coalition exhausts all relevant heterogeneity,

\[
I_{11}=0,
\]

so:

\[
s_P=\frac{C_P}{I_{00}},
\qquad
s_O=\frac{C_O}{I_{00}},
\qquad
s_P+s_O=1.
\]

This provides the paper’s intuitive headline:

> \(a\%\) of money-metric well-being inequality is attributed to preference heterogeneity and \(b\%\) to the broad non-preference environment.

Use “attributed to,” not “caused by” or “morally responsible for.”

## 9.2 Nested environment decomposition

Then decompose:

\[
C_O
=
C_{\mathrm{access}}
+
C_{\mathrm{ability}}
+
C_{\mathrm{endowments/needs}}.
\]

This preserves the economic distinction between:

- access to employment, hours, and occupations;
- wage ability/technology;
- budget endowments and needs.

The existing access/ability/preference/background decomposition remains useful as a diagnostic bridge, but it should not be the final headline architecture if it cannot generate an exhaustive preferences-versus-environment split.

## 9.3 Choice of money-metric welfare measure

There is no data-determined uniquely “correct” welfare measure. The primary measure must match the claim the paper wants to make.

The primary cross-sectional measure should:

- be comparable across households;
- use a common policy-independent reference;
- remain well-defined when opportunity sets differ;
- permit exhaustive preference/environment equalization;
- support singles and couples on a common scale;
- avoid dependence on an unstable sampled-set maximum;
- permit transparent inequality and policy analysis.

The specific measure must be selected before the final decomposition, not after inspecting which measure gives the preferred result.

## 9.4 Policy-reform welfare

A later reform paper should report at least:

1. standard compensating or equivalent variation under actual preferences;
2. a common-reference or circumstance-adjusted welfare change;
3. mean welfare change;
4. welfare inequality change;
5. winners and losers;
6. opportunity-attributable inequality change;
7. fiscal cost and cost-effectiveness.

A regional-development policy and an education policy can be compared only after specifying how each changes the structural primitives and after imposing a common fiscal-cost and social-welfare criterion.

---

# 10. Recovering individual opportunity environments

The current model recovers a household-specific opportunity density:

\[
\widehat g_i(h,w,o),
\]

not a literal finite count of available jobs.

Therefore the paper should not claim:

> Household \(i\) has 11 jobs and household \(k\) has 7 jobs.

It can report:

- probability of receiving a full-time job;
- probability of receiving each occupation;
- probability of a wage above a threshold;
- expected wage conditional on occupation;
- probabilistic menu dominance;
- effective menu diversity.

An effective number of opportunity cells can be defined on a common grid:

\[
N_i^{eff}
=
\exp
\left(
-\sum_m p_{im}\log p_{im}
\right).
\]

This is an effective diversity measure, not an actual job count.

A menu-dominance graph can compare the cumulative distribution of a common package-quality index:

\[
F_i(q)=P_{\widehat g_i}\{Q(j)\le q\}.
\]

Actual expected job counts would require a separate offer-intensity model, such as:

\[
N_i\sim Poisson(\lambda_i),
\]

which is difficult to identify from static choice data and is not part of the current baseline.

---

# 11. Household-level predictive fit

Aggregate fit is not sufficient. A model may reproduce aggregate distributions while assigning low probability to the observed outcome for many households.

For each household, compute:

\[
p_i^{chosen}=P_i(j_i^{obs}).
\]

Report:

- mean and median chosen probability;
- chosen-alternative rank;
- top-1, top-5, and top-10 hit rates;
- household log score;
- Brier scores;
- calibration curves;
- weighted and unweighted results.

## 11.1 Confusion matrices

Produce hard and probabilistic confusion matrices for:

1. employment/non-employment;
2. five broad hours categories;
3. twelve fine hours bins;
4. occupation;
5. wage bins;
6. hours × occupation;
7. hours × occupation × wage bin.

For observed category \(r\) and predicted category \(s\):

\[
M_{rs}
=
\frac{
\sum_i w_i
\mathbf 1\{y_i=r\}
\sum_{j:c(j)=s}P_{ij}
}{
\sum_i w_i\mathbf 1\{y_i=r\}
}.
\]

Also report prediction quality by:

- sex;
- education;
- age;
- children;
- region.

Exact top-1 prediction should not be the sole criterion because the model is probabilistic and wages are continuous.

---

# 12. Practical specification matrix

The comparison table should contain at least:

| ID | Specification |
|---|---|
| S0 | Current LOC4 benchmark |
| S1 | Minimum-age centering, exact reparameterization |
| S2 | Minimum-age centering + relaxed age-curvature bounds |
| S3 | Explicit 35-hour opportunity peak |
| S4 | Male children leisure-preference shifter |
| S5 | Richer highest-attained education in wage block |
| S6 | Exact-log consumption utility |
| S7 | Parsimonious education preference shifter |
| S8 | Combined supported candidate |

For every specification report:

- negative log likelihood;
- number of free parameters;
- convergence status;
- active bounds;
- basic Hessian rank/condition;
- chosen probability/log score;
- top-k fit;
- hours fit;
- occupation fit;
- wage fit;
- subgroup fit;
- key parameter changes;
- economic interpretation;
- decision: reject / retain as diagnostic / include in S8.

Do not calculate full welfare for S1–S7.

---

# 13. Potential paper portfolio

## Paper 1 — Job Market Paper

**Question:** What explains money-metric well-being inequality?

Content:

- singles and couples;
- RURO estimation;
- common-opportunity RUM benchmark;
- preferred positive specification;
- money-metric welfare;
- preferences versus broad environment;
- nested access/ability/needs decomposition;
- institutional hours and occupation-wage specification;
- specification sensitivity.

## Paper 2 — Tax-benefit reform and well-being inequality

**Question:** How does a tax-benefit reform affect labour supply, disposable-income inequality, money-metric welfare, and opportunity-related inequality?

The existing structural model and EUROMOD infrastructure can be reused.

## Possible Paper 3 — Identification and welfare attribution

**Question:** When do observationally similar preference/opportunity representations imply different welfare attributions?

Potential content:

- RUM–RURO observational equivalence;
- 35-hour peak placement;
- LOC4 sensitivity;
- external opportunity moments;
- formal conditions for channel identification.

This becomes a separate paper only if the methodological result is generalized beyond the France application.

## Package

`dclaborsupply` is research infrastructure. A software paper is optional after the package is mature, but it should not currently be counted as a core economics paper or delay the JMP.

---

# 14. Package requirements generated by the research agenda

The package should eventually support a turnkey workflow:

```text
dclaborsupply validate --data DATA --schema SCHEMA
dclaborsupply fit --data DATA --spec SPEC --output RUN
dclaborsupply infer RUN
dclaborsupply report RUN
```

The generic model grammar should support:

- RUM versus RURO;
- singles and joint-household couples;
- Box-Cox, exact-log, and translog utility;
- configurable centering and polynomial/spline bases;
- leisure normalizer separate from time endowment;
- configurable bounds and pins;
- explicit hours peaks;
- employment, hours, and occupation opportunity blocks;
- occupation- and hours-conditioned wage location;
- conditional proposals \(q(w|o)\), \(q(w|h)\), \(q(w|o,h)\);
- flexible education bases;
- post-estimation scoring and confusion matrices;
- external regional covariates and auxiliary moments;
- generic welfare and decomposition plugins.

France-specific data cleaning, EUROMOD paths, and JMP governance must remain outside the generic core.

---

# 15. Repository and documentation discipline

## 15.1 Goal 1

The previous housekeeping mission is closed. Do not reopen a broad repository-cleaning programme.

All new exploratory singles runs should live under:

```text
MNL/experiments/JMP_PS1/
```

Permanent top-level outputs are capped at:

```text
experiments/JMP_PS1/specification_matrix.yaml
experiments/JMP_PS1/model_comparison.csv
experiments/JMP_PS1/post_estimation_comparison.html
experiments/JMP_PS1/decision_note.md
```

Machine-generated manifests may remain in run directories.

## 15.2 Goal 2

Package cleanup and usability work should proceed on a separate branch. Stale build artifacts may be removed as part of the next package implementation, not as a separate mission.

## 15.3 Documentation proportionality

Permanently retain:

- one research agenda;
- one current-state dashboard;
- one experiment matrix;
- one comparison table;
- one selected-specification note;
- final review and acceptance only for the selected model.

Do not permanently retain:

- routine action cards;
- repeated delegation prompts;
- progress notes;
- minor correction memos;
- separate documents for every experiment;
- duplicate governance restatements.

---

# 16. Prioritized roadmap

## Phase 1 — immediate positive-specification sprint

**Priority:** central now

1. age-centering invariance;
2. leisure-scale invariance;
3. S2 relaxed age bounds;
4. S3 explicit 35-hour peak;
5. S4 male child shifter;
6. S5 richer education;
7. S6 exact-log utility;
8. S7 education-preference diagnostic;
9. household-level predictive fit;
10. select S8.

## Phase 2 — targeted regional/auxiliary-data audit

**Priority:** central now, but no estimation until mergeability is established

1. identify finest available geography;
2. audit four official data-source families;
3. select one regional/auxiliary identification design;
4. determine whether the design is strong identification or robustness only.

## Phase 3 — preferred singles welfare

**Priority:** after S8 selection

1. estimate and infer S8;
2. compute welfare for S0 and S8 only;
3. implement exhaustive preferences-versus-environment decomposition;
4. nest access/ability/needs within the environment;
5. retain numerical precision infrastructure.

## Phase 4 — couples

**Priority:** core JMP stage

1. joint 100-alternative proposal;
2. joint EUROMOD pricing;
3. parsimonious couple RURO;
4. couple welfare and decomposition;
5. common singles/couples welfare scale.

## Phase 5 — final JMP integration

1. combined household-type inequality;
2. final main tables and figures;
3. final claim set;
4. sampling uncertainty for welfare and decomposition;
5. manuscript.

## Phase 6 — later papers

1. policy-reform paper;
2. possible identification/methodological paper;
3. optional software publication.

---

# 17. Decisions already taken

The following are working decisions unless new evidence overturns them:

1. the final JMP should include singles and couples;
2. LOC4 is the current structural benchmark;
3. exploratory work should be fast and minimally documented;
4. the 35-hour peak should be tested explicitly;
5. age centering and leisure scaling must first be treated as invariance questions;
6. the final headline decomposition should be preferences versus the broad non-preference environment;
7. the broad environment should then be decomposed into access, ability, and needs/endowments;
8. household-level predictive fit must be added;
9. regional data should discipline opportunity channels, not be added indiscriminately;
10. unobserved preference and opportunity heterogeneity should not be introduced simultaneously at this stage;
11. the package should become a turnkey engine-ready-data-to-report system;
12. documentation should not dominate estimation.

---

# 18. Open scientific decisions

The following remain open:

1. exact bounds or alternative functional form for the age profile;
2. whether the 80-hour time endowment is economically appropriate;
3. final education grouping;
4. whether education belongs in preferences in the preferred model;
5. whether exact-log utility should replace estimated Box-Cox curvature;
6. whether conditional wage structure should include hours as well as occupation;
7. finest regional geography and viable external-data merge;
8. primary money-metric welfare criterion;
9. household versus person weighting in the combined singles/couples analysis;
10. whether a later latent-class preference model adds enough value;
11. whether an identification paper can be generalized sufficiently to stand alone;
12. final policy-reform application.

---

# 19. Expected deliverables from the next empirical sprint

The next Goal 1 return should contain only:

1. `model_comparison.csv`;
2. `post_estimation_comparison.html`;
3. recommended S8 singles specification;
4. one regional/auxiliary-data design;
5. one welfare-criterion recommendation;
6. unresolved scientific conflicts.

It should not return a new collection of mission charters, review memos, or routine execution notes.

---

## Final research direction

The project should now move from certifying the existing prototype to selecting the economically strongest positive specification and completing the singles-and-couples welfare decomposition.

The central standard is:

> **Use documentation to preserve scientific reproducibility, not to replace scientific progress.**
