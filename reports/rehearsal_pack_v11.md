# Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition

## Seminar rehearsal script — V11

The main presentation contains 19 slides. The remaining 10 slides are backup material.

## Main presentation

### Slide 1

On slide: Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition Hisham Haydar LISER and University of Luxembourg France, EU-SILC priced through EUROMOD. Seminar of 17 September. Well-being is measured from two perspectives: the attained bundle (ATT) and the ex-ante opportunity prospect (EA).

Say: Thank you. The question is how much of the inequality in money-metric well-being is attributable to unequal job opportunities rather than to differences in taste, and what happens to that attribution when a model leaves opportunities out. I will show the model, the estimates, the fit, the welfare definition and a descriptive welfare baseline. The computed preliminary restricted-operator decomposition is in the backup appendix. The certified ex-ante calculation is now reported as a separate perspective beside the attained-bundle measure. The two measures disagree about the dominant channel for single-adult households: earnings dominate the realised job, while access is about three times earnings for the whole prospect. Neither perspective is designated primary.

### Slide 2

On slide: Two people with the same tastes and the same wage need not face the same set of jobs.  How much of measured welfare inequality is attributable to unequal job access and earning opportunities, rather than to preferences?  What does a model that assumes a common choice set do to that attribution? Both questions are about a measure, not about a policy counterfactual. 2/19

Say: The two questions are the same two questions as in every version of this paper; nothing in the recent rulings touched them. The first is an attribution question about a money-metric inequality index. The second is a methodological question: a discrete-choice labour supply model that gives every household the same alternatives has to explain non-employment with a taste parameter, and I want to know whether that relabelling survives into the welfare accounting.

### Slide 3

On slide: The contribution is a structural opportunity set plus a welfare measure defined on it.  A random-utility, random-opportunity (RURO) model in which which jobs a household can reach is estimated, not assumed.  Two money-metric welfare perspectives: the bundle a household attains (ATT) and the opportunity prospect it faces (EA).  An exact Shapley decomposition over preferences, geographic/temporal access and earning opportunities, holding household resources, needs and composition fixed. The current decomposition equalises preferences, geographic/temporal job access and systematic earning opportunities while holding household resources, needs and composition fixed. 3/19

Say: The contribution has three parts. Preferences and opportunity components are jointly estimated, with their separation relying on maintained functional-form and exclusion restrictions. The welfare side asks two questions: how well off a household is in the bundle it attains, and how valuable the job prospect it faces is. The certified ex-ante calculation is now reported as a separate perspective beside the attained-bundle measure. The two measures disagree about the dominant channel for single-adult households: earnings dominate the realised job, while access is about three times earnings for the whole prospect. Neither perspective is designated primary.

### Slide 4

On slide: France, EU-SILC priced through EUROMOD: 1 540 single-adult and 2 223 couple households.  Estimation frames: final samples and the current estimated specification.  Estimation frame: each household’s observed job plus 100 drawn alternatives, every one priced through the tax–benefit system.  Fit diagnostics use a separate, larger panel: 2 048 common quadrature nodes per household.  Weights are the survey weights dwt throughout. Results use a single specification throughout. Estimates from earlier, non-comparable sample frames are not shown. 4/19

Say: Two estimation samples, singles and couples, on the corrected sampled-alternative frames. Everything on the slides after this point is the preferred specification. I am deliberately not showing the older S8 or R240 numbers alongside, because the frames differ and a side-by-side would invite a comparison the samples do not support. Each household contributes its observed job and a hundred drawn alternatives, each of which is run through EUROMOD so the consumption argument is a real disposable income, not an approximation. The second number on the slide is a different object: the positive-fit diagnostics (the corrected predictive diagnostics) integrate over a common panel of two thousand and forty-eight priced quadrature nodes per household, not over the estimation draws.

### Slide 5

