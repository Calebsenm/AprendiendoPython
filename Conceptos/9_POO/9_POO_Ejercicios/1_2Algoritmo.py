#simulacion del algoritmo 
#este es el algoritmo



B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]

print(B)
print(N)
Ubicacion_Rey = []
Linea_De_peligro = []
M=[
    [" "," ","A","B","C","D","E","F","G","H"," "," "],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    ["8","|",N[1],N[3],N[5],N[4],N[2],N[5],N[3],N[1],"|","8"],
    ["7","|",N[0],N[0],N[0],N[0],N[0],N[0],N[0],N[0],"|","7"],
    ["6","|",".",".",".",".",".",".",".",N[2],"|","6"],
    ["5","|",".",".",".",B[4],".",N[3],".",".","|","5"],
    ["4","|",".",N[2],".",N[1],".",N[5],".",N[0],"|","4"],
    ["3","|",".",".",".",".",".",".",".",".","|","3"],
    ["2","|",B[0],B[0],".",".",N[0],B[0],B[0],B[0],"|","2"],
    ["1","|",B[1],B[3],B[5],".",B[2],B[5],B[3],B[1],"|","1"],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    [" "," ","A","B","C","D","E","F","G","H"," "," "]
]

for i in range(12):
            
    for j in range(12):
        print(M[i][j],end = ' ') 
    print()


def BuscaFichas(C,Ficha_Buscada):

    for i in range(len(M)):
        for j in range(len(M[i])):
            if C[i][j] == Ficha_Buscada:
                Ubicacion_Rey.append([i,j])

            
BuscaFichas(M,B[4])

Nueva_Ubicacion_Rey = [Ubicacion_Rey[0][0],Ubicacion_Rey[0][1]]
print(Nueva_Ubicacion_Rey)

#verifica el color de la ficha
print( M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]])
CONJUNTO_FICHA = N
if M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]] in B:
    #color contrario 
    CONJUNTO_FICHA = N
elif M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]] in N:
    CONJUNTO_FICHA = B


Fihas_Ataque = [CONJUNTO_FICHA[1],CONJUNTO_FICHA[2]]
Fihas_Ataque2 = [CONJUNTO_FICHA[0],CONJUNTO_FICHA[4]]
Fihas_Ataque_Diagonal = [CONJUNTO_FICHA[2],CONJUNTO_FICHA[5]]
Ficha_Ataque_Caballo = [CONJUNTO_FICHA[3]]
cual_ficha_ataca = []

Linea_De_peligro.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]])

