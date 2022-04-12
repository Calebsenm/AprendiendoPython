"""
diseña un programa que calcule el porcentaje del numero asignado de esta manera: 
En un grupo de 600 alumnos calcula el porcentage del  10% de los alumnos hasta el 100%

"""

CantidadDeAlumnos = 600
for i in range(10,101,10):

    porcentaje = CantidadDeAlumnos * i /100
    a = round(porcentaje)
    print(f"El {i}% de los alumnos 600 alumnos es: {a} ")
    



