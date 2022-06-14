"""
Escribir un programa que pida al 
usuario una palabra y muestre por 
pantalla el número de veces que 
contiene cada vocal.

easy 2:45 pm  el 13/06/2022
"""

def Algo(A,B):
    for i in A:
        B.append(i)


M = []
word = input("Please input a word > ")
a,e,i,o,u = 0,0,0,0,0
WOrd = []
Algo(word,M)
for  ai in M:
    if ai == "a":
        a += 1
    if ai == "e":
        e += 1
    if ai == "i":
        i += 1
    if ai == "o":
        o += 1
    if ai == "u":
        u += 1
WOrd.append([["a",a],["e",e],["i",i],["o",o],["u",u]])

for i in WOrd[0]:
    print(f"La Vocal {i[0]} se repite {i[1]} veces")
