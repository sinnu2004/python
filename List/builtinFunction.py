# there are several built in function in list

my_list = [1,2,3,4]
print(my_list)

my_list.append(5)  # append elemebt at the end
print(my_list)

my_list.insert(0,5) # insert element at any position
print(my_list)

list2 = [5,6,7,8]
my_list.extend(list2)  # extend the list by adding a list,tuple, string, set or dictionary
print(my_list)

print(len(my_list))  # finding length of the list

my_list.remove(8)   # remove the element 
print(my_list)

my_list.pop(0)    # remove the element from the index
print(my_list)

my_list.sort()   # sort the list

my_list.reverse() # reverse the list 
print(my_list)

print(my_list.index(5))  # finding value of that index

print(my_list.count(5))  # couting the  number of value of the given value

del my_list[0]  # deleting element from the index
print(my_list)



my_list.clear()   # clear all the values and make it empty
print(len(my_list))

# li = [1,"hell", 2, "workd"]  # type error 
# li.sort()

lst = [1,2,3]
st = ("hello")
lst.extend(st)
print(lst)
lst.append([4,5])
print(lst)
print(type(lst))
lst.reverse()
print(lst)


