"""Fitting question bank (incl. generated Vernier/micrometer readings). Correct option first."""
import json, os
from qlib import Bank, ROOT

B = Bank('fitting')
q, n, s, tf, ar = B.q, B.n, B.s, B.tf, B.ar

# ============================ definition / fits ============================
q('def', 'e', 'Fitting in the workshop is best defined as…',
  'Shaping, finishing and assembling parts by hand tools to accurate size', ['Removing metal with a rotating multi-point cutter', 'Joining parts permanently by melting them', 'Coating parts with a thin metal layer'],
  'Fitting is manual bench work: shaping, finishing and assembling components with hand tools to accurate dimensions.', [1])
q('def', 'e', 'Fitting work is normally done with the job held in a…',
  'Bench vice', ['Lathe chuck', 'Magnetic chuck', 'Dividing head'],
  'Fitting achieves accuracy by filing, sawing, drilling and tapping, usually with the job in a bench vice.', [2])
q('def', 'm', 'Which operations are typical of fitting (bench work)?',
  'Filing, sawing, drilling and tapping', ['Turning, facing and knurling', 'Slab, gang and straddle milling', 'Copper and nickel plating'],
  'The fitting lecture lists filing, sawing, drilling and tapping as the means of achieving accuracy.', [2])
q('app', 'm', 'Why is fitting still taught when CNC machines exist?',
  'It builds manual precision for prototyping, repair and maintenance', ['It is faster than CNC for every job', 'It needs no measuring tools', 'It replaces all machining'],
  'Fitting teaches manual precision before automation and is needed in prototyping, maintenance and R&D.', [3])
q('def', 'm', 'Which skill is the fitting lab mainly meant to develop?',
  'Dimensional accuracy, tolerance awareness and surface finishing', ['CNC part programming', 'Electroplating chemistry', 'Laser-beam alignment'],
  'The fitting lecture lists precision handwork, tolerance control, surface finishing and tool control.', [4])
q('ops', 'm', 'Which of these is NOT a fitting (bench-work) operation?',
  'Knurling', ['Chipping', 'Scraping', 'Dieing (external threading)'],
  'Fitting operations: marking, sawing, chipping, filing, scraping, drilling, tapping and dieing. Knurling is a lathe operation.', [5])
q('app', 'm', 'Which is a real-world application of manual fitting given in the fitting lecture?',
  'Fitting turbine blades and repairing gear housings', ['Mass-producing bolts on a CNC lathe', 'Electroplating car bumpers', 'Laser-cutting sheet metal'],
  'Aerospace, automotive, tool design and defence: e.g. fitting turbine blades, repairing shafts and gear housings.', [6])
q('def', 'e', 'How many main types of fit are there?',
  'Three: clearance, interference and transition', ['Two: loose and tight', 'Four: clearance, press, shrink and slide', 'One: precision'],
  'The fitting lecture: mainly three types — clearance, interference and transition.', [7])
q('def', 'e', 'In a clearance fit, the shaft is…',
  'Always smaller than the hole, giving free movement', ['Always larger than the hole, needing force', 'Sometimes larger, sometimes smaller', 'Exactly equal to the hole'],
  'Clearance fit: shaft smaller than hole, free movement (e.g. a shaft rotating in a bearing).', [8])
q('def', 'e', 'In an interference fit…',
  'The shaft is slightly larger, so force is needed to assemble', ['The shaft is smaller, so it rotates freely', 'There is always a large gap', 'No assembly is possible'],
  'Interference fit: shaft slightly larger than the hole, pressed in (e.g. a gear pressed onto a shaft).', [9])
q('def', 'm', 'A fit in which the tolerance zones overlap, giving either a slight clearance or slight interference, is a…',
  'Transition fit', ['Clearance fit', 'Interference fit', 'Running fit'],
  'Transition fit: conditional overlap, a light push fit.', [10])
q('app', 'm', 'A gear pressed onto a shaft so that it cannot slip is an example of…',
  'Interference fit', ['Clearance fit', 'Transition fit', 'Running fit'],
  'The fitting lecture gives "gear pressed into shaft" as the interference-fit example.', [9])

# ============================ lab tasks / material ============================
q('wmat', 'e', 'What material is used for the ME-106 fitting job?',
  'Mild-steel plate', ['Aluminium disc', 'Cast-iron block', 'Brass rod'],
  'The fitting lecture states the material is mild-steel plate, as per the workshop drawing.', [11])
q('proc', 'm', 'In the ME-106 fitting tasks, to what accuracy is the metal block filed in Task 1?',
  '±0.1 mm', ['±1 mm', '±0.001 mm', '±5 mm'],
  'Task 1: file a metal block to exact dimensions (±0.1 mm), to understand sawing and filing.', [12])
