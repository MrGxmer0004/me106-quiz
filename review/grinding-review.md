# Grinding question bank: independent review

Reviewed file: `src/data/questions/grinding.json`, 200 questions (GRD-0001 to GRD-0200).
I also checked `knowledge/grinding.md`, `corrections.md` #7, #8, #16, #17 and #18, the 7 `grinding/*` entries in `src/data/figures.json`, all 7 PNGs in `.render/grinding/` (plus the SVG sources and `scripts/figures/fig_grinding.py` for anchor coordinates), and every source listed under "Verified lab facts". I recomputed all 4 numericals.

## Summary

| Severity | Count | IDs |
|---|---|---|
| Critical | 1 | GRD-0153 |
| Major | 10 items (14 questions, plus one bank-wide pattern) | GRD-0139, 0152, 0163, 0165, 0172, 0085, 0188, 0186, 0114, 0120, 0118/0196, 0177/0180; longest-option cue across the bank |
| Minor | about 45 questions | listed below |
| No problem found | about 140 | |

- **Keys.** I found no wrong answer key in any text question. All 4 numericals are correct (0018 = 20; 0019 ≈ 31.8, so "≈ 32"; 0020 = 1600 mm³; 0024 = 3 kW). The distractors in the numericals are the expected slips: the inverse ratio, a factor of 10, and leaving out π/4 (which gives 25.0).
- **Boundary values.** The only grade letters used in keys are E, K and T. The only grit numbers used in keys are 24, 46, 60, 180 and 400. The only structure numbers used in keys are 3 and 12. Every one of these falls in the same class in all four scales (NB, GP, GPPT, CG). The one caveat is T: CG calls it "very hard", and the key "Hard" is still right. No key depends on a disputed value.
- **Data integrity.** All fact IDs exist, and all 113 facts are used. Every diagram key matches its registry label. Answer positions are balanced (51/52/48/49).
- **Main problems.** (a) In two figures, labels point at the wrong part or at a part that cannot be told apart (surface-grinder B and H/I, cylindrical-grinder H). (b) In 91 of the 146 non-diagram 4-option questions (62%), the correct option is clearly the longest. (c) There are several exact duplicates. (d) Some questions are framed on the notebook while the notebook says something different.
- **corrections.md #18 is inaccurate.** It lists the grit disagreements as "24/30, 60/80, 180–240". The real disagreement is with CG, whose classes are coarse ≤ 36, medium 46–120, fine 150–280 and very fine 320–600. The disputed ranges are therefore about 30–36, 80–120 and 200–280. No key is affected, but #18 and facts F066 ("85 fine") and F067 ("32 medium") should be updated: in CG, 85 is medium and 32 is coarse.

## Critical

| ID | Problem | Suggested fix |
|---|---|---|
| GRD-0153 | The figure contradicts the key. On `grinding/surface-grinder`, the leader for label B ends at (300,168). That point is inside the wheel (centre (330,210), r = 55, distance 51.6), so the dot sits on the wheel face among the grit dots, not on the guard arc. The question asks for B's function, and option 3 ("Rotating abrasive wheel that removes small amounts of metal") is the wheel's function. A student who reads the figure literally picks option 3 and is marked wrong. | Move B's anchor onto the guard arc, outside the wheel (for example (300,152), r ≈ 65 from the centre). Re-render. |

## Major

