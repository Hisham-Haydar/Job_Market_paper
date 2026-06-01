# Journal of Economic Inequality (2006) 4: 77–106

DOI: 10.1007/s10888-005-9012-6

#

Springer 2005

Microsimulation as a tool for evaluating redistribution policies

FRANÇOIS BOURGUIGNON 1 and AMEDEO SPADARO 2,3,j 1 The World Bank and PSE -Paris-Jourdan Sciences Economiques-(Joint research unit 8545 CNRS -EHESS-ENPC-ENS), Paris, France, E-mail: fbourguignon@worldbank.org 2 PSE -Paris-Jourdan Sciences Economiques-(Joint research unit 8545 CNRS -EHESS-ENPC-

ENS), Paris, France.

3 Department of Applied Economics, Universitat de les Illes Balears, Ctra Valldemossa Km 7,5, 07122, Palma de Mallorca, Spain, E-mail: amedeo.spadaro@uib.es (Accepted: 22 September 2005) Abstract. During the last 20 years, microsimulation models have been increasingly applied in qualitative and quantitative analysis of public policies. This paper discusses microsimulation techniques and their theoretical background as a tool for the analysis of public policies. It next analyses basic principles for using microsimulation models and interpreting their results, with emphasis on tax incidence, redistribution and poverty analysis. It then discusses social welfare analysis permitted by microsimulation techniques and points to the limits of present approaches and some directions for future developments.

Key words: evaluation of public policies, inequality, microsimulation, poverty, redistribution.

JEL Classification Codes: C81, D31, H21, H23, H31.

1. Introduction Microsimulation models (MSMs) allow simulating the effects of a policy on a sample of economic agents (individual, households, firms) at the individual level. Policy evaluation is based on representations of the economic environment of individual agents, their budget constraints and possibly their behaviour. A policy simulation then consists of evaluating the consequences of a change in the economic environment induced by a policy reform on a vector of indicators of the activity or welfare for each individual agent in a sample of observations. The microsimulation approach in economics imitates the experimental approach in biology or psychology – with one major difference. Experimentation in biology and psychology compares the observed state and behaviour of agents before and after a change to their environment. In economics, the simulation j

Corresponding author.

78

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

bears only on the change in the environment and on Fimputed_ changes in behaviour or welfare. The comparison is thus made ex ante rather than ex post. 1 To be sure, ex post evaluations are also possible in economics, and the field of Fimpact evaluation_ is growing quickly (see [47]). But the approach often can be too cumbersome, costly and time consuming for real-time policy analysis. The use of MSMs in economics for public decision-making started to develop only recently. Orcutt 2 planted the seed of microsimulation as an instrument for economic analysis in 1957, but only since the early 1980s has the use of MSMs developed, a consequence of the rise of large and detailed datasets on individual agents and the continuing increases in, and falling costs of, computing power. 3 The usefulness of microsimulation techniques in the analysis of public policies has two aspects. First is the possibility of fully taking into account the heterogeneity of economic agents observed in micro-datasets. Working with some Ftypical agents_ (typical households or typical firms) is often the first approach to evaluating the impact of fiscal and social policies. It gives a general idea about the consequences of the reform being analysed, but it can hide unexpected effects from certain combinations of individual characteristics that could not be apprehended through Ftypical cases._ In addition, even when various Ftypical cases_ are considered, it is never clear how representative they are. Working with thousands of actual economic agents rather than a few hypothetical ones avoids these difficulties by identifying with precision who are likely to be the winners and losers of a reform. Such information is crucial to evaluate the overall welfare effect of the reform as well as political economy factors that may hamper its implementation. Second is the possibility of accurately evaluating the aggregate financial cost/ benefit of a reform. The results obtained with an MSM at the level of individual agents can be aggregated at the macro level, allowing the analyst to evaluate the effect of the policy on the government budget. Clearly, the standard Ftypical case_ approach could not permit such an accurate evaluation of the budgetary cost of a policy reform. Because of these strong advantages over the Frepresentative agent_ approach, and because of continuing progress in data availability and computing, the microsimulation approach to economic policy analysis is bound to intensify and deepen. Moreover, as analysts conduct more complicated calculations, they are likely to modify the microsimulation exercises. Indeed, this is under way. Microdata now occupy a considerable space in applied economic analysis, giving rise to more sophisticated treatment. The purpose of this paper is to review the application of microsimulation techniques to the evaluation of redistribution policies and to point to the most promising directions for further developments. By doing so, it must be clear however that this paper leaves aside other fields of application of microsimulation and therefore other techniques.

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

79 2. A taxonomy of microsimulation models applied to redistribution policies The common structure of MSMs for redistribution analysis comprises three elements: 1) a micro-dataset, containing the economic and socio-demographic characteristics of a sample of individuals or households; 2) the rules of the policies to be simulated – that is, the budget constraint facing each agent; 3) a theoretical model of the behavioural response of agents. Existing MSMs differ on this last dimension. Behavioural responses that may be of relevance for redistribution policies include labour supply, savings and household composition. A clear taxonomy of models can be established according to the inclusion of some behavioural responses, the time dimension of these responses and the partial or general equilibrium focus. MSMs that ignore behavioural responses altogether are sometimes called arithmetical models. This type of model simply applies the change in the budget constraint that households face because of the reform in redistribution policy – without taking into account any change in their market income and in their demographic composition. Based on market incomes and the socio-demographic characteristics of a household, they arithmetically derive its disposable income and net tax payments given the rules for the computation of taxes and benefits in the policy being analysed. The simplicity of these models is rather appealing, even though the computation of taxes and benefits in most advanced redistribution systems requires a few thousand lines of code. Behavioural MSMs include a detailed representation of the behavioural response of individuals and households to changes in their budget constraint. The type of behaviour taken into account differs across models, even though consumption and labour supply are the most frequent focus of interest. Given the system of pre-tax prices and wage rates, and given the shape of the budget constraint, behavioural MSMs compute the optimal consumption demand and labour supply of each agent. To do so, a model of consumption and labour supply must have been estimated, or possibly Fcalibrated_, and must be incorporated in the model’s framework. Such a model allows for more detailed analysis of household welfare and of the redistribution authority’s aggregate budget constraint. The time dimension of MSMs depends on the object of the analysis and the kind of behavioural response incorporated in the model. For instance, evaluating the effects of a reform of the income tax that would modify the treatment of children will have little effect on household composition in the short run. An arithmetical MSM would then be sufficient. Long-run effects, however, require simulating the impact of the tax reform on fertility decisions. A dynamic framework may then become necessary where households are followed over time. Likewise, the microsimulation of changes in the parameters of the taxbenefit system that affect inter-temporal consumption allocations, retirement, training, schooling and so on must be analysed with a dynamic MSM rather than a static model.

80

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

If labour supply effects arising from a reform of the tax-benefit system are large enough, changes in the structure of wages and prices may be expected to take place. Most models ignore these general equilibrium effects and may thus be called Fpartial equilibrium_ models. However, MsMs that take into account general equilibrium effects are also being developed. Some of them may be related to the now-prolific Computable General Equilibrium literature and essentially try to link sectoral models to a household micro-database. Others limit themselves to a subset of markets, most often the labour market. It would also be possible to establish a taxonomy of MSMs according to their field of application in the broad area of redistribution policies: indirect taxation, direct taxation, social security systems, non-contributory benefits and so on. Because this paper is more methodological than policy-oriented, it sticks with the preceding taxonomy. The rest of this paper reviews such models and their use, with emphasis on their implicit or explicit economic assumptions and on the appropriate way of interpreting their results.

3. Arithmetical microsimulation and tax incidence analysis Arithmetical MSMs in the redistribution field simulate the change in the real disposable income of individuals or households due to a change in the rules for calculating tax or benefit payments under the assumption that individual behaviour is unchanged. Thus, the effect of an increase in the indirect tax rate on good i for individual j is to reduce the Freal_ disposable income of j by an amount equal to the change in the final price caused by the tax times the consumption of good i by that individual. Likewise, the effect of a reform of the income tax is the change in the real disposable income that it generates for constant market income from labour or other sources. Under these assumptions it is a simple matter, at least conceptually, to identify the winners or losers of any reform of the tax-benefit system and to compute how much everyone loses or gains in real disposal income. The assumption of unchanged behaviour has often been criticised, but it is not as restrictive as it would appear. Under some conditions, they are fully consistent with behavioural responses. They simply estimate the first-round effect, itself a good approximation of final welfare effect if changes are small enough and individuals are thought to operate in perfect markets.

## 3.1. THEORETICAL JUSTIFICATION OF ARITHMETICAL MICROSIMULATION

The familiar utility theory of consumer behaviour provides a simple income metric of a change in welfare due to any modification of the budget constraint.

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

81 To measure a household’s welfare gains and losses from a reform, define V i (p, y i) as the indirect utility function of that household (indexed i):

V i ð p; y i Þ ¼ U x M ð p; y i Þ with x M ð p; y i Þ ¼ Arg max f U i ð x i Þ s:t: px i y i g ð1Þ where y i is household i’s income, p the price vector that it faces, U i (x) its direct utility function and x M (p, y i) its vector of Marshallian demand functions. The welfare effect of a public policy affecting marginally household i_s income at constant prices p is given by V i = V yi y i, where V yi is its marginal utility of income. Inverting this expression, one may express any change in the welfare of individual i in an Bequivalent^ variation of income, y i *:

