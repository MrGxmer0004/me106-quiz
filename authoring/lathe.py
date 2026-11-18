"""Centre lathe question bank. Correct option is always written first."""
from qlib import Bank

B = Bank('lathe')
q, n, s, tf, ar = B.q, B.n, B.s, B.tf, B.ar

# ============================ machine parts (text) ============================
q('def', 'e', 'A lathe is a machine tool used mainly to produce which kind of objects?',
  'Cylindrical (round) objects', ['Flat rectangular plates', 'Gear teeth on blanks', 'Internal keyways only'],
  'The lathe is employed generally to produce cylindrical objects by rotating the work against a single-point tool.', [1])
q('def', 'e', 'Which machine tool is often called the "mother of all machine tools"?',
  'Lathe', ['Milling machine', 'Shaper', 'Grinding machine'],
  'The handout calls the lathe the mother of all machine tools, because most other machine tools developed from it.', [2])
q('ops', 'e', 'Turning on a lathe removes excess material from the work to produce which kind of surface?',
  'A cylindrical or cone-shaped surface', ['A flat horizontal surface only', 'A helical gear tooth', 'A dovetail slot'],
  'Turning produces cylindrical or tapered (cone-shaped) surfaces on rotating work.', [3])
q('parts', 'm', 'Which of these is NOT one of the types of lathe listed in the ME-106 lathe handout?',
  'Slotting lathe', ['Capstan lathe', 'Turret lathe', 'Speed lathe'],
  'The handout lists engine, speed, turret, capstan and CNC lathes. "Slotting" is a different machine (a vertical shaper), not a lathe type.', [4])
q('parts', 'e', 'The most commonly used general-purpose lathe in engineering workshops is the…',
  'Engine (centre) lathe', ['Capstan lathe', 'Turret lathe', 'Speed lathe'],
  'The engine lathe (centre lathe) is the general-purpose lathe found in most workshops, including our machine shop.', [5])
q('theory', 'm', 'What is the working principle of a lathe?',
  'The work rotates while a single-point tool is fed against it', ['The tool rotates while the work is fed against it',
  'Both tool and work reciprocate in straight lines', 'An abrasive wheel rotates against fixed work'],
  'On a lathe the workpiece rotates and a single-point cutting tool is given feed motion. In milling and grinding it is the cutter or wheel that rotates.', [6, 7])
q('theory', 'e', 'In which of these machines does the WORKPIECE rotate while the tool is fed?',
  'Centre lathe', ['Milling machine', 'Surface grinder', 'Shaper'],
  'In a lathe the work rotates; in milling and grinding the cutter or wheel rotates, and in a shaper the tool reciprocates.', [7])
tf('theory', 'e', 'For metal cutting on a lathe there must always be relative motion between the tool and the workpiece.', True,
   'Cutting needs relative motion: the work rotates and the tool is fed, as noted in the lathe notes.', [8])
q('def', 'e', 'Centre-lathe turning belongs to which group of manufacturing processes?',
  'Metal removal (machining)', ['Metal joining (welding)', 'Forming (forging)', 'Casting (melting and solidification)'],
  'Turning removes metal as chips, so it is a metal-removal (machining) process.', [9])
q('parts', 'm', 'Which group of parts is mounted on the CARRIAGE of a centre lathe?',
  'Saddle, cross-slide, compound rest and tool post', ['Headstock, spindle and change gears',
  'Tailstock quill, dead centre and handwheel', 'Lead screw, feed rod and legs'],
  'The carriage slides on the bed and carries the saddle, cross-slide, compound rest and tool post (with the apron hanging in front).', [10, 26])
q('parts', 'e', 'Which part of a lathe is the main supporting structure on which the headstock, tailstock and carriage are mounted?',
  'Bed', ['Apron', 'Saddle', 'Column'],
  'The bed is the principal supporting structure; the headstock, tailstock and carriage are all mounted on it.', [11])
q('parts', 'm', 'On a lathe, the tailstock and carriage slide along the…',
  'Guideways (bedways) on top of the bed', ['Lead screw threads', 'Feed rod keyway', 'Cross-slide dovetail'],
  'The tailstock and carriage move over the guideways machined on the top face of the bed.', [12])
q('parts', 'm', 'Lathe beds are generally made of which material?',
  'Grey cast iron', ['Mild steel', 'High-speed steel', 'Aluminium alloy'],
  'The lecture states lathe beds are generally grey cast iron because of its damping, rigidity and self-lubricating qualities.', [13])
q('parts', 'm', 'Why is grey cast iron used for lathe beds?',
  'Good damping, rigidity and self-lubricating quality', ['High ductility and weldability',
  'Low density and high electrical conductivity', 'High red hardness at cutting temperatures'],
  'Grey cast iron damps vibration well, is rigid, and its graphite gives a self-lubricating surface on the ways.', [13])
q('parts', 'h', 'According to the lathe handout, a good lathe bed material should have which two properties?',
  'High compressive strength and high wear resistance', ['High ductility and high thermal expansion',
  'Low hardness and high electrical conductivity', 'High toughness and low density'],
  'The handout says bed material needs high compressive strength and high wear resistance; nickel-chromium alloyed cast iron is a good choice.', [14])
q('parts', 'h', 'Lathe bed guideways are of two types. Which pair is correct?',
  'Inner ways and outer ways', ['Upper ways and lower ways', 'Live ways and dead ways', 'Cross ways and compound ways'],
  'The lecture names the two types of guideways as inner ways and outer ways.', [15])
q('parts', 'e', 'On which side of the lathe bed is the headstock mounted (operator facing the lathe)?',
  'Left-hand side', ['Right-hand side', 'Middle, under the carriage', 'Below the bed'],
  'The headstock is on the left-hand side of the bed; the tailstock is on the right.', [16, 21])
q('parts', 'm', 'Which lathe part houses the main spindle, the speed-change gear box and the change gears?',
  'Headstock', ['Tailstock', 'Apron', 'Carriage'],
  'The headstock houses the main spindle, speed-change mechanism and change gears.', [17])
q('parts', 'm', 'Besides varying spindle speed, the headstock gear box also…',
  'Transmits power to the feed rod and lead screw', ['Moves the tailstock along the bed',
  'Locks the carriage for parting-off', 'Holds the dead centre'],
  'The headstock gear box varies spindle speed and transmits power to the feed rod and lead screw.', [18])
q('parts', 'e', 'The chuck or face plate of a lathe is attached to the…',
  'Headstock spindle', ['Tailstock quill', 'Cross-slide', 'Lead screw'],
  'The chuck or face plate is mounted on the headstock spindle, which grips and rotates the work.', [19])
q('parts', 'e', 'Which part of the lathe carries the LIVE centre?',
  'Headstock spindle', ['Tailstock quill', 'Tool post', 'Compound rest'],
  'The live centre sits in the headstock spindle and rotates with the work. The tailstock carries the dead centre.', [20])
q('parts', 'e', 'Which part of the lathe carries the DEAD centre?',
  'Tailstock', ['Headstock', 'Carriage', 'Apron'],
  'The tailstock carries the dead centre, which does not rotate; the headstock spindle carries the live centre.', [24])
q('parts', 'm', 'Which of these is a function of the tailstock?',
  'Supporting long work and holding drills or reamers', ['Giving speed changes to the spindle',
  'Engaging the half-nut for threading', 'Swivelling the tool for tapers'],
  'The tailstock supports the free end of the work and holds tools such as drills, reamers and taps.', [22])
q('parts', 'e', 'Why can the tailstock be moved along the bed?',
  'To accommodate workpieces of different lengths', ['To change the spindle speed',
  'To set the thread pitch', 'To lock the carriage'],
  'The tailstock slides on the guideways so work of different lengths can be supported.', [23])
q('parts', 'm', 'Which of these is a part of the TAILSTOCK?',
  'Quill (tailstock spindle)', ['Half-nut lever', 'Tumbler gears', 'Compound slide'],
  'The tailstock has a body, adjustable base, spindle (quill), feed screw handwheel and a locking lever.', [25])
q('parts', 'm', 'Which part of the lathe supports, moves and controls the cutting tool?',
  'Carriage', ['Headstock', 'Tailstock', 'Bed'],
  'The carriage serves as the supporting, moving and controlling part of the cutting tool.', [26])
q('parts', 'm', 'The H-shaped part of the carriage that fits over the bed and slides along the ways is the…',
  'Saddle', ['Apron', 'Compound rest', 'Tool post'],
  'The saddle is H-shaped, fits over the bed, slides along the guideways and can be locked in any position.', [27])
