# Manual Finishing Touches

## Visual polish

- [ ] **Slide 1 (title):** Consider adding an institutional affiliation or date if needed for the specific talk.
- [ ] **Slide 4 (literature):** The four-box TikZ diagram may need minor spacing adjustments depending on the final Overleaf compile. Check that all author names render correctly (accented characters: Strøm, Capéau, Karlström).
- [ ] **Slide 6 (Belgium):** If a Belgium map graphic is available, consider adding it to the left column. Currently text-only.
- [ ] **Slide 8 (raw data):** The figure_fit.png shows labor-supply state distribution (observed vs predicted), not a pure "raw data" heatmap. Consider generating a dedicated observed-only figure if desired, or leave the current combined figure as a preview of model fit.
- [ ] **Slide 15 (welfare vs income Gini):** The bar chart is drawn with TikZ. Verify the bar heights render at the right proportional scale on your screen.

## Content checks

- [ ] **Appendix 3 (sample construction):** The filtering funnel uses generic step labels. Replace the "---" entries with actual counts if available from the data pipeline.
- [ ] **Slides 11-12 (estimates):** The main-deck tables omit the two statistically insignificant interaction terms (Wallonia x High, Brussels x High) for compactness. Full tables are in Appendix 4.

## Before presenting

- [ ] Rehearse slides 1-7 to confirm they work as a standalone 15-minute talk.
- [ ] Decide whether slide 14 (elasticities) stays in the main deck or moves to appendix depending on talk length.
- [ ] Check that all four PNGs in `figures/` are up to date with the latest `03_assets/` versions.
