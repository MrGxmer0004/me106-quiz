#!/usr/bin/env node
// ME-106 question bank validator. Run: npm run validate  (add --quiet for errors + summary only)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const QDIR = path.join(ROOT, 'src/data/questions');
const KDIR = path.join(ROOT, 'knowledge');
const FIGREG = path.join(ROOT, 'src/data/figures.json');
const QUIET = process.argv.includes('--quiet');

const SHOPS = ['lathe', 'milling', 'fitting', 'electroplating', 'shaping', 'grinding', 'unconventional', 'safety'];
const PREFIX = { lathe: 'LAT', milling: 'MIL', fitting: 'FIT', electroplating: 'ELP', shaping: 'SHP', grinding: 'GRD', unconventional: 'UCM', safety: 'SAF' };
const KFILE = { lathe: 'lathe.md', milling: 'milling.md', fitting: 'fitting.md', electroplating: 'electroplating.md', shaping: 'shaping.md', grinding: 'grinding.md', unconventional: 'unconventional.md', safety: 'general-safety.md' };
const CATS = ['machine-parts', 'tools-equipment', 'job-dimensions', 'procedure', 'precautions', 'workpiece-material', 'tool-material', 'operations', 'principle-theory', 'numericals', 'gears-indexing', 'wheel-specification', 'process-parameters', 'advantages-limitations', 'applications', 'definitions', 'safety-general', 'measurement-reading'];
const TYPES = ['mcq', 'true-false', 'numerical', 'sequence', 'assertion-reason', 'diagram'];
const DIFFS = ['easy', 'medium', 'hard'];
const REQUIRED = ['id', 'shop', 'category', 'difficulty', 'type', 'question', 'options', 'answer', 'explanation', 'source', 'ref', 'tags', 'facts'];

const errors = [];
const warns = [];
const err = (id, m) => errors.push(`${id}: ${m}`);
const warn = (id, m) => warns.push(`${id}: ${m}`);

// ---------- knowledge facts ----------
const facts = {};
for (const fn of fs.readdirSync(KDIR)) {
  if (!fn.endsWith('.md') || fn === 'coverage-report.md') continue;
  for (const line of fs.readFileSync(path.join(KDIR, fn), 'utf8').split('\n')) {
    const m = line.trim().match(/^- \[([A-Z]{3}-F\d{3})\] (.*)$/);
    if (!m) continue;
    const br = [...m[2].matchAll(/\[([^\[\]]+)\]/g)].map((x) => x[1]);
    const src = br.length ? br[br.length - 1] : '';
    const lab = src.split(';').map((t) => t.trim()).filter(Boolean).some((t) => !t.toLowerCase().startsWith('theory'));
    if (facts[m[1]]) err(m[1], `duplicate fact ID in ${fn}`);
    facts[m[1]] = { file: fn, lab, text: m[2] };
  }
}

// ---------- figures ----------
const figs = fs.existsSync(FIGREG) ? JSON.parse(fs.readFileSync(FIGREG, 'utf8')) : [];
const figById = Object.fromEntries(figs.map((f) => [f.id, f]));
for (const f of figs) {
  const svgp = path.join(ROOT, 'public/figures', f.id + '.svg');
  if (!fs.existsSync(svgp)) { err(f.id, 'figure SVG missing'); continue; }
  const svg = fs.readFileSync(svgp, 'utf8');
  const tags = new Set([...svg.matchAll(/fill="#ffffff">([A-Z])<\/text>/g)].map((m) => m[1]));
  for (const L of Object.keys(f.labels || {})) {
    if (!tags.has(L)) err(f.id, `label ${L} in registry but not drawn on figure`);
    if (!facts[f.labels[L].fact]) err(f.id, `label ${L} cites unknown fact ${f.labels[L].fact}`);
  }
  for (const L of tags) if (!(f.labels || {})[L]) err(f.id, `letter ${L} drawn but missing from registry`);
  if (/<image|data:image/.test(svg)) err(f.id, 'figure embeds a raster image (must be original vector drawing)');
}