q('proc', 'm', 'Which ME-106 fitting task is meant to "prepare for assembly"?',
  'Drill and tap a hole', ['File a block to ±0.1 mm', 'Create a square/triangle shape', 'Assemble and inspect the fit'],
  'Task 3: drill and tap a hole — prepare for assembly.', [14])
q('proc', 'm', 'What is the final task (Task 4) of the ME-106 fitting lab?',
  'Assemble and inspect the fit', ['Drill and tap a hole', 'File a block to size', 'Mark out with a scriber'],
  'Task 4: assemble and inspect fit — the final project.', [15])
q('proc', 'm', 'Task 2 of the ME-106 fitting lab — creating a square/triangle shape — mainly develops…',
  'Accuracy with files', ['Speed with power tools', 'Skill in electroplating', 'Use of the lathe'],
  'Task 2: create a square/triangle shape — accuracy with files.', [13])
q('def', 'm', 'What is the stated objective of the ME-106 fitting lab?',
  'Learn manual accuracy and verify dimensions with measuring tools', ['Learn CNC programming of a mill', 'Learn to cut spur gears', 'Learn laser cutting of sheet'],
  'Objective: learn manual accuracy and verify dimensions with measuring tools.', [16])

# ============================ tools: lab list ============================
q('tools', 'e', 'Which tools are listed for the ME-106 fitting lab?',
  'Hacksaw, files, hammer, try square, centre punch, Vernier, bench vice', ['Index plate, mandrel, catch pin, worm wheel', 'Grinding wheel, dresser, magnetic chuck', 'Wire electrode, dielectric, power supply'],
  'The fitting lecture lists hacksaw; flat, round, half-round, triangular and square files; hammer; try square; centre punch; Vernier caliper; bench vice.', [17])
q('tools', 'e', 'In fitting, the bench vice is used to…',
  'Hold the workpiece firmly', ['Cut the metal', 'Measure the length', 'Mark drill points'],
  'Bench vice — holds the workpiece firmly.', [18])
q('tools', 'e', 'In fitting, the hacksaw is used for…',
  'Cutting metal (rough cutting)', ['Smooth finishing', 'Checking 90°', 'Measuring diameter'],
  'Hacksaw — rough cutting of metal.', [19])
q('tools', 'e', 'In fitting, files are used for…',
  'Smooth finishing and shaping', ['Holding the job', 'Marking drill points', 'Measuring depth'],
  'Files — smooth finishing and shaping.', [20])
q('tools', 'e', 'What is a try square used for?',
  'Checking that edges are at 90°', ['Measuring diameters to 0.02 mm', 'Cutting straight lines', 'Holding round bars'],
  'Try square — ensures 90° accuracy of edges and surfaces.', [21])
q('tools', 'e', 'In the fitting lab, the centre punch is used for…',
  'Marking drill points', ['Cutting the plate', 'Filing curves', 'Checking flatness'],
  'Centre punch — for layout and marking, especially drill points.', [22])
q('tools', 'm', 'According to the fitting lecture, the hammer is used for…',
  'Chipping and shaping (and striking punches)', ['Measuring surface finish', 'Checking squareness', 'Tightening the vice'],
  'Hammer — used for chipping and shaping.', [23])
q('tools', 'e', 'Which tools are used for precise measurement in the fitting lab?',
  'Vernier caliper and steel rule', ['Hacksaw and file', 'Centre punch and hammer', 'Bench vice and C-clamp'],
  'Vernier caliper / steel rule — for precise measurements.', [24])

# ============================ holding tools ============================
q('parts', 'm', 'Which of these is NOT a part of a bench vice?',
  'Tang', ['Fixed jaw', 'Movable jaw', 'Screw'],
  'Bench vice: fixed jaw, movable jaw, jaw plates, screw, handle, body/slide and base. The tang is part of a file.', [26])
q('parts', 'm', 'Why are soft (copper or aluminium) jaw caps fitted over the vice jaws?',
  'To protect finished surfaces from the serrated jaws', ['To make the jaws grip harder', 'To conduct heat away', 'To measure the job'],
  'The vice jaws carry hardened, serrated plates; soft caps prevent marks on finished work.', [27])
q('tools', 'm', 'When holding a job in a vice for filing, it should project…',
  'Only a little above the jaws, to avoid vibration', ['Far above the jaws for easy access', 'Below the jaws', 'At an angle of 45° to the jaws'],
  'Keeping the job low in the vice prevents it from springing and chattering.', [28])
