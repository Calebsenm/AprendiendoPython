"""
Será que se puede crear el jeugo del agedrez en pyton con la consola..  yo no lo sé solo quiero intentarlo.... ajajajjajaja
Se inició este proyecto el dia 29/04/2022
"""
from os import system

from numpy import sort


B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]



M=[
    [" "," ","A","B","C","D","E","F","G","H"," "," "],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    ["8","|",N[1],N[3],N[5],N[4],N[2],N[5],N[3],N[1],"|","8"],
    ["7","|",N[0],N[0],N[0],N[0],N[0],N[0],N[0],N[0],"|","7"],
    ["6","|",".",".",".",".",".",".",".",".","|","6"],
    ["5","|",".",".",".",".",".",".",".",".","|","5"],
    ["4","|",".",".",".",".",".",".",".",".","|","4"],
    ["3","|",".",".",".",".",".",".",".",".","|","3"],
    ["2","|",B[0],B[0],B[0],B[0],B[0],B[0],B[0],B[0],"|","2"],
    ["1","|",B[1],B[3],B[5],B[4],B[2],B[5],B[3],B[1],"|","1"],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    [" "," ","A","B","C","D","E","F","G","H"," "," "]
]
M.reverse()
for a in range(12):
    M[a].reverse()
    for b in range(12):
        a = 0

#funcion de la operacion
   
def Accion(jugador,n1,n2,n3,n4,n5,n6,n7,n8,n11,n12,n13,n14,n15,n16,n17,n18):
    system("cls")
        
    print("Las fichas..")
    print(". ".join(B))
    print(". ".join(N))
    print()


    M.reverse()
        
    for i in range(12):
            
        M[i].reverse()
        for j in range(12):
            print(M[i][j],end = ' ') 
        print()

    print(jugador)
    Numero_fila2 = int(input("Ingrese EL numero de la ficha >> "))
    Letra_columna2 = input("Ingrese La letra de la ficha >> ")

    
    if Numero_fila2 == 8:
        fila2 = n1
    elif Numero_fila2 ==7:
        fila2 = n2
    elif Numero_fila2 ==6:
        fila2 = n3
    elif Numero_fila2 ==5:
        fila2 = n4
    elif Numero_fila2 ==4:
        fila2 = n5
    elif Numero_fila2 ==3:
        fila2 = n6
    elif Numero_fila2 == 2:
        fila2 = n7
    elif Numero_fila2 ==1:
        fila2 = n8
    else:
        print("Error")
        
    #columnas
    if Letra_columna2 == "A":
        columna2 = n11
    elif Letra_columna2 =="B":
        columna2 = n12
    elif Letra_columna2 =="C":
        columna2 = n13
    elif Letra_columna2 == "D":
        columna2 = n14
    elif Letra_columna2 == "E":
        columna2 = n15
    elif Letra_columna2 == "F":
        columna2 = n16
    elif Letra_columna2 == "G":
        columna2 = n17
    elif Letra_columna2 == "H":
        columna2 = n18
    else: 
        print("Eroor")
        

    Ficha2 = M[fila2][columna2]
    print(Ficha2)

    
            
    Numero_fila2 = int(input("Numero donde Desea Mover la ficha >> "))
    Letra_columna2 = input("Letra donde Desea mover la ficha>> ")
    #hace el cambio
    if Numero_fila2 == 8:
        fila2 = n1
    elif Numero_fila2 ==7:
        fila2 = n2
    elif Numero_fila2 ==6:
        fila2 = n3
    elif Numero_fila2 ==5:
        fila2 = n4
    elif Numero_fila2 ==4:
        fila2 = n5
    elif Numero_fila2 ==3:
        fila2 = n6
    elif Numero_fila2 == 2:
        fila2 = n7
    elif Numero_fila2 ==1:
        fila2 = n8
    else:
        print("Error")
        
    #columnas
    if Letra_columna2 == "A":
        columna2 = n11
    elif Letra_columna2 =="B":
        columna2 = n12
    elif Letra_columna2 =="C":
        columna2 = n13
    elif Letra_columna2 == "D":
        columna2 = n14
    elif Letra_columna2 == "E":
        columna2 = n15
    elif Letra_columna2 == "F":
        columna2 = n16
    elif Letra_columna2 == "G":
        columna2 = n17
    elif Letra_columna2 == "H":
        columna2 = n18
    else: 
        print("Eroor")
    #el peon y su movimiento
    
    M[fila2][columna2] = Ficha2 
   




Contador_cambio = 2
while True:
    
    if Contador_cambio %2 == 0:

        Accion("Jugador1",2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9)

    else:
        Accion("Jugador2",9,8,7,6,5,4,3,2,9,8,7,6,5,4,3,2)
    Contador_cambio = Contador_cambio + 1


