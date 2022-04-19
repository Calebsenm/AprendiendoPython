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


18/04/2022    

"""
from os import system
import random


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

M = [["colombia","brazil","ecuador","Peru","venezuela"],
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
        system("cls")
        print("Has elegido la categoria Países")

        #logica del juego! :D
        Palabra_Aleatoria = random.choice(M[0])
        Lista = len( Palabra_Aleatoria)
        indice =M[0].index(Palabra_Aleatoria)
        
        Lista_de_la_palabra = []

        #imprime las barras de abajo
        for i in range(Lista):
            Lista_de_la_palabra.append(["_"])
        

        while True:
            
            for i in range(Lista):
                for j in range(1):
                    print(Lista_de_la_palabra[i][j],end = ' ')
            
            print()
            Palabra = input("Ingresa una letra > ")

            #Este convierte la palabra optenida a una lista
            NuevoArreglo = Palabra.split()
            

            if Palabra in M[0][indice]:
                print("Palabra corecta")


            else:
                print("la palabra no existe ")


    elif Opcion == "2":
        system("cls")
        print("has elegido la categoria Frutas")

    elif Opcion == "3":
        system("cls")
        print("has elegido la categoria Musica")

    elif Opcion == "4":
        system("cls")
        print("has elegido la categoria Animales")

    elif Opcion == "5":
        system("cls")
        print("has elegido la operacion Verduras")
    else:
        print("No seas Bobo la opcion no existe!")

