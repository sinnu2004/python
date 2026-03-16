import re 

# """ [a-z] -> LowerCase letteres
# [A-Z] -> UpperCase letters
# [0-9] -> digits
# \d -> digits
# \D -> non-digits """

text = "python is Awesome since 1995"

lowercase = re.findall(r"\S+",text)
print(lowercase)

print(re.findall(r"p{1}",text))
print(re.findall(r"p{1,3}",text))
print(re.findall(r"s+",text))


