# Base class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.__strength_level = strength_level  # Encapsulated attribute

    def introduce(self):
        print(f"I am {self.name}, and my power is {self.power}!")

    def get_strength(self):
        return self.__strength_level

    def set_strength(self, new_level):
        if new_level >= 0:
            self.__strength_level = new_level

# Subclass inheriting from Superhero
class FlyingHero(Superhero):
    def fly(self):
        print(f"{self.name} is flying through the skies! 🦸‍♂️✈️")

# Example usage
hero1 = FlyingHero("SkyMan", "Flight", 85)
hero1.introduce()
hero1.fly()
print("Strength Level:", hero1.get_strength())

hero1.set_strength(95)
print("Updated Strength Level:", hero1.get_strength())


#Polymorphism Challenge
# Base class
class Vehicle:
    def move(self):
        pass  # Abstract method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Demonstrates polymorphism
