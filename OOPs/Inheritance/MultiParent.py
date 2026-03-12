# When a class Inherit the property of two or more parent

class GrandFather:
    def propery(self):
        print("Land")

class Father:
    def startup(self):
        print("House")
        
class Son(GrandFather,Father):
    pass

s = Son()
s.propery()
s.startup()