q('param', 'm', 'Movement of the saddle parallel to the lathe axis gives the…',
  'Longitudinal feed', ['Depth of cut', 'Cutting speed', 'Taper angle'],
  'Saddle movement along the axis is the (longitudinal) feed; cross-slide movement sets the depth of cut.', [28])
q('parts', 'e', 'Which part moves the lathe tool at right angles to the lathe axis?',
  'Cross-slide', ['Saddle', 'Tailstock quill', 'Feed rod'],
  'The cross-slide sits on the saddle and moves the tool perpendicular to the work axis.', [29])
q('param', 'm', 'On a lathe, the depth of cut is set by moving the…',
  'Cross-slide', ['Tailstock', 'Saddle along the bed', 'Lead screw'],
  'The perpendicular distance moved by the cross-slide (via its handwheel) is the depth of cut.', [30])
q('parts', 'e', 'The compound rest is mounted directly on top of the…',
  'Cross-slide', ['Bed', 'Tailstock', 'Headstock'],
  'The compound rest (top slide) is mounted on the cross-slide, and the tool post sits on the compound rest.', [31])
q('parts', 'e', 'Which lathe part has a base graduated in degrees and is used for short tapers and angular cuts?',
  'Compound rest', ['Cross-slide', 'Apron', 'Tailstock'],
  'The compound rest swivels on a base graduated in degrees for angular cuts and tapers.', [32])
q('ops', 'm', 'In taper turning by the compound-rest method, how is the feed given?',
  'By hand, with the compound-slide handwheel', ['Automatically by the lead screw',
  'Automatically by the feed rod', 'By setting over the tailstock'],
  'The compound slide has no power feed; its handwheel is turned by hand to feed the tool along the taper.', [33, 43])
q('parts', 'e', 'Which part holds the cutting tool rigidly on a lathe?',
  'Tool post', ['Apron', 'Saddle', 'Quill'],
  'The tool post is mounted on the compound rest and clamps the tool rigidly.', [34])
q('parts', 'm', 'Which of these is NOT a type of lathe tool post?',
  'Twelve-way tool post', ['Single-screw tool post', 'Four-way tool post', 'Eight-way tool post'],
  'The lecture lists single-screw, four-way and eight-way tool posts.', [35])
q('parts', 'm', 'The carriage handwheel, half-nut lever and feed lever are located on the…',
  'Apron', ['Headstock', 'Tailstock', 'Compound rest'],
  'The apron hangs in front of the carriage and contains the carriage handwheel, half-nut lever and feed lever.', [36])
q('parts', 'm', 'Which shaft drives the carriage or cross-slide for turning, boring and facing (not threading)?',
  'Feed rod', ['Lead screw', 'Spindle', 'Tailstock screw'],
  'The feed rod transmits power from the feed box to move the carriage or cross-slide for ordinary feeds.', [37])
q('parts', 'e', 'The lead screw of a lathe is used for…',
  'Thread cutting only', ['Facing and turning feeds', 'Moving the tailstock', 'Changing spindle speed'],
  'The lead screw is a long threaded shaft used only for thread cutting; it is disengaged for normal turning.', [38])
q('parts', 'm', 'For thread cutting, the carriage is connected to the lead screw through the…',
  'Half-nut mechanism', ['Tumbler gears', 'Chuck key', 'Tailstock lock'],
  'Closing the half-nuts on the lead screw makes the carriage advance exactly one pitch per spindle revolution.', [39])
q('parts', 'e', 'Which part of a lathe collects the chips and coolant that fall from the work?',
  'Chip tray (chip pan)', ['Apron', 'Saddle', 'Gear box'],
  'The chip tray (chip pan) under the bed collects chips; the legs support the machine.', [40])
q('parts', 'h', 'On the lathe headstock, the tumbler gears are used to…',
  'Reverse or engage/disengage the feed', ['Lock the spindle for chuck changing',
  'Move the tailstock quill', 'Set the compound rest angle'],
  'The lecture lists tumbler gears for forward/reverse and engage/disengage of the feed drive.', [41])
q('param', 'm', 'Which of the three lathe feeds is given ONLY by hand?',
  'Angular feed', ['Longitudinal feed', 'Cross feed', 'Both longitudinal and cross feed'],
  'Longitudinal and cross feeds can be by hand or power; angular feed (compound slide swivelled) is hand-operated only.', [42, 43])
q('param', 'm', 'Feed given by swivelling the compound slide to the required angle is called…',
  'Angular feed', ['Cross feed', 'Longitudinal feed', 'Rapid feed'],
  'There are three feeds: longitudinal (parallel to axis), cross (perpendicular) and angular (compound slide swivelled).', [42])
q('parts', 'm', 'Which of these is NOT used to specify a centre lathe?',
  'Number of teeth on the chuck jaws', ['Distance between centres', 'Swing over bed', 'Length of bed'],
  'A lathe is specified by bed length, distance between centres, swing over bed and carriage, power, lead-screw pitch, speeds, feeds and bed width.', [44])
q('def', 'm', 'The "swing" of a lathe means…',
  'The largest work diameter that can rotate over the bed', ['The length of the bed',
  'The distance moved by the carriage per revolution', 'The angle through which the compound rest swivels'],
  'Swing is the largest diameter of work that can be swung (rotated) over the lathe bed.', [45])

# ============================ work holding ============================
q('tools', 'm', 'Which of these is NOT a standard way of holding work on a lathe?',
  'Magnetic chuck with table dogs', ['Between centres with a dog', 'In a 4-jaw chuck', 'On a face plate'],
  'Work is held between centres, on a mandrel, in a chuck, on a face plate/angle plate or in a collet. Magnetic chucks with dogs are a grinding-machine feature.', [46])
q('tools', 'm', 'When work is turned between centres, what actually drives (rotates) the workpiece?',
  'A lathe dog clamped to the work, driven by the catch plate', ['Friction at the dead centre',
  'The lead screw', 'The tailstock quill'],
  'A dog (carrier) is clamped to the work and its tail is driven by the catch (dog) plate on the spindle.', [47])
q('tools', 'e', 'In which chuck do all the jaws move together, so the work is centred automatically?',
  '3-jaw chuck', ['4-jaw chuck', 'Face plate', 'Magnetic chuck'],
  'In a 3-jaw (self-centring) chuck all three jaws move simultaneously; in a 4-jaw chuck each jaw moves independently.', [48])
q('tools', 'm', 'A 3-jaw self-centring chuck is suitable for holding which work?',
  'Round and hexagonal work', ['Irregular castings', 'Square and rectangular blocks', 'Work needing off-centre turning'],
  'The 3-jaw chuck holds cylindrical and hexagonal work; irregular shapes need a 4-jaw chuck.', [48])
q('tools', 'e', 'In a 4-jaw chuck the jaws…',
  'Move independently, each by its own screw', ['All move together through a scroll',
  'Do not move at all', 'Move only in pairs'],
  'Each jaw of a 4-jaw (independent) chuck is moved separately, so the work must be centred manually.', [49])
q('tools', 'm', 'Which chuck is preferred for holding an irregular or square workpiece?',
  '4-jaw independent chuck', ['3-jaw self-centring chuck', 'Collet chuck', 'Drill chuck'],
  'The independent jaws of a 4-jaw chuck can grip irregular shapes, which a self-centring chuck cannot.', [49])
q('tools', 'h', 'What is the main drawback of a 4-jaw independent chuck compared with a 3-jaw chuck?',
  'The work must be centred manually, which takes time', ['It cannot hold round work',
  'It grips the work less firmly', 'It cannot be used for facing'],
  'Because the jaws move independently, the work has to be trued (centred) by hand; a 3-jaw chuck centres automatically.', [49, 51])
q('tools', 'h', 'Which statement about 4-jaw chuck jaws is correct?',
  'They are reversible', ['They can only move together', 'They are fixed and cannot be adjusted', 'They are magnetised'],
  'The lecture states the jaws of a 4-jaw chuck are reversible and each moves independently.', [50])
q('tools', 'h', 'Compared with a 3-jaw chuck, a 4-jaw independent chuck…',
  'Grips more firmly but is slower to set up', ['Grips less firmly but centres automatically',
  'Can hold only round work', 'Cannot be used with HSS tools'],
  'A 4-jaw chuck gives a stronger grip and holds any shape, but centring is manual. A 3-jaw chuck is quick to set because it self-centres.', [51])
q('tools', 'm', 'A collet holds bar stock by…',
  'Being squeezed onto the bar through its slits', ['Magnetic attraction', 'Independent screw-driven jaws', 'Friction at a dead centre'],
  'A collet has slits (three in the lecture) so a sleeve can squeeze it onto the bar.', [52])
