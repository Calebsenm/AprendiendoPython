# // """
# // Escribir un programa que pregunte al 
# // usuario la fecha de su nacimiento en 
# // formato dd/mm/aaaa y muestra por pantalla, 
# // el día, el mes y el año. Adaptar el programa
# // anterior para que también funcione cuando el 
# // día o el mes se introduzcan con un solo carácter.
# // """

#finikitado el 5/05/2022          estubo conplicado eh si que si hombre
#aproximadamente 1 hora XD

#este algorimoe es capaz de eliminar barras o cualquier cosa y puede imprimir con una desacripcion


#esta variable almacena los datos ingresados
Dia_nacimiento = input("Ingresa tu fecha de nacimiento separada por / >> ")

# se convierte en una lista Lista[""] y es almacenada en una variable
Lista = list(Dia_nacimiento)

#almacena la posición de las / en una lista 
Indice_Barra = []

#este ciclo va recorrieno la lista y verifica si hay un /
#guarda la posición de la  / en una lista 
for i in range(len(Lista)):
    if Lista[i] == "/":
        Indice_Barra.append(i)
    
#imprimer los dias XD meses y años
print(
    
    "Dia = ",Dia_nacimiento[0:Indice_Barra[0]],
    "Mes = ",Dia_nacimiento[Indice_Barra[0]+1:Indice_Barra[1]],
    "Año = ",Dia_nacimiento[Indice_Barra[1]+1:]
)