import tkinter as tk
from tkinter import *
from tkinter import messagebox
from mainfile import start

def createWidgets():

    logo = PhotoImage(file="qrstored"+"\\"+"FOP_30"+".png")

    qr_logo = Label(root, image=logo)
    qr_logo.image = logo
    qr_logo.grid(row=0, column=1, pady=7, padx=30)

    intro_text1 = Label(root, text="Welcome to FOP!", bg="#FFFFFF")
    intro_text1.grid(row=1, column=1, pady=7, padx=80)

    intro_text2 = Label(root, text="Please fill in your payment information", bg="#FFFFFF")
    intro_text2.grid(row=2, column=1, pady=20, padx=0)

    text_label = Label(root, text="Enter Name/Surname: ", bg="#FFFFFF")
    text_label.grid(row=3, column=0, pady=10, padx=40)

    root.text_entry1 = Entry(root, width=65, textvariable=output)
    root.text_entry1.grid(row=3, column=1, pady=7)

    bank_account_label = Label(root, text="Enter your bank account number: ", bg="#FFFFFF")
    bank_account_label.grid(row=4, column=0, pady=10, padx=40)

    root.text_entry2 = Entry(root, width=65, textvariable=bank_account)
    root.text_entry2.grid(row=4, column=1, pady=7)

    code_label = Label(root, text="Choose the QR Code type: ", bg="#FFFFFF")
    code_label.grid(row=5, column=0, pady=10, padx=40)

    root.text_entry3 = Entry(root, width=65, textvariable=code_type)
    root.text_entry3.grid(row=5, column=1, pady=7)

    passwd_label = Label(root, text="Enter the QR code password: ", bg="#FFFFFF")
    passwd_label.grid(row=6, column=0, pady=10, padx=40)

    root.text_entry2 = Entry(root, width=65, textvariable=passw)
    root.text_entry2.grid(row=6, column=1, pady=7)

    gen_but = Button(root, text="Generate QR code", command=show_qr, width=15, bg="#E6E6FA")
    gen_but.grid(row=7, column=1, pady=7)

def show_qr():

    qr_text = Label(root, text="The QR code with payment information is saved", bg="white")
    qr_text.grid(row=8, column=0, pady=7, padx=30)

    link = start(output.get(), passw.get())
    photo = PhotoImage(file="qrstored"+"\\"+"qrimage"+".Bmp")

    qr_pic = Label(root, image=photo)
    qr_pic.image = photo
    qr_pic.grid(row=8, column=1, pady=7, padx=30)

    share_text = Label(root, text="Or copy the following link: ", bg="#FFFFFF")
    share_text.grid(row=9, column=0, pady=7, padx=30)

    share_link = Text(root, width=60, height=2)
    share_link.insert(END, link)
    share_link.grid(row=9, column=1, pady=7)

    messagebox.showinfo("Success!", "Hey! QR code generated at \qrstored\grimage.Bmp")

root = tk.Tk()

root.title("FOP: Digital invoice generator")
root.geometry("720x1280")
root.config(background="#FFFFFF")

output=StringVar()
bank_account=IntVar()
code_type=StringVar()
passw=StringVar()

createWidgets()

root.mainloop()