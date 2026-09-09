# Review of the research-story report: scientific exposition, interpretation and source fidelity

**File reviewed:** `JMP_research_story_report_v1.html` supplied on 7 September 2026.  
**Reviewer disposition:** Substantial revision required before this report becomes the authoritative presentation manual or the source text for the paper.  
**Document type:** Working review memo. One consolidated revision, not a new model-development mission.

## 1. Scope and overall assessment

This review examines the complete supplied HTML, its dynamically populated text and tables, all 24 sections, and the embedded figures and captions. The report contains 40 figure placements, including duplicate figures. I also consulted the locally supplied final-singles specification declaration, its base specification, the earlier specification-battery scripts, the older singles discussion report, and the existing literature corpus. Selected external methodological references are identified at the end. This is not a new numerical audit of confidential microdata, estimation, or EUROMOD runs. Where a claim requires a source not present in this packet, the requested correction is to recover the actual source, not to invent the missing specification.

The report is a useful collection of results, but it is not yet a dependable scholarly explanation. Its most important defect is not length or typography. It sometimes translates accurate parameter values into incorrect economic statements, combines current numerical anchors with historical pictures, and replaces analytical derivation with declarations that a convention is valid.

The proper remedy is a scientific rewrite and synchronized regeneration of existing descriptive outputs. These findings do not, by themselves, invalidate the underlying estimates or require another broad specification search.

### What already works

The report provides a navigable structure; a substantial account of the decomposition; a useful distinction between Shapley attribution and one-factor equalization; explicit discussion of reference sensitivity; the current zero cross-leisure restriction for couples; and a separation of parameter uncertainty from numerical integration uncertainty. Its embedded data machinery is valuable for traceability.

However, a key-to-number check verifies a transcription, not the meaning of the sentence surrounding it. The child-coefficient percentage and several incorrect figure captions demonstrate this limitation directly.

### Corrections to the user's diagnosis

The supplied version already contains:

- a sample-flow table with singles and couples side by side, and a separate couples waterfall, in section 3;
- a generic utility equation and several opportunity equations in section 6;
- singles and couples coefficient columns side by side in section 7;
- a couples results section, including a 46-parameter table, in section 11;
- definitions of several technical terms in the final glossary.

Consequently, the problem is not literal absence of all these objects. The problems are inconsistent integration, inadequate first-use explanation, stale assets, incomplete derivations and, in several places, incorrect interpretation. A revision should preserve the useful material instead of rebuilding it from scratch.

## 2. Restore the research question without relabelling the results

### Recommended title and first-use definition

**Job Opportunities, Preferences, and Well-Being Inequality: A RURO Analysis of French Singles and Couples**

The first paragraph should define **Random Utility–Random Opportunity (RURO)**. It is the central methodological name, not internal project jargon. By contrast, labels such as S8, R240, LOC4, pin, gate and carrier belong in the reproducibility appendix, not in the main explanation.

### Recommended main question

> How much inequality in money-metric well-being is associated with unequal access to jobs and unequal earning opportunities, rather than heterogeneous preferences, after separately accounting for non-labour resources and household composition?

The main supporting comparison should be:

> How do the level and attribution of well-being inequality change when household-specific job opportunities are omitted from the behavioural model?

Do not presuppose that the common-opportunity benchmark must increase the preference share: the reported result does not support that claim.

### Why “environment” cannot simply be replaced by “opportunities”

The report's exhaustive top-level non-preference component contains job access, earning opportunities, and endowments/needs. It is broader than labour-market opportunities. Under the female-reference raw singles result, the report gives approximately:

| Component | Share of baseline welfare inequality |
|---|---:|
| Preferences | 6.30% |
| Job access | 14.90% |
| Earning opportunities | 20.62% |
| Endowments and needs | 58.18% |

Thus job access plus earning opportunities account for about **35.5%**, not **93.7%**. The latter is the full non-preference component.

Keep the exhaustive accounting, but lead the narrative with the labour-market question. Define the top-level label as **“non-preference circumstances”** or define “environment” immediately and consistently. Do not repeatedly alternate between circumstances, opportunities, resources and environment as if they were synonyms.

A suitable opening results sentence is:

> In the primary raw singles specification, job access and earning opportunities jointly receive about 35.5% of the attribution of well-being inequality, compared with 6.3% for preferences; household resources and composition account for the remaining 58.2%. These are model- and reference-conditional Shapley attributions, not causal effects or reductions from isolated interventions.

The reference range and equivalized results should follow this sentence, not be suppressed.

## 3. Literature positioning is materially missing

There is no substantive literature discussion or normal reference list in the report. The reader cannot tell which ideas are inherited, which assumptions are standard within this particular modelling tradition, and what the paper adds.

Use the existing literature corpus rather than commissioning another broad search. The discussion needs four connected strands:

1. **Structural labour supply with constrained or latent job opportunities.** Use the Aaberge–Dagsvik–Strøm and Aaberge–Colombino traditions; Dagsvik and Jia on latent jobs and identification; and the Capéau–Decoster–Dekkers RURO application. These establish the behavioural framework and its empirical restrictions. Jointly estimating preferences and opportunities is not itself a new invention of this paper.
2. **Welfare evaluation with heterogeneous preferences.** Explain the relevance of Decoster–Haan and related equivalent-income work: heterogeneous preferences affect welfare measurement and normative reference choices. Do not reproduce their complete ranking exercise merely to cite them.
3. **Responsibility-sensitive job-choice welfare analysis.** Discuss Jacquet, Jia and Thoresen (2026) accurately: their standard CV versus circumstance-only CV comparison concerns welfare effects of a tax reform. The present paper studies cross-sectional inequality in well-being levels and a counterfactual attribution architecture. “We do the opposite” is not sufficient positioning.
4. **Distributional decomposition.** Cite the Shapley/Shorrocks foundation and the grouped/nested rule actually used. The decomposition rule allocates interactions; it does not identify the structural blocks or establish the ethical responsibility boundary.

