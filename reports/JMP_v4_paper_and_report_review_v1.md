# Review of the v4 working paper and research-story report

**Project:** *Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition*  
**Date:** 9 September 2026  
**Disposition:** Major scholarly revision and reconciliation of the reported model before circulation.  
**Retention:** One working review memo. This is not a new mission-document family or an instruction to repeat all estimation.

## Scope and evidential limits

This review covers the complete 42-page `JMP_working_paper_for_seminar_v4.pdf` [P4] and the complete reader-facing content of `JMP_research_story_report_v4.html` [R4]. The HTML contains 21 numbered substantive sections, 12 figures, 13 tables and 34 presentation questions. I inspected rendered PDF pages and figures, extracted the HTML content separately from its scripts and embedded images, and tested its rendered mathematics, figures and navigation. The review also uses the supplied novelty audit [N] as a positioning aid and checks selected original sources listed at the end.

This is a review of the documents, their internal evidence and the mathematics they state. It does **not** independently reproduce confidential-data estimates, inspect the latest executable estimator or certify the numerical welfare pipeline. “Reported result” below means reported in these attachments. A conditional mathematical deduction is explicitly distinguished from a finding about the executed code.

Page references are the printed PDF pages. HTML references use its numbered section headings or Q&A numbers. The original attachments remain unchanged.

## Executive assessment

The paper now has a potentially clear empirical message: its reported Gini decomposition assigns a large role to job access among singles and a different balance of access, earnings opportunities and household circumstances among couples. The theory figure is present, the model and sampling equations are substantially more explicit, and the report has regained its sidebar. These are real improvements.

The principal weakness is no longer lack of material. It is the coexistence of incompatible generations of that material. The abstract and results describe log consumption with an estimated coefficient; the model and boxed welfare expressions still describe a consumption coefficient fixed at one. Completed estimation is reported alongside empty coefficient and fit tables. Corrected results coexist with historical data distributions and statements that the corrective work has not happened. Several findings are interpreted incorrectly or more broadly than their own tables permit.

The next revision must therefore be a **source-reconciled rewrite**, not another layer of qualifications pasted onto old prose. Continue legitimate numerical work. Do not initiate a broad specification search merely to fix writing. If a document contradiction reflects a real executable inconsistency rather than stale text, return that precise scientific issue.

The immediate priorities are:

1. Present one current utility, opportunity system, estimator, welfare formula and result population consistently.
2. Lead with the economic question, the chosen normative reference and the decomposition findings; move implementation history out of the main paper.
3. Populate the actual coefficient, fit and distribution tables from the already completed results or state exactly what is genuinely unavailable.
4. Integrate the closest literature identified by the novelty audit and use a qualified, accurate methodological contribution claim.
5. Make the HTML an explanatory research report and the LaTeX a scholarly paper, sharing evidence and equations rather than paragraphs wholesale.

# I. Response to the author's comments

## 1. Abstract: the author is right about the priority, but not every proposed substitution is safe

**Evidence:** P4, p. 1; R4 opening abstract.

The existing abstract is approximately a page-long combination of motivation, optimization diagnostics, normative caveats and a late results paragraph. The economically important decomposition appears as the fourth finding. That order should be reversed.

A conventional abstract need not use one prescribed opening formula. “In this paper…” and a problem-first opening are both legitimate. The decisive issue is whether the reader can quickly identify the question, contribution, normative basis, method and substantive answer.

The author's linked example is Capéau, De Sadeleer, Maes and Decoster (2021), CESifo 9071 [E1]. Its abstract identifies a limitation, states the methodological contribution and explains what it permits. It is not a history of implementation corrections. That organizational lesson is appropriate; its nonparametric assumptions or welfare formula should not be imported into this different application.

### Keep in the abstract

The labour-market-opportunity question; a concise description of the own-opportunity reference; modelling labour supply as choice among latent jobs; the role of EUROMOD; structural counterfactual attribution; the main singles/couples results; and one economically important sensitivity.

### Remove from the abstract

The consumption-coefficient estimates to five decimals; likelihood improvements; the mean-absolute-error numbers; numerical closure residuals; the history of identifying utility scale; the numbered first/second/third/fourth inventory; the detailed debate over transferring axioms; and the literal Markdown placeholder for missing parameter intervals.

The missing intervals must remain transparent in the appropriate result notes. Removing a progress report from the abstract is not permission to imply statistical precision that has not been established.

### Normative language

The abstract already mentions a “responsibility-side money metric.” Thus the stance is not entirely absent, but the phrase does not explain the normative comparison. Replace it with the actual reference: the household retains its own preferences and opportunity distribution while reference consumption is equalized across alternatives.

Do not substitute the deterministic statement “consumption at the preferred job that is indifferent to the current bundle” as the literal definition of the numerical measure. That is the theoretical starting point. The document's empirical object compares ex-ante evaluations through integration. The difference should be explained accurately rather than erased to improve fluency.

### Proposed replacement abstract

**Drafting proposal based on the point estimates reported in P4, pp. 34–35; not an independent validation of those estimates.**

> We study how unequal job opportunities contribute to inequality in money-metric well-being. Our normative reference retains each household's own preferences and job opportunities, while assigning the same disposable-consumption level to every reference alternative. We construct a stochastic equivalent-consumption measure that matches the household's attained ex-ante evaluation under this reference. We model labour supply as choice among latent jobs and estimate preferences, job access and earning opportunities using French EU-SILC data, with EUROMOD calculating taxes, benefits and disposable income for alternative work arrangements. We recompute well-being under counterfactual equalizations of preferences, access, earnings opportunities, and household resources and needs, and allocate their interactions using a grouped Shapley decomposition. In the baseline Gini decomposition, labour-market opportunities account for 55.9% of well-being inequality among single-adult households, including 49.2% attributed to job access, compared with 9.9% for preferences and 34.2% for resources and needs. Among couples, earning opportunities and resources and needs account for 35.7% and 51.2%, respectively, while access accounts for 8.2% and preferences for 4.8%. The relative importance of access and earnings opportunities differs consistently between the two populations across the inequality indices considered, whereas the sign of the singles preference contribution is index-sensitive.

This wording should be updated from the final result table, not treated as a new numerical source. The introduction can explicitly attribute the theoretical own-set principle to Haydar and Maniquet (2026), work in progress, and identify the stochastic adaptation separately.

## 2. Introduction: consolidate the argument, not just its headings

**Evidence:** P4, pp. 2–8; R4, sections 1 and 3.

Adopt the author's preference for an introduction without visible subsection numbering. This is an editorial choice for this paper, not a universal economics rule. Simply removing `1.1.1` while keeping all the same fragments would not solve the problem.

The introduction should move continuously through:

