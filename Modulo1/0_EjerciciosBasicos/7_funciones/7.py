# Ejercicio 7
# Escribir una función que 
# reciba una muestra de números 
# en una lista y devuelva otra 
# lista con sus cuadrados.

# 3:47 pm 25/06/2022 
def cuadrado(numeros):
    Lista = []
    for i in numeros:
        k = int(i)
        a = k ** 2
        Lista.append(a)
    return Lista


numeros = input("ingresa los numeros separados por coma -> ")
numeros2 = numeros.split(",")

Lista = cuadrado(numeros2)
print(f"Los cuadrados de los numeros es {Lista}")