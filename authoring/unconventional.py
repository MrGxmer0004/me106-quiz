"""Unconventional machining (wire EDM + fiber laser) question bank. Correct option first; balanced lengths."""
from qlib import Bank

B = Bank('unconventional')
q, n, s, tf, ar = B.q, B.n, B.s, B.tf, B.ar

# ============================ general ============================
q('def', 'e', 'Unconventional (non-traditional) machining removes material mainly by…',
  'Energy forms such as sparks, light, chemicals or jets', ['A sharp tool that is harder than the work', 'Pressing the work into a shaped die', 'Melting the whole job and recasting it'],
  'Non-traditional processes use electrical, thermal, chemical, electrochemical or jet energy instead of a sharp tool in contact.', [1])
q('adv', 'm', 'Which is a main reason for using unconventional machining?',
  'Very hard materials and complex shapes with no cutting force', ['It is always cheaper than turning', 'It needs no electricity or energy at all', 'It works only on soft plastics'],
  'They suit very hard/brittle materials, complex shapes, tiny holes and delicate parts where tool forces must be avoided.', [2])
q('theory', 'm', 'Unconventional machining processes are classified on the basis of…',
  'The type of energy used to remove material', ['The colour of the workpiece', 'The size of the machine', 'The number of operators'],
  'Mechanical, thermal (electrothermal), electrochemical and chemical.', [3])
q('theory', 'm', 'EDM and laser-beam machining belong to which energy class?',
  'Thermal (electrothermal)', ['Mechanical', 'Electrochemical', 'Chemical'],
  'EDM, WEDM, LBM, EBM and PAM remove material by local melting and vaporisation.', [3, 4])
q('theory', 'm', 'Ultrasonic machining (USM) and abrasive-jet machining (AJM) are classed as…',
  'Mechanical processes', ['Thermal processes', 'Electrochemical processes', 'Chemical processes'],
  'USM, AJM and water-jet machining are mechanical processes.', [3])
q('theory', 'm', 'How is material removed in thermal processes like EDM and LBM?',
  'By local melting and vaporisation', ['By anodic dissolution', 'By shearing with a sharp edge', 'By chemical etching with masks'],
  'Thermal energy is applied to a small zone, which melts and vaporises.', [4])
q('theory', 'h', 'Electrochemical machining (ECM) is described as the reverse of…',
  'Electroplating', ['Welding', 'Grinding', 'Casting'],
  'ECM removes metal by anodic dissolution, the reverse of plating.', [5])
q('theory', 'm', 'In most unconventional processes, the tool…',
  'Need not be harder than the workpiece', ['Must be twice as hard as the work', 'Must be made of diamond', 'Must touch the work firmly'],
  'For example, a soft brass wire cuts hardened steel in wire EDM.', [6])

# ============================ WEDM principle ============================
q('theory', 'e', 'In wire EDM, material is removed by…',
  'Repeated electric sparks that melt and vaporise metal', ['A rotating abrasive wheel grinding it', 'A wire sawing it by friction', 'Chemicals dissolving it'],
  'Pulsed sparks between the wire and the work cause thermal erosion.', [7])
q('theory', 'e', 'During cutting in wire EDM, the wire electrode and the workpiece…',
  'Never touch each other', ['Are pressed firmly together', 'Are welded together first', 'Touch only at the start'],
  'There is no mechanical contact and practically no cutting force.', [8])
q('theory', 'm', 'What happens if the wire touches the workpiece in wire EDM?',
  'A short circuit occurs and no spark forms', ['The cutting rate doubles', 'The kerf becomes narrower', 'The wire becomes harder'],
  'Contact short-circuits the gap, so a small spark gap must be maintained.', [9])
q('parts', 'm', 'In wire EDM, the spark gap is kept constant by…',
  'A servo control system', ['A spring on the table', 'The operator by hand', 'A magnetic chuck'],
  'A servo maintains a gap of roughly 0.025–0.075 mm.', [10])
q('param', 'm', 'If the spark gap in EDM is too large…',
  'No spark forms', ['The wire shorts with the work', 'The kerf becomes zero', 'The wire melts at once'],
  'Too large: no spark. Too small: short circuit.', [11])
