# Audoly, McGee, Ocampo & Paz-Pardo 2025 — A Practitioner's Note on the Shapley-Owen-Shorrocks Decomposition

> Source of truth: the attached PDF (FRBNY Staff Reports no. 1163, August 2025).
> All page references below are to that PDF. Claims are tagged
> **[explicit]** (stated in the source), **[analogy]** (derived by me, mapping to
> my JMP), or **[not-established]** (the source does not address it). `[verify]`
> marks anything I could not confirm directly in the PDF.

---

## 0. Metadata

- **BibTeX key:** `audoly_mcgee_ocampo_pazpardo_2025` `[verify exact key]`
- **Authors:** Richard Audoly (FRB New York); Rory McGee (UWO & IFS);
  Sergio Ocampo (UWO); Gonzalo Paz-Pardo (ECB). **[explicit, p. 2]**
- **Year:** 2025 (August). **[explicit, p. 2]**
- **Outlet:** Federal Reserve Bank of New York Staff Reports, no. 1163.
  **[explicit, p. 2]**
- **DOI/URL:** https://doi.org/10.59576/sr.1163 **[explicit, p. 2]**
- **PDF filename:** `Audoly_et_al_2025_A_Practitioner_s_Note_on_the_Shapley-Owen-Shorrocks_Decomposition.pdf`
- **Tier:** T1A.
- **JMP block(s) served:** **decomposition** (primary); secondarily
  **welfare** (the note explicitly flags welfare-decomposition-from-counterfactuals
  as an application, p. 9) and **methodology / data-infrastructure** (it ships a
  reference algorithm and Matlab implementation, pp. 4, 12). It does **not** serve
  estimation, identification, the opportunity mechanism, or normative
  interpretation. **[explicit + analogy]**
- **JEL / keywords (source's own):** JEL B4; keywords "decomposition,
  methodology." **[explicit, p. 2]**
- **Provenance:** the note previously appeared as an appendix to the authors'
  paper "The Life-Cycle Dynamics of Wealth Mobility." **[explicit, p. 2]**

---

## 1. One-paragraph relevance to my JMP

This is the methodological primitive behind my **headline three-way
access/ability/preference Shapley–Shorrocks decomposition of welfare
inequality**. It states, defines, and proves-by-property exactly the
decomposition I invoke when I write "Shapley–Shorrocks, order-independent,
exhausts total inequality": the four axioms (exact additivity, symmetry,
null-factor zeroing, linearity in the decomposed function) and the closed-form
weighted-permutation contribution formula. **[explicit, pp. 2–4]** It speaks to
**none** of my three economic channels directly — access, ability, and
preference are *my* economic labelling of the inputs; the note is channel-blind
and treats inputs as abstract "players." Its decisive contributions for me are
(i) the **Owen generalisation to unions of players**, which is the formal license
for my channels being *groups* of parameters (preference = 20 params, ability =
6, access = 23) rather than single inputs **[explicit, p. 3]**; and (ii) the
explicit statement that this machinery applies to a decomposed function that is
itself **a Gini coefficient or any sample transformation** **[explicit, p. 4]**,
which is precisely my $I(\Omega^k)$. It is a citation for *method validity and
order-independence*, not for any economic finding.

---

## 2. Data and setting

**N/A as a data paper.** The note has no dataset, no country, no sample unit,
no sample size, no estimation. **[explicit — it is a methodological note,
pp. 1–9]** Its examples are algebraic toy models (a linear three-variable model,
two nonlinear three-variable models, and an $R^2$ decomposition of a linear
regression), not empirical applications. **[explicit, pp. 4–8]**

**Transport to my France pooled 2015–2017 EUROMOD cross-section:** the *method*
transports completely and is setting-agnostic — it places **no** requirement on
panel structure, administrative match, instruments, or offer/vacancy data.
**[explicit by omission + analogy]** What it does **not** supply, and what I
therefore do not have from this source: any guidance on standard errors /
inference for the decomposition components (the note is silent on sampling
variability of the Shapley shares), and any treatment of *how* the inputs are
identified or estimated — it takes the function $f$ and its inputs as given.
**[not-established]** My cluster-robust bootstrap on `idorighh` and my synthetic-
recovery certification are entirely outside this note's scope.

---

## 3. Model and objects (map object-by-object to mine)

