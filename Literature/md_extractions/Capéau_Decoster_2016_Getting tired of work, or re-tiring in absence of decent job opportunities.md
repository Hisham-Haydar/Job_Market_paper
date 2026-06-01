# Bart Capéau a André Decoster a a

Department of Economics, KU Leuven

## Abstract

This paper exploits the distinction between preference and opportunity factors in a Random Utility and Random Opportunity (RURO) model of job choice (Aaberge, Dagsvik and Strøm, 1995, and Aaberge, Colombino and Strøm, 1999). We estimate the model on Belgian data (SILC 2007). To investigate to what extent lower labour market participation of elderly is due to changing preferences (executing a job might become less enjoyable with age) or to differences in opportunities (elderly getting less, or less attractive job offers), we use the estimated model to simulate two counterfactuals.

In the first, we remove partly the age heterogeneity in opportunities, in the second we remove age heterogeneity in preferences. A comparison of labour market behaviour in these two counterfactuals with the baseline shows that opportunities which decline with age are at least as an important factor in explaining low participation rates for the elderly, as is increasing preference for leisure. The effect of opportunities seems to work primarily through the extensive margin, whereas the effect of preferences is more outspoken in the intensive than in the extensive margin.

## JEL: J22; C25; H31

Keywords: discrete choice, labour supply, random utility model, opportunities

Corresponding author:

André Decoster

Email: andre.decoster@kuleuven.be

1 This paper subsumes the October 2015 version which appeared as CES DPS15.25. We are grateful to Rolf Aaberge and Ugo Colombino for an introduction into and many discussions on the RURO–model, to Tom Wennemo for technical assistance with the estimation program and to Bart Cockx, John Dagsvik, Gijs Dekkers, Erik Schokkaert, and seminar participants at the Department of Economics of Ghent University, CES KULeuven and core Louvain–la–Neuve for comments on earlier versions of the paper. The usual disclaimer applies. Pieter Vanleenhove, Toon Vanheukelom and Rembert De Blander prepared the data from EU-SILC 2007, and used EUROMOD version F5.5 to calculate net incomes for the choice sets. We acknowledge financial support from the BELSPO–projects MIMBEL and BEL–AGEING. The results presented here are based on EUROMOD version F5.5. EUROMOD is maintained, developed and managed by the Institute for Social and Economic Research (ISER) at the University of Essex, in collaboration with national teams from the EU member states. We are indebted to the many people who have contributed to the development of EUROMOD. The process of extending and updating EUROMOD is financially supported by the European Union Programme for Employment and Social Innovation ‘Easi’ (2014-2020). The results and their interpretation are the authors’ responsibility.

1

## Introduction

In the present paper we investigate the impact of ageing on job choice behaviour, using a structural discrete choice model. Existing literature has concentrated on the early exit of elderly from the labour market. Emphasis has been put on the role of financial incentives in the social security system to leave or remain active in the labour market. See for example Gruber and Wise (1999) for an overview of these issues in different oecd countries. To that purpose, the net social security wealth, that is the present value of future benefits minus the present value of social security contributions, and the accrual of that wealth by postponing retirement or exit from the labour market through other channels such as special early leaver schemes, were used as indicators. 1 Later on, the financial implications of such social security schemes were included in a utility based decision model (Stock and Wise 1990). 2 The Stock and Wise approach boils down to the question whether continuing to work one year longer would yield a higher expected utility than retiring now. This departs from a fully forward looking dynamic framework of maximizing expected utility, in which at each point in time an optimal decision is taken, for each possible value of future possible states of the world, and expectations are taken over the possible evolution of the state of the world through time. While such fully forward looking models were developed to study the retirement decision (Rust 1989, Berkovec and Stern 1991, Rust and Phelan 1997), they have been criticised for their computational complexity in exchange for a poor gain in predictive validity (Lumsdaine et al. 1992, Belloni 2008). 3 Our point of departure is different from these studies. We do not model the exit decision. On the contrary, we exclude early leavers from our study, as well as other persons not available for the labour market (students and disabled persons). We concentrate on the labour market participation decisions of those who are still available for the labour market. This group thus comprises those who are working (as an employee), and voluntary and involuntary unemployed. To set the scene, we summarise in the next table the labour market participation figures and mean labour time of the subjects in the sample that we will use in this paper, by age category (more specifically, 30–49 years compared to 50–64 years). 1 The use of social security wealth as an indicator for financial incentives of the social security system, can at least be traced back to Feldstein (1974). 2 See Maes (2011, 2012) and Lefebvre and Orsini (2012) for applications to Belgium. Maes uses the net social security wealth and its accrual as inputs in the decision model, while Lefebvre and Orsini use simulated paths of future wages and benefits. Applications to Italy were made by Belloni and Alessie (2009, 2013). 3 Another more macroeconomic oriented strand of the literature has investigated the impact of ageing on the financial sustainability of the pension system (e.g. Buyse et al., 2013). An interesting avenue for future research is the integration of richer labour supply models, such as the one used in this paper, into these macroeconomic general equilibrium models, as for example in Aaberge et al. (2007).

Our sample consists of single males and females, and males and females living together as a couple, who either execute a job as employee, be it full or part time, or are available on the labour market to execute such a job, if they would find a suitable offer. 4 The drop in labour market participation from those aged 30 to 49 years old to those aged 50 to 64 years old ranges between 12 (males in couples) and 31 percentage points (females in couples). The time per week a person spends on jobs is almost six to more than ten hours per week lower for the groups aged 50–64, as compared to the younger age group.

Age

Category

Males in couples

Females in couples

Single males

Single females labour market labour time participation (%) mean hours per week 30–49 50–64 30–49 50–64 96% 85% 85% 73% 84% 54% 62% 58% 39.6 27.0 33.7 26.6 33.8 16.5 24.6 19.7

Source: own calculations on the basis of eu–silc 2007 Belgium.

We will investigate whether this lower participation of elderly is a matter of preferences (increasing intensity of preference for leisure with age), or whether less jobs are available, suitable for the capacities of elderly. Thereto a model is required which, contrary to the classical discrete choice models of labour supply (such as the basic model of Van Soest 1995; the discrete choice approach has been reviewed by Creedy and Kalb 2005), will allow for the impact of both labour supply and labour demand side effects. More specifically, we used a Random Utility/Random Opportunity (ruro) model of job choice (see amongst others Dagsvik and Strøm 1992, 2003, and 2006, Dagsvik, Aaberge and Strøm 1995, and Aaberge, Colombino and Strøm 1999). 5 These type of models, first developed in an abstract setting by Dagsvik (1994), try to understand individual heterogeneity in choice behaviour as a combined effect of preference differences and differences in opportunities. The ruro model fits in a broader literature which attempts to insert restrictions on the choice 4 This excludes self–employed, early retired persons and persons receiving a sickness or invalidity benefit.

As such, the definition of participation rate we will use in this paper, that is the number of employed persons relative to those employed and those available for executing a job, differs from both the employment and activity rate in eurostat–statistics. The former is the number of persons working relative to total population or the relevant sub–population, while the latter refers to those working and looking for a job, compared to the total or relevant sub–population. 5 See also the recent overviews by Aaberge and Colombino (2014), and Dagsvik, Jia, Kornstad, and

Thoresen (2014).

set into a labour supply model (see, amongst others, Altonji and Paxson 1982, 1992, Van Soest, Woittiez and Kapteyn 1990, Tummers and Woittiez 1991, Dickens and Lundberg 1993, Bloemen 2000, 2008, Ham and Reilly 2002, Müller, Neumann and Wrohlich 2015, and Beffy et al. 2016). It must be added that the inclusion of dummies for part time and full time work in an extended version of the discrete choice model of Van Soest (1995), to improve the fit, is in fact a simplified reduced form approach of earlier work with Woittiez and Kapteyn (Van Soest, Woittiez and Kapteyn, 1990) which models hours restrictions more explicitly. But the ruro model is the first one that derives these restrictions from an explicit model of a job arrival process, and stresses the individual heterogeneity, both observed and unobserved, of the availability of job offers suitable to the capacities of individual agents. This makes this model specially apt to handle the research question we envisage. Preferences are capturing the extent to which an individual is willing to trade–off leisure for consumption. Other aspects such as social relations involved in the job, challenge of the tasks, security and health, recognition, and societal relevance, influence the choice between alternative leisure activities and available jobs. These factors are however not easily observable by the analyst. It was one of the contributions of the development of probabilistic choice and random utility models, as developed by respectively Luce (1959) and McFadden (1973), to integrate these additional determinants of preferences as a non–systematic element, affecting the utility obtained from different available alternatives. By non–systematic it is meant that such factors are not related to observable characteristics. Random utility models have been applied to labour supply behaviour (Van Soest, 1995) since. They replaced the traditional continuous choice approach to labour supply behaviour (see Hausman, 1985, for a review of the traditional approach), which faced difficulties in deriving tractable closed form solutions of labour supply functions, in the presence of non–linear budget sets. Indeed, many personal income tax systems, such as e.g. a minimum income guarantee associated with a linear earned income tax, create non–convexities in the budget set (the available bundles of consumption and labour time a person can choose from), leading to discontinuities and non– uniqueness of the optimal choice in function of wage variations. These phenomena are more easily treated in a discrete choice set–up, which is the approach taken by both, probabilistic choice and random utility models. The random utility model is however still limited in scope. Interindividual differences in the availability of alternatives from which a person can choose, are exogenous to the model. Applied to job choice, differences in individual budget sets stem exclusively from wage differences and differences in unearned income. In a static model, it is indeed reasonable to assume that unearned income differences are exogenous, and do not depend on individual choices. But in standard random utility models also wages are exogenously fixed individual characteristics, reflecting a person’s productive capacities. 6 For several reasons, this is unattractive. Productive capacities can in many cases not be determined appropriately, when considered separately from the specific job in which these capacities are exhibited. Moreover, it is quite unnatural that all available job offers, even when perfectly suited to a person’s capacities and skills, would pay the same wage. Furthermore, due to organisational limitations of the production process, and social life, it is highly unlikely that persons can completely freely fix the number of hours they will work. It is exactly these type of frictions in the choice process which are taken into consideration by ruro models, as an additional factor, next to preferences, to understand choice behaviour. Job offers are considered as packages of wages, labour time regimes, and a number of other attributes (Dagsvik and Strøm 1992, 2003, and 2006, Aaberge, Dagsvik and Strøm 1995, and Aaberge, Colombino and Strøm 1999). These other attributes (challenge, safety and security, esteem and recognition, appreciation of colleagues, responsibility...) are however difficult to observe, especially to the extent that these are important from the viewpoint of the degree of job satisfaction they can provide to a person. Therefore, the individual specific availability of suitable jobs is thought of as the result of a stochastic process of job offers. The impact of explanatory variables on the intensity with which job offers arrive to a person according to that process, is estimated jointly with individual’s preference characteristics. Not only the intensity with which job offers arrive, but also the availability of, according to a person’s own judgement, attractive non–market alternatives to spend time, is individually specific. Limited physical abilities might impede someone who likes to walk outside, to do so. Choosing under such circumstances between sitting in front of a liquid crystal screen, reading books, or accepting a job, that person might opt for the latter, while the reverse might happen for someone with similar preferences, but in good physical shape. The ruro–model also allows for individual heterogeneity in restrictions on available labour time regimes, even though the effect of these type of restrictions are difficult to identify from the contribution of preferences. The present paper exploits the distinction of the ruro model between preference factors and individual differences in opportunities, in order to obtain a more nuanced picture of labour market participation of the elderly. More specifically, by estimating a ruro model (applied to Belgium) we are able to give a quantitative answer to the question to what extent lower 6 Some contributions do allow for unobserved wage heterogeneity, see e.g.

Van Soest, Das and Gong (2002), Löffler et al. (2013), and the second model discussed in Dagsvik and Jia (2014). Van Soest (1995) already incorporated the problem of imperfect observation of wages for non–participants in the extended version of his model. Besides, there is an earlier literature accounting for the fact that wages are non–linear in hours (See for example Moffitt 1984). However, none of these treats wages as an object of job choice behaviour.

labour market participation is due to changing preferences (executing a job might become less enjoyable with age) or differences in opportunities (elderly getting less, or less attractive job offers). For the interested reader, Section 2 presents a self–contained in depth exposition of our account of the ruro model. Section 3 discusses the derivation of the likelihood function resulting from the model, and explains, also in detail, the estimation method. Some technical issues are relegated to an appendix. The data are presented in Section 4. Section 5 contains the estimation results. In Section 6 we investigate the fit of the estimated model, and its behavioural implications. Finally, Section 7 draws some tentative conclusions with respect to the contribution of preferences and opportunities, in the assessment of the age profiles of labour market participation. Section 8 concludes.

2

The ruro model In the present section, we present an application of the general ruro model (Dagsvik 1994) to job choice behaviour. This job choice model was developed by Dagsvik and Strøm (1992, 2003, and 2006), Aaberge, Dagsvik and Strøm (1995), Aaberge, Colombino and Strøm (1999, 2000), Dagsvik, Locatelli and Strøm (2006, 2007), Aaberge and Columbino (2013), Aaberge and Flood (2013), and Dagsvik and Jia (2014). We first illustrate how the ruro model extends the choice problem of traditional labour supply models from a question of trading off leisure against consumption towards a model of job choice, against other non–market alternatives of time use (Subsection 2.1). Then, we discuss the preference part of the model (Subsection 2.2). Finally, we expose the modelling of opportunities (Subsection 2.3).

2.1

Opportunities and jobs In general, the ruro model is an economic model of human choice behaviour. Human decision makers are assumed to choose the best element from a set of choice possibilities or opportunities, where ‘best’ is defined in terms of preferences (or, vice versa, preferences are derived from observed choice behaviour as that objective which would be maximised given those choices). Applied to job choice, the set of opportunities is to be thought of as a set of possible activities a particular individual might choose to execute. Some of these activities are rendered available through job offers. These job offers will be indexed by j, belonging to index set J. A job offer stipulates an amount of labour time to be supplied when accepting the offer, say h, and pays a wage, w. It is assumed that this wage can be expressed in units of time effectively spent on the job, so that (gross) revenues earned by the job equal the amount of time spent on the job times the wage. 7 Gross earned labour income is thus equal to wh. Gross earned labour income together with some other characteristics, say x f, among which unearned gross income (exclusive of transfers), determine the outcome of the gross to net (disposable) income function c = f (w, h; x f ), where c stands for consumption which in a static model as the present one coincides with disposable income. 8 That is, saving is considered as part of consumption. The function f converts gross income components into net disposable income, by subtracting taxes to be paid and adding transfers and subsidies. Usually, the generation of disposable income is constructed from raw data on gross income, labour time and other characteristics, by means of a microsimulation model. Besides time spent on the job and the remuneration, jobs exhibit a number of other characteristics such as degree of responsibility, variation and challenge of the tasks, safety, healthiness, physical effort, stress, relation with colleagues and superiors. These characteristics will be denoted by s. Preferences over these non–pecuniary attributes affect job choice. One might also decline all job offers. Evidently, not executing a formal job does not require any time to be spent on the formal labour market (h = 0), and is assumed not to pay a wage (w = 0). 9 A person who does not work, receives a net transfer (that is after deducting income taxes to be paid from her replacement income) equal to f (0, 0; x f ). In that case, time is spent on executing some of the available non–market opportunities. However the set of activities 10 one has alternatively available is not the same for all individuals, neither is the extent to which a particular alternative is available. When living in a small town, attending concerts, theatre or visiting museums is certainly not as easy as for big city dwellers. If you are in a wheel chair, hiking is not an option. Which of the available non–market activities will be chosen, in case no job offer is accepted, again depends on preferences (or, vice versa, 7 This is generally not the case. Output dependent bonuses or piece–rates do not necessarily bear an obvious relation with time spent on the job. More surprisingly, in a regime with fixed monthly wages, the wage per unit of time is variable, since the number of hours a regular (that is: full time) job requires can differ over jobs, and for a specific job, the number of hours to be worked per month is not fixed. Finally, even if there is a fixed hourly wage, and no bonuses, there is no obvious way how to treat paid holidays. Should they be taken into account when calculating an hourly wage or not? When taking these into account, this would result in an increase of the gross hourly wage, as compared to the wage specified in the contract. 8 We include the gross wage, and the number of hours worked as separate arguments in that function, as some aspects of the tax system, such as the Belgian work bonus may depend on the wage, rather than on labour income, wh. We are however aware that this might cause problems for the non–parametric identification of the ruro model. 9 How to treat informal jobs in this type of framework remains largely an unresolved question. 10 The word ‘activity’ will be used here in a broad sense, including occupations which are not very ‘active’ such as sleeping and day dreaming. A certain type of agency or control is however presumed, since otherwise it would be difficult to talk about choice behaviour.

what one chooses to do allows to derive something on the shape of preferences that person supposedly has). Non–market alternatives will be indexed by i, belonging to the index set I. The index sets for jobs and non–market alternatives respectively, are disjoint: I ∩ J = ∅. We will also use the index variable z to indicate an alternative in general, that is either a job or a non–market alternative. So, z ∈ Z := I ∪ J. Actually, an alternative z involves a set of activities. From the moment this set includes one or more jobs (be it only a part time job), the index z will belong to J, while it belongs to the set of non–market opportunities I otherwise. We will be somewhat sloppy in the sequel however, by calling an alternative involving one or more jobs in the formal labour market, sometimes simply a job.

2.2

