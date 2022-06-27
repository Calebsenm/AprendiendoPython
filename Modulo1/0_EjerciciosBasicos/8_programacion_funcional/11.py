# Ejercicio 11
# Escribir una función que reciba 
# una muestra de números y devuelva 
# los valores atípicos, es decir, los 
# valores cuya puntuación típica sea 
# mayor que 3 o menor que -3. Nota: 
# La puntuación típica de un valor se 
# obtiene restando la media y dividiendo 
# por la desviación típica de la muestra.


def Funcion(A):
    Valores_atipicos = []
    Medi = 0
    desviacion = 0
    
    for i in A:
        Medi += i
        desviacion += i ** 2

    Media = Medi / len(A)
    desviacion = (desviacion/(len(A))-(Medi/ len(A))**2)**(1/2)

  
    for k in A:
        l = (k - Media) / desviacion
        if l < -3 or l > 3:
            Valores_atipicos.append(k)

    return Valores_atipicos

print(Funcion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))





