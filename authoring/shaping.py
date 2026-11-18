"""Shaping question bank. Correct option first; options kept similar in length."""
from qlib import Bank

B = Bank('shaping')
q, n, s, tf, ar = B.q, B.n, B.s, B.tf, B.ar

# ============================ principle ============================
q('def', 'e', 'A shaper is best described as a…',
  'Reciprocating machine tool using a single-point tool', ['Rotating machine tool using a multi-point cutter', 'Rotating machine tool using an abrasive wheel', 'Spark-erosion machine using a wire electrode'],
  'The shaper is a reciprocating machine tool; the ram carries a single-point tool to and fro.', [1])
q('theory', 'm', 'In a shaper, the rotary motion of the motor/bull gear is converted into…',
  'Reciprocating motion of the ram', ['Rotary motion of the table', 'Rotary motion of the tool', 'Helical motion of the work'],
  'The drive mechanism converts rotary motion into the reciprocating motion of the ram.', [2])
q('app', 'e', 'Which surfaces does a shaper mainly produce?',
  'Flat surfaces — horizontal, vertical or inclined', ['Cylindrical surfaces between centres', 'Internal bores of small diameter', 'Helical threads on round bars'],
  'Shapers produce flat surfaces in any orientation, plus slots and grooves.', [3])
q('theory', 'e', 'On a shaper, metal is cut during…',
  'The forward stroke only', ['The return stroke only', 'Both forward and return strokes', 'Neither stroke; only while feeding'],
  'Cutting takes place only in the forward stroke; the return stroke is idle.', [4])
q('def', 'e', 'The return stroke of a shaper is called the idle stroke because…',
  'No metal is removed during it', ['The motor is switched off during it', 'The ram does not move during it', 'The tool is changed during it'],
  'No cutting takes place on the return stroke, so it is wasted (idle) time.', [4])
q('theory', 'e', 'The purpose of the quick-return mechanism in a shaper is to…',
  'Reduce the time lost on the idle return stroke', ['Increase the depth of cut per stroke', 'Make the cutting stroke faster than the return', 'Reverse the direction of the cross feed'],
  'A quick-return mechanism makes the return stroke faster, reducing total machining time.', [5])
q('parts', 'e', 'Most shapers use which quick-return mechanism?',
  'Crank and slotted lever', ['Worm and worm wheel', 'Rack and pinion only', 'Lead screw and half-nut'],
  'The lecture states most shapers use the crank and slotted-lever quick-return mechanism.', [6])
q('theory', 'm', 'How does shaping differ from planing?',
  'In shaping the tool reciprocates; in planing the work does', ['In shaping the work reciprocates; in planing the tool does', 'Shaping uses a multi-point cutter; planing does not', 'Shaping is used only for round work'],
  'In a shaper the ram (tool) reciprocates over fixed work; in a planer the table (work) reciprocates under a fixed tool.', [7])
q('def', 'e', 'Machining is a metal-removal process in which metal is removed…',
  'In the form of chips by a cutting tool', ['By melting with an electric arc', 'By pressing it into a die', 'By adding a thin plated layer'],
  'Machining removes metal as chips with a suitable cutting tool to get the desired size and shape.', [8])
q('theory', 'm', 'In metal cutting, the chip thickness compared with the uncut chip thickness is…',
  'Always greater', ['Always smaller', 'Always equal', 'Zero'],
  'The chip is plastically deformed (compressed) while shearing, so it is thicker than the uncut layer.', [9])
q('theory', 'm', 'The two relative motions needed in a machine tool are…',
  'Primary (cutting) motion and secondary (feed) motion', ['Primary (feed) motion and secondary (cutting) motion', 'Rotary motion and electrical motion', 'Rapid traverse and coolant flow'],
  'Primary motion gives the cutting velocity; secondary motion feeds the tool to the uncut portion.', [10])
q('def', 'h', 'In generating a flat surface on a shaper, the generatrix is the line produced by the…',
  'Primary (cutting) motion of the tool', ['Secondary (feed) motion of the table', 'Rotation of the bull gear', 'Down feed of the tool head'],
  'Generatrix = line traced by the primary (cutting) motion; directrix = line traced by the secondary (feed) motion.', [11])
