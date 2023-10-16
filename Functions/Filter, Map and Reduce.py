# We can pass them named functions or lambdas as arguments
# The filter and map functions are lazy functions, they return an iterator, so we have to use the list() constructor to iterate over the elements
# The reduce function takes a sequence of values and returns one value

sequence_of_elements = []
sequence_of_elements = ()
sequence_of_elements = ""

def even(x):
    return x % 2 == 0

def square(x):
    return x**2

#Filtering
list(filter(even, sequence_of_elements))

[item for item in sequence_of_elements if even(item)]

list(filter(lambda x: x % 2 == 0, sequence_of_elements))

#Mapping
list(map(square, sequence_of_elements))

[item**2 for item in sequence_of_elements]

list(map(lambda x: x**2, sequence_of_elements))

#Reducing
#Initial is the initial value we can use it or skip it
#This produces the product of all the elements in the sequence of elements provided
from functools import reduce
produit = reduce(lambda x, y: x * y, sequence_of_elements, initial=1)


