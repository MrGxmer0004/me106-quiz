"""Electroplating question bank. Correct option first; options kept similar in length."""
from qlib import Bank

B = Bank('electroplating')
q, n, s, tf, ar = B.q, B.n, B.s, B.tf, B.ar

# ============================ principle ============================
q('def', 'e', 'Electroplating is…',
  'Depositing a thin metal coating on a conducting job', ['Removing metal by sparks from a job', 'Joining two metals by melting them', 'Hardening a job by quenching it'],
  'Electroplating applies a thin layer of metal on a metallic or other conducting substrate to improve appearance or surface properties.', [1])
q('theory', 'e', 'Electroplating is based on which process?',
  'Electrolysis', ['Electrical discharge', 'Induction heating', 'Photolithography'],
  'Electroplating is based on electrolysis.', [2])
q('theory', 'e', 'In electroplating, the workpiece to be coated is connected to the…',
  'Cathode (negative terminal)', ['Anode (positive terminal)', 'Earth only', 'Voltmeter'],
  'The substrate (workpiece) is the cathode; the metal to be deposited is the anode.', [3])
q('theory', 'e', 'In electroplating, the anode is usually…',
  'A plate of the metal to be deposited', ['The workpiece itself', 'A glass rod', 'A block of rubber'],
  'The anode is usually the plating metal, connected to the positive terminal.', [4])
q('theory', 'm', 'During plating, the positive metal ions in the bath move towards the…',
  'Cathode (workpiece), where they deposit as metal', ['Anode, where they deposit as metal', 'Tank wall, where they settle', 'Surface, where they escape as gas'],
  'Metal cations migrate to the cathode, gain electrons and deposit; the anode dissolves to replace them.', [5])
q('theory', 'm', 'What happens to the anode during electroplating?',
  'It dissolves into the bath, replacing the metal ions', ['It gets plated with a new layer', 'It stays completely unchanged', 'It gives off oxygen only'],
  'The anode metal goes into solution as ions, keeping the bath concentration up.', [5])
q('theory', 'e', 'Which type of electric supply is needed for electroplating?',
  'Direct current (DC)', ['Alternating current (AC)', 'High-frequency AC', 'Static charge only'],
  'Plating needs a DC source of variable voltage and current.', [6])
q('parts', 'm', 'Which of these is NOT a component of an electroplating cell?',
  'Magnetic chuck', ['DC power source', 'Anode and cathode', 'Electrolyte in a tank'],
  'A plating cell has a DC source, conductors, meters, cathode, anode and electrolyte (bath) in a tank. A magnetic chuck belongs to a surface grinder.', [7])
q('parts', 'm', 'In the plating circuit, how are the ammeter and voltmeter connected?',
  'Ammeter in series; voltmeter across the cell', ['Ammeter across; voltmeter in series', 'Both in series with the cell', 'Both across the anode only'],
  'Current is measured in series and voltage across the cell.', [8])
q('def', 'e', 'The electrolyte (bath) in electroplating is…',
  'A solution containing ions of the plating metal', ['Pure distilled water only', 'Kerosene or other dielectric oil', 'A dry powder of the plating metal'],
  'The bath supplies ions of the metal to be deposited.', [9])

# ============================ Faraday ============================
q('theory', 'm', 'According to Faraday\'s first law, the mass of metal deposited is proportional to…',
  'The quantity of electricity passed (I × t)', ['The voltage only', 'The size of the tank', 'The temperature of the anode'],
  'm ∝ Q = I × t. Current and time are the most important parameters.', [10, 11])
q('param', 'e', 'Which two parameters mainly decide how much metal is deposited?',
  'Current and time', ['Voltage and tank size', 'Colour and temperature', 'pH and tank shape'],
  'The amount deposited depends on the quantity of electricity: current × time.', [11])
q('theory', 'm', 'How much charge is needed to deposit one gram-equivalent of any metal?',
  '96,500 coulombs (1 faraday)', ['9,650 coulombs', '6.02 × 10²³ coulombs', '1,000 coulombs'],
  '1 faraday = 96,500 C deposits one gram-equivalent.', [12])
