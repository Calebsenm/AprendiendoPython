# Ejercicio 5
# Escribir una función que 
# reciba una frase y devuelva un 
# diccionario con las palabras que 
# contiene y su longitud.


def Funcion(Frace):
    Diccionario = {}

    L = Frace.split(" ")
    for i in L:
        Diccionario[i] = len(i)

    return Diccionario

print(Funcion(input("Ingresa una Frace ->")))