q('tools', 'm', 'Irregular work that cannot be held in a chuck is clamped to the…',
  'Face plate', ['Tool post', 'Catch plate only', 'Compound rest'],
  'A face plate is attached to the spindle and work is bolted/clamped to it.', [53])
q('tools', 'e', 'Chuck jaws are tightened and loosened using a…',
  'Chuck key', ['Tap wrench', 'Allen key on the tailstock', 'Spanner on the lead screw'],
  'A chuck key turns the chuck screw (or scroll) to move the jaws; always remove it before starting.', [54])

# ============================ tools used in our lab ============================
q('tools', 'e', 'In the ME-106 lathe lab, which items were used for MARKING the job?',
  'Chalk, marker, marking stand and marking plate', ['Scriber, dot punch and centre punch',
  'Vernier height gauge and angle plate', 'Divider and odd-leg caliper'],
  'The ME-106 lathe log sheet lists chalk, marking stand, marking plate and marker as the marking tools.', [55])
q('tools', 'e', 'In the ME-106 lathe lab, the diameter of the job was checked with an…',
  'Outside caliper and steel scale', ['Inside micrometer only', 'Dial indicator only', 'Bevel protractor'],
  'The log sheet lists an outside caliper and scale for measuring the job.', [56, 59])
q('tools', 'm', 'Which of these is NOT in the list of tools used in the ME-106 lathe lab?',
  'Dividing head', ['Lathe job carrier', 'Marking stand', 'Outside caliper'],
  'The lathe log sheet lists chalk, marking stand, marking plate, outside caliper, scale, marker, lathe job carrier and catch. A dividing head is a milling accessory.', [55, 56, 57])
q('tools', 'm', 'In the ME-106 lathe lab, the job was held in which device?',
  'Four-jaw chuck', ['Three-jaw chuck', 'Collet', 'Machine vice'],
  'The procedure says to fix the workpiece in the four-jaw chuck after marking 115 mm.', [57, 115])
q('tools', 'm', 'The 2025 ME-106 lathe log sheet adds which items to the tool list?',
  'Tool holder, wrench and chuck', ['Grinding wheel and coolant', 'Index plate and mandrel', 'Hacksaw and file'],
  'The 2025 log sheet also lists a lathe tool holder, a wrench and the chuck.', [58])
q('meas', 'm', 'An outside caliper has no scale. How is the measured diameter read?',
  'By transferring the setting to a steel rule', ['Directly from its Vernier', 'From its dial', 'From the cross-slide dial'],
  'An outside caliper only transfers a size; you read it by placing the legs against a steel rule.', [59])

# ============================ materials ============================
q('wmat', 'e', 'What is the workpiece material of the ME-106 lathe job?',
  'Low-carbon (mild) steel', ['Aluminium', 'Cast iron', 'High-speed steel'],
  'The lathe notes state the job is low-carbon steel, i.e. mild steel.', [60])
q('wmat', 'm', 'Mild (low-carbon) steel contains approximately…',
  'Less than 0.3% carbon', ['0.6–1.5% carbon', '2–4% carbon', 'About 6.67% carbon'],
  'Mild steel is low-carbon steel with less than about 0.3% C. 0.6–1.5% is high-carbon steel and 2–4% C is cast iron.', [61])
q('tmat', 'e', 'The cutting tool used on the lathe in the ME-106 lab is made of…',
  'High-speed steel (HSS)', ['Mild steel', 'Grey cast iron', 'Aluminium oxide'],
  'The lathe notes and log sheets use an HSS single-point tool.', [62])
q('tmat', 'e', 'Which basic rule applies to the tool and workpiece materials in machining?',
  'The tool must be harder than the workpiece', ['The workpiece must be harder than the tool',
  'Both must have equal hardness', 'Hardness does not matter in turning'],
  'The tool must always be harder than the material it cuts.', [63])
q('tmat', 'm', 'The common 18-4-1 high-speed steel contains about…',
  '18% W, 4% Cr, 1% V', ['18% Cr, 4% Ni, 1% C', '18% C, 4% Mn, 1% Si', '18% Co, 4% Mo, 1% W'],
  '18-4-1 HSS has 18% tungsten, 4% chromium and 1% vanadium (with ~0.7% C).', [64])
q('tmat', 'm', 'Why is high-speed steel called "high speed" steel?',
  'It keeps its hardness at high cutting temperatures', ['It is made by a high-speed rolling process',
  'It can only be used at high spindle speeds', 'It cools down quickly after cutting'],
  'HSS retains its hardness (red hardness) at the high temperatures produced by high-speed machining.', [65])
q('wmat', 'm', 'Medium-carbon steel contains about…',
  '0.3–0.6% carbon', ['Less than 0.1% carbon', '1.5–2.0% carbon', '2.1–4% carbon'],
  'Standard ranges: low < 0.3%, medium 0.3–0.6%, high 0.6–1.5% C. (The class notebook says 1.5–2% for medium-carbon steel. That is wrong; see corrections.md #1.)', [66])
q('wmat', 'h', 'An iron–carbon alloy with about 3% carbon is classed as…',
  'Cast iron', ['High-carbon steel', 'Medium-carbon steel', 'High-speed steel'],
  'Steel contains up to about 2.1% C. Above that the alloy is cast iron. 6.67% C corresponds to cementite (Fe₃C).', [67])
q('wmat', 'h', 'High-carbon steel contains about…',
  '0.6–1.5% carbon', ['0.05–0.3% carbon', '2.1–4.0% carbon', '6.67% carbon'],
  'High-carbon steel has roughly 0.6–1.5% C. 6.67% C is cementite, not a steel.', [66, 67])

# ============================ single point tool ============================
q('tools', 'm', 'Which of these is NOT a part of a single-point cutting tool?',
  'Tang', ['Shank', 'Flank', 'Nose'],
  'Single-point tool parts are shank, face, flank, heel, base, nose and point. Tang is part of a file.', [68])
q('def', 'm', 'On a single-point tool, the surface over which the chip flows is the…',
  'Face', ['Flank', 'Base', 'Heel'],
  'The face is the top surface over which the chip slides; the flank faces the work below the cutting edge.', [69])
q('def', 'm', 'The angle that prevents the tool flank from rubbing against the work is the…',
  'Clearance (relief) angle', ['Rake angle', 'Point angle', 'Helix angle'],
  'The clearance (relief) angle gives the flank room so it does not rub on the machined surface.', [71])
q('def', 'm', 'Which tool angle mainly helps the chip flow away and reduces the cutting force?',
  'Rake angle', ['Clearance angle', 'Lip angle', 'Taper angle'],
  'Rake angle is the slope of the tool face; a positive rake eases chip flow and lowers cutting force.', [70, 'SHP41'])

# ============================ operations ============================
q('ops', 'e', 'Which lathe operation produces a flat surface at the end of the work and reduces its length?',
  'Facing', ['Straight turning', 'Knurling', 'Grooving'],
  'Facing machines the end of the work flat; the tool is fed perpendicular to the axis.', [73])
q('ops', 'm', 'In facing, the tool is fed…',
  'Perpendicular to the lathe axis', ['Parallel to the lathe axis', 'At the half-taper angle', 'Along a helix'],
  'In facing the tool moves across the face, perpendicular to the axis (cross feed).', [73])
q('ops', 'e', 'Which operation reduces the diameter of the work along its whole length?',
  'Straight (plain) turning', ['Facing', 'Parting-off', 'Chamfering'],
  'Straight turning reduces the diameter along the length; the tool is fed parallel to the axis.', [74])
q('ops', 'e', 'Reducing the diameter over only part of the length, leaving shoulders of different diameters, is called…',
  'Step turning', ['Taper turning', 'Facing', 'Knurling'],
  'Step turning gives steps (shoulders) of different diameters along the job.', [75])
q('ops', 'e', 'The operation of bevelling the sharp end edge of a turned job is…',
  'Chamfering', ['Knurling', 'Facing', 'Grooving'],
  'Chamfering creates a slope at the end edge to remove burrs and sharp corners; our job has a 1 × 45° chamfer.', [76])
q('ops', 'e', 'Knurling on a lathe is done to…',
  'Emboss a pattern on the surface for grip', ['Cut a helical thread', 'Cut off the finished job', 'Enlarge a drilled hole'],
  'A knurling tool is pressed against the rotating work to emboss a diamond or straight pattern, e.g. on handles.', [77])
q('ops', 'm', 'A narrow recess cut at the end of a thread (as in our job) is made by…',
  'Grooving with a grooving tool', ['Knurling', 'Reaming', 'Chamfering'],
  'Grooving uses a tool shaped to the groove; the ME-106 job has a 5 mm groove next to the thread.', [78])
