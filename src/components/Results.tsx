import { useState } from 'react';
import { categoryName, shopName } from '../data';
import type { Answer, RunItem } from '../types';
import { Figure } from './Figure';

const LETTERS = ['A', 'B', 'C', 'D'];

function Breakdown({ title, rows }: { title: string; rows: { key: string; name: string; ok: number; n: number }[] }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <table className="bd">
        <tbody>
          {rows.map((r) => {
            const pct = Math.round((100 * r.ok) / r.n);
            return (
              <tr key={r.key} className={pct < 60 ? 'weak' : ''}>
                <td>{r.name}</td>
                <td className="num">{r.ok}/{r.n}</td>
                <td className="barcell"><div className="bar"><div style={{ width: `${pct}%` }} /></div></td>
                <td className="num">{pct}%{pct < 60 ? ' ⚠' : ''}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <p className="hint">⚠ = weak area (below 60%)</p>
    </div>
  );
}

function group(items: RunItem[], answers: Answer[], key: (it: RunItem) => string, name: (k: string) => string) {
  const m = new Map<string, { ok: number; n: number }>();
  items.forEach((it, i) => {
    const k = key(it);
    const v = m.get(k) ?? { ok: 0, n: 0 };
    v.n += 1; if (answers[i].correct) v.ok += 1;
    m.set(k, v);
  });
  return [...m.entries()].map(([k, v]) => ({ key: k, name: name(k), ...v })).sort((a, b) => a.ok / a.n - b.ok / b.n);
}

export function Results({ items, answers, totalMs, onRetryWrong, onSame, onSetup }: {
  items: RunItem[]; answers: Answer[]; totalMs: number;
  onRetryWrong: () => void; onSame: () => void; onSetup: () => void;
}) {
  const [wrongOnly, setWrongOnly] = useState(false);
  const ok = answers.filter((a) => a.correct).length;
  const pct = Math.round((100 * ok) / items.length);
  const mins = Math.floor(totalMs / 60000), secs = Math.round((totalMs % 60000) / 1000);
  const wrongCount = items.length - ok;
  return (
    <main className="page results">
      <section className="card score">
        <div className="big-score">{ok} / {items.length}</div>
        <div className="pct">{pct}%</div>
        <div className="time">Time: {mins} min {secs} s</div>
        <div className="row-btns">
          <button className="primary" onClick={onRetryWrong} disabled={!wrongCount}>Retry wrong ones ({wrongCount})</button>
          <button onClick={onSame}>New quiz, same settings</button>
          <button className="ghost" onClick={onSetup}>Back to setup</button>
        </div>
      </section>
      <div className="grid2">
        <Breakdown title="By shop" rows={group(items, answers, (it) => it.q.shop, shopName)} />
        <Breakdown title="By category" rows={group(items, answers, (it) => it.q.category, categoryName)} />
      </div>
      <section className="card">
        <div className="review-head">
          <h3>Review</h3>
          <label><input type="checkbox" checked={wrongOnly} onChange={(e) => setWrongOnly(e.target.checked)} /> Wrong only</label>
        </div>
        <ol className="review">
          {items.map((it, i) => {
            const a = answers[i];
            if (wrongOnly && a.correct) return null;
            return (
              <li key={it.q.id} className={a.correct ? 'ok' : 'bad'}>
                <p className="rq"><span className="badge">{shopName(it.q.shop)}</span> {it.q.question}</p>
                {it.q.figure && <Figure id={it.q.figure} showLabels />}
                <p>Your answer: <b>{a.chosen === null ? '— (not answered)' : `${LETTERS[a.chosen]}. ${it.q.options[it.order[a.chosen]]}`}</b> {a.correct ? '✓' : '✗'}</p>
                {!a.correct && <p>Correct: <b>{LETTERS[it.answer]}. {it.q.options[it.q.answer]}</b></p>}
                <p className="expl">{it.q.explanation}</p>
                <p className="ref">{it.q.ref} · {it.q.id}</p>
              </li>
            );
          })}
        </ol>
      </section>
    </main>
  );
}