On slide: A job is a package; a household draws from its own distribution over packages. access employment mass hours piecewise, 35h peak occupation sex-specific wage offer log-normal opportunity density gi(·) over reachable jobs preferences ui(c, ℓ) observed job = arg max over the drawn set Access and capability are not separately identified; the access factor is their product. 5/19

Say: This is the architecture. A job is not an hours cell: it is hours, occupation and a wage, and whether the household can reach it at all. The opportunity density factorises into an access margin, a piecewise-constant hours factor with a peak at the statutory thirty-five hour week, sex-specific occupation availability, and an occupation-conditioned log-normal wage offer. Preferences enter separately. The observed job is the argmax over what was drawn. The identification caveat is on the slide and I keep it there all talk: the access factor mixes personal capability and market availability and the cross-section does not separate them.

### Slide 6

On slide: Preferences and the opportunity density are estimated in one likelihood. Pr(ji | xi) ∝exp  ui(cij, ℓij) + log gi(j) −log qi(j) u preferences g estimated opportunity density q numerical proposal density, divided out The proposal correction is what makes the drawn alternatives a simulator for the estimated set rather than the choice set itself. 6/19

Say: One likelihood, two structural objects. The proposal density is a numerical device: the alternatives are drawn from it and it is divided back out, so it is not part of the economics. That separation matters later, because the welfare measure I am going to define must not depend on the proposal density, and I will show that it does not. Preferences and opportunity components are jointly estimated, with their separation relying on maintained functional-form and exclusion restrictions. No causal interpretation follows from that separation. The baseline deliberately keeps systematic preference heterogeneity parsimonious: age profiles for all four adult groups and a child-related shifter for women. The child term is interpreted as a reduced-form behavioural/time-constraint shifter, not as pure taste. More explicitly, systematic leisure heterogeneity contains an intercept, age, age squared and group-specific leisure curvature for all four groups, plus a child shifter for women; sex and household type are carried by separate parameter blocks.

### Slide 7

On slide: Estimated model: 41 free parameters for singles, 47 for couples. singles couples free parameters 41 47 estimation households 1 540 2 223 objective at ˆθ 6253.463 10283.034 Objectives reproduce exactly under an independent diagnostics reimplementation. 7/19

Say: The headline fact about the estimates is that they are reproducible: an evaluator built separately for the diagnostics work recovers both stored objective values to the last digit shown. That is the precondition for everything on the next two slides. The parameter counts differ because the couples specification pins nothing at the bound while the singles specification pins eleven coefficients by construction.

### Slide 8

On slide: Extensive accuracy is reportable for women in each sample; both groups of men are withheld. 0 20 40 60 80 100 extensive-margin accuracy (%), groups clearing the numerical-adequacy rule single men single women coupled men coupled women withheld: quadrature-limited 85.7% withheld: quadrature-limited 89.8% The preregistered weighted numerical-adequacy threshold is unchanged. Single men and coupled men are quadrature-limited; their extensive accuracy is not reported. 8/19

Say: the corrected predictive diagnostics fully re-evaluates the current estimates after rebuilding the structural band indicators on the priced nodes. The numerical-adequacy rule is applied mechanically at the unchanged threshold. Single women and coupled women clear it. Single men and coupled men are quadrature-limited, so their extensive accuracy is withheld. On the weighted composite decision rule, conditioning is mechanical stochastic conditioning in all four groups. The excess-dispersion adjudication is misspecification evidence for the two couple groups and inconclusive/quadrature-limited for the two single groups. The earlier three-group excess-predictability claim is withdrawn.

### Slide 9

On slide: The remaining common hours mismatch is the observed 37-hour mass point, outside structural FT. single men single women coupled men coupled women 0 1 2 3 4 5 6 7 8 share at the observed 37-hour mass point (%) gap 5.2 pp gap 3.8 pp gap 4.4 pp gap 6.5 pp 37-hour mass point: observed and corrected prediction observed predicted Underprediction of the observed 37-hour mass point is 3.8–6.5 percentage points across groups; this is not a structural full-time-band claim. 9/19

