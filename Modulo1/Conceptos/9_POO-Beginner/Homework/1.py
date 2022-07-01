
# OOP Exercise 1: Create a Class with instance 
# attributesWrite a Python program 
# to create a Vehicle class with max_speed 
# and mileage instance attributes.


class Carro:
    def __init__(self,Max_peed,mileage):
        self.Max_peed = Max_peed
        self.mileage = mileage

Car_1 = Carro(123456,87654)
print(Car_1.Max_peed,Car_1.mileage)