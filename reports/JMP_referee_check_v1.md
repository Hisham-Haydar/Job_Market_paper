# JMP referee check v1

**Audited:** [research story report v15](JMP_research_story_report_v15.html), against [Referee_report_v1.md](Referee_report_v1.md), the executed model and decomposition code, result records, number registry, diagnostics, and the supplied literature markdown corpus. Audit date: 15 September 2026.

**Scope:** C1–C5, D1–D5, and the six additional priorities. This is a factual-premise audit, not a response defending the paper or accepting the referee's publication recommendation. Compound objections are split where their premises have different verdicts. Suggestions for future research are not treated as established empirical findings.

The companion theory paper, the missing stage-4 certification-JSON attachment, and the sampling distribution of the welfare statistics are excluded as instructed. The stage-4 **code** and the available economist-facing result memo are used to identify the executed aggregation and reported results; the stage-4 certification JSON was not audited. No estimation, pricing, welfare simulation or source-file modification was performed.

## Verdict conventions and locations

- **FALSE:** the stated factual premise is contradicted by the artifacts.
- **TRUE — already disclosed:** the premise holds and v15 states or displays it. A table counts as disclosure; incomplete emphasis is not non-disclosure.
- **TRUE — undisclosed:** the premise holds but v15 does not explain it, or presents incompatible statements without acknowledging their incompatibility.
- **UNVERIFIABLE:** the artifacts do not settle the proposed inference, empirical effect or evaluative judgment.

Only **TRUE — undisclosed** findings enter the Wednesday action list below. This classification does not decide whether a disclosed limitation is economically important.

**Location notation:** `R:Lxxx` means the physical line in `reports/JMP_research_story_report_v15.html`, including appendix lines. Named headings make these locations usable in the rendered report. Other code locations use physical lines and function names; JSON locations use keys. Linked source abbreviations are defined at the end. The audited paper repository started at commit `76454c2f06f381ddaa1b68de5a8dc102c1964aaa`; evidence was read from the actual workspace, which already contained unrelated changes.

## 1. Priority determinations

| Priority | Determination | Verdict and disclosure |
|---|---|---|
| 1. C2 aggregation | ATT takes a household-weighted Gini **inside each replication**, then averages those Ginis. EA integrates and inverts **within each household**, then takes the household-weighted Gini. These are **different aggregation orders**. | ATT implementation: **TRUE — already disclosed**, R:L2883–2884. The explicit ATT/EA aggregation contrast is **TRUE — undisclosed** in the main comparison. Details in C2. |
| 2. D1 employment indicator | The displayed factorisation leaves employment access outside the employment indicator. The executed criterion multiplies the access terms by the relevant working indicator. | Equation/code mismatch: **TRUE — undisclosed**. A correct caption elsewhere does not acknowledge the mismatch. |
| 3. D2 consumption domain | EA H-F gives non-positive actual consumption zero contribution to J, while retaining the state in H. The claim that Section 3 evaluates only the observed job and a screened positive home state is incompatible with that implementation. The likelihood's purported one-euro floor is also a stale description. | EA convention: **TRUE — already disclosed**, R:L2904. Conflicting Section 2/likelihood descriptions: **TRUE — undisclosed**. |
| 4. Participation figure/table | Table: 0.8675212422; embedded figure's 2,048-node endpoint: 0.7613025543. **The table is right as a transcription of the certified S11 participation source.** The figure accurately transcribes a separate diagnostic and does not match that source. | Unreconciled presentation: **TRUE — undisclosed**. Which approximation is closer to the continuous-model probability is **UNVERIFIABLE** from this comparison. |
| 5. “Neither route” | The sentence exists, but says **“for a final decomposition.”** The preliminary ATT decomposition was executed. The two earlier proposed final ATT estimands differ from the executed mean-of-Ginis exercise. | “No decomposition was executed” is **FALSE**. Literal non-execution of the two final routes is **not shown stale** by execution of this preliminary exercise. The dangling reference to two unnamed routes is **TRUE — undisclosed**; see §2. |
| 6. D5 identifiers | All 41 singles and all 47 couples Coordinate cells are empty, although the source parameter tables contain names. | **TRUE — undisclosed**. |

## 2. Additional priority: the appendix's “neither route” sentence

**Claim.** The appendix still says neither counterfactual-attainment route was executed although a decomposition was executed.

**Exact passage:**

> “Neither counterfactual-attainment route for a final decomposition is executed here.”

**Location:** R:L2884, “Implementation record: attained-bundle counterfactual simulation.” It is outside the historical-status subsection, which starts at R:L2994. Immediately before it, R:L2883–2884 describes the executed Gumbel-max simulation and the mean over 1,000 replications.

**What settles it:** [ATT-run], `simulate` and `decompose`, L236–286; [ATT-record], `replications=1000`, `samples.{singles,couples}.coalition_values` and `.shapley`; [ATT-memo], L9–17, explicitly marks the preliminary three-factor decomposition complete and distinguishes it from the final architecture.

**Necessary qualification on “stale.”** The earlier [v11 generated report](research_story_build/story_v11.generated.md), L2212, identifies two proposed final estimands: conditioning the latent behavioural state on the observed choice, and integrating household attained welfare over counterfactual choices before inequality is calculated. It explicitly distinguishes them from the preliminary simulation. The executed code draws ordinary Gumbels without conditioning them on the observed choice ([ATT-run], L243–256), and calculates the Gini before averaging ([ATT-run], L266–286). EA instead inverts J/H; it is not the expected attained-welfare construction.

