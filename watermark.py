import sys
from pathlib import Path
from typing import Union, Literal, List
from PyPDF2 import PdfWriter, PdfReader


if len(sys.argv) < 2:
    print('Error: Please provide at least 1 PDF to watermark')
    sys.exit(1)


# Function straight from th PyPDF2 docs
def watermark(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0] # This is a ref to an object!

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)


stamp_pdf = Path('wtr.pdf')

for pdf in sys.argv[1:]:
    content_pdf = Path(pdf)
    result_pdf = Path(content_pdf.stem + '_wtr.pdf')
    watermark(content_pdf, stamp_pdf, result_pdf, 'ALL')
