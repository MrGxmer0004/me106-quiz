import math, random
from figlib import Fig


def _wheel_side(f, cx, cy, r, w=None):
    f.circle(cx, cy, r, 'f2')
    rnd = random.Random(int(cx * 7 + cy))
    for _ in range(int(r * 1.3)):
        a = rnd.uniform(0, 2 * math.pi); rr = rnd.uniform(r * 0.3, r * 0.95)
        f.circle(cx + rr * math.cos(a), cy + rr * math.sin(a), 1.4, 'k')
    f.circle(cx, cy, r * 0.22, 's')


def surface():
    f = Fig('grinding/surface-grinder', 760, 500, 'Surface grinding machine',
            'Front view line diagram of a horizontal-spindle reciprocating-table surface grinder with lettered callouts')
    f.rect(60, 430, 620, 30, 'f')                         # base
    f.rect(500, 60, 120, 370, 'f')                        # column
    f.rect(260, 80, 240, 80, 'f')                         # wheel head
    _wheel_side(f, 330, 203, 55)                          # wheel (touches work top at y=258)
    f.path('M265,203 A65,65 0 0 1 395,203 L395,160 L265,160 Z', 'f')  # guard (top half)
    f.rect(140, 340, 330, 40, 'f')                        # saddle
    f.rect(90, 300, 400, 40, 'f')                         # table
    f.rect(170, 280, 280, 20, 'f2')                       # magnetic chuck
    for x in range(180, 450, 18):
        f.line(x, 280, x, 300, 'thin')
    f.rect(270, 258, 120, 22, 'f')                        # workpiece
    f.circle(110, 395, 22, 's'); f.line(110, 395, 88, 395)    # table traverse handwheel
    f.circle(560, 130, 18, 's')                           # down feed handwheel
    f.arrow(160, 318, 230, 318, 'acc'); f.arrow(230, 318, 160, 318, 'acc')
    C = f.callout
    C('A', 360, 235, 420, 250, 'Grinding wheel', 'Rotating abrasive wheel that removes small amounts of metal', 'GRD-F001')
    C('B', 284, 157, 220, 190, 'Wheel guard', 'Covers the wheel to protect the operator from fragments and sparks', 'GRD-F024')
    C('C', 380, 100, 380, 35, 'Wheel head', 'Carries the wheel spindle and motor; moved down to set the depth of cut', 'GRD-F023')
    C('D', 560, 200, 680, 200, 'Column', 'Vertical member on which the wheel head slides up and down', 'GRD-F024')
    C('E', 430, 290, 470, 245, 'Magnetic chuck', 'Holds steel work on the table by magnetism', 'GRD-F089')
    C('F', 120, 318, 45, 290, 'Table', 'Reciprocates back and forth carrying the chuck and work', 'GRD-F023')
    C('G', 300, 360, 250, 405, 'Saddle', 'Moves the table crosswise (cross feed) on the base', 'GRD-F024')
    C('H', 110, 395, 45, 405, 'Table-traverse handwheel', 'Moves the table longitudinally by hand', 'GRD-F024')
    C('J', 640, 445, 700, 480, 'Base', 'Supports the whole machine', 'GRD-F024')
    C('K', 330, 266, 220, 245, 'Workpiece', 'Flat job being surface ground', 'GRD-F021')
    return f


def cylindrical():
    f = Fig('grinding/cylindrical-grinder', 780, 430, 'Plain cylindrical grinding machine',
            'Line diagram of a cylindrical grinder: work between headstock and tailstock centres on a reciprocating table, wheel behind, with lettered callouts')
    f.rect(50, 360, 680, 40, 'f')                          # base
    f.rect(90, 320, 600, 40, 'f')                          # lower table
    f.rect(120, 290, 540, 30, 'f2')                        # upper table
    f.rect(140, 180, 110, 110, 'f')                        # headstock (work head)
    f.rect(520, 200, 100, 90, 'f')                         # tailstock
    f.poly([(250, 225), (268, 215), (268, 235)], 'f'); f.poly([(520, 225), (502, 215), (502, 235)], 'f')
    f.rect(268, 205, 234, 40, 'f2')                        # workpiece
    f.line(230, 225, 540, 225, 'cl')
    f.rect(300, 40, 200, 70, 'f')                          # wheel head
    _wheel_side(f, 400, 157, 48)                           # wheel touching the work
    for x in (150, 630):
        f.rect(x - 8, 326, 16, 16, 'k')                    # adjustable dogs on the front of the lower table
    f.arrow(300, 340, 380, 340, 'acc'); f.arrow(380, 340, 300, 340, 'acc')
    f.arc(330, 225, 32, 200, 330, 'acc')
    C = f.callout
    C('A', 400, 75, 400, 18, 'Wheel head', 'Carries the grinding wheel and its drive; fed towards the work', 'GRD-F029')
    C('B', 440, 170, 560, 120, 'Grinding wheel', 'Abrasive wheel that grinds the work with its periphery', 'GRD-F031')
    C('C', 170, 210, 60, 160, 'Headstock (work head)', 'Rotates the work slowly; carries one centre', 'GRD-F029')
    C('D', 590, 220, 700, 180, 'Tailstock', 'Supports the other end of the work on a centre', 'GRD-F029')
    C('E', 470, 225, 480, 160, 'Workpiece', 'Cylindrical job held between centres', 'GRD-F029')
    C('F', 640, 305, 720, 280, 'Upper table', 'Carries headstock and tailstock; can be swivelled for tapers', 'GRD-F029')
    C('G', 300, 352, 250, 412, 'Lower table', 'Reciprocates along the base, carrying the upper table', 'GRD-F029')
    C('H', 150, 334, 110, 290, 'Adjustable table dog', 'Set to reverse the table at the ends of its traverse', 'GRD-F030')
    C('I', 690, 385, 745, 410, 'Base', 'Supports the machine and table ways', 'GRD-F029')
    return f


