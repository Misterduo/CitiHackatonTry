import qrcode
import qrlink

def generate(text, passw):

    link = qrlink.gen(text, passw)
    img = qrcode.make(link)
    img.save("qrstored"+"\\"+"qrimage"+".Bmp")
    return link