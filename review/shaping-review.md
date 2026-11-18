# Shaping question bank: independent review

Reviewed: `src/data/questions/shaping.json` (137 questions, SHP-0001 to SHP-0137), `knowledge/shaping.md` (70 facts), `corrections.md`, the 6 `shaping/*` registry entries, all 6 PNGs in `.render/shaping/` (plus `scripts/figures/fig_shaping.py` for exact coordinates), Log Sheets p.3–4, Manufacturing notes p.18–21, shaping.pdf p.2–12, and the wall chart.

## Summary

| Severity | Questions | IDs |
|---|---|---|
| Critical | 0 | none |
| Major | 8 (+1 bank-wide pattern) | SHP-0023, 0121, 0029, 0129, 0093, 0094, 0108, 0111; correct option is the longest in 75 of 133 multi-option questions |
| Minor | 64 more | listed below |
| Longest-option only | 15 more | listed below |
| No problem found | about 50 | |

- No answer key is wrong.
- Every numerical is correct: 2:1, 1.5:1, 1.33 s, 9 m/min, 76 strokes, 2 min, 58 254 mm³, 20 divisions, 3 cuts.
- All fact IDs exist, and all 70 facts are used. Answer positions are balanced (34/33/34/32).
- The quick-return and clapper-box figures are geometrically correct.
- The main problems:
  - The direction of the "quick-return ratio" is undefined in two questions, and the bank's own m = return/cutting makes the 1 : 2 distractor defensible.
  - "Strokes per minute" is ambiguous in SHP-0029.
  - The single-point-tool figure puts the nose at the wrong corner.
  - The shaper label "Down-feed handle (tool slide)" overlaps with the tool head.
  - The correct option is the longest far too often.

## Critical

| ID | Problem | Suggested fix |
|---|---|---|
| (none) | | |

## Major

| ID | Problem | Suggested fix |
|---|---|---|
| SHP-0023, SHP-0121 | The stem asks for the "quick-return ratio" without saying which way round. "1 : 2" is a distractor, and SHP-0026/0027 define m = return/cutting = 0.5, which is exactly 1 : 2. A student using the bank's own m picks option 1/2. | Write "ratio of cutting time to return time", as SHP-0020 and SHP-0024 do. Or replace the 1 : 2 distractor with 2.5 : 1. |
| SHP-0029 | "38 strokes per minute" is ambiguous. N in shaper formulas is double strokes. If 38 means single strokes (19 cutting strokes/min), the answer is 76/19 = 4 min, which is distractor 1. | Write "38 double strokes (cutting strokes) per minute". Do the same in SHP-0028 ("per double stroke"). |
| SHP-0129 | Figure `shaping/spt-tool`: the nose (C) is anchored at the far top-left vertex (175,194). That is where the end cutting edge meets the non-cutting back edge. The side edge D (190,210)→(280,170) and the end edge E (170,190)→(190,210) meet at (190,210). The slide (p.7) puts the nose at that front corner. The figure teaches the wrong location. C's and E's anchors are also only about 13 px apart. | Move C's anchor to (190,210) and push E's anchor towards (176,196). Re-render. |
| SHP-0093 (also 0094, 0108, 0111) | Label C is named "Down-feed handle (tool slide)", but it points at the handle above the head. Box B is the head and slide together (the code says "tool head (swivel + slide)"), and slide p.6 calls that vertical member the "Tool slide". In SHP-0093 the distractor "Down-feed handle (tool slide)" is therefore arguably a correct name for B. | Rename C to "Down-feed handle (screw)" in the registry and options, and drop "(tool slide)". Optionally say "Tool head (with tool slide)" for B. |
| Bank-wide | The correct option is the longest (or tied longest) in 75 of 133 multi-option questions (56%; chance would be 25%). It is clearly the longest (≥1.25× the next) in 34. Test-wise students can score well without knowing the material. | Lengthen the distractors, or shorten the keys, in the IDs listed under "Longest option". |

## Minor

**Ambiguity, giveaways and figure-linked**

