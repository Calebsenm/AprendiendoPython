"""

Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

renta                   tipo impositivo
menos de 10000          5%
entre 10000 y 20000     15%
entre 20000 y 35000     20%
entre 35000 y 60000     30%
masde 60000             45%


Escribe un programa que pregunte al usuario su renta
anual y muestre por pantalla el tipo inpositivo que 
le corresponde 


Finikitado el 11:28 Estuvo Hack
"""

V = [10000,20000,35000,60000]
P = [5,15,20,30,45]

renta = int(input("cual es su renta anual >> "))

if renta < 10000:
    print(f"Le corresponde {P[0]}%")

elif renta >= 10000 and renta < 20000:
    print(f"Le corresponde el {P[1]}%")

elif renta >= 20000 and renta <35000:
    print(f"Le corresponde el {P[2]}%")

elif renta >= 35000 and  renta <60000:
    print(f"Le corresponde el {P[3]}%")

elif renta >= 60000:
    print(f"le corresponde el {P[4]}%")