Thus the artifacts do **not** establish that the literal claim about those two **final** ATT routes is stale. They decisively falsify a broader reading that no counterfactual decomposition ran. What is stale in the presentation is the unexplained “neither”: v15 no longer names the two routes whose non-execution it asserts. **TRUE — undisclosed** for that missing distinction; **FALSE** for no preliminary execution. Do not replace the sentence with a claim that a final ATT route has been completed.

## 3. Major points

### C1. Preference–opportunity separation

**Referee's claim:** The separation rests on maintained restrictions whose credibility for the attribution is not established; the literature does not automatically validate their application here.

| Factual premise | Verdict | Settling evidence; disclosure in v15 |
|---|---|---|
| Leisure preferences are smooth; hours opportunities are bandwise; local unemployment, region and urbanisation are excluded from utility; wage offers do not depend on offered hours conditional on occupation and the specified covariates. | **TRUE — already disclosed** | [Single-spec], L76–99, L163–192 and access interactions through L238; [Couple-spec], L50–76, L146–175; [EA-core], `household_terms`, L122–148, and `log_kernel_rel`, L152–169. The executed S11 reconstruction is [ATT-core], `public_spec`, L231–243: it overrides the older base specification's fixed consumption coefficient, so the base YAML alone is not the complete executed specification. R:L300–332, L347 and L2041 disclose the restrictions. |
| Outside the restricted class, replacing additive utility v by v+a and g by g exp(-a) preserves exp(v)g and hence the choice law. | **TRUE — already disclosed in substance** | Direct substitution in R:L318–319 proves the identity. R:L347 says choices alone do not separate tastes and availability; R:L2041 repeats the reliance on restrictions. The exact transformation is not printed, but the non-separation premise is disclosed. |
| Dagsvik–Jia and Capéau et al. discuss residual nonparametric non-identification. | **TRUE — already disclosed in substance** | Corpus checks L1–L2 below. R:L29 and L347 acknowledge inherited restrictions and their maintained status. |
| The fitted parameter vector is unidentified within the imposed specification. | **UNVERIFIABLE as a general identification claim; not alleged by the referee** | The referee explicitly disclaims this inference (C1, referee L63). R:L2135–2136 reports local optimisation/curvature evidence and explicitly disclaims proof of global uniqueness. Neither that evidence nor the unrestricted transformation decides identification in the restricted model. |
| Direct local-condition utility effects or residential sorting actually contaminate the estimated access block in this sample. | **UNVERIFIABLE** | These are possibilities in referee L65, not documented findings. The specification excludes such direct effects; exclusion does not establish their absence in the population. R:L2041 already states the conditional interpretation and lack of an orthogonality result. |
| The requested alternative restrictions would materially change the Shapley allocation, or the current restriction set is economically insufficient. | **UNVERIFIABLE** | The inspected records document the maintained P/A/B game, not the requested comparison allowing local utility effects, different leisure flexibility and hours-dependent wages. The lack of such a result in v15 does not establish its outcome. No concession about the direction or size of attribution bias follows. |

**Literature verdict:** no mischaracterisation found for the two C1 citations. Their nonparametric statements should not be turned into a claim that this particular parametric estimate is unidentified.

### C2. Numerical comparison, estimand and aggregation order

**Referee's claim:** The welfare-perspective explanation is stronger than the numerical evidence; the ATT allocation averages Ginis of simulated realisations, not the observed distribution or household expected attained welfare.

**Executed order — settled from code, not inferred from the table caption.**

In [ATT-run], `simulate`, the loop over replications begins at L243. At L250–256 it generates common Gumbel draws and obtains each household's attained welfare under each coalition. L262 pools the household groups; L266–267 calculates the cross-household weighted Gini, raw or equivalised. `decompose`, L283–286, then supplies **the mean of those replication Ginis** to Shapley. [ATT-core], `attained_welfare`, L694–703, shows that shocks choose the bundle and do not enter its monetary welfare value.

For coalition S and equivalence scale m_i, the executed ATT object is

\[
 I^{ATT}(S)=\frac1{1000}\sum_{r=1}^{1000}
 \mathcal G_w\!\left(\{M^{ATT}_{ir}(S)/m_i\}_i\right).
\]

It is **not** \(\mathcal G_w(\{1000^{-1}\sum_r M^{ATT}_{ir}(S)/m_i\}_i)\).

In [EA-compute], L88–107, integration produces each household's J and H-F and then `WF = lam * exp((log(J)-log(HF))/beta)`. [EA-aggregate], `results_block`, L51–60, takes one Gini across these household WF values. L124–125 and L151–152 report stream A and keep stream B as a separate stability result; the reported EA Gini is not the average of the two streams' Ginis.

\[
 I^{EA}(S)=\mathcal G_w\!\left(\{\lambda_c[J_i(S)/H_i^F(S)]^{1/\beta_c}/m_i\}_i\right).
\]

**The aggregation orders differ. ATT averages after inequality; EA integrates and inverts before inequality.** EA is also not generally the expectation of the ATT money metric. Consequently the comparison differs in aggregation as well as in welfare object, reference and treatment of shocks; changing integration accuracy alone would not remove that distinction.

