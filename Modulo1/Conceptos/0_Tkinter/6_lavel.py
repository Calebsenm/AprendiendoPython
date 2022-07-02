from doctest import master
#importa el modulo de tkinder
from tkinter import *
#de tkinder.ttk import *

#creacions de la ventana master Tkinder
master = Tk()
master.geometry("175x175")
#variables de string tkinter
#puede alamacenar el valor de una cadena


v = StringVar(master, "1")

#Diccionario que creará multiples botones 

values = {

    "RadioButtom 1" : "1",
    "RadioButtom 2" : "2",
    "RadioButtom 3" : "3",
    "RadioButtom 4" : "4",
    "RadioButtom 5" : "5",
}

#ciclo que es usado para crear varios botones de circulo
#depues crea cada boton por separado

for (text,value) in values.items():
    Radiobutton(master,text=text, variable = v,
    value=value,indicator = 0,
    background= "light blue").pack(fill = X,ipady = 5)

#inicializa el ciclo puede terminar por el teclado or raton 
#interrumpir o la funcion predefinoda destruir

mainloop()