q('param', 'm', 'In wire EDM, material is removed during…',
  'Pulse-on time (Ton)', ['Pulse-off time (Toff)', 'Flushing only', 'Wire threading'],
  'The log sheet: during Ton discharge occurs and material is removed.', [12])
q('param', 'h', 'What is the purpose of the pulse-off time (Toff) in EDM?',
  'Lets the dielectric de-ionise and flushes debris away', ['Increases the spark energy', 'Moves the wire spool faster', 'Heats the workpiece'],
  'During Toff the gap recovers its insulation and debris is flushed; too short a Toff causes arcing.', [13])
q('wmat', 'e', 'Which condition must a workpiece satisfy to be cut by wire EDM?',
  'It must be electrically conductive', ['It must be soft', 'It must be non-metallic', 'It must be transparent'],
  'EDM needs a conductive workpiece; hardness does not matter.', [14])
q('wmat', 'm', 'Which material CANNOT be cut by wire EDM?',
  'Glass (non-conductor)', ['Hardened tool steel', 'Tungsten carbide', 'Titanium alloy'],
  'Non-conductors like glass, plastics and most ceramics cannot be EDMed; hard conductive metals can.', [14])
q('ops', 'm', 'In wire EDM, the wire follows the required profile under…',
  'CNC control (part program)', ['Manual hand feed only', 'A copying template', 'Gravity'],
  'The log sheet step: enter the required profile through part programming.', [15])
q('ops', 'h', 'To cut an internal profile (closed cavity) by wire EDM, you must first…',
  'Drill a start hole to thread the wire through', ['Grind the profile roughly', 'Heat the job red hot', 'Plate the job with copper'],
  'The wire must pass through the job, so a start hole is needed for internal shapes.', [16])
q('ops', 'h', 'Wire EDM can cut tapered sides by…',
  'Tilting the upper and lower wire guides', ['Bending the wire into a curve', 'Rotating the table at high speed', 'Changing the dielectric'],
  'WEDM cuts 2-D through-profiles; offsetting the guides gives a taper.', [17])

# ============================ WEDM elements ============================
q('param', 'e', 'The dielectric commonly used in wire EDM is…',
  'Deionised water', ['Kerosene', 'Compressed air', 'Machine oil'],
  'Wire EDM uses deionised water; die-sinking EDM usually uses a hydrocarbon oil such as kerosene.', [18, 19])
q('param', 'm', 'Die-sinking EDM usually uses which dielectric?',
  'A hydrocarbon oil such as kerosene', ['Deionised water', 'Compressed nitrogen', 'Salt water'],
  'Die-sinking EDM: oil (kerosene); wire EDM: deionised water.', [19])
q('def', 'm', 'Which of these is NOT a function of the dielectric in EDM?',
  'Supplying metal ions to plate the work', ['Insulating the gap until breakdown', 'Cooling the work and wire', 'Flushing away debris'],
  'The dielectric insulates, concentrates the spark, cools and flushes. Supplying metal ions is what a plating bath does.', [20])
q('param', 'm', 'Why is the water in wire EDM continuously deionised?',
  'Tap water is too conductive for proper sparking', ['To make it heavier', 'To add metal ions', 'To colour the water'],
  'Ions make water conductive; the dielectric must insulate until breakdown, so it is filtered and deionised.', [21])
q('tmat', 'e', 'The wire electrode in wire EDM is usually made of…',
  'Brass', ['Mild steel', 'Aluminium', 'Plastic'],
  'Brass (often zinc-coated) is common; copper, molybdenum or tungsten are also used.', [22])
q('param', 'm', 'Typical wire diameter in wire EDM is about…',
  '0.05–0.3 mm', ['1–3 mm', '5–10 mm', '0.001–0.005 mm'],
  'Very thin wires, about 0.05–0.3 mm (commonly 0.25 mm), are used.', [23])
q('param', 'm', 'In wire EDM, the wire is…',
  'Fed continuously and used only once', ['Reused many times after cleaning', 'Kept stationary', 'Replaced only once a year'],
  'The wire erodes, so fresh wire is fed from a spool to a take-up and not reused.', [24])
q('parts', 'm', 'The wire in wire EDM is held accurately above and below the job by…',
  'Upper and lower wire guides', ['A chuck and a tailstock', 'A vice and a clamp', 'Two centres'],
  'Upper and lower guides position the wire; they can be offset for taper cuts.', [25])
