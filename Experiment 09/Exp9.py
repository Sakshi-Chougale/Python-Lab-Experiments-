# Program to demonstrate inheritance

# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

# Child class (Single Inheritance)
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print("Marks:", self.marks)

# Multiple Inheritance
class Sports:
    def sport(self):
        print("Plays Cricket")

class Result(Student, Sports):
    def final_result(self):
        print("Final Result Generated")

# Object creation
obj = Result("Sakshi", 90)

obj.show()
obj.display()
obj.sport()
obj.final_result()