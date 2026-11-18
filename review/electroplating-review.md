# Electroplating question bank: independent review

Reviewed: `src/data/questions/electroplating.json` (127 questions, ELP-0001 to ELP-0127), `knowledge/electroplating.md` (79 facts), `corrections.md` #19–21, the 4 `electroplating/*` registry entries in `src/data/figures.json`, all 4 PNGs in `.render/electroplating/` (and anchor coordinates in `scripts/figures/fig_electroplating.py`), lecture slides p.2–12, the lab board and the 2025 log sheet.

## Summary

| Severity | Count | IDs |
|---|---|---|
| Critical | 0 | none |
| Major | 3 items | figure `electroplating/cell` label G (ELP-0104, 0100); ELP-0121 stem giveaway; longest-option cue (62 of 91 four-option MCQ/numerical items) |
| Minor | about 45 questions | listed below |
| No problem found | about 75 | |

- **Keys.** No wrong key found. Every question has exactly one defensible answer.
- **Numericals.** All 8 recomputed and correct (table under Verified facts). The distractors are the usual slips: ×10, hours used for seconds, n left out, ÷2.
- **Data integrity.** All 79 fact IDs exist and all are used. No duplicate IDs. Answer positions are balanced (32/31/31/31).
- **Known source issues.** No question uses the board's ml quantities (#19) or "Cu(CN)₂"/"Na₂PO₄" (#21). The only question on the copper current is ELP-0052, which states "about 5–8 A" in its key (#20 says questions avoid the range). The key is still right under both sources ("a few amperes").

## Critical

| ID | Problem | Suggested fix |
|---|---|---|
| none | | |

## Major

| ID | Problem | Suggested fix |
|---|---|---|
| ELP-0104 (also 0100) | On `electroplating/cell`, the G ("Tank") anchor (140,410 in the SVG) sits **inside the electrolyte fill** (rect 122–638 × 230–418), about 20 px from the wall. So both G and C ("Electrolyte") point into the liquid. 0104 can be answered only by elimination (no "Electrolyte" option). 0100 offers both "Tank" and "Electrolyte". The figure teaches the wrong mapping. | Move G's anchor onto the tank wall above the liquid line, e.g. (120,205), or onto the outer bottom edge (380,421). Re-render. |
| ELP-0121 | The stem "Why is the workpiece (A) connected to the + terminal?" gives away ELP-0122 (A = workpiece made the anode) and ELP-0034 (job = anode) if they appear in the same quiz. | Reword to "In the figure, which electrode is the workpiece, and why is it connected that way?", or ask "What is released at A, and why?" |
| Bank-wide | Longest-option cue. In 62 of 91 four-option MCQ/numerical items (68%; chance ≈ 25%), the key is uniquely the longest. Worst (key ≥ 2× the next longest): 0027, 0031, 0033, 0042, 0048, 0058, 0059, 0066, 0069 (3.1×), 0082, 0084, 0092. Full list: 0001, 0003, 0004, 0005, 0006, 0009, 0010, 0011, 0013, 0015, 0016, 0025, 0026, 0027, 0028, 0029, 0030, 0031, 0033, 0036, 0037, 0039, 0040, 0041, 0042, 0044, 0045, 0046, 0047, 0048, 0049, 0051, 0052, 0053, 0054, 0056, 0057, 0058, 0059, 0062, 0063, 0066, 0067, 0068, 0069, 0072, 0075, 0076, 0077, 0078, 0079, 0080, 0081, 0082, 0083, 0084, 0086, 0088, 0089, 0090, 0091, 0092. | Lengthen the distractors to match the key's length and detail, or trim the keys. Do the worst 12 first. ELP-0016 is a special case: only the key carries a units qualifier "(I in A, t in hours)". Put the units in the stem. |

## Minor

