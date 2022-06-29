# Ejercicio 2
# Escribir una función que 
# pida un número entero entre 
# 1 y 10, lea el fichero tabla-n.txt 
# con la tabla de multiplicar de ese 
# número, done n es el número introducido,
# y la muestre por pantalla. 
# 
# Si el fichero no existe debe mostrar 
# un mensaje por pantalla informando de ello.


# def Fichero(N):


#     return

# Fichero(input("Ingresa un numero -> "))


n = int(input('Introduce un número entero entre 1 y 10: '))
try: 
    with open(f"9_ficheros/{n}.txt" , 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)