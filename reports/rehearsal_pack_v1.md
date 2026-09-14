# Seminar rehearsal script

The main presentation contains 16 slides. The remaining 10 slides are backup material.

## Main presentation

### Slide 1

On slide: Unequal Job Opportunities and the Measurement of Welfare Inequality Hisham Haydar LISER and University of Luxembourg France, EU-SILC priced through EUROMOD. Seminar of 17 September. The welfare results use the own-set equal-consumption measure. A preliminary restricted-operator decomposition is in the backup appendix.

Say: Thank you. The question is how much of the inequality in money-metric well-being is attributable to unequal job opportunities rather than to differences in taste, and what happens to that attribution when a model leaves opportunities out. I will show the model, the estimates, the fit, the welfare definition and a descriptive welfare baseline. The computed preliminary restricted-operator decomposition is in the backup appendix. A separately defined ex-ante metric is being reconstructed for comparison. Historical ex-ante percentages are not current results and are not shown. The verified attained-bundle measure and its observed-bundle results remain the current welfare evidence; no settled comparison between the two metrics is available.

### Slide 2

On slide: Two people with the same tastes and the same wage need not face the same set of jobs.  How much of measured welfare inequality is attributable to unequal job access and earning opportunities, rather than to preferences?  What does a model that assumes a common choice set do to that attribution? Both questions are about a measure, not about a policy counterfactual. 2/16

Say: The two questions are the same two questions as in every version of this paper; they motivate the current specification. The first is an attribution question about a money-metric inequality index. The second is a methodological question: a discrete-choice labour supply model that gives every household the same alternatives has to explain non-employment with a taste parameter, and I want to know whether that relabelling survives into the welfare accounting.

### Slide 3

On slide: The contribution is a structural opportunity set plus a welfare measure defined on it.  A random-utility, random-opportunity (RURO) model in which which jobs a household can reach is estimated, not assumed.  The own-set equal-consumption money metric; in this empirical specification its direct reference collapses to universally available non-employment.  Observed-bundle welfare and resource inequality, reported separately for single-adult and couple households. The computed preliminary restricted-operator decomposition is in the backup appendix. 3/16

Say: The contribution has three parts. Preferences and opportunity components are jointly estimated, with their separation relying on maintained functional-form and exclusion restrictions. The welfare measure is taken from the companion theory paper with Francois Maniquet. A separately defined ex-ante metric is being reconstructed for comparison. Historical ex-ante percentages are not current results and are not shown. The verified attained-bundle measure and its observed-bundle results remain the current welfare evidence; no settled comparison between the two metrics is available.

### Slide 4

On slide: France, EU-SILC priced through EUROMOD: 1 540 single-adult and 2 223 couple households.  Estimation frames: final samples and the current estimated specification.  Estimation frame: each household’s observed job plus 100 drawn alternatives, every one priced through the tax–benefit system.  Fit diagnostics use a separate, larger panel: 2 048 common quadrature nodes per household.  Weights are the survey weights dwt throughout. Results use a single specification throughout. Estimates from earlier, non-comparable sample frames are not shown. 4/16

Say: The two estimation samples contain single-adult and couple households. The estimates and diagnostics use these same samples throughout. Each household contributes its observed job and a hundred drawn alternatives, each of which is run through EUROMOD so the consumption argument is a real disposable income, not an approximation. The second number on the slide is a different object: the positive-fit diagnostics (individual-level predictive diagnostics) integrate over a common panel of two thousand and forty-eight priced quadrature nodes per household, not over the estimation draws.

### Slide 5

On slide: A job is a package; a household draws from its own distribution over packages. access employment mass hours piecewise, 35h peak occupation sex-specific wage offer log-normal opportunity density gi(·) over reachable jobs preferences ui(c, ℓ) observed job = arg max over the drawn set Access and capability are not separately identified; the access factor is their product. 5/16

