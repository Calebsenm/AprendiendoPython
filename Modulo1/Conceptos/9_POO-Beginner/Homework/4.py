# OOP Exercise 4: Class Inheritance
# Given:

# Create a Bus class that inherits from the 
# Vehicle class. Give the capacity argument of 
# Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # def seating_capacity(self, capacity):
    #     return f"The seating capacity of a {self.name} is {capacity} passengers"
# ----------------------------------------------------


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage,passengers):
        super().__init__(name, max_speed, mileage)
        self.passengers = passengers
# The seating capacity of a bus is 50 passengers

#---------------------------------------------------------------------
car_1 = Bus("Bus",180,12,50)
print(f"the seating capacity of a bus is {car_1.passengers} passengers ")

