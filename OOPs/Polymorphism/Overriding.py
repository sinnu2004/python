# Overriding -> When the method name is same but implementation is changed
# Rules : 1. For Overriding a class must inherit property of class which we override
# 2. the method name must be same 

class Father:
    def marry(self):
        print("Salini")
class Son(Father):
    def marry(self):
        print("shilpa")
    
s = Son()
s.marry()