The note has **no structural labour-supply model, no choice set, no utility, no
opportunity mechanism, no budget map.** **[explicit]** It is one level of
abstraction above all of these: it decomposes an *arbitrary* function
$Y = f(X_1,\dots,X_n)$ into the contributions of its arguments. **[explicit,
p. 4]** Object-by-object:

- **Their "function $f$" ↔ my decomposed object.** For me, $f$ is the inequality
  index $I(\Omega^k)$ (a Gini) of the welfare distribution of measure $W^k$. The
  note explicitly licenses $f$ being "a transformation of the sample, for example
  the Gini coefficient." **[explicit, p. 4; analogy for the $W^k$ mapping]**
- **Their "arguments $X_j$" ↔ my channels.** For me the arguments are the
  *equalisation operations* on access, ability, and preference (each channel a
  *group* of structural parameters). The note's arguments are abstract inputs —
  "a variable, policy function, or price." **[explicit, p. 3]** The grouping is
  legitimised by the Owen union extension (§3, p. 3) — see §7.
- **Their "null value $\varnothing_j$" ↔ my "equalised-to-reference" state.** The
  note formalises sub-models by replacing absent arguments with a null value
  $\varnothing_j$, noting this can mean "setting some parameters to a
  predetermined value or excluding certain model components." **[explicit,
  footnote 2, p. 3]** In my design the "null"/baseline is the *equalised-to-
  reference-environment* state of a channel; this is a clean correspondence
  **[analogy]**, but note the difference: the note's canonical null is "zero"
  (zero regressor / zero parameter), whereas my null is "equalised to a reference
  distribution," not zero. The note's footnote 2 explicitly accommodates a
  predetermined non-zero null, so the mapping holds, but I must state my null
  state explicitly rather than inheriting "zero."

**Does any job attribute enter both utility and the opportunity mechanism?**
**N/A** — the note has no utility and no opportunity mechanism, so the
double-entry flag does not apply here. (This flag is for my structural sources;
this is a decomposition-method source.)

---

## 4. Estimation method

**N/A — no estimator, no likelihood, no choice-set construction, no proposal
density, no sampling-of-alternatives correction.** **[explicit]** The note's
"method" is a deterministic combinatorial formula evaluated over pre-computed
function values, not a statistical estimator.

**Verdict (reusable for my RURO/JAX pipeline?):** **Not applicable to the
estimation step.** The note is reusable for the **post-estimation decomposition
step only**. Concretely: after $\hat\theta$ is certified and the welfare layer
produces $\Omega_i^k$, the note's algorithm (p. 4) is the exact procedure that
turns "welfare distribution under each channel-equalisation sub-model" into the
additive access/ability/preference shares. Name the step: **decomposition
post-processing of $I(\Omega^k)$**, not estimation.

---

## 4b. Proposal / sampling-of-alternatives correction

**N/A.** **[explicit]** The note contains no alternative sampling, no proposal
density, no McFadden-style correction, and no log-prior. Its "sampling" language
(the $\frac{(n-k-1)!\,k!}{n!}$ weight interpreted as the probability of drawing a
particular sub-model of size $k$ when all model sizes are equally likely, p. 4)
is the **combinatorial averaging weight inside the Shapley formula** — a weighting
over *permutation orders of inputs*, **not** an importance-sampling correction over
choice alternatives. **Do not conflate** this weight with my $-\log\pi$ proposal
correction; they are unrelated objects that both happen to involve probabilities.
**[explicit + flag]**

---

## 5. Opportunity mechanism

**N/A.** **[explicit]** The note has **no** opportunity mechanism, no
feasibility/availability model, no offer probabilities, no reservation-wage or
participation restriction, no density over alternatives. It does not vary
anything with region, education, demographic type, or local labour market,
because it has no economic content of that kind.

**Cost of this omission for my access/ability/preference decomposition:** none
introduced by the note — the note is simply silent. The note supplies the
*aggregator* (how to attribute a non-linear outcome to grouped inputs); the
*economic content* of access, ability, and preference — and the decision that
occupation (`loc4`, ISCO) is an **access** object and never industry (`lindi`,
NACE) — comes entirely from my model and my welfare spec, not from here. The note
neither helps nor hinders the access/ability boundary; it only guarantees that
*whatever* grouping I choose, the resulting shares are additive, symmetric, and
exhaustive.

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**The note does not compute welfare and does not contain any equivalent-income,
money-metric, EV/CV, or inclusive-value object of its own.** **[explicit]** It
therefore has **no** position on my $W^1$–$W^6$ family, and **does not contain
$W^1$–$W^6$** in any form. `[explicit — the $W^1$–$W^6$ family is my/Haydar–
Maniquet content, wholly absent here]`

