class InvalidAgeError(Exception):
    pass

age = int(input("Enter your age :"))

if(age>60):
    raise InvalidAgeError("Too young for marriage!!")
else:
    print("Registration Done!!")