q('def', 'h', 'On a shaper, the directrix is the line produced by the…',
  'Secondary (feed) motion of the table', ['Primary (cutting) motion of the ram', 'Swivelling of the tool head', 'Oscillation of the slotted lever'],
  'The crosswise feed of the table traces the directrix; the ram stroke traces the generatrix.', [11])
q('theory', 'm', 'In orthogonal cutting, along which plane is metal sheared ahead of the tool?',
  'Shear plane', ['Rake plane', 'Base plane', 'Clearance plane'],
  'The notes sketch the shear plane ahead of the tool where the chip forms; the rake angle is measured on the tool face.', [12])

# ============================ quick return ============================
q('parts', 'm', 'Which of these is NOT a part of the crank and slotted-lever mechanism?',
  'Index plate', ['Bull gear', 'Sliding block', 'Slotted lever'],
  'Parts: bull gear (crank), crank pin, sliding block, slotted lever, pivot, link to ram, driving pinion. The index plate is part of a milling dividing head.', [13])
q('parts', 'm', 'In a crank shaper, the bull gear is driven by…',
  'A small driving pinion from the motor', ['The ram through a link', 'The table cross-feed screw', 'The clapper box'],
  'A driving pinion (driving gear) from the motor drives the large bull gear.', [14])
q('parts', 'm', 'In the quick-return mechanism, the sliding block…',
  'Rides on the crank pin and slides in the slotted lever', ['Is fixed to the ram and slides in the column', 'Holds the tool in the clapper box', 'Clamps the work in the vice'],
  'The sliding block on the crank pin slides in the slot, making the lever oscillate about its pivot.', [15])
q('param', 'e', 'In the ME-106 shaper wall chart, the crank turns through how many degrees during the cutting stroke?',
  '240°', ['120°', '180°', '360°'],
  'The chart shows 240° of crank rotation for the cutting stroke and 120° for the return stroke.', [16])
n('num', 'm', 'If the cutting stroke takes 240° of crank rotation and the return stroke 120°, what is the ratio of cutting time to return time?',
  '2 : 1', ['1 : 2', '3 : 2', '1 : 1'],
  'At constant crank speed, time ∝ angle: 240/120 = 2, so cutting takes twice as long as return.', [17, 16])
q('param', 'h', 'The quick-return ratio (cutting time : return time) of shapers usually lies between…',
  '3 : 2 and 2 : 1', ['1 : 2 and 1 : 1', '4 : 1 and 6 : 1', '1 : 3 and 1 : 2'],
  'Typical quick-return ratios are between about 1.5 and 2.', [18])
q('param', 'm', 'On a crank shaper, the length of stroke is changed by…',
  'Changing the crank-pin radius on the bull gear', ['Changing the number of teeth on the pinion', 'Swivelling the tool head', 'Moving the table on the cross rail'],
  'Moving the sliding block (crank pin) nearer to or farther from the bull-gear centre changes the stroke length.', [19])
q('param', 'm', 'The position of the stroke (where the ram works relative to the job) is adjusted by…',
  'Shifting the ram relative to its link and locking it', ['Changing the crank-pin radius', 'Changing the motor speed', 'Raising the cross rail'],
  'The ram is moved relative to its connection and locked with the ram locking handle, without changing the stroke length.', [20])
n('num', 'h', 'In a crank and slotted-lever mechanism, the crank radius is 100 mm and the distance from the crank centre to the lever pivot is 200 mm. What is the ratio of cutting time to return time?',
  '2 : 1', ['1.5 : 1', '3 : 1', '1 : 2'],
  'cos θ = r/d = 0.5, θ = 60°. Return angle = 2θ = 120°, cutting = 240°, so ratio = 240/120 = 2.', [70, 17])
n('num', 'h', 'For a shaper, the return stroke takes 144° of crank rotation. What is the cutting-to-return time ratio?',
  '1.5 : 1', ['2 : 1', '0.67 : 1', '2.5 : 1'],
  'Cutting angle = 360 − 144 = 216°; ratio = 216/144 = 1.5.', [70, 17])
