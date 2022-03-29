import PyPDF2
with open("D:\\pdf_python\\dummy .pdf", "rb") as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)      # rotating the page
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    print(reader.numPages)           # printing the number of pages
    with open("D:\\pdf_python\\rotated .pdf", "wb") as n_file:
        writer.write(n_file)
