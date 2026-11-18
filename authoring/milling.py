"""Milling question bank. Correct option is always written first."""
from qlib import Bank

B = Bank('milling')
q, n, s, tf, ar = B.q, B.n, B.s, B.tf, B.ar
WD_NOTE = ' (The lab calls 2.157/DP the "working depth"; textbooks call it the whole depth.)'

# ============================ principle ============================
q('def', 'e', 'Milling removes metal using a…',
  'Rotating multi-point cutter', ['Reciprocating single-point tool', 'Rotating abrasive wheel', 'Stationary form tool'],
  'Milling uses a rotating multi-point cutting tool called a milling cutter.', [1])
q('theory', 'e', 'In milling, which element rotates and which is fed?',
  'The cutter rotates; the work is fed against it', ['The work rotates; the cutter is fed', 'Both reciprocate', 'Neither moves; the table vibrates'],
  'The milling cutter rotates at a fixed position while the work (table) is fed into it.', [2])
q('def', 'e', 'In milling, the movement of the work (table) towards the cutter is called…',
  'Feed', ['Cutting speed', 'Indexing', 'Depth of cut'],
  'The notes define the movement of the metal (work) as feeding.', [3])
q('theory', 'm', 'How does a milling cutter remove metal?',
  'Each tooth removes a small chip in every revolution', ['One continuous chip is removed per pass', 'Metal is melted by friction', 'Abrasive grains rub it away'],
  'Each tooth of the multi-point cutter takes a small chip during every rotation.', [4])
q('adv', 'm', 'Why is the milling machine called one of the most versatile machine tools?',
  'It can produce flat surfaces, slots, gears and complex shapes', ['It can only produce cylindrical parts', 'It needs no cutting tool', 'It removes metal only by grinding'],
  'With different cutters and attachments (like the dividing head), a milling machine makes flat surfaces, slots, keyways, gears and contours.', [5, 120])
q('tmat', 'e', 'Milling cutters are generally made of…',
  'High-speed steel (HSS)', ['Mild steel', 'Grey cast iron', 'Aluminium'],
  'The lecture states milling cutters are generally made of HSS.', [6])
q('def', 'm', 'Machining (including milling) is best described as a…',
  'Subtractive process that removes excess material', ['Additive process that builds layers', 'Forming process without chips', 'Joining process'],
  'Machining is subtractive: excess material is removed to get the required geometry and finish.', [7])

# ============================ up / down ============================
q('ops', 'e', 'Up milling is also known as…',
  'Conventional milling', ['Climb milling', 'Gang milling', 'Face milling'],
  'Up milling = conventional milling; down milling = climb milling.', [8])
q('ops', 'e', 'Down milling is also known as…',
  'Climb milling', ['Conventional milling', 'Straddle milling', 'Slab milling'],
  'Down milling = climb milling: the cutter rotation is in the same direction as the feed.', [10])
q('ops', 'm', 'In up milling, the direction of cutter rotation at the cut is…',
  'Opposite to the direction of feed', ['The same as the direction of feed', 'Perpendicular to the table', 'Along the cutter axis'],
  'In up (conventional) milling the cutter rotates against the feed.', [8])
q('ops', 'm', 'In which milling method is the chip thickness zero at the start of the cut and maximum at the end?',
  'Up milling', ['Down milling', 'Face milling', 'Straddle milling'],
  'Up milling: chip thickness minimum at the start, maximum at the end. Down milling: the reverse.', [9])
q('ops', 'm', 'In down milling, the chip thickness is…',
  'Maximum at the start of the cut and minimum at the end', ['Zero at the start and maximum at the end', 'Constant throughout', 'Zero throughout'],
  'In down (climb) milling the tooth enters at maximum chip thickness and leaves at minimum.', [11])
q('adv', 'm', 'Which is an ADVANTAGE of up milling?',
  'Scale on the work surface does not affect tool life much', ['It gives the best surface finish', 'It needs the least clamping', 'It never chatters'],
  'In up milling the tooth starts under the scale, so surface scale does not damage the cutter much.', [12])
q('adv', 'm', 'Which is a DISADVANTAGE of up milling?',
  'The cutter tends to lift the work, so firm clamping is needed', ['It cannot be used on scaled work', 'It puts maximum radial load on the arbor at entry', 'It needs a vertical machine'],
  'In up milling the upward cutting force tends to pull the work up off the table, and the tool tends to chatter.', [13])
q('adv', 'm', 'Which milling method gives a better surface finish and less radial pressure on the arbor?',
  'Down (climb) milling', ['Up (conventional) milling', 'Gang milling', 'Angular milling'],
  'Down milling gives a better finish, puts less radial pressure on the arbor and needs less power.', [15])
q('adv', 'm', 'Why is down milling NOT suitable for workpieces with surface scale?',
  'The tooth hits the hard scale first, reducing tool life', ['The work is lifted off the table', 'Chip thickness becomes zero', 'It needs a dividing head'],
  'In down milling each tooth enters at maximum chip thickness through the hard scale, which wears the cutter.', [16])
q('adv', 'h', 'Compared with down milling, up milling…',
  'Gives a rougher surface and needs more power', ['Gives a smoother surface and needs less power', 'Needs no clamping', 'Has chip thickness maximum at the start'],
  'Up milling rubs at entry, so the finish is rougher and the power is higher; down milling is the reverse.', [14, 15])
q('adv', 'h', 'Up milling is preferred when the machine has significant backlash in the table feed screw. Why?',
  'The cutting force pushes against the feed, taking up backlash', ['The cutter pulls the table forward', 'Chip thickness is maximum at entry', 'It eliminates the need for clamping'],
  'In up milling the cutter opposes the feed, so the table is kept pressed against the screw. In climb milling the cutter can pull the table into the backlash.', [12, 14])

# ============================ operations ============================
q('ops', 'e', 'Plain (slab) milling produces…',
  'A flat surface, with teeth on the periphery of the cutter', ['A slot with the end of the cutter', 'Gear teeth with a form cutter', 'A V-groove with an angle cutter'],
  'Plain milling (slab milling) produces a flat surface with the peripheral teeth; the cutter axis is parallel to the surface.', [17])
q('ops', 'm', 'In plain (slab) milling, the cutter axis is…',
  'Parallel to the work surface', ['Perpendicular to the work surface', 'At 45° to the table', 'Vertical always'],
  'In slab milling the axis of the cutter is parallel to the surface being milled.', [17])
q('tools', 'm', 'Which cutter is used for slab milling (as given in the ME-106 notes)?',
  'Helical plain milling cutter', ['T-slot cutter', 'Dovetail cutter', 'Involute gear cutter'],
  'The notes call the helical plain milling cutter a "nick cutter", used for slab cutting.', [18])
q('ops', 'm', 'In face milling, the cutter axis is…',
  'Perpendicular to the work surface', ['Parallel to the work surface', 'Along the table feed', 'Inclined at the helix angle'],
  'Face milling uses a cutter whose axis is perpendicular to the surface being produced.', [19])
q('ops', 'm', 'In end milling, when the cutter diameter is less than the work width, the result is a…',
  'Slot cut into the part', ['Flat face across the whole part', 'Gear tooth', 'Chamfer'],
  'An end mill smaller than the work width cuts a slot.', [20])
q('ops', 'e', 'Machining two parallel vertical faces at once, using two side cutters on one arbor, is called…',
  'Straddle milling', ['Gang milling', 'Form milling', 'Face milling'],
  'Straddle milling uses two side (side-and-face) cutters separated by spacing collars.', [21])
