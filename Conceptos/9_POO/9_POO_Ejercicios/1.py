#rama EXPERIMENTAL 2 
from os import system
import math
from time import process_time



#todas las funciones importantes

B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]


Fichas_Blancas = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
Fichas_Negras= ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]

#fichas blancas

#peones
P1B = B[0]
P2B = B[0]
P3B = B[0]
P4B = B[0]
P5B = B[0]
P6B = B[0]
P7B = B[0]
P8B = B[0]

#Caballo
C1B = B[3]
C2B = B[3]

#Arfil 
A1B = B[5]
A2B = B[5]

#torres
T1B = B[1]
T2B = B[1]

#rey y reina
RB = B[4]
DB = B[2]

#fichas negras

#peones
P1N = N[0]
P2N = N[0]
P3N = N[0]
P4N = N[0]
P5N = N[0]
P6N = N[0]
P7N = N[0]
P8N = N[0]

#Caballo
C1N = N[3]
C2N = N[3]

#Arfil 
A1N = N[5]
A2N = N[5]

#torres
T1N = N[1]
T2N = N[1]

#rey y reina
RN = N[4]
DN = N[2]




M=[
    ["+","-","-","-","-","-","-","-","-","-","-","-","-","+"],
    ["|","*","*","A","B","C","D","E","F","G","H","*","*","|"],
    ["|","*","+","-","-","-","-","-","-","-","-","+","*","|"],
    ["|","8","|",T1N,C1N,A1N,DN,RN,A2N,C2N,T2N,"|","8","|"],
    ["|","7","|",P1N,P2N,P3N,P4N,P5N,P6N,P1N,P8N,"|","7","|"],
    ["|","6","|",".",".",".",".",".",".",".",".","|","6","|"],
    ["|","5","|",".",".",".",".",".",".",".",".","|","5","|"],
    ["|","4","|",".",".",".",".",".",".",".",".","|","4","|"],
    ["|","3","|",".",".",".",".",".",".",".",".","|","3","|"],
    ["|","2","|",P1B,P2B,P3B,P4B,P5B,P6B,P7B,P8B,"|","2","|"],
    ["|","1","|",T1B,C1B,A1B,DB,RB,A2B,C2B,T2B,"|","1","|"],
    ["|","*","+","-","-","-","-","-","-","-","-","+","*","|"],
    ["|","*","*","A","B","C","D","E","F","G","H","*","*","|"],
    ["+","-","-","-","-","-","-","-","-","-","-","-","-","+"],
]
M.reverse()
for a in range(14):
    M[a].reverse()
    for b in range(14):
        a = 0



#la ubicacion de fila y ocoluman para colocar la ficha
LFicha = [""]

#no se me ocurrio otra manera esta llave sirve para activar el la accion de mover ficha a la posisicon asignada
LLave_cambio_posicion = [""]

#Almacena la ubicacion de la ficha
Ubicacion_ficha = [0,0,0,0]

#se guardarán los movimientos permitidos
MovimientoPeon = []

#congunti de posisiciones
letras = ["a","b","c","d","e","f","g","h"]
#movimientos no permitidos XD 

Movimientos_no_Permitidos = [0,0]

#llave super maestra
llave_supermaestra = [True]


#Movimientos permitidos de la reina 
Movimientos_permitidos_Reina = []
#movimientos torre
Movimientos_Torre = []

#movimientos permitidos del arfil 
Movimiento_Arfil  = []

#Movimiento Cabalo
Movimiento_caballo = []

#Movimiento rey permitido 
Movimiento_Rey = []

#Moviemintos en hake 

#funcion de la operacion
def Accion(jugador,n1,n2,n3,n4,n5,n6,n7,n8,n11,n12,n13,n14,n15,n16,n17,n18,Colorde_ficha,Colorde_ficha2,Color_Variable1,Color_Variable2):
    system("cls")
        
    print("Las fichas..")
    print(". ".join(B))
    print(". ".join(N))
    print()


    M.reverse()
        
    for i in range(14):
            
        M[i].reverse()
        for j in range(14):
            print(M[i][j],end = ' ') 
        print()

    #la funcion cambia la pocision de la ficha.... 
    def Funcion_ingresaFicha(ingreso,ingreso2,LLave):
        while True:
            print(jugador)
            #Algoritmo Magistral 2
