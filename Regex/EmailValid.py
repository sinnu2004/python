import re

email = "prajapatsaurabh@gmail.com"

pattern = r"^[a-zA-Z._0-9%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if(re.match(pattern,email)):
    print("Valid Email")
else :
    print("Invalid Email")
