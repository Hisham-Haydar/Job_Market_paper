# JMP — V14 to V15 theory figure restore, v1

One figure and its caption restored; no other change, no recomputation. V14 is
untouched.

## 1. What was wrong with V14

V14 replaced the original own-set equal-consumption figure with a two-panel
regeneration on the premise that the construction requires identical
preferences for the two individuals. That premise was wrong, and the redraw
lost the construction's actual point:

- the original puts **both individuals on one pair of axes**, with both money
  metrics marked on the same consumption axis, so the two levels are visibly
  comparable at a glance;
- the two-panel version put each individual on separate axes, so that
  comparison — the reason the figure exists — disappeared;
- the original also draws equal-pay profiles across jobs and marks the
  indifference points geometrically; the redraw simplified these away.

## 2. Restored, not regenerated

`manuscript/figures/v5/theory_w1.png` is restored as the Section 3 figure.
Verified:

- `manuscript/figures/v3/theory_w1.png` and `manuscript/figures/v5/theory_w1.png`
  are byte-identical: SHA-256
  `976fe2787bf9bb269acfec07e4cf782f69486e665059ad7e3092afead1064f02`.
- That hash matches the image embedded (`data-fig="theory_w1"`) in
  `JMP_research_story_report_v4.html` through `JMP_research_story_report_v11.html`,
  checked directly against the decoded base64 payload in V4 and V11.
- It is not the V14 regeneration (`manuscript/figures/v14/fig_v14_theory_own_set.png`,
  a different hash).

`reports/research_story_build/make_v14_theory_figure.py` (the V14 regenerator)
is left in place as a record of what was tried and why it was wrong; it is not
called by the V15 build.

## 3. Corrected caption

Report (Section 3, LaTeX as in the original pre-V12 caption):

> Own-set equal-consumption equivalents: the theoretical construction from the
> companion theory paper. Two individuals, with preferences $R_i$ and $R_h$ and
> ability sets $A=\{j,k\}$ and $A^{\prime}=\{k,\ell\}$, attain bundles $z_i$ and
> $z_h$. For each individual, a common consumption level is assigned to every
> job in their own set; the level at which the preferred reference job becomes
> indifferent to the attained bundle is that individual's money metric, $W^1_i$
> and $W^1_h$. The two metrics are then directly comparable. Adapted from
> Haydar and Maniquet (2026), work in progress. This is the deterministic
> construction; the estimated ex-ante measure is its extension, defined in
> Section 3.

Gallery (plain text; the gallery loads no MathJax, matching its existing
convention for `beta_c`, `lambda_c`, `W_EA`, `Delta I`):

> Own-set equal-consumption equivalents: the theoretical construction from the
> companion theory paper. Two individuals, with preferences R_i and R_h and
> ability sets A = {j,k} and A' = {k,l}, attain bundles z_i and z_h. For each
> individual, a common consumption level is assigned to every job in their own
> set; the level at which the preferred reference job becomes indifferent to
> the attained bundle is that individual's money metric, W1_i and W1_h. The two
> metrics are then directly comparable. Adapted from Haydar and Maniquet
> (2026), work in progress. This is the deterministic construction; the
> estimated ex-ante measure is its extension, defined in Section 3.

Only two departures from the PI's literal text, both mechanical:
- the report renders `R_i`/`R_h`/etc. as LaTeX inline math (`$...$`), matching how this exact caption was typeset before it was ever regenerated;
- the gallery renders the same content as plain text, because it has no math renderer, matching every other formula already in that surface.

## 4. Surrounding text corrected

The paragraph before the figure no longer says the two individuals "share the
same preferences over consumption and jobs." It now says each individual is
evaluated with their own preferences and their own ability set, and states the
construction's point directly: the two resulting money metrics are comparable
between them despite that difference. The theoretical-illustration sentence
("no estimated value, no household data and no result") and the following
paragraph on the empirical reference being non-employment are unchanged from
V14.

## 5. Known defect — disclosed, not fixed

The restored image has label overlaps carried over from its original
production (the companion theory project's own slides, adapted "with
permission" per the historical build caption):

- the label `y(k)` sits directly on its own marker in the left (red) panel;
- the `R_i`/`R_h` axis labels near the top collide with the `y(ℓ)`/`y'(ℓ)`
  labels on the right (blue) side of the figure.

These are not corrected here. Redrawing the figure is exactly what produced
the V14 regression, so no redraw is attempted in this release. If a clean
source file exists in the companion theory project's own slide deck, obtaining
it is a separate decision for the PI; this release does not pursue it.

## 6. Scope check

- Every other embedded image in both surfaces is confirmed byte-identical to
  V14 (the theory figure is the only one that changed).
- `numbers_of_record_v15.json` equals `numbers_of_record_v14.json` on every
  key; no key is added.
- `make_v14_theory_figure.py` is not invoked by the V15 build.

## 7. Gates

All V14 gates re-run against V15, including all four negative controls
(banned terms, Stage A status, section titles, figure captions — the last with
its own theory-caption sub-control). The reader gate's exemption for "Haydar
and Maniquet" and "own-set equal-consumption equivalents" is scoped to the
theory-figure caption in both surfaces via a stable anchor phrase common to the
LaTeX (report) and plain-text (gallery) renderings, rather than to either exact
string, since a raw `$R_i$` in the caption source is not literally present in
either rendered surface (pandoc's `tex_math_dollars` rewrites `$...$` to
`\(...\)` before MathJax ever runs client-side, and the gate reads the static
HTML).

## 8. Hashes

- `JMP_research_story_report_v15.html` — see `reports/v15_surface_manifest.json`
- `JMP_results_gallery_v15.html` — see `reports/v15_surface_manifest.json`
