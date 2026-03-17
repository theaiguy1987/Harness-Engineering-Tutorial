---
name: pdf-parser
description: >
  Parses PDF files and extracts text content into structured markdown.
  Use this skill when asked to read, parse, or extract text from the
  Volvo Q4 2025 PDF report. Runs the bundled Python script to produce
  a clean markdown file that downstream skills can consume.
---

# PDF Parser

## What to do

Use the bundled `scripts/parse_pdf.py` script to extract all text content from a PDF file.

Run the script from the project root:

```bash
python .gemini/skills/pdf-parser/scripts/parse_pdf.py volvo-group-q4-2025-eng.pdf parsed-report.md
```

The script will:
1. Read every page of the PDF
2. Extract text content (including tables where possible)
3. Output a structured markdown file with page separators

## When to use

- Before any financial analysis or summarization task
- When the user asks to "read", "parse", or "extract" the PDF
- As the first step in any multi-skill workflow involving the Volvo report

## Output

- The script produces a markdown file (default: `parsed-report.md`)
- Each page is separated by a heading indicating the page number
- Tables are preserved in markdown table format where detected

## Requirements

- Python 3.8+
- `pdfplumber` package (`pip install pdfplumber`)
