# Program to demonstrate exception handling

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

else:
    print("Division successful")

finally:
    print("Program execution completed")