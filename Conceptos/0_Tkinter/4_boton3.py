#este es para cuando el el raton pase se seleccione jajaja


# importa el modulo de tkinter
from tkinter import *

from tkinter.ttk import *

#crea el objeto
root = Tk()

# inicializa la ventana de tkinter con dimensiones 100X100

root.geometry('100x100')

btn = Button (root,text = "Dame click soy un boton",command=root.destroy)

#coloca la posicion del el botom en la cima de la ventana
btn.pack(side="top")

root.mainloop()