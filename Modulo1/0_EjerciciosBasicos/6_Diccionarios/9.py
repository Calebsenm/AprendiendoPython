"""
Ejercicio 9
Escribir un programa que gestione 
las facturas pendientes de cobro de 
una empresa. Las facturas se almacenarán 
en un diccionario donde la clave de cada 
factura será el número de factura y el 
valor el coste de la factura. El programa
debe preguntar al usuario si quiere añadir 
una nueva factura, pagar una existente o 
terminar. Si desea añadir una nueva factura 
se preguntará por el número de factura y su 
coste y se añadirá al diccionario. Si se desea 
pagar una factura se preguntará por el número 
de factura y se eliminará del diccionario. 
Después de cada operación el programa debe 
mostrar por pantalla la cantidad cobrada 
hasta el momento y la cantidad pendiente de cobro.
"""
# finikitado el 21/06/2022
# 6:00 pm 
dic = {}
hola_uno = ["1 -> añadir una nueva factura","2 -> Pagar una factura","3 -> salir"]


cobrado = 0
pendiente = 0

while True:
    for i in hola_uno:
        print(i)

    deci = input("Ingresa una decicion -> ")
    if deci == "1":
        num = input("Ingresa la id ")
        price = int(input("Ingresa el precio -> "))
        dic[num] = price

        pendiente += price

    elif deci == "2":
        num = input("Ingresa la id que deseas pagar -> ")
        hola = dic.pop(num, 0)

        cobrado += hola
        pendiente -= hola
        

    elif deci == "3":
        break
        
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
        