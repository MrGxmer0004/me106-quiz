"""General workshop safety. Correct option first; balanced lengths."""
from qlib import Bank

B = Bank('safety')
q, n, s, tf, ar = B.q, B.n, B.s, B.tf, B.ar

q('safety', 'e', 'Which item of PPE must be worn in every ME-106 shop?',
  'Workshop apron', ['Welding helmet', 'Laser goggles', 'Ear muffs'],
  'Every ME-106 log sheet asks for the workshop apron.', [1])
q('safety', 'e', 'Why are closed safety (leather) shoes required in the workshop?',
  'They protect the feet from falling objects and hot chips', ['They make walking faster', 'They insulate from all electric shock', 'They keep the floor clean'],
  'Proper shoes protect feet from dropped tools, jobs and hot chips.', [2])
q('safety', 'e', 'Why must loose clothing be avoided near machines?',
  'It can be caught by rotating parts', ['It gets dirty with coolant', 'It slows down the work', 'It affects the measurements'],
  'Loose sleeves, ties and clothes can be pulled into chucks, cutters and spindles.', [3])
q('safety', 'e', 'Which of these should be removed before working on a machine?',
  'Rings, bracelets, chains and wristwatches', ['Safety shoes', 'Apron', 'Safety goggles'],
  'Loose accessories can be caught by moving parts.', [4])
q('safety', 'e', 'What should a student with long hair do before operating a machine?',
  'Tie it back or cover it', ['Leave it loose', 'Wet it with coolant', 'Nothing'],
  'Long hair can be caught in rotating parts.', [5])
q('safety', 'e', 'Safety goggles are especially needed when…',
  'Chips, sparks or splashes can fly', ['Reading the log sheet', 'Measuring with a steel rule', 'Writing calculations'],
  'Grinding, chipping, filing and plating can throw particles or liquids.', [6])
q('safety', 'm', 'Why should gloves NOT be worn near rotating parts such as a lathe chuck?',
  'They can be caught and pull the hand in', ['They reduce the cutting speed', 'They damage the chuck', 'They make the job slippery to measure'],
  'A glove snagged by a rotating part drags the hand in.', [7])
q('safety', 'e', 'You may operate a workshop machine only…',
  'With the instructor\'s permission and supervision', ['Whenever the shop is open', 'If a friend shows you how', 'After hours when it is quiet'],
  'Do not operate the machine without supervision from the shop instructor.', [8])
q('safety', 'e', 'While a machine is running, you should…',
  'Stay alert and avoid talking or fooling around', ['Use your phone between cuts', 'Leave it to fetch tools', 'Lean on it to watch closely'],
  'Stay attentive during fixing and cutting.', [9])
q('safety', 'e', 'Where should you stand while a machine runs?',
  'At a safe distance from moving parts', ['As close as possible to the cutter', 'In line with the ram or wheel', 'On the machine base'],
  'Maintain a proper distance from the running machine.', [10])
q('safety', 'e', 'What must be removed from the lathe chuck before switching on?',
  'The chuck key', ['The tool post', 'The workpiece', 'The chip tray'],
  'A chuck key left in the chuck flies out when the spindle starts.', [11])
q('safety', 'e', 'Before measuring or adjusting a job on a machine, you must…',
  'Stop the machine', ['Increase the speed', 'Engage the feed', 'Remove the guard'],
  'Always stop the machine before measuring, cleaning, adjusting or changing tools.', [12])
q('safety', 'm', 'In case of trouble on a machine, the first thing to do is…',
  'Press the emergency stop / switch off', ['Pull the job out by hand', 'Run to fetch the instructor', 'Increase the feed to finish quickly'],
  'Know where the emergency stop is and use it at once.', [13])
q('safety', 'e', 'Is it acceptable to leave a running machine unattended?',
  'No, never', ['Yes, for a few minutes', 'Yes, if the job is small', 'Yes, if the coolant is on'],
  'Never leave a running machine unattended.', [14])
q('safety', 'e', 'Before starting the machine, the job and tool must be…',
  'Clamped firmly', ['Loosely held for adjustment', 'Oiled heavily', 'Painted with chalk'],
  'Loose work or tools can be thrown out.', [15])
q('safety', 'e', 'Chips and swarf should be removed with…',
  'A brush or chip hook, after stopping the machine', ['Bare hands while cutting', 'By blowing them away', 'A wet cloth while running'],
  'Chips are sharp and hot.', [16])
