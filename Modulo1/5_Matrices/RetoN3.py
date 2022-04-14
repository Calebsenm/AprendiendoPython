"""

inicio  13/04/2022  a las 9:50 pm


requisitos funcionales del reto 3

RF01:  Terminado :D
 El usuario primero debe elegir la opción #1 (cambiar 
contraseña) para poder acceder a esta configuración.
 La nueva contraseña no puede ser igual a la contraseña 
actual.
 Antes de asignar la nueva contraseña el sistema debe
solicitar y confirmar la contraseña actual.
 El sistema debe mostrar el mensaje “Error” y finalizar la 
ejecución del programa si la contraseña ingresada no 
coincide con la actual en el proceso de validación.
 Si el usuario confirma correctamente la contraseña 
actual se solicita y guarda la nueva contraseña; luego, 
el sistema debe regresar al menú principal. 

"########################################################################################
RF02: El programa permite al usuario ingresar las coordenadas de los 
tres sitios que más frecuenta (trabajo, casa, parque).
 Datos de ingreso: Latitud, longitud; Coordenadas en grados 
decimales, solamente con 3 cifras decimales.
 Datos de salida: Ninguno, se espera que los datos ingresados 
queden almacenados en una matriz de 3 filas y 2 columnas. 
 
1 Un ejemplo de coordenada en grados decimales es 6.242, -75.589, que corresponde con la sede UPB 
Medellín. En este reto debes tener presente manejar tres cifras decimales para la precisión de los puntos.
Criterios de aceptación:
 El usuario primero debe elegir la opción #2 (ingresar 
coordenadas actuales) para poder acceder a esta 
configuración.
 El usuario debe ingresar al sistema dos números de 
coordenadas, latitud y longitud. Las coordenadas deben 
ser ingresadas al sistema de manera independiente y 
deben ser validadas.
 El usuario utilizará un punto para separar las cifras 
decimales de la coordenada que ingrese. No es 
necesario que el programa valide este carácter.
 El usuario ingresará 3 cifras decimales por cada 
coordenada ingresada. No es necesario que el 
programa valide esta cantidad de cifras.
 El usuario ingresará 3 parejas de coordenadas y el 
sistema deberá almacenarlas en una matriz de 3 filas y 
2 columnas.
 La validación de las coordenadas ingresadas se hará a 
partir de la siguiente tabla. Según el penúltimo digito
del código de su grupo, en “Fundamentos de 
programación”, revise las restricciones entre las cuales 
está permitido ingresar coordenadas en el sistema

Municipio   :  Leticia, Amazonas
Latitud     :  Sup: -3.002  Inf:-4.227
longitud    :  Or:-69.714   Occ:-70.365


 Si el usuario ingresa un valor por fuera de estos rangos 
el sistema debe mostrar el mensaje de “Error
coordenada” y finalizar la ejecución.
 Si el usuario ingresa correctamente los datos el 
sistema debe regresar al menú principal.
 Si el usuario ingresa por primera vez a esta opción debe 
diligenciar las tres coordenadas, si deja una 
coordenada vacía el sistema debe mostrar el mensaje 
“Error” y finalizar la ejecución
##############################################
Terminado :D yes yes yes 
##########################################################################################################
RF03: El programa permite al usuario actualizar las coordenadas de 
los tres sitios más frecuentados.
 Datos de ingreso: Número de coordenada que desea 
actualizar y valores de la nueva coordenada.
 Datos de salida: Ninguno, se espera un mensaje de 
confirmación.
 Criterios de aceptación:
 El usuario debe elegir la opción #2 (ingresar 
coordenadas actuales) para poder acceder a esta 
configuración.
 Solo se podrán actualizar las coordenadas si el usuario 
ha ingresado las coordenadas previamente, de lo 
contrario el usuario debe llenar las coordenadas según 
lo estipulado en el RF02.
 Antes de actualizar las coordenadas el usuario debe ver 
en pantalla las coordenadas que actualmente tiene 
almacenadas en el sistema.
 Antes de actualizar las coordenadas el usuario debe ver 
en pantalla dos mensajes referentes a información 
clave sobre sus coordenadas. Estos mensajes deberán 
mostrarse según el último digito del código de su grupo
en “Fundamentos de programación”

digito  = 0
-coordenada ubicada mas al norte
Coordenada ubicada más al sur

 El programa deberá mostrar el mensaje “Presione 1,2 ó
3 para actualizar la respectiva coordenada. Presione 0 
para regresar al menú”; si el usuario elige una opción 
incorrecta debe aparecer el mensaje “Error
actualización” y finalizar la ejecución.
 Un ejemplo de los tres criterios anteriores es el 
siguiente:

coordenada [latitud ,longitud ] 1 : [10.426, -72.897]
coordenada [latitud ,longitud ] 2 : [-4.227, -6.714]
coordenada [latitud ,longitud ] 3 : [6.284, -76.049]


la cordenada 1 es la que esta mas al norte
la coordenada 2 es la que esta mas al sur

presiones 1,2 0 tres para actualizar la respectiva coordenada o presione 0 para regresar al menu

Al momento de actualizar alguna de las coordenadas 
deben validarse los datos ingresados según lo 
estipulado por el RF02. Si el valor ingresado cumple con 
las restricciones, el programa debe regresar al menú 
principal; por el contrario, si el usuario escribe un valor 
de coordenada que no cumple las restricciones debe 
aparecer el mensaje “Error coordenada” y finalizar la 
ejecución del programa.


################################3

 Pruebas y validaciones:
o El sistema debe mostrar un menú ordenado numéricamente para la 
navegación por las diferentes opciones.
o El sistema debe permitir ingresar a las opciones 1 y 2.
o El sistema debe permitir al usuario ingresar las coordenadas de los 
tres lugares más frecuentados.
o El sistema debe permitir al usuario actualizar las coordenadas de los 
tres lugares más frecuentados.
o El sistema debe mostrar al usuario información clave sobre las 
coordenadas actuales.
 Recomendaciones:
o El archivo entregado en plataforma debe cumplir con los requisitos 
funcionales de los retos 1, 2 y 3.
o Para definir las coordenadas ubicadas en los extremos norte, sur, 
oriente y occidente puede apoyarse en la siguiente imagen:

magen recuperada de: 
https://bit.ly/2SfylAb

Para calcular el promedio de las coordenadas puede apoyarse en las
siguientes fórmulas:

promedio latitud = (latitud1 +latitud 2 + latituc 3)/3
promedio longitud = (longitud1  +longitud2 + longitud3 )/3

"""
from operator import index
from os import system, terminal_size
from re import U
import time

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