The defensible contribution is the integration of these elements: carrying explicitly modelled job opportunities through estimation, money-metric welfare and nested inequality attribution, together with the common-opportunity comparison. Avoid unverified claims that no previous paper contains any part of this architecture.

The separate Haydar–Maniquet theory paper should be cited when its particular welfare definition or axiom is used. Its full theoretical programme should not be presented as if it were the empirical paper's contribution.

## 4. Material problem in the introduction: the conventional model is caricatured

Section 1 says conventional labour-supply models give everyone the same budget set and therefore reveal anyone working part time to prefer leisure and anyone in a low-paying occupation to prefer that occupation.

This is too strong. A conventional discrete-choice labour-supply model may have household-specific wages, non-labour resources, taxes and transfers, hence different budgets, even when it gives households a common menu of hours. It need not model occupational choice at all. Observed choices are also not individual deterministic preference rankings when the model contains utility shocks.

Replace the passage with:

> Conventional discrete-choice labour-supply models can allow household-specific budgets and heterogeneous tastes while using a common menu of hours or placing limited structure on job availability. When household-specific access restrictions are omitted, estimated preference parameters may partly capture those restrictions. This paper makes the opportunity mechanism explicit and examines its consequences for welfare measurement and attribution.

The latter is a modelling risk and an empirical question, not a predetermined conclusion that every conventional model makes the same mistake.

The report also describes an observed job as “one draw” from the opportunity distribution. Available alternatives are generated by the opportunity process; the chosen job is selected using preferences. Those distributions are not the same. This distinction must govern the conceptual figure as well as the prose.

## 5. Singles and couples: integrate them without pretending they are identical

The report already has joint tables, but its descriptive sequence remains dominated by an inherited singles report. Conversely, some attempts to integrate the two types are too sweeping: “only the decision unit changes; everything above is untouched” is not accurate when the report itself gives different consumption curvature conventions and spouse-specific hours and employment parameters for couples.

Use one framework with explicit household-type and spouse indices, followed immediately by a specification-comparison table:

- one labour-supply dimension for singles versus a joint male/female alternative for couples;
- separate estimated preference blocks by sex and household type;
- singles Box–Cox consumption curvature versus the stated log-consumption couples restriction;
- exact hours, occupation, employment and wage parameter sharing;
- joint household budgeting and the four participation regimes;
- zero direct cross-leisure interaction in the current couples application.

A couples-specific subsection is appropriate. A structure that makes couples appear unestimated or merely planned is not. Nor should the report call their data frame or proposal literally identical to the singles frame.

### Cross-leisure restriction

The current clean couples model has no estimated term

\[
\beta_{\ell\ell}\,\mathcal B(\tilde\ell_m;\theta_{\ell m})\,
\mathcal B(\tilde\ell_f;\theta_{\ell f}).
\]

State that direct leisure complementarity is restricted to zero. This does **not** mean spouses' decisions are independent: joint consumption, income effects, non-linear household taxes/transfers and the joint choice problem still connect them.

The historical curvature problem is a reason the restriction was adopted, not proof that the interaction is unidentifiable in every corrected couples specification. No new interaction estimation is required to fix this exposition.

Couples welfare uncertainty should be explained where the couples results appear. Do not claim that all couples preference findings are as stable as the singles findings, and do not relegate the entire couples application to future work because one component is sensitive.

## 6. Data construction and descriptive figures need regeneration and relabelling

### 6.1 Existing joint sample accounting should be preserved

Section 3 contains 1,555 singles and 2,275 couples and a joint construction table. Keep this foundation and make it the main sample figure/table, rather than placing it after a singles-only waterfall as a correction.

Each screen should state its operational criterion, economic motivation, numbers removed by household type, and external-validity consequence. Sample selection should not be defended with phrases such as “the right denominator” without discussing the excluded population.

### 6.2 Current and historical rules are mixed

The screen table still says **floor 10**, and the continuous descriptives show **minimum employed hours 10**, while the current narrative claims the corrected five-hour construction. The recorded correction preserved the actual 6–9 hours of seven chosen workers rather than flooring them at 10. These descriptions cannot all represent the same final transformed sample.

Regenerate these summaries from the corrected chosen rows. Distinguish raw observations, transformed choices and simulated alternatives. Do not merely edit the caption while retaining an old table.

The descriptive hours intervals are also not the narrow intervals used by the structural opportunity terms. Both displays may be useful, but the report must label them separately. A graph of broad reporting bands is not a picture of the exact opportunity-density specification.

### 6.3 Several captions contradict the pictures

