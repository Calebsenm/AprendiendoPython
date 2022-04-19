"""
2. Consulta palabras pertenecientes a cinco categorías:
países, frutas, géneros musicales, animales y películas.
Escribe la lista en un archivo de texto y ten presente
las orientaciones para la creación del juego.

Para tener en cuenta:


Representa las palabras en una matriz de tipo cadena
de tamaño 5 x 5.

El usuario debe seleccionar una categoría y luego el programa,
aleatoriamente, calcula una palabra de las opciones de la
categoría seleccionada.

Seguidamente se muestra al usuario por medio de underlines
"_" la cantidad de letras que tiene la palabra oculta que debe adivinar.
El usuario ira digitando una letra a la vez para tratar 
de adivinar las letras de la palabra.
Se debe hacer un control de intentos. Cada partida tendrá un mínimo 
de intentos y este control se hará por medio de la representación de 
un personaje ahorcado.

Se hará usando la técnica vista en la sesión 
presencial, ASCII art.Si el usuario adivina la palabra se muestra un 
mensaje de felicitación y se da la posibilidad de volver a escoger 
otra categoría para continuar jugando.


Si el usuario acumula el total de opciones fallidas, pierde 
y queda ahorcado en la imagen de seguimiento. Se muestra un mensaje 
de partida perdida y se lleva al usuario a seleccionar otra categoría 
para seguir jugando.


18/04/2022             / 4: 42 pm 
 
terminado el 
19 /04/2022     a las 1:08    aproximadamente 10 horas de investigacion y desarrolloo


me gustó mucho el resultado es mi primer juego siiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
"""
from operator import index
from os import system
import random

def funcionDelmuñeco():
    ####  aqui se imprimirá el muñequito
    if cantidad_intentos == 1:
        print("""





                              /___\\
                
        """)
    elif cantidad_intentos ==2:
        print("""





                               / \\
                              /___\\
                """)
    elif cantidad_intentos ==3:
        print("""




                                |
                                |
                               / \\
                              /___\\
                """)
    elif cantidad_intentos ==4:
        print("""


                                |
                                |
                                |
                                |
                               / \\
                              /___\\
                """)
    elif cantidad_intentos ==4:
        print("""


                                |
                                |
                                |
                                |
                               / \\
                              /___\\
        """)
    elif cantidad_intentos ==5:
        print("""
                    
                                |
                                |                            
                                |
                                |
                                |
                                |
                               / \\
                              /___\\
        """)
    elif cantidad_intentos ==6:
        print("""
                    _____________
                                |
                                |                            
                                |
                                |
                                |
                                |
                               / \\
                              /___\\
        """)

    elif cantidad_intentos ==7:
        print("""
                       _________
                      |         |
                      |         |                            
                                |
                                |
                                |
                                |
                               / \\
                              /___\\
        """)

    elif cantidad_intentos ==8:
        print("""
                       _________
                      |         |
                      |         |                            
                    \\0/        |
                                |
                                |
                                |
                               / \\
                              /___\\
        """)
    elif cantidad_intentos ==9:
        print("""
                       _________
                      |         |
                      |         |                            
                     \O/        | 
                      |         |
                                |
                                |
                                |
                               / \\
                              /___\\
        """)
    elif cantidad_intentos ==10:
        print("""
                       _________
                      |         |
                      |         |                            
                     \O/        | 
                      |         |
                     / \        |
                                |
                                |
                               / \\
                              /___\\
        """)

            ####

monigote = """
  *----*      
  |    |
 \O/   | 
  |    | 
 / \   |
       |
      / \\
     /___\\
"""
system("cls")

M = [["colombia","brazil","ecuador","peru","venezuela"],
     ["tamarindo","aguacate","mandarina","banano","nispero"],
     ["vallenato","opera","Rock","bachata","salsa"],
     ["loro","ornitorrinco","hormiga","caballo","saltamontes"],
     ["tomate","zanahoria","Berenjena","cebolla","pimentón"]
    ]

print("Bienvenido al juego del Ahorcado")

print("Las categorias por elegir son las siguientes")

print("0. Salir ")
print("1. Países")
print("2. Frutas")
print("3. Generos Musicales")
print("4. Animales")
print("5. Verduras")

print(monigote)

