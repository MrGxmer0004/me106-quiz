# Lathe question bank: independent review

Reviewed file: `src/data/questions/lathe.json`, 276 questions (LAT-0001 to LAT-0276).
Also checked: `knowledge/lathe.md`, `corrections.md`, the 9 `lathe/*` entries in `src/data/figures.json`, all 9 PNGs in `.render/lathe/`, and the source pages listed under "Verified lab facts". I recomputed every numerical question.

## Summary

| Severity | Questions | IDs |
|---|---|---|
| Critical | 1 | LAT-0120 |
| Major | 19 | LAT-0070, 0106, 0113, 0127, 0137, 0156, 0197, 0210, 0213, 0218, 0230, 0231, 0232, 0233, 0234, 0235, 0243, 0275 (+0128 depends on 0127) |
| Minor only | about 99 (not also counted above) | listed below; many are only "the correct option is clearly the longest" (41 questions) or a near-duplicate |
| No problem found | about 157 | |

Overall, the keys are sound. Every number is correct except the duplicate-answer problem in LAT-0120. All fact IDs exist, and all 146 facts are used. Answer positions are balanced (68/68/67/67). The main problems are: (a) one question with two correct options; (b) some 2022-only procedure details presented as the current job; (c) three figures with wrong geometry or misleading leader lines; (d) the job drawing prints the answer to the questions asked about it.

## Critical

| ID | Problem | Suggested fix |
|---|---|---|
| LAT-0120 | Two options are correct. Key "1 : 7.5", but option 3 "2 : 15" is the same ratio (2/15 = 1/7.5 = 0.1333 = 4/30). | Replace option 3 with a wrong value, e.g. "1 : 3.81" or "4 : 34". Or ask for tan α, but LAT-0116 already does that. |

## Major

