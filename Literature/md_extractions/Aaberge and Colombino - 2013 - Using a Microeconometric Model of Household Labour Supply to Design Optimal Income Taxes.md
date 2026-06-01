# Using a Microeconometric Model of Household Labour Supply to Design Optimal Income Taxes*

Rolf Aaberze

Statistics Norway, NO-0033 Oslo, Norway rolf.aaberge@ssb.no

Ugo Colombino

University of Torino, 10153 Torino, Italy ugo.colombino@unito.it

## Abstract

With regards to empirical applications of optimal taxation theory, analytical expressions are typically adopted for optimal taxes, and then numerical values are imputed to their parameters by calibration or by using previous estimates. We aim to avoid the restrictive assumptions and possible inconsistencies of this approach. In contrast, we identify optimal taxes by iteratively running a microeconometric model, based on 1994 Norwegian data, until a given social welfare function is maximized, given the public budget constraint. The optimal rules envisage monotonically increasing marginal rates (negative on very low incomes) and -compared to the current rule -a lower average rate, lower marginal rates on low incomes, and higher marginal rates on very high incomes.

Keywords: Microsimulation; optimal taxation; random utility model

JEL classification: //21; //31; J 22

## I. Introduction

In this paper, we present an empirical analysis of optimal income taxation The purpose is not new, but the exercise illustrated here differs, in many important ways, from previous attempts to compute optimal taxes empirically. The standard procedure adopted in the literature starts with some version of the optimal taxation framework, originally set up in the influential paper by Mirrlees (1971). The next step typically consists of imputing numerical values-either determined by calibration or taken from previous empirical analysis-to the parameters (e.g., wage elasticities of labour *We thank Tom Wennemo for skilful programming assistance, and we are grateful to referee for very detailed and useful comments and suggestions. U. Colombino received financial support from the Italian Ministry of University and Research and the Compagni di San Paolo. ICER is gratefully acknowledged for providing financial support and excellen working conditions for R. Aaberge.

supply) appearing in the formulae produced by the theory. This body of literature has been surveyed by Tuomala (1990). A recent strand of research adopts a similar approach to address the inverse optimal taxation problem (i.e., retrieving the social welfare function that makes optimal a given tax rule; Bourguignon and Spadaro, 2005). There are two main problems with the optimal taxation literature, as follows, (a) The theoretical results become amenable to an operational interpretation only by adopting rather restrictive assumptions concerning the preferences, the composition of the population, and the structure of the tax rule, (b) The empirical measures used as counterparts of the theoretical concepts are usually derived from previous estimates obtained under assumptions that are different from those used in the theoretical model. As a consequence, the consistency between the theoretical model and the empirical measures is dubious, and the significance of the numerical results remains uncertain. The typical outcome of these exercises envisages a lump-sum transfer, which is progressively taxed away by very high marginal tax rates (MTRs) on lower incomes (i.e., a negative income tax mechanism). Beyond the "break-even point" (i.e., the income level where the transfer is completely exhausted), the MTRs are close to constant. However, Tuomala (2010) has suggested that these results are essentially forced by the restrictive assumptions made upon preferences, labour supply elasticities, and the distribution of productivities (or wage rates). Interestingly, when Tuomala (2010) adopts a more flexible specification of the utility function, he finds that the optimal system is progressive, with monotonically increasing MTRs. While most of the studies mentioned above have been essentially illustrative numerical exercises, several recent contributions have attempted to use optimal taxation results in the empirical evaluation or design of taxtransfer reforms. Diamond (1980, 1998), Revesz (1989), and Saez (2001) have made the results of Mirrlees easier to interpret by reformulating them in terms of labour (or income) supply elasticities, in order to provide a direct link between the theoretical results and empirical measures. Saez (2002) has developed a model that is amenable to empirical implementation, and that focuses on the relative magnitude of the labour supply elasticities at the extensive and intensive margins. Immervoll et al. (2007) have adopted the approach of Saez (2002) to evaluate alternative income support policies in European countries. Blundell et al. (2009) and Haan and Wrohlich (2010) have also used the approach of Saez (2002) to evaluate taxes and transfers for lone mothers in Germany and the UK, whereas Kleven et al. (2009) have provided results on the taxation of couples. Although these new contributions are interesting attempts in the direction of an empirical implementation of theoretical optimal taxation results, they still rely on restrictive assumptions and suffer from a possible inconsistency between the theoretical model and the empirical measures used to implement it. For example, the basic version of the model proposed by Saez (2002), which has been adopted in the empirical exercises mentioned above, does not account for income effects.1 Moreover, it relies on rather restrictive assumptions upon the way the households respond to changes in the relative attractiveness of the opportunities in the budget set.2 When it comes to empirical applications (as in Immervoll et al ., 2007; Blundell et al ., 2009; Haan and Wrohlich, 2010), the parameters of the theoretical models are given numerical values estimated with microeconometric models that do not adopt the same restrictive assumptions as in Saez (2002). Of course, some of these limitations and potential inconsistencies might be overcome in the future, but analytical solutions of the optimal income taxation problem will likely never be fully consistent with flexible structural labour supply models. Here, we follow a different, and possibly complementary, approach. We do not start from theoretical results that dictate the conditions for optimal tax rules under various assumptions. Instead, we use a microeconometric model of labour supply in order to identify, by simulation, the tax rule that maximizes a social welfare function, under the constraints that the households maximize their own utility and that the total net tax revenue remains constant. The microeconometric simulation approach is commonly used to evaluate tax reforms, but it has not often been used in empirical optimal taxation studies. The closest examples in which a similar approach is adopted are Fortin et al. (1993), Aaberge and Colombino (2006), Colombino et al. (2010), and Blundell and Shephard (20 12).3 Analytical solutions are still crucial for understanding the "grammar" of the problem, and for suggesting promising directions of reform. In contrast, microeconometric models and computational solutions allow for the introduction of less restrictive specifications of preferences and opportunity sets, and for the evaluation of more complex tax-transfer rules. The estimated model we use here represents the choices of both couples and singles, it adopts a flexible specification of the preferences, it accounts for quantity constraints in labour supply choices, and it can income effects can be accounted for, as in Saez (2001), at the cost of notable analytical and computational complications. 2 In Saez (2002), each individual has only three opportunities from which to choose: nonparticipation, and two adjacent labour income brackets. 3 Fortin et al. (1993) have used a calibrated (not estimated) model with rather restrictive (Stone-Geary) preferences, and have focused on alternative income support schemes rather than on the whole tax rule. Aaberge and Colombino (2006) have reported on the preliminary results of a simpler version of the exercise illustrated in this paper. Colombino et al. (2010) have analysed the basic income support mechanisms in some European countries. Blundell and Shephard (2012) have identified the optimal design of a specific UK policy that addresses low-income families with children. However, they have not treated the problem of interpersonal comparability, which, in their case, might be less important, given the smaller and less heterogeneous target population.