q('ops', 'm', 'In straddle milling, the distance between the two cutters is set by…',
  'Spacing collars on the arbor', ['The index plate', 'The knee elevating screw', 'The overarm'],
  'Spacing collars (spacers) between the cutters on the arbor fix the distance.', [21])
q('app', 'm', 'Straddle milling is commonly used to produce…',
  'Square or hexagonal heads (parallel faces)', ['Spur gear teeth', 'T-slots in tables', 'Internal threads'],
  'Two parallel faces at a time make square or hexagonal shapes, e.g. bolt heads.', [21])
q('ops', 'e', 'Using a set of cutters of different sizes on one arbor to machine several different surfaces in one pass is called…',
  'Gang milling', ['Straddle milling', 'End milling', 'Angular milling'],
  'Gang milling mounts a gang of cutters together on the arbor to machine several surfaces simultaneously.', [22])
q('adv', 'm', 'Gang milling is widely used because it…',
  'Saves machining time in repetitive work', ['Gives the finest surface finish', 'Needs no arbor', 'Works without coolant'],
  'Machining several surfaces in one pass saves time, which suits repetitive (production) work.', [23])
q('param', 'h', 'In gang milling, the cutting speed is calculated from…',
  'The cutter with the largest diameter', ['The cutter with the smallest diameter', 'The average of all cutter diameters', 'The arbor diameter'],
  'All cutters turn at the same rpm, so the largest cutter has the highest surface speed. The speed is chosen for that cutter.', [24])
q('ops', 'm', 'Form milling is mainly used for…',
  'Cutting gear teeth and other profiles', ['Producing large flat surfaces', 'Cutting T-slots', 'Parting off bars'],
  'Form milling uses cutters whose teeth match the required profile, e.g. gear-tooth spaces.', [25])
q('param', 'h', 'Compared with plain milling, the cutting rate in form milling is…',
  'About 20–30% lower', ['About 20–30% higher', 'The same', 'About 3 times higher'],
  'The lecture states the cutting rate in form milling is 20–30% less than in plain milling.', [26])
q('ops', 'm', 'Producing a V-block (surfaces at an angle to the spindle axis) is an example of…',
  'Angular milling', ['Gang milling', 'Straddle milling', 'Face milling'],
  'Angular milling produces surfaces at an angle other than 90° to the spindle axis, e.g. V-blocks.', [27])
q('ops', 'm', 'Which cutters can be used to cut slots or keyways?',
  'End mill, slot drill or side-and-face cutter', ['Fly cutter only', 'Face mill only', 'Grinding wheel only'],
  'Slots and keyways are cut with end mills, slot drills, side-and-face cutters or slitting saws.', [28])
q('ops', 'm', 'Which of these is NOT one of the milling operations listed in the ME-106 lecture?',
  'Knurling', ['Straddle milling', 'Form milling', 'Angular milling'],
  'The lecture lists plain, face, end, straddle, form, gang and angular milling. Knurling is a lathe operation.', [29])

# ============================ cutters ============================
q('tools', 'm', 'A milling cutter with cutting edges on both sides as well as on its periphery is a…',
  'Side-and-face cutter', ['Plain slab cutter', 'Slitting saw', 'Fly cutter'],
  'The wall chart describes the side-and-face cutter as cutting on its face and both sides.', [30])
q('tools', 'h', 'Which of these cutters is NOT shown on the "Milling cutters" wall chart in the ME-106 milling lab?',
  'Ball-nose end mill', ['Interlocking side milling cutter', 'Staggered-tooth side milling cutter', 'Half-side milling cutter'],
  'The chart shows plain, helical plain, side-and-face, interlocking side, half-side and staggered-tooth side cutters.', [31])
q('tools', 'e', 'Which cutter is used to cut T-slots like those in machine tables?',
  'T-slot cutter', ['Dovetail cutter', 'Fly cutter', 'Hollow mill'],
  'A T-slot cutter makes the wide bottom of a T-slot after a narrow slot has been cut.', [34])
q('tools', 'm', 'A thin milling cutter used for narrow slots or for cutting off is a…',
  'Slitting (slotting) saw', ['Slab cutter', 'Face mill', 'Ball-nose end mill'],
  'Slitting saws are thin discs with fine teeth for narrow slots and cutting off.', [33])
q('tools', 'm', 'A large cylindrical cutter with teeth only on its outside, used for wide flat surfaces, is the…',
  'Slab (plain) cutter', ['T-slot cutter', 'End mill', 'Dovetail cutter'],
  'The slab (plain) cutter cuts large flat surfaces with its peripheral teeth.', [32])
q('tools', 'm', 'Which cutter is pipe-shaped with teeth on the inside and is used to cut rods to size?',
  'Hollow milling cutter', ['Fly cutter', 'Slot drill', 'Side-and-face cutter'],
  'A hollow milling cutter has internal teeth and machines round rods to size.', [35])
q('tools', 'm', 'Which cutter has a rounded tip and is used for 3-D contouring of curved surfaces?',
  'Ball-nose end mill', ['Slitting saw', 'Slab cutter', 'T-slot cutter'],
  'A ball-nose end mill has a hemispherical tip for 3-D contours; a plain end mill cuts on its tip and sides.', [36])
q('tools', 'm', 'A large cutter, often with inserts, that cuts with its bottom face to give flat smooth surfaces is a…',
  'Face mill', ['Hollow mill', 'Slitting saw', 'Dovetail cutter'],
  'A face-mill cutter cuts with its face (bottom) and gives flat, smooth surfaces.', [37])
q('tools', 'e', 'Which cutter is used to machine dovetail grooves?',
  'Dovetail cutter', ['T-slot cutter', 'Fly cutter', 'Ball-nose end mill'],
  'A dovetail cutter has angled sides that produce the dovetail shape.', [38])
q('tools', 'm', 'A simple bar holding a single cutting tip, used for large smooth flat areas, is a…',
  'Fly cutter', ['Slab cutter', 'Slot drill', 'Gang cutter'],
  'A fly cutter is a single-point milling tool for light finishing of large flat areas.', [39])
q('tools', 'm', 'A roughing end mill has wavy (serrated) cutting edges. It is used for…',
  'Removing a lot of material quickly with a rough finish', ['Final finishing of gear teeth', 'Cutting very thin slots', 'Polishing surfaces'],
  'Serrated edges break the chips up, allowing heavy stock removal; the finish is rough.', [40])
q('tools', 'm', 'Cutters shaped to a specific profile, used to make gears or threads, are called…',
  'Form (formed) cutters', ['Plain cutters', 'Fly cutters', 'Hollow cutters'],
  'Formed cutters have teeth shaped to the profile they produce.', [41])
q('tools', 'e', 'Which cutter is used in the ME-106 lab to cut the spur gear teeth?',
  'Involute gear cutter', ['Slab cutter', 'T-slot cutter', 'Fly cutter'],
  'The milling TA slides and the lab tool photo show an involute gear (form) cutter for cutting spur gear teeth.', [42])
q('tools', 'h', 'Why does a set of involute gear cutters contain several cutters for one diametral pitch?',
  'Each cutter covers a range of tooth numbers', ['Each cutter is for a different material', 'Each cutter is for a different depth', 'Each cutter is for a different speed'],
  'The tooth-space shape changes with the number of teeth, so each cutter in a set covers a range of tooth numbers.', [43])