Say: This is the architecture. A job is not an hours cell: it is hours, occupation and a wage, and whether the household can reach it at all. The opportunity density factorises into an access margin, a piecewise-constant hours factor with a peak at the statutory thirty-five hour week, sex-specific occupation availability, and an occupation-conditioned log-normal wage offer. Preferences enter separately. The observed job is the argmax over what was drawn. The identification caveat is on the slide and I keep it there all talk: the access factor mixes personal capability and market availability and the cross-section does not separate them.

### Slide 6

On slide: Preferences and the opportunity density are estimated in one likelihood. Pr(ji | xi) ∝exp  ui(cij, ℓij) + log gi(j) −log qi(j) u preferences g estimated opportunity density q numerical proposal density, divided out The proposal correction is what makes the drawn alternatives a simulator for the estimated set rather than the choice set itself. 6/16

Say: One likelihood, two structural objects. The proposal density is a numerical device: the alternatives are drawn from it and it is divided back out, so it is not part of the economics. That separation matters later, because the welfare measure I am going to define must not depend on the proposal density, and I will show that it does not. Preferences and opportunity components are jointly estimated, with their separation relying on maintained functional-form and exclusion restrictions. No causal interpretation follows from that separation. The baseline deliberately keeps systematic preference heterogeneity parsimonious: age profiles for all four adult groups and a child-related shifter for women. The child term is interpreted as a reduced-form behavioural/time-constraint shifter, not as pure taste. More explicitly, systematic leisure heterogeneity contains an intercept, age, age squared and group-specific leisure curvature for all four groups, plus a child shifter for women; sex and household type are carried by separate parameter blocks.

### Slide 7

On slide: Estimated model: 41 free parameters for singles, 47 for couples. singles couples free parameters 41 47 estimation households 1 540 2 223 objective at ˆθ 6253.463 10283.034 Objectives reproduce exactly under an independent diagnostics reimplementation. 7/16

Say: The headline fact about the estimates is that they are reproducible: an evaluator built separately for the diagnostics work recovers both stored objective values to the last digit shown. That is the precondition for everything on the next two slides. The parameter counts differ because the couples specification pins nothing at the bound while the singles specification pins eleven coefficients by construction.

### Slide 8

On slide: Extensive-margin accuracy, shown only for the groups where it passes the quadrature-adequacy gate. 0; 20; 40; 60; 80; 100 extensive-margin accuracy (%), groups clearing the numerical-adequacy rule single men single women coupled men coupled women withheld: quadrature-limited 85.5% 92.3% 89.8% Values are shown only where the pre-registered weighted quadrature-adequacy rule clears for this statistic; single men are quadrature-limited and withheld. This is not a group-count result. 8/16

Say: The pre-registered adequacy gate asks whether numerical integration error is small relative to sampling variation. I show values only where that specific extensive-accuracy statistic clears the gate and withhold the single-men value because it is quadrature-limited. This is not a group-count result. Aggregate participation and occupation margins are reproduced reasonably closely, while hours fit is uneven. Individual-level predictive diagnostics raise possible excess stochastic dispersion in some groups; the group-level classification is not used as a headline result. If asked: coupled men pass the weighted gate narrowly (ratio 0.240 against 0.25) and miss the unweighted one (0.250); the deck applies the weighted rule throughout. Source details are retained in the provenance note. The displayed percentages are the observed weighted accuracies; the numerical-adequacy bootstrap means are used only to assess numerical adequacy.

### Slide 9

On slide: Calibration conditioned on prediction: observed hours against predicted hours, by predicted decile. 30 40 predicted E[h | work] 25 30 35 40 45 mean observed hours single men 30 40 predicted E[h | work] single women 30 40 predicted E[h | work] coupled men 30 40 predicted E[h | work] coupled women support coverage audited using individual-level predictive diagnostics; calibration statistics partly quadrature-limited; use the explicit group verdicts 9/16

