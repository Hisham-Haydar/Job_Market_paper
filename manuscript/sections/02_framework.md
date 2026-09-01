# 2. Framework

*Drafting note, to be stripped at final.* Every design element below carries a
status tag: **[ACCEPTED]** — on the record of an accepted run or a ratified
ruling; **[PROVISIONAL]** — computed and internally verified, but carrying an
explicit provisional label on its own artifacts; **[PENDING]** — designed but
not yet ruled or not yet on disk; **[OPEN]** — expected by an earlier draft but
**not** owed by the source text, and deliberately left unwritten rather than
reconstructed. Every numeral is bound to a source (file and
section) in the self-check table at the end of the section. The section does not
reproduce the companion theory paper; it cites it and states only what the
empirical design needs.

---

## 2.1 The model

A household does not choose hours off a continuum. It takes or declines *job
packages* that the market puts in front of it, and a package is a triple
$(h, w, k)$ — weekly hours, an hourly wage, an occupation — together with the
disposable income the tax–benefit system delivers at that triple. The
specification therefore carries two distinct objects: a **utility function**,
which says how a household ranks packages it can have, and an **opportunity
density**, which says how available each package is. The likelihood is what
separates them, and reading any coefficient means knowing which of the two it
belongs to. **[ACCEPTED]**

**Utility.** Preferences are Box–Cox over consumption and leisure, with the
taste shifters carried in the leisure weight:

$$
u_{ij} \;=\; \beta_{\ell}^{g}(\mathbf{x}_i)\,
\mathcal{B}\!\left(\tilde{\ell}_{ij};\theta_{\ell}^{g}\right)
\;+\; \beta_{c}\,\mathcal{B}\!\left(\tilde{c}_{ij};\theta_{c}\right),
\qquad
\mathcal{B}(z;\theta)=\frac{z^{\theta}-1}{\theta},
$$

$$
\beta_{\ell}^{g}(\mathbf{x}_i)\;=\;\beta_{\ell 0}^{g}
+\beta_{\ell a}^{g}a_i+\beta_{\ell a^{2}}^{g}a_i^{2}
+\mathbb{1}\{g=\text{women}\}\,\beta_{\ell k}^{g}k_i ,
$$

with $\tilde{\ell}_{ij}=(\bar L-h_{ij})/\lambda_{\ell}$,
$\tilde{c}_{ij}=c_{ij}/\lambda_c$, $a_i$ age centred and scaled by ten, $k_i$ the
number of children, and $\beta_c\equiv 1$ as the scale numeraire. The
consumption curvature $\theta_c$ is shared by the two sexes by construction of
the certified specification; the leisure curvature $\theta_{\ell}^{g}$ is not.
The leisure normaliser of record is $\lambda_{\ell}=10$ hours. **[ACCEPTED]**

**The opportunity density.** Availability factorises into four margins, each
equal to one at its own reference, the last three switched off on the
non-employment package ($E_{ij}=\mathbb{1}\{h_{ij}>0\}$):

$$
g_{ij}\;=\;g^{E}_{ij}\cdot g^{H}_{ij}\cdot g^{\mathrm{Occ}}_{ij}\cdot g^{W}_{ij}.
$$

*The access margin* $g^{E}$ is a level shift on every working package, moved by
the local unemployment rate, the region of residence and urbanisation:

$$
\log g^{E}_{ij}=E_{ij}\Bigl[\beta_{E}+\beta_{s}\tilde{s}_i
+\textstyle\sum_{r=2}^{8}\beta_{r}\mathbb{1}\{R_i=r\}
+\beta_{u}U_i+\beta_{m}M_i\Bigr].
$$

*The hours-band factor* $g^{H}$ is a step density over five bands, the statutory
35-hour band being the reference with its coefficient normalised to zero:

$$
\log g^{H}_{ij}=\sum_{b}\beta_{b}\,\mathbb{1}\{h_{ij}\in B_b\},
\qquad \beta_{\mathrm{F35}}\equiv 0 .
$$

