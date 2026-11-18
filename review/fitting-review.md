# Fitting question bank: independent review

Reviewed: `src/data/questions/fitting.json` (204 questions, FIT-0001 to FIT-0204), `knowledge/fitting.md`, `authoring/generated_readings.json`, `scripts/figures/fig_fitting.py`, the 41 `fitting/*` entries in `src/data/figures.json`, and the PNGs in `.render/fitting/`: all 9 tool figures and 11 reading figures (vernier-01, 03, 07, 09, 13; micrometer-01, 03, 04, 08, 13, 14). Sources checked: the fitting lecture PPTX (all 16 slides, including the tables on s.3, s.5 and s.10) and Manufacturing notes p.20.

## Summary

| Severity | Count | IDs |
|---|---|---|
| Critical (wrong key / two correct options) | 0 | none |
| Major | 1 issue (2 questions) | FIT-0116, FIT-0029 (bench-vice figure contradicts the key) |
| Minor | about 75 questions | see below; 36 are only "correct option is clearly the longest" |
| No problem found | about 125 | |

Every answer key is correct. Each question has exactly one correct option. I checked all 32 generated readings in code against `generated_readings.json`: key = reading, no distractor equals the reading, and all options are distinct. I read 11 of the PNGs myself and got the same readings. Answer positions are balanced (53/50/51/50). All 92 fact IDs are used and all exist. The main weaknesses are: (a) one figure contradicts a keyed fact; (b) about 20 questions marked `source: lab` cite slides that do not contain the fact; (c) the generated readings each have one far-off "giveaway" distractor; (d) the correct option is often the longest.

## Critical

None.

## Major

| ID | Problem | Suggested fix |
|---|---|---|
| FIT-0116, FIT-0029 | In `fitting/bench-vice`, the workpiece H (top at y=170) sits completely below the jaw tops (y=150). The figure therefore shows FIT-0029's distractor "Below the jaws". It contradicts the key "only a little above the jaws", the H label text ("projecting only a little above them") and FIT-F028. | In `bench_vice()`, raise the workpiece so that it projects about 10 px above the jaws, e.g. `f.rect(216, 140, 110, 40, 'f2')`. Move the H anchor to match. |

## Minor

**Source labels and refs.** These are tagged `source: lab` and cite a slide, but the fact is not on that slide. Every key is still correct.

