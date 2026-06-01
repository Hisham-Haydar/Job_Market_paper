# LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS: UNOBSERVED HETEROGENEITY AND IDENTIFICATION JOHN K. DAGSVIK a,b AND ZHIYANG JIA a * a

Research Department, Statistics Norway, Oslo, Norway

Frisch Centre for Economic Research, Oslo, Norway b

## SUMMARY

This paper discusses aspects of a modeling framework in which the notion of job choice is fundamental. In this framework, workers are assumed to have preferences over latent job opportunities belonging to worker-speciﬁc choice sets from which they choose their preferred job. The main contribution of this paper is an analysis of the identiﬁcation problem under various conditions, when conventional cross-section micro-data are applied. The modeling framework is applied to analyze labor supply behavior for married/cohabiting couples using Norwegian micro data. Based on the empirical model, we discuss further qualitative properties of the model and simulation of counterfactual policy reforms. Copyright © 2015 John Wiley & Sons, Ltd. Received 1 October 2012; Revised 23 September 2014 Supporting information may be found in the online version of this article

## 1. INTRODUCTION

In the traditional approach to labor supply modelling, individual behavior is viewed as a choice among feasible leisure and disposable income combinations. This approach has been criticized for ignoring important behavioral aspects, namely that individuals in the labor market typically have preferences over job types and may face restrictions on their choices regarding job opportunities and hours of work. Recently, the discrete-choice approach to labor supply modeling has gained widespread popularity, mainly because it is much more practical than the traditional continuous approach based on marginal calculus (See Bloemen and Kapteyn, 2008). However, from a theoretical perspective, the conventional discrete-choice approach represents no essential departure from the traditional approach. This is because the only new assumptions made are that the set of feasible hours of work is ﬁnite and the random components of the utility function have particular distributional properties. 1 The purpose of this paper is to discuss identiﬁcation and other aspects of an extended version of the conventional discrete-choice model (latent job choice model) that allow for agents’ preferences being dependent on non-pecuniary job attributes, as well as allowing for possible restrictions on hours of work opportunities. In the latent job choice model, originally proposed by Dagsvik (1994), the starting point is the assumption that a worker’s labor supply follows from his or her job choice. More precisely, labor supply is viewed as resulting from a choice among latent job ’packages’, each of which is characterized by an offered wage rate, offered hours of work and * Correspondence to: Zhiyang Jia, Research Department, Statistics Norway, Oslo, Norway. E-mail: zhiyang.jia@ssb.no 1 Van Soest (1995) and others have proposed to introduce suitable dummies in the discrete labor supply model speciﬁcation to improve the ﬁt. However, this practice implies a non-structural model unless one interprets these dummies as part of the preference representation. In this case it means that the agent has stronger preferences for working particular hours (such as part-time and full-time hours) relative to other hours. Copyright © 2015 John Wiley & Sons, Ltd.

## J. K. DAGSVIK AND Z. JIA

non-pecuniary (qualitative) attributes describing the nature of the job-speciﬁc tasks to be performed. This setup can be viewed as a version of Lancaster’s characteristic approach—see Lancaster (1966, 1971)—where agents have preferences regarding not only consumption and leisure but also job attributes. The characteristic approach is intuitively appealing because it shifts the focus to qualitative aspects of the labor market that everyday life experiences tell us are important. Examples of such latent job attributes of major importance are job-speciﬁc tasks to be performed, location and quality of the social and physical environment. More recently, Farzin (2009) has discussed the effects of including non-pecuniary variables explicitly in the traditional labor supply model. He argues that ignoring such aspects of the jobs can result in biased estimates and thus lead to misleading policy proposals. Further related approaches are put forward by Sattinger (1993, 1995) and van Ophem et al. (1993). The latent job choice model allows us to address neglected aspects in traditional labor supply analysis: namely that workers face important restrictions on their job choice in the labor market (Dagsvik et al., 2014). Versions of the job choice model have been introduced and applied before: see Aaberge et al. (1995, 1999), Dagsvik and Strøm (2004, 2006), Dagsvik and Jia (2006), Kornstad and Thoresen (2007), Di Tommaso et al. (2009), Dagsvik et al. (2011, 2014). This paper contains a number of new contributions. First, we analyze the identiﬁcation problem in depth. The identiﬁcation problem in this type of model differs from standard identiﬁcation results of discrete-choice models because the present model contains representations of both preferences and choice constraints. We also extend the identiﬁcation analysis to the case where the distribution of offered wage rates depends on unobserved individual characteristics. The empirical literature on job choice models cited above differs greatly in this respect. Aaberge et al. (1995, 1999) assume that there is no unobserved variation in wages across workers, so that any unobserved heterogeneity in wages is due to ﬁrm characteristics. In contrast, Dagsvik and Strøm (2006), Dagsvik and Jia (2006) and Dagsvik et al. (2011) assume that wage variation is due solely to person-speciﬁc characteristics. In this paper, we clarify the differences between these two approaches and compare their empirical performances using a sample of Norwegian married/cohabiting couples. Finally, based on the model estimates, we discuss properties of the respective models and the issue of policy simulations. In particular, we show how one can simulate the effect of changes in restrictions on labor supply. The paper is organized as follows. In Section 2 we discuss the basic structure of the modeling framework. In Section 3 we consider identiﬁcation issues. In Section 4 we ﬁrst report results from an empirical application. Finally, we discuss how to simulate the effect of a particular reform in the restriction on working hours.

## 2. THE MODELING FRAMEWORK

Let U(C, h, z) be the (ordinal) utility function of the household, where C denotes household consumption (disposable income), h is hours of work, z = 1, 2, …, indexes market opportunities (jobs) and z = 1, 2, …, indexes non-market opportunities. For a market opportunity z, associated hours of work and wage rate are assumed ﬁxed and equal to (H(z), W(z)), where H(z), z = 1, 2, …, takes the value on a set D and W(z) is positive. When z is negative H(z) = 0. In addition to the economic budget constraint, there are restrictions on the set of available market opportunities faced by a speciﬁc worker. This is because there are job types for which the worker is not qualiﬁed and there may be variations in the set of job opportunities for which he or she is qualiﬁed. In addition, due to competition in the labor market, jobs for which a worker is qualiﬁed may not necessarily be available to him or her. However, the choice sets of market and non-market opportunities are unobserved by the researcher. Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

Assumption 1. The utility function has the structure U ð C; h; z Þ ¼ v ð C; h Þε ð z Þ (1) for z = …, 2, 1, 1, 2, …, where v(∙) is a positive deterministic function deﬁned on [C 0, 1) × [0, M], ε(z) is a positive random taste shifter, C 0 > = 0 is a known constant that represents subsistence consumption and M is the maximum hours of work. The random taste shifters are supposed to capture the effect of unobserved heterogeneity in preferences over non-pecuniary attributes that affect preferences across agent and across alternatives. Whereas the functional form of the deterministic part of the utility, v(C, h), can be very general, the separability condition in Assumption 1 is crucial. It may not hold in general because the error terms may depend systematically on disposable income and hours of work. For given hours and wage rate, h and w, the economic budget constraint is represented by C = f(hw, I), where I is non-labor income and f(∙) is the net of tax function that transforms gross household income into after-tax household income. The function f(∙) can in principle capture all details of the tax and beneﬁt system. The next assumption concerns the representation of choice sets. Here, choice sets are allowed to be random in order to accommodate that they may vary across observable identical agents due to unobserved heterogeneity in opportunities. For technical convenience, we assume at the outset that the choice sets may contain an inﬁnite number of job and non-market opportunities.

