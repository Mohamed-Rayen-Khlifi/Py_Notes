#Declaration
a_tuple = ()
b_tuple = ()
one_value = (1,) 
multiple_values = 1, 2, 3 #Parenthese not mandatory, however the comma is 

#Accessing elements 
i = 0
print(a_tuple[i])

#We can changes sub elements in a tuple, if that sub element is mutabale 
seq = (1, 2, [1, 2, 3])
seq[1] = 2 #Doesnt work
seq[2][1] = 2 #Works