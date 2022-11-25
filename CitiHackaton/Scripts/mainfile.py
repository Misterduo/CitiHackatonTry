import qr_gen

def start(text, passw):

    link = qr_gen.generate(text, passw)
    return link
