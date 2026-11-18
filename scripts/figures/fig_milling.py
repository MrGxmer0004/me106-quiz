import math
from figlib import Fig


def _gear(f, cx, cy, r_out, r_root, n, rot=0, c='f'):
    pts = []
    for i in range(n):
        a0 = 2 * math.pi * i / n + rot
        step = 2 * math.pi / n
        for (fr, rr) in [(0.0, r_root), (0.15, r_out), (0.45, r_out), (0.6, r_root)]:
            a = a0 + fr * step
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    f.poly(pts, c)


# ---------------------------------------------------------------- horizontal mill

def horizontal():
    f = Fig('milling/horizontal-mill', 760, 520, 'Horizontal column-and-knee milling machine',
            'Side-view line diagram of a horizontal column-and-knee milling machine with lettered callouts')
    f.rect(60, 470, 560, 30, 'f')                       # base
    f.rect(80, 60, 150, 410, 'f')                       # column
    f.rect(230, 52, 400, 40, 'f')                       # overarm
    f.rect(560, 92, 40, 120, 'f')                       # arbor support
    f.line(230, 175, 600, 175, 'cl')
    f.rect(230, 168, 340, 14, 'f2')                     # arbor
    f.circle(232, 175, 18, 'f')                         # spindle nose
    _gear(f, 400, 175, 46, 38, 18)                      # cutter (side view drawn as disc)
    f.circle(400, 175, 10, 's')
    f.rect(270, 252, 360, 22, 'f')                      # table
    for x in (300, 360, 420, 480, 540, 600):
        f.rect(x, 252, 10, 6, 'k')                      # T-slots
    f.rect(340, 222, 120, 30, 'f2')                     # workpiece
    f.rect(290, 274, 300, 30, 'f')                      # saddle
    f.rect(230, 304, 300, 90, 'f')                      # knee
    f.rect(370, 394, 16, 76, 's')                       # elevating screw
    x = 372
    for yy in range(398, 466, 8):
        f.line(372, yy, 384, yy + 5, 'thin')
    f.circle(560, 320, 16, 's'); f.line(530, 320, 544, 320)   # knee crank
    f.circle(610, 289, 12, 's')                         # cross-feed handwheel
    f.circle(640, 263, 12, 's')                         # table handwheel
    f.rect(100, 80, 70, 40, 's', rx=6)                  # motor/drive
    C = f.callout
    C('A', 90, 485, 40, 470, 'Base', 'Heavy foundation casting supporting the whole machine', 'MIL-F050')
    C('B', 150, 300, 40, 300, 'Column', 'Main vertical casting housing the spindle drive; carries the overarm', 'MIL-F052')
    C('C', 300, 360, 220, 430, 'Knee', 'Slides up and down on the column (vertical feed) and carries the saddle and table', 'MIL-F053')
    C('D', 440, 289, 470, 340, 'Saddle', 'Moves on the knee towards or away from the column (cross feed)', 'MIL-F054')
    C('E', 600, 263, 690, 225, 'Table', 'Carries the work and moves longitudinally on the saddle', 'MIL-F054')
    C('F', 500, 175, 500, 120, 'Arbor', 'Horizontal shaft on which the milling cutters are mounted', 'MIL-F055')
    C('G', 450, 60, 450, 22, 'Overarm (overhanging arm)', 'Arm on top of the column that carries the arbor support', 'MIL-F050')
    C('H', 590, 150, 690, 150, 'Arbor support', 'Supports the outer end of the arbor to keep it rigid', 'MIL-F055')
    C('I', 228, 175, 180, 220, 'Spindle', 'Rotating spindle in the column that drives the arbor and cutter', 'MIL-F050')
    C('J', 400, 132, 340, 120, 'Milling cutter', 'Rotating multi-point tool that removes metal', 'MIL-F001')
    C('K', 378, 440, 450, 445, 'Elevating screw', 'Raises and lowers the knee', 'MIL-F053')
    return f


# ---------------------------------------------------------------- vertical mill