q('ops', 'm', 'In parting-off on a lathe…',
  'The carriage is locked and the tool is plunged radially', ['The tool is fed parallel to the axis',
  'The compound rest is swivelled', 'The lead screw drives the tool'],
  'Parting cuts the job off the bar; longitudinal feed is fixed and the tool is fed in radially until the work separates.', [79])
q('ops', 'm', 'Why is a centre hole drilled at the end of the workpiece?',
  'So the work can be supported between centres', ['To start a thread', 'To reduce weight', 'To hold a knurling tool'],
  'Centre drilling makes a conical seat so the work can be held on a centre (between centres) in any machine.', [80])
q('ops', 'h', 'Which tool is used for centre drilling on a lathe?',
  'Centre drill held in the tailstock', ['Parting tool in the tool post', 'Knurling tool', 'Boring bar in the chuck'],
  'A combined centre drill is held in a drill chuck in the tailstock and fed into the rotating work.', [80, 22])
q('ops', 'm', 'A uniform decrease in diameter along the length of the work is called a…',
  'Taper', ['Chamfer', 'Groove', 'Knurl'],
  'A taper is a uniform change of diameter along the length, specified by the difference in diameters over the length.', [81])
q('ops', 'm', 'Which of these is NOT a method of taper turning on a lathe?',
  'Straddle method', ['Compound-rest method', 'Tailstock set-over method', 'Form-tool method'],
  'Taper-turning methods: compound rest, form tool, tailstock set-over and taper-turning attachment. Straddle is a milling set-up.', [82])
q('ops', 'h', 'Which taper-turning method suits a long, gentle taper on work held between centres?',
  'Tailstock set-over method', ['Compound-rest method', 'Form-tool method', 'Parting-off method'],
  'Setting the tailstock over suits long, gentle tapers between centres. The compound rest suits short, steep tapers.', [83])
q('ops', 'h', 'The compound-rest method of taper turning is best suited for…',
  'Short, steep tapers', ['Long, gentle tapers', 'Very long shafts between centres', 'Internal threads'],
  'The compound slide has limited travel, so it is used for short tapers with large angles.', [83])
q('ops', 'm', 'Which taper-turning method needs a tool whose cutting edge is ground to the taper angle?',
  'Form-tool method', ['Tailstock set-over method', 'Compound-rest method', 'Taper attachment'],
  'In the form-tool method a broad tool with an edge at the taper angle is plunged in; it suits very short tapers.', [82, 83, 86])
q('ops', 'm', 'Boring on a lathe…',
  'Enlarges an existing hole', ['Produces a centre hole', 'Cuts off the job', 'Makes a diamond pattern'],
  'Boring enlarges an already-drilled hole; reaming finishes a hole to size.', [85])
q('ops', 'h', 'In form turning, the shape produced on the work is obtained by…',
  'A tool ground to the required profile', ['Swivelling the compound rest',
  'Using the lead screw', 'Setting over the tailstock'],
  'Form turning reproduces the tool profile on the work, e.g. convex or concave forms.', [86])
q('ops', 'm', 'Which of these operations is NOT normally done on a centre lathe?',
  'Gear hobbing', ['Knurling', 'Boring', 'Thread cutting'],
  'Lathe operations include facing, turning, taper turning, threading, knurling, drilling, boring, reaming and parting. Gear hobbing needs a hobbing machine.', [72])
q('adv', 'm', 'Why is the centre lathe called a versatile machine?',
  'One machine can face, turn, thread, drill, bore and knurl', ['It can cut gears with an index plate',
  'It cuts on both forward and return strokes', 'It works without any cutting tool'],
  'A single centre lathe performs many operations: facing, turning, taper turning, threading, drilling, boring, knurling and parting.', [131])
q('app', 'h', 'For which kind of part is a centre lathe LEAST suitable?',
  'Flat rectangular plates with slots', ['Shafts and pins', 'Bolts and threaded rods', 'Bushes and collars'],
  'The lathe suits rotationally symmetric parts. Flat slotted plates are milled or shaped. Lathes are also slow for mass production compared with capstan/turret/CNC.', [132])

# ============================ threads ============================
q('ops', 'e', 'Thread cutting on a lathe produces a…',
  'Helical groove on a cylindrical surface', ['Straight groove parallel to the axis',
  'Diamond pattern on the surface', 'Conical centre hole'],
  'A screw thread is a helical groove; any pitch, shape and size can be cut on a lathe with a single-point tool.', [87])
q('ops', 'm', 'During thread cutting, how far must the tool advance per revolution of the work?',
  'One pitch of the thread', ['Half the pitch', 'Twice the pitch', 'The depth of the thread'],
  'The lead screw drives the carriage so that the longitudinal feed per revolution equals the pitch.', [88])
q('def', 'm', 'The distance between corresponding points on adjacent threads, measured along the axis, is the…',
  'Pitch', ['Depth', 'Crest', 'Flank'],
  'Pitch is the axial distance between adjacent threads; crest is the top, root the bottom and flanks the sides.', [89])
q('def', 'e', 'The included angle of a metric (ISO) V-thread is…',
  '60°', ['55°', '29°', '90°'],
  'Metric threads have a 60° included angle. 55° is the Whitworth angle and 29° is the Acme angle.', [90])
q('def', 'm', 'In the thread designation M20 × 1.5, what do 20 and 1.5 stand for?',
  'Major diameter 20 mm, pitch 1.5 mm', ['Pitch 20 mm, depth 1.5 mm', 'Length 20 mm, pitch 1.5 mm', 'Minor diameter 20 mm, angle 1.5°'],
  '"M" means metric; 20 mm is the major (nominal) diameter and 1.5 mm the pitch.', [91])
q('def', 'm', 'The formula used in our lab for the depth of a metric thread is…',
  'd = 0.6134 × p', ['d = 0.866 × p', 'd = 2 × p', 'd = p / 0.6134'],
  'The lab log sheets and notes use d = 0.6134 p for the thread depth (depth of cut).', [92])
q('def', 'm', 'The core (minor) diameter of a thread is given by…',
  'Dc = Dm − 2d', ['Dc = Dm − d', 'Dc = Dm + 2d', 'Dc = Dm − p'],
  'The core diameter equals the major diameter minus twice the thread depth: Dc = Dm − 2d.', [93])
q('app', 'e', 'Square threads are mainly used in…',
  'Screw jacks and power screws', ['Electrical fittings', 'Pipe joints', 'Spectacle frames'],
  'Square threads transmit power with low friction, so they are used in load-lifting devices like screw jacks.', [94])
q('app', 'm', 'A buttress thread is used where…',
  'Heavy load must be transmitted in one direction only', ['Light fastening is needed',
  'Equal load in both directions is needed', 'Fluid-tight pipe joints are needed'],
  'A buttress thread has one steep flank and one inclined flank; it carries heavy one-way loads, e.g. in vices.', [95])
q('param', 'm', 'In the ME-106 lathe lab, why was the spindle speed reduced to about 90 rpm for threading?',
  'The carriage moves one pitch per revolution, so it must be slow enough to stop at the groove', ['The lead screw cannot rotate above 90 rpm',
  'HSS tools melt above 90 rpm', 'Facing must be repeated at low speed'],
  'Turning was done at 315 rpm but threading at about 90 rpm. In threading the carriage moves fast (one pitch per revolution), so a low speed gives time to withdraw the tool at the end of each pass.', [96, 116, 120, 88])

# ============================ parameters / numericals ============================
q('def', 'm', 'Cutting speed in turning is calculated as…',
  'V = πDN / 1000 m/min', ['V = DN / 1000 m/min', 'V = πD / N m/min', 'V = 1000 / (πDN) m/min'],
  'Cutting speed V = πDN/1000 m/min, with D in mm and N in rpm (surface speed of the work).', [97])
n('num', 'm', 'In the ME-106 lathe job, a Ø38 mm bar is turned at 315 rpm. What is the cutting speed?',
  '≈ 37.6 m/min', ['≈ 12.0 m/min', '≈ 376 m/min', '≈ 3.76 m/min'],
  'V = πDN/1000 = π × 38 × 315 / 1000 ≈ 37.6 m/min. Forgetting π gives 12.0; mis-dividing gives 376 or 3.76.', [97, 116, 102])
n('num', 'h', 'The Ø34 thread of the ME-106 job is cut at 90 rpm. What is the cutting speed?',
  '≈ 9.6 m/min', ['≈ 3.1 m/min', '≈ 96 m/min', '≈ 30.6 m/min'],
  'V = π × 34 × 90 / 1000 ≈ 9.61 m/min. Leaving out π gives 3.06 m/min.', [97, 96, 108])
