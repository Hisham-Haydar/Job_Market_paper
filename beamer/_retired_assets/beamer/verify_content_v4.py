"""v4 implementation of the existing seven verification categories.

The decisive brief supersedes v3's 23-message / 12-word requirements with
25 exact authored slides (22 in v4 plus 5b, 9b, 13b). All other gates are retained; PDF headline,
caption, note, short-order and physical page checks are added.
"""
from __future__ import annotations
import collections
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

from deck_content_v4 import HERE, CONTENT, read_content, normalized, tex_escape, expanded

local_deps=HERE/'build/python_deps'
if local_deps.exists(): sys.path.insert(0,str(local_deps))
import pymupdf

FORBIDDEN=re.compile(r'S8|LOC4|C_P|C_E|C_A|C_B|C_D|R-2|PENDING|PROVISIONAL|EXPLORATORY|deputy|ruling')
JOBS=['JMP_seminar_deck_v1','JMP_seminar_deck_v1_25min','JMP_seminar_deck_v1_rehearsal']


def argument(text,command):
    m=re.search(re.escape('\\'+command)+r'\{',text)
    if not m:return ''
    depth=1;i=m.end()
    for j in range(i,len(text)):
        if j and text[j-1]=='\\':continue
        if text[j]=='{':depth+=1
        if text[j]=='}':depth-=1
        if depth==0:return text[i:j]
    raise ValueError('unbalanced '+command)


def source_frames():
    tex=(HERE/'JMP_seminar_deck_v1.tex').read_text(encoding='utf-8')
    run,backup=tex.split('\n\\appendix\n',1)
    frames=re.findall(r'\\begin\{frame\}.*?\\end\{frame\}',run,re.S)
    tags=re.findall(r'\\(shortdeck|longdeck|mergedaway)\{%',run)
    backups=re.findall(r'\\begin\{frame\}.*?\\end\{frame\}',backup,re.S)
    return tex,frames,tags,backups


def overlay_count(frame):
    specs=re.findall(r'\\(?:only|onslide)<([^>]+)>',frame)
    return max([1]+[int(x) for spec in specs for x in re.findall(r'\d+',spec)])


def prose(text):
    text=expanded(text).replace('{,}',',')
    for a,b in [(r'\%', '%'),(r'\&','&'),('---','—'),('--','–'),(r'\textperiodcentered','·')]:
        text=text.replace(a,b)
    return re.sub(r'[{}]','',text)


def nwords(text):
    return sum(any(c.isalnum() for c in token) for token in text.split())


def authored_phrases(slide):
    """Literal prose fragments, read from the author's document."""
    n=slide['number'];d=slide['description'];pieces=[]
    if n in [4,5,'5b',6,8,9,'9b',10,11,12,13,'13b',14,15,17,19,20]:
        key='Caption line: ' if 'Caption line: ' in d else 'Caption: '
        pieces.append(d.split(key,1)[1])
    if n==12:
        pieces.append(d.split('i.e. ',1)[1].split(' Caption: ',1)[0])
    if n==13:
        pieces.append(d.split(' On slide: ',1)[1].split(' Caption: ',1)[0])
    if n==2:
        p=d.split('On slide, two lines: ',1)[1].split(' (2) ')
        pieces += [p[0], '(2) '+p[1]]
    if n==3:
        c,b=d.split('Three short columns: ',1)[1].split(' Bottom line: ')
        c=c.replace('. Random-utility ','.\nRandom-utility ').replace('. Inequality of opportunity ','.\nInequality of opportunity ')
        for col in c.split('\n'): pieces+=col.split(' — ')
        pieces.append(b)
    if n==7:pieces.append(d.split('one line: ',1)[1])
    if n==10:
        p=d.split('Two columns: ',1)[1].split(' Caption: ')[0]
        for col in p.replace('. conditional — ','.\nconditional — ').split('\n'):
            label,body=col.split(' — ');pieces += [label]+body.rstrip('.').split('; ')
    if n==16:
        p=d.split('Two lines: ',1)[1].split(' (2) ')
        pieces += [p[0],'(2) '+p[1]]
    if n==18:
        p=d.split('Small table: ',1)[1].rstrip('.')
        heading,body=p.split(': ',1)
        pieces += ['perturbation','preference share','environment ordering']
        for row in body.split('; '):
            left,right=row.split(' / ')
            for label in ['reference convention','age-curvature bounds','couples male-leisure pin']:
                if left.startswith(label):
                    pieces += [label,left[len(label):].strip(),right];break
            else:pieces += left.split(': ')+[right]
    if n==21:
        for row in d.split('Table: ',1)[1].rstrip('.').split('; '):pieces+=row.split(' → ')
    if n==22:
        p=d.split('Three lines: ',1)[1]
        p=p.replace('. Finding: ','.\nFinding: ').replace('. Margin: ','.\nMargin: ')
        pieces += p.split('\n')
    return pieces