Say: Households are sorted into deciles of their own predicted expected hours conditional on working, and each decile's mean observed hours is plotted against its mean prediction, on the common-node support. The dashed line is the forty-five degree line. Conditioning on the prediction rather than on the outcome is the direction that does not mechanically manufacture regression to the mean. The caption is the honest status. The support audit has now been done: the diagnostic analysis re-evaluates the fit on a common quadrature panel far larger than the estimation draws, no household has an effective sample size below thirty, singles have no unsupported observed bin, and only a handful of couples fall in a region that finite panel does not represent. The calibration statistics behind this picture remain partly quadrature-limited, and the group-level classification is not used as a headline result. Aggregate participation and occupation margins are reproduced reasonably closely, while hours fit is uneven. So read the shape, not the gaps.

### Slide 10

On slide: The access kernel is estimated, and it varies across households. −4 −3 −2 −1 0 single-adult estimates, log access index; bars are 1.96 x CR1 robust s.e. access constant survey-strata shift regional unemployment regional median income region 2 region 3 region 4 region 5 region 6 region 7 region 8 Single-adult estimates; horizontal bars are 1.96 × CR1 cluster-robust standard errors. Structural and model-conditional; not causal. 10/16

Say: This is the access block of the estimated opportunity density. The point is not any individual coefficient, it is that the block is estimated rather than imposed and that it moves: households in different regional access environments, and in different survey strata, face materially different employment masses at the same preferences and the same wage. This is the evidence that the opportunity side of the model is doing work. It is also the evidence the welfare measure later rests on, which is why I show it before the measure and not after.

### Slide 11

On slide: So is the earning-opportunity kernel: an offer distribution, not a single wage. 0.0 0.5 1.0 1.5 2.0 single-adult estimates, log wage-offer density; bars are 1.96 x CR1 robust s.e. offer location low education high education experience experience squared offer dispersion occupation 2 occupation 3 occupation 4 Single-adult estimates; occupation terms shift the offer location. Dispersion ˆσ = 0.382 (z = 28.7). 11/16

Say: The wage side is an offer density with an estimated dispersion, not a point wage attached to each person. Education and experience shift the location, occupation shifts it again, and the residual dispersion is precisely estimated. Two households with identical observed wages can have different earning opportunities in this model, because what they face is a distribution. That is the second half of what I mean by unequal job opportunities, and together with the access block it is what the welfare measure has to be defined on.

### Slide 12

On slide: Haydar–Maniquet W 1: the consumption at home that would leave the household exactly as well off. W 1 i = mi(o; zi) where ui mi(o), o  = ui(zi) zi attained bundle o the non-employment state mi the money metric The empirical measure uses the universally available non-employment state as its reference. A market-job reference is a sensitivity analysis that requires an unidentified intensity parameter; it is not in the baseline. 12/16

Say: If asked why this reference and not the market-job reference: the reference comparison compared the full feasible-set reference, the full feasible set including non-employment, against the market-only reference, the market-job universe. The full feasible-set reference is primary for the current paper. M at its dense-law endpoint stops being a household-specific object and becomes a whole-market reference, and at finite intensity it needs a set-size parameter the data do not identify. That is recorded as a limitation and as future work, not as a competing headline. I am not claiming F is the right reference in the theory; I am claiming it is the one this empirical specification identifies.

The money metric is derived from the own-set equal-consumption principle. Under the current empirical specification its direct reference collapses to the universally available non-employment state; opportunity heterogeneity therefore affects the current welfare measure through attained bundles.

### Slide 13

On slide: Under the current specification W 1 coincides with the staying-home equivalent — as a fact about this domain. W 1 i,F = C obs i exp h Li(jobs i )−Li(o) βc i  Inputs: C obs i , Li(jobs), Li(o), βc — nothing else.  No opportunity density g, no proposal q, no shock ε, no intensity κ.  Current nonworkers: W = C; current workers: W < C under the maintained empirical domain. This is an empirical-domain coincidence under log consumption and universally available non-employment, not a general theoretical identity. 13/16