Say: The corrected structural bands use the current model definitions. The observed 37-hour point is isolated as a separate descriptive residual cell, outside the structural full-time band. Its observed-minus-predicted gap ranges from 3.8 to 6.5 percentage points. The population MAE is 0.0140 for singles and 0.0119 for couples. Singles MAE rises slightly, so the correction is not described as an across-the-board fit improvement. The benchmark audit also found a RUM-A input-width defect: its alternative-invariant log-density shift cancels from the conditional likelihood, and RUM-B does not read those rows, but absolute RUM-A opportunity-mass metadata remain a disclosed limitation.

### Slide 10

On slide: The access kernel is estimated, and it varies across households. −4 −3 −2 −1 0 single-adult estimates, log access index; bars are 1.96 x CR1 robust s.e. access constant survey-strata shift regional unemployment regional median income region 2 region 3 region 4 region 5 region 6 region 7 region 8 Single-adult estimates; horizontal bars are 1.96 × CR1 cluster-robust standard errors. Structural and model-conditional; not causal. 10/19

Say: This is the access block of the estimated opportunity density. The point is not any individual coefficient, it is that the block is estimated rather than imposed and that it moves: households in different regional access environments, and in different survey strata, face materially different employment masses at the same preferences and the same wage. This is the evidence that the opportunity side of the model is doing work. It is also the evidence the welfare measure later rests on, which is why I show it before the measure and not after.

### Slide 11

On slide: So is the earning-opportunity kernel: an offer distribution, not a single wage. 0.0 0.5 1.0 1.5 2.0 single-adult estimates, log wage-offer density; bars are 1.96 x CR1 robust s.e. offer location low education high education experience experience squared offer dispersion occupation 2 occupation 3 occupation 4 Single-adult estimates; occupation terms shift the offer location. Dispersion ˆσ = 0.382 (z = 28.7). 11/19

Say: The wage side is an offer density with an estimated dispersion, not a point wage attached to each person. Education and experience shift the location, occupation shifts it again, and the residual dispersion is precisely estimated. Two households with identical observed wages can have different earning opportunities in this model, because what they face is a distribution. That is the second half of what I mean by unequal job opportunities, and together with the access block it is what the welfare measure has to be defined on.

### Slide 12

On slide: Two matched men, almost identical tastes, different opportunity environments. Same occupation group, hours band and wage quintile. A has 14.5 times B’s employment mass; B’s wage-offer location is 11.5 log points higher. A stated-rule teaching example: not causal, not representative. 12/19

Say: What does unequal opportunity mean in this model? These two single men look alike in an income table and have nearly identical estimated leisure profiles. Household A's employment share of opportunity mass is 0.75, household B's 0.17. B's wage offers are better: its offer distribution first-order stochastically dominates A's. But A faces more offers paying at least any given wage over essentially all offer mass. Hours and occupation opportunities are identical by construction in this specification. Neither household is better placed on every margin, and which one is better off depends on the welfare question, which is exactly where the two perspectives come in.

### Slide 13

On slide: ATT: how well off is the household in the bundle it actually attains? W 1 i = mi(o; zi) where ui mi(o), o  = ui(zi) zi attained bundle o the non-employment state mi the money metric The empirical measure uses the universally available non-employment state as its reference. A market-job reference is a sensitivity analysis that requires an unidentified intensity parameter; it is not in the baseline. 13/19

Say: If asked why this reference and not the market-job reference: the fork analysis compared Mapping F, the full feasible set including non-employment, against Mapping M, the market-job universe. R1 rules F primary for the current paper. M at its dense-law endpoint stops being a household-specific object and becomes a whole-market reference, and at finite intensity it needs a set-size parameter the data do not identify. That is recorded as a limitation and as future work, not as a competing headline. I am not claiming F is the right reference in the theory; I am claiming it is the one this empirical specification identifies.

### Slide 14

