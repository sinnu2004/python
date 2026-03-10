dis = {
    "name": "saurabh",
    "age" : 22,
    "address": "INdore",
    "college": "SOIT",
    "Location": "Bhopal"
}

for x in dis:
    print(x,end=" ")
    
for x in dis.values():
    print(x,end=" ")
    
for x in dis:
    print(dis[x],end=" ")
    
for x in dis.keys():
    print(x,end=" ")