q('tools', 'e', 'A tool with a V-groove used to hold round bars while marking or drilling is a…',
  'V-block', ['Angle plate', 'Surface plate', 'Try square'],
  'V-blocks hold cylindrical work steady.', [29])
q('tools', 'm', 'Which holding device is used to hold very small jobs or drills in the hand?',
  'Pin vice (or hand vice)', ['Bench vice', 'Angle plate', 'V-block'],
  'Pin vices hold small round jobs/drills; hand vices hold small jobs in the hand. C-clamps clamp work to a table.', [30])
q('tools', 'm', 'An L-shaped block used to hold work at 90° to the surface plate is an…',
  'Angle plate', ['V-block', 'Odd-leg caliper', 'Surface gauge'],
  'An angle plate has two faces at 90°.', [31])

# ============================ marking ============================
q('tools', 'e', 'A surface plate provides…',
  'A true flat reference surface for marking and checking flatness', ['A sharp edge for scribing', 'A magnetic surface for holding', 'A scale for measuring'],
  'The surface plate (cast iron, granite or hardened steel) is the flat datum for marking out and checking flatness.', [32])
q('tmat', 'm', 'Surface plates are commonly made of…',
  'Cast iron (or granite)', ['Aluminium', 'Copper', 'Wood'],
  'Surface plates are made of cast iron, granite or hardened steel.', [32])
q('tools', 'e', 'A hardened steel pointed tool used to scratch lines on metal is a…',
  'Scriber', ['Dot punch', 'Divider', 'File'],
  'The scriber scribes lines for marking out.', [33])
q('tools', 'm', 'Which tool scribes lines parallel to the surface plate at a set height?',
  'Surface gauge (scribing block)', ['Try square', 'Odd-leg caliper', 'Centre punch'],
  'The surface gauge (marking block) carries a scriber on an adjustable pillar.', [34])
q('tools', 'm', 'Which tool, with one bent leg and one pointed leg, is used to draw lines parallel to an edge?',
  'Odd-leg (jenny) caliper', ['Divider', 'Outside caliper', 'Try square'],
  'Odd-leg calipers also find the centre of round bars.', [35])
q('tools', 'm', 'Which tool is used to draw circles and arcs on metal?',
  'Divider', ['Odd-leg caliper', 'Scriber block', 'Centre punch'],
  'A divider has two pointed legs; it draws circles/arcs and transfers distances.', [36])
q('tools', 'm', 'The point angle of a dot punch is about…',
  '60°', ['90°', '118°', '30°'],
  'Dot punch ≈ 60° (light witness marks); centre punch ≈ 90° (deeper drill-start mark).', [37])
q('tools', 'm', 'The point angle of a centre punch is about…',
  '90°', ['60°', '45°', '135°'],
  'A centre punch has a 90° point to make a deeper mark for locating the drill.', [38])
q('tools', 'h', 'How does a dot punch differ from a centre punch?',
  'Dot punch (60°) makes light witness marks; centre punch (90°) makes a deeper drill mark', ['Dot punch (90°) makes deep drill marks; centre punch (60°) makes light marks', 'Both have a 118° point', 'Dot punch is used only on wood'],
  'Witness marks along scribed lines use the 60° dot punch; drill points are marked deeper with the 90° centre punch.', [37, 38])
q('tools', 'm', 'Which instrument is used for precise marking and height measurement from a surface plate?',
  'Vernier height gauge', ['Steel rule', 'Try square', 'Pin vice'],
  'The Vernier height gauge combines a scriber with a Vernier scale.', [39])
q('tools', 'm', 'Before scribing lines on a metal surface, it is often coated with…',
  'Chalk or marking blue', ['Grease', 'Water', 'Pumice powder'],
  'Chalk or marking blue makes the scribed lines clearly visible.', [40])

# ============================ measuring ============================
q('meas', 'e', 'A steel rule can measure to an accuracy of about…',
  '0.5 mm', ['0.02 mm', '0.01 mm', '0.001 mm'],
  'A steel rule reads to about 0.5 mm; a Vernier to 0.02 mm; a micrometer to 0.01 mm.', [41])
q('meas', 'e', 'The least count of a typical Vernier caliper is…',
  '0.02 mm', ['0.01 mm', '0.1 mm', '0.5 mm'],
  'Typical Vernier calipers have a least count of 0.02 mm.', [42])
q('meas', 'm', 'The least count of a Vernier caliper is equal to…',
  'One main-scale division minus one Vernier division', ['One main-scale division plus one Vernier division', 'Total Vernier divisions × main-scale division', 'The length of the Vernier scale'],
  'LC = 1 MSD − 1 VSD = (value of 1 MSD) ÷ (number of Vernier divisions).', [43])
