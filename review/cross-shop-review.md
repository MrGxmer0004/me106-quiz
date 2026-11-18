# Cross-shop review: ME-106 question bank

Reviewer: final cross-shop pass. No question files were edited. Bank state: 1,379 questions in 8 shop files, 745 facts, 85 figures (`node scripts/validate.js` passes).

Scratch scripts and outputs are outside the project in the session scratchpad, under `crossreview/` (`dump.py`, `topic.py`, `show.py`, `dups.py`, `dups2.py`, `checks.py`, `checks2.py`, `labels.py`).

## Summary

| Check | Result |
|---|---|
| Hard contradictions (two items keying different values for the same fact) | **0** |
| Soft inconsistencies (explanations, units or wording that disagree, or a rule followed only loosely) | **7**, see table |
| Lab items that offer 2/DP as a competing answer for the gear-cutting depth | **0** (MIL-0092, MIL-0113, MIL-0132 are clean). One borderline item: MIL-0116 |
| Cross-shop duplicate groups | **21 groups**. 38 items are suggested to drop or rewrite, mostly safety and precaution clones |
| Within-shop duplicate clusters, for reference | 18 clusters |
| Key appears as a distractor in a near-identical stem | 0 real cases (24 hits, all deliberate contrast pairs) |
| Duplicate options, ignoring case and punctuation | 0 |
| "All of the above" or "none of the above" | 0 |
| Numericals whose explanation result does not match the key | 0 (all 75 numerical items recomputed) |
| Personal data (names, roll numbers, signatures, staff) | **None found** |
| Difficulty mix | 28 / 58 / 14 (easy / medium / hard) against a target of 40 / 40 / 20. **Medium is too heavy and easy is too light** |

The facts the brief asked about all agree across shops. These include HSS 18-4-1, mild-steel carbon, all four least counts, tool parts and angles, rake and clearance, tool materials, PPE, chip removal, stopping before measuring, up and down milling, grade and structure rules, marking order, dielectrics, Faraday constants, gear formulas, fits, sign colours, extinguishers, plating parameters, the taper formula and 0.6134p.

The main problems are:
1. **Repetition of generic safety items.** The same precaution is asked in the safety shop and again in 2 to 5 machine shops, often with a cloned option set.
2. **Inconsistent difficulty labels** for identical styles and identical calculations.
3. **Overall difficulty mix.**

---

## Contradictions

### A. Facts checked across the bank (no conflicts found)

