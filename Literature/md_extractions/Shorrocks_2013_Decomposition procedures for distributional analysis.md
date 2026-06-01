# J Econ Inequal (2013) 11:99–126

DOI 10.1007/s10888-011-9214-z Decomposition procedures for distributional analysis: a unified framework based on the Shapley value

Anthony F. Shorrocks Received: 19 May 2011 / Accepted: 26 May 2011 / Published online: 7 January 2012

Keywords Inequality · Poverty · Decomposition · Shapley value

1 Introduction Decomposition techniques are used in many fields of economics to help disentangle and quantify the impact of various causal factors. Their use is particularly widespread in studies of poverty and inequality. In poverty analysis, most practitioners now employ decomposable poverty measures—especially the Foster et al. [10] family of indices—which enable the overall level of poverty to be allocated among subgroups of the population, such as those defined by geographical region, household composition, labour market characteristics or education level. Recent examples include Grootaert [11], Szekely [26], Thorbecke and Jung [28]. Other dynamic decomposition procedures are used to examine how economic growth contributes to a reduction in poverty over time, and to assess the extent to which the impact of growth is reinforced, or attenuated, by changes in income inequality: see for example, Ravallion and Huppi [20], Datt and Ravallion [6] and Tsui [29]. In the context of income inequality, decomposition techniques enable researchers to distinguish the “between-group” effect due to differences in average incomes across subgroups (males and females, say), from the “within-group” effect due to inequality within the population subgroups. Decomposition techniques have also been developed in order to measure the importance of components of income such as earnings or transfer payments.

I dedicate this paper to the memory of my mother, Vera Florence Shorrocks. A. F. Shorrocks (B) Global Economic Perspectives Ltd., London, UK e-mail: Shorrocks@wider.unu.edu Despite their widespread use, these procedures have a number of shortcomings which have become increasingly evident as more sophisticated models and econometrics are brought to bear on distributional questions. Four broad categories of problems can be distinguished. First, the contribution assigned to a specific factor is not always interpretable in an intuitively meaningful way. As Chantreuil and Trannoy [4] and Morduch and Sinclair [15] point out, this is particularly true of the decomposition by income components proposed by Shorrocks [24]. In other cases, the interpretation commonly given to a component may not be strictly accurate. Foster and Shneyerov [8], for example, question the conventional interpretation of the between-group term in the decomposition of inequality by subgroups. The second problem with conventional procedures is that they often place constraints on the kinds of poverty and inequality indices which can be used. Only certain forms of indices yield a set of contributions that sum up to the amount of poverty or inequality that requires explanation. Similar methods applied to other indices require the introduction of a vaguely defined residual or “interaction” term in order to maintain the decomposition identity. The best known example is the subgroup decomposition of the Gini coefficient, which has exercised the minds of many authors including Pyatt [19] and Lambert and Aronson [14]. A less familiar, but potentially much more serious, problem concerns the limitations placed on the types of contributory factors which can be considered. Subgroup decompositions can handle situations in which the population is partitioned on the basis of a single attribute, but have difficulty identifying the relevant contributions in multi-variate decompositions. Nor is there any established method of dealing with mixtures of factors, such as a simultaneous decomposition by subgroups (into, say, males and females) and income components (say, earnings and unearned income). As more sophisticated models are used to analyse distributional issues, these limitations have become increasingly evident. The studies by Cowell and Jenkins [5], Jenkins [12], Bourguignon et al. [3], and Bouillon et al. [1] illustrate the range of problems faced by those trying to apply current techniques to complex distributional questions. The final criticism of current decomposition methods is that the individual applications are viewed as different problems requiring different solutions. No attempt has been made to integrate the various techniques within a common overall framework. This is the main reason why it is impossible at present to combine decompositions by subgroups and income components. Yet the individual applications share certain features and objectives which enable a common structure to be formulated. Let I represent an aggregate statistical indicator, such as the overall level of poverty or inequality, and let X k, k = 1, 2, ..., m, denote a set of contributory factors which together account for the value of I. Then we can write I = f (X 1, X 2, ..., X m ), (1.1) where f (·) is a suitable aggregator function representing the underlying model. The objective in all types of decomposition exercises is to assign contributions C k to each of the factors X k, ideally in a manner that allows the value of I to be expressed as the sum of the factor contributions. The aim of this paper is to offer a solution to this general decomposition problem and to compare the results with the specific procedures currently applied to a number

Decomposition procedures for distributional analysis: a unified...

of distributional questions. In broad terms, the proposed solution considers the marginal effect on I of eliminating each of the contributory factors in sequence, and then assigns to each factor the average of its marginal contributions in all possible elimination sequences. This procedure yields an exact additive decomposition of I into m contributions. Posing the decomposition issue in the general way indicated by Eq. 1.1 highlights formal similarities with problems encountered in other areas of economics and econometrics. Of particular relevance to this paper is the classic question of cooperative game theory, which asks how a certain amount of output (or costs) should be allocated among a set of contributors (or beneficiaries). The Shapley value [22] provides a popular answer to this question. The proposed solution to the general decomposition problem turns out to be formally equivalent to the Shapley value, and is therefore referred to as the Shapley decomposition. Rongve [21] and Chantreuil and Trannoy [4] have both applied the Shapley value to the decomposition of inequality by income components, but fail to realise that a similar procedure can be used in all forms of distributional analysis, regardless of the complexity of the model, or the number and types of factors considered. Indeed, the procedure can be employed in all areas of applied economics whenever one wishes to assess the relative importance of the explanatory variables. The paper begins with a description of the general decomposition problem and the proposed solution based on the Shapley value. Section 3 shows how the procedure may be applied to three issues concerned with poverty: the effects of growth and redistribution on changes in poverty; the conventional application of decomposable poverty indices; and the impact of population shifts and changes in within-group poverty on the level of poverty over time. Section 4 looks in more detail at the features of the Shapley decomposition in the context of a hierarchical model in which groups of factors may be treated as single units. This leads to a discussion of the two-stage Shapley procedure associated with the Owen value [18]. A number of results in this section establish the conditions under which the Shapley and Owen decompositions coincide, and indicate several ways of simplifying the calculation of the factor contributions. These results are then used to generate the Shapley solution to the multi-variate decomposition of poverty by subgroups, a problem which has not been solved before. In Sections 5 and 6, attention turns to inequality analysis, beginning with decomposition by subgroups using the Entropy and Gini measures of inequality. This is followed by a discussion of the application of the Shapley rule to decomposition by source of income. The main purpose of these applications is to see how the Shapley procedure compares with existing techniques in the context of a variety of standard decomposition problems. The overall results are encouraging. In all cases, the Shapley decomposition either replicates current practice or (arguably) provides a more satisfactory method of assigning contributions to the explanatory factors. However, the greatest attraction of the procedure proposed in this paper is that it overcomes all four of the categories of problems associated with present techniques. As a consequence, it offers a unified framework capable of handling any type of decomposition exercise. After summarising the principal findings of this paper the Appendix section briefly discusses the wide range of potential applications to issues which have not previously been considered candidates for decomposition analysis.

Consider a statistical indicator I whose value is completely determined by a set of m contributory factors, X k, indexed by k ∈ K = {1, 2, ..., m} so that we may write I = f (X 1, X 2, ..., X m ), (2.1) where f (·) describes the underlying model. In the applications examined later, the indicator I will represent the overall level of poverty or inequality in the population, or the change in poverty over time. The factor X k may refer to a conventional scalar or vector variable, but other interpretations are possible and often desirable; for the moment it is best regarded as a loose descriptive label capturing influences like “uncertain returns to investments”, “differences in household composition” or “supply-side effects”. In what follows, we imagine scenarios in which some or all of the factors are eliminated, and use F(S) to signify the value that I takes when the factors X k, k ∈ / S, have been dropped. As each of the factors is either present or absent, it is convenient to characterise the model structure K, F in terms of the set of factors (or, more accurately, “factor indices”), K, and the function F: {S | S ⊆ K} → R. Since the set of factors completely accounts for I, it will also be convenient to assume throughout that F(∅) = 0: in other words, that I is zero when all the factors are removed. 1 A decomposition of K, F is a set of real values C k, k ∈ K, indicating the contribution of each of the factors. A decomposition rule C is a function which yields a set of factor contributions