n('meas', 'h', 'A Vernier has 50 divisions that span 49 main-scale divisions of 1 mm. What is its least count?',
  '0.02 mm', ['0.01 mm', '0.05 mm', '0.98 mm'],
  'LC = 1 MSD − 1 VSD = 1 − 49/50 = 0.02 mm (or 1 mm ÷ 50).', [43])
n('meas', 'h', 'A Vernier has 10 divisions equal to 9 main-scale divisions of 1 mm. What is its least count?',
  '0.1 mm', ['0.9 mm', '0.01 mm', '1 mm'],
  'LC = 1 − 9/10 = 0.1 mm.', [43])
q('meas', 'm', 'The reading of a Vernier caliper is…',
  'Main-scale reading + (coinciding Vernier division × least count)', ['Main-scale reading × coinciding division', 'Coinciding division × 0.5 mm', 'Main-scale reading − least count'],
  'Total = MSR + (k × LC).', [44])
q('meas', 'm', 'Which of these can a Vernier caliper NOT measure directly?',
  'Surface roughness', ['Outside diameter', 'Inside diameter', 'Depth of a hole'],
  'A Vernier caliper measures outside (outside jaws), inside (inside jaws) and depth (depth rod).', [46])
q('meas', 'm', 'Which part of a Vernier caliper is used to measure the depth of a hole?',
  'Depth rod (blade)', ['Inside jaws', 'Locking screw', 'Fixed jaw'],
  'The depth rod slides out from the end of the beam.', [45])
q('meas', 'e', 'The least count of a metric outside micrometer is…',
  '0.01 mm', ['0.02 mm', '0.1 mm', '0.5 mm'],
  'Pitch 0.5 mm ÷ 50 thimble divisions = 0.01 mm.', [47])
n('meas', 'm', 'A micrometer screw has a pitch of 0.5 mm and the thimble has 50 divisions. What is the least count?',
  '0.01 mm', ['0.025 mm', '0.1 mm', '0.05 mm'],
  'LC = pitch / divisions = 0.5 / 50 = 0.01 mm.', [47])
q('meas', 'm', 'The reading of a micrometer is…',
  'Sleeve reading + (thimble division × 0.01 mm)', ['Thimble division × 0.5 mm', 'Sleeve reading − thimble division', 'Sleeve reading × 0.01 mm'],
  'Total = sleeve (mm + 0.5 mm if visible) + thimble division × LC.', [48])
q('meas', 'm', 'Which part of a micrometer ensures a uniform measuring pressure?',
  'Ratchet stop', ['Lock nut', 'Anvil', 'Frame'],
  'The ratchet slips at a set torque so every reading is taken at the same pressure.', [50])
q('meas', 'm', 'Which of these is NOT a part of a micrometer?',
  'Depth rod', ['Anvil', 'Thimble', 'Sleeve'],
  'Micrometer parts: frame, anvil, spindle, sleeve (barrel), thimble, ratchet, lock nut. A depth rod belongs to a Vernier caliper.', [49])
q('meas', 'm', 'Outside and inside calipers are read by…',
  'Transferring the setting to a steel rule', ['Reading their built-in Vernier', 'Reading a dial', 'Counting thimble divisions'],
  'Plain calipers transfer a size; they have no scale of their own.', [51])
n('meas', 'h', 'A Vernier caliper shows a reading of 25.36 mm. When its jaws are closed, it reads +0.04 mm (positive zero error). What is the correct reading?',
  '25.32 mm', ['25.40 mm', '25.36 mm', '25.04 mm'],
  'Correct reading = observed − positive zero error = 25.36 − 0.04 = 25.32 mm.', [52])
n('meas', 'h', 'A micrometer reads 12.47 mm. With the faces closed it reads −0.02 mm (negative zero error). What is the correct reading?',
  '12.49 mm', ['12.45 mm', '12.47 mm', '12.27 mm'],
  'A negative zero error is added: 12.47 + 0.02 = 12.49 mm.', [52])

# ============================ cutting tools ============================
q('tools', 'm', 'Which part of a hacksaw is used to tension the blade?',
  'Wing nut', ['Handle', 'Tang', 'Heel'],
  'The wing nut on the frame tightens the blade to the correct tension.', [53])
q('tools', 'e', 'How should a hacksaw blade be fitted in the frame?',
  'Teeth pointing forward, away from the handle', ['Teeth pointing back towards the handle', 'Teeth facing upwards', 'Either way'],
  'The hacksaw cuts on the forward stroke, so the teeth must point forward.', [54])
q('proc', 'e', 'When sawing with a hacksaw, pressure is applied…',
  'Only on the forward stroke', ['Only on the return stroke', 'Equally on both strokes', 'Never; the saw cuts by its weight'],
  'The fitting procedure: apply pressure only on the forward stroke; release it on the return.', [55])
