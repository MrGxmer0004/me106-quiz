import { useMemo, useState } from 'react';
import { CATEGORIES, ESSENTIALS, QUESTIONS, SHOPS } from '../data';
import { filterQuestions } from '../quiz';
import { loadBookmarks, loadProgress } from '../storage';
import type { Settings, Shop } from '../types';

const PRESETS = [10, 20, 30, 50, 100];

function Seg<T extends string>({ value, options, onChange, label }: { value: T; options: [T, string][]; onChange: (v: T) => void; label: string }) {
  return (
    <div className="seg" role="radiogroup" aria-label={label}>
      {options.map(([v, l]) => (
        <button key={v} role="radio" aria-checked={value === v} className={value === v ? 'on' : ''} onClick={() => onChange(v)}>{l}</button>
      ))}
    </div>
  );
}

export function Setup({ settings, onChange, onStart }: { settings: Settings; onChange: (s: Settings) => void; onStart: () => void }) {
  const [showCats, setShowCats] = useState(settings.categories.length > 0);
  const [custom, setCustom] = useState(typeof settings.count === 'number' && !PRESETS.includes(settings.count) ? String(settings.count) : '');
  const s = settings;
  const set = (p: Partial<Settings>) => onChange({ ...s, ...p });
  const available = useMemo(() => filterQuestions(QUESTIONS, s, loadProgress(), loadBookmarks()).length, [s]);
  const willRun = s.count === 'all' ? available : Math.min(s.count, available);

  const toggleShop = (id: Shop) => {
    const cur = new Set(s.shops);
    if (cur.has(id)) cur.delete(id); else cur.add(id);
    set({ shops: cur.size === SHOPS.length ? [] : [...cur] });
  };
  const toggleCat = (id: string) => {
    const cur = new Set(s.categories);
    if (cur.has(id)) cur.delete(id); else cur.add(id);
    set({ categories: cur.size === CATEGORIES.length ? [] : [...cur] });
  };

  return (
    <main className="page setup">
      <section className="card">
        <h2>Question set</h2>
        <Seg label="Question set" value={s.set} onChange={(v) => set({ set: v })} options={[['full', `Full bank (${QUESTIONS.length})`], ['essentials', `Essentials (${ESSENTIALS.size})`]]} />
        <p className="hint">{s.set === 'essentials'
          ? 'Essentials: 10–24 simple MCQs per shop on the practical basics — machine parts, tools, materials, the lab job, procedure and precautions. No numericals or hard questions.'
          : 'Full bank: every question, with filters for category, difficulty, source and type.'}</p>
      </section>
      <section className="card">
        <h2>Number of questions</h2>
        <div className="chips">
          {PRESETS.map((n) => (
            <button key={n} className={`chip ${s.count === n ? 'on' : ''}`} aria-pressed={s.count === n} onClick={() => { setCustom(''); set({ count: n }); }}>{n}</button>
          ))}
          <button className={`chip ${s.count === 'all' ? 'on' : ''}`} aria-pressed={s.count === 'all'} onClick={() => { setCustom(''); set({ count: 'all' }); }}>All matching</button>
          <label className="custom">
            <span className="sr">Custom number</span>
            <input inputMode="numeric" placeholder="Custom" value={custom}
              onChange={(e) => { const v = e.target.value.replace(/\D/g, ''); setCustom(v); if (v) set({ count: Math.max(1, parseInt(v, 10)) }); }} />
          </label>
        </div>
        <p className="avail" aria-live="polite"><b>{available}</b> questions match these filters{available ? <> · this quiz will have <b>{willRun}</b></> : null}</p>
      </section>

      <section className="card">
        <h2>Shops</h2>
        <div className="chips">
          <button className={`chip ${s.shops.length === 0 ? 'on' : ''}`} aria-pressed={s.shops.length === 0} onClick={() => set({ shops: [] })}>All</button>
          {SHOPS.map((sh) => (
            <button key={sh.id} className={`chip ${s.shops.includes(sh.id) ? 'on' : ''}`} aria-pressed={s.shops.includes(sh.id)} onClick={() => toggleShop(sh.id)}>{sh.name}</button>
          ))}
        </div>
        {s.set === 'full' && <button className="linkish" aria-expanded={showCats} onClick={() => setShowCats((v) => !v)}>
          {showCats ? '▾' : '▸'} Categories {s.categories.length ? `(${s.categories.length} selected)` : '(all)'}
        </button>}
        {s.set === 'full' && showCats && (
          <div className="chips small">
            <button className={`chip ${s.categories.length === 0 ? 'on' : ''}`} aria-pressed={s.categories.length === 0} onClick={() => set({ categories: [] })}>All</button>
            {CATEGORIES.map((c) => (
              <button key={c.id} className={`chip ${s.categories.includes(c.id) ? 'on' : ''}`} aria-pressed={s.categories.includes(c.id)} onClick={() => toggleCat(c.id)}>{c.name}</button>
            ))}
          </div>
        )}
      </section>

      <section className="card grid2">
        {s.set === 'full' && <>
        <div><h3>Difficulty</h3><Seg label="Difficulty" value={s.difficulty} onChange={(v) => set({ difficulty: v })} options={[['mixed', 'Mixed'], ['easy', 'Easy'], ['medium', 'Medium'], ['hard', 'Hard']]} /></div>
        <div><h3>Source</h3><Seg label="Source" value={s.source} onChange={(v) => set({ source: v })} options={[['both', 'Both'], ['lab', 'Lab-specific'], ['theory', 'Theory']]} /></div>
        <div><h3>Question type</h3><Seg label="Question type" value={s.qtype} onChange={(v) => set({ qtype: v })} options={[['all', 'All'], ['diagram', 'Diagram only'], ['nodiagram', 'No diagrams'], ['numerical', 'Numericals']]} /></div>
        </>}
        <div><h3>Pool</h3><Seg label="Pool" value={s.pool} onChange={(v) => set({ pool: v })} options={[['all', 'All'], ['unseen', 'Unseen'], ['wrong', 'Previously wrong'], ['bookmarked', 'Bookmarked']]} /></div>
      </section>

      <section className="card">
        <h3>Mode</h3>
        <Seg label="Mode" value={s.mode} onChange={(v) => set({ mode: v })} options={[['practice', 'Practice — instant feedback'], ['test', 'Test — feedback at the end']]} />
        {s.mode === 'test' && (
          <div className="timer-row">
            <h3>Timer</h3>
            <Seg label="Timer" value={s.timer} onChange={(v) => set({ timer: v })} options={[['off', 'Off'], ['per-question', 'Per question'], ['total', 'Total']]} />
            {s.timer !== 'off' && (
              <label className="inline">
                <input type="number" min={10} max={300} value={s.secondsPerQuestion} onChange={(e) => set({ secondsPerQuestion: Math.max(10, Math.min(300, Number(e.target.value) || 45)) })} />
                <span>seconds per question{s.timer === 'total' ? ` (total ${Math.ceil((willRun * s.secondsPerQuestion) / 60)} min)` : ''}</span>
              </label>
            )}
          </div>
        )}
        <div className="toggles">
          <label><input type="checkbox" checked={s.shuffleQuestions} onChange={(e) => set({ shuffleQuestions: e.target.checked })} /> Shuffle questions</label>
          <label><input type="checkbox" checked={s.shuffleOptions} onChange={(e) => set({ shuffleOptions: e.target.checked })} /> Shuffle options</label>
        </div>
      </section>

      <div className="start-bar">
        <button className="primary big" disabled={!available} onClick={onStart}>Start {willRun ? `(${willRun})` : ''}</button>
      </div>
    </main>
  );
}
