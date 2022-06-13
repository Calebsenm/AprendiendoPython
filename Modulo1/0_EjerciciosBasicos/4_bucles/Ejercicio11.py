"""
Escribir un programa que pida al 
usuario una palabra y luego muestre 
por pantalla una a una las letras de 
la palabra introducida empezando por la última.

finikitado 12/06/2022  6:50
"""


while True:
    phrase1 = input("Please input a phrase >> ")
    listw = list(phrase1)
    listw.reverse()
    for i in listw:
        if i == " ":
            continue
        print(i)