# Karina Doorley IZA and CEPS/INSTEAD

Discussion Paper No. 7508

July 2013

## IZA

P.O. Box 7240

53072 Bonn

Germany

Phone: +49-228-3894-0

Fax: +49-228-3894-180

E-mail: iza@iza.org Any opinions expressed here are those of the author(s) and not those of IZA. Research published in this series may include views on policy, but the institute itself takes no institutional policy positions. The IZA research network is committed to the IZA Guiding Principles of Research Integrity. The Institute for the Study of Labor (IZA) in Bonn is a local and virtual international research center and a place of communication between science, politics and business. IZA is an independent nonprofit organization supported by Deutsche Post Foundation. The center is associated with the University of Bonn and offers a stimulating research environment through its international network, workshops and conferences, data service, project support, research visits and doctoral program. IZA engages in (i) original and internationally competitive research in all fields of labor economics, (ii) development of policy concepts, and (iii) dissemination of research results and concepts to the interested public. IZA Discussion Papers often represent preliminary work and are circulated to encourage discussion. Citation of such a paper should account for its provisional character. A revised version may be available directly from the author.

## ABSTRACT

Putting Structure on the RD Design:

Social Transfers and Youth Inactivity in France * Natural experiments provide explicit and robust identifying assumptions for the estimation of treatment effects. Yet their use for policy design is often limited by the difficulty in extrapolating on the basis of reduced-form estimates of policy effects. On the contrary, structural models allow us to conduct ex ante analysis of alternative policy situations. However, their internal validity is often questioned. In this paper, we suggest combining the two approaches by putting structure on a regression discontinuity (RD) design. The RD estimation exploits the fact that childless single individuals under 25 years of age are not eligible for social assistance in France. The behavioral model is identified by the discontinuity and by an additional exclusion restriction on the form of financial incentives to work. We investigate the performance of the behavioral model for predictions further away from the threshold, check external validity and use the model to predict important counterfactual policies, including the extension of social assistance to young people and the role of in-work benefit components.

## NON-TECHNICAL SUMMARY

We study the effect of the pre-2009 French social assistance program, the RMI, on labor supply. We find that eligibility for this program, which began at age 25 for single people, led to a drop of between 5 and 9% in the employment rate of young highschool dropouts. The replacement, in 2009, of the RMI by the RSA, which introduced an in-work benefit component to the transfer, is found to restore financial incentives to work and alleviate the inactivity trap for highschool dropouts. With this new system, which combines transfers to both workless and working poor, extending the program to under-25 year olds does not seem to create any significant disincentive effects to work. This is an important policy finding in the current context of very high youth unemployment and poverty in Europe.

JEL Classification:

Keywords:

## C52, H31, J22

behavioral model, regression discontinuity, labor supply

Corresponding author:

Olivier Bargain

GREQAM and AMSE

Château Lafarge

Route des Milles 13290, Les Milles

France

E-mail: olivier.bargain@univ-amu.fr *

The usual disclaimer applies.

1

## Introduction

Recent debates in the economic literature tend to compare and contrast the di¤erent approaches existing for policy evaluation (Angrist and Pischke, 2010, Deaton, 2009, Heckman and Urzua, 2010). A reasonable approach, however, seems to try to combine them optimally (Blundell, 2012). In particular, the economic literature should attempt to reconcile the methods based on randomized or natural experiments (ex post policy evaluation) with those relying on structural, behavioral models (ex ante evaluation). As stated by Imbens (2010), "much of the debate ultimately centers on the weight researchers put on internal validity versus external validity". For causal inference of actual policy e¤ects, it is hard to dispute that the experimental and quasi-experimental approaches are preferable. Critics of the structural approach generally argue that it is di¢ cult to identify all primitive parameters in an empirically compelling manner because of selection e¤ects, simultaneity bias and omitted variables. In fact, most studies using structural models are identi…ed on the basis of strong or unclear assumptions. As a result, their internal validity is often questioned. By contrast, ex post evaluation methods provide credible identifying assumptions. Yet, their external validity is often limited given the reduced-form nature of the estimated statistics and the fact that these statistics are not policy invariant parameters of economic models. This explains why structural models are still broadly used, allowing analysts to perform ex ante simulations for policy design as well as welfare analyses. 1 In this study, we combine the two approaches, focusing on the labor supply e¤ect of taxbene…t policies. We …rst rely on an age condition leading to a discontinuity in eligibility for the main social assistance program in France. We focus on the welfare program in place before 2009, a transfer to the workless poor (the Revenue Minimum d’Insertion, RMI). We exploit the fact that childless single individuals under 25 years of age are not eligible for this transfer. Estimates of the negative employment e¤ect of social assistance are identi…ed at the threshold using an RD design. To extrapolate further away from the discontinuity and perform counterfactual simulation, we add structure to the model. The labor supply model makes the underlying interpretation of the RD design explicit, i.e. optimizing agents in a static framework make participation decisions based on …nancial incentives to work. The age discontinuity a¤ects these …nancial gains and is used to identify the model. An additional exclusion restriction allows us to make predictions of participation responses at ages further away from the threshold. This framework provides an illustration of how valuable it is to combine ex post and ex ante methods. The discontinuity guarantees credible identi…cation of the structural 1 For instance, the recent development of collective models has allowed the shifting of welfare analysis from the household to the individuals level (cf. Vermeulen, 2001).

model while the latter allows us to answer some of the questions at the core of the political debate: Does an extension of welfare programs to under-25 year-olds generate greater unemployment and, possibly, long-term poverty among the youngest workers? What is the e¤ect of an EITC-type of reform that extends RMI payments to the working poor (the Revenue de Solidarité Active, RSA, introduced in 2009)? The …rst question is of particular importance in the present context of very high youth unemployment. The 16 24 year olds have been hit particularly hard by the crisis and face the highest rate of unemployment in France. The youth also have limited access to welfare programs, which results in a poverty rate twice as large as that of the 25-30 years-old (almost 11% when the poverty line is half the median income). 2 Studying age conditions for social bene…ts is not only relevant for France, as such discontinuities exist in several EU countries (e.g. Spain, Luxembourg, Denmark) and in Canada (see Lemieux and Milligan, 2008). The second question relates to recent debates on the optimal design of tax-bene…t systems and on the e¢ ciency of in-work transfers such as those in place in the UK and the US (see Immervoll et al., 2007). We simulate several counterfactual policies to answer these questions, notably the extension of social assistance to the under-25 year-olds and the introduction of the 2009 welfare system. We …nd that the 2009 system restores work incentives among the over-25 year olds, which is con…rmed by an ex post analysis of what actually happened in 2009. We also …nd that extending the new welfare program to those under 25 years of age should not reduce participation signi…cantly. Hence, it may help to reduce poverty in this group without further weakening their attachment to the labor market. The paper is structured as follows. Section 2 reviews the literature, section 3 presents the institutional background and the data while section 4 explains the empirical strategy. Section 5 reports and analyzes the results while section 6 concludes.

2

Literature 2.1

Structural Labor Supply Models and (Quasi-)Experiments A very large number of policy studies have relied on cross-sectional or panel data and structural models to analyze existing …scal and social policies, to compare them to optimal designs or to help policy making of future redistributive systems (see for instance the discussion in Blundell and MaCurdy, 1999). As argued in the introduction, the internal validity of their predictions to policy changes is not guaranteed. Maybe the main 2 Basically one youth out of four is unemployed. France has the largest youth unemployment in Europe after the four Southern European countries. Youth unemployment and youth poverty are also suspected to have additional external e¤ects like increasing crime (cf. Fougère et al., 2009).

identi…cation issue concerns the fact that omitted variables (e.g., being a "hard working" person) could positively a¤ect gross wage rates and consumption-leisure preferences simultaneously. If variation in gross wages in the population is endogenous to preferences, it can not be directly used to infer potential responses to …nancial incentives (for instance a tax reform). In traditional labor supply models, identi…cation is provided by exclusion restrictions and hinges on the validity of instruments (e.g., Hausman, 1981, for the US or Bourguignon and Magnac, 2001, for France). More recently, the use of discrete choice models allows the incorporation of all nonlinearities and discontinuities introduced by tax-bene…t rules to individual budget curves. Exploiting this variation, together with variation in demographic characteristics, is the basic identi…cation in most models (e.g. Laroque and Salanié, 2002, for France, van Soest, 1995, for the Netherlands). 3 Identi…cation may also be obtained from exogenous variation in tax-bene…t rules across regions (e.g., across US states in Hoynes, 1996) or over time (e.g., Blundell et al., 1998). Time or spatial variation in tax-bene…t rules bring the identi…cation of structural models closer to the quasi-experimental approach. Relatively independently from this, there is a strong history of using natural experiments –notably US/UK tax-bene…t reforms –to quantify labor supply responses. For example, Eissa and Liebman (1996) use a di¤erence-in-di¤erence approach to identify the impact of the US Earned Income Tax Credit (EITC) reform on the labor supply of single mothers. They …nd compelling evidence that single mothers joined the labor market in response to this incentive. Francesconi and Van der Klaauw (2007) use changes in the generosity of the UK Working Family Tax Credit (WFTC) for the same purpose. Using a RD design, Lemieux and Milligan (2008) exploit the fact that, prior to 1989 in Quebec, unattached persons younger than 30 years old received substantially less in welfare payments than similar individuals aged 30 years old or older. They …nd that more generous transfers reduce employment. We exploit a similar discontinuity here, drawing on the RD design detailed in Bargain and Doorley (2011) for the year 1999. It pertains to the fact that childless single individuals under 25 years of age were not eligible for the main social assistance program in France (RMI). 4 Interestingly, this policy feature concerns a group 3 Indeed, two persons with the same gross wage but di¤erent family composition may face di¤erent e¤ective tax schedules. This type of identi…cation is parametric since demographics themselves a¤ect labor supply. It must rely on some implicit assumption of preference continuity across demographic groups (and tax-bene…t functions must be assumed to be su¢ ciently nonlinear to provide credible identi…cation). Interestingly, the discontinuity under investigation in this study plays a similar role. Yet we only require that people just under 25 are identical to people just above 25, other things being equal. 4 In the same line of research, Chemin and Wasmer (2012) use the French labor force survey (LFS) and a triple-di¤erence approach to exploit the fact that the Alsace region in France already had a system of social assistance before the RMI was introduced all over the country. Their estimates of the disincentive e¤ect corroborate those in Bargain and Doorley (2011).