def vertical():
    f = Fig('milling/vertical-mill', 640, 540, 'Vertical milling machine',
            'Line diagram of a vertical knee-type milling machine with lettered callouts')
    f.rect(70, 495, 400, 28, 'f')
    f.rect(90, 120, 130, 375, 'f')                     # column
    f.rect(130, 60, 300, 50, 'f')                      # ram (overarm)
    f.rect(330, 110, 70, 110, 'f')                     # head
    f.rect(350, 220, 30, 40, 'f2')                     # quill/spindle
    f.rect(358, 260, 14, 40, 'f2')                     # end mill
    f.rect(240, 340, 330, 22, 'f')                     # table
    f.rect(310, 310, 110, 30, 'f2')                    # work
    f.rect(260, 362, 220, 28, 'f')                     # saddle
    f.rect(220, 390, 230, 80, 'f')                     # knee
    f.line(365, 150, 365, 470, 'cl')
    C = f.callout
    C('A', 380, 150, 470, 140, 'Milling head', 'Carries the vertical spindle and its drive', 'MIL-F056')
    C('B', 260, 85, 260, 30, 'Ram (overarm)', 'Arm on the column that carries the head; can be moved in and out', 'MIL-F056')
    C('C', 365, 245, 470, 245, 'Spindle (quill)', 'Vertical spindle that holds and rotates the end mill', 'MIL-F048')
    C('D', 540, 351, 600, 320, 'Table', 'Carries the work; moves longitudinally', 'MIL-F054')
    C('E', 470, 376, 560, 410, 'Saddle', 'Gives cross movement of the table', 'MIL-F054')
    C('F', 260, 440, 170, 470, 'Knee', 'Moves vertically on the column to raise or lower the work', 'MIL-F053')
    C('G', 150, 300, 40, 300, 'Column', 'Main vertical body of the machine', 'MIL-F052')
    C('H', 100, 510, 40, 510, 'Base', 'Supports the machine', 'MIL-F050')
    C('I', 365, 285, 470, 290, 'End mill', 'Cutter with teeth on its end and periphery, used for slots and faces', 'MIL-F036')
    return f


# ---------------------------------------------------------------- up vs down

def _cw_arrow(f, cx, cy, r, a1=150, a2=40):
    f.arc(cx, cy, r, a1, a2, 'acc')
    t = math.radians(a2)
    ex, ey = cx + r * math.cos(t), cy - r * math.sin(t)
    tx, ty = math.sin(t), math.cos(t)          # clockwise tangent in screen coords
    f.arrow(ex - tx * 6, ey - ty * 6, ex + tx * 4, ey + ty * 4, 'acc', head=13)


def updown():
    f = Fig('milling/up-down', 780, 340, 'Up milling and down milling',
            'Two sketches of a clockwise-rotating milling cutter on a workpiece with the table feed arrow; panels A and B',
            ask={'p': 'Which milling method is shown in panel {L}?', 'w': 'Which panel shows {P}?'})
    R, Rr = 70, 58
    for i, ox in enumerate([20, 410]):
        cx, cy = ox + 175, 130
        top_cut, top_raw = cy + R, cy + R - 14
        dx = math.sqrt(R * R - (top_raw - cy) ** 2)
        arc = [(cx + R * math.sin(math.radians(k)), cy + R * math.cos(math.radians(k))) for k in range(0, 37, 4)]
        if i == 0:   # down milling: work fed LEFT, uncut stock on the RIGHT
            pts = [(ox + 15, top_cut), (cx, top_cut)] + [(x, y) for (x, y) in arc if x <= cx + dx] + [(cx + dx, top_raw), (ox + 335, top_raw), (ox + 335, 270), (ox + 15, 270)]
            f.arrow(ox + 300, 300, ox + 200, 300, 'acc')
        else:        # up milling: work fed RIGHT, uncut stock on the LEFT
            arcl = [(2 * cx - x, y) for (x, y) in arc]
            pts = [(ox + 15, top_raw), (cx - dx, top_raw)] + list(reversed([(x, y) for (x, y) in arcl if x >= cx - dx])) + [(cx, top_cut), (ox + 335, top_cut), (ox + 335, 270), (ox + 15, 270)]
            f.arrow(ox + 50, 300, ox + 150, 300, 'acc')
        f.poly(pts, 'f')
        _gear(f, cx, cy, R, Rr, 14)
        f.circle(cx, cy, 14, 's'); f.circle(cx, cy, 3, 'k')
        _cw_arrow(f, cx, cy, R + 22)
        f.text(ox + 250 if i == 0 else ox + 100, 322, 'table feed', 15)
    f.panel('A', 40, 40, 'Down (climb) milling', 'Cutter teeth move in the same direction as the feed at the cut; chip thickness is maximum at the start', 'MIL-F010')
    f.panel('B', 430, 40, 'Up (conventional) milling', 'Cutter rotation opposes the feed; chip thickness starts at zero and is maximum at the end', 'MIL-F008')
    return f


