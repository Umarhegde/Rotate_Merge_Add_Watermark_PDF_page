# Rotate PDF page

import PyPDF2

with open("PDF_1.pdf", 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('rotate_pdf.pdf', 'wb') as new_file:
        writer.write(new_file)
