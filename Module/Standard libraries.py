# Operating system interface
import os

dir(os)  # Returns a list of all module functions
help(os)  # Returns an extensive manual page created from the module's docstrings
os.path.exists("file_path")  # True or False
os.path.isfile("file_path")
os.path.isdir("dir_path")
os.replace("src", "dst")  # Move a file or a directory
os.remove("path")  # Delete a file or a directory
os.rmdir("empty_dir")

# File wildcards
import glob

# Provides a function for making file lists from directory wildcard searches
glob.glob("*.py")

# Command Line Arguments
import sys

print(sys.argv)  # A list of the command line arguments when executing a script

# Mathematics and random
import math, random

math.log(10)
math.cos(math.pi)
random.choice(["apple", "pear", "banana"])
random.sample(range(100), 10)  # 10 samples from 0 - 99
random.random()  # random float
andom.randrange(6)  # random integer chosen from range(6)


# Statistics
import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)

# Internet access
# urllib.request for retrieving data from URLs
from urllib.request import urlopen

with urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as response:
    for line in response:
        line = line.decode()  # Convert bytes to a str
        print(line)

# Dates and Times
from datetime import date

now = date.today()
birthday = date(1999, 7, 30)
age = now - birthday
age.days


# Testing
import unittest

# Regular expression
import re