Say: The most likely question here is whether I have just proved that measure one and measure four are the same thing. I have not, and the distinction is explicit. The coincidence has two ingredients, both specific to what is estimated: consumption enters utility in logs, and non-employment is behaviourally available to every household. Change either and the two measures separate. If asked about the consumption argument: the welfare definition confirms that $C^{\mathrm{obs}}$ must be the exact object entering the estimated utility at the observed state, not a re-chosen normative income concept, and the measure-correspondence audit closed that provenance before the baseline was allowed to run. The money metric is derived from the own-set equal-consumption reference-set principle. Under the current empirical specification its direct reference collapses to the universally available non-employment state; opportunity heterogeneity therefore affects the current welfare measure through attained bundles. For a one-nat shortfall, $L_i(j_i^{\mathrm{obs}})-L_i(o)=-1$, the illustration is $W=C_i^{\mathrm{obs}}\exp(-1/\beta_c)<C_i^{\mathrm{obs}}$.

The one-nat shortfall has a leisure-index difference of -1. Current nonworkers: W=C. Current workers: W<C under the maintained empirical domain.

### Slide 14

On slide: Baseline W 1-F, equivalised, single adults. C eq W 1 F eq households 1 540 1 540 weighted mean 1 766 1 302 weighted median 1 588 1 165 weighted Gini 0.263292 0.249807 Units: EUR/month, household-equivalised (modified-OECD scale); survey weight dwt. A descriptive dispersion comparison, not a welfare-loss index. The modified-OECD scale is used throughout the equivalised results. Singles and couples equivalised levels are never compared. The sample aggregates reproduce to machine precision under an independent reimplementation. This is a descriptive dispersion comparison (C eq against W 1 F eq within the singles sample), not a welfare-loss index. 14/16

Say: Equivalised results are primary on this slide: the household-equivalised Gini of $\Wone_F$ is below the household-equivalised Gini of observed consumption, for singles. I show that as a descriptive dispersion comparison only, not as a welfare-loss statement --- the ratio $\Wone_F/C^{\mathrm{obs}}$ reflects the systematic leisure term at the observed job relative to home leisure, not a monetary loss, and I am not constructing a loss index on this slide. The equivalence scale is the modified-OECD scale, ratified as the primary scale for current JMP distributional reporting by the equivalence-scale analysis, on the economics review in the source analysis; the scale question is closed. The unequivalised construction this equivalises is unchanged and is in the backup appendix.

### Slide 15

On slide: Baseline W 1-F, equivalised, couples. C eq W 1 F eq households 2 223 2 223 weighted mean 2 245 1 311 weighted median 2 063 1 237 weighted Gini 0.226805 0.197403 Units: EUR/month, household-equivalised (modified-OECD scale); survey weight dwt. A descriptive dispersion comparison, not a welfare-loss index. The modified-OECD scale is used throughout the equivalised results. Singles and couples equivalised levels are never compared. Reported separately from singles: no pooled figure, and no cross-sample level comparison is drawn on this slide or elsewhere in this deck. The same independently reimplemented welfare construction and equivalence scale are used as for single adults. 15/16

Say: Same descriptive comparison, on the couples sample. I am deliberately not placing this table next to the singles one: the two are separate estimation frames, the welfare unit differs, and the analysis does not compare equivalised welfare levels across these separately estimated samples. If asked how the couples numbers compare to singles, the honest answer is that this deck does not draw that comparison, and I would want to see it examined outside a seminar slide before treating it as informative. The scale is the same ratified modified-OECD scale as on the singles slide (equivalence-scale analysis); ratifying the scale does not license a cross-sample level comparison.

### Slide 16

On slide: What I would like from you today.  Is universally available non-employment the reference you would want for this question?  Which counterfactual attainment estimand would you defend?  What would convince you the access kernel is identified, given that access and capability are not separated? Thank you. 16/16

