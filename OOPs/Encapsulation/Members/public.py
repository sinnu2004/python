# Public class has no conventions it can access inside or outside class both

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
e = Employee("saurabh",22)
print(e.name,e.age)