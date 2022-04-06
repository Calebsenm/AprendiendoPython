#este es el primer codigo que hice  para ponerme a praacticar todos los retos que no hice de min tic :)    fecha del commit 11: 10   16 /marzo /2022

from os import system
print("hOLA A MI PROYECTO PYTHON")

Usuario = 12345
Contraseña = 54321
catcha1 = 123 + 12
catcha2 = 5*3/2+ (3*2)-10.5

catcha3 = catcha2 + catcha1
contador =  1
contador2 =  3 

while contador < 4:

    #controla el las esecciones por si alguien escribe una letra
    while True:
        try:
            
            Ingreso_Usuario = int(input("hola por favor ingresa tu usuario: "))
            break
            
        except ValueError:
            print("Debes ingresar un numero el programa colapsa si no")

    if Ingreso_Usuario == Usuario:
        
        while True:
            try:
                Ingreso_contraseña = int(input("ingresa tu contraseña: "))
                break
            
            except ValueError:
                print("Debes ingresar un numero el programa colapsa si no")
        

        if Ingreso_contraseña == Contraseña:

            while True:

                print("resuleva el siguiente catcha")
                while True:
                    try:
            
                        valor_catcha = int(input(f"resuleve la siguiente operacion: {catcha1} + {catcha2}: "))
                        break
            
                    except ValueError:
                        print("Debes ingresar un numero el programa colapsa si no")
                
                if valor_catcha == catcha3:
                    print("inicio de secion con exito")

                    #INICIO DEL RETO DOS DESPUES  LO DEBES DE TERMINAR



                    exit()





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
            system("cls")
            print("contraseña es incorrecta")
            print(f"le quedan {contador2-contador} intentos")
            contador = contador+1

    else:
        
        system("cls")
        print(f"le quedan {contador2-contador} intentos")
        print("error el usuario  es incorrecto")
        contador= contador +1