Say: Three questions, in the order I most need answers. The reference domain choice is normative and I would like it challenged. The attainment estimand is the blocking design decision. And the access identification caveat is the one every discussant raises; I would rather hear what evidence would settle it than defend the current position.

## Backup / appendix

### Preliminary restricted-operator decomposition

### Backup slide 1

On slide: Preliminary restricted-operator decomposition A preliminary P/A/B decomposition has been computed for the attained-bundle money metric, holding resources, needs and composition fixed. It is a restricted counterfactual exercise, not a comprehensive share of inequality due to all opportunities. A separately defined ex-ante metric is being reconstructed for comparison; neither historical ex-ante percentages nor a settled cross-estimand conclusion are reported here.

Say: A preliminary P/A/B decomposition has been computed for the attained-bundle money metric, holding resources, needs and composition fixed. It is a restricted counterfactual exercise, not a comprehensive share of inequality due to all opportunities. A separately defined ex-ante metric is being reconstructed for comparison; neither historical ex-ante percentages nor a settled cross-estimand conclusion are reported here.

### Backup slide 2

On slide: This bounded decomposition equalises three channels, not whole job access. P systematic utility heterogeneity (tastes + reduced-form time constraints) →common reference A local geographic/temporal access shifters (region, urban/rural, year) →common reference B wage-offer location →common reference location Household resources, needs and composition are held fixed. Personal occupation access, hours-band access and node-level alternative characteristics are not equalised by A.

Say: For this bounded decomposition exercise, $A$ is local geographic/temporal access shifters (region, urban/rural, year). It is not personal occupation access, hours-band access or full job access. Children enter the current structural specification through a reduced-form female time-constraint shifter. In a unitary labour-supply model this term may capture both tastes and childcare/home-production constraints; we therefore do not interpret it as pure preference heterogeneity. The baseline deliberately keeps systematic preference heterogeneity parsimonious: age profiles for all four adult groups and a child-related shifter for women. The child term is interpreted as a reduced-form behavioural/time-constraint shifter, not as pure taste.

### Backup slide 3

On slide: The bounded decomposition is executed; the final attainment estimand remains under design. coalition S counterfactual environment carried realised draws W 1 F (zS i ) inequality IS bounded decomposition route This exercise reuses the already-priced estimation panel with no re-estimation and no new pricing. The final decomposition’s counterfactual-attainment estimand remains under design.

Say: The preliminary exercise carries the household's realised draws through each counterfactual environment. That is an executed, bounded accounting route, not the final counterfactual-attainment estimand. The final design still has to choose between a realised-bundle route with conditioned latent heterogeneity and an ex-ante $g$-computation route; the inequality of expected welfare is not the expected inequality of welfare.

### Backup slide 4

On slide: Preliminary restricted-operator decomposition In a preliminary three-factor structural exercise that holds household resources, needs and composition fixed, equalising systematic utility heterogeneity, coarse geographic/temporal access heterogeneity and earning opportunities changes money-metric well-being inequality by 1.8–9.9% of the baseline Gini, depending on household type and reporting scale. Within the Shapley allocation of that movable component, earning-opportunity heterogeneity has a larger contribution than the coarse geographic/temporal access channel in both samples and both reporting conventions. The preference contribution is not sign-robust to equivalisation. These are preliminary model-based accounting results, not causal estimates and not the final decomposition of total well-being inequality.

Say: The decomposition is bounded by design because household resources, needs and composition are held fixed. Within that bounded game, equalising P/A/B changes the Gini by 1.8–9.9% of its baseline level, depending on sample and reporting scale. The restriction is by construction; the realised numerical magnitude is a model result under that restriction. Dispersion in consumption is quantitatively large relative to dispersion in log well-being: Var(log C) is roughly 100–127% of Var(log W), with the excess offset by a large negative covariance between consumption and the leisure valuation. this bounded decomposition exercise holds household resources, needs and composition fixed, leaving important sources of dispersion outside the P/A/B allocation. If asked about wage elasticities: a valid gross-wage perturbation requires new tax-benefit repricing over the affected job alternatives, and the current priced support does not contain that counterfactual.

