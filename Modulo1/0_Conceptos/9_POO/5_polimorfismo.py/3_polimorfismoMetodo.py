class Colombia:
    def capital(self):
        print("Bogotá")

    def idioma(self):
        print("español")

class Francia:
    def capital(self):
        print("Paris")

    def idioma(self):
        print("Frances")


colombiano = Colombia()
frances = Francia()

for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()