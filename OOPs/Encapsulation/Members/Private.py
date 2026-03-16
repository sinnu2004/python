# Private member are indicated by double underscore before function 
# it is not accessible by outside the class

class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    
    def dis(self):
        return self.__name,self.__salary

# no use of private member
class Animal:
    def __init__(self,name):
        self.name = name
        

e = Employee("saurabh",40000)
# e.__name()   # it gives error
print(e.dis())


# accessing without private member 
d = Animal("pewo")  
print(d.name)