"""
Ejercicio 3
Escribir un programa que pida al 
usuario un número entero positivo 
y muestre por pantalla todos los números 
impares desde 1 hasta ese número separados por comas.

inicio 12/ 04 / 2022 a las  4:42 pm 
Terminado 12 / 04/2022 a las 5:14 pm

"""


from time import process_time


numero = int(input("ingresa un numero entero positivo: "))
a = 0

print("Con ciclo while")
while a < numero:
    c = a % 2
    if c != 0:
        print(str(a ) + "," ,end=" ")
    a  = a + 1
print()
print("Con ciclo For")

for i in range (numero):
    a = i % 2
    if a != 0:
        print(f"{i},",end=" ")


    