n('num', 'h', 'A shaper ram makes 30 double strokes per minute with a 240° : 120° quick return. How long does one cutting stroke take?',
  '≈ 1.33 s', ['≈ 0.67 s', '≈ 2.0 s', '≈ 1.0 s'],
  'One double stroke = 60/30 = 2 s. Cutting = 240/360 × 2 = 1.33 s; return = 0.67 s.', [16, 17])

# ============================ cutting speed / time ============================
q('def', 'h', 'The cutting speed of a shaper is given by…',
  'V = L·N·(1 + m) / 1000 m/min', ['V = π·D·N / 1000 m/min', 'V = L·N / (1 + m) m/min', 'V = 2·L·N m/min'],
  'L = stroke length (mm), N = double strokes/min, m = return time/cutting time. πDN/1000 is for turning.', [68])
n('num', 'h', 'A shaper has a stroke length of 150 mm, makes 40 double strokes per minute and has m = return time/cutting time = 0.5. What is the cutting speed?',
  '9 m/min', ['6 m/min', '12 m/min', '4 m/min'],
  'V = L·N·(1 + m)/1000 = 150 × 40 × 1.5 / 1000 = 9 m/min. Ignoring (1 + m) gives 6 m/min.', [68])
n('num', 'm', 'The 38 mm wide face of the ME-106 block is shaped with a cross feed of 0.5 mm per double stroke. How many double strokes are needed for one pass?',
  '76', ['19', '38', '152'],
  'Number of strokes = width/feed = 38/0.5 = 76.', [69, 44])
n('num', 'h', 'If the shaper makes 38 double strokes per minute, how long does it take to cover the 38 mm wide face of the ME-106 block once at 0.5 mm feed per double stroke?',
  '2 minutes', ['1 minute', '0.5 minute', '4 minutes'],
  'Strokes = 38/0.5 = 76; time = 76/38 = 2 min.', [69, 44])

# ============================ machine parts ============================
q('parts', 'e', 'Which part of a shaper carries the tool head and reciprocates?',
  'Ram', ['Table', 'Cross rail', 'Base'],
  'The ram reciprocates in the column guides and carries the tool head at its front.', [23])
q('parts', 'm', 'Which part of the shaper is mounted at the front of the ram and can be swivelled for angular cuts?',
  'Tool head', ['Cross rail', 'Table support', 'Clapper block'],
  'The tool head on the front of the ram can be swivelled to cut inclined surfaces (wall chart: "head can swing on front of the ram").', [24])
q('parts', 'm', 'On a shaper, the depth of cut is given by the…',
  'Down-feed screw (handle) on the tool head', ['Cross-feed screw of the table', 'Ram locking handle', 'Crank-pin adjusting screw'],
  'The down-feed screw lowers the tool slide by the required depth.', [25])
q('parts', 'm', 'What is the function of the clapper box on a shaper?',
  'Lets the tool lift on the return stroke so it does not drag', ['Holds the work firmly on the table', 'Gives the cross feed to the table', 'Sets the length of the stroke'],
  'The clapper block is hinged, so the tool swings up on the return stroke and does not rub the work.', [26])
q('parts', 'm', 'On a shaper, the table is carried on the…',
  'Cross rail on the front of the column', ['Ram at the top of the column', 'Bull gear inside the column', 'Tool head at the front of the ram'],
  'The table is mounted on the cross rail; the cross-feed screw moves it sideways and the rail can be raised or lowered.', [27, 28])
q('parts', 'm', 'Which part houses the drive mechanism and carries the ram guides?',
  'Column (body)', ['Table', 'Cross rail', 'Tool head'],
  'The column is a hollow box casting on the base that houses the bull gear mechanism and supports the ram.', [29])
q('parts', 'm', 'Which part steadies the front of the shaper table?',
  'Table support (front support)', ['Clapper box', 'Ram locking handle', 'Down-feed screw'],
  'The front support for the table (shown on the wall chart) prevents the table from sagging under cutting forces.', [30])