# ---------------------------------------------------------------- cutters panel

def cutters():
    f = Fig('milling/cutters', 780, 520, 'Milling cutters',
            'Six small line drawings of milling cutters, each marked with a letter',
            ask={'p': 'Which milling cutter is shown in panel {L}?', 'w': 'Which panel shows a {P}?',
                 'f': 'The cutter in panel {L} is mainly used for…'})
    cells = [(10, 10), (270, 10), (530, 10), (10, 265), (270, 265), (530, 265)]
    for (x, y) in cells:
        f.rect(x, y, 240, 240, 'thin', rx=8)
    # A plain/slab helical cutter (side view): cylinder with helical teeth lines
    x, y = 10, 10
    f.rect(x + 40, y + 90, 160, 90, 'f')
    for k in range(7):
        xx = x + 42 + k * 20
        f.line(xx, y + 180, xx + 30, y + 90, 'thin')
    f.rect(x + 20, y + 128, 200, 14, 'f2')
    f.panel('A', x + 22, y + 22, 'Plain (slab) helical cutter', 'Machining wide flat surfaces with the periphery teeth (slab milling)', 'MIL-F032')
    # B side-and-face cutter (front view): disc with teeth around, plus side-teeth ticks
    x, y = 270, 10
    _gear(f, x + 120, y + 135, 85, 70, 20)
    f.circle(x + 120, y + 135, 22, 's')
    for k in range(20):
        a = 2 * math.pi * k / 20
        f.line(x + 120 + 40 * math.cos(a), y + 135 + 40 * math.sin(a), x + 120 + 62 * math.cos(a), y + 135 + 62 * math.sin(a), 'thin')
    f.panel('B', x + 22, y + 22, 'Side-and-face cutter', 'Cutting slots, steps and two parallel faces (straddle milling); cuts on periphery and both sides', 'MIL-F030')
    # C end mill: shank + fluted body
    x, y = 530, 10
    f.rect(x + 95, y + 40, 50, 80, 'f')
    f.rect(x + 95, y + 120, 50, 95, 'f2')
    for k in range(5):
        f.line(x + 95, y + 130 + k * 18, x + 145, y + 120 + k * 18, 'thin')
    f.panel('C', x + 22, y + 22, 'End mill', 'Cuts on its end and sides; used for slots, pockets and faces on a vertical mill', 'MIL-F036')
    # D slitting saw: very thin disc with many fine teeth (edge view + face)
    x, y = 10, 265
    _gear(f, x + 120, y + 130, 90, 84, 48)
    f.circle(x + 120, y + 130, 20, 's')
    f.rect(x + 215, y + 40, 6, 180, 'f2')
    f.panel('D', x + 22, y + 22, 'Slitting saw', 'Very thin cutter for narrow slots and cutting off', 'MIL-F033')
    # E T-slot cutter: shank + flat disc at bottom
    x, y = 270, 265
    f.rect(x + 105, y + 40, 30, 120, 'f')
    f.rect(x + 50, y + 160, 140, 34, 'f2')
    for k in range(8):
        f.line(x + 55 + k * 18, y + 160, x + 55 + k * 18, y + 194, 'thin')
    f.panel('E', x + 22, y + 22, 'T-slot cutter', 'Cutting T-slots such as those in machine tables', 'MIL-F034')
    # F involute gear (form) cutter: disc with form-shaped teeth (front view)
    x, y = 530, 265
    cx, cy = x + 120, y + 135
    pts = []
    n = 12
    for i in range(n):
        a0 = 2 * math.pi * i / n
        st = 2 * math.pi / n
        prof = [(0.0, 62), (0.08, 70), (0.14, 82), (0.2, 88), (0.3, 88), (0.36, 82), (0.42, 70), (0.5, 62), (1.0, 62)]
        for fr, rr in prof[:-1]:
            a = a0 + fr * st
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    f.poly(pts, 'f')
    f.circle(cx, cy, 24, 's'); f.rect(cx - 5, cy - 30, 10, 8, 'k')
    f.panel('F', x + 22, y + 22, 'Involute gear cutter', 'Form cutter whose tooth profile matches the gear tooth space; used to cut spur gears', 'MIL-F042')
    return f