q('def', 'e', 'The kerf width in wire EDM equals…',
  'Wire diameter + 2 × spark gap', ['Wire diameter − spark gap', 'Spark gap only', '2 × wire diameter'],
  'The wire erodes a slot as wide as itself plus a spark gap on each side.', [26])
n('num', 'm', 'A 0.25 mm brass wire cuts with a spark gap of 0.03 mm. What is the kerf width?',
  '0.31 mm', ['0.28 mm', '0.25 mm', '0.56 mm'],
  'Kerf = d + 2g = 0.25 + 2(0.03) = 0.31 mm. Forgetting the factor 2 gives 0.28 mm.', [26])
n('num', 'h', 'A wire EDM cut produces a kerf of 0.36 mm with a 0.30 mm wire. What is the spark gap?',
  '0.03 mm', ['0.06 mm', '0.33 mm', '0.12 mm'],
  'g = (kerf − d)/2 = (0.36 − 0.30)/2 = 0.03 mm.', [26])
q('def', 'h', 'In wire EDM programming, the wire path is offset from the drawn profile by…',
  'Wire radius + spark gap', ['Wire diameter + 2 × spark gap', 'Spark gap only', 'Zero; no offset is needed'],
  'The wire centre must stay (radius + gap) away from the finished edge.', [27])
n('num', 'h', 'For a 0.25 mm wire and a 0.025 mm spark gap, what wire offset is programmed?',
  '0.15 mm', ['0.30 mm', '0.275 mm', '0.125 mm'],
  'Offset = r + g = 0.125 + 0.025 = 0.15 mm.', [27])
q('param', 'm', 'Which of these is NOT a wire EDM machining parameter?',
  'Spindle speed in rpm', ['Pulse-on time (Ton)', 'Peak current', 'Wire tension'],
  'WEDM parameters: Ton, Toff, peak current, voltage, wire tension, wire feed and flushing. There is no rotating spindle.', [28])
q('param', 'm', 'In EDM, increasing the peak current and pulse-on time generally…',
  'Increases cutting rate but roughens the surface', ['Decreases cutting rate and improves finish', 'Has no effect on the cut', 'Stops the sparks completely'],
  'Higher spark energy removes more metal per spark, giving bigger craters and a rougher surface.', [29])
q('param', 'm', 'If wire tension in wire EDM is too LOW…',
  'The wire vibrates and accuracy suffers', ['The wire always breaks at once', 'The kerf becomes zero', 'The dielectric boils'],
  'Low tension causes vibration and inaccuracy; too high causes breakage.', [30])
q('param', 'm', 'A main cause of wire breakage and poor finish in wire EDM is…',
  'Inadequate flushing of the gap', ['Using deionised water', 'Using a brass wire', 'Cutting conductive steel'],
  'Poor flushing leaves debris, causing arcing and wire breakage.', [31])
q('def', 'h', 'In EDM, the thin re-solidified layer left on the machined surface is called the…',
  'Recast layer', ['Clad layer', 'Plated layer', 'Pickled layer'],
  'Each spark leaves a crater; melted metal re-solidifies as a recast layer over a heat-affected zone.', [32])

# ============================ WEDM pros / cons ============================
q('adv', 'm', 'Which is an advantage of wire EDM?',
  'No cutting force, so thin delicate parts can be cut', ['It cuts any material, including glass', 'It is the fastest metal-removal process', 'It needs no dielectric fluid'],
  'Advantages: complex 2-D profiles, high accuracy and finish, no burrs, no cutting force, hard materials.', [33])
q('adv', 'm', 'Which is a limitation of wire EDM?',
  'Only electrically conductive materials can be cut', ['It cannot cut hardened steel', 'It leaves heavy burrs', 'It needs a very hard tool'],
  'Limitations: conductive materials only, slow removal, recast layer/HAZ, wire cost.', [34])
q('app', 'm', 'Wire EDM is widely used for making…',
  'Press-tool dies, punches and extrusion dies', ['Wooden furniture', 'Cast-iron engine blocks', 'Glass bottles'],
  'Tool and die making is the main application; also gears and aerospace/medical parts.', [35])
