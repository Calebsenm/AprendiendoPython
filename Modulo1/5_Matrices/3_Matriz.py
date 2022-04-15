"""
Ejercicio 3

Escribe un programa que lea dos matrices de la misma longitud y permita realizar 
las siguientes operaciones    

Suma,Resta,Multiplicación por Escalar  :D

15/04/2022   1:40 pm
"""

from os import system
system("cls")

M1 = []
M2 = []
M3 = ["1 Suma", "2 Resta ", "3 Multiplicacion Por Escalar","0 Salir"]

for i in range(3):
    for j in range(4):
        M1.append([0]*4)
        M2.append([0]*4)

    print()


print("Esta es la matriz 1")
for i in range(3):
    for j in range (4):
        M1[i][j] = int(input(f"Ingresa el valor Numero {i} {j} De la primera Matriz: "))

print("Esta es la matriz 2")
for i in range(3):
    for j in range(4):
        M2[i][j] = int(input(f"Ingresa el Valor Numero {i} {j} De la segunda Matriz: "))


system("cls")

print("Esta es la matriz numero 1")
for i in range(3):
    for i in range(4):
        print(M1[i][j],end=' ')
        
    print()

print("Esta es la matriz numero 2")

for i in range(3):
    for j in range(4):
        print(M2[i][j],end = ' ')
    print()




for i in range(4):
    print(M3[i])


while True:
    Opcion = int(input("ingresa una opcion >> "))
    
    if Opcion == 0:
        break
    elif Opcion == 1:
        print("Has elegido sumar las Matrices")

    elif Opcion == 2:
        print("Has elegido Restar las Matrices")

    elif Opcion == 3:
        print("Has elegido Multiplicación por escalar de matrices ")





    






