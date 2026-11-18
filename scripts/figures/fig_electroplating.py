from figlib import Fig


def cell():
    f = Fig('electroplating/cell', 760, 460, 'Electroplating cell',
            'Line diagram of an electroplating cell: DC source with meters, anode, workpiece, electrolyte in a tank, and ion-flow arrows')
    f.poly([(120, 180), (120, 420), (640, 420), (640, 180)], 's', closed=False)     # tank
    f.rect(122, 230, 516, 188, 'f')                                                 # electrolyte
    f.line(122, 230, 638, 230, 'thin')
    f.rect(330, 40, 100, 60, 'f2', rx=6)                                           # DC source
    f.text(380, 70, 'DC', 20, weight='bold')
    f.text(322, 118, '+', 24, weight='bold'); f.text(440, 118, '−', 24, weight='bold')
    f.circle(250, 70, 18, 's'); f.text(250, 70, 'A', 16, weight='bold')            # ammeter (in series, + lead)
    f.circle(380, 150, 18, 's'); f.text(380, 150, 'V', 16, weight='bold')          # voltmeter across
    f.rect(200, 190, 40, 200, 'f2')                                                 # anode (left)
    f.rect(500, 200, 30, 170, 'f')                                                  # cathode workpiece (right)
    f.line(345, 100, 345, 70); f.line(330, 70, 268, 70); f.line(232, 70, 220, 70); f.line(220, 70, 220, 190)
    f.line(415, 100, 415, 70); f.line(430, 70, 515, 70); f.line(515, 70, 515, 200)
    f.line(345, 100, 345, 150); f.line(345, 150, 362, 150); f.line(398, 150, 415, 150); f.line(415, 150, 415, 100)
    for y in (260, 300, 340):
        f.arrow(255, y, 485, y, 'acc')
        f.text(370, y - 12, 'M⁺', 15)
    C = f.callout
    C('A', 220, 300, 80, 300, 'Anode (metal to be deposited)', 'Connected to the + terminal; dissolves into the bath to replace the metal ions', 'ELP-F004')
    C('B', 515, 300, 690, 300, 'Cathode (workpiece)', 'Connected to the − terminal; metal ions deposit on it', 'ELP-F003')
    C('C', 600, 380, 700, 420, 'Electrolyte (bath)', 'Solution containing ions of the plating metal', 'ELP-F009')
    C('D', 428, 50, 520, 25, 'DC power source', 'Supplies direct current of variable voltage and current', 'ELP-F006')
    C('E', 250, 52, 170, 30, 'Ammeter', 'Connected in series to measure the plating current', 'ELP-F008')
    C('F', 394, 162, 470, 165, 'Voltmeter', 'Connected across the cell to measure voltage', 'ELP-F008')
    C('G', 140, 410, 60, 430, 'Tank', 'Container holding the electrolyte', 'ELP-F007')
    return f


def flow():
    steps = [('Mechanical cleaning (emery paper)', 'Removes rust and burrs from the mild-steel job', 'ELP-F056'),
             ('Polishing / buffing (cotton mop + emery compound)', 'Smooths and shines the surface before plating', 'ELP-F056'),
             ('Chemical cleaning (6 V, 10–15 A, ~5 min)', 'Removes grease and contaminants in the cleaning bath', 'ELP-F057'),
             ('Washing with water and pumice powder', 'Removes cleaning chemicals before plating', 'ELP-F057'),
             ('Copper plating (2–6 V, 25–30 s)', 'Deposits a copper base layer until the job turns reddish', 'ELP-F058'),
             ('Nickel plating (1.5–3 V, 5–7 min)', 'Half the job is dipped to deposit a bright nickel layer', 'ELP-F059')]
    f = Fig('electroplating/process-flow', 760, 520, 'ME-106 electroplating sequence',
            'Six blank boxes in a column joined by arrows, each lettered; the steps are not written in the boxes',
            ask={'p': 'In the ME-106 electroplating sequence shown, what is step {L}?', 'w': 'Which box in the sequence is {P}?'})
    for i, (nm, fn, fa) in enumerate(steps):
        y = 20 + i * 82
        f.rect(250, y, 260, 56, 'f', rx=10)
        L = 'ABCDEF'[i]
        f.tag(L, 380, y + 28)
        f.labels[L] = {'part': nm.split(' (')[0], 'function': fn, 'fact': fa}
        if i < 5:
            f.arrow(380, y + 58, 380, y + 80, 's')
    return f


def electroclean():
    f = Fig('electroplating/electrocleaning', 700, 380, 'Electrochemical cleaning',
            'Cell in which the workpiece is connected to the positive terminal and gas bubbles form on it')
    f.poly([(120, 120), (120, 340), (580, 340), (580, 120)], 's', closed=False)
    f.rect(122, 160, 456, 178, 'f')
    f.rect(290, 60, 120, 50, 'f2', rx=6); f.text(350, 85, 'DC', 18, weight='bold')
    f.text(300, 125, '+', 20, weight='bold'); f.text(400, 125, '−', 20, weight='bold')
    f.rect(220, 150, 30, 160, 'f2')           # workpiece (anode here)
    f.rect(450, 150, 30, 160, 'f')            # counter electrode (cathode)
    f.line(300, 110, 300, 100); f.line(300, 100, 235, 100); f.line(235, 100, 235, 150)
    f.line(400, 110, 400, 100); f.line(400, 100, 465, 100); f.line(465, 100, 465, 150)
    for (x, y) in [(258, 200), (262, 240), (256, 280), (266, 220), (270, 260)]:
        f.circle(x, y, 5, 's')
    C = f.callout
    C('A', 235, 240, 80, 240, 'Workpiece (made the anode)', 'In electro-cleaning the job is the + electrode — the reverse of plating', 'ELP-F027')
    C('B', 266, 220, 360, 210, 'Oxygen gas bubbles', 'O₂ released at the job (4OH⁻ → 2H₂O + O₂ + 4e⁻) scrubs off rust and dirt', 'ELP-F028')
    C('C', 465, 240, 620, 240, 'Cathode (counter electrode)', 'Connected to the − terminal', 'ELP-F027')
    return f


def buffing():
    f = Fig('electroplating/buffing', 720, 360, 'Buffing (polishing) machine',
            'Double-ended bench polishing machine with cloth wheels and a compound bar')
    f.rect(270, 120, 180, 90, 'f', rx=20)        # motor
    f.line(150, 165, 570, 165)                    # spindle
    for cx in (140, 580):
        f.circle(cx, 165, 70, 'f2')
        for r in (20, 35, 50, 62):
            f.circle(cx, 165, r, 'thin')
    f.poly([(320, 210), (400, 210), (420, 320), (300, 320)], 'f')   # pedestal
    f.rect(600, 250, 70, 26, 'f')                 # compound bar
    C = f.callout
    C('A', 140, 120, 60, 40, 'Buffing wheel (cloth mop)', 'Rotating cloth wheel charged with abrasive compound', 'ELP-F022')
    C('B', 635, 263, 680, 320, 'Buffing compound bar', 'Fine abrasive (alumina, SiC, iron/chromium oxide) in a wax or soap binder', 'ELP-F023')
    C('C', 360, 140, 360, 60, 'Motor', 'Drives the wheels at high speed', 'ELP-F053')
    return f


FIGS = [cell, flow, electroclean, buffing]
