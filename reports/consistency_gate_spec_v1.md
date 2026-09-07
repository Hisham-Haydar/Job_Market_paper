# Consistency gate — specification v1

**Status: normative.** This file is written *before* any artifact is edited and is
the sole authority for what `reports/run_consistency_gate.py` checks and for what
"PASS" means. `reports/consistency_gate_v1.md` was a prose audit; it is superseded
as an *instrument* by this spec, and is never overwritten. Gate reports produced
under this spec are numbered from **v2**. Amendments A and B (Goal-1 R-271 and
the Goal-2 backend note) add items 11-15; they are checked and reported exactly
like items 1-10.

Authority order, unchanged: **registry (J) > paper v2 (P) > story HTML (H) > deck
content (D) > research-lab notebook (N)**. Where the spec fixes a canonical form,
the canonical form wins over all five and every artifact is edited to it.

---

## 0. Artifacts, identifiers, and what "text" means

| id | artifact | path | text layer the gate reads |
|---|---|---|---|
| **J** | numbers of record | `JMP/reports/numbers_of_record_v1.json` | the `entries` object; read-only authority, never edited by this gate |
| **P** | paper v2 | `JMP/manuscript/JMP_working_paper_for_seminar_v2.md` | the whole file, line by line |
| **H** | research-story HTML | `JMP/reports/JMP_research_story_report_v1.html` | rendered text inside `<div id="doc">`, **excluding** `<script>` blocks (`NOR-DATA`, `AUX-DATA`, page JS) and `<code>` elements; plus the `(section id, data-k)` binding list |
| **D** | seminar deck content | `JMP/manuscript/JMP_seminar_deck_content_v2.md` (**v2.2**) | slide bodies *and* the `Say:` spoken notes; both are audience-facing |
| **N** | research-lab notebook | `MNL/experiments/JMP_SEMINAR_SPRINT/JMP_research_lab.ipynb` | **markdown cells only** for prose/notation rules; code cells only for key-binding and permitted-site rules |

H is **generated**: it is never hand-edited. Every H fix is made in
`JMP/reports/research_story_build/*.py` and the page is rebuilt. N is
**executed**: every N markdown fix is followed by a re-execution of the notebook,
so that saved outputs and Markdown cannot drift apart.

A *print site* is:

- in P, D, N-markdown — a physical line containing a numeral;
- in H — a `<span class="n" data-k="…">` binding, located by its enclosing
  `<section id="sNN">`.

A *passage* is: in P/D/N the maximal run of non-blank lines around the print site
(a paragraph, a table, or one slide record); in H the `<h2 id="sNN">` section.

A *block scope* — used by gate items 5, 8 and 9, which check a multi-paragraph
**result block** rather than a single statement — is the enclosing section: the
`<h2 id="sNN">` section in H, the enclosing `##`/`###` heading block in P, the
whole markdown cell in N, and the whole deck in D (its slides are short and a
block legitimately spans several of them).

---

## 1. Notation (GATE ITEM 1)

**Rule.** Every artifact writes the symbols and the audience-facing names of
`reports/canonical_notation_v1.md`, unchanged. Variant spellings of a canonical
symbol are a FAIL wherever they appear in audience-facing text.

### 1.1 The symbols, listed

*The two estimated objects, and the one computational object.*

| symbol | name | note |
|---|---|---|
| $u_{ij}$ | utility | how $i$ **ranks** package $j$ |
| $g_{ij}$ | opportunity density | how **available** $j$ is to $i$ |
| $q_{ij}$ | proposal density | **computation, not economics**; never called an opportunity, offer or availability |

*Utility block.*

$u_{ij}=\beta_{\ell}^{g}(\mathbf{x}_i)\,\mathcal{B}(\tilde{\ell}_{ij};\theta_{\ell}^{g})+\beta_{c}\,\mathcal{B}(\tilde{c}_{ij};\theta_{c})$,
$\mathcal{B}(z;\theta)=(z^{\theta}-1)/\theta$;
$\beta_{\ell}^{g}(\mathbf{x}_i)=\beta_{\ell 0}^{g}+\beta_{\ell a}^{g}a_i+\beta_{\ell a^{2}}^{g}a_i^{2}+\mathbb{1}\{g=\text{women}\}\beta_{\ell k}^{g}k_i$.

