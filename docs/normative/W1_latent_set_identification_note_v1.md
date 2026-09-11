<!-- NORMATIVE NOTE — W1 AND THE LATENT OPPORTUNITY SET -->

# W1 and the latent opportunity set: what is maintained and what is identified

**Status.** Read-only mathematical and source audit. No estimation, no latent-set
simulation, no welfare or decomposition rerun, no calibration, no repair of the
old W1-EA. Every number below is either (i) read from a certified record, with
the path and digest given in Appendix A, or (ii) arithmetic performed *in this
note* on a published parameter table, in which case it is labelled
**[derived here]** and is not certified.

**Notation** (deputy's, used throughout; the symbol `w` is never used).

| symbol | meaning |
|---|---|
| $\omega$ | hourly wage (EUR/hour) |
| $h$ | weekly hours; $E=\mathbb 1\{h>0\}$ |
| $j$ | a job / package; $o$ the non-employment package; $\mathcal J$ the universal set |
| $y(j)$ | gross (pre-tax) earnings at $j$ |
| $C_i(j)$ | priced monthly **disposable** income at $j$ (EUR/month) |
| $m_i(j)$ | **equivalent consumption**: the flat consumption at job $j$ that makes $i$ indifferent to the observed bundle |
| $W_i^1$ | the Measure-1 well-being level, **in consumption units** (EUR/month) |
| $L_i(j)$ | the complete non-consumption index (both spouses for couples) |
| $A_i$ | the ability (latent opportunity) set; $\mathcal C_i$ the *sampled* set, a computational object |
| $g_i,\widehat g_i$ | opportunity density and its unit-mass normalisation; $q_i$ the proposal density |

**Superseded material.** `docs/JMP_W1_theory_to_implementation_bridge_v1.md`
(the "W1-EA bridge") is superseded on two points and must not be quoted for
them: the *sign* of $\Delta$ and the $W^4/W^1\approx 34$ ratio (scale artefact,
retracted by the S12 premise audit), and $\beta_c\equiv 1$ (the specifications
of record estimate $\beta_c$). Its separability identity survives and is
re-derived below. This note supersedes nothing else and repairs nothing.

---

## 0. Notation and equivalence: the implemented inversion **is** Measure 1

### 0.1 Measure 1, and why the min is the right reading

Haydar–Maniquet (2025), §3, Measure 1:

$$W(z,R,A;y)=m \iff z\;I\;\max_R\{B\},\qquad
z'=(c',j')\in B \iff j'\in A \text{ and } c'=m .$$

Define $m_i(j)$ by $u_i\!\left(m_i(j),j\right)=u_i(z_i^{\rm obs})$; it exists and
is unique because $R$ is continuous and strictly monotone in consumption.

1. Monotonicity of $c\mapsto u_i(c,j)$ gives, for each $j\in A_i$,
   $u_i(m,j)\ge u_i(z_i^{\rm obs})\iff m\ge m_i(j)$.
2. Hence $\max_{j\in A_i}u_i(m,j)=u_i(z_i^{\rm obs})$ holds iff
   $m\ge m_i(j)$ for **some** $j$ and $m\le m_i(j)$ for **every** $j$, i.e. iff
   $m=\min_{j\in A_i}m_i(j)$. $\blacksquare$

So $W_i^1=\min_{j\in A_i}m_i(j)$ **is** Measure 1 — flat consumption on the own
set, preferred job in it, indifference — and is not an alternative measure that
happens to agree. The three other candidates are excluded by inspection of the
same section: Measure 2 and Measure 3 build $B$ from $y(j)-t$ and $y(j)+m$ and
so are not flat; Measure 5 replaces $A$ by a common $\bar A$; Measure 6 uses
$\mathcal J$ rather than $A$.

### 0.2 Closed form under the specifications of record

The S11 specifications of record fix $\theta_c\equiv 0$ and the shock scale
$\tau=1$, and **estimate** $\beta_c$ (2.0387 singles, 2.1017 couples). The
deterministic index is therefore

$$u_i(c,j)=L_i(j)+\beta_c\log(c/\lambda_c).$$

Setting $u_i(m,j)=u_i(z_i^{\rm obs})=:\bar V_i$ and solving:

$$\boxed{\;m_i(j)=\lambda_c\exp\!\left[\frac{\bar V_i-L_i(j)}{\beta_c}\right]\;}$$

which is **strictly decreasing in $L_i(j)$**. Therefore

$$W_i^1=\min_{j\in A_i}m_i(j)=\lambda_c\exp\!\left[\frac{\bar V_i-\max_{j\in A_i}L_i(j)}{\beta_c}\right]
\qquad\text{— the min is attained at the highest }L_i(j).$$

Substituting $\bar V_i=L_i(j_i^{\rm obs})+\beta_c\log\!\big(C_i(j_i^{\rm obs})/\lambda_c\big)$ removes $\lambda_c$ entirely:

$$\boxed{\;W_i^{1}=C_i\!\left(j_i^{\rm obs}\right)\cdot
\exp\!\left[\frac{L_i(j_i^{\rm obs})-\max_{j\in A_i}L_i(j)}{\beta_c}\right].\;}\tag{0.1}$$

This is the single most consequential line in the note. $\lambda_c$ cancels
exactly, which is consistent with the record's units-convention finding (four
widely separated constants agree to $2.66\times10^{-15}$ relative).

---

## 1. Reference-domain check (addendum s1) — done first

### 1.1 (a) Is non-employment in every realised set *by construction*?

**No — it is a maintained restriction, and it is not identified.** Three distinct
objects must be kept apart.

* **$\mathcal C_i$, the sampled set** ($|\mathcal C_i|=101$: $R=100$ proposal draws plus the
  observed package, both populations, S11 record). This is a *computational*
  object. `canonical_notation_v5.md` states the rule: $q$ is "computation, not
  economics; never called an opportunity, an offer or an availability". Nothing
  about $\mathcal C_i$ licenses any statement about $A_i$.
* **The welfare panel** (2,048 common nodes). The non-employment bundle is present
  in it by construction, and the Stage-D gate `assert_home_option`
  (`m08_welfare_measures.py:239-252`, config
  `welfare_m08_decomposition_v1.yaml:251`, `assert_min_count_per_household: 1`,
  HALT on failure) enforces it. This is a property of the *panel*, not of $A_i$.
* **$A_i$ itself.** The likelihood contains no free parameter on the
  non-employment row. In the engine every opportunity term is gated on the
  employment indicator: `log_h = Σ β·(x·working)`
  (`engine_jax.py:310-314`), `log_w = where(working>0, ·, 0)`
  (`engine_jax.py:316-326`), every `market_opportunity` shifter carries
  `interaction: ["working"]`
  (`estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml`, `market_opportunity`
  block). So $g_i(o)\equiv 1$ **by parametrisation** — a normalisation, not a
  datum.

