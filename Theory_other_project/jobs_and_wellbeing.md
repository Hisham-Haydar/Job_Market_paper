%2multibyte Version: 5.50.0.2960 CodePage: 1252

<!--
%\newtheorem{theorem}{Theorem}
%\newtheorem{proposition}{Proposition}
%\newtheorem{lemma}{Lemma}
%\input{tcilatex}
-->

# Jobs and Well-Being Measurement

**Hisham Haydar**  
Department of Economics, University of Luxembourg, and LISER. Email: hisham.haydar@liser.lu

**François Maniquet**  
LIDAM/CORE, Université catholique de Louvain, and LISER. Email: francois.maniquet@uclouvain.be.

**Date:** February 2025

## Abstract

We measure well-being in a model in which individuals take one job in their ability set and have heterogenous preferences over jobs and how much they are paid.

JEL Classification: H21, D63.

Keywords: jobs, well-being.

## Introduction

## The model

- Fixed universal set of existing jobs: $\mathcal{J}$.
- Pre-tax income function: $\mathbf{y}:\mathcal{J}\rightarrow \mathbb{R}_{+}$: $\mathbf{y}(j)$, also written $\mathbf{y}_j$, stands for pre-tax income associated to job $j$.
- Consumption set: $Z=\mathbb{R}_{+}\times \mathcal{J}$, typical element $z=(c,j)$, where $c$ is the consumption level and $j$ the job to which the individual is assigned.
- Preferences: $R\in\mathcal{R}$, monotonic in the first argument.
- Ability set $A\subseteq \mathcal{J}$. The set of ability sets is refer to as $\mathcal{A}$. It can be the entire set of possible subsets of $\mathcal{J}$: $\mathcal{J}:2^{\mathcal{J}}$. We can add restrictions as well, and we introduce these restrictions below when we use them.
- Well-being measure: $W: Z\times \mathcal{R} \times 2^{\mathcal{J}}\rightarrow \mathbb{R}$: $W(z,R,A)$ is the well-being level of an individual consuming bundle $z$, having preferences $R$ and ability set $A$.
- Well-being is allowed to depend on how much jobs are paid $\mathbf{y}$, so we write $W(z,R,A;\mathbf{y})$.
- To save on notation, we assume that as soon as we measure $W(z,R,A;\mathbf{y})$, $z=(c,j)$ for some $j\in A$.

Remarks on the model:

- By allowing $\mathbf{y}$ to vary, we distinguish between non-pecuniary characteristics of jobs, assumed to be fixed, and pecuniary characteristics, which may vary (across regions or through time). Of course, with a sufficiently large $\mathcal{J}$ we can represent the universe of jobs by fixing $\mathbf{y}$, so that several jobs with exactly the same tasks to perform can be distinguished depending on how much they are paid. We prefer the latter definition, though, to be allowed to make pre-tax income vary without affecting the preferences of individuals towards a particular job.

## Axioms

Basic axioms. First, $W$ is a utility representation.

**Representation:** For all $z,z'\in Z$, $R\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y}\in \mathbb{R}_{+}^{\mathcal{J}}$,

$$
z\,R\,z'\Leftrightarrow W(z,R,A;\mathbf{y})\geq W(z',R,A;\mathbf{y}).
$$

Two axioms that deal with the question: what is a job? First, Job Multiplication captures the idea that there is no difference between being able to occupy two jobs that are completely identical, both in terms of pay and preferences, or being able to occupy only one of these jobs.

**Job Duplication Invariance:** For all $z=(c,j)\in Z$, $R\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y}\in \mathbb{R}_{+}^{\mathcal{J}}$, $j'\in \mathcal{J}\setminus A$, if $\mathbf{y}(j')=\mathbf{y}(j)$ and $(x,j)\,I\,(x,j')$ for all $x\in\mathbb{R}_{+}$, then

$$
W(z,R,A;\mathbf{y})=W(z,R,A\cup\{j'\};\mathbf{y}).
$$

To define the second axiom, we need the following terminology. Let $\pi:\mathcal{J}\rightarrow \mathcal{J}$ denote a permutation on $\mathcal{J}$. We let $\Pi$ denote the set of all permutations on $\mathcal{J}$. We let $\pi(A)\in 2^{\mathcal{J}}$ denote the permutation of elements of $A$ in $\mathcal{J}$, that is $j\in\pi(A)$ if and only if there exists $j'\in A$ such that $j=\pi(j')$. For $z=(j,c)$, we define $\pi(z)=(\pi(j),c)$. We also define $\pi(\mathbf{y})$ as follows: $\pi(\mathbf{y})(j)=\mathbf{y}(\pi(j))$. Finally, we define $\pi(R)\in\mathcal{R}$ as follows: $z/,R\,z'$ if and only if $\pi(z)\,\pi(R)\,\pi(z')$.

**Job Neutrality:** For all $z\in Z$, $R\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y}\in \mathbb{R}_{+}^{\mathcal{J}}$, $\pi\in\Pi$,

