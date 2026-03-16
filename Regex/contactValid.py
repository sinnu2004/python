import re

number = "9926123455"

pattern = r"^[6-9]\d{9}$"

if(re.match(pattern,number)):
    print("Valid Phone Number")
else :
    print("Invalid Phone Number")
