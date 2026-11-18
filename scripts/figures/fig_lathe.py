import math
from figlib import Fig

# ---------------------------------------------------------------- overview

def overview():
    f = Fig('lathe/lathe-overview', 780, 420, 'Centre lathe — main parts',
            'Side-view line diagram of a centre lathe with lettered callouts A to Q')
    # legs and chip tray
    f.rect(95, 262, 90, 140, 'f')
    f.rect(560, 262, 80, 140, 'f')
    f.line(85, 402, 195, 402); f.line(550, 402, 650, 402)
    f.rect(185, 318, 375, 12, 'f2')
    # bed with guideway line
    f.rect(70, 228, 640, 34, 'f')
    f.line(70, 236, 710, 236, 'thin')
    # lead screw (threads shown) and feed rod below the bed
    f.rect(195, 265, 510, 7, 's')
    x = 199
    while x < 703:
        f.line(x, 265, x + 4, 272, 'thin'); x += 7
    f.rect(195, 280, 510, 5, 's')
    f.rect(700, 262, 12, 28, 'f')
    # headstock
    f.rect(70, 70, 140, 158, 'f')
    f.rect(85, 140, 110, 50, 's', rx=4)
    for cx, lx, ly in [(110, 98, 88), (150, 162, 86)]:
        f.circle(cx, 110, 7, 's'); f.line(cx, 103, lx, ly)
        f.circle(lx, ly - 4, 4, 'k')
    # quick-change gear box in front, below headstock
    f.rect(80, 196, 120, 28, 'f2', rx=3)
    for cx in (105, 140, 175):
        f.circle(cx, 210, 6, 's')
    # spindle nose + chuck
    f.rect(210, 122, 12, 36, 's')
    f.rect(222, 98, 26, 84, 'f', rx=3)
    f.rect(230, 92, 12, 10, 'f2'); f.rect(230, 178, 12, 10, 'f2')
    # workpiece and axis
    f.rect(248, 125, 172, 30, 'f2')
    f.line(215, 140, 600, 140, 'cl')
    # dead centre, quill, tailstock
    f.poly([(420, 140), (440, 130), (440, 150)], 'f')
    f.rect(440, 132, 12, 16, 's')
    f.rect(452, 127, 40, 26, 'f')
    f.poly([(490, 112), (565, 112), (575, 222), (482, 222)], 'f')
    f.rect(474, 218, 110, 10, 'f')
    f.line(530, 112, 545, 92); f.circle(547, 89, 4, 'k')
    f.line(569, 140, 606, 140)
    f.circle(628, 140, 22, 's'); f.circle(628, 140, 4, 'k')
    for a in (90, 210, 330):
        f.line(628, 140, 628 + 22 * math.cos(math.radians(a)), 140 - 22 * math.sin(math.radians(a)))
    f.circle(628, 118, 4, 'k')
    # carriage: saddle, cross slide, compound, tool post, tool, apron
    f.rect(330, 208, 130, 20, 'f')
    f.rect(345, 194, 100, 14, 'f')
    f.rect(360, 180, 70, 14, 'f')
    f.rect(378, 152, 34, 28, 'f2')
    f.poly([(378, 158), (350, 156), (346, 160), (378, 166)], 'f2')
    f.line(412, 160, 436, 150); f.circle(438, 149, 4, 'k')
    f.rect(340, 228, 110, 78, 'f2', rx=3)
    f.circle(368, 282, 16, 's'); f.circle(368, 282, 3, 'k')
    for a in (90, 210, 330):
        f.line(368, 282, 368 + 16 * math.cos(math.radians(a)), 282 - 16 * math.sin(math.radians(a)))
    f.line(420, 250, 432, 268); f.circle(433, 270, 4, 'k')

    C = f.callout
    C('A', 72, 150, 30, 150, 'Headstock', 'Houses the main spindle, speed gear box and change gears; carries the live centre', 'LAT-F017')
    C('B', 235, 99, 235, 40, 'Chuck', 'Grips and rotates the workpiece; attached to the headstock spindle', 'LAT-F019')
    C('C', 708, 233, 745, 222, 'Bed', 'Main supporting structure on which headstock, tailstock and carriage are mounted', 'LAT-F011')
    C('D', 535, 114, 545, 55, 'Tailstock', 'Supports the free end of long work; holds drills and reamers', 'LAT-F022')
    C('E', 430, 136, 430, 75, 'Dead centre', 'Non-rotating centre in the tailstock that supports the work', 'LAT-F024')
    C('F', 472, 127, 476, 75, 'Tailstock quill (spindle)', 'Sliding spindle of the tailstock that carries the dead centre or a drill', 'LAT-F025')
    C('G', 640, 121, 700, 95, 'Tailstock handwheel', 'Moves the tailstock quill in and out', 'LAT-F025')
    C('H', 334, 216, 298, 205, 'Saddle', 'H-shaped part of the carriage that slides along the bed ways', 'LAT-F027')
    C('I', 445, 200, 482, 206, 'Cross-slide', 'Moves the tool at right angles to the lathe axis; sets depth of cut', 'LAT-F029')
    C('J', 362, 187, 318, 170, 'Compound rest', 'Swivelling top slide used for short tapers and angular cuts', 'LAT-F032')
    C('K', 412, 168, 462, 172, 'Tool post', 'Holds the cutting tool rigidly on top of the compound rest', 'LAT-F034')
    C('L', 450, 290, 492, 300, 'Apron', 'Front of the carriage; contains the carriage handwheel, half-nut and feed levers', 'LAT-F036')
    C('M', 705, 268, 745, 262, 'Lead screw', 'Long threaded shaft used only for thread cutting', 'LAT-F038')
    C('N', 705, 282, 745, 302, 'Feed rod', 'Plain shaft that drives the carriage for turning and facing feeds', 'LAT-F037')
    C('O', 100, 370, 45, 372, 'Leg', 'Supports the whole machine on the floor', 'LAT-F040')
    C('P', 82, 210, 30, 205, 'Gear box (feed box)', 'Gives different feeds and thread pitches; drives the feed rod and lead screw', 'LAT-F018')
    C('Q', 300, 330, 300, 382, 'Chip tray', 'Collects chips and coolant falling from the work', 'LAT-F040')
    return f


