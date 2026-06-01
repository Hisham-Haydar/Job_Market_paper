# EUROMOD: The European Union Tax-Benefit

Microsimulation Model

Holly Sutherland and Francesco Figari

March 2013 EUROMOD: The European Union Tax-Benefit Microsimulation Model 1

Holly Sutherland a Francesco Figari b a b

ISER-University of Essex

University of Insubria and ISER-University of Essex

## Abstract

This paper aims to provide an introduction to the current state of the art of EUROMOD, the European Union tax-benefit microsimulation model. It explains the original motivations for building a multi-country EU-wide model and summarises its current organisation. It provides an overview of EUROMOD components, covering its policy scope, the input data, the validation process and some technical aspects such as the tax-benefit programming language and the user interface. The paper also reviews some recent applications of EUROMOD and, finally, considers future developments.

1 We would like to thank Paola De Agostini, Gijs Dekkers and Iva Tasseva for their helpful comments on this paper. We acknowledge the contribution of all past and current members of the EUROMOD consortium and in particular of our colleagues at ISER at the University of Essex without whom the achievement of EUROMOD for the whole EU-27 would not have been possible. The EUROMOD preparatory study was funded by the European Commission’s Targeted Socio-Economic Research (TSER 1996-1997). EUROMOD itself was constructed for the then EU-15 countries funded by the European Commission Fourth Framework Programme (FP4 – EUROMOD: an integrated European benefit-tax model 1998-2000 CT97-3060). It was then updated as part of the FP5 project MICRESA (Micro analysis of the European Social Agenda 2001-2004 HPSE-CT200100099). The FP6 project I-CUE (Improving the Capacity and Usability of EUROMOD 2005-2008 RIDS 011859) provided the basis to extend the model to the whole EU-27 countries and make it easier to update, maintain and use. The FP6 project AIM-AP (Accurate Income Measurement for the Assessment of Public Policies 2006-2009 No. 028412) has explored ways to improve EUROMOD capacity to include non-cash incomes, indirect taxes and modelling benefit non-take up and tax evasion. More recently, the EUROMODupdate projects, supported by the European Union Programme for Employment and Social Security – PROGRESS (2007-2013), have sustained the EUROMOD enlargement to cover 27 Member States, updating to recent policy systems and using data from the European Union Statistics on Income and Living Conditions (EU-SILC) as the input database.

2

JEL Classification: H31, C81, C88

Keywords:

EUROMOD, microsimulation, Europe

Corresponding author:

Holly Sutherland

E-mail: hollys@essex.ac.uk 3 1.

EUROMOD: A pan-European research infrastructure EUROMOD is the European Union tax-benefit microsimulation model. It simulates individual and household tax liabilities and benefit entitlements according to the policy rules in place in each member state. Its main distinguishing feature is that it covers all European countries within the same framework allowing for flexibility of the analysis and comparability of the results. Generally, EUROMOD is much more flexible than a national microsimulation model and this flexibility is essential if consistency (of results across countries), transferability (of tax-benefit system components) and use by multiple users are to be achieved. The potential trade-offs between flexibility and user friendliness are dealt with through the adoption of a user interface specifically designed for a multi-country microsimulation model. This paper aims to provide an introduction to the current state of the art of EUROMOD development and its applications, given the further enhancements of the model and its wider use since the most recent review (Sutherland, 2007). EUROMOD is a static model in the sense that the arithmetic simulation of taxes and benefits abstract from potential behavioural reactions of individuals and the socio-demographic characteristics of the population are assumed to be fixed over time. EUROMOD calculates, in a comparable manner and based on individual micro-data representative of the national populations of interest, the static effects of the tax-benefit system on household incomes for the population of each country and for the EU as a whole. EUROMOD is of value both in terms of assessing the effects of consolidated tax-benefit policies and in understanding how tax-benefit policy reforms may affect income distribution, work incentives and government budgets. EUROMOD can be used to examine the effects of actual changes in policy over time, for example to show the extent to which changes in public policies have contributed to reducing (or increasing) income poverty or inequality. It can also be used to simulate the effects of proposed, alternative or hypothetical policy changes in each member state, as well as for exploring the implications of alternative economic or demographic scenarios at national and EU levels.

4 Moreover, EUROMOD calculations can run on a set of hypothetical families that the user can define based on a number of assumptions about family and labour market characteristics. This allows the users to compare the effects of different tax-benefit systems and to derive the monetary resources available to the individuals belonging to these families under different circumstances (for example, by drawing the budget constraint charts which show the disposable income at different hours of work based on the assumed hourly wage). EUROMOD is unique in being a research tool that is relevant not only at national level and as an integrated tool for European comparative social science research, but also as a model of the EU as a whole. 2 Thus EUROMOD is of value in understanding how different policies in different countries may contribute to country specific or common objectives through (i) crosscountry comparison of specific tax-benefit instruments, (ii) policy and whole tax-benefit system swapping, and (iii) analysis of the impact of common changes across countries (Lietz and Mantovani, 2007). Static calculations performed by EUROMOD may inform other more sophisticated economic models which aim to capture, for instance, the effects of policy or socio-demographic changes on individual behaviour or macro-economic and environmental consequences. Recently, EUROMOD has been extensively used as the basis for labour supply models (see among others, Bargain et al., 2012c). EUROMOD is unusual in that it is openly accessible. It is intended for academic and noncommercial policy-relevant analysis and it is in principle available for use by any researcher subject to permission to access the micro-data that are used as input to the model. Moreover, the EUROMOD framework can be used to build fiscal microsimulation models for non-EU countries in a much more cost-effective way than starting from scratch. This has been the case for the spin-off models appeared recently for South Africa (SAMOD, see Wilkinson, 2009), Serbia (SRMOD, see Žarković-Rakić, 2010) and Russia (RUSMOD, see Popova, 2012) which have confirmed the great value of knowledge transfer from the EUROMOD community to other users. EUROMOD is not only relevant to academics but also of potential use for national and European policy makers, as the model itself embodies a knowledge base about different and 2 There are plans to extend EUROMOD to include Croatia when it joins the EU and SILC micro-data are made available.

