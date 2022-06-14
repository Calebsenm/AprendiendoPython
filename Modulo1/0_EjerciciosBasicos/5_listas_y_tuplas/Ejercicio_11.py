"""
Ejercicio 11
Escribir un programa que almacene los vectores 
(1,2,3) y  en dos listas y muestre por 
pantalla su producto escalar.

Easy  3:43PM 
13/06/2022
"""

A = (1,2,3)
B = (-1,0,2)


Resultado = 0
i = 0
while i != len(A):
    Resultado = Resultado + A[i]*B[i]
    i += 1 

print(f"El producto escalar es {Resultado}")