On slide: Under the current specification W 1 coincides with the staying-home equivalent — as a fact about this domain. W 1 i,F = C obs i exp h Li(jobs i )−Li(o) βc i  Inputs: C obs i , Li(jobs), Li(o), βc — nothing else.  No opportunity density g, no proposal q, no shock ε, no intensity κ.  Current nonworkers: W = C; current workers: W < C under the maintained empirical domain. This is an empirical-domain coincidence under log consumption and universally available non-employment, not a general theoretical identity. 14/19

Say: The most likely question here is whether this coincidence is a general identity. It is not. The coincidence has two ingredients, both specific to what is estimated: consumption enters utility in logs, and non-employment is behaviourally available to every household. Change either and the two measures separate. If asked about the consumption argument: ruling E2 confirms that $C^{\mathrm{obs}}$ must be the exact object entering the estimated utility at the observed state, not a re-chosen normative income concept, and the measure-correspondence audit closed that provenance before the baseline was allowed to run. The empirical the attained-bundle measure implementation evaluates the attained bundle against the universally available non-employment reference. Under the current specification, estimated opportunity density therefore affects this money metric through attained outcomes rather than through a direct opportunity-prospect term. For a one-nat shortfall, $L_i(j_i^{\mathrm{obs}})-L_i(o)=-1$, the illustration is $W=C_i^{\mathrm{obs}}\exp(-1/\beta_c)<C_i^{\mathrm{obs}}$.

### Slide 15

On slide: EA: how valuable is the distribution of job prospects the household faces? Ji = Z eLi(j) Ci(j) λc βcgi(j) dν, Hi = Z eLi(j)gi(j) dν, W EA i = λc exp h log Ji−log Hi βc i  Ji: the actual prospect over the whole estimated opportunity environment.  Hi: same jobs and availability, equal consumption across jobs.  W EA i : the flat consumption that makes the two prospects equally valuable. The two measures answer different welfare questions. ATT evaluates the bundle eventually reached against a common non-employment reference; EA evaluates the whole distribution of potential job outcomes against a reference that keeps the opportunity environment and equalises consumption across jobs. 15/19

Say: The second perspective values the prospect itself. Every job enters, weighted by how available it is and how much the household values it; the reference keeps exactly those jobs and preferences but pays every job the same. A common rescaling of the opportunity density cancels, so what matters is how opportunity weight is spread across jobs. Neither perspective corrects the other. Under the extreme-value shocks, log J is the expected utility of the best reachable job up to a constant, so the measure treats taste-shock variety as welfare-relevant; that is a normative position, and I flag it. The ex-ante calculation passed all its numerical checks; that certifies the computation, not causal identification, parameter uncertainty or normative uniqueness.

### Slide 16

On slide: Baseline W 1-F, equivalised, single adults. C eq W 1 F eq households 1 540 1 540 weighted mean 1 766 1 302 weighted median 1 588 1 165 weighted Gini 0.263292 0.249807 Units: EUR/month, household-equivalised (modified-OECD scale); survey weight dwt. A descriptive dispersion comparison, not a welfare-loss index. The modified-OECD scale is used throughout the equivalised results. Singles and couples equivalised levels are never compared. The sample aggregates reproduce to machine precision under an independent reimplementation. This is a descriptive dispersion comparison (C eq against W 1 F eq within the singles sample), not a welfare-loss index. 16/19

Say: Equivalised results are primary on this slide: the household-equivalised Gini of $\Wone_F$ is below the household-equivalised Gini of observed consumption, for singles. I show that as a descriptive dispersion comparison only, not as a welfare-loss statement --- the ratio $\Wone_F/C^{\mathrm{obs}}$ reflects the systematic leisure term at the observed job relative to home leisure, not a monetary loss, and I am not constructing a loss index on this slide. The equivalence scale is the modified-OECD scale, ratified as the primary scale for current JMP distributional reporting by the Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING", section 1, on the economics review in the source analysis; the scale question is closed. The unequivalised construction this equivalises is unchanged and is in the backup appendix.

