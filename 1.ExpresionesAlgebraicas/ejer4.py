"""
4. Dada una ecuación algebraica de 4 incógnitas, codifica la expresión en 
partes simples y desarrolla la ecuación en un archivo con nombre ecuacion.py

a. Calcula su resultado evaluado con valores constantes para las incógnitas.

b. Cambia los valores constantes de las incógnitas, compile y revise el resultado.

"""
"""
para resolver la ecuacion:


"""
# se importa la libreria numpy
import numpy as np
import numpy.linalg as la

M = [

    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],

]


print("las incognitas son la siguientes ")
print("W,X,Y,Z")

llena = 0
c = 0
b = 0

while llena == 0:
    

    while c <=3:
        while b<=4:
            try:
                a = int(input("ingresa un numero:"))
                
                h = len(str(a))

                if h == 0:
                    print("no puede quedar uno basio")
                    b = b-1
                M[c][b] = a
                print(M[c])
                b=b+1
            except ValueError:
                print("No se aceptan caracteres o Vacios")

        b = 0

        c = c+1
    llena = 1

print("________")

for i in range(4):
    for j in  range(5):
        print(M[i][j],end=' ')
    print()
    
A = np.array(

    [ 
        [M[0][0],M[0][1],M[0][2],M[0][3],],
        [M[1][0],M[1][1],M[1][2],M[1][3],],
        [M[2][0],M[2][1],M[2][2],M[2][3],],
        [M[3][0],M[3][1],M[3][2],M[3][3],],
    ]
)
B=np.array(
    [
        [M[0][4]],
        [M[1][4]],
        [M[2][4]],
        [M[3][4]]
    ]
)

Ainv = la.inv(A)
X = Ainv.dot(B)

C = 0


contador = 0

for i in range(4):
    for j in range(1):
        contador = contador + 1
        if contador == 1:
            C = "W"
        if contador == 2:
            C = "X"
        if contador ==3:
            C = "Y"
        if contador ==4:
            C = "Z"
        print(f"este es para {C}")
        print(X[i][j],end= ' ')
        
    print()