**What the note does say about welfare** (and the *only* thing it says):
in the Summary (p. 9) it observes that the decomposition "can also be useful in
the context of welfare decompositions from counterfactual exercises," citing
Flodén (2001) and Conesa–Kitao–Krueger (2009) as exercises that **separate the
roles of changes in the aggregate level and distributions of consumption and
leisure for welfare**, and Moschini–Tran Xuan (2025) extending these to separate
gains from redistribution over the life cycle and across generations. It notes
such welfare decompositions are in general **order-dependent**, and that the
symmetry of Shapley-Owen-Shorrocks "can therefore enhance the interpretability of
welfare decompositions at little additional cost." **[explicit, p. 9]** This is a
**motivating pointer**, not a worked welfare construction.

**Verdict:** for the welfare *object* — **incompatible / inapplicable** (the note
has no welfare object). For my welfare-*inequality decomposition* — **directly
usable as the aggregator**: it is the formal warrant that my channel shares of
$I(\Omega^k)$ are well-defined and order-independent.

---

## 6b. Inclusive value and money-metric inversion

**N/A.** **[explicit]** The note uses no inclusive value / log-sum, no EV/CV, no
own-utility inversion, and takes no expectation over extreme-value shocks
(analytically or by simulation). None of my analytic-in-shocks importance-sampling
inversion machinery has any counterpart here. Do not cite this note for anything
about the inclusive value or money-metric inversion.

---

## 7. Inequality / decomposition content  [the core of this source]

This is the substance the note exists to deliver. **[explicit, pp. 2–9]**

- **Decomposition rule:** **Shapley-Owen-Shorrocks** — the Shapley value
  (Shapley 1953) for attributing a non-linear aggregate to its inputs, extended to
  *inequality* decomposition by Shorrocks (1999, 2013), and to *unions/groups of
  players* by Owen (1977). **[explicit, pp. 2–3]**
- **Inequality index:** **index-agnostic.** The note does not privilege Gini, MLD,
  Theil, etc.; it states the decomposed function $f$ can be "the Gini coefficient"
  or any sample transformation. **[explicit, p. 4]** → My choice of Gini for
  $I(\Omega^k)$ is fully supported, and so would MLD/Theil be.
- **The four characterising properties** (the note's central formal claim; it
  asserts the decomposition is the **unique** decomposition satisfying all four):
  **[explicit, pp. 4–5]**
  1. **Exact decomposition under addition** — $\sum_{j=1}^n C_j = f(X_1,\dots,X_n)$
     (eq. 1, p. 4), so $C_j/f(\cdot)$ is the share attributable to $X_j$
     (interpretable as a proportion *as long as $f$ is non-negative*; the note
     flags that with negative $f$, components can be $C_j<0$ and the share reading
     can mislead — footnote 1, p. 5). **[explicit]**
  2. **Symmetry w.r.t. argument order** — the order in which $X_j$ is removed does
     not alter $C_j$. **[explicit, p. 5]** *This is the property I invoke as
     "order-independent."*
  3. **Null-factor zeroing (irrelevance normalisation)** — a factor that never
     changes the outcome gets $C_j=0$. **[explicit, p. 5]**
  4. **Linearity of the attribution operator in the decomposed function** — a
     closure requirement implying contributions rescale linearly with the outcome.
     **[explicit, p. 5]**
- **Closed-form contribution (eq. 2, p. 5):**
  $$
  C_j=\sum_{k=0}^{n-1}\frac{(n-k-1)!\,k!}{n!}
  \sum_{\substack{s\subseteq S_k\setminus\{X_j\}:\,|s|=k}}
  \big[f(s\cup\{X_j\})-f(s)\big].
  $$
  **[explicit]** The weight $\frac{(n-k-1)!\,k!}{n!}$ is the probability that a
  size-$k$ sub-model is selected when all model sizes are equally likely; this
  weighting is what delivers symmetry. **[explicit, pp. 5, 8]**