Random utility In the model, preferences are defined over the number of hours h spent on jobs (which is zero if one chooses not to accept any job offer), consumption, c, and the set of other attributes, s, that a job or certain non–market activities possess, and that a person might care for. These other attributes are not observed by the researcher. The observable, and thus from a behaviour theoretic point of view relevant, bundle of characteristics an alternative z ∈ Z exhibits, is denoted by (C (z), H (z)), where C (z) refers to the individually specific net disposable income associated with executing activities indicated by z, and H (z) to the labour time involved by the activities indicated by z. The utility derived from these observable characteristics is denoted by V (C (z), T − H (z); x V ), where x V are the specific values of a set of preference shifters for the individual under consideration, and T denotes the number of time units available in the period over which labour time h is registered (e.g. 168 hours a week, if labour time is expressed in hours worked per week). Alternatively, one may define preferences over consumption and leisure. The latter, say `, is equal to the time left over for non–market activities, after subtracting labour time, ` := T − h. It is assumed that the econometrician can derive some evidence on the shape of the function V on the basis of observations on (c, T − h) and x V. So, no individual preference differences apart from those explained by observable characteristics x V, are allowed for in this part of the utility function, and V is therefore called the systematic part of the utility function, and, hence, of preferences. Since the other attributes besides disposable income and labour time are not observable, their contribution to utility will be specified as a random term. Thus, when a set of activities z bears attributes s = s (z), the utility these attributes generate, is denoted by the random variable ε (s (z)). So, each individual derives a specific utility from an activity z with attributes s = s (z), and this utility is considered as the realisation of a random variable. Different realisations of these terms (one for each value s could take) thus incorporate unobserved individual preference heterogeneity. It is assumed that this utility from non– pecuniary attributes, ε (s (z)), enters overall utility of an alternative z, in a multiplicatively separable way from the systematic part of the utility function. In order to make sense, this requires both, the systematic part of the utility, and the random term, to be positively valued functions. In summary, the total utility derived from picking an alternative z ∈ Z, denoted by U (C (z), H (z), s (z); x V ), equals: U (C (z), H (z), s (z); x V) := V (C (z), T − H (z); x V) · ε (s (z)).

(1) Now, since c = f (w, h; x f ), the systematic part of the utility function, V (c, T − h; x V ), implicitly defines a utility function, say Ψ, defined over hours worked on the formal labour market, h, and wage, w:

Ψ (w, h; x V, x f) := V (f (w, h; x f), T − h; x V).

(2) Consequently, we can define preferences also in the space of hours of work, wage, and other attributes, as follows:

U (f (W (z), H (z); x f), H (z), s (z); x V) := Ψ (W (z), H (z); x V, x f) · ε (s (z)), (3) where W (z) is the wage paid by activity z. More in particular, for someone not accepting any job offer, and choosing an alternative i ∈ I which exhibits characteristics s (i), the utility equals:

U (f (0, 0; x f), 0, s (i); x V) = Ψ (0, 0; x V, x f) · ε (s (i)).

(4) The domain of the systematic part of the utility function in the hours–wage space, Ψ (·; x V, x f ), is [0, ∞) × [0, T ].

2.3

Random opportunities Both, jobs and non–market activities, are not equally available to all individuals. The probability to receive a job offer as a civil engineer, for someone who has only completed secondary school, is e.g. zero. Something similar holds for non–market activities: they are not all equally available to all agents. Someone having lost her legs will not be able to run (or not in the same fashion as before), though she might continue to be fond of it. We will follow Dagsvik (1994), and Dagsvik and Strøm (2004, 2006) by describing the way alternatives are becoming available to individual agents by means of an inhomogeneous spatial Poisson process. In that case, the intensity parameter of that process captures the rate at which alternatives are rendered available to a specific individual. The higher the intensity of available alternatives bearing certain characteristics (wages within a certain range, hours within a certain interval and other attributes within a certain subset), the higher the expected number of this type of alternatives in the opportunity set of an individual. 11 In Appendix I we provide a brief introduction to inhomogeneous spatial Poisson processes. The intensity with which a job is offered to an individual, depends on a number of personal characteristics, such as skills, education, experience, and on the characteristics of the job itself, more specifically, the wage, the labour time regime of the job, and its other attributes. In equation (3), preferences were defined over the continuous set of all possible amounts of time spent on the jobs. In the real world, however, jobs requiring a non–rational number of hours a week, are for example not available. Be it alone to organise the production process, it might sometimes be required to have a number of people working together during a fixed number of hours. So, in practice, full–time, three–quarter time, half time, one– quarter time, or 20% jobs are more densely offered. Let g 2 (h; x g 2) be the intensity with which jobs requiring h hours of labour supply, are rendered available to an individual with characteristics x g 2. Similarly, jobs pay different wages, and personal characteristics can codetermine the intensity of job offers that pay on average higher wages. Let g 1 (w |h; x g 1) be the intensity with which, among the job offers requiring h hours of work, those paying a wage equal to w, are rendered available to a person with characteristics x g 1. Persons do not only care for the wage a job pays, and the number of hours to be worked, but also for the other attributes of a job. From a behavioural theoretic point of view, these are only important in as far as they yield a specific value for the multiplication factor in the utility function for those alternatives (see equation 1). Two jobs, j 1 and j 2 say, paying the same wage and requiring the same amount of hours, with attributes yielding the same value of the multiplication factor in the utility function for those alternatives, that is ε (s (j 1 )) = ε (s (j 2 )), are thus, according to the behavioural model of equation (1), equivalent to each other in the present model, and therefore will be considered as the same opportunity. The intensity with which job offers arrive which yield a value for the multiplication factor in the utility function equal to v, is denoted by λ 1 (v; x q ). In this function, x q refers to a set of personal characteristics that determine the intensity with which job offers arrive to that person. 12 We explicitly included age in these characteristics, in order to assess potential age 11 An alternative, frequentist description of the process that governs the availability of alternatives, resulting in the same empirical model, is provided by Aaberge, Columbino and Strøm (1999). Intensity is in that case captured by the relative frequency of job offers with certain common characteristics, available to a specific individual. 12 The use of the sub–index q for those characteristics will become clear later when we introduce the q–function as the proportion of the intensity of job offers relative to the degree of availability of non–market alternatives. In short, job offer arrivals depend on personal capacities and skills which are subdivided in differentials in the intensity of job offers. We assume the following functional form for λ 1:

λ 1 (v; x q) = π 1 (x q) , v 2 (5) where π 1 (x q) is a measure for the proportion of capacities and characteristics that are useful on the job market, relative to the total set of capacities an individual is endowed with. Therefore it is normalised such that it has range (0, 1). The functional form of λ 1 makes that attributes which are particularly disliked (yielding a very small value for v) are excessively abundant, while those that are particularly liked (yielding a very high value of v), are extremely scarce, irrespective of personal characteristics x q. These characteristics affect the level of λ 1 in a similar way, for all values of v. The functional form of λ 1 also guarantees independence of irrelevant alternatives in the probability of choosing jobs (Dagsvik, 1994). The distinguishing value of different potential non–market activities, is completely absorbed by the different values of the multiplication factor in the utility function they generate. Indeed, the systematic part of the utility function is for all non–market alternatives equal to Ψ (0, 0; x V, x f ). As for jobs with the same wage and required labour input, two non–market activities, i 1 and i 2 say, with attributes yielding the same value of the multiplication factor in the utility function for those alternatives, that is ε (s (i 1 )) = ε (s (i 2 )), are from a behavioural theoretic point of view equivalent to each other, and will therefore be considered as one and the same opportunity. Similarly as for jobs, it will be assumed that leisure activities which are particularly disliked, are abundantly available, while those that are intensely desired, are rather difficult to obtain. Also, personal characteristics, the same as those having an impact on the intensity with which jobs are offered, x q, are influencing the relative availability of non–market alternatives, and this is measured by the function π 0 (x q ). The intensity with which non–market activities yielding a multiplication factor equal to, denoted by λ 0 (; x q ), are accessible to an individual with characteristics x q, is thus assumed to be equal to:

λ 0 (; x q) = π 0 (x q) .

2 (6) As π 1 is a probability measure for the proportion of capacities and characteristics that are useful on the job market, the effect of the personal characteristics x q on the availability of non–market alternatives, π 0, runs in the reverse direction as that on job offer intensity. As a matter of normalisation it will thus be imposed that π 0 (x q) + π 1 (x q) ≡ 1. The reason is that we consider a variant of the model where we assume the stock of capacities an individual is endowed with, to be fixed. Some of these are currently valuable on the job market, others those apt to execute formal jobs, and those more suited for performing leisure activities. Next, there may be personal characteristics on the basis of which discrimination in job offers by employers might take place.

not. Increasing job availability then means that some of the capacities that hitherto were not demanded for on the market, become requisites of new jobs. 13 As the availability of a certain set of alternatives is governed by a stochastic process, the utility that can be obtained from potentially available alternatives, is a random variable too. We will derive the distribution of this utility from the stochastic process governing the availability of alternatives. This will prove useful for the derivation of the likelihood that an individual will choose a particular alternative from the set of available opportunities, in the next section (Section 3.1). We start with deriving the distribution of the utility level that can be obtained from non– market alternatives. Let E u (x V, x f) be the set of values for such that non–market alternatives yield a utility level larger than or equal to u: E u (x V, x f) := {∈ R + | ψ (0, 0; x V, x f) ≥ u}. Assuming that λ 0 defined in equation (6) is the intensity measure of a Poisson process, the number of non–market alternatives that yield a utility level of at least u, available to a person with characteristics (x V, x f, x q ), will be Poisson distributed (see Appendix I). Let this number of available non–market activities yielding a utility level of at least u, be denoted by N (Ψ (0, 0; x V, x f) ≥ u). According to the Poisson distribution, the probability that N (Ψ (0, 0; x V, x f) ≥ u) = n, is equal to:

n P (N (Ψ (0, 0; x V, x f) ≥ u) = n; x q) = (Λ 0 (E u (x V ,x f) ;x q )) exp [−Λ 0 (E u (x V ,x f) ;x q )] n!

(7) n = (π 0 (x q )Ψ (0,0;x V ,x f) /u) exp [−π 0 (x q )Ψ (0,0;x V ,x f) /u] n!

, where Λ 0 (E u (x V, x f); x q) equals the expected number of non–market opportunities available to an individual, yielding a utility level at least equal to u, and it is defined as:

## Z ∞

Ψ (0, 0; x V, x f) 0 λ 0 (; x q) d = π 0 (x q) Λ (E u (x V, x f); x q) := .

(8) u u/Ψ (0,0;x V ,x f) In the present case, the Poisson process is inhomogeneous, since the intensity measure λ 0 depends on the utility value, while in an ordinary Poisson process this is a constant parameter. The higher the value of Λ 0 (E u (x V, x f); x q ), the more skewed to the right the Poisson distribution (7) becomes, that is, the higher the probability that the number of available non–market alternatives, yielding a utility level at least equal to u, is relatively big. Consequently, the probability that all available non–market alternatives yield a utility level lower than u, equals the probability that the number of available alternatives with utility 13 This is a matter of interpretation. Estimates would not be affected by a different normalisation rule. In section 7 we illustrate the implications in case the assumption of a fixed set of capacities is also maintained when simulating counterfactual situations in which the job offer intensity would increase. Relaxing that assumption for simulation exercises is not straightforward, but would lead to different results with respect the potential welfare consequences of such an event.

larger than or equal to u, is zero: P (Ψ (0, 0; x V, x f) < u; x q) = P (N (Ψ (0, 0; x V, x f) ≥ u) = 0; x q) = exp [−Λ 0 (E u (x V, x f); x q )] (9) = exp [−π 0 (x q) Ψ (0, 0; x V, x f )/u].

From the last equation, it can be concluded that the potential utility that can be derived from the available non–market alternatives, which is a stochastic variable equal to U 0 := Ψ (0, 0; x V, x f), is Fréchet distributed with location parameter µ = 0, scale parameter σ 0 (x V, x f, x q) = π 0 (x q) Ψ (0, 0; x V, x f ), and shape parameter α = 1. 14 That is, the probability that U 0 (the utility from the available non–market alternatives) will be smaller than u, is equal to:

Z u P (U 0 ≤ u; x V, x f, x q) = σ 0 (x V ,x f ,x q) (v) 2 exp σ 0 (x V ,x f ,x q) − v 0 d v (10) σ 0 (x V ,x f ,x q) = exp − .

u This will prove useful when deriving the likelihood function in the next section (Section 3.1). We now turn to the derivation of the distribution of the utility level that can be obtained from possible job offers. 15 Job offers are characterised by a labour time regime h, a wage offer w, and the utility that can be derived from other attributes v. Let H be the set of all possible labour time regimes of jobs offered in the market, and W the set of possible wage offers. Wages can obtain any positive value. Let B := B h × B w be the Cartesian product of a measurable subset of labour time regimes B h ⊆ H, and wage offers B w = (0, w), for some positive w. Analogously to the modelling of the availability of non–market opportunities, the arrival of job offers to a person exhibiting characteristics (x V, x f, x g 1, x g 2, x q ), is modelled by an inhomogeneous spatial Poisson process. The intensity parameter of this Poisson process is equal to g 2 (h; x g 2) g 1 (w |h; x g 1) λ 1 (v; x q ). Denote the set of job offers specifying a labour time regime t ∈ B h, paying a wage lower than w (that is r ∈ B w ), and which yield a utility level at least equal to u, by U h,w,u (x V, x f) := {(t, r, v) ∈ B h × B w × R + | ψ (r, t) v ≥ u}.

h −α i In general, the class of Fréchet distributions is defined as: F (x; µ, σ, α) := exp − x−µ , where µ is σ a location parameter, σ a scale parameter, and α is a shape parameter. We could alternatively argue that the multiplier in the utility function, stemming from the attractiveness of the non–pecuniary attributes of non–market alternatives to a particular individual with characteristics (x V, x f, x q ), is Fréchet distributed with location parameter µ = 0, scale parameter σ = π 0 (x q ), and shape parameter α = 1. 15 As mentioned before, a ‘job offer’ is a short hand for ‘an alternative containing at least one job offer’. 14 Let N (B, u) be the number of job offers with a wage r belonging to B w, the number of hours to be worked in B h, and yielding a utility level larger than or equal to u. The probability for an individual with characteristics (x V, x f, x g 1, x g 2, x q) to be offered n such jobs is then equal to:

P (N (B, u) = n; x V, x f, x g 1, x g 2, x q) = n (Λ 1 (U h,w,u (x V ,x f) ;x g 1 ,x g 2 ,x q )) (11) exp [−Λ 1 (U h,w,u (x V ,x f) ;x g 1 ,x g 2 ,x q )] n!

.

Again, Λ 1 (U h,w,u (x V, x f); x g 1, x g 2, x q) can be interpreted as the expected number of job offers with labour time regime, wage, and utility level in U h,w,u (x V, x f ). It is defined by:

Λ 1 (U h,w,u (x V, x f); x g 1, x g 2, x q) :=

## R

g 2 (t; x g 2) =

## R

t∈B h

## R ∞

λ 1 (v; x q) dv dr dt u/Ψ (r,t;x V ,x f) g 1 (r |t; x g 1) r∈B w t∈B h π 1 (x q)

## R

g 2 (t;x g 2)

## R

r∈B w g 1 (r|t ;x g 1) Ψ (r,t;x V ,x f) dr dt u (12) .

The possible utility level obtained from jobs with a wage in B w, number of hours to be worked in B h, and other attributes yielding a value for the multiplicative factor equal to v, is a random variable too, denoted by U B. The probability that U B is less than u, denoted by P (U B < u; x V, x f, x g 1, x g 2, x q ), is equal to the probability that there are no job offers available that pay wages and specifying a working time in these ranges, and which yield a utility level of at least u:

P (U B < u; x V, x f, x g 1, x g 2, x q) = P (N (B, u) = 0; x V, x f, x g 1, x g 2, x q) = exp [−Λ 1 (U h,w,u (x V, x f); x g 1, x g 2, x q )] (13)

## R

## R

π 1 (x q) t∈B g 2 (t;x g 2) r∈B w g 1 (r|t ;x g 1) Ψ (r,t;x V ,x f) dr dt h .

= exp − u Again, it turns out that the randomness of the utility level U B that can be obtained from jobs with working time and wage combinations in B, which is governed by the stochastic process of job offers arriving to an individual, obeys a Fréchet distribution with location parameter µ = 0, scale parameter

## Z

## Z

σ B (x V, x f, x g 1, x g 2, x q) = π 1 (x q) g 2 (t; x g 2) g 1 (r |t; x g 1) Ψ (r, t; x V, x f) d r d t, t∈B h r∈B w and shape parameter α = 1. That is,

Z u P (U B < u; x V, x f, x g 1, x g 2, x q) = σ B c (x V ,x f ,x g 1 ,x g 2 ,x q) (v) 2 exp σ B c (x V ,x f ,x g 1 ,x g 2 ,x q) − v d v 0 (14) σ B (x V ,x f ,x g 1 ,x g 2 ,x q) .

= exp − u The derivation of this distribution is equally valid for any (measurable) subset B of the space of possible working times and wage combinations, job offers might exhibit. More in particular, it holds for the complement of B in the set of all possible working time wage combinations, defined as B c := B h c × B w c where B h c := H \ B h and B w c := [w, ∞). It follows that the utility level derivable from possible job offers with working time wage combinations in B c, is a Fréchet distributed random variable, say U B c, with location parameter µ = 0, scale parameter

## Z

## Z

σ B c (x V, x f, x g 1, x g 2, x q) = π 1 (x q) g 2 (t; x g 2) g 1 (r |t; x g 1) Ψ (r, t; x V, x f) d r d t, c t∈B h c r∈B w and shape parameter α = 1. That is,

Z u P (U B c ≤ u; x V, x f, x g 1, x g 2, x q) = σ B c (x V ,x f ,x g 1 ,x g 2 ,x q) (v) 2 exp σ B c (x V ,x f ,x g 1 ,x g 2 ,x q) − v 0 d v (15) σ B c (x V ,x f ,x g 1 ,x g 2 ,x q) .

= exp − u 3 3.1

Likelihood function, functional form, and estimation

Derivation of the likelihood Now we turn to the behavioural implications of the model explained in Section 2. From the available job offers and non–market opportunities, a person will choose that alternative she likes most. The probability that this will be an alternative including a job offer with a working time wage combination in the set B, is equal to the probability that U B ≥ max {U 0, U B c }. As the processes governing the arrival of job offers and non–market opportunities are assumed to be independent, the probability that U B (the utility from a job offer with a labour time and wage combination in B) is equal to or greater than max {U 0, U B c }, is equal to the product of the probability that U B is greater than or equal to U 0 and the probability that U B is greater than or equal to U B c. That is, the product of the probability that U 0 is smaller than a certain non–negative value u and the probability that U B c is smaller than that same value u, evaluating that joint probability weighted by the likelihood that U B takes on the value u, and integrating this over all possible values u that U B could assume: P (U B ≥ max {U 0, U B c}; x V, x f, x g 1, x g 2, x q) =

