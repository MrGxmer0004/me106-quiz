import math
from figlib import Fig


def shaper():
    f = Fig('shaping/shaper', 780, 500, 'Shaping machine (shaper)',
            'Side-view line diagram of a standard crank shaper with lettered callouts')
    f.rect(60, 455, 620, 30, 'f')                        # base
    f.rect(300, 120, 300, 335, 'f')                      # column / body
    f.rect(210, 70, 420, 50, 'f')                        # ram
    f.line(560, 70, 580, 42); f.circle(582, 39, 5, 'k')     # ram locking handle (on the ram)
    f.rect(150, 60, 60, 105, 'f')                        # tool head (swivel + slide)
    f.line(180, 60, 180, 30); f.line(165, 30, 195, 30); f.circle(180, 30, 4, 'k')   # down-feed handle
    f.rect(158, 165, 44, 40, 'f2')                       # clapper box
    f.circle(170, 172, 3, 'k')
    f.rect(172, 205, 14, 40, 'f2')                       # tool
    f.poly([(172, 245), (186, 245), (179, 256)], 'f2')
    f.rect(120, 290, 160, 70, 'f')                       # table (box)
    f.rect(150, 262, 110, 28, 'f2')                      # vice
    f.rect(170, 250, 60, 12, 'f')                        # work in vice
    f.rect(270, 290, 30, 90, 'f')                        # cross-rail block (on column face)
    f.rect(140, 360, 40, 95, 's')                        # table support
    f.circle(300, 395, 12, 's')                          # cross-feed handle
    f.circle(540, 330, 30, 's'); f.circle(540, 330, 5, 'k')   # driving pulley
    f.rect(470, 400, 80, 45, 'f2', rx=4); f.text(510, 422, 'motor', 13)
    f.line(512, 340, 490, 400, 'thin'); f.line(568, 340, 540, 400, 'thin')   # belt
    C = f.callout
    C('A', 420, 95, 420, 40, 'Ram', 'Reciprocating slide that carries the tool head and gives the cutting stroke', 'SHP-F023')
    C('B', 155, 110, 90, 90, 'Tool head', 'Mounted at the front of the ram; can swivel; carries the down-feed slide and clapper box', 'SHP-F024')
    C('C', 180, 34, 90, 30, 'Down-feed handle', 'Lowers the tool to give the depth of cut', 'SHP-F025')
    C('D', 196, 185, 260, 185, 'Clapper box', 'Holds the tool post; its hinged block lets the tool lift on the return stroke', 'SHP-F026')
    C('E', 182, 230, 260, 228, 'Cutting tool', 'Single-point HSS tool that cuts on the forward stroke', 'SHP-F037')
    C('F', 155, 270, 60, 250, 'Vice', 'Holds the job on the table', 'SHP-F031')
    C('G', 130, 330, 60, 330, 'Table', 'Carries the vice and work; moved crosswise for feed', 'SHP-F027')
    C('H', 285, 330, 340, 260, 'Cross rail', 'Mounted on the column front; carries the table and its cross-feed screw', 'SHP-F028')
    C('I', 420, 220, 700, 220, 'Column (body)', 'Box casting housing the drive and carrying the ram guides', 'SHP-F029')
    C('J', 660, 470, 730, 470, 'Base', 'Supports the whole machine', 'SHP-F030')
    C('K', 160, 420, 90, 430, 'Table support', 'Front support that steadies the table', 'SHP-F030')
    C('L', 582, 39, 680, 30, 'Ram locking handle', 'Locks the ram after the stroke position has been adjusted', 'SHP-F020')
    C('M', 566, 318, 700, 300, 'Driving pulley', 'Takes power from the motor to drive the bull gear mechanism', 'SHP-F021')
    return f


