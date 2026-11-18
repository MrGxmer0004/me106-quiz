import math, random, json, os
from figlib import Fig, ROOT

# ============================================================ hand tools

def bench_vice():
    f = Fig('fitting/bench-vice', 760, 420, 'Bench vice', 'Side-view line diagram of a bench vice with lettered callouts')
    f.rect(80, 330, 420, 30, 'f')                                 # base (bolted to bench)
    f.rect(60, 360, 640, 18, 'thin')                              # bench top
    f.rect(120, 150, 90, 180, 'f')                                # fixed jaw body
    f.rect(210, 255, 300, 50, 'f')                                # slide / body
    f.rect(330, 150, 80, 105, 'f')                                # movable jaw
    f.rect(206, 150, 10, 60, 'f2'); f.rect(326, 150, 10, 60, 'f2')   # jaw plates
    for yy in range(154, 208, 8):
        f.line(206, yy, 216, yy + 4, 'thin'); f.line(326, yy, 336, yy + 4, 'thin')
    f.rect(216, 170, 110, 40, 'f2')                               # workpiece
    f.rect(410, 268, 230, 14, 's')                                # screw
    for xx in range(416, 636, 9):
        f.line(xx, 268, xx + 5, 282, 'thin')
    f.circle(650, 275, 12, 'f')                                   # handle boss
    f.rect(644, 190, 12, 170, 'f2')                               # handle (tommy bar)
    C = f.callout
    C('A', 160, 200, 60, 150, 'Fixed jaw', 'Stationary jaw cast with the body', 'FIT-F026')
    C('B', 380, 190, 470, 140, 'Movable (sliding) jaw', 'Moves in and out on the slide when the handle is turned', 'FIT-F026')
    C('C', 211, 160, 211, 100, 'Jaw plates', 'Hardened, serrated plates screwed to the jaws that grip the work', 'FIT-F027')
    C('D', 560, 275, 560, 220, 'Screw (spindle)', 'Square-threaded screw that moves the movable jaw', 'FIT-F026')
    C('E', 650, 330, 720, 330, 'Handle (tommy bar)', 'Turned to tighten or loosen the vice', 'FIT-F026')
    C('F', 300, 290, 300, 350, 'Body / slide', 'Guides the movable jaw', 'FIT-F026')
    C('G', 120, 345, 50, 300, 'Base', 'Bolted to the work bench', 'FIT-F026')
    C('H', 270, 190, 270, 120, 'Workpiece', 'Job gripped between the jaws, projecting only a little above them', 'FIT-F028')
    return f


