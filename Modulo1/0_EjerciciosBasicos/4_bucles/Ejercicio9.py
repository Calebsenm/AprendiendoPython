"""
Escribir un programa que almacene 
la cadena de caracteres contraseña 
en una variable, pregunte al usuario 
por la contraseña hasta que introduzca 
la contraseña correcta.

Finikitado 12/06/2022  menos de 5 minutos
"""

password = input("Ingresa una contraseña >> ")
while True:
    password1 = input("Confirma tu contraseña >> ")
    if password == password1:
        print("Contraseña correcta ")
        break
    else:
        print("Las contraseñas no coinciden ")