def types():
    f = Fig('grinding/types', 780, 520, 'Types of grinding',
            'Four schematic sketches of grinding operations, panels A to D',
            ask={'p': 'Which type of grinding is shown in panel {L}?', 'w': 'Which panel shows {P}?'})
    for (x, y) in [(10, 10), (400, 10), (10, 265), (400, 265)]:
        f.rect(x, y, 370, 245, 'thin', rx=8)
    # A surface: wheel over flat block, table arrow
    x, y = 10, 10
    _wheel_side(f, x + 185, y + 95, 55)
    f.rect(x + 60, y + 150, 250, 40, 'f'); f.arrow(x + 120, y + 215, x + 250, y + 215, 'acc'); f.arrow(x + 250, y + 215, x + 120, y + 215, 'acc')
    f.panel('A', x + 25, y + 25, 'Surface grinding', 'Flat surfaces finished by a wheel over a reciprocating table', 'GRD-F021')
    # B cylindrical external: wheel beside rotating cylinder (end view)
    x, y = 400, 10
    _wheel_side(f, x + 120, y + 125, 70)
    f.circle(x + 240, y + 125, 50, 'f'); f.circle(x + 240, y + 125, 4, 'k')
    f.arc(x + 240, y + 125, 66, 120, 30, 'acc')
    f.panel('B', x + 25, y + 25, 'External cylindrical grinding', 'Outside diameter of work between centres ground by the wheel periphery', 'GRD-F026')
    # C internal: small wheel inside a bore (end view)
    x, y = 10, 265
    f.circle(x + 185, y + 125, 95, 'f'); f.circle(x + 185, y + 125, 62, 's')
    f.raw(f'<circle cx="{x + 185}" cy="{y + 125}" r="61" fill="#ffffff" fill-opacity="0" stroke="none"/>')
    _wheel_side(f, x + 210, y + 125, 30)
    f.panel('C', x + 25, y + 25, 'Internal grinding', 'Bore (inside diameter) finished by a small wheel running inside it', 'GRD-F035')
    # D centreless: grinding wheel, work on rest blade, regulating wheel
    x, y = 400, 265
    _wheel_side(f, x + 95, y + 115, 70)
    f.circle(x + 200, y + 112, 26, 'f')
    f.circle(x + 290, y + 115, 55, 'f2')
    f.poly([(x + 180, y + 140), (x + 222, y + 140), (x + 210, y + 215), (x + 190, y + 215)], 'f')
    f.panel('D', x + 25, y + 25, 'Centreless grinding', 'Work rests on a blade between the grinding wheel and a regulating wheel, with no centres', 'GRD-F036')
    return f


def marking():
    f = Fig('grinding/wheel-marking', 760, 300, 'Grinding wheel marking',
            'The marking A 46 K 5 V with each position numbered 1 to 5 underneath',
            ask={'p': 'In the wheel marking shown, what does position {L} indicate?', 'w': 'In the wheel marking, which position gives the {P}?'})
    xs = [150, 270, 390, 510, 630]
    for x, t in zip(xs, ['A', '46', 'K', '5', 'V']):
        f.rect(x - 50, 70, 100, 80, 'f', rx=10)
        f.text(x, 112, t, 44, weight='bold')
    names = [('Abrasive type', 'A = aluminium oxide (C = silicon carbide)', 'GRD-F047'),
             ('Grain (grit) size', '46 = medium grain', 'GRD-F052'),
             ('Grade (hardness of bond)', 'K = medium grade', 'GRD-F055'),
             ('Structure (grain spacing)', '5 = fairly dense structure', 'GRD-F060'),
             ('Bond type', 'V = vitrified bond', 'GRD-F062')]
    for i, (x, (nm, fn, fa)) in enumerate(zip(xs, names)):
        L = '12345'[i]
        f.line(x, 150, x, 195, 'lead')
        # numeric tags drawn as discs (use letters slot mechanism)
        f.top.append(f'<circle cx="{x}" cy="{215}" r="17" fill="#e8590c"/><text x="{x}" y="{216}" font-size="19" font-weight="700" text-anchor="middle" dominant-baseline="middle" fill="#ffffff">{L}</text>')
        f.labels[L] = {'part': nm, 'function': fn, 'fact': fa}
    f.text(380, 30, 'A 46 K 5 V', 24)
    f.text(380, 270, 'positions 1 → 5 read left to right', 15)
    return f


