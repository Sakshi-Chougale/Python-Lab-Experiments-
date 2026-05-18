# Program to demonstrate dictionary operations
# Creating a dictionary
student = {
    "name": "Sakshi",
    "age": 20,
    "course": "B.Tech"
}

print("Original Dictionary:", student)
# Accessing values
print("Name:", student["name"])

# Using get() method
print("Age using get():", student.get("age"))

# Adding new key-value pair
student["city"] = "Kolhapur"
print("After adding city:", student)

# Updating value
student["age"] = 21
print("After updating age:", student)

# Removing element using pop()
student.pop("course")
print("After removing course:", student)

# Removing last inserted item
student.popitem()
print("After popitem():", student)

# Keys, Values, Items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Copy dictionary
new_student = student.copy()
print("Copied Dictionary:", new_student)

# Update dictionary
student.update({"gender": "Female"})
print("After update():", student)

# Loop through dictionary
print("Dictionary elements:")
for key, value in student.items():
    print(key, ":", value)