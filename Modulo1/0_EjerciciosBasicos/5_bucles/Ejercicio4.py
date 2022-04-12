"""
Ejercicio 4
Escribir un programa que pida al usuario un número
entero positivo y muestre por pantalla la cuenta atrás
desde ese número hasta cero separados por comas.


12 / 04 / 2022  5:15

"""

from tkinter import NUMERIC


Numero = int(input("ingresa un numero: "))

a = 0

while True:
    coma  = ","
    if Numero == 0:
        coma = ""

    print(Numero,coma ,end=" ")
    Numero = Numero -1
    a = a + 1
    
    if Numero == -1:
        break
    