# Canonical notation v1

**Authority: `manuscript/JMP_working_paper_for_seminar_v2.md` (R-268.1).** Where any
other artifact — the research-story HTML, the seminar deck, the research-lab
notebook — writes a model symbol or names a factor, it writes the symbol and the
name below, unchanged. This file exists so that "match the paper" is a checkable
instruction rather than an invitation to paraphrase.

Written to close item 1 of `reports/consistency_gate_v1.md`, which found three
different factorisations in circulation: the paper's four factors, an HTML that
separated a fifth `g^Acc` term, and notebook Markdown that collapsed the market
margins into `g^{market}`.

---

## 1. The two objects, and the rule that keeps them apart

The specification carries exactly two estimated objects. Every coefficient
belongs to one of them, and no artifact may blur which.

| object | symbol | what it says |
|---|---|---|
| utility | $u_{ij}$ | how household $i$ **ranks** package $j$ |
| opportunity density | $g_{ij}$ | how **available** package $j$ is to household $i$ |

A third object, the proposal density $q_{ij}$, is **computation, not economics**:
it is the importance-sampling density the alternatives were drawn from, is not
estimated, carries no parameter of interest, and cancels from the estimand. It is
never called an opportunity, an offer, or an availability.

## 2. Utility

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
+\mathbb{1}\{g=\text{women}\}\,\beta_{\ell k}^{g}k_i .
$$

With $\tilde{\ell}_{ij}=(\bar L-h_{ij})/\lambda_{\ell}$,
$\tilde{c}_{ij}=c_{ij}/\lambda_c$, $a_i$ age centred and scaled by ten, $k_i$ the
number of children, $\beta_c\equiv 1$ the scale numeraire, and
$\lambda_{\ell}=10$ hours. $\theta_c$ is shared across the sexes;
$\theta_{\ell}^{g}$ is not.

## 3. The opportunity density — FOUR factors, not five

$$
g_{ij}\;=\;g^{E}_{ij}\cdot g^{H}_{ij}\cdot g^{\mathrm{Occ}}_{ij}\cdot g^{W}_{ij}
$$

Each factor equals one at its own reference; the last three are switched off on
the non-employment package, $E_{ij}=\mathbb{1}\{h_{ij}>0\}$.

| symbol | audience-facing name | contents |
|---|---|---|
| $g^{E}$ | **access** (job access) | a level shift on every working package: the group-specific unemployment rate, region of residence, urbanisation |
| $g^{H}$ | **hours** | a step density over five bands; the statutory 35-hour band is the reference, $\beta_{\mathrm{F35}}\equiv 0$ |
| $g^{\mathrm{Occ}}$ | **occupation** | four categories, the first omitted, separate offer weights by sex, $\beta^{\mathrm{occ}}_{1,g}\equiv 0$ |
| $g^{W}$ | **wage offer** | occupation-conditional log-normal offer density (a Mincer equation carried *inside* the opportunity set) |

**There is no `g^{Acc}` factor and there is no `g^{market}` factor.** Local-market
access lives **inside `g^E`** — that is what its regional and unemployment-rate
terms are. Writing `g^{Acc}` alongside `g^E` assembles a five-term product the
model does not have; collapsing $g^{\mathrm{Occ}}$ and $g^{W}$ into `g^{market}`
hides the two factors the decomposition attributes separately.

Component forms, verbatim from the paper:

$$
\log g^{E}_{ij}=E_{ij}\Bigl[\beta_{E}+\beta_{s}\tilde{s}_i
+\textstyle\sum_{r=2}^{8}\beta_{r}\mathbb{1}\{R_i=r\}
+\beta_{u}U_i+\beta_{m}M_i\Bigr]
$$

$$
\log g^{H}_{ij}=\sum_{b}\beta_{b}\,\mathbb{1}\{h_{ij}\in B_b\},
\qquad \beta_{\mathrm{F35}}\equiv 0
$$