q('tools', 'h', 'Which of these is a term from milling-cutter nomenclature?',
  'Land', ['Clapper block', 'Swing over bed', 'Bastard cut'],
  'Cutter nomenclature includes outside diameter, hole, keyway, face of tooth, land, rake and clearance angles, depth of tooth, pitch and helix angle. A clapper block belongs to a shaper, swing over bed is a lathe specification, and bastard cut is a file grade.', [44])
q('tools', 'h', 'On a milling cutter, the keyway in the bore is used to…',
  'Drive the cutter from the arbor through a key', ['Collect chips', 'Hold coolant', 'Set the helix angle'],
  'The key in the cutter keyway and arbor keyway transmits the drive.', [44, 55])

# ============================ machines and parts ============================
q('parts', 'm', 'Which of these is NOT a type of milling machine?',
  'Capstan milling machine', ['Column-and-knee type', 'Bed (fixed-bed) type', 'CNC milling machine'],
  'Milling machines are column-and-knee (hand, horizontal, vertical, universal), fixed-bed/planer type and CNC. Capstan is a type of lathe.', [45])
q('parts', 'm', 'Column-and-knee milling machines are classed as horizontal or vertical according to the…',
  'Orientation of the spindle (cutter) axis', ['Shape of the base', 'Direction of the knee movement', 'Type of coolant'],
  'Horizontal and vertical refer to the axis of the spindle/cutter.', [46])
q('parts', 'e', 'In a horizontal milling machine, the spindle axis is…',
  'Horizontal, parallel to the table', ['Vertical, perpendicular to the table', 'Inclined at 45°', 'Along the column'],
  'A horizontal mill has its spindle (and arbor) parallel to the table.', [47])
q('parts', 'm', 'Cutters on a horizontal milling machine are mounted on the…',
  'Arbor', ['Quill', 'Tailstock', 'Ram'],
  'Horizontal machines use arbor-mounted cutters; vertical machines use end mills and face mills in the spindle.', [47, 55])
q('parts', 'e', 'Which cutters are normally used on a vertical milling machine?',
  'End mills and face mills', ['Arbor-mounted slab cutters', 'Grinding wheels', 'Single-point lathe tools'],
  'A vertical mill holds end mills and face mills directly in the vertical spindle.', [48])
q('adv', 'm', 'Which statement correctly compares horizontal and vertical milling machines?',
  'Horizontal: higher metal removal; vertical: more versatile for slots and profiles', ['Horizontal: more versatile; vertical: heavier cuts', 'Both are identical in use', 'Vertical machines cannot cut slots'],
  'Horizontal mills take heavy cuts on large flat surfaces; vertical mills are more versatile for slots, holes and complex profiles.', [49])
q('parts', 'm', 'Which part of a column-and-knee milling machine moves up and down on the column?',
  'Knee', ['Saddle', 'Overarm', 'Arbor'],
  'The knee slides vertically on the column (vertical feed) and carries the saddle and table.', [53])
q('parts', 'm', 'The knee of a milling machine is raised and lowered by the…',
  'Elevating screw', ['Arbor nut', 'Index crank', 'Overarm clamp'],
  'The elevating screw (worked by the knee elevating handle) raises and lowers the knee.', [53, 51])
q('parts', 'm', 'On a column-and-knee mill, cross movement (towards or away from the column) is given by the…',
  'Saddle', ['Table', 'Knee', 'Overarm'],
  'The saddle moves on the knee for cross feed; the table moves on the saddle longitudinally.', [54])
q('parts', 'm', 'The outer end of the arbor on a horizontal milling machine is supported by the…',
  'Arbor support hanging from the overarm', ['Tailstock of the dividing head', 'Knee', 'Elevating screw'],
  'The arbor support, carried on the overarm, steadies the outer end of the arbor.', [55])
q('parts', 'm', 'Which part houses the spindle drive and carries the overarm?',
  'Column', ['Knee', 'Saddle', 'Base'],
  'The column is the main vertical casting on the base; it houses the spindle drive and carries the overarm.', [52])
q('parts', 'h', 'Which of these parts is shown on the column-and-knee milling machine wall chart in the ME-106 lab?',
  'Telescopic feed shaft', ['Clapper box', 'Lead screw', 'Magnetic chuck'],
  'The chart lists base, elevating screw, knee, knee elevating handle, cross-feed handle, saddle, table, front brace, arbor support, arbor, overhanging arm, cutter, column, cone pulley and telescopic feed shaft.', [51])
q('parts', 'm', 'Which parts are typical of a vertical milling machine?',
  'Milling head, ram and quill', ['Arbor and arbor support', 'Clapper box and ram', 'Headstock and tailstock with live centre'],
  'A vertical mill has a milling head on a ram (overarm), with the spindle in a quill.', [56])
q('parts', 'm', 'In a bed-type milling machine, the table is…',
  'Mounted on a fixed bed and moves only horizontally', ['Carried on a knee that moves up and down', 'Rotated by a dividing head', 'Fixed while the bed moves'],
  'The bed-type machine replaces the knee with a large bed; the table moves only horizontally.', [57])
q('parts', 'e', 'What type of milling machine is used for the gear job in the ME-106 lab?',
  'Universal horizontal (column-and-knee) milling machine', ['CNC vertical machining centre', 'Bed-type planer mill', 'Hand milling machine'],
  'The log sheets list a universal horizontal milling machine (column-and-knee type).', [58])
q('parts', 'm', 'Which of these is NOT a main component of a horizontal milling machine?',
  'Tool head with clapper box', ['Arbor', 'Knee', 'Overarm'],
  'Horizontal mill parts: base, column, knee, saddle, table, spindle, arbor, overarm, arbor support. The clapper box belongs to a shaper.', [50])

# ============================ indexing ============================
q('def', 'e', 'In milling, indexing means…',
  'Dividing the work periphery into equal divisions', ['Measuring the cutter diameter', 'Setting the cutting speed', 'Clamping the work in a vice'],
  'Indexing divides the periphery into equal (or unequal) parts by rotating the work by a precise angle between cuts.', [59])
q('def', 'm', 'An index plate is…',
  'A plate with circles of equally spaced holes', ['A table with T-slots', 'A gear with 40 teeth', 'A graduated dial on the knee'],
  'The index plate has several hole circles; the index pin engages these holes.', [60])
q('gear', 'e', 'The worm and worm wheel of a standard dividing head give a ratio of…',
  '40 : 1', ['20 : 1', '60 : 1', '1 : 1'],
  'The worm wheel has 40 teeth and the worm is single-start, so the ratio is 40 : 1.', [62])
q('gear', 'e', 'How many turns of the index crank rotate the work once on a standard dividing head?',
  '40', ['20', '1', '360'],
  '40 turns of the crank make one turn of the work spindle (40 : 1).', [63])
q('gear', 'm', 'Which of these is NOT an indexing method?',
  'Straddle indexing', ['Direct indexing', 'Simple indexing', 'Differential indexing'],
  'The methods are direct, simple, compound and differential indexing. Straddle is a milling set-up.', [64])
q('gear', 'm', 'Direct indexing is also called…',
  'Rapid indexing', ['Compound indexing', 'Differential indexing', 'Angular indexing'],
  'Direct indexing is the simplest method, also called rapid indexing.', [65])
q('gear', 'm', 'In direct indexing…',
  'The worm is disengaged and the plate is turned by hand', ['The worm drives the spindle 40 : 1', 'Two hole circles are used together', 'Change gears drive the plate'],
  'In direct (rapid) indexing the worm is disengaged; the direct plate (24, 30 or 36 holes) is turned by hand.', [65])
