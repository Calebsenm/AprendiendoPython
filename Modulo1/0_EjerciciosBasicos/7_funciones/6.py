# #Ejercicio 6
# Escribir una función que reciba 
# una muestra de números en una 
# lista y devuelva su media.

# easy el 3:38 pm  el 25/06/2022

def Media(numero):
    a = 0
    for i in numero:
        a += int(i)
    
    return a /len(numero)


numero = input("Ingresa los numeros separados por coma ")
numero = numero.split(",") 
resultado = Media(numero)
print(f"La media del nuemero es {resultado}")
