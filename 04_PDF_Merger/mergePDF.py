

# ----------  Python Project 4: PDF Merger  ---------------


import PyPDF2

pdfFiles = ["File1.pdf", "File2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdfFiles:
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()

merger.write('merged.pdf')