## Z ∞

σ B (x V ,x f ,x g 1 ,x g 2 ,x q) (u) 2 "

exp − ( σ B x

## V

,x f ,x g 1 ,x g 2 ,x q u ) # "

exp − ( σ B c x

## V

,x f ,x g 1 ,x g 2 ,x q u ) # "

exp ( σ 0 x ,x f ,xq

## V

− u # ) d u 0

## Z ∞

σ B (x V ,x f ,x g 1 ,x g 2 ,x q) = (u) 2 σ B (x V ,x f ,x g 1 ,x g 2 ,x q) +σ B c (x V ,x f ,x g 1 ,x g 2 ,x q) +σ 0 (x V ,x f ,x q) d u exp − u (16) 0 = = σ B (x V ,x f ,x g 1 ,x g 2 ,x q) σ B (x V ,x f ,x g 1 ,x g 2 ,x q) +σ B c (x V ,x f ,x g 1 ,x g 2 ,x q) +σ 0 (x V ,x f ,x q)

## R

g 2 (t;x g 2) r∈B w g 1 (r|t ;x g 1) Ψ (r,t;x V ,x f) d r d t

## R

## R

.

π 0 (x q )Ψ (0,0;x V ,x f) +π 1 (x q) t∈H g 2 (t;x g 2) r∈W g 1 (r|t ;x g 1) Ψ (r,t;x V ,x f) d r d t π 1 (x q)

## R

t∈B h In a similar fashion, it can be derived that the probability to choose a non–market alternative, is equal to the probability that U 0 is equal to or greater than U B∪B c, which is equal to: P (U 0 ≥ U B∪B c; x V, x f, x g 1, x g 2, x q) = π 0 (x q )Ψ (0,0;x V ,x f)

## R

## R

.

π 0 (x q )Ψ (0,0;x V ,x f) +π 1 (x q) t∈H g 2 (t;x g 2) r∈W g 1 (r|t ;x g 1) Ψ (r,t;x V ,x f) d r d t (17) We noted before that the model assumes that the characteristics x q which influence the intensity with which job offers arrive to a person endowed with those characteristics, are the same as those affecting the degree of availability of non–market alternatives, but acting in the opposite direction. Equations (16) and (17) make clear that this is necessary for identifying the model. Indeed, the same result would be obtained when dividing through the numerator and denominator by π 0 (x q ). We therefore introduce the notion of relative intensity with which job offers arrive, as compared to the degree to which non–market alternatives are available:

q (x q) := π 1 (x q) .

π 0 (x q) (18) Estimating the parameters of this function, and assuming that 0 ≤ π i (x q) ≤ 1 for all x q, and i = 0, 1, and π 1 (x q) + π 0 (x q) = 1, will allow then to recover both π 1 (x q) and π 0 (x q ). An additional assumption necessary for identification, is the independence of the wage offer distribution from the hours specified by the job offers. That is g 1 (w |h; x g 1) = g 1 (w; x g 1 ), ∀ h ∈ H.

From equation (16), it follows that the likelihood 16 that a person with characteristics (x V, x f, x g 1, x g 2, x q) will choose one particular job offer requiring labour time h, and paying a wage w, is equal to:

ϕ (w, h; (x V, x f, x g 1, x g 2, x q )) = q(x q )Ψ (w,h;x V ,x f) g 1 (w;x g 1) g 2 (h;x g 2)

Ψ (0,0;x V ,x f) +q(x q)

## R

## R

s∈W t∈H , Ψ (s,t;x V ,x f) g 1 (s;x g 1) g 2 (t;x g 2) d t d s (19) Similarly, the likelihood her most preferred non–market alternative is preferred to any of the job offers, equals:

ϕ (0, 0; (x V, x f, x g 1, x g 2, x q )) =

Ψ (0,0;x V ,x f)

Ψ (0,0;x V ,x f) +q(x q)

## R

## R

s∈W t∈H .

Ψ (s,t;x V ,x f) g 1 (s;x g 1) g 2 (t;x g 2) d t d s (19’) It is worthwhile to compare the likelihood function (19)–(19) with what is obtained in a random utility function based upon discrete choice of labour time regimes (such as in Van Soest 1995, or Creedy and Kalb 2005). In this approach, the wage a person obtains, is, apart from measurement problems (see footnote 6), a fixed individual characteristic reflecting that person’s productivity. Choice of labour time is free but limited to a discrete set of alternatives, say {h k; k = 1, 2,..., K}. Under the assumption that the stochastic parts of the utility functions are Fréchet distributed, the likelihood (probability) to observe an individual choosing a labour time regime h l equals:

ϕ (w, h l; x V, x f) = Ψ (w, h l; x V, x f) .

## K

## P

Ψ (0, 0; x V, x f) + Ψ (w, h k; x V, x f) (20) k=1 The difference with (19)–(19) is twofold. Firstly, in the ruro model utilities are weighted with the intensity with which alternatives are rendered available to an individual. Next, the wage is part of the job offer. Consequently the denominator sums over all possible pairs of wages and labour time regimes, (w, h), and not only over possible labour time regimes for a given wage. Up to now, we exclusively concentrated on individual decision makers. The model is easily extended to the case of households consisting of couples (with or without children), if one is willing to assume a unitary decision making model. More specifically, it is assumed that both partners have identical tastes specified over household consumption, each of the partners’ leisure time, and other attributes associated with the activities the partners execute. The 16 We use the term likelihood, though, in econometrics, the likelihood would express this as function of the parameters of the model to be estimated.

systematic part of partners’ common utility function defined over the space of partners’ wages and working time, (w 1, h 1, w 2, h 2 ), is denoted by Ψ. If one assumes that each partner’s process of job offer arrivals and availability of non–market alternatives is independent of that of the other, one arrives at the following expressions for the likelihood that both partners, respectively, only one of them, or none of both, will accept a job offer:

Ψ (w 1 ,h 1 ,w 2 ,h 2 ;x V ,x f) ϕ w 1, h 1, w 2, h 2; x V, x f, x g j, x g j, x q j; j = 1, 2 1 ϕ w 1, h 1, 0, 0; x V, x f, x g j, x g j, x q j; j = 1, 2 1 = 2 = 2 ϕ 0, 0, w 2, h 2; x V, x f, x g j, x g j, x q j; j = 1, 2 = ϕ 0, 0, 0, 0; x V, x f, x g j, x g j, x q j; j = 1, 2 = 1 1 2 2

## Q

j=1,2 q j (x qj) g 1 j w j ;x j g 1 g 2 j h j ;x j g 2

Ψ (0,0,0,0;x V ,x f) +A+B+C Ψ (w 1 ,h 1 ,0,0;x V ,x f) q 1 (x q 1) g 1 1 w 1 ;x g 1 g 2 1 h 1 ;x g 1 1 2

Ψ (0,0,0,0;x V ,x f) +A+B+C Ψ (0,0,w 2 ,h 2 ;x V ,x f) q 2 (x q 2) g 1 2 w 2 ;x g 2 g 2 2 h 2 ;x g 2 1

Ψ (0,0,0,0;x V ,x f) +A+B+C

Ψ (0,0,0,0;x V ,x f)

Ψ (0,0,0,0;x V ,x f) +A+B+C 2 , , , , (19”) with:

A := q 1 x q 1

## R

B := q 2 x q 2

## R

## R

s 1 ∈W t 1 ∈H

## R

s 2 ∈W t 2 ∈H

## C :=

## R

## R

## R

## R

Ψ (s 1, t 1, 0, 0; x V, x f) g 1 1 s 1; x g 1 1 g 2 1 t 1; x g 2 1 d t 1 d s 1, Ψ (0, 0, s 2, t 2; x V, x f) g 1 2 s 2; x g 1 2 g 2 2 t 2; x g 2 2 d t 2 d s 2, Ψ (s 1, t 1, s 2, t 2; x V, x f) s 1 ∈W t 1 ∈H s 2 ∈W t 2 ∈H

## Q

j=1,2 q j x q j g 1 j s j; x g j g 2 j t j; x g j dt 2 ds 2 dt 1 d s 1.

1 2 The relative intensity of job offers, the wage offer density, and the labour time density of partner all become partner j specific: q j, g i j (i = 1, 2), where j (j = 1, 2). For couples, the non–market alternative is that alternative in which none of both partners is engaged in the formal labour market.

3.2

Identification Some parts of the model are non–parametrically identified. A fuller treatment of this issue is provided in Aaberge, Columbino and Strøm (1999), the working paper version of Dagsvik and Strøm (2006) (See Dagsvik and Strøm 2004), and Dagsvik and Jia (2014). The main line of argument for identifying the wage offer distribution apart from preferences runs as follows. Isolate an observationally equivalent group of individuals in the population. By this we mean that all its members have the same value for all the conditioning variables of the model, that is for (x V, x f, x g 1, x g 2, x q ). So, we omit these arguments from ϕ, and read these densities as for given values of those variables, whatever these values might be. Identify within this group two subgroups, each supplying different number of hours, say h 1 and h 2, for the same wage w. The relative proportion of these subgroups in the population is ϕ (w, h 1) /ϕ (w, h 2 ), which according to the model in equation (19) reduces to: ϕ (w, h 1) Ψ (w, h 1) g 2 (h 1) = .

ϕ (w, h 2) Ψ (w, h 2) g 2 (h 2) (21) Doing this for different levels of wages, allows to identify the function Ψ (w, h) g 2 (h). Looking then at persons performing the same number of hours, but accepting different wages, w 1 and w 2 say, gives: ϕ (w 1, h) Ψ (w 1, h) g 2 (h) g 1 (w 1) = .

ϕ (w 2, h) Ψ (w 2, h) g 2 (h) g 1 (w 2) (22) As Ψ (w, h) g 2 (h) was already identified in the previous step, it is now possible to identify

## R

g 1 (w), using the fact that it is a density, and thus that w∈W g 1 (w) d w = 1. Then, consider an observationally equivalent group of persons in the population. Some of them will be engaged in a formal job, and some of them not. The relative proportion of those groups in the population are: ϕ (w, h) Ψ (w, h) q g 1 (w) g 2 (h) = .

ϕ (0, 0)

## Ψ (0, 0)

(23) As Ψ is a utility function, we can normalise the value of Ψ (0, 0), which allows to identify q from this equation. In our empirical application, we tried to improve upon the non– parametric identification of q by introducing an exclusion restriction. More specifically, a group specific unemployment rate 17 is added as an explanatory variable for q. We assume that this variable does not affect individual preferences, but, obviously, it has some relation with the structure of labour demand. The utility function Ψ (w, h) and the distribution of offered labour time regimes g 2 (h) are however not separately non–parametrically identified. One way out is to give a more fundamental justification of the functional form used for preferences (see equation 21). For example, Dagsvik and Røine Hoff (2011) and Dagsvik (2013) give a non–parametric justification of the preferences embodied by the Box–Cox type of utility functions that we will use (see the next section). Moreover, it can be argued that the occurrence of peaks in the distribution of the number of hours worked, as observed in many datasets, around half time, three quarter time and 17 Ideally one would use the number of vacancies for suitable jobs for certain identifiable groups of persons in the population, but, this type of information is not really observable.

full time work, are not easily explained by the traditional way preferences are shaped in economics, neither by the kinks in the shape of the budget set caused by different tax structures.

3.3

Functional forms In the present section we present the functional forms of the different components of the model that will be used in the empirical application in Section 5. At the preference side, 18 – the systematic part of the function is for singles of the Box–Cox type:

α log utility α c ) h −1 , with α c, α h < 1. Intensity ln V (c, T − h; x V) = β c · c α c −1 + (β 0 h x V) · ((T −h)/T α h of preferences for leisure is increasing (decreasing) in an element of x V, if the associated parameter of β h is positive (negative). 19 The exponents, α c and α h, determine the curvature of the indifference curves in terms of labour time and consumption. The lower these are, the less substitutable leisure and consumption are;

– for couples, a unitary decision model is assumed, but spouses’ leisure time, is considered to be an assignable good. So, preferences are defined over consumption and each spouse’s leisure time. Partner’s time endowments are equal. An interaction term capturing potential complementarities between partners’ leisure time is added to the utility function. The vector of taste shifters is subdivided into two parts, each collecting the variables that apply to the respective partner (with possibly some overlaps): x V,c := (x V,1, x V,2 ). The utility function for couples as::

α thus reads ((T −h i )/T) αhi −1

## P

0 c c,g −1 ln V (c, T − h 1, T − h 2; x V,c) = β c,g · + i=1,2 β h i x V,i · α c,g α h i +β h 1 ,h 2 ·

## Q

i=1,2 αh ((T −h i )/T) α hi i −1 , with α c,g, α h i < 1 (i = 1, 2). The interpretation of the exponents and the β 0 h i (i = 1, 2) remains the same as for singles; in addition, β h 1 ,h 2 > (<)0 means that partners’ leisure are complements (substitutes).

At the opportunity side, – the logarithm of the intensity of job offers relative to the availability of non–market alternatives is linear in the covariates: ln q (x q) = η 0 q x q. The vector x q should contain a constant term, and the associated coefficient is denoted by η q,0;

18 19 For a justification, see Dagsvik and Røine Hoff (2011), and Dagsvik (2013).

More details are provided in Section 5.1.

– the wage density g 1 (w; x g 1) is assumed to be lognormal:

2 0 ln w−δ x g g 1 1 g 1 (w; x g 1) = w·σ· 1 √ 2π exp − 2 1 ; and σ – the distribution of the labour time regimes offered, is piecemeal uniform. 20 There are a number of, say K, peaks, indexed by k = 1, 2,..., K, around which the bulk of the job offers’ labour time regimes are concentrated (typically around half time, that is

## 18.5 to 20.5 hour a week in our application, three quarter time, or 29.5 to 30.5 hours

a week, and full time, or 37.5 to 40.5 hours). The lower and upper bound of peak k (k = 1, 2,..., K) are denoted by respectively H k and H k. There is a lower limit, H min, below which job offers are not considered to belong to the formal labour market (fixed at one hour a week in the application below); and an upper limit of labour time spent on formal jobs, denoted by H max, and fixed at 70 hours per week in our application.

This results in the following density function:

g 2 (h; x g 2) =   γ    1     γ exp γ 1 k + 1 h h h h if h ∈ [H min, H 1 [, h ∈ H k, H k + 1, or h ∈ H K, H max, k = 1, 2,..., K − 1, h h if h ∈ H k ,H k, k = 1, 2,..., K.

The only covariate influencing this function will be the sex of the person. An example of such a distribution function is given in Figure 1.

3.4

Estimation To estimate the parameters governing preferences, the relative intensity of market over non– market alternatives, and the distribution of wage offers and labour time regimes, a likelihood function, say L, is constructed on the basis of equations (19), (19’) and (19”). The individual contributions of a single to that likelihood function are indeed composed of the likelihood that the observed choice is the most preferred one, reflected in equations (19), or (19’), depending on whether the observed choice involves participation on the formal labour market executing a job (or a set of jobs) requiring h hours of work, and paying a wage w, or whether it is the non–market alternative. In these expressions, the numerator is thus evaluated at the actually observed choice, when constructing the likelihood function. Similarly, for couples, the first, 20 This makes that hours restrictions in the job offers have formally a similar implication as including dummies for part time and full time work in a discrete choice labour supply model, as was proposed already in the seminal paper of Van Soest (1995).

Figure 1: Peak distribution for labour time regimes 0.10  1 exp   4  0.09 0.08 0.07  1 exp   3  0.06  1 exp   2  0.05 0.04 0.03 0.02  1  1  1  1 0.01 0.00 1-18.5 18.5-20.5 29.5-30.5 37.5-40.5 40.5-70 Labour time regime of the job offer (hours per week) second, third, or fourth equation in (19”) applies, dependent on whether both partners, only partner j (j = 1, 2), or none of both actually are engaged in formal jobs. In practice, we do not observe the set of wage offers, W, nor the offered labour time regimes, H. Therefore, a set of alternatives in the space of wages and labour time regimes is sampled from a prior density function, say P (w, h; x P ). This prior may be individually specific through its possible dependence on the covariates x P. Denote the set of sampled combinations of wage offers and labour time regimes, possibly including the non–market alternative, by D. The observed choice w obs, h obs is to be always included in the sampled choice set. From the sampling densities P (w, h; x P ), the likelihood to sample a set D given that the observed choice equals w obs, h obs, can be constructed. 21 It is denoted by P D w obs, h obs, and it equals:

P D w obs, h obs :=

## Y

i:(w i ,h i )∈D

P (w i, h i; x P) .

P (w obs, h obs; x P) 21 (24) The issue of sampling choice sets for estimating the ruro model is discussed more in detail in Appendix II. It is an application of methods for estimating discrete choice models with large or latent choice sets developed by McFadden (1978) and Ben–Akiva and Lerman (1985). It is discussed also in Aaberge Dagsvik and Strøm (1995), Aaberge, Columbino and Wennemo (2009), Train (2009), and Lemp and Kockelman (2012).

Recall that the probability (density) that a job paying a wage w, and requiring a number of h hours to be worked, would be optimal given a choice set C := {0, 0}∪W ×H, was derived in equations (19), and in (19’) if the non–market alternative would be the most preferred option. The unconditional probability to sample a choice set D, denoted by Π (D), can thus be written as 22:

## X

## Π (D) =

P (D |(w i, h i )) ϕ (w i, h i; (x V, x f, x g 1, x g 2, x q )).

(25) i:(w i ,h i )∈D Using Bayes’ law, the probability (density) to observe an agent choosing a job offer that pays a wage w i and requires h i hours of labour time from the sampled set D, thus equals:

ϕ e (w i, h i; (x V, x f, x g 1, x g 2, x q, x P) |D) = P (D |(w i, h i )) ϕ (w i, h i; (x V, x f, x g 1, x g 2, x q )) .

## Π (D)

(26) Using equations (24) and (25), we can thus reformulate the simulated likelihood to observe someone choosing an alternative (w, h) from a choice set D sampled according to the prior P (w, h; x P ), as: ϕ e (w, h; (x V, x f, x g 1, x g 2, x q, x P) |D) = Ψ (w,h;x V ,x f) q(x q )g 1 (w;x g 1) g 2 (h;x g 2) /P(w,h;x P) (

Ψ 0,0;x ,x f

## V

) (

Ψ s,t;x +

P (0,0;x P)

## P

(s,t)∈D\{(0,0)}

## V

,x f ) q (x q) g 1 (s;x g 1) g 2 (t;x g 2) Ψ (w,h;x V ,x f) q(x q )g 1 (w;x g 1) g 2 (h;x g 2) =

Ψ (0,0;x V ,x f) +

## P

(s,t)∈D\{(0,0)} (27)

P (s,t;x P)

P (0,0;x P)

P (w,h;x P) Ψ (s,t;x V ,x f) q(x q )g 1 (s;x g 1) g 2 (t;x g 2)

P (0,0;x P) .

P (s,t;x P) The corresponding expression for choosing the non–market alternative equals: ϕ e (0, 0; (x V, x f, x g 1, x g 2, x q, x P) |D) (27’)

Ψ (0,0;x V ,x f) =

Ψ (0,0;x V ,x f) +

## P

(s,t)∈D\{(0,0)} Ψ (s,t;x V ,x f) q(x q )g 1 (s;x g 1) g 2 (t;x g 2)

P (0,0;x P) .

P (s,t;x P) Some further issues are in order. First, note that the constant term of the q (x q )–function, exp (η q,0 ), occurs in any term of the likelihood where γ 1 appears (that is, in those terms of the sum pertaining to a job offer on the formal labour market, (w, h): w, h > 0), and each time these terms appear as a product. Therefore both, η q,0 and γ 1, cannot be estimated separately. But γ 1 is still identified by the definition:

## P

## P K

γ 1 H max −H K + K−1

## H

## −H

+

## H

−

## H

+

## H

−

## H

exp γ (28) k + 1 k 1 min k k k ≡ 1.

k=1 k=1

22 For simplicity of notation, we drop the arguments (x V, x f, x g 1, x g 2, x q) that might influence the shape of Π (D).

This means in practice that one does not estimate all the parameters in the likelihood (27) (respectively 27’), but rather reduces these equations to: ϕ e (w, h; (x V, x f, x g 1, x g 2, x q, x P) |D) Ψ (w,h;x V ,x f) q e (x q )g 1 (w;x g 1) g 2 (h;x g 2) =

Ψ (0,0;x V ,x f) +

## P

(s,t)∈D\{(0,0)}

P (0,0;x P) (29)

P (w,h;x P) Ψ (s,t;x V ,x f) q e (x q )g 1 (s;x g 1) g 2 (t;x g 2)

P (0,0;x P) ,

P (s,t;x P) where:

g 2 (h; x g 2) = q e (x q) g 2 (h;x g 2) , γ 1 = γ 1 q (x q).

For the likelihood to choose a non–market alternative, this becomes: ϕ e (0, 0; (x V, x f, x g 1, x g 2, x q, x P) |D) (29’)

Ψ (0,0;x V ,x f) =

Ψ (0,0;x V ,x f) +

## P

(s,t)∈D\{(0,0)} Ψ (s,t;x V ,x f) q e (x q )g 1 (s;x g 1) g 2 (t;x g 2)

P (0,0;x P) ,

P (s,t;x P) Secondly, as far as (some parts of) the probability to sample a job offer, that is an alternative (w, h) such that w, h > 0, is (are) independent of the specific value of either w, or h, or both, one can drop that part from the likelihood, and it will be absorbed by the constant term of the q (x q )–function. For example, assume wages are sampled from a lognormal distribution with parameters µ and ς, labour time is sampled from the uniform distribution on the [H min, H max )–interval, and the probability to sample non–market alternatives is the observed inactivity degree in the sample (that is the relative number of persons in the sample being engaged in formal jobs for less than one hour a week), say π 0 obs. 23 That is: P (w, h; x P) = π 0 obs = if (w, h) = (0, 0), 1 − π 0 obs (wς √ 2π) −1 exp (ln w−µ)2 − 2ς 2

H max −H min = 0

The factor π 0 obs 1−π (0 obs) (30) if w > 0, h ∈ [H min, H max [, otherwise.

(H max − H min) occurs then in all terms of the likelihood for which w, h > 0. Suppose now that one drops this factor from the likelihood and estimates on the basis of:

ϕ e (w, h; (x V, x f, x g 1, x g 2, x q, x P) |D) = Ψ (w,h;x V ,x f) q (x q) g 1 (w;x g 1) g 2 (h;x g 2) ς exp

Ψ (0,0;x V ,x f) +

## P

(s,t)∈D\{(0,0)} (ln w−µ)2 2ς 2 (31) (ln s−µ)2 Ψ (s,t;x V ,x f) q (x q) g 1 (s;x g 1) g 2 (t;x g 2) ς exp 2ς 2 23 , 2 These are the specifications we will actually follow, with π 0 obs = .104, µ = 2.71, and ς = .308 for males, and the corresponding numbers for females are .246, 2.63, and .297.

where:

√ g 1 (w; x g 1) = w 2πg 1 (w; x g 1), g 2 (h;x g ) 2 , g 2 (h; x g 2) = γ 1 q (x q) = γ 1 (H max − H min) π 0 obs q (1−π 0 obs) (x q) = (H max − H min) π 0 obs q e (x q).

(1−π 0 obs)

For the non–market alternative, we obtain:

ϕ e (0, 0; (x V, x f, x g 1, x g 2, x q, x P) |D)

Ψ (0,0hx V ,x f) =

Ψ (0,0;x V ,x f) +

## P

(s,t)∈D\{(0,0)} (ln s−µ)2 Ψ (s,t;x V ,x f) q (x q) g 1 (s;x g 1) g 2 (t;x g 2) ς exp .

(31’) 2ς 2 This means that using equations (31)–(31’) in the construction of the likelihood function, would yield exactly the same estimates as using equations (29)–(29’), except for the (multiplicative) constant term of q e (x q) in (29)–(29’), which provides an estimate of γ 1 exp η q,0, while in equations (31)–(31’), the (multiplicative) constant of q (x q) is an estimate of π obs γ 1 (H max − H min) 1−π 0 obs exp η q,0.

(0) In both cases, one is able to back out an estimate of η 0,q by using equation (28). In the first case, one subtracts ln γ b 1 (with γ b 1, the estimated value of γ 1 from applying equation (28) using the estimates for q (x q )).

γ k + 1, for k = 1, 2,..., K) from the estimated constant of ln (e π obs needs to be subtracted from the estimated

In the second case, ln γ b 1 (H max − H min) 1−π 0 obs (0) constant of ln q (x q). The estimates reported below in Table 4 are inclusive of γ 1, but do not contain the sampling correction terms. That is, we used specification (29)–(29’).

3.5

Simulation In order to evaluate the fit of the estimates, or the estimated model’s prediction of behavioural reactions to changes in explanatory variables, a simulation method is used. A choice set is drawn (possibly capturing changes in the intensity with which certain alternatives become available to certain persons) and then it is determined what an agent’s best choice would be within this simulated choice set, according to the estimated preferences of that person. If simulation is used for evaluating the fit of the estimated model, then the choice set is drawn according to the model estimates (the relative intensity of job offers, the wage offer distribution, and the labour time regime offers), and the simulated choices from that set are to be compared with actual ones, as observed in the data. This is done in Figures 7–12 below (Section 6.1). Next, we will also use the simulation method for calculating elasticities, and to evaluate some counterfactuals (see Sections 6.2 and 7).

Actually, simulating with the estimated model can be done along two lines. Either one uses the estimated measure of intensity with which alternatives (w, h) are offered to an agent, that is, using the estimates of the q–function, the estimated wage offer distribution, g 1, and the estimated hours distribution, g 2, to sample a choice set {(w r, h r); r = 1, 2,..., R}. Next, one draws for each of the sampled alternatives, (w r, h r ), a random variable from the Extreme Value Type I distribution 24, say (w r, h r ). Then it is evaluated which of the drawn alternatives yields the highest utility: ln V b (f (w r, h r; x f), T − h r; x V )+ (w r, h r ). The alternative (w r, h r) thus yielding the highest utility is considered to be the agent’s optimal choice according to the model. Alternatively, one draws from a prior, P 1 (w, h; x P 1 ), and looks which alternative has the highest likelihood to be chosen. As the denominator in the likelihood (19) is the same for all alternatives, that maximum is determined by the numerator. Thus, one looks for the

P 1 (0,0;x P) maximum of V b (f (w r, h r; x f), T − h r; x V) q b (x q) g b 1 (w r; x g 1) g b 2 (h r; x g 2) P w ,h ;x 1 over the 1 (r r P 1) drawn elements (w r, h r) for which w r, h r > 0. Denote the alternative yielding the maximum by (w r ∗, h r ∗ ). The alternative chosen according to this second simulation method coincides with this maximum, (w r ∗, h r ∗ ), if V b (f (w r ∗, h r ∗; x f), T − h r ∗; x V) q b (x q) g b 1 (w r ∗; x g 1) g b 2 (h r ∗; x g 2) P 1

P 1 (0,0;x P 1) > (w r ∗ ,h r ∗ ;x P 1) V b (f (0, 0; x f), T; x V).

Else, the non–market alternative is the simulated optimal choice. The practice in Statistics Norway, by Aaberge and his collaborators, has been to follow a go between. Wages are drawn from the estimated wage distribution g b 1 (w; x g 1 ). Hours and the proportion of market versus non–market alternatives are drawn from the same priors as for the sampling of the choice set for the estimation: the uniform distribution on [H min, H max [ for the labour time, and the observed participation degree in the sample, 1 − π 0 obs, for the number of market alternatives. Then, the simulated optimal choice, (w r ∗∗, h r ∗∗ ), say, is determined as follows:

(w r ∗∗, h r ∗∗) := arg max (w r ,h r )∈{{(0,0)}∪{(w r ∗ ,h r ∗ )}} n o b (w r ∗, h r ∗; x, x f) b ∗; x g) + (w r ∗, h r ∗) b

A, ln Ψ q (x ) g (h , q 2 r 2

## V

(32) n o b (w r, h r; x, x f) + (w r, h r), ∀ r: (w r, h r) = (0, 0), and where A := ln Ψ

## V

n o b (w r, h r; x, x f) b b (w r ∗, h r ∗ ):= arg max ln Ψ q (x ) g (h ) + (w , h ) , ∀ r :

w , h > 0 .

q 2 r r r r r

## V

(w r ,h r ):w r ,h r >0

24 The logarithm of a standard Fréchet (that is with parameters µ = 0 and σ, α = 1) distributed random term is Extreme Value Type I distributed.

Notice that if one would have formulated the likelihood including the correction terms for sampling hours from the uniform distribution, and non–market opportunities from the within sample observed probability of being non–active, the equivalent of the expressions over which the maximum is taken in the bottom line of equation (32), would be:

obs π 0 b (x q) b b (w r, h r; x, x f) q e + (w r, h r).

ln Ψ g 2 (h r; x g 2) + ln (H max − H min) + ln

## V

1 − π 0 obs It can be seen from the definition of q (x q) below equation (31), and the definition of q e (x q) below equation (29), that both expressions are equivalent. Furthermore,

## K

h h

## X

0 b b b q x q + ln γ ln q e (x q) g 2 (h r; x g 2) = η b 1 + χ h r ∈ H k ,H k γ b k +1, k=1 where χ (condition) is the indicator function, which equals one if the condition serving as its argument is satisfied, and equals zero otherwise. Another in between simulation method is continuing to draw hours from the uniform distribution on [H min, H max [, but using the estimated rate of market to non–market opportunities, q b (x q ), to determine the intensity of sampling formal labour market jobs. The criterion to determine the most preferred job offer from the sampled set, (w r ∗, h r ∗ ), that replaces the bottom line of equation (32) in this case, becomes:

(w r ∗, h r ∗) := arg max (w r ,h r ):w r ,h r >0 n o b (w r, h r; x, x f) γ b ln Ψ b

## (H

−

## H

) g (h ;

x ) + (w , h ) , ∀ r :

w , h > 0 , 1 max min 2 r g r r r r 2

## V

(33) irrespective of whether the sampling correction terms have been included in the likelihood or not. In the results presented below in section 6.1 the first method of simulating was used. That is: market alternatives were drawn from the estimated wage offer and offered labour time regimes, and the relative number of job offers to non–market alternatives is determined by the estimated q-function. A similar approach is followed for constructing the counterfactuals in the simulation exercise of section 7.

4

Data The model is estimated on the Belgian database of the European Union Statistics on Income and Living Conditions (eu–silc). We use the data that were collected in 2007. The entire dataset consists of 6348 households or 15493 individuals. It is representative for the Belgian population of private households. Persons living in collective households or institutions are Table 1: Descriptive statistics for the estimation sample

Singles

Couples

Description

Female

Male

Female

Male

Age (years) 41.1 39.9 38.1 40.2 % hh having 0-3 year old children 5.78% 0.45% 18.67% 18.67% % hh having 4-6 year old children 9.46% 0.89% 17.16% 17.16% % hh having 7-9 year old children 10.16% 1.78% 18.19% 18.19% 21.3 20.6 18.0 20.4

Low educated 22.8% 24.5% 16.8% 19.8%

Secondary education 34.6% 41.9% 38.5% 39.0%

High educated 42.6% 33.6% 44.7% 41.2%

Brussels 19.8% 21.2% 9.3% 9.3%

Flanders 44.1% 45.2% 58.5% 58.5%

Wallonia 36.1% 33.6% 32.3% 32.3% 68.12 78.84 79.40 93.20

Conditional on working 35.88 39.69 32.50 40.84

Unconditional 24.45 31.29 25.81 38.06

Hourly wage (euro) 14.91 15.20 14.73 16.25

Disposable income (e /month) 1567 1588 3143

Number of observations 571 449 1457

Potential experience (years)

Education:

Residence:

Participation rate (%)

Hours worked/week:

Source: Own Calculations, EU-SILC 2007

excluded from the target population. The survey provides detailed information on earnings as well as on socio–demographic characteristics of each household. We selected three sub–samples, respectively from the subset of households in which the reference person is living with a partner of different sex (couples), from households with female reference person not living with a partner (single females), and from households with male reference person not living with a partner. Only households in which the reference person and his or her partner in case of couples, are available for the labour market; i.e. aged between 16 and 64 year and not being sick, in education, disabled or (pre)retired. Self– employed are excluded due to the lack of reliable information on hours worked and income earned. Mixed households in which only one of the partners is available for the labour market are also excluded. Finally, we drop households whose children are already available for the labour market but are still living with their parents. It is reasonable to assume that their labour supply decisions are different from those of a household without working children because it is not clear whether the members of such households consider their labour supply decisions as a collective or as an individual process. Given this data selection, we are able to estimate the labour supply model on 1457 couple households, 571 single females, and 449 single males. euromod is used as microsimulation tool for the calculation of net disposable income for each element in the opportunity set of households. 25 Gross household labour income is equal to the sum of labour earnings of all household members. The income tax and employee’s social security contributions are deducted from gross income, and social transfers such as social assistance, unemployment benefits, child benefits, and education benefits are added. We assume full take–up of social assistance if the eligibility criteria are fulfilled. Descriptive statistics for the selected sub–samples can be found in Table 1. In the wage offer equation an indicator for experience is used. Since we do not have information on the number of years a person has actually been working since she entered the labour market, potential experience is used. It is defined as the number of years since the person entered the labour market. That is age minus 15 years for a lowly educated person, age minus 19 years for a middle educated person, and age minus 23 years for a highly educated person. As this variable is highly correlated with age, we do not include age as a separate variable in the wage offer equation. Besides information from the eu–silc questionnaire, we also used external information on type specific unemployment, where types are differentiated according to age, sex and education level. This variable should serve as a proxy for job availability, and may help to identify the distinction between the contribution of opportunities and preference factors in 25 Version F5.5 was used. For more information about euromod, see Sutherland and Figari (2013) and https://www.iser.essex.ac.uk/euromod.

Table 2: Type specific unemployment rates (%)

Male

Female

Education level

Education level

Age group

Low Middle High Low Middle High 15 25 30 35 40 45 50 55 to to to to to to to to 24 29 34 39 44 49 54 64 years years years years years years years years 26.4 19.0 18.0 11.6 9.5 7.4 7.0 4.7 14.0 7.6 6.6 5.3 4.2 2.8 3.7 3.0 12.3 6.9 3.1 2.0 2.9 2.7 2.3 3.0 33.6 29.7 23.5 21.2 12.2 9.3 10.1 5.8 22.1 13.1 9.3 6.9 6.2 5.8 7.0 7.8 11.0 4.8 3.3 3.2 3.0 2.4 3.5

## 5.3 a

a The exact figure is lacking. The average across all education levels for that age class is taken.

Source: Eurostat Unemployment rates by sex, age and educational attainment level (%), Belgium 2007,

downloaded in October 2013.

variable

Table 3: Model specification

Preferences

Opportunities x V x q x g 2 x g 1 job offers hours wages

Regional dummies a

Education dummies b

Age

Group specific unemployment rate

Number of children

Gender

Potential experience a b yes yes yes no yes yes no yes yes yes yes no yes no no no no no no yes no no yes no no no yes yes

Bxl=Brussels, Fl=Flanders, Wal=Wallonia. Low, Middle, High.

the model. Table 2 shows the variation of this variable across the different types. Table 3 specifies the covariates that have been used in the different parts of the model.

5

Estimation results In Table 4 we report estimated parameters for the model. Next, we will investigate the impact of age on preference intensity for leisure (as compared to consumption), and opportunities.

Table 4: Estimation results: Preferences couples Procedure to sample choice set: importance sampling a with replacement and expected number of non–market alternatives equal to π 0 obs

Log likelihood -8427.3013

Description

Estimate 1.a) Consumption & leisure interaction M&F

Consumption Couples exponent

Consumption Couples constant

Leisure interaction M&F.in couples

Consumption single M exponent

Consumption single M constant

Consumption single F exponent

Consumption single F constant 1.b) Leisure coefficients males in couples

Leisure M in couples exponent

Leisure M in couples constant

Leisure M in couples ln(age)

Leisure M in couples ln(age) 2

Leisure M in couples ch03

Leisure M in couples ch36

Leisure M in couples ch69 Leisure M in couples dum region Walloon b

Leisure M in couples dum region Brussels Leisure M in couples dum education LOW c

Leisure M in couples dum education HIGH 1.c) Leisure coefficients females in couples

Leisure F in couples exponent

Leisure F in couples constant

Leisure F in couples ln(age)

Leisure F in couples ln(age) 2

Leisure F in couples ch03

Leisure F in couples ch36

Leisure F in couples ch69

Leisure F in couples dum region Walloon

Leisure F in couples dum region Brussels

Leisure F in couples dum education LOW

Leisure F in couples dum education HIGH a b c

Importance sampling is explained in Appendix II.

Flanders region is reference category.

Middle education level is reference category.

Standard Error t–value 0.579 4.763 0.128 0.261 4.517 -0.151 4.239 0.054 0.310 0.052 0.132 0.401 0.166 0.337 10.69 15.35 2.45 1.98 11.25 -0.91 12.58 -9.029 11.153 -5.890 0.821 -0.003 0.056 -0.011 0.106 0.131 -0.127 -0.070 0.707 5.533 3.023 0.418 0.047 0.051 0.047 0.055 0.090 0.067 0.048 -12.77 2.02 -1.95 1.97 -0.06 1.10 -0.24 1.93 1.45 -1.89 -1.47 -7.673 -7.855 4.599 -0.492 0.437 0.468 0.354 0.243 0.014 0.673 -0.713 0.552 11.558 6.583 0.932 0.162 0.171 0.172 0.145 0.208 0.293 0.162 -13.90 -0.68 0.70 -0.53 2.70 2.74 2.06 1.67 0.07 2.29 -4.42

Table 4: Estimation results ctd.: Preferences singles Procedure to sample choice set: importance sampling with replacement and expected number of non–market alternatives equal to π 0 obs

Description 1.d) Leisure coefficients single males

Leisure single M exponent

Leisure single M constant

Leisure single M ln(age)

Leisure single M ln(age) 2

Leisure single M ch36

Leisure single M ch69

Leisure single M dum region Walloon

Leisure single M dum region Brussels

Leisure single M dum education LOW

Leisure single M dum education HIGH 1.e) Leisure coefficients single females

Leisure single F exponent

Leisure single F constant

Leisure single F ln(age)

Leisure single F ln(age) 2

Leisure single F ch03

Leisure single F ch36

Leisure single F ch69

Leisure single F dum region Walloon

Leisure single F dum region Brussels

Leisure single F dum education LOW

Leisure single F dum education HIGH

Estimate

Standard Error t–value -6.169 -5.752 3.567 -0.403 -0.474 -0.906 0.835 0.211 -0.356 -0.507 1.172 17.286 9.722 1.350 0.903 0.634 0.395 0.303 0.321 0.290 -5.26 -0.33 0.37 -0.30 -0.52 -1.43 2.12 0.70 -1.11 -1.75 -9.328 22.335 -11.839 1.637 0.769 0.061 -0.054 0.121 -0.140 0.213 -0.569 1.259 12.697 6.938 0.959 0.420 0.158 0.133 0.136 0.122 0.247 0.186 -7.41 1.76 -1.71 1.71 1.83 0.39 -0.41 0.89 -1.14 0.86 -3.05 Table 4: Estimation results ctd.: Relative intensity of market alternatives and peaks hours Procedure to sample choice set: importance sampling with replacement and expected number of non–market alternatives equal to π 0 obs

Description

Estimate 2.a) Estimated coefficients opportunities & peaks males

Opportunity M constant

Opportunity M unemployment rate

Opportunity M dummy region Walloon

Opportunity M dummy region Brussels

Opportunity M dummy LOW education

Opportunity M dummy HIGH education

Opportunity M ln(age)

Opportunity M ln(age) 2

Peaks M <18.5,20.5> interval

Peaks M <29.5,30.5> interval

Peaks M <37.5,40.5> interval 2.b) Estimated coefficients opportunities & peaks females

Opportunity F constant

Opportunity F unemployment rate

Opportunity F dummy region Walloon

Opportunity F dummy region Brussels

Opportunity F dummy LOW education

Opportunity F dummy HIGH education

Opportunity F ln(age)

Opportunity F ln(age) 2

Peaks F <18.5,20.5> interval

Peaks F <29.5,30.5> interval

Peaks F <37.5,40.5> interval

Standard Error t–value -63.435 -0.491 -0.645 -1.351 -0.256 -0.103 35.200 -5.152 0.654 0.874 2.694 18.410 0.420 0.228 0.289 0.363 0.274 9.878 1.330 0.228 0.189 0.060 -3.45 -1.17 -2.83 -4.67 -0.71 -0.38 3.56 -3.87 2.86 4.61 45.21 -68.299 -0.568 -0.494 -0.851 0.285 0.212 38.169 -5.597 1.647 1.797 2.177 13.705 0.200 0.157 0.219 0.256 0.209 7.460 1.019 0.100 0.108 0.070 -4.98 -2.83 -3.14 -3.89 1.11 1.02 5.12 -5.49 16.45 16.63 31.20

Table 4: Estimation results ctd.: Wage distribution Procedure to sample choice set: importance sampling with replacement and expected number of non–market alternatives equal to π 0 obs

Description 3. Estimated coefficients wage equations 3.a) Wage equation males

