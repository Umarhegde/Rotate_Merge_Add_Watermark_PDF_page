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