### Backup slide 5

On slide: The earnings operator equalises wage-offer location only. The earning-opportunity channel equalises wage-offer location only: the systematic differences associated with education and potential experience, which shift offer locations by at most about 0.10 log points. The common offer spread (about 0.37 log points), wage-draw luck and selection remain in the residual and are quantitatively larger than the location differences removed by this operator. This is a definitional boundary of the exercise, not a measurement error. Equalising locations can change attained wages; it does not equalise the whole wage distribution. The diagnostic comparison that also compresses the common spread and selection is a bound, not an additional decomposition result. Thin effective support for couples leaves individual wage attainment noisy and remains a numerical limitation.

Say: The earning-opportunity channel equalises wage-offer location only: the systematic differences associated with education and potential experience, which shift offer locations by at most about 0.10 log points. The common offer spread (about 0.37 log points), wage-draw luck and selection remain in the residual and are quantitatively larger than the location differences removed by this operator. This is a definitional boundary of the exercise, not a measurement error. Equalising locations can change attained wages; it does not equalise the whole wage distribution. The diagnostic comparison that also compresses the common spread and selection is a bound, not an additional decomposition result. Thin effective support for couples leaves individual wage attainment noisy and remains a numerical limitation.

### Backup slide 6

On slide: Baseline W 1-F, unequivalised, single adults (verification backup). households 1 540 weighted mean 1 435 weighted median 1 320 weighted Gini 0.238 observed workers 1 336 observed non-workers 204 Units: household EUR/month, unequivalised; survey weight dwt. Descriptive baseline; no counterfactual, no decomposition, no causal reading. Secondary/verification slide: the equivalised singles slide (§6) is primary. The sample aggregates reproduce to machine precision under an independent reimplementation.

Say: This is the literal observed-bundle attained-bundle distribution before equivalisation, kept here so any question about the un-scaled level or about worker/non-worker counts has a one-slide answer. It is not the headline: the equivalised slide in §6 is. For non-workers the measure equals observed consumption exactly by construction; for workers it is strictly below it.

### Backup slide 7

On slide: Baseline W 1-F, unequivalised, couples (verification backup). households 2 223 weighted mean 2 496 weighted median 2 356 weighted Gini 0.210 observed workers 2 173 observed non-workers 50 Units: household EUR/month, unequivalised; survey weight dwt. Descriptive baseline; no counterfactual, no decomposition, no causal reading. Secondary/verification slide: the equivalised couples slide (§6) is primary. Reported separately from singles. No pooled figure: the two samples are separate estimation frames and the welfare unit differs.

Say: The couples backup is on its own slide and there is no pooled row: the two samples are separate estimation frames with different welfare units, and even on the ratified modified-OECD scale this deck never compares singles and couples levels. These are unequivalised household totals: couples pool two earnings streams, and the non-employment count is small. The pricing-floor issue that affects the neither-work bundle for a subset of couples does not enter here, because this baseline is evaluated at the observed bundle and never prices the home state.

### Backup slide 8

On slide: Pre-registered checks for the baseline W 1-F measure check singles couples non-workers, max |W 1 −C obs| 0 0 workers, ratio outside (0, 1) 0 0 dependency test (g, q, ε, κ) PASS PASS worked-household correspondence test PASS PASS indifference identity, max |∆u| 1.8e-15 1.8e-15 guards triggered 0 0 All six checks were pre-registered before execution. Worker-ratio violations were to be explained, never clipped; none occurred.

Say: The checks are the reason the baseline is presentable. The nonworker and worker checks are the model-implied domain conditions. The dependency check is the dependency test: the baseline API accepts no opportunity density, no proposal, no shock and no intensity, and does not read them indirectly. The indifference check inverts the utility numerically and confirms the indifference identity to machine precision.

### Backup slide 9