Symbols: $\tilde{\ell}_{ij}=(\bar L-h_{ij})/\lambda_{\ell}$, $\tilde c_{ij}=c_{ij}/\lambda_c$,
$a_i$ (age, **centred and scaled by ten**), $k_i$ (number of children),
$\beta_c\equiv 1$ (scale numeraire), $\lambda_\ell=10$ hours, $\theta_c$ shared
across sexes, $\theta_\ell^{g}$ not.

*Opportunity block — **four** factors.*

$g_{ij}=g^{E}_{ij}\cdot g^{H}_{ij}\cdot g^{\mathrm{Occ}}_{ij}\cdot g^{W}_{ij}$,
switched off on non-employment by $E_{ij}=\mathbb{1}\{h_{ij}>0\}$.

| symbol | audience-facing name | coefficients |
|---|---|---|
| $g^{E}$ | **access** (job access) — *local-market access lives inside it* | $\beta_E,\beta_s,\beta_r\,(r=2..8),\beta_u,\beta_m$ |
| $g^{H}$ | **hours** | $\beta_b$ over five bands, $\beta_{\mathrm{F35}}\equiv 0$ |
| $g^{\mathrm{Occ}}$ | **occupation** | $\beta^{\mathrm{occ}}_{k,g}$, $\beta^{\mathrm{occ}}_{1,g}\equiv 0$ |
| $g^{W}$ | **wage offer** | $\mu_i=\beta_{w0}+\beta_{wL}L_i+\beta_{wH}H_i+\beta_{wx}x_i+\beta_{wx^{2}}x_i^{2}$, $\sigma$, $\delta_{\mathrm{occ}}$ |

*Index and estimator.* $V_{ij}=u_{ij}+\log g_{ij}-\log q_{ij}$;
$q_{ij}=q^{E}_{ij}(q^{H}_{ij}q^{W}_{ij}q^{\mathrm{Occ}}_{ij})^{E_{ij}}$;
$\mathcal C_i$ with $|\mathcal C_i|=101$ ($R=100$ draws plus the observed package).

*Welfare.* $W^1$ (carrier), $W^4$, $W^6$ (normative-reference disclosures).

*Decomposition.* $I^{00},I^{10},I^{01},I^{11}$;
$C_{\mathrm{pref}},C_{\mathrm{env}}$; nested
$C_{\mathrm{acc}},C_{\mathrm{earn}},C_{\mathrm{needs}}$; couples
$I^{0000},I^{1000},I^{0111},I^{1111}$. Inside $C_{\mathrm{needs}}$:
$C_{\text{non-labour resources}}$ and $C_{\text{composition and needs}}$,
audience-facing names **non-labour resources** and **household composition and
needs**.

### 1.2 Forbidden symbol variants — nowhere in audience-facing text

`g^{Acc}` · `g^Acc` · `gAcc` · `log_gAcc` · `g^{market}` · `g^market` ·
`g^{Market}` · `omega_ig` · `ω_ig` · `working_ij` · `age_i` · `nkids_i`

Rationale: the first six assemble a five-term product or collapse two attributed
factors; the last five are code identifiers standing in for $\beta_\ell^g$'s
arguments and for the normalised $a_i,k_i$.

**Permitted sites for the forbidden variants:** none. In N, code cells may of
course *compute* with any identifier, but a code cell that **prints a labelled
column** to an audience uses the canonical name; the column headers
`log_gE / log_gAcc_raw / log_gOcc_raw` are therefore in scope and must be renamed
so that the printed `log_gE` is the full $\log g^{E}$ or is labelled as its
intercept part.

### 1.3 The four-factor statement

Every artifact that states the opportunity density states it as a **four**-factor
product with the four canonical names. Detection: the passage must contain the
four factor symbols $g^E$, $g^H$, $g^{\mathrm{Occ}}$, $g^W$ (in any of the
listed canonical spellings) and must not contain a fifth factor.

### 1.4 The F35 rule — normalisation and peak never conflated

The step structure of $g^H$ has its zero level at the residual bins **and** at
the statutory band: $\beta_{\mathrm{F35}}\equiv 0$ *as a band step*, which is why
A.1 estimates four band coefficients (`beta_h_pt1`, `beta_h_pt2`, `beta_h_ft`,
`beta_h_lh`). The preferred specification then separately estimates **one
coefficient on a 35-hour indicator, over and above the band structure** — the
*institutionally motivated opportunity peak*, stored as `beta_h_f35` (estimate
2.5795, the 41st coordinate; the A.2 benchmark is the same specification less
that one coordinate). The two are different objects and every passage that
states one names the other.