def quick_return():
    f = Fig('shaping/quick-return', 720, 520, 'Crank and slotted-lever quick-return mechanism',
            'Line diagram of the crank and slotted-lever mechanism with the crank angles for the cutting and return strokes lettered')
    O = (330, 230)
    r = 80
    P = (330, 230 + 2 * r)                               # pivot at 2r below gives 240/120 split
    f.circle(O[0], O[1], 115, 'f')                       # bull gear
    for k in range(60):
        a = 2 * math.pi * k / 60
        f.line(O[0] + 115 * math.cos(a), O[1] + 115 * math.sin(a), O[0] + 122 * math.cos(a), O[1] + 122 * math.sin(a), 'thin')
    f.circle(O[0], O[1], r, 'd')                         # crank-pin circle
    f.circle(O[0], O[1], 6, 'k')
    # extreme lever positions (tangent to crank circle) - dashed
    for sgn in (1, -1):
        B = (O[0] + sgn * r * math.sin(math.radians(60)), O[1] + r * math.cos(math.radians(60)))
        dx, dy = B[0] - P[0], B[1] - P[1]
        L = 330 / math.hypot(dx, dy)
        f.line(P[0], P[1], P[0] + dx * L, P[1] + dy * L, 'd')
        f.circle(B[0], B[1], 4, 'k')
    # current position: crank pin at top, lever vertical
    pin = (O[0], O[1] - r)
    f.rect(P[0] - 12, 40, 24, P[1] - 40, 'f2')           # slotted lever
    f.rect(P[0] - 4, 60, 8, P[1] - 80, 's')              # slot
    f.rect(pin[0] - 14, pin[1] - 10, 28, 20, 'f')        # sliding block
    f.circle(pin[0], pin[1], 5, 'k')
    f.line(O[0], O[1], pin[0], pin[1])                   # crank
    f.circle(P[0], P[1], 9, 'f'); f.poly([(P[0] - 20, P[1] + 25), (P[0] + 20, P[1] + 25), (P[0], P[1] + 5)], 'f')
    # ram and link
    f.rect(140, 10, 440, 22, 'f')
    f.line(P[0], 45, P[0] + 40, 21); f.circle(P[0] + 40, 21, 4, 'k')
    # driving pinion
    gx, gy = O[0] + 145 * math.cos(math.radians(20)), O[1] + 145 * math.sin(math.radians(20))
    f.circle(gx, gy, 28, 'f'); f.circle(gx, gy, 4, 'k')
    for k in range(16):
        a = 2 * math.pi * k / 16
        f.line(gx + 28 * math.cos(a), gy + 28 * math.sin(a), gx + 34 * math.cos(a), gy + 34 * math.sin(a), 'thin')
    # stroke arcs (outside bull gear): cutting = large arc over the top, return = small arc at bottom
    R2 = 150
    f.arc(O[0], O[1], R2, -30, 210, 'acc')               # 240 deg through the top
    f.arc(O[0], O[1], R2 + 12, -150, -30, 'd')           # 120 deg through the bottom
    C = f.callout
    C('A', O[0] - 90, O[1] + 70, 120, 420, 'Bull gear (crank wheel)', 'Large gear rotating at constant speed; carries the crank pin', 'SHP-F013')
    C('B', pin[0] + 4, pin[1] + 2, 470, 110, 'Crank pin', 'Pin on the bull gear whose radius sets the stroke length', 'SHP-F019')
    C('C', pin[0] - 14, pin[1] - 6, 200, 120, 'Sliding block', 'Pivoted on the crank pin; slides in the slot of the lever', 'SHP-F015')
    C('D', P[0] + 12, 300, 470, 330, 'Slotted lever (link)', 'Oscillates about the pivot, converting crank rotation into ram motion', 'SHP-F013')
    C('E', P[0] + 9, P[1], 450, 420, 'Pivot (fulcrum)', 'Fixed point at the lower end about which the slotted lever swings', 'SHP-F013')
    C('F', 520, 21, 640, 60, 'Ram', 'Reciprocates and carries the tool', 'SHP-F023')
    C('G', gx, gy, 640, 330, 'Driving pinion', 'Small gear from the motor that drives the bull gear', 'SHP-F014')
    C('H', O[0] + R2 * math.cos(math.radians(150)), O[1] - R2 * math.sin(math.radians(150)), 60, 130, 'Crank angle for the cutting stroke', 'Larger arc of crank rotation, so the cutting stroke is slower', 'SHP-F016')
    C('I', O[0] + 162 * math.cos(math.radians(-60)), O[1] + 162 * math.sin(math.radians(60)), 590, 470, 'Crank angle for the return stroke', 'Smaller arc of crank rotation, so the return stroke is faster', 'SHP-F016')
    return f


def clapper():
    f = Fig('shaping/clapper-box', 720, 340, 'Clapper box action',
            'Two sketches of the shaper tool in its clapper box: forward stroke with tool seated and cutting, return stroke with tool lifted and sliding over the work')
    for i, ox in enumerate((20, 380)):
        f.rect(ox, 30, 320, 290, 'thin', rx=8)
        f.rect(ox + 110, 60, 80, 90, 'f')                 # clapper box
        f.circle(ox + 125, 72, 5, 'k')                    # hinge pin
        f.rect(ox, 250, 320, 50, 'f')                     # work
        f.text(ox + 160, 312, 'sketch 1' if i == 0 else 'sketch 2', 15)
        if i == 0:
            f.rect(ox + 120, 70, 60, 70, 'f2')            # clapper block seated
            f.rect(ox + 140, 140, 18, 100, 'f2')
            f.poly([(ox + 140, 240), (ox + 158, 240), (ox + 140, 252)], 'f2')
            f.arrow(ox + 260, 200, ox + 200, 200, 'acc')
        else:
            g = f'<g transform="rotate(14 {ox + 125} {72})">'
            f.raw(g)
            f.rect(ox + 120, 70, 60, 70, 'f2'); f.rect(ox + 140, 140, 18, 100, 'f2')
            f.poly([(ox + 140, 240), (ox + 158, 240), (ox + 140, 252)], 'f2')
            f.raw('</g>')
            f.arrow(ox + 60, 200, ox + 120, 200, 'acc')
    C = f.callout
    C('A', 130, 100, 60, 90, 'Clapper box', 'Housing on the tool head in which the clapper block is hinged', 'SHP-F026')
    C('B', 145, 72, 80, 50, 'Hinge pin', 'Pin about which the clapper block swings forward to lift the tool', 'SHP-F026')
    C('C', 170, 110, 250, 90, 'Clapper block', 'Carries the tool post; seated firmly on the cutting stroke, free to lift on the return', 'SHP-F026')
    C('D', 158, 200, 250, 160, 'Tool', 'Single-point tool that cuts only on the forward stroke', 'SHP-F004')
    C('E', 60, 275, 60, 230, 'Workpiece', 'Job held in the vice under the tool', 'SHP-F031')
    return f


