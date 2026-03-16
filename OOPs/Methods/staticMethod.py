# Static Method -> It gives freedom to not write any variables 

class Sum:
    @staticmethod
    def add(a,b):
        return a + b

print(Sum.add(2,4))