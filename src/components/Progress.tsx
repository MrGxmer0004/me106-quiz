import { useState } from 'react';
import { QUESTIONS, SHOPS } from '../data';
import { loadBookmarks, loadProgress, resetProgress } from '../storage';

export function ProgressPage() {
  const [p, setP] = useState(loadProgress);
  const bm = loadBookmarks().length;
  const rows = SHOPS.map((s) => {
    const qs = QUESTIONS.filter((q) => q.shop === s.id);
    let attempted = 0, seen = 0, correct = 0, wrong = 0;
    for (const q of qs) {
      const st = p[q.id];
      if (!st) continue;
      attempted += 1; seen += st.seen; correct += st.correct;
      if (!st.lastCorrect) wrong += 1;
    }
    return { ...s, total: qs.length, attempted, never: qs.length - attempted, acc: seen ? Math.round((100 * correct) / seen) : null, wrong };
  });
  const reset = () => {
    if (window.confirm('Reset all progress? This clears seen/correct history on this device. Bookmarks are kept.')) { resetProgress(); setP({}); }
  };
  return (
    <main className="page">
      <section className="card">
        <h2>Your progress</h2>
        <p className="hint">Stored only in this browser. {bm} bookmarked question{bm === 1 ? '' : 's'}.</p>
        <table className="prog">
          <thead><tr><th>Shop</th><th className="num">Attempted</th><th className="num">Accuracy</th><th className="num">Never seen</th><th className="num">Last wrong</th></tr></thead>
          <tbody>
            {rows.map((r) => (
              <tr key={r.id}>
                <td>{r.name}</td>
                <td className="num">{r.attempted}/{r.total}</td>
                <td className="num">{r.acc === null ? '—' : `${r.acc}%`}</td>
                <td className="num">{r.never}</td>
                <td className="num">{r.wrong}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <button className="danger" onClick={reset}>Reset progress</button>
      </section>
    </main>
  );
}
