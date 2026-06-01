# Structural Labor Supply Models and Wage Exogeneity*

Max Löffler

ZEW and University of Cologne

Andreas Peichl ZEW, University of Mannheim, CESifo, ISER and IZA

Sebastian Siegloch

IZA, ZEW and University of Mannheim

June 2014

## ABSTRACT

There is still considerable dispute about the magnitude of labor supply elasticities. While differences in micro and macro estimates are recently attributed to frictions and adjustment costs, we show that relatively low labor supply elasticities derived from microeconometric models can also be explained by modeling assumptions with respect to wages. Specifically, we estimate 3,456 structural labor supply models each representing a plausible combination of frequently made choices. While most model assumptions do not systematically affect labor supply elasticities, our analysis shows that the results are very sensitive to the treatment of wages. In particular, the often‐made but highly restrictive independence assumption between preferences and wages is key. To overcome this restriction, we propose a flexible estimation strategy that nests commonly used models. We show that loosening the exogeneity assumption leads to labor supply elasticities that are much higher.

JEL Classification:

## C25, C52, H31, J22

Keywords:

labor supply, elasticity, random utility models, wages

Corresponding author:

Andreas Peichl

## ZEW

## L7,1

68161 Mannheim

E‐mail: peichl@zew.de * The authors thank Rolf Aaberge, Felix Bierbrauer, Richard Blundell, John Dagsvik, Alan Duncan, Peter Haan, Jan Kabátek, Nico Pestel and Eric Sommer, as well as seminar participants at CPB, IIPF, IZA, Young Scholar GSOEP Symposium, Statistics Norway and Verein für Socialpolitik for helpful comments and suggestions on earlier versions.

Knowing the true size of labor supply responses has important implications for welfare analysis (Eissa et al., 2008) and optimal taxation (Diamond and Saez, 2011, Immervoll et al., 2011). One of the most topical questions in the long and comprehensive literature on labor supply behavior is why macro elasticities are (substantially) larger than micro ones (Chetty et al., 2011, Keane and Rogerson, 2012). While older explanations focus on the use of representative agents and aggregation difficulties (Blanchard, 2007) or social multipliers (Alesina et al., 2006), more recent studies attribute differences to costs and frictions in labor supply adjustments, which standard microeconometric research designs can only imperfectly account for (Chetty, 2012). In principle, structural micro-level labor supply models should be able to capture these adjustment frictions (Aaberge et al., 1995, van Soest, 1995, Blundell et al., 2000). 1 However, even these widely used models typically produce labor supply elasticities well below those found in macro studies, which immediately raises the question of why this is the case. In this paper, we aim to answer this question by thoroughly scrutinizing state-ofthe-art micro labor supply models and their functioning. More specifically, in the first part of the paper, we test whether the numerous modeling choices and assumptions to be made when setting up structural labor supply models affect estimated elasticities. 2 We check the internal validity of these models by running controlled experiments: we set up and estimate 3,456 models each representing a different (plausible) combination of commonly made modeling assumptions using two different micro datasets—one for Germany and one for the US. Based upon the estimation results, we gather insights into how robust the statistical fit of the models and the estimated labor supply elasticities are with respect to the underlying assumptions. Our results show that the models’ predictions do not depend on the specification of the functional form or the inclusion of observed and unobserved preference heterogeneity, hours restrictions or stigma costs of welfare participation. However, we find that the treatment of wages in the estimation procedure is crucial. For instance, the choice between predicting wage rates for the full sample or only for non-workers with missing wage information—both procedures are often used in the literature— may more than double the estimated labor supply elasticities. We conclude that the attention of previous sensitivity analyses has been mainly concentrated on less important factors while the main driving forces have been neglected, i.e. the interactions

1 While recent research in labor economics typically relies on quasi-experimental methods to identify causal effects of reforms, structural models are still necessary for policy analysis and especially out of sample predictions (e.g., the ex-ante evaluation of a tax reform). 2 Note that structural models are sometimes criticized for the large number of assumptions to be made and the even larger number of possible combinations of these assumptions (Keane, 2010).

between wages, working hours and preferences. This finding is even more relevant given that most existing models (implicitly) assume exogeneity between the wage equation and the labor supply decision, which is naturally quite a restrictive assumption. 3 Against this backdrop, in the second part of the paper, we propose a novel, flexible estimation strategy to relax the strict exogeneity assumptions regarding wage rates and work preferences. Estimation results show that there is indeed strong correlation between both preferences and wages, as well as wages and hours of work. For instance, wages are lower for part-time compared to full-time jobs and individuals with higher wages are found to have higher preferences for leisure. The usual procedure to estimate wages in the first step and assume a fixed wage rate (independent of working hours) for every individual in the labor supply estimation ignores these correlation patterns and drives the estimated elasticities towards zero. In our preferred model, estimated labor supply elasticities are more than twice as high compared to conventional models assuming zero correlation between work preferences and wages (0.6 instead of 0.25). We conclude that the standard approach neglects important factors that determine a household’s response to wage changes, which yields too low micro elasticities of labor supply. Consequently, part of the unexplained difference between macro and structural micro elasticities may be due to model specification errors regarding the wage treatment. In this paper, we make three important contributions to the literature on labor supply estimation. First, there is little evidence on the functioning of structural labor supply models in general. Moreover, if such studies exist, different models are not estimated on the same dataset. 4 In that respect, we run a controlled meta-analysis, isolating the impact of the model assumptions on estimation outcomes. Second, our analysis points to a hitherto neglected factor that strongly influences the estimated labor elasticities: we show that the treatment of wages in labor supply estimations, which is rarely theoretically motivated nor subject to robustness checks, crucially affects the estimation results. In particular, we demonstrate that the commonly assumed exogeneity between wage rates and labor supply decisions plays an important rule. To tackle this issue, we propose a novel estimation strategy that relaxes this assumption and additionally allows for correlation between work preferences and wages. There3 Only little effort has been made thus far in the context of discrete choice labor supply models to overcome this assumption. Aaberge et al. (1995), Breunig et al. (2008) and Blundell and Shephard (2012) estimate preferences and wages simultaneously, in part also allowing for some correlation. We discuss the differences to our approach, which is more general, in detail in Section 5. 4 Existing surveys and meta-analyses focus on either the principles of alternative estimation strategies (Blundell and MaCurdy, 1999, Evers et al., 2008) or cross-country comparisons of empirical findings (Bargain et al., 2014). Robustness checks in previous studies usually limit themselves to small deviations in one or only few of the numerous modeling assumptions.

fore, our approach is more flexible than previous models, while at the same time it nests previous models and allows testing the assumption of zero correlation. Third, our findings of significant correlations and resulting higher labor supply elasticities have important policy implications as labor supply elasticities are key parameters when evaluating or designing optimal tax benefit policies. For instance, Diamond and Saez (2011) use an elasticity of 0.25, which is close to our estimate for the restrictive model, to derive an optimal top marginal tax rate of 72.7 %. However, an elasticity of 0.6, as found in our most flexible model, reduces the optimal tax rate to

## 52.6 %, bringing it closer to actually observed values.

The remainder of this paper is organized as follows. Section 2 presents the general modeling framework and a short overview of the existing literature. Section 3 provides information on the used data and the modeling of the tax and benefit system.

In Section 4 we conduct our analysis of modeling assumptions and present first results. The new flexible estimation approach is introduced in Section 5, before Section 6 concludes.

2 Model and existing literature The use of structural discrete choice labor supply estimations has become a standard procedure in the empirical analysis of labor supply for both econometricians and policy makers (Bargain and Peichl, 2013). The first generation of labor supply models relied on the assumption that the household’s utility is maximized over a continuous set of working hours—known as Hausman approach (see Hausman, 1981). This procedure has proven somewhat cumbersome when the budget set is non-convex, which will often be the case in presence of the complicated tax and benefits systems in most countries. Moreover, it has been shown that the estimated models are very sensitive to the underlying wages (Ericson and Flood, 1997, Eklöf and Sacklén, 2000). As the consistent estimation of this type of model relies on rather restrictive a priori assumptions (see, e.g. MaCurdy et al., 1990, or Bloemen and Kapteyn, 2008, for details), it has become increasingly popular to model the labor supply decision as choice between a (finite) set of utility levels instead of deriving the marginal utility. Starting with the works by Aaberge, Dagsvik and Strøm (1995), van Soest (1995) and Hoynes (1996), a wide range of different empirical specifications of these discrete choice models has been applied. Comparing different levels of utility avoids the cumbersome maximization process of Hausman-type models. We focus our analysis on the discrete choice approach, given that it has become the standard procedure across the literature.

Structural labor supply estimations build on the assumption of the well-known neoclassical labor supply model that decision makers maximize their utility by choosing the optimal amount of hours of work (or the optimal job, more generally). As higher working hours increase consumption but reduce leisure, households face a trade-off between these two goods. Stated mathematically for individual n:

max U C nj, L j, e nj = max U f w nj h j x nj, I n, T − h j, e nj j j ∈ J n (1) where leisure L j is denoted as difference between total time endowment T and working hours h j. Consumption C nj depends on working hours, hourly wage rate w nj, non-labor income I n, household and job characteristics x nj and the tax benefit function f. Individual n faces the decision between a set of jobs J n with working hours h j and wages w nj, including non-participation denoted as j = 0 (with h 0 = 0 and w n0 = 0). Most models in the literature make the quite restrictive assumption that wages are individual-specific and do not vary across alternatives. 5 We assume a static context, which implies that consumption equals disposable income as there is no future utility from saving. The true utility is only partly observable to the researcher while other components e nj are latent. Thus, we can write the utility of individual n choosing job type j as:

U C nj, L j x nj, β n, γ n = ϕ C nj, L j x nj, β n, γ n + e nj (2) The observed part ϕ C nj, L j x nj, β n, γ n is determined by consumption and leisure, characteristics x nj, individual preferences β n and labor market conditions γ n that capture the availability of job type j. One could think of these labor market characteristics γ n as measuring individual-specific fixed costs, search costs for part-time jobs or rigidities regarding working hours, for example. The unobserved taste variation e nj is assumed to be i.i.d. and follow the extreme value type I distribution with cumulative distribution function F (e) = exp (− exp (− e )). McFadden (1974) has shown that the probability of individual n choosing a job of type i is subsequently given by:

P U ni > U nj, ∀ j 6 = i x n, β n, γ n exp ϕ C ni, L i x ni, β n, γ n = ∑ s ∈ J n exp ϕ C ns, L s x ns, β n, γ n

5 An (3) exception are the models by Aaberge, Dagsvik and Strøm (1995) and follow-ups. We further loosen this restriction in Section 5 when estimating wages and preferences jointly.

Assuming that individuals take labor market conditions as given, we can rewrite:

P U ni > U nj, ∀ j 6 = i x n, β n, γ n exp v C ni, L i x ni, β n g i x ni, γ n = ∑ s ∈ J n exp v C ns, L s x ns, β n g s x ns, γ n (4) with v (C nj, L nj) as systematic utility function and g (j) as frequency of feasible jobs with type j. In words, the individual choice probability is given as the systematic utility part weighted by the availability of jobs with type j. In the following, we discuss the specification of v (·) and g (·) and the estimation procedure.

## 2.2 Estimation

Econometrically, the discrete choice approach boils down to the representation of the labor supply decision in a random utility model. In the very basic model, the theoretical setup implies that the household’s decision satisfies the Independence of Irrelevant Alternatives (IIA) property (Luce, 1959). In other words, the preference between two alternatives does not depend on the presence of a third one. While this assumption may seem rather restrictive at first glance, Dagsvik and Strøm (2004) and Train (2009) show that it is well in line with economic intuition and even less restrictive than the necessary assumptions to estimate continuous hours models. However, the IIA assumption is no longer needed as soon as additional random effects are incorporated in the model (see Section 2.3).

Identification. As in every structural estimation problem, it is crucial to impose a specific functional form for both v (C nj, L nj) and g (j) to obtain consistent estimates of β n and γ n. Van Soest et al. (2002) show that semi-parametric specifications also yield consistent results. We further discuss different assumptions that are frequently used below. As consumption is a function of working hours and thus leisure, identification of preference parameters relies on (a) the variation in working hours h j, hourly wages w nj, non-labor income I n and other characteristics x nj and (b) the fact that the tax function f (w nj h j, I n) is highly non-linear in h j and w nj. This also implies that labor market conditions γ n can only be separated and identified on the assumption of a specific functional form (Dagsvik and Strøm, 2006). In addition to this, the vast majority of the literature also assumes that preferences β n and labor market conditions γ n may depend on individual characteristics, but are independent of the wage rate w nj. Thus, it is assumed that:

Corr β n, w nj x nj = 0 Corr γ n, w nj x nj = 0 (5) The main reason for this assumption is that it reduces the computational burden substantially and makes the estimation more convenient. However, assuming exogeneity seems quite restrictive, as unobserved ability, for instance, is most likely positively correlated with both wage rates and work preferences. Therefore, we test and relax this assumption in Section 5.

