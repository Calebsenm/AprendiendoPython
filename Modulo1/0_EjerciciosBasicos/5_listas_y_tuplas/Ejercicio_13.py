"""
Ejercicio 13
Escribir un programa que pregunte 
por una muestra de números, separados 
por comas, los guarde en una lista y 
muestre por pantalla su media y desviación 
típica.


"""



Conjunto = []
Los_numeros = input("Ingrese una lista de numeros separados por coma > ")
Los_numeros = Los_numeros.split(",")

b = len(Los_numeros)

for i in range(b):
    Los_numeros[i] = int(Los_numeros[i])

Los_numeros = tuple(Los_numeros)

sum = 0
sumasq = 0

for i in Los_numeros:
    sum += i
    sumasq += i**2

mean = sum/b

stdev = (sumasq/b-mean**2)**(1/2)
print(f"La media es {mean} y la desviacion tipica es {stdev}")



