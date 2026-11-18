"""Grinding question bank. Correct option first. Only unambiguous grit/grade/structure values are used
(sources disagree at class boundaries — see corrections.md #17–18)."""
from qlib import Bank

B = Bank('grinding')
q, n, s, tf, ar = B.q, B.n, B.s, B.tf, B.ar

# ============================ principle ============================
q('def', 'e', 'Grinding is a machining process in which material is removed by…',
  'A rotating abrasive wheel', ['A rotating multi-point HSS cutter', 'A reciprocating single-point tool', 'Electric sparks'],
  'A rotating abrasive wheel removes very small amounts of material.', [1])
q('theory', 'e', 'In a grinding wheel, what actually does the cutting?',
  'The abrasive grains, each acting as a tiny cutting edge', ['The bond material', 'The pores', 'The wheel guard'],
  'Abrasive grains act like thousands of tiny cutting tools; the bond only holds them.', [2, 42])
q('theory', 'm', 'Grinding is classed as a finishing process because it…',
  'Removes small amounts of material to give finish and accuracy', ['Removes large amounts of material quickly', 'Adds material to the surface', 'Joins two parts together'],
  'Machining (turning, milling) does bulk removal (semi-finishing); grinding does small removal (finishing).', [3])
s('theory', 'm', 'What is the usual sequence when making a hardened, precise part?',
  'Machining → heat treatment (if needed) → grinding', ['Grinding → machining → heat treatment', 'Heat treatment → grinding → machining', 'Machining → grinding → heat treatment'],
  'Machining roughs it out, heat treatment hardens it, then grinding finishes it to size (it can cut hardened material).', [4])
q('theory', 'e', 'Grinding is usually done…',
  'After turning or milling, when high precision and finish are needed', ['Before any other machining', 'Instead of heat treatment', 'Only on soft materials'],
  'Grinding follows other machining processes when high precision and a smooth finish are required.', [5])
q('theory', 'm', 'Which of these is NOT a value-addition process listed in the grinding lecture?',
  'Inspection', ['Forming', 'Metal addition', 'Melting and solidification'],
  'The four value-addition processes are forming, metal addition, melting and solidification, and metal removal.', [6])
q('theory', 'm', 'Welding belongs to which value-addition group?',
  'Metal addition (joining)', ['Metal removal', 'Forming', 'Melting and solidification only'],
  'The notes give welding as metal addition, forging as forming, moulding (casting) as melting and solidification, and cutting as metal removal.', [6])
q('theory', 'e', 'Which of these is a metal-removal process?',
  'Grinding', ['Casting', 'Forging', 'Welding'],
  'Metal-removal processes include turning, shaping, planing, drilling, milling, broaching, gear making, threading and grinding.', [7])
q('theory', 'm', 'In grinding, the abrasive particles are very hard (> 2000 kg/mm²). Cutting speeds are usually…',
  '30 m/s or higher', ['About 30 m/min', 'Below 1 m/s', 'About 300 m/s'],
  'Chips are very small and cutting speeds high, usually 30 m/s or more.', [8])
q('theory', 'h', 'Grinding is divided into two regimes. They are…',
  'Stock-removal grinding and form-and-finish grinding', ['Wet grinding and dry grinding', 'Rough grinding and polishing', 'Hand grinding and machine grinding'],
  'The cylindrical-grinding notes divide grinding into stock-removal grinding (SRG) and form-and-finish grinding (FFG).', [9])
q('theory', 'h', 'In stock-removal grinding (e.g. abrasive cut-off), why is periodic dressing unnecessary?',
  'Wheel wear is so rapid that the wheel is self-sharpening', ['The wheel is made of diamond', 'No chips are produced', 'The wheel never touches the work'],
  'In SRG the aim is fast removal regardless of finish; wheel wear is so high that fresh grains keep appearing.', [10])
q('theory', 'h', 'In form-and-finish grinding, the wheel must be…',
  'Dressed periodically to keep sharp, clean cutting edges', ['Never dressed', 'Run without coolant', 'Run at low speed only'],
  'FFG needs good form and finish, so the wheel is dressed periodically to remove wear flats and adhering metal.', [11])
q('theory', 'h', 'In vertical-spindle surface grinding, grinding is done with the…',
  'Face of the wheel', ['Periphery of the wheel', 'Bore of the wheel', 'Regulating wheel'],
  'In vertical-spindle surface grinding the work is on a rotary table and grinding takes place on the face of the wheel.', [12])

# ============================ grinding ratio / specific energy ============================
q('def', 'e', 'Grinding ratio G is defined as…',
  'Volume of work material removed ÷ volume of wheel wear', ['Volume of wheel wear ÷ volume of work removed', 'Wheel speed ÷ work speed', 'Wheel diameter ÷ wheel width'],
  'G = V_w / V_s: volume of material removed from the work per unit volume of wheel worn.', [13])
q('def', 'm', 'For surface grinding a block, the volume of work removed V_w is…',
  'l × b × Δh', ['π/4 × d × (Di² − Df²)', 'l × b × h', 'π × D × l'],
  'V_w = length × breadth × reduction in height (Δh), as written on the lab board.', [14])
q('def', 'm', 'The volume of wheel wear V_s is calculated as…',
  '(π/4) × d × (Di² − Df²)', ['(π/4) × d × (Di − Df)²', 'π × d × (Di − Df)', '(π/4) × (Di² − Df²)'],
  'The worn volume is the ring between the initial and final diameters times the wheel width d.', [15])
q('theory', 'm', 'A higher grinding ratio means…',
  'Less wheel wear for the same metal removed', ['More wheel wear for the same metal removed', 'A rougher surface finish', 'Lower cutting speed'],
  'G = V_w/V_s, so a higher G means the wheel lasts longer.', [16])
n('num', 'm', 'A grinding operation removes 6000 mm³ of steel while the wheel loses 300 mm³. What is the grinding ratio?',
  '20', ['0.05', '200', '5'],
  'G = V_w/V_s = 6000/300 = 20. Inverting the ratio gives 0.05.', [13])