- the ambiguity of observed income and working time;
- why that ambiguity matters for welfare and attribution;
- the normative reference, attributed to its intellectual sources;
- the latent-job model and the empirical setting;
- the nearest methodological and substantive precedents;
- the contribution and principal findings;
- a concise paper roadmap.

The closest literature should be integrated into these paragraphs. Detailed identifying restrictions from other papers belong again at the relevant modelling assumptions, not as a long defensive tour in the introduction.

The following headings and prose should disappear from the paper: “The normative stance, stated before the formula”; “What this principle is, and what it is not”; “One borrowed principle, not a borrowed paper”; “the normative half is settled next”; and the repeated references to “the companion project.” Use “Haydar and Maniquet (2026)” or “the own-set equal-consumption criterion.”

Some of this defensive language reflects earlier review instructions. Such instructions are acceptance conditions for an editor, not paragraphs to paste into a manuscript.

### Suggested normative paragraph

> Comparing well-being when individuals face different job opportunities requires a reference that specifies how those opportunities enter the comparison. We draw on the own-set equal-consumption criterion of Haydar and Maniquet (2026). In its deterministic formulation, the criterion assigns to an attained situation the consumption level that would make the individual's preferred job within their own ability set equally good when every feasible job provides that same consumption. The reference therefore retains the individual's own opportunities and preferences while removing variation in pay from the reference bundles. We adapt this principle to the estimated distribution of latent jobs, evaluating attained and reference opportunities ex ante. The stochastic formulation and its properties are stated explicitly below.

Add verified normative references where the broader compensation/responsibility argument is introduced. Do not state that an unproved stochastic extension inherits a deterministic characterization.

### Keep the correct own-set comparative-static argument, but write it plainly

At fixed preferences and attained utility, enlarging the reference set can reduce the consumption amount needed to reach that utility. That is correct and economically important. It should be explained as an effect of changing the benchmark, not as a general claim that more actual opportunities reduce well-being.

Suggested wording:

> Holding the attained situation fixed, a person with a larger reference menu may need less uniform consumption to reach the same satisfaction. When actual opportunities change, however, both attainment and the reference menu may change. The net effect on equivalent consumption therefore depends on both changes.

### Roadmap paragraph

For the architecture recommended below:

> Section 2 describes the data and household budget construction. Section 3 presents the latent-jobs model, its identifying restrictions and estimation. Section 4 defines the money-metric welfare measure and the structural decomposition. Section 5 reports the behavioural and welfare results for singles and couples. Section 6 examines sensitivity and remaining limitations, and Section 7 concludes.

## 3. Framework: the requested material exists, but is fragmented and partly obsolete

**Evidence:** P4, section 3, pp. 8–10; sections 5–6, pp. 13–18; section 8, pp. 25–33.

It would be inaccurate to say that v4 contains no opportunity functions, likelihood or Shapley equations. It contains all three. The problem is that the reader encounters a short conceptual section, then data, then a fuller model, then a different generation of the welfare formula much later.

Merge the current conceptual section into the substantive model and welfare sections. Introduce the theoretical W1 principle in the introduction with Figure 1; develop the empirical model once; then derive the stochastic welfare measure from that same model. Give central equations and tables numbers so that they can be cited precisely.

Recommended main structure:

1. Introduction, with integrated literature and normative motivation.
2. Data.
3. A latent-jobs model of household labour supply: preferences, opportunities, identification and estimation.
4. Money-metric well-being and structural inequality decomposition.
5. Empirical results: behavioural fit, welfare distributions, attribution and the common-opportunity comparison.
6. Sensitivity and limitations.
7. Conclusion.

Model and welfare subsections are useful here; the author's request to remove visible introductory subsections does not imply that all technical structure should disappear.

## 4. Data: use the simple heading and describe the final sample

**Evidence:** P4, pp. 9–13.

Use “Data” as requested. Institutional detail and EUROMOD budget construction can remain subsections. Remove the historical funnel and historical distributions from the main empirical description once current samples are reported. A corrected-model paper needs descriptions of its corrected samples, not just a disclaimer below old descriptions.

# II. Material scientific and consistency findings

## 5. The principal equations do not describe the model whose estimates are reported

**Priority: central now. Evidence:** P4, pp. 13–14, 19–20, 25–27; R4, sections 7, 12 and 14.

The utility equations on p. 13 put coefficient one on consumption. The comparison table says singles have estimated Box–Cox consumption curvature. Page 14 explicitly says the consumption coefficient and shock scale are both fixed. Pages 19–20 and 27 instead report zero consumption curvature and estimated consumption coefficients 2.03873 and 2.10172.

These are different specifications. The old expressions must be replaced, not followed by a newer explanatory paragraph.

Subject to confirmation against the executed current model, the reported specification has the common form

\[
u_i(j)=L_i(j)+\beta_{c,t}\log(C_i(j)/\lambda_{c,t}),\qquad t\in\{\text{singles},\text{couples}\}.
\]

Here \(L_i\) contains the appropriate single-adult or spouse-specific leisure terms and the restrictions actually estimated. Report the two consumption coefficients once in the current coefficient table and use them consistently throughout.

Fixing the shock scale is a normalization; fixing the consumption coefficient as well imposes a restriction relative to that scale. Estimating \(\beta_c\) removes that extra restriction. The absolute cardinal utility scale is still not identified independently of its normalization. Fixing consumption curvature to zero is a functional-form decision, not what by itself identifies the random-utility scale.

## 6. The boxed welfare formula is obsolete

**Priority: central now. Evidence:** P4, pp. 25–28; R4, section 14.

The following is an algebraic consequence of the reported current log-consumption model, not an independently verified code result. For each household and coalition, write

\[
J_{i,S}=\int e^{L_{i,S}(j)}
\left(\frac{C_{i,S}(j)}{\lambda_c}\right)^{\beta_{c,S}}
\widehat g_{i,S}(j)\,d\nu(j),
\qquad
H_{i,S}=\int e^{L_{i,S}(j)}\widehat g_{i,S}(j)\,d\nu(j).
\]

The reference map is

\[
\Phi_{i,S}(m)=\beta_{c,S}\log(m/\lambda_c)+\log H_{i,S},
\]

and the equivalent amount is

\[
\boxed{
W_{i,S}=\lambda_c\exp\!\left[
\frac{\log J_{i,S}-\log H_{i,S}}{\beta_{c,S}}\right].
}
\]

Define the reference probability measure

\[
r_{i,S}(dj)=\frac{e^{L_{i,S}(j)}\widehat g_{i,S}(j)d\nu(j)}{H_{i,S}}.
\]

Then

\[
\boxed{
W_{i,S}=\left[\int C_{i,S}(j)^{\beta_{c,S}}r_{i,S}(dj)\right]^{1/\beta_{c,S}}.
}
\]