| ID | Problem | Suggested fix |
|---|---|---|
| GRD-0139 | Same B-anchor fault as 0153. The question can be answered by elimination only because "Grinding wheel" is not an option. | Same fix as 0153. |
| GRD-0152 | You cannot tell the handwheels apart. H and I are identical plain circles at the same height, and nothing shows which one drives the table and which drives the cross slide. Both H and I are offered as options, so the answer is a 50/50 guess. (0145 and 0146 are answerable only because each offers a single handwheel.) | Add motion arrows: a ↔ arrow beside H along the table, and an in/out ⊙ symbol at I on the saddle. Or drop the "which label shows the cross-feed handwheel" question. |
| GRD-0163, GRD-0165 | Label H on `grinding/cylindrical-grinder` (adjustable table dog) is drawn as black blocks on the upper table, inside the headstock and tailstock footprints. They look like clamp bolts or feet. The notebook sketch (NB p.10) has the dogs on the front of the **lower** (reciprocating) table, near the ends. The H bubble also overlaps the headstock. | Redraw both dogs on the front face of the lower table G near its ends, with a reversing lever on the base between them. |
| GRD-0172 | Ambiguous. "Work NOT held between centres or in a chuck": panel A (surface grinding) shows a block lying on a plain table with no chuck drawn, so A is defensible. Panel C's chuck is not drawn either. | Reword to "Which panel shows the work supported on a rest blade and driven by a second (regulating) wheel?" |
| GRD-0085 | The question is framed as "In the notebook example C 32 _ 8 B". But NB p.7 writes "C → Carbide", with arrows to both "silica carbide" and "cubic boron nitride" (corrections #7). On the notebook's own terms, distractor 0 "CBN and resinoid" is defensible. Also, NB p.8 does give the grade, written as "Hard grade" (letter looks like Y), so the "illegible" note in F067 overstates it. | Drop the "notebook" framing (ask "Decode C 32 Y 8 B: abrasive and bond?"), or replace the CBN distractor. Add "(the notebook's C → CBN is wrong, corrections #7)" to the explanation. |
| GRD-0188 (and 0186) | Possible giveaway. The registry/SVG `<title>` is "Dressing a grinding wheel", which shows as a tooltip if the SVG is inlined or as a caption if the title is shown, and that is the answer to 0188. The aria-label names a "single-point diamond dresser", which is the answer to 0186. The renderer is not in this repo, so I could not confirm whether either is shown. | Make sure the quiz UI shows neither the title nor the alt text for diagram questions, or neutralise them ("Figure G-6"). |
| GRD-0114, GRD-0120 | Sequence questions where the key is the only complete chain: 6 steps in 0114 and 7 in 0120, against 4–5 in each distractor. The key is also about twice as long. You can answer by length alone. | Give all options the same number of steps, using the same step set in different orders. |
| GRD-0118 / GRD-0196 | Exact duplicates: same fact (F095), same answer (outside micrometer after the trial cut). | Delete 0196, or turn it into a question on the Vernier caliper from the tool list. |
| GRD-0177 / GRD-0180 | Exact duplicate: both ask what position 4 ("5") of A 46 K 5 V means, and the answer is structure. | Delete 0180, or ask "is structure 5 dense or open?" (dense in GP/GPPT, "regular" in CG; avoid it, or use 3 or 12). |
| Bank-wide | Longest-option cue. In 91 of 146 non-diagram 4-option items (62%, against about 25% by chance), the key is uniquely the longest option. The worst cases (key ≥ 1.6× the next longest) are 0041, 0097, 0115, 0180 and 0194. Others include 0011, 0023, 0037, 0043, 0049, 0070, 0076, 0081, 0093, 0094, 0095, 0101, 0102, 0103, 0107, 0111, 0113, 0119, 0126 and 0130. | Lengthen the distractors so they match the key's length and specificity, or trim the keys. Do 0041, 0097, 0115, 0180, 0194, 0114 and 0120 first. |

## Minor

| ID | Problem | Suggested fix |
|---|---|---|
| GRD-0074 | The explanation says "Low structure numbers are dense in all sources", which is false: the notebook (NB p.8) says 0–7 is **open**. A notebook-trained student will choose "Open wheel". The key is right (GP, GPPT and CG agree). | Explanation: "dense in GP, GPPT and CG; the notebook has this reversed (corrections #8)". Do the same for 0075 and 0133. |
| GRD-0051 | NB p.7 maps C to SiC **and** CBN, and "Cubic boron nitride" is a distractor. The explanation already flags this, so it is fine. | None needed beyond citing corrections #7. |
| GRD-0084 | The explanation says "85 is a fine grit". In CG, 80 and 100 are **medium**. The key is not affected. | Delete that clause, or say "fine in NB/GP/GPPT". |
| GRD-0067 | The key "Hard" is right, but CG classes T as "very hard" (S–Z). | Add "(CG: very hard)" to the explanation. |
| GRD-0177, 0180; figure `wheel-marking` label 4 | "5 = fairly dense structure". GP and GPPT call 5 dense, CG calls it "regular" (5–7). | Change to "5 = structure number (low = dense)". |
| GRD-0007 | Option "Melting and solidification only": fusion welding does involve melting and solidification. The word "only" is the only thing that makes it wrong. The welding example is in NB p.5, not GL p.1. | Replace that distractor with "Forming". Set the ref to Manufacturing notes p.5. |
| GRD-0168 | Distractor "Creep-feed grinding" is a type of surface grinding, and panel A shows it just as well. | Replace it with "Internal grinding". |
| GRD-0188 | Distractor "Surface grinding a block": the dresser holder C is drawn as a rectangular bar under the wheel and looks like a workpiece. | Draw the holder as a slim shank angled at about 10–15°, or replace the distractor. |
| GRD-0148 | K's anchor (330,266) is exactly at the wheel–work contact, on the wheel's bottom rim. The wheel (bottom y = 265) also overlaps the work (top y = 258). | Move the anchor to about (360,272) inside the block. Lift the wheel so it is tangent to the work. |
| GRD-0145, 0146 | The same H/I issue as 0152. Each is answerable only because a single handwheel is offered, but the label-to-name mapping can't be learned from the figure. | Fix the figure (see 0152). |
| GRD-0184 | Only 2 options (A/B), and labelled hard. | Make it easy, or add options (glazed, loaded, either). |
| GRD-0071 | Labelled hard, but it is trivial: "Colour of the wheel". | Make it easy, or use a plausible distractor such as "Bond type symbol" or "Wheel diameter". |
| GRD-0185, 0186, 0187 | Category "wheel-specification", but they are about dressing tools. | Category → tools-equipment. |
| GRD-0168 to 0173 | Category "machine-parts", but they ask about grinding operations or types. | Category → operations. |
| GRD-0103 | Category "job-dimensions", but it asks about objectives. No dimensions are involved. | Category → procedure (or objectives). |
| GRD-0054 | The ref is CG p.3, but CG says SiC is for "non-ferrous metals" only. Cast iron comes from GPPT s.14 and NB p.7. | Ref → Grinding PPT s.14. |
| GRD-0083 | Ref "Grinding slides p.5" is the centreless slide and says nothing about cut-off wheels. | Ref → Theory: Hajra Choudhury (CG p.1 mentions resin-bonded billet wheels). |
| GRD-0126 | The explanation cites LS p.7 for "stand to one side". LS says only "maintain a proper distance". | Add "Theory: Hajra Choudhury" for the "one side" part. |
| GRD-0112, 0113, 0114, 0118, 0119 | The step numbers in the explanations follow the KB's merged list, not the log sheet. LS p.8 has 8 steps in each procedure. Coolant is step 7, demagnetise is step 8, the trial cut is step 5 and dressing is step 6. | Renumber the explanations to match LS, or drop the step numbers. |
| GRD-0118/0196, 0109/0197, 0192/0200, 0174/0179, 0066/0181, 0068/0069/0070/0132, 0064/0135, 0090/0091, 0099/0100/0134, 0111/0127 | Near-duplicates: same fact and same answer. | Keep one of each pair for any single sitting, or tag them so the quiz never draws both. |
| GRD-0079 | Distractor "Bakelite-free rubber" is a made-up term, and Bakelite *is* a resinoid bond, so it confuses the point being tested. | Replace it with "Shellac". |
| GRD-0022, 0046, 0077, 0081, 0091, 0095, 0100, 0110, 0112, 0116, 0122, 0124, 0128, 0193, 0196, 0199 | Silly distractors, for example "Anode, cathode and electrolyte", "Laser", "Dielectric pump", "Hung on a wire", "Cover the wheel with it", "With the guard fitted", "Molten wax", "Hammer the flange" and "Dial-less caliper". | Replace them with plausible confusions (other grinder parts, other bond/abrasive names, other lab steps). |
| GRD-0198 | A pedestal/bench grinder is not part of the ME-106 grinding job (surface and cylindrical only). The theory is correct (≤ 3 mm). | Optional: tag it "theory / out-of-lab". |

## Figures

| Figure | Finding | Severity |
|---|---|---|
| `grinding/surface-grinder` B | The anchor is on the wheel face, not the guard (see 0153). | Critical |
| `grinding/surface-grinder` H, I | Two identical handwheels with no motion cue. A third handwheel, on the column (down-feed), has no label. | Major |
| `grinding/surface-grinder` K | The anchor is at the wheel–work contact, and the wheel overlaps the work by 7 px. The saddle and handwheels float above the base, unsupported. | Minor |
| `grinding/surface-grinder` other labels | A wheel, C wheel head, D column, E magnetic chuck (hatched), F table (↔ arrow), G saddle and J base all point correctly. | OK |
| `grinding/cylindrical-grinder` H | The dogs are drawn as blocks inside the headstock and tailstock footprints on the upper table. NB p.10 has them on the front of the lower table. | Major |
| `grinding/cylindrical-grinder` other labels | A wheel head, B wheel, C headstock (left, with rotation arrow), D tailstock, E work between centres, F upper table, G lower table (↔ arrow, matching the NB "table movement" arrow) and I base are correct. The wheel does not touch the work (7 px gap). | Minor |
| `grinding/types` | A surface, B external cylindrical, C internal and D centreless (blade plus a separate regulating wheel) are all correct. In C and D the wheels do not touch the work (7–9 px gaps). Panel A could also be read as creep-feed (see 0168). Nothing gives away the answers. | Minor |
| `grinding/wheel-marking` | The order A–46–K–5–V matches GP p.12 and CG p.2. Label 4's function says "fairly dense" (CG says "regular"). | Minor |
| `grinding/structure` | A is dense and B is open, which matches GP p.10, GPPT s.14 and CG. The alt text describes the packing but does not name the classes. | OK |
| `grinding/dressing` | A wheel, B diamond and C holder are correct. The diamond touches about 40° below centre with no drag angle, and the feed arrow is horizontal (radial). "Across the face" would be into the page in this view. The SVG title and alt text name the answer to 0188 and 0186. | Minor (title/alt: Major if shown) |
| `grinding/grinding-ratio` | Di (dashed new wheel), Df (worn wheel), d, l, b and G = Vw/Vs match the blackboard. The Δh dashed line is drawn across the top face (between the front and back top edges) rather than as the original top surface, so it reads as a line on the face. | Minor |
| Hidden text | I grepped all SVG `<text>`: only labels and dimension text. No part names are leaked in the figures. | OK |

## Verified lab facts

- **LS p.7 (log sheet).** Objectives: (1) surface finish on a plane surface with a surface grinder; (2) surface finish on a cylindrical surface with a cylindrical grinder. The job drawing shows the cylindrical job between centres, with the "dead center" at the tailstock end. Tools: chuck, mild-steel cylindrical rod, cubical piece, Vernier caliper, grinding wheel, coolant (water-based) and workpiece holder. Precautions: apron and leather shoes; no loose accessories (bracelets, chains); tie long hair back; material fixed tightly; keep a proper distance from the wheel and machine; check the wheel clears the work before starting. Questions 0103–0107, 0122–0127 and 0131 match.
- **LS p.8, surface grinding (8 steps).** Take the raw material → clear/clean the bed → magnetic parallels around the work → magnetic chuck on → wheel about an inch above the work → make sure the wheel is not in contact → adjust the wheels and start with coolant → wait for the wheel to stop, then demagnetise and remove. Questions 0108–0115 match (step numbers aside).
- **LS p.8, cylindrical grinding (8 steps).** Take the rough cylindrical stock → hold the job well centred → adjust the wheel position before starting → start the coolant → trial cut, then correct the size with an outside micrometer → dress the wheel for fine finish → finish the job → remove the work and switch off. Questions 0116–0121 and 0196 match.
- **NB p.5–10 (notebook).**
  - Value addition: forging/forming, metal addition (welding), melting and solidification (moulding), metal removal.
  - Bulk removal is semi-finishing; small removal (grinding) is finishing.
  - G = work volume removed / wheel wear.
  - Specific energy: 2–5 J/mm³ for machining, 15–50 J/mm³ for grinding.
  - Machine types: surface, cylindrical, internal. Marking order: abrasive–grain–grade–structure–bond.
  - Grit: 10–30 coarse, 30–80 medium, 80–200 fine, 200–600 very fine. Grade: A–H soft (for hard work), I–P medium, Q–Z hard (for soft work).
  - Structure is **reversed** (0–7 open), as corrections #8 notes.
  - Bonds V/B/R. Example A 85 I 5 V. Example C 32 (Y) 8 B is "hard grade".
  - Dressing removes the outer layer. A blunt wheel shows glazing, is shiny and smooth, and self-sharpens.
  - Advantages: finish, accuracy, hard materials. Disadvantages: cost, high specific energy, coolant needed.
  - Cylindrical grinder sketch: headstock, work, wheel, tailstock, upper and lower tables, adjustable dogs on the lower table, base.
- **Grinding Ratio.jpg (blackboard).** GR = Vw/Vs; Vw = l·b·Δh; Vs = (π/4)·d·(Di² − Df²). Questions 0015, 0016, 0019 and 0020 match.
- **CG (pdftotext).**
  - SRG vs FFG. In SRG the wheel self-sharpens, so dressing is unnecessary. Vertical-spindle grinding uses the wheel face. Speeds are ≥ 30 m/s and grain hardness > 2000 kg/mm².
  - Marking A 46 K 8 V (CG calls 8 "open"). Size is diameter × thickness × bore. Abrasive symbols: A/C/D/B(CBN).
  - Grit: coarse 8–36, medium 46–120, fine 150–280, very fine 320–600. Grade: soft E–I, medium J–M, hard N–R, very hard S–Z. Structure: 1–4 small, 5–7 regular, 8–10 large, 11–14 very large.
  - Alumina for ferrous/high-tensile; SiC for non-ferrous; diamond for ceramics/polishing.
  - Plain grinder is lathe-like, with traverse and plunge. The universal grinder swivels and has an internal attachment. Centreless: blade, slow regulating wheel, inclined for through-feed. Tool-post grinder.
- **GP (Grinding pdf.pdf).**
  - p.2 classification (surface; cylindrical OD/ID; centreless for long slender rods). p.3 reciprocating/rotary table × horizontal/vertical spindle. p.4 hydraulic table carrying headstock and tailstock.
  - p.5 regulating wheel rubber-bonded, both wheels rotating in the **same direction**, tilted for through-feed.
  - p.7 CBN for very hard materials. p.8 grit: coarse 10–24, medium 30–60, fine 80–180, very fine 220–600. p.9 grade A–H / I–P / Q–Z, with the selection factors. p.10 structure: dense 1–8, open 9–15; open for rough work and soft materials, dense for hard/brittle. p.11 bonds V/S/E/B/R/O. p.12 A 46 K 5 V.
- **GL (Grinding Lab.pdf).** p.1 the four value-addition groups. p.2 the metal-removal list. p.3 surface/cylindrical/internal. p.4 surface grinder parts (column, wheel, wheel head, table, saddle, base). p.7 machining → heat treatment → grinding. p.8 advantages. p.9 51 A 60 K 5 V 05 (manufacturer's abrasive mark and identifier).
- **GPPT.**
  - s.2 precautions (shoes, apron, attentive, no ornaments/watches, supervision). s.5 definition. s.7 reasons. s.8 applications, including turbine blades and landing gear.
  - s.9 surface grinding (table reciprocates, wheel moves down; beds, gauges, dies). s.10 cylindrical (between centres or chuck; wheel fast, work slow; shafts, rollers, bearings). s.11 centreless (regulating wheel slower; rest blade). s.12 tool-and-cutter.
  - s.13 grains, bond, structure, pores. s.14 A for steel, C for cast iron/non-ferrous; grit coarse 10–24, medium 30–60, fine 80–220, very fine 240+; grade A–H / I–P / Q–Z; structure dense 1–7, open 8–14; bonds V/B/R.
  - s.15 balancing. s.16 defects (burn, chatter, glazing, finish, cracks). s.17 truing and dressing.
- **Theory checks passed:**
  - Glazing comes from too hard a grade, loading from soft ductile work with too dense a wheel. Dressing sharpens the wheel; truing restores its geometry.
  - Soft grade for hard work. Vitrified is the most common bond. Resinoid/rubber for cut-off wheels; rubber for regulating wheels. CBN, not diamond, for hardened steel.
  - Centreless wheels rotate in the same direction, with the regulating wheel slower and tilted.
  - Magnetic chucks hold only ferromagnetic work. Ring test. Blotters. Work rest at ≤ 3 mm.

---
## Fixes applied by the author (round 1)
Note: question IDs after GRD-0117 shifted, because two exact duplicates were removed (the outside-micrometer tool question and the custom "position 4" figure question) along with the cross-feed handwheel label questions.
- GRD-0153/0139 (critical): label B now anchors on the guard arc. The wheel is moved up so it just touches the work (no overlap).
- GRD-0152/0145/0146: the cross-feed handwheel callout (I) is removed from the surface-grinder figure, so H (table traverse) is unambiguous.
- Cylindrical grinder: the table dogs now sit on the front of the lower table near its ends, and the wheel touches the work. Types panel B: the wheel touches the work.
- Grinding-ratio figure: the block is drawn at its ground height, with the original top dashed above it, so Δh is the gap.
- GRD-0172: reworded to "work resting on a blade and controlled by a regulating wheel".
- GRD-0085: distractor "CBN and resinoid" replaced with "Diamond and resinoid". GRD-F067 text notes that the notebook calls it a hard grade.
- GRD-0074 and GRD-0084 explanations corrected.
- corrections.md #18 rewritten with the actual conflicting ranges.
- Distractors "Creep-feed grinding" and "Surface grinding a block" replaced.
- All figures: SVG <title> removed and the aria-label made generic, so nothing in the SVG gives an answer away. The registry keeps title and alt for the gallery only.
- Option lengths: 69 questions rebalanced (authoring/fix_grinding.py).