which is rarely studied in the literature. Childless singles are seldom concerned by welfare reforms in the US or the UK (changes in the EITC or the WFTC most often concerned households or single individuals with children). It is, however, important to infer policy responses for this group. Indeed, youth unemployment is a recurrent problem in many OECD countries and in France in particular. It is therefore crucial to evaluate the potential increase in inactivity that may follow an extension of social transfers to the under 25’s, as motivated in the introduction.

2.2

Comparison Comparing methods is a …rst important step. Lalonde’s (1986) landmark paper studied the ability of a number of econometric methods, including Heckman’s selection model, to replicate the results from an experimental evaluation of a labor market program, on the basis of non-experimental data. A systematic comparison of the employment e¤ect of tax-bene…t policies, as measured by ex post evaluation techniques, with those predicted using structural models is essentially absent from the literature. A few studies have recently pursued this comparison, carrying out ex post evaluations using di¤erence-indi¤erence methods (e.g., Blundell, 2006, Cai et al., 2007, Thoresen et al., 2012), regression discontinuity (Hansen and Liu, 2011) or randomised experiments (Todd and Wolpin, 2006). While most of these studies point to the satisfying performance of structural models, others do not (especially Choi, 2011 and Keane and Wolpin, 2007). Most of these studies tend to put structural model predictions beside an ex post evaluation of the same policy e¤ect, and conclude from the comparison on the quality or ‡aws of the structural approach. This is an important and useful exercise. Yet such comparaisons run the risk of treating one or other of the approaches in a biased way. More fundamentally, ex post and ex ante evaluation approaches are complementary, as discussed in the introduction. In particular, the external validity of ex post evaluation methods is hard to test if the parameters of interest are endogenous to policies. In this case, (well identi…ed) structural models may be used for that purpose. This motivates the approach of our study.

2.3

Using (Quasi) Experiment to Identify Structural Models This attempt is not new. A few studies have explored the bene…ts of randomization or quasi-experiments for identi…cation, estimation and assessment of structural models. Imbens (2010) cites an early example, Hausman and Wise (1979), who estimate a model for attrition with data from a randomized income maintenance experiment. Recent examples include Card and Hyslop (2005), who estimate a structural model of welfare participation using experimental data from Canada; Todd and Wolpin (2003), who analyze data from Mexico’s Progresa program; Attanasio et al. (2011) who also analyze the e¤ect of Progresa on education choices; Imbens, Rubin and Sacerdote (2001) who estimate labor supply models, exploiting random variation in unearned income using data from lottery winners and Du‡o, Hanna, and Ryan (2007) who look at the e¤ect of monitoring and …nancial incentives on teacher’s absences. Arguably, there is more room for such work where (quasi) experimental variation is used to improve the identi…cation of structural models. In the absence of pure experimental data, the question of which type of natural experiment is suitable to identify behavioral models arises. In this paper, we suggest using RD as one of the simplest and "cleanest" forms of natural experiments. Using RD designs is, unsurprisingly, popular in the labor supply literature as this strategy provides assignment to treatment that is ‘as good as random’in the neighborhood of the discontinuity (Lee and Lemieux, 2010). Additionally, studying speci…c policy discontinuities, such as the age discontinuity in the RMI, provides a more clear-cut assessment than natural experiments based on policy changes over time, which must control for simultaneous changes in the economic environment. Lemieux and Milligan (2008) actually …nd that commonly used di¤erence-in-di¤erences estimators may perform poorly with inappropriately chosen control groups, notably, groups not placed in the same labor market as the treated. RD analyses provide an advantageous alternative when available, although they must verify if other policies could generate similar discontinuities. These considerations are guiding our approach. We also acknowledge that, even though RD designs may have the highest degree of internal validity among quasi-experiments, they also show strong limitations regarding the possibility of extrapolation to other subpopulations than those used for causal inference. 5 We show that combining RD with a structural behavioral model under minimalist assumptions allows us to perform counterfactual simulations for answering important policy questions.

3

Institutional Background and Data Institutional Background. The policy we study, the RMI, acted until 2009 as a ‘last resort’ bene…t for those who are ineligible for (or have exhausted their right to) other bene…ts in France. We describe here the situation relevant for the year studied, 1999, but the situation for the workless poor is almost unchanged by the 2009 RSA reform that we 5 One recent attempt to do so identi…es causal e¤ects away from the RD discontinuity by conditioning on covariates besides the running variable, in an e¤ort to eliminate the relationship between the running and outcome variable (Angrist and Rokkanen, 2013) The authors, however, admit that it is not always possible to …nd such controls.

describe and simulate below (the RSA simply adds an in-work transfers to the working poor). The RMI can be claimed by any French resident, aged at least 25 (or aged under 25 with a dependent child) and not in education. The RMI is often complemented by means-tested housing subsidies which, together with the RMI, almost lift a workless poor person to the poverty line at 40% of median equivalized income. In practice, entitlement to the RMI does not include any obligation to actively seek work or to train, and it is time unlimited. Denote R the maximum amount of RMI that a single individual can obtain and S(E) the amount of housing subsidy she can obtain as a function of her earnings E. As a simpli…cation, we can de…ne this person’s disposable income as C(E; A) = S(E) + max(0; R t:E):1(A 25) with A denoting age in years and t the taper rate of RMI. Speci…cally around the age cut-o¤ and for someone out of work, we have C(0; 24) = S(0) and C(0; 25) = S(0) + R. With 1999 …gures, C(0; 25) is around EUR 540 per month and 162% more than C(0; 24). After a short period, during which it is possible to cumulate earnings and some RMI, the withdrawal rate t becomes 100%. This con…scatory implicit taxation on earnings is expected to discourage participation, especially among those with weak attachment to the labor market and low wage prospects (see Gurgand and Margolis, 2008, Bargain and Doorley, 2011, Wasmer and Chemin, 2012). The system prevailing after 2009, the RSA, introduces an in-work transfer by permanently reducing the taper rate t from 100% to 38%. The age condition is maintained.

Data. RD estimations must rely on very large samples. With standard survey data, age cells would become too small for meaningful analysis. For this reason, we pursue both the RD analysis and the structural model estimation using the French Census Data for the year 1999. Its coverage is universal and samples of 1=4 of the population are publicly available from INSEE, corresponding to around 14:5 million people. Previous Census, 1982 and 1990, cannot be used since they correspond to years before the introduction of the RMI (1989) or just after (a period with still few recipients). Our data for 1999, however, corresponds to a peak year, with around one million RMI recipients and following a gradual expansion of the scheme from 1990 to 1999 (see Bargain and Doorley, 2011). Note that more recent Census years could be used in principle. Census data collection became annual starting in 2004. However, only 1=5 of the population is interviewed each year, resulting in samples of 1=20 of the population each year. For this reason and because of limited access to these new waves, we …nd it more appropriate to carry out our main analysis on the 1999 Census. Census data for years 2004-2011 is nonetheless used hereafter to study the RSA reform and to check the external validity of our model. The Census provides data on age (in days), employment, type of contract, work duration, marital status and household type. Data on income and receipt of RMI or other bene…ts is, unfortunately, not available. Wage estimations are therefore conducted using the French Labor Force Survey (LFS), a panel survey conducted on an annual basis for the period 1990-2002. For cross-sectional use, the annual LFS is a representative sample of the French population, with a sampling rate of 1=300, providing information on employment, labor income (base salary plus all bonuses and extra time payment and in-kind advantages), education and demographics. Hence, it is possible to calculate hourly wages and estimate wage equations on key variables like age and detailed education categories, as explained below (see also Chemin and Wasmer, 2012).

Selection. The selection is applied to both Census and LFS data. We retain individuals aged 20-30 who are potential workers, i.e., not in education, in the army or living on a (disability) pension. Our analysis focuses on singles without children who live alone. First, childless single individuals represent the main group of RMI claimants. Contrary to couples, whose joint labor supply decision is a relatively complicated problem, they also allow for clear interpretations of the potential labor supply e¤ects. Discarding individuals with children is due to the fact that a parent is eligible for the RMI regardless of age. Finally, and di¤erently from Bargain and Doorley (2011), we consider both female and male singles, as well as all education categories. We also present results for a speci…c group, the high school (HS) dropouts, who have the lowest …nancial gains to work in the short term and, possibly, weaker attachment to the labor market. They represent 22% of the population of young singles aged 25 30 but are over-represented among single RMI recipients in this age range, accounting for 52% of this group.

Descriptive Statistics and Disposable Income Simulations. Both Census and LFS data have comparable de…nitions of the key variables and, in particular, education categories. 6 Table 1 provides descriptive statistics (for LFS, we consider the sole year 1999 or, alternatively, a pool of years 1997-2001). We show that the two selected samples are comparable in terms of demographic and education structures, which gives con…dence in the wage imputation we conduct hereafter. Additional material available from the authors compares the employment-age patterns within the two data sources, using the ILO de…nition in both cases, for people aged 20-30 (see also Bargain and Vicard, 2012). The LFS shows larger employment rates (as re‡ected in the average employment …gures in Table 1), a discrepancy that becomes smaller for older age groups. Given the smaller sample size of the LFS, employment levels by age also show a slightly more erratic pattern 6 Both datasets provide detailed information on quali…cations: junior school diploma (Diplôme National du Brevet, BEPC, or lower secondary level diploma), junior vocational quali…cation certi…cates (Certi…cat d’Aptitude Professionnelle, CAP, and Brevet d’Etudes Professionnelles, BEP), high school diploma (Baccalauréat, or upper secondary level diploma), …rst college degree or advanced vocational degree, higher degrees from universities or business/engineer "Grandes Ecoles".

in these surveys. The overall trends are, however, very similar. For both samples, we also calculate disposable income C(E; A) for each individual in the data, as a function of gross earnings E and age A. 7 This function accounts for social contributions and taxes paid on labor income as well as bene…ts received, which we approximate by very detailed numerical simulation of the French tax-bene…t rules. For our selection of childless single individuals, simulated transfers essentially consist of the RMI (a function of age A) and housing bene…ts. Importantly, Table 1 shows that the levels of disposable income are consistent across the two data sources. Note that we also use our simulations to generate disposable income levels under di¤erent labor supply choices, for the purpose of estimating a structural labor supply model. That is, we simulate disposable income when an individual is not working, C(0; A), or when she is working H hours per week, paid at the wage rate w, C(wH; A). As described below, we also calculate disposable income under hypothetical, counterfactual scenarios where (i) RMI is replaced by the 2009 RSA system, (ii) RMI is withdrawn from the French social system; (iii) the age condition for eligibility is removed; (iv) RMI is replaced by the 2009 RSA and extended to all (age condition removed).

