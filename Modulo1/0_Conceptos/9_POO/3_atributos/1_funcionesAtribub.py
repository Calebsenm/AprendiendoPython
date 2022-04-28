from pydoc import doc
from unittest.mock import seal


class Persona:
    Edad = 17
    nombre = "victor"
    pais = "colombia"

doctor = Persona()

print("la edad es: ",doctor.Edad)

#tener el valor de l atributo de manera directa
print("la edad es:  ",getattr(doctor,"Edad"))


"""
La edad es: 17
La edad es: 17

"""
#si existe valores... hasttr
print("el doctor tiene una edad? ",hasattr(doctor,"Edad"))

"""
el doctor tiene una edad?  True
"""
#el metodo para cambiar
print("el nombre es: ",doctor.nombre)
setattr(doctor,"nombre","Caleb")
print("el nombre es: ",doctor.nombre)

"""
el nombre es:  victor
el nombre es:  Caleb
"""
#Para eliminar
delattr(Persona.pais)

"""
Error...
"""