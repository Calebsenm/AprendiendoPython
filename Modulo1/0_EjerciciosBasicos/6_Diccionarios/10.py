# Ejercicio 10
# Escribir un programa que permita gestionar la 
# base de datos de clientes de una empresa. Los 
# clientes se guardarán en un diccionario en el 
# que la clave de cada cliente será su NIF, y el
#  valor será otro diccionario con los datos del 
# cliente (nombre, dirección, teléfono, correo, 
# preferente), donde preferente tendrá el valor 
# True si se trata de un cliente preferente. El
#  programa debe preguntar al usuario por una opción 
# del siguiente menú: (1) Añadir cliente, (2) Eliminar 
# cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
#  (5) Listar clientes preferentes, (6) Terminar. 
# En función de la opción elegida el programa tendrá
#  que hacer lo siguiente:

# 1 Preguntar los datos del cliente, crear un diccionario 
# con los datos y añadirlo a la base de datos.
#
# 2 Preguntar por el NIF del cliente y eliminar sus datos 
# de la base de datos.
# 
# 3 Preguntar por el NIF del cliente y mostrar sus datos.
# 
# 4 Mostrar lista de todos los clientes de la base datos 
# con su NIF y nombre.
# 
# 5 Mostrar la lista de clientes preferentes de la base 
# de datos con su NIF y nombre.
# 
# 6Terminar el programa.

# inicio 6:45 pm - 21/06/2022
#fin     10:00 pm - 21/06/2022


from os import system
import sys

Base_Datos = {}
Menu = {1:"Añadir cliente",2:"Eliminar cliente",3:"Mostrar cliente",4:"Listar todos los clientes",5:"Listar clientes preferentes",6:"Terminar"}



while True:
    system("cls")
    for i in Menu:
        print(i,Menu[i])

    a = int(input("Que deseas escoger -> "))
    if a == 1:
        nif = input("Ingresa el nif del cliente ")
        nombre = input("Ingresa el nombre ")
        direccion = input("Ingresa la direccion ")
        telefono = input("Ingresa el telefono ")
        correo = input("ingresa tu correo ")
        preferente = input("preferente ")

        Base_Datos[nif] = {
            "niff" : nif,
            "Nombre" : nombre,
            "Direccion" : direccion,
            "Telefono" : telefono,
            "Correo" : correo,
            "Preferente": preferente    
        }

    elif a == 2:
        nifff = input("Ingresa el nif ")
        for o,p in Base_Datos.items():
            if o == nifff:
                for m,n in p.items():
                    p[m] = 0
        print(f"El usuario  {nifff} ha sido eliminado correctamente ")
        a = input("Ingrese cualquier letra para continuar ")
        # Base_Datos[nifff].clear()
    elif a == 3:
        niff = input("Ingresa el nif que deseas motrar ")
        for ll,kk in Base_Datos[niff].items():
            print(ll,":",kk)
        a = input("Ingrese cualquier letra para continuar ")
    elif a == 4:

        for key,value in Base_Datos.items():
            print(key)
            for key2,value2 in value.items():
                print(key2,":",value2)
        a = input("Ingrese cualquier letra para continuar ")

    elif a == 5:
        for llave,valor in Base_Datos.items():
            print(f"El niff {llave}")
            if valor["Preferente"] == "True":
                for llave2,valor2 in valor.items():
                    print(f"{llave2}:{valor2}")
        a = input("Ingrese cualquier letra para continuar ")
    elif a == 6:
        break
    else:
        print("Fatattattataa") 
        
                  