q('safety', 'm', 'Which electrical safety rule applies in the workshop?',
  'Never touch switches or connections with wet hands', ['Open panels to reset faults yourself', 'Use bare wires for quick connections', 'Bypass the earth wire if it trips'],
  'Water conducts electricity; do not touch electrical connections.', [17])
q('safety', 'e', 'Heavy machine parts and tools should be…',
  'Handled with care', ['Thrown onto the bench', 'Left on the machine bed', 'Moved by one person always'],
  'Handle heavy machines and tools with care.', [18])
q('safety', 'e', 'Why must the floor around machines be kept clean?',
  'Oil and chips on the floor cause slips and falls', ['It keeps the machine cool', 'It improves the surface finish', 'It reduces coolant use'],
  'Keep the area free of oil, chips and obstacles.', [19])
q('safety', 'e', 'After finishing work on a machine, you should…',
  'Clean it and return the tools to their place', ['Leave the chips for the next batch', 'Leave tools on the bed', 'Keep the machine running'],
  'Clean the machine and workspace after use.', [20])
q('safety', 'e', 'Which is a basic rule about tools?',
  'Use the right tool and never a damaged one', ['Any tool will do for any job', 'Damaged tools are fine for practice', 'Borrow tools without asking'],
  'Use the correct tool; do not use damaged tools.', [21])
q('safety', 'e', 'What should you do if you get even a small cut in the workshop?',
  'Report it to the instructor and get first aid', ['Ignore it and keep working', 'Wash it in coolant', 'Cover it with chalk'],
  'Report every injury; know where the first-aid box is.', [22])
q('safety', 'm', 'Which extinguisher should be used on an electrical or oil fire?',
  'CO₂ or dry powder', ['Water', 'Sand mixed with oil', 'A wet cloth'],
  'Never use water on electrical or oil fires; water is for ordinary combustibles.', [23])
q('safety', 'm', 'Water-type fire extinguishers are suitable only for…',
  'Ordinary combustibles like wood and paper', ['Electrical fires', 'Oil fires', 'Burning metals'],
  'Water conducts electricity and spreads oil fires.', [23])
q('safety', 'm', 'In safety colour codes, a solid blue circular sign means…',
  'A mandatory instruction (must do)', ['Danger / stop', 'Safe condition / first aid', 'Caution / warning'],
  'Red = stop/prohibition/fire, yellow = caution, green = safe/first aid, blue = mandatory.', [24])
q('safety', 'm', 'In safety colour codes, green indicates…',
  'Safe condition, first aid or exit', ['Danger', 'Mandatory action', 'Caution'],
  'Green = safe condition or first aid.', [24])
q('safety', 'm', 'Which of these is NOT a correct workshop safety practice?',
  'Wearing gloves while operating a drill', ['Wearing safety goggles while grinding', 'Tying back long hair', 'Stopping the machine before measuring'],
  'Gloves can be caught by rotating parts.', [7, 6, 5, 12])
q('safety', 'm', 'The ME-106 fitting lab summarises safety as…',
  'Skill + Awareness + Discipline', ['Speed + Force + Luck', 'Gloves + Goggles + Guards', 'Time + Effort + Tools'],
  'Safety = Skill + Awareness + Discipline.', [25])
s('safety', 'm', 'Which is the safe sequence when a job must be measured on a machine?',
  'Stop the machine → wait for it to come to rest → measure', ['Measure → stop the machine → wait', 'Slow the machine → measure while it turns → stop', 'Measure while running → stop → measure again'],
  'Never measure a moving job.', [12])
tf('safety', 'e', 'It is safe to remove chips with bare hands if you are careful.', False, 'False. Use a brush or chip hook after stopping the machine.', [16])
tf('safety', 'e', 'The chuck key must be removed before the lathe is switched on.', True, 'True. A key left in the chuck is flung out when the spindle starts.', [11])
ar('safety', 'h', 'Gloves must not be worn near rotating machine parts.',
   'A glove caught by a rotating part can drag the hand in.', 'a', 'Both true, and R explains A.', [7])
ar('safety', 'h', 'Water must not be used on an electrical fire.',
   'Water is a good electrical insulator.', 'c', 'A is true; R is false — water conducts electricity.', [23])

B.labels('safety/signs', 'p', cat='safety', diffs={'p': 'e'}, extra_parts=['Fire equipment location', 'Radiation hazard only'])
B.labels('safety/signs', 'w', cat='safety', only={'w': ['A', 'C']}, diffs={'w': 'm'})

B.save()
