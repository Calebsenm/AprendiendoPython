"""
Será que se puede crear el jeugo del agedrez en pyton con la consola..  yo no lo sé solo quiero intentarlo.... ajajajjajaja
Se inició este proyecto el dia 29/04/2022
"""
"""
horas concientes de inversion 5 horas  hasta las 8:28  del dia 9/05/2022
                                
"""
from os import system
from pickle import TRUE
from time import time

from numpy import sort
from pygame import Color


#todas las funciones importantes

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

#la ubicacion de fila y ocoluman para colocar la ficha
LFicha = [""]

#no se me ocurrio otra manera esta llave sirve para activar el la accion de mover ficha a la posisicon asignada
LLave_cambio_posicion = [""]

#Almacena la ubicacion de la ficha
Ubicacion_ficha = []

#se guardarán los movimientos permitidos
MovimientoPeon = []














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

            Numero_fila2 = int(input(ingreso2))
            Letra_columna2 = input(ingreso)

            
            
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
            if LLave == True:
                #guarda donde esta
                Ubicacion_ficha.append(fila2)
                Ubicacion_ficha.append(columna2)
            elif LLave == False:
                #guarda donde se moverá
                Ubicacion_ficha.append(fila2)
                Ubicacion_ficha.append(columna2)
            else:
                print("Nada por aqui nada por allá")

                

            if LLave == True:
            
                #Muestra que ficha es......
                Ficha2 = M[fila2][columna2]

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
                    print(Ficha2)
                    M[fila2][columna2]="."
                    break


            LLave1 = LLave
            #esta llave activa si se puede hacer el movimiento o no 
            llave_veryficacion = 0

            if LLave1 == False:
                

                def Algoritmo(La_ficha,peon,torre,reina,caballo,rey,arfil):
                    #Aqui de de ir el algorimo que coloca las posibilidades de la ficha 
                    #verifica que ficha es 
                    
                    #Algoritmo del peon
                    #Ve que ficha es i apartir de eso empiezan los algoritmos
                    if La_ficha == peon:
                        #debes definir la posicion del peon 
                        Posicion_ficha = [fila2,columna2]
                        print(Posicion_ficha)
                        a = input("")
                        #voy a definir si está en la primera posicion o no ficha negra 
                        if Ubicacion_ficha[0] == M[8]:
                            
                            if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == ".":
                                #pocicion libre
                                MovimientoPeon.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]])
                            
                            elif M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]]==".":
                                MovimientoPeon.append([Ubicacion_ficha[0]-2,Ubicacion_ficha[1]])
                            #verifica si la posccion permitida es igual  la posicion ingresada para luego guardarla
                            if MovimientoPeon[0][0]  == Ubicacion_ficha[2] and MovimientoPeon[0][1] == Ubicacion_ficha[3]:
                                #esta es para confirmar el cambio :D 
                                LLave_cambio_posicion.append(True)
                                LLave_cambio_posicion.pop(0)
                            elif MovimientoPeon[1][0]  == Ubicacion_ficha[2] and MovimientoPeon[1][1] == Ubicacion_ficha[3]:
                                #esta es para confirmar el cambio :D 
                                LLave_cambio_posicion.append(True)
                                LLave_cambio_posicion.pop(0)
                            #LIMPIA LAS POCCICIONES :D
                            Ubicacion_ficha.clear()
                        #hace el movimiento si la ficha ya no está en la posicion inicial
                        else:
                            if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == ".":
                                #pocicion libre
                                MovimientoPeon.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]])
                            #verifica si la posccion permitida es igual  la posicion ingresada para luego guardarla
                            if MovimientoPeon[0][0]  == Ubicacion_ficha[2] and MovimientoPeon[0][1] == Ubicacion_ficha[3]:
                                #esta es para confirmar el cambio :D 
                                LLave_cambio_posicion.append(True)
                                LLave_cambio_posicion.pop(0)
                            #LIMPIA LAS POCCICIONES :D
                            Ubicacion_ficha.clear()




                        #si es ficha blanca 
                        if Ubicacion_ficha[0] == M[3]:
                            if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == ".":
                                #pocicion libre
                                MovimientoPeon.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]])
                            
                            elif M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]]==".":
                                MovimientoPeon.append([Ubicacion_ficha[0]+2,Ubicacion_ficha[1]])
                            #verifica si la posccion permitida es igual  la posicion ingresada para luego guardarla
                            if MovimientoPeon[0][0]  == Ubicacion_ficha[2] and MovimientoPeon[0][1] == Ubicacion_ficha[3]:
                                #esta es para confirmar el cambio :D 
                                LLave_cambio_posicion.append(True)
                                LLave_cambio_posicion.pop(0)
                            elif MovimientoPeon[1][0]  == Ubicacion_ficha[2] and MovimientoPeon[1][1] == Ubicacion_ficha[3]:
                                #esta es para confirmar el cambio :D 
                                LLave_cambio_posicion.append(True)
                                LLave_cambio_posicion.pop(0)
                            #LIMPIA LAS POCCICIONES :D
                            Ubicacion_ficha.clear()
                        #hace el movimiento si la ficha ya no está en la posicion inicial
                        else:
                            if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == ".":
                                #pocicion libre
                                MovimientoPeon.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]])
                            #verifica si la posccion permitida es igual  la posicion ingresada para luego guardarla
                            if MovimientoPeon[0][0]  == Ubicacion_ficha[2] and MovimientoPeon[0][1] == Ubicacion_ficha[3]:
                                #esta es para confirmar el cambio :D 
                                LLave_cambio_posicion.append(True)
                                LLave_cambio_posicion.pop(0)
                            #LIMPIA LAS POCCICIONES :D
                            Ubicacion_ficha.clear()









                        #verificar que tien en frente
                        #deves activar la funcion de cierre para que el cambio se efectue
                        


                        
                    elif La_ficha == torre:
                        #Torre
                        pass
                    elif La_ficha == reina:
                        #Reina
                        pass
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

                    M[fila2][columna2] = LFicha[0]
                    break
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


