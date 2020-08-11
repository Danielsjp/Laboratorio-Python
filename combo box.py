from tkinter import *
from tkinter.ttk import *
import random
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
combo = Combobox(window)
valores = [1, 2, 3, 4, 5, "Text"]
hola = random.choice(valores)
combo['values']= valores
combo.current(hola) #set the random value
combo.grid(column=0, row=0)
lbl = Label(text="Default"+combo.get())
lbl.grid(column=0, row=3)
window.mainloop()