# ---------------------------------------------------------------- straddle / gang

def straddle_gang():
    f = Fig('milling/straddle-gang', 760, 330, 'Straddle and gang milling set-ups',
            'Two front views of cutters on a horizontal arbor machining a workpiece; panels A and B',
            ask={'p': 'Which milling set-up is shown in panel {L}?', 'w': 'Which panel shows {P}?'})
    # A straddle: two equal side cutters, work between
    ox = 20
    f.line(ox, 90, ox + 340, 90, 'cl')
    f.rect(ox + 10, 82, 320, 16, 'f2')
    for x in (ox + 110, ox + 210):
        f.rect(x, 40, 22, 100, 'f')
    f.rect(ox + 132, 84, 78, 12, 's')  # spacer collars
    f.text(ox + 171, 70, 'spacer', 13)
    f.poly([(ox + 60, 290), (ox + 60, 220), (ox + 132, 220), (ox + 132, 128), (ox + 210, 128), (ox + 210, 220), (ox + 280, 220), (ox + 280, 290)], 'f')
    # B gang: cutters of different diameters
    ox = 400
    f.line(ox, 90, ox + 340, 90, 'cl')
    f.rect(ox + 10, 82, 320, 16, 'f2')
    f.rect(ox + 60, 50, 60, 80, 'f')
    f.rect(ox + 120, 30, 80, 120, 'f')
    f.rect(ox + 200, 60, 80, 60, 'f')
    f.poly([(ox + 60, 290), (ox + 60, 130), (ox + 120, 130), (ox + 120, 150), (ox + 200, 150), (ox + 200, 120), (ox + 280, 120), (ox + 280, 290)], 'f')
    f.panel('A', 40, 40, 'Straddle milling', 'Two side cutters separated by spacer collars machine two parallel faces at once', 'MIL-F021')
    f.panel('B', 420, 40, 'Gang milling', 'Several cutters of different sizes on one arbor machine several surfaces simultaneously', 'MIL-F022')
    return f


# ---------------------------------------------------------------- dividing head

def dividing_head():
    f = Fig('milling/dividing-head', 780, 440, 'Universal dividing (indexing) head — schematic',
            'Schematic of a dividing head showing index plate, crank, worm and worm wheel driving the work spindle, with lettered callouts')
    # index plate (front)
    pcx, pcy = 150, 230
    f.circle(pcx, pcy, 110, 'f')
    for rr, nh in ((95, 33), (78, 27), (61, 21)):
        for k in range(nh):
            a = 2 * math.pi * k / nh
            f.circle(pcx + rr * math.cos(a), pcy + rr * math.sin(a), 2.6, 'k')
    # crank and pin
    ca = -0.35
    ux, uy = math.cos(ca), math.sin(ca)
    f.poly([(pcx - uy * 7, pcy + ux * 7), (pcx + ux * 95 - uy * 7, pcy + uy * 95 + ux * 7),
            (pcx + ux * 95 + uy * 7, pcy + uy * 95 - ux * 7), (pcx + uy * 7, pcy - ux * 7)], 'f2')
    f.rect(pcx - 8, pcy - 8, 16, 16, 'f2')
    pin = (pcx + 95 * ux, pcy + 95 * uy)
    f.circle(pin[0], pin[1], 8, 'f2')
    # sector arms
    f.line(pcx, pcy, pcx + 105 * math.cos(-0.9), pcy + 105 * math.sin(-0.9), 'acc')
    f.line(pcx, pcy, pcx + 105 * math.cos(-0.9 + 5.14), pcy + 105 * math.sin(-0.9 + 5.14), 'acc')
    # worm shaft from crank to worm
    f.rect(150, 222, 290, 16, 'f2')
    # worm (helical)
    f.rect(390, 205, 100, 50, 'f')
    for k in range(7):
        f.line(395 + k * 14, 255, 409 + k * 14, 205, 'thin')
    # worm wheel (edge view as gear above worm)
    _gear(f, 440, 130, 75, 66, 40)
    f.circle(440, 130, 18, 's')
    # spindle and work
    f.line(440, 130, 740, 130, 'cl')
    f.rect(458, 122, 200, 16, 'f2')
    f.rect(560, 95, 30, 70, 'f')   # gear blank on mandrel
    # tailstock
    f.poly([(690, 130), (705, 120), (705, 140)], 'f')
    f.rect(705, 110, 50, 120, 'f')
    f.text(440, 30, '40 : 1', 18, weight='bold')
    C = f.callout
    C('A', 70, 290, 40, 360, 'Index plate', 'Plate with circles of equally spaced holes used to count crank movement', 'MIL-F060')
    C('B', pcx + 55 * ux, pcy + 55 * uy, 40, 150, 'Index crank', 'Handle turned to rotate the worm; 40 turns = one turn of the work', 'MIL-F063')
    C('C', pin[0] + 4, pin[1] - 6, 250, 80, 'Index pin (plunger)', 'Engages a hole of the selected circle to lock the crank', 'MIL-F060')
    C('D', pcx + 100 * math.cos(-0.9 + 5.14), pcy + 100 * math.sin(-0.9 + 5.14), 120, 400, 'Sector arms', 'Set to span the required number of holes so they need not be counted each time', 'MIL-F072')
    C('E', 470, 230, 520, 300, 'Worm (single start)', 'Driven by the crank; turns the worm wheel one tooth per revolution', 'MIL-F062')
    C('F', 470, 75, 520, 40, 'Worm wheel (40 teeth)', 'Fixed to the work spindle; gives the 40 : 1 reduction', 'MIL-F062')
    C('G', 620, 130, 620, 200, 'Work spindle / mandrel', 'Carries the gear blank and rotates it by the indexed amount', 'MIL-F100')
    C('H', 730, 170, 730, 260, 'Tailstock', 'Supports the outer end of the mandrel', 'MIL-F061')
    return f


