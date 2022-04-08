"""
4.Crea un programa que se llame Calculadora.py y
que calcule la suma, la resta, la multiplicación,
la división y la potencia cuadrada.


7/04/2022
"""
from os import system
system("cls")

#inprime la lista de las opciones :D
print("Welcome a la super calculadora compax")
M = ["1_Suma","2_Resta","3_Multiplicación","4_Division","5_Potencia cuadrada"]
for i in range(5):
    print(M[i],end=' ')
    print()

while True:
    
    try: 
        Resultado = 0
        Valor1 = int(input("Ingresa el valor 1: "))
        Valor2 = int(input("Ingresa el valor 2: "))

        Eleccion = 0
        print("Si deseas salir ingresa 0")
        Elecion = int(input("Ingresa el numero de la operacione que deseas ingresar: "))

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

    except ValueError:
        print("EL dato no esta permitido NO sea bobo le piden numeros ")


    