In order to estimate the preference coefficients, one has to evaluate both functions v and g for every household n = 1,..., N and every choice category within the choice set J n. Given the different income levels, the model can be estimated via maximum likelihood. The derivation of the (log)-likelihood function is straightforward (McFadden, 1974). However, some modeling assumptions have to be made, as well as several possible extensions to this simple setup.

## 2.3 Model setup

Choice set. The first decision in the estimation relates to the construction of the choice set (see Aaberge et al., 2009, for a detailed discussion of this issue). Most authors simply pick a set of representative levels of hours of work and assume (small) identical choice sets for the whole population. In our analysis, we follow the literature and assume that households with a single decision maker face seven possible labor supply states, i.e. either non-participation or working 10, 20, 30, 40, 50 or 60 hours per week. Couple households are assumed to face 7 2 alternatives. 6 Functional form of the systematic utility. As the discrete choice approach relies on the comparison of different utility levels, it is crucial to determine the form of the systematic utility function. In theoretical terms, the function v represents the direct utility function of the household. Most applications rely on either a translog, a quadratic or a Box-Cox transformed utility specification. However, several other choices are possible.

Heterogeneity in preferences. Observed heterogeneity in the labor supply behavior can be rather easily introduced in the context of structural labor supply models. The preference coefficients of the direct utility function are usually interacted with some observed household characteristics, such as age or the presence of children, as taste shifters.

6 Note that the results are generally not sensitive to the number of choices (e.g., 4 vs. 7 vs. 13) or the exact value assigned to each category – see, e.g., Bargain et al. (2014).

Moreover, including also unobserved heterogeneity overcomes the IIA assumption as it allows for unobservable variation in preferences between choice alternatives. There are two main ways to do so: in most applied works, either a random coefficient model (van Soest, 1995) or a latent class model (Hoynes, 1996) is assumed. While the former assumes a set of coefficients to be (multivariate) normally distributed, the latter assumes a set of discrete mass points for the estimated coefficients. Keane and Wasi (2012) discuss the performance of both approaches. We focus on the random coefficient approach as it has become standard across the literature.

Welfare stigma and benefit take-up. While the model as described thus far assumes that households only build their preferences with respect to the levels of consumption and leisure, their utility may also depend on the source of income. For example, the participation in welfare programs may be connected to an unobservable stigma that affects the household’s utility and prevents some households from taking up benefits (Moffitt, 1983). In the discrete choice context, this can be incorporated by accounting for the potential disutility from welfare participation and expanding the choice set such that the household explicitly chooses between benefit take-up and non-participation (Hoynes, 1996, Keane and Moffitt, 1998).

Fixed costs and hours restrictions. Moreover, van Soest (1995) argues that working part-time could also be connected with an unobservable disutility, because part-time jobs may exhibit higher search costs. Euwals and van Soest (1999) extend this idea by introducing fixed costs of work, which have since been used in several applications. While both approaches help to explain the observed labor market outcomes, their rational remains rather ad hoc. Aaberge et al. (1995) provide a more convenient theoretical framework that delivers a structural interpretation of fixed costs and the utility connected to certain hours alternatives. In their model, households choose between (latent) job offers that not only differ regarding the working hours, but also in terms of availability, wages and non-monetary attributes.

## 2.4 Wage imputation procedure

In addition to the specification of the utility function, there are important modeling assumptions regarding the wage imputation. In order to calculate the disposable income for the different choice alternatives, one needs information on the hourly wage rates. While for actual workers the wage rate can be calculated by gross earnings and hours of work (we use standardized working hours to reduce the potential division bias, see Borjas, 1980, and Ziliak and Kniesner, 1999, for a discussion), the wage information is typically missing for non-workers. The first decision is how to deal with missing wages in the estimation process. In practice, wages are either estimated beforehand and treated as given within the estimation of the labor supply model or wages and preferences are estimated jointly. In addition, one has to decide whether the estimated wage rates are used only if wages are not observed or for the full sample (see MaCurdy et al., 1990, for a discussion of the advantages and disadvantages of both approaches). In either case, one can ignore or explicitly include potential sample selection issues in the observed wages. After estimating the wage equation, another important question is whether the potential errors in the wage rate prediction are incorporated in the labor supply estimation. Especially when using predicted wages for the full sample, the “new” distribution of wages will typically have a significantly lower variance and the predicted wage will differ considerably from the observed one, at least for some workers. Thus, ignoring the error when predicting wage rates, which is still done in practice, leads to inconsistent estimates. The standard procedure to incorporate wage prediction errors is to integrate over the whole estimated wage distribution and thus integrating out the wage prediction error during the estimation process (van Soest, 1995). One approximation used in some applications is to simply add a single random draw to the predicted wage rates (Bargain et al., 2014). While this procedure lacks a theoretical rationale, it substantially reduces the computational burden of the estimation.

## 2.5 Estimation approach

The named extensions especially regarding the inclusion of unobserved heterogeneity and the incorporation of wage prediction errors complicate the estimation procedure and lead to the more general representation as mixed logit model (Train, 2009). Taking the most general specification as reference, the likelihood function can be written as:

## N

## L =

∏

## + ∞ Z

## + ∞ Z

+ ∞

## Z

n = 1 − ∞ − ∞ − ∞ exp (v ni {·| ŵ ni, β n }) g (i | γ n) f (β n, γ n) f (ŵ n) dβ n dγ n d ŵ n (6) ∑ j ∈ J n exp v nj ·| ŵ nj, β n g (j | γ n) where i ∈ J n denotes the alternative chosen by individual n. The likelihood contributions not only depend on the systematical utility function, but also on the availability of the choice alternatives, denoted by g (i). This setup implies that the availability of choice alternatives can be separated from the systematic utility, which is a reasonable assumption at least for labor markets in industrialized countries. As the preferences may also include unobserved heterogeneity, the probability that household n maximizes its utility at choice alternative i has to be integrated over the possible set of coefficients (β n, γ n). Similarly, the individual likelihood contributions have to be integrated over the range of possible wage predictions ŵ nj. As both variables will typically not be uniformly distributed, the choice probability has to be weighted by the probability density of the random components. The model as written down in equation (6) is very general and less restrictive than the conditional logit setup. In turn, it is no longer possible to find an analytical solution. Train (2009) proposes the use of maximum simulated likelihood methods instead. In order to retrieve the simulated likelihood, the double integral has to be approximated and averaged over r = 1,..., R random draws from the distributions of (β n, γ n) and ŵ nj. The simulated log-likelihood is subsequently given by:

 n o  (r) (r) (r) exp v · ŵ , β g i γ n n ni ni  1  n o  ln (SL) = ∑ ln  ∑ ( r ) ( r ) ( r )

R r = 1 ∑ n = 1 g j γ n j ∈ J n exp v nj · ŵ nj, β n

## N

## R

(7) When the number of draws goes to infinity, the simulated log-likelihood in (7) converges to the log-likelihood of the model denoted in (6). Instead of relying on conventional random draws, we approximate the likelihood function using pseudo-random Halton sequences. This reduces the number of draws needed to ensure stable results as Halton sequences cover the desired distribution more evenly (Train, 2009). 7

## 2.6 Existing literature

Tables 1 and 2 provide an overview of the empirical specification of several popular models that have been applied in recent years. As one can see, mainly three utility functions have been used, i.e. either a translog, a quadratic or a Box-Cox transformed specification. As the Stone-Geary function can be interpreted as a simplification of the translog or the Box-Cox utility function, only the higher-degree polynomials used in van Soest et al. (2002) stand out from the list. Their approach can be seen as approximation to a non-parametric specification of the utility function. The inclusion of observed heterogeneity shows a similar picture. All studies allow for observed heterogeneity in the preferences for leisure, whereas fewer studies allow for preference heterogeneity regarding consumption. The evidence on unobserved heterogeneity is somewhat more mixed, just like the inclusion of heterogeneity in fixed costs and the potential stigma from welfare participation.

As working hours are typically concentrated in only few hours categories, most authors include in their models fixed costs of working, hours restrictions, or both.

7 Details on the estimation procedure can be found in Löffler (2013).

Table 1: Different model specifications

Heterogeneity *

Utility

Welfare

Paper

Function

Observed

Unobs.

Stigma

Constraints

Aaberge et al. (1995, 2009)

Aaberge et al. (1999)

Dagsvik and Strøm (2006)

Dagsvik et al. (2011)

Blundell and Shephard (2012)

Box-Cox

Box-Cox

Box-Cox

Box-Cox

Box-Cox

## L

## L, FC

## L, FC

## L, FC

## L, C, S, FC

— — — —

## C, S

— — — —

Yes

## FC, HR

## FC, HR

## FC, HR

## FC, HR

## FC

van Soest (1995)

Euwals and van Soest (1999) van Soest and Das (2001)

Flood et al. (2004)

Haan (2006)

Flood et al. (2007)

Translog

Translog

Translog

Translog

Translog

Translog

## L

## L, FC

## L, FC

## L, L 2, S

## L, C

## L, C, FC, S

## —/L †

## L

## L

## L, L 2, S

## —/C

## L, C, FC, S

— — —

Yes —

Yes

## —/HR

## FC

## FC

—

## HR

## FC

Stone-Geary

Polynomial

## L, S

## L

## L, S

## L

Yes —

## —/FC

## FC

Quadratic

Quadratic

Quadratic

L, S L, C, FC L, C, FC

L, S C, S C

Yes

Yes — —

## FC

## FC

Hoynes (1996) van Soest et al. (2002)

Keane and Moffitt (1998)

Blundell et al. (1999, 2000)

Bargain et al. (2014) * † L and C denote heterogeneity in preferences for leisure and consumption, respectively. S denotes the disutility from welfare participation. FC refers to fixed costs of working and HR to hours restrictions. Robustness checks and alternative model specifications are separated by slashes.

Table 2: Wage imputation methods

Estimation

Approach

Sample

Selection

Imputation

Prediction

Error

Aaberge et al. (1995, 2009)

Aaberge et al. (1999)

Keane and Moffitt (1998) van Soest et al. (2002)

Blundell and Shephard (2012)

Simultaneous

Simultaneous

Simult./Two step *

Simultaneous

Simult./Two step — — — — —

Full sample

Full sample

Non-workers

Non-workers

Non-workers — — —

Integrated out

Integrated out van Soest (1995)

Euwals and van Soest (1999)

Blundell et al. (1999, 2000) van Soest and Das (2001)

Haan (2006)

Flood et al. (2007)

Dagsvik et al. (2011)

Two step

Two step

Two step

Two step

Two step

Two step

Two step

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Non-workers

Non-workers

Non-workers

Non-workers

Non-workers

Non-workers

Non-workers —/Integrated out

Integrated out

Integrated out

Integrated out — —/Integrated out —

Hoynes (1996)

Flood et al. (2004)

Dagsvik and Strøm (2006)

Bargain et al. (2014)

Two step

Two step

Two step

Two step

Yes

Yes

Yes

Yes

Full sample

Full sample

Full sample

Full sample — —

Integrated out

Random draw

Paper * Robustness checks and alternative model specifications are separated by slashes.

Fixed costs and hours restrictions can also be interpreted as measures for the availability of the respective choice alternatives (Aaberge et al., 2009). Less than half of the models explicitly allowed for stigma effects and non-take-up of welfare benefits. This is interesting due to the common finding that the benefit participation rate deviates substantially from full take-up. Thus, models that do not explicitly account for the potential disutility are expected to over-predict the number of recipients. Less variation can be found in terms of the model’s treatment of wages. While most studies estimate wages and the labor supply decision in a two-step procedure, only the models of Aaberge et al. (1995, and follow-ups), Keane and Moffitt (1998), van Soest et al. (2002) and Blundell and Shephard (2012) apply a simultaneous maximum likelihood procedure. In turn, these models neglect potential sample selection issues when estimating wages. As can be seen, there is no consensus in the literature whether predicted wages should be used only for individuals with unobserved wages or for the full sample, the advantage of the latter choice is there is eventually only one wage distribution. Regarding the handling of the wage prediction errors, it becomes increasingly common practice to incorporate and integrate out the errors during the estimation.

3 Data The baseline estimations in this paper are performed on the German Socio-Economic Panel (SOEP), a representative household panel survey for Germany (Wagner et al., 2007). SOEP includes now more than 24,000 individuals in around 11,000 households. We use the 2008 wave of SOEP, which provides household data from 2008, as well as data on the labor supply behavior and incomes from the preceding year (i.e. the year before the Great Recession). We rely on the tax and transfer system of 2007, focusing our analysis on the working age population and thus excluding individuals younger than 17 or above the retirement age of 65 from our estimations. Our sample is further restricted to those households where at least one decision maker can adjust her labor supply. Therefore, we exclude households where all decision makers are self-employed (since it is difficult to measure true hours and wages for those), civil servants 8 or in the military service. Moreover, our subsample includes some households with more than two adults, which mainly includes adult children living with their parents. We exclude these young adults from the estimation as it is unclear how their consumption and utility are determined (Dagsvik et al., 2011).

8 Tenured civil servants cannot freely adjust the weekly working hours. Note that we keep all other public sector employees.