$$
\log g^{\mathrm{Occ}}_{ij}=E_{ij}\sum_{k=2}^{4}\beta^{\mathrm{occ}}_{k,g}
\mathbb{1}\{o_{ij}=k\}, \qquad \beta^{\mathrm{occ}}_{1,g}\equiv 0
$$

$$
\log g^{W}_{ij}=E_{ij}\Bigl[-\tfrac12\Bigl(\tfrac{\log w_{ij}-\mu_i}{\sigma}\Bigr)^{2}
-\log\sigma-\tfrac12\log 2\pi-\log w_{ij}\Bigr],
\qquad
\mu_i=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i+\beta_{wx^{2}}x_i^{2}
$$

## 4. The index and the estimator

$$
V_{ij}(\theta)=\underbrace{u_{ij}(\theta)}_{\text{tastes}}
+\underbrace{\log g_{ij}(\theta)}_{\text{availability}}
-\underbrace{\log q_{ij}}_{\text{proposal correction}},
\qquad
q_{ij}=q^{E}_{ij}\bigl(q^{H}_{ij}q^{W}_{ij}q^{\mathrm{Occ}}_{ij}\bigr)^{E_{ij}}
$$

$$
\hat{\theta}=\arg\max_{\theta}\sum_{i=1}^{N}
\Bigl[V_{i\,j^{*}_i}(\theta)-\log\!\!\sum_{j\in\mathcal{C}_i}\!\exp V_{ij}(\theta)\Bigr]
$$

Each household carries its observed package plus $R=100$ drawn alternatives, so
$|\mathcal{C}_i|=101$.

## 5. The welfare measure $W^1$ — the three clauses, all required

$W^1_i$ is the **uniform pay** that, offered at every job in household $i$'s **own
opportunity distribution**, reproduces the expected welfare it actually attains.
Three clauses travel with it and none is optional:

1. it **neutralises pay differences within the reachable set**;
2. **differences in the set itself remain**, and are what the decomposition
   attributes;
3. the inversion uses the **same coalition's set and preferences on both sides**.

$W^1$ is *not* "income at a common reference leisure". The phrase **reference
leisure** describes a different object — the alternative couples measure of
Appendix D.3, which really does pin both spouses at 35 hours — and must not be
used for $W^1$ anywhere.

## 6. Decomposition symbols

| symbol | name |
|---|---|
| $I^{00}$ | baseline inequality: own preferences, own environment |
| $I^{10}$ | preferences equalised to the reference block |
| $I^{01}$ | environment equalised (access, earning opportunities and endowments/needs together) |
| $I^{11}$ | both equalised — the exhaustiveness test, which must be zero |
| $C_{\mathrm{pref}}$ | contribution attributed to preferences |
| $C_{\mathrm{env}}$ | contribution attributed to the complete non-preference environment |
| $C_{\mathrm{acc}}$, $C_{\mathrm{earn}}$, $C_{\mathrm{needs}}$ | the three nested environment channels |

Couples use the four-digit state names $I^{0000}$, $I^{1000}$, $I^{0111}$,
$I^{1111}$ on the same convention.

**Never write `C_P`, `C_E`, `C_A`, `C_B`, `C_D` in audience-facing text.** Those
are internal column stems of the estimation tables; the reader-facing names are
the subscripted forms above.

## 7. Wording that travels with the symbols

- A contribution is a **Shapley/Owen value — an average over the orders** in which
  channels are equalised. It is **attributed to** a channel, or the channel
  **accounts for** it. It never "removes" a share.
- **"Reduces" is reserved for the one-factor counterfactual**: equalising the
  environment alone *reduces* inequality by 77 per cent ($I^{00}\to I^{01}$);
  equalising preferences alone *raises* it by 10 per cent ($I^{00}\to I^{10}$).
  The Shapley attribution averages the two orders and returns 93.7 / 6.3.
- The two reference conventions are the **female-primary** reference and the
  **male structural-zero** sensitivity. They are reported as a pair and
  **never averaged**.
- Integration bands (RQMC, eight scrambles) and CR1 parameter intervals are two
  different objects and are **never merged**.