### Slide 17

On slide: Baseline W 1-F, equivalised, couples. C eq W 1 F eq households 2 223 2 223 weighted mean 2 245 1 311 weighted median 2 063 1 237 weighted Gini 0.226805 0.197403 Units: EUR/month, household-equivalised (modified-OECD scale); survey weight dwt. A descriptive dispersion comparison, not a welfare-loss index. The modified-OECD scale is used throughout the equivalised results. Singles and couples equivalised levels are never compared. Reported separately from singles: no pooled figure, and no cross-sample level comparison is drawn on this slide or elsewhere in this deck. The same independently reimplemented welfare construction and equivalence scale are used as for single adults. 17/19

Say: Same descriptive comparison, on the couples sample. I am deliberately not placing this table next to the singles one: the two are separate estimation frames, the welfare unit differs, and the analysis does not permit presenting a singles/couples equivalised-level comparison as a finding. If asked how the couples numbers compare to singles, the honest answer is that this deck does not draw that comparison, and I would want to see it examined outside a seminar slide before treating it as informative. The scale is the same ratified modified-OECD scale as on the singles slide (Deputy ruling "SCALE CLOSED; CHILD-SHIFTER FRAMING", section 1); ratifying the scale does not license a cross-sample level comparison.

### Slide 18

On slide: The welfare question changes which labour-market inequality matters. ATT: the attained bundle raw equivalised single adult 2.4% 1.9% couple 6.7% 3.5% Earning opportunities > access in both populations and at both scales. EA: the whole opportunity prospect raw equivalised single adult 14.8% 20.3% couple 21.3% 7.9% Singles: access ≃3× earnings; couples: no reversal, earnings > access. The importance assigned to different labour-market inequalities depends on whether welfare evaluates the realised outcome or the opportunity prospect itself. Cells: access plus earning opportunities as a share of each perspective’s own baseline Gini, holding resources, needs and composition fixed. Neither perspective is designated primary. 18/19

Say: This is the comparison to remember. The attained-bundle measure asks what the realised job is worth; earning opportunities dominate because wages drive disposable consumption at that job. The ex-ante measure asks what the whole job prospect is worth; reachability therefore enters directly, and for single-adult households access is 3.3 times earnings before equivalisation and 3.2 times after it. For couples, equivalisation is materially consequential: the ex-ante access-plus-earnings share moves from 21.3 to 7.9 per cent and the preference contribution turns negative. I make no directional preference claim and do not designate either welfare perspective as primary. All cells come from a restricted accounting that holds resources, needs and composition fixed; they are not causal or total opportunity shares.

### Slide 19

On slide: What I would like from you today.  Is universally available non-employment the reference you would want for this question?  Which counterfactual attainment estimand would you defend?  What would convince you the access kernel is identified, given that access and capability are not separated? Thank you. 19/19

Say: Three questions, in the order I most need answers. The reference domain choice is normative and I would like it challenged. The attainment estimand is the blocking design decision. And the access identification caveat is the one every discussant raises; I would rather hear what evidence would settle it than defend the current position.

## Backup / appendix

### Backup slide 1

On slide: Preliminary restricted-operator decomposition The attained-bundle and ex-ante decompositions apply the same restricted three-pathway game while holding resources, needs and composition fixed. The ex-ante calculation is numerically certified; the attained-bundle counterfactual remains preliminary. Neither is a comprehensive or causal share of inequality due to all opportunities.

Say: The attained-bundle and ex-ante decompositions apply the same restricted three-pathway game while holding resources, needs and composition fixed. The ex-ante calculation is numerically certified; the attained-bundle counterfactual remains preliminary. Neither is a comprehensive or causal share of inequality due to all opportunities.

### Backup slide 2

