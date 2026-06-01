# Quantitative Economics 9 (2018), 571–615 1759-7331/20180571

Empirical welfare analysis for discrete choice:

Some general results

Debopam Bhattacharya

Faculty of Economics, University of Cambridge This paper develops nonparametric methods for welfare-analysis of economic changes in the common setting of multinomial choice. The results cover (a) simultaneous price-change of multiple alternatives, (b) introduction/elimination of an option, (c) changes in choice-characteristics, and (d) choice among nonexclusive alternatives. In these cases, Marshallian consumer surplus becomes pathdependent, but Hicksian welfare remains well-defined. We demonstrate that under completely unrestricted preference-heterogeneity and income-effects, the distributions of Hicksian welfare are point-identified from structural choiceprobabilities in scenarios (a), (b), and only set-identified in (c), (d). In programevaluation contexts, our results enable the calculation of compensated-effects, that is, the program’s cash-equivalent and resulting deadweight-loss. They also facilitate a theoretically justified cost-benefit comparison of interventions targeting different outcomes, for example, a tuition-subsidy and a health-product subsidy.

Welfare analyses under endogeneity is briefly discussed. An application to data on choice of fishing-mode illustrates the methods.

Keywords. Multinomial choice, general heterogeneity, income effects, compen-

sating variation, deadweight loss, multiple price change, elimination of alternative, change in characteristics, weak separability, nonexclusive choice, compensated program-effects.

JEL classification. C14, C25, D12, D61, H22.

1. Introduction Welfare calculations, based on the compensating and equivalent variation (CV and EV, henceforth), lie at the heart of economic policy analysis. Although theoretically well understood, these measures are rarely calculated or reported as part of econometric program evaluations. Indeed, empirical studies—both reduced-form and structural— usually adopt a paternalistic view and evaluate a policy intervention in terms of its uncompensated effects on individual outcomes. But they ignore the compensated effects which are required for cost-benefit analysis of the intervention. For example, in an educational context, researchers typically evaluate the impact of a tuition subsidy via its Debopam Bhattacharya: debobhatta@gmail.com I am grateful to Pascaline Dupas, Jerry Hausman, Whitney Newey, and seminar participants at the University of Wisconsin for feedback and suggestions. All errors are mine. This project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 681565).

net effect on college-enrollment (cf. Ichimura and Taber (2002), Kane (2003)). But they stop short of evaluating how much the subsidy is valued by the potential beneficiaries themselves, that is, the lump-sum income transfer that would result in the same individual utilities as the subsidy, and any resulting deadweight loss thereof. 1 The present paper develops methods for calculating such welfare effects as part of program evaluation studies, without imposing restrictive assumptions on the nature of preferenceheterogeneity or income effects. The setting is where we observe individual level data on a cross section of consumers making choices among discrete alternatives, and the goal is to estimate the effects of hypothetical economic changes on consumer welfare. In practical settings, allowing for general heterogeneity in consumer preferences makes empirical welfare analysis a challenging problem. Some advances based on Roy’s identity have recently been made for the case of a continuous good, such as gasoline consumption (cf., Hausman (1981), Hausman and Newey (2016, 2017), Lewbel (2001), Lewbel and Pendakur (2017)). However, many important real-life decisions involve discrete choice, such as college attendance, choice of commuting method, school choice, retirement decisions, and so forth. The Roy’s identity based methods used for continuous choice cannot be applied to these settings, owing to the nonsmoothness of individual demand in price and income. 2 Until recently, available methods for welfare analysis in discrete choice settings were based on restrictive and arbitrary assumptions on preference heterogeneity, for example, quasilinear preferences implying absence of income effects (cf., Domencich and McFadden (1975), Small and Rosen (1981)), or parametrically specified utility functions and heterogeneity distributions (McFadden (1981), Dagsvik and Karlstrom (2005)). Indeed, two key concerns with parametric analyses are (a) model misspecification leading to erroneous substantive conclusions, and (b) identification of welfare distributions solely from functional form assumptions. Recently, Bhattacharya (2015) has shown that for heterogeneous consumers facing the choice between discrete alternatives, the marginal distributions of EV/CV resulting from ceteris paribus price change of a single alternative can be expressed as closed-form transformations of choice probabilities. Taking Bhattacharya (2015) as the point of departure, the present paper makes three new contributions, as follows. Our first set of results, presented in Section 2, concern welfare effects of simultaneous price changes of several alternatives. Multiple price changes are common in real life. For example, a reduction in the ticket price of an airline serving a route is likely 1 Stiglitz (2000, p. 276) noted that empirical researchers typically ignore income effects owing to the perceived difficulty of calculating them, and Goolsbee (1999, p. 10) pointed out that whereas the economic theory of welfare concerns compensated elasticities, common program evaluation studies in public finance typically report uncompensated effects. 2 The closest parallel to Roy’s Identity for discrete choice is the so-called Daly–Williams–Zachary theorem (McFadden, (1981, Section 5.8)), which shows that in an additive random utility model with scalar heterogeneity, the choice probabilities equal certain derivatives of the average indirect utility. Even if we restrict preferences in this way, this result is not useful for analysis of individual welfare distributions, since the income compensation that maintains average utility is not the same as the average of the income compensations that maintain individual utilities, unless preferences are quasilinear. We are interested in the latter distribution, and hence the DWZ theorem is not relevant to our problem.

to lower the prices of competing airlines; a tuition subsidy in an area with prevalence of teenage labor is likely to raise teens’ wages in response; a rise in gasoline prices is likely to raise prices of several transport alternatives, and so on. The impact of such simultaneous price changes on consumer welfare is the key consideration for policymakers in regard to their decision on whether to implement a proposed policy change (cf., Willig, Salop, and Scherer (1991)). We show that under completely general heterogeneity, money-metric welfare effects of such price changes continue to remain welldefined, whereas the analog of the Marshallian Consumer Surplus becomes path dependent (Proposition 1). Furthermore, EV/CV distributions in this case are expressible as closed-form transformations of estimable choice probabilities (Theorem 1). These results cover situations where some price changes are negative, some zero and some positive. A key issue here, elaborated in Section 2.1 below, is that although welfare effects of multiple price changes are well-defined, their distributions cannot be obtained by iterating results for a single price change. This is because the income at which welfare distributions are to be evaluated varies in an unobservable way across individuals from the second iteration onward, due to unobservable preference heterogeneity, and thus cannot be conditioned on. Consequently, new results are required for welfare analysis in these situations. For welfare evaluations in applications, it has been common practice to use the socalled log-sum formula (cf., Small and Rosen (1981), Train (2009)), which relies on strong parametric assumptions regarding both preferences and heterogeneity; see Carneiro, Das, and Reis (2016) and Knittel and Metaxoglou (2014) for some applications. 3 Here, we show that under completely general preference heterogeneity and income effects, one can express welfare distributions resulting from multiple simultaneous price changes in terms of simple transformations of choice probability functions, thereby reducing welfare analysis to the problem of estimating choice probabilities. Crucially, our welfare expressions (a) hold when income effects are nonnegligible, as is likely for bigger purchases like children’s education and consumer durables, and (b) apply to arbitrary patterns of price changes across alternatives, thereby making the results useful across a wide range of empirical situations. The above results are also shown to imply the distribution of welfare loss resulting from elimination of an existing alternative, or equivalently, retrospective welfare gain from having added a new alternative to the choice set. Previous econometric studies of such problems either ignored consumer heterogeneity, and implicitly assumed a “representative consumer” model, and/or worked under restrictive parametric assumptions (Willig, Salop, and Scherer (1991), Hausman (1996), Hausman and Leonard (2002), Hausman (2003), Trajtenberg (1989)). In contrast, our set-up allows for (a) unrestricted consumer heterogeneity, and (b) arbitrary effects of eliminating the alternative on the 3 Some of these restrictive assumptions have subsequently been replaced with less stringent parametric assumptions; cf. Herriges and Kling (1999), McFadden and Train (2000), Dagsvik and Karlstrom (2005), and Goolsbee and Klenow (2006). All of these still require specification of the dimension and distribution of unobserved heterogeneity and functional form of utility functions, about which no a priori information is available. Indeed, all welfare related measures are identified in these settings solely from assumed knowledge of these functional forms.

price of existing alternatives, thus greatly increasing the scope of the results. 4 Importantly, these results are robust to failure of parametric assumptions, and clarify which features of welfare distributions can and which ones cannot be learned from demand data alone without functional form assumptions. Indeed, we show below that Hicksian welfare distributions in this case can again be expressed as closed-form transformations of choice probabilities without any assumption on heterogeneity. Nonetheless, calculating the tails of these distributions require observation of demand at prices where aggregate demand at an adjusted income level reaches zero. At high income levels, such prices may not be observed, since producers have no incentive to set a price where aggregate demand is zero. In that case, a lower bound on the welfare distributions can be obtained using the value of aggregate demand at the highest observed price. 5 A heuristic empirical practice, popular in empirical research, for calculating welfare effects of new goods involves integrating the choice probability function from the current price to infinity. We provide a formal justification of this ad hoc practice, and show that this does indeed yield the average EV, if prices of substitutes remain unchanged; however, calculation of the average CV and/or allowing for prices of substitutes to change entail different expressions. Section 3 of this paper considers two extensions, namely welfare analysis for (i) change in characteristics of an alternative, with or without an accompanying price change, and (ii) multinomial choice with nonexclusive options. An example of the former is the classic transport choice setting where, say, increasing the frequency of buses would raise utility from choosing the bus option, as opposed to driving or walking. Typically, characteristics of alternatives do not appear as additive components of net income in utilities, unlike prices (via the budget constraint), and hence the price change results are not useful for analyzing welfare effects of quality changes. We show that typically such welfare distributions are not identified from structural choice probabilities; nonetheless, bounds can be constructed on them, and hence on average welfare. We also show that further restrictions on preferences, such as weak separability of heterogeneity, restores point identification. Our second extension pertains to choice among nonexclusive options. An example is where a cable-TV company offering a sports package and a movie package raises product prices; the resulting welfare calculations require new results because the packages are not exclusive alternatives for a potential consumer. We show that the welfare distribution resulting from a single price change can be directly expressed as a closed-form functional of choice probabilities but that for multiple price changes it cannot, unlike the case of multinomial choice among exclusive options. We then show how to construct nonparametric bounds for these distributions. Taken together, these results provide new insights into welfare analysis in practical discrete choice situations, as well as providing practitioners with useful empirical tools 4 Welfare calculations in the two scenarios described above correspond to situations where the price vectors before and after are given. The process through which the final price vector following the relevant change is calculated requires modeling the supply side; see Hausman and Leonard (2002, pp. 256–258), for an illustration of the methodology. 5 For common parametric models, like mixed logit, these issues are assumed away, and welfare distributions are point-identified simply via functional form assumptions.

for evaluating policy changes in real life settings. In Section 4, we discuss some issues related to practical implementation of our results, and state a new and useful finding, namely that under income endogeneity and corresponding to a price increase, the EV but not the CV can be used for legitimate welfare analysis even in the absence of instruments or control functions. Section 5 provides an empirical illustration of our methods in a setting of multinomial choice among modes of fishing. Using microdata, previously analyzed in Herriges and Kling (1999), we conduct private welfare analysis of price and quality changes, and the elimination of choice alternatives (e.g., for environmental protection). We show that logsum based estimates are substantively very different from those obtained using our methods. In particular, our estimates vary much less with income, and more importantly, have an income-gradient of the opposite sign, implying the exact opposite conclusion regarding progressivity of the economic changes, compared with the logsum estimates. The proofs of all theoretical results are provided in the Appendix.

2. Multiple price changes Set-up and notation: Consider a multinomial choice situation where alternatives are indexed by j = 1 J; individual income is denoted by Y, and price of alternative j by P j. Individual utility from choosing alternative j is U j (Y − P j η), j = 1 J, where η denotes individual heterogeneity of unknown dimension; η is distributed in the population with unknown marginal CDF F η (·). We have a cross-sectional random sample of consumers, and observe their characteristics including income, the prices they face, and the choice they make. The following analysis implicitly conditions on observable nonincome characteristics. Define the structural choice probability for alternative j evaluated at price vector p and income y, denoted {q j (p y)}, j = 1 J, as (1) q j (p y) = 1 U j (y − p j r) > max U k (y − p k r) dF η (r) k= j In words, if we randomly sample individuals from the population, and offer the price vector p and income y to each sampled individual, then a fraction q j (p y) will choose alternative j, in expectation. Assumption 1. Assume that for each η and for each j = 1 J, the utility function U j (· η) is continuous and strictly increasing. The first part of Assumption 1 simply says that utilities are nonsatiated with respect to the numeraire. Note that this assumption leaves the dimension of heterogeneity completely unspecified, and says nothing about how utility changes with unobserved heterogeneity. Now consider a hypothetical change in the price vector from p 0 ≡ (p 10 p 20 p J0) to p 1 ≡ (p 11 p 21 p J1 ). Then the EV at income y for an η type consumer is the income reduction S in the initial situation that would lead to attainment of the eventual indirect utility. Formally, the EV is the solution S to the equation:

max U 1 (y − p 11 η) U 2 (y − p 21 η) U J (y − p J1 η) = max U 1 (y − S − p 10 η) U 2 (y − p 20 − S η) U J (y − p J0 − S η) (2) Similarly, the CV is the income compensation in the eventual situation necessary to restore the initial indirect utility; formally, the CV is the solution S to the equation:

max U 1 (y + S − p 11 η) U 2 (y + S − p 21 η) U J (y + S − p J1 η) = max U 1 (y − p 10 η) U 2 (y − p 20 η) U J (y − p J0 η) (3) As η varies in the population, the CV and EV will have a distribution across consumers. Our goal is to estimate these distribution functions using the cross-sectional dataset. Note that by analogy with the single price change case, one can attempt to define the change in average Marshallian consumer surplus in the multiple price change case via the line-integral

## CS(L) = −

## J

q j (p y) dp j (4)