q('gear', 'm', 'Which hole circles are used on a direct indexing plate?',
  '24, 30 and 36', ['15, 16 and 17', '21, 23 and 27', '37, 39 and 41'],
  'The lecture states direct indexing uses a plate with 24, 30 or 36 holes.', [65])
n('gear', 'm', 'Using direct indexing on a 24-hole plate, how many holes are moved for each side of a square?',
  '6 holes', ['4 holes', '24 holes', '96 holes'],
  '24 holes / 4 divisions = 6 holes each time (lecture example).', [66])
n('gear', 'm', 'Using direct indexing on a 24-hole plate, how many holes are moved for each face of a hexagon?',
  '4 holes', ['6 holes', '3 holes', '144 holes'],
  '24 / 6 = 4 holes per division.', [66, 65])
q('gear', 'm', 'In simple (plain) indexing, the crank movement per division is…',
  '40 / N turns', ['N / 40 turns', '40 × N turns', '360 / N turns'],
  'With a 40 : 1 dividing head, crank turns = 40/N. A common mistake is to use 40 × N or N/40.', [67])
n('gear', 'h', 'Simple indexing for N = 7 divisions needs…',
  '5 full turns + 35 holes on the 49-hole circle', ['5 full turns + 5 holes on the 7-hole circle', '7 full turns + 5 holes on the 49-hole circle', '280 full turns'],
  '40/7 = 5 5/7. There is no 7-hole circle, so 5/7 = 35/49: 5 turns + 35 holes on the 49-hole circle (lecture example).', [68])
q('gear', 'h', 'Compound indexing involves…',
  'Moving the crank on one circle and then the plate itself on another circle', ['Disengaging the worm and turning the plate by hand', 'Using change gears between spindle and plate', 'Moving only the sector arms'],
  'Compound indexing combines crank movement on one hole circle with movement of the plate (rear lock pin released) on another.', [69])
q('gear', 'h', 'Differential indexing is used when…',
  'Simple indexing cannot give the required division', ['The work is square', 'Only 24, 30 or 36 divisions are needed', 'The worm is disengaged'],
  'Differential indexing gears the spindle to the plate to obtain divisions not possible with simple indexing (e.g. some primes).', [70])
q('gear', 'm', 'Which hole circles are on index plate 2 (Brown & Sharpe) used in the ME-106 lab?',
  '21, 23, 27, 29, 31, 33', ['15, 16, 17, 18, 19, 20', '37, 39, 41, 43, 47, 49', '24, 30, 36'],
  'Plate 1: 15–20; Plate 2: 21, 23, 27, 29, 31, 33; Plate 3: 37, 39, 41, 43, 47, 49.', [71])
q('gear', 'm', 'Which of these is a hole circle on index plate 3 (Brown & Sharpe)?',
  '43', ['33', '20', '24'],
  'Plate 3 has 37, 39, 41, 43, 47 and 49 holes.', [71])
q('gear', 'm', 'What is the purpose of the sector arms on a dividing head?',
  'To span the required number of holes so they need not be counted each time', ['To lock the work spindle', 'To engage the worm', 'To change the 40 : 1 ratio'],
  'The sector arms are set to the needed number of hole spaces, which speeds up indexing and avoids counting errors.', [72])
q('prec', 'm', 'While indexing a gear, the index crank should never be turned backwards because…',
  'Backlash in the worm drive will spoil the division', ['The plate will fall off', 'The cutter will reverse', 'The coolant will stop'],
  'The 2025 log sheet says not to rotate the index-plate handle in the opposite direction; reversing introduces backlash errors.', [73, 114])

# ============================ gear terminology & formulas ============================
q('gear', 'm', 'Diametral pitch (DP) is defined as…',
  'Number of teeth per inch of pitch-circle diameter', ['Number of teeth per inch of circumference', 'Pitch-circle diameter per tooth in mm', 'Outside diameter divided by 2'],
  'DP = N / D_pitch (inches). (The notebook\'s "teeth / circumference" is wrong. See corrections.md.)', [74])
q('gear', 'e', 'The formula for the outside (blank) diameter of a spur gear in the DP system is…',
  'OD = (N + 2) / DP', ['OD = N / DP', 'OD = (N − 2) / DP', 'OD = DP / (N + 2)'],
  'OD = (N + 2)/DP: the pitch diameter N/DP plus two addenda of 1/DP each.', [75])
q('gear', 'm', 'Pitch-circle diameter in the DP system is…',
  'N / DP', ['(N + 2) / DP', 'DP / N', 'π / DP'],
  'D_pitch = N/DP. Adding two addenda (2/DP) gives the outside diameter.', [76])
q('gear', 'm', 'In the DP system, the addendum equals…',
  '1 / DP', ['1.157 / DP', '2.157 / DP', 'π / DP'],
  'Addendum = 1/DP, dedendum = 1.157/DP, clearance = 0.157/DP.', [77])
q('gear', 'm', 'In the DP system, the dedendum equals…',
  '1.157 / DP', ['1 / DP', '0.157 / DP', '2 / DP'],
  'Dedendum = addendum + clearance = 1/DP + 0.157/DP = 1.157/DP.', [77])
q('gear', 'h', 'In standard gear terminology, 2.157/DP is the…',
  'Whole depth (addendum + dedendum)', ['Clearance', 'Addendum', 'Circular pitch'],
  'Whole depth = 1/DP + 1.157/DP = 2.157/DP. Standard working depth (two addenda) = 2/DP. Our lab calls 2.157/DP the "working depth".', [78])
q('gear', 'h', 'In textbook gear terminology, the depth of engagement of two mating teeth (two addenda) equals…',
  '2 / DP', ['π / DP', '1 / DP', '1.157 / DP'],
  'Working depth = sum of the addenda of two mating gears = 2/DP. Whole depth = 2.157/DP (called "working depth" in our lab).', [78])
q('gear', 'm', 'In the ME-106 milling lab, the depth to which the gear teeth are cut ("working depth") is calculated as…',
  '2.157 / DP', ['π / DP', '(N + 2) / DP', '40 / N'],
  'The lab board and log sheet use W.D. = 2.157/DP.' + WD_NOTE, [79])
q('gear', 'm', 'Circular pitch in the DP system is…',
  'π / DP', ['DP / π', '25.4 / DP', '1 / DP'],
  'Circular pitch = π × D_pitch / N = π/DP.', [80])
q('gear', 'm', 'The relation between module m (mm) and diametral pitch DP (per inch) is…',
  'm = 25.4 / DP', ['m = DP / 25.4', 'm = π / DP', 'm = 25.4 × DP'],
  'Module = pitch diameter (mm) / N, and 1 inch = 25.4 mm, so m = 25.4/DP.', [81])
q('gear', 'e', 'A spur gear has teeth that are…',
  'Straight and parallel to the axis of rotation', ['Inclined to the axis', 'Cut on a cone', 'Cut on the inside of a ring'],
  'A spur gear is the simplest and most common gear, with straight teeth parallel to the axis.', [82])
q('gear', 'm', 'Which of these is NOT a spur gear nomenclature term?',
  'Helix angle', ['Addendum', 'Pitch circle', 'Circular pitch'],
  'Spur gears have straight teeth, so they have no helix angle. Addendum, dedendum, pitch circle, circular pitch and tooth thickness are spur-gear terms.', [83])

# gear types (text)
q('gear', 'e', 'Spur gears and ordinary (parallel-axis) helical gears connect shafts that are…',
  'Parallel', ['Intersecting', 'Non-intersecting at 90°', 'Co-axial and opposite'],
  'Spur, helical and herringbone gears all connect parallel shafts.', [84])