5 changing national policy structures and systems within a comparative framework. See the web site of the EU Social Situation Observatory (www.socialsituation.eu) for recent policy applications of the model and recent publications from DG-EMPL (European Commission, 2012; 2013a) and DG-ECFIN (European Commission, 2013b) of the European Commission, which increasingly make use of EUROMOD results. Moreover, in order to satisfy the increasing need of public availability of ex-ante policy evaluation tools, more recently EUROMOD has started to be used as the “engine” behind simplified national web-based microsimulation models which allow a wider audience of users to assess the distributional and budgetary effects of planned or hypothetical policy reforms (see, for example, www.flemosi.be). See the official EUROMOD web site (https://www.iser.essex.ac.uk/euromod) for up-to-date information and detailed instructions on how to access the model. The paper is structured as follows. Section 2 summarises the original motivations for building EUROMOD and its current organisation. Section 3 gives an overview of EUROMOD components, highlighting the policy scope, input data and the validation process, followed by a brief description of the tax-benefit programming language and the user interface in Section 4. Section 5 reviews some recent applications based on EUROMOD. In Section 6 future developments and limitations are discussed.

2.

Recent history and current organisation The motivations which inspired the first EUROMOD prototype (Sutherland, 1997) are still valid after more than 15 years of accumulated expertise. The pioneering work by Atkinson et al. (1988) looked at the implications of applying the British tax system based on personal deductions to the French population and replacing the existing quotient familial. Some years later, Callan and Sutherland (1997) explored the impact of basic income schemes in the UK and Ireland but they could not include more European countries in a consistent way due to limitations of the national models available at that time. The natural option seemed to be the development of EUROMOD, a consistent European-wide model especially designed to maximise comparability across countries, recognising that national models tend to run with national assumptions and conventions “hardwired” in, and 6 that access to many models at once may be difficult to negotiate, if possible at all (Sutherland, 2007). The development of EUROMOD has been sustained by a succession of European Commission research grants and the involvement of a large group of researchers from universities, research institutes and ministries from all European countries, collaborating in the project and providing national expertise. The management and scientific coordination has been led by Professor Holly Sutherland with a team of researchers based originally at the University of Cambridge and now at the Institute for Social and Economic Research (ISER) at the University of Essex. EUROMOD has provided the impetus for the construction of associated national models in countries where they did not exist before or were not generally available (among others, Austria, Greece, Latvia, Luxembourg, Malta, Portugal, Spain). Moreover, many national team members are involved in the development and use of national models 3 which facilitate a fruitful interaction and mutual ongoing learning.

3.

3.1

EUROMOD overview

Policy scope and simulation As with most of static microsimulation models, EUROMOD combines information on relevant policy rules with detailed and representative micro-data on individual and household circumstances drawn from national household income surveys and other data sources. The results of EUROMOD calculations are stored at the micro level and can be easily analysed with any statistical software. Moreover, EUROMOD can also be used to calculate a set of work incentive indicators (Effective Marginal Tax Rates, Replacement Rates and Participation Tax Rates) which gives a first indication of the likely impact of policy reforms on individual work behaviour. EUROMOD aims to simulate as much as possible of the tax and benefit components of household disposable income. Generally, the following instruments are simulated in all countries: income taxes (national and local), social contributions (paid by the employees, selfemployed and employers), family benefits, housing benefits, social assistance and other 3 Among others, SWITCH for Ireland (Callan et al., 2011a), TaBeIta for Italy (Fiorio, 2009), FASIT for Sweden (Odencrants and von Hofsten, 2012), MEFISTO for Flanders – Belgium (Decancq et al., 2012), ALAN for Estonia (Võrk et al., 2008), POLIMOD for the UK (Redmond et al., 1998).

7 income-related benefits. Instruments which are not simulated are taken directly from the data and included in the concept of disposable income. This is the case for most contributory benefits and pensions (due to the lack of information on previous employment and contribution history in the cross-sectional survey data used as input of EUROMOD) and disability benefits (because of the need to know the nature and severity of the disability, which is also not present in the data). The extent of these types of benefits varies across countries. For example, in some countries it is possible to simulate non-contributory elements of the pension system; while in countries without such pensions, no component of the pension system can be simulated. Moreover, EUROMOD simulates unemployment benefits based on assumptions related to individual characteristics (e.g. previous earnings) not available in the cross-sectional input data. The simulation of unemployment benefits is mainly intended for the calculation of replacement rates. Currently (i.e. the latest EUROMOD public version F6.0 released in August 2012) EUROMOD simulates the policy systems up to 2010 for all EU 27 countries. The national policy systems have been introduced into EUROMOD through a three stage process; as a consequence, 2005 systems are modelled for nine countries; 2006 systems for eighteen; and from 2007 to 2010 system for all the 27 EU countries. It is planned that the F7.0 release in summer 2013 will cover policy systems up to 2012 for all EU 27 countries. The simulations run on several alternative input micro-datasets mainly starting from 2006 up to 2008. Overall, there are more than 250 policy-data-country combinations at the disposal of the user which have been validated. The ongoing EUROMODupdate2 project aims at updating policy systems annually and data on an annual or biannual basis. 4 Descriptive statistics are published regularly on the EUROMOD web pages, representing a first reference point for up-to-date baseline statistics produced by the public version of the model. Jara and Tumino (2013) provide a comprehensive overview of the redistributive and work incentive effects of the taxbenefit systems across the 27 European countries.

4 The year of the data refers to the data collection period. In case of SILC data the income reference period is the previous year (e.g. 2007 income data are from EU-SILC 2008). In the F7.0 release (summer 2013), half of the countries will be based on 2010 data and the other half of the countries will be based on 2010 data as part of the public release planned in 2014. For details on the current road map for publicly available releases of EUROMOD see Avram, Sutherland et al (2012) or https://www.iser.essex.ac.uk/euromod/developingeuromod/euromodupdate2.

8 3.2

Input data Most of EUROMOD input data are derived from the European Union Statistics on Income and Living Conditions (EU-SILC) data as released by Eurostat (Eurostat, 2012). In some countries (Belgium, Bulgaria, the Czech Republic, Greece, Spain, Italy, Lithuania, Luxembourg, Austria, Poland and Slovakia), the national version of SILC -provided by national statistics institutes -is used directly or to complement the EU version due to the availability of more detailed variables. In some circumstances, different or additional national surveys are used (e.g. the Family Resources Survey in the UK which will become the basis of the SILC from 2013). The advantages of using EU-SILC in terms of comparability across countries, efficiency in developing and maintaining a microsimulation model for many countries, complementarity with other key social indicators (e.g. material deprivation and work intensity), possibility to use EUROMOD to evaluate the progress towards the EU 2020 official targets for the promotion of social inclusion, and simplification of access arrangements counterbalances some limitations of the data. The major drawbacks are common to other survey data. In particular, the coverage of financial income is generally low with an impact on the simulation of taxes on capital income. Moreover, the lack of information about assets and the aggregation of income variables at annual level do not help in defining precisely the meanstests used in the simulation of social assistance programmes. In addition, the Eurostat version of the SILC provides information on income components in harmonised form. This involves the aggregation of benefits according to function (e.g. unemployment, old age). In preparing the input database for EUROMOD the information on the individual benefit payments must be recovered using imputation of some kind. This process inevitably reduces the precision of estimates using these data (Figari et al., 2007). The EUROMOD input database contains information at the individual level on household demographic, labour market characteristics, gross market income and all other income sources (i.e. pensions, public transfers and private incomes). The grossing-up survey weights are included in the input data and used in the analysis in order to correct for non-response and sampling error and to obtain aggregate estimates at the population level. If gross income values are not directly recorded during the survey operations and are imputed in a non-satisfactory way, a net-to-gross procedure is applied to the net income variables in order to derive the gross values used in the policy simulation.

9 Moreover, a standardised approach of defining and naming the variables (both in input and output EUROMD data, see Sutherland et al., 2008) enables the user to recognise similar taxbenefit components across countries and facilitates the possibility to adapt different data sources as EUROMOD input data (see Dal Bianco and Zantomio (2013) on the development of harmonized gross and net income measures in SHARE data by using EUROMOD or Vandelannoote et al. (2013) who adapt the Flemish Families and Care Survey for a specific analysis focusing on the responsiveness of labour supply to different childcare arrangements). The “baseline” simulations of a policy system are run on input data referring to the same income reference period (e.g. the baseline simulation of the 2007 policy system runs on 2008 EU-SILC data which income reference period is 2007). Nevertheless, the use of updating factors for each income source (i.e. Consumer Price Index, average earnings increase, legal variations in benefit amounts, or other specific indexes as appropriate) brings the income values from the income reference period up to the level of the policy year.

3.3

Validation of simulations and documentation Baseline systems in EUROMOD have been validated and tested at micro level (i.e. case-bycase validation) and macro level. The aggregate estimates for expenditure and number of recipients of each benefit (and revenue and number of tax payers of each tax) is regularly compared with the same information from external sources (e.g. administrative statistics and national microsimulation models, if available). Moreover, the simulated income distribution (in terms of poverty rates by age, income shares and overall inequality) has been compared with the income distribution recorded in the input data, and alternative sources if available. The results of the validation exercises are reported in the Country Reports (available on the EUROMOD web pages) which also contain background information on the tax-benefit system for each country, a detailed description of all tax-benefit components simulated in EUROMOD, a general overview of the input data (including information on sample quality, weights, data adjustment, imputations and assumptions) and an extended summary of the validation process. Moreover, annual reports document the headline indicators produced by each new release of EUROMOD and discuss explanations for discrepancies between EUROMOD estimates and external aggregate statistics (Avram, Sutherland et al., 2012; Jara, Sutherland et al., 2013).

10 The disposable income simulated by EUROMOD corresponds to market income and public pensions after taxes and social insurance contributions are deducted and cash benefits added. Due to lack of the necessary information, EUROMOD baseline results do not comprehensively take into account non take-up of benefits or tax evasion. Therefore, the legal rules are assumed to be universally respected and the costs of compliance and claiming are assumed to be zero. This can result in the over-estimation of taxes and benefits and gives rise to differences between EUROMOD estimates of disposable income and income values recorded in the underlying datasets (Figari et al., 2012a). At the same time, estimates based on the assumption of full tax compliance and take-up can be interpreted as showing the intended effects of the system. Moreover, the estimates of theoretical benefit entitlements and tax liabilities are the key ingredient for the estimation of the extent and incidence of benefit non-take up (Matsaganis et al., 2010b; Tasseva, 2012) and tax evasion (Matsaganis et al., 2010a) which is one of the research areas where the microsimulation models can play an important role. In countries characterised by high rates of benefit non take-up (among others, Belgium, France, Greece, Ireland, Romania, and the UK), a simple correction is included in EUROMOD by considering the take-up proportions reported on a caseload basis in external statistics. We impose that only the same percentage of people entitled to a given benefit, selected randomly in the sample, does in fact take up their entitlement. The non take-up correction is applied at the household level for each benefit separately, so that people entitled to the same benefits within a household exhibit the same take-up behaviour. In general we assume that take-up behaviour is not affected by changes in the size of benefit entitlement. However, by considering differential take-up proportions according to type of claimant some of this effect is captured. At the same time, in countries where tax evasion is a widespread phenomenon, which affect in a substantial way the macrovalidation of EUROMOD simulations (among others, Bulgaria, Greece and Italy), a simple correction is included in order to split some income sources (generally employment and self-employment income) recorded in the survey into a first component which is assumed to be reported to the tax authority and in a residual component which is assumed to be evaded (see Ceriani et al. 2013).

11 Both the corrections for benefit non take-up and tax evasion are documented in the Country reports and applied in a transparent way which is capable of being “switched off” or adapted by the users, depending on the analysis that they wish to do.

4.

Tax-benefit programming language and user interface EUROMOD constitutes a software platform made of a programming language specific to (static) tax-benefit calculations and generic enough to accommodate many different countries. The tax-benefit rules are stored and displayed in a very flexible modular system design in a standardised way for each country and each policy year simulated. The tax-benefit rules, expressed either as monetary or non-monetary values, act as parameters of EUROMOD functions. These functions constitute the building blocks of the EUROMOD tax-benefit modelling language read directly by the code. They are fully documented in a series of user manuals. EUROMOD code is written in C++ and compiled, meaning that the users have access to an executable file and they do not need to access the code itself. This is possible because there are no parts of the national tax-benefit systems that are hard-wired in the code and policy changes can be implemented without reprogramming the code itself. When a user runs EUROMOD, the code reads the tax-benefit rules stored in the user interface, implements such rules on the input data and produces an individual level output data with information coming from the input data and the tax-benefit simulation. The implementation of complex policy reforms is facilitated by the flexible definition of the major functions. These include the functions used to define the units of assessment (i.e. the group of people on which the taxbenefit rules are to be performed), the income lists (i.e. the aggregations of monetary variables used as input to tax-benefit algorithms) and the policy spine (i.e. the order of policy simulations). The current version of EUROMOD is the result of the expertise and the technical developments achieved over many years. The interface of the current public release is built using Microsoft Excel which is convenient but not always stable. A special-purpose standalone user interface, programmed using Microsoft .net Framework is currently in its testing phase. This promised to enhance the user-friendliness of the model and makes it completely independent of any other software.

12 Such a flexible and transparent framework has proved to be very useful to shortcut the process of building similar microsimulation models with potentially comparable outputs for any country.

5.

An overview of recent applications based on EUROMOD To give a complete list of all publications based on EUROMOD is beyond the scope of this article. In the following, we want to provide some insights into research areas where EUROMOD has been recently used and where it can play a central role in future research developments. 5.1

Redistributive effects of tax-benefit policies Before the full availability of the EU-SILC data including both net and gross incomes in 2009, EUROMOD offered a remarkable contribution to economic research on the redistributive effects of tax-benefit policies across Europe, being the only available source of income micro-data before and after government intervention for all European countries. Immervoll et al. (2006) is one of the first and most cited empirical analysis on the redistributive effects of taxes and benefits in European countries. More recently, Paulus et al. (2010) offer new insights into the redistributive role of the government transfers by considering the impact of the most important in-kind benefits (education, health, public housing), while Decoster et al. (2010) look at the post-tax income distribution by taking into account indirect taxes as well. Nevertheless, the strength of EUROMOD in producing tailored micro-level information emerges in a number of studies focusing on the redistributive aspects of specific tax-benefit policies implemented across Europe or across time. For example, Figari et al. (2011a) explore the effects of tax-benefit systems on differences in income and incentives to earn income within couples, highlighting important gender effects of taxes and benefits. Figari et al. (2013) describe the redistributive effects of Minimum Income schemes by comparing their coverage and adequacy for persons of working age in the European Union. Looking at the overall tax-benefit system, Bargain in a series of papers develops and extends a methodology to quantify the relative effect of tax-benefit policy changes over time, by decomposing the overall effect in the contribution of the changes in the tax-benefit structure, 13 in the underlying population and in the distribution of market income (Bargain and Callan, 2010; Bargain 2012a, 2012b).

5.2

Policy swapping analysis One of the initial motivations for building a multi-country model at the European level came from the attempts to investigate the different characteristics of the tax-benefit systems, in order to evaluate the potential impact of “borrowing” policies in place in other countries. Such experiments are nowadays known as “policy swapping” exercises and they may be particular useful to understand the likely impact of any policies on a given population of interest, to capture the interaction between tax-benefit systems and the characteristics of such a population and to assess the effectiveness of the national policies. Two areas of research have been investigated recently. The first strand focuses on child benefits highlighting the relevance of policy swapping exercises in distinguishing between the effects of level of spending, policy structure and impacts due to the characteristics of national populations (Canto et al., 2012; Levy et al., 2007; 2009; Salanauskaite and Verbist, 2013). In a cross-country perspective, Figari et al. (2011b) used EUROMOD simulations to suggest a new comprehensive measure of support given through tax-benefit systems to families with children, taking into account all provisions contingent on the presence of children and not only those channelled through benefits explicitly labelled for children. The second strand is about in-work benefits which have been proposed and implemented in a number of European countries to make the tax-benefit system more favourable for low paid earners. Analysis of in-work benefits requires that the interaction of these instruments with the rest of the tax-benefit system is taken into consideration in order to evaluate the overall work incentives embedded in the system (Bargain and Orsini, 2006; Figari, 2010; 2011).

5.3

Tax design aspects The detailed simulation of the personal income tax in EUROMOD offers the potential for empirical studies focussing on specific aspects of the design of personal income tax. Recently, different contributions focussed on the redistributive and work incentive effects of the implementation of a flat rate income tax which has become increasingly popular in the policy debate but is as yet limited to Eastern Europe (among others, Paulus and Peichl, 2009).

14 In recent years, the financial crisis has revived interest in housing taxation across Europe. On the one hand, concerns have been raised about the role played by mortgage interest tax relief (Matsaganis and Flevotomou, 2007a; 2007b). On the other hand, housing taxation is in the spotlight as one of the few practicable ways of raising tax revenues while lowering the tax wedge on labour income (Figari et al., 2012b). Maestri (2012) extends the existing literature by evaluating the redistributive effect of a comprehensive set of housing-related policies, taking into account the housing advantage of homeowners and social tenants. 5.4

Work incentives and labour supply The short term effects of a policy reform (often referred to as the overnight effect) give useful insights into the redistributive and budgetary effects of a policy change. Nevertheless, EUROMOD is increasingly used to analyse the strength of work incentives and the secondround effects related to the policy changes. A number of papers make use of the static indicators of work incentives produced by EUROMOD to capture the incentive effect at the intensive (hours) margin (i.e. Effective Marginal Tax Rates showing how much of a marginal increase in gross earnings – due to longer hours or extra effort – is levied in increased taxes or lower benefits; see Immervoll, 2004 and Jara and Tumino, 2013) and at the extensive (participation) margin (i.e. Net Replacement Rates or Participation Tax Rates; see Immervoll and O’Donoghue, 2004) Moreover, the static calculations produced by EUROMOD are increasingly used to derive the budget sets used in the structural discrete choice labour supply models which are a wellestablished and recognised modelling set up to predict the individual behavioural adjustments to policy changes. Bargain et al. (2012c) provide the first large-scale international comparison of labor supply elasticities for 17 European countries (and the US), separately by gender and marital status. By using EUROMOD, they are able to net out measurement differences affecting previous analysis due to non-harmonized empirical approaches and different data sources. Other papers focus on methodological aspects related to the labor supply modelling (Colombino, 2012; Liégeois and Islam, 2012) or specific policy questions (Bargain and Orsini, 2006; Colombino et al., 2010; Figari, 2011). Moreover, labor supply estimated preferences and elasticities are a key ingredient in a series of papers on the optimality of tax systems and welfare regimes (Bargain et al., 2011; 2012a; Bourguignon and Spadaro, 2012;

15 Immervoll et al., 2007; 2011) and the cross-country perspective offered by EUROMOD proves to shed new light in this strand of literature.

5.5

The economic downturn More recently, at the onset of the economic downturn affecting European countries since the end of 2008, EUROMOD proved to be one of the most important tools to provide an ex-ante evaluation of the consequences of the crisis on income distribution in Europe. Figari et al. (2011c), Avram et al. (2011) and Fernandez et al. (2013) apply a stress test approach to tax-benefit systems in order to predict the cushioning effects of the social protection schemes for those who lose their job and to assess the overall income stabilisation – through relative and absolute welfare state resilience – after a macroeconomic shock. Callan et al. (2011b) and Avram et al. (2012) compare the distributional effects of policy changes presented as fiscal consolidation measures in different EU countries that experienced large budget deficits following the financial crisis, highlighting the distributive effects of different policy mixes implemented across Europe. Focusing on Greece, Leventi and Matsaganis (2011) distinguish between two inter-related factors. On the one hand, the austerity measures taken to reduce fiscal deficits; on the other hand, the wider recession, and quantify the distributional implications of both factors providing, in a timely fashion, the first comprehensive assessment of the distributive impact of the crisis in Greece. Dolls et al. (2012a, 2012b) analyze the effectiveness of the tax and transfer systems in the European Union (and the US) to act as an automatic stabilizer in an economic crisis, showing the extent to which European tax-benefit systems, although heterogeneous, are more effective in absorbing a macroeconomic shock than in the US. Moreover, Bargain et al. (2012b) show that moving towards a European fiscal union would have a stabilising effect, through either an EU-wide tax and transfer system or an EU-wide system of fiscal equalisation.

6.

Concluding remarks: a vision for the future The current version of EUROMOD represents the accumulation of technical developments and expertise over many years and involving a large team of people. Continuing to keep it upto-date in terms of both policy and data, while improving quality and comparability across so 16 many countries, already poses a set of ambitious aims for EUROMOD over the next few years. Nevertheless, the academic engagement with the analytical challenges posed by new policy agendas related to Europe 2020 on the one hand, and effective recovery from economic crisis on the other, provide additional opportunities. These include extending the scope of what EUROMOD can do, and how it can be used. First of all, the policy scope can be further extended by i) integrating in a systematic way the simulation of indirect taxes, ii) including the value of private non-cash incomes (imputed rent for owner-occupied accommodation, consumption of own production and fringe benefits provided by the employers), and iii) the value of public services (health, education, public housing, elderly and child care services). The methodological approaches developed as part of the AIM-AP project and already tested in a number of countries are the natural starting point for these extensions. 5 Nevertheless. the simulation of policies with an effect over the life cycle of individuals (e.g. contributory pensions) remains out of the scope of a multi-country static model like EUROMOD due to data limitations and the need of a dynamic modelling set up which, however, could use EUROMOD calculations as a starting point. Secondly, there is scope for technical improvement. Further refinement of the policy simulations requires benefit non take-up and tax evasion to be modelled in a way which is often constrained by data requirements. Connected to this, more work is needed to impute gross income values (when these are not collected directly in the survey data) by making systematic use of net-to-gross procedures based on microsimulation models. Thirdly, the recent volatility in economic conditions has demonstrated both the need for and challenges associated with estimating “current” risk of poverty and income inequality, as well as the direction of recent trends. Microsimulation approaches can be used to “nowcast” the current situation based on a combination of somewhat out-of-date micro-data, macro indicators about near-current economic conditions, and current policy rules. The simple updating of incomes from data year to policy year and assumptions of unchanging personal characteristics described above can be elaborated to include (for example) the modelling of 5

