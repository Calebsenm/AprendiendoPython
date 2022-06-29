# Ejercicio 3
# Escribir una función que pida 
# dos números n y m entre 1 y 10, 
# lea el fichero tabla-n.txt con la 
# tabla de multiplicar de ese número, 
# y muestre por pantalla la línea m del 
# fichero. Si el fichero no existe debe 
# mostrar un mensaje por pantalla 
# informando de ello.

def Hello(A,B):
    try:
        with open(f"9_ficheros/{A}.txt","r") as f:
            Contenido = f.readlines()
            print(Contenido[B-1])
    except FileNotFoundError:
        print(f"No existe el fichero con la tabla del {A}")    

Numero1 = int(input("Ingrese un numero -> ")) 
Nunero2 = int(input("ingrese un numeri -> "))

Hello(Numero1,Nunero2)