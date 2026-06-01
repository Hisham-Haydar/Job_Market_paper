# Full Core JMP Notes

Short prefatory note:
- generated from markdown files in `core_jmp_notes`
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

**Source file:** `core_jmp_notes/Aaberge_Colombino_2018.md`

---
title: "Structural Labour Supply Models and Microsimulation"
authors: [Rolf Aaberge, Ugo Colombino]
year: 2018
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the methodological survey that defines the playing field my JMP enters. It sets out the canonical RURO + microsimulation pipeline I am implementing for France 2016, and — crucially — it identifies the unresolved welfare-evaluation tension my JMP is designed to resolve: common utility (interpersonally comparable but ignores preference heterogeneity) vs Fleurbaey preference-respecting (respects heterogeneity but indexing-dilemma). Whenever I want to motivate why my $W(z,R,A;y)$ framework is needed rather than just one more application of an existing welfare metric, this is the paper I cite as the official statement of the open problem.

## What it tells me about opportunities vs preferences
The paper gives the cleanest written articulation of why the RURO is the right vehicle for an opportunity-vs-preference decomposition: the structural interpretation of the dummy coefficients ($\gamma_0=\ln J+A_0$, $\gamma_\ell=\ln(J_\ell/J)+A_\ell$) means the opportunity block is policy-invariant in a way that the DC dummies are not. It also gives me the Colombino (2013) iterative-equilibrium argument I will need when a referee asks whether my opportunity counterfactuals are partial-equilibrium artefacts — the framework supports endogenous reshaping of $p(w,h)$ in response to large reforms.

## What it tells me about welfare measurement
The key passage for me is the explicit acknowledgment that the common utility function $V(y,h)$ "by definition contains interpersonal comparability of both welfare levels and welfare differences" — meaning it achieves comparability by assumption, not by argument. That is exactly the methodological move I want to avoid. The paper's honest "no clear winner" between common utility and Fleurbaey is the gap my framework targets: I want a welfare object that is interpersonally comparable in the same way King (1983) equivalent income is, but conditions on the opportunity set so that "comparability" is not a euphemism for "ignoring $A$".

## What it tells me about decomposition
The paper does not implement decomposition exercises directly, but it surveys the rank-dependent SWF family (Weymark/Yaari) which is the natural target for any inequality decomposition I want to do. It also flags the Norwegian elasticity-decline result over 1979–2011 as a potential decomposition target — a useful analogue: that decline can be re-read as an opportunity-set expansion (the female extensive margin saturated), which is exactly the kind of $A$-channel attribution my Shapley exercise is designed to make quantitatively.

## What it tells me about empirical design
Five concrete lessons. (i) Adopt the McFadden (1978)/Ben-Akiva-Lerman (1985) importance sampling for the alternatives — it is the standard. (ii) Specify $p(w,h)=p_1 g_1(h)g_2(w)$ explicitly rather than via dummies, to keep the opportunity primitive visible for downstream welfare. (iii) Take an explicit stance on the $\varepsilon$ interpretation (RUM vs optimisation error) since it determines whether $\varepsilon$ enters welfare. (iv) For the optimal-tax extension, follow the iterative microsimulation approach of equation (16) rather than analytical Mirrlees. (v) When elasticities are reported, distinguish between extensive/intensive and historical/current to allow comparison with the Norwegian time series.

## How I may cite it in the paper
As the canonical methodological survey of the entire structural-labour-supply + microsimulation + social-welfare-evaluation pipeline. Likely citations: in the introduction as the statement of the unresolved welfare-evaluation tension; in the model section as the source of the unified DC/RURO formalism; in the welfare-framework section as the source of the common-utility-vs-Fleurbaey contrast my framework navigates; and in the optimal-tax / extension section as the methodological reference for any computational optimum-tax exercise built on top of the welfare layer.

## What limitation of this paper my JMP may address
The paper presents the common utility function and the Fleurbaey preference-respecting approach as a stark binary and concludes there is no clear winner. My JMP introduces a third option — the $W(z,R,A;y)$ framework — that conditions welfare on both preferences and opportunities, using the responsibility cut to decide which preference differences the social planner should respect and the opportunity primitive to decide which differences should be compensated. This dissolves the binary the paper leaves open and gives a constructive welfare object that is interpersonally comparable without assuming preferences are homogeneous.

---

<a id="paper-002"></a>

## Aaberge Colombino Strom 1999

**Source file:** `core_jmp_notes/Aaberge_Colombino_Strom_1999.md`

---
title: "Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints"
authors: [Rolf Aaberge, Ugo Colombino, Steinar Strøm]
year: 1999
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the canonical demonstration that the RURO/latent-jobs machinery survives translation to a high-unemployment European labour market — exactly the setting my France 2016 prototype lives in. It is the closest historical analogue to my exercise: couples, non-convex tax-benefit budget set, identification of an opportunity scale parameter, regional heterogeneity in opportunities, and a tax-reform simulation grounded in the estimated structural model. The methodological choices the authors had to make in 1999 are essentially the choices I am making for France in 2026.

## What it tells me about opportunities vs preferences
The paper operationalises my $W(z,R,A;y)$ split in a clean way: $v(C,h)$ is the preferences block, $g_0$ and $g(h,w)$ are the opportunity block, and the structural unemployment equation $\rho=(1-g_0)\varphi(0,0)$ gives a quantitative measure of how much of observed non-participation is opportunity-driven rather than preference-driven. This is exactly the kind of decomposition I want for France, with regional/educational variation in $g_0$ playing the role that the North/South cut plays here.

## What it tells me about welfare measurement
The paper does not compute a welfare object — it stops at the disposable-income Gini for the policy comparison. That is the gap my JMP fills. But the comparison of three revenue-neutral tax regimes is a useful template: report distributional outcomes under several explicit counterfactuals and let the welfare measure aggregate them. The authors' finding that the flat tax raises the Gini while leaving aggregate labour supply nearly unchanged previews the Bargain et al. (2013) money-metric exercise I will lean on more heavily.

## What it tells me about decomposition
The North/South $g_0$ gap is a worked example of a circumstance-driven opportunity wedge — and it is large enough (significant Northern coefficient, $t=6.5$ for women) to drive a material slice of any opportunity-vs-preference decomposition. For my France pipeline, this validates building the opportunity Shapley component on geographic + education cells rather than relying solely on demographic shifters inside $v$. The cross-spouse elasticity finding (own-wage effects are largely neutralised by cross-effects) also warns me that any decomposition done at the individual rather than household level will mis-attribute income variation.

