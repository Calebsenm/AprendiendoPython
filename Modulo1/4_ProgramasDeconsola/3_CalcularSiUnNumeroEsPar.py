"""
Crea un programa que verifique si eun numero es par o es imopar


terminado del 11 abril del 2022 a las 7:53 pm

"""

print("Vienvenido al programa")


while True:
    try:
        print("si deseas terminar el progrma ingresa 0 ")
        Dato = int(input ("Porfavor ingresa un valor un numero: "))
        Dato2 =  Dato % 2

        if Dato == 0:
            break
        if Dato2 == 0:
            print("EL numero ingresado es par")
        
        else:
            print("El numero ingresado es impar")

    except ValueError:
        print("el valor no esta permitido")