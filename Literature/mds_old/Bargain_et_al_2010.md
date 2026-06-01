---

title: "Making work pay in a rationed labor market"
authors: ["Olivier Bargain", "Marco Caliendo", "Peter Haan", "Kristian Orsini"]
year: 2010
outlet: "Journal of Population Economics"
country_or_context: "Germany"
population: "Working-age singles and couples in Germany; analysis distinguishes single women, single men, couples with both spouses flexible, couples with only male flexible labor supply, and couples with only female flexible labor supply"
data_period: "2003 GSOEP wave, fiscal year 2002"
shelf: "making_work_pay_rationed_market"
tags: ["labor supply", "rationing", "involuntary unemployment", "double-hurdle", "tax-benefit reform", "Germany", "mini-job reform", "employment bonus", "structural model", "secondary earners"]
priority: "high"
read_status: "extracted"
------------------------

# Full citation

Bargain, Olivier, Marco Caliendo, Peter Haan, and Kristian Orsini. 2010. “Making work pay in a rationed labor market.” *Journal of Population Economics* 23(1): 323–351. 

# One-sentence contribution

The paper evaluates two German-style individualized in-work transfer reforms with a static structural labor supply model that explicitly incorporates involuntary unemployment through a double-hurdle framework, and shows that policies targeted at low wages outperform policies targeted at low earnings. 

# Why this paper matters

This paper matters because it combines two issues that are often treated separately: the design of “making work pay” reforms and the fact that observed non-employment may reflect rationing rather than voluntary leisure choice. The authors argue that ignoring demand-side constraints biases estimated labor supply elasticities and can materially distort ex ante policy evaluation in a country like Germany. 

For your potential JMP, the paper is useful as a bridge between structural labor supply, tax-benefit simulation, and constrained choice. It is not a latent-jobs or RURO paper, but it is one of the clearer examples where opportunities are not collapsed entirely into tastes: involuntary unemployment is modeled as a separate hurdle. It is also useful for thinking about how policy conclusions depend on whether one targets low earnings or low productivity. 

# Core research question

How do two alternative individualized “making work pay” reforms in Germany affect labor supply and employment when one explicitly accounts for involuntary unemployment and labor-market rationing, rather than assuming all non-employment is voluntarily chosen? 

# Economic setting and context

The setting is Germany in the early 2000s. The paper studies the 2003 mini-job reform and a hypothetical reform inspired by the Belgian Employment Bonus, both evaluated against the prereform German tax-benefit system. The broader policy question is how to design in-work transfers so that they increase employment without generating strong negative intensive-margin incentives, especially for secondary earners in couples. 

The mini-job reform extends exemptions from social security contributions for low monthly earnings and removes the previous 15-hour weekly limit, but remains conditional on low earnings. The Employment Bonus instead conditions support on low wages, expressed in full-time-equivalent earnings, and is designed to distinguish low productivity from low effort. The paper repeatedly contrasts these individualized reforms with family-based tax credits such as the US EITC and UK WTC, which create negative work incentives for secondary earners because eligibility depends on family income. 

# Model / theoretical framework

The model is a static structural household labor supply model with discrete hours choices, combined with a demand-side rationing equation. In the unconstrained benchmark, households choose among discrete hours alternatives by utility maximization over leisure and disposable income. In the constrained specification, this is augmented by a latent involuntary-unemployment equation, yielding a double-hurdle model. 

The choice object is a discrete hours category. For singles, the model selects among six choices: 0, [0,12], ]12,20], ]20,34], ]34,40], and >40 hours. For couples where both spouses are flexible, choices are joint combinations of spouses’ discrete hours, giving 36 household alternatives. Couples with only one flexible spouse are handled in a male- or female-chauvinist framework in which the other spouse’s labor supply is fixed. 

The feasible set is therefore not modeled as a latent set of jobs or offers. Rather, the key non-preference constraint is employment rationing: after a household decides whether and how much it would like to work, a second hurdle determines whether the individual is involuntarily unemployed. The framework is positive with policy applications, not a normative welfare-ranking model. 