The consequence is sharp, and it is the main negative finding of §1. Under a
Poisson reading of $g_i\,d\nu$ (§2), an atom of intensity 1 at $o$ and a
*deterministically present* $o$ produce **identical choice probabilities**: with
i.i.d. Gumbel marks the market part contributes a Gumbel with location
$\log\int_{\rm mkt}e^{u}\,d\mu_i$, the home point a Gumbel with location $u_i(o)$,
and the max-of-independent-Gumbels probability is
$e^{u_i(o)}/\big(e^{u_i(o)}+\int_{\rm mkt}e^{u}d\mu_i\big)$ in both readings. But
the two readings differ at the **set** level: in the Poisson reading
$\Pr(o\notin A_i)=e^{-1}=0.368$. The data cannot separate them.

> **Finding 1a.** "$o\in A_i$ for every $i$" — the premise Measure 4 assumes
> outright and the premise on which §1.3 rests — is **observationally
> equivalent** to a reading in which it fails with probability $e^{-1}$. It is
> economically compelling (one can always not work) and it is the PI's to adopt;
> it is *not* established by the estimated model and must be declared, not
> inferred.

**Couples, the joint analogue (NN).** The couples package space is a space of
*pairs*; the joint non-employment point is $(o,o)$. The same argument applies to
it verbatim, with one addition the record confirms: on the 2,048-node panel,
`max_abs_L_home_minus_any_NN_node = 0.0` (`s12_w4_premise_audit_v1.json`,
`couples.home_bundle`), i.e. all NN nodes tie exactly in $L$, so "the NN node" is
well defined up to a tie-break with no consequence for $L$.

**Domain exception, recorded.** 119 of 2,223 couples have their eligible NN
bundle **outside the positive-consumption subdomain** on the welfare panel, and
the S10 101-alternative estimation domain carries 60 exact home atoms outside
the domain and 155 non-positive-consumption alternatives
(`s12_w4_premise_audit_v1.json`, `consumption_domain_count_reconciliation`; the
record warns explicitly that the 60/155 counts must not be transferred to the
2,048-node panel). For those 119 couples $m_i(o)=\lambda_c\exp[(\bar V_i-L_i(o))/\beta_c]$
is still finite and well defined — the formula never evaluates $\log C_i(o)$ —
but the *attained* side $\bar V_i$ is undefined at a node with $C\le 0$, so any
statement anchored on the NN bundle's own consumption fails for them.

### 1.2 (b) Does non-employment maximise systematic utility at equal consumption?

**Yes — for every household, and provably over the whole covariate domain, not
merely on the realised sample.**

Under equal consumption, utility differences are differences in $L$ alone.
In both executed specifications

$$L_i(j)=\beta_\ell^{g}(\mathbf x_i)\,\mathcal B\!\left(\tilde\ell_{ij};\theta_\ell^{g}\right),
\qquad \tilde\ell_{ij}=(80-h_{ij})/10,$$

for a single adult, and for a couple the index is **additive across spouses with
no cross-leisure term** — the couples specification of record carries 47
coordinates and `beta_ll` is *absent from the coordinate list*, not merely pinned
(`s11_welfare_specs_of_record_v1.json`, `results.COUPLES.names`). Two facts then
suffice:

1. $\mathcal B(z;\theta)=(z^\theta-1)/\theta$ has $\mathcal B'(z)=z^{\theta-1}>0$
   for **every** $\theta$, including the estimated negatives
   ($\theta_\ell$: $-1.6263$ sm, $-0.9274$ sf, $-0.9761$ cm, $-1.6863$ cf). So
   $\mathcal B(\tilde\ell)$ is strictly maximised at $h=0$, since employed hours
   are supported on $[5,70]$.
2. Therefore $L$ is maximised at $o$ **iff** $\beta_\ell^{g}(\mathbf x_i)>0$;
   for a couple, iff **both** $\beta_\ell^{m}(\mathbf x_i)>0$ and
   $\beta_\ell^{f}(\mathbf x_i)>0$, and then the joint maximiser is NN. (This is
   where the absence of $\beta_{\ell\ell}$ is load-bearing: with a cross term the
   problem would not separate and NN would need a joint argument.)

$\beta_\ell^{g}(\mathbf x_i)=\beta_{\ell 0}+\beta_{\ell a}a_i+\beta_{\ell a^2}a_i^2+\mathbb 1\{{\rm women}\}\beta_{\ell k}k_i$
is a quadratic in centred age with a **positive** leading coefficient in all four
blocks, so it attains a global minimum over the whole real line. **[derived here]**,
from the S11 parameter tables:

| block | $\beta_{\ell a^2}$ | $a^\*$ (decades) | $\min_a\beta_\ell$ at $k=0$ | child term | verdict |
|---|---:|---:|---:|---|---|
| singles male | $+0.77828$ | $-0.95206$ | **7.81447** | — | $>0$ for all $a$ |
| singles female | $+1.00000$ | $-0.03388$ | **5.86714** | $+0.16664\,k\ \ge 0$ | $>0$ for all $(a,k)$ |
| couples male | $+0.00648$ | $+0.61637$ | **3.97890** | — | $>0$ for all $a$ |
| couples female | $+0.00731$ | $+8.40369$ | **12.58681** | $-0.30547\,k$ | $>0$ iff $k<41.20$ |

> **Finding 1b.** Premise (b) holds **unconditionally** for three of the four
> preference blocks and, for couples' women, for every child count below 41.2 —
> i.e. on any admissible covariate domain. There are **no exceptions to list**.
> This is a stronger statement than a sample check, and it is stable to
> re-estimation only in the sense that the sign of $\beta_{\ell 0}$ is what it
> depends on; it should be re-verified whenever the preference block moves.

**Independent confirmation from the record.** The S12 premise audit evaluates
$\arg\max_j L_i(j)$ node by node on the whole welfare panel and reports
`home_is_argmax_L: pass = true, n_fail = 0`, with
$\max_j L_i(j)-L_i(o)=0.0$ **exactly** (tolerance $2\times10^{-12}$), for
1,540 singles $\times$ 2,048 nodes and 2,223 couples $\times$ 2,048 nodes.
Algebra and record agree.

**One caveat that is not cosmetic.** "Maximises systematic utility" is a
statement about $L$, i.e. about $R$ represented by the *deterministic* index. The
model also carries i.i.d. type-I extreme-value shocks at scale $\tau=1$. The
deputy's own instruction is that the shocks stay in the conditioning and are
**excluded from the welfare ordering**; §1.3 and (0.1) depend on that exclusion.
If the shocks were admitted into $R$, no job would be the taste-maximum almost
surely and the whole of §1.3 would fail. This is a third maintained assumption,
alongside $o\in A_i$ and $\beta_\ell>0$.

### 1.3 (c) The consequence, reported under both readings

Combining (0.1) with $\arg\max_{j\in A_i}L_i(j)=o$:

**Reading I — non-employment *inside* the reference set (Measure 1 as written, with $o\in A_i$).**

$$\boxed{\;W_i^{1}=m_i(o)=C_i\!\left(j_i^{\rm obs}\right)\exp\!\left[\frac{L_i(j_i^{\rm obs})-L_i(o)}{\beta_c}\right]\;}\tag{1.1}$$

