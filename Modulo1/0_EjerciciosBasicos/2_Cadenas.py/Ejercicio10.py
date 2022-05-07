#Escribir un programa 
# que pregunte por consola 
# por los productos de una 
# cesta de la compra, separados 
# por comas, y muestre por pantalla 
# cada uno de los productos en una línea 
# distinta.

#finikitado el 7/05/2022   2 horitas bien interesantes JAJAJAJA

from ast import Break
from os import system
system("cls")

M  = []
M2 = [0]

LLave1 = 1

while True:
    print("Por favor ingrese los producto \nde una compra separados por comas ")
    Productos = input(">> ")

  
    if  "," in Productos[0] or "," in Productos[len(Productos)-1]:
        print("No esta permitida una coma al principio o al final ")
    elif not "," in Productos or "." in Productos or "-" in Productos or "_" in Productos or " " in Productos or  "+" in Productos:
        print("El caracter no está permitido")
    else:
        break

for i in range(len(Productos)):
    if "," in Productos[i]:
        M2.append(i)

LLave = 2
for i in range(len(M2)-1):
    if LLave == 2:
        M.append(Productos[M2[i]:M2[i+1]])
    else:
        M.append(Productos[M2[i]+1:M2[i+1]])
    if LLave == len(M2):
        M.append(Productos[M2[i+1]+1:len(Productos)])
    LLave = LLave + 1

for i in range(len(M)):
    print(f"{i+1}. {M[i]}",end="\n")