Table 1: Summary statistics for single childless 20-30 year olds in the Census and LFS

All

Proportion of men

Age

Education:

Junior vocational qualification

Highschool

Vocational highschool

Graduate qualification

Dropouts

Work hours

Employment rate

Employment income*

Disposable income (a)*

Disposable income (b)*

Sample size

Under 25

Over 25

Census

## LFS

(pool)

## LFS

Census

## LFS

(pool)

## LFS

Census

## LFS

(pool)

## LFS

0.56 26

0.58 26

0.57 27

0.51 23

0.54 23

0.51 23

0.58 27.5

0.60 27

0.60 27

0.26 0.06

0.13 0.39

0.16 30

0.81 1,534

1,032 1,002 0.25 0.07 0.13 0.37 0.18 32 0.83 1,440 0.25 0.07 0.13 0.38 0.17 26 0.81 1,429 0.25 0.08 0.16 0.32 0.19 31 0.83 1,267 0.26 0.08 0.17 0.29 0.19 31 0.81 1,228 0.24 0.06 0.11 0.41 0.17 32 0.81 1,510 1,136 983 926 0.24 0.05 0.12 0.43 0.15 31 0.82 1,583 1,081 1,054 0.25 0.07 0.11 0.39 0.18 33 0.83 1,510 1,132 0.29 0.07 0.17 0.28 0.19 29 0.79 1,392 893 855 1,190 1,217 202,093 9,986 2,040 53,048 2,833 570 149,045 7,153 1,470 Note: selection of childless single individuals between 20-30 years old. Data sources are the 1999 French Census, the pooled 1997-2001 Labor Force Survey (LFS) and the 1999 LFS. Disposable income is calculated using labor income and the EUROMOD tax-benefit simulator on the data. In Census data, it is calculated on the basis of two alternative wage imputations: (a) using wage estimation on LFS and (b) using wage matching with the LFS. * All monetary variables are expressed in 1999 EUR/month. Employment income excludes zeros. Disposable income is found to be positive for all observations.

7 Capital income is ignored as very small amounts are reported in this age group, especially for the low-educated youths that we focus on.

4 Before turning to the structural model, we discuss how the age discontinuity in the RMI program can be exploited to measure the disincentive e¤ect of this welfare program on labor market participation.

4.1

RD Design We start from Rubin’s framework, denoting Y i the participation binary variable and T i the treatment variable for each unit i. Here, being treated refers to the possibility of availing of the welfare program. As in Lemieux and Milligan (2008), this is simply determined by the age eligibility condition for the program, that is, T i = I(A i A) with A the forcing variable (age) and A the age limit. Age is available in days so that we know exactly what age people are at Census day and their employment status at that date. Consequently, and because the treatment variable is a deterministic function of age, we are in the presence of a “sharp” RD design. We denote Y i1 the potential outcome (participation decision) if exposed to treatment, i.e. if in the eligible age range, and Y i0 the potential outcome otherwise. Considering age in days as a continuous variable, we can make the usual assumption:

Condition 1 (local continuity) The mean values of Y 1 and Y 0, conditional on A, are continuous functions of A at A:

Condition 1 leads to a measure of the average treatment e¤ect of the program at A as captured by any discontinuity at this threshold:

AT E(A) = lim + E(Y 1 =A = A)

## A!A

lim E(Y 0 =A = A): A!A This RD design can be expressed parametrically. In fact, this becomes necessary when the forcing variable is discrete, which is a more reasonable framework when age is expressed in years or quarters: This is a more appropriate setting since it is not clear when the potential labor supply response should occur (after turning 25). 8 Also, age cells would be very small and would display a very erratic pattern if age is expressed in days. A discrete dependent variable means that we cannot compare observations "close enough" on both sides of the cuto¤ point to be able to identify the e¤ect. Hence, we rely on various parametric functions of the forcing variable A in order to balance the usual tradeo¤ between precision and bias (Lee and Card, 2008). Consider the regression model with 8 Using panel administrative data and a very similar setting for Denmark, Jonassen (2013) shows that transitions in and out of social assistance driven by the age condition take place within 26 weeks.

Y i denoting the propensity to be employed for individual i:

Y i = i + i:

(A i) + i:I(A i (1)

A) + " i:

The model is easily estimated by logit or probit techniques, with employment Y i = 1 for those with Y i > 0 and 0 otherwise. Alternatively, a simple linear probability model can be used by replacing Y i by Y i in (1) (see Lemieux and Milligan, 2008). The e¤ect of age A i on the outcome variable is captured by a smooth function (A i) and by T i = I(A i A). Under the identi…cation assumption of () being a continuous function, i.e. the parametric version of Condition 1, the treatment e¤ect is obtained by estimating the discontinuity in the empirical regression function at the point where the forcing variable switches from 0 to 1. Note that coe¢ cients vary linearly with a set Z i of individual characteristics other than age (gender, education) and, so, are written with the subscript i. In particular, we may have (observed) heterogeneity in the treatment e¤ect, with 0 1 i = i + i Z i. In particular, because of their weaker attachment to the labor market, HS dropouts may behave di¤erently from other education groups so that we must di¤erentiate the employment e¤ect for HS dropouts from those with a degree. 9 At this stage, it becomes clear that the RD design allows only limited extrapolation. The employment elasticity of social assistance parameters can be calculated. For instance, denoting Y the mean employment rate and focusing on the maximum bene…t level R,

## =Y

we can derive the employment elasticity of a change in social assistance dY (around dR=R:05 in Bargain and Doorley, 2011, and:04 in Lemieux and Milligan, 2008). Yet it is di¢ cult to say much more. For instance, we cannot extrapolate further away from the discontinuity to answer our initial question regarding the employment e¤ect of extending social assistance to those under 25. At a minimal cost, putting structure on the RD design shall allow us to do so.

4.2

Adding Structure General Model. The interpretation of a potential disincentive e¤ect of social assistance in the above RD design coincides with the rationality assumed in static labor supply models (for instance, van Soest, 1995). In their discrete version, these models are based on the assumption of agents choosing the weekly worked hours option j = 1;:::; J in a discrete set of J common work durations (for instance non-participation, part-time, full-time and overtime). In this setting, we can write utility at choice j as:

U ij = U i (H j; C(w i H j; A i)

F i:1(H j > 0)) + 9 ij (2) We refrain from using more detailed education categories for comparability with the next model, as explained further below.

with disposable income C(w i H; A i) (equivalent to consumption in this static framework) and hours worked H j. Disposable income is reduced by a level F i for positive hours choices. This term may capture …xed costs of working as well as the cost of job search on the labor market, so that it must vary with individual characteristics including age. The deterministic utility levels are completed by i.i.d. error terms ij, assumed to follow an extreme value type I (EV-I) distribution and to represent possible observational errors, optimization errors or transitory situations. Because it accounts for the full tax-bene…t rules in function C, this structural model is broadly used for policy analysis (see Blundell and MaCurdy, 1999). As previously discussed, identi…cation often relies on the nonlinearity of this function or time/spatial variation in the tax-bene…t rules. In our setting, we originally use the age condition in social assistance eligibility, creating exogenous variation in …nancial incentives, as the key source of identi…cation. Since this discontinuity changes only the …nancial conditions between working and not working, we shall focus on the participation margin. As discussed in the concluding section, the more general model presented in equation (2) could be identi…ed using our approach but would require more variation (for instance other discontinuities a¤ecting …nancial gains between full and part time work).

Speci…cations and Exclusion Restriction. We complete the speci…cation in the general case. Translog or quadratic utility functions in hours H j and consumption C are typically used for function U i (see Blundell and MaCurdy, 1999). Bargain (2006) and van Soest et al. (2002) show, however, that it is not possible to identify preferences from other structural components like …xed (or variable) costs of work, unless strong parametric assumptions are made. Instead, we opt for a ‡exible speci…cation where preference parameters vary with the choice j:

U ij = a ij + g ij: (A i) + b ij:C(w i H j; A i) + c ij:C(w i H j; A i) 2 + ij:

(3) In this way, the "disutility" of work or other components like work costs are speci…ed through choice-speci…c terms a ij and g ij and, hence, are not forced to vary linearly or quadratically with H j as in standard functional forms. The same is true for interaction between hours and consumption, with coe¢ cients b ij and c ij. Bargain (2006) shows that this speci…cation nests the standard quadratic utility function used in many applications and better …ts the data. In addition, coe¢ cients in (3) vary linearly with several tasteshifters (gender, education) and possibly random terms for unobserved heterogeneity. While it is obvious that i, in the reduced form equation (1), is identi…ed at the age discontinuity and cannot, itself, vary with age, we must impose such a simple restriction in the structural equation (3):

Condition 2 (exclusion restriction) Marginal utility of consumption b ij does not vary with age.

In a standard labor supply model, this means that one of the usual taste shifters, age, is left out of some of the coe¢ cients. This exclusion restriction is debatable, yet it is obviously the price for identi…cation based on the age discontinuity and it is totally consistent with the reduced form RD equation. Moreover, age a¤ects the utility function in other, relevant ways: (i) a direct e¤ect (A i ), entering the utility function in an (additive) separable way and re‡ecting how age changes work preferences, …xed costs of work or search costs (these three components are usually not identi…ed from each other, see van Soest et al., 2002) and (ii) an indirect e¤ect through …nancial incentives C, since age is a determinant of both wages w i and the tax-bene…t function C(; A i ).

Participation Model. With this setting, we now focus on the participation margin. 10 The choice of working full-time (j = 1) rather than staying out of the labor market (j = 0) depends only on the di¤erence Y i = U i1 U i0 so that only the coe¢ cients on consumption are identi…ed while the other ones are normalized to zero for the non-working option (a i0 = g i0 = 0). The quadratic term in consumption, in equation (3), is not necessary as we model participation only. The …nal model is very close to the speci…cation used in Laroque and Salanié (2002). Dropping subscript 1 from coe¢ cients a i1 and g i1, we can write the propensity to be employed as:

Y i = a i + g i: (A i) + b 1i:C(w i H 1; A i) b 0i:C(0; A i) + i (4) with i = 1i 0i. The model is now very similar to the RD model in equation (1), with the same constant and smooth function of age (A i ); plus a term capturing the discontinuity e¤ect. The main di¤erence, however, is the structure put on the latter. The treatment e¤ect, i.e. the age condition of the RMI, a¤ects individual participation decisions through their …nancial incentives to work, now measured by the distance between disposable income when employed, C(w e i H 1; A i ), and disposable income when out of work, 11 C(0; A i ). By focusing on a speci…c group of the population, i.e. childless singles, we rule 10 While the main reason for this choice is a clean identi…cation (i.e. the age discontinuity only a¤ects this margin), other motivations are given in the literature. Laroque and Salanié (2002) estimate female participation on French data and justify this focus by the small variability in work hours in France. Also, participation is the main margin of adjustment in the short-run (in particular, labor market frictions ensure that people cannot adjust their work duration beyond the mere choice to participate or not, cf. Chetty et al., 2011). In our application, we set H 1 to 39 hours per week, the institutionally set full time option in France in 1999. 11 In practice, as can be seen in equation (4), we do not force the model to depend on the exact di¤erence between these two income levels. Instead, we let them freely a¤ect the probability of employment. Indeed, out most of the usual sources of identi…cation stemming, as explained above, from the nonlinearity of tax-bene…t systems combined with variation in demographic composition. The identi…cation of the model relies on the same behavioral assumption as in the RD design: (statically) optimizing agents decide upon their labor supply based on …nancial incentives, and those aged 25 have lower incentives to work than similar persons aged 24. As in the reduced-form model, coe¢ cients vary with gender and education. The latter is simply a dummy for HS dropouts: in addition to lower wage prospects, which should be re‡ected in wages w i, people with only compulsory education may have lower attachment to the labor market than individuals with a degree (see Be¤y et al., 2006; Gurgand and Margolis, 2008). In a supply-side model, this can be rationalized in the form of larger search costs, i.e. participation costs (see van Soest et al, 2002). Notice that we refrain from using more detailed education categories for identi…cation purposes. Indeed, detailed education is the main information identifying wages and, hence, cannot also be used in preferences. This exclusion restriction is common in the literature (van Soest et al., 2002). We also add unobserved heterogeneity in coe¢ cient b 1i, that is:

b 1i = b 01i + b 11i Z i + b 21i u i where u i is a random, normally distributed term u i (with zero mean and variance 2 u ). This term corresponds to the unobserved preference for work, so that the total distribution of the model is a mixture of a normal and an EV-I distribution. In this case, the model can be estimated by simulated maximum likelihood, as explained below.

4.3

Wages, Estimation Method and Discussion Wage Imputation: Estimation and Matching. The central component of …nancial gains to work in equation (4) is the wage rate. When estimating structural models, it is standard to proceed in two stages, …rst with the estimation of a wage equation to predict wages for non-workers, then with the estimation of the labor supply model. We specify the wage equation as:

log w i = (A i) +:EDU C i +:Z i + i + i (5) assuming a normally distributed residual i and including the following explanatory variables: a smooth function of age (A i ), the set of detailed education categories EDU C i and additional controls Z i (gender). The traditional labor supply literature has pointed to two issues relating to wage endogeneity. First, hourly wages may be partly determined individuals may value additional income when not working in a di¤erent way from in-work earnings, simply because of di¤erent marginal utilities of consumption at the two labor supply points (but also for other reasons like …xed costs of work or the stigma e¤ect when living on welfare).

by omitted unobservable variables (being hard working) which are associated with preferences, as discussed above. We follow the standard Heckman approach and introduce an inverse Mills ratio i, estimated on the basis of a reduced form employment probability. The latter includes the age function (A i ), controls Z i and disposable income at zero hours C(0; A i) as an instrument, relying again on the discontinuity at age 25 for identi…cation. Second, calculated as earnings divided by worked hours, hourly wages may be contaminated by the same measurement error as those contained in worked hours, the so-called division bias. To avoid this bias, we predict wages for all observations, workers and non-workers, as suggested by Eklof and Sacklén (2000). Predicting for all makes it less of a concern to use one dataset for estimation (LFS) and another for predictions (Census), as long as (i) the second data source provides accurate information on wages, (ii) both datasets contain the same variables, with identical de…nition. As argued above and in Chemin and Wasmer (2012), the LFS is a robust dataset that contains detailed information on earnings and that can be used for reliable wage estimation. Moreover, all variables, and in particular the education categories in vector EDU C i, are available in both datasets according the exact same de…nition. Thus we use estimates of equation (B.1) to predict wages for all individuals in the Census, drawing wage residuals i in a normal distribution with zero mean and using their estimated empirical variance. Since workers cannot receive wages below the minimum wage, in principle, we discard i draws leading to wages below this wage ‡oor for individuals in work in the Census. The normality assumption may be a poor approximation for the speci…c population studied (childless single aged 20-30). Hence, we also suggest an alternative imputation method based on a matching approach. That is, for each individual in the Census, we pick a wage value randomly in his/her age-gender-education group in the LFS. Over a large number of draws, this is equivalent to imputing the conditional mean wage of a given cell plus an error term drawn from the empirical distribution (rather than from a normal distribution). Once again, we discard draws that lead to imputed wages below the minimum wage for those who are observed working in the Census, while those who do not work can earn any wage in the random distribution.

Estimation of the Structural Model. Model (4) is estimated by simulated maximum likelihood. Under the assumption that error terms ij follow an EV-I distribution, the (conditional) probability for each individual of choosing a given alternative has an explicit analytical solution, i.e., a logistic function of deterministic utilities at all choices. This multinomial logit model boils down to a simple logit in our case. Because the model is nonlinear, the wage prediction errors e i are taken explicitly into account for a consistent estimation. The unconditional probability is obtained by integrating out the disturbance terms u i and i in the likelihood. In practice, this is done by averaging the conditional probability over a number of draws for these terms, recalculating disposable income each time. 12 Non-employment and Demand-Side. Non-employment can be rationalized by (i) low …nancial gains to work (low i or high C(0; A i )); (ii) high preferences for leisure (low u i ); (iii) classic unemployment (productivity below the minimum wage); (iv) "other" nonemployment corresponding to frictional or cyclical unemployment. Our modeling of (i) and (ii) is very similar to Laroque and Salanié (2002). For (iii), we cannot estimate the wage equation jointly with the employment model in order to account for the probability of being rationed in the individual likelihood. Hence, we simply assume that workers cannot be paid below the minimum wage, as explained above, while non-workers may have such low productivities. For (iv), we take a i +g i: (A i) as a non-identi…ed combination of supplyside factors (work disutility or work costs) and demand-side factors (job search costs), as previously explained. 13 In Bargain and Doorley (2011), we show that HS dropouts and those with a basic vocational training have similar …nancial gains to work but the latter show no drop in employment at 25. This indicates that those with basic quali…cations have more attachment to the labor market, i.e lower job search costs. 14 5 5.1

Results

Basic Estimation Results and Comparisons We …rst present the estimations of the RMI e¤ect on youth employment in France using RD versus predictions of the participation model. Next, we provide further checks of the internal and external validity of the model. Other results are reported in Appendix B. In particular, wage imputation using both estimation and matching appears to reproduce reasonable estimates of the wage distribution in the Census data (see Appendix B.1). We also discuss estimates of both RD and structural models in detail (Appendix B.2).

RD Estimates. We …rst present a graphical analysis of the RMI e¤ect. In Figure 1, we plot raw employment rates by age, along with 95% con…dence intervals using our 12 A computationally convenient approach consists in using sequences of Halton draws, as suggested by Train (2003). This allows us to reduce the number of draws to a tractable level (r = 10). 13 See van Soest et al. (2002) for a similar interpretation of involuntary unemployment in a supply-side framework. For a more structural modeling of the "other" non-employment, based on similar exclusion restrictions, see Laroque and Salanié (2002). 14 Note that under the assumption stated in condition 2, this (reduced-form) part of the model is not RMI-dependent, so that our policy simulations should not be biased. Arguably, however, general equilibrium e¤ects may invalidate this statement.

selected sample from the 1999 Census. We distinguish between the full sample and the sub-group of HS dropouts. The graphical representation of the discontinuity suggests a very small drop in employment at age 25 when all groups are taken into account. For HS dropouts, however, there is a signi…cant drop, of around 4 percentage points (ppt). RD estimations of equation (1) con…rm a magnitude of i in a range between 3:6 and 5:8 ppt for HS dropouts over all speci…cations of the model (age in years or quarters, () as quadratic, cubic, quartic or quadratic spline). The e¤ect expressed in percentage points can be divided by the employment rate at age 24 for the HS dropout (67:7%) to give the proportion of people concerned by the disincentive e¤ect at the discontinuity, i.e., between 5:3 8:6% in this group. This order of magnitude is similar to estimates in Bargain and Doorley (2011) who focus on men only. An important aspect is whether results are sensitive to the distance of observations from the discontinuity. The parametric estimation provides global estimates of the regression function over all values of the forcing variable, while the RD design depends instead on local estimates of the regression function at the cuto¤ point. Thus we have also checked whether the treatment e¤ect varies in a linear spline model for an increasingly small window around age 25. We …nd very stable estimates, which are additionally con…rmed by non-parametric estimations with varying bandwidths. Finally, we compare these results to the changes in employment at age 25 for a number of placebo control groups not a¤ected by the discontinuity. The …rst group is uneducated workers with children, i.e. not a¤ected by the age condition. We …nd no signi…cant employment change at 25 for this group. A second set of comparison groups consists of uneducated workers in 1982 (before the introduction of the RMI) and in 1990 (only one year after its introduction, i.e., a time when the program was not yet well publicized and concerned a much smaller population). As shown in Figure 2, there is no sign of a discontinuity at 25 for these two placebo groups.

Dynamics. The RD design in the case of an age-based discontinuity is a special case of the standard RD design (Lee and Lemieux, 2010) as assignment to treatment, i.e., eligibility for the RMI, is inevitable (all subjects will eventually age into the program). Two issues arise in this case. Firstly, the discontinuity should be interpreted as the combined e¤ect of all factors that switch on at the threshold. An extensive examination of any other potential in‡uences on employment at age 25 is undertaken by Bargain and Doorley (2011), con…rming that there is no other factor at work at this age threshold, except the RMI. Secondly, because treatment is inevitable with the passage of time, individuals may fully anticipate the change in regime and adjust their labor market behavior before the threshold. In this case, optimizing behavior, in anticipation of eventual eligibility for the RMI, would accentuate observed e¤ects. We believe that this is implausible for a number of reasons (see further discussion in Bargain and Doorley, 2011). First, it seems unlikely Figure 1: Employment Rate of Childless Singles and Discontinuity (Census 1999).8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 20 22 24 age

