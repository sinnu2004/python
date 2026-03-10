try:
    f = open("data.txt")
except FileNotFoundError:
    print("Upload a pure file!!")
else:
    print(f)