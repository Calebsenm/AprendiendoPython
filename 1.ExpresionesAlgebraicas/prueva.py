# se desarrolla toda la ecuacion ::::::::
# se logra pasar los datos de la matrix m a U
# Se logra contar los datos de cada dato dentro de la matirix

# verificar si es un dato do doy y ingresarlos a la matrix hija

# esta es la matriz madre ingresada
M = [   ["-A","+2B","+3C","-5D","=","40"],
        ["-A","+4B","+3C","+9D","=","46"],
        ["-4A","+3B","+2C","-8D","=","30"],
        ["-7A","+6B","+4C","-7C","=","50"],
]

b = 0        # la fila 
c = 0         # dentro de las columnas
# a= len(M[b][c])
# print(a)


# Matriz donde se copiaran los datos de de la matiz ingresada!
U = [   [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]    ]
# este ciclo recorrera la matriz y contará la cantidad que contiene cada sub lista
while b <= 3:
    while c <=5:

        
        GuardaMatrix = M [b][c]
        NumeroDeCaracteres = len(GuardaMatrix)
        

        print(f" esto es una prueva {NumeroDeCaracteres}")
        U[b][c] = GuardaMatrix
        
        
        c = c +1
        
    c = 0
    b = b+1

# recorre la matriz madre y la imprime
print("-------------------------")
print("|Esta es la matrix madre|")
print("-------------------------")
for g in range(4):
    for h in range(6):
        print(M[g][h],end='')
    print()

#recorre la matriz hija y la imprime

print("-------------------------")
print("|Esta es la matrix copia|")
print("-------------------------")

for i in range(4):
    for j in range(6):
        print(U[i][j],end=' ')
    print()



