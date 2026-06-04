# A Practitioner's Guide to Cluster-Robust Inference

A. Colin Cameron Douglas L. Miller

## ABSTRACT

We consider statistical inference for regression when data are grouped into clusters, with regression model errors independent across clusters but correlated within clusters. Examples include data on individuals with clustering on village or region or other category such as industry, and state-year differences-in-differences studies with clustering on state. In s settings, default standard errors can greatly overstate estimator precision Instead, if the number of clusters is large, statistical inference after OLS should be based on cluster-robust standard errors. We outline the basic method as well as many complications that can arise in practice. These include cluster-specific fixed effects, few clusters, multiway clustering, and estimators other than OLS.

## I. Introduction

In an empiricist's day-to-day practice, most effort is spent on getting unbiased or consistent point estimates. That is, a lot of attention is given to the param eters (ß). In this paper, we focus on getting accurate statistical inference, a fundamen tal component of which is obtaining accurate standard errors (se, the estimated stan dard deviation of ß). We begin with the basic reminder that empirical researchers should also really care about getting this part right. An asymptotic 95 percent confi dence interval is ß ± 1.96 x se, and hypothesis testing is typically based on the Wald "f-statistic" w = (ß -ß0) / se. Both ß and se are critical ingredients for statistical in Colin Cameron is a professor in the Department of Economics at UC-Davis. Doug Miller is an associate professor in the Department of Economics at UC-Davis. They thank four referees and the journal editor for very helpful comments and for guidance, participants at the 2013 California Econometrics Conference, a workshop sponsored by the U.K. Programme Evaluation for Policy Analysis, seminars at University of Southern California and at University of Uppsala, and the many people who over time have sent them cluster-related puzzles (the solutions to some of which appear in this paper). Doug Miller acknowledges financial support from the Center for Health and Wellbeing at the Woodrow Wilson School of Public Policy at Princeton University. The data used in this article can be obtained beginning November 2015 through

October 2018 from the authors.

[Submitted March 2013; accepted January 2014] ISSN 0022-166X E-ISSN 1548-8004 © 2015 by the Board of Regents of the University of Wisconsin System

## THE JOURNAL OF HUMAN RESOURCES • 50-2

ference, and we should be paying as much attention to getting a good se as we do to obtaining ß. In this paper, we consider statistical inference in regression models where observa tions can be grouped into clusters, with model errors uncorrelated across clusters but correlated within cluster. One leading example of "clustered errors" is individual-level cross-section data with clustering on geographical region, such as village or state. Then model errors for individuals in the same region may be correlated while model errors for individuals in different regions are assumed to be uncorrelated. A second leading example is panel data. Then model errors in different time periods for a given individual (for example, person, firm, or region) may be correlated while model errors for different individuals are assumed to be uncorrelated. Failure to control for within-cluster error correlation can lead to very misleadingly small standard errors, and consequent misleadingly narrow confidence intervals, large r-statistics, and low p-values. It is not unusual to have applications where standard errors that control for within-cluster correlation are several times larger than default standard errors that ignore such correlation. As shown below, the need for such con trol increases not only with increase in the size of within-cluster error correlation, but the need also increases with the size of within-cluster correlation of regressors and with the number of observations within a cluster. A leading example, highlighted by Moulton (1986, 1990), is when interest lies in measuring the effect of a policy variable, or other aggregated regressor, that takes the same value for all observations within a cluster. One way to control for clustered errors in a linear regression model is to addition ally specify a model for the within-cluster error correlation, consistently estimate the parameters of this error correlation model, and then estimate the original model by feasible generalized least squares (FGLS) rather than ordinary least squares (OLS). Examples include random effects estimators and, more generally, random coefficient and hierarchical models. If all goes well, this provides valid statistical inference as well as estimates of the parameters of the original regression model that are more efficient than OLS. However, these desirable properties hold only under the very strong assumption that the model for within-cluster error correlation is correctly specified. A more recent method to control for clustered errors is to estimate the regression model with limited or no control for within-cluster error correlation, and then, post estimation, obtain "cluster-robust" standard errors proposed by White (1984, pp. 134— 142) for OLS with a multivariate dependent variable (directly applicable to balanced clusters), by Liang and Zeger (1986) for linear and nonlinear models, and by Arellano (1987) for the fixed effects estimator in linear panel models. These cluster-robust stan dard errors do not require specification of a model for within-cluster error correlation but do require the additional assumption that the number of clusters, rather than just the number of observations, goes to infinity. Cluster-robust standard errors are now widely used, popularized in part by Rogers (1993), which incorporated the method in Stata, and by Bertrand, Duflo, and Mullaina than (2004), which pointed out that many differences-in-differences studies failed to control for clustered errors, and those that did often clustered at the wrong level. Cam eron and Miller (2011) and Wooldridge (2003, 2006) provide surveys, and lengthy expositions are given in Angrist and Pischke (2009) and Wooldridge (2010).

One goal of this paper is to provide the practitioner with the methods to implement cluster-robust inference. To this end, we include in the paper reference to relevant Stata commands (for Version 13) because Stata is the computer package most often used in applied microeconometrics research. And we will post on our websites more expansive Stata code and the data sets used in this paper. A second goal is presenting how to deal with complications such as determining when there is a need to cluster, incorporating fixed effects, and inference when there are few clusters. A third goal is to provide an ex position of the underlying econometric theory as this can aid in understanding compli cations. In practice, the most difficult complication to deal with can be "few" clusters, see Section VI. There is no clear-cut definition of "few"; depending on the situation, "few" may range from less than 20 to less than 50 clusters in the balanced case. We focus on OLS, for simplicity and because this is the most commonly used esti mation method in practice. Section II presents the basic results for OLS with clustered errors. In principle, implementation is straightforward as econometrics packages in clude cluster-robust as an option for the commonly used estimators; in Stata it is the vce(cluster) option. The remainder of the survey concentrates on complications that often arise in practice. Section III addresses how the addition of fixed effects impacts cluster-robust inference. Section IV deals with the obvious complication that it is not always clear what to cluster over. Section V considers clustering when different ways exist to do so and these ways are not nested in each other. Section VI considers how to adjust inference when there are just a few clusters as, without adjustment, test statistics based on the cluster-robust standard errors overreject and confidence intervals are too narrow. Section VII presents extension to the full range of estimators — instrumental variables, nonlinear models such as logit and probit, and generalized method of mo ments. Section VIII presents both empirical examples and real-data based simulations. Concluding thoughts are given in Section IX.

## II. Cluster-Robust Inference

In this section, we present the fundamentals of cluster-robust inference.

For these basic results, we assume that the model does not include cluster-specific fixed effects, that it is clear how to form the clusters, and that there are many clusters. We relax these conditions in subsequent sections. Clustered errors have two main consequences: They (usually) reduce the precision of ß, and the standard estimator for the variance of ß, V[ß], is (usually) biased down ward from the true variance. Computing cluster-robust standard errors is a fix for the latter issue. We illustrate these issues, initially in the context of a very simple model and then in the following subsection in a more typical model.

A. A Simple Example For simplicity, we begin with OLS with a single regressor that is nonstochastic, and assume no intercept in the model. The results extend to multiple regression with sto chastic regressors. Let yt = ßjc, + «j, i = 1,..., N, where x. is nonstochastic and E[u] = 0. The OLS estimator ß = Xjxiyj / 2,pcf can be reexpressed as ß -ß = S,jc,w, / Ipc?, so in general (1) V[ß] = E[(ß -ß)2] = V [X *,«,] / (S *,2)2 /

If / errors are uncorre case of homoskedastic

