# WAP using classes to print name, age, address, enrollment no of student

class Student:
    def __init__(self,name,age,address,enroll):
        self.name = name
        self.age = age
        self.address = address
        self.enroll = enroll
        
    def dis(self):
        print(self.name,self.age,self.address,self.enroll)

s1 = Student("saurabh",22,"Indore","00268")
s2 = Student("Ravi",22,"Sagar",60)

s1.dis()
s2.dis()