| Factual premise | Verdict | Settling evidence; disclosure in v15 |
|---|---|---|
| ATT coalition values are means of replication-specific Ginis. | **TRUE — already disclosed** | Code above; [ATT-record], `replications`, `.coalition_values`; R:L2883–2884 explicitly gives the simulation and averaging sequence. |
| ATT and EA use the same aggregation order. | **FALSE** | Code above. Also, the attached referee does **not** assert this: C2, referee L97–125, gives the mean-of-Ginis ATT equation and distinguishes it from inequality of expected welfare. The report's “same operators” is not “same aggregation order.” |
| The main definition/comparison does not explicitly state the different aggregation orders. | **TRUE — undisclosed** | R:L440 uses a single generic Gini definition for both perspectives; R:L411, L2017 and L2049 discuss different welfare questions/integration supports without stating the expectation-versus-Gini distinction. Appendix disclosure of ATT's construction is present but the explicit comparison is missing. |
| Observed equivalised singles ATT Gini 0.2498 and simulated baseline 0.2451 concern different objects. | **TRUE — already disclosed** | [ATT-validation], `singles.equivalised`: observed `0.24980721054552937`, model `0.24509171934146293`. R:L1416/L1432 displays the observed result; R:L1610 identifies the coalition table as simulated, with baseline at L1680. This is not a numerical contradiction. |
| “Change from actual” denotes change from a simulated baseline, not from the observed Gini. | **TRUE — already disclosed in the caption's simulation description; label remains misleading** | [ATT-run], coalition-table output L461–469 in the MNL_decomp copy, subtracts mean EMPTY from mean coalition Gini. R:L1608–1616 and L1736–1742 label this “actual” while explicitly describing simulation. Correct labelling belongs with the missing main estimand definition, not a claim that the simulation was hidden. |
| The finite ATT support's short-hours limitation and its unquantified attribution effect are disclosed. | **TRUE — already disclosed** | [ATT-core], `N_ALTS` and accepted-panel construction; R:L6, L2017, L2036, L2049. R:L2036 explicitly says its direct effect has not been fully quantified. EA uses a different design: [EA-memo], L12–43. |
| A second seed or exact Shapley closure establishes accuracy relative to the continuous opportunity distribution. | **FALSE** | [ATT-run], L243–256 and L302–305, changes simulation draws on the same panel. Shapley operates on the supplied coalition Ginis. R:L2034 and L2049 already separate simulation, arithmetic and integration limitations. The referee correctly rejects this inference. |
| Numerical inadequacy explains the reversal, or the reversal would survive an adequately integrated ATT calculation. | **UNVERIFIABLE** | Neither direction is established by the current comparison. R:L2017/L2049 explicitly permits integration to explain part of the difference; R:L2024 says the singles-versus-couples explanation is not tested. The mechanistic dominance claim is an interpretation, not a theorem of either formula. |

### C3. The moving own-opportunity reference

**Referee's claim:** EA is a well-defined monetary index on its stated domain, but a moving own reference can neutralise opportunity improvements; ATT and EA also treat shocks differently.

