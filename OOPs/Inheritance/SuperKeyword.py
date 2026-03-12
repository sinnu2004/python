# Super Keyword is used to inherit the value of other classes

class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        
    def dis(self):
        print(self.name,self.age,self.address)
    
class Employee(Person):
    def __init__(self,name,age,address,salary,dept):
        super().__init__(name,age,address)
        self.salary = salary
        self.dept = dept
        
    def dis2(self):
        print(self.name,self.age,self.address,self.address,self.salary,self.dept)
    

e = Employee("saurabh",22,"Indore",100000,"IT")
e.dis()
e.dis2()