Wage M σ

Wage M constant

Wage M potential experience

Wage M potential experience 2

Wage M low education

Wage M high education 3.b) Wage equation females

Wage F σ

Wage F constant

Wage F potential experience

Wage F potential experience 2

Wage F low education

Wage F high education 5.1

Estimate

Standard Error t–value 0.266 2.074 2.233 -2.844 -0.155 0.267 0.004 0.029 0.250 0.560 0.019 0.015 59.48 70.87 8.92 -5.08 -8.03 17.45 0.263 2.053 2.303 -3.273 -0.107 0.299 0.005 0.027 0.242 0.603 0.024 0.016 58.44 77.02 9.50 -5.43 -4.54 18.81

Preferences In order to investigate preferences for leisure, we will look at the shape of the indifference curves in consumption hours of labour time space for a job with given characteristics s. Of two preference orderings, the one exhibiting steeper indifference curves in this space, is said to exhibit more intense preferences for leisure. In order for that criterion to be applicable, it is necessary that these preference orderings satisfy the single crossing property: for every point (c, h) in the consumption hours of labour time space, the intersection of the indifference sets of both preferences should consist only of that point. A sufficient condition for single crossingness to be satisfied, is that the marginal rate of substitution between consumption and labour time is everywhere larger for the preference ordering exhibiting the more intense preference for leisure. The marginal rate of substitution between consumption and labour time for singles equals:

β 0 h,j x V · (T − h j) α h,j −1 /T α h,j , j = 1, 2, (34)

MRS c,h j = α −1 β c,j · c j c,j and for couples it is equal to:

MRS c,h j = α α −1 α α −1 α ) hi −1 β 0 h j x V,j · (T − h j) hj /T hj + β h 1 ,h 2 ((T −h i )/T (T − h j) hj /T hj α h i β c,g · c α c,g −1 , (35) i, j = 1, 2; i 6 = j.

Notice that the covariates influencing preferences affect the marginal rate of substitution 0 only through their influence on β h j x V. More specifically, in case β 0 h j x V increases in one of the covariates, the marginal rate of substitution in any point (c, h j) becomes higher for persons with a larger value on that variable. Everything else keeping constant, a person exhibiting a higher value on that covariate will have relatively steeper indifference curves. That is, she will exhibit a more intense preference for leisure. We illustrate this in Figures 2 and 3 for the case of age. For single males, age has a concave 0 parabolic impact on β h j x V with the top situated at 93 years. So, the marginal rate of substitution between consumption and labour time, and thus intensity of preferences for leisure, increases with age in the range of the values obtained for age in our data (16–64 years). This is illustrated by the black indifference curves in consumption labour time space in Figure 2: the dashed curve applies to a single male of 25 years, the steeper full curve to someone of 36 years old, and the steepest, dotted curve to someone of 58 years old. The curves become steeper with age.

0 For single females, the influence of age on β h j x V is convex parabolic, with the bottom at the age of 37 years. So, the indifference curves for consumption and labour time become flatter from the age of 16 until that of 37 years, and their slope starts increasing when becoming older than 37 years. This is illustrated by the gray curves in Figure 2. The dashed (age 25 years) and dotted curves (age 58 years) are both steeper than that of a single female at the age of 36 years. Preference intensity for leisure of single females is lowest at the age of 37 years. At first sight it seems that females have more intense preference for leisure than males (compare the grey and black curves in Figure 2), but note that the indifference curves of males and females exhibit a different curvature (determined by the exponents of consumption and leisure time, α c and α h, which are different for single males and females). Hence, the preference orderings of single males and females are not single crossing. A classification of intensity of preferences for leisure with respect to sex on the base of steepness of indifference curves can therefore not be made. For males, respectively females in couples the situation is reversed as compared to the case of singles (see Figure 3). Female spouses have increasing intensity of preference for leisure with age until the age of 107 years. For males the least intense preference for leisure is reached at the age of 36 years. Again, as the exponents of female’s and male’s leisure time in couples differ, the indifference curves of household consumption and each partner’s labour time are not single crossing, and cannot be compared to each other in terms of that criterion. As far as the significance of these effects is concerned, the precision of the estimates for age of females in couples and that of single males is poor. Those of single females and males in couples are reasonable.

Figure 2: Impact of age on steepness of indifference curves: singles 2200 1800 1600 1400 1200 60 58 56 54 52 50 48 46 44 42 40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 8 10 6 4 2 1000 0 disposable inocme in € per month 2000

Labour time: hours per week (grey=female -black=male) As for the impact of education, the intensity of preference for leisure relative to consumption of females is decreasing with education level, irrespective of whether they are single, or live in a couple. The effect of a lower education level is small though for singles, and not really significantly different from that of middle education. For males, the situation is again different, with both higher and lower educated men having less intense preference for leisure relative to consumption, irrespective whether they are single or live in couples. The precision of the estimate for lowly educated single men is poor, while the other education coefficients are moderately well estimated.

5.2

Opportunities Figure 4 represents the estimation of the wage offer distributions differentiated by sex and education level. Notice that this is a wage offer distribution. Simulated and observed wages are discussed in Section 6.1. The estimates of these distributions are very precise, and robust to different specifications for other parts of the model. From Figure 4 it can be seen that a higher education level shifts the wage offer distribution to the right, both for males and females. A similar effect is obtained for most of the range of potential experience. Table 5 reports e.g. the means of the wage offer distribution for 10 and 25 years of potential experience at different education levels, both for males and females. The mean of the wage offers increases with 1.7 to 2.7 euro over this range. However, as potential experience surpasses 35 years for females, and 39 years for men, the effect of additional Figure 3: Impact of age on steepness of indifference curves: couples 5500

Male (Age M 36 F 36)

Male (Age M 58 F 36)

Female (Age M 36 F 25)

Female (Age M 36 F 36)

Female (Age M 36 F 58) 4500 4000 3500 3000 2500 60 58 56 54 52 50 48 46 44 42 40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 2000 0

Disposable inocme in € per month 5000

Male (Age M 25 F 36)

Labour time: hours per week (grey=female -black=male) experience becomes slightly negative. Potentially, the variable takes up an age effect here. However, age and potential experience were by construction too much correlated to include them separately in this part of the model. The differences between males and females are small (dashed lines in Figure 4 apply to females, the full lines to males) as compared to the impact of the other covariates, and not always in the disadvantage of females. The latter is the case for persons with a middle education level.

Table 5: Mean of the wage offer distributions by sex, education and experience

Gross wage (euro per hour)

Education level Low Middle High

Male

Female

Years of potential experience 10 year 25 year 10 year 25 year 8.58 10.02 13.08 10.33 12.06 15.74 8.83 9.83 13.25 10.50 11.69 15.76 Figure 4: Estimated wage offer distributions differentiated by sex and education

Low education

Middle Education

High education 0 5 10 15 20 25 30 35

Gross Wage (Euro per hour)

Male

Female Figure 5 represents the distributions of offered labour time regimes by sex. 26 Again, these are not actual labour time regimes nor the ones chosen according to the model. The most salient observation is that this distribution is different for males and for females, the latter receiving more part time, and less full time job offers. The resulting frequency distribution of offered labour time regimes is represented in Table 6.

26 Admittedly, this part of the model is not non–parametrically identified (see Section 3.2). So, if one would like to explain this peak pattern by differences in preferences, we cannot tell this to be wrong on pure empirical grounds.

Figure 5: Estimated distribution of offered labour time regimes  1 exp   4 

Females

Males  1 exp   4  38  1 exp   3   1 exp   2   1 exp   3   1 exp   2   1  1 1-18.5 18.5-20.5  1  1 29.5-30.5 37.5-40.5 Labour time regime of the job offer (hours per week) 40.5-70  1  1 1-18.5 18.5-20.5  1  1 29.5-30.5 37.5-40.5 Labour time regime of the job offer (hours per week) 40.5-70 Table 6: Frequency table of offered labour time regimes by sex

Labour time regime (hours per week)

Male

Female 1.0–18.5 18.5–20.5 20.5–29.5 29.5–30.5 30.5–37.5 37.5–40.5 40.5–70.0 15.4% 3.4% 7.9% 2.1% 6.2% 39.0% 26.0% 16.5% 9.8% 8.5% 5.7% 6.6% 25.0% 28.0% Figure 6 and Table 7 report the impact of the covariates x q on the intensity of job offers (the π 1 –function). This variable measures the extent to which vacancies posted on the labour market are suited for the capacities a person is endowed with. As ruro is a static model, the total stock of capacities of a person is assumed to be fixed. As such, the estimated π 1 can be interpreted as the percentage of alternatives available to an individual which include a job offer. Grey curves in Figure 6 apply to females, black ones to males. The reference category (full lines) applies to a person living in Flanders region (Fl) with middle education level. Job offer intensity increases with age until the age of about 30 years, while it (quite drastically) decreases afterwards, a little more so for females than for males. Dashed and dotted curves reflect the impact of region when compared to the corresponding full lines. Job offer intensity is lower in Wallonia (Wal, dashed lines), and especially in Brussels capital region (Bxl, dotted lines). Notice however that regions are defined on the basis of the residence of respondents. So, these figures should be interpreted as reflecting the intensity of suitable job offers given the capacities of persons living in a certain region, irrespective of the region in which the job offer has been posted. Within the model, the sign of the effect of education on π 1 does not depend on the level of type–specific unemployment rate nor on the age of a person. We therefore report in Table 7 the impact of education by representing it at fixed values for age (30 years) and type specific unemployment rates (6%). Surprisingly, for males high education lowers job offer intensity, while for females low education raises job offer intensity. However, the effects are small, certainly in the light of the rather large standard errors of the estimated coefficients for these variables.

Relative number of market as compared tot total number of alternatives ( ˆ 1) Figure 6: Intensity of demand for individual capacities on the labour market in function of age, and differentiated by sex and region 80% 70% 60% 50% 40% 30% 20% 10% 0% 20 25 30 35 40 45 50 55 60 Age (curves evaluated at group specific unemployment rate=6%)

Male Fl

Male Wal

Male Bxl

Female Fl

Female Wal

Female Bxl Table 7: Intensity of demand for individual capacities on the labour market Evaluated at age=30 years, and type specific unemployment rate=6%

Male

Education level Low Middle High

Bxl

Fl

Female

Region

Wal

Bxl

Fl 38.2% 70.5% 55.6% 63.0% 80.0% 44.4% 75.5% 61.8% 56.2% 75.0% 41.8% 73.5% 59.3% 61.3% 78.8%

Wal 70.9% 64.7% 69.4% 65 6

Fit and behavioural response 6.1

Fit We now evaluate the fit of the estimates reported in Table 4, using the first simulation method discussed in Section 3.5. We first report results for couples (Figures 7–9), and then for singles (Figures 10–12). We compare the marginal distributions of ‘observed’ and simulated disposable income, which equals the value for consumption, c, in the model 27 (Figures 7 and 10), observed and simulated wages of males and females (Figures 8 and 11), and observed and simulated hours of work (Figures 9 and 12). The curves labelled by observed refer to observed values, while estimated refers to simulated values by the estimated model. Observed and simulated consumption and wages are compared by means of Gaussian kernel densities of both distributions. For wages, the distributions are conditional on being positive (labour market participants only). For the labour time regimes, we construct a histogram with bins coinciding with the peaks and troughs of the offered labour time regimes distributions. In this way, one can get a first assessment of the extent to which differences in offered labour time regimes are reflected in actual choices. We come back to this distinction between offered alternatives and actual choices while discussing Figure 12. Of course, even if the observed and simulated values would perfectly coincide, there might still occur large differences between simulated and observed values for each individual separately. The concordancy tables between observed and simulated labour time regimes are reported in Appendix III.

1. Couples. The mean estimated consumption within couples is 3083 e per month. Compare that with the observed mean of 3143 e per month reported in Table 1. The simulated distribution (black curve in Figure 7) slightly overestimates the number of households with lower incomes, at the expense of those with modal disposable incomes (compare the simulated values, represented by the black curve, with the observed values represented by the dashed grey one). The simulated (conditional) distribution of female wages (black curve on the rhs panel of Figure 8) is fatter at moderately low and moderately high wages, and less densely populated at modal incomes, as compared to the observed one (grey dashed curve on the rhs panel of Figure 8). Similarly, the simulated wage distribution of the males

27 Disposable income is actually not an observed value, but calculated from gross income by euromod.

(black line on the lhs panel of Figure 8) is more populated at lower wages than the observed one (dashed grey line on the lhs panel of Figure 8), at the expense of a smaller occurrence of modal wages. Figure 7: Densities simulated and observed disposable income for couples Curves labelled by estimated refer to the simulation obtained from the estimated model, while observed refers to observed values. Figure 8: Densities simulated and observed wages males (left) and females (right) in couples The number of non–participants in the labour market is overestimated. Compare thereto the filled grey (observed) and unfilled black bordered (simulated) left most spikes in both panels of Figure 9. Still, the number of cases in which none of both partners work, is underestimated (2.6% simulated as compared to 3.9% in the sample). The estimated peaks are in general somewhat underestimated, except for the number of females accepting a full time job, which is overestimated. More than full time jobs by males, and jobs between three quarter and full time are underestimated. For females the occurrence of jobs less than half time is overestimated.

Figure 9: Histograms labour time males (left) and females (right) in couples 2. Singles. Figures 10–12 represent the fit of the model for singles. The occurrence of moderately low consumption levels of single females is underestimated, while that of modal incomes is overestimated (rhs of Figure 10). Mean estimated consumption of females is 1575 e per month, to be compared with the observed value of 1567 e per month observed (see Table 1). For males these figures are respectively 1571 e per month fitted versus 1588 e per month observed. The empirical distribution is somewhat less skewed to the right than the fitted one. That is to a lesser extent also the case for the single females. The wage distribution of single females (rhs of Figure 11) is better fitted than that of males (lhs of Figure 11). The simulated distribution for females is somewhat more skewed to the right than the observed one. The simulated distribution of males has slightly fatter tails than the observed one. Labour market participation of single males (lhs of Figure 12) is overestimated, while that of single females is somewhat underestimated (rhs of Figure 12). The observed occurrence of half, three quarter and full time jobs for males is well fitted. Occurrence Figure 10: Densities disposable income single males (left) and single females (right) Figure 11: Densities wages single males (left) and females (right) of half time and full time jobs among single females is underestimated, that of three quarter jobs slightly overestimated. Finally, the simulated and observed distribution of labour time regimes for single males (lhs of Figure 12) illustrate that these should be distinguished from the availability of job offers specifying certain labour time regimes, as was mentioned at the beginning of this section. Estimates of the relative availability of half time and three quarter time jobs as compared to jobs between three quarter time and full time were represented by the corresponding peaks and through in Figure 5. So, despite our estimates reveal that half time and three quarter time jobs are more intensely offered than jobs between three quarter time and full time, single males do not choose, neither according to the data, nor according to the simulated behaviour, the former type of jobs more often than the latter.

Figure 12: Histograms labour time regimes single males (left) and single females (right) 6.2

Elasticities Table 8 reports the total reaction in terms of labour supply and the effect on participation to the labour market (extensive margin), following a shift of the density of the males’, respectively females’, wage offer distribution to the right by 10% (augmenting the estimated location parameter with ln 1.1). Additionally, we report intensive margins (effect on labour time conditional on participating in the base line, including the decline in labour time of those who were working in the baseline, but do not any more execute a job after the shift of the wage offer distribution). The variable ‘part in’ gives the percentage of entrants into the labour market, while ‘part out’ represents the percentage of leavers (due to cross effects in couples).

Table 8: Aggregate wage elasticities of labour supply Shift of female wage distribution Shift of male wage distribution

Couple

Single

Couple

Single

Female

Male

Female

Female

Male

Male

Total elasticity

## 0.5034 −0.1054

Intensive margin 0.1660 −0.1342

Part in 2.883% 0.275%

Part out 0.000% 1.098% 0.4786 0.0363 2.977% 0.000% −0.2200 0.3104 −0.2559 0.1331 0.412% 1.647% 1.510% 0.000% 0.2858 0.0280 2.004% 0.000% Compared to Marshallian elasticities in the literature estimated by static models using micro data, the total elasticity estimates produced here are rather large (Compare e.g. with the figures reported in Tables 6 and 7 of Keane, 2011). It should be stressed however that the figures reported here are conceptually of a different nature, in that actually obtained wages in the present model are the result of choosing the most attractive job offer according to the persons’ preferences. Therefore, a reaction to an exogenous change in that wage cannot be conceived of in the framework we used. What was, alternatively, done, is to shift the entire distribution of the wages included in the job offers, to the right. This cannot be considered the same as a change in an exogenously given wage. As the total elasticities reported here include the extensive margin, and are calculated as the proportional change in total labour time for the whole sub–sample, these should be better compared with macro elasticities. These are usually much larger compared to the figures obtained here. 28 Possibly the incorporation by the ruro model of frictions due to restrictions in the labour market opportunities an agent faces, might account for the lower values of the elasticities reported here, compared to the macro figures.

7 Age profiles of labour market participation: the contribution of preferences versus opportunities In the present section we want to explore to what extent the lower participation figures of and the decrease in the number of hours worked by older persons in the dataset (cf. the introduction) can, according to the model, be ascribed to an increasing intensity of preference for leisure, or rather to the lower intensity of job offers suitable to the capacities of older people. Thereto we performed two counterfactual simulation exercises, and compare them with the baseline simulation. In the first, we have changed the intensity of job offers π 1. Every individual in the sample got the maximal value for π 1 in function of age. Figure 6 showed that this corresponds to the age of 30. We thus partially equalise differences in opportunities due to age (hence the label ‘EO’) and calculate labour market choices as if all individuals would get the same number of suitable job offers as someone of age 30. In the second simulation, we leave opportunities unaffected, but modify preferences (labelled ‘EP’). Every individual now is endowed with preferences exhibiting the lowest intensity of preferences for leisure according to age, that is yielding the flattest indifference curves. For single females this is 37 years, and for males in couples 36 years. For single males and females in couples, the indifference curve is uniformly steepening with age in the relevant age range of the sample. In these cases we used 21 years as the ‘lowest’ age. Table 9 contains the results of these simulations. For both counterfactuals we calculated the 28 On the controversy about micro versus macro estimates, see amongst others Chetty et al. (2011), Chetty (2012), Fiorito and Zanella (2012), Keane and Rogerson (2012), Jäntti et al. (2015), and the references therein.

Table 9: Participation and avg. labour time by age class in baseline and counterfactuals Age 15<age<=30 30<age<=40 40<age<=50 50<age<=64 all

Category

Couples: males n obs.

part base part EO part EP hours base hours EO hours EP hours base hours EO hours EP 250 537 416 254 1457 participation 93.2% 94.2% 94.5% 81.9% 92.0% 94.4% 94.4% 97.1% 94.1% 95.1% 94.0% 94.6% 94.5% 81.1% 92.1% average hours of labour time per week – unconditional 35.1 38.0 38.2 32.6 36.6 35.4 38.1 39.8 36.8 37.9 36.3 38.8 39.1 33.6 37.6 average hours of labour time per week – conditional on part.

37.7 40.3

40.5 39.8

39.8 37.6

40.4 41.0

39.2 39.9

38.6 41.0

41.4 41.4

40.8

Category n obs.

part base part EO part EP hours base hours EO hours EP hours base hours EO hours EP

Couples: females 365 524 402 166 1457 participation 82.5% 85.1% 77.6% 49.4% 78.3% 86.0% 86.8% 88.8% 86.7% 87.2% 84.1% 88.5% 84.8% 63.9% 83.6% average hours of labour time per week – unconditional 27.6 26.0 25.0 16.1 25.0 28.2 26.4 28.3 26.3 27.4 30.1 30.2 31.6 23.5 29.8 average hours of labour time per week – conditional on part.

33.4 30.5

32.2 32.5

31.9 32.8

30.4 31.9

30.4 31.4

35.7 34.1

37.2 36.8

35.6 mean participation rate (denoted by ‘part’ in the table) and mean labour supply (denoted by ‘hours’ in the table) by age category. For hours we both calculated the unconditional mean, and the average hours conditional on participating. It seems as if ‘equalising’ differences in opportunities with respect to age, has in the first place an impact on the extensive margin, and much less so on the intensive margin of the number of hours worked. Overall, that is, the Table 9: Participation and avg. labour time by age class in baseline and counterfactuals ctd.

Age 15<age<=30 30<age<=40 40<age<=50 50<age<=64 all

Category

Singles: males n obs.

part base part EO part EP hours base hours EO hours EP hours base hours EO hours EP 106 135 119 89 449 participation 77.4% 91.1% 84.9% 65.2% 81.1% 78.3% 92.6% 90.8% 87.6% 87.8% 79.2% 92.6% 87.4% 71.9% 84.0% average hours of labour time per week – unconditional 29.5 35.3 33.1 24.7 31.3 30.3 35.7 35.3 32.8 33.7 30.6 37.3 35.2 28.8 33.5 average hours of labour time per week – conditional on part.

38.1 38.7

39.0 37.9

38.6 38.7

38.5 38.9

37.4 38.4

38.7 40.3

40.2 40.1

39.9

Category n obs.

part base part EO part EP hours base hours EO hours EP hours base hours EO hours EP

Singles: females 102 180 171 118 571 participation 63.7% 70.0% 73.1% 55.9% 66.9% 66.7% 73.3% 82.5% 90.7% 78.5% 66.7% 70.6% 74.3% 59.3% 68.7% average hours of labour time per week – unconditional 22.4 26.7 25.0 18.5 23.7 23.6 27.9 28.4 30.0 27.7 23.8 26.9 25.6 22.5 25.1 average hours of labour time per week – conditional on part.

35.1 38.1

34.2 33.2

35.5 35.3

38.0 34.4

33.0 35.3

35.7 38.2

34.4 38.0

36.5 four subgroups combined, the participation rate goes up with 6.9 percentage points (from 82.0% to 88.9%) in the ‘EO’–counterfactual. This effect is substantial for all subgroups, ranging from +3.1 percentage points (ppt) for males in couples, to +8.9 ppt for females in couples, and +6.7 and even +11.6 ppt for respectively single males and females. The breakdown of this effect according to age groups reveals that the rise in participation rates increases with age for singles, while for persons in couples it mirrors the concave shape of π 1 with respect to age. Equalising opportunities has no perceptible effect on the average number of hours worked, once we condition on participation. For the whole sample the effect is even slightly negative (the average number of hours decreases from 36.4 to 36.1). This is the result of a small decrease for all subgroups, save for males in couples where we find a small increase (from 39.8 to 39.9 hours worked per week). The second counterfactual shows that a decrease in the intensity of preferences for leisure both has an impact on the participation rate and on the number of hours worked. The overall participation rate increases with 2.6 ppt from 82.0% in the baseline to 84.6% under this ‘equalising preferences’ scenario. This is a much smaller increase than under the ‘EO’–scenario which yielded an increase of 6.9 ppt. Also in contrast with the previous ‘EO’–counterfactual, we do find an effect on the intensive margin now. On average, the number of hours conditional on participation increases with 1.9 (from

## 36.4 to 38.3), compared to the small decrease in the ‘EO’–scenario. This effect is largest for

females in couples (+3.7 hours). For males and females in couples and for single males the effect on hours is more uniform across age classes than in the ‘EO’–counterfactual.

2.5 5

utility counterfactual 7.5 10 12.5 15 17.5

Figure 13: Utility couples: baseline and counterfactual 2.5 5 7.5 10 12.5 utility baseline

## EO

15 17.5 baseline In the Figures 13–15, we report comparisons of utility obtained in the baseline with utility in the ‘equalised opportunity’ counterfactual. We do not reproduce a similar picture for the ‘EP’–counterfactual, since preferences have been changed thereto. Consequently, utility comparisons between baseline results and counterfactual for the same individual have no clear meaning. The black line in the figure is the 45 ◦ –line and reflects utility in the baseline. The dots are the utility levels obtained by the optimal choice in the ‘EO’–counterfactual, i.e. when job offer intensity would have reached the same value as when a person was thirty years old. Dots above the black line imply a gain in utility, dots below the black line, a loss. Since for all individuals, the job offer intensity in the counterfactual is at least as large as in the baseline, and for most individuals it is larger, one would at first sight expect that no one would be worse off in the counterfactual compared to the baseline. Yet, for all three sub– samples, we do find some cases in which the final choice is less preferred when confronted with an environment in which the opportunity set has been changed in the direction of more job offers. Hence, a bit surprisingly maybe, increasing the intensity of job offers does not imply a Pareto improvement. The explanation for having dots below the black line, is that increasing the job opportunities for persons with a low preference for jobs (elderly), might be harmful to these people. Indeed, since in this model, the job offer intensity is expressed as a relative number of market versus non–market opportunities, a higher job offer intensity, is tantamount to loosing some non–market opportunities. The latter might have been especially valuable for those with relatively more intense preference for leisure. It might be considered an unattractive property of the model that increasing the intensity of job offers is, by definition, mirrored by lowering the degree of availability of non–market opportunities. Indeed, why would I loose the opportunities to do what I liked most, when more jobs were offered to me? The worst that could happen is that none of these additional opportunities is more attractive than what I am currently doing, keeping the level of utility constant. Still, in this static model, the total stock of capacities an individual is endowed with, is considered as fixed. Increasing job offer intensity then means that capacities which were originally only apt for performing non–market activities, now become valuable on the market. In such a case, increasing job offer intensity is not a bless for all.

2.5 5

utility counterfactual 12.5 7.5 10 15 17.5 Figure 14: Utility single females: baseline and counterfactual 2.5 5 7.5 10 utility baseline

## EO

12.5 15

17.5 baseline

2.5 5

utility counterfactual 7.5 10 12.5 15 17.5 Figure 15: Utility single males: baseline and counterfactual 2.5 5 7.5 10 utility baseline

## EO

12.5 baseline

15 17.5 8

## Conclusion

This paper has tried to shed some light on the lower labour market participation of the elderly by exploiting a rich structural model of labour supply, the so–called ruro model. Contrary to standard random utility models of labour supply, this model adds substantially more heterogeneity in individual opportunities by integrating an individual specific job offer intensity as an explanatory variable for observed behaviour. We have estimated this model on Belgian eu–silc data of 2007, which allowed us to quantify to what extent lower labour market participation is due to changing preferences (executing a job might become less enjoyable with age) or differences in opportunities (elderly getting less, or less attractive job offers). The estimates indicate that the relation between job offer intensity and age has an inverted U–shape with top at about 30 years. Job offer intensity after that age decreases sharply, so that the avaialbility of suitable jobs after the age of 50 is lower than that for youngsters. This effect is a bit more outspoken for females than for males. We also found important regional variation in the job offer intensity, being lower for persons living in Wallonia, and especially in the Brussels capital region, as compared to those living in Flanders. As for the distribution of wage offers, we found, unsurprisingly, that, on average, higher wages were offered to persons with higher education level. The differences between males and females, however, were small. The effect of age on preferences was less clear–cut than the effect on opportunities. We found two cases where the intensity of preference for leisure, or the distaste for paid work, monotonically increases with age in the relevant age range (i.e. 16 to 64 years for our data): for females in couples, and for single males. For both these groups, indifference curves in the labour time versus consumption space, become steeper with age. For the other two subgroups, i.e. single females and males in couples, the pattern is non–monotonic. For single females and males in couples, preference intensity for leisure is lowest at the age of respectively 37 and 36 years. Their indifference curves become flatter from the age of 16 until that of 37 (respectively 36) years, and their slope starts increasing when becoming older than 37 (respectively 36) years. To get an idea of the relative importance of both forms of heterogeneity (impact of age via preferences and opportunities), we conducted a simulation of two counterfactuals. First, we removed part of heterogeneity in opportunities by giving all individuals the maximal job offer intensity in terms of age (that of a 30 years old person). Second, we removed part of the heterogeneity in preferences by endowing all individuals with preferences at the subgroup specific age at which the intensity of preference for leisure was at its minimum. Our tentative conclusion from a comparison of labour market behaviour in these two counterfactuals with the baseline situation, is that opportunities which decline with age are at least as an important factor in explaining low participation rates for the elderly, as is the fact that preference change with growing older. More specifically, the effect of opportunities seems to work primarily through the extensive margin, whereas the effect of preferences is more outspoken in the intensive than in the extensive margin. From a policy point of view this might be relevant. We feel that the rich specification of the ruro model is promising. Therefore, we think we should try to estimate with data which allow for a better identification of the indivual job offer intensity (π 1 ). This might e.g. be obtained by re–estimating the model with more exogenous variation in job availability, either by e.g. using cross-country variation or variation through time. Needless to say that the corresponding work to produce choice sets for the estimation in this framework might be labour intensive (one needs a cross– country microsimulation model and/or a microsimulation model which can model the gross– net trajectory for several years). Secondly, structural models like the one presented in this paper are obvious candidates as suppliers of essential information for normative analyses, based on — in this case, revealed — preferences. After careful scrutiny of how sensitive estimated preferences are to the inclusion and specific specification of additional constraints from the demand side of the labour market, we plan to construct welfare measures in line with our first attempt in Decoster and Haan (2015). This is especially important when trying to make welfare comparisons between countries or at different moments in time, when the respective populations to be compared do not necessarily have the same preferences.

## References

[1] Aaberge R. & U. Colombino (2013), “Using a microeconometric model of household labour supply to design optimal income taxes,” Scandinavian Journal of Economics, vol. 115(2), 449–475.

[2] Aaberge R. & U. Colombino (2014), “Labour supply models,” in: C. O’Donoghue (ed.) Handbook of Microsimulation Modelling. Contributions to economic Analysis vol. 293. Emerald Group Publishing Ltd.: Bingley, 167–221.

[3] Aaberge R., U. Colombino, E. Holmøy, B. Strøm & T. Wennemo (2007), “Population ageing and fiscal sustainability: Integrating Detailed Labour Supply models with CGE Models,” in: A. Harding & A. Gupta (eds.), Modelling our Future: Population Ageing, Social Security and Taxation, Elsevier: Amsterdam, 259–290.

[4] Aaberge R., U. Colombino, & S. Strøm (1999), “Labour supply in Italy: an empirical analysis of joint decisions, with taxes and quantity constraints,” Journal of Applied Econometrics, vol. 14(4), 403–422.

[5] Aaberge R., U. Colombino, & S. Strøm (2000), “Labor supply responses and welfare effects from replacing current tax rules by a flat tax: Empirical evidence from Italy, Norway and Sweden,” Journal of Population Economics, vol. 13(4), 595–625.

[6] Aaberge R., U. Colombino, & T. Wennemo (2009), “Evaluating alternative representations of the choice sets in models of labour supply,” Journal of Economic Surveys, vol. 23(3), 586–612.

[7] Aaberge R., J.K. Dagsvik & S. Strøm (1995), “Labor supply responses and welfare effects of tax reforms,” Scandinavian Journal of Economics, vol. 97(4), 635–659.

[8] Aaberge R. & L. Flood (2013) “U.S. versus Sweden. The effect of alternative in–work tax credit policies on labour supply of single mothers,” Statistics Norway, Discussion paper no. 761.

[9] Altonji J.G. & C.H. Paxson (1982), “Labor supply preferences, hours constraints, and hours–wage trade–offs,” Journal of Labor Economics, vol. 6(2), 254–276.

[10] Altonji J.G. & C.H. Paxson (1992), “Labor supply, hours constraints, and job mobility,”

Journal of Human Resources, vol. 27(2), 256–278.

[11] Beffy M., R. Blundell, A. Bozio, G. Laroque & M. To (2016) “Labour supply and taxation with restricted choices,” ifs wp w15/02.

[12] Belloni M. (2008) “The option value model in retirement literature: the trade–off between computational complexity and predictive validity,” enepri Research Report No. 50, aim–WP6.

[13] Belloni M. & R. Alessie (2009) “The importance of financial incentives on retirement choices: new evidence for Italy,” Labour Economics, vol. 16(5), 578–588.

[14] Belloni M. & R. Alessie (2013) “Retirement choices in Italy: What an option value model tells us,” Oxford Bulletin of Economics and Statistics, vol. 75(4), 499–527.

[15] Ben–Akiva M. & S.R. Lerman (1985), Discrete Choice Analysis, mit press: Cambridge, ma, 261–269 (Ch. 9.3).

[16] Berkovec J. & S. Stern (1991) “Job exit behavior of older men,” Econometrica, vol. 59(1), 189–210.

[17] Bloemen H.G. (2000), “A model of labour supply with job offer restrictions,” Labour

Economics, vol. 7(3), 297–312.

[18] Bloemen H.G. (2008), “Job search, hours restrictions, and desired hours of work,”

Journal of Labor Economics, vol. 26(1), 137–179.

[19] Buyse T., F. Heylen & R. Van de Kerckhove (2013), “Pension reform, employment by age and long–run growth,” Journal of Population Economics, 26(2), 769–809.

[20] Chetty R. (2012) “Bounds on elasticities with optimization frictions: a synthesis of micro and macro evidence on labor supply,” Econometrica, vol. 80(3), 969–1018.

[21] Chetty R., A. Guren, D. Manoli & A. Weber (2011) “Are micro and macro labor supply elasticities consistent? A review of evidence on the intensive and extensive margins,” American Economic Review, vol. 101(3), 471–475.

[22] Creedy J. & G. Kalb (2005) “Discrete hours labour supply modelling: Specification, estimation and simulation,” Journal of Economic Surveys, vol. 19(5), 697–734.

[23] Dagsvik J.K. (1994) “Discrete and continuous choice, max–stable processes, and independence from irrelevant attributes,” Econometrica, vol. 62(5), 1179–1205.

[24] Dagsvik K.J. (2013) “Justification of functional form assumptions in structural models:

a correction,” Theory and Decision 75(2), 79–83.

[25] Dagsvik K.J. & S. Røine Hoff (2011), “Justification of functional form assumptions in structural models: applications and testing of qualitative measurement axioms,” Theory and Decision 70(2), 215–254.

[26] Dagsvik J.K. & Z. Jia (2014) “Labor supply as a choice among latent jobs: unobserved heterogeneity and identification,” Journal of Applied Econometrics, first online 6 Jan. 2015, DOI: 10.1002/jae.2428.

[27] Dagsvik J.K., Z. Jia, T. Kornstad & T.O. Thoresen (2014) “Theoretical and practical arguments for modeling labor supply as a choice among latent jobs,” Journal of Economic Surveys, vol. 28(1), 134–151.

[28] Dagsvik J.K., M. Locatelli & S. Strøm (2006) “Simulating labor supply behaviour when workers have preferences over job opportunities and face non–linear budget constraints,” Centre for Household, Income, Lambour and Demographic Economics (child, Torino, Italy)), Discussion paper no. 01/2006.

[29] Dagsvik J.K., M. Locatelli & S. Strøm (2007) “Evaluation of tax reforms when workers have preferences over job attributes and face latent choice restrictions,” Centre for Household, Income, Labour and Demographic Economics (child, Torino, Italy)), Discussion paper no. 13/2007.