This is a weighted power mean. It is an arithmetic mean only at \(\beta_c=1\). The document's arithmetic-mean derivation, derivative omitting \(\beta_c\), and corresponding Q&A answer must be replaced. For the current log reference, \(\Phi'(m)=\beta_c/m\).

The consumption-unit constant cancels in the power-mean representation. If a stored normalized array is correctly converted back to physical consumption, a change in \(\lambda_c\) alone under log utility adds an alternative-invariant constant and does not create the old Box–Cox scaling problem. Verify actual units and array conversion; do not carry an obsolete unresolved issue forward without checking its applicability.

A general Box–Cox reference can also be inverted explicitly with the appropriate coefficient. Thus “away from log consumption there is no such closed form” should mean “no such power-mean simplification,” not that no closed-form inverse exists.

## 7. The power-mean figure confuses weights, contributions and marginal sensitivity

**Evidence:** P4, p. 27, p. 39 and Figure 12, p. 41; R4 preference/welfare exposition.

There are three different quantities:

1. The reference probability weight \(r_j\).
2. The power-moment contribution \(r_j C_j^\beta\).
3. The marginal effect of consumption on the resulting welfare amount,
   \[
   \frac{\partial W}{\partial C_j}
   =r_jC_j^{\beta-1}W^{1-\beta}.
   \]

Holding \(r\) fixed, the reference probability weights do not rise with consumption. Contributions to the power moment do. Marginal sensitivity has exponent \(\beta-1\), not \(\beta\).

The graph plots a term proportional to \(C^{\beta}\), but the prose says the curve would be flat at \(\beta=1\). That curve is linear at one; a standardized marginal-sensitivity curve proportional to \(C^{\beta-1}\) is flat at one.

Likewise, the reported 4.11 factor for twice the consumption is a ratio of power-moment contributions at equal reference weights, not a statement that the job is 4.11 times as available. For normalized discrete choice probabilities, the own-consumption elasticity is \(\beta(1-p_j)\), not simply \(\beta\). The latter is the elasticity of an unnormalized contribution, holding the other inputs fixed.

Choose one plotted object and label it precisely. My preferred explanatory version is either:

- “Relative contribution to the consumption power moment,” plotting \((C/C_0)^\beta\), with a linear \(\beta=1\) comparison; or
- “Relative marginal sensitivity of equivalent consumption,” plotting \((C/C_0)^{\beta-1}\), with a flat comparison.

The title should say **consumption coefficient / power-mean order**, not consumption curvature. The reported curvature is zero; the coefficient multiplying log consumption is a different parameter. Neither parameter is the across-household inequality-aversion parameter in an Atkinson index.

## 8. Pay neutrality: the stated numerical identity does not support the abstract's conclusion

**Evidence:** P4, abstract and pp. 27–28; R4 opening and section 14.

The paper reports that changing the normalized conditional wage density leaves \(H_i\) unchanged to numerical precision, and that the welfare response therefore travels through attained value. It then concludes that the empirical measure fails Independence of pay. That conclusion does not follow from this experiment alone.

A reference can be directly pay-neutral while welfare changes because a different earning environment changes attainment. The deterministic axiom is a fixed-attainment comparison, not a claim that changing wages can never change the evaluated outcome.

Use this narrower statement:

> Under the stated factorization, the flat-consumption reference is invariant to the conditional wage density because that density integrates to one and non-consumption utility has no wage argument. Changes in earning opportunities can nevertheless change equivalent consumption through the attained evaluation.

Do not infer either a full axiomatic characterization or its failure from a counterfactual that changes attainment. To make an axiomatic claim, define the primitives held fixed and prove the property for the stochastic measure. The theory-to-empirics qualification can be concise; it does not need a paragraph of denials in the abstract.

The paper also labels the maxima of EUR 438 / 34% and nearby bridge quantities as coming from a non-final frame. Do not mix those historical magnitudes with current numerical identities in one result paragraph. Recompute the example on the current inputs or move it to clearly separated history.

## 9. The W1–W4 sign claims contradict the stated maintained conditions

**Evidence:** P4, pp. 26–27; R4, section 14. **Conditional mathematical finding.**

The text states that non-work maximizes the reference non-consumption utility. If

\[
L_i(o)\ge L_i(j)\quad\text{for all reference states},
\qquad \int\widehat g_i\,d\nu=1,
\]

then

\[
H_i=\int e^{L_i(j)}\widehat g_i(j)d\nu(j)\le e^{L_i(o)}.
\]

Therefore, for the document's definition,

\[
\Delta_i=L_i(o)-\log H_i\ge0,
\qquad
\log\frac{W_i^{1,EA}}{W_i^{4,EA}}=\frac{\Delta_i}{\beta_c}\ge0.
\]

The manuscript nevertheless says its stated \(\Delta_i\) is negative throughout the couples panel and has mixed signs for singles. At least one of the sign convention, reference normalization, stated home-maximization condition or source binding differs from the printed account.

Require one targeted comparison of the actual current definitions and source arrays. Do not repair this by flipping a sign in the sentence without checking what was computed. If the conditions fail for some current households, qualify the home-maximization assertion rather than force the result.

The temperature limit also needs consistent indexing: attained and reference values must use the same \(\tau\). The meaningful statement is convergence of the two consistently defined measures as \(\tau\) goes to zero, not convergence to the staying-home value evaluated at a different fixed temperature. This is a mathematical property of the specified family, not a fresh empirical robustness exercise.

## 10. The stochastic foundations are described inconsistently

**Evidence:** P4, pp. 14, 25–26.

The model section expressly maintains a mixed-measure choice density and declines an expected-maximum interpretation without an additional stochastic construction. The welfare section then describes idiosyncratic shocks as added and the integration as smoothing over them.

Choose an explicit and source-supported account. A finite-menu extreme-value derivation does not automatically supply the continuous-job construction. Conversely, a deliberately defined structural density and ex-ante welfare functional can be stated as maintained objects without pretending to prove a latent-process theorem. The report should explain the assumptions and any unresolved implication in positive language.

Likewise, the empirical model has common support and heterogeneous intensities. The initial “many jobs versus only one job” story is a useful motivation, but it is not a literal recovered pair of menus in this application. Use it as motivation and then state what the model represents.

## 11. Inference and optimization language overstates what the diagnostics establish

**Evidence:** P4, pp. 19–20.

The paper reports agreement across multiple starts and positive local curvature. These support a stable local solution found from the tested starts, not a theorem of global uniqueness. Replace “single optimum” in reader-facing prose with the actual multistart evidence.

Raw Hessian condition numbers are coordinate-dependent. Standardized condition numbers are also conditional on the chosen standardization. Scaling by robust standard errors does not turn a matrix into a complete measure of identification.

Most concretely, the same page says couples have no active bounds and then attributes a conditioning issue to a **bound-active experience coefficient**. This is an internal source/version conflict. Bind the scaled diagnostic to the current 47-dimensional estimate or remove the obsolete explanation.

