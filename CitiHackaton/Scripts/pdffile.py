from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import sharefile

def make_pdfile(text, unique_id, passw):

    packet=io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(10, 550, str(text))
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    existing_pdf = PdfFileReader(open("download.pdf", "rb"))
    output = PdfFileWriter()

    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    output_name = "database"+"\\"+"protected"+str(unique_id)+".pdf"
    outputStream = open(output_name, "wb")
    output.encrypt(passw, use_128bit=True)
    output.write(outputStream)
    outputStream.close()

    url = sharefile.upload(output_name, "/"+"protected"+str(unique_id)+".pdf")
    return url