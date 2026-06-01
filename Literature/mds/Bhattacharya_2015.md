---

title: "Nonparametric Welfare Analysis for Discrete Choice"
authors: ["Debopam Bhattacharya"]
year: 2015
outlet: "Econometrica"
country_or_context: "General methodological setting; no single country application"
population: "Individuals facing binary, unordered multinomial, or ordered discrete choices"
data_period: ""
shelf: "welfare_methods_discrete_choice"
tags: ["discrete choice", "equivalent variation", "compensating variation", "nonparametric identification", "unobserved heterogeneity", "money-metric welfare", "unordered multinomial choice", "ordered choice"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bhattacharya, Debopam. 2015. “Nonparametric Welfare Analysis for Discrete Choice.” *Econometrica* 83(2): 617–649. 

# One-sentence contribution

The paper shows that, for binary and unordered multinomial discrete choice models, the marginal distributions and means of equivalent variation (EV) and compensating variation (CV) from a price change are nonparametrically point-identified from structural choice probabilities alone, even under unrestricted unobserved preference heterogeneity and without specifying utility functional forms. 

# Why this paper matters

This paper matters because it sharply separates two issues that are often conflated in structural applied work: identification of behavioural heterogeneity and identification of welfare objects. Its central claim is that one can recover money-metric welfare effects for discrete choice without identifying the dimension or distribution of heterogeneity and without imposing parametric utility structure, provided one is in the binary or unordered multinomial case. 

For your project, the paper is important less because it models labour supply or opportunity sets directly, and more because it clarifies what can be recovered from observed discrete choices when preferences are heterogeneous. It is especially useful as a methodological benchmark on welfare measurement under heterogeneity, and as a warning that some welfare results are fundamentally identified while others are only artifacts of functional-form assumptions. 

# Core research question

Can the distribution of money-metric welfare effects from price changes in discrete choice settings be nonparametrically identified when individuals have unrestricted, possibly high-dimensional unobserved heterogeneity in preferences and utilities are otherwise left unspecified? 

# Economic setting and context

The paper studies generic discrete-choice environments rather than a specific country, market, or dataset. The motivating examples include taxation of unemployment benefits, fare changes in transportation mode choice, and supermarket brand choices under discounts or taxes. The observed data environment is individual-level microdata containing realized discrete choices, prices faced, income, and possibly covariates. 

The object of interest is the welfare impact of a hypothetical price change for a discrete good or alternative, measured by EV and CV. The analysis is methodological and identification-theoretic, not an empirical application to a single market. 

# Model / theoretical framework

The model class is nonparametric random-utility-based welfare analysis for discrete choice. In the binary case, the agent chooses between buying and not buying a discrete good, with utilities (U_1(Y-P,\eta)) and (U_0(Y,\eta)), where (\eta) is an individual-specific taste component of unrestricted and possibly unknown dimension. The budget constraint is (W + PQ = Y), and the structural choice probability is
[
\bar q(p,y)=\Pr{U_1(y-p,\eta)>U_0(y,\eta)}.
]


The feasible set is a finite set of discrete alternatives. In the unordered multinomial case, the paper reduces welfare analysis for a price change in one alternative to a binary comparison between that alternative and a composite outside option. In the ordered-choice case with a common unit price across quantities, the paper shows that this reduction fails in a fundamental way. 

The framework is positive with welfare applications. It is positive because it studies what can be identified from choice probabilities under minimal restrictions on utility. It is welfare-oriented because the target objects are Hicksian money-metric measures, EV and CV, not merely demand elasticities or choice probabilities. The paper is not explicitly normative in the fairness, compensation, or responsibility sense. 

# Key objects

The main economic objects are the structural choice probabilities (\bar q(p,y)) in the binary case and (\bar q_1(t,p_{-1},y)) in the unordered multinomial case; the individual welfare changes (S^{EV}) and (S^{CV}); and the underlying utilities (U_j(\cdot,\eta)), which are assumed only to be continuous and strictly increasing in the numeraire. 

The core identified objects are the marginal distributions of EV and CV. For a binary price increase from (p_0) to (p_1), Theorem 1 shows that for (0 \le a < p_1-p_0),
[
\Pr(S^{EV}\le a)=1-\bar q(p_0+a,y), \qquad
\Pr(S^{CV}\le a)=1-\bar q(p_0+a,y+a).
]
Corollary 1 then gives average EV and CV as integrals of choice probabilities. These formulas are the analytical center of the paper. 

# Data

There is no empirical application with a specific dataset, country sample, or time period. The paper is written for a setting in which the researcher observes individual choices, prices, income, and possibly covariates in microdata. It discusses how the structural choice probabilities could be estimated nonparametrically from such data, or with control functions if price or income are endogenous. 

# Identification logic

The identification logic is very concrete. The paper shows that, under continuity and strict monotonicity of utilities in the numeraire, EV and CV distributions can be written as closed-form functionals of structural choice probabilities. Thus welfare identification does not require identification of the distribution of (\eta), its dimension, or the functional form of utilities. This is the main theorem for binary and unordered multinomial choice. 

The variation relied upon is variation in prices and income sufficient to recover structural choice probabilities. If prices and income are conditionally independent of heterogeneity, (\bar q) can be obtained by nonparametric regression of choices on prices and income. If endogeneity is present, the paper suggests control-function methods as a way to recover structural choice probabilities. The paper is explicit that its theorems identify welfare as a functional of structural choice probabilities, and that separate identification of (\bar q) from observed data is an additional step. 

Identification fails, in general, for ordered choice with three or more alternatives when all units face the same per-unit price. The reason is not merely technical; it is that the relevant counterfactual comparison probabilities are not observed from the feasible family of budget sets. This is one of the most important conceptual results in the paper. 

# Estimation / empirical strategy

The paper is mainly about identification rather than estimation. Its empirical strategy is therefore generic: estimate structural choice probabilities nonparametrically when the necessary support exists, then plug those into the closed-form formulas for EV and CV distributions and their means. For expected welfare, the resulting objects are partial means of the estimated choice-probability function. 

The paper also discusses practical limits. If hypothetical price changes lie outside the observed support, or if price variation is limited, then fully nonparametric computation is not feasible and one must either impose parametric structure or derive bounds. It explicitly advises sensitivity analysis between nonparametric and parametric implementations whenever possible. 

# Treatment of preferences

Preferences are allowed to be highly heterogeneous and almost unrestricted. The heterogeneity term (\eta) may be vector-valued, of unknown dimension, and enter utility in arbitrary ways. Utilities need not be quasilinear, differentiable, or parametrically specified. The paper emphasizes that restricting heterogeneity to a scalar or low-dimensional form can impose strong and often hidden restrictions on the set of admissible preference profiles. 

This is one of the strongest aspects of the paper for your purposes. It is explicitly designed to avoid deriving welfare conclusions from arbitrary assumptions about the dimension or distribution of unobserved heterogeneity. The appendix example is especially important: it shows a case where even the dimension of heterogeneity is not identified, yet welfare distributions remain point-identified. 

# Treatment of opportunities / constraints

The paper does not model opportunities explicitly in the sense of feasible job sets, latent offer sets, or individual-specific opportunity correspondences (A_i). The constraint structure is the budget set generated by income, prices, and the set of discrete alternatives. In that sense, opportunities are treated as the menu of alternatives under observed prices, not as labor-market opportunity sets or socially relevant feasible sets. 

Availability constraints are therefore implicit and generic rather than modeled as a separate object. In the binary and unordered multinomial settings, the paper assumes the relevant alternatives are available as the choice set under study. It does not use latent jobs, job-offer distributions, hours restrictions, or demand-side rationing. 

The paper clearly helps distinguish preference heterogeneity from welfare identification, but it does not distinguish preference heterogeneity from opportunity heterogeneity in your sense. There is no decomposition into “preferences versus opportunities,” and no explicit demand-side opportunity heterogeneity. For your project, this is a limitation. 

# Welfare / normative object

The welfare object is exact money-metric welfare from price changes, specifically EV and CV. These are defined at fixed income (y) as the income changes that equalize maximized utility before and after a price change. The paper is not interested in a social-welfare functional over persons; it is interested in identifying the distribution of individual welfare effects induced by heterogeneity. 

The paper is therefore positive with welfare applications, rather than explicitly normative. It does not develop a fairness criterion, does not take a stand on compensation for opportunities, and does not discuss responsibility-sensitive welfare evaluation. Nor does it construct reference opportunity sets. Its welfare notion is standard Hicksian money-metric welfare. 

For your project, the useful part is methodological: it shows that even under very general heterogeneity, some welfare distributions are recoverable directly from discrete-choice probabilities. The less useful part is normative: nothing here addresses responsibility for opportunities, compensation for unequal feasible sets, or decomposition of inequality into preference and opportunity components. 

# Main findings

The main result is that in binary and unordered multinomial choice models, the marginal distributions of EV and CV are nonparametrically point-identified as simple functionals of structural choice probabilities. This holds under continuity and strict monotonicity in the numeraire, without knowing the dimension or distribution of unobserved heterogeneity and without specifying utility functional forms. 

A second major result is that, for a price increase, average EV equals the change in average Marshallian consumer surplus even without quasilinearity. By contrast, average CV generally differs from average EV; for a normal good, average CV exceeds average EV. The paper derives these conclusions from the identified welfare distributions. 

A third major result is the asymmetry between unordered and ordered choice. The nonparametric point-identification results that hold for binary and unordered multinomial choice fail for ordered choice with three or more alternatives when all units share the same unit price. This links the paper to Hausman–Newey style partial-identification results for continuous-choice welfare. 

# Main limitations

The most important limitation for your purposes is that the paper has no explicit theory of opportunity sets. It studies budget sets and discrete alternatives, but not feasible job sets, latent opportunities, or unequal access to alternatives as an independent object of analysis. This limits its direct relevance for a (W(z,R,A;y)) framework where (A) is central. 

A second limitation is that the welfare object is narrow. EV and CV are exact and useful money-metric measures, but they are not general well-being measures in the axiomatic sense you are developing. They are tied to price changes and do not directly speak to fairness, responsibility, or opportunity-sensitive compensation. 

A third limitation is practical identification. The theory is elegant, but implementation still requires sufficient support in prices and incomes to estimate structural choice probabilities. Outside observed support, or with limited price variation, the paper itself acknowledges that one must rely on parametric structure or bounds. 

A fourth limitation is that the paper is not a decomposition paper. It does not provide a decomposition of observed inequality or welfare inequality into preferences, opportunities, prices, or policies. It therefore fits your project better as a methodological reference on welfare recovery under heterogeneity than as a direct source on inequality decomposition. 

# Relevance for my JMP

## possible use for framing

This paper is useful for framing a methodological distinction between identifying preference heterogeneity and identifying welfare objects. It can help justify why one should not infer that a welfare measure is impossible merely because the heterogeneity distribution is not identified. 

## possible use for model design

It is moderately useful for model design if you want a welfare layer that sits on top of a discrete-choice model without forcing parametric assumptions on utility heterogeneity. It is not useful for designing the opportunity-set component (A), because it does not model opportunities explicitly beyond the observed choice menu and budget variation. 

## possible use for identification

This is where the paper is strongest for your JMP. It provides a clean example of identification theorems that derive welfare objects from observable choice-probability functions, and it sharply identifies when such recovery fails. The ordered/unordered distinction is especially valuable as a model-diagnostics insight. 

## possible use for welfare measurement

It is highly useful for welfare measurement if your object is money-metric welfare from price changes in discrete choice. It is much less useful if your target is a broader well-being measure depending on realized bundle, preferences, feasible set, and pay schedule. 

## possible use for decomposition

Direct use is limited. The paper does not decompose welfare inequality into preferences, opportunities, and other components. At most, it suggests that one could separately study welfare identification and heterogeneity identification rather than conflating them. 

## possible use for comparative application

Indirectly, it could be used in comparative applications if one has discrete-choice data across countries or regions and wants to compare welfare effects of price changes with minimal utility structure. But the paper itself does not provide a cross-country design or comparative application. 

# Research questions this paper inspires

1. In a labour-supply model with latent job offers, can one derive nonparametric or semiparametric analogues of Bhattacharya’s EV/CV identification results when the relevant alternatives are jobs rather than consumer goods?

2. Which parts of a (W(z,R,A;y)) framework can be identified from observed discrete choices alone, and which parts require explicit modeling or observation of opportunity sets (A)?

3. Can one construct a money-metric welfare measure for discrete labour choices that remains identified under unrestricted preference heterogeneity but is also sensitive to unequal opportunity sets?

4. Does an ordered-hours labour-supply model suffer from a welfare-identification failure analogous to Bhattacharya’s ordered-choice result when the effective “unit price” of work is common across adjacent hours categories?

5. Can one decompose welfare differences in discrete-choice settings into components due to price schedules, preference heterogeneity, and opportunity-set heterogeneity while preserving nonparametric identification of at least some margins?

# Challenge to this paper

The main challenge is that the paper solves a narrower problem than the one your project faces. It shows how to identify EV and CV from choice probabilities, but it leaves untouched the ethically central question of whether welfare comparisons should control for, compensate for, or hold agents responsible for differences in feasible opportunities. In that sense, it is a powerful econometric paper with only limited normative reach. 

# Relation to my jobs_and_wellbeing framework

[explicit in paper] The paper studies welfare as an individual money-metric response to price changes in discrete choice, with unrestricted heterogeneity in utility and without parametric specification of utility functions. Its central objects are realized discrete choices, structural choice probabilities, and EV/CV distributions. 

[reasonable inference for my project] A loose mapping to your framework is that the realized chosen alternative corresponds to part of (z), and the heterogeneous utility representation corresponds loosely to (R). However, the paper has no explicit analogue of (A) as a feasible job or ability set, and its price/income environment is not a pay schedule (y) in your sense but a standard budget environment. 

[explicit in paper] The paper is not about jobs, labour-market opportunity sets, or responsibility-sensitive welfare. It is about price-change welfare in discrete choice and the identification of EV/CV from structural choice probabilities. 

[reasonable inference for my project] The paper is therefore closest to your project on the dimension of welfare measurement under heterogeneous preferences, not on the dimensions of reference opportunity sets, responsibility for opportunities, or decomposition of inequality into preferences and opportunities. It is not naturally aligned with independence of (A), independence of (y), laissez-faire type evaluation, or reference opportunity sets. If forced into your taxonomy, it is closest to “none of these directly,” with some indirect relevance for how a money-metric welfare layer might be identified once a positive model is in place. 

[unclear from paper] Whether its identification strategy could be extended to a full (W(z,R,A;y)) setting with latent feasible sets and normative axioms is not addressed in the paper. 

# Relation to Bargain et al. (2013)

This paper is related to the Bargain et al. line of work only at a methodological distance. Both are concerned with welfare analysis under heterogeneous preferences in discrete-choice environments, but Bhattacharya studies generic nonparametric identification of EV/CV, whereas Bargain-type work is typically embedded in structural labour-supply and tax-benefit microsimulation. Bhattacharya is more general on heterogeneity and less specific on labour supply, interpersonal comparability, and policy design. For your purposes, it is a complementary methodological paper rather than a substitute benchmark. [reasonable inference for my project] 

# Relation to opportunities vs preferences

The paper is strong on preferences and weak on opportunities. It is designed to allow very rich unobserved preference heterogeneity and to show that welfare effects can still be identified. But opportunities are not modeled as unequal feasible sets; they are only the alternative menus and budget configurations induced by the discrete-choice setting. 

Its most useful conceptual lesson for your opportunities-versus-preferences agenda is negative rather than positive: one should not read “unidentified heterogeneity” as “unidentified welfare.” But one also should not mistake this for an opportunity-sensitive framework. The paper does not help with compensating for unequal opportunities or assigning responsibility across opportunity sets. 

# Useful quotations / formulas

For binary choice under a price increase from (p_0) to (p_1), the central identification formulas are
[
\Pr(S^{EV}\le a)=1-\bar q(p_0+a,y), \qquad
\Pr(S^{CV}\le a)=1-\bar q(p_0+a,y+a),
]
for (0 \le a < p_1-p_0). These are the key closed-form results of Theorem 1. 

The corresponding mean welfare formulas are
[
\mu_{EV}(y,p_0,p_1)=\int_{p_0}^{p_1}\bar q(p,y),dp, \qquad
\mu_{CV}(y,p_0,p_1)=\int_{p_0}^{p_1}\bar q(p, y+p-p_0),dp.
]
These are especially useful because they show average EV equals the change in average Marshallian consumer surplus even without quasilinearity. 

# Suggested tags

discrete-choice-welfare, nonparametric-identification, EV, CV, heterogeneous-preferences, unordered-multinomial, ordered-choice-failure, money-metric-welfare

# My quick takeaway

This is a methodologically important paper for the welfare side of your corpus, but not a paper on opportunities in the labour-market sense. Its main value is to show that discrete-choice welfare objects can sometimes be identified far more robustly than the underlying heterogeneity structure. For your JMP, it is best read as a clean reference on welfare identification under heterogeneous preferences, and as a boundary marker showing what remains missing when one wants to move from discrete-choice welfare to a full (W(z,R,A;y)) framework with explicit opportunity sets and responsibility-sensitive evaluation.
