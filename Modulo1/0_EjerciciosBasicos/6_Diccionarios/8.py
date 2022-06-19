"""
Ejercicio 8
Escribir un programa que 
cree un diccionario de 
traducción español-inglés. 
El usuario introducirá las 
palabras en español e inglés 
separadas por dos puntos, y 
cada par <palabra>:<traducción>
separados por comas.
El programa debe crear un 
diccionario con las palabras 
y sus traducciones. 
Después pedirá una frase en español
y utilizará el diccionario para 
traducirla palabra a palabra. 
Si una palabra no está en el
diccionario debe dejarla sin traducir.
"""

dic = {}
palabra = input("Ingresa una plabra y su ytaduccion al ingles separados por : ")
dic[palabra[:":"]] = palabra[":":]
print(dic)