q('def', 'm', 'The mass deposited in electroplating is given by m =…',
  'M·I·t / (n·F)', ['n·F / (M·I·t)', 'M·n·F / (I·t)', 'I·t / (M·n·F)'],
  'M = atomic mass, n = valency, I = current (A), t = time (s), F = 96,500 C/mol.', [13])
q('theory', 'h', 'Faraday\'s second law states that, for the same charge, the masses deposited are proportional to…',
  'The chemical equivalents (M/n) of the metals', ['The voltages applied', 'The densities of the metals', 'The tank volumes'],
  'Equal charge deposits masses in the ratio of the equivalent weights.', [14])
q('param', 'm', 'For copper, the electroplating lecture gives the mass deposited as about…',
  '1.185 × I × t grams (I in A, t in hours)', ['1.185 × I × t kilograms', '0.185 × I × t grams', '11.85 × I × t grams'],
  'For Cu²⁺: 63.5/(2 × 96,500) × 3600 = 1.185 g per ampere-hour.', [15])
n('num', 'm', 'How much copper is deposited by 2 A flowing for 3 hours?',
  '≈ 7.11 g', ['≈ 2.37 g', '≈ 0.59 g', '≈ 71.1 g'],
  'm = 1.185 × I × t = 1.185 × 2 × 3 = 7.11 g.', [15])
n('num', 'h', 'In the ME-106 copper plating step, about 5 A flows for 30 s. Roughly how much copper is deposited?',
  '≈ 0.049 g', ['≈ 0.49 g', '≈ 4.9 g', '≈ 177.8 g'],
  't = 30 s = 1/120 h. m = 1.185 × 5 × (1/120) ≈ 0.049 g. Using 30 hours instead of 30 seconds gives 177.8 g.', [15, 42])
n('num', 'h', 'Using m = M·I·t/(n·F), how much copper (M = 63.5, n = 2) is deposited by 2 A in 965 s?',
  '≈ 0.635 g', ['≈ 1.27 g', '≈ 0.318 g', '≈ 63.5 g'],
  'm = 63.5 × 2 × 965 / (2 × 96,500) = 0.635 g. Forgetting n = 2 gives 1.27 g.', [13])
n('num', 'h', 'How long does it take to deposit 1 g of copper (M = 63.5, n = 2) with a current of 2 A?',
  '≈ 25 minutes', ['≈ 12.7 minutes', '≈ 50 minutes', '≈ 4.2 hours'],
  't = m·n·F / (M·I) = 1 × 2 × 96,500 / (63.5 × 2) ≈ 1520 s ≈ 25.3 min.', [13])
n('num', 'h', 'Nickel plating in the ME-106 lab runs at about 5 A for 6 minutes. Approximately how much nickel is deposited? (≈ 1.095 g per A·h)',
  '≈ 0.55 g', ['≈ 5.5 g', '≈ 0.055 g', '≈ 32.9 g'],
  't = 6 min = 0.1 h. m = 1.095 × 5 × 0.1 ≈ 0.55 g.', [16, 49])
n('num', 'm', 'What quantity of charge passes when 2 A flows for 30 seconds?',
  '60 C', ['15 C', '0.067 C', '600 C'],
  'Q = I × t = 2 × 30 = 60 coulombs.', [10, 17])
n('num', 'h', 'The electrochemical equivalent of copper (Cu²⁺, M = 63.5) is about…',
  '3.29 × 10⁻⁴ g/C', ['6.58 × 10⁻⁴ g/C', '1.185 g/C', '96,500 g/C'],
  'Z = M/(nF) = 63.5/(2 × 96,500) = 3.29 × 10⁻⁴ g per coulomb.', [17])
n('num', 'h', '0.635 g of copper (density 8.96 g/cm³) is deposited evenly on an area of 10 cm². What is the coating thickness?',
  '≈ 71 µm', ['≈ 7.1 µm', '≈ 710 µm', '≈ 0.71 µm'],
  'Volume = 0.635/8.96 = 0.0709 cm³; thickness = 0.0709/10 = 0.00709 cm ≈ 71 µm.', [13])
q('param', 'm', 'Too high a current density during plating usually gives…',
  'Burnt, rough or powdery deposits', ['A thicker, brighter deposit', 'No deposit at all', 'A deposit on the anode instead'],
  'Excessive current density burns the deposit; the bath and job need the correct current per unit area.', [18, 75])

