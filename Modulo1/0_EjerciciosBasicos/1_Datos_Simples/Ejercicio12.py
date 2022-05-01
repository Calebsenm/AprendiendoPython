"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ 
cada una. El pan que no es el día tiene un 
descuento del 60%. Escribir un programa que 
comience leyendo el número de barras vendidas 
que no son del día. Después el programa debe 
mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y 
el coste final total.

finikitado el 1/05/2022

"""
Barras_Pan = 3.49
Descuento_Panes = 60

print(f"Una barra de pan fresca cuesta {Barras_Pan}")
print(f"EL descuento es del {Descuento_Panes} %")
print(f"El precio del pan con un {Descuento_Panes}% de descuento es de {Barras_Pan-(Barras_Pan*60/100):.4f} $")