q('theory', 'm', 'How does die-sinking EDM differ from wire EDM?',
  'A shaped electrode sinks a 3-D cavity instead of a wire cutting a profile', ['It uses a laser beam instead of sparks', 'It works without any dielectric', 'It needs no electric power'],
  'Die-sinking: shaped copper/graphite electrode, usually in oil. Wire EDM: moving wire, 2-D through-profiles, deionised water.', [36])

# ============================ laser principle ============================
q('theory', 'e', 'In laser cutting, material is removed by…',
  'A focused beam melting or vaporising the metal', ['A spinning cutter shearing the metal', 'Sparks between a wire and the metal', 'Chemicals dissolving the metal'],
  'The beam melts/vaporises a narrow zone; a coaxial assist-gas jet blows the melt out of the kerf.', [37])
q('def', 'e', 'LASER stands for…',
  'Light Amplification by Stimulated Emission of Radiation', ['Light And Sound Energy Release', 'Linear Amplified Spark Electric Radiation', 'Low-Angle Surface Erosion by Radiation'],
  'LASER = Light Amplification by Stimulated Emission of Radiation.', [38])
q('theory', 'm', 'The gain medium of a fiber laser is…',
  'An optical fiber doped with ytterbium', ['A tube of CO₂ gas', 'A ruby crystal', 'Deionised water'],
  'Fiber lasers are solid-state lasers with a Yb-doped fiber.', [39])
q('param', 'm', 'The wavelength of a fiber laser is about…',
  '1.06 µm (1064 nm)', ['10.6 µm', '0.5 nm', '1 mm'],
  'Fiber ≈ 1.06 µm; CO₂ ≈ 10.6 µm.', [40])
q('theory', 'm', 'Why are fiber lasers preferred over CO₂ lasers for cutting metal sheet?',
  'Metals absorb the shorter 1.06 µm wavelength much better', ['Fiber lasers have a longer wavelength', 'Fiber lasers need no assist gas', 'CO₂ lasers cannot be focused'],
  'Metals absorb ~1 µm light far better than 10.6 µm light.', [41])
q('app', 'm', 'CO₂ lasers are widely used for cutting…',
  'Non-metals such as wood, acrylic and plastics', ['Only hardened tool steel', 'Only copper and brass', 'Only glass fibres'],
  'CO₂ lasers (10.6 µm) suit non-metals.', [42])
q('parts', 'm', 'In a fiber laser cutting machine, the beam reaches the cutting head through…',
  'A flexible optical fiber', ['A rigid steel pipe of mirrors only', 'A copper wire', 'A water jet'],
  'The beam is delivered by fiber; the path is CNC-programmed.', [43])
q('adv', 'm', 'Since laser cutting is non-contact, it has…',
  'No tool wear and no cutting force', ['Very high tool wear', 'A large clamping force on the job', 'A need for a sharp cutter'],
  'Non-contact processing: no tool wear, no mechanical force.', [44])

# ============================ laser gas / params ============================
q('param', 'm', 'Which assist gas is normally used for laser cutting mild steel?',
  'Oxygen', ['Nitrogen', 'Argon', 'Helium'],
  'O₂ reacts exothermically with iron, adding heat for faster/thicker cuts (with an oxide layer on the edge).', [45])
q('param', 'm', 'Which assist gas is used for clean, oxide-free cuts in stainless steel and aluminium?',
  'Nitrogen', ['Oxygen', 'Carbon dioxide', 'Hydrogen'],
  'N₂ is inert; the laser supplies all the energy and the edges stay bright.', [46])
q('theory', 'h', 'Why does oxygen assist gas allow faster cutting of mild steel?',
  'Its exothermic reaction with iron adds extra heat', ['It cools the kerf faster', 'It is heavier than nitrogen', 'It increases the laser wavelength'],
  'The iron–oxygen reaction releases heat, supplementing the laser energy.', [45])
q('adv', 'h', 'What is the drawback of cutting mild steel with oxygen assist gas?',
  'An oxide layer forms on the cut edge', ['The kerf becomes very wide', 'The cut cannot go through', 'The lens melts at once'],
  'Oxygen leaves an oxidised edge; nitrogen gives oxide-free edges.', [45, 46])
q('param', 'm', 'A cheap assist-gas option for thin sheets is…',
  'Compressed air', ['Pure argon', 'Liquid helium', 'Steam'],
  'Compressed air is a low-cost option for thin material.', [47])