Assumption 2. The taste shifters {ε(z), z = …, 2, 1} associated with the available non-market opportunities and {ε(z), z = 1, 2, …} associated with the available jobs are realizations of two independent Poisson processes on (0, 1). The intensity of the non-market process is equal to ε 2 and the intensity of the market process is equal to θε 2, where θ is a positive constant. The available (offered) combinations of job-speciﬁc hours of work and wage rates {(H(z), W(z)), z = 1, 2, …} are independent of the corresponding taste shifters and are distributed on D × (0, 1), where D is ﬁnite and contains at least three points, according to a joint probability density function (p.d.f.) g 1 (h)g 2 (w j h). Assumption 2 asserts that the taste shifters associated with the set of available opportunities are independently scattered on the positive part of the real line but in a non-homogeneous way. The probability that there is a job z in the choice set with taste shifter ε(z) 2 (ε, ε + Δε) for some given positive ε is (approximately) equal to θε 2 Δε. Since θε 2 is decreasing in ε, it means that the intensity is large for ε close to zero. In other words, while many available jobs are unattractive, there are relatively few attractive jobs available. For example, jobs and non-market opportunities may be located in another region or country. The parameter θ is clearly a measure of job availability since a high value of θ means that there is a high probability that a job with a given level of ε(z) is available. Dagsvik (1994) has demonstrated that θ can be interpreted as the ratio of the number of available market opportunities of interest (to the agent) to the number of non-market opportunities of interest. Note also that whereas in Assumption 1 preferences of hours are deﬁned on the continuous set [0, M], the set of feasible hours of work, D, is a discrete subset of (0, M). The interpretation of g 1 (h) is as the probability that a job z with H(z) = h is available to the agent. The interpretation of g 2 (w jh)Δw is as the probability (when Δw is small) that a job z with W(z) 2 (w, w + Δw) is available to the agent, given that H(z) = h. In the following we shall sometimes call θg 1 (h)g 2 (w j h) the opportunity measure and g 1 (h)g 2 (w jh) the opportunity density. A motivation for this particular type of representation of the set of available opportunities is given by Dagsvik (1994). He demonstrates that the intensities of the Poisson processes must have the form given in Assumption 2 in order for the choice of job to satisfy the independence from irrelevant alternatives Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

(IIA) property. 2 In general, the offered distribution of wage rates may depend on hours of work, similarly to Mofﬁtt (1984). Aaronson and French (2009) have given a theoretical argument that supports this possibility. Let φ(h, w jI) denote the joint density of hours of work and wage rate of the chosen job, given nonlabor income I, and similarly let φ(0, 0 jI) be the probability of not working. 3 Theorem 1. If Assumptions 1 and 2 hold, then the joint p.d.f. of observing hours and wage rate combination (h, w) is given by φ h; wjI ¼ v ð f ð hw; I Þ; h Þθg 1 ð h Þg 2 ð wjh Þ

## X 1

v ð f ð 0; I Þ; 0 Þ þ θ v ð f ð ry; I Þ; r Þg 1 ð r Þg 2 ð y j rÞdy (2a) ∫ r2D 0 for h > 0, and the probability of not working is given by φ 0; 0jI ¼ v ð f ð 0; I Þ; 0 Þ

## X 1

v ð f ð 0; I Þ; 0 Þ þ θ v ð f ð ry; I Þ; r Þg 1 ð r Þg 2 ð y j rÞdy (2b) ∫ r2D 0 In the case with discrete conditional distribution of offered wage rates (or continuous distribution of offered hours of work) similar expressions as in equation (2a, b) follow. The only difference is that the integration is replaced by summation (or summation is replaced by integration). The proof of Theorem 1 follows from Dagsvik (1994) but for the reader’s convenience a simpliﬁed version is given in the supplementary Appendix (supporting information). This proof also covers the special case with degenerate distribution of offered wage rates. It may be the case that many people view the number of available market opportunities of interest to be less than the number of nonmarket opportunities of interest. In addition, since θ enters the model as a factor multiplied by v(C, h) it means that θ also can capture psychological ‘costs’ of working. For these reasons one might expect that in empirical applications θ will be less than one. We noted above that the model in Theorem 1 is consistent with an interpretation with stochastic sets of available job opportunities. There may, however, be additional unobserved heterogeneity that could enter the opportunity measure in other ways. Note that g 2 (wjh) may be interpreted as the conditional distribution of offered wages given offered hours of work equal to h. The model (2a, b) above assumes that g 2 (w j h) is the same for observable identical individuals (Assumption 2). This may be rather restrictive. Studies on wage formations and wage dispersion have stressed the importance of unobserved individual heterogeneity; see, for example, Abowd et al. (1999) and Mortensen (2003). We will next consider a typical approach: namely that the distribution of offered wage rates for an individual depends both on observed covariates and on unobserved variables summarized in a random-effect component η, which is assumed to be independent of the taste shifters {ε(z)}. It is also possible to allow θ to depend on η, i.e. θ = θ(η). We shall only consider the special case where g 2 (wjh; η) depends on η whereas g 1 (h) is independent of η. The motivation for this is that we believe that hours restrictions are 2 Dagsvik (1994) uses an equivalent additive utility speciﬁcation, in which case the intensity that corresponds to θε is equal to ε θe. 3 For simplicity we apply the terminology of joint density function, although the marginal distribution of realized hours of work is discrete. 2 Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

determined to a large extent by institutional regulations determined by negotiation between the unions of employers and workers and therefore not dependent on individual characteristics. The extended choice model is given as 0 1

## B

## C

## B

## C

v ð f ð hw; I Þ; h Þθ ð η Þg 1 ð h Þg 2 ð wjh; η Þ

## C

φ h; wjI ¼ E η B 1

## B

## C

## X

@

## A

v ð f ð 0; I Þ; 0 Þ þ v ð f ð ry; I Þ; r Þθ ð η Þg 1 ð r Þg 2 ð yjr; η Þdy (3a) ∫ r2D 0 for h > 0, and 0

## B

## B

φð0; 0jIÞ ¼ E η B

## B

@ 1 v ð f ð 0; I Þ; 0 Þ þ

## X 1

v ð f ð 0; I Þ; 0 Þ ∫ v ð f ð ry; I Þ; r Þθ ð η Þg 1 ð r Þg 2 ð yjr; η Þdy

## C

## C

## C

## C

## A

