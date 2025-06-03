# Superclass: Person
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.id_number}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, id_number, course):
        super().__init__(name, age, id_number)
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, id_number, subject):
        super().__init__(name, age, id_number)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, id_number, department):
        super().__init__(name, age, id_number)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

# Create objects and display their info
student = Student("Alice", 20, "ST123", "Computer Science")
lecturer = Lecturer("Dr. Smith", 45, "LE456", "Artificial Intelligence")
staff = Staff("John Doe", 38, "SF789", "Administration")

# Test method
print("\n--- Student Info ---")
student.display_info()

print("\n--- Lecturer Info ---")
lecturer.display_info()

print("\n--- Staff Info ---")
staff.display_info()