$$
W(z,R,A;\mathbf{y})=W(\pi(z),\pi(R),\pi(A);\pi(\mathbf{y})).
$$

I guess we will need axioms of Continuity.

We begin with compensation axioms.

**Full Compensation:** For all $z,z'\in Z$, $R\in \mathcal{R}$, $A,A'\subseteq \mathcal{J}$, $\mathbf{y}, \mathbf{y}' \in \mathbb{R}_{+}^{\mathcal{J}}$,

$$
z\,I\,z'\Rightarrow W(z,R,A;\mathbf{y})=W(z',R,A';\mathbf{y}').
$$

We can decompose Full Compensation into these two, weaker, axioms.

**Independence of $\mathbf{y}$:** For all $z\in Z$, $R\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y}, \mathbf{y}' \in \mathbb{R}_{+}^{\mathcal{J}}$,

$$
W(z,R,A;\mathbf{y})=W(z,R,A;\mathbf{y}').
$$

> **Note in original**
>
> Shouldn't be written:
>
> **Independence of $\mathbf{y}$:** For all $z,z'\in Z$, $R\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y}, \mathbf{y}' \in \mathbb{R}_{+}^{\mathcal{J}}$,
>
> $$
> z\,I\,z'\Rightarrow W(z,R,A;\mathbf{y})=W(z',R,A;\mathbf{y'}).
> $$

**Independence of $A$:** For all $z,z'\in Z$, $R\in \mathcal{R}$, $A,A'\subseteq \mathcal{J}$, $\mathbf{y}\in \mathbb{R}_{+}^{\mathcal{J}}$,

$$
z\,I\,z'\Rightarrow W(z,R,A;\mathbf{y})=W(z',R,A';\mathbf{y}).
$$

These two properties are different in nature. Independence of $\mathbf{y}$ implies that individuals are not responsible for how much the jobs they are able to take pay. This leaves the possibility to hold individuals responsible for the set of jobs they are able to take. Independence of $A$ implies that individuals are not responsible for the set of jobs they are able to take but well-being may be measured by reference to pre-tax incomes. This leaves the possibility to make well-being differ among individuals on the basis that one of them happens to like jobs that are more productive.

It is easy to see that a well-being measure $W$ satisfies Full Compensation if and only if it satisfies Independence of $\mathbf{y}$ and Independence of $A$. We should study them separately, but we should also check which well-being measures satisfies Full Compensation.

**Compensation for Reference Preferences.** There exists $\tilde{\mathcal{R}}\subseteq\mathcal{R}$ such that or all $z,z'\in Z$, $R\in \tilde{\mathcal{R}}$, $A,A'\subseteq \mathcal{J}$, $\mathbf{y}, \mathbf{y}' \in \mathbb{R}_{+}^{\mathcal{J}}$,

$$
z\,I\,z'\Rightarrow W(z,R,A;\mathbf{y})=W(z',R,A';\mathbf{y}').
$$

Job $j$ is irrelevant for an individual of type $(R,A)$ at pre-tax incomes $\mathbf{y}(j)$ if $j\in A$ but this individual will never take job $j$: there is another job, $j'$, which this individual can take, which pays less, and independently of the tax (by tax progressivity the tax on $j$ cannot be lower than that on $j'$) this individual always prefers taking job $j'$: $j$ is irrelevant for individual $(R,A)$, if $j\in A$ and there exists $j'\in A$ such that $\mathbf{y}(j')<\mathbf{y}(j)$ and for all $t\in\mathbb{R}$, $z,z'\in Z$ such that $z=(\mathbf{y}(j)-t,j)$ and $z'=(\mathbf{y}(j')-t,j')$: $z'\,P\,z$. For $(R,A)$ we let $Irr(A;R,\mathbf{y})$ denote the set of irrelevant jobs for an individual of type $(R,A)$ facing pre-tax incomes $\mathbf{y}$.