# ============================ cleaning ============================
q('proc', 'e', 'Why is the job cleaned thoroughly before electroplating?',
  'For good adhesion, a smooth surface and good appearance', ['To make the job heavier before plating', 'To magnetise the job for holding', 'To remove the need for current'],
  'Cleaning gives better adhesion of the coating, a smooth surface and an aesthetic appearance.', [19])
q('tools', 'e', 'Which tools are used for mechanical cleaning before plating?',
  'Wire (abrasive) brush and emery paper', ['Hacksaw and file', 'Diamond dresser', 'Index plate'],
  'Mechanical cleaning removes rust and burrs with a metal abrasive brush or emery paper (scratch brushing).', [20])
q('tools', 'm', 'In the ME-106 lab, polishing before plating is done on a…',
  'Cotton mop (buffing wheel) with emery compound', ['Grinding wheel with diamond', 'Lathe with a form tool', 'Shaper with an HSS tool'],
  'The board and log sheet: polishing with cotton mop and emery compound on the polishing machine.', [21])
q('def', 'm', 'Buffing is…',
  'Rubbing the job on a rotating cloth wheel with compound', ['Cutting the job on a slitting saw', 'Heating the job to remove grease', 'Dipping the job in acid to etch it'],
  'Buffing polishes/smoothens/shines a metal piece using a rotating fabric wheel charged with fine abrasive compound.', [22])
q('tools', 'm', 'Buffing compound consists of…',
  'Fine abrasive particles in a wax, soap or fat binder', ['Coarse sand in water', 'Pure copper powder', 'Dielectric oil and graphite'],
  'Abrasives: alumina, SiC, iron oxide, chromium oxide; binders: fatty acid, greaseless wax, soap.', [23])
q('tools', 'h', 'Which of these is NOT a type of buffing wheel listed in the electroplating lecture?',
  'Vitrified grinding wheel', ['Spiral sewn', 'Loose buff', 'Flannel'],
  'Buffing wheels: spiral sewn, loose buffs, concentric sewn and flannel. A vitrified wheel is a grinding wheel.', [24])
q('param', 'm', 'In buffing, low pressure on the wheel is used for…',
  'A finer finish', ['Faster metal removal', 'Saving time', 'Removing deep rust'],
  'More pressure is quicker but wastes compound; low pressure gives a finer finish. Pressure is applied by hand.', [25])
q('proc', 'm', 'What type of chemical cleaning is used in the electroplating lab?',
  'Electro-chemical cleaning plus chemical cleaning', ['Only mechanical cleaning', 'Only cleaning with water', 'Only sand blasting'],
  'The lecture: "actually it\'s electro-chemical cleaning and chemical cleaning".', [26])
q('theory', 'm', 'In electrochemical cleaning, the workpiece is made the…',
  'Anode (positive)', ['Cathode (negative)', 'Neutral electrode', 'Earth'],
  'Electrochemical cleaning is the reverse of electroplating: the job is the anode.', [27])
q('theory', 'h', 'In electrochemical cleaning, what removes rust and contaminants from the job?',
  'Oxygen gas released at the job surface', ['Hydrogen gas released at the anode tank', 'Copper ions plating over the rust', 'Steam produced by the current'],
  'At the job (anode): 4OH⁻ → 2H₂O + O₂ + 4e⁻. The oxygen bubbles scrub the surface.', [28])
q('theory', 'm', 'In chemical cleaning, trisodium phosphate is added to…',
  'Remove hydrocarbons like grease', ['Protect aluminium from soda', 'Supply copper ions', 'Increase the voltage'],
  'Trisodium phosphate removes grease; sodium silicate protects aluminium against soda; sodium carbonate is the base cleaner.', [29])
q('theory', 'm', 'In chemical cleaning, sodium silicate is added to…',
  'Protect aluminium against the soda', ['Remove grease from steel', 'Supply nickel ions', 'Brighten the copper deposit'],
  'Sodium silicate protects aluminium against attack by soda.', [29])
q('theory', 'h', 'Which of these chemicals is NOT in the ME-106 chemical-cleaning bath written on the lab board?',
  'Nickel sulphate', ['Sodium carbonate', 'Sodium hydroxide', 'Sodium silicate'],
  'The board lists Na₂CO₃, NaOH, trisodium phosphate, NaCN, Na₂SiO₃ and water. Nickel sulphate belongs to the nickel bath.', [30])
