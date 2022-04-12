"""
Crea un programa que ingrese un dato y luego lo eleve a una potencia.
el programa debe pedir el numero uno y un numero dos el cual es la potencia

listo el 11 / abril del 2022 a las 10: 18 pm
"""

while True:  
    try:
            
        PrimerNumero = int(input("Ingresa un numero: "))

        if PrimerNumero > 100:
            print("EL dato es muy alto para ingresar")
        if PrimerNumero < 0  or PrimerNumero <101:
            NumeroDos = int(input("Ingresa el numero que sera la potencia: "))
            if NumeroDos >10:
                print("EL valor es superior debe ingresar  un numero menor")
            elif NumeroDos <11:
                resultado = PrimerNumero ** NumeroDos
                print(f"La el resulytado del operacion es: {resultado}")
                break

    except ValueError:
        print("NO seas nood le piden un nuemero")