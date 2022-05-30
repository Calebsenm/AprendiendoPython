M =[ 
    [1,0,0,1],
    [1,0,0,1],
    [0,1,0,1]
]

text_file = open('Text.py','a')

for i in range(len(M)):
    for j in range(1,4,1):
        print(M[i][j],end= " ")
        text_file.write(str(f"print( {[i,j]})"))
    print()
 


print("U+1F617")