# ---------------------------------------------------------------- chucks

def chucks():
    f = Fig('lathe/chucks', 640, 330, 'Lathe chucks — front views',
            'Front views of two lathe chucks, panel A and panel B',
            ask={'p': 'Which chuck is shown in panel {L}?', 'w': 'Which panel shows a {P}?'})
    # A: 3-jaw self-centring
    cx, cy = 160, 165
    f.circle(cx, cy, 110, 'f'); f.circle(cx, cy, 22, 's')
    for a in (90, 210, 330):
        r = math.radians(a)
        ux, uy = math.cos(r), -math.sin(r)
        px, py = -uy, ux
        pts = []
        for (s, t) in [(30, -14), (85, -14), (85, 14), (30, 14)]:
            pts.append((cx + ux * s + px * t, cy + uy * s + py * t))
        f.poly(pts, 'f2')
        for s in (44, 56, 68):
            f.line(cx + ux * s + px * -14, cy + uy * s + py * -14, cx + ux * s + px * 14, cy + uy * s + py * 14, 'thin')
    for a in (30, 150, 270):  # single key socket set
        r = math.radians(a)
        f.rect(cx + 95 * math.cos(r) - 5, cy - 95 * math.sin(r) - 5, 10, 10, 's')
    # B: 4-jaw independent
    cx = 480
    f.circle(cx, cy, 110, 'f'); f.circle(cx, cy, 22, 's')
    for ring in (50, 75):
        f.circle(cx, cy, ring, 'thin')
    for a in (0, 90, 180, 270):
        r = math.radians(a)
        ux, uy = math.cos(r), -math.sin(r)
        px, py = -uy, ux
        pts = [(cx + ux * s + px * t, cy + uy * s + py * t) for (s, t) in [(28, -13), (80, -13), (80, 13), (28, 13)]]
        f.poly(pts, 'f2')
        sx, sy = cx + ux * 97, cy + uy * 97
        f.rect(sx - 6, sy - 6, 12, 12, 's')  # each jaw has its own screw square
    f.panel('A', 40, 40, '3-jaw (self-centring) chuck', 'All three jaws move together through a scroll, so round or hexagonal work is centred automatically', 'LAT-F048')
    f.panel('B', 360, 40, '4-jaw (independent) chuck', 'Each jaw has its own screw and moves independently, so irregular work can be held but must be centred manually', 'LAT-F049')
    return f