On slide: This bounded decomposition equalises three channels, not whole job access. P systematic utility heterogeneity (tastes + reduced-form time constraints) →common reference A local geographic/temporal access shifters (region, urban/rural, year) →common reference B wage-offer location →common reference location Household resources, needs and composition are held fixed; adding them as a fourth pathway D is a planned extension, and A + B + D would not be an opportunity share. Personal occupation access and hours-band access are not equalised by A.

Say: For the preliminary restricted decomposition, $A$ is local geographic/temporal access shifters (region, urban/rural, year). It is not personal occupation access, hours-band access or full job access. Children enter the current structural specification through a reduced-form female time-constraint shifter. In a unitary labour-supply model this term may capture both tastes and childcare/home-production constraints; we therefore do not interpret it as pure preference heterogeneity. The baseline deliberately keeps systematic preference heterogeneity parsimonious: age profiles for all four adult groups and a child-related shifter for women. The child term is interpreted as a reduced-form behavioural/time-constraint shifter, not as pure taste.

### Backup slide 3

On slide: The bounded decomposition is executed; the final attainment estimand remains under design. coalition S counterfactual environment carried realised draws W 1 F (zS i ) inequality IS bounded decomposition route This exercise reuses the already-priced estimation panel with no re-estimation and no new pricing. The final decomposition’s counterfactual-attainment estimand remains under design.

Say: The preliminary exercise carries the household's realised draws through each counterfactual environment. That is an executed, bounded accounting route, not the final counterfactual-attainment estimand. The final design still has to choose between a realised-bundle route with conditioned latent heterogeneity and an ex-ante $g$-computation route; the inequality of expected welfare is not the expected inequality of welfare.

### Backup slide 4

On slide: Preliminary restricted-operator decomposition In a preliminary three-factor structural exercise that holds household resources, needs and composition fixed, equalising systematic utility heterogeneity, coarse geographic/temporal access heterogeneity and earning opportunities changes money-metric well-being inequality by 1.8–9.9% of the baseline Gini, depending on household type and reporting scale. Within the Shapley allocation of that movable component, earning-opportunity heterogeneity has a larger contribution than the coarse geographic/temporal access channel in both samples and both reporting conventions. The preference contribution is not sign-robust to equivalisation. This percentage is the change generated by the declared restricted P/A/B game. It is not an estimate of the total fraction of inequality caused by unequal job opportunities. These are preliminary model-based accounting results, not causal estimates and not the final decomposition of total well-being inequality.

Say: The decomposition is bounded by design because household resources, needs and composition are held fixed. Within that bounded game, equalising P/A/B changes the Gini by 1.8--9.9% of its baseline level, depending on sample and reporting scale. The restriction is by construction; the realised numerical magnitude is a model result under that restriction. Dispersion in consumption is quantitatively large relative to dispersion in log well-being: Var(log C) is roughly 100--127% of Var(log W), with the excess offset by a large negative covariance between consumption and the leisure valuation. the preliminary restricted decomposition holds household resources, needs and composition fixed, leaving important sources of dispersion outside the P/A/B allocation. If asked about wage elasticities: a valid gross-wage perturbation requires new tax-benefit repricing over the affected job alternatives, and the current priced support does not contain that counterfactual. This percentage is the change generated by the declared restricted P/A/B game. It is not an estimate of the total fraction of inequality caused by unequal job opportunities. The preliminary attainment exercise is evaluated on the already-priced estimation panel. That panel sparsely represents the lower part of the structural hours support. A separate integration audit shows substantial structural mass in that region. The direct importance of this limitation for the current attained-bundle decomposition has not been fully quantified, so the result remains explicitly preliminary.

### Backup slide 5

On slide: The earnings operator equalises wage-offer location only. The earning-opportunity channel equalises wage-offer location only: the systematic differences associated with education and potential experience, which shift offer locations by at most about 0.10 log points. The common offer spread (about 0.37 log points), wage-draw luck and selection remain in the residual and are quantitatively larger than the location differences removed by this operator. This is a definitional boundary of the exercise, not a measurement error. Equalising locations can change attained wages; it does not equalise the whole wage distribution. The diagnostic comparison that also compresses the common spread and selection is a bound, not an additional decomposition result. Thin effective support for couples leaves individual wage attainment noisy and remains a numerical limitation.

