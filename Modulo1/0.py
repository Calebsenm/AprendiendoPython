# class dog:
#     atri1 = "mamal "
#     atri2 = "dog"

#     #a samopple method

#     def fun(self):
#         print("i am a",self.atri1)
#         print("i am a",self.atri2)

# Rodger = dog()
# print(Rodger.atri1)
# Rodger.fun()

###########################################################


# class person:
   
#     #init method 
#     def __init__(self,name) -> None:
#         self.name = name

#     #sample Method
#     def say_hi(self):
#         print("hello my  name is",self.name)

# p = person("caleb")
# p.say_hi()

#      


###################################################
# Programa Python3 para mostrar que las variables con un valor
# asignado en la declaración de clase, son variables de clase y
# Las variables dentro de los métodos y los constructores son instancia
# variables


#class for the dog 


class Dog:
    animal = "parrot"

    def __init__(self,color,breed):
        self.color = color
        self.breed = breed


#objects of a class

lorito1 = 