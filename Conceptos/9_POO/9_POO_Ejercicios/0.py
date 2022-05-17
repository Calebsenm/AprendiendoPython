#Este codigo es de respaldo 

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
1      5:23 PM                                                              un bug que me quitó el sueño lo pude haver aniquilado en un minuto y estuve horas aniquilandolo JAJAJAJAJAJA

      
"""


"""

contolar si tiene una ficha bloqueda al frente para luego devolver el movimiento                anikilado estubo lleno de bugs  tarde mas de 4 horas buscandolo no sabia como hacer esta funcionalidad lo logré
para terminar con el peon debes verificar si está en la primera movida para luego permitirle los dos pasos
falta verificar si el pen está en la utltima posiscion y sisi entonces el peon se convierte en una reina o la que decida el jugador 




 si todo sale mal en el padado has esto XD SISISIISISIISISISIIS    #si se bloquea con las otras fichas debes modificar para se ejecute si solo es un peon es un peon
 elimina todo 
"""
from asyncio import sleep
from os import system
from pickle import TRUE
from time import time
import math


#todas las funciones importantes

B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]





M=[
    [" "," ","A","B","C","D","E","F","G","H"," "," "],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    ["8","|",N[1],N[3],N[5],N[4],N[2],N[5],N[3],N[1],"|","8"],
    ["7","|",N[0],N[0],N[0],N[0],N[0],N[0],N[0],N[0],"|","7"],
    ["6","|",".",".",".",".",".",N[0],".",".","|","6"],
    ["5","|",".",".",".",".",".",".",".",".","|","5"],
    ["4","|",".",".",".",".",".",".",".",".","|","4"],
    ["3","|",".",".",".",".",B[0],".",".",".","|","3"],
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
Ubicacion_ficha = [0,0,0,0]

#se guardarán los movimientos permitidos
MovimientoPeon = []

#congunti de posisiciones
letras = ["a","b","c","d","e","f","g","h"]
#movimientos no permitidos XD 

Movimientos_no_Permitidos = [0,0]

#llave super maestra
llave_supermaestra = [True]

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
                Ficha3 =  M[fila2-1][columna2]

                #guarda la posicion de la ficha tomada
                LFicha.append(Ficha2)
                LFicha.pop(0)
                
                #verifica la ficha elegida y está bacia
                if Ficha2 ==".":
                    print("La ficha no existe")
                

                #si se bloquea con las otras fichas debes modificar para se ejecute si solo es un peon es un peon

               

                #verifica si ha ingresado una ficha contraria
                elif Ficha2 == Colorde_ficha[0] or Ficha2 == Colorde_ficha[1] or Ficha2 == Colorde_ficha[2] or Ficha2 == Colorde_ficha[3] and Ficha2 == Colorde_ficha[4] or Ficha2 == Colorde_ficha[5]:
                    print("Error de turno")
                #coloca el punto de la posisicon donde se movia
                else:

                    if Ficha2 == B[0] or Ficha2 ==N[0]:
                        if Ficha3 in B:
                            print("Error la ficha está bloqueada ")
                        elif Ficha3 in N:
                            print("Eror la ficha está bloqueada Si ")
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

                            #si peon esta en el primer movimiento 
                            


                            #limpia los moviemintos y luego los igresa
                            Movimientos_Permitidos.clear()
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

                            #verifica si tiene una                        

                            Movimento_relativo.clear()
                            

                            Movimento_relativo.append(Ubicacion_ficha[2])
                            Movimento_relativo.append(Ubicacion_ficha[3])
                            
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
                    #posiccion anterior
                    M[Posicion_Relativa[0]][Posicion_Relativa[1]]="."
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