y * i ¼ V i = V y i ð2Þ In other words, there is complete equivalence between the change in the welfare income metric, y i *, and the change in welfare once a value has been selected for the marginal utility of income V yi. But the latter is essentially unobserved and has therefore to be chosen arbitrarily on a purely normative basis. Consider now a policy change that affects the price vector p. Differentiating the indirect utility function yields:

## X

V ij p j ð3Þ

V i ¼ j where V ij is the derivative of the indirect utility function with respect to the price p j. From the envelope theorem, or Sheppard’s lemma or Roy theorem, it is known that:

ð p; y i Þ V j ¼ V y i :x M j ð4Þ Replacing in Equation (3) and using the welfare income metric definition Equation (2), the change in the price vector p causes a change in the welfare of individual i equivalent to a change in income given by:

## X

x ij p j ð5Þ y i * ¼ j where x ji is the actual consumption of good j by household i. The preceding equation fully justifies the arithmetical microsimulation approach. It implies that the change in the welfare income metric due to a change in price is simply equal to the change in the cost of the consumption basket due to the price change p. This result generalizes easily to the case where the Fconsumption_ vector x also includes labour supply or possibly the production of certain goods by the household itself. In this more general case, 82

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

call y i 0 the income of household i that is truly exogenous – that is, income not coming from labour or from the sale of goods. The preceding argument implies that:

## X

x ij p j þ y 0 i ð6Þ y * i ¼ j where x ji is now to be interpreted as the Fnet_ demand of good (or labour service) j by the household. Then, imagine a change in the tax-benefit system that affects the price the household receives for the goods and services it sells on the market, its exogenous income y i 0 and possibly the price of the goods that it consumes. The preceding expression shows that the change in the welfare of agent i may be obtained by applying the new price system generated by the reform of the taxbenefit system to the agent’s initial bundle of consumption, production and labour supply. This is exactly the assumption behind the arithmetical microsimulation approach. Since the preceding argument applies only at the margin, it can be shown moreover that the same reasoning applies when the price system is non-linear, as with tax-benefit systems in most developed countries – through instruments like progressive income taxes or means-tested benefits. According to the foregoing argument, it is erroneous to present arithmetical MSMs as being based on the assumption that agents’ behaviour is totally rigid. In effect, this approach to the evaluation of policy reforms is fully consistent with the existence of behavioural responses. The point is simply that these responses may be ignored when evaluating individual change in welfare levels, if some specific conditions hold: that the reform is causing only Fmarginal_ changes in the budget constraint faced by agents, and that all agents are optimising under their sole budget constraint, which implies that all markets are perfect in the sense that agents are never rationed. If this argument justifies that arithmetical MSMs may ignore behavioural responses when evaluating changes in individual and social welfare, it does not offer the same justification when evaluating changes in tax revenues or benefit payments due to a reform. The envelope theorem cannot be invoked in that case, and it is simply not true that raising the tax rate on a specific good will increase revenues proportionally to the initial consumption of that good. Thus, arithmetical MSMs do not permit taking the budget constraint of the government rigorously into account, when strong behavioural responses to a reform are expected. Another case where behavioural responses cannot be dispensed with and the envelope theorem is insufficient is when redistribution or tax-incidence analysis focuses on other criteria than individual welfare. Consider studies of the way various policies affect income poverty, with poor people defined as those whose monetary income is below some predetermined threshold. In this case, too, accounting for labour–supply responses is indispensable, even though such a strict definition of poverty may be debated.

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

83 Still other sources of inaccuracy are present in the arithmetical MSM approach. 4 The first comes from the assumption, often made when using arithmetical MSMs for tax-incidence analysis, that tax changes are completely passed on to consumers’ prices or net wages. This would be true only in a longrun competitive market equilibrium (a hypothesis that may be far from reality). To be fully rigorous, some type of partial or general equilibrium model taking into account the production side of the economy should be used to determine how a change in the tax system translates into changes in consumer or producer prices and changes in wage rates. Tax evasion and non take-up of the benefits are other important sources of inaccuracy in arithmetical MSMs. These models are normally built under the hypothesis that taxpayers report all their incomes and that any household entitled to a certain benefit actually cashes it. In reality, tax evasion often is common, and some households do not ask for social assistance even though they are entitled to it by the law. 5 This may occur because of social stigma, a lack of information or the complexity of the administrative procedures. Moreover, some households may be receiving benefits, even though they do not qualify for them, because of information problems in the management of the system. 6 Tax evasion and non take-up could be handled without too much difficulty if it could be assumed that they would not be affected by a reform of the tax-benefit system. It would be sufficient to observe this phenomenon in the database used for the simulation. But this is unlikely. Increasing income tax rates makes tax evasion more profitable, other things equal, and increasing a benefit makes non take-up more costly. In other words, tax evasion and non take-up may be part of the behavioural responses ignored in the arithmetical MSMs.

## 3.2. EXAMPLES OF APPLICATION

There is an extensive literature on the application of arithmetical MSM techniques to the analysis of reforms of tax-benefit systems. Atkinson and Sutherland [10], Merz [81], Citro and Hanusheck [32], Harding [58], Sutherland [99], Gupta and Kapur [55], among others, offer surveys of MSMs and their use in Europe and United States. 7 Tax incidence analysis and the analysis of the incidence of public spending in education or health also belong to the arithmetical MSM tradition (see [34, 93] for tax incidence and [40] for public spending).

In Europe, the analysis of policy reforms at national and continental levels has received particular attention, especially for the harmonization of tax and social policies. Atkinson, Bourguignon and Chiappori [8] analyse the effect, for a given sample of French households, of replacing the French tax-benefit system with the British. De Lathouwer [38] simulates the implementation of the unemployment benefit scheme enforced in the Netherlands for a sample of Belgian households, shedding light on the importance of the socio-demographic characteristics of the 84

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

population for the performance of a redistributive system. Callan and Sutherland [29] compare the effects of different types of fiscal and social policies on the welfare of households in certain EEC countries. Bourguignon and others [21] use a microsimulation model to simulate the effects of enforcing the same child benefit scheme on the populations of France, the United Kingdom and Italy. Atkinson and others [9] analyse the effect of introducing universal minimum oldage income in a larger number of European countries. 8 By definition, MSMs provide information on the way every individual or household in a sample is affected by a reform in the redistribution system. This allows identifying precisely the gainers and the losers from a reform and their characteristics. In general, however, information at the individual level must be aggregated to be of some policy significance. Typically, individuals or households are grouped by socio-demographic characteristics or by initial level of real income or welfare. Changes in their disposable income due to the reform are given for these various groups. Most models also provide changes in several social welfare indicators computed for the whole population. These include the mean disposable income per adult equivalent, inequality indices (Gini, Theil and Atkinson measures with varying inequality aversion parameters), several poverty measures and the application of relative or absolute Lorenz dominance criteria. 9 Several models also provide information on the distribution of the effective marginal tax rates in the population, defined as the additional disposable income resulting from an additional currency unit of market income after taking into account changes in taxes and benefits. Although no behavioural response is taken into account in the model, these marginal tax rates give information on the labour supply incentives for a particular tax-benefit system. Changes in these marginal tax rates can be useful because they indicate the likely direction of behavioural responses and whether the direction is different for people with different characteristics. 10 4. Behavioural microsimulation models and social welfare analysis Because ignoring behavioural reactions can lead to misleading results in several situations, this section discusses how behavioural responses may be introduced in MSMs and applied to social welfare analysis.

## 4.1. BUILDING A BEHAVIOURAL MICROSIMULATION MODEL

As with arithmetical models, behavioural MSMs rely on micro-data on households, but they add something important to the analysis. The point is not only to count how much more or less everyone is receiving or paying because of a reform in his or her budgets constraint but also to take into account the behavioural response of the agents to this change. This may be done through the estimation of a structural econometric model for the cross-section of households

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

85 in the survey being used or through the calibration of a behavioural model with some predetermined structure, to make it consistent with behaviour actually observed in the survey. Tax-benefit models with labour supply responses are the archetypical example of behavioural MSMs. Changes in the tax-benefit system in these models affect the budget constraint of households. They modify their disposable income with unchanged labour supply, but through the corresponding income effects-and through changes in the after-tax price of labour, they also modify labour supply decisions. By how much is determined through simulating a model of labour supply behaviour. The behavioural MSM approach thus comprises three steps: specifying the logical economic structure of the model being used, estimating or calibrating the model and simulating it with alternative reforms of the tax-benefit system. These steps are considered in turn. 11

## 4.2. THE STANDARD CONTINUOUS MODELLING OF LABOUR SUPPLY

The logical economic structure is that of the textbook utility-maximizing consumer. An economic agent i with characteristics z i chooses his or her volume of consumption c i and his or her labour supply L i to maximize his or her preferences represented by the utility function u() under a budget constraint that incorporates the whole tax-benefit system. Formally, this is represented by:

Max u ð c i; L i; z i;; " i Þ s:t: c i y 0i þ w i L i þ NT ð w i L i; L i; y 0i; z i; Þ; L i 0 ð7Þ In the budget constraint y 0i stands for (exogenous) non-labour income, w i for the wage rate and NT() for the tax-benefit or Fnet tax_ schedule. Taxes and benefits depend on the characteristics of the agent, his or her non-labour income and his or her labour income, w i L i. It may also depend directly on the quantity of labour being supplied, as in workfare programmes. The term stands for the parameters of the tax-benefit system: various tax rates, means-testing of benefits and so on. Likewise, and " i are coefficients that parameterise preferences, the first common, the second idiosyncratic. The solution of that programme yields the following labour supply function:

L i ¼ F ð w i; y 0i; z i;; " i; Þ ð8Þ This function is non-linear. In particular, it is equal to zero in some subset of the space of its arguments – that is, the non-participation solution. Suppose now that a sample of agents is observed in some household survey. The problem is to estimate the function F() above, or equivalently the preference parameters and " i, since all the other individual-specific variables or tax-benefit parameters are observed. To do so, preference parameters are broken down into a set of coefficients common to all agents, and a set " i that is idiosyncratic, playing the usual role of the random term in standard regressions.

86

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

Estimation proceeds as with standard models, minimizing the role of the idiosyncratic preference term in explaining cross-sectional differences in labour supply. This leads to a set of estimates ^ for the common preference parameters and " ^ i for the idiosyncratic preference terms. For each observation in the sample:

L i ¼ F z i; w i; y 0i; ^; " ^ i;

ð9Þ It is now possible to simulate alternative tax-benefit systems. This simply requires modifying the set of parameters. 12 In the absence of general equilibrium effects, the change in labour supply due to moving to the set of parameters s is given by:

ð10Þ L si L i ¼ F z i; w i; y 0i; ^; " ^ i; s F z i; w i; y 0i; ^; " ^ i;

The change in the disposable income may also be computed for every agent. It is given by:

C i s C i ¼ w i L si L i þ NT y 0i; w i L si; L si; z i; s NT ð y 0i; w i L i; L i; z i; Þ ð11Þ Now, one may also derive changes in any measure of individual welfare. Several difficulties in the foregoing model must be emphasized. Its estimation generally is not easy. It is highly non-linear because of the non-linearity of the budget constraint and possibly its non-convexity due to the tax-benefit schedule NT() and corner solutions at L i = 0. Functional forms must be chosen for preferences, which may introduce some arbitrariness in the whole procedure. Finally, it may be feared that imposing full economic rationality and a functional form for preferences severely restricts the estimates obtained. There has been a debate on this point since the first model of this type [59] appeared in the literature (see [78]).

## 4.3. USING DISCRETE CHOICE MODELS OF LABOUR SUPPLY

It turns out that simpler and less restrictive specifications may be used, considerably weakening the critiques. In particular, specifications used in recent work consider labour supply as a discrete variable that may take only a few alternative values and evaluate the utility of the agent for each of these values and the corresponding disposable income given by the budget constraint. As before, the behavioural rule is simply that agents choose the value that leads to the highest level of utility. But the utility function may be specified in a very general way, with practically no restriction. Such a representation is therefore as close as possible to what is revealed by the data.

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

87 Formally, a specification that generalizes what is most often found in the recent tax-benefit labour supply literature is the following:

L i ¼ D j if U i j ¼ f z i; w i; c i j; j; " i j U i k ¼ f z i; w i; c i k; k; " i k for all k 6¼ j ð12Þ where D j is the duration of work in the jth alternative, U ij the utility associated with that alternative and c ij the disposable income given by the budget constraint in Equation (7):

c i j ¼ y 0i þ w i :L i þ NT w i D j; D j; y 0i; z i;

ð13Þ When the function f() is linear with respect to its common preference parameters j and additive with respect to the idiosyncratic terms " ij, and when those terms are iid with a double exponential distribution, this model is the standard multinomial logit. It may also be noted that it encompasses the initial model Equation (7). It is sufficient to make the following substitution:

f z i; w i; c i j; j; " i j ¼ u c i j; D j; z i;; " i j ð14Þ This specification, which involves restrictions across the various work duration alternatives, is the one most often used. 13 Even under its more general form, the foregoing specification might still be found restrictive because it relies on some utility-maximizing assumption. Two remarks are important here. First, it must be clear that ex ante incidence analysis of tax-benefit reforms cannot dispense with such a basic assumption. To establish a counterfactual to the reform, the ex ante nature of the analysis requires some assumption about the way agents choose between alternatives. 14 The assumption that agents maximize some criterion defined in the most flexible way across alternatives is not really restrictive. Second, it must be clear that if no restriction is imposed across alternatives, the utility-maximizing assumption is compatible with the most flexible representation of the way labour supply choices observed in a survey are related to individual characteristics, including the wage rate and the disposable income defined by the tax-benefit system NT(). That model (12) can be interpreted as representing utility-maximizing behaviour is to some extent secondary, though this permits implementing counterfactual simulations in a simple way. More important is that this model fits the data as closely as possible. Interestingly, the only restriction on that objective in the general expression (12) is the assumption that the utility associated with each alternative depends on the wage rate and the non-labour income of an individual only through c ij –that is, the disposable income given by the budget constraint and the tax-benefit schedule NT(). 15 The economic structure of this 88

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

model thus lies essentially in the way the income effect is specified. If it were not for that property, it would simply be a reduced-form model aimed at fitting the data as well as possible. In effect, the restriction that the income effect must be proportional to disposable income seems a minimal assumption to ensure that this representation of cross-sectional differences in labour supply behaviour is consistent with elementary rationality. It is also perfectly clear that, within this framework, the simulated effect of a reform of the tax-benefit system NT() on individual labour supply is estimated on the basis of observed cross-sectional differences in disposable income in the status quo. The role of idiosyncratic terms " ^ i or " ^ i j in the whole approach must not be downplayed. They represent the unobserved heterogeneity of agents’ labour supply behaviour. Therefore, they may be responsible for some heterogeneity in responses to a reform of taxes and benefits. It may be seen in Equation (14) that agents otherwise identical might react differently to a change in disposable incomes, despite the fact that these changes are the same for all of them. For this, it is enough that the idiosyncratic terms " ^ i j be sufficiently different. Some will modify their work duration due to a tax-benefit reform, while others will not. Estimates of the idiosyncratic terms result directly from the econometric estimation of the common preference parameters ^ in the continuous specification Equation (9) or ^ i j in the discrete model (12). These are standard regression residuals in the first case and Bpseudo-residuals’’ in the second. But one may also opt for a Bcalibration^ rather than an econometric estimation approach. Some of the coefficients ^ or ^ i j are not estimated but given arbitrary values deemed reasonable by the analyst. Then, as in the standard estimation procedure, estimates of the idiosyncratic terms are obtained by imposing that predicted choices, under the status quo, coincide with actual choices. It is important to emphasize that there is some ambiguity about who the Bagents^ behind the standard labour supply model Equation (7) should be. Traditionally, the literature considers Bindividual agents^, even though the welfare implications of the analysis concern households. Extending the model to households requires considering simultaneously the labour supply decision of all members at working age. This makes the analysis more complex. It becomes practically intractable with continuous representation – see, for instance, Hausman and Ruud [62] – but only lengthens computation time with the discrete approach.

## 4.4. ILLUSTRATIVE APPLICATIONS OF BEHAVIOURAL

## MICROSIMULATION MODELS

Applications of the foregoing models are now numerous. They are surveyed in Blundell and MaCurdy [17] and in Creedy and Duncan [35]. The discrete approach is well illustrated by van Soest [107], Hoynes [67] or Keane and Moffit

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

89 [70]. An application of the Fcalibration_ approach may be found in Spadaro [97]. A nice application of a behavioural MSM, illustrating the potential of this approach, is the work of Blundell and others [16], evaluating the likely effect of introducing the Working Families Tax Credit (WTFC) in United Kingdom. They separately estimate a discrete labour supply model for married couples and single parents for a sample of UK households coming from the Family Resources Survey of 1995 and 1996. Then they use the estimated model to simulate the labour supply responses under the new budget constraint using the TAXBEN MSM developed at the Institute for Fiscal Studies. The results show that behavioural responses reduce the cost estimated in the purely arithmetical scenario by 14%. This is mostly due to the increase in the labour force participation of single mothers and the subsequent increase in tax receipts. Similar analysis has been implemented for recent tax reforms in the United States [67, 70], the Netherlands [37], France [14], Germany [18], Italy [2] and Spain [75]. Applications of behavioural MSMs to indirect tax reforms are also numerous [34, 39, 69, 77, 79, 83, 91, 105]. All these studies evaluate the likely effects of VAT reforms on consumption patterns and individual and social welfare by simulating the consumption behaviour from some system of demands previously estimated with micro-econometric techniques. These types of consumption behavioural microsimulation are surveyed in Symons and Warren [101]. The microsimulation of consumption behaviour has also been used for green tax reforms to evaluate the efficiency and distributive effects of fuel, carbon or CO 2 emissions taxes. They are surveyed in Grubb and others [54], Hoerner and Bosquet [66] and Gago and others [50]. In addition to labour supply and consumption patterns, other dimensions of household behaviour matter for welfare and may be affected by tax-benefit systems. Oportunidades in Mexico, Bolsa Familia in Brazil and similar Fconditional cash transfer programmes_ in several other countries offer a clear example of policies in developing countries that can be evaluated ex ante by behavioural MSMs. 16 Consider the Bolsa Escola programme in Brazil, a part of the broader Bolsa Familia. It consists of a cash transfer to households whose income per capita is below a threshold of 90 Reais (about $45) per month and with a child of school age, conditional on these children effectively attending school. The monthly transfer is equal to 15 Reais per child going to school, limited to 45 Reais per household. This may be considered as a conditional cash transfer programme because it combines cash transfers based on a means – test and some additional conditionality – that is, having children of school age actually going to school. Because the main occupational alternative to school is work, this really is a labour supply problem similar to the one analysed above. Bourguignon and others [20] estimate a multilogit model of schooling and labour supply for all 90

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

