

class Organism():
    alive = True

class Animal(Organism):
    def eat(self):
        print("this animal is eating ")


class Dog(Animal):
    def bark(self):
        print("this dog is barking ")


class Cat(Animal):
    def meow(self):
        print("this cat is meowing")

# -----------------------------------------------
dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
# --------------------------------
cat = Cat()
print(cat.alive)
cat.eat()
cat.meow()