and since $L_i(o)\ge L_i(j)$ for all $j$, the exponent is $\le 0$:
$W_i^1\le C_i(j_i^{\rm obs})$, with equality exactly for a non-employed
household. **Plainly:** under the executed specifications, Measure 1 collapses to
Measure 4 (the staying-home equivalent), and reduces to *observed disposable
income discounted by the leisure forgone relative to full leisure*. The
remaining latent set does **not** affect baseline $W^1$ at fixed attainment —
$A_i$ enters (1.1) only through the statement $o\in A_i$. Access can still affect
*counterfactual* attainment, because a counterfactual moves $j_i^{\rm obs}$ (§4, §6C).

Three things follow that should be said out loud rather than left in the algebra.

* This is **not** a theorem about Measure 1. Haydar–Maniquet's table records
  $W^1$ as **not** satisfying Independence of $A$, and Theorem 1 shows no measure
  satisfies Representation, Independence of $A$ and Responsibility For Equal Pay
  together. The collapse here is **domain-restricted**: it holds on the subdomain
  where every $A$ contains $o$ and every admissible $R$ ranks $o$ first at equal
  consumption. Theorem 1's proof constructs $A=\{j_1,j_2\}$ with opposed tastes
  and no home node — precisely the configuration this subdomain excludes. There
  is no contradiction, and no axiom has been rescued.
* The normative content changes. On this subdomain the measure that was chosen
  *to hold individuals responsible for their ability set* stops distinguishing
  ability sets. Whatever "job access" contributes to measured inequality in the
  decomposition therefore travels entirely through attainment, never through the
  reference.
* The executed object is **not** (1.1). See §6B: the S12 implementation evaluates
  attainment ex ante, not at $j_i^{\rm obs}$.

**Reading II — non-employment *excluded* from the reference set (the
"working-opportunities-only" domain).**

$$W_i^{1{\rm -W}}=\min_{j\in A_i\cap\{h>0\}}m_i(j)
=\lambda_c\exp\!\left[\frac{\bar V_i-\max_{j\in A_i,\,h_j>0}L_i(j)}{\beta_c}\right].$$

Here the latent set **does** bind: the max runs over a random set, the answer
depends on how much of the market the household can actually reach, and the
offer-intensity scale is not inert (§3). This reading is already computed in the
record as a *reference-domain diagnostic* (not a robustness specification) on the
stochastic functional, and the difference is large for single adults:

| | median level (EUR/month) | median ratio to the executed $W^1$ |
|---|---:|---:|
| singles | 17,458.38 | **4.2896** |
| couples | 1,791.30 | **1.0097** |

> **Neither reading is adopted here.** The choice is the PI's. It is not a
> technical detail: for single adults it moves the level by a factor of four and
> it decides whether baseline $W^1$ is latent-set-free (Reading I) or
> latent-set-bound (Reading II).

---

## 2. The stochastic opportunity process: what the executed likelihood maintains

### 2.1 The likelihood, exactly as coded

The index and the criterion, from the engine and the manuscript:

$$V_{ij}=u_{ij}+\log g_{ij}-\log q_{ij},\qquad
\Pr(y\mid\mathcal C_i)=\frac{n_y\exp V_{iy}}{\sum_{s\in\mathcal C_i}\exp V_{is}},$$

with $g_{ij}=g^{E}_{ij}\big(g^{H}_{ij}g^{\rm Occ}_{ij}g^{W}_{ij}\big)^{E_{ij}}$ and
$q_{ij}=q^{E}_{ij}\big(q^{H}_{ij}q^{W}_{ij}q^{\rm Occ}_{ij}\big)^{E_{ij}}$.
Code: `engine_jax.py:292-340` (index; $u$ at 300-308, $\log h$ at 310-314,
$\log \omega$-density at 316-326, $\log$ market + centering at 328-337, the
composite and $-\log q$ at 339-340), `engine_jax.py:342-350` (criterion),
`jgroup_logsumexp` at `engine_jax.py:73-100` with the criterion-A multiplicity
$\log n_y$ added to the numerator only (line 99).

**No Poisson count appears anywhere in the code, and none is needed to write the
likelihood.** What the criterion literally maintains is weaker and should be
stated as such:

1. **Relative composition of offers.** Within a household, $g$ is a *measure on
   the package space* whose shape is identified: the hours-band elevations over a
   residual reference set of total width 26.5 h/week, the occupation table with
   $\beta^{\rm occ}_{1,g}\equiv 0$, and the truncated log-normal wage-offer
   density renormalised on $[2,590]$ EUR/hour.
2. **Market vs non-market relative intensity.** $g^{E}$ is *not* a household
   constant: every one of its coefficients multiplies a column interacted with
   `working`, so $g^{E}_{ij}=\exp\{(\beta_E+\beta_s s_i+\sum_r\beta_r{\rm reg}_{ir}+\beta_u u_i+\beta_m m_i)E_{ij}\}$.
   It is exactly the log intensity of market packages *relative to the
   non-employment atom*, and it is identified: $\beta_E=-3.1735$ (SE$_{\rm CR1}$
   0.4053, $z=-7.83$) for singles; $\beta_E^{m}=-2.1233$, $\beta_E^{f}=-2.8148$
   for couples.
3. **A common intensity normalisation, imposed not estimated.** $g_i(o)\equiv 1$
   (§1.1). Relaxing it — writing $g_i(o)=\kappa_i$ free — makes $\log\kappa_i$
   and $\beta_E$ (plus the household market index) exactly collinear.
4. **No expected number of realised market jobs is estimated.** The criterion
   never forms a count. A count exists only under an *added* Poisson hypothesis
   (§2.3).

### 2.2 The $\kappa_i$ test, algebraically

Let $\kappa_i>0$ and replace $g_{ij}\mapsto\kappa_i g_{ij}$ for **every** $j$
including $o$. Then $\log g_{ij}\mapsto\log g_{ij}+\log\kappa_i$, so
$V_{ij}\mapsto V_{ij}+\log\kappa_i$ for every $j\in\mathcal C_i$, and

$$\frac{n_y e^{V_{iy}+\log\kappa_i}}{\sum_{s}e^{V_{is}+\log\kappa_i}}
=\frac{n_y e^{V_{iy}}}{\sum_{s}e^{V_{is}}} .$$

**The choice probabilities are unchanged. A household-specific common
opportunity-intensity scale is not identified.** Cited lines: the shift enters at
`engine_jax.py:339-340`; it cancels in `jgroup_logsumexp`
(`engine_jax.py:90-92` for the denominator, line 94 or 97 for the numerator);
nothing else in `neg_ll` (`engine_jax.py:342-350`) sees $g$.

