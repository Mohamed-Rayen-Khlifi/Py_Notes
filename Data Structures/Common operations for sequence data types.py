#Comprehensions
# List
[item.upper() for item in a_list]
[item for item in range(10) if item % 2 == 0]
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[num for elem in [[1,2,3], [4,5,6], [7,8,9]] for num in elem]
# Tuple
(item**2 for item in range(20))
# Dictionnary
{v:k for k,v in dict.items()} 
# Sets
{n for n in range(10)}

#Built in functions
# Returns a new sequence object contains the new content and doesnt modify the original sequence object
reversed and sorted
# Returns one value
sum, max, min, len

#Common methods
copy() and clear()

#Slicing
#These methods are used with Strings, Lists, Sets and Tuples
#They are of this form: sequence[start:end:step] 
#All slice operations return a new sequence containing the requested elements
#The start from the left is index 0
#The start from the right is index -1
my_list = [1, 2, 3, 4]
my_tuple = ('a', 'b', 'c', 'd')
my_string = 'Rayen'
my_list[:] #Whole list (0 to len(my_list))
my_tuple[:5] #From the start(0) til index 4
my_string[1:] #From index 1 to the end of the string (1 to len(my_string))
my_list[::-1] #Reversed list

#Enumerate function
#When looping through a sequence, the position index and corresponding value can be retrieved at the same time 
for index, value in enumerate(['tic', 'tac', 'toe']):
    print(index, value)

#Zip function
#To loop over two or more sequences at the same time
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#Unpacking
# Sequences that can be unpacked include lists, tuples, strings, range function or enumerate function
# Number of elements on the right should be equal to the number of values to unpack
student = ("Sue", 23, [10, 15, 20])
name, age, grades = student
