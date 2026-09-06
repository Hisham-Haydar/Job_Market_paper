"""Build the three existing Beamer drivers with latexmk; fail on any error."""
from pathlib import Path
import argparse
import os
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
BUILD=HERE/'build'
JOBS={'full':'JMP_seminar_deck_v1','short':'JMP_seminar_deck_v1_25min',
      'rehearsal':'JMP_seminar_deck_v1_rehearsal'}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('variant',choices=['all',*JOBS],default='all',nargs='?')
    p.add_argument('--no-verify',action='store_true',help='compile pass during layout work')
    a=p.parse_args()
    env=os.environ.copy()
    env['PYTHONPATH']=str(BUILD/'python_deps')+os.pathsep+env.get('PYTHONPATH','')
    env['MPLCONFIGDIR']=str(BUILD/'matplotlib')
    env['PYTHONIOENCODING']='utf-8'
    if os.name=='nt':
        # Git's usr\bin carries the perl latexmk needs. But Git's mingw64\bin
        # ships a Glyph & Cog pdftotext with no -bbox (it exits 99 on the word
        # -bbox the verifier reads), so MiKTeX's Poppler build goes in FRONT.
        poppler=Path(os.path.expanduser(
            r'~\AppData\Local\Programs\MiKTeX\miktex\bin\x64'))
        head=[str(poppler)] if (poppler/'pdftotext.exe').is_file() else []
        env['PATH']=os.pathsep.join(
            head+[r'C:\Program Files\Git\usr\bin',env['PATH']])
    def run(args,**kw):
        return subprocess.run(args,cwd=HERE,env=env,check=True,**kw)
    BUILD.mkdir(exist_ok=True)
    run([sys.executable,'make_deck_macros_v1.py'])
    run([sys.executable,'make_slide_figures_v1.py','--missing-only'])
    run([sys.executable,'make_slide_figures_v41.py'])
    jobs=list(JOBS.values()) if a.variant=='all' else [JOBS[a.variant]]
    for job in jobs:
        print('Building '+job,flush=True)
        with (BUILD/(job+'_latexmk.txt')).open('w',encoding='utf-8') as f:
            run(['latexmk','-pdf','-interaction=nonstopmode','-halt-on-error',
                 '-outdir=build',job+'.tex'],stdout=f,stderr=subprocess.STDOUT)
        run(['pdftotext','-layout','build/'+job+'.pdf','build/'+job+'_text.txt'])
        log=(BUILD/(job+'.log')).read_text(encoding='utf-8',errors='replace')
        print('  overfull=%d underfull=%d'%(log.count('Overfull'),log.count('Underfull')),flush=True)
    if not a.no_verify:
        cmd=[sys.executable,'verify_deck_v1.py']
        for job in jobs:cmd+=['--job',job]
        run(cmd)
        if a.variant=='all':run([sys.executable,'write_deck_report_v4.py'])
    return 0


if __name__=='__main__':sys.exit(main())
