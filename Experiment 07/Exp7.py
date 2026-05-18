
# Program to demonstrate built-in and user-defined functions

# Built-in Functions
numbers = [10, 20, 30, 40]

print("List:", numbers)
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# User-defined Functions

# Function with parameters and return value
def add(a, b):
    return a + b

# Function without return value
def greet(name):
    print("Hello", name)

# Function with default argument
def power(x, y=2):
    return x ** y

# Function Calls

print("\nAddition:", add(5, 3))
greet("Sakshi")
print("Power (default):", power(4))      # square
print("Power (custom):", power(2, 3))    # cube