# ---------------------------------------------------------------- between centres

def centres():
    f = Fig('lathe/centres-dog', 760, 300, 'Work held between centres with a lathe dog',
            'Line diagram of a workpiece held between live and dead centres, driven by a dog and catch plate')
    y = 150
    f.line(30, y, 740, y, 'cl')
    # headstock spindle nose and catch (driving) plate with pin
    f.rect(30, 110, 60, 80, 'f')
    f.rect(90, 70, 18, 160, 'f2')
    f.rect(108, 80, 14, 12, 'k')  # driving pin
    # live centre
    f.poly([(108, 140), (150, 150), (108, 160)], 'f')
    # dog (carrier)
    f.rect(180, 112, 40, 76, 'f', rx=6)
    f.rect(193, 92, 14, 20, 's')  # set screw
    f.poly([(185, 112), (150, 92), (124, 92), (124, 104), (150, 104), (185, 124)], 'f')
    # workpiece
    f.rect(150, 128, 450, 44, 'f2')
    # dead centre and tailstock quill
    f.poly([(600, 150), (640, 138), (640, 162)], 'f')
    f.rect(640, 132, 100, 36, 'f')
    f.arc(560, 150, 34, 200, 330, 'acc')
    f.arrow(588, 169, 590, 168, 'acc', head=11)
    C = f.callout
    C('A', 99, 75, 70, 40, 'Catch (driving) plate', 'Screwed on the spindle nose; its pin drives the tail of the dog', 'LAT-F047')
    C('B', 128, 147, 120, 245, 'Live centre', 'Centre in the headstock spindle that rotates with the work', 'LAT-F020')
    C('C', 205, 113, 235, 45, 'Lathe dog (carrier)', 'Clamped to the work by a set screw and driven by the catch plate', 'LAT-F047')
    C('D', 400, 130, 400, 70, 'Workpiece', 'Job held and turned between the two centres', 'LAT-F046')
    C('E', 618, 146, 600, 70, 'Dead centre', 'Non-rotating centre in the tailstock that supports the free end', 'LAT-F024')
    C('F', 700, 168, 700, 245, 'Tailstock quill', 'Tailstock spindle that carries the dead centre', 'LAT-F025')
    return f


FIGS = [overview, chucks, centres]


# ---------------------------------------------------------------- operations panel