n('num', 'h', 'A block 100 mm × 50 mm is surface-ground, reducing its height by 2 mm. The wheel (width 20 mm) wears from Ø200 to Ø199.95 mm. What is G (approximately)?',
  '≈ 32', ['≈ 25', '≈ 0.03', '≈ 320'],
  'V_w = 100 × 50 × 2 = 10 000 mm³. V_s = (π/4) × 20 × (200² − 199.95²) = 15.708 × 19.9975 ≈ 314 mm³. G = 10 000/314 ≈ 32. Leaving out π/4 gives ≈ 25.', [13, 14, 15], fig='grinding/grinding-ratio')
n('num', 'm', 'In surface grinding, a block 80 mm long and 40 mm wide has its height reduced by 0.5 mm. What volume of work is removed?',
  '1600 mm³', ['3200 mm³', '160 mm³', '120 mm³'],
  'V_w = l × b × Δh = 80 × 40 × 0.5 = 1600 mm³.', [14], fig='grinding/grinding-ratio')
q('def', 'e', 'Specific energy in machining means…',
  'Energy needed to remove a unit volume (1 mm³) of material', ['Energy stored in the wheel', 'Power of the motor', 'Energy lost in the coolant'],
  'Specific energy is the energy required to remove 1 mm³ of material.', [17])
q('theory', 'm', 'How does the specific energy of grinding compare with conventional machining?',
  'Much higher (≈ 15–50 J/mm³ vs ≈ 2–5 J/mm³)', ['Much lower', 'About the same', 'Zero, because grains are self-sharpening'],
  'The lab notes give 15–50 J/mm³ for grinding vs 2–5 J/mm³ for normal machining.', [18])
q('theory', 'h', 'Why is the specific energy of grinding so high?',
  'Very small chips, negative rake grains, rubbing and ploughing', ['The wheel rotates slowly', 'Only one grain cuts at a time', 'The work is always hardened'],
  'Most grains have large negative rake and many only rub or plough, so most energy turns into heat. That is why coolant is essential.', [19])
n('num', 'h', 'Grinding steel at a removal rate of 100 mm³/s with a specific energy of 30 J/mm³ needs a power of about…',
  '3 kW', ['0.3 kW', '30 kW', '3.33 W'],
  'Power = specific energy × removal rate = 30 J/mm³ × 100 mm³/s = 3000 W = 3 kW.', [17, 18])

# ============================ machines ============================
q('parts', 'e', 'Conventional grinding machines are broadly classified as…',
  'Surface, cylindrical and internal grinders', ['Up, down and climb grinders', 'Horizontal, vertical and universal shapers', 'Capstan, turret and engine grinders'],
  'The grinding lecture classifies machines as surface, cylindrical and internal (plus tool-and-cutter and centreless).', [20])
q('parts', 'e', 'A surface grinding machine is used to finish…',
  'Flat surfaces', ['External cylindrical surfaces', 'Internal bores', 'Long slender rods without centres'],
  'Surface grinding produces flat surfaces.', [21])
q('parts', 'm', 'Surface grinders are of two general types according to the table. They are…',
  'Reciprocating-table and rotating-table', ['Fixed-table and magnetic-table', 'Knee-type and bed-type', 'Push-type and draw-type'],
  'Surface grinders have a reciprocating table or a rotating table, each with a horizontal or vertical spindle.', [22])
q('parts', 'm', 'In a horizontal-spindle surface grinder, the depth of cut is set by…',
  'Moving the wheel head down', ['Moving the table sideways', 'Rotating the work', 'Tilting the column'],
  'The table moves back and forth; the wheel above is moved vertically to set the depth of cut.', [23])
q('app', 'm', 'Which is a typical application of surface grinding?',
  'Finishing machine beds, flat tools, gauges and dies', ['Finishing crankshafts', 'Grinding long pins without centres', 'Sharpening drills'],
  'Surface grinding finishes flat items such as machine beds, gauges and dies.', [25])
q('parts', 'e', 'A cylindrical grinding machine is used to finish…',
  'External cylindrical surfaces', ['Flat surfaces only', 'T-slots', 'Gear teeth'],
  'It grinds external cylindrical surfaces, which may be straight, tapered, stepped or profiled.', [26])
q('parts', 'm', 'In cylindrical grinding the work is held between centres (or in a chuck), and…',
  'The wheel rotates fast while the work rotates slowly', ['The work rotates fast while the wheel is stationary', 'Neither rotates', 'Only the table rotates'],
  'The wheel runs at high speed and the work rotates slowly.', [27])
q('parts', 'h', 'In a cylindrical grinder, which part is reciprocated (often by a hydraulic drive) to traverse the work past the wheel?',
  'The table carrying the headstock and tailstock', ['The wheel head only', 'The regulating wheel', 'The magnetic chuck'],
  'The table carrying the headstock, tailstock and work is reciprocated by a hydraulic drive.', [28])
q('parts', 'm', 'On a cylindrical grinder, the adjustable table dogs are used to…',
  'Set the limits (reversal points) of the table traverse', ['Hold the work between centres', 'Dress the wheel', 'Balance the wheel'],
  'The dogs on the table trip the reversing mechanism at the ends of the traverse.', [30])
q('parts', 'm', 'Which of these is NOT a part of a cylindrical grinder (from the ME-106 notes)?',
  'Clapper box', ['Headstock (work head)', 'Upper table', 'Adjustable dogs'],
  'The notes show headstock, workpiece, wheel, tailstock, upper and lower tables, adjustable dogs and base. The clapper box is on a shaper.', [29])
q('parts', 'm', 'A plain centre-type cylindrical grinder is most similar in layout to a…',
  'Centre lathe', ['Shaper', 'Drilling machine', 'Milling machine'],
  'The work is held between headstock and tailstock centres, much like on a centre lathe, and the disc wheel grinds with its periphery.', [31])
q('ops', 'm', 'In plunge grinding…',
  'The wheel is fed straight in without traverse', ['The work traverses past the wheel', 'The work is supported on a rest blade', 'The wheel face is used'],
  'Traverse grinding moves the work past the wheel; plunge grinding feeds the wheel straight in.', [32])
q('parts', 'h', 'What extra capability does a universal cylindrical grinder have over a plain one?',
  'Swivelling table, headstock and wheel head, plus an internal grinding attachment', ['A magnetic chuck', 'A regulating wheel', 'A ram and clapper box'],
  'The universal grinder can grind any taper and has an additional head for internal grinding.', [33])
