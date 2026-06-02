# JMP T2 Focused Extraction Prompt (v2)

> **Use for:** T2 (selective) and any T3 paper worth a short structured note.
> Core T1A/T1B papers use `JMP_T1_exhaustive_extraction_prompt_v2.md`.
> **What changed from v1 (`summary_T2.md`):** corrected to the **three-way
> access / ability / preference** decomposition; added the $W^1$–$W^6$ family and
> proposal-correction hooks; added the empirical-JMP vs theory-paper boundary.
> Section numbers stay non-contiguous on purpose so these notes co-index with the
> full T1 template.

---

ROLE
You are an expert research assistant in structural labour-supply econometrics,
discrete-choice random-utility (RURO / latent jobs) models, money-metric /
equivalent-income welfare, and the inequality-of-opportunity / Shapley–Shorrocks
decomposition literature.

TASK
Produce a focused, retrieval-oriented Markdown summary (600–1200 words) of the
attached paper, for my empirical JMP *"Unequal Job Opportunities and Well-Being
Inequality: A Latent-Jobs Structural Decomposition"* (Haydar 2026). This is a
**supporting / background** paper: prioritise what bears on my opportunity
mechanism (access / ability), my welfare object, my decomposition, and
identification; treat the rest briefly. Do not summarize my project — use the
anchor only to judge relevance.

MY PROJECT — anchor (current; supersedes the old two-factor framing):
- **Question.** How much of money-metric well-being inequality is driven by
  unequal **job opportunities** vs heterogeneous **preferences**, with labour
  supply as choice among latent jobs?
- **Model.** RURO / latent jobs: choice value
  `u + log h + log w + log market − log π`; `−log π` is the mandatory
  proposal/prior correction; household inclusive value is the log-sum.
- **Three channels (NOT two-factor).** **preference** = utility $v$; **ability**
  = wage technology in $g$ (education/experience returns, $\sigma$; the
  Independence-of-$y$/pay dimension); **access** = the rest of $g$ (hours,
  market, region, urbanisation, year, occupation offers; the
  Independence-of-$A$/feasible-set dimension). "Opportunity" = access + ability.
- **Estimation.** France pooled EU-SILC 2015–2017 via EUROMOD; singles + couples
  (couples joint); certified 47-param baseline (synthetic-recovery certified).
- **Welfare.** Ex-ante, household-level, money-metric, preference-respecting
  equivalent income, computed as the **family $W^1$–$W^6$** on a
  compensation–responsibility spectrum (Ind-$y$ = pay/ability; Ind-$A$ = access);
  $W^3$ Full Responsibility, $W^5$/$W^1$ one-sided duals, $W^4$/$W^6$ Full
  Compensation.
- **Contribution.** Three-way access/ability/preference Shapley–Shorrocks
  decomposition, anchored on $W^3$/$W^5$/$W^1$.
- **Boundaries.** Not a country-ranking/beyond-GDP paper; **not** the separate
  Haydar–Maniquet theory paper (import normative readings as **cited primitives**,
  re-derive nothing); opportunities are **deterministic**; occupation
  (`loc4`, ISCO) is **access**, never industry/sector (`lindi`, NACE, reserved).

OUTPUT — use exactly this structure (non-contiguous numbering matches the T1
template; "N/A" if a section does not apply):

# Author Year — Title

## 0. Metadata
BibTeX key, authors, year, outlet, DOI/URL, PDF filename, tier, and which JMP
block(s) it serves (estimation / identification / welfare / decomposition /
opportunity-mechanism (access / ability) / normative-interpretation /
data-infrastructure / motivation).

## 1. One-paragraph relevance to my JMP
Two to four sentences; name the channel(s) or welfare measure(s) it speaks to.

## 2. Data, setting, and model in brief
Country, year, data, sample unit, core model/method in a few sentences. Note one
feature I do not have if relevant.

## 5. Opportunity mechanism
How feasibility/availability of jobs/hours/wages/occupations is modelled, if at
all, mapped to **access** vs **ability** where possible. If it assumes a common
universal choice set with no explicit opportunity mechanism, say so plainly.
(Keep this section even when brief — it is load-bearing for me.)

## 6. Welfare object
Whether/how the paper computes welfare; money-metric vs other; constrained vs
universal set; ex-ante vs ex-post; reference object. Where it sits on my
$W^1$–$W^6$ map (or which Ind-$y$/Ind-$A$ stance), if any. Relation to my
constrained ex-ante money-metric. (Keep this section.)

## 7. Inequality / decomposition content
Inequality index, decomposition rule, counterfactual construction,
order-independence/exhaustiveness. Reusable for my **three-way**
access/ability/preference Shapley split? If it is two-way (opportunity/preference,
or compensate/reward), say how it would extend to three channels. (Keep this
section.)

## 8. Identification and separation of preferences from opportunities
What identifies tastes vs constraints (and ability vs access if possible) here,
and whether it transports to my France pooled cross-section (no panel, no external
instrument). Honest and brief. (Keep this section.)

## 9. Key results and magnitudes
The one to three numbers worth remembering, with units and population.

## 12. What I can cite this paper for
## 13. What I should NOT cite this paper for (overclaim risks)
Include the relevant boundary flags: two-way vs three-way; ex-post/universal vs
constrained ex-ante; sector/industry vs occupation-as-access; random vs
deterministic opportunities; and the **theory-paper boundary** (never attribute
the companion characterisation/proofs to the JMP).

## 16. TL;DR for retrieval
Three dense sentences for indexing, naming the channel(s) / welfare stance.

RULES
Do not invent claims, theorem numbers, estimates, or DOIs; write "[uncertain,
needs verification]" where unsure. Distinguish explicit-in-source from
derived-by-analogy from not-established. Use the **three-way access / ability /
preference** vocabulary; flag any source that uses the obsolete two-factor
framing. Keep **occupation (ISCO / `loc4`)** separate from **industry / sector
(NACE / `lindi`)**; flag any conflation. Treat opportunities as **deterministic**.
Respect the **empirical-JMP vs theory-paper boundary**. LaTeX for all math. No
praise, no filler. If a section does not apply, write "N/A" — do not pad.