def marking_tools():
    f = Fig('fitting/marking-tools', 780, 520, 'Marking and holding tools',
            'Eight small line drawings of fitting marking and holding tools, each marked with a letter',
            ask={'p': 'Which tool is shown in panel {L}?', 'w': 'Which panel shows a {P}?', 'f': 'The tool in panel {L} is used to…'})
    cells = [(10 + (i % 4) * 192, 10 + (i // 4) * 255) for i in range(8)]
    for (x, y) in cells:
        f.rect(x, y, 182, 245, 'thin', rx=8)
    # A scriber
    x, y = cells[0]
    f.rect(x + 86, y + 50, 10, 150, 'f'); f.poly([(x + 86, y + 200), (x + 96, y + 200), (x + 91, y + 228)], 'f2')
    f.poly([(x + 86, y + 50), (x + 96, y + 50), (x + 100, y + 38), (x + 112, y + 30)], 's')
    f.panel('A', x + 20, y + 20, 'Scriber', 'Scratch (scribe) fine lines on metal for marking out', 'FIT-F033')
    # B try square
    x, y = cells[1]
    f.rect(x + 40, y + 50, 26, 160, 'f2'); f.rect(x + 66, y + 50, 90, 12, 'f')
    f.panel('B', x + 20, y + 20, 'Try square', 'Check squareness (90°) of edges and surfaces', 'FIT-F021')
    # C V-block with round bar
    x, y = cells[2]
    f.poly([(x + 30, y + 200), (x + 30, y + 110), (x + 70, y + 110), (x + 91, y + 150), (x + 112, y + 110), (x + 152, y + 110), (x + 152, y + 200)], 'f')
    f.circle(x + 91, y + 128, 26, 'f2')
    f.panel('C', x + 20, y + 20, 'V-block', 'Hold round bars steady for marking or drilling', 'FIT-F029')
    # D surface gauge (scribing block)
    x, y = cells[3]
    f.rect(x + 40, y + 200, 100, 18, 'f'); f.rect(x + 86, y + 70, 8, 130, 'f2')
    f.line(x + 60, y + 120, x + 150, y + 105); f.circle(x + 90, y + 115, 6, 'k')
    f.panel('D', x + 20, y + 20, 'Surface gauge (scribing block)', 'Scribe lines parallel to the surface plate at a set height', 'FIT-F034')
    # E odd-leg caliper
    x, y = cells[4]
    f.circle(x + 91, y + 55, 10, 'f')
    f.line(x + 86, y + 62, x + 60, y + 210); f.line(x + 60, y + 210, x + 72, y + 214)
    f.line(x + 96, y + 62, x + 122, y + 214)
    f.panel('E', x + 20, y + 20, 'Odd-leg (jenny) caliper', 'Draw lines parallel to an edge or find the centre of a bar', 'FIT-F035')
    # F divider
    x, y = cells[5]
    f.circle(x + 91, y + 55, 10, 'f'); f.line(x + 91, y + 45, x + 91, y + 35)
    f.line(x + 86, y + 62, x + 55, y + 214); f.line(x + 96, y + 62, x + 127, y + 214)
    f.line(x + 70, y + 140, x + 112, y + 140, 'thin')
    f.panel('F', x + 20, y + 20, 'Divider', 'Draw circles and arcs, and transfer distances', 'FIT-F036')
    # G angle plate
    x, y = cells[6]
    f.poly([(x + 40, y + 210), (x + 150, y + 210), (x + 150, y + 190), (x + 62, y + 190), (x + 62, y + 70), (x + 40, y + 70)], 'f')
    for yy in (100, 140): f.rect(x + 46, y + yy, 10, 20, 's')
    f.panel('G', x + 20, y + 20, 'Angle plate', 'Hold work at 90° to the surface plate', 'FIT-F031')
    # H C-clamp
    x, y = cells[7]
    f.path(f'M{x+120},{y+60} L{x+60},{y+60} Q{x+40},{y+60} {x+40},{y+80} L{x+40},{y+180} Q{x+40},{y+200} {x+60},{y+200} L{x+120},{y+200}', 's')
    f.rect(x + 108, y + 52, 18, 18, 'f'); f.rect(x + 112, y + 70, 10, 100, 'f2'); f.rect(x + 104, y + 170, 26, 10, 'f')
    f.rect(x + 108, y + 192, 18, 14, 'f')
    f.panel('H', x + 20, y + 20, 'C-clamp', 'Clamp work to a table or angle plate', 'FIT-F030')
    return f


def punches():
    f = Fig('fitting/punches', 640, 360, 'Dot punch and centre punch',
            'Two punches side by side with their point angles marked; panels A and B',
            ask={'p': 'Which punch is shown in panel {L}?', 'w': 'Which panel shows a {P}?'})
    for i, (ox, ang) in enumerate(((60, 60), (380, 90))):
        cx = ox + 100
        f.rect(cx - 16, 50, 32, 200, 'f')
        for k in range(12):
            f.line(cx - 16, 70 + k * 8, cx + 16, 74 + k * 8, 'thin')
        h = 16 / math.tan(math.radians(ang / 2))
        f.poly([(cx - 16, 250), (cx + 16, 250), (cx, 250 + h)], 'f2')
        f.arc(cx, 250 + h, 26, 90 + ang / 2, 90 - ang / 2, 'acc')
        f.text(cx, 250 + h + 52, f'{ang}°', 20, weight='bold')
    f.panel('A', 40, 40, 'Dot punch', 'Point angle about 60°; light witness marks along scribed lines', 'FIT-F037')
    f.panel('B', 360, 40, 'Centre punch', 'Point angle about 90°; deeper mark to locate the drill', 'FIT-F038')
    return f


def hacksaw():
    f = Fig('fitting/hacksaw', 780, 340, 'Hacksaw', 'Line diagram of an adjustable-frame hacksaw with lettered callouts and the cutting direction')
    f.path('M140,90 L640,90 L640,230', 's')
    f.path('M140,90 L140,230', 's')
    f.rect(132, 220, 516, 18, 'f2')                               # blade
    x = 140
    while x < 640:
        f.poly([(x, 238), (x + 8, 238), (x + 8, 246)], 'k')     # teeth pointing forward (away from handle, to the right)
        x += 10
    f.path('M60,140 Q60,110 90,110 L140,110 L140,200 L95,200 Q60,200 60,170 Z', 'f')   # handle
    f.circle(655, 230, 10, 'f'); f.line(660, 220, 680, 205); f.line(660, 240, 680, 255)   # wing nut
    f.arrow(320, 290, 470, 290, 'acc')
    f.text(395, 315, 'cutting stroke', 15)
    C = f.callout
    C('A', 400, 90, 400, 40, 'Frame', 'Holds the blade in tension', 'FIT-F053')
    C('B', 300, 229, 260, 290, 'Blade', 'Hardened saw blade (high-carbon steel or HSS) with teeth', 'FIT-F057')
    C('C', 95, 160, 40, 260, 'Handle', 'Gripped to push and pull the saw', 'FIT-F053')
    C('D', 668, 230, 730, 170, 'Wing nut', 'Tightens the blade to the correct tension', 'FIT-F053')
    C('E', 560, 244, 600, 300, 'Teeth', 'Point forward, away from the handle, because the saw cuts on the forward stroke', 'FIT-F054')
    return f


def file_parts():
    f = Fig('fitting/file-parts', 780, 300, 'Parts of a file', 'Line diagram of a flat file with lettered parts')
    f.poly([(80, 150), (190, 135), (190, 165)], 'f')              # tang
    f.rect(190, 125, 40, 50, 'f')                                 # heel (uncut)
    f.poly([(230, 120), (650, 128), (700, 140), (700, 160), (650, 172), (230, 180)], 'f2')   # body
    for xx in range(240, 690, 14):
        f.line(xx, 124, xx + 10, 176, 'thin')
    C = f.callout
    C('A', 130, 150, 120, 90, 'Tang', 'Pointed end that fits into the wooden handle', 'FIT-F058')
    C('B', 210, 150, 210, 230, 'Heel', 'Uncut part next to the tang', 'FIT-F058')
    C('C', 450, 150, 450, 70, 'Face', 'Broad cutting surface carrying the teeth', 'FIT-F058')
    C('D', 450, 178, 450, 240, 'Edge', 'Narrow side of the file', 'FIT-F058')
    C('E', 700, 150, 740, 100, 'Point (tip)', 'Far end of the file, opposite the tang', 'FIT-F058')
    return f


def file_sections():
    f = Fig('fitting/file-sections', 780, 260, 'File cross-sections', 'Five file cross-sections, panels A to E',
            ask={'p': 'Which file shape is shown in cross-section {L}?', 'w': 'Which cross-section is a {P}?', 'f': 'The file in section {L} is mainly used for…'})
    xs = [80, 230, 380, 530, 680]
    for x in xs:
        f.rect(x - 70, 10, 140, 240, 'thin', rx=8)
    y = 150
    f.rect(xs[0] - 45, y - 12, 90, 24, 'f2')
    f.rect(xs[1] - 25, y - 25, 50, 50, 'f2')
    f.circle(xs[2], y, 26, 'f2')
    f.path(f'M{xs[3]-45},{y+12} L{xs[3]+45},{y+12} Q{xs[3]},{y-34} {xs[3]-45},{y+12} Z', 'f2')
    f.poly([(xs[4] - 32, y + 22), (xs[4] + 32, y + 22), (xs[4], y - 33)], 'f2')
    data = [('Flat file', 'Filing flat surfaces', 'FIT-F063'), ('Square file', 'Filing square slots and holes', 'FIT-F063'),
            ('Round file', 'Enlarging round holes and filing concave curves', 'FIT-F063'),
            ('Half-round file', 'Filing concave curves (round side) and flat surfaces (flat side)', 'FIT-F063'),
            ('Triangular (three-square) file', 'Filing corners and angles less than 90°', 'FIT-F063')]
    for x, L, (n_, fn, fa) in zip(xs, 'ABCDE', data):
        f.panel(L, x - 48, 34, n_, fn, fa)
    return f


def hammers():
    f = Fig('fitting/hammers', 720, 320, 'Fitting hammers', 'Two hammer heads: panel A and panel B',
            ask={'p': 'Which hammer is shown in panel {L}?', 'w': 'Which panel shows a {P}?'})
    for i, ox in enumerate((30, 380)):
        f.rect(ox, 30, 320, 270, 'thin', rx=8)
        cx = ox + 160
        f.rect(cx - 12, 140, 24, 150, 'f2')                       # handle
        f.rect(cx - 100, 100, 160, 40, 'f')                       # head body
        f.rect(cx - 120, 95, 20, 50, 'f')                         # flat face
        if i == 0:
            f.path(f'M{cx+60},{100} A30,20 0 0 1 {cx+60},{140}', 'f')   # ball peen
            f.circle(cx + 78, 120, 20, 'f')
        else:
            f.poly([(cx + 60, 100), (cx + 105, 112), (cx + 105, 128), (cx + 60, 140)], 'f')   # cross peen (wedge, at right angle to handle seen edge-on)
            f.line(cx + 105, 112, cx + 105, 128)
    f.panel('A', 55, 55, 'Ball-peen hammer', 'Flat face for striking; hemispherical peen for riveting and peening', 'FIT-F072')
    f.panel('B', 405, 55, 'Cross-peen hammer', 'Wedge-shaped peen at right angles to the handle', 'FIT-F073')
    return f


def vernier_parts():
    f = Fig('fitting/vernier-parts', 800, 340, 'Vernier caliper — parts', 'Line diagram of a Vernier caliper with lettered parts')
    f.rect(60, 120, 680, 40, 'f')                                 # beam / main scale
    for k in range(0, 66):
        x = 140 + k * 9
        f.line(x, 120, x, 128 + (6 if k % 10 == 0 else 0) + (3 if k % 5 == 0 else 0), 'thin')
    f.poly([(60, 160), (110, 160), (110, 260), (90, 290), (60, 290)], 'f')           # fixed outside jaw
    f.poly([(60, 120), (110, 120), (110, 90), (95, 60), (80, 90), (80, 120)], 'f')   # fixed inside jaw
    f.rect(250, 110, 150, 60, 'f2')                               # slider with vernier
    f.poly([(250, 170), (300, 170), (300, 260), (280, 290), (250, 260)], 'f2')       # movable outside jaw
    f.poly([(250, 110), (290, 110), (290, 90), (272, 60), (262, 90), (250, 90)], 'f2')   # movable inside jaw
    for k in range(0, 11):
        x = 262 + k * 12
        f.line(x, 170, x, 160 - (6 if k % 5 == 0 else 0), 'thin')
    f.rect(320, 96, 24, 14, 's')                                  # locking screw
    f.rect(740, 136, 50, 8, 'f2')                                 # depth rod
    C = f.callout
    C('A', 500, 125, 500, 60, 'Main scale', 'Fixed scale on the beam, graduated in mm', 'FIT-F045')
    C('B', 330, 163, 420, 230, 'Vernier scale', 'Sliding scale; the coinciding line gives the fraction (LC 0.02 mm)', 'FIT-F045')
    C('C', 85, 230, 30, 230, 'Fixed outside jaw', 'Measures outside dimensions together with the movable jaw', 'FIT-F046')
    C('D', 275, 240, 350, 290, 'Movable outside jaw', 'Slides with the vernier to grip the outside of the job', 'FIT-F046')
    C('E', 272, 75, 190, 40, 'Inside jaws', 'Measure inside dimensions such as bores and slots', 'FIT-F046')
    C('F', 332, 100, 400, 60, 'Locking screw', 'Locks the slider so the reading is not lost', 'FIT-F045')
    C('G', 770, 140, 760, 200, 'Depth rod (blade)', 'Measures the depth of holes and steps', 'FIT-F046')
    return f


def micrometer_parts():
    f = Fig('fitting/micrometer-parts', 800, 360, 'Outside micrometer — parts', 'Line diagram of an outside micrometer with lettered parts')
    f.path('M150,150 L150,280 Q150,320 200,320 L420,320 Q460,320 460,280 L460,190', 's')
    f.path('M175,150 L175,275 Q175,295 205,295 L415,295 Q435,295 435,275 L435,190', 's')
    f.rect(140, 130, 45, 40, 'f')                                 # anvil
    f.rect(225, 140, 95, 20, 'f2')                                # spindle (gap between anvil and spindle faces)
    f.rect(320, 130, 130, 40, 'f')                                # sleeve/barrel
    f.line(320, 150, 450, 150, 'thin')
    for k in range(13):
        f.line(330 + k * 9, 150, 330 + k * 9, 142 if k % 2 == 0 else 157, 'thin')
    f.rect(450, 120, 140, 60, 'f2')                               # thimble
    for k in range(8):
        f.line(450, 125 + k * 7, 462, 125 + k * 7, 'thin')
    f.rect(590, 132, 70, 36, 'f')                                 # ratchet
    f.rect(355, 172, 40, 14, 's')                                 # lock nut
    C = f.callout
    C('A', 300, 300, 300, 350, 'Frame', 'C-shaped body that carries the anvil and barrel', 'FIT-F049')
    C('B', 160, 135, 120, 80, 'Anvil', 'Fixed measuring face', 'FIT-F049')
    C('C', 270, 150, 270, 90, 'Spindle', 'Moving measuring face, advanced by the screw', 'FIT-F049')
    C('D', 400, 135, 400, 80, 'Sleeve (barrel)', 'Carries the main scale in mm and half-mm', 'FIT-F049')
    C('E', 520, 125, 520, 70, 'Thimble', 'Rotating scale with 50 divisions (0.01 mm each)', 'FIT-F049')
    C('F', 625, 150, 700, 110, 'Ratchet stop', 'Slips at a set torque so the measuring pressure is uniform', 'FIT-F050')
    C('G', 375, 180, 375, 240, 'Lock nut', 'Locks the spindle to hold the reading', 'FIT-F049')
    return f


# ============================================================ generated readings

VER_LC = 0.02
MIC_LC = 0.01


def vernier_reading(idx, reading):
    """Vernier caliper reading figure; 50-division vernier over 49 mm (LC 0.02 mm)."""
    M = int(reading)
    k = round((reading - M) / VER_LC)
    f = Fig(f'fitting/vernier-{idx:02d}', 900, 260, f'Vernier reading #{idx}',
            'Enlarged view of a Vernier caliper scale; the orange arrow marks the coinciding Vernier line')
    s = 15.0                                           # px per mm
    vz = 60.0                                          # vernier zero x on screen
    ms0 = vz - reading * s                             # screen x of main-scale 0 mm
    # main scale (top)
    f.rect(20, 40, 860, 60, 'f')
    mm = int(max(0, (20 - ms0) / s))
    while ms0 + mm * s < 880:
        x = ms0 + mm * s
        if x >= 20:
            L = 30 if mm % 10 == 0 else (22 if mm % 5 == 0 else 14)
            f.line(x, 100, x, 100 - L, 'thin' if mm % 5 else 's')
            if mm % 10 == 0:
                f.text(x, 52, str(mm), 17, weight='bold')
        mm += 1
    f.text(860, 28, 'main scale (mm)', 13, anchor='end')
    # vernier (bottom): 50 divisions in 49 mm
    f.rect(vz - 15, 100, 49 * s + 30, 60, 'f2')
    for j in range(51):
        x = vz + j * 0.98 * s
        L = 26 if j % 5 == 0 else 15
        f.line(x, 100, x, 100 + L, 's' if j % 5 == 0 else 'thin')
        if j % 5 == 0:
            f.text(x, 140, str(j // 5), 14)
    # arrow at coinciding line
    xc = vz + k * 0.98 * s
    f.arrow(xc, 205, xc, 168, 'acc', head=12)
    f.text(xc, 222, 'coincides', 13)
    f.text(vz, 245, 'vernier 0', 13)
    f.text(860, 245, 'least count 0.02 mm · vernier numbers are tenths of a mm', 13, anchor='end')
    return f, M, k


def micrometer_reading(idx, reading):
    """Micrometer reading figure; sleeve in mm with half-mm marks below the datum, thimble 50 divisions."""
    f = Fig(f'fitting/micrometer-{idx:02d}', 820, 300, f'Micrometer reading #{idx}',
            'Enlarged view of a micrometer sleeve and thimble scale')
    whole_half = math.floor(reading * 2) / 2          # sleeve reading (multiple of 0.5)
    th = round((reading - whole_half) / MIC_LC)       # thimble division 0..49
    s = 40.0                                          # px per mm on sleeve
    edge = 560                                        # thimble edge x
    z = edge - whole_half * s - 8                     # screen x of 0 mm (thimble edge slightly past the last visible line)
    datum = 150
    f.rect(40, 110, edge - 40, 80, 'f')               # sleeve
    f.line(40, datum, edge, datum, 's')               # datum line
    mm = 0
    while True:
        x = z + mm * s
        if x > edge - 2:
            break
        if x >= 40:
            f.line(x, datum, x, datum - 22, 's')
            if mm % 5 == 0:
                f.text(x, datum - 34, str(mm), 16, weight='bold')
        xh = x + s / 2
        if 40 <= xh < edge - 2:
            f.line(xh, datum, xh, datum + 16, 'thin')
        mm += 1
    # thimble: shows divisions around the datum
    f.rect(edge, 60, 200, 180, 'f2')
    pitch_px = 14
    for d in range(-6, 7):
        val = (th + d) % 50
        y = datum - d * pitch_px
        L = 22 if val % 5 == 0 else 12
        f.line(edge, y, edge + L, y, 's' if val % 5 == 0 else 'thin')
        if val % 5 == 0:
            f.text(edge + 40, y, str(val), 15, anchor='start')
    f.text(edge - 10, datum + 60, 'sleeve (mm above, half-mm below the line)', 13, anchor='end')
    f.text(edge + 100, 262, 'thimble: 50 div = 0.5 mm', 13)
    return f, whole_half, th


def generated():
    rnd = random.Random(106)
    out, data = [], {'vernier': [], 'micrometer': []}
    vals = set()
    while len(data['vernier']) < 18:
        r = round(rnd.randint(1000, 7900) * 0.02, 2)    # multiples of 0.02 mm between 20 and 158 mm
        frac = round(r - int(r), 2)
        if r in vals or frac < 0.06 or frac > 0.94:
            continue
        vals.add(r)
        f, M, k = vernier_reading(len(data['vernier']) + 1, r)
        out.append(f); data['vernier'].append({'id': f.id, 'reading': r, 'msr': M, 'k': k})
    vals = set()
    while len(data['micrometer']) < 14:
        r = round(rnd.randint(500, 2499) * 0.01, 2)     # 5.00–24.99 mm
        th = round((r - math.floor(r * 2) / 2) / 0.01)
        if r in vals or th < 3 or th > 47:
            continue
        vals.add(r)
        f, sl, t = micrometer_reading(len(data['micrometer']) + 1, r)
        out.append(f); data['micrometer'].append({'id': f.id, 'reading': r, 'sleeve': sl, 'thimble': t})
    json.dump(data, open(os.path.join(ROOT, 'authoring', 'generated_readings.json'), 'w'), indent=1)
    return out


FIGS = [bench_vice, marking_tools, punches, hacksaw, file_parts, file_sections, hammers, vernier_parts, micrometer_parts, generated]
