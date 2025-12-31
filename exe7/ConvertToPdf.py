import markdown
import pdfkit
from pathlib import Path

md_path = Path("example.md")
html_path = Path("temp.html")
pdf_path = Path("output.pdf")

md_text = md_path.read_text(encoding="utf-8")

html = markdown.markdown(md_text)

html_path.write_text(html, encoding="utf-8")

config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

pdfkit.from_file(str(html_path), str(pdf_path), configuration=config)

print("PDF created successfully!")
