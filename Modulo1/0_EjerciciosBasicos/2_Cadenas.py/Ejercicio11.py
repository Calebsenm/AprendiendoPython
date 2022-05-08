"""
Escribir un programa que pregunte 
el nombre el un producto, su precio 
y un número de unidades y muestre por 
pantalla una cadena con el nombre del 
producto seguido de su precio unitario 
con 6 dígitos enteros y 2 decimales, el 
número de unidades con tres dígitos y el 
coste total con 8 dígitos enteros y 2 decimales.


"""

Nombre = input("Ingrese el nombre del producto >> ")
Precio = float(input("Ingrese el precio >> "))
Numero_unidades = float(input("Ingrese el numero de unidades >> "))

print(f"el {Nombre} Cuesta {Precio} Numero de productos {Numero_unidades :.0f} total = {Numero_unidades*Precio :.2f}$")
