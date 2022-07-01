# OOP Exercise 5: Define a property that must
#  have the same value for every class instance (object)

# Define a class attribute”color” 
# with a default value white. I.e., 
# Every Vehicle should be white.

# Use the following code for this exercise.

class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# Expected Output:

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18



Car_1 = Bus("School Volvo",180,12)


print(f"Color: {Car_1.color}, Vehicle name: {Car_1.name}, Speed: {Car_1.max_speed}, Mileage: {Car_1.mileage}")

car = Car("Audi Q5", 240, 18)
print("Color",car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)