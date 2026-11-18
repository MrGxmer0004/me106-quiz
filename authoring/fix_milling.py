# Option-length balancing patches for milling.py
PATCH = {
 'In milling, which element rotates and which is fed?':
  ['Both the cutter and the work reciprocate', 'The work rotates; the cutter is fed along it', 'Neither rotates; the table only vibrates'],
 'How does a milling cutter remove metal?':
  ['Abrasive grains on its face rub the metal away', 'One continuous chip is removed in each pass', 'The metal is melted by friction at the teeth'],
 'Why is the milling machine called one of the most versatile machine tools?':
  ['It needs no cutting tool for most operations', 'It can produce only cylindrical parts quickly', 'It removes metal only by abrasive grinding'],
 'Machining (including milling) is best described as a…':
  ['Additive process that builds up layers of material', 'Forming process that shapes metal without chips', 'Joining process that fuses two parts together'],
 'In down milling, the chip thickness is…':
  ['Zero at the start of the cut and maximum at the end', 'Constant from the start to the end of the cut', 'Zero throughout, since the teeth only rub'],
 'Which is a DISADVANTAGE of up milling?':
  ['It cannot be used at all on work having scale', 'It gives the smoothest finish of all methods', 'It can only be done on a vertical machine'],
 'Which is an ADVANTAGE of up milling?':
  ['The cutter never chatters, even with light clamping', 'It gives the best surface finish of all methods', 'It needs the least clamping force on the work'],
 'Why is down milling NOT suitable for workpieces with surface scale?':
  ['It needs a dividing head to be fitted to the table', 'The chip thickness becomes zero at the scale', 'The work is lifted off the table by the cutter'],
 'Up milling is preferred when the machine has significant backlash in the table feed screw. Why?':
  ['The cutter pulls the table forward into the cut', 'It removes the need to clamp the work at all', 'The chip thickness is maximum at entry, which helps'],
 'Plain (slab) milling produces…':
  ['Gear teeth, using a form cutter on the arbor', 'A slot, using the end teeth of the cutter', 'A V-groove, using a double-angle cutter'],
 'Straddle milling is commonly used to produce…':
  ['Spur gear teeth on a blank', 'Internal threads in a bore', 'T-slots in machine tables'],
 'Which cutters can be used to cut slots or keyways?':
  ['Face mill only, with inserts', 'Fly cutter only, single-point', 'Grinding wheel only, vitrified'],
 'A roughing end mill has wavy (serrated) cutting edges. It is used for…':
  ['Final finishing of involute gear teeth', 'Polishing surfaces to a mirror finish', 'Cutting very thin slots and parting off'],
 'On a milling cutter, the keyway in the bore is used to…':
  ['Set the helix angle of the teeth', 'Collect chips during the cut', 'Hold the coolant near the teeth'],
 'Column-and-knee milling machines are classed as horizontal or vertical according to the…':
  ['Direction in which the knee moves', 'Type of coolant used on the work', 'Shape of the base casting'],
 'Which statement correctly compares horizontal and vertical milling machines?':
  ['Horizontal: more versatile for profiles; vertical: heavier metal removal', 'Vertical machines cannot cut slots; horizontal machines cannot face', 'Both machines have identical uses and use the same cutters'],
 'What type of milling machine is used for the gear job in the ME-106 lab?':
  ['Bed-type (planer-type) milling machine', 'Hand milling machine without power feed', 'CNC vertical machining centre with ATC'],
 'Which of these is NOT a main component of a horizontal milling machine?':
  ['Knee (with elevating screw)', 'Arbor (carrying the cutters)', 'Overarm (overhanging arm)'],
 'In milling, indexing means…':
  ['Measuring the diameter of the cutter', 'Setting the cutting speed of the spindle', 'Clamping the work firmly in the vice'],
 'An index plate is…':
  ['A graduated dial fitted on the knee', 'A gear wheel having exactly 40 teeth', 'A table having T-slots for clamping'],
 'In direct indexing…':
  ['Two hole circles are used one after the other', 'Change gears drive the plate from the spindle', 'The worm drives the spindle through 40 : 1'],
 'Compound indexing involves…':
  ['Using change gears between the spindle and the index plate', 'Disengaging the worm and turning the plate directly by hand', 'Moving only the sector arms while the crank stays fixed'],
 'What is the purpose of the sector arms on a dividing head?':
  ['To engage the worm with the worm wheel when indexing', 'To change the 40 : 1 ratio of the dividing head', 'To lock the work spindle firmly while cutting'],
 'While indexing a gear, the index crank should never be turned backwards because…':
  ['The coolant supply will stop automatically', 'The cutter rotation will be reversed', 'The index plate will fall off its shaft'],
 'In standard gear terminology, 2.157/DP is the…':
  ['Clearance (root gap)', 'Circular pitch (arc)', 'Addendum (tip height)'],
 'A spur gear has teeth that are…':
  ['Cut on the inside of a ring', 'Inclined at an angle to the axis', 'Cut on the surface of a cone'],
 'Compared with spur gears, helical gears…':
  ['Are noisier and produce no axial thrust', 'Convert rotary motion into linear motion', 'Connect shafts that intersect at 90°'],
 'A worm and worm wheel connect shafts that are…':
  ['Intersecting at 90°', 'Parallel to each other', 'Co-axial (in line)'],
 'In an internal gear…':
  ['Teeth are cut on the surface of a cone', 'Teeth form a continuous screw thread', 'Teeth are cut along a straight bar'],
 'Crossed helical (spiral) gears are used for shafts that are…':
  ['Parallel to each other', 'Co-axial (in a line)', 'Intersecting at 90°'],
 'What is the objective of the ME-106 milling job?':
  ['To cut a helical gear from a round steel bar', 'To face-mill a rectangular block to 73 mm', 'To cut a keyway along a shaft with an end mill'],
 'How is the ME-106 gear blank held during milling?':
  ['In a 4-jaw chuck on the milling table', 'On the magnetic chuck of the table', 'In a machine vice clamped to the table'],
 'Which tools does the notebook list for the milling job?':
  ['Grinding wheel, dresser and coolant', 'Emery paper, wire and pumice powder', 'Hacksaw, flat file and scriber'],
 'What is the FIRST step of the ME-106 milling procedure?':
  ['Switch on the machine and the coolant', 'Cut the first tooth space on the blank', 'Polish the finished gear with a file'],
 'In the ME-106 milling procedure, what is calculated immediately after the number of teeth?':
  ['The grinding ratio of the cutter wear', 'The cutting speed of the cutter in m/min', 'The taper angle for the gear blank'],
 'Which step comes immediately after calculating the depth and indexing?':
  ['Polish the gear with the rough flat file', 'Measure the finished gear with a caliper', 'Remove the mandrel from the dividing head'],
 'What is the correct sequence of the ME-106 milling procedure?':
  ['Clamp blank and start → cut and index repeatedly → calculate N → fix index plate → file the gear → calculate depth & index',
   'Fix index plate → file the gear → calculate N → clamp blank and start → cut and index repeatedly → calculate depth & index',
   'Calculate depth & index → cut and index repeatedly → clamp blank and start → calculate N → fix index plate → file the gear'],
 'How are successive tooth spaces cut on the ME-106 gear?':
  ['Cut all the spaces at once with a gang of cutters', 'Index for all teeth first, then take one single cut', 'Rotate the blank continuously while the cutter feeds'],
 'In the ME-106 milling job, how many tooth spaces are cut (one per indexing position)?':
  {'c': '22 times', 'w': ['27 times', '33 times', '40 times']},
 'Why is the table brought back before indexing to the next tooth?':
  ['To let the coolant cool the blank down', 'To change the cutter for the next tooth', 'To reset the depth dial back to zero'],
 'Which precaution about the workpiece appears on the 2025 milling log sheet?':
  ['Demagnetise the workpiece after use', 'Coat the workpiece with pumice powder', 'Rinse the workpiece in the plating bath'],
 'Which precaution is specific to indexing on the dividing head?':
  ['Check that the grinding wheel clears the work', 'Do not lower the shaper head more than 2 mm', 'Maintain a constant spark gap with the wire'],
 'Which electrical precaution appears on the ME-106 milling log sheet?':
  ['Keep the control-panel door open while working', 'Touch the earth wire before starting', 'Reset the main breaker yourself if it trips'],
 'Which of these should be avoided while milling, according to the TA slides?':
  ['Safety shoes with steel toe caps', 'Supervision by the shop instructor', 'A workshop apron, properly tied'],
 'According to the milling TA slides, the machine should NOT be operated…':
  ['While wearing safety shoes', 'With the coolant switched on', 'With the cutter guard in place'],
 'What is the correct way to set the depth of cut for the gear teeth?':
  ['Move the work clear → raise the knee by the depth → touch the blank with the rotating cutter → zero the knee dial',
   'Raise the knee by the depth → touch the blank with the rotating cutter → zero the knee dial → move the work clear',
   'Zero the knee dial anywhere → raise the knee by the depth → move the work clear → touch the blank with the cutter'],
 'Which slide is used to put on the depth of cut for the gear teeth on a horizontal column-and-knee machine?':
  ['Index crank (dividing head)', 'Arbor support (on overarm)', 'Overarm (on the column)'],
 'Once the depth is set for gear cutting, which slides are locked?':
  ['Table only, leaving knee and saddle free', 'Index crank and sector arms only', 'Overarm and column, leaving all slides free'],
 'Before cutting the gear, the dividing head and tailstock centres must be…':
  ['Loosely held so that the blank can slip if needed', 'Removed from the table before the cut starts', 'Set at 45° to the table for a straight tooth'],
 'Which practice is correct on the milling machine?':
  ['Remove the guard so the cutter can be watched closely', 'Feed the work by hand into a stopped cutter', 'Use the highest speed for every work material'],
 'Before starting the cut, you should check that the cutter…':
  ['Has its teeth painted for easy counting', 'Is slightly loose on the arbor for safety', 'Is touching the blank at the full depth'],
}

# cross-shop review: duplicates dropped
PATCH['According to the milling TA slides, the machine should NOT be operated…'] = {'drop': True}
PATCH['Which eye protection is recommended while milling?'] = {'drop': True}
PATCH['Which of these should be avoided while milling, according to the TA slides?'] = {'drop': True}
PATCH['Chips on the milling table should be removed…'] = {'drop': True}
PATCH['When should the gear be measured or the chips removed on the milling machine?'] = {'drop': True}
PATCH['Which footwear precaution appears on the ME-106 milling log sheets?'] = {'drop': True}
