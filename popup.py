from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
def clicked():
    res = messagebox.askokcancel('Message title','Message content')
    # messagebox.showinfo('Message title', 'Message content')
    # messagebox.showwarning('Message title', 'Message content')  #shows warning message
    # messagebox.showerror('Message title', 'Message content')    #shows error message
    # res = messagebox.askquestion('Message title','Message content')
    # res = messagebox.askyesno('Message title','Message content')
    # res = messagebox.askyesnocancel('Message title','Message content')
    # res = messagebox.askokcancel('Message title','Message content')
    # If you click OK or yes or retry, it will return True value, but if you choose no or cancel, it will return False.

btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)
window.mainloop()