| Fact | Items checked | Keyed value everywhere | Status |
|---|---|---|---|
| HSS 18-4-1 and "why HSS" | LAT-0066, LAT-0068, LAT-0069, LAT-0155, SHP-0045, SHP-0047, SHP-0049, MIL-0006 | 18 W, 4 Cr, 1 V; red (hot) hardness | Consistent |
| Mild-steel carbon | LAT-0064, LAT-0065, LAT-0070, LAT-0071, LAT-0072; MS workpiece in ELP-0063, FIT-0013, GRD-0104 | < 0.3 % C; medium 0.3–0.6; high 0.6–1.5; > 2.1 = cast iron | Consistent (corrections #1 and #2 applied) |
| Vernier least count, 0.02 mm | FIT-0045, FIT-0047, FIT-0161, FIT-0173–0190 | 0.02 mm | Consistent |
| Micrometer least count, 0.01 mm | FIT-0052, FIT-0053, FIT-0054, FIT-0108, FIT-0171, FIT-0172, FIT-0191–0204 | 0.01 mm | Consistent |
| Lathe cross-slide least count, 0.02 mm | LAT-0112, LAT-0113 | 0.02 mm (radial) | Consistent |
| Shaper down-feed least count, 0.05 mm | SHP-0061, SHP-0062 | 0.05 mm | Consistent; 0.05 mm never keyed for a different instrument |
| Single-point tool parts | LAT-0073, LAT-0074, LAT-0223–0229 vs SHP-0046, SHP-0126–0132 | Shank, face, flank, nose, base; tang is not a part | Consistent |
| Rake and clearance definitions | LAT-0075, LAT-0076, LAT-0228, LAT-0229, SHP-0051, SHP-0052 | Rake helps chip flow and lowers force; clearance stops the flank rubbing | Consistent |
| Cutting-tool materials | SHP-0048, SHP-0049, SHP-0050, GRD-0055, GRD-0056, LAT-0067, UCM-0008 | Carbon tool steel → HSS → carbide → ceramic → CBN → diamond | Consistent. LAT-0067 ("tool harder than work") and UCM-0008 ("need not be harder") are consistent in context |
| Apron, shoes, goggles, gloves | SAF-0001–0007, SAF-0028, LAT-0144, LAT-0259, LAT-0270, MIL-0140, MIL-0250, GRD-0122, GRD-0129, SHP-0076, FIT-0095, ELP-0075, ELP-0084, ELP-0086, UCM-0066 | Apron and closed shoes everywhere; safety goggles; no gloves near rotating parts; gloves required at plating baths | Consistent. The two glove rules depend on context, and each stem names that context |
| Chip removal | SAF-0016, LAT-0145, LAT-0152, LAT-0265, LAT-0269, MIL-0149, MIL-0248, SHP-0083, FIT-0100 | Brush or chip hook, after stopping; never by hand or by blowing | Consistent |
| Stop before measuring or adjusting | SAF-0012, LAT-0149, LAT-0257, LAT-0262, LAT-0266, MIL-0248, SHP-0069, SHP-0080 | Machine stopped | Consistent |
| Up vs down milling | MIL-0008–0018, MIL-0152, MIL-0182–0185 | Up = conventional, chip thickness zero to maximum; down = climb, better finish, poor with scale | Consistent |
| Grade rule | GRD-0064–0070, GRD-0092, GRD-0132, GRD-0135, GRD-0087 | Grade = bond strength; soft wheel for hard work; A–H soft, I–P medium, Q–Z hard | Consistent; no boundary letter keyed |
| Structure rule | GRD-0072–0076, GRD-0133, GRD-0180–0182, GRD-0086, GRD-0087 | Low number = dense, high number = open | Consistent (correction #8 applied everywhere) |
| Wheel-marking order | GRD-0047, GRD-0048, GRD-0049, GRD-0086, GRD-0173–0179 | Abrasive, grit, grade, structure, bond | Consistent |
| Dielectric types | UCM-0021–0024, UCM-0042, UCM-0128, UCM-0130, UCM-0148, GRD-0191 | Wire EDM: deionised water; die-sinking EDM: hydrocarbon oil or kerosene | Consistent |
| Faraday constants | ELP-0013, ELP-0014, ELP-0016–0023 | F = 96,500 C; Cu 1.185 g/A·h; Z(Cu) = 3.29 × 10⁻⁴ g/C; Ni 1.095 g/A·h | Consistent; arithmetic verified |
| Gear formulas | MIL-0085–0094, MIL-0110–0123, MIL-0132, MIL-0214–0226 | DP = N/PCD; OD = (N+2)/DP; addendum 1/DP; dedendum 1.157/DP; circular pitch π/DP; m = 25.4/DP | Consistent |
| Lab "working depth" = 2.157/DP | Lab: MIL-0092, MIL-0113, MIL-0132. Theory: MIL-0090, MIL-0091, MIL-0220, MIL-0225 | Theory items call 2.157/DP the whole depth and 2/DP the working depth. No lab depth item offers 2/DP (0.125 in) | Compliant |
| Fits | FIT-0008–0012 | Clearance, transition, interference; gear pressed on a shaft = interference | Consistent; the piston example is never used (correction #22) |
| Sign colours and extinguishers | SAF-0023–0026, SAF-0035–0039 | Red = prohibition, yellow = warning, blue = mandatory, green = safe; CO₂ or dry powder for electrical and oil fires | Consistent; only in the safety shop |
| Copper and nickel plating parameters | ELP-0050–0053, ELP-0060, ELP-0062, ELP-0097, ELP-0018, ELP-0021 | Cu 2–6 V, 25–30 s; Ni 1.5–3 V, 5–7 min | Consistent (current: see B3 and B4) |
| Taper formula | LAT-0115–0120, LAT-0140, LAT-0240 | tan α = (D − d)/2L; ME-106 job α ≈ 3.81° | Consistent; arithmetic verified |
| Thread depth 0.6134p | LAT-0102, LAT-0121–0124 | d = 0.6134p; Dc = D − 2d | Consistent |

### B. Soft inconsistencies (no key is wrong, but a student could notice a conflict)

| # | Items | What disagrees | Suggested fix |
|---|---|---|---|
| B1 | FIT-0079, FIT-0080 vs LAT-0122, LAT-0123 | Fitting gives tap drill = D − p (M10×1.5 → 8.5 mm). Lathe gives core diameter = D − 2(0.6134p) (M10×1.5 → 8.16 mm). A student who meets both may think the tap drill should equal the core diameter. | Add one clause to the FIT-0079 explanation: "The tap drill is slightly larger than the core diameter (D − 1.227p), leaving about 75 % thread engagement." |
| B2 | MIL-0116 (lab, addendum for DP 16) | Offers 0.125 in (= 2/DP, the textbook working depth) as a distractor in a lab-labelled item. This does not break the depth rule, because the stem asks for the addendum, but it puts 2/DP in front of students in a lab item. | Replace 0.125 in with 0.0982 in (tooth thickness π/2DP), or relabel the item as theory. |
| B3 | ELP-0060 explanation ("about 5 A"), ELP-0021 stem ("about 5 A") vs ELP-0062 explanation ("5 A/sq ft") | The same board value is stated as a current in two places and as a current density in another. | Pick one unit. If the board says A/sq ft, change ELP-0021 to "a current of about 5 A (assume)" and drop "about 5 A" from the ELP-0060 explanation. |
| B4 | ELP-0018 (copper at "about 5 A") vs ELP-0052 (5–8 A log sheet, 6–8 A board); corrections.md #20 | 5 A lies outside the board range. Corrections #20 says no question asks about copper current, but ELP-0052 and ELP-0018 do. | Change ELP-0018 to 6 A (m ≈ 0.059 g), or say "assume 5 A". Update the corrections #20 text. |
| B5 | GRD-0084 explanation | Calls grit 85 "fine in the notebook scale". 80–120 is the disputed band in corrections #18. The key is unaffected (the item asks about A and V). | Delete the grit remark from the explanation. |
| B6 | SAF-0001 | Says the apron "must be worn in every ME-106 shop", but the unconventional (WEDM and laser) log sheet does not list it, and SAF-F001 cites no UCM source. | Reword to "in the machine shops" or "in every shop with a log-sheet dress rule". |
| B7 | MIL-0138 | "How many times is the work indexed to cut all the teeth? → 22." There are 21 index moves between 22 cuts; the 22nd move only returns to the start. Strict students may argue for 21, which is not offered, so the key survives. | Reword the stem to "How many tooth spaces are cut…" or "how many divisions…". |

---

## Duplicates across shops

How to use this: "true duplicate" means the same fact, the same angle and usually a cloned option set. If the app runs per-shop quizzes, a shop copy still has some value, so it is marked "drop (or keep if per-shop quizzes are the main mode)". In a mixed quiz, every pair below repeats.

| Group | Items | Verdict | Keep | Drop / rewrite |
|---|---|---|---|---|
| D1 Rake angle | LAT-0076, SHP-0051 (similarity 0.98, same keys and distractors) | True duplicate | LAT-0076 | **Drop SHP-0051**. SHP-0052 already covers shaper rake. |
| D2 "Tang is not a part of a single-point tool" | LAT-0073, SHP-0046 | True duplicate | SHP-0046 (fuller list) | **Drop LAT-0073**, or rewrite it as "which is NOT a lathe tool angle". |
| D3 Lab cutting tool is HSS | LAT-0066, SHP-0045, MIL-0006 | Near duplicate (same distractor pool) | LAT-0066, MIL-0006 (milling cutter, a different tool) | SHP-0045: drop, or keep for per-shop quizzes |
| D4 Calipers read by transfer to a rule | FIT-0057, LAT-0063 | True duplicate | FIT-0057 | **Drop LAT-0063** (LAT-0059 and LAT-0268 cover lathe measuring) |
| D5 Chuck key | LAT-0148, SAF-0011, LAT-0263 (consequence), LAT-0057 (what tightens jaws) | LAT-0148 = SAF-0011 | LAT-0148, LAT-0263, LAT-0057 | **Drop SAF-0011** (lathe-specific; already in lathe) |
| D6 Stop before measuring | SAF-0012, LAT-0149, LAT-0266 (T/F), MIL-0248 | Same fact ×4 | SAF-0012, LAT-0149 | **Drop LAT-0266, MIL-0248** |
| D7 Chip removal with brush after stopping | SAF-0016, LAT-0265, SHP-0083, MIL-0149 (+ LAT-0145 log sheet, LAT-0152 UNSAFE, LAT-0269 scenario, FIT-0100 filings) | 4 clones | SAF-0016, LAT-0145, LAT-0269, FIT-0100 | **Drop LAT-0265, SHP-0083, MIL-0149**; LAT-0152 optional |
| D8 Eye protection = safety goggles | LAT-0259, MIL-0250 (same distractors), SAF-0006 (+ GRD-0129, UCM-0066 distinct) | LAT-0259 = MIL-0250 | SAF-0006, GRD-0129, UCM-0066 | **Drop LAT-0259 and MIL-0250** (or keep one) |
| D9 Long hair | GRD-0124, SAF-0005 | True duplicate | SAF-0005 | **Drop GRD-0124** (GRD-0131 still lists tying hair) |
| D10 Remove rings, watches, chains | SAF-0004, GRD-0123, MIL-0146 | True duplicates | SAF-0004 | **Drop GRD-0123, MIL-0146** |
| D11 Loose clothing caught by rotating parts | SAF-0003, LAT-0264 | True duplicate | SAF-0003 | **Drop LAT-0264** (LAT-0144 keeps the log-sheet dress rule) |
| D12 No operation without supervision | SAF-0008, GRD-0128, MIL-0147 (GRD and MIL have identical option sets) | True duplicates | SAF-0008 | **Drop GRD-0128 and MIL-0147** (or keep one shop copy) |
| D13 Fitting safety motto | FIT-0104, SAF-0027 | Exact duplicate | FIT-0104 (its source is the fitting lecture) | **Drop SAF-0027** |
| D14 Log-sheet dress precaution | SAF-0001, SAF-0002, LAT-0144, FIT-0095, SHP-0076, ELP-0075, GRD-0122, MIL-0140 | 8 items, almost all keyed "apron and shoes" | SAF-0001, SAF-0002, LAT-0144 (tight clothes), FIT-0095 (goggles) | SHP-0076, ELP-0075, GRD-0122, MIL-0140: drop, or keep for per-shop quizzes |
| D15 Keep a proper distance | SAF-0010, MIL-0141 (+ LAT-0146 hot chips, GRD-0126 plane of the wheel, SHP-0082 ram line: distinct angles) | SAF-0010 = MIL-0141 | SAF-0010, LAT-0146, GRD-0126, SHP-0082 | **Drop MIL-0141** |
| D16 Clean up after use | SAF-0020, MIL-0148 | True duplicate | SAF-0020 | **Drop MIL-0148** |
| D17 Stay alert during fixing and cutting | SAF-0009, MIL-0144 | Same log-sheet line | SAF-0009 | **Drop MIL-0144** (weak distractors) |
| D18 Handle heavy machines and tools with care | LAT-0151, SAF-0018 | Same log-sheet line | LAT-0151 | **Drop SAF-0018** (weak distractors) |
| D19 Damaged tools | FIT-0097, SAF-0021 | Near duplicate | FIT-0097 | SAF-0021 optional |
| D20 Clamp job and tool firmly | SAF-0015, LAT-0261, GRD-0125 (+ MIL-0142, UCM-0093 log-sheet lines) | LAT-0261 ≈ GRD-0125 ("why clamp firmly") | SAF-0015, GRD-0125, MIL-0142, UCM-0093 | LAT-0261 optional drop |
| D21 Change settings only when stopped | LAT-0257, SHP-0080 (+ SHP-0069 in shaping) | Different machines; SHP-0069 = SHP-0080 within shaping | LAT-0257, SHP-0069 | **Drop SHP-0080** |

Not flagged, because each tests a different fact or angle: ELP-0063, FIT-0013, LAT-0064, GRD-0104 (each shop's own workpiece); GRD-0112 and MIL-0135 (coolant step in two procedures); MIL-0145 and SAF-0017 (different electrical rules); LAT-0067 and UCM-0008; FIT-0062 and SHP-0004 (forward stroke in different tools); FIT-0027 and LAT-0073 (tang as the odd one out in different lists).

**Count:** about 24 items are clear drops. About 14 more are optional, depending on whether per-shop quizzes are the main mode.

### Within-shop duplicate clusters, for the shop owners

- Lathe: LAT-0058 = LAT-0273 (same answer, categorised differently); LAT-0059 ≈ LAT-0274; LAT-0149 = LAT-0266; LAT-0145, LAT-0152, LAT-0265 and LAT-0269 (chips ×4).
- Milling: MIL-0070 = MIL-0156; MIL-0084 = MIL-0143 ≈ MIL-0150 (crank backwards ×3); MIL-0149 ≈ MIL-0248; MIL-0011, MIL-0012 and MIL-0184 (chip-thickness variation ×3).
- Grinding: GRD-0064 = GRD-0135; GRD-0068, GRD-0069, GRD-0070 and GRD-0132 (soft wheel for hard work ×4; the validator flags GRD-0068 and GRD-0069 at 1.00); GRD-0073, GRD-0074, GRD-0075, GRD-0133, GRD-0180 and GRD-0181 (structure number ×6); GRD-0100 = GRD-0134.
- Safety: SAF-0007 = SAF-0028 (gloves; the assertion-reason item adds nothing).
- Shaping: SHP-0069 = SHP-0080.
- Fitting: FIT-0039, FIT-0040, FIT-0041, FIT-0106 and FIT-0131/0132 (punch angles ×5+). There are also 32 "Read the Vernier/micrometer" items (FIT-0173–0204). They are good drill, but they are 16 % of fitting and all labelled medium.
- Unconventional: UCM-0021, UCM-0024, UCM-0128, UCM-0130 and UCM-0148 (deionised water ×5); UCM-0075 ≈ UCM-0093.

---

## Label issues

### 1. Overall difficulty mix

| | Easy | Medium | Hard |
|---|---|---|---|
| Whole bank (1,379) | 388 (28.1 %) | 804 (58.3 %) | 187 (13.6 %) |
| Target | 40 % | 40 % | 20 % |
| Figure items (436) | 34 % | 62 % | **4 %** |
| Non-figure items (943) | 25 % | 57 % | 18 % |

By shop (easy / medium / hard): lathe 30/56/14; milling 22/60/18; fitting 37/54/8; electroplating 23/63/13; shaping 26/61/13; grinding 25/58/17; unconventional 22/66/12; safety 67/31/3.

A relabel simulation with two consistent rules gives **36 / 48 / 16**:
- Rule 1: "name the part" and "which X is shown in panel" figure items go medium → easy (112 items).
- Rule 2: medium numerical and sequence items go medium → hard (34 items).

Reaching 20 % hard would then need about 50 more medium → hard moves among two-step "why" items, or new hard items. Electroplating, unconventional and fitting have the least hard content.

### 2. The same style is labelled differently in different shops

| Style | What happens |
|---|---|
| "In the figure, what is the part labelled X?" | Fitting 32/32 easy; electroplating 10 easy / 3 medium; lathe 17/20; milling 11/21; shaping 13/16; grinding 10/12; unconventional 11/17. The single-point tool figure is medium in both lathe (LAT-0223–0229) and shaping (SHP-0126–0132), while fitting's file and hacksaw figures are all easy. Pick one rule, e.g. naming = easy and function = medium. |
| "Which label shows X?" | Medium in every shop (consistent). |
| Assertion-reason | All 20 items are hard. Some carry trivial content: SAF-0028 (gloves), LAT-0155 (HSS harder than MS), GRD-0132 and GRD-0133. Relabel these medium. |
| Identical calculation, different difficulty | LAT-0121 easy vs LAT-0124 medium (0.6134p); MIL-0110 and MIL-0118 medium vs MIL-0123 hard (N = OD·DP − 2); UCM-0030 medium vs UCM-0129 hard (kerf = d + 2g); SHP-0019 medium vs SHP-0024 hard (stroke-time ratio); MIL-0210 medium vs MIL-0213 hard (extra holes); FIT-0047 and FIT-0048 hard vs FIT-0053 medium (least-count calculation; FIT-0048 is a one-liner). |
| Safety clones | LAT-0259 easy vs MIL-0250 medium (identical); SAF-0016 and SHP-0083 easy vs MIL-0149 medium; SAF-0008 easy vs GRD-0128 and MIL-0147 medium; SAF-0003 easy vs LAT-0264 medium. |
| Over-rated safety items | LAT-0263 hard ("chuck key left in, what happens?"), LAT-0269 hard, LAT-0271 hard. These are easy or medium content. |

### 3. Source (lab / theory) labels that disagree for the same fact

- Rake angle: LAT-0076 is theory, SHP-0051 is lab.
- The lathe single-point tool figure mixes LAT-0223–0227 (lab) with LAT-0228 and LAT-0229 (theory), and LAT-0074 and LAT-0075 are theory.
- Stop before measuring: SAF-0012 is lab, LAT-0149 and MIL-0248 are theory.
- Chip removal: SAF-0016 is lab, SHP-0083 and MIL-0149 are theory.
- Suggested rule: "lab" if any ME-106 source (log sheet, slide, board or handout) states it, otherwise "theory".

### 4. Category labels

- LAT-0058 (tools-equipment) and LAT-0273 (procedure) are the same question with different categories.
- Indexing calculations are split between `numericals` (MIL-0111, MIL-0119, MIL-0121) and `gears-indexing` (MIL-0078, MIL-0210, MIL-0212, MIL-0213).
- Least-count calculations are `measurement-reading` in fitting (FIT-0047, FIT-0048, FIT-0053), while the cross-slide calculation is `numericals` in lathe (LAT-0113).
- Pick one category per style.

### 5. Answer-length cue (from the validator)

The correct option is clearly the longest in 31 grinding, 24 fitting, 23 milling and 22 electroplating items. This is not a key error, but it is an exploitable cue worth a pass.

---

## Programmatic checks

| # | What was run | Result |
|---|---|---|
| P1 | `dump.py`: flattened all 8 files into `all.json` and `all.txt` | 1,379 items; fields checked |
| P2 | `topic.py` regex sweeps for each fact in the brief (HSS, %C, least counts, rake/clearance/flank, tool materials, PPE, chips, up/down, grade/structure/marking, dielectric, Faraday, gear and DP, fits, signs and fire, plating V/A/time, taper, 0.6134), then manual reading of every hit | Results in the Contradictions section: 0 hard conflicts, 7 soft |
| P3 | `dups.py` / `dups2.py`: TF-IDF cosine over (stem + key, key weighted ×2) for all 950k pairs, threshold 0.55 | 214 cross-shop pairs (159 involve figure items with generic "part labelled X" or "panel" stems on different figures, excluded); 55 non-figure cross-shop pairs read by hand. These gave the 21 groups above. 378 same-shop pairs; the top ones are in the within-shop list. |
| P4 | `checks2.py` key-as-distractor: stem-only cosine ≥ 0.6 → 597 pairs. 345 same-figure sibling pairs (different label or panel letter) skipped; 252 compared. Flagged when one item's normalised key appears among the other's distractors. | **24 hits, all legitimate contrast pairs** (e.g. FIT-0039 dot punch 60° / FIT-0040 centre punch 90°; GRD-0059–0062 grit classes; GRD-0065–0067 grade letters; GRD-0074/0075; MIL-0008/0009; MIL-0088/0089; MIL-0110/0118; MIL-0239/0240; SHP-0019/0024; SHP-0054–0056; UCM-0075/0082). **0 inconsistent keys.** |
| P5 | Duplicate options, normalised for case, whitespace and punctuation (maths symbols kept) | **0.** A naive alphanumeric-only pass gives 9 false positives where only symbols differ (GRD-0015 "l×b×Δh" vs "l×b×h"; MIL-0109 "1 inch" vs "1½ inch"; ELP-0017 "71.1 g" vs "7.11 g"; LAT-0103, LAT-0107, MIL-0077, MIL-0086, MIL-0093, MIL-0094). All are genuinely distinct. |
| P6 | Regex `(all\|none\|both) of the (above\|these)` over stems and options | **0** |
| P7 | `checks.py` numeric: for 151 items with a numeric key and a formula in the explanation, compared the final number of the explanation's main clause with the key (1.1 % tolerance) | 26 automatic flags. All were reviewed: they are explanations that end with distractor commentary ("Forgetting the 2 gives…") or symbolic keys. **0 real mismatches.** |
| P8 | Manual recomputation of all 75 numerical items (type `numerical` or category `numericals`), including ELP-0017–0024, GRD-0018–0020, GRD-0024, LAT-0108–0125, MIL-0075–0123, MIL-0210–0213, SHP-0019–0029, SHP-0057, UCM-0030–0033 and UCM-0129 | All keys correct. Only rounding note: ELP-0020 explains 25.3 min against a key of "≈ 25 minutes", which is fine. |
| P9 | `labels.py`: difficulty and source by question style and shop; relabel simulation | Results in Label issues |

---

## Personal-data scan

**Result: clean. No personal data was found.**

Scope: all 8 question files (stem, options, explanation, ref, tags), `src/data/figures.json` (titles, alt text, label part and function text), `knowledge/*.md` (including coverage-report.md) and `corrections.md`.

| Pattern | Hits |
|---|---|
| 8 or more consecutive digits (roll numbers) | 0 (longest numbers: "00709" from 0.00709 cm in ELP-0024; "17741" from a bath quantity quoted in corrections #19) |
| "roll", "enrolment" or "reg no" | 0 relevant (only "rolled copper", "rollers", "pitch circles roll") |
| Titles (Prof, Dr, Mr, Mrs, Ms, Shri, Smt, Sir, Madam) | 0 |
| "signature" or "signed" | 0 |
| Email addresses or 10-digit phone numbers | 0 |
| Role followed by a capitalised name (TA, instructor, lecturer, faculty, "prepared by", student) | 0. "TA" appears only as a source name ("Milling TA slides"), never with a person. |
| Capitalised word pairs not at sentence start | Only technical phrases ("Light Amplification", "Stimulated Emission") and the publication "Laser Focus World" |

Named people that do appear are only published textbook authors used as theory references (Hajra Choudhury, Kalpakjian, P.K. Mishra, P.N. Rao, Callister, Dini, B.S. Raghuwanshi). These are bibliographic citations, not personal data. No lecturer, TA, lab staff or student name from the slides or log sheets appears anywhere.

---
## Fixes applied by the author
- Dropped cross-shop duplicates (20 questions):
  - supervision, accessories, long hair and eye-protection copies in grinding/milling;
  - chip-removal copies in lathe/shaping/milling;
  - stop-before-measuring copies in lathe/milling;
  - loose-clothing (lathe), chuck key and motto (safety);
  - rake angle (SHP-0051), tang (LAT-0073), caliper transfer (LAT-0063);
  - dress-precaution copies in fitting/shaping/milling.

  Their facts are now cited by the surviving question, and fact coverage is still 100%.
- Difficulty rules applied bank-wide:
  - "name the part" / "which label" figure look-ups = easy;
  - numerical/sequence questions that combine 3+ facts = hard.

  The mix is now 40/46/14.
- Electroplating:
  - The Faraday numerical now uses 6 A (inside both lab ranges).
  - ELP-F049 now separates 5 A (log sheet) from 5 A/sq ft (board current density).
  - corrections.md #20 rewritten.
- MIL-0138 reworded to "tooth spaces cut (one per indexing position)".
- Tap-drill explanation now notes it is a rule of thumb, distinct from the lathe core-diameter formula.
- Not changed: MIL-0116 (addendum question). 0.125 in is a valid distractor there; it is not a lab-depth question.
