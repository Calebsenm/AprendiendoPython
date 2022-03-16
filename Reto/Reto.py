#este es el primer codigo que hice  para ponerme a praacticar todos los retos que no hice de min tic :)    fecha del commit 11: 10   16 /marzo /2022

from os import system
print("hOLA A MI PROYECTO PYTHON")

Usuario = 12345
Contraseña = 54321
catcha1 = 123 + 12
catcha2 = 5*3+(2)/1

catcha3 = catcha2 + catcha1
contador =  1
Ingreso_Usuario = int(input("hola por favor ingresa tu usuario: "))

while contador < 4:
        
    if Ingreso_Usuario == Usuario:

        Ingreso_contraseña = int(input("ingresa tu contraseña: "))

        if Ingreso_contraseña == Contraseña:

            while True:

                print("resuleva el siguiente catcha")

                valor_catcha = int(input(f"resuleve la siguiente operacion: {catcha1} + {catcha2}: "))
                
                if valor_catcha == catcha3:
                    print("inicio de secion con exito")


                else:
                    print("Error catcha es incorrecto")
                    contador + 1
                    contadorDos = 1

                    if contador ==3:
                        print("ha lacanzado la maxima cantidad de intentos")
                        break
                    else:
                        print("intentelo mueva mente")
                        contador = contador+1
        else:
            System("cls")
            print("contraseña es incorrecta")
            print(f"le quedan {contador} intentos")
            contador = contador+1

    else:
        System("cls")
        print("error el usuario  es incorrecto")
        print(f"le quedan {contador} intentos")
        contador= contador +1


