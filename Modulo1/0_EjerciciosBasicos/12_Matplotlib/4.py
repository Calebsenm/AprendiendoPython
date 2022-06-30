# Ejercicio 4
# Escribir una función que reciba una 
# serie de Pandas con el número de 
# ventas de un producto durante los 
# meses de un trimestre y un título 
# y cree un diagrama de sectores con 
# las ventas en formato png con el titulo dado. 
# El diagrama debe guardarse en un fichero con 
# formato png y el título dado.

import pandas as pd
import matplotlib.pyplot as plt


def Hola(Ventas, Titulo):
    fig, ax = plt.subplots()
    Ventas.plot(kind = 'pie', ax = ax)
    plt.ylabel('')
    plt.title(Titulo)
    plt.savefig("12_Matplotlib/4.png")
    return
    


ventas = {'Enero':200, 'Febrero':240, 'Marzo':310,"Abril":250,"Marzo":50}
s_ventas = pd.Series(ventas)
Hola(s_ventas, 'Ventas primer trimestre')