Fixing the log-consumption functional form is not, by itself, what identifies utility scale. The appropriate claim is that the consumption coefficient is estimated relative to the normalized stochastic scale, under the maintained model.

The primary text needs economic estimates and behavioural evidence. Eigenvalues, polishing-path counts and machine precision belong mainly in the technical appendix or report.

## 12. A genuine unresolved observation/retention issue must not be removed as “negative prose”

**Evidence:** P4, p. 17; Appendix, pp. 38–39.

The manuscript explicitly says that conditioning on the chosen-wage/hours retention event remains unresolved. That is potentially an econometric issue, not a stylistic caveat. Source-check whether it is now resolved in the executed criterion or remains a real question.

The sample screen and structural offer support are different objects. A conditional likelihood appropriate to unselected observations is not automatically appropriate to an outcome-selected sample. This review does not determine which correction is needed without the current observation rule and code. It requires one precise resolution before the manuscript says every relevant estimator issue is settled.

Similarly, small observed cross-coordinate correlations and a binomial-looking count distribution are diagnostics, not proofs that the generator implements independent draws. The generator's construction and conditional-sampling derivation should establish the law. For the labelled-sample derivation, explain how the collection is represented without conditioning on a label that already reveals which slot was forced to be the observed choice; account for multiplicities consistently.

None of this is an instruction to replace the current estimator on the basis of prose inspection alone.

# III. Empirical results: what is supported by the displayed tables

## 13. The top-level arithmetic checks out at displayed precision

**Evidence:** P4, pp. 33–34; R4, sections 18–19. **Reviewer calculation from rounded published cells.**

For singles:

\[
(I_{00},I_{10},I_{01},I_{11})=(0.193596,0.218795,0.063459,0).
\]

For couples:

\[
(I_{00},I_{10},I_{01},I_{11})=(0.132465,0.129046,0.009427,0).
\]

Applying the printed two-player formulas reproduces the displayed contributions:

| Quantity | Singles | Couples |
|---|---:|---:|
| Preference Shapley contribution | 0.019130 | 0.006423 |
| Non-preference contribution | 0.174466 | 0.126042 |
| Preference share | 9.8814% | 4.8488% |
| Preference-only inequality reduction | **−13.0163%** | **+2.5811%** |
| Environment-only inequality reduction | **67.2209%** | **92.8834%** |

A negative reduction means an increase. The singles Gini rises when preferences alone are equalized even though their Shapley contribution is positive. This is an excellent explanatory example for the report. The previous 77% one-factor result is not the current table's result.

This calculation checks algebra on the printed four cells. It does not independently verify household welfare, all coalition calculations or machine-precision residuals. Small discrepancies between sums of separately rounded lower-level cells should not be mistaken for numerical failures.

## 14. Correct the multi-index ranking statement

**Evidence:** P4, pp. 35–36; R4, section 19.

The prose says that access exceeds resources/needs for singles except under half the squared coefficient of variation. The table contains **two** exceptions: GE(1), where resources/needs receive 52.73% against access's 49.64%, and GE(2), where they receive 62.86% against 40.89%.

The supported statements are:

- Access exceeds earnings opportunities for singles under all six indices.
- Earnings opportunities exceed access for couples under all six.
- Access alone exceeds resources/needs for singles under four of six indices.
- Access plus earnings opportunities exceeds resources/needs for singles under five of six, with GE(2) the exception.
- Resources/needs are the largest of P/A/B/D for couples under all six.

Those are descriptive rankings of reported point estimates. Parameter intervals are still pending, so do not convert them into claims of statistically established ordering.

## 15. The preference sign is index-sensitive, and that belongs in the principal interpretation

**Evidence:** P4, pp. 35–36.

For singles, the reported preference share is positive for Gini and negative for all five alternatives. The phrase “preferences explain about ten per cent of inequality” must therefore specify the baseline Gini and reference. It is not a metric-invariant empirical conclusion.

A useful correction to an overly broad critique is needed here: in a general Shapley game, a negative allocation is not identical to a negative one-factor effect. But in this **two-group exhaustive game with nonnegative inequality indices**, the manuscript's implication can be derived. When \(I_{11}=0\),

\[
2C_P=I_{00}-I_{10}+I_{01}.
\]

If \(C_P<0\), then \(I_{00}-I_{10}<-I_{01}\le0\). Thus preference-only equalization must increase inequality under those conditions.

Do not call that particular implication false. State it as a consequence of the game's closure and nonnegative index, not the general definition of a negative Shapley contribution. The converse does not hold; the singles Gini is the immediate counterexample.

Suggested text:

> The preference allocation is positive for the Gini but negative for the other reported indices. In this exhaustive two-group game, those negative allocations imply that preference-only equalization increases the corresponding inequality statistic. Their magnitudes nevertheless average effects across coalition orders rather than equal the isolated preference effect.

## 16. Levels, references and uncertainty need to accompany the shares

**Evidence:** P4, pp. 30–36.

The paper provides Gini levels and a multi-index table of shares, but not the six baseline index levels or a visible corrected equivalized-results panel. The prose says such a panel exists. It does not in this supplied PDF/report.

Report each index's level, contribution units, shares and basis. Define Atkinson(1), Atkinson(2), GE(0), GE(1) and GE(2) analytically in the methods/appendix. Label “Half CV squared” as \(GE(2)=CV^2/2\). Multiplying an index by a positive constant scales its level and Shapley contributions but not its shares; GE(2) and CV² are not distinct robustness games in that sense.

The relation \(A(1)=1-e^{-GE(0)}\) explains why these two indices rank complete positive distributions in the same order while their Shapley shares can differ: nonlinear transformation does not commute with averaging marginal contributions. This is a useful report explanation, not a reason to discard one requested index.

Do not manufacture confidence intervals. Bind the pending parameter propagation when completed, and report numerical uncertainty separately. Until then use “estimated attribution” and distinguish point-estimate ranking from statistical evidence about a difference. A concise table note is enough; a page-long status statement is not.

## 17. The singles–couples contrast is interesting, but its explanation remains conditional

**Evidence:** P4, pp. 31–35.

The documents correctly identify different within-type reference operators: weighted index moments and a reference-sex block for singles, medoid spouse arguments and retained spouse-specific coefficients for couples. These are legitimate disclosed design choices, but they mean the difference in attribution cannot be assigned entirely to household type without considering reference and specification differences.

The suggested second-earner buffering explanation is not established by the decomposition. Two earnings streams do not mechanically imply more dispersion than one; dependence and resource pooling matter. Retain at most a short hypothesis sentence or explain the mechanism using a separately defined counterfactual. Do not turn this into another required pre-seminar empirical mission.

