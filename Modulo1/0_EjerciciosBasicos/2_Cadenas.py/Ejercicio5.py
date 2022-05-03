"""
Escribir un programa que pida
al usuario que introduzca una 
frase en la consola y muestre por 
pantalla la frase invertida.

finikitado el 2/05/2022

"""

frace = input("Ingresa una frase >> ")
frace = list(frace)
frace = reversed(frace)
frace ="".join(frace)
print(frace)

"""
Ingresa una frase >> hola como estás
sátse omoc aloh
"""