q('tools', 'h', 'For cutting a thin-walled tube, which hacksaw blade should be chosen?',
  'Fine pitch (more teeth per inch)', ['Coarse pitch (few teeth per inch)', 'Blade with no set', 'Wood-cutting blade'],
  'Fine-pitch blades keep at least 2–3 teeth on thin or hard sections; coarse pitch suits soft thick material.', [56])
q('tmat', 'm', 'Hacksaw blades are generally made of…',
  'High-carbon steel or HSS', ['Mild steel', 'Aluminium', 'Cast iron'],
  'Blades are hardened high-carbon steel or HSS.', [57])
q('tools', 'm', 'Which part of a file fits into the wooden handle?',
  'Tang', ['Heel', 'Point', 'Edge'],
  'File parts: tang, heel, face, edge, point. The tang goes into the handle.', [58])
q('tools', 'm', 'Files are classified by…',
  'Length, grade of cut, cross-section and type of cut', ['Colour and weight', 'Hardness of the handle', 'Speed of use'],
  'Files are specified by length, grade (cut), cross-sectional shape and single/double cut.', [59])
s('tools', 'h', 'Arrange file grades from COARSEST to FINEST.',
  'Rough → bastard → second cut → smooth → dead smooth', ['Bastard → rough → smooth → second cut → dead smooth', 'Dead smooth → smooth → second cut → bastard → rough', 'Second cut → rough → bastard → dead smooth → smooth'],
  'Rough is coarsest; dead smooth is finest.', [60])
q('tools', 'm', 'Which file grade is used for fast metal removal (rough work)?',
  'Bastard', ['Dead smooth', 'Smooth', 'Second cut'],
  'Bastard files remove metal quickly; smooth and dead-smooth files give the final finish.', [61])
q('tools', 'm', 'Which file would you use to finish an internal corner of less than 90°?',
  'Triangular (three-square) file', ['Round file', 'Flat file', 'Half-round file'],
  'Triangular files reach acute corners; round files enlarge holes; flat files do flat surfaces.', [63, 62])
q('tools', 'm', 'Which file is used for filing a concave curved surface and also a flat surface?',
  'Half-round file', ['Square file', 'Triangular file', 'Knife-edge file'],
  'The half-round file has one flat side and one curved side.', [63])
q('tools', 'e', 'Which file is used for filing large flat surfaces?',
  'Flat file', ['Round file', 'Triangular file', 'Square file'],
  'The fitting procedure: flat file for flat surfaces, round/half-round for curves.', [63, 79])
q('tmat', 'm', 'Files are made of…',
  'High-carbon steel, hardened and tempered', ['Mild steel, annealed', 'Grey cast iron', 'Aluminium alloy'],
  'Files must be hard to cut steel, so they are hardened and tempered high-carbon steel.', [64])
q('ops', 'h', 'Draw filing is done to…',
  'Give a fine finish by pushing the file sideways along the work', ['Remove metal quickly across the work', 'Cut a slot in the job', 'Mark a line on the job'],
  'Cross filing removes metal; draw filing (file held crosswise, moved along the work) gives a fine finish.', [65])
q('tools', 'm', 'Filings that clog the teeth of a file (pinning) are removed with a…',
  'File card (file cleaner)', ['Scriber', 'Dot punch', 'Try square'],
  'A file card is a wire brush for cleaning file teeth.', [66])
q('tools', 'h', 'The cutting angle of a flat cold chisel for mild steel is about…',
  '60°', ['30°', '90°', '120°'],
  'For mild steel the chisel point is ground to about 60°.', [67])
q('tools', 'm', 'Taps are used to cut…',
  'Internal threads', ['External threads', 'Keyways', 'Flat surfaces'],
  'Taps cut internal threads; dies cut external threads.', [68, 69])
s('tools', 'h', 'In what order are the taps of a set used?',
  'Taper tap → intermediate (second/plug) tap → bottoming tap', ['Bottoming tap → taper tap → intermediate tap', 'Intermediate tap → bottoming tap → taper tap', 'Bottoming tap → intermediate tap → taper tap'],
  'The taper tap starts the thread, the intermediate tap deepens it, and the bottoming tap cuts full threads to the bottom of a blind hole.', [68])
q('tools', 'm', 'A tap is turned using a…',
  'Tap wrench', ['Die stock', 'Chuck key', 'Spanner'],
  'A tap wrench turns the tap; a die stock holds and turns a die.', [69])
