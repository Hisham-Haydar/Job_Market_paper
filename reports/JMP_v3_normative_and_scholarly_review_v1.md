# JMP v3: normative architecture and scholarly presentation review

**Date:** 8 September 2026  
**Disposition:** substantive revision; keep corrective estimation and writing moving in parallel.  
**Retention:** one working review memo, including the consolidated Goal-1 instruction in Section VI. No additional review-document family is needed.

## I. Scope and overall assessment

Reviewed materials:

- `JMP_working_paper_for_seminar_v3.pdf`: all 30 pages, text and rendered pages.
- `JMP_research_story_report_v3.html`: full readable body, structure and rendered layout.
- `JMP_research_story_report_v2.html`: comparison of report design and content coverage.
- `RURO_post_estimation_styled.py`: static inspection of the relevant utility, derivative, plotting, elasticity and density-reconstruction functions; not a complete software certification.
- `jobs_and_wellbeing.md`: the locally available theory draft, dated February 2025, including definitions of Measures 1–5 and the compensation/responsibility axioms.
- `Literature_collection.md`: the existing literature map.
- `fr2016_source_to_estimation_sample_audit_v1.md`: used to check the occupation mapping and the provenance of historical data problems.

The latest theory presentation mentioned by the PI is not present among the current local review attachments. The Goal-1 Manager must locate it in the repository and identify the exact version. The supplied older theory draft does not contain the full current Measure 6. Properties of that updated measure should not be certified from its name or from a secondary project summary.

This review does not re-estimate the confidential model, inspect the server directly, or establish that pending corrective runs have completed. Numerical statements in v3 that are labelled historical remain historical.

### Overall judgment

The mathematical exposition is materially improved. The exact title has been restored. Singles and couples now appear together, the opportunity/choice/proposal distinction is clearer, the reference inversion has an explicit closed form, and the distinction between attribution and isolated equalization is much better explained.

The central remaining problem is not insufficient polish. It is that the economic and normative argument still follows an inherited evaluator rather than establishing why that evaluator is the right counterpart of the chosen well-being criterion. The conversation with François makes this issue central now.

Recommended disposition:

1. Adopt the own-set equal-consumption equivalent, theoretical Measure 1, as the **primary normative target** to be translated into the empirical setting.
2. Do not relabel the current ex-ante flat-consumption integrator as that theory measure without establishing the bridge.
3. Keep the own-set laissez-faire subsidy, Measure 3, as a later contrasting redistribution-relative object, not the primary positive level-inequality metric.
4. Continue the corrected positive estimation, budget reconstruction and manuscript writing. The unresolved welfare bridge blocks promotion of headline welfare results, not all research activity.
5. Restore the report's explanatory design; retain the paper as a separate scholarly argument.

## II. What the ethical discussion establishes—and what it does not

### N1. Start with a normative principle, not a convenient numerical routine

The introduction should explain why a welfare ranking must specify how preferences, the individual's feasible job opportunities, and pay attached to jobs are treated. The behavioural likelihood does not choose this ethical stance.

The proposed reference for Measure 1 is

\[
W_i^1=w \quad\Longleftrightarrow\quad
u_i(z_i)=\max_{j\in A_i}u_i(w,j).
\]

The monetary argument is an equivalent consumption amount. The measure is already money-metric; there is not a second arbitrary conversion from an otherwise complete non-monetary W1 to euros. In the application, consumption units and household interpretation must make the amount monthly euros.

**Source:** `jobs_and_wellbeing.md`, Measures, Measure 1; Representation and Responsibility for Equal Pay.

The older draft associates Measure 1 with Independence of pay and Responsibility for Equal Pay. Its table does **not** label it Full Responsibility. The manuscript should therefore describe a particular own-set, pay-neutral reference, or a mixed compensation/responsibility position, rather than calling it the fully responsibility-oriented endpoint.

Nor does selecting this reference establish that geographic location, education or all estimated preferences are morally chosen. The empirical attribution and a moral verdict remain different statements.

### N2. Independence of ability sets does not eliminate every opportunity effect

The supplied axiom compares situations with preferences fixed and attained bundles held fixed or indifferent:

\[
z\,I_i\,z'\quad\Rightarrow\quad
W(z,R_i,A;y)=W(z',R_i,A';y).
\]

This excludes a **direct reference-set effect at a given attained preference level**. It does not imply

