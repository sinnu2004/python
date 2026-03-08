n = 5

alpha = 65

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(chr(alpha),end=" ")
    print("\n")
