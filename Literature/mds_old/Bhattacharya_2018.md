---

title: "Empirical welfare analysis for discrete choice: Some general results"
authors: ["Debopam Bhattacharya"]
year: 2018
outlet: "Quantitative Economics"
country_or_context: "General methodological paper with an empirical illustration on recreational fishing-mode choice in Southern California"
population: "General multinomial discrete-choice setting; empirical illustration uses 1,182 recreational fishers choosing among beach, pier, private-boat, and charter-boat fishing"
data_period: "[unclear from paper]"
shelf: "empirical_discrete_choice_welfare_general"
tags: ["discrete choice", "welfare analysis", "compensating variation", "equivalent variation", "multiple price changes", "elimination of alternatives", "quality change", "nonexclusive choice", "deadweight loss", "program evaluation"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bhattacharya, Debopam. 2018. “Empirical welfare analysis for discrete choice: Some general results.” *Quantitative Economics* 9: 571–615. 

# One-sentence contribution

The paper develops nonparametric welfare methods for multinomial discrete choice under unrestricted heterogeneity, showing when distributions of Hicksian welfare effects are point-identified from structural choice probabilities and when they are only set-identified. 

# Why this paper matters

This paper matters because it takes the 2015 Bhattacharya result for a single price change and extends it to more realistic policy environments: simultaneous price changes, introduction or elimination of alternatives, quality changes, and nonexclusive choice. It is therefore much closer to actual empirical policy evaluation than the simpler earlier result. 

For your potential JMP, the paper is highly relevant on the welfare side. It does not solve the opportunity-set problem, but it gives a flexible welfare-analysis toolkit for discrete-choice environments with heterogeneous preferences and nontrivial income effects. That is especially useful if your eventual behavioral model is not quasilinear and you want to evaluate policy changes in money-metric terms without relying entirely on logsum formulas or tight parametric structure. 

# Core research question

How can one conduct empirical welfare analysis for multinomial discrete choice under unrestricted heterogeneity and income effects in practically important scenarios such as multiple simultaneous price changes, elimination or introduction of an option, quality changes, and nonexclusive alternatives? 

# Economic setting and context

The paper is mainly methodological. Its motivating applications include tuition subsidies, health-product subsidies, transport choice, and other policy interventions where researchers usually report uncompensated outcome changes but not compensated welfare effects such as cash-equivalent benefits or deadweight loss. 

The empirical illustration uses recreational fishing-mode choice in Southern California. Individuals choose among beach, pier, private-boat, and charter-boat fishing, with observed prices, income, and catch rates. The paper uses this application to show how its nonparametric welfare calculations differ from standard logsum-based calculations. 

# Model / theoretical framework

The model class is a multinomial discrete-choice random utility framework with unrestricted unobserved heterogeneity. Utility from choosing alternative (j) is written as (U_j(Y-P_j,\eta)), where (Y) is income, (P_j) is the price of alternative (j), and (\eta) is unobserved heterogeneity of unknown dimension. The structural choice probabilities are
[
q_j(p,y)=\int 1!\left{U_j(y-p_j,r)>\max_{k\neq j}U_k(y-p_k,r)\right},dF_\eta(r).
]
This is the central positive object from which welfare results are derived. 

The paper studies four environments. First, simultaneous price changes of multiple exclusive alternatives. Second, elimination or introduction of an alternative, possibly with induced price changes in the remaining alternatives. Third, changes in characteristics or quality of an alternative, possibly with an accompanying price change. Fourth, multinomial choice with nonexclusive options. 

The framework is explicitly welfare-oriented. Hicksian EV and CV are the main objects. A key conceptual result is that, with multiple price changes, Hicksian welfare remains well-defined while the analog of Marshallian consumer surplus becomes path-dependent. 

# Key objects

The main objects are structural choice probabilities (q_j(p,y)), distributions of individual EV and CV, average Hicksian welfare, and deadweight loss. The paper also studies “compensated program effects,” defined as the program’s cash-equivalent value to individuals. 

A second key object is the distinction between point identification and set identification. For multiple price changes and elimination of alternatives, welfare distributions are point-identified from structural choice probabilities. For quality changes and nonexclusive choice, welfare distributions are generally not point-identified, but bounds can be constructed. 

In the empirical illustration, the main outcome objects are average CV from multiple price changes, welfare loss from eliminating private-boat or charter-boat fishing, and welfare loss from a deterioration in the catch rate of beach fishing. Figures 1–4 and Table 2 summarize these. 

# Data

The empirical application uses a cross section of 1,182 individuals choosing among four fishing modes in Southern California: beach, pier, private boat, and charter boat. The paper records the chosen mode, monthly income, the price of each alternative faced by the individual, and the catch rate associated with each alternative. The price variables mainly reflect travel costs to the fishing site. Table 1 reports the summary statistics. 

Mean monthly income in the sample is about $5,250, and the mean prices are roughly $103 for beach and pier, $55 for private boat, and $84 for charter boat. Mean catch rates differ substantially across alternatives, with charter boat having the highest average catch rate. The application keeps some characteristics at mean values when plotting welfare by income. 

# Identification logic

The paper’s identification logic is built around structural choice probabilities rather than parametric utility recovery. The key claim is that in some economically important discrete-choice settings, the distributions of Hicksian welfare are exact functionals of the (q_j(p,y)). Once these structural choice probabilities are identified or estimated, welfare objects follow directly. 

For simultaneous price changes of multiple exclusive alternatives, the paper proves that EV and CV distributions are point-identified even though Marshallian consumer surplus is path-dependent and even though one cannot simply iterate the earlier single-price-change result. The reason is that after the first step of an iterative decomposition, the relevant income level becomes individually heterogeneous and unobserved, so a fresh theorem is needed. 

For elimination of an alternative, the paper formalizes the heuristic idea that product elimination can be viewed as a price going to infinity, but shows carefully what can and cannot be learned. The EV and CV distributions are again obtainable from choice probabilities, though tail calculation may require observing very high prices or else settling for lower bounds. 

For quality change and nonexclusive alternatives, point identification fails in general. The paper constructs nonparametric bounds instead. It also shows that additional preference structure, such as weak separability, can restore point identification in the quality-change case. 

# Estimation / empirical strategy

The theory sections are analytical. The practical strategy is: estimate structural choice probabilities, then plug them into the welfare formulas. The paper emphasizes that this can be done nonparametrically using kernel or series methods, or via flexible approximations if data are limited. 

In the fishing application, each alternative’s choice probability is approximated with a partially linear specification,
[
q_j(p,y,x)=h_j(y-p_j)+x^\prime\beta_j+(y1_{-j}-p_{-j})^\prime\gamma_j,
]
where (h_j) is a cubic in own net income, (x) collects catch rates, and the remaining alternatives’ net incomes enter linearly. This is used as a series/sieve-style approximation rather than as a deeply structural utility specification. 

The paper then compares the resulting welfare calculations to standard logsum calculations under quasilinear-type assumptions. Bootstrapped confidence intervals are reported for selected average welfare measures in Table 2. 

# Treatment of preferences

Preferences are modeled nonparametrically and very flexibly. The paper does not specify the dimension of heterogeneity, the distribution of heterogeneity, or the functional form of utility beyond continuity and monotonicity in the numeraire. This is one of the paper’s main strengths. 

The paper’s methodological stance is that welfare analysis should not require identification of the entire preference distribution. Structural choice probabilities already contain the relevant information for many welfare questions. In that sense, the paper treats preference heterogeneity seriously while avoiding strong parametric commitments. 

However, the paper is not about fairness-sensitive heterogeneity or responsibility-sensitive welfare. Preferences are heterogeneous, but the welfare objects remain Hicksian money-metric objects. 

# Treatment of opportunities / constraints

This is not an opportunities paper in the RURO or latent-job sense. The paper takes the discrete alternatives as given and studies how economic changes affecting those alternatives map into welfare. The “introduction/elimination of an option” results are about changes in the choice environment, but not about endogenous or heterogeneous opportunity sets in the labor-market sense. 

The nonexclusive-choice section is relevant to the structure of feasible choice, but again in a combinatorial choice-set sense, not as a model of rationing, job offers, or demand-side constraints. The paper is therefore highly relevant for welfare analysis conditional on a given discrete-choice environment, but not for separating preferences from opportunities. 

For your agenda, this means the paper is best viewed as a welfare-calculus extension that could sit on top of a richer model of opportunities, rather than as a substitute for such a model. 

# Welfare / normative object

The welfare objects are Hicksian: EV, CV, and deadweight loss. The paper is explicitly normative in the applied welfare sense and repeatedly emphasizes compensated program effects and cash-equivalent valuations of policy changes. 

A core conceptual result is that Hicksian welfare remains well-defined in settings where Marshallian consumer surplus becomes path-dependent. This is one of the paper’s most important theoretical contributions. 

The paper is not a social welfare or fairness paper. It works at the level of individual money-metric welfare and aggregates primarily through averages and deadweight-loss calculations, rather than through an explicit social welfare function. 

# Main findings

First, for simultaneous price changes of multiple exclusive alternatives, individual EV and CV distributions are point-identified from structural choice probabilities under unrestricted heterogeneity and income effects. This generalizes the 2015 single-price-change result in a nontrivial way. 

Second, for multiple price changes, Marshallian consumer surplus is path-dependent, but Hicksian welfare is still well-defined. This is a major conceptual clarification for applied welfare analysis. 

Third, elimination or introduction of an alternative also yields point-identified Hicksian welfare distributions from choice probabilities, though in practice one may only get lower bounds on average welfare if demand at very high prices is not observed. 

Fourth, for quality changes and nonexclusive-choice settings, welfare distributions are generally not point-identified from structural choice probabilities alone. The paper derives nonparametric bounds instead, and shows that additional restrictions such as weak separability can restore point identification in the quality-change case. 

Fifth, the paper makes a useful endogeneity point: under income endogeneity, for a price rise, the EV distribution at realized income is not affected by income endogeneity, whereas the CV distribution is. This gives researchers a legitimate welfare object even when income exogeneity is doubtful and no instrument is available. 

Sixth, in the fishing application, nonparametric welfare estimates differ sharply from logsum estimates. According to Figure 1 on page 24, for a specific multiple-price-change experiment, the paper’s estimates are much larger and increase slightly with income, whereas the logsum estimates are smaller and slope downward with income. 

Seventh, the elimination experiments also show large substantive differences. Figure 2 on page 25 indicates that, relative to logsum estimates, the paper’s estimates are much lower for eliminating the private-boat option and much higher for eliminating the charter-boat option. Figure 3 further shows that both eliminations generate large private welfare losses, on the order of roughly 10% of monthly income in the illustration. 

Eighth, Table 2 on page 27 reports mean welfare losses at mean income of about $4,000: $42.57 for the multiple-price-change exercise, $536.37 for eliminating private-boat fishing, $588.16 for eliminating charter-boat fishing, and an upper-bound loss of $7.05 for the catch-rate deterioration exercise. The corresponding logsum numbers are $19.21, $1212.4, $280.29, and $4.68, respectively. 

# Main limitations

A first limitation, relative to your research direction, is that the paper treats the choice environment as given. It does not model heterogeneous opportunity sets, labor-market frictions, job offers, or rationing. 

A second limitation is that some practically important settings remain only partially identified. Quality changes and nonexclusive choice require bounds unless further preference restrictions are imposed. 

A third limitation is that empirical implementation still requires good estimates of structural choice probabilities over relevant price-income ranges. In elimination problems, the tails may be hard to learn nonparametrically if data do not include very high prices. 

A fourth limitation is that the empirical illustration is small and highly specific. It is useful as proof of concept, but it is not a broad validation exercise across many policy environments. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a JMP that wants to evaluate policy changes in welfare terms without relying mechanically on logsum calculations or quasilinear utility. It gives a strong methodological justification for richer welfare analysis in discrete-choice settings. 

## possible use for model design

It is useful if your final model is a discrete-choice labor-supply or job-choice model and you want to evaluate reforms involving multiple simultaneous changes, introduction or removal of options, or quality changes. This paper shows how the welfare layer changes across those cases. 

## possible use for identification

This is one of the paper’s strongest contributions for your project. It tells you which welfare objects are point-identified and which are only bounded under general heterogeneity. That is directly relevant if you want to be explicit about what your model can and cannot recover. 

## possible use for welfare measurement

Highly useful. The paper extends nonparametric Hicksian welfare analysis to several settings that are much closer to actual policy design than a single-price-change environment. It is especially valuable for cash-equivalent program valuation and deadweight-loss analysis. 

## possible use for cross-country comparison

Potentially useful if you estimate comparable discrete-choice systems across countries and want to evaluate similar reforms. But the paper does not solve cross-country comparability of opportunity sets or institutions; it only provides the welfare mechanics conditional on the estimated choice environment. 

# Research questions this paper inspires

Can Bhattacharya’s nonparametric welfare formulas for multiple price changes be embedded in a labor-supply model with explicit latent job opportunities rather than a fixed discrete choice environment?

How much do structural welfare conclusions about tax-benefit reforms change when one moves from logsum-based calculations to Bhattacharya-style nonparametric Hicksian welfare calculations?

In labor-supply settings with hours restrictions or RURO opportunity sets, which policy changes remain point-identified in welfare terms and which become only set-identified?

Can one combine this paper’s compensated program-effect framework with a preference-versus-opportunity decomposition so that welfare losses are attributed separately to prices, preferences, and choice-set deprivation? 

# Challenge to this paper

The strongest unresolved issue is that the paper provides a sophisticated welfare layer without endogenizing or structurally modeling the availability of alternatives themselves. This is entirely consistent with the paper’s objective, but it means the welfare analysis remains conditional on a potentially misspecified choice environment. A future paper could challenge it by integrating these nonparametric Hicksian methods with a structural model of heterogeneous opportunities. 

# Relation to Bargain et al. (2013)

The relation is methodological and complementary. Bargain et al. (2013) is a structural labor-supply and welfare-comparison paper with a specific substantive application, while Bhattacharya (2018) develops nonparametric Hicksian welfare tools for general discrete-choice environments. Relative to Bargain et al., this paper is much stronger on robustness of welfare identification and much weaker on labor-supply structure, household behavior, and institutional detail. For your corpus, it is a methodological welfare reference rather than a benchmark substantive labor-supply paper. 

# Relation to opportunities vs preferences

This paper mainly refines welfare analysis under rich preference heterogeneity, not the separation of preferences from opportunities. It treats the feasible alternatives as given. Therefore, if a behavioral model already conflates poor opportunities with preferences, the welfare calculations here inherit that conflation. It is very useful once the behavioral environment is credible, but it does not by itself solve the opportunities-versus-preferences problem central to your agenda. 

# Useful quotations / formulas

The paper’s key multiple-price-change result is that the marginal EV and CV distributions can be written as piecewise sums of structural choice probabilities. The exact formula depends on the ranking of price changes across alternatives, but the principle is that Hicksian welfare remains a closed-form functional of the (q_j)’s even when several prices move at once. 

For elimination of an alternative with no price change in remaining alternatives, the paper shows
[
E(CV)=\int_{p_{J+1}}^\infty q_{J+1}(p_{10},\ldots,p_{J0},r,y+r-p_{J+1}),dr,
]
and
[
E(EV)=\int_{p_{J+1}}^\infty q_{J+1}(p_{10},\ldots,p_{J0},r,y),dr.
]
These formulas formalize the common heuristic that eliminating an alternative is like sending its price to infinity, but they also show the difference between CV and EV. 

The fishing application is also instructive visually. Figure 1 on page 24, Figures 2–3 on page 25, and Figure 4 on page 27 show that the nonparametric welfare estimates can differ sharply from logsum estimates not only in magnitude but also in the sign of their income gradient. That is an especially important practical warning. 

# Suggested tags

#discrete_choice #welfare_analysis #compensating_variation #equivalent_variation #multiple_price_changes #elimination_of_alternatives #quality_change #nonexclusive_choice #deadweight_loss #program_evaluation

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That once you move beyond a single-price-change toy problem, welfare analysis in discrete choice becomes much more subtle—but many important Hicksian welfare objects are still recoverable from choice probabilities without committing to heavy parametric structure, and standard logsum calculations can be very misleading.
