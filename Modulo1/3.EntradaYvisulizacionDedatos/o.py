from os import system
a = 0
b = 0

A = ["1","2","3","4","5","6","7"]
B = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]



while True:
    
    # while a <= 6:
    #     print(A[b],B[b])
    #     b = b + 1
    #     a = a + 1
    system("cls")
    for i in range(7):
        print(A[i],B[i])
    DeccicionTomada = int(input("Ingresa una opcion: "))

    
    if DeccicionTomada == 6:
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

                    dato1= ""
                    dato = 0
                    if Eleccion ==1:
                        dato,dato1 = 0,"Cambiar contraseña"
                    if Eleccion ==2:
                        dato,dato1 = 1,"Ingresar coordenadas actuales"
                    if Eleccion ==3:
                        dato,dato1= 2,"Ubicar zona wifi más cercana"
                    if Eleccion ==4:
                        dato,dato1 = 3,"Guardar archivo con ubicación cercana"
                    if Eleccion ==5:
                        dato,dato1 = 4,"Actualizar registros de zonas wifi desde archivo"
                    

                    B[dato]= B[0]
                    B[0]=dato1
                    
            else:
                print("Error")
                print("La adivinansa uno esta equibocada")
                break

           
        else: 
            exit()
