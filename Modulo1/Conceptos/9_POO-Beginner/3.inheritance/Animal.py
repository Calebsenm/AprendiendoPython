
class Animal:
    alive  = True

    def eat(self):
        print("this animal is eating")
    

    def sleep(seld):
        print("this animal is sleeping")


#inheritance
class Rabbit(Animal):
    def run(self):
        print("this animal is running")

class Fish(Animal):
    def swim(self):
        print("this animal is swimming")

class Hawk(Animal):
    def fly(self):
        print("thi animal is fliying")
    



#---------------------------------------------------
#objets 

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()


print(rabbit.alive)
rabbit.eat()

#----------------------------------------------------
rabbit.run()
fish.swim()
hawk.fly()



