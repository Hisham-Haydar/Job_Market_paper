# J Popul Econ (2012) 25:741–761

DOI 10.1007/s00148-010-0331-y

## ORIGINAL PAPER

Accounting for family background when designing optimal income taxes: a microeconometric simulation analysis

Rolf Aaberge · Ugo Colombino Received: 8 January 2009 / Accepted: 1 July 2010 / Published online: 14 September 2010 Abstract We develop an extended version of Roemer’s Equality of Opportunity (EOp) criterion that accounts for income differentials between as well as within types, where types are defined by circumstances that are beyond people’s control (parental education, in this study). A microeconometric model of labour supply in Italy is employed to identify income tax-transfer rules that are optimal according to the extended EOp criterion. Overall, the results do not conform to the perhaps common expectation that the more conventional Equality of Outcome criterion is more supportive of “interventionist” (redistributive) policies than the EOp approach.

Keywords Equality of opportunity · Equality of outcome ·

Optimal income taxation

JEL Classification D63 · H21 · H31

Responsible editor: Christian Dustmann Electronic supplementary material The online version of this article (doi:10.1007/s00148-010-0331-y) contains supplementary material, which is available to authorized users. R. Aaberge Research Department, Statistics Norway, P.O. Box 8131 Dep, 0033 Oslo, Norway U. Colombino (B) Collegio Carlo Alberto, Via Real Collegio 30, 10124 Moncalieri, Italy e-mail: ugo.colombino@unito.it There is large research evidence regarding the impact of family background (e.g. parental education and/or income) on the economic success or, more generally, the level of well-being attained by the off-spring. The hypotheses on the channels through which the effect takes place can vary, but the existence of the effect itself is well-established. 1 In the terminology used in Roemer’s theory of Equality of Opportunity (EOp), 2 family background belongs to the category of the “circumstances”, i.e. something beyond the individual’s control. The EOp criterion is interesting from the policy point-of-view, since the majority of citizens in most industrialised countries, although not unfavourable to redistribution, seem sensitive to the way a certain outcome has been attained. If the level of well-being attained by a given individual is seen as depending on her circumstances (such as family background) and her own effort, the policies inspired by the EOp criterion should account for the impact of the part of well-being attributable to circumstances (rather than to effort) on the distribution of well-being. In contrast, the policies inspired by the criterion of equality of achievement or Equality of Outcome (EO) should care about the distribution of well-being irrespective of whether inequality is originated by circumstances or by effort. Although the EOp criterion does not necessarily imply less redistribution than the EO criterion, redistribution is more likely to receive support if it is designed to correct circumstances that are beyond people’s control. Instead, if a bad outcome is associated with a lack of effort, redistribution is likely to be much less acceptable. In designing EOp-inspired mechanisms, besides direct interventions such as targeted income support, educational services etc. one can also consider indirect policies such as income taxation. In this paper, we address the following question: What is the optimal income tax-transfer rule from the EOp perspective? More specifically, we present an empirical analysis of second-best optimal income taxation, adopting EOp as the evaluation criterion. The main purpose of this paper is to explore the implications of adopting the EOp criterion for the design of tax-transfer systems as compared to the EO criterion. A secondary purpose is to extend a previous contribution (Roemer et al. 2003), where the EOp criterion has been applied to evaluate the performance of current income tax rules in various countries, using a relatively simple common model of labour supply behaviour with calibrated parameters. The present paper extends the previous study in several respects. First, instead of evaluating the current tax rules, we wish to determine the second-best optimal income tax rules (according to the EOp perspective). As in Mirrlees (1971), second-best optimality means that we limit ourselves to tax-transfer rules that depend only on income i.e. we assume that individualspecific lump-sum taxes are not feasible, nor can the tax-transfer rule depend

1 Behrman

2 Roemer et al. (1999), Ermisch and Francesconi (2001), Sacerdote (2002), Dustmann (2004) (1998) Accounting for family background when designing optimal income on (observable) circumstances or “types”. Our aim consists of identifying the tax-transfers rule that best conforms to the EOp criterion, assuming that the rule depends only on income. There are many examples in tax policy analysis or design where a similar second-best perspective in adopted. For example, it is frequently asked whether the tax rule is more or less favourable to men rather than to women, to singles rather than to couples, to the young rather than to the elderly etc., even though the (actual or perspective) tax rule does not (directly) depend on those characteristics. Second, we introduce an extended version of pure-EOp criterion of Roemer (1998), which can be considered as a combination of the pure EOp criterion and the more traditional EO criterion. Third, we employ a relatively sophisticated model of labour supply that provides a simultaneous treatment of partners’ decisions and accounts for quantity constraints on the distribution of hours. Finally, while the analysis in Roemer et al. (2003) only concerned male heads of household 25–40 years old, this study deals with approximately the entire labour force. Whilst most tax evaluations are either based on representative agent models or micro-econometric models for single individuals or married females conditional on husbands’ income, this study relies on models for both married couples and single individuals. With respect to the traditional literature on optimal taxation, our contribution differs in two ways. First, while we share the same aim of identifying second-best tax-transfer rule, the social welfare function to be maximized is based on the EOp criterion instead of the EO criterion. Second, we solve the optimization problem computationally (i.e. by iteratively simulating a microeconometric model) rather than analytically. 3 In Section 2, we discuss the justification and definition of the EOp criterion and its relationship to more traditional concepts of social welfare such as the EO criterion. In the same section, we also introduce and motivate the extended EOp criterion. In Section 3.1, we use a micro-econometric model of household labour supply, estimated on 1993 Italian data, to simulate the effects of various constant-revenue “affine” tax-transfer rules, i.e. rules defined by a universal lump-sum transfer (positive or negative) and a constant marginal tax rate that produces the same revenue collected with the observed 1993 rule. These tax rules are evaluated and compared according to the extended EOp criterion. Furthermore, the EOp-optimal tax rule is also identified. The main reason to perform the exercise with the affine tax rules is to make our results (obtained with a very detailed microeconometric model) comparable to those reported in Roemer et al. (2003) (obtained with a simple theoretical model and calibrated parameters). In fact, in Section 3.2, we

3 The computational approach to designing optimal taxes is also adopted in Aaberge and