children ages 10 to 15 in households surveyed in the Brazilian household survey, PNAD, in a year preceding programme implementation. The identification condition in that model is the following: the way children’s earnings and the income of other household members enter the utility of the various alternatives is uniquely determined through the disposable income of the whole family. After estimating the model of the labour supply/schooling decision without conditional cash transfers, the Bolsa Escola programme was simulated for each of the households in PNAD. The results show that the programme is indeed effective in reducing the number of poor children not going to school, much more than what would result from an unconditional means-tested cash transfer. However, its effect on poverty turned out to be rather limited due to the programme’s limited size. 17 Before moving to some other possible applications of the foregoing framework, three limitations must be stressed. First, it has to be recognized that this approach is difficult to implement because it generally requires the estimation of an original behavioural model that fits the policy to be evaluated or designed – and of course the corresponding micro-data. Because of this, it is unlikely that an analysis conducted in a given country for a particular policy can be applied without substantial modification to another country or in the same country to another type of policy. The methodological investment behind this approach may thus be important. This justifies applying first a pure arithmetical microsimulation approach or a simpler behavioural model based on calibration. Second, the behavioural approach relies on a structural model that requires some minimal set of assumptions, and there generally is no way of testing these assumptions. In the labour supply model with a discrete choice representation, the basic assumption is that wage and non-labour income variables matter for occupational decisions only through the net disposable income they command, as given by the tax-benefit system. By contrast, a reduced-form model would be based independently on wage and non-labour income. Econometrically, the two approaches may not differ much in explanatory power, but clearly the second approach would not permit simulating the effects of any change in the tax-benefit system, since the system itself would be embedded in the model’s coefficients. Third, the strongest assumption is that cross-sectional income effects, as estimated on the basis of a standard household survey, coincide with the income effects that will be produced by the programme or the reforms under study. In other words, time income effects for a given agent are assumed to coincide with observed cross-sectional income differences. Again, this hypothesis is hard to test and yet absolutely necessary for ex ante analysis. Nothing is possible without it. The only test one can think of would be to combine ex ante and ex post analysis. For instance, one could try to run some ex ante analysis on a household survey taken before the implementation of the reform and then compare the results obtained in the ex post evaluations of that programme. Coincidence would support the assumption that cross-sectional and individual-specific income effects are identical. 18

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

91 Because of some possibly strong assumptions there is unavoidably some uncertainty about the predictions that come out of ex ante incidence analysis based on behavioural MSMs. This said, such a tool is absolutely necessary in order to reflect on the optimal design of policies most likely to generate strong behavioural responses.

4.5. BEHAVIOURAL MSMs AND APPLIED OPTIMAL REDISTRIBUTION THEORY Including behavioural responses in an MSM framework allows for explicit analysis of the equity-efficiency trade-off in the spirit of standard optimal redistribution analysis. In arithmetical models, such analysis could be performed only in a very indirect way – for instance, comparing social welfare indicators and the distribution of marginal effective rates across alternative tax-benefit systems, the latter taken as an indicator of the disincentives and distortions caused by these systems. A more rigorous treatment can be used once a behavioural model has been specified. This is discussed below for labour supply behaviour. The specification of labour supply behaviour implicitly refers to preferences represented by some utility function, as in Equations (7)–(8) above. With the same notation, let V(w i, y 0i; z i;, " i;) be the corresponding indirect utility function for individual i. The social welfare function SWF() corresponding to a tax-benefit system with parameters may then be defined as:

SWF ð Þ ¼ n

## X

G ½ V ð w i; y 0i; z i;; " i; Þ ð15Þ i¼1 where n is the number of agents in the population and G[] is the social valuation of individual welfare. G[] is an increasing and concave function, its concavity an indication of the level of aversion towards inequality of the redistribution authority. Following a methodology proposed by King [71], it is often convenient to replace the indirect utility function V() by a money metric y e, defined as the nonlabour income that must be given to the agent in some benchmark situation to raise his or her utility to the level actually achieved with a given policy. Let V i = V(w i, y 0i; z i;, " i;) be the utility actually achieved by individual i when the parameters of the tax-benefit system is. Then, a money metric y e (V i) of V i using the tax-benefit system 0 and the case w i = 0 as a benchmark, is given by the solution to the equation:

V b0; y e ð V i Þ; z i;; " i; 0 e ¼ V i:

ð16Þ The social welfare function may then be defined on the money metric of utility, rather than on the utilities themselves:

92

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

SWF ð Þ ¼ n

## X

f y e ½ V ð w i; y 0i; z i;; " i; Þ g ð17Þ i¼1 where () may now be given the usual interpretation of the social utility of individual Fincome._ The obvious advantage of that transformation of the initial expression of social welfare is that it does not depend any more on the cardinalization of the utility function used to represent individual preferences. 19 Within such a framework, it is possible to perform comparative social evaluation of alternative redistribution policies, as summarized by sets of parameters A and B. This only requires being able to compute the indirect utility functions for each individual i in the population, inverting it as in Equation (16) thanks to some numerical algorithm and evaluating the social welfare SWF associated to each system. 20 Equipped with a numerical algorithm that computes the social welfare associated with a tax-benefit system, it becomes possible to consider optimizing the redistribution, fully taking into account the trade-off between equity and efficiency. The relevant reference here is the optimal taxation literature and the pioneering work of Ramsey [90] and Diamond and Mirrlees [41, 42] for indirect taxation and Mirrlees [82] for direct taxation. Atkinson and Stiglitz [11] and Tuomala [106] offer extensive syntheses of that literature. Behavioural MSMs and the computation of social welfare according to the equations here make possible some simple applications of that literature. The simplest consists of comparing two tax-benefit systems, characterized for instance by two sets of parameters, A and B, and determining which system leads to the highest level of social welfare. Of course, the comparison makes sense only if the budget of the redistribution authority is the same in the two systems-that is, if tax receipts net of transfers are the same with A and B. This corresponds to the standard Bgovernment budget constraint^ in optimal taxation models. An example of this approach is Spadaro [97], where the 1995 French and British tax-benefit systems are microsimulated respectively on samples of French and UK households in order to find which system is the Fbest_ for a given level of social aversion to inequality and for each population. As is usual in this type of work, the constant net tax receipt constraint is taken care of through the introduction in one of the two systems of an artificial tax assumed to be strictly proportional to incomes–and ensures budgetary equivalence across the two systems. 21 A very similar application consists of investigating the effects of modifying some subset of the parameters of a tax-benefit system and seeing whether this improves the social welfare function–allowing, of course, for a constant government budget. If this exercise is repeated for a broad enough set of alternative definitions of the social welfare function, this is equivalent to investigating Pareto – improving reforms of the initial tax-benefit system. Ahmad

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

93 and Stern have pioneered this type of application of MSMs for indirect taxationsee Ahmad and Stern [7]. The foregoing approaches may be seen as a kind of discrete approach to the original optimal taxation theoretical models. An approach closer to those models would optimize a tax-benefit system for some subset of its parameters across some permissible range. In effect, this was the approach developed by Stern [98] when applying Mirrlees’ model to a linear income taxation model. 22 The difference from what could be done today with MSMs is that Stern focused on hypothetical distributions of individual labour productivities rather than the actual ones – and on hypothetical representations of labour supply behaviour rather than accurate econometric estimates of that behaviour. Oddly enough, however, there do not seem to be many recent attempts at using existing behavioural MSMs in that way. Is this because such an approach necessarily relies on the specification of a single social welfare function, which is essentially debatable? Or because econometric estimates of labour supply behaviour in existing MSMs are simply too imprecise? Applying the original models of Diamond and Mirrlees [41, 42] and Mirrlees [85] without functional restrictions to actual MSMs raises major difficulties when the heterogeneity among individuals or households is multidimensional rather than unidimensional. Indeed, households differ not only in their consumption of various goods and their wage rate but also in some socio-demographic characteristics that create differences in the utility they draw from a given level of consumption or in non-labour income. These difficulties come on top of the need to ground optimal taxation on the choice of a specific social welfare function. This explains the limited use of optimal taxation analysis in the applied public finance literature. Another way of using the original optimal taxation models consists of having them reveal the social welfare function implicit in the observed tax-benefit system, given labour supply and consumption behaviour. Known as the Foptimum inverse_ problem, this was first analysed in economics by Kurz [73]. For indirect taxation, one can go back from the observed structure of tax rates across goods and services to the weight of individual households in the social welfare function, depending on their structure of consumption, and under the assumption that the observed indirect taxation system is indeed optimal. For direct taxation, it is also possible to identify the weights of individual households in the social welfare function and to test whether this weight is both positive and decreasing with income, as assumed in the optimal taxation model. Christiansen and Jansen [31] used that approach to study the Norwegian indirect tax system, whereas Ahmad and Stern [7] showed that the 1979–1980 Indian indirect tax system could not be Pareto optimal and derived from the optimum inverse approach directions for Pareto-improving reforms. Bourguignon and Spadaro [23] analysed the redistribution system in France, the United Kingdom and Spain using the optimum inverse approach based on the Euromod MSM and 94

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