| ID | Problem | Suggested fix |
|---|---|---|
| ELP-0052 | The key states "about 5–8 A" (log sheet). The board says 6–8 A, and corrections #20 says no question uses the range. The ref says "blackboard", but the range is from the log sheet. | Key: "A few amperes (single digits)", or ref "Log Sheet; board 6–8 A". |
| ELP-0018 | Uses 5 A for copper. That is only on the log sheet (the board says 6–8 A), but the ref cites only the board. The key is computed from the given values, so it is unaffected. | Ref → "Electroplating Log Sheet". Or use 6 A (key ≈ 0.059 g). |
| ELP-0021 | The ref cites the board for 5 A, but the board writes "5 A/sq ft" (a current density). The 5 A is from the log sheet. | Ref → "Electroplating Log Sheet". |
| ELP-0025 | Ref "Electroplating blackboard". The board says nothing about burnt deposits. | Ref → "Theory: Dini". |
| ELP-0088 | Ref lecture p.4. The slide gives "better adhesion" only; peeling and blistering are theory. Category "definitions" → defects. | Ref add "Theory: Dini". Category → advantages-limitations or process-parameters. |
| ELP-0089 | Category "definitions", but it asks about a defect's cause. | Category → process-parameters. |
| ELP-0065 | The explanation says "Dielectric fluid is used in wire EDM". It is used in EDM in general (0008 says EDM). | "…used in EDM". |
| ELP-0008, 0010, 0030, 0065, 0099, 0100 | "Dielectric" distractors appear in 6 items. Students learn that "dielectric" is always wrong. 0008 and 0065 both have "Dielectric fluid" as the NOT answer. | Vary them: e.g. "Grinding coolant", "Flux", "Quenching oil". |
| ELP-0027 | Distractor "Hacksaw and file": a file does remove burrs, so it is half-defensible as mechanical cleaning. | Replace with "Hacksaw and scriber". |
| ELP-0004 | Silly distractors: "A block of rubber", "A glass rod". | Use "A carbon/graphite rod", "The tank wall". |
| ELP-0033 | "Only mechanical cleaning" cannot be a type of chemical cleaning. | Use "Only pickling in dilute acid". |
| ELP-0039 | "No current at all, for 1 day" and "230 V AC, 1 hour" are silly. | Use the copper/nickel values (2–6 V, 25–30 s; 1.5–3 V, 5–7 min). |
| ELP-0074 | Option 1 ends "rinsing → rinsing → rinsing". The key is the only option that starts with degreasing and ends with drying. Labelled hard. | Use plausible permutations (e.g. swap pickling and degreasing). Difficulty → easy/medium. |
| ELP-0073 | Labelled hard, but every distractor starts with plating or polishing. | Use near-miss orders (e.g. chemical cleaning before polishing; no wash after copper). |
| ELP-0075, 0077, 0078, 0080, 0081, 0082, 0083, 0084, 0085, 0086 | Silly distractors: "Wear sandals for comfort", "Wear loose sleeves", "Switch the supply to AC for safety", "Lean over the tank", "Taste the bath", "Cyanide is radioactive/magnetic", "No health effects", "No protection is needed", "A heater", "always liquid". | Replace with plausible but wrong precautions (e.g. "cotton gloves are enough", "a ceiling fan is adequate ventilation", "cyanide dust forms only in nickel baths"). |
| ELP-0057, 0061, 0093, 0099, 0116 | Weak distractors: "Main source of copper" (Ni bath), "None of it"/"Only the threads", non-metals offered for "which metal is plated", "Dielectric nozzle", "Nickel stripping". | Replace with on-topic options. |
| ELP-0031, 0038, 0079, 0111, 0041 | Labelled hard but easy: "Vitrified grinding wheel", "Nickel sulphate" in the cleaning bath, "No limit is needed", non-electrode letters as distractors. | Difficulty → easy/medium. |
| ELP-0036, 0037, 0038, 0046–0049, 0055–0058, 0062 | Category "workpiece-material" for bath and cleaning chemistry. It is not the job material. | Category → process-parameters (or a bath-chemistry category if the schema allows one). |
| ELP-0014, 0016 | 0014 (formula) is "definitions" and 0016 (1.185 factor) is "process-parameters". | Category → principle-theory or numericals. |
| ELP-0122, 0124 | Part-ID questions labelled "principle-theory". | Category → machine-parts. |
| ELP-0003 / 0109 / 0094 / 0099 / 0106 | Workpiece = cathode is asked 5 times; 0003 and 0109 are near-identical. | Drop 0109, or ask about the ion direction instead. |
| ELP-0007 / 0096 / 0095(R) | DC not AC is asked 3 times. | Drop 0096. |
| ELP-0034 / 0121 / 0122 / 0095(A) | Electro-cleaning anode is asked 4 times. | Keep 0034 and 0122. Reword 0121 (see Major). |
| ELP-0011 / 0012 | Both ask that the deposit depends on I × t. | Drop one, or make 0012 ask what the 96,500 C constant represents. |
| ELP-0008 / 0065 | Both are NOT questions keyed "Dielectric fluid". | Change one key (e.g. 0065 → "Hacksaw"). |
| ELP-0114/0118, 0116/0119, 0117/0120 | "What is step X" vs "which box is X" are mirror pairs on the same figure (9 process-flow items in all). | Keep one of each pair in any one quiz. |
| ELP-0018, 0021, 0045, 0094, 0097 | Stems cue other items: 0018 gives "30 s" (→0051), 0021 gives "6 minutes" (→0060), 0045 gives "copper before nickel" (→0070), 0094-A gives workpiece = cathode (→0003), 0097 gives the Cu/Ni time order. | Exclude co-occurrence in one quiz, or neutralise the stems. |
| ELP-0102, 0103 | The meter glyphs "A" and "V" in the figure give away Ammeter/Voltmeter. Also, the ammeter glyph "A" can be confused with label bubble A (anode) in 0098, 0105 and 0111. | Accept as easy, or replace the glyphs with plain circles and keep the meter symbols in the legend only. At least make sure label letters are not reused inside symbols. |

