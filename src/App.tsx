import { useEffect, useState } from 'react';
import { QUESTIONS } from './data';
import { filterQuestions, prepare } from './quiz';
import { loadBookmarks, loadProgress, loadSettings, saveSettings } from './storage';
import type { Answer, RunItem, Settings } from './types';
import { Setup } from './components/Setup';
import { Quiz } from './components/Quiz';
import { Results } from './components/Results';
import { ProgressPage } from './components/Progress';
import { Revise } from './components/Revise';

type View = 'setup' | 'quiz' | 'results' | 'progress' | 'revise';

function viewFromHash(): View {
  const h = window.location.hash.replace('#/', '');
  return h === 'progress' || h === 'revise' ? h : 'setup';
}

export default function App() {
  const [view, setView] = useState<View>(viewFromHash);
  const [settings, setSettings] = useState<Settings>(loadSettings);
  const [items, setItems] = useState<RunItem[]>([]);
  const [answers, setAnswers] = useState<Answer[]>([]);
  const [totalMs, setTotalMs] = useState(0);
  const [runKey, setRunKey] = useState(0);

  useEffect(() => {
    const h = () => { const v = viewFromHash(); if (view !== 'quiz' && view !== 'results') setView(v); else if (v !== 'setup') setView(v); };
    window.addEventListener('hashchange', h);
    return () => window.removeEventListener('hashchange', h);
  }, [view]);
  useEffect(() => { window.scrollTo(0, 0); }, [view, runKey]);

  const go = (v: View) => { setView(v); window.location.hash = v === 'setup' || v === 'quiz' || v === 'results' ? '#/' : `#/${v}`; };
  const update = (s: Settings) => { setSettings(s); saveSettings(s); };
  const start = (list = filterQuestions(QUESTIONS, settings, loadProgress(), loadBookmarks()), s = settings) => {
    const run = prepare(list, s);
    if (!run.length) return;
    setItems(run); setRunKey((k) => k + 1); go('quiz');
  };

  return (
    <div className="app">
      <header className="topbar">
        <button className="brand" onClick={() => { if (view !== 'quiz' || window.confirm('Leave this quiz? Your answers so far will be lost.')) go('setup'); }}>
          <span className="logo" aria-hidden="true">⚙</span> ME-106 Workshop Quiz
        </button>
        <nav aria-label="Main">
          <button className={view === 'setup' ? 'on' : ''} onClick={() => { if (view !== 'quiz' || window.confirm('Leave this quiz?')) go('setup'); }}>Quiz</button>
          <button className={view === 'revise' ? 'on' : ''} onClick={() => { if (view !== 'quiz' || window.confirm('Leave this quiz?')) go('revise'); }}>Revise</button>
          <button className={view === 'progress' ? 'on' : ''} onClick={() => { if (view !== 'quiz' || window.confirm('Leave this quiz?')) go('progress'); }}>Progress</button>
        </nav>
      </header>

      {view === 'setup' && <Setup settings={settings} onChange={update} onStart={() => start()} />}
      {view === 'quiz' && (
        <Quiz key={runKey} items={items} settings={settings}
          onFinish={(a, ms) => { setAnswers(a); setTotalMs(ms); go('results'); }}
          onQuit={() => go('setup')} />
      )}
      {view === 'results' && (
        <Results items={items} answers={answers} totalMs={totalMs}
          onRetryWrong={() => start(items.filter((_, i) => !answers[i].correct).map((it) => it.q), { ...settings, count: 'all' })}
          onSame={() => start()}
          onSetup={() => go('setup')} />
      )}
      {view === 'progress' && <ProgressPage />}
      {view === 'revise' && <Revise />}

      <footer className="foot">Built for ME-106 practice. Questions may contain errors — report via the button.</footer>
    </div>
  );
}