accommodate a detailed representation of complex tax-transfer systems. The optimal tax rules turn out to envisage an average tax rate lower than the current one, a modest lump-sum tax (interpretable as a property tax), a negative tax on low incomes (close to mechanisms such as the Earned Income Tax Credit or the In-Work Tax Credit policies), and a progressive MTR profile culminating in a 100 per cent MRT on very high incomes (about 1.5 per cent of the sample). This scenario contrasts sharply with the results obtained by the numerical exercises inspired by the leading contribution of Mirrlees (1971). It is closer to the picture that is typically revealed by empirical applications that adopt the theoretical results of Saez (2002). However, using a flexible microeconometric model as a computational tool, we are able to explore a larger variety of tax-transfer rules, and to perform a more articulated analysis of the effects of the various rules upon different segments of the population. Obviously, the results of our computational exercise cannot claim a generality that is similar to the analytical solutions. While analytical solutions establish an explicit relationship between the fundamentals of the economy (preferences, skill distribution, etc.), the results of our computational exercise are application-specific (in this paper, Norway-specific); this is the price of taking into account a more detailed and flexible representation of preferences and opportunity sets. However, in principle, this limitation of our computational exercise can be overcome. By performing similar exercises on many different economies, it should again be possible to identify -empirically -a more general relationship between the fundamentals of the economy and the optimal income tax rule. As explained in Section II, the microeconometric model used in this study contains 78 parameters that capture the heterogeneity of preferences and opportunities among households and individuals. The estimated model is used to simulate the choices, given a particular tax rule. Thus, these choices are generated by preferences and opportunities that vary across the decision units. However, because preferences are heterogeneous and because some individuals are single, whereas others form families and live together, when it comes to social evaluation it does not make sense to treat the estimated utility functions as comparable individual welfare functions. In order to solve the interpersonal comparability problem, we adopt a method that consists of using a common utility function in order to produce interpersonal^ comparable individual welfare measures to be used as arguments of the social welfare function. The common utility function is justified as a normative standard where the social planner treats individuals symmetrically, and it is only used to compute and compare the individual welfare levels that provide the basis for the social welfare evaluation of tax reforms; it is not used for simulating household behaviour (where, instead, the estimated individual utility functions are used). This procedure, which circumvents the problem of interpersonal comparability of heterogeneous preferences, is well established in the body of the literature concerning empirical public economics. It has been proposed by Deaton and Muellbauer (1980) and Hammond (1991), and it forms the basis for the definition and measurement of a money-metric measure of utility in King (1983) and Aaberge et al. (2004). Moreover, it has been applied, for example, by Fortin et al. (1993), Colombino (1998), and Colombino et al. (2010). As a practical matter, an average of the estimated individual utility functions or an estimated utility function (individual welfare function) with common parameters (as in our case) is typically used. We present a brief description of the microeconometric model in Section II. The empirical specification of the model and the estimates of the model parameters have already been provided by Aaberge and Colombino (2011). In order to illustrate the behavioural implications of the estimates, in Section II, we report the wage elasticities of labour supply, whereas Aaberge and Colombino (2011) have presented the income elasticities. Because the microeconometric model, once estimated, is used for a rather ambitious purpose (i.e., simulating choices with a view to identifying optimal tax rules), it is important to check its reliability. Ultimately, the model should be judged on its ability to carry out the job it has been built for (i.e., predicting the outcomes of policy changes). In Section II, therefore, we perform an out-of-sample prediction exercise where we use the model (estimated on 1994 data) to predict household-specific distributions of income in Norway in 2001. In Section III, we present the social welfare evaluation method and the computational procedure for solving the optimal taxation problem. The resulting optimal rules are presented in Section IV In Section V, we provide some final comments.

## II. Modelling Framework

Microeconometric Labour Supply Model In this section, we present a sketch of the microeconometric model. A full description has been given by Aaberge and Colombino (2011). The model can be considered as an extension of the standard multinomial logit model, and it differs from the traditional models of labour supply in several respects.4 First, it accounts for observed as well as unobserved heterogeneity in preferences and constraints. Second, it includes both single-person households and married or cohabiting couples who make joint laboursupply decisions. A proper model of the interaction between spouses in their labour-supply decisions is important, because most of the individuals 4Examples of previous applications of this approach can be found in Aaberge et al. (1995, 1999, 2000, 2004).

are married or cohabiting. Third, by taking all the details of the tax system into account, the budget sets become complex and non-convex in certain intervals. For expository simplicity, in this section we consider only the behaviour of a single-person household. The extension to couples has been fully explained by Aaberge and Colombino (2011). The agents choose a job from alternatives characterized by the wage rate wf hours of work A, and other characteristics j. The problem solved by the agent is max U (c, h, s J) (w,h,sJ)eB

S.t.