## What it tells me about empirical design
Five concrete lessons. (i) Estimate $g_0$ jointly with preferences and discipline it with the unemployment rate — do not normalise it away. (ii) Allow the marginal utility of consumption to differ by employment status when the country has a meaningful informal sector (relevant for some EU robustness checks). (iii) Use a uniform hours density with peaks rather than a fully flexible $g(h)$ — identification is fragile. (iv) Estimate spouses jointly; cross-effects are first-order and a unitary household objective is a defensible default. (v) Run the Hausman comparison as a robustness exercise — the 60% gap in female hours elasticity is a citable benchmark for the size of the bias my framework corrects.

## How I may cite it in the paper
As the empirical workhorse of the RURO literature alongside Aaberge & Colombino (2018) and Aaberge, Colombino & Wennemo (2009). Likely citations: in the model section as the canonical couples extension of Dagsvik (1994); in the empirical-design section as the precedent for identifying an opportunity scale parameter from unemployment data; in the decomposition section as the precedent for region-conditioned opportunity heterogeneity; and in the elasticity-discussion section as the reference for the Hausman-vs-RURO bias.

## What limitation of this paper my JMP may address
Three. (i) No welfare measurement — my JMP layers a money-metric welfare object on the same structural primitives. (ii) The opportunity decomposition is ad hoc (North/South + local unemployment ratio) rather than a formal Shapley-Shorrocks split — my JMP delivers an order-independent decomposition of welfare inequality. (iii) The paper does not engage with the responsibility cut between $R$ and $A$, treating the gender gap in elasticities as a pure modelling output rather than a normative object — my JMP makes that responsibility cut explicit and reports the welfare-inequality consequence of choosing it differently.

---

<a id="paper-003"></a>

## Aaberge Colombino Wennemo 2009

**Source file:** `core_jmp_notes/Aaberge_Colombino_Wennemo_2009.md`

---
title: "Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply"
authors: [Rolf Aaberge, Ugo Colombino, Tom Wennemo]
year: 2009
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the empirical case for not running my JMP on a stripped-down Van Soest specification. The headline finding — that prediction errors under a flat-tax counterfactual run 30–55% in models without opportunity dummies and collapse to under 5% with the right dummies — is exactly the kind of evidence I need to defend the structural cost of my approach. It also validates the specific design choice in my France pipeline: 24 (or thereabouts) sampled wage-vigintile × hours alternatives plus opportunity features, rather than a sparse fixed grid.

## What it tells me about opportunities vs preferences
The paper provides a striking asymmetric identification result: preferences are recoverable from in-sample data under almost any choice-set design, but opportunities are not. That maps directly onto my $W(z,R,A;y)$ framework — it implies that the $A$-block in my decomposition is the empirically fragile piece and demands the strongest specification discipline. It also makes a concrete suggestion: the job-availability dummy approximates $\log p^0$ and the peaks dummies approximate $g_1(h)$, so my opportunity block can be parametrised parsimoniously rather than fully nonparametrically.

## What it tells me about welfare measurement
The paper does not compute welfare, but its negative result transfers directly. If a model mis-predicts the post-reform hours distribution by 30–55%, then any money-metric welfare object built on that model will misallocate utility across constrained vs voluntary outcomes by a similar order of magnitude. So the cost of choice-set misspecification is not a second-order econometric inconvenience for me — it is first-order for the welfare numbers my JMP reports. This is the strongest existing argument for why a welfare-and-opportunity decomposition cannot be done credibly inside a conventional Van Soest model.

## What it tells me about decomposition
Two implications. (i) The preference-vs-opportunity Shapley split I want to compute is asymmetric in identification: the opportunity share is the harder one to nail down empirically, so its sensitivity to specification is what I should stress-test. (ii) The "interaction of more alternatives with the job dummy" matters more than either alone, which suggests I should not skimp on either margin in my France implementation — sparse alternatives + opportunity dummies, or rich alternatives without dummies, both fail.

## What it tells me about empirical design
Five concrete lessons for the France 2016 pipeline. (i) Use sampled rather than fixed alternatives. (ii) Aim for ~24 alternatives per agent rather than the 6–8 typical of Van Soest applications. (iii) Include a job/participation dummy AND hours-peak dummies. (iv) Do not over-trust in-sample fit as a model-selection criterion — report out-of-sample policy-prediction stability. (v) Run a Monte-Carlo robustness exercise from my own estimated model and report how the welfare decomposition shifts under leaner specifications.

## How I may cite it in the paper
As the methodological backstop for my choice-set design. Likely citations: in the empirical-implementation section as the reference for the sampled-alternatives + dummies specification; in the robustness section as the precedent for Monte-Carlo evaluation of choice-set sensitivity; and in the limitations section as the source of the warning that opportunity-block identification is fragile and depends on the maintained parametric form.

## What limitation of this paper my JMP may address
The paper is purely about labour-supply prediction, not welfare — its central claim about opportunities mattering for policy is asserted but never quantified in welfare units. My JMP closes that gap: I take the paper's "use the dummies" prescription, build an opportunity-aware model, and translate the resulting predictions into a money-metric welfare-inequality decomposition. The Monte-Carlo design also gives me a template for the robustness exercise that the paper itself does not cross to welfare measurement.

---

<a id="paper-004"></a>

## Bargain et al 2013

**Source file:** `core_jmp_notes/Bargain_et_al_2013.md`

---
title: "Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US"
authors: [Olivier Bargain, André Decoster, Mathias Dolls, Dirk Neumann, Andreas Peichl, Sebastian Siegloch]
year: 2013
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the empirical template for the welfare layer I am putting on top of my France 2016 RURO model. It defines the menu of preference-respecting money-metric welfare measures (rent, wage, rent + reference wage), shows that the choice among them has first-order consequences for rankings, and runs the harmonised microsimulation pipeline whose downstream version I am building. It is also the cleanest illustration of the central problem my JMP is designed to solve: that without an explicit opportunity primitive, "preferences" silently absorb opportunities and welfare rankings cannot tell the two apart.