q('app', 'm', 'Cylindrical grinding is typically used for…',
  'Shafts, rollers and precision bearings', ['Flat gauges and dies', 'Machine table T-slots', 'Sheet-metal cutting'],
  'Shafts, rollers and bearing races are ground on cylindrical grinders.', [34])
q('parts', 'e', 'Internal grinding is used to finish…',
  'The inside diameter (bore) of cylindrical work', ['Flat surfaces', 'Gear teeth', 'Threads on bolts'],
  'Internal grinding finishes bores with a small wheel running inside the hole.', [35])
q('parts', 'm', 'In centreless grinding, the work is supported by…',
  'A work-rest blade between the grinding and regulating wheels', ['Two centres', 'A three-jaw chuck', 'A magnetic chuck'],
  'No centres are used; the work rests on a blade and is controlled by the regulating wheel.', [36])
q('parts', 'm', 'In centreless grinding, the regulating wheel…',
  'Rotates slower than the grinding wheel and controls the work rotation', ['Rotates faster than the grinding wheel', 'Does the actual grinding', 'Is a diamond dresser'],
  'The rubber-bonded regulating wheel turns slowly and controls the speed of the work. Both wheels turn in the same direction.', [37])
q('parts', 'h', 'In through-feed centreless grinding, how is the axial movement of the work produced?',
  'By tilting the regulating wheel at a small angle', ['By a lead screw', 'By a reciprocating table', 'By the magnetic chuck'],
  'A slight tilt of the regulating wheel gives an axial component that feeds the work through.', [38])
q('app', 'm', 'Centreless grinding is best suited for…',
  'High-volume grinding of long slender rods and pins', ['Single flat plates', 'Large gear teeth', 'Cutting tool sharpening'],
  'It needs no centres or clamping, so it suits mass production of rods, pins and valve spools.', [39])
q('parts', 'e', 'Which grinder is used to sharpen drills, milling cutters and gear cutters?',
  'Tool-and-cutter grinder', ['Centreless grinder', 'Surface grinder', 'Internal grinder'],
  'Tool-and-cutter grinders sharpen and recondition cutting tools.', [40])
q('parts', 'h', 'A tool-post grinder is…',
  'A self-powered wheel head mounted on a lathe tool post', ['A grinder for the shaper tool post', 'A cylindrical grinder with a tool post', 'A hand grinder'],
  'It mounts on the lathe compound rest; the lathe spindle rotates the work and the carriage traverses the wheel.', [41])

# ============================ wheel ============================
q('wheel', 'e', 'Which three things make up a grinding wheel?',
  'Abrasive grains, bond and pores', ['Teeth, flutes and shank', 'Anode, cathode and electrolyte', 'Shank, face and flank'],
  'Grains cut, the bond holds them, and pores carry chips away and let coolant flow.', [42])
q('wheel', 'e', 'What is the correct order of a standard grinding-wheel marking?',
  'Abrasive – grain size – grade – structure – bond', ['Bond – grade – abrasive – structure – grain size', 'Grain size – abrasive – bond – grade – structure', 'Structure – bond – grade – grain size – abrasive'],
  'The standard order is abrasive, grain size, grade, structure, bond (with optional manufacturer\'s symbols before and after).', [43])
q('wheel', 'm', 'Decode the wheel marking A 46 K 5 V.',
  'Al₂O₃, medium grain, medium grade, structure 5, vitrified bond', ['SiC, fine grain, hard grade, open structure, resinoid bond', 'Al₂O₃, coarse grain, soft grade, open structure, rubber bond', 'Diamond, medium grain, medium grade, dense structure, metal bond'],
  'A = aluminium oxide; 46 = medium grit; K = medium grade; 5 = structure number; V = vitrified bond.', [44])
q('wheel', 'h', 'In the marking 51 A 60 K 5 V 05, what do "51" and "05" represent?',
  'Manufacturer\'s abrasive symbol and manufacturer\'s record (identifier)', ['Wheel diameter and bore', 'Maximum speed and grit size', 'Structure and grade'],
  'The prefix is the manufacturer\'s mark for the exact abrasive type; the suffix is the manufacturer\'s identifier.', [45])
q('wheel', 'm', 'The size of a grinding wheel is specified in the order…',
  'Diameter × thickness × bore', ['Bore × diameter × grit', 'Thickness × grade × bond', 'Diameter × grade × structure'],
  'Wheel size is given as diameter × thickness × bore (e.g. 200 × 25 × 31.75).', [46])
q('wheel', 'e', 'In grinding wheel marking, the letter C stands for…',
  'Silicon carbide', ['Cubic boron nitride', 'Carbon steel', 'Ceramic bond'],
  'A = aluminium oxide, C = silicon carbide, D = diamond; CBN has its own symbol. (The notebook wrongly put CBN under C.)', [47])
q('wheel', 'e', 'In grinding wheel marking, the letter A stands for…',
  'Aluminium oxide (alumina)', ['Aluminium metal', 'Abrasive of any type', 'Acid-resistant bond'],
  'A = aluminium oxide, the most widely used abrasive.', [47])
q('wheel', 'm', 'Which abrasive is generally used for grinding steels and other high-tensile ferrous metals?',
  'Aluminium oxide', ['Silicon carbide', 'Diamond', 'Boron carbide'],
  'Alumina is the most widely used abrasive, for steels, ferrous alloys and high-tensile materials.', [48])
q('wheel', 'm', 'Which abrasive is generally used for grinding cast iron and non-ferrous metals?',
  'Silicon carbide', ['Aluminium oxide', 'Cubic boron nitride', 'Zirconia–alumina'],
  'SiC is used for cast iron, non-ferrous metals and non-metals (low-tensile, brittle materials).', [49])
q('wheel', 'm', 'Diamond abrasive wheels are mainly used for…',
  'Very hard materials like carbides and ceramics', ['Soft aluminium', 'Mild steel shafts', 'Wood'],
  'Diamond is used for ceramics, carbides and final polishing, but it is costly.', [50])
q('wheel', 'h', 'Which abrasive is preferred for grinding hardened tool steels?',
  'Cubic boron nitride (CBN)', ['Silicon carbide', 'Diamond', 'Emery'],
  'CBN is a superabrasive suited to very hard ferrous materials such as hardened tool steels (diamond reacts with iron at high temperature).', [51])