q('tools', 'e', 'How is the job held on the shaper in the ME-106 lab?',
  'In a machine vice on the table', ['Between centres', 'On a magnetic chuck', 'In a three-jaw chuck'],
  'The notes say to lock the workpiece in the plain machine vice; the log sheet says to fix it tightly using the clamp.', [31])
q('parts', 'm', 'Which set of parts is shown on the "Parts of a standard shaper" chart in the ME-106 lab?',
  'Ram, clapper box, tool, table and front support', ['Arbor, overarm, knee and saddle', 'Headstock, tailstock, carriage and apron', 'Wheel head, magnetic chuck and dogs'],
  'The wall chart labels the head (swivelling on the ram), clapper box, tool, ram, table and front support for the table.', [22])
q('parts', 'm', 'Which of these parts is NOT found on a shaper?',
  'Lead screw with half-nut', ['Clapper box', 'Cross rail', 'Ram'],
  'Lead screw and half-nut are lathe threading parts. Shapers have a ram, tool head, clapper box, table, cross rail, column and base.', [21])

# ============================ classification ============================
q('theory', 'm', 'Shapers classified by the mechanism that drives the ram are…',
  'Crank, geared and hydraulic types', ['Standard and universal types', 'Push and draw types', 'Horizontal, vertical and travelling-head types'],
  'By ram drive: crank, geared, hydraulic. By table: standard, universal. By ram position: horizontal, vertical, travelling head. By stroke: push, draw.', [32])
q('theory', 'm', 'Shapers classified by the design of the table are…',
  'Standard and universal shapers', ['Crank and hydraulic shapers', 'Push and draw shapers', 'Horizontal and vertical shapers'],
  'A universal shaper\'s table can be swivelled and tilted; a standard shaper\'s cannot.', [33])
q('theory', 'm', 'Horizontal, vertical and travelling-head shapers are classified by…',
  'Position and travel of the ram', ['Type of drive mechanism', 'Design of the table', 'Type of cutting stroke'],
  'This classification is by the position and travel of the ram.', [34])
q('theory', 'm', 'Shapers classified by the type of cutting stroke are…',
  'Push type and draw type', ['Crank type and geared type', 'Standard and universal', 'Horizontal and vertical'],
  'In a push type the tool cuts as the ram moves away from the column; in a draw type it cuts on the stroke towards the column.', [35])
q('theory', 'h', 'In a push-type shaper, cutting takes place when the ram moves…',
  'Away from the column', ['Towards the column', 'In both directions', 'Vertically downwards'],
  'Push type (most common): cuts on the outward stroke. Draw type: cuts on the stroke towards the column.', [36])

# ============================ tools / materials ============================
q('tmat', 'e', 'The single-point cutting tool used on the shaper in the ME-106 lab is made of…',
  'High-speed steel (HSS)', ['Mild steel', 'Grey cast iron', 'Silicon carbide'],
  'The shaping log sheet lists a single-point cutting tool made of high-speed steel.', [37])
q('tools', 'm', 'Which of these is NOT a part of a single-point cutting tool (as in the shaping slides)?',
  'Tang', ['Heel', 'Minor flank', 'Side cutting edge'],
  'Parts: shank, face, base, heel, nose, side and end cutting edges, major and minor flanks. Tang is part of a file.', [38])
q('tmat', 'm', 'Which property lets a cutting tool keep its hardness at high cutting temperatures?',
  'Hot (red) hardness', ['High ductility', 'Low density', 'High electrical conductivity'],
  'Cutting-tool properties: hot hardness, toughness, wear resistance, chemical stability, shock resistance, low friction, favourable cost.', [39])
q('tmat', 'm', 'Which of these is NOT a desirable property of a cutting-tool material?',
  'High friction with the chip', ['Wear resistance', 'Toughness', 'Hot hardness'],
  'Low friction is desirable, along with hot hardness, toughness, wear resistance, chemical stability and shock resistance.', [39])
q('tmat', 'h', 'Which list of cutting-tool materials is in order of increasing hot hardness?',
  'Carbon tool steel → HSS → cemented carbide → ceramic', ['Ceramic → cemented carbide → HSS → carbon tool steel', 'HSS → carbon tool steel → ceramic → cemented carbide', 'Cemented carbide → carbon tool steel → ceramic → HSS'],
  'Hot hardness rises from carbon tool steel to HSS, carbides, ceramics, CBN and diamond.', [40])