q('def', 'm', 'Besides removing molten metal, the assist gas also…',
  'Protects the lens from spatter and cools the cut', ['Supplies the laser light', 'Polishes the sheet', 'Charges the workpiece'],
  'The coaxial gas jet keeps spatter off the optics and cools the cut zone.', [48])
q('param', 'm', 'Which of these is NOT a laser-cutting parameter?',
  'Number of cutter teeth', ['Laser power', 'Cutting speed', 'Focal position'],
  'Parameters: power, speed, focal position, gas type and pressure, nozzle diameter, stand-off.', [49])
q('parts', 'm', 'In the laser cutting head, the beam is focused to a small spot by the…',
  'Focusing lens', ['Collimating lens', 'Assist-gas inlet', 'Fiber connector'],
  'The collimator makes the beam parallel; the focusing lens concentrates it to a spot.', [50])
q('def', 'm', 'Stand-off distance in laser cutting is the gap between…',
  'The nozzle tip and the workpiece surface', ['The lens and the fiber', 'Two passes of the beam', 'The table and the floor'],
  'It affects gas flow and focus position.', [51])
q('def', 'm', 'Compared with other thermal cutting, laser cutting gives…',
  'A narrow kerf and a small heat-affected zone', ['A wide kerf and a large HAZ', 'No kerf at all', 'A thick recast layer always'],
  'Kerf is a few tenths of a mm and the HAZ is small.', [52])
q('def', 'm', 'In laser cutting, "dross" means…',
  'Re-solidified metal stuck to the bottom edge', ['The beam wavelength', 'The assist-gas pressure', 'The fiber coating'],
  'Dross is melt that did not get blown away; striations are lines on the cut face.', [53])
q('param', 'h', 'If the laser cutting speed is too HIGH, the likely result is…',
  'An incomplete cut and dross on the underside', ['A very wide kerf and large HAZ', 'Perfect cut with no change', 'Burning of the nozzle'],
  'Too fast: the beam cannot cut through, leaving dross. Too slow: wide kerf and big HAZ.', [54])

# ============================ laser pros / cons / safety ============================
q('adv', 'm', 'Which is an advantage of fiber laser cutting?',
  'High speed and precision with intricate shapes', ['It needs no electricity', 'It cuts any thickness easily', 'Its equipment is very cheap'],
  'Advantages: speed, precision, narrow kerf, small HAZ, no tool wear, intricate shapes.', [55])
q('adv', 'm', 'Which is a limitation of fiber laser cutting?',
  'High equipment cost and a thickness limit', ['It always needs a sharp cutter', 'It cannot cut mild steel', 'It works only on wood'],
  'Limitations: high cost, thickness limits, reflective metals can be difficult, fumes.', [56])
q('wmat', 'h', 'Which metals are often difficult to laser cut because they reflect the beam?',
  'Copper and brass', ['Mild steel and stainless steel', 'Cast iron and wrought iron', 'Titanium and nickel'],
  'Highly reflective metals like copper and brass reflect much of the beam.', [56])
q('prec', 'e', 'Which eye protection is required near a fiber laser cutter?',
  'Laser safety goggles rated for its wavelength', ['Ordinary sunglasses', 'Welding goggles of any shade', 'No protection is needed'],
  'Wear laser goggles of the correct wavelength rating and never look into the beam.', [57])
q('prec', 'm', 'Which is a laser-cutting safety rule?',
  'Keep the enclosure closed and use fume extraction', ['Look into the beam to check focus', 'Put hands on the bed to steady the sheet', 'Switch off the extraction to save power'],
  'Keep the enclosure closed, extract fumes, keep hands off the bed, and watch for fire.', [57])

# ============================ lab jobs ============================
q('dims', 'e', 'What are the objectives of the ME-106 unconventional machining practice?',
  'To study wire EDM and the fiber laser cutting machine', ['To study CNC milling and 3D printing', 'To study ECM and USM', 'To study plasma and water-jet cutting'],
  'Objectives: 1 study wire electrical discharge machining; 2 study the fiber laser cutting machine.', [58])
q('dims', 'e', 'What job is cut on the wire EDM in the ME-106 lab?',
  'A square 10 mm × 10 mm, 5 mm thick', ['A ring cut from sheet', 'A 22-tooth spur gear', 'A stepped shaft'],
  'The log sheet drawing: EDM square 10 × 10 mm with 5 mm thickness.', [59])
