"""
Será que se puede crear el jeugo del agedrez en pyton con la consola..  yo no lo sé solo quiero intentarlo.... ajajajjajaja
Se inició este proyecto el dia 29/04/2022
"""
from os import system
from pickle import TRUE

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
#funcion de la operacion
   
def Accion(jugador,n1,n2,n3,n4,n5,n6,n7,n8,n11,n12,n13,n14,n15,n16,n17,n18,Colorde_ficha):
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
            if LLave1 == False:
                #esta llave activa si se puede hacer el movimiento o no 
                llave_veryficacion = 0

                def Algoritmo(La_ficha):
                    #Aqui de de ir el algorimo que coloca las posibilidades de la ficha 
                    #verifica que ficha es 
                    

                    if LFicha[0] == Colorde_ficha[0]:
                        #peon
                        Posicion_ficha = [fila2,columna2]

                        #debes definir la posicion del peon y verificar que tien en frente
                        #deves activar la funcion de cierre para que el cambio se efectue
                        


                        pass
                    elif LFicha[0] == Colorde_ficha[1]:
                        #Torre
                        pass
                    elif LFicha[0] == Colorde_ficha[2]:
                        #Reina
                        pass
                    elif LFicha[0] == Colorde_ficha[3]:
                        #caballo
                        pass
                    elif LFicha[0] == Colorde_ficha[4]:
                        #reY
                        pass
                    elif LFicha[0] == Colorde_ficha[5]:
                        #Arfil 
                        pass
                    
                Algoritmo(LFicha[0])

                #coloca el la ficha en la posicion colocada
                if llave_veryficacion == True:

                    M[fila2][columna2] = LFicha[0]
                    break
    #Se pasqa por parametros las occiones y una llave que activa la opcion de eleccion o la opcion de colocar fica 
    Funcion_ingresaFicha("Ingrese La letra de la ficha >> ","Ingrese EL numero de la ficha >> ",True)
    #trae la posicion de la ficha
    fila2 = LFicha[0]
    Ficha_elegida =fila2
    Funcion_ingresaFicha("Letra donde Desea mover la ficha>> ","Numero donde Desea Mover la ficha >> ",False)
    

Contador_cambio = 2
while True:
    
    #hace que cambien de occion van rotando las acciones...
    if Contador_cambio %2 == 0:
        # se pasa por parametro las poscciones de la letra dentro de la matriz M
        # y el Color de ficha que verifica si le corresponde el juego 
        Accion("Jugador1",2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,N)

    else:
        Accion("Jugador2",9,8,7,6,5,4,3,2,9,8,7,6,5,4,3,2,B)
    Contador_cambio = Contador_cambio + 1