On slide: Quadrature adequacy for extensive-margin accuracy group extensive accuracy status coupled women 89.8% reported (ratio 0.02) single women 85.5% reported (ratio 0.15) coupled men 92.3% reported (ratio 0.24) single men — quadrature-limited, withheld Weighted, all households. Ratio is Monte Carlo s.e. over sampling s.d.; the pre-registered criterion is ≤0.25. Node bootstrap over 2 048 common quadrature nodes per household (diagnostic panel, not the estimation draws). Simulated bands: 500 outcome vectors at fixed ˆθ. Source: individual-level predictive diagnostics.

Say: The gate was fixed before the statistics were computed. It asks whether numerical integration error is small enough relative to sampling variation for the statistic to be a statement about the model rather than about the quadrature. Withholding rather than downgrading is deliberate: a quadrature-limited number carries no information about fit.

### Backup slide 10

On slide: Scope of the welfare evidence shown here question treatment here empirical reference home is selected on this empirical domain alternative welfare construction excluded from the baseline measure correspondence verified for worked households counterfactual attainment in design, not executed reported scope descriptive baseline and bounded preliminary decomposition observed consumption the estimated utility’s own argument alternative consumption benchmark not constructed or reported equivalised reporting primary (§6), using the modified-OECD scale Supporting technical provenance is retained in the source-only provenance block.

Say: This backup slide exists so that any question of the form "why is that not here" has a one-line answer with a document behind it.

## Extended Q&A (beyond the deck's own slide notes)

### Q — What exactly does the preliminary decomposition support?

Say: In a preliminary three-factor structural exercise that holds household resources, needs and composition fixed, equalising systematic utility heterogeneity, coarse geographic/temporal access heterogeneity and earning opportunities changes money-metric well-being inequality by 1.8–9.9% of the baseline Gini, depending on household type and reporting scale. Within the Shapley allocation of that movable component, earning-opportunity heterogeneity has a larger contribution than the coarse geographic/temporal access channel in both samples and both reporting conventions. The preference contribution is not sign-robust to equivalisation.

These are preliminary model-based accounting results, not causal estimates and not the final decomposition of total well-being inequality.

### Q — Why are wage elasticities omitted?

Say: A valid gross-wage perturbation requires new tax-benefit repricing over the affected job alternatives, and the current priced support does not contain that counterfactual. I therefore do not report an approximate or mock elasticity figure.

### Q — The coupled-men accuracy bar is there but the caption calls it close. How close, exactly?

Say: The rule was fixed before either number was computed, which is why I trust the verdict either way. For coupled men's extensive-margin accuracy, the weighted ratio — Monte Carlo standard error over sampling standard deviation — is 0.2398, against a threshold of 0.25: it clears with about one percentage point of the ratio to spare. The unweighted version of the same statistic misses: its ratio is 0.2503, about three hundredths of a percentage point over the line. The deck applies the weighted rule throughout, because that's the protocol specified before either number was seen, and because survey weights are the right unit for a population statistic — not because it's the version that happens to pass.

*(Backup: weighted MC s.e. 0.0018088, simulated sampling s.d. 0.0075443, threshold 0.0018861, ratio 0.239759 — ADEQUATE. Unweighted MC s.e. 0.0014983, simulated s.d. 0.0059854, threshold 0.0014963, ratio 0.250320 — QUADRATURE-LIMITED, excess ≈0.00032 over the 0.25 line. Source details are retained in the provenance note. The binding rule uses weighted results.)*

### Q — Why fix the time endowment at eighty hours? Does that choice matter?

Say: Leisure is defined as eighty hours a week minus hours worked — that's a convention, and the model is not indifferent to it. A diagnostic re-estimation at seventy-five and ninety hours, holding everything else to the certified protocol, shows the fit moves materially in both directions, and at ninety a second leisure-curvature coefficient joins the boundary that is interior at eighty — that's a genuine change in what the model can identify, not just a relabelling of the same optimum. A separate check on the leisure-scale normalizer, by contrast, found a pure units artefact that moves nothing. So eighty hours is a maintained convention, not a free choice the model is agnostic to, and it's on the list of open items rather than settled. The reported magnitudes describe this completed sensitivity diagnostic.

