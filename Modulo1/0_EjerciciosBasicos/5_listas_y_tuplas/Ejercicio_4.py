"""
Ejercicio 4
Escribir un programa que pregunte 
al usuario los números ganadores de 
la lotería primitiva, los almacene en 
una lista y los muestre por pantalla 
ordenados de menor a mayor.

finished 12/06/2022
"""

Wins = []
a = 0
while a != 5:
    numbers = input("Input the numbers >> ")
    Wins.append(int(numbers))
    a += 1

Wins.sort()

print(f"the winning numbers is -> {str(Wins)}")