q('wheel', 'm', 'The grain (grit) size number of a grinding wheel is based on…',
  'Number of openings per linear inch of the sieve', ['Weight of each grain in mg', 'Diameter of the wheel', 'Hardness of the bond'],
  'Grit number = sieve openings per linear inch; grains passing a finer sieve get a larger number.', [52])
q('wheel', 'e', 'A larger grit number on a grinding wheel means…',
  'Finer grains', ['Coarser grains', 'A harder bond', 'A more open structure'],
  'Larger number = finer grain size.', [52])
q('wheel', 'm', 'A wheel of grit size 24 is classed as…',
  'Coarse', ['Medium', 'Fine', 'Very fine'],
  'Grit 24 is coarse in all the lab sources.', [53])
q('wheel', 'm', 'A wheel of grit size 60 is classed as…',
  'Medium', ['Coarse', 'Fine', 'Very fine'],
  'Grit 60 is medium in all the lab sources.', [53])
q('wheel', 'm', 'A wheel of grit size 180 is classed as…',
  'Fine', ['Coarse', 'Medium', 'Very coarse'],
  'Grit 180 is fine in all the lab sources.', [53])
q('wheel', 'm', 'A wheel of grit size 400 is classed as…',
  'Very fine', ['Coarse', 'Medium', 'Fine'],
  'Grit 400 is very fine.', [53])
q('wheel', 'm', 'For precision finish grinding, which grain size would you choose?',
  'Fine', ['Coarse', 'Very coarse', 'It does not matter'],
  'Fine and very fine grains are used for precision grinding; coarse and medium for rough grinding.', [54])
q('wheel', 'e', 'The "grade" of a grinding wheel refers to…',
  'Strength (hardness) of the bond holding the grains', ['Hardness of the abrasive grains', 'Size of the grains', 'Spacing between the grains'],
  'Grade is the bond strength: how easily grains are released. It is not the hardness of the abrasive itself.', [55])
q('wheel', 'm', 'Grade letter E indicates a…',
  'Soft wheel', ['Medium wheel', 'Hard wheel', 'Very fine wheel'],
  'E is soft in every scale used in the lab sources.', [56])
q('wheel', 'm', 'Grade letter K indicates a…',
  'Medium wheel', ['Soft wheel', 'Hard wheel', 'Very hard wheel'],
  'K is medium grade.', [56])
q('wheel', 'm', 'Grade letter T indicates a…',
  'Hard wheel', ['Soft wheel', 'Medium wheel', 'Fine wheel'],
  'Grades Q–Z are hard (T falls well inside the hard range).', [56])
q('wheel', 'e', 'For grinding a HARD workpiece material, which grade of wheel is used?',
  'Soft grade', ['Hard grade', 'Any grade', 'Very hard grade'],
  'Soft wheel for hard work, hard wheel for soft work.', [57])
q('wheel', 'e', 'For grinding a SOFT workpiece material, which grade of wheel is used?',
  'Hard grade', ['Soft grade', 'Very soft grade', 'Any grade'],
  'Hard wheel for soft work: the grains stay sharp longer on soft material, so a strong bond keeps them in place.', [57])
q('wheel', 'h', 'Why is a soft-grade wheel used on hard work?',
  'Grains blunt quickly, so a weak bond releases them and exposes sharp grains', ['A soft wheel cuts faster on any material', 'Hard work needs a smoother wheel', 'Soft wheels produce no heat'],
  'On hard work, grains dull quickly. A soft bond lets them break out (self-sharpening) instead of glazing.', [58])
q('wheel', 'h', 'Which factor is NOT considered when selecting the grade of a grinding wheel?',
  'Colour of the wheel', ['Hardness of the work material', 'Area of contact with the work', 'Grinding speed'],
  'Grade selection depends on work hardness, grinding speed, contact area and machine capability.', [59])
q('wheel', 'e', 'The "structure" of a grinding wheel refers to…',
  'Spacing (porosity) between abrasive grains', ['Strength of the bond', 'Type of abrasive', 'Diameter of the wheel'],
  'Structure is how closely the grains are packed; it is shown by a number.', [60])
q('wheel', 'm', 'A higher structure number on a grinding wheel means…',
  'A more open structure (wider grain spacing)', ['A denser structure', 'A harder bond', 'Finer grains'],
  'Low number = dense; high number = open. (The notebook had this reversed; see corrections.md.)', [60])
q('wheel', 'm', 'Structure number 3 indicates a…',
  'Dense wheel', ['Open wheel', 'Soft wheel', 'Coarse wheel'],
  'Low structure numbers are dense in all sources.', [60])
q('wheel', 'm', 'Structure number 12 indicates a…',
  'Open wheel', ['Dense wheel', 'Hard wheel', 'Fine wheel'],
  'High structure numbers are open.', [60])
q('wheel', 'm', 'An open-structure wheel is recommended for…',
  'Rough grinding and soft, ductile materials', ['Hard, brittle materials and fine finish', 'Diamond dressing', 'Polishing glass'],
  'Open wheels have room for large chips (less loading). Dense wheels suit hard, brittle materials and fine finish.', [61])
q('wheel', 'e', 'In a grinding wheel, the bond…',
  'Holds the abrasive grains together in wheel form', ['Does the cutting', 'Is the coolant', 'Is the dresser'],
  'The bond is the adhesive that holds the grains together.', [62])
q('wheel', 'e', 'Bond letter V in a wheel marking stands for…',
  'Vitrified', ['Vulcanised rubber', 'Very hard', 'Vacuum-brazed metal'],
  'V = vitrified, the most common bond.', [63])
q('wheel', 'm', 'Bond letter B in a wheel marking stands for…',
  'Resinoid', ['Boron', 'Brass', 'Bakelite-free rubber'],
  'B = resinoid (resin), R = rubber, E = shellac, S = silicate, M = metal, V = vitrified.', [63])
q('wheel', 'm', 'Which pairing of bond letter and bond is correct?',
  'E – shellac', ['R – resinoid', 'S – shellac', 'M – rubber'],
  'E = shellac, R = rubber, S = silicate, M = metal, B = resinoid.', [63])