#Matris dela opcion 3

P = [ 

    [0,0],
    [0,0],
    [0,0]
]

latitud_superior = -3.002 
latitud_inferior = -4.227

longitud_superior = -69.714 
longitud_inferior = -70.365
Indice_de_lamatris1 = 0
Indice_de_lamatris2 = 0
uno = 1
operacion_definida = 0

decicion_de_cierre  = 1

recorrido = 0

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

                        #aqui inicia el reto numero 3  :D
                        
                        elif DeccicionTomada == 1:
                            print(f"Has elegido la opcion Numero {DeccicionTomada1}")
                            print("Has elegido cabiar contraseña")
                            

                            VerificarContraseña = int(input ("Ingresa tu contraseña: "))
                            if VerificarContraseña == Contraseña:
                            
                                while True:
                                    NuevaContraseña = int(input("Ingresa tu nueva contraseña: "))
                                    NuevaContraseña1 = int(input("Porfavor confirma la contraseña: "))
                                    if NuevaContraseña == NuevaContraseña1:
                                        print("la contraseña es correcta")
                                        print("la contraseñas se han guardado correctamente")

                                        Contraseña = NuevaContraseña1
                                        time.sleep(1)
                                        break 
                                    else:
                                        print("Las contraseñas no coinciden intentelo nueva mente")
                            else:
                                print("Error")   
                            
                        elif DeccicionTomada == 2:
                            
                            print(f"Has elegido la opcion Numero {DeccicionTomada1}")
                            print("Ingresar coordenadas actuales")
                                
                            if recorrido ==1:
                                print("Estas son las coordenadas! ")

                                print(f"Coordenada [latitud][longitud] 1 : {P[0]}")
                                print(f"Coordenada [latitud][longitud] 2 : {P[1]}")
                                print(f"Coordenada [latitud][longitud] 3 : {P[2]}")

                                while True:
                                    holasi= 0
                                    print(f"La coordenada 1 es la que está mas al {holasi}")
                                    print(f"La coordenada 2 es la que está mas al {holasi2}")
                                                        

                                    decicion_de_cierre = int(input("Presiona 0 para regresar al menú 0 Presione 1,2 o 3 para actuallizar la respectiva coordenada "))
                                                        
                                    if decicion_de_cierre == 0:
                                        break
                                    elif decicion_de_cierre == 1:
                                        CambioDeMatrix()
                                                            
                                    elif decicion_de_cierre == 2:
                                        CambioDeMatrix()
                                                            
                                    elif decicion_de_cierre == 3:
                                        CambioDeMatrix()
                                                            
                                    else:
                                        print("la decicion no esta permitida")



                            elif recorrido ==0:
                                recorrido = 1
                                #funcion que permite hacer el cambio de la sellecionada
                                def CambioDeMatrix ():
                                    
                                    while True:
                                        try:
                                            
                                            latitud = float(input(f"ingresa la  latitud N {decicion_de_cierre}:  "))
                                            numero_de_letras = len(str(latitud))
                                            
                                            if latitud <= latitud_superior and latitud >= latitud_inferior  and numero_de_letras == 6 :
                                                
                                                print("las coordenadas entan dentro del rango")
                                                longitud = float(input(f"Ingresa  la longitud N {decicion_de_cierre}:  "))
                                                
                                                numero_de_letras2 = len(str(longitud))

                                                if longitud <= longitud_superior and longitud >= longitud_inferior and numero_de_letras2 == 7:
                                                    
                                                    print("Cordenadas dentro del rango")
                                                    P [decicion_de_cierre-1][0] = latitud
                                                    P [decicion_de_cierre-1][1] = longitud

                                                    
                                                    print(f"Coordenada [latitud][longitud] 1 : {P[0]}")
                                                    print(f"Coordenada [latitud][longitud] 2 : {P[1]}")
                                                    print(f"Coordenada [latitud][longitud] 3 : {P[2]}")
                                                    break

                                                else:
                                                    system("cls")
                                                    print("Error las corrdenadas entan fuera del rango ") 
                                                    
                                            else:
                                                print("Error las coordenadas son incorrectras")
                                        except ValueError:
                                            print("Error")

                                # pide las distintas coordenadas y las verfica y luego las ingresa a  la matris
                                while True:
                                    try:
                                        
                                        #este contrla la laopcion y rompe cuando y ase an ingresado las matrices
                                        if uno ==3:
                                            break
                                        
                                        latitud = float(input(f"ingresa la  latitud N {uno +1 }:  "))
                                        
                                        numero_de_letras = len(str(latitud))
                                        
                                        if latitud <= latitud_superior and latitud >= latitud_inferior  and numero_de_letras == 6 :
                                            
                                            print("las coordenadas entan dentro del rango")
                                            longitud = float(input(f"Ingresa  la longitud N {uno +1}:  "))
                                            #esta variable actualiza los numeros de la opcion cuando se ingresan las corrdenadas
                                            
                                            numero_de_letras2 = len(str(longitud))

                                            if longitud <= longitud_superior and longitud >= longitud_inferior and numero_de_letras2 == 7:
                                                
                                                print("Cordenadas dentro del rango")

                                                P[Indice_de_lamatris2][Indice_de_lamatris1] =latitud
                                                Indice_de_lamatris1 = Indice_de_lamatris1  +1
                                                P[Indice_de_lamatris2][Indice_de_lamatris1] = longitud
                                                Indice_de_lamatris2 = Indice_de_lamatris2 +1
                                                Indice_de_lamatris1  = 0


                                                print(f"Coordenada [latitud][longitud] 1 : {P[0]}")
                                                print(f"Coordenada [latitud][longitud] 2 : {P[1]}")
                                                print(f"Coordenada [latitud][longitud] 3 : {P[2]}")
                                                uno = uno + 1

                                                
                                                if Indice_de_lamatris2 == 3:
                                                    operacion_definida = 1


                                                if operacion_definida ==1:

                                                    while True:
                                                        holasi= ""
                                                        holasi2 = ""
                                                        a1 = P[0][0]
                                                        b1 = P[0][1]

                                                        a2 = P[1][0]
                                                        b2 = P[1][1]

                                                        a3 = P[2][0]
                                                        b3 = P[2][0]

                                                        Promedio_latitud = (a1+a2+b3) /3
                                                        Promedio_longitud = (b1+b2+b3)/3

                                                        if Promedio_latitud < 0:
                                                            holasi = "Sur"
                                                        elif Promedio_longitud <0:
                                                            holasi = "Oeste"
                                                        elif Promedio_latitud >0:
                                                            holasi2 = "Norte"
                                                        elif Promedio_longitud >0:
                                                            holasi2 = "Este"
                                                        

                                                        print(f"La coordenada 1 es la que está mas al {holasi}")
                                                        print(f"La coordenada 2 es la que está mas al {holasi2}")
                                                       

                                                        decicion_de_cierre = int(input("Presiona 0 para regresar al menú 0 Presione 1,2 o 3 para actuallizar la respectiva coordenada "))
                                                        
                                                        if decicion_de_cierre == 0:
                                                            break
                                                        elif decicion_de_cierre == 1:
                                                            CambioDeMatrix()
                                                            
                                                        elif decicion_de_cierre == 2:
                                                            CambioDeMatrix()
                                                            
                                                        elif decicion_de_cierre == 3:
                                                            CambioDeMatrix()
                                                            
                                                        else:
                                                            print("la decicion no esta permitida")
                                                
                                            else:
                                                system("cls")
                                                print("Error las corrdenadas entan fuera del rango ") 
                                                uno  = uno - 1  
                                        else:
                                            print("Error las coordenadas son incorrectras")
                                    except ValueError:
                                        print("Error")
                        

                               
                                
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