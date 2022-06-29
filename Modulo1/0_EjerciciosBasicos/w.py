# # n = int(input("Introduce un número entero positivo mayor que 2: "))
# # i = 2
# # while n % i != 0:
# #     i += 1
# # if i == n:
# #     print(str(n) + " es primo")
# # else:
# #     print(str(n) + " no es primo")


# # h = {"a":1,"b":2}

# # if 1 in h:
# #     print("Yes")

# a = {1:{"itt":"True" ,"oll":11}, 2:{"itt":"False" ,"oll":11}}

# for llave,key in a.items():
#     if key["itt"] == "True":
#         for llave2,key2 in key.items():
#             print(llave2,":",key2)



# # Ejercicio 10
# # Escribir un programa que permita gestionar la 
# # base de datos de clientes de una empresa. Los 
# # clientes se guardarán en un diccionario en el 
# # que la clave de cada cliente será su NIF, y el
# #  valor será otro diccionario con los datos del 
# # cliente (nombre, dirección, teléfono, correo, 
# # preferente), donde preferente tendrá el valor 
# # True si se trata de un cliente preferente. El
# #  programa debe preguntar al usuario por una opción 
# # del siguiente menú: (1) Añadir cliente, (2) Eliminar 
# # cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
# #  (5) Listar clientes preferentes, (6) Terminar. 
# # En función de la opción elegida el programa tendrá
# #  que hacer lo siguiente:

# # 1 Preguntar los datos del cliente, crear un diccionario 
# # con los datos y añadirlo a la base de datos.
# #
# # 2 Preguntar por el NIF del cliente y eliminar sus datos 
# # de la base de datos.
# # 
# # 3 Preguntar por el NIF del cliente y mostrar sus datos.
# # 
# # 4 Mostrar lista de todos los clientes de la base datos 
# # con su NIF y nombre.
# # 
# # 5 Mostrar la lista de clientes preferentes de la base 
# # de datos con su NIF y nombre.
# # 
# # 6Terminar el programa.

# # inicio 6:45 pm - 21/06/2022
# #fin     10:00 pm - 21/06/2022


# from os import system
# import sys

# Base_Datos = {}
# Menu = {1:"Añadir cliente",2:"Eliminar cliente",3:"Mostrar cliente",4:"Listar todos los clientes",5:"Listar clientes preferentes",6:"Terminar"}



# while True:
#     system("cls")
#     for i in Menu:
#         print(i,Menu[i])

#     a = int(input("Que deseas escoger -> "))
#     if a == 1:
#         nif = input("Ingresa el nif del cliente ")
#         nombre = input("Ingresa el nombre ")
#         direccion = input("Ingresa la direccion ")
#         telefono = input("Ingresa el telefono ")
#         correo = input("ingresa tu correo ")
#         preferente = input("preferente ")

#         Base_Datos[nif] = {
#             "niff" : nif,
#             "Nombre" : nombre,
#             "Direccion" : direccion,
#             "Telefono" : telefono,
#             "Correo" : correo,
#             "Preferente": preferente    
#         }

#     elif a == 2:
#         nifff = input("Ingresa el nif ")
#         for o,p in Base_Datos.items():
#             if o == nifff:
#                 for m,n in p.items():
#                     p[m] = 0
#         print(f"El usuario  {nifff} ha sido eliminado correctamente ")
#         a = input("Ingrese cualquier letra para continuar ")
#         # Base_Datos[nifff].clear()
#     elif a == 3:
#         niff = input("Ingresa el nif que deseas motrar ")
#         for ll,kk in Base_Datos[niff].items():
#             print(ll,":",kk)
#         a = input("Ingrese cualquier letra para continuar ")
#     elif a == 4:

#         for key,value in Base_Datos.items():
#             print(key)
#             for key2,value2 in value.items():
#                 print(key2,":",value2)
#         a = input("Ingrese cualquier letra para continuar ")

#     elif a == 5:
#         for llave,valor in Base_Datos.items():
#             print(f"El niff {llave}")
#             if valor["Preferente"] == "True":
#                 for llave2,valor2 in valor.items():
#                     print(f"{llave2}:{valor2}")
#         a = input("Ingrese cualquier letra para continuar ")
#     elif a == 6:
#         break
#     else:
#         print("Fatattattataa") 
        
                  

# key_list = ['name', 'age', 'address']
# value_list = ['Johnny', '27', 'New York']

# dict_from_list = {key_list[i]: value_list[i] for i in range(len(key_list))}
# print(dict_from_list)

##################################################

# print(pow(10,0.5))

##################
# para ordenar y luego invertir


#recurisvidad

# hola = [2,23,53,676,3,64,754,854,3,40,222,43,23,34,33,6]
# hola2 = [2,5,3,1,212,2,3,1,40,4,3,224,8,6]
# hola.sort()
# hola2.sort()


# print(hola)

# def recursivo(a,b = hola):

#     if b[a-1] in hola2:
#         print(b[a-1])
#         return 1
#     if a == 0 or a == 1:
#         return 1
#     return recursivo(a-1)
    

# recursivo(len(hola))


#######################################################

## Bucle recursivo JAJJAJAJAJJa
# hola = [1,2]


# def mimi(A,B,C = 0):
#     print(C)
#     if A == 0 or A == 1:
#         return 1
#     return mimi(A-1,B,C+1)

# mimi(len(hola),hola)



# def A(a=1):
#     print(a)
#     return A(a+1) 
# A()

##############################


# l = "123432345432"

# for i in l:
#     print(i)

# hola = { "a": 1 }
# p = tuple(zip(hola.keys(),hola.values()))
# print(p)


# hola = {1:345}
# print(hola[1])



#26/06/2022 

# ##un bug tremendo que 
# from math import sin, cos, tan, exp, log

# Valores = {}

# def ciclo(A,B):
#     for i in range(B):
#         Valores[i+1] = A(i+1)
    

# def seno(numero):

#     ciclo(sin,numero)
   

# def coseno(numero1):
#     ciclo(cos,numero1)
  

# def tangente(numero2):
#     ciclo(tan,numero2)
    

# def exponencial(numero3):
#     ciclo(exp,numero3)
    

# def nerperiano(numero4):
#     ciclo(log,numero4)
    

# def opcion(a,b):
#     opciones = [seno(b),coseno(b),tangente(b),exponencial(b),nerperiano(b)]
#     return opciones[b-1]

# opciones = {1:"seno",2:"coceno",3:"tangente",4:"exponencial",5:"logaritmo nerperiano"}
# for i,j in opciones.items():
#     print(i,j)
# operacion = int(input("Ingresa el numero dela opcion -> "))
# numero = int(input("Ingresa el numero -> "))


# opcion(operacion,numero)

# for i,j in Valores.items():
#     print(i,"->",j)





# def a():
#     print("A")

# def b():
#     print("B")

# horas_del_dia = int(input("Ingresa tu hora: ") )
# def lista(hola):
#     horas = {
#     1:a(),
#     2:b(),
    
#     }  
#     return horas.get(hola,"Que te pasa no ves que debes ingresar un numero solo dentro del rango")
# hola = horas_del_dia
# print(lista(hola))