L j=1 where L denotes a path from p 0 to p 1 (cf. Auerbach (1985, equation (2.2))). The negative sign stems from the fact that rise in price leads to a loss in consumer surplus. In the set-up described above, we first show that for arbitrary price changes, the EV and CV are well-defined under Assumption 1, but the Marshallian Consumer Surplus is not. We then show why one cannot get welfare distributions for multiple price changes by iterating a simpler result for a single price change, and then establish the first main result of this paper, namely that the marginal distributions of individual-level EV and CV for arbitrary changes in the price vector can be obtained as closed-form functionals of the structural choice probabilities. We will assume without loss of generality that p J1 − p J0 ≥ p J−11 − p J−10 ≥ · · · ≥ p 11 − p 10 (5) That is, label the alternative with the smallest price change (the smallest could be a negative number, representing a fall in price) alternative 1, the next smallest as alternative 2 and so on. Now, it is well known that for continuous choice with multiple prices changing simultaneously, the Marshallian Consumer Surplus is generically undefined in the sense that the corresponding line-integral is path-dependent, but the Hicksian CV and EV continue to remain well-defined (cf., Tirole (1988, p. 11)). Our first result establishes that the same conclusion holds for discrete choice.

Proposition 1. Consider the multinomial choice set-up with J alternatives. Consider a price change from p 0 ≡ (p 10 p 20 p J0) to p 1 ≡ (p 11 p 21 p J1 ). Under Assumption 1, the individual compensating and equivalent variations are uniquely defined.

Proof. Let p 0 = (p 10 p 20 p J0) denote the initial price vector and p 1 = (p 11 p 21 p J1) denote the final price vector. By definition, max U 1 (y − p 11 η) U J (y − p J1 η) (6) = max U 1 (y − p 10 − S η) U J (y − p J0 − S η) Since each U j (· η) is continuous, the RHS must be continuous in S. Now, if S < p 11 −p 10, then the RHS will be larger than the LHS, and if S > p J1 − p J0, then the RHS will be smaller than the LHS. By continuity and the intermediate value theorem, there must exist at least one S that solves (6). Now, since each U j (· η) is strictly increasing, the RHS of (6) is strictly decreasing in S. Therefore, the solution must be unique. An exactly analogous argument works for the CV where the corresponding equality is max U 1 (y − p 11 + S η) U J (y − p J1 + S η) (7) = max U 1 (y − p 10 η) U J (y − p J0 η) Marshallian consumer surplus: It can be shown that for discrete choice with multiple price changes, the integral (4) is path-dependent. In the Appendix, we demonstrate this for the case with 3 alternatives.

## 2.1 Welfare distributions for multiple price changes

Bhattacharya (2015) showed that in the above setting, when the price of a single alternative changes ceteris paribus, the resulting CV and EV distributions can be expressed as closed-form functionals of choice probabilities. Interestingly, one cannot iterate this single price change result to obtain the welfare distribution for simultaneous changes in the prices of multiple alternatives. This fact is shown in the Appendix. Consequently, an independent result is required for welfare analysis corresponding to simultaneous changes in multiple prices, and it is given by the following theorem. Theorem 1. Consider the multinomial choice set up with J exclusive alternatives. Consider a price change from p 0 ≡ (p 10 p 20 p J0) to p 1 ≡ (p 11 p 21 p J1) satisfying (5). Denote p j1 − p j0 by p j for j = 1 J. Under Assumption 1, the marginal distribution of the individual EV evaluated at income y is given by

Pr(EV ≤ a) ⎧ ⎪ 0 if a < p 1 ⎪ ⎪ ⎪ ⎪ j ⎪ ⎪ p 11 p j1 ⎪ ⎪ q k ⎪ ⎪ ⎪ p j+10 + a p J0 + a y ⎪ ⎪ k=1 ⎪ ⎪ ⎨ if p ≤ a < p a ≥ 0 1 ≤ j ≤ J − 1 j j+1 = j ⎪ ⎪ p 11 − a p j1 − a ⎪ ⎪ q k ⎪ ⎪ p j+10 p J0 y − a ⎪ ⎪ k=1 ⎪ ⎪ ⎪ ⎪ ⎪ if p j ≤ a < p j+1 a < 0 1 ≤ j ≤ J − 1 ⎪ ⎪ ⎪ ⎩ 1 if a ≥ p

## J

(8) while that of the individual CV evaluated at income y is given by

Pr(CV ≤ a) ⎧ ⎪ 0 if a < p 1 ⎪ ⎪ ⎪ ⎪ j ⎪ ⎪ p 11 p j1 ⎪ ⎪ q k ⎪ ⎪ ⎪ p j+10 + a p J0 + a y + a ⎪ k=1 ⎪ ⎪ ⎪ ⎨ if p ≤ a < p a ≥ 0 1 ≤ j ≤ J − 1 j j+1 = j ⎪ ⎪ p 11 − a p j1 − a ⎪ ⎪ q k ⎪ ⎪ p j+10 p J0 y ⎪ ⎪ k=1 ⎪ ⎪ ⎪ ⎪ ⎪ if p j ≤ a < p j+1 a < 0 1 ≤ j ≤ J − 1 ⎪ ⎪ ⎪ ⎩ 1 if a ≥ p (9)

## J

where q k s are defined above in equation (1). (The separate entries for a ≥ 0 and a < 0 in each line of (8) and (9) arise from accommodating rise and fall of prices, respectively).

These distributional results cover positive, zero, and negative price changes. For example, in the 3-alternative case, suppose alternative 2 is the outside option with price p 21 = p 20 = 0, and p 1 < 0 < p 3, then (8) becomes ⎧ ⎪ 0 ⎪ ⎪ ⎪ ⎨ q (p − a 0 p y − a) 1 11 30

Pr(EV ≤ a) = ⎪ q 1 (p 11 0 p 30 + a y) + q 1 (p 11 0 p 30 + a y) ⎪ ⎪ ⎪ ⎩ 1 if a < p 1 if p 1 ≤ a < 0 if 0 ≤ a < p 3 (10) if a ≥ p 3 Finally, note that in the above results, Assumption 1 guarantees that the CDFs are non-decreasing. For instance, in the 3-alternative case, for the CV we require q 1 (p 11 p 20 + a p 30 + a y + a) ≤ q 1 p 11 p 20 + a p 30 + a y + a (11) whenever p 11 − p 10 ≤ a < a. But this is true because the LHS is the probability of the event U 1 (y + a − p 11 η) ≥ max U 2 (y − p 20 η) U 3 (y − p 30 η) ⇒ U 1 y + a − p 11 η ≥ max U 2 (y − p 20 η) U 3 (y − p 30 η) U 2 y + a − p 20 + a η ⇐⇒ U 1 y + a − p 11 η ≥ max U 3 y + a − p 30 + a η whose probability is the RHS of the previous display.

since a > a Remark 1. It is implicit throughout that the price changes do not alter the distribution of heterogeneity, for example, a large tuition subsidy in a district might attract outsiders with a strong preference for education to migrate in, altering the distribution of preferences relative to the status-quo. In other words, the price changes considered here are assumed to be modest enough to have no impact on the distribution of η, as is implicitly assumed in this literature.

The expected welfare change and deadweight loss follow from the CDF. For example, if (10) results from a subsidy |p 1 | on alternative 1, and a tax p 3 on alternative 3, then E(Deadwt_Loss) = E(EV) − p 1 × q 1 (p 11 0 p 31 y) − p 3 × q 3 (p 11 0 p 31 y + p 3)

## 2.2 Elimination of an alternative

Consider a setting of multinomial choice among exclusive alternatives {1 J + 1}. Suppose the alternative J + 1 is eliminated subsequently, which can potentially affect consumer welfare by both restricting the choice set and also by affecting the prices of other alternatives. Assume that we have data on a cross section of individual choices in the preelimination situation. We wish to calculate the distribution of Hicksian welfare effects that would result from eliminating the J + 1th alternative. Applied researchers typically use the heuristic idea that eliminating an alternative is “like” raising its price to infinity, and thereafter use the welfare formulae for price change to evaluate welfare effects of eliminating an alternative. Our analysis below provides a formal justification for this heuristic approach, and shows that it is valid only when prices of other alternatives do not change and when one is interested in the EV. Furthermore, the incorporation of preference heterogeneity and income effects reveals interesting differences between CV and EV based formulae and identifiability of their distribution. Toward that end, consider an individual at income y and unobserved heterogeneity η whose utility from consuming alternative j at price p j is given by U j (y − p j η). The problem is to find the distribution of welfare effects across such individuals resulting from potentially eliminating alternative J + 1. Suppose from an initial price vector (p 10 p J0 p J+1 ), following elimination of the J + 1th alternative, the eventual price vector becomes (p 11 p J1 ). The marginal distributions of EV and CV resulting from this change are given by the following corollary, whose proof appears in the Appendix.

Corollary 1. Suppose Assumption 1 holds for all alternatives. Also assume that for any bundle (j y − p j ), if p j ↑ ∞ with prices of other alternatives finite, then for each η at least one other bundle (k y − p k) will be strictly preferred to (j y − p j ). Let q k (· · y) be as defined in (1), with J + 1 alternatives. Then

Pr(CV ≤ a) ⎧ ⎪ 0 if a < p 1 ⎪ ⎪ ⎞ ⎛ ⎪ ⎪ ⎪ j p p ⎪ 11 j1 ⎜ ⎪ ⎪ ⎟ ⎪ ⎪ q k ⎝ p j+10 + a p J0 + a p J+1 + a ⎠ ⎪ ⎪ ⎪ ⎪ k=1 y + a ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ if p j ≤ a < p j+1 j = 1 J − 1 a ≥ 0 j = ⎪ p 11 − a p j1 − a ⎪ ⎪ q k ⎪ ⎪ p j+10 p J0 p J+1 y ⎪ ⎪ k=1 ⎪ ⎪ ⎪ ⎪ if p j ≤ a < p j+1 1 ≤ j < J − 1 a < 0 ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ 1 − q J+1 (p 11 p J1 p J+1 + a y + a) if p J ≤ a a ≥ 0 ⎪ ⎪ ⎪ ⎩ 1 − q (p − a p − a p y) if p ≤ a < 0

## J

## J+1

11

## J1

## J+1

(12)

On the other hand,

Pr(EV ≤ a) ⎧ ⎪ 0 if a < p 11 − p 10 ⎪ ⎪ ⎪ j ⎪ ⎪ ⎪ p 11 p j1 ⎪ ⎪ q k ⎪ ⎪ p j+10 + a p J0 + a p J+1 + a y ⎪ k=1 ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ if p j ≤ a < p j+1 j = 1 J − 1 a ≥ 0 j = p 11 − a p j1 − a ⎪ q k ⎪ ⎪ ⎪ p j+10 p J0 p J+1 y − a ⎪ ⎪ k=1 ⎪ ⎪ ⎪ ⎪ if p j ≤ a < p j+1 1 ≤ j < J − 1 a < 0 ⎪ ⎪ ⎪ ⎪ ⎪ 1 − q J+1 (p 11 p J1 p J+1 + a y) if p J ≤ a a ≥ 0 ⎪ ⎪ ⎪ ⎩ 1 − q J+1 (p 11 − a p J1 − a p J+1 y − a) if p J ≤ a < 0 (13) As in the previous theorem, the pairs of results for a < 0 and a ≥ 0 correspond to which existing alternatives have become more and less expensive, respectively, following the elimination of the J + 1th alternative. Also, note that in order to calculate the probabilities appearing in Theorem 2, we need to observe adequate cross-sectional variation in the price of all J + 1 alternatives in the preelimination period. Corollary 2. If elimination of the alternative has no effect on prices of the other alternatives, then p j1 = p j0 for all j = 1 J, and the above results simplify to 0 if a < 0

Pr(CV ≤ a) = (14) 1 − q J+1 (p 10 p J0 p J+1 + a y + a) if 0 ≤ a 0 if a < 0 (15)

Pr(EV ≤ a) = 1 − q J+1 (p 10 p J0 p J+1 + a y) if 0 ≤ a

The corresponding average values are given by ∞ q J+1 (p 10 p J0 r y + r − p J+1) dr

## E(EV) =

(16) p J+1 ∞ q J+1 (p 10 p J0 r y) dr (17) p J+1 using the change of variable r = p J+1 + a. The expression (17) is commonly used as an ad hoc measure of the welfare effect of introducing a new product. Thus it follows from the above discussion that if elimination of the alternative entails no price change for the other alternatives, then the commonly used expression happens to equal the mean EV, but ceases to be so if one is interested in the mean CV, or prices of substitutes also change. In order to calculate the above expressions nonparametrically, a researcher needs to observe demand up to the price where the choice probability becomes zero. Typically, in a dataset, one is unlikely to observe such prices, since producers have no incentive to raise prices where revenue is zero. But then one can obtain a lower bound for E(CV) by integrating up to the highest price observed in the dataset where demand from consumers is nonzero. This is in contrast to the case of price changes for multiple alternatives, reported in equation (8) above, where welfare distributions are nonparametrically identified as long as the hypothetical price changes are within the range of the observed price data. Of course, for parametric choice probabilities, for example, random coefficient logit, expressions like (17) are identified directly from functional form assumptions. Finally, note that the above expressions can also be used for retrospective calculation of welfare distributions corresponding to introduction of a new alternative, simply by interchanging the labels of EV and CV. Here, “retrospective” means that we must have consumption data after the product has been introduced.

3. Two extensions In this section, we develop results for nonparametric welfare analysis in two practically important settings, namely (i) quality change in an alternative, and (ii) price changes when alternatives are nonexclusive. In these two cases, in general, one cannot express the distribution of welfare using functionals of structural choice probabilities; nonetheless, bounds can be constructed on the welfare distribution functions, and thus, on average welfare, as shown below.

## 3.1 Change in characteristics

The first setting we consider is where characteristics of a choice alternative changes. For example, consider a household in a poor country that is deciding whether to send its teenage daughter to school, or to let her stay at home. It is intuitive that the teacher student ratio in the local school would be an important determinant of the utility from school attendance. Similarly, in transportation choice settings, increasing the frequency of buses would raise every individual’s utility from choosing the bus option, as opposed to driving or walking. These characteristics, unlike prices, do not appear as additive components of net income inside utilities. The additivity of price, resulting from the budget constraint, was instrumental in deriving the results of the previous section. Therefore, welfare analysis of changes in characteristics would require a result that is different from those above. In this subsection, we develop such a result. To keep the exposition transparent, we will focus on binary choice, and then outline how to generalize to the multinomial case. Accordingly, suppose an individual at income y and preference η is choosing between two options 0 and 1, with utilities given by U 0 (y η) and U 1 (y − p x η), where x represents a vector of characteristics of option 1. For example, in the schooling example, option 0 is staying at home, option 1 is going to school, p is the tuition fee, and x is the teacher-student ratio in the local school. Define the structural choice probability of alternative 1 at price p, income y and quality x as q 1 (p y x) = 1 U 1 (y − p x r) > U 0 (y r) dF η (r) (18) where F η (·) represents the marginal distribution of unobserved heterogeneity. We will make the following assumption.

