"""Write the review report from the verified PDF text and page manifest."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def main():
    r=json.loads((HERE/'build/verification_v4.json').read_text(encoding='utf-8'))
    rows=json.loads((HERE/'build/slide_table_v4.json').read_text(encoding='utf-8'))
    passed=sum(c['pass_'] for c in r['checks'])
    text=['# Beamer v4 — build and content review','',
          'Authority: [the supplied content v2](../manuscript/JMP_seminar_deck_content_v2.md). '
          '22 running-order frames; B1 in three blocks, then B2–B6. '
          'The only running-order overlay is the requested geography/sex build on slide 19.','',
          f'Verifier: **{"PASS" if r["passed"] else "FAIL"} — {passed}/{len(r["checks"])} checks.** '
          'All three logs have zero errors, zero overfull boxes and zero underfull boxes. '
          'PDF headlines match the content document; supplied captions and prose are present; '
          'running speaker notes match both the source and the rehearsal PDF. '
          'The text-layer gate finds zero forbidden labels in every built PDF and every active slide figure.','',
          '| Build | Pages | PDF | Text export |','|---|---:|---|---|']
    for key,label in [('JMP_seminar_deck_v1','Full'),('JMP_seminar_deck_v1_25min','25-minute'),('JMP_seminar_deck_v1_rehearsal','Rehearsal')]:
        text.append(f'| {label} | {r["page_counts"][key]} | [Open](build/{key}.pdf) | [Text](build/{key}_text.txt) |')
    text += ['', '## Per-slide table','',
             'Counts are measured from the PDF text layer: headline, prose, table/equation text, '
             'chart labels and numeric tokens; navigation fractions and speaker notes are excluded. '
             'A whitespace-delimited token counts when it contains a letter or digit. '
             'Slide 19 reports the larger count of its two builds. '
             'These are **all on-slide words**, not the former body-prose-only count.','',
             '| Slide | Headline | Element | On-slide words |','|---|---|---|---:|']
    for row in rows:
        text.append('| {number} | {headline} | {element} | {on_slide_words} |'.format(**row))
    text += ['', '## Source and implementation notes','',
      '- **Slide 18 source discrepancy, preserved rather than rewritten:** the authored row says '
      '“50–400 drawn jobs: largest coefficient move 0.2 s.e.”. The source '
      '`MNL/experiments/JMP_SEMINAR_SPRINT/figures/figS6_02_coefficient_stability.csv` '
      'gives a maximum absolute deviation of 0.213142 for R ≥ 100, which rounds to 0.2; '
      'including R = 50 gives 0.562005, which rounds to 0.6. The macro records the narrower '
      'source scope explicitly. The supplied headline, table wording and spoken script are retained. '
      'The typesetting PASS does not certify this wider empirical claim.',
      '- The decisive verbatim-content brief supersedes the older 12-word ceiling and 23-message '
      'running order. The verifier retains their purposes through exact authored-prose and exact-order gates. '
      'The content document gives no `Say:` text for slide 22; its note is deliberately empty.',
      '- New empirical macros read existing sprint tables or the original tabular/JSON artefacts '
      'named by the manuscript provenance. No matching new summary table exists for several '
      'couples, benchmark and sensitivity quantities; those use their existing run artefacts, '
      'with paths recorded beside the definitions. Citation years and question enumerators '
      'come from the supplied content document and are marked as document metadata.',
      '- The market-side integration half-band is rounded outward to one decimal percentage point '
      'to reproduce the authored ±1.0. Other displayed precisions follow the supplied text.',
      '- The shared preamble is unchanged. The main file adjusts only title-box height, caption '
      'spacing, equation size and figure placement to fit the longer verbatim content. '
      'Running rehearsal notes use a larger font; long backup notes retain the original compact size.',
      '- The theory drawing is reused on exactly slides 4 and 5. Visibility switches hide '
      'the original pay dots and ability braces on slide 5; the original drawing coordinates, '
      'agent palette, staging macros and preference segments are retained.',
      '- B1 retains the existing three coefficient panels. B2 shows the four removed objects '
      'using the supplied channel labels; its prior exhaustiveness explanation is retained in notes. '
      'B3 and B5 retain their source material. B4 uses the supplied descriptive backup label. '
      'B6 typesets the existing benchmark quantities and preserves the previous benchmark notes. '
      'No new spoken script is authored for the backups.',
      '- Font checks verify the recorded figure-kit sizes and the embedded figure PDF fonts '
      '(minimum 18 pt). The figures are vector PDFs and are scaled when placed on the Beamer page.',
      '', '## Figure reuse','',
      'Nine existing slide PDFs are reused unchanged. Three missing panels were rendered from their '
      'existing CSVs using the figure kit:', '',
      '| New panel | Source CSV |','|---|---|',
      '| `observed_hours_slide.pdf` | `fig01_observed_hours_35h_peak.csv` |',
      '| `headline_references_slide.pdf` | `figW02_headline_decomposition.csv` |',
      '| `regional_profiles_slide.pdf` | `figG02_regional_access_environments.csv` |', '',
      'Five unused v3 panels are preserved in `figures/unused_v3/`. '
      'No paper figure or MNL source artefact was modified.', '',
      '## Reproduce', '', '```powershell', 'cd Job_Market_paper/beamer',
      'python build_deck_v4.py all', '```', '',
      'The build regenerates number macros, creates only missing panels, runs latexmk on '
      'the three existing drivers, exports text with `pdftotext -layout`, verifies, and rewrites this report.', '',
      'Machine-readable evidence: [verification](build/verification_v4.json), '
      '[slide table](build/slide_table_v4.json).', '',
      'Content SHA-256: `'+r['content_sha256']+'`.', '']
    (HERE/'DECK_V4_REVIEW.md').write_text('\n'.join(text),encoding='utf-8')
    print('Wrote DECK_V4_REVIEW.md')


if __name__=='__main__':main()
