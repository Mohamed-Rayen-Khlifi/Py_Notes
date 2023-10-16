#Declaration
a_list = []
b_list = []
for i in range(1, 6):
    a_list += [i]  # What's on the right should be an iterable sequence of elements
                   # Such as a String, a list or a tuple
b_list += "birthday" # ['b','i','r','t','h','d','a','y']

#List Concatination
con_list = a_list + b_list

#Accessing Elements 
i = 0
print(a_list[i])

#Modifying lists with slicing
my_list = [1, 2, 3, 4]
new_list = ["This is a new", "List"]
my_list[0:3:1] = new_list
my_list = new_list
# Slicing leaves the same object but changes its values
# However assignment changes the object that the list variable references (A new physical object with different @)


#del statement
# Can only be used with lists or variables and not tuples or strings
# Same as slicing, it doesnt create a new object, it modifies the one being referenced by the variable
del my_list[0:2:1]
del my_list # Deletes the variable from the interactive session
del my_list[0] #Del can also be used to delete an entire variable


#Sorting
# Method for the list object and makes the list variable reference a new object after sort
# Sorting strings is based on the ASCII code of the first character
new_list.sort()
new_list.sort(reverse=True)
new_list.sort(key=lambda item: item[2])

#Reverse a list
my_list.reverse()

#Searching
# Return the first index of the occurence of the value or an exception error
my_list.index(value, start, end)

#Adding elements
index = 0
iterable = [1, 2, 3]
# One element at a certain index
new_list.insert(index, value)
# One element at the end of the list
new_list.append(value)
# Multiple elements
new_list.extend(iterable)  # One argument only, iterable is a sequence of objects

#Removing elements
# Remove based on item value
new_list.remove(value)
# Remove the last item
new_list.pop()

#Occurences of elements
new_list.count(value)