def pdf_words(path):
    r=subprocess.run([shutil.which('pdftotext'),'-bbox',str(path),'-'],capture_output=True,check=True)
    root=ET.fromstring(r.stdout)
    return [[(w.text or '',*[float(w.attrib[k]) for k in ['xMin','yMin','xMax','yMax']])
             for w in p.iter() if w.tag.endswith('}word')]
            for p in root.iter() if p.tag.endswith('}page')]


def main(build='build',jobs=None):
    jobs=jobs or JOBS;out=HERE/build;checks=[]
    def check(label,condition,detail=''):
        checks.append(dict(check=label,pass_=bool(condition),detail=detail))
        print('  [%s] %s%s'%('PASS' if condition else 'FAIL',label,': '+str(detail) if detail else ''))
    tex,frames,tags,backups=source_frames();slides,short=read_content()
    ids=[int(n) if n.isdigit() else n for n in re.findall(r'(?m)^% SLIDE (\d+b?)$',tex.split('\n\\appendix\n',1)[0])]
    byid=dict(zip(ids,frames));content_byid={s['number']:s for s in slides}
    slidedir=HERE/'figures/slides'
    print('=== 1. figure paths ===')
    used=set(re.findall(r'\\slidefig\{([^}]+)\}',tex))
    onfile={p.name.removesuffix('_slide.pdf') for p in slidedir.glob('*_slide.pdf')}
    check('every slide figure resolves',not (used-onfile),str(sorted(used-onfile)))
    check('no unused active slide figure',not (onfile-used),str(sorted(onfile-used)))
    check('no paper-style figure left on a slide',not re.search(r'\\deckfig\{',tex))
    check('theory figure appears exactly on slides 4 and 5',
          [n for n,f in zip(ids,frames) if r'\ModelFigure{' in f]==[4,5])
    check('empirical figure replaces both primitives',all(x in byid[5] for x in
          [r'\HidePayDots',r'\HideAbilitySets',r'\OppDistribution',r'\WageDensity']))
    print('=== 2. number macros ===')
    nums=(HERE/'deck_numbers_v1.tex').read_text(encoding='utf-8')
    defined=set(re.findall(r'\\newcommand\{\\([A-Za-z]+)\}',nums))
    usedmac=set(re.findall(r'\\([A-Za-z]+)\b',tex))
    check('no orphaned generated macro',not (defined-usedmac),str(sorted(defined-usedmac)))
    expectedprefix=r'^(?:V(?:State|Share|Round|Band|Male|Par|Hours|Emp|Ext|Peak|Gap|Bench|Age|Couple|Draw|Geo|Wish)|Doc|Share|Band|Par|Sub|Bench|Ext|Reg|EOne|Hours|Emp|Occ|Wage|Wish|Geo|PrefN|PrefNeg|Rnd|N[A-Z]|I[A-Z]|Level)'
    style_defined=set(re.findall(r'\\newcommand\{\\([A-Za-z]+)\}',
        (HERE/'jmp_beamer_preamble.tex').read_text(encoding='utf-8')+
        (HERE/'theory_model_figure.tex').read_text(encoding='utf-8')))
    missing=sorted(m for m in usedmac if re.match(expectedprefix,m) and m not in defined|style_defined)
    check('every number macro is generated',not missing,str(missing))
    nearmiss=sorted(u for u in usedmac-defined if any(k.endswith(u) and len(k)-len(u)<=2 for k in defined))
    check('no near-miss of a generated macro',not nearmiss,str(nearmiss))
    literal=[]
    for i,frame in enumerate(frames+backups):
        f=frame.replace('\\note{'+argument(frame,'note')+'}','')
        f=re.sub(r'\\\[.*?\\\]|\$.*?\$','',f,flags=re.S)
        f=re.sub(r'\\renewcommand\{[^}]+\}\{[^}]+\}','',f)
        f=re.sub(r'\d+(?:\.\d+)?(?:pt|em|ex|cm|\\textwidth|\\paperwidth)','',f)
        f=re.sub(r'\\slidefig\{[^}]+\}|\\(?:only|onslide)<[^>]+>|\\textsuperscript\{[^}]+\}', '',f)
        f=re.sub(r'\\(?:OppDistribution|WageDensity)\{[^}]+\}|B\d','',f)
        digits=re.findall(r'\d+(?:[,.]\d+)*',f)
        if digits:literal.append(f'frame {i+1}: {digits}')
    check('no hand-typed quantitative numerals on slides',not literal,'; '.join(literal) or 'all numerical prose uses generated commands')
    # Regenerate to an isolated output file, then compare bytes with the
    # compiled macro input (generator output is filtered against source deck).
    from make_deck_macros_v1 import build as numbers_build,DEFAULT_SPRINT
    import tempfile
    probe=HERE/'deck_numbers_check.tmp'
    numbers_build(DEFAULT_SPRINT,probe)
    check('number macros equal regenerated source values',probe.read_bytes()==(HERE/'deck_numbers_v1.tex').read_bytes())
    probe.unlink()
    print('=== 3. frames, orders and pages ===')
    check('exactly 26 running-order slides',len(frames)==len(slides)==26)
    check('exact 45-minute order including insertions',ids==[s['number'] for s in slides],str(ids))
    check('exact unchanged 25-minute order',[n for n,t in zip(ids,tags) if t=='shortdeck']==short==[1,2,3,5,6,7,9,12,13,14,15,16,17,18,22],str(short))
    check('the final plan has nine full-only slides',tags.count('longdeck')==9)
    check('the final plan has two merges',tags.count('mergedaway')==2)
    check('B1 in three blocks, then B2--B6',len(backups)==8 and
          [re.search(r'B\d',argument(f,'headlineframe')).group() for f in backups]==['B1']*3+['B2','B3','B4','B5','B6'])
    check('exact build counts for household, preferences and geography',
          {n:overlay_count(f) for n,f in zip(ids,frames) if overlay_count(f)>1}=={'5b':4,'9b':2,19:2})
    check('welfare equation uses flat pay on own set',
          r'\Omega_i(\text{flat pay }w\text{ on own set})=\Omega_i(\text{actual})' in byid[12]
          and r'u_i(W^1_i,\bar l)' not in byid[12])
    # Numerical checks independently separate the two counterfactual scopes.
    import pandas as pd
    from make_deck_macros_v1 import DEFAULT_SPRINT
    from deck_content_v4 import macro_values
    values=macro_values()
    states=pd.read_csv(DEFAULT_SPRINT/'figures/figW01_welfare_distributions.csv')
    states=states[states.basis=='W1_raw'].set_index('cell')
    drop=100*(states.loc['{}','gini']-states.loc['{A,B,D}','gini'])/states.loc['{}','gini']
    check('77 percent is the direct environment counterfactual',float(values['VEnvAlone'])==round(drop))
    drawdata=pd.read_csv(DEFAULT_SPRINT/'figures/figS6_02_coefficient_stability.csv')
    check('draw-count macros cover both declared ranges',
          float(values['VDrawMoveAll'])==round(drawdata.deviation_in_R100_SE.abs().max(),2)
          and float(values['VDrawMove'])==round(drawdata[drawdata.R>=100].deviation_in_R100_SE.abs().max(),1))
    manifest=json.loads((slidedir/'v41_source_manifest.json').read_text(encoding='utf8'))
    changed=[r['path'] for r in manifest if hashlib.sha256((DEFAULT_SPRINT.parents[1]/r['path']).read_bytes()).hexdigest()!=r['sha256']]
    check('v4.1 read-only figure inputs match source fingerprints',not changed,str(changed))
    density=json.loads((slidedir/'welfare_distribution_checks.json').read_text(encoding='utf8'))
    check('four density summaries match figW01 CSV',len(density)==4 and all(r['summary_matches'] for r in density))
    curves=json.loads((slidedir/'indifference_checks.json').read_text(encoding='utf8'))
    check('indifference curves use two own budgets and pass through observed jobs',
          len(curves)==2 and all(r['priced_nodes']==101 and r['utility_residual_max']<1e-10 and r['observed_curve_consumption_error']<1e-8 for r in curves))
    print('=== 4. logs; 5. PDF text; 6. exact authored words ===')
    tables=[];counts={}
    for job in jobs:
        path=out/(job+'.pdf');log=out/(job+'.log')
        check('PDF present: '+job,path.exists())
        check('log present: '+job,log.exists())
        if not path.exists() or not log.exists():continue
        text=log.read_text(encoding='utf-8',errors='replace')
        errors=len(re.findall(r'^!',text,re.M));over=text.count('Overfull');under=text.count('Underfull')
        check('clean log: '+job,errors==over==under==0,f'{errors} errors / {over} overfull / {under} underfull')
        order=short if job.endswith('_25min') else ids
        schedule=[(n,byid[n]) for n in order]+[(f'B{n}',f) for n,f in zip(['1a','1b','1c','2','3','4','5','6'],backups)]
        pageframes=[(n,f) for n,f in schedule for _ in range(overlay_count(f))]
        pdf=pymupdf.open(path);counts[job]=len(pdf)
        check('PDF pages = frames + overlays: '+job,len(pdf)==len(pageframes),f'{len(pdf)} pages / {len(schedule)} frames')
        noteview=job.endswith('_rehearsal');width=pdf[0].rect.width/(2 if noteview else 1)
        check('page aspect / notes second screen: '+job,abs(pdf[0].rect.width/pdf[0].rect.height-(32/9 if noteview else 16/9))<0.002)
        subprocess.run([shutil.which('pdftotext'),'-layout',str(path),str(out/(job+'_text.txt'))],check=True,capture_output=True)
        words=pdf_words(path)
        headbad=[];phrasebad=[];notebad=[];forbidden=[];allrows=[]
        for pi,((number,frame),page,wds) in enumerate(zip(pageframes,pdf,words)):
            # Header bounds are measured from the actual white title text,
            # then authoritative Poppler words are read in that rectangle.
            spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
            white=[s for s in spans if all((s['color']>>shift)&255 >= 240 for shift in [0,8,16]) and s['bbox'][0]<width]
            bottom=max([s['bbox'][3] for s in white],default=0)+1
            projection=[w for w in wds if w[1]<width]
            head=' '.join(w[0] for w in projection if w[2]<bottom)
            body=' '.join(w[0] for w in projection if w[2]>=bottom and w[4]<page.rect.height-14)
            full=' '.join(w[0] for w in projection)
            if number in content_byid:
                expected=content_byid[number]['headline']
                if number==1:
                    if normalized(expected) not in normalized(full):headbad.append(str(number))
                    head=expected
                elif normalized(head)!=normalized(expected):headbad.append(f'{number}: {head!r} != {expected!r}')
                for phrase in authored_phrases(content_byid[number]):
                    if normalized(phrase) not in normalized(full):phrasebad.append(f'{number}: {phrase}')
                if noteview:
                    note=' '.join(w[0] for w in wds if w[1]>=width)
                    # TeX may hyphenate prose at a line ending. Source notes
                    # are also compared byte-for-byte after TeX encoding below.
                    if normalized(note).replace('-','')!=normalized(content_byid[number]['note']).replace('-',''):
                        notebad.append(str(number))
            else:
                expected=prose(argument(frame,'headlineframe'))
                if normalized(head)!=normalized(expected):headbad.append(str(number)+': '+head)
            hits=FORBIDDEN.findall(' '.join(w[0] for w in wds))
            if hits:forbidden.append(f'p{pi+1}: {hits}')
            element=' / '.join(re.findall(r'\\slidefig\{([^}]+)\}',frame))
            display=bool(re.search(r'(?<!\\)\\\[',frame))
            if not element:element='theory diagram' if r'\ModelFigure{' in frame else 'equations + table' if display and r'\begin{tabular}' in frame else 'equations' if display else 'table' if r'\begin{tabular}' in frame else 'three literature columns' if number==3 else 'text'
            row=dict(number=number,headline=expected,element=element,builds=overlay_count(frame),on_slide_words=nwords(full) if number==1 else nwords(head+' '+body),body_words=nwords(body),pdf_page=pi+1)
            allrows.append(row)
        check('PDF headlines equal authoritative content: '+job,not headbad,'; '.join(headbad) or 'all headlines match')
        check('authored captions and prose present verbatim: '+job,not phrasebad,'; '.join(phrasebad) or 'all authored fragments match')
        check('no internal label in PDF text layer: '+job,not forbidden,'; '.join(forbidden) or 'zero hits')
        if noteview:check('rehearsal notes match authored speech: '+job,not notebad,','.join(notebad) or 'all running notes match')
        if job==JOBS[0]:tables=allrows
        pdf.close()
    if JOBS[0] in jobs and JOBS[2] in jobs:
        full=pymupdf.open(out/(JOBS[0]+'.pdf'))
        rehearsal=pymupdf.open(out/(JOBS[2]+'.pdf'))
        differing=[]
        for i in range(min(len(full),len(rehearsal))):
            a=full[i].get_pixmap()
            b=rehearsal[i].get_pixmap(clip=full[i].rect)
            if (a.width,a.height,a.samples)!=(b.width,b.height,b.samples):differing.append(i+1)
        check('rehearsal projection pixels equal full deck',len(full)==len(rehearsal) and not differing,str(differing) if differing else 'all pages identical')
        full.close();rehearsal.close()
    notesbad=[str(n) for n,f in zip(ids,frames) if argument(f,'note')!=tex_escape(content_byid[n]['note'])]
    check('source notes are verbatim (TeX encoding only)',not notesbad,','.join(notesbad))
    original=subprocess.run(['git','show','a42c15b:beamer/jmp_beamer_preamble.tex'],cwd=HERE,capture_output=True,check=True).stdout
    check('shared preamble unchanged from v3',original.replace(b'\r\n',b'\n')==(HERE/'jmp_beamer_preamble.tex').read_bytes().replace(b'\r\n',b'\n'))
    # v3's <=12-word cap is superseded by the exact longer author text.
    # The authored-prose gates above retain and strengthen its purpose:
    # prohibit unauthorised copy instead of silently accepting extra words.
    check('26-slide content replaces the legacy 12-word ceiling',len(slides)==26,'word counts reported; verbatim content gates enforced above')
    print('=== 7. slide figure fonts and text ===')
    style=json.loads((slidedir/'slide_style_v1.json').read_text())
    pts={k:v for k,v in style.items() if k.endswith('size') and isinstance(v,(int,float))}
    check('every recorded font >= 18 pt',bool(pts) and min(pts.values())>=18,str(pts))
    fs=style['figure.figsize'];check('16:9 figure-kit canvas',abs(fs[0]/fs[1]-16/9)<0.02)
    bad=[];small=[]
    for name in sorted(used):
        p=slidedir/(name+'_slide.pdf')
        if not p.exists():continue
        r=subprocess.run([shutil.which('pdftotext'),str(p),'-'],capture_output=True,check=True)
        hits=FORBIDDEN.findall(r.stdout.decode('utf-8'))
        if hits:bad.append(name+':'+str(hits))
        pdf=pymupdf.open(p)
        sizes=[s['size'] for b in pdf[0].get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
        if not sizes or min(sizes)<17.99:small.append(name+':'+str(min(sizes,default=0)))
        pdf.close()
    check('no internal label in a slide figure',not bad,'; '.join(bad) or 'zero hits')
    check('actual figure PDF fonts >= 18 pt',not small,'; '.join(small) or 'all active figure PDFs pass')
    if tables:
        # One table row per logical frame; the geography row has both elements.
        unique={}
        for row in tables:
            key=row['number']
            if key not in unique:unique[key]=row
            else:unique[key]['on_slide_words']=max(unique[key]['on_slide_words'],row['on_slide_words'])
        data=list(unique.values())
        with (HERE/'slide_table_v1.csv').open('w',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(data[0]));writer.writeheader();writer.writerows(data)
        (out/'slide_table_v4.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    report=dict(passed=all(c['pass_'] for c in checks),checks=checks,page_counts=counts,
                content_sha256=hashlib.sha256(CONTENT.read_bytes()).hexdigest())
    (out/'verification_v4.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print('\nVERDICT: '+('ALL PASS' if report['passed'] else 'FAIL')+f' ({sum(c["pass_"] for c in checks)}/{len(checks)} checks)')
    return 0 if report['passed'] else 1