| Figure identifier | Actual visual content | Report caption/problem | Required correction |
|---|---|---|---|
| `rg_fig1_1_sample_funnel` | Old funnel ending in singles | Presented as the primary sample-construction story | Replace main display with a common funnel branching into both final samples |
| `rg_fig2_3_wage_age` | Separate wage and age histograms | Says wages against age by education and discusses an experience profile | Correct the caption; construct a conditional wage/profile graph only from actual suitable data |
| `rg_fig2_1_income_distributions` | Disposable income overall, by sex, and by education | Says earned income, non-labour income and disposable income | Correct the caption and add a real resource-component display from the actual variables |
| `rg_fig2_2_hours_bands` | Old singles broad hours-band display | Implies the actual structural bands; embedded wording suggests hours are not continuous | Distinguish continuous hours with band-dependent density from descriptive binning |
| `rg_fig3_1_lorenz_and_deciles` | Singles observed disposable-income Lorenz/deciles | No couples coverage; plotted and text Gini not identical | Recompute using the final sample and the stated weights; label type and income concept |
| `r240_couples_participation_obs_vs_pred` | Four joint participation regimes | Generic caption suggests spouse marginals | Name the four regimes and give their denominators |
| Main welfare/coefficient figures | Many retain S8, LOC4, R240 and process labels inside the image | Text cleanup does not reach image labels | Regenerate the images, not only their HTML captions |

The old `fr_singles_results_discussion_v1_noCode.html` is a useful template for descriptive coverage, not a source of automatically current results.

### 6.4 What to show for both populations

Provide comparable tables for singles and couples: age, education, household composition, employment, hours, occupation, observed wages, non-labour inputs, disposable income and geography. For couples, show spouse-specific labour variables and household-level income only once per household.

Provide raw household income distributions within type and equivalized comparisons under the disclosed convention. Pool only quantities that are actually comparable under the adopted definitions; the unresolved pooled welfare decomposition must not be silently replaced by an exhaustive one.

### 6.5 Other data clarifications

Distinguish the survey wave, income reference period, EUROMOD policy year, uprating and euro-price year. The report's year label is not a substitute for this chronology.

The descriptive row “gsur (job-access probability)” is incorrect: it is a group unemployment-rate regressor, not the model's probability of access.

The operative child count is household members below age 20, not necessarily a biological-parent-linked count or legal dependent count. Explain the relationship to the separately constructed parent-linked child-age variables.

Explain observed worker wages, annualization for months worked, and the fact that latent counterfactual offers are modelled rather than obtained by using a non-worker's imputed wage as an observed outcome.

Explain treatment of non-positive disposable income before applying a positive-domain utility transformation. The report should state the actual production rule, not leave flooring, exclusion or shifting implicit.

EUROMOD pricing is exact relative to its coded policy rules, input assumptions and simulation settings. It is not a proof that actual take-up, actual taxes or actual disposable income are observed without error. Sample wage bounds are research/support restrictions, not automatically a limit on what EUROMOD is capable of calculating.

## 7. Define ISCO and justify the four-group aggregation

Explain International Standard Classification of Occupations, the relevant ISCO-08 vintage and the underlying major-group codes. The model's four categories are a further research aggregation, not the ILO's own four official task categories.

| Model category | Underlying ISCO major groups | Descriptive content |
|---|---|---|
| 1 | 6–9 | Agriculture-related skilled work, crafts/trades, machine/plant operators, and elementary occupations |
| 2 | 5 | Services and sales |
| 3 | 4 | Clerical support |
| 4 | 1–3 | Managers, professionals, technicians and associate professionals |

If retaining “routine manual / non-routine manual / routine cognitive / non-routine cognitive,” explain that these are broad task proxies. In particular, not every job in ISCO 6–9 is literally routine. State treatment of armed forces and missing occupational codes, and why this aggregation is feasible in the sample.

The public French socio-professional tables cannot be uniquely mapped into these four groups from their published coarse cells. Do not convert that limitation into the false blanket statement that no official PCS–ISCO correspondence exists. Official probabilistic correspondences and a unique aggregate crosswalk are different things.

## 8. Separate non-labour income, resources and simulated transfers

“Non-labour resources” is the name of an empirical factor and therefore needs an exact inventory. It is not automatically synonymous with every receipt that is not an observed wage.

A helpful schematic budget notation is

\[
c_i(j)=\mathcal T\big(y^L_i(j),r_i,d_i;\tau\big),
\]

where \(y^L_i(j)\) denotes labour earnings at the alternative, \(r_i\) the resource inputs held fixed as the job changes, \(d_i\) household composition/needs and other relevant budget characteristics, and \(\tau\) the common policy system. This notation is explanatory; its arguments must be filled from the actual production budget model.

For each actual resource variable, state whether it is an input or an EUROMOD output, its unit, whether it is held fixed across jobs, and how the resource-equalization operator replaces it. Capital income and private transfers are possible examples, not a substitute for the actual list.

Means-tested benefits must not be treated as fixed non-labour income merely because they are not wages. Their values can change with earnings, resource inputs and household composition. Explain that distinction before interpreting the new resources/composition split.

Two explanations in section 16 require deletion or qualification:

- **“The only channel that operates on non-employed households.”** False for ex-ante opportunity-based welfare. An actually non-employed household's evaluation still depends on potential working alternatives and their access and pay.
- **“It acts on the level of the budget, not its slope,” with level shifts necessarily stronger than opportunity changes.** Not generally true under means testing and non-linear tax-benefit rules, and not a theorem explaining the estimated shares.

The result that resources receive a large attribution is informative without these invented mechanisms. Interpret the computed counterfactuals and interactions instead.

## 9. Analytical model exposition: present the mechanism before the code conventions

### 9.1 Distinguish four objects

Introduce separately:

1. systematic utility and its stochastic component;
2. the structural opportunity measure/density;
3. the resulting distribution of chosen jobs;
4. the analyst's sampling proposal.

A generic reduced-form choice-density expression that can organize the exposition is

\[
f_i^{choice}(j;\theta)
=\frac{\exp\{u_i(j;\theta_P)\}\,G_i(j;\theta_O)}
{\int_{\mathcal J}\exp\{u_i(z;\theta_P)\}\,G_i(z;\theta_O)\,d\nu(z)}.
\]

