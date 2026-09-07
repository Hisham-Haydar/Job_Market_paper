// Render the published page to plain text with all numerals substituted,
// so the prose can be proof-read as the reader will see it.
const fs = require('fs');
const vm = require('vm');

const P = 'C:/Users/hisham/Repo/Job_Market_paper/reports/JMP_research_story_report_v1.html';
const html = fs.readFileSync(P, 'utf8');

function grab(id) {
  const m = html.match(new RegExp(
    '<script id="' + id + '" type="application/json">([\\s\\S]*?)</script>'));
  return JSON.parse(m[1]);
}
const NOR = grab('NOR-DATA');
const AUX = grab('AUX-DATA');

const blocks = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
const code = blocks[blocks.length - 1][1];
const sb = { MINUS: '\u2212', Math, Number, Array, String };
vm.createContext(sb);
vm.runInContext(
  code.match(/function dg\(d, dflt\)\{[^}]*\}/)[0] + '\n' +
  code.match(/function fmt\(v, f, d\)\{[\s\S]*?\n\}/)[0] + '\nthis.fmt = fmt;', sb);

function look(src, key) {
  if (src === 'nor') { const e = NOR.entries[key]; return e === undefined ? undefined : e.value; }
  let c = AUX;
  for (const p of key.split('.')) { if (c === null || c === undefined) return undefined; c = c[p]; }
  return c;
}

let body = html.split('<main id="doc">')[1].split('</main>')[0];

body = body.replace(
  /<span class="n" data-src="([^"]+)" data-k="([^"]+)" data-f="([^"]+)"(?: data-d="(\d+)")?[^>]*><\/span>/g,
  (m, s, k, f, d) => sb.fmt(look(s, k), f, d));
body = body.replace(/<span class="lit"[^>]*>([\s\S]*?)<\/span>/g, '$1');
body = body.replace(/<figure class="fig">[\s\S]*?<\/figure>/g, '\n   [FIGURE]\n');
body = body.replace(/<div class="box-t">([\s\S]*?)<\/div>/g, '\n>> $1\n');
body = body.replace(/<h2[^>]*>/g, '\n\n======== ').replace(/<h3[^>]*>/g, '\n--- ');
body = body.replace(/<li>/g, '\n  - ');
body = body.replace(/<\/(p|li|h2|h3|h4|tr|div|ul|ol)>/g, '\n');
body = body.replace(/<\/t[dh]>/g, ' | ');
body = body.replace(/<[^>]+>/g, '');

const ENT = {
  '&mdash;': '--', '&ndash;': '-', '&nbsp;': ' ', '&rsquo;': "'", '&lsquo;': "'",
  '&ldquo;': '"', '&rdquo;': '"', '&amp;': '&', '&minus;': '-', '&plusmn;': '+/-',
  '&hellip;': '...', '&lt;': '<', '&gt;': '>', '&theta;': 'theta', '&mu;': 'mu',
  '&sigma;': 'sigma', '&omega;': 'omega', '&beta;': 'beta', '&delta;': 'delta',
  '&eacute;': 'e', '&egrave;': 'e', '&times;': 'x', '&cup;': 'U', '&quot;': '"',
};
body = body.replace(/&[a-z]+;/g, m => ENT[m] !== undefined ? ENT[m] : m);
body = body.replace(/[ \t]+/g, ' ').replace(/ *\n */g, '\n').replace(/\n{3,}/g, '\n\n');

fs.writeFileSync(process.argv[2] || 'rendered.txt', body, 'utf8');
console.log('wrote ' + (body.length / 1024).toFixed(0) + ' KB of text');
const leftover = body.match(/&[a-z]+;/g);
if (leftover) console.log('unconverted entities:', [...new Set(leftover)].join(' '));
