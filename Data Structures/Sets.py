#Declaration
# Unordered collections of unique values
# If a value is duplicated in the declaration, the duplicate is removed by Python
# Using set() on a sequence eliminates duplicate elements
colors = {"orange", "green", "blue", "red"}
alphabet = set('abcdefghijklmnpqrstuvwxyz')

#Subsets and supersets
# Their arguments can be sets or any sequence
super_set = {}
sub_set = {}
super_set.issuperset(sub_set)  
subset.issubset(super_set)

#Mathematical Methods and Operations
# Union
super_set | sub_set
super_set.Union() #Takes list argument
# Intersection
super_set & sub_set
super_set.Intersection() #Takes list argument
# Difference
super_set - sub_set
super_set.Difference() #Takes list argument
# IsDisjoint
sub_set.IsDisjoint(sub_set)

#Methods
super_set.update(range(10)) # Change the values of the super_set to host the argument
super_set.add(10) # Will add the argument to the set
super_set.remove(10) #Will remove the key 10 if it exists or it will throw and exception
super_set.discard(10)