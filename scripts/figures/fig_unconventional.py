import math
from figlib import Fig


def wedm():
    f = Fig('unconventional/wedm', 780, 520, 'Wire-cut EDM — schematic',
            'Schematic of a wire EDM: wire runs from a supply spool through upper and lower guides past the workpiece to a take-up, with a pulse power supply, dielectric nozzles and an X–Y table')
    f.circle(110, 90, 45, 'f'); f.circle(110, 90, 10, 'k')                      # supply spool
    f.circle(110, 440, 45, 'f'); f.circle(110, 440, 10, 'k')                    # take-up spool
    # wire path
    f.line(150, 75, 380, 75); f.line(380, 75, 380, 470); f.line(380, 470, 150, 455)
    f.rect(350, 120, 60, 40, 'f2'); f.rect(350, 380, 60, 40, 'f2')             # upper / lower guides (with nozzles)
    f.poly([(365, 160), (395, 160), (388, 178), (372, 178)], 'f')              # upper nozzle
    f.poly([(365, 380), (395, 380), (388, 362), (372, 362)], 'f')              # lower nozzle
    f.rect(240, 230, 280, 100, 'f')                                            # workpiece
    f.rect(377, 230, 6, 100, 'k')                                              # kerf (cut slot) behind the wire
    f.rect(200, 330, 360, 22, 'f2')                                            # X-Y table
    f.arrow(470, 364, 540, 364, 'acc'); f.arrow(540, 364, 470, 364, 'acc')
    f.rect(600, 200, 130, 80, 'f2', rx=6); f.text(665, 228, 'Pulse', 15, weight='bold'); f.text(665, 250, 'generator', 15, weight='bold')
    f.text(612, 300, '−  wire', 14, anchor='start'); f.text(612, 318, '+  work', 14, anchor='start')
    f.line(600, 220, 420, 140, 'thin'); f.line(600, 265, 520, 280, 'thin')
    f.rect(600, 400, 130, 60, 'f2', rx=6); f.text(665, 430, 'CNC / servo', 15, weight='bold')
    f.line(600, 430, 560, 345, 'thin')
    C = f.callout
    C('A', 110, 90, 40, 40, 'Wire supply spool', 'Feeds fresh wire continuously; the wire is used only once', 'UCM-F024')
    C('B', 410, 140, 470, 110, 'Upper wire guide', 'Guides the wire accurately above the job (can tilt for taper cuts)', 'UCM-F025')
    C('C', 410, 400, 470, 440, 'Lower wire guide', 'Guides the wire accurately below the job', 'UCM-F025')
    C('D', 380, 200, 300, 180, 'Wire electrode', 'Thin brass wire (≈0.05–0.3 mm) that sparks against the job without touching it', 'UCM-F022')
    C('E', 300, 280, 200, 260, 'Workpiece', 'Must be electrically conductive; held on the table', 'UCM-F014')
    C('F', 395, 170, 470, 190, 'Dielectric nozzle', 'Flushes deionised water through the gap to cool and remove debris', 'UCM-F020')
    C('G', 540, 341, 640, 360, 'X–Y worktable', 'Moves the job along the programmed profile under CNC control', 'UCM-F015')
    C('H', 665, 240, 760, 160, 'Pulse power supply', 'Applies pulsed DC voltage between wire and work (Ton / Toff)', 'UCM-F012')
    C('I', 665, 430, 760, 490, 'CNC / servo control', 'Follows the part program and keeps the spark gap constant', 'UCM-F010')
    C('J', 110, 440, 40, 500, 'Used-wire take-up', 'Collects the eroded wire, which is not reused', 'UCM-F024')
    C('K', 380, 290, 300, 400, 'Kerf (cut slot)', 'Width = wire diameter + 2 × spark gap', 'UCM-F026')
    return f


