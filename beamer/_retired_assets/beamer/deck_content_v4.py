"""Read the author's content; do not generate or paraphrase prose."""
from pathlib import Path
import re
import unicodedata

HERE = Path(__file__).resolve().parent
CONTENT = HERE.parent / 'manuscript/JMP_seminar_deck_content_v2.md'


def read_content():
    source = CONTENT.read_text(encoding='utf-8')
    chunks = re.split(r'(?m)^(\d+b?) — ', source)[1:]
    slides = []
    for number, chunk in zip(chunks[::2], chunks[1::2]):
        chunk = re.split(r'\n\n(?:Backups|25-minute running order:)',chunk,1)[0].strip()
        description, _, note = chunk.partition('\nSay: ')
        if number == '1':
            headline = description.split('Title. ', 1)[1].split(' · ', 1)[0]
        elif number == '22':
            headline = 'Conclusion'
        elif number.endswith('b'):
            headline = description.split('Headline: ',1)[1].split('\n',1)[0]
        else:
            headline = description.split('Headline: ', 1)[1].split('. ', 1)[0] + '.'
        slides.append(dict(number=number if number.endswith('b') else int(number), headline=headline,
                           description=description, note=note.strip()))
    short = re.search(r'25-minute running order: ([\d, ]+)', source).group(1)
    slides.sort(key=lambda s:(int(str(s['number']).rstrip('b')),str(s['number']).endswith('b')))
    return slides, [int(n) for n in short.split(',')]


def tex_escape(text):
    """Only encoding / mathematical typography substitutions, never wording."""
    text = unicodedata.normalize('NFC', text)
    translation = {'&': r'\&', '%': r'\%', '_': r'\_', '#': r'\#',
                   '−': r'\ensuremath{-}', '→': r'\ensuremath{\to}',
                   '±': r'\ensuremath{\pm}', '≈': r'\ensuremath{\approx}',
                   '×': r'\ensuremath{\times}', '¹': r'\textsuperscript{1}',
                   'ℓ': r'\ensuremath{\ell}', 'Ω': r'\ensuremath{\Omega}',
                   'β': r'\ensuremath{\beta}', 'θ': r'\ensuremath{\theta}',
                   '′': r'\ensuremath{\prime}', '½': r'\ensuremath{\frac{1}{2}}'}
    return ''.join(translation.get(c, c) for c in text)


def normalized(text):
    """Ignore PDF line breaks, ligatures and typographic spacing only."""
    text = unicodedata.normalize('NFKC', text).replace('\u00ad', '')
    text = text.translate(str.maketrans({'–':'-', '—':'-', '−':'-',
                                       '’':"'", '‘':"'", '“':'"', '”':'"'}))
    return re.sub(r'\s+', '', text)


def macro_values():
    source = (HERE / 'deck_numbers_v1.tex').read_text(encoding='utf-8')
    return dict(re.findall(r'\\newcommand\{\\([A-Za-z]+)\}\{(.*)\}', source))


def expanded(text):
    for name, value in sorted(macro_values().items(), key=lambda x: -len(x[0])):
        text = re.sub(r'\\' + name + r'\b(?:\{\})?', lambda m: value, text)
    return text
