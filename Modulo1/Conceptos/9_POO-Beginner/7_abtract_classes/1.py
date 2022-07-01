from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("this car is stopped")



class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("this motorcycle is stopped")
    
#---------------------------------------
car = Car()
motorcicle = Motorcycle()

car.go()
motorcicle.go()

car.stop()
motorcicle.stop()



