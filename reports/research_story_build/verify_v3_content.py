"""Bounded revision checks. Text presence is not certification of estimates."""
import json
from pathlib import Path
import re
from v3_sections import TITLE, SECTIONS, ABSTRACT, QA

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
source='\n'.join(s for _,s in SECTIONS)
checks={
 1: TITLE=='Unequal Job Opportunities and Well-Being Inequality: A Latent-Jobs Structural Decomposition',
 2: ABSTRACT.startswith('Observed differences in earnings and working time') and 'under correction' not in ABSTRACT,
 3: '{{figure:motivation}}' in source and '{{figure:reference}}' in source,
 4: all(s in source for s in ['Dagsvik and Strøm','Capéau, Decoster and Dekkers','Decoster and Haan','Jacquet, Jia and Thoresen','Aaberge, Colombino and Strøm']),
 5: 'narrower market-opportunity allocation' in source,
 6: all(s not in source for s in ['preferences cannot generate','78.6','21.4']),
 7: all(s in source for s in ['\\log f_i','\\omega_{im}=','\\omega_{if}=','{{table:bands}}']),
 8: 'maintained reduced structural representation' in source,
 9: 'relative intensities rather than' in source,
 10: 'cancels in comparisons between working jobs' in source,
 11: 'jointly impose a restriction' in source,
 12: 'one flat monthly disposable-consumption amount to every alternative' in source,
 13: '{{n:welf_comparisons}}' in SECTIONS[12][1] and 'arithmetic consumption average' in SECTIONS[12][1],
 14: 'no unconditional theorem that a wider opportunity set raises' in source,
 15: 'mean squared-age or squared-experience' in source and '{{table:operators}}' in source,
 16: 'not necessarily one' in source,
 17: 'not uniformly an observed wage' in source and 'Employee fringe benefits are non-cash' in source,
 18: 'conditions correctly on retention remains a substantive open question' in source,
 19: all('{{table:'+k+'}}' in source for k in ['coefficients','fit','states','contributions']),
 20: 'no empirical allocation of this welfare between partners' in source,
 21: 'A finite standard error signals estimation uncertainty, not non-identification' in source,
 22: '{{figure:matched}}' in source and 'six panels' in source,
 23: 'common structural opportunity density' in source and 'no such test is reported' in source,
 24: not re.search(r'(?<!\\)qquad', source),
 25: 'does not freshly reconstruct the raw survey' in source,
 26: 'small first integral alone does not bound the second' in source,
}
assert all(checks.values()), {k:v for k,v in checks.items() if not v}
assert len(QA)>=25
for f in ['JMP_research_story_report_v3.html','numbers_of_record_v3.json']:
    assert (ROOT/'reports'/f).is_file()
tex=(ROOT/'manuscript/JMP_working_paper_for_seminar_v3.tex').read_text('utf-8')
assert TITLE in tex
assert '{{' not in tex
for path in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',tex):
    assert (ROOT/'manuscript'/path).is_file(),path
record={'text_checks':checks,'questions':len(QA),
        'interpretation':'Presence checks plus manual reading; not certification of corrected estimates.',
        'finding_25_status':'Historical notebook identity preserved and corrected-input cell tested; complete fresh corrective orchestration remains pending.',
        'scientific_open':'Corrected sample/budgets/support/criterion/estimates and downstream results; resource-pathway repricing; estimator-to-welfare scale equivalence; stochastic foundation; cross-type reference.'}
(HERE/'render_checks_v3/content_checks.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print('All 26 findings have explicit dispositions in the text; fresh corrective notebook execution remains pending.')
