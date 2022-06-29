# Ejercicio 6
# Escribir un programa para gestionar 
# un listín telefónico con los nombres y 
# los teléfonos de los clientes de una empresa. 

# El programa incorporar funciones crear el fichero 
# con el listín si no existe,
#  para consultar el teléfono
#  de un cliente,
# 
#  añadir el teléfono de un nuevo cliente 
# y eliminar el teléfono de un cliente. 
# 
# El listín debe 
# estar guardado en el fichero de texto listin.txt donde 
# el nombre del cliente y su teléfono deben aparecer 
# separados por comas y cada cliente en una línea distinta.

#finished 6:18 pm
#28/06/2022 

from os import system



def Lista_Contactos(Cntp):
    with open("9_ficheros/Lita.txt","a") as Lista:
        Lista.write(f"{Cntp}\n")

def Numero(Nombre):
    try :
        with open("9_ficheros/Lita.txt","r") as Numero:
            for i in Numero.readlines():
                A = i.split(",")
                if A[0] == Nombre:
                   return f"{A[0]} -> {A[+1]}"
                else:
                     return f"El numero de telefono de {Nombre} no \nno se ecuentra registrado"          
    except FileNotFoundError:
        return "Erorr no se encuentra un archivo "

def Crear(A):
    with open("9_ficheros/Lita.txt","a") as Numero:
        Numero.write(A+"\n")
            

def Borrar(Nombre):
    F = open("9_ficheros/Lita.txt","r")
    Lineas = F.readlines()
    
   
    F.close()

    F = open("9_ficheros/Lita.txt","w")  

    for i in Lineas:
        A = i.split(",")
        if not A[0] == Nombre:
            F.write(i)
    
    F.close()

    


Options = {1:"Crear fichero",2:"Consultar numero",3:"Añadir un nuevo numero",4:"Eliminar cliente"}
while True:
    system("cls")
    for a,i in Options.items():
        print(a,i)
    Option = int(input("Please input a option -> "))
    
    if Option == 1:
        Lista = input("Ingrese El nombre junto con el Telefonno separado por , -> ")
        Lista_Contactos(Lista)
    
    if Option == 2:
        name = input("Que numero deseas buscar ingresa el nombre -> ")
        print( Numero(name))
        a = input("Ingrese cualquier tecla para continuar")
    
    if Option == 3:
        Lista = input("Ingrese El nombre junto con el Telefonno separado por , -> ")
        Crear(Lista)
        
    if Option == 4:
        name = input("Que numero deseas eliminar ingresa el nombre -> ")
        Borrar(name)
        a = input("Ingrese cualquier tecla para continuar")
    if Option == 5:
        break

    