"""
Escribir un programa que pida al usuario un número 
entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura el número introducido.

finikitado 5:19 = 10/06/2022
"""
from turtle import right


inp = int(input("ingresa la cantidad del triangulo > "))
iterator = 1
while iterator != inp:
    dato = "*"
    print(dato*iterator)
    iterator += 1