## Figures

| Figure | Check | Result |
|---|---|---|
| `electroplating/cell` | Polarity | Correct. The left electrode A goes via the ammeter to **+**; the right electrode B (workpiece) goes to **−**. |
| | Ion direction | Correct. The M⁺ arrows run anode → workpiece (cathode). |
| | Meters | The ammeter is in series on the + lead (correct). The voltmeter is across the DC output terminals, not the cell leads. That is acceptable (the ammeter drop is negligible), but strictly it reads source voltage. Optional: move the V leads onto the anode/cathode wires after the ammeter. |
| | Anchors | A, B, D, E and F are on the right parts. C is in the liquid (correct). **G is in the liquid, not on the tank** (Major, above). |
| `electroplating/process-flow` | Blank boxes | All 6 boxes are blank, with letters only. The title and alt text give nothing away. |
| | Sequence | 6 boxes (mechanical → polishing → chemical → wash → Cu → Ni) omit the **wash after copper**. ELP-0073 (7 steps) and ELP-0071 both include it. No key conflicts. Optional: add an unlettered "wash" arrow note, or a 7th box. |
| `electroplating/electrocleaning` | Polarity | Correct. Workpiece A goes to **+** (anode), with bubbles (O₂, label B) on A. C goes to **−**. |
| | Realism | No H₂ bubbles are drawn on the cathode C, where H₂ would form (twice the gas volume). Harmless. Optional: add small bubbles at C, unlabelled. |
| `electroplating/buffing` | Anchors | A is on the left cloth wheel, B on the compound bar, C on the motor. All correct. |
| | Drawing | The wheels are drawn face-on (concentric rings) while the motor is side-on, with the spindle line passing through the wheel faces. That is a mixed projection. The compound bar floats in space, away from the wheel. Optional: draw the wheels edge-on (as on the log-sheet sketch) and hold the bar against the wheel rim. The title "Buffing (polishing) machine" hints at ELP-0125. |

## Verified facts

**Numericals (F = 96,500; Cu 63.5/2; Ni 58.69/2)**

| ID | Recomputed | Key |
|---|---|---|
| factor Cu | 63.5 × 3600 / 193,000 = 1.1845 g/(A·h) | 1.185 ✓ |
| factor Ni | 58.69 × 3600 / 193,000 = 1.0947 g/(A·h) | 1.095 ✓ |
| 0017 | 1.185 × 2 × 3 = 7.11 g | ✓ |
| 0018 | 1.185 × 5 × (30/3600) = 0.0494 g (MIt/nF: 63.5 × 150 / 193,000 = 0.0493) | 0.049 ✓; 177.8 = 30 h ✓ |
| 0019 | 63.5 × 2 × 965 / 193,000 = 0.635 g | ✓; 1.27 = n omitted ✓ |
| 0020 | 1 × 193,000 / (63.5 × 2) = 1520 s = 25.3 min | ≈ 25 min ✓; 12.7 min = n omitted ✓ |
| 0021 | 1.095 × 5 × 0.1 = 0.548 g | 0.55 ✓; 32.9 = 6 h ✓ |
| 0022 | Q = 2 × 30 = 60 C | ✓ |
| 0023 | Z = 63.5 / 193,000 = 3.29 × 10⁻⁴ g/C | ✓; 6.58 × 10⁻⁴ = n omitted ✓ |
| 0024 | 0.635 / 8.96 = 0.0709 cm³; / 10 cm² = 7.09 × 10⁻³ cm = 70.9 µm | ≈ 71 µm ✓ |

**Lab facts (board, log sheet)**

