export type Shop = 'lathe' | 'milling' | 'fitting' | 'electroplating' | 'shaping' | 'grinding' | 'unconventional' | 'safety';
export type Difficulty = 'easy' | 'medium' | 'hard';
export type QType = 'mcq' | 'true-false' | 'numerical' | 'sequence' | 'assertion-reason' | 'diagram';

export interface Question {
  id: string;
  shop: Shop;
  category: string;
  difficulty: Difficulty;
  type: QType;
  question: string;
  options: string[];
  answer: number;
  explanation: string;
  source: 'lab' | 'theory';
  ref: string;
  tags: string[];
  facts: string[];
  figure?: string;
  label?: string;
  keepOrder?: boolean;
}

export interface FigureLabel { part: string; function: string; fact: string }
export interface FigureEntry { id: string; shop: Shop; title: string; alt: string; labels: Record<string, FigureLabel> }

export type Mode = 'practice' | 'test';
export type Pool = 'all' | 'unseen' | 'wrong' | 'bookmarked';
export type TypeFilter = 'all' | 'diagram' | 'nodiagram' | 'numerical';
export type SourceFilter = 'both' | 'lab' | 'theory';
export type DiffFilter = 'mixed' | Difficulty;

export type QSet = 'full' | 'essentials';

export interface Settings {
  set: QSet;
  count: number | 'all';
  shops: Shop[];          // empty = all
  categories: string[];   // empty = all
  difficulty: DiffFilter;
  source: SourceFilter;
  qtype: TypeFilter;
  mode: Mode;
  pool: Pool;
  shuffleQuestions: boolean;
  shuffleOptions: boolean;
  timer: 'off' | 'per-question' | 'total';
  secondsPerQuestion: number;
}

/** A question prepared for one quiz run: options in display order, answer remapped. */
export interface RunItem {
  q: Question;
  order: number[];        // order[i] = original option index shown at position i
  answer: number;         // display index of correct option
}

export interface Answer { chosen: number | null; correct: boolean; timeMs: number }
