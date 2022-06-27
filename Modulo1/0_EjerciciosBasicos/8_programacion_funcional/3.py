# Ejercicio 3
# Escribir una función que reciba otra función 
# y una lista, y devuelva otra lista con el resultado 
# de aplicar la función dada a cada uno de los elementos de la lista.

#7:00pm   26/06/2022 
#7:13 pm   26/06/2022 

def Hola(Funcion,Lista):
    L = []
    for i in Lista:
        L.append(Funcion(i))
    return L

def Raiz(Numero):
    return Numero ** 2

Hola1 = Hola(Raiz,[1,2,3,4,5,6,7,8,9,10]) 
print(Hola1)