Quadratic trend 26 28 30 age 95% confidence interval

Quadratic trend 95% confidence interval Figure 2: Employment Rates of Childless Singles between 1982 and 1999 (Census).55

Employment rate.6.65.7.75.8

HS dropouts 20 22 24 26 28

Age

Employment rate 1999

Employment rate 1982

Note: kernal-weighted local polynomial smoothing used

Employment rate 1990 30 that the group which displays the largest response to the RMI, HS dropouts, would be fully aware of the bene…t rules and, thus, work more until they turn 25 in order to be able to drop out of the labor market at age 25. Second, for a 20-25 year old, eligibility for the RMI will certainly happen at age 25 but may also happen if the individual has a child in the meantime or cohabits with somebody who is eligible. We, however, observe no accelerated fertility or cohabitation rates before age 25, indicating limited anticipation e¤ects in this respect. Third, we do …nd evidence that the share of HS dropouts on short-term contracts decreases discontinuously after age 25, indicating that, rather than working more or harder, highschool dropouts are lingering in precarious activities until they become eligible for the RMI, at which point the cost of …nding another short-term contract may seem large when a minimum income is guaranteed anyway. Finally, a graphical inspection of the employment trends of 20-25 year olds in 1982 (before the introduction of the RMI), in 1990 and in 1999 shows little evidence of a time change in employment trends before the discontinuity (see Figure 2). The overall di¤erence in employment rates between 1990 and 1999 is partly due to the steep increase in youth employment from the 1990’s onwards and partly due to the fact that HS dropouts represent a smaller (and more negatively selected on the labor market) proportion of the overall population now than they did in the 1980’s and 1990’s.

Estimates of the RMI Employment E¤ect. Table 2 compares the predictions of the RMI employment e¤ect from both RD design and the structural model, relying on a cubic function of age in both cases. The …rst columns report the actual employment rates at 24 and 25 years of age. The di¤erence is 0:7 ppt in the broader group compared to 3:4 ppt among HS dropouts. In the RD framework, accounting for the age trends to extrapolate towards the threshold, we obtain treatment e¤ects of 1:6 ppt and 3:9 ppt for these two groups respectively. Both e¤ects are statistically signi…cant and con…rm a substantial negative e¤ect of the RMI on singles. The e¤ect is stronger for men, even if not signi…cantly so. Turning to the behavioral model, we …nd slightly underpredicted rates of participation compared to actual ones. Nonetheless, the employment e¤ect of the RMI predicted by the model is well in line with the RD results, i.e. 1:5 and 3:9 ppt for the whole selected sample and for HS dropouts respectively (see Appendix A on how to calculate the treatment e¤ect in both cases). We observe slightly more homogenous results across gender groups for the whole sample compared to RD estimates. For HS dropouts, however, the model predicts the slightly larger e¤ects for men in this speci…cation well. The e¤ects are not signi…cantly di¤erent from those of the RD approach. 15 Note that a good …t at the cuto¤ was expected, since the behavioral model simply translates the 15 Alternative speci…cations of the smooth function of age (quadratic, quartic) do not a¤ect these conclusions qualitatively, and quantitative di¤erences are relatively small (see Table 5).

discontinuity e¤ect from a reduced-form to an income e¤ect speci…cation in the objective function. Performances of the model regarding predictions of employment rates further away from the cuto¤ or of policy reforms are less guaranteed –we check them in the next subsection. A …nal aspect we need to investigate here is whether the basic results are sensitive to the distribution of wages. We apply the alternative way to impute wages as discussed above, i.e. the matching procedure. For each observation in the Census, we simply draw a wage among the LFS observations within the same age-education-gender cell. Table 3 shows that with this imputation technique, the model predicts employment levels better than with the previous approach based on wage estimation. In contrast, it tends to underpredict slightly the employment e¤ect of the RMI for the HS dropouts and to attenuate di¤erence between gender. Nonetheless, estimates of the RMI e¤ect are close enough to previous results and to RD estimates, i.e. a drop of 1:5 ppt overall and 3:4 among HS dropouts. We provide an interpretation of these results in the next sub-section.

Table 2: Employment E¤ects of the RMI: RD vs. Structural Model

Actual Participation Rates

Predicted Part. Rates (Model)

RMI Effect (RD)

RMI Effect (Model)

Age 24

Age 25

Diff.

Age 24

Age 25

Diff.

Estim.

s.e.

Estim.

s.e.

All education groups

All

Male

Female 82.9% 83.4% 82.4% 82.2% 83.3% 80.8% -0.7 -0.1 -1.6 81.7% 82.8% 80.6% 81.2% 82.0% 80.2% -0.6 -0.8 -0.4 -1.6 -0.7 -2.5 (0.4) (0.6) (0.7) -1.5 -1.7 -1.3 (0.5) (0.5) (0.6)

HS Dropouts All Male Female 67.7% 70.5% 63.1% 64.3% 66.5% 60.8% -3.4 -4.0 -2.3 65.8% 68.0% 62.3% 62.6% 64.5% 59.6% -3.2 -3.5 -2.7 -3.9 -4.2 -3.4 (1.4) (1.8) (2.4) -3.9 -4.1 -3.6 (1.5) (1.6) (1.8) All figures are based on the 1999 Census data. Participation rates are predicted using the structural behavioral model (Model), with wage estimated from the Labor Force Survey. The employment effect of the RMI is estimated using the RD design (RD) or predicted using the behavioral model (Model). Both approaches rely here on a cubic age specification. Estimates significant at the 1% (5 or 10%) level in bold (italic). Standard errors are reported in brackets.

5.2

Checking for Internal and External Validity We now check the internal and external validity of our model, combining identi…cation from a natural experiment (the discontinuity) and standard behavioral assumptions (optimizing behavior based on …nancial incentives in a static framework). Internal validity refers here to the …t to the data while external validity refers to the ability of the model to correctly perform out-of-sample predictions or predictions of future policy scenarios.

Table 3: Employment E¤ects of the RMI: RD vs. Structural Model (Matched Wages)

Actual Participation Rates

Predicted Part. Rates (Model)

RMI Effect (RD)

RMI Effect (Model)

Age 24

Age 25

Diff.

Age 24

Age 25

Diff.

Estim.

s.e.

Estim.

s.e.

All education groups

All

Male

Female 82.9% 83.4% 82.4% 82.2% 83.3% 80.8% -0.7 -0.1 -1.6 82.4% 83.3% 81.4% 81.9% 82.8% 80.8% -0.5 -0.5 -0.6 -1.6 -0.7 -2.5 (0.4) (0.6) (0.7) -1.5 -1.5 -1.6 (0.5) (0.5) (0.6)

HS Dropouts All Male Female 67.7% 70.5% 63.1% 64.3% 66.5% 60.8% -3.4 -4.0 -2.3 66.5% 68.5% 63.2% 63.6% 65.9% 59.8% -2.9 -2.6 -3.5 -3.9 -4.2 -3.4 (1.4) (1.8) (2.4) -3.4 -3.3 -3.6 (1.5) (1.6) (1.8) All figures are based on the 1999 Census data. Participation rates are predicted using the structural behavioral model (Model), with wage matching from the Labor Force Survey. The employment effect of the RMI is estimated using the RD design (RD) or predicted using the behavioral model (Model). Both approaches rely here on a cubic age specification. Estimates significant at the 1% (5 or 10%) level in bold (italic). Standard errors are reported in brackets.

Internal Validity: Employment Rates at Various Ages. A …rst check of the performance of the structural model is whether the model can predict employment rates well at all age levels. Figure 3 reports actual employment levels, predicted employment rates and con…dence intervals at all ages (using speci…cations with a cubic function of age). We distinguish results for the whole selection and for HS dropouts respectively. The model actually shows a good …t for the entire selection of years around the discontinuity, which con…rms the role of the discontinuity in the identi…cation of the model. For almost all age groups, actual employment rates are in the predicted con…dence intervals. Figure 4 shows the same type of result when matching is used for wage imputation. As commented above, employment rate predictions are even better in this case. The reason for this is that wage matching captures the actual wage distribution better, as shown in Appendix B.1. This approach does not impose normality on wage errors nor any speci…c functional form on the impact of education or age on wages. As a result, the predicted employment-age pattern in this case lines up very closely with the actual one, as can be seen in Figure 4. Yet, the wage estimation technique, although less ‡exible, is more suited to the RD approach in the sense that it imposes the same smooth function of age on wage predictions (the full model underlying Figure 3 thus depends on a cubic function of age in both preferences and wage determinants). Hence, it conforms more with the continuity assumption imposed through function and leads to a more continuous employment rate pro…le, as seen in Figure 3. As a result, while being less accurate in terms of employment level predictions, it is more accurate in its prediction of the employment drop at 25. The important conclusion is that, despite this trade-o¤, both wage imputation techniques (and the various speci…cations of ) lead to similar conclusions. This is also true for the series of simulations to come. This gives us con…dence in the extrapolation we perform next using the structural model.

Figure 3: Employment Rate of Childless Singles: Fit of the Structural Model.8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 age

Predicted empl.

20 22 24 26 28 30 age

Actual empl.

Predicted empl.

Predicted empl. 95% CI

Actual empl.

Predicted empl. 95% CI Out-of-sample Prediction of the RMI E¤ect. We now rely on a cross-validation sample to provide a …rst check of the external validity of the structural model. We rely on two sub-samples for the same year of data (1999). We estimate our base model on a random half of the selected sample (estimation sample), and use estimates to predict employment rates and treatment e¤ect on the other half (holdout sample). 16 Results are reported in Table 4. The …rst observation is that the treatment e¤ect on the holdout sample, measured by RD, is very similar to what was found for the full sample (1:1 and 3:5 for the whole selection and for HS dropouts respectively). The participation model seems to perform relatively well, even if treatment e¤ects are larger than the "true" response as measured by the RD (2:0 and 4:1 for the whole selection and 16 The advantage of such a strategy (see also Keane and Wolpin, 2007), compared to using another year of data, is that we do not need to control for time changes that may a¤ect the sample and which could be di¤erent for the "treated" and the "control" groups (the main di¢ culty in di¤erence-in-di¤erence studies). However, a more advanced validation should rely on a “holdout sample” which would di¤er from the sample used in the estimation and whose policy regime is well outside the support of the data. For instance, we could simulate the withdrawal of the RMI and compare to the actual pre-RMI situation using 1982 Census data. This seems too old, however, to be used as a check for the simulation of a no-RMI situation in 1999. The next paragraph suggests another validation exercise of this type.

Figure 4: Employment Rate of Childless Singles: Fit of the Structural Model (Matched Wages).8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 age

Predicted empl.

20 22 24 26 28 30 age

Actual empl.

Predicted empl.

Predicted empl. 95% CI

Actual empl.

Predicted empl. 95% CI for HS dropouts respectively). In line with the RD results, the model points to larger responses by single men compared to single women, both in the full sample and among HS dropouts. It predicts the RMI e¤ect for men very precisely and seems to overpredict responses for women, yet both RD estimates and model predictions agree that the e¤ect is not signi…cant for the latter.