// ---------- questions ----------
const all = [];
const ids = new Set();
for (const shop of SHOPS) {
  const p = path.join(QDIR, shop + '.json');
  if (!fs.existsSync(p)) { warn(shop, 'no question file yet'); continue; }
  let arr;
  try { arr = JSON.parse(fs.readFileSync(p, 'utf8')); } catch (e) { err(shop, 'invalid JSON: ' + e.message); continue; }
  for (const q of arr) {
    const id = q.id || '(no id)';
    for (const k of REQUIRED) if (q[k] === undefined || q[k] === null || q[k] === '') err(id, `missing field ${k}`);
    if (ids.has(id)) err(id, 'duplicate question ID'); ids.add(id);
    if (!id.startsWith(PREFIX[shop] + '-')) err(id, `ID prefix should be ${PREFIX[shop]}`);
    if (q.shop !== shop) err(id, `shop "${q.shop}" but in ${shop}.json`);
    if (!CATS.includes(q.category)) err(id, `bad category ${q.category}`);
    if (!TYPES.includes(q.type)) err(id, `bad type ${q.type}`);
    if (!DIFFS.includes(q.difficulty)) err(id, `bad difficulty ${q.difficulty}`);
    if (!['lab', 'theory'].includes(q.source)) err(id, `bad source ${q.source}`);
    const o = q.options || [];
    if (!Array.isArray(o) || o.length < 2 || o.length > 4) err(id, `needs 2–4 options (has ${o.length})`);
    if (new Set(o.map((x) => String(x).trim().toLowerCase())).size !== o.length) err(id, 'duplicate options');
    if (o.some((x) => typeof x !== 'string' || !x.trim())) err(id, 'empty or non-string option');
    if (!Number.isInteger(q.answer) || q.answer < 0 || q.answer >= o.length) err(id, `answer index ${q.answer} invalid`);
    if (!q.explanation || q.explanation.trim().length < 10) err(id, 'explanation empty/too short');
    if (o.some((x) => /\b(all|none) of the (above|these)\b/i.test(x))) err(id, '"all/none of the above" option');
    if (q.type === 'true-false' && JSON.stringify(o) !== '["True","False"]') err(id, 'true-false options must be ["True","False"]');
    if (['true-false', 'sequence', 'assertion-reason'].includes(q.type) && q.type !== 'sequence' && !q.keepOrder) err(id, `${q.type} must have keepOrder`);
    if (!Array.isArray(q.facts) || !q.facts.length) err(id, 'no facts cited');
    for (const f of q.facts || []) if (!facts[f]) err(id, `unknown fact ${f}`);
    if (q.source === 'lab' && !(q.facts || []).some((f) => facts[f]?.lab)) err(id, 'source=lab but cites only theory facts');
    if (q.source === 'theory' && (q.facts || []).some((f) => facts[f]?.lab)) warn(id, 'source=theory but cites a lab fact');
    if (q.figure) {
      const F = figById[q.figure];
      if (!F) err(id, `figure ${q.figure} not in registry`);
      else {
        if (q.label && !F.labels[q.label]) err(id, `label ${q.label} not in ${q.figure}`);
        if (q.label && q.ask === 'part' && o[q.answer] !== F.labels[q.label].part) err(id, `answer "${o[q.answer]}" ≠ registry part "${F.labels[q.label].part}" for ${q.label}`);
        if (q.label && q.ask === 'which' && o[q.answer] !== q.label) err(id, `answer should be letter ${q.label}`);
        if (q.label && q.ask === 'function' && o[q.answer] !== F.labels[q.label].function) err(id, `answer ≠ registry function for ${q.label}`);
      }
      if (q.type !== 'diagram' && q.type !== 'numerical' && q.type !== 'true-false') warn(id, `has figure but type ${q.type}`);
    } else if (q.type === 'diagram') err(id, 'type diagram but no figure');
    if (/(roll no|roll number|signature of)/i.test(q.question + q.explanation)) warn(id, 'mentions personal-data words');
    all.push(q);
  }
}

// ---------- near-duplicates (token Jaccard on normalised question text) ----------
const norm = (s) => s.toLowerCase().replace(/[^a-z0-9ø°.\s]/g, ' ').split(/\s+/).filter((w) => w.length > 2);
const toks = all.map((q) => new Set(norm(q.question + ' || ' + q.options[q.answer])));
const dups = [];
for (let i = 0; i < all.length; i++) {
  for (let j = i + 1; j < all.length; j++) {
    if (all[i].figure && all[j].figure) continue; // label questions share templates across figures
    const a = toks[i], b = toks[j];
    let inter = 0; for (const t of a) if (b.has(t)) inter++;
    const jac = inter / (a.size + b.size - inter || 1);
    if (jac > 0.85) dups.push(`${all[i].id} ~ ${all[j].id} (${jac.toFixed(2)})`);
  }
}
// exact duplicate question text + same answer
const seen = new Map();
for (const q of all) {
  const k = (q.figure || '') + '|' + q.question.trim().toLowerCase() + '|' + q.options[q.answer];
  if (seen.has(k)) err(q.id, `exact duplicate of ${seen.get(k)}`); else seen.set(k, q.id);
}

