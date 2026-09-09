"""Offline browser and PDF checks; no network allowed during HTML test."""
import json
from pathlib import Path
import re
import pymupdf
from playwright.sync_api import sync_playwright

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
OUT=HERE/'render_checks_v3'
OUT.mkdir(exist_ok=True)
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',headless=True)
    context=browser.new_context(viewport={'width':1400,'height':1100},offline=True)
    page=context.new_page()
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto((ROOT/'reports/JMP_research_story_report_v3.html').as_uri())
    page.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise')
    page.evaluate('MathJax.startup.promise')
    info=page.evaluate('''() => ({math:document.querySelectorAll('.math').length,
       rendered:document.querySelectorAll('mjx-container').length,
       errors:Array.from(document.querySelectorAll('[data-mjx-error],mjx-merror')).map(x=>x.textContent),
       images:Array.from(document.images).every(x=>x.complete&&x.naturalWidth>0),
       text:document.body.innerText, details:document.querySelectorAll('details').length})''')
    info['javascript_errors']=errors
    page.screenshot(path=str(OUT/'html_opening.png'))
    heading=page.get_by_role('heading',name='13. Welfare: the verified identity and its numerical implementation',exact=True)
    heading.scroll_into_view_if_needed()
    page.screenshot(path=str(OUT/'html_welfare.png'))
    (OUT/'html_text.txt').write_text(info.pop('text'),encoding='utf-8')
    browser.close()
doc=pymupdf.open(ROOT/'manuscript/JMP_working_paper_for_seminar_v3.pdf')
text='\n'.join(page.get_text() for page in doc)
info['pdf_pages']=len(doc)
info['pdf_unresolved_citations']='[?]' in text or '(?)' in text
for n,page in enumerate(doc):
    page.get_pixmap(matrix=pymupdf.Matrix(.65,.65)).save(OUT/f'pdf_{n+1:02d}.png')
(OUT/'pdf_text.txt').write_text(text,encoding='utf-8')
(OUT/'checks.json').write_text(json.dumps(info,indent=2),encoding='utf-8')
print(json.dumps(info,indent=2))
assert info['rendered']==info['math'] and info['math']>0, 'Offline math did not render completely'
assert not info['errors'] and not errors and info['images']
assert not info['pdf_unresolved_citations']
