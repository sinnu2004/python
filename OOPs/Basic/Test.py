class Test:
    def __init__(s,name):
        s.name = name
    
    def dis(s):
        return s.name



obj = Test("saurabh")
print(obj.dis())
print(type(obj))