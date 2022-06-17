# Ejercicio 3
# Escribir un programa que guarde 
# en un diccionario los precios de 
# las frutas de la tabla, pregunte 
# al usuario por una fruta, un número 
# de kilos y muestre por pantalla el 
# precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe 
# mostrar un mensaje informando de ello.

# patano 1.35
# manzana 0.80
# pera 0.85
# naranja 0.70

#easy xd 12:07 pm
#15/06/2022

Frutas = {
    "patano": 1.35,
    "manzana" : 0.80,
    "pera" : 0.85,
    "naranja" : 0.70
}

fruta = input("Please input a frute ->")


price = 0
if fruta in Frutas:
    kile = input ("Input the K ->")
    price = Frutas[fruta] * float(kile)

    print("EL precio es ",price) 
else:
    print("the frute does not exist ")