"""
realiza la implemetacion de la funcionalidad que permita ingresar
datos al usuario y seleccionar la operacion a efectuar.

-Operaciones disponibles para la calculadora suma, resta,multiplicacion.logaritmo, coseno,seno, raiz cuadrada , convertir decimal a binario y binario adecimal

-Valida que las operaciones se puedan realizar, en caso contrario imprime un mensaje error

"""

import math

M = ["1 suma","2 multiplicacion","3 resta","4 multiplicacion","5 logaritmo","6 coseno","7 seno","8 Rais cuadrada","9 decimal a binario","10 binario a decimal"]

for i in range (9):
    print(M[i])


while True:
    
    desicion = int(input("ingresa el numero de la operacion que desas realizar >> "))
    

    if desicion == 1:
        numero1 = int(input("Por favor ingresa un numero >>> "))
        numero2 = int(input("Por favor ingresa el siguiente numero >>"))
        operacion = numero1 + numero2
        print(f"la suma es: {operacion}")

    elif desicion == 2:
        numero1 = int(input("Por favor ingresa un numero >>> "))
        numero2 = int(input("Por favor ingresa el siguiente numero >>"))
        operacion = numero1 - numero2
        print(f"la resta es: {operacion}")

    elif desicion == 3:
        numero1 = int(input("Por favor ingresa un numero >>> "))
        numero2 = int(input("Por favor ingresa el siguiente numero >>"))
        operacion = numero1 * numero2
        print(f"la operacion es: {operacion}")
    elif desicion == 4:
        numero1 = int(input("Por favor ingresa un numero >>> "))
        numero2 = int(input("Por favor ingresa el siguiente numero >>"))
        operacion = math.log(numero1,numero2)    
        print(f"las operaciones del logaritmo son las siguientes {operacion} ")
    elif desicion == 5:
        numero1 = int(input("Por favor ingresa un numero >>> "))
        numero2 = int(input("Por favor ingresa el siguiente numero >>"))
        operacion = math.cos(numero1 + numero2)

        print(f"La operacion del cos es {operacion}")

    elif desicion == 6:
        numero1 = int(input("Por favor ingresa un numero >>> "))
        numero2 = int(input("Por favor ingresa el siguiente numero >>"))
        operacion = math.sin(numero1 + numero2) 
        print(f"la operacion del sin  es {operacion}")


    elif desicion == 7:
        numero1 = int(input("Por favor ingresa un numero >>> "))
        numero2 = int(input("Por favor ingresa el siguiente numero >>"))

        operacion = math.sqrt(numero1 + numero2)
        print(f"La operacion es la siguiente {operacion}")
    elif desicion == 8:
        
        print("has elegido convertir a binario: ")
        valor = int(input("ingresa el numero que deseas convertir en binario >>> ") )

        M=[]
        cociente = 1


        while cociente != 0:
            

            valor2 = valor %2
            valor = valor //2

            valor1 = str(valor2)
            
            M.append(valor1)
            
            

            cociente = valor
        M.reverse()

        # se imprimes in coorchetes
        lista = "".join(M)
        print(f"Tu numero binario es el siguiente...  {lista}")
            
    elif desicion == 9:
        continue