This is a pedagogical representation, not a replacement of the production model's normalization. Define the reference measure \(\nu\), including the non-employment atom, discrete occupation and continuous hours/wages. Derive the application from the actual RURO assumptions and cite its lineage.

The model is not a claim that agents include “access” or the proposal correction in their preferences. The terms arise in the econometric choice representation.

### 9.2 Utility

Section 6 already includes Box–Cox formulas. What is missing is an exact correspondence between symbols and the evaluated inputs: consumption units and normalization, the time endowment, leisure normalization, age transformation, child-count definition, household-type differences and the shock scale.

For couples, each spouse needs the appropriate own-age argument. A generic sex index alone is insufficient if preferences differ between singles and couples. The couples consumption restriction must be visible, not hidden after an equation seemingly shared without modification.

Fixing a consumption coefficient does not automatically put utility in euros. Nor does preference-respecting equivalent income require identical consumption curvature across all people. Explain the maintained utility-scale and functional-form restrictions separately from the normative reference and inversion.

### 9.3 Structural densities

For each of employment, hours, occupation and wage offers, give: formula, conditioning variables, support, units/base measure, normalization, reference category, household-type sharing, and economic interpretation.

The sentence that all four factors equal one at a reference is false as a description of the displayed lognormal wage density. Distinguish unnormalized relative intensities, normalized conditional densities and the overall mixed distribution.

For a disjoint hours interval \(B_b\) with constant height \(\exp(\alpha_b)\), its integrated mass depends on \(|B_b|\), not only on its coefficient. A height ratio is not a probability ratio between bands of different widths.

The active 35-hour term is an elevated density over **[33.5, 36.5)**, not a literal point mass at exactly 35 hours. Use “narrow-band peak around 35 hours” unless a genuine atom is actually implemented.

For wages, show the occupation-conditioned lognormal density and its location equation. Explain reference occupation, shared slopes, common dispersion, and positive-wage worker gating. Its mean, median and mode are distinct:

\[
\operatorname{median}(w)=e^{\mu},\quad
E[w]=e^{\mu+\sigma^2/2},\quad
\operatorname{mode}(w)=e^{\mu-\sigma^2}.
\]

The observed-worker wage distribution is selected; it must not be compared to the raw latent offer density as if they were the same target.

### 9.4 Identification

Delete the assertion **“Nothing about the functional form does this work.”** The structural separation depends on the model's parametric restrictions, channel assignments, variation and exclusion assumptions. Excluding a regressor in code is not empirical proof of a valid exclusion restriction.

Explain why group unemployment is economically proposed to shift access, and discuss sorting and omitted local preferences/amenities. Avoid declaring one coefficient “the exclusion restriction that identifies access separately from taste” without specifying the conditional argument.

The claim that age never enters opportunities is inconsistent with potential experience in the wage-offer equation. More generally, a characteristic can affect several structural paths. The decomposition allocates paths/objects; it does not require every raw variable to appear once in the entire economic model.

The 35-hour concentration supports the relevance of modelling an institutional hours feature. It does not nonparametrically prove that its whole effect belongs to offers rather than tastes.

## 10. Sampling: explain and substantiate the chosen-row convention

Section 5 is too declarative. It should give the actual proposal components and parameters, including any focal intervals, continuous background, truncation, group conditioning and mixture weights.

For a continuous mixture,

\[
q_H(h)=\sum_b\omega_b f_b(h),\qquad \omega_b\ge0,\quad\sum_b\omega_b=1.
\]

The example adding 0.30 and 0.05 is correct only if those quantities are already mixture-weighted contributions under the same dominating measure. It is not correct to add an atom's probability mass to a continuous density at the same point without defining a mixed measure.

Most importantly, **“the observed job is always included, therefore its log correction is zero” is not a complete derivation of a sampled-alternatives likelihood.** In conventional conditional sampled-choice likelihoods the relevant object is the probability of the sampled set conditional on each candidate having been chosen. Alternatively, a simulated-integral likelihood must be derived from its own integration identity and normalization. The report must identify which construction its implementation uses and reproduce that derivation.

This review does not authorize changing the accepted chosen-row treatment. It identifies an insufficient justification in the report. If the accepted estimator cannot be justified from its actual design, that is a specific econometric issue to return—not something to cover by a more confident caption.

Separate the finite-sample approximation from the exact population model. “q cancels from everything” is too strong at finite numerical resolution. Distinguish the estimation sample of alternatives from the larger ex-ante welfare integration nodes, their weights, their non-employment handling and their role.

## 11. Incorrect interpretations of actual parameter values

### 11.1 Children: a concrete formula error

Section 7 says the single-female child coefficient 1.1690 corresponds to approximately **221.9%** of a leisure-weight unit. The coefficient enters additively:

\[
\beta_{\ell i}=\beta_{\ell0}+\beta_{\ell a}a_i+
\beta_{\ell a^2}a_i^2+\beta_{\ell k}k_i.
\]

One additional child therefore raises this index by **1.1690 model units**, not by \(100(e^{1.1690}-1)\) percent. At the particular reference profile with leisure weight 4.2437, the proportional index change is about 27.5%; that is a profile-specific illustration, not a labour-supply elasticity.

The same row says “positive, as expected,” but the couples estimate in that row is **−0.5586**, with standard error 1.3010. Give each application's sign and uncertainty accurately.

Not retaining the single-male count coefficient is not proof that fathers have no childcare-related labour-supply response. State that this particular term was not supported sufficiently in the tested specification. The female estimate is also only marginally precise, not a strong universal childcare effect.

