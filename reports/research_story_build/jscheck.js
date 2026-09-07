// Syntax-check the page's inline JS, and exercise its formatter on real keys.
const fs = require('fs');
const vm = require('vm');

const P = 'C:/Users/hisham/Repo/Job_Market_paper/reports/JMP_research_story_report_v1.html';
const html = fs.readFileSync(P, 'utf8');

function grab(id) {
  const m = html.match(new RegExp('<script id="' + id +
    '" type="application/json">([\\s\\S]*?)</script>'));
  return JSON.parse(m[1]);
}
const NOR = grab('NOR-DATA');
const AUX = grab('AUX-DATA');
console.log('NOR entries', Object.keys(NOR.entries).length);
console.log('AUX groups ', Object.keys(AUX).filter(k => k[0] !== '_').join(', '));

// last <script> block is the page logic
const blocks = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
const code = blocks[blocks.length - 1][1];
try {
  new vm.Script(code);
  console.log('page JS syntax: OK (' + code.length + ' chars)');
} catch (e) {
  console.log('page JS syntax: FAIL ' + e.message);
  process.exit(1);
}

// re-implement fmt() exactly as the page defines it, by evaluating the
// function source lifted from the page, so the check tests the real code.
const fmtSrc = code.match(/function fmt\(v, f, d\)\{[\s\S]*?\n\}/)[0];
const dgSrc = code.match(/function dg\(d, dflt\)\{[^}]*\}/)[0];
const sandbox = { MINUS: '\u2212', Math, Number, Array, String, console };
vm.createContext(sandbox);
vm.runInContext(dgSrc + '\n' + fmtSrc + '\nthis.fmt = fmt;', sandbox);

// pull every (key, fmt, digits) triple actually used by the document
const uses = [...html.matchAll(
  /<span class="n" data-src="([^"]+)" data-k="([^"]+)" data-f="([^"]+)"(?: data-d="(\d+)")?/g)];
console.log('bound spans', uses.length);

function lookup(src, key) {
  if (src === 'nor') {
    const e = NOR.entries[key];
    return e === undefined ? undefined : e.value;
  }
  let cur = AUX;
  for (const part of key.split('.')) {
    if (cur === null || cur === undefined) return undefined;
    cur = cur[part];
  }
  return cur;
}

let bad = 0, blank = 0;
for (const [, src, key, f, d] of uses) {
  const v = lookup(src, key);
  if (v === undefined) { console.log('  MISSING', src + ':' + key); bad++; continue; }
  const out = sandbox.fmt(v, f, d);
  if (out === '??' || out === 'NaN' || out === '' || /NaN/.test(out)) {
    console.log('  BAD RENDER', src + ':' + key, 'fmt=' + f, '->', JSON.stringify(out));
    blank++;
  }
}
console.log('missing keys', bad, '| bad renders', blank);

const SPOT = [
  ['nor', 'C_pref_female_raw_share', 'pct', '2'],
  ['nor', 'C_env_female_raw_share', 'pct', '2'],
  ['nor', 'equalization_pref_only', 'signpct', '1'],
  ['nor', 'equalization_env_only', 'signpct', '1'],
  ['nor', 'state_I11_female_raw', 'sci', '1'],
  ['nor', 'n_households_singles', 'int', undefined],
  ['nor', 'drawcount_ladder', 'list', undefined],
  ['nor', 'beta_ll_status', 'raw', undefined],
  ['nor', 'C_pref_female_raw__cr1_interval', 'range', undefined],
  ['nor', 'rum_leisure_gap_benchmark', 'sf3', undefined],
  ['nor', 'regional_opportunity_mass_range_B', 'range', undefined],
  ['nor', 's_env_female_raw__cr1_interval', 'rangepct', '1'],
  ['aux', 'params41.beta_h_f35.estimate', 'f4', undefined],
  ['aux', 'params41.beta_l_age2_sm.se_robust', 'f4', undefined],
  ['aux', 'hours_cells.female|F35.lfs_share_of_focal_bands', 'f3', undefined],
  ['aux', 'chron.peak_negll_gain', 'f1', undefined],
  ['aux', 'defs.R_reference', 'int', undefined],
];
console.log('\nspot checks');
for (const [src, key, f, d] of SPOT) {
  console.log('  ' + (key + ' [' + f + ']').padEnd(58),
              JSON.stringify(sandbox.fmt(lookup(src, key), f, d)));
}
process.exit(bad + blank === 0 ? 0 : 1);
