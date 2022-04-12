"""
2. Edita el programa Calculadora.py, en 
el que agregues opciones decorativas de 
menú y uses ASCII art. Recuerda aplicar 
las secuencias de escape.



Programa terminado  en el  11/04/2022  a las 7:24 pm 
"""
from os import system
system("cls")


#imprime la calculadora 

print("Bienvenidos a tu calculadora")
print("  _____________________                 ")   
print(" |  _________________  |                   ") 
print(" | | JO           0. | |                   ") 
print(" | |_________________| |                  ")  
print(" |  ___ ___ ___   ___  |                  ")  
print(" | | 7 | 8 | 9 | | + | |                  ")  
print(" | |___|___|___| |___| |                  ")  
print(" | | 4 | 5 | 6 | | - | |                  ")  
print(" |___|___|___| |___| | |                  ")  
print(" | | 1 | 2 | 3 | | x | |                  ") 
print(" |___|___|___| |___| | |                  ")  
print(" | | . | 0 | = | | / | |                  ")  
print(" |___|___|___| |___| | |                 ")  
print(" |_____________________|                  ")  


#inprime la lista de las opciones :D
print("Welcome a la super calculadora compax")
M = ["1_Suma","2_Resta","3_Multiplicación","4_Division","5_Potencia cuadrada"]
for i in range(5):
    print(M[i],end=' ')
    print()

while True:
    
    try: 

        #Pide los nummeros para realizar la operacion

        Resultado = 0
        Valor1 = int(input("Ingresa el valor 1: "))
        Valor2 = int(input("Ingresa el valor 2: "))

        Eleccion = 0
        print("Si deseas salir ingresa 0")
        Elecion = int(input("Ingresa el numero de la operacione que deseas ingresar: "))

        #Las los condicionales que validad la imformacion 

        if Elecion == 0:
            break
        elif Elecion == 1:
            Resultado = Valor1 + Valor2
            Eleccion = "Suma"

        elif Elecion == 2:
            Resultado = Valor1 - Valor2
            Eleccion = "Resta"


        elif Elecion == 3:
            Resultado = Valor1 * Valor2
            Eleccion = "Multiplicacion"

        elif Elecion == 4:
            Resultado = Valor1 / Valor2
            Eleccion = "Division"

        elif Elecion ==5:
            Resultado = Valor1 ** Valor2
            Eleccion = "Potencia cuadrada" 
        else:
            print("La opcion no existe")

        print(f"EL resultado dela {Eleccion}  es  {Resultado}")

    #captura los errores
    except ValueError:
        print("EL dato no esta permitido NO sea bobo le piden numeros ")