| ID | Problem | Suggested fix |
|---|---|---|
| FIT-0040, FIT-0132 | 90° centre-punch angle cited to "lecture s.12". s.12 gives only the purpose (stop the drill slipping), not the angle. | Ref "Theory: Hajra Choudhury"; source theory. |
| FIT-0061, FIT-0105, FIT-0137 | Teeth pointing away from the handle cited to s.12. s.12 only says "apply pressure only on forward stroke". | Add the theory ref; source theory (FIT-0105 can keep s.12 for R). |
| FIT-0027, FIT-0109, 0110, 0112, 0113, 0114, 0115, 0118, 0119 | Bench-vice parts cited to s.8. s.8 only says "Holding Devices: Bench Vice". | Ref theory. |
| FIT-0069, FIT-0145, FIT-0148, FIT-0150 | Uses of the square and triangular files cited to s.12. s.12 names only the flat and round/half-round files. s.8 only names the shapes. | Ref theory. |
| FIT-0035 | The definition ("hardened steel pointed tool") is not on s.12; s.12 only mentions using a scriber. | Add the theory ref. |
| KB F026, F038, F054, F062 | The same mis-citations in `knowledge/fitting.md` (F062's knife-edge file is not on s.8). F008's example ("shaft in a bearing") differs from PPT s.10 ("shaft in a freely rotating fan"). The bearing example is supported by s.5/s.6 (cycle wheel). | Fix the slide refs. |

**Generated readings.**

| ID | Problem | Suggested fix |
|---|---|---|
| FIT-0173, 0174, 0175, 0177, 0180, 0181, 0182, 0183, 0184, 0185, 0186, 0187, 0188 | One distractor is 2–4 mm away (e.g. 0181: 155.00 for 151.80; 0185: 104.70; 0188: 97.30). A glance at the main scale rules it out, so these are really 3-option questions. | Use near-miss errors instead: MSR ± 1, k × 0.01, k read as label × 0.1, or one division off (± 0.02). |
| FIT-0191, 0194, 0198, 0199, 0200, 0201, 0203 | Same problem (0191: 12.90 for 10.79; 0198: 18.10; 0203: 16.70; 0200 and 0201 both use 10.10). | Use ± 0.5 mm (half-line missed or added), ± 0.01, or thimble ± 1. |
| FIT-0173–0204 | Difficulty is arbitrary: every third one is "hard" (0173, 0176, 0179, …), and nothing else differs. | Make them all medium, or base the label on a real feature (half-mm line present, k > 40). |
| FIT-0173, 0176, 0186 (and others with "1 small divisions") | Grammar in the explanation. | "1 small division". |
| micrometer-01…14 (figure) | The thimble edge is always drawn 0.2 mm past the last sleeve line, whatever the thimble value. For 12.47 (mic-13) it should be about 0.47 mm past; for 15.05 (mic-14), 0.05 mm. The readings are unaffected, but the picture is not physically consistent. | `edge = z + reading*s` (place the edge at the true position). |
| micrometer-04, micrometer-14 (figure) | The sleeve labels "20" and "15" are half hidden under the thimble edge. | Draw the labels after the thimble, or offset them left. |
| vernier-* (figure) | In most figures, no main-scale number is visible left of the Vernier zero (only about 2.7 mm of scale is shown). Students must count back from the next decade (e.g. 4 lines back from 140 in vernier-01). This is fine, but harder than a real caliper. | Optional: set `vz` to about 120 px. |

**Category and difficulty mislabels.**

| ID | Problem | Suggested fix |
|---|---|---|
| FIT-0034 | Category `workpiece-material` for surface-plate material. | `tool-material`. |
| FIT-0015, 0016, 0017 | Category `job-dimensions`, but these tasks (drill/tap, assemble, shape) are not dimensions. | `procedure`. |
| FIT-0079, 0080 vs 0047, 0048, 0053, 0058, 0059 | Numericals are split between `numericals` and `measurement-reading`. | Make them consistent. |
| FIT-0027, 0028 vs 0109–0119 | Bench-vice parts are split between `machine-parts` and `tools-equipment`. | Make them consistent. |
| FIT-0048 | "Hard" for 1 − 9/10 = 0.1 mm. | easy/medium. |
| FIT-0107, 0108 | Both true/false questions are keyed True. | Make one of them a False statement. |

**Ambiguity and wording.**

| ID | Problem | Suggested fix |
|---|---|---|
| FIT-0153 | Telling cross-peen from straight-peen (a distractor) in a 2D side view depends on projection: the wedge taper is visible only because the edge is perpendicular to the handle. Weaker students will guess. | Add an end-view inset, or say in the explanation "the taper is seen in side view, so the edge is across the handle". |
| FIT-0068 | The stem says "(rough work)", and "Rough" is also a file grade (not offered). This may confuse. | Stem: "for fast metal removal in general bench work". |
| FIT-0138 | The figure's "cutting stroke" arrow (pointing away from the handle) gives the answer away. | Use a figure variant without the arrow for this question. |
| FIT-0129, FIT-0130 | "Which panel shows a odd-leg…", "a angle plate". | Make the `ask` template produce "an". |

**Silly distractors** (they make the question easy, but are not wrong): FIT-0003 ("Copper and nickel plating"), 0005 ("Laser-beam alignment"), 0010 ("No assembly is possible"), 0017 ("Skill in electroplating"), 0018 (all three off-domain), 0019 (EDM/milling/grinding kits), 0041 ("used only on wood"), 0061 ("Teeth facing upwards"), 0062 ("cuts by its weight"), 0066 ("Colour and weight"), 0085 ("Colour of the head"), 0088 ("To harden the metal"), 0091 ("Plate the job with nickel"), 0094 ("hacksaw needs chalk"), 0095 ("Laser goggles"), 0096 ("Never use a vice"), 0097 ("Lend them to others"), 0103 ("without goggles for better view"). Replace one or two per question with plausible errors, e.g. for 0095 "Gloves and goggles only"; for 0097 "Use them only for rough work" (already present). Keep the others.

**Near-duplicates** (consider dropping one of each set or varying the angle):
- FIT-0023 / FIT-0107 (try square, 90°): almost word-for-word.
- FIT-0062 / FIT-0138 (pressure on the forward stroke).
- FIT-0061 / FIT-0105 / FIT-0137 (tooth direction).
- FIT-0039 + FIT-0040 / FIT-0041 / FIT-0106 / FIT-0131 / FIT-0132 (punch angles).
- FIT-0024 / FIT-0081 / FIT-0088 (punch mark stops the drill slipping).
- FIT-0052 / FIT-0053 (micrometer LC); FIT-0045 / FIT-0047 (Vernier LC).
- FIT-0055 / FIT-0171 (ratchet); FIT-0065 / FIT-0139 (tang).
- FIT-0051 / FIT-0160 / FIT-0162 (depth rod); FIT-0070 / FIT-0151 (half-round).
- FIT-0002 / FIT-0020 (bench vice holds the job).
- FIT-0123 / FIT-0128, FIT-0124 / FIT-0129, FIT-0126 / FIT-0130 (the same panel asked as "part" and "which").
- FIT-0030 / FIT-0122, FIT-0032 / FIT-0126, FIT-0036 / FIT-0123, FIT-0037 / FIT-0124 (text question plus figure question on the same tool; acceptable).

**Correct option clearly the longest** (≥ 1.4 × the longest distractor and ≥ 12 characters longer; 36): FIT-0001, 0004, 0005, 0007, 0010, 0018, 0019, 0025, 0028, 0029, 0031, 0033, 0034, 0036, 0049, 0064, 0066, 0069, 0072, 0073, 0074, 0081, 0086, 0087, 0088, 0091, 0092, 0094, 0096, 0099, 0100, 0101, 0104, 0123, 0148, 0151. The worst are 0005 (63 vs 24 characters), 0018 (64 vs 31), 0092 (40 vs 15), 0004, 0066, 0100. For the figure questions (0123, 0148, 0151), lengthen the distractors (e.g. "Vernier height gauge", "Knife-edge (slitting) file").

## Figures

| Figure | Verdict |
|---|---|
| bench-vice | Anchors A–H all sit on the named parts. **Major:** the workpiece is drawn below the jaw tops (see Major). Minor: the tommy bar runs down to the bench top. |
| marking-tools | All 8 panels are recognisable and the panel letters match the registry. Minor: in the **V-block (C)** the V is only about 55° (standard is 90°), and the bar overlaps the flanks instead of resting tangent to them, so it looks like a V drawn inside the circle. Fix: widen the notch to 90° and place the bar centre at r/sin45° above the apex. |
| punches | The geometry is correct: half-width 16 with h = 16/tan(θ/2) gives exactly 60° (A) and 90° (B). Minor: the angle arcs (r = 26) are drawn at the shoulder, not at the tip. In B the arc (r 26 > cone height 16) sits on the shank. Use r ≈ 10 centred at the tip. |
| hacksaw | **Teeth verified:** each tooth is (x,238)–(x+8,238)–(x+8,246), so the vertical rake face is at the front and the tip leans away from the handle. Correct for cutting on the forward stroke. The cutting-stroke arrow points away from the handle. Anchors A–E are correct. Minor: "adjustable frame" is not shown, and the handle is mounted mid-height on the rear upright. |
| file-parts | Anchors are correct (tang, heel, face, edge = lower outline, point). Minor: the cut hatching runs outside the outline at the tapered point (x ≈ 650–700). |
| file-sections | Flat, square, round, half-round and triangular are all correct and distinct. |
| hammers | A is a ball peen (correct). B shows a wedge taper in side view with the handle in plane, which is a cross-peen (correct). See FIT-0153 for the ambiguity. |
| vernier-parts | Anchors A–G are correct. Minor: the Vernier ticks (12 px) are wider than the main-scale ticks (9 px), the reverse of a real 0.98 mm Vernier, and the two scales are not adjacent. This is schematic only. |
| micrometer-parts | Anchors A–G are correct. The sleeve shows mm and half-mm ticks on both sides of the datum. Minor: the frame's right arm does not meet the barrel. |
| vernier-NN | **Geometry verified in code and on 5 PNGs:** 50 divisions at 0.98 mm (= 49 mm). The labels 0–10 fall every 5 divisions (tenths of a mm). The arrow is at vz + 0.98k·s, which coincides with main-scale mark M + k. My readings: 01 = 136 + 21×0.02 = 136.42; 03 = 22.74; 07 = 152.10; 09 = 151.80; 13 = 100.94. All match the keys. |
| micrometer-NN | **Verified on 6 PNGs:** whole mm above the datum, half-mm below. Thimble numbers increase upwards, which is right for a right-hand screw (the front of the thimble moves down as it opens). They wrap mod 50. My readings: 01 = 10.5 + 0.29 = 10.79; 03 = 9.56; 04 = 20.28; 08 = 14.91; 13 = 12.47; 14 = 15.05. All match the keys. See the Minor table for the edge-offset and clipped-label notes. |

## Verified facts

- **Tool list (PPT s.8):** hacksaw; flat, round, half-round, triangular and square files; hammer; try square; centre punch; Vernier caliper; holding device: bench vice. Matches FIT-0019 and F017. Notes p.20 (ball-peen hammer, surface plate, try square, marking block, steel scale, Vernier 0.02 mm, dot punch) is not attributed to the lab in any question. This is correct.
- **Uses (PPT s.9):** bench vice holds; hacksaw rough cuts; files finish/shape; try square 90°; centre punch layout/marking; hammer chipping/shaping; Vernier/steel rule measure. Matches FIT-0020 to FIT-0026.
- **Material (PPT s.8):** mild-steel plate as per the workshop drawing. Matches FIT-0013.
- **Tasks (PPT s.3 table):** T1 file a block to ±0.1 mm (sawing and filing); T2 square/triangle (accuracy with files); T3 drill and tap (prepare for assembly); T4 assemble and inspect the fit (final project). Objective: manual accuracy plus verifying dimensions. Matches FIT-0014 to FIT-0018.
- **7-step procedure (PPT s.12):** safety check → marking → centre punching → cutting → filing → checking → fitment and inspection. Matches FIT-0086 to FIT-0094. The forward-stroke tip, steel rule + scriber + try square, and "prevent drill bit slipping" are all on s.12.
- **Precautions (PPT s.13):** goggles, apron, closed shoes; proper grip; vice jaws tight and parallel; no damaged tools; clean workspace; tools sharp; no excess force; clamp securely; Safety = Skill + Awareness + Discipline. Matches FIT-0095 to FIT-0098, FIT-0103 and FIT-0104.
- **Fits (PPT s.10):** three types. Clearance (shaft smaller, free); interference (shaft larger, force; gear pressed onto shaft); transition (overlap, slight push). The PPT's transition example (piston in liner) is rightly not used (corrections #22). The non-standard "perfect" and "precision" fits on s.5 and s.10 are not used as keys.
- **Theory (all correct):**
  - Dot punch 60°, centre punch 90°.
  - File grades from coarsest: rough → bastard → second cut → smooth → dead smooth.
  - Taps: taper → intermediate → bottoming.
  - Tap drill ≈ D − p (M10×1.5 → 8.5; M8×1.25 → 6.75 ≈ 6.8).
  - Zero error: subtract a positive error, add a negative one (25.36 − 0.04 = 25.32; 12.47 + 0.02 = 12.49).
  - Least count: 1 MSD − 1 VSD (49/50 → 0.02; 9/10 → 0.1). Micrometer 0.5/50 = 0.01.
  - Hacksaw teeth point forward; fine pitch for thin or hard sections.
  - Cold chisel about 60° for mild steel (texts give 55–60°; the options are unambiguous).
  - Cross-peen is perpendicular to the handle, straight-peen parallel to it.
  - Steel rule about 0.5 mm; files and blades are high-carbon steel (or HSS for blades).

---
## Fixes applied by the author (round 1)
- FIT-0116/0029 (major): bench-vice figure redrawn; the job now projects a little above the jaws.
- Generated readings: the giveaway distractors (×0.1 vernier and int+×0.1 micrometer) are replaced with realistic misreads (±1 division, 0.01 vs 0.02 LC, MSR ±1, wrong half-mm). All readings are now medium difficulty. "1 small divisions" grammar fixed.
- Micrometer figures: the thimble edge is drawn at the true reading position, and sleeve labels too close to the thimble are omitted (the lines are still countable).
- Hacksaw figure: the "cutting stroke" arrow is removed. V-block redrawn with a true 90° V and the bar resting on both flanks.
- Refs: FIT-F038, F054 and F063 are now theory-only (the PPT does not show the angles, tooth direction or file uses). F026 notes the labelled vice image on s.8.
- FIT-0153: "Straight-peen hammer" distractor removed.
- Categories: surface-plate material → tool-material; Tasks 1–4 → procedure. One T/F now has a False key. Template grammar fixed ("the odd-leg…").
- Option-length balancing: 40 questions (authoring/fix_fitting.py).
