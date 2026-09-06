# The JMP seminar deck

*Unequal Job Opportunities and the Measurement of Welfare Inequality.*

Built from the frozen content document
[manuscript/JMP_seminar_deck_content_v1.md](../manuscript/JMP_seminar_deck_content_v1.md)
(Goal-1 R-256) against the frozen figure and table set at JMP commit `b1dea12`.

**No science here.** This is typesetting. Every number on every slide is a
generated macro read from a named seminar-sprint artefact; every figure is a
PDF copied from the frozen sprint figure set. Nothing is computed, re-estimated
or typed by hand.

## Files

| file | what it is |
|---|---|
| `JMP_seminar_deck_v1.tex` | the deck — 23 running-order slides plus 5 backups |
| `JMP_seminar_deck_v1_25min.tex` | driver: sets `\ShortDeck` and inputs the deck |
| `JMP_seminar_deck_v1_rehearsal.tex` | driver: sets `\RehearsalDeck` and inputs the deck |
| `jmp_beamer_preamble.tex` | shared preamble — theme, colours, macros |
| `deck_numbers_v1.tex` | **generated.** 116 number macros. Do not edit. |
| `make_deck_macros_v1.py` | generates `deck_numbers_v1.tex` from the sprint artefacts |
| `verify_deck_v1.py` | checks figures, macros, frame/page counts, and the log |
| `build_deck_v1.sh` | regenerates, builds all three variants, verifies |
| `figures/` | the 19 figure PDFs, copied from the frozen sprint set |
| `reference/Theory_talk/` | the companion theory talk, the source of the shared style |

## Building

```sh
export PATH="$LOCALAPPDATA/Programs/MiKTeX/miktex/bin/x64:$PATH"   # Windows
./build_deck_v1.sh              # all three, then verify
./build_deck_v1.sh full         # 45-minute projection deck only
./build_deck_v1.sh short        # 25-minute running order only
./build_deck_v1.sh rehearsal    # presenter build only
```

`latexmk` needs `perl`; Git Bash supplies it on Windows.

Output lands in `build/`:

| build | pages | what it is |
|---|---|---|
| `JMP_seminar_deck_v1.pdf` | 32 | the 45-minute deck: 28 frames + 4 overlay steps |
| `JMP_seminar_deck_v1_25min.pdf` | 24 | the 25-minute running order: 21 frames + 3 overlay steps |
| `JMP_seminar_deck_v1_rehearsal.pdf` | 32 | slide left, speaker notes right, for a second screen |

Put the rehearsal PDF on the presenter screen and the projection PDF on the beamer.

## The two lengths

Each running-order frame carries one of three tags, so the two variants come
from one source and cannot drift:

| tag | 45 min | 25 min |
|---|---|---|
| `\shortdeck{...}` | kept | kept |
| `\longdeck{...}` | kept | **cut to backup** — slides 9, 12, 17, 18, 22 |
| `\mergedaway{...}` | kept | **merged away** — slide 7 into 6, slide 11 into 10 |

`\mergedonly{...}` marks content that appears only in the merged form of a
slide, so the short deck loses no message. 23 − 5 − 2 = **16 slides**, the
frozen plan's figure.

## Numbers

`make_deck_macros_v1.py` reads the frozen artefacts under
`MNL/experiments/JMP_SEMINAR_SPRINT/` and writes one `\newcommand` per number,
grouped by source. The provenance table at the end of the content document is
the authority for which artefact backs which slide.

Regenerate after any change to the sprint tables:

```sh
python make_deck_macros_v1.py
```

The generator refuses a duplicate macro name and a name that is not
letters-only (TeX would split `\FooB2` after the `B`).

## Style, reused from the theory talk

The preamble carries over, verbatim, the conventions of the companion theory
talk `reference/Theory_talk/slides/Presentation.tex` (*Jobs and Well-Being
Measurement*, Haydar and Maniquet), so the two decks read as one visual family.
Elements marked `[THEORY-TALK]` in `jmp_beamer_preamble.tex`:

- `metropolis` theme with the `deepred` accent `RGB(150,25,35)` on the frame
  title, progress bar and title separator;
- `\metroset{numbering=fraction}` — the *current/total* frame number;
- `appendixnumberbeamer`, so the backups do not inflate the running-order total;
- visible deep-red hyperlink colours for rehearsal;
- the `pgfpages` second-screen note view and the ragged-right note-page
  template (retuned here: this deck's notes are longer);
- the two-agent sketch palette `agenti` (red) / `agenth` (blue), reused for
  the two households of slides 2 and 14;
- the package set: `inputenc`, `babel`, `amsmath`, `amssymb`, `amsfonts`,
  `booktabs`, `tikz` with `decorations.pathreplacing` and `arrows.meta`.

Backup slide **B5** reuses the theory talk's compensation-versus-responsibility
frame and its $W^{1}$ construction, cited to the companion paper and kept as a
separate slide rather than merged into this deck's own welfare slide 14.

## Notation

Audience-facing channel names are words, never letters: *preferences*, *job
access*, *earning opportunities*, *household endowments and needs*. The
preamble defines `\pref`, `\acc`, `\earn`, `\needs`, `\env` so each is spelled
and coloured the same way everywhere.

Theory-paper symbols — $W$, $z$, $R$, $A$, $\mathbf y$, $W^{1}$ — appear only
on B5, where the companion paper is cited.
