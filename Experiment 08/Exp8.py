# Program to demonstrate classes and objects

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # Method to display details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    # Method to calculate grade
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

# Creating object
s1 = Student("Sakshi", 20, 85)

# Accessing methods
s1.display()
print("Grade:", s1.get_grade())