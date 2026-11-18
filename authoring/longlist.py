import json, sys
shop = sys.argv[1]
Q = json.load(open(f'src/data/questions/{shop}.json'))
for q in Q:
    if q.get('keepOrder') or len(q['options']) < 3 or q.get('figure'): continue
    L = [len(o) for o in q['options']]; c = L[q['answer']]; m = max(L[i] for i in range(len(L)) if i != q['answer'])
    if c > 1.3 * m and c - m > 8:
        print('Q:', q['question']); print('  C:', q['options'][q['answer']]); print('  W:', ' | '.join(o for i, o in enumerate(q['options']) if i != q['answer']))
