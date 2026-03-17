"""
parse_pdf.py — Extract text and tables from a PDF into structured markdown.

Usage:
    python parse_pdf.py <input.pdf> [output.md]

Requires: pdfplumber (pip install pdfplumber)
"""

import sys
import os

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber is not installed. Run: pip install pdfplumber")
    sys.exit(1)


def extract_pdf_to_markdown(pdf_path: str, output_path: str) -> None:
    if not os.path.isfile(pdf_path):
        print(f"Error: File not found: {pdf_path}")
        sys.exit(1)

    lines: list[str] = []
    lines.append(f"# Parsed Report: {os.path.basename(pdf_path)}\n")

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"Parsing {total_pages} pages from {pdf_path}...")

        for i, page in enumerate(pdf.pages, start=1):
            lines.append(f"\n---\n\n## Page {i}\n")

            # Try to extract tables first
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    if not table:
                        continue
                    # Build markdown table
                    header = table[0]
                    lines.append(
                        "| " + " | ".join(str(c or "") for c in header) + " |"
                    )
                    lines.append(
                        "| " + " | ".join("---" for _ in header) + " |"
                    )
                    for row in table[1:]:
                        lines.append(
                            "| " + " | ".join(str(c or "") for c in row) + " |"
                        )
                    lines.append("")

            # Also extract full text for non-table content
            text = page.extract_text()
            if text:
                lines.append(text)
                lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Done. Output written to {output_path} ({total_pages} pages)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_pdf.py <input.pdf> [output.md]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "parsed-report.md"
    extract_pdf_to_markdown(input_file, output_file)