https://www.iser.essex.ac.uk/euromod/research-and-policy-analysis-using-euromod/aim-ap

17 labour market change and re-weighting to adjust for major demographic change due to e.g migration. A start on such an agenda has been made using EUROMOD by Navicke et al. (2013) and work will continue. Fourthly, the availability of a model that covers the whole EU combined with new interest in EU-level fiscal policy (among other contributions, see the Focus on European Fiscal Union in the spring 2012 issue of the CESifo Forum) provides the opportunity to carry out policyrelevant analysis at the EU-level. This means exploring the implications of policy options for budgets at the EU level as well as for implicit flows of resources between as well as within countries. Some studies already did this using just part of the EU (Bargain et al., 2012b; Levy et al., 2007a). A recent study of the potential for an EU child benefit did this for the whole EU27 (see Levy et al., 2013). Finally, the possibility of offering access to a simplified version of EUROMOD to policymakers and civil society at large via the web is an exciting development. For a complicated analysis, it will still be necessary to access EUROMOD itself, to take advantage of its flexibility. But an interface on the web, which offered limited choice, could still be a powerful tool of a different kind if those choices are informed by, and responsive to, national debates and current policy issues. This itself requires resources, of course, but by building on the existing modelling infrastructure is extremely cost-effective. For the success of this vision and for the future challenges of EUROMOD, the cooperation between academic researchers, policy users and stakeholders at national and EU level will be of vital importance and it will contribute to integrate tax-benefit models into the mainstream of economic policy-making (Atkinson 2009).

