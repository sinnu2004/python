class op:
    def add(self,a,b):
        return a + b
    

plus_op = op()
print(plus_op.add("hello","world"))
print(plus_op.add(2,3))