As the labor supply decision is known to be rather heterogeneous across population subgroups, we separate the sample into five distinct demographical subpopulations. The first two groups are defined as single men and single women with or without dependent children. Our estimation subsample contains 779 households with single males and 1,065 households with single females. In addition, we specify three different kinds of couple households. First, we define 688 couple households in which the male partner has a flexible labor supply but the female partner is inflexible (e.g. due to self-employment or exclusion restrictions regarding the age). Second, we have 1,042 couple households in which the male partner has an inflexible labor supply but the female partner is flexible. In order to model the household labor supply decision of these “semi-flexible” couple households, we assume that the flexible partner faces his or her labor supply decision conditional on the labor supply behavior of the inflexible partner. Third, our sample includes 3,099 couple households in which both partners are flexible regarding their labor supply behavior. For the computation of consumption levels for the different choice categories, we rely on IZA’s policy simulation model IZAΨMOD (v3.0.0), which incorporates a very detailed representation of the German tax and benefit system (see Peichl et al., 2010, for a comprehensive documentation). Some of the estimated models would require applying the tax and benefit system for every possible wage rate for every household in every step of the numerical likelihood maximization, although doing so would slow down the estimation process substantially. To avoid this cumbersome procedure, we approximate the tax and benefit system by using a highly flexible second-degree polynomial that transforms monthly gross earnings into disposable income while controlling for a rich set of household characteristics, as well as all available sources of non-labor incomes. The resulting R 2 shows a very good fit of more than 99% for all population subgroups but single women (only 97% for them), which confirms that our approximation performs rather well. In order to also allow for unobserved tax determinants, we balance the predicted amounts of consumption by a single random draw for each household; otherwise, we would mistakenly reduce the variance in the consumption variable. The results are very much in line with those taking advantage of the full representation of the tax and transfer system, we are thus confident that the approximation does not affect our findings. As a robustness check, we compare our results obtained with German data to results for the USA. For this, we use data from IPUMS-CPS which is an integrated dataset of the March Current Population Survey (CPS) for 2007. In order to calculate income and payroll taxes, we use NBER’s simulation model TAXSIM.

Despite the presence of some robustness checks in the literature (see tables 1 and 2), these checks are usually narrowed down to a small deviation in just one of the modeling assumptions. By contrast, Evers et al. (2008) and Bargain and Peichl (2013) perform meta-analyses of labor supply models comparing estimated labor supply elasticities for different countries and explain them mainly by study characteristics. In either case, it is difficult to draw detailed and general conclusions on the specification of discrete choice models from the reported results. We overcome these difficulties by estimating a large variety of different modeling assumptions in a controlled environment using the same data. The estimation results allow us to determine how sensitive the estimated outcomes are with respect to the specification and the wage imputation procedure used in the model.

## 4.1 Analysis setup

For our analysis, we combine frequently used modeling assumptions and estimate all sensible combinations of these specifications. We estimate 3,456 different model specifications for the five distinct labor supply types, which leads us to 17,280 maximum likelihood estimations. However, the sample of estimation results is reduced because not all models did converge in a reasonable time span as we applied an automatic routine to find initial values and estimate this large number of models. We drop from our analysis those estimation results that did not converge. Depending on the labor supply group we lose up to 6 percent of our sample and end up with 16,730 different estimation results. 9 Table 3 shows the different specifications and the number of converged estimation results and reads as follows. We estimate 1,152 distinct models with a Box-Cox transformed utility specification for each of the five labor supply groups, although only 1,022 estimation results for single males and 1,132 for single females are included in our sample. Regardless of the functional form of the utility function, 1,152 of the estimated models neglect any kind of hours restrictions or fixed costs, 1,152 models include part-time restrictions and 1,152 models account for fixed costs of work.

In order to make the estimation results comparable across the different labor supply groups, we standardize the statistical fit and the estimated elasticities within a labor supply group. We subsequently pool the data and regress the estimation results on the different modeling assumptions (mainly represented as dummy variables). We

9 We drop models that did not converge after 100 iterations of Stata’s maximum likelihood implementation. Of course, more complex models take longer to converge. Apart from that, we do not find systematic effects of different types of assumptions on the probability of not converging.

Table 3: Estimated model combinations

Number of Converged Models *

Model Parameter

Option

## N

SgM

SgF

CoM

CoF

CoMF

Utility function

Box-Cox

Quadratic

Translog 1,152 1,152 1,152 1,022 1,152 1,125 1,132 1,151 1,144 951 1,152 1,148 1,148 1,133 1,148 1,029 1,152 1,143

Welfare stigma

No

Yes 1,728 1,728 1,642 1,657 1,701 1,726 1,607 1,644 1,713 1,716 1,664 1,660 —

Fixed costs

Part-time 1,152 1,152 1,152 1,091 1,064 1,144 1,141 1,137 1,149 1,040 1,061 1,150 1,131 1,149 1,149 1,109 1,063 1,152 — 10 5 288 1,584 1,584 288 1,440 1,571 288 1,564 1,575 283 1,429 1,539 288 1,559 1,582 286 1,456 1,582 — in C only in L only in L, C 864 864 864 864 835 827 827 810 864 862 858 843 822 834 798 797 860 861 859 849 834 822 836 832 — in C only in L only in L, C with correl.

576 864 576 864 576 574 863 520 804 538 571 853 574 856 573 566 846 523 795 521 570 862 569 854 574 574 863 541 791 555

Full sample

Non-workers 1,728 1,728 1,652 1,647 1,708 1,719 1,635 1,616 1,710 1,719 1,655 1,669 — 1 random draw

Integrated out 1,296 1,296 864 1,217 1,236 846 1,293 1,291 843 1,219 1,203 829 1,291 1,284 854 1,245 1,239 840 3,456 3,299 3,427 3,251 3,429 3,324

Hours restrictions

Number of Halton draws

Observed heterogeneity

Unobserved heterogeneity

Wage imputation

Wage prediction error Total * Single males (females) are denoted by SgM (SgF). Couples where only the male (female) partner has a flexible labor supply are denoted by CoM (CoF). CoMF denotes fully flexible couples. The column N refers to the number of possible model combinations for each choice whereas the subsequent columns report the number of converged models.

measure the statistical fit by the Akaike Information Criterion (AIC) of the models. To retrieve (uncompensated) labor supply elasticities, we increase the own-wage rates by ten percent and simulate the labor supply reaction to this wage change.

## 4.2 Estimation results

The results of these meta-regressions can be found in table 4. As the dependent variables have been standardized, the coefficients are difficult to interpret. Our results show, e.g. that using a quadratic utility function increases the AIC by 12% of a standard deviation in the sample and thereby worsens the statistical fit. These results have to be compared to a rather simple reference model using a translog utility Table 4: Marginal impact of modeling assumptions (SOEP)

Fit

Utility function

Quadratic

Box-Cox

Welfare stigma

Number of Halton draws

Hours restrictions

Part-time restrictions

Fixed costs

Observed heterogeneity in C only in L only in C and L

Unobserved heterogeneity in C only in L only in C and L in C and L (with correl.)

Wage imputation

Full sample, no correction

Full sample, error integrated out

Full sample, 1 random draw

Non-workers, error integrated out

Non-workers, 1 random draw

Constant

Labor supply types

Observations

## R 2

10% own wage elasticities

## AIC

Ext.

Int.

Total

## 0.119 ∗∗∗

(0.023) -0.020 (0.026)

## 0.968 ∗∗∗

(0.076) -0.010 ∗∗∗ (0.001)

## 0.124 ∗∗∗

(0.028)

## 0.116 ∗∗∗

(0.040) 0.045 (0.062) 0.005 (0.004) -0.015 (0.062)

## 0.080 ∗∗

(0.035) 0.065 (0.047) -0.003 (0.004) 0.004 (0.053)

## 0.085 ∗∗

(0.034) 0.065 (0.042) -0.002 (0.004) -1.647 ∗∗∗ (0.082) -1.093 ∗∗∗ (0.070)

## 0.384 ∗∗∗

(0.070)

## 0.481 ∗∗∗

(0.067)

## 0.105 ∗∗

(0.039)

## 0.187 ∗∗∗

(0.040)

## 0.152 ∗∗∗

(0.042)

## 0.238 ∗∗∗

(0.041) -0.335 ∗∗∗ (0.057) -0.381 ∗∗∗ (0.061) -0.475 ∗∗∗ (0.070) -0.049 (0.035) 0.048 (0.038) 0.016 (0.044)

## 0.060 ∗∗

(0.022)

## 0.045 ∗∗

(0.021) 0.012 (0.019)

## 0.043 ∗

(0.023)

## 0.046 ∗

(0.023) 0.013 (0.022) 0.005 (0.014) 0.005 (0.013) -0.041 ∗∗∗ (0.013) -0.119 ∗∗∗ (0.016) -0.006 (0.023) -0.081 ∗∗∗ (0.023) -0.037 (0.024) -0.082 ∗∗ (0.034) -0.059 ∗ (0.032) -0.029 (0.028) -0.069 ∗∗ (0.027) -0.102 ∗∗∗ (0.034) -0.051 (0.030) -0.037 (0.027) -0.064 ∗∗ (0.026) -0.101 ∗∗∗ (0.033) -0.811 ∗∗∗ (0.119) -0.530 ∗∗∗ (0.048) -0.104 ∗∗ (0.049) 0.000 (0.067) 0.070 (0.056)

## 2.121 ∗∗∗

(0.094)

## 1.399 ∗∗∗

(0.119) 0.071 (0.062) 0.048 (0.063) -0.230 ∗∗∗ (0.038)

## 2.235 ∗∗∗

(0.091)

## 1.385 ∗∗∗

(0.123) 0.131 (0.093) 0.040 (0.041) -0.232 ∗∗∗ (0.035)

## 2.240 ∗∗∗

(0.086)

## 1.406 ∗∗∗

(0.124) 0.121 (0.088) 0.041 (0.041) -0.235 ∗∗∗ (0.037)

## 1.004 ∗∗∗

(0.121)

Yes 16730 0.854 -0.939 ∗∗∗ (0.094)

Yes 13219 0.849 -0.678 ∗∗∗ (0.087)

Yes 13219 0.870 -0.726 ∗∗∗ (0.087)

Yes 13219 0.881 Notes: Uncompensated labor supply elasticities are simulated by increasing the individual wage rates by 10 percent and aggregating individual labor supply responses. Dependent variables have been standardized, i.e., an estimate of 1.0 indicates an increase of one standard deviation in the outcome. The AIC is negatively related to the statistical fit of the model—the better the fit, the lower the AIC. Standard errors clusted by labor supply group and wage imputation procedure. ∗ p < 0.1, ∗∗ p < 0.05, ∗∗∗ p < 0.01 function, neglecting observed and unobserved heterogeneity in preferences as well as fixed costs of working, hours restrictions or any stigma from welfare participation. In this reference model, we use observed wage rates for actual workers and predict wages for non-workers without incorporating the wage prediction error in the labor supply estimation. We find many statistically significant relationships. However, the presented standard errors are not bootstrapped, given that this would render our sensitivity analysis computationally infeasible. Bootstrapped standard errors would be substantially larger than those presented. As the coefficients are measured in standard deviations, only those of at least one standard deviation (in absolute values) are also economically interesting. We summarize the key findings below.

Goodness of fit. Although the statistical fit is usually not the main outcome of interest, our results show several interesting patterns for future applications (see table 4). First, the choice of the utility function does not systematically improve or worsen the statistical fit. Our analysis confirms the usual finding that the implementation of hours restrictions, fixed costs and observed preference heterogeneity clearly help to explain the labor supply choices. Estimating random coefficients models that also allow for unobserved heterogeneity yields little value-added compared to the computational burden of the estimation. The results regarding the wage imputation show that these specification decisions also affect the statistical fit of the model substantially. Predicting wages not only for non-workers but also for the full sample improves the fit significantly. However, this is unsurprising as it demonstrates how much of the variation in the data is lost by using predicted instead of actual wages for the full sample when not accounting for errors in the wage rate prediction. More generally, our results show that apart from the implementation of fixed costs or hours restrictions, there is hardly a single modeling assumption that guarantees a good fit. Instead, several small issues help to explain the observed labor market outcomes and add up to a good fit.

Labor supply elasticities. Even more important than the statistical fit is whether specific modeling assumptions systematically influence the out-of-sample predictions when simulating policy or wage changes. Figure 1 shows the distribution of labor supply elasticities across the converged models for the four labor supply types. 10 The graph shows considerable variation across the different modeling setups (within a specific labor supply group as well as across groups). In line with the literature, we find that the estimated elasticities are rather robust regarding the specification of the

10 We aggregated semi-flex couples and couples with two flexible partners to calculate elasticities.

utility function, as well as the implementation of observed and unobserved heterogeneity. This is reassuring as it shows that the frequently applied specifications do not restrict the labor supply decision a priori. The only (weak) exception seems to be the implementation of hours restrictions or fixed costs, which tend to drive extensive elasticities up. This finding supports the view that jobs with very few weekly working hours are harder to find than regular part-time or full-time jobs. It is thus more likely that people switch from non-participation to 20 or 40 than to 5 or 10 hours of work when accounting for this fact, which leads to higher elasticities at the extensive margin.

Figure 1: Labor supply elasticities of converged models