- **Counterfactual / "zeroing-out" construction:** each input is included or
  excluded across all $2^n$ sub-models; an excluded input is set to its **null
  value $\varnothing_j$** (zero regressor/parameter in the regression examples, or
  "setting some parameters to a predetermined value or excluding certain model
  components" in structural models — footnote 2, p. 3). The decomposition is
  additive **relative to the null model** (the all-excluded reference): the
  worked nonlinear example shows the intercept $\beta_0$ drops out, i.e. the
  decomposition recovers $f(X_1,X_2,X_3)-f(\varnothing_1,\varnothing_2,\varnothing_3)$,
  **not** the level including the null-model value. **[explicit, pp. 6–7]** For the
  $R^2$ example the null model has $R^2(\varnothing)=0$, so there the
  decomposition recovers the *full* $R^2$ level. **[explicit, p. 8]**
  → **Design consequence for me:** my reported channel shares sum to
  $I(\Omega^k)-I(\text{null/all-equalised})$, **not** to $I(\Omega^k)$ outright,
  unless my all-channels-equalised state has zero inequality. I must declare what
  my "all-equalised" reference produces and whether my exhaustiveness gate targets
  $I(\Omega^k)$ or $I(\Omega^k)-I(\text{reference})$. The note makes this reference
  dependence explicit and is the right citation for stating it.
- **Owen grouping (decisive for my three channels):** the same concept applies
  "when a group of inputs moves together, as is the case when changing all prices
  or initial conditions in counterfactuals," via Owen's (1977) generalisation to
  unions of players. **[explicit, p. 3]** The Summary adds that **judiciously
  grouping factors can minimise the computational cost**, which grows
  substantially with the number of factors. **[explicit, p. 9]** → This is the
  formal warrant for treating preference / ability / access as three *grouped*
  players rather than ~47 individual parameters, and the practical argument for
  doing so (cost $\sim 2^n$).
- **Cost:** $2^n$ sub-model evaluations; the note states the cost "grows
  substantially with the number of factors" and recommends grouping to contain it.
  **[explicit, pp. 8–9]** → With $n=3$ channels this is $2^3=8$ welfare-distribution
  evaluations per measure, trivial; the $n$ that matters for me is the channel
  count, not the parameter count, *because* of Owen grouping.

**Verdict (reusable for my three-way access/ability/preference split anchored on
$W^3$/$W^5$/$W^1$?):** **Yes, directly.** This note *is* the method I cite for
that split. It is **not two-way** and imposes no two-way restriction — it is
$n$-ary and group-aware, so it accommodates three channels natively with **no
extension required**. (Contrast: a source that only did factor-component or a
two-way opportunity-vs-preference cut would need extending; this one does not.)

---

## 8. Identification and the separation of preferences from opportunities

**N/A — and important to state plainly.** **[explicit]** The note contributes
**nothing** to identification. It assumes the inputs $X_j$ and the function $f$
are already given, and says nothing about what identifies tastes vs constraints,
nor about distinguishing ability from access. The clean separation of preference
from opportunity, and of ability from access, is an **identifying normative and
econometric assumption made in my model and welfare spec** (the parameter-to-
channel membership table), **not** something this note supplies or validates.

**Defence against the "your decomposition is mechanical" referee — what this note
does and does not buy me.** It buys me that, *given* a channel partition, the
attribution is the unique additive, symmetric, exhaustive one — so the referee
cannot attack the *aggregation rule* as arbitrary or order-dependent. It does
**not** buy me the *channel partition itself*: the note is explicit that
contributions are defined relative to a chosen null and chosen inputs, so a
referee can still legitimately contest *which parameters are access vs ability vs
preference* and *what the equalised reference is*. That contest is mine to win
with the model and the synthetic-recovery argument, not with this citation. **Do
not oversell this note as resolving the mechanicalness critique — it resolves only
the order-dependence half of it.** **[explicit + analogy]**

---

## 9. Key results and magnitudes

**No empirical magnitudes** — the note reports no elasticities, welfare effects,
opportunity shares, or decomposition shares from data. **[explicit]** Its
"results" are algebraic identities from the toy examples, useful only as
worked checks:

- **Linear model** $Y=\beta_1X_1+\beta_2X_2+\beta_3X_3$: $C_j=\beta_jX_j$ exactly;
  order is irrelevant; the Shapley decomposition coincides with the usual
  regression decomposition. **[explicit, pp. 6–7]**
- **Nonlinear example I** $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3X_2$:
  $C_1=\beta_1X_1$ (linear entrant), and the interaction term is **split evenly** —
  $C_2=\beta_2X_2+\tfrac12\beta_3X_2X_3$, $C_3=\tfrac12\beta_3X_2X_3$. The intuition
  the note draws: $\beta_2X_2$ appears in all sub-models (probability 1 of
  appearing), the interaction $\beta_3X_2X_3$ appears in 2 of 4 (probability
  $\tfrac12$); weighting by probability of appearance enforces symmetry.
  **[explicit, pp. 6–9; eqs. 7–8]** → **This is the single most useful takeaway for
  my decomposition's interpretation:** interaction effects between channels are
  **shared equally** between the interacting channels, not assigned to one. So any
  access×ability or preference×access interaction in my welfare inequality is
  split 50/50 between the two channels involved — I should expect and report this,
  not be surprised by it.
- **$R^2$ example:** decomposing $R^2=\mathrm{SSE}/\mathrm{SST}$ of a linear
  regression is a **nonlinear** decomposition even though the model is linear; the
  null model gives $R^2(\varnothing)=0$ so the components recover the full $R^2$;
  the Shapley $R^2$ differs from the standard **partial $R^2$**, and the partial
  $R^2$ fails the exact-decomposition requirement and (applied iteratively) the
  symmetry requirement. **[explicit, pp. 7–8, 11; eqs. 11–16]**

**Benchmarking my own numbers:** the note offers no external benchmark for the
plausibility of my opportunity share or welfare spread. **[not-established]**

---

## 10. Estimators, theorems, or formal results

**Result R1 — uniqueness of the Shapley-Owen-Shorrocks decomposition.**
*Statement (near-verbatim, p. 4):* the decomposition is "the unique decomposition
satisfying four important properties" — (i) exact additivity
$\sum_{j=1}^n C_j=f(X_1,\dots,X_n)$; (ii) symmetry in argument order; (iii) zero
contribution to null-effect factors; (iv) linearity of the attribution operator
in the decomposed function. **[explicit]**
*Assumptions:* a function $f$ with a well-defined null value $\varnothing_j$ for
each argument; finite input set. **[explicit, footnote 2]**
*Technique (bullets):*
- treat each input as a player, the outcome as the surplus of the coalition;
- average the marginal contribution $f(s\cup\{X_j\})-f(s)$ over all sub-models $s$
  not containing $j$;
- weight each sub-model size $k$ by $\frac{(n-k-1)!\,k!}{n!}$ (equal probability
  over model sizes), which enforces symmetry;
- Owen (1977) extends the same averaging to unions of players (groups).
*Verdict (reusability):* **Yes** for my **decomposition layer** — this is the
theorem I cite for additivity + order-independence + exhaustiveness of the
access/ability/preference shares. **No** for my estimation or welfare-inversion
layers (out of scope).

**Result R2 — closed-form contribution (eq. 2, p. 5).** Statement reproduced in
§7. *Reusability:* **Yes** — directly implementable; for $n=3$ channels it is the
8-row sub-model enumeration. The note ships a **Matlab reference implementation**
(`shapley_owen_shorrocks(X_ind, f_vals)`, p. 12) taking a binary $2^n\times n$
sub-model indicator matrix and a $2^n$ vector of function values, returning the
$n\times1$ contribution vector. **[explicit]** → I should port this to
Python/JAX as my decomposition post-processor and unit-test it against the note's
toy examples (linear → $C_j=\beta_jX_j$; nonlinear I → the half-split) as exact
recovery checks. **[analogy — porting/test plan is mine, not the note's]**

**Algorithm A1 — the SOS algorithm (p. 4).** For each input $j$: initialise
$C(j)=0$; loop sub-model sizes $k=0,\dots,n-1$; weight $\omega_k=\frac{(n-k-1)!\,k!}{n!}$;
find rows with $k$ inputs excluding $j$; accumulate
$C(j)\mathrel{+}=\omega_k\,[F(s\cup\{j\})-F(s)]$. **[explicit]** *Reusability:*
**Yes**, this is the spec for my implementation.

---

## 11. Robustness and specification sensitivity

The note's relevant "robustness" content is methodological, not empirical:

- **Reference/null-state dependence.** The decomposition is additive *relative to
  the null model*; what the components sum to depends on the null
  ($f(\cdot)-f(\varnothing)$ in nonlinear example I; full level in the $R^2$ case
  where $f(\varnothing)=0$). **[explicit, pp. 7–8]** → My robustness section must
  report sensitivity to the **equalised-reference definition** (my null), exactly
  the cut my welfare spec flags (e.g. education-as-access vs education-as-ability
  re-allocation; pinned-preference held-vs-swapped). The note is the citation for
  *why* this matters formally.
- **Grouping choice.** Because cost is $2^n$ and grouping is legitimate (Owen),
  *how* I group parameters into channels is a specification choice with both
  cost and interpretation consequences. **[explicit, pp. 3, 9]** → Robustness to
  the ability/access boundary (my §6.3 deferred re-allocation) is a *grouping*
  robustness in this note's language.
- **Order-robustness as the selling point vs alternatives.** The note praises
  Nakajima–Telyukova (2020) for providing robustness to alternative elimination
  orders, and criticises decompositions that report only one order (De Nardi et
  al. 2025) or are non-additive. **[explicit, p. 9]** → This is my argument for
  choosing SOS over a single-order "zero-out" decomposition in the first place.

What it does **not** tell me to stress-test: choice-set size, number of draws,
number of starts, opportunity-set definitions, circumstance partitions — all
**out of scope** (no structural model here). **[not-established]**

---

## 12. What I can cite this paper for

- The **definition and four characterising axioms** of the
  Shapley-Owen-Shorrocks decomposition, and its **uniqueness** as the
  decomposition satisfying them (additivity, symmetry/order-independence,
  null-factor zeroing, linearity). **[explicit, pp. 4–5]**
- The **closed-form contribution formula** (eq. 2) and the **algorithm**
  (p. 4) I implement. **[explicit]**
- That the decomposed function $f$ **may be a Gini coefficient or any sample
  transformation** — i.e. that decomposing $I(\Omega^k)$ is a legitimate use.
  **[explicit, p. 4]**
- The **Owen (1977) union/grouping extension**: the formal license to decompose
  **groups of inputs that move together** (my preference/ability/access channels),
  and the practical point that **grouping contains the $2^n$ cost**. **[explicit,
  pp. 3, 9]**
- That **interaction effects are split symmetrically** between interacting inputs
  (the half-split in nonlinear example I). **[explicit, pp. 6–9]**
- That the decomposition is **additive relative to a declared null/reference
  state**, with the components summing to $f(\cdot)-f(\varnothing)$. **[explicit,
  pp. 7–8]**
- That **Shapley-Owen-Shorrocks is well-suited to welfare decompositions from
  counterfactual exercises**, where single-order eliminations are otherwise
  order-dependent (citing Flodén 2001; Conesa–Kitao–Krueger 2009;
  Moschini–Tran Xuan 2025). **[explicit, p. 9]**
- The **distinction from partial $R^2$** (Shapley $R^2 \ne$ partial $R^2$; partial
  $R^2$ violates exactness and, iterated, symmetry) — useful if a referee proposes
  a partial/sequential alternative. **[explicit, pp. 7–8, 11]**
- As a **recent, practitioner-facing secondary citation** for the method,
  alongside the **primary** Shorrocks (1999, 2013) and the game-theoretic roots
  Shapley (1953) / Owen (1977). **[explicit, references pp. 10–11]**

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Not** for any **economic finding, magnitude, elasticity, welfare effect, or
  opportunity share** — it reports none. **[explicit]**
- **Not** as a source of the **access/ability/preference channels** themselves,
  nor of any opportunity/preference economics — it is channel-blind; the channels
  are my model's content. Do not let the note's authority bleed into the channel
  partition.
- **Not** for **identification** of preferences vs opportunities, or ability vs
  access — silent on all of it (§8). Do not cite it against the "mechanical
  decomposition" referee on the *partition* question; it answers only the
  *order-dependence* question.
- **Not** for **inference / standard errors** on the decomposition shares — the
  note gives no sampling theory for the Shapley components. My cluster-robust
  bootstrap is unsupported by this source.
- **Not** for any **welfare object** ($W^1$–$W^6$, equivalent income, EV/CV,
  inclusive value, money-metric inversion). The note **does not contain
  $W^1$–$W^6$** and constructs no welfare metric; its welfare relevance is a
  one-paragraph pointer (p. 9), not a construction.
- **Boundary flags:**
  - **Two-way vs three-way:** N/A as a limitation here — the note is $n$-ary, so
    it does *not* impose a two-way structure; do not describe it as a two-factor
    method.
  - **Ex-post / universal-set welfare:** N/A — no welfare object to mischaracterise.
  - **"Sectoral"/industry language:** the note never mentions occupation or
    industry; do not import its "inputs/players" abstraction as if it endorsed
    occupation-as-access. The occupation (`loc4`, ISCO) vs industry (`lindi`,
    NACE) distinction is entirely mine.
  - **Random vs deterministic opportunities:** the note's probability language is
    the **permutation-order weight** inside the Shapley formula, **not** any claim
    about random opportunities. Do not read it as bearing on the random-vs-
    deterministic-opportunity framing.
  - **Theory-paper boundary:** trivially respected — the note is unrelated to the
    Haydar–Maniquet axioms; never let "uniqueness/characterisation" language in
    *this* note be confused with the companion paper's *welfare-measure*
    characterisation. They are different objects (a decomposition operator vs a
    family of welfare measures).

---

## 14. Direct quotes worth citing

Short, exact, verbatim, with page numbers (each ≤ 1 quote per use, kept brief):

1. p. 4: "the order in which the arguments are removed matters in general for the
   decomposition." `[verify exact wording — p. 4]`
2. p. 5: "Symmetry with respect to the order of the arguments." (property heading)
   **[explicit]**
3. p. 4: the decomposition "can be ... the Gini coefficient." `[verify exact
   wording — p. 4]`
4. p. 3: "the same concept applies when a group of inputs moves together."
   `[verify exact wording — p. 3]`
5. p. 9: the symmetry of the decomposition "can therefore enhance the
   interpretability of welfare decompositions at little additional cost."
   `[verify exact wording — p. 9]`

> I have paraphrased rather than transcribed long passages; the five above are
> short fragments. Verify each against the PDF before quoting in the draft.

---

## 15. Open questions and risks for my draft

- **Null/reference state must be declared.** The note makes the decomposition
  reference-dependent (sums to $f(\cdot)-f(\varnothing)$). My draft must state what
  the all-channels-equalised welfare inequality is and whether my exhaustiveness
  gate targets $I(\Omega^k)$ or $I(\Omega^k)-I(\text{reference})$. Leaving this
  implicit is a referee opening.
- **Inference gap is mine to fill.** The note gives no variance theory for the
  shares; my cluster-robust bootstrap on `idorighh` is the right instrument but
  cannot cite this note for it. Budget the bootstrap cost (it scales with the
  measure menu × the $2^n$ sub-models).
- **Interaction-splitting must be communicated.** Because cross-channel
  interactions are split 50/50, a reader expecting interactions assigned to "the
  opportunity side" will misread the shares. Pre-empt this in the decomposition
  section.
- **Grouping is a specification choice, not a neutral act.** The ability/access
  boundary (education-as-ability vs education-as-access) changes the *grouping*
  and hence the shares; the note frames this as legitimate but consequential.
  Tie my §6.3 re-allocation robustness to this explicitly.
- **Non-negativity caveat (footnote 1, p. 5).** Share interpretation $C_j/f$ is
  clean only for non-negative $f$. A Gini is non-negative, so this is satisfied for
  $I(\Omega^k)$; but if I ever decompose a *signed* welfare gap, components can go
  negative and the proportion reading breaks. Note this where relevant.

---

## 16. TL;DR for retrieval

A FRBNY practitioner note (Audoly–McGee–Ocampo–Paz-Pardo 2025) that defines the
**Shapley-Owen-Shorrocks decomposition** of an arbitrary non-linear function into
additive, order-independent, exhaustive contributions of its inputs — the exact
method I cite for my **three-way access/ability/preference** decomposition of
welfare-inequality $I(\Omega^k)$, with the **Owen union extension** licensing
*grouped* channels and bounding the $2^n$ cost. It carries **no economic content,
no welfare object, no $W^1$–$W^6$, no identification, and no inference theory** —
it informs the **decomposition aggregator only**, supplying the uniqueness axioms
(eq. 1), the contribution formula (eq. 2), a Matlab reference implementation, and
the key interpretive facts (interactions split symmetrically; additivity is
relative to a declared null). It speaks to **none** of the access/ability/
preference channels economically and bears on **no** welfare measure; its sole
welfare relevance is a one-paragraph pointer (p. 9) that SOS improves the
interpretability of order-dependent counterfactual welfare decompositions.
