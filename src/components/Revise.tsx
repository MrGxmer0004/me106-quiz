import { useMemo, useState } from 'react';
import { FIGURES, SHOPS } from '../data';
import type { Shop } from '../types';
import { Figure } from './Figure';

const notes = import.meta.glob('../../knowledge/*.md', { eager: true, query: '?raw', import: 'default' }) as Record<string, string>;
const FILE: Record<Shop, string> = {
  lathe: 'lathe', milling: 'milling', fitting: 'fitting', electroplating: 'electroplating', shaping: 'shaping',
  grinding: 'grinding', unconventional: 'unconventional', safety: 'general-safety',
};

/** Strip fact IDs, source tags and authoring-only sections. */
function clean(md: string): string {
  const out: string[] = [];
  let skip = false;
  for (const raw of md.split('\n')) {
    if (/^##\s+Figures needed/i.test(raw)) { skip = true; continue; }
    if (/^##\s/.test(raw)) skip = false;
    if (skip) continue;
    if (/^Source keys:/i.test(raw)) continue;
    let l = raw.replace(/\[[A-Z]{3}-F\d{3}\]\s*/g, '');
    l = l.replace(/\s*\[[^\[\]]*(?:p\.|s\.|theory|LS|NB|CLLS|BOARD|LEC|HO|MLS|TA|GPPT|CG|GL|GP|GR|SH|PPT|EP|ELS|UCM|CHART|TOOLS)[^\[\]]*\]/g, '');
    l = l.replace(/\s*\((?:corrects notebook[^)]*|see corrections[^)]*|board's[^)]*)\)/gi, '');
    out.push(l);
  }
  return out.join('\n');
}

function inline(t: string) {
  const parts = t.split(/(\*\*[^*]+\*\*|`[^`]+`)/g);
  return parts.map((p, i) => (p.startsWith('**') ? <b key={i}>{p.slice(2, -2)}</b> : p.startsWith('`') ? <code key={i}>{p.slice(1, -1)}</code> : p));
}

function Markdown({ text }: { text: string }) {
  const blocks: JSX.Element[] = [];
  let list: string[] = [];
  const flush = () => {
    if (list.length) { blocks.push(<ul key={blocks.length}>{list.map((x, i) => <li key={i}>{inline(x)}</li>)}</ul>); list = []; }
  };
  for (const line of text.split('\n')) {
    const m = line.match(/^(#{1,4})\s+(.*)$/);
    if (m) { flush(); const lvl = Math.min(4, m[1].length + 1); const H = `h${lvl}` as 'h2'; blocks.push(<H key={blocks.length}>{inline(m[2])}</H>); continue; }
    if (/^\s*-\s+/.test(line)) { list.push(line.replace(/^\s*-\s+/, '')); continue; }
    if (!line.trim()) { flush(); continue; }
    flush(); blocks.push(<p key={blocks.length}>{inline(line)}</p>);
  }
  flush();
  return <div className="md">{blocks}</div>;
}

export function Revise() {
  const [shop, setShop] = useState<Shop>('lathe');
  const [tab, setTab] = useState<'notes' | 'figures'>('notes');
  const md = useMemo(() => {
    const key = Object.keys(notes).find((k) => k.endsWith(`/${FILE[shop]}.md`));
    return key ? clean(notes[key]) : '';
  }, [shop]);
  // show one example of each generated reading series; the rest are quiz-only
  const figs = FIGURES.filter((f) => f.shop === shop && !/(vernier|micrometer)-(0[2-9]|[1-9]\d)$/.test(f.id));
  return (
    <main className="page revise">
      <div className="tabs" role="tablist" aria-label="Shop">
        {SHOPS.map((s) => (
          <button key={s.id} role="tab" aria-selected={shop === s.id} className={shop === s.id ? 'on' : ''} onClick={() => setShop(s.id)}>{s.name}</button>
        ))}
      </div>
      <div className="seg" role="tablist" aria-label="View">
        <button role="tab" aria-selected={tab === 'notes'} className={tab === 'notes' ? 'on' : ''} onClick={() => setTab('notes')}>Notes</button>
        <button role="tab" aria-selected={tab === 'figures'} className={tab === 'figures' ? 'on' : ''} onClick={() => setTab('figures')}>Figures ({figs.length})</button>
      </div>
      {tab === 'notes' ? (
        <section className="card"><Markdown text={md} /></section>
      ) : (
        <section className="gallery">
          {figs.length === 0 && <p className="hint">No figures for this shop.</p>}
          {figs.map((f) => (
            <figure key={f.id} className="card">
              <figcaption><b>{f.title}</b></figcaption>
              <Figure id={f.id} showLabels alt={f.alt} />
            </figure>
          ))}
        </section>
      )}
    </main>
  );
}
