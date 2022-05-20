#ultimo respaldo 

"""
Será que se puede crear el jeugo del agedrez en pyton con la consola..  yo no lo sé solo quiero intentarlo.... ajajajjajaja
Se inició este proyecto el dia 29/04/2022
"""
"""
horas concientes de inversion 5 horas  hasta las 8:28  del dia 9/05/2022    5 horas
dia 10/05/2022  el dia de ayer la mitad que hice no sirvio de mucho         1 hora    
11 / 05 / 2022                                                              1 hora  
12 / 05 / 2022                                                              2 horas perdidas     
13 / 05 / 2022                                                              3 horas  se logro identificar el bug XD y se corrigio una parte               
14/ 05 / 2022                                                               3 horas corrigiendo bugs   
15/05/ 2022                                                                 2 horas matando bugs  se aniquiláron los bug maximos no se si habra quedado despues de la aniquilacion maxima 
5:23 PM                                                                     un bug que me quitó el sueño lo pude haver aniquilado en un minuto y estuve horas aniquilandolo JAJAJAJAJAJA
16/05/2020       12:17 AM                                                    1 hora detalles y se puede hacer dos movimientos en la primera jugada 
17/ 05/ 1:12     1.13 AM                                                     1 :20 minutos  hora haciendo la funcionalidad del peon en la posicion 8 hace el cambio por otra ficha
                                                                             terminado  no XD me di cunta de un erorr gravisimo
18/05/2022       7:22 PM  - 9:16 PM                                         3 hora fin del peon y sus funcionalidades  + movimiento torre XD                                                                    
19 /05/2022                                                                 3 horas movimiento de la reina 
20 /05/2022      
"""


"""

contolar si tiene una ficha bloqueda al frente para luego devolver el movimiento                                     anikilado estubo lleno de bugs  tarde mas de 4 horas buscandolo no sabia como hacer esta funcionalidad lo logré
para terminar con el peon debes verificar si está en la primera movida para luego permitirle los dos pasos           finikitado estuvo facil no hubo bugs se me ocurrio a la primerra
falta verificar si el pen está en la utltima posiscion y sisi entonces el peon se convierte en una reina o la que decida el jugador   finikitado XD  no hubo bugs agresivos solo un error 

#la toree
debe verificar si la torre que tiene em frente para recorrer y a la dereccha


 si todo sale mal en el padado has esto XD SISISIISISIISISISIIS    #si se bloquea con las otras fichas debes modificar para se ejecute si solo es un peon es un peon
 elimina todo 
"""
from ast import Break
from asyncio import sleep
from os import system
from pickle import TRUE
from time import time
import math


#todas las funciones importantes

B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]


Fichas_Blancas = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
Fichas_Negras= ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]



