"""Authoring helper for the ME-106 question bank.

Each shop has an authoring script (authoring/<shop>.py) that builds questions with this
library and writes src/data/questions/<shop>.json. In authoring, the correct option is
always written FIRST; the library then places it at a balanced, deterministic position
(unless the options must keep their order). `source` and `ref` are derived from the
cited fact IDs, so they always agree with the knowledge base.

The JSON files are the canonical data the website and validator use. Small edits can be
made directly in the JSON (then run `npm run validate`); re-running an authoring script
regenerates that shop's JSON from scratch.
"""
import json, os, random, re, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KDIR = os.path.join(ROOT, 'knowledge')
QDIR = os.path.join(ROOT, 'src', 'data', 'questions')
FIGREG = os.path.join(ROOT, 'src', 'data', 'figures.json')

PREFIX = {'lathe': 'LAT', 'milling': 'MIL', 'fitting': 'FIT', 'electroplating': 'ELP',
          'shaping': 'SHP', 'grinding': 'GRD', 'unconventional': 'UCM', 'safety': 'SAF'}
KFILE = {'lathe': 'lathe.md', 'milling': 'milling.md', 'fitting': 'fitting.md',
         'electroplating': 'electroplating.md', 'shaping': 'shaping.md', 'grinding': 'grinding.md',
         'unconventional': 'unconventional.md', 'safety': 'general-safety.md'}

CAT = {'parts': 'machine-parts', 'tools': 'tools-equipment', 'dims': 'job-dimensions',
       'proc': 'procedure', 'prec': 'precautions', 'wmat': 'workpiece-material',
       'tmat': 'tool-material', 'ops': 'operations', 'theory': 'principle-theory',
       'num': 'numericals', 'gear': 'gears-indexing', 'wheel': 'wheel-specification',
       'param': 'process-parameters', 'adv': 'advantages-limitations', 'app': 'applications',
       'def': 'definitions', 'safety': 'safety-general', 'meas': 'measurement-reading'}
DIFF = {'e': 'easy', 'm': 'medium', 'h': 'hard'}
TYPE = {'mcq': 'mcq', 'n': 'numerical', 's': 'sequence', 'd': 'diagram', 'tf': 'true-false',
        'ar': 'assertion-reason'}

# Readable names for source keys, per knowledge file
SRCNAME = {
    '*': {'LS': 'Log Sheets ME-106', 'NB': 'Manufacturing notes', 'CLLS': 'Central Lathe Log sheet',
          'MLS1': 'Milling Log Sheet #1', 'MLS2': 'Milling Log Sheet #2', 'TA': 'Milling TA slides',
          'GPPT': 'Grinding PPT', 'PPT': 'Fitting lecture', 'ELS': 'Electroplating Log Sheet',
          'UCM': 'Unconventional log sheet', 'HO': 'Centre Lathe handout', 'CG': 'Cylindrical grinding notes',
          'GL': 'Grinding Lab slides', 'GP': 'Grinding slides', 'GR': 'Grinding ratio board',
          'SH': 'Shaping slides', 'EP': 'Electroplating lecture', 'TOOLS': 'Milling tools photo'},
    'lathe.md': {'BOARD': 'Lathe job blackboard', 'LEC': 'Centre Lathe lecture slide'},
    'milling.md': {'BOARD': 'Milling blackboard', 'LEC': 'Milling lecture slide', 'CHART': 'Milling wall chart'},
    'shaping.md': {'CHART': 'Shaper wall chart'},
    'electroplating.md': {'BOARD': 'Electroplating blackboard'},
}

_FACTS = None
LABKEYS = set(['LS', 'NB', 'CLLS', 'BOARD', 'LEC', 'HO', 'MLS1', 'MLS2', 'CHART', 'TOOLS', 'TA', 'CG', 'GL', 'GP', 'GPPT', 'GR', 'SH', 'PPT', 'EP', 'ELS', 'UCM'])


def load_facts():
    """Return {fact_id: {'text','src','lab','file'}} from all knowledge files."""
    global _FACTS
    if _FACTS is not None:
        return _FACTS
    facts = {}
    for fn in sorted(os.listdir(KDIR)):
        if not fn.endswith('.md') or fn == 'coverage-report.md':
            continue
        for line in open(os.path.join(KDIR, fn), encoding='utf-8'):
            m = re.match(r'^- \[([A-Z]{3}-F\d{3})\] (.*)$', line.strip())
            if not m:
                continue
            fid, rest = m.group(1), m.group(2)
            brackets = re.findall(r'\[([^\[\]]+)\]', rest)
            src = brackets[-1] if brackets else ''
            toks = [t.strip() for t in src.split(';') if t.strip()]
            lab = any(t.split()[0].rstrip(':,') in LABKEYS for t in toks if t.split())
            facts[fid] = {'text': rest, 'src': src, 'toks': toks, 'lab': lab, 'file': fn}
    _FACTS = facts
    return facts