def _op_cell(f, ox, oy, kind):
    """Draw one operation sketch in a 240x170 cell (work axis horizontal, chuck at left)."""
    y = oy + 85
    f.rect(ox + 8, oy + 40, 22, 90, 'f')  # chuck jaw block
    f.line(ox + 8, y, ox + 232, y, 'cl')
    def tool(tx, ty, ang=90, length=50):
        # rectangular tool shank ending in a point at (tx,ty); ang = direction from tip to shank
        a = math.radians(ang)
        ux, uy = math.cos(a), math.sin(a)
        px, py = -uy, ux
        w = 9
        pts = [(tx, ty), (tx + ux * 14 + px * w, ty + uy * 14 + py * w),
               (tx + ux * length + px * w, ty + uy * length + py * w),
               (tx + ux * length - px * w, ty + uy * length - py * w),
               (tx + ux * 14 - px * w, ty + uy * 14 - py * w)]
        f.poly(pts, 'f2')
    r = 30
    if kind == 'facing':
        f.rect(ox + 30, y - r, 150, 2 * r, 'f')
        tool(ox + 182, y - r - 2, 300, 48)
        f.arrow(ox + 205, y - 40, ox + 205, y - 5)
    elif kind == 'straight':
        f.rect(ox + 30, y - r, 30, 2 * r, 'f')
        f.rect(ox + 60, y - r + 8, 150, 2 * r - 16, 'f')
        f.line(ox + 60, y - r, ox + 210, y - r, 'd'); f.line(ox + 60, y + r, ox + 210, y + r, 'd'); f.line(ox + 210, y - r, ox + 210, y + r, 'd')
        tool(ox + 60, y - r + 8, 270, 45)
        f.arrow(ox + 130, oy + 22, ox + 75, oy + 22)
    elif kind == 'step':
        f.rect(ox + 30, y - r, 100, 2 * r, 'f')
        f.rect(ox + 130, y - 18, 80, 36, 'f')
        tool(ox + 132, y - 18, 270, 45)
        f.arrow(ox + 205, oy + 22, ox + 150, oy + 22)
    elif kind == 'taper':
        f.poly([(ox + 30, y - r), (ox + 90, y - r), (ox + 210, y - 14), (ox + 210, y + 14), (ox + 90, y + r), (ox + 30, y + r)], 'f')
        tool(ox + 150, y - 22, 250, 45)
        f.arrow(ox + 205, y - 38, ox + 140, y - 54)
    elif kind == 'grooving':
        f.rect(ox + 30, y - r, 180, 2 * r, 'f')
        f.rect(ox + 140, y - r, 14, 10, 'k')
        f.rect(ox + 140, oy + 10, 14, 45, 'f2')
        f.arrow(ox + 175, oy + 12, ox + 175, oy + 45)
    elif kind == 'parting':
        f.rect(ox + 30, y - r, 180, 2 * r, 'f')
        f.rect(ox + 150, y - r, 6, 2 * r - 8, 'k')
        f.rect(ox + 149, oy + 5, 8, 50, 'f2')
        f.arrow(ox + 175, oy + 12, ox + 175, oy + 70)
    elif kind == 'chamfer':
        f.poly([(ox + 30, y - r), (ox + 190, y - r), (ox + 210, y - r + 20), (ox + 210, y + r - 20), (ox + 190, y + r), (ox + 30, y + r)], 'f')
        f.poly([(ox + 200, y - r + 10), (ox + 232, y - r - 22), (ox + 222, y - r - 32), (ox + 190, y - r)], 'f2')
        f.text(ox + 150, oy + 22, '45°', 15)
    elif kind == 'centre':
        f.rect(ox + 30, y - r, 150, 2 * r, 'f')
        f.poly([(ox + 180, y - 8), (ox + 166, y), (ox + 180, y + 8)], 'k')
        f.rect(ox + 186, y - 10, 46, 20, 'f2')
        f.poly([(ox + 186, y - 4), (ox + 172, y), (ox + 186, y + 4)], 'f2')
        f.arrow(ox + 225, y + 28, ox + 192, y + 28)
    elif kind == 'thread':
        f.rect(ox + 30, y - r, 180, 2 * r, 'f')
        x = ox + 90
        while x < ox + 205:
            f.poly([(x, y - r), (x + 6, y - r + 9), (x + 12, y - r)], 'k')
            f.poly([(x, y + r), (x + 6, y + r - 9), (x + 12, y + r)], 'k')
            x += 12
        f.poly([(ox + 120, y - r + 9), (ox + 114, y - r - 2), (ox + 126, y - r - 2)], 'f2')
        f.rect(ox + 110, y - r - 47, 20, 45, 'f2')
        f.arrow(ox + 165, oy + 18, ox + 115, oy + 18)
    elif kind == 'knurling':
        f.rect(ox + 30, y - r, 180, 2 * r, 'f')
        for k in range(10):
            xx = ox + 100 + k * 10
            f.line(xx, y - r, xx + 12, y + r, 'thin'); f.line(xx + 12, y - r, xx, y + r, 'thin')
        f.circle(ox + 150, y - r - 14, 14, 'f2'); f.circle(ox + 120, y - r - 14, 14, 'f2')
        f.rect(ox + 110, y - r - 50, 50, 16, 'f2')


