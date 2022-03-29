import PyPDF2
a = ["D:\\pdf_python\\dummy .pdf", "D:\\pdf_python\\twopage.pdf"]
def merge(l1):
    merger = PyPDF2.PdfFileMerger()   # merging two or more pdf
    for i in l1:
        merger.append(i)
        print(i)
    merger.write("super.pdf")
merge(a)
