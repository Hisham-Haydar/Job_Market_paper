# JMP — V13 to V14 theory figure release, v1

One figure restored; no number, table or other figure changed. V13 is untouched.

## 1. Where the figure was found

- **Stored image.** `manuscript/figures/v3/theory_w1.png` (copied to
  `manuscript/figures/v5/theory_w1.png`, first committed in `e27fc25`). Its
  build caption describes it as "adapted with permission from the companion
  theory project's presentation". It was embedded in reports V4 to V11
  (`data-fig="theory_w1"`).
- **When it was lost.** From V7 onward it survived only inside the inherited
  "Technical record: Introduction" appendix copy. **V12 deleted that copy as a
  duplicate, and the figure went with it.** This was an error in the V12
  structural pass; V13 did not restore it.
- **No generator survives.** `build_v3.py` and `build_v5.py` only copy the PNG;
  no plotting or TikZ source exists in the builders or in
  `Theory_other_project/jobs_and_wellbeing.tex`.

## 2. Regenerated, not reused

The stored image fails the brief:
- It draws two different preference relations (R_i and R_h) rather than one.
- Several labels overlap: y(k) collides with its marker, and R_i and R_h collide with y(ℓ) and y′(ℓ).
- It carries measure notation from the slides.

`reports/research_story_build/make_v14_theory_figure.py` draws the construction
afresh from Measure 1 of the companion theory paper:
- one illustrative preference relation shared by both individuals;
- Individual 1 with ability set {j, k}, Individual 2 with {k, ℓ};
- in each panel: the attained bundle, the bundles indifferent to it, the same consumption w on every job in the own set, the preferred job at equal consumption (circled), and w marked as the money metric;
- jobs outside the own set greyed.

The axes carry no numeric ticks; the figure states on its face that it is a
theoretical illustration with no estimated values or household data. It is
saved as a 256-colour palette PNG
(`manuscript/figures/v14/fig_v14_theory_own_set.png`, SHA-256
`c569c92352cd2b23b154d98aef79fa4fbce48598272704a394330e0a998094dd`).

## 3. Rendered caption

"Own-set equal-consumption equivalents: the theoretical construction from the
companion theory paper. Two individuals with the same preferences but different
ability sets attain different bundles. For each individual a common consumption
level is assigned to every job in their own set; the level at which the
preferred reference job becomes indifferent to the attained bundle is the money
metric. Adapted from Haydar and Maniquet (2026), work in progress. This is the
deterministic construction; the estimated ex-ante measure is its extension,
defined in Section 3."

Two adjustments to the PI's wording:
- **Section reference.** The ex-ante measure is defined in Section 3 (Perspective 2), so "Section 4" became "Section 3".
- **"the estimated measure" became "the estimated ex-ante measure".** V14 reports two estimated measures, and only the ex-ante one extends the own-set construction. On this domain, the attained-bundle measure's reference collapses to non-employment.

## 4. Placement and surrounding text

The figure sits in Section 3 immediately after the two-perspective framing
sentence and before "Perspective 1 — ATT". It is preceded by a short paragraph
that explains the construction and states that the figure contains no estimated
value, household data or result. It is followed by a paragraph stating that:
- the attained-bundle measure's reference is non-employment, which on the current empirical domain every household prefers when all jobs pay the same;
- the ex-ante measure applies the equal-consumption idea to the estimated opportunity prospect.

In the gallery, the same figure and bridging paragraph follow the welfare
panel's framing sentence.

## 5. Nothing else changed

- `story_v14.generated.md` differs from V13 only by the two paragraphs and the figure.
- The number-to-source gate checks every embedded image other than the theory figure against V13, in both surfaces, and finds them byte-identical. That includes the matched-household figure and the four V13 figures.
- The registry equals V13 on every key and adds none.

## 6. Gates (`reports/v14_release_gate_summary.md`, all PASS)

**Caption gate.** The scope was already limited to captions that name an access channel, so the theory caption passes on its own. Two controls both fail as required:
- a planted outdated access definition;
- the same violation planted *inside* the theory caption, which shows there is no blanket exemption.

**Reader gate.** The author and construction names ("Haydar and Maniquet", "own-set equal-consumption") are exempted only inside this exact caption; anywhere else in the rendered text they still fail.

**Other checks:**
- the other three negative controls (banned terms, Stage A status, section titles) still fail as required;
- 57 reader checks, including figure order and the surrounding statements;
- 41 number-to-source checks, including no numbers on the theory figure, palette encoding, not the old image, and other images byte-identical;
- render, sync, deck and notebook regressions;
- V9–V13 byte-preservation.

## 7. Hashes

- `JMP_research_story_report_v14.html` — `293baba49dcff7f40df6d2be423f0caa2c14f110aaaa3246599368d6a9b0b4af`
- `JMP_results_gallery_v14.html` — `ea608d57cc4a3742fe3b13a76b16c6135fd0125d78f63a969cd077da8cf8901e`
