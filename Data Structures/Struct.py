from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


Rayen = Employee("Rayen", "Computer science", 1000)
