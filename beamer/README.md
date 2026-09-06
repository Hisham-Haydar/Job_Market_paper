# The JMP seminar deck ? v4

The [authoritative content](../manuscript/JMP_seminar_deck_content_v2.md) supplies the headlines, on-slide prose and running speaker notes. This implementation preserves that text. The final verbatim brief supersedes the earlier 12-word body limit and 23-message plan.

Open the [full deck](build/JMP_seminar_deck_v1.pdf), [25-minute deck](build/JMP_seminar_deck_v1_25min.pdf), or [rehearsal deck](build/JMP_seminar_deck_v1_rehearsal.pdf). The [review report](DECK_V4_REVIEW.md) contains the complete per-slide table, verification results, source caveats and figure provenance.

| Build | Running frames | Backup frames | Extra overlay pages | PDF pages |
|---|---:|---:|---:|---:|
| Full | 22 | 8 | 1 | 31 |
| 25-minute | 15 | 8 | 0 | 23 |
| Rehearsal | 22 | 8 | 1 | 31 |

The short order is **1, 2, 3, 5, 6, 7, 9, 12, 13, 14, 15, 16, 17, 18, 22**. It uses the existing driver and frame tags. Slide 19 has the only two-step running build. The rehearsal PDF places the unchanged projection on the left and the supplied speech on the right. Slide 22 has no supplied speech, so its note is empty.

## Build

From this directory:

```powershell
python build_deck_v4.py all
python build_deck_v4.py full
python build_deck_v4.py short
python build_deck_v4.py rehearsal
```

The existing `./build_deck_v1.sh [all|full|short|rehearsal]` entry point calls the same builder. A latexmk failure stops the build; no return code is ignored. On Windows, the builder adds Git's Perl directory to the child process PATH. MiKTeX may need ordinary Windows permissions to access its own cache/log directories.

Dependencies: Python, the packages in `requirements-beamer.txt`, latexmk, pdflatex, pdftotext, and the existing Beamer/Metropolis/TikZ LaTeX packages. This workspace has the Python plotting/PDF dependencies installed in the ignored `build/python_deps/` directory. To reproduce that installation:

```powershell
python -m pip install --target build/python_deps -r requirements-beamer.txt
```

The build reads the sibling `MNL/experiments/JMP_SEMINAR_SPRINT/` tree. It does not modify it. It regenerates number macros, renders only missing slide panels, compiles the three existing TeX drivers with latexmk, exports each text layer with `pdftotext -layout`, runs verification and writes the review report.

## Files

| File | Role |
|---|---|
| `JMP_seminar_deck_v1.tex` | v4 deck; one source for all variants |
| `JMP_seminar_deck_v1_25min.tex` | existing short-deck driver |
| `JMP_seminar_deck_v1_rehearsal.tex` | existing second-screen driver |
| `jmp_beamer_preamble.tex` | shared style, unchanged from v3 |
| `theory_model_figure.tex` | companion drawing; switches replace the primitives on slide 5 |
| `make_deck_macros_v1.py` | source-backed numbers at the author's display precision |
| `deck_numbers_v1.tex` | generated commands; do not edit manually |
| `make_slide_figures_v1.py` | original figure kit plus the three missing panels |
| `figures/slides/` | 12 active single-panel PDFs |
| `figures/unused_v3/` | five preserved, unused v3 panels |
| `deck_content_v4.py` | reads authoritative headlines and speech |
| `verify_deck_v1.py`, `verify_content_v4.py` | verifier entry point and v4 gates |
| `build_deck_v4.py`, `build_deck_v1.sh` | native and shell build entry points |
| `slide_table_v1.py` | displays the PDF-derived table; supports `--csv` |
| `write_deck_report_v4.py` | builds the review report from verification evidence |

## Verification

The original gate families remain: paths, macros, frame/page counts, logs, forbidden labels, text volume and figure fonts. The final content replaces the old fixed word cap with exact authored-text checks. Additional gates compare the PDF headline rectangle with the corresponding content string, check captions and prose, compare the source notes and rendered rehearsal speech, enforce the exact short order, reject hand-typed quantitative numerals and confirm that the shared preamble is unchanged.

```powershell
python verify_deck_v1.py
python slide_table_v1.py --csv slide_table_v1.csv
```

[Machine-readable verification](build/verification_v4.json) and the [per-slide table](build/slide_table_v4.json) are committed with the PDFs. Word counts include rendered headline, body, chart and table text; navigation and notes are excluded. See the review report for the source discrepancy on slide 18: its authored 0.2 s.e. claim corresponds to the 100?400 comparison, while its displayed range begins at 50.

## Reused theory style

Metropolis, deep-red RGB(150,25,35), the red/blue agent palette, current/total frame numbering, appendix handling, visible-link colours, the package set and second-screen notes remain shared with the companion talk. Main-file layout adjustments allow the longer verbatim headlines and captions to fit. The common theory figure appears only on slides 4 and 5; B5 keeps the separately cited welfare-family material.

## Text exports

- [Full](build/JMP_seminar_deck_v1_text.txt)
- [25-minute](build/JMP_seminar_deck_v1_25min_text.txt)
- [Rehearsal](build/JMP_seminar_deck_v1_rehearsal_text.txt)
