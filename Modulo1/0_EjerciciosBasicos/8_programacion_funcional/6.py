# Ejercicio 6
# Escribir una función reciba una 
# lista de notas y devuelva la lista 
# de calificaciones correspondientes 
# a esas notas.

Lista = [1,2,3,4,5]


def Funcion(A):
    Aprovado = []

    for i in A:
        if i == 1:
            Aprovado.append("Malisimo")
        elif i == 2:
            Aprovado.append("Bajo")
        elif i == 3:
            Aprovado.append("Regular")
        elif i == 4:
            Aprovado.append("Alto")
        else:
            Aprovado.append("Superior")
     
    return Aprovado


print(Funcion(Lista))

