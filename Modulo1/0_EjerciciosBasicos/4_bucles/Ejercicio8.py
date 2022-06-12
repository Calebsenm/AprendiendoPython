"""
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

finikitado 11/06/2022   a las 11:16  20Minutos aprox la verdad no se
"""

el_numero = int(input("ingrese un numero > "))
if el_numero % 2 == 0:
    el_numero -=1

M = []
itere = 1
while True:
    M.insert(0,str(itere))
    itere +=2
    i = " ".join(M)
    print(i)
    if M[0] == str(el_numero):
        break
   