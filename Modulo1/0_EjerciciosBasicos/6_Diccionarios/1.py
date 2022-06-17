"""
Ejercicio 1
Escribir un programa que 
guarde en una variable el 
diccionario {'Euro':'€', 
'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una 
divisa y muestre su símbolo o 
un mensaje de aviso si la divisa 
no está en el diccionario.

finished ok 
15/06/2022   9:58 am
"""

Billetes = {
    "dollar":"$",
    "euro":"€",
    "Yen": "¥"
}

billete = input("Ingrese una divisa -> ")
if billete in Billetes:
    print(Billetes[billete]) 
else:
    print("Eso no existe ")