q('param', 'm', 'What conditions are used for chemical cleaning in the ME-106 lab (board)?',
  'About 6 V, 10–15 A, for about 5 minutes', ['About 1.5 V, 1 A, for 5 seconds', 'About 230 V AC, for 1 hour', 'No current at all, for 1 day'],
  'Lab board: voltage 6 V, current 10–15 A, time 5 min.', [31])
q('proc', 'm', 'After chemical cleaning in the ME-106 lab, the job is washed with…',
  'Water and pumice powder', ['Kerosene and wax', 'Molten salt', 'Dilute nickel solution'],
  'The log sheet: dip in the cleaning solution, then wash with water and pumice powder.', [32])
q('def', 'h', 'In plating practice, pickling means…',
  'Dipping in dilute acid to remove oxide scale and rust', ['Coating with wax before plating', 'Heating the job in oil', 'Polishing on a cloth mop'],
  'Degreasing removes oil, pickling (dilute acid dip) removes scale, and rinsing prevents chemical carry-over.', [33])

# ============================ copper ============================
q('app', 'm', 'Copper plating is used to…',
  'Give a corrosion-resistant coat and a base for other plating', ['Make the surface magnetic', 'Harden the steel core', 'Remove burrs from the job'],
  'Copper plating gives corrosion resistance and provides a base for later plating (e.g. nickel).', [34])
q('theory', 'm', 'Copper can be electroplated from which two types of bath?',
  'Acid bath or cyanide bath', ['Oil bath or water bath', 'Salt bath or sand bath', 'Nickel bath or chrome bath'],
  'Copper is plated by acid plating or cyanide plating; cyanide is popular.', [35])
q('adv', 'm', 'Which is an advantage of cyanide copper plating?',
  'Good adhesion and decorative finish on many metals', ['It is completely non-toxic', 'It needs no cleaning beforehand', 'It works without electric current'],
  'Cyanide copper plates steels, zinc, aluminium, magnesium, nickel and lead with good adherence and decorative finish.', [36])
q('theory', 'h', 'Why is a cyanide copper layer often applied before acid nickel plating on steel?',
  'It protects the steel from acid attack in the nickel bath', ['It makes the nickel layer thinner', 'It removes the need for cleaning', 'It turns the nickel layer magnetic'],
  'The cyanide copper strike protects the base metal from acid attack during subsequent acid plating.', [37])
q('theory', 'm', 'In the cyanide copper bath, copper cyanide is not soluble in water. What is added to dissolve it?',
  'Sodium or potassium cyanide', ['Sulphuric acid', 'Boric acid', 'Pumice powder'],
  'NaCN or KCN forms soluble copper complexes; excess cyanide gives good deposits and good anode corrosion.', [38, 39])
q('theory', 'h', 'Why is excess NaCN/KCN kept in the copper cyanide bath?',
  'For good-quality deposits and good anode dissolution', ['To make the bath acidic', 'To raise the bath temperature', 'To plate nickel at the same time'],
  'Excess free cyanide gives good-quality deposits and good anode corrosion.', [39])
q('theory', 'm', 'Caustic soda (NaOH) is added to the copper cyanide bath to…',
  'Increase conductivity and reduce cyanide decomposition', ['Supply copper ions', 'Lower the pH to acid', 'Remove the anode'],
  'NaOH/KOH increases conductivity, reduces electrochemical attack on steel containers and reduces decomposition of cyanide.', [40])
q('theory', 'h', 'In the copper cyanide bath, Rochelle salt is used to…',
  'Give a fine-grained copper deposit', ['Remove excess carbonate', 'Protect aluminium from soda', 'Supply nickel ions'],
  'Rochelle salt gives a fine-grained deposit; lime may be used to remove excess carbonate.', [41])
q('param', 'm', 'In the ME-106 copper plating step, what voltage is used?',
  '2 to 6 V', ['1.5 to 3 V', '6 to 10 V', '220 V AC'],
  'Copper plating: 2–6 V for about 25–30 s. (Nickel: 1.5–3 V for 5–7 min.)', [42])