q('tmat', 'm', 'Which of these is a cutting-tool material listed in the shaping slides?',
  'Cubic boron nitride (CBN)', ['Grey cast iron', 'Mild steel', 'Aluminium alloy'],
  'The slides list carbon tool steel, HSS, cemented carbide, ceramic, CBN and diamond.', [40])
q('def', 'm', 'Which tool angle reduces cutting force and helps the chip flow away?',
  'Rake angle', ['Clearance angle', 'Nose angle', 'Helix angle'],
  'Rake angle eases chip flow; clearance (relief) angle stops the flank rubbing the work.', [41])
q('tmat', 'h', 'Why are shaper tools made more robust, with smaller rake angles, than lathe tools?',
  'They take an impact at the start of every cutting stroke', ['They cut on both strokes', 'They never touch the work', 'They are made of softer steel'],
  'Shaping is an intermittent cut: the tool strikes the work at the beginning of each stroke, so it needs a strong edge.', [42])

# ============================ the lab job ============================
q('dims', 'e', 'What is the objective of the ME-106 shaping job?',
  'To reduce a block to 38 mm × 21 mm × 73 mm', ['To turn a bar to Ø38 mm', 'To cut a 22-tooth spur gear', 'To grind a flat face to finish'],
  'The shaping log sheet objective: reduce the given block to the desired dimensions 38 × 21 × 73 mm.', [43])
q('dims', 'e', 'What is the finished LENGTH of the ME-106 shaping block?',
  '73 mm', ['38 mm', '21 mm', '115 mm'],
  'The block is 73 mm long, 38 mm wide and 21 mm high.', [44])
q('dims', 'e', 'What is the finished HEIGHT (thickness) of the ME-106 shaping block?',
  '21 mm', ['38 mm', '73 mm', '25 mm'],
  'Height (thickness) = 21 mm; width = 38 mm; length = 73 mm.', [44])
q('dims', 'm', 'What is the finished WIDTH of the ME-106 shaping block?',
  '38 mm', ['21 mm', '73 mm', '34 mm'],
  'Width = 38 mm.', [44])
n('dims', 'm', 'What is the volume of the finished ME-106 shaping block?',
  '58 254 mm³', ['29 127 mm³', '5 825 mm³', '132 mm³'],
  '73 × 38 × 21 = 58 254 mm³. (132 mm is just the sum of the three dimensions.)', [44])
q('tools', 'e', 'Which tools are listed on the ME-106 shaping log sheet?',
  'HSS tool, scale with stand, marking block, try square, hammer, chalk, dot punch', ['Index plate, mandrel, catch pin, worm wheel', 'Emery paper, pumice powder, wire, solution', 'Wire electrode, dielectric, clamping wire'],
  'The shaping log sheet lists the HSS single-point tool, scale with base (stand), marking block, try square, hammer, chalk and dot punch.', [45])
q('tools', 'm', 'Which marking tool is used in the ME-106 shaping lab to check that edges are at 90°?',
  'Try square', ['Centre gauge', 'Dividing head', 'Outside caliper'],
  'The try square (written "tri-square" on the log sheet) is used while marking the block.', [45, 47])
q('tools', 'm', 'In the ME-106 shaping lab, the dot punch and hammer are used to…',
  'Make the marked lines permanent and clear', ['Hold the block in the vice', 'Give the depth of cut', 'Change the stroke length'],
  'After chalk-and-scale marking, punching makes the marking clear (notes: "punching to make marking clear").', [47, 48])
q('meas', 'm', 'What was the least count of the down-feed scale (the wheel above the tool head) on the ME-106 shaper?',
  '0.05 mm', ['0.02 mm', '0.01 mm', '0.5 mm'],
  'The shaping log sheet notes L.C. = 0.05 mm for the scale wheel above the head.', [46])
n('meas', 'm', 'With a down-feed least count of 0.05 mm, how many divisions lower the tool by 1 mm?',
  '20 divisions', ['50 divisions', '5 divisions', '10 divisions'],
  '1 mm / 0.05 mm = 20 divisions.', [46, 52])

