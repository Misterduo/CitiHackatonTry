import pdffile
import random

def gen(text, passw):

    unique_id = random.choice(range(1, 100000))
    url = pdffile.make_pdfile(text, unique_id, passw)
    return url