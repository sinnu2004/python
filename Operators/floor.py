# Floor Division -> Nearest and Smallest int number after division 
# a = -27 and b = 12  a//b -> -2.25   answer -> -3  explaination    -3 > -2.25 > -2 
# WAP using Floor Division operator 

def floor(a,b):
    return a//b

a = int(input("Enter the 1st number :"))
b = int(input("Enter 2nd number :"))

print(floor(a,b))