| ID | Problem | Suggested fix |
|---|---|---|
| SHP-0014 | The stem says "metal sheared…", and the key is "Shear plane", so the stem gives the answer away. It is marked "hard". | Ask "What is the angle measured on the tool face called?" (rake angle), or mark it easy. |
| SHP-0119, SHP-0120 | These have only two options (50% guess), and each is the inverse of the other. H's leader anchor at (198,225) floats 18 units inside the orange arc (R = 150) and about 10 units outside the gear teeth, so it is nearer the gear than the arc. | Keep one of the two. Add options such as "both arcs are equal" and "depends on motor speed", or ask for the angle. Put H's anchor on the arc, e.g. (330 − 150 cos 30°, 230 − 75). |
| SHP-0113, 0116, 0117, 0118 | The distractors "Crank angle for the cutting stroke (240°)" and "…return stroke (120°)" print the answer to SHP-0018 and say that the arcs are the angles. | Use other part names as distractors (link, ram, slide, bevel gear). |
| SHP-0126 | The figure caption reads "return (idle) stroke" and has a direction arrow. The key repeats "On the return stroke…" and is the longest option (77 characters against 46). | Remove the captions from the figure used for this question, or reword the key to the same length as the others. |
| SHP-0134 | Base (H) is anchored on the lower edge of the shank's front face, so it can be read as "Shank" (A). | Draw the underside or a hatched base strip and anchor H on it. |
| SHP-0103, SHP-0109 | The ram locking handle (L) is drawn on the column under the rear of the ram. Slide p.6 has it on top of the ram. | Move L onto the top of the ram. |
| SHP-0104 | Driving pulley M is a plain circle in the middle of the column and looks like the bull gear. | Draw spokes, as on slide p.6, or a belt. |
| SHP-0136, SHP-0137 | In `job-q` the receding edge Q (38 mm, drawn about 97 units) is about the same length as R (21 mm, about 92 units). Proportion does not tell the student which is 38; only "vertical = height" does. | Use a receding scale of about 0.8 instead of 0.6×0.8, so that Q is clearly longer than R. |
| SHP-0115/0114 (figure) | The B (crank pin) and C (sliding block) anchors are about 17 px apart, and the pin is hidden under the block. | Draw the block semi-transparent, or anchor C on the block's far edge. |
| quick-return (figure) | Driving pinion G (r 28, centre 171 from O) does not touch the bull gear (r 122): there is a 21-unit gap, and the pinion has no teeth. | Move G to a centre distance of about 150 and add teeth. |

**Labels (category, difficulty, source)**

| ID | Problem | Suggested fix |
|---|---|---|
| SHP-0038 | Marked "hard", but all three distractors are other machines (grinder, milling, lathe). | Mark it easy, or use shaper-part distractors (e.g. "bull gear, cross rail, column"). |
| SHP-0040–0044 | Classification questions are tagged `machine-parts`. | Tag them `principle-theory`, or add a classification category. |
| SHP-0026 | The formula question is tagged `definitions`. | Tag it `numericals`. |
| SHP-0075 | Easy arithmetic is marked "hard" and tagged `procedure`, although it is of type numerical. | Mark it medium and tag it `numericals`. |
| SHP-0057 | One multiplication is marked "hard". | Mark it medium. |
| SHP-0091 | The true/false question is marked medium. | Mark it easy. |
| SHP-0122 | Stroke-length adjustment is tagged `machine-parts`. | Tag it `process-parameters`, like SHP-0021. |
| SHP-0023, SHP-0024 | `source: lab`, but the basis is theory (SHP-F070). | Set `source: theory`. |
| SHP-0080 | A procedure fact (LS p.3) is tagged `precautions`, and it duplicates SHP-0069. | Drop it, or reword it as a safety reason. |

**Refs and knowledge base**

| ID | Problem | Suggested fix |
|---|---|---|
| SHP-0036, SHP-0102 | They cite slides p.6, but p.6 does not label a table support. The wall chart does ("Front support for table"). | Cite the shaper wall chart. |
| SHP-0049 (and SHP-F040) | Slide p.4 only lists the materials. The hot-hardness order comes from theory. | Add "Theory: Kalpakjian". |
| SHP-0087 | Keyways, V-blocks and dovetails are not on slide p.5. | Add "Theory: Hajra Choudhury". |
| SHP-0019 (and SHP-F017) | NB p.19 shows only the 240°/120° sketch, not the ratio. | Cite theory for the ratio. |
| SHP-0071 (and SHP-F055/F056) | The log sheet has 10 steps: 7 repeat until size, 8 switch off and remove waste, 9 remove the block and repeat steps 2–8, 10 readjust the ratchet. The knowledge base calls this "Step 7", and the explanation says "Steps 7–9". | Renumber: F055 = steps 8–9, F056 = step 10. |
| SHP-0065 | "After marking, the block is fixed in vice", but the notebook has punching between marking and the vice. | Say "After marking and punching". |

