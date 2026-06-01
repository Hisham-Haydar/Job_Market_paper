# NONPARAMETRIC ESTIMATION WITH NONLINEAR BUDGET SETS

By Soren Blomquist and Whitney Newey

Keywords: Nonlinear budget sets, nonparametric estimation, additive models.

## 1. Introduction

[Manual cleanup note: the PDF text layer merged the title page, acknowledgements, and opening pages into a single corrupted block. The unreadable span has been replaced with a short readable reconstruction of the opening argument.]

Choice models with nonlinear budget sets provide a precise way to account for nonlinear tax structures in empirical work. The paper proposes a nonparametric approach to estimating these models by treating hours of labor supply as a function of the entire budget set and then exploiting the structure implied by utility maximization with piecewise linear convex budget sets.

The central argument of the introduction is that direct nonparametric regression on all budget-set characteristics would suffer from the curse of dimensionality. The authors show that convexity and utility-maximization restrictions reduce this problem substantially, yielding an estimator that remains accurate even when the number of budget segments differs across observations. The paper then applies the estimator to Swedish tax-reform data.

## 2. Utility Maximization and Convex Budget Sets

Our approach is to nonparametrically estimate the conditional mean of hours given the budget set. That is, if h i is the hours of the ith individual and x i represents the budget set, our goal is to estimate (2.1)

Eh i x i = h̄x i In comparison with the maximum likelihood approach, this one imposes fewer restrictions but only estimates the ﬁrst (conditional) moment. Consequently, some aspects of labor supply will not be identiﬁed and efﬁciency may be lost, but the estimator will be robust to functional form assumptions. Speciﬁcally, estimation of only the conditional mean will not generally permit identiﬁcation of the distribution of preferences and the labor supply function, because there are more functions to be identiﬁed (two) than there are conditional moment restrictions (one). However, conditional mean estimation does permit prediction of the effect of tax structure changes on labor supply, as long as the predictions lie within the range of the data. That is, there must be sufﬁcient variation in budget set characteristics so that there are budget sets in the data that are close to the ones for the prediction. Our approach shares this feature with all nonparametric approaches, which do not identify predictions outside the range of the data. To better understand the issues it is useful to consider a labor supply function of the form h i = hx i v i + i where v i represents individual heterogeneity, and i is measurement error. The typical maximum likelihood speciﬁcation relies on an assumption that v i and i are normal and homoskedastic, while all that we require is that v i be independent of x i and E i x i = 0. In this case h̄x i = hx i v gv dv, where gv is the density of v. The maximum likelihood approach could be used to estimate (the parameters of) gv and hx v, which could be used for welfare comparisons and efﬁcient prediction. Our approach is to estimate h̄x i directly, without imposing functional form, which is useful for nonparametric prediction. By adopting this approach, we only identify objects that depend on h̄x i, rather than the whole distribution of preferences. Generally the two functions hx v and gv will not both be identiﬁed from the single restriction. Also, there may be some loss in efﬁciency relative to maximum likelihood estimation of a correctly speciﬁed parametric model. Our approach will be valid for quite general data generating processes. The conditional expectation h̄x is well deﬁned without utility maximization or convex budget constraints. However, without some simplifying structure on h̄x it will in general be infeasible to estimate it due to a severe dimensionality problem. In particular, a piecewise linear budget constraint with J segments depends on 3J − 1 numbers (or 2J if it is continuous). For the intercept y j and slope w j of the jth segment j = 1 J, and the end point j between the j and j + 1 segments, a full description of the budget set corresponds to (2.2) x = J y 1 y J w 1 w J 1 J −1 If the budget frontier is continuous, then j = y j − y j+1 /w j+1 − w j can be dropped from x, reducing the dimension somewhat. However, in any case x will be large dimensional, and h̄x difﬁcult to estimate, for J greater than 2 or 3. Restrictions implied by utility maximization with convex preferences and convex budget sets reduce greatly this dimensionality problem. To derive these restrictions we take as a starting point the assumption that desired hours for a linear budget set are given by (2.3) h ∗ = y w v where v is a scalar unobserved variable that represents individual heterogeneity. This set up allows for h ∗ to be nonlinear in the heterogeneity variable, as is known to be important from Brown and Walker (1989). We also will assume that v is statistically independent of the budget set and that y w v is strictly increasing in v. The independence assumption would be appropriate for a crosssection of labor markets, where individuals are wage takers, and are not choosing among a proﬁle of wage and hours combinations, and where tastes for work are not correlated with skill levels. Endogeneity can be allowed for, as discussed below, although it complicates the estimation. In our empirical example we do not ﬁnd much evidence of endogeneity. We will focus here on the case, common in applications, where the budget set is piecewise linear. Let −1 y w denote the inverse of the function y w v as a function of v and ¯ y w = (2.4) y w v gv dv − y w = −1 − y w y w v − gv dv The following result gives the form of the expected hours function. Theorem 2.1: If for all J and j = 1 J y j w j v gv dv < y j w j v is strictly increasing in v on its support, and Prh = 0x = 0, then (2.5) ¯ J w J + h̄x = y

## J

−1 j=1 y j w j j − y j+1 w j+1 j This expression corresponds to an additive decomposition of expected hours over different budget segments and kink points. 2 It is a representation of h̄x ¯ J w J for a linear budget set plus a term that in terms of the average hours y corrects for the nonlinearity of the budget sets. When y w v is linear in v this correction term is analogous to the Heckman (1979) correction in the sample ¯ selection model. The y w is like the regression function and the difference term like the inverse mills ratio in a selection correction. The correction term has dimension three, and has a particular difference form. Exploiting this structure in the nonparametric estimation leads to an estimator with accuracy that does not depend on J, allowing us to do nonparametric estimation with any number of budget segments. Of course this term is here accounting only for the nonlinearity of the budget sets, and not for sample selection. We assume throughout that gross wages are always observed. The conditions of this result specify that the probability of no work is zero. This condition is appropriate for describing the labor supply of those who work when there is no (or very little) bias from selecting that sample. Such is the case for our application and others where there are few unemployed. In many applications though, such as female labor supply, sample selection could cause a problem (e.g. see Mroz (1987)). This problem could be dealt with by considering simultaneously the decisions of whether and how much to work. This consideration is beyond the scope of this paper.

¯ An important feature of expected hours is that y w is an additive component. This function is the conditional expectation of hours given a linear budget segment. It contains useful information about preferences. For example, its derivatives could be compared with those for parametric models to obtain simple speciﬁcation tests. It could w also be used to estimate average approximate sur¯ plus changes of the form w 1 2 y w dw, for wage rates w 1 and w 2, corresponding to linear tax schedule changes. Furthermore, when y w v = y w + v ¯ and Ev = 0, then y w = y w, which could be used to calculate surplus changes for nonlinear taxes for speciﬁc values of v. Of course, without further identifying information about the distribution of v it would be hard to interpret such calculations, corresponding as they do to particular values of v.

