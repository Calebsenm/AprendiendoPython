"""
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

finikitado el 8/05/2022
"""

while True:
    numero1 = int(input("Ingresa el primer numero para dividir >> "))
    while True:
        numero2 = int(input("Ingresa el divisor >> "))
        if numero2 == 0:
            print("No se puede colocar el cero como divisor")
        else:
            break
    print(f"La Division es la siguiente {numero1 / numero2}")


