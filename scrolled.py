from tkinter import *

from tkinter import scrolledtext

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

txt = scrolledtext.ScrolledText(window,width=40,height=10)

txt.insert(INSERT,'You text goes here')

txt.grid(column=0,row=0)

def clicked():

    txt.delete(1.0,END)

btn = Button(window, text="Delete", command=clicked)

btn.grid(column=0, row=10)

window.mainloop()