External Validity: Predicting the E¤ect of the 2009 Reform. We now attempt to compare model predictions of policy reforms with what e¤ectively happened after these reforms. We …rst simulate the 2009 reform, which essentially reduced the withdrawal rate t from 100% to 38%, introducing an in-work-bene…t component. This new minimum income is called the Revenu de Solidarite Active (RSA). The simulation of the RSA reform in Figure 5 shows a small positive e¤ect on the over-25 employment rates for the whole selection. For the group of HS dropouts, it has a larger positive e¤ects on employment rates, of about 3 ppt, which fades towards age 30. For the under-25, note that there is no e¤ect since the age condition also applies to the new scheme. Focusing on HS dropouts, we report the employment e¤ects of the RMI (using RD and model predictions) and of the RSA (using model predictions) in the left panel of Table 5. For the RMI, we observe slightly larger e¤ects with the quadratic and the quartic functions of age, both in the RD Table 4: Employment E¤ects of the RMI: using Cross-validation Samples

Actual Participation Rates

Predicted Part. Rates (Model)

RMI Effect (RD)

RMI Effect (Model)

Age 24

Age 25

Diff.

Age 24

Age 25

Diff.

Estim.

s.e.

Estim.

s.e.

All education groups

All

Male

Female 82.8% 83.6% 80.9% 82.3% 83.8% 80.2% -0.5 0.2 -0.7 81.8% 82.6% 80.9% 81.0% 81.7% 80.2% -0.8 -0.9 -0.7 -1.1 -1.7 -0.4 (0.6) (0.7) (0.7) -2.0 -2.1 -1.8 (0.7) (0.8) (0.8)

HS Dropouts All Male Female 66.8% 70.9% 59.9% 64.1% 65.9% 61.2% -2.7 -4.9 1.3 65.7% 67.3% 63.0% 62.6% 64.0% 60.3% -3.1 -3.3 -2.7 -3.5 -4.1 -2.5 (1.6) (1.7) (1.8) -4.1 -4.2 -3.9 (2.1) (2.2) (2.5) All figures are based on a 50% sample of the 1999 Census data. Participation rates are predicted using the structural behavioral model (Model). The model is estimated on the other 50% sample (with wage estimated from the Labor Force Survey). The employment effect of the RMI is estimated using the RD design (RD) or predicted using the behavioral model (Model). Both approaches rely here on a cubic age specification. Estimates significant at the 1% (5 or 10%) level in bold (italic). Standard errors are reported in brackets.

and in the structural model. As previously discussed, however, estimates are in a range of reasonably similar magnitude, pointing to a disincentive e¤ect of the RMI between 5:6 and 4:1 for men and 5:1 and 3:6 for women according to the behavioral model (comparing the two …rst columns, we also con…rm that RD and model predictions are very close in all speci…cations). The RSA employment e¤ect at age 25 (third column) is much smaller and not signi…cantly di¤erent from zero in most cases, con…rming the re-incentivizing e¤ect of the in-work component. The di¤erence between RMI and RSA e¤ects points to a correction of the inactivity trap by around 3 ppt thanks to the RSA reform, with slightly larger e¤ects for women (between 3:5 and 3:9) than for men (between 2:6 and 3). In the right panel of Table 5, we compare these results with RD estimates of the RMI e¤ect before the actual reform took place (we pooled Census data for years 2004-2008 to obtain a sample size similar to the Census 1999, as explained in the data section above) and after it took place (we pool years 2010 and 2011, excluding 2009 since the reforms took place in the middle of that year). Results are very similar to the model prediction. First, despite time changes in labor market conditions between 1999 and 2004-2008, we observe a similar disincentive e¤ect of the RMI before the reform. It is slightly smaller than in 1999, i.e. between 3:6 and 2:6 overall. Then, the two years under the RSA system show no disincentive e¤ect at the cuto¤. Finally, the di¤erential e¤ect between the two welfare regimes is positive and very close to our simulation, i.e. between 2:8 and 3:4 overall. RD estimates also con…rm a slightly larger re-incentivization of the RSA for women compared to men. The e¤ect is, unfortunately, not statistically signi…cant in most speci…cations because of the smaller sample used for the RSA regime, which results in a lack of power. 17 Notwithstanding, the proximity with our model prediction is reassuring –even if it is only suggestive evidence –about the external validity of the model and of the natural experiment underlying model identi…cation.

Figure 5: Counterfactual Employment Simulations: 2009 In-Work Bene…t Reform (RSA).8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 20 22 24 age 95% CI base 5.3 26 28 30 age 95% CI RSA reform 95% CI base 95% CI RSA reform

Counterfactual Simulations Finally, we use our behavioral model to predict important counterfactual policy scenarios. We provide results using the cubic speci…cation of age and the wage estimation approach. Results with other speci…cations of are very similar (available from the authors) as are results based on wage matching (reported in Appendix C).

Policy Simulation: Abolishing the RMI. Our …rst simulation examines the e¤ect of abolishing the RMI. As expected, Figure 6 shows that removing the RMI would increase participation just over the 25-year-old threshold. This scenario is certainly not a political option but an interesting benchmark for comparison. In particular, comparing with Figure 5, we see that the RSA reform simulated earlier has almost the same relative e¤ect on employment as removing the RMI, i.e. it brings the employment level of HS dropouts 17 As explained in the data section, Census data since 2004 is collected on an annual basis and for 1/5 of the population each year. Our RD estimates for the RSA thus rely on a sample for years 2010-2011 corresponding to 2/5 of the size of the sample used for our main analysis.

Table 5: External Validity of the Structural Model: Employment E¤ect of the RSA Reform

Census 1999

## 1999 RMI

RMI effect (model)

RSA effect (model)

Diff.

## 2004-08 RMI

effect (RD)

## 2010-11 RSA

effect (RD)

Diff.

(1) (2) (3) (3) -(2) (4) (5) (5) -(4) -5.8 (1.1) -5.8 (1.9) -4.2 (1.8) -5.4 (1.4) -5.6 (1.4) -5.1 (1.7) -2.5 (1.4) -3.0 (1.4) -1.6 (1.7) 3.0 (2.0) 2.6 (2.0) 3.5 (2.4) -3.6 (1.0) -3.1 (1.3) -5.0 (1.5) -0.8 (1.5) -0.6 (2.2) -1.2 (4.9) 2.8 (1.4) 2.6 (2.0) 3.8 (4.2) -3.9 (1.4) -4.2 (1.8) -3.4 (2.4) -3.9 (1.5) -4.1 (1.6) -3.6 (1.8) -1.0 (1.5) -1.5 (1.6) -0.1 (1.8) 3.0 (2.2) 2.6 (2.2) 3.5 (2.5) -2.6 (1.6) -2.2 (1.9) -3.5 (1.9) 0.8 (2.3) 0.8 (3.1) 1.3 (6.1) 3.4 (2.1) 3.0 (2.8) 4.8 (5.2) -4.5 (1.6) -6.2 (2.0) -2.2 (2.6) -4.6 (1.8) -4.8 (1.8) -4.4 (2.0) -1.3 (1.8) -1.9 (1.8) -0.4 (2.0) 3.3 (2.5) 3.0 (2.5) 3.9 (2.9) -2.9 (1.5) -2.6 (1.9) -3.7 (1.9) 0.2 (1.4) 0.2 (2.4) 0.2 (5.6) 3.0 (2.1) 2.8 (2.3) 4.0 (4.8)

Age specification effect (RD)

Q u ad ratic

All

Men

Women

Cu b ic

All

Men

Women

Q u artic

All

Men

Women

Census 2004-2011 Selection: childless single individuals aged 20-30, HS dropouts. Estimates represent the employment effect of RMI/RSA according to RD design (RD) or to predictions of the structural model (model). Simulation of a shift from RMI to RSA using the model estimated on 1999 Census data is compared to the actual policy chance (replacement of RMI by RSA in 2009). Both RD and structural model rely on alternative smooth functions of ages (quadratic, cubic or quartic). Standard errors in brackets.

aged 25-30 to around 65 67%. Even if more costly, the RSA scheme is certainly more politically acceptable and was the path taken by the French government in 2009.

Figure 6: Counterfactual Employment Simulations: Abolishing the RMI.8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 20 22 24 age 95% CI base 26 28 30 age 95% CI abolish RMI 95% CI base 95% CI abolish RMI Policy Simulation: Extending the RMI to the Youth. Youth unemployment is a severe issue in France like in several EU countries. It has received renewed attention recently as it becomes even more accentuated in a recessionary context. As the young are more at risk of unemployment and less likely to have made enough contributions to claim unemployment bene…t, the RMI can be an important source of income for them. Currently, their limited access to welfare programs results in very large poverty rates, as discussed in the introduction. This raises the question of extending the RMI to those under 25 years of age. Of course, this strategy runs the risk of increasing welfare dependency by fostering it at a younger age and of further increasing unemployment among young workers if inactivity traps exist. Figure 7 simulates the 1999 RMI scenario, abolishing the age condition. While this hypothetical reform has little e¤ect on the whole sample, the HS dropouts show a negative employment response, similar to the one observed at the cuto¤. Introducing the RMI for those under 25 induces a drop in participation of 5 ppt in this group. Symmetrically to the e¤ect of abolishing the RMI, this shows that young workers with low wage prospects may be tempted to claim the RMI and live on welfare, which casts doubts on the desirability of extending unconditional welfare payments to this group.

Figure 7: Counterfactual Employment Simulations: Extending RMI to the Young

Employment rate.65.7.5.5.55.55.6.6

Employment rate.65.7.75.75.8.8.85

HS Dropouts.85