# ---------------------------------------------------------------- index plate with move

def _index_plate(fid, holes, turns, extra, title, fact):
    f = Fig(fid, 560, 470, title,
            f'Index plate showing a {holes}-hole circle, the crank pin start hole and the sector arms spanning {extra} hole spaces')
    cx, cy, r = 280, 235, 170
    f.circle(cx, cy, 205, 'f')
    start = -90
    for k in range(holes):
        a = math.radians(start + 360 * k / holes)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        if k == 0:
            f.circle(x, y, 9, 'accf' if False else 's'); f.circle(x, y, 5, 'k')
        elif k == extra:
            f.circle(x, y, 9, 's'); f.circle(x, y, 5, 'acct')
        else:
            f.circle(x, y, 4, 'k')
    a2 = math.radians(start + 360 * extra / holes)
    f.line(cx, cy, cx + (r + 25) * math.cos(math.radians(start)), cy + (r + 25) * math.sin(math.radians(start)), 'acc')
    f.line(cx, cy, cx + (r + 25) * math.cos(a2), cy + (r + 25) * math.sin(a2), 'acc')
    # arc arrow
    f.arc(cx, cy, r - 30, 90, 90 - 360 * extra / holes, 'acc')
    f.circle(cx, cy, 14, 'f2')
    f.text(cx, cy + 40, f'{holes}-hole circle', 18, weight='bold')
    f.text(cx, 18, 'start hole', 14)
    return f


def plate33():
    return _index_plate('milling/index-plate-33', 33, 1, 27, 'Index plate: 22-tooth gear (ME-106 job)', 'MIL-F098')


def plate21():
    return _index_plate('milling/index-plate-21', 21, 2, 18, 'Index plate: 14-tooth practice example', 'MIL-F096')


# ---------------------------------------------------------------- gear nomenclature