# Key objects

The core behavioral objects are utility over disposable income and leisure, discrete hours-choice probabilities, labor supply elasticities, and transition predictions under alternative tax-benefit rules. The main tax-policy objects are the mini-job reform and the Employment Bonus reform. 

The central constraint object is the latent involuntary-unemployment indicator
[
I_i^*=\beta X_i+\eta_i,
]
modeled as a probit-type rationing equation. This equation determines the risk of demand-side unemployment separately from the labor supply choice equation. 

The main reform-evaluation objects are changes in participation, total hours in full-time equivalents, extensive- and intensive-margin decompositions, and the share of newly rationed workers among new labor-market entrants after reform. 

# Data

The paper uses the 2003 wave of the German Socio-Economic Panel (GSOEP), containing information for fiscal year 2002. The estimation sample excludes the self-employed, retired individuals, disabled persons, those on maternity leave, and those in full-time education. 

The sample is partitioned into five groups: 1,022 single women, 783 single men, 3,822 couples where both spouses have flexible labor supply, 970 couples where only the woman has flexible labor supply, and 562 couples where only the man has flexible labor supply. The paper models these groups separately because both preferences and rationing risks differ across them. 

The main variables include working hours, hourly wages, education, age, children, East/West Germany, region, and past employment history. For the rationing equation, the authors also use local labor-market conditions based on labor office district clusters and information on job search and readiness to work. 

# Identification logic

Identification of involuntary unemployment relies on two survey questions: whether the individual actively searched for a job in the last four weeks, and whether the individual is ready to take up a job within the next two weeks. Individuals answering both positively are classified as involuntarily unemployed, following the ILO logic. This provides the empirical basis for the rationing hurdle. 

The probability of rationing is identified with regional demand-side variables and individual characteristics. The regional side uses a five-cluster classification of labor office districts, ordered by labor-market tightness, with East Germany and weak labor markets showing substantially higher involuntary-unemployment rates. The individual side uses education and lagged employment-status indicators, which are significant predictors of rationing risk. 

Identification of labor supply then comes from the standard structural variation in the nonlinear German tax-benefit system combined with the discrete-choice structure. The paper also uses information on desired part-time versus full-time work among the involuntarily unemployed to sharpen identification of preferences. A key maintained assumption is independence between the utility error terms and the rationing error term, so the two hurdles can be estimated separately. 

# Estimation / empirical strategy

The unconstrained model is a standard discrete-choice structural labor supply model with extreme-value errors, estimated separately for singles and for different couple types. The constrained model adds the rationing probit and derives a joint double-hurdle likelihood. 

The utility function is specified quadratically in leisure and disposable income, with taste shifters depending on age, number and age of children, and region. Dummy variables for part-time categories are included to capture specific utility or disutility associated with part-time work. Tax-benefit microsimulation is used to compute disposable income at each hours point. 

Policy effects are then simulated under both the unconstrained and constrained models. The paper computes participation changes and total-hours changes, decomposed into intensive and extensive margins, and shows how ignoring rationing leads to biased predictions. 

# Treatment of preferences

Preferences are modeled over disposable income and leisure in a standard structural labor supply way, with coefficients varying by household characteristics. The presence of young children raises women’s preference for leisure, East German women appear to have lower preferences for nonmarket time, and part-time categories carry specific utility effects. 

However, the paper’s main conceptual move is not to enrich preference heterogeneity but to prevent constraints from being misread as preferences. The authors explicitly argue that unconstrained estimation produces a “triple bias”: misspecification, erroneous freedom of choice, and overstatement of the taste for leisure. In that sense, preferences are important but they are not allowed to absorb all non-employment. 

This is not a preference-respecting normative paper. Preferences are purely behavioral objects, not welfare-comparison objects. 

# Treatment of opportunities / constraints

This is the most important section for your agenda.

