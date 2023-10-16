#Description of a function
"""Function?"""
#Function description and its source code 
"""Function??""" 

#Functions are objects
#We can assign them to variables
#We canpass them to functions 
#We canreturn them from functions

#Return value of a function
#Fonction always returns something
#If no return statemnt is provided, the function returns None object by default

#Declartion
def fn(arguments):
    #Body
    #Possible return statement
    return 
f = fn
f(1)

#Default argument values
# By default, arguments may be passed to a Python function either by position or explicitly by keyword
# If we use arg= and arg2= when we are calling the function they are called keywords (arguments preceeded by identifier)
# Unlike positional arguments, the order of these arguments doesn't matter
def fn2(arg=0, arg2=1):
    return
fn2() #arg=0, arg2=1
fn2(1) #arg=1, arg2=1
fn2(1,2) == fn(arg=1, arg2=2) == fn(arg2=2, arg=1) #arg=1, arg2=1, 
# The default value is evaluated only once
# So if the default is mutable, it can make a difference per example
def f(a, L=[]):
    L.append(a)
    return L
print(f(1)) #[1]
print(f(2)) #[1, 2]
print(f(3)) #[1, 2, 3]



#Arbitrary argument list
# This argument must be the last one in the parameter list in case we have other arguments
# These arguments will be wrapped up into a tuple 
# If we wanna use an argument after the *args, it has to be called using its specific argument keyword
def fn3(arg1, arg2, *args):
    return args


#Passing arguments by value
# Fonction takes a copie of the argument object and works with it 
# This means the function doesnt altert the value of the original object


#Passing arguments by reference (Python's case)
# Fonction takes the @ of the original argument object and alters it (Only if the object is mutabale)
# If the object is immutabale, the function creates another object and works on it

#Object identifier in memory
id(fn) 
# Same object or not?
fn is fn2 #Is like saying id(fn) == id(fn2)