Show the existing reference sensitivities in one common format. Do not describe raw household shares as a pooled interpersonal welfare comparison. Singles and couples are both core applications even when their degrees of precision or current normative comparability differ.

## 18. The decomposition contribution needs formal operators, not an originality slogan

**Evidence:** P4, pp. 31–33; novelty audit [N], pp. 3–5, 12–14.

The existing operator table is useful. Complete it with exact current reference definitions and resolve its pending-versus-completed resource-priority contradiction. State that an operator changes a structural pathway, not every occurrence of a raw characteristic. Education, for example, can enter wages and the group-unemployment lookup without both pathways being equalized at once.

Define the state map directly:

\[
I_S=\mathcal I\{W_i(T_S X)\}_{i=1}^N,
\qquad v(S)=I_{\varnothing}-I_S.
\]

Specify how \(T_S\) is assembled. A product of operators is not well defined independently of order unless the operators commute on the permitted objects, or a simultaneous substitution map is specified. A consistent treatment of budgets, composition and needs is part of the economic definition.

Explain why the grouping \(P\) versus \(\{A,B,D\}\) is preferred and how its lower-level subdivision is handled. The group allocation rule is inherited. The application-specific contribution is the economically defined welfare game and empirical answer, subject to the maintained model and reference choices. Do not claim that complete recomputation or writing down a cooperative game is new in general.

## 19. The benchmark evidence does not yet support the abstract's strongest behavioural claim

**Evidence:** P4, pp. 20, 36.

The draft reports the common-opportunity benchmark objective 6395.11 against the RURO 6253.46, a difference of about 141.64. It asserts in the abstract that the difference is concentrated precisely on the margins governed by opportunities. The displayed fit table is entirely pending, and no fit-by-margin benchmark table establishes that claim in the attachment.

Provide a compact comparison table with the current specifications, free parameter counts, common sample/conditioning basis, objective and population-fit moments. Use a likelihood-ratio test only if nesting and inferential conditions are established. A better maximized criterion alone does not prove the model is necessary or that an economic mechanism has been identified.

Keep opportunity heterogeneity, common opportunity shape, utility terms and numerical proposal distinct. State what is changed in each benchmark with equations, not just labels. The corrected benchmark welfare calculations are still explicitly absent, so do not insert the historical preference-attribution or welfare-Gini differences as current results.

# IV. Data, figures and the report

## 20. Rebuild the main data section on the current sample

**Evidence:** P4, pp. 9–13, 19 and 39; R4, sections 4–6.

The final counts are reported as 1,540 singles and 2,223 couples, but the main funnel ends at the historical 1,555 and 2,275. Replace it with the final funnel, including a clear starting roster count and the additional corrections. Do not reconstruct the missing intermediate counts from subtraction when exclusions overlap.

Distinguish unsupported military occupations from genuinely missing occupation codes. The civilian mapping excludes ISCO 0 for a particular modelling reason; that is not the same as occupation not being recorded.

Retain the improved exact four-group ISCO mapping (6–9, 5, 4, 1–3), but present it as a small table. Define education categories and potential experience just as clearly. Show current distributions of age, children, employment, hours, occupation, observed/imputed wage inputs, resources and simulated disposable consumption for singles and couples.

Use EU-SILC collection year, income reference year and EUROMOD policy year consistently. Cite official data and classification documentation in the bibliography, not only the generic EUROMOD paper. Keep the household budget aggregation statement and accounting convention, but remove stale claims that the all-member correction remains undone.

GSUR is now described, including its population-weighted exposure-index interpretation. Preserve that definition if it matches the builder. Regional group variation supports the access specification conditional on its exclusion and functional-form assumptions; it does not establish separate identification merely because the tax system is national. The paper's longer warning about what regions are not can become one identification qualification.

Non-labour resources should be described by economic classes and measurement units. Do not add stocks, imputed benefits and cash flows as though they formed one monthly cash-income sum. Explain which are budget inputs and which are endogenous tax-benefit outputs.

## 21. Every figure: retain, update or reposition

| Figure, PDF page | Assessment and action |
|---|---|
| 1, p. 3: theory own-set reference | Requested figure is present. Retain it. Shorten the caption; credit Haydar–Maniquet (2026), work in progress. Explain the stochastic adaptation in the text. |
| 2, p. 9: generic ambiguity schematic | Optional motivation. It partly duplicates Figure 1 and delays the model. Move to report/appendix if the main paper needs space. |
| 3, p. 10: monetary reference curves | Explicitly historical. Regenerate with the current log/estimated-coefficient evaluator before using it to teach the main measure. |
| 4, p. 13: resource incidence and consumption | Explicitly historical, including the old singles aggregation. Replace with current data distributions. |
| 5, p. 22: matched household illustration | Six-panel caption is much improved, but the example is historical. Reapply the same selection rule to current estimates or move to history. Name the four occupation groups and remove fractional category ticks. |
| 6, p. 23: singles indifference curves | Useful. Retain after current-parameter binding. Note the log consumption-axis scale. Do not call a curve ending at the plotting limit economically infeasible under unbounded log consumption. |
| 7, p. 23: marginal utilities | Useful diagnostics, best emphasized in the report. Physical units are valuable. Avoid comparing raw utility magnitudes across separately estimated groups. |
| 8, p. 24: MRS and exact one-hour compensation | Useful, but the middle panel's “empirical” label should say household-level model-implied estimates. Define whether the discrete compensation is for more work or more leisure and use the same sign convention in caption/text. |
| 9, p. 24: normalization | Retain as a report/appendix diagnostic. It is exact reparameterization, not a fresh empirical robustness estimate. Document transformations of all relevant coefficients and constraints. |
| 10, p. 40: couples indifference slices | Useful and should be shown alongside singles when introducing preference evidence, not exclusively as a remote extension. |
| 11, p. 40: one-nat conversion | Secondary interpretive diagnostic. Its reported conversion factors agree with the displayed consumption coefficients; do not make this the economic headline. |
| 12, p. 41: power-mean effect | Rewrite labels/exponents/caption as in Finding 7. The present figure and prose describe different notions of weight. |

### Proposed concise Figure 1 caption

