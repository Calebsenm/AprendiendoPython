"""
Escribe un programa que lea
una matriz de longitud n x m, 
luego imprime la matriz en consola 
similar al referente de la imagen. 
Guarda el archivo como LecturaMatriz.py

| 2 0 5 8 |
| 1 3 7 4 |
| 6 9 0 2 |

"""

from os import system

#pedir dimenciones y llenarls por teclado
fila=int(input("Dime el numero de filas: "))
columna=int(input("Dime el numero de colummna: "))
"""
#crear matris nula
"""

# las listas quedaron listas 
M=[]

print()

for i in range(columna):    
         M.append([0]*fila)

for i in range(columna):
    for j in range(fila):
        print(M[i][j],end = ' ')
    print()

for i in range(columna):
    for j in range(fila):
        M[i][j] = int(input(f"ingresa el numero en la posicion {i} {j}: "))
    print()


for i in range (columna):
    for j in range(fila):
        print(M[i][j] ,end= ' ')
    print()


    