## What it tells me about opportunities vs preferences
The paper makes the silent-conflation problem concrete. It explicitly acknowledges (p. 814–815) that country-specific preference parameters likely embed country-specific opportunity constraints — childcare, part-time availability, institutions — and concedes the framework cannot resolve which is which. This is exactly the gap my RURO-based France implementation closes. The paper also gives me a numeric anchor for how large the unresolved opportunity content might be: country-specific "preferences" account for ~85% of cross-country reranking, an upper bound on what a richer opportunity model could relabel as $A$.

## What it tells me about welfare measurement
Three direct lessons. (i) Use the $v^{RW}$ family rather than collapsing to either extreme — varying $w^r$ across p25/p50/p75 of the wage distribution is a clean way to display the responsibility-spectrum without taking a stand. (ii) Computing welfare metrics by expectation over taste draws is preferable to evaluating at point estimates. (iii) Robustness to Box-Cox vs quadratic utility is high in their data, which suggests the welfare layer is reasonably insensitive to the specific functional form of $v(C,h)$ — a useful prior for the parametric-form sensitivity I will need to report given the Dagsvik & Jia (2016) non-identification result.

## What it tells me about decomposition
The paper's Section 5.3 decomposition (counterfactually swapping demographics vs preference parameters across countries) is a methodological precursor to the Shapley-Shorrocks decomposition I want to do. It shows exactly the kind of additive split between two channels that Shapley generalises with order-independence. The paper's finding that demographics contribute almost nothing relative to deep parameters is the result that I will need to qualify by introducing a third (opportunity) channel.

## What it tells me about empirical design
Three lessons for the France pipeline. (i) Restrict the sample to a comparable demographic core (married women) for the headline results, then expand. (ii) Use a discrete grid of seven hours categories at minimum. (iii) Estimate country-specific preference parameters rather than imposing pooled coefficients — the cross-country MRS spread of ~5× is too large to absorb into demographic shifters. For me this translates to letting French preference parameters vary across regions and education cells rather than imposing a single parameter vector.

## How I may cite it in the paper
As the canonical empirical implementation of the Fleurbaey welfare metrics. Likely citations: in the welfare-framework section as the source of the $v^W$, $v^{RW}$, $v^R$ definitions; in the literature section as the leading demonstration that the metric choice changes welfare rankings; in the limitations section as the precursor that explicitly acknowledged the missing opportunity block; and in the discussion section as the natural cross-country comparator if I extend the France pipeline to a multi-country exercise.

## What limitation of this paper my JMP may address
The most important one. The paper computes preference-respecting welfare metrics on a model that does not separate preferences from opportunities, so the resulting cross-country reranking is necessarily contaminated. My JMP layers the same Fleurbaey welfare machinery on top of a RURO model where $R$ and $A$ are separately identified (modulo the parametric resolution from Dagsvik & Jia 2016), so the welfare-inequality decomposition can attribute shares to opportunities rather than booking them silently as preferences. The paper's own decomposition can be read as an upper bound on the opportunity share that my JMP makes visible.

---

<a id="paper-005"></a>

## Beffy et al 2019

**Source file:** `core_jmp_notes/Beffy_et_al_2019.md`

---
title: "Labour Supply and Taxation with Restricted Choices"
authors: [Magali Beffy, Richard Blundell, Antoine Bozio, Guy Laroque, Maxime Tô]
year: 2019
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the strongest existing identification result for separating preferences from opportunities in a discrete-choice labour-supply model — and it does so without invoking the full RURO machinery I use, which makes it an essential robustness reference. The headline empirical finding (offer restrictions halve elasticities for UK mothers) is the most compelling outside-the-RURO evidence that the $A$ block in $W(z,R,A;y)$ is empirically first-order, not just theoretically interesting. If a referee prefers a less structural approach, this is the model they will compare mine against.

## What it tells me about opportunities vs preferences
Three things. First, the dominated-region argument is a clever non-RURO way to identify the opportunity block — variation in how the budget constraint is shaped serves as the exclusion restriction that variation in non-labour income serves in Dagsvik & Jia (2016). Second, the comparison of constrained vs unconstrained hours (26.2 vs 35.5) gives a clean numeric anchor for the size of the opportunity wedge — a useful benchmark for what "opportunity-equalised" hours might look like in my France counterfactual. Third, it shows that the opportunity block has observable correlates (education raises full-time offers), validating my plan to condition $g(h)$ on education.

## What it tells me about welfare measurement
The paper does not implement welfare, but it sketches exactly the welfare object I want: the money-metric gap between realised constrained utility and the unconstrained optimum. The fact that the women who fail the unrestricted-choice test are systematically poorer, lone, and lower-wage tells me the welfare cost of opportunity restrictions is correlated with circumstances — i.e., the opportunity-share contribution to welfare inequality is sign-predictable. This is a useful prior to bring to the France decomposition.

## What it tells me about decomposition
The 2× elasticity gap between unrestricted and two-offer specifications has a direct decomposition implication: roughly half of what naïve discrete-choice models book as a "preference response" to taxes is actually opportunity-driven. So in any tax-reform welfare decomposition, the preference share is overstated by something on the order of 50% if I use a Van-Soest-style model. That is the magnitude of the misclassification my JMP needs to correct.

## What it tells me about empirical design
Four lessons. (i) Use the budget-constraint dominated set as a diagnostic — flag observations in dominated regions and report the share. (ii) Allow opportunity-distribution covariates (education, household type, region) in $g(h)$ from the start — the paper finds these matter. (iii) Discipline the offer distribution with a parsimonious mixture rather than a fully nonparametric form. (iv) Estimate jointly with consumption and wage equations rather than sequentially — the control-function approach handles wage endogeneity cleanly.

## How I may cite it in the paper
As the leading non-RURO identification result for restricted-choice labour supply. Likely citations: in the framework section to motivate the opportunity primitive; in the identification section as a complementary identification source (budget non-linearities) to my own (functional-form-based identification of $v(C,h)\cdot g(h)$); in the empirical section as the benchmark for the magnitude of the elasticity bias from ignoring opportunities; and in the limitations section to acknowledge that my opportunity primitive carries wage information that theirs does not.

## What limitation of this paper my JMP may address
Three. (i) The two-offer restriction is arbitrary; my RURO opportunity scale $\theta$ implicitly estimates the effective number of offers. (ii) Their offer distribution is over hours only; mine is over (hours, wage) pairs, which matters for any welfare object that weights both income and time. (iii) They produce no welfare object despite the framework being well-designed for one — my JMP delivers exactly that object and a Shapley-Shorrocks decomposition built on top of it.