def spark_gap():
    f = Fig('unconventional/spark-gap', 760, 400, 'Spark gap close-up',
            'Enlarged section through the wire and the cut: wire, spark gap, dielectric, a spark, craters and debris, with the kerf width dimensioned')
    f.rect(40, 60, 680, 300, 'f')                                    # workpiece
    f.rect(300, 60, 160, 300, 'thin')                                # kerf boundary
    f.raw('<rect x="301" y="61" width="158" height="298" fill="#4dabf7" fill-opacity="0.18" stroke="none"/>')
    f.circle(380, 210, 55, 'f2')                                     # wire section
    f.path('M435,210 l12,-8 l-6,16 l14,-10', 'acc')                  # spark
    for (cx, cy) in [(455, 150), (455, 270), (305, 180), (305, 245)]:
        f.arc(cx + (5 if cx > 400 else -5), cy, 8, 90 if cx > 400 else -90, 270 if cx > 400 else 90, 's')
    for (x, y) in [(330, 120), (420, 300), (350, 310), (430, 110)]:
        f.circle(x, y, 3, 'k')
    f.hdim(300, 460, 385, '', 14, above=False)
    f.hdim(325, 435, 30, '', 14)
    C = f.callout
    C('A', 380, 210, 380, 140, 'Wire electrode (diameter d)', 'Moving brass wire; never touches the job', 'UCM-F008')
    C('B', 447, 210, 560, 120, 'Spark gap (g)', 'Small gap kept constant by the servo; sparks jump across it', 'UCM-F009')
    C('C', 440, 205, 560, 210, 'Spark (discharge)', 'Pulse of energy that melts and vaporises a tiny bit of metal', 'UCM-F007')
    C('D', 460, 270, 560, 300, 'Crater', 'Small pit left by each spark on the cut surface', 'UCM-F032')
    C('E', 330, 120, 220, 110, 'Debris', 'Eroded particles flushed away by the dielectric', 'UCM-F020')
    C('F', 380, 30, 520, 30, 'Wire diameter (d)', 'Size of the wire electrode', 'UCM-F023')
    C('G', 380, 385, 520, 385, 'Kerf width', 'Kerf = d + 2g', 'UCM-F026')
    C('H', 320, 330, 200, 330, 'Dielectric (deionised water)', 'Insulates until breakdown, cools and flushes the gap', 'UCM-F018')
    return f


def laser_head():
    f = Fig('unconventional/laser-head', 720, 520, 'Fiber laser cutting head',
            'Section of a laser cutting head: fiber input, collimating lens, focusing lens, assist-gas inlet and nozzle above the sheet, with focal point, stand-off and kerf')
    f.rect(330, 20, 60, 40, 'f2')                                         # fiber connector
    f.poly([(300, 60), (420, 60), (420, 330), (395, 360), (325, 360), (300, 330)], 's')   # head body
    f.raw('<polygon points="352,60 368,60 400,150 400,170 320,170 320,150" fill="#e8590c" fill-opacity="0.18"/>')
    f.raw('<polygon points="320,190 400,190 362,420 358,420" fill="#e8590c" fill-opacity="0.22"/>')
    f.path('M315,150 Q360,135 405,150 Q360,165 315,150 Z', 'f2')          # collimator lens
    f.path('M315,190 Q360,170 405,190 Q360,210 315,190 Z', 'f2')          # focusing lens
    f.poly([(325, 360), (395, 360), (372, 400), (348, 400)], 'f')         # nozzle
    f.rect(420, 280, 90, 18, 'f'); f.arrow(520, 289, 425, 289, 'acc')     # gas inlet
    f.rect(80, 430, 560, 30, 'f')                                         # sheet
    f.rect(356, 430, 8, 30, 'k')                                          # kerf
    for k in range(4):
        f.circle(355 + (k % 2) * 10, 470 + k * 10, 3, 'k')                # ejected molten metal
    f.circle(360, 420, 4, 'k')
    f.vdim(250, 400, 430, '', 14)
    C = f.callout
    C('A', 360, 35, 470, 30, 'Optical fiber input', 'Delivers the 1.06 µm beam from the fiber laser source', 'UCM-F043')
    C('B', 400, 150, 500, 130, 'Collimating lens', 'Makes the diverging beam from the fiber parallel', 'UCM-F050')
    C('C', 400, 190, 500, 200, 'Focusing lens', 'Focuses the beam to a tiny, intense spot', 'UCM-F050')
    C('D', 505, 289, 600, 250, 'Assist-gas inlet', 'Supplies O₂, N₂ or air to blow molten metal out of the kerf', 'UCM-F045')
    C('E', 372, 385, 480, 380, 'Nozzle', 'Directs the assist gas coaxially with the beam', 'UCM-F050')
    C('F', 360, 420, 200, 380, 'Focal point', 'Smallest, most intense spot, set on or just in the sheet', 'UCM-F049')
    C('G', 250, 415, 140, 410, 'Stand-off distance', 'Gap between the nozzle tip and the sheet surface', 'UCM-F051')
    C('H', 360, 445, 480, 490, 'Kerf', 'Narrow slot (a few tenths of a mm) cut through the sheet', 'UCM-F052')
    C('I', 365, 490, 250, 505, 'Molten metal ejected', 'Blown out by the assist-gas jet', 'UCM-F037')
    return f


