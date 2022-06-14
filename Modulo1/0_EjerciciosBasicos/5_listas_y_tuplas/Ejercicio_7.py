"""
Escribir un programa que almacene el abecedario en una 
lista, elimine de la lista las letras que ocupen posiciones 
múltiplos de 3, y muestre por pantalla la lista resultante.

finish 13/06/2022 2:06:PM
"""

ABCD = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
Mul = []
New = []
for i in range (1,100,3):
    Mul.append(i)

for i in range(len(ABCD)):
    if not i in Mul:
        New.append(ABCD[i])

for i in New:
    print(i,end = " ")



