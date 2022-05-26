#simulacion del algoritmo 
#este es un espermiento la rama primcipa els el 1_2Algoritmo.py


B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]

print(B)
print(N)
Ubicacion_Rey = []
Linea_De_peligro = []
M=[
    [" "," ","A","B","C","D","E","F","G","H"," "," "],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    ["8","|",".",".",".",".",N[5],".",N[2],".","|","8"],
    ["7","|",".",".",".",".",".",".",".",".","|","7"],
    ["6","|",".",".",".",".",".",".",".",".","|","6"],
    ["5","|",".",".",".",B[4],".",".",".",".","|","5"],
    ["4","|",N[1],".",".",".",".",N[3],".",".","|","4"],
    ["3","|",".",".",".",".",".",".",".",".","|","3"],
    ["2","|",".",".",".",".",".",".",".",".","|","2"],
    ["1","|",".",".",N[2],".",".",".",".",N[5],"|","1"],
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



# Nueva_Ubicacion_Rey = [Ubicacion_Rey[0][0],Ubicacion_Rey[0][1]]
# print(Nueva_Ubicacion_Rey)

def Algoritmo_De_busqueda(Nueva_Ubicacion_Rey):

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


Nueva_Ubicacion_Rey_Origen = [Ubicacion_Rey[0][0],Ubicacion_Rey[0][1]]


Una_ficha_Arriba = [Nueva_Ubicacion_Rey_Origen[0]-1,Nueva_Ubicacion_Rey_Origen[1]]
Una_ficha_Arriba_Derecha = [Nueva_Ubicacion_Rey_Origen[0]-1,Nueva_Ubicacion_Rey_Origen[1]+1]
Una_ficha_Arriba_Isquierda =  [Nueva_Ubicacion_Rey_Origen[0]-1,Nueva_Ubicacion_Rey_Origen[1]-1] 
Una_ficha_Isquierda = [Nueva_Ubicacion_Rey_Origen[0],Nueva_Ubicacion_Rey_Origen[1]-1]
Una_ficha_Derecha = [Nueva_Ubicacion_Rey_Origen[0],Nueva_Ubicacion_Rey_Origen[1]+1]
Una_ficha_Abajo = [Nueva_Ubicacion_Rey_Origen[0]+1,Nueva_Ubicacion_Rey_Origen[1]] 
Una_ficha_Abajo_Derecha = [Nueva_Ubicacion_Rey_Origen[0]+1,Nueva_Ubicacion_Rey_Origen[1]+1] 
Una_ficha_Abajo_Isquierda = [Nueva_Ubicacion_Rey_Origen[0]+1,Nueva_Ubicacion_Rey_Origen[1]-1]



Algoritmo_De_busqueda(Nueva_Ubicacion_Rey_Origen)

#esta es la line de peligro
print(Linea_De_peligro)

#esta es la anterior ubicacion de un rey
print(Ubicacion_Rey)

#esta es para la pocision actual 
print(Nueva_Ubicacion_Rey_Origen) 


#verifica si esta en hake
i = 0
while True:
    if Nueva_Ubicacion_Rey_Origen[0] == Linea_De_peligro[i][i] and Nueva_Ubicacion_Rey_Origen[1] == Linea_De_peligro[i][i+1]:
        for i in range(len(Nueva_Ubicacion_Rey_Origen)):
            
            print(f"La ficha está en hake por {M[Nueva_Ubicacion_Rey_Origen[0]][Nueva_Ubicacion_Rey_Origen[1]]}")
        
        break 
    else:
        print("NO hay hake")
        break
#Verica si está en hakemate

#esta ba a buscar 8 posiciones al redesdor para ver si estan en hakemate
Algoritmo_De_busqueda(Una_ficha_Arriba)
Algoritmo_De_busqueda(Una_ficha_Arriba_Derecha)
Algoritmo_De_busqueda(Una_ficha_Arriba_Isquierda)
Algoritmo_De_busqueda(Una_ficha_Derecha)
Algoritmo_De_busqueda(Una_ficha_Isquierda)
Algoritmo_De_busqueda(Una_ficha_Abajo)
Algoritmo_De_busqueda(Una_ficha_Arriba_Derecha)
Algoritmo_De_busqueda(Una_ficha_Abajo_Isquierda)


#ba a buscar todos los duplicados en la linea de peligro y los reubicará e la nueva linea de peligro

print("Esta es la lina de peligro")
Nueva_linea_Peligro = []

for i in Linea_De_peligro:
    if not i in Nueva_linea_Peligro:
        Nueva_linea_Peligro.append(i)
#va a imprimir la nueva linea de peligro 

for i in Nueva_linea_Peligro:
    print(i)





Posicioneslibre = []
print("Esta es la ubicacion del rey dentro del tablero")

print(Nueva_Ubicacion_Rey_Origen)




#verifica si la posisicion actual esta en hake
if Nueva_Ubicacion_Rey_Origen in Nueva_linea_Peligro:
    print("Posicion en Haque")
else:
    print("el movimiento no está en hake")

#verifica arriba
if [Nueva_Ubicacion_Rey_Origen[0]-1,Nueva_Ubicacion_Rey_Origen[1]] in Nueva_linea_Peligro:
    print("Movimiento en Haque") 
elif M[Nueva_Ubicacion_Rey_Origen[0]-1][Nueva_Ubicacion_Rey_Origen[1]] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey_Origen[0]-1][Nueva_Ubicacion_Rey_Origen[1]]  == "_":
    print("posion Bloquedad ")