q('param', 'm', 'For how long is the job kept in the copper bath in the ME-106 lab?',
  'About 25–30 seconds', ['About 5–7 minutes', 'About 1 hour', 'About 2 seconds'],
  'Copper: 25–30 s; nickel: 5–7 min.', [42])
q('param', 'm', 'Roughly what current is used for copper plating in the ME-106 lab?',
  'A few amperes (about 5–8 A)', ['A few milliamperes', 'About 100 A', 'About 1000 A'],
  'The log sheet gives 5–8 A (the board 6–8 A).', [43])
q('proc', 'e', 'In the ME-106 lab, when is the job taken out of the copper bath?',
  'When it turns reddish (copper coloured)', ['When it turns silvery white', 'When bubbles stop', 'After exactly one hour'],
  'The log sheet: dip in copper solution until the workpiece becomes red, then wash it again.', [44])

# ============================ nickel ============================
q('app', 'm', 'Nickel plating is done to improve…',
  'Wear and corrosion resistance and bright appearance', ['Electrical insulation of the job', 'Magnetic softness of the core', 'Weldability of the job'],
  'Nickel plating improves wear, heat or corrosion resistance and gives a bright decorative appearance.', [45])
q('theory', 'm', 'In a Watts nickel bath, the primary source of nickel ions is…',
  'Nickel sulphate (NiSO₄)', ['Nickel chloride (NiCl₂)', 'Boric acid (H₃BO₃)', 'Sodium cyanide (NaCN)'],
  'NiSO₄ supplies Ni ions; NiCl₂ increases conductivity and helps anode dissolution; boric acid controls pH.', [46])
q('theory', 'm', 'Boric acid is added to the nickel bath to…',
  'Control the pH of the solution', ['Supply nickel ions', 'Remove grease', 'Make the deposit red'],
  'Boric acid (H₃BO₃) buffers the pH.', [46])
q('theory', 'm', 'Nickel chloride in the nickel bath…',
  'Increases conductivity and helps the anode dissolve', ['Is the main source of copper', 'Removes oxygen bubbles', 'Lowers the bath temperature'],
  'NiCl₂ increases conductivity and helps dissolution of the Ni electrode.', [46])
q('theory', 'h', 'Why is sulphuric acid added regularly to the nickel bath?',
  'Hydrogen ions are lost as H₂ gas, so acid is replenished', ['To dissolve the copper layer', 'To make the bath alkaline', 'To supply nickel ions'],
  'As H⁺ ions are liberated as hydrogen gas, H₂SO₄ is added regularly.', [47])
q('parts', 'm', 'In nickel plating, the anode is…',
  'Nickel metal (lumps, or pieces in a titanium basket)', ['The mild-steel workpiece', 'A copper plate', 'A carbon rod only'],
  'Nickel anodes are lumps of various shapes, or small pieces kept in a titanium basket.', [48])
q('param', 'm', 'What voltage and time are used for nickel plating in the ME-106 lab?',
  '1.5–3 V for 5–7 minutes', ['2–6 V for 25–30 seconds', '6 V for 5 minutes', '12 V for 1 hour'],
  'Nickel: 1.5–3 V, about 5 A, 5–7 min.', [49])
q('dims', 'm', 'In the ME-106 electroplating job, how much of the job is nickel plated?',
  'About half of it', ['The whole job', 'None of it', 'Only the threads'],
  'The log sheet: dip half of the copper-plated workpiece in the nickel solution, so both layers are visible.', [50])
q('theory', 'm', 'Which ingredients are written on the lab board for the nickel bath?',
  'Nickel salts, boric acid and water', ['Copper cyanide and NaCN', 'Sodium carbonate and NaOH', 'Kerosene and graphite'],
  'Board: nickel salts, boric acid, water; 1.5–3 V; 5 A/sq ft; 5–7 min.', [51])

# ============================ lab job / tools ============================
q('wmat', 'e', 'What is the workpiece material in the ME-106 electroplating job?',
  'Mild steel', ['Aluminium', 'Copper', 'Plastic'],
  'Name of operation: electroplating of workpiece (mild steel).', [52])
