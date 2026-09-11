<!-- NORMATIVE NOTE — W1 REFERENCE-DOMAIN FORK -->

# W1 reference-domain fork: full feasible set (F) versus market-job reference (M)

**Status.** Read-only theory and source audit answering the PI/deputy ruling
"W1 REFERENCE-DOMAIN FORK". No code, no rerun, no re-estimation, no welfare or
decomposition run, no set-size normalisation, no repair of W1-EA. Every number
below is either (i) read from a certified record (path and digest in Appendix A),
or (ii) arithmetic performed *in this note* on the S11 parameter tables, labelled
**[derived here]**. That arithmetic used a throwaway calculator: nothing was saved
and no project code was written.

**Citability: CITABLE.** Every [derived here] numeral — including 0.850, 12.1×,
"1–5%", the Table 1 factors and the couples threshold 4.278 — is reproduced by
`docs/normative/scripts/fork_derived_numerals_v1.py` (sha256
`994c3dfaad7cbafd2f76871ac05629e0ee60947b5a00085f944a0bebe11d8e9c`) against
`docs/normative/fork_derived_numerals_v1.csv` (sha256
`2677356a555ec3eb65623227e3d26363925c2d11add1112c8db925213f77bf8e`), reading only
the accepted S11 parameter tables and the named reference households, at the
memo's printed precision: **158/158 pass, script exit 0**. REC-1 / Deputy R3
item 2 is closed. Appendix B lists them.

