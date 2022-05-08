"""
Ejercicio 4
Escribir un programa que 
pida al usuario un número 
entero y muestre por pantalla
si es par o impar.
"""

from os import system

while True:
    system("cls")

    numero = int(input("Ingrese un numero :D >> "))
    if numero % 2 == 0:
        print("EL numero es par")
    else:
        print("El numero es impar")
    desicion = input("Ingresa 0 para salir de lo contrario ingresa enter >> ")

    if desicion == "0":
        break