q('def', 'm', 'In turning, "feed" means…',
  'Distance the tool advances per revolution of the work', ['Thickness of metal removed in one pass',
  'Surface speed of the work', 'Number of passes needed'],
  'Feed is measured in mm/rev. Depth of cut is the radial thickness removed in a pass.', [98])
n('num', 'm', 'A bar is turned from Ø38 mm to Ø34 mm in one pass. What is the depth of cut?',
  '2 mm', ['4 mm', '1 mm', '36 mm'],
  'Depth of cut = (D − d)/2 = (38 − 34)/2 = 2 mm. 4 mm is the reduction in diameter, not the depth of cut.', [99])
q('meas', 'm', 'What was the least count of the cross-slide dial on the ME-106 lathe?',
  '0.02 mm', ['0.01 mm', '0.05 mm', '0.1 mm'],
  'The lathe log sheet notes the cross-slide least count as 0.02 mm.', [100])
n('num', 'h', 'Each division of the cross-slide dial moves the tool 0.02 mm radially. The dial is advanced by 25 divisions for one cut. By how much does the work DIAMETER reduce?',
  '1.0 mm', ['0.5 mm', '0.25 mm', '2.0 mm'],
  '25 × 0.02 = 0.5 mm radial depth of cut. Metal comes off all round, so the diameter reduces by 2 × 0.5 = 1.0 mm.', [100, 99, 30])
n('num', 'h', 'To reduce a diameter from 38 mm to 34 mm with a depth of cut of 0.5 mm per pass, how many passes are needed?',
  '4 passes', ['8 passes', '2 passes', '6 passes'],
  'Radial material = (38 − 34)/2 = 2 mm; 2 / 0.5 = 4 passes. Using the full diameter difference gives 8.', [99])

# ============================ taper numericals ============================
n('num', 'm', 'In the formula tan α = (D − d)/2L for taper turning, α is…',
  'The half taper angle (compound-rest setting)', ['The full included angle of the cone',
  'The rake angle of the tool', 'The helix angle of the thread'],
  'α is the half taper angle, which is the angle the compound rest is swivelled to.', [84], fig='lathe/taper')
n('num', 'm', 'For the ME-106 lathe job, the taper goes from Ø38 to Ø34 over 30 mm. What is tan α?',
  '1/15 (≈ 0.0667)', ['2/15 (≈ 0.133)', '1/30 (≈ 0.033)', '4/34 (≈ 0.118)'],
  'tan α = (38 − 34)/(2 × 30) = 4/60 = 1/15. Forgetting the 2 gives 2/15.', [84, 106, 111], fig='lathe/taper')
n('num', 'h', 'At what angle should the compound rest be set to turn the taper on the ME-106 job (Ø38 → Ø34 over 30 mm)?',
  '≈ 3.81°', ['≈ 7.59°', '≈ 7.63°', '≈ 1.91°'],
  'α = tan⁻¹[(38 − 34)/(2 × 30)] = tan⁻¹(0.0667) ≈ 3.81°. Forgetting the 2 gives 7.59°; the full cone angle is 2α ≈ 7.63°.', [84, 111])
n('num', 'h', 'A taper is turned from Ø50 mm to Ø40 mm over a length of 100 mm. What is the half taper angle?',
  '≈ 2.86°', ['≈ 5.71°', '≈ 5.73°', '≈ 1.43°'],
  'tan α = (50 − 40)/(2 × 100) = 0.05, so α ≈ 2.86°. Forgetting the 2 gives tan α = 0.1, i.e. 5.71°.', [84])
n('num', 'm', 'On the ME-106 taper (Ø38 → Ø34), how much material is removed from the RADIUS at the small end?',
  '2 mm', ['4 mm', '1 mm', '34 mm'],
  'Radial reduction = (38 − 34)/2 = 2 mm at the small end; the diameter reduces by 4 mm.', [106, 99])
n('num', 'h', 'For the ME-106 job taper (Ø38 → Ø34 over 30 mm), the taper ratio (D − d) : L is…',
  '1 : 7.5', ['1 : 15', '1 : 30', '1 : 3.75'],
  '(D − d) : L = 4 : 30 = 1 : 7.5. The 1 : 15 figure is tan α, i.e. half of this ratio.', [81, 106])

# ============================ thread numericals ============================
n('num', 'e', 'Using d = 0.6134 p, what is the thread depth for the 1.5 mm pitch thread on the ME-106 job?',
  '≈ 0.92 mm', ['≈ 1.84 mm', '≈ 1.30 mm', '≈ 0.61 mm'],
  'd = 0.6134 × 1.5 = 0.920 mm. 1.84 mm is 2d; 0.61 mm is the factor without the pitch.', [92, 112])
n('num', 'm', 'What is the core diameter of the Ø34 × 1.5 thread on the ME-106 lathe job?',
  '≈ 32.16 mm', ['≈ 33.08 mm', '≈ 31.00 mm', '≈ 35.84 mm'],
  'Dc = Dm − 2d = 34 − 2(0.92) = 32.16 mm. Subtracting d once gives 33.08 mm; adding gives 35.84 mm.', [93, 113, 108])
n('num', 'h', 'For an M20 × 2.5 thread, what is the core diameter (using d = 0.6134 p)?',
  '≈ 16.93 mm', ['≈ 18.47 mm', '≈ 15.00 mm', '≈ 23.07 mm'],
  'd = 0.6134 × 2.5 = 1.534 mm; Dc = 20 − 2(1.534) ≈ 16.93 mm.', [91, 92, 93])
n('num', 'm', 'What is the thread depth for a 2 mm pitch metric thread (d = 0.6134 p)?',
  '≈ 1.23 mm', ['≈ 2.45 mm', '≈ 0.61 mm', '≈ 3.26 mm'],
  'd = 0.6134 × 2 = 1.227 mm.', [92])
n('num', 'h', 'On a lathe, a thread of 1.5 mm pitch is being cut. How far does the carriage move in 20 revolutions of the work?',
  '30 mm', ['15 mm', '1.5 mm', '60 mm'],
  'During threading the tool advances one pitch per revolution: 20 × 1.5 = 30 mm.', [88])

# ============================ the ME-106 job (text) ============================
q('dims', 'e', 'What is the objective of the ME-106 lathe job?',
  'To perform facing, turning and threading on a cylindrical workpiece', ['To cut a spur gear on a disc',
  'To finish a flat surface by grinding', 'To reduce a block to 38 × 21 × 73 mm'],
  'The lathe log sheet objective: perform facing, turning and threading operations on a cylindrical workpiece using a lathe.', [101])
q('dims', 'e', 'According to the ME-106 lathe notes, what was the raw stock size?',
  'Mild-steel bar about 120 mm long, Ø38 mm', ['Aluminium disc 1½ in diameter', 'Mild-steel block 40 × 25 × 80 mm', 'Ø50 mm bar, 200 mm long'],
  'The lathe notes give the workpiece as 120 mm long and 38 mm in diameter.', [102])
n('dims', 'm', 'A 120 mm bar (as recorded in the lathe notes) is faced to the 115 mm overall length. How much length is removed by facing in total?',
  '5 mm', ['2.5 mm', '10 mm', '15 mm'],
  'Raw length 120 mm − finished 115 mm = 5 mm removed in total by facing (shared between the two ends).', [102, 103, 117])
q('dims', 'e', 'What is the overall length of the finished ME-106 lathe job?',
  '115 mm', ['120 mm', '110 mm', '125 mm'],
  'The job drawing shows an overall length of 115 mm (raw bar 120 mm).', [103])
q('dims', 'e', 'Units used on the ME-106 lathe job drawing are…',
  'Millimetres', ['Inches', 'Centimetres', 'Thou (mils)'],
  'The board drawing states "All dimensions are in mm". (The milling gear job uses inches.)', [104])

# ============================ procedure ============================
s('proc', 'm', 'What is the correct order of the first four steps of the ME-106 lathe job?',
  'Measure the bar → mark 115 mm and fix in 4-jaw chuck → centre and set speed → facing',
  ['Facing → measure the bar → fix in chuck → set speed',
   'Fix in chuck → facing → measure the bar → set speed',
   'Set speed → facing → fix in chuck → measure the bar'],
  'Log sheet steps 1–4: measure length and diameter; mark 115 mm and fix in the four-jaw chuck; check centre and set 315 rpm; perform facing.', [114, 115, 116, 117])
q('proc', 'e', 'What is the FIRST step of the ME-106 lathe procedure?',
  'Measure the length and diameter of the raw workpiece', ['Perform facing', 'Set the spindle to 90 rpm', 'Swivel the compound rest'],
  'Step 1 is to measure the length and diameter of the raw workpiece; then mark and fix it in the chuck.', [114])
