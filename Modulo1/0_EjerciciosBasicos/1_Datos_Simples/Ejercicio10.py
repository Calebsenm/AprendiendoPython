"""
Una juguetería tiene mucho 
éxito en dos de sus productos: 
payasos y muñecas. Suele hacer 
venta por correo y la empresa de 
logística les cobra por peso de 
cada paquete así que deben calcular 
el peso de los payasos y muñecas 
que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de 
payasos y muñecas vendidos en el último 
pedido y calcule el peso total del paquete que 
será enviado.

Finikitado 1/05/2022

"""

Payaso = 112
Muñeca = 75 

print("Vienvenido a La Tiena")
Payasos = int(input("Ingresa la cantidad de Payasos >> "))
Munecas = int(input("Ingresa La cantidad de Muñecas "))

Peso_Total = Payasos * Payaso + Munecas * Muñeca
print(f"La lista queda De la siguiente Manera \n{Payasos} Payasos \n{Munecas} Muñecas \nPeso Total {Peso_Total} KLG")