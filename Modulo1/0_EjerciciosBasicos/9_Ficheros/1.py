# Ejercicio 1
# Escribir una función que pida un número 
# entero entre 1 y 10 y guarde en un fichero 
# con el nombre tabla-n.txt la tabla de multiplicar 
# de ese número, done n es el número introducido.


def Numero(A,B = 1):
    
    with open(f"1","a") as f:
        f.write(f"{B} X {A} = {B*A}\n")
   
    if B == 10:
        return 
    
    return Numero(A,B+1)

Numero(int(input("Ingresa un numro -> ")))