---
title: "Equal Opportunity or Equal Social Outcome?"
authors: [Marc Fleurbaey]
year: 1995
outlet: "Economics and Philosophy, 11, 25--55"
country_or_context: "Abstract normative theory of distributive justice"
population: "Not applicable"
data_period: "Not applicable"
shelf: "equal opportunity / responsibility / compensation / factor-selective vs outcome-selective egalitarianism"
tags: [equal-opportunity, equal-social-outcome, factor-selective-egalitarianism, outcome-selective-egalitarianism, responsibility, compensation, separability, Pareto-conflict, privacy, free-will, Fleurbaey]
priority: "very high"
read_status: "extracted"
---

# Full citation

Fleurbaey, M. (1995). Equal opportunity or equal social outcome? *Economics and Philosophy*, 11, 25--55.

# One-sentence contribution

Argues that the standard equal-opportunity / factor-selective egalitarian approach (compensate talents, respect will) is theoretically unstable -- requiring strong separability, conflicting with Pareto efficiency, and depending on a problematic notion of free-will-based responsibility -- and proposes instead "outcome-selective egalitarianism": equalize selected social outcomes while preserving a private sphere.

# Why this paper matters

This is Fleurbaey's early, deep critique of the entire equal-opportunity architecture, not just a specific formulation. For my JMP, it provides a fundamental normative warning: simply decomposing inequality into "compensable circumstances" and "responsible choices" is not enough. The paper motivates building a framework that is more careful about what enters the justice metric and what remains private -- a concern directly relevant to defining $W(z,R,A;y)$.

# Core research question

Should egalitarian justice equalise opportunities (by compensating for talents/circumstances while leaving will/choice to individual responsibility), or is it better to equalise selected "social outcomes" while protecting a private sphere?

# Model / theoretical framework

**Normative critique and alternative.** Individual outcome $\mathcal{O}(r, t, w)$ where $r$ = resources (socially controllable), $t$ = talents/circumstances (to be compensated), $w$ = will (individual responsibility). Two schools within "factor-selective egalitarianism":
- **Equal resources school** (Rawls, Dworkin, van Parijs): equalise extended resources $(r, t)$; identify $w$ with personal goals and ambitions.
- **Equal opportunity school** (Arneson, Cohen, Roemer, Sen): equalise choice sets; identify $w$ with personal control and responsibility.

**Equal opportunity defined:** Choice sets $\{(\mathcal{O}_i, w_i) \mid \mathcal{O}_i = \mathcal{O}(r_i, t_i, w_i), w_i \in W\}$ must be the same across individuals.

**Separability requisite (Section 3):** Equal opportunity is generally nonempty only if:
$$\mathcal{O}(r, t, w) = \mu(\nu(r, t), w)$$
Resources and talents must first collapse into a single extended-resource bundle $\nu(r,t)$. Equal opportunity therefore presupposes -- rather than solves -- the aggregation of external and internal resources.

**Distributional requirements:**
- **RT (More Resource for less Talent):** $\forall i,j$: $r_i \geq r_j \Leftrightarrow t_i \leq t_j$.
- **OW (better Outcome for better Will):** $\forall i,j$: $\mathcal{O}_i \geq \mathcal{O}_j \Leftrightarrow w_i \geq w_j$.
- **ERET (Equal Resource for Equal Talent):** $\forall i,j$: $t_i = t_j \Rightarrow r_i = r_j$.

These are shown to be mutually incompatible or to conflict with Pareto optimality.

**Constructive alternative (Section 7):** Outcome-selective egalitarianism. Split outcomes: $\mathcal{O} = (\mathcal{O}_1, \mathcal{O}_2)$, where $\mathcal{O}_1$ = social outcomes (society equalises) and $\mathcal{O}_2$ = private outcomes (protected sphere). Illustrative social outcomes: health, education, wealth, collective decision-making power, social integration. Illustrative private: life-style, subjective satisfaction, cheerfulness.

# Key objects

- Outcome function $\mathcal{O}(r, t, w)$ and its three-factor decomposition.
- Separability condition $\mathcal{O} = \mu(\nu(r,t), w)$.
- Two reference criteria derived from weakening RT + OW:
  - **Roemer's criterion:** Select reference will $\bar{w}$; equalise $\mathcal{O}(r, t, \bar{w})$ across individuals.
  - **Egalitarian-equivalent criterion** (Pazner-Schmeidler): Select reference bundle $(\bar{r}, \bar{t})$; each individual gets outcome $\mathcal{O}(\bar{r}, \bar{t}, w_i)$.