q('gear', 'm', 'Compared with spur gears, helical gears…',
  'Run more smoothly and quietly but produce axial thrust', ['Are noisier and produce no thrust', 'Connect intersecting shafts', 'Convert rotary to linear motion'],
  'Inclined teeth engage gradually: smoother and quieter, but with an axial thrust component.', [85])
q('gear', 'm', 'Why are double-helical (herringbone) gears used?',
  'The opposite helices cancel the axial thrust', ['They connect intersecting shafts', 'They give a 40 : 1 reduction', 'They convert rotation into straight-line motion'],
  'Two opposite-hand helices produce equal and opposite axial thrusts that cancel.', [86])
q('gear', 'e', 'Bevel gears are used to connect shafts that are…',
  'Intersecting (usually at 90°)', ['Parallel', 'Non-intersecting and non-parallel', 'In a straight line'],
  'Bevel gears are conical and connect intersecting shafts.', [87])
q('gear', 'm', 'A worm and worm wheel connect shafts that are…',
  'Non-intersecting and at right angles', ['Parallel', 'Intersecting at 90°', 'Co-axial'],
  'The worm and worm wheel connect perpendicular, non-intersecting shafts and give a large reduction (40 : 1 in the dividing head).', [88])
q('gear', 'e', 'Which gear arrangement converts rotary motion into straight-line motion?',
  'Rack and pinion', ['Bevel gears', 'Worm and worm wheel', 'Internal gear'],
  'A pinion rolling on a straight rack turns rotation into linear motion. The rack is a gear of infinite radius.', [89])
q('gear', 'm', 'In an internal gear…',
  'Teeth are cut on the inside of a ring', ['Teeth are cut on a cone', 'Teeth form a screw thread', 'Teeth are on a straight bar'],
  'An internal gear has inward-facing teeth and meshes with an external pinion on a parallel shaft.', [90])
q('gear', 'h', 'Crossed helical (spiral) gears are used for shafts that are…',
  'Non-parallel and non-intersecting', ['Parallel', 'Intersecting', 'Co-axial'],
  'Crossed helical gears connect skew (non-parallel, non-intersecting) shafts.', [91])
q('gear', 'h', 'Which gear pair gives the largest speed reduction in a single stage?',
  'Worm and worm wheel', ['Spur gears', 'Herringbone gears', 'Bevel gears'],
  'A single-start worm advances the wheel only one tooth per revolution, so ratios like 40 : 1 are easy.', [88, 62])

# ============================ the ME-106 job ============================
q('dims', 'e', 'What is the objective of the ME-106 milling job?',
  'To make a spur gear from a circular workpiece by milling', ['To cut a keyway in a shaft', 'To face-mill a rectangular block', 'To cut a helical gear'],
  'The milling log sheet objective: to make a spur gear using milling operations from a circular workpiece.', [92])
q('wmat', 'e', 'What is the workpiece material for the ME-106 spur gear?',
  'Aluminium', ['Mild steel', 'Cast iron', 'Brass'],
  'The gear blank is an aluminium circular disc with a centre hole.', [93])
q('dims', 'e', 'What diametral pitch is used for the ME-106 gear?',
  'DP = 16', ['DP = 12', 'DP = 20', 'DP = 1.5'],
  'The lab board and log sheet give DP = 16 (teeth per inch).', [94])
q('dims', 'e', 'What is the outside (blank) diameter of the ME-106 gear?',
  '1½ inch', ['1 inch', '2 inch', '22 mm'],
  'The 2025 board and log sheet give OD = 1½ in with DP 16.', [97])
n('num', 'm', 'For the ME-106 gear, OD = 1½ in and DP = 16. How many teeth does the gear have?',
  '22', ['24', '14', '26'],
  'OD = (N + 2)/DP → N = OD × DP − 2 = 1.5 × 16 − 2 = 22. Forgetting the −2 gives 24.', [75, 97])
n('num', 'h', 'For the 22-tooth ME-106 gear, how is the index crank moved for each tooth?',
  '1 full turn + 27 holes on the 33-hole circle', ['1 full turn + 9 holes on the 33-hole circle', '2 full turns + 18 holes on the 21-hole circle', '880 full turns'],
  '40/22 = 1 18/22 = 1 9/11. Multiply 9/11 by 3/3 = 27/33, so 1 turn + 27 holes on the 33-hole circle (plate 2). 40 × 22 = 880 is the classic mistake.', [67, 98])
q('gear', 'm', 'Which index plate is used for the ME-106 22-tooth gear?',
  'Plate 2 (contains the 33-hole circle)', ['Plate 1 (15–20 holes)', 'Plate 3 (37–49 holes)', 'Direct plate (24/30/36 holes)'],
  '9/11 = 27/33, and the 33-hole circle is on plate 2.', [98, 71])
n('num', 'm', 'For the ME-106 gear (DP 16), what depth is set for cutting the teeth, using the lab formula?',
  '≈ 0.1348 in (≈ 3.4 mm)', ['≈ 0.0723 in (≈ 1.8 mm)', '≈ 0.0625 in (≈ 1.6 mm)', '≈ 0.1963 in (≈ 5.0 mm)'],
  '2.157/16 = 0.1348 in = 3.42 mm. 0.0723 in is the dedendum alone, 0.0625 in the addendum, and 0.1963 in the circular pitch.' + WD_NOTE, [79, 99])
n('num', 'h', 'For the ME-106 gear (22 teeth, DP 16), what is the pitch-circle diameter?',
  '1.375 in', ['1.5 in', '1.25 in', '0.727 in'],
  'D_pitch = N/DP = 22/16 = 1.375 in. 1.5 in is the outside diameter.', [76, 97])
n('num', 'h', 'For the ME-106 gear (DP 16), what is the circular pitch?',
  '≈ 0.196 in', ['≈ 0.0625 in', '≈ 0.135 in', '≈ 50.3 in'],
  'Circular pitch = π/DP = 3.1416/16 = 0.196 in.', [80, 94])
n('num', 'm', 'For DP 16, what is the addendum?',
  '0.0625 in', ['0.0723 in', '0.1348 in', '0.125 in'],
  'Addendum = 1/DP = 1/16 = 0.0625 in. 0.0723 is the dedendum (1.157/16).', [77, 94])
n('num', 'h', 'What module (mm) is equivalent to DP 16?',
  '≈ 1.59 mm', ['≈ 0.63 mm', '≈ 16 mm', '≈ 406 mm'],
  'm = 25.4/DP = 25.4/16 = 1.5875 mm.', [81, 94])
n('num', 'm', 'Practice: a gear blank of OD 1 in is cut with DP 16. How many teeth?',
  '14', ['16', '18', '12'],
  'N = OD × DP − 2 = 16 − 2 = 14 (worked example in the notes).', [95, 75])
n('num', 'h', 'Practice: indexing for a 14-tooth gear on a standard dividing head is…',
  '2 full turns + 18 holes on the 21-hole circle', ['2 full turns + 6 holes on the 21-hole circle', '1 full turn + 27 holes on the 33-hole circle', '560 full turns'],
  '40/14 = 2 6/7 = 2 18/21, so 2 turns + 18 holes on the 21-hole circle.', [96, 67])
n('num', 'h', 'How many degrees does the work rotate for one full turn of the index crank?',
  '9°', ['40°', '1°', '360°'],
  'One turn of the work (360°) takes 40 crank turns, so 360/40 = 9° per crank turn.', [63])
