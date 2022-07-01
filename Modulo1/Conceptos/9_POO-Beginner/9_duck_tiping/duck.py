from turtle import pen


class Duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is qcuacking")

class Chicken:
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person():
    def cath(self,duck):
        duck.walk()
        duck.talk()
        
        print("You caught the critter !")

#---------------------------------------------------------

duck = Duck()
chicken  = Chicken()
person = Person()


duck.talk()
duck.walk()


chicken.talk()
chicken.walk()

person.cath(duck)