else:
    print("Posisicion libre")
    Posicioneslibre.append(True)

#verifica arriba Derecha 
if [Nueva_Ubicacion_Rey_Origen[0]-1,Nueva_Ubicacion_Rey_Origen[1]+1] in Nueva_linea_Peligro:
    print("Movimiento en Haque") 
elif M[Nueva_Ubicacion_Rey_Origen[0]-1][Nueva_Ubicacion_Rey_Origen[1]+1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey_Origen[0]-1][Nueva_Ubicacion_Rey_Origen[1]+1]  == "_":
    print("posion Bloquedada ")
else:
    print("Posisicion libre")
    Posicioneslibre.append(True)



#verifica arriba isquierda
if [Nueva_Ubicacion_Rey_Origen[0]-1,Nueva_Ubicacion_Rey_Origen[1]-1] in Nueva_linea_Peligro:
    print("Movimiento en Haque") 
elif M[Nueva_Ubicacion_Rey_Origen[0]-1][Nueva_Ubicacion_Rey_Origen[1]-1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey_Origen[0]-1][Nueva_Ubicacion_Rey_Origen[1]-1]  == "_":
    print("posion Bloquedada ")
else:
    print("Posisicion libre")
    Posicioneslibre.append(True)

#verifica isquierda
if [Nueva_Ubicacion_Rey_Origen[0],Nueva_Ubicacion_Rey_Origen[1]-1] in Nueva_linea_Peligro:
    print("Movimiento en Haque") 
elif M[Nueva_Ubicacion_Rey_Origen[0]][Nueva_Ubicacion_Rey_Origen[1]-1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey_Origen[0]][Nueva_Ubicacion_Rey_Origen[1]-1]  == "|":
    print("posion Bloqueda ")
else:
    print("Posisicion libre")
    Posicioneslibre.append(True)


#verifica Derecha 
if [Nueva_Ubicacion_Rey_Origen[0],Nueva_Ubicacion_Rey_Origen[1]+1] in Nueva_linea_Peligro:
    print("Movimiento en Haque") 
elif M[Nueva_Ubicacion_Rey_Origen[0]][Nueva_Ubicacion_Rey_Origen[1]+1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey_Origen[0]][Nueva_Ubicacion_Rey_Origen[1]+1]  == "|":
    print("posion Bloqueda ")
else:
    print("Posisicion libre")
    Posicioneslibre.append(True)


#verifica abajo Derecha 
if [Nueva_Ubicacion_Rey_Origen[0]+1,Nueva_Ubicacion_Rey_Origen[1]+1] in Nueva_linea_Peligro:
    print("Movimiento en Haque") 
elif M[Nueva_Ubicacion_Rey_Origen[0]+1][Nueva_Ubicacion_Rey_Origen[1]+1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey_Origen[0]+1][Nueva_Ubicacion_Rey_Origen[1]+1]  == "_":
    print("posion Bloqueda ")
else:
    print("Posisicion libre")
    Posicioneslibre.append(True)

#verifica abajo isquierda  
if [Nueva_Ubicacion_Rey_Origen[0]+1,Nueva_Ubicacion_Rey_Origen[1]-1] in Nueva_linea_Peligro:
    print("Movimiento en Haque") 
elif M[Nueva_Ubicacion_Rey_Origen[0]+1][Nueva_Ubicacion_Rey_Origen[1]-1] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey_Origen[0]+1][Nueva_Ubicacion_Rey_Origen[1]-1]  == "_":
    print("posion Bloqueda ")
else:
    print("Posisicion libre")
    Posicioneslibre.append(True)

#verifica abajo 
if [Nueva_Ubicacion_Rey_Origen[0]+1,Nueva_Ubicacion_Rey_Origen[1]] in Nueva_linea_Peligro:
    print("Movimiento en Haque") 
elif M[Nueva_Ubicacion_Rey_Origen[0]+1][Nueva_Ubicacion_Rey_Origen[1]] in N:
    print("ficha bloqueada")
elif M[Nueva_Ubicacion_Rey_Origen[0]+1][Nueva_Ubicacion_Rey_Origen[1]]  == "_":
    print("posion Bloqueda ")
else:
    print("Posisicion libre")
    Posicioneslibre.append(True)

if True in Posicioneslibre:
    print("Tiene Un Movimiento Libre")
    print("")
else:
    print("Haquemate")


