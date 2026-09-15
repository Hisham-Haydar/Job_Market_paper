# Seminar deck change log: V18 against V17

## Scope and sources

V18 is a bounded expansion of V17. V17, V16 and r6 are unchanged, and the V17 style is kept: short conceptual titles, formal objects on slides, narration in notes.

**Numbers.** `make_deck_numbers_r6.py --v18` writes 415 macros. It reads only `reports/numbers_of_record_v15.json`:

| Kind | Count | What they are |
|---|---:|---|
| Registry entries | 131 | Individual values from the registry |
| Gallery fields | 208 | Coefficient estimates and standard errors, coefficient labels, sample funnel |
| Derived | 46 | Ratios and sums of registry values; each records its formula and input keys |

- **No re-running.** No model is evaluated, re-estimated or re-priced.
- **Retired record never read.** `registry.discussion_tables` holds the retired record and is not read.
- **Excluded tables.** `registry.gallery.fit` is not used. Its hours bands belong to an older lineage and do not match V15's corrected moments.

**Figures.** V18 uses five V15 image files, each byte-identical to an image embedded in the V15 report or gallery: the theory figure, the central result, matched households, fit by margin, and the marginal rate of substitution.

## A. Title slide

The title slide is sparse and follows ruling A: title, subtitle, author, "University of Luxembourg & LISER", "4th-Year PhD Workshop", "Discussant: Sebastian Dobre". It contains no internal names.

## B. Decomposition: three main slides replace V17's "Results" slide

**1. How much is associated with opportunities?** (slide 14)
- A 2×2 display: ex-ante prospect and attained bundle, for single adults and couples.
- The large equivalised values are 20.3%, 7.9%, 1.9% and 3.5%.
- The raw values sit in small grey text underneath: 14.8%, 21.3%, 2.4% and 6.7%.
- Label: "A + B as % of the relevant baseline Gini".
- Footer: resources, needs and composition held fixed; A is the currently estimated local-access channel.
- The ruling's eight-word question is shortened to a six-word title so the style check (titles of six words or fewer) still holds.

**2. Which opportunity channel matters?** (slide 15)
- Large numbers, no table. Ex-ante, equivalised, % of baseline Gini.
- Single adults: access 15.5%, earnings 4.8%, A + B = 20.3%.
- Couples: access 3.7%, earnings 4.2%, A + B = 7.9%.
- Message: single adults, access > earnings; couples, earnings > access but close; attained bundle, earnings > access for both.

**3. Where does baseline inequality go?** (slide 16, the 100% display) — a table for both populations.

| Row | Formula | Single adults | Couples |
|---|---|---:|---:|
| Preferences | φ_P / I_0 | 0.1% | −1.8% |
| Local access | φ_A / I_0 | 15.5% | 3.7% |
| Earning opportunities | φ_B / I_0 | 4.8% | 4.2% |
| **Not allocated by this exercise** | 1 − (φ_P + φ_A + φ_B) / I_0 | 79.6% | 93.9% |
| Total | | 100.0% | 100.0% |

- **Rounding.** Each channel row is rounded to one decimal. The not-allocated row is 100 minus those rounded rows, so every column closes to exactly 100.0% and the A + B rows equal the slide 14 headline. The unrounded remainders are 79.55% and 93.82%.
- **X1 (couples reconciliation), on the slide.** The preference row is shown and negative. One line reads: "Couples: A + B alone = 7.9%; P + A + B = 6.1% because the preference contribution is negative (−1.8%)."
- **X2 (the remainder is not a channel), on the slide.** One line reads: "Not allocated is not a channel: it holds household resources, needs and composition fixed, retains sex-specific preference and opportunity blocks, and excludes wage-draw luck and the common offer spread, which exceed the location differences equalised."
- **Couples display.** Couples are shown in a table, never a stacked bar.

## C. Selected estimates (slide 9, after Estimation)

All four estimates are shown, from the V15 gallery, with cluster-robust standard errors:

| Estimate | Single adults | Couples |
|---|---|---|
| β_c, consumption weight | 2.0387 (0.2917) | 2.1017 (0.2939) |
| β_E,s, local unemployment exposure in employment access | −1.4422 (0.2356) | −1.1924 (0.1557) |
| β_wH, high-education shift in wage-offer location | 0.1491 (0.0308) | 0.1817 (0.0197) |
| σ, log-wage dispersion | 0.3815 (0.0133) | 0.3631 (0.0072) |

The interpretation is in the notes only, and it calls these structural associations, not causal estimates.

## D. Backup appendix and navigation

