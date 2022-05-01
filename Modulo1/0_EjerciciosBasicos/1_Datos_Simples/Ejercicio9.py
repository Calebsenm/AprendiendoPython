"""
Escribir un programa que 
pregunte al usuario una 
cantidad a invertir, el 
interés anual y el número 
de años, y muestre por pantalla 
el capital obtenido en la inversión.

Fiquitado el 1/05/2022
"""

dinero = int(input("Porfavor ingrese el dinero a invertir >> "))
interez = int(input("Ingrese el interes anual >> "))
años = int(input("Ingrese La cantidad de años a invertir >> "))



a  = 0
while True:
    Dinero_Total = (dinero * interez /100 ) + dinero
    print(Dinero_Total)
    dinero = Dinero_Total

    if a == años:
        break
    a = a + 1

print(f"Su dinero total es de {Dinero_Total} $")