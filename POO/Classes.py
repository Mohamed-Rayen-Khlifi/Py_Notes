# Definition
class Creature:
    def __init__(self, status):
        self.status = status

    def greet(self):
        pass


class Another_Base_Class:
    pass


class Person(Creature, Another_Base_Class):  # Inheritance
    # The search for attributes is first done with the Derived class Person, then it is searched for in the left most base class and recursively in its base classes and if its not there, then the search is done on the class to the right in the same manner
    # All classes inherit from Object
    Nationnality = "Tunisian"  # Class variable (Shared)
    # If the shared variable is a mutabale object like lists than be careful
    # Because changing it for one instance will result in changing it in the others as well

    __Status = "Alive"  # Private variable

    def __init__(
        self, name, age, job, status
    ):  # Constructor initializes instance variables
        super().__init__(status)
        self.name = name  # Instance Variable
        self.age = age
        self.job = job

    def used_to_be_called(self):
        pass

    # Overrides the greet method in the base class Creature

    def greet(self):
        # Methods may call other methods
        self.used_to_be_called()
        print(
            f"""
        Hi my name is {self.name}, I'm {self.age} years old and I'm a {self.job}. 
        Nice to meet you!
        """
        )


Rayen = Person("Rayen", 24, "Software Engineer")
Rayen.greet()

# Built-in functions that work with inheritance
print(isinstance(Rayen, Person))  # Rayen is an instance of Person
print(issubclass(Person, Creature))  # Person is a subclass(inherits from) of Creature
