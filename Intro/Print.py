arg1 = 1
arg2 = 2
arg3 = 3
text = 'Hello'

#Transforms all the arguments to strings, and concatenates them with spaces
print(arg1,arg2,arg3)

#Concatenates arguments with spaces only if all arguments are str  
print(str(arg1) + str(arg2) + str(arg3))

#End is by default '\n'
print(text, end=' ')

#Sep is the seperator between resaults, its a whitespace by default  
print(arg1, arg2, arg3, sep=' ')

