"""
Ejercicio 5
Escribir un programa que almacene 
en una lista los números del 1 al 10 y 
los muestre por pantalla en orden inverso 
separados por comas.

9:19 PM
12/06/2022
"""


List = [1,2,3,4,5,6,7,8,9,10]
List.reverse()
for i in List:
    print(f"{i},",end=" ")