Say: The earning-opportunity channel equalises wage-offer location only: the systematic differences associated with education and potential experience, which shift offer locations by at most about 0.10 log points. The common offer spread (about 0.37 log points), wage-draw luck and selection remain in the residual and are quantitatively larger than the location differences removed by this operator. This is a definitional boundary of the exercise, not a measurement error. Equalising locations can change attained wages; it does not equalise the whole wage distribution. The diagnostic comparison that also compresses the common spread and selection is a bound, not an additional decomposition result. Thin effective support for couples leaves individual wage attainment noisy and remains a numerical limitation.

### Backup slide 6

On slide: Baseline W 1-F, unequivalised, single adults (verification backup). households 1 540 weighted mean 1 435 weighted median 1 320 weighted Gini 0.238 observed workers 1 336 observed non-workers 204 Units: household EUR/month, unequivalised; survey weight dwt. Descriptive baseline; no counterfactual, no decomposition, no causal reading. Secondary/verification slide: the equivalised singles slide (§6) is primary. The sample aggregates reproduce to machine precision under an independent reimplementation.

Say: This is the literal observed-bundle the attained-bundle measure distribution before equivalisation, kept here so any question about the un-scaled level or about worker/non-worker counts has a one-slide answer. It is not the headline: the equivalised slide in §6 is. For non-workers the measure equals observed consumption exactly by construction; for workers it is strictly below it.

### Backup slide 7

On slide: Baseline W 1-F, unequivalised, couples (verification backup). households 2 223 weighted mean 2 496 weighted median 2 356 weighted Gini 0.210 observed workers 2 173 observed non-workers 50 Units: household EUR/month, unequivalised; survey weight dwt. Descriptive baseline; no counterfactual, no decomposition, no causal reading. Secondary/verification slide: the equivalised couples slide (§6) is primary. Reported separately from singles. No pooled figure: the two samples are separate estimation frames and the welfare unit differs.

Say: The couples backup is on its own slide and there is no pooled row: the two samples are separate estimation frames with different welfare units, and even on the ratified modified-OECD scale this deck never compares singles and couples levels. These are unequivalised household totals: couples pool two earnings streams, and the non-employment count is small. The pricing-floor issue that affects the neither-work bundle for a subset of couples does not enter here, because this baseline is evaluated at the observed bundle and never prices the home state.

### Backup slide 8

On slide: Pre-registered checks for the baseline W 1-F measure check singles couples non-workers, max |W 1 −C obs| 0 0 workers, ratio outside (0, 1) 0 0 dependency test (g, q, ε, κ) PASS PASS worked-household correspondence test PASS PASS indifference identity, max |∆u| 1.8e-15 1.8e-15 guards triggered 0 0 All six checks were pre-registered before execution. Worker-ratio violations were to be explained, never clipped; none occurred.

Say: The checks are the reason the baseline is presentable. C1 and C2 are the model-implied domain conditions. C3 is the dependency test: the baseline API accepts no opportunity density, no proposal, no shock and no intensity, and does not read them indirectly. C5 inverts the utility numerically and confirms the indifference identity to machine precision.

### Backup slide 9

On slide: Quadrature adequacy for extensive-margin accuracy group extensive accuracy status coupled women 89.8% reported (ratio 0.05) single women 85.7% reported (ratio 0.10) coupled men — quadrature-limited, withheld single men — quadrature-limited, withheld Weighted, all households. Ratio is Monte Carlo s.e. over sampling s.d.; the pre-registered criterion is ≤0.25. Node bootstrap over 2 048 common quadrature nodes per household (diagnostic panel, not the estimation draws). Simulated bands: 500 outcome vectors at fixed ˆθ. Source: individual-level predictive diagnostics.

