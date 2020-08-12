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
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=3, row=0)
rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=4)
rad2.grid(column=1, row=4)
rad3.grid(column=2, row=4)

window.mainloop()