(3b) r2D 0 for h = 0. Whereas model (2a, b) implies that the choice probabilities satisfy the IIA property, this is not the case with the model in equation (3a, b) owing to the random effect η. In the speciﬁcation of the model in equation (3a, b), the conditional distribution of offered wage rates g 2 (wjh; η) can be represented by an offered wage rate equation which depends on (H(z), ξ(z), η), where the latent variable ξ(z) represents jobspeciﬁc unobserved variation in offered wage rates across jobs given offered hours of work. A special version of the offered wage rate equation above have an additive separable form such as logW ð z Þ ¼ α þ ψ ð H ð z Þ Þ þ η þ ξ ð z Þ (4) where α is a function of individual characteristics, η, ξ(z) and H(z) are assumed to be mutually independent and ψ(H(z)) represents the inﬂuence of the job-speciﬁc offered hours. The case where equation (4) holds and ξ(z) = 0 needs further discussion. This corresponds to a model with degenerate distribution of offered wage rates, where the offered wage rates for a given individual vary only with respect to offered hours of work. Examples of studies within the conventional framework of this type include Mofﬁtt (1984), Lundberg (1985), Biddle and Zarkin (1989), Wolf (2002) and Aaronson and French (2004). These authors typically ﬁnd a positive or inverse U shape relationship between the wage rates and hours worked. This feature is consistent with ﬁndings in the literature where part-time workers have been found to earn less than full-time workers. However, the gap seems to be very small, once important job characteristics such as occupations are considered (Manning and Petrongolo, 2008). Within our framework, when ξ(z) = 0 it follows from equation (4) that for any job z we have η = log W(z) ψ(H(z)) α. Thus, given that the chosen hours of work and wage rate combination equals (h,w), it follows that any job z (say) with hours of work H(z) has wage rate given by W(z) = w exp(ψ(H(z)) ψ(h)). Consequently, in the case with ξ(z) = 0 equation (3a) reduces to φ ð h; wjI Þ ¼ v ð f ð hw; I Þ; h Þθ ð log w ψ ð h Þ α Þg 1 ð h Þg η ð log w ψ ð h Þ α Þ=w

## X

v ð f ð 0; I Þ; 0 Þ þ θ ð log w ψ ð h Þ α Þ v ð f ð rw exp ð ψ ð r Þ ψ ð h Þ α; I Þ; r Þg 1 ð r Þ (5) r2D where g η () is the p.d.f. of η. If in addition, we assume that ψ() = 0, i.e. the offered wage rate does not depend on offered hours of work, and that θ(η) = θ, equation (5) reduces to Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

φ ð h; wjI Þ ¼ g η ð log w α Þ v ð f ð hw; I Þ; h Þθg 1 ð h Þ

## X

w v ð f ð 0; I Þ; 0 Þ þ θ v ð f ð rw; I Þ; r Þg 1 ð r Þ (6) r2D whereas in the analogous expression for the probability of not working the random effect must be integrated out. A two-sector model similar to the model given by equation (6) has been applied by Dagsvik and Strøm (2006) to analyze labor supply and sectoral choice. When η = ψ(h) = 0 we get a model where offered wage rates vary across different job offers (to a given agent). This model version was applied by Aaberge et al. (1995, 1999).

## 3. IDENTIFICATION

We now turn to a discussion on identiﬁcation of the model. We start with the simpler case where the random effect in the wage rate equation is ruled out, i.e. the model is as presented in Theorem 1. From Theorem 1 it follows that for positive h φ ð h; w j IÞ=φ ð 0; 0 j IÞ ¼ v ð f ð hw; I Þ; h Þθg 1 ð h Þg 2 ð w j hÞ=v ð f ð 0; I Þ; 0 Þ (7) Since both φ(h, w|I) and φ(0, 0|I) are observable, the right-hand side of equation (7) can be identiﬁed non-parametrically. However, it remains unclear if one can separately identify v(C, h) and θg 1 (h)g 2 (w|h). Essentially, the identiﬁcation problem arises from the fact that observed labor supply behavior is a result of both preferences (utility function) and latent job choice constraints (opportunity measure) in our model. If available, information on desired hours of work could be used to identify preferences, since job choice constraints are irrelevant in this case. 4 Subsequently, based on the estimated preferences, one could, with this information, estimate the opportunity measure using data on actual observed behavior. In this way, both the utility function and the opportunity measure can be identiﬁed. This approach is. however. not straightforward because the representation of job types in stated preference surveys may not fully correspond to the variety of job offers agents face in real labor markets. Note that, even if panel data or independent cross-section data are available, it is hard to see how this would help to solve the identiﬁcation problem in general. If, for example, preference parameters were assumed to be ﬁxed over time, this would enable us to identify changes in the opportunity measure non-parametrically, but not the level. In what follows we limit our discussion to the situation where only cross-section data are available. That is, we have observations on hours of work, wage, non-labor income and individual characteristics. Assumption 3 summarizes some useful regularity conditions for the deterministic part of the utility function v(C, h) and the net of tax function. Assumption 3. The deterministic part of the utility function v(C, h) is continuously differentiable in C and the net of tax function f(u, I) is continuous, piecewise differentiable and strictly increasing in u and I. One important property of our setup is that non-labor income enters the utility speciﬁcation in a particular manner, namely such that it can generate variation in consumption while keeping hours of work and the wage rate constant, and it enters the model only through consumption, not affecting the

4 See for example, Bloemen (2008) and references therein for some recent studies using desired hours of work to identify preferences. Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

opportunity measure. The next theorem shows to what extent the model can be non-parametrically identiﬁed in this case. Theorem 2. Assume that Assumptions 1–3 hold. Then, v(C, h) can be expressed as v(C, h) = ζ (C) r λ * (C, h)δ(h) for h > 0, where ζ (C) and λ * (C, h) are identiﬁed but r is an unknown constant and δ(h) an unknown function of h. The proof of Theorem 2 is given in APPENDIX A. Theorem 2 shows that, even under the exclusion restriction that non-labor income does not affect the opportunity measure, the model is nonparametrically unidentiﬁed. Dagsvik and Strøm (1997) show identiﬁcation in an analogous model by assuming that preferences are separable in consumption and hours of work and, more importantly, that ﬁxed cost of working is observed. However, such information is rarely available. Assumption 4.

The offered wage rates and the offered hours of work are independently distributed.

Theorem 3. Assume that Assumptions 1–4 hold. Then the distribution of offered hours is identiﬁed and v(C, h) = λ(C, h)δ(h), where λ(C, h) is identiﬁed but δ(h) is not identiﬁed. The proof is given in APPENDIX A. When offered wage rates and hours of work are correlated, additional restrictions are needed to achieve identiﬁcation. Note that, for the purpose of simulating solely the effect of counterfactual changes in taxes and wage rates, it is not necessary to identify δ(h) and g 1 (h) separately as long as g 1 (h) is kept ﬁxed. The reason is that the effect of changes in taxed and wages only enters the model through C and the opportunity density of offered wage rates. One way to obtain full identiﬁcation is to make parametric functional form assumptions about both v(C, h) and θg 1 (h)g 2 (w|h). Below, we consider one particular parametric utility speciﬁcation, namely the generalized Box–Cox function, given by log v ð C; h Þ ¼ γ 1 ð C α 1 Þ=α þ γ 2 ð 1 h=M Þ β 1 =β þ γ 3 ð C α 1 Þ ð 1 h=M Þ β 1 =αβ (8) See Dagsvik and Strøm (2006) and Dagsvik and Røine Hoff (2011) for a theoretical justiﬁcation based on invariance principles. 5 Assumption 5. There exists an interval (u, u +) such that when u 2 (u, u + ), the marginal net of tax rate w.r.t. non-labor income ∂f(u, I)/∂I does not vary with u. Assumption 5 is not particularly restrictive. In fact, most tax systems satisfy this condition. Assumption 6. The function log v(C, h) is a generalized Box–Cox function as given in equation (8). Furthermore, there exist two points h 1 ≠ h 2 2 D such that g 1 (h 1) = g 1 (h 2 ). The following theorem summarizes the key identiﬁcation results when additional functional form assumptions are made for v(C, h) and g 1 (h)g 2 (w|h). Theorem 4. Assume that Assumptions 1–3, 5 and 6 hold. Then the model given by equation (2a, b) is identiﬁed. The proof of Theorem 4 is given in the supplementary Appendix. Theorem 4 gives sufﬁcient conditions for the model in equation (2a, b) to be fully identiﬁed. Assumption 5 may not be necessary but is made here for convenience.