[30] Dagsvik J.K. & S. Strøm (1992) “Labour supply with non–convex budget sets, hours restriction and non–pecuniary job attributes,” Central Bureau of Statistics Norway, Discussion Paper No 76.

[31] Dagsvik J.K. & S. Strøm (2003) “Analyzing labor supply behavior with latent job opportunity sets and institutional choice constraints,” Statistics Norway, Research Department, Discussion Paper No 344.

[32] Dagsvik J.K. & S. Strøm (2004) “Sectoral labour supply, choice restrictions and functional form,” Statistics Norway, Discussion paper no. 388.

[33] Dagsvik J.K. & S. Strøm (2006) “Sectoral labour supply, choice restrictions and functional form,” Journal of Applied Econometrics, vol. 21(6), 803–826.

[34] Decoster A. & P. Haan (2015) “Empirical welfare analysis with preference heterogeneity,”

International Tax and Public Finance, vol.22(2), 224–251.

[35] Dickens W.T. & S.J. Lundberg (1993) “Hours restrictions and labor supply,” International Economic Review, vol. 34(1), 169–192.

[36] Feldstein M. (1974) “Social security, induced retirement, and aggregate capital accumulation,” The Journal of Political Economy, vol. 82(5), 905–926.

[37] Fiorito R. & G. Zanella (2012) “The anatomy of the aggregate labor supply elasticities,”

