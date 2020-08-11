from tkinter import *

window = Tk()

window.title("Ejemplo Formulario")

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

window.geometry('350x200')

def clicked():

    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)

## Boton con Colores
## btn = Button(window, text="Click Me", bg="orange", fg="red")

btn.grid(column=1, row=0)

window.mainloop()