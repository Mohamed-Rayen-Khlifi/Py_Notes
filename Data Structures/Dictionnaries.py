#Declaration
# Unordered collections of key-value pairs
# Keys must be immutable they can either be int or str
# Values can be mutable or immutable
dict = {'French': 'fr', 'English':'en', 
        'Italy':'it', 'Tunisia': 'tn'}
dict2 = {}
dict3 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict4 = dict(sape=4139, guido=4127, jack=4098)

#Iterating
# These methods return iterable objects, we can transform them into lists or tuples using their respectives constructors
dict.items()  #The items method returns each key value pair as a tuple pair
dict.keys()  #Its a view to the dictionnary; it looks at the real time data of the dictionnary not a copy
dict.values() #Same as keys

#Acces a value
dict['Key']
dict.get('Key','Error Value') #By default, if no error value argument is provided, get returns None

#Assign a value to a certain key
dict['Key'] = 'Value' #If the key doesnt exist, it will create it in the dictionnary and assign its value

#Removing elements
dict.pop('Key')
del dict['Key']

#Update
# The update methods can take a dictionnary with one or many elements
dict.update({'New_Key':'Value'}) #Add a new pair
dict.update({'Existing Key':'Value'}) #Update the existing pair




