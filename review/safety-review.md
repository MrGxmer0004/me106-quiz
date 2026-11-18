# General safety question bank: independent review

Reviewed: `src/data/questions/safety.json` (39 Qs, SAF-0001 to SAF-0039), `knowledge/general-safety.md`, the `safety/signs` registry entry and PNG, and `scripts/figures/fig_safety.py`. I did not re-check the lab-tagged facts against LS, CLLS, MLS1, TA, GPPT or PPT, because those files were not part of this review. I checked the theory items against ISO 3864-1 / IS 9457 and standard fire-safety practice.

## Summary

| Severity | Count | IDs |
|---|---|---|
| Critical | 0 | none |
| Major | 2 rows (bank-wide cue; 8 duplicate clusters covering 19 Qs) | see below |
| Minor | about 14 Qs, plus 2 figure items | see below |

- **Keys.** I found no wrong key. The A-R items (0032, 0033) and the T/F items (0030, 0031) are correct.
- **Answer positions:** 11/10/10/8. This is fine.
- **Main problems.** (a) In 23 of 35 eligible questions (66%), the key is uniquely the longest option. (b) Heavy overlap between questions. (c) The difficulty mix is skewed: 25 easy, 12 medium, 2 hard, and the 2 "hard" items are simple.

## Critical

| ID | Problem | Suggested fix |
|---|---|---|
| none | | |

## Major

| ID | Problem | Suggested fix |
|---|---|---|
| Bank-wide | Longest-option cue. 23 of 35 keys are uniquely the longest. Worst cases: 0004 (2.93×), 0024 (2.56×), 0026 (2.06×), 0016 (1.92×), 0022 (1.73×), 0008 (1.71×), 0009 (1.70×), 0019 (1.60×) and 0002 (1.51×). | Lengthen the distractors to match. Do the ≥1.5× items first. |
| 0011/0031; 0016/0030; 0007/0032/0027; 0012/0029; 0023/0033 (+0024); 0025/0036/0039; 0026/0037; 0034/0038 | Each cluster tests the same single fact (chuck key, chips by hand, gloves, stop before measuring, water on electrical fire, blue = mandatory, green = safe, prohibition sign). That is 19 of 39 questions spread over 8 facts. | Keep one or two per cluster. Use the freed slots for uncovered angles: guards, an e-stop location question, the class of fire for oil, the yellow-triangle meaning in a scenario, and so on. |

Key uniquely longest:
- **≥1.5×:** 0002, 0004, 0008, 0009, 0016, 0019, 0022, 0024, 0026.
- **1.2–1.5×:** 0003, 0005, 0006, 0017, 0020, 0021, 0025, 0028, 0036.
- **<1.2×:** 0007, 0010, 0013, 0027, 0029.

## Minor

| ID | Problem | Suggested fix |
|---|---|---|
| SAF-0001 | The explanation says "Every ME-106 log sheet asks for the workshop apron". The Unconventional log sheet does not mention the apron or any PPE. | Change it to "The shop log sheets and TA slides ask for the apron". |
| SAF-0016 | Option 1, "By blowing them away", does not fit the stem "removed with…". The key is the only option that says "after stopping the machine", which gives it away. | Reword option 1 as "Compressed air while running", and put the timing in every option or in none. |
| SAF-0005 | "Nothing" and "Leave it loose" are the same answer, so the question has effectively 3 options. | Replace one with "Tuck it inside the apron". |
| SAF-0014 | Three distractors are "Yes, if…" against the single "No, never". The pattern gives the key away. | Use 4 different conditions, or change it to T/F. |
| SAF-0018, 0022, 0021, 0009 | Silly distractors: "Thrown onto the bench", "Cover it with chalk", "Wash it in coolant", "Borrow tools without asking", "Use your phone between cuts". | Use plausible mistakes (for example "Lift it alone if it is under 25 kg", or "Apply a plaster and continue without reporting"). |
| SAF-0023 | The key is right, but foam is also a standard extinguisher for oil (class B) fires and is not offered. An informed student may hesitate. | Change the stem to "electrical fire", or add "(not foam)" to the explanation. |
| SAF-0027 | `source: lab`, but the key rests on SAF-F007, which is theory (Hajra Choudhury). | Set `source: theory`, or mixed. |
| SAF-0032, 0033 | Rated hard, but both are one-step recall items. | Rate them medium. |
| Bank | Difficulty mix: 64% easy, 5% hard. | Add 3–4 scenario questions (for example "A coolant spill near a running lathe: what first?"). |
| Bank | All 39 questions are in one category ("safety-general"). | Optional: split into PPE, machine operation, housekeeping, fire, and signs. |
| SAF-0034 | Distractor "Fire equipment location" uses red, which could tempt, but its shape is a square, so the key is still unique. | None needed. |

## Figures

| Figure | Check | Result |
|---|---|---|
| `safety/signs` A | Prohibition: red ring with diagonal bar, white field | Shape and colour OK. **The bar runs bottom-left → top-right.** ISO 3864-1 / ISO 7010 P001 runs it top-left → bottom-right at 45°. Minor. Fix in `fig_safety.py`: line from (62,112) to (158,208). |
| B | Warning: yellow triangle, black border, "!" | OK |
| C | Mandatory: solid blue circle | OK. It has no white pictogram, which is acceptable for a "shape and colour" sign. |
| D | Safe condition: green rectangle with white cross (first aid) | OK |
| Registry `alt` | Says "Four blank safety signs" | B has "!" and D has a cross, so the alt text is inaccurate. Cosmetic. |
| Giveaways | D's first-aid cross makes "Safe condition / first aid" obvious, and B's "!" makes "Warning" obvious | Acceptable for recognition items. The SVG is neutral (`aria-label="Figure"`, no `<title>`). |
| Question match | 0034–0039 | Each key matches the registry label. Each question has only one option that fits the shape and colour. |

## Verified facts

- **ISO 3864-1 / IS 9457 colours.** Red = prohibition, danger, fire equipment. Yellow (with black) = warning. Blue = mandatory. Green = safe condition, first aid, exit. Shapes: circle with bar = prohibition, triangle = warning, solid circle = mandatory, square or rectangle = safe condition. All match 0025, 0026 and 0034–0039.
- **Fire.** Water is for ordinary combustibles (class A). CO₂ or dry powder is for electrical fires. Water must never go on electrical, oil or metal fires (water conducts electricity and spreads oil). Matches 0023, 0024 and 0033.
- **General practice.** No gloves near rotating parts. Remove the chuck key before starting. Stop the machine before measuring or cleaning. Remove chips with a brush or hook. Tie hair back. No loose clothing or jewellery. Goggles where chips or sparks fly. E-stop on trouble. Never leave a machine unattended. Report all injuries. All are consistent with the keys.
- **"Safety = Skill + Awareness + Discipline"** is taken from SAF-F025 (PPT s.13) as given. I did not re-check it against the PPT.
