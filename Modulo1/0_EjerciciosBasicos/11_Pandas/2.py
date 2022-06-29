# Ejercicio 2
# Escribir una función que reciba un 
# diccionario con las notas de los alumno 
# de un curso y devuelva una serie con la nota 
# mínima, la máxima, media y la desviación típica.


import pandas as APA

def Refe(A):
    Notas = APA.Series(A)
    Estadisticas = APA.Series([Notas.min(),Notas.max(),Notas.mean(),Notas.std()],index = ["MIn","Max","Media","Desviacion tipica"])
    return Estadisticas


Note = {
    "Juan":2,
    "Caleb": 4,
    "pepe":3,
    "Manuel":5
}
print(Refe(Note))


