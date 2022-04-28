#Herencia

from mailbox import NoSuchMailboxError


class Pajaro:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def Descripcion(self):
        return "{} es un pajaro de tipo {}".format(self.nombre,self.tipo)

class loro(Pajaro):
    def ataque(self,tipoataque):
        return "{} tipo de ataque : {}".format(self.nombre,tipoataque)
        

class Aguila(Pajaro):
    def ataque(self,tipoataque):
        return "{} tipo de ataque : {}".format(self.nombre,tipoataque)



Nuevo_pajaro = loro("Periquillo","rabioso")
print(Nuevo_pajaro.Descripcion())
print(Nuevo_pajaro.ataque("Mordida rabisa"))

"""
Periquillo es un pajaro de tipo rabioso
Periquillo tipo de ataque : Mordida rabisa
"""