q('wheel', 'm', 'Why is vitrified bond the most widely used?',
  'Strong, rigid, porous, and unaffected by water, oil and acids', ['It is flexible for thin cut-off wheels', 'It is the cheapest rubber', 'It melts during use to self-sharpen'],
  'Vitrified (glass-like) bonds are strong and porous and resist coolants.', [64])
q('wheel', 'h', 'Which bond is used for the regulating wheel of a centreless grinder?',
  'Rubber (R)', ['Vitrified (V)', 'Shellac (E)', 'Silicate (S)'],
  'The regulating wheel is rubber-bonded, which gives it enough friction to control the work.', [65, 37])
q('wheel', 'h', 'Thin, high-speed abrasive cut-off wheels are usually made with which bond?',
  'Resinoid (or rubber)', ['Vitrified', 'Silicate', 'Oxychloride'],
  'Resinoid and rubber bonds are tough and slightly flexible, which suits thin cut-off wheels and high speeds.', [65])
q('wheel', 'm', 'In the notebook example "A 85 I 5 V", what do A and V denote?',
  'Aluminium oxide abrasive and vitrified bond', ['Silicon carbide abrasive and resinoid bond', 'Diamond abrasive and vitrified bond', 'Aluminium oxide abrasive and rubber bond'],
  'A = aluminium oxide, V = vitrified. 85 is a fine grit and 5 is the structure number.', [66])
q('wheel', 'm', 'In the notebook example "C 32 _ 8 B", what are the abrasive and bond?',
  'Silicon carbide and resinoid', ['Aluminium oxide and vitrified', 'CBN and resinoid', 'Silicon carbide and rubber'],
  'C = silicon carbide; B = resinoid. (The grade letter is illegible in the notes.)', [67])
q('wheel', 'h', 'Decode the wheel marking C 60 K 12 B.',
  'SiC, medium grain, medium grade, open structure, resinoid bond', ['Al₂O₃, fine grain, hard grade, dense structure, rubber bond', 'SiC, coarse grain, soft grade, dense structure, vitrified bond', 'CBN, medium grain, medium grade, open structure, metal bond'],
  'C = silicon carbide; 60 = medium grit; K = medium grade; 12 = open structure; B = resinoid bond.', [47, 53, 56, 60, 63])
q('wheel', 'h', 'Which marking would suit finish-grinding hardened steel?',
  'A 180 E 3 V', ['C 24 T 12 B', 'C 24 E 12 R', 'A 24 T 12 B'],
  'Steel → aluminium oxide (A); finish → fine grit (180); hard work → soft grade (E); dense structure (3) for a fine finish; vitrified bond.', [48, 54, 57, 61])

# ============================ wheel condition ============================
q('def', 'e', 'Dressing a grinding wheel means…',
  'Removing the dull outer layer to expose fresh sharp grains', ['Balancing the wheel on an arbor', 'Painting the wheel marking', 'Changing the bond type'],
  'Dressing sharpens the wheel by removing dull grains and embedded chips with a dresser.', [68])
q('def', 'm', 'Truing a grinding wheel means…',
  'Restoring its correct shape so it runs concentric', ['Sharpening its grains', 'Removing glazing only', 'Checking it for cracks'],
  'Truing makes the wheel round and true to its axis (usually with a diamond); dressing sharpens it.', [69])
q('def', 'm', 'Glazing of a grinding wheel is…',
  'Grains becoming blunt so the wheel surface turns smooth and shiny', ['Metal chips filling the pores', 'The wheel cracking', 'The bond softening'],
  'A glazed wheel has dull, shiny grains that rub instead of cut.', [70])
q('def', 'e', 'How can you identify a blunt (glazed) grinding wheel?',
  'Its surface looks shiny and smooth', ['It turns red', 'It sparks less brightly only', 'It becomes larger in diameter'],
  'The notes: a blunt wheel shows a shiny, smooth abrasive surface.', [71])
q('def', 'h', 'Glazing is most likely when…',
  'The wheel grade is too hard for the work', ['The wheel grade is too soft', 'The grit is too coarse', 'The coolant flow is excessive'],
  'A hard bond holds blunt grains too long, so they glaze. The remedy is to dress the wheel or use a softer grade.', [72])
q('def', 'm', 'Loading of a grinding wheel means…',
  'Chips of the work metal clog the pores of the wheel', ['The wheel surface becomes shiny from dull grains', 'The wheel is overloaded electrically', 'The wheel runs out of balance'],
  'Loading is clogging by metal particles, common when grinding soft ductile metals. Remedy: dress it and use a more open wheel.', [73])
q('def', 'm', 'Self-sharpening of a grinding wheel means…',
  'Blunt grains break away on their own, exposing new sharp grains', ['The wheel sharpens itself with coolant', 'The dresser is automatic', 'The wheel gets harder with use'],
  'When cutting forces on blunt grains exceed the bond strength, the grains break out and fresh ones take over.', [74])
q('def', 'm', 'Why must a grinding wheel be balanced before use?',
  'An unbalanced wheel causes vibration and chatter marks', ['To change its grade', 'To make it glaze', 'To reduce its diameter'],
  'Imbalance causes vibration (chatter), poor finish and danger. Wheels are balanced on a balancing stand.', [75])
q('def', 'h', 'Burn marks on a ground surface are usually caused by…',
  'Excessive heat, often from a dull wheel', ['Too much coolant', 'Too open a structure', 'Balancing the wheel'],
  'Burn marks come from overheating: a dull or glazed wheel, too heavy a cut, or poor coolant.', [76])
q('def', 'h', 'Chatter (vibration) marks on a ground surface are mainly due to…',
  'Wheel imbalance or a loose set-up', ['Fine grit size', 'Soft-grade wheel', 'Vitrified bond'],
  'Imbalance or loose machine set-up causes chatter marks.', [76, 75])

# ============================ advantages / applications ============================
q('adv', 'e', 'Which of these is an advantage of grinding?',
  'It can finish hard materials to good accuracy and finish', ['It is cheap with low power use', 'It needs no coolant', 'It removes large volumes quickly'],
  'Advantages: good surface finish, good dimensional accuracy, and hardness does not matter.', [77])
