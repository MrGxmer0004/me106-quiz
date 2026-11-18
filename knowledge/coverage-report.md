# Phase 1 coverage report

## 1. File inventory

| File | Type | Pages/slides | Text layer | Duplicate? | Read how |
|---|---|---|---|---|---|
| Log Sheets ME-106.pdf | scanned log sheets | 9 | garbage OCR | = Log Sheets.pdf (md5 match) | visually, 150 dpi; pp.5–6 CNC/3D skipped |
| Log Sheets.pdf | — | 9 | — | duplicate | skipped |
| Central Lathe Log sheet.pdf | phone photo | 2 | no | unique (2025 lathe sheet) | visually |
| Central Lathe Diagram.jpg | blackboard photo | 1 | — | unique | visually |
| Centre Lathe.pdf | photos of printed handout | 14 | no | unique (p.14 repeats p.2) | visually |
| Central Lathe..pdf | lecture screenshots | 27 | no | unique | visually |
| Manufacturing_Notes_2023.pdf | handwritten notebook | 36 | no | unique | pp.1–22 fully; pp.23–36 confirmed CNC/3D (out of scope) |
| Milling.pdf | lecture screenshots (rotated) | 28 | no | unique | visually |
| Milling TA.pptx | slides | 19 | yes | Milling TA.key = Keynote copy | text + all images; .key skipped |
| Milling Formula_.jpg / Milling Lab_.jpg / Milling Tools.jpg | photos | 1 each | — | unique | visually (board zoomed) |
| Milling Log Sheet #1.jpg / #2.jpg | photos | 1 each | — | unique (2025 sheet) | visually |
| Grinding Lab.pdf | lecture slides | 9 | partial | unique | text + visually |
| Grinding pdf.pdf | slides | 12 | partial | unique | text + visually |
| Cylindrical grinding.pdf | notes | 8 | yes | unique | text + visual check |
| GrindingPPT.pptx (60 MB) | slides | 18 | yes | unique | text + all 7 images |
| Grinding Ratio.jpg | blackboard photo | 1 | — | unique | visually |
| shaping.pdf | slides | 12 | partial | unique | text + visually |
| Shaping Workshop.jpg | wall-chart photo | 1 | — | unique | visually |
| Fitting lab lecture final.pptx | slides | 16 | yes | unique | text + all images |
| Electroplating.pdf | lecture screenshots | 12 | no | = Electroplating for workshop practice.pdf (md5 match) | visually |
| Electroplating Lab.jpg / Electroplating Log Sheet.jpg | photos | 1 each | — | unique | visually (board zoomed) |
| Unconventional.pdf | log sheet | 2 | no | unique | visually |

Nothing was unreadable. Partly illegible items are listed in §4.

## 2. Coverage by shop × topic

Ratings: **S** = strong (lab sources cover it well), **T** = thin (lab sources only touch it; filled from theory), **M** = missing from lab sources (all from theory), — = not applicable.

| Topic | Lathe | Milling | Grinding | Shaping | Fitting | Electroplating | Unconventional | Safety |
|---|---|---|---|---|---|---|---|---|
| Machine & parts | S | S | S | S | T (vice only) | S (cell) | M | — |
| Tools & equipment | S | S | S | S | S | S | S (EDM list) | — |
| Workpiece / tool material | S | S (Al blank, HSS) | S | S | T (MS plate) | S | M | — |
| Job & dimensions | S | S | T (no dimensions) | S | **M (no drawing)** | T (no dimensions) | T (square only; ring has no dimensions) | — |
| Procedure | S | S | S | S | S | S | S | — |
| Precautions | S | S | S | S | S | S | S | S |
| Principle / theory | S | S | S | S | T | S | **M** | — |
| Formulas / numericals | S | S | S | T | M (Vernier/micrometer) | S (Faraday) | M (kerf) | — |
| Classifications | S | S | S | S | T | — | M | — |
| Advantages / limitations | T | S | S | M | — | T | M | — |
| Applications | T | T | S | T | S | M | M | — |

### What was filled from theory
- **Unconventional:** all principle, parameters, materials, advantages, limitations and laser/EDM theory (49 of 84 facts). I checked the main points against web sources (deionised water and brass wire 0.05–0.3 mm; servo gap about 0.05 mm; fiber laser 1.06 µm vs CO₂ 10.6 µm; O₂ for mild steel and N₂ for stainless; classification by energy type).
- **Fitting:** marking, measuring and cutting tools, files, hacksaw, taps and dies, hammers, Vernier and micrometer (45 of 92 facts), from Hajra Choudhury Vol. I.
- **Milling:** gear proportions (addendum, dedendum, module, circular pitch) and gear types.
- **Electroplating:** Faraday's-law numericals, defects, the industrial process sequence.
- **Lathe / shaping / grinding:** a few gaps (cutting speed formula, rake and clearance, glazing vs loading, wheel safety).

## 3. Fact counts

| File | Facts | Lab-sourced | Theory-only |
|---|---|---|---|
| lathe.md | 132 | 116 | 16 |
| milling.md | 121 | 103 | 18 |
| grinding.md | 106 | 98 | 8 |
| shaping.md | 67 | 58 | 9 |
| fitting.md | 91 | 46 | 45 |
| electroplating.md | 79 | 67 | 12 |
| unconventional.md | 84 | 35 | 49 |
| general-safety.md | 25 | 18 | 7 |
| **Total** | **705** | **541** | **164** |

## 4. Decisions (confirmed by you)
1. **Lathe job = 2025 drawing**: Ø38 × 35 (1 × 45° chamfer) → taper 38→34 over 30 → groove 5 → Ø34 × 1.5 thread, 25 long → Ø32 × 20; 115 overall. The 2022 drawing has been removed from the KB.
2. **Milling gear = 22 teeth**: OD 1½ in, DP 16 → 40/22 = 1 turn + 27 holes on the 33-hole circle. The 14-tooth case (OD 1 in) stays only as a practice numerical.
3. **"Working depth = 2.157/DP"**: lab questions use the lab's name, with an explanation note, and never offer 2/DP as a distractor. Separate theory questions teach whole depth (2.157/DP) vs working depth (2/DP).
4. **Notebook p.20 tool list**: the shop is uncertain, so it is not attributed to either one. Fitting tools come from the fitting PPT plus theory.

## 5. Still open (left out of questions until you supply them)
- Fitting job drawing and dimensions: there is no fitting log sheet or drawing in the files.
- Laser ring dimensions: the log sheet shows only the shape.
- Shaping job 73 × 38 × 21 mm: this comes from the 2022 sheet only. It is used as the lab job unless you say it changed.
- Illegible items not used: the grade letter in "C 32 _ 8 B"; "sulbo catalyst?" in the grinding coolant entry; the nickel salt names on the electroplating board.