The code itself demonstrates the inertness. `market_opportunity` declares
`center_within_choice_set: true, center_weights: "proposal"`, and
`_center_proposal` (`engine_jax.py:114-120`, invoked at `engine_jax.py:333-337`)
subtracts the proposal-weighted within-set mean of $\log g^{\rm market}$. Because
every market shifter is a household-level covariate times $E_{ij}$, that mean is
$c_i\bar E_i$ with $c_i$ the household market index, so centering *is* the
substitution $\kappa_i=\exp(-c_i\bar E_i)$. It is applied for numerical
conditioning, it changes $g_i(o)$ from 1 to $\exp(-c_i\bar E_i)$, and it leaves
the likelihood exactly invariant. That is the cleanest possible demonstration
that $\kappa_i$ is free.

> **Finding 2.** The identified opportunity object is the measure $g_i\,d\nu$
> **relative to the non-employment atom**, i.e. up to one positive
> household-specific factor. The offer-intensity *scale* is fixed by the
> normalisation $g_i(o)\equiv 1$ and by nothing else.

### 2.3 The scale, from the model and the likelihood only

Two statements about the scale are licensed; a third is not.

**Licensed.** *Relative* market intensity per unit of base measure is
$\exp(\beta_E+c_i)$. On the S11 singles estimates, at zero household market index
and before centering, $\exp(\beta_E)=0.04187$: a unit of $\nu$-mass in the market
carries about 4.2% of the non-employment atom's intensity.

**Licensed only under an added hypothesis.** *If* one adds the hypothesis that
$A_i$ is generated by an inhomogeneous Poisson process on $\mathcal J$ with
intensity measure $\mu_i(dj)=g_i(j)\nu(dj)$, and *if* one keeps the normalisation
$g_i(o)\equiv 1$ (so the home option arrives with intensity exactly one), then

$$\mathbb E\!\left[N_i^{\rm mkt}\right]=\int_{\rm mkt}g_i\,d\nu
=e^{\beta_E+c_i}\Big(\textstyle\sum_k e^{\beta^{\rm occ}_{k,g}}\Big)\int_5^{70}e^{g^{H}(h)}\,dh ,$$

the wage factor contributing exactly 1 because $g^W$ is renormalised on its own
support. **[derived here]**, at $c_i=0$, uncentered:

| quantity | value |
|---|---:|
| $\int_5^{70}\exp\{g^H(h)\}dh$ (residual width 26.5) | 109.6096 |
| $\sum_k e^{\beta^{\rm occ}_{k,m}}$ / $\sum_k e^{\beta^{\rm occ}_{k,f}}$ | 2.0963 / 4.5428 |
| $\mathbb E[N^{\rm mkt}]$, single men / single women | **9.62** / **20.84** |

This number is invariant to the units of $\nu$ (rescaling hours or wage units
rescales $\nu$ and shifts $\beta_E$ by exactly the offsetting amount), which is
why it is well posed at all. It is **not** invariant to the normalisation
$g_i(o)\equiv 1$: it is literally "expected market offers per home option", and
the denominator is the convention. For couples the package space is a space of
**pairs**, so a Poisson-on-pairs reading implies a product-form dependence
between the spouses' offer arrivals that is a maintained assumption and is
nowhere tested.

**Not licensed.** The old W1-EA kernel masses — median $\int\widehat g$ of
**0.0773** (singles) and **147.96** (couples) on the S12 panel's $H$-domain — are
**not set sizes, not offer counts, and must not be reinterpreted as such.** They
are the total mass of the *un-normalised* welfare kernel on the panel's own
domain under the panel's own per-node base-measure convention. They combine (i)
the free scale $\kappa_i$ of §2.2 with (ii) the discretisation convention of the
2,048-node grid. The record itself withheld the as-run $W^4$ levels for exactly
this reason, and its verdict line is `failed_premise: "(b): ghat is not
normalized on the domain used by H"`.

---

## 3. How $W^1$ depends on the scale

### 3.1 The Poisson survival form, and why it degenerates here

The model does not itself supply a Poisson count (§2.3). *Conditional on adding
one*, with intensity $\kappa_i\lambda_i(dj)$ on the market and the home option
present with certainty, the theory measure of §0 has the survival function the
deputy writes:

$$\Pr\!\left(W_i^1>x\mid\kappa_i\right)=\Pr\!\left(\text{no available job with }m_i(j)\le x\right)
=e^{-\kappa_i\Lambda_i(x)},\qquad
\Lambda_i(x)=\lambda_i\big(\{j:\ m_i(j)\le x\}\big),$$

truncated above at $m_i(o)$ because $o$ is available with certainty:
$\Pr(W_i^1>x)=0$ for $x\ge m_i(o)$. The scale enters as a pure exponent:
$\kappa_i$ multiplies the whole cumulative hazard, so raising it stochastically
*lowers* $W^1$, and the two limits are

* $\kappa_i\to 0$: $\Pr(W^1>x)\to 1$ for every $x<m_i(o)$, so $W_i^1\to m_i(o)$ —
  the staying-home equivalent, Measure 4;
* $\kappa_i\to\infty$: $\Pr(W^1>x)\to 0$ for every $x$ with $\Lambda_i(x)>0$, so
  $W_i^1\to\operatorname{ess\,inf}\{m_i(j)\}$ over the market support — the
  taste-best reachable job.

**But §1.2 collapses this.** Since $L_i(o)>L_i(j)$ strictly for every $j$ with
$h_j\ge5$, and $m_i(\cdot)$ is strictly decreasing in $L_i(\cdot)$, we have
$m_i(j)>m_i(o)$ for every market $j$, hence

$$\Lambda_i(x)=0\ \ \text{for all }x\le m_i(o)
\quad\Longrightarrow\quad \Pr(W_i^1>x)=\mathbb 1\{x<m_i(o)\}\ \text{ for every }\kappa_i>0 .$$

> **Finding 3 (Reading I).** $W_i^1=m_i(o)$ **almost surely, for every value of
> $\kappa_i$**. The offer-intensity scale is not merely unidentified — it is
> *irrelevant* to baseline $W^1$. The two limits above coincide because the
> $\kappa\to 0$ limit is already attained at every $\kappa$.
>
> **Finding 3 (Reading II).** Drop $o$ from the reference domain and the
> degeneracy is gone: $\Lambda_i$ is non-trivial, $\Pr(W^{1{\rm -W}}>x)=e^{-\kappa_i\Lambda_i(x)}$
> is strictly decreasing in $\kappa_i$, $\kappa_i\to0$ gives $W^{1{\rm -W}}\to+\infty$
> (an empty reachable market: the household cannot be compensated by any flat pay
> at a job it cannot get) and $\kappa_i\to\infty$ gives the support infimum.
> Under Reading II, $W^1$ is identified **only conditional on a scale**.

### 3.2 What the model *does* support, and the analogue there

The functional actually executed is not a min over a random set; it is a
log-integral. Its analogue of §3.1 is an exact invariance, and it is better news.

With $\widehat g_{i,S}$ the state-$S$ kernel and $\theta_c=0$
(`04_welfare_and_decomposition.tex`, and `run_s12_welfare_record_v1.py:338-357`):

