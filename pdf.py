import sys
from pathlib import Path
import PyPDF2

if len(sys.argv) < 3:
    print('Error: Please provide at least 2 PDFs to merge')
    sys.exit(1)

merged_path = Path('merged.pdf')
with PyPDF2.PdfMerger(fileobj=merged_path) as pdf_merger:
    for pdf_path in sys.argv[1:]:
        pdf = Path(pdf_path)
        if pdf.is_file():
            pdf_merger.append(pdf)


# with open('twopage.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     page = reader.pages[0].rotate(180)

#     with open('my_pdf.pdf', 'wb') as pdf:
#         writer = PyPDF2.PdfWriter()
#         writer.add_page(page)
#         writer.add_page(reader.pages[1])
#         writer.write(pdf)
