#cierra el menu de tkinter

from tkinter import *

root = Tk()

root.geometry('100x100')

btn = Button(root,text="Dame click Para cerrar ",bd = '5',
                        command= root.destroy)

btn.pack(side='top')
root.mainloop()

