# Conditional Statements

# 1 : if statements

# WAP to print is a number is even or not

def iseven(n):
    if(n%2==0):
        return True
    return False

n = int(input("enter the number :"))
print(iseven(n))


# 2 : if-else statement

# WAP a program to check if even or odd 

def isnum(n):
    if(n%2==0):
        print("Even number")
    else :
        print("Odd number")

n = int(input("Enter the number:"))
isnum(n)

# 3 : if elif statement

# WAP to print grades of marks 

def marks(n):
    if(n>=90):
        print("Grade A")
    elif(n>=80 and n<90):
        print("Grade B")
    elif(n>=70 and n<80):
        print("Grade c")
    elif(n>=60 and n<70):
        print("Grade D")
    elif(n>=33 and n<60):
        print("Grade F")
    elif(n<33):
        print("Fail")

n = int(input("Enter the number "))
marks(n)