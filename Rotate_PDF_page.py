# Rotate PDF page

# import PyPDF2

# with open("PDF_1.pdf", 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('rotate_pdf.pdf', 'wb') as new_file:
#         writer.write(new_file)

# Merge PDFs

# from PyPDF2 import PdfFileMerger
# import sys

# input = sys.argv[1:]

# merger = PdfFileMerger()

# for pdf in input:
#     merger.append(pdf)

# merger.write("result.pdf")
# merger.close()


# Input of watermark in all page

import PyPDF2

pdf_page = PyPDF2.PdfFileReader(open('result.pdf', 'rb'))
watermark_page = PyPDF2.PdfFileReader(open('WATERMARK_PDF.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(pdf_page.getNumPages()):
    page = pdf_page.getPage(i)
    page.mergePage(watermark_page.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