def gear_terms():
    f = Fig('milling/gear-nomenclature', 780, 470, 'Spur gear tooth nomenclature',
            'Enlarged view of five spur-gear teeth with outside, pitch and root circles and lettered terms')
    cx, cy = 390, 1180
    Rp = 900
    Ro, Rr = Rp + 70, Rp - 81
    n = 48
    st = 2 * math.pi / n
    pts = []
    for i in range(-3, 4):
        a0 = -math.pi / 2 + i * st
        for fr, rr in [(-0.5, Rr), (-0.29, Rr), (-0.17, Ro), (0.17, Ro), (0.29, Rr), (0.5, Rr)]:
            a = a0 + fr * st
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    pts += [(pts[-1][0], 470), (pts[0][0], 470)]
    f.poly(pts, 'f')
    span = 26
    f.arc(cx, cy, Ro, 90 + span, 90 - span, 'd')
    f.arc(cx, cy, Rp, 90 + span, 90 - span, 'cl')
    f.arc(cx, cy, Rr, 90 + span, 90 - span, 'd')
    P = lambda rr, ang: (cx + rr * math.cos(ang), cy + rr * math.sin(ang))
    sp = -math.pi / 2 + 0.5 * st           # centre of the tooth space right of the middle tooth
    x0 = P(Rp, sp)[0]
    f.vdim(x0, cy - Ro, cy - Rp, '', 14, left=False)
    f.vdim(x0, cy - Rp, cy - Rr, '', 14, left=False)
    sp2 = -math.pi / 2 - 1.5 * st
    x1 = P(Rp, sp2)[0]
    f.vdim(x1, cy - Ro, cy - Rr, '', 14)
    # circular pitch: arc above tips between centres of two adjacent teeth
    f.arc(cx, cy, Ro + 30, 90, 90 - math.degrees(st), 'thin')
    for ang in (-math.pi / 2, -math.pi / 2 + st):
        a, b = P(Rp, ang), P(Ro + 40, ang)
        f.line(a[0], a[1], b[0], b[1], 'thin')
    # tooth thickness: accent arc on pitch circle across the tooth left of middle
    tl = -math.pi / 2 - st
    f.arc(cx, cy, Rp, 90 + math.degrees(st) + math.degrees(0.25 * st), 90 + math.degrees(st) - math.degrees(0.25 * st), 'acc')
    C = f.callout
    C('A', x0, cy - (Ro + Rp) / 2, x0 + 120, 120, 'Addendum', 'Radial height of the tooth above the pitch circle = 1/DP', 'MIL-F077')
    C('B', x0, cy - (Rp + Rr) / 2, x0 + 120, 330, 'Dedendum', 'Radial depth of the tooth below the pitch circle = 1.157/DP', 'MIL-F077')
    C('C', *P(Rp, -math.pi / 2 + math.radians(22)), 730, 230, 'Pitch circle', 'Imaginary circle on which mating gears roll; diameter = N/DP', 'MIL-F076')
    C('D', *P(Ro, -math.pi / 2 - math.radians(23)), 50, 120, 'Outside (addendum) circle', 'Circle through the tooth tips; diameter OD = (N + 2)/DP', 'MIL-F075')
    C('E', *P(Rr, -math.pi / 2 - math.radians(24)), 50, 330, 'Root (dedendum) circle', 'Circle through the bottoms of the tooth spaces', 'MIL-F083')
    C('F', *P(Ro + 30, -math.pi / 2 + 0.5 * st), cx + 70, 30, 'Circular pitch', 'Distance between corresponding points of adjacent teeth along the pitch circle = π/DP', 'MIL-F080')
    C('G', x1, cy - (Ro + Rr) / 2, x1 - 100, 400, 'Whole depth', 'Total depth of the tooth space = addendum + dedendum = 2.157/DP', 'MIL-F078')
    C('H', *P(Rp, tl), P(Rp, tl)[0] - 40, 30, 'Tooth thickness (on pitch circle)', 'Width of a tooth measured along the pitch circle = π/(2·DP)', 'MIL-F080')
    return f


# ---------------------------------------------------------------- gear types

