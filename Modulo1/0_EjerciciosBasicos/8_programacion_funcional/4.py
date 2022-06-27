# Ejercicio 4
# Escribir una función que reciba otra 
# función booleana y una lista, y devuelva 
# otra lista con los elementos de la lista 
# que devuelvan True al aplicarles la función booleana.

#7:13 pm   26/06/2022


def Funcion(Funcion2,Lista):
    Li = []
    for i in Lista:
        if Funcion2(i):
            Li.append(i)
    return Li
def Boleana(A):
    return A % 2 == 1

Resultado = Funcion(Boleana,[1,2,3,4,5,6,7,8,9,10])
print(Resultado)