n('num', 'h', 'Simple indexing for 36 divisions can be done as…',
  '1 full turn + 2 holes on the 18-hole circle', ['1 full turn + 4 holes on the 18-hole circle', '36 full turns', '1 full turn + 1 hole on the 36-hole circle'],
  '40/36 = 1 1/9 = 1 2/18. So 1 turn + 2 holes on the 18-hole circle (plate 1). There is no 36-hole circle on the simple-indexing plates.', [67, 71])
n('num', 'm', 'For a 40-tooth gear, the index crank movement per tooth is…',
  'Exactly 1 full turn', ['40 full turns', 'Half a turn', '1 turn + 1 hole on any circle'],
  '40/40 = 1 turn per division.', [67])
n('num', 'h', 'A gear blank of 2 in OD is to be cut with DP 12. How many teeth will the gear have?',
  '22', ['24', '20', '26'],
  'N = OD × DP − 2 = 2 × 12 − 2 = 22.', [75])
q('dims', 'm', 'How is the ME-106 gear blank held during milling?',
  'On a mandrel between the dividing head and the tailstock', ['In a machine vice on the table', 'In a 4-jaw lathe chuck', 'On a magnetic chuck'],
  'The aluminium blank is mounted on a mandrel (shaft) supported by the dividing head and tailstock.', [100])

# ============================ tools ============================
q('tools', 'e', 'Which item from the ME-106 milling tool list holds the gear blank?',
  'Mandrel', ['Catch pin', 'Rough flat file', 'Coolant'],
  'The blank is mounted on a mandrel. The catch pin locks the index crank, and the file is used for deburring.', [101, 100])
q('tools', 'm', 'Which of these is NOT in the ME-106 milling log-sheet tool lists?',
  'Grinding wheel', ['Index plate', 'Worm wheel', 'Catch pin'],
  'The milling log sheets list the milling machine, index plate, chalk, catch pin, shaft, mandrel, worm wheel, tailstock, rough flat file, bench vice, coolant and calipers.', [101])
q('tools', 'm', 'In the ME-106 milling lab, what is the rough flat file used for?',
  'Finishing (deburring) the cut gear', ['Measuring the outside diameter', 'Indexing the crank', 'Driving the arbor'],
  'After cutting, the gear is polished/deburred with a file.', [101, 110])
q('tools', 'e', 'Which tool is used to measure the outside diameter of the gear blank?',
  'Outside caliper', ['Try square', 'Centre punch', 'Feeler gauge'],
  'The outer diameter of the blank is measured with an outside caliper (with a steel rule).', [104, 102])
q('tools', 'm', 'Which tools does the notebook list for the milling job?',
  'Outside caliper, mandrel and chuck key', ['Hacksaw, file and scriber', 'Grinding wheel and dresser', 'Emery paper and pumice powder'],
  'The notes list outside caliper, mandrel and chuck key for the milling job.', [102])
q('tools', 'm', 'Which item was photographed among the ME-106 milling lab tools?',
  'Involute gear cutter', ['Hacksaw frame', 'Centre punch', 'Magnetic V-block'],
  'The milling tools photo shows a flat file, outside caliper, index plate, steel rule, involute gear cutter, double-ended spanner, finished gears and a gear-train model.', [103])

# ============================ procedure ============================
q('proc', 'e', 'What is the FIRST step of the ME-106 milling procedure?',
  'Calculate the number of teeth from OD and DP', ['Switch on the coolant', 'Polish the gear with a file', 'Cut the first tooth space'],
  'Step 1: calculate the number of teeth using the outside diameter and diametral pitch.', [105])
q('proc', 'm', 'In the ME-106 milling procedure, what is calculated immediately after the number of teeth?',
  'The working depth (2.157/DP) and the indexing (40/N)', ['The cutting speed of the cutter', 'The taper angle', 'The grinding ratio'],
  'Step 2: calculate the working depth and the index.', [106])
q('proc', 'm', 'Which step comes immediately after calculating the depth and indexing?',
  'Fix the appropriate index plate on the dividing head', ['Polish the gear', 'Remove the mandrel', 'Measure the finished gear'],
  'Step 3: fix the index plate that has the required hole circle (33 holes for our gear).', [107])
s('proc', 'h', 'What is the correct sequence of the ME-106 milling procedure?',
  'Calculate N → calculate depth & index → fix index plate → clamp blank and start → cut and index repeatedly → file the gear',
  ['Clamp blank → cut all teeth → calculate N → fix index plate → file the gear → calculate depth',
   'Fix index plate → file the gear → calculate N → clamp blank → cut teeth → calculate depth',
   'Calculate depth → cut teeth → clamp blank → calculate N → fix index plate → file the gear'],
  'Log sheet: calculate teeth; calculate working depth and index; fix index plate; clamp workpiece and switch on machine and coolant; cut, return and index, repeat; polish with file.', [105, 106, 107, 108, 109, 110])
q('proc', 'm', 'After clamping the blank, what is switched on along with the machine?',
  'Coolant', ['Magnetic chuck', 'Power feed of the knee', 'Tailstock drive motor'],
  'Step 4: clamp the workpiece tightly, then switch on the machine and the coolant.', [108])
q('proc', 'm', 'How are successive tooth spaces cut on the ME-106 gear?',
  'Cut one space, bring the table back, index the crank, and repeat', ['Cut all spaces at once with a gang of cutters', 'Rotate the blank continuously while cutting', 'Index first for all teeth, then cut once'],
  'Feed the blank into the cutter to cut one tooth space, return the table, index, and repeat until all 22 spaces are cut.', [109])
q('proc', 'e', 'What is the LAST step of the ME-106 milling procedure?',
  'Polish (deburr) the gear with a file', ['Calculate the number of teeth', 'Fix the index plate', 'Switch on the coolant'],
  'The final step is to polish/finish the job using a file.', [110])
q('proc', 'm', 'In the ME-106 milling job, how many times is the work indexed to cut all the teeth?',
  '22 times (once per tooth)', ['40 times', '27 times', '33 times'],
  'One tooth space is cut per indexing move, so a 22-tooth gear needs 22 divisions.', [109, 97])
q('proc', 'm', 'Why is the table brought back before indexing to the next tooth?',
  'So the blank is clear of the cutter while it is rotated', ['To change the cutter', 'To reset the depth to zero', 'To cool the coolant'],
  'The blank must be clear of the rotating cutter before it is indexed, otherwise the cutter would damage the gear.', [109])

# ============================ precautions ============================
q('prec', 'e', 'Which footwear precaution appears on the ME-106 milling log sheets?',
  'Wear proper (safety) shoes', ['Open sandals are allowed', 'Canvas sports shoes are enough', 'Any footwear is acceptable'],
  'Both milling log sheets and the TA slides say to wear proper/safety shoes.', [111])
q('prec', 'e', 'While the milling machine is running, you should…',
  'Keep a proper distance from the machine', ['Lean over the cutter to watch', 'Hold the blank by hand', 'Touch the arbor to check speed'],
  'Maintain a proper distance from the machine while it is on.', [112])
q('prec', 'm', 'Which precaution about the workpiece appears on the 2025 milling log sheet?',
  'Fix the workpiece in the machine properly', ['Demagnetise it after use', 'Rinse it in water', 'Coat it with pumice'],
  'Fix (clamp) the workpiece properly in the machine.', [113])
q('prec', 'm', 'Which precaution is specific to indexing on the dividing head?',
  'Do not rotate the index-plate handle in the opposite direction', ['Do not exceed 2 mm depth on the shaper', 'Check the wheel clears the work', 'Maintain the spark gap'],
  'Turning the crank backwards introduces backlash errors in the division.', [114])