def jobs(blank=False):
    f = Fig('unconventional/jobs' + ('-q' if blank else ''), 720, 340, 'ME-106 unconventional machining jobs' + (' — dimensions hidden' if blank else ''),
            'Panel A: a square plate cut on wire EDM; panel B: a ring cut on the fiber laser' + ('' if blank else ', with dimensions'),
            ask={'p': 'Which machine was used for the job in panel {L}?', 'w': 'Which panel shows the job made on the {P}?'})
    f.rect(20, 20, 330, 300, 'thin', rx=8); f.rect(370, 20, 330, 300, 'thin', rx=8)
    k = 15
    f.rect(110, 90, 10 * k, 10 * k, 'f')
    f.poly([(260, 90), (285, 72), (285, 222), (260, 240)], 'f2')     # 5 mm thickness edge (oblique)
    f.poly([(110, 90), (135, 72), (285, 72), (260, 90)], 'f2')
    if not blank:
        f.hdim(110, 260, 270, '10', 16, above=False); f.vdim(90, 90, 240, '10', 16); f.text(305, 160, '5', 16)
    f.circle(535, 165, 100, 'f'); f.raw('<circle cx="535" cy="165" r="55" fill="#ffffff" stroke="currentColor" stroke-width="2"/>')
    f.panel('A', 45, 45, 'Wire-cut EDM', 'Square 10 mm × 10 mm, 5 mm thick', 'UCM-F059')
    f.panel('B', 395, 45, 'Fiber laser cutting machine', 'Ring (annulus) cut from metal sheet', 'UCM-F060')
    return f


def edm_compare():
    f = Fig('unconventional/edm-compare', 720, 340, 'Die-sinking EDM vs wire EDM',
            'Two sketches: a shaped electrode sinking a cavity into a block, and a thin wire cutting a through-profile',
            ask={'p': 'Which process is shown in panel {L}?', 'w': 'Which panel shows {P}?'})
    f.rect(20, 20, 330, 300, 'thin', rx=8); f.rect(370, 20, 330, 300, 'thin', rx=8)
    f.rect(90, 180, 190, 110, 'f'); f.rect(150, 70, 70, 80, 'f2'); f.poly([(150, 150), (220, 150), (205, 180), (165, 180)], 'f2')
    f.raw('<path d="M165,180 L205,180 L195,205 L175,205 Z" fill="#ffffff" stroke="currentColor" stroke-width="2"/>')
    f.arrow(185, 45, 185, 68, 'acc')
    f.rect(440, 150, 190, 110, 'f'); f.line(535, 50, 535, 300); f.rect(530, 150, 10, 110, 'k')
    f.arrow(560, 290, 610, 290, 'acc')
    f.panel('A', 45, 45, 'Die-sinking EDM', 'Shaped (copper/graphite) electrode sinks a 3-D cavity, usually in oil', 'UCM-F036')
    f.panel('B', 395, 45, 'Wire EDM', 'Moving thin wire cuts a 2-D through-profile, usually in deionised water', 'UCM-F036')
    return f


FIGS = [wedm, spark_gap, laser_head, jobs, lambda: jobs(True), edm_compare]
