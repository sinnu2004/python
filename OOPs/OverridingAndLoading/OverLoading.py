# when the method name is same but parameter is changed in another inherited class

class Calculator:
    def add(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b
    
    def add(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return self.a + self.b + self.c
    
c = Calculator()
print(c.add(2,3,5))