OPS = [('facing', 'Facing', 'Flat end surface; tool fed perpendicular to the axis; reduces length', 'LAT-F073'),
       ('straight', 'Straight (plain) turning', 'Diameter reduced along the length; tool fed parallel to the axis', 'LAT-F074'),
       ('step', 'Step turning', 'Diameter reduced over part of the length, leaving a shoulder', 'LAT-F075'),
       ('taper', 'Taper turning', 'Uniform change of diameter along the length; tool fed at the half-taper angle', 'LAT-F081'),
       ('grooving', 'Grooving', 'Narrow groove cut by plunging a grooving tool radially', 'LAT-F078'),
       ('parting', 'Parting-off', 'Tool plunged radially until the finished job is cut off', 'LAT-F079'),
       ('chamfer', 'Chamfering', 'Bevels the sharp end edge (e.g. 45°) to remove burrs', 'LAT-F076'),
       ('centre', 'Centre drilling', 'Conical centre hole drilled from the tailstock so the work can be supported on a centre', 'LAT-F080'),
       ('thread', 'Thread cutting', 'Helical groove cut by a single-point tool fed one pitch per revolution', 'LAT-F087'),
       ('knurling', 'Knurling', 'Pattern pressed (embossed) on the surface by knurling rollers', 'LAT-F077')]


def operations():
    f = Fig('lathe/operations', 760, 700, 'Lathe operations',
            'Ten small sketches of lathe operations, each marked with a letter A to J; orange arrows show feed direction',
            ask={'p': 'Which lathe operation is shown in panel {L}?', 'w': 'Which panel shows {P}?',
                 'f': 'What does the operation in panel {L} do?'})
    for i, (k, name, func, fact) in enumerate(OPS):
        col, row = i % 3, i // 3
        if i == 9:
            col = 1
        ox, oy = 10 + col * 250, 10 + row * 172
        f.rect(ox, oy, 240, 165, 'thin', rx=8)
        _op_cell(f, ox, oy, k)
        f.panel('ABCDEFGHIJ'[i], ox + 22, oy + 22, name, func, fact)
    return f


# ---------------------------------------------------------------- thread profiles

def threads():
    f = Fig('lathe/thread-profiles', 780, 330, 'Thread profiles',
            'Three thread profiles marked A, B and C',
            ask={'p': 'Which thread profile is shown in panel {L}?', 'w': 'Which panel shows a {P}?',
                 'f': 'What is the thread form in panel {L} typically used for?'})
    base = 230
    # A metric V 60
    ox = 30
    pts = [(ox, base)]
    p = 70
    for k in range(3):
        x = ox + k * p
        pts += [(x + p * 0.5, base - 60.6), (x + p, base)]
    f.poly(pts + [(ox + 3 * p, base + 30), (ox, base + 30)], 'f')
    f.arc(ox + p * 1.5, base - 60.6, 34, 240, 300, 'acc')
    f.text(ox + p * 1.5, base - 90, '60°', 17)
    # B square
    ox = 290
    pts = [(ox, base)]
    for k in range(3):
        x = ox + k * 70
        pts += [(x, base - 60), (x + 35, base - 60), (x + 35, base), (x + 70, base)]
    f.poly(pts + [(ox + 210, base + 30), (ox, base + 30)], 'f')
    # C buttress
    ox = 550
    pts = [(ox, base)]
    for k in range(3):
        x = ox + k * 70
        pts += [(x + 8, base - 65), (x + 20, base - 65), (x + 70, base)]
    f.poly(pts + [(ox + 210, base + 30), (ox, base + 30)], 'f')
    for x in (30, 290, 550):
        f.hdim(x, x + 70, base + 55, 'p', 16)
    f.panel('A', 30, 40, 'Metric V-thread', 'Fastening threads (bolts, nuts, screws); 60° included angle', 'LAT-F090')
    f.panel('B', 290, 40, 'Square thread', 'Power/load transmission such as screw jacks and lead screws', 'LAT-F094')
    f.panel('C', 550, 40, 'Buttress thread', 'Transmits heavy load in one direction only, e.g. vices', 'LAT-F095')
    return f