Assumption 2. (i) For each x and η, U 1 (· x η) is strictly increasing and continuous; additionally, for each η. U 0 (· η) is strictly increasing and continuous.

Now, suppose from an initial price p 0 and initial quality x 0, the price and attribute change to p 1 and x 1, respectively. It is reasonable to assume that improvement of quality will be funded, at least partially, by an increase in prices, and hence we consider p 1 ≥ p 0. Setting p 1 = p 0, we can cover the case where there is no change in price, for example, the improvement is funded by external resources. The private CV resulting from this change is defined by the solution S to the equation max U 0 (y η) U 1 (y − p 0 x 0 η) = max U 0 (y + S η) U 1 (y + S − p 1 x 1 η) (19) Our first result is that the distribution of S cannot be identified from knowledge of the structural choice probabilities. We demonstrate this in the Appendix via a counterexample, and state the conclusion as a theorem.

Theorem 2. Under Assumption 2, the marginal distribution of S is not identified from the structural choice probabilities (the proof is in the Appendix).

One can, of course, construct bounds on these distributions, which are provided in Propositions 2 and 3 in the Appendix. To see where these bounds come from, note from (19) and Assumption 2(i), that for a < 0,

Pr(CV ≤ a) ⎡ ⎤ max U 0 (y η) U 1 (y − p 0 x 0 η) ⎢ ⎥ ⎥ = Pr ⎢ ⎣ ≤ max U 0 (y + a η) U 1 (y + a − p 1 x 1 η) ⎦ <y "

# = Pr max U 0 (y η) U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) The Frechet upper bound on this is given by # "

Pr U 0 (y η) ≤ U 1 (y + a − p 1 x 1 η) min # "

Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) q 1 (p 1 − a y x 1) = min # "

Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) The ultimate upper bound comes from a lower bound on Pr[U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η)], obtained using # "

Pr U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η) "

# ≥ max Pr U 1 (y − p 0 x 0 η) ≥ U 0 y η ≥ U 1 (y + a − p 1 x 1 η) y and then applying Frechet bounds to this. In the application below, we provide explicit numerical expressions for these bounds. It is straightforward to extend the above result to the case of multinomial choice. Formally, if we have alternatives 0 1 J with the quality of alternative 1 changing from x 10 to x 11, and price changing form p 0 to p 1, then the CV solves max U 0 (y η) U 1 (y − p 0 x 10 η) U 2 (y − p 2 x 2 η) U J (y − p J x J η) U 0 (y + S η) U 1 (y + S − p 1 x 11 η) = max U 2 (y + S − p 2 x 2 η) U J (y + S − p J x J η)

Letting U −1 (y p x η) ≡ max U 0 (y η) U 2 (y − p 2 x 2 η) U J (y − p J x J η) the previous display reduces to max U −1 (y p x η) U 1 (y − p 0 x 10 η) = max U −1 (y + S p x η) U 1 (y + S − p 1 x 11 η) which is the same as (19) with U 0 (y η) replaced by U −1 (y p x η). The corresponding bounds on the CV distribution (see equation (44) in the Appendix) would involve replacing q 0 (·)s with the probability of not buying alternative 1.

Remark 2. Defining and proving “sharpness” of such bounds without any assumptions on the structure of preferences and dimension of heterogeneity (except Assumption 2) would be an interesting exercise. We believe that such results are best developed as corollaries of some fundamental revealed preference type results, related to McFadden and Richter (1990). As such, there is sufficient material here for an independent paper. We are currently exploring these and some related questions in a separate project. We conclude this subsection with the observation that further restrictions on preferences, though short of fully parametric specifications, can yield point-identification of welfare distributions for quality change. One such restriction is that the utility from alternative 1 is weakly separable in unobserved heterogeneity, that is, U 1 (y − p x η) ≡ V 1 (h 1 (y − p x) η), where V 1 (· η) is strictly increasing for each η, and h 1 (· ·) is continuous and strictly increasing in the first component. A special case of weak separability, where the functional form of h 1 (· ·) is assumed known up to estimable real parameters is the familiar “index restriction,” popular in the semiparametrics literature. Weak separability has been used previously in econometrics for identifying effects of endogenous dummy variables (cf. Vytlacil and Yildiz (2007)), while index restrictions have been used for achieving identification in general demand systems; cf. Berry and Haile (2015). Consider a change from (p 0 x 0) to (p 1 x 1) satisfying the following condition. Condition S. Assume that the change from (p 0 x 0) to (p 1 x 1) is small enough that there exists a finite a satisfying h 1 (y + a − p 1 x 1) = h 1 (y − p 0 x 0) This basically says that the quality and price change are not so large that no amount of compensation can restore the utility from consuming alternative 1 to the prechange level for any η. Proposition 2. Suppose weak separability holds. Consider a change from (p 0 x 0) to (p 1 x 1) satisfying condition (S). Then there is a unique ā that solves q 1 (p 1 − ā y x 1) = q 1 (p 0 y x 0 ). Furthermore, the distribution of individual CV resulting from this change is point-identified from the structural choice probabilities, and it is given by the following expressions: If ā ≤ 0, then ⎧ ⎪ if a < ā ⎪ ⎨ 0 Pr(S ≤ a) = q 1 (p 1 − a y x 1) if ā ≤ a < 0 ⎪ ⎪ ⎩ 1 if a ≥ 0

If ā > 0, then ⎧ ⎪ if a < 0 ⎪ ⎨ 0 Pr(S ≤ a) = q 0 (p 0 + a y + a x 0) if 0 ≤ a < ā ⎪ ⎪ ⎩ 1 if a ≥ ā (The proof is in the Appendix.) Assume that there are two binary choices which are nonexclusive among themselves. For example, suppose choice 1 for a household is whether to subscribe to a sports package offered by a cable TV network which costs P 1 and choice 2 is whether to subscribe to a movie package which costs P 2. A household with income Y and preferences η then has four exclusive options—{1}, {2}, {1 2}, {0} (where {0} denotes choosing none of the two packages) with respective utilities U 1 (Y − P 1 η), U 2 (Y − P 2 η), U 12 (Y − P 1 − P 2 η), and U 0 (Y η), respectively. Single price change: Consider the CV corresponding to a rise in the price of the sports package from p 10 to p 11 with the price of the movie package fixed at p 2. The CV evaluated at income Y = y is the solution to the equation max U 0 (y + CV η) U 1 (y + CV − p 11 η) U 2 (y + CV − p 2 η) U 12 (y + CV − p 11 − p 2 η) U 0 (y η) U 1 (y − p 10 η) = max U 2 (y − p 2 η) U 12 (y − p 10 − p 2 η) (20) Now, group option {1} and {1 2} together (call it group A) and options {0} and {2} together and call it group B. Define def ε = (p 2 η) def V A (y − p 1 ε) = max U 1 (y − p 1 η) U 12 (y − p 1 − p 2 η) def V B (y ε) = max U 0 (y η) U 2 (y − p 2 η)

Then (20) becomes max V A (y + CV − p 11 ε) V B (y + CV ε) = max V A (y − p 10 ε) V B (y ε) (21) If the U functions are strictly increasing in the first argument for each η, then so are V A (· ε) and V B (· ε) for each ε. Now we can apply Theorem 1 of Bhattacharya (2015) for binary choice to this problem and get the marginal distribution of the compensating variation. For example, for 0 ≤ a < p 11 − p 10, Theorem 1 of Bhattacharya (2015) gives

Pr(CV ≤ a) "

# = Pr V B (y + a ε) ≥ V A y + a − (p 10 + a) ε ⎡ ⎤ max U 0 (y + a η) U 2 (y + a − p 2 η) ⎢ ⎥ ⎢ ⎥ = Pr ⎢ ⎥ U 1 y + a − (p 10 + a) η ⎣ ≥ max ⎦ U 12 y + a − (p 10 + a) − p 2 η = q 0 (p 10 + a p 2 y + a) + q 2 (p 10 + a p 2 y + a)

Thus ⎧ ⎪ ⎪ ⎨ 0 Pr(CV ≤ a) = q 0 (p 10 + a p 2 y + a) + q 2 (p 10 + a p 2 y + a) ⎪ ⎪ ⎩ 1 if a < 0 if 0 ≤ a < p 11 − p 10 if a ≥ p 11 − p 10 Multiple price changes: The key fact enabling us to write (20) as the binary choice CV (21) is that P 2 is being held fixed at p 2; if P 2 also varied across individuals, then the distribution of ε would vary beyond the variation of η and the binary formulation would no longer be applicable. Indeed, for multiple price changes in the nonexclusive alternatives case, welfare distributions can no longer be written in terms of choice probabilities. To see this, consider a simultaneous rise in P 1 and P 2 from (p 10 p 20) to (p 11 p 21 ). Assume that 0 < p 11 − p 10 < p 21 − p 20. Then the CV is defined via U 0 (y + CV η) U 1 (y + CV − p 11 η) max U 2 (y + CV − p 21 η) U 12 (y + CV − p 11 − p 21 η) = max U 0 (y η) U 1 (y − p 10 η) U 2 (y − p 20 η) U 12 (y − p 10 − p 20 η)

Now,

Pr[CV = p 11 − p 10] ⎡ ⎫ ⎤ ⎧ U 0 (y η) U 2 (y − p 20 η) ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎥ ⎪ ⎪ ⎢ ⎪ ⎪ ⎥ ⎪ ⎪ ⎢ ⎪ ⎪

## U

(y − p − p η) ⎥ ⎪ ⎪ 12 ⎢ 10 20 ⎪ ⎪ ⎬ ⎥ ⎨ ⎢ ⎥ ⎢ = Pr ⎢ U 1 (y − p 10 η) ≥ max U 0 (y + p 11 − p 10 η) ⎥ ⎥ ⎪ ⎪ ⎢ ⎪ ⎪ ⎥ ⎪ ⎪ ⎢ ⎪ ⎪ ⎥ ⎪ ⎪ ⎢

## U

(y + p − p − p η) 2 11 10 21 ⎪ ⎪ ⎪ ⎪ ⎦ ⎣ ⎪ ⎪ ⎪ ⎪ ⎭ ⎩ U 12 (y − p 10 − p 21 η) ' ( U 2 (y − p 20 η) U 12 (y − p 10 − p 20 η) = Pr U 1 (y − p 10 η) ≥ max U 0 (y + p 11 − p 10 η) (22) This probability is not generically point-identified from the choice probabilities. To see this, consider the following counterexample. Counterexample: Consider a classic McFadden (1973) type utility specification: U j (a η) = β j a + η j, for j = 0 1 2 12, where the β j are nonstochastic coefficients, and the ηs are distributed standardized extreme valued. Then because the regressors (y y − p 1 y − p 2 y + p 1 − p 2) constitute a 3-dimensional subspace—the sum of the 1st and the 4th regressors equals the sum of the 2nd and the 3rd implying exact multicollinearity—the 4 coefficients (β 0 β 1 β 2 β 12) are not separately identified. A direct way to verify this is to note that the Hessian of the likelihood function is of the form W ⊗ XX, where X ≡ (y y − p 10 y − p 20 y − p 10 − p 20) (cf. Böhning (1992, pp. 198–199)), and so its expectation is of the form E(W ⊗ XX ). Given that the 4th component of X is an exact linear combination of the first 3, in each block E(W ij XX) of the Kronecker product the 4th row is exactly the same linear combination of the first 3 rows. So it follows that E(W ⊗ XX) is globally singular. Therefore, by Rothenberg (1971, Theorem 1), the parameter vector β is not even locally identified. Now the expression for Pr[CV = p 11 − p 10] in this case equals q 1 (y + p 11 − p 10 y − p 10 y − p 20 y − p 10 − p 20) exp β 1 (y − p 10) = exp β 0 (y + p 11 − p 10) + exp β 1 (y − p 10) + exp β 2 (y − p 20) + exp β 12 (y − p 10 − p 20) (23) Since x ≡ (y + p 11 − p 10 y − p 10 y − p 20 y − p 10 − p 20) spans a 4-dimensional space (unless p 11 = p 10 ), we cannot have that for some θ = β, q 1 (y + p 11 − p 10 y − p 10 y − p 20 y − p 10 − p 20; β) = q 1 (y + p 11 − p 10 y − p 10 y − p 20 y − p 10 − p 20; θ) for all p 10, p 11, p 20, y, if the joint distribution of (p 10 p 11 p 20 y) is nondegenerate. To see this explicitly, consider the following thought experiment. Suppose at a specific value x of the regressors, q 1 (x β) = q 1 (x θ), for some θ = β. Now holding p 10, p 20, y fixed, if we increase p 11, then the denominator of q 1 (· β) will increase more (resp., less) than that of q 1 (· θ) if β 0 > θ 0 (resp., β 0 < θ 0 ), so that q 1 (· β) = q 1 (· θ) cannot continue to hold. Therefore, we must have β 0 = θ 0. Next, if we increase y, p 10 and p 20 by the same amount such that y − p 10, y − p 20 remain fixed, only the 4th term in the denominator of (23) will change, and by the same logic as above, maintaining q 1 (· β) = q 1 (· θ) would require β 12 = θ 12. Changing y and p 10 by the same amount holding p 11 and p 20 fixed would deliver β 2 = θ 2, and changing y while changing p 20 by the same amount and changing p 11 the same amount in the opposite direction while holding p 10 fixed would deliver β 1 = θ 1. Thus although there exist θ = β which will produce the same choice probabilities for all potentially observable values of prices and income, the expression (22) is different with positive probability (w.r.t. the joint distribution of the regressors) if θ = β. This implies that the CV distribution cannot be learned from the choice probabilities unless p 11 = p 10, which is the single price change scenario. We summarize the above discussion as a theorem. Theorem 3. For multinomial choice with nonexclusive alternatives, the marginal distribution of EV and CV resulting from a change in the price of a single alternative can be expressed as a closed-form functional of the structural choice probabilities. For a simultaneous price change of multiple alternatives, the welfare distributions are not pointidentified from the structural choice probabilities. Note that the conclusion of the above theorem is starkly different from the multinomial case with exclusive alternatives where welfare distributions are point-identified from the structural choice probabilities for both single and multiple price changes. An intuition for the result is that in the nonexclusive case, there is a systematic relationship between the prices of the different ultimate options, so that in a dataset we can never observe independent price variations across the various (composite) options, no matter how many price combinations are observed across the constituent individual alternatives. Bounds for the CV distribution: One can nonetheless bound the probability (22) using Assumption 1. In particular, let