Colombino (2008).

perform a similar exercise as in Section 3.1, but looking at the class of tax rules defined by a transfer and two tax rates (instead of one as for the affine rules). In Section 4, we compare the evaluation of tax rules according the EOp and EO criteria. Since it, in many cases, turns out that the optimal tax rule is a universal lump-sum tax, and since lump-sum taxes are typically judged hard to implement and to support politically, in Section 5, we provide optimal tax rules under the constraint that lump-sum taxes are not allowed. Section 6 summarises the main results. The Electronic Supplementary Material illustrates the microeconometric model, the dataset used, the estimates and the the 1993 tax rule.

2 The EO and EOp criteria The standard approach in evaluating tax systems is to employ a social objective (welfare) function as the basic evaluating instrument. This function is commonly used to summarise the changes in (adult equivalent) incomes resulting from introducing various alternatives to the actual tax system in a country. The simplest way to summarise the changes that take place is to add up the income differentials, implying that individuals are given equal welfare weights independently of whether they are poor or rich. However, if besides total welfare we also care about the distributional consequences of a tax system, then an alternative to the linear additive welfare function is required. In this paper, we rely on the class of rank-dependent social welfare functions that originates from Mehran (1976) and are defined by 1

## W =

p (t) F −1 (t) dt, (2.1) 0 where F is the cumulative distribution function of (adult equivalent) income with mean μ, F −1 (t) is its inverse (i.e. the income of the individual located at the tth quantile) and p(t) is a positive weight-function defined on the unit interval. As demonstrated by Yaari (1988), the social welfare function (2.1) can be given a normative justification as it is made for the social welfare function introduced by Atkinson (1970). 4 In this paper, we use the following specification of p(t):

⎧ ⎨ − log t, k = 1 k p k (t) = (2.2) k−1 ⎩ 1 − t , k = 2, 3,....

k − 1 Note that the inequality aversion exhibited by the social welfare function W k associated with p k (t) decreases with increasing k. As k → ∞, W k approaches

4 Several other authors have discussed rationales for this approach, see e.g. Sen (1974), Hey and Lambert (1980), Donaldson and Weymark (1980, 1983), Weymark (1981), Ben Porath and Gilboa (1994) and Aaberge (2001).

Accounting for family background when designing optimal income inequality neutrality and coincides with the linear additive welfare function defined by 1

## W ∞ =

F −1 (t) dt = μ.

(2.3) 0 It follows by straightforward calculations that W k ≤ μ for all j and that W k is equal to the mean μ for finite k if and only if F is the egalitarian distribution. Thus, W k can be interpreted as the equally distributed (equivalent) level of equivalent income. As recognised by Yaari (1988) this property suggests that C k, defined by

C k = 1 −

W k , k = 1, 2...

μ (2.4) can be used as a measure of inequality. 5 Moreover, as was recognized by Ebert (1987) the justification of the social welfare function W k = μ(1 − C k) can be made in terms of value judgement of the trade-off between the mean and (in)equality in the distribution of income. For a given sum of incomes the welfare functions W k take their maximum value when everyone receives the same income and may thus be interpreted as EO-criteria (equality of outcome) when employed as a measure for judging between tax systems. Aaberge (2007) proves that the family of inequality measures {C k: k = 1, 2,.. .} and the mean μ provide a complete characterization of the distribution function F. However, in applied work one has for practical reasons to restrict to a few measures of inequality. To this end, Aaberge (2007) draws on standard statistical practice to justify the use of C 1 (the Bonferroni (1930) coefficient), C 2 (the Gini coefficient) and C 3 as a basis for summarizing the inequality information in an income distribution and the associated social welfare functions W 1, W 2 and W 3 to assess the trade-off between efficiency and (in)equality. Moreover, these three measures of inequality also prove to supplement each other with regard to sensitivity to transfers at the lower, the central and the upper part of the income distribution. In order to ease the interpretation of the inequality aversion profiles exhibited by W 1, W 2, W 3 and W ∞ Table 1 displays ratios of the corresponding weights—as defined by (2.2)—of the median individual and the 1% poorest, the 5% poorest, the 30% poorest and the 5% richest individual for different social welfare criteria. As can be observed from the weight profiles provided by Table 1, for example W 1 will be particular sensitive to changes in policies that affect the welfare of the poor. As indicated by Roemer (1998), using social welfare functions based on equality of outcome is controversial and might suffer from the drawback of

5 As demonstrated by Aaberge (2001) C k – measures can also be axiomatically justified as criteria for ranking Lorenz curves.

weight profiles of four different social welfare functions p(.01)/p(.5) p(.05)/p(.5) p(.30)/p(.5) p(.95)/p(.5)

## W 1

(Bonferroni)

## W 2

(Gini)

## W 3

## W ∞

(Utilitarian) 6.64 4.32 1.74 0.07 1.98 1.90 1.40 0.10 1,33 1.33 1.21 0.13 1 1 1 1 receiving little support among citizens. 6 This is due to the fact that differences in might be case because outcomes resulting from differences in efforts are, by many, considered ethically acceptable and thus should not be the target of a redistribution policy. An egalitarian redistribution policy should instead seek to equalise those income differentials arising from factors beyond the control of the individual. Thus, not only the outcome but also its origin and how it was obtained matters. This is the essential idea behind Roemer’s (1998) theory of equality of opportunity, where people are supposed to differ with respect to circumstances, which are attributes of the environment of the individual that influence her earning potential, and which are “beyond her control”. Roemer’s theory has first and foremost been used as a basis for evaluating the impact of specific policies on distributions of income and education across types; see e.g. Roemer et al. (2003). 7 This study defines circumstances by family background (proxied by father’s education) and classifies the individuals into three types according to father’s years of education: • • • less than 5 years (Type 1), 5–8 years (Type 2), and more than 8 years (Type 3). Let F −1 j (t) denote the income level of the individual located at the tth quantile of the income distribution (F j) of type j. The differences in incomes within each type are assumed to be due to different degrees of effort for which the individual is to be held responsible, whereas income differences that may be traced back to family background are considered to be beyond the control of the individual. As indicated by Roemer (1998), this suggests that we may measure a person’s effort by the quantile of the income distribution where he is located. Thus two individuals of different type have expended the same degree of effort if they have identical position (rank) in the income distribution of their type; i.e. an individual of type i with income F i −1 (t) and an individual of type j with income F −1 j (t) are supposed to expend the same degree of effort, which means that an EOp welfare function should aim at reducing the difference between this incomes. More precisely, an EOp tax-transfer policy should aim at maximizing min j F −1 j (t) for each quantile t. However, since this

