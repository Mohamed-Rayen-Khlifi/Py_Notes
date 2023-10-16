#Normal String
" " or ' '

#Multiline String / Doc String (Accessed by function_name.__doc__)
""" """  or ''' '''

#Escape Sequences
"""
\n
\t
\\
\"
\'
"""

#Formatted string
var = 'Rayen'
f'{var} is inside a string' #'Rayen is inside a string'
# Field width
f'{var:number} is inside a string' #The field for the var value is going to have a width of number

#Raw string
r'C:\some\name' #C:\some\name

#Format method
'{}'.format(12) #'12'
'{} {}'.format('Rayen', 'Khlifi') #'Rayen Khlifi'
'{0} {0} {1}'.format('Happy','Birthday') #'Happy Happy Birthday'
'{first} {last}'.format(first='Rayen',last='Khlifi') #'Rayen Khlifi'

#Acces element number i
i = 0
print("String"[i]) #S

#Concatenation
s1 = 'Happy'
s2 = 'Birthday'
res = s1 + ' ' + s2 #'Happy Birthday'

#Multiplication
symbol = '<'
symbol *= 5 #'<<<<<'

#Stripping white spaces
s1.strip() 
s1.lstrip()
s1.rstrip()

#Changing character case
s1.capitalize() #Capitalizes the first letter of s1
s1.title() #Capitalizes all of s1
s1.upper() 
s1.lower()

#Searching for substrings
start_index = 3
end_index = 10
s1.count('Searched text', start_index, end_index)
s1.index('Searched text') #Returns value error if not found
s1.rindex('Searched text') 
s1.find('Searched text') #Returns -1 if not found
s1.rfind('Searched text')

#Starts with and ends with
s1.startswith('start text')
s1.endswith('end text')


#Replacing substrings
s1.replace('substring to match', 'replacement') 

#Splitting strings
s1.split() #Splits based on white spaces
s1.split('delimiter criteria') #Splits based on that string  criteria

#Partitionning strings
'Rayen: 20, 17, 18'.partition(': ') #('Rayen', ':', '20, 17, 18')
'Rayen: 20, 17, 18'.rpartition(': ') #('20, 17, 18', ':', 'Rayen'0)

#Joinning strings
list_of_strings = ['Ray', 'Em']
'delimiter to join the strings by'.join(list_of_strings)

#Splitting lines
lines = "first line\nsecond line\nthird line\n"
lines.splitlines() #['first line', 'second line', 'third line']
lines.splitlines(True) #['first line\n', 'second line\n', 'third line\n']

#Other methods
s1.isnumeric()
s1.isalnum()
s1.isspace() 
s1.isidentifier()

#Comparaison between strings
#Based on the first character's ASCII number; ord function (lexigraphical)
#We can use all the mathematical operators