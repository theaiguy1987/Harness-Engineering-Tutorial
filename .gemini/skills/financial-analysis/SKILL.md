---
name: financial-analysis
description: >
  Analyzes parsed financial report content from a Volvo Group quarterly report.
  Use this skill when asked to summarize, analyze, or extract financial insights
  from the Volvo Q4 2025 report. Reads the parsed markdown (from pdf-parser)
  and produces a structured financial analysis saved as financial-analysis.md.
---

# Financial Analysis Skill

## What to do

Read the parsed report file (`parsed-report.md`) produced by the `pdf-parser` skill.
If `parsed-report.md` does not exist, first activate the `pdf-parser` skill to generate it.

Analyze the content and produce a structured financial analysis. Save the output as `financial-analysis.md`.

---

## Structure of the analysis

Produce the following sections in this order:

- Headline snapshot - The 3 most important things to know about Q4 and Full Year 2025
2. **Revenue performance** - How did net sales move vs last year? Which regions grew or declined?
3. **Profitability** - Operating margins and income, what drove the changes
4. **Segment breakdown** - How did Trucks, Construction Equipment, Buses, Volvo Penta, and Financial Services each perform?
5. **Risks and headwinds** - What pressures did management flag?
6. **Outlook for 2026** - What does the report say about what comes next?

---

## Rules for every section

- Always compare 2025 figures to 2024 (year-on-year context is mandatory)
- Use bullet points, not paragraphs
- Flag any figure that declined more than 20% year-on-year with [WARNING]
- Keep the entire analysis under 300 words
- End each section with one "So what?" sentence in italics
- All figures in SEK unless stated otherwise
- Cite page numbers from the parsed report where key figures were found

---

## Key metrics to look for

When reading the parsed report, prioritize extracting these data points:

| Metric | Where to look |
|--------|---------------|
| Net sales (Q4 and FY) | Income statement / financial summary |
| Adjusted operating income | Income statement |
| Adjusted operating margin | Income statement |
| Order intake by segment | Segment reporting pages |
| Deliveries by segment | Segment reporting pages |
| EPS (earnings per share) | Per-share data |
| Proposed dividend | Board proposal section |
| Net financial position | Balance sheet summary |
| Regional sales breakdown | Geographic reporting |
| Truck deliveries by market | Truck segment detail |

---

## About me

[BLANK - add your details here to personalize the analysis]

#
