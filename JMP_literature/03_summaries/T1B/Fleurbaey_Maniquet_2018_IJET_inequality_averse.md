# Fleurbaey & Maniquet 2018 — Inequality-averse well-being measurement

> Extraction produced under `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> Source of truth: the attached PDF (*International Journal of Economic Theory*
> 14 (2018) 35–50). Where the source does not establish something, it is marked
> `[verify]` or stated as **not-established**. Tags used throughout:
> **[explicit]** = stated in the PDF; **[analogy]** = my mapping to the JMP, not
> in the source; **[not-established]** = the source does not contain it.
> This is for the empirical JMP; it is **not** the companion Haydar–Maniquet
> theory paper, and this Fleurbaey–Maniquet paper is a third, separate object.

---

## 0. Metadata

- **BibTeX key:** `FleurbaeyManiquet2018` [verify exact key in your `.bib`]
- **Authors:** Marc Fleurbaey (Princeton University); François Maniquet (CORE, Université Catholique de Louvain). **[explicit]**
- **Year:** 2018 (accepted 28 May 2017). **[explicit]**
- **Outlet:** *International Journal of Economic Theory* 14 (2018), pp. 35–50. **[explicit]**
- **DOI:** 10.1111/ijet.12140. **[explicit, from header]**
- **PDF filename:** `Fleurbaey_maniquet_2018.pdf`
- **Tier:** T1B (core, normative-foundations supporting; not the empirical-estimation core).
- **JMP block(s) served:** **welfare** (primary) and **normative-interpretation** (primary); it supplies the *axiomatic foundation* for the money-metric measure used as the JMP welfare object, and a second admissible measure (ray utility). It does **not** serve estimation, identification, decomposition, opportunity-mechanism (access/ability), or data-infrastructure.

---

## 1. One-paragraph relevance to my JMP

This is the paper that *characterises* the money-metric utility as a well-being measure from fairness/transfer axioms, which is exactly the normative warrant my JMP needs for using a preference-respecting money-metric equivalent income as its welfare object. **[explicit]** It shows that imposing **infimum nested contour** plus a transfer principle (**diminishing priority**) pins the reference preferences down to *linear* preferences, so that the well-being measure is (a strictly concave transform of) the money-metric utility $W^p$; an alternative axiom combination pins down the *ray utility* $W^\ell$ instead. **[explicit]** It speaks to **none** of my three structural channels (access / ability / preference) directly — it has no labour supply, no jobs, no opportunity set, no econometrics — but it speaks to the *measurement core* that all six of my $W^1$–$W^6$ measures share: the "respect individual preferences" requirement and the money-metric construction. **[analogy for the channel mapping; explicit for the characterisation]** Its function in my paper is as a cited primitive justifying the money-metric reference-price construction; **it is not the companion theory paper and does not contain my $W^1$–$W^6$ family.** **[explicit: it characterises $W^p$ and $W^\ell$, two measures, not a six-member labour-jobs family]**

---

## 2. Data and setting

**N/A — this is a pure axiomatic theory paper.** **[explicit]** There is no country, year, dataset, sample unit, sample size, or budget-set construction. The "setting" is an abstract consumption model: $K$ divisible goods, consumption set $X = \mathbb{R}^K_+$, and a domain $\mathcal R$ of continuous, convex, monotonic preference orderings. **[explicit, p. 36]**

Does the setting transport to my France pooled 2015–2017 EUROMOD cross-section? **Not as data** — there is nothing empirical to transport. **As a measurement primitive, yes:** the money-metric measure it characterises is defined over commodity bundles $x$ and an ordinal preference $R$, which maps onto my (consumption, leisure) bundles and estimated household preference. **[analogy]** Features the paper assumes that I must supply elsewhere: **(i)** divisible goods with monotonic preferences (my leisure dimension is bounded and my discrete-choice setting is not divisible-commodity — the authors themselves flag bounded/leisure dimensions as outside their model, see §15); **(ii)** a reference price vector $p$ (my reference-price / reference-set choice); **(iii)** there is **no** panel, administrative match, instrument, or vacancy/offer data because there is no data at all. **[explicit on (i) and (ii); the absence of empirics is explicit]**

---

## 3. Model and objects (map object-by-object to mine)

| My object | Their counterpart | Match? |
|---|---|---|
| Latent-jobs choice set $\mathcal C_i$ | none — they have an abstract bundle space $X=\mathbb R^K_+$, no choice set over jobs | **No counterpart** [explicit] |
| Preference utility $v$ (Box–Cox over $c,\ell$) | ordinal preference ordering $R\in\mathcal R$ (continuous, convex, monotonic) | Partial: same role (respect-preferences), but theirs is fully general ordinal, mine is parametric Box–Cox [explicit/analogy] |
| Opportunity density $g$ (hours / wage / market / occupation) | **none** | **No counterpart — they have no availability/opportunity mechanism at all** [explicit] |
| EUROMOD disposable-income budget map | a reference price vector $p$ used only to define $W^p$ | Different role: $p$ is a normative reference, not an empirical budget [explicit] |
| My welfare measure $W^k$ | their $W$, characterised as $W^p$ (money-metric) or $W^\ell$ (ray) | Their $W^p$ = the *core* my $W^k$ family is built on [explicit for $W^p$; the family extension is mine, analogy] |

The deterministic-utility ↔ preference-respecting requirement is **explicit and central**: they require $x\,R\,x' \Leftrightarrow W(x,R)\ge W(x',R)$ (respect of individual preferences). **[explicit, p. 36]** They have **no** opportunity / availability mechanism, so there is nothing to separate into hours / wage(ability) / market / occupation channels. **[explicit]**

**Flag — does any attribute enter both utility and the opportunity mechanism?** **N/A** — there is no opportunity mechanism in this paper, so the double-entry concern cannot arise here. **[explicit]** (This is one of the things the paper *cannot* speak to, recorded in §13.)

---

## 4. Estimation method

**N/A — there is no estimator, no likelihood, no choice-set construction, no sampling, no numerical optimisation.** **[explicit]** The paper's "method" is axiomatic characterisation: it states axioms (transfer + nested-contour properties) and proves which functional forms satisfy them.

**Verdict: not reusable for my RURO/JAX estimation pipeline.** It contributes nothing to estimation; its contribution is entirely to the welfare-object definition (§6). **[explicit]**

---

## 4b. Proposal / sampling-of-alternatives correction

**N/A.** There is no sampling of alternatives, no proposal density, and therefore no $\log(\text{prior})$ correction in this paper. **[explicit]** The paper has no importance-sampling or Monte-Carlo content of any kind; it is closed-form axiomatic theory. My proposal-individualisation concern has no analogue here.

---

## 5. Opportunity mechanism  [MOST IMPORTANT — but absent here]

**There is no explicit opportunity mechanism in this paper, and no implicit one either.** **[explicit]** The well-being measure $W(x,R)$ is defined on a single consumed bundle $x$ and a preference ordering $R$; it does **not** depend on a feasible set, an availability density, offer probabilities, a reservation wage, or local labour-market conditions. The authors state explicitly that $W$ "does not depend on any additional data" beyond the ordinal preference. **[explicit, p. 36]**

- **access** (hours / market-participation / region / year / occupation offers): **no counterpart.** **[explicit]**
- **ability** (wage technology, returns to education/experience, residual productivity): **no counterpart.** **[explicit]**
- **occupation** as availability vs. something else: **not present**; no occupation, sector, or industry object appears, so there is **no** sector/industry conflation to flag. **[explicit]**

**Cost of this omission for my decomposition (what to record):** this paper justifies *how to convert an attained bundle to a money figure under respect-of-preferences*, but it is silent on *where the attained bundle comes from* and on *what the feasible set was*. My access/ability/preference decomposition therefore cannot draw any feasible-set structure from this paper — it must come from the RURO opportunity layer (Aaberge–Colombino–Strøm 1999, Dagsvik, etc.). What this paper *does* give the decomposition is the legitimacy of the money-metric measure being decomposed. **[analogy]**

---

## 6. Welfare object — and its place on my $W^1$–$W^6$ map

**Does the paper compute welfare?** It does not *compute* anything numerically; it *characterises* well-being measures. **[explicit]**

**Type:** the two characterised measures are
- **Money-metric utility $W^p$**: $W^p(x,R)=w \Leftrightarrow x\, I\, \max(R,\{x'\in X \mid p x'\le w\})$ — i.e. the income $w$ that, at reference prices $p$, buys a bundle indifferent to $x$ under $R$. This is the minimal expenditure at reference prices $p$ to reach the satisfaction of $x$. **[explicit, pp. 42–43]**
- **Ray utility $W^\ell$**: $W^\ell(x,R)=w \Leftrightarrow x\, I\, w\ell$ — i.e. the scalar multiple $w$ of a reference bundle $\ell$ to which $x$ is indifferent. **[explicit, p. 44]**

Both are **reference-based, preference-respecting** money-metric-type objects; neither is an expected-maximum / log-sum / inclusive-value object, and neither is a discrete-choice CV/EV. **[explicit — the paper is in a divisible-goods, deterministic-bundle world; there are no shocks, no log-sums]**

**Defined over a universal or a constrained feasible set?** Over a single consumed bundle $x\in X$ (the whole orthant), evaluated against a **reference price vector $p$** (for $W^p$) or a **reference bundle/ray $\ell$** (for $W^\ell$). There is **no** feasible-set restriction, so it is neither "universal-set" nor "constrained-feasible-set" in my sense; it is bundle-and-reference based. **[explicit]**

**Reference used:** for $W^p$, a price vector $p\in\text{interior}[S^{K-1}]$ (the simplex); for $W^\ell$, a bundle $\ell\in\text{interior}[X]$. **[explicit]**

**Discrete-choice subtleties (log-sum, chosen-alternative selection, Hicksian/Marshallian, integration over heterogeneity, ex-ante/ex-post):** **none handled — none arise.** The paper has no discrete choice and no stochastic component, so ex-ante vs. ex-post does not appear. **[explicit / not-established by construction]**

**Locate on my $W^1$–$W^6$ map:**
- The **money-metric core** $W^p$ is the construction underlying *all six* of my measures, which are equivalent-income objects converting attained utility to money under own preferences. **[analogy — the link is in my welfare spec, not in this paper]**
- This paper does **not** contain or imply my access-vs-ability (Ind-$y$/Ind-$A$) classification, and does **not** contain $W^1$–$W^6$. It characterises *two* measures ($W^p$, $W^\ell$); the labelling $W^1,\dots,W^6$ and the compensation–responsibility spectrum are objects of my welfare spec / the companion theory paper, **not** this paper. **[explicit: do not attribute the six-measure family here]**

**Verdict:** **directly usable** as the axiomatic justification for the money-metric reference-price form of the welfare core; **adaptable** for the ray-utility alternative if I want a second admissible reference; **incompatible** as-is with the discrete-choice, ex-ante, feasible-set machinery (it must be paired with the RURO inclusive-value construction, which this paper does not provide). **[explicit / analogy]**

---

## 6b. Inclusive value and money-metric inversion

**Inclusive value (log-sum / expected maximum):** **not used.** **[explicit]** The paper has no extreme-value shocks and no expectation over a choice set.

**Money-metric inversion:** the money-metric measure $W^p$ is *defined* by an indifference condition — the money $w$ such that $x$ is indifferent to the $R$-best affordable bundle on the budget $\{x' : p x' \le w\}$. **[explicit, p. 43]** This is a reference-price expenditure-minimisation construction, i.e. conceptually a one-dimensional "what income reaches this satisfaction" object — which is exactly the *shape* of my one-dimensional bracketing root-solve. **[analogy — the paper states the indifference definition; the numerical inversion is mine]** The paper does **not** invert against an *own-utility map evaluated at an inclusive value*; there is no inclusive value here. The expectation-over-shocks question is **N/A** (no shocks). **[explicit]**

---

## 7. Inequality / decomposition content  [three-way where relevant]

**No inequality index, no decomposition rule, no counterfactual construction.** **[explicit]** The paper is about *measure characterisation*, not about decomposing measured inequality.

It does, however, engage **inequality aversion at the measurement level**: the transfer axioms (nested priority, diminishing priority, weak diminishing priority) encode resource inequality aversion as a property of the *measure*, motivated by the requirement that an egalitarian aggregator give priority to the worse-off. **[explicit, §3, pp. 39–41]** The explicitly stated aggregation result is only that the characterised measures are *intended to be arguments of social welfare functions*, and that the precise aggregation is left outside the analysis. **[explicit, p. 37]**

**Verdict for my three-way access/ability/preference Shapley–Shorrocks split:** **not reusable as a decomposition** — there is no Shapley, Shorrocks, factor, subgroup, or RIF content. What it does is *upstream* of my decomposition: it tells me the *measure* I decompose can be made inequality-averse (a concave transform $g\circ W^p$) and remains preference-respecting. The paper is not even a two-way decomposition; it is **zero-way** (no decomposition at all). To connect to my three channels it would have to be combined with an entirely separate opportunity model and a separate decomposition apparatus. **[explicit]**

---

## 8. Identification and the separation of preferences from opportunities  [STRICT]

**N/A in the econometric sense — there is no identification problem here, no data, no estimator, and no preferences-vs-opportunities separation.** **[explicit]**

The relevant "separation" the paper *does* make is conceptual and bears recording for my identification note: the well-being measure uses **only the ordinal preference $R$**, discarding any cardinal subjective-well-being information $U$ that represents the same ordering. The authors prove (via continuity + nested contour) that if data recorded $W(x,U)$, the axioms would force $W$ to depend on $U$ only through the ordering $R$. **[explicit, pp. 38–39]** This supports my "preference-respecting, ordinal-preference-only" stance against a referee who wants cardinal utility comparisons, but it says **nothing** about identifying tastes from constraints — because there are no constraints in the model. **Does it transport to my France pooled cross-section (no panel, no instrument)?** The *measurement* stance transports (I can defend ordinal-preference-respecting welfare); the *identification of the opportunity layer* gets **no** support from this paper. Do not let this paper carry weight against the "your decomposition is mechanical" referee — that defence must come from the structural/identification papers, not from here. **[explicit / analogy]**

---

## 9. Key results and magnitudes

**No empirical magnitudes** (no elasticities, no participation/hours effects, no welfare magnitudes, no decomposition shares). **[explicit]** The "results" are formal characterisations (see §10). There is nothing here to benchmark my opportunity share or welfare spread against. **[explicit]**

---

## 10. Estimators, theorems, or formal results

For each, statement is given near-verbatim in LaTeX as it appears in the PDF; assumptions and technique summarised; reusability judged for my welfare-inversion layer.

**Axiom 1 (Supremum nested contour).** [explicit, p. 37]
> For all $x,x',x''\in X$, $R,R',R''\in\mathcal R$, if $L(x,R)\subset \text{interior}[L(x',R')\cup L(x'',R'')]$, then $W(x,R) < \max\{W(x',R'),W(x'',R'')\}$.
- *Technique:* binary version (weaker than the 2017a countable-sequence version, which the authors note is "unduly strong"). [explicit, footnote 2]
- *Reusability:* **no** (it is a measure-characterisation axiom, not an estimator). Relevant only to justify which reference (Leontief → ray utility) my welfare core would correspond to *if* I went the ray route.

**Lemma 1.** [explicit, p. 37]
> $W$ satisfies supremum nested contour iff there exists $R^w\in\mathcal R^w$ such that, for all $x\in X,R\in\mathcal R$, $W(x,R)=\max_{x'\in L(x,R)} W(x',R^w)$.
- *Reusability:* **no** directly; conceptual ("best/worst reference preference" representation).

**Axiom 2 (Infimum nested contour).** [explicit, p. 38]
> For all $x,x',x''\in X$, $R,R',R''\in\mathcal R$, if $U(x,R)\subset \text{interior}[CH(U(x',R')\cup U(x'',R''))]$, then $W(x,R) > \min\{W(x',R'),W(x'',R'')\}$.

**Lemma 2.** [explicit, p. 38]
> $W$ satisfies infimum nested contour iff there exists $R^b\in\mathcal R^b$ such that $W(x,R)=\min_{x'\in U(x,R)} W(x',R^b)$.

**Axiom 3 (Nested contour).** [explicit, p. 38]
> If $U(x,R)\cap L(x',R')=\varnothing$ then $W(x,R)>W(x',R')$. (Implied by Axioms 1 and 2.)

**Axiom 4 (Nested priority).** [explicit, p. 39] — a resource-inequality-aversion transfer axiom (full strength).

**Lemma 3.** [explicit, p. 40]
> No well-being measure satisfies nested priority and nested contour.
- *Significance:* the strong transfer axiom is incompatible with the basic nested-contour requirement; motivates weakening to *diminishing priority*. [explicit]

**Axiom 5 (Diminishing priority).** [explicit, p. 41] — the weakened transfer axiom (translated transfers; weaker than the Bosmans–Decancq–Ooghe 2015 transfer axiom, which only requires the sum to be constant). [explicit, p. 42]

**Theorem 1.** [explicit, p. 43] — **the result most relevant to my money-metric core.**
> A well-being measure $W$ satisfies infimum nested contour and diminishing priority if and only if there exist a vector $p\in\text{interior}[S^{K-1}]$ and a strictly concave function $g:\mathbb R_+\to\mathbb R_+$ such that $W = g\circ W^p$.
- *Assumptions:* $X=\mathbb R^K_+$; continuous, convex, monotonic preferences; the proof is developed for $X=\mathbb R^2_+$ WLOG. [explicit, p. 46]
- *Technique (3–5 bullets):* (i) infimum nested contour ⇒ "best-preferences" representation (Lemma 2); (ii) diminishing priority forces the reference preferences $R^b$ to be **linear**; (iii) linear reference preferences ⇒ measure ordinally equivalent to money-metric utility $W^p$; (iv) the strict inequality in diminishing priority forces strict concavity of the transform $g$. [explicit]
- *Verdict:* **yes, citable as the axiomatic justification** for using a (concave transform of the) money-metric utility as my preference-respecting welfare core. It does **not** give me the inclusive-value/ex-ante machinery. [explicit for the characterisation; the gap is explicit]

**Lemma 4.** [explicit, p. 43]
> No well-being measure satisfies supremum nested contour and diminishing priority.

**Axiom 6 (Weak diminishing priority).** [explicit, p. 43] — diminishing priority restricted to one specific direction $\Delta$.

**Theorem 2.** [explicit, p. 45] — characterises the **ray utility**.
> A well-being measure $W$ satisfies supremum nested contour and weak diminishing priority if and only if there exist a bundle $\ell\in\text{interior}[X]$ and a strictly concave function $g:\mathbb R_+\to\mathbb R_+$ such that $W=g\circ W^\ell$.
- *Technique:* weak diminishing priority + supremum nested contour force the reference preferences $R^w$ to be **Leontief**; Leontief reference ⇒ ray utility $W^\ell$; strict inequality ⇒ strict concavity. [explicit, pp. 44, 48]
- *Verdict:* **maybe** — usable only if I want a *second* admissible money-metric-type reference (ray utility) as a robustness/alternative to the price-based money metric. Not the baseline.

**Axiom 7 (Unchanged indifference independence).** [explicit, p. 45] — used inside the proof of Lemma 3; well-being depends only on the indifference set at the consumed bundle.

---

## 11. Robustness and specification sensitivity

There is no empirical robustness section. The paper's "specification sensitivity" is *axiomatic*: which combination of axioms one imposes determines which measure is characterised. **[explicit]**

- Infimum nested contour + diminishing priority → **money-metric utility** $W^p$ (Theorem 1). **[explicit]**
- Supremum nested contour + weak diminishing priority → **ray utility** $W^\ell$ (Theorem 2). **[explicit]**
- Strengthening to full nested priority → **impossibility** with nested contour (Lemma 3). **[explicit]**
- Supremum nested contour + full diminishing priority → **impossibility** (Lemma 4). **[explicit]**

What this tells me to stress-test in my own work: my choice of **reference price $p$** (and, for the ray alternative, the **reference bundle $\ell$**) is a genuine normative degree of freedom, not innocuous — the measure is only pinned *up to* the reference and a concave transform $g$. My welfare spec's reference choices are therefore the analogue of their $p$/$\ell$ choice, and the across-measure spread I plan to report is, in their language, partly a sensitivity to the reference. **[analogy]** The authors also flag a domain caveat directly relevant to me: the divisible-goods, monotonic-preference model is **not adapted** to settings where a dimension is bounded or preferences are non-monotonic — they name health/leisure explicitly. My leisure dimension is bounded, so the characterisation does not literally cover my space. **[explicit, p. 50 / §15]**

---

## 12. What I can cite this paper for

- That the **money-metric utility is axiomatically justified** as a preference-respecting, inequality-averse well-being measure (concave transform of $W^p$), via infimum nested contour + diminishing priority (Theorem 1). **[explicit]**
- That a **preference-respecting** well-being measure can be built using *only ordinal, non-comparable* preference data (no interpersonal cardinal utility), which is the informational basis of the Kaldor–Hicks–Scitovsky tradition. **[explicit, pp. 35–36]**
- That the **ray utility** is a second axiomatically-characterised admissible measure (Theorem 2), available as an alternative reference construction. **[explicit]**
- That respecting preferences means the measure depends on the bundle *only through the indifference set* (unchanged indifference independence), discarding cardinal subjective-well-being information. **[explicit, pp. 38–39, Axiom 7]**
- That the money-metric utility, "criticised by Donaldson (1992) and defended by Fleurbaey and Blanchet (2013)," is here given a positive axiomatic foundation rather than being merely an arbitrary example. **[explicit, p. 36]**

---

## 13. What I should NOT cite this paper for  [overclaim risks]

- **Do not** cite it for any **labour-supply, discrete-choice, latent-jobs, or opportunity-set** content — it has none. **[explicit]**
- **Do not** cite it for the **inclusive-value / ex-ante / log-sum** welfare object — the paper is deterministic divisible-goods theory with no expected-maximum. My ex-ante construction is not from here. **[explicit]**
- **Do not** attribute the **$W^1$–$W^6$ family** or the **compensation–responsibility spectrum** or the **Ind-$y$/Ind-$A$ classification** to this paper. It characterises **two** measures ($W^p$, $W^\ell$); the six-measure family is from my welfare spec and the companion theory paper. **[explicit]**
- **Do not** cite it for any **decomposition** (two-way *or* three-way) — there is no decomposition apparatus here. **[explicit]**
- **Do not** read any "sectoral"/"industry" or "occupation-as-access" content into it — no such objects exist; there is no risk of conflation here because the variables are simply absent. **[explicit]**
- **Random-opportunity flag:** N/A — the paper has no opportunity object at all, random or deterministic. Do not use it to adjudicate the deterministic-opportunities framing. **[explicit]**
- **Theory-paper boundary:** this Fleurbaey–Maniquet 2018 paper is **distinct from the companion Haydar–Maniquet theory paper**. Do not conflate the two, and do not read this paper as establishing my JMP's normative taxonomy. It is a cited *primitive* for the money-metric form only. **[explicit on what it characterises; boundary per the prompt]**
- **Domain caveat:** do not claim its characterisation literally applies to my bounded-leisure / discrete space — the authors restrict to divisible, monotonic-preference goods and explicitly defer bounded/non-monotonic dimensions. **[explicit, p. 50]**

---

## 14. Direct quotes worth citing

(Short, exact, with page numbers. Use sparingly; paraphrase by default.)

1. "We construct individual well-being measures that respect individual preferences and depend on the bundles of goods consumed by the individual." (abstract, p. 35) **[explicit]**
2. "The money-metric utility measures it by the income needed to obtain the current satisfaction of the individual, at given reference market prices." (p. 36) **[explicit]**
3. Theorem 1: "$W$ satisfies infimum nested contour and diminishing priority if and only if there exist a vector $p$ ... and a strictly concave function $g$ ... such that $W = g\circ W^p$." (p. 43) **[explicit]**
4. "No well-being measure satisfies nested priority and nested contour." (Lemma 3, p. 40) **[explicit]**
5. "The well-being measures we justify in this paper are intended to be arguments of social welfare functions, but the precise way of aggregating individual well-being remains outside the current analysis." (p. 37) **[explicit]**
6. On the future-research domain caveat: if "health or leisure is a dimension, one dimension in the space is bounded and preferences for leisure may not be monotonic." (p. 50) **[explicit]**

---

## 15. Open questions and risks for my draft

- **Bounded-dimension gap.** The authors themselves flag that bounded dimensions (leisure, health) and non-monotonic preferences are *outside* their divisible-goods model. **[explicit, p. 50]** My welfare space has bounded leisure, so I cannot claim Theorem 1 *literally* covers my object; I should cite it as the motivating axiomatic foundation for the money-metric form and acknowledge the domain extension is not formally established here. **Risk:** a theory-literate referee could press this. **[analogy for the implication]**
- **Reference-choice is a normative degree of freedom.** The measure is pinned only up to a reference ($p$ or $\ell$) and a concave transform $g$. **[explicit]** This is a strength for my "family/spread" thesis (it *legitimises* reporting sensitivity to the reference) but I must be explicit that the spread is partly reference-sensitivity, not pure opportunity content.
- **No aggregation.** The paper deliberately leaves aggregation outside. **[explicit, p. 37]** My inequality index and Shapley aggregation are therefore *not* covered by this paper and need their own warrant.
- **Concave transform $g$.** Theorem 1 admits a strictly concave $g$ on top of $W^p$. My welfare layer should state whether it uses raw $W^p$ (linear $g$) or a concave transform, since the two differ in inequality-aversion content. **[explicit that $g$ is free; the choice is mine — analogy]**

---

## 16. TL;DR for retrieval

Fleurbaey–Maniquet (2018, *IJET*) axiomatically **characterises** the money-metric utility (Theorem 1: infimum nested contour + diminishing priority ⇒ a strictly concave transform of $W^p$) and the ray utility (Theorem 2) as the only preference-respecting, inequality-averse well-being measures, using purely ordinal non-comparable preference data over divisible goods — supplying the **normative foundation for my JMP's money-metric welfare core** but **none** of its access/ability/preference structure, inclusive-value machinery, or decomposition. It is a **pure theory paper with no data, no labour supply, and no opportunity mechanism**, characterising **two** measures (not my $W^1$–$W^6$ family), and is **distinct from the companion Haydar–Maniquet theory paper**; cite it for the money-metric reference-price justification only, and note its explicit caveat that bounded/non-monotonic dimensions (leisure) lie outside its model.