q('tools', 'e', 'Which of these is listed as a tool/material on the ME-106 electroplating log sheet?',
  'Pumice powder', ['Index plate', 'Grinding wheel', 'Hacksaw'],
  'Tools: mild-steel workpiece, emery paper, polishing machine, pumice powder, electroplating solution, wire.', [53])
q('tools', 'm', 'Which item is NOT on the ME-106 electroplating tool list?',
  'Vernier height gauge', ['Emery paper', 'Polishing machine', 'Wire'],
  'Tools: mild-steel workpiece, emery paper, polishing machine, pumice powder, electroplating solution, wire.', [53])
q('tools', 'm', 'Why is the job tied with wire in the electroplating lab?',
  'To hang it in the solution and make the electrical contact', ['To measure its length', 'To stop it rusting', 'To heat it up'],
  'The job is tied with wire to dip it in the baths and connect it to the supply.', [54])
q('dims', 'm', 'What does the ME-106 electroplating job drawing show?',
  'A job with a copper-plated part and a nickel-plated part', ['A spur gear with 22 teeth', 'A stepped shaft with a thread', 'A 10 × 10 × 5 mm square'],
  'The drawing shows the workpiece with copper and nickel electroplated regions, the solution box and the polishing machine.', [55])

# ============================ procedure ============================
q('proc', 'e', 'What is the FIRST step of the ME-106 electroplating procedure?',
  'Clean with emery paper and polish on the machine', ['Dip the job in the nickel bath', 'Dip the job in the copper bath', 'Wash the job with pumice powder'],
  'Step 1 (mechanical cleaning): clean with emery paper, polish with cotton mop and emery compound on the polishing machine.', [56])
q('proc', 'm', 'Which step comes immediately AFTER mechanical cleaning and polishing?',
  'Chemical cleaning, then washing with water and pumice', ['Nickel plating', 'Copper plating', 'Drying in an oven'],
  'Step 2: tie with wire, dip in the cleaning solution, wash with water and pumice powder.', [57])
q('proc', 'm', 'In the ME-106 lab, which plating is done FIRST?',
  'Copper plating', ['Nickel plating', 'Chromium plating', 'Zinc plating'],
  'Copper (2–6 V, 25–30 s) is plated first; then half the job is nickel plated.', [58, 59])
q('proc', 'm', 'What is done immediately after the copper plating step?',
  'The job is washed again', ['The job is polished on a grinding wheel', 'The job is heated', 'The job is cut in half'],
  'The log sheet: plate until reddish, then wash it again, then nickel plate.', [58])
q('proc', 'e', 'What is the LAST step of the ME-106 electroplating procedure?',
  'Nickel plating half of the job', ['Mechanical cleaning', 'Chemical cleaning', 'Copper plating'],
  'Step 4: dip half of it in nickel solution (1.5–3 V, 5 A, 5–7 min); electroplating is done.', [59])
s('proc', 'm', 'What is the correct order of the ME-106 electroplating steps?',
  'Mechanical cleaning → polishing → chemical cleaning → washing → copper plating → washing → nickel plating',
  ['Polishing → nickel plating → chemical cleaning → washing → mechanical cleaning → washing → copper plating',
   'Chemical cleaning → copper plating → mechanical cleaning → washing → polishing → washing → nickel plating',
   'Copper plating → washing → nickel plating → polishing → washing → chemical cleaning → mechanical cleaning'],
  'From the log sheet and the lab board.', [60])
s('proc', 'm', 'The general industrial sequence for electroplating is…',
  'Degreasing → rinsing → pickling → rinsing → plating → rinsing → drying',
  ['Plating → rinsing → degreasing → rinsing → pickling → drying → rinsing', 'Pickling → rinsing → plating → degreasing → rinsing → drying → rinsing', 'Degreasing → plating → rinsing → pickling → drying → rinsing → rinsing'],
  'Clean, rinse, remove scale, rinse, plate, rinse, dry.', [61])

# ============================ precautions ============================
q('prec', 'e', 'Which dress precaution appears on the ME-106 electroplating log sheet?',
  'Wear proper shoes and an apron', ['Wear sandals for comfort', 'Wear no apron near baths', 'Wear loose sleeves'],
  'Precaution 1: wear proper shoes and apron in the workshop.', [62])