**Independence of Irrelevant Jobs:** For all $z=(c,j)\in Z$, $R\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $j'\in A$, $\mathbf{y} \in \mathbb{R}_{+}^{\mathcal{J}}$, if $j\neq j'$ and $j'\in Irr(A;R,\mathbf{y})$, then

$$
W(z,R,A;\mathbf{y})=W(z,R,A\setminus\{j'\};\mathbf{y})
$$

Full Compensation implies Independence of $\mathbf{y}$, Compensation for Reference Preferences and Independence of Irrelevant Jobs.

A job $j$ is infeasible for an individual of type $(R,A)$ if this individual is not able to take it, that is, if $j\notin A$. Since bundles are of the form $z=(c,j)$, if $j\notin A$, then no bundle containing job $j$ can be chosen by this individual. Therefore, preferences over such infeasible jobs should not affect the well-being level assigned to feasible bundles. In other words, only the restriction of preferences to feasible bundles should matter for well-being measurement.

**Independence of Preferences over Infeasible Jobs (IPIJ):**  
For all $R,R'\in\mathcal R$, all $A\subseteq \mathcal J$, all $\mathbf y\in\mathbb R_+^{\mathcal J}$, if for all $z,z'\in Z$,

$$
z\,R\,z' \ \Longleftrightarrow\ z\,R'\,z',
$$

then for all $z\in Z$,

$$
W(z,R,A;\mathbf y)=W(z,R',A;\mathbf y).
$$

Full Compensation does not imply Independence of Preferences over Infeasible Jobs, since the former compares indifferent bundles under a fixed preference relation, whereas the latter requires invariance of the well-being measure to changes in preferences outside the feasible set

Next, responsibility axioms. We use the following terminology: $\max_{R}\{A;\mathbf{y}\}$ stands for any of the preferred bundles among those composed of jobs in $A$ and their pre-tax income in $\mathbf{y}$, absent any taxation. Note that if there are several bundles that maximize $R$ in $A$, they are indifferent to each other.

We now turn to the responsibility axioms. To define them, we need the following terminology. For $R\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y} \in \mathbb{R}_{+}^{\mathcal{J}}$, we let $\argmax_{(A,\mathbf{y})}R$ denote one of the bundles that maximizes preferences $R$ in the set of bundles defined by the pair $(A,\mathbf{y})$. Note that if there are several best bundles in $(A,\mathbf{y})$, the

**Full Responsibility:** For all $R,R'\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y} \in \mathbb{R}_{+}^{\mathcal{J}}$,

$$
W(\argmax_{(A,\mathbf{y})}R,R,A;\mathbf{y})=W(\argmax_{(A,\mathbf{y})}R',R',A;\mathbf{y}).
$$

**Responsibility For Equal Pay:** For all $R,R'\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y} \in \mathbb{R}_{+}^{\mathcal{J}}$ such that $\mathbf{y}(j)=\mathbf{y}(j')$ for all $j,j'\in A$,

$$
W(\argmax_{(A,\mathbf{y})}R,R,A;\mathbf{y})=W(\argmax_{(A,\mathbf{y})}R',R',A;\mathbf{y}).
$$

**Responsibility When the Preferred Job is Possible:** we apply Responsibility only if at least one of the jobs that individuals prefer over all existing jobs is in the ability set.

**Responsibility When the Preferred Job is Possible:** For all $R,R'\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y} \in \mathbb{R}_{+}^{\mathcal{J}}$, if $\argmax_{(\mathcal{J},\mathbf{y})}R\in A$ and $\argmax_{(\mathcal{J},\mathbf{y})}R'\in A$ then

$$
W(\argmax_{(A,\mathbf{y})}R,R,A;\mathbf{y})=W(\argmax_{(A,\mathbf{y})}R',R',A;\mathbf{y}).
$$

> **Note in original**
>
> does it make a difference if it was $A'$?
>
> $$
> W(\argmax_{(A,\mathbf{y})}R,R,A;\mathbf{y})=W(\argmax_{(A,\mathbf{y})}R',R',A';\mathbf{y}).
> $$

We can combine the restrictions to Responsibility contained in the latter two axioms and obtain the following axiom.

**Weak Responsibility:** For all $R,R'\in \mathcal{R}$, $A\subseteq \mathcal{J}$, $\mathbf{y} \in \mathbb{R}_{+}^{\mathcal{J}}$ such that $\mathbf{y}(j)=\mathbf{y}(j')$ for all $j,j'\in A$, if $\argmax_{(\mathcal{J},\mathbf{y})}R\in A$ and $\argmax_{(\mathcal{J},\mathbf{y})}R'\in A$ then

$$
W(\argmax_{(A,\mathbf{y})}R,R,A;\mathbf{y})=W(\argmax_{(A,\mathbf{y})}R',R',A;\mathbf{y}).
$$

### Responsibility for acquired ability (RAA)

We model ability sets as partly the outcome of past choices and partly due to circumstances, we introduce a reduced-form *ability-formation correspondence*. Let $\Theta$ denote the set of circumstances (non-responsibility factors such as health shocks, family background constraints, and labour-market frictions), and let $E$ denote the set of merit/investment levels (education, training, and job experience). The observed ability set is generated by a correspondence

$$
A:\Theta\times E \to 2^{\mathcal J},\qquad (\theta,e)\mapsto A(\theta,e)\subseteq \mathcal J.
$$

We impose the following responsibility requirement: for any preferences $R\in\mathcal R$, any income function $\mathbf y\in\mathbb R_+^{\mathcal J}$, any circumstances $\theta\in\Theta$, and any two feasible merit levels $e,e'\in E(\theta)$,

$$
W\!\big(\max_{R}\{A(\theta,e);\mathbf y\},\,R,\,A(\theta,e);\,\mathbf y\big)
=
W\!\big(\max_{R}\{A(\theta,e');\mathbf y\},\,R,\,A(\theta,e');\,\mathbf y\big),
$$

that is, conditional on the same circumstances $\theta$, differences in the achieved ability set that arise from different feasible merit choices should not affect the well-being level assigned at the laissez-faire.

## Measures

**Measure 1:** We restrict our attention to the individual's ability set, without looking at the pre-tax incomes associated to these jobs, and we look at the preferred job and its corresponding consumption level that leaves the individual indifferent to their current bundle.

$$
W(z, R, A;\mathbf{y})=w\Leftrightarrow z\,I\,\max_R\{B\}
$$

where

$$
z'=(c',j')\in B\Leftrightarrow j'\in A \textrm{ and } c'=w.
$$

If I'm right, this measure satisfies Independence of $\mathbf{y}$ and Responsibility For Equal Pay. I am confident it is the only measure to satisfy these two axioms. To be proven.

**Measure 2:** We restrict our attention to the individual's ability set, we look at the preferred job in this set to which the individual is indifferent to their current bundle, where “preferred job” means that the tax (or subsidy) that would leave them indifferent is minimal, and we apply this tax (or subsidy) to all the jobs in the ability set to identify the "best-paid equivalent" job, the pay of which is the well-being of the individual.

$$
W(z, R, A;\mathbf{y})=w\Leftrightarrow z\,I\,\max_R\{B\}
$$

where there exists $t\in\mathbb{R}$ such that

$$
z'=(c',j')\in B\Leftrightarrow j'\in A \textrm{ and } c'=\mathbf{y(j')}-t,
$$