6 See also Dworkin (1981a, b), Arneson (1989, 1990), Cohen (1989) and Roemer (1993). refer to Peragine (2002, 2004), Bourguignon et al. (2003) and Checchi and Peragine (2009) for discussions on how to measure (in)equality of opportunity.

7 We Accounting for family background when designing optimal income criterion is rather demanding and in most cases will not produce a complete ordering of the tax-transfer systems under consideration, a weaker ranking criterion is required. To this end, Roemer (1998) proposes to employ as the social objective the average of the lowest income at each quantile:

∞ =

## W

1 min F −1 j (t) dt j (2.5) 0 ∞ ignores income differences within the most disadvantaged group and Thus, W is solely concerned about differences that arise from the observed differential circumstances. By contrast, the EO criteria defined by (2.1) does not distinguish between the different sources that contribute to income inequality. As an alternative to (2.5) we introduce the following family of extended EOp welfare functions, k =

## W

1 p k (t) min F −1 j (t) dt, j k = 1, 2,..., (2.6) 0 k and W ∞ where p k (t) is defined as in (2.2). The essential difference between W k gives increasing weight to lower quantiles in the income distribution is that W k captures also an of the most disadvantage group. Thus, in this respect, W aspect of inequality within types. Our justification for introducing the extended EOp welfare functions is twofold. First, besides parents’ education (or other indicators one might have chosen), there might be other exogenous factors that affect individuals’ achievements. Thus, given the definition of types based on father’s education, differences in income within the most disadvantaged group might still be partly due to circumstances and partly due to effort. The extended EOp welfare functions (2.6) accounts for the fact that part of the differences within the most disadvantaged group might still arise from different circumstances rather than from different levels of effort. Second, the extended EOp welfare functions might be considered as a mixture of the pure EOp welfare function and the EO welfare functions. Thus, the extended EOp criterion provides a better basis for understanding differences in results produced by the pure EOp criterion and by the EO criteria. Note that the extended EOp welfare functions treat transfers from individuals that do not belong to the most disadvantage group to individuals that belong to the most disadvantage group as welfare improving. Moreover, transfers from richer to poorer individuals within the most disadvantage group is also welfare improving. Note that min F i −1 (t) defines the inverse of the following cumulative distrii bution function (F) (x) = max F i (x).

## F

i (2.7) k as we did for the EOp Thus, we may decompose the EOp welfare functions W welfare functions W k. Accordingly, we have that k, k = W

## ∞ 1 − C

## W

k = 1, 2,...

(2.8) k, defined by where C k = 1 − W k,

## C

∞

## W

k = 1, 2,...

(2.9) is a measure of inequality for the mixture distribution F.

k Expression (2.8) demonstrates that the extended EOp welfare functions W for k < ∞ takes into account value judgements about the trade-off between the mean income and the inequality in the distribution of income of the most (observed) EOp disadvantaged people. Note that the EOp criterion was originally interpreted as more acceptable from the point of view of individualistic societies. Our extended EOp welfare functions are concerned about inequality between observable types as well as inequality within the (observable) worst-off distribution defined by (2.9) and can in that sense be considered to capture features from both the pure EOp welfare function and the EO welfare functions. The basic version of the EOp criterion only looks at the mean of the (observable) worst-off distribution. By contrast, EO takes into account the whole income distribution. For a given sum of incomes, EO will consider equality of income (everyone receives the same income) as the most desirable income distribution. The pure EOp will instead consider equality in mean incomes across observable types as the ultimate goal. Since the extended EOp combines these two criteria, transfers that increase the mean income of the worst-off group and/or reduce the income differentials between the individuals within the worst-off distribution are considered welfare improving by the extended EOp. Thus, in the case of a fixed total income also the extended EOp will consider equality of income as the most desirable distribution. However, by transferring money from the most advantaged type to the most disadvantaged type, EOp inequality may be reduced although transfers may be conflicting with the Pigou-Dalton transfer principle, which states that an income transfer from a richer to a poorer person reduces overall income inequality, provided that the receiver does not become richer than the donor. Note that the EOp and the EO criteria coincide if and only if the type-specific distributions coincide. Moreover, we want to stress that while the pure EOp is a special case of our generalized EOp, the latter is not a special case of EO. The two criteria (EO and EOp) are not nested. Accordingly, theoretical considerations cannot be used to clarify whether EOp or EO will favors the most inequality averse tax structure. This is simply an empirical question. Thus, whether it is more “efficient” to reduce inequality between types or within the worst-off distribution depends on the specific situation. When labour supply responses to taxation are taken into account, the composition of observable types in the worst-off distribution will change Accounting for family background when designing optimal income and depend on the chosen welfare function as well as on the considered tax rule. Thus, the large heterogeneity in labour supply responses to tax changes that is captured by our model(s) makes it impossible to state anything on EOp or EO optimality before the simulation exercises have been completed.

