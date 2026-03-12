# WAP to Print MRO

class GrandFather:
    def propery(self):
        print("Land")

class Father:
    def startup(self):
        print("House")
        
class Son(GrandFather,Father):
    pass


print(Son.__mro__)