c = f(wh, I) (1) where h is hours of work, w is the pre-tax job characteristics (besides h and w; e.g., oc unobserved (by the analyst) job and/or hou pre-tax non-labour income (exogenous), c i / is the tax rule that transforms gross pr disposable income c, and B is the set of the household (including non-market oppor i.e., "jobs" with w = 0 and h = 0). Agents preferences and in their wage (as in the the number of available jobs of different agent, wage rates (unlike in the traditional job. Let p(h,w,s) denote the density of a By representing the choice set B by a prob example, allow for the fact that jobs wit range are more or less likely to be found, characteristics, or for the fact that, for diffe of market opportunities might differ. We a can be factorized as U [f(wh, /), A, 5, j] = v [f(wh, /), A, s] s(J' (2) where v and e(J) are the systematic and random components, respectively. The term e(J) is a random variable, which accounts for the effect on utility of all the characteristics of the household -job match that are observed by the household but not by us. Moreover, we assume that e(J) is independently and identically distributed, according to the type III extreme value distribution. We observe the chosen A, w, and s. Therefore, we can specify the probability that the agent chooses a job with observed characteristics (h,w,s ). It can be shown that, under assumptions (1) and (2), and given the extreme value distribution for s, we can write the probability density function of a choice (h,w,s) as5 v _ v[f(wh,Ifh,s]p(h1w,s)

V'W'S _ f f fv[f(xy,I),y,z]p(y,x,z)dxdydz' The density (3) is the contribution of an observation (h, w, s) to the likelihood function, which is then maximized in order to estimate the parameters of v [/(Aw, /), h,s] and p(h, w,s). The intuition behind expression (3) is that the probability of a choice (h,w,s) can be expressed as the relative attractiveness -weighted by a measure of availability p(h, w, s)-of jobs of type (h, w, s ). Given convenient parametric specifications of the functions v and p, the 78 parameters of the model can be estimated by maximizing the likelihood function formed on the basis of expression (3). The estimation is based on 1994 data collected by the 1995 Norwegian Survey of Level of Living, which includes detailed income data from tax reported records.6 We have restricted the ages of the individuals to between 20 and 62 in order to minimize the inclusion in the sample of individuals who, in principle, are eligible for retirement, because an analysis of retirement decisions is beyond the scope of this study. Moreover, the self-employed, as well as individuals receiving permanent disability benefits, are excluded from the sample. The sample contains 1,842 couples, 309 single females, and 312 single males. The estimates are reported in Aaberge and Colombino (201 1). When interpreting the random utility model illustrated above, it is important to stress that, in the model, household members choose from a set of jobs (characterized by A, w, and other characteristics s and y), not just from jobs that differ in hours of work h. Thus, the responses of households include many dimensions: hours, wage rates, and non-pecuniary job characteristics. Theoretical optimal taxation models typically consider effort as the agents' choice variable. Effort does not coincide with hours of work; it might include searching for jobs of better quality, putting more effort into each hour of work, or even configuring reported incomes in a more favourable way in view of taxation. A related concept -taxable income -has been used, among others, by Feldstein (1995) and Gruber and Saez (2002). The idea is that in evaluating the effects of changes in taxes, one should not just look at hours of work (and participation), because household responses include many other dimensions. At least some of these multidimensional responses are reflected in taxable income. However, the structural empirical models of labour supply used for tax-reform evaluations have traditionally 5 For the derivation of the choice density (3), see Aaberge et al. (1999). Note that density (3) can be considered as a special case of the more general framework developed by Dagsvik (1994). A more specialized type of continuous multinomial logit was introduced by BenAkiva and Watanatada (1981). 6 At the time of performing the exercise presented in this paper, the 1994 sample was chosen because of the relatively stable macroeconomic conditions.

considered hours of work as the sole choice variable, implicitly equating hours of work and effort. An exception has been provided by Bourguignon and Spadaro (2005), who under rather special assumptions have been able to impute to each agent an effort value. Our model does not strictly equate effort to hours of work, because households -as a response to a change in the tax system -might choose a new job that differs from the previous job, with respect not only to hours of work but also to wage rate and other job characteristics. However, while we account for the disutility of hours of work and choice of sector, we only implicitly account (through the random utility component) for the fact that the other dimensions of effort might also bear a utility cost. Therefore, we cannot claim that our model is completely consistent with the "effort-taxable income" approach. We return to this limitation in Section V Behavioural Implications In this section, we illustrate some of the behavioural implication of the estimates. First, we report the wage elasticities of labour supply because they are useful for understanding and interpreting the optimal taxation results that are presented in Section IV Second, because the model is used for a rather ambitious operation (i.e., computing optimal tax-transfer rules), we illustrate the prediction performance of the model with an out-of-sample exercise. The wage elasticities reported in Table 1 are computed by means of stochastic simulation. Note that the households face exogenous opportunity joint density functions of h, w, and s. Because many individuals in this labour supply model of discrete choice will not react to small exogenous changes, the elasticities in Table 1 have been computed as an average of the percentage changes in labour supply from a 10 per cent increase in the means of the wage densities. Given the simulated responses of each individual, we aggregate these to compute the aggregate elasticities. We find that the overall wage elasticity is equal to 0.12, which suggests rather low behavioural responses. However, by looking behind the overall elasticity, the picture changes substantially. The major features of the estimated labour supply elasticities can be summarized as follows: (a) labour supply for married women is far more elastic than for married men; (b) individuals belonging to low-income households are much more elastic than individuals belonging to high-income households. As demonstrated, for example, by Roed and Strom (2002) and Meghir and Phillips (2008), these results are consistent with the findings in many recent studies. The profile of the wage elasticity across the income deciles is related to the hours worked. Households belonging to the higher-income brackets, on average, participate more and work longer hours; other things being equal, this tends Table 1. Labour-supply elasticities with respect to wage for single females, single males, married females, and married males by deciles of household disposable income (Norway, 1994)

Female elasticities Male elasticities

Income decile Own Own Type of under the 1994 wage Cross wage Cross Family status elasticity tax system elasticities elasticities elasticities elasticities Single females Elasticity of the I 0.59 0.00 and males probability of II 0.45 0.00 participation III-VIII 0.06 0.06

## IX

## X

0.00 0.00

All

Elasticity the of 0.00 0.00 0.12

## I

conditional 0.04 -0.17

## II

-0.04 0.77 0.00 expectation of III-VIII -0.08 -0.08 total supply of IX -0.07 0.00 hours

## X

0.00

All -0.09 0.00 -0.02

Elasticity of the I 0.42 0.77 unconditional

## II

0.42 0.00

expectation of III -VIII -0.02 -0.02 total supply of IX -0.07 0.00 hours

## X

0.00 0.00

All 0.02 0.02 Married/ Elasticity of the I 1 .03 -0.28 0.90 -0.23 cohabitating probability of II 0.35 -0.14 0.79 0.00 females and participation III -VIII 0.14 -0.23 0.13 -0.10 males

## IX

0.12 -0.12

0.06 -0.06

## X 0.07 0.00 0.06 -0.19

All 0.21 -0.19 0.23 -0.11 Elasticity of the I 1.51 -0.01 0.87 0.11 conditional

## II

0.62 -0.53

0.38 -0.08

expectation of III-VIII 0.27 -0.24 0.18 -0.14 total supply IX 0.08 -0.22 0.02 -0.09 of hours

## X 0.19 -0.10 -0.02 -0.23

All 0.31 -0.25 0.16 -0.13 Elasticity of the I 2.54 -0.29 1.77 -0.12 unconditional II 0.97 -0.67 1.17 -0.08 expectation of III-VIII 0.41 -0.47 0.31 -0.24 total supply IX 0.20 -0.34 0.08 -0.14 of to hours lower the

## X 0.26 -0.10 0.05 -0.42

All 0.52 -0.42 0.39 -0.23 wage elasticity of labou elasticities are relevant in many c modelling joint household decision

In principle, elasticities such as t to compute optimal tax-transfer et al. (2007), and Blundell et al. (2 tion I, we do not think that this p of the possible oretical inconsistencies optimal taxation

The editors of betwe model

The an

Scandinavian Table 2. Current tax rule in Norway; as of 1994, for singles without children and for couples without children and with two wage earners Gross earnings

## (NOK

1994)

Tax (0-17,000) 0 (1 7,000-24,709) 0.25x-4,250 (24,709-28,250) 0.078x (28,250-140,500) 0.302x-6,328 (140,500-208,000) 0.358x-14,196 (208,000-234,500) 0.453x-33,956

## (234,500-) 0.495X-43,804

Notes: x denotes annual earnings.

10,000 NOK ~ 1,250 euros.

the elasticities.

tioned above,

For

Tax exam typically ado and income effects.7 Mic that are much more flexi ical results. The approac flexibility, and guarante the optimal tax-transfer the microeconometric model of household behaviour until the social welfare function is maximized under the constraint that the total net tax revenue remains constant. For the out-of-sample prediction exercise, we have used the model estimated on the 1994 sample and the 2001 data (exogenous variables) from the 2002 Norwegian Survey of Level of Living, in order to predict the choices made in 2001 under the new 2001 tax rules.8 Tables 2 and 3 describe some of the characteristics of the 1994 and 2001 tax regimes. The basic features of the 1994 Norwegian tax system were determined by the major tax reform of 1992, which introduced a so-called dual income tax system characterized by a 28 per cent flat tax rate on capital income, in combination with progressive tax rates on labour income plus 7.8 per cent social insurance contribution. Further measures broadened the tax base of business income substantially, and removed various previous tax credits and deductions. In order to reduce incentives for taxpayers to classify labour income as capital income, the reform established rules for mandatory income splitting for dividing business income into capital and labour income, 7 Aaberge and Colombino (2006, 2011) have reported on more detailed results for wage and income elasticities. Income effects are not negligible; their order of magnitude is close to the order of magnitude of wage elasticities and they vary substantially across gender, household type, location in the income distribution, and composition of income. 8 Both 1994 and 2001 data are characterized by relatively stable macroeconomic conditions.

Table 3. The 2001 tax function for singles without children and for couples without children and with two wage earners Gross earnings

## (NOK

2001)

Tax [0-22,200) 0 [22,200-32,267) 0.25x-5,550 [32,267-60,600) 0.078x [60,600-144,545) 0.358x-16,968 [1 44,545-1 83, 1 82) 0.296x-8,064 [1 83, 1 82-289,000) 0.358-x-l 9,348 [289,000-793,200) 0.493x-58,363 [793,200-) 0.553x-105,955

Notes: x denotes annual earnings.

10,000 NOK ~ 1,250 euros.

Table in 4.

2001,

Observed as mean and decile

Tax pre inco

Couples Single females Single males Deciles Observed Simulated Observed Simulated Observed Simulated 1 50 49 45 47 41 42 2 68 64 56 61 54 55 3 77 74 68 71 65 67 4 83 83 79 79 76 76 90 88 87 86 5 89 6 7 90 95 102 98 107 101 111 98 108 97 107 97 108 8 111 117 123 121 119 121 9 125 131 139 138 137 141 10 199 187 189 188 218 207 with the resulting imp progressive surtax.

The of small and the businesses 2001, marginal surtax, w rate increased, re

Table 3.

Disposable inco outcomes to observed o individual, evaluating t nent drawn from the ty and identifying the sel level.

The individual pr the 10 income deciles.

## T

diction exercise.

The m distribution.

The editors of

The

## S

## III. Design of Optimal Income Taxes

Framework of the Social Planner The body of literature on optimal taxation relies on the maximization of social welfare functions, defined as summary measures of the distribution of individual utility levels, where utility levels are assumed to be interpersonally comparable. In this section, we explain the method adopted for allowing the aggregation of comparable individual welfare levels and the computational procedure used to solve the optimal taxation problem.

Individual Welfare Functions Because the microeconomic labour supply model used in this study allows heterogeneous preferences for leisure and consumption and, moreover, because some individuals are singles and others live as couples, it makes no sense to treat the estimated utility functions as comparable individual welfare functions. Thus, it is necessary to introduce measures of individual welfare that permit interpersonal comparisons.9 Here, we follow an approach similar to the approaches advocated by Deaton and Muellbauer (1980), King (1983), and Hammond (1991). Specifically, we use a common utility function to evaluate the bundles chosen by the households according to their own preferences.10 The common utility function (or individual welfare function) is to be interpreted just as the input of a social welfare function. It is not used to simulate behaviour, only to evaluate -in a comparable way -the results of choices made according to the actual individual utility functions. The individual welfare function V used by the social planner is specified as log V(y, h) = K2 + Y4 (^-^) • (4) Here, L is leisure, defined as L = 1 -(A /0.8736), and y is the individual's equivalent after tax income, defined by c = f (wh, I) for singles ^ y = c I -= = -f (wpAp, wmAm, I) for m

## V2 V2

9 See Boadway et al. (2002) and Fleurbaey and Maniquet (2006) for a personal comparability of utility when preferences for leisure differ be 10An alternative approach has been recently proposed and illustrated (2010).

Table 5. Estimates of the parameters of the individual welfare function (Norway, 1994)

Variable

Income

Parameter after tax

Estimate

Std (y)

## Y' -0.649

## Y2 3.026

Leisure (L) dev.

0.086 0.138

## Y3 -12.262 0.556

## Y4 0.045 0.011

where F and M denote fe tional form of expressio the utility functions in t bino, 2006, 2011). By divi incomes of couples into to estimate the paramete expression (3) with the sy by the individual welfar opportunity densities p. T the model of Section II. T

A different way to circu is to avoid interpersonal the social evaluation excl example of this method "winners" under the optim

Social

Welfare

Function

When evaluating the distr system and/or a tax ref losses using a social welf the one that adds up the objection to the linear ad are given equal welfare w rich.

However, concern for

11 The square root scale is one tions. The number of household specification of the utility fun leisure (Aaberge and Colombin

12 This is just an illustration;

a different definition of the o winners).

are assigned larger welfare weights than rich individuals. This structure is captured by the family of rank-dependent welfare functions,13 w= [q(t)F~'t)dt, (6)

Jo where F~l is the left inverse of the cumulative distribution function of the individual welfare levels V with mean /z, and q(t) is a positive weightfunction defined on the unit interval. The social welfare functions (6) can be given a normative justification similar to the one underlying the expected utility social welfare functions introduced by Atkinson (1970). Given suitable continuity and dominance assumptions for the preference ordering defined on the family of distributions F, Yaari (1987, 1988) has demonstrated that the following axiom characterizes the family of rankdependent measures of social welfare functions (6), where q(t) is a positive non-decreasing function of t. Axiom (Dual Independence). Let F¡, F2, and F3 be members of F and let ot G [0, 1]. Then, F'>F2 implies [«Ff1 + (1 -a)^-1]-1 idctFî1 + (1 -a)F3"1]-1. We refer to Yaari (1987, 1988) for a discussion of the difference betwee the dual independence axiom and the conventional independence axiom used to justify the expected utility social welfare functions. In this paper we use the following specification of q(t ):

-log t, k = 1 qk^ = 1 k~Tļ ~ ř*~l)' * = 2, Note that the inequality aversion exhibited by the social ^(associated with qu(t)) decreases with increasing k. As proaches inequality neutrality and coincides with the linea function defined by

W00= f F~'t)dt = n

Jo It follows, by straightforward calculations, that Wk < ß for all k and that Wk is equal to the mean ¡jl for finite k if and only if F is the egalitarian distribution. Thus, Wk can be interpreted as the equally distributed individual welfare level. As recognized by Yaari (1988), this property suggests

13 Several other authors have discussed the rationale for rank-dependent measures of inequality and social welfare (e.g., Sen, 1974; Hey and Lambert, 1980; Donaldson and Weymark, 1980, 1983; Weymark, 1981; Ben Porath and Gilboa, 1994; Aaberge, 2001).

Table 6. Distributional weight profiles of four different social welfare functions

Wx (Bonferroni) W2 (Gini) W3 (Utilitarian) q(0.01)/q(0.5) q(0.05)/q(0.5) q(0.30)/q(0.5) q(0.95)/q(0.5) that

Ck , 6.64 4.32 1.74 0.07 1.98 1.90 1.40 0.10 defined 1.33 1.33 1.21 0.13 1 1 1 1 by

Wk

Ck = l--, k= 1,2,..., (9) ß can be used as a summary measure of inequ (2000, 2007), C' is actually equivalent to the proposed by Bonferroni (1930), whilst C2 is (2000, 2007) has demonstrated that C' exhibi aversion, and is particularly sensitive to chang of the population, whilst C2 normally pays take place in the middle part of the income dis exhibits upside inequality aversion, and is changes that occur in the upper part of the the close relationship between Cy, C¿, and C treating them as a group, and calling them inequality measures. In order to ease the int aversion profiles exhibited by W 1, W2, W the ratios of the corresponding weights -d median individual and the 1 per cent poorest, t per cent poorest, and the 5 per cent richest welfare criteria. As can be observed from th Table 6, W' will be particular sensitive to c the welfare of the poor, whereas the inequa rather moderate, and Wœ exhibits neutrality w Optimal Taxation Problem We strictly consider only personal income ta of the optimal income tax literature, all the 14Note that Aaberge (2001) has provided an axiomatic ju as the criteria for ranking Lorenz curves. Thus, the just Wk = ļi(1 -e*), defined by equation (6) (and equatio a value judgement of the trade-off between the mean welfare.

tax system (VAT, consumption taxes, payroll taxes, social assistance, etc.) have been kept constant, as of 1994 in Norway. The optimal taxation problem considered in this exercise can be formulated as max fV[V(y1F, hiF), V(y2F, h2F), ■■■, V(ynF, h„F),

## Ů

V(ym, ^im)> V(y2M, A2m ), • • •, V(jnM, A„m)] s.t.

yi F = y¡ M = Ci/y/ 2, 1 = 1,2,...,/!

y, [wífAÍF + wím^ím + 1¡ -/(VF,FA,F, Ii', #)] >: G /•= 1 (c¿, A, F, A, M. ÍÍF, ÍÍM. ji) = arg max U¡ (c, AF) AM, sF, ím, y) s.t. c¡ (w,h,s,j)€Bj = /(w/fA/f, W/MA/M, //;#), / = 1,2,...,«. Here, n is the number of households, and G denotes the total net tax revenue required (set equal to the current one in our exercise). For simplicity of exposition, expression (10) assumes that n households are couples, whereas, in fact, we consider both couples and singles. In expression (10), each couple contributes to the social welfare functions, with two terms corresponding to the individual welfare functions of the two partners. For singles, we have just one term V(yif h,) and y¡ = c/ (according to expression (5)). All the variables are the same as those that appear in expression (1). The function c, = /(vv/fA/f, Wiuhiuli' which transforms gross incomes (w/pAfF, w/mAím, Ii) into net available income c,, denotes a class of tax rules defined up to a vector of parameters ů. We consider a class of piecewise-linear tax rules with a (positive or negative) lump-sum transfer and five income brackets. Therefore, the parameters are the amount of the lump-sum transfer, the lower and upper limits of the income brackets, and the MTR applied to the income brackets. Household / maximizes its own utility given the tax rule /(w,-pA,-F, w/mA/m^ ;#) by choosing the job (e,-, A/f, A/m, Si?, j/m» jó-Taking the individual utility-maximizing choices into account as a constraint (i.e., the incentive-compatibility constraint), the social planner searches for the tax rule (i.e., the parameter vector ů) that maximizes the social welfare function W, subject to the constraint that the total net tax revenue must at least be as large as G. The social welfare function W takes as arguments the evaluations of the chosen jobs, according to the individual welfare function V. Given the very flexible and general specifications adopted for the random utility functions and of the opportunity sets (Aaberge and Colombino, 2011), problem (10) cannot be solved analytically. The maximization of W is performed by a global maximization procedure that efficiently scans the parameter space. At each run of (10) the iterative procedure, the maximization of the individual utility function is simulated by the microeconometric model described in Section II. The search for the optimal tax rule is limited to the class of piecewise-linear rules, with five brackets:

z + d -TļZ if 0 < z < zi;

/-1 z + d-^ti (z,--Z,_i) -Tl (z-Z/_i) c= if f if i=1 f z/_ ^ i < < z ^ / < z/, 0 / 2, = 0 2, 3, 4;

4 Z + d -T| (z,--Z/_i) -Ts (z -Z4) if z > Z4.

1=1 Here, c is the net available income, z is the sum of gross market income (earnings plus capital income) and taxable public transfers, (ri, T2,..., r 5) are the MTRs applied to the five income brackets, zř is the upper limit of the ith bracket (1 = 1, 2, 3, and 4), zo = 0 and d is a lump sum that can be positive (i.e., a lump-sum transfer) or negative (i.e., a lumpsum tax). Thus, each particular tax rule is characterized by 10 parameters (ri, T2, t3, t4, T5, zi, Z2, Z3, Z4, d). The tax rule is quite flexible because the MTRs are allowed to be positive or negative (less than 1 in absolute value), and the bracket limits are allowed to take any positive value only subject to the constraints z,-> zf-_ 1. The tax rule specified by expression (11) replaces the current rule, as of 1994, whose main characteristics are illustrated by the examples of Table 2, and also belongs to the class of piecewise linear tax rules.15 The dataset is the same as the one used for the estimation of the model (Section II). The identification of the optimal tax rules consists of the following four steps.

(a) For each household, we simulate the opportunity set, which contains the observed job plus 199 market and non-market alternatives drawn from the estimated p densities defined in Section II. For each household and each alternative in the opportunity set, we then draw a value e from the type III extreme value distribution. Next, the new tax rule is applied to the gross incomes of the individual earners in order to obtain disposable incomes (income after tax) corresponding to each alternative in the choice set. For each household, a new choice (c, Ap, j) for couples or {c,h,s,j) for singles -is given by the alternative that

15 Taxes include the part of social security contributions paid by the employee.

Table 7. Optimal tax rules according to alternative social welfare criteria

Social welfare function

W' (Bonferroni) W2 (Gini) W3 (Utilitarian) x' -0.30 -0.80 -0.70 -0.80 r2 0.06 0.20 0.22 0.24 r3 0.29 0.26 0.26 0.29 r4 0.39 0.38 0.37 0.33 t5 1.00 1.00 1.00 1.00 d -13,600 -7,500 -5,200 -5,800 zi 10,000 10,000 10,000 10,000

## Z2 120,000 130,000 140,000 230,000

## Z3 220,000 230,000 240,000 290,000

## Z4 730,000 720,000 720,000 790,000

Notes: d, z¡, Z2,z3, and Z4 are in 1994 NOK (10,000 maximizes the household-specific u tion (2). 16 (b) To each decision maker (wife, husband, or single), an equivalent income y is imputed according to expression (5). The purpose of this procedure is to convert the distribution of incomes (c) across heterogeneous families into a distribution of (equivalent) incomes (y) across adult individuals.

(c) As a result of the previous steps, now for each individual we have a simulated pair (y, h ). Then, we compute the individual welfare levels by applying to the chosen (y, h) the individual welfare function (4).

(d) Then, we compute the social welfare function Wk for k = 1, 2, 3, oo.

The optimization is performed by iterating steps (a) -(d) in order to find the tax rule in the class (11) that produces the highest value of Wk for each value of k, under the constraint of constant total net tax revenue.17

## IV. Optimal Tax-Transfer Schedules

The results of our exercise are reported in Tables 7-11. Table 7 displays the optimal tax rules. In order to make it easier to compare the behavioural responses to the 1994 tax system and to the various optimal tax systems, we 16Colombino (1998), Colombino et al. (2010), and Blundell and Shephard (2012) have used a different method, where the maximum utility is not found by simulation but is measured instead by the expected maximum utility (McFadden, 1978). The two methods are asymptotically equivalent, but the method adopted in this paper turns out to be more flexible and robust for producing disaggregated results.

17The optimal tax-transfer parameters are determined by an iterative grid-search procedure developed by Tom Wennemo at the Research Department of Statistics Norway. Each optimization requires the evaluation of approximately 200,000 tax-transfer rules.

Table 8. Percentage of individuals by income intervals under different tax systems Proportions located in various gross income segments Couples Couples Single Single

Income intervals (males) (females) males females 1994 tax system 0-30,000 5 16 0 0 30,000-130,000 11 33 26 24 130,000-230,000 31 35 41 51 230,000-730,000 52 16 33 24 730,000> 2 0 0 0

## IF

i -optimal tax system 0-30 000 2 10 0 0 30,000-130,000 9 32 22 22 130,000-230,000 29 41 42 51 230,000-730,000 58 17 35 27 730,000> 2 0 0 0 ^-optimal tax system 0-30,000 3 12 0 0 30,000-130,000 9 32 23 22 130,000-230,000 28 39 41 50 230,000-730,000 59 17 36 28 730,000> 1 0 0 0

FF3-optimal tax system 0-30,000 3 12 0 0 30,000-130,000 8 31 23 21 130,000-230,000 27 39 41 50 230,000-730,000 60 17 36 28 730,000> 2 0 0 0 ^Foo -optimal tax system 0-30,000 3 13 0 0 30,000-130,000 8 31 22 20 130,000-230,000 25 37 40 50 230,000-730,000 62 18 38 30 730,000> 2 0 0 0 report the proport brackets in

Table the behavioural im percentages of wi 1994 income distribution. Under any social welfare function, the MTRs are continuously increasing for all levels of income. Clearly, the pattern of elasticities -sharply decreasing with respect to income -illustrated in Table 1 contributes to the profile of the optimal MTR. The most striking results are represented by the negative MTR on the first bracket and by the 100 per cent MTR on the last bracket. These results are obviously driven by the pattern of the elasticities displayed in Table 1. From each of the panels of Table 1, we Table 9. Percentage changes in participation rates, annual hours of work, and disposable income under the optimal tax rules

Social welfare function

W i (Bonferroni) W2 (Gini) W3 (Utilitarian) Single males Participation rates 2.3 2.3 2.3 2.3

Annual hours 4.9 5.0 5.1 6.0

Disposable income 10.0 9.7 10.0 11.9 Single females Participation rates 4.0 4.4 4.4 4.8

Annual hours 6.0 6.6 6.6 9.0

Disposable income 4.7 4.6 4.5 6.6 Couples Participation rates, M 2.6 2.3 2.3 2.7

Participation rates, F 5.8 4.3 3.9 3.3

Annual hours, M 5.9 6.2 6.6 9.4

Annual hours, F 10.6 8.1 7.0 6.3

Disposable income 9.2 9.4 9.9 13.3 Table 10. Percentage changes in labour supply income decile under the optimal tax rules

Social welfare function

Income decile

## W'

Wqq under the (Bonferroni) W2 (Gini) W3 (Utilitarian) 1994 system Male Female Male Female Male Female Male Female Singles I 60.5 64.7 57.3 54.4 62.8 54.4 62.8 60.3

## II 18.6 17.9 18.6 21.3 18.6 21.3 20.3 29.3

## III-

## VIII

## IX

## X

0.0 1.3

All 0.9 3.0 1.2 4.5 0.0 0.0 0.0 0.0 1.3 0.0 4.9 6.0 5.0 1.1 0.0 1.3 6.6 4.5 0.0 0.0 5.1 1.7 2.6 6.6 7.2 -0.4 1.3 0.0 6.0 9.0 Couples I 50.4 74.4 43.8 60.7 42.8 56.0 49.5 60.8

## II 22.2 22.9 23.3 19.5 22.9 20.5 32.7 18.6

## III-

## VIII

## IX

## X

0.7 -3.3

All 2.6 0.5 0.0 5.9 5.1 4.2 0.7 -2.9 0.2 -2.9 6.2 that changes elastic.

3.5 1.0

10.6 observe

to 7.7 0.7 8.1 6.7 1.2 0.9 6.6 the in 3.6 0.5 7.0 -1.4 0.1 9.4 6.3 labour

Moreover, in by particular responsive 18

Except

## MTR

The and than when the editors of of incenti comparing for females those w belo participation.1 income wage

The supply economic married/cohabitating tion), 2.7 -0.3 effects elasticities

Scandinavian are is

Journal ass com of

Eco Table 1 1. Percentage of winners under optimal tax rules

Social welfare function

Income decile

## W'

Wœ under the (Bonferroni) W2 (Gini) W 3 (Utilitarian) 1994 system Male Female Male Female Male Female Male Female

Singles

## II

## III-

## I

79 66

## VIII

## IX

## X

Couples

## II

86 79 76

All

## I

68 45 85 83 34 79 38 62 64 64 72 84 71 72 85 87 69 79 80 62 67 73 84 86 70 70 81 72 81 79 62 69 55 68 55 77 66 45 83 48 38 86 41 76 61 79 73 79 55 83 86 88 72 83 62 68 45 82 85

All 72 55 63 70

## IX

83 66 82

## III-VIII

## X

76 62 62 65 61 73 84 64 70 87 73 83 87 88 90 88 91 74 72 79 78 79 83 80 82 a subsidy or a tax credit on plemented, such as the Wor

Income Tax Credit in the U

The 100 per cent MTR on t hardly be realistically impl our model. As shown in Ta average, a wage elasticity o (with the exception of mar ment of the population (1.5 of hours, despite a reductio characteristics of induce to them the job (cap choose job their earnings become a ren rule).19 This argument car pletely inelastic in our mod might represent emerging from compensated wage a very our signi exercis elasticity con uncompensated wage elasticities. H (reported by Aaberge and Colomb inversely related to the income lev 19An anonymous referee correctl be willing to

However, we cent, because accept a MTR abov decided to constrai official

The rates editors of above

The

Scand obtained by the numerical exercises based on the optimal tax formulae of Mirrlees. The typical outcome of these exercises envisages a positive lump-sum transfer, which is progressively taxed away by very high MTRs on lower incomes (i.e., a negative income tax mechanism); after the income level where the transfer is exhausted, the tax rule is close to proportional. However, Tuomala (2010) has suggested that these results are essentially forced by the restrictive assumption typically made upon preferences, elasticities, and distribution of productivities (or wage rates). Table 7 shows that the more egalitarian the social welfare criterion, the more progressive the optimal tax rule. For example, the optimal rule according to Bonferroni is more progressive than the optimal rule according to Gini, which, in turn, is more progressive than the optimal utilitarian rule. The lump sum d turns out to be a tax. This result can be explained by the fact that households with low or average/incomes are particularly sensitive to changes in marginal taxes (see Table 1). Thus, the MTRs on low and average incomes are kept low, both for minimizing distortions and for fulfilling distributive goals. However, because the total net tax revenue must be kept unchanged, the optimal tax rule envisages a universal lumpsum tax. A possible practical implementation close to a lump-sum tax might be represented by a tax on wealth or on property (e.g., on owneroccupied houses). According to this interpretation, the optimal tax rules would imply -with respect to the 1994 rule -a lower taxation on earnings complemented by a property tax. All the optimal rules imply a higher income after tax for most levels of gross income (Table 9). In other words, the optimal rules are able to extract the same total tax revenue from a larger total gross income (i.e., under a lower average tax rate). Together with the optimal MTRs of Table 7, this result provides a controversial perspective in view of the tax reforms implemented in many developed countries during the last decades. In most cases, these reforms have embodied the idea of improving efficiency and labour-supply incentives through a lower average tax rate and lower MTRs on the highest incomes.20 Our results give clear support to the first part (i.e., lowering the average tax rate). As for the second part, the picture is less clear-cut. Our results suggest that a lower average tax rate should be mainly obtained by lowering the marginal and average tax rates, particularly on low and average incomes (and also on a substantial part of high incomes), and by sharply increasing them on very high income levels.21 20For example, Blundell (1996) has reported that, during the 1980s and early 1990s, in some countries, the top MTRs were cut from 70-80 per cent down to about 40-50 per cent. Concerning these issues, the discussion by Roed and Strom (2001) is especially relevant. 21 A second important difference between our exercise and the implemented reforms referred to in the main text is that these reforms typically envisaged a reduction of the total tax Table 10 shows that the strongest labour-supply response comes from households in the lower income deciles (i.e., those who show a more elastic labour supply). While females in couples receive a stronger incentive to work under the Bonferroni regime than under the Utilitarian regime, the opposite is the case for the males. This is because the wife faces, on average, lower wages than the husband, and the lower tax brackets are more relevant for her (i.e., those where the Bonferroni regime imposes much lower MTRs than the Utilitarian -and the current -regime). However, the Utilitarian regime is especially favourable (also compared to the current regime) for those who decide to locate themselves in high tax brackets, where husbands are more likely to be found. The implication is that a more egalitarian criterion also involves stronger work incentives for married women (and especially those in the lower income deciles), and therefore also a more egalitarian intergender distribution of income. Table 11 shows the percentage of winners under the optimal rules, by marital status, gender, and household income decile under the current 1994 rule. Individuals are defined as winners if their welfare is higher under the new tax rule than under the current 1994 rule. All the optimal rules would largely "win the referendum" against the current rule, because they all imply a strong majority of winners. However, the percentage of winners varies substantially across the different subgroups, and especially across income deciles. Single women in the IX and X income deciles are the only ones who would "vote against" all the optimal tax rules. The current (1994) tax system provides important deductions that favour, in particular, the group of relatively well-off single women with children. The deductions are removed in the class of tax-transfer rule we optimize upon. As a consequence, a majority of these women turn out to be losers under the optimal rules.

## V. Conclusions

We have performed an exercise in designing optimal income taxes. Unl what is typically done in the literature, in this exercise we do not rely on priori theoretical optimal taxation results, but instead we employ a mic conometric model of labour supply in order to maximize a social welf function with respect to a parametrically defined income tax rule. M ern microeconometric models of labour supply are based on very gene and flexible assumptions. They can accommodate many realistic featur such as general structures of heterogeneous preferences, simultaneous cisions of household members, complicated (non-convex, non-continuou revenue, together with a reduction in the average tax rate, while in our simulations we the total tax revenue unchanged.

non-differentiable, etc.) constraints and opportunity sets, multidimensional heterogeneity of both households and jobs, quantitative constraints, etc. It is simply not feasible (at least, so far) to obtain analytical solutions for the optimal income taxation problem in such environments. Yet, these features are very relevant and important, especially in view of evaluating or designing reforms. Analytical solutions remain indispensable for understanding the grammar of the problem, and for suggesting promising classes of tax-transfer systems that can then be more deeply investigated with the microeconometric model.22 The microeconometric model adopted in this paper, and fully described by Aaberge and Colombino (2006, 2011), is designed to allow for a detailed description of complex choice sets and budget constraints. The model is used to identify, by simulation, the tax rule that maximizes a social welfare function. We have kept fixed the current (1994) system of transfers, income support, and social assistance policies, but we allow for a lump sum that can be positive (i.e., a transfer) or negative (i.e., a tax). We have explored a variety of different social welfare criteria. The MTRs always turn out to be monotonically increasing with income. More egalitarian social welfare functions tend to imply more progressive tax rules. For all the social welfare functions used, the optimal bottom MTR is negative and the optimal top MRT always turns out to be 100 per cent for sufficiently high gross income levels (depending on the social welfare function, approximately above 720,000-790,000 NOK 1994), which concerns not more than 2 per cent of the tax payers. The negative MTR on the lowest income bracket suggests a mechanism close to policies such as the Working Families Tax Credit in the UK or the Earned Income Tax Credit in the USA. The 100 per cent top MTR can be mainly explained by the inelastic labour supply at the top of the income distribution (Table 1) and by non-pecuniary characteristics that might make a job attractive, even though it carries a 100 per cent MTR. All the optimal tax rules imply an average tax rate lower than the current 1994 one, and imply -with respect to the current rule -lower marginal rates on low and/or average income levels, and a higher marginal rate on very high income levels. The pattern of wage elasticities of labour supply illustrated in Section II helps to explain the profile of the optimal tax rules. Our results are partially at odds with the tax reforms that have taken place in many countries during the last decades. While these reforms have embodied the idea of lowering average tax rates, the way in which they have been implemented has typically 22 The philosophy inspiring this approach is similar to the one adopted long ago in engineering and also, recently and successfully, in other applications of mechanism design (auctions, negotiation procedures, matching markets, etc.) where analytical solutions are complemented by computational simulations or experiments that account for a host of realistic features, which cannot be included in the theoretical model. Roth (2002) has provided a very inspired survey of this approach.

consisted of reducing the top marginal rates. In contrast, our results suggest lowering average tax rates by reducing marginal rates, except for those of very high income levels. Even though we think that the approach illustrated here can usefully complement theoretical work and analytical solutions, and actually improve upon them concerning the representation of preferences, constraints, and policies, clearly there are many dimensions of the tax-transfer rules that are relevant for their evaluation (e.g., implementation and administrative costs) but are beyond the purpose of our exercise. Moreover, some of the results illustrated in Section IV might change with the inclusion in the behavioural model of features that are currently not taken into account. A candidate for further refinements is the modelling of the choice by households at the top of the income distribution. For example, the optimal top MTR might turn out to be lower than 100 per cent if we were able to fully account for other dimensions of households' responses, such as intercountry mobility and taxable income response (see Feldstein, 1995; Gruber and Saez, 2002).23

## References

Aaberge, R. (2000), Characterizations of Lorenz Curves and Income Distributions, Social

Choice and Welfare 17, 639-653.

Aaberge, R. (2001), Axiomatic Characterization of the Gini Coefficient and Lorenz Curve

Orderings, Journal of Economic Theory 101, 115-132.

Aaberge, R. (2007), Gini's Nuclear Family, Journal of Economic Inequality 5, 305-322.

Aaberge, R. and Colombino, U. (2006), Designing Optimal Taxes with a Microeconometric Model of Household Labour Supply, IZA Discussion Paper No. 2468.

Aaberge, R. and Colombino, U. (2011), Empirical Optimal Income Taxation: A Microeconometric Application to Norway, CHILD Working Paper No. 16/2011.

Aaberge, R., Colombino, U., and Strom, S. (1999), Labour Supply in Italy: An Empirical Analysis of Joint Household Decisions, with Taxes and Quantity Constraints, Journal of

Applied Econometrics 14, 403-422.

Aaberge, R., Colombino, U., and Strom, S. (2000), Labour Supply Responses and Welfare Effects from Replacing Current Tax Rules by a Flat Tax: Empirical Evidence from Italy, Norway and Sweden, Journal of Population Economics 13, 595-621.

Aaberge, R., Colombino, U., and Strom, S. (2004), Do More Equal Slices Shrink the Cake?

An Empirical Investigation of Tax-Transfer Reform Proposals in Italy, Journal of Population Economics 17, 767-785.

Aaberge, R., Dagsvik, J. K., and Strom, S. (1995), Labour Supply Responses and Welfare Effects of Tax Reforms, Scandinavian Journal of Economics 97, 635-659.

Atkinson, A. B. (1970), On the Measurement of Inequality, Journal of Economic Theory 2, 244-263.

23 However, based on previous exercises where we constrained the top MTR to be lower than 100 per cent, we expect the overall qualitative features of the optimal tax rule to remain unaffected.

Ben-Akiva, M. and Watanatada, T. (1981), Application of a Continuous Spatial Choice Logit Model, in C. F. Manski and D. McFadden (eds.), Structural Analysis of Discrete Data with

Econometric Applications, MIT Press, Cambridge, MA.

Ben Porath, E. and Gilboa, I. (1994), Linear Measures, the Gini Index, and the IncomeEquality Trade-Off, Journal of Economic Theory 64, 443-467.

Blundell, R. (1996), Labour Supply and Taxation, in M. Devereux (ed.), The Economics of

Tax Policy, Oxford University Press, Oxford.

Blundell, R., Brewer, M., Haan, P., and Shephard, A. (2009), Optimal Income Taxation of Lone Mothers: An Empirical Comparison of the UK and Germany, Economic Journal

## 119, F101-F121.

Blundell, R. and Shephard, A. (2012), Employment, Hours of Work and the Optimal Taxation of Low Income Families, Review of Economic Studies 79, 481-510.

Boadway, R., Marchand, M., Pestieau, P., and Racionero, M. (2002), Optimal Redistribution with Heterogeneous Preferences for Leisure, Journal of Public Economic Theory 4, 475-498.

Bonferroni, C. (1930), Elementi di Statistica Generale, Seeber, Firenze.

Bourguignon F. and Spadaro, A. (2005), Tax-Benefit Revealed Social Preferences, PSE

Working Paper 2005-22.

Colombino, U. (1998), Evaluating the Effects of New Telephone Tariffs on Residential Users' Demand and Welfare. A Model for Italy, Information Economics and Policy 10, 283-303.

Colombino, U., Locatelli, M., Narazani, E., and O'Donoghue, C. (2010), Alternative Basic Income Mechanisms: An Evaluation Exercise with a Microeconometric Model, Basic

Income Studies 5(1).

Dagsvik, J. K. (1994), Discrete and Continuous Choice, Max-Stable Processes and Independence from Irrelevant Attributes, Econometrica 62, 1179-1205.

Deaton, A. and Muellbauer, J. (1980), Economics and Consumer Behavior, Cambridge University Press, Cambridge.

Decoster, A. and Haan, P. (2010), Empirical Welfare Analysis in Random Utility Models of

Labour Supply, IZA Discussion Paper 5301.

Diamond, P. (1980), Income Taxation with Fixed Hours of Work, Journal of Public Economics 12, 101-110.

Diamond, P. (1998), Optimal Income Taxation: An Example with a U-Shaped pattern of Optimal Marginal Tax Rates, American Economic Review 88, 83-95.

Donaldson, D. and Weymark, J. A. (1980), A Single Parameter Generalization of the Gini Indices of Inequality, Journal of Economic Theory 22, 67-86.

Donaldson, D. and Weymark, J. A. (1983), Ethically Flexible Indices for Income Distributions in the Continuum, Journal of Economic Theory 29, 353-358.

Feldstein, M. (1995), The Effect of Marginal Tax Rates on Taxable Income: A Panel Study of the 1986 Tax Reform Act, Journal of Political Economy 103, 551-572.

Fleurbaey, M. and Maniquet, F. (2006), Fair Income Tax, Review of Economic Studies 73, 55-84.

Fortin, B., Truchon, M., and Beauséjour, L. (1993), On Reforming the Welfare System:

Workfare Meets the Negative Income Tax, Journal of Public Economics 31, 119-151.

Gruber, J. and Saez, E. (2002), The Elasticity of Taxable Income: Evidence and Implications,

Journal of Public Economics 84, 1-32.

Hammond, P. J. (1991), Interpersonal Comparisons of Utility: Why and How They Are and Should Be Made?, in J. Elster and J. E. Roemer (eds.), Interpersonal Comparisons of Well-Being. Studies in Rationality and Social Change, Cambridge University Press, in collaboration with Maison des Sciences de l'Homme, Cambridge, 200-254.

Haan, P. and Wrohlich, K. (2010), Optimal Taxation: The Design of Child-Related Cash and

In-Kind Benefits, German Economic Review 11, 278-301.

Hey, J. D. and Lambert, P. J. (1980), Relative Deprivation and the Gini Coefficient: Comment, Quarterly Journal of Economics 94, 567-573. King, M. (1983), Welfare Analysis of Tax Reforms Using Household Data, Journal of Public Economics 21, 183-214. Kleven, H. J., Kreine, C. T., and Saez, E. (2009), The Optimal Income Taxation of Couples, Econometrica 77, 537-560. Immervoll, H., Kleven, H. J., Kreiner, C. T., and Saez, E. (2007), Welfare Reforms in European Countries: A Microsimulation Analysis, Economic Journal 117, 1-44. McFadden, D. (1978), Modeling the Choice of Residential Location, in A. Karlqvist, L. Lundqvist, F. Snickars, and J. Weibull (eds.), Spatial Interaction Theory and Planning Models, North-Holland, Amsterdam, 75-96. Meghir, C. and Phillips, D. (2008), Labour Supply and Taxes, IZA Discussion Paper no. 3405. Mirrlees, J. A. (1971), An Exploration in the Theory of Optimal Income Taxation, Review of Economic Studies 38, 175-208. Revesz, J. T. (1989), The Optimal Taxation of Labour Income, Public Finance 44, 453-475. Roth, A. E. (2002), The Economist as Engineer: Game Theory, Experimental Economics and Computation as Tools of Design Economics, Econometrica 70, 1341-1378. Roed, K. and Strom, S. (2002), Progressive Taxes and the Labour Market-Is the Trade-Off between Equality and Efficiency Inevitable?, Journal of Economic Surveys 16, 77-100. Saez, E. (2001), Using Elasticities to Derive Optimal Income Tax Rates, Review of Economic Studies 68, 205-229. Saez, E. (2002), Optimal Income Transfer Programs: Intensive versus Extensive Labour Supply Responses, Quarterly Journal of Economics 117, 1039-1073. Sen, A. (1974), Informational Bases of Alternative Welfare Approaches, Journal of Public Economics 3, 387-403. Tuomala, M. (1990), Optimal Income Tax and Redistribution, Clarendon Press, Oxford. Tuomala, M. (2010), On Optimal Non-Linear Income Taxation: Numerical Results Revisited, International Tax and Public Finance 17, 259-270. Weymark, J. (1981), Generalized Gini Inequality Indices, Mathematical Social Sciences 1, 409-430. Yaari, M. E. (1987), The Dual Theory of Choice under Risk, Econometrica 55, 95-115. Yaari, M. E. (1988), A Controversial Proposal Concerning Inequality Measurement, Journal of Economic Theory 44, 381-397. First version submitted April 2010; final version received November 2011.
