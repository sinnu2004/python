# Single Level Inheritance -> When a class is inherited property of only one class

class Electronics:
    def __init__(self):
        pass
    
    def dis(self):
        print("hello world")

class light(Electronics):  # the light class inherit the property of Electronics
    pass

L = light()   
L.dis()