¯ The structure of the conditional expectation should help to identify y w.

¯

Of course y w is equal to h̄x when the budget set is linear, but because ¯ of the restricted form for h̄x, y w may be identiﬁed even when there is not data with approximately linear budget constraints. The following result gives ¯ necessary and sufﬁcient conditions for identiﬁcation of y w over a set Y W (meaning that any two functions satisfying equation (2.5) must coincide on Y W ).

2 for hours of Expression (2.5) is derived under the assumption that there is no upper limit H for hours of work, we would get one more term. This term work. If we introduce an upper limit H would be similar to that at h = 0, and would be small if there was little probability of choosing H.

¯

Theorem 2.2: y w is identiﬁed over Y W if and only if for any func¯ tions ay w and by w satisfying the restrictions on y w and y w respectively, ay J w J +

## J

−1 j=1 by j w j j − by j+1 w j+1 j = 0 implies ay w = 0 for all y w ∈ Y W. A necessary condition for identiﬁcation of ¯ y w on Y W is that Y W is included in the intersection of the support of y 1 w 1 and y J w J.

¯

This result shows that y w can at most be identiﬁed over the sets that include observations on both y 1 w 1 and y J w J, i.e. on initial and ﬁnal virtual incomes and wages. It would also be useful to have simple sufﬁcient conditions for identiﬁcation, but these are difﬁcult to ﬁnd because of the potentially complicated nature of the budget sets. It should be noted that there may be only a few sources of variation in the ¯ budget set that serve to identify y w. These include variation in the basic wage, nonlabor income, and other variables that shift the budget set for a given tax structure. When changes in tax structure are included in the data, as in our application, these may also help with identiﬁcation. Such variation may help predict the effect of tax changes. Another important feature of equation (2.5) is that its additivity and equality restrictions can be tested. This could be accomplished by testing for the presence of interaction or other terms that do not appear in equation (2.5). When budget sets are convex such tests would be a check of the joint hypothesis of utility maximization, convex preferences, and a single individual heterogeneity variable v. When budget sets are nonconvex they will also test for the importance of nonconvexities. Some nonconvexity in the budget sets can be allowed for in a straightforward way. Suppose for some budget segment j, other than last or second to last, we have w j > w j −1 and w j +1 < w j −1. If there is positive probability of being on segment j and j + 1, then (2.6) ¯ J w J + h̄x = y

## J

−1 j=1 y j w j j − y j+1 w j+1 j +y j w j y j +1 w j +1 The term quantiﬁes the effect of the deviation from convexity on expected hours. It will depend on the budget sets in a complicated way that is difﬁcult to specify in terms of y w v and the distribution of v. However, it can be allowed for by including the additional function in this equation. Another type of nonconvexity that may be important is a discontinuity in the budget set. If the slope does not change on either side of the discontinuity there would be an additional term y j y j +1 j.

Nonconvexities may raise the dimension of the unknown function and remove some of the equality restrictions, making it more difﬁcult to estimate expected hours. However if the nonconvexities are small or few individuals are located at nonconvexities, the additional terms would be small relative to the rest of h̄x, and ignoring them would be approximately correct. In these cases the integration over individual heterogeneity implicit in this nonparametric approach helps reduce the importance of nonconvexities. When the nonconvexities only occur for a few individuals, that part of the expected hours function will not be very important. So far, we have only considered h̄x = Ehx. If the measurement error i in equation (2.1) only satisﬁes the conditional moment restriction E i x i = 0, then that is all the information available. If however i satisﬁes other restrictions, then it may be possible to use this information to estimate h̄x more efﬁciently and/or identify w y v and the distribution of v. Suppose that i is independent of the budget set. Consider any monotonic increasing function h. Then for the density f of and the monotonic increasing function ¯ h = h+ f d, E h x = E ¯ hx v x For convex preferences and budget set the form of this conditional expectation will be analogous to equation (2.5). This restriction could be used to estimate the conditional expectation h̄x more efﬁciently. Also, it may be possible to identify y w v gv, and f from several such restrictions. We leave the pursuit of these objectives to future research. A vector of covariates z could be allowed for by specifying that has the form y w z v. The form of the expected labor supply function would then be the same as in Theorem 2.1, with the covariates z included as additional arguments ¯ With this speciﬁcation the addition of each covariate would raise the in and. dimension of the nonparametric function, making it impractical to allow for more than a very few covariates. An alternative approach would be to specify that has an index form y w z 0 v where 0 is an unknown vector of parameters, analogously to Ichimura (1993). Then ¯ J w J z 0 +

Ehx z = y

## J

−1 j=1 y j w j j z 0 −y j+1 w j+1 j z 0 Here the dimension of the nonparametric speciﬁcation is four, which may make allowing for covariates practical even when there are several. This speciﬁcation could be estimated using a nonlinear version of the least squares estimator described in the next section. We can allow for endogeneity of the variables determining the budget set using control variates as in Blundell and Powell (2001). Here h̄x is precisely the average structural function they consider, and can be identiﬁed in the way they describe. Suppose that x = b z 1, where b is a vector of variables that may be endogenous and z 1 is a subvector of potential instruments. Also suppose that b = rz 1 z 2 + $ with v $ independent of z 1 and z 2, and the measurement error has mean zero given z and $. Then, since x is a function of z and $,

Ehx $ = EEhz $x $ ¯ J w J $ + = y

## J

−1 j=1 y j w j j $ − y j+1 w j+1 j $ ¯ where y w $ and y w $ are deﬁned exactly as in equation (2.4), except that the integration is over the conditional density of v given $. Furthermore, as shown by Blundell and Powell (2001), h̄x = Ehx $f $ d$. Thus, h̄x can be obtained from a conditional expectation with the same form in Theorem 2.1, with $ added as a variable, followed by integration over the marginal distribution of $. For estimation $ can be replaced with the residual from the nonparametric regression of b on z, and integration with the average over the empirical distribution of the residuals. This model can also be used to test for endogene¯ ity, by checking to see whether the residuals are signiﬁcant in y w $ and y w $.

3 estimation We focus on methods for which it is easy to impose the additivity and equality restrictions of equation (2.5). Series estimation is particularly convenient for this purpose. Stone (1985) has shown how to impose additivity (by excluding interaction terms) and Porter (1998) equality (by imposing equality of coefﬁcients). For each positive integer K let p kK x k = 1 K denote K functions of x that impose these restrictions, and let p K x = p 1K x p KK x be an associated vector of approximating functions. For data x i h i i = 1 n, let P = p K x 1 p K x n and H = h 1 h n. A series estimator of h̄x is given by ĥx = p K x * ˆ (3.1)

