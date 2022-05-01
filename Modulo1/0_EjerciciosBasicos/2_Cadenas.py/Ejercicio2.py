"""
Ejercicio 2
Escribir un programa que pregunte el 
nombre completo del usuario en la consola 
y después muestre por pantalla el nombre 
completo del usuario tres veces, una con 
todas las letras minúsculas, otra con todas 
las letras mayúsculas y otra solo con la 
primera letra del nombre y de los apellidos 
en mayúscula. El usuario puede introducir su 
nombre combinando mayúsculas y minúsculas como 
quiera.

FINIKITADO 1/05/2022
"""

nombre1 = input("Ingresa tu Nombre >> ")
apellido1 = input("Ingresa tu appellido1 >> ")
apellido2 = input("Ingresa tu apellido2 >> ")

nombre = nombre1.lower(),apellido1.lower(),apellido2.lower()
nombre = " ".join(nombre)

print(nombre)

nombre = nombre.upper()
print(nombre)

nombre = nombre1.capitalize(),apellido1.capitalize(),apellido2.capitalize()
nombre = " ".join(nombre)
print(nombre)


"""
Ingresa tu Nombre >> HOLA 
Ingresa tu appellido1 >> COMO 
Ingresa tu apellido2 >> ESTAS
hola  como  estas
HOLA  COMO  ESTAS
Hola  Como  Estas
"""