def thread_terms():
    f = Fig('lathe/thread-terms', 760, 380, 'Screw thread nomenclature',
            'Enlarged V-thread profile with lettered features')
    base, p = 250, 120
    top = base - 103.9
    pts = [(60, base)]
    for k in range(4):
        x = 60 + k * p
        pts += [(x + p / 2, top), (x + p, base)]
    f.poly(pts + [(540, 320), (60, 320)], 'f')
    f.line(40, top, 680, top, 'd'); f.line(40, base, 680, base, 'd')
    f.line(40, 340, 680, 340, 'cl')
    f.hdim(60 + p / 2, 60 + 1.5 * p, 95, '', 16)
    f.vdim(600, top, base, '', 16, left=False)
    f.vdim(640, top, 340, '', 16, left=False)
    f.vdim(670, base, 340, '', 16, left=False)
    C = f.callout
    C('A', 60 + 2.5 * p, top, 60 + 2.5 * p, 70, 'Crest', 'Top surface of the thread', 'LAT-F089')
    C('B', 60 + 2 * p, base, 60 + 2 * p, 300, 'Root', 'Bottom of the groove between two threads', 'LAT-F089')
    C('C', 60 + 0.25 * p, (top + base) / 2, 30, 160, 'Flank', 'Side surface joining crest and root', 'LAT-F089')
    C('D', 60 + p, 95, 120, 60, 'Pitch', 'Axial distance between corresponding points on adjacent threads', 'LAT-F089')
    C('E', 600, 190, 560, 190, 'Depth of thread', 'Radial distance between crest and root (d = 0.6134 p for our metric thread)', 'LAT-F092')
    C('F', 640, 220, 715, 205, 'Major diameter (radius shown)', 'Largest diameter of the thread, measured over the crests', 'LAT-F089')
    C('G', 670, 320, 715, 355, 'Minor (core) diameter (radius shown)', 'Smallest diameter, at the roots: Dc = Dm − 2d', 'LAT-F093')
    return f


# ---------------------------------------------------------------- single point tool

def spt():
    f = Fig('lathe/spt-tool', 720, 385, 'Single-point cutting tool',
            'Line drawing of a single-point lathe tool in plan and side views with lettered features')
    # plan view
    f.poly([(260, 80), (640, 80), (640, 150), (200, 150), (140, 120), (150, 95)], 'f')
    f.text(400, 175, 'plan view', 14)
    # side view: positive rake face sloping back from the cutting edge, flank relieved below it
    f.poly([(150, 236), (270, 256), (640, 256), (640, 336), (182, 336)], 'f')
    f.line(150, 236, 330, 236, 'd')       # horizontal reference through the cutting edge
    f.line(150, 236, 150, 346, 'd')       # vertical reference through the cutting edge
    f.arc(150, 236, 110, 0, -9.5, 'acc')  # rake angle
    f.arc(150, 236, 95, -90, -73.9, 'acc')  # clearance angle
    f.text(400, 362, 'side view', 14)
    C = f.callout
    C('A', 500, 115, 500, 35, 'Shank', 'Main body of the tool held in the tool post', 'LAT-F068')
    C('B', 145, 107, 85, 70, 'Nose', 'Corner where the side and end cutting edges meet', 'LAT-F068')
    C('C', 210, 246, 205, 200, 'Face', 'Top surface over which the chip flows', 'LAT-F068')
    C('D', 165, 283, 90, 270, 'Flank', 'Surface below the cutting edge, facing the work', 'LAT-F068')
    C('E', 520, 336, 560, 368, 'Base', 'Bottom surface of the shank that rests on the tool post', 'LAT-F068')
    C('F', 258, 246, 300, 205, 'Rake angle', 'Slope of the face; eases chip flow and lowers cutting force', 'LAT-F070')
    C('G', 163, 330, 90, 345, 'Clearance (relief) angle', 'Angle of the flank that stops it rubbing on the work', 'LAT-F071')
    return f


# ---------------------------------------------------------------- taper geometry

def taper():
    f = Fig('lathe/taper', 720, 300, 'Taper geometry', 'Side view of a tapered portion with dimensions D, d, L and half-angle α')
    f.poly([(150, 70), (550, 120), (550, 220), (150, 270)], 'f')
    f.line(100, 170, 620, 170, 'cl')
    f.line(150, 70, 560, 70, 'd')
    f.arc(150, 70, 140, 0, -7.1, 'acc')
    f.text(310, 88, 'α', 20)
    f.vdim(110, 70, 270, 'D', 20)
    f.vdim(590, 120, 220, 'd', 20, left=False)
    f.hdim(150, 550, 290, 'L', 18, above=True)
    f.text(360, 35, 'tan α = (D − d) / 2L', 20)
    return f