while True:
    #ataque hacia arriba
    A = 1
    Movimiento_recursivo1 = []
    while True:
        if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]] in Fihas_Ataque:
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]])
            cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]])
            Movimiento_recursivo1.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]])
            break
        if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]] == ".":
            Movimiento_recursivo1.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]])
    
        else:
            break
        A = A + 1
    # print("Este es el moviminto recursivo")
    # print(Movimiento_recursivo1)

    for i in range(len(Movimiento_recursivo1)):
        for j in range(1):
            
            if M[Movimiento_recursivo1[i][0]][Movimiento_recursivo1[i][1]] in Fihas_Ataque:

                for o in range(len(Movimiento_recursivo1)):
                    for s in range(1):
                        Linea_De_peligro.append([Movimiento_recursivo1[o][s],Movimiento_recursivo1[o][s+1]])
    


    #ataque arriba derecha
    Movimiento_recursivo2 = []
    A = 1
    while True:
        if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]+A] in Fihas_Ataque_Diagonal:
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]+A])
            cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]+A])
            Movimiento_recursivo2.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]+A])
            break
        if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]+A] == ".":
            Movimiento_recursivo2.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]+A])
        elif A == 1:
            if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]+A] in Fihas_Ataque2:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]+A])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]+A])


                break
            break

        else:
            break
        A = A + 1
    # print("Este es el movimiento resucursivo")
    # print(Movimiento_recursivo2)
    for i in range(len(Movimiento_recursivo2)):
        for j in range(1):
            if M[Movimiento_recursivo2[i][0]][Movimiento_recursivo2[i][1]] in Fihas_Ataque_Diagonal:

                for o in range(len(Movimiento_recursivo2)):
                    for s in range(1):
                        Linea_De_peligro.append([Movimiento_recursivo2[o][s],Movimiento_recursivo2[o][s+1]])
    

    
    #ataque arriba isquierda
    Movimiento_recursivo3 = []
    A = 1
    while True:
        if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]-A] in Fihas_Ataque_Diagonal:
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]-A])
            cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]-A])
            Movimiento_recursivo3.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]-A])


            break
        if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]-A] == ".":
            Movimiento_recursivo3.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]-A])
        elif A == 1:
            if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]-A] in Fihas_Ataque2:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]-A])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]-A])
                
                break
            break

        else:
            break
        
        A = A + 1
    # print("Este es el movimiento resucursivo")
    # print(Movimiento_recursivo3)
    for i in range(len(Movimiento_recursivo3)):
        for j in range(1):
            
            if M[Movimiento_recursivo3[i][0]][Movimiento_recursivo3[i][1]] in Fihas_Ataque_Diagonal:

                for o in range(len(Movimiento_recursivo3)):
                    for s in range(1):
                        Linea_De_peligro.append([Movimiento_recursivo3[o][s],Movimiento_recursivo3[o][s+1]])
    

    #ataque hacia la derecha
    A = 1
    Movimiento_recursivo = []
    while True:
        if M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]+A] in Fihas_Ataque:
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]+A])
            cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]+A])
            Movimiento_recursivo.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]+A])
            break
        if M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]+A] == ".":
            Movimiento_recursivo.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]+A])
        else:
            break
        A = A + 1
    # print("Este es el movimiento resucursivo")
    # print(Movimiento_recursivo)
    for i in range(len(Movimiento_recursivo)):
        for j in range(1):
            
            if M[Movimiento_recursivo[i][0]][Movimiento_recursivo[i][1]] in Fihas_Ataque:

                for o in range(len(Movimiento_recursivo)):
                    for s in range(1):
                        Linea_De_peligro.append([Movimiento_recursivo[o][s],Movimiento_recursivo[o][s+1]])
    
    #ataque hacia la isquierda
    A = 1
    Movimiento_recursivo4 = []
    while True:
        if M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]-A] in Fihas_Ataque:
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]-A])
            cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]-A])
            Movimiento_recursivo4.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]-A])
            break
        if M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]-A] == ".":
            Movimiento_recursivo4.append([Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]-A])
        else:
            break
        A = A + 1
    # print("Este es el movimiento resucursivo")
    # print(Movimiento_recursivo4)
    for i in range(len(Movimiento_recursivo4)):
        for j in range(1):
            
            if M[Movimiento_recursivo4[i][0]][Movimiento_recursivo4[i][1]] in Fihas_Ataque:

                for o in range(len(Movimiento_recursivo4)):
                    for s in range(1):
                        Linea_De_peligro.append([Movimiento_recursivo4[o][s],Movimiento_recursivo4[o][s+1]])
    
    #ataque hacia abajo
    Movimiento_recursivo5 = []
    A = 1
    while True:
        if M[Nueva_Ubicacion_Rey[0]+A][Nueva_Ubicacion_Rey[1]] in Fihas_Ataque:
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]])
            cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]])
            Movimiento_recursivo5.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]])

            break
        if M[Nueva_Ubicacion_Rey[0]+A][Nueva_Ubicacion_Rey[1]] == ".":
            Movimiento_recursivo5.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]])
    
        else:
            break
        A = A + 1

    # print("Este es el movimiento resucursivo")
    # print(Movimiento_recursivo5)
    for i in range(len(Movimiento_recursivo5)):
        for j in range(1):
            
            if M[Movimiento_recursivo5[i][0]][Movimiento_recursivo5[i][1]] in Fihas_Ataque:

                for o in range(len(Movimiento_recursivo5)):
                    for s in range(1):
                        Linea_De_peligro.append([Movimiento_recursivo5[o][s],Movimiento_recursivo5[o][s+1]])
    

    #ataque abajo derecha
    Movimiento_recursivo6 = []
    A = 1
    while True:
        if M[Nueva_Ubicacion_Rey[0]+A][Nueva_Ubicacion_Rey[1]+A] in Fihas_Ataque_Diagonal:
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]+A])
            cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]+A])
            Movimiento_recursivo6.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]+A])
            break
        if M[Nueva_Ubicacion_Rey[0]+A][Nueva_Ubicacion_Rey[1]+A] == ".":
            Movimiento_recursivo6.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]+A])
       

        else:
            break
        A = A + 1
    # print("Este es el movimiento resucursivo")
    # print(Movimiento_recursivo6)
    for i in range(len(Movimiento_recursivo6)):
        for j in range(1):
            # print(M[Movimiento_recursivo6[i][0]][Movimiento_recursivo6[i][1]] )
            if M[Movimiento_recursivo6[i][0]][Movimiento_recursivo6[i][1]] in Fihas_Ataque_Diagonal:

                for o in range(len(Movimiento_recursivo6)):
                    for s in range(1):
                        Linea_De_peligro.append([Movimiento_recursivo6[o][s],Movimiento_recursivo6[o][s+1]])


    #ataque abajo isquierda
    Movimiento_recursivo7 = []
    A = 1
    while True:
        if M[Nueva_Ubicacion_Rey[0]+A][Nueva_Ubicacion_Rey[1]-A] in Fihas_Ataque_Diagonal:
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]-A])
            cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]-A])
            Movimiento_recursivo7.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]-A])
            break
        if M[Nueva_Ubicacion_Rey[0]+A][Nueva_Ubicacion_Rey[1]-A] == ".":
            Movimiento_recursivo7.append([Nueva_Ubicacion_Rey[0]+A,Nueva_Ubicacion_Rey[1]-A])
        else:
            break
        A = A + 1
    # print("Este es el movimiento resucursivo")
    # print(Movimiento_recursivo7)
    for i in range(len(Movimiento_recursivo7)):
        for j in range(1):
            if M[Movimiento_recursivo7[i][0]][Movimiento_recursivo7[i][1]] in Fihas_Ataque_Diagonal:

                for o in range(len(Movimiento_recursivo7)):
                    for s in range(1):
                        Linea_De_peligro.append([Movimiento_recursivo7[o][s],Movimiento_recursivo7[o][s+1]])
   
   
    #Ataque de un caballo
    #Diagonal Derecha Arriba
    if not M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]+1]  == "_" and not  M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]+1] == "|":
        if not M[Nueva_Ubicacion_Rey[0]-2][Nueva_Ubicacion_Rey[1]+1] == "_":
            if M[Nueva_Ubicacion_Rey[0]-2][Nueva_Ubicacion_Rey[1]+1] in Ficha_Ataque_Caballo:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-2,Nueva_Ubicacion_Rey[1]+1])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-2,Nueva_Ubicacion_Rey[1]+1])

        
        if not M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]+2] == "|":
            if M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]+2] in Ficha_Ataque_Caballo:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-1,Nueva_Ubicacion_Rey[1]+2])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-1,Nueva_Ubicacion_Rey[1]+2])
    
    #Diagonal isquierda arriba
    if not M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]-1]  == "_" and not  M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]-1] == "|":
        if not M[Nueva_Ubicacion_Rey[0]-2][Nueva_Ubicacion_Rey[1]-1] == "_":
            if M[Nueva_Ubicacion_Rey[0]-2][Nueva_Ubicacion_Rey[1]-1] in Ficha_Ataque_Caballo:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-2,Nueva_Ubicacion_Rey[1]-1])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-2,Nueva_Ubicacion_Rey[1]-1])

        
        if not M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]-2] == "|":
            if M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]-2] in Ficha_Ataque_Caballo:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-1,Nueva_Ubicacion_Rey[1]-2])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]-1,Nueva_Ubicacion_Rey[1]-2])
    
    #Diagonal isquierda abajo
    if not M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]-1]  == "_" and not  M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]-1] == "|":
        if not M[Nueva_Ubicacion_Rey[0]+2][Nueva_Ubicacion_Rey[1]-1] == "_":
            if M[Nueva_Ubicacion_Rey[0]+2][Nueva_Ubicacion_Rey[1]-1] in Ficha_Ataque_Caballo:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]+2,Nueva_Ubicacion_Rey[1]-1])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]+2,Nueva_Ubicacion_Rey[1]-1])

        
        if not M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]-2] == "|":
            if M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]-2] in Ficha_Ataque_Caballo:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]+1,Nueva_Ubicacion_Rey[1]-2])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]+1,Nueva_Ubicacion_Rey[1]-2])
    
    #Diagonal Derecha abajo
    if not M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]+1]  == "_" and not  M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]+1] == "|":
        if not M[Nueva_Ubicacion_Rey[0]+2][Nueva_Ubicacion_Rey[1]+1] == "_":
            if M[Nueva_Ubicacion_Rey[0]+2][Nueva_Ubicacion_Rey[1]+1] in Ficha_Ataque_Caballo:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]+2,Nueva_Ubicacion_Rey[1]-1])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]+2,Nueva_Ubicacion_Rey[1]-1])

        
        if not M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]+2] == "|":
            if M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]+2] in Ficha_Ataque_Caballo:
                Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]+1,Nueva_Ubicacion_Rey[1]+2])
                cual_ficha_ataca.append([Nueva_Ubicacion_Rey[0]+1,Nueva_Ubicacion_Rey[1]+2])
    


    


    break
   


    #ataque del caballo