and

$$
w=\max_{j\in A}\mathbf{y}(j)-t.
$$

In particular, if $z=\argmax_A R$, then $W(z, R, A;\mathbf{y})=\max_{j\in A}\mathbf{y}(j)$.

If I'm right, this measure satisfies Full Responsibility and Compensation for Reference Preferences if the reference preferenes are $R^{c}\in\mathcal{R}$ defined by

$$
z=(c;j)\,R^{c}\,z'=(c',j')\Leftrightarrow c\geq c'.
$$

I am reasonably confident it is the only measure to satisfy these two axioms and some other ones that will extend Job Neutrality. To be proven.

**Measure 3:** The Laisser-Faire measure. All individuals have the same well-being at laisser-faire. Otherwise, compute the amount of tax $t$ that leaves the individual indifferent between their current bundle and maximizing over their ability set and maying $t$ (better to write it as a subsidy I guess).

$$
W(z, R, A;\mathbf{y})=w\Leftrightarrow z\,I\,\max_R\{B\}
$$

where

$$
z'=(c',j')\in B\Leftrightarrow j'\in A \textrm{ and } c'=\mathbf{y}(j')+w.
$$

I think the Laisser-Faire measure satisfies Full Responsibility and Independence of Irrelevant Jobs and it is the only one that satisfies these two axioms