### 11.2 Group unemployment: a missing factor of ten

The supplied base specification scales `gsur` by **10**. The report's displayed employment equation and interpretation omit that scale while calling the variable a 0–1 rate.

With coefficient −1.2525, a one-percentage-point rise in the underlying rate corresponds to

\[
\exp\{-1.2525\times10\times0.01\}\simeq0.8823
\]

in the relative working-opportunity factor. Thus it is about an 11.8% change in that factor, not an 11.8-percentage-point change in employment. The exact implication for choice requires the full normalization and utility model.

For couples, verify the actual clean-specification transformation rather than importing the singles scale by assumption.

### 11.3 Leisure weight is not itself the price of time

A coefficient multiplying transformed leisure is not automatically euros per hour. For the additive specification with \(\tilde c=c/\lambda_c\) and \(\tilde\ell=\ell/\lambda_\ell\), a local consumption compensation slope is

\[
\frac{u_\ell}{u_c}=
\frac{\beta_{\ell i}}{\beta_c}
\frac{\lambda_c}{\lambda_\ell}
\frac{\tilde\ell^{\theta_\ell-1}}{\tilde c^{\theta_c-1}}.
\]

Define both units. Monthly consumption against weekly labour hours yields compensation in monthly euros per extra weekly hour; it is not automatically an hourly wage. A local derivative and an exact finite compensation for an additional hour are also different calculations.

Use evaluated MRS curves to interpret time valuation, not raw leisure-intercept comparisons across models with different curvatures and transformations.

### 11.4 Bounds and invariance

The report says that re-expressing leisure units moves an active coefficient away from 1 and makes it “strictly interior,” establishing that the bound is merely a units artifact. This is not valid. Under a true reparameterization the admissible set must also be transformed; boundary activity is not removed simply by changing the numerical coordinate.

Furthermore, the stated transformed values 0.035 and 0.056 need to be reconciled with the final exponents. Under the supplied scale map \((40/10)^{\theta_\ell}\), the final exponents printed in section 7 give approximately 0.0888 and 0.2240. These are coordinates, not proof of interiority.

The separate re-estimation with widened bounds is the relevant sensitivity. Keep its actual result and remove the misleading normalization argument.

### 11.5 What coefficient exponentiation can mean

Provide a concise interpretation key: additive index coefficient; multiplicative density-height coefficient; log-wage location contrast; dispersion; curvature; normalizing restriction. Only exponentiate where the formula warrants it. A positive coefficient's intuitive direction should not be invented when nonlinearities, selection or uncertainty prevent a clean unconditional statement.

## 12. Inference and numerical integration need first-use explanations

A glossary at the end is useful but insufficient. Define these terms before reporting their intervals.

### Household-robust inference and CR1

Each household supplies one observed choice and one log-likelihood contribution. Its simulated alternatives are not 101 independently sampled economic outcomes. Write the household score and sandwich explicitly:

