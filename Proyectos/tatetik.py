""" 
Se va a crear el juego del tatetick
creador caleb seña 

dia en que se Terminó es 4:51 pm  el dia 27 / 04/2022
"""

from os import system
system("cls")

#el cuadró será imprimido...
def cuadro():
      system("cls")
      print("Debes recordar que las filas van en diagonal     ---")
      print("Debes recordar que las columnas van en vertical   | ")
      print(" ____________________")
      print("|      |      |      | ")
      print(f"|  {M[0][0]}   |   {M[0][1]}  |   {M[0][2]}  | ")
      print("|______|______|______| ")
      print("|      |      |      | ")
      print(f"|  {M[1][0]}   |  {M[1][1]}   |   {M[1][2]}  | ")
      print("|______|______|______|")
      print("|      |      |      | ")
      print(f"|  {M[2][0]}   |  {M[2][1]}   |   {M[2][2]}  | ")
      print("|______|______|______| ")

#la logica del juego

def Logica(operador,jugador):
      print(f"{jugador} Te corresponde La Palabra {operador}") 
      while True:
            try:
                  numero1 = int(input("ingresa el numero de la fila donde vas a colocar la marca >> "))
                  numero2 = int(input ("ingresa el numero de la comuna donde vas a colocar la marca >> "))
                  if numero1 < 4 and numero1 > 0 and numero2 < 4 and numero2 > 0:
                        if " " in M[numero1-1][numero2-1]:
                              M[numero1-1][numero2-1] = operador                                                               
                              break
                        
                  else:
                        print("""

                        Uno de los numeros está fura de
                        rango deve revisar que los numeros 
                        estén dentro del rango 1 a 3 fuera
                        de rango los valores no están
                        permitidos

                        """)
                  
            except ValueError:
                  print("no debes colocar un objeto que sea diferente a los numeros especificados")
      

#variables involucadras
M = [
      [" "," "," "],
      [" "," "," "],
      [" "," "," "],
]

Nombres = {
        "jugador1" : "",
        "Jugador2" : "",

}  

#inicio del juego 
print("**********************")
print("* Welcome to MY game*")
print("**********************")

#nombres

while True:

      NombreJugador1 = input("ingresa el nombre del jugador 1 >> ")
      NombreJugador2 = input("ingresa el nombre del jugador 2 >> ")
      if NombreJugador1 == NombreJugador2:
            print("EL nombre ya está repertido")
            NombreJugador2 = input("ingresa el nombre del jugador 2 >> ")
            break
      else:
           break


cuadro()
print(f"{NombreJugador1} Tendrá la letra X")
print(f"{NombreJugador2} Tendrá la letra O")

#verifica y actualiza el juego...
bueltaa = 0
while True:
      system("cls")
      cuadro()


      #se verifica si un gugador ganana
      #fila 1 
      # EL va buascar la filas y columnas que se repiten si encuentra 3 filas o trs comlunas el va a colapsar y termina el juego
      if M[1-1][1-1] == M [1-1][2-1] and   M [1-1][2-1] == M[1-1][3-1]:
            if not M[0][0] == " ":
                  if "X" in M[0][1]:
                        print(f"Gano el jugador {NombreJugador1}  X")
                        exit()
                  elif "O" in M[0][1]:
                        print(f"Gano el jugador {NombreJugador2}  O")
                                          
                        exit()
      # columna 1
      elif M[0][0] == M [1][0] and   M [1][0] == M[2][0]:
            if not M[0][0] == " ":
                  if "X" in M[0][1]:
                        print(f"Gano el jugador {NombreJugador1}  X")
                        exit()
                  elif "O" in M[0][1]:
                        print(f"Gano el jugador {NombreJugador2}  O")
                                          
                        exit()
      # fila 2
      elif M[1][0] == M [1][1] and   M [1][1] == M[1][2]:
            if not M[0][0] == " ":
                  if "X" in M[1][1]:
                        print(f"Gano el jugador {NombreJugador1}  X")
                        exit()
                  elif "O" in M[1][1]:
                        print(f"Gano el jugador {NombreJugador2}  O")
                                          
                        exit()
      # columna 2
      elif M[0][1] == M [1][1] and   M [1][1] == M[1][2]:
            if not M[0][0] == " ":
                  if "X" in M[1][1]:
                        print(f"Gano el jugador {NombreJugador1}  X")
                        exit()
                  elif "O" in M[1][1]:
                        print(f"Gano el jugador {NombreJugador2}  O")
                                          
                        exit()
      # fila 3
      elif M[2][0] == M [2][1] and   M [2][1] == M[2][2]:
            if not M[0][0] == " ":
                  if "X" in M[2][1]:
                        print(f"Gano el jugador {NombreJugador1}  X")
                        exit()
                  elif "O" in M[2][1]:
                        print(f"Gano el jugador {NombreJugador2}  O")
                                          
                        exit()
       # columna 3
      elif M[0][2] == M [1][2] and   M [1][2] == M[2][2]:
            if not M[0][0] == " ":
                  if "X" in M[1][2]:
                        print(f"Gano el jugador {NombreJugador1}  X")
                        exit()
                  if "O" in M[1][2]:
                        print(f"Gano el jugador {NombreJugador2}  O")
                                          
                        exit()

      #Diagolal \ 
      elif M[0][0] == M [1][1] and   M [1][1] == M[2][2]:
            if not M[0][0] == " ":
                  if "X" in M[0][0]:
                        print(f"Gano el jugador {NombreJugador1}  X")
                        exit()
                  if "O" in M[0][0]:
                        print(f"Gano el jugador {NombreJugador2}  O")
                                          
                        exit()
      #Diagolal \ 
      elif M[0][2] == M [1][1] and   M [1][1] == M[2][0]:
            if not M[0][0] == " ":
                  if "X" in M[2][0]:
                        print(f"Gano el jugador {NombreJugador1}  X")
                        exit()
                  elif "O" in M[2][0]:
                        print(f"Gano el jugador {NombreJugador2}  O")
                                          
                        exit()
      #Verificará si la matris esta llena 
      if not " " in M[0][0] and not " " in M[0][1] and not " " in M[0][2] and not " " in M[1][0] and not " " in M[1][1] and not " " in M[1][2] and not " " in M[2][0] and not " " in M[2][1] and not " " in M[2][2]:
            print("..........EL juego se ha acabado.........")
            exit()
      
      #Cambia el numero de jugador e invoca la logica del juego
      if bueltaa %2 == 0:
            Logica("X",jugador=NombreJugador1)       
      else:
            Logica("O",jugador=NombreJugador2)
                                
      bueltaa = bueltaa + 1
    