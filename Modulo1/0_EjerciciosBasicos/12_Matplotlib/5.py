# Ejercicio 5
# Escribir una función que reciba una serie 
# de Pandas con el número de ventas de un 
# producto por años y una cadena con el tipo 
# de gráfico a generar (lineas, barras, sectores, areas) 
# y devuelva un diagrama del tipo indicado con la 
# evolución de las ventas por años y con el título 
# “Evolución del número de ventas”.


import matplotlib.pyplot as mp
import pandas as pn

def Funcion_Ventas(A,B,C = "blue"):

    if B == "Lineas":
        fig, ax = mp.subplots()
        ax.plot(A)
        mp.title(B)

    if B == "Area":
        fig,ax = mp.subplots()
        ax.bar(A.keys(),A.values(), color = C)
        mp.title(B)

    if B == "Barras":
        fig,ax = mp.subplots()
        ax.bar(A.keys(),A.values(), color = C)
        mp.title(B)

    if B == "Sectores":
        fig,ax = mp.subplots()
        A.plot(kind = "pie",ax = ax)
        mp.ylabel('')
        mp.title(B)

    return


Diccionario = {
    2000:1200, 
    2001:  840, 
    2002: 1325, 
    2003:1280, 
    2004:1500
  
}

Pandeadeado = pn.Series(Diccionario)
Funcion_Ventas(Pandeadeado,"Lineas")
mp.show()
Funcion_Ventas(Diccionario,"Area")
mp.show()
Funcion_Ventas(Diccionario,"Barras")
mp.show()
Funcion_Ventas(Pandeadeado,"Sectores")
mp.show()