18

## REFERENCES

Atkinson A. B. (2009)'An enlarged role for tax-benefit models', in Lelkes O. and H.

Sutherland (Eds.), Tax and Benefit Policies in the Enlarged Europe: Assessing the Impact with Microsimulation Models. Farnham: Ashgate.

Atkinson A. B., Bourguignon F. and P. A. Chiappori (1988),'What do we learn about tax reforms from international comparisons? France and Britain', European Economic Review, 32.

Avram S., H. Sutherland, et al. (2012)'Baseline results from EUROMOD: 2006-2009 policies', EUROMOD Working Paper Series EM1/12.

Avram S., H. Sutherland, I. Tasseva and A. Tumino (2011)'Income protection and poverty risk for the unemployed in Europe', Social Situation Observatory Research Note 1/2011.

Avram S., F. Figari, C. Leventi, H. Levy, J. Navicke, M. Matsaganis, E. Militaru, A. Paulus, O. Rastrigina and H. Sutherland (2012)'The distributional effects of fiscal consolidation in 9 EU countries'. Social Situation Observatory Research Note 01/2012.

Bargain O. (2012a)'Back to the Future: Decomposition Analysis of Distributive Policies Using Behavioural Simulations'. International Tax and Public Finance 19(5): 708-731.

Bargain O., (2012b)'The Distributional Effects of Tax‐Benefit Policies Under New Labour: A Decomposition Approach', Oxford Bulletin of Economics and Statistics 74(6): 856-874.

