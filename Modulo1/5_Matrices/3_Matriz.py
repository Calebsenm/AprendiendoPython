"""
Ejercicio 3

Escribe un programa que lea dos matrices de la misma longitud y permita realizar 
las siguientes operaciones    

Suma,Resta,Multiplicación por Escalar  :D

15/04/2022   1:40 pm
17/04/2022   4:51 pm    se terminó
"""

from os import system
system("cls")

M1 = []
M2 = []
M3 = ["1 Suma", "2 Resta ", "3 Multiplicacion Por Escalar","0 Salir"]
#este aqui se almacenará la nueva matris luego de la opracion
M4  = []

for i in range(3):
    for j in range(4):
        M2.append([0]*4)
        M4.append([0]*4)

    print()
for i in range(3):
    for j in range(4):
        M1.append([0]*4)

system("cls")

print("Esta es la matriz 1")

i = 0
j = 0

for i in range(3):
    for j in range (4):
        M1[i][j] = int(input(f"Ingresa un numero en la pocicion {i} {j} De la primera Matris >> "))

print("Esta es la matriz 2")
for i in range(3):
    for j in range(4):
        M2[i][j] = int(input(f"Ingresa el Valor Numero {i} {j} De la segunda Matris: "))

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


print()


#imprime la lista de opciones 

for i in range(4):
    print(M3[i])


while True:
    Opcion = int(input("ingresa una opcion >> "))
    
    if Opcion == 0:
        break
    elif Opcion == 1:
        system("cls")
        print("Has elegido sumar las Matrices")
        
        #Ciclo que irá recorreindo la matris y la sumará 
        
        print("La matris sumada queda de la siguiente forma")
        for i in range(3):
            for j in range(4):
                M4[i][j] = M1[i][j] + M2[i][j]

        for i in range(3):
            for j in range(4):
                print(M4[i][j],end = ' ')
            
            print()

    elif Opcion == 2:
        system("cls")
        print("Has elegido Restar las Matrices")
        for i in range(3):
            for j in range(4):
                M4[i][j] = M1[i][j] - M2[i][j]

        for i in range(3):
            for j in range(4):
                print(M4[i][j],end = ' ')
            
            print()



    elif Opcion == 3:
        print("Has elegido Multiplicación por escalar de matrices ")

        system("cls")
        print("Has elegido Multiplicar las Matrices")
        for i in range(3):
            for j in range(4):
                M4[i][j] = M1[i][j] * M2[i][j]

        for i in range(3):
            for j in range(4):
                print(M4[i][j],end = ' ')
            
            print()


    