## A =

## B =

p ∗ 1 p ∗ 2 y ∗: y ∗ − p ∗ 1 ≥ y − p 10 y ∗ − p ∗ 2 ≤ y − p 20 y ∗ − p ∗ 1 − p ∗ 2 ≤ y − p 10 − p 20 y ∗ ≤ y + p 11 − p 10 p ∗ 1 p ∗ 2 y ∗: y ∗ − p ∗ 1 ≤ y − p 10 y ∗ − p ∗ 2 ≥ y − p 20 y ∗ − p ∗ 1 − p ∗ 2 ≥ y − p 10 − p 20 y ∗ ≥ y + p 11 − p 10 Then an upper bound consistent with Assumption 1 is given by ' Pr U 1 (y − p 10 η) ≥ max U 2 (y − p 20 η) U 12 (y − p 10 − p 20 η) ( U 0 (y + p 11 − p 10 η) ⎫ ⎤ ⎧ ∗ ⎡ ∗

## U

y − p η ⎪ ⎪ 2 2 ⎪ ⎪ ⎨ ⎢ ∗ ∗ ⎬ ⎥ ∗ ∗ ∗ ⎢ U 1 y − p η ≥ max U 12 y − p − p η ⎥

Pr ≤ ∗ inf 1 1 2 ⎦ ⎣ ⎪ ⎪ (p 1 p ∗ 2 y ∗ )∈A ⎪ ⎪ ⎭ ⎩ ∗

U 0 y η ∗ ∗ ∗ = ∗ inf q 1 p 1 p 2 y ∗ (24) (p 1 p 2 y ∗ )∈A These bounds arise from the fact that if, for example, y ∗ − p ∗ 1 ≥ y − p 10, then U 1 (y ∗ − p ∗ 1 η) ≥ U 1 (y − p 10 η), by Assumption 1, so that the probability of U 1 (y − p 10 η) exceeding a specific number is smaller than that of U 1 (y ∗ − p ∗ 1 η) exceeding that same number. Similarly, y ∗ − p ∗ 2 ≤ y − p 20 implies that U 2 (y − p 20 η) ≥ U 2 (y ∗ − p ∗ 2 η) so that the probability of U 2 (y − p 20 η) being exceeded by a number is smaller than that of U 2 (y ∗ − p ∗ 2 η) being exceeded by it, etc. By a similar logic, a lower bound on (22) is given by ' Pr U 1 (y − p 10 η) ≥ max U 0 (y + p 11 − p 10 η) U 2 (y − p 20 η) ( U 12 (y − p 10 − p 20 η) ⎫ ⎤ ⎧ ∗ U 2 y − p ∗ 2 η ⎪ ⎪ ⎪ ⎪ ⎬ ⎥ ⎨ ⎢ ∗ ∗ ∗ ∗ ∗ ⎢ Pr ⎣ U 1 y − p 1 η ≥ max U 12 y − p 1 − p 2 η ⎥ ≥ sup ⎦ ⎪ ⎪ ⎪ ⎪ (p ∗ 1 p ∗ 2 y ∗ )∈B ⎭ ⎩ ∗

U 0 y η ∗ ∗ ∗ = sup q 1 p 1 p 2 y ⎡ (p ∗ 1 p ∗ 2 y ∗ )∈B (25) Remark 3. In some practical situations, suppliers may provide a discount if a household buys both options. If this discounted price varies in the cross section over and above that of the constituent options, then this setting becomes identical to a multinomial choice with four alternatives and independent price variation across them. One can then point-identify the EV/CV distributions for multiple price changes simply by using Theorem 1.

4. Discussions on implementation The results reported in Theorem 1, and the associated corollaries are fully nonparametric in that no functional form assumptions are required to derive them. When implementing these results in practical applications, one can therefore estimate conditional choice probabilities nonparametrically, for example, using kernel or series regressions, and then use those estimates to calculate welfare distributions. For instance, recall the 3alternative case, leading to (10), where we have, say, p 11 −p 10 < 0 = p 21 −p 20 < p 31 −p 30. For any random variable X with CDF F(·) and finite mean, the expectation satisfies

## E(X) = −

0 −∞ ∞ 1 − F(x) dx;

F(x) dx + 0 thus the mean EV from (10) is given by − 0 p 1 p 3 q 1 (p 11 − a 0 p 30 y − a) da + q 3 (p 11 0 p 30 + a y) da (26) 0 where q j (p 1 p 2 p 3 y) denotes the choice probability of alternative j when the price of the three alternatives are (p 1 p 2 p 3) and income is y. If the dataset is of modest size, so that kernel regressions are imprecise, then one can alternatively use a parametric approximation to the choice probabilities. Numerical integration routines are now available in popular software packages like STATA and MATLAB, and can be used to calculate the integrals of choice probabilities in the same way that consumer surplus was traditionally calculated by earlier researchers.

## 4.1 Endogeneity

In this subsection, we briefly discuss the issue of price/income “endogeneity,” that is, situations where price or income are correlated with unobserved preference heterogeneity η, conditional on all other covariates. Note that our theoretical results in Sections 2 and 3 establish the closed-form mapping between welfare distributions and structural choice probabilities. Once the structural choice probabilities (or nonparametric bounds on them) are identified, our results deliver identification of the corresponding welfare distributions without requiring any additional modification due to endogeneity. Nonetheless, in practical applications, estimation of the structural choice probabilities would be necessary before our results can be applied. In this subsection, we (a) briefly outline how existing econometric methods can be used to estimate structural choice probabilities, and (b) more importantly, highlight that for price increase (resp., decrease) the estimation of EV (resp., CV) does not require any correction for income endogeneity. Income endogeneity: In applications, observed income may be endogenous with respect to individual choice, for example, when omitted variables, such as unrecorded education level, can both determine individual choice and be correlated with income. Under such endogeneity, the observed choice probabilities would potentially differ from the structural choice probabilities, and one can define welfare distributions either unconditionally, or conditionally on income, analogous to the average treatment effect and the average effect of treatment on the treated, respectively, in the program evaluation literature. In this context, an important and useful insight, not previously noted, is that for a price rise, the distribution of the income-conditioned EV is not affected by income endogeneity, whereas that of the CV is; for a fall in price, the conclusion holds with CV and EV reversed. To see why that is the case, recall the three alternative cases discussed above, and define the conditional-on-income structural choice probability at income y as q j c p 1 p 2 p 3 y y =

1 U j y − p j η ≥ max U k y − p k η dF(η|y) k= j where F(·|y) denotes the distribution of the unobserved heterogeneity η for individuals whose realized income is y, where y may or may not equal y. Now, for a real number a, satisfying p 11 − p 10 ≤ a < p 21 − p 20, it is easy to see that similar to equation (10), the distributions of EV at a, evaluated at income y, conditional on realized income being y, are given by Pr(EV ≤ a|Inc = y) = q 1 c (p 11 p 20 + a p 30 + a y y) (27) while for CV it is given by Pr(CV ≤ a|Inc = y) = q 1 c (p 11 p 20 + a p 30 + a y + a y) (28) Now, q 1 c (p 11 p 20 + a p 30 + a y y), by definition, is the fraction of individuals currently at income y who would choose alternative 1 at prices (p 11 p 20 + a p 30 + a), had their income been y. Now if prices are exogenous in the sense that P ⊥ η|Y, then the observable choice probability conditional on price p and income y q̄ 1 (py) = 1 U 1 (y − p 1 η) ≥ max U k (y − p k η) f (η|p y) dη by P⊥η|Y = k= 1

1 U 1 (y − p 1 η) ≥ max U k (y − p k η) f (η|y) dη = q 1 c (p y y) k= 1 Therefore, (27) equals q̄ 1 (p 11 p 20 + a p 30 + a y y), so no corrections are required owing to endogeneity. However, in (28), q 1 c (p 11 p 20 + a p 30 + a y + a y) is the fraction of individuals currently at income y who would choose alternative 1 at prices (p 11 p 20 + a p 30 + a), had their income been y + a. This fraction is counterfactual and not directly estimable because the distribution of η is likely to be different across people with income y + a relative to those with income y, due to endogeneity. To summarize, if the objective of welfare analysis is to calculate the EV distribution resulting from price rise for individuals whose realized income equals the hypothetical income, then endogeneity of income is irrelevant to the analysis. This implies that if exogeneity of income is suspect and no obvious instrument or control function is available, then a researcher can still perform meaningful welfare analysis based on the EV distribution at realized income, provided price is exogenous conditional on income and other observed covariates. Furthermore, one can calculate aggregate welfare in the population by integrating q̄ 1 (py) = q 1 c (p y y) over the marginal distribution of income. Price endogeneity: Price can be correlated with individual heterogeneity either because there are unobserved choice attributes which vary across individuals, or spatial concentration of individuals with strong preferences for the good could raise local prices. In such cases, control function methods (e.g., Blundell and Powell (2003)) can potentially be used to identify structural choice probabilities. For example, prices in neighboring markets (a la Hausman (1996)) can be used as instruments to generate residuals in a first stage, and then these residuals used as control functions in a second step. Such instruments are more likely to be valid if spatial correlation in prices result primarily from spatial correlation in supply costs and not from spatial correlation of consumer preferences. A complete resolution of these issues is left to future research.

5. Empirical illustration In this section, we provide a brief empirical illustration of our methods using a dataset on choice of fishing mode in Southern California, previously analyzed in Herriges and Kling (1999). Our primary purpose is to see what sorts of numerical results one gets by applying our methods to a real dataset. As an aside, we also compare our results to a fully parametric, logsum-type approach, popular in applications. The key features of our microdata, which are publicly available, are discussed in Kling and Thomson (1996). The dataset consists of a cross section of 1182 individuals. For each individual, there are 4 potential modes of fishing, namely from the beach, the pier, a charter boat, and a private boat, labeled 1 through 4, respectively. Individual income ($ per month) is recorded, together with the chosen mode, the price of each alternative faced by the individual, and the exogenous catch rate, that is, the average number of fish per hour of fishing at the site (obtained from an external source) corresponding to each option. The price reflects primarily transportation costs to the fishing site; see Kling and Thomson (1996) for a more detailed description of the variables. Table 1 provides summary statistics. We use these data to calculate distributions of individual compensating variation corresponding to two hypothetical policy changes. The first is a simultaneous change in

Table 1. Summary statistics.

Variable beach pier private charter catch-rate beach catch-rate pier catch-rate private catch-rate charter income price-beach price-pier price-private price-charter

Mean

Min

Max 011 015 035 038 024 016 017 063 5250 10342 10342 5526 8438 032 036 048 049 019 016 021 071 2958 10364 10364 6271 6354 000 000 000 000 007 000 000 000 500 129 129 229 2729 100 100 100 100 053 045 074 231 10 000 84319 84319 66611 69111 Note: Beach is a dummy for fishing from the beach, price-beach is its price, catch-rate beach is the number of fish caught per hour, and income is individual monthly income in dollars. Similarly for the other alternatives.

the prices of fishing from the beach, the pier, and from a private boat. The second is the private welfare effect of availability of the private boat option and, separately, that of the charter boat option at hypothetical prices. That is, we consider a thought experiment where we assume that the private option was initially available at a specific price, and was subsequently eliminated, for example, due to environmental concerns. The third exercise involves welfare effects of quality-change, namely a lowering of the catch rate of the beach option. For each exercise, the mean CV is reported across a range of incomes, while keeping all other variables (i.e., those not being targeted by the change) fixed at their mean value. We maintain the assumption of independence between budget sets and preferences, for this illustration. In order to avoid curse of dimensionality problems during estimation, we model the choice probability of each alternative j in a partially linear fashion as q j (p y x) = h j (y − p j) + x β j + (y1 −j − p −j) γ j (29) where h j (· ·) denotes a cubic in income and own price, y1 − p −j denotes the vector of income minus price of other alternatives and x denotes catch rates. These specifications are to be interpreted as series/sieve approximations to the true nonparametric choice probabilities. Multiple price change: For the first exercise, we consider an initial price vector p 0 = (140 140 60 12) and final price vector p 1 = (40 40 60 72). Note that the price of alternatives 1 and 2 have fallen by 100, while that of alternative 4 has risen by 60, with the price of 3 fixed at 60. These changes in prices correspond to a fall from approximately the 75th to the 25th percentile for alternatives 1 and 2, and a rise from the 25th to the 75th percentile for alternative 4. The marginal distribution of individual welfare losses at income y with catch rates set at their mean values x is given by (cf. equation (10)) ⎧ ⎪ 0 ⎪ ⎪ ⎪ ⎨ (q + q )(40 − a 40 − a 60 12 y x) 1 2

Pr(CV ≤ a) = ⎪ (40 40 60 12 + a y + a x) 1 − q ⎪ 4 ⎪ ⎪ ⎩ 1 if a < −100 if − 100 ≤ a < 0 if 0 ≤ a < 60 (30) if a ≥ 60 We will contrast the mean welfare estimates resulting from this exercise with the popular Small and Rosen (1981) approach using the so-called “log-sum” formula (cf., Train (2009, p. 56)). For the multiple price change case, for example, adding income and catch rate as controls, the log-sum values are given by

## E(CV)