## * ˆ = P P

−

## P H

− where B denotes any symmetric generalized inverse. Two types of terms are needed for an approximation of the h̄x in equation ¯ (2.5). The ﬁrst consists of terms that approximate y w. For this purpose we consider power series that have the form (3.2) pk p kK x = y J qk w J We will focus on power series as approximating functions, although regression splines or other types of approximating functions could be used. The second type of term that is needed is for the correction term in equation (2.5). For this purpose we consider terms based on functions kK y w that can approximate y w. Differencing these gives (3.3) p kK x =

## J

−1 j=1 kK y j w j j − kK y j+1 w j+1 j Linear combinations of this type of function will approximate the correction term when linear combinations of kK y w approximate y w. Any kK y w that depends only on will drop out, and need not be used for any p kK x. Other terms may also drop out. We consider a raw power series approximation and one that is centered at the Gaussian case. An important and interesting feature of this approach is that the number of budget segments may vary across individuals in a completely ﬂexible way. The number of budget segments enters only through the form of the approximating functions in equation (3.3), and does not affect K. This feature allows the number of budget segments to be as large as needed. The reason that we are able to do this is that this estimator imposes the additivity and equality restrictions of equation (2.5). Consequently, it will have convergence properties that are uniform in the number of budget segments, as we discuss in the next section.

31 Power Series A raw power series approximation uses powers of the three variables y w, and of the form (3.4) kK y w = mk y pk w qk pk + qk ≥ 1 Linear combinations of these terms can approximate the function kK y w. Consequently, linear combinations of the functions in equation (3.3) will approximate the correction term in h̄x.

32 Gaussian Centered Approximation Another kind of approximation is obtained by taking as the leading term one that is exact for some parametric speciﬁcation for y w v and the distribution of v. The motivation for this type is to center the approximation at a parametric model in the hope that this will give the right location and scale for the approximation. We consider the case where y w v = c + *y + /w + v and v is distributed N 0 1 v 2. In this case, y w = 1 v 2 − c − *y − /w /1 v 2u = −u4u − 5u where 4u and 5u are the Gaussian p.d.f. and CDF respectively. Let ĉ * ˆ /̂, and 1̂ v be estimators of the parameters, as could be obtained from the MLE. An alternative that is simpler to compute would be instrumental variables estimation of the equation h = c + *ỹ + /w̃ + ṽ, where ỹ and w̃ are the intercept and slope of the budget segment where h is located, and instruments such as the average of intercept and slope across all segments are used. These estimators need not be consistent for the approximation to be valid. Then let ˆ − /̂w /1̂ v ˆ y w = 1̂ v 2 − ĉ − *y The approximation we consider uses this function as the ﬁrst term.

To construct a full, three dimensional approximation, we consider a one-toone transformation of y w. This transformation forms a nonsingular linear combination and then applies a monotonic transformation to each component. Let ȳ and w̄ be the mean of the intercepts and slopes across all budget segments and individuals. The linear transformation is     − ĉ − * ˆ ȳ − /̂ w̄   w  →   − ĉ − * ˆ ȳ − /̂w  ˆ − /̂w y − ĉ − *y This triangular transformation is one-to-one as long as /̂ = 0 and * ˆ = 0. We then apply the strictly monotonic transform 1̂ v 2·/1̂ v. Power series terms in these transformed variables then take the form kK y w = ˆ ȳ w̄ mk ˆ y w pk ˆ ȳ w qk pk + qk ≥ 1 The term with pk = 1 and mk = qk = 0 is an exact correction for a normal if the parameter estimators are consistent. Thus, this approximation is centered at the normal correction, having that as the leading term. Also, the location and scale of all three of these functions has been set, inside the 2· transformation, which could help center the power series. In addition, one of the transformations depends only on, so that by the form of the correction term only interactions of this with other terms is needed. The presence of the estimated parameters should have no effect on the convergence rate of the estimator, or on the asymptotic variance of the estimators. Varying those parameters does not affect consistency of ĥx, as long as they correspond to a nonsingular linear transformation of y w. Therefore, by the reasoning given in Section 6 of Newey and McFadden (1994), the asymptotic variance is unaffected.

33 Choosing the Number of Terms To make use of the nonparametric ﬂexibility of series estimators it is important to choose the number of terms based on the data. Here we will use a crossvalidation criteria to compare different speciﬁcations. This criteria is n 2

## C V K = 1 − SSEK

h i − h̄ i=1

## SSEK =

n i=1 h i − ĝx i 2 1 − p K x i P P − p K x i 2 The term SSEK is the sum of squares of one-step ahead forecast errors, where all the observations other than the ith are used to form coefﬁcients for predicting the ith. It has been divided by the sample sum of squares for h to make the criteria invariant to the scale of h. Choosing K to maximize C V K is known to minimize asymptotic mean-square error (Andrews (1991)), where the bias goes to zero at the same rate as the standard deviation. Larger values of K are required for asymptotic inference, so that the bias goes to zero faster than standard deviation. Here we will report results, including cross-validation values, for a range of K, focusing on larger values of K.

34 Functional Estimation In many cases we may not only be interested in the expected labor supply function, but also in functionals of it. One important example is a wage elasticity of the expected labor supply for a linear budget set, given by E w = w̄/h̃ 9 h̄J w w ȳ ȳ /9w w= w̄ where h̃ is the hours level and w̄ and ȳ are the wage and income. These elasticities can be compared with those for parametric speciﬁcations to measure the impact of functional form assumptions. Another important example is the percent change in average labor supply from budget set shifts for a group of individuals. If x s B represents the budget set before the change and x s A after, then this functional is

## S

## S

## S

## M =

h̄x s A − h̄x s B h̄x s B (3.5) s=1 s=1 s=1 Such functionals can be estimated by substituting ĥ for h̄ in their formulae. Standard errors for these estimates can be constructed using the usual approach for series estimators. Inference is straightforward when there is a linear functional ah such that the object of estimation is = 0 = ah̄. An estimator of this linear functional can be formed as = ˆ = aĥ. Let A = ap 1 ap K, Q = P P /n, and? = ni=1 p K x i p K x i h i − ĝx i 2 /n. Then an estimator of the asymptotic variance of = is (3.6)

## V = A Q −? Q − A

This estimator is just the usual one for a linear combination A * ˆ of least squares coefﬁcients, with Q −? Q − being the White (1980) estimator of the least squares ˆ This estimator will lead to correct asymptotic inferences asymptotic variance of *. because it accounts properly for variance, and because bias will be small relative to variance under the regularity conditions discussed below. Then, √ d V −1/2 n = ˆ − = 0 → N 0 1 ˆ Nonlinear funcso that V /n is an appropriate asymptotic standard error for =. tions of linear functionals can be handled by the standard delta method.

