"""Offline HTML math/image rendering and visual review captures for v6."""
import json
from pathlib import Path
import pymupdf
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports/research_story_build/render_checks_v6'
OUT.mkdir(exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        headless=True)
    context = browser.new_context(viewport={'width': 1400, 'height': 1100}, offline=True)
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto((ROOT / 'reports/JMP_research_story_report_v6.html').as_uri())
    page.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise')
    page.evaluate('MathJax.startup.promise')
    info = page.evaluate('''() => ({math:document.querySelectorAll('.math').length,
        rendered:document.querySelectorAll('#doc mjx-container').length,
        navigation_math:document.querySelectorAll('#toc mjx-container').length,
        unrendered_math:Array.from(document.querySelectorAll('.math')).filter(x=>!x.querySelector('mjx-container')).length,
        errors:Array.from(document.querySelectorAll('[data-mjx-error],mjx-merror')).map(x=>x.textContent),
        images:Array.from(document.images).every(x=>x.complete&&x.naturalWidth>0),
        details:document.querySelectorAll('details').length})''')
    page.screenshot(path=str(OUT / 'html_opening.png'))
    page.get_by_role('heading', name='11. Appendix D. Preliminary restricted-operator decomposition', exact=True).scroll_into_view_if_needed()
    page.screenshot(path=str(OUT / 'html_appendix.png'))
    info['javascript_errors'] = errors
    browser.close()
for kind, rel, needle in (
    ('paper', 'manuscript/JMP_working_paper_for_seminar_v6.pdf', 'Preliminary restricted-operator'),
    ('deck', 'beamer/build/JMP_seminar_deck_r6.pdf', 'The earnings operator equalises'),
):
    doc = pymupdf.open(ROOT / rel)
    for i, page in enumerate(doc):
        if needle in page.get_text():
            page.get_pixmap(matrix=pymupdf.Matrix(1.1, 1.1)).save(OUT / (kind + '_appendix.png'))
            info[kind + '_appendix_page'] = i + 1
            break
    info[kind + '_pages'] = len(doc)
    info[kind + '_unresolved_citations'] = any('[?]' in p.get_text() or '(?)' in p.get_text() for p in doc)
info['status'] = 'PASS' if (info['math'] == info['rendered'] and info['math'] > 0 and
    not info['errors'] and not errors and not info['unrendered_math'] and info['images'] and info['details'] == 2 and
    not info['paper_unresolved_citations'] and not info['deck_unresolved_citations']) else 'FAIL'
(ROOT / 'reports/report_v6_render_gate.json').write_text(json.dumps(info, indent=2) + '\n', encoding='utf-8')
print(json.dumps(info, indent=2))
raise SystemExit(0 if info['status'] == 'PASS' else 1)
