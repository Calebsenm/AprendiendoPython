"""
Ejercicio 4
Los teléfonos de una empresa 
tienen el siguiente formato 
prefijo-número-extension donde 
el prefijo es el código del país 
+34, y la extensión tiene dos dígitos 
(por ejemplo +34-913724710-56). 
Escribir un programa que pregunte
por un número de teléfono con este
formato y muestre por pantalla el 
número de teléfono sin el prefijo y 
la extensión.

medio finikitado.............
"""
print("un ejemplo del numero sería +57-3007838212141-56")
Numero_Telefono = input("Ingrese el numero de telefono con el prefijo y la extencion >>> ")

M = list(Numero_Telefono)
M[0]= " "
M[1]= " "
M[2]= " "
M[3]= " "
M[-0]= " "
M[-1]= " "
M[-2]= " "
M[-3]= " "
M = "".join(M)
print(M)