q('prec', 'm', 'According to the ME-106 log sheet, the workpiece should be handled carefully during…',
  'Cleaning and polishing', ['Weighing only', 'Painting', 'Packing'],
  'Precaution 2: handle the workpiece with care while cleaning and polishing.', [63])
q('prec', 'm', 'Which precaution about the equipment is on the ME-106 electroplating log sheet?',
  'Operate the plating machines with caution, at a safe distance', ['Touch the bath to check the temperature', 'Switch the supply to AC for safety', 'Lean over the tank to watch closely'],
  'Precautions 3–4: operate the electroplating machines with caution and maintain an appropriate distance.', [64])
q('prec', 'm', 'Why must cyanide baths be handled with great care?',
  'Cyanide is highly poisonous to use and dispose of', ['Cyanide is radioactive', 'Cyanide is magnetic', 'Cyanide makes the job brittle'],
  'Cyanide is highly poisonous; its level in air is limited to 5 mg/m³ over an 8-hour shift.', [65])
q('prec', 'h', 'The amount of cyanide in workshop air should be limited to about…',
  '5 mg/m³ averaged over an 8-hour shift', ['500 mg/m³ at any time', '5 g/m³ per hour', 'No limit is needed'],
  'From the electroplating lecture precautions slide.', [65])
q('prec', 'm', 'When can cyanide dust be produced?',
  'When handling cyanide salts or making up solutions', ['Only during nickel plating', 'Only when the bath is cold', 'Never; cyanide is always liquid'],
  'Cyanide dust is possible when handling any cyanide salts, making additions or making up new solutions.', [66])
q('prec', 'e', 'Which precaution applies after copper cyanide plating?',
  'Rinse the parts thoroughly and wash your hands', ['Taste the bath to check strength', 'Dry the job without rinsing', 'Store the job in the bath'],
  'Don\'t touch the solution; rinse plated parts thoroughly to remove trapped solution; wash hands properly.', [67])
q('prec', 'm', 'Why is copper dust from grinding and polishing a hazard?',
  'Copper dust in large quantity is dangerous to breathe', ['It is explosive in water', 'It is radioactive', 'It turns into cyanide'],
  'The lecture warns that copper dust in large quantities (from grinding, polishing) is dangerous.', [68])
q('prec', 'm', 'Nickel and nickel salts can cause…',
  'Skin dermatitis and lung problems on long exposure', ['Instant burns like strong acid', 'Radiation sickness', 'No health effects at all'],
  'Nickel can cause dermatitis through skin contact and may affect lungs during long-term inhalation.', [69])
q('prec', 'e', 'Which protection is mandatory near plating baths?',
  'Protective clothing, eye protection and gloves', ['Only a cap', 'Only ear plugs', 'No protection is needed'],
  'Mandatory protective clothing, eye protection and gloves; wash immediately after skin contact.', [70])
q('prec', 'm', 'Which ventilation is required for plating areas?',
  'Local exhaust ventilation', ['None; windows must be closed', 'Only a ceiling fan', 'A heater to warm the room'],
  'Local exhaust ventilation removes fumes and mist from the baths.', [71])
q('prec', 'e', 'Near the plating line you must not…',
  'Eat, drink or smoke', ['Wear gloves', 'Wear an apron', 'Use exhaust fans'],
  'Avoid smoking, eating and drinking on the plating line.', [72])
q('prec', 'm', 'When diluting concentrated acid for a bath, you should…',
  'Add the acid slowly to water', ['Add water quickly to the acid', 'Mix them in a closed bottle', 'Heat the acid first'],
  'Always add acid to water slowly; adding water to acid can boil and splash.', [73])

# ============================ defects / applications ============================
q('def', 'm', 'If the job is not cleaned properly before plating, the coating will…',
  'Peel off or blister due to poor adhesion', ['Be thicker and stronger', 'Plate faster', 'Become magnetic'],
  'Poor cleaning leads to poor adhesion.', [74])
q('def', 'h', 'Small pits in a plated surface are usually caused by…',
  'Hydrogen bubbles sticking to the cathode', ['Too low a current density', 'Excess polishing', 'Using a nickel anode'],
  'Anti-pitting agents are added to stop hydrogen bubbles clinging to the job; high current density gives burnt deposits.', [75])