def structure():
    f = Fig('grinding/structure', 700, 300, 'Wheel structure: dense vs open',
            'Two magnified views of abrasive grains in bond; panel A grains closely packed, panel B grains widely spaced',
            ask={'p': 'Which wheel structure is shown in panel {L}?', 'w': 'Which panel shows a {P}?'})
    rnd = random.Random(3)
    for i, (ox, sp) in enumerate([(20, 26), (370, 46)]):
        f.rect(ox, 50, 310, 220, 'thin', rx=8)
        y = 70
        while y < 255:
            x = ox + 20 + rnd.uniform(0, 8)
            while x < ox + 295:
                r = rnd.uniform(8, 11)
                pts = [(x + r * math.cos(a) * rnd.uniform(0.75, 1.1), y + r * math.sin(a) * rnd.uniform(0.75, 1.1)) for a in [k * math.pi / 3 for k in range(6)]]
                f.poly(pts, 'f2')
                x += sp + rnd.uniform(-3, 3)
            y += sp * 0.9
    f.panel('A', 40, 30, 'Dense structure (low number)', 'Grains closely packed; for hard, brittle materials and fine finish', 'GRD-F061')
    f.panel('B', 390, 30, 'Open structure (high number)', 'Grains widely spaced with large pores; for soft ductile materials and rough grinding', 'GRD-F061')
    return f


def dressing():
    f = Fig('grinding/dressing', 640, 360, 'Dressing a grinding wheel',
            'Side view of a grinding wheel with a single-point diamond dresser held against its face')
    cx, cy, r = 230, 170, 120
    _wheel_side(f, cx, cy, r)
    tx, ty = cx + r * math.cos(math.radians(40)), cy + r * math.sin(math.radians(40))
    f.poly([(tx, ty + 1), (tx - 12, ty + 24), (tx + 14, ty + 24)], 'f2')      # diamond tip touching the wheel
    f.rect(tx - 18, ty + 24, 150, 28, 'f')                                    # holder
    f.arc(cx, cy, r + 20, 120, 40, 'acc')
    e = math.radians(40)
    ex, ey = cx + (r + 20) * math.cos(e), cy - (r + 20) * math.sin(e)
    f.arrow(ex - 0.64 * 6, ey - 0.77 * 6, ex + 0.64 * 4, ey + 0.77 * 4, 'acc', head=13)
    f.arrow(tx + 175, ty + 38, tx + 140, ty + 38, 'acc')
    C = f.callout
    C('A', 180, 120, 60, 40, 'Grinding wheel', 'Abrasive wheel whose face is being dressed', 'GRD-F068')
    C('B', tx + 2, ty + 12, tx + 90, ty - 50, 'Diamond dresser', 'Tool that removes the dull, loaded surface to expose sharp grains (dressing) and trues the wheel', 'GRD-F069')
    C('C', tx + 100, ty + 52, tx + 130, ty + 90, 'Dresser holder', 'Rigid holder that feeds the diamond across the wheel face', 'GRD-F068')
    return f


def gratio():
    f = Fig('grinding/grinding-ratio', 720, 340, 'Grinding ratio set-up',
            'Wheel of width d worn from initial diameter Di to final diameter Df while a block of length l and breadth b is reduced in height by Δh')
    _wheel_side(f, 230, 150, 100)
    f.circle(230, 150, 115, 'd')
    f.hdim(115, 345, 22, 'Di (new wheel)', 15)
    f.hdim(130, 330, 285, 'Df (worn wheel)', 15, above=False)
    f.text(230, 325, 'wheel width = d', 15)
    f.poly([(420, 244), (640, 244), (680, 214), (460, 214)], 'f')
    f.poly([(420, 244), (640, 244), (640, 290), (420, 290)], 'f')
    f.poly([(640, 244), (680, 214), (680, 260), (640, 290)], 'f')
    f.poly([(420, 230), (640, 230), (680, 200), (460, 200)], 'd')   # original top before grinding
    f.line(420, 230, 420, 244, 'd'); f.line(640, 230, 640, 244, 'd'); f.line(680, 200, 680, 214, 'd')
    f.hdim(420, 640, 312, 'l', 16, above=False)
    f.text(672, 285, 'b', 16)
    f.text(410, 237, 'Δh', 15, anchor='end')
    f.text(560, 120, 'G = Vw / Vs', 20, weight='bold')
    return f


FIGS = [surface, cylindrical, types, marking, structure, dressing, gratio]