As examples consider the wage elasticity and tax change effects described above. The wage elasticity estimator and standard error would be = ˆ = A * ˆ SE = ˆ = A Q −? Q − A/n (3.7) A = w̄/h̃ 9p K J w w ȳ ȳ /9w w= w̄ The estimator of a tax change effect and its associated standard error would be ˆ * ˆ

## = ˆ = D */B

SE = ˆ = C Q −? Q − C/n (3.8)

## B =

## S

s=1 p K x s B /S

## D =

## S

s=1 p K x s A /S − B

## ˆ /B * ˆ

## C = D − =B

In the empirical example we will report estimators of both elasticities and tax change effects, along with the standard errors described here.

4 large sample theory The difference form of the conditional expectation allows us to derive convergence rates that are uniform in an unbounded number of budget segments. In this way the accuracy of the nonparametric estimator does not depend on the number of budget segments. Obtaining these rates requires approximation of both the function y w and its ﬁrst derivatives. A literature search has only revealed such approximation rates for polynomials under strong smoothness restrictions. For this reason, we also give theoretical results for tensor product splines, e.g. as described in Newey (1997). Also, to avoid technical complications we only give results for raw power series approximation in equation (3.4), and not the one that depends on parameter estimators. The ﬁrst assumption covers both the power series and spline cases. Assumption 1: There is a constant C such that max j≤J i w ji, max j≤J i y ji, max j≤J i −1 j ≤ C. Also, either (a) p K x consists of sth order tensor product splines ¯ and y w and y w have s bounded, continuous derivatives; or (b) p K x ¯ is a power series and y w and y w are continuously differentiable of all orders with kth derivatives bounded by C k for some constant C. This condition leads to an approximation rate where there is a constant C such that for each K there exists * K with (4.1) sup h̄x − p K x * K ≤ CK −A x

A = s − 1 /3 splines

A = any positive constant (power series).

In what follows we will let A be as given in this equation for the respective cases. If J were bounded, then for power series the strong smoothness assumption could be replaced by the conditions of part (a), and A could be chosen to be s/3 for both splines and power series. Allowing for unbounded J, as we have done, seems appropriate for environments where the number of segments can vary greatly across observations. The next condition is a standard one in the series estimation literature. Assumption 2: (h i x i ), (i = 1 n) are i.i.d. and var(h i x i) is bounded. Let ĥ i = p K x i * ˆ and h̄ i = h̄x i. Theorem 4.1: If Assumptions 1–2 are satisﬁed, then O p K/n + K −2A.

n i=1 ĥ i − h̄ i 2 /n = The K/n term in the conclusion of the theorem is a variance term. The other term is a bias term that corresponds to equation (4.1). The best attainable convergence rate is obtained by choosing them so that bias and variance terms vanish at the same rate. Then the convergence rate for ĥ (i.e. the square root of the rate from Theorem 4.1) is n −A/1+2A. For splines this rate is n −s−1 /1+2s. From Stone (1982) it follows that this is the optimal rate for estimation of a function and its ﬁrst derivative, when s derivatives exists and the dimension is 3. Estimation of the ﬁrst derivative is important for obtaining an approximation that is uniform in a possibly unbounded number of segments. If J were bounded, then one could obtain a convergence rate that was optimal for estimation of just the function itself, and not of the derivative. Theorem 4.1 gives a convergence rate for the sample MSE. To obtain a rate for the population MSE and uniform convergence, as well as for asymptotic normality, the following condition is useful. Assumption 3: For each K there is a constant matrix B and bK such that for p̃ K x = Bp K x, the smallest eigenvalue of Ep̃ K x p̃ K x is bounded away from zero uniformly in K p̃ K x ≤ bK, and bK 2 K/n → 0. This condition is exactly the one given in Newey (1997). It ensures convergence in probability of the second moment matrix of the approximating functions, after a normalization. This condition places an upper bound on the rate at which K can grow. In Newey (1997) primitive conditions are given that lead to the requirement that K 3 /n → 0 for power series and K 2 /n → 0 for splines. Developing analogous precise rates here is more difﬁcult, because of the unusual form of p K x. We leave this development to future work. Assumption 3 is the critical condition that allows us to derive convergence rates and asymptotic normality results exactly like those of Newey (1997). For completeness, we give a brief report of these results, because they justify the asymptotic inference procedures that we use. The only difference with Newey (1997) is the form for A from equation (4.1). We refer the interested reader to Newey (1997) for more detailed explanations. Let X denote the support of x, and F 0 x the distribution function of x i. Theorem 4.2: If Assumptions 1–3 are satisﬁed, then

## K

## + K −2A

ĥx − h̄x 2 dF 0 x = O p n

## K

sup ĥx − h̄x = O p bK

## + K −A

n x∈X Some additional conditions are important for the asymptotic normality result. Assumption 4: EEh i − h̄x i F 4 x i is bounded, and varh i x i is bounded away from zero. Assumption 5: a(h) is a scalar, there exists C such that ah < C sup x∈X hx, and there exists h K x = p K x * ˜ such that Eh K x 2 → 0 and ah K is bounded away from zero. To state the asymptotic normality result it is useful to work with an asymptotic variance formula. Let 1 2 x = varhx and (4.2) Q = Ep K x p K x? = Ep K x p K x 1x 2

## V K = A Q −1?Q −1 A

Theorem √ 4.3: If Assumptions 1–5 are satisﬁed and

O p bK / n and

## √ −A

nK → 0, then = ˆ = = 0 + √ −1/2 d d nV K −1/2 = ˆ − = 0 → N 0 1 n V

## = ˆ − = 0 → N 0 1

√ The condition nK −A → 0 ensures that the bias is small relative to the variance.

√ Assumption 6: There is vx with Evx vx ﬁnite and nonsingular such that ah̄ = Evx h̄x, ap kK = Evx p kK x, for all k, and there is * K with Evx − p K x * K 2 → 0. The asymptotic variance of the estimator is determined by the function vx from Assumption 6 and is equal to (4.3)

V = Evx vx varh x Theorem 4.4: If Assumptions 1–4 and 6 are satisﬁed, and √ d n = ˆ − = 0 → N 0 V p

## V → V

√ nK −A → 0, then 2468 2469 5 estimation on swedish data

