import { useCallback, useEffect, useRef, useState } from 'react';
import { categoryName, shopName } from '../data';
import { loadBookmarks, recordAnswer, toggleBookmark } from '../storage';
import type { Answer, RunItem, Settings } from '../types';
import { Figure } from './Figure';

const LETTERS = ['A', 'B', 'C', 'D'];

export function Quiz({ items, settings, onFinish, onQuit }: {
  items: RunItem[]; settings: Settings;
  onFinish: (answers: Answer[], totalMs: number) => void; onQuit: () => void;
}) {
  const [i, setI] = useState(0);
  const [answers, setAnswers] = useState<Answer[]>(() => items.map(() => ({ chosen: null, correct: false, timeMs: 0 })));
  const [revealed, setRevealed] = useState(false);       // practice: answered current
  const [showLabels, setShowLabels] = useState(false);
  const [bookmarks, setBookmarks] = useState(loadBookmarks);
  const [toast, setToast] = useState('');
  const started = useRef(Date.now());
  const qStart = useRef(Date.now());
  const total = settings.timer === 'total' ? items.length * settings.secondsPerQuestion : 0;
  const [left, setLeft] = useState(settings.timer === 'per-question' ? settings.secondsPerQuestion : total);
  const item = items[i];
  const practice = settings.mode === 'practice';
  const a = answers[i];

  const finish = useCallback((ans: Answer[]) => {
    if (!practice) ans.forEach((x, k) => recordAnswer(items[k].q.id, x.correct));
    onFinish(ans, Date.now() - started.current);
  }, [items, onFinish, practice]);

  const next = useCallback(() => {
    const ans = answers.slice();
    ans[i] = { ...ans[i], timeMs: ans[i].timeMs + (Date.now() - qStart.current) };
    setAnswers(ans);
    if (i + 1 >= items.length) { finish(ans); return; }
    setI(i + 1); setRevealed(false); setShowLabels(false); qStart.current = Date.now();
    if (settings.timer === 'per-question') setLeft(settings.secondsPerQuestion);
  }, [answers, i, items.length, finish, settings.timer, settings.secondsPerQuestion]);

  const choose = useCallback((k: number) => {
    if (practice && revealed) return;
    const correct = k === item.answer;
    const ans = answers.slice();
    ans[i] = { ...ans[i], chosen: k, correct };
    setAnswers(ans);
    if (practice) { setRevealed(true); recordAnswer(item.q.id, correct); }
  }, [answers, i, item, practice, revealed]);

  // timer (test mode)
  useEffect(() => {
    if (practice || settings.timer === 'off') return;
    const t = setInterval(() => setLeft((v) => v - 1), 1000);
    return () => clearInterval(t);
  }, [practice, settings.timer, i]);
  useEffect(() => {
    if (practice || settings.timer === 'off' || left > 0) return;
    if (settings.timer === 'per-question') next(); else finish(answers);
  }, [left]); // eslint-disable-line react-hooks/exhaustive-deps

  const bm = bookmarks.includes(item.q.id);
  const doBookmark = useCallback(() => setBookmarks(toggleBookmark(item.q.id)), [item]);
  const report = async () => {
    const text = `ME-106 quiz issue — ${item.q.id}\n${item.q.question}\nOptions: ${item.q.options.join(' | ')}\nKeyed answer: ${item.q.options[item.q.answer]}\nProblem: `;
    try { await navigator.clipboard.writeText(text); setToast('Copied question ID and text — paste it into a message to report the issue.'); }
    catch { setToast(`Could not copy automatically. Question ID: ${item.q.id}`); }
    setTimeout(() => setToast(''), 3500);
  };
  const quit = () => { if (window.confirm('Quit this quiz? Your answers so far will be lost.')) onQuit(); };

  // keyboard shortcuts: 1–4 or A–D answer, Enter next, Shift+B bookmark (plain B is option B)
  useEffect(() => {
    const h = (e: KeyboardEvent) => {
      const tag = (e.target as HTMLElement)?.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA' || e.metaKey || e.ctrlKey || e.altKey) return;
      const k = e.key.toLowerCase();
      if (k === 'enter') {
        if (practice ? revealed : a.chosen !== null) { e.preventDefault(); next(); }
        return;
      }
      if (e.shiftKey && k === 'b') { doBookmark(); return; }
      const idx = '1234'.indexOf(k) >= 0 ? '1234'.indexOf(k) : 'abcd'.indexOf(k);
      if (k.length === 1 && idx >= 0 && idx < item.order.length) choose(idx);
    };
    window.addEventListener('keydown', h);
    return () => window.removeEventListener('keydown', h);
  }, [item, practice, revealed, a.chosen, next, choose, doBookmark]);

  const optClass = (k: number) => {
    if (practice && revealed) {
      if (k === item.answer) return 'opt correct';
      if (k === a.chosen) return 'opt wrong';
      return 'opt dim';
    }
    return a.chosen === k ? 'opt chosen' : 'opt';
  };
  const lines = item.q.question.split('\n');

  return (
    <main className="page quiz">
      <div className="quiz-top">
        <div className="progress" role="progressbar" aria-valuemin={0} aria-valuemax={items.length} aria-valuenow={i + 1}>
          <div style={{ width: `${((i + (revealed || a.chosen !== null ? 1 : 0)) / items.length) * 100}%` }} />
        </div>
        <div className="meta">
          <span className="count">Q {i + 1} / {items.length}</span>
          <span className="badge">{shopName(item.q.shop)}</span>
          <span className="badge soft">{categoryName(item.q.category)}</span>
          <span className={`pill ${item.q.difficulty}`}>{item.q.difficulty}</span>
          {!practice && settings.timer !== 'off' && <span className={`timer ${left <= 10 ? 'low' : ''}`}>⏱ {Math.floor(Math.max(left, 0) / 60)}:{String(Math.max(left, 0) % 60).padStart(2, '0')}</span>}
        </div>
      </div>

      {item.q.figure && <Figure id={item.q.figure} showLabels={showLabels} />}

      <h2 className="qtext">{lines.map((l, k) => <span key={k}>{l}{k < lines.length - 1 && <br />}</span>)}</h2>

      <div className="options" role="group" aria-label="Answer options">
        {item.order.map((orig, k) => (
          <button key={k} className={optClass(k)} onClick={() => choose(k)} disabled={practice && revealed}
            aria-pressed={a.chosen === k}>
            <span className="key">{LETTERS[k]}</span>
            <span className="otext">{item.q.options[orig]}</span>
            {practice && revealed && k === item.answer && <span className="mark" aria-label="correct answer">✓</span>}
            {practice && revealed && k === a.chosen && k !== item.answer && <span className="mark" aria-label="your answer, wrong">✗</span>}
          </button>
        ))}
      </div>

      {practice && revealed && (
        <div className={`feedback ${a.correct ? 'ok' : 'bad'}`} aria-live="polite">
          <p className="verdict">{a.correct ? '✓ Correct' : `✗ Not quite — the answer is ${LETTERS[item.answer]}.`}</p>
          <p>{item.q.explanation}</p>
          <p className="ref">{item.q.source === 'lab' ? 'Lab source' : 'Theory'}: {item.q.ref} · {item.q.id}</p>
          {item.q.figure && <button className="linkish" onClick={() => setShowLabels((v) => !v)}>{showLabels ? 'Hide' : 'Reveal all'} figure labels</button>}
        </div>
      )}

      <div className="quiz-actions">
        <button className="ghost" onClick={quit}>Quit</button>
        <button className={`ghost ${bm ? 'on' : ''}`} onClick={doBookmark} aria-pressed={bm} title="Bookmark (B)">{bm ? '★' : '☆'} Bookmark</button>
        <button className="ghost" onClick={report}>Report issue</button>
        <button className="primary" onClick={next} disabled={practice ? !revealed : a.chosen === null}>
          {i + 1 >= items.length ? 'Finish' : 'Next'} →
        </button>
      </div>
      <p className="hint">Keys: 1–4 or A–D to answer · Enter for next · Shift+B to bookmark</p>
      {toast && <div className="toast" role="status">{toast}</div>}
    </main>
  );
}