\[
W(z_i(A),R_i,A;y)=W(z_i(A'),R_i,A';y),
\]

when changes in opportunities lead to differently ranked attained bundles.

For example, a staying-home equivalent can change because restricted employment access lowers attained consumption or utility. This is an indirect attainment channel even though the reference itself does not depend on A.

Consequently, do not justify rejecting Measures 4–6 by saying they are mathematically incapable of reflecting inequality caused by opportunities. A more precise motivation is that the PI wants the individual's own opportunities to remain relevant to the **reference evaluation**, not only to the process that produces the attained outcome.

This is a deduction from the stated axiom, not an alternative theorem attributed to François. The exact latest classifications should be checked against the updated theory manuscript.

**Source:** `jobs_and_wellbeing.md`, Independence of A, Full Compensation, Measures 4–5.

### N3. The current flat-consumption functional is not yet an implementation of theoretical W1

The v3 paper, Section 8.1, implements

\[
V_i=\log\int e^{b_i(C_i(j))+L_i(j)}\widehat g_i(j)\,d\nu(j),
\]

and determines \(W_i^{flat}\) from

\[
b_i(W_i^{flat})+
\log\int e^{L_i(j)}\widehat g_i(j)\,d\nu(j)=V_i.
\]

For separable deterministic utility, the theory equation instead becomes

\[
b_i(W_i^1)+\max_{j\in A_i}L_i(j)=u_i(z_i).
\]

There are two substantive replacements: observed/attained-bundle utility is replaced by an integral-based evaluation, and a maximum over the individual's set is replaced by a log weighted integral. They are not equal by algebra. A proof that the current numerical inversion matches its own closed form only verifies that implementation.

Do not write “W1” for both objects without a qualifying superscript and an explicit relationship. The existing evaluator can remain a named stochastic/flat-consumption candidate or a historical comparison. It cannot inherit the deterministic theory's axioms by terminology.

The narrow question for Goal 1 is: what object represents the current outcome and the individual's opportunities, and why does the proposed stochastic evaluation implement or deliberately extend the selected normative reference? Do not presume the answer from an old execution contract.

**Source:** v3 PDF, pp. 6–7 and 17–21; theory Measure 1. **Assessment:** mathematical comparison of the two displayed definitions.

### N4. The current deterministic preference domain creates a potential W1–W4 coincidence

This is the most consequential application-specific deduction.

Suppose the implemented deterministic utility is

\[
u_i(c,j)=b_i(c)+L_i(j),
\]

leisure is positively valued over the relevant domain, there is no intrinsic utility of occupation/work beyond the leisure term, and staying home is always available. At common consumption m, the preferred alternative is then staying home:

\[
\max_{j\in A_i}u_i(m,j)=u_i(m,o).
\]

Thus literal theoretical W1 equals the staying-home equivalent on that restricted preference domain. For couples with positive spouse-leisure weights, additive leisure, no direct interaction and both-at-home available, the analogous statement applies to the joint non-work alternative.

This does not contradict the general theory: the theory admits preferences under which jobs have valued non-pecuniary characteristics. It means that the distinction between its measures can disappear on a narrower estimated utility class.

Further, v3 explicitly states that its positive densities have common support. Changes in their relative intensity are not automatically changes in a deterministic A. Replacing A by the support of g would leave a common set here. Treating the analyst's 100 sampled alternatives as a realised personal ability set would be unjustified.

Goal 1 must check this consequence, including the actual sign/domain of the leisure weights. It should not insert a random-set process, arbitrary accessibility threshold or new job-amenity coefficients merely to prevent the coincidence. If a stochastic extension is proposed, specify it and identify which claims remain valid; if the coincidence is retained, explain it honestly.

**Source:** v3 PDF, Sections 5.1–5.2, pp. 10–13; theory Measures 1 and 4. **Assessment:** conditional deduction, not a claim about every possible random-utility extension.

### N5. An own-set reference does not mean “a bigger set necessarily means higher W”

For fixed attained utility and preferences, enlarging A weakly raises \(\max_{j\in A}u_i(m,j)\). With monotonicity in consumption, the consumption required to match the same attained utility therefore weakly falls. The outcome effect of a changed set can offset or outweigh this reference effect.

The introduction must distinguish measuring attainment relative to own opportunities from assigning an unconditional positive intrinsic value to menu size. Do not promise either general ranking without checking the chosen criterion.

### N6. Measure 3 is useful for a different empirical contrast

The own-set laissez-faire measure is

\[
u_i(z_i)=\max_{j\in A_i}u_i(y(j)+s_i,j).
\]

At the household's own laissez-faire optimum, \(s_i=0\), irrespective of differences across its set or pay schedule. That equal-zero property is a normalization of this welfare object, not evidence of equal economic prospects. Away from laissez-faire, s can be signed and describes an equivalent subsidy relative to that reference.

It is therefore useful for contrasting redistribution relative to own earning possibilities, but is not automatically a positive standard-of-living level. Do not compute the usual logarithmic generalized entropy or Atkinson indices on signed values, and do not add a convenient constant to make them positive. Also specify admissible reference bundles if a negative subsidy makes zero-earnings non-employment consumption non-positive.

Recommendation: W1-oriented primary level evaluation, with Measure 3 as a clearly distinguished later contrast. No full six-measure empirical battery is required to follow the normative direction.

**Source:** theory Measure 3. **Assessment:** domain and interpretation implications of its definition.

### N7. Preserve the separation between two papers without excluding theory from the JMP

The JMP may use a selected principle from Haydar–Maniquet and cite its definition and relevant result. It need not re-prove or empirically implement the entire family. The present repeated disclaimers that the projects are distinct should be replaced by one clear statement of the exact borrowed principle and the empirical extension required.

Use the PI's current attribution: **Haydar and Maniquet (2026), work in progress / unpublished manuscript**. Verify the current title and figure against the version in the repository. Preserve the February 2025 source as historical; do not pretend it already contains the updated sixth measure or latest proof.

## III. Review of the report and paper

### R1. Layout: the report regressed toward a manuscript rendering

The v2 HTML has sticky left navigation, themed information boxes and differentiated explanatory material. The v3 HTML has a simple central text column, no comparable navigation, and a largely paper-like sequence. V3 contains four figure images, compared with 41 image placements in v2; this does not imply that every old plot should return.

Restore the v2 interface while keeping the corrected v3 mathematics. Add a short overview, a navigable sequence of economic questions, worked examples, interpretation boxes and expandable technical notes. Keep evidence/source maps collapsed in the internal report. The report should teach the reader; the paper should argue the contribution.

The v3 bundled mathematical renderer worked offline in the inspection environment. Retain that improvement. Do not copy the old version's stale equations or numerical claims merely to recover its design.

### R2. Title: corrected; keep it fixed

Both v3 documents now use the requested title:

**Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition.**

No further title variation is warranted.

### R3. Abstract: improved opening, incomplete ethical and empirical content

Unlike the earlier abstract, v3 opens with earnings, working time and the economic distinction, not a RURO definition. That improvement should be acknowledged.

It is still a methodological prospectus. Once the normative bridge is selected, add one clear sentence stating the own-opportunity reference principle and its purpose. When corrected findings exist, report the principal result, the actual opportunity contribution rather than the whole non-preference share, and the important sensitivity. Do not invent results to finish the abstract.

Keep build/correction status in one unobtrusive working-draft note. Avoid turning the abstract into an audit response.

### R4. Delete the currency sentence

PDF p. 1 and the opening HTML section say: “The question is therefore not whether income is measured in the right currency.” This contrasts the study with a problem no one raised.

Suggested replacement:

> The question is how much inequality in well-being is associated with differences in accessible job opportunities, once preferences, resources and household needs are treated explicitly. Answering it requires both a behavioural model and a normative rule for comparing individuals whose opportunities and preferences differ.

This is proposed prose, not a description of an already verified empirical finding.

### R5. Literature: more developed than before, but still incomplete and overly defensive

The PDF devotes pp. 2–5 to related literature and lists ten references. Therefore “there is no literature” is inaccurate. The problem is the missing foundations for the selected normative rule, sparse official-data references, and repeated “we do not inherit / not first / not identical” phrasing.

Reorganize around three questions: what identifies preferences and opportunities; what fairness principle determines the money metric; and what the attribution adds relative to the closest empirical studies. State the contribution affirmatively, then delimit it once.

Selected source priorities:

- Dagsvik–Strøm (2006), Dagsvik–Jia (2016), Capéau–Decoster–Dekkers (2016) for job opportunities, functional restrictions, stochastic foundation and estimation.
- Relevant Aaberge–Dagsvik–Strøm/Aaberge–Colombino work already in the corpus for the development of constrained structural labour supply and welfare applications.
- Decoster–Haan (2015), Fleurbaey–Maniquet (2017, and later work where substantively relevant), and equivalent-income foundations for the normative construction.
- Haydar–Maniquet (2026, work in progress) for the selected own-set principle, with the empirical mapping stated separately.
- Jacquet–Jia–Thoresen (2026) as a responsibility-sensitive reform-welfare comparator, not a numerical benchmark for level-inequality shares.
- The actual sampled-alternative methodological source, and the sources defining the inequality/attribution methods used.
- Eurostat and EUROMOD/JRC documentation for the actual data and model.

More references should answer missing substantive questions, not satisfy a numerical quota.

### R6. Original papers: selectively extract, do not halt writing to convert everything

The corpus is a useful discovery and synthesis aid. A summary cannot establish a particular equation, identification restriction, theorem or graphical construction. For those claims, read the original PDF or publisher/institutional full text and preserve page/section references.

Goal 1 should inventory existing original PDFs and text extracts first. Convert only the core papers actually used, with page-aware extraction and a link to the original; check displayed mathematics and figures visually. A complete PDF-to-Markdown conversion project is neither necessary nor a prerequisite for the next draft. Do not cite a generated summary as if it were the original article.

### R7. The requested theory figure is still not the current schematic

PDF p. 6 contains a newly made consumption–leisure motivation figure, and p. 7 contains reference-curve illustrations of the existing evaluator. Thus there are conceptual figures and theory citations. They are not the actual theory-presentation figure requested by the PI.

Locate the current theory presentation in the repository. Select and verify the precise panel illustrating the chosen W1 reference. Reproduce or adapt it with a proper work-in-progress credit and a caption explaining the fixed objects and the monetary equivalent. Do not label a fixed-leisure intersection or an integrated log-sum as a literal W1 maximization unless the relationship has been established.

The empirical same-profile illustration should remain a separate figure, not substitute for the normative illustration. Any smooth budget/indifference depiction claiming optimality must actually satisfy the intended tangency, endpoint or discrete-menu condition.

### R8. Theory reference: present but dated and peripheral

Haydar–Maniquet appears on pp. 5–6 and in the bibliography, as a 2025 companion manuscript. The correction is to use the current 2026 work-in-progress attribution and the exact substantive connection—not merely add an otherwise absent name.

### R9. Data provenance needs a positive description

PDF Section 4 begins with a “French household input delivered for 2016 survey collection.” Spell out EU-SILC, its harmonization by Eurostat, the EUROMOD input transformation, and the tax-benefit simulator separately. Identify the actual access route and input vintage from the authorised data record, rather than assuming Eurostat directly produced every EUROMOD-specific transformation.

State 2016 collection, 2015 income reference and French 2015 policy clearly. Explain the static/full-year employment construction and the mixed timing of current hours/status and annual earnings. Do not call simulated disposable resources observed consumption expenditure.

Official EUROMOD documentation distinguishes its policy rules from the harmonized microdata on which they operate. This is the appropriate institutional citation alongside the precise project input documentation.

### R10. French regional motivation is useful, but discrete administrative regions do not identify causal effects

Give a substantive reason for this application: harmonized household budgets can be linked to regional, education- and sex-specific labour-market indicators within a common national institutional setting.

Do not state that regions are disconnected labour markets merely because they are categorical variables. Administrative discreteness does not supply a regression-discontinuity design, exogeneity of residence or separation from commuting and sorting. Use “regional labour-market heterogeneity” unless “segregation” is defined and measured.

Substantiate the motivation with one map or regional-by-group table using the actual opportunity-year series and the sample's coverage. Do not cite contemporary regional gaps as measurements of the 2015 application.

### R11. GSUR is present, but poorly positioned; its aggregation needs interpretation

The PDF explicitly describes GSUR on p. 12 and gives Eurostat series identifiers on p. 29. The HTML has the same model description and source appendix. It is not absent.

Move its definition and role into the data/identification narrative: source year, 20–64 age band, education/sex cells, regional crosswalk, missing-cell handling, units, scale factor and model entry. The printed employment index uses ten times the rate in fractional units.

A substantive point remains: p. 12 says regional rates are aggregated with population weights rather than labour-force weights. If small-area rates are u_r=U_r/LF_r, their union's unemployment rate is

\[
u_{union}=\frac{\sum_r LF_r u_r}{\sum_r LF_r}.
\]

Population weighting generally defines a different exposure index. That can be a deliberate regressor, but it must be labelled and motivated accordingly. Inspect the actual builder before changing it. If the intended object was an aggregate unemployment rate, correct it and propagate the change; if it is a population-weighted exposure index, state that instead. A relabelling decision must not silently change estimation.

An external unemployment series is not automatically an exogenous opportunity instrument. Its exclusion from preferences and remaining limitations still require discussion.

### R12. Occupation grouping is misstated again

PDF p. 9 describes groups as “elementary; services/sales; clerical/craft/operators; and managers/professionals/technicians.” That is not the exact mapping recorded in the source audit.

| Research group | ISCO-08 majors | Correct descriptive content |
|---|---|---|
| 1 | 6, 7, 8, 9 | Skilled agricultural work, craft/trades, operators/assemblers and elementary occupations |
| 2 | 5 | Services and sales |
| 3 | 4 | Clerical support |
| 4 | 1, 2, 3 | Managers, professionals, technicians and associate professionals |

These are project aggregates, not four official ILO task categories. Tie labels to the executed mapping and explain missing/armed-forces treatment under the selected sample rule. Do not move crafts/operators into the clerical group in prose.

**Sources:** source-to-sample audit Section 6; ILO ISCO-08 major-group definitions.

### R13. The report lacks the visual evidence required to understand the model

The four v3 figures are motivation, two evaluator reference curves, resource incidence/consumption quantiles, and a matched-pair illustration. There are no dedicated marginal-utility plots or normalization comparison panels. Resource incidence is not a distribution of resource amounts.

Restore a curated set of figure families: sample and distributions; preferences/MU/MRS; opportunities and choice fit; welfare construction; inequality and attribution; reference/draw/scale sensitivity. Include singles and both-flexible couples, using spouse-level displays for labour variables and household-level displays for resources/welfare.

The report may contain extensive explanatory panels; the paper should select a small set supporting its main argument, with other diagnostics in appendices. Do not populate every page with historical plots while corrected quantities remain unavailable.

### R14. Estimation-to-welfare scaling is a real scientific dependency

PDF pp. 21 and 29 report singles consumption scaling of 1911.11 in estimation versus 1774.52 in the welfare panel. The report explicitly states that unchanged-parameter behavioural equivalence has not been established.

For non-log consumption, changing the scale generally changes relative cardinal utility and choice probabilities unless parameters/stochastic scale are transformed appropriately. Using the panel scale to recover physical euros does not establish that the utility function is the estimated one.

This must be reconciled before the corrected welfare interpretation is promoted. It should not be buried in a reproducibility table, but neither should its full history dominate the final paper once fixed.

### R15. Report unfinished corrections once, not in every paragraph

The v3 draft is admirably explicit that corrected tables are pending. It also reads repeatedly like a response-to-referees document: “the earlier mistake,” “no completed local result,” “not supplied,” “the historical convention.” Consolidate implementation history in the internal report and one scientific appendix.

The paper's main exposition should state the maintained model and its limits positively. Keep one version-status note and local status labels where historical numbers are actually displayed. Do not fill pending corrected cells with historical estimates merely to make the paper appear finished.

### R16. Remove all internal paths from the paper, including appendices

PDF pp. 27–29 contain extensive local paths, code filenames, hash strings and environment inspection details. This directly conflicts with the requested scholarly presentation.

Keep a conventional reproducibility description—data source/vintage, policy system, sample definitions, estimator, software citation and eventual public replication availability. Move internal code-to-equation maps and machine provenance outside the circulated manuscript into the internal report/repository. A public repository citation is not the same as printing a private filesystem path.

### R17. Statistical and behavioural language still needs care

One household contributes one choice likelihood. Alternative rows are numerical components of that contribution, not independent survey observations. Explain the household score and sandwich adjustment on that basis, rather than implying that a set of observed jobs was sampled repeatedly within household.

Report unweighted estimation separately from survey-weighted summaries. Explain the conditional nature of inference when group rates, proposal fits, policy inputs and active constraints are held fixed. A large finite standard error does not by itself prove non-identification. A positive-definite Hessian does not establish the normative validity of the welfare measure.

### R18. Comparable units do not establish comparable welfare meanings

The report is correct to distinguish raw and equivalized household values. Continue to report singles and couples in parallel. Do not infer that their reference levels become normatively identical simply because both are divided by an OECD scale.

Pooled levels and pooled decomposition require a defensible common cross-type interpretation. Group-specific offsets chosen only to achieve zero grand-coalition inequality are not justified. The current within-type reference constructions (weighted index means versus couple medoid arguments) should be explained and assessed before comparison.

### R19. Inequality robustness should be implemented, not dismissed as optional future prose

Once a defensible positive W is computed, calculate Gini, Atkinson with aversion 1 and 2, GE(0), GE(1), and CV squared (equivalent to twice GE(2)). Use the same household weights and state-specific equivalence convention.

For any index used in attribution, recompute that index on every coalition's W distribution. Gini decomposition shares do not transfer to Atkinson or generalized entropy. Signed subsidy measures need appropriate absolute/signed summaries; do not add arbitrary constants to make relative indices computable.

### R20. The notebook remains a core output, not a backend demonstration

The v3 appendix acknowledges that the inspected route is mainly replay/refitting on priced inputs. The eventual canonical notebook must expose source construction, new alternatives, pricing, estimation, population prediction, welfare, inequality and figures. It should call the production modules and show actual compatibility of installed server/laptop backends.

Do not repeat a historical CPU-only artifact as a refutation of Goal 2's separate CUDA parity return. Conversely, generic or historical parity does not certify the changed estimator. Resolve the exact tested version and scope in the internal technical record, not in the economic argument.

## IV. The old plotting script: useful design reference, unsafe as a scientific calculator without repair

The script has valuable report layout and diagnostic ideas. It also contains material mathematical and reporting defects. These findings are static code findings; they do not establish that these outputs appeared in v3.

### S1. The elasticity routine does not compute structural labour-supply elasticities

`compute_structural_elasticities`, approximately lines 733–816, assigns:

```python
hicksian = 1 - theta_l
marshallian = hicksian - 0.1
participation = hicksian * 0.3
intensive = hicksian * 0.7
```

The couples branches use the same assignments. These are not derivatives of predicted labour supply under the household budget and opportunity model. The routine cannot be presented as estimated compensated/uncompensated/extensive/intensive elasticities. It is called in the reporting flow, so the risk is operational, not merely a dead comment.

Quarantine these labels/results. If genuine elasticities are later requested, specify the perturbation, hold-fixed objects, budget recalculation and compensation convention, then simulate the population response. Do not retain the numeric shortcuts as approximations without a derivation—which is absent here.

### S2. Some “median-characteristic” curves use only the intercept

`plot_mu_distributions_by_group`, around lines 1251–1260, sets `beta_l_median = beta_l0` and then explicitly passes over the shifter loop. A centred age variable does not make all covariate contributions vanish at a median household; children and squared terms especially need explicit evaluation.

Use the full estimated shifter function at an actual documented profile, or plot the distribution across households. Another helper in the file does evaluate the shifters from a specification, so repair the caller rather than asserting that no correct helper exists anywhere.

### S3. Contour values are transposed without matching coordinates

`plot_utility_contours_all_groups` constructs C and L on a mesh, evaluates U there, and calls `contourf(L, C, U.T)` and `contour(L, C, U.T)` around lines 978–980. The square grid masks the shape error; values are no longer attached to their evaluation coordinates.

Use matched coordinates and values, and check a few plotted contour points against the actual utility function. This is precisely why attractive graphs are not self-validating.

### S4. Default parameters and domains can silently represent the wrong model

Several plotting paths replace unavailable curvature by 0.5. Some do not accept the specification needed to recover couples' fixed log consumption. Such fallbacks are unacceptable for paper figures: an unresolved parameter should fail or be explicitly marked, not create a different utility family.

The normalized leisure grid 0.1–2.5 in several functions also fails to cover the current empirical range implied by T=80, lambda_l=10 and h in [5,70], with non-work at normalized leisure 8. Choose supported physical grids, not inherited arbitrary ranges.

### S5. Density reconstruction has incompatible routes

The legacy `_compute_log_w` uses a normal log-wage kernel without the wage Jacobian; the later spec-driven opportunity reconstruction includes `-log(w)`. Neither route should silently stand in for the successor's truncated wage density and exact conditional specification. The correct reference measure matters.

Plot population predictions from the active production density and integrate them appropriately. Sampled-set conditional probabilities and historical anchored softmax outputs are not automatically population predicted shares.

### S6. Derivative units and interpretation

For the current separable utility written in physical quantities,

\[
u_C=\frac{\beta_c}{\lambda_c}(C/\lambda_c)^{\theta_c-1},
\qquad
u_L=\frac{\omega_i}{\lambda_\ell}(L/\lambda_\ell)^{\theta_\ell-1}.
\]

The helper's derivatives with respect to normalized c and l are not wrong merely because they use normalized units. They must, however, be multiplied by the chain-rule factors for physical-unit plots. Plotting \(u_L/u_C\) gives monthly consumption compensation for an extra recurring weekly hour of leisure. Convert by 52/12 only if reporting compensation per physical hour rather than that recurring-weekly-hours convention.

For couples, hold the other spouse's leisure fixed and include the actual interaction if estimated. If beta_ll is zero, say so. Raw marginal utilities across separately estimated utility scales are not interpersonal welfare comparisons.

### S7. Normalization plots should separate invariance from a different model

Let lambda_l' = k lambda_l with theta_l unchanged. For the separable term, an exact transformation is

\[
\omega_i'=k^{\theta_\ell}\omega_i,
\]

applied to every component of the leisure-weight function. It preserves utility up to an alternative-independent constant. For theta_l=0, the weight is unchanged and the log term gains a constant. Bounds/pins must transform too when claiming equivalence.

Plot identical physical-unit indifference curves/MRS under the exact transformation, and separately plot results of a relaxed-bound refit if such a refit is performed. Do not describe changes created by untransformed parameters or bounds as evidence that a unit choice changes preferences. T, the time endowment, is not the same object as lambda_l, the measurement scale.

The estimation-to-welfare consumption-scale discrepancy is a separate issue and requires its own exact model transformation check.

## V. Proposed narrative and figures

### Opening normative paragraph (proposed, subject to the bridge decision)

> Comparing well-being across people with different labour-market prospects requires a decision about which circumstances should enter the comparison itself. We use an own-opportunity reference: the monetary benchmark is constructed from the jobs an individual can take, while their actual pay is neutralized in the equal-consumption reference. This separates the valuation of an attained situation from an assumption that everyone faces the same feasible jobs. We then ask how differences in labour-market opportunities, preferences, resources and household needs contribute to inequality under that stated criterion.

Do not follow this paragraph with a log-integral formula labelled theoretical Measure 1 unless the empirical bridge has been justified.

### Report organization

Restore the sidebar and explanatory boxes. Sequence: research question and ethical stance; theory reference illustration; data and regional link; complete RURO model; estimates and preference diagnostics; behavioural fit; step-by-step welfare calculation; inequality and grouped attribution; findings/sensitivity; limitations and scientific development history. Use math, a worked example and a plain economic interpretation together.

### Figure families

1. **Normative comparison:** actual theory-presentation panel adapted with W1 definition; separate empirical reference diagram where justified.
2. **Data and geography:** both-type funnel; labour/resource distributions; actual GSUR-by-region/group coverage and variation.
3. **Estimated preferences:** full-profile leisure weights/curvatures; physical-unit marginal utility and MRS; own indifference curves, couples conditional slices.
4. **Opportunities and fit:** occupation-conditioned wage offers; hours/access masses; observed versus population-model employment/hours/occupation/wages; matched illustration with explicit conditioning.
5. **Welfare and attribution:** distribution/Lorenz by household type; four counterfactual states; grouped contribution chart, with isolated equalization separately identified.
6. **Sensitivity:** integration resolution, valid parameter uncertainty, normative reference, alternative inequality index, support and true reparameterization checks.

The final paper selects the figures that answer its questions; the report can retain more diagnostic detail. Every empirical figure must use the selected model version, source population, correct units and explicit status. Avoid internal S8/R240/JMP labels on reader-facing axes.

## VI. Consolidated instruction to Goal 1 Manager

**Tool/chat:** existing Goal 1 Manager Thinking chat. Local Codex carries out source extraction, code changes, figure regeneration and document builds in the authorised repository. No new broad Deep Research project.

**Provide to Goal 1:** this review; the uploaded v3 PDF and HTML; v2 HTML for design; `RURO_post_estimation_styled.py`; `jobs_and_wellbeing.md`; `Literature_collection.md`; and the current source-to-sample audit. These review files are available locally in this conversation.

**Goal 1 must locate and provide to Codex:** the latest 2026 theory manuscript and presentation (not verified in this review), actual current LaTeX/bibliography, the selected/current corrected singles and couples specifications and results, welfare functions and operators, sample/GSUR/occupation builders, figure generators and the canonical notebook. Do not invent missing paths or treat a library filename as proof of a local file. Confidential data remain in their permitted environment.

Copy-paste instruction:

```text
PI/DEPUTY — NORMATIVE ALIGNMENT AND V4 SCHOLARLY REVISION

Use the attached JMP_v3_normative_and_scholarly_review_v1.md as ONE consolidated
instruction. Continue the already-authorised corrective positive estimation,
data/budget reconstruction and writing. Do not create another mission family.

A. NORMATIVE DIRECTION

The PI's discussion with François establishes that the ethical stance must be
stated before selecting the welfare formula.

Adopt theoretical Measure 1, the own-set equal-consumption equivalent, as the
PRIMARY NORMATIVE TARGET:

u_i(z_i) = max_{j in A_i} u_i(W1_i, j).

Keep Measure 3, the own-set laissez-faire subsidy, as a later contrasting object.
Do not call Measure 1 Full Responsibility. Verify its precise axioms against the
latest theory manuscript. Cite Haydar–Maniquet (2026), work in progress.

Do not justify the selection by saying Independence of A makes opportunity
attribution impossible: it restricts the direct reference-set channel at fixed
attainment, not every effect of A through attained outcomes.

B. ONE BRIDGE QUESTION BEFORE WELFARE PROMOTION

The current evaluator uses an ex-ante log integral and a log-integral reference,
not the maximum and realised-bundle utility in theoretical W1.

Do not relabel the current calculation W1 or attach the theory's axioms to it
without establishing the relationship.

In the existing decision note and the draft's normative section, resolve:
- the evaluated attainment: actual bundle or an explicitly justified ex-ante
  object;
- the empirical counterpart of A versus opportunity intensity g;
- the role of unobserved job attributes/preferences, if any;
- why the proposed reference operation implements or deliberately extends W1.

Check the immediate restricted-domain consequence: with positively valued
leisure, no intrinsic preference for work/occupation, and non-work always
available, theoretical W1's flat-consumption maximizer is non-work, so W1
coincides with the staying-home equivalent. The common positive support of g
also does not identify household-specific deterministic sets.

Report that consequence honestly. Do not invent an accessibility threshold,
treat quadrature draws as realised jobs, or add amenities solely to prevent it.
If a stochastic extension is needed, return ONE recommended explicit bridge and
its changed assumptions for the PI/co-author's decision. Do not open a six-measure
search. This holds welfare headline promotion, not positive estimation or writing.

C. REPORT AND PAPER

Deliver one revised explanatory HTML report and one LaTeX paper/PDF, plus the
existing executable notebook. No third walkthrough document.

Restore the v2 report's left sidebar, colors and explanatory boxes, while retaining
v3's corrected analytical mathematics and offline mathematical rendering.

The report must teach the work step by step to the PI and an economics/mathematics
reader. The paper must present an economic argument, not a record of review replies.

Keep the exact agreed title. Delete the currency sentence. Put the ethical stance
and the narrow labour-market-opportunity question in the introduction. Rewrite
the abstract around the question, normative criterion, empirical approach and
actual corrected findings when available.

Remove ALL private/internal filesystem paths, hashes, script names and environment
inspection records from the circulated paper, including its appendices. Keep
technical provenance in the internal report/repository only.

D. THEORY FIGURE AND LITERATURE

Locate the latest theory presentation in the repository and use the actual relevant
W1 figure with a verified caption and work-in-progress credit. The current schematic
is not a substitute for that request. Do not mislabel a fixed-leisure diagram or
logsum illustration as the literal implemented W1.

Use the existing literature corpus to locate originals. Inventory available PDFs
and extracts, and perform page-aware extraction only for the core papers needed.
Do not block writing on converting the entire library. Check equations/theorems
in originals and cite the original papers, not generated summaries.

Develop the normative foundations, structural opportunity assumptions, estimator,
and inequality methods with citations at the relevant claims. Avoid citation
padding and repeated defensive claims about what the paper does not invent.

E. DATA AND REGIONAL ARGUMENT

Explicitly identify EU-SILC, Eurostat harmonization/access, EUROMOD input
construction and the policy calculator, with official citations and the actual
source vintage. Keep collection, income-reference and policy years distinct.

GSUR IS already in v3; move it into the data/identification narrative. Explain its
region/education/sex cells, year, age band, units, external source and role in
employment access. Inspect population-weighted versus labour-force-weighted
aggregation: label an exposure index accurately or correct an intended aggregate
rate, without silently changing the specification.

Motivate France using actual regional heterogeneity and data linkage. Discrete
administrative regions do not by themselves identify causal region effects or
prove isolated labour markets.

Correct the occupation prose to the executed ISCO mapping: 6–9 / 5 / 4 / 1–3.
Do not put crafts/operators in the clerical group in the report.

F. FIGURES AND OLD SCRIPT

Use RURO_post_estimation_styled.py as a design reference, not as a trusted calculator.

Do not reuse its alleged elasticities (1-theta_l, minus 0.1, 30/70 allocations).
They are not structural labour-supply response calculations. Inspect any old
outputs that would otherwise be reused; this finding does not imply v3 printed
those numbers.

Repair the intercept-only “median” curves, silent parameter defaults and the
unmatched U.T contour transpose. Plot using the ACTUAL production utility and
population prediction functions, including the correct wage Jacobian and
truncation.

Produce meaningful sample distributions, full-profile preference curves, MUC/MUL,
MRS and indifference-curve slices for singles and couples. Use physical units,
chain-rule derivatives and real supported domains. Raw utility scales are not
interpersonal welfare comparisons.

Show exact normalization invariance separately from a changed-bound refit.
Resolve the estimation-to-welfare consumption-scale discrepancy before promoting
new welfare outputs. Explain every figure's population, units, held-fixed objects
and empirical/illustrative status without internal model labels.

G. INEQUALITY AND DELIVERY

Once the primary positive money metric is defined and computed, include Gini,
Atkinson(1), Atkinson(2), GE(0), GE(1) and CV-squared robustness. Recompute the
coalition functional for each index. Do not apply positive relative indices to a
signed LF subsidy using an arbitrary additive shift.

Keep singles and both-flexible couples as core applications. Preserve the current
couples restrictions honestly until a changed specification is actually estimated.

Return the narrow welfare-bridge decision first. In parallel continue the V4
report, LaTeX/PDF, bibliography/figure dependencies and canonical notebook. Use
corrected data and parameters when they exist; do not manufacture final numerical
results or imply that the old shares survive automatically.

Record the direction once in the existing decision note. No new charter, no
separate review chain for every plot, and no mass literature-conversion project.
```

**Save / next:** retain this as the single working review memo. Goal 1 updates the current report and manuscript to their next version (v4 unless already advanced), with LaTeX source, compiled PDF and dependencies, and updates the same notebook. The next scientific decision is the interpretation/implementation bridge for W1; routine layout and verified plotting repairs need not await another PI approval.

## VII. External sources checked for this review

These references support the indicated methodological or institutional statements; they do not establish that the JMP implements their exact formulas.

- Capéau, B., A. Decoster and G. Dekkers (2016), “Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium,” *International Journal of Microsimulation* 9(2), 144–191. DOI: 10.34196/ijm.00139. Original article and figure page inspected for the relevance of opportunity/preference exposition and diagnostics.
- Decoster, A. and P. Haan (2015), “Empirical Welfare Analysis with Preference Heterogeneity,” *International Tax and Public Finance* 22(2), 224–251. DOI: 10.1007/s10797-014-9304-5. Institutional publication record supports the preference-respecting/ethical-ordering comparison.
- Fleurbaey, M. and F. Maniquet (2017), “Fairness and Well-Being Measurement,” *Mathematical Social Sciences* 87, 40–51. DOI: 10.1016/j.mathsocsci.2016.11.003. Normative preference-respecting measurement reference, not a source of the JMP's exact log-integral functional.
- Dagsvik, J. K. and A. Karlström (2005), “Compensating Variation and Hicksian Choice Probabilities in Random Utility Models that are Nonlinear in Income,” *Review of Economic Studies* 72(1), 57–76. DOI: 10.1111/0034-6527.00324. Relevant to random-utility welfare, not proof of the current own-set measure.
- European Commission/JRC, EUROMOD official overview, “What is EUROMOD?” and download/data-access documentation. Policy calculator and input data distinguished.
- ILO, official ISCO-08 structure and major-group definitions.
- Eurostat EU-LFS methodology; CEDEFOP's Eurostat-sourced unemployment-rate definition, and ECB glossary: unemployment is measured relative to the labour force. The aggregation formula in this memo is an arithmetic consequence of that definition.

The manuscript should additionally consult the original papers for all detailed literature claims rather than cite this review as their authority.
