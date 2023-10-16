#Exceptions come in different types,
#Handling exceptions so they do not interrupt the normal flow of a program
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (ValueError, NameError):
        print("Oops!  That was no valid number.  Try again...")

    except TypeError as e:
        print("Wrong type")
    else: 
        print('This only executes if no exceptions were caught')
    finally: 
        print('This will always execute even if any or no exceptions occur')
