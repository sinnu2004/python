# Hierarichal Inheritance

class Animal:
    def dis(self):
        print("Eating")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Cow(Animal):
    pass

A = Animal()
C = Cat()
D = Dog()
c = Cow()

print(A.dis(),C.dis(),D.dis(),c.dis())