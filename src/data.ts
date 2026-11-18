import type { Question, FigureEntry, Shop } from './types';
import figuresJson from './data/figures.json';

const modules = import.meta.glob('./data/questions/*.json', { eager: true, import: 'default' }) as Record<string, Question[]>;

export const SHOPS: { id: Shop; name: string }[] = [
  { id: 'lathe', name: 'Lathe' },
  { id: 'milling', name: 'Milling' },
  { id: 'fitting', name: 'Fitting' },
  { id: 'electroplating', name: 'Electroplating' },
  { id: 'shaping', name: 'Shaping' },
  { id: 'grinding', name: 'Grinding' },
  { id: 'unconventional', name: 'Unconventional' },
  { id: 'safety', name: 'Safety' },
];
export const shopName = (s: string) => SHOPS.find((x) => x.id === s)?.name ?? s;

export const CATEGORIES: { id: string; name: string }[] = [
  { id: 'machine-parts', name: 'Machine parts' },
  { id: 'tools-equipment', name: 'Tools & equipment' },
  { id: 'job-dimensions', name: 'Job dimensions' },
  { id: 'procedure', name: 'Procedure' },
  { id: 'precautions', name: 'Precautions' },
  { id: 'workpiece-material', name: 'Workpiece material' },
  { id: 'tool-material', name: 'Tool material' },
  { id: 'operations', name: 'Operations' },
  { id: 'principle-theory', name: 'Principle & theory' },
  { id: 'numericals', name: 'Numericals' },
  { id: 'gears-indexing', name: 'Gears & indexing' },
  { id: 'wheel-specification', name: 'Wheel specification' },
  { id: 'process-parameters', name: 'Process parameters' },
  { id: 'advantages-limitations', name: 'Advantages & limitations' },
  { id: 'applications', name: 'Applications' },
  { id: 'definitions', name: 'Definitions' },
  { id: 'safety-general', name: 'General safety' },
  { id: 'measurement-reading', name: 'Measurement & reading' },
];
export const categoryName = (c: string) => CATEGORIES.find((x) => x.id === c)?.name ?? c;

const order = SHOPS.map((s) => s.id);
export const QUESTIONS: Question[] = Object.values(modules)
  .flat()
  .sort((a, b) => order.indexOf(a.shop) - order.indexOf(b.shop) || a.id.localeCompare(b.id));
export const QBYID: Record<string, Question> = Object.fromEntries(QUESTIONS.map((q) => [q.id, q]));
export const FIGURES = figuresJson as FigureEntry[];
export const FIGBYID: Record<string, FigureEntry> = Object.fromEntries(FIGURES.map((f) => [f.id, f]));