print()
while True:

    Opcion = input("Decide que categoria deseas elegir > ")
    if Opcion == "0":
        system("cls")
        break

    if Opcion == "1":

        ###########################################################
        cantidad_intentos = 0
        system("cls")
        

        #logica del juego! :D
        Palabra_Aleatoria = random.choice(M[0])
        Lista = len( Palabra_Aleatoria)
        indice = M[0].index(Palabra_Aleatoria)

        Lista_de_la_palabra = []
        #imprime las barras de abajo
        for i in range(Lista):
            Lista_de_la_palabra.append("_")

        while True:
            system("cls")
            #imprime el monigote
            print("Has elegido la categoria Países")
            
            funcionDelmuñeco()
            if cantidad_intentos == 10:
                print("el juego ha terminado")
                break

            
            #imprime el arrglo
            for i in range(Lista):
                print(Lista_de_la_palabra[i],end = ' ')
            print("")
            

            Letra = input("Ingresa una letra > ")

            #Este convierte la palabra optenida a una lista
            
            NuevoArreglo_Palabra = list(Palabra_Aleatoria)
            
            #condiciona si la letra exite dentro del arreglo
            if Letra in M[0][indice]:
                print("Palabra corecta")

                #esta buscará la palabra y la colocará en la posicion
                def Indices(lst,item):
                    return [i for i,x in enumerate(lst) if x ==item]
                Indices_Palabras_mencionadas = Indices(NuevoArreglo_Palabra,Letra)

                Cuenta_Areglo = len(Indices_Palabras_mencionadas)

                #coloca las palabras en el arreglo
                for i in range(Cuenta_Areglo):

                    b = Indices_Palabras_mencionadas[i]
                    
                    Lista_de_la_palabra[b] = NuevoArreglo_Palabra[b]

                    print()
                #Verificará si ganó el juego
                if "_" in Lista_de_la_palabra:
                    continue
                else:
                    system("cls")
                    print("¡ Felicidades ha gado el juego ! ")
                    break

            else:
                print("la palabra no existe ")
                cantidad_intentos = cantidad_intentos + 1
        ##################################################################


    elif Opcion == "2":
        
        ####################################
        ###########################################################
        cantidad_intentos = 0
        system("cls")
        

        #logica del juego! :D
        Palabra_Aleatoria = random.choice(M[1])
        Lista = len( Palabra_Aleatoria)
        indice = M[1].index(Palabra_Aleatoria)

        Lista_de_la_palabra = []
        #imprime las barras de abajo
        for i in range(Lista):
            Lista_de_la_palabra.append("_")

        while True:
            system("cls")
            print("has elegido la categoria Frutas")
            #imprime el monigote
            funcionDelmuñeco()
            if cantidad_intentos == 10:
                print("el juego ha terminado")
                break


            #imprime el arrglo
            for i in range(Lista):
                print(Lista_de_la_palabra[i],end = ' ')
            print("")
            

            Letra = input("Ingresa una letra > ")

            #Este convierte la palabra optenida a una lista
            
            NuevoArreglo_Palabra = list(Palabra_Aleatoria)
            
            #condiciona si la letra exite dentro del arreglo
            if Letra in M[1][indice]:
                print("Palabra corecta")

                #esta buscará la palabra y la colocará en la posicion
                def Indices(lst,item):
                    return [i for i,x in enumerate(lst) if x ==item]
                Indices_Palabras_mencionadas = Indices(NuevoArreglo_Palabra,Letra)

                Cuenta_Areglo = len(Indices_Palabras_mencionadas)

                #coloca las palabras en el arreglo
                for i in range(Cuenta_Areglo):

                    b = Indices_Palabras_mencionadas[i]
                    
                    Lista_de_la_palabra[b] = NuevoArreglo_Palabra[b]

                    print()
                #Verificará si ganó el juego
                if "_" in Lista_de_la_palabra:
                    continue
                else:
                    system("cls")
                    print("¡ Felicidades ha gado el juego ! ")
                    break

            else:
                print("la palabra no existe ")
                cantidad_intentos = cantidad_intentos + 1
        ####################################

    elif Opcion == "3":
        system("cls")
        print("has elegido la categoria Musica")

         ###########################################################
        cantidad_intentos = 0
        system("cls")
        

        #logica del juego! :D
        Palabra_Aleatoria = random.choice(M[2])
        Lista = len( Palabra_Aleatoria)
        indice = M[2].index(Palabra_Aleatoria)

        Lista_de_la_palabra = []
        #imprime las barras de abajo
        for i in range(Lista):
            Lista_de_la_palabra.append("_")

        while True:
            system("cls")
            print("has elegido la Musica")
            #imprime el monigote
            funcionDelmuñeco()
            if cantidad_intentos == 10:
                print("el juego ha terminado")
                break


            #imprime el arrglo
            for i in range(Lista):
                print(Lista_de_la_palabra[i],end = ' ')
            print("")
            

            Letra = input("Ingresa una letra > ")

            #Este convierte la palabra optenida a una lista
            
            NuevoArreglo_Palabra = list(Palabra_Aleatoria)
            
            #condiciona si la letra exite dentro del arreglo
            if Letra in M[2][indice]:
                print("Palabra corecta")

                #esta buscará la palabra y la colocará en la posicion
                def Indices(lst,item):
                    return [i for i,x in enumerate(lst) if x ==item]
                Indices_Palabras_mencionadas = Indices(NuevoArreglo_Palabra,Letra)

                Cuenta_Areglo = len(Indices_Palabras_mencionadas)

                #coloca las palabras en el arreglo
                for i in range(Cuenta_Areglo):

                    b = Indices_Palabras_mencionadas[i]
                    
                    Lista_de_la_palabra[b] = NuevoArreglo_Palabra[b]

                    print()
                #Verificará si ganó el juego
                if "_" in Lista_de_la_palabra:
                    continue
                else:
                    system("cls")
                    print("¡ Felicidades ha gado el juego ! ")
                    break

            else:
                print("la palabra no existe ")
                cantidad_intentos = cantidad_intentos + 1
        ####################################

    elif Opcion == "4":
        system("cls")
        print("has elegido la categoria Animales")

        ###########################################################
        cantidad_intentos = 0
        system("cls")
        

        #logica del juego! :D
        Palabra_Aleatoria = random.choice(M[3])
        Lista = len( Palabra_Aleatoria)
        indice = M[3].index(Palabra_Aleatoria)

        Lista_de_la_palabra = []
        #imprime las barras de abajo
        for i in range(Lista):
            Lista_de_la_palabra.append("_")

        while True:
            system("cls")
            print("Animales")
            #imprime el monigote
            funcionDelmuñeco()
            if cantidad_intentos == 10:
                print("el juego ha terminado")
                break


            #imprime el arrglo
            for i in range(Lista):
                print(Lista_de_la_palabra[i],end = ' ')
            print("")
            

            Letra = input("Ingresa una letra > ")

            #Este convierte la palabra optenida a una lista
            
            NuevoArreglo_Palabra = list(Palabra_Aleatoria)
            
            #condiciona si la letra exite dentro del arreglo
            if Letra in M[3][indice]:
                print("Palabra corecta")

                #esta buscará la palabra y la colocará en la posicion
                def Indices(lst,item):
                    return [i for i,x in enumerate(lst) if x ==item]
                Indices_Palabras_mencionadas = Indices(NuevoArreglo_Palabra,Letra)

                Cuenta_Areglo = len(Indices_Palabras_mencionadas)

                #coloca las palabras en el arreglo
                for i in range(Cuenta_Areglo):

                    b = Indices_Palabras_mencionadas[i]
                    
                    Lista_de_la_palabra[b] = NuevoArreglo_Palabra[b]

                    print()
                #Verificará si ganó el juego
                if "_" in Lista_de_la_palabra:
                    continue
                else:
                    system("cls")
                    print("¡ Felicidades ha gado el juego ! ")
                    break

            else:
                print("la palabra no existe ")
                cantidad_intentos = cantidad_intentos + 1
        ####################################

    elif Opcion == "5":
        system("cls")
        print("has elegido la operacion Verduras")

         ###########################################################
        cantidad_intentos = 0
        system("cls")
        

        #logica del juego! :D
        Palabra_Aleatoria = random.choice(M[4])
        Lista = len( Palabra_Aleatoria)
        indice = M[4].index(Palabra_Aleatoria)

        Lista_de_la_palabra = []
        #imprime las barras de abajo
        for i in range(Lista):
            Lista_de_la_palabra.append("_")

        while True:
            system("cls")
            print("has elegido la categoria Frutas")
            #imprime el monigote
            funcionDelmuñeco()
            if cantidad_intentos == 10:
                print("el juego ha terminado")
                break


            #imprime el arrglo
            for i in range(Lista):
                print(Lista_de_la_palabra[i],end = ' ')
            print("")
            

            Letra = input("Ingresa una letra > ")

            #Este convierte la palabra optenida a una lista
            
            NuevoArreglo_Palabra = list(Palabra_Aleatoria)
            
            #condiciona si la letra exite dentro del arreglo
            if Letra in M[4][indice]:
                print("Palabra corecta")

                #esta buscará la palabra y la colocará en la posicion
                def Indices(lst,item):
                    return [i for i,x in enumerate(lst) if x ==item]
                Indices_Palabras_mencionadas = Indices(NuevoArreglo_Palabra,Letra)

                Cuenta_Areglo = len(Indices_Palabras_mencionadas)

                #coloca las palabras en el arreglo
                for i in range(Cuenta_Areglo):

                    b = Indices_Palabras_mencionadas[i]
                    
                    Lista_de_la_palabra[b] = NuevoArreglo_Palabra[b]

                    print()
                #Verificará si ganó el juego
                if "_" in Lista_de_la_palabra:
                    continue
                else:
                    system("cls")
                    print("¡ Felicidades ha gado el juego ! ")
                    break

            else:
                print("la palabra no existe ")
                cantidad_intentos = cantidad_intentos + 1
        ####################################
    else:
        print("No seas Bobo la opcion no existe!")

