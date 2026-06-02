# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software project** — it is the working repository for an economics **job market paper (JMP)**. The bulk of the content is PDFs, Markdown notes, LaTeX, and a small set of Python/PowerShell utility scripts that maintain a literature corpus and presentation assets. There is no application to build, no test suite, and no package manifest. "Code" here means document-processing and figure-generation pipelines.

When working here, the primary value is usually editing/synthesizing prose and maintaining the literature pipeline — not shipping software. Treat `.md` design documents as first-class artifacts.

## The paper in one paragraph

The JMP asks: *how much of observed inequality in money-metric well-being is due to unequal job opportunities rather than heterogeneous preferences?* It models labor supply as a choice among **latent job packages** (a RURO / latent-jobs discrete-choice model), computes a money-metric welfare measure relative to the **constrained feasible job set**, and decomposes welfare inequality into an **opportunity** component and a **preference** component using an order-independent (Shapley-style) rule. Tax-benefit microsimulation feeds the budget mapping but is an input, not the contribution. The single-country empirical setting is **France**. See [JMP.md](JMP.md) for the authoritative project framing (central question, methods, what's done, what remains).

This opportunity-vs-preference framing recurs throughout the materials and even drives the figure color scheme (`C_OBS` = opportunity/observed = dark blue, `C_PRED` = preference/predicted = orange in [Presentation_mock/03_assets/_make_figures.py](Presentation_mock/03_assets/_make_figures.py)). Keep that distinction central when editing or generating content.

## Directory roles

These roles are documented in [Design/README_JMP_workspace.md](Design/README_JMP_workspace.md) and matter because content is organized by *function*, not by topic:

- `Literature/` — the literature corpus: source PDFs, per-paper Markdown extractions, and the scripts that process them. The corpus is organized into six conceptual "shelves" (defined in [Literature/make_shelves.py](Literature/make_shelves.py)): RURO/latent-jobs labor supply, welfare measurement for discrete choice, equivalent income / beyond-GDP, responsibility/compensation/fairness, inequality of opportunity & decomposition, microsimulation & tax-benefit policy.
- `Design/` — framing and concept documents (abstracts, concept notes, intro skeleton, positioning memos). Files are explicitly versioned by filename suffix (`_v1`, `_v2`, `_v3_france`); the highest version / `_france` variant is current.
- `Prototype/` — early empirical/scope memos before they become production work (France setting, status, scope-decision).
- `Deep_reports/` — long-form deep research reports (gap checks, roadmap, lit reviews).
- `Presentation_mock/` — seminar deck: `beamer/` (LaTeX deck) and `03_assets/` (figure-generation scripts + generated PNG/CSV outputs).
- `Theory_other_project/` — a *separate* theory project. Keep it distinct from the JMP literature stream.
- `Code/` — intended for reproducible analysis code; currently empty (the empirical model is not yet implemented).

## Versioning convention

Design and prototype documents are versioned in the filename, not via git history (the repo has a single commit). When asked to revise a document, prefer creating the next `_vN` rather than overwriting, and look for `_france`-suffixed variants which supersede generic ones.

## Common workflows / commands

All scripts run from Windows with PowerShell as the shell. Python scripts use only the standard library plus `matplotlib`/`numpy` (figures) and `openpyxl` (shelves spreadsheet).

**Literature pipeline** (run from `Literature/`):
- Re-extract Markdown from source PDFs (cleans JSTOR/Wiley/SSRN boilerplate; requires MiKTeX `pdftotext` at the hardcoded path in the script):
  `python Literature/improve_md_extractions.py`
- Concatenate per-paper extractions in `md_extractions/` into one indexed file `full_literaterature.md`:
  `python Literature/build_full_literaterature.py` (override with `--input-dir`, `--output-file`, `--document-title`)
- Convert `Literature_collection.md` → compilable `Literature_collection.tex` (handles LaTeX escaping and math-span preservation):
  `python Literature/md_to_tex.py` (input/output paths are hardcoded at the top of the file)
- Regenerate the six-shelf library spreadsheet `JMP_Library_Shelves.xlsx`:
  `python Literature/make_shelves.py`
- Batch-print the PDF corpus to a physical printer via Adobe Reader, with a CSV log/checklist and retry logic (Windows-only):
  `Literature/Printing.ps1`

**Presentation figures** (run from `Presentation_mock/03_assets/`):
- `python Presentation_mock/03_assets/_make_figures.py` and `python Presentation_mock/03_assets/_make_elasticity_figure.py` regenerate the slide PNGs. Both write to a hardcoded absolute `OUT` path and force the `Agg` backend. The plotted numbers are **mock/illustrative values** hardcoded in the scripts (the empirical model is not yet estimated) — do not treat them as results.

**Presentation deck**:
- `Presentation_mock/beamer/main.tex` is a self-contained Beamer deck; all slide text lives in that one file. Compile with **pdfLaTeX** (Overleaf-ready, standard packages only). See [Presentation_mock/beamer/README_overleaf.md](Presentation_mock/beamer/README_overleaf.md).

## Gotchas

- **Hardcoded absolute paths.** Most scripts embed `C:\Users\hisham\Desktop\Job_Market_paper\...` paths and tool locations (e.g. MiKTeX `pdftotext`, Adobe Reader). Editing for portability means changing those constants, not assuming CWD-relative behavior.
- **Encoding.** Some top-level structure files (e.g. `JMP_project_files_structure.md`) are UTF-16; treat `.md` files as potentially UTF-16 when raw bytes look doubled. The Python scripts standardize on UTF-8 with `errors="replace"`.
- **"full_literaterature"** — the misspelling is intentional/consistent across the script and its output file; match it, don't "fix" it, or the pipeline breaks.
- The figure numbers, elasticities, and decomposition shares in `03_assets/` and the beamer deck are placeholders for a not-yet-run empirical model.
