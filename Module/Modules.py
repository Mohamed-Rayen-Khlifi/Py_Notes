# A file containing python code such as functions and classes, it is used with modular programming, which aims to seperate a program into parts
# Module description
"""Module?"""

# Module description and its source code
"""Module??"""

# Import module name
# This does not add the names of the functions defined in math directly to the current namespace
# It only adds the module name math, and using that module name we can access the functions in it
import math as mt

mt.pi

# Import definitions from the module
from random import randrange, choices
from matplotlib import *

# How to create a module
# Add this to the end of the module file
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
