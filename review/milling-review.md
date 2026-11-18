# Milling question bank: independent review

Reviewed file: `src/data/questions/milling.json`, 252 questions (MIL-0001 to MIL-0252).
Also checked: `knowledge/milling.md` (131 facts), `corrections.md`, the 10 `milling/*` entries in `src/data/figures.json`, all 10 PNGs in `.render/milling/` (and their SVG sources for geometry), and every source listed under "Verified lab facts". I recomputed every numerical question and checked every indexing distractor for a second valid move.

## Summary

| Severity | Questions | IDs |
|---|---|---|
| Critical | 1 | MIL-0152 |
| Major | 6 | MIL-0027, 0091, 0113, 0190, 0199, 0207 |
| Minor only | 88 (34 of these only have the "correct option is clearly the longest" cue) | listed below |
| No problem found | 157 | |

Overall, the keys are sound. Every numerical answer is correct, and no indexing question has a second valid move among its options. All fact IDs exist, and all 131 facts are used. Each option list is unique, and answer positions are balanced (64/65/61/62). The main problems are: (a) one assertion–reason key that can be argued; (b) two questions that break the confirmed "working depth" rule or invite confusion with it; (c) one dividing-head leader line that points at nothing; (d) one cutter drawing that can be read as a distractor.

## Critical

| ID | Problem | Suggested fix |
|---|---|---|
| MIL-0152 | The A–R key can be argued. The key is "both true, R is NOT the explanation". But down milling gives a better finish precisely because the tooth enters at full chip thickness, with no rubbing or ploughing at a zero-thickness entry. TA s.8 says up milling is "rougher … due to rubbing at the start of cut". So R (chip maximum at the start) arguably *is* the explanation, and many students and teachers would pick option 0. The explanation's "no rubbing at the end of the cut" is also wrong: in down milling the chip thins to zero at the *end*. | Replace R with a statement that is true and clearly unrelated (e.g. "Down milling is also called climb milling"). Or drop the question. Fix the explanation either way. |

## Major

| ID | Problem | Suggested fix |
|---|---|---|
| MIL-0113 | This is a lab-job depth question, but option 1 "≈ 0.125 in" is 2/DP, and the explanation labels it "textbook working depth". KB MIL-F079 says lab-job questions "never offer 2/DP as a distractor". Putting it next to the lab's "working depth" invites exactly the confusion the rule exists to prevent. | Replace 0.125 in with ≈ 0.0723 in (≈ 1.8 mm, the dedendum). Remove "textbook working depth" from the explanation. |
| MIL-0091 | "Textbook working depth = 2/DP", with 2.157/DP as a distractor. The question is allowed as theory, but the lab teaches "W.D. = 2.157/DP" (board, both log sheets, notebook). A student who learned the lab name will pick option 2 and be marked wrong, and a student who memorises this key may answer a lab-set exam question wrong. This is the highest-risk question in the bank. | Either drop it, or avoid the term: "The sum of the addenda of two mating gears (2 × addendum) equals…" → 2/DP. Then 2.157/DP does not clash with the lab's name. |
| MIL-0027 | Stem: "several cutters (same or different) on one arbor … several surfaces at once" → Gang. Straddle (option 1) also fits: lecture s.12 defines straddle as "Two or more cutters are mounted on an arbor", and the notebook p.1 defines straddle as "use of various cutters of same type at once". Two of the course sources support straddle. | Make the stem specific: "cutters of different diameters/types … several different surfaces in one pass", or replace the Straddle distractor with Form milling. |
| MIL-0190 | Figure panel E (shank + wide toothed disc, side view) also looks like a shell face mill on its arbor, and "Face mill" is option 0. Two plausible answers. | Replace the "Face mill" distractor (e.g. with Slitting saw or Fly cutter). Or redraw E inside a T-slot with the narrow neck visible in the slot. |
| MIL-0199, MIL-0207 | In `dividing-head`, label B (Index crank) has its leader end at (110, 200), on blank plate surface up and left of the centre. The crank is drawn from (150, 230) to (209, 156), up and right, and lies under the orange sector-arm line (to 215, 148), so it is practically invisible. Students cannot see what B points to. | Draw the crank as a distinct thicker dark arm with a handle knob, at an angle away from both sector arms, and end B's leader on it. |

## Minor