| ID | Problem | Suggested fix |
|---|---|---|
| LAT-0156 | Arguable A–R key. Low threading speed is used because the carriage must move one pitch per revolution: at 315 rpm × 1.5 mm the carriage moves about 470 mm/min, which is too fast to disengage at the groove. So R arguably does explain A, and many students and teachers would choose option 0. The explanation's own reason (controlling the tool and withdrawing it) follows from R. | Replace R with a statement that is true and clearly unrelated (e.g. "The lead screw is disengaged during plain turning"). Or drop the question. |
| LAT-0113 | Ambiguous. The source (LS p.1 step 5) gives only "least count of cross slider is 0.02 mm". It does not say whether a division is 0.02 mm of tool (radial) movement or 0.02 mm of diameter. Many lathe dials read diameter directly, and then the answer would be 0.5 mm (option 2). | State it in the stem: "each division moves the tool 0.02 mm radially". |
| LAT-0106 | The keyed answer is circular. "Why was speed reduced to 90 rpm for threading?" → "Thread cutting is done at a much lower speed than turning" restates the question. The real reason, given in the explanation, is not an option. | Make the key "So the operator can control the carriage and withdraw the tool at the end of each pass (the carriage moves one pitch per rev)". |
| LAT-0243 | Distractor "Slightly above the axis for rough cuts" is advice found in some shop texts, so it is arguably correct for external turning. | Reword the stem to facing ("When facing, the tool tip must be set…"), or change the distractor to "Well above the axis to increase clearance". |
| LAT-0137 | 2022-only detail presented as the current job. "Plain turning to the largest diameter" is LS p.2 step 7 (Ø38 bar → Ø37 over the whole length). The 2025 procedure (CLLS p.1) is: measure → mark 115 & chuck → centre/set rotation → facing → groove and taper → thread. It has no plain or step-turning step. The 2025 largest diameter (Ø38) equals the recorded raw bar (Ø38), so there may be no plain-turning step at all. | Label it as the 2022 log sheet, or ask "after facing, what comes next on the 2025 sheet" (groove and taper). |
| LAT-0275 | Same 2022-only basis as LAT-0137 ("plain turning first sizes the largest diameter"). The option is also much longer than the others. | Same as LAT-0137. |
| LAT-0127 (and LAT-0128) | The raw stock "120 mm × Ø38" comes from NB p.17, which goes with the 2022/23 job (Ø37 max; NB p.11 drawing). The 2025 sheet gives no raw size. With a finished Ø38 section, a Ø38 bar leaves no turning allowance, so the 2025 raw size is unverified. LAT-0128 (120 − 115 = 5 mm) depends on it and cites CLLS. | Confirm the 2025 raw bar size, or say "(2022–23 notes)" in both stems. |
| LAT-0070 | Option 3 "1.5–2.0% carbon" is exactly what the lab notebook says (NB p.16, correction #1). The key is right by the standard classification, but a student who revised from the notes will choose 3 and be marked wrong, and the explanation does not mention this. | Add to the explanation: "The class notes say 1.5–2 %; that is wrong (corrections.md #1)." Or replace the distractor. |
| LAT-0197 | Figure `lathe/operations` panel B is wrong (see Figures). The arrow shows the tool moving left, but the part already passed (right of the tool) is drawn at full diameter, and the "material to remove" strip is drawn ahead of the tool. That is only consistent with the tool feeding to the right. | Redraw so the work right of the tool is at the reduced diameter, or reverse the arrow. |
| LAT-0210, LAT-0213 | Figure `lathe/thread-profiles` panel A is labelled 60°, but it is drawn with a 53.1° included angle (half-width 35, height 70 → 2·atan(0.5)). That is closer to Whitworth 55° than to metric 60°. The 60° arc does not line up with the flanks. | Set the tooth height to 35/tan 30° ≈ 60.6 (or the half-pitch to 40.4 for height 70). |
| LAT-0218 | Figure `lathe/thread-terms`: label C (flank) has a leader line from (155,300) to (210,190) that passes exactly through the root vertex at (180,250). Students may read C as pointing at the root (B is the root). The V is also drawn at 53°, not 60°. | Move C's label so the leader does not cross a vertex (e.g. label at the upper left of the flank). Fix the V to 60°. |
| LAT-0230–0235 | Figure `lathe/job-2025` prints every dimension (Ø38, 30, 5, Ø34 × 1.5, Ø32, 20, 1 × 45°) next to the segment the question asks about. These questions test reading, not recall, and the exam will not show the drawing. | Render a variant with the asked dimension hidden (or all dimensions hidden) for these questions. |

## Minor

**Wording and source date (2022-only details, not wrong).** The 2025 sheet does not have these. Say "2022 log sheet" in the stem, or add the CLLS ref where it applies.
- LAT-0134, 0254, 0106, 0108, 0109, 0156: 315 rpm and 90 rpm appear only on LS p.1–2 (2022) and NB p.17. CLLS p.1 says only "set rotation for required diameter". This is fine if the machine is unchanged, but the source is not the current sheet.
- LAT-0112 (least count 0.02 mm) is LS p.1 only.
- LAT-0145, 0150, 0267: "remove chips timely" and "move the tailstock carefully" are only on the 2022 sheet. LAT-0150 says "the ME-106 lathe log sheet" while there are two sheets.
- LAT-0138, 0142, and fact F121: plain and step turning in the order come from LS (2022). The 2025 sheet lists only facing → groove & taper → thread. The keys stay valid because the other options are clearly wrong.
- LAT-0255: the explanation says "marked 25 mm length" (2025) but cites LS p.2 (2022, where the thread is 20 mm long). Cite CLLS p.1.

**Refs.**
- LAT-0026: the "supporting, moving and controlling part of the cutting tool" wording is on LEC s.16, not HO p.4.
- LAT-0068: NB p.17 gives only 18 % W and 4 % Cr; the vanadium comes from theory, so add the Hajra Choudhury ref.
- LAT-0115, 0118: HO p.12 defines D, d, l and α but does not print tan α = (D−d)/2L. The formula is on LS p.2, CLLS p.2 and NB p.14.
- LAT-0116: the tan α calculation is on CLLS p.2, not p.1.
- LAT-0151 ("on both sheets") cites only LS p.1; add CLLS p.1. Confirmed on both.
- LAT-0061, 0058, 0059, 0060: CLLS p.1 supports these as well; add it.
- LAT-0002: the explanation's "because most other machine tools developed from it" is not in the handout. It is harmless.

**Numerics.**
- LAT-0118: the distractor "≈5.73°" should be 5.72° (2 × 2.862 = 5.725). It is still wrong either way, so the key is unaffected.

**Category labels.**
- LAT-0013, 0014, 0015 (bed material) are tagged workpiece-material; should be machine-parts.
- LAT-0210–0215 (thread forms) are tagged operations; should be definitions or applications.
- LAT-0115 (meaning of α) is tagged numericals; should be definitions.
- LAT-0004 (types of lathe) is tagged machine-parts; should be definitions.

**Difficulty labels.**
- Too high: LAT-0125 (20 × 1.5, hard → easy), 0238 (30 + 25, hard → easy), 0236 (hard → medium), 0072, 0086, 0093, 0096, 0248, 0254, 0271 (hard → medium), 0263, 0269 (hard → easy).

**Format and distractors.**
- LAT-0189 has only 2 options (50 % guess).
- LAT-0187/0188/0189: the chucks figure has the captions "3 jaws"/"4 jaws", which make the panel questions trivial.
- Silly or cross-shop distractors that are too easy to eliminate: LAT-0044 ("number of teeth on chuck jaws"), 0145 ("blown away with the mouth"), 0150 and 0151 (index crank, plating solution, dielectric, wheel dressing), 0244 ("the chuck has 4 jaws"), 0251 ("by its colour"), 0259 ("welding helmet", "no protection"), 0261 ("to reduce the thread pitch"), 0263 ("the tailstock locks"), 0268 ("so the thread pitch changes", "motor runs cooler").
- In 41 questions the correct option is at least 1.4× longer than every distractor. The worst cases: LAT-0047, 0137, 0267, 0242, 0135, 0264, 0083, 0126, 0012, 0024, 0052, 0084, 0246, 0249, 0275. The full list: 0012, 0023, 0024, 0047, 0052, 0055, 0063, 0075, 0079, 0082, 0083, 0084, 0085, 0126, 0131, 0132, 0133, 0135, 0136, 0137, 0140, 0141, 0144, 0148, 0151, 0165, 0221, 0229, 0239, 0242, 0246, 0249, 0256, 0260, 0261, 0263, 0264, 0267, 0269, 0273, 0275. Pad the distractors or trim the keys.

**Near-duplicates** (keep one of each, or vary them):
- 0253/0272: rotate the chuck by hand.
- 0148/0263: chuck key.
- 0149/0266: measure only when stopped.
- 0145/0265/0269/0152: chip removal.
- 0058/0273: marking tools.
- 0059/0274: measuring tools.
- 0134/0254: speeds.
- 0137/0275: plain turning before step turning.
- 0052/0054: 4-jaw vs 3-jaw.
- 0140/0240: compound rest for the taper.
- 0042/0043: angular feed.
- 0098/0125: one pitch per revolution.
- 0144/0264: dress.
- 0013/0014: bed cast iron.
- 0021/0157/0191: live centre.

## Figures

- `lathe/lathe-overview`: mostly correct, and all 17 letters point at the registry's parts. Small issues:
  - The tool-post clamp lever ends in a black ball that sits at the bottom of the dead-centre cone, right next to E's leader dot. Two dots on the dead centre look like a second callout, so move the lever.
  - The tool wedge sits under the work instead of at centre height, and the tool-post block touches the work's underside.
  - P (gear box) is drawn inside the headstock outline. That is acceptable, but A and P overlap.
- `lathe/chucks`: correct (3 stepped jaws with scroll key sockets; 4 independent jaws with screw heads and concentric rings). The captions "3 jaws"/"4 jaws" give away LAT-0187–0189.
- `lathe/centres-dog`: OK. The catch plate pin drives the bent tail of the dog, the live centre is in the spindle, the dead centre is in the quill, and the rotation arrow is on the work.
- `lathe/operations`:
  - Panel B (straight turning) has wrong geometry: the reduced diameter is drawn ahead of the tool, not behind it (Major, LAT-0197).
  - Panel F (parting) has a slot drawn below the axis, so the tool appears to go past the centre. The tool needs to reach only the axis.
  - Panel I (threading) shows the tool as a flat-ended rectangle with no 60° point, sitting on the crests.
  - G (chamfer) and J (knurl) have no feed arrows, though the alt text says arrows show feed.
  - A, C, D, E, H are OK. The taper arrow is roughly parallel to the taper surface and points toward the large end.
- `lathe/thread-profiles`:
  - Panel A is labelled 60° but drawn at 53° (Major).
  - The square thread is drawn about 70 % of p deep, against the usual p/2 (minor).
  - The buttress is drawn about 7° / 38°, against the usual 45° (acceptable).
  - The pitch arrows are correct.
- `lathe/thread-terms`:
  - The C leader passes through the root vertex (Major).
  - The V is drawn at 53°.
  - Otherwise correct: A crest, B root, D pitch (crest to crest), E depth (crest line to root line), F major radius to the axis, G minor radius to the axis.
- `lathe/spt-tool`: OK. Positive back rake (face sloping down from the cutting edge, measured from the horizontal), end clearance measured from the vertical, base under the shank, nose in plan view. The angle markers are tiny ticks rather than arcs and are hard to see.
- `lathe/taper`: OK. D, d, L and half-angle α are correct, and the formula is printed.
- `lathe/job-2025`:
  - The geometry matches the 2025 drawing (35/30/5/25/20 = 115; Ø38, Ø38→Ø34, groove, Ø34 × 1.5, Ø32; 1 × 45° at the left; centre holes at both ends). The drawn diameters are to scale.
  - The printed dimensions give away LAT-0230–0235 (Major).
  - The CLLS and BOARD sketches also seem to show a small chamfer at the right end, which the figure does not draw (minor).

## Verified lab facts

Pages opened, and what each confirmed. Personal details on the log sheets were not copied.

- **Central Lathe Log sheet.pdf p.1 (2025)**:
  - Drawing: Ø38 × 35 with 1 × 45° chamfer; taper to Ø34 over 30; 5 groove; 34 × 1.5 pitch thread, 25 long; Ø32 × 20; 115 overall; centre holes at both ends; "all dimensions in mm".
  - Objective: facing, turning and threading.
  - Tools: marker, marking stand, marking plate, outside caliper, scale, marking chalk, lathe job carrier, catch, lathe (tool) holder, wrench, chuck.
  - Procedure: (1) measure length and diameter; (2) mark 115 mm and fix in the 4-jaw chuck; (3) check the centre and set rotation; (4) facing to length; (5) groove and taper turn; (6) thread 1.5 mm pitch over 25 mm. **No rpm values are given, and there is no plain/step-turning step.**
  - Precautions: proper distance (hot chips); apron, tight clothes and shoes; measure in proper lighting with inner and outer calipers; handle heavy machines and tools with care.
- **Central Lathe Log sheet.pdf p.2**: tan θ = (38−34)/(2×30) = 1/15, θ = 3.814°; d = 0.6134 × 1.5 = 0.92 mm; Dc = 34 − 1.84 = 32.16 mm. All match LAT-0116, 0117, 0121, 0122.
- **Central Lathe Diagram.jpg (board)**: confirms the 2025 dimensions (Ø38, 1 × 45° chamfer, 35/30/5/25/20, 115, Ø34, Ø34 × 1.5 mm pitch, Ø32), centre holes at both ends, and "All dimensions are in mm".
- **Log Sheets ME-106.pdf p.1 (2022)**:
  - Job Ø37 × 35, Ø35, taper, groove 5, Ø30 × 1.5 thread, 20 long, 115 overall.
  - Tools: chalk, marking stand, marking plate, outside caliper, scale, marker, lathe job carrier, catch.
  - Steps 1–4 match LAT-0131; 315 rpm; least count of the cross slide 0.02 mm.
  - Precautions: apron/tight clothes/shoes; handle heavy machinery with care; remove chips timely; move the tailstock carefully.
- **Log Sheets ME-106.pdf p.2 (2022)**:
  - Order: plain turn to Ø37 → step turn Ø35 → step turn Ø30 → 5 mm groove → taper (tool post set to θ = 5.7°) → look up the table for 1.5 pitch and set 90 rpm → threading.
  - d = 0.9201; Dc = 28.16.
  - Confirms the order in LAT-0138, 0139, 0142, 0242, and that the speeds and plain/step turning are 2022 details.
- **Manufacturing_Notes_2023.pdf**:
  - p.11: 2022 job drawing; metal-removal process; low-carbon (mild) steel; tool harder than the work; HSS; relative motion.
  - p.12: parts sketch including chip tray and legs; the live/dead centre statement (correction #10); 3-jaw vs 4-jaw.
  - p.13: facing, turning, straight vs step turning; the "feed" definition that correction #12 fixes.
  - p.14: taper formula; grooving; parting-off; centre drilling.
  - p.15: thread nomenclature; M20 × 1.5; 60°; d = 0.6134p; Dc = Dm − 2d; square thread for load lifting.
  - p.16: buttress (≈45°); chamfering; mild steel < 0.3 % C. The wrong "medium 1.5–2 %" and "6.67 % max in steel" are here.
  - p.17: HSS 18 % W, 4 % Cr (no V); workpiece 120 long, Ø38; 4-jaw chuck; 315 rpm; same tool list.
- **Centre Lathe.pdf (handout)**:
  - p.1: types of lathe; mother of machine tools; cylindrical/cone surfaces.
  - p.2: engine lathe; working principle.
  - p.3: bed (guideways; compressive strength and wear resistance; Ni-Cr cast iron); headstock on the left, gear box to the feed rod and lead screw, chuck/face plate on the spindle.
  - p.4: tailstock on the right, drills/reamers, moves for length; carriage.
  - p.5: saddle feed; cross-slide perpendicular, depth of cut.
  - p.6: compound slide on the cross-slide; tool post.
  - p.7: feed rod; lead screw for threading only and disengaged otherwise.
  - p.8: work-holding methods; tool parts (shank, face, flank, heel, base, nose, point).
  - p.9: operations list; facing.
  - p.10: straight turning; chamfering.
  - p.11: knurling; parting ("feed is fixed or locked").
  - p.12: taper definition and symbols; thread cutting.
  - p.13: feed = pitch per revolution; specification list.
- **Central Lathe..pdf (lecture)**:
  - s.7: parts list, specification, swing.
  - s.9–10: form tool.
  - s.12: chip pan.
  - s.13: grey cast iron; inner and outer ways.
  - s.14: headstock houses spindle, speed mechanism and change gears; "has live centre"; tumbler gears forward/reverse and engage/disengage.
  - s.15: tailstock dead centre; parts T1–T6.
  - s.16: carriage, apron, half-nut lever, feed lever.
  - s.17: H-shaped saddle.
  - s.19: compound rest graduated base; its handwheel gives the taper feed.
  - s.20: single-screw, 4-way and 8-way tool posts.
  - s.21: three feeds; angular feed is by hand only.
  - s.22: half-nut.
  - s.23: dog and dog plate.
  - s.24: 3-jaw (cylindrical and hexagonal work, jaws move together) and 4-jaw (reversible jaws, independent).
  - s.25: collet with three slits.
  - s.26: face plate with 4 clamps.
  - s.27: operations.

---
## Fixes applied by the author (round 1)
- LAT-0120: distractor "2 : 15" replaced with "1 : 3.75".
- LAT-0156: reason replaced with "The lead screw is used only for thread cutting" (key: both true, R not the explanation); explanation rewritten.
- LAT-0113: stem now says each division moves the tool 0.02 mm radially.
- LAT-0106: the key now gives the real reason (carriage moves one pitch per rev, so a low speed leaves time to withdraw the tool at the groove).
- LAT-0243: distractor changed to "Well above the axis to increase clearance".
- LAT-0070: explanation flags the notebook's wrong 1.5–2% value.
- LAT-0127/0128: reworded as "according to the lathe notes"; fact LAT-F102 now says it is from the 2022–23 notes and not restated on the 2025 sheet.
- LAT-0137, LAT-0275 and the sequence/order questions: rewritten to the 2025 log-sheet procedure (facing → groove & taper → threading). Facts LAT-F118/F121 updated.
- Job questions (LAT-0230 onward) now use a new figure `lathe/job-2025-q` with dimensions hidden. The dimensioned drawing stays for the revision gallery.
- Figures: operations panel B redrawn (reduced diameter behind the tool, original outline dashed); thread V angles corrected to 60° (profiles and nomenclature); flank leader moved off the root vertex; "3 jaws"/"4 jaws" captions removed from the chucks figure.
- Category fixes: bed-material questions → machine-parts; thread-profile figure questions → definitions.
- Not changed: the 315/90 rpm and 0.02 mm least-count facts are kept as lab facts (same shop and machine; from the 2022 log sheet), and their refs say so.

## Re-check (round 1)

What I re-checked: the listed IDs, every question citing LAT-F118 or LAT-F121 (0137, 0138, 0139, 0142, 0242, 0255, 0275, 0276), the job questions now on `lathe/job-2025-q` (0230–0238), the category fixes (0013–0015, 0210–0215), and the re-rendered PNGs. I also checked the updated facts F102, F118 and F121.

| Item | Status | Reason |
|---|---|---|
| LAT-0120 | OK | The new distractor 1 : 3.75 (= 4 : 15) is wrong. 1 : 7.5 is now the only correct option. |
| LAT-0156 | OK | The new R ("lead screw used only for thread cutting") is true and does not explain the low speed, so key 1 is clear. The explanation is correct. |
| LAT-0113 | OK | The stem now states 0.02 mm radial per division. 25 × 0.02 × 2 = 1.0 mm. |
| LAT-0106 | OK (minor left) | The key now gives the real reason. The distractors are clearly wrong. The key is still noticeably the longest option. |
| LAT-0243 | OK | "Well above the axis to increase clearance" is clearly wrong (raising the tool reduces clearance). |
| LAT-0070 | OK | The explanation now flags the notebook's wrong 1.5–2 % value. |
| LAT-0127 | OK | Now "according to the lathe notes", and F102 is dated 2022–23. Matches NB p.17. |
| LAT-0128 | OK | Stem says the 120 mm is "as recorded in the lathe notes". 120 − 115 = 5 mm. |
| LAT-0137 | OK (minor left) | The key "grooving and taper turning" matches CLLS p.1 step 5. **Minor:** F118 now begins "After facing, the smaller diameters are turned", which the 2025 sheet does not say, and it sits oddly with this key ("immediately after facing → groove & taper"). Reword F118 to "The 2025 sheet goes from facing straight to grooving and taper turning; the 2022 sheet had plain and step turning in between". |
| LAT-0138 | OK | Facing is first among taper, thread and groove on both sheets. |
| LAT-0139 | OK | "Grooving and taper turning" comes immediately before threading on CLLS p.1. On LS p.2 only the speed and gear setting comes between, and that is not an option. |
| LAT-0142 | OK (minor left) | The key matches CLLS p.1 steps 1–6. **Minor:** only the key uses the long step names ("mark 115 mm & fix in 4-jaw chuck", "centre & set rotation"); the distractors use short ones. Use the same labels in all four options. |
| LAT-0242 | **Still wrong (Major)** | Not updated. The explanation still says "after step turning", which is 2022 only. The key "…before taper turning and threading" rests on the 2022 order (LS p.2 steps 10–11). The 2025 sheet, which F121 now cites, lists "groove and taper turn" as one step and gives no order between them. Fix: key "After facing, with the taper turning, before threading"; explanation from CLLS p.1. |
| LAT-0255 | OK | Thread cutting is last on both sheets, and "25 mm" now has the CLLS ref. |
| LAT-0275 | OK (minor left) | The new "why is threading last" question is sound, and the explanation is consistent. **Minor:** the key is much longer than the distractors, and "The lead screw only works after facing" is a weak distractor. The reason is standard practice, not stated on a log sheet, so add a theory ref. |
| LAT-0276 | OK (minor left) | Key is correct. **Minor:** fact F118 and the CLLS p.1 ref do not support a feed-rod question; drop them (F037 and F038 are enough). |
| LAT-0230–0235 | OK | `job-2025-q` hides all dimension text, including the 1 × 45° callout. The questions now test recall. The chamfer, centre marks, groove and thread hatching are still drawn, which LAT-0237 needs. The leftover "All dimensions in mm" note is harmless. |
| LAT-0236, 0238 | OK | Arithmetic is correct (35 + 30 + 5 = 70; 30 + 25 = 55). The stems say "from the job drawing", but the new figure shows no numbers; change to "from the job dimensions". |
| LAT-0237 | OK | Conical centre marks are visible at both ends in `job-2025-q`. |
| LAT-0013–0015, 0210–0215 categories | OK | Now machine-parts and definitions. |
| `operations.png` panel B | OK (minor left) | Fixed: the reduced diameter is now behind (right of) the tool, the original outline is dashed, and the feed arrow points left, so it is consistent. **Minor:** mid-pass, B now looks very like panel C (step turning): a shoulder with the tool moving left. LAT-0197's options don't include step turning, so the key is safe. Avoid any future "which panel shows straight/step turning" question unless B is drawn near the chuck end of the pass. Panels F, I, G and J are unchanged (minor notes stand). |
| `thread-profiles.png` | OK | V tooth: half-pitch 35, height 60.6, so 2·atan(35/60.6) = 60.0°. The 60° arc now fits between the flanks. |
| `thread-terms.png` | OK | Height 103.9 for half-pitch 60 gives 60.0°. The C leader now goes from (30,160) to a point on the first flank and crosses no vertex. A, B, D, E, F, G are unchanged and correct. |
| `chucks.png` | OK | "3 jaws"/"4 jaws" captions removed. Jaws and screw sockets are unchanged and correct. |
| `job-2025-q.png` | OK | Geometry is the same as `job-2025` (scaled and correct); only the dimension text is hidden. |

Result: 1 item still wrong (LAT-0242, Major). Six items are fixed but have small Minor points left (0106, 0137/F118, 0142, 0275, 0276, panel B looking like C). Everything else listed is fixed.

## Fixes applied by the author (round 2)
- LAT-0242: key is now "After facing, together with taper turning, before threading"; explanation quotes the 2025 sheet.
- LAT-F118 reworded to the 2025 sheet's single "groove and taper turn" step.
- LAT-0236/0238: stems now say "In the ME-106 lathe job" (the blank figure has no numbers).
- LAT-0276: no longer cites LAT-F118.
- Option-length balancing: distractors rewritten for 55 questions (authoring/fix_lathe.py); 14 flagged remain (6 are figure-label questions).
