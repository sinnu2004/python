try:
    print(10//0)
    try:
        a = [1,2,3]
    except IndexError:
        print("Tried to retrieve element outside list")
except ZeroDivisionError:
    print("Tried to divide by zero!!")
finally:
    print("Code Completed!!")