Bargain O., and T. Callan (2010)'Analysing the Effects of Tax-Benefit Reforms on Income Distribution: A Decomposition Approach', Journal of Economic Inequality 8(1): 1-21.

Bargain O., Decoster A., Dolls M., Neumann D., Peichl A., and S. Siegloch (2012a)'Welfare, Labor Supply and Heterogeneous Preferences: Evidence for Europe and the US', Social Choice and Welfare. Forthcoming.

Bargain O., Dolls M., Fuest C., Neumann D., Peichl A., Pestel N., and S. Siegloch (2012b) 'Fiscal Union in Europe? Redistributive and Stabilising Effects of an EU Tax-Benefit System', IZA Discussion Paper 6585.

Bargain O., Dolls M., Neumann D., Peichl A., and S. Siegloch (2011)'Tax-Benefit Systems in Europe and the US: Between Equity and Efficiency', IZA Discussion Paper 5440.

Bargain O. and K. Orsini (2006)'In-work policies in Europe: killing two birds with one stone', Labour Economics 13: 667–97.

Bargain O., Orsini, K., and A. Peichl (2012c)'Comparing Labor Supply Elasticities in Europe and the US: New Results', IZA Discussion Paper 6735.

Bourguignon F., and A. Spadaro (2012)'Tax–benefit revealed social preferences', Journal of

