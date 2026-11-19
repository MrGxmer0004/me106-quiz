# ME-106 Workshop Quiz

A static practice-quiz website for **ME-106 Workshop Practice** at IIT (BHU). It covers the six syllabus activities: centre lathe, milling, fitting & electroplating, shaping, grinding, and unconventional machining (wire-cut EDM and fiber laser), plus general workshop safety.

- About 1,360 MCQs across 8 shops. Each question is tagged with shop, category, difficulty, type, and **lab** or **theory** source.
- 85 original SVG figures, including generated Vernier caliper and micrometer reading figures. More than 400 questions use a figure.
- Practice mode (instant feedback) and test mode (optional timer, full review at the end).
- Progress, "previously wrong" and bookmarks are stored in your browser (`localStorage`). There is no login and no backend.
- An **Essentials** set (143 questions, 10–24 per shop): simple single-answer MCQs on the practical basics (parts, tools, materials, the lab job, procedure, precautions). Pick it under "Question set" on the setup page.
- A **Revise** page with clean notes for each shop and a figure gallery listing every label.

## Run locally

```bash
npm i
npm run dev
```

Then open the URL Vite prints (usually http://localhost:5173).

## Project layout

```
knowledge/*.md              Fact base, one file per shop. Every fact has an ID (e.g. LAT-F001) and a source tag.
knowledge/coverage-report.md  What the source files covered and what was filled from standard textbooks.
corrections.md              Errors found in the class notes/boards, and what the bank uses instead.
src/data/questions/*.json   The question bank (canonical data used by the site).
src/data/figures.json       Figure registry: id, title, alt, and letter → part/function/fact for every label.
public/figures/<shop>/*.svg Original line-diagram figures (strokes use currentColor, so they follow dark mode).
authoring/*.py              Scripts that generate each shop's JSON (correct option written first; positions balanced).
authoring/fix_<shop>.py     Distractor/label patches applied on top of the authoring scripts.
scripts/figures/*.py        Figure source code (python3 scripts/figures/build.py [shop ...]).
scripts/validate.js         Validator; `npm run build` runs it first.
review/*.md                 Independent review reports for each shop and the cross-shop review, with the fixes applied.
```

## Adding or editing questions

Each entry in `src/data/questions/<shop>.json` looks like this:

```json
{
  "id": "LAT-0001",
  "shop": "lathe",
  "category": "machine-parts",
  "difficulty": "easy",
  "type": "mcq",
  "question": "Which part of a centre lathe holds the live centre?",
  "options": ["Headstock", "Tailstock", "Carriage", "Apron"],
  "answer": 0,
  "explanation": "The live centre sits in the headstock spindle…",
  "source": "lab",
  "ref": "Centre Lathe lecture slide 14",
  "tags": [],
  "facts": ["LAT-F020"]
}
```

- `type` is one of: `mcq` | `true-false` | `numerical` | `sequence` | `assertion-reason` | `diagram`. True/false uses `["True", "False"]`.
- `answer` is the **0-based index** of the correct option. Options are shuffled at quiz time unless `"keepOrder": true`.
- `facts` must list existing fact IDs from `knowledge/*.md`.
- Diagram questions add `"figure": "lathe/lathe-overview"`. Questions that point at a letter also add `"label": "C"`.
- Do not use "All/None of the above".

You can edit the JSON directly for small fixes. If you re-run `python3 authoring/<shop>.py`, that shop's JSON is regenerated from the authoring script, so put lasting changes there or in `authoring/fix_<shop>.py`.

After regenerating any shop's JSON, re-run `python3 authoring/essentials.py` so the Essentials list (`src/data/essentials.json`) points at the right IDs. The validator stops the build if it is out of date.

Always check your changes with:

```bash
npm run validate
```

The validator checks:
- IDs, required fields and enums;
- options, the answer index, duplicate options and "all/none of the above";
- near-duplicate questions;
- fact references and coverage (zero uncovered lab facts allowed);
- that every figure exists and that registry letters match the letters drawn;
- that "what is label X" keys equal the registry part name.

It also prints count matrices (shop × category, type and difficulty) and the answer-position balance.

To rebuild figures (needs `rsvg-convert` from librsvg for the PNG previews in `.render/`):

```bash
python3 scripts/figures/build.py lathe
```

## Deploy (Vercel)

1. Create an empty GitHub repository and push this folder to it (see below).
2. On vercel.com, choose **Add New → Project**, then import the repository.
3. Set Framework preset: **Vite**. The build command `npm run build` and output directory `dist` are detected automatically.
4. Click **Deploy**.

`npm run build` runs the validator first, so a broken question never ships.

## Notes

- Source lecture files, log sheets and photos are **not** in this repository (copyright and personal data); `.gitignore` blocks PDFs, PPTX, KEY and images.
- Questions may contain errors. Use **Report issue** on the quiz screen: it copies the question ID and text to your clipboard.
