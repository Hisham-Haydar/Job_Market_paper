---

title: "Nonparametric Welfare Analysis for Discrete Choice"
authors: ["Debopam Bhattacharya"]
year: 2015
outlet: "Econometrica"
country_or_context: "General methodological discrete-choice framework; no country-specific empirical application"
population: "[not an empirical paper]"
data_period: "[not applicable]"
shelf: "nonparametric_discrete_choice_welfare_ev_cv"
tags: ["discrete choice", "nonparametric welfare", "equivalent variation", "compensating variation", "unobserved heterogeneity", "choice probabilities", "binary choice", "multinomial choice", "ordered choice", "consumer surplus"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bhattacharya, Debopam. 2015. “Nonparametric Welfare Analysis for Discrete Choice.” *Econometrica* 83(2): 617–649. 

# One-sentence contribution

The paper shows that, for binary and unordered multinomial discrete choice under essentially unrestricted unobserved preference heterogeneity, the marginal distributions of equivalent variation and compensating variation from a price change are nonparametrically point-identified as simple functionals of choice probabilities. 

# Why this paper matters

This paper matters because it isolates a basic identification fact: for a broad class of discrete-choice settings, one does not need a parametric random utility model with known heterogeneity distribution in order to recover welfare effects of a price change. The relevant information is already contained in the choice probabilities themselves. 

For your potential JMP, this is highly relevant on the welfare side. It does not build a labor-supply model, a latent-job model, or an opportunity-set model, but it gives a rigorous nonparametric welfare layer for discrete choice with heterogeneous preferences. It is especially useful if you want to avoid basing welfare conclusions entirely on heavily parameterized utility specifications. 

# Core research question

When individuals make discrete choices and preferences are heterogeneous in unrestricted, unobserved ways, can the distribution of money-metric welfare changes from a price change—specifically EV and CV—be identified nonparametrically from observed choice behavior? 

# Economic setting and context

The paper is methodological rather than empirical. The motivating contexts are price changes affecting discrete decisions such as unemployment-exit choices, transport mode choice, and supermarket brand choice. These are examples, not applications estimated in the paper. 

The economic setting is a standard discrete-choice random utility environment in which the researcher observes individual choices, prices, income, and possibly other covariates, and wants to evaluate welfare effects of a hypothetical price change. The paper studies both binary choice and unordered multinomial choice, and then contrasts these with ordered choice. 

# Model / theoretical framework

The model class is a nonparametric discrete-choice random utility model. In the binary case, an individual chooses between buying and not buying a discrete good. Utility from buying is (U_1(Y-P,\eta)), utility from not buying is (U_0(Y,\eta)), where (\eta) is unobserved heterogeneity of unknown dimension and unknown distribution. Utility is assumed continuous and strictly increasing in the numeraire. 

The key structural object is the choice probability
[
\bar q(p,y)=\Pr!\left(U_1(y-p,\eta)>U_0(y,\eta)\right),
]
evaluated at hypothetical price-income pairs. The analysis then derives the marginal distributions of EV and CV directly from this object. 

For unordered multinomial choice, the problem is reduced to a binary comparison between one focal alternative and a composite outside option formed from the remaining alternatives. This allows the binary-choice welfare logic to carry over. The framework is positive with welfare analysis; it is not a social-choice or fairness-axiom paper. 

# Key objects

The main objects are the structural choice probabilities, the marginal distributions of equivalent variation and compensating variation, their means, and associated objects such as deadweight loss. These are the central welfare objects of the paper. 

In the binary case, the paper derives explicit formulas for
[
\Pr(SEV\le a)
\quad\text{and}\quad
\Pr(SCV\le a),
]
for a price increase from (p_0) to (p_1), and shows that these are simple transformations of (\bar q(\cdot,\cdot)). For unordered multinomial choice, the same logic applies using the alternative-specific choice probability (\bar q_1(\cdot)). 

A second key object is the contrast between unordered multinomial choice and ordered choice. In ordered choice with a common unit price across alternatives, the paper shows that the distributions of EV and CV are generically not nonparametrically point-identified. This is a major conceptual object in the paper, not a side remark. 

# Data

There are no data. This is a theory and identification paper. The paper discusses what would be observed in microdata—individual choices, prices, income, and covariates—but it contains no empirical application and no estimation exercise on an actual dataset. 

# Identification logic

This is the core contribution.

The paper’s main identification result is that in binary choice, the marginal distributions of EV and CV are exact closed-form functionals of the structural choice probability (\bar q(p,y)). For a price increase from (p_0) to (p_1), the paper shows
[
\Pr(SEV\le a)=1-\bar q(p_0+a,y),
\qquad
\Pr(SCV\le a)=1-\bar q(p_0+a,y+a),
]
for (0\le a<p_1-p_0). These formulas require no specification of the dimension of heterogeneity, no parametric utility form, and no identified heterogeneity distribution. 

The intuition is that the welfare threshold (a) can be translated into a reservation-price comparison. For EV, the probability that EV is below (a) is the probability that the individual would not buy when the initial price is increased to (p_0+a) at income (y). For CV, the relevant comparison uses both the higher price and the compensation-adjusted income (y+a). 

For unordered multinomial choice, identification proceeds by collapsing all non-focal alternatives into a composite outside option. Then the same binary-choice argument applies to the focal alternative’s choice probability. By contrast, for ordered choice with a common unit price, the relevant counterfactual comparisons needed for welfare are not observed in the data, so nonparametric point identification fails. The diagrams on pages 22–23 make this difference especially clear: in ordered choice, the relevant bundles do not lie on the observed budget lines, whereas in unordered choice with alternative-specific pricing they do. 

# Estimation / empirical strategy

There is no empirical estimation in the paper. The strategy is analytical derivation of welfare-distribution formulas from the structural choice probabilities. If the researcher can estimate these probabilities—nonparametrically under exogeneity, or with control functions under endogeneity—then welfare distributions are obtained by direct plug-in. 

The paper also discusses inference briefly. For nonparametrically estimated choice probabilities, welfare distributions can be estimated by substitution. Means of welfare objects are partial-mean functionals of the choice probabilities. In parametric models such as multinomial logit or mixed logit, the same formulas remain useful because one can compute EV/CV directly from estimated choice probabilities rather than by first recovering expenditure functions from a fully specified random utility system. 

# Treatment of preferences

Preferences are modeled in the broadest possible way consistent with the paper’s goals. The heterogeneity term (\eta) may be vector-valued, of unknown dimension, and enter utilities in arbitrary ways. The paper emphasizes that restricting heterogeneity to a known scalar or known random-coefficient structure imposes strong and often hidden behavioral restrictions. 

A central message is that welfare identification does not require identification of the heterogeneity distribution itself. The paper even provides an example where the dimension and distribution of heterogeneity are not identified from choice probabilities, yet the welfare distributions remain point-identified. This is a methodological result of first-order importance. 

This is not a preference-respecting welfare theory in the Fleurbaey-Maniquet sense. Preferences matter because they generate heterogeneous EV and CV, but the welfare object remains conventional money-metric welfare under price change. 

# Treatment of opportunities / constraints

The paper does not model opportunities or constraints as first-class objects in the way your agenda requires. The feasible discrete alternatives are taken as given, and the analysis asks how price changes affect welfare through choice behavior. 

There is no latent job-offer process, no RURO structure, no rationing, and no explicit heterogeneous opportunity sets. The distinction between ordered and unordered choice is important, but it is a distinction about the data structure and price variation needed for welfare identification, not about labor-market opportunities. 

For your research direction, this means the paper is useful for welfare analysis conditional on a given discrete-choice environment, but it does not help separate preferences from opportunities. If the underlying choice model already conflates them, the welfare distributions derived here inherit that conflation. 

# Welfare / normative object

The welfare objects are equivalent variation and compensating variation, both at the distributional level and at the mean. The paper is explicitly about money-metric welfare from price changes in discrete-choice models. 

The paper is therefore normatively focused, but in the conventional applied-welfare sense rather than in a broader social-welfare or fairness-theoretic sense. It does not build a social welfare function over persons, except indirectly through averages of EV/CV or deadweight loss. Its concern is exact individual welfare compensation under heterogeneity. 

# Main findings

First, for binary and unordered multinomial choice, the marginal distributions of EV and CV are nonparametrically point-identified as simple closed-form functionals of choice probabilities, even under unrestricted unobserved heterogeneity and without specifying utility functional forms. This is the main theorem of the paper. 

Second, average EV for a price rise equals the change in average Marshallian consumer surplus, even when utility is not quasilinear in income. This is a strong and elegant result because it shows that a classic surplus formula survives beyond quasilinear utility in this discrete-choice setting. 

Third, for a normal good, average CV exceeds average EV for a price increase. This follows directly from the choice-probability expressions for the two welfare objects and the definition of normality. 

Fourth, the dimension and distribution of heterogeneity need not be known or identified for welfare identification. The paper stresses that this is not merely a technical convenience; it substantially broadens the set of admissible preference distributions. 

Fifth, nonparametric point identification fails for ordered choice with three or more alternatives if the same unit price applies across alternatives. Pages 18–23 and Figures 1–2 show this sharply. This is one of the paper’s most important conceptual findings because it marks a boundary of the nonparametric welfare approach. 

# Main limitations

A first limitation, relative to your research interests, is that the paper is not about labor supply, job choice, or opportunity sets. It is a welfare-identification paper for discrete choice under price changes. 

A second limitation is that the paper studies marginal distributions of EV and CV, not richer welfare objects such as joint welfare distributions, welfare ranks, or social welfare orderings across heterogeneous individuals. Later papers, including the 2021 Capéau et al. paper, go further in that direction. 

A third limitation is that the result is strongest for binary and unordered multinomial settings. Ordered-choice environments with uniform unit pricing break point identification, so the framework is not universally applicable across discrete-choice structures. 

A fourth limitation is that the analysis focuses on price changes of discrete goods. Quality changes, entry/exit of alternatives, and richer reforms are outside the paper’s main scope. 

# Relevance for my JMP

## possible use for framing

This paper is useful for framing a JMP that wants to avoid overreliance on parametric structural welfare calculations. It provides a clean methodological benchmark: some welfare objects can be read directly from choice probabilities without identifying the full preference distribution. 

## possible use for model design

If your project ends with a discrete-choice model over jobs, labor-supply states, or welfare-relevant alternatives, this paper suggests a way to build welfare calculations from the estimated choice probabilities rather than only from a tightly specified utility system. 

## possible use for identification

This is where the paper is strongest. It tells you precisely when welfare distributions are point-identified and when they are not. In particular, it warns that the structure of the choice problem itself matters for welfare identification. 

## possible use for welfare measurement

Highly useful. The paper gives exact, nonparametric formulas for EV and CV distributions and their means. It is one of the cleanest methodological references for money-metric welfare in discrete choice with heterogeneous preferences. 

## possible use for cross-country comparison

Indirectly useful. If comparable discrete-choice probabilities are available across countries, the formulas could in principle be used country by country. But the paper itself does not address cross-country comparability of opportunities, institutions, or welfare metrics. 

# Research questions this paper inspires

Can Bhattacharya-style nonparametric EV/CV formulas be adapted to a RURO or latent-job model in which the relevant choice probabilities already incorporate heterogeneous opportunities?

How much do policy welfare conclusions change when one replaces parametric structural labor-supply EV/CV calculations with Bhattacharya-style nonparametric welfare calculations?

What welfare objects remain point-identified once the choice problem is enlarged from unordered alternatives to richer ordered or quasi-continuous labor-supply environments?

Can one move from marginal EV/CV distributions to richer joint welfare distributions in a way that preserves the same nonparametric spirit? 

# Challenge to this paper

The strongest omission is that the paper identifies welfare effects without asking whether the underlying discrete alternatives themselves adequately represent the individual’s opportunity set. This is entirely appropriate for the paper’s purpose, but it means that the welfare analysis is only as credible as the underlying choice environment. A future paper could challenge this by combining Bhattacharya’s nonparametric welfare logic with an explicit model of heterogeneous opportunities. 

# Relation to Bargain et al. (2013)

The relation is methodological rather than direct. Bargain et al. (2013) is a structural labor-supply and welfare-comparison paper with a specific applied setting, whereas Bhattacharya (2015) is a theory paper showing that certain money-metric welfare distributions in discrete choice are identifiable without heavy parametric structure. Relative to Bargain et al., this paper is much stronger on nonparametric welfare identification and much weaker on labor-supply modeling, tax-benefit detail, and cross-country substantive application. For your corpus, it is best read as a methodological benchmark that can discipline later applied welfare analyses. 

# Relation to opportunities vs preferences

This paper is mainly about heterogeneous preferences, not about opportunities. It allows very flexible unobserved taste heterogeneity, but it takes the discrete choice set as given. As a result, it does not help disentangle welfare differences caused by preferences from welfare differences caused by unequal opportunity sets. It is therefore valuable for your welfare toolkit, but not a solution to the opportunities-versus-preferences problem itself. 

# Useful quotations / formulas

The central identification formulas are
[
\Pr(SEV\le a)=1-\bar q(p_0+a,y),
\qquad
\Pr(SCV\le a)=1-\bar q(p_0+a,y+a),
]
for (0\le a<p_1-p_0). These are the paper’s key results for binary choice. 

The corresponding average welfare formulas are
[
E(EV)=\int_{p_0}^{p_1}\bar q(p,y),dp,
\qquad
E(CV)=\int_{p_0}^{p_1}\bar q(p,y+p-p_0),dp.
]
These make clear why average EV coincides with the change in Marshallian consumer surplus. 

The ordered-versus-unordered distinction is also fundamental. The diagrams on pages 22–23 show why, in ordered choice with a common unit price, the relevant counterfactual choice probabilities needed for welfare are not observed, whereas in unordered choice with alternative-specific pricing they are. 

# Suggested tags

#nonparametric_welfare #discrete_choice #EV #CV #choice_probabilities #unobserved_heterogeneity #binary_choice #multinomial_choice #ordered_choice #consumer_surplus

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That in many discrete-choice settings, exact distributions of EV and CV are already encoded in the choice probabilities themselves—so the real question is not always how to parameterize preferences better, but whether the underlying choice environment is the right one for welfare analysis.