q('def', 'h', 'The "throwing power" of a plating bath is its ability to…',
  'Deposit a uniform coat on recessed, irregular surfaces', ['Plate at very high voltage', 'Throw metal particles at the job', 'Remove rust quickly'],
  'Throwing power = uniformity of deposit on irregular shapes.', [76])
q('app', 'm', 'Which is NOT a purpose of electroplating?',
  'Reducing the hardness of the core metal', ['Corrosion protection', 'Decorative appearance', 'Building up worn parts'],
  'Plating is used for corrosion protection, decoration, wear resistance, building up worn parts and conductivity. It does not soften the core.', [77])
q('app', 'e', 'Which is a common application of electroplating?',
  'Decorative coats on bathroom fittings and car parts', ['Cutting sheet metal', 'Casting engine blocks', 'Turning shafts'],
  'Applications: automobile parts, bathroom fittings, utensils, jewellery, electrical contacts.', [78])
q('wmat', 'm', 'Which of these metals is commonly electroplated?',
  'Chromium', ['Tungsten carbide', 'Silicon carbide', 'Graphite'],
  'Common plating metals: copper, nickel, chromium, zinc, tin, silver, gold.', [79])

# ============================ AR / TF ============================
ar('theory', 'h', 'In electroplating, the workpiece is made the cathode.',
   'Positive metal ions are attracted to the negative electrode and deposit there.', 'a', 'Both true, and R explains A.', [3, 5])
ar('theory', 'h', 'In electrochemical cleaning the workpiece is made the anode.',
   'Electroplating requires an AC supply.', 'c', 'A is true; R is false — plating and electro-cleaning both use DC.', [27, 6])
tf('theory', 'e', 'Electroplating can be done with an AC supply.', False, 'False. A DC supply is needed.', [6])
tf('param', 'm', 'In the ME-106 lab, nickel plating takes longer than copper plating.', True,
   'True: copper ~25–30 s, nickel ~5–7 min.', [42, 49])

# ============================ diagrams ============================
B.labels('electroplating/cell', 'p', cat='parts', diffs={'p': 'e'}, extra_parts=['Buffing wheel'])
B.labels('electroplating/cell', 'f', cat='parts', only={'f': ['A', 'B', 'E', 'F']}, diffs={'f': 'm'})
CL = 'electroplating/cell'
q('theory', 'm', 'In the electroplating cell shown, the workpiece is connected to which terminal?', 'Negative (−)', ['Positive (+)', 'Neither terminal', 'Both terminals'],
  'B, the workpiece, is the cathode, connected to the − terminal of the DC source.', [3], fig=CL)
q('theory', 'm', 'In the figure, in which direction do the metal ions (M⁺) move?', 'From the anode side towards the workpiece', ['From the workpiece towards the anode', 'Up towards the DC source', 'Down into the tank wall'],
  'Positive metal ions move through the bath towards the cathode (the workpiece) and deposit on it.', [5], fig=CL)
q('theory', 'm', 'In the figure, which electrode slowly dissolves during plating?', 'A', ['B', 'C', 'G'],
  'A is the anode of the plating metal; it dissolves and replenishes the ions deposited on B.', [5], fig=CL)
FL = 'electroplating/process-flow'
B.labels(FL, 'p', cat='proc', diffs={'p': 'm'}, extra_parts=['Nickel stripping', 'Heat treatment'])
B.labels(FL, 'w', cat='proc', only={'w': ['C', 'E', 'G']}, diffs={'w': 'm'})
EC = 'electroplating/electrocleaning'
q('theory', 'm', 'The figure shows electrochemical cleaning. Why is the workpiece (A) connected the way it is?', 'Cleaning is the reverse of plating, so the job is the anode', ['So that copper plates on it as the cathode', 'So that the job becomes magnetic', 'Because an AC supply is used here'],
  'In electro-cleaning the job is made the anode; oxygen released on it scrubs off rust.', [27], fig=EC)
B.labels(EC, 'p', cat='theory', diffs={'p': 'm'}, extra_parts=['Hydrogen gas bubbles', 'Copper deposit'])
B.labels('electroplating/buffing', 'p', cat='tools', diffs={'p': 'e'}, extra_parts=['Grinding wheel', 'Wire brush'])

B.save()
