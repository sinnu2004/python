dis = {
    "name": "saurabh",
    "age" : 22,
    "address": "Indore"
}

dis.pop("name")
print(dis)

dis.popitem()
print(dis)

dis["name"] = "saurabh"
dis["address"] = "Bhopal"

print(dis)

del dis["name"]
print(dis)

