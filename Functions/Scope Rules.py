#Global scope
x = 10 

#Local scope
def doesnt_modify():
    x = 13    
    print(x) #13

print(x) #10

#Using a global variable in a function
def modifies():
    global x 
    x = 13
    print(x) #13

print(x) #13

