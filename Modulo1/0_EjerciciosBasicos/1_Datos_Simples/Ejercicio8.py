"""
Escribir un programa que pida
 al usuario dos números enteros
  y muestre por pantalla la <n> 
  entre <m> da un cociente <c> 
  y un resto <r> donde <n> y <m> 
  son los números introducidos por
   el usuario, y <c> y <r> son el 
   cociente y el resto de la división
    entera respectivamente.

1/05/2022
"""
numero1  = int(input("ingrese un numero >> "))
numero2 = int(input("Ingrese otro nuermero >> "))

numero3 = numero1 / numero2
print("El cociente de la operacion es " + str(numero3) )

numero3 = numero1 % numero2
print("EL residuo de la Operacion es >> " + str(numero3))