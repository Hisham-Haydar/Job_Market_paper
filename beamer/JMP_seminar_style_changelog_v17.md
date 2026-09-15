# Seminar deck style changelog: V17 against V16

## What V17 is

V17 is a style revision of V16, modelled on the companion theory talk *Jobs and Well-Being Measurement*.

- **What did not change.** No number changed. No new result or source was added. V16 and r6 are untouched.
- **Numbers.** V17 uses 58 macros from `make_deck_numbers_r6.py --v17`. The script reads only `reports/numbers_of_record_v15.json`. It keeps V16's 51 macros and adds the data-slide definitions: policy year, sampled alternatives, occupation groups, and the hours and wage supports.
- **Figures.** The three figures are the same V15 image files, byte-identical.

| | V16 | V17 |
|---|---|---|
| Main slides | 18 | 16 (title + 15 numbered) |
| Backup | none | 4, after the conclusion |
| Frame titles | full-sentence headlines, 15 of them longer than six words | short conceptual nouns, all six words or fewer |
| Slide bodies | prose, bullets, red caveat lines | equations, figures, labelled columns, a bracketed citation |
| Narration | split between slide and notes | notes only |
| Caveats | red caveat line on most slides | one dedicated slide ("What is not claimed") |

## Structure

V17 follows the ruling's 16-slide order:

1. Title
2. Motivation
3. The conflict
4. Research question
5. Literature and gap
6. Job packages
7. Opportunities: the choice probability
8. Data and EUROMOD
9. Estimation
10. Welfare
11. Ex-ante prospect welfare
12. Attained-bundle welfare
13. Inequality and Shapley decomposition
14. Results: prospects versus attained outcomes
15. What is not claimed
16. Conclusion

Backup slides: B1 ex-ante decomposition, B2 attained-bundle decomposition, B3 matched households, B4 equivalisation.

## Added

- **The conflict (slide 3).** Placed before the data. It uses the theory talk's two-column form: compensation versus responsibility, then the impossibility $\nexists W$: Full Compensation $\wedge$ Full Responsibility, with the [Fleurbaey & Maniquet] citation. The compensation column is adapted to job opportunities. The citation carries no year, because every numeral on a slide must resolve to the V15 number record.
- **Data and EUROMOD (slide 8).** A dedicated slide. It shows the sample sizes, survey and policy years, supports and sampled alternatives as labelled columns.
- **Welfare (slide 10).** The theory figure is now the centre of the welfare section. Its caption is shortened for a slide: it keeps the own-set construction and the "Adapted from Haydar and Maniquet (2026), work in progress" attribution. It drops the section reference and the $W^1$ notation.
- **Results (slide 14).** Framed as *prospects versus attained outcomes*. The V15 figure sits above two labelled columns, EA prospects and ATT attained outcomes, each with its range and ordering.
- **What is not claimed (slide 15).** One slide carries every caveat as two labelled columns:
  - *Scope:* resources, needs and composition held fixed; local access, not total opportunity; preliminary.
  - *Not claimed:* causal effects; parameter uncertainty; preferences as responsibility; a primary perspective.
- **Backup slides B1–B4.** B1 and B2 hold the two decomposition tables moved out of the main deck. B3 holds the matched-household figure. B4 is a new two-column slide on equivalisation.
- **Speaking notes.** Every sentence of V16 slide prose was moved into `\note{}` or dropped. Equation notes still open with "In words:".

## Removed from the main deck

- **Real-world inequality prose (V16 slide 2).** Replaced by the Motivation slide with two columns: observed $C_i$ and well-being $M_i$, with their Ginis.
- **Literature prose columns (V16 slide 3).** Author names are kept; the explanatory text moved to notes.
- **Stand-alone "two different welfare questions" table (V16 slide 12).** The statement now appears on slides 14–15, and the comparison is framed as prospects versus attained outcomes.
- **EA and ATT results tables (V16 slides 15–16).** Moved to backup slides B1 and B2.
- **Matched-household slide (V16 slide 7).** Moved to backup slide B3.
- **Red caveat lines under figures and equations.** Removed from every main slide except "What is not claimed".
- **Sentence headlines.** All replaced by short titles.

## Checks

`verify_deck_r6.py --deck v17` runs the verifier repointed the same way it was for V16. The V16 and r6 runs still pass: V16 18/18, r6 19/19.

**Carried over.** All V16 checks are repeated against V17's own titles, required statements and caption:
- retired tokens and the out-of-scope ban;
- typed numerals and every number on a slide resolving to the V15 registry;
- figure files and retired-lineage paths;
- confusion-matrix wording, no pooled figure, no side-by-side comparison;
- structure, the research question, the five equations and the central figure;
- required statements, no-primacy wording, the caption, and internal labels (now 42 patterns, adding version strings and "frozen"/"accepted");
- no 80–90% claims.

**Added:**
- **G-V17-STYLE:** no frame title longer than six words, and no rendered body paragraph longer than three lines.
- **G-V17-CAVEATS:** red caveat text only on the dedicated slide.
- **G-V17-BACKUP:** results tables only in backup, after the conclusion.
- **G-V17-CONFLICT:** the conflict is slide 3, before the data, with the impossibility and the citation.
- **G-V17-THEORYFIG:** the theory figure is on the main Welfare slide, and its caption has no section reference.

**Result.** 23/23 pass. All four negative controls fire:

| Control | Injected | Result |
|---|---|---|
| NC-LABEL | "S11" | label check fails |
| NC-REGISTRY | "12.34" | registry check fails |
| NC-STYLE-TITLE | a seven-word title | style check fails |
| NC-STYLE-PARAGRAPH | none: runs the paragraph check on V16's own rendered PDF | finds 3 paragraphs over three lines; V16 also has 15 titles over six words |

**Rehearsal script.** `reports/rehearsal_pack_v1.md` is regenerated to the V17 numbering and is identical to `reports/rehearsal_pack_v17.md`.