a calibrated model of labour supply. They found that revealed social preferences satisfy the usual regularity assumptions – positive and decreasing marginal social welfare of individual utility – as long as the wage elasticity of labour supply is below some threshold. For Spain and the United Kingdom, this threshold seems reasonably above the range of available econometric estimates of the wage elasticity of labour supply. For France, however, the threshold is much lower, so that it cannot be ruled out that revealed social preferences are non-Paretian beyond some income level [24]. Using the same type of method, Oliver and Spadaro [85] analyse how the 1999 reform of the income tax in Spain may be interpreted as resulting from a change in social preferences with respect to inequality.

5. Extensions and directions for future research The microsimulation approaches to the evaluation of redistribution policies discussed here were defined within a partial equilibrium and static framework. But redistribution policies may have powerful general equilibrium effects–for instance, by modifying the sectoral structure of the economy in the case of indirect taxation. They may also affect the whole lifetime budget constraint of people and therefore some important decisions in their life cycle. To cover these important dimensions of redistribution policies, several extensions of the basic arithmetical and behavioural MSMs have been proposed or are being researched. This final section outlines them.

## 5.1. MICRO–MACRO MODELLING AND MICROSIMULATION

A promising direction of research is the integration of macro models and MSMs, the Fmicro–macro_ approach to modelling. Numerous economy-wide models, particularly the Computable General Equilibrium models, 23 already incorporate several Frepresentative households_, which are used to analyse the distributional effects of economy-wide policies and possibly the indirect, general equilibrium effects of redistribution policies. The full integration of economy-wide modelling and MSMs consists of replacing these Frepresentative households_ by actual households as observed in standard household surveys. Several attempts have been made in that direction.

## 5.2. TOP–DOWN APPROACHES

The simplest link between economy-wide modelling and the MSM approach proceeds top down. A policy is simulated at the macro-level, based on some aggregate representation of household behaviour, possibly using representative households. The simulated changes in prices, wage rates and self-employment

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

95 incomes are then passed down to a microsimulation module as in arithmetical MSMs. In other words, the welfare effects of changes in prices and wage rates are computed according to the envelope theorem for all households in a microdatabase. An excellent example of this approach is the analysis of the distributional consequences of China’s accession to the WTO by Chen and Ravallion [30]. 24 There are two drawbacks to linking an arithmetical MSM to an economy-wide modelling tool. The first is that the envelope theorem is based on the assumption that all markets are perfectly competitive. The second is that the possible economy-wide feedback effects of the distributional consequences of a given policy are not taken into account. 25 Bourguignon and others [22] generalized the preceding approach to the case where the labour market is imperfect and some individuals are rationed out of formal employment, or out of employment all together. In effect, they combine a CGE model, where wages are assumed to be rigid in the formal sector of the economy, with a MSM that includes behavioural features. However, the behaviour modelled is more the way rationing does occur on the labour market than the way individual agents freely decide about the sector they want to work in, on the basis of observed remuneration rates on these markets. The main macro–micro link is thus the extent of rationing in the labour market, and the main use of the MSM is to select households or individuals who will actually be barred from, or let in, the formal sector. In the application considered in that paper, it turns out that the selectivity of labour market rationing is the channel through which economy-wide policies have the most distributional impact. 26

## 5.3. FULLY INTEGRATED MICRO–MACRO MODELS

The second weakness of the top–down micro–macro approach is of course the absence of feedback from the micro to the macro level. Several attempts have now been made to fully integrate a behavioural MSM into an economy-wide modelling framework. For instance, Gortz and others [53] studied the effect of changing opening hours of retail trade in Denmark based on an estimated micro model of time allocation behaviour covering 2,000 households. Rutherford and others [92] analysed the effect of Russia’s accession to the WTO based on a model that included the consumption and labour supply behaviour of 50,000 households. Cogneau and Robilliard [33] also built an integrated model where some 3,000 Malagasy households have to allocate their labour to different uses and sectors along the lines of the well-known model by Heckman and Sedlacek [64] and make consumption choices across different goods and markets. In a dynamic setting, Heckman and others [63], Townsend [103] and others also fully integrated a representation of the labour supply, training and saving behaviour of a heterogeneous population, as observed in household surveys, and macro equilibrium mechanisms in the economy. 27 96

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

Because the burden of computation is extremely high, we would expect that the greater availability of powerful machines will enhance the implementation of such integrated micro–macro approaches. At the same time, the implementation of these methods raises difficult questions about the way micro behaviour is modelled and, in particular, the way in which individual heterogeneity is entered in the analysis. For instance, it makes a big difference whether heterogeneity in preferences is introduced as an additive term in conventional consumption or labour supply functions, or as idiosyncratic price, wage or income elasticities. For the first case, experience seems to show that there is little difference between the top-down and the fully integrated approach–see Hertel and Reimer [65]. For the second case, this is not true anymore, as discussed in Browning and others [26].

## 5.4. INTRODUCING DYNAMICS

Much of the possible links between micro and macro phenomena refers to a static framework, which may often seem inappropriate. Transferring income among agents at a given point of time is not the only function of redistribution systems, which are also responsible for transferring income from a period to another or from a given state of the world to another for a given person. This is the function of pension, unemployment and health insurance schemes. Likewise, economy-wide policies with some distributional impact may affect people in a way that depends on where they stand in their life cycle. The microsimulation of these policies thus requires a dynamic or life-cycle perspective.

One might think that the basic typology of static MSMs, and particularly the arithmetic-behavioural and the partial-general equilibrium distinctions, would apply to dynamic MSMs. This is not totally true, however. For instance, a dynamic arithmetical MSM should logically rely on the observation of sequential data about such individual characteristics as income, employment status and household composition. In other words, it should rely on some kind of panel data. Even though such data are more available in developed countries, they are dated and thus may not be of much relevance for simulating the forward-looking effects of a change in policy. Nor are they long enough to permit simulating lifecycle effects.

Instead of relying on actual panel data, dynamic arithmetical MSMs generally rely on synthetic panel data that simulate individual trajectories in the economic and social space. 28 They are generally obtained by applying to a cross-section of individuals and households observed at a point of time in a household survey the transition probabilities from a set of individual characteristics to another. These probabilities thus generate individual demographic and economic characteristics in the next period. And this procedure is repeated sequentially until reaching the time horizon selected for the analysis, or possibly until the individual is simulated as exiting the sample of observations, as for death or retirement.

Transition probabilities themselves are obtained from different sources. They are

## MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES

97 assumed to be constant, so that the society is supposed to be in some kind of steady state, and they are supposed to be independent of the policy analysed. In a dynamic setting, arithmetical MSMs necessarily incorporate some kind of modelling to generate synthetic panel data for applying changes in redistribution policies. 29 If the socio-economic state of an individual can be described by a vector of characteristics X t, the idea is to update this vector to the period t + 1 according to some exogenous stochastic processes obtained from the appropriate data. 30 For instance, a person may become unemployed with a probability P t that depends on his or her characteristics X t. He or she may die, get sick, marry or divorce, have children, receive some inheritance, move from a wage bracket to another and so on. The probabilities of these various events taking place between time t and t + 1 may be given jointly, or they may be assumed independent of each other. Once such a synthetic panel data set has been put together, it is a simple matter to simulate the effect of changing some particular features of tax-benefit systems, like unemployment insurance, child benefits or the way the pension system works. Such models are now being used in a number of countries (DEMOGEN in Canada, SFB3 in Germany, Dynastie in France and so on). One precaution not always taken when using these synthetic data is that they result from a random drawing procedure, which means that the result of any microsimulation is itself a random variable. For this reason, it is important when analysing the results of a microsimulation to perform robustness analysis using Monte-Carlo or bootstrapping methods (see [25]). 31 In a dynamic behavioural MSM, the transition probabilities P t should partly become endogenous and reactive to the intertemporal budget constraint facing agents. Depending on the behaviour of interest and the parameters of interest in the tax-benefit system, the analyst should thus model the decision-making process on labour supply, consumption, savings, marriage, fertility and the like, in function of the budget and other constraints facing the agent, and his or her expectations about future prices, wages and truly exogenous transition probabilities. 32 This type of model is still relatively scarce in the literature, very much because of the complexity and the difficulty of dealing dynamically with uncertainty, expectation formation and market imperfections. Available models tend to concentrate on some specific behaviour, abstracting from other important components of the demo-economic life cycle. For instance, Townsend [103], Townsend and Ueda [104] and Giné and Townsend [52] concentrate on saving/ investment behaviour under uncertainty and in different financial market environments. Heckman and others [63] focus on schooling and training behaviour. Although important in their own right, such models are specialized and do not permit analysing tax-benefit systems in all their dimensions. Extending these models to a general equilibrium setting requires assumptions about the way expectations are formed. Perfect foresight is generally assumed, 98

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

