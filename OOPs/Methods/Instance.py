# Method is valid for a particular method is called instance
# name and age is intances of s1 and s2 object respectively
# the instance is not same for s1 and s2 object 

class Animal:
    def __init__(self,name):
        self.name = name
    def dis(self):
        return self.name

dog = Animal("Pewo")
print(dog.dis())