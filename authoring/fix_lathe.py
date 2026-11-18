# Option-length balancing patches for lathe.py: question text -> new distractors (or {'c': correct, 'w': wrongs}).
PATCH = {
 'On a lathe, the tailstock and carriage slide along the…':
  ['Threads of the lead screw under the bed', 'Dovetail slide on top of the cross-slide', 'Keyway cut along the length of the feed rod'],
 'Besides varying spindle speed, the headstock gear box also…':
  ['Locks the carriage in place for parting-off', 'Moves the tailstock along the bed guideways', 'Holds the dead centre in line with the spindle'],
 'Which of these is a function of the tailstock?':
  ['Giving the different speed changes to the spindle', 'Engaging the half-nut on the lead screw for threading', 'Swivelling the tool post to the angle for tapers'],
 'Why can the tailstock be moved along the bed?':
  ['To lock the carriage in position for facing', 'To set the pitch of the thread being cut', 'To change the speed of the main spindle'],
 'Which of these is a part of the TAILSTOCK?':
  ['Half-nut lever (apron)', 'Compound slide (top slide)', 'Tumbler gears (headstock)'],
 'In taper turning by the compound-rest method, how is the feed given?':
  ['By setting the tailstock over from the axis', 'Automatically, through the feed rod and apron', 'Automatically, through the lead screw and half-nut'],
 'Which part of a lathe collects the chips and coolant that fall from the work?':
  ['Gear box (feed box)', 'Apron (carriage front)', 'Saddle (H-shaped slide)'],
 'Which of these is NOT used to specify a centre lathe?':
  ['Distance between the centres', 'Swing diameter over the bed', 'Length of the lathe bed'],
 'When work is turned between centres, what actually drives (rotates) the workpiece?':
  ['Friction between the work and the dead centre', 'The lead screw acting through the half-nut', 'The tailstock quill pressing on the work end'],
 'What is the main drawback of a 4-jaw independent chuck compared with a 3-jaw chuck?':
  ['It cannot be used for facing the end of the job', 'It cannot hold round work of any diameter', 'It grips the work far less firmly than a 3-jaw'],
 'A collet holds bar stock by…':
  ['Four independent jaws, each worked by a screw', 'Magnetic attraction between collet and bar', 'Friction between the bar and the dead centre'],
 'In the ME-106 lathe lab, the diameter of the job was checked with an…':
  ['Inside micrometer and depth gauge', 'Dial indicator on a magnetic stand', 'Bevel protractor and try square'],
 'An outside caliper has no scale. How is the measured diameter read?':
  ['Directly from the Vernier scale on its legs', 'From a dial gauge fixed on its hinge', 'From the cross-slide dial of the lathe'],
 'The angle that prevents the tool flank from rubbing against the work is the…':
  ['Rake (top) angle', 'Helix (lead) angle', 'Point (lip) angle'],
 'Which operation reduces the diameter of the work along its whole length?':
  ['Chamfering at the end', 'Facing across the end', 'Parting-off (cutting off)'],
 'Knurling on a lathe is done to…':
  ['Enlarge an already drilled hole to size', 'Cut off the finished job from the bar', 'Cut a helical thread on the surface'],
 'A narrow recess cut at the end of a thread (as in our job) is made by…':
  ['Chamfering with a 45° tool', 'Knurling with a knurling tool', 'Reaming with a hand reamer'],
 'In parting-off on a lathe…':
  ['The tool is fed parallel to the lathe axis', 'The lead screw drives the tool along the work', 'The compound rest is swivelled to 45° and fed'],
 'Why is a centre hole drilled at the end of the workpiece?':
  ['To reduce the weight of the finished job', 'To hold the knurling tool during knurling', 'To start the thread at the correct pitch'],
 'In form turning, the shape produced on the work is obtained by…':
  ['Engaging the lead screw and half-nut', 'Setting over the tailstock from the axis', 'Swivelling the compound rest to an angle'],
 'Why is the centre lathe called a versatile machine?':
  ['It works without any cutting tool at all', 'It cuts gears using an index plate and crank', 'It cuts on both the forward and return strokes'],
 'For which kind of part is a centre lathe LEAST suitable?':
  ['Round shafts and pins', 'Bolts and threaded rods', 'Bushes and collars'],
 'Square threads are mainly used in…':
  ['Pipe joints and plumbing fittings', 'Spectacle-frame hinge screws', 'Electrical lamp-holder fittings'],
 'A buttress thread is used where…':
  ['Equal load must be carried in both directions', 'Fluid-tight joints in pipes are needed', 'Only light fastening of thin parts is needed'],
 'In the ME-106 lathe lab, why was the spindle speed reduced to about 90 rpm for threading?':
  {'c': 'Slow speed gives time to withdraw the tool at the groove', 'w': ['The lead screw cannot be rotated above 90 rpm', 'HSS tools soften and melt above 90 rpm', 'Facing has to be repeated at the lower speed']},
 'In turning, "feed" means…':
  ['Number of passes needed to finish the job', 'Surface speed of the work in m/min', 'Thickness of metal removed in one pass'],
 'What is the objective of the ME-106 lathe job?':
  ['To finish a flat steel surface by grinding', 'To cut a spur gear on an aluminium disc', 'To reduce a block to 38 × 21 × 73 mm on a shaper'],
 'What is the correct order of the first four steps of the ME-106 lathe job?':
  ['Set speed → facing → mark 115 mm and fix in 4-jaw chuck → measure the bar', 'Facing → measure the bar → mark 115 mm and fix in 4-jaw chuck → set speed', 'Mark 115 mm and fix in 4-jaw chuck → facing → measure the bar → set speed'],
 'What is the FIRST step of the ME-106 lathe procedure?':
  ['Swivel the compound rest to the taper angle', 'Perform facing to bring the job to length', 'Set the spindle to 90 rpm for threading'],
 'In the ME-106 lathe procedure, which step comes immediately AFTER fixing the job in the four-jaw chuck?':
  ['Taper turning with the compound rest', 'Thread cutting at 1.5 mm pitch', 'Removing the job to measure it again'],
 'Why must the job be checked for centring after fixing it in the four-jaw chuck?':
  ['The tailstock moves automatically during cutting', 'The thread pitch has to be set from the centre', 'The lead screw has to be aligned with the job'],
 'In the ME-106 lathe job, facing is done to…':
  ['Cut the 1.5 mm pitch thread', 'Reduce the diameter to Ø34', 'Turn the taper at the end'],
 'In the 2025 ME-106 lathe log sheet, which step comes immediately after facing?':
  ['Knurling the Ø32 end section', 'Parting-off the finished job', 'Thread cutting at 1.5 mm pitch'],
 'How is the taper on the ME-106 job turned?':
  ['By setting the tailstock over from the axis', 'With a broad form tool plunged straight in', 'By engaging the lead screw and half-nut'],
 'Before cutting the 1.5 mm pitch thread on the ME-106 job, the operator…':
  ['Engages the feed rod for power cross feed', 'Swivels the compound rest to 3.81° for the taper', 'Removes the four-jaw chuck and fits a collet'],
 'Which is the correct sequence of steps on the 2025 ME-106 lathe log sheet?':
  ['Measure → threading → facing → groove & taper turning → mark 115 mm & fix in 4-jaw chuck → centre & set rotation',
   'Facing → measure → threading → mark 115 mm & fix in 4-jaw chuck → groove & taper turning → centre & set rotation',
   'Mark 115 mm & fix in 4-jaw chuck → threading → facing → measure → centre & set rotation → groove & taper turning'],
 'Which dress precaution is given on the ME-106 lathe log sheet?':
  ['Wear loose, comfortable clothes and sandals', 'Wear gloves while the chuck is rotating', 'Roll up sleeves loosely and wear a tie'],
 'Before switching on the lathe, you must always…':
  ['Loosen the tool post clamping screw', 'Engage the half-nut on the lead screw', 'Remove the tailstock from the bed'],
 'Which precaution appears on both ME-106 lathe log sheets?':
  ['Never switch the coolant pump off', 'Keep the dielectric fluid flowing', 'Dress the wheel before every cut'],
 'In the ME-106 lathe job, at what stage is the length of 115 mm marked on the bar?':
  ['After parting the job off the bar', 'After the taper has been turned', 'After the thread has been cut'],
 'In the ME-106 job, the 5 mm groove is cut…':
  {'c': 'After facing, together with taper turning, before threading', 'w': ['Before the raw bar is measured', 'After the thread has been finished', 'Before the job is faced to length']},
 'Why should the tool overhang from the tool post be kept short?':
  ['To engage the lead screw more easily', 'To increase the cutting speed of the work', 'To make the taper angle steeper'],
 'How is a job centred in a four-jaw chuck?':
  ['Run the lathe at high speed and watch the chips form', 'Tighten all four jaws together with one key turn', 'Bring up the tailstock and press the job hard'],
 'Which is the correct order for cutting a thread on a centre lathe?':
  ['Take light successive cuts → set gear box for pitch → engage half-nut → set tool square with centre gauge',
   'Engage half-nut → set gear box for pitch → set tool square with centre gauge → take one deep cut',
   'Set tool square with centre gauge → take light successive cuts → set gear box for pitch → engage half-nut'],
 'How is the finished thread on the lathe job checked?':
  ['With an outside caliper and steel rule only', 'With a try square held against the flanks', 'By comparing its colour with the bar'],
 'What should you do if your hand gets close to the rotating chuck?':
  ['Use a cloth to brake the chuck gently', 'Slow the chuck down with your palm', 'Grab the job firmly to stop it'],
 'Which of these is a safe practice on the lathe?':
  ['Leaving the chuck key in the chuck between jobs', 'Leaning on the carriage while it is cutting', 'Wearing a loose tie and open sleeves'],
 'Why must the tool and job be clamped firmly before starting the lathe?':
  ['To increase the cutting speed of the job', 'To reduce the pitch of the thread cut', 'To keep the tool cool during cutting'],
 'A student leaves the chuck key in the chuck and switches on. What is the danger?':
  ['The lead screw disengages from the half-nut', 'The pitch of the thread changes suddenly', 'The tailstock locks itself to the bed'],
 'Tight-fitting clothes are required in the lathe shop because…':
  ['They protect the operator from electric shock', 'They help in marking the job with chalk', 'They keep the coolant off the operator'],
 'Why does the lathe log sheet ask you to move the tailstock carefully?':
  {'c': 'It is heavy and can hit the carriage or run off the bed', 'w': ['It carries the live centre that drives the job', 'It controls the speed of the main spindle', 'It holds the lead screw used for threading']},
 'Why should measurements on the lathe be taken in proper lighting?':
  ['So that the chips cool down faster', 'So that the thread pitch does not change', 'So that the motor runs cooler'],
 'A long, continuous chip is winding around the rotating job. What should you do?':
  ['Increase the spindle speed so the chip breaks', 'Cut it with pliers while the lathe keeps running', 'Pull it off quickly by hand before it tangles'],
 'In the ME-106 lathe job, which marking tools are used in the marking step?':
  ['Scriber, dot punch and hammer', 'Divider, centre punch and V-block', 'Surface gauge, angle plate and scriber'],
 'Why is threading done LAST in the ME-106 lathe job?':
  {'c': 'The thread must run up to the groove, which is cut earlier', 'w': ['Threading has to be done before facing the ends', 'Threading removes the 1 × 45° chamfer at the end', 'The lead screw can be used only after facing']},
}

# cross-shop review: duplicates dropped
PATCH['Tight-fitting clothes are required in the lathe shop because…'] = {'drop': True}
PATCH['The correct way to clear long chips from a lathe is to…'] = {'drop': True}
PATCH['It is acceptable to measure the lathe job with a caliper while it is rotating slowly.'] = {'drop': True}
PATCH['Which of these is NOT a part of a single-point cutting tool?'] = {'drop': True}
PATCH['An outside caliper has no scale. How is the measured diameter read?'] = {'drop': True}