n('num', 'h', 'What tap-drill size is used for an M10 × 1.5 thread?',
  '8.5 mm', ['10 mm', '11.5 mm', '7.0 mm'],
  'Tap drill ≈ major diameter − pitch = 10 − 1.5 = 8.5 mm. (This is a drilling rule of thumb leaving some thread engagement; the lathe formula Dc = D − 2 × 0.6134p gives the full core diameter.)', [70])
n('num', 'h', 'What tap-drill size is used for an M8 × 1.25 thread?',
  '6.75 mm (≈ 6.8 mm)', ['8 mm', '9.25 mm', '5.5 mm'],
  'Tap drill ≈ 8 − 1.25 = 6.75 mm (a 6.8 mm drill is used).', [70])
q('proc', 'm', 'Before drilling a hole in fitting, the drill point is first…',
  'Centre-punched so the drill does not wander', ['Filed flat', 'Chamfered with a chisel', 'Polished'],
  'A centre-punch mark guides the drill point and stops it slipping.', [71, 77])

# ============================ striking ============================
q('tools', 'e', 'Which hammer is most used in fitting?',
  'Ball-peen hammer', ['Sledge hammer', 'Claw hammer', 'Soft rubber mallet'],
  'The ball-peen hammer (flat face + ball peen) is the usual fitting hammer.', [72])
q('tools', 'm', 'The hemispherical end of a ball-peen hammer is used for…',
  'Riveting and peening', ['Pulling nails', 'Checking flatness', 'Cutting sheet'],
  'The ball peen spreads metal for riveting and peening; the flat face is for striking.', [72])
q('tools', 'h', 'In a cross-peen hammer, the peen is…',
  'Wedge-shaped and at right angles to the handle', ['Hemispherical', 'Wedge-shaped and parallel to the handle', 'Flat and round'],
  'Cross peen: at right angles to the handle. Straight peen: parallel to the handle.', [73])
q('tools', 'm', 'Fitting hammers are specified by…',
  'Weight of the head', ['Length of the handle only', 'Colour of the head', 'Diameter of the face only'],
  'Hammers are specified by head weight (e.g. 0.25–1 kg) and are forged carbon steel.', [74])

# ============================ procedure ============================
q('proc', 'e', 'What is the FIRST step of the ME-106 fitting procedure?',
  'Safety check, then clamp the work firmly in the vice', ['Cutting with a hacksaw', 'Filing the edges', 'Submitting for inspection'],
  'Step 1: safety check — apron and goggles, tools in good condition, workpiece clamped firmly in the bench vice.', [75])
q('proc', 'm', 'In the ME-106 fitting procedure, which tools are used for marking?',
  'Steel rule, scriber and try square', ['Hacksaw and file', 'Micrometer and ratchet', 'Hammer and chisel'],
  'Step 2: mark dimensions using the steel rule and scriber; use the try square to keep 90° edges.', [76])
q('proc', 'm', 'Why are punch marks made at drill points (step 3 of the fitting procedure)?',
  'To prevent the drill bit from slipping', ['To harden the metal', 'To measure the hole depth', 'To file the edge'],
  'Step 3: light hammer blows make punch marks at drill points; purpose: prevent the drill bit from slipping.', [77])
q('proc', 'm', 'Which step comes immediately AFTER centre punching in the ME-106 fitting procedure?',
  'Cutting along the marked lines with a hacksaw', ['Marking with scriber and try square', 'Fitment and inspection', 'Safety check'],
  'Order: safety → marking → centre punching → cutting → filing → checking → fitment & inspection.', [78, 82])
q('proc', 'm', 'In the filing step of the ME-106 procedure, how should the file be moved for a smooth finish?',
  'With uniform motion', ['With short jerky strokes', 'Only on the return stroke', 'In circles'],
  'Step 5: use the flat file for flat surfaces and round/half-round for curves; maintain uniform motion.', [79])
q('proc', 'm', 'What is done in the "checking" step of the ME-106 fitting procedure?',
  'Measure with Vernier and try square; re-file if necessary', ['Polish with emery and pumice', 'Plate the job with nickel', 'Harden the job in a furnace'],
  'Step 6: measure with Vernier/try square to ensure accuracy; re-file if necessary.', [80])
q('proc', 'e', 'What is the LAST step of the ME-106 fitting procedure?',
  'Fitment and inspection by the instructor', ['Marking', 'Centre punching', 'Safety check'],
  'Step 7: assemble and check the fit; submit the piece for the instructor\'s inspection.', [81])