**Rule.** Any passage that writes $\beta_{\mathrm{F35}}\equiv 0$ (or "the 35-hour
band is the reference", or "normalised to zero") must, in the *same passage*,
name the separately estimated 35-hour peak. Any passage that reports the
estimated peak must not describe the same coefficient as normalised to zero.

---

## 2. The $W^1$ statement (GATE ITEM 2)

### 2.1 The canonical sentence

One sentence, from **paper v2 §3.3**, is canonical. Every artifact must contain
it **verbatim** or in one of the named paraphrases of §2.2:

> **$W^1_i$ is the uniform pay that, offered at every job in household $i$'s own
> opportunity distribution, reproduces the expected welfare the household
> actually attains.**

Matching is on a normalised form: LaTeX/HTML markup stripped, `$W^1_i$` → `W1`,
curly apostrophes → `'`, whitespace collapsed, case-folded. The matched core is

`is the uniform pay that, offered at every job in household i's own opportunity distribution, reproduces the expected welfare the household actually attains`

### 2.2 Named paraphrases (the only ones permitted)

| id | permitted in | text |
|---|---|---|
| **PARA-1** | D (slide 4 caption) | "the uniform pay across the jobs you can reach that would leave you as well off" |
| **PARA-2** | D (slide 12 `Say:`) | "the uniform pay across the jobs a household can reach that would leave it exactly as well off as its actual opportunity situation" |
| **PARA-3** | H, N (section/cell lead) | "the uniform pay offered at every job in household i's own opportunity distribution that reproduces the expected welfare it actually attains" |

No other paraphrase is licensed. In particular $W^1$ is **never** "income at a
common reference leisure", never "equivalent income at a common reference
*pay* evaluated at a common reference household", and never defined with the
equivalence scale inside the inversion (see §2.4).

### 2.3 The three clauses — all three, in every artifact

Wherever $W^1$ is defined, the passage carries all three:

1. **neutralises pay differences within the reachable set** — regex
   `neutrali[sz]` within 160 characters of `pay`;
2. **differences in the set itself remain** — literal, spelling-tolerant
   (`differences in the set itself remain`);
3. **the same coalition's set and preferences on both sides** — literal
   (`same coalition's set and preferences on both sides`).

### 2.4 Forbidden $W^1$ constructions

- the equivalence scale inside the inversion: any rendering of
  `BC(w_i / needs_i` , `w_i/needs_i`, `w / needs`, or an equation defining $W^1$
  in which a needs/equivalence scale appears **inside** the utility argument.
  Equivalization is applied to the **raw $W^1$ vector afterwards** (paper §3.5).
- a **common reference household** as the object $W^1$ is inverted against
  (`common reference household`) — the reference is the household's **own**
  opportunity distribution;
- the phrase **`reference leisure`** anywhere in connection with $W^1$; it names
  the different couples measure of Appendix D.3 only;
- any **cross-measure quantitative robustness** claim: `lower bound within its
  own family`, `lower bound on inequality`, or a statement that $W^4$/$W^6$
  corroborate the $W^1$ magnitude. $W^4$/$W^6$ are **normative-reference
  disclosures** only.

---

## 3. negLL labels (GATE ITEM 3)

### 3.1 The two canonical labels — no others

```
singles final model negLL 18022.764617170084
couples clean baseline negLL 43493.342239066726
```

`negll_singles_final = 18022.764617170084` · `negll_couples_final = 43493.342239066726`.

### 3.2 Rules

- **L1 (canonical label present).** An artifact that reports either value at any
  precision must contain the corresponding canonical label string verbatim at
  least once. (Vacuous for an artifact that reports neither — currently D.)
- **L2 (label purity at every print site).** At every print site of either value
  — evaluated in a ±400-character window around that site, not over the whole
  passage, so that an unrelated sentence elsewhere in a long section cannot
  convict it — the text must name the quantity `negLL` or `negative
  log-likelihood`, and
  must **not** name it any of: `log-likelihood` unqualified (i.e. not immediately
  preceded by `negative`), `log likelihood` unqualified, `objective`,
  `objective value`, `criterion`.
- **L3 (sign).** No artifact may describe a positive printed value of either
  quantity as a log-likelihood; a log-likelihood has the opposite sign.
- **L4 (precision).** Full precision is required at least once per artifact per
  value (in the canonical label of L1). Rounded display elsewhere is permitted
  and is not a numerical failure.

Print-site detection: numerals matching `18022\.76` / `43493\.34` in P, D, N; the
bindings `data-k="negll_singles_final"` / `data-k="negll_couples_final"` in H;
`reproduce("negll_…")` and printed `negll…=` lines in N.

`peak_negll_gain` (430.7) is a **likelihood gain**, a different quantity; the
phrase "in log-likelihood" is wrong there too and is replaced by "in negLL"
(a *fall* in negLL). It is checked under L2 as its own print site.

---

## 4. Coverage: bands and intervals (GATE ITEM 4)

- **COV-1 (RQMC band travels with every printed state and contribution).** For
  every registry key $k$ that is a state or contribution **point** (prefix
  `state_`, `couples_state_`, `C_`, `couples_C_`, no `_share`/`__` suffix) and
  that has a sibling `k__rqmc_band` in J: if $k$ is printed in an artifact, the
  band must be printed in the **same passage**. In H this is checked on
  bindings within the same `<section>`. In P/D/N a print site is a passage
  containing the **report-precision rendering** of the value — `%.6f` of its
  magnitude (table precision) or `%.2f` of `100·value` (share precision) — and
  the passage must carry `±`, `+/-`, or the word `band` — the last admits an
  explicit **band pointer** ("bands in Table 7.1a"), which discharges the rule
  for a passage that restates a value the artifact tables elsewhere with its
  band. Looser prose renderings
  ("a Gini of about 0.134") are deliberately *not* print sites: they restate a
  number the table already carries with its band.
- **COV-2 (headline shares carry CR1).** An artifact that prints
  `C_env_female_raw_share` or `C_pref_female_raw_share` anywhere must also print
  the CR1 interval, and every **section or passage that states the headline
  result** must carry it adjacently. The interval — `s_env_female_raw__cr1_interval` = [0.8911, 0.9578] and
  `s_pref_female_raw__cr1_interval` = [0.0422, 0.1089] — i.e. `[89.1, 95.8]` and
  `[4.2, 10.9]` in per cent.
- **COV-3 (the two uncertainties are never merged).** Every passage carrying both
  must contain the never-merged statement (`never merged` / `not merged` /
  `two different objects`). Forbidden: any single interval presented as covering
  both integration and parameter uncertainty.
- **COV-4 (CR1 intervals only where one was computed).** J holds CR1 intervals
  only for `*_female_raw__cr1_interval`, so no *registry-backed* CR1 interval
  exists on a male-reference arm. `tables/parameter_uncertainty_v1.csv` does
  carry equivalized intervals, and Appendix F prints them against that source;
  that is licensed. What is a FAIL is printing or implying an interval for a
  quantity for which none was computed — in particular any male-reference
  interval, and any interval quoted without its arm named.
- **COV-5 (bands are jackknifed as whole quantities).** A band on a ratio or a sum
  is never composed from the bands on its parts. Artifacts state this where they
  print ratio bands.

---

## 5. Nested endowments-and-needs semantics (GATE ITEM 5)

The deputy closure's **six points**. Every artifact that reports the split
carries all six.

| # | point | canonical form the gate looks for |
|---|---|---|
| **NE-1** | **resources / composition-and-needs** | the two factors are named **non-labour resources** and **household composition and needs**; the channel split is two-way, inside $C_{\mathrm{needs}}$ |
| **NE-2** | **no tax-schedule factor** | the tax-benefit schedule is **one common policy function, not a household-specific swappable object**, hence **not a third factor**; it is a qualitative mechanism |
| **NE-3** | **Shapley vs one-factor** | composition is **attributed 12.45 %** but **equalising it alone removes 2.00 %**; both numbers appear together, and the gap is named as the general Shapley-vs-one-factor lesson |
| **NE-4** | **no general dominance claim** | resources lead ~4:1 **on the raw basis only**; once equivalized the two are level and **which leads is reference-dependent and is not claimed** (male arm reverses) |
| **NE-5** | **exact stored values** | printed numbers equal J at displayed precision: raw 45.73 ± 1.80 / 12.45 ± 1.00; equivalized 33.25 ± 1.33 / 32.85 ± 0.68; one-factor 35.30 / 2.00 / 46.04 raw and 23.17 / 20.30 / 56.11 equivalized |
| **NE-6** | **no causal reading** | a descriptive/structural, **not causal** guard in the same passage |

Two further standing traps, checked here:

- **NE-7 (denominators).** The shares **of the needs channel** (78.59 / 21.41 %)
  and the shares **of total inequality** (45.73 / 12.45 %) are distinct and are
  never interchanged: any passage printing one must name its denominator.
- **NE-8 (band provenance).** A share band is the jackknife of the **ratio**, not
  the contribution band divided by $I^{00}$ (raw female: ±1.80, not ±1.27).

---

## 6. Reference labels (GATE ITEM 6)

- **REF-1.** The two conventions are named exactly **female-primary** (the
  reference) and **male structural-zero** (the sensitivity). Forbidden variants:
  a bare "male reference" / "female reference" used as the audience-facing label
  in prose (registry `basis` strings and table stubs are exempt), and any label
  implying a third convention.
- **REF-2.** They are **reported as a pair** and **never averaged**. Every
  passage reporting one must report the other or point at it; the phrase
  `never averaged` must be present where the pair is introduced.
- **REF-3.** `beta_l_nkids_male_status` is **ABSENT; structural zero by the
  sex-specific shifter specification** — never "estimated as zero", never "not
  significant".
- **REF-4 (couples).** Couples carry **one shared parameter vector with per-sex
  coordinates**, not a singles-style sex-reference arm; no artifact may apply the
  singles reference-pair language to couples.

---

## 7. Couples `beta_ll` (GATE ITEM 7)

Every artifact that mentions the couples cross-leisure term states all four:

- **BLL-1** status **ABSENT** from the certified couples specification (J
  `beta_ll_status = "ABSENT"`);
- **BLL-2** the welfare pipeline's effective value is **exactly 0.0**, and this is
  **not an estimated-then-zeroed coordinate**;
- **BLL-3** the form it *would* take —
  `beta_ll * BoxCox(leisure_male) * BoxCox(leisure_female)`, or the same product
  of two Box–Cox leisure terms in the artifact's own notation;
- **BLL-4** it is a **named limitation** on identifying cross-spouse leisure
  complementarity.

**Forbidden:** `beta_ll estimated`, `estimated beta_ll`, `beta_ll was estimated`,
`beta_ll = 0` presented as an estimate.

---

## 8. The RUM block (GATE ITEM 8)

The benchmark is a **common-choice-set RUM** (RUM_B). Required, wherever the
comparison is reported:

| quantity | J key | value |
|---|---|---|
| preference share, RURO | `rum_share_pref_RURO_raw` | 6.3 % |
| preference share, RUM_B | `rum_share_pref_RUMB_raw` | 6.4 % |
| change in measured inequality | `rum_inequality_drop_raw` | −24.2 % |
| leisure gap, RURO | `rum_leisure_gap_final` | +0.428 |
| leisure gap, RUM_B | `rum_leisure_gap_benchmark` | −1.991 |
| omitted share → preferences | `rum_omitted_share_relabelled_as_preferences` | −4.0 % |
| omitted share → endowments and needs | `rum_omitted_share_relabelled_as_needs` | +36.0 % |
| omitted share → leaves the measured total | `rum_omitted_share_leaves_measured_total` | +68.0 % |

- **RUM-1.** All eight travel together where the block is reported; the three
  destinations are signed and sum to one.
- **RUM-2.** The headline reading is: omitting heterogeneous opportunities
  **does not raise the preference share** (6.3 → 6.4); it **relabels the
  market-side contribution into endowments and needs** and drops measured
  inequality by 24.2 %.
- **RUM-3 (forbidden claim).** The misclassification is **not** a clean
  "opportunity becomes taste" story: no artifact may write that omitted
  opportunity is re-attributed to preferences/tastes as the headline. The sex
  leisure gap **reverses sign** (+0.428 → −1.991) and that reversal, not a
  preference-share rise, is the finding.
- **RUM-4.** The §6.7 common-choice-set RUM preference share (3.32 % benchmark
  row of Table 7.1) is a **different object** from the RUM_B decomposition and
  the two are never equated.

---

## 9. Geographic and sex results (GATE ITEM 9)

- **GEO-1.** Geography is **87.6 %** of the access channel (`geo_share_of_C_acc_raw`)
  and **13.05 % ± 0.74** of baseline inequality (`geo_share_of_I00_raw`,
  `…__band`), raw female-primary.
- **GEO-2.** The equivalized access ratio is **1.019** — a signed contribution
  ratio above one, **not** a percentage to clip.
- **GEO-3.** The **housing-allowance rent zone inside needs** is distinguished
  from the **structural access geography**; they are never merged.
- **GEO-4.** A descriptive, **not causal** guard travels with the geography
  result.
- **SEX-1.** The sex re-aggregation prints access shares for men and women on the
  named basis: men 19.58 % raw / 16.74 % equivalized / 18.44 % male-reference;
  women 9.79 % / 7.17 % / 9.02 %; geographic shares men 16.22 %, women 13.08 %.
- **SEX-2.** The men's preference share is **−2.69 %** on the female-primary
  reference and **+2.78 %** on the male structural-zero sensitivity; the **sign
  change with the reference** is stated wherever it is printed, and the two are
  never averaged.

---

## 10. Forbidden terms and their permitted sites (GATE ITEM 10)

| term | permitted sites | everywhere else |
|---|---|---|
| `removes 93.7` | — | FAIL |
| `reference leisure` | P Appendix D.3 (the couples measure it actually names) | FAIL |
| `beta_ll estimated` | — | FAIL |
| `S8` | P: the line range of `### A.4 Provenance note: the storage vector` and the whole of the `## Self-check table` appendix; H: `<div class="box prov">` provenance boxes and the embedded `NOR-DATA`/`AUX-DATA` blocks; N: **code cells** and saved execution logs | FAIL |
| `LOC4` | same as `S8` | FAIL |
| `C_P`, `C_E`, `C_A`, `C_B`, `C_D` as channel names | same as `S8`; plus registry key strings `couples_C_*` inside code/bindings | FAIL |
| `g^{Acc}`, `g^{market}` (and the variants of §1.2) | — | FAIL |
| `removed` as the verb for a Shapley share | — | FAIL — a share is **attributed to**; `reduces` is reserved for the one-factor counterfactual |
| `bootstrap` | P/H/N where the sentence is an explicit denial ("not a bootstrap") | FAIL |
| `provisional`, `pending` as a **status label** | — | FAIL (ordinary English use is exempt; the gate flags upper-case status tokens `PROVISIONAL`, `PENDING`, and `NESTED_ENDOWMENTS_PROVISIONAL_PENDING_ECONOMICS_REVIEW`) |

D (the deck) has **no** permitted site for any term in this table.

---

---

# Amendment A — content items (Goal-1 R-271)

Items 11 to 14 are added to the gate. They are checked exactly like items 1–10
and appear in the same verdict matrix.

## 11. The boundary-active coordinates carry the age-bound diagnostic (GATE ITEM 11)

Two free coordinates — `beta_l_age2_sm` and `beta_l_age2_sf` — rest on an active
box bound at $+1.0$ in the $\lambda_\ell = 10$ unit and carry no standard error.
**Wherever an artifact introduces them, one line must carry the diagnostic and
its verdict**, so that a reader never meets the bound without meeting what it
costs.

**Required, in the same passage as the boundary-active coordinates** (H §7, and
paper §5 — §5.2, where §5 states the bound-activity fact):

| # | fact | value of record |
|---|---|---|
| AB-1 | the box was widened by a **factor of five** on half-widths | linear $\pm5\to\pm25$, quadratic $\pm1\to\pm5$ |
| AB-2 | **the bounds disappear** | active bounds $2\to0$, interior $39\to41$ |
| AB-3 | the objective gain is negligible | $\Delta$negLL **0.552** (18022.7646 → 18022.2124); $\Delta$AIC $=\Delta$BIC $=-1.104$; **not** a chi-square statistic |
| AB-4 | **$+1.0$ lies inside both freed intervals** | men $1.447$, $[-0.584, 3.477]$; women $1.722$, $[-0.032, 3.475]$ |
| AB-5 | the bound is a **unit artefact**: the exact $\lambda_\ell=40$ re-expression, no re-estimation, sends $+1.0$ to strictly interior values | **0.034845** (men) and **0.055555** (women) — 0.035 / 0.056 |
| AB-6 | the **retention verdict** | the preferred specification is retained, and the margin is close (`RETAIN_S8_CLOSE`) |

The line must also point at where the full diagnostic lives: **H §19**, paper
§5.5. Detection: the passage naming the two boundary-active coordinates must
carry a pointer plus AB-1…AB-6.

## 12. The consumption curvature is MAINTAINED, not tested (GATE ITEM 12)

$\theta_c$ is **shared across the sexes by construction of the certified
specification**. It is a *maintained assumption*, and the two reasons are stated:

1. $\beta_c \equiv 1$ is the **scale numeraire**, so the consumption block carries
   the units of the money metric and a sex-split curvature would split the metric
   itself;
2. **parsimony** — the specification search never proposed a sex-specific
   consumption curvature, so it was never tested.

**Rules.**

- **TC-1.** Wherever $\theta_c$ is reported (H §7, paper §3.2 and §6.1), the
  passage says it is **maintained common** and **not tested sex-specifically**.
- **TC-2.** No artifact may describe the common curvature as an estimated or
  tested restriction, or imply a sex-specific curvature was rejected. `theta_c`
  = 0.168 (s.e. 0.074, $z$ = 2.27) is the *level*, not a test of pooling.
- **TC-3.** It appears in the **limitations list** — H §20 and paper §10 — as a
  named **candidate money-metric sensitivity**: the money metric inverts the
  consumption block, so a sex-specific curvature would move $W^1$ for men and
  women differently and is the untested assumption closest to the headline.

## 13. The couples coefficient table (GATE ITEM 13)

The R240 clean baseline's **46 free coordinates** are printed in full, by
economic block and spouse, with robust CR1 standard errors, in **H §11** and
**paper Appendix D.1**.

- **CT-1.** 46 rows, one per coordinate of
  `runs/couples_clean_baseline/r240_step3_estimation_v1.json:parameter_table`,
  in its nine blocks: male leisure (4), female leisure (5), male hours
  opportunity (6), female hours opportunity (6), employment access (10), male
  occupation opportunity (3), female occupation opportunity (3), wage (6),
  occupation wage location (3).
- **CT-2.** Each row carries the estimate and the **robust CR1 standard error at
  $K_{\text{interior}}$** (`se_robust_CR1_Kint`), with $z$; the single
  active-bound coordinate `beta_w_pexp2` carries no standard error.
- **CT-3.** The counts travel with the table: **46 free, 45 interior, 1 active
  bound, 12 pinned inert**, $G = 2{,}275$, $K_{\text{interior}} = 45$.
- **CT-4.** Every numeral is **bound to a registry key** emitted by
  `beamer/make_numbers_of_record_v1.py` — `couples_param_<name>__estimate`,
  `__se_robust`, `__z_robust`, and the counts `n_couples_free`,
  `n_couples_interior`, `n_couples_at_bound`, `n_couples_pinned`. Hand-typed
  couples coefficients are a FAIL.
- **CT-5.** The table's **note states the `beta_ll` ABSENT row**: the
  cross-leisure interaction is not a row of this table because it is not a
  coordinate of the model — status ABSENT, welfare-effective 0.0, form
  `beta_ll * BoxCox(leisure_male) * BoxCox(leisure_female)`.

## 14. Children: the male term and child age (GATE ITEM 14)

In **H §12** (and the paper's matching paragraph in §6.1):

- **CH-1.** The male child-count shifter is described in three parts and all
  three appear: it was **tested** (historical S-battery S4, one male child-count
  shifter added to S0: $+1.6468$, robust s.e. $1.8671$, $z = 0.88$, W-4 flagged;
  $\Delta$AIC $+1.506$, $\Delta$BIC $+6.855$ / $+11.470$); it is **not
  identified** on that evidence; and its **exposure** in the estimation sample is
  small — 91 of 714 single men (**12.75 %** of single men, **5.85 %** of the
  1,555-household sample; weighted 9.36 % and 4.48 %).
- **CH-2.** Its status in the certified model is **ABSENT; structural zero by the
  sex-specific shifter specification** — never "estimated as zero", never "not
  significant" (this is item 6's REF-3, restated at its own site).
- **CH-3.** The **scope caveat** travels with it: the historical test was run on
  the pre-floor5 S0/LOC4 frame and has **not** been re-run on the final corrected
  S8 model.
- **CH-4.** The **child-age variables are named as post-seminar work**, by name
  and not by gesture: each child's **date of birth** and the **parent–child link**
  are already in the raw frame of 11,459 households, so a child's **age**, the
  **youngest-child age**, and a **pre-school (under-6) indicator** are
  constructible with no new data. They are named as future work, not as a
  result.

---

# Amendment B — Torch parity and execution profiles (Goal-2 note)

## 15. Execution profiles and backend parity (GATE ITEM 15)

Checked in **H §21** and the **notebook**. The statement is about *capability and
numerical parity*, never about runtime.

| profile | required status | required qualification |
|---|---|---|
| `server_jax_cpu` | **SUPPORTED** | the profile every certified result is on; the default |
| `laptop_jax_cpu` | **SUPPORTED** | *parity-cleared* — and the artifact must say **which** clearance: the accepted package **PKG-04B**, commit `1eed2756`, whose `unsupported_forms_used` is empty and which carries the occupation-conditional wage location the legacy public pin `258d6eda` lacked |
| `laptop_torch_cuda` | **SUPPORTED** for the **frozen final singles model** | Goal-2 parity, from `export/pkg04b_final_s8_parity_v1.json`, verdict `GOAL1_PKG04B_PARITY_ACCEPT` |

- **BP-1 (the parity list).** Where Torch support is claimed, the parity is
  itemised and matches the artefact: **negLL 18022.764617170084 exact** (bitwise,
  0 ULP); **gradient** max abs $1.42\times10^{-13}$; **Hessian**
  $3.64\times10^{-12}$; **household scores** $2.84\times10^{-14}$ over the full
  $1555\times41$ matrix; **CR1 covariance** $1.58\times10^{-13}$; **robust SE**
  $4.24\times10^{-14}$; the **active-bound set** `{beta_l_age2_sm,
  beta_l_age2_sf}` and the **10 pinned coordinates** identical, pinned gradients
  exactly 0.0.
- **BP-2 (the device caveat, required).** The parity artefact records
  `torch_cuda_available: false` on the server and
  `cuda_disposition.status = CUDA_NOT_AVAILABLE_SERVER_LAPTOP_BUNDLE_EXPORTED`:
  the measured Torch comparison is **Torch CPU against JAX**, and the CUDA
  *device* comparison is the named outstanding item. An artifact claiming Torch
  support must carry this caveat; claiming a measured CUDA parity is a FAIL.
- **BP-3 (the obsolete sentence is gone).** The claim that a backend **cannot
  represent** the occupation-conditioned wage location or the final hours
  specification is **removed everywhere** — paper Appendix C, H §21, notebook.
  Detection: the strings `cannot represent the specification`, `cannot represent
  this specification`, and `GPU grammar cannot represent`, and any sentence
  pairing `occupation-conditional wage location` / `occupation-conditioned wage`
  with `cannot`.
- **BP-4 (the default is unchanged).** `server_jax_cpu` remains the default
  profile, and every artifact says so. **Runtime is not re-established**: the old
  "the CPU route is about 2.7 times faster" comparison is retired rather than
  restated, and no new runtime claim is made outside the benchmark cell's own
  printed output.
- **BP-5 (the benchmark cell).** The notebook carries a benchmark cell comparing
  complete-model runtime across the available profiles. It **runs only where the
  backend is installed** and otherwise prints `SKIPPED` with the reason. Its
  output is a **diagnostic on the machine it ran on**, is labelled as such, and
  is not a number of record.

---

## 16. Pass rule and reporting

- Each of the fifteen gate items yields one verdict per artifact: **PASS**, **FAIL**,
  or **N/A** (the artifact does not report that object at all — N/A must be
  *justified* by the absence of every trigger, never used to excuse a partial
  report).
- The gate **PASSES** only when every (item, artifact) cell is PASS or a
  justified N/A.
- The report is written to `reports/consistency_gate_v2.md` (and `_v3`, … on
  later re-runs if v2 is retained). `reports/consistency_gate_v1.md` and this
  spec are **never overwritten**.
- The gate is not a substitute for the existing verifiers. A gate PASS is
  meaningful only alongside: `reports/research_story_build/verify.py` (CHECK A+B),
  `beamer/verify_content_v4.py`, `beamer/verify_deck_v1.py`, and
  `MNL/experiments/JMP_SEMINAR_SPRINT/runs/headline_table/verify_paper_integration_v1.py`.
- **H is rebuilt and N is re-executed before the run that is reported as final**;
  a gate run over a stale build is reported as such and does not count as PASS.
