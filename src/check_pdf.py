from pathlib import Path
from pypdf import PdfReader

for path in sorted(Path("data").iterdir()):
    print("-" * 60)
    print(path.name)
    if path.suffix.lower() != ".pdf":
        print("  NOT a .pdf file -> re-download it as a PDF")
        continue
    try:
        reader = PdfReader(path)
        pages = len(reader.pages)
        first = reader.pages[0].extract_text() or ""
        middle = reader.pages[pages // 2].extract_text() or ""
        print(f"  pages: {pages} | first-page chars: {len(first)} | middle-page chars: {len(middle)}")
        print("  preview:", first[:150].replace("\n", " "))
    except Exception as e:
        print("  ERROR:", e)