Say: The gate was fixed before the statistics were computed. It asks whether numerical integration error is small enough relative to sampling variation for the statistic to be a statement about the model rather than about the quadrature. Withholding rather than downgrading is deliberate: a quadrature-limited number carries no information about fit.

### Backup slide 10

On slide: Scope of the welfare evidence shown here question treatment here empirical reference home is selected on this empirical domain alternative welfare construction excluded from the baseline measure correspondence verified for worked households counterfactual attainment in design, not executed reported scope descriptive baseline and bounded preliminary decomposition observed consumption the estimated utility’s own argument alternative consumption benchmark not constructed or reported equivalised reporting primary (§6), using the modified-OECD scale Supporting technical provenance is retained in the source-only provenance block.

Say: This backup slide exists so that any question of the form "why is that not here" has a one-line answer with a document behind it.

## Extended Q&A

### What are the two welfare perspectives?

The two measures answer different welfare questions. The attained-bundle
measure (ATT) evaluates the bundle eventually reached against a common
non-employment reference: how well off is the household in the bundle it
actually attains? The ex-ante measure (EA) evaluates the household's entire
distribution of potential job outcomes against a reference prospect that
preserves the same opportunity environment while equalising consumption across
jobs: how valuable is the distribution of job prospects it faces? Neither
corrects the other, and neither is designated primary.

### What does the decomposition hold fixed?

The current decomposition equalises preferences, geographic/temporal job access
and systematic earning opportunities while holding household resources, needs
and composition fixed. Those receive no allocated share. Adding them as a
fourth pathway is a planned extension; if it is added, access plus earnings
remains the labour-market opportunity component, and the broader
non-preference total would not be an opportunity share.

### What do the matched households show?

Two employed single men with the same occupation group, hours band and wage
quintile and nearly identical estimated leisure profiles face very different
access, while the one with less access has the better wage-offer distribution.
Neither is better placed on every margin. It is a stated-rule teaching example,
not causal and not representative.

### What is the central result?

The importance assigned to different labour-market inequalities depends on
whether welfare evaluates the realised outcome or the opportunity prospect
itself. Under attained-bundle welfare, earning opportunities matter more than
access. Under ex-ante welfare, access becomes much more important for
single-adult households. Couples show no such reversal.

### Why do they disagree about the dominant channel?

The ex-ante measure values the whole prospect, so reachability matters directly.
The attained-bundle measure sees only the realised job, where wages drive
disposable consumption. Earning opportunities dominate the attained-bundle
accounting. For single-adult households, access is about three times earning
opportunities in the ex-ante accounting. Earnings remain larger for couples.

### What are the ex-ante magnitudes?

Access plus earning opportunities accounts for 14.8% of baseline ex-ante
inequality for single adults on the raw-household basis and 20.3% after
equivalisation. For couples the corresponding figures are 21.3% and 7.9%.
These are restricted accounting shares, not total or causal opportunity shares.

### Why is the couples scale result flagged?

Equivalisation moves the couples ex-ante access-plus-earnings share from 21.3%
to 7.9% and turns the preference contribution negative. The scale convention
is materially consequential, so no directional claim about preferences is
made.

### Are the ex-ante results numerically certified?

Yes. All twelve declared checks pass for both household types, including
reference-integral accuracy, effective sample size, wage-tail control, two-seed
stability, analytical identities, Shapley closure and an independent
implementation. That certifies the calculation, not the model's maintained
economic assumptions or a causal interpretation.

### How should the earlier figures near 90% be understood?

They described all non-preference circumstances, including household resources
and composition, not job opportunities. They are not comparable with the
restricted access-and-earnings figures in the current results.

### What remains preliminary?

The attained-bundle counterfactual is still subject to ongoing numerical
validation, especially because its finite integration sample sparsely covers
short hours. Both decompositions hold resources, needs and composition fixed;
neither propagates parameter uncertainty.