51 Data Source We use data from three waves of the Swedish “Level of Living” survey. The data pertain to the years 1973, 1980, and 1990. The surveys were performed in 1974, 1981, and 1991. The 1974 and 1981 data sources are brieﬂy described in Blomquist (1983) and Blomquist and Hansson-Brusewitz (1990) respectively. The 1990 data is based on a survey performed in the Spring of 1991. The sample consists of 6,710 randomly chosen individuals aged 18–75. The response rate was 79.1%. Certain information, like taxation and social security data, were acquired from ﬁscal authorities and the National Social Insurance Board. 3 Sample statistics are provided in Appendix A. In the estimation we only use data for married or cohabiting men in ages 20–60. Farmers, pensioners, students, those with more than 5 weeks of sick leave, those who were liable for military service, and the self employed are excluded. This leaves us with 777 observations for 1973, 864 for 1980, and 680 for 1990. The tax systems for 1973 and 1980 are described in Blomquist (1983) and Blomquist and Hansson-Brusewitz (1990). The tax system for 1990 is available from the authors upon request. Housing allowances have over time become increasingly important. For 1980 and 1990 we have therefore included the effect of housing allowances on the budget constraints. The housing allowances increase the marginal tax rates in certain intervals and also create nonconvexities. We assume that these nonconvexities have small effects of the type discussed in Section 2 and hence ignore them in the nonparametric estimation and convexify the budget sets for parametric estimation. We also check for bias from ignoring nonconvexity in a Monte Carlo example given below. The fact that we pool data from three points in time has the obvious advantage that we have more observations than if we considered single years. Another important advantage is that we obtain a variation in budget sets that is not possible with data from just one point in time. The tax systems were quite different in the three time periods, which generates a large variation in the shapes of budget sets. Furthermore, we have data from before and after a large tax reform, which should help us identify the effect of that reform on labor supply. 4

52 Parametric Estimates We pool the data for the three years and estimate a linear model y w v = c + *y + /w + v where v and are independent of each other and distributed N 0 1 v 2 and N 0 1 2. The data from 1973 and 1990 were converted into the 1980 price level. We have also convexiﬁed the budget constraints for data from 3 Detailed information on the 1990 data source can be found in Fritzell and Lundberg (1994). We have chosen not to include time effects. Although including them might improve the ﬁt of the model, they would also be collinear with the time series variation in the budget set that is helping to identify the effect of a tax reform. 4 1980 and 1990, as is common in previous work and consistent with the assumption that nonconvexities have small effects. We show the results in equation (5.1). Here E w and E y are elasticity estimates for wage and income that are evaluated at the mean of the net wage rates and virtual incomes from the segments where individual’s observed hours of work are located. All elasticities are evaluated at the same values for the wage rate, virtual income, and hours of work. Standard errors are given in parentheses beneath each coefﬁcient. (5.1) h = 1914 + 0157w −000865y −00996 AGE − 00346NC 0309 00175 000145 0188 00786 ln L = −22543

E w = 123 0137 1 v = 270 00641 1 = 105 00889

E y = −022 00370 The standard errors are based on a numerical approximation to the Hessian of the log-likelihood function, which may be less reliable than an analytical formula, because this model is highly nonlinear (especially in the variance parameters). Because the age and number of children coefﬁcients are insigniﬁcant here, we exclude them from consideration for the nonparametric estimator. Much of the interest in nonlinear budget sets stems from a wish to be able to predict the effect of changes in the tax system on labor supply. Here we estimate the effect of Swedish tax reform on expected hours of work, 5 by estimating the parameter M of equation (3.5). Blomquist, Eklof, and Newey (2001) perform a detailed analysis of the effect of Swedish tax reform between 1980 and 1991. Here we consider a simpliﬁed and stylized version of that reform, as described in Appendix B. Our purpose here is not to give an accurate prediction of the effect of the actual tax reform but to make a comparison between the parametric and nonparametric methods. 6 Around 1980 the Swedish tax system reached a peak in terms of high marginal tax rates. Then, gradually during the’80’s the marginal tax rates were lowered with a quite large change in the tax system between 1990 and 1991. We will use the actual distribution of gross wage rates and nonlabor income from the 1980 data set to calculate the effect of the changes in the tax system between 1980 and 1991. The 1980 and 1990 income tax systems are described more fully in Blomquist and Hansson-Brusewitz (1990) and Blomquist, Eklof, and Newey (2001). We use the labor supply function from equation (5.1) and estimate the conditional expectation of hours given each 1980 individual’s

5 There exist alternative approaches to evaluating the effect of tax reform on labor supply. Blundell, Duncan, and Meghir (1998) and Eissa (1995) use difference in differences estimators to estimate the effect of tax reform on female hours of work. 6 Agell, Englund, and Södersten (1995) contain a broad evaluation of the Swedish tax reform. Aronsson and Palme (1998) also contain a description of tax reform in Sweden. They present labor supply functions derived from a household model and estimated by a maximum likelihood technique.

budget set by simulation. We do these calculations using original (nonconvex) budget sets. We obtain the estimate

## M = 0546

0212 To motivate the need for the nonparametric estimates we consider two speciﬁcation checks, focusing on the wage elasticity, because of its pivotal importance to the tax effect. We use this approach to speciﬁcation testing, rather than a goodness of ﬁt approach, because it focuses on the sensitivity of something we care greatly about. The ﬁrst check is a Hausman test based on the difference of the MLE and a two-step least squares estimator based on the Gaussian correction to the conditional expectation using the MLE. Although, the two-step standard errors are inconsistent due to estimated regressors, they overstate the variance because the ﬁrst step is MLE. Also, although the MLE standard error is larger than the two-step standard error, the two step standard error is an upper bound on the standard error of the difference of the two-step estimator and the MLE. Thus, a lower bound on the absolute value of the Hausman test can be formed by dividing the absolute value of the difference of the estimators by the two-step standard error. The two-step elasticity, standard error, and lower bound on the test are

E w 2S = 0826 0123

## T = 328

The value of |T | is signiﬁcant at conventional levels, providing evidence of misspeciﬁcation. The second check is a Hausman test based on the difference of the MLE and an instrumental variables (IV) estimate of the linear labor supply model with the wage and income for the budget segment where the individual located and instruments given by the average across segments of the slopes and intercepts. The resulting estimator of the wage elasticity, with associated heteroskedasticity consistent standard error and speciﬁcation test statistic, are

E w IV = 0718 0176

## T = 464

The IV estimator is inconsistent, so that strictly speaking this test statistic is incorrect. Nevertheless, the inconsistency is often quite small, so that such a large value may provide evidence of misspeciﬁcation. To check for such evidence we consider a small Monte Carlo study, where the true model had parameters equal to the MLE estimates from equation (5.1), with AGE and NC set to their mean values, and the budget sets were those given in the data. The data were generated by utility maximization using the utility function corresponding to the MLE estimate of the linear labor supply function. Over 1000 replications the median value for the IV estimator of the wage elasticity was 120, and the 1 quantile was 100. Thus, the estimate 0718 is far into the lower tail of the Monte Carlo distribution of the IV estimator, so that the bias of IV cannot account for the small value for the elasticity estimator found in the data.

## TABLE I

Power Series

Additional Terms

## CV