q('dims', 'e', 'What job is cut on the fiber laser in the ME-106 lab?',
  'A ring (annulus) from metal sheet', ['A 10 × 10 × 5 mm square', 'A hexagonal nut', 'A spur gear'],
  'The log sheet drawing shows a laser-cut ring.', [60])
n('num', 'm', 'What is the volume of the 10 × 10 × 5 mm wire-EDM square?',
  '500 mm³', ['100 mm³', '50 mm³', '1000 mm³'],
  '10 × 10 × 5 = 500 mm³.', [59])
n('num', 'm', 'The 10 × 10 mm EDM square is cut out of a plate along its full perimeter. What length of cut does the wire travel?',
  '40 mm', ['20 mm', '100 mm', '50 mm'],
  'Perimeter = 4 × 10 = 40 mm.', [59])
q('tools', 'm', 'Which of these is listed in the ME-106 wire EDM tool list?',
  'Clamping wire', ['Grinding wheel', 'Index plate', 'Emery paper'],
  'Tools: wire-cut EDM machine, clamping tool, clamping wire, power supply, dielectric fluid supply, part programming, wire electrode.', [61])
q('tools', 'm', 'Which item is NOT in the ME-106 wire EDM tool list?',
  'Assist-gas cylinder', ['Dielectric fluid supply', 'Part programming', 'Wire electrode'],
  'Assist gas belongs to laser cutting.', [61])

# ============================ WEDM procedure ============================
q('proc', 'e', 'What is the FIRST step of the ME-106 wire EDM procedure?',
  'Clamp the workpiece properly on the machine', ['Apply pulsed voltage to the wire', 'Remove and inspect the job', 'Enter the profile in the program'],
  'Step 1: clamp the workpiece properly on the EDM machine.', [62])
q('proc', 'm', 'Which step comes immediately after clamping the job in the ME-106 wire EDM procedure?',
  'Fix and tension the wire electrode', ['Start the dielectric pump', 'Inspect the finished job', 'Apply pulsed voltage'],
  'Step 2: fix and tension the wire electrode.', [63])
q('proc', 'm', 'In the ME-106 wire EDM procedure, which step comes before entering the profile through part programming?',
  'Supplying the dielectric fluid to the machining zone', ['Removing and inspecting the job', 'Applying pulsed voltage', 'The wire completing the cut'],
  'Steps 3–5: set parameters → supply dielectric → enter profile by part programming.', [64, 65, 66])
q('proc', 'm', 'In the ME-106 wire EDM procedure, the machining parameters are set…',
  'After fixing the wire and before supplying dielectric', ['After the job is removed', 'Only after the cut is complete', 'Before clamping the job'],
  'Step 3: set the required machining parameters.', [64])
q('proc', 'm', 'What must be maintained between the wire and workpiece during the cut (step 6)?',
  'A small spark gap', ['Firm contact pressure', 'A 5 mm air gap', 'A layer of grease'],
  'Step 6: maintain a small spark gap between wire and workpiece.', [67])
q('proc', 'm', 'In step 7 of the ME-106 wire EDM procedure, what is applied between the wire and the job?',
  'Pulsed electrical voltage', ['Steady AC mains voltage', 'Compressed air', 'A grinding force'],
  'Step 7: apply pulsed electrical voltage between the wire and workpiece.', [68])
q('proc', 'm', 'According to the ME-106 log sheet, how is material removed in wire EDM (step 8)?',
  'By the heat generated by the sparks', ['By the wire rubbing the job', 'By chemical attack of the water', 'By the clamping pressure'],
  'Step 8: material is removed due to the heat generated by the sparks.', [69])
q('proc', 'e', 'What is the LAST step of the ME-106 wire EDM procedure?',
  'Remove and inspect the machined job', ['Fix and tension the wire', 'Clamp the job', 'Set the parameters'],
  'Step 11 (the last): remove and inspect the machined job.', [71])
q('proc', 'm', 'In the ME-106 wire EDM procedure, how is the profile completed (step 10)?',
  'The wire moves along the programmed profile', ['The operator saws by hand', 'The table rotates the job', 'The job is turned on a lathe'],
  'Step 10: the wire moves according to the programmed profile and completes the cut.', [70])