Economic Inequality 10(1): 75-108.

Callan T. and H. Sutherland (1997)'The impact of comparable policies in European countries:

microsimulation approaches’, European Economic Review, 41: 627-633.

Callan T., Keane C., Walsh J. R., and M. Lane (2011a)'From Data to Policy Analysis: Taxbenefit Modelling Using SILC 2008', Statistical and Social Inquiry Society of Ireland 40:1-10.

19 Callan T., C. Leventi, H. Levy, M. Matsaganis, A. Paulus and H. Sutherland (2011b)'The distributional effects of austerity measures: a comparison of six EU countries', EUROMOD Working Paper Series EM6/11.

Canto O., Adiego M., Ayala L., Levy H., and M. Paniagua (2012)'Going regional. The effectiveness of different tax-benefit policies in combating child poverty in Spain', EUROMOD Working Paper Series: EM2/12.

Ceriani L., Fiorio C., and C. Gigliarano (2013)'The importance of choosing the data set for tax-benefit analysis', The International Journal of Microsimulation 6(1): 86-121.

Colombino U. (2012)'Equilibrium policy simulation with random utility models of labor supply', EUROMOD Working Paper Series: EM5/12.

Colombino U., Locatelli M., Narazani E., and C. O’Donoghue (2010)'Alternative Basic Income Mechanisms: An Evaluation Exercise with a Microeconometric Model', Basic Income Studies 5(1).

