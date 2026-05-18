# Program to demonstrate file handling

# Writing to file
with open("sample.txt", "w") as f:
    f.write("Hello Python\n")
    f.write("File Handling Example\n")

# Reading file
with open("sample.txt", "r") as f:
    print("File Content:")
    print(f.read())

# Appending to file
with open("sample.txt", "a") as f:
    f.write("Appending new line\n")

# Reading line by line
with open("sample.txt", "r") as f:
    print("\nReading line by line:")
    for line in f:
        print(line.strip())