Review of Economic Dynamics, vol. 15(2), 171–187.

[38] Gruber J. & D.A. Wise (eds.) (1999), Social Security and Retirement around the World, nber Book Series – International Social Security, University of Chicago Press: Chicago.

[39] Ham J.C. & K.T. Reilly (2002) “Testing intertemporal substitution, implicit contracts, and hours restriction models of the labor market using micro data,” American Economic Review, vol. 92(4), 905–927.

[40] Hausman J.A. (1985) “Taxes and labor supply,” in: A.J. Auerbach & M. Feldstein (eds.), Handbook of Public Economics, Elsevier Science Publishers B.V. (North-Holland): Amsterdam, 213–263.

[41] Jäntti M., J. Pirttilä & H. Selin (2015) “Estimating labour supply elasticities based on cross–country micro data: A bridge between micro and macro estimates?” Journal of Public Economics, vol.127, 87–99.

[42] Keane M.P. (2011) “Labor supply and taxes: a survey,” Journal of Economic Literature, vol.1 49(4), 961–1075.

[43] Keane M. & R. Rogerson (2012) “Micro and macro labor supply elasticities: a reassessment of conventional wisdom,” Journal of Economic Literature, vol. 50(2), 464–476.

[44] Lefebvre M. & K. Orsini (2012) “A structural model for early exit of older men in

Belgium,” Empirical Economics, vol. 43(1), 379–398.

[45] Lemp J.D. & K.M.Kockelman (2012), “Strategic sampling for large choice sets in estimation and application,” Transportation Research Part A 46(3), 602–613.

[46] Löffler M., A. Peichl and S. Siegloch (2014) “Structural labor supply models and wage exogeneity,” iza dp No.8281 Forschungsinstitut zur Zukunft der Arbeit: Bonn.

[47] Luce D.R. (1959, repr. 2005) Individual Choice Behavior: A Theoretical Analysis, Dover

Publications Inc.: Mineola, New York.

[48] Lumsdaine R.L., J.H. Stock & A.D. Wise (1992) “Three models of retirement: computational complexity versus predictive validity,” in: D.A. Wise (ed.) Topics in the Economics of Aging, University of Chicago Press: Chicago, 21–60.

[49] Maes M. (2011) “Will the dismantlement of early retirement schemes increase older unemployment? A competing–risk analysis for Belgium,” Labour, vol. 25(2), 252–267.

[50] Maes M. (2012) “Financial and distributional implications of early retirement in Belgium,” Reflets et perspectives de la vie économique, vol. 51(3), 29–41.

[51] McFadden D. (1973) “Conditional logit analysis of qualitative choice behavior,” in:

P. Zarembka (ed.), Frontiers in Econometrics, Academic Press: New York, 1973, 105– 142.

[52] McFadden D. (1978), “Modelling the choice of residential location,” in A. Karlqvist,

## L. Lundqvist, F. Snickars & J. Weibull (eds.), Spatial Interaction Theory and Planning

Models, North-Holland: Amsterdam, 75–96.

[53] Moffitt R. (1984) “The estimation of a joint wage–hours labor supply model,” Journal of Labor Economics, Vol. 2(4), 550–566.

[54] Müller K.–U., M. Neumann & K. Wrohlich (2015) “Labor supply under participation and hours constraints. An extended structural model for policy evaluations,”, mimeo.

[55] Rust J. (1989) “A dynamic programming model of retirement behavior,” in:

D.A. Wise (ed.) The Economics of Aging, University of Chicago Press: Chicago, 359– 404.

[56] Rust J. & C. Phelan (1997) “How social security and medicare affect retirement behavior in a world of incomplete markets,” Econometrica, vol. 65(4), 781–831.

[57] Stock J.H. & D.A. Wise (1990) “Pensions, the option value of work, and retirement,”

Econometrica, vol. 58(5), 1151–1180.

[58] Sutherland H. & F. Figari (2013) “euromod: the European Union tax–benefit microsimulation model,” International Journal of Microsimulation, vol. 6(1), 4–26.

[59] Tummers M.P. & I. Woittiez (1991) “A simultaneous wage and labor supply model with hours restrictions,” Journal of Human Resources, vol. 26 (3), 393–423.

[60] Train K.E. (2009, 2 nd ed.), Discrete Choice Methods with Simulation, Cambridge University Press: Cambridge, pp.64–66.

[61] Van Soest A. (1995) “Structural models of family labor supply: a discrete choice approach,” The Journal of Human Resources, vol. 30(1), 63–88.

[62] Van Soest A., M. Das & X. Gong (2002) “A structural labour supply model with flexible preferences,” Journal of Econometrics, vol. 107(1–2), 345–374.

[63] Van Soest A., I. Woittiez & A. Kapteyn (1990) “Labor supply, income taxes, and hours restrictions in the Netherlands,” Journal of Human Resources, vol. 25(3), Special Issue on Taxation and Labor Supply in Industrial Countries, 517–558.

Appendices

Appendix I Poisson processes Originally, a Poisson process is a stochastic process describing the probability of the number of occurrences of a particular event during a certain time spell. More specifically, a Poisson process assumes that distribution of the time between each pair of consecutive events is independent from the moment at which the first of these two events occurred, or from any other event in the past, and that these inter–arrival times are exponentially distributed with parameter λ (the exponential distribution function of a stochastic variable x is 1 − exp (−λx) /λ). This parameter λ measures the intensity with which such events occur. Under these assumptions, the probability that a certain event occurs n times within a given unit of time, with n ∈ {0, 1, 2.. .}, equals:

λ n exp [−λ] , n!

where N (t) is the number of events that occurred in total after t units of time. P (N (t + 1) − N (t) = n) = (a. 1) Equation (a. 1) is a Poisson distribution with intensity parameter λ. More generally, for a Poisson process, it holds that the number of events occurring within an interval of length τ is Poisson distributed with parameter λτ:

(λτ) n exp [−λτ] .

(a. 2) n!

In this standard Poisson process, λ · τ is the expected number of events to occur within a time P (N (t + τ) − N (t) = n) = interval of length τ. A Poisson process is inhomogeneous if the intensity parameter depends on the moment of measurement, λ (t) say. In that case, the probability that n events occur within a time interval [t, t + τ ], equals: P (N (t + τ) − N (t) = n) = where Λ ([t, t + τ ]) :=

R t+τ t (Λ ([t, t + τ ])) n exp [−Λ ([t, t + τ ])] , n!

(a. 3) λ (s) d s, is the expected number of times the event occurs in the interval [t, t + τ ]. A Poisson process can also be spatial. Let an event be described as a point in an m–dimensional space. A spatial Poisson process determines the probability that n events occur within a subset of

## R

the m–dimensional space. Let, for example, B be a subset of R m with volume ρ (B) := x∈B d x = 1. Furthermore, let N (B) be the number of events occurring in B. If the occurrence of such events obeys a spatial Poisson process with intensity parameter λ, then the probability that there occur n events in B, follows a Poisson distribution:

λ n exp [−λ] .

(a. 4) n!

More generally, for such a spatial Poisson the number of events to occur within a set B with P (N (B) = n) = volume ρ (B) not necessarily equal to one, is Poisson distributed with parameter λρ (B):

P (N (B) = n) = (λρ (B)) n exp [−λρ (B)] .

n!

(a. 5) Again, λρ (B) is the expected number of events to occur in set B. Such a spatial Poisson process is said to be inhomogeneous if the intensity of occurrence depends on the points x ∈ R m. To describe that process, assume that there exists a measure ρ defined on (measurable) subsets of the space R m and let the intensity function λ (x) be integrable with respect to that measure. The probability that there occur n events in a measurable subset B of R m, is then:

P (N (B) = n) = where Λ (B) := (Λ (B)) n exp [−Λ (B)] ,.

n!

## R

x∈B (a. 6) λ (x) d ρ (x), is equal to the expected number of events in the set B.

Job offers and the availability of non–market activities each are described by an inhomogeneous spatial Poison process in ruro models. These processes are independent. However, given that the ruro model is static, the stock of capacities an individual is endowed with, is assumed to be fixed. If demand for these capacities (by means of job offers) intensifies, a relatively smaller amount of these capacities serves exclusively for executing non–market activities.

Appendix II Sampling choice sets The McFadden approach. The method of sampling choice sets for estimating discrete choice models was originally developed by McFadden (1978, section 7) in order to handle cases where the number of choices is so large that the true likelihood function would become intractable. A summary of this procedure can be found in Train (2009, pp. 64–66). Assume that the true choice set, C, consists of a very large, but still discrete, number of alternatives, indexed by j, k ∈ C := {1, 2,..., C}, where C is a natural number. Assume also that the choice behaviour can be reflected by a multinomial logit model. The systematic part of the utility of an alternative j ∈ C is denoted by V j. That is, V j is a shorthand for a function of a set of covariates whose values change across alternatives, say x j, and a set of parameters to be estimated, β say. Total utility derived from j ∈ C is:

U j := V j + j, (a. 7) where j is a to the researcher unobserved factor determining that person’s preferences. Assuming that this term is drawn from an Extreme Value Type I distribution, which has distribution function exp [− exp (− j )], the probability that this person will opt for alternative j from the set of available alternatives C, P j,C say, is equal to:

P j,C = P exp (V j) .

k∈C exp (V k) (a. 8) This is a more general version of equation (20) in the main text. For some reason, it might be impossible to collect information on all the alternatives in C that are available to a particular individual (e.g. because this set is too large). Therefore the researcher might sample a set of alternatives D from C. The observed alternative is included in D, since it is observed, and thus, by definition, must have been one of the possible alternatives from which the person has chosen. One might for example partition the set C into M subsets (with M a natural number such that M < C). Each member of the partition is denoted by K m (m ∈ M := {1, 2,..., M }). One can then sample the chosen alternative j with certainty from the subset that contains the chosen alternative, K m: j ∈ K m, and sample at random an alternative from the remaining subsets, K m: j ∈ / K m.

Sampling a choice set induces a probability to select a subset D from the true choice set C, given that the person is observed to have selected j. This probability will be denoted by π (D |j; C ). For example, when using the sampling procedure discussed in the previous paragraph, and letting K m be the Q number of elements in the subset K m of the partition (for each m ∈ M), then π (D |j; C) = K n / M m=1 K m, where n is the index of the subset to which the chosen alternative j belongs, n := m ∈ M: j ∈ K m.

By sampling a choice set D, the researcher can only retrieve some information on factors leading a person to choose alternative j from D rather than from C, while she is actually interested in the latter. Denote the probability to choose j from D by P j,D. Train (2009) shows that:

P j,D = P exp (V j) π (D |j; C) k∈D exp (V k) π (D |k; C) .

(a. 9) The essence of the proof lays in the observation that the probability to sample a set D from C, and observing an agent to choose j, say θ C (D, j), is equal to π (D |j; C) · P j,C. Similarly, by reversing the conditioning from j to D, this probability to sample a set D from C, and observing an agent to choose j, θ C (D, j), is also equal to P j,D ·Π (D), where Π (D) is the unconditional probability to select

## P

a subset D from C according to the sampling procedure, that is Π (D) := k∈C π (D |k; C) · P k,C =

## P

k∈D π (D |k; C) · P k,C. The equality follows from observing that the conditional probability to select a set D, given the observed choice is k, while k does not belong to the sampled set D, is zero, by definition of the allowed sampling procedures: π (D |k; C) = 0 if k ∈ / D. Equating both expressions for θ C (D, j) and solving for P j,D gives equation (a. 9 ). McFadden (1978) has shown that the parameters β of the utility function, V j := v (β; x j ), can be estimated consistently by maximising the sampled log–likelihood function L (β; X) based on the corrected probabilities (a. 9 ), where X is a data set containing for each observation t values of choice k’s attributes, x t,k say, for all k ∈ D. Let j (t) denote observation t 0 s observed choice from the set C. Then, this sampled log–likelihood function becomes:

 

## X

## X

π (D t |k; C) ,

L (β; X) := − ln  exp v (β; x t,k) − v β; x t,j(t) π (D t |j (t); C) t (a. 10) k∈D t McFadden’s result relies upon imposing the positive conditioning property upon the choice set sampling probabilities π (D |k; C ), which reads as: for all j, k ∈ D: if π (D |j; C) > 0 then π (D |k; C) > 0.

(a. 11) A stronger condition which is also sufficient for consistency (and which implies a further simplification for the sampled likelihood function) is the uniform conditioning property: ∀ j, k ∈ D: π (D |j; C) = π (D |k; C).

(a. 12) In that case the correction factor, π (D t |k; C) /π (D t |j (t); C ), in the sampled log–likelihood function (a. 10 ), drops out. One could wonder why then the uniform conditioning property has not been unanimously followed, for reasons of simplicity. Note however that this would result in sampling alternatives that for some, or all, agents are relatively unlikely to be chosen. Sampling such alternatives would yield poor information on the factors explaining a person’s actual choice. This method is therefore generally less efficient (yielding larger standard errors for the estimates of β) than sampling alternatives on the basis of some prior knowledge or evidence on the alternatives having been chosen, or likely to be chosen. This is the idea behind importance sampling, which will be discussed later.

