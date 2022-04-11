
"""
este es el primer codigo que hice
para ponerme a praacticar todos los retos que no hice de min tic :)
fecha del commit       Desconocida
Fecha de De finalizacion del reto N2 : 8:00 pm  / 10/abril/2022

mas de 4 Dias Trababajando en el reto
"""
#objetivos del reto 2                                       Fecha de creacion 7 / 04 / 2022  9:30 pm
"""
Requisitos funcionales:
o RF01: El programa muestra el siguiente menú de opciones en 
consola para el uso del programa: 1. Cambiar contraseña, 2. Ingresar 
coordenadas actuales, 3. Ubicar zona wifi más cercana, 4. Guardar 
archivo con ubicación cercana, 5. Actualizar registros de zonas wifi 
desde archivo, 6. Elegir opción de menú favorita, 7. Cerrar sesión.

 Datos de ingreso: Ninguno, el menú de opciones aparece 
luego de completar el inicio de sesión.

 Datos de salida: Ninguno, se le pide al usuario los datos 
requeridos para ingresar a la opción elegida.

 Criterios de aceptación:
 El menú debe visualizarse completo en consola 
después de iniciar sesión (Reto#1).
 El menú debe mostrarse en una lista ordenada por 
números.
 El sistema debe mostrar el mensaje “Elija una opción” 
al final del menú para recibir las instrucciones del 
usuario.

#######################################################################################################
o RF02: El programa permite elegir una opción del menú como favorito.
 Datos de ingreso: 

 El usuario ingresa al sistema el número 6 del menú de 
opciones.
 El usuario ingresa al sistema un número del 1 al 5 como 
opción favorita.
 Datos de salida: Menú reordenado con la opción favorita de 
primero.


 Criterios de aceptación:
 El usuario solo podrá reordenar las primeras 5 opciones 
del menú; elegir opción favorita y cerrar sesión siempre 
deben aparecer al final.

 El programa deberá mostrar el mensaje “Seleccione 
opción favorita” después de acceder a esta 
funcionalidad.

 El programa deberá mostrar el mensaje “Error” si el 
usuario elige una opción incorrecta (número diferente 
entre 1 y 5) y finalizar la ejecución del programa.

 Si la opción de favorito es válida el programa deberá 
solicitar una doble confirmación al usuario, previo al 
ejecutar el cambio del menú. Esta confirmación deberá 
ser diseñada con dos adivinanzas en pantalla que 
tengan como respuesta las últimas dos cifras del 
código del grupo al que pertenece en “Fundamentos de 
programación”. Ejemplo: 51593


o Primera adivinanza: “Para confirmar por favor 
responda: Si me giras pierdo tres unidades por 
eso debes colocarme siempre de pie, la 
respuesta es”: 9

o Segunda adivinanza: “Para confirmar por favor 
responda: Me separaron de mi hermano siamés, 
antes era un ocho y ahora soy un… la respuesta 
es”: 3

El programa debe verificar la repuesta de la primera 
adivinanza antes de pasar a la segunda; si el usuario 
falla en una, no se podrá efectuar el cambio, mostrará 
el mensaje “Error” y volverá al menú principal
programado por defecto.

 El programa deberá limpiar la consola y mostrar
completo y numerado el nuevo menú elegido. Al final 
debe aparecer el mensaje “Elija una opción”.                                                Completado


################################################################
RF03: El programa genera una alerta si el usuario elige una opción 
incorrecta.
 Datos de ingreso: El usuario ingresa un número que no es 
opción de menú.
 Datos de salida: ninguno, se espera un mensaje de alerta por 
elegir una opción incorrecta o no esperada.
 Criterios de aceptación:
 El programa deberá mostrar el mensaje “Error” si el 
usuario elige una opción incorrecta. 
 El programa luego del mensaje de error debe solicitar al 
usuario que ingrese nuevamente la opción del menú 
que desea utilizar a través del mensaje “Elija una 
opción”.
 Si el usuario se equivoca más de tres veces seguidas, 
dentro del mismo menú, al momento de elegir una
opción, el programa debe finalizar la ejecución de 
manera inmediata y mostrar el mensaje “Error”.
 Recomendación: Disponer de una variable contador o 
acumulador                                                                     listo :D
##################################################################
RF04: El programa permite acceder a las opciones del menú
 Datos de ingreso: El usuario ingresa al sistema un número 
entre 1 y 5.
 Datos de salida: ninguno, se espera un mensaje de 
confirmación ingreso a la opción elegida.
 Criterios de aceptación: 
 Al elegir la opción del menú el programa debe mostrar 
el mensaje “Usted ha elegido la opción número #”
Ejemplo: “Usted ha elegido la opción 3”
 El programa debe finalizar la ejecución luego de 
mostrar el mensaje de ingreso a una de las opciones 
del menú
###################################################                             listo :D

RF05: El programa permite al usuario salir del menú.
 Datos de ingreso: El usuario ingresa al sistema el número 7 del 
menú de opciones.
 Datos de salida: ninguno, se espera un mensaje de 
confirmación de cierre de sesión si decide salir del menú.
 Criterios de aceptación: 
 Al elegir la opción de cerrar sesión el sistema debe salir 
del menú, mostrar el mensaje “Hasta pronto” y finalizar 
la ejecución del programa
"""


