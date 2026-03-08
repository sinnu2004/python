

my_set = set([1,34,55,6,6,33,5,33])

my_set.remove(34)
print(my_set)

# my_set.remove(34)  it gives error 
my_set.discard(34)
print(my_set)