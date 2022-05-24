#simulacion del algoritmo 



B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]

Ubicacion_Rey = []
Linea_De_peligro = []
M=[
    [" "," ","A","B","C","D","E","F","G","H"," "," "],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    ["8","|",N[1],N[3],N[5],N[4],N[2],N[5],N[3],N[1],"|","8"],
    ["7","|",N[0],N[0],N[0],N[0],N[0],N[0],N[0],N[0],"|","7"],
    ["6","|",".",".",".",".",".",".",".",".","|","6"],
    ["5","|",".",".",".",".",".",".",".",".","|","5"],
    ["4","|",".",".",".",".",N[1],".",".",".","|","4"],
    ["3","|",".",".",".",".",".",".",".",".","|","3"],
    ["2","|",B[0],B[0],B[0],".",B[0],B[0],B[0],B[0],"|","2"],
    ["1","|",B[1],B[3],B[5],B[4],B[2],B[5],B[3],B[1],"|","1"],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    [" "," ","A","B","C","D","E","F","G","H"," "," "]
]

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
if M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]] in B:
    #color contrario 
    CONJUNTO_FICHA = N
elif M[Nueva_Ubicacion_Rey[0]][Nueva_Ubicacion_Rey[1]] in N:
    CONJUNTO_FICHA = B



while True:
    #ataque hacia arriba
    A = 1
    while True:
        if M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]] == CONJUNTO_FICHA[1] or M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]] == CONJUNTO_FICHA[2]  :
            print("Está en hake")

        if  M[Nueva_Ubicacion_Rey[0]-A][Nueva_Ubicacion_Rey[1]] == ".":
            Linea_De_peligro.append([Nueva_Ubicacion_Rey[0]-A,Nueva_Ubicacion_Rey[1]])
        else:
            break 
        
    
        A = A + 1
    break
    #ataque arriba derecha
    #ataque arriba isquierda
    #ataque Derecha
    #ataque isquierda
    #ataque derecha abajo
    #ataque isquierda abajo
    #ataque abajo

    #ataque del caballo

print(Linea_De_peligro)