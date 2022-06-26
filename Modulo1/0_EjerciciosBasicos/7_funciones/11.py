# Ejercicio 11
# Escribir un programa que reciba 
# una cadena de caracteres y devuelva 
# un diccionario con cada palabra que 
# contiene y su frecuencia. Escribir 
# otra función que reciba el diccionario 
# generado con la función anterior y 
# devuelva una tupla con la palabra más 
# repetida y su frecuencia.

#estubo interesante y entretenido 
#con la opsicion de mis padres terminer JAJAJAJAJJA

#fin  11:17 PM El dia 25/06/2022
#
def Palabras(palabras):
    lista = palabras.split(" ")
    Diccionario = {}

    Flecha1 = 0
    Flecha2 = 0
    Repeticiones = 0

    while True:
        while True:

            if lista[Flecha1] == lista[Flecha2]:
                Repeticiones += 1
                Diccionario[lista[Flecha1]] = Repeticiones 

            if len(lista)-1 == Flecha2:
                Diccionario[lista[Flecha1]] = Repeticiones 
                break 
            Flecha2 += 1
        
        if len(lista)-1 == Flecha1:
            break
        Flecha1 += 1
        Flecha2 = 0
        Repeticiones = 0

    return Diccionario
        
def Tupla(Dic):
    OL = []
    for i,o in Dic.items():
        OL.append(o)
    OL.sort()
    OL.reverse()

    di = 0
    a = 0
    for s,h in Dic.items():
        if h == OL[di]:
            lk = s,h
            a =  tuple(lk)
            break
        di += 1
    return a





texto = input("Ingresa un parrafo > ")

print(Palabras(texto))
print(Tupla(Palabras(texto)))