q('prec', 'e', 'According to the ME-106 milling log sheets, you must stay alert during…',
  'Fixing and cutting', ['Only the calculation', 'Only after cutting', 'Only while filing'],
  'Stay alert during fixing and cutting.', [115])
q('prec', 'm', 'Which electrical precaution appears on the ME-106 milling log sheet?',
  'Do not touch any electrical connections', ['Always touch the earth wire', 'Switch on with wet hands', 'Open the control panel'],
  'The 2022 milling log sheet says not to touch any electrical connections.', [116])
q('prec', 'm', 'Which of these should be avoided while milling, according to the TA slides?',
  'Loose threads, ornaments and wristwatches', ['Safety shoes', 'Apron', 'Supervision by the instructor'],
  'Loose items can be caught by the rotating cutter or arbor.', [117])
q('prec', 'm', 'According to the milling TA slides, the machine should NOT be operated…',
  'Without the shop instructor\'s supervision', ['With coolant on', 'With safety shoes', 'With the guard in place'],
  'Do not operate the machine without supervision; clean the machine and workspace after use.', [118])
q('prec', 'm', 'What should you do after finishing work on the milling machine?',
  'Clean the machine and workspace', ['Leave the chips on the table', 'Leave the machine running', 'Remove the guards'],
  'The TA slides ask you to clean the machine and workspace after use.', [118])
q('prec', 'm', 'Chips on the milling table should be removed…',
  'With a brush, after the cutter has stopped', ['By hand, while the cutter runs', 'With compressed air towards others', 'By the coolant only, while running'],
  'Never remove chips or measure the job while the cutter is rotating.', [119])
q('prec', 'm', 'Which of these is NOT a milling-shop precaution?',
  'Turn the index crank backwards to correct a mistake', ['Wear safety shoes and apron', 'Stay alert during fixing and cutting', 'Keep a proper distance from the running machine'],
  'Reversing the crank causes backlash errors. The other three are precautions on the milling log sheets.', [114, 111, 112, 115])
q('app', 'm', 'Which is a typical application of milling?',
  'Cutting gears, keyways and slots', ['Turning long shafts', 'Electroplating parts', 'Cutting internal threads by hand'],
  'Milling is used for gears, keyways, slots, flat surfaces of machine parts and dies.', [121])

# ============================ assertion-reason / T-F ============================
ar('ops', 'h', 'Down milling gives a better surface finish than up milling.',
   'Down milling is also known as climb milling.', 'b',
   'Both are true, but R is only another name for the method and explains nothing. The better finish comes from each tooth entering at full chip thickness, so there is no rubbing at entry.', [15, 10])
ar('gear', 'h', 'A 22-tooth gear cannot be indexed using only full turns of the crank.',
   'In simple indexing the crank turns per division = 40/N.', 'a',
   'Both true, R explains A: 40/22 = 1.818 is not a whole number, so a fraction (27/33) must be taken on a hole circle.', [67, 98])
ar('param', 'h', 'In gang milling the cutting speed is based on the largest cutter.',
   'All cutters on the arbor rotate at the same rpm.', 'a',
   'Both true and R explains A: same rpm means the largest diameter has the highest surface speed, so it limits the rpm.', [24])
tf('gear', 'm', 'Bevel gears connect parallel shafts.', False,
   'False. Bevel gears connect intersecting shafts; spur and helical gears connect parallel shafts.', [87, 84])
tf('gear', 'e', 'On a standard dividing head, 40 turns of the index crank turn the work once.', True,
   'True. The worm wheel has 40 teeth and the worm is single-start (40 : 1).', [63, 62])
tf('wmat', 'e', 'The ME-106 spur gear is cut from a mild-steel blank.', False,
   'False. The gear blank is an aluminium circular disc.', [93])

# ============================ diagrams ============================
B.labels('milling/horizontal-mill', 'p', diffs={'p': 'e'})
B.labels('milling/horizontal-mill', 'w', only={'w': ['C', 'F', 'G', 'H', 'K']})
B.labels('milling/horizontal-mill', 'f', only={'f': ['D', 'H', 'F']})
B.labels('milling/vertical-mill', 'p', only={'p': ['A', 'B', 'C', 'I', 'F']}, diffs={'p': 'm'})
B.labels('milling/up-down', 'p', cat='ops', diffs={'p': 'm'}, extra_parts=['Gang milling', 'Face milling'])
UD = 'milling/up-down'
q('ops', 'h', 'In panel A of the figure (cutter rotating clockwise), how does the chip thickness vary during each tooth\'s cut?',
  'Maximum at entry, decreasing to minimum at exit', ['Zero at entry, increasing to maximum at exit', 'Constant throughout', 'Zero throughout'],
  'Panel A is down (climb) milling: the teeth move with the feed and enter the uncut stock at full chip thickness.', [11], fig=UD)
q('ops', 'h', 'In panel B of the figure, the cutter rotates clockwise and the table moves to the right. Why is this up milling?',
  'At the cut, the teeth move opposite to the table feed', ['At the cut, the teeth move with the table feed', 'The cutter axis is vertical', 'Two cutters are used'],
  'With clockwise rotation, the bottom teeth move left while the work feeds right, so the cutter opposes the feed: up (conventional) milling.', [8], fig=UD)
B.labels('milling/cutters', 'p', cat='tools', diffs={'p': 'm'}, extra_parts=['Fly cutter', 'Dovetail cutter', 'Ball-nose end mill'])
CU = 'milling/cutters'
q('tools', 'm', 'Which cutter in the figure is used to cut the spur gear in the ME-106 lab?', 'F', ['A', 'B', 'C'],
  'F is the involute gear (form) cutter; its tooth profile matches the gear tooth space.', [42], fig=CU)
q('tools', 'h', 'Which cutter in the figure is used on a vertical milling machine to cut slots and pockets with its end?', 'C', ['A', 'B', 'D'],
  'C is the end mill, which cuts on its end and sides. A (slab) and B (side-and-face) are arbor-mounted cutters for horizontal machines.', [36, 48], fig=CU)
q('tools', 'm', 'Which cutter in the figure would be used for slab milling of a wide flat surface?', 'A', ['C', 'D', 'E'],
  'A is a helical plain (slab) cutter that cuts with its periphery.', [17, 32], fig=CU)
q('tools', 'm', 'A pair of the cutters in panel B, mounted with spacers, would be used for which set-up?', 'Straddle milling', ['Face milling', 'End milling', 'Form milling'],
  'Two side-and-face cutters separated by spacing collars machine two parallel faces at once: straddle milling.', [21, 30], fig=CU)
B.labels('milling/straddle-gang', 'p', cat='ops', diffs={'p': 'm'}, extra_parts=['Form milling', 'Face milling'])
B.labels('milling/dividing-head', 'p', cat='gear', diffs={'p': 'm'})
B.labels('milling/dividing-head', 'f', cat='gear', only={'f': ['A', 'B', 'D', 'F']}, diffs={'f': 'm'})
IP = 'milling/index-plate-33'
n('gear', 'm', 'The figure shows the 33-hole circle used for the ME-106 22-tooth gear. After the full turn, the sector arms span how many hole spaces?',
  '27', ['9', '18', '33'],
  '40/22 = 1 9/11 = 1 27/33, so the sector arms are set to 27 spaces on the 33-hole circle.', [98], fig=IP)
