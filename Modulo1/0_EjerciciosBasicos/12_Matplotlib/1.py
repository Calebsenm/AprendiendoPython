# Ejercicio 1
# Escribir un programa que pregunte al usuario 
# por las ventas de un rango de años y muestre 
# por pantalla un diagrama de líneas con la 
# evolución de las ventas.

import matplotlib.pyplot as plt

inicio = int(input("Incicio -> "))
fin = int(input("Fin -> "))

Ventas = {}

for i  in range(inicio,fin+1):
    Ventas[i] = input(f"Ingresa el numero del año {str(i)} -> ")



# para la grafiquita ___

fig, ax = plt.subplots()
# Dibujamos la línea con las ventas a partir del diccionario
ax.plot(Ventas.keys(), Ventas.values())
# Mostarmos el gráfico por pantalla
plt.show()
