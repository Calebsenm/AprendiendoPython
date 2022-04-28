#metodo contructor

from mailbox import NoSuchMailboxError


class Persona:   
    pass
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año
    def Descipcion(self):
        return "{} tiene {} años".format(self.nombre,self.año)
    def comentario(self,frase):
        return "{} dice {}".format(self.nombre,frase)


doctor = Persona("José",17)
print(doctor.Descipcion())
print(doctor.comentario("hola como estas"))
"""
José tiene 17 años
José dice hola como estas
"""

# modificar un atributo..

class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

Mi_correo = Email()
print(Mi_correo.enviado)
Mi_correo.enviar_correo()
print(Mi_correo.enviado)

"""
False
True
"""