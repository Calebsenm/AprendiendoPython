# Ejercicio 8
# Escribir una función reciba un diccionario 
# con las asignaturas y las notas de un alumno 
# y devuelva otro diccionario con las asignaturas 
# en mayúsculas y las calificaciones correspondientes 
# a las notas aprobadas

Dicionario = {
    "matematicas":4,
    "lengua":1,
    "sociales":1,
    "ingles":5,
    "imformatica":5
}

def Funcion(A):
    B = {}
    for i,j in A.items():
        AB = ""
        if j == 1:
            continue
        elif j == 2:
            continue
        elif j == 3:
            AB = "Regular"
        elif j == 4:
            AB = "Alto"
        else:
            AB = "Superior"

        B[i.upper()] =  AB.upper()
    
    return B

A = Funcion(Dicionario)
for i,j in A.items():
    print(i,"-",j)

