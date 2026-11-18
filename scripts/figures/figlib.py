"""Tiny SVG builder for original ME-106 schematic figures.

Strokes and text use currentColor so figures follow light/dark mode when inlined.
Lettered callouts (orange discs with white letters) never reveal part names.
"""
import math, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ACC = '#e8590c'


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


class Fig:
    def __init__(self, fid, w, h, title, alt, ask=None):
        self.id, self.w, self.h, self.title, self.alt = fid, w, h, title, alt
        self.shop = fid.split('/')[0]
        self.uid = re.sub(r'[^a-z0-9]', '', fid.lower())
        self.el, self.top, self.labels = [], [], {}
        self.ask = ask or {}

    # primitives -------------------------------------------------------
    def raw(self, s):
        self.el.append(s)

    def line(self, x1, y1, x2, y2, c='s'):
        self.el.append(f'<line class="{c}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')

    def rect(self, x, y, w, h, c='s', rx=0):
        self.el.append(f'<rect class="{c}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}"/>')

    def circle(self, cx, cy, r, c='s'):
        self.el.append(f'<circle class="{c}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>')

    def poly(self, pts, c='s', closed=True):
        tag = 'polygon' if closed else 'polyline'
        p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        self.el.append(f'<{tag} class="{c}" points="{p}"/>')

    def path(self, d, c='s'):
        self.el.append(f'<path class="{c}" d="{d}"/>')

    def text(self, x, y, s, size=18, anchor='middle', c='tx', weight='normal', rot=None):
        tr = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot is not None else ''
        self.el.append(f'<text class="{c}" x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
                       f'font-weight="{weight}" dominant-baseline="middle"{tr}>{esc(s)}</text>')

    def arc(self, cx, cy, r, a1, a2, c='s'):
        """Arc from angle a1 to a2 (degrees, 0 = +x, counter-clockwise visually = negative y)."""
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
        x2, y2 = cx + r * math.cos(math.radians(a2)), cy - r * math.sin(math.radians(a2))
        large = 1 if abs(a2 - a1) > 180 else 0
        sweep = 0 if a2 > a1 else 1
        self.path(f'M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} {sweep} {x2:.1f},{y2:.1f}', c)

    def arrow(self, x1, y1, x2, y2, c='acc', head=10):
        self.line(x1, y1, x2, y2, c)
        a = math.atan2(y2 - y1, x2 - x1)
        p1 = (x2 - head * math.cos(a - 0.4), y2 - head * math.sin(a - 0.4))
        p2 = (x2 - head * math.cos(a + 0.4), y2 - head * math.sin(a + 0.4))
        fc = 'accf' if c.startswith('acc') else 'k'
        self.poly([(x2, y2), p1, p2], fc)

    def _ah(self, x, y, ang):
        h = 9
        p1 = (x + h * math.cos(ang - 0.35), y + h * math.sin(ang - 0.35))
        p2 = (x + h * math.cos(ang + 0.35), y + h * math.sin(ang + 0.35))
        self.poly([(x, y), p1, p2], 'k')

    def hdim(self, x1, x2, y, label, size=17, above=True):
        """Horizontal dimension line with arrows at both ends."""
        self.line(x1, y, x2, y, 'thin')
        self._ah(x1, y, 0)
        self._ah(x2, y, math.pi)
        self.text((x1 + x2) / 2, y - 12 if above else y + 14, label, size)

    def vdim(self, x, y1, y2, label, size=17, left=True):
        """Vertical dimension line with arrows at both ends; text rotated."""
        self.line(x, y1, x, y2, 'thin')
        self._ah(x, y1, math.pi / 2)
        self._ah(x, y2, -math.pi / 2)
        tx = x - 13 if left else x + 13
        self.text(tx, (y1 + y2) / 2, label, size, rot=-90)

    def hatch(self, x, y, w, h, step=10):
        """Diagonal hatching inside a rectangle (section)."""
        self.el.append(f'<clipPath id="{self.uid}c{len(self.el)}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>')
        cid = f'{self.uid}c{len(self.el) - 1}'
        g = [f'<g clip-path="url(#{cid})">']
        k = -h
        while k < w:
            g.append(f'<line class="thin" x1="{x + k:.1f}" y1="{y + h:.1f}" x2="{x + k + h:.1f}" y2="{y:.1f}"/>')
            k += step
        g.append('</g>')
        self.el.append(''.join(g))

    # callouts ----------------------------------------------------------
    def callout(self, L, tx, ty, lx, ly, part, function, fact, dot=True):
        """Leader line from target (tx,ty) to letter disc at (lx,ly)."""
        d = math.hypot(lx - tx, ly - ty) or 1
        ex, ey = lx - (lx - tx) * 15 / d, ly - (ly - ty) * 15 / d
        self.top.append(f'<line class="lead" x1="{tx:.1f}" y1="{ty:.1f}" x2="{ex:.1f}" y2="{ey:.1f}"/>')
        if dot:
            self.top.append(f'<circle class="k" cx="{tx:.1f}" cy="{ty:.1f}" r="3"/>')
        self.tag(L, lx, ly)
        self.labels[L] = {'part': part, 'function': function, 'fact': fact}

    def tag(self, L, x, y):
        self.top.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="{ACC}"/>'
                        f'<text x="{x:.1f}" y="{y + 1:.1f}" font-size="19" font-weight="700" text-anchor="middle" '
                        f'dominant-baseline="middle" fill="#ffffff">{L}</text>')

    def panel(self, L, x, y, part, function, fact):
        """Letter for a whole panel (identify-the-panel figures)."""
        self.tag(L, x, y)
        self.labels[L] = {'part': part, 'function': function, 'fact': fact}

    # output -------------------------------------------------------------
    def svg(self):
        style = ('.s{fill:none;stroke:currentColor;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}'
                 '.thin{fill:none;stroke:currentColor;stroke-width:1.1}'
                 '.lead{fill:none;stroke:currentColor;stroke-width:1.2;opacity:.85}'
                 '.f{fill:currentColor;fill-opacity:.10;stroke:currentColor;stroke-width:2;stroke-linejoin:round}'
                 '.f2{fill:currentColor;fill-opacity:.22;stroke:currentColor;stroke-width:2;stroke-linejoin:round}'
                 '.k{fill:currentColor;stroke:none}'
                 '.d{fill:none;stroke:currentColor;stroke-width:1.5;stroke-dasharray:6 4}'
                 '.cl{fill:none;stroke:currentColor;stroke-width:1;stroke-dasharray:14 4 3 4;opacity:.7}'
                 f'.acc{{fill:none;stroke:{ACC};stroke-width:2.4;stroke-linecap:round}}'
                 f'.accf{{fill:{ACC};stroke:none}}'
                 f'.acct{{fill:{ACC};stroke:none}}'
                 '.tx{fill:currentColor;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}'
                 'text{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}')
        body = '\n'.join(self.el + self.top)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" role="img" '
                f'aria-label="{esc(self.alt)}"><title>{esc(self.title)}</title><style>{style}</style>\n{body}\n</svg>\n')

    def entry(self):
        e = {'id': self.id, 'shop': self.shop, 'title': self.title, 'alt': self.alt, 'labels': self.labels}
        if self.ask:
            e['ask'] = self.ask
        return e

    def save(self):
        p = os.path.join(ROOT, 'public', 'figures', self.id + '.svg')
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8').write(self.svg())
        # every label letter used must appear as a tag
        return self.entry()