# ---------------------------------------------------------------- ME-106 job drawing (data driven)

JOB = {'chamfer': '1 × 45°',
       'seg': [  # (start dia, end dia, length, label)
           (38, 38, 35, 'P'), (38, 34, 30, 'Q'), (30, 30, 5, 'R'), (34, 34, 25, 'S'), (32, 32, 20, 'T')],
       'thread': 'Ø34 × 1.5 pitch'}


def job(blank=False):
    f = Fig('lathe/job-2025' + ('-q' if blank else ''), 780, 360, 'ME-106 lathe job (2025 drawing)' + (' — dimensions hidden' if blank else ''),
            'Drawing of the stepped, tapered and threaded lathe job; segments lettered P to T' + (', dimensions not shown' if blank else ', fully dimensioned'),
            ask={'p': 'In the lathe job drawing, which feature is segment {L}?'})
    sx, y0, k = 80, 170, 5.4  # scale px/mm
    x = sx
    for (d1, d2, L, tag) in JOB['seg']:
        x2 = x + L * k
        h1, h2 = d1 * k / 2 * 0.95, d2 * k / 2 * 0.95
        if tag == 'P':
            c = 1 * k
            f.poly([(x, y0 - h1 + c), (x + c, y0 - h1), (x2, y0 - h1), (x2, y0 + h1), (x + c, y0 + h1), (x, y0 + h1 - c)], 'f')
        else:
            f.poly([(x, y0 - h1), (x2, y0 - h2), (x2, y0 + h2), (x, y0 + h1)], 'f')
        if tag == 'S':
            xx = x
            while xx < x2 - 2:
                f.line(xx, y0 - h1, xx + 4, y0 - h1 + 6, 'thin'); f.line(xx, y0 + h1, xx + 4, y0 + h1 - 6, 'thin')
                xx += 8
            f.line(x, y0 - h1 + 6, x2, y0 - h1 + 6, 'thin'); f.line(x, y0 + h1 - 6, x2, y0 + h1 - 6, 'thin')
        f.hdim(x, x2, 280, '' if blank else str(L), 16, above=False)
        ty = 60 if tag != 'R' else 32
        f.tag(tag, (x + x2) / 2, ty)
        f.line((x + x2) / 2, ty + 15, (x + x2) / 2, y0 - max(h1, h2) - 2, 'lead')
        x = x2
    f.line(sx - 20, y0, x + 20, y0, 'cl')
    f.hdim(sx, x, 330, '' if blank else '115', 17, above=False)
    # centre holes
    for xx, s in ((sx, 1), (x, -1)):
        f.poly([(xx, y0 - 5), (xx + 10 * s, y0), (xx, y0 + 5)], 's')
    f.text(620, 20, 'All dimensions in mm', 15)
    names = {'P': ('Ø38 plain section, 35 mm long', 'LAT-F105'), 'Q': ('Taper from Ø38 to Ø34, 30 mm long', 'LAT-F106'),
             'R': ('Groove, 5 mm wide', 'LAT-F107'), 'S': ('Thread Ø34 × 1.5 mm pitch, 25 mm long', 'LAT-F108'),
             'T': ('Ø32 end section, 20 mm long', 'LAT-F109')}
    for t, (n, fa) in names.items():
        f.labels[t] = {'part': n, 'function': n, 'fact': fa}
    # diameter notes under the drawing
    if blank:
        return f
    f.text(80 + 17.5 * k, y0 - 30, 'Ø38', 16)
    f.text(80 + 50 * k, y0 - 30, 'Ø38 → Ø34', 15)
    f.text(80 + (70 + 12.5) * k, y0 - 30, 'Ø34 × 1.5', 15)
    f.text(80 + (95 + 10) * k, y0 - 30, 'Ø32', 16)
    f.text(sx + 10, y0 - 108, '1 × 45°', 14, anchor='start')
    return f


FIGS = [overview, chucks, centres, operations, threads, thread_terms, spt, taper, job, lambda: job(True)]
