"""Render report/paper v6 from v6_sections.py and frozen v5 evidence.

No estimator, diagnostic, pricing or ex-ante numerical routine is called.
Run with MNL/.venv/Scripts/python.exe from any working directory.
"""
from pathlib import Path
import base64
import datetime as dt
import html
import json
import re
import urllib.request
import pypandoc
from v6_sections import TITLE, ABSTRACT, PRELIM_NOTE, SECTIONS, QA
from v6_render_inputs import HERE, ROOT, PAPER, FIG, REG, USED, DIAG_SHA256, resolve

today = dt.datetime.now().strftime('%d %B %Y')
bib = (PAPER / 'JMP_working_paper_for_seminar_v5.bib').read_text('utf-8')
BIB = PAPER / 'JMP_working_paper_for_seminar_v6.bib'
BIB.write_text(bib, encoding='utf-8')

# READER-VOICE-1: keep machine provenance in each generated surface without
# exposing internal workflow vocabulary to readers.  The paper receives TeX
# comments and the story report receives an HTML comment; both copies are
# deliberately identical so citation gates can inspect either block.
READER_VOICE_PROVENANCE = [
    'BEGIN READER-VOICE PROVENANCE',
    'Source-only provenance; excluded from rendered reader text.',
    ('Specifications: S11; artifact '
     's11_welfare_specs_of_record_v1.json; SHA-256 '
     '5FDC88502493CE540B088880EECF049BC268392FF3E8790FFE78A16AA6DDC884.'),
    ('Welfare definition: Mapping F; artifact JMP_W1_fork_ruling_v1.md; '
     'SHA-256 7F5D26857D8A96174A9924848F65A02611944273D7775FDC52DC82364A818C05.'),
    ('Welfare authorization: BASELINE-F-1 and E1; artifact '
     'JMP_W1_BASELINE_F1_authorization_and_Cobs_ruling_v1.md; SHA-256 '
     '54DFD886E41D0A89C1056CBEA5FA51E0A1294D3CA0813F938802BDC3DBD9EE0E.'),
    ('Welfare aggregates: artifact baseline_f1_verification_v1.md; MNL commit '
     '6048c9f7; independent verification b5550af5; SHA-256 '
     'DA7BADF639F3D502D47B301558453D76501C9C44033ECE3F17BDE350BFD5E55F.'),
    ('Equivalised reporting: E3-EQ; artifact '
     'JMP_BASELINE_F1_equivalised_reporting_v1.md; commit 4c4e07e; SHA-256 '
     'DACD34B593D0E676AC802779960DBB4F4BDC32A462C26F8852D56C9D4C95A669.'),
    ('Predictive diagnostics: POSFIT v3; repository MNL_posfit; branch '
     'diagnostics/posfit-v3; commit 96693269; artifact run_provenance.json; '
     'SHA-256 BDC3722C325FF8A27BE719AA52A741DF7BEEF9515B4A63554C65E8769EB7F40B.'),
    ('Bounded decomposition: DECOMP-2; repository MNL_decomp; branch '
     'welfare/preseminar-pab; commit b52761b4; artifact '
     'preseminar_pab_record_v1.json; SHA-256 '
     'BCBE4B6FC742DAA39535D5C3EB03BDA0641055A9F5E851B4F53F62FA3E612011.'),
    ('Leisure scaling: WS4; commit 5a8e6bba; artifacts '
     'ws4_sectionC_lambda_v1.png and ws4_sectionC_T_v1.png.'),
    'Diagnostic boundary: DECOMP-DIAG-1; artifact docs/Decomposition_diag_1.txt; SHA-256 ' + DIAG_SHA256 + '.',
    'REPORT-V6: presentation-only successor; frozen v5 tables, figures and scalar values.',
    'END READER-VOICE PROVENANCE',
]

# =========================================================================== #
# 8.  ASSEMBLY
# =========================================================================== #
report = ('# ' + TITLE + '\n\nHisham Haydar \u00b7 University of Luxembourg '
          'and LISER\n\nBuild date: ' + today + '.\n\n## Abstract\n\n'
          + resolve(ABSTRACT, 'report') + '\n\n*' + PRELIM_NOTE + '*\n')
paper = ('\\begin{abstract}\n' + resolve(ABSTRACT, 'paper')
         + '\n\\end{abstract}\n\n*' + PRELIM_NOTE + '*\n\n')

