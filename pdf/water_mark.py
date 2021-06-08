import PyPDF2

with open("dummy.pdf", "rb") as dummy_file, open("wtr.pdf", "rb") as watermark_file:
    template = PyPDF2.PdfFileReader(dummy_file)
    watermark = PyPDF2.PdfFileReader(watermark_file)
    output = PyPDF2.PdfFileWriter()

    page = template.getPage(0)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open("merged_file.pdf", "wb") as file:
        output.write(file)