// ---------- reports ----------
const pad = (s, n) => String(s).padEnd(n);
const lpad = (s, n) => String(s).padStart(n);
function table(rows, cols, get, title) {
  console.log('\n' + title);
  const w = Math.max(...rows.map((r) => r.length), 10) + 1;
  console.log(pad('', w) + cols.map((c) => lpad(c.slice(0, 6), 7)).join('') + lpad('total', 7));
  for (const r of rows) {
    const vals = cols.map((c) => get(r, c));
    console.log(pad(r, w) + vals.map((v) => lpad(v || '.', 7)).join('') + lpad(vals.reduce((a, b) => a + b, 0), 7));
  }
}
const count = (f) => all.filter(f).length;
const shopsPresent = SHOPS.filter((s) => all.some((q) => q.shop === s));

if (!QUIET) {
  console.log(`Questions: ${all.length}  |  facts: ${Object.keys(facts).length}  |  figures: ${figs.length}`);
  const catAbbr = CATS;
  console.log('\nShop × category (columns in order):');
  CATS.forEach((c, i) => console.log(`  c${String(i + 1).padStart(2, '0')} = ${c}`));
  table(shopsPresent, CATS.map((c, i) => 'c' + String(i + 1).padStart(2, '0')), (s, c) => count((q) => q.shop === s && q.category === CATS[+c.slice(1) - 1]), 'Counts:');
  table(shopsPresent, TYPES, (s, t) => count((q) => q.shop === s && q.type === t), 'Shop × type:');
  table(shopsPresent, ['figure'], (s) => count((q) => q.shop === s && q.figure), 'Questions using a figure:');
  table(shopsPresent, DIFFS, (s, d) => count((q) => q.shop === s && q.difficulty === d), 'Shop × difficulty:');
  table(shopsPresent, ['lab', 'theory'], (s, d) => count((q) => q.shop === s && q.source === d), 'Shop × source:');
  // answer positions (only shuffle-able questions)
  const pos = [0, 0, 0, 0];
  for (const q of all) if (!q.keepOrder && q.options.length === 4) pos[q.answer]++;
  console.log('\nCorrect-answer position (4-option, unshuffled data): A=%d B=%d C=%d D=%d', ...pos);
  const tfShare = count((q) => q.type === 'true-false') / (all.length || 1);
  console.log(`True/False share: ${(100 * tfShare).toFixed(1)}%`);
  // procedure/tools/precautions share
  console.log('\nProfessor-flagged categories share per shop (procedure / tools / precautions):');
  for (const s of shopsPresent) {
    const n = count((q) => q.shop === s);
    const f = (c) => ((100 * count((q) => q.shop === s && q.category === c)) / n).toFixed(0) + '%';
    console.log(`  ${pad(s, 15)} ${f('procedure')} / ${f('tools-equipment')} / ${f('precautions')}`);
  }
}
if (all.some((q) => q.difficulty)) {
  const n = all.length || 1;
  console.log(`\nDifficulty mix: easy ${(100 * count((q) => q.difficulty === 'easy') / n).toFixed(0)}% / medium ${(100 * count((q) => q.difficulty === 'medium') / n).toFixed(0)}% / hard ${(100 * count((q) => q.difficulty === 'hard') / n).toFixed(0)}%`);
}

// ---------- fact coverage ----------
const used = new Set(all.flatMap((q) => q.facts || []));
const shopsWithQs = new Set(all.map((q) => q.shop));
const kfShops = Object.fromEntries(Object.entries(KFILE).map(([s, f]) => [f, s]));
const uncoveredLab = [], uncoveredTheory = [];
for (const [fid, f] of Object.entries(facts)) {
  if (!shopsWithQs.has(kfShops[f.file])) continue; // only check shops that have questions
  if (!used.has(fid)) (f.lab ? uncoveredLab : uncoveredTheory).push(fid);
}
console.log(`\nFact coverage: ${used.size} facts cited. Uncovered LAB facts: ${uncoveredLab.length}. Uncovered theory facts: ${uncoveredTheory.length}.`);
if (uncoveredLab.length) { console.log('  Uncovered lab facts: ' + uncoveredLab.join(', ')); uncoveredLab.forEach((f) => err(f, 'lab fact has no question')); }
if (uncoveredTheory.length) console.log('  Uncovered theory facts: ' + uncoveredTheory.join(', '));
if (dups.length) { console.log(`\nPossible near-duplicates (${dups.length}) — review:`); dups.slice(0, 80).forEach((d) => console.log('  ' + d)); }
if (warns.length && !QUIET) { console.log(`\nWarnings (${warns.length}):`); warns.slice(0, 60).forEach((w) => console.log('  ' + w)); }
if (errors.length) {
  console.log(`\n✗ ${errors.length} error(s):`); errors.slice(0, 200).forEach((e) => console.log('  ' + e));
  process.exit(1);
}
console.log('\n✓ Validation passed.');
