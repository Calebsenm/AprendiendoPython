# OOP Exercise 3: Create a child class 
# Bus that will inherit all of the variables 
# and methods of the Vehicle class


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
        pass

# Create a Bus object that will inherit all
# of the variables and methods of the 
# parent Vehicle class and display it.

# Expected Output:

# Vehicle Name: School Volvo 
# Speed: 180 Mileage: 12

car_1 = Bus("School Volvo", 180, 12)
print("Vehicle Name:",car_1.name, "Speed:", car_1.max_speed, "Mileage:", car_1.mileage)