print(Linea_De_peligro)

#verifica si esta en hake
i = 0
while True:
    if Nueva_Ubicacion_Rey[0] == Linea_De_peligro[i][i] and Nueva_Ubicacion_Rey[1] == Linea_De_peligro[i][i+1]:
        for i in range(len(cual_ficha_ataca)):
            for j in range(1):
                print(f"La ficha está en hake por {M[cual_ficha_ataca[i][0]][cual_ficha_ataca[i][1]]}")
        
        break 
    else:
        print("NO hay hake")
        break
#Verica si está en hakemate

print("Esta es la ubicacion del rey dentro del tablero")

print(Nueva_Ubicacion_Rey)




#verifica si la posisicion actual esta en hake
if Nueva_Ubicacion_Rey in Linea_De_peligro:
    print("Movimiento en jake")
else:
    print("el movimiento no está en hake")

#verifica arriba
if [Nueva_Ubicacion_Rey[0]-1,Nueva_Ubicacion_Rey[1]] in Linea_De_peligro:
    print("Posicion en hake") 
elif M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]]  == "_":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")

#verifica arriba Derecha 
if [Nueva_Ubicacion_Rey[0]-1,Nueva_Ubicacion_Rey[1]+1] in Linea_De_peligro:
    print("Posicion en hake") 
