"""
Ejercicio 2
Escribir un programa que pregunte al 
usuario su edad y muestre por pantalla 
todos los años que ha cumplido 
(desde 1 hasta su edad).

inicio 12 /04/2022 hora 4:28 pm
Terminado 12 /04/2022 hora 4:39 pm
"""

print("Vienvenido al programa")
edad = int(input("ingresa tu edad actual: "))

a = 0

while a < edad:
    b = a + 1
    print(f"Has cunplido {b} años")
    a =  a +1



for i in range(edad):
    b = i + 1
    print(f"Has cunplido {b} años")