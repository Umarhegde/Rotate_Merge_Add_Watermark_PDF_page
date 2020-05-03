# Merge PDFs

from PyPDF2 import PdfFileMerger
import sys

input = sys.argv[1:]

merger = PdfFileMerger()

for pdf in input:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