elif M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]+1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]+1]  == "_":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")



#verifica arriba isquierda
if [Nueva_Ubicacion_Rey[0]-1,Nueva_Ubicacion_Rey[1]-1] in Linea_De_peligro:
    print("Posicion en hake") 
elif M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]-1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey[0]-1][Nueva_Ubicacion_Rey[1]-1]  == "_":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")

#verifica isquierda
if [Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]-1] in Linea_De_peligro:
    print("Posicion en hake") 
elif M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]-1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]-1]  == "|":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")


#verifica Derecha 
if [Nueva_Ubicacion_Rey[0],Nueva_Ubicacion_Rey[1]+1] in Linea_De_peligro:
    print("Posicion en hake") 
elif M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]+1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]+1]  == "|":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")


#verifica abajo Derecha 
if [Nueva_Ubicacion_Rey[0]+1,Nueva_Ubicacion_Rey[1]+1] in Linea_De_peligro:
    print("Posicion en hake") 
elif M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]+1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]+1]  == "_":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")

#verifica abajo isquierda  
if [Nueva_Ubicacion_Rey[0]+1,Nueva_Ubicacion_Rey[1]-1] in Linea_De_peligro:
    print("Posicion en hake") 
elif M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]-1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]-1]  == "_":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")

#verifica abajo 
if [Nueva_Ubicacion_Rey[0]+1,Nueva_Ubicacion_Rey[1]] in Linea_De_peligro:
    print("Posicion en hake") 
elif M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey[0]+1][Nueva_Ubicacion_Rey[1]]  == "_":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")