s('proc', 'h', 'What is the correct order of the ME-106 wire EDM procedure?',
  'Clamp job → fix & tension wire → set parameters → supply dielectric → enter profile → keep spark gap → apply pulses → cut → remove & inspect',
  ['Fix & tension wire → clamp job → apply pulses → set parameters → enter profile → supply dielectric → keep spark gap → cut → remove & inspect',
   'Enter profile → apply pulses → clamp job → supply dielectric → fix & tension wire → set parameters → keep spark gap → cut → remove & inspect',
   'Supply dielectric → set parameters → clamp job → cut → fix & tension wire → enter profile → keep spark gap → apply pulses → remove & inspect'],
  'From the Unconventional log sheet.', [62, 63, 64, 65, 66, 67, 68, 70, 71])

# ============================ laser procedure ============================
q('proc', 'e', 'What is the FIRST step of the ME-106 fiber laser procedure?',
  'Clamp the metal sheet properly on the bed', ['Start the laser beam', 'Inspect the cut piece', 'Do a dry run'],
  'Step 1: clamp the metal sheet properly on the machine bed.', [72])
q('proc', 'm', 'Where is the cutting profile set for the fiber laser?',
  'In the CNC controller', ['On the clamping wire', 'In the dielectric tank', 'On the index plate'],
  'Step 2: set the required cutting profile in the CNC controller.', [73])
q('proc', 'm', 'Which settings are made in step 3 of the ME-106 fiber laser procedure?',
  'Laser power, cutting speed and assist gas', ['Ton, Toff and wire tension', 'Grit, grade and bond', 'Index plate and crank'],
  'Step 3: set laser power, cutting speed and assist gas.', [74])
q('proc', 'm', 'In the ME-106 fiber laser procedure, how is the beam focused on the job?',
  'Using the remote (focus control)', ['By moving the sheet by hand', 'By tilting the bed', 'By changing the gas'],
  'Step 4: focus the laser beam on the workpiece through the remote.', [75])
q('proc', 'm', 'Why is a dry run done before laser cutting?',
  'To check the laser will cut at the correct place', ['To clean the lens', 'To heat the sheet', 'To cool the nozzle'],
  'Step 5 and precaution 6: check by dry cutting (dry run) whether the laser will cut in the correct place.', [76, 84])
q('proc', 'm', 'Which step comes immediately AFTER the dry run in the fiber laser procedure?',
  'Start the beam and cut along the programmed path', ['Clamp the sheet', 'Set the power and speed', 'Focus the beam'],
  'Step 6: start the laser beam and cut along the programmed path.', [77])
q('proc', 'e', 'What is the LAST step of the ME-106 fiber laser procedure?',
  'Remove the cut piece and inspect the profile', ['Clamp the sheet', 'Do a dry run', 'Set the assist gas'],
  'Step 7: remove the cut piece and inspect the profile.', [78])
s('proc', 'h', 'What is the correct order of the ME-106 fiber laser procedure?',
  'Clamp sheet → set profile in CNC → set power, speed & gas → focus beam → dry run → cut → remove & inspect',
  ['Set power, speed & gas → clamp sheet → cut → focus beam → dry run → set profile in CNC → remove & inspect',
   'Dry run → clamp sheet → set profile in CNC → cut → focus beam → set power, speed & gas → remove & inspect',
   'Focus beam → cut → clamp sheet → dry run → set profile in CNC → set power, speed & gas → remove & inspect'],
  'From the Unconventional log sheet p.2.', [72, 73, 74, 75, 76, 77, 78])

# ============================ precautions ============================
q('prec', 'e', 'Which precaution applies to both wire EDM and laser cutting in the ME-106 log sheet?',
  'Clamp the workpiece properly', ['Dress the wheel before use', 'Lower the head 1 mm', 'Do not rotate the crank backwards'],
  'Precaution 1: clamp the workpiece properly.', [79])
q('prec', 'm', 'Which wire EDM precaution is listed on the ME-106 log sheet?',
  'Maintain correct wire tension and spark gap', ['Keep the wire touching the job', 'Use tap water as dielectric', 'Remove the dielectric during cutting'],
  'Precaution 2: maintain correct wire tension and spark gap.', [80])