Singles, men

Singles, women

Couples, men

Couples, women 8 6 4

Density 2 0 8 6 4 2 0 0 .5 1 1.5 0 .5 1 1.5

Aggregated 10% own wage elasticities (total) Substantially more of the variation can be explained when analyzing the impact of the wage imputation and the handling of wage prediction errors. Our results hold the important message that this part of the model specification is much more relevant to the estimated elasticities than the utility specification. For instance, using predicted wages not only for non-workers but also for the full sample roughly doubles the estimated elasticities when not accounting for the wage prediction error. This substantial difference can be explained by the fact that predicting wages for the full sample reduces the variance of the wage distribution substantially. To explain the observed working hours with less variation in wages and thus income and consumption, the implied elasticities have to increase. Accounting for wage prediction errors and integrating them out during the estimation markedly reduces the difference. Interestingly, the results differ substantially depending on whether a single random draw or higher numbers are used. The ad hoc procedure of adding a single random draw tends to cancel out the effect of a full sample prediction. In contrast, correcting for the wage prediction error tends to reduce the elasticities, but we still observe the estimated elasticities to be significantly higher than those in which the wage rates were only imputed for non-workers.

Robustness. We performed a wide range of robustness checks to confirm that our results are not special to the used data and methods. In particular, we also used a different wave from the same data set and performed our analysis also using data from the CPS for the US (see table 8 in the online appendix). In addition to the marginal impact (holding all other specification details constant), we investigated the partial impact of the modeling assumptions (in table 9 in the online appendix), which only shows the differences in means due to the specific assumptions (e.g. mean of elasticities using a translog utility specification vs. mean of elasticities using other functional forms, irrespective of other modeling issues). The results we obtained were qualitatively the same. We also checked the robustness regarding the calculation of elasticities and found no differences whether we simulated 1% or 10% changes in the own-wage rate (table 10). Also switching the calculation of the elasticities from aggregated to mean, median or other quantile measures did not affect our findings (tables 11 and 12).

Summary. Our results partly confirm previous findings in the literature. While the empirical specification of the systematic utility function has an impact on the statistical fit, we find only little differences in the estimated elasticities. It thus may be justified to rely on simpler model setups when the computational burden is a major concern. However, the majority of applied robustness checks focus on the effects of different utility specifications and usually ignore how the underlying wage treatment may influence the results. We find that these assumptions explain much more variation in outcomes than the specification of the utility function. Most previous robustness checks have thus concentrated on issues of secondary order. Instead, more attention should be paid to the wage imputation and the handling of wage prediction errors. Modeling choices regarding the wage handling may thus also explain part of the large variation found in labor supply studies.

Our analysis shows that the wage imputation procedure and the handling of the wage prediction error have a huge impact on estimated labor supply elasticities. Nonetheless, it is common practice to estimate the labor supply decision conditional on observed or predicted wages. Wage rates are estimated beforehand and treated as exogenous within the labor supply estimation. This procedure reduces the computational burden, but is naturally rather restrictive. While there are some Hausman-type studies that loosen this fairly strong assumption and find correlation between wages and hours of work (Moffitt, 1984, Tummers and Woittiez, 1991), only little effort has been taken so far in the context of discrete choice labor supply models. Aaberge et al. (1995) and follow-ups estimate labor supply on a random choice set based upon draws from hours and wage distributions they estimate simultaneously. Breunig et al. (2008) and Blundell and Shephard (2012) assume a fixed individual-specific wage rate but allow one specific preference parameter to be correlated with the error term of the wage equation. Although this accounts for at least some interaction between preferences and wages, it still assumes that the labor supply decision is exogenous to the wage rate. Moreover, the correlation structure is rather arbitrary and restrictive. For instance, one may think of potential correlation between the wage rate and several different preference parameters. This issue is especially important as we expect that correlations between preferences and wages may drive the estimated elasticities. Consider two identical workers with the same observed characteristics but different unobservable productivity and thus wage rates. Suppose in case A that there are indeed no feedback effects between wages and preferences. Subsequently both workers will have the same preferences and their reaction to wage increases will only differ due to their initial consumption level. Now consider case B, in which preferences for, say, consumption are negatively correlated with productivity. Hence, the less productive worker has now a higher preference for consumption, whereas preferences of the more productive worker stay constant. As the less productive worker now values consumption and income more compared to case A, it follows that his labor supply elasticity increases. We show this mechanism in a simple model at the end of Appendix A.

## 5.1 Estimation setup

We propose a very flexible estimation strategy that overcomes the restrictive exogeneity assumptions of the standard estimation procedure in equation (5) to examine this issue empirically. More specific, we allow the wage rate to depend on hours of work and preferences for leisure and consumption to be correlated with the error term of the wage equation. However, to render this model feasible, we have to impose some distributional assumptions on the random terms. More precisely, preferences for consumption and leisure and the wage equation residuals are assumed to follow a multivariate normal distribution. We assume that wages are log-normally distributed and estimate them on tenure, education and dummies for having migrated, living in East Germany, being handicapped or working either part-time or overtime. Labor supply and wages are estimated jointly using a full information maximum likelihood framework:

!

0 ln w − x β

## 1 R

(r) (r) (r) (r) w,ni w ni ln (SL) = ∑ ln ∑ P U ni > U nj, ∀ j 6 = i β n, β w, e w,n =

## R

σ w n ∈ E r = 1 !

o

1 R n (r) (r) (r) (r) + ∑ ln

## P

## U

>

## U

, ∀ j 6 = i β , β , e w w,n n ni nj

R r ∑ n ∈ U = 1 ln w ni − x w,ni β 0 w − ln σ w (8) + ∑ ln φ σ w n ∈ E (r) (r) where U denotes the subset of unemployed individuals and β n, e w,n are the (randomly drawn) preference coefficients and the error terms of the log-wage equation, respectively. φ (·) is the density of a standard normal distribution. This framework relates to the estimation approach outlined in Blundell and Shephard (2012), although we approximate the likelihood function using a set of R Halton draws instead of Gaussian Hermite quadrature. Fitting preferences and wages jointly makes it possible to estimate both the influence of hours of work on the wage rate and the variancecovariance matrix of preferences and wages. See Appendix A for details on the model.

Identification. In order to separate and identify both effects properly, we use the actual wage equation residual for workers whose wage rate is observed (subset E), whereas we use multivariate normally distributed Halton sequences to integrate over a set of possible wage equation errors for unemployed individuals. While the standard model assumes preferences and wages to be exogenous, we allow for (multivariate normal) correlation patterns. This makes our estimation approach more flexible, but in turn places another functional form assumption on the estimated covariances. Chiou and Walker (2007) show that the use of small numbers of draws may mask identification of mixed logit models. We therefore run our estimations using different numbers of draws. While most studies rely on even fewer than 50 (Halton) draws, we use up to 4,000 Halton draws to check the robustness of our results. Reassuringly the estimated variance-covariance matrix is robust to the approximation in terms of both the coefficients and their standard errors with as few as 50 draws. Table 7 in Appendix B shows the estimation results for our most flexible model using different numbers of draws, varying between 10 and 4,000, indicating that the results are remarkably stable when using at least 50 draws.

## 5.2 Empirical results

Due to computational constraints, we only estimate our model for the subset of single females in our sample. Table 5 summarizes the results regarding the correlation patterns for this group. We do not present the complete table of estimates here to save space. Full results can be found in Appendix B (table 6). 11 The different models are defined as follows:

(1) Common two-step estimation assuming wages as exogenous.

(2) Estimates preferences and wages jointly.

(3) Extends (2) by allowing for hours-dependent wages.

(4) Extends (3) by additionally allowing for correlation between wages and preferences for consumption.

(5) Extends (4) by additionally allowing for correlation between wages and taste for leisure. Our results show that there is indeed correlation between wages and hours of work. For single women, working part-time yields a wage decrease of roughly 7% on average compared to a typical full-time job (see column (5)). The results are statistically significant different from zero at the 5% level. Working 50 or more hours a week is also connected to a decrease in hourly wages compared to full-time employment, although the effect is economically small and statistically not different from zero. These findings indicate an inverted U-shaped relationship between wages and hours of work, and thereby confirm the findings of Moffitt (1984) within the classical continuous hours approach. The estimated variance-covariance matrix between wages and preferences for consumption and leisure shows that there is also significant correlation, whereby we find that higher wages are strongly negatively correlated with preferences for consumption and positively correlated with preferences for leisure (suggesting a backward bending labor supply curve).

11 The estimated labor supply and wage equations show the expected signs for the covariates.

Table 5: Joint estimation results single females (1) (2)

Log-wages

Part time 0.038 (0.030) -0.107 ∗∗∗ (0.029)

Over time

## N

Pseudo R 2

Log-likelihood

## AIC

## BIC

Halton draws (3) 7455 0.175 -1710 3461 3607 50 7455 0.465 -2228 4513 4714 50 7455 0.466 -2220 4503 4717 50

Correlation ρ C,ln W (4) -0.041 (0.032) -0.053 (0.036) -0.075 ∗∗ (0.031) -0.016 (0.029) 7455 0.475 -2186 4438 4666 50 7455 0.477 -2176 4419 4654 50 -0.774 ∗∗∗ (0.061) -0.717 ∗∗∗ (0.088)

## 0.511 ∗∗∗

(0.107) 0.285 0.457 0.307 0.456 0.789 0.501 0.575 1.004 0.631 0.227 0.041 0.268 0.365 0.063 0.428 0.461 0.076 0.537 ρ L,ln W

Mean 10% Elasticities

Intensive

## 0.210 0.259

Extensive

## 0.308 0.450

Total

## 0.222 0.283

Aggregated 10% elasticities

Intensive

## 0.172 0.200

Extensive

## 0.030 0.039

Total

## 0.201 0.239

(5) Notes: Standard errors in parentheses, ∗ p < 0.1, ∗∗ p < 0.05, ∗∗∗ p < 0.01. Model (1) corresponds to a common two-step estimation assuming wages as exogeneous. Model (2) estimates preferences and wages jointly. Model (3) allows in addition wages to depend on hours of work. Model (4) also allows for correlation between wages and preferences for consumption. Model (5) extends model (4) by allowing in addition for correlation between wages and taste for leisure. Note that table 7 in Appendix B shows the estimation results for model (5) using different numbers of draws, varying between 10 and 4,000.

The statistical criteria show that models (3) to (5) clearly outperform model (2) irrespective of the specific measure. 12 Even more importantly, both intensive and extensive elasticities rise when the model allows for more flexible preference and wage patterns (compare model (1) to the other four models). In fact, switching from the most restrictive (1) to the most flexible model (5) more than doubles the estimated elasticities from above 0.2 to around 0.6—despite using the same data and identify12 An often used approach to evaluate the performance of different estimators is to run Monte Carlo simulations. However, in our setting, the (joint) significance of the additional regressors and the information criteria presented below allow us to conclude whether our flexible model outperforms the standard approach. In addition, the outcome of the Monte Carlo study depends on the data generating process. If it is chosen with a complex (without a) correlation structure, it would be tautological to conclude that the model allowing for correlation performs best (worst).

ing variation. Indeed, this is strongly in line with the theoretical intuition described above. Our results show that the usual approach to estimate wages separately and independently from the labor supply decision neglects important correlation patterns that determine a households’ response to wage changes, driving elasticities towards zero. Hence, when allowing for a more flexible specification, microeconometrically estimated elasticities come closer to macroeconomic ones (Keane, 2011, Chetty et al., 2011, Keane and Rogerson, 2012). One reason for this could be that the more flexible model implicitly captures some of the frictions that are seen as key in explaining these differences. It would be interesting to explicitly incorporate frictions, which are right now captured, among other things, by, e.g., dummies for different hour categories, into the structural estimation and compare the findings to our results in future research.

6 Conclusion Structural labor supply models are frequently used in the empirical labor supply analysis for many different purposes. In recent years, it has become a standard procedure to estimate labor supply decisions as a choice among a set of different hours alternatives or job opportunities. In contrast to this popularity, little is known about how the numerous modeling assumptions influence the statistical fit, as well as the estimated labor supply elasticities. In this paper, we provide an overview of the most important specification issues and conduct a comprehensive sensitivity analysis to disentangle the driving factors behind the results from structural labor supply models. Our results show that even if the modeling assumptions concerning the direct utility specification increase or worsen the statistical fit, i.e. the power to explain the observed labor supply behavior, the models are robust in terms of estimated labor supply elasticities. In contrast, the models are highly sensitive to changes in the underlying wage distribution, a mechanisms almost completely neglected in the literature to date. Thus, the question of whether to use predicted or observed wages for actual workers and whether and how to integrate the wage prediction error out during the estimation process has a large and statistically significant impact on the statistical fit of the model and the estimated labor supply elasticities. We further tackle this issue and propose an alternative estimation method that overcomes the restrictive independence assumptions between wages and work preferences. We allow for correlation between wages and preferences, as well as wage rates that depend on hours of work. Our results show that there are indeed significant correlation patterns in both dimension, which were usually ignored in previous empirical applications. While the standard approach assumes that every worker faces a fixed wage rate irrespective of hours of work, we find that working part-time significantly lowers the hourly wage rate by 7 %. Moreover, we find significant correlation between wages and preferences for both leisure and consumption. Our findings clearly reject the exogeneity assumptions that are implicitly made in most discrete choice labor supply applications. Our findings have important implications for tax policy design. Diamond and Saez (2011) derive simple formulas for the optimal (top) marginal tax rates based upon labor supply elasticities. 13 They assume an elasticity of 0.25 as an “a mid-range estimate from the empirical literature” which is close to our estimate for the restrictive model. This leads to an optimal top marginal tax rate of τ = 1 + 1.5 1 ∗ 0.25 = 72.7 %. However, an elasticity of 0.6 as found in our most flexible model reduces the optimal tax rate to 52.6% bringing it closer to actually observed values (the top labor tax rate in the US is 42.5 %). While we cannot claim that we have identified the true value for the labor supply elasticity—which might not even exist—our analysis shows that more attention should be paid to the specification of structural labor supply models before using them for policy analysis.

