import PyPDF2

PdfFiles = ["1.pdf","2.pdf"]
merge = PyPDF2.PdfMerger()
for file in PdfFiles:
    PdfFile = open(file , "rb")
    PdfReader = PyPDF2.PdfReader(PdfFile)
    merge.append(PdfReader)
PdfFile.close()
merge.write('merged.pdf')