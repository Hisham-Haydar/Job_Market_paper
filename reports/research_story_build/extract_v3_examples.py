"""Export anonymous, already-priced evaluator examples; no new estimation/pricing.

Uses the identity audit's input-hash checks and its disclosed history-only
runtime exception. No identifiers or original household demographic rows leave
the evaluator. Displayed jobs are quadrature nodes, not observed jobs.
"""
import importlib.util
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
MNL = HERE.parents[2] / 'MNL'
spec = importlib.util.spec_from_file_location('identity', MNL/'scripts/corr/check_welfare_identity_v1.py')
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
out = {'status': 'current evaluator at historical estimates, not corrected results',
       'privacy': 'No identifiers or raw profiles; simulated jobs only; selected median-value household per type.'}

def norm(x):
    return np.exp(x - np.logaddexp.reduce(x))

selected = {}
single_calls = {}
original = a.S1.W1C.wm.compute_measures
def single_capture(cfg, core, **kwargs):
    ans = original(cfg, core, **kwargs)
    if core.group != 'singles_female':
        return ans
    call = single_calls.get(core.group, 0)
    single_calls[core.group] = call + 1
    states = ['baseline', 'preferences', 'environment', 'all']
    if call >= len(states):
        return ans
    state = states[call]
    if core.group not in selected:
        selected[core.group] = int(np.argsort(ans['W1'])[len(ans['W1'])//2])
    i = selected[core.group]
    c = core.c_norm[i]*core.c_scale
    l = core.leisure_term[i]
    opp = core.opp[i]
    bc = a.S1.W1C.wm.box_cox(core.c_norm[i], core.theta_c)
    v = l + opp + bc
    hours = 80-core.l_norm[i]*core.l_scale
    sample = sorted(set([int(np.argmin(hours)), int(np.argmin(abs(hours-20))),
                         int(np.argmin(abs(hours-35))), int(np.argmax(hours))]))
    item = {'W': float(ans['W1'][i]), 'lambda': core.c_scale, 'theta': core.theta_c,
            'logJ': float(np.logaddexp.reduce(v)-np.logaddexp.reduce(opp)),
            'logH': float(np.logaddexp.reduce(l+opp)-np.logaddexp.reduce(opp)),
            'nodes': int(c.size), 'jobs': []}
    for r in sample:
        item['jobs'].append({'hours': float(hours[r]), 'C': float(c[r]),
          'L': float(l[r]), 'opportunity': float(norm(opp)[r]),
          'choice': float(norm(v)[r]), 'reference': float(norm(l+opp)[r])})
    out.setdefault('single', {})[state] = item
    return ans
a.S1.W1C.wm.compute_measures = single_capture
print('Extracting singles examples', flush=True)
a.singles()

original_load = a.load_couples
last = {}
def capture_load(frame, spec, **kwargs):
    last['frame'] = frame
    return original_load(frame, spec, **kwargs)
a.load_couples = capture_load
original_c = a.CL.w1_own
couple_call = 0
def couple_capture(V, log_c, cols, scale):
    global couple_call
    ans = original_c(V, log_c, cols, scale)
    state = ['baseline', 'preferences', 'environment', 'all'][couple_call]
    couple_call += 1
    if 'couple' not in selected:
        selected['couple'] = int(np.argsort(ans['W1'])[len(ans['W1'])//2])
    i = selected['couple']
    frame = last['frame'].iloc[i*V.shape[1]:(i+1)*V.shape[1]]
    # Get utility coefficients from the executable named parameter order.
    model_spec, _ = a.RL.load_spec()
    names = list(model_spec.all_param_names)
    th = np.load(a.C3.CB/'r240_theta_hat_v1.npy')
    td = dict(zip(names, th))
    first = frame.iloc[[0]]
    am, af = a.CL.leisure_coefficients(first, td)
    hm = frame['hours_male'].to_numpy() if 'hours_male' in frame else frame['h_male'].to_numpy()
    hf = frame['hours_female'].to_numpy() if 'hours_female' in frame else frame['h_female'].to_numpy()
    lm = (80-hm)/10
    lf = (80-hf)/10
    l = am[0]*a.CL.bc(lm, td['theta_l_m']) + af[0]*a.CL.bc(lf, td['theta_l_f'])
    v = V[i]
    opp = v-log_c[i]-l
    c = np.exp(log_c[i])*scale
    sample = []
    for em, ef in [(False,False),(True,False),(False,True),(True,True)]:
        inds = np.flatnonzero((hm>0)==em)
        inds = inds[((hf[inds]>0)==ef)]
        if len(inds): sample.append(int(inds[len(inds)//2]))
    item = {'W': float(ans['W1'][i]), 'lambda': scale, 'theta': 0,
            'logJ': float(np.logaddexp.reduce(v)-np.logaddexp.reduce(opp)),
            'logH': float(np.logaddexp.reduce(v-log_c[i])-np.logaddexp.reduce(opp)),
            'nodes': int(c.size), 'jobs': []}
    for r in sample:
        item['jobs'].append({'hours_m':float(hm[r]), 'hours_f':float(hf[r]),
           'C':float(c[r]), 'L':float(l[r]), 'opportunity':float(norm(opp)[r]),
           'choice':float(norm(v)[r]), 'reference':float(norm(v-log_c[i])[r])})
    out.setdefault('couple', {})[state] = item
    return ans
a.CL.w1_own = couple_capture
print('Extracting couples examples', flush=True)
a.couples()
(HERE/'evaluator_examples_v3.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
print('Wrote anonymous evaluator examples', flush=True)
