# Ejercicio 3
# Escribir una función que reciba una 
# serie de Pandas con las notas de los 
# alumnos de un curso y devuelva un 
# diagrama de cajas con las notas. El 
# diagrama debe tener el título 
# “Distribución de notas”.

import pandas as pa
import matplotlib.pyplot as mpl
import numpy as np

def Function(A):
    mpl.title("Distribución de notas") 
    return A.plot.box(grid = "True")
    


Notas = [2,4,6,4,2,7,0,3,7,3,7,9,3,5,7,4]
l_Notas = pa.Series(Notas)

Function(l_Notas)
mpl.show()