---

<a id="paper-006"></a>

## Bhattacharya 2015

**Source file:** `core_jmp_notes/Bhattacharya_2015.md`

---
title: "Nonparametric Welfare Analysis for Discrete Choice"
authors: [Debopam Bhattacharya]
year: 2015
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the theoretical benchmark against which my parametric welfare layer needs to be honest. Bhattacharya proves that money-metric welfare is nonparametrically identified in unordered discrete choice but NOT in ordered discrete choice — exactly the dividing line between the RURO framework I use (jobs are unordered alternatives, each with its own (h,w) package) and the conventional ordered-hours Van Soest framework. So this paper gives me a clean theoretical reason to prefer my modelling choice on welfare-identification grounds, independent of the labour-supply prediction reasons in Aaberge, Colombino & Wennemo (2009).

## What it tells me about opportunities vs preferences
The paper itself does not engage with the $R$-vs-$A$ split — all welfare variation in its setup arises from preference heterogeneity. But the asymmetry it documents (unordered identifies, ordered does not) is the welfare-side analogue of the asymmetry Beffy et al. (2019) document on the labour-supply side. Both point to the same lesson: the empirical content of $A$ is exposed only when the choice set is allowed to be non-trivial. For my decomposition, that means the parametric resolution of the Dagsvik & Jia (2016) non-identification ($\delta(h)$) is the binding constraint on welfare identification, not the lack of nonparametric tools.

## What it tells me about welfare measurement
Three things. (i) Use the FULL distribution of EV/CV, not just the mean — the closed-form CDF makes this almost free. (ii) The mean-EV-equals-Marshallian-consumer-surplus result generalises beyond quasilinear utility, so I can compute aggregate welfare effects of tax counterfactuals from choice probabilities directly without needing to integrate utility differences. (iii) For my France pipeline I should report welfare CDFs (e.g., quantiles of EV by education or region), not just means — this exploits the paper's strongest result and gives the welfare-inequality decomposition more empirical content.

## What it tells me about decomposition
Indirectly important. The paper shows that the full welfare distribution is identified, which means quantile-based decompositions and inequality functionals (Gini of EV, Atkinson of EV) are well-defined objects. So my Shapley decomposition can in principle be done not just on aggregate welfare but on welfare inequality at every quantile of the distribution. That is a richer decomposition target than the income-quantile decompositions that Bourguignon-Ferreira-Menéndez and Ferreira-Gignoux deploy in the inequality-of-opportunity literature.

## What it tells me about empirical design
Two lessons. (i) When estimating choice probabilities for the welfare layer, use a flexible enough specification (e.g., mixed logit at the household level) so the welfare CDF inherits the flexibility, even if the underlying RURO has parametric structure for identification. (ii) Treat the wage variation across (h,w) job packages as the "price variation" Bhattacharya needs — this is what places my model in the unordered-multinomial case and lets me cite his identification result.

## How I may cite it in the paper
As the theoretical benchmark for welfare identification in discrete choice. Likely citations: in the welfare-framework section to motivate why a money-metric approach is well-defined for my model class; in the methods section as the source of the closed-form CDF representation if I report welfare distributions; and in the discussion section as the result that distinguishes the RURO welfare layer from a Van-Soest-with-ordered-hours welfare layer at the level of identification.

## What limitation of this paper my JMP may address
The most important one for me is that Bhattacharya assumes free choice — no demand-side restrictions, no opportunity heterogeneity. My JMP layers welfare measurement on top of a model that treats opportunities as a primitive, so the welfare object I compute is welfare-given-the-opportunity-set, which is the empirically relevant quantity in a constrained labour market. The paper sketches this gap explicitly but does not fill it; a RURO-based welfare analysis is the natural way to extend Bhattacharya's nonparametric machinery to environments where the choice set itself varies across individuals.

---

<a id="paper-007"></a>

## Bourguignon Ferreira Menendez 2007

**Source file:** `core_jmp_notes/Bourguignon_Ferreira_Menendez_2007.md`

---
title: "Inequality of Opportunity in Brazil"
authors: [François Bourguignon, Francisco H. G. Ferreira, Marta Menéndez]
year: 2007
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the empirical-style template for the inequality-of-opportunity literature my decomposition exercise plugs into, and the cleanest example of how *not* to measure opportunities for my purposes. The paper proxies opportunities with observed background variables (race, parental education, region of birth) — exactly the reduced-form approach my structural RURO framework supersedes by modelling opportunities as actual feasible job sets. So this paper is at once the literature my decomposition speaks to and the limitation my framework addresses.

## What it tells me about opportunities vs preferences
The paper makes the conceptual cut between circumstances (compensable) and effort (not compensable) but does not separate effort from preferences — the residual mixes them indistinguishably. This is the silent-conflation problem on the inequality-of-opportunity side, mirroring the same problem in Bargain et al. (2013) on the welfare-measurement side. My JMP fills both gaps simultaneously: structural preferences from RURO, structural opportunities from the opportunity density, and the residual much smaller because both are explicitly modelled.

## What it tells me about welfare measurement
None directly — the paper decomposes earnings inequality, not welfare inequality. But the methodological lesson transfers: any welfare object I decompose should also be decomposed by an *equalisation* counterfactual rather than a regression-coefficient interpretation. The Bourguignon-Ferreira-Menéndez "compute inequality on the equalised-circumstance counterfactual distribution" approach is exactly what the Shapley rule generalises when extended to multiple factors.

## What it tells me about decomposition
Three lessons. (i) The direct/indirect-effect decomposition (60% of circumstance effect operates directly on wages, 40% through effort proxies) is a useful conceptual template — my structural decomposition should distinguish opportunity effects that operate *through* labour-supply choices (extensive margin) from those that operate directly on the wage given the choice (intensive margin). (ii) Reporting bounds rather than point estimates via Monte Carlo over admissible coefficient configurations is a defensible identification strategy when instruments are absent — useful for my parametric-form sensitivity analysis. (iii) The 23% headline number for circumstance share is a benchmark to compare against my opportunity-share number for France; if mine is much higher, that is itself informative about how much the structural opportunity primitive captures that circumstance proxies miss.