$$J_{i,S}=\int e^{L_{i,S}}\Big(\tfrac{C_{i,S}}{\lambda_c}\Big)^{\beta_c}\widehat g_{i,S}\,d\nu,\quad
H_{i,S}=\int e^{L_{i,S}}\,\widehat g^{\,\rm ref}_{i,S}\,d\nu,\quad
W_{i,S}=\lambda_c\exp\!\left[\frac{\log J_{i,S}-\log H_{i,S}}{\beta_c}\right]
=\left[\int C_{i,S}^{\beta_c}r_{i,S}(dj)\right]^{1/\beta_c},$$

with $r_{i,S}=e^{L}\widehat g/H$ the reference **probability** measure.

Apply $\widehat g_{i,S}\mapsto\kappa_i\widehat g_{i,S}$: both $J$ and $H$ scale by
$\kappa_i$, the difference of logs is unchanged, equivalently $r_{i,S}$ is
unchanged because it is normalised.

> **Finding 3 (implemented object).** $W_{i,S}$ is **exactly $\kappa_i$-invariant,
> in every state $S$** — because the code takes numerator and denominator over the
> *same* state's kernel (`run_s12_welfare_record_v1.py:342-347`: `attained =
> lse(u + op)`, `lam = lse(u - beta*log(c) + op_reference)`, both at coalition key
> `ck`). The unidentified scale therefore contaminates neither baseline $W^1$, nor
> the sixteen coalition states, nor the Owen decomposition built on them.

The exception is instructive and is the whole content of the retracted bridge:
$W^4=\lambda_c\exp[(\log J_i-\log S_i-L_i(o))/\beta_c]$
(`m08_welfare_measures.py:289-294`; `run_s12_welfare_record_v1.py:353-355`) has a
*single node* in the denominator and therefore **no integral against which
$\kappa_i$ can cancel**. That is why the as-run $W^4$ levels were scale-dependent
and were withheld, why the couples sign reversed and the singles sign did not,
and why after normalising $\widehat g$ to unit mass on exactly $H$'s domain the
record reports $\Delta\ge0$ and $W^4/W^1\le1$ **everywhere** (medians 0.9843
singles, 0.6242 couples; identity residual $5.9\times10^{-17}$ / $1.1\times10^{-16}$).
Any comparison of an integral measure with a single-node measure inherits the
free scale; a ratio of two integral measures does not.

---

## 4. Conditioning on the observed choice (clarification s3F, addendum s3)

### 4.1 The conditional law

Take the behavioural model as it is: a latent collection of packages, each
carrying its own i.i.d. type-I extreme-value shock at scale $\tau=1$, and the
observed package $y$ the argmax of $u+\varepsilon$.

Under the Poisson-plus-Gumbel construction of §3.1 the marked process
$\{(j,\varepsilon_j)\}$ on $\mathcal J\times\mathbb R$ with intensity
$\kappa_i\lambda_i(dj)\times e^{-\varepsilon}d\varepsilon$ has three properties
that deliver the conditional law in closed form:

1. the induced process of *utility values* $\{u_i(j)+\varepsilon_j\}$ on
   $\mathbb R$ is Poisson with intensity $\Theta_i\,e^{-v}dv$, where
   $\Theta_i=\kappa_i\int e^{u_i}d\lambda_i$;
2. its maximum $M_i$ is Gumbel with location $\log\Theta_i$;
3. the **location** of the maximum is independent of $M_i$, with
   $\Pr(y\in B)=\int_B e^{u_i}d\lambda_i\big/\int e^{u_i}d\lambda_i$ — which is
   exactly the executed criterion, and is where the $\kappa_i$-cancellation of
   §2.2 comes from.

Conditioning on $\{y \text{ chosen},\,M_i=v\}$, the **remaining** points form a
Poisson process on $\{(j,\varepsilon):u_i(j)+\varepsilon<v\}$ — the original
process **truncated below the attained utility level**, with the chosen point
inserted at $(y,v-u_i(y))$.

$$\boxed{\;A_i\mid(y,M_i=v)\ \sim\ \{y\}\ \cup\ \text{PPP}\ \text{restricted to}\ \{u_i+\varepsilon<v\}.\;}$$

Three consequences.

* **Simply adding $y$ to an unconditionally simulated set is not justified.** The
  unconditional draw places points above the attained level with positive
  probability; every such point contradicts the observation that $y$ was chosen.
  A set built that way is not a draw from $A_i\mid y$ — it over-represents
  high-utility alternatives, and the bias is one-sided: it makes every
  household's opportunity set look better than the data say it is. (Under Reading
  I this never surfaces, because $W^1$ does not read the set; under Reading II
  and in every counterfactual it does.)
* **$M_i$ is not observed.** Only $y$ is. The conditional law must be integrated
  over $M_i\mid y\sim$ Gumbel$(\log\Theta_i)$, whose location contains
  $\kappa_i$. So the conditional set law **does** depend on the unidentified
  scale, even though the choice probabilities do not.
* **The shocks stay in the conditioning.** They are what makes $M_i$ random given
  $(u_i,\lambda_i)$; excluding them from the *welfare ordering* (deputy's rule,
  used in §1.2) does not remove them from the *selection* mechanism.

### 4.2 What counterfactuals additionally need

Beyond everything already maintained for the baseline, a counterfactual attained
bundle requires:

1. **A value for $\kappa_i$** (or an explicit normalisation of it), because
   $M_i\mid y$ depends on it — §4.1.
2. **A re-selection rule for the shocks.** Either the household's realised
   $\varepsilon$-field is held fixed (a "same person, same match values" rule,
   which requires the conditional law of the whole marked process, not just of
   the set) or it is redrawn (an ex-ante rule, which answers a different
   question). The record's implementation takes the second route implicitly by
   using inclusive values; the choice is normative and should be declared.
3. **Invariance of $g$ and of the preference coefficients to the intervention.**
   The operators $T_P,T_A,T_B,T_D$ substitute *arguments* and hold coefficients
   fixed; that is a Lucas-type invariance assumption on the opportunity
   technology.
4. **No equilibrium response.** The operators equalise a factor across *all*
   households simultaneously, so the counterfactual is a general-equilibrium
   object being evaluated with a partial-equilibrium kernel. No market clearing
   for jobs is imposed and none is claimed.
5. **A stated attainment estimand** — realised bundle versus ex-ante inclusive
   value (§6B). Under the ex-ante estimand, items 1 and 2 are discharged
   automatically and the counterfactual inherits the $\kappa$-invariance of §3.2;
   under the realised-bundle estimand they are not.

---

## 5. Job identity versus pay (clarification s4)

**The mapping.** The empirical offer is $(k,h,\omega)$: occupation
$k\in\{1,\dots,4\}$, weekly hours $h\in[5,70]$, hourly wage
$\omega\in[2,590]$. Gross earnings are $y(j)=\omega\cdot h\cdot 52/12$
(the record forms exactly this: `run_s12_welfare_record_v1.py:411-413`).
Disposable income $C_i(j)$ is the tax–benefit function of $y(j)$ and the
household's budget inputs. Theory's job $j$ is the package; theory's $y(j)$ is
its pay.

**The question.** Are two offers with the same $(k,h)$ and different $\omega$
distinct jobs, or pay realisations of one job? Haydar–Maniquet address exactly
this in their model remarks (p. 2): one may either fix $y$ and distinguish jobs
by pay, or keep the job as the non-pecuniary bundle and let $y$ vary — and they
choose the convention that lets "pre-tax income vary without affecting the
preferences of individuals towards a particular job". The wording of the passage
is ambiguous as extracted; the *reason* given is unambiguous and points to the
second convention.

**The answer: the distinction does not affect $W^1$ — proved, not refuted.**

By (0.1), $m_i(j)$ depends on $j$ **only through $L_i(j)$**. In both executed
specifications $L_i(j)=\beta_\ell^{g}(\mathbf x_i)\mathcal B((80-h_{ij})/10;\theta_\ell^{g})$
is a function of **hours alone** — no wage argument, no occupation argument
(`engine_jax.py:300-308`: `u = beta_l_coeff*bc_l + beta_c*bc_c`, and
`bc_l = jbox_cox(leisure, theta_l)`). Therefore:

$$\omega\neq\omega'\ \text{with}\ (k,h)\ \text{equal}\ \Longrightarrow\ L_i(j)=L_i(j')\ \Longrightarrow\ m_i(j)=m_i(j'),$$

so the set $\{m_i(j):j\in A_i\}$, and hence its minimum, is invariant to whether
the wage coordinate is treated as a job label or as a realisation of $y$ on one
job. Collapsing the wage dimension is a **duplication** of packages in $A$, and a
min over a set is invariant to duplication.

**Which axiom does the work.** *Not* Job Duplication Invariance. JDI's antecedent
requires $y(j')=y(j)$ **and** $(x,j)\,I\,(x,j')$ for all $x$; here the second
holds and the first fails by construction, so JDI does not apply literally. The
invariance comes from **Independence of $y$**, which Measure 1 satisfies
(Haydar–Maniquet's table, $W^1$ row, $+$): the reference budget $B$ sets
$c'=m$ flat at every $j'\in A$, so $y$ never enters $B$ at all. JDI is what makes
the *duplication* harmless once the wage is collapsed; Independence of $y$ is
what makes the wage irrelevant in the first place.

**The same statement for the implemented integral, and its one honest caveat.**
For a min, duplication is free. For an integral it is not: the wage dimension
carries **mass**, so collapsing it reweights. The record establishes that it does
not matter here, and the reason is structural: $g^W$ is renormalised on its own
support, so it integrates to one conditional on employment and occupation, and
$L$ has no wage argument; hence $H_i$ is exactly free of every wage-block
parameter. Verified: $\max_i|\Delta\log H_i| = 1.78\times10^{-15}$ (singles),
$7.11\times10^{-15}$ (couples); median direct-reference-channel change **EUR
0.000** in both. The code goes further and builds the reference on an explicitly
wage-free kernel (`run_s12_welfare_record_v1.py:382`:
`wagefree_opp = opp_hat - log_gw + log_qw`), so pay-neutrality of the reference
is a construction as well as a property.

> The licensed sentence, and only it: **the reference is directly pay-neutral,
> and earning opportunities reach the measure through attainment** (median total
> change $-17.43$ EUR/month singles, $+110.53$ couples). This *supersedes* the
> old bridge's R2 defect ("the wage block is not inert in $W^1$", EUR 438 / 34%),
> which was measured on a non-final frame with a wage-carrying reference kernel.
> A change travelling through attainment does **not** establish that
> Independence of $y$ fails for the stochastic functional; that would require
> fixing the primitives the axiom holds fixed, which has not been done.

---

## 6. Three identification questions, answered separately

### (A) Is the full conditional distribution of $A_i$ identified?

**No.** What is identified from choices, under the maintained exclusion
restrictions (the local group-unemployment measure, region and urbanisation enter
availability and not preferences; the wage-offer distribution is independent of
offered hours conditional on occupation; preferences smooth in hours against
step-function availability), is the **relative composition** of $g_i$ across the
package space — and that only relative to the non-employment atom (§2.2).

Not identified: (i) the common intensity $\kappa_i$; (ii) therefore any count,
including $\mathbb E[N_i^{\rm mkt}]$ and $\Pr(A_i=\emptyset)$; (iii) the
*dependence structure* of the point process — Poisson, and for couples
product-form across spouses, are additional hypotheses under which the same
likelihood arises, and the record's own literature notes state the project's
stance that "the RO is estimation machinery, not a claim that opportunities are
random"; (iv) whether $o\in A_i$ with certainty (§1.1, Finding 1a).

*Maintained:* the four-factor functional form of $g$, the exclusion restrictions,
$\tau=1$, and $g_i(o)\equiv1$. *Identified:* the coefficients of the four blocks,
hence $g_i$ up to one positive household-specific factor.

### (B) Is baseline $W^1$ at the observed attained bundle identified even if $A$ is not?

**Under Reading I: yes, point identified, and it does not touch $A_i$ at all.**
By (1.1), $W_i^1=C_i(j_i^{\rm obs})\exp\{[L_i(j_i^{\rm obs})-L_i(o)]/\beta_c\}$.
The inputs are the observed disposable income, the observed hours, the leisure
block $(\beta_{\ell0},\beta_{\ell a},\beta_{\ell a^2},\beta_{\ell k},\theta_\ell)$
and $\beta_c$. **No opportunity parameter enters. No latent set enters. $\kappa_i$
does not enter. $\lambda_c$ cancels.** Identification of baseline $W^1$ reduces
entirely to identification of the preference block.

*Maintained for this:* $o\in A_i$ (not identified — Finding 1a);
$\beta_\ell^g(\mathbf x_i)>0$ (proved, Finding 1b); shocks excluded from the
welfare ordering.

**Under Reading II: no.** $W^{1{\rm -W}}$ is a min over the market part of $A_i$;
its distribution is $e^{-\kappa_i\Lambda_i(x)}$ and the scale is free.

**A third answer is needed, because the executed object is neither.** The S12
implementation evaluates the attained side **ex ante**:
$\log J_{i,S}=\log\int e^{u_{i,S}}\widehat g_{i,S}\,d\nu$, an inclusive value over
the household's own opportunity distribution over a 2,048-node common panel — not
$u_i(z_i^{\rm obs})$. The resulting $W_{i,S}=[\int C^{\beta_c}r_{i,S}(dj)]^{1/\beta_c}$
is a power mean of order $\beta_c$ of consumption under the reference measure. It
**is** identified given the parametric $g$ and the exclusion restrictions, and it
**is** $\kappa$-invariant (§3.2). But it is a **different estimand** from Measure
1 at the observed bundle: in it, the latent opportunity distribution is the whole
content of the reference weights $r_{i,S}$, whereas in (1.1) it is absent. The
two answer different questions — "what flat pay makes the jobs she faces as good
as the prospect she faces" versus "what flat pay on her own set makes her as well
off as the bundle she has". Reader-facing text must not use "the job she has" for
the first.

### (C) Are the counterfactual attained bundles and their $W^1$ identified under P/A/B/D?

**Under the ex-ante estimand: yes, conditionally, and the conditions are the ones
already declared.** $W_i(T_SX)$ is $\kappa$-invariant in every state (§3.2), the
reference moves with the state (`run_s12_welfare_record_v1.py:342-347`), the
identity closes numerically ($I_{\{P,A,B,D\}}$ zero to $\sim10^{-15}$; top-level
identity residual $2.78\times10^{-17}$), and the Owen decomposition inherits both.
What it rests on is §4.2 items 3–5: coefficient invariance under substitution, no
equilibrium response, and the ex-ante attainment rule. None of these is
identified; all are maintained.

**Under the realised-bundle estimand (Reading I made counterfactual): no.** A
counterfactual $j_i^{\rm obs}$ has to be re-selected from $A_i\mid y$, which
requires $\kappa_i$ and a shock rule (§4.1–4.2). Note the asymmetry this creates:
under Reading I *baseline* $W^1$ is latent-set-free but *counterfactual* $W^1$ is
not. Access affects welfare only through where people end up, which is exactly
what the decomposition is trying to measure — so the measure's baseline
insensitivity to $A$ is not a licence to ignore $A$ in the counterfactuals.

---

## 7. Verdict

**The verdict differs for baseline and counterfactual, and it differs by
reference-domain reading. No normalisation is chosen here.**

| object | verdict |
|---|---|
| **(B) Baseline $W^1$, Reading I** (Measure 1 with $o\in A$, observed attainment) | **POINT IDENTIFIED**, and latent-set-free: eq. (1.1). Conditional on three *declared* maintained assumptions, none of them identified: $o\in A_i$; $\beta_\ell>0$ (proved on the whole covariate domain); shocks excluded from $R$. |
| **(B) Baseline $W^1$, Reading II** (working-opportunities-only reference) | **IDENTIFIED CONDITIONAL ON A SCALE.** |
| **(B) Baseline $W^1$-EA**, the object actually executed | **POINT IDENTIFIED** given the parametric $g$ and the exclusion restrictions, and exactly $\kappa$-invariant — but it is **NOT YET MAPPABLE** onto Measure 1, because its attainment is ex ante rather than at $z_i^{\rm obs}$. |
| **(C) Counterfactuals, ex-ante estimand** | **IDENTIFIED CONDITIONAL** on coefficient invariance, no equilibrium response and the ex-ante attainment rule. $\kappa$-invariant. |
| **(C) Counterfactuals, realised-bundle estimand** | **IDENTIFIED CONDITIONAL ON A SCALE.** |
| **(A) The conditional law of $A_i$** | **NOT IDENTIFIED**, and not identifiable from choice data under this criterion. |

### 7.1 The unidentified object, its economic meaning, and how $W^1$ depends on it

**The object.** One positive household-specific scalar $\kappa_i$ multiplying the
whole opportunity measure, currently normalised away by $g_i(o)\equiv1$
(equivalently: the arrival intensity of the non-employment option is set to one).

**Its economic meaning.** How *thick* the household's opportunity environment is
in absolute terms — the expected number of job opportunities available, as
against their relative composition. It is the difference between "she is twice as
likely to be offered a full-time as a part-time job" (identified) and "she can
expect nine offers rather than two" (not identified).

**How $W^1$ depends on it.** Summarising §3:

* implemented $W^1$-EA, baseline and all sixteen states: **exactly invariant** —
  $\kappa$ cancels between $J$ and $H$;
* Reading I baseline $W^1$: **irrelevant** — $\Lambda_i(x)\equiv0$ below $m_i(o)$,
  so $W^1=m_i(o)$ for every $\kappa$;
* Reading II $W^{1{\rm -W}}$: **monotone and unbounded** — $\Pr(W^{1{\rm -W}}>x)=e^{-\kappa_i\Lambda_i(x)}$,
  spanning $+\infty$ at $\kappa\to0$ and the market support infimum at $\kappa\to\infty$;
* $W^4$ as a *level*, and any $W^4$-vs-$W^1$ comparison: **scale-dependent**,
  which is exactly the defect the S12 audit found and corrected by unit-mass
  normalisation on $H$'s own domain.

**Calibration sources, if the PI moves to a reading that needs one.** Listed, not
recommended, and not costed: (i) matching the employment margin — the model's
implied $\Pr(\text{at least one market offer})$ against observed non-employment
rates by group, which identifies $\kappa$ only jointly with the reservation
structure; (ii) vacancies-per-jobseeker from the French vacancy statistics,
which measures a market-level ratio and needs an explicit mapping to a
household-level intensity; (iii) external offer-arrival evidence from search
models (Bloemen 2000's covariate-dependent Poisson $\lambda_i=\exp(\theta'z_i)$
is the closest antecedent, and his own conclusion — that once the arrival rate
carries individual characteristics "the parameters of the underlying utility
specification cannot be traced down any more" — is a warning about doing this
*jointly*, not a licence to calibrate freely).

**A transparent sensitivity design, if one is needed.** Fix Reading II, put
$\kappa_i=\kappa\cdot\kappa_i^{\rm base}$ with $\kappa_i^{\rm base}$ the current
normalisation, and report $W^{1{\rm -W}}$, its inequality and the Owen shares on a
grid of $\kappa$ spanning the plausible offer-arrival range end to end — with the
*shares* plotted against $\kappa$, not just the levels, because a share can be
stable while a level is not. Report the grid; choose no point on it.

### 7.2 What is and is not affected

| reported object | affected by the unidentified scale? |
|---|---|
| baseline $W_i$ (as executed, ex ante) | **No** — exactly $\kappa$-invariant (§3.2) |
| baseline inequality of $W_i$ | **No** — a monotone functional of an invariant vector |
| the P/A/B/D counterfactual states $I_S$ | **No**, under the ex-ante estimand |
| the Shapley/Owen decomposition | **No**, for the same reason |
| $W^4$ levels and $W^4/W^1$ | **Yes** — requires unit-mass normalisation on $H$'s domain; already handled |
| the working-only reference domain ($W^{1{\rm -W}}$) | **Yes** — and the level moves by $\times4.29$ at the singles median |
| any statement of the form "she has $N$ job opportunities" | **Yes, entirely** — such a statement is not licensed by this model |

### 7.3 The three declarations this note asks for

1. **The reference domain.** Reading I or Reading II. Not a technical detail: it
   decides whether $W^1$ is latent-set-free, and it moves the singles level by a
   factor of four.
2. **The availability of non-employment.** "$o\in A_i$ for every $i$" is a
   maintained assumption, observationally equivalent to a reading in which it
   fails with probability $e^{-1}$. Adopt it explicitly, in the paper, as a
   modelling restriction.
3. **The attainment estimand.** Realised bundle ($z_i^{\rm obs}$, eq. 1.1) or
   ex-ante inclusive value (as executed). The two are different estimands and
   only the first is Measure 1 as written. Under the second, the sentence "the
   job she has" is wrong and "the jobs she faces" is right.

Nothing else in this note requires a decision. Stop.

---

## Appendix A — sources, paths, hashes

Repository heads at the time of audit: `MNL` `aa36e816e46568ff448810e5b89c28ea616a2476`;
submodule `MNL/dclaborsupply-monorepo` `55bb0d0ea7a1ad2d683f8b2b2a9f7bfb3d5118df`;
`Job_Market_paper` `834055e8da5573ae237f40d38229e836b6717270`.

| object | path | sha256 |
|---|---|---|
| RURO likelihood engine (index, criterion) | `MNL/dclaborsupply-monorepo/packages/dclaborsupply/src/dclaborsupply/likelihood/engine_jax.py` | `681420523f1efb76389c624e437549ee8971184672327d483296862708845983` |
| truncated wage-offer primitives | `…/likelihood/wage_density.py` | `083b5cf5deeae485a270c60fd2b7d6188bf6a72c65aedf9f12d56aa11972a0eb` |
| Stage-D measures ($W^1$ at 283-288, $W^4$ at 289-294, inversion at 405-500) | `MNL/scripts/welfare/m08_welfare_measures.py` | `ccb8a2c9ddece225522201d8b667e69530c8c23c90d3f192c6a2523a19c21335` |
| certified base spec | `MNL/scripts/bpool/specs/estimation_spec_joint_pooled_v1_bll0_tlmpin.yaml` | `492bcfa9c766bfcb5d8536f5e920cc0b00ffa600b7b89db60b250365f331f211` |
| S11 specifications of record (both populations) | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_welfare_specs_of_record_v1.json` | `5fdc88502493ce540b088880eecf049bc268392ff3e8790ffe78a16aa6ddc884` |
| S12 $W^4$ premise audit (the authoritative bridge) | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s12_welfare_record/s12_w4_premise_audit_v1.json` | `3f65e92655363e3522548a19d76afedd946a730afcd6f725efe44d383cc1e142` |
| S12 welfare-record driver ($W^1$/$W^4$/working-only at 338-357) | `…/runs/s12_welfare_record/run_s12_welfare_record_v1.py` | `5ed7a47120e03f0629ce336e06b4bd1376ddd22f86988ce5d9caa2d33958e743` |
| notation authority | `Job_Market_paper/reports/canonical_notation_v5.md` | — |
| welfare section of record | `Job_Market_paper/manuscript/sections/04_welfare_and_decomposition.tex` | — |
| theory source | `Job_Market_paper/Literature/core_papers/haydar_maniquet_2026_wip.md` (extraction of *Jobs and Well-Being Measurement*, Feb 2025) | — |

Key function names: `build_jax_singles_ll`, `build_jax_couples_ll`, `jgroup_logsumexp`,
`_center_proposal`, `_jlog_wage_density`, `jbox_cox` (engine);
`FrozenReferenceCore.R_replace`, `.R_single_node`, `.assert_home_option`,
`compute_measures`, `solve_monotone` (Stage-D); `single_vectors`,
`W1C.measures_consistent` (S12 driver).

Anchors of record used above: singles $n=1{,}540$, negLL 6253.463074379619,
$\beta_c=2.038731824410903$ (SE$_{\rm CR1}$ 0.2917), $\theta_c\equiv0$, $\tau=1$,
52 coordinates / 41 free; couples $n=2{,}223$, negLL 10283.03436935076,
$\beta_c=2.101720268206207$ (SE$_{\rm CR1}$ 0.2939), 47 coordinates, all free;
$\lambda_c$ of record 1938.238719107138 / 4247.875047307145 (welfare panel
1774.5182182328458 / 3821.448012098882 — a units convention, cancelling to
$2.66\times10^{-15}$).

**Numbers derived in this note and not certified:** the four $\min_a\beta_\ell$
values and the $k<41.20$ bound (§1.2), and $\int_5^{70}e^{g^H}dh=109.6096$, the
occupation sums 2.0963 / 4.5428 and $\mathbb E[N^{\rm mkt}]=9.62/20.84$ (§2.3).
All are arithmetic on the S11 parameter table; none involves a rerun.

## Appendix B — literature mapping

| Haydar–Maniquet object | location in the source | counterpart here |
|---|---|---|
| $\mathcal J$, $y:\mathcal J\to\mathbb R_+$, $Z=\mathbb R_+\times\mathcal J$ | §1 | package space $(e,k,h,\omega)$ with base measure $\nu$; $y(j)=\omega h\cdot52/12$; $C_i(j)$ the priced disposable income |
| ability set $A\subseteq\mathcal J$ | §1 | the latent set $A_i$ — **not** the sampled set $\mathcal C_i$, which is a proposal artefact |
| $W(z,R,A;y)$ | §2 | $W^1_i$ in EUR/month |
| **Measure 1**: $z\,I\,\max_R\{B\}$, $B=\{(m,j'):j'\in A\}$ | §3 | eq. (0.1) / (1.1); executed as $W^1$-EA with an ex-ante attained side |
| **Measure 4**: $z\,I\,(m,o)$, $o\in A$ for all $A$ | §3 | `R_single_node`, `m08_welfare_measures.py:289-294`; §1.3 shows Measure 1 $\equiv$ Measure 4 on this domain |
| **Measure 5**: reference ability set $\bar A$ | §3 | `R_abar` / `AbarReference` (implementer's binding, not ratified) |
| **Measure 6**: preferred job over $\mathcal J$ at equal pay | §3 | `R_universal` |
| Job Duplication Invariance; Job Neutrality | §2 | structural axioms; JDI's antecedent fails for wage-differentiated offers (§5) |
| **Independence of $y$** ($W^1$: $+$) | §2, table §3 | the axiom that makes the wage-coordinate convention irrelevant for $W^1$ (§5) |
| Independence of $A$ ($W^1$: $-$; $W^4$: $+$) | table §3 | the domain-restricted collapse of §1.3 does not overturn this; see Theorem 1 |
| Responsibility For Equal Pay ($W^1$: $+$) | §2, table §3 | with Independence of $y$, the pair Haydar–Maniquet conjecture characterises Measure 1 |
| **Theorem 1** (no $W$ with Representation + Ind. of $A$ + Resp. For Equal Pay) | §4 | its construction ($A=\{j_1,j_2\}$, opposed tastes, no home node) is excluded by the subdomain of §1.3 — hence no contradiction |
| Dagsvik–Jia (2016), Capeau–Decoster (2016), Capeau et al. (2015) — Poisson-scattered latent jobs, Fréchet max | project summaries, `JMP_literature/03_summaries/T1A/` | the *source* of the RURO criterion; all three treat opportunities as genuinely stochastic, and the project's own notes record that this paper's stance is deterministic feasible sets with "RO as estimation machinery". §2–§3 show that stance is a **reading**, not a model restriction, and that it is the reading under which $\kappa$ has no meaning to lose |
| Bloemen (2000) — $\lambda_i=\exp(\theta'z_i)$ Poisson offer count | `JMP_literature/03_summaries/T1A/Bloemen_2000_job_offer_restrictions.md` | the calibration antecedent of §7.1(iii), and its warning about joint identification of utility and arrival rate |