q('adv', 'm', 'Which of these is a disadvantage of grinding (from the ME-106 notes)?',
  'High specific energy, so high power is needed', ['Poor surface finish', 'Cannot grind hardened steel', 'Low dimensional accuracy'],
  'Disadvantages: costly, high specific energy (more power), and cooling is a must.', [78])
q('adv', 'm', 'Why is coolant essential in grinding?',
  'Most of the high grinding energy turns into heat', ['To make the wheel heavier', 'To lubricate the bond only', 'To magnetise the work'],
  'High specific energy means a lot of heat; coolant prevents burning, distortion and wheel damage.', [78, 19])
q('adv', 'm', 'Which is NOT a reason for using grinding?',
  'Bulk removal of large amounts of material cheaply', ['Micron-level accuracy', 'Mirror-like surface finish', 'Sharpening drills and cutters'],
  'Grinding is for finish, accuracy, hard materials, tool sharpening and burr removal, not cheap bulk removal.', [79])
q('app', 'm', 'Which is an application of grinding listed in the grinding slides?',
  'Finishing turbine blades and landing-gear parts', ['Casting engine blocks', 'Welding pipelines', 'Forging crankshaft blanks'],
  'Applications: automobile parts, tool sharpening, aerospace (turbine blades, landing gear), steel scale removal, electronics.', [80])

# ============================ lab job ============================
q('dims', 'e', 'What are the two objectives of the ME-106 grinding job?',
  'Surface-finish a flat face (surface grinder) and a cylindrical surface (cylindrical grinder)', ['Cut a spur gear and a keyway', 'Sharpen a drill and a lathe tool', 'Grind a thread and a cam'],
  'Objective 1: surface finish on a plane surface (surface grinder). Objective 2: surface finish on a cylindrical surface (cylindrical grinder).', [81, 82])
q('wmat', 'e', 'What workpieces are used in the ME-106 grinding job?',
  'A mild-steel cylindrical rod and a cubical block', ['An aluminium disc and a brass rod', 'A cast-iron bed and a copper plate', 'A HSS tool blank only'],
  'The grinding log sheet lists a mild-steel cylindrical rod and a cubical block.', [83])
q('tools', 'm', 'Which of these is in the ME-106 grinding log-sheet tool list?',
  'Vernier caliper', ['Dividing head', 'Hacksaw', 'Index plate'],
  'Tools: chuck, MS cylindrical rod, cubical block, Vernier caliper, grinding wheel, coolant and workpiece holder.', [84])
q('tools', 'm', 'Which item is NOT in the ME-106 grinding log-sheet tool list?',
  'Involute gear cutter', ['Grinding wheel', 'Coolant', 'Workpiece holder'],
  'The involute gear cutter belongs to the milling lab.', [84])
q('tools', 'm', 'In the ME-106 cylindrical grinding set-up, how is the job held?',
  'Between centres (dead centre at the tailstock)', ['In a machine vice', 'On the magnetic chuck', 'On a rest blade'],
  'The job drawing shows the cylindrical job held between centres.', [85])

# ============================ procedure ============================
q('proc', 'e', 'In surface grinding (ME-106 procedure), what must be done before placing the workpiece on the table?',
  'Clean the table (bed)', ['Dress the wheel to zero size', 'Start the coolant', 'Demagnetise the work'],
  'Step 2: clean the bed before placing the workpiece on it.', [87])
q('proc', 'm', 'Why are magnetic parallels placed around the workpiece in surface grinding?',
  'To stop the work shifting during grinding', ['To dress the wheel', 'To cool the work', 'To measure the height'],
  'Step 3: magnetic parallels around the work ensure it does not shift.', [88])
q('proc', 'e', 'In the ME-106 surface grinding procedure, how is the workpiece held on the table?',
  'By switching on the magnetic chuck', ['With a lathe dog', 'With a 4-jaw chuck', 'With clamping wire'],
  'Step 4: turn the magnetic chuck on to fix the workpiece.', [89])
q('proc', 'm', 'Before starting the surface grinder, the wheel is set…',
  'About an inch above the work, not touching it', ['Touching the work firmly', 'At the full depth of cut', 'Below the table level'],
  'Step 5–6: set the wheel about an inch above the work and make sure it is not in contact before starting.', [90])
q('proc', 'm', 'In the ME-106 surface grinding procedure, what is started along with the machine?',
  'Coolant', ['Dielectric pump', 'Laser', 'Index head'],
  'Step 6: adjust the handwheels as required and start the machine with coolant.', [91])
q('proc', 'm', 'At the end of surface grinding, what should you do before removing the workpiece?',
  'Wait for the wheel to stop, then demagnetise the chuck', ['Remove it while the wheel runs', 'Remove it with the chuck still magnetised', 'Dress the wheel first'],
  'Step 7: wait until the wheel stops, then remove the work by demagnetising the plate.', [92])
s('proc', 'h', 'Which is the correct order of the ME-106 surface grinding steps?',
  'Clean table → place work with magnetic parallels → magnetise chuck → set wheel clear → start with coolant → stop, demagnetise, remove',
  ['Magnetise chuck → clean table → start machine → place work → demagnetise',
   'Start with coolant → place work → clean table → magnetise chuck → remove',
   'Place work → start with coolant → clean table → set wheel clear → magnetise chuck'],
  'Log-sheet steps 1–7 in order.', [86, 87, 88, 89, 90, 91, 92])
q('proc', 'e', 'What is the first step of the ME-106 surface grinding procedure?',
  'Take the raw material whose surface is to be finished', ['Demagnetise the chuck', 'Dress the wheel', 'Start the coolant'],
  'Step 1: take the raw material for which surface finish is required.', [86])
q('proc', 'm', 'In the ME-106 cylindrical grinding procedure, the job must be…',
  'Held well centred on the machine', ['Placed on the magnetic chuck', 'Clamped in a vice', 'Hung on a wire'],
  'Step 2: hold the job well centred.', [93])
q('proc', 'm', 'In cylindrical grinding (ME-106), which comes first?',
  'Adjust the wheel position before starting the machine', ['Dress the wheel for fine finish', 'Remove the workpiece', 'Make the final cut'],
  'The wheel position is adjusted, then the coolant is started, before the trial cut.', [94])
