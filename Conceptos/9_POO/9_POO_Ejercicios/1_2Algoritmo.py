#simulacion del algoritmo 
#este es un espermiento la rama primcipa els el 1_2Algoritmo.py


B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]

print(B)
print(N)

M=[
    [" "," ","A","B","C","D","E","F","G","H"," "," "],
    [" ","_","_","_","_","_","_","_","_","_","_"," "],
    ["8","|",B[4],".",N[4],".",B[5],".",B[2],B[2],"|","8"],
    ["7","|",".",".",".",".",".",".",".",".","|","7"],
    ["6","|",".",".",".",".",".",".",".",B[1],"|","6"],
    ["5","|",".",".",".",".",".",".",".",".","|","5"],
    ["4","|",B[1],".",".",".",".",B[3],".",".","|","4"],
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