- Order: mechanical cleaning (emery + cotton-mop polishing) → chemical cleaning → wash with water + pumice → copper plating until red → wash → half the job in nickel. The log sheet matches; the board lists the same sections in the same order. ✓ (0068–0073)
- Copper: 2–6 V, 25–30 s (board and log), until reddish (log). Current is 6–8 A on the board and 5–8 A on the log. ✓ (0050, 0051, 0053)
- Nickel: 1.5–3 V, 5–7 min (board and log); "5 ampere" (log) versus "5 A/sq ft" (board, a current density); half the job (log). ✓ (0060, 0061). Note: F049 treats 5 A and 5 A/sq ft as the same, but they are different quantities. No key is affected.
- Chemical cleaning: 6 V, 10–15 A, 5 min (board); then water + pumice (board item J, log step ii). The bath is Na₂CO₃, NaOH, "Na₂PO₄" (= Na₃PO₄), NaCN, Na₂SiO₃, water. ✓ (0038–0040)
- Tools: mild-steel workpiece, emery paper, polishing machine, pumice powder, electroplating solution, wire. ✓ (0064, 0065)
- Precautions (log): proper shoes and apron; handle the job with care while cleaning and polishing; operate the machines with caution; keep an appropriate distance. ✓ (0075–0077)
- Nickel bath on the board: nickel salts (three, names partly illegible), boric acid, water. ✓ (0062)

**Lecture facts (slides)**

- p.2: thin metal layer on a conducting substrate; electrolysis; substrate = cathode, plating metal = anode; m ∝ quantity of electricity; 96,500 C per gram-equivalent; "for copper 1.185 I×t". The slide does not state hours (that is derived), and the nickel factor is hidden by the webcam. ✓
- p.3: cell = variable DC source, high-capacity conductors, current/voltage meters, cathode = work, anode = plating metal, electrolyte (bath) in a tank. ✓
- p.4: cleaning for adhesion, smoothness and appearance; mechanical cleaning (metal abrasive brush, emery paper); buffing with emery compound; chemical cleaning is "more specifically electrochemical". ✓
- p.5: buffing = rubbing against a rotating cloth wheel impregnated with fine abrasive; binders are fat, greaseless wax and soap. ✓
- p.6: electro-cleaning is the reverse of plating, with the work as anode; 4OH⁻ → 2H₂O + O₂ + 4e⁻; the O₂ removes rust. Na₂CO₃; Na₂SiO₃ protects Al against soda; TSP removes grease. ✓
- p.7: Cu gives a corrosion-resistant coat and a base for other plating; acid or cyanide bath, with cyanide popular; plates steel, Zn, Al, Mg, Ni and Pb; good adhesion and decorative finish; protects the base metal from acid attack in later Ni plating; cyanide is highly poisonous for use and disposal. ✓
- p.8: CuCN is insoluble, so NaCN/KCN forms soluble complexes; excess cyanide gives good deposits and anode corrosion; NaOH/KOH increases conductivity, reduces attack on steel anode containers and reduces cyanide decomposition; Rochelle salt gives a fine grain; Na₂CO₃/K₂CO₃ improve conductivity; carbonate builds up and lime removes it. ✓
- p.9: copper dust is dangerous; cyanide limit 5 mg/m³ over an 8-h shift; dust forms when handling salts, making additions or making up new solutions; don't touch the solution, rinse parts and wash hands. ✓
- p.10: Ni gives wear, heat and corrosion resistance and a bright finish; NiSO₄ is the primary Ni source; NiCl₂ increases conductivity and anode dissolution; H₂SO₄ is added because H⁺ is lost as H₂; boric acid controls pH; brighteners and anti-pitting agents; anodes are Ni lumps or pieces in a Ti basket. ✓
- p.11: dermatitis, lungs on long-term inhalation; protective clothing, eye protection and gloves are mandatory; local exhaust; care during bath make-up and maintenance; no smoking, eating or drinking. ✓
- p.12: wheel types are spiral sewn, loose, concentric sewn and flannel; compound comes as solid bars (alumina, SiC, FeO, CrO in fatty acid, greaseless wax or soap); pressure is applied by hand, with more pressure faster but wasteful and low pressure finer. ✓

---
## Fixes applied by the author (round 1)
- Cell figure: the Tank (G) anchor is moved onto the tank wall above the liquid. The "A"/"V" letters are removed from the meter circles, so the ammeter/voltmeter questions test series vs parallel connection.
- ELP-0121: the stem no longer states the polarity.
- ELP-0016: every option now carries the same units.
- All "dielectric" distractors are replaced (ELP-0008, 0010, 0030, 0065, 0099/0100).
- The silly sequence distractor ("rinsing → rinsing → rinsing") and other silly distractors are replaced.
- Process flow now has 7 boxes, including the wash after copper plating.
- Bath-chemistry questions are recategorised from workpiece-material to principle-theory, and the defect questions to principle-theory.
- Difficulty lowered on 0031, 0041, 0073, 0074, 0079 and 0111.
- Option-length balancing: about 50 questions (authoring/fix_electroplating.py).
