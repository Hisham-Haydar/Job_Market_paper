# Full Core Full Notes

Short prefatory note:
- generated from markdown files in `core_full_notes`
- includes 13 extracted papers in a single file
- sorted alphabetically by extraction filename
- section titles are based on extraction filenames for a cleaner index
- each section preserves the full extracted markdown content underneath
- index links use stable internal anchors

## Index

1. [Aaberge Colombino 2018](#paper-001)
2. [Aaberge Colombino Strom 1999](#paper-002)
3. [Aaberge Colombino Wennemo 2009](#paper-003)
4. [Bargain et al 2013](#paper-004)
5. [Beffy et al 2019](#paper-005)
6. [Bhattacharya 2015](#paper-006)
7. [Bourguignon Ferreira Menendez 2007](#paper-007)
8. [Capeau et al 2021](#paper-008)
9. [Dagsvik et al 2014](#paper-009)
10. [Dagsvik Jia 2016](#paper-010)
11. [Ferreira Gignoux 2011](#paper-011)
12. [Jacquet Jia Thoresen 2026](#paper-012)
13. [Shorrocks 2013](#paper-013)

---

<a id="paper-001"></a>

## Aaberge Colombino 2018

**Source file:** `core_full_notes/Aaberge_Colombino_2018.md`

---
title: "Structural Labour Supply Models and Microsimulation"
authors: [Rolf Aaberge, Ugo Colombino]
year: 2018
outlet: "International Journal of Microsimulation, 11(1), 162–197"
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "canonical"
---

## Full citation
Aaberge, R., & Colombino, U. (2018). Structural Labour Supply Models and Microsimulation. *International Journal of Microsimulation*, 11(1), 162–197.

## One-sentence contribution
The authoritative survey of structural labour-supply models — the conventional Discrete Choice (Van Soest) model and the Random Utility Random Opportunities (RURO) model — and their integration with tax-benefit microsimulation, with explicit treatment of the interpersonal-comparability problem in welfare evaluation, the choice between a common welfare function and Fleurbaey-style preference-respecting metrics, and the computational optimal-taxation problem.

## Core research question
How should structural labour-supply models be specified, estimated, and embedded in microsimulation pipelines for both positive policy evaluation and normative social-welfare analysis, and what trade-offs face the analyst choosing between a common welfare function (which assumes interpersonal comparability) and preference-respecting welfare metrics (which preserve heterogeneity but face the indexing dilemma)?

## Model / framework
Surveys two model classes side by side. (i) Discrete Choice with optional dummy refinements: $P(h)\propto\exp\{v(f(wh,I),h)\}\,\exp\{\gamma(h)\}$. (ii) RURO: $\varphi(w,h)\propto\exp\{v(f(wh,I),h)\}\,p(w,h)$ with $p(w,h)=p_1 g_1(h)g_2(w)$ for $h>0$. Establishes that DC is the special case of RURO when wages are fixed and the opportunity density is uniform, and gives the structural reinterpretation of DC dummies as opportunity terms ($\gamma_0=\ln J+A_0$, $\gamma_\ell=\ln(J_\ell/J)+A_\ell$). Welfare layer covers (a) a common utility function $V(y,h)$ used as the social planner's index, (b) the King (1983) equivalent income, and (c) the Fleurbaey preference-respecting class. The optimal-tax problem $\max_\vartheta W(U_1,\ldots,U_N)$ subject to incentive-compatibility and revenue constraints is solved by iterative microsimulation rather than analytically.

## Data
None new — the survey draws on Italian SHIW (1987, 1993), Norwegian administrative tax data (1979–2011), Swedish HINK (1981), and the cumulative empirical literature.

## Identification logic
Discusses identification at survey level. Preferences identified from tax-function non-linearities; opportunity-density parameters identified from the joint hours-wage distribution and participation rates; structural vs reduced-form interpretation of dummy coefficients drives the policy-invariance properties needed for ex-ante simulation. Argues forcefully that no observational design can identify policy-invariant parameters without a structural model (Marschak/Lucas).

## Treatment of preferences
Surveys two interpretations of the random component $\varepsilon$: as unobserved job attributes inside utility (the RUM/RURO interpretation) or as optimisation error outside utility (the conventional DC interpretation). The interpretation matters for welfare evaluation because the first includes $\varepsilon$ in welfare and the second excludes it. Heterogeneity flexibility runs from observed taste-shifters through Mixed Logit random parameters.

## Treatment of opportunities / constraints
Central. The paper argues that the RURO's structural representation of opportunities $p(w,h)$ is the key advantage for ex-ante policy simulation, because the DC dummies are reduced-form and may not be policy-invariant — a tax reform changes the labour demand and hence the opportunity density. The Colombino (2013) iterative equilibrium procedure exploiting the structural interpretation of the dummies is the recommended fix when the analyst wants to simulate not just labour supply but the joint equilibrium with reshaped opportunities.

## Welfare / normative object
Three approaches surveyed. (i) Common utility function $V(y,h)$ — same functional form as individual utility but homogeneous parameters; achieves interpersonal comparability by assumption. (ii) King (1983) equivalent income at reference characteristics and reference budget. (iii) Fleurbaey-Maniquet preference-respecting metrics — flagged as "promising" but acknowledged to be sensitive to the chosen reference, citing the Decoster & Haan (2015) work-loving-vs-work-averse critique. Both primal Atkinson SWFs and dual rank-dependent (Weymark/Yaari) SWFs are surveyed as aggregators.

## Main findings
(i) DC is a special case of RURO; RURO's "dummies" have a structural opportunity interpretation that DC's do not. (ii) Choice-set specification has dramatic out-of-sample consequences (citing Aaberge, Colombino & Wennemo 2009). (iii) Norwegian total labour-supply elasticity declined from positive to near zero between 1979 and 2011, mostly because the female extensive margin saturated. (iv) Computational optimal taxes generated by RURO + microsimulation deliver monotonically rising MTRs and a negative bottom MTR (in-work credit), in contrast to the U-shape predicted by analytical Mirrlees/Saez under restrictive assumptions. (v) The common-utility vs preference-respecting tension in welfare evaluation is not resolved by the paper — both have honest weaknesses.

## Main limitations
A survey, not a new empirical contribution. Dynamic and collective/bargaining models are mentioned but not developed. General-equilibrium and labour-demand effects are flagged but not synthesised in detail. The fundamental tension between the common-utility approach and preference-respecting welfare measures is acknowledged but not adjudicated.

## Quick takeaway
The reference survey for the entire RURO + microsimulation + social-welfare-evaluation pipeline. Its most important interpretive move is to position the common-utility function and the Fleurbaey preference-respecting metrics as competing rather than complementary approaches with no clear winner — exactly the unresolved tension that a $W(z,R,A;y)$ framework conditioning welfare on both preferences and opportunities is designed to resolve.

---

<a id="paper-002"></a>

## Aaberge Colombino Strom 1999

**Source file:** `core_full_notes/Aaberge_Colombino_Strom_1999.md`

---
title: "Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints"
authors: [Rolf Aaberge, Ugo Colombino, Steinar Strøm]
year: 1999
outlet: "Journal of Applied Econometrics, 14(4), 403–422"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Aaberge, R., Colombino, U., & Strøm, S. (1999). Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints. *Journal of Applied Econometrics*, 14(4), 403–422.

## One-sentence contribution
The first application of the Dagsvik (1994) job-choice framework to Italian data, jointly modelling spouses' labour supply over a fully non-convex tax-benefit budget set with explicit quantity constraints, and showing that the conventional Hausman approach overstates female unconditional hours elasticities by roughly sixty percent because it ignores opportunity rationing.

## Core research question
What are the labour supply elasticities and the distributional and behavioural effects of tax reforms in Italy when the model jointly accounts for (i) couples' joint decisions, (ii) the exact non-convex Italian budget set, and (iii) quantity constraints captured by an opportunity scale parameter $g_0$ that allows for involuntary non-participation?

## Model / framework
RURO model with multiplicative utility $U_i(C,h,j)=v_i(C,h)\,\varepsilon_{ij}$ and i.i.d. extreme-value job-level shocks. Each agent has a market opportunity set with conditional density $g_i(h,w)$ and a non-market option, with the relative scale $g_{0i}$ measuring market vs non-market availability. The choice probability is $\varphi_i(h,w)\propto\Psi_i(h,w)\,g_{0i}\,g_i(h,w)$ for $h>0$ where $\Psi_i(h,w)=v_i(f(wh,I),h)$. Systematic utility uses Box-Cox-style leisure terms with demographic shifters and a consumption term where the marginal utility of consumption is allowed to differ by employment status (capturing underground-economy income). Hours density is uniform with an estimated full-time peak $\theta_k=\exp(\alpha)$.

## Data
Bank of Italy Survey of Household Income and Wealth, 1987. 2,953 married couples, both spouses 20–68, excluding heavily self-employed. Italian 1987 tax-benefit system with eight progressive brackets (12%–62%) modelled exactly.

## Identification logic
Two pieces. First, $g_0$ is identified non-parametrically from the unemployment rate via $\rho=(1-g_0)\varphi(0,0)$: the gap between observed non-participation and what the model would predict in a "fair environment" with $g_0=1$ pins down the opportunity scarcity. Second, conditional on separability $v(C,h)=v_1(C)v_2(h)$, the marginal utility of income $v_1$ is identified from variation in the tax function with respect to fixed costs of work, after which the wage opportunity density $g_1(w\mid h)$ is identified from the residual variation. Cross-region variation in $g_0$ (North vs South) and in unemployment rates pins down its determinants.

## Treatment of preferences
Box-Cox in leisure for each spouse with quadratic-in-log-age and child-presence shifters; consumption enters via an exponential term whose level is allowed to differ by joint employment status, intentionally capturing the role of unreported income in Italy. Estimated utility is strictly concave in consumption and leisure for both genders.

## Treatment of opportunities / constraints
Opportunities are first-class. The hours opportunity density $g_2(h)$ is uniform with a full-time peak estimated at $\theta_F\approx 11$, $\theta_M\approx 12$ — full-time jobs are about an order of magnitude more prevalent than part-time slots. The opportunity scale $\log g_{0F}$ depends on a Northern-region indicator and the local female unemployment-to-employment ratio, and similarly for males. Estimates deliver $g_0<1$ for both genders, formal evidence of rationing, with significantly more female opportunities in the North.

## Welfare / normative object
None directly. Distributional impact of counterfactual tax regimes is summarised through the Gini coefficient on disposable income, but no money-metric or compensating-variation welfare object is computed.

## Main findings
(i) Aggregate uncomp. hours elasticities: 0.05 male, 0.74 female, the latter driven mainly by participation (0.65). (ii) Female elasticity falls from 3.44 in the poorest decile to 0.04 in the richest; the male elasticity turns negative (–0.04) at the top. (iii) The Hausman approach overstates the female unconditional hours elasticity by ~60% (1.18 vs 0.74) because it ignores opportunity rationing. (iv) A revenue-neutral flat tax at 26.3% raises the disposable-income Gini from 0.238 to 0.247 with negligible behavioural response; greater progression lowers it to 0.220 with a small drop in female participation. (v) Strong cross-spouse wage effects largely neutralise the partial-equilibrium own-wage responses.

## Main limitations
Static, single cross-section; no dynamic or life-cycle extensive margin. Wage opportunities and hours opportunities are assumed independent. The household objective is a unitary utility — no intra-household bargaining. The "underground economy" channel is captured only through a status-dependent consumption coefficient. No formal welfare measurement and no responsibility cut on $g_0$.

## Quick takeaway
The benchmark application showing that the RURO framework can be operationalised in a high-unemployment Southern European setting with strong opportunity heterogeneity, and that ignoring opportunity scarcity meaningfully biases the labour-supply elasticities that drive tax-reform evaluations. The structural identification of $g_0$ from the unemployment rate is a citable template for any RURO model that wants to put rationing on a quantitative footing.

---

<a id="paper-003"></a>

## Aaberge Colombino Wennemo 2009

**Source file:** `core_full_notes/Aaberge_Colombino_Wennemo_2009.md`

---
title: "Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply"
authors: [Rolf Aaberge, Ugo Colombino, Tom Wennemo]
year: 2009
outlet: "Journal of Economic Surveys, 23(3), 586–612"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Aaberge, R., Colombino, U., & Wennemo, T. (2009). Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply. *Journal of Economic Surveys*, 23(3), 586–612.

## One-sentence contribution
A controlled Monte-Carlo comparison of sixteen discrete-choice labour-supply specifications — crossing fixed vs sampled alternatives, six vs twenty-four points, and the inclusion of job and hours-peak dummies — that shows in-sample fit is essentially uninformative about model quality and that out-of-sample policy predictions are accurate only when the choice set explicitly carries opportunity-density features.

## Core research question
How sensitive are estimated labour-supply elasticities and tax-reform predictions to the specification of the discrete choice set, and which features of that specification — number of alternatives, fixed vs sampled draws, treatment of job availability — are responsible for accurate out-of-sample behaviour?

## Model / framework
The "true" data-generating process is a continuous RURO model on Norwegian women (Aaberge & Colombino 2006) with opportunity density $p(h,w)=p^0 g_1(h)g_2(w\mid h)$, where $g_1(h)$ has peaks at part-time and full-time hours. Sixteen alternative discrete-choice models are estimated on Monte-Carlo samples drawn from this true model, crossing four choice-set sizes (6 fixed, 24 fixed, 6 sampled, 24 sampled) with four treatments of job availability (no correction; job dummy $d_0$ alone; peaks dummies $d_1,d_2$ alone; both). All models share the same Box-Cox preference structure with extreme-value taste shocks, so the comparison isolates choice-set design.

## Data
Norwegian 1995 administrative + survey data, 1,842 married/cohabiting women aged 20–62. The true RURO is estimated once on this sample; 100 Monte-Carlo replicates of size 1,842 are then drawn from the estimated true model, and each candidate model is re-estimated on each replicate.

## Identification logic
The exercise inherits identification from the true RURO model. The diagnostic identification question is then operational: can simpler models recover the true model's out-of-sample predictions from in-sample data? In-sample fit is found to identify preferences across all sixteen specifications equally well; the opportunity component is identified only when the choice set carries explicit job-availability features ($d_0$ approximating $\log p^0$ and $d_1,d_2$ approximating the peaks in $g_1$).

## Treatment of preferences
Box-Cox utility in disposable income and leisure with age and child taste-shifters and Type-I extreme-value job-level shocks. Functional form is held identical across all sixteen variants so the experiment isolates choice-set effects rather than preference-form effects.

## Treatment of opportunities / constraints
The paper's centre of gravity. The true model has an opportunity scale $p^0<1$ (rationing), a hours density with two institutional peaks, and a log-normal conditional wage density. Candidate models approximate these with combinations of a job dummy (overall market vs non-market opportunity ratio) and peaks dummies (institutional bunching at part-time and full-time hours). Only specifications carrying both kinds of dummies recover the opportunity content of the true model.

## Welfare / normative object
None directly computed. The exercise is positive but the implications are explicitly normative: any welfare evaluation built on a model that mispredicts hours under the counterfactual cannot deliver credible welfare numbers under the same counterfactual.

## Main findings
(i) All sixteen models fit the 1995 baseline hours distribution similarly well. (ii) Under a revenue-neutral 25% flat-tax counterfactual, mean prediction errors range from 30–55% for specifications without opportunity-density features down to under 5% for the 24-sampled-alternatives specification with both job and peaks dummies. (iii) The interaction of "more alternatives" with "job dummy" matters more than either alone. (iv) The marginal value of peaks dummies exceeds that of the job dummy. (v) Sampled vs fixed alternatives matters less than the dummy structure once the latter is in place.

## Main limitations
The reference truth is itself a parametric RURO, not an external benchmark — the ranking of competing models is conditional on the RURO being correct. Only female labour supply is modelled; husbands are held fixed. Only one counterfactual (a flat tax) is examined. The Norwegian opportunity structure has unusually pronounced peaks, so quantitative magnitudes may not transfer cleanly to economies with smoother hours distributions. No welfare object is computed.

## Quick takeaway
The cleanest empirical demonstration that opportunity-density features are first-order for tax-reform predictions even when in-sample fit is indistinguishable. Any RURO-vs-Van-Soest comparison should cite this paper for the specific finding that "job dummy + peaks dummies + sampled alternatives" is the minimum specification that recovers the truth, and any welfare exercise that omits opportunity features should be expected to inherit the 30–55% bias seen in the labour-supply layer.

---

<a id="paper-004"></a>

## Bargain et al 2013

**Source file:** `core_full_notes/Bargain_et_al_2013.md`

---
title: "Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US"
authors: [Olivier Bargain, André Decoster, Mathias Dolls, Dirk Neumann, Andreas Peichl, Sebastian Siegloch]
year: 2013
outlet: "Social Choice and Welfare, 41(4), 789–817"
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "canonical"
---

## Full citation
Bargain, O., Decoster, A., Dolls, M., Neumann, D., Peichl, A., & Siegloch, S. (2013). Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US. *Social Choice and Welfare*, 41(4), 789–817.

## One-sentence contribution
Operationalises three Fleurbaey-style welfare metrics — "wage" (full responsibility for preferences), "rent + reference wage" (intermediate), and "rent" (full compensation for preferences) — on harmonised micro-data and tax-benefit simulators for twelve countries, and shows that the choice between compensation and liberal-reward axioms shifts cross-country welfare rankings by tens of percentile points and is driven primarily by country-specific preference parameters rather than by demographic composition.

## Core research question
How do cross-country welfare rankings of married women's households change when one moves from income-based comparisons to leisure-inclusive welfare metrics that take different normative positions on the responsibility individuals should bear for their consumption-leisure preferences?

## Model / framework
Country-specific Box-Cox discrete-choice labour-supply model in seven hours categories with extreme-value taste shocks: $u_i(c,T-h)=\beta_c(c^{\alpha_c}-1)/\alpha_c+\beta_{li}((T-h)^{\alpha_l}-1)/\alpha_l$, $\beta_{li}=\beta_{l0}+\beta_{lz}z_i$. Three welfare metrics from Fleurbaey (2006, 2008): the "wage" metric $v_i^W$ (minimum hypothetical wage at zero non-labour income that delivers utility $u$), the "rent + reference wage" metric $v_i^{RW}$ (expenditure function evaluated at a reference wage $w^r$ taken at p25/p50/p75 of the pooled wage distribution), and the "rent" metric $v_i^R$ (consumption at zero hours that delivers $u$). The latter two are limit cases of the first.

## Data
Harmonised household micro-data for 12 countries circa 2001 (EU-SILC, ECHP, GSOEP, IPUMS-CPS). Tax-benefit rules simulated by EUROMOD v.D16 for European countries and TAXSIM v.9 for the US. Sample is married women with working-age partners; husbands' hours are fixed; non-worker wages are imputed via Heckman selection.

## Identification logic
Preference parameters are identified country-by-country from observed labour-supply choices over known tax-benefit budget constraints — the standard van Soest identification. Welfare metrics are then computed deterministically from the estimated indifference curves; no further identification assumptions are required. The decomposition exercise (Section 5.3) identifies the relative roles of demographic composition and country-specific preference parameters by counterfactually swapping each across countries.

## Treatment of preferences
Preferences are the central object. Heterogeneity is allowed across two dimensions: observed taste-shifters $z_i$ (age, education, children) entering $\beta_{li}$, and country-specific deep parameters $(\alpha_c,\alpha_l,\beta_c,\beta_{l0})$. The paper does not adjudicate which metric is normatively correct; it documents that the choice has first-order empirical consequences. MRS at a common bundle ranges from 3.7 PPP-USD/h (Portugal) to 17.6 (Ireland), a near 5× spread.

## Treatment of opportunities / constraints
Opportunities enter only through the budget constraint and the wage rate. There is no explicit modelling of opportunity densities, job availability, rationing, fixed costs of work, childcare provision, or part-time availability. The paper acknowledges this as a key limitation: country-specific "preferences" partly absorb country-specific opportunity constraints.

## Welfare / normative object
Three individual-level money-metric welfare measures, all ordinal and respecting the compensation principle for individuals with identical preferences. They differ in their treatment of the liberal-reward principle. No social welfare function is applied — the paper deliberately stops at interpersonal comparisons because aggregation requires further normative choices (the Fleurbaey-style indexing dilemma).

## Main findings
(i) Income rankings differ markedly from preference-respecting welfare rankings: the US drops from a percentile rank of 63.3 (income) to 60.9 ("wage") and 62.4 ("rent"); Ireland rises from 53.1 to 58.2 ("wage"); Finland drops from 29.7 to 24.1 ("rent"). (ii) For seven of twelve countries the rent-vs-wage gap exceeds 3 percentile points. (iii) The decomposition shows that country-specific preference parameters, not demographic composition, drive the metric-dependent reranking. (iv) Cross-country MRS varies by a factor of nearly five at a common bundle, identifying which countries are flagged as "work-loving" vs "work-averse". (v) Robustness to Box-Cox vs quadratic utility, to alternative reference households, and to alternative aggregation rules within the metric is high.

## Main limitations
No demand-side opportunity modelling — involuntary unemployment, hours rationing, and fixed costs are absorbed into the preference block. Sample restricted to married women; men and singles excluded. No SWF aggregation. Static, no life-cycle. Most consequentially, country-specific "preferences" almost certainly capture cross-country differences in opportunities (childcare, part-time availability, institutions), so the central finding cannot cleanly be attributed to genuine taste differences.

## Quick takeaway
The leading empirical demonstration that the normative choice between compensation-principle and liberal-reward welfare metrics has first-order consequences for cross-country welfare rankings, and the paper any responsibility-sensitive welfare exercise will cite for the menu of money-metric formulas it makes operational. Its most important caveat — that the model conflates $R$ and $A$ — is exactly the gap a RURO-based welfare exercise can close.

---

<a id="paper-005"></a>

## Beffy et al 2019

**Source file:** `core_full_notes/Beffy_et_al_2019.md`

---
title: "Labour Supply and Taxation with Restricted Choices"
authors: [Magali Beffy, Richard Blundell, Antoine Bozio, Guy Laroque, Maxime Tô]
year: 2019
outlet: "Journal of Econometrics, 211(1), 16–46"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Beffy, M., Blundell, R., Bozio, A., Laroque, G., & Tô, M. (2019). Labour Supply and Taxation with Restricted Choices. *Journal of Econometrics*, 211(1), 16–46.

## One-sentence contribution
A "two-offer" structural labour-supply model in which each woman chooses among exactly two randomly drawn hours offers and the offer distribution is identified separately from preferences using non-linearities in the budget constraint, with the empirical finding that ignoring offer restrictions roughly doubles estimated Frisch and Marshallian elasticities for UK mothers.

## Core research question
Can preferences and the distribution of hours offers be separately identified when individuals face restricted choice sets, and what does that separation imply for estimated elasticities, predicted employment, and the response of women's labour supply to a major welfare-reform episode?

## Model / framework
Life-cycle CRRA utility $u(c,h)=c^{1-\gamma}/(1-\gamma)+a(L-h)^{1-\phi}/(1-\phi)$ with fixed costs of work $b$. Each agent receives two i.i.d. hours offers from a discrete distribution $g=(g_1,\ldots,g_I)$ and picks the offer (or non-participation) with the highest indirect utility. Choice probabilities take the closed form $\ell_i=g_i^2+2g_i\sum_{j\neq i}g_j p_i(\{i,j\})$. The dominated set $H^W$ — hours ranges where the budget function $S(w,h)=\sup_{x\le h}R(w,x)$ is flat — provides a nonparametric rejection device: any choices observed there must reflect offer restrictions, not preferences. The $n$-offer generalisation converges to the unrestricted discrete-choice model as $n\to\infty$.

## Data
UK Family Expenditure Survey 1997–2002, 10,575 women with children (single or married mothers). Tax-benefit rules simulated through IFS-Taxben — Working Families' Tax Credit, Income Support, Family Credit, rent and local-tax rebates produce highly non-convex budget sets. Median hourly wage £5.85; median usual hours 26/week; ~37% non-employment.

## Identification logic
Three sequential results. (i) Lemma 1: with $g$ known, preference utilities are uniquely identified from observed choice shares via a system whose Jacobian is dominant-diagonal (Gale-Nikaido). (ii) Lemma 2: with preferences known, $g$ is uniquely recovered from the same system with roles reversed. (iii) Joint identification under three conditions — a parametric dimension count, semi-parametric exclusion restrictions from cross-sectional budget-constraint heterogeneity (e.g. spouse income shifts $R$ but not $g$), and nonparametric identification of $g$ from observed choices in dominated regions of the budget set.

## Treatment of preferences
CRRA in consumption and leisure with observed shifters (cohabiting, age of youngest child, birth cohort) and unobserved normal taste shock. The framework deliberately purges preferences of demand-side contamination: estimated $\phi$ rises sharply once offer restrictions are introduced, indicating that part of what conventional models read as a strong taste for leisure is actually offer rationing.

## Treatment of opportunities / constraints
The offer distribution $g(h\mid Z^o)$ is the explicit opportunity primitive — a mixture of two truncated normals with means at ~15 and ~38 hours, mixture weight $p_1$ allowed to depend on education, location, and year. More-educated women receive proportionally more full-time offers. The constrained-vs-unconstrained gap is large: predicted employment 62.5% vs 71%, average hours 26.2 vs 35.5. Women rejecting the unrestricted-choice model are disproportionately lone, young, low-wage, and high-fertility.

## Welfare / normative object
None directly. The framework is purely positive but the building blocks for a welfare exercise are present: the gap between constrained realised utility and the unconstrained optimum is an individual-level money-metric cost of the offer restriction.

## Main findings
(i) 2.6% of working women observed at strictly dominated hours; 7.9% fail the parametric revealed-preference inequality. (ii) Mixture means of the offer distribution at $m_1\approx 15$ and $m_2\approx 38$ hours. (iii) Adding offer restrictions halves estimated elasticities — Frisch falls from ~0.58 to ~0.30, Marshallian from ~0.58 to ~0.20. (iv) Removing all hours restrictions in simulation raises mean hours by ~9 and employment by ~9 percentage points. (v) Women who fail the unrestricted model are economically poorer households on average.

## Main limitations
The "two" in "two-offer" is unmotivated by data — the $n$-offer generalisation is sketched but not estimated. The offer distribution is over hours only, not over (hours, wage) pairs, so wage rationing is invisible. Offers are independent of preferences (no sorting). Sample is restricted to women with children; men and childless women are excluded. Static framework applied across a period of major welfare reform. No welfare object is constructed.

## Quick takeaway
The cleanest formal identification result for separating preferences from opportunities in a discrete-choice labour-supply model, with budget-set non-linearities playing the role of an exclusion restriction. The empirical headline — accounting for offer restrictions roughly halves elasticities — is the strongest single piece of evidence that conflating $R$ and $A$ has first-order quantitative consequences for the policy elasticities that drive tax-reform welfare numbers.

---

<a id="paper-006"></a>

## Bhattacharya 2015

**Source file:** `core_full_notes/Bhattacharya_2015.md`

---
title: "Nonparametric Welfare Analysis for Discrete Choice"
authors: [Debopam Bhattacharya]
year: 2015
outlet: "Econometrica, 83(2), 617–649"
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "canonical"
---

## Full citation
Bhattacharya, D. (2015). Nonparametric Welfare Analysis for Discrete Choice. *Econometrica*, 83(2), 617–649.

## One-sentence contribution
Establishes that for binary and unordered multinomial discrete choice with arbitrary unobserved preference heterogeneity, the marginal distributions of equivalent and compensating variation from a price change are point-identified as closed-form functionals of conditional choice probabilities — but the same identification fails for ordered choice at a uniform unit price.

## Core research question
Under what conditions on the structure of the discrete-choice problem can the entire distribution of money-metric welfare (EV and CV) from a discrete price change be recovered nonparametrically from observed choice probabilities, without specifying the functional form of utility, the dimension of the heterogeneity vector, or its distribution?

## Model / framework
A consumer with income $Y$ chooses among $J+1$ alternatives at known prices and receives utility $U_j(Y-p_j,\eta)$ that is continuous and strictly increasing in the numeraire (the only substantive assumption). Under a price change $p_0\to p_1$ for alternative $j$, EV takes one of three values per type $\eta$: zero (non-buyers at both prices), $t(y,\eta)-p_0$ for switchers (where $t$ is the reservation price), or $p_1-p_0$ for inframarginal buyers. Aggregating, the EV CDF is $\Pr\{S^{EV}\le a\}=1-\bar q(p_0+a,y)$ on $[0,p_1-p_0]$, and the CV CDF is the same expression with $y$ replaced by $y+a$. Section 3 shows that for ordered choice at a uniform unit price the analogous identification fails because price variation does not generate the orthogonal coverage required to trace the welfare distribution.

## Data
None. The paper is purely theoretical, with a brief computational example using multinomial logit.

## Identification logic
The trick is to slice the population by reservation price: changes in the price-income pair sweep out exactly the boundary types whose welfare equals the local price increment. Because choice probabilities $\bar q(p,y)$ identify the mass of switchers between every pair of (price, income) pairs, they identify the entire welfare CDF. The result requires variation in own price and income but not in the structure of $U$ or in the heterogeneity distribution. The negative ordered-choice result follows because uniform per-unit pricing collapses the price grid that the unordered case relies on.

## Treatment of preferences
Maximally general. Heterogeneity vector $\eta$ has unknown dimension, unknown distribution, and enters utility in an arbitrary way. The only restriction is local non-satiation in the numeraire. This is strictly weaker than the quasilinear-utility assumption (Domencich & McFadden 1975), the no-income-effects approximation (Small & Rosen 1981), or the parametric heterogeneity assumed by Herriges & Kling (1999) and Dagsvik & Karlström (2005).

## Treatment of opportunities / constraints
Not modelled. The choice set is assumed to be the same full menu for every consumer; no rationing, no demand-side restrictions, no heterogeneous feasible sets. Welfare variation arises entirely from preference heterogeneity.

## Welfare / normative object
The full marginal distributions of EV and CV — strictly more informative than the mean. Mean welfare follows as a corollary: $E(EV)=\int_{p_0}^{p_1}\bar q(p,y)\,dp$ (the change in Marshallian consumer surplus, generalised beyond quasilinear utility) and $E(CV)=\int_{p_0}^{p_1}\bar q(p,y+p-p_0)\,dp$. For normal goods $E(EV)\le E(CV)$. Distributions can be aggregated into any social welfare functional, but the paper does not aggregate.

## Main findings
(i) Theorem 1: closed-form EV and CV CDFs from binary choice probabilities. (ii) Theorem 2: extension to unordered multinomial via composite outside option. (iii) Corollary 1: average EV equals the change in Marshallian consumer surplus regardless of income effects. (iv) Section 3 (negative): for ordered choice at a uniform unit price, welfare distributions are not point-identified. (v) Appendix: distinct heterogeneity distributions can produce identical choice probabilities yet still imply identical welfare distributions — heterogeneity itself need not be identified.

## Main limitations
Static one-period framework. Assumes free choice — no rationing, no restricted choice sets. Requires substantial price and income variation in the data, which may be unavailable. The negative ordered-choice result directly bites for the most common labour-supply discretisation (van Soest hours grid at a single wage). No empirical application; the companion empirical paper is Bhattacharya (2018).

## Quick takeaway
The benchmark identification result for nonparametric welfare analysis in discrete choice. The positive result vindicates frameworks that treat alternatives as unordered (each with its own price/wage) — including RURO — as theoretically capable of nonparametric welfare identification. The negative result is the hidden cost of ordered-hours discrete-choice labour-supply models: any welfare object computed from them carries identification only via the maintained parametric form.

---

<a id="paper-007"></a>

## Bourguignon Ferreira Menendez 2007

**Source file:** `core_full_notes/Bourguignon_Ferreira_Menendez_2007.md`

---
title: "Inequality of Opportunity in Brazil"
authors: [François Bourguignon, Francisco H. G. Ferreira, Marta Menéndez]
year: 2007
outlet: "Review of Income and Wealth, 53(4)"
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "canonical"
---

## Full citation
Bourguignon, F., Ferreira, F. H. G., & Menéndez, M. (2007). Inequality of Opportunity in Brazil. *Review of Income and Wealth*, 53(4).

## One-sentence contribution
Operationalises Roemer's circumstance-vs-effort distinction on Brazilian male earnings data via a counterfactual-based decomposition that equalises observed circumstances and recomputes inequality, finding that five exogenous circumstance variables account for 10–37% of the Theil index of urban male earnings inequality across cohorts, with roughly 60% of that effect operating directly on wages rather than through observed effort proxies.

## Core research question
What share of observed male earnings inequality in urban Brazil can be attributed to exogenous circumstances (race, region of birth, parental education, father's occupation) versus "effort," and how much of the circumstance effect operates directly on wages rather than indirectly through circumstance-influenced effort variables such as schooling, migration, and labour-market status?

## Model / framework
A reduced-form earnings function $w_i=f(C_i,E(C_i,v_i),u_i)$ where $C_i$ are circumstance variables, $E_i$ are "effort" variables themselves shaped by $C_i$ (effort in quotation marks because they are not derived from optimisation), and $u_i$ is an unobserved residual. The opportunity share is defined as $\Theta_I=[I(F)-I(\Phi)]/I(F)$, with $I(\Phi)$ the inequality of the counterfactual distribution that equalises observed circumstances. A direct-effect decomposition $\Theta_I^d=[I(F)-I(F^d)]/I(F)$ separates the part of the circumstance effect that operates conditional on observed efforts. There is no utility function, no labour-supply model, and no explicit feasible-set object.

## Data
PNAD 1996 household survey from IBGE, restricted to urban males aged 26–60 with positive earnings — 28,474 observations across seven five-year birth cohorts (1936–1940 through 1966–1970). Outcome: real hourly earnings.

## Identification logic
The decomposition is not point-identified causally because the residual $u$ may be correlated with the regressors. The paper deploys a partial-identification strategy: a Monte Carlo procedure draws admissible correlations between regressors and residuals subject to positive-semi-definiteness and sign restrictions, constructs the implied unbiased coefficient estimates, and reports 90% confidence intervals across the admissible set. Results are presented as bounds rather than point estimates — a methodological strength relative to the rest of the IOp literature.

## Treatment of preferences
None. There is no utility function and no behavioural model. The "effort" variables are observed proxies, not optimisation outputs — the authors place the term in quotation marks throughout because schooling, migration, and labour-market status are themselves shaped by circumstances and luck. Preference heterogeneity is invisibly bundled into the residual.

## Treatment of opportunities / constraints
Opportunities are operationalised through observed background circumstances — the Roemerian rather than the RURO conception. There is no representation of feasible job sets, latent offers, hours restrictions, or local labour-demand variation. A worker with "good" parental circumstances facing a depressed local market is indistinguishable in the data from a worker with the same circumstances facing a thriving market.

## Welfare / normative object
None directly. The decomposed object is observed earnings inequality (Theil, with Gini robustness). Normative motivation is compensatory in spirit — earnings inequalities driven by circumstances beyond individual control are flagged as unfair — but there is no explicit welfare measure that combines bundles, preferences, feasible sets, and tax schedules.

## Main findings
(i) Five observed circumstances explain 10–37% of the Theil index of male earnings inequality across cohorts, with a simple average of about 23%. (ii) About 60% of that opportunity effect operates directly on wages conditional on observed effort, rather than through schooling/migration/labour-market-status channels. (iii) Parental education is the most important individual circumstance variable; father's occupation second; race matters more for younger cohorts. (iv) Weak evidence of a declining opportunity share for younger cohorts, but cohort effects cannot be cleanly separated from time effects. (v) Bounded inference produces coherent confidence intervals around all of these magnitudes.

## Main limitations
Opportunities are proxied by observed background variables rather than represented as feasible sets — a worker with bad local job availability is not flagged as opportunity-deprived if their parental circumstances are good. The "effort" residual contains preference heterogeneity, luck, measurement error, and unobserved circumstances, mixed indistinguishably. Outcome is current earnings of active men only — excludes participation, household composition, non-labour income, and broader well-being. Identification is bounded rather than point.

## Quick takeaway
The benchmark empirical demonstration of Roemerian opportunity decomposition on a developing-country dataset, with admirable methodological discipline (partial identification via Monte Carlo). Its central limitation — that "opportunities" are observed background characteristics rather than feasible sets — is exactly the gap that a structural RURO-based opportunity primitive can close, and the direct/indirect architecture is a useful template for richer multi-channel decompositions.

---

<a id="paper-008"></a>

## Capeau et al 2021

**Source file:** `core_full_notes/Capeau_et_al_2021.md`

---
title: "Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare"
authors: [Bart Capéau, Liebrecht De Sadeleer, Sebastiaan Maes, André Decoster]
year: 2021
outlet: "CESifo Working Paper No. 9071"
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "canonical"
---

## Full citation
Capéau, B., De Sadeleer, L., Maes, S., & Decoster, A. (2021). Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare. *CESifo Working Paper No. 9071*.

## One-sentence contribution
Extends the nonparametric welfare-identification programme from Bhattacharya (2015) to Fleurbaey-style nested opportunity set (NOS) welfare measures, showing that the joint distribution of welfare *levels* and *differences* — and therefore additively-separable social welfare — is identified from choice and transition probabilities alone, with a German SOEP application that finds ~15% of single females lose from a flat-tax + basic-income reform and that losers are disproportionately initially well-off.

## Core research question
Can the marginal, conditional, and joint distributions of NOS welfare levels (a class that nests money-metric utility and equivalent income), of welfare differences such as compensating variation, and of the social welfare functional that aggregates them, be nonparametrically identified from observed choice and transition probabilities in DC-RUMs with unrestricted unobserved preference heterogeneity?

## Model / framework
A DC-RUM with $n$ alternatives, a numeraire, and an arbitrary unobserved preference type $\omega$. Utility $U_c^\omega(y-p_c)$ is continuous and strictly increasing in the numeraire (A1), with $F(\omega)$ exogenous to $(\mathbf{p},y)$ (A2) and standard utility maximisation (A3). The NOS welfare measure $W^\omega(y-p_k,k)=\sup_\lambda\{\lambda\mid U_k^\omega(y-p_k)\ge\max_{(y',c)\in B_\lambda}U_c^\omega(y')\}$ uses a common nested family of opportunity sets and includes money-metric utility, Pazner ray utilities, and equivalent income as special cases. The pivotal Lemma 1 translates "welfare exceeds $w$" into "alternative $k$ is optimal at virtual prices $\tilde{\mathbf{p}}(w)$", which is what reduces welfare distributions to functionals of choice/transition probabilities.

## Data
German SOEP 2018, 1,922 single females under 60, hourly wages 4–90 EUR, asset income below 12,000 EUR/yr. Three discrete alternatives — non-working, part-time (5–32h/wk), full-time ($\ge$ 32h/wk) — with disposable incomes from a German tax-benefit calculator. Counterfactual: replace the progressive tax with a 42% flat rate plus an unconditional basic income (revenue-neutral on the full SOEP).

## Identification logic
Lemma 1 maps welfare events to choice events at virtual prices. Theorem 1 turns the marginal welfare CDF into a single-choice probability $P_k$ evaluated at virtual prices; Theorems 2–4 turn joint distributions of welfare levels and CV into transition probabilities $P_{i,j}$ at combinations of actual, post-reform, and virtual prices; Proposition 2 expresses any additively-separable social welfare functional as an integral of choice probabilities. With cross-sectional data only, transition probabilities are not point-identified but are bounded via Boole-Fréchet inequalities and a stochastic revealed-preference shape restriction (Proposition 3), giving sharp upper and lower envelopes for welfare distributions and SWF differences.

## Treatment of preferences
Maximally general: $\omega$ has arbitrary dimension and distribution. The paper deliberately does not recover preferences or their distribution — the welfare distributions are identified without recovering either. This is the core methodological contribution and the strongest possible robustness statement against parametric mis-specification of $v(C,h)$ in the labour-supply welfare literature.

## Treatment of opportunities / constraints
Not modelled empirically. The choice set $\{NW,PT,FT\}$ is treated as freely available to all individuals. Opportunities enter only as the family of nested *virtual* opportunity sets $B_\lambda$ used to define welfare — these are normative reference objects, not descriptions of demand-side rationing. The paper acknowledges that endogeneity of $(\mathbf{p},y)$ to $\omega$ would violate A2, and that real-world heterogeneity in actual choice sets is outside the framework.

## Welfare / normative object
Several layers. (i) Distribution of NOS welfare levels for individual ranking. (ii) Distribution of CV for distributional incidence of price changes. (iii) Joint distribution of levels and CV for "who-gains-where-on-the-distribution" analysis. (iv) Additively-separable social welfare functional with NOS welfare as the sub-utility.

## Main findings
(i) Theorems 1–4 deliver closed-form representations of welfare distributions as functionals of choice/transition probabilities. (ii) Proposition 2: SWF differences are integrals of choice probabilities at virtual prices. (iii) Proposition 3: cross-sectional Boole-Fréchet bounds on transition probabilities, sharpened by stochastic revealed preference. (iv) Empirically, ~25% of single females have deterministic welfare under MMU at actual reference prices. (v) High-wage full-time workers' welfare first-order dominates other groups, but lower wage quartiles are intermingled — unobserved preferences carry meaningful weight in welfare levels. (vi) The flat-tax + basic-income reform first-order dominates the baseline SWF, but ~15% lose, and losers are concentrated in the initially best-off third (13.1% loser rate vs 0.6% in the bottom third).

## Main limitations
Working paper. Empirical application uses only three alternatives, so the welfare distribution is necessarily coarse. Cross-sectional data deliver bounds rather than point identification of joint level-difference distributions. Estimation of choice probabilities uses semiparametric logits with shape-restriction penalties, so functional-form bias is not literally absent. No demand-side opportunity modelling — all choice variation attributed to preferences. Sensitivity to the choice of reference prices for MMU is not explored. The ordered-choice issue from Bhattacharya (2015) is acknowledged but not solved.

## Quick takeaway
The most general nonparametric welfare-identification result available for discrete choice — and the one that makes Fleurbaey-style welfare levels (not just differences) operational. For any RURO welfare exercise, this is the benchmark of what is identifiable without parametric structure on preferences or heterogeneity, and the empirical illustration provides a clean template for the joint level-difference distributional analysis of a tax reform.

---

<a id="paper-009"></a>

## Dagsvik et al 2014

**Source file:** `core_full_notes/Dagsvik_et_al_2014.md`

---
title: "Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs"
authors: [John K. Dagsvik, Zhiyang Jia, Tom Kornstad, Thor O. Thoresen]
year: 2014
outlet: "Journal of Economic Surveys, 28(1), 134–151"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Dagsvik, J. K., Jia, Z., Kornstad, T., & Thoresen, T. O. (2014). Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs. *Journal of Economic Surveys*, 28(1), 134–151.

## One-sentence contribution
A unified survey-style defence of the latent-jobs framework: it shows that the ad hoc hours dummies in the conventional discrete-choice model (Van Soest 1995) have an exact structural reinterpretation as the log of an opportunity measure plus a log opportunity distribution, and argues on this basis that the latent-jobs model is the theoretically appropriate baseline for labour-supply analysis.

## Core research question
How should the discrete-choice labour-supply framework be extended from a discretisation of the standard consumer problem to a structural model of job choice that explicitly distinguishes preferences over consumption and leisure from demand-side restrictions on the set of available jobs?

## Model / framework
Compares three nested approaches: (i) the Hausman continuous labour-supply equation; (ii) the conventional discrete-choice model with ad hoc hours dummies $\gamma(h)$; (iii) the job-choice model where utility is $U(C,h,z)=v(C,h)+\varepsilon(z)$ with i.i.d. extreme-value job-level taste shocks and the choice set contains $m(h)$ latent jobs at each hours level. Defining $\theta=\sum_h m(h)$ and $g(h)=m(h)/\theta$, the choice probability becomes a logit in $\psi(h)+\log\theta+\log g(h)$ (eq. 14) — formally identical to the dummy-augmented Van Soest model with the explicit identification $\gamma(h)=\log\theta+\log g(h)$. Box-Cox systematic utility is justified by invariance axioms.

## Data
The paper is a survey rather than an empirical study. Empirical illustrations use Norwegian Labour Force Survey 1997 (estimation) and 2003 tax-return / 2006 Labour Force Survey data for out-of-sample validation across a tax reform that cut the top marginal rate from 55.3% to 47.8%.

## Identification logic
Without functional-form restrictions only the sum $\psi(h)+\log g(h)$ is identified — preferences and opportunities are confounded. Two routes restore separation: parametric structure on $v(C,h)$ (the Box-Cox specification with invariance) or external information on desired hours (Euwals & van Soest 1999; Bloemen 2008). For tax/wage counterfactuals one does not actually need the separation, because only the income component of $v$ enters changes in the budget constraint.

## Treatment of preferences
$v(C,h)$ is treated as a true structural utility. The paper's central interpretive claim is that the convention of letting $\gamma(h)$ enter additively with $v(C,h)$ — and then calling the sum "preferences" — implies non-monotone preferences over hours, which is implausible. Reassigning $\gamma(h)$ to opportunities preserves a well-behaved $v(C,h)$.

## Treatment of opportunities / constraints
Opportunities are first-class. They consist of (i) an opportunity measure $\theta$ (total available jobs, allowed to depend on education and demographics, and interpretable as containing fixed costs of work) and (ii) an opportunity distribution $g(h)$ (fraction of available jobs at each hours level, typically uniform with peaks at full-time and part-time). $\theta$ in principle has a two-sided matching microfoundation but the survey treats it as exogenous in the short run.

## Welfare / normative object
None directly. But the paper makes the welfare-relevant point that conflating $g(h)$ with preferences via $\gamma(h)$ implies any welfare measure built on the misidentified utility will misclassify constrained outcomes as voluntary choices. References Dagsvik & Karlström (2005) for the matching CV machinery.

## Main findings
(i) The dummy-augmented Van Soest model and the latent-jobs model are *observationally equivalent* in their reduced form but interpretively distinct. (ii) The latent-jobs model provides a structural rationale for hours peaks. (iii) The framework can simulate demand-side counterfactuals (e.g. removing part-time positions) that the conventional model cannot. (iv) Out-of-sample, the model predicts the post-reform 2006 hours distribution well for women, less well for men. (v) Wage elasticities are not constant — they scale with $(1-P)$, so cross-country elasticity differences may partly be a mechanical consequence of differences in participation rates rather than of preferences or opportunities.

## Main limitations
A survey paper, not an empirical contribution; the authors explicitly state the alternative model "will in general not provide better fit." $g(h)$ is held fixed in the short run, so equilibrium responses of opportunities to large reforms are ignored. IIA is maintained. Nonparametric identification of preferences vs opportunities fails. No welfare analysis is implemented.

## Quick takeaway
The framing manifesto for RURO/latent-jobs labour supply. Its central, citable result is the equivalence $\gamma(h)=\log\theta+\log g(h)$, which gives any future RURO welfare or decomposition exercise a clean reinterpretation of the dummy-augmented conventional model as a special case where opportunities have been silently absorbed into preferences.

---

<a id="paper-010"></a>

## Dagsvik Jia 2016

**Source file:** `core_full_notes/Dagsvik_Jia_2016.md`

---
title: "Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification"
authors: [John K. Dagsvik, Zhiyang Jia]
year: 2016
outlet: "Journal of Applied Econometrics, 31(3), 487–506"
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "canonical"
---

## Full citation
Dagsvik, J. K., & Jia, Z. (2016). Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification. *Journal of Applied Econometrics*, 31(3), 487–506.

## One-sentence contribution
Provides the first formal nonparametric identification analysis of the latent-jobs (RURO) labour-supply model and shows that preferences and the opportunity measure cannot be separately recovered from cross-sectional choice data without parametric structure, while Box-Cox utility plus regularity conditions restore full identification.

## Core research question
Under what conditions are preferences $v(C,h)$ and the opportunity measure $\theta\, g_1(h)\, g_2(w\mid h)$ separately identified in a latent-jobs labour-supply model from cross-sectional data on hours, wages, and non-labour income, and does it matter empirically whether wage heterogeneity is modelled as variation across jobs or across individuals?

## Model / framework
A multiplicative random-utility random-opportunity model. Utility on a job is $U(C,h,z)=v(C,h)\varepsilon(z)$ with i.i.d. extreme-value taste shocks. Job offers arrive as an inhomogeneous Poisson process: market intensity $\theta$, hours density $g_1(h)$, conditional wage density $g_2(w\mid h)$. Choice probabilities have the standard RURO logit-style form (eq. 2a). Two competing wage-heterogeneity specifications are compared: Model 1 with job-specific wage shocks (Aaberge, Colombino & Strøm 1999 style) and Model 2 with individual-specific wage random effects.

## Data
Norwegian Labor Survey 1997. 2,515 married/cohabiting couples aged 25–64, neither self-employed nor in education. Eight feasible annual hours: 0, 208, 624, 1040, 1456, 1950, 2340, 2600.

## Identification logic
The fundamental equation is the ratio of working to non-working choice probabilities: $\varphi(h,w\mid I)/\varphi(0,0\mid I)\propto v(f(hw,I),h)\,\theta\,g_1(h)\,g_2(w\mid h)/v(f(0,I),0)$. Variation in non-labour income $I$ identifies the shape of $v$ in $C$ at each $h$ but not the level across $h$ values. Theorem 2 (negative): $v(C,h)$ is identified only up to an unknown multiplicative function $\delta(h)$, so $\delta(h)$ and $g_1(h)$ are not separately identified. Theorem 3: under wage-hours independence, $g_1(h)$ alone is identified. Theorem 4 (positive): Box-Cox utility plus a regularity condition on the marginal net-of-tax rate restores full identification. Theorem 5 extends identification when wages contain an unobserved individual random effect $\eta$.

## Treatment of preferences
Box-Cox utility in consumption and leisure with a consumption–leisure interaction (eq. 8). Demographic shifters (age, children) enter the leisure parameter. The estimated $\log v(C,h)$ is strictly increasing and concave in both arguments. The framework provides a theoretical rationale for hours dummies in conventional discrete-choice models: what looks like a preference peak at part-time/full-time is reinterpreted as a demand-side opportunity peak in $g_1(h)$.

## Treatment of opportunities / constraints
Opportunities enter as a separate measure $\theta\, g_1(h)\, g_2(w\mid h)$. $\theta$ is estimated below 1 for both genders (interesting market jobs are scarcer than interesting non-market opportunities); $\theta_F$ rises with women's schooling. $g_1(h)$ has a much higher full-time peak for men and a higher part-time peak for women. A counterfactual that removes the part-time peak and reallocates mass to full-time produces a large female shift from part-time to full-time, illustrating an $A$-channel simulation that conventional models cannot perform.

## Welfare / normative object
None. The paper is purely about identification and positive analysis (elasticities, model fit, demand-side simulation).

## Main findings
(i) Without parametric structure, $v(C,h)$ is only identified up to an unknown function of $h$. (ii) For tax/wage simulations the unidentified $\delta(h)$ does not matter. (iii) Model 2 (individual-specific wages) fits the Norwegian data better than Model 1 (job-specific wages). (iv) Female participation elasticity 0.33, male 0.01; female unconditional-hours elasticity 0.62, male –0.02; elasticities decline sharply with the wage level. (v) Removing the part-time hours peak shifts women toward full-time without much male response.

## Main limitations
Cross-sectional data only. Hours are subject to division-bias measurement error that the three-stage estimator does not fully eliminate. Wage–hours independence (Assumption 4) is imposed. No bargaining inside couples. Sector-specific opportunity heterogeneity is ignored. No welfare analysis is attempted, so the welfare implications of the identification result are only conjectural.

## Quick takeaway
The definitive identification reference for RURO models. The result that $v(C,h)$ and $g_1(h)$ are not separately nonparametrically identified means that any opportunity-vs-preference decomposition in this class of models inherits its credibility from its parametric assumptions. For tax/wage counterfactuals the non-identification is irrelevant; for welfare comparisons across individuals choosing different hours it matters directly.

---

<a id="paper-011"></a>

## Ferreira Gignoux 2011

**Source file:** `core_full_notes/Ferreira_Gignoux_2011.md`

---
title: "The Measurement of Inequality of Opportunity: Theory and an Application to Latin America"
authors: [Francisco H. G. Ferreira, Jérémie Gignoux]
year: 2011
outlet: "Review of Income and Wealth, 57(4), 622–657"
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "canonical"
---

## Full citation
Ferreira, F. H. G., & Gignoux, J. (2011). The Measurement of Inequality of Opportunity: Theory and an Application to Latin America. *Review of Income and Wealth*, 57(4), 622–657.

## One-sentence contribution
Formalises a scalar inequality-of-opportunity measure as between-type inequality in a smoothed advantage distribution (types defined by predetermined circumstances), proves it is a lower bound on true opportunity inequality, ties it uniquely to the mean log deviation under path-independent decomposability, and applies the framework to six Latin American countries.

## Core research question
How should inequality of opportunity be measured in theory — both axiomatically and operationally — and what magnitudes does the resulting lower-bound estimate take across six Latin American countries when "opportunities" are defined by predetermined background circumstances?

## Model / framework
A measurement framework, not a behavioural one. The population is partitioned into Roemerian types $T_k$ that are homogeneous in observed circumstances $C$. Equality of opportunity is weakened from equality of conditional advantage *distributions* (Roemer's strong version) to equality of conditional *means* (van de Gaer's ex-ante version). Each individual's advantage $y_i$ is replaced by their type mean $\mu^k$, producing a smoothed distribution; between-type inequality in this smoothed distribution is the opportunity component. Two indices are reported: an absolute version $\theta_a=I(\{\mu^k_i\})$ and a relative version $\theta_r=I(\{\mu^k_i\})/I(y)$. Imposing path-independent decomposability uniquely pins both to the mean log deviation $E_0$. There is no utility function, no labour-supply behaviour, and no explicit feasible-set object.

## Data
Six nationally representative household surveys, restricted to household heads and spouses aged 30–49 with positive income or consumption: Brazil PNAD 1996, Colombia ECV 2003, Ecuador ECV 2006, Guatemala ENCOVI 2000, Panama ENV 2003, Peru ENAHO 2001. Sample sizes range from 4,556 (Panama) to 70,521 (Brazil). Advantage variables: household per capita income and household per capita consumption. Circumstances: parental education, father's occupation, ethnicity/race, region or area of birth, and gender (in labour-earnings specifications).

## Identification logic
No causal identification claim. The decomposition is a between-/within-type partition under the maintained assumption that observed circumstances are exogenous to individual choice. The lower-bound interpretation rests on a circumstance-incompleteness argument: any unobserved circumstance would refine the type partition and weakly increase between-type inequality in the smoothed distribution, so any IEO measure based on observed circumstances is a lower bound on true opportunity inequality.

## Treatment of preferences
None. There is no utility function and no taste heterogeneity. Preference variation is absorbed silently into the within-type residual, which is normatively labelled "ethically acceptable" without behavioural justification.

## Treatment of opportunities / constraints
Opportunities are operationalised as predetermined circumstance types — the Roemer/van-de-Gaer conception. There is no representation of feasible job sets, latent offers, hours restrictions, or local labour-demand variation. A worker with good parental circumstances facing a depressed local market is indistinguishable in the data from a worker with the same circumstances facing a thriving market.

## Welfare / normative object
Inequality indices, not a welfare function. Normative motivation is compensatory: inequalities driven by exogenous circumstances are unfair and should be neutralised; inequalities driven by effort or choice may be acceptable. There is no welfare object that combines bundles, preferences, feasible sets, and tax schedules.

## Main findings
(i) The lower-bound opportunity share $\theta_r$ is large in every country: 0.23–0.34 of total income inequality and 0.25–0.51 of consumption inequality, with Guatemala highest and Colombia lowest. (ii) Non-parametric (cell-mean) and parametric (regression-based) estimators of $\theta_r$ are statistically indistinguishable, supporting the parametric approach in smaller samples. (iii) Family background — parental education and father's occupation — is the most important set of circumstances; ethnicity/race and region/area of birth matter substantially in countries with large indigenous populations. (iv) Opportunity-deprived types are heavily concentrated among ethnic minorities and low-parental-education backgrounds, with stark differences in mean advantage across the worst- and best-off types. (v) The path-independent-decomposability axiom uniquely ties the measure to the mean log deviation $E_0$, providing an axiomatic foundation that other inequality indices cannot match.

## Main limitations
The estimates are lower bounds, and the gap between observed-circumstance IEO and true opportunity inequality is unknown. Opportunities are circumstance types rather than feasible sets — demand-side job availability is invisible. Preferences and effort are not structurally modelled, so the residual cannot be cleanly interpreted as "responsibility." Results are sensitive to the observed circumstance set and to discretisation choices, and international comparability requires coarse coding that loses within-country granularity.

## Quick takeaway
The cleanest theoretical-plus-empirical reference for between-type inequality-of-opportunity measurement, with two enduring contributions: the axiomatic uniqueness of the mean-log-deviation-based opportunity index under path-independent decomposability, and the lower-bound interpretation that disciplines how circumstance-based IEO numbers should be read. Its central limitation — opportunities as observed circumstance types rather than feasible sets — is exactly the gap that a structural RURO opportunity primitive can close, and the smoothed-distribution machinery transfers cleanly to a welfare object $W(z,R,A;y)$ in place of income or consumption.

---

<a id="paper-012"></a>

## Jacquet Jia Thoresen 2026

**Source file:** `core_full_notes/Jacquet_Jia_Thoresen_2026.md`

---
title: "How Much Does Responsibility Matter in Fairness Measurement?"
authors: [Laurence Jacquet, Zhiyang Jia, Thor O. Thoresen]
year: 2026
outlet: "CESifo Working Paper No. 12418"
shelf: "Responsibility / Fairness / Equality of opportunity"
note_type: "canonical"
---

## Full citation
Jacquet, L., Jia, Z., & Thoresen, T. O. (2026). How Much Does Responsibility Matter in Fairness Measurement? *CESifo Working Paper No. 12418*, January 2026.

## One-sentence contribution
Operationalises the responsibility-vs-circumstance distinction within the Dagsvik job-choice (RURO) labour-supply model by constructing a circumstance-only Compensating Variation (CV$^{\text{circ}}$) that holds preferences at a reference value while preserving each household's actual opportunity set, and shows on Norwegian data that the welfare ranking of a major bracket-tax reform is essentially unchanged across the bottom nine deciles but diverges materially at the very top.

## Core research question
How much does it matter empirically whether welfare measurement of a tax reform respects each household's idiosyncratic preferences (a responsibility-respecting standard) or instead neutralises preferences and lets only circumstance-driven variation drive the welfare comparison (a compensation-only standard) — and where in the income distribution does the distinction bite?

## Model / framework
Dagsvik (1994) / Dagsvik & Jia (2016) job-choice model for couples. Utility on a job is $U(C,h_F,h_M,z)=u(C,h_F,h_M)+\varepsilon(z)$ with iid extreme-value taste shocks. Indirect utility decomposes additively: $V=u(f(\cdot),h_F,h_M)+\log Q_F(h_F)+\log Q_M(h_M)+\eta$, with the first term capturing preferences ($R$) and the $\log Q$ terms capturing opportunities ($A$). Female opportunity scale $\log\theta_F=\gamma_{F1}+\gamma_{F2}S$ depends on schooling; male scale normalised to one. Box-Cox systematic utility with 15 parameters. Three welfare objects: standard CV (own preferences, own opportunities), CV$^{\text{circ}}$ (reference preferences $\bar\gamma$ at sample medians, own opportunities, common $\bar\eta$), and the change in Conditional Equality $\Delta CE$ following Fleurbaey (2008).

## Data
Norwegian Labour Force Survey 2015 merged with Income and Wealth Statistics, 1,594 married couples. Tax-benefit calculations via the LOTTE microsimulator. Self-employed, weekly hours above 80, and wages outside NOK [70, 600] excluded. Reform studied: the 2013–2019 Norwegian "bracket tax" episode that replaced the two-tier surtax with a multi-bracket system while generally lowering MTRs.

## Identification logic
Standard RURO identification with the additional structure required for the responsibility cut. Preferences identified from variation in hours conditional on budget constraints; the female opportunity measure $\theta_F$ identified from the residual hours variation, parametrised through education; male $\theta_M$ normalised. The separation of $R$ from $A$ relies on the additive indirect-utility decomposition. CV is computed for each household using its own estimated preferences; CV$^{\text{circ}}$ is computed using $\bar\gamma$ — the difference is then interpretable as the welfare contribution of preference heterogeneity holding circumstances fixed.

## Treatment of preferences
Preferences are treated as responsibility characteristics following Kaplow (2008) and Lockwood & Weinzierl (2015) — tastes, not needs. Rich observed heterogeneity through age (log and squared), number of children below/above 6, gender, plus a spousal leisure interaction. The error $\varepsilon(z)$ is interpreted as preference heterogeneity (the paper notes Roemer & Trannoy 2016's caveat that this is itself contestable).

## Treatment of opportunities / constraints
Opportunities are an explicit primitive. The latent job set $B(h)$ has $Q(h)$ jobs at each hours level; the total market opportunity scale $\theta=\sum_{h>0}Q(h)$ contrasts market against non-market alternatives. The female scale depends on education; the hours density $g(h)$ has peaks at full-time and part-time. CV$^{\text{circ}}$ keeps these intact while neutralising preferences — so the metric measures welfare-given-the-opportunity-set, exactly the responsibility-sensitive object the fairness literature requires.

## Welfare / normative object
Three measures. (i) Standard CV — money-metric utility, preserves own preferences and circumstances. (ii) CV$^{\text{circ}}$ — preferences set to $\bar\gamma$, circumstances kept; isolates circumstance-driven welfare variation. (iii) $\Delta CE$ — Fleurbaey (2008) Conditional Equality, evaluated on a hypothetical equivalent linear budget at reference preferences. CV and CV$^{\text{circ}}$ are computed by McFadden (1999) simulation with $K$ Gumbel draws per household.

## Main findings
(i) Average reform welfare effects are similar under CV (NOK 18,384) and CV$^{\text{circ}}$ (NOK 18,677); CV$^{\text{circ}}$ is slightly less dispersed. (ii) Across deciles 1–9 the two measures track closely — the reform is welfare-improving for the vast majority of Norwegian couples regardless of which standard is applied. (iii) At decile 10 the gap opens: CV$^{\text{circ}}$ records larger gains than CV, because high-income women have stronger leisure preferences that are neutralised under CV$^{\text{circ}}$. (iv) 71–93% of households remain in the same quintile when ranked by CV vs CV$^{\text{circ}}$. (v) $\Delta CE$ and CV$^{\text{circ}}$ deliver the same distributional pattern, confirming the responsibility-sensitive metrics are empirically aligned with one another.

## Main limitations
The opportunity measure is parametrised through education only (and normalised for men), so any cross-individual variation in opportunities not captured by schooling is silently booked as preferences. The $\bar\gamma$ choice (sample medians) is one defensible reference but could materially affect CV$^{\text{circ}}$. The error term $\varepsilon(z)$ is classified as a preference component but could equally be read as a circumstance under different normative axioms. The exercise is a two-way comparison rather than a full Shapley decomposition. Single cross-section, single country, single reform — the headline "responsibility matters mostly at the top" claim is conditional on all three.

## Quick takeaway
The closest existing implementation of a $W(z,R,A;y)$ welfare exercise within a structural RURO model. Its central methodological move — substitute reference preferences while keeping actual opportunities to construct CV$^{\text{circ}}$ — is the canonical responsibility-sensitive analogue of Bargain et al. (2013)'s preference-respecting Fleurbaey metrics, and its empirical headline (responsibility binds mostly at the top of the income distribution in Norway) is the benchmark any cross-country extension will need to engage with.

---

<a id="paper-013"></a>

## Shorrocks 2013

**Source file:** `core_full_notes/Shorrocks_2013.md`

---
title: "Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value"
authors: [Anthony F. Shorrocks]
year: 2013
outlet: "Journal of Economic Inequality, 11, 99–126"
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "canonical"
---

## Full citation
Shorrocks, A. F. (2013). Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value. *Journal of Economic Inequality*, 11, 99–126.

## One-sentence contribution
Establishes that the Shapley value — assigning to each factor its average marginal contribution across all elimination orders — provides an exact, symmetric, order-independent additive decomposition rule that unifies the patchwork of poverty- and inequality-decomposition formulas in the prior literature, and extends naturally to grouped factors via the Owen value.

## Core research question
How should one decompose a distributional indicator $I=f(X_1,\ldots,X_m)$ into additive contributions from each factor in a way that is exact (contributions sum to the total), symmetric across factors, free of arbitrary residual or interaction terms, and applicable when the underlying function $f$ is nonlinear?

## Model / framework
For an indicator $I=f(X_1,\ldots,X_m)$, define the subset-value function $F(S)$ as the value of $I$ when only factors in $S$ are "active" (with $F(\varnothing)=0$ as a normalisation). The Shapley contribution of factor $k$ is the weighted average over all subsets $S\subseteq K\setminus\{k\}$ of the marginal effect $\Delta_k F(S)=F(S\cup\{k\})-F(S)$, with weights $\pi(|S|,|K\setminus\{k\}|)=(m-|S|-1)!|S|!/m!$. The decomposition satisfies (i) exact additivity, (ii) symmetry / order invariance, (iii) null-effect normalisation (a factor that never moves $f$ gets contribution zero), and (iv) linearity of the attribution operator. The hierarchical Owen extension treats grouped factors as primary players in a two-stage decomposition (between groups, then within groups), with consistency conditions identified in the paper.

## Data
None — the paper is purely methodological.

## Identification logic
Not an identification paper. The Shapley rule is an attribution rule once the analyst has defined the factor list, the counterfactuals that "remove" each factor, and the indicator $I$. Identification of the factors themselves is upstream of the decomposition.

## Treatment of preferences
None modelled. Preferences enter only if an analyst defines them as a factor in $f$ upstream.

## Treatment of opportunities / constraints
None modelled. Opportunities enter only if an analyst defines them as a factor.

## Welfare / normative object
None directly. The decomposition rule is normatively neutral about the choice of indicator: it can decompose poverty headcounts, Gini coefficients, mean log deviations, or any other aggregate distributional statistic the analyst supplies.

## Main findings
(i) The Shapley rule reproduces conventional decompositions in benchmark cases — e.g., the Datt-Ravallion growth-vs-redistribution decomposition without the residual term, and Shorrocks's own (1982) MLD subgroup decomposition. (ii) For Gini and other non-decomposable indices, the Shapley rule supplies an exact additive split where ad hoc rules previously left a residual. (iii) For source decomposition of inequality the Shapley split coincides with the natural variance-of-source decomposition for the variance, and provides a defensible analogue for other indices. (iv) The Owen extension handles grouped factors consistently under stated regularity conditions.

## Main limitations
The paper supplies a rule, not a model. Its outputs depend entirely on the analyst's choice of factor list and on the counterfactual definition that "removes" each factor — choices that are economic and normative, not mechanical. Causal interpretation requires those upstream choices to be defensible. The rule does not tell the analyst what should count as a primary vs secondary factor, nor whether a given indicator $I$ is the right normative summary statistic.

## Quick takeaway
The methodological reference for any decomposition exercise that needs an exact, symmetric, residual-free additive split into factor contributions in a nonlinear setting. The substantive economic and normative work — defining factors, defining their null counterfactuals, choosing $I$ — is upstream of the rule itself, and the credibility of any Shapley decomposition lives or dies on those upstream choices.