5

See also the errata in Dagsvik (2013).

Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

We shall next consider the more general setting where we allow for unobserved heterogeneity in the offered wage rate, i.e. the model given by equation (3a, b). To achieve identiﬁcation, it is necessary to introduce an exogenous variable X which inﬂuences only the opportunity density.

Assumption 7.

The offered wage rates are generated by log W ð z Þ ¼ Xb þ a þ η þ ξ ð z Þ (9) where X is a continuous covariate that does not affect preferences and can take any real value, ξ(z) and η are zero mean random variables which are independent of each other and independent of the taste shifters, and a and b are unknown parameters. Furthermore, θ is either a constant or has the structure θ ¼ θ ð a þ Xb þ η Þ (10) Assumption 7 asserts that the offered wage rate equation is additively separable in a + Xb, η and ξ(z). The formulation in equation (9) is a special case of equation (4) with ψ() = 0, α = a + Xb. The parameter a may depend on individual characteristics other than X. The motivation for the particular formulation of θ() in Assumption 7 is that a + Xb + η is supposed to represent the effect of observed and unobserved individual ability which may affect the opportunity measure. Here, ξ(z) and η may be discrete or continuous random variables and ξ(z) may also be degenerate. In the following we need to extend our notation of φ(h, w|I) to φ(h, w|I, X) to indicate that the latter p.d.f. is conditional on X. Assumption 8.

The function φ(h, w|I, X)/v(f(hw, I), h)) satisﬁes 1 1 ∫ 1 ∫ 0 ð j X j m jlog wj n φ ð h; w j I; XÞ=v ð f ð hw; I Þ; h ÞÞdw dX < 1 for m, n = 0, 1, 2, h 2 D and I > 0. 6 Theorem 5. i. If Assumptions 1–4, 7 and 8 hold, then v(C, h) is identiﬁed apart from a multiplicative term that may depend on h, θ() is identiﬁed up to a constant and the distribution of offered wage rates conditional on the random effect is identiﬁed. ii. If Assumptions 1–4, and 6 to 8 hold then the model in equation (3a, b) is identiﬁed. The proof of Theorem 5 is given in the supplementary Appendix. Theorem 5 extends the identiﬁcation results of Theorems 3 and 4 to the case with a random effect in the offered wage rate distribution. It is worth noting that the independence condition (Assumption 4) is still maintained in Theorem 5 in contrast to Theorem 4, where offered wage rate and hours of work are allowed to be correlated. Theorems 2–5 hold also in the case where the distribution of offered wage rates is discrete or the distribution of offered hours of work is continuous. Furthermore, Theorem 5 holds when X is a discrete variable or when the distribution of offered wage rates across jobs is degenerate, that is, where each agent only faces one individual speciﬁc wage rate.

6 The assumption is analogous in the case where X is discrete, in which case the integral with respect to X is replaced by a sum. Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

4.1. Model Speciﬁcation and Estimation Results In this section we report results from an empirical application based on micro data from the Norwegian Labor Survey 1997. Table I summarizes the data for our empirical analysis. Details about variable deﬁnitions and the data, and the speciﬁcation of a joint labor supply model for married couples, can be found in the supplementary Appendix. The systematic part of the utility function is assumed to be a generalized Box–Cox functional form, similarly to equation (8). Alternatively, we could have used a ﬂexible polynomial speciﬁcation similarly to van Soest et al. (2002). Dagsvik and Strøm (2004, 2006) found that the Box–Cox functional form is more or less as ﬂexible as the polynomial speciﬁcations, and in contrast to the latter ones it is globally concave. For each spouse, we specify eight feasible annual hours of work alternatives, namely 0, 208, 624, 1040, 1456, 1950, 2340 and 2600. The logarithm of the job availability measures θ F and θ M are speciﬁed as linear functions of length of schooling. The opportunity probability mass functions of offered hours, g 1k (h), k = F, M, are uniform except for peaks at full-time and part-time hours. The full-time peak corresponds to 1950 hours annually (37.5 hours a week), while the part-time peak corresponds to 1040 hours annually (20 hours a week). The part-time and full-time peaks in the hours distribution are supposed to capture the effect of institutional regulations on hours of work. Recall that this speciﬁcation of the opportunity distribution is formally equivalent to introducing suitable dummy variables at full-time and part-time hours of work in the utility speciﬁcation of the conventional discrete-choice speciﬁcation; see, for example, van Soest (1995). An advantage with our framework is that it provides a theoretical rationale for introducing such dummies, in contrast to the conventional discrete-choice labor supply model. A central issue in our empirical illustration is how to specify the opportunity density of offered wage rates. A fairly general class of speciﬁcations accounting for unobserved heterogeneity across both jobs and agents, as well as allowing for correlation between offered hours of work and offered wage rates, is given in equation (4). It remains, however, to prove that the model is identiﬁed in this case. Even in the case where offered hours and wage rates are independent, it is a demanding task to obtain structural

Table I. Summary statistics

Both working

Only husband working

Only wife working

Mean

## SD

Mean

## SD

Mean

## SD

Men

Age

Education

Experience non-labor income wage rate weekly hours of work 45.06 12.58 25.48 6320 153.82 38.43 8.44 2.89 9.14 12032 52.98 5.38 44.06 12.26 24.80 10796 169.11 39.16 9.41 2.71 9.99 15543 65.47 5.91 50.40 11.80 31.60 30604 9.91 3.03 11.08 30395

Women

Age

Education

Experience

Non-labor income

Wage rate

Weekly hours of work

No. of children 0–6

No. of children 7–18

No. of households 42.75 12.10 23.65 17655 120.12 30.45 0.37 0.85 2254 8.39 2.72 9.33 16558 37.79 8.93 0.68 0.97 41.68 10.87 23.81 27689 9.70 2.26 10.71 21701 0.70 0.94 256 0.89 0.97 47.40 11.80 28.60 13848 22.82 29.78 0.20 1.00 5 7.86 2.86 10.01 14219 17.98 12.06 0.45 0.71 Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

estimates due to measurement error in reported hours worked. In our dataset, only weekly hours of work are reported but not the usual number of weeks worked during a year. Furthermore, overtime is not reported. This type of measurement error is common in datasets used for labor supply analysis.