⎫ ⎤ ⎡ ⎧ exp b 01 + αp 10 + β 1 z + exp b 02 + αp 2 + β 2 z ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎢ ⎪ ⎪ ⎪ ⎥ ⎨ ⎢ + exp b 03 + αp 2 + β 3 z + exp b 04 + αp 40 + β 4 z ⎬ ⎥ 1 ⎢ ⎥ = ⎥ ⎢ ln ⎥ ⎪ |α| ⎢ ⎪ exp b 01 + αp 11 + β 1 z + exp b 02 + αp 2 + β 2 z ⎪ ⎪ ⎪ ⎦ ⎣ ⎪ ⎪ ⎪ ⎪ ⎪ ⎭ ⎩ + exp b 03 + αp 2 + β 3 z + exp b 04 + αp 41 + β 4 z (31) where the bs represent the alternative specific intercepts, |α| is the constant marginal utility of income and z = (x y), the mean values of catch rates and income. The b’s and α are estimated via the constrained “mlogit” command in Stata after imposing constant marginal utility of income by requiring price coefficients to be identical across alternatives. The substantive difference in functional forms between (29), (30), and (31) is in how price and income appear in them. The logsum formula is based on the constant marginal utility of income, and thus requires price coefficients to be identical across alternatives. In addition, income is arbitrarily incorporated as a covariate, as is usually done in applications. Our expressions, instead, include income y as appearing in the form of y − p j, and are thus consistent with a coherent, theoretically justified specification. In Figure 1, we plot the average CV by income, evaluated at mean values of controls, based on the logsum formula of Small and Rosen, adding income as an additional control, 6 and then using our methods (30) with specification (29) for the choice probabilities. Evidently, the logsum estimates are small, and decrease with income, whereas our CV estimates imply larger (about 2 times) welfare losses which increase with income. The numerical results do vary a bit if a quadratic or a linear spline is used as opposed to a cubic, but these two substantive features continue to hold. It is also interesting to note that due to a higher proportion (3 times) of people choosing alternative 4 whose 6 The logsum formula comes from an assumption of quasilinear utilities where there is no income effect. Taken literally, this would imply a flat welfare estimate against income. But in most empirical applications, income is added as a demographic variable (as opposed to coming from the budget constraint), which is what we use here.

Figure 1. Average CV for multiple price change. Average welfare loss in $ by monthly income from a price fall from the 75th to the 25th percentile for beach and pier fishing, and a rise from the 25th to the 75th percentile for private-boat fishing, evaluated at mean values of income and catch rate of all alternatives and mean price of charter-boat fishing. Solid line corresponds to our nonparametric estimates, dashed line to the logsum estimates.

price has risen, the overall welfare is reduced, that is, average CV is positive, although the prices of alternatives 1 and 2 have fallen by a large amount. Eliminate alternative: Suppose the local government is considering means to reduce environmental damage by banning either the private boat or the charter boat option. For deciding which option to ban, it is useful to know the loss in private welfare from each. Toward that end, we first consider eliminating the private option from a situation where the price vector was (75 75 60 33), which are essentially the median values in the data, and the catch rates were at their mean value, denoted x, and assuming no changes in the prices of alternatives 1–3. In this case, average CV is given by ∞ q 4 (75 75 60 33 + a y + a x) (32)

## E(CV) =

0 These will be compared with the corresponding numbers resulting from eliminating the charter boat option. In Figures 2 and 3, we plot the average welfare losses from elimination of respectively the private and the charter option. We compare our estimates using (29) and (32) with those obtained using a logsum approach. To calculate the integral up to infinity in (32), we simply use the highest observed price as the upper limit of the integral. As such, our estimates may be viewed as a lower bound on the average CV. Evidently, our estimates are much flatter against income relative to the logsum estimates; they are much lower (less than 50%) for elimination of the private option, and Figure 2. Elimination of option: LogSum vs cubic. Average welfare loss $ by monthly income from elimination of charter-boat and of private boat fishing. Solid line corresponds to our nonparametric estimates, dashed line to the logsum estimates. All calculations are performed at mean values of other characteristics.

Figure 3. Eliminate charter vs pvt. Average welfare loss $ by monthly income from elimination of charter-boat and of private boat fishing. Dashed line corresponds to charter-boat and solid line to private boat. All calculations are performed at mean values of other characteristics.

much higher (about twice on average for lower incomes) for the charter option. It is also important to note that the slope of average welfare w.r.t. income has different signs, for example, the logsum estimates imply that eliminating the charter boat option will hurt the rich more than the poor, whereas our CV estimates imply the exact opposite. Figure 3 shows, in a slightly blown up scale, that elimination of these options entail fairly significant losses in private welfare, amounting to about 10% of the average monthly income. Putting Figures 2 and 3 together, it is also evident that the logsum estimates would imply a much larger difference in welfare losses between eliminating the private versus the charter option, compared with our CV estimates. Quality change: Finally, the third exercise involves decreasing the catch rate of alternative 1, namely beach fishing from the 4th quartile 053 to the 1st quartile 006, keeping all other variables fixed at their mean value, denoted z. Assuming that catch rate is a normal characteristic for all individuals, the bounds on the CDF of the CV are given by Proposition 2 in the Appendix, namely

Pr(CV ≤ a) where ∈ [L U] if a < 0 = 1 if a ≥ 0 ⎧ ⎫ ⎪ ⎪ q 1 75 − a + y − y y z 053 ⎪ ⎪ ⎪ ⎪ ⎬ ⎨ max y <y + q 0 75 + y − y y z 006

L = max ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎭ ⎩ − 1 − q (75 − a z y 053) 0 0 ⎧ ⎫ ⎪ ⎪ q 1 (75 − a y z 053) ⎪ ⎪ ⎪ ⎪ ⎨ ⎬

U = min q 1 75 − a + y − y y z 053 ⎪ min ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ y ≥y + q 0 75 + y − y y z 006 ⎭ (33) q 0 (p z y x) ≡ 1 − q 1 (p y z x) To compare these bounds with the logsum formulae, which are based on quasilinear utility assumption, we use two alternative specifications of the logsum, one that incorporates income as an additional covariate and one that does not. The logsum expressions are essentially (31) with the same prices but different catch rates in the numerator and denominator. We finally obtain the following graph, where we plot the average welfare loss (i.e., negative of the CV) by income. The bounds (dashed lines) are relatively tight. The lower bound remains zero, but the upper bound hovers around $750 for most of the income range. Relative to the logsum estimates with income included as a covariate (the nearly straight downward sloping line), our bounds are much flatter, and higher than the logsum estimates at high incomes. Indeed, the logsum estimate yields negative welfare losses, that is, welfare gains from reduced catch rates, which is an artifact of the functional form assumption, and Figure 4. Avg. welfare loss from reduced catch rate. Average welfare loss $ by monthly income from decreasing the catch rate of alternative 1, namely, beach fishing from the 4th quartile 053 to the 1st quartile 006, keeping all other variables fixed at their mean value. Lower and upper bounds from our calculations are shown via dotted lines and Logsum estimates with no income effect by the solid line, and with income as covariate by downward sloping, almost a straight line.

Table 2. Mean welfare loss & 95% C.I. in $ at mean income.

Multiple Price Change Eliminate Pvt. Boat Eliminate Charter Decrease Catch-rate of Beach

Cubic

Approximation

Bootstrap C.I.

LogSum 4257 53637 58816 705 40.0, 43.1 292.31, 705.08 582.4, 591.8 4.55, 11.91 1921 12124 28029 468 Note: Mean CV and associated bootstrapped confidence interval for (i) simultaneous price change of beach and pier fishing from $ 140 to $ 40 and of private boat fishing from $ 12 to $ 72, (ii) elimination of private, and (iii) of charter boat, and (iv) a fall in catch rate of beach fishing from 053 to 006 per hour (upper bound of average welfare loss). All quantities are evaluated at mean income of $ 4000 per month, and mean values of all other regressors.

is difficult to interpret. Of course, these differences in slopes are also important from a policy perspective, because the variation of welfare with income determines the progressivity of the economic change. As discussed above, the key difference in functional forms between our estimates and the logsum formulae lies in the treatment of income. One can see from Figure 4 that if one ignores income entirely, given the quasilinear basis of logsum estimates, then one gets the solid flat line at around $184 which lies entirely within our bounds. Our final set of results in Table 2 report the welfare changes discussed above, together with bootstrapped confidence intervals, evaluated at Income = $4000 per month, which is about the mean income. The confidence intervals are evaluated over 100 replications, and the top 1% and bottom 1% of values are discarded. The logsum estimates are reported in the last column for comparison. It is evident from this table that the cubic approximation based estimates of compensating variation are reasonably precise, and the corresponding confidence intervals do not contain the logsum estimates, except for the case of quality change. Finally, the sizes of the point estimates show that elimination of the private or the charter boat option entails very high welfare loss, amounting to nearly 13% of mean income; but the change in catch rate has a very small welfare impact, suggesting that it is the overall experience of fishing from one’s chosen alternative, rather than the quantity of fish caught, that is primarily valued by individuals. It is not obviously possible to conclude empirically whether our estimates are more accurate than the logsum ones. But since our estimates correspond to a theoretically consistent utility structure, do not impose constant marginal utility of income, and are not based on specific distributional assumptions, they should be viewed as more robust on theoretical grounds. In the above application, our estimates differ substantially from the logsum ones, which does therefore raise doubt about the strong assumptions underlying the logsum approach. Indeed, our theoretical results above show that specification of choice probabilities fully determines welfare estimates (or bounds thereof ), without any reference to underlying utility structures. So any differences between our results and the logsum ones must necessarily arise from differences in functional forms for choice probabilities. One could also try using alternative and more flexible parametric models such as the mixed or nested logit, and compare them with our results. Since our primary goal here is to provide a “proof of concept” regarding empirical feasibility of our theoretical methods, we leave such comparisons to future research.

6. Summary and conclusion In this paper, we have developed expressions for welfare effects of economic changes in multinomial choice settings, allowing for completely general consumer heterogeneity and income effects. The paper considers four practical scenarios: (a) simultaneous change in prices of multiple alternatives, (b) the introduction or elimination of an alternative, possibly accompanied by price changes of other alternatives, (c) change in the quality of an alternative possibly accompanied by a price change, and (d) situations where choice alternatives are nonexclusive. The key results are: (1) Hicksian welfare changes are well-defined in all cases under the mild assumption that the numeraire is a normal good, (2) in cases (a) and (b) the marginal distributions of CV and EV can be expressed as simple closed-form functions of choice probabilities without requiring any assumption on the functional forms of utilities, preference heterogeneity or income effects and (3) this last conclusion fails for quality change or when alternatives are nonexclusive, but welfare distributions can still be bounded in these cases. Our approach delivers welfare analysis without requiring identification of preference distributions. As such, it strictly dominates random-coefficient based methods which require a researcher to either make arbitrary assumptions on the distribution of random coeffi17597331, 2018, 2, cients (e.g., that they are normally distributed), or to require full support of regressors for identification and to solve difficult ill-posed inverse problems in estimation. At a practical level, our methods can be used in program evaluation studies to calculate “compensated” program effects, that is, the program’s value to the subjects themselves, measured in terms of its cash equivalent, and the associated deadweight loss, while allowing for arbitrary preference distribution in the population. These moneymetric welfare measures can also be compared across interventions with different outcomes. For example, a tuition subsidy for school attendance, and an adoption subsidy for take-up of a health-product cannot be directly compared in terms of their average outcomes which are in different units; but their cash equivalents and the associated deadweight loss can be directly compared, since both are expressible in monetary units. This comparison can then inform the decision of which public subsidy program should be adopted.

## Appendix

Path-dependence of line integral defining Marshallian consumer surplus for discrete choice Consider a setting with three mutually exclusive alternatives with initial prices p 0 ≡ (p 10 p 20 p 30) and final prices p 1 ≡ (p 11 p 21 p 31 ). Let y denote income and q j (p y) denote the choice probability of alternative j when the price vector is p and income is y. Then the change in average consumer surplus arising from the price change from p 0 to p 1 can be defined using (4) via the line integral

## CS(L) = −

q 1 (p y) dp 1 + q 2 (p y) dp 2 + q 3 (p y) dp 3

## L

where L denotes a path L(t) from t = 0 to t = 1 such that L(0) ≡ p 0 ≡ (p 10 p 20 p 30) and L(1) ≡ p 1 ≡ (p 11 p 22 p 33 ). Consider two different such paths L 1 (t) = p 10 + t(p 11 − p 10) p 20 + t(p 21 − p 20) p 30 + t(p 31 − p 30) L 2 (t) = p 10 + t 2 (p 11 − p 10) p 20 + t(p 21 − p 20) p 30 + t(p 31 − p 30)

Then ⎤ (p 11 − p 10) × q 1 p 0 + t(p 1 − p 0) y 1 ⎢ ⎥ ⎢ + (p 21 − p 20) × q 2 p 0 + t(p 1 − p 0) y ⎥ dt

## CS(L 1) = −

⎦ ⎣ 0 + (p 31 − p 30) × q 3 p 0 + t(p 1 − p 0) y ⎡

But ⎛ ⎞ ⎞ ⎤ p 11 − p 10 ⎟ ⎟ ⎥ ⎢ 2t(p − p) × q ⎜ p + t(p − p) + t 2 − t ⎜ 0 ⎠ y ⎠ ⎥ ⎝ ⎢ 11 10 1 ⎝ 0 1 0 ⎢ ⎥ ⎢ ⎥ 0 ⎢ ⎥ ⎢ ⎞ ⎞ ⎥ ⎛ ⎛ ⎢ ⎥ 1 ⎢ p − p 10 ⎥ 2 ⎜ 11 ⎢ ⎟ ⎟ ⎥ ⎜ =− 0 ⎢ + (p 21 − p 20) × q 2 ⎝ p 0 + t(p 1 − p 0) + t − t ⎝ ⎠ y ⎠ ⎥ dt ⎥ 0 ⎢ ⎢ ⎥ 0 ⎢ ⎥ ⎢ ⎥ ⎛ ⎞ ⎞ ⎛ ⎢ ⎥ p 11 − p 10 ⎢ ⎥ 2 ⎜ ⎢ ⎜ ⎟ ⎟ ⎥ ⎣ + (p 31 − p 30) × q 3 ⎝ p 0 + t(p 1 − p 0) + t − t ⎝ 0 ⎠ y ⎠ ⎦ 0 ⎡ ⎛ which would in general differ from CS(L 1 ). Thus the CS is not well-defined for simultaneous change in multiple prices. Note that if only p 1 changes, then 1 # "

CS(L 1) = −(p 11 − p 10) × q 1 p 10 + t(p 11 − p 10) y dt 0 # (p 11 − p 10) × q 1 p 10 + t 2 (p 11 − p 10) y t dt 1 "

## CS(L 2) = −2

0 = −(p 11 − p 10) × 1 q 1 p 10 + r(p 11 − p 10) y dr substituting t 2 = r 0

## = CS(L 1)