3 Optimal tax-transfer rules In what follows, we determine—by microeconometric simulation—the income tax-transfer rules that maximize social welfare functions as defined by (2.6). It is important to stress that the tax-transfer rules we consider are assumed to depend only on income (as much as current rules essentially do). In particular, they do not depend on the “type” (father’s education in this exercise) the individuals belong to. In other words, we aim at finding the tax-transfer rules that best conform to the EOp criterion within the class of rules that only depend on income. Despite the fact that “types” might be observable, we postulate that it is not practical or realistic or politically acceptable to actually use them as an argument of the tax-transfer rule. We take, therefore, a secondbest perspective where only income can be used as an instrument. The optimal rules are determined computationally, i.e. we employ a microeconometric model that is capable of simulating choices (labour supply) of couples and singles facing alternative tax-transfer rules. Given a parametric representation of the tax-transfer rule, we iteratively search the parameter space until the social welfare function is maximized under the constraint of a constant total net tax revenue. The model is explained in detail in the Electronic Supplementary Material. The sample used for the estimation and the simulation of the model is obtained from the Bank-of-Italy 1993 Survey of Household Income and Wealth (SHIW 1993). It contains single females, single males and couples that are between 19 and 54 years old. To capture the heterogeneity in preferences, we have estimated three separate models of labour supply: one for single females, one for single males and one for couples. The main features of the 1993 tax rule—i.e. the actual tax rules the households face—are briefly illustrated in the Electronic Supplementary Material. The identification of the optimal tax-transfer rules consist of five main steps: 1. A tax rule (member of a parametric class of rules to be explained in Sections 3.1 and 3.2) is applied to individual earners’ gross incomes in order to obtain disposable incomes. New labour supply responses in view of a new tax rule are taken into account by the household labour supply models for singles and couples described in the Electronic Supplementary Material. Note that the utility functions (and choice sets) of the underlying micro-econometric model(s) are stochastic. Thus, we use stochastic simulation to find, for each individual/couple, the optimal choice given a tax-transfer rule. The simulations are made under the conditions of unchanging total tax revenue and non-negative disposable household incomes.

2. To each decision making individual between 18 and 54 years old, an equivalent income is imputed, computed as total disposable household income divided by the square root of the number of household members. 3. We then build the individual equivalent income distributions F 1, F 2 and F 3 for the types defined according to parental (actually father’s) education: less than 5 years (type 1), 5–8 years (type 2) and more than 8 years (type 3).

k for k = 1, 2, 3 and ∞.

4. Finally, we compute W 5. Optimization is performed by iterating the above steps, in order to find the k for each value of k under the tax rule that produces the highest value of W constraint of unchanged tax revenue.

## 3.1 EOp evaluation of alternative two-parameter tax rules

The alternative two-parameter tax rules are of the following type:

x = c + (1 − t) y, where y = gross income, x = disposable income, c = lump-sum transfer (positive or negative) t = constant marginal tax rate. This is the class of tax-transfer rule considered in Roemer et al. (2003). Here, however, we use a more sophisticated empirical strategy. In Sections 3.2 and 5 we will consider three-parameter tax-transfer rules. Note that the income and tax figures below are measured in 1,000 ITL since the model is estimated for a pre-EURO year (to get the equivalent in EURO the figures must be divided by 1.93627). The results of the two-parameter tax reform simulations are summarised in Tables 2 and 3 and in Fig. 1. Table 2 presents the EOp-optimal affine tax rules for different values of k, i.e. for different degrees of concern for within-type inequality. Recall that the higher is k, the lower is the concern for within type inequality. As demonstrated by Table 2, the optimal policy is very sensitive to the value of k. For k ≥ 3, the EOp-optimal tax rule is the pure lump-sum tax (i.e. t = 0 and c < 0) whereas for k ≤ 2 the optimal tax rule consists of a very high marginal

Table 2 Optimal twoparameter tax-transfer rules under various EOp k) criteria (W k 1 2

Marginal tax rate, t

Lump-sum tax/transfer, c .774 .637 11,500 9,500 ∞ 3 0 −5,790 0 −5,790 Accounting for family background when designing optimal income k) of different tax-transfer rules

Table 3 EOp performance (W

Tax system k)

