"""
Escribir un programa que lea un entero positivo, n
, introducido por el usuario y después muestre
 en pantalla la suma de todos los enteros desde 1 hasta n.
  La suma de los  primeros enteros positivos puede 
  ser calculada de la siguiente forma:

  suma = (n(n+1)) / 2

30 / 04 / 2022

"""

Numero = int(input("Ingresa un numero entero >> "))

Suma = (Numero * (Numero + 1)) / 2

print(f" La suma de de los numeros desde 1 un hasta {Numero} es {Suma}")