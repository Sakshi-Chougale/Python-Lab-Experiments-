# Program to demonstrate tuple operations

# Creating a tuple
t = (10, 20, 30, 40, 10, 50)

print("Original Tuple:", t)

# Indexing
print("First element:", t[0])
print("Last element:", t[-1])

# Slicing
print("Elements from index 1 to 4:", t[1:5])

# Length of tuple
print("Length:", len(t))

# Count occurrences
print("Count of 10:", t.count(10))

# Find index
print("Index of 30:", t.index(30))

# Concatenation
t2 = (60, 70)
t3 = t + t2
print("After concatenation:", t3)

# Repetition
print("Tuple repeated:", t * 2)

# Membership test
print("Is 20 present?", 20 in t)
print("Is 100 present?", 100 in t)

# Iteration
print("Elements in tuple:")
for i in t:
    print(i, end=" ")
