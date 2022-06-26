# Ejercicio 8
# Escribir una función que reciba 
# una muestra de números en una 
# lista y devuelva un diccionario 
# con su media, varianza y desviación 
# típica.


#3:48 pm 25/06/2022
#5:21 pm 25/06/2022


def Funcion(Numeros):
    
    cantidad = 0
    desviacion = 0
    diccionario = {}

    for i in Numeros:
        io = int(i)
        cantidad += io
        desviacion += io ** 2

    varianza = 0
    for i in Numeros:
        io = int(i)
        varianza += (io - cantidad /len(Numeros)) ** 2

    diccionario["Media"] =  cantidad /len(Numeros)
    diccionario["Varianza"] = varianza/len(Numeros)
    diccionario["Desviacion"] = (desviacion/(len(Numeros))-(cantidad/ len(Numeros))**2)**(1/2)

    return diccionario

AS = input("Ingresa ina lista de numeros separados por coma ")
AS = AS.split(",")
print(Funcion(AS))