\[
s_i=\frac{\partial\ell_i}{\partial\theta},\quad
H=-\sum_i\frac{\partial^2\ell_i}{\partial\theta\partial\theta'},\quad
M=\sum_i s_i s_i',\quad
\widehat V=c_{FS}H^{-1}MH^{-1}.
\]

State whether the objective is summed or averaged and how survey weights enter estimation, reporting and welfare aggregation. Explain CR1 as the adopted finite-sample adjustment, including the report's \(G/(G-K)\) convention. Define the interior coordinate set used for inference.

Excluding boundary-active coordinates is the application's conditional active-set treatment, not the universal definition of cluster-robust inference. “Reporting an interval would be wrong” is too broad: boundary-aware procedures can exist. Say that ordinary unconstrained normal intervals are not used for those coordinates here.

### RQMC

Define randomized quasi-Monte Carlo as randomized, deliberately well-spread integration points, used here to approximate latent-job integrals. Independent scrambles provide a way to measure numerical integration variability. Explain how the actual production estimator combines the integrals before logarithms/inversion, and distinguish this from parameter uncertainty across hypothetical household samples.

### Jackknife

Define a leave-one-scramble-out calculation: omit one complete scramble, recompute the whole target, repeat, and use the variation across these recalculations to assess numerical sensitivity. For a conventional replicate jackknife,

\[
\widehat{\operatorname{Var}}_{JK}(T)
=\frac{B-1}{B}\sum_b\left(T_{(-b)}-\bar T_{(-\cdot)}\right)^2.
\]

Then print the exact implemented band rule if it additionally includes a bias diagnostic or a different centre. Do not label a numerical band a sampling confidence interval. For normalized shares recompute the ratio per replicate, not the component intervals separately.

“Owen scramble” and “Owen value” refer to different operations. One is a numerical randomization and the other a grouped attribution rule; explain them separately.

### Uncertainty comparisons

The report prints a reference-only preference-share range around 6.3–10.9% and a parameter interval around 4.2–10.9%. These values do not support sweeping prose that reference sensitivity dwarfs parameter uncertainty. Compare the appropriate objects directly and avoid combining reference ranges, conditional parameter intervals and RQMC bands into one vague robustness claim.

## 13. Welfare exposition contains a substantive overstatement

Section 13 needs the precise analytical reference map, not only the code-like log-sum equation. Define the attained ex-ante value and reference map, for example schematically:

\[
\Phi_{i,S}(m)=\mathcal V_{i,S},\qquad W_{i,S}=\Phi_{i,S}^{-1}(\mathcal V_{i,S}).
\]

Then give their actual integrals, support, normalization, wage/consumption replacement, non-employment treatment, unit of \(m\), and dependence on coalition \(S\). This notation is an exposition requirement, not authorization to change the welfare measure.

In particular, distinguish **gross hourly wages**, **monthly earnings**, **disposable consumption**, and the **uniform reference amount**. “Flat pay at every job” does not settle these distinctions.

The report says no variation in job pay survives into the measure because pay is flattened in the reference situation. That is misleading. Flattening pay in the comparator does not imply that actual earnings opportunities cease to affect attained ex-ante welfare and the compensating reference amount. The report itself attributes a positive component to earning opportunities.

Similarly, a blanket claim that a wider opportunity distribution must increase this own-opportunity-set money metric requires proof under the actual definition: an opportunity change can alter both attained welfare and its own-set reference map. The report must state the applicable property and conditions, or qualify the claim. It must not import monotonicity from a different, fixed-reference welfare definition.

Euros are a common unit; their use alone does not establish the normative legitimacy of interpersonal comparisons. Explain the ethical reference and why this measure is appropriate for this paper, while keeping the separate theory contribution distinct.

## 14. Decomposition: preserve the good explanation, remove invented mechanisms

The distinction between attribution and isolated equalization is a strength. Keep the explicit two-player formula, with 1 meaning “equalized”:

\[
C_P=\tfrac12[(I_{00}-I_{10})+(I_{01}-I_{11})],\qquad
C_E=\tfrac12[(I_{00}-I_{01})+(I_{10}-I_{11})].
\]

It shows immediately why preference equalization alone can raise inequality while its Shapley contribution is positive, and why the environment's approximately 93.7% attribution differs from its approximately 77% standalone reduction.

Specify the grouping/nesting rule used to divide \(C_E\), and later the endowments/needs component. Do not silently substitute a flat multi-player Shapley calculation that might allocate interactions differently.

The report explains the preference-equalization increase as people having adapted their tastes to their environments. That is an untested behavioural story. The observed joint distribution, counterfactual references and nonlinear interactions suffice to generate the result without identifying preference formation. Present adaptation as a possible interpretation only if separately supported—not as the measured mechanism.

For channel assignments, distinguish an estimated structural role from a normative responsibility judgment. Education-related earnings differences are not proved to be innate ability; preferences are not automatically morally responsible choices; and the access block need not identify discrimination separately from capability or availability.

The composition/equivalence-scale convention should be justified by the factor definition. Closure is an implication, not the normative argument. A different separation of budget composition and normative needs would be a different counterfactual question, not inherently impossible or automatically double counting.

No third “tax-system contribution” should be fabricated when the common policy function is held fixed.

## 15. External evidence: important errors that must be removed

Section 10 says a group's mean desired hours exceeding the upper bound of its actual-hours band implies **every worker** in that band wants more hours. This is false. A mean condition does not establish a statement for each individual. Even the mean-gap interpretation requires the two means to describe the same conditional population.

The report also says the direction of a wish-more gradient is robust to reversing the binary code while the level is uncertain. For a genuine binary reversal, \(p\) becomes \(1-p\), reversing an increasing/decreasing pattern. The claim needs a separately demonstrated argument; otherwise omit the unresolved result.

This contradicts the earlier decision to stop the auxiliary-moment route without a clean model counterpart. Retain reliable official underemployment figures as descriptive context; do not turn them into a validation of the estimated offer weights or an identified preference/constraint wedge.

The 35-hour external comparison also needs its denominator: a share conditional on the five selected bands is not a share of all employed workers. Define whether observations outside those bands are excluded from all three sources.

The report should distinguish the **already assembled public DADS wage benchmark** from unavailable restricted DADS/BTS microdata. The former can be incorporated with the observed-sample/model/external three-way comparison. Do not say the entire wage benchmark is unavailable because the latter is not accessible.

## 16. Matched-household figure: what it actually shows and how to caption it

The currently embedded forward-match figure is not the older pair described in earlier chat. It displays two employed single men matched on occupation **4**, an hours band and wage quintile **4**. Their preference profiles are close by a distance criterion, not identical; observed jobs are comparable categories, not identical bundles. Their median conditional offer wages, approximately **€11.38 and €11.05**, are similar, not dramatically different.

The most striking contrast is the employment-related mass. The plot mixes wording such as “offer density” and “P(offer taken up).” Those labels must be resolved from the computation. A normalized opportunity mass and an actual employment choice probability are different objects.

For clarity, use the same mathematical distinction throughout:

\[
p_i^{opp}(E=1)=\frac{\int_{E=1}G_i(j)\,d\nu(j)}{\int G_i(j)\,d\nu(j)},
\qquad
p_i^{choice}(E=1)=\frac{\int_{E=1}e^{u_i(j)}G_i(j)\,d\nu(j)}{\int e^{u_i(j)}G_i(j)\,d\nu(j)}.
\]

These expressions define what the labels could mean; the source must determine which was plotted. They are not interchangeable.

Suggested caption, after resolving that object:

> **Similar estimated preferences, different employment-access environments.** The two single men are selected by the stated matching rule among employed households in the same observed occupation group, hours band and wage quintile. Their estimated leisure-preference curves are close, not identical. Panel (a) plots the leisure component of utility; panels (b) and (c) show the specified opportunity masses over hours and occupations; panel (d) shows conditional wage-offer densities and marks the observed wages. In this same-sex comparison the hours and occupational profiles are common conditional on employment, so their unconditional mass differences are driven primarily by the employment-access margin. The example illustrates a model-conditional contrast, not a causal regional effect, an individual ability ranking or a recovered count of available jobs.

Give the matching criterion and tolerance in a short note, not opaque distance values without interpretation. Keep the displayed personal details appropriately anonymized. A theoretical figure, an actual matched pair and a counterfactual relocation of one profile need distinct titles and captions.

## 17. Geography and the common-opportunity benchmark

### Geography

The geographic result is conditional on the current channel assignment. Geography enters employment access, while other location-sensitive budget features remain in the composition/resource budget mapping. Say this explicitly.

Do not call the employment-access result a **lower bound** on the full effect of place. Omitted geographic wage, hours, amenity and sorting channels can offset or reinforce one another, and signed Shapley contributions do not furnish a bound without additional assumptions.

Conditional working hours/occupation/wage summaries may remain unchanged while their unconditional probabilities change with the employment mass. Captions should specify which is shown.

### RUM

Section 18 calls the likelihood difference a decisive test on 25 degrees of freedom. That conflicts with the supplied manager return describing the comparison as an upper-bound/descriptive likelihood result. Recover the accepted benchmark inference status; do not infer a chi-square reference distribution merely by subtracting parameter counts. The table also labels positive negative-log-likelihood values as “log-likelihood”; correct that sign label.

Explain the benchmark with a term-by-term analytical table: what becomes common, what remains in the budget and preferences, what hours constants are reinterpreted/re-estimated, what happens to structural wage terms, and what proposal is retained. Do not infer this solely from parameter names.

Do not write \(g^E=0\) to mean no heterogeneous employment-access effect. Zero density excludes jobs. Setting a log index to zero yields a unit relative factor, which is different, and the full reference distribution still needs its specified normalization. The exact benchmark may use a different common density, so extract its actual formula.

The behavioural relabelling of constants and the welfare-attribution result are distinct. The current evidence shows a small change in the preference **share** alongside a fall in total inequality and the absolute preference contribution. A reversal in leisure-intercept differences alone is not proof of a reversal in the complete MRS ordering.

Avoid calling this identified “true misclassification” without a truth benchmark. It is a comparison of interpretations and welfare accounting across maintained models.

## 18. Scientific history, first-use notation and the notebook

The development history should be compact and correct. The five-hour correction did not introduce a five-hour minimum to remove benefit-dominated near-zero jobs: it corrected seven chosen rows previously floored at ten. Several historical variant descriptions also fail to match the supplied scripts: the richer-education trial split the low education tier; the exact-log trial concerned consumption curvature; the tertiary-education trial concerned leisure preferences. These are not the occupation/sex interaction experiments attributed to them in parts of the report.

The notebook chapter is internally contradictory: it calls CUDA supported, then cites a CPU-only comparison and says CUDA parity remains outstanding; it also says the notebook's profiles still point to an older incompatible package. Separate **engine capability**, **parity on the target model**, and **the installation actually selected by the notebook**. The latest Goal-2 message reports final-singles CUDA parity, but that does not by itself install the relevant package or establish couples CUDA support.

The hands-on guide currently describes mostly a cached-data replay/refit workflow. It needs to state honestly whether raw sample construction, new alternative generation and EUROMOD repricing can actually be launched from the notebook, or whether they remain external stages. Subsetting an existing R=400 bundle is not generating arbitrary new draws.

The report and shared exports should not persist confidential household records. A secure live walkthrough and a public illustrative example are different outputs.

Move the large numeric-key/self-check register and implementation filenames into a collapsed technical appendix. Regenerate the seminar Q&A from corrected text: it currently repeats several of the errors identified above.

## 19. Recommended structure of the revised report and manuscript

Use the same intellectual spine, at different levels of detail:

1. Research question, motivation and contribution, including literature positioning.
2. Common household framework and the distinction between preferences, opportunities and other circumstances.
3. Data and sample construction: common source, parallel singles/couples screens and descriptive distributions.
4. RURO model: budgets, utility, mixed opportunity measure, chosen-job distribution and identification assumptions.
5. Estimation and numerical integration: exact proposals, likelihood, inference and separate numerical uncertainty.
6. Estimated parameters and fit: singles and couples in parallel, with economically valid interpretations.
7. Welfare measure and normative reference, followed by raw/equivalized definitions.
8. Counterfactual game and nested decomposition; attribution versus isolated equalization.
9. Results: market opportunities, preferences, resources/needs, references and uncertainty; type-specific results with their qualifications.
10. Common-opportunity benchmark, geographic illustration and genuinely informative external benchmarks.
11. Limits and a short scientific development history.
12. Notebook operating guide and seminar questions; technical provenance in an appendix.

The paper should contain the core equations, sample decisions, main descriptives, parameter/fit evidence and interpretation. The HTML can provide more worked examples and fuller explanation. The notebook should execute the same model. None should carry incompatible definitions merely because they target different audiences.

## 20. Consolidated instruction for Goal 1

**Tool/chat:** Goal 1 Thinking/Manager for economic rewriting; local Codex for source extraction, rebuilding tables/figures and rendering.  
**Workspace:** current report; this review; the current manuscript and deck; final singles/couples specifications and outputs; existing literature corpus and bibliography; final data-construction code; external public benchmark artifacts; current research notebook.  
**Save:** one revised report, an updated current paper source and the existing executable notebook. Do not create separate audit-memo families.

```text
REVISION — SCHOLARLY RESEARCH REPORT AND MATCHING PAPER TEXT

Treat the attached review as one consolidated revision list, not as a new
specification-search mandate.

Keep the frozen estimates unless a specific source inconsistency establishes
that a reported object is wrong. Do not defend incorrect prose with an earlier
acceptance status.

1. Reframe the opening around unequal job access/earning opportunities versus
   preferences, accounting separately for resources and composition. Define
   RURO in the opening. Retain the exhaustive non-preference component without
   relabelling its entire share as job opportunities.

2. Add literature positioning and a proper bibliography from the existing
   corpus. State the exact incremental contribution rather than claiming to
   invent joint opportunity/preference estimation.

3. Integrate singles and couples throughout data, model, estimates and fit.
   Preserve their actual specification differences and the couples beta_ll=0
   limitation. Do not imply that coupled decisions are independent.

4. Rebuild final-sample descriptive tables and figures for both populations.
   Correct the stale floor-10/minimum-hours information and all mismatched
   captions. Use actual resource variables for resource distributions.

5. Write the utility, budget, structural opportunity densities, normalizers,
   proposal densities, likelihood, welfare inversion and decomposition in
   analytical notation with defined symbols and units. Extract—not guess—the
   chosen-row correction derivation and the common-opportunity RUM construction.

6. Correct the substantive interpretation errors itemized in the review:
   additive child effect versus exponentiation; gsur scaling; density height
   versus mass; narrow 35-hour band versus atom; leisure weight versus MRS;
   constrained inference and transformed bounds; mean desired-hours claims;
   unsupported coding-direction robustness; opportunity effects for actual
   non-workers; welfare-reference flattening versus actual earnings effects;
   geographic lower-bound language; and the unsupported LR-test interpretation.

7. Explain CR1, RQMC, jackknife, survey weighting and conditional parameter
   uncertainty before first use. Keep numerical bands, parameter intervals and
   normative-reference ranges separate.

8. Replace the matched-household caption with a panel-specific explanation of
   the actual pair, matching restrictions and the precise mass/probability
   plotted. Do not call similar jobs/preferences identical.

9. Reconcile notebook capability, actual installation and the latest singles
   CPU/CUDA parity. State which raw-to-report stages are executable and which
   are cached/external. Do not infer couples device support from singles parity.

10. Apply the corrections to HTML, current manuscript/LaTeX, image labels,
    captions and Q&A together. Keep implementation identifiers in a technical
    appendix; do not hide substantive uncertainty there.

If the actual source cannot establish a formula or empirical statement, label
that specific point unresolved and return it. Do not fill the gap from a parser
name, prior chat wording or generic modelling convention.

Return the revised report and paper, refreshed final-sample figures, and a short
list of unresolved economic questions. No new broad model search or report family.
```

**Recommended filenames:** `JMP_research_story_report_v2.html` and the next version of the existing seminar manuscript. Update the actual current `.tex` source when present rather than inventing a parallel authoritative draft. Keep this review as `JMP_research_story_report_review_v1.md`. The notebook remains the single existing research laboratory.

## 21. Sources and scope of external checks

**Primary reviewed evidence:** uploaded `JMP_research_story_report_v1.html`, sections and figure identifiers cited above. All reported numerical comparisons in this memo are quotations or arithmetic based on that report unless otherwise specified.

**Supplied supporting project sources:** `estimation_spec_S8_corrected_floor5_v1.yaml`; `estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`; `run_ps1_battery_part1.py`; `run_ps1_battery_part2.py`; `JMP_final_rich_engine_terms_contract_v1.yaml`; `fr_singles_results_discussion_v1_noCode.html`; `Literature_collection.md`. The corrected-singles declaration explicitly binds the base specification and code extensions, so the base's gsur scale is relevant to the reported singles formula. Historical files are used for their documented historical experiments, not to certify current couples equations.

**Selected external methodological and literature checks:**

- Aaberge, Colombino and Strøm (1999), “Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints,” Journal of Applied Econometrics 14(4), 403–422.
- Dagsvik and Jia (2016), “Labor Supply as a Choice among Latent Jobs: Unobserved Heterogeneity and Identification,” Journal of Applied Econometrics 31(3), 487–506; DOI 10.1002/jae.2428. Earlier working-paper version: Statistics Norway Discussion Paper 786.
- Decoster and Haan (2015), “Empirical Welfare Analysis with Preference Heterogeneity,” International Tax and Public Finance 22, 224–251; DOI 10.1007/s10797-014-9304-5. The user previously discussed an earlier working-paper version.
- Jacquet, Jia and Thoresen (2026), “How Much Does Responsibility Matter in Fairness Measurement?” CESifo Working Paper 12418; DOI 10.65864/wf42ly1k5t. Publisher abstract establishes the tax-reform CV/CVcirc comparison; no exhaustive novelty conclusion is inferred from the abstract.
- Shorrocks (2013), “Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value,” Journal of Economic Inequality 11, 99–126; DOI 10.1007/s10888-011-9214-z.
- Train (2009), Discrete Choice Methods with Simulation, second edition, chapters 2 and 3; utility scale and the conditional sampled-alternatives likelihood, especially section 3.7.1.
- Cameron and Miller (2015), “A Practitioner's Guide to Cluster-Robust Inference,” Journal of Human Resources 50(2), 317–372; DOI 10.3368/jhr.50.2.317.
- ILO, official ISCO-08 classification documentation; used to distinguish major occupational groups from the application's task-proxy aggregation.
- Owen (2026), “Randomized Quasi-Monte Carlo Integration,” arXiv:2608.17143; used for the methodological meaning of randomized integration, not to reconstruct the application's precise band formula.

**Bottom line:** Preserve the research and its actual numbers, but substantially revise how they are explained. The next deliverable should be an economics report that a reader can understand and interrogate without access to the author's file system—not a more elaborate certificate that the same numbers were copied correctly.
