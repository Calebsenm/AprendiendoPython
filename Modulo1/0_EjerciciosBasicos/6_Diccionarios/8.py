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

while True:
    palabra = input("Ingresa una plabra y su ytaduccion al ingles separados por : ")
    dic[palabra[:palabra.find(":")]] = palabra[palabra.find(":")+1:]
    print(dic)

    lol = input("Deseas gurdar palabras ingrese cualquier ficha de lo contrario ingresa no -> ")
    if lol == "no":
        break
la_frace = input("Ingresa la frace que deseas traducir -> ")
palabras = la_frace.split(" ")
Palabras2 = {}

o = 0
for i in palabras:
    if i in dic:
        Palabras2[o] = dic[i]
    else:
        Palabras2[o] = i

    o += 1

for i in Palabras2:
    print(Palabras2[i],end = " ")