q('proc', 'm', 'After the trial cut in cylindrical grinding, the size is checked with…',
  'An outside micrometer', ['A try square', 'A centre gauge', 'A surface plate'],
  'Step 3: take a trial cut and use an outside micrometer to correct the error.', [95])
q('proc', 'm', 'In the ME-106 cylindrical grinding procedure, the wheel is dressed…',
  'Before the final finishing passes, for a fine finish', ['After switching off the machine', 'Before placing the job', 'Never'],
  'Step 4: dress the wheel for fine finish, then finish the job.', [96])
s('proc', 'h', 'Which is the correct order for the ME-106 cylindrical grinding procedure?',
  'Hold job centred → adjust wheel → start coolant → trial cut and micrometer check → dress wheel → finish → remove job and switch off',
  ['Dress wheel → remove job → trial cut → hold job → start coolant',
   'Trial cut → hold job → finish → dress wheel → adjust wheel',
   'Start coolant → remove job → hold job → dress wheel → trial cut'],
  'Log-sheet cylindrical grinding steps in order.', [93, 94, 95, 96, 97])
q('proc', 'm', 'What is the LAST step in the ME-106 cylindrical grinding procedure?',
  'Remove the workpiece and switch off the machine', ['Take a trial cut', 'Dress the wheel', 'Adjust the wheel position'],
  'After the work is finished, remove the workpiece and turn off the machine.', [97])

# ============================ precautions ============================
q('prec', 'e', 'Which footwear and clothing does the ME-106 grinding log sheet require?',
  'Apron and leather (safety) shoes', ['Sandals and loose clothes', 'Gloves only', 'No special clothing'],
  'Always wear an apron and leather shoes for safety.', [98])
q('prec', 'e', 'Which accessories should NOT be worn while grinding?',
  'Bracelets, chains and wristwatches', ['Safety shoes', 'Apron', 'Safety goggles'],
  'Loose accessories such as bracelets and neck-chains can be caught.', [99])
q('prec', 'e', 'What should a student with long hair do before grinding?',
  'Tie it back', ['Leave it loose', 'Cover the wheel with it', 'Nothing'],
  'Long hair must be tied back, as stated on the grinding log sheet.', [100])
q('prec', 'm', 'Why must the material be fixed firmly on the grinding machine?',
  'A loose job can be thrown by the wheel', ['To speed up the wheel', 'To improve the bond', 'To reduce coolant use'],
  'Make sure the material is correctly fixed (magnetised or between centres) before grinding.', [101])
q('prec', 'm', 'Where should you stand when starting a grinding wheel?',
  'At a proper distance, to one side of the wheel', ['Directly in line with the wheel', 'Leaning over the wheel', 'In front of the guard opening'],
  'Keep a proper distance and stand to one side; if a wheel bursts, fragments fly in the plane of rotation.', [102])
q('prec', 'e', 'Before starting the grinder, you must check that…',
  'The wheel clears the work', ['The wheel is touching the work', 'The coolant is off', 'The magnetic chuck is off'],
  'Check that the wheel clears the work before starting.', [103])
q('prec', 'm', 'According to the grinding slides, the machine should not be operated…',
  'Without the shop instructor\'s supervision', ['With coolant', 'With safety shoes', 'With the guard fitted'],
  'Stay attentive and never operate without supervision.', [104])
q('prec', 'm', 'Why must the wheel guard be kept in place and goggles worn while grinding?',
  'Sparks and abrasive particles fly off the wheel', ['To keep the wheel clean', 'To increase the speed', 'To reduce noise only'],
  'Sparks, grit and (rarely) wheel fragments fly off, so the guard and goggles protect the operator.', [105])
q('prec', 'h', 'Before mounting a new grinding wheel, which checks are essential?',
  'Ring test for cracks, and maximum safe speed marked on the wheel', ['Grit colour and wheel weight', 'Grade letter only', 'Coolant temperature'],
  'A cracked wheel can burst. Tap it (ring test) and never exceed the marked maximum speed.', [106])
q('prec', 'm', 'Which of these is NOT a grinding-shop precaution?',
  'Remove the workpiece while the wheel is still running', ['Wear an apron and leather shoes', 'Check that the wheel clears the work', 'Tie long hair back'],
  'Wait until the wheel stops before removing the work. The others are log-sheet precautions.', [92, 98, 103, 100])

# ============================ AR / TF ============================
ar('wheel', 'h', 'A soft-grade wheel is used for grinding hard materials.',
   'In a soft wheel, blunt grains are released easily, exposing fresh sharp grains.', 'a',
   'Both true, and R explains A.', [57, 58])
ar('wheel', 'h', 'A higher structure number means a denser wheel.',
   'Structure describes the spacing between grains.', 'd',
   'A is false: a higher number means more open. R is true.', [60])
ar('theory', 'h', 'Coolant is essential in grinding.',
   'The specific energy of grinding is much higher than that of turning.', 'a',
   'Both true, R explains A: high specific energy becomes heat, which coolant removes.', [78, 18])
tf('wheel', 'e', 'In grinding wheel marking, the grade refers to the hardness of the abrasive grains themselves.', False,
   'False. Grade refers to the strength of the bond holding the grains.', [55])
tf('theory', 'm', 'Grinding can finish hardened steel that ordinary cutting tools cannot machine easily.', True,
   'True. Hardness does not matter for grinding, which is one of its key advantages.', [77])
tf('parts', 'm', 'In centreless grinding, the grinding wheel and regulating wheel rotate in opposite directions.', False,
   'False. Both wheels rotate in the same direction; the regulating wheel turns much slower.', [37])

# ============================ diagrams ============================
B.labels('grinding/surface-grinder', 'p', diffs={'p': 'e'})
B.labels('grinding/surface-grinder', 'w', only={'w': ['C', 'E', 'G', 'I']})
B.labels('grinding/surface-grinder', 'f', only={'f': ['B', 'E', 'C']}, diffs={'f': 'm'})
B.labels('grinding/cylindrical-grinder', 'p', diffs={'p': 'm'}, extra_parts=['Magnetic chuck', 'Regulating wheel'])
B.labels('grinding/cylindrical-grinder', 'f', only={'f': ['H', 'F', 'C']}, diffs={'f': 'm'})
B.labels('grinding/types', 'p', cat='parts', diffs={'p': 'e'}, extra_parts=['Tool-and-cutter grinding', 'Creep-feed grinding'])
TY = 'grinding/types'
q('parts', 'm', 'In the figure, which panel shows grinding where the work is NOT held between centres or in a chuck?', 'D', ['A', 'B', 'C'],
  'D is centreless grinding: the work rests on a blade between the grinding wheel and the regulating wheel.', [36], fig=TY)
