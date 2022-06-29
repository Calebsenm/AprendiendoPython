#Crear una lista en exel 
#con la nota de los alumnos en matematicas

#Debe haver 10 notas y al final debe mostrar
#La nota final del Estudiante

from os import system


Opciones = {1:"Crear un archivo",2:"Ingresar notas"}
Asignatura2 = 0
while True:
    system("cls")
    for i,j in Opciones.items():
        print(i,j)
     
    decicion = int(input("ingresa una decicion -> "))
    if decicion == 1:
        Asignatura = input("Ingrese la asignatura -> ") 
        Asignatura2 = Asignatura
        Fichero = open(f"./{Asignatura}.csv","w")
        Fichero.write("Nombre;Nota1;Nota2;Nota3;Nota4;Nota5;Nota final;Aclaracion;\n")
        Fichero.close()
        input("Has creado corectamente el archivo \nIngresa cualquier leytra para contuar")

    elif decicion == 2:

        Notas = []
        Notas2 = Notas
       

        Fichero = open(f"./{Asignatura}.csv","a",encoding="utf-8")
        Promedio = 0

        j = 0
        for i in range(6):
            if j == 0:
                ASD = input("Ingresa el nombre ->")
                Notas.append(ASD)
            else:
                asd = int(input(f"Ingresa la nota {j} -> "))
                Notas.append(asd)
            j += 1

        for jk in Notas:
            Fichero.write(f"{jk};")

        Notas2.pop(0)
        for l in Notas2:
            Promedio += l
        Promedio2 = Promedio / len(Notas2)
        
        Fichero.write(f"{Promedio2};")
        if Promedio2 >= 0 and Promedio2 <= 1:
            Fichero.write(f"Usted es una decepción;\n")

        if Promedio2 > 1 and Promedio2 < 3:
            Fichero.write(f"Usted Debe estudiar;\n")
        if Promedio2 > 3 and Promedio2 < 4:
            Fichero.write(f"Usted le Debe dar pena lo que saco;\n")
        if Promedio2 > 4 and Promedio2 < 4.8:
            Fichero.write(f"Usted Saco una nota buena ;\n")
        if Promedio2 > 4.8 and Promedio2 <= 5:
            Fichero.write(f"Felicidades por su notal Alta;\n")

        
        Fichero.close()
        input("Has ingresado corectamente Las notas \nTngresa cualquier leytra para contuar")
            
           



        
    
