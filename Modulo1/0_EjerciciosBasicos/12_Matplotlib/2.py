# Ejercicio 2
# Escribir una función que reciba una diccionario 
# con las notas de las asignaturas de un curso y 
# una cadena con el nombre de un color y devuelva 
# un diagrama de barras de las notas en el color dado.



import matplotlib.pyplot as pth



def lista(A,B):
    fig,ax = pth.subplots()
    ax.bar(A.keys(),A.values(), color = B)


Notas = {
    "Matematicas":10,
    "Lengua":9,
    "ingles":8,
    }
lista(Notas,"blue")


pth.show()