See, for example, Borjas (1980) and Blundell et al. (2007) for extensive discussions on how to deal with this problem in conventional labor supply models. This measurement error creates a spurious negative correlation between the observed wage rate and hours in our data (0.22 for married women,

## 0.17 for married men). 7 This so-called ‘division bias’ problem poses considerable challenges for em-

pirical analyses based on this type of data.

When offered wage rates and offered hours of work are independent, the division bias problem can be reduced by adopting the three-stage estimation procedure proposed by Dagsvik and Strøm (2004, 2006). This amounts to estimating a reduced-form participation probability in the ﬁrst stage, and subsequently estimating wage rate equations using the results from the ﬁrst stage to control for selectivity bias. In the third stage the labor supply model is estimated by the maximum likelihood method after inserting the wage rates predicted by the estimated wage equations into the model and integrating out the respective error terms. Under standard assumptions about the measurement error this leads to unbiased wage rate equations in the second stage apart from the estimate of the variance of the error terms which may be upward biased. This procedure does not, of course, eliminate the measurement error in hours of work but it removes the spurious negative correlation between observed hours and wage rates. Measurement error may still be a problem in the last-stage maximum likelihood estimation, since it may cause misclassiﬁcation of the dependent variable (individual’s working hours). Hausman et al.

(1998) suggest a method to control for the misspeciﬁcation problem in a binary-choice model.

However, their method is not readily applicable in our analysis.

Given Assumption 4, we have estimated two special cases of the model in equation (3a, b): Model 1 and Model 2. Using the notation of equation (4), Model 1 is based on the assumption that all observable identical individuals are assumed to face the same offered wage rate distribution across jobs (η = ψ() = 0), whereas in Model 2 each individual faces only one offered wage, though this wage may be different for observationally identical individuals (ξ(z) = ψ() = 0). Thus the interpretation of the ﬁrst stage wage rate equations is rather different in the two model versions, although the estimated wage equations have the same structure. In Model 1, the error terms in the wage rate equations measure the variation of wage rate offers across different jobs. In contrast, in Model 2, the error terms represent unobserved individual heterogeneity. 8 The speciﬁcation of the wage rate equations is conventional. In Model 1 ξ(z) is assumed to be normally distributed with zero mean and in Model 2 η is assumed to be normally distributed with zero mean. Thus the estimated residual variances in the wage rate equations are interpreted as the variance of ξ(z) and η in Models 1 and 2, respectively. The term α is speciﬁed as a linear function of length of schooling, potential experience, potential experience squared and a dummy variable for marriage status. Potential experience is deﬁned as age minus years of schooling minus 7. The estimates of the wage rate equations are presented in Table S1 in the supplementary Appendix. As shown in Table S1, the selection bias in the wage rate equations is negligible.

The estimates of the two models are reported in Table S2 in the supplementary Appendix. In both models the results imply that log v(C, h) is strictly increasing and concave in consumption and leisure.

The marginal utility of leisure of married women is decreasing until about the age of 35 and thereafter

7 This error is sometimes called’division bias’ and is a rather common problem in many typically available datasets; see, for example, the discussion in Borjas (1980). 8 One should, in principle, interpret the estimated error terms in the Mincer type wage equations as the sum of inter-and intraindividual effects, ξ(z) + η. Although it seems technically possible to separate the contribution of these two terms, we believe that this identiﬁcation hinges too much on the mathematical structure of the model and is therefore not theoretically sound, given the available information. Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

increasing. The similar pattern holds for the married men, only with the minimum value obtained around the age of 37. The number of children has a signiﬁcant effect on the marginal utility of leisure for married women. In contrast, the marginal utility of leisure for married men does not depend significantly on the number of children. This indicates that the female takes more responsibility for children within the family than the male, which is not a surprising result. The measure of the job availability for the married women, θ F, depends positively on the length of schooling (S). Higher educational level increases the job opportunities for married women. The corresponding estimate for married men turns out not to be signiﬁcant. This may be due to the fact that in our dataset there are only very few married men who are out of the labor force. For both genders, the value of θ is estimated to be less than 1. Similar results are reported by Dagsvik and Strøm (2006), Di Tommaso et al. (2009) and Dagsvik et al.

(2011). As discussed earlier, this can be interpreted as indicating that the number of interesting and available jobs is smaller than the number of interesting non-market opportunities. Note also that the full-time peak in the opportunity probability mass function of hours for married men is substantially higher than the corresponding peak for married women whereas the opposite is true for the part-time peaks. The reason for this is that women seem to have stronger preferences than men for working in particular labor market sectors (such as health care and teaching) and therefore may face different choice restrictions. This could partly be due to differences in gender-speciﬁc human capital investments, which are important in shaping the job choice constraints. 9 Both Model 1 and Model 2 ﬁt the data quite well. Figures S1 and S2 in the supplementary Appendix display the observed and (aggregate) predicted values of participation and hours of work for each spouse based on our model. Model 2 seems to perform slightly better than Model 1. Since our model represents the behavior of couples, it seems more interesting to consider the joint distribution of hours of work rather than just the marginals. Owing to the problem of thin cells, we are forced to consider joint distributions with highly aggregate hours of work intervals and combine selected hours of work intervals taking into account the fact that some hours of work alternatives are chosen by only a few households in our sample. For men, we distinguish only between the cases where they work less than full time (0–1456 hours a year) or work full time and more (<= 1950 hours a year). For women, we distinguish between three options (not working, working less than full time and working full time and more). Altogether, our selected aggregation procedure implies just six cells. Figure 1 shows the predicted and observed distributions of hours of work on these six cells. The ﬁt of both models is quite good, with Model 2 performing slightly better than Model 1.

These visual inspections of the marginal and joint distributions of hours of work can be seen as an informal and crude way to check goodness of ﬁt of the models. Several alternative model evaluation methods are used for discrete-choice models in the literature; see, for example, Train (2009). One popular summary measure analogous to the R 2 measure applied in regression analysis is McFadden’s ρ 2 measure (pseudo R 2 ); see McFadden (1973). The respective values of the log-likelihood functions are approximately equal to 5309 and 5243. The corresponding ρ 2 values for the two models are

## 0.49 and 0.50 respectively. These results seem to be consistent with the informal check based on

Figure 1, and Figures S1 and S2 in the supplementary Appendix.

Another way of measuring goodness of ﬁt uses tests based on comparing predicted probabilities with corresponding observed frequencies on some partitions of the outcome and exogenous variables in the tradition of the Pearson chi-square statistics. We have applied the chi-square test statistics of Andrews (1988a,b). To partition of cells as above (six cells). The test statistic is given ⌢ this end we ⌢ used the same ⌢ 1 as F ¼ Nv N β ′ V ^ v N β, where v N β is the vector of differences between the predicted and ob⌢ p ﬃﬃﬃﬃ served frequencies on the chosen cells, and V ^ is the estimated covariance matrix of v N β

N. In our

9 In a sector-speciﬁc model, as in Dagsvik and Strøm (2006), one could obtain explicit sector-speciﬁc opportunity measures. Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

Figure 1. Predicted and observed joint hours of work distributions for couples, 1997 case, the test statistic F is asymptotically chi-square distributed with 5 degrees of freedom. The test statistic for Model 1 is equal to 57.6 and for Model 2 it is equal to 10.4. The 5% signiﬁcance level for the chi-square distribution with 5 degrees of freedom is 11.07. Thus Model 2 passes Andrew’s test at 5% signiﬁcance level, while Model 1 is far from passing the test. Thus Model 2 ﬁts the data better than Model 1 and we therefore select Model 2 as our maintained model.

4.2. Aggregate Wage Elasticities and’Labor Supply Curves’ In this section, we present selected gross wage elasticities and ﬁgures for what we call labor supply curves. We have calculated elasticities that take into account both the systematic terms and the unobservables in the model. This means that we account for how the mean of the distribution of labor supply is affected by changes in (say) gross wage levels. There are two types of elasticities reported in the literature; see, for example, Dagsvik and Strøm (2006) and van Soest and Das (2001). One type is the so-called average elasticity, which is simply the average of the individual elasticities calculated from the formulas for expected hours of work or probability of working given the individual observed characteristics. The second is called aggregated elasticity, which is the elasticity of the aggregate (or average) response (e.g. the elasticity of the population mean hours of work). Table II displays aggregated gross wage elasticities for both models. The standard errors are generated using bootstrap methods with 100 replications. We have also computed the average elasticities for both models: the estimates are quite close to the aggregated elasticities reported in Table II. The unconditional wage elasticity of hours of work is deﬁned as the elasticity of expected number of hours of work with respect to wage. The corresponding elasticity of hours of work conditional on working can be found by subtracting the wage elasticity of the probability of working from the unconditional wage elasticity of hours of work. In general, both models show that the gross wage elasticities are moderate for married females and very small for married males. Model 2 seems to predict a stronger labor supply response than Model 1, Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

Table II. Aggregated gross wage elasticities

Model 1

Probability of working, men

Probability of working, women

Hours of work, men (unconditional)

Hours of work, women (unconditional)

Model 2

Women’s wage

Men’s wage

Both wages

Women’s wage

Men’s wage

Both wages 0.006 (0.003) 0.221 (0.015) 0.022 (0.004) 0.405 (0.025) 0.007 (0.003) 0.145 (0.020) 0.047 (0.007) 0.268 (0.034) 0.003 (0.001) 0.091 (0.023) 0.028 (0.008) 0.151 (0.050) 0.007 (0.003) 0.333 (0.022) 0.022 (0.005) 0.618 (0.039) 0.010 (0.004) 0.165 (0.022) 0.080 (0.009) 0.272 (0.038) 0.006 (0.003) 0.205 (0.024) 0.062 (0.009) 0.381 (0.054)

Bootstrapped standard errors in parentheses.

though the differences are not big. Using estimates from Model 2, for married females the own-wage elasticity of the probability of working is equal to 0.33, which means that if the gross wages of married females were to increase by 5% (say), then the aggregate proportion of married females working would increase by around 1.5%. The cross-wage elasticity for married women is negative and smaller in size than own wage elasticity, as found in many studies. The elasticity of the probability of working for married women with respect to both spouses’ gross wage rate is equal to 0.2. This means that the proportion of married women working would increase by 1%, if both spouses’ wage rates were increased by 5%. Since the model is highly nonlinear, the aggregate elasticities may cover substantial variation in elasticities across different wage levels and individual characteristics. Remember that when we have estimated the model we can compute wage elasticities conditional on given hypothetical wage levels, without using wage equations. To illustrate the nonlinearity in the labor supply response resulting from wage changes, we have plotted what we call expected labor supply curves. These curves show expected hours of work as a function of the wage rates, conditional on other characteristics (non-labor income, age, family size and opportunity measure). We have generated labor supply curves for married women for a typical household, which is constructed using the sample average value of household characteristics given that the household consists of a husband aged 45, a wife aged 42 and one school-age child. Both parents have 12 years of education. We look at two different scenarios: the husband’s wage is high (200 NOK (Norwegian krone) per hour) 10 or low (100 NOK per hour). Figure 2 shows how the expected annual hours of work of married women in both models vary with her expected gross wage level. Both models predict that labor supply elasticities decrease as the women’s wage increases. However, at low wage rate levels the labor supply curves are steeper for Model 2 than for Model 1, whereas the difference is small between the two models at high wage rate levels.

4.3. Simulation of Changes in the Opportunity Distribution of Offered Hours of Work Using our framework, we can also simulate the effect on labor supply from changing the opportunity distribution. Since our model is not an equilibrium one, we can only simulate pure supply effects conditional on given job availability measures, (θ F, θ M ), and the distributions of offered hours and wage rates.

10 Around $30 per hour at 1997 exchange rates.

Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

Figure 2. Married women’s expected hours of work in a typical household, by husband’s wage. The shaded area shows the 95% conﬁdence band In Norway, there is a high proportion of married women in part-time positions. In our sample, more than 35% of the married women are working between 20 and 30 hours a week, while only around 40% are working full time (37.5 hours a week). Many of those in part-time jobs are employed in the public sector, especially in health care. Whereas Norwegian working environment legislation opens for the possibility of voluntary part-time jobs, an important reason for the high concentration of part-time workers relates to particular institutional regulations in the public health sector. Part-time positions are sometimes the only positions offered by public health care organizations, especially in more rural areas. The proposed reform can be interpreted as a change in the opportunity distribution of hours for women, obtained by removing the part-time peak and increasing the full-time peak (since the part-time jobs are replaced by full-time ones) while keeping the total number of available jobs unchanged (i.e. θ F is unchanged). See APPENDIX B for details. Figure 3 displays the results from such a simulation. As we can see, there is a signiﬁcant decrease in the proportion of married women who choose to work part time, accompanied by an increase in the proportion of full-time hours of work of about a similar magnitude. In addition, we found that the corresponding labor supply of married men changes very little with the introduction of this reform. However, one needs to be careful when interpreting this result in the context of reforms speciﬁc to labor market sectors (such as the health care sector), since sector-speciﬁc preferences and restrictions are not explicitly accounted for in the model. Nevertheless, this simulation exercise clearly illustrates the advantage and potential of our modeling framework. Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

Figure 3. Hours of work for married women, before and after reform. The 95% conﬁdence intervals are represented by the error bars

## 5. CONCLUSIONS

The traditional models of labor supply, being versions of the theory of consumer demand with two goods—disposable income and leisure—simplify the choice setting in labor markets. In real labor markets, agents have preferences over pecuniary as well as non-pecuniary aspects of jobs and face limited sets of job opportunities in the labor market due to competition between workers and restrictions resulting from institutional regulations on hours of work. An essential feature of the modeling framework discussed in this paper is that it allows the researcher to accommodate restrictions on hours of work and the set of feasible jobs typically observed in many datasets. A major contribution of this paper is the analysis of identiﬁcation. The standard identiﬁcation results for multinomial and mixed logit models do not apply because our modeling framework contains a representation of both preferences and latent choice constraints (opportunity measure). Although the model is, in general, not identiﬁed we have demonstrated how it will be identiﬁed under speciﬁc conditions even in the presence of unobserved heterogeneity in the offered wage rate distribution. We have carried out an empirical application based on micro data from Norway. In contrast to Dagsvik and Strøm (2006), who estimated a similar model for married women given the husband’s labor supply, we study the joint labor supply behavior for married couples. We have, moreover, estimated two versions of the model based on two’extreme’ assumptions about wage heterogeneity. A model with solely inter-individual variation in wage rates seems to ﬁt the data better than a model that allows only for variation in wage rates across jobs. We have computed labor supply curves to illustrate the substantial nonlinearity in the labor supply responses, as a function of wage rates and to illustrate how these curves depend on the two model formulations. Subsequently, we have shown how one can use the model to simulate the effect of hypothetical changes in the opportunity measure. Changes of this sort cannot be studied using conventional discrete labor supply models. The data we have applied are not ideal owing to measurement error in the hours of work observations. We are currently working on establishing another dataset with much less measurement error in Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

hours, which hopefully will be helpful for studying the relationship between the offered wage rates and offered hours within a labor supply modeling framework.

## ACKNOWLEDGEMENTS

We thank J. Aasness, T. O. Thoresen and T. Skjerpen for helpful comments. We are particularly grateful for the extensive and constructive criticism, help and suggestions by T. Magnac and two anonymous referees.

## REFERENCES

Aaberge R, Dagsvik JK, Strøm S. 1995. Labor supply responses and welfare effects of tax reforms. Scandinavian Journal of Economics 97: 635–659. Aaberge R, Columbino U, Strøm S. 1999. Labor supply in Italy: an empirical analysis of joint household decisions with taxes and quantity constraints. Journal of Applied Econometrics 14: 403–422. Aaronson D, French E. 2004. The effect of part-time work on wages: evidence from the social security rules. Journal of Labor Economics 22: 329–352. Aaronson D, French E. 2009. The effect of progressive taxation on labor supply with hours and wages are jointly determined. Journal of Human Resources 44: 386–408. Abowd J, Kramarz F, Margolis D. 1999. High wage workers and high wage ﬁrms. Econometrica, 67: 251–334. Andrews DWK. 1988a. Chi-square diagnostic tests for econometric models: introduction and applications. Journal of Econometrics 37: 135–156. Andrews DWK. 1988b. Chi-square diagnostic tests for econometric models: theory. Econometrica 56: 1419–1453. Borjas G. 1980. The relationship between wages and weekly hours of work: the role of the division bias. Journal of Human Resources 15: 409–423. Biddle J, Zarkin G. 1989. Choice among wage–hours packages: an empirical investigation of male labor supply. Journal of Labor Economics 7: 415–437. Bloemen H. 2008. Job search, hours restrictions, and desired hours of work. Journal of Labor Economics 26: 137–179. Bloemen H, Kapteyn A. 2008. The estimation of utility consistent labor supply models by means of simulated scores. Journal of Applied Econometrics 23: 395–422. Blundell R, MaCurdy T, Meghir C. 2007. Labor supply models: unobserved heterogeneity, nonparticipation and dynamics. In Handbook of Econometrics, Vol. 6A, Heckman JJ, Leamer EE (eds). Elsevier: Amsterdam; 4667–4775. Dagsvik JK. 1994. Discrete and continuous choice, max-stable processes and independence from irrelevant attributes. Econometrica 62: 1179–1205. Dagsvik JK. 2013. Justiﬁcation of functional form assumptions in structural models: a correction. Theory and Decision 75: 79–83. Dagsvik JK, Jia Z. 2006. Labor supply as a choice among latent job opportunities: a practical empirical approach. Discussion paper 481, Research Department, Statistics Norway, Oslo. Dagsvik JK, Røine Hoff S. 2011. Justiﬁcation of functional form assumptions in structural models: applications and testing of qualitative measurement axioms. Theory and Decision 70: 215–254. Dagsvik JK, Strøm S. 1997. A framework for labor supply analysis in the presence of complicated budget restrictions and qualitative opportunity aspects. Memorandum 22, Department of Economics, University of Oslo. Dagsvik JK, Strøm S. 2004. Sectoral labor supply, choice restrictions and functional form. Discussion paper 388, Statistics Norway, Oslo. Dagsvik JK, Strøm S. 2006. Sectoral labor supply, choice restrictions and functional form. Journal of Applied Econometrics 21: 803–826. Dagsvik JK, Jia Z, Orsini K, van Camp G. 2011. Subsidies on low-skilled workers’ social security contributions: the case of Belgium. Empirical Economics 40: 779–806. Dagsvik JK, Jia Z, Kornstad T, Thoresen T. 2014. Theoretical and practical arguments for modeling labor supply as a choice among latent jobs. Journal of Economic Surveys 28: 134–151. Di Tommaso ML, Sæther EM, Strøm S. 2009. Nurses wanted. Journal of Health Economics 28: 748–757. Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

Farzin YH. 2009. The effect of non-pecuniary motivations on labor supply. Quarterly Review of Economics and

Finance 49: 1236–1259.

Hausman JA, Abrevaya J, Scott-Morton FM. 1998. Misclassiﬁcation of the dependent variable in a discreteresponse setting. Journal of Econometrics 87: 239–269.

Kornstad T, Thoresen T. 2007. A discrete choice model for labor supply and child care. Journal of Population

Economics 20: 781–803.

Lancaster K. 1966. A new approach to consumer demand. Journal of Political Economy 74: 132–157.

Lancaster K. 1971. Consumer Demand: A New Approach. Columbia University Press: New York.

Lundberg S. 1985. Tied wage–hours offers and the endogeneity of wages. Review of Economics and Statistics 83:

638–646.

Manning A, Petrongolo B. 2008. The part-time pay penalty for women in Britain. Economic Journal 118:

## F28–F51.

McFadden D. 1973. Conditional logit analysis of qualitative choice behavior. In Frontiers in Econometrics, Zarmebka P (ed.). Academic Press: New York; 105–142.

Mofﬁtt R. 1984. The estimation of a joint wage–hours labor supply model. Journal of Labor Economics 2:

550–566.

Mortensen DT. 2003. Wage Dispersion: Why are Similar Workers Paid Differently? MIT Press: Cambridge, MA.

Sattinger M. 1993. Assignment models of the distribution of earnings. Journal of Economic Literature 31:

831–880.

Sattinger M. 1995. Search and the efﬁcient assignment of workers to jobs. International Economic Review 36:

283–302.

Train K. 2009. Discrete Choice Methods with Simulation. Cambridge University Press: New York.

van Ophem H, Hartog J, Vijverberg W. 1993. Job complexities and wages. International Economic Review 34:

853–873.

van Soest A. 1995. Structural models of family labor supply: a discrete choice approach. Journal of Human

Resources 30: 63–88.

van Soest A, Das M. 2001. Family labor supply and proposed tax reforms in the Netherlands. De Economist 149:

191–218.

van Soest A, Das M, Gong X. 2002. A structural labour supply model with ﬂexible preferences. Journal of Econometrics 107: 345–375.

Wolf E. 2002. Lower wage rates for fewer hours? A simultaneous wage–hours model for Germany. Labour

Economics 9: 643–663.

## APPENDIX A

Proof of Theorem 2. Let F ′ k ð x Þ denote the partial derivative with respect to the kth component of x of a function F(x). By Assumption 3, f(u, I) is invertible in u for a given I except at a ﬁnite number of points. Thus κ(C, I) determined by C = f(κ(C, I), I) is a well-deﬁned function and equals the wage income which is needed to achieve disposable income C at given non-labor income level I. From equation (2a, b) we have that v ð f ð hw; I Þ; h Þθg ð h; w Þ φ ð h; wjI Þ ¼ v ð f ð 0; I Þ; 0 Þ φ ð 0; 0 j IÞ

## (A:1)

where φ(h, w|I) is the joint density of observed hours and wage rate. By taking the logarithm transformation of equation (A.1) and differentiating with respect to I we obtain v ′ 1 ð f ð hw; I Þ; h Þf ′ 2 ð hw; I Þ v ′ 1 ð f ð 0; I Þ; 0 Þ f ′ 2 ð 0; I Þ φ ′ 3 ð h; wjI Þ φ ′ 3 ð 0; 0jI Þ ¼ v ð f ð hw; I Þ; h Þ v ð f ð 0; I Þ; 0 Þ φ ð h; wjI Þ φ ð 0; 0 j IÞ By inserting wh = κ(C, I) into equation (A.2) and rearranging, (A.2) becomes Copyright © 2015 John Wiley & Sons, Ltd.

## (A:2)

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

v ′ 1 ð C; h Þ ∂log v ð C; h Þ r ð I Þ ¼ ¼ ′ þ Γ ð C; h; I Þ v ð C; h Þ

## ∂C

f 2 ð κ ð C; I Þ; I Þ

## (A:3)

where

Γ ð C; h; I Þ ¼ φ ′ 3 ð h; κ ð C; I Þ=hjI Þ φ ′ 3 ð 0; 0jI Þ 1 ′ φ ð h; κ ð C; I Þ=hjI Þ φ ð 0; 0jI Þ f 2 ð κ ð C; I Þ; I Þ

## (A:4)

and r ð I Þ ¼ v ′ 1 ð f ð 0; I Þ; 0 Þ f ′ 2 ð 0; I Þ=v ð f ð 0; I Þ; 0 Þ:

## (A:5)

By integrating equation (A.3) with respect to consumption we get that

## C

## C

dz þ Γ ð z; h; I Þdz ′ f ð κ ð z; I Þ; I Þ C 0

## C 0 2

log v ð C; h Þ log v ð C 0; h Þ ¼ r ð I Þ ∫ ∫

## (A:6)

Let

## C

log ζ ð C; I Þ ¼

## C

dz and log λ ð C; h; I Þ ¼ Γ ð z; h; I Þdz ′ ð κ ð z;

## I

## Þ;

## I

## Þ

f

## C 0 2

## C 0

∫ ∫ With this notation we obtain from equation (A.6) that v ð C; h Þ ¼ ζ ð C; I Þ r ð I Þ λ ð C; h; I Þv ð C 0; h Þ

## (A:7)

for h > 0. We note that the left-hand side of equation (A.7) does not depend on I. We can therefore keep I ﬁxed and equal to any given I * (say) in the expression on the right-hand side. Since f(u, I) is known and Γ(C, h, I) is identiﬁed due to (A.4), both ζ (C, I *) and λ * (C, h, I *) are identiﬁed for positive h. However, even when I* has been ﬁxed, equation (A.5) cannot be used to determine r(I *) since v(C, 0) is not identiﬁed. When I * has been ﬁxed, we can suppress I * in the notation and write ζ (C) = ζ (C, I * ), λ * (C, h) = λ * (C, h, I * ), r = r(I *) and v(C 0, h) = δ(h) in equation (A.7), which completes the proof. Proof of Theorem 3. By Assumption 4, g 2 (w|h) = g 2 (w). Note next that the relation in (A.7) does not necessesarily imply that r(I) is independent of I. From equations (2a) and (A.7) it then follows that for I > 0,h ≠ h * 2 D φ ð h; wjI Þ v ð f ð hw; I Þ; h Þg 1 ð h Þ ζ ð f ð hw; I Þ; I Þ r ð I Þ λ ð f ð hw; I Þ; h; I Þδ ð h Þg 1 ð h Þ ¼ ¼ φ ð h; wjI Þ v ð f ð h w; I Þ; h Þg 1 ð h Þ ζ ð f ð h w; I Þ; I Þ r ð I Þ λ ð f ð h w; I Þ; h; I Þδ ð h Þg 1 ð h Þ which implies that for w 1 ≠ w 2 φ ð h; w 1 jI Þλ ð f ð h w 1; I Þ; h; I Þ φ ð h; w 2 jI Þλ ð f ð hw 2; I Þ; h; I Þ log φ ð h; w 1 jI Þλ ð f ð hw 1; I Þ; h; I Þ φ ð h; w 2 jI Þλ ð f ð h w 2; I Þ; h; I Þ ζ ð f ð hw 1; I Þ; I Þ ζ ð f ð h w 2; I Þ; I Þ ¼ r ð I Þlog ζ ð f ð h w 1; I Þ; I Þ ζ ð f ð hw 2; I Þ; I Þ Copyright © 2015 John Wiley & Sons, Ltd.

## (A:8)

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## LABOR SUPPLY AS A CHOICE AMONG LATENT JOBS

From equation (A.8) we see that r(I) is identiﬁed. Thus λ(C, h) deﬁned by λ(C, h) = ζ (C, I) r(I) λ * (C, h, I) is identiﬁed and equation (A.7) implies that λ(C, h) does not depend on I. Hence v(C, h) = λ(C, h)δ(h) for positive h. We thus realize that v(C, h) is identiﬁed for positive h up to a multiplicative term δ(h) that is solely a function of hours of work. Consider next the case with h = 0. From equation (A.5) we have ∂log v ð f ð 0; I Þ; 0 Þ ¼ r ð I Þ

## ∂I

## (A:9)

The right-hand side of equation (A.9) is known, since r(I) is identiﬁed by equation (A.8). By integrating equation (A.9) with respect to I we realize that log v(f(0, I), 0) is determined for each positive I up to an additive constant. But this means that v(C, 0) is identiﬁed up to a multiplicative constant. In the case where the distribution of offered wage rates is not degenerate we get from equation (2a) and the results above g 2 ð w Þ ¼ g 2 ð w Þ φ ð h; wjI Þ=λ ð f ð hw; I Þ; h Þ φ ð h; w j IÞ=λ ð f ð hw; I Þ; h Þ

## (A:10)

By integrating equation (A.10) (or summing in the case with discrete offered wage rates) with respect to positive w it follows (because the left-hand side is a p.d.f. function) that 1 g 2 ð w Þ ð φ ð h; y j IÞ=λ ð f ð hy; I Þ; hÞ Þdy 1 ¼ φ ð h; w jI Þ=λ ð f ð hw; I Þ; h Þ 0 ∫ which together with (A.10) yields g 2 ð w Þ ¼ 1 φ ð h; wjI Þ=λ ð f ð hw; I Þ; h Þ

## (A:11)

∫ 0 ð φ ð h; y j IÞ=λ ð f ð hy; I Þ; h ÞÞdy which shows that g 2 (w) is identiﬁed. The proof is thus complete.

## APPENDIX B

Simulation of Changes in the Opportunity Distribution of Offered Hours of Work Recall that in our framework g 1F (h) represents the proportion of jobs with hours of work, h, that are available to the wife, whereas the parameter θ F is a measure of job availability to the wife. Note that there are two peaks in the estimated offered hour distribution, namely when h = h p (part time) and h = h f (full-time). The proposed reform can be interpreted as a change in the opportunity distribution of hours for women, obtained by removing the part-time peak and increasing the fulltime peak (since the part-time jobs are replaced by full-time ones) while keeping the job availability unchanged (i.e. θ F is unchanged). Denote the new opportunity distribution by g 1F ð h Þ. After the part-time peak has been removed, the offered hours are uniformly distributed apart from a peak at the full-time interval. Since there are ﬁve intervals for which the new opportunity density is constant, we must have that Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae

## J. K. DAGSVIK AND Z. JIA

g 1F ð h Þ ¼ 1 g 1F h p g 1F h f =5 for h ≠ h f. In addition, the sum of jobs in part-time and full-time intervals is the same before and after reform:

θ F g 1F h p þ θ F g 1F ð h F Þ ¼ θ F g 1F h p þ θ F g 1F ð h F Þ

From these two equations it follows that g 1F h f ¼ 6g 1F h p þ 6g 1F h f 1 =5 One can apply the model to simulate the corresponding realized labor supply distribution by replacing g 1F (h) with g 1F ð h Þ.

Copyright © 2015 John Wiley & Sons, Ltd.

J. Appl. Econ. 31: 487–506 (2016)

DOI: 10.1002/jae
