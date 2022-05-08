"""
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años
y tener unos ingresos iguales o superiores a 1000 € mensuales. 

Escribir un programa que pregunte al usuario su edad
y sus ingresos mensuales y muestre por pantalla si el 
usuario tiene que tributar o no.

finikitado 4/02/2022
"""

edad = int(input("digite su edad >> "))
ingresos = int(input("Ingrese sus ingresos mensuales >> "))

if edad >= 17:
    if ingresos == 1000:
        print("Usted debe tributar")
    else:
        print("usted no puede tributar")
else:
    print("usted no puede tributar")


