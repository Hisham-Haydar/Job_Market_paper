# Paper expository carry-over v1

**Input to PAPER-TEX.** The research-story report v2 (R-272) added a large
amount of exposition that did not exist anywhere before. This file decides, item
by item, **what goes into the paper and in what compressed form**, and what
stays in the report only. It is a disposition list, not a draft.

The governing distinction: the paper must be **self-contained and defensible to
a referee**; the report may be **discursive and pedagogical**. Anything a
referee would need in order to evaluate a claim goes into the paper. Anything
that only helps a reader who is meeting the object for the first time stays in
the report.

Source of every row: `reports/JMP_research_story_report_v1.html`, built from
`reports/research_story_build/`.

---

## A. Goes into the paper

### A1. The sample-construction waterfall, with reasons — §4.1

**Status: the paper already has the table; it lacks the reasons.**
Report §3 gives each screen a one-line economic justification and states that
the *same* screens produce both estimation samples, with singles and couples
traced side by side at every step.

**Carry compactly:** add a `reason` column to the paper's existing Table 4.1
(one clause per row, not the report's full sentence), and add the couples
column pair so the single table serves both samples. Drop the report's
narrative framing. **Cost: about a third of a page**, and it removes a standing
referee question about whether the couples sample was constructed differently.

### A2. The engine-ready / source-data distinction — §4.4

**Status: partially present.** The paper explains that the tax-benefit
simulator is run once in advance; it does not state crisply that the estimation
data are a *derived* object with a fixed set of drawn alternatives.

**Carry compactly:** two sentences in §4.4, no table.

### A3. The four operators in words and in mathematics — §7.1

**Status: this is the largest genuine gap.** The paper defines the
decomposition and names the channels, but nowhere states each counterfactual in
the form *we replace X by its reference, holding Y fixed, and re-evaluate*.
Report §14.3 does, for all four, with the formula beside each.

**Carry in full, compressed:** a single displayed list of four operators with
their formulas — the report's four `\longmapsto` displays, plus the
one-sentence English gloss for each. **This belongs in the paper as a matter of
replicability**: a reader cannot currently reconstruct the equalising-endowments
operator from §7 alone. Keep the report's note that the equivalence scale
travels with the composition factor, which is load-bearing for exhaustiveness.
**Cost: about half a page.**

### A4. The classification argument — new §7.x

**Status: absent from the paper as an argued unit.** Report §14.5 argues why
each object sits in its channel, and — the part that matters most — names four
places where the line is a **choice rather than a deduction**: composition
entering both the scale and the schedule; the statutory peak placed in offers
rather than tastes; the consumption curvature held common; access possibly
mixing capability with availability.

**Carry in full, compressed:** the four-row classification table plus the
four-item "where the line is a choice" list, as a short subsection at the head
of §7. **This is the single highest-value carry-over.** It converts four
referee objections into four disclosed modelling decisions, and three of the
four are already conceded elsewhere in the paper in scattered form (§3.5, §6.3,
§10.1) — consolidating them is a net reduction in length.

### A5. The common-opportunity benchmark as a *replacement* — §6.7

**Status: the paper is correct but not explicit.** Report §14.4 states that the
benchmark replaces every household's own density by one population-common
density normalised to integrate to one, **with the preference block
re-estimated against it** — and that it is therefore not the preferred model
with a factor switched off.

**Carry compactly:** one displayed line and two sentences at the head of §6.7.
Cheap, and it forecloses the most common misreading of that section.

### A6. The plain-language readings of the headline coefficients — §6.1–§6.4

**Status: partially present, unevenly.** The paper reads the 35-hour peak as a
density ratio and the unemployment coefficient qualitatively. It does not read
the occupation-access coefficients, the education loadings or the occupation
wage shifts in magnitudes.

**Carry selectively — not the whole column.** Add the ratio or percentage
reading for the coefficients the paper actually discusses in prose: the
statutory peak, the group unemployment rate, the two large occupation-access
coefficients, and the high-education wage loading. **Do not** carry a reading
for all 41 + 46 coordinates; that is the report's job. Add one sentence to
Appendix A saying that every coordinate's reading is in the report.

### A7. The standard error, defined rather than labelled — §5.1 and Appendix A

**Status: the paper says "CR1" and gives the correction.** It never says in
words what the clustering allows for.

**Carry compactly:** one sentence at first use — arbitrary correlation among a
household's own rows, independence across households, with the finite-sample
correction — and then the short label thereafter.

### A8. The maintained consumption curvature — §3.2, §6.1, §10.2

**Status: carried in the R-271 amendment. No further action.** Listed here so
PAPER-TEX does not re-derive it.

---

## B. Stays in the report only

### B1. The descriptive distributions and the observed-income Gini

Six figures and two tables of sample description. A referee does not need them
and the paper's Table 4.2 already carries composition. **Keep the report's
warning box** — that observed income inequality and the welfare measure are not
comparable — as a *footnote* in the paper's §7.1, because that confusion is
likely; drop everything else.

### B2. The Box–Cox transformation explained from first principles

The report explains what the curvature parameter does to the shape of the
function. A paper reader knows this. **Report only.**

### B3. The worked household through the four densities

Report §6.4 multiplies four ratios to build one package's availability weight.
Pedagogically the strongest thing in the report; entirely redundant for a
referee, who reads the functional forms directly. **Report only.**

### B4. The glossary

Fifteen definitions. **Report only.** A paper defines terms at first use, which
A7 handles for the one term that was genuinely undefined.

### B5. "One model, two applications" as a framing device

The report's §6.2 comparison table exists to stop the reader treating couples
as an appendix. The paper achieves the same by having §8 be a full section.
**Report only** — but PAPER-TEX should check that §8's opening sentence says
the couple is the *same* model with a two-adult decision unit, which currently
it only implies.

### B6. The reproduction guide and the self-check section

Sections 21 and 23 of the report. **Report only, permanently.** These are the
two sections whose subject is the computation.

---

## C. Two things the paper should *lose* to the report

### C1. The parameter-by-parameter prose in §6.1

The paper walks through the blocks in prose *and* prints Appendix A. With the
report now carrying a reading for every coordinate, §6.1 can be cut to the
coefficients that carry an argument — the peak, the unemployment rate, the
occupation contrasts, the curvatures — and point at the report for the rest.
**Saves roughly half a page and improves the section.**

### C2. The chronology of the specification search

§8 of the report and the paper's own specification history overlap. The paper
needs the nesting and the two rejections that matter; the narrative of what was
tried in which order is report material.

---

## D. Order of work for PAPER-TEX

1. **A4** (classification and the four choices) — highest value, largest
   referee effect, partly a consolidation of existing scattered text.
2. **A3** (the four operators) — replicability gap; do it before any other
   §7 edit.
3. **A5**, **A7** — each under a paragraph, both foreclose misreadings.
4. **A1**, **A2**, **A6** — mechanical additions to existing tables and prose.
5. **C1**, **C2** — the compensating cuts, which should be made in the same
   pass so the section does not grow.

Nothing in section B is to be carried without a specific instruction, and
nothing in this file changes a number: every quantity referred to here is
already in `reports/numbers_of_record_v1.json` and is reported identically in
the paper and in the report today.
