import PyPDF2

with open("dummy.pdf", "rb") as dummy_file:
    file = PyPDF2.PdfFileReader(dummy_file)
    print(file)
