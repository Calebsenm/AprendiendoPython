# Ejercicio 6
# Escribir un programa que almacene 
# las asignaturas de un curso (por ejemplo 
# Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha 
# sacado en cada asignatura y elimine de la lista 
# las asignaturas aprobadas. Al final el programa 
# debe mostrar por pantalla las asignaturas que el 
# usuario tiene que repetir.

# finikitado xd 



subjects = ["Matemáticas"," Física", "Química", "Historia","Lengua"]
notes = []
lol = []
for i in subjects:
    notes2 = int(input(f"plese input las notas of {i} -> "))
    notes.append([i,notes2])
    lol.append([i,notes2])

for a in notes: 
    if a[1] >= 3: 
        lol.remove(a)

for b in range(len(lol)) :
    print(f"Usted debe repetir {notes[b][0]} Your nota {notes[b][1]}")
    print("Esto es espanglish")
    