s('proc', 'h', 'What is the correct sequence of the ME-106 fitting procedure?',
  'Safety check → marking → centre punching → cutting → filing → checking → fitment & inspection',
  ['Marking → safety check → cutting → centre punching → checking → filing → fitment & inspection',
   'Safety check → cutting → marking → filing → centre punching → fitment & inspection → checking',
   'Centre punching → marking → safety check → filing → cutting → checking → fitment & inspection'],
  'The seven steps from the fitting lecture.', [82, 75, 76, 77, 78, 79, 80, 81])
q('proc', 'h', 'In the fitting procedure, why is marking done BEFORE cutting?',
  'The cutting and filing must follow the marked lines', ['Marking hardens the cutting line', 'The hacksaw needs chalk to cut', 'Marking is optional'],
  'Marking (scriber, rule, try square) sets out the lines that the saw and files then follow.', [76, 78])

# ============================ precautions ============================
q('prec', 'e', 'Which PPE is required in the fitting shop according to the lecture?',
  'Safety goggles, apron and closed shoes', ['Gloves only', 'Laser goggles', 'No PPE needed for hand tools'],
  'Always wear safety goggles, apron and closed shoes.', [83])
q('prec', 'm', 'Which precaution about the bench vice is given in the fitting lecture?',
  'Keep the jaws tight and parallel; clamp the job securely', ['Keep the jaws loose for easy filing', 'Hammer the vice handle to tighten it', 'Never use a vice'],
  'Keep bench vice jaws tight and parallel and clamp workpieces securely.', [84])
q('prec', 'e', 'What should be done with damaged hand tools?',
  'Do not use them', ['Use them carefully', 'Lend them to others', 'Use them only for rough work'],
  'Do not use damaged tools; keep tools sharp and properly gripped.', [85])
q('prec', 'm', 'Which precaution about force is given for filing and sawing?',
  'Do not apply excessive force', ['Apply maximum force on both strokes', 'Use your body weight on the return stroke', 'Strike the file with a hammer'],
  'Excess force breaks blades, spoils the finish and causes injury.', [86])
q('prec', 'e', 'Why must a file never be used without a handle?',
  'The pointed tang can pierce the hand', ['The file will cut slower', 'The teeth will clog', 'The file will bend'],
  'Never use a file without a handle — the tang can injure the palm.', [88])
q('prec', 'e', 'How should filings be cleared from the bench?',
  'With a brush, not by blowing or with bare hands', ['By blowing them away', 'By wiping with the palm', 'By leaving them'],
  'Blowing sends particles into eyes; bare hands get splinters.', [89])
q('prec', 'm', 'Which is correct practice when sawing with a hacksaw?',
  'Use steady, full-length strokes with correct blade tension', ['Use short fast strokes with a loose blade', 'Press hard on the return stroke', 'Twist the blade in the cut'],
  'Use the full blade length, steady strokes and correct tension; ease off near the end of the cut.', [90, 55])
q('prec', 'm', 'Which tool is UNSAFE to use?',
  'A chisel with a mushroomed head', ['A file with a tight handle', 'A hammer with a firm head', 'A sharp scriber with a cap'],
  'A mushroomed chisel head can throw off splinters; a loose hammer head can fly off.', [91])
q('prec', 'e', 'Which of these is a fitting-shop precaution from the lecture?',
  'Maintain a clean and safe workspace', ['Keep filings on the bench for reuse', 'Leave tools on the vice', 'Work without goggles for better view'],
  'A clean workspace is one of the listed precautions.', [87])
q('prec', 'm', 'The fitting-lab safety motto is…',
  'Safety = Skill + Awareness + Discipline', ['Speed = Skill + Force', 'Safety = Gloves + Goggles', 'Accuracy = Force + Time'],
  'From the fitting lecture safety slide.', [92, 'SAF25'])

# ============================ AR / TF ============================
ar('tools', 'h', 'A hacksaw blade is fitted with its teeth pointing away from the handle.',
   'A hacksaw cuts on the forward stroke.', 'a', 'Both true, and R explains A.', [54])
ar('tools', 'h', 'A centre punch is used before drilling.',
   'A centre punch has a 60° point angle.', 'c', 'A is true, but R is false: a centre punch is about 90°; the dot punch is about 60°.', [38, 37])
tf('tools', 'e', 'A try square is used to measure diameters to 0.02 mm.', False, 'False. A try square checks squareness (90°); diameters to 0.02 mm are measured with a Vernier caliper.', [21, 42])
tf('meas', 'm', 'A micrometer has a finer least count than a Vernier caliper.', True, 'True: 0.01 mm vs 0.02 mm.', [42, 47])

