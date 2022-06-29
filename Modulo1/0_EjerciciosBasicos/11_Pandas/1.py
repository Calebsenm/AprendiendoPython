# Ejercicio 1
# Escribir un programa que pregunte al usuario 
# por las ventas de un rango de años y muestre 
# por pantalla una serie con los datos de las 
# ventas indexada por los años, antes y después 
# de aplicarles un descuento del 10%.

#Facil fue aprendiendo del ejercicio


import pandas as PA

inicio = int(input("Ingresa el año de inicio -> "))
fin = int(input("Ingresa el año de fin -> "))

Valores = {}
for i in range(inicio,fin+1):
    Valores[i] = int(input(f"Ingresa la venta del año {i} -> "))

Valores = PA.Series(Valores)
print("Ventas\n",Valores * 0.9)