13 The 1 − g formula for the optimal top tax rate is τ = 1 − g + ae where g is the marginal social welfare weight for the top earners, a is the parameter of the Pareto (income) distribution and e is the labor supply elasticity. Diamond and Saez (2011) assume g = 0 to derive the optimal revenue maximizing top tax rate and use an estimated Pareto coefficient of 1.5 for the US.

## References

Aaberge, R., Colombino, U. and Strøm, S. (1999). Labour Supply in Italy: An Empirical Analysis of Joint Houshold Decisions, with Taxes and Quantity Constraints, Journal of Applied Econometrics 14(4): 403–422. Aaberge, R., Colombino, U. and Wennemo, T. (2009). Evaluating Alternative Representations of the Choice Sets in Models of Labor Supply, Journal of Economic Surveys 23(3): 586–612. Aaberge, R., Dagsvik, J. K. and Strøm, S. (1995). Labor Supply Responses and Welfare Effects of Tax Reforms, The Scandinavian Journal of Economics 97(4): 635–659. Alesina, A. F., Glaeser, E. L. and Sacerdote, B. (2006). Work and Leisure in the United States and Europe: Why So Different?, NBER Macroeconomics Annual 2005, Vol. 20, MIT Press, pp. 1–64. Bargain, O., Orsini, K. and Peichl, A. (2014). Comparing Labor Supply Elasticities in Europe and the US: New Results, Journal of Human Resources (forthcoming). Bargain, O. and Peichl, A. (2013). Steady-State Labor Supply Elasticities: An International Comparison, IZA Discussion Paper 7698. Blanchard, O. (2007). Comment on “Do Taxes Explain European Employment? Indivisible Labor, Human Capital, Lotteries, and Savings” (by L. Ljungqvist and T. J. Sargent), NBER Macroeconomics Annual 2006, Vol. 21, MIT Press, pp. 225–232. Bloemen, H. G. and Kapteyn, A. (2008). The estimation of utility-consistent labor supply models by means of simulated scores, Journal of Applied Econometrics 23(4): 395– 422. Blundell, R., Duncan, A., McCrae, J. and Meghir, C. (1999). Evaluating In-Work Benefit Reform: the Working Families Tax Credit in the UK. paper presented at the Joint Center for Poverty Research conference, Northwestern University. Blundell, R., Duncan, A., McCrae, J. and Meghir, C. (2000). The Labour Market Impact of the Working Families’ Tax Credit, Fiscal Studies 21(1): 75–104. Blundell, R. and MaCurdy, T. E. (1999). Labor Supply: A Review of Alternative Approaches, in O. Ashenfelter and D. Card (eds), Handbook of Labor Economics, NorthHolland, Amsterdam. Blundell, R. and Shephard, A. (2012). Employment, Hours of Work and the Optimal Taxation of Low-Income Families, Review of Economic Studies 79(2): 481–510.

Borjas, G. J. (1980). The Relationship between Wages and Weekly Hours of Work: The Role of Division Bias, Journal of Human Resources 15(3): 409–423. Breunig, R., Cobb-Clark, D. A. and Gong, X. (2008). Improving the Modelling of Couples’ Labour Supply, Economic Record 84(267): 466–485. Chetty, R. (2012). Bounds on Elasticities with Optimization Frictions: A Synthesis of Micro and Macro Evidence on Labor Supply, Econometrica 80(3): 969–1018. Chetty, R., Guren, A., Manoli, D. and Weber, A. (2011). Are Micro and Macro Labor Supply Elasticities Consistent? A Review of Evidence on the Intensive and Extensive Margins, American Economic Review: Papers and Proceedings 101(3): 471–475. Chiou, L. and Walker, J. L. (2007). Masking identification of discrete choice models under simulation methods, Journal of Econometrics 141(2): 683–703. Dagsvik, J. K., Jia, Z., Orsini, K. and van Camp, G. (2011). Subsidies on low-skilled workers’ social security contributions: the case of Belgium, Empirical Economics 40(3): 779–806. Dagsvik, J. K. and Strøm, S. (2004). Sectoral Labor Supply, Choice Restrictions and Functional Form, Discussion Papers Statistics Norway 388. Dagsvik, J. K. and Strøm, S. (2006). Sectoral Labor Supply, Choice Restrictions and Functional Form, Journal of Applied Econometrics 21(6): 803–826. Diamond, P. and Saez, E. (2011). The Case for a Progressive Tax: From Basic Research to Policy Recommendations, Journal of Economic Perspectives 25(4): 165–190. Eissa, N., Kleven, H. J. and Kreiner, C. T. (2008). Evaluation of Four Tax Reforms in The United States: Labor Supply and Welfare Effects For Single Mothers, Journal of Public Economics 92(3-4): 795–816. Eklöf, M. and Sacklén, H. (2000). The Hausman-MaCurdy Controversy: Why Do the Results Differ across Studies?, Journal of Human Resources 35(1): 204–220. Ericson, P. and Flood, L. (1997). A Monte Carlo Evaluation of Labor Supply Models, Empirical Economics 22(3): 431–460. Euwals, R. and van Soest, A. (1999). Desired and actual labour supply of unmarried men and women in the Netherlands, Labour Economics 6(1): 95–118. Evers, M., de Mooij, R. and van Vuuren, D. (2008). The Wage Elasticity of Labour Supply: A Synthesis of Empirical Estimates, De Economist 156(1): 25–43.

Flood, L., Hansen, J. and Wahlberg, R. (2004). Household Labor Supply and Welfare Participation in Sweden, Journal of Human Resources 39(4): 1008–1032. Flood, L., Wahlberg, R. and Pylkkänen, E. (2007). From Welfare to Work: Evaluating a Tax and Benefit Reform Targeted at Single Mothers in Sweden, LABOUR 21(3): 443– 471. Haan, P. (2006). Much ado about nothing: conditional logit vs. random coefficient models for estimating labour supply elasticities, Applied Economics Letters 13(4): 251– 256. Hausman, J. A. (1981). Labor Supply, in H. J. Aaron and J. A. Pechman (eds), How taxes affect economic behavior, Brookings Institution, pp. 27–72. Hoynes, H. W. (1996). Welfare Transfers in Two-Parent Families: Labor Supply and Welfare Participation Under AFDC-UP, Econometrica 64(2): 295–332. Immervoll, H., Kleven, H. J., Kreiner, C. T. and Verdelin, N. (2011). Optimal tax and transfer programs for couples with extensive labor supply responses, Journal of Public Economics 95(11): 1485–1500. Keane, M. P. (2010). Structural vs. atheoretic approaches to econometrics, Journal of Econometrics 156(1): 3–20. Keane, M. P. (2011). Labor Supply and Taxes: A Survey, Journal of Economic Literature 49(4): 961–1075. Keane, M. P. and Moffitt, R. (1998). A Structural Model of Multiple Welfare Program Participation and Labor Supply, International Economic Review 39(3): 553–589. Keane, M. P. and Wasi, N. (2012). Comparing Alternative Models of Heterogeneity in Consumer Choice Behavior, Journal of Applied Econometrics 28(6): 1018–1045. Keane, M. and Rogerson, R. (2012). Micro and Macro Labor Supply Elasticities: A Reassessment of Conventional Wisdom, Journal of Economic Literature 50(2): 464–476. Löffler, M. (2013). Fitting Complex Mixed Logit Models: An Application to Labor Supply. Mimeo, presented at the Stata Conference in New Orleans, July 2013. Luce, R. D. (1959). Individual Choice Behavior: A Theoretical Analysis, Wiley, New York. MaCurdy, T. E., Green, D. and Paarsch, H. (1990). Assessing Empirical Approaches for Analyzing Taxes and Labor Supply, Journal of Human Resources 25(3): 412–490.

McFadden, D. (1974). Conditional logit analysis of qualitative choice behavior, in P. Zarembka (ed.), Frontiers in Econometrics, Academic Press, New York. Moffitt, R. (1983). An Economic Model of Welfare Stigma, American Economic Review 73(5): 1023–1035. Moffitt, R. (1984). The Estimation of a Joint Wage-Hours Labor Supply Model, Journal of Labor Economics 2(4): 550–566. Peichl, A., Schneider, H. and Siegloch, S. (2010). Documentation IZAΨMOD: The IZA Policy Simulation Model, IZA Discussion Papers 4865. Train, K. E. (2009). Discrete Choice Methods with Simulation, second edn, Cambridge University Press. Tummers, M. P. and Woittiez, I. (1991). A Simultaneous Wage and Labor Supply Model With Hours Restrictions, Journal of Human Resources 26(3): 393–423. van Soest, A. (1995). Structural Models of Family Labor Supply – A Discrete Choice Approach, Journal of Human Resources 30(1): 63–88. van Soest, A. and Das, M. (2001). Family Labor Supply and Proposed Tax Reforms in the Netherlands, De Economist 149(2): 191–218. van Soest, A., Das, M. and Gong, X. (2002). A structural labour supply model with flexible preferences, Journal of Econometrics 107(1-2): 345–374. Wagner, G. G., Frick, J. R. and Schupp, J. (2007). The German Socio-Economic Panel Study (SOEP) – Scope, Evolution and Enhancements, Journal of Applied Social Science Studies 127(1): 139–169. Ziliak, J. P. and Kniesner, T. J. (1999). Estimating life-cycle labor supply tax effects, Journal of Political Economy 107(2): 326–359.

A Joint estimation For the joint maximum likelihood estimation in Section 5, we use a Box-Cox transformed utility specification. Thus, the systematic utility of individual n choosing alternative j is given by:

(λ) (λ) (λ) (λ) v C nj, L j = x n β 0 1 + β C,n C nj C + β 2 C nj C L j L + x n β 0 3 + β L,n L j L + β FC,n 1 (h j > 0) + β 4 1 (h j = 20) + β 5 1 (h j = 40) (λ) (λ L) with C nj C and L j (λ)

C nj C = (9) defined as:

 ∗ λ  C nj C − 1 λ C  ln C ∗ nj if λ C 6 = 0 (λ L)

L j if λ C = 0 ∗

C nj = C nj /1000 =  ∗ λ  L j L − 1 λ L  ln L ∗ j if λ L 6 = 0 (10) if λ L = 0

L ∗ nj = L nj /80 (11) and wages given by the wage equation:

ln w n = z n γ 0 + e w,n (12) We further assume that preferences (β C,n, β L,n, β FC,n) and wages (the residual e w,n of the log-wage equation) are multivariate normally distributed:

      e w,n β C,n β L,n β FC,n           ∼ N  µ =        0 β C β L β FC      

## , Ω = 

    σ w 2 σ C,w σ C 2 σ L,w σ C,L σ L 2 2 0 σ C,FC σ L,FC σ FC       0

##  = LL 

    (13) Instead of estimating the variance-covariance-matrix directly, we estimate its Cholesky decomposition L. As we cannot directly simulate from the joint distribution, we draw (r) R Halton sequences µ i,n (i = 1,..., 4, r = 1,..., R) from a standard normal and transform them accordingly to the estimated factorization L:

 (r) ê w,n  (r)  β̂ C,n   (r)  β̂ L,n (r) β̂ FC,n        =      0 β̂ C β̂ L β̂ FC        +      l ˆ w,w 0 0 0 l ˆ C,w l ˆ C,C 0 0 l ˆ L,w 0 l ˆ L,L 0 0 0 0 l ˆ FC,FC (r)    (r)   µ 2,n     (r)   µ 3,n (r) µ 4,n        µ 1,n (14) (r) We use the actual wage equation residual if the wage is observed, thus µ 1,n = x w,n β̂ 0 w .

(r) σ w and µ i,n ∼ N (0, 1) (i = 2, 3, 4). If individual n is unemployed ln w n − and we do not observe her wage rate, we also draw her log-wage equation residual (r) from a normal distribution, µ 1,n ∼ N (0, 1). Using a simplified version of the above model makes it possible to show how the commonly neglected covariance terms influence resulting labor supply elasticities. Consider the utility function outlined in equation (9) and set β 1, β 2, β 3, β FC,n, β 4, β 5, λ C and λ L equal to zero and give β L,n zero variance for simplicity. Now let us assume that leisure is the residual of total time of the week minus hours worked (L j = T − H j) and consumption is a function of wages, hours and non-labor income (C nj = w n H j + R n ). The agent’s problem can subsequently be written as:

max β C,n ln C n,j + β L,n ln L j = max β C,n ln (w n H j + R n) + β L,n ln (T − H j).

## H

## H

(15) It follows from utility maximization that the labor supply function is given by:

H n ∗ = β C,n T β L,n R n − w − 1.

β L,n + β C,n β L,n + β C,n n (16) We can derive individual labor supply elasticities as:

e H,w,n = β L,n R n /T ∂H n ∗ w n = .

∗ ∂w n H n β C,n w n − β L,n R n /T (17) The elasticity depends inversely on the product of preferences for consumption β C,n and hourly wage rates w n. Moreover, β C,n and ln w n are assumed to be bivariate normally distributed (see equation (13)). It follows that labor supply elasticities decrease with increasing covariance between wages and consumption preferences.

B Joint estimation results Table 6: Joint estimation results single females—full results (1)

Preferences

C × Age

C × Age 2

C × Handicap

## 0.678 ∗∗∗

(0.204) -0.008 ∗∗∗ (0.002) 0.527 (1.550) (2) (3)

## 0.920 ∗∗∗

(0.315) -0.011 ∗∗∗ (0.004) 1.457 (2.044)

## 0.698 ∗∗∗

(0.184) -0.008 ∗∗∗ (0.002) 1.194 (1.627) (4)

## 0.569 ∗∗∗

(0.213) -0.007 ∗∗∗ (0.003) 1.507 (1.936) (5)

## 0.591 ∗∗∗

(0.221) -0.007 ∗∗∗ (0.003) 1.675 (1.909)

## C

## C × L

λ C

L × Age

L × Age 2

L × Handicap

L × Care

L × Children 2

L × Children 3,6

L × Children 7,16

## L

λ L

Restrictions

Fixed costs 1 (h = 20) 1 (h = 40)

Log-wages

Tenure

Tenure 2 /100

University

Unskilled

East

Foreigner

Handicapped -8.253 ∗∗ (3.910)

## 0.801 ∗∗

(0.354) 0.255 (0.183) 0.093 (0.095) -0.001 (0.001) 0.440 (0.785)

## 2.624 ∗∗

(1.284)

## 1.536 ∗

(0.894) 0.456 (0.306)

## 0.402 ∗∗

(0.160) -1.296 (1.875) -0.775 ∗∗ (0.371) -7.741 (4.746)

## 1.042 ∗

(0.542) 0.164 (0.140) 0.075 (0.105) -0.000 (0.001) 0.888 (0.922)

## 3.700 ∗

(1.890) 1.847 (1.135) 0.401 (0.358)

## 0.393 ∗∗

(0.192) 0.382 (1.867) -0.988 ∗∗∗ (0.315) -7.740 ∗∗ (3.458) 0.491 (0.392) 0.302 (0.202) 0.104 (0.084) -0.001 (0.001) 0.592 (0.751)

## 2.749 ∗∗

(1.361)

## 1.575 ∗

(0.892) 0.436 (0.296)

## 0.384 ∗∗

(0.153) -1.204 (1.491) -0.754 ∗∗∗ (0.275) -1.031 (3.964)

## 0.797 ∗

(0.466)

## 0.485 ∗∗∗

(0.120) 0.059 (0.116) -0.000 (0.001) 0.809 (1.071)

## 4.337 ∗∗

(1.938)

## 2.113 ∗

(1.185) 0.220 (0.372)

## 0.364 ∗

(0.213) 1.448 (2.317) -0.736 ∗∗ (0.308) -0.194 (3.936) -0.352 (0.475)

## 0.330 ∗∗

(0.130) 0.043 (0.103) 0.000 (0.001) 0.610 (0.938)

## 4.000 ∗∗

(1.787)

## 2.054 ∗

(1.099) 0.233 (0.333)

## 0.348 ∗

(0.197) 2.787 (2.025) -1.013 ∗∗∗ (0.320) -0.745 ∗∗ (0.319) -0.071 (0.123)

## 0.811 ∗∗∗

(0.089) -1.000 ∗∗∗ (0.232) -0.063 (0.124)

## 0.739 ∗∗∗

(0.095) -1.109 ∗∗∗ (0.185) -0.029 (0.126)

## 0.628 ∗∗∗

(0.128) -1.078 ∗∗∗ (0.209) -0.070 (0.126)

## 0.411 ∗∗

(0.195) -1.049 ∗∗∗ (0.206) -0.124 (0.128)

## 0.407 ∗∗

(0.201)

## 0.051 ∗∗∗

(0.005) -0.089 ∗∗∗ (0.014)

## 0.295 ∗∗∗

(0.033) -0.259 ∗∗∗ (0.057) -0.287 ∗∗∗ (0.037) -0.072 (0.072) -0.192 ∗∗

## 0.052 ∗∗∗

(0.005) -0.091 ∗∗∗ (0.014)

## 0.310 ∗∗∗

(0.033) -0.266 ∗∗∗ (0.057) -0.286 ∗∗∗ (0.037) -0.070 (0.071) -0.205 ∗∗

## 0.049 ∗∗∗

(0.004) -0.084 ∗∗∗ (0.013)

## 0.276 ∗∗∗

(0.031) -0.272 ∗∗∗ (0.051) -0.242 ∗∗∗ (0.035) -0.060 (0.065) -0.195 ∗∗

## 0.045 ∗∗∗

(0.004) -0.075 ∗∗∗ (0.012)

## 0.253 ∗∗∗

(0.029) -0.255 ∗∗∗ (0.047) -0.209 ∗∗∗ (0.033) -0.045 (0.059) -0.179 ∗∗ (0.082)

Part time

Over time

## 2.169 ∗∗∗

(0.030)

Constant (0.082) 0.038 (0.030) -0.107 ∗∗∗ (0.029)

## 2.170 ∗∗∗

(0.034) (0.084) -0.041 (0.032) -0.053 (0.036)

## 2.219 ∗∗∗

(0.034) (0.083) -0.075 ∗∗ (0.031) -0.016 (0.029)

## 2.251 ∗∗∗

(0.033)

## 0.447 ∗∗∗

(0.011) -2.040 ∗∗∗ (0.529)

## 1.982 ∗∗∗

(0.723)

## 0.957 ∗∗∗

(0.286)

## 1.607 ∗∗∗

(0.487) 0.357 (0.575)

Cholesky matrix l ln W 0.249 (1.158)

## 2.838 ∗∗

(1.127)

## 1.361 ∗∗∗

(0.504)

## 0.450 ∗∗∗

(0.011) -2.249 ∗∗∗ (0.640)

## 1.838 ∗∗∗

(0.682) 0.286 (0.889) 0.939 (0.730)

## 1.496 ∗∗∗

(0.543) 0.842 (0.614) 0.095 (0.382) 0.220 (0.477)

## 1.605 ∗∗

(0.684) 0.413 (0.570) 7455 0.466 -2220 4503 4717 50 7455 0.475 -2186 4438 4666 50 l C,ln W l C l L,ln W l L l FC

## N

Pseudo R 2

Log-likelihood

## AIC

## BIC

Halton draws 7455 0.175 -1710 3461 3607 50 7455 0.465 -2228 4513 4714 50

Correlation ρ C,ln W -0.774 ∗∗∗ (0.061) -0.717 ∗∗∗ (0.088)

## 0.511 ∗∗∗

(0.107) ρ L,ln W

Aggregated 10% elasticities

Intensive 0.172

Extensive 0.030

Total 0.201

Mean 10% Elasticities

Intensive 0.210

Extensive 0.308

Total 0.222 7455 0.477 -2176 4419 4654 50 0.200 0.039 0.239 0.227 0.041 0.268 0.365 0.063 0.428 0.461 0.076 0.537 0.259 0.450 0.283 0.285 0.457 0.307 0.456 0.789 0.501 0.575 1.004 0.631

Notes: Standard errors in parentheses, ∗ p < 0.1, ∗∗ p < 0.05, ∗∗∗ p < 0.01.

Table 7: Joint estimation results single females—sensitivity of model (5) w.r.t. number of Halton draws (1)

Preferences

C × Age

C × Age 2

C × Handicap

## C

## C × L

λ C

L × Age

L × Age 2

L × Handicap

L × Care

L × Children 2

L × Children 3,6

L × Children 7,16

## L

λ L

Restrictions

Fixed costs 1 (h = 20) 1 (h = 40)

Log-wages

Tenure

Tenure 2 /100 (2) (3) (4) (5) (6) (7)

## 0.463 ∗∗∗

(0.168) -0.006 ∗∗∗ (0.002) 1.525 (1.590) -1.943 (3.312) -0.286 (0.495)

## 0.315 ∗∗

(0.148) 0.060 (0.106) -0.000 (0.001) 0.582 (0.962)

## 3.263 ∗∗

(1.423)

## 1.657 ∗

(0.879) 0.159 (0.302) 0.267 (0.169) 1.397 (2.055) -0.580 ∗∗ (0.232)

## 0.591 ∗∗∗

(0.221) -0.007 ∗∗∗ (0.003) 1.675 (1.909) -0.194 (3.936) -0.352 (0.475)

## 0.330 ∗∗

(0.130) 0.043 (0.103) 0.000 (0.001) 0.610 (0.938)

## 4.000 ∗∗

(1.787)

## 2.054 ∗

(1.099) 0.233 (0.333)

## 0.348 ∗

(0.197) 2.787 (2.025) -1.013 ∗∗∗ (0.320)

## 0.538 ∗∗

(0.211) -0.007 ∗∗∗ (0.003) 1.379 (1.846) 0.458 (3.891) -0.311 (0.459)

## 0.349 ∗∗∗

(0.135) 0.020 (0.100) 0.000 (0.001) 0.451 (0.895)

## 3.769 ∗∗

(1.697)

## 2.050 ∗

(1.073) 0.290 (0.340)

## 0.362 ∗

(0.194) 3.010 (1.991) -1.067 ∗∗∗ (0.335)

## 0.546 ∗∗

(0.219) -0.007 ∗∗∗ (0.003) 1.309 (1.855) 0.829 (4.023) -0.324 (0.467)

## 0.346 ∗∗∗

(0.134) 0.016 (0.101) 0.000 (0.001) 0.384 (0.869)

## 3.821 ∗∗

(1.733)

## 2.088 ∗

(1.096) 0.319 (0.357)

## 0.360 ∗

(0.194) 3.201 (2.037) -1.116 ∗∗∗ (0.333)

## 0.543 ∗∗

(0.217) -0.007 ∗∗∗ (0.003) 1.250 (1.799) 0.867 (3.998) -0.313 (0.476)

## 0.350 ∗∗∗

(0.135) 0.017 (0.101) 0.000 (0.001) 0.345 (0.830)

## 3.819 ∗∗

(1.733)

## 2.091 ∗

(1.095) 0.312 (0.354)

## 0.361 ∗

(0.193) 3.195 (2.026) -1.115 ∗∗∗ (0.339)

## 0.540 ∗∗

(0.215) -0.007 ∗∗∗ (0.003) 1.264 (1.808) 0.683 (3.960) -0.306 (0.472)

## 0.351 ∗∗∗

(0.136) 0.018 (0.101) 0.000 (0.001) 0.357 (0.849)

## 3.795 ∗∗

(1.714)

## 2.076 ∗

(1.084) 0.303 (0.350)

## 0.364 ∗

(0.195) 3.113 (2.017) -1.090 ∗∗∗ (0.338)

## 0.540 ∗∗

(0.215) -0.007 ∗∗∗ (0.003) 1.299 (1.818) 0.742 (3.969) -0.312 (0.474)

## 0.349 ∗∗

(0.136) 0.018 (0.101) 0.000 (0.001) 0.380 (0.855)

## 3.805 ∗∗

(1.716)

## 2.079 ∗

(1.085) 0.304 (0.351)

## 0.362 ∗

(0.194) 3.137 (2.022) -1.091 ∗∗∗ (0.335) -0.949 ∗∗∗ (0.187) -0.094 (0.124)

## 0.497 ∗∗∗

(0.159) -1.049 ∗∗∗ (0.206) -0.124 (0.128)

## 0.407 ∗∗

(0.201) -1.076 ∗∗∗ (0.201) -0.128 (0.128)

## 0.428 ∗∗

(0.196) -1.088 ∗∗∗ (0.202) -0.136 (0.129)

## 0.422 ∗∗

(0.200) -1.086 ∗∗∗ (0.202) -0.136 (0.129)

## 0.422 ∗∗

(0.200) -1.081 ∗∗∗ (0.201) -0.131 (0.128)

## 0.424 ∗∗

(0.199) -1.081 ∗∗∗ (0.201) -0.132 (0.128)

## 0.423 ∗∗

(0.199)

## 0.045 ∗∗∗

(0.004) -0.075 ∗∗∗

## 0.045 ∗∗∗

(0.004) -0.075 ∗∗∗

## 0.045 ∗∗∗

(0.004) -0.075 ∗∗∗

## 0.045 ∗∗∗