q('proc', 'm', 'In the ME-106 lathe procedure, which step comes immediately AFTER fixing the job in the four-jaw chuck?',
  'Check the centring and set the spindle speed', ['Thread cutting', 'Taper turning', 'Remove the job and measure it'],
  'After chucking, the centre is checked (4-jaw work is centred manually) and the speed set to 315 rpm, then facing is done.', [115, 116])
q('proc', 'e', 'In the ME-106 lathe lab, the spindle speed set for facing and turning was about…',
  '315 rpm', ['90 rpm', '1500 rpm', '40 rpm'],
  'The log sheet and notes record 315 rpm for turning; threading was done at about 90 rpm.', [116])
q('proc', 'm', 'Why must the job be checked for centring after fixing it in the four-jaw chuck?',
  'Its jaws move independently, so the job is not self-centred', ['The tailstock moves automatically',
  'The lead screw needs aligning', 'To set the thread pitch'],
  'A 4-jaw chuck does not self-centre, so the job is trued manually before cutting.', [116, 49])
q('proc', 'e', 'In the ME-106 lathe job, facing is done to…',
  'Bring the job to the desired length', ['Reduce the diameter', 'Cut the thread', 'Make the taper'],
  'Step 4: perform facing on the workpiece to get the desired length (115 mm).', [117])
q('proc', 'm', 'In the 2025 ME-106 lathe log sheet, which step comes immediately after facing?',
  'Grooving and taper turning in the marked areas', ['Thread cutting', 'Parting-off', 'Knurling'],
  'The 2025 sheet: measure → mark & chuck → centre & set rotation → facing → groove and taper turn → threading.', [117, 118, 121])
q('proc', 'm', 'In the ME-106 lathe procedure, which of these is done first?',
  'Facing', ['Taper turning', 'Thread cutting', 'Grooving'],
  'Facing to length comes before grooving, taper turning and threading.', [117, 121])
q('proc', 'h', 'Which step comes immediately BEFORE thread cutting in the ME-106 lathe procedure?',
  'Grooving and taper turning', ['Facing', 'Measuring the raw bar', 'Fixing the job in the chuck'],
  'The log sheet sequence ends: … groove (5 mm) and taper turning with the compound rest → threading at reduced speed.', [119, 120, 121])
q('proc', 'm', 'How is the taper on the ME-106 job turned?',
  'By swivelling the compound rest to the half-taper angle', ['By setting over the tailstock',
  'With a form tool plunged in', 'By using the lead screw'],
  'The log sheet sets the tool post/compound rest at the calculated angle and turns the taper.', [119])
q('proc', 'm', 'Before cutting the 1.5 mm pitch thread on the ME-106 job, the operator…',
  'Sets the change gears from the chart and reduces speed', ['Swivels the compound rest to 3.81°',
  'Engages the feed rod', 'Removes the four-jaw chuck'],
  'The log sheet says to look at the table (chart) for 1.5 mm pitch, arrange the gears and set the speed to about 90 rpm.', [120])
s('proc', 'h', 'Which is the correct sequence of steps on the 2025 ME-106 lathe log sheet?',
  'Measure → mark 115 mm & fix in 4-jaw chuck → centre & set rotation → facing → groove & taper turning → threading',
  ['Facing → measure → threading → mark & chuck → groove & taper turning → centre',
   'Mark & chuck → threading → facing → measure → centre → groove & taper turning',
   'Measure → threading → facing → groove & taper turning → mark & chuck → centre'],
  'The 2025 log sheet lists these six steps in this order.', [121, 114, 115, 116, 117, 120])
q('proc', 'm', 'Besides facing, turning, taper turning, grooving and threading, which other operations appear on the ME-106 lathe job drawing?',
  'Centre drilling and chamfering', ['Knurling and boring', 'Reaming and parting-off', 'Slotting and gear cutting'],
  'The drawing shows centre holes at both ends and a 1 × 45° chamfer.', [122, 110, 105])

# ============================ precautions ============================
q('prec', 'e', 'Which dress precaution is given on the ME-106 lathe log sheet?',
  'Wear the workshop apron, tight-fitting clothes and shoes', ['Wear loose clothes for comfort',
  'Wear gloves while the chuck rotates', 'Wear sandals for easy movement'],
  'The log sheet precaution: always wear the manufacturing apron, tight-fitted clothes and shoes.', [123])
q('prec', 'e', 'According to the ME-106 lathe log sheet, chips should be…',
  'Removed in time, to avoid accidents', ['Left until the job is finished', 'Blown away with the mouth', 'Pulled off by hand while cutting'],
  'Remove chips timely to avoid accidents — and use a brush or chip hook, never bare hands.', [125])
q('prec', 'm', 'Why does the 2025 lathe log sheet ask students to stay at a proper distance from the machine?',
  'Hot chips may fly off the work', ['The tailstock moves on its own', 'The bed vibrates heavily', 'The lead screw is live electrically'],
  'Chips at high temperature can fly off, so stand at a proper distance.', [127])
q('prec', 'm', 'Which precaution about measuring is given on the 2025 lathe log sheet?',
  'Measure in proper lighting with inside and outside calipers', ['Measure only while the job rotates',
  'Measure with the chuck key left in place', 'Measure only after removing the job from the chuck'],
  'Take good measurements in proper lighting using inner and outer calipers.', [128])
q('prec', 'e', 'Before switching on the lathe, you must always…',
  'Remove the chuck key from the chuck', ['Engage the half-nut', 'Loosen the tool post', 'Remove the tailstock'],
  'A chuck key left in the chuck is thrown out violently when the spindle starts.', [129, 'SAF11'])
q('prec', 'e', 'When should the lathe job be measured with a caliper?',
  'Only after stopping the machine', ['While the chuck is rotating slowly', 'During thread cutting', 'While feeding the tool'],
  'Always stop the lathe before measuring the job or changing speeds/gears.', [130])
q('prec', 'm', 'Which of these is a precaution specific to the ME-106 lathe log sheet?',
  'Move the tailstock carefully', ['Demagnetise the chuck before removing the job',
  'Do not rotate the index crank backwards', 'Do not touch the plating solution'],
  'The lathe log sheet lists: apron/tight clothes/shoes, handle heavy machines with care, remove chips timely, move the tailstock carefully.', [126])
q('prec', 'e', 'Which precaution appears on both ME-106 lathe log sheets?',
  'Handle heavy machines and tools with care', ['Never leave the coolant off', 'Keep the dielectric flowing', 'Dress the wheel before use'],
  'Both lathe sheets say to handle heavy machines and tools with care.', [124])
q('prec', 'm', 'Which of these is UNSAFE practice on the lathe?',
  'Removing chips with bare hands while the lathe runs', ['Using a brush to clear chips after stopping',
  'Stopping the lathe before measuring', 'Removing the chuck key before starting'],
  'Chips are sharp and hot. Clear them with a brush or hook after stopping the machine.', [125, 130])

# ============================ assertion–reason / true-false ============================
ar('tools', 'h', 'A 3-jaw chuck cannot hold a rectangular block securely.',
   'The jaws of a 3-jaw chuck move together and centre round or hexagonal work.', 'a',
   'Both are true and R explains A: because the three jaws move together on a scroll, they suit only round or hexagonal shapes, so irregular work needs a 4-jaw chuck.', [48, 49])
ar('parts', 'h', 'The lead screw is disengaged during ordinary plain turning.',
   'The lead screw is used only for thread cutting.', 'a',
   'Both are true and R explains A: the lead screw is reserved for threading (to keep it accurate); the feed rod gives ordinary feeds.', [38, 37])
ar('tmat', 'h', 'HSS is used for the lathe tool in the ME-106 lab.',
   'HSS is softer than mild steel, so it does not chip.', 'c',
   'A is true but R is false: HSS is much harder than mild steel. The tool must be harder than the work, and HSS keeps its hardness at cutting temperatures.', [62, 63, 65])
ar('param', 'h', 'Threading on the ME-106 lathe was done at a lower spindle speed than turning.',
   'The lead screw is used only for thread cutting.', 'b',
   'Both are true, but R does not explain A. The low speed is used because the carriage advances one pitch per revolution, which is fast at turning speeds, so the operator could not withdraw the tool in time at the groove.', [96, 38])
tf('parts', 'm', 'The tailstock of a lathe carries the live centre.', False,
   'False. The headstock spindle carries the live centre, which rotates with the work. The tailstock carries the dead centre, which does not rotate.', [20, 24])
tf('param', 'm', 'In turning, the depth of cut equals half the reduction in diameter.', True,
   'True. Depth of cut = (D − d)/2, because metal is removed all round the work.', [99])
tf('dims', 'm', 'In the ME-106 (2025) job, the threaded portion is 25 mm long.', True,
   'True. The Ø34 × 1.5 thread runs for 25 mm, between the 5 mm groove and the Ø32 end section.', [108])

