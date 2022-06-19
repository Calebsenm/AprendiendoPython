"""
Ejercicio 6
Escribir un programa que cree un diccionario 
vacío y lo vaya llenado con información sobre 
una persona (por ejemplo nombre, edad, sexo, 
teléfono, correo electrónico, etc.) que se 
le pida al usuario. Cada vez que se añada 
un nuevo dato debe imprimirse el contenido 
del diccionario

esay 10:20 pm 
18/06/2022

"""

Obtions = {1:"Nombre",2:"Apellido",3:"Edad",4:"sexo",5:"Correro electronico"}
principal = {}
for i in Obtions:
    objeto1 = input(f"Cual es tu {Obtions[i]} ")
    principal[Obtions[i]] = objeto1
    print(principal)


datos = {}

while True:
    dato = input("Ingresa el valor ")
    ingresa = input(f"ingrea el {dato} ")
    datos[dato] = ingresa
    da = input("Quieres salir si / no ") 
    if da == "si":
        break
    else:
        print(datos)