If instead errors are vhet[W using

V[mJ =

E[w2] of each of the mates naturally estimate is = the to of

## OLS

Vhet[ß] = the the p s t cluste scalar residual, p

## 1 (X*

The resulting standard error for ß is often called a robust standard error, though a bet ter, more precise, term is heteroskedastic-robust standard error. What if errors are correlated over /? In the most general case where all errors are correlated with each other, 2*a| = X XCov[x<""xä] = X 2-voe[m;"/]> so

VcJß] = p / px2j2.

The obvious extension of White (1980) is to use V[ß] = (X^jxpcjûfij]) / (2,x2)2but this equals zero since Xpclûi = 0. Instead, one needs to first set a large fraction of th error correlations E[uuß to zero. For time series data with errors assumed to be co related only up to, say, m periods apart as well as heteroskedastic, White's result can be extended to yield a heteroskedastic-and autocorrelation-consistent (HAC) variance estimate; see Newey and West (1987). In this paper, we consider clustered errors, with E[um] = 0 unless observations i and j are in the same cluster (such as same region). Then (2) Vclu[ß] = in same clustei"])1 £*?) > where the indicator function 1[A] equals 1 if event A happens and equals 0 if even A does not happen. Provided the number of clusters goes to infinity, we can use the variance estimate (3) Vdu[ß] = [X XWi'lw' in same cluster]] / ■xi?

## (X

This estimate is called a cluster-robust estimate though, more precisely, it is hetero skedastic-and cluster-robust. This estimate reduces to Vhet[ß] in the special case that there is only one observation in each cluster. Typically Vclu[ß] exceeds Vhet[ß] due to the addition of terms when i * j. The amount of increase is larger (1) the more positively associated are the regressors across observations in the same cluster (via xx. in Equation 3), (2) the more correlated are the errors (via E[w;w] in Equation 2), and (3) the more observations are in the same cluster (via 1 [i,j in same cluster] in Equation 3). There are several take-away messages. First there can be great loss of efficiency in OLS estimation if errors are correlated within cluster rather than completely uncorrected. Intuitively, if errors are positively correlated within cluster, then an additional observation in the cluster no longer provides a completely independent piece of new information. Sec ond, failure to control for this within-cluster error correlation can lead to using standard errors that are too small, with consequent overly narrow confidence intervals, overly large ^-statistics, and overrejection of true null hypotheses. Third, it is straightforward to obtain cluster-robust standard errors, though they do rely on the assumption that the number of clusters goes to infinity (see Section VI for the few clusters case).

B. Clustered Errors and Two Leading Examples Let i denote the i'h of N individuals in the sample and g denote the g'h of G clusters. Then for individual i in cluster g the linear model with (one-way) clustering is (4) yig = x'igß + uig, where xig is a K x 1 vector. As usual, it is assumed that E[uig\xjg\ = 0. The key assump tion is that errors are uncorrected across clusters while errors for individuals belong ing to the same cluster may be correlated. Thus (5) E[uiguJg, I xig,x#] = 0, unless g = g'.

1. Example 1: individuals in cluster Hersch (1998) uses cross-section individual-level data to estimate the impact of job injury risk on wages. As there is no individual-level data on job-injury rate, a more aggregated measure such as job injury risk in the individual's industry is used as a regressor. Then for individual i (with N -5,960) in industry g (with G = 211) yig = yXxg + 4s + v The regressor x is perfectly correlated within industry. The error term will be posi tively correlated within industry if the model systematically overpredicts (or under predicts) wages in a given industry. In this case, default OLS standard errors will be downward biased. To measure the extent of this downward bias, suppose errors are equicorrelated within cluster, so Cor[m,«] = p for all; t j. This pattern is suitable when observa tions can be viewed as exchangeable, with ordering not mattering. Common examples include the current one, individuals or households within a village or other geographic unit (such as state), individuals within a household, and students within a school. Then a useful approximation is that for the k'h regressor the default OLS variance estima based on j2(XÏ)_i, where s is the standard error of the regression, should be inflated b (6) rk = 1 + pXkPu(Ng -1), where pr, is a measure _ of the within-cluster correlation of x,, p„ is the within-clust fxk

Igk' ru error correlation, clusters are of 1981);

see

Scott single a equ and regressor.

very importan creasing in (1) the within-cluster correlation of the regressor (2) the within-cluster correlation of the error (3) the number of observations in each cluster. For clusters of unequal size replace (N -1) in (6) by ((VfA',,] I N) + Ng -1); see Moulton (1986, p. 387). Note that there is no cluster problem if any one of the follow ing occur: pI4 = 0 or pu = 0 or Ng = 1. In an influential paper, Moulton (1990) pointed out that in many settings the inflation factor Jk can be large even if pu is small. It considered a log earnings re gression using March CPS data (N ~ 18,946), regressors aggregated at the state level (G = 49), and errors correlated within state (pu = 0.032). The average group size was 18,946 / 49 = 387, pv< = 1 for a state-level regressor, so Equation 6 yields ft = 1 + 1 x 0.032 x 386 = 13.3. The weak correlation of errors within state was still enough to lead to cluster-corrected standard errors being Vl3.3 = 3.7 times larger than the (incorrect) default standard errors! In such examples of cross-section data with an aggregated regressor, the cluster robust standard errors can be much larger despite low within-cluster error correlation because the regressor of interest is perfectly correlated within cluster and there may be many observations per cluster.

2. Example 2: differences-in-differences (DiD) in a state-year panel Interest may lie in how wages respond to a binary policy variable dts that varies by state and over time. Then at time t in state s y* = "Y x d„ + <s7 + as + 8, + uls, where we assume independence over states, so the ordering of subscripts (t, s) corre sponds to (i, g) in Equation 4, and at and 8, are state and year effects. The binary regressor dts equals one if the policy of interest is in effect and equals zero otherwise. The regressor dts is often highly serially correlated since, for example, dts will equal a string of zeroes followed by a string of ones for a state that switches from never having the policy in place to forever after having the policy in place. The error uts is correlated over time for a given state if the model systematically overpre dicts (or underpredicts) wages in a given state. Again, the default standard errors are likely to be downward biased.

In the panel data case, the within-cluster (that is, within-individual) error correlation decreases as the time separation increases so errors are not equicorrelated. A better model for the errors is a time-series model such as an autoregressive error of order one that im plies that Coi[uls, ufs] = p1'. The true variance of the OLS estimator will again be larger than the OLS default although the consequences of clustering are less extreme than in the case of equicorrelated errors (see Cameron and Miller 2011, Section 2.3, for more detail). In such DiD examples with panel data, the cluster-robust standard errors can be much larger than the default because both the regressor of interest and the errors are highly correlated within cluster. Note also that this complication can exist even with the inclusion of fixed effects (see Section III). The same problems arise if we additionally have data on individuals, so that y us = y x < + 4s + », +8, + «te In an influential paper, Bertrand, Duflo, and Mullainathan (2004) demonstrated the importance of using cluster-robust standard errors in DiD settings. Furthermore, the clustering should be on state, assuming error independence across states. The cluster ing should not be on state-year pairs because, for example, the error for California in 2010 is likely to be correlated with the error for California in 2009. The issues raised here are relevant for any panel data application, not just DiD stud ies. The DiD panel example with binary policy regressor is often emphasized in the cluster-robust literature because it is widely used and it has a regressor that is highly serially correlated, even after mean-differencing to control for fixed effects. This serial correlation leads to a potentially large difference between cluster-robust and default standard errors.

## C. The Cluster-Robust Variance Matrix Estimate

Stacking all observations in the g'h cluster, the Model 4 can be written as yg = xg$ + ug, g = \,...,G, whereyg and u are Ng x 1 vectors,Xg is an Ng x K matrix, and there areNg observations in cluster g. Further stacking y, Xg and ug over the G clusters then yields the model = Xß + u.

The OLS estimator is (g y1 g ß = (**)-'**= ^X'gXg vg=i y g=i In general, the variance matrix conditional on X is (7) V[ß] = (A-^Q-'BtXCV)-1, with (8) B = X'V[u\X]X.

Given error independence across clusters, V|wlX| has a block-diagonal structure, and Equation 8 simplifies to

## G

(9) Ädu = «=i The matrix ßdu, the middle part of the "sandwich matrix" Equation 7, corresponds to the numerator of Equation 2. Bclu can be written as:

G Ng Ng «du = ES g=I i=l y=i where co = o

E[u, «, \X

J is the error o covariance for the ig'h and jg'h observations.

We

Vo

Jo o a can will gain be cluster regresso tions rors m giv tion of correlat

Implem estimate do) vc where

## G

(id «du = x WA' g=i and ûg = yg-X,ß is the vector of OLS residuals for the g'h cluster. Formally, Equa tion 10 and Equation 11 provides a consistent estimate of the variance matrix if G~]Zg^\X'gûgù'gXg -G~^^=^L[X'gugu'gXg] A 0 as G —» °°. Initial derivations of this estimator, by White (1984, pp. 134-42) for balanced clusters, and by Liang and Zeger (1986) for unbalanced, assumed a finite number of observations per cluster. Hansen (2007a) showed that the CRVE can also be used if Ng —> °°, the case for long panels, in addition to G —> °°. Carter, Schnepel, and Steigerwald (2013) considers unbalanced panels with either Ng fixed or Ng —> The sandwich formula for the CRVE extends to many estimators other than OLS; see Section VII. Algebraically, the estimator Equation 10 and Equation 11 equals Equations 7 and 9 with E[ugu'g] replaced with ûgûg. What is striking about this is that for each cluster g, the Ng x Ng matrix ûgû'g is bound to be a very poor estimate of the Ng x Ng matrix E[«Ä«^]—there is no averaging going on to enable use of a Law of Large Numbers. The "magic" of the CRVE is that despite this, by averaging across all G clusters in Equation 11, we are able to get a consistent variance estimate. This fact helps us to understand one of the limitations of this method in practice — the averaging that makes V[ß] accurate for V[ß] is an average based on the number of clusters G. In applications with few clusters, this can lead to problems that we discuss below in Section VI. Finite-sample modifications of Equation 11 are typically used to reduce downward bias in Vclu[ß] due to finite G. Stata uses yJcûg in Equation 11 rather than ûg, with (12) c =

## G -1 N -K

In general c -G / (G -1), though Section HIB addresses an important exception when fixed effects are directly estimated. Some other packages such as SAS use c-G / (G -1), a simpler correction that is also used by Stata for extensions to nonlinear models. Either choice of c usually lessens, but does not fully eliminate, the usual downward bias in the CRVE. Other finite-cluster corrections are discussed in Section VI but there is no clear best correction.

D. Feasible GLS If errors are correlated within cluster, then in general OLS is inefficient and feasible GLS may be more efficient. Suppose we specify a model for Qg = E[ugug \ Xg] in Equation 9, such as within cluster equicorrelation. Then the GLS estimator is (X'Q~1X)~lÄ''Q~ii)>, where £2 = Diag[Og]. Given a consistent estimate Ù, of £2, the feasible GLS estimator of ß is

## (G

(13) ß

## FGLS

Vs=1 g=l The FGLS estimator is second-moment efficient, with variance matrix (14) vdef[ßFGLS] = (jrn-1*)-1, under the strong assumption that the error variance Q is correctly specified. Remarkably, the cluster-robust method of the previous section can be extended to FGLS. Essentially, OLS is the special case where Qg = <t2/v. The cluster-robust es timate of the asymptotic variance matrix of the FGLS estimator is (g (15) vclu[ßFGLS] = (xn-'xr (A"n~'x)"',

V?=i where ûg = yg -A^ßpoLs-This estimator requires that ug and uh are uncorrelated when g * h, and that G -> °°, but permits E[ugu'g \ Xg] *. The approach of speci fying a model for the error variances and then doing inference that guards against misspecification of this model is especially popular in the biostatistics literature that calls ily a "working" variance matrix (see, for example, Liang and Zeger 1986). There are many possible candidate models for Clg, depending on the type of data being analyzed. For individual-level data clustered by region, the example in Section IIB 1, a com mon starting point model is the random effects (RE) model. The error in Model 4 is specified to have two components: (iö) uig = ag + e;g, where ag is a cluster-specific error or common shock that is assumed to be independent and identically distributed (iid) (0, o^), and ejg is an idiosyncratic error that is assumed to be iid (0, <r2e). Then V[«;g] = cn + uj and Cov[wig, ujg\ = for i * j. It follows that the intraclass correlation of the error pu = Cor[«;g, uJg] = <t\ / (o^ + <t^) so this model implies equicorrelated errors within cluster. Richer models that introduce heteroskeda ticity include random coefficients models and hierarchical linear models.

For panel data, the example in Section IIB2, a range of time series models for ui may be used, including autoregressive and moving average error models. Analysis of within-cluster residual correlation patterns after OLS estimation can be helpful in se lecting a model for Cig.

Note that in all cases if cluster-specific fixed effects are included as regressors an

## N

is small then bias-corrected FGLS should be used; see Section IIIC.

g The efficiency gains of FGLS need not be great. As an extreme example, with equicorrelated errors, balanced clusters, and all regressors invariant within cluster (jt.ç = jc) the FGLS estimator equals the OLS estimator — and so there is no efficiency gain to AjLS. With equicorrelated errors and general X, Scott and Holt (1982) provides an upper bound to the maximum proportionate efficiency loss of OLS, compared to the variance of the FGLS estimator, of 1 / [1 + (4(1 -p„)[l + (,Vmax -l)p„) / (Nmax x p„)2], iVraax = max{Np..., N G). This upper bound is increasing in the error correlation pu and the maximum cluster size /Vmax. For low pu, the maximal efficiency gain can be low.

For example, Scott and Holt (1982) notes that for pu = 0.05 and iVmax = 20 there is at most a 12 percent efficiency loss of OLS compared to FGLS. With pu = 0.2 and /Vmax = 100, the efficiency loss could be as much as 86 percent, though this depends on the nature of X.

There is no clear guide to when FGLS may lead to considerable improvement in efficiency, and the efficiency gains can be modest. However, especially in models without cluster-specific fixed effects, implementation of FGLS and use of Equation 15 to guard against misspecification of Q,, is straightforward. And even modest efficiency gains can be beneficial. It is remarkable that current econometric practice with clus tered errors ignores the potential efficiency gains of FGLS.

E. Implementation for OLS and FGLS For regression software that provides a cluster-robust option, implementation of the CRVE for OLS simply requires defining for each observation a cluster identifier vari able that takes one of G distinct values according to the observation's cluster, and then passing this cluster identifier to the estimation command's cluster-robust option. For example, if the cluster identifier is id_clu, then Stata OLS command regress y x becomes regress y x, vce(cluster id_clu). Wald hypothesis tests and confidence intervals are then implemented in the usual way. In some cases, however, joint tests of several hypotheses and of overall statistical significance may not be possible. The CRVE Vclu[ß] is guaranteed to be positive semi definite, so the estimated variance of the individual components of ß are necessarily nonnegative. But Vclu[ß] is not necessarily positive definite, so it is possible that the variance matrix of linear combinations of the components of ß is singular. The rank of VC|U[ß] equals the rank of B defined in Equation 11. Because B = C'C, where C = [JV'/i, • • • X'GûG\ is a K x G matrix, it follows that the rank of B, and hence that of Vclu[ß], is at most the rank of C. Because X\ûx + ••• + X'GûG = 0, the rank of C is at most the minimum of K and G -1. Effectively, the rank of Vdu[ß] equals min(AT, G -1), though it can be less than this in some examples such as perfect collinearity of regres sors and cluster-specific dummy regressors (see Section HIB for the latter).

A common setting is to have a richly specified model with thousands of observa tions in far fewer clusters, leading to more regressors than clusters. Then Vclu[ß] is rank-deficient, so it will not be possible to perform an overall F test of the joint statis tical significance of all regressors. And in a log-wage regression with occupation dum mies and clustering on state, we cannot test the joint statistical significance of the oc cupation dummies if there are more occupations than states. But it is still okay to perform statistical inference on individual regression coefficients and to do joint tests on a limited number of restrictions (potentially as many as min(#T, G -1)). Regression software usually also includes a panel data component. Panel commands may enable not only OLS with cluster-robust standard errors but also FGLS for some models of within-cluster error correlation with default (and possibly cluster-robust) standard errors. It is important to note that those panel data commands that do not ex plicitly use time-series methods —an example is FGLS with equicorrelation of errors within-cluster—can be applied more generally to other forms of clustered data, such as individual-level data with clustering on geographic region. For example, in Stata first give the command xtset idjclu to let Stata know that the cluster-identifier is variable id_clu. Then the Stata command xtreg y x, pa corr(ind) vce(robust) yields OLS estimates with cluster-robust standard errors. Note that for Stata xt commands, option vce(robust) is generally interpreted as meaning cluster-robust; this is always the case from Version 12.1 on. The xt commands use standard normal critical values whereas command regress uses Student's T(G -1) critical values; see Sections VI and VIIA for further discussion. For FGLS estimation, the commands vary with the model for. For equicorrelated errors, a starting point for the example in Section IIB 1, the FGLS estimator can be obtained using command xtreg y x, pa corr(exch) or command xtreg y x, re; slightly different estimates are obtained due to slightly different estimates of the equicorrela tion. For FGLS estimation of hierarchical models that are richer than a random effects model, use Stata command mixed (Version 13) orxtmixed (earlier versions). For FGLS with panel data and time variable time, first give the command xtset id_clu time to let Stata know both the cluster-identifier and time variable. A starting point for the ex ample in Section IIB2 is an autoregressive error of order 1, estimated using command xtreg y x, pa corrfar 1). Stata permits a wide range of possible models for serially correlated errors. In all of these FGLS examples, the reported standard errors are the default ones that assume correct specification of Qg. Better practice is to add option vce(robust) for xtreg commands, or option vce(cluster id_clu) for mixed commands, as this yields standard errors that are based on the cluster-robust variance defined in Equation 15.

F. Cluster-Bootstrap Variance Matrix Estimate Not all econometrics packages compute cluster-robust variance estimates, and even those that do may not do so for all estimators. In that case, one can use a pairs cluster bootstrap that, like the CRVE, gives a consistent estimate of V[ß] when errors are clustered. To implement this bootstrap, do the following steps B times: (1) form G clusters {(^*,AT*),...,^,^)} by resampling with replacement G times from the original sample of clusters, and (2) compute the estimate of ß, denoted ßÄ in the b'h bootstrap sample. Then, given the B estimates ß,,..., ßfi, compute the variance of these

Vc1u;b„„t[ß] = 7j-i(ßi-ß)(ßi-ß)', ** 1 6=1 where ß = Ä~'£f=|ß4, and B = 400 should be more than adequate in most settings. It is important that the resampling be done over entire clusters rather than over individual observations. Each bootstrap resample will have exactly G clusters, with some of the original clusters not appearing at all while others of the original clusters may be re peated in the resample two or more times. The terms "pairs" is used as (y, X) are resampled as a pair. The term "nonparametric" is also used for this bootstrap. Some alternative bootstraps hold Xg fixed while resampling. For finite clusters, if Vclu[ß] uses *Jcûg in Equation 11 then for comparability Vclu;boot[ß] should be multiplied by the constant c defined in Equation 12. The pairs cluster bootstrap leads to a cluster-robust variance matrix for OLS with rank K even if K > G. An alternative resampling method that can be used is the leave-one-cluster-out jackknife. Then, letting ßg denote the estimator of ß when the g'h cluster is deleted,

## C-1 G --

vdu;jacl£[ß] = ^X(ßg-ß)(ßg-ß)' u g=i where ß = G~'2g=1ßg. This older method can be v bootstrap that does not work as well for nonlinear the bootstrap and has the same rank as the CRVE.

Unlike a percentile-f cluster bootstrap, presented and cluster jackknife variance matrix estimates are CRVE so it is best and quickest to use the CRVE if always available, especially for estimators more c one can instead use the pairs cluster bootstrap, thou potential pitfalls if there are few clusters, or even In Stata, the pairs cluster bootstrap for OLS wi mented in several equivalent ways including: reg reps(400) seed(l0101)); xtreg y x, pa corrf ind) vce bootstrap, cluster!id_clu) reps(400) seed(10101): r used for estimation commands and user-written pr option. We recommend 400 bootstrap iterations fo bility one should always set the seed.

For the jackknife the commands are instead, re cluster(id_clu)); xtreg y x, pa corr(ind) vce(jack regress y x. For Stata xt commands, options vce interpreted as meaning cluster bootstrap and clust

## 12.1 on.

## III. Cluster-Specific Fixed Effects

The cluster-specific fixed effects (FE) mod cept for each cluster, so

## G

(17) y,g = 4ß + «g + uig = 4ß + + "tg> h= 1 where, the h'h of G dummy variables, equals one if the ig'h observation is in cluster h and equals zero otherwise. There are several different ways to obtain the same cluster-specific fixed effects esti mator. The two most commonly used are the following. The least squares dummy variable (LSDV) estimator directly estimates the second line of Equation 17, with OLS regression of y. on xig and the G dummy variables dl,..., dGjg, in which case the dummy variable coefficients â = y -x'ß where y„ = N'^f.y. and x = The within es

## O

## O

## O

## O

## O

## O

## O

## O

timator, al within or m (18)

The that 17 (y,g - main it that error con we but

Cov[jclg, u to inconsi

Model 18 t result cluste diately to

In the rem fixed effe error and

The

The degrees-of rather tha cluster size a modified version of the Hausman test.

A. Do Fixed Effects Fully Control for Within-Cluster Correlation? While cluster-specific effects will control for part of the within-cluster correlation of the error, in general they will not completely control for within-cluster error correla tion (not to mention heteroskedasticity). So the CRVE should still be used. There are several ways to make this important point. Suppose we have data on students in classrooms in schools. A natural model, a special case of a hierarchical model, is to suppose that there is both an unobserved school effect and, on top of that, an unobserved classroom effect. Letting i denote in dividual, s school, and c classroom, we have yisc = x'Jfß + + 8C + eISC. A regression with school-level fixed effects (or random effects) will control for within-school cor relation but not the additional within-classroom correlation. Suppose we have a short panel (T fixed, N -> =») 0f uncorrected individuals and estimate yu = x':$ + ai + uir Then the error uit may be correlated over time (that is, within-cluster) due to omitted factors that evolve progressively over time. Inoue and Solon (2006) provides a test for this serial correlation. Cameron and Trivedi (2005, p. 710) presents an FE individual-level panel data log-earnings regressed on log-hours example with cluster-robust standard errors four times the default. Serial correlation in the error may be due to omitting lagged y as a regressor. When y. {is included as an additional regressor in the FE model, the Arellano-Bond estimator is used and, even with yu l included, the Arellano-Bond methodology requires that we first test whether the remaining error ujt is serially correlated. Finally, suppose we have a single cross-section (or a single time series). This can be viewed as regression on a single cluster. Then in the model yt, = a + *'ß + ui (or y, = a + x'ß + u), the intercept is the cluster-specific fixed effect. There are many reasons for why the error uj (or ut) may be correlated in this regression.

B. Cluster-Robust Variance Matrix with Fixed Effects Since inclusion of cluster-specific fixed effects may not fully control for cluster cor relation (and/or heteroskedasticity), default standard errors that assume ujg to be iid may be invalid. So one should use cluster-robust standard errors. Arellano (1987) showed that Vclu[ß] defined in Equations 10 and 11 remains valid for the within estimator that controls for inclusion of G cluster-specific fixed effects, provided G -* <*> and N is small. If instead one obtains the LSDV estimator, the CRVE formula gives the same CRVE for ß as that for the within estimator, with the important proviso that the same degrees-of-freedom adjustment must be used —see below. The fixed effects estimates âg obtained for the LSDV estimator are essentially based only on Ng observations, so V[âg] is inconsistent for V[âg], just as &g is incon sistent for a Hansen (2007a, p. 600) shows that this CRVE can also be used if additionally Ng —» °o, for both the case where within-cluster correlation is always present (for example, for many individuals in each village) and for the case where within-cluster correlation eventually disappears (for example, for panel data where time series cor relation disappears for observations far apart in time). The rates of convergence are VG in the first case and <jGNg in the second case but the same asymptotic variance matrix is obtained in either case. Kézdi (2004) analyzed the CRVE in FE models for a range of values of G and N. It is important to note that, while LSDV and within estimation lead to identical es timates of ß, they can yield different standard errors due to different finite sample degrees-of-freedom correction. It is well known that if default standard errors are used, that is, it is assumed that uig in Equation 17 is iid, then one can safely use standard errors after LSDV estimation as this correctly views the number of parameters as G + K rather than K. If instead the within estimator is used, however, manual OLS estimation of Equation 18 will mistak enly view the number of parameters to equal K rather than G + K. (Built-in panel es timation commands for the within estimator —that is, a fixed effects command — should remain okay to use because they should be programmed to use G + K in calculating the standard errors.) It is not well known that if cluster-robust standard errors are used, and cluster sizes are small, then inference should be based on the within estimator standard errors. We thank Arindrajit Dube and Jason Lindo for bringing this issue to our attention. Within and LSDV estimation lead to the same cluster-robust standard errors if we apply For mula 11 to the respective regressions, or if we multiply this estimate by c = G / (G -1). Differences arise, however, if we multiply by the small-sample correction c given in Equation 12. Within estimation sets c = [G / (G -1)] / [(N -1) / (N -K + 1)] since there are only (K-1) regressors — the within model is estimated without an intercept. LSDV estimation uses c = [G / (G -1)] / [(N -1) / (N -G -K + 1)] since the G clus ter dummies are also included as regressors. For balanced clusters with N = N, and G large relative to K,c -1 for within-estimation and c -N, / (N, -1) for LSDV es timation. Suppose there are only two observations per cluster, due to only two indi viduals per household or two time periods in a panel setting, so N = N, = 2. Then c = 2 / (2 -1) = 2 for LSDV estimation, leading to CRVE that is twice that from within estimation. Within estimation leads to the correct finite-sample correction. In Stata, the within command xtreg y x,fe vce(robust) gives the desired CRVE. The alternative LSDV commands regress y x i.id_clu, vce(cluster id_clu) and, equivalently, regress y x, absorb(id_clu) vce(cluster id_clu) use the wrong degrees-of-freedom cor rection. If a CRVE is needed, then use xtreg. If there is reason to instead use regress i.id, then the cluster-robust standard errors should be multiplied by the square root of [N -(K -1)] / [N -G -(K -1)], especially if N is small. The inclusion of cluster-specific dummy variables increases the dimension of the CRVE but does not lead to a corresponding increase in its rank. To see this, stack the dummy variable dhig for cluster g into the Ng x 1 vector dh. Then dh'gûg = 0, by the OLS normal equations, leading to the rank of Vclu[ß] falling by one for each cluster specific effect. If there are k regressors varying within cluster and G -1 dummies then, even though there are K + G -1 parameters ß, the rank of Vclu[ß] is only the minimum of K and G -1. And a test that a,,..., aG are jointly statistically significant is a test of G -1 restrictions (since the intercept or one of the fixed effects needs to be dropped). So even if the cluster-specific fixed effects are consistently estimated (that is, if -> °°), it is not possible to perform this test if K < G -1, which is often the case. If cluster-specific effects are present, then the pairs cluster bootstrap must be adapted to account for the following complication. Suppose Cluster 3 appears twice in a bootstrap resample. Then if clusters in the bootstrap rèsample are identified from the original cluster-identifier, the two occurrences of Cluster 3 will be incorrectly treated as one large cluster rather than two distinct clusters. In Stata, the bootstrap option idcluster ensures that distinct identifiers are used in each bootstrap resample. Examples are regress y x i.id_clu, vce(boot, cluster(id_clu) idcluster(newid) reps(400) seed(lOlOl)) and, more simply, xtreg y x, fe vce(boot, reps(400) seed(lOlOl)), as in this latter case Stata automatically accounts for this complication.

## C. Feasible GLS with Fixed Effects

When cluster-specific fixed effects are present, more efficient FGLS estimation can become more complicated. In particular, if asymptotic theory relies on G —> °° with N fixed, the ag cannot be consistently estimated. The within estimator of ß is none theless consistent, as ag disappears in the mean-differenced model. But the resulting residuals ûjg are contaminated because they depend on both ß and âg, and these re siduals will be used to form a FGLS estimator. This leads to bias in the FGLS estima tor so one needs to use bias-corrected FGLS unless Ng -> <*>. The correction method varies with the model for O,, = V[«,,], and currently there are no Stata user-written commands to implement these methods. For panel data, a commonly used model specifies an AR(p) model for the errors uig in Equation 17. If fixed effects are present, then there is a bias (of order Ngl) in estima tion of the AR(p) coefficients. Hansen (2007b) obtains bias-corrected estimates of the AR(p) coefficients and uses these in FGLS estimation. Hansen (2007b) in simulations shows considerable efficiency gains in bias-corrected FGLS compared to OLS. Brewer, Crossley, and Joyce (2013) considers a DiD model with individual-level U.S. panel data with N-750,127, T = 30, and a placebo state-level law, so clustering is on state with G -50. It finds that bias-corrected FGLS for AR(2) errors, using the Hansen (2007b) correction, leads to higher power than FE estimation. In its example, ignoring the bias correction does not change results much, perhaps because T = 30 is reasonably large. For balanced clusters with Q.gthe same for all g, say £2g = £2», and for Ng small, then the FGLS estimator in Equation 13 can be used without need to specify a model for £2». Instead we can let Q, have ij'h entry G~'Xg=1â,gû -, where ûjg are the residuals from initial OLS estimation. These assumptions may be reasonable for a balanced panel. Two complications can arise. First, even without fixed effects there may be many off diagonal elements to estimate and this number can be large relative to the number of observations. Second, the fixed effects lead to bias in estimating the off-diagonal co variances. Hausman and Kuersteiner (2008) presents fixes for both complications.

D. Testing the Need for Fixed Effects FE estimation is often accompanied by a loss of precision in estimation, as only within-cluster variation is used (recall we regress (ylg -yg) on (xig -xg)). Further more, the coefficient of a cluster-invariant regressor is not identified because then xjg -xg = 0. Thus, it is standard to test whether it is sufficient to estimate by OLS or FGLS, without cluster-specific fixed effects. The usual test is a Hausman test based on the difference between the FE estimator, ßFE, and the RE estimator, ßRE. Let ß, denote a subcomponent of ß, possibly just the coefficient of a single regressor of key interest; at most, ß, contains the coefficients of all regressors that are not invariant within cluster or, in the case of panel data, that are not aggregate time effects that take the same value for each individual. The chi squared distributed test statistic is ^Haus = (ßl;FE ~~ Pi;Re) ^'(ßl;FE ~ ßl;RE)> where V is a consistent estimate of V[ß1;FE -ß,.RE]. Many studies use the standard form of the Hausman test. This obtains V under the strong assumption that ßRE is fully efficient under the null hypothesis. This requires the unreasonably strong assumptions that ag and eig in Equation 16 are iid, requiring that neither ag nor eig is heteroskedastic and that eig has no within-cluster correlation. As already noted, these assumptions are likely to fail and one should not use default standard errors. Instead, a CRVE should be used. For similar reasons, the standard form of the Hausman test should not be used.

Wooldridge (2010, p. 332) instead proposes implementing a cluster-robust version of the Hausman test by the following OLS regression yig = 4ß + w'gy + uig, where wg denotes the subcomponent of xjg that varies within cluster and wg = N~{X%xwlg. If H0: y = 0 is rejected using a Wald test based on a cluster-robust estimate of the vari ance matrix, then the fixed effects model is necessary. The Stata user-written command xtoverid, due to Schaffer and Stillman (2010), implements this test. An alternative is to use the pairs cluster bootstrap to obtain V, in each resample obtaining ß,.FE and ß1;RE, leading to B resample estimates of (ß,;FE -ß] RF). We are unaware of studies comparing these two cluster-robust versions of the Hausman test.

## IV. What to Cluster Over?

It is not always clear what to cluster over —that is, how to define the clusters — and there may even be more than one way to cluster. Before providing some guidance, we note that it is possible for cluster-robust er rors to actually be smaller than default standard errors. First, in some rare cases errors may be negatively correlated, most likely when N = 2, in which case Equation 6 pre dicts a reduction in the standard error. Second, cluster-robust is also heteroskedastic robust and White heteroskedastic-robust standard errors in practice are sometimes larger and sometimes smaller than the default. Third, if clustering has a modest effect so cluster-robust and default standard errors are similar in expectation, then cluster-robust may be smaller due to noise. In cases where the cluster-robust standard errors are smaller, they are usually not much smaller than the default, whereas in other applications they can be much, much larger.

A. Factors Determining What to Cluster Over There are two guiding principles that determine what to cluster over. First, given V[ß] defined in Equations 7 and 9, whenever there is reason to be lieve that both the regressors and the errors might be correlated within cluster, we should think about clustering defined in a broad enough way to account for that clustering. Going the other way, if we think that either the regressors or the errors are likely to be uncorrelated within a potential group, then there is no need to cluster within that group. Second, Vclu[ß] is an average of G terms that gets closer to V[ß] only as G gets large. If we define very large clusters, so that there are very few clusters to average over in Equation 11, then the resulting Vclu[ß] can be a very poor estimate of V[ß]. This com plication, and discussion of how few is "few," is the subject of Section VI. These two principles mirror the bias-variance tradeoff that is common in many estimation problems — larger and fewer clusters have less bias but more variability. There is no general solution to this tradeoff, and there is no formal test of the level at which to cluster. The consensus is to be conservative and avoid bias and to use bigger and more aggregate clusters when possible, up to and including the point at which there is concern about having too few clusters.

For example, suppose your data set included individuals within counties within states, and you were considering whether to cluster at the county level or the state level. We have been inclined to recommend clustering at the state level. If there was within-state cross-county correlation of the regressors and errors, then ignoring this correlation (for example, by clustering at the county level) would lead to incorrect in ference. In practice, researchers often cluster at progressively higher (that is, broader) levels and stop clustering when there is relatively little change in the standard errors. This seems to be a reasonable approach. There are settings where one may not need to use cluster-robust standard errors. We outline several though note that in all these cases it is always possible to still obtain cluster-robust standard errors and contrast them to default standard errors. If there is an appreciable difference, then use cluster-robust standard errors. If a key regressor is randomly assigned within clusters, or is as good as randomly assigned, then the within-cluster correlation of the regressor is likely to be zero. Thus, there is no need to cluster standard errors even if the model's errors are clustered. In this setting, if there are additionally control variables of interest, and if these are not randomly assigned within cluster, then we may wish to cluster our standard errors for the sake of correct inference on the control variables. If the model includes cluster-specific fixed effects, and we believe that within-cluster correlation of errors is solely driven by a common shock process, then we may not be worried about clustering. The fixed effects will absorb away the common shock, and the remaining errors will have zero within-cluster correlation. More generally, control variables may absorb systematic within-cluster correlation. For example, in a state-year panel setting, control variables may capture the state-specific business cycle. However, as already noted in Section IIIA, the within-cluster correlation is usually not fully eliminated. And even if it is eliminated, the errors may still be heteroskedas tic. Stock and Watson (2008) shows that, surprisingly, applying the usual White (1980) heteroskedastic-consistent variance matrix estimate to the FE estimator leads to incon sistent estimation of V[ß] if Ng is small (though it is correct if N = 2). It derives a bias-corrected formula for heteroskedastic-robust standard errors. Alternatively, and more simply, the CRVE is consistent for V[ß] even if the errors are only heteroskedas tic, though this estimator of V[ß] is more variable. Finally, as already noted in Section IID, we can always build a parametric model of the correlation structure of the errors and estimate by FGLS. If we believe that this parametric model captures the salient features of the error correlations, then default FGLS standard errors can be used.

B. Clustering Due to Survey Design Clustering routinely arises due to the sampling methods used in complex surveys. Rather than randomly draw individuals from the entire population, costs are reduced by sampling only a randomly selected subset of primary sampling units (such as a geo graphic area), followed by random selection, or stratified selection, of people within the chosen primary sampling units. The survey methods literature uses methods to control for clustering that predate the cluster-robust approach of this paper. The loss of estimator precision due to clustered sampling is called the design effect: "The design effect or Deff is the ratio of the actual variance of a sample to the variance of a simple random sample of the same number of elements" (Kish 1965, p. 258). Kish and Frankel (1974) gives the variance inflation formula Equation 6 in the nonregression case of estimation of the mean. Pfeffermann and Nathan (1981) considers the more general regression case. The CRVE is called the linearization formula, and the common use of G -1 as the degrees of freedom used in hypothesis testing comes from the survey methods literature; see Shah, Holt, and Folsom (1977), which predates the econometrics literature. Applied economists routinely use data from complex surveys, controlling for clus tering by using a cluster-robust variance matrix estimate. At the minimum, one should cluster at the level of the primary sampling unit though often there is reason to cluster at a broader level, such as clustering on state if regressors and errors are correlated within state. The survey methods literature additionally controls for two other features of survey data — weighting and stratification. These methods are well-established and are incor porated in specialized software as well as in some broad-based packages such as Stata. Bhattacharya (2005) provides a comprehensive treatment in a GMM framework. If sample weights are provided, then it is common to perform weighted least squares. Then the CRVE forßWLS = (X'WXy]X'Wy is that given in Equation 15 with replaced by Wg. The need to weight can be ignored if stratification is on only the exogenous regressors and we assume correct specification of the model so that in our sample E[^|.Y] = Xß. In that special case, both weighted and unweighted estimators are consistent, and weighted OLS actually may be less efficient if, for example, model errors are iid; see, for example, Solon, Haider, and Wooldridge (2013). An other situation in which to use weighted least squares, unrelated to complex surveys, is when data for the ig'h observation is obtained by in turn averaging N. observations and N. varies.

## 'S

Stratification of the sample can enable more precise statistical inference. These gains can be beneficial in the nonregression case, such as estimating the monthly na tional unemployment rate. The gains can become much smaller once regressors are included because these can partially control for stratification; see, for example, the application in Bhattacharya (2005). Econometrics applications therefore usually do not adjust standard errors for stratification, leading to conservative inference due to some relatively small overestimation of the standard errors.

## V. Multiway Clustering

The discussion to date has presumed that if there is more than one potential way to cluster, these ways are nested in each other, such as households within states. But when clusters are nonnested, traditional cluster-robust inference can only deal with one of the dimensions. In some applications it is possible to include sufficient regressors to eliminate concern about error correlation in all but one dimension, and then do cluster-robust inference for that remaining dimension. A leading example is that in a state-year panel there may be clustering both within years and within states. If the within-year clustering is due to shocks that are the same across all observations in a given year, then including year fixed effects as regressors will absorb within-year clustering, an inference then need only control for clustering on state. When this approach is not applicable, the one-way cluster robust variance can be extended to multiway clustering. Before discussing this topic, we highlight on error that we find some practitioners make, which is to cluster at the intersection the two groupings. In the preceding example, some might be tempted to cluster the state-year level. A Stata example is to use the command regress y x, vcefclust id_styr) where id_styr is a state-year identifier. This will be very inadequate becaus it imposes the restriction that observations are independent if they are in the same state but in different years. Indeed, if the data is aggregated at the state-year level there is only one observation at the state-year level, so this is identical to using heteroskedastic-robust standard errors —that is, not clustering at all. This point wa highlighted by Bertrand, Duflo, and Mullainathan (2004), which advocated clustering on the state.

A. Multiway Cluster-Robust Variance Matrix Estimate The cluster-robust estimate of V[ß] defined in Equations 10 and 11 can be generalized to clustering in multiple dimensions. In a change of notation, suppress the subscript for cluster and more simply denote the model for an individual observation as (19) y, = x'fi + u, Regular one-way clustering is based on the assumption that E\upj\xp x;J = 0, unles observations i and j are in the same cluster. Then Equation 11 sets B = 1 [ij in same cluster], where ùl = yi -jt'ß. In multiway clustering, the key assumption is that EjiijU xj\ = 0, unless observations i and j share any cluster dimension. The the multiway cluster robust estimate of V[ß] replaces Equation 11 with

## N N

(20) B ='^^xjx'jûfi -\ [/, j share any cluster], /=Iy=l This method relies on asymptotics that are in the number of clusters o with the fewest number of clusters. This method is thus most approp dimension has many clusters. Theory for two-way cluster robust estimates of the variance matrix Cameron, Gelbach, and Miller (2006, 2011), Miglioretti and Heage Thompson (2006,2011). See also empirical panel data applications by Pischke (2003), which clustered at individual level and at regionxtim Petersen (2009), which clustered at firm level and at year level. Cam and Miller (2011) presents an extension to multiway clustering. L cluster-robust, the method can be applied to estimators other than OL For two-way clustering, this robust variance estimator is easy to im software that computes the usual one-way cluster-robust estimate. Fir different cluster-robust "variance" matrices for the estimator by one in, respectively, the first dimension, the second dimension, and by th the first and second dimensions. Then add the first two variance mat count for double-counting, subtract the third. Thus (21) V2way[ß] = V,[ß] + V2[ß] -Vln2[ß], where the three component variance estimates are computed using Equations 10 and 11 for the three different ways of clustering. We spell this out in a step-by-step fashion. (1) Identify your two ways of clustering. Make sure you have a variable that identi fies each way of clustering. Also create a variable that identifies unique "group 1 by group 2" combinations. For example, suppose you have individual-level data spanning many U.S. states and many years, and you want to cluster on state and on year. You will need a variable for state (for example, California), a variable for year (for example, 1990), and a variable for state-by-year (California and 1990). (2) Estimate your model, clustering on "group 1For example, regress y on x, clustering on state. Save the variance matrix as V,. (3) Estimate your model, clustering on "group 2." For example, regress y on x, clustering on year. Save the variance matrix as V2. (4) Estimate your model, clustering on "group 1 by group 2." For example, re gress y on -V, clustering on state-by-year. Save the variance matrix as vln2. (5) Create a new variance matrix V2way = V, + V2 -Vln2. This is your new two way cluster robust variance matrix for ß. (6) Standard errors are the square root of the diagonal elements of this matrix. If you are interested in only one coefficient, you can also just focus on saving the standard error for this coefficient in Steps 2-4 above, and then create se2way = •y/se? + se^ -sejn2. In taking these steps, you should watch out for some potential pitfalls. With per fectly multicollinear regressors such as inclusion of dummy variables — some of which are redundant — a statistical package may automatically drop one or more variables to ensure a nonsingular set of regressors. If the package happens to drop different sets of variables in Steps 2,3, and 4, then the resulting Vs will not be comparable, and adding them together in Step 5 will give a nonsense result. To prevent this issue, manually inspect the estimation results in Steps 2,3, and 4 to ensure that each step has the same set of regressors, the same number of observations, etc. The only things that should be different are the reported standard errors and the reported number of clusters.

B. Implementation Unlike the standard one-way cluster case, V2way[ß] is not guaranteed to be positive semidefinite, so it is possible that it may compute negative variances. In some applica tions with fixed effects, V[ß] may be non positive-definite, but the subcomponent of V[ß] associated with the regressors of interest may be positive-definite. This may lead to an error message, even though inference is appropriate for the parameters of inter est. Our informal observation is that this issue is most likely to arise when clustering is done over the same groups as the fixed effects. Few clusters in one or more dimen sions can also lead to V2way[ß] being a nonpositive-semidefinite matrix. Cameron, Gelbach, and Miller (2011) presents an eigendecomposition technique used in the time series HAC literature that zeroes out negative eigenvalues in V2way[ß] to produce a positive semidefinite variance matrix estimate.

The Stata user-written command cmgreg, available at the authors' websites, imple ments multiway clustering for the OLS estimator with, if needed, the negative eige value adjustment. The Stata add-on command ivreg2, due to Baum, Schaffer, and Sti man (2007), implements two-way clustering for OLS, IV and linear GMM estimation. Other researchers have also posted code, available from searching the Web. Cameron, Gelbach, and Miller (2011) applies the two-way method to data from Hersch (1998) that examines the relationship between individual wages and injury ris measured separately at the industry level and the occupation level. The log-wage for 5,960 individuals is regressed on these two injury risk measures, with standard erro obtained by two-way clustering on 211 industries and 387 occupations. In that cas two-way clustering leads to only a modest change in the standard error of the industr job risk coefficient compared to the standard error with one-way clustering on indu try. Because industry job risk is perfectly correlated within industry, by Result 6 w need to cluster on industry if there is any within-industry error correlation. By similar logic, the additional need to cluster on occupation depends on the within-occupatio correlation of job industry risk, and this correlation need not be high. For the occup tion job risk coefficient, the two-way and one-way cluster (on occupation) standar errors are similar. Despite the modest difference in this example, two-way clusterin avoids the need to report standard errors for one coefficient clustering in one way an for the second coefficient clustering in the second way. Cameron, Gelbach, and Miller (2011) also applies the two-way cluster-robust method to data on volume of trade between 98 countries with 3,262 unique countr pairs. In that case, two-way clustering on each of the countries in the country pa leads to standard errors that are 36 percent larger than one-way clustering and 230 p cent more than heteroskedastic-robust standard errors. Cameron and Miller (2012 studies such dyadic data in further detail. It notes that two-way clustering does not pick up all the potential correlations in the data. Instead, more general cluster-robus methods, including one proposed by Fafchamps and Gubert (2007), should be use

## C. Feasible GLS

Similar to one-way clustering, FGLS is more efficient than OLS, provided an appro priate model for ft = E{uu'\X\ is specified and is consistently estimated.

The random effects model can be extended to multiway clustering. For individual i in clusters g and h, the two-way random effects model specifies yigh = + ag + bh + zigh> where the errors a.g, 8h, and ejgh are each assumed to be iid distributed with mean 0. For example, Moulton (1986) considered clustering due to grouping of regressors (schoo ing, age, and weeks worked) in a log earnings regression, and estimated a model with common random shock for each year of schooling, for each year of age, and for each number of weeks worked. The two-way random effects model can be estimated using standard software for (nested) hierarchical linear models. See, for example, Cameron and Trivedi (2009, Chapter 9.5.7) for Stata commandxtmixed (command mixed from Version 13 on). For estimation of a many-way random effects model, see Davis (2002), which modeled film attendance data clustered by film, theater, and time.

The default standard errors after FGLS estimation require that Q is correctly speci fied. For two-way and multiway random effects models, FGLS estimation entails transforming the data in such a way that there is no obvious method for computing a variance matrix estimate that is robust to misspecification of O. Instead, if there is concern about misspecification of £2, then one needs to consider FGLS with richer models for Q. and assume that these are correctly specified—see Rabe-Hesketh and Skrondal (2012) for richer hierarchical models in Stata—or do less efficient OLS with two-way cluster-robust standard errors.

D. Spatial Correlation Cluster-robust variance matrix estimates are closely related to spatial-robust variance matrix estimates. In general, for Model 19, B in Equation 20 has the form

## N N

(22) B = Y^iU^XtX'jûjùj,;= ij=i where w(i,j) are weights. For cluster-robust inference, these weights are e (cluster in common) or zero (no cluster in common). But the weights can from one to zero, as in the case of the H AC variance matrix estimate for t where w(i, j) decays to zero as \i -j\ increases. For spatial data, it is assumed that model errors become less correlated as t distance between observations grows. For example, with state-level data th tion that model errors are uncorrelated across states may be relaxed to allow tion that decays to zero as the distance between states gets large. Conley ( vides conditions under which Equations 10 and 22 provide a robust varian estimate for the OLS estimator, where the weights w(i, j) decay with the tance. The estimate (which Conley also generalizes to GMM models) is ofte spatial-HAC estimate rather than spatial-robust, as proofs use mixing cond ensure decay of dependence) as observations grow apart in distance. These co are not applicable to clustering due to common shocks, which leads to th robust estimator with independence of observations across clusters. Driscoll and Kraay (1998) considers panel data with T time periods and N als, with errors potentially correlated across individuals (and no spatial da though this correlation across individuals disappears for observations that than m time periods apart. Let it denote the typical observation. The Dris spatial correlation consistent (SCC) variance matrix estimate can be show weight Mit, js) = 1 -d(it, js) / {m + 1) in Equation 22, where the summati over i,j, s, and t, and d(it,js) = \t -sj if \t -s| < m and d(it, js) = 0 otherw method requires that the number of time periods T -> °°, so is not suitable panels while N may be fixed or N The Stata add-on command xtsc Hoechle (2007), implements this variance estimator. An estimator proposed by Thompson (2006) allows for across-cluster (in ample firm) correlation for observations close in time in addition to with correlation at any time separation. The Thompson estimator can be thought o Mit, js) = 1 [i,j share a firm, or d(it,js) < m], Foote (2007) contrasts the cluster-robust and these other variance matrix estimators in the context of a macro economics example. Petersen (2009) contrasts various methods for panel data on fi nancial firms where there is concern about both within firm correlation (over time) and across firm correlation due to common shocks. Barrios et al. (2012) considers state-year panel data on individuals in states over years with state-level treatment and outcome (earnings) that is correlated spatially across states. This spatial correlation can be ignored if the state-level treatment is randomly assigned. But if the treatment is correlated over states (for example, adja cent states may be more likely to have similar minimum wage laws) then one can no longer use standard errors clustered at the state level. Instead, one should additionally allow for spatial correlation of errors across states. The authors additionally contrast traditional model-based inference with randomization inference. In practice, data can have cluster, spatial, and time series aspects, leading to hybrids of cluster-robust, spatial-HAC, and time-series HAC estimators. Furthermore, it may be possible to parameterize some of the error correlation. For example, for a time se ries AR(1) error it may be preferable to use Ebased on an AR(1) model rather than w{t,s)ûtûs. To date, empirical practice has not commonly modeled these combined types of error correlations. This may become more common in the future.

## VI. Few Clusters

We return to one-way clustering and focus on the Wald "/-statistic"

(23) w= ß where ß is one element in the parameter vector ß, and the standard error sg is the square root of the appropriate diagonal entry in Vdu[ß], If G —> °° then w ~ N[0,1] under H0: ß = ß0. For finite G, the distribution of w is unknown even with normal errors. It is common to use the T distribution with G -1 degrees of freedom. It is not unusual for the number of clusters G to be quite small. Despite few clusters, ß may still be a reasonably precise estimate of ß if there are many observations per cluster. But with small G, the asymptotics have not kicked in. Then Vclu[ß] can be downward-biased. One should at a minimum use T(G -1) critical values and Vclu[ß] defined in Equa tions 10 and 11 with residuals scaled by Vc where c is defined in Equation 12 or c = GI (G -1). Most packages rescale the residuals — Stata uses the first choice of c and SAS the second. The use of T(G -1) critical values is less common. Stata uses the T(G -1) distribution after command regress y x, vce(cluster). But the alternative command xtreg y x, vce(robust) instead uses standard normal critical values. Even with both of these adjustments, Wald tests generally overreject. The extent of overrejection depends on both how few clusters there are and the particular data and model used. In some cases the overrejection is mild, in others cases a test with nominal size 0.05 may have true test size of 0.10. The next subsection outlines the basic problem and discusses how few is "few" clusters. The subsequent three subsections present three approaches to finite-cluster correction — bias-corrected variance, bootstrap with asymptotic refinement, and use of the Tdistribution with adjusted degrees-of-freedom. The final subsection considers special cases.

A. The Basic Problems with Few Clusters There are two main problems with few clusters. First, OLS leads to "overfitting," with estimated residuals systematically too close to zero compared to the true error terms. This leads to a downward-biased cluster-robust variance matrix estimate. The second problem is that even with bias-correction the use of fitted residuals to form the esti mate B of B leads to overrejection (and confidence intervals that are too narrow) if the critical values are from the standard normal or even the T(G -1) distribution. For the linear regression model with independent homoskedastic normally distrib uted errors, similar problems are easily controlled. An unbiased variance matrix is obtained by estimating the error variance cr2 by.v2 = uü / (N -K) rather than û'ù / N. This is the "fix" in the OLS setting for the first problem. The analogue to the second problem is that the N[0,1] distribution is a poor approximation to the true distribution of the Wald statistic. In the iid case, the Wald statistic w can be shown to be exactly T(N-K) distributed. For nonnormal homoskedastic errors, the T(N-K) is still felt to provide a good approximation provided N is not too small. Both of these problems arise in the clustered setting albeit with more complicated manifestations and fixes. For independent heteroskedastic normally distributed errors there are no exact results. MacKinnon and White (1985) considers several adjustments to the heteroskedastic - consistent variance estimate of White (1980) including one called HC2 that is unbi ased in the special case that errors are homoskedastic. Unfortunately, if errors are actu ally heteroskedastic, as expected, the HC2 estimate is no longer unbiased for V[ß] — an unbiased estimator depends on the unknown pattern of heteroskedasticity and on the design matrix X. And there is no way to obtain an exact T distribution result for w even if errors are normally distributed. Other proposed solutions for testing and forming confidence intervals include using a T distribution with data-determined degrees of freedom and using a bootstrap with asymptotic refinement. In the following subsections, we consider extensions of these various adjustments to the clustered case where the problems can become even more pronounced. Before proceeding, we note that there is no specific point at which we need to worry about few clusters. Instead, "more is better." Current consensus appears to be that G = 50 is enough for state-year panel data. In particular, Bertrand, Dufio, and Mullainathan (2004, Table 8) finds in its simulations that for a policy dummy variable with high within-cluster correlation, a Wald test based on the standard CRVE with critical value of 1.96 had rejection rates of 0.063,0.058,0.080, and 0.115 for number of states (G) equal to, respectively, 50, 20, 10, and 6. The simulations of Cameron, Gelbach, and Miller (2008, Table 3), based on a quite different data generating process but again with standard CRVE and critical value of 1.96, had rejection rates of 0.068, 0.081,0.118, and 0.208 for G equal to, respectively, 30,20,10, and 5. In both cases, the rejection rates would also exceed 0.05 if the critical value was from the T{G -1) distribution. The preceding results are for balanced clusters. Cameron, Gelbach, and Miller (2008, Table 4, Column 8) considers unbalanced clusters when G -10. The rejection rate with unbalanced clusters, half of size N = 10 and half of size 50, is 0.183, ap preciably worse than rejection rates of 0.126 and 0.115 for balanced clusters of sizes, respectively, 10 and 100. Recent papers by Carter, Schnepel, and Steigerwald (2013) and Imbens and Kolesar (2012) provide theory that also indicates that the effective number of clusters is reduced when N varies across clusters; see also the simulatio?

in MacKinnon and Webb (2013). Similar issues may also arise if the clusters are bal anced, but estimation is by weighted LS that places different weights on different clus ters. Cheng and Hoekstra (2013) documents that weighting can result in overrejection in the panel DiD setting of Bertrand, Duflo, and Mullainathan (2004). To repeat a key message, there is no clear-cut definition of "few." Depending on the situation, "few" may range from less than 20 clusters to less than 50 clusters in the balanced case and even more clusters in the unbalanced case.

B. Solution 1: Bias-Corrected Cluster-Robust Variance Matrix A weakness of the standard CRVE with residual ûg is that it is biased for Vc]u[ß], since E[«g«g] * E[wg«g]-The bias depends on the form of il,, but will usually be downward. Several corrected residuals ùg to use in place of üg in Equation 11 have been proposed. The simplest, already mentioned, is to use üg = yjG / (G -1)h or ûg = Vcm,; where c is defined in Equation 12. One should at least use either of these corrections. Bell and McCaffrey (2002) uses (24) ùg = [INg-Hgg ]-1/2«g, where H = Xg(X'Xy'Xg. This transformed residual leads to unbiased CRVE in the special case that E[«Ä«g] = o-2/. This is a cluster generalization of the HC2 variance estimate of MacKinnon and White (1985), so we refer to it as the CR2VE. Bell and McCaffrey (2002) also uses (25) This transformed residual leads to CRVE that can be shown to equal the delete-one cluster jackknife estimate of the variance of the OLS estimator. This jackknife correc tion leads to upward-biased CRVE if in fact E[ugu'g] = tr2/. This is a cluster general ization of the HC3 variance estimate of MacKinnon and White (1985), so we refer to it as the CR3VE. Angrist and Pischke (2009, Chapter 8) and Cameron, Gelbach, and Miller (2008) provide a more extensive discussion and cite more of the relevant literature. This lit erature includes papers that propose corrections for the more general case that E[ugu'g\ * cr2/ but has a known parameterization, such as an RE model, and extension to generalized linear models. Angrist and Lavy (2002) applies the CR2VE Correction 24 in an application with G = 30 to 40 and finds that the correction increases cluster-robust standard errors by between 10 and 50 percent. Cameron, Gelbach, and Miller (2008, Table 3) finds that the CR3VE Correction 24 has rejection rates of 0.062, 0.070, 0.092, and 0.138 for G equal to, respectively, 30, 20, 10, and 5. These rejection rates are a considerable improvement on 0.068, 0.081, 0.118, and 0.208 for the standard CRVE, but there is still considerable overrejection for very small G. The literature has gravitated to using the CR2VE adjustment rather than the CR3VE adjustment. This reduces but does not eliminate overrejection when there are few clusters.

## C. Solution 2: Cluster Bootstrap with Asymptotic Refinement

In Section IIF, we introduced the bootstrap as it is usually used, to calculate standard errors that rely on regular asymptotic theory. Here, we consider a different use of the bootstrap, one with asymptotic refinement that may lead to improved finite-sample inference.

We consider inference based on G -» °° (formally, >/G((3 -ß) has a limit normal distribution). Then a two-sided Wald test of nominal size 0.05, for example, can be shown to have true size 0.05 + 0(G_1) when the usual asymptotic normal approxima tion is used. For G -* °° this equals the desired 0.05 but for finite G this differs from 0.05. If an appropriate bootstrap with asymptotic refinement is instead used, the true size is 0.05 + 0(G~3/2). This is closer to the desired 0.05 for large G, as G~3/2 < G"1.

Hopefully, this is also the case for small G, something that is established using ap propriate Monte Carlo experiments. For a one-sided test or a nonsymmetric two-sided test the rates are instead, respectively, 0.05 + 0(G~1/2) and 0.05 + Asymptotic refinement can be achieved by bootstrapping a statistic that is asymp totically pivotal, meaning the asymptotic distribution does not depend on any un known parameters. The estimator ß is not asymptotically pivotal as its distribution depends on V[ß], which in turn depends on unknown variance parameters in V[«|X].

The Wald t-statistic defined in Equation 23 is asymptotically pivotal as its asymptotic distribution is /V[0,1], which does not depend on unknown parameters.

1. Percentile-t bootstrap A percentile-? bootstrap obtains B draws, w\,w'B, from the distribution of the Wald f-statistic as follows. B times do the following:

(1) Obtain G clusters {(j>*, A-*),..., (y*G, X'G)} by one of the cluster bootstrap meth ods detailed below.

(2) Compute the OLS estimate ßj in this resample.

(3) Calculate the Wald test statistic w*b = (ß*b -ß) /sg> where Sg* is the cluster-robust standard error of ß*, and ß is the OLS estimate of ß from the original sample.

Note that we center on ß and not ß0, as the bootstrap views the sample as the popula tion, that is, ß = ß, and the B resamples are based on this "population." Note also that the standard error in Step 3 needs to be cluster-robust. A good choice of B is B = 999;

this is more than B for standard error estimation as tests are in the tails of the distribu tion, and is such that (B + l)a is an integer for common choices of test size a.

Let w*,),..., w*B) denote the ordered values of w*,..., wB. These ordered values trace out the density of the Wald t-statistic, taking the place of a standard normal or T dis tribution. For example, the critical values for a 95 percent nonsymmetric confidence interval or a 5 percent nonsymmetric Wald test are the lower 2.5 percentile and upper

## 97.5 percentile of w*,..., w*B rather than, for example, the standard normal values of

-1.96 and 1.96. The p-value for a symmetric test based on the original sample Wald statistic w equals the proportion of times that |wj > Iwl b = 1,..., B.

The simplest cluster resampling method is the pairs cluster resampling introduced in Section IIF. Then in Step 1 above we form G clusters {(>>,*, X*),...,(>>g, X^)} by resampling with replacement G times from the original sample of clusters. This method has the advantage of being applicable to a wide range of estimators, not just OLS. However, for some types of data the pairs cluster bootstrap may not be app cable—see "Bootstrap with Caution" below. Cameron, Gelbach, and Miller (2008) found that in Monte Carlos with few clusters the pairs cluster bootstrap did not eliminate test overrejection. The authors propose using an alternative percentile-/' bootstrap, the wild cluster bootstrap, that holds th regressors fixed across bootstrap replications.

2. Wild cluster bootstrap The wild cluster bootstrap resampling method is as follows. First, estimate the main model, imposing (forcing) the null hypothesis H{) that you wish to test, to give estimate ßHo. For example, for test of statistical significance of a single variable, regress yjg o all components of xig except the variable that has regressor with coefficient zero und the null hypothesis. Form the residual ûig = yt -jc^ßH(]. Then obtain the k'h resampl for Step 1 above as follows: (la) Randomly assign cluster g the weight d = -1 with probability 0.5 and the weight d = 1 with probability 0.5. All observations in cluster g get the same value of the weight.

(lb) Generate new pseudo-residuals ujg = dg x ù!g, and hence new outcome vari ables y*g = 4PHq + uig.

Then proceed with Step 2 as before, regressing y*g on xig, and calculate wh as in Step 3. The p-value for the test based on the original sample Wald statistic w equals th proportion of times that |w| > |w£j, b -1,..., B. For the wild bootstrap, the values w*,..., w*B cannot be used directly to form critical values for a confidence interval. Instead, they can be used to provide ap-value for tes ing a hypothesis. To form a confidence interval, one needs to invert a sequence of test profiling over a range of candidate null hypotheses H0: ß = ß0. For each of these nu hypotheses, obtain the value. The 95 percent confidence interval is the set of valu ofß0for which p > 0.05. This method is computationally intensive but conceptuall straightforward. As a practical matter, you may want to ensure that you have the sam set of bootstrap draws across candidate hypotheses so as to not introduce addition bootstrapping noise into the determination of where the cutoff is. In principle, it is possible to directly use a bootstrap for bias-reduction, such as to remove bias in standard errors. In practice this is not done, however, as in practice an bias reduction comes at the expense of considerably greater variability. A conservativ estimate of the standard error equals the width of a 95 percent confidence interval, obtained using asymptotic refinement, divided by 2 x 1.96. Note that for the wild cluster bootstrap the resamples {(j*, A'1),...,(j>g, A"c)} hav the same X in each resample, whereas for pairs cluster both y* and X* vary across th B resamples. The wild cluster bootstrap is an extension of the wild bootstrap pro posed for heteroskedastic data. Essentially, it works because the two-point distrib tion for forming u ensures that E[«*] = 0 and V[«*] = ügü'. There are other tw point distributions that also do so, but Davidson and Flachaire (2008) shows that in the heteroskedastic case it is best to use the weights d^ = {-1,1}, called Rademache weights.

The wild cluster bootstrap essentially replaces y in each resample with one of two values, y* *Ph„ + « o or (j = XßH o = n o o -« Because this is done across G clusters, there are at most values of w'B.

If bootstrap as we possible data sets

Webb (2013) possible sible 16 rvalues values, 0.0625.

of w* for

Full eration expa statis of exa enum this is of equally plausib issue since 210 =

Webb

## G

by (2013) prop instead posed usin distributi

## {-VT?,

## -VI,

## -V!?,

wild bo

MacKinnon and two-point that, can with overreject wild 3.

even co bootstrap

Bootstrap

## G

w with

Regardless of the finement or wild clusters is to exa should be done w strapping t-statis can take the and variance;

(2) tion strap the

We replications distribution;

detail

First, if sense, the one the then rest for of

Second, few are the the cases case, ables, a you whe then if then r bo you you in ar som can a lead to zero o zero or missing error is reason zero to or m expect errors are zero plus machine precision noise, rather than exactly zero, very large t values may result. Then your bootstrap distribution of f-statistics will have really fat tails and you will not reject anything, even false null hypotheses. No variation or very limited variation in treatment can also result in many of your ß*s being "perfect fit" ß*s with limited variability. Then the bootstrap standard deviation of the ß*s will be too small, and if you use it as your estimated standard error you will overreject. In this case, we suggest using the wild cluster bootstrap. Third, if your pairs cluster bootstrap samples draw nearly multicollinear samples, you can get huge ß*s. This can make a bootstrapped standard error seem very large. You need to determine what in the bootstrap samples "causes" the huge ß*s. If this is some pathological but common draw, then you may need to think about a different type of bootstrap, such as the wild cluster bootstrap, or give up on bootstrapping meth ods. For an extreme example, consider a DiD model with first-order "control" fixed effects and an interaction term. Suppose that a bootstrap sample happens to have among its "treatment group" only observations where "post = 1Then the variables "treated" and "treated*post" are collinear, and an OLS package will drop one of these variables. If it drops the "post" variable, it will report a coefficient on "treated*post"; this coefficient will not be a proper interaction term, but instead also will include the level effect for the treated group. Fourth, with less than ten clusters the wild cluster bootstrap should use the six-point version of Webb (2013). Fifth, in general, if you see missing values in your bootstrapped t-statistics, then you need to figure out why. Don't take your bootstrap results at face value until you know what's going on.

D. Solution 3: Improved Critical Values Using a T-Distribution The simplest small-sample correction for the Wald statistic is to base inference on a T distribution rather than the standard normal, with degrees of freedom at most the number of clusters G. Recent research has proposed methods that lead to using degrees of freedom much less than G, especially if clusters are unbalanced.

1. G-L degrees of freedom Some packages, including Stata after command regress, use G -1 degrees of freedom for r-tests and /"-tests based on cluster-robust standard errors. This choice emanates from the complex survey literature; Bell and McCaffrey (2002) notes, however, that with normal errors this choice still tends to result in test overrejection so the degrees of freedom should be even less than this. Even the T(G -1) can make quite a difference. For example, with G = 10 for a two sided test at level 0.05, the critical value for T(9) is 2.262 rather than 1.960, and if w = 1.960, the p-value based on 7(9) is 0.082 rather than 0.05. In Monte Carlo simulations by Cameron, Gelbach, and Miller (2008), this choice works reasonably well, and at a minimum one should use the T(G -1) distribution rather than the standard normal. For models that include L regressors that are invariant within cluster, Donald and Lang (2007) provides a rationale for using the T(G-L) distribution. If clusters are bal anced and all regressors are invariant within cluster, then the OLS estimator in the model yig -Jtgß + uig is equivalent to OLS estimation in the grouped model yg = x'gß + ug. If ïï is iid normally distributed, then the W^ld statistic is T(G -L) distributed, where V[ß] = j2(ArX')"1 and s2 = (G -L)~12güg. Note that ug is iid normal in the random effects model if the error components are iid normal. Usually, if there is a time-invariant regressor there is only one in addition to the intercept, in which case L-2. Donald and Lang extends this approach to inference on ß in a model that addition ally includes regressors z; that vary within clusters and allow for unbalanced clusters, leading to G-Lfor the Rfe estimator. Wooldridge (2006) presents an expansive expo sition of the Donald and Lang approach. It also proposes an alternative approach based on minimum distance estimation. See Wooldridge (2006) and, for a summary, Cam eron and Miller (2011).

2. Data-determined degrees of freedom For testing the difference between two means of normally and independently distrib uted populations with different variances, the t test is not exactly T distributed. This is known as the Behrens-Fisher problem. Satterthwaite (1946) proposed an approxi mation that was extended to regression with clustered errors in Bell and McCaffrey (2002) and developed further in Imbens and Kolesar (2012). The T(N-k) distribution is the ratio of N[0,1] to independent vlx2(.'V -K)\ / (V -k). For linear regression under iid normal errors, the derivation of the T(N-k) distribution for the Wald f-statistic uses the result that (N -K)(sj / oj) -x2(N ~ K), where is the usual unbiased estimate of a? = V[ß], This resuit no longer holds for non-iid er rors, even if they are normally distributed. Instead, an approximation uses the T(v*) distribution where v* is such that the first two moments of v*(s| / oj) equal the first two moments (v* and 2v*) of the x2(v*) distribution. Assuming s| is unbiased for oj, E[v*(s? / <t|)] = v*. And V[v*(s? / ct?)] = 2v* if v* = 2[(<r?)2 / vfs|]]. Thus, the Wald /-statistic is treated as being T(v*) distributed where v* = 2(cr?)2 / V[s?]. Assumptions are needed to obtain an expression for V[s|]. For clustered errors with u ~ N[0, £2] and using the CRVE defined in Section IIC, or using CR2VE or CR3VE defined in Section VIB, Bell and McCaffrey (2002) shows that the distribution of the Wald /-statistic defined in Equation 23 can be approximated by the T(v*) distribution where (26) and\j are the eigenvalues of the G x G matrix G'ÙG, where £2 is consistent for £2, the N x G matrix G has g'h column (IN -H)'gAgXg(XrX)~xek, (IN -H)g is the Ng x N submatrix for cluster g of the N x N matrix IN -XiX'Xy'X', A = (IN -Hgg)~V2 for CR2VE, and ek is a K x 1 vector of zeroes aside from 1 in the /r position if ß = ßt. Note that v* needs to be calculated separately, and differs, for each regression coeffi cient. The method extends to Wald tests based on scalar linear combinations c'ß. The justification relies on normal errors and knowledge of Cl = E[uu'\X\. Bell and McCaffrey (2002) performs simulations with balanced clusters (G = 20 and Ng = 10) and equicorrelated errors within cluster. It calculates v* assuming £2 = cr2/, even though er rors are in fact clustered, and finds that its method leads to Wald tests with true size closer to the nominal size than tests based on the conventional CRVE, CRV2E, and CRV3E.

Imbens and Kolesar (2012) additionally considers calculating v* where Q is based on equicorrelated errors within cluster. It follows the Monte Carlo designs of Cameron, Gelbach, and Miller (2008), with G = 5 and 10 and equicorrelated errors. It finds that all finite-sample adjustments perform better than using the standard CRVE with T{G -1) critical values. The best methods use the CR2VE and T(v*), with slight overrejec tion with v* based on ft = s2I (Bell and McCaffrey) and slight underrejection with v* based on Ù assuming equicorrelated errors (Imbens and Kolesar). For G = 5, these methods outperform the two-point wild cluster bootstrap as expected given the very low G problem discussed in Section VIC. More surprisingly, these methods also out perform wild cluster bootstrap when G = 10, perhaps because Imbens and Kolesar (2012) may not have imposed the null hypothesis in forming the residuals for this bootstrap.

3. Effective number of clusters Carter, Schnepel, and Steigerwald (2013) proposes a measure of the effective number of clusters. This measure is

## (27) G' = ——,

(1 + 5)' where8 = (1 / G)i^{(ng -Ï)2 / 72},7g = ^k(X'XrlX'pgX^X'X)-iek,ekisiK x 1 vector of zeroes aside from 1 in the k'h position if ß = ßs, and 7 = (1 / G)2^=17g. Note that G* varies with the regression coefficient considered, and the method extends to Wald tests based on scalar linear combinations c'ß. The quantity 8 measures cluster heterogeneity, which disappears if -y = 7 for all g. Given the formula for yg, cluster heterogeneity (8 * 0) can arise for many reasons including variation in N, variation in X, and variation in Qg across clusters. In simu lations using standard normal critical values. Carter et al. (2013) finds that test size distortion occurs for G* < 20. In application, it assumes errors are perfectly correlated within cluster, so £2g = //' where / is an Ng x 1 vector of ones. For data from the Ten nessee STAR experiment, it finds G* = 192 when G = 318. For the Hersch (1998) data of Section IIB, with very unbalanced clusters, it finds for the industry job risk coeffi cient and with clustering on industry that G* = 19 when G = 211. Carter et al. (2013) does not actually propose using critical values based on the T(G*) distribution. The key component in obtaining the formula for v* in the Bell and McCaffrey (2002) approach is determining V[s| / cr|], which equals E[(s? -oj) / oj] given s| is unbiased for oj. Carter et al. (2013) instead works with E[(î? -cr|) / oj] where s|, de fined in this paper, is an approximation to s| that is good for large G (formally / aj -> s| / cr| asG —> °°).NowE[(5? -cr?) / cr?|= 2(1 + 8) / G, see Carter et al. (2013), where 8 is defined in Equation 27. This suggests using the T{G*) distribution as an approximation and that this approximation will improve as G increases.

E. Special Cases With few clusters, additional results can be obtained if there are many observations in each group. In DiD studies, the few-clusters problem arises if few groups are treated, even if G is large. And the few-clusters problem is more likely to arise if there is multiway clustering.

1. Fixed number of clusters with cluster size growing The preceding adjustments to the degrees of freedom of the T distribution are based on the assumption of normal errors. In some settings, asymptotic results can be obtained when G is small, provided Ng —> °°. Bester, Conley, and Hansen (2011), building on Hansen (2007a), gives conditions under which the Mest statistic based on Equation 11 is -JG / (G -1) times TC{dis tributed. Then using iig = JG / (G -\)ûg in Equation 11 yields a T(G -1) distributed statistic. In addition to assuming G is fixed while Ng —> °°, it is assumed that the within group correlation satisfies a mixing condition (this does not happen in all data settings, although it does for time series and spatial correlation), and that homogeneity assumptions are satisfied, including equality of plim (1 /Ng)X'gXg for all g. Let ß,r denote the estimate of parameter ß in cluster g, ß = G~'2®=1|Jg denote the average of the G estimates, and = (G -l)2^=1(ßg -ß)2 denote their variance. Sup pose that the ßg are asymptotically normal as N —» °° with common mean ß, and consider test of H0: ß = ß0 based on t = VG(ßg -ß0) /. Then Ibragimov and Mül ler (2010) shows that tests based on the T{G -1) distribution will be conservative tests (that is, underreject) for level a < 0.083. This approach permits correct inference even with extremely few clusters, assuming N is large. However, the requirement that clus ter estimates are asymptotically independent must be met. Thus, the method is not directly applicable to a state-year DiD application when there are year fixed effects (or other regressor that varies over time but not states). In that case, Ibragimov and Müller proposes applying its method after aggregating subsets of states into groups in which some states are treated and some are not.

2. Few treated groups Problems arise if most of the variation in the regressor is concentrated in just a few clusters, even when G is sufficiently large. This occurs if the key regressor is a cluster-specific binary treatment dummy and there are few treated groups. Conley and Taber (2011) examines a differences-in-differences (DiD) model in which there are few treated groups and an increasing number of control groups. If there are group-time random effects, then the DiD model is inconsistent because the treated groups random effects are not averaged away. If the random effects are nor mally distributed, then the model of Donald and Lang (2007) applies and inference can use a T distribution based on the number of treated groups. If the group-time shocks are not random, then the T distribution may be a poor approximation. Conley and Taber (2011) then proposes a novel method that uses the distribution of the untreated groups to perform inference on the treatment parameter. Abadie, Diamond, and Hainmueller (2010) proposes synthetic control methods that provide a data-driven method to select the control group in a DiD study and that provide inference under random permutations of assignment to treated and untreated groups. The methods are suitable for treatment that affects few observational units.

3. What if you have multiway clustering and few clusters? Sometimes we are worried about multiway clustering but one or both of the way has few clusters. Currently, we are not aware of an ideal approach to deal with th problem. One potential solution is to try to add sufficient control variables so as minimize concerns about clustering in one of the ways, and then use a one-way few clusters cluster robust approach on the other way. Another potential solution is t model one of the ways of clustering in a parametric way, such as with a common shoc or an autoregressive error model. Then you can construct a variance estimator that is hybrid of the parametric model and cluster robust in the remaining dimension.

## VII. Extensions

The preceding material has focused on the OLS (and FGLS) estimator and tests on a single coefficient. The basic results generalize to multiple hypothesis tests, instrumental variables (IV) estimation, nonlinear estimators, and generalized method of moments (GMM). These extensions are incorporated in Stata though Stata generally computes test p values and confidence intervals using standard normal and chi-squared distributions rather than T and F distributions. And for nonlinear models, stronger assumptions are needed to ensure that the estimator of ß retains its consistency in the presence of clustering. We provide a brief overview.

A. Cluster-Robust F-tests Consider Wald joint tests of several restrictions on the regression parameters. Except in the special case of linear restrictions and OLS with iid normal errors, asymptotic theory yields only a chi-squared distributed statistic, such as W, that is \2(h) distrib uted where h is the number of (linearly independent) restrictions. Alternatively, we can use the related F statistic, F=W //i. This yields the same p-value as the chi-squared test if we treat F as being F {h, °°) distributed. In the cluster case, a finite-sample adjustment instead treats F as being F(h, G -1) distributed. This is analo gous to using the T(G -1) distribution rather than N[0,1] for a test on a single coefficient. In Stata, the finite-sample adjustment of using the T(G -1) for a Mest on a single coefficient, and using the F(h,G -1) for an F-test, is only done after OLS regression with command regress. Otherwise, Stata reports critical values and p-values based on the N[0,l] and x2W distributions. Thus, Stata does no finite-cluster correction for tests and confidence intervals fol lowing instrumental variables estimation commands, nonlinear model estimation com mands, or even after command regress in the case of tests and confidence intervals us ing commands testnl and nlcom. The discussion in Section VI was limited to inference after OLS regression, but it seems reasonable to believe that for other estimators one should also base inference on the T(G -1) and F(h,G -1) distributions, and even then tests may overreject when there are few clusters. Some of the few-cluster methods of Section VI can be extended to tests of more than one restriction following OLS regression. The Wald test can be based on the bias adjusted variance matrices CR2VE or CR3VE, rather than CRVE. For a bootstrap with asymptotic refinement of a Wald test of H0: Äß = r, in the b'h resample we compute fVö' = (Rß'b -Äß)'[ÄVdu[ßj]Ä']_,(Äßj -Äß). Extension of the data-determined de grees of freedom method of Section VID to tests of more than one restriction requires, at a minimum, extension of Theorem 4 of Bell and McCaffrey (2002) from the case that covers ß, where ß is a single component of ß, to Äß An alternative ad hoc ap proach would be to use the F(h,v*) distribution where v* is an average (possibly weighted by estimator precision) of v* defined in Equation 26 computed separately for each exclusion restriction. For the estimators discussed in the remainder of Section VII, the rank of Vclu[ß] is again the minimum of G -1 and the number of parameters (K). This means that at most G -1 restrictions can be tested using a Wald test, in addition to the usual require ment that h < K.

B. Instrumental Variables Estimators The cluster-robust variance matrix estimate for the OLS estimator extends naturally to the IV estimator, the two-stage least squares (2SLS) estimator, and the linear GMM estimator. The following additional adjustments must be made when errors are clustered. First, a modified version of the Hausman test of endogeneity needs to be used. Second, the usual inference methods when instruments are weak need to be adjusted. Third, tests of overidentifying restrictions after GMM need to be based on an optimal weighting matrix that controls for cluster correlation of the errors.

1. IV and 2SLS In matrix notation, the OLS estimator in the model y = Xß + u is inconsistent if E[«|A"] * 0. We assume existence of a set of instruments Z that satisfy E[«|Z] = 0 and satisfy other conditions, notably Z is of full rank with dim[Z] > dim[A] and Cor[Z, X] * 0. For the clustered case, the assumption that errors in different clusters are uncorre cted is now one of uncorrected errors conditional on the instruments Z, rather than uncorrected errors conditional on the regressors X. In the g'h cluster the matrix of in struments Zg is an Ng x M matrix, where M > K, and we assume that E[«g|Zg] = 0 and Co\[ugu'h\Zg, Zh\ = 0 for g * h. In the just-identified case, with Z and X having the same dimension, the IV estima tor is ßIV = (Z'Xf'Zy, and the cluster-robust variance matrix estimate is

## (G

(28) VtJß[v] = (Z'X) ri

ÏWi (X'zy where üg = yg -A^,ßlv are residuals calculated using the consiste again assume G -> °°. As for OLS, the CRVE may be rank-defic minimum of K and G -1. In the overidentified case with Z having dimension greater than X, the 2SLS estimator is the special case of the linear GMM estimator in Equation 29 below with W = (Z'Z)~\ and the CRVE is that in Equation 30 below with W = (Z'Z)-1 and the 2SLS resid als. In the just-identified case, 2SLS is equivalent to IV. A test for endogeneity of a regressor(s) can be conducted by comparing the OL estimator to the 2SLS (or IV) estimator that controls for this endogeneity. The tw estimators have the same probability limit given exogeneity and different probabilit limits given endogeneity. This is a classic setting for the Hausman test but, as in th Hausman test for fixed effects discussed in Section HID, the standard version of the Hausman test cannot be used when errors are clustered. Instead let X = [X{X2\ where Xx is potentially endogenous and X2 is exogenous, and let vig denote the residu als from first-stage OLS regression of the endogenous regressors on instruments an exogenous regressors. Then estimate by OLS the model y,g = *i'/gßi + *2/gß2 + t'ugy + "ig The regressors jc(are considered endogenous if we reject H0: y = 0 using a Wald tes based on a CRVE. In Stata, this is implemented using command estât endogenous (Alternatively, a pairs cluster bootstrap can be used to estimate the variance o ß2SLS ~ ßoLs) 2. Weak instruments When endogenous regressor(s) are weakly correlated with instrument(s), after partial ling out the exogenous regressors in the model, there is great loss of precision. Then the standard error for the coefficient of the endogenous regressor is much higher after IV or 2SLS estimation than after OLS estimation. Additionally, asymptotic theory takes an unusually long time to kick in so that even with large samples the IV estimator can still have considerable bias and the Wald statistic is still not close to normally distributed. See, for example, Bound, Jaeger, and Baker (1995), Andrews and Stock (2007), and textbook discussions in Cameron and Trivedi (2005,2009). For this second consequence, called the "weak instrument" problem, the economet rics literature has focused on providing theory and guidance in the case of homoskedas tic errors. Not all of the proposed methods extend to errors that are correlated within cluster. And the problem may even be greater in the clustered case, as the asymptotics are then in G -> <*> rather than N -> °°, though we are unaware of evidence on this. We begin with a case of a single endogenous regressor. A standard diagnostic for detecting weak instruments is to estimate by OLS the first-stage regression of the endogenous regressor on the exogenous regressors and the additional instrument(s). Then calculate the /^-statistic for the joint significance of the instruments; in the case of a just-identified model there is only one instrument to test so the /-"-statistic is the square of the /-statistic. With clustered errors, this F-statistic needs to be based on a cluster-robust variance matrix estimate. It is common practice to interpret the cluster-robust F-statistic in the same way as when errors are iid, using the tables of Stock and Yogo (2005) or the popular rule-of-thumb, due to Staiger and Stock (1997), that there may be a weak instrument problem if F < 10. But it should be noted that these diagnostics for weak instruments were developed for the simpler case of iid er rors. Note also that the first-stage cluster-robust F-statistic can only be computed if the number of instruments is less than the number of clusters.

With more than one endogenous variable and iid errors, the /-"-statistic generalizes to the Cragg-Donald minimum eigenvalue statistic, and one can again use the tables of Stock and Yogo (2005). For clustered errors generalizations of the Cragg-Donald minimum eigenvalue statistic have been proposed, see Kleibergen and Paap (2008), but it is again not clear whether these statistics can be compared to the Stock and Yogo tables when errors are clustered. Now consider statistical inference that is valid even if instruments are weak, again beginning with the case of a single endogenous regressor. Among the several testing methods that have been proposed given iid errors, the Anderson-Rubin method can be generalized to the setting of clustered errors. Consider the model yig = ßxjg + ujg, where the regressor x is endogenous and the first-stage equation is xjg = z'g~n + vig. (If there are additional exogenous regressors x2, as is usually the case, the method still works if the variables y, x, and z are defined after partialling out xr) The two equations imply that yig -fi*xIg = ^«(ß -ß") + wig, where wig = uig + vig(ß -ß*). So a test of ß = ß* is equivalent to a Wald test of 7 = 0 in the model yig -ß*xig = z'gy + wig. With clustered errors, the test is based on cluster-robust standard errors. Additionally, a weak instrument 95 percent confidence interval for ß can be con structed by regressing yig -ß*xjg on zig for a range of values of ß* and including in the confidence interval for ß only those values of ß* for which we did not reject H0: y = 0 when testing at 5 percent. As in the iid case, this can yield confidence intervals that are unbounded or empty, and the method loses power when the model is overidentified. When there is more than one endogenous regressor, this method can also be used, but it can only perform a joint F-test on the coefficients of all endogenous regressors rather than separate tests for each of the endogenous regressors. Chernozhukov and Hansen (2008) provides a simple presentation of the method and an empirical example. Finlay and Magnusson (2009) provides this and other extensions, and provides a command ivtest for Stata. We speculate that if addition ally there are few clusters, then some of the adjustments discussed in Section VI would help. Baum, Schaffer, and Stillman (2007) provides a comprehensive discussion of vari ous methods for IV, 2SLS, limited information maximum likelihood (LIML), k-c\ass, continuous updating, and GMM estimation in linear models, and present methods using their ivreg2 Stata command. They include weak instruments methods for errors that are iid, heteroskedastic, or within-cluster correlated errors.

3. Linear GMM For overidentified models, the linear GMM estimator is more efficient than the 2SLS estimator if E[uu'\Z] i=-cr2/. Then (29) Pgmm = (X'ZWÏX)-\X'ZWZ'y), where W is a full rank K x K weighting matrix. The CRVE for GMM is f G \ (30) vclu[ßGMM] = (x'zwz'xyx'zw

## SWA

## WZ'X{X'ZWZ'X)-\

vs=1 where « are residuals calculated using the GMM estimator.

For clustered errors, the efficient two-step GMM estimator uses W = (2® lZ'gûgû'gZg)~\ where ûg are 2SLS residuals. Implementation of this estimator requires that the num ber of clusters exceeds the number of instruments as otherwise 2^=1Z'm m'Z is no

## O

## O

## O

## O

## Ö

invertible.

Here

## Z

contai and the additional instrum gressors.

When this con poses doing two-step

## GMM

dent variable y, the endo additional instruments th

The overidentifying res is a limited test of i struments than necessary following the cluster ver (1998).

test,

Just as

## GLS

lead to more moment is more eff efficient es condition moment

## E[«|Z]

condition

## E[Z

where

## Ù

is consistent fo specification of

## D,

simila ments to

## GMM

are seldom exception is

Shore-Shepp instruments and groupreason may be that this special case of a random e a pairs cluster bootstrap

## C. Nonlinear Models

For nonlinear models, there are several ways to handle clustering. We provide a brief summary; see Cameron and Miller (2011) for further details.

For concreteness, we focus on logit regression. Recall that in the cross-section case y. takes value 0 or 1 and the logit model specifies that E[_v,|*;] = Pr[yt = 1 |jc;] = ).

where A (z) = ez / (1 + e~).

1. Different models for clustering The simplest approach is a pooled approach that assumes that clustering does not change the functional form for the conditional probability of a single observation. Thus, for the logit model, whatever the nature of clustering, it is assumed that (31) E[>g*Ij?] = Pr [yig = l|*,g] = A(^ß). This is called a population-averaged approach, as A(jc^ß) is obtained after averaging out any within-cluster correlation. Inference needs to control for within-cluster cor relation, however, and more efficient estimation may be possible. The generalized estimating equations (GEE) approach, due to Liang and Zeger (1986) and widely used in biostatistics, introduces within-cluster correlation into the class of generalized linear models (GLM), a class that includes the logit model. One possible model for within-cluster correlation is equicorrelation, with Cori^, yj|xig, xjg] = p. The Stata command xtgee y x, family (binomial) link(logit) corr(exchangeable) estimates the population-averaged logit model and provides the CRVE assuming the equicorrelation model for within-cluster correlation is correctly specified. The option vce(robust) provides a CRVE that is robust to misspecification of the model for within-cluster correlation. Command xtgee includes a range of mod els for the within-error correlation. The method is a nonlinear analog of FGLS given in Section IID, and asymptotic theory requires G —> A further extension is nonlinear GMM. For example, with endogenous regressors and instruments z that satisfy E[yig -exp(jt'!;ß)|zw] = 0, a nonlinear GMM estimator minimizes Ä(ß)'W/A(ß) where A(ß) = lg2:zig(yig -expfx'^ß)). Other choices of A(ß) that allow for intracluster correlation may lead to more efficient estimation, analogous to the linear GMM example discussed at the end of Section VIIB. Given a choice of A(ß), the two-step nonlinear GMM estimator at the second step uses weighting matrix W that is the inverse of a consistent estimator of V[A(ß)], and one can then use the minimized objection function for an overidentifying restrictions test. Now suppose we consider a random effects logit model with normally distributed random effect, so (32) Pr[^ig = l|ag,x;g] = A(ag + x^ß), where ag ~ /V[0, orj]. If ag is known, the Ng observations in cluster g are independent with joint density

Ng f(y>g>~,yNggKxg) = nAK + 4^ -AK + x'<M~y,g i= 1 Since ag is unknown it is integrated out, leading to joint density

## I

## V'='

( =

Ng \

## J

## IF«,

where h(ag\<j2J is the 7V[0, <r^] density. There is no closed form solution for this inte gral, but it is only one-dimensional so numerical approximation (such as Gaussian quadrature) can be used. The consequent MLE can be obtained in Stata using the command xtlogit y x, re. Note that in this RE logit model Equation 31 no longer holds, so ß in the Model 32 is scaled differently from ß in Equation 31. Furthermore, ß in Equation 32 is inconsistent if the distribution for ag is misspecified, so there is little point in using option vce(robust) after command xtlogit, re. It is important to realize that in nonlinear models such as logit, the population averaged and random effects approaches lead to quite different estimates of ß that are not comparable since ß means different things in the different models. The resulting estimated average marginal effects may be similar, however, just as they are in stan dard cross-section logit and probit models. With few clusters, Wald statistics are likely to overreject as in the linear case, even if we scale the CRVE's given in this section by G / (G -1) as is typically done; see Equation 12 for the linear case. McCaffrey, Bell, and Botts (2001) considers bias correction of the CRVE in generalized linear models. Asymptotic refinement using a + x'i pairs cluster bootstrap as in Section VIC is possible. The wild bootstrap given in Sec tion VID is no longer possible in a nonlinear model, aside from nonlinear least squares, as it requires additively separable errors. Instead, one can use the score wild bootstrap proposed by Klein and Santos (2012) for nonlinear models, including maximum like lihood and GMM models. The idea in this paper is to estimate the model once, gener ate scores for all observations, and then perform a bootstrap in the wild-cluster style, perturbing the scores by bootstrap weights at each step. For each bootstrap replication, the perturbed scores are used to build a test statistic, and the resulting distribution of this test statistic can be used for inference. It finds that this method performs well in small samples and can greatly ease computational burden because the nonlinear model need only be estimated once. The conservative test of Ibragimov and Müller (2010) can be used if N —> 2. Fixed effects A cluster-specific fixed effects version of the logit model treats the unobserved param eter ag in Equation 32 as being correlated with the regressors xig. In that case, both the population-averaged and random effects logit estimators are inconsistent for ß. Instead, we need a fixed effects logit estimator. In general, there is an incidental parameters problem if asymptotics are that N is fixed while G —> °°, as there are only Ng observations for each ag, and inconsistent estimation of ag spills over to inconsis tent estimation of ß. Remarkably for the logit model it is nonetheless possible to con sistently estimate ß. The logit fixed effects estimator is obtained in Stata using the command xtlogit y x, fe. Note, however, that the marginal effect in Model 32 is 5PrL>',£ = llv*«]/ = A(as + ~ A(a« + *,*ß))ß*-Unlike the linear FE model, this depends on the unknown ag. So the marginal effects cannot be computed though the ratio of the marginal effects of the klhand l'h regressor equals / ß,, which can be consistently estimated. The logit model is one of few nonlinear models for which fixed effects estima tion is possible when Ng is small. The other models are Poisson with E[yjg\Xg, ag] = exp(ap + x'„ß), and nonlinear models with E[v |AT, a„] = a„ + m(x'.ß), where m() is a o o o o o o o s

The inclu estim son r estim sever for s g

Yoon and

Galvao with correlation the number of in

## D.

Cluster-Rando

Increasingly, rese laboratory experi to account for the clustered nature of the data. And so when designing these experi ments, they should also account for clustering. Fitzsimons et al. (2012) uses a wild cluster bootstrap in an experiment with 12 treated and 12 control clusters. Traditional guidance for computing power analyses and minimum detectable effects (see Duflo, Glennerster, and Kremer 2007, pp. 3918-22; Hemming and Marsh 2013) are based on assumptions of either independent errors or, in a clustered setting, a ran dom effects common-shock model. Ideally, one would account for more general forms of clustering in these calculations (the types of clustering that motivate cluster-robust variance estimation), but this can be difficult to do ex ante. If you have a data set that is similar to the one you will be analyzing later, then you can assign a placebo treat ment and compute the ratio of cluster-robust standard errors to default standard errors. This can provide a sense of how to adjust the traditional measures used in design of experiments.

## VIII. Empirical Example

In this section, we illustrate the most common applications of cluster robust inference. There are two examples. The first is a Moulton-type setting that uses individual-level cross section data with clustering on state. The second is the Bertrand et al. (2004) example of DiD in a state-year panel with clustering on state and poten tially with state fixed effects. The microdata are from the March CPS, downloaded from IPUMS-CPS (King et al. 2010). We use data covering individuals who worked 40 or more weeks during the prior year and whose usual hours per week in that year was 30 or more. The hourly wage is constructed as annual earnings divided by annual hours (usual hours per week times number of weeks worked), deflated to real 1999 dollars, and observations with real wage in the range ($2, $100) are kept. The cross-section example uses individual-level data for 2012. The panel example uses data aggregated to the state-year level for 1977 to 2012. In both cases, we esti mate log-wage regressions and perform inference on a generated regressor that has zero coefficient. Specifically, we test H0: ß = 0 using w = ß / For each example, we present results for a single data set before presenting a Monte Carlo experiment that focuses on inference when there are few clusters. We contrast various ways to compute standard errors and perform Wald tests. Even when using a single statistical package, different ways to estimate the same model may lead to different empirical results due to calculation of different degrees of freedom, especially in models with fixed effects, and due to uses of different distributions in computingp-values and critical values. To make this dependence clear, we provide the particular Stata command used to obtain the results given below; similar issues arise if alternative statistical packages are employed. The data and accompanying Stata code (Version 13) are available at our websites.

A. Individual-Level Cross-Section Data: One Sample In our first application, we use data on 65,685 individuals from the year 2012. The model is

Table 1

Cross-section individual level data Impacts of Clustering and Estimator Choices on Estimated Coefficients and

Standard Errors

Estimation Method OLS OLS FGLS FGLS

## (RE)

## (RE)

0.0108 0.0314

Slope

Slope coefficient coefficient 0.0108 0.0314

Standard

Standard errors errors

Default

Default 0.0042

## 0.0042 0.0199

0.0199

Heteroscedastic

Heteroscedastic robust robust

## 0.0042 0.0042 —

## 0.0229 0.0229 0.0214

0.0214

Cluster

Cluster robust robust (cluster on (cluster state) on state) 0.0216

Pairs

Pairs cluster cluster bootstrap bootstrap 0.0224

## 0.0224 0.0216

Number observations

Number observations 65,685 65,685 65,685 65,685 51 51 •

Number

Number clusters (states) clusters (states) 51 51 to 5, to 519 5,866 to 5,866

Cluster

Cluster size range size range 519 to 519 5,866

Intraclass

Intraclass correlation correlation 0.018 0.018 — Notes: March 2012 CPS data, from 1PUMS download. Default standard errors for OLS assume errors are iid; default standard errors for FGLS assume the random effects model is correctly specified. The bootstrap uses 399 replications. A fixed effect model is not possible because the regressor is invariant within states.

(33) yig = £dg + z;gy + uig, where y is log-wage, dg is a randomly generated dummy "policy" variable equal to one for one-half of the states and zero for the other half, and zig is a set of individual level controls (age, age squared, and education in years). Estimation is by OLS and by FGLS controlling for state-level random effects. The policy variable d is often referred to as a "placebo" treatment and should be statistically significant in only 5 percent of tests performed at significance level 0.05. Table 1 reports the estimated coefficient of the policy variable, along with its stan dard error computed in several different ways, when there are 51 clusters (states). OLS results given in the first column of Table 1 are obtained using Stata command regress. The default standard error is misleadingly small (se = 0.0042), leading to the dummy variable being very highly statistically significant (t = -0.0226 / 0.0042 = -5.42) even though it was randomly generated independently of log-wage. The White heteroskedastic-robust standard error, from regress option vce(robust), is similar in magnitude. From Section IVA, White standard errors should not be used if N is small but here Ng is large. The cluster-robust standard error (se -0.0229) using op tion vce(cluster state) is 5.5 times larger and leads to the more sensible result that the regressor is statistically insignificant (t --0.99). In results not presented in Table 1, the cluster-robust standard errors of the other regressors —age, age squared, and edu cation—were, respectively, 1.2,1.2, and 2.3 times the default. So ignoring clustering again understates the standard errors. As expected, a pairs cluster bootstrap (with out asymptotic refinement) using option vce(boot, cluster(state)), yields very similar cluster-robust standard error. Note that Formula 6 suggests that the cluster-robust standard errors are 4.9 times the default (V1 + (1 x 0.018 x (65685 / 51 -1) = 4.9), close to the observed multiple of 5.5. Formula 6 may work especially well in this example as taking the natural loga rithm of wage leads to model error that is close to homoskedastic and equicorrelation is a good error model for individuals clustered in regions. FGLS estimates for a random effects model with error process defined in Equation 16 are given in the second column of Table 1. These were obtained using command xtreg, re after xtset state. The cluster-robust standard error defined in Equation 15 and computed using option vce(robust) is 0.0214/0.0199 = 1.08 times larger than the de fault. The pairs cluster bootstrap, implemented using option vce(boot), yields a similar cluster-robust standard error. In principle, FGLS can be more efficient than OLS. In this example, there is a mod est gain in efficiency with the cluster-robust standard error equal to 0.0214 for FGLS compared to 0.0229 for OLS. Finally, to illustrate the potential pitfalls of pairs cluster bootstrapping for stan dard errors when there are few clusters, discussed in Section VIC, we examine a modification with only six states broken into treated (AZ, LA, MD) and control (DE, PA, UT). For these six states, we estimate a model similar to that in Table 1. Then ß = 0.0373 with default se = 0.0128. We then perform a pairs cluster boot strap with 999 replications. The bootstrap se -0.0622 is similar to the cluster-robust se = 0.0577. However, several problems arise. First, 28 replications cannot be esti mated, presumably due to no variation in treatment in the bootstrap samples. Sec ond, a kernel density estimate of the bootstrapped ß.v reveals that their distribution is very multimodal and has limited density near the middle of the distribution. Considering these results, we would not feel comfortable using the pairs cluster bootstrap in this data set with these few clusters. Better to base inference on a wild cluster bootstrap. This example highlights the need to use cluster-robust standard errors even when model errors are only weakly correlated within cluster (the intraclass correlation of the residuals in this application is 0.018), if the regressor is substantially correlated within cluster (here perfectly correlated within cluster), and/or cluster sizes are large (ranging here from 519 to 5,866).

B. Individual-Level Cross-Section Data: Monte Carlo We next perform a Monte Carlo exercise to investigate the performance of various cluster-robust methods as the number of clusters becomes small. The analysis is based on the same cross-section regression as in the previous subsection. In each replication, we generate a data set by sampling (with replacement) states and all their associated observations. For quicker computation of the Monte Carlo simulation, within each state we use only a 20 percent subsample of individuals, so there are on average approximately 260 observations per cluster. We explore the effect of the number of clusters G by performing varying simula tions with G equal to 6,10,20,30, or 50. Given a sample of states, we assign a dummy "policy" variable to one-half of the states. We run OLS regressions of log-wage on th policy variable and the same controls as used for the Table 1 regressions.

In these simulations, we perform tests of the null hypothesis that the slope coe ficient of the policy variable is zero. Table 2 presents rejection rates that with million of replications should equal 0.05, since we are testing a true hypothesis at a nominal percent level. For G = 6 and 10, we perform 4,000 simulations, so we expect that 9 percent of these simulations will yield estimated test size in the range (0.043,0.057) i the true test size is 0.05. For larger G, there are 1,000 simulations and the 95 percen simulation interval is instead (0.036,0.064).

We begin with lengthy discussion of the many clusters case. These results are given in the final column (G = 50) of Table 2. Rows 1-9 report sizes for Wald tests based on t = ß / se where se is computed in various ways while Rows 10-15 report sizes fo tests using various bootstraps with an asymptotic refinement. Basic Stata commands yield the standard errors in Rows 1-4 and 9, while the remaining rows require add tional coding.

Row 1 presents the size of tests using heteroskedastic-robust standard errors, ob tained using Stata command regress, vce(robust). Ignoring clustering leads to great overrejection due to considerable underestimation of the standard error. Using Formula 6 for this 20 percent subsample yields a standard error inflation factor of yj1 + (1 x 0.018 x (0.20 x 65685 / 51 -1) = 2.38.So / = 1.96 using the heteroskedastic - robust standard error is really / = 1.96 / 2.38 = 0.82. And using standard normal critical values, an apparent p = 0.05 is really p = 0.41 since Pr[lzl > 0.82] = 0.41. This crude approximation is fairly close to p = 0.498 obtained in this simulation.

Results using cluster-robust standard errors, presented in Rows 2-4 and obtained from regress, vce(cluster state), show that even with 50 clusters the choice of distribu tion to use in obtaining critical value makes a difference. The rejection rate is closer to

## 0.05 when T(G -1) critical values are used than when /V[0,1] critical values are used.

Using T{G -2) in Row 4, suggested by the study of Donald and Lang (2007), leads to slight further improvement, but there is still overrejection.

Results using the bias adjustments CR2 and CR3 discussed in Section VIB, along with T(G -1) critical values, are presented in Rows 5-6. Bias adjustment leads to further decrease in the rejection rates, toward the desired 0.05.

Rows 7 and 8 use critical values from the T distribution with the data-determined degrees-of-freedom of Section VID, equal to 17 on average when G = 50 (see Rows 14 and 17). This leads to further improvement in the Monte Carlo rejection rate.

Bootstrap standard errors obtained from a standard pairs cluster bootstrap, imple mented using command regress, vcefboot, clusterfstate)) are used in Row 9. For G = 50, the rejection rate is essentially the same as that in Row 3, as expected since this bootstrap has no asymptotic refinement.

Rows 10-15 implement the various percentile-/ bootstraps with asymptotic refine ment presented in Section VIC. Only 399 bootstraps are used here as any consequent bootstrap simulation error averages out over the many Monte Carlo replications. But if these bootstraps were used just once, as in an empirical study, a percentile-/ boot strap should use at least 999 replications. Row 10 can be computed using the boot strap: command, see our posted code, while Rows 11-15 require additional coding.

For G = 50, the various bootstraps give similar results with rejection rates of a bit more than 0.06.

Rows 16-19 give the effective number of clusters. The Imbens and Kolesar (2013) measure v* in Equation 26, denoted IK, and the Carter, Schnepel, and Steigerwald (2013) measure G* in Equation 27, denoted CSS, are both equal to 17 on average when G = 50. For the IK measure, across the 1,000 simulations the 5th percentile is 9.6 and the 95th percentile is 29.5.

We next examine settings with fewer clusters than G = 50. Then most methods lead to rejection rates even further away from the nominal test size of 0.05.

Consider the case G-6. Rows 2-4 and 8 compute the same Wald test statistic but use different degrees of freedom in computing p-values. This makes an enormous difference when G is small, as the critical value for a Wald test at level 0.05 rises from

## 2.571 to 2.776 and 3.182 for, respectively, the T(5), 7T4), and 7Ï3) distributions, and

from Row 16 the IK degrees of freedom averages 3.3 across the simulations. The CSS degrees of freedom is larger than the IK as, from Section VID, it involves an approxi mation that only disappears as G becomes large.

Using a bias-corrected CRVE also makes a big difference. It appears from Rows 6 and 7 that it is best to use the CR3 bias-correction with T(G -1) critical values, and the CR2 bias-correction with 7Tv*) critical values where v* is the Imbens and Kolesar (2013) calculated degrees of freedom.

A downside to using cluster-robust standard errors is that they provide an estimate of the standard deviation of ß that is more variable than the default or heteroskedastic robust standard errors. This introduces a potential bias — variance tradeoff. To see whether this increased variability is an issue, we performed 1,000 Monte Carlo repli cations using the full cross-section microdata set, resampling the 50 states with re placement. The standard deviation of the cluster-robust standard error across the 1,000 replications equaled 12.3 percent of the mean cluster-robust standard error, while the standard deviation of the heteroskedastic-robust standard error equaled 4.5 percent of its mean. So while the CRVE is less biased than heteroskedastic-robust (or default), it is also more variable. But the increased variability is relatively small, especially com pared to the very large bias that can arise if clustering is not controlled for.

Rows 10-15 present various bootstraps with asymptotic refinement. From Row 10, the pairs cluster bootstrap performs extremely poorly for G < 10.

Results for the wild cluster bootstrap using a Rademacher 2 point distribution are pre sented in Rows 11-13. From Section VIB, this bootstrap yields only 26 = 64 possible data sets when G = 6, and hence at most 64 unique values for w*. This leads to indeterminacy for the testp-value. Suppose thep-value is in the range [a,b]. Then H0 is rejected in Row 11 ifa<0.05,inRow 12if(a+b)/2<0.05,and in Row 13 if b < 0.05. The indeterminacy leads to substantially different results for G as low as six, though not for G > 10.

The wild cluster bootstrap using the Webb 6 point distribution, see Row 14, does not have this complication when G = 6. And it yields essentially the same results as those using the Rademacher 2 point distribution when G > 10.

Comparing Row 15 to Row 12, we see that imposing the null hypothesis in per forming the wild bootstrap does not change the rejection rate very much in this set of simulations when G > 10, although it appears to matter when G = 6. By comparison, we have found a more substantial difference when simulating from the d.g.p. of Cam eron et al. (2008).

In summary, the various wild cluster bootstraps lead to test size that is closer to

## 0.05 than using a standard Wald test with cluster-robust standard errors and T(G -1)

xooinir)"r)^^t«^ o ^■.oooooooo

## LT)

## IT)

o 000000000 (NmONO\ONh^h •2

## O

o ^toooooooo m 1 000000000

## U

## «4M

o & hOCOh^in^iO^O

## O

joqqqqqq

## CM

dodododoo

## <D

## JD

## Ë

« 3 hhriONOOOONfN z in^oo^^^inhh;opoooo dodododoo v.

^inininNoori'tM nHCJoooi-iriHoo <N r-H O O O — O

## -C>

000000000

## O'

s

## I

i

## I

## D

£

## <D V

o 3 -3 13 13 > > t

## CO

^2 13 a > o -o

## <D

## <U

o 13 13 o u

## 'C \ £

.

## O

o o

## ÛJ) 3 I

o £

## (U <D

j3 J3 -3 13 13

## <D

## £ <D

:§ s fi "O o o c > ^

## S> W

c3

## "Q -S

## R ^

## Q -S

## "•G V*

fs à! o s I ev l dat Monte Carl R j ction a es f Tru S

Tabl e2 e 2 Cros -ection i d vidual u N l Hypothesi (Sl p = 0) with D f er nt Number of Clust and Dif er t R j c ion Meth ds

O u C3 h o o ^ to

## K */

•h.H u u ' ~ Ë ë O ë -â o S | ■s Cl

## "S -S»

c Ë « 13 13 •a.2 c'S.2 *3 ^ ~ s

S-0 s s c c > > > 13 é è srsr ••g u o

## G

## <D

## O

## T3

## O

## _C

s

## <D

## O

£

## S

~o

## C

o £

## I

C/5 <+h J-,

CT <n 6 o cd D O

## -O X)

(N m

## (U <

t 5

PT s=T

## U U

## 1K

jü jj c3 os 4—> -t-1

## 03 C/3

## ÇA <J)

## C C

## O O

c c o o

## T3

## C 3

c3 X) -£ c3 u,u S,°,0 <4-1 <4-1 g.3 s-r;

ë £

## S

w ■*-> f* <u <u a a d) 0) (D 0) (D xi to "T

C/n CX (N r t ci °n y, is

O [s «5 ». c o

3 W o c3 "S -O

## C C "£

## O O §

s-;--—

## (U D O

/ (/) C/D (/) ezs t/o to £ u u u u u U (X 3 3 3 3 3 5 3 -a -H o o o ^ vo ^ VO'sO in o o o o o o 000000 in in

On *0 in Q 5 « 2

## U _' »

vd os on r-en s 8,-i i—I CN •'' § I s S -S <a 10 in in 10 in in 000000 000000 en en en 00 § ri vo ö ri ^

## '-H (N 1

§« Ö <u o

## X C =

## C3 ^

## M U *0

ä S « s.2?

## \0 M M M ^ O

\0 \Q \Q iTi

## OOOOOO

o o ö o o* o

ON in ON la

On ON w u Si in in r-en cn so vo vo

## OOOOOO

000000

## S -2 *

.2

S «s 5 s ü cd 2 3 rj vo in en r n.a c -i "a. > > ^'g ^ o ^ T3 «Bg;

on r-00 on vd o on tj-r-00

## OOOOOO

## OOOOOO

00 ^ ^ en en n en "

U M ffl (U CO is su 12 0 3 9,

S "g i

## O M (-,

Q. m U t M S es 1 o

## <L>

## <D <U

-2 -3 13 es > > *c3 >

## W>

c

## GO _05

g c 'o *0 o-a, 1 1 o o £ £ s * s •§ "i J3 s

## C «8

## ^ CA >

0) •s s ^

## O

o 0 £ ^ "«3 75 "c ^ ~ e s 2:

## Ë

## X>

• £ c o 3 0 c 03 c.5.2 ^ £ o c 'S'5 •e -3 -3 »0 =

## CA

.2.2.2 "3 3 "3

## X) X>

lia.

— u T5 3 c

5 S s e c fli, U.

o o >%

## X5

## 4, ^ -C 4,

£ 3 u-w o £

## <D

## SI

1 fc £ S! o « s -§ ■O Q s "3 C/3 <U > > S.5 ^ Q.

.s s

D S - S ä s S o x> m iC ü W)

## ^'S

c u ^ la £'"3 c c3 a)

## G »-<

•S ü 2 ex o

Si

## T3

## •£ D

-g a: & pc $ &

## O

73 cd www ><r w

## "S

## Ë O

r ^

E-i £} il

Oh Oh

O-O-Oh

V-(h

## H H H

ctf c3 (Q (4 w ci -O X) a> 7"

## O O

000 000

## -O X) -O

## O

& "o w _i-H CA 03

## CA CA

## CA CA CA

3 ^ -2-3-2 "o Tj "o *0 "o -o -o

## "O "O "O

i".s = =

## Ë

>■—-■ y £ u * -a a « * C c a)

## H

o <u g ^ <u x:

? o O 05 0,"£ Un X> î£} <u o reo k, k

## O O

s ë s

## <D (U

u.2 S >.>

Q gl > « o c £ o s g-«S ^ o Su.73 5 tS.2 o p xi -y *-■ cd a> o >

## 0-<Z

## Q Q

## C 4)

a 3 o

CA t/3 CA CA CA O O i^-2

## O 1/5

## ..Q S

2 > -a

## O

(N <u

## ^ V)

## B 3

eS m ~0 Oh on >

Oh

## U

w U l) n!« M ft _-C x ^ 2 o o jr!2 -c S s ä H Ci 5 u

## H ^13«

ifl T3 c3 c r= & & fa is " g

## (D <D

u m B ^ te BGU<

Sa« o

Z fi £ * "■*-»'•<-»

## O O

,<L>,u

B m « x Sf ^ critical values. But the test size still exceeds 0.05 and the bias adjustments in Rows 6 and 7 appear to do better. This example illustrates that at a minimum one should use a cluster-robust Wald test with T(G -1) critical values. Especially when there are few clusters, it is better still to use bias-adjusted cluster-robust standard errors or to use a wild cluster bootstrap. In this Monte Carlo experiment, with few clusters the test size was closest to the nominal size using a Wald test with cluster-robust standard errors computed using the CR2 correction and T(v*) critical values, or using the larger CR2 correction with T(G -1) critical values.

## C. State-Year Panel Data: One Sample

We next turn to a panel difference-in-difference application motivated by Bertrand et al. (2004). The underlying data are again individual-level data from the CPS but now obtained for each of the years 1977 to 2012.

In applications where the policy regressor of interest is only observed at the state year level, it is common to first aggregate the individual-level data to the state-year level before OLS regression. Several methods are used. We use the following method:

The model estimated for 51 states from 1977-2012 is (34) yts = as + 5, + ß x d,s + uls, where v„ is the average log-wage in year t and state s (after partialling out individual level covariates), as and 8, are state and year dummies, and dts is a random "policy"

variable that turns on and stays on for the last 18 years for one-half of the states. Here G = 51, 7 = 36, and 7V= 1836.

The individual level covariates (age, age squared, and years of education) are par tialled out using a two-step estimation procedure presented in Hansen (2007b). Define D,s to be state-by-year dummies. First, we OLS regress log wage (yjls) on state-by-year dummies Dts and on the individual level covariates. And second, yls in Equation 34 equals the estimated coefficients of the Dts dummies.

To speed up bootstraps, and to facilitate computation of the CR2 residual adjust ment, we additionally partial out the state fixed effects and year fixed effects in Equa tion 34 by the standard Frisch-Waugh method. We separately regress yts and dts on the state dummies and the year dummies. Then ß is estimated by regressing the residuals of yts on the residuals of dls with no constant. As noted below, regression using residu als leads to slightly different standard errors due to different degrees of freedom used in calculating the CRVE.

Table 3 presents results for the policy dummy regressor, which should have coef ficient zero since it is randomly assigned.

We begin with Model 1, OLS controlling for state and year fixed effects. Using default or White-robust standard errors (Rows 1-2) leads to a standard error of 0.0037 that is much smaller than the cluster-robust standard error of 0.0119 (Row 3), where clustering is on state. Similar standard errors are obtained using the CR2 correction (Rows 4 and 5) and bootstrap without asymptotic refinement (Row 6). Note that from Rows 10 and 11 the IK and CSS degrees of freedom are calculated to be, respectively, G -1 and G, an artifact of having balanced cluster sizes and a single regressor that is symmetric across clusters.

c* r< ^t ^ cd cj ^ ^ CS cd cd <N

C ^p

C c C c e ^p c/3 oo o

## P

v-> g

Ph

ON fc

## ON D

0)

## J3

= ss e

HOHHHh

## M

m VD vo vo vo "n in

## V)

in Tf rf oo oo oo oo oo oo oo x > c/5 e « > 00 oo oo

## 00 (N

o < s rr-no o tj tj 00 on

Os On

C/3 c.2 0 0 0 0 0 0

## J

o

## S

—i <

## IZ>

## J

p o £

## TJ

s

## <N (N

## NO

^0 ^t

## O

## O

o

## NO

vo 00 00

VO no

## CO

m r-H r-H

## O

## O « « O

O cd cd es

## « O

o c

## Q

c o o c c c o o o i I o o 00 00 10

## IT)

## J"3£

1*1 o

## II 8.

R" co o 1 § c

## CO

cz!

## (N

cs 0 a & r*\

Ph c3 tj > p >> ti

## O O O O O O

o 05

(N M (N (S (N (S

## VO ^ ^ (N

## (N

^ r-r

## IT)

in >T) in U-) *n r-H -h > Os

On Q\

On Q\

On Q\ 0\ § 8:

## C/3

j (N in IT) \0 VO NO VO NO

NO in in <N <N (N <N

## O

## O O

## O M

## N (N

## M (N

## M

o o o o o £ vo

## NO

## «T>

## C/3

o q o o — ^ o

## V~)

«/->

IT) «r>

NO no CO 1—H 00 in

2 On

O On

## <U ON

<u U " e 000000 o

## H-)

## -H

*-<

## <N

## (N

## M

o r-rh-ov on 00 00 00

## X 00

## NO

## VO

## CT)

CO n m rH r-H rH rH

## ,-H

rH 880000 800000 o cd cj cd cd C3 cd

## G

## C G

## C G

## C

O o <-h ^ <n m

## CO

en _i 00 m

## T3 X> 2.

0 0 0 0 0 0 ««u w a> d c o ^ ^ 5 <u

## J3

## M S 6,

## CO <£;

cd O o 13 cd > >"d -O u

## G

## O

-h

## —H

<u • <U cd n <u |u • •« «4-H u."£5 <+H t_

## T3

•0 vs

## \C

^ bû. ob 1 I c ^ 'o'£ '5 ex

O. c®

## V3

ü ^ t o.2.a.2 -o -a *5 k ë S fc t: 1

## O 00«

## O 03 1/3

u o u tj

## S "0

0 a 3 si § 5 -° § cd cd X 3 8 o O ce C

## H5

## C

<u e 2 [Li [Li Ü « 05 a; £

## Q

## Q

-5 w ^ — o 0

## -L-' 03

Table 3 Sta e-y ar p nel dat wi h d f er nc s-in d f er nc s e tima on Impacts of Clu tering a d Estima on Ch ices on E tima ed Co f ic ents, S a d r E o s, and p-v lues -,.

0 12

P ° S3 ä.

•8.§

## =-G

## S UJ

53 £5 55 13 8."

o o 5 5 1 cs cd ç3 cd cd cd j3 Q 1— *"* u

## CO

## «1 CO

## M CO

## W

000 000

## XI

## X) X) JO

## X>

Vh kn l-< <D <L> a> <1> <l>

O O O O a Q eu 3

## « O

1-m'

## 0> <L>

to to 2 -2

## 5 5.3 "3 -S

V3 t/3 u u u u <£ £ &

## H

O g

## •O.

Cfi g «4H

## .S O

## O

o u ^ l| ■w ■w -w w -W +-> w m b u a c

## C

## C C C

<4h fl) d <4-1 <u <u 3

## D "O

*0

## ■8 -O S

S S n e 9add a * * o

## O

o" C)

QJ o § >* sy

Crt _

## X! 1

## O X

cd t> q S3

## <N

## (N <N

## (N §" G

01 c* 05 h S tN

UUi2

UU2i 1) o o <u

## 4> Q.

a.

o -u cd ^r,

T=ï J £ * fi a

## C C <U

## <D

■ c u o g'S ö ô o ^

## PTPT

## ^ ^ O

o

## I I'

lis +« 3 3

## C.O

## •S ^

7-8^ >

## U

## 2 U

e

Sfi.22 o

Is

## -C

•ë 5 ^ ■fi 'fi a c u

## TD

o « o w

## -D

## -O

## *C

o

## M

o ^ 0 5

## J2

t5 *3% 3 ■— u c 0) a) c

## S3

is §

## W M *—<

## DD Q

000 £ 2 2 2 2 2 c J2 it3 « e

Cu

O o £ 3 3 -2 £ 5 £j 1/5 «5

## (D

## D £ ^

u es §

## I

e

## I

## L

o a

## X

## ^ S

o

O sq 3

## «4H

«41 -2 o o O o

## U-.

u ^ u %%

## S

## 6 E

6 m 1 ^ G ^ & |g £ u

## I

## D

## 3 D

3 fc £

## ±2 <B

ea *Ç5 -û The inclusion of state and year fixed effects complicates computation of the de grees of freedom (df) adjustment used in computing the CRVE. The Row 3, Colum 1 results are obtained from regression of residual on residual without intercept, ing command regress, noconstant vce(cluster(state)). Then, from Formula 1 df = [G / (G -1)] x [GT / (GT -1)]. If instead we directly regressed log-wage on th state and year fixed effects and the K regressors, again using regress, vce(cluster(state)), then df = [G / (G -1)] x [GT / (GT -T -G -1)] and the cluster-robust standar error equals 0.0122 rather than 0.0119. And if instead we directly estimate the lo wage equation using xtreg, vce(robust) after xtset state, then df = G / (G -1) and th cluster-robust standard error equals 0.0120. In this example with large T and G, thes adjustments make little difference, but for small G or Tone should use df = G / (G - as explained in Section HIB. The corresponding /»-values for tests of the null hypothesis that ß = 0, following OLS regression, are given in Column 4 of Table 3. Default and heteroskedastic-robust standard errors lead to erroneously large /-statistics (of 0.0156 / 0.0037 = 4.22), s p = 0.000 and the null hypothesis is incorrectly rejected. Using various standard e rors that control for clustering (Rows 3-6) leads to p -0.20 so that the null is no rejected. Rows 7-9 report p-values from several percentile-? bootstraps that again le to rejection of H0: ß = 0. For illustrative purposes, we also compute standard errors allowing for two-wa clustering, see Section V, with clustering on both state and year. These are compute using the user-generated Stata add-on program cgmreg.ado. Clustering on year i necessary if both the regressor and the model errors are correlated across states a given year. For this application, the result (s.e. = 0.01167) is very similar to tha from clustering on state alone (s.e. = 0.01185). In some other panel applications, th two-way cluster robust standard errors can be substantially larger than those fro clustering on state alone. The main lesson from the Model 1 OLS results is that even after inclusion of state fixed effects one needs to use cluster-robust standard errors that cluster on state. The inclusion of state fixed effects did not eliminate the within-state correlation of the error. In this example, the correct cluster-robust standard errors are 3.6 times larger than the default. Model 2 again uses OLS estimation but drops the state fixed effects from Equa tion 34. Dropping these fixed effects leads to much less precise estimation as the cluster-robust standard error (Row 3) increases from 0.0119 to 0.0226 and this cluster robust standard error is now 0.0226 / 0.0062 = 3.6 times the default, compared to a ratio of 3.6 when state fixed effects were included. Note that inclusion of state fixed effects (Model 1) did soak up some of the within-state error correlation as expected, but there still remained substantial within-cluster correlation of the error so that cluster-robust standard errors need to be used. For Model 2, the comparisons of the various standard errors and p-values are quali tatively similar to those for Model 1 so are not discussed further. Model 3 estimates the same model as Model 1, except that the state and year fixed effects are directly estimated, and estimation is now by FGLS allowing for an AR(1) process for the errors. Because there are 36 years of data, the bias correction of Hansen (2007b) —see Section IIIC —will make little difference and is not used here. Estima tion uses Stata command xtreg, pa corr(ar 1) after xtset state.

Comparing Rows 1 and 3, again, even with inclusion of state fixed effects, one should obtain standard errors that cluster on state, using xtreg, pa option vce(robust)). The difference is not as pronounced as for OLS, with FGLS cluster-robust standard error that is 0.0084/0.0062 = 1.4 times the default. FGLS estimation has led to substantial gain in efficiency, with cluster-robust stan dard error (Row 3) for FGLS of 0.0084 compared to 0.0119 for OLS. This example illustrates that, even with state fixed effects included in a state year panel, inference should be based on cluster-robust standard errors. Furthermore, there can be substantial efficiency gains to estimating by FGLS rather than OLS.

D. State-Year Panel Data: Monte Carlo We next perform a Monte Carlo exercise to investigate the performance of various cluster-robust methods as the number of clusters becomes small. The analysis is based on the same state-year panel regression as in the previous subsection, with each state-year observation based on log-wages after partialling out the individual level covariates. In each simulation, we draw a random set of G states (with replacement), where G takes values 6,10,20,30, and 50. When a state is drawn, we take all years of data for that state. We then assign our DiD "policy" variable to half the states with the policy turned on midway through the time period. In these simulations, we perform tests of the null hypothesis that the slope coefficient of the policy variable is zero. As in Table 2, for G = 6 and 10 we perform 4,000 simulations, so we expect that 95 percent of these simulations will yield estimated test size in the range (0.043,0.057). For larger G, there are 1,000 simulations and the 95 percent simulation interval is instead (0.036, 0.064). We begin with the last column of Table 4, with G -50 states. All tests aside from that based on default standard errors (Row 1) have rejection rates that are not appre ciably different from 0.05 once we allow for simulation error. As the number of clusters decreases, it becomes clear that one should use the T(G -1) or T(G -2) distribution for critical values and even this leads to mild overrejection with low G. The pairs cluster percentile-f bootstrap fails with few clusters, with rejec tion rate of only 0.005 when G = 6. For low G, the wild cluster percentile-f bootstrap has similar results with either two-point or six-point weights with very slight over rejection.

## XI. Concluding Thoughts

It is important to aim for correct statistical inference, many empirical applications feature the potential for errors to be correlated within clusters, and we need to make sure our inference accounts for this. Often this is straightforward to do using traditional cluster-robust variance estimators —but sometimes things can be tricky. The leading difficulties are (1) determining how to define the clusters, and (2) dealing with few clusters; however, other complications can arise as well. When faced with these difficulties, there is no simple hard and fast rule regarding how to proceed. You need to think carefully about the potential for correlations in your model errors and

## ON

o\ in

ITl oo 00 vo T) in >n in vo —< oo oo oo oo r^ r o in o m

## U

in m in ^ m

## T)

## Q P Q

IT) o o Q o O o O o iT) odd 000 0 06000 0 0 0 0 -sO Tt

## ON

## SO

vo 0\ 00 oo VO h rf h in in o o © o o o o o

## Q ©

o o en m en m rJ Tt m m m 60000 00000 000 o 00 m, in in m <n

M <n (N o o

## <N

v

## JO

>n m in "n >n in «n in in >n rf i 00000 66060 000

## Q Q Q

in 10 o o © o o o o

## B

3

## Z

o o 00 00 so m m o o rr-o\ on so so so

Os OS G\ OS OS Os 00000 66060 000 600 -h -in in in in

## Q Q Q

in o o o o so

## C\

## OS G\

OS y/~) in ON

## Q\ \D

00 00 ^ rr-in m in in m o o vo so o «n in in 00000 60660 m -h o o o 0) 0) 3 13 > 13 c o o •c

## 'C

3

## X)

o

## D

5 s I

## J3

13.5

## .S 3

> 13

## O

o X> x (U u » 3 3 3 h h o-'jg

## ^'S

## <L>

o

## _ O

^3,3 13 ^ 5 S? 5 uT -

## 'C

$ o > > >.O o mo "+3 *-j

S* *c

## *C

1 ° o o >-^ 5-"

0)

## C/5 I

## <U

c o

## 0) <D

## *Q

## T3

## O

## -C

## OJ

s in 13 73 c

## S

Table 4 Sta e-y ar p nel dat wi h d f er nc s-in d f er nc s e tima on Monte Carl R j ction a es f Tru N l Hypothesi (Sl p = 0) with D f er nt Number of Clust and Dif er t R j c ion Meth ds

## C

c

## O

## O

## O TD

-o u C cd ^ I S B 2j 8 I

ST ^ £--< E-i to B B

## _D

s 2 CÖ Ctf X)

## C/2 C/3

c/5 J—1 xr> 05 a

C C a M C C

## I

V—« i-H i-H 1 cz> c/3 -3 3

## W <+-«

## PJ

~ 0,1 £ o o o g 5 <3 e

## —1 (N

o o.2 o

## Z

## H

03

## T3

## C

cd 03 u tS c3

## B

## U D

## <D Ü

## O

to £

## C/3 (/3 S'3

3 3.fa 3 13

Dh

Q U u u

U u

## U (2

a û -o 13 <u ü ^ u

O cx

## O-I I

## 2 SO

s»-cd c3

OO o g &

## TD

## TD *

## <D

## (D •

## -C

## -C O

o zj ~o 3 u I I I I I 4 Vh I 5-"

t_ G c 8 £

## ,0,0^ O

"cd c3 £

## B ^

—■ — W ê rrt C3 rrt

## C3

0 ^ 13 O c«

## O

## S-H —J

* ^

## O S£

## S2

-o

## •O

## O

o

## -C

## -C

0)

Js 03 ^ <* > §•&"

*! §■ 8 u fi1

## H

hi *3 if

## O

## O O

o o o -û

## -O X>

## X)

11 1— c <u a> s t« C/2 C/5 &

## Q-

a-

## 3 3 J3

## S"

S-"o t_ t_ c/> <z>

## 2 H *S

'3 0 ° Oh

Qh o ^

## O

o o o 2 2 il || 03 how that interacts with correlations in your covariates. In this essay, we have aimed to present the current leading set of tools available to practitioners to deal with clustering issues.

## References

Abadie, Alberto, Alexis Diamond, and Jens Hainmueller. 2010. "Synthetic Control Methods for Comparative Case Studies: Estimating the Effect of California's Tobacco Control Program." Journal of the American Statistical Association 105(490):493-505.

Acemoglu, Daron, and Jörn-Steffen Pischke. 2003. "Minimum Wages and On-the-Job Train ing." Research in Labor Economics 22:159-202.

Andrews, Donald W.K., and James H. Stock. 2007. "Inference with Weak Instruments." In Advances in Economics and Econometrics, Theory and Applications: Ninth World Congress of the Econometric Society, Volume III, ed. Richard Blundell, Whitney K. Newey, and T.

Persson, 122-73. Cambridge: Cambridge University Press.

Angrist, Joshua D., and Victor Lavy. 2002. "The Effect of High School Matriculation Awards:

Evidence from Randomized Trials." American Economic Review 99:1384-414.

Angrist, Joshua D., and Jörn-Steffen Pischke. 2009. Mostly Harmless Econometrics: An

Empiricist's Companion. Princeton: Princeton University Press.

Arellano, Manuel. 1987. "Computing Robust Standard Errors for Within-Group Estimators."

Oxford Bulletin of Economics and Statistics 49(4):431-34.

Barrios, Thomas, Rebecca Diamond, Guido W. Imbens, and Michal Kolesâr. 2012. "Cluster ing, Spatial Correlations and Randomization Inference." Journal of the American Statistical

Association 107(498):578-91.

Baum, Christopher F., Mark E. Schaffer, and Steven Stillman. 2007. "Enhanced Routines for Instrumental Variables/GMM Estimation and Testing." The Stata Journal 7(4):465-506.

Bell, Robert M., and Daniel F. McCaffrey. 2002. "Bias Reduction in Standard Errors for Linear Regression with Multi-Stage Samples." Survey Methodology 28(2): 169-79.

Bertrand, Marianne, Esther Duflo, and Sendhil Mullainathan. 2004. "How Much Should We Trust Differences-in-Differences Estimates?" Quarterly Journal of Economics 119(1): 249-75.

Bester, C. Alan, Timothy G. Conley, and Christian B. Hansen. 2011. "Inference with Depen dent Data Using Cluster Covariance Estimators." Journal of Econometrics 165(2): 137-51.

Bhattacharya, Debopam. 2005. "Asymptotic Inference from Multi-Stage Samples." Journal of

Econometrics 126:145-71.

Bound, John, David A. Jaeger, and Regina M. Baker. 1995. "Problems with Instrumental Variables Estimation When the Correlation Between the Instruments and the Endogenous Explanatory Variable is Weak." Journal of the American Statistical Association 90(430):

443-50.

Brewer, Mike, Thomas F. Crossley, and Robert Joyce. 2013. "Inference with

Differences-in-Differences Revisited." Unpublished, http://www.iza.org/conference_files/

PolicyEval_2013/joyce_r8616.pdf Cameron, A. Colin, Jonah G. Gelbach, and Douglas L. Miller. 2006. "Robust Inference with

Multi-Way Clustering." NBER Technical Working Paper 0327.

. 2008. "Bootstrap-Based Improvements for Inference with Clustered Errors." Review of

Economics and Statistics. 90(3):414-27.

. 2011. "Robust Inference with Multi-Way Clustering." Journal Business and Economic

Statistics 29(2):238-49.

Cameron, A. Colin, and Douglas L. Miller. 2011. "Robust Inference with Clustered Data." In Handbook of Empirical Economics and Finance, ed. Aman Ullah and David E. Giles, 1-28.

Boca Raton: CRC Press.

. 2012. "Robust Inference with Dyadic Data: With Applications to Country-Pair Interna tional Trade." University of California-Davis. Unpublished, http://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2012_July_09.pdf Cameron, A. Colin, and Pravin K. Trivedi. 2005. Microeconometrics: Methods and Applica tions. Cambridge: Cambridge University Press.. 2009. Microeconometrics Using Stata. College Station: Stata Press.

Carter, Andrew V., Kevin T. Schnepel, and Douglas G. Steigerwald. 2013. "Asymptotic Beha ior of a t Test Robust to Cluster Heterogeneity." University of California-Santa Barbara. Un published. http://www.econ.ucsb.edu/~doug/researchpapers/Asymptotic%20Behavior%20 of%20a%20t%20Test%20Robust%20to%20Cluster%20Heterogeneity.pdf Cheng, Cheng, and Mark Hoekstra. 2013. "Pitfalls in Weighted Least Squares Estimation: A Practitioner's Guide." Texas A&M University. Unpublished. Chernozhukov, Victor, and Christian Hansen. 2008. "The Reduced Form: A Simple Approach to Inference with Weak Instruments." Economics Letters 100(1 ):68—71. Conley, Timothy G. 1999. "GMM Estimation with Cross Sectional Dependence." Journal of Econometrics 92(1 ): 1 -45. Conley, Timothy G., and Christopher R. Taber. 201 i. "Inference with'Difference in Dif ferences' with a Small Number of Policy Changes." Review of Economics and Statistics 93(1 ): 113—25. Davidson, Russell, and Emmanuel Flachaire. 2008. "The Wild Bootstrap, Tamed at Last." Journal of Econometrics 146(1 ): 162—69. Davis, Peter. 2002. "Estimating Multi-Way Error Components Models with Unbalanced Data Structures." Journal of Econometrics 106(1 ):67—95. Donald, Stephen G., and Kevin Lang. 2007. "Inference with Difference-in-Differences and Other Panel Data." Review of Economics and Statistics 89(2):221—33. Driscoll, John C.. and Aart C. Kraay. 1998. "Consistent Covariance Matrix Estimation with Spatially Dependent Panel Data." Review of Economics and Statistics 80(4):549-60. Duflo, Esther, Rachel Glennerster, and Michael Kremer. 2007. "Using Randomization in Development Economics Research: A Toolkit." In Handbook of Development Economics, Volume 4, ed. Dani Rodrik and Mark Rosenzweig, 3895-962. Amsterdam: North-Holland. Fafchamps, Marcel, and Flore Gubert. 2007. "The Formation of Risk Sharing Networks." Journal of Development Economics 83(2):326-50. Fernândez-Val, Ivân. 2009. "Fixed Effects Estimation of Structural Parameters and Marginal Effects in Panel Probit Models." Journal of Econometrics 150(1 ):70—85. Finlay, Keith, and Leandro M. Magnusson. 2009. "Implementing Weak Instrument Robust Tests for a General Class of Instrumental-Variables Models." Stata Journal 9(3):398-421. Fitzsimons, Emla, Bansi Malde, Alice Mesnard, and Marcos Vera-Hernândez. 2012. "House hold Responses to Information on Child Nutrition: Experimental Evidence from Malawi." IFS Working Paper W12/07. Foote, Christopher L. 2007. "Space and Time in Macroeconomic Panel Data: Young Workers and State-Level Unemployment Revisited." Working Paper 07-10, Federal Reserve Bank of Boston. Greenwald, Bruce C. 1983. "A General Analysis of Bias in the Estimated Standard Errors of Least Squares Coefficients." Journal of Econometrics 22(3):323—38. Hansen, Christian. 2007a. "Asymptotic Properties of a Robust Variance Matrix Estimator for Panel Data when T is Large." Journal of Econometrics 141(2):597-620.. 2007b. "Generalized Least Squares Inference in Panel and Multi-Level Models with Serial Correlation and Fixed Effects." Journal of Econometrics 141 (2):597—620. Hausman, Jerry, and Guido Kuersteiner. 2008. "Difference in Difference Meets Generalized Least Squares: Higher Order Properties of Hypotheses Tests." Journal of Econometrics 144(2):371—91.

Hemming, Karla, and Jen Marsh. 2013. "A Menu-Driven Facility for Sample-Size Calcula tions in Cluster Randomized Controlled Trails." Stata Journal 13(1): 114-35. Hersch, Joni. 1998. "Compensating Wage Differentials for Gender-Specific Job Injury Rates." American Economic Review 88(3):598-607. Hoechle, Daniel. 2007. "Robust Standard Errors for Panel Regressions with Cross-sectional Dependence." Stata Journal 7(3):281—312. Hoxby, Caroline, and M. Daniele Paserman. 1998. "Overidentification Tests with Group Data." NBER Technical Working Paper 0223. Ibragimov, Rustam, and Ulrich K. Müller. 2010. "T-Statistic Based Correlation and Heteroge neity Robust Inference." Journal of Business and Economic Statistics 28(4):453-68. Imbens, Guido W., and Michal Kolesar. 2012. "Robust Standard Errors in Small Samples: Some Practical Advice." NBER Working Paper 18478. Inoue, Atsushi, and Gary Solon. 2006. "A Portmanteau Test for Serially Correlated Errors in Fixed Effects Models." Econometric Theory 22(5):835—51. Kézdi, Gâbor. 2004. "Robust Standard Error Estimation in Fixed-Effects Panel Models." Hungarian Statistical Review Special Number 9:95-116. King, Miriam, Steven Ruggles, J. Trent Alexander, Sarah Flood, Katie Genadek, Matthew B. Schroeder, Brandon Trampe, and Rebecca Vick. 2010. Integrated Public Use Microdata Series, Current Population Survey: Version 3.0. [Machine-readable database]. Minneapolis: University of Minnesota. Kish, Leslie. 1965. Survey Sampling. New York: John Wiley. Kish, Leslie, and Martin R. Frankel. 1974. "Inference from Complex Surveys with Discus sion." Journal Royal Statistical Society B 36(1): 1—37. Kleibergen, F., and R. Paap. 2006. "Generalized Reduced Rank Tests Using the Singular Value Decomposition." Journal of Econometrics 133(1):97—128. Klein, Patrick, and Andres Santos. 2012. "A Score Based Approach to Wild Bootstrap Infer ence." Journal of Econometric Methods 1(1):23—41. Kloek, T. 1981. "OLS Estimation in a Model Where a Microvariable Is Explained by Aggregates and Contemporaneous Disturbances Are Equicorrelated." Econometrica 49(l):205-207. Liang, Kung-Yee, and Scott L. Zeger. 1986. "Longitudinal Data Analysis Using Generalized Linear Models." Biometrika 73(1): 13—22. MacKinnon, James G., and Halbert White. 1985. "Some Heteroskedasticity-Consistent Covari ance Matrix Estimators with Improved Finite Sample Properties." Journal of Econometrics 29(3):305-25. MacKinnon, James, and Matthew D. Webb. 2013. "Wild Bootstrap Inference for Wildly Dif ferent Cluster Sizes." Queens Economics Department Working Paper Number 1314. McCaffrey, Daniel F., Robert M. Bell, and Carsten H. Botts. 2001. "Generalizations of Bias Reduced Linearization." Proceedings of the Survey Research Methods Section, American Statistical Association. Miglioretti, D.L., and P.J. Heagerty. 2006. "Marginal Modeling of Nonnested Multilevel Data using Standard Software." American Journal of Epidemiology 165(4):453—63. Moulton, Brent R. 1986. "Random Group Effects and the Precision of Regression Estimates." Journal of Econometrics 32:385-97.. 1990. "An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units." Review of Economics and Statistics 72(3):334-38. Newey, Whitney K., and Kenneth D. West. 1987. "A Simple, Positive Semi-Definite, Heteroscedasticity and Autocorrelation Consistent Covariance Matrix." Econometrica 55(3):703-708. Petersen, Mitchell A. 2009. "Estimating Standard Errors in Finance Panel Data Sets: Compar ing Approaches." Review of Financial Studies 22(l):435-80.

Pfeffermann, Daniel, and Gaf Nathan. 1981. "Regression Analysis of Data from a Cluster Sample." Journal American Statistical Association 76(375):681 —89. Rabe-Hesketh, Sophia, and Anders Skrondal. 2012. Multilevel and Longitudinal Modeling Using Stata, Volumes I and II, Third Edition. College Station: Stata Press. Rogers, William H. 1993. "Regression Standard Errors in Clustered Samples." Stata Technical Bulletin 13:19-23. Satterthwaite, F. E. 1946. "An Approximate Distribution of Estimates of Variance Compo nents." Biometrics Bulletin 2(6): 110-14. Schaffen Mark E., and Steven Stillman. 2010. "xtoverid: Stata Module to Calculate Tests of Overidentifying Restrictions after xtreg, xtivreg, xtivreg2 and xthtaylor." http://ideas.repec.org/c/boc/bocode/s456779.html Scott, A.J., and D. Holt. 1982. "The Effect of Two-Stage Sampling on Ordinary Least Squares Methods." Journal American Statistical Association 77(380):848-54. Shah, Bbabubhai V., M.M. Holt, and Ralph E. Folsom. 1977. "Inference About Regression Models from Sample Survey Data." Bulletin of the International Statistical Institute Pro ceedings of the 41 st Session 47(3):43-57. Shore-Sheppard, L. 1996. "The Precision of Instrumental Variables Estimates with Grouped Data." Princeton University Industrial Relations Section Working Paper 374. Solon, Gary, Steven J. Haider, and Jeffrey Wooldridge. 2013. "What Are We Weighting For?" NBER Working Paper 18859. Staiger, Douglas, and James H. Stock. 1997. "Instrumental Variables Regression with Weak Instruments." Econometrica 65:557-86. Stock, James H., and Mark W. Watson. 2008. "Heteroskedasticity-robust Standard Errors for Fixed Effects Panel Data Regression." Econometrica 76(1 ): 155-74. Stock, James H., and M. Yogo. 2005. "Testing for Weak Instruments in Linear IV Regres sions." In Identification and Inference for Econometric Models, ed. Donald W.K. Andrews and James H. Stock, 80-108. Cambridge: Cambridge University Press. Thompson, Samuel. 2006. "Simple Formulas for Standard Errors that Cluster by Both Firm and Time." SSRN paper. http://ssrn.com/abstract=914002.. 2011. "Simple Formulas for Standard Errors that Cluster by Both Firm and Time." Journal of Financial Economics 99(1): 1-10. Webb, Matthew D. 2013. "Reworking Wild Bootstrap Based Inference for Clustered Errors." Queens Economics Department Working Paper 1315. White, Halbert. 1980. "A Heteroskedasticity-Consistent Covariance Matrix Estimator and a Direct Test for Heteroskedasticity." Econometrica 48(4):817—38.. 1984. Asymptotic Theory for Econometricians. San Diego: Academic Press.

Wooldridge, Jeffrey M. 2003. "Cluster-Sample Methods in Applied Econometrics." American Economic Review 93(2): 133-38.. 2006. "Cluster-Sample Methods in Applied Econometrics: An Extended Analysis." Michigan State University. Unpublished. http://econ.ucsb.edu/~doug/245a/Papers/Cluster %20Sample%20Methods%20in%20Applied%20Econometrics.pdf. 2010. Econometric Analysis of Cross Section and Panel Data. Cambridge: MIT Press.

Yoon, Jungmo, and Antonio Galvao. 2013. "Robust Inference for Panel Quantile Regression Models with Individual Effects and Serial Correlation." Unpublished.