_n = 0
for sec in SECTIONS:
    if sec.get('report', True):
        _n += 1
        report += '\n\n# %d. %s\n\n' % (_n, sec['title'])
        report += resolve(sec['body'], 'report')

_started_appendix = False
for sec in SECTIONS:
    if not sec.get('paper', True):
        continue
    if sec.get('appendix') and not _started_appendix:
        paper += '\n\\appendix\n'
        _started_appendix = True
    paper += '\n\n# %s\n\n' % sec['title']
    paper += resolve(sec['body'], 'paper')

report += '\n# Questions for presentation preparation\n'
for i, (q, a) in enumerate(QA, 1):
    report += '\n## %d. %s\n\n%s\n' % (i, q, resolve(a, 'report'))
report += '\n# Bibliography\n\n::: {#refs}\n:::\n'
(HERE / 'story_v6.generated.md').write_text(report, encoding='utf-8')

header = (r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,booktabs,longtable,array,graphicx,calc}
\usepackage{ragged2e}
\usepackage{needspace}
\usepackage{float}
\raggedbottom
% Float discipline. The panel figures are about 0.43\textheight each, so the
% default allowance of several top floats lets two of them plus a long-captioned
% table exceed the page and produce an overfull vbox in the output routine.
\setcounter{topnumber}{1}
\setcounter{bottomnumber}{1}
\setcounter{totalnumber}{2}
\renewcommand{\topfraction}{0.6}
\renewcommand{\bottomfraction}{0.4}
\renewcommand{\textfraction}{0.12}
\renewcommand{\floatpagefraction}{0.7}
\usepackage{xurl}
\usepackage[round]{natbib}
\usepackage[colorlinks=true,allcolors=blue]{hyperref}
\usepackage{bookmark}
\usepackage{caption}
\captionsetup{font=small,labelfont=bf}
\setlength{\emergencystretch}{3em}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\title{''' + TITLE + r'''}
\author{Hisham Haydar\\University of Luxembourg and LISER}
\date{Build: ''' + today + r'''\\Discussion draft}
\begin{document}
\maketitle
''')
body = pypandoc.convert_text(
    paper, 'latex', format='markdown+raw_tex+tex_math_dollars',
    extra_args=['--natbib', '--wrap=none']).replace('\r\n', '\n')
body = body.replace(r'\def\LTcaptype{none}', '')
# Figures are pinned where they are written rather than floated. longtable
# mis-accounts the remaining page height when a float shares the page, which
# clipped the last rows of a table and, on one page, a whole paragraph. With
# every figure placed in sequence the page breaking is correct, and \raggedbottom
# absorbs the slack.
body = body.replace(r'\begin{figure}', r'\begin{figure}[H]')


def wrap_table(m):
    n = len(m[1])
    first = .155 if n == 7 else (.25 if n >= 4 else .42)
    # Leave room for 2*tabcolsep per column. A residual 0.12154pt overfull
    # survives on wide tables regardless of these widths: it is pandoc's
    # longtable rule geometry, is 0.04 mm, and check_v5_pdf_layout.py
    # confirms no ink crosses the margin.
    total = .98 - .014 * n
    widths = [first] + [(total - first) / (n - 1)] * (n - 1)
    return (r'\begin{longtable}[]{@{}'
            # \RaggedRight, not \raggedright: the latter carries infinite
            # glue shrinkage, and longtable splitting a page inside such a cell
            # produces an overfull vbox that runs past the bottom margin.
            + ''.join(r'>{\RaggedRight\arraybackslash}p{' + f'{w:.4f}'
                      + r'\linewidth}' for w in widths) + r'@{}}')


body = re.sub(r'\\begin\{longtable\}\[\]\{@\{\}([lrc]+)@\{\}\}', wrap_table, body)
# \Needspace forces the page to break BEFORE a table when too little room is
# left: pandoc's longtable keeps its caption and header together in one
# unbreakable chunk, and starting that chunk near the foot of a page is what
# produced the overfull vbox that ran past the bottom margin.
body = body.replace(
    r'\begin{longtable}',
    r'\Needspace*{12\baselineskip}\small\setlength{\tabcolsep}{3pt}'
    r'\begin{longtable}')
_tex_provenance = '\n'.join('% ' + line for line in READER_VOICE_PROVENANCE)
tex = (header + body + '\n\\bibliographystyle{plainnat}\n'
       '\\bibliography{JMP_working_paper_for_seminar_v6}\n'
       + _tex_provenance + '\n\\end{document}\n')
(PAPER / 'JMP_working_paper_for_seminar_v6.tex').write_text(tex, encoding='utf-8')

# ---- the HTML report ------------------------------------------------------ #
rendered = pypandoc.convert_text(
    report, 'html5', format='markdown+tex_math_dollars',
    extra_args=['--mathjax', '--citeproc', '--bibliography=' + str(BIB),
                '--wrap=none']).replace('\r\n', '\n')


def embed(m):
    p = Path(html.unescape(m[1]))
    return ('src="data:image/png;base64,'
            + base64.b64encode(p.read_bytes()).decode()
            + '" data-fig="' + p.stem + '"')


rendered = re.sub(r'src="([^"]+\.png)"', embed, rendered)
# tables scroll inside their own container rather than overflowing the viewport
rendered = re.sub(r'<table', '<div class="tw"><table', rendered)
rendered = re.sub(r'</table>', '</table></div>', rendered)
# Scientific history and the notebook description stay available but outside the
# main reading flow. The heading is KEPT so the section still has an anchor and
# a table-of-contents entry; only its body collapses.
for _h in [s['title'] for s in SECTIONS if s.get('collapse')]:
    _pat = (r'(<h1[^>]*>[\d.\s]*' + re.escape(_h) + r'</h1>)(.*?)(?=<h1|\Z)')
    rendered = re.sub(
        _pat, lambda m: (m[1] + '<details><summary>Show this section</summary>'
                         + m[2] + '</details>'), rendered, flags=re.S)

vendor = HERE / 'vendor/tex-svg.js'
vendor.parent.mkdir(exist_ok=True)
if not vendor.exists():
    urllib.request.urlretrieve(
        'https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js', vendor)
mathjax = vendor.read_text('utf-8')

css = (":root{--ink:#1a1a1a;--mut:#5a5f66;--line:#dcdfe4;--bg:#fff;"
       "--soft:#f6f7f9;--accent:#1f4e79;--accent2:#7a3b12}"
       "*{box-sizing:border-box}"
       "body{margin:0;background:var(--bg);color:var(--ink);"
       "font:17px/1.62 Georgia,'Iowan Old Style','Times New Roman',serif}"
       "#wrap{display:flex;align-items:flex-start;max-width:1500px;margin:0 auto}"
       "#toc{position:sticky;top:0;flex:0 0 306px;height:100vh;overflow-y:auto;"
       "padding:22px 16px 60px 20px;border-right:1px solid var(--line);"
       "background:var(--soft);font-family:-apple-system,BlinkMacSystemFont,"
       "'Segoe UI',Roboto,sans-serif;font-size:13px;line-height:1.45}"
       "#toc h2{font-size:11px;letter-spacing:.14em;text-transform:uppercase;"
       "color:var(--mut);margin:0 0 12px;font-weight:700;border:0;padding:0}"
       "#toc a{display:block;padding:4px 8px;color:var(--ink);"
       "text-decoration:none;border-radius:4px;border-left:2px solid transparent}"
       "#toc a:hover{background:#e9ecf1}"
       "#toc a.sub{padding-left:20px;color:var(--mut);font-size:12px}"
       "#toc a.on{background:#e3eaf3;border-left-color:var(--accent);"
       "font-weight:600}"
       "#doc{flex:1 1 auto;min-width:0;padding:34px 52px 140px;max-width:1020px}"
       "h1{font-size:27px;line-height:1.24;margin:2.2em 0 .35em;padding-top:.4em;"
       "border-top:2px solid var(--ink);letter-spacing:-.01em}"
       "h1:first-of-type{margin-top:.2em;border-top:0}"
       "h2{font-size:20px;margin:1.7em 0 .4em;color:var(--accent);line-height:1.3}"
       "h3{font-size:16.5px;margin:1.4em 0 .3em;font-family:-apple-system,"
       "BlinkMacSystemFont,'Segoe UI',sans-serif}"
       "p{margin:.62em 0}ul,ol{margin:.55em 0 .55em 0;padding-left:1.35em}"
       "li{margin:.28em 0}"
       "figure{margin:2em 0}img{max-width:100%;height:auto}"
       "figcaption{font:14px/1.55 -apple-system,BlinkMacSystemFont,'Segoe UI',"
       "sans-serif;color:var(--mut);margin-top:.5em}"
       ".tw{overflow-x:auto;margin:1.5em 0;-webkit-overflow-scrolling:touch}"
       "table{border-collapse:collapse;width:100%;min-width:520px;"
       "font:13.5px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}"
       "td,th{padding:8px 9px;border-bottom:1px solid var(--line);"
       "text-align:left;vertical-align:top}th{background:#eef3f5}"
       ".math.display{display:block;overflow-x:auto;margin:1.6em 0}"
       "code{overflow-wrap:anywhere;font-size:.85em;background:var(--soft);"
       "padding:1px 4px;border-radius:3px}"
       "blockquote{margin:1.1em 0;padding:13px 17px;border:1px solid #c9d8e8;"
       "border-left:3px solid var(--accent);border-radius:6px;background:#eef3f8}"
       "blockquote p{margin:.3em 0}"
       "details{margin:2em 0;padding:16px 18px;background:var(--soft);"
       "border:1px solid var(--line);border-radius:6px}"
       "summary{font-weight:700;cursor:pointer;font-family:-apple-system,"
       "BlinkMacSystemFont,'Segoe UI',sans-serif}"
       "#refs div{margin:.7em 0;padding-left:1.6em;text-indent:-1.6em}"
       "a{color:var(--accent)}"
       "@media(max-width:1100px){#wrap{display:block}#toc{position:static;"
       "height:auto;width:auto;flex:none;border-right:0;"
       "border-bottom:1px solid var(--line)}#doc{padding:24px 20px 80px}}"
       "@media print{#toc{display:none}#doc{max-width:none;padding:0}"
       "body{font-size:11pt}details{display:block}}")

_nav = []
_seen: dict = {}


def _slug(t):
    b = re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', t).lower()).strip('-')[:60] or 'sec'
    _seen[b] = _seen.get(b, 0) + 1
    return b if _seen[b] == 1 else '%s-%d' % (b, _seen[b])


def _anchor(m):
    lvl, inner = m[1], m[2]
    sid = _slug(inner)
    _nav.append((lvl, sid, re.sub(r'<[^>]+>', '', inner)))
    return '<h%s id="%s">%s</h%s>' % (lvl, sid, inner, lvl)


rendered = re.sub(r'<h([12])[^>]*>(.*?)</h\1>', _anchor, rendered, flags=re.S)
toc_html = '<h2>Contents</h2>' + ''.join(
    '<a class="%s" href="#%s">%s</a>' % ('' if l == '1' else 'sub', sid, txt)
    for l, sid, txt in _nav)

_html_provenance = ('<!--\n' + '\n'.join(READER_VOICE_PROVENANCE)
                    + '\n-->')
htmlout = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1">'
           '<title>' + TITLE + '</title><style>' + css + '</style>'
           '<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]],'
           'displayMath:[["\\\\[","\\\\]"]]},svg:{fontCache:"local"},'
           'options:{enableMenu:false}};</script><script>' + mathjax
           + '</script></head><body><div id="wrap"><nav id="toc">' + toc_html
           + '</nav><main id="doc">' + rendered + '</main></div>'
           '<script>(function(){var ls=[].slice.call('
           'document.querySelectorAll("#toc a")),'
           'hs=ls.map(function(a){return document.getElementById('
           'a.getAttribute("href").slice(1));});'
           'function on(){var y=scrollY+120,k=0;hs.forEach(function(h,i){'
           'if(h&&h.offsetTop<=y)k=i;});ls.forEach(function(a,i){'
           'a.className=a.className.replace(/ ?on/,"")+(i===k?" on":"");});}'
           'addEventListener("scroll",on,{passive:true});on();})();</script>'
           + _html_provenance +
           '</body></html>')
(ROOT / 'reports/JMP_research_story_report_v6.html').write_text(
    htmlout, encoding='utf-8')


registry = json.loads((ROOT / 'reports/numbers_of_record_v5.json').read_text('utf-8'))
registry.update(build_date=today, entries=REG, used_keys=sorted(USED),
                unused_keys=sorted(set(REG) - USED))
registry['presentation_version'] = 'v6; numerical evidence preserved from v5; diagnostic boundary added'
(ROOT / 'reports/numbers_of_record_v6.json').write_text(
    json.dumps(registry, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('v6 report, editable Markdown, paper TeX and numerical registry written.')
