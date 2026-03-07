# Modulus Operator -> used for finding remainder

# Conditions : 
# 1 if a>b -> Calculate exact remainder
# 2 is a<b -> directly the answer is a 
# 3 if a or b negative then : a%b -> a + (-b * (a//b))

def mod(a,b):
    return a%b

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

print(mod(a,b))