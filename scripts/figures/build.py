"""Build figures: python3 scripts/figures/build.py [shop ...]

Writes public/figures/<shop>/<name>.svg, merges entries into src/data/figures.json,
and renders PNG previews to .render/ (gitignored) for visual checking.
"""
import importlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from figlib import ROOT  # noqa

SHOPS = ['lathe', 'milling', 'grinding', 'shaping', 'fitting', 'electroplating', 'unconventional', 'safety']
REG = os.path.join(ROOT, 'src', 'data', 'figures.json')


def main(shops):
    reg = json.load(open(REG, encoding='utf-8')) if os.path.exists(REG) else []
    present = [sh for sh in shops if os.path.exists(os.path.join(HERE, 'fig_' + sh + '.py'))]
    reg = [e for e in reg if e['shop'] not in present]
    for shop in shops:
        try:
            mod = importlib.import_module('fig_' + shop)
        except ModuleNotFoundError:
            print('skip (no figure module):', shop)
            continue
        for fn in mod.FIGS:
            figs = fn()
            for f in (figs if isinstance(figs, list) else [figs]):
                reg.append(f.save())
                svgp = os.path.join(ROOT, 'public', 'figures', f.id + '.svg')
                png = os.path.join(ROOT, '.render', f.id + '.png')
                os.makedirs(os.path.dirname(png), exist_ok=True)
                subprocess.run(['rsvg-convert', '-b', 'white', '-w', '900', svgp, '-o', png], check=True)
                print('built', f.id, len(f.labels), 'labels')
    reg.sort(key=lambda e: (SHOPS.index(e['shop']), e['id']))
    json.dump(reg, open(REG, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main(sys.argv[1:] or SHOPS)
