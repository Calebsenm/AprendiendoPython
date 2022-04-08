"""
Crea un programa que se llame Entrada.py,
que permita leer correctamente los siguientes
tipos de datos: entero, flotante, booleano,
char, cadena
"""

try: 
    Flotante = float(input ("ingresa un valor flotante: "))
    print(Flotante)
    print(type)
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

try:
    Valor = int (input ("Ingresa un valor entero: "))
    print(Valor)
    print(type(Valor))

except ValueError:
    print("Oops!  That was no valid number.  Try again...")


try:
    Valor = input ("Ingresa un valor booleano: ")
    Valor  = bool(Valor)
    print(Valor)
    print(type(Valor))

except ValueError:
    print("Oops!  That was no valid number.  Try again...")


try:
    Valor = input ("Ingresa un valor str: ")
    Valor  = str(Valor)
    print(Valor)
    print(type(Valor))

except ValueError:
    print("Oops!  That was no valid number.  Try again...")

try:
    Valor = input ("ingresa una plabra")
    print(type(Valor))
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

