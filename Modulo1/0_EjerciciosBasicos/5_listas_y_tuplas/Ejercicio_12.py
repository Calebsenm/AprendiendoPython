# Escribir un programa que almacene las matrices
# en una lista y muestre por pantalla su producto.
# A [[1,2,3],[4,5,6]]     B = [[-1,0],[0,1],[1,1]] 
#(1, 5)
#(2, 11)
# 

#muchas horas invertidas xd +2

# Nota: Para representar matrices mediante 
# listas usar listas anidadas, representando 
# cada vector fila en una lista.



A = [
    [1,2,3],
    [4,5,6]
]

B = [
    [-1,0],
    [0,1],
    [1,1]
] 

Matris = [
    [],
    []
 ]


for i in range(len(A)): 
    for j in range(len(A[0])):
        Matris[0].append(A[i][j])

        
for q in range(len(B)):
    for w in range(len(B[0])):
        if w == 0:
            Matris[1].append(B[q][0])
        
for q in range(len(B)):
    for w in range(len(B[0])):  
        if w == 1:
            Matris[1].append(B[q][1])
        
      
print(Matris)

La = [[],[]]

for e in range(len(Matris[1])):
    if e <= 2:

        La[0].append(Matris[0][e] * Matris[1][e])
        La[1].append(Matris[0][e] * Matris[1][e+3])

    if e >= 3:
        La[0].append(Matris[0][e] * Matris[1][e-3])
        La[1].append(Matris[0][e] * Matris[1][e])
   

print()
print(La)

el_resultado = [[],[]]
uno = 0
dos = 0
tres = 0
cuatro  = 0

p = 0
for t in La[0]:
    if p <= 2:
        uno += t
    if p >= 3:
        dos += t
    p += 1


ñ = 0
for l in La[1]:
    if ñ <= 2:
        tres += l
    if ñ >= 3:
        cuatro += l
    ñ += 1
    
print(f"{uno} {tres} \n{dos} {cuatro}")

# Log = [[],[]]

# # for i in range(len(A)):
# #     for j in range(len(A[0])):
# #         for k in range(len(B)):
# #             for l in range(len(B[0])-1):
# #                 Matris[0].append([int(A[i][j])*int(B[k][0])])
# #                 Matris[1].append([int(A[i][j])*int(B[k][1])])

# a = 0 
# while True:
#     a += 1


# for i in range(len(Matris)):
#     print(Matris[i])

# for ñ in range(len(Matris)):
#     for s in range(len(Matris[ñ])):
#         if s <= 9:
#             for q in range(len(Matris[ñ][s])):
#                 if ñ == 0:
#                     Log[0].append(Matris[ñ][s][q])
#                 else:
#                     Log[1].append(Matris[ñ][s][q])
#         if s > 9:
#             for v in range(len(Matris[ñ][s])):
#                 if ñ == 0:
#                     Log[0].append(Matris[ñ][s][v])
#                 else:
#                     Log[1].append(Matris[ñ][s][v])

# Resultado = [
#     [],
#     []
# ]
# uno = 0
# dos = 0
# tre = 0
# cua = 0

# for x in range(len(Log)):
#     if x == 0:
#         for c in range(len(Log[x])):
#             if c <= 6:
#                 uno += Log[x][c]
#             else:
#                 dos += Log[x][c]

#     if x == 1:
#         for a in range(len(Log[x])):
#             if a <= 6:
#                 tre += Log[x][a]
#             else:
#                 cua += Log[x][a]

# print()
# for i in range(len(Log)):
#     print(Log[i])

# print()
# result = [
#     [uno,dos],
#     [tre,cua]
# ]
# for w in result[0]:
#     print(w,end=" ")
# print()
# for e in result[1]:
#     print(e,end=" ")