## What it tells me about empirical design
Two practical lessons. (i) Be explicit about which observed variables are circumstances and which are responsibility variables — the line is normative and the paper is admirably transparent that schooling-as-effort is contestable. (ii) Run the decomposition cohort by cohort (or in my case, region/education cell by cell) to expose heterogeneity in the opportunity share rather than collapse to a single national number — the cohort-by-cohort tabulation is one of the paper's most informative outputs.

## How I may cite it in the paper
As the canonical empirical reference for circumstance-based inequality-of-opportunity decomposition. Likely citations: in the literature section as the leading reduced-form approach to opportunity inequality; in the methodological section as the precedent for the equalised-counterfactual decomposition strategy; in the discussion as the comparator number for the share of inequality attributable to opportunities; and in the limitations section as the precursor whose conflation of effort with preferences my framework dissolves.

## What limitation of this paper my JMP may address
The most important one. The paper proxies opportunities with observable background characteristics and bundles preferences indistinguishably into the residual. My JMP replaces the proxy with a structural opportunity primitive (RURO $g(h,w)$ and $\theta$) and the residual with structural preferences from the same model. The result is a decomposition that attributes inequality not just to "circumstances vs effort" but to the four economically meaningful primitives — preferences, opportunities, wages, and non-labour income — within a unified Shapley-Shorrocks framework. This is a substantive advance: where the paper can attribute 23% to "circumstances", my JMP can attribute that share more finely and defensibly across the channels economic theory actually identifies.

---

<a id="paper-008"></a>

## Capeau et al 2021

**Source file:** `core_jmp_notes/Capeau_et_al_2021.md`

---
title: "Nonparametric Welfare Analysis for Discrete Choice: Levels and Differences of Individual and Social Welfare"
authors: [Bart Capéau, Liebrecht De Sadeleer, Sebastiaan Maes, André Decoster]
year: 2021
shelf: "Welfare measurement / Equivalent income / Money-metric"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the paper that makes Fleurbaey welfare *levels* — not just differences — operational from choice probabilities. My JMP needs welfare levels to do an inequality decomposition (rank individuals on a money-metric scale and decompose the inequality of those levels), and Capéau et al. give the cleanest existing identification machinery for that object. It is also the natural generalisation of Bhattacharya (2015) and the natural complement to Bargain et al. (2013): it tells me which parts of my parametric welfare layer are identification-essential and which are just functional-form convenience.

## What it tells me about opportunities vs preferences
The paper deliberately attributes all choice variation to preferences and bypasses opportunities entirely — its NOS sets are normative virtual objects, not actual constraints. This is exactly the gap my JMP fills. But the empirical finding that lower wage quartiles are intermingled in welfare-level dominance ranks (i.e., unobserved preferences move welfare levels meaningfully) sets an important upper bound on how far an opportunity-side decomposition can push: if preferences genuinely carry this much within-wage-group welfare-level dispersion, the opportunity share will not be the whole story.

## What it tells me about welfare measurement
Three direct lessons. (i) Use the joint distribution of welfare levels and CV — the "who gains where on the baseline distribution" object is exactly the policy-evaluation table I want for any French reform counterfactual, and Theorem 4 gives the closed form. (ii) The MMU-equals-income result for ~25% of the sample is a useful deterministic check — anyone whose actual reference prices match the chosen reference prices has a known welfare level, which is a sanity test for my pipeline. (iii) Use NOS measures more general than MMU; the Pazner ray and equivalent-income variants are also identified and may be normatively preferable for the responsibility-sensitive cut my JMP cares about.

## What it tells me about decomposition
The SWF representation (Proposition 2) gives me a formal route to decompose differences in social welfare across counterfactuals into integrals of differences in choice probabilities. This is the analytic counterpart of the Shapley decomposition I want to do at the inequality level: I can write any SWF change as a sum of "choice-probability differences at virtual prices" and partition those by the source of the policy change. The paper itself does not Shapley-decompose, but it provides the additive structure that makes a Shapley exercise on top of it well-defined.

## What it tells me about empirical design
Five lessons. (i) Estimate choice probabilities semiparametrically with shape restrictions (own-price decreasing, cross-price increasing) — this is robust without being arbitrary. (ii) When only cross-sectional data are available, use Boole-Fréchet bounds for transition probabilities and report intervals rather than point estimates for joint-distribution objects. (iii) Take reference prices for MMU at sample medians of price differentials — defensible and replicable. (iv) Report welfare levels by wage-quartile and by chosen alternative, as in Figure 5–6 — a clear way to display the heterogeneity. (v) Run the deterministic-welfare check (Corollary 2): the share of the sample with $MMU=y$ is a hard accuracy benchmark for the estimated choice probabilities.

## How I may cite it in the paper
As the welfare-identification reference for NOS measures and as the methodological route from choice probabilities to welfare distributions. Likely citations: in the welfare-framework section as the source of the NOS welfare-level definition; in the methods section for the closed-form CDF representations of welfare levels and CV; in the empirical section as the precedent for the joint level-difference reform analysis; and in the limitations section as the precursor that flagged but did not address opportunity heterogeneity in the choice set.

## What limitation of this paper my JMP may address
The most important one is the assumption of a common, exogenous choice set — the paper attributes all choice variation to preferences and treats $\{NW,PT,FT\}$ as freely available to all single females. My JMP layers the same NOS welfare machinery on a RURO model where the opportunity set varies across individuals via $\theta$ and $g(h)$, so the welfare levels I identify reflect the realised opportunity constraint rather than a counterfactual unrestricted choice. This means the welfare-inequality decomposition I produce can attribute shares to opportunities, while Capéau et al.'s framework would book the same variation as preferences. The cross-sectional-only setting (bounds rather than point identification of joint distributions) is an additional limitation my single-cross-section France pipeline shares — I should adopt their Boole-Fréchet bounding strategy directly.

---

<a id="paper-009"></a>

## Dagsvik et al 2014

**Source file:** `core_jmp_notes/Dagsvik_et_al_2014.md`

---
title: "Theoretical and Practical Arguments for Modeling Labor Supply as a Choice Among Latent Jobs"
authors: [John K. Dagsvik, Zhiyang Jia, Tom Kornstad, Thor O. Thoresen]
year: 2014
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the framing manifesto behind the modelling choice at the heart of my France 2016 prototype. It gives me the citable theoretical defence of the latent-jobs structure I use, and — crucially — the formal bridge $\gamma(h)=\log\theta+\log g(h)$ that lets me reinterpret the conventional Van Soest dummy-augmented model as a special case of my framework where opportunities have been silently absorbed into preferences. Whenever a referee asks "why latent jobs rather than dummies?", this is the paper I cite.

