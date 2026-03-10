a = [1,2,3,4]

#print(a[8]) # give index out exception


try:
    print(a[8])
except IndexError:
    print("Tried to retrive the value outside the list")
finally:
    print("Code Completed!")