- **Appendix.** 32 backup slides: the appendix map plus 31 content slides.
- **Main-slide buttons.** 14 main slides carry discreet bottom-left buttons.
- **Backup navigation.** Every backup slide has [Back] to its main slide and [Appendix map].
- **Beamer symbols.** No default Beamer navigation symbols are shown.
- **PDF links.** The compiled PDF has 129 internal links, all resolving.

**Backup slides built**

| Group | Slides |
|---|---|
| Model | utility specification · opportunity density · sampled-alternative likelihood · identification |
| Estimation | preference parameters · employment-access parameters · hours and occupation opportunities · wage-offer equation · common versus household-specific opportunities · curvature and inference |
| Fit | extensive-margin fit · fit by margin (figure) · the thirty-seven-hour point · matched households · marginal rate of substitution (figure) |
| Welfare | attained-bundle derivation (includes why ATT is the staying-home equivalent) · ex-ante derivation · ex-ante numerical validation · equivalisation |
| Decomposition | central figure · ex-ante decomposition in Gini points · attained-bundle decomposition in Gini points · ex-ante channels as % of baseline · attained-bundle channels as % of baseline · composition of the explained component · Shapley versus one-factor equalisation · what is not allocated / future D channel · robustness of the attained-bundle decomposition |
| Data | sample selection · EUROMOD pricing · numerical design |

**Menu items not built, and why**

| Ruling item | Why not built |
|---|---|
| B26–B29, eight coalition Ginis (EA and ATT) | V15 reports no ex-ante coalition Ginis. The attained-bundle coalition Ginis appear only in V15's report text, not in the number registry. |
| B30 as a numeric table (one-factor vs Shapley) | Same source constraint. It is built as a conceptual slide with formulas, no numbers. |
| B13 as a table (hours distribution) | The registry's hours moments are the older band lineage. V15's corrected fit figure is used instead. |
| B16 indifference-curve figure | Omitted to keep the appendix focused. The marginal-rate-of-substitution figure is included. |
| B21 sensitivity numbers (equivalisation) | The alternative-domain shares exist only in V15's appendix text under internal labels, not in the registry. The equivalisation convention and the couples shift are shown. |
| B34 Monte Carlo replication counts and ex-ante draw counts | Not in the registry. The numerical design shows registry values only. |
| Hours and occupation standard errors | Omitted for space. They are in the gallery and in the paper. |

## E. Explained-component backup (Display 2)

- **Formula.** s_k = φ_k / (φ_P + φ_A + φ_B), ex-ante, equivalised.

  | Share | Single adults | Couples |
  |---|---:|---:|
  | Preferences | 0.7% | −28.5% |
  | Local access | 75.9% | 60.6% |
  | Earning opportunities | 23.4% | 67.9% |
  | Total | 100.0% | 100.0% |

- **Note, on the slide and in the notes.** "These are shares of the currently explained P/A/B change, not shares of total inequality. Negative components are possible under Shapley attribution."
- **Raw scale.** Omitted: at one decimal the raw couples shares sum to 100.1.
- **Denominators.** The two denominators never appear on the same slide or in the same sentence.

## F. Elasticities

None added. V15 states "Wage elasticities are not reported." No old value is imported.

## Checks

`verify_deck_r6.py --deck v18` passes 32 of 32.

**Repointed from V17:**
- **Numbers:** retired tokens, out-of-scope ban, typed numerals, registry.
- **Content:** assets, lineage, confusion-matrix wording, no pooled figure, no side-by-side comparison, structure, research question, equations, central slide, required statements, no-primacy wording, caption, labels, no 80–90% claims.
- **Style and layout:** style, caveats, backup, conflict, theory figure.

**New:**
- **G-V18-DENOMINATORS:** no slide or sentence mixes the two denominators.
- **G-V18-LINKS:** every source target exists and every PDF link resolves.
- **G-V18-HUNDRED:** the 100% display closes, shows the negative couples row, and carries the X1 and X2 text.
- **G-V18-GOAL1:** agrees with the manager's verification to rounding of its inputs.
- **G-V18-TITLE**, **G-V18-ESTIMATES**, **G-V18-NOCAUSAL**, **G-V18-ELASTICITY**, **G-V18-APPENDIX.**

**Negative controls:** all seven fire. Four are carried over (label, number, style title, style paragraph); three are new:
- a "share of explained change" phrase injected onto the 100% slide;
- a button pointed at a missing target;
- an 85% opportunity claim.

**Regression:** r6 19/19, V16 18/18, V17 23/23.

**Rehearsal script:** `reports/rehearsal_pack_v1.md` is regenerated to V18 numbering and is identical to `reports/rehearsal_pack_v18.md`.
