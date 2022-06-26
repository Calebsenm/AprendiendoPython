# Ejercicio 3
# Escribir una función que reciba 
# un número entero positivo y 
# evuelva su factorial.

# Estuvo interesante esta recursividad

def Factorial(numero):
    print(numero)
    if numero == 1 or numero == 0 :
        return 1
    return  numero * Factorial(numero-1)

hola = int(input("Ingresa el numero > "))
hola2 = Factorial(hola)
print(f"el factorial de {hola} es {hola2}")



