"""
Ejercicio 1
Escribir un programa que pregunte 
el nombre del usuario en la consola 
y un número entero e imprima por 
pantalla en líneas distintas el nombre 
del usuario tantas veces como el número 
introducido.

finikitado el 1 / 5/2022

"""
nombre = input("Ingresa tu nombre >> ")
numero = int(input("Cuantas veces desea imprimir el nombre >> "))

for i in range(numero):
    print(f"{i+1}",nombre)