All 20 22 24 26 28 30 20 22 24 age 95% CI base 26 28 30 age 95% CI no age condition 95% CI base 95% CI no age condition Policy Simulation: Extending the RSA to the Youth. This calls for a last simulation: What would be the e¤ect of extending the RSA scheme to the under-25? This is a highly topical and relevant question in the current policy debate in France (see Bargain and Vicard, 2012). 18 We start with a baseline simulation of the RSA policy scenario and additionally simulate a removal of the age condition. Extending the RSA to the young combines two opposite forces. On the one hand, we have seen that extending out-of-work welfare programs to the young creates disincentive e¤ects for the under-25’s, especially for the HS dropouts. On the other hand, the young can also bene…t from in-work incentives with the RSA. The overall e¤ect is undetermined. The results, in Figure 8, show that extending the RSA to the young would not have a signi…cant employment e¤ect for the whole selected group. We observe a small decrease in employment rates for the more vulnerable HS dropouts, yet it is not signi…cant. Hence, our simulation gives support to the extension of welfare programs in France provided that in-work components are in place to "make work pay". 18 An extension to 18-25 year olds was actually implemented in September 2011, although with very strict eligibility rules. A very small number of young workers have actually taken up this "RSA junior" so this should not a¤ect our results on Census 2010-2011 in the previous sub-section.

Figure 8: Counterfactual Employment Simulations: Extending RSA to the Young.8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 20 22 age

## 95% CI RSA

6 24 26 28 30 age 95% CI RSA: no age condition

## 95% CI RSA

95% CI RSA: no age condition

## Conclusions

We study the labor supply e¤ect of the pre-2009 French social assistance program around age 25, i.e. the age limit under which young workers are not eligible. This discontinuity provides a neat identi…cation of the policy e¤ect around the cuto¤. However, RD estimates do not allow extrapolation further away from it or the simulation of alternative systems. Hence, we estimate a more structural model identi…ed on the same discontinuity and on an additional exclusion restriction which allows extrapolation. The model reproduces the participation drop at age 25 and also predicts employment levels at other age levels satisfactorily. It also allows the simulation of counterfactual policies. Compared to recent RD results for the 2009 reform, the model performs relatively well in showing that this reform and, notably, its in-work bene…t component, restores …nancial incentives to work and alleviates the inactivity trap for HS dropouts. With this new system which combines transfers to both workless and working poor, the extension to the under-25 year olds does not seem to create any signi…cant disincentive e¤ects. We have focused on a structural participation model. The extensive margin is, arguably, the primary dimension that merits investigation in the context of youth unemployment. This is surely the margin with the greatest degree of potential response in the short run, simply because people can always opt out of the labor market (in contrast, …nding a different hour contract may be di¢ cult and subject to constraints, cf. Chetty et al, 2011). In this respect it is, therefore, the best ground for reconciling structural models and natural experiments as we do here. Note, however, that the more general labor supply model presented above could be identi…ed and estimated using additional sources of exogenous variation, e.g., other discontinuities a¤ecting the …nancial gains to work part-time versus full-time. We leave this for future research. Moreover, labor supply models rarely account for the interaction between labor supply adjustment and the demand-side of the economy. Future work should integrate the two approaches more systematically. Finally, the structural model should be tested more formally, notably the exclusion restriction that allows extrapolation further away from the age cuto¤. For this, better data are required. For instance, consecutive years of Census data with changes in the nature of the discontinuity could be used to control for year (business cycle) e¤ects and age e¤ects while checking the prediction of the model regarding changes in the size of the social welfare discontinuity over time.

## References

[1] Angrist, J.D. and J.S. Pischke (2010): “The credibility revolution in empirical economics: How better research design is taking the con out of econometrics”, Journal of Economic Perspectives, 24, 3–30.

[2] Angrist, J.D. and M. Rokkanen (2013): "Wanna Get Away? RD Identi…cation Away from the Cuto¤," IZA Discussion Papers 7429, Institute for the Study of Labor

## (IZA).

[3] Arulampalam, W., A. Booth and M. Bryan (2007): "Is There a Glass Ceiling over Europe? Exploring the Gender Pay Gap across the Wage Distribution," Industrial and Labor Relations Review, 60(2), 163-186.

[4] Attanasio, O., C. Meghir and A. Santiago (2011): “Education choices in Mexico:

Using a structural model and a randomized experiment to evaluate PROGRESA”, Review of Economic Studies.

[5] Bargain, O. (2009): “Flexible labour supply models”, Economics Letters, 105, 103105 [6] Bargain, O. and K. Doorley (2011): "Caught in the Trap? Welfare’s Disincentive and the Labor Supply of Single Men", Journal of Public Economics, 95(9-10), 1096-1110.

[7] Bargain, O, and A. Vicard (2012): "Le RMI puis le RSA découragent-ils certains jeunes de travailler? Une analyse sur les jeunes autour de 25 ans", Economie et Statistiques, forthcoming.

[8] Be¤y, M., M. Buchinsky, D. Fougère, T. Kamionka, F. Kramarz (2006): "The Returns to Seniority in France (and Why Are They Lower than in the United States?)", IZA DP No. 1935 [9] Blundell, R. (2006): "Earned income tax credit policies: Impact and optimality:

The Adam Smith Lecture, 2005," Labour Economics, Elsevier, vol. 13(4), pages 423-443, August.

[10] Blundell, R., (2012) “Tax policy reform: The role of empirical evidence”, Journal of the European Economic Association, 10, 43–77.

[11] Blundell, R. et T. MaCurdy (1999), "Labor Supply: A Review of Alternative Approaches," in Handbook of Labor Economics, Vol. 3A. Ashenfelter and Card eds.

[12] Blundell, R., Duncan, A. and Meghir, C. (1998): "Estimating Labour Supply Responses Using Tax Reforms", Econometrica 66(4)(4): 827–861.

[13] Bourguignon, F. and T. Magnac (1990): “Labour supply and taxation in France”,

Journal of Human Resources, 25, 358-389.

[14] Cai, L., G. Kalb, Y-P Tseng, H. Vu (2008): "The E¤ect of Financial Incentives on Labour Supply: Evidence for Lone Parents from Microsimulation and QuasiExperimental Evaluation", Fiscal Studies, 29, 2, 285–325 [15] Card, D., and D. Hyslop, (2005), “Estimating the E¤ects of a Time-Limited Earnings

Subsidy for Welfare-Leavers,’Econometrica, Vol 73(6):1723-1770 [16] Chemin, M. and E. Wasmer (2011): "Ex-ante and ex-post evaluation of the 1989 French welfare reform using a natural experiment: the 1908 social laws in AlsaceMoselle », working paper.

[17] Chetty, R., J. Friedman, T. Olsen and L. Pistaferri (2011): "Adjustment Costs, Firm Responses, and Micro vs. Macro Labor Supply Elasticities: Evidence from Danish Tax Records," Quarterly Journal of Economics, 126(2), 749-804 [18] Choi, E.J. (2011): "Evaluating a Structural Model of Labor Supply and Welfare Participation: Evidence from State Welfare Reform Experiments", mimeo [19] Deaton, A., (2009) “Instruments of development: randomization in the Tropics and the search for the elusive keys to economic development”, Proceedings of the British Academy, 162, 123-160, Oxford: Oxford University Press [20] Du‡o, E., R. Hanna, and S. Ryan (2007): “MonitoringWorks: Getting Teachers to Come to School,”unpublished manuscript, department of economics, MIT [21] Eissa, N. and J.B. Liebman (1996): "Labor supply response to the Earned Income Tax Credit", Quarterly Journal of Economics 111(2): 605–637.

[22] Eklof, M. and H. Sacklén (2000): “The Hausman-MaCurdy Controversy: Why do Results Di¤er Between Studies?”, Journal of Human Resources, 35(1), 204-220 [23] Fougère, D., F. Kramarz, J. Pouget (2009): "Youth unemployment and crime in France", Journal of the European Economic Association, 75(5), 909-938 [24] Francesconi, M. and W. Van der Klaauw (2007): "The Socioeconomic Consequences of’In-Work’ Bene…t Reform for British Lone Mothers", Journal of Human Resources, 42(1), 1-31 [25] Gurgand M. and D. Margolis (2008): "Does work pay in France? Monetary incentives, hours constraints, and the guaranteed minimum income", Journal of Public Economics, 92,1669–1697 [26] Hansen, J. & X. Liu, 2011. "Estimating Labor Supply Responses and Welfare Participation: Using a Natural Experiment to Validate a Structural Labor Supply Model," IZA Discussion Papers 5718, Institute for the Study of Labor (IZA).

[27] Hausman, J., (1981), Stochastic Problems in the Simulation of Labor Supply, No 0788, NBER Working Papers, National Bureau of Economic Research, Inc.

[28] Hausman, J., and D. Wise, (1979), “Attritin Bias in Experimental and Panel Data:

The Gary Income Maintenance Experiment,’Econometrica, Vol. 47(2): 455-473.

[29] Hoynes, H. W. (1996): "Welfare transfers in two-parent families: Labor supply and welfare participation under AFDC-UP", Econometrica, 64(29), 295-332.

[30] Imbens, G. W. (2010) “Better LATE than Nothing: Some Comments on Deaton (2009) and Heckman and Urzua (2009)”, Journal of Economic Literature, 48, 399-423 [31] Imbens, G., D. Rubin, and B. Sacerdote, (2001): "Estimating the E¤ect of Unearned Income on Labor Supply, Earnings, Savings and Consumption: Evidence from a Survey of Lottery Players", American Economic Review 91, 778-794 [32] Immervoll H., H. Kleven, C. Kreiner and E. Saez (2007): "Welfare reform in European countries: A microsimulation analysis", Economic Journal, 117(516), 1-44.

[33] Jonassen, A. (2013): "Disincentive e¤ect of a generous social assistance scheme",

Aarhus university.

[34] Keane, M. and K. Wolpin (2007): "Exploring The Usefulness Of A Nonrandom Holdout Sample For Model Validation: Welfare E¤ects On Female Behavior," International Economic Review, 48(4), 1351-1378.

[35] Lalonde, R.J., (1986): "Evaluating the Econometric Evaluations of Training Programs with Experimental Data", American Economic Review, 76, 604-620 [36] Laroque G. and B.Salanié (2002): "Labour market institutions and employment in

France", Journal of Applied Econometrics, 17, 25-48 [37] Lee, D.S. and Card, D. (2008): "Regression discontinuity inference with speci…cation error", Journal of Econometrics, 142(2), 655-674 [38] Lee, D.S, and T. Lemieux (2010): "Regression discontinuity designs in Economics",

