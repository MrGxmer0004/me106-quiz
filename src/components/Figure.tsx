import { useEffect, useState } from 'react';

import { FIGBYID } from '../data';

const cache = new Map<string, string>();

async function loadSvg(id: string): Promise<string> {
  if (cache.has(id)) return cache.get(id)!;
  const res = await fetch(`${import.meta.env.BASE_URL}figures/${id}.svg`);
  const txt = await res.text();
  cache.set(id, txt);
  return txt;
}

export function useSvg(id: string | undefined) {
  const [svg, setSvg] = useState<string>(id && cache.get(id) || '');
  useEffect(() => {
    let alive = true;
    if (!id) return;
    loadSvg(id).then((t) => alive && setSvg(t)).catch(() => alive && setSvg(''));
    return () => { alive = false; };
  }, [id]);
  return svg;
}

/** Inline SVG (so strokes follow the theme via currentColor). Tap to open the zoom view. */
export function Figure({ id, showLabels, alt }: { id: string; showLabels?: boolean; alt?: string }) {
  const svg = useSvg(id);
  const [zoom, setZoom] = useState(false);
  const [scale, setScale] = useState(1);
  const entry = FIGBYID[id];
  useEffect(() => {
    if (!zoom) return;
    const h = (e: KeyboardEvent) => { if (e.key === 'Escape') setZoom(false); };
    window.addEventListener('keydown', h);
    return () => window.removeEventListener('keydown', h);
  }, [zoom]);
  const labels = entry ? Object.entries(entry.labels) : [];
  return (
    <div className="figure">
      <button className="figure-frame" onClick={() => { setScale(1); setZoom(true); }} aria-label={`${alt ?? 'Figure'} — tap to zoom`}>
        <div className="svg-host" role="img" aria-label={alt ?? 'Figure'} dangerouslySetInnerHTML={{ __html: svg }} />
        <span className="zoom-hint" aria-hidden="true">⤢ tap to zoom</span>
      </button>
      {showLabels && labels.length > 0 && (
        <ul className="legend">
          {labels.map(([k, v]) => (
            <li key={k}><span className="tag">{k}</span> <b>{v.part}</b> — {v.function}</li>
          ))}
        </ul>
      )}
      {zoom && (
        <div className="zoom-overlay" role="dialog" aria-modal="true" aria-label="Zoomed figure" onClick={() => setZoom(false)}>
          <div className="zoom-bar" onClick={(e) => e.stopPropagation()}>
            <button onClick={() => setScale((s) => Math.max(1, s - 0.5))} aria-label="Zoom out">−</button>
            <span>{Math.round(scale * 100)}%</span>
            <button onClick={() => setScale((s) => Math.min(4, s + 0.5))} aria-label="Zoom in">+</button>
            <button onClick={() => setZoom(false)} aria-label="Close zoom">✕</button>
          </div>
          <div className="zoom-scroll" onClick={(e) => e.stopPropagation()}>
            <div className="svg-host zoomed" style={{ width: `${scale * 100}%` }} dangerouslySetInnerHTML={{ __html: svg }} />
          </div>
        </div>
      )}
    </div>
  );
}
