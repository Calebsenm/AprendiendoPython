"""
Reto numero 4..
 
se inicia el 21 /04/2022 a las 10:04 am 



"""

from operator import index
from os import system, terminal_size
from re import U
import time
from math import asin, cos,sin,sqrt

# la matiris 
Matriz = [
    [-3.777,-70.302,91],
    [-4.134,-69.983,223],
    [-4.006,-70.123,149],
    [-3.846,-70.222,211]
]

def Calcula(latitud,longitud):
    l_distancias=[]
    R=6372.79547798

    for i in range (4):
        delta = Matriz[i][0] -latitud
        dlong = Matriz[i][0] -longitud
        Distancia=2*R*asin(sqrt(sin(delta/2)**2+ (cos(latitud)*cos(Matriz[i][0])*sin(dlong/2)**2)))   
        l_distancias.append(Distancia)

    return l_distancias


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
holasi= ""
holasi2 = ""
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
                                    print("La coordenada 1 es la que está mas al sur")
                                    print("La coordenada 2 es la que está mas al este")                                                    
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
                                            print("las coordenadas estan dentro del rango")
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
                                                        print("La coordenada 1 es la que está mas al sur")
                                                        print("La coordenada 2 es la que está mas al este ")
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
                                                print("Error las corrdenadas estan fuera del rango ") 
                                                uno  = uno - 1  
                                        else:
                                            print("Error las coordenadas son incorrectas")
                                    except ValueError:
                                        print("Error")                                                                                    
                        elif DeccicionTomada == 3:
                            # Aqui se inicia el reto numero 4.......
                            if 0 in P[0]:
                                system("cls")
                                print("Error")
                                time.sleep(1)
                            if not 0 in P[0]:
                                print(f"Coordenada [latitud][longitud] 1 : {P[0]}")
                                print(f"Coordenada [latitud][longitud] 2 : {P[1]}")
                                print(f"Coordenada [latitud][longitud] 3 : {P[2]}")
                                deciccion = int(input("Porfavor ingrese una opcion para calcular la distancia entre los puntos de conexción 1, 2, o 3,"))
                                if deciccion == 1 or deciccion ==2 or deciccion ==3:
                                    latitud = P[deciccion -1][0]
                                    longitud = P[deciccion -1][1]
                                    lista_distancias = Calcula(latitud , longitud)
                                    distancia_ordenada = lista_distancias[:]
                                    distancia_ordenada.sort()
                                    posicion1  = lista_distancias.index(distancia_ordenada[0])
                                    posicion2  = lista_distancias.index(distancia_ordenada[1])
                                    if Matriz[posicion1][2] > Matriz[posicion2][2]:
                                        posicion1,posicion2=posicion2,posicion1
                                    print("Zona wifi con menos usuarios")
                                    print(f"la zona wifi 1: ubicada en [{Matriz[posicion1][0]},{Matriz[posicion1][1]}] a {round(lista_distancias[posicion1])} metros, tiene en promedio {Matriz[posicion1][2]} usuarios")
                                    print(f"la zona wifi 2: ubicada en [{Matriz[posicion2][0]},{Matriz[posicion1][1]}] a {round(lista_distancias[posicion2])} metros, tiene en promedio {Matriz[posicion2][2]} usuarios")
                                    opcx=int(input("elija 1 o 2 para recibir indicaciones de llegada"))
                                    if opcx==1 or opcx==2:
                                        if opcx==1:
                                            posx=posicion1
                                        elif opcx==2:
                                            posx=posicion2
                                        if latitud < Matriz[posx][0]:
                                            direccion1="norte"
                                        else:
                                            direccion1="sur"
                                        if longitud<Matriz[posx][1]:
                                            direccion2="oriente"
                                        else:
                                            direccion2="occidente"
                                        tiempo_moto=round(lista_distancias[posx]/19.44,1)
                                        tiempo_apie=round(lista_distancias[posx]/0.483,1)
                                        print(f"Para llegar a la zona wifi dirijase al {direccion2} y luego hacia el {direccion1}")
                                        print(f"-Tiempo en moto: {tiempo_moto} ")
                                        print(f"-Tiempo a pie {tiempo_apie}")
                                        salir=input("presione 0 para salir: ")
                                    else:
                                        print("Error zona wifi")
                                        exit()
                                else:
                                    print("error")                                                                                
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