**Measure 4:** The Staying-Home Equivalent measure. Assume there is a “job”, say $o$, consisting of staying home, with $\mathbf{y}(o)=0$, such that everybody has it in their ability set: for all $A\in\mathcal{A}$, $o\in A$. Then, we can measure well-being by computing the consumption level that leaves an individual indifferent between their current bundle and staying home with that consumption level.

$$
W(z, R, A;\mathbf{y})=w\Leftrightarrow z\,I\,(w,o).
$$

**Measure 5:** The Reference Ability LF measure. We fix a reference ability set $\bar{A}\subseteq \mathcal{J}$. Instead of evaluating an individual relative to their own actual ability set, as in the Laisser-Faire measure, we evaluate them relative to a common reference set of jobs. The idea is to compute the amount of subsidy that, when added uniformly to all jobs in the reference ability set, makes the individual indifferent between their current bundle and the best job they would choose in that subsidized reference set. In this way, well-being is measured relative to a common benchmark of job opportunities.

$$
W(z,R,A;\mathbf{y})=w
\Leftrightarrow
z\,I\,\max_R\{B\}
$$

where

$$
z'=(c',j')\in B
\Leftrightarrow
j'\in \bar{A}
\textrm{ and }
c'=\mathbf{y}(j')+w.
$$

In particular, if $z=\argmax_{(\bar{A},\mathbf{y})}R$, then $W(z,R,A;\mathbf{y})=0$.  
This measure satisfies Independence of $A$, Independence of Irrelevant Jobs, and a responsibility principle relative to the reference ability set $\bar{A}$. It does not satisfy Independence of $\mathbf{y}$, and in general it does not satisfy Full Responsibility, since the latter is defined with respect to the actual ability set $A$ rather than the reference ability set $\bar{A}$. As a special case, if we take $\bar{A}=\mathcal{J}$, then the measure satisfies Responsibility When the Preferred Job is Possible, since whenever an individual's preferred job in $(\mathcal{J},\mathbf{y})$ belongs to the actual ability set $A$, the preferred feasible bundle in $(A,\mathbf{y})$ coincides with the preferred bundle in the reference set and therefore receives well-being level $0$.

\\

|  | $W^1$ | $W^2$ | $W^3$ | $W^4$ |
|---|---|---|---|---|
| Full Compensation | - | - | - | + |
| Ind. of $\mathbf{y}$ | + | - | - | + |
| Ind. of $A$ | - | - | - | + |
| Comp.\ for $R^{horizontal}$ | + | + | - | + |
| Comp.\ for $R^{lenient}$ | - | - |  | + |
| Comp.\ for Ref. Pref. | + | - | ? | + |
| Ind.\ of Irr.\ Jobs (IIJ) | + | - | + | + |
| Full Responsibility | - | + | + | - |
| Resp.\ For Equal Pay | + | + | + | - |
| Resp.\ When Pref. Job is Poss. | - | + | + | - |
| Weak Resp. | + | + | + | - |
| Ind.\ Pref.\ Infeas.\ Jobs (IPIJ) | + | + | + | + |
| Resp.\ ref.\ abilities | - | - | + | - |

## Results

### Theorem

If a well-being measure $W$ satisfies Responsibility for Equal Pay and Independence of $\mathbf{y}$, then $W=W^1$.

### Proof

We need to prove that for all $z,z'\in Z$, $R,R'\in\mathcal{R}$, $A,A'\in 2^{\mathcal{J}}$, $y,y'\in\mathbb{R}_{+}^{\mathcal{J}}$, if there exists $w\in\mathbb{R}_{+}$ such that

$$
z=\argmax_{A,\mathbf{y}^w}R
\tag{th\_1\_z}
$$