**Silly or other-shop distractors.** Replace these with plausible shaper options.
- SHP-0001 (spark erosion)
- SHP-0004 ("Neither stroke")
- SHP-0005 ("motor switched off")
- SHP-0008 ("only for round work")
- SHP-0009 (plating, die)
- SHP-0010 ("Zero")
- SHP-0052 ("never touch the work")
- SHP-0053 (gear, grinding)
- SHP-0058 (all three: EDM, dividing head, electroplating)
- SHP-0065 (mandrel, "hung on a wire")
- SHP-0070 ("tapping the clapper box", "pulling the ram")
- SHP-0076 (sandals, loose sleeves, wristwatch)
- SHP-0081 ("ram hits the column")
- SHP-0083 ("blowing them towards others", "need not be removed")
- SHP-0086 ("needs a diamond tool", "cannot make flat surfaces")
- SHP-0087 (electroplating)

**Near-duplicates.** Keep one of each group in an exam draw, or set an exclusion group.
- 0019 / 0023 / 0121: all give 2 : 1.
- 0004 / 0005 / 0090: idle return stroke.
- 0018 / 0091 / 0119 / 0120: 240°/120° split.
- 0033 / 0089 / 0110 / 0126: clapper function.
- 0069 / 0080: depth set with the machine off.
- 0072 / 0079: ratchet direction.
- 0054 / 0055 / 0056 against 0135 / 0136 / 0137: block dimensions.
- 0028 / 0029: same setup.
- 0021 / 0122: stroke length.
- 0030 / 0092 / 0105 (ram), 0032 / 0094 / 0108 / 0111 (down feed), 0036 / 0102 (table support), 0045 / 0096 (HSS tool): the same fact asked repeatedly.
- 0114 / 0115: pin and block share one spot in the figure.
- 0090: true/false form of 0004.

**Longest option.** The correct option is clearly the longest (≥1.25× the next) in:

0003, 0016, 0022, 0032, 0033, 0036, 0037, 0039, 0045, 0048, 0050, 0052, 0053, 0058 (79 characters against 43), 0060, 0065, 0066 (60 against 33), 0071, 0072, 0074, 0079, 0081, 0082, 0083, 0085, 0086, 0087, 0094, 0126 (77 against 46), 0130.

Borderline: 0035, 0042, 0068, 0125.

## Figures

| Figure | Verdict |
|---|---|
| `shaping/quick-return` | **Geometry correct.** The crank centre O is at (330,230) and the crank-pin r = 80. The pivot is at (330,390), which is 2r below, so cos θ = r/d = 0.5 and θ = 60°. The tangent points are at ±60° from the downward vertical, i.e. 30° below horizontal. H is the orange arc from −30° to 210° = 240° over the top, far from the pivot, and is the cutting stroke. I is the dashed arc from −150° to −30° = 120°, near the pivot, and is the return stroke. This matches the chart and NB p.19 (Cut 240° on top, Ret 120° at the bottom). The figure prints no angles. Faults: H's anchor is off the arc; pinion G does not mesh and has no teeth; the B and C anchors overlap; the part-name distractors print 240°/120° (see Minor). |
| `shaping/clapper-box` | **Correct.** The cut moves left (consistent with push type: the column is on the right of `shaper`). The hinge pin is at the top-left, the leading side. On return (moving right) the block rotates +14° about the hinge, the bottom swings forward, and the tool tip trails to the left and rises about 5 px while sliding on the work. The tip geometry has its clearance underneath. Only the captions give away SHP-0126. |
| `shaping/shaper` | Anchors A, B, D–K, M sit on the named parts. C is named in a way that overlaps with B (Major). L is drawn on the column rather than the ram. M looks like the bull gear. There is an unlabelled dot (the hinge) inside D and an unlabelled circle (the elevating handle) near H, which is harmless. No text gives anything away. |
| `shaping/spt-tool` | B, D, E, F, G and A are correct. The nose C is at the wrong vertex (Major). Base H is on an edge that is shared with the shank face. There is no heel, although the slides list one; that is acceptable. |
| `shaping/job-q` | No dimensions are shown. P = 73 (front, horizontal), Q = receding edge, R = vertical, which matches the log-sheet sketch (38 receding, 21 vertical, 73 along). Q and R are drawn at about the same length (Minor). |
| `shaping/job` | It is dimensioned correctly (73 / 21 / 38). No question uses it, so it gives nothing away. |