# ============================ diagrams ============================
B.labels('fitting/bench-vice', 'p', cat='tools', diffs={'p': 'e'})
B.labels('fitting/bench-vice', 'f', cat='tools', only={'f': ['C', 'D', 'B']}, diffs={'f': 'm'})
B.labels('fitting/marking-tools', 'p', cat='tools', diffs={'p': 'e'}, extra_parts=['Centre punch', 'Pin vice'])
B.labels('fitting/marking-tools', 'w', cat='tools', only={'w': ['D', 'E', 'G']})
B.labels('fitting/punches', 'p', cat='tools', diffs={'p': 'm'}, extra_parts=['Pin punch', 'Nail punch'])
B.labels('fitting/hacksaw', 'p', cat='tools', diffs={'p': 'e'}, extra_parts=['Tang', 'Tommy bar'])
q('tools', 'm', 'In the hacksaw figure, in which direction must pressure be applied?', 'Forward stroke (away from the handle)', ['Return stroke (towards the handle)', 'Both strokes equally', 'Downward only, without moving'],
  'The teeth (E) point away from the handle, so the saw cuts and is pressed only on the forward stroke.', [54, 55], fig='fitting/hacksaw')
B.labels('fitting/file-parts', 'p', cat='tools', diffs={'p': 'e'}, extra_parts=['Shank', 'Ferrule'])
B.labels('fitting/file-sections', 'p', cat='tools', diffs={'p': 'e'}, extra_parts=['Knife-edge file', 'Warding file'])
B.labels('fitting/file-sections', 'f', cat='tools', only={'f': ['C', 'E', 'D']}, diffs={'f': 'm'})
B.labels('fitting/hammers', 'p', cat='tools', diffs={'p': 'm'}, extra_parts=['Sledge hammer', 'Claw hammer'])
B.labels('fitting/vernier-parts', 'p', cat='meas', diffs={'p': 'e'})
B.labels('fitting/vernier-parts', 'f', cat='meas', only={'f': ['B', 'G', 'E']}, diffs={'f': 'm'})
B.labels('fitting/micrometer-parts', 'p', cat='meas', diffs={'p': 'e'}, extra_parts=['Depth rod', 'Vernier scale'])
B.labels('fitting/micrometer-parts', 'f', cat='meas', only={'f': ['F', 'E']}, diffs={'f': 'm'})

# ============================ generated readings ============================
G = json.load(open(os.path.join(ROOT, 'authoring', 'generated_readings.json')))
fmt = lambda v: f'{v:.2f} mm'
for i, v in enumerate(G['vernier']):
    r, M, k = v['reading'], v['msr'], v['k']
    cands = [round(M + k * 0.01, 2), round(M + 1 + k * 0.02, 2), round(M + (k + 1) * 0.02, 2), round(M + (k - 1) * 0.02, 2), round(M - 1 + k * 0.02, 2)]
    wr = []
    for c in cands:
        if c != r and c > 0 and fmt(c) not in [fmt(x) for x in wr] and len(wr) < 3:
            wr.append(c)
    q('meas', 'm', 'Read the Vernier caliper shown (least count 0.02 mm). The orange arrow marks the coinciding Vernier line.',
      fmt(r), [fmt(x) for x in wr],
      f'The Vernier zero lies just past {M} mm on the main scale, so MSR = {M} mm. The coinciding line is division {k} (label {k // 5}, then {k % 5} small division{'s' if k % 5 != 1 else ''}), so {k} × 0.02 = {k * 0.02:.2f} mm. Reading = {M} + {k * 0.02:.2f} = {r:.2f} mm.',
      [44, 42], fig=v['id'], tags=['generated', 'vernier'])
for i, v in enumerate(G['micrometer']):
    r, sl, th = v['reading'], v['sleeve'], v['thimble']
    half = (sl % 1) == 0.5
    cands = [round(sl - 0.5 + th * 0.01, 2) if half else round(sl + 0.5 + th * 0.01, 2), round(sl + (th + 1) * 0.01, 2), round(sl + (th - 1) * 0.01, 2), round(sl + 1 + th * 0.01, 2)]
    wr = []
    for c in cands:
        if abs(c - r) > 1e-6 and c > 0 and f'{c:.2f} mm' not in [w for w in wr] and len(wr) < 3:
            wr.append(f'{c:.2f} mm')
    q('meas', 'm', 'Read the micrometer shown (least count 0.01 mm).', fmt(r), wr,
      f'The last visible sleeve line is {sl:.1f} mm ({"a half-mm line below the datum is visible" if half else "no half-mm line is visible past the last whole mm"}). The thimble division on the datum line is {th}, so {th} × 0.01 = {th * 0.01:.2f} mm. Reading = {sl:.1f} + {th * 0.01:.2f} = {r:.2f} mm.',
      [48, 47], fig=v['id'], tags=['generated', 'micrometer'])

B.save()
