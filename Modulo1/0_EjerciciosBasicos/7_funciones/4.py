# Ejercicio 4
# Escribir una función que calcule el total 
# de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA 
# y el porcentaje de IVA a aplicar, y devolver 
# el total de la factura. Si se invoca la función 
# sin pasarle el porcentaje de IVA, deberá aplicar 
# un 21%.


def Funcion_iva(iva = 0,por = 21):
    producto = (iva * por)/100 + iva
    return producto

iva = input("Ingresa el dinero ")
por = input("ingresa el porcentaje de iva ")

Fun = Funcion_iva(int(iva),int(por))
print(f"El precio final es de {Fun}")

a = Funcion_iva(10)
print(a)