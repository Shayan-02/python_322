# a = []
# print(type(a))

# b = list()
# print(type(b))

lst = [1, 2, 3, 4, 5]

# add

lst.append(6) # add to end of the list
print(lst)

lst.insert(0, 0)

# add in index of the list
lst.insert(2, "ali rezaee")
print(lst)

# delete

lst.pop() # delete the last item of list

print(lst)

lst.pop(4) # delete item in index of list

print(lst)

lst.remove("ali rezaee") # delete item by that value

print(lst)

