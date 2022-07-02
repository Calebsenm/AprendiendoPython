# heremcia multiple 

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("LLamando....")

    def ocupado(self):
        print("ocupado....")


class Camara:
    def __init__(self):
        pass
    def Fotografia(self):
        print("tomando fotos...")

class Reproduccion:
    def __init__(self):
        pass
    def reproducciondemusica(self):
        print("reproduciendo Musica")
    def reproducirvideo(self):
        print("reproducir un video....")


class smartfone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print("telefono apagado")

movil = smartfone()
print(movil.Fotografia())
print(movil.llamar())