#funcion del menu



from operator import index
from os import system, terminal_size
from re import U
print("HOLA A MI PROYECTO PYTHON")

Usuario = 12345
Contraseña = 54321
catcha1 = 123 + 12
catcha2 = 5*3/2+ (3*2)-10.5

catcha3 = catcha2 + catcha1
contador =  1
contador2 =  3 

a = 1
b = 0


A = [1,2,3,4,5,6,7]
B = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
M = [1,2,3,4,5]



Acumulador = 0


# al cambiar algo dpor ejemplo 3 debe pasar a uno y el objeto en 1 debe pasar a 3

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

                while True:
                
                    if valor_catcha == catcha3:
                        print("inicio de secion con exito")

                        #INICIO DEL RETO DOS DESPUES  LO DEBES DE TERMINAR



                        
                        system("cls")
                        for i in range(7):
                            print(A[i],B[i])
                        # DeccicionTomada = int(input("Ingresa una opcion: "))
                        # #las deciciones  se cambian 

                        DeccicionTomada1 = int(input("Ingresa una opcion: "))
                        #las deciciones  se cambian 
                        
                        

                        
                        if DeccicionTomada1 == 1:
                            DeccicionTomada = M[0] 
                            
                           
                        if DeccicionTomada1 == 2:
                            DeccicionTomada = M[1]
                            
                            

                        if DeccicionTomada1 == 3:
                            DeccicionTomada = M[2]
                            

                        if DeccicionTomada1 == 4:
                            DeccicionTomada = M[3]
                            
                            
                            
                        if DeccicionTomada1 == 5:
                            DeccicionTomada = M[4]
                            
                            
                            
                        if DeccicionTomada1 ==6:
                            DeccicionTomada = A[5]
                        if DeccicionTomada1 ==0:
                            DeccicionTomad = 0



                        uno = 0
                        if DeccicionTomada1 == 0 or DeccicionTomada1 == 7:

                            
                            uno = B[6]
                            print(f"Has elegido {uno}")
                            Desicion_De_salida = input("Deseas si deseas salir ingresa si, si no deseas salir igresa no: ")
                            
                            if Desicion_De_salida == "si":
                                print("Hasta pronto")
                                exit()
                                
                            elif Desicion_De_salida == "no":
                                continue
                            else:
                                print("Error")

                        elif DeccicionTomada1 >7 or DeccicionTomada1< 0:
                            print(" Error")
                            Acumulador = Acumulador +1 
                            if Acumulador >3:
                                print("Error")
                                exit()


                        elif DeccicionTomada == 1:
                            
                            print(f"Has elegido la opcion Numero {DeccicionTomada1}")

                            print("Has elegido cabiar contraseña")
                            Cambiode_contraseña = input("Ingresa un numero ")

                            
                            
                        elif DeccicionTomada == 2:
                            
                            print(f"Has elegido la opcion Numero {DeccicionTomada1}")

                            print("Ingresar coordenadas actuales")
                            Cambiode_contraseña = input("Ingresa un numero ")
                            
                        elif DeccicionTomada == 3:
                           
                            print(f"Has elegido la opcion Numero {DeccicionTomada1}")
                            print("Ubicar zona wifi más cercana")
                            Cambiode_contraseña = input("Ingresa un numero ")
                            
                            
                        elif DeccicionTomada == 4:
                            
                            print(f"Has elegido la opcion Numero {DeccicionTomada1}")


                            print("Guardar archivo con ubicación cercana")
                            Cambiode_contraseña = input("Ingresa un numero ")

                        elif DeccicionTomada == 5:
                            
                            print(f"Has elegido la opcion Numero {DeccicionTomada1}")

                            print("Actualizar registros de zonas wifi desde archivo : ")
                            Cambiode_contraseña = input("Ingresa un numero ")


                        # si el usuario ingresa la opcion numero 6
                        elif DeccicionTomada == 6:
                            
                            print(f"Has elegido la opcion Numero 6")
                            

                            #Ejecuta el cambio de la opcion favorita
                            print("Has ingresado a la opcion favorita")
                            Eleccion = int(input("Ingresa una opcion favorita: "))

                            if Eleccion >= 0 and Eleccion <= 5:

                                correcto1 = 9
                                correcto2 = 3

                                print("Para confirmar porfavor responda los dos acertijos")
                                adivinanza1 = int(input("Si me giras pierdo tres unidades por eso debes colocarme siempre de pie: "))
                                adivinanza2 = int(input("Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es: "))

                                
                                if adivinanza1 == correcto1:
                                    if adivinanza2 == correcto2:
                                        print("Las adivinansas son correctas")

                                        
                                        #elimina el dato seleccionado y lo coloca en la posicion numero 1
                                        a = B[Eleccion-1]
                                        B.remove(a)
                                        B.insert(0,a)

                                        M.remove(Eleccion)
                                        M.insert(0,Eleccion)

                                else:
                                    print("Error")
                                    print("La adivinansa uno esta equibocada")
                                    break

                            
                            else: 
                                exit()
    
                        elif DeccicionTomada == 7:
                            print(" has salido con exito")

                        elif DeccicionTomada == 8:
                            break

                    
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

