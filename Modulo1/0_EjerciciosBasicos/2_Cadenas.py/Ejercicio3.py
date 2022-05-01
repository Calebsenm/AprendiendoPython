"""
Escribir un programa que pregunte 
el nombre del usuario en la consola y 
después de que el usuario lo introduzca 
muestre por pantalla <NOMBRE> tiene <n> 
letras, donde <NOMBRE> es el nombre de 
usuario en mayúsculas y <n> es el número
de letras que tienen el nombre.

finikitado el 1/05/2022

"""

nombre = input("ingresa tu nombre >> ")
print(f"{nombre.upper()} tiene {len(nombre)} letras ")

"""
ingresa tu nombre >> Caleb Seña MElo
CALEB SEÑA MELO tiene 15 letras 
"""