n('gear', 'h', 'Using the 33-hole circle in the figure, how many full crank turns are made before the extra hole spaces for each tooth of the ME-106 gear?',
  '1', ['2', '0', '22'],
  '40/22 = 1.818…, i.e. 1 full turn plus 27/33 of a turn.', [98, 67], fig=IP)
n('gear', 'h', 'If the 33-hole circle in the figure were used for an 11-tooth gear, the move per division would be…',
  '3 full turns + 21 holes', ['3 full turns + 7 holes', '4 full turns', '1 full turn + 27 holes'],
  '40/11 = 3 7/11 = 3 21/33, so 3 turns + 21 holes on the 33-hole circle.', [67, 71], fig=IP)
n('gear', 'h', 'The figure shows a 21-hole circle used for a 14-tooth practice gear. How many extra holes beyond the full turns?',
  '18', ['6', '14', '21'],
  '40/14 = 2 6/7 = 2 18/21, so 2 full turns + 18 holes.', [96], fig='milling/index-plate-21')
B.labels('milling/gear-nomenclature', 'p', cat='gear', diffs={'p': 'm'})
B.labels('milling/gear-nomenclature', 'f', cat='gear', only={'f': ['A', 'B', 'D', 'G', 'F']}, diffs={'f': 'h'})
B.labels('milling/gear-types', 'p', cat='gear', diffs={'p': 'e'}, extra_parts=['Crossed helical gears', 'Spiral bevel gears'])
GT = 'milling/gear-types'
q('gear', 'm', 'In the figure, which panel shows gears on INTERSECTING shafts?', 'D', ['A', 'E', 'G'],
  'D is a pair of bevel gears, whose shafts intersect (usually at 90°).', [87], fig=GT)
q('gear', 'm', 'In the figure, which panel shows gears on non-intersecting shafts at right angles with a large speed reduction?', 'E', ['D', 'B', 'F'],
  'E is a worm and worm wheel, the same type used inside the dividing head (40 : 1).', [88], fig=GT)
q('gear', 'm', 'In the figure, which panel shows a drive that converts rotation into straight-line motion?', 'F', ['A', 'C', 'G'],
  'F is a rack and pinion.', [89], fig=GT)
q('gear', 'h', 'In the figure, which panel shows parallel-shaft gears in which the axial thrust cancels out?', 'C', ['A', 'B', 'G'],
  'C is a double-helical (herringbone) gear pair: the opposite helices cancel each other\'s axial thrust. B (single helical) produces thrust.', [86, 85], fig=GT)
q('gear', 'm', 'Which panel in the figure shows the type of gear made in the ME-106 milling lab?', 'A', ['B', 'D', 'E'],
  'The ME-106 job is a spur gear (panel A): straight teeth parallel to the axis.', [82, 92], fig=GT)

# ============================ more procedure / precautions (standard practice) ============================
q('tools', 'h', 'Which Brown & Sharpe involute cutter number is used for the 22-tooth ME-106 gear?',
  'No. 5 (21–25 teeth)', ['No. 3 (35–54 teeth)', 'No. 7 (14–16 teeth)', 'No. 1 (135 teeth to rack)'],
  'Cutter No. 5 covers 21–25 teeth, so it suits the 22-tooth gear. No. 7 would be used for the 14-tooth practice gear.', [122, 97])
q('tools', 'h', 'For a 14-tooth gear, which Brown & Sharpe involute cutter number is used?',
  'No. 7 (14–16 teeth)', ['No. 5 (21–25 teeth)', 'No. 1 (135 teeth to rack)', 'No. 4 (26–34 teeth)'],
  'Cutter No. 7 covers 14–16 teeth.', [122, 95])
q('proc', 'm', 'Before cutting the first tooth space, the involute cutter must be…',
  'Centred over the axis of the gear blank', ['Offset to one side of the blank', 'Tilted at the helix angle', 'Set below the mandrel axis'],
  'Centring the cutter over the blank axis makes the tooth spaces symmetrical.', [123])
s('proc', 'h', 'What is the correct way to set the depth of cut for the gear teeth?',
  'Touch the blank with the rotating cutter → zero the knee dial → move the work clear → raise the knee by the depth',
  ['Raise the knee by the depth → touch the blank → zero the dial → move clear',
   'Zero the dial anywhere → raise the knee by the depth → touch the blank',
   'Move the work clear → raise the knee fully → touch the blank → zero the dial'],
  'Touch off (e.g. with a paper strip), zero the knee dial, move clear, then raise by the calculated depth (≈0.1348 in for DP 16).', [124, 99])
q('proc', 'm', 'Which slide is used to put on the depth of cut for the gear teeth on a horizontal column-and-knee machine?',
  'Knee (elevating screw)', ['Overarm', 'Arbor support', 'Index crank'],
  'The knee is raised by the calculated depth using the elevating screw and its dial.', [124, 53])
q('proc', 'm', 'Once the depth is set for gear cutting, which slides are locked?',
  'Knee and saddle, leaving only the table feed free', ['Table only', 'Index crank and sector arms', 'Overarm and column'],
  'Locking the knee and saddle keeps depth and position constant; only the longitudinal table feed moves the blank under the cutter.', [126])
q('proc', 'm', 'Before cutting the gear, the dividing head and tailstock centres must be…',
  'Aligned with the table travel, with the blank tight on the mandrel', ['Set at 45° to the table', 'Loosely held so the blank can slip', 'Removed from the table'],
  'Misalignment would make the tooth depth vary along the face; the blank must not slip on the mandrel.', [125, 100])
q('proc', 'h', 'If the gear blank slips on the mandrel during cutting, what happens to the gear?',
  'The tooth spacing becomes uneven', ['The teeth become deeper', 'The OD increases', 'Nothing, because the index plate corrects it'],
  'Indexing rotates the mandrel; if the blank slips, it does not rotate by the indexed amount, so the spacing is wrong.', [125, 113])
q('prec', 'e', 'While the milling cutter is rotating, you should never…',
  'Reach over or near the cutter', ['Stand at a proper distance', 'Keep the guard in place', 'Watch the feed from the side'],
  'Keep hands away from the cutter path at all times.', [127])
q('prec', 'e', 'When should the gear be measured or the chips removed on the milling machine?',
  'Only after stopping the machine', ['While the cutter is turning slowly', 'During the cut', 'Any time, if wearing gloves'],
  'Stop the machine before measuring, removing chips or adjusting the work.', [128])
q('prec', 'h', 'On a horizontal milling machine, when should the arbor nut be finally tightened?',
  'After the arbor support is in place', ['Before mounting the cutters', 'While the spindle is running', 'Never; it must stay loose'],
  'Tightening the nut without the outer support can bend the arbor. Also check the cutter rotation direction.', [129])
q('prec', 'm', 'Which eye protection is recommended while milling?',
  'Safety goggles', ['Laser safety goggles', 'Welding helmet', 'Tinted sunglasses'],
  'Chips fly from the cutter, so wear safety goggles.', [130])
q('prec', 'm', 'Which practice is correct on the milling machine?',
  'Keep the cutter guard in place and use the correct speed and feed', ['Remove the guard for a better view', 'Use the highest speed for every material', 'Feed by hand into a stopped cutter'],
  'Guards protect against contact and chips; the speed and feed must suit the material and cutter.', [131])
q('prec', 'm', 'Before starting the cut, you should check that the cutter…',
  'Rotates in the correct direction for the set-up', ['Is touching the blank at full depth', 'Is loose on the arbor', 'Is wet with dielectric'],
  'Wrong rotation means the teeth rub instead of cut and can damage the cutter or work.', [129])

B.save()
