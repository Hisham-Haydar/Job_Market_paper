# -*- coding: utf-8 -*-
"""HTML shell: styling, the render-from-JSON engine, and the self-check."""

CSS = r"""
:root{
  --ink:#1a1a1a; --mut:#5a5f66; --line:#dcdfe4; --bg:#ffffff; --soft:#f6f7f9;
  --accent:#1f4e79; --accent2:#7a3b12; --warn:#8a1c1c; --ok:#14612e;
  --mono:"SFMono-Regular",Consolas,"Liberation Mono",Menlo,monospace;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.62 Georgia,"Iowan Old Style","Times New Roman",serif;}
#wrap{display:flex;align-items:flex-start;max-width:1500px;margin:0 auto}
#toc{position:sticky;top:0;flex:0 0 302px;height:100vh;overflow-y:auto;
  padding:22px 16px 60px 20px;border-right:1px solid var(--line);background:var(--soft);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;font-size:13px;line-height:1.45}
#toc h2{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);
  margin:0 0 12px;font-weight:700}
#toc a{display:block;padding:4px 8px;color:var(--ink);text-decoration:none;border-radius:4px;
  border-left:2px solid transparent}
#toc a:hover{background:#e9ecf1}
#toc a.on{background:#e3eaf3;border-left-color:var(--accent);font-weight:600}
#toc .tnum{display:inline-block;min-width:22px;color:var(--mut);font-variant-numeric:tabular-nums}
#toc .grp{margin:14px 0 5px;padding-left:8px;font-size:10.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--mut);font-weight:700}
#doc{flex:1 1 auto;min-width:0;padding:34px 46px 140px;max-width:1000px}
h1{font-size:31px;line-height:1.22;margin:.1em 0 .1em;letter-spacing:-.01em}
.sub{color:var(--mut);font-size:15.5px;margin:0 0 4px}
.bandnote{color:var(--mut);font-size:10.5px;font-weight:400;white-space:nowrap}
h2{font-size:23px;margin:2.4em 0 .5em;padding-top:.45em;border-top:2px solid var(--ink);
  line-height:1.25;letter-spacing:-.005em}
h3{font-size:17.5px;margin:1.7em 0 .4em;color:var(--accent)}
h4{font-size:15px;margin:1.3em 0 .3em;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
p{margin:.62em 0}
ul,ol{margin:.55em 0 .55em 0;padding-left:1.35em}
li{margin:.28em 0}
code,.mono{font-family:var(--mono);font-size:.875em;background:var(--soft);
  padding:1px 4px;border-radius:3px}
a{color:var(--accent)}
.n{font-variant-numeric:tabular-nums;font-weight:600;
   border-bottom:1px dotted #b6bec9;cursor:help}
.n.bad{background:#ffe2e2;color:var(--warn);font-weight:700;border-bottom:2px solid var(--warn)}
.lit{font-variant-numeric:tabular-nums;border-bottom:1px dotted #e0d3b8;cursor:help}
.eq{font-family:var(--mono);font-size:13.5px;line-height:1.85;background:var(--soft);
  border-left:3px solid var(--accent);padding:11px 15px;margin:.85em 0;overflow-x:auto;
  white-space:pre-wrap}
.eq .cmt{color:var(--mut)}
table{border-collapse:collapse;width:100%;margin:.9em 0;font-size:13.4px;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.scroll{overflow-x:auto;margin:.9em 0}
.scroll table{margin:0}
th,td{border-bottom:1px solid var(--line);padding:5px 9px;text-align:left;vertical-align:top}
th{background:var(--soft);font-weight:700;font-size:12px;letter-spacing:.02em;
  border-bottom:2px solid #c6ccd4;position:sticky;top:0}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
tbody tr:hover{background:#fafbfc}
tr.grouphead td{background:#eef1f5;font-weight:700;font-size:12.5px;letter-spacing:.03em}
.bound{color:var(--accent2);font-weight:700}
.box{border:1px solid var(--line);border-radius:6px;padding:13px 17px;margin:1.1em 0;
  background:var(--soft);font-size:14.6px}
.box-t{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-weight:700;
  font-size:11.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--mut);margin-bottom:7px}
.box.prov{background:#f4f1ea;border-color:#ddd3bd}
.box.prov .box-t{color:var(--accent2)}
.box.warn{background:#fdf2f2;border-color:#f0cfcf}
.box.warn .box-t{color:var(--warn)}
.box.key{background:#eef3f8;border-color:#c9d8e8}
.box.key .box-t{color:var(--accent)}
.box.say{background:#f1f6f1;border-color:#cfe0cf}
.box.say .box-t{color:var(--ok)}
figure.fig{margin:1.3em 0;border:1px solid var(--line);border-radius:6px;padding:11px;background:#fff}
figure.fig img{width:100%;height:auto;display:block;border-radius:3px}
figcaption{font-size:12.8px;color:var(--mut);margin-top:8px;line-height:1.5;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.figname{font-family:var(--mono);font-size:11px;background:var(--soft);padding:1px 5px;
  border-radius:3px;margin-right:7px;color:var(--accent)}
.credit{margin-top:4px;font-style:italic;font-size:12px}
.qa{border-left:3px solid var(--line);padding:2px 0 2px 15px;margin:1.15em 0}
.qa:target{border-left-color:var(--accent);background:#f7fafd}
.qa-q{font-weight:700;font-size:16.5px;margin-bottom:6px}
.qa-i{display:inline-block;min-width:36px;color:var(--accent);font-family:var(--mono);font-size:13px}
.qa-s,.qa-t,.qa-p{font-size:14.6px;margin:5px 0}
.qa-s{background:#f1f6f1;border-radius:4px;padding:6px 10px}
.qa-p{color:var(--mut);font-size:13.6px}
.lab{display:inline-block;min-width:88px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--mut);font-weight:700;
  vertical-align:top}
.qa-s .lab{color:var(--ok)}
.termtab td:first-child{font-family:var(--mono);font-size:12px}
hr.soft{border:0;border-top:1px solid var(--line);margin:2.2em 0}
.tag{display:inline-block;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;font-weight:700;
  padding:1.5px 7px;border-radius:9px;background:#e6ebf1;color:var(--accent);margin-left:6px;
  vertical-align:middle}
.tag.no{background:#fbe6e6;color:var(--warn)}
.tag.yes{background:#e6f2e9;color:var(--ok)}
.lede{font-size:17px;color:#33383f}
#sc-summary{font-size:15px}
.sc-ok{color:var(--ok);font-weight:700}
.sc-bad{color:var(--warn);font-weight:700}
@media print{
  #toc{display:none} #doc{max-width:none;padding:0}
  h2{page-break-after:avoid} figure.fig{page-break-inside:avoid}
}
@media (max-width:1080px){
  #wrap{display:block} #toc{position:static;height:auto;width:auto;flex:none;
    border-right:0;border-bottom:1px solid var(--line)} #doc{padding:24px 20px 90px}
}
"""


