class Vehicle:
    def go(self):
        pass

class Vehicle:
    def stop(self):
        pass
    
v = Vehicle()   # No Similar name of class is valid it will just reinitialize or remove previous attribute or method
# v.go()  # it will give error
v.stop()