# ABC (Abstract Base Class) is used to achieve data abstraction
# @abstractmethod are used to abstract any method

from abc import ABC, abstractmethod

class Gree(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class English(Gree):
    def say_hello(self):
        return "hello"
    
g = English()
print(g.say_hello())