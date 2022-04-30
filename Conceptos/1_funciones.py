####################################################
#la primera funcion
def hola_mundo():
    print("! Hola señores !")

hola_mundo()

""" 
! Hola  señores ¡
"""
#####################################################
#con asignaciones 

def hola2(nombre,apellido):
    print(f"hola {nombre} {apellido} ")

hola2(nombre = "Caleb",apellido = "Seña")
"""
una alternativa seriá

nombre = Caleb 
apellido = Seña

hola2(nombre,apellido)


tambien se pueden colocar directamente en la funccion asi

def hola(nombre = "hola "):
    print(nombre)
"""

""" 
Caleb seña 
"""
######################################################
def test():
    return "Una cadena", 20, [1,2,3]

cadena, numero, lista = test()

print(cadena)
print(numero)
print(lista)