# ============================ procedure ============================
s('proc', 'm', 'What is the correct order of the shaping procedure given in the ME-106 notes?',
  'Chalk & marking → punching → lock job in vice → align with cross feed → give depth → start machine',
  ['Lock job in vice → start machine → chalk & marking → punching → give depth → align with cross feed',
   'Punching → chalk & marking → give depth → start machine → lock job in vice → align with cross feed',
   'Start machine → give depth → chalk & marking → lock job in vice → punching → align with cross feed'],
  'Notebook procedure: 1 chalk & marking, 2 punching, 3 lock the job in the plain machine vice, 4 align with the cross-feed handle, 5 give depth with the depth handle, 6 start the machine.', [48])
q('proc', 'e', 'What is the FIRST step of the ME-106 shaping procedure?',
  'Mark the dimensions on the block', ['Start the machine with the black button', 'Lower the tool by 2 mm', 'Remove the waste material'],
  'Step 1: mark the dimensions using the scale with stand, marking block, try square, hammer and dot punch.', [49, 48])
q('proc', 'e', 'After marking, the block is…',
  'Fixed tightly in the vice (clamp)', ['Placed on a magnetic chuck', 'Mounted on a mandrel', 'Hung on a wire'],
  'Step 2: configure the machine so the block fits tightly using the clamp (vice).', [50])
q('proc', 'm', 'In the ME-106 procedure, how is the tool first brought up to the block?',
  'Using the ratchet-and-crank feed until the tool just touches', ['By starting the ram at full speed', 'By lowering the head 2 mm at once', 'By swivelling the tool head 90°'],
  'Step 3: using the ratchet and crank mechanism, bring the tool near the block so they just touch.', [51])
q('proc', 'm', 'For the first cut in the ME-106 shaping job, the tool head is lowered by…',
  '1 mm', ['0.05 mm', '2.5 mm', '5 mm'],
  'Step 4: using the wheel above the head, bring the head and tool down by 1 mm on the scale.', [52])
q('proc', 'm', 'In the ME-106 shaping job, by how much is the head lowered for later cuts?',
  '0.5 to 1 mm, as required', ['3 to 4 mm each time', 'Exactly 0.05 mm', '5 mm per cut'],
  'Step 6: after the first removal, bring the head down again by 0.5–1 mm as required (with the machine off).', [54])
q('proc', 'm', 'In the ME-106 shaping procedure, when is the depth of cut increased?',
  'With the machine switched off', ['While the ram is moving fast', 'During the cutting stroke', 'Only after all sides are done'],
  'The log sheet says the head is brought down again with the machine turned off.', [54, 61])
q('proc', 'm', 'How is the ME-106 shaping machine started?',
  'With the (black) push button', ['By turning the bull gear by hand', 'By pulling the ram', 'By tapping the clapper box'],
  'Step 5: start the machine using the black button.', [53])
q('proc', 'm', 'After one side of the block reaches size, what is done next?',
  'Switch off, remove waste, then repeat for the other sides', ['Switch to a grinding wheel', 'Leave the machine running and turn the block', 'Polish the side with a file only'],
  'Steps 7–9: once one side is at size, turn off the machine, remove waste, remove the block and repeat steps 2–8 for the other sides.', [55])
q('proc', 'h', 'Why must the crank on the ratchet be readjusted while shaping?',
  'So the table feeds in the correct direction during the run', ['So the ram stroke becomes longer', 'So the tool lifts on the cutting stroke', 'So the vice opens automatically'],
  'The log sheet: always readjust the crank on the ratchet so the base (table) moves in the correct direction while the machine runs.', [56])
q('proc', 'm', 'In the ME-106 notes, which handle is used to align the job with the tool before cutting?',
  'Cross-feed handle', ['Ram locking handle', 'Down-feed handle', 'Motor switch'],
  'Notes step 4: use the cross-feed handle to align the work with the tool; step 5: use the depth handle to give depth of cut.', [48])