## What it tells me about opportunities vs preferences
The paper's central interpretive move — that hours dummies $\gamma(h)$ are demand-side opportunity terms, not preference terms — is exactly the move my decomposition relies on. Without it, the Van Soest representation would book the part-time and full-time spikes as preferences, and any opportunity share of welfare inequality would mechanically collapse to zero. The paper also reminds me that the additive convention $v(C,h)+\gamma(h)$ implies non-monotone preferences in hours, which is normatively unattractive for any responsibility-sensitive welfare measure.

## What it tells me about welfare measurement
No welfare object is implemented, but the paper makes the right warning: any welfare measure built on the misidentified utility $v(C,h)+\gamma(h)$ will misclassify constrained outcomes as voluntary choices. This is exactly the misclassification my JMP is designed to avoid. It also points to Dagsvik & Karlström (2005) for matching-CV machinery, which is a useful cross-reference if I ever want to compute exact compensating variation rather than the AEI money-metric I currently use.

## What it tells me about decomposition
For pure tax/wage counterfactuals (variation in $C$ at fixed budget mapping), the latent-jobs structure and the dummy model deliver the same predictions, so the structural choice does not buy me anything mechanical. Where it buys something is in $A$-channel counterfactuals: equalising or reshaping $g(h)$ across cells is a counterfactual the dummy model literally cannot represent because the "preference" dummies are not portable across populations. My opportunity-equalisation Shapley component therefore lives or dies on this paper's structural reinterpretation.

## What it tells me about empirical design
Three concrete lessons. (i) Specify $g(h)$ flexibly with peaks at full-time and part-time and let $\theta$ depend on education and demographics — these are the moments the data identify well. (ii) Use Box-Cox systematic utility justified by the invariance axioms; this is the parametric form the latent-jobs literature has converged on. (iii) Be explicit that the wage elasticity scales with $(1-P)$, so when I report French elasticities and benchmark them against Norwegian or US numbers, I should adjust for the participation gap rather than treat raw elasticity differences as preference differences.

## How I may cite it in the paper
As the structural-interpretation reference for the RURO/latent-jobs framework, paired with Dagsvik & Jia (2016) for identification. Likely citations: in the model section when I introduce $g(h)$ and $\theta$, in a methodological footnote when I explain why I do not use additive hours dummies, and in the discussion when I motivate the $A$-channel counterfactuals as exercises that conventional discrete-choice models cannot perform.

## What limitation of this paper my JMP may address
The paper is a survey and explicitly states it does not improve fit, does not implement welfare, and freezes $g(h)$ in the short run. My JMP closes the welfare loop: I take the structural reinterpretation as given, layer on a money-metric welfare object, and produce a quantitative Shapley decomposition where the share attributable to $g(h)$ and $\theta$ becomes a reportable number. The out-of-sample prediction exercise the authors run for the 2006 Norwegian reform is also a template for the validation exercise I should run on a French reform episode.

---

<a id="paper-010"></a>

## Dagsvik Jia 2016

**Source file:** `core_jmp_notes/Dagsvik_Jia_2016.md`

---
title: "Labor Supply as a Choice Among Latent Jobs: Unobserved Heterogeneity and Identification"
authors: [John K. Dagsvik, Zhiyang Jia]
year: 2016
shelf: "RURO / Latent Jobs / Constrained Labour Supply"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the cleanest existing identification analysis of the latent-jobs model that sits at the centre of my France 2016 prototype. My JMP separates preferences from opportunities and then uses both to decompose welfare inequality; this paper tells me precisely what that separation can and cannot deliver from cross-sectional data, and which functional-form choices buy back identification when nonparametric identification fails. It is the paper a referee will most likely cite when asking whether my opportunity-vs-preference decomposition is anything more than an artefact of my parametric assumptions.

## What it tells me about opportunities vs preferences
The product $v(C,h)\cdot g_1(h)$ is identified, the individual factors are not. The unidentified piece $\delta(h)$ is precisely a function of hours that could be reallocated freely between the preference block and the opportunity block. Practically: any narrative that the preference share of inequality is "X%" rather than "Y%" only holds inside the maintained parametric family. This is a constraint I should state explicitly rather than hide. The paper also shows empirically that Model 2 (individual-specific wages) dominates Model 1 (job-specific wages) on Norwegian couples, which is directly informative for how I should specify wage heterogeneity in the France pipeline.

## What it tells me about welfare measurement
The paper does no welfare analysis but the identification result has a sharp welfare implication. Whenever the welfare object compares utility levels across individuals choosing different hours — which is exactly what an AEI-style money-metric measure does — the unidentified $\delta(h)$ enters. So my welfare layer is parametric in the same sense the preference block is parametric. This sets up a natural sensitivity check: report the decomposition under at least two parameterisations of $v(C,h)$ and show how much the opportunity share moves.

## What it tells me about decomposition
For tax/wage counterfactuals (variation in $C$ holding $h$ fixed), the non-identification of $\delta(h)$ is harmless. For my opportunity-equalisation counterfactual it bites: equalising $g_1(h)$ across region $\times$ education cells is precisely a counterfactual that changes which hours $h$ are chosen, and the welfare evaluation of the new choices uses the identified-only-up-to-$\delta(h)$ utility. So the Shapley share I attribute to opportunities is conditional on the parametric decomposition of $v(C,h)\cdot g_1(h)$ chosen at estimation.

## What it tells me about empirical design
Three concrete design lessons. (i) Use Box-Cox preferences and the regularity condition (Assumption 5) to anchor identification. (ii) Specify wage heterogeneity at the individual level rather than at the job level — Model 2 dominated empirically and is also more transparent for the welfare layer. (iii) The three-stage estimator (participation probability → Heckman wage equations → ML) is a sensible template, and division-bias measurement error in hours is something I should expect to live with rather than fully resolve.

## How I may cite it in the paper
As the identification reference for the RURO/latent-jobs model. Likely citations: in the model section when I introduce the multiplicative utility-opportunity structure, in the identification section to flag what is and is not nonparametrically identified, and in a robustness/limitations paragraph to justify why I report the decomposition under at least two parametric specifications.

