# watermark on the first page only
import PyPDF2
input_f = "D:\\pdf_python\\super.pdf"
water = "D:\\pdf_python\\wtr.pdf"
out_f = "D:\\pdf_python\\super_water.pdf"
with open(input_f, "rb") as f1:
    pdf = PyPDF2.PdfFileReader(f1)
    with open(water, "rb") as f2:
        watermark = PyPDF2.PdfFileReader(f2)
        first_page = pdf.getPage(0)
        first_page_watermark = watermark.getPage(0)
        first_page.mergePage(first_page_watermark)
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(first_page)
        with open(out_f, "wb") as filehandle_output:
            pdf_writer.write(filehandle_output)