#________________________________________________________________________________________________________________________________________________________
            Nueva_linea_Peligro = []


            #ataque 
            Ubicacion_Todas_fichas_Arriba= []
            Ubicacion_Todas_fichas_Abajo= []
            #ataques de las fichas de arriba 
            Todos_Los_posiblesAtaques_Arriba = []
            #ataque de las fichas de ababjp
            Todos_Los_posiblesAtaques_Abajo = []
            




            #buscará las fichas 
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if M[i][j] in Colorde_ficha:
                        Ubicacion_Todas_fichas_Arriba.append([i,j])
                    if M[i][j] in Colorde_ficha2:
                        Ubicacion_Todas_fichas_Abajo.append([i,j])

            # print("Ubicacion de las fichas De Arriba arriba")
            # print(Ubicacion_Todas_fichas_Arriba)
            # print("Ubicacion de las fichas De abajo")
            # print(Ubicacion_Todas_fichas_Abajo)


            #este es un clico que va recorreindo todas las posiciones de las fichas de arriba 
            #fichas de arriba 
            def Algorimit_maximous(Color_variable,Color_Opuesto,Ubicacion,Ataques,Operador_positivo,Operador_negativo):
                for a in range(len(Ubicacion)):

                    # si son peones......
                    if M[ Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[0]:
                        # print(M[ Ubicacion_Todas_fichas_Arriba[a][0]][Ubicacion_Todas_fichas_Arriba[a][1]])
                        #derecha 
                        if  M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_negativo] in Color_Opuesto or M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_negativo] == ".":
                            Ataques.append([ Ubicacion[a][0]+Operador_positivo,Ubicacion[a][1]+Operador_negativo])
                        #isquierda
                        if  M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_positivo] in Color_Opuesto or M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_positivo] == ".":
                            Ataques.append([ Ubicacion[a][0]+Operador_positivo,Ubicacion[a][1]+Operador_positivo])
                    
                    # ##########################################################################################################################################
                    #si es un rey 
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[4]:
                        #arriba
                        def Algoritmo_deciciones_rey(Diagonal,Vertical):
                            if M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] in Color_Opuesto or M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] == ".":
                                Ataques.append([Ubicacion[a][0]+Diagonal,Ubicacion[a][1]+Vertical])
                        #arriba                                              #abajo                                #Derecha                                       isquierda                                     #arriba Derecha                                                 #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_deciciones_rey(Operador_positivo,0),Algoritmo_deciciones_rey(Operador_negativo,0),Algoritmo_deciciones_rey(0,Operador_positivo),Algoritmo_deciciones_rey(0,Operador_negativo),Algoritmo_deciciones_rey(Operador_positivo,Operador_positivo),Algoritmo_deciciones_rey(Operador_positivo,Operador_negativo), Algoritmo_deciciones_rey(Operador_negativo,Operador_positivo),Algoritmo_deciciones_rey(Operador_negativo,Operador_negativo)
                        
                    # ##########################################################################################################################################
                    ## ******************************************************************************************************************************************
                    #si es una reina
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[2]:
                        def Algoritmo_Deciciones_Reina(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    break
                                
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba                                         #abajo                                          #Derecha                                       isquierda                                     #arriba Derecha                                                 #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Reina(Operador_positivo,0),Algoritmo_Deciciones_Reina(Operador_negativo,0),Algoritmo_Deciciones_Reina(0,Operador_positivo),Algoritmo_Deciciones_Reina(0,Operador_negativo),Algoritmo_Deciciones_Reina(Operador_positivo,Operador_positivo),Algoritmo_Deciciones_Reina(Operador_positivo,Operador_negativo), Algoritmo_Deciciones_Reina(Operador_negativo,Operador_positivo),Algoritmo_Deciciones_Reina(Operador_negativo,Operador_negativo)

                    # ******************************************************************************************************************************************
                    ## ******************************************************************************************************************************************
                    #si es un arfil 
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[5]:
                        def Algoritmo_Deciciones_Arfil(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    break
                                
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba Derecha                                                  #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Arfil(Operador_positivo,Operador_positivo),Algoritmo_Deciciones_Arfil(Operador_positivo,Operador_negativo), Algoritmo_Deciciones_Arfil(Operador_negativo,Operador_positivo),Algoritmo_Deciciones_Arfil(Operador_negativo,Operador_negativo)
                    
                    # ******************************************************************************************************************************************
                    # Si es una torre
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[1]:
                        def Algoritmo_Deciciones_Torre(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    break
                                
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba                                         #abajo                                          #Derecha                                        #isquierda                                    
                        Algoritmo_Deciciones_Torre(Operador_positivo,0),Algoritmo_Deciciones_Torre(Operador_negativo,0),Algoritmo_Deciciones_Torre(0,Operador_positivo),Algoritmo_Deciciones_Torre(0,Operador_negativo)

                    # ####################################################################################################################################################
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[3]:
                        def Algoritmo_Deciciones_Caballo(Diagonal,Vertical):
                            if M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] in Color_Opuesto or M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] == ".":
                                Ataques.append([Ubicacion[a][0]+Diagonal,Ubicacion[a][1]+Vertical])
                            
                        # L arriba Derecha                                                                                                                                           #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Caballo(Operador_negativo + Operador_negativo,Operador_positivo)
                        # L arriba isquierda
                        Algoritmo_Deciciones_Caballo(Operador_negativo + Operador_negativo,Operador_negativo)
                        # L Derecha arriba 
                        Algoritmo_Deciciones_Caballo(Operador_negativo,Operador_positivo + Operador_positivo)
                        # L Derecha Abajo 
                        Algoritmo_Deciciones_Caballo(Operador_positivo,Operador_positivo + Operador_positivo)
                        # L Isquierda Arriba
                        Algoritmo_Deciciones_Caballo(Operador_negativo,Operador_negativo + Operador_negativo)
                        # L Isquierda Abajo 
                        Algoritmo_Deciciones_Caballo(Operador_positivo,Operador_negativo + Operador_negativo)
                        # L Abajo Derecha                        
                        Algoritmo_Deciciones_Caballo(Operador_positivo + Operador_positivo,Operador_positivo)
                        # L Abajo isquierda
                        Algoritmo_Deciciones_Caballo(Operador_positivo + Operador_positivo,Operador_negativo)
                    
                        
 



            #Las fichas de arriba 
            Algorimit_maximous(Color_Variable2,Color_Variable1,Ubicacion_Todas_fichas_Arriba,Todos_Los_posiblesAtaques_Arriba,+1,-1)
            #las fuchas de abajo
            Algorimit_maximous(Color_Variable1,Color_Variable2,Ubicacion_Todas_fichas_Abajo,Todos_Los_posiblesAtaques_Abajo,-1,+1)
        

            # print("Estos son todos los ataques de las fichas De arriba ")
            # print(Todos_Los_posiblesAtaques_Arriba)
            
            # print("Estos son todos los ataques de las fichas De abajo ")
            # print(Todos_Los_posiblesAtaques_Abajo)
            
            Linea_del_ataque_hacia_el_rey = []

            for a in range(len(Ubicacion_Todas_fichas_Abajo)):
                if M[Ubicacion_Todas_fichas_Abajo[a][0]][Ubicacion_Todas_fichas_Abajo[a][1]] == Color_Variable1[4]:
                    POSICION = [Ubicacion_Todas_fichas_Abajo[a][0],Ubicacion_Todas_fichas_Abajo[a][1]] 
                    if POSICION in Todos_Los_posiblesAtaques_Arriba:
                        print("El REY ESTá en HAAKE")

                    # Iterador = 1
                    # while True:
                    #     if M[POSICION[0]][POSICION[1]] == ".":
                        

                    



#______________________________________________________________________________________________________________________________________________________________


         
            #Pide la entrada modificada

            while True:
                input_ficha = input(f"{ingreso2} {ingreso}")
                if len(input_ficha) == 2:
                    if input_ficha[1] in letras:
                        if not input_ficha[0].isalpha():
                            if int(input_ficha[0]) > 0 and int(input_ficha[0]) <9:
                                if input_ficha[1].isalpha():
                                    break
                                else:
                                    print("Se equivocó ingresando jugada")
                            else:
                                print("Se equivocó ingresando jugada")
                        else:    
                            print("Se equivocó ingresando jugada")
                    else:
                        print("Se equivocó ingresando jugada")
                else:    
                    print("Se equivocó ingresando jugada")

            Numero_fila2 = int(input_ficha[0])
            Letra_columna2 = input_ficha[1]

            #la convierte en mayuscula si es minuscula 
            Letra_columna2 = Letra_columna2.upper()
            
            
            
            #Funcion que cambia las opciones
            
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
                print("Error")
        
            #GUARDARÁ LA POSICION DE LA FICHA PASANDO COMO LLAVE TRUE O FALSE
        
            #esta llave activa si se puede hacer el movimiento o no 


            LLave1 = LLave
            
            

           
            if LLave1 == True:
                #guarda donde esta
                Ubicacion_ficha.clear()
                Ubicacion_ficha.append(fila2)
                Ubicacion_ficha.append(columna2)

                #Va a calcular todos los ataques de todas las fichas XD 
            elif LLave1 == False:
                #la limpia

                Ubicacion_ficha.append(0)
                Ubicacion_ficha.append(0)
                Ubicacion_ficha.pop(2)
                Ubicacion_ficha.pop(2)
              

                #guarda donde se moverá
                Ubicacion_ficha.append(fila2)
                Ubicacion_ficha.append(columna2)

                #elimina los ceros de la posicion agregada
                if 0 in Ubicacion_ficha:
                    Ubicacion_ficha.pop(2)
                    Ubicacion_ficha.pop(2)


            else:
                print("Nada por aqui nada por allá")

                

            if LLave1 == True:
            
                #Muestra que ficha es......
                Ficha2 = M[fila2][columna2]
                #frente
                Ficha3 = M[fila2-1][columna2]
                #isquierdda
                Ficha4 = M[fila2-1][columna2-1]
                #derecha 
                Ficha5 = M[fila2-1][columna2+1]

                #guarda la posicion de la ficha tomada
                LFicha.append(Ficha2)
                LFicha.pop(0)
                
                #verifica la ficha elegida y está bacia
                if Ficha2 ==".":
                    print("La ficha no existe")
                


                #verifica si ha ingresado una ficha contraria
                elif Ficha2 == Colorde_ficha[0] or Ficha2 == Colorde_ficha[1] or Ficha2 == Colorde_ficha[2] or Ficha2 == Colorde_ficha[3] or Ficha2 == Colorde_ficha[4] or Ficha2 == Colorde_ficha[5]:
                    print("Error de turno")
                #coloca el punto de la posisicon donde se movia
                else:
                    print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])
                    
                    #Este es el algoritmo Super ultra  maestro 100% hacker Pro mil quitasueño
                    # Sirve para Verificar si está en haque o Haquemate 
                    #-----------------------------------------------------------------------------------------------------
                    # ____________________________________________________________________________________________________ 

                    #si se bloquea con las otras fichas debes modificar para se ejecute si solo es un peon es un peon
                    #SI es un peon   permite identificar que ficha tiene en frente y a sus lads para ver si el peon está bloqueado 
                    if Ficha2 == B[0] or Ficha2 ==N[0]:
                        #verifica si está bloqueado por las pociciones 
                        print(f"{Ficha2}{Ficha3}{Ficha4}{Ficha5}")
                        #ficha blanca 
                        if Ficha3 in B or Ficha3 in N:
                            #si la ficha es blanca 
                            if Ficha2 in B:
                                if Ficha4 in N :
                                    break
                                elif Ficha5 in N:
                                    break
                                else: 
                                    print("Error La ficha blanca está bloqueada")
                            elif Ficha2 in N:
                                if Ficha4 in B :
                                    break
                                elif Ficha5 in B:
                                    break
                                else: 
                                    print("Error La ficha negra esta bloqueda ")
                        else:
                            print(Ficha2)
                            # M[fila2][columna2]="."
                            break
                    
                    #si es una torre
                    if Ficha2 == B[1] or Ficha2 == N[1]:
                        Movimientos_Torre.clear()
                        print("Es la torre")
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])
                        
                        #Color de la ficha elegida 
                        COLOR_ELEGIDO2 = 0

                         #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[1]:
                            #es una ficha blanca
                            COLOR_ELEGIDO2 = Fichas_Blancas 
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[1]:
                            #es una ficha negra 
                            COLOR_ELEGIDO2 = Fichas_Negras
                        print(COLOR_ELEGIDO2)
                        print("!")

                        #Posicion actual
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        #algoritmo 
                        def Algoritmo_Torre():
                        #el algoritmo que busca hacia arriba
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == ".":
                                    Movimientos_Torre.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]])

                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO2:
                                    Movimientos_Torre.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO2 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == "_":
                                    break

                                i = i + 1
                             #algoritmo Derecha
                            i = 1
                            while True:
                                print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i])
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_Torre.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO2:
                                    Movimientos_Torre.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO2 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "|":
                                    break
                                i = i + 1 
                            #algoritmo isquierda
                            i = 1
                            while True:
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_Torre.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO2:
                                    Movimientos_Torre.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO2 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == "_":
                                    break
                                i = i + 1 

                             #el algoritmo que busca hacia abajo
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == ".":
                                    Movimientos_Torre.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO2:
                                    Movimientos_Torre.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO2 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == "_":
                                    break

                                i = i + 1
                       #Verifica si está bloqueada a su alrededor 
                        #arriba 
                        print(COLOR_ELEGIDO2)
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] in COLOR_ELEGIDO2 and M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] != "-":
                           
                            Algoritmo_Torre()  
                            break
                       
                        #derecha
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO2 and M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] != "|":
                            Algoritmo_Torre()
                            break
                        #isquierda
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO2 and M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] != "|":
                            Algoritmo_Torre()
                            break
                        #abajo 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] in COLOR_ELEGIDO2 and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] != "-":
                            Algoritmo_Torre()
                            break
                    
                        else:
                            print("La ficha está bloqueada")
                        
                    # else:
                    #     print(Ficha2)
                    #     # M[fila2][columna2]="."
                    #     break

                       


                    #Algoritmo de reina posiciones permitidas 
                    if Ficha2 == B[2] or Ficha2 == N[2]:
                        Movimientos_permitidos_Reina.clear()

                        print("Es una reina")
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        #color de la ficha elegida
                        COLOR_ELEGIDO1 = 0
                        #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[2]:
                            #es una ficha blanca
                            COLOR_ELEGIDO1 = Fichas_Blancas 
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[2]:
                            #es una ficha negra 
                            COLOR_ELEGIDO1 = Fichas_Negras

                        #Posicion actual
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        #ALgoritmo ficha
                        def Super_Algoritmo():
                            #el algoritmo que busca hacia arriba
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == "-":
                                    break

                                i = i + 1

                            #el algoritmo que busca hacia arriba derecha
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == "+":
                                   break

                                i = i + 1
                            #algoritmo arriba isquierda
                            i = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == "+":
                                    break
                                i = i + 1 
                            #algoritmo isquierda 
                            i = 1
                            while True:
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == "|":
                                    break
                                i = i + 1 
                            #algoritmo Derecha
                            i = 1
                            while True:
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] == "|":
                                    break
                                i = i + 1 
                            
                            #el algoritmo que busca hacia abajo
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == "-":
                                    break

                                i = i + 1
                            #el algoritmo que busca hacia abajo derecha 
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == "+":
                                    break

                                i = i + 1
                            
                            #el algoritmo que busca hacia abajo isquierda
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == "+":
                                    break

                                i = i + 1



                        #Verifica si está bloqueada a su alrededor 
                        #arriba 
                        print(COLOR_ELEGIDO1)
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 and  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] != "-":
                           
                            Super_Algoritmo()    
                           
                            break
                        #arriba derecha
                        elif M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] != "+" :
                            Super_Algoritmo()
                            break
                        #arriba isquierda
                        elif M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] == "."or  not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1 and  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] != "+":
                            Super_Algoritmo()
                            break
                        #derecha
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "." or not  M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] != "|":
                            Super_Algoritmo()
                            break
                        #isquierda
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] != "|":
                            Super_Algoritmo()
                            break
                        #abajo 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] != "-":
                            Super_Algoritmo()
                            break
                        #abajo derecha 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] != "+":
                            Super_Algoritmo()
                            break
                        #abajo isquierda 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]!="+":
                            Super_Algoritmo()
                            break
                        else:
                            print("La ficha está bloqueada")


                    #esto es para el caballo
                    if Ficha2 == B[3] or Ficha2 == N[3]:
                        
                        Movimiento_caballo.clear()
                        print("Esto es un caballo")
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        Color_ficha_elegida  = 0
                        #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[3]:
                            #es una ficha blanca
                            Color_ficha_elegida = Fichas_Blancas 
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[3]:
                            #es una ficha negra 
                            Color_ficha_elegida = Fichas_Negras

                        #Posicion actual
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        #la llave incomprensible
                        llave_imcomprensible = [False]

                        #es ta es incompresible HHAHHAHAHHAHAHAHAHHAHA
                        #va moverse una posicion diagonal si siene un dianonal no pasa  luega en la nueva posicion
                        #va a buscar en frente y la isquierda si tiene un gion o si no permite agregar el movimiento           
                        #diagonal Derecha arriba 
                        while True:
                            if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1]== "-" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "+" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "|":  
                                if not M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]+1]== "-" :
                                    if not M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]+1] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]-2,Ubicacion_ficha[1]+1])
                                        llave_imcomprensible.append(True)
                                    
                                
                                if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+2]== "+" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+2]== "|":
                                    if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+2] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]+2])
                                        llave_imcomprensible.append(True)
                                        

                            #diagonal isquierda arriba 
                            if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1]== "-" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1]== "+"  or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1]== "|":  
                                if not M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]-1]== "-":
                                    if not M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]-1] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]-2,Ubicacion_ficha[1]-1])
                                        llave_imcomprensible.append(True)
                                        
                                
                                if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-2]== "|" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-2]== "+":
                                    if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-2] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]-2])
                                        llave_imcomprensible.append(True)
                                        

                            #digonal isquierda abajo
                            if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]== "-" or  not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]== "+"  or  not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]== "|":  
                                if not M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]-1]== "-":
                                    if not M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]-1] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]+2,Ubicacion_ficha[1]-1])
                                        llave_imcomprensible.append(True)
                                        
                                
                                if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-2]== "|" or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-2] == "+":
                                    if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-2] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]-2])
                                        llave_imcomprensible.append(True)
                                        

                            #diagonal iderecha abajo           
                            if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1]== "-" or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1]== "|"  or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1]== "+":  
                                if not M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]+1]== "-":
                                    if not M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]+1] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]+2,Ubicacion_ficha[1]+1])
                                        llave_imcomprensible.append(True)
                                        
                            
                                if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+2]== "|" or not  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+2]== "+":
                                    if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+2] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]+2])
                                        llave_imcomprensible.append(True)
                            break

                        #si sale mal solo colocas if llave_imcomprensible[0] == True   
                        if len(llave_imcomprensible) > 1:
                            llave_imcomprensible.clear()
                            break
                        else:
                            print("La ficha está bloquedad")
                        

                    #Esto es para el arfil 
                    if Ficha2 == B[5] or Ficha2 == N[5]:
                        Movimiento_Arfil.clear()

                        print("Esto es un arfil")
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        Color_ficha_elegida  = 0
                         #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[5]:
                            #es una ficha blanca
                            Color_ficha_elegida = Fichas_Blancas 
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[5]:
                            #es una ficha negra 
                            Color_ficha_elegida = Fichas_Negras

                        #Posicion actual
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        def Algorito_Arfil():
                            #el algoritmo que busca hacia arriba derecha
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == ".":
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] in Color_ficha_elegida:
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in Color_ficha_elegida or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == "+":
                                   break

                                i = i + 1
                            
                            #el algoritmo que busca hacia arriba isquierda
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == ".":
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in Color_ficha_elegida:
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in Color_ficha_elegida or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == "+":
                                   break

                                i = i + 1 

                            #el algoritmo que busca abajo  isquierda
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == ".":
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] in Color_ficha_elegida:
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] in Color_ficha_elegida or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == "+":
                                   break

                                i = i + 1 

                            #el algoritmo que busca abajo isquierda
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == ".":
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] in Color_ficha_elegida:
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] in Color_ficha_elegida or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == "+":
                                   break

                                i = i + 1 
                        
                        #Verifica si está bloqueada a su alrededor 
                      
                        #arriba derecha
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] in Color_ficha_elegida and M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] != "+" :
                            Algorito_Arfil()
                            break
                        #arriba isquierda
                        elif M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] == "."or  not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] in Color_ficha_elegida and  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] != "+":
                            Algorito_Arfil()
                            break
                      
                        #abajo derecha 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] in Color_ficha_elegida and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1]  != "+":
                            Algorito_Arfil()
                            break
                        #abajo isquierda 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] in Color_ficha_elegida and  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]  != "+":
                            Algorito_Arfil()
                            break
                        else:
                            print("La ficha está bloqueada")
                    
                    
                    
                    
                    #si es el rey
                    if Ficha2 == B[4] or Ficha2 == N[4]:
                        Movimiento_Rey.clear()

                        print("La ficha es el rey")
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        COLOR_ELEGIDO1  = 0
                         #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[4]:
                            #es una ficha blanca
                            COLOR_ELEGIDO1 = Fichas_Negras
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[4]:
                            #es una ficha negra 
                            COLOR_ELEGIDO1 = Fichas_Blancas 

                        #Posicion actual
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])



                        #Llava incomprensible 
                        hola = [False]
                        #Verifica si está bloqueada a su alrededor 
                        #arriba 
                        print(COLOR_ELEGIDO1)

                        Movimiento_permitido_arriba111 = [Ubicacion_ficha[0]-1,Ubicacion_ficha[1]]

                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == "." or  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:

                            if  Movimiento_permitido_arriba111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")

                            elif not Movimiento_permitido_arriba111 in Todos_Los_posiblesAtaques_Arriba:
                                    
                                Movimiento_Rey.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]])
                                hola.append(True)
                           
                        #arriba derecha
                        Movimiento_permitido_arriba_derecha111 = [Ubicacion_ficha[0]-1,Ubicacion_ficha[1]+1]
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "." or M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                            
                            if  Movimiento_permitido_arriba_derecha111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")

                            elif not Movimiento_permitido_arriba_derecha111 in Todos_Los_posiblesAtaques_Arriba:
                                Movimiento_Rey.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]+1])
                                hola.append(True)


                        #arriba isquierda
                        Movimiento_permitido_arriba_isquierda111 = [Ubicacion_ficha[0]-1,Ubicacion_ficha[1]-1]
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] == "."or  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            
                            if Movimiento_permitido_arriba_isquierda111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")
                            elif not Movimiento_permitido_arriba_isquierda111 in Todos_Los_posiblesAtaques_Arriba:
                                
                                Movimiento_Rey.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]-1])
                                hola.append(True)
                       
                        #derecha
                        Movimiento_permitido_Derecha111 = [Ubicacion_ficha[0],Ubicacion_ficha[1]+1]

                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "." or  M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                           
                            if Movimiento_permitido_Derecha111 in Todos_Los_posiblesAtaques_Arriba:
                               print("La posicion esta Siendo atacada no está permitido el movimiento")
                            elif not Movimiento_permitido_Derecha111 in Todos_Los_posiblesAtaques_Arriba: 

                                Movimiento_Rey.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+1])
                                hola.append(True)

                        #isquierda
                        Movimiento_Permitido_isquierda111 = [Ubicacion_ficha[0],Ubicacion_ficha[1]-1]

                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] == "." or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            
                            if Movimiento_Permitido_isquierda111  in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")

                            elif not  Movimiento_Permitido_isquierda111  in Todos_Los_posiblesAtaques_Arriba:
                                Movimiento_Rey.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-1])
                                hola.append(True)
                        #abajo 

                        Movimiento_abajo_111 = [Ubicacion_ficha[0]+1,Ubicacion_ficha[1]]

                        if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == "." or  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                            if Movimiento_abajo_111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")
                            elif not Movimiento_abajo_111 in Todos_Los_posiblesAtaques_Arriba:
                                Movimiento_Rey.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]])
                                hola.append(True)

                        #abajo derecha 
                        Movimiento_abajo_derecha111 = [Ubicacion_ficha[0]+1,Ubicacion_ficha[1]+1]

                        if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] == "." or M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                            
                            if Movimiento_abajo_derecha111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")
                            elif not Movimiento_abajo_derecha111 in Todos_Los_posiblesAtaques_Arriba:
                                Movimiento_Rey.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]+1])
                                hola.append(True)


                        #abajo isquierda 
                        Movimiento_abajo_isquierda111 = [Ubicacion_ficha[0]+1,Ubicacion_ficha[1]-1]

                        if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] == "." or M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            
                            if Movimiento_abajo_isquierda111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")

                            elif not Movimiento_abajo_isquierda111 in Todos_Los_posiblesAtaques_Arriba:

                                Movimiento_Rey.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]-1])
                                hola.append(True)

                        #verifica si está en hakemate

                        
                        if len(hola) > 1:
                            hola.clear()
                            break
                        else:
                            print("La ficha está bloqueada")
           

            if LLave1 == False:
                #posicion relativa de las fichas
                #ubicavion
                Posicion_Relativa = [0,0]
                #se moverá 
                Movimento_relativo = [0,0]

                def Algoritmo(La_ficha,peon,torre,reina,caballo,rey,arfil):
                    #Ve que ficha es, y  apartir de eso empiezan los algoritmos
                    if La_ficha == peon:
                        #peon 
                        print("El peon esta en ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("El Peon se mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])
                        
                        #Movimientos Permitidos 
                        Movimientos_Permitidos = [[1],[1]]
                        #que ficha es negra o blanca
                        if Colorde_ficha == N:
                            
                            #ficha negra

                            ##guarda las possiconoes de la ficcha 
                            Posicion_Relativa.clear() 

                            Posicion_Relativa.append(Ubicacion_ficha[0])
                            Posicion_Relativa.append(Ubicacion_ficha[1])

                            #limpia los moviemintos y luego los igresa
                            Movimientos_Permitidos.clear()
                            
                            
                            #si no se ha movido y esta en la pocicion inicial 2 de la casilla entonces permite hacer 2 movimientos 
                            if Posicion_Relativa[0] == 9:
                                print("El peon se encuentra en la primera casilla ")

                                o = 1
                                i = 0
                                while i < 2:
                                    if not M[Posicion_Relativa[0]-o][Posicion_Relativa[1]] in N or  M[Posicion_Relativa[0]-o][Posicion_Relativa[1]] in B:
                                        if M[Posicion_Relativa[0]-o][Posicion_Relativa[1]] == ".":
                                            Movimientos_Permitidos.append(Posicion_Relativa[0]-o)
                                            Movimientos_Permitidos.append(Posicion_Relativa[1])
                                        else:
                                            print("Error el Peon no Puede saltar una Ficha")
                                            break
                                    o = o + 1
                                    i = i + 1

                            
                            #verifica que tiene en frente
                            if M[Posicion_Relativa[0]-1][Posicion_Relativa[1]] == ".":

                                Movimientos_Permitidos.append(Posicion_Relativa[0]-1)
                                Movimientos_Permitidos.append(Posicion_Relativa[1])
                                                                    
                            #todo funciona OK :D        si la ficha no esta en los negros y no es igual a | y igual a un punto
                            # Verifica que tiene en la isquierda......
                
                            print(M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1])
                            
                            if not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1] in B :
                                if not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1] == ".":
                                    if  not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1] == "|":
                                
                                        Movimientos_Permitidos.append(Posicion_Relativa[0]-1)
                                        Movimientos_Permitidos.append(Posicion_Relativa[1]-1)
                            # verifica que tiene en la derecha .........
                            print(M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1])

                            if not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1] in B:
                                if not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1] == ".":
                                    if  not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1] == "|":
                                    
                                        Movimientos_Permitidos.append(Posicion_Relativa[0]-1)
                                        Movimientos_Permitidos.append(Posicion_Relativa[1]+1)

                            # aqui se verifican los movimientos  XD                        

                            Movimento_relativo.clear()
                            

                            Movimento_relativo.append(Ubicacion_ficha[2])
                            Movimento_relativo.append(Ubicacion_ficha[3])



                            #Si el peon llega a la ultima posicion entonces se le permite cambiar por una ficha
                            if Movimento_relativo[0] == 3:
                                system("cls")
                                LAS_fichas_del_cambio = [T1B,DB,C1B,A1B]
                                while True:
                                    print("Has llegado a la ultima posicion ahora puedes cambiar el peon por la ficha que deses ")
                                    for i in range(len(LAS_fichas_del_cambio)):
                                        print(f"{i+1} = {LAS_fichas_del_cambio[i]}.   ",end=" ")
                                        print()
                                    while True:
                                        try:
                                            
                                            Que_ficha = int(input("Por que fichas deseas remplasar el peon ingrese un numero "))

                                            if Que_ficha == 1:
                                                LFicha.pop(0)
                                                LFicha.append(LAS_fichas_del_cambio[0])
                                                break
                                            elif Que_ficha == 2:
                                                LFicha.pop(0)
                                                LFicha.append(LAS_fichas_del_cambio[1])
                                                break
                                            elif Que_ficha == 3:
                                                LFicha.pop(0)
                                                LFicha.append(LAS_fichas_del_cambio[2])
                                                break
                                            elif Que_ficha == 4:
                                                LFicha.pop(0)
                                                LFicha.append(LAS_fichas_del_cambio[3])
                                                break
                                            else:
                                                print("No sea pendejo este numero no existe")
                                        except ValueError:
                                            print("No sea bobo le pidieron un numero ")

                                    break
                            #recorre el movimiento lo divide en dos y busca si con iguales con la eleccion 
                            movi = 0
                            cantidad = len(Movimientos_Permitidos) /2
                            cantidad = math.trunc(cantidad)
                            for i in range(cantidad):

                                #si encuentra el movimiento igual al movimiento 
                                if Movimientos_Permitidos[movi] == Movimento_relativo[0]:
                                    if  Movimientos_Permitidos[movi+1] == Movimento_relativo[1] :
    
                                        #se activa toda la llave para hacer el cambio de ficha
                                        LLave_cambio_posicion.pop(0)
                                        LLave_cambio_posicion.append(True)
                                else:
                                    print("Movimiento Fuera de rango ")
                                    #isquierda
                                    print(M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1])
                                    #derecha
                                    print(M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1])
                                    
                                    print(Movimientos_Permitidos)
                                movi = movi + 2
                            
                        elif Colorde_ficha == B:
                            #ficha Blanca

                            ##guarda las posiciones de la ficcha 
                            Posicion_Relativa.clear()
                          
                            Posicion_Relativa.append(Ubicacion_ficha[0])
                            Posicion_Relativa.append(Ubicacion_ficha[1])

                            #limpia los moviemintos y luego los igresa
                            Movimientos_Permitidos.clear()

                             
                            #si peon esta en el primer movimiento permite hacer ingresa los movimientos permitidos 
                            if Posicion_Relativa[0] == 9:
                                print("El peon se encuentra en la primera casilla ")

                                o = 1
                                i = 0
                                while  i < 2:
                                    if not M[Posicion_Relativa[0]-o][Posicion_Relativa[1]] in N or  M[Posicion_Relativa[0]-o][Posicion_Relativa[1]] in B:
                                        if M[Posicion_Relativa[0]-o][Posicion_Relativa[1]] == ".":
                                            Movimientos_Permitidos.append(Posicion_Relativa[0]-o)
                                            Movimientos_Permitidos.append(Posicion_Relativa[1])
                                        else:
                                            print("Error La ficha no se puede saltar ")
                                            break

                                    o = o + 1
                                    i = i + 1
                            



                            
                            #verifica que tiene en frente
                            if M[Posicion_Relativa[0]-1][Posicion_Relativa[1]] == ".":

                                Movimientos_Permitidos.append(Posicion_Relativa[0]-1)
                                Movimientos_Permitidos.append(Posicion_Relativa[1])

                           
                            #todo funciona OK :D        si la ficha no esta en los negros y no es igual a | y igual a un punto
                            # Verifica que tiene en la isquierda......
                            #isquierda

                            print(M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1])
                            if not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1] in N:
                                if not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1] ==".": 
                                    if not M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1] == "|":
                                       
                                        Movimientos_Permitidos.append(Posicion_Relativa[0]-1)
                                        Movimientos_Permitidos.append(Posicion_Relativa[1]-1)
                            
                            print(M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1])
                            #Derecha
                            if  not  M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1] in N:
                                if not  M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1] == ".":
                                    if not  M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1] == "|":
                                       
                                        Movimientos_Permitidos.append(Posicion_Relativa[0]-1)
                                        Movimientos_Permitidos.append(Posicion_Relativa[1]+1)

                            
                            

                            Movimento_relativo.clear()
                        

                            Movimento_relativo.append(Ubicacion_ficha[2])
                            Movimento_relativo.append(Ubicacion_ficha[3])

                            
                             #Si el peon llega a la ultima posicion entonces se le permite cambiar por una ficha
                            if Movimento_relativo[0] == 3:
                                system("cls")
                                LAS_fichas_del_cambio = [T1N,DN,C1N,A1N]
                                while True:
                                    print("Has llegado a la ultima posicion ahora puedes cambiar el peon por la ficha que deses ")
                                    for i in range(len(LAS_fichas_del_cambio)):
                                        print(f"  {i+1} = {LAS_fichas_del_cambio[i]}      ",end=" ")
                                        print()
                                    while True:
                                        try:
                                            
                                            Que_ficha = int(input("Por que fichas deseas remplasar el peon ingrese un numero "))

                                            if Que_ficha == 1:
                                                LFicha.pop(0)
                                                LFicha.append(LAS_fichas_del_cambio[0])
                                                break
                                            elif Que_ficha == 2:
                                                LFicha.pop(0)
                                                LFicha.append(LAS_fichas_del_cambio[1])
                                                break
                                            elif Que_ficha == 3:
                                                LFicha.pop(0)
                                                LFicha.append(LAS_fichas_del_cambio[2])
                                                break
                                            elif Que_ficha == 4:
                                                LFicha.pop(0)
                                                LFicha.append(LAS_fichas_del_cambio[3])
                                                break
                                            else:
                                                print("No sea pendejo este numero no existe")
                                        except ValueError:
                                            print("No sea bobo le pidieron un numero ")

                                    break


                            
                            #recorre el movimiento lo divide en dos y busca si con iguales con la eleccion 
                            movi = 0
                            cantidad = len(Movimientos_Permitidos) /2
                            cantidad = math.trunc(cantidad)
                           
                            for i in range(cantidad):

                                #si encuentra el movimiento igual al movimiento 
                                if Movimientos_Permitidos[movi] == Movimento_relativo[0]:
                                    if Movimientos_Permitidos[movi+1] == Movimento_relativo[1] :

                                        LLave_cambio_posicion.pop(0)
                                        LLave_cambio_posicion.append(True)
                                else:
                                    print("Movimiento Fuera de rango ")
                                    print(Movimientos_Permitidos)
                                    print(M[Posicion_Relativa[0]-1][Posicion_Relativa[1]-1])
                                    print(M[Posicion_Relativa[0]-1][Posicion_Relativa[1]+1])

                                movi = movi + 2
                           
                    #EL algoritmo de la torre Torre 
                    elif La_ficha == torre:
                        #La torrre 
                        print("El la Torre esta en ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("La Torre se va a mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #los movimintos 
                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimientos_Torre)

                        for i in range(len(Movimientos_Torre)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimientos_Torre[i][j] and  Movimento_relativo[1] == Movimientos_Torre[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                                   

                        
                    elif La_ficha == reina:
                        #Reina
                        print("El la Reina esta en ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("La reina se va a mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimientos_permitidos_Reina)
                        
                        for i in range(len(Movimientos_permitidos_Reina)):
                            for  j in range(1):
                                # print(Movimientos_permitidos_Reina[i][j] )
                                # print(Movimientos_permitidos_Reina[i][j+1] )
                                # print(Movimientos_permitidos_Reina[i][j]+1)
                                if Movimento_relativo[0] == Movimientos_permitidos_Reina[i][j] and  Movimento_relativo[1] == Movimientos_permitidos_Reina[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                                   
                        
                    elif La_ficha == caballo:
                        #caballo
                        print("El el caballo ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("La Torre se va a mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        
                        #los movimintos 
                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimiento_caballo)

                        for i in range(len(Movimiento_caballo)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimiento_caballo[i][j] and  Movimento_relativo[1] == Movimiento_caballo[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 



                        
                    elif La_ficha == rey:
                        #Rey
                        print("El rey Está ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("El rey se va a mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #los movimintos 
                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimiento_Rey)

                        for i in range(len(Movimiento_Rey)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimiento_Rey[i][j] and  Movimento_relativo[1] == Movimiento_Rey[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                        
                    elif La_ficha == arfil:
                        #Arfil 
                        #imprime las posiciones 
                        print("El la Torre esta en ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("La Torre se va a mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #los movimintos 
                        #los movimientos 
                        #guarda los movimientos

                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimiento_Arfil)

                        #compara cada movimiento permitido de la ficha con el moviento ingresado si coinciden ingresa una llave 
                        for i in range(len(Movimiento_Arfil)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimiento_Arfil[i][j] and  Movimento_relativo[1] == Movimiento_Arfil[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                    
                #pasa la ficha y la posicion de la ficha cuando se selecciona
                Algoritmo(LFicha[0],peon=Colorde_ficha2[0],torre=Colorde_ficha2[1],reina=Colorde_ficha2[2],caballo=Colorde_ficha2[3],rey=Colorde_ficha2[4],arfil=Colorde_ficha2[5])

                #coloca el la ficha en la posicion colocada
                if LLave_cambio_posicion[0] == True:
                    #posiccion anterior
                    M[Posicion_Relativa[0]][Posicion_Relativa[1]] = "."
                    M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] = "."
                    #posicion de movimiento
                    M[fila2][columna2] = LFicha[0]

                    #limpia la llave para la proxima entrada
                    LLave_cambio_posicion.pop(0)
                    LLave_cambio_posicion.append(0)

                    break #si todo está ok pasa esto 

    #condicional supermaestro
    #Se pasqa por parametros las occiones y una llave que activa la opcion de eleccion o la opcion de colocar fica 
    
    Funcion_ingresaFicha("y La letra de la ficha >","Ingrese EL numero",True)
    
    Funcion_ingresaFicha("Letra donde Desea mover la ficha > ","Numero y ",False)
    

Contador_cambio = 2
while True:
    
    #hace que cambien de occion van rotando las acciones...
    if Contador_cambio %2 == 0:
        # se pasa por parametro las poscciones de la letra dentro de la matriz M
        # y el Color de ficha que verifica si le corresponde el juego 
        Accion("Jugador1",3,4,5,6,7,8,9,10,3,4,5,6,7,8,9,10,N,B,Fichas_Blancas,Fichas_Negras)

#
    else:
        Accion("Jugador2",10,9,8,7,6,5,4,3,10,9,8,7,6,5,4,3,B,N,Fichas_Negras,Fichas_Blancas)
        #limpia La ubicacion del rey
       

    Contador_cambio = Contador_cambio + 1


