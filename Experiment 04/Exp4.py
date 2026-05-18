# Program for list operations

my_list = [10, 20, 30]

print("Original List:", my_list)

my_list.append(40)
print("After append:", my_list)

my_list.insert(1, 50)
print("After insert:", my_list)

my_list.remove(10)
print("After remove(10):", my_list)

my_list.pop()
print("After pop():", my_list)

my_list.reverse()
print("After reverse:", my_list)

print("Indexing:", my_list[0])
print("Slicing:", my_list[1:3])

my_list.sort()
print("Sorted List:", my_list)