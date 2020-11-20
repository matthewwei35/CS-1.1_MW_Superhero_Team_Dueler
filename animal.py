# -----------------
# animal.py
# -----------------

# Animal Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

# Frog Class
class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping")

lion = Animal("Lion")
lion.eat()
lion.drink()

frog = Frog("Frog")
frog.eat()
frog.drink()
frog.jump()