# ============================ diagrams ============================
B.labels('lathe/lathe-overview', 'p', diffs={'p': 'e'})
B.labels('lathe/lathe-overview', 'w', only={'w': ['D', 'H', 'J', 'M', 'N', 'L']})
B.labels('lathe/lathe-overview', 'f', only={'f': ['A', 'I', 'K', 'P']}, diffs={'f': 'm'})
B.labels('lathe/chucks', 'p', diffs={'p': 'm'}, cat='tools', extra_parts=['Collet chuck', 'Magnetic chuck'])
q('tools', 'm', 'In the figure, which chuck must have the work centred manually?', 'B', ['A'],
  'Panel B is the 4-jaw independent chuck. Each jaw is moved separately, so the job is centred by hand, as was done in our lab.',
  [49], fig='lathe/chucks')
B.labels('lathe/centres-dog', 'p', diffs={'p': 'm'}, cat='tools', extra_parts=['Face plate', 'Tool post'])
B.labels('lathe/operations', 'p', cat='ops', diffs={'p': 'e'})
B.labels('lathe/operations', 'w', cat='ops', only={'w': ['D', 'F', 'H', 'I']})
B.labels('lathe/thread-profiles', 'pf', cat='def', diffs={'p': 'm', 'f': 'm'}, extra_parts=['Acme thread', 'Knuckle thread'],
         extra_funcs=['Pipe joints that must be fluid-tight', 'Rounded threads for rough use, e.g. railway couplings'])
B.labels('lathe/thread-terms', 'p', cat='def', diffs={'p': 'm'})
B.labels('lathe/spt-tool', 'p', cat='tools', diffs={'p': 'm'})

J = 'lathe/job-2025-q'
q('dims', 'e', 'In the ME-106 lathe job drawing, what is the diameter of section P?', 'Ø38 mm', ['Ø34 mm', 'Ø32 mm', 'Ø37 mm'],
  'Section P is the Ø38 plain section, 35 mm long, with a 1 × 45° chamfer at the left end.', [105], fig=J, label='P')
q('dims', 'm', 'In the job drawing, what is the length of the taper Q?', '30 mm', ['35 mm', '25 mm', '20 mm'],
  'The taper runs from Ø38 to Ø34 over 30 mm.', [106], fig=J, label='Q')
q('dims', 'e', 'In the job drawing, what is the width of the groove R?', '5 mm', ['3 mm', '10 mm', '1.5 mm'],
  'A 5 mm groove separates the taper from the thread.', [107], fig=J, label='R')
q('dims', 'm', 'What is the thread specification of section S on the job drawing?', 'Ø34 × 1.5 mm pitch', ['Ø32 × 1.5 mm pitch', 'Ø34 × 2 mm pitch', 'Ø30 × 1.5 mm pitch'],
  'Section S is threaded Ø34 × 1.5 mm pitch, 25 mm long.', [108], fig=J, label='S')
q('dims', 'm', 'What are the diameter and length of the end section T on the job drawing?', 'Ø32 mm, 20 mm long', ['Ø34 mm, 25 mm long', 'Ø32 mm, 25 mm long', 'Ø30 mm, 20 mm long'],
  'Section T at the right end is Ø32 mm and 20 mm long.', [109], fig=J, label='T')
q('dims', 'e', 'What chamfer is specified at the left end of the ME-106 lathe job?', '1 × 45°', ['2 × 30°', '1 × 60°', '5 × 45°'],
  'The drawing calls for a 1 × 45° chamfer at the left end of the Ø38 section.', [105, 76], fig=J)
n('dims', 'h', 'In the ME-106 lathe job, how far from the LEFT end does the threaded portion start?', '70 mm', ['65 mm', '95 mm', '35 mm'],
  'Left end → Ø38 (35) → taper (30) → groove (5): 35 + 30 + 5 = 70 mm. The thread then runs to 95 mm.', [105, 106, 107, 108], fig=J)
q('dims', 'm', 'The job drawing shows small conical marks at both ends on the axis. They indicate…', 'Centre-drilled holes', ['Chamfers', 'Knurled ends', 'Grooves'],
  'Both ends of the ME-106 job are centre-drilled so the work can be supported on centres.', [110, 80], fig=J)
n('dims', 'h', 'In the ME-106 lathe job, what is the sum of the lengths of the taper and the thread?', '55 mm', ['50 mm', '60 mm', '45 mm'],
  'Taper 30 mm + thread 25 mm = 55 mm.', [106, 108], fig=J)

# ============================ more procedure (lab + standard practice) ============================
q('proc', 'm', 'In the ME-106 lathe job, at what stage is the length of 115 mm marked on the bar?',
  'Before fixing the bar in the four-jaw chuck', ['After thread cutting', 'After taper turning', 'After parting-off'],
  'Step 2 of the log sheet: mark 115 mm on the workpiece and fix it in the four-jaw chuck.', [115])
q('proc', 'm', 'Which lathe part is swivelled during the taper-turning step of the ME-106 job?',
  'Compound rest', ['Tailstock', 'Cross-slide', 'Headstock'],
  'For taper turning the compound rest (tool post slide) is set at the half-taper angle (≈3.81°) and fed by hand.', [119, 32])
q('proc', 'h', 'During the threading step of the ME-106 job, what drives the carriage along the work?',
  'Lead screw via the half-nut', ['Feed rod via the apron gears', 'Compound-slide handwheel', 'Tailstock handwheel'],
  'For threading the half-nut is engaged on the lead screw so the carriage moves exactly one pitch (1.5 mm) per revolution.', [120, 38, 39])
q('proc', 'm', 'In the ME-106 job, the 5 mm groove is cut…',
  'At the end of the thread, before taper turning and threading', ['After the thread is finished', 'Before facing', 'Before measuring the bar'],
  'The 2025 log sheet: after facing, "groove and taper turn in desired area", then thread to 1.5 mm pitch up to the groove.', [119, 121])
q('proc', 'm', 'Where is the tool tip set when a lathe tool is clamped in the tool post?',
  'Exactly at centre height (level with the lathe axis)', ['Well above the axis to increase clearance', 'Well below the axis to avoid rubbing', 'At any height'],
  'The tip must be on the lathe axis. Above or below centre changes the effective rake and clearance and leaves a pip when facing.', [133])
q('proc', 'h', 'After facing, a small pip is left at the centre of the job face. What is the likely cause?',
  'The tool tip is not at centre height', ['The spindle speed is too high', 'The chuck has 4 jaws', 'The feed rod is engaged'],
  'A pip at the centre is the classic sign that the tool is above or below centre height.', [133, 73])
q('proc', 'm', 'Why should the tool overhang from the tool post be kept short?',
  'To keep the tool rigid and avoid chatter', ['To increase the cutting speed', 'To make the taper steeper', 'To engage the lead screw'],
  'A long overhang makes the tool spring and vibrate (chatter); keep it short and clamp firmly.', [134])
q('proc', 'm', 'How is a job centred in a four-jaw chuck?',
  'Rotate by hand, check run-out with chalk/surface gauge and adjust opposite jaws', ['Tighten all jaws together with one key turn',
  'Bring up the tailstock and press hard', 'Run the lathe at high speed and watch the chips'],
  'With independent jaws, the job is trued by turning the chuck by hand and adjusting opposite jaws in pairs until run-out is removed.', [135, 116])
q('proc', 'm', 'Which order of cuts gives the best finish and size control on a lathe?',
  'Rough cuts first, then a light finishing cut', ['Finishing cut first, then rough cuts', 'Only one deep cut', 'Alternate deep and light cuts at random'],
  'Rough cuts remove most of the metal quickly; a final light cut with fine feed gives finish and accurate size.', [136])
q('proc', 'h', 'For a final finishing cut on the lathe you would use…',
  'Small depth of cut and fine feed', ['Large depth of cut and coarse feed', 'Large depth of cut and fine feed', 'Zero feed'],
  'Finishing cuts are light (small depth) with fine feed for good surface finish.', [136, 98])
s('proc', 'h', 'Which is the correct order for cutting a thread on a centre lathe?',
  'Set gear box for pitch → set tool square with centre gauge → engage half-nut → take light successive cuts',
  ['Engage half-nut → set gear box → set tool square → take one deep cut',
   'Take light cuts → set gear box → engage half-nut → set tool square',
   'Set tool square → take light cuts → set gear box → engage half-nut'],
  'Set the pitch first, square the 60° tool with a centre gauge, engage the half-nut and take several light cuts, withdrawing the tool after each pass.', [137])
