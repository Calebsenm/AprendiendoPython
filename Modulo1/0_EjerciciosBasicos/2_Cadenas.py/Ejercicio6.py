"""
Ejercicio 6
ir un programa que pida al 
usuario que introduzca una frase 
en la consola y una vocal, y después 
muestre por pantalla la misma frase 
pero con la vocal introducida 
en mayúscula.

finikitado el 2/05/2022
"""

frace = input("Ingresa una Frace >> ")
palabra = input("Ingresa una letra >> ")

print(frace.replace(palabra,palabra.upper()))

"""
Ingresa una Frace >> Hola soy el ingeniero de la nasa 
Ingresa una letra >> a
HolA soy el ingeniero de lA nAsA 

"""