and we get back path independence. Thus the loss of path-independence arises only for multiple simultaneous price changes. Iterating single price change: We show that welfare analysis of multiple price changes cannot be done by iterating the single price change result of Bhattacharya (2015). Consider a choice among three alternatives (J = 3), and suppose that price of alternative 1 changes from p 10 to p 11, and that of 2 from p 20 to p 21, and price of 3 is unchanged at p 3. Suppose we try to calculate the overall CV, starting with, say, price change of alternative 1, followed by 2 (the order in which we do this does not matter, by Proposition 1) and applying Theorem 2 of Bhattacharya (2015) at each stage. Suppose the CVs corresponding to the two price changes are denoted by S 1 and S 2, respectively. Then, by definition, max U 1 (y − p 10 η) U 2 (y − p 20 η) U 3 (y − p 3 η) = max U 1 (y + S 1 − p 11 η) U 2 (y + S 1 − p 20 η) U 3 (y + S 1 − p 3 η) ⎧ ⎫ U 1 (y + S 1 + S 2 − p 11 η) U 2 (y + S 1 + S 2 − p 21 η) ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ ⎬

## S

=S, overall CV = max ⎪ ⎪ ⎪ ⎪ (y +

## S

+

## S

− p η)

## U

⎪ ⎪ 3 1 2 3 ⎪ ⎪ ⎩ ⎭

## S

Then using Theorem 2 of Bhattacharya (2015), we can get the marginal distribution of S 1 but we cannot get the marginal distribution of S 1 + S 2 because the price of both alternatives 1 and 2 have changed between lines 1 and 3 of the previous display, and so Theorem 2 of Bhattacharya (2015) does not apply. Second, because we cannot calculate the value of the CV S 1 for an individual (we can only calculate its distribution across all individuals), we cannot apply Theorem 2 of Bhattacharya (2015) to calculate the marginal distribution of S 2, since the income at which we could potentially apply the theorem depends on S 1 which is unknown, unlike y, which is a fixed known constant.

Proof of Theorem 1. First, consider EV.

Note that the EV is defined by max U 1 (y − p 11 η) U 2 (y − p 21 η) U J (y − p J1 η) = max U 1 (y − S − p 10 η) U 2 (y − p 20 − S η) U J (y − p J0 − S η) (34) We have already shown in Proposition 1 that under Assumption 1, the solution to (34) exists and is unique. Furthermore, because the RHS is strictly decreasing in S, we have that

EV ≤ a ⇔ ⎧ ⎫ ⎪ max U 1 (y − p 11 η) U 2 (y − p 21 η) U J (y − p J1 η) ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ ⎬ U 1 (y − a − p 10 η) U 2 (y − p 20 − a η) ⎪ ⎪ ⎪ ⎪ ≥ max ⎪ ⎪ ⎩ ⎭ U J (y − p J0 − a η) Now, if a satisfies p l1 − p l0 ≤ a < p l+11 − p l+10, then

Pr(EV ≤ a) ⎤ ⎡

U 1 (y − p 11 η) ⎢ ⎫ ⎥ ⎧ ⎥ ⎢ (y − p η)

## U

(y − p η)

## U

(y − p η)

## U

⎥ ⎢

## J

⎪ ⎪ 2 21

## J1

l l1 ⎪ ⎪ ⎥ ⎢ ⎬ ⎨ = Pr ⎢ ⎥ ⎥ ⎢ ≥ max U 1 (y − a − p 10 η) U 2 (y − p 20 − a η) ⎦ ⎣ ⎪ ⎪ ⎪ ⎪ ⎭ ⎩ U l (y − a − p l0 η) U J (y − p J0 − a η) ⎡ ⎤

U 2 (y − p 21 η) ⎢ ⎫ ⎥ ⎧ ⎢ ⎥ (y − p η)

## U

(y − p η)

## U

(y − p η)

## U

⎢ ⎥

## J

⎪ ⎪ 1 11

## J1

l l1 ⎪ ⎪ ⎢ ⎥ ⎬ ⎨ + Pr ⎢ ⎥ ⎢ ≥ max U 1 (y − a − p 10 η) U 2 (y − p 20 − a η) ⎥ ⎣ ⎦ ⎪ ⎪ ⎪ ⎪ ⎭ ⎩ U l (y − a − p l0 η) U J (y − p J0 − a η) + ··· (35) ⎤

U l (y − p l1 η) ⎢ ⎧ ⎫ ⎥ ⎥ ⎢ ⎪ U 1 (y − p 11 η) U 2 (y − p 21 η) U l−1 (y − p l−11 η) ⎪ ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎢ ⎪ ⎪ ⎨ U l+1 (y − p l+11 η) U J (y − p J1 η) ⎬ ⎥ + Pr ⎢ ⎥ ⎥ ⎢ ≥ max ⎥ ⎢ ⎪ ⎪ ⎥ ⎢ ⎪ ⎪

## U

(y − a − p η)

## U

(y − p − a η) 1 10 2 20 ⎪ ⎪ ⎦ ⎣ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ U (y − a − p η) U (y − p − a η) ⎭ ⎡ l ⎡ l0

## J

## J0

⎤

U 1 (y − p 11 η) ⎢ ⎥ (1) ⎢ ⎥ = Pr ⎢ ⎥ U 2 (y − p 21 η) U l (y − p l1 η) ⎣ ≥ max ⎦ U l+1 (y − a − p l+10) U J (y − p J0 − a η) ⎡ ⎤

U 2 (y − p 21 η) ⎢ ⎥ ⎢ ⎥ + Pr ⎢ ⎥ U 1 (y − p 11 η) U l (y − p l1 η) ⎣ ≥ max ⎦ U l+1 (y − a − p l+10) U J (y − p J0 − a η) + ··· ⎡ ⎤

U l (y − p l1 η) ⎢ ⎥ ⎢ ⎥ + Pr ⎢ ⎥ U 1 (y − p 11 η) U l−1 (y − p l−11 η) ⎣ ≥ max ⎦ U l+1 (y − a − p l+10 η) U J (y − p J0 − a η) where the equality marked (1) uses the fact that y − p j1 ≥ y − a − p j0, for all j = 1 l, since p l1 − p l0 ≤ a. The above probability equals q 1 (p 11 p 21 p l1 p l+10 + a p J0 + a y) + q 2 (p 11 p 21 p l1 p l+10 + a p J0 + a y) + · · · + q l (p 11 p 21 p l1 p l+10 + a p J0 + a y) if a ≥ 0, and equals = q 1 (p 11 − a p 21 − a p l1 − a p l+10 p J0 y − a) + q 2 (p 11 − a p 21 − a p l1 − a p l+10 p J0 y − a) + · · · + q l (p 11 − a p 21 − a p l1 − a p l+10 p J0 y − a) if a < 0. This is precisely expression (8). The different expressions for a ≥ 0 and a < 0 are needed to accommodate an outside good whose price remains 0 before and after. For example, if the lth alternative is the outside good, and thus p l1 = p l0 = 0 and a ≥ 0, then one can evaluate the necessary probability by observing behavior at income y, for example, ⎡ ⎤

U 1 (y − p 11 η) ⎢ ⎥ ⎢ ⎥

Pr ⎢ ⎥ U 2 (y − p 21 η) U l (y − p l1 η) ⎣ ≥ max ⎦ U l+1 (y − a − p l+10) U J (y − p J0 − a η) ⎤ ⎡

U 1 (y − p 11 η) ⎢ ⎥ ⎥ ⎢ = Pr ⎢ ⎥ U 2 (y − p 21 η) U l (y η) ⎦ ⎣ ≥ max U l+1 (y − a − p l+10) U J (y − p J0 − a η) = q 1 (p 11 p 21 p l1 p l+10 + a p J0 + a y) But if the outside alternative is l + 1, then p l+11 = p l+10 = 0 and a < 0, and so ⎡ ⎤

U 1 (y − p 11 η) ⎢ ⎥ ⎢ ⎥

Pr ⎢ ⎥ U 2 (y − p 21 η) U l (y − p l1 η) ⎣ ≥ max ⎦ U l+1 (y − a − p l+10) U J (y − p J0 − a η) ⎤ ⎡

U 1 (y − p 11 η) ⎢ ⎥ ⎥ ⎢ = Pr ⎢ U 2 (y − p 21 η) U l (y − p l1 η) ⎥ ⎦ ⎣ ≥ max U l+1 (y − a) U J (y − p J0 − a η) But we cannot evaluate this probability by observing behavior at income y, as no one in the data faces a price of a < 0 for the l + 1th alternative, that is, the outside good. So the only way to learn this probability is to observe individuals at income y − a facing a price of zero for the outside good. Next, consider CV, defined as the solution S to the equation max U 1 (y + S − p 11 η) U 2 (y + S − p 21 η) U J (y + S − p J1 η) = max U 1 (y − p 10 η) U 2 (y − p 20 η) U J (y − p J0 η) (36) By exactly similar logic as above, CV ≤ a is equivalent to max U 1 (y − p 10 η) U 2 (y − p 20 η) U J (y − p J0 η) ≤ max U 1 (y + a − p 11 η) U 2 (y + a − p 21 η) U J (y + a − p J1 η) (37)

Accordingly, we have that

Pr(CV ≤ a) ⎡ ⎤ U k (y + a − p k1 η) ⎢ ⎧ ⎫ ⎥ ⎥ ⎢ U 1 (y − p 10 η) U k−1 (y − p k−10 η) U k (y − p k0 η) ⎪ ⎪ ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎥ ⎢ j ⎪ ⎪ ⎪ ⎪ ⎢

## U

(y − p η)

## U

(y − p η) ⎥

## J

⎪ ⎪

## J0

k+1 k+10 ⎪ ⎪ ⎥ ⎢ ⎨ ⎬ =

Pr ⎢ ⎥ ⎥ ⎢ ≥ max (y + a − p η)

## U

(y + a − p η)

## U

1 11 j−1 j−11 k=1 ⎢ ⎪ ⎪ ⎪ ⎪ ⎥ ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎢ ⎪ ⎪ ⎪ U j (y + a − p j1 η) U j+1 (y + a − p j+11 η) ⎪ ⎥ ⎦ ⎣ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ ⎭ U J (y + a − p J1 η) ⎤ ⎡ U k (y + a − p k1 η) ⎢ ⎧ ⎫ ⎥ ⎥ ⎢ U 1 (y − p 10 η) U k−1 (y − p k−10 η) ⎪ ⎪ ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎥ ⎢ j ⎪ ⎪ ⎪ ⎪ ⎢ (y − p η)

## U

(y − p η)

## U

⎥

## J

⎪ ⎪

## J0

k+1 k+10 ⎪ ⎪ ⎥ ⎨ ⎬ =

Pr ⎢ ⎥ ⎢ ⎥ ⎢ ≥ max

## U

(y + a − p η)

## U

(y + a − p η) 1 11 j−1 j−11 k=1 ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎥ ⎢ ⎪ ⎪ ⎪ ⎪ ⎥ ⎢ ⎪ ⎪ U j (y + a − p j1 η) U j+1 (y + a − p j+11 η) ⎪ ⎪ ⎦ ⎣ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ ⎭ U J (y + a − p J1 η) ⎡ ⎤ U k (y + a − p k1 η) j ⎢ ⎥ ⎢ ⎥ =

Pr ⎢ U 1 (y + a − p 11 η) U j (y + a − p j1 η) ⎥ ⎣ ≥ max ⎦ k=1 U j+1 (y − p j+10 η) U J (y − p J0 η) The second equality follows from the fact that k ≤ j and p j1 − p j0 ≤ a, and so we have by Assumption 1 that U k (y + a − p k1 η) ≥ U k (y − p k0 η). The third equality follows from p j1 − p j0 ≤ a < p j+11 − p j+10, so by Assumption 1, U k (y − p k0 η) ≤ U k (y + a − p k1 η) for all k ≤ j and U k (y − p k0 η) > U k (y + a − p k1 η) for all k > j. Finally, ⎡ ⎤ U k (y + a − p k1 η) j ⎢ ⎥ ⎢ ⎥

Pr ⎢ U 1 (y + a − p 11 η) U j (y + a − p j1 η) ⎥ ⎣ ≥ max ⎦ k=1 U j+1 (y − p j+10 η) U J (y − p J0 η) ⎧ j ⎪ ⎪ ⎪ ⎪ q k (p 11 p j1 p j+10 + a p J0 + a y + a) if a ≥ 0 ⎪ ⎨ k=1 ≡ j ⎪ ⎪ ⎪ ⎪ q k (p 11 − a p j1 − a p j+10 p J0 y) if a < 0 ⎪ ⎩ k=1 Proof of Corollary 1. The EV is the solution S to the equation:

max U 1 (y − S − p 10 η) U J (y − S − p J0 η) U J+1 (y − S − p J+1 η) = max U 1 (y − p 11 η) U J (y − p J1 η) (38) We seek to find the marginal distribution of S. To do so, we first show that for each η, the S(η) solving (38) is identical to the EV T (η) for a different problem, and the distribution of T (η) in that other problem follows as a corollary of our Theorem 1 above. The other problem is as follows: consider a multinomial choice problem with J + 1 alternatives, where the price vector changes from an initial value of (p 10 p J0 p J+1) to (p 11 p J1 p ), where p J1 − p J0 ≥ p J−11 − p J−10 ≥ · · · ≥ p 11 − p 10. Then the resulting EV satisfies max U 1 (y − T − p 10 η) U J (y − T − p J0 η) U J+1 (y − T − p J+1 η) (39) = max U 1 (y − p 11 η) U 2 (y − p 21 η) U J (y − p J1 η) U J+1 y − p η Now, suppose p tends to infinity. Recall the assumption that for any bundle (j y − p j ), if p j ↑ ∞, then for each η, at least one other bundle (k y − p k) will be strictly preferred to (j y − p j ).Therefore, the maximum on the RHS of (39) cannot be the J + 1th term. Therefore, as p tends to infinity, (39) reduces to (38), and we conclude that for each η, the EV S(η) for elimination of the J + 1th alternative is the same as the EV T (η p) when the new price p of the J + 1th alternative increases to infinity, that is, lim p ↑∞ T (η p) = S(η) pointwise in η. To calculate the distribution of T (η p) for any fixed p, we can apply Theorem 1 with price of the J + 1th alternative changing to p. Now, observe that the random variable 1{T (η p) ≤ a} is bounded uniformly in p by 1 ) for each a, 1 dF(η) = 1 < ∞, and T (η p) → T (η ∞) ≡ S(η) pointwise in η as p ↑ ∞. Therefore, it follows by the dominated convergence theorem that for each a,

