"""Resolve v6 prose against frozen v5 rendered tables/figures and scalar registry.

Recover each asset by matching the original template to its generated Markdown.
Literal prose must match exactly; no fallback, estimate or diagnostic is run.
"""
from pathlib import Path
import hashlib
import json
import re
import v5_sections

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAPER = ROOT / 'manuscript'
FIG = PAPER / 'figures/v5'
REG = json.loads((ROOT / 'reports/numbers_of_record_v5.json').read_text('utf-8'))['entries']
USED = set()
TABLES, CAPTIONS = {}, {}

def strip_modes(text, target):
    for tag in ('report-only', 'paper-only'):
        if tag == target + '-only':
            text = text.replace('{{' + tag + '}}', '').replace('{{/' + tag + '}}', '')
        else:
            text = re.sub(r'\{\{' + tag + r'\}\}.*?\{\{/' + tag + r'\}\}', '', text, flags=re.S)
    return text

generated = (HERE / 'story_v5.generated.md').read_text('utf-8')
templates = [v5_sections.ABSTRACT] + [s['body'] for s in v5_sections.SECTIONS] + [a for q, a in v5_sections.QA]
for template in templates:
    raw = strip_modes(template, 'report')
    tokens = list(re.finditer(r'\{\{(.*?)\}\}', raw))
    parts, at = [], 0
    for token in tokens:
        # Table/figure boundaries are structural. A generic lazy capture can
        # split adjacent tables at their internal blank lines or truncate the
        # final table of a section before its parameter rows.
        if token[1].startswith('table:'):
            capture = r'(\nTable: [^\n]+\n\n(?:\|[^\n]*\n)+\n?)'
        elif token[1].startswith('figure:'):
            capture = r'(\n!\[[^\n]+\]\([^\n]+\)\{width=95%\}\n)'
        else:
            capture = '(.*?)'
        parts.extend([re.escape(raw[at:token.start()]), capture])
        at = token.end()
    parts.append(re.escape(raw[at:]))
    match = re.search(''.join(parts), generated, flags=re.S)
    if not match:
        raise SystemExit('Frozen v5 template/generated Markdown mismatch: ' + raw[:90])
    for token, value in zip(tokens, match.groups()):
        kind, key = token[1].split(':', 1)
        if kind == 'table':
            if key in TABLES:
                assert TABLES[key] == value
            TABLES[key] = value
        elif kind == 'figure':
            CAPTIONS[key] = value

diag_path = ROOT / 'docs/Decomposition_diag_1.txt'
diag = diag_path.read_text('utf-8')
for key, pattern, unit in (
    ('diag1_location_log', r'at most about (0\.10) log points', 'log points'),
    ('diag1_sigma', r'sigma ≈ (0\.37)', 'log points'),
):
    match = re.search(pattern, diag)
    if not match:
        raise SystemExit('Diagnostic source missing: ' + key)
    REG[key] = {'value': float(match[1]), 'source': 'docs/Decomposition_diag_1.txt::5. Verdict',
                'status': 'diagnostic', 'units': unit}
DIAG_SHA256 = hashlib.sha256(diag_path.read_bytes()).hexdigest().upper()

def val(key, fmt=None):
    USED.add(key)
    value = REG[key]['value']
    if key.endswith('_year'):
        return str(value)
    if fmt:
        return format(float(value), fmt)
    if isinstance(value, float):
        return format(value, '.6g')
    if isinstance(value, int):
        return format(value, ',d')
    return str(value)

def resolve(text, target):
    text = strip_modes(text, target)
    text = re.sub(r'\{\{table:(.*?)\}\}', lambda m: TABLES[m[1]], text)
    def figure(match):
        value = CAPTIONS[match[1]]
        if target == 'paper':
            value = value.replace(str(FIG).replace('\\', '/') + '/', 'figures/v5/')
        return value
    text = re.sub(r'\{\{figure:(.*?)\}\}', figure, text)
    text = re.sub(r'\{\{n:([^|}]+?)(?:\|([^}]+))?\}\}', lambda m: val(m[1], m[2]), text)
    if '{{' in text:
        raise SystemExit('Unresolved v6 token')
    return text