The preferred positive specification adds one coefficient on a 35-hour indicator
inside this factor. We label it an **institutionally motivated opportunity
peak**: it is a feature of the estimated offer density at the statutory week,
not an estimate of the causal effect of any statute. The restricted model at
that coefficient equal to zero reproduces the benchmark objective bitwise, so
the addition is a genuine one-degree-of-freedom restriction rather than a
reparameterisation. **[ACCEPTED]**

*The occupation weights* $g^{\mathrm{Occ}}$ place four occupation categories,
the first omitted, with a separate set of offer weights for men and for women:
$\log g^{\mathrm{Occ}}_{ij}=E_{ij}\sum_{k=2}^{4}\beta^{\mathrm{occ}}_{k,g}
\mathbb{1}\{o_{ij}=k\}$, $\beta^{\mathrm{occ}}_{1,g}\equiv 0$.

*The wage location* $g^{W}$ is an occupation-conditional log-normal offer
density — a Mincer equation carried **inside** the opportunity set, so that it
describes the wage a person could be offered rather than the wage the employed
are seen at:

$$
\log g^{W}_{ij}=E_{ij}\Bigl[-\tfrac12\Bigl(\tfrac{\log w_{ij}-\mu_i}{\sigma}\Bigr)^{2}
-\log\sigma-\tfrac12\log 2\pi-\log w_{ij}\Bigr],
\qquad
\mu_i=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i+\beta_{wx^{2}}x_i^{2},
$$

with the preferred specification adding occupation-specific location shifts
$\delta_{\mathrm{occ}}$. These are **location shifts of the offer distribution,
not causal occupational wage premia**, and no manuscript sentence may read them
as the latter. **[ACCEPTED]**