q('proc', 'h', 'In the ME-106 notes, which step comes immediately BEFORE starting the machine?',
  'Giving the depth of cut with the depth handle', ['Chalk marking', 'Punching', 'Removing waste material'],
  'Order: … align with cross feed → give depth with depth handle → start machine.', [48])
n('proc', 'm', 'A face needs 2 mm removed. The first cut is 1 mm and later cuts are 0.5 mm each. How many cuts are needed in total?',
  '3', ['2', '4', '5'],
  '1 mm (first cut) + 0.5 + 0.5 = 2 mm, so 3 cuts.', [52, 54])

# ============================ precautions ============================
q('prec', 'e', 'Which dress precaution appears on the ME-106 shaping log sheet?',
  'Wear an apron', ['Wear loose sleeves', 'Wear sandals', 'Wear a wristwatch'],
  'Precaution 1: wear an apron.', [57])
q('prec', 'e', 'While the shaper is running, you should never…',
  'Put your hands on the machine', ['Stand at a safe distance', 'Watch the feed direction', 'Keep the area clear of chips'],
  'Precaution 2: never put hands on the machine while it is turned on.', [58])
q('prec', 'm', 'After touching the block, the head should NOT be lowered by more than about…',
  '2 mm', ['0.05 mm', '10 mm', '20 mm'],
  'Precaution 3: the head should not be brought down more than 2 mm after touching the block (too deep a cut can break the tool).', [59])
q('prec', 'm', 'Which precaution about the ratchet appears on the ME-106 shaping log sheet?',
  'Ensure the table moves in the correct direction', ['Keep the ratchet disengaged always', 'Oil the ratchet during cutting', 'Remove the ratchet before starting'],
  'Precaution 4: ensure the ratchet system is configured so the base moves in the correct direction.', [60])
q('prec', 'm', 'When should the depth of cut be changed on the shaper?',
  'Only when the machine is stopped', ['During the cutting stroke', 'During the return stroke at full speed', 'Any time, if you are quick'],
  'The log sheet procedure increases depth with the machine turned off.', [61])
q('prec', 'm', 'Before starting a shaper, the stroke length and position must be set so that…',
  'The tool clears the work at both ends of the stroke', ['The tool stays in the middle of the job', 'The ram hits the column', 'The tool touches the vice jaws'],
  'The tool must overrun the job slightly at both ends; otherwise it hits the work or the vice.', [62])
q('prec', 'm', 'Where should the operator NOT stand while the shaper is running?',
  'In front of the ram, in line with its stroke', ['Beside the table', 'At the feed handle side', 'Behind a safety guard'],
  'Never stand in line with the reciprocating ram.', [63])
q('prec', 'e', 'Chips on the shaper table should be removed…',
  'With a brush after stopping the machine', ['By hand while the ram moves', 'By blowing them towards others', 'They need not be removed'],
  'Clamp firmly and remove chips with a brush, never by hand.', [64])
q('prec', 'm', 'Which of these is NOT a shaping-lab precaution?',
  'Lower the head 5 mm per cut to save time', ['Wear an apron', 'Never put hands on the running machine', 'Check the ratchet feed direction'],
  'The head must not be lowered more than about 2 mm after touching the block.', [59, 57, 58, 60])

# ============================ advantages / applications ============================
q('adv', 'm', 'Which is an advantage of a shaper?',
  'Simple, cheap single-point tools and easy set-up', ['Very high production rate', 'Cuts on both strokes', 'Produces cylindrical parts'],
  'Shapers use inexpensive single-point tools and are easy to set up for small jobs.', [65])
q('adv', 'm', 'Which is a limitation of the shaper?',
  'It is slow, because it cuts only on one stroke', ['It cannot make flat surfaces', 'It needs a diamond tool', 'It can only cut round work'],
  'Cutting takes place only in the forward stroke, so production is slow; it suits small or medium jobs.', [66])
q('app', 'm', 'Which job is typically done on a shaper?',
  'Machining keyways, V-blocks and dovetails', ['Cutting threads on long shafts', 'Electroplating mild steel', 'Grinding crankshaft pins'],
  'Shapers machine flat horizontal, vertical and inclined surfaces, slots, keyways, V-blocks and dovetails.', [67])

