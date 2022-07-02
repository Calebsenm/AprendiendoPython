#Clases y objetos

# class Carro:
#     marca = "x"
#     modelo = "1"
#     placa = "0110"

# Renoul = Carro()
# print(Carro.placa)
# print(Carro.modelo)
# print(Carro.marca)

# A = Carro.placa
# print(A)
#################################################
#Clases y objetos

# class EquipoA:
#     Jugador1 = "Caleb1" 
#     Jugador2 = "Caleb3"
#     Jugador3 = "Caleb3"
#     Jugador4 = "Caleb4"

# class EquipoB:
#     Jugador1 = "Lolo1"
#     Jugador2 = "Lolo2"
#     Jugador3 = "Lolo3"
#     Jugador4 = "Lolo4"


# print(EquipoA.Jugador1)
# print(EquipoB.Jugador2)


# class Persona:
#     pass

# Caleb1 = Persona()
# Caleb2 = Persona()


# Caleb1.Edad = 10
# Caleb1.Estatura = 23
# Caleb1.Pais = "Colombia"
# Caleb1.Sexo = "M"

# Caleb2.Edad = 10
# Caleb2.Estatura = 23
# Caleb2.Pais = "Colombia"
# Caleb2.Sexo = "M"


# print(Caleb1.Edad)
# print(Caleb2.Edad)


#____________________________________________________________
# Metodo self
# sel hace referencia a el mismo se piuede colocar otro nombre 
# self es el argumento que se le pasa a la funcion para luego llamarla 

#____________________________________________________________


# class Matematicas:
#     def Suma(hola):
#         hola.Numero1 = 1
#         hola.Numero2 = 2

#     def Resta(hola2):
#         hola2.Numero1 = 2
#         hola2.Numero2 = 2

# suma = Matematicas()
# suma.Suma()
# resta = Matematicas()
# resta.Resta()

# print(suma.Numero1 + suma.Numero2)
################################################################################
# __init__  se inicialisa antes y no es sesesario colocar un color
################################################################################

# class Ropa:
#     def __init__(self):
#         self.Color = "ROJO"
#         self.Marca = "M"
#         self.Talla = "Prado"
    
#     def __init__(self) :
#         self.Precio = 200

# sueter = Ropa()
# print(sueter.Precio)



class Calculadora:
    def __init__(self,Numero1,Numero2):
        self.Suma = Numero1 + Numero2
        self.Resta = Numero1 - Numero2
        self.Multiplicacion = Numero1 * Numero2
        self.Division = Numero1 / Numero2

Operacion = Calculadora(20,10)

print(Operacion.Suma)

    