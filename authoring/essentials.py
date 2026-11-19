"""Pick the 'Essentials' set: ~10-20 simple single-answer MCQs per shop covering the practical basics.

Rules: easy/medium only; types mcq or diagram (label naming); no true/false, assertion-reason,
sequence or numerical questions; one question per fact; spread over categories by quota.
Manual overrides (FORCE / EXCLUDE) keep the set sensible. Writes src/data/essentials.json.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QDIR = os.path.join(ROOT, 'src', 'data', 'questions')

# per-shop category quotas (order = priority)
Q = {
 'lathe': {'machine-parts': 9, 'tools-equipment': 3, 'operations': 4, 'workpiece-material': 1, 'tool-material': 1, 'job-dimensions': 1, 'procedure': 2, 'precautions': 2},
 'milling': {'machine-parts': 4, 'operations': 4, 'tools-equipment': 3, 'gears-indexing': 4, 'workpiece-material': 1, 'job-dimensions': 1, 'procedure': 1, 'precautions': 2},
 'grinding': {'machine-parts': 4, 'wheel-specification': 5, 'definitions': 3, 'tools-equipment': 1, 'principle-theory': 1, 'procedure': 2, 'precautions': 2},
 'fitting': {'tools-equipment': 9, 'measurement-reading': 2, 'definitions': 2, 'workpiece-material': 1, 'procedure': 2, 'precautions': 2},
 'shaping': {'machine-parts': 5, 'principle-theory': 2, 'tools-equipment': 2, 'tool-material': 1, 'job-dimensions': 1, 'procedure': 2, 'precautions': 2},
 'electroplating': {'principle-theory': 4, 'machine-parts': 2, 'tools-equipment': 2, 'workpiece-material': 1, 'process-parameters': 2, 'procedure': 2, 'precautions': 2},
 'unconventional': {'principle-theory': 4, 'machine-parts': 4, 'process-parameters': 3, 'tool-material': 1, 'job-dimensions': 1, 'procedure': 2, 'precautions': 2, 'advantages-limitations': 1},
 'safety': {'safety-general': 10},
}
EXCLUDE_WORDS = ['NOT ', 'Practice:', 'Which of these is NOT']   # keep it straightforward
# Manual review (by question-text prefix, or (figure, label) for label questions) — IDs shift when banks regenerate.
FORCE = [
 'Which part holds the cutting tool rigidly', 'Which part moves the lathe tool at right angles', 'Which lathe part has a base graduated in degrees',
 'The lead screw of a lathe is used for', 'The included angle of a metric', 'What is the overall length of the finished ME-106 lathe job',
 'Thread cutting on a lathe produces', 'The operation of bevelling the sharp end', 'Which of these is a function of the tailstock',
 'Which part of a column-and-knee milling machine moves up and down', 'Cutters on a horizontal milling machine are mounted',
 'In milling, indexing means', 'What diametral pitch is used for the ME-106 gear', 'What is the outside (blank) diameter of the ME-106 gear',
 'Which index plate is used for the ME-106 22-tooth gear',
 'Dressing a grinding wheel means', 'Glazing of a grinding wheel is', 'For grinding a HARD workpiece', 'In grinding wheel marking, the letter A stands for',
 'The point angle of a dot punch', 'The least count of a metric outside micrometer', 'How many main types of fit', 'Which part of a file fits into',
 'In the ME-106 shaper wall chart, the crank turns', 'What is the function of the clapper box on a shaper', 'What is the finished LENGTH of the ME-106 shaping block',
 'In the ME-106 lab, which plating is done FIRST', 'What voltage and time are used for nickel plating', 'Copper plating is used to',
 'Which assist gas is normally used for laser cutting mild steel', 'Which assist gas is used for clean, oxide-free', 'What job is cut on the wire EDM',
 'What job is cut on the fiber laser', 'Why is a dry run done before laser cutting',
]
EXCLUDE = [
 'On which side of the lathe bed is the headstock', 'The most commonly used general-purpose lathe', 'Turning on a lathe removes excess material',
 'Which cutter is used to machine dovetail grooves', ('milling/horizontal-mill', 'A'), 'Specific energy in machining means',
 'For copper, the electroplating lecture gives', 'If the spark gap in EDM is too large',
]


def matches(q, rules):
    for r in rules:
        if isinstance(r, tuple):
            if q.get('figure') == r[0] and q.get('label') == r[1] and q.get('ask') == 'part':
                return True
        elif q['question'].startswith(r):
            return True
    return False


def ok(q):
    if q['difficulty'] not in ('easy', 'medium') or q['type'] not in ('mcq', 'diagram'):
        return False
    if any(w in q['question'] for w in EXCLUDE_WORDS):
        return False
    if q.get('figure') and (q.get('ask') not in ('part',) or 'reading' in q['figure'] or 'vernier-' in q['figure'] or 'micrometer-' in q['figure']):
        return False   # diagram questions only as simple "what is label X"
    return not matches(q, EXCLUDE)


def pick(shop):
    qs = json.load(open(os.path.join(QDIR, shop + '.json')))
    used_facts, chosen, figs = set(), [], {}
    for q in qs:
        if matches(q, FORCE) and q['difficulty'] != 'hard' and q['type'] in ('mcq', 'diagram'):
            chosen.append(q); used_facts.update(q['facts'])
    for cat, n in Q[shop].items():
        cands = [q for q in qs if q['category'] == cat and ok(q) and q not in chosen]
        cands.sort(key=lambda q: (q['source'] != 'lab', q['difficulty'] != 'easy', bool(q.get('figure')), q['id']))
        got = sum(1 for q in chosen if q['category'] == cat)
        for q in cands:
            if got >= n:
                break
            if used_facts & set(q['facts']):
                continue
            f = q.get('figure')
            if f and figs.get(f, 0) >= 3:          # at most 3 label questions per figure
                continue
            chosen.append(q); used_facts.update(q['facts']); got += 1
            if f:
                figs[f] = figs.get(f, 0) + 1
    missing = [r for r in FORCE if isinstance(r, str) and any(q['question'].startswith(r) for q in qs) is False]
    order = [q['id'] for q in qs]
    return sorted((q['id'] for q in chosen), key=order.index)


if __name__ == '__main__':
    out = {shop: pick(shop) for shop in Q}
    allq = [q for f in os.listdir(QDIR) for q in json.load(open(os.path.join(QDIR, f)))]
    for r in FORCE:
        if not any(q['question'].startswith(r) for q in allq):
            raise SystemExit('FORCE rule matched nothing: ' + r)
    byid = {q['id']: q for q in allq}
    out['_check'] = {i: byid[i]['question'][:60] for k, v in list(out.items()) if k != '_check' for i in v}
    json.dump(out, open(os.path.join(ROOT, 'src', 'data', 'essentials.json'), 'w'), indent=1)
    print({k: len(v) for k, v in out.items() if k != '_check'}, 'total', len(out['_check']))