# ============================ AR / TF ============================
ar('theory', 'h', 'The return stroke of a shaper is made faster than the cutting stroke.',
   'No metal is removed during the return stroke.', 'a',
   'Both true, and R explains A: since the return stroke is idle, it is speeded up (quick return) to save time.', [4, 5])
ar('parts', 'h', 'The clapper block lifts the tool during the return stroke.',
   'The clapper block is rigidly bolted to the tool head.', 'c',
   'A is true, R is false: the clapper block is HINGED on a pin, which is what lets it lift.', [26])
tf('theory', 'e', 'In a shaper, metal is removed on both the forward and return strokes.', False,
   'False. Metal is removed only on the forward stroke; the return stroke is idle.', [4])
tf('param', 'm', 'In a crank shaper with a 240°/120° split, the return stroke is faster than the cutting stroke.', True,
   'True. The return stroke uses only 120° of crank rotation versus 240°, so it takes half the time.', [16, 17])

# ============================ diagrams ============================
B.labels('shaping/shaper', 'p', diffs={'p': 'e'})
B.labels('shaping/shaper', 'w', only={'w': ['A', 'D', 'H', 'C', 'L']})
B.labels('shaping/shaper', 'f', only={'f': ['D', 'C', 'H']}, diffs={'f': 'm'})
QR = 'shaping/quick-return'
B.labels(QR, 'p', only={'p': ['A', 'B', 'C', 'D', 'E', 'G']}, diffs={'p': 'm'}, extra_parts=['Clapper block', 'Index plate'])
q('param', 'm', 'In the quick-return figure, which label marks the crank angle of the CUTTING stroke?', 'H', ['I', 'D', 'A'],
  'H is the larger (240°) arc of crank rotation, so the cutting stroke is the slow one. I is the 120° return arc.', [16], fig=QR, label='H', ask='which')
n('num', 'h', 'In the figure the crank-pin circle radius is exactly half the distance from the crank centre to the pivot. What is the ratio of cutting time to return time?',
  '2 : 1', ['1.5 : 1', '1 : 2', '3 : 1'],
  'cos θ = r/d = 0.5 → θ = 60°; return = 120°, cutting = 240°; ratio = 2.', [70], fig=QR)
q('parts', 'h', 'In the figure, what happens to the stroke length if the crank pin B is moved nearer the bull-gear centre?',
  'The stroke length decreases', ['The stroke length increases', 'The return becomes slower than the cut', 'Nothing changes'],
  'A smaller crank-pin radius makes the slotted lever swing through a smaller angle, so the ram stroke is shorter.', [19], fig=QR)
CB = 'shaping/clapper-box'
B.labels(CB, 'p', only={'p': ['A', 'B', 'C']}, diffs={'p': 'm'}, extra_parts=['Tool slide', 'Ram'])
q('parts', 'm', 'In sketch 2 of the figure, why has the tool swung up?',
  'On the return stroke the hinged clapper block lifts so the tool does not drag', ['The tool has broken', 'The depth of cut was increased', 'The tool head was swivelled for an angular cut'],
  'Friction on the return stroke swings the hinged clapper block up, so the tool slides over the work instead of digging in.', [26], fig=CB)
B.labels('shaping/spt-tool', 'p', cat='tools', diffs={'p': 'm'}, extra_parts=['Tang', 'Land'])
JB = 'shaping/job-q'
q('dims', 'e', 'In the figure of the ME-106 shaping block, what is the length of edge P?', '73 mm', ['38 mm', '21 mm', '83 mm'],
  'P is the length of the block: 73 mm.', [44], fig=JB, label='P')
q('dims', 'm', 'In the figure of the ME-106 shaping block, what is the dimension of edge Q?', '38 mm', ['21 mm', '73 mm', '28 mm'],
  'Q is the width of the block: 38 mm.', [44], fig=JB, label='Q')
q('dims', 'm', 'In the figure of the ME-106 shaping block, what is the dimension of edge R?', '21 mm', ['38 mm', '12 mm', '31 mm'],
  'R is the height (thickness): 21 mm.', [44], fig=JB, label='R')

B.save()