- Social/private outcome partition $\mathcal{O} = (\mathcal{O}_1, \mathcal{O}_2)$.
- Maximin over social outcomes: $\max \min_i \varphi(s_i, h_i, e_i, we_i, p_i, si_i)$ (illustrative with 6 dimensions).

# Treatment of preferences

Not modelled as $R_i$ in the Fleurbaey-Maniquet technical sense. But the paper is deeply concerned with the status of tastes, ambitions, and will. Key arguments:

1. **Free will problem:** Grounding justice on "genuine free choice" is metaphysically fragile and practically unworkable. Incompatibilist and compatibilist views both create problems for the equal opportunity principle.

2. **Bert example (pp. 40--42):** A reckless motorcyclist suffers a head injury. Under strict equal opportunity, he gets no compensation because his risk-taking was "his responsibility." Fleurbaey argues this verdict is morally crude: the scale of suffering should matter, not just the attribution of responsibility.

3. **Changing selves:** Responsibility for past choices becomes morally unstable when personality evolves over time -- "Bert II" (reformed) should not bear all consequences of "Bert I" (reckless).

4. **Two senses of responsibility:** (i) "responsible for" in the causal/blame sense (linked to free will); (ii) "responsible for" in the institutional/decision-making sense (this domain is under this decision-maker's authority). The paper proposes grounding the private sphere on sense (ii), not sense (i).

# Treatment of opportunities / constraints

Opportunities are defined abstractly as sets of attainable outcome levels as $w$ varies, NOT as explicit feasible job sets, latent offers, or demand-side constraints. No $A_i$ object in the labour economics sense.

The paper's central finding is that even this abstract opportunity concept is fragile: it requires separability, fails under externalities and mutual interactions (Section 5 -- the "race on separate tracks" picture is unrealistic), and depends on a contested notion of responsibility.

# Welfare / normative object

The proposed alternative is outcome-selective egalitarianism: equalise social outcomes $\mathcal{O}_1$ (those for which social institutions bear decision-making responsibility), protect private outcomes $\mathcal{O}_2$ (those belonging to individual autonomy). The boundary between social and private is partly a matter of public deliberation, not metaphysics.

This is directly relevant to what enters $W(z,R,A;y)$. The paper suggests that not every element of $z$, $R$, $A$, or $y$ should automatically enter the justice metric. Some dimensions may legitimately remain in a protected private sphere.

# Main findings

1. **Separability requisite:** Equal opportunity is nonempty only if $\mathcal{O}(r,t,w) = \mu(\nu(r,t), w)$. The approach presupposes rather than solves the aggregation of resources and talents.

2. **Pareto conflict:** RT and OW (and even ERET) can conflict with Pareto optimality in multidimensional or nonstandard environments (Section 4).

3. **Externalities destroy equal opportunity:** When one agent's will affects another's outcome, ex ante opportunity sets become unstable or ill-defined (Section 5).

4. **Responsibility critique:** Free-will-based responsibility is metaphysically fragile, practically unworkable, and morally crude. The Bert example shows that strict equal opportunity can produce morally repugnant verdicts (Section 6).

5. **Constructive alternative:** Outcome-selective egalitarianism with social/private distinction. Responsibility in the institutional (decision-making) sense, not the metaphysical (free will) sense (Section 7).

6. **Maximin illustration (Section 8):** Six social outcomes (respect for private sphere, health, education, wealth, decision-making power, social integration) with maximin aggregation.

# Main limitations

- The constructive alternative remains partly programmatic: no fully developed formal welfare measure.
- The social/private boundary is left to public deliberation, not uniquely determined.
- Opportunity concept is philosophical, not the economic feasible-set concept needed for structural models.
- No empirical application.

# Relevance for my JMP

## possible use for normative architecture
Extremely valuable. The paper motivates a framework that does not simply decompose inequality into "compensable opportunities" and "responsible choices" but is more careful about what enters the justice metric. This shapes how I define $W(z,R,A;y)$: which dimensions of $z$ are "social outcomes" for which society should seek equalisation, and which are "private" and protected?

## possible use for critique of naïve decomposition
The separability and Pareto conflicts warn against treating opportunity-based decomposition as ethically self-sufficient. My framework should be robust to these critiques.

## possible use for the two senses of responsibility
The institutional (decision-making) sense of responsibility, distinct from the metaphysical (free will) sense, provides a more defensible foundation for the private sphere in my framework.

# Research questions this paper inspires

1. Can $W(z,R,A;y)$ be defined with an explicit protected private sphere, where some dimensions of $z$ are evaluated socially and others are not?

2. Does the separability critique apply to opportunity-set-based welfare measures like equivalent income, or does the explicit feasible-set structure $A_i$ avoid it?

3. Can the Bert-type moral objection to strict responsibility be formalised as a constraint on $W$?

# Challenge to this paper

The critique is stronger than the construction. The paper convincingly destabilises factor-selective egalitarianism but the outcome-selective alternative is only partially formalised. For my JMP, this is an invitation: the next step is to give this alternative a sharper individual welfare representation -- which is precisely what $W(z,R,A;y)$ aims to do.

# Relation to my jobs_and_wellbeing framework

[Explicit in paper] Rejects decomposing causal factors into compensable and non-compensable. Proposes decomposing outcomes into social (equalise) and private (protect). No $W(z,R,A;y)$, no $A$, no $R$ in technical sense.

[Reasonable inference for my project] The paper suggests that not every element of $z$, $R$, $A$, or $y$ should enter the justice metric identically. Some belong to a protected sphere. My framework should be interpretable through this lens: equivalent income captures "social outcomes" (income, opportunity-set quality) while respecting preference diversity as part of the "private sphere."

[Unclear from paper] How to map the social/private distinction into formal axioms on $W$; whether independence of $A$ or independence of $y$ relates to the social/private boundary.

# Relation to Bargain et al. (2013)

Not directly related. Both care about preference heterogeneity, but Bargain et al. is an empirical welfare paper while this is a philosophical critique of the equal-opportunity framework.

# Relation to opportunities vs preferences

Centrally about opportunities versus outcomes, and indirectly about opportunities versus preferences. The paper cautions against treating "opportunities" as a morally self-sufficient object. Even if opportunities matter, the real normative task may be to decide which outcomes society should equalise and which should remain private. This is a meta-level contribution to the opportunities-vs-preferences debate.

# Useful quotations / formulas

**Separability requisite:**
$$\mathcal{O}(r, t, w) = \mu(\nu(r, t), w)$$

**Equal opportunity definition:** Equality of attainable sets $\{(\mathcal{O}_i, w_i) \mid \mathcal{O}_i = \mathcal{O}(r_i, t_i, w_i), w_i \in W\}$.

**Outcome-selective decomposition:**
$$\mathcal{O} = (\mathcal{O}_1, \mathcal{O}_2)$$

**Two senses of responsibility (pp. 44--45):** (i) "responsible for your act" (causal/blame, linked to free will); (ii) "responsible for this domain" (institutional, decision-making authority). The private sphere should be grounded on (ii), not (i).

**Bert example (pp. 40--42):** Under strict equal opportunity, a reckless motorcyclist who suffers a head injury gets no compensation. "A society complying with equal opportunity looks rather primitive."

**Maximin illustration (p. 53):**
$$\max \min_i \varphi(s_i, h_i, e_i, we_i, p_i, si_i)$$

# Suggested tags

equal-opportunity, equal-social-outcome, factor-selective-egalitarianism, outcome-selective-egalitarianism, responsibility, compensation, separability, Pareto-conflict, privacy, free-will, Bert-example, Fleurbaey

# My quick takeaway

A foundational normative paper that breaks the hold of the standard "equalise opportunities, respect choices" formula. Its critique -- that equal opportunity requires unrealistic separability, conflicts with efficiency, and depends on a problematic free-will-based notion of responsibility -- is devastating. Its constructive alternative (outcome-selective egalitarianism with a social/private distinction) is only partially formalised, but it motivates exactly the kind of careful welfare framework my JMP aims to build. The key takeaway for $W(z,R,A;y)$: not every dimension should enter the justice metric the same way, and responsibility should be understood institutionally, not metaphysically.