*(Backup: `TOTAL_LEISURE_HOURS = 80.0`, the leisure definition. The sensitivity analysis is documented in the provenance note. negLL vs T=80: singles +4.74 (T=75) / −3.83 (T=90); couples +16.30 (T=75) / −15.13 (T=90). At T=90, `beta_l_age2_sm` joins `beta_l_age2_sf` at its bound. Quote: "T is not pinned down by the data to be flat." Contrast: `lambda_l` normalizer sensitivity in the same report is a pure units artefact, invariant to 1e-6 on derived economic objects.)*

---



<!-- BEGIN READER-VOICE PROVENANCE

Source-only provenance; excluded from rendered reader text.
Specifications: S11; artifact s11_welfare_specs_of_record_v1.json; SHA-256
5FDC88502493CE540B088880EECF049BC268392FF3E8790FFE78A16AA6DDC884.
Welfare definition: Mapping F; artifact JMP_W1_fork_ruling_v1.md; Deputy
ruling R1; SHA-256
7F5D26857D8A96174A9924848F65A02611944273D7775FDC52DC82364A818C05.
Welfare authorization: BASELINE-F-1 and E1; artifact
JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md; SHA-256
54DFD886E41D0A89C1056CBEA5FA51E0A1294D3CA0813F938802BDC3DBD9EE0E.
Welfare aggregates: artifact baseline_f1_verification_v1.md; MNL commit
6048c9f7; independent verification b5550af5; SHA-256
DA7BADF639F3D502D47B301558453D76501C9C44033ECE3F17BDE350BFD5E55F.
Equivalised reporting: E3-EQ; artifact
JMP_BASELINE_F1_equivalised_reporting_v1.md; commit 4c4e07e; scale ruling
"SCALE CLOSED; CHILD-SHIFTER FRAMING", s1; artifact
JMP_SCALE_REVIEW_1_equivalence_scale_economics_v1.md; SHA-256
7CACE61E4476148D05C894729F05FF38F79AF803B9E637449EC76F9CB808014E.
Predictive diagnostics: POSFIT v3; repository MNL_posfit; branch
diagnostics/posfit-v3; commit 96693269; evaluator commit 55bb0d0; artifact
run_provenance.json; SHA-256
BDC3722C325FF8A27BE719AA52A741DF7BEEF9515B4A63554C65E8769EB7F40B.
Bounded decomposition: DECOMP-2; repository MNL_decomp; branch
welfare/preseminar-pab; commit b52761b4; artifact
preseminar_pab_record_v1.json; SHA-256
BCBE4B6FC742DAA39535D5C3EB03BDA0641055A9F5E851B4F53F62FA3E612011.
Diagnostic boundary: DECOMP-DIAG-1; docs/Decomposition_diag_1.txt; SHA-256 EAD1B7C8243FE1498F00DCF287331BEEC94165332AA3BB64041A0F645D339A74; location and common spread in log points.
Presentation: REPORT-V6; all decomposition frames after appendix.

Script generator: beamer/build_rehearsal_script_v6.py.
Extended Q&A source: predecessor reports/rehearsal_pack_v1.md.
Diagnostic Q&A: MNL_posfit/outputs/positive_fit_diagnostics_v3/g2_adequacy.csv; couples_male; extensive_accuracy.
Time sensitivity: MNL@5a8e6bba; experiments/JMP_SEMINAR_SPRINT/runs/ws4_leisure_norm_time_sens/JMP_leisure_normalisation_time_sensitivity_v1.md.
Leisure definition: MNL/scripts/enhanced/enh_RURO_prep_mnl_basic.py:52.
END READER-VOICE PROVENANCE -->