but equilibrium resolution may be difficult. The models already cited are among the few examples of integrated dynamic micro–macro models available at this stage. Yet, it seems likely that dynamic MSMs will become more numerous in the future. This is because they are the only tools that allow for the satisfactory analysis of many policy issues (demand for tertiary education, savings behaviour and role of the financial sector, pensions and population aging, health, etc.) on the agenda of any government.

6. Conclusion This brief survey has shown that microsimulation techniques have become relevant practically for the whole of applied economic policy analysis. The greater availability of large and detailed micro-datasets and the foreseeable increase in computing power are drastically modifying our approach to the evaluation of policy reforms. Instead of reasoning through representative agents and aggregate models of the economy, we now try more and more to take into account the fundamental heterogeneity of agents. By dispensing with the very demanding assumption necessary for perfect aggregation of individual behaviours, such an approach greatly improves the macro analysis of reforms. At the same time, it permits evaluating their full distributional impact. This can be done in several instances, under the assumption of no behavioural response. Simple microsimulation tools are straightforwardly developed on that basis and should be used more systematically. Extending the analysis to cover behavioural responses and the potential general equilibrium and macro-economic effects of reforms requires investing more in micro-economic and macro-economic modelling. Attempts in that direction, briefly described in this survey, show the difficulty of the approach but also the benefits that policy-making could draw from this kind of instrument.

Acknowledgements The authors acknowledge Rolf Aaberge, François Laysney and an anonymous referee for helpful comments. Amedeo Spadaro acknowledges financial support of Spanish Government–MCYT, (SEC2002-02606) and Fundación BBVA.

Notes 1 By ex ante evaluation we mean quantitative techniques – that can be both micro and macro–to Fpredict_ the likely impact of a change in policy (tax, subsidy, trade policy reform, exchange rate regime) prior to their implementation. But it is also crucial to evaluate ex post the actual impact of policies and, ideally, to measure the difference with ex ante predictions, and on that basis to explore ways to improve their performances. 2 See Orcutt [86], Orcutt and others [87] and Orcutt and others [88].

MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES 3

99 For a detailed description of the Fhistory_ and developments of microsimulation in economic analysis, see Atkinson and Sutherland [10], Merz [81], Citro and Hanusheck [32], Harding [58] and Gupta and Kapur [55]. 4 See the list established by Sahn and Younger [93] for applications of this approach to the incidence of indirect taxation. 5 About the take-up problem see Hancock and others [56]. 6 See Duclos [43 – 45] and Duclos and others [46]. 7 See also the papers presented at the conference: BInternational Microsimulation Conference on Population, Ageing and Health: Modelling Our Future^ held in Canberra, Australia, in December 2003. The papers can be downloaded from: www.natsem.canberra.edu.au. 8 The preceding studies all rely on Euromod, an ambitious microsimulation model that covers the 15 EU members For a detailed description and other applications of this model, see Sutherland [100] and the website: www.econ.cam.ac.uk/dae/mu/emod.htm. 9 For a complete survey on welfare dominance theory, see Lambert [76]. 10 See Bourguignon and others [19]. 11 The most basic methodological reference for this approach is the pioneering work by

Hausman [59–61].

12 Assuming indeed a structural specification of the NT() function general enough for all reforms to be represented by a change in parameters. 13 For an extensive discussion of these specifications, see Bargain [13]. 14 On the contrary, in ex post approaches to the evaluation of policy reforms counterfactuals are obtained by observing the difference between individuals who are confronted to, or concerned with, the reform and individuals who are not. 15 Of course, it is also necessary to check that utility is monotonically increasing with disposable income for this general specification to make any sense. 16 Those programmes may also be evaluated ex post through impact evaluation techniques.

Progresa, the ancestor of Oportunidades, has been the object of very careful evaluation. For detailed information, see the website of the International Food Policy Research Institute: www.ifpri.org/themes/progresa.htm. 17 A similar exercise has been made to evaluate ex ante the Progresa programme in Mexico by Todd and Wolpin [102] and by Attanasio and others [12]. In both cases, the modelling framework includes dynamic features and is more sophisticated. Earlier attempts at microsimulating the effects of educational policies on schooling include Gertler and Glewwe [51] – see also Younger [108]. Overall, however, it is somewhat remarkable that little ex ante analysis of such programmes is performed in developing countries. 18 Rather satisfactory results have been obtained in that direction by Todd and Wolpin [102] and Attanasio and others [12]. 19 An inconvenience is that the equivalent income function is not guaranteed to be concave, which means that, if the function () is not concave enough, the SWF could favour inequality increasing transfers. Blackorby and Donaldson [15] show that this will not be the case if the individual utility function is quasi-homothetic. 20 See, for example, Aaberge and others [1, 3–5]. 21 See, for instance, Bourguignon and Spadaro [23]. A proportional income tax is being used as the closest approximation to a Fneutral_ tax that would take care of the budget constraint without major distortions of the economy. Practically, however, a proportional tax on income or consumption has an effect on labour supply. Iterating with the whole MSM is thus necessary to determine the level of the tax rate that will satisfy the budget constraint.

100

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

22 See also Slemrod and others [96] for an extension to a two tier linear income taxation model.

See also Judd and others [68] for a computational approach to dynamic optimal taxation. 23 See Shoven and Walley [95]. 24 It is true that, by emphasizing changes in relative prices and in the sectoral structure of the economy, this approach is more adapted to developing than developed countries. Yet, there also are applications to developed countries-see for instance Meagher [80] for Australia. See also the survey on poverty and trade by Hertel and Reimer [65]. 25 A interesting application of an integrated micro-macro analysis is Labandeira and others [74]. 26 See also Bussolo and Lay [27]. 27 Top-down and fully integrated micro–macro models are not really exclusive. In particular, one may think of resolving fully integrated models in an iterative way going from the macro equilibrium of markets to micro behaviour and then back to the economy-wide model after aggregating total consumption or labour supply at the micro model. See Savard [94] and Aaberge and others [6]. 28 An alternative could be the use of panel data to inform the estimation of behavioral effects with explicit time dimension. See Duncan and Weeks [48]. 29 On dynamic microsimulation of household behaviour, see Harding [57], O’Donoghue [84] and Zaidi and Rake [109]. See also Dupont and others [49] for a survey on dynamic MSMs applied to pensions system analysis. 30 Caldwell [28], page 5. 31 Sensitivity and Robustness analysis are important also when performing arithmetical microsimulation analysis. See Pudney and Sutherland [89] and Creedy and others [36]. 32 Browning and others [26] and Blundell and MaCurdy [17] contain an excellent discussion about these problems. See also Klevmarken [72].

## References

1.

2.

3.

4.

5.

6.

7. Aaberge, R., Colombino, U. and Strøm, S.: Social Evaluation of Individual Welfare Effecys from Income Taxation, Discussion Paper 230 Statistics Norway, Oslo, Norway, 1998. Aaberge, R., Colombino, U. and Strøm, S.: Evaluating alternative tax reforms in Italy with a model of joint labour supply of married couples, Structural Change and Economic Dynamics 9 (1998) 415–433. Aaberge, R., Colombino, U. and Strøm, S.: Labour supply in Italy: An empirical analysis of joint household decisions, with taxes and quantity constraints, Journal of Applied Econometrics 14(4) (1999) 403–422. Aaberge, R., Colombino, U. and Strøm, S.: Labour supply responses and welfare effects from replacing current tax rules by a flat tax: Empirical evidence from Italy, Norway and Sweden, Journal of Population Economics 13(4) (2000) 595–621. Aaberge, R., Colombino, U. and Strøm, S.: Do More Equal Slices Shrink the Cake? An Empirical Evaluation of Tax-Transfer Reform Proposals in Italy, WP CHILD #19/2001. 37/ 2003, University of Oslo, Department of Economics, Oslo, Norway, 2001. Aaberge, R., Colombino, U., Holmøy, E., Strøm, B. and Wennemo, T.: Population Aging and Fiscal Sustainability: An Integrated Micro–macro Analysis of Required Tax Changes, Discussion Paper 366, Statistics Norway, Oslo, Norway, 2004. Ahmad, E. and Stern, N.: The theory of reform and Indian direct taxes, Journal of Public Economics 25 (1984) 259–298.

MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES 8.

9.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

20.

21.

22.

23.

24.

