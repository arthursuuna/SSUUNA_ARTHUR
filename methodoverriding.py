# Base class
class Employee:
    def describe_role(self):
        print("I am an employee of the company.")

# Subclass that overrides the method
class Manager(Employee):
    def describe_role(self):
        print("I am a manager. I oversee teams and operations.")

# Testing
emp = Employee()
mgr = Manager()

emp.describe_role()   # Output: I am an employee of the company.
mgr.describe_role()   # Output: I am a manager. I oversee teams and operations.
