# GEMINI.md
> This file is the agent's map for this repository.
> Everything Gemini needs to know about this project lives here.

---

## Getting started

Welcome. You have just loaded the context for a hands-on Harness Engineering exercise.

### Step 0 — Environment setup (do this first, every time)

Before running any skill, ensure the Python virtual environment `demo-venv` is active.
**Run this check immediately when you load this file:**

```bash
# If demo-venv does not exist — create it and install dependencies
python -m venv demo-venv
demo-venv\Scripts\activate        # Windows
# source demo-venv/bin/activate   # macOS / Linux
pip install -r requirements.txt

# If demo-venv already exists — just activate it
demo-venv\Scripts\activate        # Windows
# source demo-venv/bin/activate   # macOS / Linux
```

> **Agent instruction:** On startup, check whether `demo-venv` exists in the project root.
> If it does not exist, create it and install `requirements.txt`. If it exists, activate it.
> Do not proceed with any skill until the environment is confirmed active.

---

Here is what is available to you in this project:

- A real financial report: `volvo-group-q4-2025-eng.pdf`
- Three agent skills already installed in `.gemini/skills/`:
  - `pdf-parser` — reads and extracts the PDF into structured markdown
  - `financial-analysis` — analyzes the extracted content and produces a brief
  - `executive-brief` — turns the analysis into a PowerPoint presentation

**The natural next step is to run the full pipeline.** You can do this with a single prompt:

> Parse the Volvo Q4 2025 PDF, then run the financial analysis, then create the executive brief presentation.

Gemini will activate each skill in sequence and produce three output files:
`parsed-report.md` → `financial-analysis.md` → `executive-brief.pptx`

Once you have the output, open `financial-analysis.md` and read it.
Ask yourself: does the analysis reflect *your* perspective and priorities?
If not, open `.gemini/skills/financial-analysis/SKILL.md`, fill in the **About me** section, and re-run.
That loop — run, review, refine, re-run — is the core of harness engineering.

---

## What this project is

This repository contains the Volvo Group Q4 and Full Year 2025 financial report (`volvo-group-q4-2025-eng.pdf`).

The goal of this project is to analyze that report and produce a **slide-ready executive brief** — a structured, clear, concise summary of the most important findings, suitable for presentation to a non-specialist audience.

---

## The source document

**File:** `volvo-group-q4-2025-eng.pdf`
**Publisher:** AB Volvo (publ)
**Period covered:** Q4 2025 and Full Year 2025
**Released:** January 28, 2026

The report covers five business segments:
- **Trucks** — the largest segment by revenue (SEK 323.5 bn full year)
- **Construction Equipment** — includes Volvo CE; SDLG was divested in September 2025
- **Buses** — smaller segment, showing recovery signals
- **Volvo Penta** — engines for marine and industrial use; standout margin performer
- **Financial Services** — captive finance arm; growing portfolio but rising credit provisions

Key figures to be aware of:
- Full year net sales: SEK 479.2 billion (vs 526.8 in 2024) — a 9% decline
- Full year adjusted operating income: SEK 51.2 billion (vs 65.7) — a 22% decline
- Full year adjusted operating margin: 10.7% (vs 12.5%)
- Q4 net sales: SEK 123.8 billion (vs 138.4)
- Q4 adjusted operating margin: 10.3% (vs 10.1%) — actually improved year-on-year
- Earnings per share (full year): SEK 16.94 (vs 24.78)
- Proposed dividend: SEK 8.50 ordinary + SEK 4.50 extra per share
- Net financial position (Industrial Operations): SEK 63.0 billion

---

## Output rules

All outputs produced in this project must follow these rules:

1. **Format:** Markdown (`.md`) unless otherwise instructed
2. **Length:** Executive brief — concise and scannable. No walls of text.
3. **Structure:** Use clear headings. Every section should be independently readable.
4. **Numbers:** Always cite figures directly from the PDF. Do not estimate or invent.
5. **Comparisons:** Always show year-on-year context (2025 vs 2024) when quoting a number.
6. **Tone:** Professional but plain. Avoid jargon. Write as if the reader is intelligent but not a financial analyst.
7. **Currency:** All figures are in SEK (Swedish Kronor) unless stated otherwise.
8. **Slide-readiness:** Every section should be translatable into a single slide. Bullet points preferred over paragraphs.

---

## What this project is NOT

- This is not a full audit or detailed accounting exercise
- Do not reproduce the entire report — synthesize and select
- Do not speculate about future performance beyond what the report itself states

---

## How to reference the document

When Gemini reads the PDF, treat it as the single source of truth.
If something is unclear or missing from the PDF, say so explicitly — do not fill gaps with assumptions.
