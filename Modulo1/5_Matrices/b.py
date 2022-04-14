from os import system
import time
#todad las variablees utlizadas

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
system("cls")


while True:
        
    OP = int(input ("ingrese la opcion 2  : si deseas salir ingresa la opcion 0: "))
    if OP == 0:
        break
    elif OP == 2:
        if recorrido ==1:
            print("las contraseñas han sido gurdadas")
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
                    if uno ==4:
                        break
                    latitud = float(input(f"ingresa la  latitud N {uno}:  "))
                    numero_de_letras = len(str(latitud))
                    
                    if latitud <= latitud_superior and latitud >= latitud_inferior  and numero_de_letras == 6 :
                        
                        print("las coordenadas entan dentro del rango")
                        longitud = float(input(f"Ingresa  la longitud N {uno}:  "))
                        #esta variable actualiza los numeros de la opcion cuando se ingresan las corrdenadas
                        uno = uno + 1
                        
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
                            

                            
                            if Indice_de_lamatris2 == 3:
                                operacion_definida = 1


                            if operacion_definida ==1:

                                while True:
                                    holasi= 0
                                    print(f"La coordenada 1 es la que está mas al {0}")
                                    print(f"La coordenada 2 es la que está mas al {0}")
                                    print(f"La coordenada 3 es la que está mas al {0}")

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
                    else:
                        print("Error las coordenadas son incorrectras")
                except ValueError:
                    print("Error")

        
