import type { Settings } from './types';

const KEY = { settings: 'me106.settings.v1', progress: 'me106.progress.v1', bookmarks: 'me106.bookmarks.v1' };

function read<T>(k: string, fallback: T): T {
  try {
    const v = localStorage.getItem(k);
    return v ? (JSON.parse(v) as T) : fallback;
  } catch {
    return fallback;
  }
}
function write(k: string, v: unknown) {
  try {
    localStorage.setItem(k, JSON.stringify(v));
  } catch {
    /* storage unavailable: fail quietly */
  }
}

export const DEFAULT_SETTINGS: Settings = {
  count: 20, shops: [], categories: [], difficulty: 'mixed', source: 'both', qtype: 'all',
  mode: 'practice', pool: 'all', shuffleQuestions: true, shuffleOptions: true, timer: 'off', secondsPerQuestion: 45,
};
export const loadSettings = (): Settings => ({ ...DEFAULT_SETTINGS, ...read<Partial<Settings>>(KEY.settings, {}) });
export const saveSettings = (s: Settings) => write(KEY.settings, s);

export interface QStat { seen: number; correct: number; lastCorrect: boolean }
export type Progress = Record<string, QStat>;
export const loadProgress = (): Progress => read<Progress>(KEY.progress, {});
export function recordAnswer(id: string, correct: boolean) {
  const p = loadProgress();
  const s = p[id] ?? { seen: 0, correct: 0, lastCorrect: false };
  s.seen += 1;
  if (correct) s.correct += 1;
  s.lastCorrect = correct;
  p[id] = s;
  write(KEY.progress, p);
}
export const resetProgress = () => write(KEY.progress, {});

export const loadBookmarks = (): string[] => read<string[]>(KEY.bookmarks, []);
export function toggleBookmark(id: string): string[] {
  const b = new Set(loadBookmarks());
  if (b.has(id)) b.delete(id); else b.add(id);
  const arr = [...b];
  write(KEY.bookmarks, arr);
  return arr;
}
