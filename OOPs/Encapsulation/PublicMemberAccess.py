# Public member can access using getter/setter method and name mangling methods

class Animal:
    def __init__(self,s):
        self.__s = s
    
    def dis(self):
        return self.__s

cat = Animal("meow")

print(cat.dis())  # access using getter/setter method
print(cat._Animal__s)   # access using name mangling method 