q('prec', 'm', 'What must be ensured about the dielectric during wire EDM?',
  'A continuous supply of dielectric fluid', ['It is switched off during the cut', 'It is replaced by oxygen', 'It is heated to boiling'],
  'Precaution 3: ensure continuous supply of dielectric fluid.', [81])
q('prec', 'm', 'Which electrical settings must be set correctly in wire EDM (log sheet)?',
  'Ton, Toff and peak current', ['Grit, grade and bond', 'Feed rod and lead screw', 'Voltage of the plating bath'],
  'Precaution 4: set Ton, Toff and peak current correctly.', [82])
q('prec', 'm', 'Which laser precaution is listed on the ME-106 log sheet?',
  'Set correct laser power and cutting speed', ['Look into the beam to focus it', 'Use oil as dielectric', 'Keep the wire slack'],
  'Precaution 5: set the correct laser power and cutting speed.', [83])

# ============================ AR / TF ============================
ar('theory', 'h', 'Wire EDM can cut hardened tool steel easily.',
   'In EDM the hardness of the workpiece does not affect material removal.', 'a',
   'Both true, and R explains A: removal is by sparks, so only conductivity matters, not hardness.', [14])
ar('theory', 'h', 'Fiber lasers are preferred for cutting metal sheet.',
   'The fiber-laser wavelength (10.6 µm) is longer than that of CO₂ lasers.', 'c',
   'A is true but R is false: fiber ≈ 1.06 µm (shorter); CO₂ ≈ 10.6 µm. Metals absorb the shorter wavelength better.', [40, 41])
ar('param', 'h', 'Nitrogen is used as assist gas for stainless steel.',
   'Nitrogen gives clean, oxide-free cut edges.', 'a', 'Both true and R explains A.', [46])
tf('theory', 'e', 'In wire EDM, the wire must touch the workpiece to cut it.', False,
   'False. A spark gap is kept; contact would short-circuit.', [8, 9])

# ============================ diagrams ============================
B.labels('unconventional/wedm', 'p', cat='parts', diffs={'p': 'e'})
B.labels('unconventional/wedm', 'w', cat='parts', only={'w': ['B', 'F', 'I', 'K']})
B.labels('unconventional/wedm', 'f', cat='parts', only={'f': ['F', 'I', 'J', 'H']}, diffs={'f': 'm'})
SG = 'unconventional/spark-gap'
B.labels(SG, 'p', cat='theory', diffs={'p': 'm'})
n('num', 'h', 'In the spark-gap figure, the wire diameter F is 0.20 mm and gap B is 0.04 mm. What is kerf width G?',
  '0.28 mm', ['0.24 mm', '0.20 mm', '0.40 mm'],
  'Kerf = d + 2g = 0.20 + 0.08 = 0.28 mm.', [26], fig=SG)
q('theory', 'm', 'In the spark-gap figure, what fills the gap between the wire and the work?', 'Deionised water (dielectric)', ['Air at atmospheric pressure', 'Molten brass', 'Assist gas (oxygen)'],
  'H is the dielectric: it insulates, cools and flushes debris.', [18, 20], fig=SG)
LH = 'unconventional/laser-head'
B.labels(LH, 'p', cat='parts', diffs={'p': 'm'})
B.labels(LH, 'f', cat='parts', only={'f': ['B', 'C', 'D']}, diffs={'f': 'm'})
JB = 'unconventional/jobs-q'
B.labels(JB, 'p', cat='dims', diffs={'p': 'e'}, extra_parts=['Die-sinking EDM', 'CNC milling machine'])
q('dims', 'm', 'In the figure, what are the dimensions of the job in panel A?', '10 mm × 10 mm × 5 mm', ['10 mm × 5 mm × 5 mm', '20 mm × 20 mm × 5 mm', '10 mm × 10 mm × 10 mm'],
  'Panel A is the wire-EDM square: 10 × 10 mm, 5 mm thick.', [59], fig=JB)
B.labels('unconventional/edm-compare', 'p', cat='theory', diffs={'p': 'm'}, extra_parts=['Electrochemical machining', 'Laser beam machining'])
q('theory', 'm', 'In the EDM comparison figure, which panel normally uses deionised water as the dielectric?', 'B', ['A'],
  'Panel B (wire EDM) uses deionised water; panel A (die-sinking) usually uses kerosene/oil.', [18, 19], fig='unconventional/edm-compare')

B.save()