M=[
    [" "," ","A","B","C","D","E","F","G","H"," "," "],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    ["8","|",N[1],N[3],N[5],N[4],N[2],N[5],N[3],N[1],"|","8"],
    ["7","|",N[0],N[0],N[0],B[0],N[0],N[0],N[0],N[0],"|","7"],
    ["6","|",".",".",".",".",".",".",".",".","|","6"],
    ["5","|",".",".",".",B[2],".",".",N[2],".","|","5"],
    ["4","|",N[1],".",".",".",B[1],".",".",N[1],"|","4"],
    ["3","|",".",".",".",".",".",".",".",".","|","3"],
    ["2","|",B[0],B[0],B[0],B[0],B[0],N[2],B[0],B[0],"|","2"],
    ["1","|",B[1],B[3],B[5],B[4],B[2],B[5],B[3],B[1],"|","1"],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    [" "," ","A","B","C","D","E","F","G","H"," "," "]
]
M.reverse()
for a in range(12):
    M[a].reverse()
    for b in range(12):
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
#funcion de la operacion
def Accion(jugador,n1,n2,n3,n4,n5,n6,n7,n8,n11,n12,n13,n14,n15,n16,n17,n18,Colorde_ficha,Colorde_ficha2):
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

    #la funcion cambia la pocision de la ficha.... 
    def Funcion_ingresaFicha(ingreso,ingreso2,LLave):
        while True:
            print(jugador)

            
            #controla la entrada 
            while True:
                try:
                    Numero_fila2 = int(input(ingreso2)) 
                    if Numero_fila2 > 0 and Numero_fila2 <9:
                        Letra_columna2 = input(ingreso)
                        if Letra_columna2.isalpha():
                            Letra_columna2 = Letra_columna2.lower()
                            if Letra_columna2 in letras:
                                break
                            else:
                                print("No sea pendejo XD")
                        else:
                            print("Error el caracter no está permitido ")
                
                except ValueError:
                    print("Es un error ")

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
                elif Ficha2 == Colorde_ficha[0] or Ficha2 == Colorde_ficha[1] or Ficha2 == Colorde_ficha[2] or Ficha2 == Colorde_ficha[3] and Ficha2 == Colorde_ficha[4] or Ficha2 == Colorde_ficha[5]:
                    print("Error de turno")
                #coloca el punto de la posisicon donde se movia
                else:

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
                        if Ficha2 in N:

                            if M[fila2+1][columna2] in B or M[fila2+1][columna2] == ".":
                                break
                            elif M[fila2-1][columna2] in B or M[fila2-1][columna2] == ".":
                                break
                            elif M[fila2][columna2+1] in B or  M[fila2][columna2+1] == ".":
                                break
                            elif M[fila2][columna2-1] in B or  M[fila2][columna2-1] == ".":
                                break
                            else:
                                print("La ficha está bloqueada")

                        elif Ficha2 in B:
                            if M[fila2+1][columna2] in N  or M[fila2+1][columna2] == ".":
                                break
                            elif M[fila2-1][columna2] in N or M[fila2-1][columna2] == ".":
                                break
                            elif M[fila2][columna2+1] in N or  M[fila2][columna2+1] == ".":
                                break
                            elif M[fila2][columna2-1] in N  or  M[fila2][columna2-1] == "." :
                                break
                            else:
                                print("La ficha está bloqueada")


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
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == "_":
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
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == "_":
                                   break

                                i = i + 1
                            #algoritmo arriba isquierda
                            i = 0
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i],Ubicacion_ficha[1]-i)
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == "_":
                                    break
                                i = i + 1 
                            #algoritmo isquierda 
                            i = 0
                            while True:
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]],Ubicacion_ficha[1]-i)
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == "_":
                                    break
                                i = i + 1 
                            #algoritmo Derecha
                            i = 0
                            while True:
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]],Ubicacion_ficha[1]+i)
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "_":
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
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == "_":
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
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == "_":
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
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == "_":
                                    break

                                i = i + 1



                        #Verifica si está bloqueada a su alrededor 
                        #arriba 
                        print(COLOR_ELEGIDO1)
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                           
                            Super_Algoritmo()    
                           
                            break
                        #arriba derecha
                        elif M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                            Super_Algoritmo()
                            break
                        #arriba isquierda
                        elif M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] == "."or  not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            Super_Algoritmo()
                            break
                        #derecha
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "." or not  M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                            Super_Algoritmo()
                            break
                        #isquierda
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            Super_Algoritmo()
                            break
                        #abajo 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                            Super_Algoritmo()
                            break
                        #abajo derecha 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                            Super_Algoritmo()
                            break
                        #abajo isquierda 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            Super_Algoritmo()
                            break
                        else:
                            print("La ficha está bloqueada")


                    



                        
                    else:
                        print(Ficha2)
                        # M[fila2][columna2]="."
                        break

           

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
                            if Posicion_Relativa[0] == 8:
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
                            if Movimento_relativo[0] == 2:
                                system("cls")
                                LAS_fichas_del_cambio = ["\u2656","\u2655","\u2658","\u2657"]
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
                            if Posicion_Relativa[0] == 8:
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
                            if Movimento_relativo[0] == 2:
                                system("cls")
                                LAS_fichas_del_cambio = ["\u265C","\u265B","\u265E","\u265D"]
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
                        print("La torre se encuentra en la posicion  ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("El Peon se mover a la posicion ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])
                        
                        Movimientos_Permitidos = []
                        #los colores
                        def ALgoritmo_dela_Torre(Color_Ficha,Color_Ficha2):
                            #ficha negra

                            ##guarda las possiconoes de la ficcha 
                            Posicion_Relativa.clear() 
                            Posicion_Relativa.append(Ubicacion_ficha[0])
                            Posicion_Relativa.append(Ubicacion_ficha[1])

                            #limpia los moviemintos y luego los igresa
                            Movimientos_Permitidos.clear()

                            #el el Algoritmo que buscará las fichas verticalmente hacia riba 
                            iterador = 1
                            while True:
                                if M[Posicion_Relativa[0]-iterador][Posicion_Relativa[1]] == ".":
                                    Movimientos_Permitidos.append(Posicion_Relativa[0]-iterador)
                                    Movimientos_Permitidos.append(Posicion_Relativa[1])

                                elif M[Posicion_Relativa[0]-iterador][Posicion_Relativa[1]] in Color_Ficha:
                                    break
                                        
                                elif M[Posicion_Relativa[0]-iterador][Posicion_Relativa[1]] in Color_Ficha2:
                                    Movimientos_Permitidos.append(Posicion_Relativa[0]-iterador)
                                    Movimientos_Permitidos.append(Posicion_Relativa[1])
                                    break
                                

                                iterador = iterador + 1

                            #algoritmo de busqueda hacia abajo
                            iterador2 = 0
                            while True:
                                if M[Posicion_Relativa[0]+iterador2][Posicion_Relativa[1]] == ".":
                                    Movimientos_Permitidos.append(Posicion_Relativa[0]+iterador2)
                                    Movimientos_Permitidos.append(Posicion_Relativa[1])

                                elif  M[Posicion_Relativa[0]+iterador2][Posicion_Relativa[1]] in Color_Ficha2:
                                    break
                                elif M[Posicion_Relativa[0]+iterador2][Posicion_Relativa[1]] in Color_Ficha:
                                    Movimientos_Permitidos.append(Posicion_Relativa[0]+iterador2)
                                    Movimientos_Permitidos.append(Posicion_Relativa[1])

                                    break
                                iterador2 = iterador2 + 1
                           
                            #algoritmo de busqueda hacia derecha
                            iterador3 = 0
                            while True:
                                if M[Posicion_Relativa[0]][Posicion_Relativa[1]+iterador3] == ".":
                                    Movimientos_Permitidos.append(Posicion_Relativa[0])
                                    Movimientos_Permitidos.append(Posicion_Relativa[1]+iterador3)

                                elif M[Posicion_Relativa[0]][Posicion_Relativa[1]+iterador3] in Color_Ficha2:
                                    break
                                elif M[Posicion_Relativa[0]][Posicion_Relativa[1]+iterador3] in Color_Ficha:
                                    Movimientos_Permitidos.append(Posicion_Relativa[0])
                                    Movimientos_Permitidos.append(Posicion_Relativa[1+iterador3])

                                    break
                                iterador3 = iterador3 + 1
                            
                            #algoritmo de busqueda hacia abajo
                            iterador4 = 0
                            while True:
                                if M[Posicion_Relativa[0]][Posicion_Relativa[1]-iterador4] == ".":
                                    Movimientos_Permitidos.append(Posicion_Relativa[0])
                                    Movimientos_Permitidos.append(Posicion_Relativa[1]-iterador4)
                                
                                elif M[Posicion_Relativa[0]][Posicion_Relativa[1]-iterador4] in Color_Ficha2:
                                    break
                                elif M[Posicion_Relativa[0]][Posicion_Relativa[1]-iterador4] in Color_Ficha:
                                    Movimientos_Permitidos.append(Posicion_Relativa[0])
                                    Movimientos_Permitidos.append(Posicion_Relativa[1]-iterador4)

                                    break
                                iterador4 = iterador4 + 1

                            #los movimientos 
                            Movimento_relativo.clear()
                            Movimento_relativo.append(Ubicacion_ficha[2])
                            Movimento_relativo.append(Ubicacion_ficha[3])

                            #Comprueba los movimientos XD
                            Movimienos = 0
                            Cantidad = math.trunc(len(Movimientos_Permitidos)/2)
                            for i in range(Cantidad):
                                if Movimientos_Permitidos[Movimienos] == Movimento_relativo[0]:
                                    if Movimientos_Permitidos[Movimienos+1] == Movimientos_Permitidos[1]:
                                        LLave_cambio_posicion.pop(0)
                                        LLave_cambio_posicion.append(True)
                                else:
                                    print("Movimiento no permitido el movimiento está fuera de rango")
                                Movimienos = Movimienos + 2



                        if Colorde_ficha == B:
                            ALgoritmo_dela_Torre(N,B)
                        elif Colorde_ficha == N:
                            ALgoritmo_dela_Torre(B,N)






                            
                        
                    elif La_ficha == reina:
                        #Reina
                        print("El peon esta en ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("El Peon se mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimientos_permitidos_Reina)
                        
                        for i in range(len(Movimientos_permitidos_Reina)):
                            for  j in range(1):
                                print(Movimientos_permitidos_Reina[i][j] )
                                print(Movimientos_permitidos_Reina[i][j+1] )
                                print(Movimientos_permitidos_Reina[i][j]+1)
                                if Movimento_relativo[0] == Movimientos_permitidos_Reina[i][j] and  Movimento_relativo[1] == Movimientos_permitidos_Reina[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                                   
                        
                    elif La_ficha == caballo:
                        #caballo
                        pass
                    elif La_ficha == rey:
                        #reY
                        pass
                    elif La_ficha == arfil:
                        #Arfil 
                        pass
                    
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
    
    Funcion_ingresaFicha("Ingrese La letra de la ficha >> ","Ingrese EL numero de la ficha >> ",True)
    
    Funcion_ingresaFicha("Letra donde Desea mover la ficha>> ","Numero donde Desea Mover la ficha >> ",False)
    

Contador_cambio = 2
while True:
    
    #hace que cambien de occion van rotando las acciones...
    if Contador_cambio %2 == 0:
        # se pasa por parametro las poscciones de la letra dentro de la matriz M
        # y el Color de ficha que verifica si le corresponde el juego 
        Accion("Jugador1",2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,N,B)

    else:
        Accion("Jugador2",9,8,7,6,5,4,3,2,9,8,7,6,5,4,3,2,B,N)
        
    Contador_cambio = Contador_cambio + 1


