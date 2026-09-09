# Canonical notation, v5

This supersedes `canonical_notation_v1.md` and §1.1 and §1.4 of
`consistency_gate_spec_v1.md` **where, and only where, the model changed**.
Everything else in that specification — the forbidden symbol variants, the
four-factor rule, the $W^1$ statement clauses, the reference labels, the
coverage rules, the nested semantics and the forbidden-term table — is carried
forward unchanged and is enforced by `run_v5_gate.py`.

## Why an amendment was needed

The v1 notation canon was written against the specification in force at the
time. Two of its clauses assert facts about that specification which the S11
specifications of record contradict. Enforcing them against v5 would fail the
paper for describing the model it actually estimates.

| v1 clause | v1 statement | S11 specification of record | Disposition |
|---|---|---|---|
| §1.1, utility block | $\beta_c\equiv 1$ (scale numeraire) | $\beta_c$ is **estimated**: 2.0387 (singles), 2.1017 (couples) | **Superseded.** $\beta_c$ is a free coordinate. |
| §1.1, utility block | $\theta_c$ shared across sexes, estimated | $\theta_c\equiv 0$ exactly, both populations | **Superseded.** The consumption term is $\beta_c\log\tilde c_{ij}$. |
| §1.4, the F35 rule | $\beta_{\mathrm{F35}}\equiv 0$ as a band step, with a separately estimated 35-hour peak over and above four band coefficients | $g^{H}$ has **five** band coefficients over one residual reference set of total width 26.5 hours per week; `beta_h_f35` is the coefficient on the band $[33.5,36.5)$, not a peak added to a normalized band | **Superseded.** The five-band statement replaces it. |

No other clause of the v1 specification is amended. In particular the
`beta_ll` rule, the RUM-block rule, the geographic and sex rules and the whole
forbidden-term table stand.

## The canon, v5

### The three objects

| symbol | name | note |
|---|---|---|
| $u_{ij}$ | utility | how $i$ **ranks** package $j$ |
| $g_{ij}$ | opportunity density | how **available** $j$ is to $i$ |
| $q_{ij}$ | proposal density | **computation, not economics**; never called an opportunity, an offer or an availability |

### Utility block

$$u_{ij}=\beta_{\ell}^{g}(\mathbf x_i)\,\mathcal B(\tilde\ell_{ij};\theta_{\ell}^{g})+\beta_c\log\tilde c_{ij},\qquad \mathcal B(z;\theta)=(z^{\theta}-1)/\theta,\quad\mathcal B(z;0)=\log z,$$

$$\beta_{\ell}^{g}(\mathbf x_i)=\beta_{\ell 0}^{g}+\beta_{\ell a}^{g}a_i+\beta_{\ell a^{2}}^{g}a_i^{2}+\mathbb 1\{g=\text{women}\}\beta_{\ell k}^{g}k_i .$$

Symbols: $\tilde\ell_{ij}=(\bar L-h_{ij})/\lambda_\ell$ with $\bar L=80$ hours
and $\lambda_\ell=10$ hours; $\tilde c_{ij}=C_{ij}/\lambda_c$; $a_i$ age,
centred and scaled by ten; $k_i$ the child count.

**$\theta_c\equiv 0$** in both populations, exactly, so the consumption term is
$\beta_c\log\tilde c_{ij}$ and $\partial u/\partial C=\beta_c/C$.

**$\beta_c$ is estimated**, common within a population, and is simultaneously
the coefficient on log consumption and the **order of the power mean** the
money metric is. It is *not* the consumption curvature and *not* an
across-household inequality-aversion parameter.

$\lambda_c$ is a units convention: under $\theta_c=0$ it enters as the
alternative-invariant constant $-\beta_c\log\lambda_c$ and cancels from every
choice probability and exactly from $W^1$. The constant **of record** is the one
carried by the estimation frame: 1938.238719 (singles), 4247.875047 (couples).

The random-utility shock is i.i.d. type-I extreme value with scale $\tau=1$.

### Opportunity block — four factors

$$g_{ij}=g^{E}_{ij}\cdot\left(g^{H}_{ij}\,g^{\mathrm{Occ}}_{ij}\,g^{W}_{ij}\right)^{E_{ij}},\qquad E_{ij}=\mathbb 1\{h_{ij}>0\}.$$

| symbol | audience-facing name | coefficients |
|---|---|---|
| $g^{E}$ | **access** (job access) — *local-market access lives inside it* | $\beta_E,\beta_s,\beta_r\,(r=2..8),\beta_u,\beta_m$ |
| $g^{H}$ | **hours** | five band coefficients over one residual reference set |
| $g^{\mathrm{Occ}}$ | **occupation** | $\beta^{\mathrm{occ}}_{k,g}$ with $\beta^{\mathrm{occ}}_{1,g}\equiv 0$ |
| $g^{W}$ | **wage offer** | $\mu_i,\sigma,\delta_{\mathrm{occ}}$, truncated to $[2,590]$ EUR/hour and renormalized on that support |

**The five-band rule (replaces §1.4).** $g^{H}$ elevates five bands —
$[17.5,21.5)$, $[28.5,30.5)$, $[33.5,36.5)$, $[36.5,40.5]$ and $[44.5,70]$ —
over the residual set $[5,17.5)\cup[21.5,28.5)\cup[30.5,33.5)\cup(40.5,44.5)$ of
total width 26.5 hours per week. The reference is that residual set. **No band
coefficient is normalized to zero**, and `beta_h_f35` is the coefficient on the
band $[33.5,36.5)$. Any passage describing the 35-hour feature states it as a
density elevation over an interval and never as an atom at 35 hours, and never
as a peak added on top of a normalized band.

### Index and estimator

$$V_{ij}=u_{ij}+\log g_{ij}-\log q_{ij},\qquad q_{ij}=q^{E}_{ij}\left(q^{H}_{ij}q^{W}_{ij}q^{\mathrm{Occ}}_{ij}\right)^{E_{ij}},$$

with $\mathcal C_i$ the sampled set, $|\mathcal C_i|=101$ ($R=100$ draws plus the
observed package), multiplicities retained in the numerator and the denominator
taken over slots.

### Welfare

$W^1$ is the carrier. Under $\theta_c=0$,

$$W^{1}_{i,S}=\lambda_c\exp\!\left[\frac{\log J_{i,S}-\log H_{i,S}}{\beta_c}\right]=\left[\int C_{i,S}^{\beta_c}\,r_{i,S}(dj)\right]^{1/\beta_c},$$

a weighted power mean of order $\beta_c$, arithmetic **only** at $\beta_c=1$.
$W^4$ is the compensation-side comparison, publishable only with the unit-mass
normalization of the kernel on exactly the domain $H$ uses. $W^3$ is a
single-adult diagnostic.

### Decomposition

$X_i=(P_i,A_i,B_i,D_i)$; operators $T_P,T_A,T_B,T_D$ applied as one
**simultaneous substitution map**, never as an ordered product; $X^S=T_S(X)$;
$I_S=\mathcal I\{W_i(T_SX)\}$; $v(S)=I_\varnothing-I_S$. States
$I^{00},I^{10},I^{01},I^{11}$. Audience-facing component names: **preferences**,
**job access**, **earning opportunities**, **resources and needs**, with the
subdivision of the last into **non-labour resources** and **household
composition and needs**.

A Shapley or Owen share is **attributed to** a factor. The verb *reduces* is
reserved for the one-factor counterfactual, and *removes* is never used for a
share.