def spt():
    f = Fig('shaping/spt-tool', 720, 400, 'Single-point cutting tool (shaper)',
            'Oblique line drawing of a single-point cutting tool with lettered features')
    # oblique box tool: shank to the right, cutting head to the left
    f.poly([(260, 150), (640, 110), (660, 130), (280, 170)], 'f')       # top of shank
    f.poly([(280, 170), (660, 130), (660, 210), (280, 250)], 'f')       # front of shank
    f.poly([(170, 190), (260, 150), (280, 170), (190, 210)], 'f2')      # face (rake) of head
    f.poly([(190, 210), (280, 170), (280, 250), (215, 285)], 'f')       # side flank (major)
    f.poly([(170, 190), (190, 210), (215, 285), (198, 280)], 'f')       # end flank (minor)
    f.line(170, 190, 190, 210)
    C = f.callout
    C('A', 500, 170, 520, 60, 'Shank', 'Body of the tool, clamped in the tool post', 'SHP-F038')
    C('B', 220, 182, 230, 90, 'Face', 'Top surface over which the chip slides', 'SHP-F038')
    C('C', 190, 210, 90, 260, 'Nose', 'Tip where the side and end cutting edges meet', 'SHP-F038')
    C('D', 235, 190, 330, 90, 'Side (major) cutting edge', 'Main cutting edge along the side of the tool', 'SHP-F038')
    C('E', 178, 198, 90, 150, 'End (minor) cutting edge', 'Cutting edge at the end of the tool', 'SHP-F038')
    C('F', 245, 240, 300, 330, 'Major (side) flank', 'Surface below the side cutting edge', 'SHP-F038')
    C('G', 202, 260, 120, 320, 'Minor (end) flank', 'Surface below the end cutting edge', 'SHP-F038')
    return f


def job(blank=False):
    f = Fig('shaping/job' + ('-q' if blank else ''), 640, 360, 'ME-106 shaping job' + (' — dimensions hidden' if blank else ''),
            'Oblique drawing of the rectangular block made on the shaper' + (', edges lettered' if blank else ', fully dimensioned'),
            ask={'p': 'In the shaping job drawing, edge {L} is the block\'s…'})
    k = 4.4
    L, W, H = 73 * k, 38 * k * 0.9, 21 * k
    x0, y0 = 120, 260
    dx, dy = W * 0.8, -W * 0.55
    front = [(x0, y0), (x0 + L, y0), (x0 + L, y0 - H), (x0, y0 - H)]
    f.poly(front, 'f')
    f.poly([(x0, y0 - H), (x0 + L, y0 - H), (x0 + L + dx, y0 - H + dy), (x0 + dx, y0 - H + dy)], 'f2')
    f.poly([(x0 + L, y0), (x0 + L + dx, y0 + dy), (x0 + L + dx, y0 - H + dy), (x0 + L, y0 - H)], 'f')
    if blank:
        f.tag('P', x0 + L / 2, y0 + 30); f.line(x0 + L / 2, y0 + 15, x0 + L / 2, y0 + 2, 'lead')
        f.tag('Q', x0 + L + dx / 2 + 30, y0 + dy / 2 + 15); f.line(x0 + L + dx / 2 + 16, y0 + dy / 2 + 8, x0 + L + dx / 2 + 3, y0 + dy / 2 + 2, 'lead')
        f.tag('R', x0 - 30, y0 - H / 2); f.line(x0 - 15, y0 - H / 2, x0 - 2, y0 - H / 2, 'lead')
        f.labels.update({'P': {'part': 'Length (73 mm)', 'function': '73 mm', 'fact': 'SHP-F044'},
                         'Q': {'part': 'Width (38 mm)', 'function': '38 mm', 'fact': 'SHP-F044'},
                         'R': {'part': 'Height / thickness (21 mm)', 'function': '21 mm', 'fact': 'SHP-F044'}})
    else:
        f.hdim(x0, x0 + L, y0 + 30, '73', 17, above=False)
        f.vdim(x0 - 25, y0 - H, y0, '21', 17)
        f.text(x0 + L + dx / 2 + 28, y0 + dy / 2 + 12, '38', 17)
        f.text(320, 30, 'All dimensions in mm', 15)
    return f


FIGS = [shaper, quick_return, clapper, spt, job, lambda: job(True)]