## Verified lab facts

All are checked against LS p.3–4 unless another source is named.

- **Job size.** The objective is "38 mm × 21 mm × 73 mm". The sketch shows 73 along the length, 21 high, and 38 on the receding edge. Volume = 58 254 mm³.
- **Tools.**
  1. Single-point HSS tool.
  2. Scale with base (stand).
  3. Marking block.
  4. Try square ("triscale").
  5. Hammer.
  6. Chalk.
  7. Dot punch.

  Step 1 uses tools 2, 3, 4, 5 and 7. NB p.20 also lists a surface plate, a vernier caliper (0.02 mm) and a ball-pein hammer, but no question depends on them.
- **Least count.** "L.C. 0.05 mm", written in the margin at step 4 (scale wheel above the head). 1 mm = 20 divisions.
- **Cuts.** Step 3: bring the tool up with the ratchet and crank until it just touches. Step 4: bring the head down 1 mm. Step 5: start with the black button. Step 6: after the first removal, bring the head down 0.5–1 mm as required, with the machine turned off.
- **Steps 7–10.** 7: repeat to size on one side. 8: switch off and remove waste. 9: remove the block and repeat for the other sides. 10: always readjust the crank on the ratchet so the "base" (the table) moves in the correct direction.
- **Precautions (LS p.4).** 1: apron. 2: never put hands on the machine while it is on. 3: do not bring the head down more than 2 mm after touching the block. 4: ratchet set so the base moves in the correct direction. The theory precautions (SHP-F062–F064) are standard.
- **Notebook procedure (NB p.21).** Chalk and marking → punching (to make the marking clear) → lock the workpiece in the plain machine vice → cross-feed handle to align → depth handle for the depth of cut → start the machine. This matches SHP-0063, 0073 and 0074.
- **Quick return.** The chart and NB p.19 show cut 240° and return 120°. The chart labels the link, pin, bevel gears, slide, sliding block, slotted link, pivot and driving gear.
- **Theory.**
  - Push type cuts away from the column, draw type towards it.
  - The clapper block is hinged and lifts on the return stroke.
  - Stroke length is set by the crank-pin radius; stroke position by moving the ram and locking it.
  - Generatrix comes from the primary (cutting) motion and directrix from the secondary (feed) motion (slides p.8–9).
  - Tool materials in order: carbon tool steel < HSS < carbide < ceramic < CBN < diamond.
  - In shaping the tool reciprocates; in planing the work does.
  - V = L·N(1+m)/1000.
  - Cutting and return angles are 360° − 2θ and 2θ, with cos θ = r/d.

  All are correct.
- **Source typos not used in any question.** The slides say "ideal stroke" (meaning idle) and "Cubic boron nitrate" (meaning nitride). The knowledge base and the questions use the correct terms.

---
## Fixes applied by the author (round 1)
- SHP-0023/0121: stems now ask for the "ratio of cutting time to return time".
- SHP-0028/0029: now "double strokes" throughout.
- spt-tool: the nose (C) now anchors where the side and end cutting edges meet. The end cutting edge (E) is on its own edge. The ambiguous Base label is removed.
- Shaper C label renamed "Down-feed handle". The ram locking handle (L) is moved onto the ram. The driving pulley (M) is now a small pulley belted to a motor, and Column (I) is re-anchored.
- Quick-return: the H anchor is on the cutting arc. The pinion G has teeth and meshes with the bull gear. Labels no longer print 240°/120°. The two inverse 2-option arc questions are merged into one 4-option question.
- Clapper-box captions are now "sketch 1/2" (they no longer say "return stroke").
- job-q: the width edge Q is drawn longer, so it is distinct from the height R.
- Classification questions are recategorised to principle-theory. Difficulty lowered on SHP-0014, 0038, 0057 and 0075.
- Option-length balancing: 22 questions (authoring/fix_shaping.py).
