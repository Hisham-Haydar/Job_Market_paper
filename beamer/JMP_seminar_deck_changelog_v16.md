# Seminar deck changelog — V16 against r6

**What V16 is.** A rebuild, not an edit. `JMP_seminar_deck_r6.tex` and its PDF are unchanged. V16 has 18 slides and no backup appendix. r6 had 32 pages: 16 main frames, 10 backup frames and 6 section divider pages. V16's content comes only from `reports/JMP_research_story_report_v15.html` and `reports/JMP_results_gallery_v15.html`.

**New V16 slide order.** Real-world inequality → literature gap → research question → latent-jobs model → welfare, EA and ATT → the decomposition → results → limitations → conclusion.

## Added

- **Real-world inequality slide (2).** Uses consumption Ginis and attained-bundle well-being Ginis, reported within each population.
- **Literature-gap slide (3).** Covers three strands: latent-jobs labour supply, money-metric welfare with heterogeneous preferences, and Shapley decomposition.
- **Research-question slide (4).** Carries the brief's research question and three subquestions verbatim.
- **Systematic-utility equation (5).** Shown with the child term described as a reduced-form time-constraint shifter.
- **Choice law with the opportunity density (6).** The four opportunity blocks are described in words, and local access is defined.
- **Matched-household illustration (7).** Uses the V15 figure.
- **Subquestion-1 evidence (8).** Compares the model with the common-opportunity benchmarks: free coordinates, population fit and the criterion gap.
- **Theory figure with its V15 caption (9).** The caption names the companion paper; this is intentional.
- **Ex-ante (EA) welfare equation (10).** Presented first, as the opportunity-prospect perspective, and flagged as a normative position.
- **Attained-bundle (ATT) equation (11).** Presented as the benchmark.
- **"The two measures answer different welfare questions" (12).** A comparison table. The slide states that neither perspective is designated primary.
- **Decomposition slide (13).** Defines the P, A and B channels and gives the Shapley equation. It states on the slide that household resources, needs and composition are held fixed, that access is local access and not total opportunity, and that the decomposition is preliminary and makes no causal claim.
- **Central-result slide (14).** Reuses the V15 ATT-versus-EA figure (`manuscript/figures/v13/fig_v13_central_result.png`) unchanged.
- **EA results table (15).** Access and earnings Gini points, their combined share of baseline inequality, and the access-to-earnings ratio for single adults.
- **ATT results table (16).**
- **Limitations slide (17).** States on the slide: preliminary, no causal claim, no parameter uncertainty yet, and preferences not equated with responsibility.
- **Conclusion slide (18).** Answers the three subquestions.
- **Spoken notes.** Every equation slide's note opens with one spoken interpretation line.

## Removed

- **Old question and contribution slides (r6 2–3).** They were framed around a common-choice-set question and one welfare measure.
- **Data-frame slide (r6 4).** It described estimation draws and diagnostic panels.
- **Package-diagram and proposal-corrected likelihood slides (r6 5–6).** Replaced by the utility and choice-law equations.
- **Parameter-count and objective table (r6 7).**
- **Fit slides (r6 8–9).** The extensive-margin accuracy chart and the calibration-by-decile chart. Fit is now covered briefly in the slide-8 notes.
- **Estimated access and earning-kernel figures (r6 10–11).** Replaced by the matched-household illustration.
- **Single-measure welfare slides (r6 12–13).** These included the headline that named the theory measure. V16 never calls the ex-ante measure "Measure 1" or by the companion paper's name.
- **Equivalised baseline distribution slides (r6 14–15)** and the feedback-request slide (r6 16).
- **All 10 r6 backup slides.** These were:
  - the decomposition confined to backup, with its scope wording;
  - the unequivalised verification slides;
  - the pre-registered checks;
  - quadrature adequacy;
  - the evidence-scope slide.
- **Section divider pages.**
- **The r6 statement that the ex-ante metric was "being reconstructed" with no results.** V15 has certified ex-ante results.

## Numbers, figures and gates

- **Numbers.** `make_deck_numbers_r6.py --v16` writes `deck_numbers_v16.tex` with 51 macros. It reads only `reports/numbers_of_record_v15.json` and formats values; it does no arithmetic. The r6 path is unchanged.
- **Figures.** V16 uses three V15 image files, included in place. Each is byte-identical to an image embedded in the V15 report and gallery. r6's generated figures are not used.
- **Gates.** `verify_deck_r6.py --deck v16` runs 18 gates and 2 negative controls. The r6 gates still run by default and still pass 19/19.
  - Kept from r6: retired tokens, the out-of-scope ban, typed numerals, assets, lineage, confusion-matrix wording, no pooled figure, and no side-by-side comparison.
  - New: every numeral on every slide must resolve to a V15-registry entry, plus the structure, question, equation, central-result, required-statement, no-primacy, caption, internal-label and no-80–90% gates.
- **Rehearsal script.** `reports/rehearsal_pack_v1.md` is regenerated to V16 numbering, identical to `reports/rehearsal_pack_v16.md`. It no longer describes r6 or r7.
