# a block of code which will stops the programme
# 
a = 10
b = 0

#print(a//b)   # exception

# exception handling 
try:
    print(a//b)
except Exception as e:
    print("Value of b is Zero!!")
    