E w 1 y J w J y w y y J 2 w J 2 y 2 w 2 y J w J yw 2 y y J 3 w J 3 y 2 w 2 yw y J 2 w J y J w J 2 00472 0313 0305 0323 0369 0364 0350 0364 0331 0263 0252 0372 0761 0760 0763 0543 0659 0628 0636 0845 0775 0714

## SE E

w 0104 0128 0127 0129 0151 0197 0223 0223 0275 0286 0289

## M

0252 0295 0288 0298 0370 0374 0380 0366 0334 0321 0301

## SE M

00721 00979 00998 0103 0101 0101 0102 0103 0103 0103 0112

53 Nonparametric Estimates The strong evidence of misspeciﬁcation that we have found motivates the need for nonparametric estimates in this application. The ﬁrst estimator we consider is that based on power series. It was found that the income elasticity was generally not statistically signiﬁcant, so we report only cross-validation values, wage elasticities, and estimates of the tax change effect (as described in Section 3). Table I gives the results, listing in the left column the additional approximating functions p q p q used for each row. Here m y p w q denotes i m j y j w j − y j+1 w j+1. Also, w 2 is dropped from the third line and w from the fourth line to avoid perfect multicollinearity. We ﬁnd wage elasticities that are much lower than estimated by the MLE. In most cases they are about the size of the IV estimates. Also, the estimates of the tax change effect are very much smaller than the MLE estimate 0546. The last two rows are about 60 percent the size of the MLE. We give most credence to these cases because the number of terms is substantially larger than where the cross-validation criteria is maximized, so that the bias should be smaller than the standard error, as needed for correct asymptotic inference. Although the MLE tax effect standard error is larger than the nonparametric standard errors, a lower bound for the absolute value of a speciﬁcation test can be formed from the difference of the MLE and nonparametric estimates divided by the nonparametric standard error. For the last row of the table the result is 2.19, showing that the nonparametric estimator and MLE are statistically different. To better understand the properties of the power series estimator we carried out a small Monte Carlo study with the same design as for the IV case (i.e. where the true model was the Gaussian MLE and there were 1000 replications). In each replication the number of approximating functions was chosen to be four greater than that which maximized the CV criterion, and the minimum value of K considered was 12. Including so many terms was intended to keep the bias as small as possible. The mean of M was.0507, so that there is about a 10 percent 2472 2473

## TABLE II

Gaussian Power Series

Additional Terms:

1 y J w J w w y J 2 w J 2 2 w 2 y J w J w 2 2 w y J 3 w J 3 2 2 w y J 2 w J y J w J 2 w

## CV

E w

SE w

## M

00472 0292 0280 0270 0299 0172 00929 00391 0231 0137 0303 0277 0372 0826 0822 0810 0797 0675 0786 0799 0819 108 107 105 0104 0123 0124 0133 0132 0142 0201 0202 0200 0244 0246 0254 0252 0347 0344 0340 0348 0339 0343 0345 0331 0300 0295 0262

## SE M

00721 00720 00733 00750 00770 00789 00802 00799 00795 00804 00791 00852 downward bias for the series estimator in this design. Also, the standard error was.0129, while the mean of the asymptotic standard error was.0121, so that there is some downward bias in the asymptotic standard errors. Although a 10 percent bias in the series estimator is not enough to explain the difference between the MLE and nonparametric estimates, it is enough to motivate considering the Gaussian power series estimator, which should be less biased, at least in the Gaussian case. Table II gives results for this estimator, when IV is used to estimate the values that are plugged into the Gaussian power series.

q Here m p w denotes j ˆ j ȳ w̄ m ˆ j y j w j p ˆ j ȳ w j q − ˆ j y j+1, w j+1 p ˆ j ȳ w j+1 q. The estimates M here are similar to those for power series, except that they are slightly smaller and more precisely estimated. To check the potential bias of this estimator, we carried out a Monte Carlo study with the same design as for the power series estimator. We found that the mean of M was.0535, so that the Gaussian power series estimator is much less downward biased than the power series estimator. The estimate of the variance of M was.00845 while the mean of asymptotic standard errors was.00838, which is quite close. Thus, we ﬁnd that the higher precision of the Gaussian power series estimator is present in its ﬁnite sample distribution as well as in the asymptotic standard errors. Overall, the smaller bias, higher precision, and more accurate standard errors lead us to prefer the Gaussian power series estimate, although both nonparametric estimators produce similar M. It is interesting to note that there is little bias in the Gaussian power series despite the presence of nonconvexities in the budget set. Thus, at least for the budget sets in this Swedish data, we ﬁnd that little bias is produced by imposing the convexity restrictions despite the presence of nonconvexity. We also consider a test for this bias by testing for the inclusion of additional terms that do not appear in the convex case. In particular, we added regressors that are the one-third and two-thirds highest kink points for each budget set to the Gaussian power series speciﬁcation with 22 terms. We found a two degree of freedom chisquared test statistic of 3.63. This statistic is not signiﬁcant at conventional levels. We did ﬁnd that M was.0510 with a standard error.0185, a large change in M but with a large standard error. The standard normal Hausman test statistic based on the difference of this estimate with the last row of Table II is 1.51. We also tested for endogeneity of the gross wage using the residual $ ˆ from a regression of the log of the gross wage on a constant, age, number of children, and indicator variables for region of the country where the individual grew up. This regression had an F -statistic of 11.6, indicating that these instruments do help explain wages. We calculated Wald tests for the inclusion of $ ˆ $ ˆ 2, and $ ˆ 3 in the regression of hours on the Gaussian approximating functions, for different numbers of approximating functions. This speciﬁcation restricts the residual $ ˆ to enter in an additive way, and so may not have the best power in cases where it enters nonadditively. The largest value of the test statistic was 6.5, with p-value well over.05. Most of the Wald statistics (for different numbers of approximating terms) were less than 5. Thus, we do not ﬁnd much evidence of endogeneity. Corresponding tests for just a linear term produced even less evidence of endogeneity. It is interesting to consider the source of difference between the MLE and the nonparametric estimates. The M estimates are not very sensitive to the inclusion ˜ of nonlinear terms in the approximation of y w. This suggests that within the utility maximization model the differences between the MLE and nonparametric estimates may result from v and/or being nonnormal. A simple, though crude, estimator of the distribution of v + can be obtained from IV residuals when y w v = c + *y + /w + v. Figure 1 shows a kernel estimator of the density of the IV residual as well as a normal distribution with the same variance. We

Figure 1.—Kernel density estimate for IV residuals.

2474 2475

Figure 2.—Monte Carlo estimate; one replication.

