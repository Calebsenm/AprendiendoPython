# Ejercicio 1
# Escribir una función que aplique 
# un descuento a un precio y otra 
# que aplique el IVA a un precio. 
# Escribir una tercera función que 
# reciba un diccionario con los precios 
# y porcentajes de una cesta de la compra, 
# y una de las funciones anteriores, 
# y utilice la función pasada para aplicar 
# los descuentos o el IVA a los productos 
# de la cesta y devolver el precio final de 
# la cesta.

#finikitado was easy 
#5:00pm   26/06/2022 


def Descuento(Precio,descuento):
    return  Precio - Precio * descuento / 100

def Iva(Precio,iva):
    return Precio + Precio * iva / 100

def Precios(Diccionario,funcion):
    Diccionario2 = {}
    for i,j in Diccionario.items():
        Diccionario2[funcion(i,j)] = j

    return Diccionario2


print(Descuento(100,10)) 
print(Iva(100,10))
print(Precios({100:10, 120:15,1000:85},Iva))