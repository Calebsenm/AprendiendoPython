"""
Ejercicio 2
Escribir un programa que almacene 
las asignaturas de un curso 
(por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una 
lista y la muestre por pantalla el 
mensaje Yo estudio <asignatura>, 
donde <asignatura> es cada una de las 
asignaturas de la lista.


finished  12/06/2022 
"""
subjects =  []
while True:
    
    the_subject = input("Input a subject >> ")
    subjects.append(the_subject)
    for i in subjects:
        print("yo estudio "+i)