def gear_types():
    f = Fig('milling/gear-types', 780, 560, 'Types of gears',
            'Seven simple line drawings of gear pairs, each marked with a letter',
            ask={'p': 'Which type of gear drive is shown in panel {L}?', 'w': 'Which panel shows {P}?',
                 'f': 'The gears in panel {L} connect shafts that are…'})
    cells = [(10, 10), (270, 10), (530, 10), (10, 190), (270, 190), (530, 190), (270, 370)]
    for (x, y) in cells:
        f.rect(x, y, 240, 170, 'thin', rx=8)
    # A spur: two meshing gears, front view
    x, y = 10, 10
    _gear(f, x + 85, y + 95, 52, 44, 16); _gear(f, x + 175, y + 95, 40, 32, 12, rot=0.26)
    f.circle(x + 85, y + 95, 6, 'k'); f.circle(x + 175, y + 95, 6, 'k')
    f.panel('A', x + 20, y + 20, 'Spur gears', 'Parallel shafts; straight teeth parallel to the axis', 'MIL-F084')
    # B helical: side view rectangles with slanted teeth
    x, y = 270, 10
    for j, (xx, w) in enumerate(((x + 40, 70), (x + 120, 70))):
        f.rect(xx, y + 40, w, 110, 'f')
        for k in range(7):
            if j == 0:
                f.line(xx, y + 60 + k * 14, xx + w, y + 40 + k * 14, 'thin')
            else:
                f.line(xx, y + 40 + k * 14, xx + w, y + 60 + k * 14, 'thin')
    f.panel('B', x + 20, y + 20, 'Helical gears', 'Parallel shafts; teeth inclined to the axis, smoother running with axial thrust', 'MIL-F085')
    # C herringbone
    x, y = 530, 10
    for j, xx in enumerate((x + 40, x + 125)):
        f.rect(xx, y + 40, 75, 110, 'f')
        for k in range(7):
            yy = y + 48 + k * 14
            d = 10 if j == 0 else -10
            f.line(xx, yy + (0 if j == 0 else 10), xx + 37, yy + (10 if j == 0 else 0), 'thin'); f.line(xx + 37, yy + (10 if j == 0 else 0), xx + 75, yy + (0 if j == 0 else 10), 'thin')
    f.panel('C', x + 20, y + 20, 'Double-helical (herringbone) gears', 'Parallel shafts; opposite helices cancel the axial thrust', 'MIL-F086')
    # D bevel: two cone frusta whose apexes meet at the intersection of the axes
    x, y = 10, 190
    ax, ay = x + 150, y + 85                    # apex where the axes cross; both pitch cones have 45° half-angles
    f.line(ax, y + 160, ax, y + 40, 'cl'); f.line(x + 50, ay, ax + 40, ay, 'cl')
    f.poly([(ax - 30, ay + 30), (ax + 30, ay + 30), (ax + 65, ay + 65), (ax - 65, ay + 65)], 'f')    # gear on vertical axis
    f.poly([(ax - 30, ay - 30), (ax - 30, ay + 30), (ax - 65, ay + 65), (ax - 65, ay - 65)], 'f')    # gear on horizontal axis
    for (px, py) in [(ax + 65, ay + 65), (ax - 65, ay - 65), (ax - 65, ay + 65)]:
        f.line(px, py, ax, ay, 'd')
    f.panel('D', x + 20, y + 20, 'Bevel gears', 'Intersecting shafts, usually at 90°', 'MIL-F087')
    # E worm & wheel
    x, y = 270, 190
    _gear(f, x + 120, y + 70, 48, 40, 20)
    f.rect(x + 40, y + 120, 160, 34, 'f')
    for k in range(10):
        f.line(x + 45 + k * 15, y + 154, x + 57 + k * 15, y + 120, 'thin')
    f.panel('E', x + 20, y + 20, 'Worm and worm wheel', 'Non-intersecting shafts at 90°; large speed reduction', 'MIL-F088')
    # F rack & pinion
    x, y = 530, 190
    _gear(f, x + 120, y + 75, 42, 34, 14)
    pts = [(x + 20, y + 155)]
    xx = x + 20
    while xx < x + 220:
        pts += [(xx, y + 125), (xx + 5, y + 117), (xx + 11, y + 117), (xx + 16, y + 125)]
        xx += 16
    pts += [(x + 220, y + 125), (x + 220, y + 155)]
    f.poly(pts, 'f')
    f.arrow(x + 150, y + 165, x + 210, y + 165, 'acc')
    f.panel('F', x + 20, y + 20, 'Rack and pinion', 'Converts rotary motion into straight-line motion', 'MIL-F089')
    # G internal
    x, y = 270, 370
    cx, cy = x + 120, y + 88
    f.circle(cx, cy, 72, 'f')
    pts = []
    n = 24
    for i in range(n):
        a0 = 2 * math.pi * i / n
        st = 2 * math.pi / n
        for fr, rr in [(0, 62), (0.15, 52), (0.45, 52), (0.6, 62)]:
            a = a0 + fr * st
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    f.raw('<polygon class="s" style="fill:var(--bg,#fff);fill-opacity:1" points="' + ' '.join(f'{px:.1f},{py:.1f}' for px, py in pts) + '"/>')
    _gear(f, cx + 18, cy, 30, 23, 10)
    f.panel('G', x + 20, y + 20, 'Internal gear', 'Teeth cut on the inside of a ring; meshes with a pinion on a parallel shaft', 'MIL-F090')
    return f


FIGS = [horizontal, vertical, updown, cutters, straddle_gang, dividing_head, plate33, plate21, gear_terms, gear_types]