ﬁnd very large departures from normality, with the IV distribution being very much more sharply peaked, and also asymmetric and thick tailed. The small inconsistency of IV and potential lumpiness due to kinks is not large enough to explain these discrepancies, as shown by Figure 2, which gives a typical density function (for one replication) for the IV residuals when the true v and are Gaussian. Thus, these ﬁgures provide evidence against the normality of v and/or, suggesting that MLE using a more ﬂexible distributional speciﬁcation would be useful. Here we have restricted attention to nonparametric estimates because of their relative computational simplicity. The tax reform estimate is about.03 in most of the nonparametric speciﬁcations here. We found similar estimates in earlier work, Blomquist and Newey (1997), using a different method in which we approximate budget sets by ones with only three segments, and then regress labor supply on variables from these approximate budget sets. Thus, the size of the tax reform estimate is even more robust to the form of the nonparametric estimator than is evident in the results here.

6 conclusion In this paper we have proposed a nonparametric model and estimator for labor supply with a nonlinear budget set. We exploit the structure implied by utility maximization to obtain series estimators. These estimators are relatively simple to compute and robust to distributional misspeciﬁcation. We apply our nonparametric method to Swedish data and use the estimated nonparametric function to predict the effect of Swedish tax reform. We compare our method with a parametric maximum likelihood method. Here we ﬁnd large differences between the parametric and nonparametric estimates, with the nonparametric estimate being about 60 percent the size of the parametric one. The designed ﬂexibility of our nonparametric approach lends credence to the idea that the maximum likelihood estimates overstate the size of the effect of Swedish tax reform. The simplicity of our approach, together with its ﬂexibility, should make it a useful alternative to maximum likelihood estimation with nonlinear budget sets. It can be used to construct speciﬁcation tests for the MLE. It is also very easy to compute relative to maximum likelihood, and so would be easy to include in applications to data with nonlinear budget sets. Economics Dept., Uppsala University, Uppsala, Sweden; soren.blomquist@nek. uu.se and Dept. of Economics, MIT, E52-262D, Cambridge, MA 02142-1347, U.S.A.; wnewey@mit.edu.; econ-www.mit.edu/faculty/wnewey/index.htm

February, 1999; ﬁnal revision received January, 2002.

APPENDIX A: Sample Statistics Hours of work are measured in thousands of hours, virtual income in thousands of SEK, and the wage rate in SEK. The marginal wage rates and virtual incomes are calculated at observed hours of work for each individual. The economic variables are expressed in the 1980 price level.

Mean

Variance 1973:

# of observations: 777

Hours of work

Marginal wage rate

Virtual income

Variable 2133 1627 3634 00656 1967 33106 1980:

# of observations: 864

Hours of work

Marginal wage rate

Virtual income 2098 1490 6919 00605 3102 84048 1990:

# of observations: 680

Hours of work

Marginal wage rate

Virtual income 2120 1977 5551 01067 3027 39943

All years combined:

# of observations: 2321

Hours of work

Marginal wage rate

Virtual income 2116 1655 5418 00760 2793 73179 2476 2477

APPENDIX B: 1991 Income Tax System The local income tax was roughly as in 1980. In the federal income tax schedule there was a basic standard deduction of SEK 10,000. For taxable income up to SEK 180,000 the federal tax was zero. For taxable income above 180,000 the federal tax rate was 20%. Denoting labor income by x, taking account of the standard deduction, and deﬂating to the 1980 price level gives the tax schedule.

x −77661 77661−

Marginal tax 0 020 Between 1980 and 1991 there was also a base broadening for the VAT and an increase of the VAT rate from 21.34% to 25%. 7 In crude terms assuming the increase in the VAT tax is completely rolled over onto consumers, the combined effect of the base broadening and increase in the VAT tax rate is equivalent to an increase in proportional income tax with four percentage points. There was also a change in payroll taxes from a rate of 35.25% in 1980 to 37.4% in 1991. The rates are in terms of income net of the payroll tax. Expressed as a percentage of gross labor income the percentages are 26.06% and 27.26% respectively. In Sweden there is a discussion of whether the payroll taxes should be fully regarded as taxes or if some part should be treated as a fee for insurance. Here we treat the payroll taxes as taxes. In crude terms the change in payroll taxes between 1980 and 1991 is equivalent to an increase in a proportional income tax with 1.2 percentage points. The combined effects of the change in VAT and payroll taxes is hence equivalent to an increase of a proportional income tax with 5 percentage points. We treat the changes in the VAT and the payroll tax in a simpliﬁed way and represent the changes as an increase by ﬁve percentage points in a proportional income tax. We then obtain the following tax schedule.

Tax Schedule Including the Effect of Increased VAT and Payroll Taxes x −77661 77661−

Marginal tax 005 025

APPENDIX C: Proofs of Theorems Proof of Theorem 2.1: Let j v = y j w j v. By assumption each j v is strictly increasing in v and j v gv dv is ﬁnite. Desired hours will equal zero if 1 v ≤ 0, i.e. v ≤ 1 −1 0 for 0 = 0. Desired hours will fall on the jth segment if j−1 ≤ j v ≤ l j, i.e. if j −1 j−1 ≤ v ≤ j −1 j. Also, desired hours will be located at the kink j if j v ≥ j and j+1 v ≤ j, i.e. if j −1 j ≤ v ≤ −1 j+1 j. Then for the density gv of v expected hours of work will be h̄x = (7.1)

## J −1

−1 j j j=1 −1 j−1 j +

## −1 J −1

## J

j v gv dv + j −1 j j+1 −1 j j gv dv

J v gv dv −1 y w −1 y w

Deﬁne ay w = − y w v gv dv and by w = − gv dv. By Prh = 0x = 1 −1 1 ¯ J w J − ay J w J J −1.

0, −1 1 v gv dv = ay 1 w 1 1. Also, −1

J v gv dv = y 1 7 0

## J

## J −1

There was a change of the VAT rate in 1980. 21.34% is a weighted average for the year.

Then, it follows from equation (7.1) that h̄x = ay 1 w 1 1 +

## J −1

j=2 ay j w j j − ay j w j j−1 ¯ J w J − ay J w J J −1 + y +

## J −1

j=1 j by j+1 w j+1 j − by j w j j The conclusion then follows from y w = ay w − by w by collecting terms.

## Q.E.D.

Proof of Theorem 2.2: The ﬁrst statement follows similarly to Theorem 2.1 of Newey, Powell, and Vella (1999). To prove the second statement, note ﬁrst that if Y W is not included in the support of y J w J, then any ay w that is nonzero outside the support and zero inside will satisfy Pray J w J = 0 = 1 but ay w is not zero on Y W, contradicting identiﬁcation. Now suppose Y W is not also included in the support of y 1 w 1. Let ay w be an indicator that is zero on the intersection of Y W with the support of y 1 but 1 on that part of Y W that is outside the support of w 1 y 1, and let by w = ay w. Then ay J w J +

## J −1