JS = r"""
(function(){
"use strict";
var NOR = JSON.parse(document.getElementById('NOR-DATA').textContent);
var AUX = JSON.parse(document.getElementById('AUX-DATA').textContent);
var MINUS = '−';

function lookup(src, key){
  if(src === 'nor'){
    var e = NOR.entries[key];
    if(e === undefined) return null;
    return {v:e.value, ref:e.reference, source:e.source, basis:e.basis||'', col:e.column_or_key||''};
  }
  var cur = AUX, parts = key.split('.');
  for(var i=0;i<parts.length;i++){
    if(cur===null||cur===undefined) return null;
    cur = cur[parts[i]];
  }
  if(cur===undefined) return null;
  return {v:cur, ref:'auxiliary block '+key, source:(AUX._sources[parts[0]]||'(auxiliary)'),
          basis:'', col:key};
}

function dg(d, dflt){ return (d===undefined||d===null||d==='') ? dflt : parseInt(d,10); }

function fmt(v, f, d){
  if(v===null||v===undefined) return '??';
  if(Array.isArray(v)){
    if(f==='range') return v.map(function(x){return fmt(x,'f3',d);}).join(' to ');
    if(f==='rangepct') return v.map(function(x){return fmt(x,'pct',d);}).join(' to ');
    return v.map(function(x){return fmt(x,(f==='list'?'auto':f),d);}).join(', ');
  }
  if(typeof v === 'boolean') return v ? 'yes' : 'no';
  if(typeof v === 'string') return v;
  var av = Math.abs(v);
  switch(f){
    case 'int':      return Math.round(v).toLocaleString('en-GB');
    case 'pct':      return (v*100).toFixed(dg(d,1))+'%';
    case 'pctabs':   return (av*100).toFixed(dg(d,1))+'%';
    case 'signpct':  return (v>=0?'+':MINUS)+(av*100).toFixed(dg(d,1))+'%';
    case 'pp':       return (v*100).toFixed(dg(d,2));
    case 'ppabs':    return (av*100).toFixed(dg(d,2));
    case 'f1':       return v.toFixed(1);
    case 'f2':       return v.toFixed(2);
    case 'f3':       return v.toFixed(3);
    case 'f4':       return v.toFixed(4);
    case 'f5':       return v.toFixed(5);
    case 'sf1':      return (v>=0?'+':MINUS)+av.toFixed(1);
    case 'sf2':      return (v>=0?'+':MINUS)+av.toFixed(2);
    case 'f6':       return v.toFixed(6);
    case 'sf3':      return (v>=0?'+':MINUS)+av.toFixed(3);
    case 'sf4':      return (v>=0?'+':MINUS)+av.toFixed(4);
    case 'sci':      return v===0 ? '0' : v.toExponential(dg(d,1)).replace('e','×10^').replace('+','');
    case 'raw':      return String(v);
    default:
      if(v===0) return '0';
      if(av<1e-6) return v.toExponential(2);
      if(Number.isInteger(v)) return v.toLocaleString('en-GB');
      return v.toFixed(dg(d,4));
  }
}

var REG = [];
function render(){
  var els = document.querySelectorAll('#doc .n');
  for(var i=0;i<els.length;i++){
    var el = els[i];
    var src = el.getAttribute('data-src')||'nor';
    var key = el.getAttribute('data-k');
    var rec = lookup(src, key);
    if(rec===null){
      el.textContent = 'MISSING:'+key;
      el.className = 'n bad';
      REG.push({i:REG.length+1, txt:'MISSING', src:src, key:key, art:'—', ref:'KEY NOT FOUND', ok:false});
      continue;
    }
    var out = fmt(rec.v, el.getAttribute('data-f')||'auto', el.getAttribute('data-d'));
    el.textContent = out;
    var note = el.getAttribute('data-note')||'';
    el.title = key+'\n'+rec.ref+(rec.basis?('\nbasis: '+rec.basis):'')+
               '\nartefact: '+rec.source+(note?('\n'+note):'');
    REG.push({i:REG.length+1, txt:out, src:src, key:key, art:rec.source, ref:rec.ref, ok:true});
  }
}

function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}

// Classification of every numeral in the body.  Mirrors scripts/verify.py.
var SKIP_TAGS = {SCRIPT:1, STYLE:1, CODE:1, H1:1, H2:1, H3:1, H4:1, TH:1,
                 FIGCAPTION:1};
var SKIP_CLASS = ['n','lit','eq','exempt'];
var RE_PROPER = /\b(?:NUTS-\d|ISCO-\d+|EU-SILC|EU-LFS|SRCV|PT1|PT2|F35|FT|LH|R-\d+)\b/g;
var RE_RANGE  = /\d+(?:\.\d+)?\s*[–—-]\s*\d+(?:\.\d+)?/g;
var RE_XREF   = new RegExp(
  '\\b(?:sub)?(?:sections?|blocks?|figures?|parts?|steps?|points?|tables?)' +
  '\\s*\\u00a0?\\s*\\d+(?:\\.\\d+)?' +
  '(?:\\s*(?:,|and|to|&)\\s*\\d+(?:\\.\\d+)?)*', 'gi');

function strayAudit(){
  var root = document.getElementById('doc');
  var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
  var out = {stray:[], xref:0, structural:0}, node;
  while((node = w.nextNode())){
    if(!/[0-9]/.test(node.nodeValue)) continue;
    var el = node.parentElement, cls = false, tagSkip = false, sc = false;
    while(el && el !== root){
      if(el.id === 's23'){ sc = true; break; }
      for(var c=0;c<SKIP_CLASS.length;c++){
        if(el.classList.contains(SKIP_CLASS[c])){ cls = true; }
      }
      if(SKIP_TAGS[el.tagName]) tagSkip = true;
      el = el.parentElement;
    }
    if(sc || cls) continue;
    if(tagSkip){ out.structural++; continue; }
    var txt = node.nodeValue.replace(/\s+/g,' ').trim();
    if(!txt) continue;
    var rest = txt.replace(RE_PROPER,' ').replace(RE_RANGE,' ').replace(RE_XREF,' ');
    if(/[0-9]/.test(rest)) out.stray.push(rest.trim().slice(0,200));
    else out.xref++;
  }
  return out;
}

function buildSelfCheck(){
  var miss = REG.filter(function(r){return !r.ok;});
  var audit = strayAudit();
  var stray = audit.stray;
  var lits = document.querySelectorAll('#doc .lit');

  var s = document.getElementById('sc-summary');
  var okA = miss.length===0, okB = stray.length===0;
  s.innerHTML =
    '<div class="scroll"><table><thead><tr><th>Category</th><th class="num">Count</th>'+
    '<th>What it is</th></tr></thead><tbody>'+
    '<tr><td><b>Bound numerals</b></td><td class="num">'+REG.length+'</td>'+
    '<td>Rendered from a key in one of the two embedded blocks. Every numeric claim '+
    'in this document is one of these.</td></tr>'+
    '<tr><td><b>Declared literals</b></td><td class="num">'+lits.length+'</td>'+
    '<td>Definitions rather than results &mdash; band edges, age bounds, calendar '+
    'years, illustrative arithmetic. Each carries its reason.</td></tr>'+
    '<tr><td><b>Structural / identifier</b></td><td class="num">'+audit.structural+'</td>'+
    '<td>Inside a code span, a heading, a column label or a figure caption: names and '+
    'identifiers, never results.</td></tr>'+
    '<tr><td><b>Cross-references</b></td><td class="num">'+audit.xref+'</td>'+
    '<td>&ldquo;section 12&rdquo;, &ldquo;blocks 2 to 5&rdquo;, a &ldquo;13&ndash;18&rdquo; '+
    'range: navigation within this document.</td></tr>'+
    '<tr><td><b>Unclassified</b></td><td class="num">'+stray.length+'</td>'+
    '<td>Anything else. Must be zero.</td></tr>'+
    '</tbody></table></div>'+
    '<p>The numbers file offers <b>'+Object.keys(NOR.entries).length+'</b> entries in total.</p>'+
    '<p>Check A &mdash; every bound numeral resolves to an existing key: '+
    (okA?'<span class="sc-ok">PASS</span>':'<span class="sc-bad">FAIL &mdash; '+miss.length+' missing</span>')+
    '<br>Check B &mdash; no unclassified numeral anywhere in the prose: '+
    (okB?'<span class="sc-ok">PASS</span>':'<span class="sc-bad">FAIL &mdash; '+stray.length+' unclassified</span>')+'</p>';

  if(miss.length){
    var mh = '<h4>Missing keys</h4><ul>';
    miss.forEach(function(r){ mh += '<li><code>'+esc(r.src)+':'+esc(r.key)+'</code></li>'; });
    document.getElementById('sc-missing').innerHTML = mh+'</ul>';
  }
  if(stray.length){
    var sh = '<h4>Unclassified numerals in prose</h4><ul>';
    stray.forEach(function(t){ sh += '<li><code>'+esc(t)+'</code></li>'; });
    document.getElementById('sc-stray').innerHTML = sh+'</ul>';
  }

  // the numeral -> key register
  var seen = {}, rows = '';
  REG.forEach(function(r){
    var id = r.src+':'+r.key;
    if(seen[id]) { seen[id].c += 1; return; }
    seen[id] = {r:r, c:1};
  });
  var keys = Object.keys(seen).sort();
  keys.forEach(function(id){
    var e = seen[id], r = e.r;
    rows += '<tr><td><code>'+esc(r.key)+'</code></td><td>'+esc(r.src)+'</td>'+
            '<td class="num">'+e.c+'</td><td>'+esc(r.txt)+'</td>'+
            '<td>'+esc(r.art)+'</td><td>'+esc(r.ref)+'</td></tr>';
  });
  document.getElementById('sc-register').innerHTML =
    '<div class="scroll"><table><thead><tr><th>key</th><th>block</th>'+
    '<th class="num">uses</th><th>first rendering</th><th>frozen artefact</th>'+
    '<th>what it is</th></tr></thead><tbody>'+rows+'</tbody></table></div>';

  // declared literals
  var lrows = '', lseen = {};
  for(var i=0;i<lits.length;i++){
    var t = lits[i].textContent, why = lits[i].getAttribute('data-why')||'';
    var k = t+'|'+why;
    if(lseen[k]){ lseen[k].c++; continue; }
    lseen[k] = {t:t, why:why, c:1};
  }
  Object.keys(lseen).sort().forEach(function(k){
    var e = lseen[k];
    lrows += '<tr><td>'+esc(e.t)+'</td><td class="num">'+e.c+'</td><td>'+esc(e.why)+'</td></tr>';
  });
  document.getElementById('sc-literals').innerHTML =
    '<div class="scroll"><table><thead><tr><th>literal</th><th class="num">uses</th>'+
    '<th>why it is not a result</th></tr></thead><tbody>'+lrows+'</tbody></table></div>';

  // unused keys
  var used = {}; REG.forEach(function(r){ if(r.src==='nor') used[r.key]=1; });
  var unused = Object.keys(NOR.entries).filter(function(k){return !used[k];}).sort();
  document.getElementById('sc-unused').innerHTML =
    '<p><b>'+unused.length+'</b> of the numbers file&rsquo;s '+
    Object.keys(NOR.entries).length+' entries are not cited in this document '+
    '(mostly the male-reference and equivalized mirrors of cited raw quantities, '+
    'and the per-state welfare grid). They are listed so the coverage gap is visible '+
    'rather than implicit.</p><p class="mono" style="font-size:11.5px;color:#5a5f66">'+
    unused.map(esc).join(' · ')+'</p>';
}

// -- table of contents ------------------------------------------------------ #
function tocSpy(){
  var links = [].slice.call(document.querySelectorAll('#toc a[data-sec]'));
  var secs = links.map(function(a){ return document.getElementById(a.getAttribute('data-sec')); });
  function upd(){
    var best = 0, y = window.scrollY + 130;
    for(var i=0;i<secs.length;i++){ if(secs[i] && secs[i].offsetTop <= y) best = i; }
    links.forEach(function(a,i){ a.className = (i===best)?'on':''; });
  }
  window.addEventListener('scroll', upd, {passive:true});
  upd();
}

render();
buildSelfCheck();
tocSpy();
})();
"""


def page(title: str, toc_html: str, body_html: str, nor_json: str, aux_json: str) -> str:
    return (
        "<!doctype html>\n"
        '<html lang="en"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>" + title + "</title>\n"
        "<style>" + CSS + "</style>\n"
        "</head><body>\n"
        '<div id="wrap">\n'
        '<nav id="toc">' + toc_html + "</nav>\n"
        '<main id="doc">' + body_html + "</main>\n"
        "</div>\n"
        '<script id="NOR-DATA" type="application/json">' + nor_json + "</script>\n"
        '<script id="AUX-DATA" type="application/json">' + aux_json + "</script>\n"
        "<script>" + JS + "</script>\n"
        "</body></html>\n"
    )