Journal of Economic Literature, 48, 281–355 [39] Lemieux, T. and K. Milligan (2008): "Incentive e¤ects of social assistance: a regression discontinuity approach", Journal of Econometrics, 142(2), 807–828 [40] Thoresen, T.O. and T.E. Vattø (2012): "Income Responses to Tax Changes. Reconciling Results of Quasi-Experimental Evaluation and Structural Labor Supply Model Simulations", mimeo [41] Todd, P. and K. Wolpin (2003): “Using a Social Experiment to Validate a Dynamic Behavioral Model of Child Schooling and Fertility: Assessing the Impact of a School Subsidy Program in Mexico”, Penn Institute for Economic Research [42] Train, K. (2003), Discrete Choice Models using Simulation. Cambridge, UK: Cambridge University Press.

[43] van Soest, A. (1995): “Structural Models of Family Labor Supply: a Discrete Choice

Approach”, Journal of Human Resources, 30, 63-88.

[44] van Soest, A., M. Das and X. Gong (2002): “A structural labor supply model with non-parametric preferences”, Journal of Econometrics, 107 (1-2), 345-374 [45] Vermeulen, F. (2002), “Collective household models: principles and main results”,

Journal of Economic Surveys, 16, 533-564

## A

Measuring the Treatment E¤ect We can use the structural model to predict employment levels at 24 and 25, and check whether predictions reproduce the actual discontinuity in employment-age patterns. The age di¤erential in employment levels is not exactly equal to the treatment e¤ect, however. Ignoring individual heterogeneity and assuming we use a linear probability model to ease notation, we can write the treatment e¤ect in the RD design as:

## = Y 25

## Y 24 +:[(25)

(6) (24)] with Y A the average participation level at age A. By analogy, we can de…ne the treatment e¤ect in the structural model as:

## Y 25

Y 24 + g:[(25) (7) (24)]:

When assuming b 1 = b 0 = b > 0, this also corresponds to b f[C(w e i H; 25)

## C(0; 25)]

[C(w e i H; 24) [fb 1 C(w e i H; 25) b 0 C(0; 25)g

C(0; 24)]g;

i.e. a change in the …nancial gains to work between 25 and 24 years of age. This de…nition fails to account for the di¤erentiated e¤ect of age on wages at age 24 and 25, however. Therefore, the correct measure of the policy e¤ect at the cuto¤ requires the evaluation of the employment gap at age 25, accounting for the counterfactual situation C 0 (no RMI):

fb 1 C 0 (w e i H; 25) b 0 C 0 (0; 25)g]:

The policy e¤ect at the cuto¤ is therefore:

## Y 25

Y 24 + g:[(25) +b 0 fC(0; 25) (8) (24)]

C 0 (0; 24)g b 1 fC 0 (w e i H; 25)

C(w e i H; 24)g In this formula, C(0; 25) C 0 (0; 24) is zero by de…nition. Hence, the only di¤erence with (7) is a correction for the di¤erence in wage levels between age 25 and 24 in the last term.

## B

## B.1

Wage and Labor Supply Estimations

Wage Imputation Log hourly wage estimations using the LFS data are reported in Table B.1 together with the reduced-form participation equation for the Heckman correction. A signi…cant gender gap can be observed, in line with the existence of a "sticky ‡oor" e¤ect in France (Arulampalam et al, 2007) as well as a regular wage progression with the level of education. The Inverse Mills ratio is not signi…cant. In the participation equation, disposable income when out of work is negative, as expected. It is not statistically signi…cant, probably due to the lack of power in the LFS (Chemin and Wasmer, 2012, reproduce our RD results using 12 years of LFS while we use here only the 3 years surrounding 1999). We check the robustness of our wage imputation in Figures B.1 (men) and B.2 (women). The …rst row shows that actual and predicted log wage distributions for workers in the LFS are relatively comparable, with the exception of the few observations below the minimum, a situation that we rule out in our predictions. The middle-left graph of each Figure shows that the distribution of predicted (log) wages for workers in the Census is very comparable to the one obtained in LFS (top right graph). This con…rms that comparable distributions of socio-demographics in both surveys allows comparable predictions of the wage distribution. The second row also compares the log wage imputation in the Census based on linear estimation to the other method based on matching (see section 4.3). The latter actually compares much better to the actual (log) wage distribution, i.e. the top right graph, and captures, in particular, the density of observations just above the minimum wage. Finally, the last row of each Figure compares the distributions of predicted (log) wages for the whole Census selection, i.e. both for workers and non-workers, using both methods. Moving from wages to disposable incomes, we have seen in Table 1 that predicted disposable incomes –calculated using tax-bene…t simulation and either actual gross incomes (in the LFS) or work duration and imputed wages (in the Census) –line up quite closely in the two datasets.

## B.2

Labor Supply Estimations Table B.2 shows the estimates of the RD model and of the participation model. The constant for the RD model is in line with the treatment e¤ect for uneducated females as reported in Table 2 (3:3). Looking at the constant in the coe¢ cients on in-work and out-of-work income in the participation model, the marginal e¤ect of 1 additional EUR on participation is very di¤erent whether we consider in-work or out-of-work income. The e¤ect of income at zero hours is roughly four times smaller, which could re‡ect (i) the fact that …nancial incentives depend primarily on income prospects on the labor market, (2) the negative e¤ects attached to welfare payments (e.g., stigma), (3) other reasons including the lack of variability in C(0; A) for the identi…cation of a di¤erentiated e¤ect. For educated females, the e¤ect of welfare income is reduced by half in each model.

Table B.1: Wage Estimation with Selection on LFS Data

Variables

Log wage

Age

Age square / 100

Female

Junior vocational qualification

Highschool diploma

Vocational highschool dipl.

Graduate qualification

Disposable income 0 hours/100

Inverse Mills ratio

Constant -0.048 0.001 -0.112 0.054 0.168 0.131 0.352 (0.023) (0.000) (0.007) (0.011) (0.016) (0.013) (0.011) -0.003 4.177 (0.101) (0.301)

Employment

## 0.079 (0.099)

-0.002 (0.002)

## 0.042 (0.027)

-0.006 (0.017)

Observations 7,101 Selection: pooled LFS 1997-2001. Standard errors in parenthesis -0.338 (1.263) 9,986 Table B.2: Estimates: RD and Participation Models on Census Data

## RD

Behavioral Model

Coefficient s.e.

Coefficient s.e.

Preference for work

Age

Age2

Age3

Age*educated

Age2*educated

Age3*educated

Male

Male*educated

Educated

Constant 0.721 -0.027 0.000 -0.366 0.015 0.000 0.061 -0.031 3.228 -5.857 0.221 0.009 0.000 0.244 0.010 0.000 0.005 0.005 1.994 1.805 2.837 -0.104 0.001 -1.206 0.051 -0.001 0.557 0.043 10.869 -27.041 1.217 0.049 0.001 1.421 0.057 0.001 0.059 0.029 11.635 9.953

Coefficients on Age >=25 Educated Male Constant 0.027 -0.009 -0.033 0.012 0.004 0.012 -0.025 0.011 0.047 0.022 0.008 0.020 Coefficients on Income when H=39 hours/week (divided by 100)

Educated -0.070

Male -0.039

Constant 0.214 0.007 0.005 0.007 Coefficients on Income when H=0 (divided by 100) Educated Male Constant

Log Likelihood prob > chi2

Observations 202093 -91701 0 202093 RD estimates are obtained by OLS. The participation model is estimated by simulated ML with conditional probabilities averaged over ten wage x unobserved heterogeneity draws.

Density 1 1.5 2.5 0 0.5

Density 1 1.5 2 2.5

Predicted log wage LFS workers 2.5

Actual log wage LFS workers 2 3 4 log wage 5 6 2 3 4 log wage 5

Actual log wage distribution

Predicted log wage distribution

Minimum wage

Minimum wage

Density 1 1.5 2.5 0 0.5

Density 1 1.5 2 2.5

Matched log wage Census workers 2.5

Predicted log wage Census workers 6 2 3 4 log wage 5 6 2 3 4 log wage 5

Predicted log wage distribution

Predicted log wage distribution

Minimum wage

Minimum wage

Density 1 1.5 2.5 0 0.5

Density 1 1.5 2 2.5

Matched log wage Census all 2.5

Predicted log wage Census all 6 2 3 4 log wage 5 6 2 3 4 log wage 5

Predicted log wage distribution

Predicted log wage distribution

Minimum wage

Minimum wage 6 Figure B.1: Comparing Predicted and Matched Log Wage Distributions in LFS and

Census Data (Men)

Density 1 1.5 2.5 0 0.5

Density 1 1.5 2 2.5

Predicted log wage LFS workers 2.5

Actual log wage LFS workers 2 3 4 log wage 5 6 2 3 4 log wage 5

Actual log wage distribution

Predicted log wage distribution

Minimum wage

Minimum wage

Density 1 1.5 2.5 0 0.5

Density 1 1.5 2 2.5

Matched log wage Census workers 2.5

Predicted log wage Census workers 6 2 3 4 log wage 5 6 2 3 4 log wage 5

Predicted log wage distribution

Predicted log wage distribution

Minimum wage

Minimum wage

Density 1 1.5 2.5 0 0.5

Density 1 1.5 2 2.5

Matched log wage Census all 2.5

Predicted log wage Census all 6 2 3 4 log wage 5 6 2 3 4 log wage 5

Predicted log wage distribution

Predicted log wage distribution

Minimum wage

Minimum wage 6 Figure B.2: Comparing Predicted and Matched Log Wage Distributions in LFS and

Census Data (Women)

## C

.8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 20 22 24 age 26 28 30 age 95% CI base 95% CI RSA reform 95% CI base 95% CI RSA reform Figure C.1: Counterfactuals: Replacing RMI with RSA (Matched Wages).8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 20 22 24 age 95% CI base 26 28 age 95% CI abolish RMI 95% CI base 95% CI abolish RMI

Figure C.2: Counterfactuals: Abolishing RMI (Matched Wages) 30.8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85.85

All 20 22 24 26 28 30 20 22 24 age 95% CI base 26 28 30 age 95% CI no age condition 95% CI base 95% CI no age condition Figure C.3: Counterfactuals: Extending RMI to the Young (Matched Wages).8.75

Employment rate.65.7.6.55.5.5.55.6

Employment rate.65.7.75.8.85

HS Dropouts.85

All 20 22 24 26 28 30 20 22 age

## 95% CI RSA

24 26 28 age 95% CI RSA: no age condition

## 95% CI RSA

95% CI RSA: no age condition Figure C.4: Counterfactuals: Extending RSA to the Young (Matched Wages) 30