(0.004) -0.075 ∗∗∗

## 0.045 ∗∗∗

(0.004) -0.075 ∗∗∗

## 0.045 ∗∗∗

(0.004) -0.075 ∗∗∗

## 0.045 ∗∗∗

(0.004) -0.075 ∗∗∗

University

Unskilled

East

Foreigner

Handicapped

Part time

Over time

Constant

Cholesky matrix l ln W l C,ln W l C l L,ln W l L l FC

## N

Pseudo R 2

Log-likelihood

## AIC

## BIC

Halton draws

Correlation ρ C,ln W ρ L,ln W (0.012)

## 0.253 ∗∗∗

(0.029) -0.258 ∗∗∗ (0.047) -0.209 ∗∗∗ (0.034) -0.053 (0.059) -0.184 ∗∗ (0.082) -0.069 ∗∗ (0.033) -0.052 (0.033)

## 2.259 ∗∗∗

(0.034) (0.012)

## 0.253 ∗∗∗

(0.029) -0.255 ∗∗∗ (0.047) -0.209 ∗∗∗ (0.033) -0.045 (0.059) -0.179 ∗∗ (0.083) -0.075 ∗∗ (0.031) -0.016 (0.029)

## 2.251 ∗∗∗

(0.033) (0.012)

## 0.249 ∗∗∗

(0.029) -0.257 ∗∗∗ (0.046) -0.207 ∗∗∗ (0.033) -0.047 (0.058) -0.175 ∗∗ (0.083) -0.076 ∗∗ (0.032) -0.011 (0.031)

## 2.252 ∗∗∗

(0.033) (0.012)

## 0.248 ∗∗∗

(0.029) -0.256 ∗∗∗ (0.046) -0.206 ∗∗∗ (0.033) -0.046 (0.058) -0.174 ∗∗ (0.083) -0.079 ∗∗ (0.031) -0.006 (0.031)

## 2.253 ∗∗∗

(0.033) (0.012)

## 0.248 ∗∗∗

(0.029) -0.256 ∗∗∗ (0.046) -0.205 ∗∗∗ (0.033) -0.046 (0.058) -0.173 ∗∗ (0.083) -0.079 ∗∗ (0.032) -0.005 (0.032)

## 2.253 ∗∗∗

(0.033) (0.012)

## 0.248 ∗∗∗

(0.029) -0.256 ∗∗∗ (0.046) -0.206 ∗∗∗ (0.033) -0.046 (0.058) -0.174 ∗∗ (0.083) -0.078 ∗∗ (0.032) -0.008 (0.031)

## 2.253 ∗∗∗

(0.033) (0.012)

## 0.248 ∗∗∗

(0.029) -0.256 ∗∗∗ (0.046) -0.206 ∗∗∗ (0.033) -0.046 (0.058) -0.174 ∗∗ (0.083) -0.078 ∗∗ (0.032) -0.008 (0.031)

## 2.253 ∗∗∗

(0.033)

## 0.444 ∗∗∗

(0.011) -1.244 ∗∗∗ (0.267)

## 0.789 ∗

(0.403)

## 0.820 ∗∗∗

(0.239) 0.555 (0.487) 0.284 (0.310)

## 0.447 ∗∗∗

(0.011) -2.040 ∗∗∗ (0.529)

## 1.982 ∗∗∗

(0.723)

## 0.957 ∗∗∗

(0.286)

## 1.607 ∗∗∗

(0.487) 0.357 (0.575)

## 0.447 ∗∗∗

(0.011) -1.959 ∗∗∗ (0.494)

## 1.791 ∗∗∗

(0.692)

## 0.942 ∗∗∗

(0.283)

## 1.532 ∗∗∗

(0.459) 0.084 (0.663)

## 0.447 ∗∗∗

(0.011) -2.050 ∗∗∗ (0.534)

## 1.928 ∗∗

(0.748)

## 0.980 ∗∗∗

(0.295)

## 1.609 ∗∗∗

(0.495) 0.051 (0.704)

## 0.447 ∗∗∗

(0.011) -2.057 ∗∗∗ (0.525)

## 1.925 ∗∗∗

(0.719)

## 0.985 ∗∗∗

(0.295)

## 1.607 ∗∗∗

(0.487) -0.054 (0.677)

## 0.447 ∗∗∗

(0.011) -2.021 ∗∗∗ (0.520)

## 1.876 ∗∗∗

(0.712)

## 0.965 ∗∗∗

(0.289)

## 1.572 ∗∗∗

(0.475) 0.005 (0.671)

## 0.447 ∗∗∗

(0.011) -2.023 ∗∗∗ (0.514)

## 1.881 ∗∗∗

(0.706)

## 0.969 ∗∗∗

(0.290)

## 1.578 ∗∗∗

(0.476) -0.002 (0.675) 7455 0.476 -2179 4427 4662 10 -0.845 ∗∗∗ (0.108)

## 0.828 ∗∗∗

(0.231)

Aggregated 10% elasticities

Intensive 0.463

Extensive 0.074 7455 0.477 -2176 4419 4654 50 7455 0.477 -2176 4420 4655 250 7455 0.477 -2176 4419 4655 500 7455 0.477 -2175 4419 4654 1000 7455 0.477 -2176 4419 4654 2000 7455 0.477 -2176 4419 4654 4000 -0.717 ∗∗∗ (0.088)

## 0.511 ∗∗∗

(0.107) -0.738 ∗∗∗ (0.095)

## 0.524 ∗∗∗

(0.103) -0.728 ∗∗∗ (0.092)

## 0.520 ∗∗∗

(0.099) -0.730 ∗∗∗ (0.090)

## 0.523 ∗∗∗

(0.098) -0.733 ∗∗∗ (0.090)

## 0.523 ∗∗∗

(0.101) -0.732 ∗∗∗ (0.090)

## 0.523 ∗∗∗

(0.100) 0.461 0.076 0.463 0.077 0.462 0.077 0.463 0.077 0.463 0.077 0.463 0.077

Total 0.537

Intensive 0.573

Extensive 0.922

Total 0.618 0.537 0.540 0.539 0.540 0.540 0.540 0.575 1.004 0.631 0.577 1.005 0.635 0.580 1.011 0.638 0.578 1.012 0.636 0.578 1.008 0.636 0.578 1.009 0.636

Notes: Standard errors in parentheses, ∗ p < 0.1, ∗∗ p < 0.05, ∗∗∗ p < 0.01.

C Online appendix Table 8: Marginal impact of modeling assumptions (CPS)

Fit

Utility function

Quadratic

Number of Halton draws

Hours restrictions

Part-time restrictions

Fixed costs

Observed heterogeneity in C only in L only in C and L

Unobserved heterogeneity in C only in L only in C and L in C and L (with correl.)

Wage imputation

Full sample, no correction

Full sample, 1 random draw

Non-workers, 1 random draw

Constant

Labor supply types

Observations

## R 2

10% own wage elasticities

## AIC

Ext.

Int.

Total

## 0.640 ∗∗∗

(0.062) -0.015 ∗∗∗ (0.002) 0.217 (0.183)

## 0.022 ∗∗

(0.008) 0.207 (0.185)

## 0.023 ∗∗

(0.008) 0.210 (0.185)

## 0.022 ∗∗

(0.008) -1.855 ∗∗∗ (0.089) -1.279 ∗∗∗ (0.067)

## 0.420 ∗∗

(0.188) 0.192 (0.120)

## 0.397 ∗

(0.189) 0.125 (0.104)

## 0.403 ∗

(0.190) 0.142 (0.106) -0.138 ∗∗∗ (0.015) -0.258 ∗∗∗ (0.026) -0.309 ∗∗∗ (0.027) -0.152 ∗∗∗ (0.036) -0.066 ∗ (0.036) -0.115 ∗∗ (0.040) -0.051 (0.031) -0.080 ∗ (0.044) -0.094 ∗ (0.044) -0.078 ∗∗ (0.031) -0.076 ∗ (0.042) -0.097 ∗∗ (0.043)

## 0.067 ∗∗∗

(0.013)

## 0.070 ∗∗∗

(0.007)

## 0.046 ∗∗∗

(0.009)

## 0.021 ∗∗∗

(0.007) -0.118 ∗∗∗ (0.037) -0.119 ∗∗ (0.053) -0.089 ∗∗ (0.032) -0.063 ∗∗ (0.029) -0.113 ∗∗ (0.044) -0.121 ∗∗ (0.054) -0.083 ∗∗ (0.036) -0.058 ∗∗ (0.025) -0.114 ∗∗ (0.043) -0.120 ∗∗ (0.055) -0.084 ∗∗ (0.035) -0.059 ∗∗ (0.026) -0.111 ∗ (0.057) 0.025 (0.046) 0.030 (0.053)

## 0.912 ∗∗∗

(0.284) 0.338 (0.244) -0.329 (0.362)

## 0.918 ∗∗∗

(0.300)

## 0.428 ∗

(0.229) -0.237 (0.362)

## 0.921 ∗∗∗

(0.299)

## 0.413 ∗

(0.230) -0.255 (0.363)

## 0.832 ∗∗∗

(0.098)

Yes 4305 0.820 -0.813 ∗∗∗ (0.271)

Yes 3439 0.353 -0.864 ∗∗∗ (0.270)

Yes 3439 0.340 -0.857 ∗∗∗ (0.270)

Yes 3439 0.344 Notes: Uncompensated labor supply elasticities are simulated by increasing the individual wage rates by 10 percent and aggregating individual labor supply responses. Dependent variables have been standardized, i.e., an estimate of 1.0 indicates an increase of one standard deviation in the outcome. The AIC is negatively related to the statistical fit of the model—the better the fit, the lower the AIC. Standard errors clusted by labor supply group and wage imputation procedure. ∗ p < 0.1, ∗∗ p < 0.05, ∗∗∗ p < 0.01 Table 9: Partial impact of modeling assumptions (SOEP)

Fit

Utility function

Translog

Quadratic

Box-Cox

Welfare stigma

Number of Halton draws

Hours restrictions

None

Part-time restrictions

Fixed costs

Observed heterogeneity

None in C only in L only in C and L

Unobserved heterogeneity

None in C only in L only in C and L in C and L (with correl.)

Wage imputation

Full sample imputation

Error integrated out

Full sample, no correction

Full sample, error integrated out

Full sample, 1 random draw

Non-workers, error integrated out

## N

10% own wage elasticities

## AIC

Ext.

Int.

Total -0.045 ∗ (0.024)

## 0.135 ∗∗∗

(0.013) -0.093 ∗∗∗ (0.017)

## 0.965 ∗∗∗

(0.076) -0.013 ∗∗∗ (0.003) -0.125 ∗∗∗ (0.021)

## 0.067 ∗

(0.039) 0.061 (0.049) 0.051 (0.061) 0.008 (0.007) -0.035 (0.045) -0.054 (0.053)

## 0.094 ∗∗

(0.034) 0.072 (0.047) -0.003 (0.007) -0.047 (0.040) -0.037 (0.046)

## 0.090 ∗∗

(0.034) 0.071 (0.042) -0.001 (0.007)

## 1.376 ∗∗∗

(0.075) -1.110 ∗∗∗ (0.052) -0.244 ∗∗∗ (0.034) -0.425 ∗∗∗ (0.067)

## 0.145 ∗∗∗

(0.041)

## 0.278 ∗∗∗

(0.033) -0.139 ∗∗∗ (0.038) 0.013 (0.024)

## 0.127 ∗∗∗

(0.024) -0.188 ∗∗∗ (0.039) 0.035 (0.026)

## 0.153 ∗∗∗

(0.023)

## 0.398 ∗∗∗

(0.063) -0.046 ∗∗ (0.017) -0.121 ∗∗∗ (0.020) -0.235 ∗∗∗ (0.031) -0.002 (0.038) -0.070 ∗∗∗ (0.015)

## 0.067 ∗∗∗

(0.015) 0.004 (0.022) -0.035 ∗ (0.019)

## 0.042 ∗∗∗

(0.014)

## 0.028 ∗

(0.014) -0.036 ∗∗∗ (0.010) -0.030 (0.021)

## 0.024 ∗

(0.013)

## 0.035 ∗∗

(0.014) -0.030 ∗∗∗ (0.010) 0.057 (0.040)

## 0.029 ∗

(0.015) 0.050 (0.040) -0.035 ∗∗ (0.015) -0.102 ∗∗ (0.039) 0.090 (0.110)

## 0.075 ∗∗

(0.036) -0.123 (0.110) 0.039 (0.039) -0.128 (0.102) 0.125 (0.117) 0.013 (0.038) -0.032 (0.110) 0.006 (0.038) -0.124 (0.111) 0.122 (0.117) 0.023 (0.038) -0.047 (0.111) 0.011 (0.038) -0.127 (0.110) -0.498 ∗∗∗ (0.100) -0.037 (0.125) -0.720 ∗∗∗ (0.119) -0.334 ∗∗∗ (0.081) 0.143 (0.089)

## 0.269 ∗∗∗

(0.094)

## 1.248 ∗∗∗

(0.288) 0.267 (0.351)

## 1.921 ∗∗∗

(0.145)

## 1.004 ∗∗∗

