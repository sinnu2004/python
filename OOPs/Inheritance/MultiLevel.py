# Multi Level Inheritance -> 

class GrandFather:
    def propery(self):
        print("Land+Gold")

class Father(GrandFather):
    def startup(self):
        print("House+Business")
        
class Son(Father):
    pass

s = Son()
s.propery()
s.startup()