$$
z'=\argmax_{A',\mathbf{y}^w}R'
\tag{th\_1\_z'}
$$

then (*) $W(z,R,A;\mathbf{y})=W(z',R',A';\mathbf{y}')$.

Let $z,z'$ and $w$ satisfy (th\_1\_z) and (th\_1\_z'). By Independence of $\mathbf{y}$,

$$
(*)\Leftrightarrow W(z,R,A;\mathbf{y}^w)=W(z',R',A';\mathbf{y}^w).
$$

Let $\bar{z},\bar{z}'\in Z$ be defined by

$$
\bar{z}=(w,j)= \argmax_{A,\mathbf{y}^w}R,\quad j\in A
$$

$$
\bar{z}'=(w,j')= \argmax_{A',\mathbf{y}^w}R',\quad j'\in A.
$$

By Representation, $W(z,R,A;\mathbf{y}^w)=W(\bar{z},R,A;\mathbf{y}^w)$ and $W(z',R',A';\mathbf{y}^w)=W(\bar{z}',R',A';\mathbf{y}^w)$, so that

$$
W(z,R,A;\mathbf{y}^w)=W(z',R',A';\mathbf{y}^w) \Leftrightarrow W(\bar{z},R,A;\mathbf{y}^w)=W(\bar{z}',R',A';\mathbf{y}^w).
$$

By Responsibility for Equal Pay, $W(\bar{z},R,A;\mathbf{y}^w)=W(\bar{z},R^c,A;\mathbf{y}^w)$ and $W(\bar{z}',R',A';\mathbf{y}^w)=W(\bar{z}',R^c,A';\mathbf{y}^w)$, so that

$$
W(\bar{z},R,A;\mathbf{y}^w)=W(\bar{z}',R',A';\mathbf{y}^w) \Leftrightarrow W(\bar{z},R^c,A;\mathbf{y}^w)=W(\bar{z}',R^c,A';\mathbf{y}^w).
$$

Let $\bar{A}\subseteq\mathcal{J}$ be defined by $\bar{A}=A\cup A'$. By Job Duplication Invariance applied $\lvert \bar{A}\setminus A \rvert$ times, $W(\bar{z},R^c,A;\mathbf{y}^w)=W(\bar{z},R^c,\bar{A};\mathbf{y}^w)$. By Job Duplication Invariance applied $\lvert \bar{A}\setminus A' \rvert$ times, $W(\bar{z}',R^c,A';\mathbf{y}^w)=W(\bar{z}',R^c,\bar{A};\mathbf{y}^w)$ so that

$$
W(\bar{z},R^c,A;\mathbf{y}^w)=W(\bar{z}',R^c,A';\mathbf{y}^w) \Leftrightarrow W(\bar{z},R^c,\bar{A};\mathbf{y}^w)=W(\bar{z}',R^c,\bar{A};\mathbf{y}^w).
$$

By construction, $\bar{z}\,I^c\,\bar{z}'$, so that, by Representation,

$$
W(\bar{z},R^c,\bar{A};\mathbf{y}^w)=W(\bar{z}',R^c,\bar{A};\mathbf{y}^w)
$$

which completes the proof.

## Extension

In the model above, the norm of compensation means that individuals are not responsible for their ability set. One may object, however, that ability sets come both from some background that individuals do not control but also from their past efforts, especially during their education period or when they held previous jobs. That suggests defining variables $e\in E$ and $b\in B$, so that abilities are determined by these two variables: there is a function $A:E\times B\rightarrow \mathcal{A}$ such that $A(e,b)$ stands for the ability set of an individual having exerted effort $e$ with background $b$. Note that preferences now depend on bundle $z$ but also on past effort $e$. The model becomes: we look for a well-being function $W((z,e),R;\mathbf{y},b)$ where $z\in A(e,b)$.

---

%%%%% Newpage introduced so that quotation is not split across pages

## Introduction

$i,h\in N$, $j,k\in\mathcal{J}$ such that

- $j\in A_i$, $j\notin \mu(N)$ (that is nobody is assigned job $j$), $k\in A_h\setminus A_i$,
- $y_j=y_k$,
- $u(b_i(a))<u(y_j-(y_{\mu(i)}-C(i),\ell_j,x_j)$,
- $u(b_h(a))<u(y_k-(y_{\mu(i)}-C(i),\ell_k,x_k)$