j=1 by j w j j − by j+1 w j+1 j = ay J w J + ay 1 w 1 − ay J w J = ay 1 w 1 = 0 but ay w is nonzero on part of Y W, contradicting identiﬁcation.

## Q.E.D.

Proof of Theorem 3.1: Let qy w K r denote a three dimensional tensor spline or power series of order r. By Edmunds and Evans (1989) for splines, and by a Taylor expansion for power series, for A as in equation (4.1) there is qy w K r such that for Ly w K r = y w − qy w K r sup Ly w K r ≤ Cr −3A sup L y y w K r ≤ Cr −3A sup L w y w K r ≤ Cr −3A where the supremum is taken over all observable y w. Therefore, it follows that

## J

−1

## J

−1 y j w j j − y j+1 w j+1 j − qy j w j j K r − qy j+1 w j+1 j K r j=1 j=1 ≤

## J −1

j=1 =

## J −1

j=1 Ly j w j j K r − Ly j+1 w j+1 j K r L y y j ∗ w j ∗ j K r y j − y j+1 + L w y j ∗ w j ∗ j K r w j − w j+1 ≤ Cr −3A

## J −1

j=1 y j − y j+1 + w j − w j+1 ≤ 4CMr −3A where the last inequality follows by y j monotonic increasing (in j) and w j monotonic decreasing. Also, by the deﬁnition of p K x and y w three-dimensional, there are constants D and D such that

## J −1

j=1 qy j w j j K r − qy j+1 w j+1 j K r = p K x / K Dr 3 ≤ K ≤ D r 3 It then follows from these last two equations that uniformly in J, (7.2)

## J −1

y j w j j − y j+1 w j+1 j − p K x / K ≤ 4CMD

## A

## K −A

j=1 ¯ J w J − It also follows by a standard approximation results that there is K and C such that y

## Q.E.D.

p K x K ≤ CK −A. The conclusion then follows as in Newey (1997). Proof of Theorem 3.2: Follows from Theorem 1 of Newey (1997).

## Q.E.D.

Proof of Theorem 3.3: Follows from Theorem 2 of Newey (1997).

## Q.E.D.

Proof of Theorem 3.4: Follows from Theorem 3 of Newey (1997).

## Q.E.D.

## REFERENCES

Agell, J., P. Englund, and J. Södersten (1995): Svensk Skattepolitik i Teori och Praktik: 1991 års Skattereform. SOU 1995:104 bilaga 1. Andrews, D. W. K. (1991): “Asymptotic Optimality of Generalized CL, Cross-Validation and Generalized Cross-Validation in Regression with Heteroskedastic Errors,” Journal of Econometrics, 47, 359–377. Aronsson, T., and M. Palme (1998): “A Decade of Tax and Beneﬁt Reforms in Sweden: Effects on Labour Supply, Welfare and Inequality,” Economica, 65, 39–67. Blomquist, S. (1983): “The Effect of Income Taxation on the Labor Supply of Married Women in Sweden,” Journal of Public Economics, 22, 169–197. Blomquist, S., and U. Hansson-Brusewitz (1990): “The Effect of Taxes on Male and Female Labor Supply in Sweden,” Journal of Human Resources, 25, 317–357. Blomquist, S., M. Eklof, and W. K. Newey (2001): “Tax Reform Evaluation Using Nonparametric Methods: Sweden 1980–1991,” Journal of Public Economics, 79, 543–568. Blomquist, S., and W. K. Newey (1997): “Nonparametric Estimation of Labor Supply Functions Generated by Piece Wise Linear Budget Constraints,” Working Paper 1997: 24, Dept. of Economics, Uppsala University. Blundell, R., A. Duncan, and C. Meghir (1998): “Estimating Labour Supply Responses Using Tax Reforms,” Econometrica, 66, 827–861. Blundell, R., and J. L. Powell (2001): “Endogeneity in Nonparametric and Semiparametric Regression Models,” Invited Paper, 2000 World Meeting of the Econometric Society. Brown, B. W., and M. B. Walker (1989): “The Random Utility Hypothesis and Inference on Demand Systems,” Econometrica, 47, 815–829. Burtless, G., and J. Hausman (1978): “The Effect of Taxes on Labor Supply,” Journal of Political Economy, 86, 1103–1130. Edmunds, D. E., and W. Evans (1989): “Entropy Numbers and Approximation Numbers in Function Spaces,” Proceedings of the London Mathematical Society, 58, 137–152. Eissa, N. (1995): “Taxation and Labor Supply of Married Women: The Tax Reform Act of 1986 as a Natural Experiment,” NBER Working Paper #5032. Fritzell, J., and O. Lundberg (1994): Vardagens villkor: Levnadsfforhallanden i Sverige under tre decennier, Brombergs forlag. Hausman, J. (1985): “The Econometrics of Nonlinear Budget Sets,” Econometrica, 53, 1255–1282. Heckman, J. J. (1979): “Sample Selection Bias as Speciﬁcation Error,” Econometrica, 47, 153–161. Ichimura, H. (1993): “Estimation of Single Index Models,” Journal of Econometrics, 58, 71–120. Hoynes, H. (1996): “Welfare Transfers in Two-Parent Families: Labor Supply and Welfare Participation Under the AFDC-UP Program,” Econometrica, 64, 295–332. Keane, M., and R. Mofﬁtt (1998): “A Structural Model of Multiple Welfare Program Participation and Labor Supply,” International Economic Review, 39, 553–589.

Mroz, T. (1987): “The Sensitivity of an Empirical Model of Married Women’s Hours of Work to Economic and Statistical Assumptions,” Econometrica, 55, 765–799. Newey, W. K. (1997): “Convergence Rates and Asymptotic Normality for Series Estimators,” Journal of Econometrics, 79, 147–168. Newey, W. K., and D. McFadden (1994): “Large Sample Estimation and Hypothesis Testing,” Handbook of Econometrics, Volume 4, ed. by R. F. Engle and D. McFadden. Amsterdam: Elsevier. Newey, W. K., J. L., Powell, and F. Vella (1999): “Nonparametric Estimation of Triangular Simultaneous Equations Models,” Econometrica, 67, 567–603. Pierce, D. A. (1982): “The Asymptotic Effect of Substituting Estimators for Parameters in Certain Types of Statistics,” Annals of Statistics, 10, 475–478. Porter, J. (1998): “Nonparametric Estimation with Panel Data,” Working Paper, Department of Economics, Harvard. Stone, C. J. (1982): “Optimal Global Rates of Convergence for Nonparametric Regression,” Annals of Statistics, 10, 1040–1053.

(1985): “Additive Regression and Other Nonparametric Models,” Annals of Statistics, 13, 689–705. White, H. (1980): “Using Least Squares to Approximate Unknown Regression Functions,” International Economic Review, 21, 149–170.

2480