| Factual premise | Verdict | Settling evidence; disclosure in v15 |
|---|---|---|
| H preserves the household's own opportunity environment; common intensity rescaling cancels. | **TRUE — already disclosed** | [EA-compute], L97–107 and L118–125; R:L388–406. |
| With positive consumption and beta_c>0, the index is a leisure-and-opportunity-weighted power mean of consumption. | **TRUE — already disclosed through the defining equations** | Dividing R:L382–391 and raising R:L396–399 to beta_c cancels lambda_c. The weights are exp(L)g/H, not choice probabilities proportional to exp(L)g C^beta_c. Executed implementation: [EA-compute], L88–107. |
| Adding positive offer mass with a lower weighted C^beta_c can lower this index while increasing J under fixed non-employment normalisation. | **TRUE — undisclosed** | From the displayed/implemented ratio, write \(Q(t)=(A+tx)/(H+t)\). Then \(Q'(t)=(xH-A)/(H+t)^2<0\) when \(x<A/H\), while the numerator rises if x>0. Since beta_c>0, the monetary index falls. This is a conditional algebraic property, not a measured effect in the French sample. R:L403–408 discusses composition and common rescaling but does not state this expansion property. |
| Constant consumption makes the index equal that consumption irrespective of the opportunity environment. | **TRUE — already disclosed** | [EA-compute], L114–116; [EA-memo], L82; R:L2949, “Constant-consumption identity.” The referee explicitly recognises prior disclosure. |
| ATT excludes the realised taste shock from welfare, whereas EA is given an expected-maximum interpretation involving taste shocks. | **TRUE — already disclosed separately** | [ATT-core], L687–703; R:L363–375 excludes a shock term. R:L408 explicitly discusses the EA interpretation and its normative dependence on interpreting shocks as tastes rather than errors. |
| The “Outcomes versus prospects” comparison omits the shock-treatment asymmetry. | **TRUE — undisclosed in that comparison** | R:L411 and L2024 present the outcome/prospect contrast without distinguishing this asymmetry. The facts are available elsewhere, but the comparison does not say that it changes more than timing. |
| Decoster–Haan first calculates state-specific welfare and then probability-weights it. | **TRUE — undisclosed as this specific literature comparison** | Corpus L3 below. R:L31 discusses their normative references, but not their order of aggregation. |
| The stochastic normative justification is inadequate, or the index is normatively invalid. | **UNVERIFIABLE** | The code and equations establish a construction and the properties above, not acceptance of a normative standard. The referee calls it well defined rather than algebraically erroneous. The companion theory is excluded from this audit. |

**Domain qualification:** the referee's power-mean derivation explicitly assumes positive consumption. In the executed H-F convention, a non-positive-consumption state receives zero numerator contribution but retains reference weight. The positive-consumption derivation should not be read as deletion of those states or as permission to take a fractional power of negative consumption.

### C4. Fit inconsistency and validation

**Referee's claim:** The participation figure contradicts the table; joint non-employment is underpredicted; a different integration support or an out-of-fold proposal is not independent structural validation.

#### Participation: both origins identified

| Display/source | Actual value and location | Finding |
|---|---|---|
| V15 corrected singles table, male employment | Observed **0.8805**, model **0.8675**; R:L780–783, under “Predictive fit.” | Matches the number registry and S11 source below. |
| Number registry | [Registry], `gallery.fit`, row `sample=singles, sex=male, margin=employment`: observed `0.880499570183976`, model `0.8675212421778828`. | Agrees with the table. |
| Certified S11 source | [S11-fit], **CSV L2**, same full-precision numbers; [S11-report], L83. | **The table matches this source.** |
| Corrected report input | [Fit-corrected], `moments`, row `model=SINGLES, sex=male, moment=employment`, same values. [Fit-render], L55–60 and L133–146, binds the table to this file. | The correction retains this employment value. |
| Embedded participation-convergence figure | R:L2888–2889, `data-fig="node_convergence_v3b"`, “Numerical convergence of predicted participation as the number of integration points grows.” [Node-CSV], **L19**, gives `singles_male,2048,...,0.7613025542831254,0.880499570183976`. | **The figure does not match the certified S11 participation source.** It does match its own diagnostic CSV. |

The embedded PNG bytes have SHA-256 `dad3d79e4da7c4393482ae3e063ff25074690d318e98d491d4e09ca9b356e70f`, identical to [Node-PNG]. This establishes the image's origin without guessing its endpoint from the pixels.

The source difference is substantive. [Fit-code], `_direct_probabilities`, L109–124, uses the R=100 estimation draws excluding the chosen anchor, handles the non-employment atom separately, and combines its exact weight with Monte Carlo market weights. [Node-code], `build_groups`, L141–164 and L174–192, uses the separate S12 predictive panel, excludes the singles observed anchor, and records `exact_atom=False`; `rqmc_probabilities`, L39–58, normalises the valid sampled-node weights. [Node-provenance] records the corrected panels, the S11 evaluator and the same S11 objective values. This is not evidence that a different structural parameter estimate was used.

**Verdict:** **TRUE — undisclosed** for the unreconciled display discrepancy. The table is the correct report of the certified S11 value; the figure is a faithful separate-support diagnostic. It is not justified to call the figure a transcription error or conclude that the certified approximation is the continuous-model truth. The **10.6219 percentage-point difference** between the two predictions remains numerically unexplained by merely tracing their sources. No displayed figure-to-table reconciliation is present in R:L745–752 or L2885–2889.

#### Remaining C4 premises

| Factual premise | Verdict | Settling evidence; disclosure in v15 |
|---|---|---|
| Joint non-employment is observed at 0.0222 but predicted at 0.0043. | **TRUE — already disclosed** | [Fit-corrected], `moments[model=COUPLES, moment=quadrant::NN]`: `0.022182163362762384` vs `0.004340944461498334`. R:L1092–1094 prints the discrepancy. The prose foregrounds other margins, but the discrepancy is not hidden. |
| Coupled women's 37-hour interval has observed 0.0785 vs predicted 0.0134. | **TRUE — already disclosed** | [Fit-corrected], `moments[model=COUPLES, sex=female, moment=hours::h_36_5_37_5]`: `0.07854562840762848` vs `0.013412446315291626`; R:L1268–1270. R:L752 and L2037 also discuss it. |
| Close marginal participation need not imply close joint non-employment. | **TRUE — already disclosed numerically** | The two marginal probabilities do not determine their joint distribution. The reported spouse-specific rows and the NN row display the distinction. |
| The affected households occupy the lower welfare tail and materially change the couples allocation. | **UNVERIFIABLE** | The aggregate fit table does not link NN prediction errors to household welfare ranks or quantify their impact on phi_A/phi_B. The referee asks for investigation rather than claiming this effect is established. |
| These displays evaluate predictions against the estimation population, not independent held-out structural observations. | **TRUE — undisclosed in the validation description** | [Fit-code], `fit_singles`, L151–173, compares predictions to `is_chosen` rows of the accepted frame. [Node-code], L146–163/L181–192, joins observed outcomes from the estimation frame. R:L745 says “not an in-sample fitted choice” and “tests the model away from the realised choices”; it does not explicitly state that these remain the same estimation households/outcomes. Distinguishing population probabilities from sampled-set probabilities is correct; independent validation does not follow. |
| Out-of-fold fitting of the proposal is itself out-of-sample validation of structural parameters. | **FALSE** | [S10-prepare], L1–7 and L26–29, corrects the proposal; [S10-lib], objective constructors beginning L111, fits the structural model on its full supplied frame. R:L2134 correctly attributes out-of-fold fitting to the **proposal**. The paper does not expressly call that alone structural cross-validation; do not attribute that stronger claim to it. |

### C5. Sampling uncertainty of the orderings

**Referee's claim:** Reported channel orderings have no propagated sampling uncertainty, even though v15 acknowledges this; the equivalised couples EA difference is small.

| Factual premise | Verdict | Settling evidence; disclosure in v15 |
|---|---|---|
| The reported ATT/EA decompositions are evaluated at fixed structural estimates; their repeat runs are numerical checks rather than confidence intervals. | **TRUE — already disclosed** | [ATT-run], L236–305, varies the seed after parameters and coalitions have been built. [EA-compute], L189–197/L223–224, loads one parameter vector; [EA-aggregate], L128–139, compares numerical streams. R:L2034 states both the absence of propagated estimation uncertainty and the nature of repeat runs; R:L2884 states fixed estimates. This verifies the nature of these reported runs, without auditing the excluded sampling-distribution item. |
| The displayed EA couples-equivalised contributions differ by 0.00055 Gini points. | **TRUE — already disclosed through the displayed entries** | R:L1944–1945: A=0.00449, B=0.00504; subtraction gives 0.00055. [EA-memo], L117–122, reports the same rounded entries. This is a rounded-entry contrast, not an exact full-precision estimate. |
| Numerical seed stability or individual coefficient standard errors establishes sampling precision of that contrast. | **FALSE** | Those objects do not provide a sampling distribution of the nonlinear contrast. R:L2034 already makes this distinction. The referee correctly rejects the inference. |
| Earnings exceed access in the current couples point estimates, but a population ordering/significance result is established. | **TRUE — already disclosed** for the point ordering; **UNVERIFIABLE** for the population inference | [EA-memo], L117–122, and [ATT-record], `.samples.couples.shapley`, give the point ordering. R:L1955 and L2022 state it. No sampling test is inferred or attempted here. |
| One singles coefficient is bound-active and its treatment matters to a future uncertainty procedure. | **TRUE — already disclosed** for bound activity; the appropriate future procedure is **UNVERIFIABLE** here | [Singles-params], row `beta_l_age2_sf`, and R:L2135/L2147. No sampling-distribution audit was undertaken. |

## 4. Minor points

### D1. Employment indicator in the opportunity factorisation

**Claim/premise:** The printed expression places the access factor outside the employment indicator, so it multiplies home and work alike and cancels from probabilities.

**Verdict: TRUE — undisclosed** for the equation/code mismatch. **FALSE** for an implementation that omits employment access; the referee explicitly does not allege that.

R:L327–328 prints

\[
g_i(j)=g_i^E[g_i^H(h)g_i^{Occ}(k)g_i^W(w\mid k)]^{E_i(j)}.
\]

[Single-spec], L89–92, assigns `beta_E` to `working`; L190–238 gives each geographic/access shifter a working interaction. The executed [Likelihood], L310–314 and L328–340, applies those variables before forming the choice index. A household-common centring term may rescale all masses but does not undo relative employment access. The home-normalised form consistent with the code is

\[
\frac{g_i(j)}{g_i(o)}=
\begin{cases}
1,&j=o,\\
g_i^E g_i^H(h)g_i^{Occ}(k)g_i^W(w\mid k),&h>0.
\end{cases}
\]

For couples it is the product of the spouse-specific factors switched on by their respective working indicators:

\[
\frac{g_i(j_m,j_f)}{g_i(o_m,o_f)}
=\prod_{s\in\{m,f\}}
 [g_{is}^E g_{is}^H(h_s)g_{is}^{Occ}(k_s)g_{is}^W(w_s\mid k_s)]^{E_{is}}.
\]

[Likelihood], L469–500 and L532–559, applies common household shifters to `working_m + working_f` and spouse terms to the relevant spouse indicator. [EA-core], L158–169, independently implements the sum of working-spouse log kernels. This states the opportunity factorisation, not independence of spouses' **choices**, which depend on the joint budget.

**Disclosure:** R:L325 says the blocks are switched off in non-employment; the opportunity-estimates caption also correctly says the employment index multiplies working. Neither acknowledges that the displayed equation fails to do so. Correct prose elsewhere does not resolve the mismatch.

### D2. Non-positive consumption

**Claim/premise:** R:L115 says Section 3 evaluates only the observed job and home state, both already screened positive; EA integrates alternative jobs and retains households with non-positive home consumption.

**Verdict: TRUE — undisclosed** for the conflicting description. The implemented EA domain convention itself is **TRUE — already disclosed** at R:L2904.

The executed conventions are:

| Object | Executed treatment | Settling location |
|---|---|---|
| Likelihood | Non-positive actual-consumption states are outside `in_choice_domain` and receive index **minus infinity**, hence zero probability. The internal `1.0` is a computational guard on masked rows, not a one-euro consumption alternative. | [S10-metadata], `choice_domain_column` and `denominator="literal sum over all in-domain slots"`; [Loader], L581–591, L654–662; [Likelihood], L339–346/L558–564. The upstream [S4-build], L649–668, explicitly preserves raw consumption and removes households with invalid observed choices. |
| Observed ATT | Uses positive observed raw consumption and the difference between attained and home **leisure indices**. It does not require the household's actual home disposable consumption to be positive to use the home leisure reference. | [Baseline-ATT], `build_baseline_f1`, L236–280, and R:L363–375. |
| Simulated ATT | Selects a finite-index, in-domain alternative; asserts positive attained raw consumption; evaluates the ATT formula without its realised Gumbel shock. | [ATT-core], L653–661 and L687–703. |
| EA numerator J | Non-positive home and market consumption contribute zero. | [EA-compute], L88–94 and L102–104. |
| EA full reference H-F | Retains the home atom and **all** market states, including those with non-positive actual consumption: `HF = 1.0 + Msum`. These states receive the common hypothetical reference consumption. | [EA-compute], L97–107. |
| EA H-D sensitivity | Drops non-positive-consumption states from the reference as well. | [EA-compute], L101/L107. |
| EA H-X sensitivity | Excludes households with non-positive home consumption; 73 singles and 60 couples. | [EA-aggregate], L157–162; [EA-memo], L125; R:L2904. |

**Additional correction to the referee's framing:** its request to separate the “likelihood's one-euro floor” repeats v15's description. As a factual account of the executed likelihood, that premise is **FALSE**. The floor statements at R:L115 and L2134 are themselves stale. Do not preserve them as authoritative while correcting only the EA paragraph.

Neither the non-positive home states nor the conflict proves that either monetary welfare formula is undefined: actual consumption in a home state is distinct from the positive hypothetical consumption assigned to a welfare reference.

### D3. Conventional random-utility benchmark

**Claim/premise:** “A standard random-utility model assumes every household chooses from the same set of jobs. Then any difference in what households do has to be a difference in what they want” is too general.

**Verdict: TRUE — undisclosed.** R:L315 contains the passage; R:L11 repeats the second assertion. The report's own model has household-specific consumption budgets and random shocks (R:L289–312). With identical preference parameters and common alternative labels, different net-consumption schedules change utility and therefore probabilities; different random draws also change realised choices. There is no mathematical requirement of a random-utility model that every household have identical feasible alternatives. P003 explicitly discusses both fixed and household-specific sampled choice sets (L38–47, corpus L4 below).

The narrower premise that omitted availability heterogeneity **can** be absorbed into fitted utility is supported by the choice-law factorisation. No artifact establishes that all observed choice differences must be taste differences in a common-opportunity model. The report does not acknowledge or qualify its categorical statement.

### D4. Literature distinction and omitted papers

**Claim/premise:** “Levels versus changes” is an imprecise novelty distinction because the actual Shapley allocation concerns a baseline-minus-equalisation difference; P003 and P080 deserve engagement and are not discussed.

| Premise | Verdict | Settling evidence; disclosure |
|---|---|---|
| The allocation is \(I(\varnothing)-I(PAB)\), a difference between two distributions under the same policy environment. | **TRUE — already disclosed** | R:L440–455; [ATT-run], `decompose`, and [EA-aggregate], `shapley`, L39–48. R:L32–34 already identifies structural operators as the distinction, although “decomposition of a cross-sectional level” can be sharpened. This is not evidence of incorrect arithmetic or a concealed change object. |
| P003 finds choice-set representation can have little effect on observed fit but appreciably larger effects on policy predictions. | **TRUE — undisclosed as a literature comparison** | Corpus L4. Its “out-of-sample” results are hypothetical policy/flat-tax predictions, not necessarily independent held-out observations. The referee's narrower relevance claim is accurate. |
| P080 develops identification of preferences and restricted choice sets, including heterogeneous nonlinear budgets. | **TRUE — undisclosed as a literature comparison** | Corpus L5. These are conditions in its own constrained-choice model; not an automatic identification theorem for this implementation. |
| Those two papers are absent from v15's discussion. | **TRUE — undisclosed** | Full visible-text search found no Beffy, Wennemo, or 2009 reference; inspect R:L27–35 and the bibliography R:L2051–2119. Other Aaberge papers are cited; they do not substitute for P003. |
| Either citation disproves the paper's specific conjunction/priority claim. | **UNVERIFIABLE; not asserted by the referee** | The referee explicitly says neither paper alone invalidates it. No exhaustive novelty or priority audit is claimed here. |

### D5. Parameter identifiers

**Claim/premise:** Both appendix parameter tables promise a Coordinate key but display blank coordinate cells.

**Verdict: TRUE — undisclosed.** Parsing the two tables under R:L2145, “Implementation record: estimated parameter vectors and code names,” finds **41/41 blank singles Coordinate cells and 47/47 blank couples cells**. Singles header R:L2152; first blank cell R:L2162 followed by estimate 8.51993 and CR1 standard error 3.54798 at L2163–2164. Couples header R:L2495; first blank cell R:L2505.

The identifiers exist in [Singles-params] and [Couples-params], column `param`. Singles CSV L2 identifies the first row as **`beta_l0_sm`**, estimate `8.519929455035971`, robust standard error `3.54798180009809`. Thus this is a missing rendering/key problem, not unavailable parameter names. No missing-name warning or alternative complete key is supplied with these tables.

## 5. Targeted literature audit

Canonical, page-mapped markdown files were used, not the `.agent.md` summaries. Physical PDF pages below refer to the corpus's embedded page markers. No original-PDF typography audit or exhaustive literature-priority claim is made. The identification premises below are stated in prose and do not require repairing uncertain extracted formulas.

| ID | Referee characterisation | Corpus location | Verdict / qualification |
|---|---|---|---|
| L1: P077, Dagsvik and Jia (2016) | Excluding non-labour income from opportunities is insufficient for nonparametric identification. | [P077], physical p.8, L162–172, Theorem 2 and following discussion. | **TRUE. No mischaracterisation.** It does not establish non-identification within every restricted parametric model. |
| L2: P074, Capéau, Decoster and Dekkers | Utility and hours-opportunity distribution retain nonparametric confounding. | [P074], physical pp.14–15, §3.2, L594–640; explicit statement at L626–628. | **TRUE. No mischaracterisation.** The filename says 2015; the article header says *International Journal of Microsimulation* (2016), 9(2), 144–191. The referee identifies P074 without making a conflicting publication-year claim. |
| L3: P072, Decoster and Haan (2015) | Calculate welfare in discrete states, then average with choice probabilities. Also compare orderings under different normative metrics (referee §B). | [P072], physical p.17, L1101–1114. | **TRUE. No mischaracterisation.** State-specific monetary transformation precedes expectation. This is not the average of realised cross-sectional Ginis, and is not in general inversion of an expected-maximum index. |
| L4: P003, Aaberge, Colombino and Wennemo (2009) | Choice-set specification can affect observed fit little and policy predictions much more. | [P003], abstract L38–54; simulation/policy discussion L1308–1316. | **TRUE. No mischaracterisation.** “Out-of-sample” here includes predictions under a hypothetical flat-tax reform; do not cite it as proof that the present model fails held-out validation. |
| L5: P080, Beffy et al. (2019) | Identification conditions for preferences and restricted choice sets, with heterogeneous nonlinear budgets. | [P080], abstract L64–76; §3.3.3 L1091–1094 and continuation L1196–1200. | **TRUE. No mischaracterisation.** The paper concentrates on at most two offers in its principal construction and derives conditions; its findings are not blanket identification for any latent-jobs model. |
| L6: P008, Jacquet, Jia and Thoresen (2026), referee §B | Structural job-choice model with conventional and preference-standardised compensating variation. | [P008], L97–102 and L134–153. | **TRUE. No mischaracterisation.** The comparison concerns a tax reform; preference characteristics are set to reference values for circumstance-CV. R:L30 already acknowledges this precedent. |

The report's acknowledgement that it inherits the Shapley allocation (referee §B) is directly confirmed by R:L33 and L457. Nothing in the checked literature establishes the particular empirical channel ordering here. No factual literature mischaracterisation was found in the referee's targeted claims; the qualifications above limit what can be inferred from them.

## 6. Wednesday action list: only TRUE — undisclosed findings

These are document-level actions implied by this audit, **not changes made here**.

1. **C2/C3:** state ATT's mean-of-Ginis estimand in the main definition and explicitly compare aggregation order, references and shock treatment with EA. Make the simulated-baseline label unambiguous.
2. **D1:** put the employment access factor under the correct employment switch, with the home normalisation and couples counterpart.
3. **D2:** reconcile Section 2 and the likelihood appendix with domain masking; remove the false one-euro-floor description and distinguish observed ATT, simulated ATT, EA J and full-reference H.
4. **C4:** reconcile or clearly identify the separate sources/targets of the participation figure and table; say that 0.867521 is the S11 source-of-record value and 0.761303 is the separate-support diagnostic. State that fit comparisons use the estimation population, without implying held-out structural validation.
5. **Appendix wording:** name the two proposed final ATT routes and distinguish their status from the executed preliminary exercise. Do not report the preliminary calculation as unexecuted or a final route as completed.
6. **D5:** restore the `param` identifiers in both Coordinate columns.
7. **C3:** state the moving-reference opportunity-expansion property and identify Decoster–Haan's different aggregation construction.
8. **D3/D4:** qualify the categorical random-utility benchmark and engage the verified P003/P080 comparisons.

Already-disclosed numerical limitations, maintained identification assumptions, printed joint-fit discrepancies and unpropagated estimation uncertainty are **not** classified as newly undisclosed defects. The adequacy of those limitations, the untested mechanism for the reversal, lower-tail effects and population orderings remain **UNVERIFIABLE** here; they are not conceded.

## 7. Source map and audit integrity

The following links identify exact files. Function/line/key locations throughout the report refer to these workspace copies. The active MNL environment resolves `dclaborsupply` inside **`MNL/dclaborsupply-monorepo`**; the similarly named top-level monorepo and older standalone environments are not the executed criterion used for the likelihood/domain findings.

- **ATT-run:** [MNL_decomp/scripts/welfare/run_preseminar_pab_decomposition_v1.py][ATT-run].
- **ATT-core:** [MNL_decomp/scripts/welfare/preseminar_pab_v1.py][ATT-core].
- **ATT-record / validation / memo:** [result record][ATT-record], [baseline validation][ATT-validation], [implementation memo][ATT-memo].
- **EA-compute / aggregate / core / memo:** [stage3_compute.py][EA-compute], [stage4_certify.py][EA-aggregate], [wea_core.py][EA-core], [WEA result memo][EA-memo].
- **Likelihood / Loader:** [active engine_jax.py][Likelihood], [active data/loader.py][Loader].
- **Specifications:** [single-adult base specification][Single-spec], [couples specification][Couple-spec], with S11 overrides in ATT-core and [S10 estimation library][S10-lib].
- **Frame/domain provenance:** [S10 preparation][S10-prepare], [S10 metadata][S10-metadata], [S4 construction][S4-build], [observed ATT evaluator][Baseline-ATT].
- **Parameter keys:** [singles][Singles-params], [couples][Couples-params].
- **Fit lineage:** [certified S11 CSV][S11-fit], [S11 report][S11-report], [corrected fit JSON][Fit-corrected], [render inputs][Fit-render], [criterion-B population-fit code][Fit-code].
- **Figure lineage:** [node CSV][Node-CSV], [node PNG][Node-PNG], [provenance][Node-provenance], [node probability evaluator][Node-code].
- **Registry:** [numbers_of_record_v15.json][Registry].

SHA-256 fingerprints of the reviewed main artifacts:

| Artifact | SHA-256 |
|---|---|
| v15 HTML | `acdc5b860c3e1be52b520f784dba890cf885160fd1ec74a29a1bb0aee47c5318` |
| Referee report | `bca8039ca6040c97051fd9dcf0e2b297a922b4075624c8a0ddf1676182d74ec5` |
| v15 number registry | `c456e6ecb554bb31c0791824cd4734533274d83fa3f282789cf8caca09c79909` |
| ATT-run | `41b769e6712c7ea2e91cdbf5e5c57fc059d33198fae45e2f40d225be55f81005` |
| ATT-core | `1595056d65cb66034d4a1c051247f41e29fa15b62d76f283e2bfb3d13267289e` |
| EA-compute | `75371b95b7dd7f9737c81e7da00f17a79b26d6f246c0b60785228fbd7b508079` |
| EA-aggregate | `7657d0c8c0f242b86874cc4bef3108658aab86a12b15b4c837ee4d6b8f8eecf0` |

[ATT-run]: ../../MNL_decomp/scripts/welfare/run_preseminar_pab_decomposition_v1.py
[ATT-core]: ../../MNL_decomp/scripts/welfare/preseminar_pab_v1.py
[ATT-record]: ../../MNL_decomp/outputs/welfare/preseminar_pab_v1/preseminar_pab_record_v1.json
[ATT-validation]: ../../MNL_decomp/outputs/welfare/preseminar_pab_v1/stage2_baseline_validation_v1.json
[ATT-memo]: ../../MNL_decomp/docs/normative/JMP_preseminar_PAB_decomposition_v1.md
[EA-compute]: ../../MNL_wea/scripts/welfare/wea_sprint1/stage3_compute.py
[EA-aggregate]: ../../MNL_wea/scripts/welfare/wea_sprint1/stage4_certify.py
[EA-core]: ../../MNL_wea/scripts/welfare/wea_sprint1/wea_core.py
[EA-memo]: ../../MNL_wea/docs/wea_sprint_1/WEA_SPRINT_1_result_memo_v1.md
[Likelihood]: ../../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py
[Loader]: ../../MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/data/loader.py
[Single-spec]: ../../MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml
[Couple-spec]: ../../MNL/experiments/JMP_SEMINAR_SPRINT/configs/estimation_spec_couples_clean_r240_v1.yaml
[S10-lib]: ../../MNL/experiments/JMP_SEMINAR_SPRINT/runs/s10_criterion_a_iid_r100/s10_estimation_lib_v1.py
[S10-prepare]: ../../MNL/experiments/JMP_SEMINAR_SPRINT/runs/s10_criterion_a_iid_r100/run_s10_prepare_criterion_a_v1.py
[S10-metadata]: ../../MNL/outputs/corr/s10_criterion_a_iid_r100_v1/engine_metadata_criterion_a_v1.json
[S4-build]: ../../MNL/experiments/JMP_SEMINAR_SPRINT/runs/s4_iid_crossfit_r100/build_s4_iid_crossfit_r100_v1.py
[Baseline-ATT]: ../../MNL/scripts/welfare/baseline_f1.py
[Singles-params]: ../../MNL_decomp/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv
[Couples-params]: ../../MNL_decomp/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv
[Registry]: numbers_of_record_v15.json
[S11-fit]: ../../MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_criterion_b_population_moments_v1.csv
[S11-report]: ../../MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_report_v1.md
[Fit-corrected]: ../../MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/bandfix2_recompute/new_results_v1.json
[Fit-render]: research_story_build/v7_render_inputs.py
[Fit-code]: ../../MNL_posfit/experiments/JMP_SEMINAR_SPRINT/runs/s10_criterion_a_iid_r100/run_s10_population_fit_v1.py
[Node-CSV]: ../../MNL_posfit/outputs/posfit_node_convergence_v3b/convergence_table.csv
[Node-PNG]: ../../MNL_posfit/outputs/posfit_node_convergence_v3b/figures/node_convergence.png
[Node-provenance]: ../../MNL_posfit/outputs/posfit_node_convergence_v3b/run_provenance.json
[Node-code]: ../../MNL_posfit/scripts/diagnostics/build_positive_fit_diagnostics_v2b.py
[P077]: ../JMP_lit_collection/Markdowns/Dagsvik_and_Jia_2016/Dagsvik_and_Jia_2016_Labor_Supply_as_a_Choice_Among_Latent_Jobs.md
[P074]: ../JMP_lit_collection/Markdowns/Capéau_et_al._-_2015_-_Estimating_and_Simulating_with_a_Random_Utility_R/Capéau_et_al._-_2015_-_Estimating_and_Simulating_with_a_Random_Utility_R.md
[P072]: ../JMP_lit_collection/Markdowns/Decoster_and_Haan_-_2015_-_Empirical_welfare_analysis_with_preference_he/Decoster_and_Haan_-_2015_-_Empirical_welfare_analysis_with_preference_he.md
[P003]: ../JMP_lit_collection/Markdowns/Aaberge_et_al_2009_Evaluating_Alternative_Representations_of_the_Choice/Aaberge_et_al_2009_Evaluating_Alternative_Representations_of_the_Choice.md
[P080]: ../JMP_lit_collection/Markdowns/Beffy_et_al_2019_Labour_supply_and_taxation_with_restricted_choices/Beffy_et_al_2019_Labour_supply_and_taxation_with_restricted_choices.md
[P008]: ../JMP_lit_collection/Markdowns/Jacquet_et_al_2026_How_Much_Does_Responsibility_Matter_in_Fairness_Measu/Jacquet_et_al_2026_How_Much_Does_Responsibility_Matter_in_Fairness_Measu.md