## What limitation of this paper my JMP may address
The paper stops short of any welfare analysis and explicitly acknowledges that the welfare implications of its identification result are unexplored. My JMP closes that loop: I take the parametric resolution they propose (Box-Cox + regularity), inherit their non-identification caveat, and then show how the maintained specification translates into a money-metric welfare object and a Shapley decomposition of welfare inequality. The decomposition exercise also makes the cost of the non-identification visible and quantifiable — sensitivity of the opportunity share to the parametric form of $v(C,h)$ becomes a falsifiable, reportable number rather than a footnote.

---

<a id="paper-011"></a>

## Ferreira Gignoux 2011

**Source file:** `core_jmp_notes/Ferreira_Gignoux_2011.md`

---
title: "The Measurement of Inequality of Opportunity: Theory and an Application to Latin America"
authors: [Francisco H. G. Ferreira, Jérémie Gignoux]
year: 2011
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the theoretical reference for the inequality-of-opportunity measurement framework my decomposition exercise sits inside. It supplies the axiomatic justification (path-independent decomposability uniquely picks out the mean log deviation), the lower-bound interpretation that disciplines how circumstance-based opportunity shares should be read, and the smoothed-distribution machinery I am directly extending by replacing income with welfare $W(z,R,A;y)$. It is also the cleanest articulation of the limitation my structural framework addresses: opportunities are observed background types, not feasible sets.

## What it tells me about opportunities vs preferences
The paper makes the circumstance-vs-effort cut sharply but does not separate effort from preferences — both vanish into the within-type residual that is silently labelled "ethically acceptable". This is the same silent-conflation problem as in Bourguignon-Ferreira-Menéndez (2007), and my JMP dissolves it by structurally identifying preferences from RURO and structural opportunities from the opportunity density $g(h,w)$ and $\theta$. Where this paper has one residual that mixes effort, preferences, luck, and unobserved circumstances, my JMP has four economically-disciplined channels.

## What it tells me about welfare measurement
Indirectly important. The advantage variable in this paper is income or consumption, but the smoothed-distribution machinery is welfare-agnostic — it transfers cleanly to a welfare object $W(z,R,A;y)$ as the advantage variable. The lower-bound interpretation also generalises: any opportunity measure built on observed circumstances is a lower bound on true opportunity inequality, and the same will be true of my welfare-based version. The paper itself flags this generalisation as an open direction; my JMP delivers it.

## What it tells me about decomposition
Three direct lessons. (i) Path-independent decomposability uniquely pins the opportunity index to $E_0$ — useful when I report inequality-of-welfare-opportunity numbers, since it gives an axiomatic justification for choosing $E_0$ over Gini or Atkinson. (ii) The non-parametric/parametric agreement test is a defensible robustness check — I should run my structural Shapley decomposition both with full parametric structure and with a non-parametric cell-mean version and verify the headline numbers are close. (iii) Lower-bound logic also applies to my decomposition: any unobserved heterogeneity in opportunities or preferences would weakly increase the structural-channel contribution, so my numbers are also lower bounds on the true structural-factor share.

## What it tells me about empirical design
Three lessons. (i) Define types coarsely enough that cells are populated for non-parametric estimation, but finely enough that within-type variation is plausibly orthogonal to circumstances — the paper's parental-education × ethnicity × region partition is a good template. (ii) Report opportunity-deprivation profiles ranking types by mean advantage to identify the worst-off — this is one of the paper's most policy-relevant outputs and transfers naturally to my welfare object: ranking RURO-type cells by mean welfare identifies opportunity-deprived groups in welfare space, not just income space. (iii) Use both income and consumption as advantage variables to test sensitivity — the opportunity share rises substantially when consumption replaces income in this paper's data, which is itself informative.

## How I may cite it in the paper
As the canonical theoretical reference for inequality-of-opportunity measurement. Likely citations: in the literature section as the formalisation of the van-de-Gaer ex-ante approach; in the methodological section to justify $E_0$ as the inequality index for the opportunity component via path-independent decomposability; in the discussion as the comparator for international magnitudes of the lower-bound opportunity share; and in the limitations section as the precursor whose circumstance-type opportunity definition my structural feasible-set primitive supersedes.

## What limitation of this paper my JMP may address
Two. (i) Opportunities are circumstance types, not feasible sets — demand-side job availability and hours restrictions are invisible. My RURO framework with $g(h,w)$ and $\theta$ replaces the type partition with a structural opportunity primitive that captures exactly this missing variation. (ii) The within-type residual is treated as ethically distinct without a structural account of effort or preferences. My JMP supplies that account: structural preferences from RURO occupy the residual, and the Shapley-Shorrocks decomposition splits the welfare-inequality total into preference, opportunity, wage, and non-labour-income components rather than collapsing everything non-circumstantial into a single un-interpreted residual.

---

<a id="paper-012"></a>

## Jacquet Jia Thoresen 2026

**Source file:** `core_jmp_notes/Jacquet_Jia_Thoresen_2026.md`

---
title: "How Much Does Responsibility Matter in Fairness Measurement?"
authors: [Laurence Jacquet, Zhiyang Jia, Thor O. Thoresen]
year: 2026
shelf: "Responsibility / Fairness / Equality of opportunity"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the existing paper closest to what my JMP is doing. It implements the responsibility cut in a RURO model, constructs a circumstance-only welfare object, and evaluates a real tax reform with it. The methodological footprint is essentially the one I am extending to France 2016. So this is both my closest competitor — anyone reading my JMP will ask "what's new beyond Jacquet-Jia-Thoresen?" — and my most direct methodological precedent. My JMP needs to define its contribution sharply against this paper.

## What it tells me about opportunities vs preferences
The paper gives the cleanest worked example of the additive decomposition $V=u+\log Q_F+\log Q_M+\eta$ that licenses the $R/A$ split inside RURO. It also delivers the empirical headline I need to engage with: in Norway 2015, conditioning on opportunities while neutralising preferences leaves welfare rankings essentially unchanged in deciles 1–9 and only diverges at the top. That is a strong "responsibility-matters-little" result that my France pipeline either replicates (in which case the result generalises) or refutes (in which case I have a comparative-finding contribution).

