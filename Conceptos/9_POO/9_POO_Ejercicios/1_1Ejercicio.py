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
Contador_cambio = 1

while True:
  
    if Contador_cambio == 1:
        system("cls")
        
        print("Las fichas..")
        print(". ".join(B))
        print(". ".join(N))
        print()


        for i in range(12):
            for j in range(12):
                print(M[i][j],end = ' ') 
            print()

        #pide la posicion de la ficha
        Numero_fila = int(input("Ingrese EL numero de la ficha >> "))
        Letra_columna = input("Ingrese La letra de la ficha >> ")
        
        if Numero_fila == 1:
            fila = 9
        
        #coloca las filas
        elif Numero_fila == 2:
            fila = 8
        elif Numero_fila == 3:
            fila = 7
        elif Numero_fila == 4:
            fila =6
        elif Numero_fila == 5:
            fila =5
        elif Numero_fila == 6:
            fila =4
        elif Numero_fila == 7:
            fila =3
        elif Numero_fila == 8:
            fila =2
        else:
            print("error")
        #ubica las colunas
        if Letra_columna == "A":
            columna = 2
        elif Letra_columna == "B":
            columna = 3
        elif Letra_columna == "C":
            columna = 4
        elif Letra_columna == "D":
            columna = 5
        elif Letra_columna == "E":
            columna = 6
        elif Letra_columna == "F":
            columna = 7
        elif Letra_columna == "G":
            columna = 8
        elif Letra_columna == "H":
            columna = 9
        

        Ficha = M[fila][columna]
        print(Ficha)

        Letra = input("Letra donde Desea mover la ficha>> ")
        # Numero = input("Numero donde Desea Mover la ficha >> ")

        #hace el cambio
        Contador_cambio = 0

    elif Contador_cambio == 0:
        system("cls")
        Contador_cambio = 1
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

        Numero_fila2 = int(input("Ingrese EL numero de la ficha >> "))
        Letra_columna2 = input("Ingrese La letra de la ficha >> ")

        if Numero_fila2 == 8:
            fila2 = 2
        elif Numero_fila2 ==7:
            fila2 = 3
        elif Numero_fila2 ==6:
            fila2 = 4
        elif Numero_fila2 ==5:
            fila2 = 5
        elif Numero_fila2 ==4:
            fila2 = 6
        elif Numero_fila2 ==3:
            fila2 =7
        elif Numero_fila2 == 2:
            fila2 = 8
        elif Numero_fila2 ==1:
            fila2 = 9
        else:
            print("Error")
        
        #columnas
        if Letra_columna2 == "A":
            columna2 = 9
        elif Letra_columna2 =="B":
            columna2 = 8
        elif Letra_columna2 =="C":
            columna2 = 7
        elif Letra_columna2 == "D":
            columna2 = 6
        elif Letra_columna2 == "E":
            columna2 = 5
        elif Letra_columna2 == "F":
            columna2 = 4
        elif Letra_columna2 == "G":
            columna2 = 3
        elif Letra_columna2 == "H":
            columna2 = 2
        else: 
            print("Eroor")
        

        Ficha2 = M[fila2][columna2]
        print(Ficha2)

        Letra = input("Letra donde Desea mover la ficha>> ")
        # Numero = input("Numero donde Desea Mover la ficha >> ")

        #hace el cambio
        