One convention is not visible in the algebra and is stated because it governs
how the regional and occupation coefficients are read: the estimator centres
those terms within each household's own choice set, weighting by the proposal
density,
$\tilde m_{ij}=m_{ij}-\sum_{j'}q_{ij'}m_{ij'}\big/\sum_{j'}q_{ij'}$, so they are
read against the household's own set rather than a global origin. **[ACCEPTED]**

**The opportunity set is an estimated density, not a menu.** Nothing in the data
records the jobs a household could have had. What the design delivers is
$g_{ij}$ — an availability weight over a continuous latent job space, estimated
jointly with tastes in one likelihood, which is what stops a taste parameter
from quietly absorbing an availability one. Every welfare and decomposition
object in §2.3–§2.4 is a functional of that estimated density, and inherits its
model-conditionality. **[ACCEPTED]**

---

## 2.2 Estimation on sampled alternatives

The choice set is not enumerable, so it is sampled. The estimator is a
conditional logit over sampled choice sets,

$$
\hat{\theta}=\arg\max_{\theta}\sum_{i=1}^{N}
\Bigl[V_{i\,j^{*}_i}(\theta)-\log\!\!\sum_{j\in\mathcal{C}_i}\!\exp V_{ij}(\theta)\Bigr],
$$

$$
V_{ij}(\theta)=\underbrace{u_{ij}(\theta)}_{\text{tastes}}
+\underbrace{\log g_{ij}(\theta)}_{\text{availability}}
-\underbrace{\log q_{ij}}_{\text{proposal correction}},
\qquad
q_{ij}=q^{E}_{ij}\bigl(q^{H}_{ij}q^{W}_{ij}q^{\mathrm{Occ}}_{ij}\bigr)^{E_{ij}} .
$$

Each household is given its observed package plus drawn alternatives; the
$-\log q_{ij}$ offset is McFadden's sampling-of-alternatives correction, which
makes the sampled-set likelihood consistent for the parameters of the full
choice set. The correction is exactly zero on the observed row and takes a fixed
value on the non-employment row, so it bites only on the drawn working packages.
The estimation sample is 1,555 single-adult households at 101 alternatives each,
157,055 rows; the parameter vector has 51 coordinates, 41 free, 10 carrying
identically zero gradient on a singles-only sample, and 39 interior.
**[ACCEPTED]**

**$q$ is computation, $g$ is economics.** The two objects share the words
"hours", "wage" and "occupation" and share nothing else. $q$ is the
importance-sampling proposal the alternatives were *drawn* from: a calibrated
numerical instrument, not estimated, carrying no parameter of interest, and
cancelling from the estimand exactly, because the composite index carries the
matching $-\log q$ correction. Changing the proposal can change only the
Monte-Carlo efficiency of the estimator. An arm that "does better" as a proposal
is a better *sampler*, never a better *model*, and no coefficient, sign or
magnitude on the proposal side may be read economically. In particular, **a
proposal may be richer than its target**: conditioning the wage proposal on
occupation is a variance-reduction choice and says nothing about whether wage
offers genuinely shift with occupation — only the structural $g^{W}$ block
speaks to that. **[ACCEPTED]**

**Identification remarks.** Two invariance results discipline how the estimates
are read, and both are exact reparameterisation checks rather than robustness
exercises.

1. *Age centring is exact.* Re-centring the age variable and carrying the
   admissible set through the exact map returns the same optimum: the objective
   agrees with the specification of record to $1.38\times10^{-10}$ against a
   $10^{-8}$ band, and the active set and the near-boundary flagged set are
   identical. **[ACCEPTED]**

2. *Bound-activity in the leisure block is a normalisation artefact, not a
   property of the model.* The leisure normaliser is a unit choice. Re-expressing
   the accepted point at $\lambda_{\ell}=40$ by the exact map — no
   re-estimation — sends the age-squared coefficients from $+1.0$ (at the
   ceiling of their box in the $\lambda_{\ell}=10$ unit) to $0.034845$ for men
   and $0.055555$ for women, strictly interior. The statement "age-squared is at
   a bound" is therefore a statement about the $\lambda_{\ell}=10$ unit, not
   about the model. Invariance across $\lambda_{\ell}\in\{10,40,45\}$ holds with
   the objective bitwise equal, choice probabilities agreeing to
   $6.11\times10^{-16}$, marginal rates of substitution to $5.55\times10^{-16}$
   in relative terms and indifference curves to $2.17\times10^{-10}$ euros.
   **[ACCEPTED]**

Inference is a cluster-robust (CR1/HC1) sandwich on household-clustered scores
with $G=1{,}555$ clusters, the bread taken on the interior block, and the finite-
sample constant $c=G/(G-K_{\text{interior}})=1.0257255936675462$ at
$K_{\text{interior}}=39$; coefficients are read against the normal quantile
$z_{0.975}=1.959963984540054$ rather than a $t$ quantile, because the sandwich is
an asymptotic normal-approximation object with no exact small-sample $t$
distribution behind it. Two coordinates rest on active bounds and are dropped
from the inference block entirely, carrying no standard error. **[ACCEPTED]**

Full estimation detail — the multi-start protocol, the four-leg convergence
standard, the curvature battery and the profile machinery — is in **Appendix A**.

---

## 2.3 The welfare measure

Welfare is money-metric. Each measure asks what consumption level, under a
stated reference object, would leave the household exactly as well off as its
own opportunity situation. In the companion theory paper's notation, a measure
solves

$$
W(z,R,A;y)=w \quad\Longleftrightarrow\quad z \;\mathrel{I}\; \max_{R}\{B\},
$$

an indifference between the attained bundle $z$ and the own-preference optimum
over a measure-specific counterfactual budget $B$; the measures differ **only**
in how $B$ is built. The axiomatic basis is the theory paper's, and is not
reproduced here: what that paper establishes, and what we use, is that each
member of the family is characterised by the responsibility/compensation stance
its reference encodes, so that choosing a reference is a normative act made
explicit rather than a technical convenience. We cite it and take the family as
given. **[ACCEPTED]**

**The carrier measure: $W^1$, equivalent income at a common reference pay.**
$W^1$ builds $B$ from the household's **own** opportunity set $A$ with **pay
ignored**: $z'=(c',j')\in B \iff j'\in A$ and $c'=w$, a flat consumption level
$w$ at every job in $A$. The money-metric anchor is that flat level $w$ itself.
$W^1$ is therefore the equivalent income at a common reference pay: it
compensates for pay and holds the household responsible for its set — it prices
*what you can get*, never *what it pays*. It is the measure the decomposition is
carried on. **[ACCEPTED]**

**The normative-reference sensitivities: $W^4$ and $W^6$.** $W^4$ takes the
non-employment option as its reference — the consumption level making the
household indifferent between $z$ and staying home at $w$ — and is a Full
Compensation reading. $W^6$ takes the universal job set under an equal-pay
profile, and is Full Compensation with a weak-responsibility component. They are
reported as **normative-reference disclosures**: they show how the valuation
moves when the responsibility cut moves. They are **not** evidence that the
$W^1$ result is quantitatively robust, and no cross-measure quantitative
robustness claim is licensed in any form. **[ACCEPTED]**

One member of the family is not operational on this design and is recorded as a
compatibility finding rather than a result: the best-paid-equivalent measure
requires the maximum pay over the household's actual set, whereas any
implementation here can only form the maximum over its *sampled* nodes. On a
continuous latent support those are not the same object, and the gap is not a
precision problem a longer basis fixes — the sampled-set maximum has no
basis-invariant target. It is out of the source decomposition and out of
paper-facing welfare inequality. **[ACCEPTED]**

**The ex-ante continuum construction. [PROVISIONAL]** The nodes are *integration
support*, not a menu, and in the ex-ante construction the observed job carries no
privileged mass in any state: the estimator drops the observed job's privileged
weight in all sixteen coalition states, keeps only stochastic nodes with the
exact proposal correction, and averages across scrambles before the log and the
money-metric inversion. This is a design property that was **tested, not
assumed**. The observed job's median mass share is $0.0000$, so removing it
shifts the fully-common-state index by about $10^{-5}$; and 98.9–99.7% of the
variance at that state is persistent between households rather than
within-household across scrambles, so the dispersion is not finite-support
integration noise. The structural non-employment atom survives the construction
— every household retains at least 404 drawn non-working nodes and at least 50 in
every scramble — which is what makes the ex-ante cells comparable to the
sampled-set cells they replace. The two are never mixed. The construction
currently carries the status `EX_ANTE_SUPPORT_DIAGNOSTIC_IN_PROGRESS`.

**The coalition-consistent inversion. [PENDING — D4]** The money metric inverts
each household's welfare level against a *frozen reference core*: its own
baseline choice set, held fixed at the baseline coalition by contract, precisely
so that the yardstick does not move when the coalition does. That is what makes
coalition values comparable at all. It also means the inversion's reference is
**not** equalised by any operator in the decomposition, by design. The
requirement this raises — that the same reference set $\bar A$ and the same
responsibility stance $R$ appear on *both* sides of the inversion in every
coalition — is the open design item, and is settled in the D4 stream rather than
here. Until it is settled, no share, ratio or percentage built on the fully
common state is claimable (§2.4).

---

## 2.4 The decomposition

**The two-player structure.** The headline architecture is an exhaustive
two-player game — **preferences versus the complete environment** — with the
environment's internal channels entering as a *nested*, grouped layer. In Owen
terms the coalition structure is $\{\{P\},\{A,B,D\}\}$ over the primitive
players

* $P$ — preferences: the leisure weight, its age profile, the child shifter, and
  the preference block itself;
* $A$ — access: the employment margin, its regional and urbanisation arguments,
  and occupation availability;
* $B$ — wage ability and wage technology: the education and experience loadings
  of the offer-wage location;
* $D$ — the complete budget channel: non-labour income, needs-related
  demographics and every other household-specific input to the tax–benefit
  budget mapping.

Two properties of the structure matter for how it is read. First, the two-player
partition sums to 100% by construction, so preferences and environment exhaust
the game *conditional on exhaustiveness holding* (see below). Second, **signed
contributions are legitimate**: a channel may enter with either sign, because
equalising a channel can raise measured inequality as easily as lower it, and no
component is a share of a positive total. Nothing here is a pie chart. The
nested $A/B/D$ layer is reported **unranked**: this section makes no claim about
the relative size of access and wage-ability, in either direction.
**[ACCEPTED]**

$D$-equalisation is a **panel swap, not a reweighting**: node utilities are
re-evaluated against the budget the tax–benefit system returns for the node's
own wage and hours against a common reference background. The residual of the
earlier three-player presentation is **not** relabelled as $C_D$; $C_D$ is formed
from its own Owen marginals, because the interactions have to be evaluated
rather than assumed away. A variable used on both sides moves only on the side it
is used on — the leisure-weight child term stays with $P$, while the
tax-benefit-side child term moves with $D$. **[ACCEPTED]**

**The four cells and their level analogues.** The design evaluates exactly four
preference/environment states, under one identical welfare definition and
reference convention in all four:

| cell | preferences | environment | coalition |
|---|---|---|---|
| $W^{00}$ | own | own | $\{\}$ |
| $W^{10}$ | reference | own | $\{P\}$ |
| $W^{01}$ | own | reference | $\{A,B,D\}$ |
| $W^{11}$ | reference | reference | $\{A,B,D,P\}$ |

with $I^{00},I^{10},I^{01},I^{11}$ the corresponding inequality indices. These
are **well-being levels under stated reference conventions**. The governing
ruling is explicit: *"This is not compensating variation and requires no tax
reform."* No cell is a compensating variation, none is $CV$, $CV^{\circ}$ or
$CV^{\mathrm{pref}}$, and none may be described in those terms. **[ACCEPTED]**

**The mapping note, verbatim. [ACCEPTED]** The design record states the
$CV$-family architecture in these terms:

> Record in decision_note.md:
>
> - standard CV compares pre/post policy environments under actual
>   preferences and circumstances;
> - CVcirc neutralizes preferences while retaining circumstances;
> - CVpref neutralizes wages/opportunities while retaining preferences;
> - the JMP two-player Shapley uses all four preference/environment
>   combinations and is not merely the opposite of CVcirc.
>
> Do not execute a tax reform inside the current sprint.
>
> Preserve standard CV, CVcirc and CVpref as a later policy module after
> the cross-sectional JMP decomposition is complete.

*(Design record: consolidated rulings document, §7 "CV / TAX-REFORM
ARCHITECTURE" of the complete R-202 ruling, entered by the dated corrective
append of 2026-09-01.)*

The four cells are the **level analogues** of those objects, by what each
neutralizes rather than by identity — $W^{10}$ answers to $CV^{\circ}$
(preferences neutralized, circumstances retained), $W^{01}$ to
$CV^{\mathrm{pref}}$ (wages and opportunities neutralized, preferences
retained), and $W^{00}$ to the actual-preferences-and-circumstances state that
a standard $CV$ evaluates across a reform. $W^{11}$ has **no** $CV$-family
counterpart. The analogy is one of construction only: the $CV$ objects are
compensating variations across a policy reform and the cells are levels with no
reform in them, which is why the sentence quoted above governs — no cell may be
called a $CV$. The record's own warning carries directly into the reading of
§2.4: the two-player Shapley **uses all four** combinations and **is not merely
the opposite of $CV^{\circ}$**. **[ACCEPTED]**

> **[OPEN — not owed by the source text.]** Earlier drafts recorded a deputy
> positioning sentence on Jacquet, Jia and Thoresen (2026) as owed verbatim by
> this clause. The complete ruling is now on disk and §7 contains **no such
> sentence**; the expectation was mistaken. Nothing is reconstructed here. A
> positioning sentence, if wanted, requires new deputy text entered by its own
> dated append. The paper's distinctness from that work is argued in the
> positioning memo, not by quoted authority.

**Exhaustiveness is a tested property, not an assumption.** The construction is
licensed to report shares only if the fully common state $I^{11}$ is negligible,
and the negligibility test was **pre-stated before any cell was read**: $I^{11}$
counts as negligible only if *both* (i) $|I^{11}|\le 0.00125$, the certified
Gini-scale component-level precision constant of record, and (ii)
$|I^{11}|/I^{00}\le 0.01$. The ruling is equally explicit that $I^{11}$ is not to
be forced to zero and not to be renormalised mechanically, and that a
non-negligible $I^{11}$ **halts** the headline. **[ACCEPTED]**

On the complete-environment implementation the test **fails on both limbs, in
every arm**: $I^{1111}/I^{0000}=3.0288$ on the preferred specification and
$3.2566$ on the benchmark, under the primary reference block, with the
reconciliation identities holding at machine precision. Equalising preferences
and the complete environment leaves an index roughly three times the one we
started from. Accordingly the shares $s_P$ and $s_E$ are **not computed, not
forced and not renormalised**, the headline percentage is halted, and the
surviving heterogeneous objects are enumerated by measurement rather than
argument. The measurement is what identifies the open item: the budget channel
demonstrably removes the dispersion it was built to remove, and the fully common
state barely moves — so the residual is not budget heterogeneity, and §2.3's
inversion reference is where the design work now sits. **[PROVISIONAL]**

This is a stronger statement than the earlier presentation could make. In the
three-player frame the same quantity read as a leftover residual; in the
four-cell frame it is a *named cell*, the object the exhaustiveness test is
about, and the failure is unavoidable rather than easy to under-weight. Nothing
was hidden by the earlier frame; the new frame makes the test decisive.
**[ACCEPTED]**

---

## 2.5 The numerical layer

Three sources of numerical error are handled separately and reported separately.
None of them is sampling uncertainty.

**Importance sampling with a defensive mixture.** Alternatives are drawn from a
proposal that is a **defensive mixture**: each unit block allocates 75 base draws
and 25 defensive draws — mixture weight $\lambda=0.25$ exactly — on disjoint
ladder, base, defensive and counter address spaces, so that no region of the job
space carries a proposal density that can vanish relative to the target. The
mixture bound is checked as a gate rather than assumed. **[ACCEPTED]**

**Randomised QMC for the welfare integrals.** The welfare functionals are
integrals over the estimated opportunity density, and are evaluated on an
Owen-scrambled Sobol basis with **eight independent scrambles**. Per household
the per-scramble integral $J_{ir}$ is formed on its own sub-basis, and
$\bar J_i=\mathrm{mean}_r J_{ir}$ is taken **before** the log and before the
money-metric inversion — the order matters, and it is the order of record. That
$\bar J_i$ equals the corresponding column selection on the single staged basis
was **falsified numerically rather than asserted**: computed the two ways, the
largest relative disagreement across all 1,555 households is
$1.37\times10^{-14}$ and $1.42\times10^{-14}$, i.e. float64 summation order.
**[ACCEPTED]**

**Bands: delete-one-scramble jackknife.** Precision is reported by a
delete-one-scramble jackknife over the eight scrambles,

$$
SE_{\text{jack}}=\sqrt{\tfrac{7}{8}\textstyle\sum_r (T_{(-r)}-\bar T)^2},
\qquad
E_T=t_{0.975,7}\cdot SE_{\text{jack}},\quad t_{0.975,7}=2.364624251 .
$$

No bias term is folded into $E_T$; the jackknife bias signal is computed and
disclosed on every row as a diagnostic with no pass/fail role. Precision
standards are stated per class of quantity rather than as one global tolerance,
because the quantities live on different scales: a mean or a median must be
resolved to 0.25% of its own scale, while a Gini and each component level of the
decomposition — a weighted sum of Gini differences, hence on the Gini scale —
must be resolved to 0.00125 in absolute terms. **[ACCEPTED]**

**MC bands are numerical-integration precision, never sampling confidence
intervals.** This is a reporting rule, not a caveat. The band $\pm E_T$ addresses
how well the integral is resolved on the basis it was computed on, and nothing
else. No sampling-uncertainty language attaches to it, and every banded quantity
travels with its band — a bare point estimate is not a licensed claim.
**[ACCEPTED]**

**Profile envelopes are a separate object.** Where a coordinate's conditional
influence is at issue, it is reported as a likelihood-profile envelope with the
remaining coordinates re-optimised at each constrained point. That envelope
addresses conditional uncertainty in that coordinate only. It is a different
object from the numerical band, and the two are **never combined**: their union,
sum or any other composition must not be presented as a statistical confidence
interval. Every profile envelope travels with its active-set and box-boundary
caveat. **[ACCEPTED]**

**The three-way uncertainty report.** Every welfare or decomposition magnitude is
therefore accompanied by up to three distinct objects, always shown separately:

| object | what it addresses |
|---|---|
| the RQMC band $\pm E_T$ | numerical-integration uncertainty **only** |
| the 95% profile envelope | conditional uncertainty in the profiled coordinate **only** |
| sampling uncertainty of the estimated parameter vector | **not estimated for these functionals** |

The third row is stated rather than elided: the welfare functionals in this paper
carry no sampling-uncertainty estimate, and no reader should infer one from the
first two. **[ACCEPTED]**

The instrument-level detail — the scramble construction, the common-random-number
pairing, the staging identities and the gate battery — is in **Appendix C**.

---

## Self-check table

### (a) Numerals → source

| numeral (as used above) | source |
|---|---|
| 1,555 households / 101 alternatives / 157,055 rows | `MNL/experiments/JMP_PS1/decision_note.md` §11.2 |
| 51 coordinates / 41 free / 10 pinned / 39 interior | `decision_note.md` §11.1 |
| $\beta_c\equiv 1$ (scale numeraire); $\beta_{\mathrm{F35}}\equiv 0$; $\beta^{\mathrm{occ}}_{1,g}\equiv 0$ | `MNL/notebooks/france/fr_singles_results_discussion_v1.ipynb` §4(a)–(b) |
| $\lambda_{\ell}=10$ hours (leisure normaliser of record) | `decision_note.md` §19.7 (`l_scale = 10.0`) |
| five hours bands, four occupation categories, regions $r=2..8$ | notebook §4(b) |
| $G=1{,}555$; $K_{\text{interior}}=39$; $c=1.0257255936675462$; $z_{0.975}=1.959963984540054$ | `decision_note.md` §11.1 ("Robust inference") |
| age-centring invariance: negLL agreement $1.38\times10^{-10}$, band $10^{-8}$ | `decision_note.md` §1 |
| $\lambda_{\ell}=40$ re-expression: age² $+1.0 \to 0.034845$ (sm) / $0.055555$ (sf) | `decision_note.md` §2A(b) |
| $\lambda_{\ell}\in\{10,40,45\}$: probabilities $\le 6.11\times10^{-16}$; MRS $\le 5.55\times10^{-16}$; indifference curves $\le 2.17\times10^{-10}$ EUR | `decision_note.md` §1 |
| ex-ante: node-0 median mass $0.0000$; shift $\approx 10^{-5}$; persistence 98.9–99.7%; $\ge 404$ non-working nodes, $\ge 50$ per scramble | `decision_note.md` §19.7 |
| negligibility thresholds $0.00125$ (absolute) and $0.01$ (relative to $I^{00}$) | `decision_note.md` §17.3 |
| $I^{1111}/I^{0000}=3.0288$ (S8) and $3.2566$ (LOC4), primary reference block | `decision_note.md` §19.4 |
| defensive mixture: 75 base / 25 defensive, $\lambda=0.25$ exact | `MNL/docs/France_case/P2a/FR_P2a_m08_16x_pricing_and_functional_evaluation_v1.md` ("Blocks, superblocks, prefix") |
| eight scrambles; $\bar J_i$ before log and inversion; identity falsified to $1.37/1.42\times10^{-14}$ | `MNL/docs/France_case/P2a/FR_P2a_m08_loc4_rqmc_final_precision_results_v1.md` §2 |
| $SE_{\text{jack}}$ formula; $t_{0.975,7}=2.364624251$; no bias term folded in | same, §2 |
| precision standards: 0.25% of scale (mean/median); 0.00125 absolute (Gini, component levels) | notebook §8 ("The provisional numbers…") |

### (b) Claims → status

| claim / design element | status |
|---|---|
| Box–Cox utility, taste shifters in the leisure weight | **[ACCEPTED]** |
| four-factor opportunity density $g^{E}g^{H}g^{\mathrm{Occ}}g^{W}$ | **[ACCEPTED]** |
| 35-hour band coefficient as an *institutionally motivated opportunity peak* (not a statutory effect) | **[ACCEPTED]** |
| $\delta_{\mathrm{occ}}$ as offer-distribution location shifts, not causal premia | **[ACCEPTED]** |
| within-choice-set centring convention | **[ACCEPTED]** |
| $-\log q$ sampling-of-alternatives correction | **[ACCEPTED]** |
| "$q$ is computation, $g$ is economics"; a proposal may be richer than its target | **[ACCEPTED]** |
| age-centring exactness; bound-activity as a normalisation artefact | **[ACCEPTED]** |
| CR1/HC1 sandwich; $z$ rather than $t$; two bound-active coordinates carry no SE | **[ACCEPTED]** |
| $W^1$ as the carrier measure, equivalent income at a common reference pay | **[ACCEPTED]** |
| $W^4$/$W^6$ as normative-reference sensitivities; **no** cross-measure quantitative robustness claim | **[ACCEPTED]** |
| best-paid-equivalent measure excluded (no basis-invariant target) | **[ACCEPTED]** |
| ex-ante continuum: nodes are integration support; observed job not privileged | **[PROVISIONAL]** (`EX_ANTE_SUPPORT_DIAGNOSTIC_IN_PROGRESS`) |
| coalition-consistent inversion (same $R$ and $\bar A$ on both sides) | **[PENDING — D4]** |
| two-player Owen structure $\{\{P\},\{A,B,D\}\}$; nested $A/B/D$ unranked | **[ACCEPTED]** |
| $D$-equalisation as a panel swap; $C_D$ from its own marginals | **[ACCEPTED]** |
| four cells $W^{00}/W^{10}/W^{01}/W^{11}$; no cell is a compensating variation | **[ACCEPTED]** |
| level-analogue mapping note, quoted verbatim from the design record | **[ACCEPTED]** |
| Jacquet–Jia–Thoresen positioning sentence | **[OPEN — no such sentence in the source clause; not owed, not reconstructed]** |
| exhaustiveness as a pre-stated, tested property | **[ACCEPTED]** |
| exhaustiveness fails; headline halted; $s_P$/$s_E$ not formed | **[PROVISIONAL]** |
| defensive-mixture importance sampling | **[ACCEPTED]** |
| Owen-scrambled Sobol, 8 scrambles, delete-one-scramble jackknife | **[ACCEPTED]** |
| MC bands are numerical-integration precision, never sampling CIs | **[ACCEPTED]** |
| profile envelope a separate object; never combined with the band | **[ACCEPTED]** |
| three-way uncertainty reporting, third row stated not elided | **[ACCEPTED]** |

### (c) Prohibitions observed in this section

No headline percentage; no ordering claim between access and wage-ability in
either direction; no "stable component signs" or any collective-sign
formulation; no cross-measure quantitative robustness claim; no cell described as
a compensating variation; no "effect of the 35-hour law"; no theory-paper content
reproduced (the measure family is cited to it, and its axiomatics are not
restated).