## What it tells me about welfare measurement
The CV$^{\text{circ}}$ construction is exactly the welfare object I want to build for France. Lessons: (i) compute it via McFadden (1999) simulation with $K$ Gumbel draws per household, not via a closed form; (ii) take $\bar\gamma$ at sample medians rather than at any one reference person; (iii) verify alignment between CV$^{\text{circ}}$ and Fleurbaey's $\Delta CE$ as a cross-method robustness check — this paper finds them empirically aligned, which is reassuring. The paper does not implement CV$^{\text{pref}}$ (neutralising opportunities while keeping preferences), but mentions it as the natural complementary object. That is a clean opening for my JMP — completing the $2\times 2$ of (own/reference) preferences × (own/reference) opportunities is something this paper notably does not do.

## What it tells me about decomposition
The paper does a two-way comparison (CV vs CV$^{\text{circ}}$) but not a Shapley decomposition. It treats the difference between the two as the welfare contribution of preference heterogeneity. My JMP can extend this by adding the third channel (wage / non-labour income) and using a Shapley-Shorrocks decomposition for order-independence. The paper's own implicit decomposition into "preferences" and "circumstances" is best read as a special case of the four-way decomposition my framework produces.

## What it tells me about empirical design
Five lessons. (i) Estimate via Conditional Logit ML on the joint household choice set (here 56 alternatives = 7 male × 8 female). (ii) Box-Cox systematic utility with ~15 parameters is feasible at sample sizes around 1,500–2,500 couples — this is the order of magnitude my France SRCV sample sits at. (iii) Identify the female opportunity measure through schooling at minimum; for France I should add region and possibly sector. (iv) Normalise the male opportunity measure to one only if male participation is near-universal — for France this is a defensible call for prime-age men but maybe not for older cohorts. (v) Exclude self-employment and extreme wage outliers consistently with the Norwegian sample selection.

## How I may cite it in the paper
As the canonical existing implementation of CV$^{\text{circ}}$ inside a RURO model. Likely citations: in the introduction as the closest existing methodological precedent; in the model section as the source of the additive RURO indirect-utility decomposition; in the welfare-framework section as the source of CV$^{\text{circ}}$; in the empirical-results section as the Norwegian benchmark for the "where in the distribution does responsibility bite" question; and in the limitations section as the precedent that does not extend to a full Shapley decomposition or to opportunity-side neutralisation.

## What limitation of this paper my JMP may address
Three. (i) The opportunity measure depends on schooling only; my France pipeline can enrich it with region and education jointly, which the paper itself flags as a productive direction and which may flip the headline result. (ii) The two-way comparison stops short of a four-way Shapley decomposition over preferences, opportunities, wages, and non-labour income — my JMP delivers exactly that. (iii) The CV$^{\text{pref}}$ counterpart (neutralising opportunities) is mentioned but not constructed; my framework completes the $2\times 2$, which is normatively important because the responsibility cut and the compensation cut are dual objects, not the same one viewed twice.

---

<a id="paper-013"></a>

## Shorrocks 2013

**Source file:** `core_jmp_notes/Shorrocks_2013.md`

---
title: "Decomposition Procedures for Distributional Analysis: A Unified Framework Based on the Shapley Value"
authors: [Anthony F. Shorrocks]
year: 2013
shelf: "Decomposition methods / Inequality of opportunity"
note_type: "JMP-linked"
---

## Why this paper matters for my JMP
This is the methodological backbone of the welfare-inequality decomposition that gives my JMP its quantitative headline. My core deliverable is a Shapley-Shorrocks decomposition of welfare inequality into preference, opportunity, wage, and non-labour-income components — and Shorrocks (2013) is the rule I am applying. It is also the methodological reference any referee will check to verify that my decomposition is exact, symmetric, and residual-free rather than ad hoc.

## What it tells me about opportunities vs preferences
Nothing directly — the paper is normatively neutral. But it gives me the formal apparatus to make the opportunity-vs-preference split *quantitative* once I have defined the underlying factors in my structural model. The hard substantive work (what does "removing opportunity heterogeneity" mean in a RURO model?) is upstream of the Shapley rule itself, and the paper is explicit about this division of labour. My JMP needs to be careful to defend the upstream factor definitions on economic grounds and let Shorrocks (2013) do the attribution mechanics.

## What it tells me about welfare measurement
Indirectly important. Once I have computed welfare levels under the $W(z,R,A;y)$ framework, the Shapley rule lets me decompose any inequality measure of those welfare levels — Gini, MLD, Atkinson, variance — into factor contributions. Importantly, the rule gives the same factor split for the variance regardless of which inequality index is chosen as the target, which means I can run a robustness check across several indices and present a unified narrative.

## What it tells me about decomposition
Three direct lessons. (i) Use the Shapley rule rather than any sequential or ad hoc procedure — the order-invariance is non-negotiable for credibility. (ii) Use the Owen hierarchical extension to group factors: my four primary factors (preferences, opportunities, wages, non-labour income) can each be decomposed further in a second stage if needed. (iii) Document all $2^m$ subset evaluations explicitly so the decomposition is fully reproducible — for $m=4$ this is 16 subset evaluations per household, which is computationally trivial.

## What it tells me about empirical design
Two practical lessons. (i) Define the null counterfactual for each factor with care — the Shapley contribution literally depends on what "$X_k$ removed" means. For my opportunity counterfactual, "remove opportunity heterogeneity" should mean equalising $g(h)$ and $\theta$ across cells in some interpretable way (e.g., to the population-mean opportunity distribution), not setting them to zero. (ii) Pre-register the factor list and the null counterfactuals in the appendix so the decomposition is not ex-post tuned — this is the strongest defence against the "results-depend-on-counterfactual" critique the paper itself flags.

## How I may cite it in the paper
As the methodological reference for the Shapley-Shorrocks rule. Likely citations: in the methods section to introduce the decomposition formula; in the implementation appendix to motivate the choice of the Shapley rule over ad hoc sequential decompositions; in the robustness section to justify reporting multiple inequality indices under the same factor split; and possibly in the limitations section to acknowledge that the decomposition is conditional on the analyst-defined null counterfactuals.

## What limitation of this paper my JMP may address
The paper itself is a tool, not a model — it does not define preferences, opportunities, or pay schedules as factors. My JMP supplies exactly that upstream definition: it takes the RURO structural model as the source of $R$ and $A$, the wage distribution as the source of pay heterogeneity, and the EUROMOD tax-benefit calculator as the source of $y$, and feeds those four factors into the Shapley rule. So my contribution complements Shorrocks's by populating the framework with economically-disciplined factors rather than leaving the choice to the analyst.