q('parts', 'm', 'In the figure, which panel would be used to finish a bore?', 'C', ['A', 'B', 'D'],
  'C is internal grinding: a small wheel runs inside the bore.', [35], fig=TY)
B.labels('grinding/wheel-marking', 'p', cat='wheel', diffs={'p': 'm'})
WM = 'grinding/wheel-marking'
q('wheel', 'm', 'In the wheel marking shown, which position would read "C" for a silicon carbide wheel?', '1', ['2', '3', '5'],
  'Position 1 is the abrasive type (A = aluminium oxide, C = silicon carbide).', [47, 43], fig=WM)
q('wheel', 'm', 'In the wheel marking shown, what does "5" at position 4 tell you?', 'The structure (grain spacing) number', ['The grit size', 'The grade', 'The bond type'],
  'Position 4 is the structure. A low number like 5 is fairly dense.', [60], fig=WM)
q('wheel', 'm', 'In the wheel marking shown, "K" at position 3 means the wheel is…', 'Medium grade', ['Soft grade', 'Hard grade', 'Fine grain'],
  'Position 3 is grade; K is medium.', [56], fig=WM)
B.labels('grinding/structure', 'p', cat='wheel', diffs={'p': 'm'}, extra_parts=['Glazed wheel', 'Loaded wheel'])
q('wheel', 'h', 'Which wheel in the figure is better for rough grinding of a soft ductile metal?', 'B', ['A'],
  'B is the open structure: large pores hold the chips, so the wheel does not load up.', [61], fig='grinding/structure')
B.labels('grinding/dressing', 'p', cat='wheel', diffs={'p': 'm'}, extra_parts=['Magnetic parallel', 'Work-rest blade'])
q('def', 'm', 'What operation is being performed in the figure?', 'Dressing the grinding wheel', ['Balancing the grinding wheel', 'Surface grinding a block', 'Centreless grinding'],
  'A diamond dresser is fed across the rotating wheel to remove dull grains and true its face.', [68, 69], fig='grinding/dressing')

# ============================ tools & accessories (standard) ============================
q('tools', 'm', 'Which dresser is used for precise dressing and truing of a grinding wheel?',
  'Single-point diamond dresser', ['Star-wheel (Huntington) dresser', 'File card', 'Centre punch'],
  'A diamond dresser gives precise truing and dressing; a star-wheel dresser is for rough dressing.', [107])
q('tools', 'h', 'A star-wheel (Huntington) dresser is mainly used for…',
  'Rough dressing of coarse wheels', ['Precision truing of fine wheels', 'Balancing wheels', 'Measuring grit size'],
  'Star-wheel dressers crush and break out dull grains on coarse wheels; for precision a diamond is used.', [107])
q('tools', 'm', 'A grinding wheel is balanced using…',
  'A balancing stand with balance weights in the flange', ['A magnetic chuck', 'A dial on the wheel head', 'The table dogs'],
  'The wheel on its arbor is placed on knife edges or rollers, and the flange weights are moved until it stays put in any position.', [108])
q('tools', 'm', 'Which workpiece CANNOT be held directly on a magnetic chuck?',
  'Aluminium block', ['Mild-steel block', 'Cast-iron block', 'Tool-steel plate'],
  'Magnetic chucks hold only ferromagnetic materials. Aluminium or brass needs a vice or fixture.', [109, 89])
q('tools', 'm', 'Grinding coolant is usually…',
  'A water-based soluble-oil emulsion', ['Kerosene', 'Deionised water only', 'Molten wax'],
  'A soluble-oil emulsion cools, washes away swarf and reduces loading. (Deionised water is the dielectric in wire EDM.)', [110])
q('tools', 'h', 'When mounting a grinding wheel on its spindle, what is placed between the flanges and the wheel?',
  'Soft paper or rubber washers (blotters)', ['Steel shims', 'Magnetic parallels', 'Emery paper'],
  'Blotters spread the clamping pressure evenly; the flanges must be equal size and the nut only snug.', [111])
q('tools', 'h', 'In the ring test, a sound vitrified wheel tapped with a wooden mallet gives…',
  'A clear ringing sound', ['A dull thud', 'No sound at all', 'Sparks'],
  'A clear ring means the wheel is sound; a dull sound suggests a crack, so the wheel must not be used.', [112, 106])
q('tools', 'e', 'Which tool is used in the ME-106 cylindrical grinding procedure to check the size after the trial cut?',
  'Outside micrometer', ['Steel rule only', 'Try square', 'Dial-less caliper'],
  'The log sheet says to take a trial cut and use an outside micrometer to correct the error.', [95])
q('tools', 'm', 'Which accessory keeps a steel block from shifting on the surface grinder in the ME-106 procedure?',
  'Magnetic parallels', ['Lathe dog', 'Spacer collars', 'Clapper box'],
  'Magnetic parallels are placed around the workpiece on the magnetic chuck.', [88])
q('prec', 'm', 'On a pedestal (bench) grinder, the work rest should be set…',
  'Close to the wheel, about 2–3 mm', ['Far from the wheel, about 25 mm', 'Touching the wheel', 'Removed for better access'],
  'A large gap lets the work be dragged between the rest and the wheel, which can jam or break the wheel.', [113])
q('prec', 'm', 'When tightening the spindle nut on a newly mounted grinding wheel, you should…',
  'Tighten only enough to hold the wheel firmly', ['Tighten as hard as possible with an extension bar', 'Leave it loose', 'Hammer the flange'],
  'Over-tightening can crack the wheel; use equal flanges and blotters.', [111])
q('proc', 'h', 'An aluminium block is to be surface ground. How should it be held?',
  'In a vice or fixture on the table (not directly on the magnetic chuck)', ['Directly on the magnetic chuck', 'Between centres', 'On a rest blade'],
  'Aluminium is non-magnetic, so the magnetic chuck cannot hold it.', [109])

B.save()