**P1 (couples parameter-table provenance): RESOLVED.** S11 is the accepted
baseline for both singles and couples, per dashboard entries R-286 ("the
preference-figure family is regenerated at the final parameters") and R-291
("ONE MODEL, EVERYWHERE … the reported specification is the S11 record").
`experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv`
(2,275-couple frame) is **provisional**, not accepted, and was used only by the
non-accepted MEASURE-MAP-1 return. Every couples numeral in this memo uses the
S11 table; §5.1's threshold 4.278 and R240's 5.52 are not the same claim about
the same accepted object, and the fork's figures stand.

**Status of the conclusions: PENDING RULING.** Verdicts B and C, the
recommendation (F), and the amendments to the note are proposals to the PI and
deputy, not rulings. The numerals above are citable; the normative conclusions
they support are not yet ruled on.

**Builds on** `docs/normative/W1_latent_set_identification_note_v1.md` (hereafter
**"the note"**). Its equations are cited as (0.1), (1.1) and so on, and its findings
as "note F1b" and so on. They are not re-derived here. §3.1 and §1.3 amend four
of the note's secondary statements; its Mapping-F result stands.

**Revision log.** All three passes are on 2026-09-11. The first pass was never
committed and is recoverable only from this log.

| pass | trigger | what changed |
|---|---|---|
| **r0 — first pass** | original FORK-1 ruling header | Caught the header's reversed nonworker sign. Verdict **B**, or C if $o$ is a job. Dense-law finding: $A^M$ non-empty almost surely, $\kappa$ irrelevant, M ≈ F × 1.01–1.05. **Recommendation: M**, evaluated under the dense law as the closed form (M.4), with the law-free band. Rationale: (1) the manuscript and the co-author's example read $A$ as market jobs; (2) F makes $W^1\equiv W^4$; (3) under the dense law M has no $\kappa$ and no empty set; (4) the gap to F is small. Empty-set treatments T1–T4, with the $+\infty$ convention inside T4 |
| **r1 — revised header** | the **PI** replaced header items 2 and 5 and **added item 7, a prior the PI introduced**: that the $\kappa\to\infty$ limit is an Independence-of-$A$ object, so M's access channel lives only at finite $\kappa$ | Pointwise check and the worker upper-bound qualifier (§1.2); treatment (e) analysed separately, with a finite ceiling and a jump at $\emptyset$ (§3.4); §4.4 added. Verifying the PI's prior, this note sharpened it: the $\kappa\to\infty$ limit is exactly **Measure 6 over market jobs**. That disposes of r0's rationales (1) and (2): (1) is delivered only at unidentified finite $\kappa$, and (2) is symmetric ($W^1\equiv W^6$). **Recommendation flipped M → F.** The flip follows from the PI's prior, as verified here; it was not reached independently in r0 |
| **r2 — closing items** | PI review of r1 | Couples reference configuration explained term by term; man-only becomes the reference in a narrow region (§5.1). Memo-grade label on derived numerals. Theory identities separated from implemented objects, including $W^4$ (§6.1). This log. Co-author source named (§2.8). Committed; hash recorded outside the file |
| **r3 — REC-1 numeral correction** | REC-1 (Deputy R3 item 2): `docs/normative/scripts/fork_derived_numerals_v1.py` reproduced 154/158 Table 1 numerals; four cells were off beyond the memo's printed rounding | **Cause: double rounding in the first pass** — the calculator's output was rounded to 4 decimals and then again to 3 for the table. **Source: `fork_derived_numerals_v1.csv`.** Four Table 1 cells corrected to the script's values: single men, minimum weight, $\rho(50)$ 0.737→**0.736**; single men, age 20, nonworker-band lower end 1.011→**1.010**; single women, age 20, $\rho(50)$ 0.305→**0.304**; single women, age 60, nonworker-band lower end 1.044→**1.043**. Nothing else in the memo changed. Script now exits 0, 158/158 passing; numerals promoted to CITABLE (§0 status block) |

The revised header items are reproduced verbatim in Appendix C.

**Theory source.** `Theory_other_project/jobs_and_wellbeing.tex` (authoritative;
cited as **tex l.N**) and the theorem index `jobs_and_wellbeing.agent.md`.

**Notation** (deputy's; the symbol `w` is not used for anything):

| symbol | meaning |
|---|---|
| $\omega$ | hourly wage |
| $C_i$, $C_i^{\rm obs}$ | disposable income (consumption resource); its observed value |
| $m_i(j)$ | equivalent consumption at reference job $j$: $u_i(m_i(j),j)=u_i(z_i^{\rm obs})$ |
| $W_i^1$ | money-metric well-being, $\min_{j\in A_i}m_i(j)$ |
| $L_i(j)$ | non-consumption index. Hours-only: $\beta_\ell^g(\mathbf x_i)\,\mathcal B((80-h_j)/10;\theta_\ell^g)$, additive across spouses (note §1.2, §5) |
| $o$ | non-employment; for couples the joint point $(o,o)$ ("NN") |
| $A_i^M$ | market reference set: singles, $E=1$; couples, at least one spouse employed |
| $A_i^+$ | full feasible set $A_i^M\cup\{o\}$ (couples: $\cup\{(o,o)\}$) |
| $\bar L_i^{\rm mkt},\ \underline L_i^{\rm mkt}$ | sup and inf of $L_i$ over the **support** of the market offer measure |
| $x$ | a flat consumption level (the manuscript's "$w$" in Measure 1, renamed) |
| $\mathbf y^{[x]}$ | the equal-pay profile $\mathbf y^{[x]}(j)=x$ (the manuscript's $\mathbf y^w$) |
| $\kappa_i$ | the household-specific common opportunity-intensity factor (note §2.2) |
| $G(s)=e^{-e^{-s}}$ | standard Gumbel cdf |

Under the specifications of record, $\theta_c\equiv0$, $\tau=1$, $\beta_c$ is
estimated (2.0387 singles, 2.1017 couples), and the hours offer support is
$[5,70]$ h/week (record: `spec_conventions.h_min = 5.0, h_max = 70.0`).

---

## 0. Header priors: verified, not assumed

| # | prior stated in the ruling header | verdict | where |
|---|---|---|---|
| 1 | Under F, $W^1=m_i(o)$ for all $i$; $\kappa$ irrelevant; W1-EA $\kappa$-invariant in all 16 states | **Accepted as proved** (note (1.1), F1b, F3, §3.2). One premise is **strengthened**: under the construction on which the executed criterion is exact, $o\in A_i$ holds almost surely, not by assumption (§3.1) | §1.1 |
| 2a | Worker under M: $W_M^1=C^{\rm obs}\exp\{[L(j^{\rm obs})-\max_{A^M}L]/\beta_c\}\le C^{\rm obs}$, equality iff $j^{\rm obs}$ is $L$-best in $A^M$ | **Verified** | §1.2 |
| 2b | Nonworker under M: $W_M^1<C^{\rm obs}$ whenever $A^M\neq\emptyset$ | **REVERSED.** $W_M^1>C^{\rm obs}$ **strictly**, for every non-empty $A^M$ and every parameter value in the estimated domain | §1.2 |
| 2c | Nonworker: undefined when $A^M=\emptyset$ | **Verified** (a minimum over the empty set) | §1.2, §3 |
| 2d | Finite lower bound $W_M^1\ge C^{\rm obs}\exp\{[L(j^{\rm obs})-\bar L^{\rm mkt}]/\beta_c\}$; scale dependence bounded | **Verified**, and complemented by an **upper** bound. The bound is sharp and needs no $\kappa$ and no set law. Values are in Table 1. The unboundedness in note F3 (Reading II) comes **only** from the empty event | §1.2 |
| 2e (rev.) | Pointwise check: $A^M\subset A^M\cup\{o\}$ ⇒ $W^1_M\ge W^1_F$ for every household | **Verified, and strict:** $W^1_M/W^1_F=e^{[L(o)-\max_{A^M}L]/\beta_c}>1$ because $\max_{A^M}L\le\bar L^{\rm mkt}<L(o)$. Every number reported here passes the check (list in §1.2) | §1.2 |
| 2f (rev.) | Upper bound: "a singleton set at the lowest-$L$ market job" | **Verified for nonworkers** ($A^M=\{70\text{ h job}\}$). **For workers, that singleton is inadmissible** unless it is $j^{\rm obs}$, because observed employment puts $j^{\rm obs}$ in $A^M$. The admissible worker upper bound is $A^M=\{j^{\rm obs}\}$, i.e. $C^{\rm obs}$ | §1.2 |
| 5(e) (rev.) | $\min\emptyset=+\infty$: a nonworker's $W^1_M$ "rises without bound as the market set thins" | **Refined.** On non-empty sets, thinning raises $W^1_M$ monotonically but only up to a **finite ceiling** $C^{\rm obs}e^{[L(o)-L(70)]/\beta_c}$ (12.1× at the reference single man). The ceiling is finite only because of the maintained 70 h support cap. The $+\infty$ is a **jump at $\emptyset$**, not a continuous rise. In distribution, $W^1_M\to+\infty$ in probability for nonworkers as $\kappa\to0$ | §3.4(e) |
| 7 (rev.) | Intensity limits | **Verified with one sharpening.** $\kappa\to\infty$ gives the closed form (M.4), identified given the maintained support endpoint, with **no** direct access dispersion. It is exactly **Measure 6 over the market-job universe**, an Independence-of-$A$ object: M's analogue of F's collapse into $W^4$. $\kappa\to0$ gives $C^{\rm obs}$ for workers and $\emptyset$ for nonworkers. The model cannot say whether $\kappa$ is common or household-specific | §4.4 |
| prelim. | PI's preliminary reading of `The_draft_theorypaper.tex`: verdict B, conditional on $A^M\neq\emptyset$ | **Confirmed against the authoritative source**, with one qualifier: B holds iff staying home is not a job in the ability set; otherwise C (RFEP fails, §2.3) | §2.6 |
| 3 | Co-author example consistent with M, inconsistent with F | **Consistent with M** (it is the worker equality case). Inconsistent with F **only on the estimated preference domain** (note F1b), not in the abstract theory. The primary text was not located; the assessment rests on the header's description | §2.8 |
| 4 | Trace Representation / RFEP / Independence of $\mathbf y$ | Done. **Verdict B** under the manuscript's default job universe; C if $o$ is treated as a job in the ability set | §2 |
| 5 | $\Pr(A^M=\emptyset)$ under the note's foundation | **0** under the law the executed criterion implies. It is **positive and $\kappa$-dependent** only under an added finite-count hypothesis | §3 |
| 6 | No 100 alternatives / 2,048 nodes / kernel masses as counts; no code | Complied | — |

---

## 1. Audit of the two mappings

### 1.1 Mapping F: full feasible set

From note (0.1) with $\arg\max_{A_i^+}L_i=o$ (note F1b: $\beta_\ell^g(\mathbf x)>0$ on the
whole covariate domain, $\mathcal B'>0$, no cross-leisure term for couples):

$$W_{i,F}^1=m_i(o)=C_i^{\rm obs}\exp\!\Big[\tfrac{L_i(j_i^{\rm obs})-L_i(o)}{\beta_c}\Big]\qquad\text{(note (1.1)); couples: }o\to(o,o).$$

**Direct dependence on latent market opportunities that disappears, all of it.**
Nothing from the market part of $A_i$ enters baseline $W^1_F$. That includes:
the opportunity composition $g_i$ (hours elevations, the occupation table, the
wage-offer density), the market-intensity index ($\beta_E$ and the market
shifters), the common scale $\kappa_i$, the set law (Poisson or otherwise), any
set size, and whether $A_i^M$ is empty. $A_i$ enters only through the statement
"$o\in A_i$".

**Indirect dependence through attainment that remains.**
(i) *Baseline:* $j_i^{\rm obs}$ and $C_i^{\rm obs}$ were produced by choice from
$A_i$, but they are data. No latent object is needed to compute $W^1_F$.
(ii) *Counterfactuals:* the operators move the attained bundle. Under the
realised-bundle estimand it must be re-selected from $A_i\mid y$, which needs
$\kappa_i$ and a shock rule (note §4.2, §6C). Under the ex-ante estimand it is
$\kappa$-invariant (note §3.2). Access therefore reaches $W^1_F$ **only** through
where households end up.

**Consequence to keep in view.** At $z^{\rm obs}$, $W^1_F\equiv W^4$ for every
household (note §1.3). Under F, reporting "$W^1$" and "$W^4$" at the observed
bundle reports one object twice.

### 1.2 Mapping M: market-job reference

The derivation of note (0.1) uses only $\bar V_i=u_i(z_i^{\rm obs})$ and never the
convention that $z$'s job lies in $A$. It therefore applies verbatim with
$A=A_i^M$, for workers and nonworkers alike:

$$\boxed{\;W_{i,M}^1=C_i^{\rm obs}\exp\!\Big[\tfrac{L_i(j_i^{\rm obs})-\max_{j\in A_i^M}L_i(j)}{\beta_c}\Big]\;}\tag{M.1}$$

When $A_i^M$ is infinite (§3.1), read "max" as "sup" and $W^1_{i,M}$ as the
infimum of $m_i$ over $A_i^M$.

**Workers (verified).** $j^{\rm obs}\in A^M$, so $\max_{A^M}L\ge L(j^{\rm obs})$ and
$W^1_M\le C^{\rm obs}$. Equality holds iff $j^{\rm obs}$ is $L$-best in the realised
$A^M$. Because $L$ depends on hours only and is strictly increasing in leisure,
that is **iff $A^M$ contains no job with fewer weekly hours than $j^{\rm obs}$**.
Occupation and wage are irrelevant (note §5). For couples it holds iff no
configuration in $A^M$ has a higher joint $L$.

**Nonworkers (the header's inequality is reversed).** $z^{\rm obs}=(C^{\rm obs},o)$ with
$o\notin A^M$. By note F1b, $L(o)>L(j)$ for every market $j$ (strictly, since market
hours are at least 5). Hence $\max_{A^M}L<L(o)$ and

$$W^1_{i,M}=C_i^{\rm obs}\exp\!\Big[\tfrac{L_i(o)-\max_{A_i^M}L_i}{\beta_c}\Big]\;>\;C_i^{\rm obs}\qquad\text{whenever }A_i^M\neq\emptyset .$$

Economically: to be as well off at her best market job as she is at home with
$C^{\rm obs}$, a nonworker needs **more** than $C^{\rm obs}$, because the market job
costs leisure. The "$<$" in the header cannot hold at any parameter value in the
estimated domain. The expression is undefined when $A^M=\emptyset$ (§3).

**Sharp, law-free bounds.** Let $\bar L^{\rm mkt}$ and $\underline L^{\rm mkt}$ be
the sup and inf of $L$ over the support of the market offer measure.
- **Singles:** $\bar L^{\rm mkt}=L(h{=}5)$ and $\underline L^{\rm mkt}=L(h{=}70)$.
- **Couples:** additivity and the absence of a cross term give
  $\bar L^{\rm mkt}=\max\{L^m(0)+L^f(5),\,L^m(5)+L^f(0)\}$, the better
  single-earner 5-hour configuration.

For every set law and every $\kappa$:

$$\text{workers: }\;C^{\rm obs}e^{[L(j^{\rm obs})-\bar L^{\rm mkt}]/\beta_c}\;\le\;W^1_M\;\le\;C^{\rm obs},\tag{M.2}$$
$$\text{nonworkers, }A^M\ne\emptyset:\;C^{\rm obs}e^{[L(o)-\bar L^{\rm mkt}]/\beta_c}\;\le\;W^1_M\;\le\;C^{\rm obs}e^{[L(o)-\underline L^{\rm mkt}]/\beta_c}.\tag{M.3}$$

Each end is attained by an admissible set:
- The **lower** end: a set whose hours reach down to 5 (attained in the closure).
- The worker **upper** end: $A^M=\{j^{\rm obs}\}$. A singleton at the lowest-$L$
  market job (70 h) would give $C^{\rm obs}e^{[L(j^{\rm obs})-L(70)]/\beta_c}>C^{\rm obs}$,
  but it is inadmissible for a worker unless $j^{\rm obs}$ is that job, because
  observed employment puts $j^{\rm obs}$ in $A^M$.
- The nonworker **upper** end: $A^M=\{\text{a 70-hour job}\}$.

The data (a choice from $A^M$) are consistent with each of these sets, so the
bounds are the identified set when no set law is imposed. **The scale dependence
under M is bounded. It becomes unbounded only through the empty event.**

**Table 1 — bound factors from the estimated leisure block and hours support [derived here].**
- Worker lower-bound factor: $\rho(h)=\exp\{[L(h)-L(5)]/\beta_c\}$.
- Dense-law M/F gap: $\exp\{[L(o)-L(5)]/\beta_c\}$.
- Nonworker band: (M.3) divided by $C^{\rm obs}$.
- $\beta_\ell(\mathbf x)$ is evaluated at: the block minimum (note §1.2); the certified
  reference household (`pff_step1_reference_v1.json`, field `omega_at_reference`,
  which there denotes the leisure weight, not a wage); and the singles age-support
  endpoints 20 and 60 (same record, age centre 42.72, decades, $k=0$).

| block | $\beta_\ell(\mathbf x)$ case | $\beta_\ell$ | $\rho(20)$ | $\rho(35)$ | $\rho(39)$ | $\rho(50)$ | M/F gap (dense) | nonworker band |
|---|---|---:|---:|---:|---:|---:|---:|---|
| single men | minimum (age 33.2) | 7.814 | 0.962 | 0.891 | 0.862 | 0.736 | 1.0089 | [1.009, 9.75] |
| | reference HH (age 43, 39 h) | 8.562 | 0.958 | 0.881 | **0.850** | 0.715 | 1.0098 | [1.010, 12.1] |
| | age 20 | 9.171 | 0.955 | 0.874 | 0.840 | 0.698 | 1.0105 | [1.010, 14.5] |
| | age 60 | 13.403 | 0.935 | 0.821 | 0.775 | 0.592 | 1.0153 | [1.015, 49.7] |
| single women | minimum ($k=0$, age 42.4) | 5.867 | 0.896 | 0.748 | 0.698 | 0.527 | 1.0282 | [1.028, 14.2] |
| | reference HH (age 41, 1 child, 35 h) | 6.053 | 0.893 | **0.741** | 0.690 | 0.516 | 1.0291 | [1.029, 15.4] |
| | age 20 ($k=0$) | 10.878 | 0.815 | 0.584 | 0.513 | 0.304 | 1.0529 | [1.053, 137] |
| | age 60 ($k=0$) | 8.970 | 0.845 | 0.642 | 0.577 | 0.375 | 1.0435 | [1.043, 57.7] |

Box-Cox values used: single men $\theta_\ell=-1.6263$, $\mathcal B(8)=0.594005$,
$\mathcal B(7.5)=0.591693$; single women $\theta_\ell=-0.9274$, $\mathcal B(8)=0.921565$,
$\mathcal B(7.5)=0.911895$. The factors are household-specific through
$\beta_\ell(\mathbf x_i)$ and $h^{\rm obs}$. A larger $\beta_\ell$ widens the band.

**The three reference households [derived here].**

| household | $W^1_F/C^{\rm obs}$ | $W^1_M/C^{\rm obs}$: law-free band | $W^1_M/C^{\rm obs}$: dense law (§4) | EUR/month, $C^{\rm obs}$ of record |
|---|---:|---|---:|---|
| single man, 43, 39 h | 0.8415 | [0.8498, 1.0000] | 0.8498 | F 1,589; M ∈ [1,605, 1,889] |
| single woman, 41, 1 child, 35 h | 0.7203 | [0.7412, 1.0000] | 0.7412 | F 1,339; M ∈ [1,378, 1,859] |
| couple, 38/37, 3 children, 39 h / 35 h | 0.6587 | [0.6670, 0.7868] with free disposal; [0.6670, 1] without | 0.6670 | F 2,769; M ∈ [2,804, 3,308] (free disposal) |

So for the reference single man, no set law and no value of $\kappa$ can move
$W^1_M$ by more than a factor of $1/0.8498=1.18$.

**Pointwise check (revised item 2).** A minimum over the subset $A^M$ of
$A^M\cup\{o\}$ is weakly larger, so $W^1_M\ge W^1_F$ for every household. Here the
inequality is **strict**: $W^1_M/W^1_F=e^{[L(o)-\max_{A^M}L]/\beta_c}$, and
$\max_{A^M}L\le\bar L^{\rm mkt}<L(o)$ because market hours are at least 5. Every
figure in this note satisfies it:
- Reference households, F versus the M lower end: 0.8415 < 0.8498; 0.7203 < 0.7412;
  0.6587 < 0.6670.
- Man-only couple: 0.7868 < 0.7967.
- Nonworkers: $W^1_F=C^{\rm obs}<W^1_M$.
- Every Table 1 M/F gap exceeds 1.

**Comparison with F.**
- Workers: $W^1_M/W^1_F=\exp\{[L(o)-\max_{A^M}L]/\beta_c\}$, which lies in
  $[e^{[L(o)-\bar L^{\rm mkt}]/\beta_c},\,e^{[L(o)-L(j^{\rm obs})]/\beta_c}]$.
  For the reference single man that is $[1.010, 1.188]$.
- Nonworkers: $W^1_M/W^1_F=W^1_M/C^{\rm obs}$, which is band (M.3).

> **Not transferable.** The note's Reading-II median ratio of **×4.29 (singles)**
> was computed on the **ex-ante stochastic functional** of W1-EA, not on Measure 1
> at $z^{\rm obs}$. At $z^{\rm obs}$ a worker's M/F ratio cannot exceed
> $e^{[L(o)-L(j^{\rm obs})]/\beta_c}$ (1.19 for the reference single man). The
> ×4.29 must not be cited as the consequence of choosing M.

---

## 2. Is Mapping M still Haydar–Maniquet $W^1$?

### 2.1 What the manuscript says

- **tex l.107:** $\mathcal J$ is the "Fixed universal set of *existing jobs*".
  **l.111:** "Ability set $A\subseteq\mathcal J$"; $\mathcal A$ may be all of $2^{\mathcal J}$,
  with restrictions "introduce[d] … when we use them".
- **l.114:** "To save on notation, we assume that as soon as we measure
  $W(z,R,A;\mathbf y)$, $z=(c,j)$ for some $j\in A$." This is a **domain restriction**
  on $W$.
- **l.97 (abstract):** "individuals take one job in their ability set." The baseline
  model contains **no non-employment state**.
- **l.198:** "A job $j$ is infeasible … if $j\notin A$. … if $j\notin A$, then no
  bundle containing job $j$ can be chosen by this individual." Semantically, $A$ is
  what can be chosen.
- **l.306 (Measure 4 only):** "Assume there is a '*job*', say $o$, consisting of
  staying home, with $\mathbf y(o)=0$, such that everybody has it in their ability
  set: for all $A\in\mathcal A$, $o\in A$." The word "job" is in scare quotes and
  the sentence opens with "Assume". It is a restriction on $\mathcal A$ introduced
  for Measure 4.
- **thm:imp1** (l.393–449) is proved with $A=\{j_1,j_2\}$ and singletons
  $\{j_2\}$, sets that contain no $o$. **thm:w4** (l.850–866) aligns the environment
  to $(\{o\},\mathbf 0)$ and so needs $o\in\mathcal J$ and $\{o\}\in\mathcal A$.

### 2.2 Two ways to place an observed nonworker

- **Reading (α) — $o$ is a state, not a job.** $o\notin\mathcal J$. Ability sets stay
  subsets of $\mathcal J$ (market jobs). The bundle space is extended to
  $Z^+=Z\cup(\mathbb R_+\times\{o\})$, and l.114 is relaxed to
  "$z$'s job $\in A\cup\{o\}$".
- **Reading (β) — $o$ is a job in the ability set** (Measure 4's convention, and
  l.198's semantics). The ability set is $A^+$, and M evaluates against
  $A^+\setminus\{o\}\ne A^+$.

### 2.3 Under (β), M violates Responsibility For Equal Pay

RFEP (l.225–229) requires that the value of $W$ at $\arg\max_{(A,\mathbf y)}R$ be
independent of $R$ whenever pay is equal on $A$. Take the ability set $A^+$ with
equal pay $\mathbf y^{[x]}$ on $A^+$. (If $\mathbf y(o)=0$ is imposed, then $x=0$
and the argument is unchanged.)

- Let $R$ rank $o$ first at equal consumption, as every estimated preference does
  (note F1b). Its laissez-faire bundle is $(x,o)$, and
  $W_M\big((x,o),R,A^+\big)=\min_{j\in A^M}m(j)>x$.
- Let $R'$ rank a market job $j^\*\in A^M$ first. Its laissez-faire bundle is
  $(x,j^\*)$, and $W_M=m(j^\*)=x$.

The two values differ, so RFEP fails. Under (β), M **compensates** the
preference for staying home at equal pay, where Measure 1 holds individuals
responsible for it. **Reading (β) ⇒ verdict C.**

### 2.4 Under (α), trace of the axioms and of thm:w1

Let $D^+=\{(z,R,A,\mathbf y):A\in2^{\mathcal J}\setminus\{\emptyset\},\ z\in\mathbb R_+\times(A\cup\{o\})\}$
and $W^1$ be defined by Measure 1's formula (l.258–266). By note §0.1 that formula
equals $\min_{A}m$, and its derivation never used "$z$'s job $\in A$".

| axiom | $W^1$ on $D^+$ | used in thm:w1's proof? |
|---|---|---|
| **Representation** (l.124–127) | **Holds.** At fixed $(R,A)$, $W^1=\varphi_A^{-1}(u(z))$ with $\varphi_A(x)=\max_{j\in A}u(x,j)$ strictly increasing. The axiom as written already quantifies over all of $Z$; only l.114 restricted it | yes, once: linking $z$ to $\bar z$ |
| **Independence of $\mathbf y$** (l.158–162) | **Holds.** The reference budget $B$ contains no $\mathbf y$ | yes |
| **RFEP** (l.225–229) | **Holds, content unchanged.** It bites only at $\arg\max_{(A,\mathbf y)}R$, which under (α) is always a market bundle. It is **silent at nonworker points** | yes, at $\bar z$ only |
| **Job Duplication Invariance** (l.132–136) | **Fails if read literally at nonworker points.** Adding to $A$ a copy of $z$'s job $o$ lowers $W^1$ from $m$ above $C$ down to $C$. **Holds** once the antecedent requires $z$'s job $\in A$, which is its stated rationale ("being able to occupy two identical jobs") | yes, at $\bar z$ only (restricted form suffices) |
| **Job Neutrality** (l.140–144) | **Holds.** Permutations act on $\mathcal J$; $o$ stays fixed | structural |
| **IPIJ** (l.200–209) | At nonworker points $W^1$ depends on how $R$ ranks $o$-bundles, with $o\notin A$. **Holds** if "feasible bundles" is read over $A\cup\{\text{job}(z)\}$. (As printed, the axiom quantifies over all of $Z$, which makes it vacuous; the prose intends feasible bundles.) | no |
| **Independence of $A$** | fails, as $W^1$ always does (table l.343) | no |

**Proof trace of thm:w1 (l.553–595) on $D^+$.**
- **Hypothesis.** The printed hypothesis (th\_1\_z) reads
  "$z=\arg\max_{(A,\mathbf y^{[x]})}R$". The next step uses Representation to
  pass from $z$ to $\bar z$, so "$z\,I\,\arg\max$" is what is meant (as in
  thm:w2/w3). With "=", a nonworker could never satisfy the hypothesis, since her
  job is not in $A$. With "$I$", she does iff $A\ne\emptyset$. The consumption-domain
  condition $u(z)\ge\max_{A}u(0,j)$ holds automatically under $\beta_c\log c$.
- **S1**, Independence of $\mathbf y$: ✓.
- **S2**, Representation between $z$ (job $o$) and $\bar z=(x,j)$ with $j\in A$: ✓ on $Z^+$.
- **S3**, RFEP at $\bar z$: ✓.
- **S4**, JDI at $\bar z$ under $R^c$: ✓ (restricted form).
- **S5**, Representation under $R^c$: ✓.

> **Result [derived here].** On $D^+$, any $W$ satisfying Representation (on
> $Z^+$), Independence of $\mathbf y$, RFEP, JDI (antecedent: $z$'s job $\in A$) and
> Job Neutrality agrees with $W^1$ in the manuscript's sense. Conversely, $W^1$
> satisfies these axioms on $D^+$. The characterization **survives the domain
> extension**. Its only new requirement is **$A\neq\emptyset$**; for the empty
> set it is silent.
>
> One pre-existing point, orthogonal to the fork: the proof establishes
> "equal $x$ ⇒ equal $W$", i.e. ordinal equivalence up to the scale convention
> $W(\text{laissez-faire at }\mathbf y^{[x]})=x$. The companion results thm:w3 and
> thm:w5 were already restated ordinally (agent.md).

### 2.5 Which reading does the manuscript support?

**For (α).**
- $\mathcal J$ is "existing jobs" (l.107).
- $o$ appears only as an assumed, quote-marked "job" for Measure 4 (l.306).
- $\mathcal A$ defaults to $2^{\mathcal J}$, and the impossibility proofs use
  $o$-free sets (thm:imp1).
- The abstract contains no non-employment.

The formal definitions therefore read $A$ as the **market-job** ability set.

**Against (α).** The semantics of l.198 ("what can be chosen") and the domain of
thm:w4. If the JMP invokes thm:w4 to characterize $W^4$, it places $o$ in the
ability set. Under (α), $W^4$'s formula $z\,I\,(x,o)$ is still well defined on
$Z^+$, but thm:w4's proof route through $(\{o\},\mathbf 0)$ is not available and
would need restating.

**The substance is the same in both readings.** M assigns a nonworker at
consumption $x$ strictly more than $x$ (about 1–5% more under the dense law, §4),
and assigns an equal-consumption worker at her $L$-best market job exactly $x$.
Under (β) this is an RFEP violation; under (α) RFEP does not reach the comparison.
**The verdict turns on one question: is staying home an *ability*?**

### 2.6 Verdict

> **B — MINOR DOMAIN EXTENSION**, under the manuscript's default job universe
> (reading α). The equal-consumption own-set construction and both characterizing
> axioms (Independence of $\mathbf y$, RFEP) are intact. Four amendments must be
> declared:
> - **(E1)** $z$'s job $\in A\cup\{o\}$, with $o\notin\mathcal J$ (relaxes l.114);
> - **(E2)** $A\neq\emptyset$;
> - **(E3)** JDI's antecedent restricted to $z$'s job $\in A$;
> - **(E4)** IPIJ read over $A\cup\{\text{job}(z)\}$.
>
> For **workers** alone, M is **A — the same $W^1$**. If the paper anywhere
> treats $o$ as a job in the ability set on the domain where $W^1$ is
> characterized (reading β), the verdict is **C**.
>
> **For comparison, F is A:** the same $W^1$, on Measure 4's restriction of
> $\mathcal A$. On the estimated preference domain it makes $W^1$ coincide with
> $W^4$ (note §1.3).

**The PI's preliminary reading is confirmed.** That reading was taken from the
project copy `The_draft_theorypaper.tex`. Against the authoritative source the
same three points hold: Measure 1 (tex l.258–266) never uses "$z$'s job $\in A$";
that convention is introduced "to save on notation" (l.114); and Representation
pins an out-of-set bundle to its indifferent in-set bundle only when $A\neq\emptyset$.
The trace adds three things:
- the qualifier that B requires staying home **not** to be a job in the ability
  set (§2.3);
- the "=" versus "$I$" issue in thm:w1's printed hypothesis;
- the restatements of JDI and IPIJ, (E3) and (E4).

### 2.7 Cross-check against the impossibility theorems

thm:imp1 is unaffected. $W^1_M$ fails Independence of $A$ as $W^1$ should.
Under F, $W^1_F$ satisfies Independence of $A$ on the estimated subdomain (note
§1.3), so F moves $W^1$ into $W^4$'s column of the table. Under M with the dense
law (§4.1a), $W^1_M$ equals **Measure 6 over the market-job universe** (§4.4). That
measure satisfies Full Compensation, and hence Independence of $A$ (table l.341–343).
M therefore moves $W^1$ into $W^6$'s column. Only a finite set law restores
$A$-dependence.

### 2.8 Normative-intent evidence (project history, not instruction)

**Source.** The PI identifies the primary source as `discussion2.md`, attached to an
archive chat. It is **not in either repository**. A search of the Job_Market_paper
and MNL text sources, the local session transcripts, and the user's Downloads,
Desktop, Documents and Repo folders found no copy. This note therefore relies on the
ruling header's description, and **its numbers cannot be re-derived here**. The
caveat stands until an excerpt is placed in `docs/normative/`.
As described, the example has:
- market-job sets $\{1,2\}$ and $\{2,3\}$ with no home option;
- a measure anchored at the observed job;
- $W_i=100$ "since job 3 is not in the ability set", and $W_k=60$.

**Consistent with M.** The binding comparison is among market jobs in the own
set. "Since job 3 is not in the ability set" is precisely the M worker equality
case: if 100 is $i$'s observed consumption at her $L$-best *available* job, (M.1)
gives $W_i=C_i^{\rm obs}=100$.

**Inconsistent with F only on the estimated preference domain.** Under F, every
worker has $W^1_F<C^{\rm obs}$ (note (1.1)), so a value equal to observed
consumption cannot arise for a worker. The operative reason would become "since
$o$ is in the ability set". In the **abstract** theory, however, the example
specifies no preference over $o$. If $o$ were not ranked first, adding it would
change nothing. The inconsistency is F combined with note F1b, not F as such.

**$W_k=60$** cannot be checked without the example's bundles.

**Silent on nonworkers.** The example therefore offers no evidence on amendments
(E1)–(E4).

**Corroborating history.** The Theory-talk spoken script, slide 7
(`beamer/reference/Theory_talk/slides/spoken_script_click_cues.tex`, l.103–124),
illustrates $W^1$ with $A=\{j,k\}$ and $A'=\{k,\ell\}$, market jobs only, no home
node: "the overall preferred job is not in the ability set — job $j$ — so we
restrict ourselves to the preferred job within the ability set." Same structure.

**Manuscript.** Its formal definitions support reading $A$ as the market-job set
(§2.5).

---

## 3. The empty market ability set

### 3.1 Which set law does the model support?

**The criterion is exact under a dense law.** The executed criterion is an
importance-sampled approximation to

$$\Pr(y\in dj)=\frac{e^{u_i(j)}g_i(j)\,\nu(dj)}{e^{u_i(o)}+\int_{\rm mkt}e^{u_i}g_i\,d\nu},$$

which is Dagsvik–Jia (2016) **Theorem 1**. They derive it from their
**Assumption 2**: offers form an inhomogeneous Poisson process whose multiplicative
taste shifters have intensity $\varepsilon^{-2}d\varepsilon$, for non-market and
market opportunities alike (`Literature/markdowns/Dagsvik_Jia_2016.md`, l.42–51).
In logs this is the note's §4.1 intensity $\kappa_i\lambda_i(dj)\,e^{-\epsilon}d\epsilon$.
Its total mass is **infinite**: every set of positive $\lambda$-mass contains
infinitely many latent jobs almost surely, and only finitely many exceed any given
match level. Under this construction the executed criterion holds **exactly**
(note §4.1, properties 1–3).

**Finite-count readings do not reproduce the criterion.** Take a Poisson number of
jobs with i.i.d. Gumbel marks, as in the note's §3.1 and the $e^{-1}$ of note F1a.
By the Mecke formula, the choice density is proportional to
$\kappa\lambda(dj)\,e^{u(j)}\,\mathbb E[1/(e^{u(j)}+S)]$, with
$S=\sum_{k\in A}e^{u_k}$. That factor varies with $u(j)$, so the density is not
proportional to $e^{u(j)}$. For $o$ with $N\sim$ Poisson(1) copies,

$$\Pr(o)=\sum_{n\ge1}\tfrac{e^{-1}}{n!}\,\tfrac{ne^{u_o}}{ne^{u_o}+\Theta}\;<\;\tfrac{e^{u_o}}{e^{u_o}+\Theta}$$

by Jensen's inequality (the summand is concave in $n$). As $\Theta$ varies across
households this is not of the form $a/(a+\Theta)$. Finite readings approximate the
criterion when the expected count is large and are separable from it only through
functional form.

> **Amendments to the note (recorded; the note is not edited).**
> - **(N1)** Note F1a: the $e^{-1}$ reading is **not** strictly observationally
>   equivalent to deterministic $o$ under the executed criterion. Under the
>   construction on which that criterion is exact, $o\in A_i$ **almost surely**.
>   F's premise is thereby strengthened.
> - **(N2)** The note's §3.1 survival form $e^{-\kappa\Lambda(x)}$ belongs to the
>   finite reading. Under the exact construction $\Lambda=\infty$, and Reading II
>   sits at its $\kappa\to\infty$ endpoint.
> - **(N3)** Note F3 (Reading II) says "$\kappa\to0$ ⇒ $W\to+\infty$". That holds for
>   nonworkers or unconditioned sets only. A worker's set contains $j^{\rm obs}$, so
>   $W\to C^{\rm obs}$ (§1.2).
> - **(N4)** The ×4.29 ratio is not a property of Measure 1 at $z^{\rm obs}$ (§1.2).

**Deterministic-set stance.** The record states the project's stance as "RO as
estimation machinery". With a continuous hours offer density, a deterministic set
whose composition is $g_i$ is itself dense in the support. A *finite* deterministic
set needs an extra object that the criterion does not contain.

### 3.2 Singles

- **Does the model admit zero market offers?**
  - Dense law: **no**, $\Pr(A^M_i=\emptyset)=0$.
  - Finite hypothesis (added): $\Pr=\exp(-\kappa_i\Lambda_i^{\rm mkt})>0$.
- **Identified from the RURO likelihood?** **No.** The executed likelihood contains
  no $\kappa_i$ (note §2.2) and is the dense-law likelihood. A finite law would enter
  only through the Jensen distortion above, i.e. identification by functional form,
  which the estimator does not use. $\Pr(\emptyset)$ is therefore either 0 by the
  model's foundation or an unidentified number in $(0,1)$ under an added hypothesis.
  (Under the normalisation $g_i(o)\equiv1$ the finite reading would give
  $e^{-9.62}$ or $e^{-20.84}$ at $c_i=0$, from note §2.3. Those values are the
  normalisation's, not the data's, and are not job counts.)
- **Workers.** $j^{\rm obs}\in A^M$ in every reading, so the set is **never empty**.
- **Nonworkers.**
  - Dense law: non-empty almost surely **even conditional on having chosen $o$**.
    The conditional law (note §4.1) is the process truncated to
    $\{u+\epsilon<v\}$, which still has infinite mass in every region.
  - Finite hypothesis: $\Pr(A^M=\emptyset\mid o\text{ chosen})=e^{-\kappa\Lambda}/P_i^{\rm fin}(o)>e^{-\kappa\Lambda}$,
    since an empty set forces $o$. Observed non-employment is evidence of a thin
    market. This probability ranges over $(0,1)$ as $\kappa$ ranges over
    $(0,\infty)$ and tends to 1 as $\kappa\to0$.

### 3.3 Couples

- **Who is at risk.** Every couple with at least one employed spouse has
  $j^{\rm obs}\in A^M$. **Only observed NN couples are at risk.**
- **Dense law** (Poisson on pairs; the joint criterion is exact under it):
  $\Pr=0$.
- **Finite Poisson-on-pairs:** $\exp(-\kappa\lambda(\{\text{pairs with}\ge1\text{ employed}\}))$.
- **Cartesian product of spouse sets** (each containing $o$):
  $e^{-\kappa_m\Lambda_m-\kappa_f\Lambda_f}$.
- The two finite versions differ, and **only the product version has free
  disposal** (a spouse can always leave her or his job). Neither reproduces the
  executed joint criterion exactly.

### 3.4 Principled treatments, if a finite law is adopted (none chosen)

Labels (a)–(e) follow revised header item 5.

| treatment | what it assumes | implications |
|---|---|---|
| **(a)** Condition on $A^M\neq\emptyset$ | Households with an empty market set lie outside the welfare comparison | The population becomes $\kappa$-dependent: nonworkers drop out with probability $\Pr(\emptyset\mid o)$. It needs the law of $A^M\mid y$ on the non-empty event, hence $\kappa$. Counterfactual access moves the conditioning event, so a decomposition would run on a moving population |
| **(b)** Report $W^1_M$ on the non-empty event together with the mass of the empty event | Nothing about the empty state's welfare | Honest but incomplete. No scalar inequality index or Owen decomposition exists over the full population. The mass is $\kappa$-dependent and must be reported across the $\kappa$ grid |
| **(c)** Assign the observed bundle's own $m$: $W^1:=m_i(j^{\rm obs})=C^{\rm obs}$ on the empty event | A household with no market options is its own reference: Measure 1 on $A=\{o\}$, i.e. Mapping F on that event | Breaks $W^1$'s set-monotonicity: $W^1$ should weakly fall when a job is added, but adding one 70-hour job to $\emptyset$ raises $W$ from $C$ to as much as $12\times C$ (reference single man, Table 1). A discontinuous F/M hybrid whose empty-event mass is $\kappa$-dependent |
| **(d)** Treat the empty event as a distinct welfare state | The welfare ordering is incomplete across the state boundary | Needs a separate rule comparing the state with scaled households. Decompositions need that rule, or must hold the state's mass fixed, which access operators do not |
| **(e)** The formal convention $\min\emptyset=+\infty$ | The mathematical infimum convention is adopted as a welfare statement. This is Measure 1's set-monotonicity (at a fixed bundle, a smaller $A$ gives a weakly higher $W^1$) taken to its limit | See the analysis below |

**Analysis of (e).**
- **Pointwise.** For a nonworker, removing market jobs from a non-empty $A^M$ raises
  $W^1_M$ monotonically, but only up to the finite ceiling of (M.3),
  $C^{\rm obs}e^{[L(o)-\underline L^{\rm mkt}]/\beta_c}$. That is 12.1× at the
  reference single man and 5.6× (free disposal) at an NN couple with the reference
  weights. The rise is bounded because the hours support is capped at 70 h
  ($\tilde\ell=1$, $\mathcal B=0$). With $\theta_\ell<0$, $\mathcal B(\tilde\ell)\to-\infty$
  as leisure tends to 0, so without the maintained cap the rise **would** be
  continuous and unbounded. With the cap, the $+\infty$ is a **discontinuous jump
  at $\emptyset$**, from at most the ceiling to $+\infty$. The PI's "rises without
  bound as the market set thins" therefore holds only in this jump sense, or
  without the cap.
- **In distribution.** Under a finite law, $\Pr(A^M=\emptyset\mid o)\to1$ as
  $\kappa\to0$ (§3.2). Hence $W^1_M\to+\infty$ in probability for every nonworker,
  and, under a finite law, $\mathbb E[W^1_M]=+\infty$ at every finite $\kappa$
  (the empty event has positive mass).
- **Implications.**
  - Households with the thinnest markets sit at the **top** of the distribution:
    having no market access is rated as the best-off state.
  - Every mean-based level or inequality index is infinite, and the Owen
    decomposition is undefined.
  - The measure is discontinuous at the empty set.

  This is why (e) cannot be adopted as a number. It is the formal content of (d),
  and it shows why (d) must be a *state* rather than a value.

Under the dense law, and under F, no treatment is needed.

---

## 4. Latent-set size and intensity

### 4.1 The identification result, derived from the RURO model

$W^1_M$ depends on $A^M$ **only** through $S_i=\max_{j\in A_i^M}L_i(j)$. This is an
extremal (support-type) functional of the realised set, and because $L$ depends on
hours only, it is the $L$ of the shortest-hours element. Three cases follow.

**(a) The model's exact foundation (dense law).** $S_i=\bar L_i^{\rm mkt}$ almost
surely. Every neighbourhood of 5 h/week in the support holds infinitely many latent
jobs, and their match values do not matter because shocks are excluded from the
welfare ordering. Hence

$$W^1_{i,M}=C_i^{\rm obs}\exp\!\Big[\tfrac{L_i(j_i^{\rm obs})-\bar L_i^{\rm mkt}}{\beta_c}\Big]\quad\text{a.s., for every }\kappa\text{ and every shape of }g\text{ on the same support}.\tag{M.4}$$

This is the lower end of (M.2)–(M.3). It needs **no intensity and no set size**.
It needs instead:
- the **support endpoint**: 5 h/week for singles; for couples, the better
  single-earner 5-hour configuration. This is maintained, not identified from choices;
- the deputy's shock exclusion.

The gap to F is $e^{[L(o)-\bar L^{\rm mkt}]/\beta_c}$ [derived here]:
- single men: 1.009–1.015 over ages 20–60;
- single women: 1.028–1.053 ($k=0$; children raise it slightly);
- couples: 1.012–1.013 at the block minima and at the reference household
  (woman-only at 5 h is the $L$-best configuration there; no couples age support
  was located, so no wider range is claimed).

M under the dense law is therefore Measure 1 with **a reference job common to all
households** (the shortest market job). It is F with $o$ replaced by the marginal
market job, and it tends to F as the support endpoint tends to 0.

**(b) A finite law (added hypothesis).** Condition on $y$ and on the attained level
$v$. The other latent points are a Poisson process thinned by $G(v-u_i(k))$, so

$$\Pr\big(\text{no market latent job with }L>\ell\text{ besides }y\mid y,v\big)=\exp\!\Big\{-\kappa_i\!\int_{{\rm mkt},\,L>\ell}G(v-u_i(k))\,\lambda_i(dk)\Big\},$$

and $v\mid y$ itself has a $\kappa$-dependent law (note §4.1). The distribution of
$W^1_M$ therefore depends on $\kappa_i$. It stays inside (M.2)–(M.3), tends to (M.4)
as $\kappa\to\infty$, and as $\kappa\to0$ tends to $C^{\rm obs}$ for workers and to
the empty set for nonworkers.

**(c) No law.** The identified set is (M.2)–(M.3), and it is sharp.

### 4.2 The unidentified scale required under (b)

- **The scalar or object.** $\kappa_i^{\rm eff}>0$: the absolute intensity of the
  latent market jobs that count as belonging to $A_i$, i.e. the expected number of
  such jobs per unit of the identified opportunity measure. In the dense
  construction it is equivalently a **cut in the match-value dimension**,
  $\kappa^{\rm eff}_i=\kappa_ie^{-c_i}$. Any finite ability set extracted from the
  model's latent process needs such a cut.
- **Why it cancels from choice probabilities.** $V_{ij}\mapsto V_{ij}+\log\kappa_i$
  for every $j$, which cancels in the log-sum-exp (note §2.2). In the dense
  construction, scaling the intensity is a common location shift of every match
  value, and the law of the argmax's location is invariant (note §4.1, property 3).
  A cut below the attained level never removes the chosen point. Choices reveal
  only the maximum.
- **Why it does not cancel from $W^1_M$.** $W^1_M$ reads the realised set's
  extremal $L$, not the argmax location. $\kappa$ multiplies the cumulative hazard in
  (b), and there is no ratio for it to cancel in. Contrast W1-EA, where $\kappa$
  cancels between $J$ and $H$ (note §3.2).
- **External data or calibration that could identify it** (listed, not recommended):
  - (i) Hours-constraint self-reports. The share of workers who would work fewer
    hours at the same hourly pay maps to $\Pr(\text{no shorter-hours job in }A^M)$,
    which is exactly the M equality case. This is the most direct link, but it
    needs an explicit mapping from a stated constraint to the latent set. The
    project's LFS moments (R-249) cover the wish-for-*more*-hours margin, which is
    the other side of the support.
  - (ii) Vacancy-to-jobseeker ratios (market-level; need a household-level mapping)
    (note §7.1(ii)).
  - (iii) Offer-arrival rates from search models (Bloemen 2000), with his warning
    about joint identification (note §7.1(iii)).
  - (iv) The employment margin by group, which identifies $\kappa$ only jointly with
    the reservation structure (note §7.1(i)).
- **A transparent sensitivity analysis.**
  1. Report (M.4) as the value under the model's foundation.
  2. Report the $\kappa$-free band (M.2)–(M.3) for every household.
  3. If a finite law is entertained: a grid of $\kappa^{\rm eff}$ multipliers from
     "about one market job with $L$ above the observed" to dense, drawn from the
     **conditional** law of note §4.1 (never an unconditional draw with $y$ added).
     Plot the level distribution, inequality and, later, the Owen shares against
     $\kappa$, together with the nonworker empty-event mass under whichever of
     (a)–(e) the PI selects.
  4. A support-endpoint sensitivity for (M.4), from 5 down to 1 h/week.

  Choose no point on any grid.

### 4.3 What this means for the fork

Under the model's own foundation, **neither mapping gives baseline $W^1$ any
household-specific ability-set content**: F references home, and M references the
shortest market job, both common to all households. The force of the co-author's
example (different people, different sets) needs a **finite** set law, and a finite
set law needs $\kappa^{\rm eff}$, which choices do not identify. The substantive
fork is therefore not F versus M. It is **dense (identified, set-free)** versus
**finite (set-bound, needs $\kappa$)**. At $z^{\rm obs}$, F versus M under the dense
law is a 1–5% question.

### 4.4 Intensity limits (revised header item 7)

Let the market offer intensity be $\kappa_i\lambda_i$, with $\lambda_i$ the
identified relative measure (note §2.2). $W^1_M$ depends on $A^M_i$ only through
$S_i=\max_{A^M_i}L_i$ (§4.1).

**$\kappa\to\infty$.** Under the conditional law of note §4.1, the realised set
fills the market hours support, $S_i\to\bar L_i^{\rm mkt}$ almost surely, and
$W^1_M$ converges to (M.4). This limit coincides with the dense law.
- **(i) Identified?** Yes, **conditional on the maintained support endpoint**
  (`h_min = 5.0`, a spec convention) and on shock exclusion. (M.4) contains only
  observed $C^{\rm obs}$ and $h^{\rm obs}$, the identified leisure block and
  $\beta_c$. No opportunity parameter and no $\kappa$ enters. The data do not
  identify the endpoint itself: the lowest observed employed hours are 5 (couples,
  women), 6 (singles) and 9 (couples, men), per the record in Appendix A.
- **(ii) Direct access dispersion?** **None.** The hours support $[5,70]$ is common
  to all households. On it the offer density is strictly positive for every
  household, because every factor of $g$ is an exponential and the band elevations
  and market shifters scale the density without moving the support. Occupation and
  wage offers do not enter $L$. $\bar L_i^{\rm mkt}=L_i(5\text{ h})$ varies across
  households only through $\beta_\ell^g(\mathbf x_i)$, which is preferences. For
  couples, which spouse's 5 h configuration is the reference is also decided by
  preferences alone.
- **(iii) An Independence-of-$A$ object?** Yes, and a named one. With the realised
  set dense in the market universe $\mathcal J^{\rm mkt}$,
  $W^1_M=\inf_{j\in\mathcal J^{\rm mkt}}m_i(j)$, which is **Measure 6** (tex l.335:
  "their preferred job over all existing jobs", at equal pay) with
  $\mathcal J=\mathcal J^{\rm mkt}$. $W^6$ satisfies Full Compensation, hence
  Independence of $A$ (table l.341–343), and thm:w6 characterizes it. **This is M's
  analogue of F's collapse.** F turns $W^1$ into $W^4$, which on the estimated
  domain equals $W^6$ over $\mathcal J^{\rm mkt}\cup\{o\}$. M at $\kappa=\infty$
  turns $W^1$ into $W^6$ over $\mathcal J^{\rm mkt}$.

  *Implementation caution:* the record's executed $W^6$
  (`m08_welfare_measures.py:295–303, 522–537`) is a log-sum-exp over a universal
  leisure grid, not the minimum. The theory identity must not be read as a numerical
  identity with the reported $W^6$ until that grid's domain and functional are
  checked. Not checked here.

**$\kappa\to0$.** Workers: the conditional set shrinks to $\{j^{\rm obs}\}$ and
$W^1_M\to C^{\rm obs}$. That is Measure 1 on the singleton own-job set, pure
consumption, and also degenerate. Nonworkers: $\Pr(\emptyset\mid o)\to1$, so
$W^1_M$ is undefined, or $+\infty$ under convention (e).

**Conclusion (the PI's prior, verified).** Both limits are degenerate, and neither
carries direct access dispersion. **Under M, the direct opportunity channel exists
only at finite $\kappa$**, which choices do not identify. Adopting M as a carrier of
access content therefore commits the analysis to one of two things: external
intensity information, or a reported $\kappa$-sensitivity band (§4.2). The decision
is **F versus (M + a $\kappa$ stance)**. Taking $\kappa=\infty$ is itself a stance,
the model's own. It returns $W^6$ over market jobs, not a household-specific $W^1$.

**Is $\kappa$ common or household-specific under the model?** The model cannot
say. The likelihood is invariant to *any* household-specific $\kappa_i>0$ (note
§2.2), and the executed code already applies one: its centering sets
$\kappa_i=e^{-c_i\bar E_i}$ (note §2.2). A common $\kappa$, meaning one
home-option intensity for everyone relative to the market, is an **added
restriction**. The identified content is $\lambda_i$ up to $\kappa_i$.

**What external data would pin it** (§4.2):
- hours-constraint self-reports (would work fewer hours at the same hourly pay),
  which bear directly on the $W^1_M=C^{\rm obs}$ event;
- vacancy-to-jobseeker ratios by market cell, for a $\kappa$ common within a cell;
- offer-arrival rates from search models (Bloemen 2000), for a covariate-dependent
  $\kappa_i$;
- the employment margin, only jointly with the reservation structure.

---

## 5. Couples

**Coherence.** The joint $L$ is additive with no cross-leisure term (note §1.2).
The joint opportunity measure is product-form on pairs, with the NN atom normalised
to 1 (note §2.1, §2.3). The M region is a union of three product blocks (man only,
woman only, both). Excluding only NN is therefore coherent with both the utility
and the opportunity structure.

| configuration | in $A^M$? | issues |
|---|---|---|
| **Neither works** | no | Observed NN couples have $z^{\rm obs}=(C,(o,o))\notin A^M$, so amendment (E1) applies and $W^1_M>C^{\rm obs}$ strictly (note F1b, both spouses). The empty-set risk exists **only** here. The 119 couples whose NN node lies outside the positive-consumption domain (note §1.1) no longer affect the reference, because M never evaluates the NN node; they matter only through their own $C^{\rm obs}$. Band [derived here, reference $\beta$'s]: $[1.0125,\,5.60]\times C^{\rm obs}$ with free disposal, $[1.0125,\,187]\times C^{\rm obs}$ without |
| **Man only** | yes | $W\le C^{\rm obs}$. Man-only at 5 h is one of the two candidates for the $L$-best configuration. Reference household at 39 h: F 0.7868, dense-law M 0.7967, band [0.7967, 1] |
| **Woman only** | yes | Symmetric. **Woman-only at 5 h is the $L$-best configuration** at the reference household and at the block minima: the 0→5 h leisure loss is 0.0262 versus the man's 0.0356. It is **not** the reference for every couple. Man-only wins when $\beta_\ell^f/\beta_\ell^m>4.278$, a narrow region with a young woman and a large age gap (§5.1) |
| **Both work** | yes | **Never the $L$-best configuration** under free disposal or the dense law, since replacing either spouse's job with $o$ strictly raises $L$. Dual earners therefore have $W^1_M<C^{\rm obs}$ strictly, and the upper bound tightens to $C^{\rm obs}\min\{e^{-\ell_f(h_f)/\beta_c},e^{-\ell_m(h_m)/\beta_c}\}$, with $\ell_s(h)=L^s(0)-L^s(h)$. Under finite Poisson-on-pairs (no free disposal) the upper bound is $C^{\rm obs}$ |

**Issues to report separately.**
- (i) **Free disposal** is a coherence requirement that a finite law on pairs must
  add. Poisson-on-pairs violates it, and the Cartesian product restores it at the
  cost of exactness.
- (ii) Product-form dependence between spouses' offers is maintained and untested
  (note §2.3).
- (iii) The household welfare unit is unaffected, but the M reference
  configuration switches between spouses as $\beta_\ell^m(\mathbf x)$ and
  $\beta_\ell^f(\mathbf x)$ vary.

### 5.1 Which single-earner configuration is the reference, term by term

**Why the block levels mislead.** The couples index has no cross-leisure term
(`beta_ll` is absent from the 47 coordinates) and no other interaction. So
$L(o,h_f{=}5)-L(h_m{=}5,o)=\ell_m(5)-\ell_f(5)$, where $\ell_s(5)=L^s(0)-L^s(5)$ is
spouse $s$'s own 0→5 h leisure loss. What matters is that **finite difference near
full leisure**, not the level of $\beta_\ell$:

$$\ell_s(5)=\beta_\ell^s(\mathbf x)\,\big[\mathcal B(8;\theta_\ell^s)-\mathcal B(7.5;\theta_\ell^s)\big].$$

**Term by term [derived here] from `s11_couples_parameter_table_v1.csv`.**

| term | men | women |
|---|---:|---:|
| $\theta_\ell^s$ | $-0.97611$ | $-1.68631$ |
| $\mathcal B(8)$ | 0.889893 | 0.575222 |
| $\mathcal B(7.5)$ | 0.881143 | 0.573176 |
| $\Delta\mathcal B=\mathcal B(8)-\mathcal B(7.5)$ | **0.008751** | **0.002045** |
| slope $\mathcal B'(7.75)=7.75^{\theta-1}$ | 0.01748 | 0.00408 |
| $\beta_\ell^s$ at the block minimum | 3.9789 | 12.5868 |
| $\ell_s(5)$ at the block minimum | 0.03482 | **0.02575** |
| $\beta_\ell^s$ at the reference household (man 38, woman 37, $k=3$) | 4.0686 | 12.8135 |
| $\ell_s(5)$ at the reference household | 0.03560 | **0.02621** |

The women's curvature is steeper: $\theta_\ell^f=-1.686$ against $-0.976$. That makes
their Box-Cox increment over the last 5 hours **4.278 times smaller** than the men's
($0.008751/0.002045$). This more than offsets a leisure weight that is only about
3.15 times larger. Hence woman-only at 5 h is the reference.

**When man-only is the reference instead.** Exactly when

$$\beta_\ell^f(a_f,k)\,/\,\beta_\ell^m(a_m)\;>\;4.2784 .$$

Both $\beta_\ell^s$ are quadratics in the spouse's own age, centred at 41.10 years
with scale 1. The women's weight also carries $-0.3055\,k$.
- If both spouses have the same age, the ratio peaks at **3.33** ($k=0$, age 37.7),
  so woman-only always wins. As $|a|\to\infty$ the ratio tends to 1.13.
- With independent ages, man-only needs $\beta_\ell^f>4.2784\times\min\beta_\ell^m=17.02$.
  That requires a woman aged **≤ 24.9** ($k=0$; ≤ 24.0 at $k=1$; ≤ 23.2 at $k=2$)
  or ≥ 74.1, and a man near the age that minimises $\beta_\ell^m$ (41.7).
- Examples, woman at $k=0$: a 20-year-old woman needs a man aged 33.4–50.1; a
  24-year-old woman needs a man aged 38.3–45.1.

So the couples reference under M is woman-only at 5 h except in a young-woman,
large-age-gap corner. **How many sample couples fall in that corner is not
computed here.** It needs the couples frame, i.e. a script. Either way the
consequence for $W^1_M$ is small: the M/F gap is
$e^{\min\{\ell_m(5),\ell_f(5)\}/\beta_c}$, about 1.01–1.02 over the ages examined
(20–60).

**Discarded alternative — "both employed".** With $A^{MM}=\{\text{both employed}\}$:
- every single-earner couple's observed bundle falls outside $A^{MM}$, so the domain
  extension spreads from NN couples to all single-earner households, which then get
  $W>C^{\rm obs}$;
- the reference becomes "both at 5 h", which excludes behaviourally feasible,
  market-active configurations with no theoretical reason;
- under a finite product law the empty-set risk rises to
  $1-(1-e^{-\kappa\Lambda_m})(1-e^{-\kappa\Lambda_f})$.

Reported only; not a candidate.

---

## 6. Comparative verdict

| | **FULL SET F** | **MARKET REFERENCE M** |
|---|---|---|
| theory status | **A — the same $W^1$**, on Measure 4's restriction $o\in A$ for all $A$ | **B — minor domain extension** (E1–E4) under the default job universe; **A** for workers; **C** if staying home is treated as a job in the ability set (RFEP fails, §2.3) |
| non-employment in the reference | yes; it is the $L$-maximiser for every household (note F1b) | no; it stays in behaviour only |
| defined for nonworkers? | yes, $W=C^{\rm obs}$ | yes, $W>C^{\rm obs}$ strictly, **given $A^M\neq\emptyset$** (almost surely under the dense law) |
| pointwise order | $W^1_F\le W^1_M$ for every household (strict) | $W^1_M>W^1_F$ for every household |
| direct $A$ sensitivity | none (only "$o\in A$", which holds a.s. under the exact law) | $\kappa=\infty$ (dense law): **none**; the common support endpoint gives Measure 6 over $\mathcal J^{\rm mkt}$. Finite $\kappa$: yes, within the bounded band (M.2)–(M.3). $\kappa\to0$: $C^{\rm obs}$ for workers, $\emptyset$ for nonworkers |
| collapses to | $W^4$ (= $W^6$ over $\mathcal J^{\rm mkt}\cup\{o\}$) on the estimated domain | $W^6$ over $\mathcal J^{\rm mkt}$ at $\kappa=\infty$; household-specific $W^1$ only at finite $\kappa$ |
| needs a latent set law? | no | **yes**: dense gives (M.4); finite gives a $\kappa$-dependent distribution; with no law, sharp bounds only |
| needs an absolute set size? | no | dense: no. Finite: **yes**, $\kappa_i^{\rm eff}$, not identified (§4.2) |
| empty-set problem? | no | dense: no. Finite: yes for nonworkers and NN couples only, needing one of (a)–(e); (e) is analysed and cannot serve as a number |
| counterfactual attainment role | access enters **only** through the attained bundle (realised-bundle estimand needs $\kappa$ and a shock rule; ex-ante is $\kappa$-invariant) | the same, plus under a finite law the reference itself moves with counterfactual access |
| implementation burden | closed form (note (1.1)): $L(o)$ only | dense: closed form (M.4), $L$ at 5 h, and for couples a max over two single-earner configurations. Finite: conditional latent-set simulation, $\kappa$ grid, empty-set treatment, couples free-disposal convention |
| normative interpretation | "Flat consumption at home equivalent to the bundle." Coincides with $W^4$ at $z^{\rm obs}$; responsibility for ability sets is empty at baseline | "Flat consumption at the best market job equivalent to the bundle." Nonworkers are valued at their market equivalent. At $\kappa=\infty$ this is the least time-demanding market job (about 1–5% above F), i.e. $W^6$ over market jobs, so responsibility for ability sets is again empty at baseline. It becomes household-specific only at a finite, unidentified $\kappa$ |

### Recommendation (not implemented)

> **Primary empirical mapping: F**, $W^1_{i,F}=m_i(o)$ (note (1.1)), reported with
> the declared statement that on the estimated preference domain it coincides with
> **Measure 4 at $z^{\rm obs}$**. This is a theory identity. The executed $W^4$ is a
> different object (§6.1) and must not stand in for it.
>
> **M is reported beside it, not as primary**, in two forms, neither needing a
> $\kappa$ choice:
> - its $\kappa=\infty$ value (M.4), which is $W^6$ over market jobs;
> - the law-free sharp band (M.2)–(M.3). This is exactly the range any $\kappa$
>   stance could place $W^1_M$ in, and it is the $\kappa$-sensitivity band in
>   closed form.

**Why F.**
1. **The decision is F versus (M + a $\kappa$ stance)** (§4.4, verified), and no
   identified $\kappa$ stance gives M content that F lacks.
   - At $\kappa=\infty$, M is Measure 6 over market jobs. That is an
     Independence-of-$A$ object with no direct access dispersion, the same kind of
     collapse as F into $W^4$, and within 1–5% of F.
   - At finite $\kappa$, M carries household-specific access content, but $\kappa$
     is not identified. Making that version primary would impose exactly the
     set-size normalisation the ruling forbids.
2. **On everything the two share, F dominates the $\kappa=\infty$ version of M.**
   - Theory status: A versus B. F needs no domain extension and no restatement of
     JDI or IPIJ.
   - Dependencies: F does not depend on the maintained 5 h support endpoint.
   - Empty sets: F has none under any set law.
   - Content and identification: equal. Both are closed-form, $\kappa$-free, and
     have no household-specific set content.
3. **This revises the first version's recommendation, and the reason is explicit.**
   That version argued for M because (i) the manuscript and the co-author's example
   read the ability set as market jobs, and (ii) F makes $W^1\equiv W^4$.
   Revised header item 7 disposes of both.
   - On (i): the substance of the example, that different people have different
     sets, is delivered **only** by finite $\kappa$. The $\kappa=\infty$ version of
     M honours its letter (no $o$ in the reference) but not its content.
   - On (ii): the $\kappa=\infty$ version of M makes $W^1\equiv W^6$ over market
     jobs, a symmetric duplication. Whether it duplicates the record's executed
     $W^6$ is not established (§4.4 caution).

**Costs of F, stated.**
- Non-employment enters the reference, which departs from the reading of the
  ability set as market jobs that the manuscript's definitions and the co-author's
  example suggest (§2.5, §2.8).
- $W^1$ and $W^4$ coincide at $z^{\rm obs}$, and the paper must say so rather than
  present them as two measures.
- Access reaches $W^1$ only through attainment (§1.1).
- The recommended object, Measure 1 at $z^{\rm obs}$ via note (1.1), **is not
  implemented anywhere in the record**. Every executed $W^k$ is an ex-ante or
  smoothed stand-in (§6.1).

**When to switch to M as primary.** Adopt M + a finite $\kappa$ if and only if the
PI (i) wants the direct opportunity channel inside baseline $W^1$ and (ii) accepts
one of two things:
- external intensity information mapped to a household-level $\kappa_i$ (§4.2,
  §4.4 list); or
- presenting the $\kappa$-sensitivity band itself as the result, with an
  empty-set treatment chosen from (a)–(d). Treatment (e) cannot serve as a number.

M's theory status is then B, conditional on staying home not being a job in the
ability set (§2.6).

### 6.1 Theory identities versus implemented objects

Every identity in this note ($W^1_F\equiv W^4$, $W^1_M\equiv W^6$ over market jobs,
(M.1)–(M.4)) holds between **theory measures evaluated at the observed bundle
$z^{\rm obs}$**. None of the executed objects in the record is such a measure:

| theory object used here | executed counterpart in the record | how it differs |
|---|---|---|
| Measure 1 at $z^{\rm obs}$ (note (1.1), (M.1)) | W1-EA, `run_s12_welfare_record_v1.py:346–348` | The attained side is **ex ante**, $\log J=\mathrm{lse}(u+\text{op})$, not $u(z^{\rm obs})$. The reference is a log-sum-exp, and the result is a power mean of consumption (note §3.2, §6B) |
| Measure 4 at $z^{\rm obs}$ (F's collapse) | $W^4$, `run_s12_welfare_record_v1.py:355–356`; Stage-D `m08_welfare_measures.py:419, 476–483` | The attained side is the same ex-ante inclusive value less $\log(\#\text{nodes})$ (`V_actual = V_is − logS`), **not** $u(z^{\rm obs})$. It was scale-dependent until the unit-mass fix (note §3.2) |
| Measure 6 over $\mathcal J^{\rm mkt}$ (M at $\kappa=\infty$) | $W^6$, `m08_welfare_measures.py:295–303, 522–537` | A log-sum-exp **average** over a universal leisure grid less $\log n_J$: a smoothed stand-in for the minimum. The grid's domain (whether it includes $h=0$) was not checked |
| $W^1$ on the market-only reference (M) | working-only diagnostic, `run_s12_welfare_record_v1.py:351–352` | A log-sum-exp over working nodes with ex-ante attainment. This is the source of the ×4.29, which is why that figure does not transfer (§1.2) |

**Consequence.** The recommendation concerns **which theory object to implement**.
It does not license reading any existing $W^k$ number as that object. Choosing F
does not make the executed $W^4$ the F value of $W^1$. Implementing either mapping
at $z^{\rm obs}$ is new work, and the closed forms (1.1) and (M.4) are what it would
reproduce.

No welfare rerun, no decomposition rerun, no re-estimation, no set-size
normalisation, no repair of W1-EA. Stop.

---

## Appendix A — sources, paths, hashes

Repository heads at audit time: `Job_Market_paper` `834055e8da5573ae237f40d38229e836b6717270`;
`MNL` `aa36e816e46568ff448810e5b89c28ea616a2476`. At audit time `docs/normative/`
was untracked in `Job_Market_paper`; under r3 (REC-1) this document, the note it
builds on, `JMP_W1_fork_ruling_v1.md`, and the REC-1 script/CSV are all tracked
and committed on `docs/w1-reference-domain-fork`. This document's own commit hash
and file digest are recorded outside the file, to avoid pinning a file to its own
hash.

| object | path | sha256 |
|---|---|---|
| theory manuscript (authoritative) | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.tex` | `d8687d3cfb71ce00f81613286e784c71c0e643721987bebf0d57226afe2a02d1` |
| theorem index | `Job_Market_paper/Theory_other_project/jobs_and_wellbeing.agent.md` | `4940775b8b57ab5ec4278795d2fe7361de8119e2019f45fa3bbf8fce138f4c2a` |
| the note (starting point) | `Job_Market_paper/docs/normative/W1_latent_set_identification_note_v1.md` | `8b02ff93b94a72327caa8d16476a3bf5c6176894162e0758f03562ee6329e226` |
| S11 singles parameter table (accepted baseline, P1) | `MNL/experiments/JMP_SEMINAR_SPRINT/runs/s11_welfare_specs_of_record/s11_singles_parameter_table_v1.csv` | `cee4a136f9ce69753965beaa779753bed59e75972490ebb0f2b6114f790413ab` |
| S11 couples parameter table (accepted baseline, P1) | `…/s11_welfare_specs_of_record/s11_couples_parameter_table_v1.csv` | `fc1794b437c74ac4e6ab240aaa7c71b7c38ee21512395a175b38c785a5e061c9` |
| conventions and reference households (age centre/scale, age support 20–60, $\beta_\ell$ at reference, $C^{\rm obs}$) | `…/runs/preference_figures_final/pff_step1_reference_v1.json` | `594a941ebacad8e4b4462e464732199d836b8ca65c43a0679368e0c03375d41a` |
| hours support $h_{\min}=5$, $h_{\max}=70$ (`binding.spec_conventions`) | `…/runs/figE1_matched_households/e1_matched_households_v1.json` | `4dbb3e6abf918689a8027ed093ece2aeaf884d64fd2f25c9282cf3396a5c3454` |
| RURO source, Assumption 2 and Theorem 1 | `Job_Market_paper/Literature/markdowns/Dagsvik_Jia_2016.md` (l.42–51) | `29cf5975c22e40b4224408c48f7cf1f11c6f1d8412e2aff665bc4645ce9a804d` |
| Theory-talk script (history) | `Job_Market_paper/beamer/reference/Theory_talk/slides/spoken_script_click_cues.tex` (l.103–124) | `f07a475eeb1004d2c6cdbc3376289945f359eec424e9abf26141df44e9029236` |
| **REC-1 reproduction script** | `Job_Market_paper/docs/normative/scripts/fork_derived_numerals_v1.py` | `994c3dfaad7cbafd2f76871ac05629e0ee60947b5a00085f944a0bebe11d8e9c` |
| **REC-1 pass/fail table (158/158 pass)** | `Job_Market_paper/docs/normative/fork_derived_numerals_v1.csv` | `2677356a555ec3eb65623227e3d26363925c2d11add1112c8db925213f77bf8e` |
| Deputy FORK-1 implementation record | `Job_Market_paper/docs/normative/JMP_W1_fork_ruling_v1.md` | recorded outside the file with this commit's hash (pin-recursion rule) |

**P1, not used.** `MNL/experiments/JMP_SEMINAR_SPRINT/runs/couples_clean_baseline/r240_step3_parameter_table_v1.csv`
(sha256 `c4aee66a2adf8b08f1314913b52ee3c2218a7f5c0cd1b9c42f1ec82e4a21cc8c`) is the
provisional 2,275-couple R-240 table. It is **not** an input to this memo or to
the REC-1 script; it is recorded here only because MEASURE-MAP-1 (not accepted)
used it and reported a different couples threshold (5.52) as a result.

Manuscript line references used: l.97, 107, 111, 114, 124–127, 132–136, 140–144,
158–162, 198, 200–209, 225–229, 258–266, 306, 339–353 (table), 393–449 (thm:imp1),
547–595 (thm:w1), 838–869 (thm:w4).

## Appendix B — numbers derived here (CITABLE; reproduced by REC-1)

**Reproduced, 158/158, by `docs/normative/scripts/fork_derived_numerals_v1.py`
against `docs/normative/fork_derived_numerals_v1.csv` (hashes in the status
block above and in Appendix A).** All are arithmetic on the S11 tables with
$\ell=(80-h)/10$ and
$\mathcal B(z;\theta)=(z^\theta-1)/\theta$:
- the couples term-by-term table of §5.1: $\Delta\mathcal B$ = 0.008751 and
  0.002045, the threshold 4.2784, the peak ratio 3.33, and the age boundaries;
- every entry of Table 1;
- the reference-household rows in §1.2 (EUR values use the record's $C^{\rm obs}$:
  1,888.62, 1,859.06 and 4,204.29);
- the dense-law M/F gaps in §4.1;
- the couples values in §5 (reference $\beta_\ell^m=4.0686$, $\beta_\ell^f=12.8135$,
  $\beta_c=2.1017$; $\theta_\ell^m=-0.9761$, $\theta_\ell^f=-1.6863$; 0→5 h losses
  0.0356 and 0.0262);
- the $12\times C$ example in treatment (c), and the 12.1× and 5.6× ceilings in
  the analysis of (e).

The singles age endpoints use centre 42.7235 and scale 10 from the record. No
couples age support was located, so couples values are reported only at the block
minima and the reference household. Nothing was simulated, re-estimated or
normalised.

## Appendix C — revised header items (verbatim, PI, 2026-09-11)

```
2 Under theta_c = 0, m_i(j) = C_i^obs exp{[L_i(j^obs) - L_i(j)]/beta_c}.
  WORKER: j^obs in A_i^M, so W1_M = C_i^obs exp{[L_i(j^obs) -
  max_{A_i^M} L_i]/beta_c} <= C_i^obs, equality iff j^obs has the
  highest L in the realized market set.
  NONWORKER: z^obs = (C^obs, o), o notin A_i^M. Since L_i(o) > L_i(j)
  for all market j (W1AUDIT-1), m_i(j) > C_i^obs for every market j,
  so W1_M = C_i^obs exp{[L_i(o) - max_{A_i^M} L_i]/beta_c} > C_i^obs
  when A_i^M is non-empty. VERIFY THIS SIGN; the prior card stated
  it reversed.
  Pointwise check: A^M subset of A^M u {o} implies W1_M >= W1_F for
  every household; any violation is an error to report, not a finding.
  Bounds: state both from the estimated hours block. Lower bound:
  max_{A^M} L <= Lbar_i^M (sup over market hours support). Upper
  bound: a singleton set at the lowest-L market job.
5 Empty set: derive Pr(A_i^M = empty) under the stochastic foundation
  W1AUDIT-1 established (do not assume Poisson unless the model
  supports it). Observed employment conditions A^M non-empty for
  workers; report what is known for nonworkers. List principled
  treatments WITHOUT choosing, with what each assumes:
  (a) conditioning on non-emptiness;
  (b) W1_M on the non-empty event, reported with the empty event's mass;
  (c) assigning the observed bundle's own m;
  (d) the empty event as a distinct welfare state;
  (e) the formal convention min over empty set = +infinity, including
      its implication that a nonworker's W1_M rises without bound as
      the market set thins.
7 Intensity limits: if an unidentified scale kappa exists, derive
  W1_M as kappa -> infinity and kappa -> 0. State whether the
  kappa -> infinity limit (i) is identified, (ii) retains any direct
  access dispersion given the kernel's hours support, and (iii)
  coincides with an independence-of-A object. State whether kappa is
  common or household-specific under the model, and what external
  data would pin it.
```

Where each item is answered:
- item 2: §1.2 (sign, pointwise check, bounds; the upper-bound qualifier for
  workers);
- item 5: §3.1–§3.4 (treatment (e) analysed separately);
- item 7: §4.4.