> **Own-set equal-consumption equivalents.** Individuals with preferences \(R_i,R_h\) and ability sets \(A=\{j,k\}\), \(A'=\{k,\ell\}\) attain \(z_i,z_h\). For each individual, a common consumption level is assigned to every job in their own set. The level making the preferred reference job indifferent to the attained bundle defines the money metric. Adapted from Haydar and Maniquet (2026), work in progress.

The caption need not recapitulate every axiom or list things the picture does not estimate. The main text should state that it is the deterministic theoretical construction. Do not assert permission as an independently verified fact unless that permission is documented or supplied by the authors.

### A mathematical correction to the indifference-curve explanation

P4, p. 21 says that at sufficiently low leisure no consumption can attain some utility level because the reference leaves the transform's range. With the current utility \(L(\ell)+\beta\log(C/\lambda)\), any finite target utility and finite \(L\) at positive leisure yield

\[
C=\lambda\exp\{(\bar u-L(\ell))/\beta\}>0.
\]

The required amount may leave the plotted or model-budget range, but a positive mathematical solution still exists. Do not retain a Box–Cox range argument from a previous specification. At a singular zero-leisure endpoint or a separately imposed consumption bound the qualification differs; state the actual domain.

## 22. The central welfare result still has no central welfare figure

**Evidence:** complete figures inventory, P4 and R4.

The documents now contain numerous preference diagnostics but no principal graph of the corrected welfare distribution or its decomposition. The argument culminates in a table at p. 34, after a large amount of technical history.

Prioritize:

- corrected income versus money-metric welfare distributions or Lorenz curves within each type, with the exact income and welfare definitions;
- a signed grouped-attribution plot for singles and couples;
- a simple comparison of one-factor effects and Shapley allocations;
- a compact multi-index/reference sensitivity display.

These are graphical presentations of existing requested outputs, not new research programmes. Do not use pie charts for rows with negative contributions. Keep optional normalization/nat diagnostics mainly in the report, so the paper's figures match its title and main finding.

The corrected coefficient and population-fit panels are equally important. A table of optimizer diagnostics cannot substitute for them.

## 23. The HTML layout is improved; the document's pedagogical role is not yet fulfilled

**Evidence:** browser-rendered R4, all numbered sections and Q&A.

The sticky sidebar is restored. The bundled mathematical rendering works in the inspection environment: 234 mathematical containers, no reported rendering errors, and 12 loaded figures. Retain these improvements. No need to redesign the visual theme again.

The report nevertheless repeats most paper prose, including its page-like abstract and contradictions. It should instead walk the reader through the economic objects. Use short explanatory boxes after important equations and current worked examples with visible inputs, intermediate quantities and interpretation. Put scientific history in a clearly separated, preferably collapsible section.

The Q&A must be regenerated from the corrected explanation. Specific stale answers include:

- Q5: describes the first picture as generic motivation, although the first is now theoretical W1.
- Q24: says log utility gives an arithmetic consumption average without conditioning on \(\beta_c=1\).
- Q31: says corrected nested attribution is not established, while section 19 displays corrected singles suballocation.
- Q6: evades the actual dates instead of answering “2016 collection, 2015 income reference and the stated 2015 policy system.”

The bibliography is a long paragraph with only one external clickable citation link in the inspected HTML. Render separate bibliography entries and make in-text citations navigate to them. In narrow-screen testing, several tables overflowed the viewport; add horizontal scrolling wrappers rather than shrinking all text.

## 24. The paper should not read as a quality-control log

**Evidence:** throughout P4, particularly pp. 1–8, 19–20, 25–30, 35 and 37–39.

Necessary qualifications should remain, but the current prose repeatedly narrates how earlier errors were removed. It speaks to a reviewer of the workflow rather than an economist reading a study.

Examples of replacement patterns:

| Current style | Scholarly replacement |
|---|---|
| “The normative half is settled next…” | State the chosen normative reference and cite its source. |
| “One borrowed principle, not a borrowed paper.” | Explain the specific reference criterion used in this empirical application. |
| “A retraction, at its exact scope.” | State the current finding and its index/reference sensitivity. Put the supersession in research history. |
| “The licensed statement is therefore…” | Write the scientific statement, with its assumptions and evidence. |
| “Nothing in this section is now awaiting…” | Remove unless the item is genuinely unresolved; use a concise table note where needed. |
| “Not the same numerical zero; we quote each…” | “The numerical invariance residual is negligible in both samples,” with detailed values in a technical table if useful. |

Explicitly saying what the paper does not identify is sometimes essential. One clear statement about structural attribution versus causal effects is preferable to repeating it in every caption. Likewise, describing a stochastic adaptation once precisely is preferable to repeatedly disclaiming that it is “not the companion paper.”

The inspection found no private filesystem paths in the v4 PDF text. That previous problem is improved. Internal labels such as SCALE-1, generic “certified” language and machine-precision narration remain and should be translated or relocated.

# V. Literature and contribution: how to use the novelty audit

## 25. The literature is not absent; its selection and argument need revision

**Evidence:** P4, pp. 4–8 and references, pp. 41–42; novelty audit [N].

There are ten references and several pages of discussion. The problem is not a minimum citation count. It is the repeated structure “their paper does X; we do not claim X,” coupled with omission of the closest decomposition precedents identified in the new audit.

Mühlhan (2023) already combines structural labour supply, involuntary-unemployment restrictions and Shapley attribution of household-income inequality changes [E2]. Creedy and Hérault (2011), section 5, already construct money-metric distributions under policy/population states and average the two decomposition paths [E3]. These are direct boundaries on broad novelty claims. Their original papers, rather than only the audit's summaries, should support the comparisons.

Use the audit as a working map, not proof of universal priority or an unquestionable authority on every bibliographic detail. Its first-known conclusion is expressly qualified by its search scope and the actual implemented object.

A concise contribution formulation is:

> We develop an application-specific structural decomposition of money-metric well-being inequality. The decomposition counterfactuals separately equalize preferences, employment and occupational access, earning opportunities, and household resources and needs within an estimated latent-jobs model. Welfare and inequality are recomputed under each coalition, and the resulting interactions are allocated using the established grouped Shapley–Owen–Shorrocks rule.

Verify which parts of access are household-varying in the current specification. A common hours-density shape may be an important estimated model component without constituting a source of between-household access heterogeneity. Avoid a novelty sentence suggesting that every hours-opportunity parameter is an independently equalized household factor when the operators do something narrower.

The introduction should integrate the closest contrasts; the model and welfare sections should cite assumptions and principles where they are used. Add normative foundations, the actual sampling-likelihood reference and inequality-index references. Do not compensate for missing key citations by adding a long list of tangential papers.

The author's abstract example is also substantively relevant to welfare-level analysis under preference heterogeneity, but it studies a different nonparametric identification object [E1]. Use it as a careful comparison, not authority for the present stochastic reference.

## 26. The current novelty claim needs less defensiveness and more formal precision

The strongest defensible methodological emphasis is the **specific economic counterfactual game**, not discovery of a new allocation principle. Explain the exact welfare outcome, normative reference, factor substitutions, joint-dependence treatment and grouping. A mere product notation \(\prod T_k\) should not hide an operator-order conflict.

Audoly and coauthors provide contemporary guidance for grouped nonlinear decomposition [E4]. Shapley, Owen and Shorrocks are the foundations. Complete recomputation has precedents, so it should be described as required methodological discipline rather than claimed new on its own.

Use conservative “we develop/implement” language in the abstract. A narrowly qualified priority statement can appear in the related discussion only if it still matches the executed object after the welfare revision. “First structural labour-supply Shapley decomposition” and “first decomposition of money-metric inequality” remain inappropriate.

# VI. Additional completion issues

## 27. Report unresolved matters accurately without allowing them to dominate the paper

Current examples of contradictory status include completed positive estimates versus pending tables; completed support correction versus symbolic unchosen endpoints; current welfare versus historical worked examples; and empty couples active set versus a bound-active experience diagnostic.

Build one current evidence map internally, then write from it. The paper need not contain that map or its paths. A dated preliminary-result note can acknowledge outstanding parameter intervals. Do not leave the literal Markdown placeholder in a circulated abstract. Do not remove an actual unresolved observation-rule problem just because it is inconvenient to the narrative.

## 28. The W3 diagnostic is neither defined nor presented sufficiently

**Evidence:** P4, p. 36 and welfare sections.

The reader sees an unexplained “relative-index companion measure,” bracket counts and negative-value counts without a complete mathematical definition or result table. State the actual gross-pay and resource reference once if W3 remains in the report. Otherwise reserve it for a properly labelled appendix rather than imply a completed contrast.

Failure of a numerical bracket is not by itself proof that a measure does not exist. Distinguish an insufficient upper bracket, an empty positive-consumption domain, and a target lying below the attainable reference range. Conversely, successful bracketing with “no negatives” is not sufficient for log-based indices if zeros remain. Positive welfare levels and a positive mean must be checked explicitly.

Do not make W3 or couples partial-resource repricing prerequisites for explaining the already selected primary measure. They are secondary to making the core paper coherent.

## 29. The canonical notebook remains incompletely described

**Evidence:** P4, Appendix A.1, pp. 38–39; R4, section 21.

One paragraph says the notebook exposes the pipeline end to end; the next says refitting does not reconstruct raw data, new alternatives or pricing. Distinguish a replay/refit interface from a genuine source-data-to-results interface.

The notebook can call reusable production functions rather than duplicate their internals. But the promised A-to-Z capability requires explicit runnable stages for source construction, generation of alternatives, pricing, estimation, inference, population prediction, welfare and figures. Report what exists and what remains; do not infer notebook capability from backend parity.

This review does not inspect the latest notebook implementation. Goal 1 should check it in the authorised workspace and retain one canonical notebook rather than creating another to satisfy the report wording.

## 30. Separate editorial work from genuinely new empirical work

The main fixes now are extraction, binding, derivation and rewriting. Updated tables from existing result files, corrected captions, a repaired welfare formula, and a revised introduction do not require a new model search.

A new calculation is justified when needed to resolve a concrete mathematical/source inconsistency, populate a previously authorised missing result, or regenerate a figure whose inputs changed. Keep those checks bounded. Do not introduce new model variants merely to obtain a more attractive abstract or protect the old ranking.

**Central now:** one current model, correct welfare formula, source-bound coefficients/fit/results, normative explanation, literature positioning and scholarly rewrite.  
**Useful later:** further welfare-family contrasts, causal regional designs, additional household structures and richer preference specifications not needed to resolve an identified current defect.  
**Not worth doing:** another broad literature collection, another general report, or a separate governance memo for every correction.

# VII. Consolidated instruction to Goal 1

**Chat:** Existing Goal 1 Manager, Thinking mode.  
**Execution:** Local Codex for source extraction, table/figure generation and builds in the authorised data environment. Goal 1 is responsible for the economic and mathematical account.  
**Attachments:** this review; `JMP_working_paper_for_seminar_v4.pdf`; `JMP_research_story_report_v4.html`; `novelty-audit-structural-well-being-inequality.docx`; `Literature_collection.md`. These files are confirmed available in the current conversation.  
**Workspace inputs Goal 1 must locate:** current LaTeX and bibliography; current single/couple model specifications and estimates; score/covariance/fit outputs; current household welfare and all coalition index tables; current data construction and descriptive outputs; theory figure source; figure generators; canonical notebook. Do not guess a current result path from an old review. No confidential person/household rows need to be uploaded to a chat.  
**Save:** revised existing manuscript as v5 `.tex` and compiled PDF with its `.bib` and figure/table dependencies; revised v5 research-story HTML and editable source; update the same notebook. Keep this review as one working memo and put only a short completion entry in the existing decision note.

```text
PI/DEPUTY — V5 SCHOLARLY REWRITE AND CURRENT-MODEL RECONCILIATION

Use the attached v4 review and the author's comments as ONE consolidated revision
instruction. The next deliverable is not v4 with another layer of warnings.

The objective is a readable economics paper and a genuinely explanatory report
which both describe the same current model and results.

1. ESTABLISH THE CURRENT MODEL FROM EXECUTED SOURCES

Resolve the v4 contradictions before rewriting around them:
- beta_c fixed at one versus estimated;
- estimated singles Box-Cox curvature versus theta_c fixed at zero;
- final samples versus historical funnels/descriptives;
- completed bounded support versus “not yet established”;
- empty couples active set versus a bound-active experience diagnostic;
- completed coefficients/fit versus all-pending result tables;
- corrected welfare versus historical worked examples and appendix status.

Confirm the current equations and source files internally. No new governance
report is required. If a contradiction is only stale prose, replace it. If it
reflects a real estimator, observation-rule or welfare-code inconsistency, return
that exact issue rather than declaring it repaired editorially.

2. REWRITE THE PAPER AS AN ECONOMICS PAPER

Retain exactly the agreed title.

Use one Introduction with integrated motivation, normative stance, relevant
literature, contribution, findings and a roadmap. No visible introductory
micro-subsections. Cite Haydar and Maniquet (2026), work in progress, not “the
companion project”. Explain the actual stochastic adaptation accurately.

Abstract: question, normative reference, latent-job approach, EUROMOD, main
within-type decomposition findings and the important index sensitivity.
Remove optimizer gains, nat conversions, machine closure, the first/second/third
inventory and the status-report paragraph. Do not fabricate parameter intervals.

Call the data section “Data”. Consolidate current sections 3 and 5 into the
actual model/framework sequence. Present welfare and grouped decomposition in
one connected methodological section following that model.

Remove reviewer-response prose, repeated denials and historical repair narration
from the main argument. Keep essential assumptions and limitations once, in the
appropriate places. Preserve scientific history in a separate report appendix.

3. CORRECT THE MATHEMATICS

For the reported log-consumption specification with estimated beta_c, use:

u = L + beta_c log(C/lambda_c)
J = integral exp(L) (C/lambda_c)^beta_c ghat dnu
H = integral exp(L) ghat dnu
W = lambda_c exp[(log J - log H)/beta_c].

The corresponding reference-weighted mean has order beta_c, not order one.
Update the derivative, worked examples, Q&A, plots and explanation together.
Check the printed formula against the current evaluator.

Separate reference weights, power-moment contributions and marginal welfare
sensitivities. Repair Figure 12 accordingly. beta_c is not theta_c.

For the W1/W4 bridge, reconcile the actual sign definition with:
L(home) >= L(j) and integral ghat = 1 imply L(home)-log H >= 0.
Do not simply flip the sentence to match the desired inequality.

The H wage-neutrality check is a fixed-reference property. A total welfare change
through attained value does not by itself disprove Independence of pay. State
only the property actually established and distinguish the deterministic theory
from the stochastic functional.

4. PRESENT THE EXISTING EVIDENCE

Populate the current coefficient tables, including beta_c, and observed-versus-
model fit for singles and couples. Show opportunity and wage blocks as well as
preferences. Bind current counts, scope and uncertainty; retain pins as restrictions.

Show corrected distributions and a current worked welfare example for each type.
Do not teach the current evaluator with beta_c=1 historical calculations.

Present the primary Gini allocation as reported, conditional on its reference,
and show one-factor effects separately. Do not carry forward the old 77% figure.

Correct the multi-index interpretation:
access exceeds resources/needs for singles in four of six indices; GE(1) and
GE(2) are exceptions. Combined access+earnings exceeds resources/needs in five
of six. The access-versus-earnings ordering differs between singles and couples
under all six. Preference sign for singles is index-sensitive.

Negative preference shares imply an adverse one-factor effect in this particular
exhaustive nonnegative-index two-group game; explain the conditional result, not
as a general definition of Shapley. Positive shares do not imply a favourable
one-factor effect.

Report six index levels and index-specific attribution. Label GE(2)=CV^2/2.
Supply the promised equivalized panel when available; otherwise remove the false
statement that it is already shown. Keep parameter and numerical intervals separate.

5. USE THE NOVELTY AUDIT CRITICALLY

Integrate Muehlhan (2023) and Creedy-Herault (2011) from their originals, alongside
the closest RURO and normative welfare papers. Cite the allocation machinery.
The new element is the application-specific structural welfare game and empirical
answer, not a new Shapley rule or the first use of full recomputation in general.

Do not use the novelty audit as a bibliography substitute or proof of priority.
No new broad literature search is requested.

6. FIGURES AND REPORT

Retain the theory figure with a shorter explanatory caption and appropriate credit.
Preserve the restored HTML sidebar and working offline mathematics.

Share equations, bibliography and result sources across outputs, not identical
prose. The report should explain each step with a question, equation, interpretation,
current worked example and evidence. Correct its Q&A; do not paste old answers.

Prioritize current data distributions, observed-versus-model fit, welfare
Lorenz/distribution plots and a signed decomposition display. Keep most nat and
normalization diagnostics in the report/appendix. Do not create more figures at
the expense of displaying the central welfare findings.

No private paths or internal mission labels in the circulated paper. Number
important equations and all tables. Inspect rendered output, including captions,
mathematics, table references and remaining obsolete claims.

7. DELIVER

Return:
- v5 LaTeX source, compiled PDF, bibliography and figure/table dependencies;
- v5 explanatory HTML with editable source;
- the existing canonical notebook updated, or a precise description of any
  remaining A-to-Z capability gap;
- only genuinely unresolved scientific matters.

No additional mission-document family. Do not re-estimate solely because prose
was stale; do rerun an affected calculation when an actual source or code error
requires it.
```

# Source key and selected original references checked

**[P4]** `JMP_working_paper_for_seminar_v4.pdf`, build 9 September 2026, 42 pages; uploaded in this conversation. Page-specific evidence is given throughout this review.

**[R4]** `JMP_research_story_report_v4.html`, build 9 September 2026; uploaded in this conversation. All substantive sections and Q&A were inspected; no raw household data or current numerical execution was accessed.

**[N]** `novelty-audit-structural-well-being-inequality.docx`, supplied novelty-positioning audit through 9 September 2026. Its qualified conclusions are used as a working comparison map.

**[E1]** Capéau, B., De Sadeleer, L., Maes, S., and Decoster, A. (2021). *Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare*. CESifo Working Paper 9071. Original publisher PDF: https://www.ifo.de/DocDL/cesifo1_wp9071.pdf . Abstract on PDF page 3; introduction and framework thereafter. Used here for the abstract's organization and as a distinct welfare-level literature comparator, not as the source of the JMP's estimator or reference formula.

**[E2]** Mühlhan, J. (2023). *The ‘German Job Miracle’ and Its Impact on Income Inequality: A Decomposition Study*. International Journal of Microsimulation, 16(1), 28–64. https://www.microsimulation.pub/articles/00274 . Original article inspected for the structural-income-decomposition comparison.

**[E3]** Creedy, J., and Hérault, N. (2011). *Decomposing Inequality and Social Welfare Changes: The Use of Alternative Welfare Metrics*. University of Melbourne working-paper version. https://fbe.unimelb.edu.au/__data/assets/pdf_file/0006/784257/1121.pdf . Section 5, printed pp. 21–24, defines the money-metric distributions and policy/population path average. This provides a direct antecedent to money-metric inequality decomposition, not the same opportunity game.

**[E4]** Audoly, R., McGee, R., Ocampo, S., and Paz-Pardo, G. (2025). *A Practitioner's Note on the Shapley-Owen-Shorrocks Decomposition*. Federal Reserve Bank of New York Staff Report 1163. https://www.newyorkfed.org/research/staff_reports/sr1163 . Use for the inherited grouped nonlinear allocation framework.

**[E5]** Capéau, B., Decoster, A., and Dekkers, G. (2016). *Estimating and Simulating with a Random Utility Random Opportunity Model of Job Choice: Presentation and Application to Belgium*. International Journal of Microsimulation, 9(2), 144–191. https://www.microsimulation.pub/articles/00139 . Relevant applied model/estimation exposition already discussed in P4; verify any particular assumption against the original rather than copying a general summary.

**Normative references to bind in the rewrite:** Haydar and Maniquet (2026), latest work-in-progress version in the author's repository; Fleurbaey and Maniquet (2017), *Fairness and Well-Being Measurement*, Mathematical Social Sciences 90, 119–126; Decoster and Haan (2015), *Empirical Welfare Analysis with Preference Heterogeneity*, International Tax and Public Finance 22, 224–251. The latest Haydar–Maniquet source and characterization were not independently re-audited for this document review. The rewrite must use the version actually supplying the stated principle.

---

**Final assessment:** The report now contains an empirical argument worth presenting. The next version should make that argument shorter, more coherent and more strongly evidenced—not more defensive. Success is one current model, one current welfare formula, source-bound results, an explicit normative interpretation and a paper that can be read without knowing the project's internal workflow.
