from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
def clicked():
    # messagebox.showinfo('Message title', 'Message content')
    # messagebox.showwarning('Message title', 'Message content')  #shows warning message
    messagebox.showerror('Message title', 'Message content')    #shows error message
btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)
window.mainloop()