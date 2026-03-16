# It is accessible within the class and its subclass
# it's convention is single underscore


class Car:
    _car_brand = "Toyota"
    
class Brand(Car):
    def display(self):
        print(self._car_brand)

class ani:
    anima = "sa"

a = ani()
print(a.anima)  # it doesn't give error 

c = Car()
# c._car_brand()  it gives an error

b = Brand()
b.display()  