The paper does not model a job opportunity set in the RURO or latent-jobs sense. It does, however, model one important constraint explicitly: involuntary unemployment due to demand-side rationing. That already marks a sharp departure from pure supply-side labor supply models in which all non-employment is treated as chosen. 

The opportunity side is therefore represented as a latent employment hurdle rather than as a rich set of feasible jobs. Conditional on being able to work, individuals choose among discrete hours categories in the usual way. So the paper separates preferences from one constraint margin—access to employment—but not from richer opportunity heterogeneity over hours, wages, occupations, or job amenities. 

Relative to your agenda, this makes the paper valuable but limited. It is valuable because it demonstrates concretely that ignoring constraints biases elasticities and reform predictions. It is limited because the feasible set is still not modeled as an explicit job-opportunity set. 

# Welfare / normative object

There is no formal welfare metric such as equivalent income, compensating variation, or a social welfare function. The paper is positive with policy-design implications. It evaluates reforms through employment, hours, and cost-efficiency rather than through an explicit welfare ranking. 

The normative language is practical rather than formal. The authors discuss the “efficiency” of individualized transfers, the design of wage-targeted versus earnings-targeted support, and the danger of part-time traps, but not a deeper theory of well-being or social evaluation. 

# Main findings

First, the paper finds that individualized wage-targeted support performs better than individualized earnings-targeted support. The Employment Bonus generates substantially larger employment effects than the mini-job reform and avoids the negative intensive-margin effects created by earnings-conditioned support. 

Second, the mini-job reform has only a modest positive participation effect and can reduce total labor supply once intensive-margin contractions are accounted for. Under the constrained model, it creates about 43,000 additional participants but reduces total labor supply by about 11,000 FTE overall; the unconstrained model predicts a smaller net reduction of about 4,000 FTE. This reflects the part-time trap created by targeting low earnings. 

Third, the Employment Bonus has much larger positive effects. Under the constrained model it generates about 159,000 new participants and about 211,000 additional FTE, compared with about 295,000 and 339,000 under the unconstrained model. So the positive employment case for the reform remains, but the unconstrained model substantially overstates it. 

Fourth, ignoring rationing biases labor supply elasticities and policy predictions. The authors characterize a triple bias in unconstrained estimation and show that the participation bias usually dominates, leading unconstrained models to overstate employment responses, especially for groups with more involuntary unemployment such as singles and men in couples. 

Fifth, the discrepancy between constrained and unconstrained prediction is small when reform effects are minor and concentrated on voluntarily inactive secondary earners, as with the mini-job reform, but becomes large when reforms activate groups more exposed to rationing, as with the Employment Bonus. For the latter, the unconstrained model overstates employment effects by about 60%. 

Sixth, the paper’s cost-efficiency comparison also favors the Employment Bonus. Using constrained-model simulations, the implied unit cost per new entrant is much lower for the Employment Bonus than for the mini-job reform. 

# Main limitations

A first limitation is that the paper models opportunities only through an involuntary-unemployment hurdle. It does not model restricted hours offers, wage-offer distributions, latent jobs, or richer opportunity sets. Relative to your interests, this is a major limitation. 

A second limitation is the partial-equilibrium treatment of rationing. The authors hold individual rationing probabilities fixed under reform because the rationing equation is reduced-form. So the analysis cannot capture endogenous labor demand, vacancy creation, or wage adjustments. 

A third limitation is the static structure. Search costs, duration dependence, and dynamic transitions are not modeled structurally, even though the authors acknowledge discouragement and other dynamic issues. 

A fourth limitation is normative thinness. The paper gives strong policy-design conclusions without an explicit welfare object, so its “efficiency” claims are ultimately employment- and cost-based rather than grounded in a formal welfare criterion. 

# Relevance for my JMP

## possible use for framing

This paper is very useful for framing a project that insists policy evaluation should not assume all non-employment is voluntary. It gives you a concrete empirical example where ignoring constraints changes the policy conclusion materially. 

## possible use for model design

