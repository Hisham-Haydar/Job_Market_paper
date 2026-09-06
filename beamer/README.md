# The JMP seminar deck

*Unequal Job Opportunities and the Measurement of Welfare Inequality.*

Frame order and messages from the frozen content document
[manuscript/JMP_seminar_deck_content_v1.md](../manuscript/JMP_seminar_deck_content_v1.md)
(Goal-1 R-256), against the frozen figure and table set at JMP commit `b1dea12`.

**No science here.** This is typesetting. Every number on every slide is a
generated macro read from a named seminar-sprint artefact; every visual is
re-rendered from the same data CSVs the paper figures use. Nothing is computed,
re-estimated or typed by hand.

## The slide grammar

Every frame is:

> a **headline** that states the message as a sentence and carries its one
> number, plus **one visual or one equation**.

Body text is at most **twelve words** — a single caption line at most. Every
remaining number, every qualifier and all provenance live in `\note{}`. There
are no number-soup lines on any slide. Overlays appear only where a figure or an
argument builds.

`python slide_table_v1.py` prints the per-slide table — headline, visual or
equation, body-word count, 25-minute disposition — and `--csv` writes it out.

## Files

| file | what it is |
|---|---|
| `JMP_seminar_deck_v1.tex` | the deck — 23 running-order slides plus 8 backups |
| `JMP_seminar_deck_v1_25min.tex` | driver: sets `\ShortDeck` and inputs the deck |
| `JMP_seminar_deck_v1_rehearsal.tex` | driver: sets `\RehearsalDeck` and inputs the deck |
| `jmp_beamer_preamble.tex` | shared preamble — theme, colours, slide grammar |
| `deck_numbers_v1.tex` | **generated.** 123 number macros. Do not edit. |
| `make_deck_macros_v1.py` | generates `deck_numbers_v1.tex` from the sprint artefacts |
| `make_slide_figures_v1.py` | generates `figures/slides/` from the sprint data CSVs |
| `slide_table_v1.py` | prints the per-slide table |
| `verify_deck_v1.py` | 20 checks: figures, macros, counts, logs, text layer, words, fonts |
| `build_deck_v1.sh` | regenerates everything, builds all three variants, verifies |
| `figures/slides/` | the 17 slide-native figure PDFs |
| `figures/` | the paper-style figure PDFs, kept for reference |
| `reference/Theory_talk/` | the companion theory talk, the source of the shared style |

## Building

```sh
export PATH="$LOCALAPPDATA/Programs/MiKTeX/miktex/bin/x64:$PATH"   # Windows
./build_deck_v1.sh              # all three, then the table, then verify
./build_deck_v1.sh full         # 45-minute projection deck only
./build_deck_v1.sh short        # 25-minute running order only
./build_deck_v1.sh rehearsal    # presenter build only
```

`latexmk` needs `perl`; Git Bash supplies it on Windows.

| build | pages | what it is |
|---|---|---|
| `JMP_seminar_deck_v1.pdf` | 35 | the 45-minute deck: 31 frames + 4 overlay steps |
| `JMP_seminar_deck_v1_25min.pdf` | 28 | the 25-minute running order |
| `JMP_seminar_deck_v1_rehearsal.pdf` | 35 | slide left, speaker notes right, second screen |

## Slide-native figures

`make_slide_figures_v1.py` renders `figures/slides/<name>_slide.pdf` from the
**same data CSVs** as the paper figures, under a slide style rather than a paper
style:

- **one panel per file** — multi-panel paper figures are split, and each slide
  takes the panel that carries its message;
- **16:9 canvas** (13.33 × 7.5 in), so a figure fills a widescreen frame;
- **every text element ≥ 18 pt** at slide scale;
- **no figure title, no footnote, no status or provenance stamp, and no
  internal label anywhere** — not in the source and not in the PDF text layer;
- minimal legends, and the house colours of the paper figure kit.

Internal names (`C_P`, `C_A`, `S8`, `LOC4`, the arm keys) are mapped to audience
words *before* they can reach an axis, a legend or a tick, through a vocabulary
that **raises on an unknown key** rather than passing it through. The permitted
words are: *final model / benchmark*; *preferences / job access / earning
opportunities / household endowments and needs*; *female reference / male
reference*.

## Equation slides

Five frames carry an equation instead of a figure, in the paper's notation:

| where | equation |
|---|---|
| B0 (backup) | the preference block, Box–Cox in leisure and consumption |
| slide 5 | the opportunity density `g = gᴱ gᴴ gᴼᶜᶜ gᵂ`, four factors named in words |
| slide 6 | the estimator `V = u + log g − log q`; *q is computation, g is economics* |
| slide 14 | the welfare measure `W¹` and the four states in a 2×2 grid |
| slide 15 | the decomposition identities, with the words beside the symbols |

## The two lengths

Each running-order frame carries one of three tags, so the two variants come
from one source and cannot drift:

| tag | 45 min | 25 min |
|---|---|---|
| `\shortdeck{...}` | kept | kept |
| `\longdeck{...}` | kept | **cut to backup** — slides 9, 12, 17, 18, 22 |
| `\mergedaway{...}` | kept | **merged away** — slide 7 into 6, slide 11 into 10 |

`\mergedonly{...}` marks content that appears only in the merged form of a
slide, so the short deck loses no message. 23 − 5 − 2 = **16 slides**.

## Verification

`verify_deck_v1.py` runs 20 checks and is part of every build:

1. every slide figure resolves; none is unused; no paper-style figure is left
   on a slide;
2. every number macro is generated, with no near-miss and no orphan;
3. the frame, overlay and page counts agree, and the two lengths are 23 and 16;
4. all three logs are clean — 0 errors, 0 overfull, 0 underfull;
5. **the PDF text layer** of every built PDF and every slide figure carries no
   internal label (`pdftotext` + the forbidden-label regex `S8|LOC4|C_P|C_E|C_A|
   C_B|C_D|R-2|PENDING|PROVISIONAL|EXPLORATORY|deputy|ruling`);
6. no frame carries more than 12 words of body text, counting neither the
   headline nor an equation, diagram or table (those are the visual);
7. the slide figures were rendered with every font ≥ 18 pt on a 16:9 canvas, as
   recorded by the figure kit in `figures/slides/slide_style_v1.json`.

## Style, reused from the theory talk

The preamble carries over, verbatim, the conventions of the companion theory
talk `reference/Theory_talk/slides/Presentation.tex` (*Jobs and Well-Being
Measurement*, Haydar and Maniquet). Elements marked `[THEORY-TALK]` in
`jmp_beamer_preamble.tex`: the `metropolis` theme with the `deepred`
`RGB(150,25,35)` accent, the current/total frame fraction,
`appendixnumberbeamer`, visible deep-red hyperlinks, the `pgfpages`
second-screen note view and its note-page template, the `agenti`/`agenth`
two-agent palette, and the package set.

Backup slide **B5** reuses the theory talk's compensation-versus-responsibility
frame and its `W¹` construction, cited to the companion paper and kept as a
separate slide rather than merged into the deck's own welfare slide.

## Notation

Audience-facing channel names are words, never letters: *preferences*, *job
access*, *earning opportunities*, *household endowments and needs*. The
preamble defines `\pref`, `\acc`, `\earn`, `\needs`, `\env` so each is spelled
and coloured the same way everywhere, and the figure kit uses the same colours.

Theory-paper symbols — `W`, `z`, `R`, `A`, `y`, `W¹` — appear on B5, where the
companion paper is cited, and in the welfare-measure equation that B5 explains.