Dal Bianco C., and F. Zantomio (2013)'The development of harmonized gross and net income measures in SHARE', mimeo, University of Padova.

Decancq K., Decoster A., Spiritus K., and G. Verbist (2012)'MEFISTO: a new microsimulation model for Flanders', FLEMOSI Discussion Paper 14.

Decoster A., Loughrey, J., O’Donoghue, C., and D. Verwerft (2010)'How regressive are indirect taxes? A microsimulation analysis for five European countries', Journal of Policy Analysis and Management 29(2): 326-350.

Dolls M., Fuest C., and A. Peichl (2012a)'Automatic stabilizers and economic crisis: US vs.

Europe', Journal of Public Economics 96: 279-294.

Dolls M., Fuest C., and A. Peichl (2012b)'Automatic stabilization and discretionary fiscal policy in the financial crisis' IZA Journal of Labor Policy 1(4): 1-19.

European Commission (2012) Employment and Social Developments in Europe 2012,

Luxembourg: Publications Office of the European Union.

European Commission (2013a), EU Employment and Social Situation Quarterly Review (March), Brussels: The European Commission.

European Commission (2013b) The role of tax policy in times of fiscal consolidation, Luxembourg: Publications Office of the European Union. Forthcoming.

Eurostat (2012) 2010 Comparative EU intermediate quality report, European Commission:

Eurostat.

Fernandez Salgado M., Figari F., Sutherland H., and A. Tumino (2013)'Welfare compensation for unemployment in the Great Recession', Review of Income and Wealth. Forthcoming.

Figari F. (2010)'Can In-work Benefits Improve Social Inclusion in the Southern European countries?' Journal of European Social Policy 20(4): 301-315.

Figari F. (2011)'From housewives to independent earners: can the tax system help Italian women to work?', ISER Working Paper 15-2011, University of Essex.

20 Figari F., Iacovou M., Sutherland H., and A. Skew (2012a)'Approximations to the truth:

comparing survey and microsimulation approaches to measuring income for social indicators', Social Indicators Research 105 (3): 387-407.

Figari F., Immervoll H., Levy H., and H. Sutherland (2011a)'Inequalities within couples in Europe: market incomes and the role of taxes and benefits', The Eastern Economic Journal 37, 344-366.

Figari F., Levy H., and H. Sutherland (2007)'Using the EU-SILC for policy simulation:

prospects, some limitations and some suggestions' in Comparative EU statistics on Income and Living Conditions: Issues and Challenges. Eurostat Methodologies and Working Papers, European Communities.

Figari F., Matsaganis M., and H. Sutherland (2013)'Are European social safety nets tight enough? Coverage and adequacy of minimum income schemes in 14 EU countries', International Journal of Social Welfare 22: 3-14 Figari F., Paulus A. and H. Sutherland (2011b)'Measuring the size and impact of public cash support for children in cross-national perspective', Social Science Computer Review 29(1): 85-102.

Figari F., Paulus, A., Sutherland, H., Tsakloglou, P., Verbist, G., and F. Zantomio (2012b) 'Taxing the benefit of homeownership. Distributional effects of including imputed rent in taxable income', IZA Discussion Paper No. 6493.

Figari F., Salvatori A. and H. Sutherland (2011c)'Economic down turn and stress testing European welfare systems', Research in Labour Economics 32: 257-286.

Fiorio C.V. (2009) Microsimulation and analysis of income distribution, VDM Verlag. Immervoll H. and C. O’Donoghue (2004)'What Difference does a Job Make? The Income Consequences of Joblessness in Europe' in D Gallie (ed.), Resisting Marginalisation: Unemployment Experience and Social Policy in the European Union, Oxford: Oxford University Press, 105-139.

Immervoll H. (2004)'Average and marginal effective tax rates facing workers in the EU. A micro-level analysis of levels, distributions and driving factors', OECD Social, Employment and Migration Working Paper No. 19, OECD: Paris.

Immervoll H., Kleven H. J., Kreiner C. T., and E. Saez (2007)'Welfare reform in European countries: a microsimulation analysis', The Economic Journal 117(516): 1–44.

Immervoll H., Kleven H. J., Kreiner C. T., and N. Verdelin (2011)'Optimal tax and transfer programs for couples with extensive labor supply responses', Journal of Public Economics 95 (11-12): 1485-1500.

Immervoll H., Levy, H., Lietz, C., Mantovani, D., O’Donoghue, C., Sutherland, H., and G.

Verbist (2006)'Household incomes and redistribution in the European Union: quantifying the equalizing properties of taxes and benefits' in Papadimitriou, D. B. (Ed.), The Distributional Effects of Government Spending and Taxation, Palgrave Macmillan.