101 Atkinson, A., Bourguignon, F. and Chiappori, P.A.: What do we learn about tax reforms from international comparisons? France and Britain, European Economic Review 32(2–3) (1988) 343–352. Atkinson, A., Bourguignon, F., O’Donoghue, C., Sutherland, H. and Utili, F.: Microsimulation of social policy in the European Union: Case study of a European minimum pension, Economica 69(274) (2002) 229–243. Atkinson, A. and Sutherland, H. (eds.), Tax Benefit Models. STICERD Occasional Paper 10, LSE. Suntory and Toyota International Centres for Economics and Related Disciplines, London, 1988. Atkinson, A. and Stiglitz, J.: Lectures on Public Economics, McGraw-Hill, New York, 1980. Attanasio, O., Meghir, C. and Székely, M.: Using Randomized Experiments and Structural Models for FScaling Up_: Evidence from the PROGRESA Evaluation, World Bank. Paper presented at the Annual World Bank Conference on Development Economics, May 21–23, Bangalore, India, 2003. Bargain, O.: On Modelling Household Labor Supply with Taxation, Département et Laboratoire d’Economie Théorique et Appliquée (DELTA), Paris, 2004. Bargain, O.: Aide au retour à l’emploi et à l’activité des femmes en couple, Revue de l’OFCE 88 (2004) 59–87. Blackorby, C. and Donaldson, D.: Money metric utility: A harmless normalisation? Journal of Economic Theory 46 (1988) 120–129. Blundell, R., Duncan, A., McCrae, J. and Meghir, C.: The labour market impact of the working families’ tax credit, Fiscal Studies 21(1) (2000) 75–104. Blundell, R. and MaCurdy, T.: Labour Supply: A Review of Alternative Approaches, In: O. Ashenfelter and D. Card (eds.), Handbook of Labour Economics, Vol. 3a, North-Holland, Amsterdam, 1999. Bonin, H., Kempe, W. and Schneider, H.: Household Labour Supply Effects of Low-wages Subsidies in Germany, IZA Discussion Paper 637, Institute for the Study of Labor, Bonn, Germany, 2002. Bourguignon, F., Chiappori, P.A. and Hugounenq, R.: Exploring the Distribution and Incentive Effects of Tax Harmonization, In: A. Heimler and D. Meulders, (eds.), Empirical Approaches to Fiscal Policy Modelling, Chapman and Hall, London, 1993. Bourguignon, F., Ferreira, F. and Leite, P.: Conditional cash transfers, schooling and child labour: Micro-simulating bolsa escola, World Bank Economic Review 17(2) (2003) 229–254. Bourguignon, F., O’Donoghue, C., Sastre, J., Spadaro, A. and Utili, F.: Eur3: A prototype European tax-benefits model, In: A. Gupta and V. Kapur (eds.), Microsimulation in Government Policy and Forecasting, North-Holland, Amsterdam, 2000. Bourguignon, F., Robillard, A.S. and Robinson, S.: Representative versus real households in the macroeconomic modelling of inequality, In: T.J. Kehoe, T.N. Srinivasan and J. Whalley (eds.), Frontiers in Applied General Equilibrium Modelling, Cambridge University Press, Cambridge, 2004. Bourguignon, F. and Spadaro, A.: Social Preferences Revealed through Effective Marginal Tax Rates, DELTA Working Paper 2000-29, Département et Laboratoire d’Economie Théorique et Appliquée (DELTA), Paris, 2000. Bourguignon, F. and Spadaro, A.: Tax-Benefit Revealed Social Preferences: Are Tax Authorities Non-Paretian? Département et Laboratoire d’Economie Théorique et Appliquée (DELTA), Paris, 2005.

102

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

25.

Bradley, E. and Tibshirani, J.: An Introduction to the Bootstrap, Chapman and Hall, New York, 1993. Browning, M., Hansen, L.P. and Heckman, J.: Micro data and general equilibrium models, In: Taylor and Woodford (eds.), Handbook of Macroeconomics, Vol. 1, North-Holland, Amsterdam, 1999. Bussolo, M. and Lay, J.: Globalisation and Poverty Changes: A Case Study on Colombia, Working Paper 226, OECD Development Centre, Paris, 2003. Caldwell, S.B.: Static, Dynamic and Mixed Microsimulation, Department of Sociology, Cornell University, Ithaca, NY, 1990. Callan, T. and Sutherland, H.: The impact of comparable policies in European countries: Microsimulation approaches, European Economic Review 41(3–5) (1997) 327–333. Chen, S. and Ravallion, M.: Households Welfare Impacts of China’s accession to the World Trade Organization, Working Paper 3040, World Bank, Washington, D.C. 2003. Christiansen, V. and Jansen, E.: Implicit social preferences in the Norwegian system of indirect taxation, Journal of Public Economics 10 (1978) 217–245. Citro, C. and Hanushek, E.: Improving Information for Social Policy Decision – The Uses of Microsimulation Modelling, National Academy, Washington, D.C., 1991. Cogneau, D. and Robilliard, A.S.: Croissance, distribution et pauvreté: un modèle de micro simulation en équilibre général appliqué à Madagascar, Working Paper DT2001/19, Développement, Institutions and Analyses de Long terme, Paris, 2001. Creedy, J.: Modelling Indirect Taxes and Tax Reform, Edward Elgar, Northampton, Mass, 1999. Creedy, J. and Duncan, A.: Behavioural microsimulation with labour supply responses, Journal of Economic Surveys 16(1) (2002) 1–38. Creedy, J., Kalb, G. and Kew, H.: Confidence Intervals for Policy Reforms in Behavioural Tax Microsimulation Modelling, Research Paper 936, Department of Economics, University of Melbourne, Australia, 2005. Das, M. and van Soest, A.: Family Labour Supply and Proposed Tax Reforms in The Netherlands, De Economist 149 (2001) 191–218. De Lathouwer, L.: A Case Study of Unemployment Scheme for Belgium and The Netherlands, In: Harding (ed.), Microsimulation and Public Policy, North-Holland, Amsterdam, 1996. Decoster, A. and Van Camp, G.: Redistributive effects of the shift from personal income taxes to indirect taxes: Belgium 1988–93, Fiscal Studies 22(1) (2001) 79–106. Demery, L.: Analysing the Incidence of Public Spending, In: F. Bourguignon and L.A. Pereira da Silva (eds.), The Impact of Economic Policies on Poverty and Income Distribution: Evaluation Techniques and Tools, Oxford University Press, Oxford, 2003. Diamond, P. and Mirrlees, J.: Optimal taxation and public production: I – Production efficiency, American Economic Review 61(1) (1971) 8–27. Diamond, P. and Mirrlees, J.: Optimal taxation and public production: II – Production efficiency, American Economic Review 61(3) (1971) 261–278. Duclos, J.-Y.: Modelling the take-up of state support, Journal of Public Economics 58(3) (1995) 391–415. Duclos, J.-Y.: On equity aspects of imperfect poverty relief, Review of Income and Wealth 41(2) (1995) 177–190. Duclos, J.-Y.: Estimating and testing a model of welfare participation: The case of supplementary benefits in Britain, Economica 64(253) (1997) 81–100. Duclos, J.-Y., Makdissi, P. and Wodon, Q.: Poverty-Dominant Program Reforms: the Role of Targeting and Allocation Rules, Journal of Development Economics 77(1) (2005) 53–57.

26.

27.

28.

29.

30.

31.

32.

33.

34.

35.

36.

37.

38.

39.

40.

41.

42.

43.

44.

45.

46.

MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES 47.

103 Duflo, E.: Scaling Up and Evaluation, Paper Presented at the Annual World Bank Conference on Development Economics, May 21–23, Bangalore, India, 2003.

48. Duncan, A. and Weeks, M.: Transitions estimators in discrete labour supply models, In: L.

Mitton, H. Sutherland and M. Weeks (eds.), Microsimulation Modelling for Policy Analysis: Challenges and Innovations, Cambridge University Press, Cambridge, 2000.

49. Dupont, G., Hagneré, C. and Touzé, V.: Les modèles de microsimulation dynamique dans l’analyse des réformes des systèmes de retraites: une tentative de bilan, Economie et Prévision 160–161(4–5) (2004) 167–192.

50. Gago, A., Labandeira, X. and Rodriguez, M.: International Empirical Evidence on Green Tax Reforms, Universidad de Vigo, Department of Applied Economics, 2004.

51. Gertler, P. and Glewwe, P.: The willingness to pay for education in developing countries:

Evidence from rural Peru, Journal of Public Economics 42(3) (1990) 251–275.

52. Giné, X. and Townsend, R.: Evaluation of Financial Liberalization: A General Equilibrium Model with Constrained Occupation Choice, University of Chicago, Department of Economics, Chicago, Ill. www.src.uchicago.edu/users/robt/workingpapers/gtwp.pdf, 2004.

53. Gortz, M., Konnerup, M. and Kastberg-Nielsen, C.: Butikkernes *bningstider: Hvad betyder de for forbrugerne? (Shops Opening Hours: Consequences for Consumers), In: S.E. Hougaard Jensen (ed.), Økonomi og erhvervspolitik (Economics and Business Politics), Handelshøjskolens Forlag, Copenhagen, Denmark, 2000.

54. Grubb, M., Edmonds, J., ten Brink, P. and Morrison, M.: The costs of limiting fossil-fuel CO2 emissions, Annual Review of Energy and Environment 18 (1993) 397–478.

55. Gupta, A. and Kapur, V.: Microsimulation in Government Policy and Forecasting, North-

Holland, Amsterdam, 2000.

56. Hancock, R., Pudney, S. and Sutherland, H.: Using Econometric Models of Benefit Take-up by British Pensioners in Microsimulation Models, Paper presented at the International Microsimulation Conference on Population, Ageing and Health: Modelling Our Future, December 7–12, Canberra, Australia, 2003.

57. Harding, A.: Lifetime Income Distribution and Redistribution: Applications of a Microsimulation Model, North-Holland, Amsterdam, 1993.

58. Harding, A.: Microsimulation and Public Policy, North-Holland, Amsterdam, 1996. 59. Hausman, J.: The effect of wages, taxes and fixed costs on women’s labour force participation, Journal of Public Economics 14 (1980) 161–194.

60. Hausman, J.: Labour supply, In: H. Aaron and J. Pechman (eds.), How Taxes Affect

Economic Behavior, Washington, D.C.: Brookings Institution, 1981.