(0.239) -0.599 ∗∗ (0.237) -0.544 ∗∗ (0.227)

## 1.313 ∗∗∗

(0.294) 0.190 (0.359)

## 2.033 ∗∗∗

(0.144)

## 0.935 ∗∗∗

(0.253) -0.554 ∗∗ (0.258) -0.606 ∗∗ (0.230)

## 1.317 ∗∗∗

(0.296) 0.207 (0.362)

## 2.036 ∗∗∗

(0.142)

## 0.960 ∗∗∗

(0.254) -0.569 ∗∗ (0.257) -0.602 ∗∗ (0.231) 16,730 13,219 13,219 13,219 Notes: Uncompensated labor supply elasticities are simulated by increasing the individual wage rates by 10 percent and aggregating individual labor supply responses.

∗

Standard errors clusted by labor supply ∗∗ ∗∗∗ p < 0.1, p < 0.05, p < 0.01 Table 10: Marginal impact, aggregated 1% elasticities (SOEP)

Fit

Utility function

Quadratic

Box-Cox

Welfare stigma

Number of Halton draws

Hours restrictions

Part-time restrictions

Fixed costs

Observed heterogeneity in C only in L only in C and L

Unobserved heterogeneity in C only in L only in C and L in C and L (with correl.)

Wage imputation

Full sample, no correction

Full sample, error integrated out

Full sample, 1 random draw

Non-workers, error integrated out

Non-workers, 1 random draw

Constant

Labor supply types

Observations

## R 2

1% own wage elasticities

## AIC

Ext.

Int.

Total

## 0.119 ∗∗∗

(0.023) -0.020 (0.026)

## 0.968 ∗∗∗

(0.076) -0.010 ∗∗∗ (0.001)

## 0.132 ∗∗∗

(0.028)

## 0.133 ∗∗∗

(0.042) -0.028 (0.084)

## 0.007 ∗

(0.004) 0.030 (0.050)

## 0.087 ∗∗

(0.035) 0.084 (0.053) -0.002 (0.004) 0.043 (0.043)

## 0.094 ∗∗

(0.035) 0.071 (0.044) -0.001 (0.004) -1.647 ∗∗∗ (0.082) -1.093 ∗∗∗ (0.070)

## 0.390 ∗∗∗

(0.071)

## 0.494 ∗∗∗

(0.068)

## 0.134 ∗∗∗

(0.038)

## 0.217 ∗∗∗

(0.039)

## 0.176 ∗∗∗

(0.041)

## 0.264 ∗∗∗

(0.041) -0.335 ∗∗∗ (0.057) -0.381 ∗∗∗ (0.061) -0.475 ∗∗∗ (0.070) -0.057 (0.035) 0.032 (0.037) -0.002 (0.044)

## 0.060 ∗∗

(0.022)

## 0.041 ∗

(0.022) 0.016 (0.020)

## 0.042 ∗

(0.022)

## 0.041 ∗

(0.023) 0.013 (0.022) 0.005 (0.014) 0.005 (0.013) -0.041 ∗∗∗ (0.013) -0.119 ∗∗∗ (0.016) -0.009 (0.024) -0.085 ∗∗∗ (0.024) -0.036 (0.025) -0.087 ∗∗ (0.033) -0.054 ∗ (0.031) -0.032 (0.028) -0.068 ∗∗ (0.027) -0.092 ∗∗ (0.033) -0.048 (0.030) -0.040 (0.027) -0.064 ∗∗ (0.026) -0.093 ∗∗∗ (0.033) -0.811 ∗∗∗ (0.119) -0.530 ∗∗∗ (0.048) -0.104 ∗∗ (0.049) 0.000 (0.067) 0.070 (0.056)

## 2.089 ∗∗∗

(0.117)

## 1.427 ∗∗∗

(0.103) 0.086 (0.085) 0.054 (0.062) -0.157 ∗∗∗ (0.056)

## 2.245 ∗∗∗

(0.088)

## 1.398 ∗∗∗

(0.114) 0.102 (0.078) 0.046 (0.035) -0.220 ∗∗∗ (0.028)

## 2.248 ∗∗∗

(0.084)

## 1.425 ∗∗∗

(0.117) 0.100 (0.079) 0.048 (0.038) -0.214 ∗∗∗ (0.032)

## 1.004 ∗∗∗

(0.121)

Yes 16730 0.854 -0.930 ∗∗∗ (0.104)

Yes 13219 0.816 -0.730 ∗∗∗ (0.084)

Yes 13219 0.880 -0.770 ∗∗∗ (0.087)

Yes 13219 0.889 Notes: Uncompensated labor supply elasticities are simulated by increasing the individual wage rates by 1 percent and aggregating individual labor supply responses. Dependent variables have been standardized, i.e., an estimate of 1.0 indicates an increase of one standard deviation in the outcome. The AIC is negatively related to the statistical fit of the model—the better the fit, the lower the AIC. Standard errors clusted by labor supply group and wage imputation procedure. ∗ p < 0.1, ∗∗ p < 0.05, ∗∗∗ p < 0.01 Table 11: Marginal impact, mean 10% elasticities (SOEP)

Fit

Utility function

Quadratic

Box-Cox

Welfare stigma

Number of Halton draws

Hours restrictions

Part-time restrictions

Fixed costs

Observed heterogeneity in C only in L only in C and L

Unobserved heterogeneity in C only in L only in C and L in C and L (with correl.)

Wage imputation

Full sample, no correction

Full sample, error integrated out

Full sample, 1 random draw

Non-workers, error integrated out

Non-workers, 1 random draw

Constant

Labor supply types

Observations

## R 2

10% own wage elasticities

## AIC

Ext.

Int.

Total

## 0.119 ∗∗∗

(0.023) -0.020 (0.026)

## 0.968 ∗∗∗

(0.076) -0.010 ∗∗∗ (0.001)

## 0.100 ∗∗∗

(0.033)

## 0.101 ∗∗

(0.041) -0.026 (0.063) 0.005 (0.004) 0.022 (0.047)

## 0.097 ∗∗∗

(0.034) 0.034 (0.045) -0.003 (0.004) 0.041 (0.038)

## 0.096 ∗∗∗

(0.033) 0.026 (0.039) -0.001 (0.004) -1.647 ∗∗∗ (0.082) -1.093 ∗∗∗ (0.070)

## 0.353 ∗∗∗

(0.089)

## 0.448 ∗∗∗

(0.087)

## 0.169 ∗∗∗

(0.045)

## 0.254 ∗∗∗

(0.044)

## 0.219 ∗∗∗

(0.056)

## 0.307 ∗∗∗

(0.053) -0.335 ∗∗∗ (0.057) -0.381 ∗∗∗ (0.061) -0.475 ∗∗∗ (0.070) 0.037 (0.036)

## 0.187 ∗∗∗

(0.040)

## 0.187 ∗∗∗

(0.053)

## 0.048 ∗

(0.024)

## 0.068 ∗∗∗

(0.022) 0.036 (0.022) 0.046 (0.027)

## 0.101 ∗∗∗

(0.027)

## 0.074 ∗∗

(0.029) 0.005 (0.014) 0.005 (0.013) -0.041 ∗∗∗ (0.013) -0.119 ∗∗∗ (0.016) 0.001 (0.022) -0.075 ∗∗∗ (0.026) -0.027 (0.025) -0.083 ∗∗ (0.036) -0.046 (0.031) -0.031 (0.028) -0.059 ∗∗ (0.026) -0.097 ∗∗∗ (0.033) -0.036 (0.029) -0.041 (0.026) -0.053 ∗∗ (0.025) -0.098 ∗∗∗ (0.033) -0.811 ∗∗∗ (0.119) -0.530 ∗∗∗ (0.048) -0.104 ∗∗ (0.049) 0.000 (0.067) 0.070 (0.056)

## 2.130 ∗∗∗

(0.106)

## 1.265 ∗∗∗

(0.134) 0.058 (0.049) 0.035 (0.053) -0.164 ∗∗∗ (0.028)

## 2.264 ∗∗∗

(0.092)

## 1.365 ∗∗∗

(0.132) 0.146 (0.087) 0.062 (0.042) -0.220 ∗∗∗ (0.034)

## 2.267 ∗∗∗

(0.089)

## 1.364 ∗∗∗

(0.140) 0.122 (0.078) 0.057 (0.043) -0.210 ∗∗∗ (0.035)

## 1.004 ∗∗∗

(0.121)

Yes 16730 0.854 -0.966 ∗∗∗ (0.119)

Yes 13219 0.820 -0.749 ∗∗∗ (0.091)

Yes 13219 0.876 -0.814 ∗∗∗ (0.097)

Yes 13219 0.883 Notes: Uncompensated labor supply elasticities are simulated by increasing the individual wage rates by 10 percent and taking the mean individual labor supply response. Dependent variables have been standardized, i.e., an estimate of 1.0 indicates an increase of one standard deviation in the outcome. The AIC is negatively related to the statistical fit of the model—the better the fit, the lower the AIC. Standard errors clusted by labor supply group and wage imputation procedure. ∗ p < 0.1, ∗∗ p < 0.05, ∗∗∗ p < 0.01 Table 12: Marginal impact, median 10% elasticities (SOEP)

Fit

Utility function

Quadratic

Box-Cox

Welfare stigma

Number of Halton draws

Hours restrictions

Part-time restrictions

Fixed costs

Observed heterogeneity in C only in L only in C and L

Unobserved heterogeneity in C only in L only in C and L in C and L (with correl.)

Wage imputation

Full sample, no correction

Full sample, error integrated out

Full sample, 1 random draw

Non-workers, error integrated out

Non-workers, 1 random draw

Constant

Labor supply types

Observations

## R 2

10% own wage elasticities

## AIC

Ext.

Int.

Total

## 0.119 ∗∗∗

(0.023) -0.020 (0.026)

## 0.968 ∗∗∗

(0.076) -0.010 ∗∗∗ (0.001)

## 0.107 ∗∗∗

(0.030)

## 0.084 ∗∗

(0.036) 0.001 (0.059) 0.005 (0.005) 0.079 (0.063) 0.042 (0.044) 0.062 (0.068) -0.005 (0.005)

## 0.098 ∗

(0.048) 0.056 (0.040) 0.059 (0.062) -0.003 (0.005) -1.647 ∗∗∗ (0.082) -1.093 ∗∗∗ (0.070)

## 0.370 ∗∗∗

(0.084)

## 0.448 ∗∗∗

(0.085) 0.046 (0.069) 0.112 (0.076)

## 0.116 ∗

(0.058)

## 0.181 ∗∗∗

(0.063) -0.335 ∗∗∗ (0.057) -0.381 ∗∗∗ (0.061) -0.475 ∗∗∗ (0.070) 0.046 (0.035)

## 0.136 ∗∗∗

(0.037)

## 0.130 ∗∗∗

(0.044) 0.010 (0.023) -0.034 (0.022) -0.103 ∗∗∗ (0.025) 0.013 (0.022) -0.001 (0.023) -0.068 ∗∗∗ (0.024) 0.005 (0.014) 0.005 (0.013) -0.041 ∗∗∗ (0.013) -0.119 ∗∗∗ (0.016) -0.020 (0.027) -0.077 ∗∗∗ (0.026) -0.052 ∗∗ (0.025) -0.107 ∗∗ (0.040) -0.098 ∗∗ (0.038) -0.010 (0.038) -0.096 ∗∗∗ (0.030) -0.132 ∗∗∗ (0.036) -0.088 ∗∗ (0.036) -0.017 (0.036) -0.088 ∗∗∗ (0.029) -0.122 ∗∗∗ (0.036) -0.811 ∗∗∗ (0.119) -0.530 ∗∗∗ (0.048) -0.104 ∗∗ (0.049) 0.000 (0.067) 0.070 (0.056)

## 2.169 ∗∗∗

(0.098)

## 1.278 ∗∗∗

(0.140) 0.060 (0.053) 0.042 (0.050) -0.187 ∗∗∗ (0.033)

## 2.052 ∗∗∗

(0.123)

## 1.390 ∗∗∗

(0.106) 0.227 (0.140) 0.013 (0.035) -0.265 ∗∗∗ (0.047)

## 2.110 ∗∗∗

(0.112)

## 1.397 ∗∗∗

(0.103) 0.199 (0.127) 0.021 (0.032) -0.266 ∗∗∗ (0.042)

## 1.004 ∗∗∗

(0.121)

Yes 16730 0.854 -0.940 ∗∗∗ (0.114)

Yes 13219 0.832 -0.529 ∗∗∗ (0.104)

Yes 13219 0.769 -0.623 ∗∗∗ (0.096)

Yes 13219 0.806 Notes: Uncompensated labor supply elasticities are simulated by increasing the individual wage rates by 10 percent and taking the median individual labor supply response. Dependent variables have been standardized, i.e., an estimate of 1.0 indicates an increase of one standard deviation in the outcome. The AIC is negatively related to the statistical fit of the model—the better the fit, the lower the AIC. Standard errors clusted by labor supply group and wage imputation procedure. ∗ p < 0.1, ∗∗ p < 0.05, ∗∗∗ p < 0.01