Social objective function (W Flat tax EOp2 (1) EOp2 (2) EOp2 (3) t = .181 c = 0 t = .774 c = 11,500 t = .637 c = 9,500 t = 0 c = −5,790 k 1 2 3 ∞ 10,523 12,797 13,893 18,323 10,834 13,496 14,823 20,449 12,661 13,652 14,077 15,641 12,406 13,660 14,237 16,486 9,942 13,270 14,992 22,231 tax rate and a positive lump-sum transfer. An implication is that the concern for the equality of opportunity by itself does not imply high marginal tax rates. Only if we also account for within type inequality, does the optimal policy entail high marginal tax rates. In order to interpret correctly our results, it should be remembered that the lump-sum rule considered here is not the lump-sum rule envisaged in the 2nd Welfare Theorem, which would require individual (or household)-specific lump-sum taxes or transfers. In our exercise, the lump-sum rule envisages taxes or transfers equal for everyone. Table 3 and Figs. 1 and 2 give more details. The graphs illustrate the equivalent income distributions under the actual 1993 tax rule (Fig. 1) and under the EOp-optimal rules for k = 1 and k ≥ 3 (Fig. 2). Table 3 reports the value of the EOp criterion for different tax rules, including—as a benchmark—the Flat Tax. In particular, we focus on the comparison between the observed rule (1993), the pure flat tax (a theoretical benchmark), and the three linear rules that are EOp optimal under different values of k. In each column (i.e. for each k) the bold figure is the maximised value of the EOp criterion, i.e. it corresponds to the EOp-optimal tax rule. EOp2(r) denotes the EOp-optimal affine tax rule when k = r.

Fig. 1 Distributions of observed equivalent income by type. 1,000 ITL 1 0.9 0.8 0.7 0.6 0.5

High parental education 0.4

Intermediate parental education 0.3

Low parental education 0.2 0.1 0 0 20000 40000 60000 80000 100000 120000 140000

Eop2(1)

Eop2(3) 1 0.9 0.8 0.7

High parental education 0.6 0.5 0.4

Intermediate parental education 0.3

Low parental education 0.2 0.1 0 0 20000 40000 60000 1 0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1 0 80000 100000 120000 140000

High parental education

Intermediate parental education

Low parental education 0 20000 40000 60000 80000 100000 120000 140000 Fig. 2 Distributions of individual equivalent income by type under the EOp2(1) and EOp2(3) tax systems. 1,000 ITL Table 3 enables us to compare the EOp performance of the various rules for a given k (note that the comparison only makes sense between elements of the same column). We can see that although the flat tax is never EOp-optimal, for any value of k, it improves upon the observed 1993 rule. More generally, one can always find an affine tax rule that is EOp-preferred to the observed 1993 one. However, the direction along which one can find EOp-optimal tax rules depends crucially on the value of k. If k = 1 one has to move towards very high marginal tax rates (coupled with high transfers). If k is greater than 1, then the EOp-optimal tax rules require lower marginal tax rates—and more revenue collected through the lump-sum part of the tax. These aspects are further illustrated by Fig. 3, where we draw the curve – in the (c, t) plane—of the revenue-constant affine tax rules, and for k = 1, 2, we indicate the sets of tax rules with a lower (dotted line) or with a higher (solid line) EOp performance with respect to the observed rule. The graphs show that a higher concern for within-type inequality (i.e. k = 1 compared to k = 2) tends to favour higher marginal tax rates and higher (positive) transfers. Table 4 shows the efficiency and inequality components of the rules illustrated in Tables 2 and 3. We note that the Flat tax and Lump-Sum Tax (i.e.

~ 1 0,8 0,8 0,6 t t 0,6 0,4 0,4 0,2 0,2 0 -6000 -4000 -2000 ~

Under W 2 1,

Under W 1 0 2000 4000 6000 8000 10000 12000 14000 c 0,0 -6000 -4000 -2000 0 2000 4000 6000 8000 10000 12000 14000 c Fig. 3 Sets of revenue constant affine tax systems under different EOp welfare criteria Accounting for family background when designing optimal income k) for different tax-transfer rules Table 4 Decomposition of EOp social welfare (W

Tax system ∞

## W

Measure of inequality 1 2

## C

## C

3

## C

1993 Tax system t = .181

Flat tax c = 0 t = .774

EOp2 (1) c = 11,500 t = .637

EOp2 (2) c = 9,500 t = 0

EOp2 (3) c = −5,790 18,323 .426 .302 .242 20,449 .470 .340 .275 15,642 .191 .127 .100 16,486 .247 .171 .136 22,231 .553 .403 .326 EOp2(3)) are more efficient than, but disequalizing with respect to, the current system. The opposite happens with EOp2(2) and EOp2(1). The fact that the optimal tax rule is the pure lump-sum tax, provided that we do not put too much weight on within-type inequality, is a somewhat striking result in itself. After all, EOp is an egalitarian criterion, and one would expect it to favour higher marginal tax rates. How can we explain this apparently counter-intuitive result? A possible explanation lies in the relatively high labour supply response of the least advantaged individuals. Since the EOp criterion requires the maximisation of a weighted average of the incomes of the least advantaged type, and since the labour supply of these individuals turns out to be very responsive to higher net wage rates, it follows that lower marginal tax rates (or, in the limit, a marginal tax rate equal to 0) can in fact improve substantially the welfare of this group. However, this effect may be counterbalanced if we give enough weight (low value of k) to within-type inequality. Table 5 gives some support to this argument by illustrating the labour supply response of the different types when facing alternative tax rules. When the pure lump-sum tax is applied, the labour supply (and therefore the Table 5 Labour supply by types under different tax-transfer rules. Hours of work Tax system

All

Type 1 2 3

1993 Tax system t = .181

Flat tax c = 0 t = .774

EOp2 (1) c = 11,500 t = .637

EOp2 (2) c = 9,500 t = 0

EOp2 (3) c = −5,790 1,383 1,279 1,383 1,469 1,391 (+0.58) 1,369 (+7.04) 1,362 (+1.52) 1,471 (+0.14) 1,095 (−20.82) 1,109 (−13.29) 1,087 (−21.40) 1,100 (−25.12) 1,160 (−16.12) 1,142 (−10.71) 1,148 (−16.99) 1,200 (−18.31) 1,487 (+7.52) 1,450 (+13.37) 1,459 (+5.50) 1,578 (+7.42) Percentage changes relative to the labour supply under the 1993 tax system in parentheses available income) of type 1 (the most disadvantaged group) increases much more (as percentage variation) than labour supply of types 2 or 3. 8 The different population considered and the heterogeneity of the labour supply elasticity most likely also play a crucial role in explaining the differences between our results and those obtained by Roemer et al. (2003), where only males are considered and a fixed value of the labour supply elasticity is set equal to 0.06. The social welfare criterion corresponding to the one adopted ∞. For this social welfare function, we get that the in Roemer et al. (2003) is W optimal rule is a pure lump-sum tax = 5790 (tax rate = 0). Roemer et al. (2003) obtain instead an optimal tax rate that varies from .65 to .83 and an optimal (positive) lump-sum transfer that varies from 16630 to 21300. In order to get optimal rules that are close to those of Roemer et al. (2003) we should use 1, i.e. the social welfare function corresponding to the Bonferroni version of

## W

the generalized version of the EOp crierion.

Overall it seems that the heterogeneity of labour supply behaviour plays a crucial role in shaping the optimal tax rules for a given social welfare function: this gives support to the use of microeconometric simulation tools for investigating optimal taxation issues.

What happens to specific groups of people under the EOp-optimal rules and in particular under the pure lump-sum policy? Table 6 presents, for various sub-samples, their composition in terms of EOp types, the average net observed income in 1993, and the change in average income when the lumpsum rule is applied. The results in Table 6 give a more vivid understanding of the effects of the “reform” from the viewpoints of efficiency and equality.

All the sub-samples on average gain in the sense that they get more income.

If we look at the gains across types, we see that types 2 or 3 almost always gain proportionately more than type 1. However, this is not relevant from the point of view of the EOp criterion, according to which we only care about what happens to the worst-off type for each quantile (in our case, in practice, this is type 1). Under the lump-sum rule, type 1 gains more than under the alternative rules; it does not matter if type 2 and 3 gain even more. Where do these gains come from? Clearly there are two (interdependent) channels, higher net wages (in fact an agent gets the whole gross wage under the lump-sum rule) and higher labour supply. For example, we can compute from Table 6 that overall average income increases by 54% gross of the lump-sum tax of 5,790,000 ITL.

Since the overall increase in labour supply amounts to 7.5% (from Table 5), we have a 46.5% gain attributable to the increase in net wage and to the interaction between wage and labour supply across the sample. We have seen that the lump-sum rule is within-type disequalizing (Table 4). However, we know that the generalised EOp index is only affected by the inequality among the individuals belonging to the worst-off type. If we look at what is going on

8 To be sure, a bias in favour of the lump-sum tax might be due to the fact that we equate income and welfare. When accounting for the value of leisure (object of on-going research), the policy prescriptions might change.

Accounting for family background when designing optimal income Table 6 Effects on household net available income when introducing lump-sum taxation (EOp2(3)), by demographic group and household type Individual and household characteristics All

Single males

Single females

Two person households

Three person households

Households with more than three persons

Poor individuals

Non-poor individuals

Household type (by family background) 1 2 3

All

Proportion (percent)

Mean income

Changes in mean income

Proportion (percent)

Mean income

Changes in mean income

Proportion (percent)

Mean income

Changes in mean income

Proportion (percent)

Mean income

Changes in mean income

Proportion (percent)

Mean income

Changes in mean income

Proportion (percent) 20.3 21,107 3,907 19.9 22,369 3,210 15.8 18,076 3,134 15.3 24,377 7,153 16.5 20,091 4,678 23.5 54.7 22,831 5,794 51.7 28,480 7,013 51.7 20,110 2,568 51.2 28,613 9,781 55.0 24,795 5,066 55.8 25.0 29,312 12,011 28.4 34,046 7,343 32.6 26,085 4,412 33.5 33,913 14,909 28.5 29,050 14,333 20.7 100 23,540 6,969 100 28,843 6,350 100 21,734 3,258 100 29,741 11,097 100 25,235 7,648 100

Mean income

Changes in mean income

Proportion (percent)

Mean income

Changes in mean income

Proportion (percent)

Mean income

Changes in mean income 16,848 3,022 39.2 7,235 5,276 18.0 21,320 3,537 20,516 5,153 50.4 7,720 7,487 55.2 24,541 5,603 27,349 9,785 10.4 7,424 13,174 26.8 30,368 11,955 21,064 5,608 100 7,500 7,216 100 25,528 6,939

Income amounts are in 1,000 LIT more generally in the whole sample, the effect upon distribution is less clearcut. For example, the relative gain of the poor is larger than the relative gain of the non-poor.

## 3.2 EOp evaluation of alternative three-parameter tax rules

One might suspect that the results—in particular the EOp-optimality of a pure lump-sum tax for k = 3 or greater—are somewhat forced by the fact that we restrict the simulation to a two-dimensional class of tax rules. Since the disadvantaged individuals are more responsive—in terms of labour supply— than the rich and/or advantaged individuals, we should be able to improve upon the pure lump-sum tax or upon the high marginal rate rules, by adopting a three-parameter tax-transfer rule. Here, we explore this policy direction. The class of tax rules considered is defined as follows:

x = c + (1 − t 1) y if y ≤ y c + (1 − t 1) y + (1 − t 2) (y − y) if y > y k) Table 7 Optimal three-parameter tax-transfer rules under various EOp criteria (W k 1 2 3 ∞ t 1 t 2 c .856 .776 12,500 .251 .531 3,500 0 .168 −3,500 0 0 −5,790 where x = disposable income, y = gross income, y = average individual gross income in Italy on the survey year (1993), t 1, t 2 = marginal tax rates. Clearly, one could consider even more general and flexible rules. 9 Here, however, our aim is not the design of a realistic optimal system but rather the use of a stylized and easy-to-visualize class of tax-transfer rules as a basis for comparing the implications of different evaluation criteria. On the other hand, even a rule with two brackets is not devoid of realism since the recent trend for tax reform moves in the direction of simplifying the rules and reducing the number of brackets. Table 7 reports the optimal three-parameter rules for different values of k. For example, for k = 1 the optimal rule is defined by a transfer c = 12,500, a first marginal tax rate t 1 = 0.856 and a second marginal tax rate t 2 = 0.776. By comparing Table 7 with Table 2, we see that the EOp-optimal rules differ significantly depending on whether one considers a two-parameter (Table 2) or a three-parameter rule (Table 7). When k = 1, the three-parameter EOpoptimal rule gives two very high and slightly regressive tax rates 10 complemented by a large positive transfer, inducing a net-vs-gross income profile close to the ones implied by the Negative Income Tax schemes. The most marked differences with respect to the two-parameter case are found when using the k = 2. While the two-parameter case called for tax rate over 60% combined with a positive transfer of 9,500,000 ITL, the three-parameter case entails two very different tax rates with a marked progressive structure (from 25% to 53%) and a much lower transfer (3,500,000 ITL). For any k ≥ 3, the two-parameter case chooses the pure lump-sum tax as the EOp-optimal policy. When we use a three-parameter rule, with k = 3, we still have a positive tax rate (17%) for the higher incomes, combined with a 3,500,000 ITL lump-sum tax. However, when we employ the pure EOp-welfare function (k = ∞), we are back to the EOp optimality of the pure lump-sum tax. It is worth mentioning that when the EOp-version of the Gini welfare function is adopted, the optimal tax rule is close to the actual one if not for

9 See for example Aaberge and Colombino (2008).

in the sense that the marginal tax rate decreases with income.

10 Regressive Accounting for family background when designing optimal income k) for three-parameter tax-transfer rules Table 8 Decomposition of EOp social welfare (W

Tax system ∞

## W

Measure of inequality 1 2

## C

## C

3

## C

1993 Tax system ⎛ ⎞ t 1 = .856 EOp3 (1) ⎝ t 2 = .776 ⎠ ⎛ c = 12,500 ⎞ t 1 = .251 EOp3 (2) ⎝ t 2 = .531 ⎠ ⎛ c = 3,500 ⎞ t 1 = 0 EOp3 (3) ⎝ t 2 = .168 ⎠ c = −3,500 t 1 = t 2 = 0

EOp3 (∞) c = −5,790 18,323 .426 .302 .242 15,393 .176 .116 .091 18,508 .364 .253 .201 21,156 .497 .355 .285 22,231 .553 .403 .326 the important difference of prescribing a universal lump-sum positive transfer of 3,500,000 ITL, which has no comparable counterpart in the actual system. Table 8 is the analogue of Table 4 for the three-parameter rule. It shows the decomposition of the EOp social welfare function for different values of k and different tax rules, that is, the current 1993 rule and the four EOp-optimal rules with EOp3(r) denoting the EOp-optimal three-parameter tax rule when k = r. Table 8 also provides an illustration of the equity-efficiency trade-off. The lump-sum rule (i.e. EOp3(∞)) is the most efficient one (measuring efficiency ∞ ). If we adopt an egalitarian criterion, e.g. the Gini version of the with W EOp criterion, the optimal rule is EOp3(2). We have a loss of efficiency equal to 22,231–18,508. However, the loss of efficiency is more than compensated by a gain in equality: indeed, the Gini coefficient decreases from .403 to .253 and the Gini EOp welfare function increases from 22,231(1–0.403) = 13,271 to 18,508(1–0.253) = 13,825.

4 Comparison of empirical results based on EOp and EO criteria In this section, we focus upon the evaluation of the EOp-optimal policies (illustrated in Section 3) using the more traditional evaluation criterion of equality of outcome (EO criterion, see Section 2). Table 9 reports the EO performance, i.e. the level of the EO social welfare function (defined in Section 2) of five policies discussed above for various values of k. The policies are the observed 1993 tax rule, and the four EOp-optimal three-parameter rules for k = 1, 2, 3 and ∞. The Table shows the efficiency and inequality components of the EO social welfare function. More generally, we have also searched for the EO-optimal rule within the whole classes of the two-parameter and threeparameter tax rules, and it always turns out that a universal lump-sum tax is optimal whatever the value of k. Thus, if we do not explicitly account for inequality between types according to the EOp criterion, the optimal policy Table 9 Decomposition of the EO social welfare (W k) for different tax-transfer rules Tax system

Mean income

Measure of inequality

## C 1

## C 2

## C 3

⎛ ⎞ t 1 = .856 ⎝ t 2 = .776 ⎠

EOp3 (1) c ⎛ = 12,500 ⎞ t 1 = .251 EOp3 (2) ⎝ t 2 = .531 ⎠ ⎛ c = 3,500 ⎞ t 1 = 0 EOp3 (3) ⎝ t 2 = .168 ⎠ c = −3,500 t 1 = t 2 = 0

EOp3 (∞) c = −5,790 23,540 .416 .295 .237 16,560 .193 .130 .104 21,477 .364 .255 .203 27,573 .499 .363 .294 30,510 .544 .402 .327 always consists in a zero marginal tax rate coupled with a positive universal lump-sum tax, whatever the degree of inequality aversion. Table 9 suggests that this result is due to very large efficiency effects of the lump-tax rule, large enough to over-compensate the also large inequality effects. It might appear paradoxical that, overall, EOp requires more redistribution (through marginal tax rates) than EO. However, the paradox is only apparent. EOp is motivated by a methodological position that focuses on inequality due to circumstances: but this position does not necessarily imply less redistribution—a consequence of EO and EOp being non-nested criteria. Table 9 can also be read from the perspective of the efficiency-equity tradeoff, as we did when commenting Table 8 at the end of Section 3.2—but this time adopting the EO criterion. The EO-most efficient policy is a lump-sum tax = 5,790 (i.e. EOp3 (∞)). This policy entails a mean income = 30,510. However, it also implies a high level of inequality, measured for example by the Gini coefficient (C 2) = .402. Let us consider a more egalitarian policy, such as EOp3(2). This policy reduces the C 2 to .255; however, it also brings about a loss of efficiency equal to 10,033 = 30,510 − 21,477.

5 Optimal rules when a universal lump-sum tax is not feasible As we have seen in previous sections, in many cases it turns out that the socially optimal tax rule is a universal lump-sum tax. Notice that this lumpsum tax is identical for everyone and is not to be confused with the policy k) Table 10 Optimal three-parameter tax-transfer rules under various EOp criteria (W k 1 2 3 ∞ t 1 t 2 c .856 .776 12,500 .251 .531 3,500 0.106 0.346 0 .313 0 0

Lump-sum taxes not feasible Accounting for family background when designing optimal income Table 11 Optimal three-parameter tax-transfer rules under various EO (W k) criteria k 1 2 3 ∞ t 1 t 2 c .298 .178 2000 .313 0 0 .313 0 0 .313 0 0

Lump-sum taxes not feasible of individualized lump-sum taxes that would be optimal in a first-best world. However, even a universal lump-sum tax might be not feasible, for example because it might be judged as not politically acceptable. Therefore, we also computed optimal tax rules where lump-sum positive transfers are allowed but not lump-sum taxes. The results are summarised in Tables 10 and 11, respectively, for the EOp and the EO criterion. As it is the case with the policies computed in the previous sections, the optimal no-lump-sum policies are the same under EOp and under EO when k = ∞, with no transfers, a 31.3% marginal tax rate on the first segment and a 0% marginal tax rate on the second segment. This same rule remains the best one under EO for k = 3 and k = 2. For the same values of k, the EOp criterion prescribes instead a progressive rules (for k = 2, it also requires a positive transfer). For k = 1 the two criteria diverge again: EOp prescribes a very large transfer together with very high (slightly regressive) marginal rates, while EO prescribes a modest transfer and much lower (regressive) marginal rates. Overall, as was also the case with the policies admitting lump-sum taxes, the EOp criterion seems to require more redistribution than the EO criterion.

6 Conclusion We have used a micro-econometric model of household labour supply in Italy in order to simulate and identify optimal (second-best) income tax-transfer rules within classes of two-and three-parameter rules according to the criterion of Equality of Opportunity as developed by Roemer (1998). We have also offered an extended version of the EOp criterion that permits us to complement the pure EOp criterion with a variable degree of aversion to inequality within the worst-off distribution. When we admit the feasibility of universal (i.e. not individual-specific) lump-sum taxes, the optimal tax rule turns out to be in fact a universal lump-sum tax under the pure EOp criterion or under the extended EOp with moderate degrees of aversion to inequality (k = 3) within the worst-off distribution. The result seems to depend on a relatively high labour supply response from the most disadvantaged type: the labour supply incentives—and the efficiency effects for the most disadvantaged—generated by the pure lump-sum tax are large enough to overcome the disequalizing effects of lump-sum taxation. A high degree of inequality aversion (k less than 3) instead produces EOp-optimal rules with strictly positive marginal tax rates. It is worth mentioning that when the EOp version of the Gini welfare function is adopted, the optimal tax rule is close to the actual one if not for the important difference of prescribing a universal lump-sum positive transfer of 3,500,000 ITL (=1,807 Euros), which has no comparable counterpart in the actual system. When using the EO criterion, the universal lump-sum tax always turns out to be optimal, at least with respect to the classes of two-and three-parameter rules. Overall, the results do not conform to the perhaps common expectation that the EO criterion is more supportive of “interventionist” (redistributive) policies than an EOp approach. On the contrary, our data and our model indicate that EO never calls for redistribution, and only if an extended EOp criterion is introduced may redistributive intervention (through increasing marginal tax rates and/or positive transfers) be optimal depending on the degree of social aversion to inequality. The policy prescription might change if we included the value of leisure in the measurement of individual welfare. For example, since under the pure lump-sum tax people work (and earn) a lot more, it might be the case that, when account is taken of their reduced leisure, the lump-sum tax is not so desirable. 11 We also identified the optimal rules when assuming that only universal lump-sum positive transfers (not taxes) are feasible. In this case the pure EOp criterion and utilitarian EO criterion dictate the same rule, namely a system where all the taxes are collected from incomes in the first bracket. This same rule remains the optimal one under the EO criterion except in the Bonferroni case (k = 1). However, the optimal rules become definitely more redistributive when adopting the extended EOp criterion. Looking at the results from a methodological perspective, the importance of heterogeneous labour supply responses in shaping the optimal tax rules suggests that simulation based on microenometric models is a useful tool for investigating optimal taxation issues. Acknowledgements We would like to thank Tom Wennemo for skilful programming. Parts of this paper were written while Rolf Aaberge was visiting ICER in Torino. ICER is gratefully acknowledged for providing financial support and excellent working conditions. The Italian Ministry of University and Research (MURST, project MM13317213, 2000–2002) and the Norwegian Research Council have provided financial support for this project. We thank two anonymous referees for helpful comments.

## References

Aaberge R (2001) Axiomatic characterization of the Gini coefficient and Lorenz curve orderings.

J Econ Theory 101(1):115–132 Aaberge R (2007) Gini’s nuclear family. J Econ Inequal 5(3):305–322 Aaberge R, Colombino U (2008) Designing optimal taxes with a microeconometric model of household labour supply. WP CHILD n. 06/2008. www.child-centre.it Aaberge R, Colombino U, Strøm S (1999) Labour supply in Italy: an empirical analysis of joint household decisions, with taxes and quantity constraints. J Appl Econ 14(4):403–422

11 The inclusion of the value of leisure will be pursued in future work.

Accounting for family background when designing optimal income Aaberge R, Colombino U, Strøm S (2000) Labor supply responses and welfare effects from replacing current tax rules by a flat tax: empirical evidence from Italy, Norway and Sweden. J Arneson R (1989) Equality and equality of opportunity for welfare. Philos Stud 56(1):77–93 Arneson R (1990) Liberalism, distributive subjectivism, and equal opportunity for welfare. Philos Public Aff 19(2):159–194 Atkinson AB (1970) On the measurement of inequality. J Econ Theory 2(3):244–263 Behrman J et al (1999) Women’s schooling, home teaching and economic growth. J Polit Econ 107(4):682–714 Ben Porath E, Gilboa I (1994) Linear measures, the Gini index, and the income-equality trade-off. J Econ Theory 64(2):443–467 Bonferroni C (1930) Elementi di Statistica Generale. Seeber, Firenze Bourguignon F, Ferreira F, Menéndez M (2003) Inequality of outcomes and inequality of opportunities in Brazil. World Bank Policy Research Papers 3174 Checchi D, Peragine V (2009) Regional disparities and inequality of opportunity: the case of Italy. J Econ Inequal. doi:10.1007/s10888-009-9118-3 Cohen GA (1989) On the currency of egalitarian justice. Ethics 99(4):906–944 Dagsvik JK (1994) Discrete and continuous choice, max-stable processes and independence from irrelevant attributes. Econometrica 62(5):1179–1205 Donaldson D, Weymark JA (1980) A single parameter generalization of the Gini indices of inequality. J Econ Theory 22(1):67–86 Donaldson D, Weymark JA (1983) Ethically flexible indices for income distributions in the continuum. J Econ Theory 29(2):353–358 Dustmann C (2004) Parental background, secondary school track choice, and wages. Oxf Econ Pap 56(2):209–230 Dworkin R (1981a) What is equality? Part 1: equality of welfare. Philos Public Aff 10(3):185–246 Dworkin R (1981b) What is equality? Part 2: equality of resources. Philos Public Aff 10(4):283–345 Ebert U (1987) Size and distribution of incomes as determinants of social welfare. J Econ Theory 41(1):22–33 Ermisch J, Francesconi M (2001) Family matters: impact of family background on educational attainment. Economica 68(270):137–156 Hey JD, Lambert PJ (1980) Relative deprivation and the Gini coefficient: comment. Q J Econ 95(3):567–573 Mehran F (1976) Linear measures of inequality. Econometrica 44(4):805–809 Mirrlees JA (1971) An exploration in the theory of optimal income taxation. Rev Econ Stud 38(2):175–208 Peragine V (2002) Opportunity egalitarianism and income inequality: the rank-dependent approach. Math Soc Sci 44(1):45–64 Peragine V (2004) Measuring and implementing equality of opportunity for income. Soc Choice Welf 22(1):1–24 Roemer J (1993) A pragmatic theory of responsibility for the egalitarian planner. Philos Public Aff 22(2):146–166 Roemer J (1998) Equality of opportunity. Harvard University Press, Cambridge Roemer JE, Aaberge R, Colombino U, Fritzell J, Jenkins SP, Lefranc A, Marx I, Page M, Pommer E, Ruiz-Castillo J (2003) To what extent do fiscal regimes equalize opportunities for income acquisition among citizens? J Public Econ 87(3–4):539–565 Sacerdote B (2002) The nature and nurture of economic outcomes. Am Econ Rev (Papers and Proceedings) 92(2):344–348 Sen A (1974) Informational bases of alternative welfare approaches. J Public Econ 3(4):387–403 Weymark J (1981) Generalised Gini inequality indices. Math Soc Sci 1(4):409–430 Yaari ME (1988) A controversial proposal concerning inequality measurement. J Econ Theory 44(2):381–397