1 T η p ≤ a dF(η) lim Pr T η p ≤ a = lim p ↑∞ p ↑∞ =

## T

η p ≤ a dF(η) 1 lim p ↑∞ = Pr S(η) ≤ a (I am grateful to an anonymous referee for pointing out the need for the DCT argument.) The RHS of the previous display is the object we want, namely the CDF of the EV for problem (38), and the LHS is the limit of the CDF for EV in (39) as p ↑ ∞, which is obtained from Theorem 1 by taking the new price of the J + 1th alternative to infinity. An exactly analogous conclusion holds for the CV, and this proves Corollary 1. Proof of Theorem 2. The proof works by constructing a counterexample. Suppose η ≡ (η 1 η 0) is jointly independent of price, income, and quality (P Y X) and η 1 ⊥ η 0. Assume that the support of price distribution is [p L p H ], support of income Y is [y L y H] and that x is a scalar with support [x L x H ], with p H < y L. Let U 1 (Y − P X η) = Y − P + Xη 1 U 0 (Y η) = (1 − η 0 )Y where η 0 is distributed uniform (0 1) and the support of η 1 —denoted by [L U]— satisfies 0 < L < 1, U ≤ x p H L. Assume η 1 is continuously distributed, and denote the CDF of η 1 by G(·). An individual of type (y η) and facing price p and quality x chooses alternative 1 if and only if y − p + xη 1 > (1 − η 0 )y. Now, consider the choice probability in this model. Since 0 ≤ x L η 1 ≤ x H η 1 ≤ p L w.p. 1, it follows that for any p, y, x in the support of the data, we must have that p − y < xη 1 < p, or 0 < p − xη 1 < 1 y w.p. 1 (40) Therefore, the structural choice probability of alternative 1 at price p, quality x and income y is given by q 1 (p y x) = Pr y − p + xη 1 > (1 − η 0 )y = Pr{η 0 y + xη 1 > p} + * p − xη 1 since y > 0 = Pr η 0 > y -

## U,

p − xη 1 1 − dG(η 1) = y

## L

(41) by η 1 ⊥ η 0 inequality (40) and η 0 ∼ U(0 1) -, x p + E(η 1) = 1 − y y Now, consider a change from (p 0 x 0) to (p 1 x 1) satisfying x 1 > x 0 p 1 > p 0 p 1 − p 0

## ∈ (L U)

x 1 − x 0 and p 1 x 1 < p 0 x 0 (42) We wish to calculate the distribution of CV resulting from this change. The CV is defined by the solution S to the equation max U 0 (y η) U 1 (y − p 0 x 0 η) = max U 0 (y + S η) U 1 (y + S − p 1 x 1 η)

Note that

Pr(S = 0) # "

= Pr max U 0 (y η) U 1 (y − p 0 x 0 η) = max U 0 (y η) U 1 (y − p 1 x 1 η) # "

= Pr U 0 (y η) ≥ max U 1 (y − p 0 x 0 η) U 1 (y − p 1 x 1 η) since U 1 (y − p 1 x 1 η) − U 1 (y − p 0 x 0 η) equals (x 1 − x 0 )η 1 + p 0 − p 1, which is continuously distributed as η 1 is continuously distributed, so that # "

Pr U 1 (y − p 1 x 1 η) = U 1 (y − p 1 x 1 η) = 0

Therefore, "

# = Pr U 0 (y η) ≥ max U 1 (y − p 0 x 0 η) U 1 (y − p 1 x 1 η) # "

= Pr U 0 (y η) ≥ U 1 (y − p 0 x 0 η) ≥ U 1 (y − p 1 x 1 η) "

# + Pr U 0 (y η) ≥ U 1 (y − p 1 x 1 η) ≥ U 1 (y − p 0 x 0 η) "

# = Pr (1 − η 0 )y ≥ y − p 0 + x 0 η 1 ≥ y − p 1 + x 1 η 1 "

# + Pr (1 − η 0 )y ≥ y − p 1 + x 1 η 1 ≥ y − p 0 + x 0 η 1 /.

p 0 − x 0 η 1 p 1 − p 0 η 1 ≤ = Pr η 0 ≤ y x 1 − x 0 /.

p 1 − x 1 η 1 p 1 − p 0 η 1 > + Pr η 0 ≤ y x 1 − x 0 - -

## U,

p 1 −p 0, x 1 −x 0 p 0 − x 0 η 1 p 1 − x 1 η 1 dG(η 1) + p −p dG(η 1) = 1 0 y y

## L

x −x =

U, p

## L

= 0 - − x 0 η 1 dG(η 1) + y p 0 x 0 − E(η 1) + y y p 1 −p 0 x 1 −x 0 = 1 − q 1 (p 0 y x 0) +,

## U

## U

p 1 −p 0 x 1 −x 0 1

## U

p 1 −p 0 x 1 −x 0, (43) 0 - p 1 − x 1 η 1 p 0 − x 0 η 1 − dG(η 1) y y - p 1 − p 0 + (x 0 − x 1 )η 1 dG(η 1) y, - p 1 − p 0 + (x 0 − x 1 )η 1 dG(η 1) y Clearly, this expression is different for different choices of G(·) with the same expec0 tation. In particular, if p x 1 −p is smaller than E(η 1 ), then for a degenerate distribution 1 −x 0 G 1 with point mass 1 at its expected value will yield a value of 1 − q 1 (p 0 y x 0) for (43), whereas a nondegenerate G 2 with the same expectation will yield a strictly smaller value 0. However, since G 1 than 1 − q 1 (p 1 y x 1 ), since p 1 − p 0 + (x 0 − x 1 )η 1 < 0 if η 1 > p x 1 −p 1 −x 0 and G 2 have identical expectations, they will yield identical choice probabilities for all p, y, x, by (41). Thus we cannot identify Pr(S = 0) from the choice probabilities.

Proof of Proposition 2. Assume U 1 (y − p x η) ≡ V 1 (h 1 (y − p x) η). Define ā as the unique solution to h 1 (y + ā − p 1 x 1) = h 1 (y − p 0 x 0 ). The existence and uniqueness of ā follow from the properties of h 1 (· ·) and condition S. Then ā can be obtained as the solution to q 1 (p 1 − ā y x 1) = q 1 (p 0 y x 0 ), since "

# Pr U 0 (y η) ≤ V 1 h 1 (y + ā − p 1 x 1) η "

# = Pr U 0 (y η) ≤ V 1 h 1 (y − p 0 x 0) η

Now,

