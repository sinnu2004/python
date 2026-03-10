# n = int(input("Enter the value "))
#print(n)  # if user write string 

n = None
try:
    n = int(input("Enter the value :"))
except ValueError:
    print("Only pass int values")
else:
    print(n)

