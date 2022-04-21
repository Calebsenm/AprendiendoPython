"""
aqui se optimisó el juego del orcado y se mejoró unas opciones

version 2

21/04/2022 / 12:10 am 
"""


from operator import index
from os import system
import random
from time import sleep

def Funcionalidad_Opjeto(Numero,Desicion):
    cantidad_intentos  = 0
        #funcion que imprimirá el munéquito.

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
                     _________
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
        elif cantidad_intentos == 9:
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
  
###########################################################
    
    system("cls")
    
            
    #logica del juego! :D
    Palabra_Aleatoria = random.choice(M[Numero])
    Lista = len( Palabra_Aleatoria)
    indice = M[Numero].index(Palabra_Aleatoria)

    Lista_de_la_palabra = []
    #imprime las barras de abajo
    for i in range(Lista):
        Lista_de_la_palabra.append("_")
    

    #Verifica si gana
  
    holasi = 0
    #logica general del programa
    while True:
        #Verificará si ganó el juego
        if not "_" in Lista_de_la_palabra:
            holasi = holasi + 1
        if holasi == 2:
            system("cls")
            print("¡ Felicidades ha gado el juego ! ")
            sleep(1)
            break
            
        #break de cierre
        if cantidad_intentos == 10:
            system("cls")
            print("oh no! el juego ha terminado")

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
            break



        system("cls")
        #imprime el monigote
        print(Desicion)
                
        funcionDelmuñeco()
        

                
        #imprime el arrglo
        for i in range(Lista):
            print(Lista_de_la_palabra[i],end = ' ')
        print("")
                

        Letra = input("Ingresa una letra > ")

        #Este convierte la palabra optenida a una lista
                
        NuevoArreglo_Palabra = list(Palabra_Aleatoria)
                
        #condiciona si la letra exite dentro del arreglo
        if Letra in M[Numero][indice]:
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
            
           
        else:
            
            print("la palabra no existe ")
            cantidad_intentos = cantidad_intentos + 1
        ##################################################################
        
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


listado = ["0. Salir ","1. Países","2. Frutas,","3. Generos Musicales","4. Animales","5. Verduras"]
print(monigote) 
cantidad_intentos = 0
print()
while True:
    
    for i in range(6):
        print(listado[i])
       
    Opcion = input("Decide que categoria deseas elegir > ")
    if Opcion == "0":
        system("cls")
        break
    if Opcion == "1":        
        Funcionalidad_Opjeto(0,"Has seleccionado la opcion País")
    elif Opcion == "2":
        Funcionalidad_Opjeto(1,"Has seleccionado Frutas")
    elif Opcion == "3":
        Funcionalidad_Opjeto(2,"Has seleccionado Genero de Musica")
    elif Opcion == "4":
        Funcionalidad_Opjeto(3,"Has seleccionad Animales")
    elif Opcion == "5":
        Funcionalidad_Opjeto(4,"Has seleccionado Verduras")
    else:
        print("No seas Bobo la opcion no existe!")

