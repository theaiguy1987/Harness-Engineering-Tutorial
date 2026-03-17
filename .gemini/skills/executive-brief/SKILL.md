---
name: executive-brief
description: >
  Generates a PowerPoint presentation from a financial analysis markdown file.
  Use this skill when asked to create slides, a presentation, or an executive
  brief deck from the Volvo Q4 2025 analysis. Runs the bundled Python script
  to produce a .pptx file.
---

# Executive Brief Presentation Skill

## What to do

Take the financial analysis (`financial-analysis.md`) produced by the `financial-analysis` skill
and convert it into a slide-ready PowerPoint presentation.

If `financial-analysis.md` does not exist, first activate the `financial-analysis` skill to generate it.

Run the bundled script from the project root:

```bash
python .gemini/skills/executive-brief/scripts/create_pptx.py financial-analysis.md executive-brief.pptx
```

The script will:
1. Read the markdown analysis file
2. Parse each `##` heading into a separate slide
3. Convert bullet points into slide content
4. Apply a clean, professional layout
5. Output a `.pptx` file ready for presentation

---

## Slide design rules

- **Title slide**: "Volvo Group — Q4 & Full Year 2025 Executive Brief"
- **One slide per section** from the analysis (6 content slides)
- **Bullet points only** — no paragraphs on slides
- **Max 6 bullets per slide** — if more, split or summarize
- **Font**: Use clean sans-serif (Calibri)
- **Highlight declines >20%** with red text where flagged with ⚠️
- **Final slide**: "Key Takeaway" — one sentence summary

---

## Output

- Default output file: `executive-brief.pptx`
- The presentation should have 7-8 slides total (title + 6 content + takeaway)

---

## Requirements

- Python 3.8+
- `python-pptx` package (`pip install python-pptx`)
