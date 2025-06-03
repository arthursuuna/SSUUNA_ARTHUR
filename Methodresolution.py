class Person:
    def who_am_i(self):
        print("I am a Person")

class Employee(Person):
    def who_am_i(self):
        print("I am an Employee")

class Student(Person):
    def who_am_i(self):
        print("I am a Student")

class WorkingStudent(Employee, Student):
    pass

# Create an object of WorkingStudent
ws = WorkingStudent()
ws.who_am_i()

# Show the method resolution order
print(WorkingStudent.__mro__)
