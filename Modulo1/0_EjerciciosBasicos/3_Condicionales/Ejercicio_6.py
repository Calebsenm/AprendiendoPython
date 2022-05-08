"""
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos
A y B de acuerdo al sexo y el nombre. El grupo A esta 
formado por las mujeres con un nombre anterior a la M 
y los hombres con un nombre posterior a la N y el grupo B 
por el resto. Escribir un programa que pregunte al usuario su 
nombre y sexo, y muestre por pantalla el grupo que le corresponde.

finikitado el 8/05/2022
"""

M = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]

Nombre = input("Ingrese su numbre >> ")
Sexo = input("Usred es M o H ? >> ")

if Sexo.upper() == "M":
    if Nombre.lower() < "m":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")
else:
    if Nombre.lower() > "n":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")


    
        


