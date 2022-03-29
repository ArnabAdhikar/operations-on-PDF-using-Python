# watermark on the first page only
# run the code in a new project
import PyPDF2
a = PyPDF2.PdfFileReader(open("twopage.pdf", "rb"))
b = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
c = PyPDF2.PdfFileWriter()     # creating a writer object
for i in range(a.getNumPages()):
    page = a.getPage(i)
    page.mergePage(b.getPage(0))
    c.addPage(page)
    with open("super_water.pdf", 'wb') as f1:
        c.write(f1)    # write all the data stored in c to the f1.
