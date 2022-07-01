
class Prey:

    def flee(self):
        print("this animal flees")
    

class Predator:

    def hunt(self):
        print("this animal is hunting")



class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey):
    pass
#-----------------------------------------

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


fish.flee()
fish.hunt()

rabbit.flee()
hawk.hunt()