q('tools', 'm', 'Which gauge is used to set a threading tool square to the work and check its 60° angle?',
  'Centre (thread) gauge', ['Feeler gauge', 'Telescopic gauge', 'Radius gauge'],
  'A centre gauge has 60° notches; it is used to grind the thread tool and set it square to the work.', [138])
q('proc', 'm', 'How is the finished thread on the lathe job checked?',
  'With a screw-pitch gauge or a mating nut', ['With a try square', 'With an outside caliper only', 'By its colour'],
  'Pitch is checked with a screw-pitch gauge; fit is checked by running a mating nut on.', [139])
q('proc', 'm', 'At the end of each threading pass, the operator should…',
  'Withdraw the tool, then return the carriage for the next cut', ['Leave the tool in the groove and reverse at full depth',
  'Increase the depth by 2 mm', 'Disengage the chuck'],
  'The tool is withdrawn with the cross-slide at the end of each pass, the carriage is returned, and the next light cut is taken.', [137])
q('proc', 'm', 'Before switching on the lathe after setting up a job, you should…',
  'Turn the chuck once by hand to check clearances', ['Switch on at the highest speed to test', 'Engage the half-nut', 'Remove the tool post'],
  'Rotating the chuck by hand confirms that the jaws and job clear the tool and carriage.', [140])
q('proc', 'h', 'In the ME-106 lathe procedure, which spindle speeds were used for (i) turning and (ii) threading?',
  '(i) 315 rpm, (ii) 90 rpm', ['(i) 90 rpm, (ii) 315 rpm', '(i) 315 rpm, (ii) 315 rpm', '(i) 1500 rpm, (ii) 90 rpm'],
  'Turning was done at about 315 rpm and threading at a reduced speed of about 90 rpm.', [116, 120])
q('proc', 'm', 'In the ME-106 job, which operation finishes the job last according to the procedure?',
  'Thread cutting', ['Facing', 'Step turning', 'Measuring the raw bar'],
  'The final step listed on the log sheets is to perform threading over the marked 25 mm length.', [120, 121])

# ============================ more precautions ============================
q('prec', 'e', 'What should you do if your hand gets close to the rotating chuck?',
  'Never touch it; never try to stop the chuck by hand', ['Slow it down with your palm', 'Grab the job to stop it', 'Use a cloth to brake it'],
  'Never touch the rotating job or chuck, and never stop it by hand. Switch off and let it come to rest.', [141])
q('prec', 'e', 'When is it safe to change the spindle speed or gears on the lathe?',
  'Only when the machine is stopped', ['While it is running slowly', 'During thread cutting', 'Whenever the job is small'],
  'Gears and speed levers are changed only after the spindle has stopped.', [142])
q('prec', 'm', 'Before drilling with a drill held in the tailstock, you must…',
  'Lock the tailstock to the bed', ['Engage the lead screw', 'Remove the tool post', 'Swivel the compound rest'],
  'An unlocked tailstock is pushed back by the drilling thrust; lock the tailstock (and quill) first.', [143])
q('prec', 'e', 'Which eye protection should be worn on the lathe?',
  'Safety goggles', ['Laser goggles', 'Welding helmet', 'No protection is needed'],
  'Flying chips can injure the eyes, so wear safety goggles.', [145])
q('prec', 'm', 'Which of these is a safe practice on the lathe?',
  'Keeping the bed ways clear of tools while cutting', ['Leaving the chuck key in the chuck', 'Leaning on the carriage', 'Wearing a loose tie'],
  'Do not keep tools on the bed or carriage, do not lean on the machine, and remove the chuck key.', [146, 129])
q('prec', 'm', 'Why must the tool and job be clamped firmly before starting the lathe?',
  'A loose tool or job can be thrown out or dig in', ['To increase the cutting speed', 'To reduce the thread pitch', 'To cool the tool'],
  'Firm clamping prevents the job or tool from loosening, digging in or flying out.', [144])
q('prec', 'm', 'Which of these is NOT a lathe-shop precaution?',
  'Stop the chuck by hand to save time', ['Remove the chuck key before starting', 'Stop the machine before measuring', 'Wear tight-fitting clothes'],
  'Stopping the chuck by hand is dangerous. The others are standard precautions on the lathe log sheets and in workshop practice.', [141, 129, 130, 123])
q('prec', 'h', 'A student leaves the chuck key in the chuck and switches on. What is the danger?',
  'The key is thrown out with great force', ['The thread pitch changes', 'The lead screw disengages', 'The tailstock locks'],
  'The spinning chuck flings the key out, which can seriously injure people nearby. Always remove the key first.', [129])
q('prec', 'm', 'Tight-fitting clothes are required in the lathe shop because…',
  'Loose clothing can be caught by the rotating chuck or work', ['They keep the coolant off', 'They prevent electric shock', 'They help in marking the job'],
  'Loose sleeves, ties or clothes can be pulled into rotating parts.', [123])
q('prec', 'e', 'The correct way to clear long chips from a lathe is to…',
  'Stop the machine and use a brush or chip hook', ['Pull them away by hand while cutting', 'Blow them away with your mouth', 'Ignore them until the job ends'],
  'Chips are sharp and hot. Remove them in time with a brush or hook, never with bare hands.', [125])
tf('prec', 'e', 'It is acceptable to measure the lathe job with a caliper while it is rotating slowly.', False,
   'False. Always stop the machine before measuring.', [130])

q('prec', 'm', 'Why does the lathe log sheet ask you to move the tailstock carefully?',
  'It is heavy and can crash into the carriage or fall off the bed end', ['It carries the live centre', 'It controls spindle speed', 'It holds the lead screw'],
  'The tailstock is a heavy casting; sliding it roughly can damage the ways, hit the carriage or run off the end of the bed.', [126, 23])
q('prec', 'm', 'Why should measurements on the lathe be taken in proper lighting?',
  'So caliper settings are read accurately', ['So the chips cool faster', 'So the motor runs cooler', 'So the thread pitch changes'],
  'Calipers have no scale; a correct reading against the rule needs good light, as stated on the 2025 log sheet.', [128, 59])
q('prec', 'h', 'A long, continuous chip is winding around the rotating job. What should you do?',
  'Stop the lathe, then remove the chip with a hook or brush', ['Pull it off by hand quickly', 'Cut it with pliers while running', 'Increase the speed to break it'],
  'Never handle chips on a running machine. Stop it, then use a chip hook or brush.', [125, 141])
q('prec', 'm', 'Which item of PPE is NOT normally required for the ME-106 lathe practice?',
  'Laser safety goggles', ['Workshop apron', 'Closed shoes', 'Safety goggles'],
  'Lathe work needs an apron, tight clothes, shoes and eye protection; laser goggles are for the fiber laser.', [123, 145])
q('prec', 'h', 'Which precaution protects the operator from HOT chips specifically?',
  'Stand at a proper distance and wear goggles', ['Move the tailstock carefully', 'Set the tool at centre height', 'Use the lead screw only for threading'],
  'Hot chips can fly, so keep a proper distance (2025 log sheet) and protect your eyes.', [127, 145])
q('prec', 'm', 'Before starting the lathe, which check prevents the chuck jaws from hitting the carriage?',
  'Rotate the chuck once by hand', ['Engage the half-nut', 'Set the compound to 45°', 'Lock the tailstock quill'],
  'Hand-rotating the chuck shows whether the jaws or job foul the tool or carriage.', [140])
q('proc', 'e', 'In the ME-106 lathe job, which marking tools are used in the marking step?',
  'Chalk, marker, marking stand and plate', ['Scriber and dot punch', 'Divider and centre punch', 'Surface gauge and V-block'],
  'The job is marked using chalk/marker with the marking stand and marking plate, then measured with scale and outside caliper.', [55, 115])
q('proc', 'm', 'Which measuring tools are used in step 1 of the ME-106 lathe procedure?',
  'Steel scale and outside caliper', ['Micrometer and dial gauge', 'Vernier height gauge', 'Bevel protractor'],
  'The raw length and diameter are measured with the steel scale and outside caliper.', [56, 114])
q('proc', 'h', 'Why is threading done LAST in the ME-106 lathe job?',
  'The groove and the other diameters must be finished first so the thread can run up to the groove', ['Threading must be done before facing',
  'The lead screw only works after facing', 'Threading removes the chamfer'],
  'The thread is cut last, up to the 5 mm groove that was cut earlier; turning after threading would damage the thread.', [118, 120, 121])
q('proc', 'm', 'What is engaged for plain turning but NOT used for threading?',
  'Feed rod (power feed)', ['Lead screw', 'Half-nut', 'Change gears for pitch'],
  'Ordinary turning feed comes from the feed rod; threading uses the lead screw and half-nut.', [37, 38])

B.save()