| ID | Problem | Suggested fix |
|---|---|---|
| MIL-0014 | Distractor "maximum radial load on the arbor at entry" is half-supported by lecture s.7 ("down milling: less radial pressure on arbor"). It is false only because of "at entry". | Use a distractor that is plainly false, e.g. "It gives the best surface finish". |
| MIL-0049 | Explanation says "quill (lathe)". The quill is also a vertical-milling-machine part (MIL-F056; MIL-0063 key; vertical-mill label C). Also, a taper-shank end mill does have a tang. | Explanation: "quill (spindle sleeve of a vertical mill/lathe tailstock, not cutter nomenclature)". Replace Tang with e.g. "Clapper box" or "Rake of the grinding wheel". |
| MIL-0097 | "Spur and helical gears connect shafts that are…": crossed helical gears connect non-intersecting shafts at 90° (MIL-0104), which is option 2. "Parallel" is still the only option true for both, but it is easy to stumble on. | Stem: "Spur gears and (parallel-axis) helical gears…". |
| MIL-0121 | The explanation dismisses option 2 because "there is no 36-hole circle". The real reason is that 1/36 ≠ 1/9 (it would need 4 holes). Key and options are fine: 3/27 is valid but not offered. | Explanation: "1 hole on 36 = 1/36, not 1/9; the 18-hole circle needs 2 holes (or 3 on 27)." |
| MIL-0138 | "How many times is the work indexed to cut all the teeth?" can be argued as 21 (moves between 22 cuts). 21 is not offered, so the key stands. | "How many tooth spaces (divisions) are cut…" |
| MIL-0024 | Straddle is often described as a special case of gang milling, and Gang is a distractor. The stem's "two side cutters … two parallel faces" makes straddle the best answer. | Acceptable. Optionally swap Gang for Angular milling. |
| MIL-0018 | Ref "Milling lecture slide 5" does not mention backlash. Only TA s.8 does. KB MIL-F012 has the same mis-citation. | Ref: TA s.8. |
| MIL-0106, MIL-0126 | MIL-0106: the ref is LS p.9, but "from a circular workpiece" is from MLS1. MIL-0126: the ref is LS p.9, but chalk, file, bench vice, coolant and calipers are only on MLS1. | Add Milling Log Sheet #1 to the refs. |
| MIL-0125 | Explanation: "The catch pin locks the index crank". No source says what the "catch pin" is. | Soften: "(the index/latch pin)" or drop the sentence. |
| MIL-0239, MIL-0240, MIL-0242, MIL-0243, MIL-0245, MIL-0246 | `source: lab`, but the facts are theory (Machinery's Handbook / Hajra Choudhury). No lab source names a B&S cutter number or the touch-off method. | Set `source: theory`, or tag them as mixed. |
| MIL-0124 | Category `job-dimensions` (it is about work-holding). | `procedure` or `tools-equipment`. |
| MIL-0180 | Category `machine-parts` for "End mill". | `tools-equipment`. |
| MIL-0076, MIL-0120, MIL-0122, MIL-0139, MIL-0149, MIL-0252, MIL-0017 | Marked `hard`, but they are one-step questions or have silly distractors (24/6; 360/40; 40/40; "To cool the coolant"; "By hand, while the cutter runs"; "Is wet with dielectric"). | `easy` (0076, 0122, 0139, 0149, 0252) / `medium` (0120, 0017). |
| MIL-0002, 0005, 0012, 0130, 0135, 0139, 0140, 0144, 0145, 0245, 0250, 0252 | Silly or cross-shop give-away distractors: "Both reciprocate", "the table vibrates", "needs no cutting tool", "Zero throughout", "Dielectric filter", "Laser", "Dielectric pump", "Work barefoot", "Lunch breaks", "Switch on with wet hands", "Loosely held so the blank can slip", "Laser goggles", "Is wet with dielectric". | Replace them with plausible milling-shop alternatives. |
| MIL-0070 / MIL-0156; MIL-0107 / MIL-0157; MIL-0084 / MIL-0143 / MIL-0150; MIL-0149 / MIL-0248; MIL-0141 / MIL-0247; MIL-0047 / MIL-0191 / MIL-0192 | Near-duplicates (40 crank turns; aluminium blank; don't reverse the crank; chips/measure only when stopped; keep away from the cutter; involute cutter used in lab). | Keep one of each set, or make sure a quiz never draws two from the same set. |
| MIL-0219, MIL-0226 | Figure: the circular-pitch bracket F is drawn above the outside circle (tip to tip), not along the pitch circle. | Move bracket F onto the pitch circle (C). |
| MIL-0228, MIL-0229 | Figure: both helical gears in panel B have the same slope (lines rise to the right), and both herringbones in C have the same chevron. A meshing parallel-axis pair has opposite hands. | Mirror the lines on the right-hand gear in B (and C). |
| MIL-0230 | Figure: the bevel cone apices (≈(132, 305) and ≈(111, 322)) do not meet at the axis intersection (132, 322). | Redraw both cones with apex at the axis crossing. |
| MIL-0231 | Figure: the worm in E (a flat bar with slant lines) looks like the rack in F. | Draw the worm as a cylinder with a thread profile on the top/bottom edge and a centre line. |
| MIL-0197 | Figure: in gang panel B, the cutter and work outlines merge (same fill), so the separate cutters are hard to see. | Use a darker fill for the cutters, or a gap between cutter and work. |
| Longest-answer cue only (34) | The correct option is ≥ 1.4× as long as every distractor: MIL-0006, 0008, 0013, 0016, 0019, 0021, 0026, 0033, 0045, 0046, 0050, 0056, 0062, 0065, 0066, 0067, 0068, 0073, 0079, 0083, 0090, 0095, 0098, 0101, 0104, 0131, 0132, 0133, 0136, 0142, 0146, 0147, 0244, 0251. The cue is also present in 0005, 0018, 0047, 0084, 0106, 0124, 0138, 0139, 0143, 0145, 0243, 0245. | Lengthen the distractors to match. |
| KB / corrections.md | (1) Notebook p.1 defines straddle milling as "various cutters of same type at once" (wrong; this is closer to gang), and it is not in corrections.md. (2) MIL-F108 cites LS p.9 for coolant; LS p.9 does not mention coolant. (3) MIL-F056 cites LEC s.19 for "quill"; s.19 does not list a quill. (4) MIL-F012 backlash: LEC s.5 → TA s.8. | Add (1) to corrections.md. Fix the citations. |
| figures.json `milling/cutters` | `alt` says "Seven small line drawings", but there are six panels (A–F). | "Six small line drawings…". |

## Figures

- `up-down`: correct. Cutter clockwise: bottom teeth move left. Panel A, feed left → down milling. The tooth enters at the top of the full-height stock on the right (thick chip first), and the uncut stock (y = 186) is on the right, ahead of the cut. Panel B, feed right → up milling; the tooth enters at the bottom (zero chip), and the uncut stock is on the left. This matches lecture s.4/s.6. No chip is drawn (fine).
- `horizontal-mill`: all 11 leaders (A–K) land on the right parts. Labels match the facts.
- `vertical-mill`: all 9 leaders correct. D, E, G and H have no questions (fine).
- `cutters`: A–F identifications are correct. E can be read as a face mill (Major, MIL-0190). The registry alt says seven (Minor).
- `straddle-gang`: correct. In panel B the cutter outlines merge with the work (Minor).
- `dividing-head`: the worm wheel has exactly 40 teeth, and A and C–H are correct. B's leader points to empty plate, and the crank is hidden under a sector arm (Major, MIL-0199/0207). The views are mixed (wheel and plate face-on, but spindle and worm shaft drawn in-plane); this is acceptable as a schematic.
- `index-plate-33`: 33 holes. From the start hole clockwise to the end hole there are 27 spaces (26 intermediate holes). The arc runs clockwise. Correct.
- `index-plate-21`: 21 holes, 18 spaces clockwise. Correct.
- `gear-nomenclature`: A–H all correct (addendum 82 px < dedendum 93 px, ratio ≈ 1.13, close to 1.157). The circular-pitch bracket is off the pitch circle (Minor).
- `gear-types`: A–G identifications are correct. Same-hand helices and herringbones, bevel apex offset, and worm looks like a rack (Minor).

## Verified lab facts

- **Milling Log Sheet #1.jpg** (2025): objective "spur gear … from a circular workpiece"; tools (universal horizontal milling machine, index plate (2), chalk, catch pin, shaft, mandrel, worm wheel, rough flat file, bench vise, coolant, calipers); procedure steps i–vi (teeth → working depth & index → fix index plate → clamp, machine + coolant on → cut, bring back, index, repeat → polish with file); the 5 precautions (shoes & apron, distance, fix workpiece, don't reverse index-plate handle, stay alert). All match KB F092, F101, F105–F110, F111–F115.
- **Milling Log Sheet #2.jpg**: OD = (N+2)/DP; W.D. = 2.157/DP "= 0.1328″ = 3.4 mm" (the 0.1328 slip is already in corrections #5); OD 1½″ → N = 22; DP 16; index 40/N = 1 9/11 = 1 + 27/33 → 2nd plate; plate table 15–20 / 21,23,27,29,31,33 / 37,39,41,43,47,49.
- **Milling Formula_.jpg** (board): same as MLS2 (objective, OD 1½″, DP 16 inch⁻¹, N = 22, W.D. 2.157/DP = 0.1328″ = 3.4 mm, 1 + 27/33, three-column plate table).
- **Milling Lab_.jpg** (wall charts): Cutters chart: plain, helical plain, side-and-face (with the "cutting edges on both sides as well as … periphery" text), interlocking side, half-side, staggered-tooth. Column-and-knee chart: parts 1–15 exactly as MIL-F051. Universal dividing head chart: parts 1–13 exactly as MIL-F061, plus set-ups for differential indexing and helical milling.
- **Milling Tools.jpg**: flat file, outside caliper, index plate, steel rule, involute gear cutter, double-ended spanner, finished spur gears, gear-train model (plus a cardboard tooth template). Matches MIL-F103.
- **Log Sheets ME-106.pdf p.9** (2022): objective "spur gear using milling operations"; tools (column-and-knee machine, catch pin, shaft, index plate, tailstock, worm wheel, mandrel); procedure (teeth from OD & DP, indexing, run slowly, polish); precautions (shoes, distance, alert, don't touch electrical connections); sketch "n = 14". No coolant is mentioned.
- **Manufacturing_Notes_2023.pdf pp.1–4**: p.1 down/up milling definitions, helical plain = "nick cutter" for slab cutting, straddle mis-definition; p.2 gang milling, machine types, aluminium circular disc, tools (outside caliper, mandrel, chuck key); p.3 DP = teeth/circumference (corrections #3), OD 1″, DP 16 → n = 14, 40 turns, 40/14 = 2 6/7; p.4 plate table, "plate 2 (21 holes)" 2 + 18/21, W.D. = 2.157/16 = 0.1346″ (corrections #4).
- **Milling.pdf** (lecture, 28 slides, all viewed): s.3 HSS/versatile; s.4–7 up/down definitions, chip thickness, advantages and disadvantages (no backlash mention); s.8 operation list; s.9–15 plain/face/end/straddle/form (20–30 % less)/gang (largest cutter)/angular; s.16 cutter nomenclature; s.17–20 machine types and parts (no quill in the s.19 list); s.22 index plate figure, worm wheel 40 teeth, single-thread worm; s.23–24 direct indexing 24/30/36, square → 6 holes; s.25–26 40/7 = 5 + 35/49; s.27 compound indexing.
- **Milling TA.pptx** (python-pptx text, including tables): s.2 precautions; s.5–6 machining and milling definitions; s.8 up/down table (backlash, power, finish); s.9 machine types; s.11 horizontal vs vertical table; s.14 involute cutter; s.15–16 cutter tables (slab, side-and-face, slotting, gang, formed, hollow, T-slot; end mill, face mill, ball nose, slot drill, roughing, dovetail, fly); s.17 indexing; s.18 plate table; s.19 DP = teeth per inch of pitch diameter, spur gear definition.
- **Theory checks**: the B&S cutter ranges (No. 5 for 21–25 → 22-tooth job; No. 7 for 14–16) are correct; addendum 1/DP, dedendum 1.157/DP, whole depth 2.157/DP, circular pitch π/DP, module 25.4/DP; all DP-16 values recomputed (0.0625, 0.0723, 0.1348 in = 3.42 mm, 0.196 in, 1.5875 mm, PCD 1.375 in); indexing for 7, 11, 14, 22, 36 and 40 divisions and 9° per crank turn recomputed; gear shaft arrangements are correct.

---
## Fixes applied by the author (round 1)
- MIL-0152: Reason replaced with "Down milling is also known as climb milling" (key b). The explanation now says the better finish comes from full-thickness entry with no rubbing.
- MIL-0091: reworded as "depth of engagement of two mating teeth (two addenda)", and 2.157/DP removed from its options.
- MIL-0113: distractor 0.125 in (2/DP) replaced with 0.0723 in (dedendum); explanation updated.
- MIL-0027: gang stem now says "a set of cutters of different sizes … machine several different surfaces in one pass".
- MIL-0014: distractors rewritten, removing "maximum radial load on arbor at entry".
- MIL-0049: distractors are now clapper block / swing over bed / bastard cut (no tang or quill).
- MIL-0097: the stem now says "spur gears and ordinary (parallel-axis) helical gears".
- MIL-0190: "Face mill" removed from the panel-E options.
- Silly distractors replaced ("Lunch breaks", "Laser", "Dielectric pump", dielectric in MIL-0252).
- Difficulty hard → medium: MIL-0076, 0122, 0139, 0149, 0252.
- Figures:
  - dividing-head: the crank is redrawn as a distinct arm at its own angle, with label B on it.
  - gear-types: the helical pair has opposite hands; the bevel cones meet at the axis intersection.
  - gear-nomenclature: the circular-pitch extension lines start at the pitch circle.
  - cutters: alt text now says six drawings.
- corrections.md #23 added (the notebook's straddle-milling definition).
