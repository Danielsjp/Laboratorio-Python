from tkinter import *
import smtplib
# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
sender = "from@smtp.mailtrap.io"
receiver = "to@smtp.mailtrap.io"
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
##txt = Entry(window,width=10)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
message = f"""\
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}
    This is a test e-mail message."""
def clicked(sender,receiver,message):
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("f836c4ea30bc62", "5f2bfb059db3e9")
        server.sendmail(sender, receiver, message)
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()