Jara X., H. Sutherland, et al. (2013)'Baseline results from the new EU27 EUROMOD (20072010)', EUROMOD Working Paper Series EM3/13.

21 Jara X. and A. Tumino (2013)'Tax-benefit systems, income distribution and work incentives in the European Union', The International Journal of Microsimulation 6(1): 27-62.

Leventi C., and M. Matsaganis (2011)'The distributional impact of the crisis in Greece',

EUROMOD Working Paper Series EM WP 3/11.

Levy H., Lietz, C., and H. Sutherland (2007)'Swapping policies: alternative tax-benefit strategies to support children in Austria, Spain and the UK', Journal of Social Policy 36(4): 625-647.

Levy H., C. Lietz and H. Sutherland (2007a)'A guaranteed income for Europe’s children?' in Jenkins S. and J. Micklewright (Eds.), Inequality and Poverty Re-examined, Oxford: Oxford University Press.

Levy H., M. Matsaganis and H. Sutherland (2013)'Towards a European Union Child Basic Income? Within and between country effects', The International Journal of Microsimulation 6(1): 63-85.

Levy H., Morawski, L., and M. Myck (2009)'Alternative tax-benefit strategies to support children in Poland', in Lelkes O. and H. Sutherland (Eds.) An Enlarged Role for Tax Benefit Models: assessing policies in the enlarged European Union, Farnham: Asghate.

Liégeois P., and N. Islam (2012)'Dealing with negative marginal utilities in the discrete choice modeling of labor supply', Economics Letters 118(1): 16-18.

Lietz C. and D. Mantovani (2007)'A short introduction to EUROMOD: an integrated European tax-benefit model' in Bargain, O. (Ed) Micro-Simulation in Action: Policy Analysis in Europe using EUROMOD, Research in Labor Economics 25: 1-16.

Maestri V. (2012)'Economic well-being and distributional effects of housing-related policies in 3 European countries', EUROMOD Working Paper Series: EM10/12.

Matsaganis M., and M. Flevotomou (2007a)'A basic income for housing? Simulating a universal housing transfer in the Netherlands and Sweden', Basic Income Studies 2(2): 1–25.

Matsaganis M., and M. Flevotomou (2007b)'The impact of mortgage interest tax relief in the Netherlands, Sweden, Finland, Italy and Greece', EUROMOD Working Paper EM2/07.

Matsaganis M., Benedek, D., Flevotomou, M., Lelkes, O., Mantovani, D., and S.

Nienadowska (2010a)'Distributional implications of income tax evasion in Greece, Hungary and Italy', MPRA Paper No. 21465.

Matsaganis M., Levy H., and M. Flevotomou (2010b)'Non take up of social benefits in Greece and Spain', Social Policy & Administration 44(7): 827-844.

Navicke J., O. Rastrigina and H. Sutherland (2013)'Using EUROMOD to “nowcast” poverty risk in the European Union', Eurostat Methodologies and Working papers series. Forthcoming.

Odencrants M., and H. von Hofsten (2012)'FASIT -a Swedish tax-benefit simulation model',

Statistics Sweden.

Paulus A. and A. Peichl (2009)'Effects of flat tax reforms in Western Europe', Journal of

Policy Modeling 31(5): 620-636.

22 Paulus A., Sutherland, H., and P. Tsakloglou (2010)'The distributional impact of in kind public benefits in European countries', Journal of Policy Analysis and Management 29(2): 243-266.

Popova D. (2012)'Constructing The Tax-benefit Micro Simulation Model For Russia –

RUSMOD', EUROMOD Working Paper Series EM7/12.

Redmond G., Sutherland H., and M. Wilson (1998) The Arithmetic of Tax and Social Security Reform: A User's Guide to Microsimulation Methods and Analysis, Cambridge: Cambridge University Press.

Salanauskaite L. and V. Gerlinde (2013)'Is the "neighbour's" lawn greener? Comparing family support in Lithuania and four other New Member States', Journal of European Social Policy. Forthcoming.

Sutherland H., Figari F., Lelkes O., Levy H., Lietz C., Mantovani D. and A. Paulus (2008) 'Improving the Capacity and Usability of EUROMOD: Final Report', EUROMOD Working Paper Series EM4/08.

Sutherland H. (1997)'The EUROMOD Preparatory Study: a Summary report', Microsimulation Unit Discussion Paper, MU9705, University of Cambridge.

Sutherland H. (2007)'EUROMOD: the tax-benefit microsimulation model for the European Union' in Gupta, A., and A. Harding (Eds.), Modelling Our Future: population ageing, health and aged care, International Symposia in Economic Theory and Econometrics, Vol 16. Elsevier.

Tasseva I. (2012)'Evaluating the performance of means-tested benefits in Bulgaria',

EUROMOD Working Paper Series EM8/12.

Vandelannoote D., Vanleenhove, P., Ghysels, J., and G. Verbist (2013)'Maternal employment: the impact of triple rationing in childcare in Flanders', FLEMOSI Discussion Paper. Forthcoming.

Võrk A., Paulus, A., and H. Poltimäe (2008)'Impact of taxation policy on distribution of household’s tax burden', PRAXIS Center for Policy Studies, Toimetised 42.

Wilkinson K. (2009)'Adapting EUROMOD for use in a developing country -the case of South Africa and SAMOD', EUROMOD Working Paper Series EM5/09.

Žarković-Rakić J. (2010)'First Serbian Tax-Benefit Microsimulation Model – SRMOD', The Quarterly Monitor of Economic Trends and Policies in Serbia: 20.

23
