from abc import ABC, abstractmethod

class Animal(ABC):
    
    @property
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        print("Bhaow")
        
d = Dog()
d.sound()