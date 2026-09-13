# Beamer JMP Presentation — Overleaf Guide

## How to compile

1. Upload the entire `beamer/` folder to Overleaf (or create a new project and upload all files).
2. Set the compiler to **pdfLaTeX** (Menu > Compiler > pdfLaTeX).
3. Compile `main.tex`.

No special packages beyond a standard TeX Live / Overleaf installation are needed.
Required packages (all standard): `beamer`, `lmodern`, `booktabs`, `graphicx`, `tikz`, `appendixnumberbeamer`, `array`, `multirow`.

## File structure

```
beamer/
  main.tex                  -- full deck (all slide text lives here)
  figures/
    figure_fit.png
    figure_decomposition_shares.png
    figure_responsibility_sensitivity.png
    figure_elasticities.png
  README_overleaf.md        -- this file
  TODO_notes.md             -- manual finishing touches still needed
```

## Slide map

### Front-loaded 15-minute core (slides 1-7)

| Slide | Title | Role |
|-------|-------|------|
| 1 | Title page | Opening — clean, no ribbon |
| 2 | In one slide: model, welfare, decomposition, result | Paper in a nutshell |
| 3 | Outcomes do not reveal the same thing for everyone | Why economists should care |
| 4 | This paper sits at the intersection of four literatures | Named-paper literature positioning |
| 5 | Existing papers stop too early | What they do vs what I do |
| 6 | Belgium is the clean first application | Design and sample |
| 7 | Unequal opportunities explain a large share of welfare inequality | **Main result** |

### Continuation (slides 8-22)

| Slide | Title | Role |
|-------|-------|------|
| 8 | The raw data already show structured opportunity differences | Data motivation |
| 9 | The 16 job packages make latent opportunities operational | Model structure |
| 10 | Identification is simple to state: ranking versus access | Identification |
| 11 | Preference heterogeneity is meaningful, but not a catch-all residual | Preference estimates |
| 12 | The opportunity estimates reveal a real labor-market structure | Opportunity estimates |
| 13 | The benchmark misses exactly the gradients... | Fit / SQ1 revisited |
| 14 | Elasticities validate the structure... | Secondary behavioral validation |
| 15 | Welfare inequality is not the same object as income inequality | Welfare distribution |
| 16 | The decomposition is built from transparent counterfactuals | Counterfactual logic |
| 17 | The main decomposition result is balanced, not rhetorical | Core decomposition |
| 18 | The opportunity contribution depends on responsibility assumptions... | Responsibility sensitivity |
| 19 | Decomposition matters more than welfare levels alone | Why decomposition |
| 20 | The Belgium baseline is a paper; Europe is an agenda | Scope / scale-up |
| 21 | The paper is narrow by design, not narrow by ambition | Design strategy |
| 22 | What the committee should remember | Closing |

### Appendix / backup (9 slides)

| Appendix | Content |
|----------|---------|
| 1 | Full named-paper literature map |
| 2 | Full "what they do / what I do" matrix |
| 3 | Sample construction |
| 4 | Full structural estimates (preference + opportunity) |
| 5 | Benchmark comparison by cell |
| 6 | Welfare construction schematic |
| 7 | Full decomposition table |
| 8 | Responsibility-sensitivity table |
| 9 | Elasticity table and definition |

## Source-of-truth inputs

| Priority | Type | Source file |
|----------|------|-------------|
| 1 | Structure | `01_outline/mock_jmp_slide_outline_v9.md` |
| 2 | Script (front 15 min) | `04_script/mock_jmp_front15_script_v6.md` |
| 3 | Script (continuation) | `04_script/mock_jmp_continuation_script_v5.md` |
| 4 | Results | `02_results/mock_jmp_completed_results_v1.md` |
| 5 | Elasticities | `02_results/mock_jmp_elasticity_addon_v1.md` |
| 6 | Literature | `01_outline/literature_architecture_v1_deep_Report.md` + `Literature_architecture_v1_reply.md` |

## Where to edit slide text

All slide content is in `main.tex`. Search for `SLIDE 1` through `SLIDE 22` and `APPENDIX 1` through `APPENDIX 9` in comments to jump to specific slides.

## Where figures and tables come from

All four PNG figures were generated from the quantitative source-of-truth files and stored in `03_assets/`. The `figures/` subfolder inside `beamer/` contains copies for compilation.

To update a figure: regenerate it in `03_assets/` and copy it to `beamer/figures/`.

## Color conventions

- `cblue` (#2c5f8a): opportunity / primary emphasis / key numbers
- `corange` (#e07b3a): preference / secondary emphasis / contrast
- `cgrey` (#6b6b6b): annotations / de-emphasized text

## Section navigation bar

The CambridgeUS theme renders the current section in the header bar. Sections are:
Introduction | Literature | Design & Result | Data & Model | Estimation | Decomposition | Conclusion