The Aaberge–Colombino–Wennemo approach. Aaberge, Colombino and Wennemo (2009) propose a similar sampling procedure for estimating the ruro model.

In abstracto, the individual contributions to the likelihood function of the ruro model equal (compare with equation (19) of the main text):

Q j,C;p = R exp (V j) p (j) , k∈C exp (V k) p (k) d ρ (k) (a. 13) where p (k) is a measure for the intensity with which alternative k is rendered available to the individual decision maker, and j is the chosen alternative. The set of alternatives C might be continuous, and ρ (·) is a measure defined over the space of alternatives. So, p is a shorthand for a function of a set of explanatory variables whose value may be varying across alternatives, say x p,j (j ∈ C), and a set of parameters to be estimated, δ. In practice, it might be impossible to observe or use the whole set of alternatives C in the estimation, and a sample D is drawn. Assume the probability to sample an alternative k from C to be equal to φ (k). Then, the correction proposed by Aaberge, Colombino, and Wennemo (2009, see equation (9), p.593) is equal to: b j,D;p,φ = P exp (V j) p (j) /φ (j) .

## Q

k∈D exp (V k) p (k) /φ (k) (a. 14) The intuitive rationale is that estimates of exp (V k) p (k) will be affected by the sampling procedure. More specifically, the term referring to an alternative k in a person’s simulated contribution to the likelihood function, that would be sampled relatively more often than the intensity with which it is really rendered available to that person, will get too big a weight. Therefore, its true value, exp (V k) p (k), will be underestimated. Dividing true by its sampling weight, φ (k), would correct for that.

Relating both approaches. The connection between both approaches seems rather vague at first sight. The formal connection between both, the McFadden (1978) approach and the Aaberge–Colombino–Wennemo (2009) approach, is explained in Ben–Akiva and Lerman (1985). Recall that the probability to choose an alternative j from the sampled choice set D, P j,D, can be written as:

P j,D = θ C (D, j) .

## Π (D)

(a. 15) Now, in the model of Aaberge, Colombino and Strøm (1999), θ C (D, j) is equal to π (D |j; C) Q j,C;p (see equation a. 13 ). The unconditional probability to select a subset D from C according to the

## P

## P

sampling procedure, Π (D), equals k∈C π (D |k; C) · Q k,C;p = k∈D π (D |k; C) · Q k,C;p. Using equation (a. 13 ), this results in:

P j,D = exp (V j) p (j) π (D |j; C) θ C (D, j) .

## = P

## Π (D)

k∈D exp (V k) p (k) π (D |k; C) (a. 16) This is the equivalent for the ruro model of equation (a. 9) in a simple logit model. One class of sampling choice sets is importance sampling. Each alternative j from the choice set C gets a (prior) probability weight φ (j) to be sampled from C. So, the probability to sample the

## Q

## Q

set D from the set of all alternatives C, Π (D), is equal to φ (j) (1 − φ (j)). 29 One always j∈D j ∈D / includes the chosen alternative according to the data, as an element in the sampled choice set. This implies that the probability to sample D, given the chosen alternative is k, denoted earlier

## Q

## Q

## Q

## Q

as π (D |k, C ), equals φ (j) (1 − φ (j)) /φ (k) = φ (j) (1 − φ (j)) = Π (D) /φ (k).

j∈D j ∈D / j∈D:

j6 = k j ∈D /

So, equation (a. 16) reduces to:

P j,D = P exp (V j) p (j) Π (D) /φ (j) k∈D exp (V k) p (k) Π (D) /φ (k)

## = P

exp (V j) p (j) /φ (j) , (a. 17) k∈D exp (V k) p (k) /φ (k) which is exactly equation (a. 14) we were looking for.

Importance sampling for the ruro model. There are several methods of importance sampling. Ben–Akiva and Lerman (1985, 265–267) mention for example three variants. They all however result in the same expression for the corrected likelihood (a. 14 ). In the ruro model the set of possible alternatives consists of the union of, on the one hand, the so– called non–market alternatives (that is, possible sets of activities when not accepting any possible job offer), and, on the other hand, the set of possible packages of a wage, w, and a number of hours (per week) to be worked, say h, both as specified in a particular job offer. A specific wage–labour time regime is thus denoted by (w, h). As far as it concerns a job offer, it is assumed that with w > 0 and H max > h ≥ H min, with H min > 0. Then, non–market alternatives are denoted as wage labour time regime packages (w, h), such that (w, h) ≡ (0, 0). So, we have a mixed distribution of the discrete variable (0, 0) that indicates the option not to accept any job offer, and the bi–dimensional continuous variable (w, h) ∈ R ++ × [H min, H max [. 30 Furthermore, in the ruro model, the probability (density) p (k) specified in the previous section, is a measure for the intensity with which an alternative k characterised by a wage–labour time bundle (w k, h k ), is rendered available to the agent. In the sequel, the log normal density with 31 location parameter µ 1, and scale parameter σ, of a random variable z, is abbreviated by n (z; µ 1, σ).

That is n (z; µ 1, σ) := 1 √ zσ 2π 1) exp − (ln z−µ 2 2σ 2 if z > 0, and it equals zero otherwise. Then, the probability (density) p (k) for the ruro model in the main text can be written as (see Section 3.3): 29 See Ben–Akiva and Lerman (1985, p.265) on independent importance sampling. Recall that the realisation of the stochastic process that describes the intensity with which suitable job offers are rendered available to an individual, results in a discrete set of job offers, each specifying a combination of a wage offer and a labour time regime, (w, h) ∈ R ++ × [H min, H max [. 31 That is the concrete specification we assumed for the wage offer distribution function g 1, as notified in

Section 3.3.

30   π 0 η q; x q if (w k, h k) = (0, 0),    0   1 − π 0 η q; x q n w k; δ g 1 x g 1, σ γ 1 exp (γ k)   if (w k, h k) ∈ R ++ × [H k−1 ,H k−1 [, for k = 2,..., K + 1, p (k) =   0  , σ γ 1 if (w k, h k) ∈ R ++ × ∪ [H k−1, H k [, 1 − π η ;

x n w ;

δ x 0 q g k  q g 1 1  k=1,...,K+1    0 else, (a. 18) where H 0 := H min < H 1 <H 1 <... < H k <H k <... < H K <H K < H K+1 := H max. These values define the bins of a piecewise uniform distribution for labour time regimes. 32 The intensity with which suitable job offers are rendered available to an individual with characteristics x q, is specified −1 33 by 1 − π 0 η q; x q := 1 + exp −η 0 q x q . The parameters (δ q, δ g 1, σ, γ 1, γ 2,..., γ K+1) form together the parameter vector δ, determining the intensity with which alternatives are rendered available to individuals with characteristics (x q, x g 1 ), as discussed in Section 2.3, and which has to be estimated jointly with the preference parameters β. 34 Where necessary, the dependency of p (k) on δ will explicitly referred to in the notation as follows: p (δ; x q, x g 1, w k, h k) := p (k). The suitable job offers rendered available to an individual are however not observed. But, the econometrician can revert to the method of sampling a choice set, and constructing a sampled likelihood, in order to try to estimate the relevant parameters of the model, β and δ. The alternatives to be sampled are wage labour time regime combinations. The sampling methods described here make a fixed number of draws n s form the set {(0, 0)}∪R ++ × [H min, H max [. With an a priori fixed probability, say π 0 obs, a draw picks a non–market alternative (that is, (w, h) = (0, 0)). Else, a wage–labour time regime is fixed by independently sampling the wage from a log normal distribution with a priori determined location and scale parameters, µ and ς say, and the labour time regime from a uniform distribution on the interval [H min, H max [. The probability (density, in case (w, h) > 0) to draw a wage labour time bundle (w, h), denoted by P (w, h), is thus 35:

 obs    π 0 1 − π 0 obs · n (w; µ, ς) ·

P (w, h) =    0 1

H max −H min if (w, h) = (0, 0), if (w, h) ∈ R ++ × [H min, H max [, (a. 19) else.

Four options are considered: either one implements the probability of drawing the non–market alternatives by fixing the number of times the non–market alternative is to be drawn, say n 0, as being equal to the integer nearest to π 0 obs · (n s + 1). Or, one treats the number of times the non–market alternative is drawn, to be a random number, say K 0, with expected value E {K 0} = π 0 obs · (n s + 1), 32 See Section 3.3. An illustration of the shape of that distribution function is given in Figure 1. See Section 3.3. 34 The vector of covariates determining the value of the density p (k) referred to earlier, and denoted as x p,k, thus consists in this case of (x q, x g 1, w k, h k ). We do not mention x g 2 explicitly here, as they are implicitly included by letting the γ’s be sex specific. 35 See equation (30). 33 by letting the probability of each draw to be the non–market alternative, to be equal to π 0 obs. Secondly, one can sample with or without replacement. Lemp and Kockelman (2012) argue that sampling with replacement is inefficient since the same alternative may appear several times in the sampled choice set while not yielding additional information on choice behaviour. But on the other hand they warn that figuring out the selection probabilities of the sampled choice set D, denoted earlier as Π (D), might be cumbersome (with larger datasets) if the sampling takes place without replacement. One way to implement sampling without replacement, is selecting n s alternatives according to the a priori determined probability (density) P (w, h) (see equation a. 19 ), and then remove the repeated draws from the sampled set. If one samples without replacement, the size of the sampled choice is a random number, while it is fixed when drawing takes place with replacement. Finally, to reassure that the actually chosen alternative belongs to the sampled choice set, one adds it to the sampled set if it was not selected yet, or else, an additional randomly chosen alternative is drawn according to the probability (density) P (w, h). In case draws are with replacement, this renders the size of the sampled choice set to be equal to n s + 1. Otherwise, when drawing is without replacement, the expected size of the sampled choice set is equal n s + 1 − π 0 obs · (n s + 1) − 1. 36 In the present application we opted for sampling with replacement according to equation (a. 19 ), and treating the number of non–market alternatives as a random variable. In that case, the probability to draw a choice set D, Π (D), equals:

## Π (D) =

k 0 π 0 obs 1 − π 0 obs

H max − H min n s + 1−k 0

## Y

n (w k; µ, ς), (a. 20) (w k ,h k )∈D\{(0,0)} where k 0 is the actual realisation of K 0 for a specific draw of the choice set. The conditional sampling probabilities, π (D |k; C ), equal Π (D) /P (w k, h k) for all (w k, h k) ∈ D. So, the positive conditioning property is satisfied. The sampled log–likelihood function thus reduces to 37: L (β, δ; X) := p (δ;x t,q ,x t,g 1 ,w k ,h k) P (w j(t) ,h j(t))

## P

## P

− t ln .

k∈D t exp v (β; x t,k) − v β; x t,j(t) p (δ;x t,q ,x t,g 1 ,w j(t) ,h j(t)) P(w k ,h k) (a. 21) For couples, the elements of the choice set to be sampled consist of quadruples (w 1, h 1, w 2, h 2) ∈ [{(0, 0)} ∪ R ++ × [H min, H max [] 2, specifying a wage labour time regime for each partner i (i = 36 Of course, if the number of times the non–market alternative is drawn, was fixed, the size of the sampled choice set will be fixed too, and equals n s + 1 − (n 0 − 1). 37 In the ruro model, the systematic part of the utility function depends solely on the wage and labour time characteristics of a job, but parameters of the utility function may depend on individual characteristics, say x t,V. Therefore v (β; x t,k) is in fact a shorthand for v (β (x t,V); w t,k, h t,k ), with β (x t,V) a function of the variables x t,V. See Section 2.2 for the relation of preferences defined over the space of consumption leisure time bundles, and preference in the wage–labour time regime space.

1, 2). Sampling of these alternatives is done by independently sampling for each of the partners a wage labour time regime bundle (w i, h i) according to the same prior as for singles, P i (w i, h i) (see equation a. 19 ). The probability (density) P i is indexed on the partner i (i = 1, 2) since their obs characterising parameters, π i,0, µ i, ς i need not to be the same for both partners. So, importance sampling of alternatives (w 1, h 1, w 2, h 2) takes place according to according to the probability (density) function:

F (w 1, h 1, w 2, h 2) = P 1 (w 1, h 1) · P 2 (w 2, h 2).

(a. 22) Denote the sampled choice set for couples by D c, and let D i c be the set of combinations of wages and labour time regimes in the sampled choice set D c that pertain to partner i. That is, D 1 c := {(w 1, h 1) |∃ (w 2, h 2): (w 1, h 1, w 2, h 2) ∈ D c }, and D 2 c := {(w 2, h 2) |∃ (w 1, h 1): (w 1, h 1, w 2, h 2) ∈ D c }. Furthermore, let k 00, k 01, k 10 be respectively the actual number of times the alternative in which both do not accept any job offer is drawn, the number of times an alternative in which the first, respectively second, partner does not accept a job offer while the second, respectively first does, is drawn, for a specific outcome of the sampling procedure. We then obtain the following sampling probability for a choice set D c, Π (D c ): Π (D c) = obs · π obs k 00 · π obs · 1 − π obs k 01 · obs · π obs k 10 · π 1,0 1 − π 1,0 2,0 1,0 2,0 2,0 obs · 1 − π obs n s +1−k 00 −k 01 −k 10 · 1 − π 1,0 2,0   2(n s +1−k 00 )−k 01 −k 10 Q

## Q

1  n (w i,k; µ i,0, ς i,0) .

·

H max −H min i=1,2 (w i,k ,h i,k) ∈D c \{(0,0)} i The conditional sampling probabilities, π (D c |k; C ), equal Π (D c) /

## Q

(a. 23)

## (P

(w , h )) for all i i,k i,k i=1,2 (w 1,k, h 1,k, w 2,k, h 2,k) ∈ D c. So, the positive conditioning property is satisfied. The part of the sampled log–likelihood function that pertains to observations on couples, becomes:

## P

L (β c, δ 1, δ 2; X) := − t ln l t, with l t = "

## Q

## P

k∈D c t exp v c (β c; x t,k) − v c β c; x t,j(t) i=1,2 p δ i ;x ti ,q ,x t p δ i ;x ti ,q ,x t i ,w i,k ,h i,k i ,g 1 i ,w j (t) ,h j (t) i i i ,g 1 !# P i w j (t) ,h j (t) i i .

P i (w i,k ,h i,k) (a. 24) Here, v c is the household utility function which is defined over quadruples (w 1, h 1, w 2, h 2 ), and parameters β c may depend on household characteristics or individual household members’ characteristics, as further specified in Section 3.3.

Appendix III Concordancy tables The row totals of the next tables represent the number of persons in the sample observed in the different labour time regimes (no participation, one to 18.5 hours, half time (18.5–20.5), 20.5 to

## 29.5 hours, three quarter time (29.5–30.5), 30.5 to 37.5 hours, full time (37.5–40.5), and more than

full time), while the cells for each row reflect how these are distributed across the labour regimes according to the simulation. The column totals compose then the simulated marginal distribution.

The histograms in the main text (Figures 9 and 12) are thus based on a comparison of the row and corresponding column totals.

Table a. I: Observed versus simulated labour time: males in couples

Simulated 20.5–29.5 29.5–30.5

Observed no part.

1.0–18.5 18.5–20.5 no part.

1.0–18.5 18.5–20.5 20.5–29.5 29.5–30.5 30.5–37.5 37.5–40.5 40.5–100 38 0 0 2 4 10 46 17 1 0 0 0 0 8 16 5 2 0 0 0 0 2 11 2 2 1 0 0 1 11 34 14 col. tot.

117 30 17 63 30.5–37.5 37.5–40.5 40.5–100 row tot.

1 0 0 0 2 3 12 8 9 0 0 1 1 21 54 35 28 5 9 13 16 88 407 178 18 1 5 3 4 34 183 91 99 7 14 19 28 177 763 350 26 121 744 339 1457 Table a. II: Observed versus simulated labour time: females in couples

Simulated 20.5–29.5 29.5–30.5

Observed no part.

1.0–18.5 18.5–20.5 30.5–37.5 37.5–40.5 40.5–100 row tot.

no part.

1.0–18.5 18.5–20.5 20.5–29.5 29.5–30.5 30.5–37.5 37.5–40.5 40.5–100 130 20 34 23 14 37 48 10 15 7 17 18 9 24 44 7 26 2 7 15 13 18 33 9 27 0 8 17 11 22 26 7 18 2 12 7 7 14 24 5 17 4 13 14 11 17 32 11 53 25 37 37 32 75 113 36 14 6 11 17 8 18 52 17 300 66 139 148 105 225 372 102 col. tot.

316 141 123 118 89 119 408 143 1457 Table a. III: Observed versus simulated labour time: single males

Simulated 20.5–29.5 29.5–30.5

Observed no part.

1.0–18.5 18.5–20.5 no part.

1.0–18.5 18.5–20.5 20.5–29.5 29.5–30.5 30.5–37.5 37.5–40.5 40.5–100 47 0 3 1 0 4 24 6 3 0 1 0 0 1 8 1 0 0 0 1 0 2 4 2 1 0 0 1 0 1 16 2 col. tot.

85 14 9 21 30.5–37.5 37.5–40.5 40.5–100 row tot.

1 0 1 0 0 1 1 1 3 0 0 0 0 4 17 9 30 2 3 7 1 25 90 41 10 0 0 2 3 11 39 18 95 2 8 12 4 49 199 80 5 33 199 83 449 Table a. IV: Observed versus simulated labour time: single females

Simulated 20.5–29.5 29.5–30.5

Observed no part.

1.0–18.5 18.5–20.5 no part.

1.0–18.5 18.5–20.5 20.5–29.5 29.5–30.5 30.5–37.5 37.5–40.5 40.5–100 103 3 11 4 7 18 35 8 11 0 3 2 1 4 8 1 4 0 1 1 1 5 6 1 10 0 0 1 1 3 21 2 col. tot.

189 30 19 38 30.5–37.5 37.5–40.5 40.5–100 row tot.

11 0 1 3 1 2 11 1 8 0 2 1 2 4 12 5 26 6 8 6 13 22 62 8 9 0 3 7 1 6 29 25 182 9 29 25 27 64 184 51 30 34 151 80 571
