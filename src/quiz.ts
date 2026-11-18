import type { Question, RunItem, Settings } from './types';
import type { Progress } from './storage';

export function shuffle<T>(a: T[]): T[] {
  const r = a.slice();
  for (let i = r.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [r[i], r[j]] = [r[j], r[i]];
  }
  return r;
}

export function filterQuestions(all: Question[], s: Settings, progress: Progress, bookmarks: string[]): Question[] {
  const bm = new Set(bookmarks);
  return all.filter((q) => {
    if (s.shops.length && !s.shops.includes(q.shop)) return false;
    if (s.categories.length && !s.categories.includes(q.category)) return false;
    if (s.difficulty !== 'mixed' && q.difficulty !== s.difficulty) return false;
    if (s.source !== 'both' && q.source !== s.source) return false;
    if (s.qtype === 'diagram' && !q.figure) return false;
    if (s.qtype === 'nodiagram' && q.figure) return false;
    if (s.qtype === 'numerical' && q.type !== 'numerical' && q.category !== 'numericals') return false;
    const st = progress[q.id];
    if (s.pool === 'unseen' && st && st.seen > 0) return false;
    if (s.pool === 'wrong' && !(st && !st.lastCorrect)) return false;
    if (s.pool === 'bookmarked' && !bm.has(q.id)) return false;
    return true;
  });
}

export function prepare(qs: Question[], s: Settings): RunItem[] {
  const list = s.shuffleQuestions ? shuffle(qs) : qs.slice();
  const n = s.count === 'all' ? list.length : Math.min(s.count, list.length);
  return list.slice(0, n).map((q) => {
    const idx = q.options.map((_, i) => i);
    const order = s.shuffleOptions && !q.keepOrder ? shuffle(idx) : idx;
    return { q, order, answer: order.indexOf(q.answer) };
  });
}
