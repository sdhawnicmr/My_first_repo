class Animal:
    alive = True
    def __int__(self):
        self.eyes = 2

    def eat(self):
        print("eats grass")
    def sleep(self):
        print("Sleep at night")

class Fish(Animal):
    def __init__(self):
        super().__int__()

    def eat(self):
        print("Eats insect")

fish= Fish()
fish.eat()
print(fish.alive)
print(fish.eyes)