"""
Escribir un programa que almacene 
las asignaturas de un curso 
(por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una 
lista, pregunte al usuario la nota 
que ha sacado en cada asignatura, y 
después las muestre por pantalla con 
el mensaje En <asignatura> has sacado 
<nota> donde <asignatura> es cada una 
des las asignaturas de la lista y <nota> 
cada una de las correspondientes notas 
introducidas por el usuario.

Finikitado 8:34 
12/06/2022
"""

subjects = []
qualification = []

while True:
    o = 0
    while o != 5:
        subject = input("please input a subject > ")
        subjects.append(subject)
        quan1 = input("please input a qualification  > ")
        qualification.append(quan1)

        o += 1 
    j = 0
    for i  in  subjects:
        print(f"En la asignatura de {i} Obtuviste {qualification[j]}")

        j += 1