61. Hausman, J.: The econometrics of nonlinear budget set, Econometrica 53 (1985) 1255– 1282.

62. Hausman, J. and Ruud, P.: Family labour supply with taxes, American Economic Review 74 (1994) 242–248.

63. Heckman, J., Lochner, L. and Taber, C.: Explaining rising wage inequality: Explorations with a dynamic general equilibrium model of labor earnings with heterogeneous agents, Review of Economics Dynamics 1 (1998) 1–58.

64. Heckman, J. and Sedlacek, G.: Self-selection and the distribution of hourly wages, Journal of Labor Economics 8(1) (1990) 329–363.

65. Hertel, T. and Reimer, J.: Predicting the Poverty Impacts of Trade Reform, World Bank Policy Research Working Paper 3444, Washington, D.C., 2004.

66. Hoerner, A. and Bosquet, B.: Environmental Tax Reform: The European Experience, Center for a Sustainable Economy, Washington, D.C., 2001.

67. Hoynes, H.: Welfare transfers in two parent families: Labour supply and welfare participation under AFDC-UP, Econometrica 64 (1996) 295–332.

104 68.

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

Judd, K., Kubler, F. and Schmedders, K.: Computational methods for dynamic equilibria with heterogeneous agents, In: M. Dewatripont, L.P. Hansen and S. Turnovsky (eds.), Advances in Economics and Econometrics, Cambridge University Press, Cambridge, 2000.

69. Kaplanoglou, G. and Newbery, D.M.: Indirect taxation in Greece: Evaluation and possible reform, International Tax and Public Finance 10 (2003) 511–533.

70. Keane, M. and Moffit, R.: A structural model of multiple welfare program participation and labour supply, International Economic Review 39 (1998) 553–589.

71. King, M.A.: Welfare analysis of tax reforms using households data, Journal of Public

Economics 21 (1983) 183–214.

72. Klevmarken, N.A.: Modelling Behavioural Response in EUROMOD, Microsimulation Unit Working Paper MU9702, Institute for Social and Economic Research, University of Essex,

## UK, 1997.

73. Kurz, M.: On the inverse optimal problem, In: H.W. Kuhn and G.P. Szego, (eds.), Mathematical Systems Theory and Economics, Springer, Berlin Heidelberg New York, 1968.

74. Labandeira, X., Labeaga, J.M. and Rodriguez, M.: A macro and microeconomic integrated approach to assess the effects of public policies, Universidad de Vigo, Department of Applied Economics, 2004.

75. Labeaga, J.M., Oliver, X. and Spadaro, A.: Discrete Choice Models of Labour Supply, Behavioural Microsimulation and the Spanish Tax Reforms, FEDEA Working Paper, www.fedea.es, 2005.

76. Lambert, P.: The Distribution and Redistribution of Income: A Mathematical Analysis,

Manchester University Press, Manchester, UK, 1993.

77. Liberati, P.: The distributional effects of indirect tax changes in Italy, International Tax and

Public Finance 8(1) (2001) 27–51.

78. MaCurdy, T.E., Green, D. and Paarsch, H.: Assessing empirical approaches for analysing taxes and labour supply, Journal of Human Resources 25(3) (1990) 415–490.

79. Madden, D.: An analysis of indirect tax reform in Ireland in the 1980s, Fiscal Studies 16 (1995) 18–37.

80. Meagher, G.A.: Forecasting Changes in Income Distribution: An Applied General Equilibrium Approach, Centre of Policy Studies and the IMPACT Project Working Paper OP-78, Monash University, Victoria, Australia, 1993.

81. Merz, J.: Microsimulation – A survey of principles, developments and applications,

International Journal of Forecasting 7 (1991) 77–104.

82. Mirrlees, J.A.: An exploration in the theory of optimum income taxation, Review of

Economic Studies 38(114) (1971) 175–208.

83. Newbery, D.M.G.: The distributional impact of price changes in Hungary and in the United

Kingdom, Economic Journal 105 (1995) 847–863.

84. O’Donoghue, C.: Dynamic microsimulation: A methodological survey, Brazilian Electronic

Economic Journal 4(2) (1999).

85. Oliver, X. and Spadaro, A.: Are Spanish Governments Really Averse to Inequality? An Empirically-Based Normative Analysis of the 1998 and 1999 Spanish Tax-Benefit Systems, Investigaciones Economicas 28(3) (2004)551–66.

86. Orcutt, G.: A new type of socio-economic system, Review of Economic and Statistics 58 (1957) 773–797.

87. Orcutt, G, Greenberger, M., Korbel, J. and Rivlin, A.: Microanalysis of Socio-Economic Systems: A Simulation Study, Harper and Row, New York, 1961.

88. Orcutt, G., Merz, J. and Quinke, H.: Microanalytic Simulation Models to Support Social and

Financial Policy, North-Holland, Amsterdam, 1986.

MICROSIMULATION AS A TOOL FOR EVALUATING REDISTRIBUTION POLICIES 89.

90.

91.

92.

93.

94.

95.

96.

97.

98.

99.

100.

101.

102.

103.

104.

105.

106.

105 Pudney, S. and Sutherland, H.: How reliable are microsimulation results? An analysis of the role of sampling error in a UK tax-benefit model, Journal of Public Economics 53(3) (1994) 327–365. Ramsey, F.: A contribution to the theory of taxation, Economic Journal 37 (1927) 47–61. Redmond, G., Sutherland, H. and Wilson, M.: The Arithmetic of Tax and Social Security Reform: A User’s Guide to Microsimulation Methods and Analysis, Cambridge University Press, Cambridge, 1998. Rutherford, T., Shepotylo, O. and Tarr, D.: Household and Poverty Effects from Russia’s Accession to the WTO, World Bank, Presented at the 7th Annual Conference on Global Economic Analysis, June 17–19, Washington, D.C. www.worldbank.org/trade/russia-wto, 2004. Sahn, D. and Younger, S.: Estimating the incidence of indirect taxes in developing countries, In: F. Bourguignon and Pereira da Silva L.A. (eds.), The Impact of Economic Policies on Poverty and Income Distribution: Evaluation Techniques and Tools, Oxford University Press, Oxford, 2003. Savard, L.: Poverty and Income Distribution in a CGE-Household Microsimulation Model: Top-Down/Bottom-Up Approach, CIRPÉE Working Paper 03-43. Centre interuniversitaire sur le risque, les politiques économiques et l’emploi, Quebec, 2003. Shoven, J.B. and Whalley, J.: Applied general equilibrium models of taxation and international trade: An introduction and survey, Journal of Economic Literature 22(3) (1984) 1007–1051. Slemrod, J., Yitzhaki, S. and Mayshar, J.: The optimal two-bracket linear income tax, Journal of Public Economics 53(2) (1994) 269–290. Spadaro, A.: Microsimulation and normative policy evaluation: An application to some EU tax-benefits system, Journal of Public Economic Theory 7(4) 2005. Stern, N.: On the Specification of Models of Optimum Income Taxation, Journal of Public Economics 6 (1976) 123–162. Sutherland, H.: Les modèles statiques de microsimulation en Europe dans les années 90, Economie et Statistique 315 (1998) 35–50. Sutherland, H.: Final Report EUROMOD: An Integrated European Benefit-Tax Model, EUROMOD Working Paper EM9/01, University of Cambridge, Department of Applied Economics, Cambridge, 2001. Symons, E. and Warren, N.: Modelling consumer behaviour response to commodity tax reforms in microsimulation models, In: A. Harding (ed.), Microsimulation and Public Policy, North-Holland, Amsterdam, 1996. Todd, P. and Wolpin, K.: Using Experimental Data to Validate a Dynamic Behavioral Model of Child Schooling and Fertility: Assessing the Impact of a School Subsidy Program in Mexico, University of Pennsylvania, Population Studies Center, Philadelphia, 2002. Townsend, R.: Safety Nets and Financial Institutions in the Asian Crisis: the Allocation of Within-Country Risk, International Monetary Fund. Prepared for the IMF Conference on Macroeconomic Policies and Poverty Reduction, March 14–15, Washington, D.C. http:// cier.uchicago.edu/papers/papers.htm, 2002. Townsend, R. and Ueda, K.: Financial Deepening, Inequality, and Growth: A Model-Based Quantitative Evaluation, IMF Working Paper 03-193, International Monetary Fund, Washington, D.C. www.imf.org/external/pubs/ft/wp/2003/wp03193.pdf, 2003. Tsakloglou, P. and Mitrakos, T.: On the distributional impact of excise duties: Evidence from Greece, Public Finance/Finances Publiques 53 (1998) 78–101. Tuomala, M.: Optimal Income Tax and Redistribution, Oxford University Press, Oxford, 1990.

106

## FRANÇOIS BOURGUIGNON AND AMEDEO SPADARO

107.

van Soest, A.: A structural model of family labour supply: A discrete choice approach, Journal of Human Resources 30 (1995) 63–88. Younger, S.: Benefits on the margin: Observation on the average vs. marginal benefit incidence, World Bank Economic Review 17(1) (2003) 89–106. Zaidi, A. and Rake, K.: Dynamic microsimulation models: A review and some lessons for SAGE, SAGE Discussion Paper 2, ESRC SAGE Research Group, London School of Economics, London, 2001.

108.

109.