Pr(S ≤ a) ( ' max U 0 (y η) U 1 (y − p 0 x 0 η) = Pr ≤ max U 0 (y + a η) U 1 (y + a − p 1 x 1 η) ' ( max U 0 (y η) V 1 h 1 (y − p 0 x 0) η = Pr ≤ max U 0 (y + a η) V 1 h 1 (y + a − p 1 x 1) η "

# Pr max U 0 (y η) V 1 h 1 (y − p 0 x 0) η ≤ U 0 (y + a η) if a < ā = # " Pr U 0 (y η) ≤ max U 0 (y + a η) V 1 h 1 (y + a − p 1 x 1) η if a ≥ ā

The first of these probabilities equals if a < 0 "

# Pr V 1 h 1 (y − p 0 x 0) η ≤ U 0 (y + a η) if a ≥ 0 0 if a < 0 = q 0 (p 0 + a y + a x 0) if a ≥ 0 0 while the second equals "

# Pr U 0 (y η) ≤ V 1 h 1 (y + a − p 1 x 1) η if a < 0 if a ≥ 0 1 = q 1 (p 1 − a y x 1) 1 if a < 0 if a ≥ 0

Therefore, ⎧ ⎪ 0 ⎪ ⎪ ⎪ ⎨ q (p + a y + a x) 1 0 0

Pr(S ≤ a) = ⎪ q 1 (p 1 − a y x 1) ⎪ ⎪ ⎪ ⎩ 1 if a < min{ā 0} if 0 ≤ a < ā if ā ≤ a < 0 if a ≥ max{0 ā}

Bounds for quality change Proposition 3. Suppose quality is a scalar. If higher values of x represent higher quality, that is, U 1 (a · η) is strictly increasing for each a and η, and Assumption 2 holds, then the marginal distribution function of CV at income y resulting from a change of (p 0 x 0) to (p 1 x 1) satisfies the following bounds:

⎫ ⎤ ⎧ ⎧ ⎡ q 1 p 1 − a + y − y y x 1 ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ max ⎬ ⎥ ⎪ ⎢ ⎪ ⎪ ≤y ⎢ y ⎪ max ⎥ p + y − y y x + q ⎪ 0 0 0 ⎢ ⎥ ⎪ ⎪ ⎪ ⎪ ⎢ ⎥ ⎪ ⎪ ⎪ ⎩ ⎭ ⎪ ⎢ ⎥ ⎪ ⎪ − 1 − q 0 (p 1 − a y x 1) 0 ⎢ ⎥ ⎪ ⎪ ⎢ ⎥ ⎪ ∈ ⎢ ⎪ ⎫ ⎥ ⎧ ⎪ ⎪ ⎢ ⎥ q 1 (p 1 − a y x 1) ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎢ ⎥ ⎪ ⎬ ⎨ ⎪ ⎢ ⎥ ⎪ ⎪ ⎢ ⎥ ⎪ min + y − y y x p q 0 0 0 ⎪ ⎦ ⎪ ⎪ ⎪ ⎪ ⎣ ⎪ ⎪ min ⎪ ⎭ ⎩ y ≥y ⎪ ⎪ + q p − a + y − y y x ⎪ 1 1 1 ⎪ ⎪ ⎪ ⎪ if a < 0 ⎪ ⎨ ⎡ ⎤ ⎧ ⎫ q 0 (p 0 + a y + a x 0)

Pr(S ≤ a) ⎪ ⎪ ⎪ ⎪ ⎪ ⎢ ⎨ ⎬ ⎥ ⎪ ⎪ ⎢ max ⎥ ⎪ q 1 p 1 − a + y − y y x 1 ⎪ ⎢ ⎥ ⎪ ⎪ ⎪ ⎪ ⎢ ⎥ ⎪ ⎪ ⎪ max − 1 ⎪ ⎢ ⎩ y ≥y+a ⎭ ⎥ ⎪ ⎪ + y − y y x + q p ⎢ ⎥ 0 0 0 ⎪ ⎪ ⎢ ⎥ ⎪ ∈ ⎢ ⎪ ⎫ ⎧ ⎞ ⎛ ⎥ ⎪ ⎪ ⎢ ⎥ q (p + a y + a x ) ⎪ ⎪ ⎪ 0 0 0 ⎪ ⎪ ⎪ ⎢ ⎥ ⎪ ⎬ ⎨ ⎪ ⎟ ⎜ ⎢ ⎥ ⎪ ⎪ ⎟ ⎜ ⎢ ⎥ ⎪ 1 min p + y − y y x q 0 0 0 ⎪ ⎣ ⎠ ⎝ ⎦ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ + min ⎪ ⎭ ⎩ ⎪ ≤y+a y ⎪ + q 1 p 1 − a + y − y y x 1 ⎪ ⎪ ⎪ ⎪ ⎪ if 0 ≤ a ≤ p 1 − p 0 ⎪ ⎪ ⎪ ⎩ = 1 if a ≥ p 1 − p 0 (44) Corollary 3. If we allow x to be multidimensional, or that utility is increasing in quality, the corresponding (wider) bounds would involve max/min over all y and not, for example, y ≤ y or y ≥ y + a, etc. For example, the first line of (44) would become ⎡ ⎤ q 1 p 1 − a + y − y y x 1 ⎢ max max − 1 − q 0 (p 1 − a y x 1) 0 ⎥ ⎥ ⎢ y + q 0 p 0 + y − y y x 0 ⎥ ⎢ ⎥ if a < 0 ⎢ ⎥ ⎢ ⎥ ⎢ q 0 p 0 + y − y y x 0 ⎦ ⎣ min q (p − a y x) min 1 1 1 y + q 1 p 1 − a + y − y y x 1 etc. Proof of Proposition 3. Note that the CV is defined as the solution S to the equation max U 0 (y η) U 1 (y − p 0 x 0 η) max U 0 (y + S η) U 1 (y + S − p 1 x 1 η)

Now, by Assumption 2(i),

Pr(S ≤ a) ( ' max U 0 (y η) U 1 (y − p 0 x 0 η) = Pr ≤ max U 0 (y + a η) U 1 (y + a − p 1 x 1 η) (45) Now, for a < 0, by Assumption 2(i). (45) reduces to

Pr(S ≤ a) ( ' max U 0 (y η) U 1 (y − p 0 x 0 η) = Pr ≤ U 1 (y + a − p 1 x 1 η) ' ( U 0 (y η) ≤ U 1 (y + a − p 1 x 1 η) = Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) (46) This probability has the Frechet upper bound given by # "

Pr U 0 (y η) ≤ U 1 (y + a − p 1 x 1 η) min # "

Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) "

# = min q 1 (p 1 − a y x 1) Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η)

Now, # "

Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) "

# = 1 − Pr U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η) "

# ≤ 1 − min Pr U 1 (y − p 0 x 0 η) ≥ U 0 y η ≥ U 1 (y + a − p 1 x 1 η) y # "

Pr U 1 (y − p 0 x 0 η) ≥ U 0 y η ≤ 1 − min max "

# − 1 0 y + Pr U 0 y η ≥ U 1 (y + a − p 1 x 1 η) q 1 p 0 + y − y y x 0 = 1 − min max − 1 0 y + q 0 p 1 − a + y − y y x 1 q 0 p 0 + y − y y x 0 = min min 1 y + q 1 p 1 − a + y − y y x 1 Replacing in (47), we get the upper bound as ⎧ q 0 p 0 + y − y y x 0 ⎪ ⎪ ⎨ min q 1 (p 1 − a y x 1) min + q 1 p 1 − a + y − y y x 1 ⎪ ⎪ y ⎪ ⎪ ⎩ ⎩ ⎧ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎭ ⎪ ⎭ If y <y, then this term exceeds q 1 (p 1 −ayx 1) q 0 p 0 + y − y y x 0 = min q 1 (p 1 − a y x 1) min y ≥y + q 1 p 1 − a + y − y y x 1 ⎫ ⎫ ⎪ ⎪ ⎪ ⎬ ⎪ ⎬ (47)

The Frechet lower bound is given by "

# Pr U 0 (y η) ≤ U 1 (y + a − p 1 x 1 η) max "

# + Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) − 1 0 q 1 (p 1 − a y x 1) = max "

# + Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) − 1 0 "

# ⎫ ⎧ Pr U 1 (y − p 0 x 0 η) ≤ U 0 y η ≤ U 1 (y + a − p 1 x 1 η) ⎬ ⎨ max y ≥ max ⎭ ⎩ − q 0 (p 1 − a y x 1) 0 ⎧ # "

⎫ ⎪ ⎪ Pr U 0 y η ≤ U 1 (y + a − p 1 x 1 η) ⎪ ⎪ ⎪ ⎨ max max ⎬ 0 ⎪ "

# y + Pr U 1 (y − p 0 x 0 η) ≤ U 0 y η − 1 ≥ max ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ − q (p − a y x) 0 ⎭ 0 1 1 ⎫ ⎧ max max q 1 p 1 − a + y − y y x 1 + q 0 p 0 + y − y y x 0 − 1 0 ⎪ ⎪ ⎪ ⎪ ⎨ ⎬ y If y≥y, then sum is less than 1, as a<0 = max ⎪ ⎪ ⎪ ⎪ ⎩ ⎭ − q 0 (p 1 − a y x 1) 0 ⎧ ⎫ ⎪ q 1 p 1 − a + y − y y x 1 + q 0 p 0 + y − y y x 0 − 1 0 ⎪ ⎨ max max ⎬ y <y = max ⎪ ⎪ ⎩ − q (p − a y x) 0 ⎭ 0 1 1 ⎫ ⎧ q 1 p 1 − a + y − y y x 1 + q 0 p 0 + y − y y x 0 ⎬ ⎨ max y <y = max ⎭ ⎩ − 1 − q 0 (p 1 − a y x 1) 0 Finally, for a ≥ 0, we get that

Pr(S ≤ a) ( ' max U 0 (y η) U 1 (y − p 0 x 0 η) = Pr ≤ max U 0 (y + a η) U 1 (y + a − p 1 x 1 η) ' ( U 1 (y − p 0 x 0 η) = Pr ≤ max U 0 (y + a η) U 1 (y + a − p 1 x 1 η) which equals 1 if a ≥ p 1 − p 0. If a < p 1 − p 0, then

Pr(S > a) ( ' U 1 (y − p 0 x 0 η) = Pr > max U 0 (y + a η) U 1 (y + a − p 1 x 1 η) ' ( U 1 (y − p 0 x 0 η) > U 0 (y + a η) = Pr U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η) The Frechet lower bound on this is given by # ⎧ "

⎫ Pr U 1 (y − p 0 x 0 η) > U 0 (y + a η) ⎪ ⎪ ⎪ ⎪ ⎨ "

# ⎬ max + Pr U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η) ⎪ ⎪ ⎪ ⎪ ⎩ ⎭ − 1 0 ⎧ ⎫ ⎪ ⎪ q 1 (p 0 + a y + a x 0) ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ ⎬ "

# ⎪ + max y

Pr

## U

(y − p x η) >

## U

η ≥

## U

(y + a − p x η) 1 0 0 0 1 1 1 ≥ max y ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ − 1 0 ⎭ ⎧ ⎫ ⎪ ⎪ q 1 (p 0 + a y + a x 0) ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ ⎬ + max p + q p q + y − y y x − a + y − y y x η 1 0 0 0 1 1 ≥ max y ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ − 2 0 ⎭

The Frechet upper bound is given by '

Pr U 1 (y − p 0 x 0 η) > U 0 (y + a η) ( U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η) # "

Pr U 1 (y − p 0 x 0 η) > U 0 (y + a η) ≤ min "

# Pr U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η) # "

Pr U 1 (y − p 0 x 0 η) > U 0 (y + a η) ≤ min "

# Pr U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η) q 1 (p 0 + a y + a x 0) = min "

# Pr U 1 (y − p 0 x 0 η) > U 1 (y + a − p 1 x 1 η) The previous two displays imply that the upper bound on Pr(S ≤ a) is given by ⎧ ⎫ ⎨ q 0 (p 0 + a y + a x 0) ⎬ min ⎩ + min q 0 p 0 + y − y y x 0 + q 1 p 1 − a + y − y y η 1 ⎭ y ⎫ ⎫ ⎧ ⎬ ⎬ ⎨ q 0 (p 0 + a y + a x 0) = min 1 ⎩ ⎩ + min q 0 p 0 + y − y y x 0 + q 1 p 1 − a + y − y y x 1 η ⎭ ⎭ ⎧ ⎨ y and a lower bound by q 0 (p 0 + a y + a x 0) max "

# Pr U 1 (y − p 0 x 0 η) ≤ U 1 (y + a − p 1 x 1 η) ⎧ ⎫ ⎨ q 0 (p 0 + a y + a x 0) ⎬ ≥ max ⎩ max q 1 p 1 − a + y − y y x 1 + q 0 p 0 + y − y y x 0 − 1 ⎭ y Putting all of this together, we get that ⎧ ⎡ ⎤ q 1 p 1 − a + y − y y x 1 ⎪ ⎪ ⎪ ⎢ max max ⎪ − 1 − q 0 (p 1 − a y x 1) 0 ⎥ ⎪ ⎢ ⎥ ⎪ y <y ⎪ + q 0 p 0 + y − y y x 0 ⎢ ⎥ ⎪ ⎪ ⎢ ⎥ ⎪ ∈ ⎪ ⎢ ⎥ ⎪ ⎪ ⎢ ⎥ p + y − y y x q ⎪ 0 0 0 ⎪ ⎣ ⎦ ⎪ min q 1 (p 1 − a y x 1) min ⎪ ⎪ ⎪ y ≥y ⎪ + q 1 p 1 − a + y − y y x 1 ⎪ ⎪ ⎪ ⎪ ⎪ if a < 0 ⎪ ⎪ ⎡ ⎤ ⎧ ⎫ ⎪ ⎪ ⎪ q 0 (p 0 + a y + a x 0) ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ ⎬ ⎨ ⎢ ⎥ ⎢ max ⎥ q 1 p 1 − a + y − y y x 1

Pr(S ≤ a) ⎢ ⎥ ⎪ ⎪ ⎪ ⎢ ⎥ ⎪ ⎪ max − 1 ⎪ ⎩ ⎭ ⎪ ⎢ ⎥ ⎪ y ≥y+a ⎪ + y − y y x + q p ⎢ ⎥ 0 0 0 ⎪ ⎪ ⎢ ⎥ ⎪ ∈ ⎪ ⎫ ⎧ ⎞ ⎛ ⎢ ⎥ ⎪ ⎪ ⎢ ⎥ q (p + a y + a x ) ⎪ ⎪ ⎪ 0 0 0 ⎪ ⎪ ⎪ ⎢ ⎥ ⎪ ⎨ ⎜ ⎪ ⎟ ⎬ ⎥ ⎢ ⎪ ⎪ ⎟ ⎜ ⎢ ⎥ 1 min p + y − y y x q ⎪ 0 0 0 ⎪ ⎠ ⎪ ⎦ ⎝ ⎣ ⎪ ⎪ ⎪ ⎪ ⎪ + min ⎪ ⎭ ⎩ ⎪ y ≤y+a ⎪ + q 1 p 1 − a + y − y y x 1 ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ if 0 ≤ a < p 1 − p 0 ⎪ ⎪ ⎩ = 1 if a ≥ p 1 − p 0 For p 0 = p 1, we have ⎧ ⎡ ⎡ ⎤ ⎤ q 1 p 0 − a + y − y y x 1 ⎪ ⎪ ⎪ ⎢ ⎢ max max ⎥ ⎪ − 1 − q 0 (p 0 − a y x 1) 0 ⎥ ⎪ ⎢ ⎢ ⎥ ⎥ ⎪ y <y ⎪ + y − y y x + q p ⎢ ⎢ ⎥ ⎥ 0 0 0 ⎪ ⎢ ⎢ ⎪ ⎥ ⎥ ⎪ ∈ ⎪ ⎢ ⎢ ⎥ ⎥ ⎨ ⎢ ⎢ ⎥ ⎥ q 0 p 0 + y − y y x 0 ⎣ ⎣ min q (p − a y x) min ⎦ ⎦

Pr(S ≤ a) 1 0 1 ⎪ ⎪ y ≥y ⎪ + q 1 p 0 − a + y − y y x 1 ⎪ ⎪ ⎪ ⎪ ⎪ if a < 0 ⎪ ⎪ ⎪ ⎩ = 1 if a ≥ 0

## References

Auerbach, A. J. (1985), “The theory of excess burden and optimal taxation.” In Handbook of Public Economics, Vol. 1, 61–127. [576] Berry, S. and P. Haile (2015), “Identification in differentiated products markets.” NBER Working Paper No. 21500. [584] Bhattacharya, D. (2015), “Nonparametric welfare analysis for discrete choice.” Econometrica, 83 (2), 617–649. [572, 577, 585, 600, 601] Blundell, R. and J. Powell (2003), “Endogeneity in nonparametric and semiparametric regression models.” In Advances in Economics and Econometrics, Cambridge University Press, Cambridge, UK. [591] Böhning, D. (1992), “Multinomial logistic regression algorithm.” Annals of the Institute of Statistical Mathematics, 44 (1), 197–200. [586] Carneiro, P., J. Das, and H. Reis (2016), “The value of private schools: Evidence from Pakistan.” Working paper, University College London. [573] Dagsvik, J. and A. Karlstrom (2005), “Compensating variation and Hicksian choice probabilities in random utility models that are nonlinear in income.” Review of Economic Studies, 72 (1), 57–76. [572, 573] Domencich, T. and D. McFadden (1975), Urban Travel Demand—A Behavioral Analysis. North-Holland, Oxford. [572] Goolsbee, A. (1999), “Evidence on the high-income Laffer curve from six decades of tax reform.” Brookings Papers on Economic Activity, Economic Studies Program, The Brookings Institution, 30 (2), 1–64. [572] Goolsbee, A. and P. Klenow (2006), “Valuing consumer products by the time spent using them: An application to the Internet.” American Economic Review, 96, 108–113. [573] Hausman, J. (1981), “Exact consumer’s surplus and deadweight loss.” The American Economic Review, 71 (4), 662–676. [572] Hausman, J. (1996), “Valuation of new goods under perfect and imperfect competition.” In The Economics of New Goods, 207–248, University of Chicago Press, Chicago.[573, 591] Hausman, J. (2003), “Sources of bias and solutions to bias in the consumer price index.” The Journal of Economic Perspectives, 17 (1), 23–44. [573] Hausman, J. A. and G. K. Leonard (2002), “The competitive effects of a new product introduction: A case study.” The Journal of Industrial Economics, 50 (3), 237–263. [573, 574] Hausman, J. and W. Newey (2016), “Individual heterogeneity and average welfare.” Econometrica, 84 (3), 1225–1248. [572] Hausman, J. and W. Newey (2017), “Nonparametric welfare analysis.” Annual Review of Economics, 9, 521–546. [572] Herriges, J. and C. Kling (1999), “Nonlinear income effects in random utility models.” The Review of Economics and Statistics, 81 (1), 62–72. [573, 575, 591] Ichimura, H. and C. Taber (2002), “Semiparametric reduced-form estimation of tuition subsidies.” American Economic Review, 2002, 286–292. [572] Kane, T. J. (2003), “A quasi-experimental estimate of the impact of financial aid on college-going.” No. w9703, National Bureau of Economic Research. [572] Kling, C. L. and C. J. Thomson (1996), “The implications of model specification for welfare estimation in nested logit models.” American Journal of Agricultural Economics, 78 (1), 103–114. [591] Knittel, C. R. and K. Metaxoglou (2014), “Estimation of random-coefficient demand models: Two empiricists’ perspective.” Review of Economics and Statistics, 96 (1), 34–59. [573] Lewbel, A. (2001), “Demand systems with and without errors.” The American Economic Review, 91 (3), 611–618. [572] Lewbel, A. and K. Pendakur (2017), “Unobserved preference heterogeneity in demand using generalized random coefficients.” Journal of Political Economy, 125 (4), 1100– 1148. [572] McFadden, D. (1973), “Conditional logit analysis of qualitative choice behavior.” [586] McFadden, D. (1981), “Econometric models of probabilistic choice.” In Structural Analysis of Discrete Data With Econometric Applications (C. F. Manski and D. McFadden, eds.), Chapter 5. MIT Press, Cambridge, MA. [572] McFadden, D. and M. K. Richter (1990), “Stochastic rationality and revealed stochastic preference.” In Preferences, Uncertainty, and Optimality: Essays in Honor of Leo Hurwicz, 161–186, Westview Press, Boulder, CO. [584] McFadden, D. and K. Train (2000), “Mixed MNL models for discrete response.” Journal of Applied Econometrics, 15 (5), 447–470. [573] Rothenberg, T. J. (1971), “Identification in parametric models.” Econometrica: Journal of the Econometric Society, 39 (3), 577–591. [587] Small, K. and H. Rosen (1981), “Applied welfare economics with discrete choice models.” Econometrica., 49 (1), 105–130. [572, 573, 593] Stiglitz, J. (2000), Economics of the Public Sector. W. W. Norton, New York. [572] Tirole, J. (1988), The Theory of Industrial Organization. MIT Press, Cambridge. [576] Train, K. (2009), Discrete Choice Methods With Simulation. Cambridge University Press, Cambridge, UK. [573, 593] Trajtenberg, M. (1989), “The welfare analysis of product innovations, with an application to computed tomography scanners.” Journal of Political Economy, 97 (2), 444–479. [573] Vytlacil, E. and N. Yildiz (2007), “Dummy endogenous variables in weakly separable models.” Econometrica, 75 (3), 757–779. [584] Willig, R., S. Salop, and F. Scherer (1991), “Merger analysis, industrial organization theory, and merger guidelines.” Brookings Papers on Economic Activity. Microeconomics, 22, 281–332. [573] Co-editor Christopher Taber handled this manuscript. Manuscript received 22 July, 2017; final version accepted 19 October, 2017; available online 23 October, 2017.
