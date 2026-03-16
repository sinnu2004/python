# Encapsulation is the concept of OOPs where we bundle data member and method. So 
# No one can directly access the data and attribute

# Normal convention for the public member
# single underscore(_) for the protected member
# double underscore(__) for the private memeber

class Animal:
    def __init__(self,name):
        self._name = name

dog = Animal("pewo")
# print(dog.name) # it gives error
print(dog._name)