C k = C k (K, F), k ∈ K, (2.2) for any possible model K, F. In seeking to construct a decomposition rule, several desiderata come to mind. First, that it should be symmetric (or anonymous) in the sense that the contribution assigned to any given factor should not depend on the way in which the factors are labelled or listed. Secondly, that the decomposition should be exact (and additive), so that

C k (K, F) = F(K), (2.3) k∈K for all K, F. When condition (2.3) is satisfied, it is meaningful to speak of the proportion of observed inequality or poverty attributable to factor k. It is also desirable that the contributions of the factors can be interpreted in an intuitively appealing way. In this respect, the most natural candidate is the rule which equates the contribution of each factor to its (first round) marginal impact M k (K, F) = F(K) − F(K\{k}), k ∈ K.

(2.4) This decomposition rule is symmetric, but will not normally yield an exact decomposition. A second possibility is to consider the marginal impact of each of the factors when they are eliminated in sequence. Let σ = (σ 1, σ 2, ..., σ m) indicate

1 If F(·) is derived from an econometric model, this constraint will usually mean that one of the factors represents the unexplained residuals. When the constraint is not satisfied automatically, I can always be renormalised so that it measures the “surplus” due to the identified factors.

Decomposition procedures for distributional analysis: a unified... the order in which the factors are removed, and let S(σ r, σ) = {σ i | i > r} be the set of factors that remain after factor σ r has been eliminated. Then the marginal impacts are given by C k σ = F(S(k, σ) ∪ {k}) − F(S(k, σ) = k F(S(k, σ )), k ∈ K, (2.5) where k F(S) ≡ F(S ∪ {k}) − F(S),

S ⊆ K\{k}, (2.6) is the marginal effect of adding factor k to the set S. Using the fact that S(σ r, σ) = S(σ r+1, σ) ∪ {σ r+1} for r = 1, 2, ..., m − 1, we deduce m m

C k σ =

C σ σ r = [F(S(σ r, σ) ∪ {σ r }) − F(S(σ r, σ ))] k∈K r=1 r=1 = F(S(σ 1, σ) ∪ {σ 1 }) − F(S(σ m, σ )) = F(K) − F(∅) = F(K).

(2.7) The decomposition (2.5) is therefore exact. However, the value of the contribution assigned to any given factor depends on the order in which the factors appear in the elimination sequence σ, so the factors are not treated symmetrically. This “path dependence” problem may be remedied by considering the m! possible elimination sequences, denoted here by the set, and by computing the expected value of C k σ when the sequences in are chosen at random. This yields the decomposition rule C S given by 1 1

C k σ = k F(S(k, σ )) σ ∈ σ ∈ m!

m!

m−1 1 = k F(S)

S ⊆ K\{k} σ ∈ s=0 |S | = s m!

S(k, σ) = S

C k S (K, F) = = m−1 s=0

S ⊆ K\{k} |S | = s (m − 1 − s)!s!

k F(S).

m!

(2.8) Using π(s, m − 1) = (m − 1 − s)!s!/m! to indicate the relevant probability, 2 Eq. 2.8 is expressed more succinctly as π(|S |, |K\{k}|) k F(S) = E S⊆K\{k} k F(S), k ∈ K, (2.9)

C k S (K, F) =

S⊆K\{k} where E S⊆L is the expectation taken with respect to the subsets of L. From Eq. 2.7 it is clear that C S is an exact decomposition rule, and also one which treats the factors symmetrically. Furthermore, the contributions can be interpreted as the expected marginal impact of each factor when the expectation is taken over all the possible elimination paths. Expression 2.8 will be familiar to many readers, since it corresponds to the Shapley value for the cooperative game in which “output” or “surplus” F(K) is shared amongst the set of “inputs” or “agents” K (see, for example, Moulin [16], Chapter 5). The application to distributional analysis is quite different from the context in which 2 π(|S |, | M |) is the probability of randomly selecting the subset S from M, given that all subset sizes from 0 to | M | are equally likely.

the Shapley value was conceived, and the results therefore need to be reinterpreted. Nevertheless, it seems convenient and appropriate to refer to Eq. 2.8 as the Shapley

3 Applications of the Shapley Decomposition to Poverty Analysis To illustrate how the Shapley decomposition operates in practice, this section looks at three simple applications to poverty analysis.

## 3.1 The impact of growth and redistribution on the change in poverty

An important issue in development economics concerns the extent to which economic growth helps to alleviate poverty. With a fixed real poverty standard, growth is normally expected to raise the incomes of some of the poor, thereby reducing the value of any conventional poverty index. However, this tendency can be moderated, or even reversed, if economic growth is accompanied by redistribution in the direction of increased inequality.

Datt and Ravallion [6] suggest a method for separating out the effects of growth and redistribution on the change in poverty between two points of time. Given a fixed poverty line, the poverty level at time t (t = 1, 2) may be expressed as a function P(μ t, L t) of mean income μ t and the Lorenz curve L t. Denoting the growth factor by G = μ 2 /μ 1 − 1, and the redistribution factor by R = L 2 − L 1, 4 the problem becomes one of identifying the contributions of growth G and redistribution

R in the decomposition of P = P(μ 2, L 2) − P(μ 1, L 1) = P(μ 1 (1 + G), L 1 + R) − P(μ 1, L 1) = F(G, R).

(3.1) Figure 1 illustrates the basic structure of the Shapley decomposition for this example, which is particularly simple given that there are just two factors, G and R, and hence only two possible elimination sequences. Eliminating G before R produces the path portrayed on the left, with the marginal contribution F(G, R) − F(R) for the growth factor, and the contribution F(R) for the redistribution effect. Repeating the exercise for the right-hand path, and then averaging the results, yields the Shapley contributions 1

## S

## C G

## = [F(G, R) − F(R) + F(G)]

2 1 (3.2)

## C SR = [F(G, R) − F(G) + F(R)]

2

3 Several characterisations of the Shapley value are available, and may be reinterpreted in the present framework. For example, Eq. 2.8 is the only symmetric and exact decomposition rule which, for each k, yields contributions C k (K, F) that depend only on the set of marginal effects {k F(S) | S ⊆ K\{k}} relating to factor k [30]. 4 This is a slight abuse of notation, as the growth and redistribution factors ought to be distinguished from the variables representing growth and redistribution. However, in this example, the growth and redistribution factors are eliminated by setting G and R equal to zero, so no serious confusion arises. Factors and variables are distinguished more carefully in later sections.

Decomposition procedures for distributional analysis: a unified...

decomposition for the growth and redistribution components of the change in poverty When growth is absent, G takes the value 0 and the change in poverty becomes F(R) = P(μ 1, L 2) − P(μ 1, L 1) = D L P(μ 1, L), (3.3) where D L P(μ, L) = P(μ, L 2) − P(μ, L 1) indicates the rise in poverty due to a shift in the Lorenz curve from L 1 to L 2, holding mean income constant at μ. Conversely, eliminating the redistribution factor by setting R = 0 yields F(G) = P(μ 2, L 1) − P(μ 1, L 1) = D μ P(μ, L 1 ), (3.4) where D μ P(μ, L) = P(μ 2, L) − P(μ 1, L), is the rise in poverty due to a change in mean income from μ 1 to μ 2, with the fixed Lorenz curve L. The Shapley contributions for the growth and redistribution effects are therefore given by

## S

=

## C G

1

## [F(G, R) − F(R) + F(G)]

2 = 1 [P(μ 2, L 2) − P(μ 1, L 2) + P(μ 2, L 1) − P(μ 1, L 1 )] 2 = 1 D μ P (μ, L 1) + D μ P (μ, L 2) 2

## C SR =

1 [D L P(μ 1, L) + D L P(μ 2, L)]. 2 (3.5) These contributions sum up, as expected, to the overall change in poverty, and

## S

have intuitively appealing interpretations. The growth component, C G , indicates the rise in poverty due to a shift in mean income from μ 1 to μ 2, averaged with respect to the Lorenz curves prevailing in the base and final years, while the redistribution effect, C SR, represents the average impact of the change in the distribution of relative incomes, with the average taken with respect to the mean income levels in the two periods. Despite the attractions of the Shapley decomposition values given in Eq. 3.5, these are not the contributions proposed by Datt and Ravallion [6]. Instead, they associate the growth and redistribution effects with the marginal change in poverty starting from the base year situation. This yields the contributions C G = D μ P(μ, L 1) and C R = D L P(μ 1, L). 5 These do not sum to the observed change in poverty, so Datt and Ravallion are obliged to introduce a residual term E into their decomposition equation

## P = C G + C R + E.

(3.6) They acknowledge the criticisms which can be levelled against the residual component, and note that it can be made to vanish by averaging over the base and final years, as is done in Eq. 3.5. However, this solution is rejected as being arbitrary ([6], footnote 3). Far from being arbitrary, the above analysis suggests that this is exactly the outcome which results from applying a systematic decomposition procedure to the growth-redistribution issue. Furthermore, the general framework outlined in Section 2 offers the chance of extending the analysis to cover not only changes in the poverty line, but also more disaggregated influences such as changes in mean incomes and income inequality within the modern and traditional sectors.

## 3.2 Decomposable poverty indices

Another standard application of decomposition techniques involves the use of decomposable poverty indices. When assigning contributions to subgroups of the population, such indices enable the overall degree of poverty, P, to be written

## P =

m ν k P k, (3.7) k=1 where ν k and P k respectively indicate the population share and poverty level associated with subgroup k ∈ K = {1, 2, ..., m}. Indices with this property—especially the family of measures proposed by Foster et al. [10]—are nowadays used routinely to study the way in which differences according to region, household size, age, and education attainment contribute to the overall level of poverty. In many respects, this is the simplest and most clear-cut application of decomposition techniques. Suppose, for instance, that the population is partitioned into m regions. Then factor k can be interpreted as “poverty within region k”, and the question of interest is the contribution which this factor makes to poverty in the whole country. Adopting the notation of Section 2, the model structure K, F is defined by

## F(S) =

ν k P k, (3.8) k∈S so k F(S) = ν k P k, for all S ⊆ K\{k}.

(3.9) Since eliminating poverty in region k reduces aggregate poverty by the amount ν k P k regardless of the order in which the regions are considered, it follows from Eqs. 2.4 terms correspond to the first round marginal effects; in other words, C G = M G ({G, R}, F) and C R = M R ({G, R}, F) in the notation of Eq. 2.4. 5 These

Decomposition procedures for distributional analysis: a unified...

and 2.9 that these values yield both the first round marginal effects and the terms in the Shapley decomposition; in other words C k S (K, F) = M k (K, F) = ν k P k, k ∈ K.

(3.10) Not surprisingly, this allocation of poverty contributions to population subgroups accords exactly with common practice. A more complex situation emerges if we wish to perform a simultaneous decomposition by more than one attribute. In fact there is no recognised procedure at present for dealing with this problem. Suppose, for instance, that the population is subdivided into m 1 regions indexed by K and m 2 age groups indexed by L. This yields a total of m 1 m 2 region-age cells which, if treated separately, can be assigned contributions as before, by replacing Eq. 3.7 with ν k P k, (3.11)

## P =

k∈K ∈L where the subscripts k refer to region k and age group. However, we are more likely to be interested in the overall impact of poverty in region k, or in age group, rather than the contribution of the subgroup corresponding to region k and age group . In other words, what we really seek are the m 1 + m 2 contributions associated with the regional and age factors. The Shapley procedure offers a solution to this problem by defining the model structure K ∪ L, F where

## F(S ∪ T) =

ν k P k, S ⊆ K, T ⊆ L.

(3.12) k∈S ∈T

Eliminating poverty in region k now yields ν k P k = k F(T), k F(S ∪ T) =

S ⊆ K\{k}, T ⊆ L.

(3.13)

## ∈T

In contrast to Eq. 3.9 above, Eq. 3.13 shows that the factors no longer operate independently: the marginal impact of removing poverty in region k depends on whether poverty has already been eliminated in one or more of the age groups. To obtain the Shapley contributions for the regions, first note that {S | S ⊆ M} = {M\S | S ⊆ M} and π(|S |, | M |) = π(| M\S |, | M |), so 1

## E S⊆M F(S) = E S⊆M [F(S) + F(M\S)].

2

Note also that Eq. 3.13 implies k F(S) + k F(M\S) = ν k P k +

## ∈S∩L

ν k P k = k F(M ∩ L), (3.14) (3.15)

## ∈(M\S)∩L

for all S ⊆ M ⊆ K ∪ L. So choosing any k ∈ K and setting M = L ∪ K\{k} yields

1 E S⊆M k F(S) + k F(M\S) 2 1 1 1 ν k P k, = E S⊆M k F(L) = k F(L) = C k S (K ∪ L, F) = E S⊆M k F(S) =

## ∈L

(3.16) or equivalently, in the notation of Eq. 3.7, C k S (K ∪ L, F) = 1 ν k P k 2 (3.17) Thus, in this two attribute example, each region is assigned exactly half the contribution that would be obtained in a decomposition by region alone. A similar result applies to the age group factors. More generally, in a simultaneous decomposition by n attributes, each factor is allocated one nth of the contribution obtained in the single attribute decomposition. 6 This result will be comforting to those who use decomposable poverty indices, for it shows that nothing is lost by looking at each attribute in isolation; the outcomes of multi-attribute decompositions can be calculated immediately from the series of single attribute results, and the relative importance of different subgroups remains the same, regardless of the number of attributes considered.

## 3.3 Changes in poverty over time

Decomposable poverty indices can also be used to identify the subgroup contributions to poverty changes over time. If ν kt and P kt represent the population share and poverty level of subgroup k ∈ K at time t (t = 1, 2), Eq. 3.7 yields [ν k2 P k2 − ν k1 P k1].

## P =

(3.18) k∈K The aim here is to account for the overall change in poverty, P, in terms of changes in poverty within subgroups, P k = P k2 − P k1, k ∈ K, and the population shifts between subgroups, ν k = ν k2 − ν k1, k ∈ K. The subgroup poverty values can be changed independently, so the poverty change factors may be indexed by the set K p = {p k, k ∈ K}.However the population shifts necessarily sum to zero. To avoid complications at this stage, the population shift factors will be treated as a single composite factor, denoted by K s. The model structure K p ∪ {K s },F is then given by [ν k (T)P k (S) − ν k1 P k1 ], S ⊆ K p, T ⊆ {K s }, (3.19)

## F(S ∪ T) =

k∈K where

P k (S) =

P k2 if p k ∈ S

P k1 if p k ∈ S ;

ν k (T) = ν k2 if T = K s ν k1 if T = ∅ .

(3.20) For each p k ∈ K p we have p k F(S ∪ T) = ν k (T)P k (S ∪ {p k }) − ν k (T)P k (S) = ν k (T)P k,

6 See

Proposition 4 in the next section.

S ⊆ K p \{p k },

T ⊆ {K s }, (3.21) Decomposition procedures for distributional analysis: a unified... and setting M = {K s} ∪ K p \{p k }, it follows that p k F(S) + p k F(M\S) = ν k (S ∩ {K s })P k + ν k ((M\S) ∩ {K s })P k = (ν k1 + ν k2 )P k, (3.22) for all S ⊆ M. So, using Eq. 3.14, the Shapley contribution associated with the change in poverty within subgroup k is given by 1 E S⊆M p k F(S) + p k F(M\S) 2 1 ν k1 + ν k2 = E S⊆M (ν k1 + ν k2 )P k =

P k.

2 2 C Sp k = E S⊆M p k F(S) =

Conversely K s F(S) = [ν k (K s) − ν k (∅)] P k (S) = k∈K

P k (S)ν k,

S ⊆ K p.

(3.23) (3.24) k∈K

So 1 E S⊆K p K s F(S) + K s F(K p \S) 2 P k (S) + P k (K p \S) ν k

## S

= E S⊆K p K s F(S) =

## C K

s 1

E S⊆K p k∈K 2 1

P k1 + P k2 ν k = E S⊆K p [P k1 + P k2 ]ν k = (3.25) k∈K k∈K 2 2 This is a very natural allocation of contributions given that we seek a decomposition which treats the factors in a symmetric way, and given that Eq. 3.18 may be rewritten ν k1 + ν k2

P k1 + P k2

## P =

P k + ν k.

(3.26) 2 2 = k∈K k∈K

4 Hierarchical structures Despite its attractive properties, the Shapley decomposition has one major drawback for distributional analysis: the contribution assigned to any given factor is usually sensitive to the way in which the other factors are treated. In many applications, certain groups of factors naturally cluster together. This leads to a hierarchical structure comprising a set of primary factors, each of which is subdivided into a (possibly single element) group of secondary factors. For example, when income inequality is decomposed by source of income (see Section 6 below), one may first wish to regard income as the sum of labour income, investment income and transfers. Then investment income, say, might be split into interest, dividends, capital gains and rent. The Shapley decomposition does not guarantee that the contribution assigned to earnings will be the same if investment income is treated as a single entity or viewed in terms of its separate components. Nor does it ensure that the inequality contributions assigned to the components of investment income sum to the contribution of investment income treated as a single unit. To study this issue in more detail, consider a hierarchical model K, A, F consisting of a set of m secondary factors indexed by K, and a partition of K into a set of primary factors A = {L j, j ∈ J}. The fine (i.e. secondary factor) structure of the model is denoted by K, F. Replacing each set of secondary factors with its corresponding primary factor produces the aggregated model A, F A defined by

## F A (T) = F(K T ),

## T ⊆ A,

(4.1) where

## K T = ∪ L∈T L,

## T ⊆ A,

(4.2) denotes the set of secondary factors covered by the subset T of primary factors. More generally, substituting a subset B ⊆ A of primary factors for their corresponding groups of secondary factors produces the partially aggregated model B ∪ K\K B, F B defined by F B (S ∪ T) = F(S ∪ K T ),

## S ⊆ K\K B,

## T ⊆ B.

(4.3) A decomposition rule for hierarchical models is a function C ∗ which assigns the contribution C k ∗ (K, A, F) to each secondary factor k ∈ K, and the contribution C ∗ L (K, A, F) to each primary factor L ∈ A. It will be said to be aggregation consistent for the model K, A, F if

## C ∗ L (K, A, F) =

C k ∗ (K, A, F), each L ∈ A, (4.4) k∈L or in other words, if the contribution of each primary factor is the sum of the contributions of its constituents. Applying the Shapley decomposition both to the fine model structure K, F and to the aggregated model A, F A produces the hierarchical decomposition rule C k S (K, A, F) = C k S (K, F), k ∈ K;

C L S (K, A, F) = C L S (A, F A ),

## L ∈ A. (4.5)

As already mentioned, this procedure does not ensure aggregation consistency. However, the problem can be overcome by adopting a sequential Shapley approach along the lines proposed by Owen [18]. First, contributions are allocated as above to each of the primary factors using the Shapley decomposition of the aggregated model A, F A. This yields C L O (K, A, F) = C L S A, F A = E T⊆A\{L} F A (T ∪ {L}) − F A (T) = E T⊆A\{L} [F(K T ∪ L) − F(K T )] = F̄ L (L), each L ∈ A, (4.6) where F̄ L (S) = E T⊆A\{L} F(K T ∪ S) − F(K T),

## S ⊆ L, L ∈ A.

(4.7) The contribution of each primary factor L is then allocated amongst its constituents, by applying the Shapley decomposition to L, F̄ L:

C k O (K, A, F) = C k S (L, F̄ L) = E S⊆L\{k} k F̄ L (S) = E T⊆A\{L} E S⊆L\{k} k F(K T ∪ S), k ∈ L, L ∈ A.

(4.8)

Decomposition procedures for distributional analysis: a unified...

As the Shapley decomposition is exact, it follows that

C k O (K, A, F) = C k S (L, F̄ L) = F̄ L (L) k∈L k∈L = C L O (K, A, F), each L ∈ A.

(4.9) So this two-stage procedure is always aggregation consistent. 7 Although the hierarchical form of the Shapley rule is not usually aggregation consistent, there is one important exception. Let us say that the function F: {S |S ⊆ K} → R is separable over L ⊆ K if k F(S ∪ T) = k F(S), all k ∈ L, T ⊆ L\{k}, S ⊆ K\L;

(4.10) in other words, the marginal contribution of each factor k ∈ L does not depend on the other factors in L. Note that if F is separable over L, then F is also separable over any subset of L. Note also that if T is written as T = {k 1, k 2, ..., k t }, then it follows from (4.10) that t

## F(S ∪ T) − F(S) =

k r F(S ∪ {k 1, ..., k r−1 }) r=1 k F(S), all T ⊆ L, S ⊆ K\L, (4.11) = k∈T so the marginal effect of introducing any group T of factors from the subset L is the sum of the marginal effects of introducing each factor separately. We now obtain: Proposition 1 Consider the model K, F, and suppose F is separable over L ⊆ K. Then C k S (K, F) = C k S ({L} ∪ K\L, F {L} ), k ∈ K\L (4.12a)

## S

C k S (K, F) = C {L}

## ({L} ∪ K\L, F {L})

(4.12b) C k S (K, F) = C k S (K\L ∪ {k}, F), (4.12c) k∈L k ∈ L where F {L} is def ined in Eq. 4.3. Proof See Appendix. Proposition 1 establishes three things. Equation 4.12a shows that treating a separable subset L as a single entity in the Shapley decomposition does not affect the contributions assigned to the factors outside L. As a consequence, the sum of the contributions of the factors in L must equal the contribution of the grouped factor in the more aggregated model, as indicated in Eq. 4.12b. Finally, Eq. 4.12c shows that the contribution of any factor k in a separable set L can disregard the complementary set of factors L\{k}.

7 The two-stage decomposition can be extended to a multi-stage procedure if the secondary factors are divided into tertiary factors, and so on.

Framed in terms of hierarchical structures, Proposition 1 implies that any separable set of secondary factors can be replaced by its corresponding primary factor without altering the contributions of the other factors. This process may be repeated for further separable groups of factors, thereby establishing: Proposition 2 Consider the hierarchical model K, A, F, and suppose that F is separable over each L ∈ A. Then, for all L ∈ A and all k ∈ L, we have C k S (K, F) = C k O (K, A, F) = E T⊆A\{L} k F(K T) = k F̄ L (∅).

(4.13) So the Shapley and Owen decompositions coincide, and the Shapley decomposition is aggregation consistent. Proof See Appendix. The results of Proposition 2 enable several short-cuts to be implemented in the calculation of the Shapley contributions. While the requirement that F is separable over each L ∈ A may seem very restrictive, it should be noted that F is (trivially) separable over any single element subset of K. So it is always possible to apply Proposition 2, by treating any non-separable subsets of factors as a set of single factors in the partition A of K. If F is not separable over the primary factor L, then Proposition 2 leads us to expect that the Shapley contributions of the secondary factors k ∈ L will not be obtained by the Owen two-stage method. In such situations, it may well be the case that the Owen procedure is favoured, in order to ensure an aggregation consistent decomposition. However, there are likely to be several alternative ways in which secondary factors can be grouped together into primary factors, leaving room for judgements about the most appropriate arrangement. In the general structural model denoted by K, F, factors can interact in complex ways, and there is nothing to prevent some of the factors being redundant in the sense that a proper subset of K completely accounts for the initial level, F(K), of the statistic under examination. This will be captured by saying that the set of factors L ⊆ K is suf f icient if F(S) = 0 for all S ⊆ K\L. The sufficiency property leads to a powerful result when combined with the results of Proposition 2. For if each of the primary factors L ∈ A are sufficient in the hierarchical model K, A, F then, for all L ∈ A, all T ⊆ A\{L}, and all S ⊆ L, we have

## F(K T ∪ S) = 0

(4.14) unless T = A\{L} and S = ∅. So

## F̄ L (S) =

1 1

## F(K A\{L} ∪ S) =

## F(K\L ∪ S),

## |A |

## |A |

## S ⊆ L,

(4.15) and, if F is separable over L, then k F̄ L (S) = 1 1 k F(K\{k}) =

M k (K, F),

## |A |

## |A |

k ∈ L, S ⊆ L\{k}, (4.16)

Decomposition procedures for distributional analysis: a unified...

in the notation of Eq. 2.4. Combined with Proposition 2, this yields: Proposition 3 For the hierarchical model K, A, F, suppose that F is separable over each L ∈ A, and that each L ∈ A is suf f icient. Then C k S (K, F) = C k S (L, F̄ L) =

1 M k (K, F), |A | k ∈ L, L ∈ A.

(4.17) Thus, in the context described, the Shapley contributions are determined solely by the number of primary factors, |A |, and the f irst round marginal ef fects, M k (K, F). The implications of Proposition 3 are well illustrated by returning to the example of decomposable poverty indices discussed in Section 3.2, which can now be extended easily to the general multivariate case by defining the primary factors in terms of the attributes (region, household size, etc.), and the secondary factors in terms of the attribute subgroups. To be specific, suppose K is partitioned into A = {L j, j ∈ J}, where L j refers to attribute j, and k ∈ L j is the factor representing poverty within category k of attribute j. Then the hierarchical model K, A, F is characterised by j j

## F(S) =

ν k P k (S), each j ∈ J, S ⊆ K, (4.18) k∈L j ∩S j j where ν k and P k (S) respectively indicate the population share and poverty level associated with category k of attribute j after the factors in the set K\S have been removed, and where j j P k (S ∪ T) = P k (S ∪ {k}), all j ∈ J, S ⊆ K\L j, T ⊆ L j, (4.19) since the poverty level associated with category k ∈ L j is not affected by eliminating poverty in the categories L j \{k}. Condition (4.19) implies that the function F is separable over each L j ∈ A. Furthermore, F(S) = 0 for S ⊆ K\L j, so each of the primary factors L j, j ∈ J, is sufficient. It therefore follows from Proposition 3 and Eq. 4.16 that

C k S (K, F) = 1 1 j j

M k (K, F) = ν P (K),

## | J |

| J | k k all k ∈ L j, j ∈ J.

(4.20) This establishes: Proposition 4 When a decomposable poverty index is employed in a multivariate poverty decomposition with n attributes, the Shapley contribution associated with category k of attribute j is given by

C k S = j 1 j j ν P, n k k (4.21) j where ν k is the population share associated with category k of attribute j and P k is the poverty level observed for this category. The intuition behind this result is clear. Each of the n attributes accounts for the overall poverty level P, and must therefore be assigned the contribution P/n, given that the factors are treated symmetrically. Furthermore, the secondary factors associated with any attribute operate independently (in the sense captured by the separability property), so the contribution of each attribute is allocated amongst its constituent factors in proportion to their marginal effect.

5 Inequality decomposition by subgroups The results obtained in the preceding section assist in the analysis of some of the other standard applications of decomposition methods. We first consider the question of decomposing inequality by subgroups, a topic pioneered by Theil [27] and later developed by Bourguignon [2], Shorrocks [23, 25], and Foster and Shneyerov [8, 9], amongst others. The problem may be posed in terms of a set of individuals N = {1, 2, ..., n} with income vector y and mean income μ, which is partitioned into a set of subgroups N k (k = 1, 2, ..., m) with vectors y k and means μ k. Without loss of generality, it may be assumed that the subgroups are numbered so that μ 1 ≤ μ 2 ≤ ... ≤ μ m, and that each of the subgroup income vectors is arranged in increasing order. For each subgroup k, denote the (ordered) vector of relative incomes by w k = y k /μ k, the relative mean income by b k = μ k /μ, and the share of the population by ν k. Then for any inequality index I(·) which is symmetric and scale invariant (i.e. homogeneous of degree zero), the overall level of inequality can be expressed as I y 1, y 2, ..., y m = I w 1 b 1, w 2 b 2,..., w m b m = Ī w 1, w 2,..., w m, b, (5.1) where b = (b 1, ..., b m ). In this framework, decomposition of inequality by subgroups is typically viewed as the exercise which assigns contributions to inequality within each subgroup (as captured in the vectors w k ), and to the “between-group” effect (as captured by b). We will think of these as the within-group factors, indexed by K = {1, 2,..., m}, and the between-group factor indexed by the (single element) set L.

## 5.1 Entropy indices

Subgroup inequality decomposition is most often undertaken using an inequality measure drawn from the entropy family E c (y) = E c (y 1, ..., y n) = 1 φ c (y i /μ), n (5.2) i∈N where φ c (t) = (t c − 1)/[c(c − 1)], c = 0, 1; φ 1 (t) = t ln t; and φ 0 (t) = − ln t. These indices yield the decomposition equation E c y 1, y 2, ..., y m = Ē c w 1, w 2, ..., w m, b = m k=1 m ν k b ck E c w k + ν k φ c (b k ).

(5.3) k=1 It is standard practice to allocate the contribution W k = ν k b ck E c w k, k = 1, 2, ..., m, (5.4)

Decomposition procedures for distributional analysis: a unified...

to the within-group factors, on the grounds that W k is the amount by which overall inequality falls when incomes within subgroup k are redistributed equally. The remaining “between group component”

## B =

m ν k φ c (b k) (5.5) k=1 is the level of inequality which results when the incomes of all individuals are replaced by the mean of the subgroup to which they belong, and is usually regarded as the contribution of the between-group factor. Although this procedure yields an exact decomposition of inequality, the interpretation of the between-group component, B, is questionable. As Foster and Shneyerov [8] point out, eliminating the between-group factor not only removes the component B but also changes the weights attached to the subgroup inequality values in the within-group component. If the between-group factor is eliminated by setting each b k = 1, 8 then the (first round) marginal effect is

## B =

m m ν k b ck − 1 E c w k + ν k φ c (b k ).

k=1 (5.6) k=1 Removing the within-group factors in subsequent rounds produces the contributions (5.7) W k = ν k E c w k, k = 1, 2, ..., m.

The expressions for B and B coincide only when c = 0, corresponding to the mean logarithmic deviation index, E 0. In all other cases the standard practice of assigning the contributions according to Eqs. 5.4 and 5.5 rests on the implicit assumption that the between-group factor is eliminated last. The Shapley decomposition treats the factors symmetrically, and consequently yields an intermediate solution. Defining K and L as above, and setting A = {K, L}, yields the hierarchical model K ∪ L, A, F where

## F(S ∪ T) =

W k (T) + B(T), S ⊆ K, T ⊆ L, (5.8) k∈S with W k (L) = W k; W k (∅) = W k; B(L) = B; B(∅) = B. Since k F(S ∪ T) = W k (T), k ∈ K, S ⊆ K\{k}, T ⊆ L, (5.9) the function F is separable over K, and also (trivially) over L. So by Proposition 2 the Shapley contributions may be obtained via the Owen two-stage procedure. This gives 1 1

## [F(K ∪ L) − F(L) + F(K)] =

W k + W k k∈K 2 2 1

## C L S (K ∪ L, A, F) =

## B + B

(5.10) 2

S C K (K ∪ L, A, F) =

8 While it is usual to eliminate the between group factor by setting each b = 1, there is no compelling k reason for doing so. We follow standard practice here, but note that setting each b k = β > 0 results in only minor modifications to the analysis.

as the contributions of the primary factors, and 1 1 [k F(∅) + k F(L)] =

W k + W k, 2 2 C k S (K ∪ L, A, F) = k ∈ K, (5.11) as the contributions of the individual within-group factors.

As already mentioned, standard practice assigns the within-and between-group inequality contributions given by Eqs. 5.4 and 5.5. The Shapley decomposition generates the same assignment when the mean logarithmic deviation index, E 0, is chosen as the measure of inequality, but the results will not be the same when other indices are employed. 9 While the Shapley decomposition departs from common practice, there is a compelling logic behind the assignment rule, and to that extent it offers a potential improvement over current methods.

## 5.2 The Gini coefficient

Numerous attempts have been made to decompose the Gini coefficient along similar lines to Eq. 5.3. Using the notation described earlier in this section, the most common method may be formulated by supposing that person i occurs in the ith position when the distribution is written y = y 1, y 2, ..., y m, and in position r i when all incomes are arranged in increasing order. 10 The value of the Gini coefficient is then given by

G(y) = 2 n 2 μ r i (y i − μ) (5.12) i∈N and yields the decomposition equation 2 m r i (y i − μ) G = G y 1, y 2, ..., y m = 2 k=1 i∈N k n μ 2 m = 2 i(y i − μ k) + i(μ k − μ) + (r i − i)y i i∈N k i∈N k i∈N k k=1 n μ

## = W + B + R,

(5.13) where k 2 2 2 = i − μ ν b

## G

y = ν k b k G w k ) (y i k k k n 2 μ m

## W =

k=1 i∈N k m m k=1 k=1 is a weighted sum of the within-group inequality values, and ⎡ ⎤ m m k m 2 i(μ k − μ) = b k ν k ⎣ ν j − ν j ⎦

## B = 2

n μ j=1 k=1 i∈N k k=1 (5.14) (5.15) j=k

9 The methods may be reconciled by explicitly recognising the different treatment of the within-and between-group factors. This may be done by redefining the problem so that the between-group term is separated out, and the question becomes one of allocating contributions to the within-group factors in the decomposition of I − B. 10 For convenience it is assumed that all incomes are distinct, and hence that r i is uniquely defined.

Decomposition procedures for distributional analysis: a unified...

is the “between-group component”, indicating the value of the Gini coefficient when all incomes are replaced by the mean income of the subgroup to which they belong. The final term, R, in Eq. 5.13 is a residual or “interaction” effect which vanishes when the subgroup income ranges do not overlap (so that r i = i, for all i), and is otherwise strictly positive. The Gini decomposition (5.13) is less satisfactory than the corresponding Entropy formulation (5.13), because the interaction term introduces a third, vaguely specified, element into the equation. It is difficult to predict how the interaction effect will respond to changes in subgroup characteristics, such as a narrowing of income differentials between subgroups. As a consequence, the overall Gini value may react perversely to such changes: for example, a reduction in inequality in every subgroup may cause overall inequality to rise, even when the subgroup means and sizes are held constant. The Shapley decomposition cannot overcome this “subgroup inconsistency” problem, since this is a fundamental property of the Gini index. However, it does remove the need for a separate interaction term, by absorbing this component into the contributions of the within-and between-group factors. While the results may be obtained straightforwardly via a suitable computer algorithm, they do not produce simple analytical formulae. To gain some idea of the outcome, consider the 2-factor decomposition based on the within-group primary factor, K, and the between group primary factor, L. The elimination sequence (K, L) yields the marginal contributions

## C K = W + R; C L = B,

(5.16) so in this case the whole interaction effect is allocated to the within-group factor. However, the situation becomes more complex when the between group factor is removed in the first round, since setting each b k = 1 not only eliminates the betweengroup component B in Eq. 5.13, but also changes W and R to

## W =

m ν k 2 G w k k=1 and 2 r i − i w i k, 2 n μ i∈N m

## R =

k=1 (5.17) k respectively, where is the position of person i when the vector w 1, w 2, ..., w m is rearranged in increasing order. The elimination path (L, K) therefore produces the marginal contributions r i C L = G − W − R; C K = W + R, (5.18) and the Shapley decomposition is given by 1 1

## C K + C K =

## W + W + R + R

2 2 1 1

## C L S =

## C L + C L = B +

## W − W + R − R.

2 2

## S

=

## C K

(5.19) This assignment retains the basic features of the Shapley decomposition: the contributions sum to the overall Gini value, and they correspond to the marginal effect of removing each factor, averaged over all the elimination sequences. However there seems little prospect of gaining insights from further inspection of the formulae. One glimmer of hope is provided by the fact that the contributions in Eq. 5.19 may be rewritten as 1

## S

## G − C K − C L

## C K

## = C K +

2 1 (5.20)

## G − C K − C L

## C L S = C L +

2 So the contributions effectively begin with the first round marginal effects C K and C L, and then allocate half the “surplus” to each of the factors. This is a general consequence of applying the Shapley decomposition to two factors. However the property does not generalise easily when the within-group effects are treated separately; and since the model is not separable with respect to the set of withingroup factors (unlike the Entropy case in Section 5.1), the individual within-group effects are not expected to sum to the combined within-group effect derived above.

6 Inequality decomposition by source of income The last of the conventional decomposition problems concerns the situation in which income is divided into components such as earnings, investment income, taxes and transfers, and we seek to identify the contribution of these income sources to overall income inequality. If y = (y 1, y 2, ..., y n) denotes the distribution of income for a population of size n, and y k is the distribution of income from source k ∈ K = {1, 2, ..., m}, the original model may be written (6.1)

I = I(y) = I y k, k∈K where I(·) is an inequality index. This leads naturally to the model structure K, F, where the factors represent “incomes from source k” and are indexed by K, and the function F(·) is defined by

## F(S) = I

y k, S ⊆ K, (6.2) k∈S with the understanding that F(∅) = 0. A slightly different formulation results if the factors are interpreted as “differences in incomes from source k”. Denoting mean income by μ, the mean income from source k by μ k, and the n-tuple of 1’s by e, the model structure now becomes K, F̃, where y k + μ k e, S ⊆ K.

(6.3)

## F̃(S) = I

k∈S k ∈S / The distinction between Eqs. 6.2 and 6.3 is subtle, but important. It is best appreciated by considering a component of income which is equally distributed— for instance, a poll tax or subsidy. Since there are no differences across individuals, the marginal impact of removing these differences is always zero. As a consequence, the Shapley decomposition based on Eq. 6.3 suggests that any equally distributed component of income makes no contribution to overall inequality. In contrast, in the model based on Eq. 6.2, eliminating a poll subsidy will typically increase income inequality, so here the Shapley decomposition yields a negative contribution,

Decomposition procedures for distributional analysis: a unified...

suggesting an equalising effect (see Proposition 5 below). This probably accords better with intuition, although, as already indicated, the distinction really turns on whether one is interested in the contribution of a particular source of income, or in the contribution of variations in incomes from that source. Before the results of the Shapley decomposition are discussed, it is worth reviewing the methods currently used to decompose income inequality by source. If the variance is employed as the inequality index, Eq. 6.1 becomes σ 2 (y) = σ 2 k∈K y k = k∈K cov y k, y.

(6.4)

This suggests the factor contributions:

C k = cov x k, x, k ∈ K, (6.5) an assignment rule which Shorrocks [24] calls “the natural decomposition of the variance”. Similarly, using Eq. 5.12, the Gini index may be written 2 2 2 r i (y i − μ) = cov(r, y) = cov r, y k, 2 n μ i=1 nμ nμ n

G(y) = (6.6) k∈K suggesting the “natural decomposition of the Gini” given by

C k = 2 cov r, y k, nμ k ∈ K.

(6.7) Shorrocks [24] shows that many other decomposition rules can be constructed, but narrows down the options using a set of axioms. In combination these yield a unique decomposition rule in which the relative contribution of each income component is given by the natural decomposition of the variance, regardless of the choice of inequality index. For our purposes, the feature of most interest is the fact that both Eqs. 6.5 and 6.7—and more generally any allocation based on “natural decompositions”—assign a zero contribution to any component of income which is equally distributed. In general terms, this means that current methods conform more with the model based on Eq. 6.3, which looks for the contribution of income differences, rather than the model based on Eq. 6.2, which seeks the contributions of income levels. The Shapley decomposition is able to handle both interpretations, and therefore provides a richer range of possibilities. The results for the variance are the most easy to derive. In this particular case, formulations (6.2) and (6.3) coincide and yield

F(S) = F̃(S) = σ 2 k∈S y k,

## S ⊆ K,

(6.8) so y t − σ 2 y t k F(S) = σ 2 y k + t∈S t∈S y t + σ 2 y k, S ⊆ K\{k}.

= 2cov y k, t∈S (6.9)

Using Eq. 3.4, it then follows that 1 C k S (K, F) = C k S (K, F̃) = E S⊆K\{k} [k F(S) + k F(K\S\{k})] 2 y t + σ 2 y k = E S⊆K\{k} cov y k, t∈K\{k} = cov y k, y − y k + σ 2 y k = cov y k, y, k ∈ K.

(6.10) Thus, when the variance is used to measure inequality, the Shapley decomposition of inequality by source generates the usual “natural” decomposition values given in Eq. 6.5, regardless of whether the contributions are interpreted along the lines of Eq. 6.2 or Eq. 6.3. Similar conclusions do not hold for any other index, although the result is partially true when the square of the coefficient of variation is selected as the inequality index. In this case, interpretation (6.3) yields

F̃(S) = σ 2 y k /μ 2, S ⊆ K, (6.11) k∈S and repeating the above steps establishes that C k S (K, F̃) = cov y k, y /μ 2, k ∈ K.

(6.12) So the relative contribution of each factor again conforms with the natural decomposition of the variance when the factors are viewed as income differences from the various sources. Under the alternative scenario (6.2) based on income levels, the Shapley decomposition does not appear to produce informative formulae for indices other than the variance. It is possible, however, to draw one useful conclusion regarding the contribution of a source of income which is distributed equally across the population. Assume that μ k > 0 for all k ∈ K, and that the index I(·) is scale invariant and strictly Schur-convex. Then, since equal income increments are equalising, we have

## I

y t + αe < I y t, for all α > 0, and all S ⊆ K.

(6.13) t∈S t∈S So if y = μ e we can deduce that k k k F(S) < 0, for all S ⊆ K\{k}, (6.14) from which it follows that C k S (K, F) < 0. Thus Proposition 5 Consider the decomposition of income inequality where the factors represent incomes from various sources. Suppose that the mean income from each source is positive, and that the inequality index is scale invariant and strictly Schurconvex. Then the Shapley decomposition will assign a negative inequality contribution to any component of income which is distributed equally across the population.

7 Concluding remarks The main objective of this paper was to describe a general method of assessing the contributions of a set of factors which together account for the observed value of

Decomposition procedures for distributional analysis: a unified...

some aggregate statistic. The proposed solution involves calculating the marginal impact of each of the factors as they are eliminated in succession, and then averaging these marginal effects over all the possible elimination sequences. The resulting formula is formally identical to the Shapley value in cooperative game theory, and has therefore been referred to as the Shapley decomposition. The Shapley procedure has several basic features which make it an attractive candidate for a general decomposition rule. It treats the factors in a symmetric manner; the contributions sum to the amount which needs to be “explained”; and the contributions can be interpreted as the expected marginal effects. This paper has demonstrated that it also generates sensible results when applied to the standard decomposition problems encountered in distributional analysis. In three classic situations, the Shapley rule exactly replicates current practice: the application of decomposable poverty indices to population subgroups; inequality decomposition by subgroups using the mean logarithmic deviation index; and inequality decomposition by source of income using the variance as the measure of inequality. In other applications, such as the growth-redistribution issue discussed in Section 3.1, and the Gini decomposition considered in Section 5.2, it improves upon existing methods by avoiding the need to introduce a residual component into the decomposition equation. The paper has also shown how the Shapley procedure can provide solutions to problems which have previously been difficult to address, such as multi-variate poverty decomposition discussed in Section 4. Most of these applications are concerned with specific situations where previous work has suggested simple expressions for the factor contributions, and where the Shapley decomposition also yields explicit formulae, enabling the results to be compared. But the great advantage of the procedure proposed in this paper is that it can be applied to a wide range of problems which cannot be solved with existing techniques. Applications using other aggregate indicators or more complex models are unlikely to yield simple analytic expressions for the Shapley contributions, and will therefore require an algorithm to calculate the values (and, ideally, also their standard errors). In many situations, there will be sets of factors which group naturally together, suggesting a hierarchical model of the type described in Section 4, and the replacement of the Shapley rule by the two-stage Owen procedure. While it is difficult to predict the properties of the factor contributions in these general circumstances, the results of Section 4 and elsewhere will help researchers understand why certain features are observed in practice. For example, Propositions 1 and 2 will help explain why groups of factors can be treated as a single entity without affecting their total contribution, and Proposition 5 tells us to expect that a negative inequality contribution will be attached to any income component which is distributed roughly evenly across the population. Many other topics are obvious candidates for application of the Shapley decomposition procedure. These include the division of income mobility into structural and exchange components; a breakdown of the distributional impact taxes and benefits; the decomposition of wage inequality along the lines proposed by Juhn et al. [13], and the measurement of discrimination due to Oaxaca [17]. In the longer run, however, the applications with the greatest potential are the standard econometric formulations of applied economics, which all conform to the general specification (1.1) indicated at the outset. Fields [7] recognises the link between conventional OLS regressions and the problem of decomposing income inequality by source. The results of this paper suggest that the link can be extended to any econometric specification used in applied economics, in order to supplement the standard measures of statistical significance with an assessment of the relative importance of the explanatory variables.

## Appendix

To demonstrate Propositions 1 and 2, we first define α(r, n) = n!

, r!(n − r)!

n ≥ r, (8.1) and recall that π(r, n) = r!(n − r)!

1 = , (n + 1)!

(n + 1)α(r, n) n ≥ r.

(8.2) Identifying the coefficient of x r in the expansion of (1 − x) −s−1 (1 − x) −(n−s)−1 reveals that r t=0 α(t, r)π(s + t, n + r) = p r!(s + t)!(n + r − s − t)!

t=0 t!(r − t)!(n + r + 1)!

s!(n − s)!

= π(s, n) (n + 1)!

r+1 = α(t − 1, r)π(s + t − 1, n + r) = t=1 (8.3) for all n ≥ s ≥ 0 and all r ≥ 0. The proofs of Propositions 1 and 2 are now established via the following two Lemmas Lemma 1 Consider the model K, F, and suppose F is separable over L ⊆ K. Then, for all S ⊆ K\L and all n ≥ s ≥ 0, we have π(s + |T |, n + |L|)F(S ∪ T) = π(s + |T |, n + |L|)F(S ∪ K T) (8.4)

## T⊆L

## T⊆{L}

Proof Let p = |L| and t = |T |. Given that F is separable over L, condition (4.11) yields k F(S) T⊆L F(S ∪ T) = α(t, p)F(S) +

## T⊆L

|T |=t |T |=t k∈T t k F(S) k∈L p t p − t

## F(S) + F(S ∪ L)

= α(t, p) p p = α(t, p)F(S) + α(t, p) (8.5)

Decomposition procedures for distributional analysis: a unified...

Hence, using Eq. 8.3, π(s + |T |, n + |L|)F(S ∪ T) = p π(s + t, n + p) t=0 = p−1

## F(S ∪ T)

## T⊆L

|T |=t α(t, p − 1)π(s + t, n + p)F(S) t=0 + p α(t − 1, p − 1)π(s + t, n + p)F(S ∪ L) t=1 = π(s, n + 1)F(S) + π(s + 1, n + 1)F(S ∪ L) π(s + |T |, n + |L|)F(S ∪ K T) =

## T⊆{L}

This completes the proof of Lemma 1. Lemma 2 Given the hierarchical model K, A, F, consider any B ⊆ A such that F is separable over each L ∈ B. Then, for all S ⊆ K\K B and all n ≥ s ≥ 0, we have π(s + |T |, n + |K B |)F(S ∪ T)

## T⊆K B

= π(s + |T |, n + |B|)F(S ∪ K T) (8.6)

## T⊆B

Proof Let B = {L 1, L 2, ..., L r }. Then repeated application of Lemma 1 yields π (s + |T |, n + |K B |) F(S ∪ T)

## T⊆K B

= ...

## T 1 ⊆L 1 T 2 ⊆L 2

= ...

## T 1 ⊆{L 1} T 2 ⊆{L 2}

= ⎛ π ⎝ s +

T r ⊆L r

## T 1 ⊆{L 1} T 2 ⊆L 2

= |T j |, n + j=1 ⎛ π ⎝ s +

T r ⊆L r ...

r

T r ⊆{L r} |L j | ⎠ F ∪ rj=1 T j ∪ S |T j |, n + 1 + j=1 π ⎝ s + ⎞ j=1 r ⎛ r r r ⎞ |L j | ⎠ F ∪ rj=2 T j ∪ K T 1 ∪ S j=2 ⎞ |T j |, n + r ⎠ F ∪ rj=1 K T j ∪ S j=1 π(s + |T|, n + |B|)F(S ∪ K T) (8.7)

## T⊆B

This completes the proof of Lemma 2.

We now proceed to demonstrate Propositions 1 and 2.

Proof of Proposition 1 Let N = K\L, m = |K|, and n = |N|. Then, using Lemma 1, we have

C k S (K, F) = π(|S ∪ T |, m − 1) k F(S ∪ T)

S⊆N\{k} T⊆L = π(|S ∪ T |, n) k F (S ∪ K T) S⊆N\{k} T⊆{L} = E S⊆{L}∪N\{k} k F {L} (S) = C k S {L} ∪ N, F {L} (8.8) for all k ∈ N, as required in Eq. 4.12. In addition, since the Shapley decomposition is exact, it follows that S ({L} ∪ N, F {L}) = F {L} ({L} ∪ N) − C {L}

## = F(K) −

C k S {L} ∪ N, F {L} k∈N

C k S (K, k∈N

## F) =

C k S (K, F) (8.9) k∈L as required for Eq. 4.12b. Finally, for all k ∈ L and all s such that n ≥ t ≥ 0, separability over L implies π(|S| + t, m − 1) k F(S ∪ T)

S⊆L\{k} = = m−n−1

S⊆L\{k} |S|=s s=0 m−n−1 s=0 π(s + t, m − 1) k F(T) α(s, m − n − 1)π(s + t, m − 1) k F(T) = π(t, n) k F(T), (8.10) using Eq. 8.3. Hence

C k S (K, F) = π(|S ∪ T |, m − 1) k F(S ∪ T)

T⊆N S⊆L\{k} = π(|T |, n) k F(T) = E T⊆N k F(T)

## T⊆N

= C k S (N ∪ {k}, F), as required for Eq. 4.12c, and the proof of Proposition 1 is complete.

(8.11) Decomposition procedures for distributional analysis: a unified... Proof of Proposition 2 Consider any L ∈ A and any k ∈ L, and let m = |K| and n = |K\L |. Then, Eq. 8.9 and Lemma 2 yield the Shapley contributions

C k S (K, F) = π(|S ∪ T |, m − 1) k F(S ∪ T)

T⊆K A\{L} S⊆L\{k} = π(|T |, n) k F(T) =

## T⊆K A\{L}

π(|T |, |A| − 1) k F(K T)

## T⊆A\{L}

= E T⊆A\{L} k F(K T) = k F̄ L (∅).

(8.12) Since F is separable over L, it follows from Eq. 4.8 that C k O (K, A, F) = E T⊆A\{L} E S⊆L\{k} k F(K T ∪ S) = E T⊆A\{L} E S⊆L\{k} k F(K T) = E T⊆A\{L} k F(K T ).

So the proof of Proposition 2 is complete.

(8.13)

## References

1. Bouillon, C., Legovini, A., Lustig, N.: Rising inequality in Mexico: returns to household characteristics and the ‘Chiappas effect’. Paper presented at the LACEA Conference, Buenos Aires (1998) 2. Bourguignon, F.: Decomposable income inequality measures. Econometrica 47, 901–920 (1979) 3. Bourguignon, F., Fournier, M., Gurgand, M.: Distribution, development and education: Taiwan, 1979–1994. Paper presented at the LACEA Conference, Buenos Aires (1998) 4. Chantreuil, F., Trannoy, A.: Inequality decomposition values. Mimeo, Université de Cergy-

Pointoise (1997) 5. Cowell, F.A., Jenkins, S.P.: How much inequality can we explain—a methodology and an application to the United-States. Econ. J. 105, 421–430 (1995) 6. Datt, G., Ravallion, M.: Growth and redistribution components of changes in poverty measures—a decomposition with applications to Brazil and India in the 1980s. J. Dev. Econ.

38, 275–296 (1992) 7. Fields, G.S.: Accounting for differences in income inequality. Mimeo, Cornell University (1995) 8. Foster, J.E., Shneyerov, A.A.: Path independent inequality measures. Discussion Paper No. 97-W04, Department of Economics, Vanderbilt University (1996) 9. Foster, J.E., Shneyerov, A.A.: A general class of additively decomposable inequality indices.

Discussion Paper No. 97-W10, Department of Economics, Vanderbilt University (1997) 10. Foster, J.E., Greer, J., Thorbecke, E.: A class of decomposable poverty indices. Econometrica 52, 761–765 (1984) 11. Grootaert, C.: Structural change and poverty in Africa: a decomposition analysis for Cote d’Ivoire. J. Dev. Econ. 47, 375–402 (1995) 12. Jenkins, S.P.: Accounting for inequality trends: decomposition analyses for the UK, 1971–86.

Economica 62, 29–64 (1995) 13. Juhn, C., Murphy, K.M., Pierce, B.: Wage inequality and the rise in returns to skill. J. Polit. Econ.

101, 410–442 (1993) 14. Lambert, P.J., Aronson, J.R.: Inequality decomposition analysis and the Gini coefficient revisited. Econ. J. 103, 1221–1227 (1993) 15. Morduch, J., Sinclair, T.: Rethinking inequality decomposition, with evidence from rural China.

Mimeo, Stanford University (1998) 16. Moulin, H.: Axioms of Cooperative Decision Making. Cambridge University Press (1988) 17. Oaxaca, R.: Male-female wage differentials in urban labour markets. Int. Econ. Rev. 14, 693–709 (1973) 18. Owen, G.: Values of games with priori unions. In: Heim, R., Moeschlin, O. (eds.) Essays in Mathematical Economics and Game Theory. Springer, New York (1977) 19. Pyatt, G.: On the interpretation and disaggregation of Gini coefficients. Econ. J. 86, 243–255 (1976) 20. Ravallion, M., Huppi, M.: Measuring changes in poverty: a methodological case study of Indonesia during an adjustment period. World Bank Econ. Rev. 5, 57–84 (1991) 21. Rongve, I.: A Shapley decomposition of inequality indices by income source. Discussion Paper #59, Department of Economics, University of Regina (1995) 22. Shapley, L.: A value for n-person games. In: Kuhn, H.W., Tucker, A.W. (eds.) Contributions to the Theory of Games, vol. 2. Princeton University Press (1953) 23. Shorrocks, A.F.: The class of additively decomposable inequality measures. Econometrica 48, 613–625 (1980) 24. Shorrocks, A.F.: Inequality decomposition by factor components. Econometrica 50, 193–211 (1982) 25. Shorrocks, A.F.: Inequality decomposition by population subgroups. Econometrica 52, 1369– 1385 (1984) 26. Szekely, M.: Poverty in Mexico during adjustment. Rev. Income Wealth 1995(3), 331–348 (1995) 27. Theil, H.: Statistical Decomposition Analysis. North Holland, Amsterdam (1972) 28. Thorbecke, E., Jung, H.S.: A multiplier decomposition method to analyze poverty alleviation. J. Dev. Econ. 48, 279–300 (1996) 29. Tsui, K.-Y.: Growth-equity decomposition of a change in poverty: an axiomatic approach. Econ. Lett. 50, 417–424 (1996) 30. Young, H.P.: Monotonic solutions of cooperative games. Int. J. Game Theory 14, 65–72 (1985) Reproduced with permission of the copyright owner. Further reproduction prohibited without permission.