def readable(tok, fn):
    if tok.lower().startswith('theory'):
        return 'Theory: ' + tok.split(':', 1)[1].strip()
    key = tok.split()[0]
    rest = tok[len(key):].strip()
    name = SRCNAME.get(fn, {}).get(key) or SRCNAME['*'].get(key) or key
    if key == 'LEC' and rest.startswith('s.'):
        rest = rest[2:]
    return (name + ' ' + rest).strip()


class Bank:
    def __init__(self, shop):
        self.shop = shop
        self.prefix = PREFIX[shop]
        self.qs = []
        self.facts = load_facts()
        self.rng = random.Random('me106-' + shop)
        self.pos = {}
        self.figs = None
        self.patch = {}
        try:
            import importlib
            self.patch = importlib.import_module('fix_' + shop).PATCH
        except ModuleNotFoundError:
            pass
        self.patched = set()

    # ---------- helpers ----------
    def _facts(self, facts):
        out = []
        for f in (facts.split() if isinstance(facts, str) else facts):
            f = str(f)
            if re.fullmatch(r'\d+', f):
                f = '%s-F%03d' % (self.prefix, int(f))
            elif re.fullmatch(r'[A-Z]{3}\d+', f):
                f = '%s-F%03d' % (f[:3], int(f[3:]))
            if f not in self.facts:
                raise ValueError('Unknown fact %s' % f)
            out.append(f)
        return out

    def _slot(self, n):
        """Balanced deterministic position for the correct answer among n options."""
        st = self.pos.setdefault(n, [])
        if not st:
            st.extend(self.rng.sample(range(n), n))
        return st.pop()

    def _meta(self, facts):
        fl = self._facts(facts)
        lab = any(self.facts[f]['lab'] for f in fl)
        # ref: from first fact (prefer a lab token if lab question)
        refs = []
        for f in fl:
            info = self.facts[f]
            toks = info['toks']
            if lab:
                toks = [t for t in toks if not t.lower().startswith('theory')] or toks
            for t in toks[:1]:
                r = readable(t, info['file'])
                if r not in refs:
                    refs.append(r)
        return fl, ('lab' if lab else 'theory'), '; '.join(refs[:2])

    def _add(self, d):
        d['id'] = '%s-%04d' % (self.prefix, len(self.qs) + 1)  # IDs are sequential after drops
        d['shop'] = self.shop
        self.qs.append(d)
        return d

    # ---------- question builders ----------
    def q(self, cat, diff, question, correct, wrongs, exp, facts, tags=None, type='mcq',
          fig=None, label=None, ask=None, keep=False, answer=None):
        fl, src, ref = self._meta(facts)
        if question in self.patch and isinstance(self.patch[question], dict) and self.patch[question].get('drop'):  # works for keepOrder types too
            self.patched.add(question)
            return None
        if question in self.patch and not keep:
            pt = self.patch[question]
            if isinstance(pt, dict):
                correct = pt.get('c', correct)
                wrongs = pt.get('w', wrongs)
                cat = pt.get('cat', cat)
                diff = pt.get('d', diff)
            else:
                wrongs = pt
            self.patched.add(question)
        if keep:
            opts = [correct] + list(wrongs) if answer is None else list(wrongs)
            ans = 0 if answer is None else answer
        else:
            opts = list(wrongs)
            self.rng.shuffle(opts)
            pos = self._slot(len(opts) + 1)
            opts.insert(pos, correct)
            ans = pos
        d = {'category': CAT.get(cat, cat), 'difficulty': DIFF.get(diff, diff),
             'type': TYPE.get(type, type), 'question': question, 'options': opts,
             'answer': ans, 'explanation': exp, 'source': src, 'ref': ref,
             'tags': tags or [], 'facts': fl}
        if fig:
            d['figure'] = fig
            if d['type'] == 'mcq':
                d['type'] = 'diagram'
        if label:
            d['label'] = label
        if ask:
            d['ask'] = ask
        if keep:
            d['keepOrder'] = True
        return self._add(d)

    def n(self, cat, diff, question, correct, wrongs, exp, facts, **kw):
        return self.q(cat, diff, question, correct, wrongs, exp, facts, type='n', **kw)

    def s(self, cat, diff, question, correct, wrongs, exp, facts, **kw):
        return self.q(cat, diff, question, correct, wrongs, exp, facts, type='s', **kw)

    def tf(self, cat, diff, statement, truth, exp, facts, tags=None, fig=None):
        d = self.q(cat, diff, statement, 'True', ['False'], exp, facts, tags=tags, type='tf',
                   keep=True, answer=0 if truth else 1, fig=fig)
        if d is None:
            return None
        d['options'] = ['True', 'False']
        d['type'] = 'true-false'
        return d

    def ar(self, cat, diff, assertion, reason, code, exp, facts, tags=None):
        opts = ['Both A and R are true, and R is the correct explanation of A',
                'Both A and R are true, but R is NOT the correct explanation of A',
                'A is true, but R is false',
                'A is false, but R is true']
        qtext = 'Assertion (A): %s\nReason (R): %s' % (assertion, reason)
        return self.q(cat, diff, qtext, None, opts, exp, facts, tags=tags, type='ar', keep=True,
                      answer='abcd'.index(code))

    # ---------- figure-driven questions ----------
    def fig(self, fid):
        if self.figs is None:
            self.figs = {f['id']: f for f in json.load(open(FIGREG, encoding='utf-8'))}
        return self.figs[fid]

    def labels(self, fid, kinds='pw', letters=None, cat='parts', diffs=None, tags=None, extra_parts=None, only=None, extra_funcs=None):
        """Generate label questions from the registry.
        kinds: p = 'what is label X', w = 'which label shows Y', f = 'function of label X'."""
        F = self.fig(fid)
        L = F['labels']
        letters = letters or list(L.keys())
        diffs = diffs or {'p': 'e', 'w': 'm', 'f': 'm'}
        tpl = F.get('ask', {})
        allparts = [v['part'] for v in L.values()] + list(extra_parts or [])
        for k in kinds:
            for X in ((only or {}).get(k) or letters):
                lab = L[X]
                part, func, fact = lab['part'], lab['function'], lab['fact']
                if k == 'p':
                    others = [p for p in allparts if p != part]
                    wr = self.rng.sample(others, min(3, len(others)))
                    qt = tpl.get('p', 'In the figure, what is the part labelled {L}?').format(L=X)
                    exp = '%s = %s. %s.' % (X, part, func)
                    self.q(cat, diffs['p'], qt, part, wr, exp, [fact], tags=tags, fig=fid, label=X, ask='part')
                elif k == 'w':
                    others = [x for x in L.keys() if x != X]
                    wr = self.rng.sample(others, min(3, len(others)))
                    qt = tpl.get('w', 'In the figure, which label shows the {P}?').format(P=part[0].lower() + part[1:] if not part[:2].isupper() else part)
                    exp = '%s = %s. %s.' % (X, part, func)
                    self.q(cat, diffs['w'], qt, X, wr, exp, [fact], tags=tags, fig=fid, label=X, ask='which')
                elif k == 'f':
                    others = [v['function'] for kk, v in L.items() if kk != X] + list(extra_funcs or [])
                    wr = self.rng.sample(others, min(3, len(others)))
                    qt = tpl.get('f', 'In the figure, what is the function of the part labelled {L}?').format(L=X)
                    exp = '%s = %s. %s.' % (X, part, func)
                    self.q(cat, diffs['f'], qt, func, wr, exp, [fact], tags=tags, fig=fid, label=X, ask='function')

    # ---------- output ----------
    def save(self):
        unused = set(self.patch) - self.patched
        if unused:
            raise SystemExit('Patch keys not matched: ' + repr(sorted(unused))[:500])
        os.makedirs(QDIR, exist_ok=True)
        out = []
        for d in self.qs:
            # consistency rules (cross-shop review): label look-ups are easy; multi-fact calculations/sequences are hard
            if d.get('ask') in ('part', 'which') and d['difficulty'] == 'medium':
                d['difficulty'] = 'easy'
            if d['type'] in ('numerical', 'sequence') and d['difficulty'] == 'medium' and len(d['facts']) >= 3:
                d['difficulty'] = 'hard'
            o = {k: d[k] for k in ['id', 'shop', 'category', 'difficulty', 'type', 'question', 'options',
                                    'answer', 'explanation', 'source', 'ref', 'tags', 'facts']}
            for k in ['figure', 'label', 'ask', 'keepOrder']:
                if k in d:
                    o[k] = d[k]
            out.append(o)
        p = os.path.join(QDIR, self.shop + '.json')
        json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        nd = sum(1 for o in out if 'figure' in o)
        longq = []
        for o in out:
            if o.get('keepOrder') or len(o['options']) < 3 or 'figure' in o:
                continue
            L = [len(x) for x in o['options']]; c = L[o['answer']]; m = max(L[i] for i in range(len(L)) if i != o['answer'])
            if c > 1.3 * m and c - m > 8:
                longq.append(o['question'][:70])
        if longq:
            print('  WARNING %d questions with clearly-longest correct option:' % len(longq))
            for t in longq[:60]:
                print('    -', t)
        print('%s: %d questions (%d with figures) -> %s' % (self.shop, len(out), nd, os.path.relpath(p, ROOT)))