It is useful as an intermediate design reference. If you want to move from standard structural labor supply toward opportunity-sensitive models, this paper shows one tractable way to introduce a demand-side constraint without yet specifying a full job-offer process. 

## possible use for identification

The paper is useful because it combines survey information on unemployment status, regional labor-market indicators, and structural tax-benefit variation to identify rationing separately from preferences. That is directly relevant to your concern that preferences and opportunities should not be conflated. 

## possible use for welfare measurement

Indirectly useful. It shows that any welfare or policy evaluation built on pure supply-side labor supply may be biased if involuntary unemployment is present. But it leaves the welfare metric itself open. 

## possible use for cross-country comparison

It is relevant for cross-country work because it highlights that labor-market rationing differs across institutional settings. Germany’s stronger demand-side constraints are one reason why constrained and unconstrained policy evaluations diverge. That warns against transporting results from less rationed economies too mechanically. 

# Research questions this paper inspires

How much of the cross-country difference in estimated labor supply elasticities is due to different degrees of involuntary unemployment rather than differences in preferences?

Would the relative superiority of wage-targeted over earnings-targeted in-work transfers survive in a model with explicit latent job opportunities rather than a reduced-form rationing hurdle?

How do employment effects of in-work transfers change when rationing probabilities are endogenized through labor demand rather than held fixed?

Can one integrate this paper’s double-hurdle treatment of involuntary unemployment with a richer opportunity-set model over hours, wages, and job characteristics? 

# Challenge to this paper

The strongest simplification is that rationing is modeled as a binary access constraint rather than as a structured opportunity set. This is enough to show that pure supply-side models are inadequate, but not enough to say which jobs, hours, or wage-hours packages are actually available. A future paper could challenge this by replacing the reduced-form unemployment hurdle with an explicit job-opportunity process. 

# Relation to Bargain et al. (2013)

This paper is an earlier and behaviorally more labor-market-constrained contribution than Bargain et al. (2013). The 2010 paper is about tax-transfer design and the consequences of rationing for labor supply estimation and policy evaluation; the later 2013 paper moves toward welfare comparison under heterogeneous preferences. In that sense, the 2010 paper is stronger on the presence of labor-market constraints, while the 2013 paper is more directly relevant for welfare ranking. For your agenda, the two papers are complementary: this one disciplines the positive model by admitting rationing, while the later one is closer to the normative layer. 

# Relation to opportunities vs preferences

This paper partially helps separate preferences from opportunities. It rejects the view that observed non-employment is simply taste for leisure and instead introduces involuntary unemployment as a distinct demand-side constraint. That is an important step. But opportunities are represented only coarsely, as access to employment, not as a structured set of job opportunities. So it moves in the right direction without fully reaching the opportunity-set perspective you are interested in. 

# Useful quotations / formulas

The key rationing equation is
[
I_i^*=\beta X_i+\eta_i,
]
which is the central formal representation of involuntary unemployment in the paper. It is the main formula capturing the opportunity side. 

The discrete-choice utility representation is
[
V_{ij}=U(L_{fij},L_{mij},C_{ij},Z_i)+\varepsilon_{ij},
]
with standard multinomial logit probabilities in the unconstrained case. This is the behavioral backbone of the model. 

A short statement of the main methodological message is that ignoring involuntary unemployment leads to a “triple bias”: misspecification, erroneous freedom of choice, and overstatement of the taste for leisure. That is the paper’s most concise characterization of why unconstrained policy evaluation can go wrong. 

# Suggested tags

#labor_supply #rationing #involuntary_unemployment #double_hurdle #taxbenefit #Germany #mini_jobs #employment_bonus #structural_model #making_work_pay

# My quick takeaway

If I only remember one thing from this paper for my JMP, what should it be? That a policy conclusion about “making work pay” can look very different once non-employment is treated as partly constrained rather than fully chosen—and that wage-targeted support is much cleaner than earnings-targeted support when the goal is to raise employment without creating a part-time trap.
