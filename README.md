# CitiHackatonTry
This repository consists of the code used to try and create a prototype for Citi Hackaton.
I have tried to create a small environment, where the user would input the data needed to create the "digital invoice" - the file to start the program is called the "startfile.py", located in CitiHackaton/Scripts/startfile.py.
The interface and the initial parts of the code work according to plan, but I have faced an error that I didn't manage to correct in time.
To recreate the closest to the real experience, I decided to try and connect our inputs to the code generator, which would afterward connect to the API Server in order to have the information located on the 'firm's database'. After the dropbox connection, the code is supposed to generate a code to access the server, where the program will show the details, and the ar reader on the app would identify the inputs shown and use the given information to have the payment ready, thus reducing time and effort of the real people (only PIN, and password if used by the code creator for protection).
Unfortunately, due to time constraints, and unforeseen circumstances, the final API connection error remains, therefore the final step is not achievable at this prototype version (error resides in the sharedfile.py).

The following libraries were used in python code writing: tkinter, qrcode, random, reportlab, PyPDF2, sys, dropbox.

Thank you for your time and attention!
