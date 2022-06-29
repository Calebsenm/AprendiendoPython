# Ejercicio 3
# Escribir una función que reciba un diccionario 
# con las notas de los alumnos de un curso y 
# devuelva una serie con las notas de los alumnos 
# aprobados ordenadas de mayor a menor.

import pandas as PA
def Funtion(NT):
    Valor = PA.Series(Notas)
    return Valor[Valor >= 3].sort_values(ascending=False)
    


Notas = {
    "Carlos":1,
    "Manuel":4,
    "Roberto":6,
    "Pepe":7
}
print(Funtion(Notas))